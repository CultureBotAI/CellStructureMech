# PR 2367: current-input review of ten records and adversarial follow-up

- Review: 20261103T150238Z-pr2367-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T14:50:16.680122Z
- Finished UTC: 2026-11-03T15:02:38Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of the complete ten-record PR2367 cohort. Two stale records are substantively refreshed and ten explicit structured-source applicability exclusions corrected. Eight inherited and two new scientific findings remain open (five major, five minor), with exact source scopes and lineage: six targets need curation and four receive qualified positive assessments. Original review observations and all scientific records remain unchanged.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 144d19dec1ea5ad91cc299a6711e3fec9c157056. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 07860cdd96065310a36fb2173dbcee46b957e995.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base f23e1970804e4f93de15a4ae275af84d48e6ce14.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009514 | data/structures/membrane_organelle/glyoxysome.yaml | maintained | glyoxysome |
| GO:0005794 | data/structures/membrane_organelle/golgi_apparatus.yaml | maintained | Golgi apparatus |
| GO:0005798 | data/structures/membrane_organelle/golgi_associated_vesicle.yaml | maintained | Golgi-associated vesicle |
| GO:0030660 | data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml | maintained | Golgi-associated vesicle membrane |
| GO:0031985 | data/structures/membrane_organelle/golgi_cisterna.yaml | maintained | Golgi cisterna |
| GO:0032580 | data/structures/membrane_organelle/golgi_cisterna_membrane.yaml | maintained | Golgi cisterna membrane |
| GO:0005796 | data/structures/membrane_organelle/golgi_lumen.yaml | maintained | Golgi lumen |
| GO:0000139 | data/structures/membrane_organelle/golgi_membrane.yaml | maintained | Golgi membrane |
| GO:0046859 | data/structures/membrane_organelle/hydrogenosomal_membrane.yaml | maintained | hydrogenosomal membrane |
| GO:0042566 | data/structures/membrane_organelle/hydrogenosome.yaml | maintained | hydrogenosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0009514 | passed | True | GO:0009514 | Documented focused command passed. |
| validate-strict GO:0009514 | passed | True | GO:0009514 | Documented focused command passed. |
| validate GO:0005794 | passed | True | GO:0005794 | Documented focused command passed. |
| validate-strict GO:0005794 | passed | True | GO:0005794 | Documented focused command passed. |
| validate GO:0005798 | passed | True | GO:0005798 | Documented focused command passed. |
| validate-strict GO:0005798 | passed | True | GO:0005798 | Documented focused command passed. |
| validate GO:0030660 | passed | True | GO:0030660 | Documented focused command passed. |
| validate-strict GO:0030660 | passed | True | GO:0030660 | Documented focused command passed. |
| validate GO:0031985 | passed | True | GO:0031985 | Documented focused command passed. |
| validate-strict GO:0031985 | passed | True | GO:0031985 | Documented focused command passed. |
| validate GO:0032580 | passed | True | GO:0032580 | Documented focused command passed. |
| validate-strict GO:0032580 | passed | True | GO:0032580 | Documented focused command passed. |
| validate GO:0005796 | passed | True | GO:0005796 | Documented focused command passed. |
| validate-strict GO:0005796 | passed | True | GO:0005796 | Documented focused command passed. |
| validate GO:0000139 | passed | True | GO:0000139 | Documented focused command passed. |
| validate-strict GO:0000139 | passed | True | GO:0000139 | Documented focused command passed. |
| validate GO:0046859 | passed | True | GO:0046859 | Documented focused command passed. |
| validate-strict GO:0046859 | passed | True | GO:0046859 | Documented focused command passed. |
| validate GO:0042566 | passed | True | GO:0042566 | Documented focused command passed. |
| validate-strict GO:0042566 | passed | True | GO:0042566 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | All ten explicit expression-only exclusions are corrected using complete-record molecular/pathway assertions. Fresh complete official catalogue responses and bounded searches for Saccharomyces, Neurospora and Trichomonas host coverage yield no matching datasets. No unmatched host proxy or unsupported downstream query is used. Noncoverage is not biological absence. Historical adapter-runner unavailability keeps its actual timestamp and is not represented as a fresh execution. |
| Independent claim-level source review | passed | True | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native glyoxysome UniProt verify check | passed | True | GO:0009514 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native glyoxysome UniProt causal check | passed | True | GO:0009514 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi apparatus UniProt verify check | passed | True | GO:0005794 | Read-only native command returned zero. Six reviewed S. cerevisiae S288C examples (OCH1/P31755, MNN1/P39106, KRE2/P27809, SED5/Q01590, TLG2/Q08144, SEC22/P22214) and two COVERED nodes. Identity does not establish that the SNARE cohort is one complex or certify every mechanistic assertion. |
| Native Golgi apparatus UniProt causal check | passed | True | GO:0005794 | Read-only native command returned zero. Six reviewed S. cerevisiae S288C examples (OCH1/P31755, MNN1/P39106, KRE2/P27809, SED5/Q01590, TLG2/Q08144, SEC22/P22214) and two COVERED nodes. Identity does not establish that the SNARE cohort is one complex or certify every mechanistic assertion. |
| Native Golgi-associated vesicle UniProt verify check | passed | True | GO:0005798 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi-associated vesicle UniProt causal check | passed | True | GO:0005798 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi-associated vesicle membrane UniProt verify check | passed | True | GO:0030660 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi-associated vesicle membrane UniProt causal check | passed | True | GO:0030660 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi cisterna UniProt verify check | passed | True | GO:0031985 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi cisterna UniProt causal check | passed | True | GO:0031985 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi cisterna membrane UniProt verify check | passed | True | GO:0032580 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi cisterna membrane UniProt causal check | passed | True | GO:0032580 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi lumen UniProt verify check | passed | True | GO:0005796 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi lumen UniProt causal check | passed | True | GO:0005796 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi membrane UniProt verify check | passed | True | GO:0000139 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native Golgi membrane UniProt causal check | passed | True | GO:0000139 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native hydrogenosomal membrane UniProt verify check | passed | True | GO:0046859 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native hydrogenosomal membrane UniProt causal check | passed | True | GO:0046859 | Read-only native command returned zero. This record has no represented protein examples and no typed molecular nodes; narrative molecular/pathway assertions are assessed separately. |
| Native hydrogenosome UniProt verify check | passed | True | GO:0042566 | Read-only native command returned zero. No protein examples; three NO_GENE_SYMBOLS typed nodes are anchored to import machinery, pyruvate-metabolism enzymes and FeS machinery class components. This is not individual protein verification or source-level localization proof. |
| Native hydrogenosome UniProt causal check | passed | True | GO:0042566 | Read-only native command returned zero. No protein examples; three NO_GENE_SYMBOLS typed nodes are anchored to import machinery, pyruvate-metabolism enzymes and FeS machinery class components. This is not individual protein verification or source-level localization proof. |

## Scientific And Domain Assessments

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0031985.

Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. Both actual native commands exit0; no hidden family or necessity certification.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0031985.

Original pair validates/renders; all 14 historical inputs match its source; target unchanged. No historical group/neighbor/category finding is terminally resolved. Exact cisterna F1 lineage retained where applicable.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0031985.

All current fields, evidence, history, discussions and graphs inspected. No target image assets, quantitative properties, associated_traits or verbatim snippets. Empty optional accession inventories and unset exact lipid chemistry are not invented completeness defects. PROPOSED remains unchanged.

### Positive pathway trigger and matched-host assessment

scope: supported. Targets: GO:0031985.

Explicit current cisternal maturation with resident-marker identity transitions triggers assessment. Original check is an unsupported expression-only exclusion, not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module query or unrelated-organism proxy is justified. Historical unavailable runner is separately dated; source fallback is complete within declared tiers.

### Yeast species and experimental scope

scope: supported. Targets: GO:0031985.

NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured prevalence. Losev and Matsuura-Tokita directly examine budding-yeast cisternal marker transitions; canonical imaging example is supported. Exact supplement strain constructions and universal all-eukaryote dynamics are not inferred.

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0032580.

Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. Both actual native commands exit0; no hidden family or necessity certification.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0032580.

Original pair validates/renders; all 17 historical inputs match its source; target unchanged. No historical group/neighbor/category finding is terminally resolved. Exact cisterna F1 lineage retained where applicable.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0032580.

All current fields, evidence, history, discussions and graphs inspected. No target image assets, quantitative properties, associated_traits or verbatim snippets. Empty optional accession inventories and unset exact lipid chemistry are not invented completeness defects. PROPOSED remains unchanged.

### Positive pathway trigger and matched-host assessment

scope: supported. Targets: GO:0032580.

Explicit current cisternal maturation with resident-marker identity transitions triggers assessment. Original check is an unsupported expression-only exclusion, not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module query or unrelated-organism proxy is justified. Historical unavailable runner is separately dated; source fallback is complete within declared tiers.

### Yeast species and experimental scope

scope: supported. Targets: GO:0032580.

NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured prevalence. Losev and Matsuura-Tokita directly examine budding-yeast cisternal marker transitions; canonical imaging example is supported. Exact supplement strain constructions and universal all-eukaryote dynamics are not inferred.

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0005796.

Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. Both actual native commands exit0; no hidden family or necessity certification.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0005796.

Original pair validates/renders; all 16 historical inputs match its source; target unchanged. No historical group/neighbor/category finding is terminally resolved. Exact cisterna F1 lineage retained where applicable.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0005796.

All current fields, evidence, history, discussions and graphs inspected. No target image assets, quantitative properties, associated_traits or verbatim snippets. Empty optional accession inventories and unset exact lipid chemistry are not invented completeness defects. PROPOSED remains unchanged.

### Positive pathway trigger and matched-host assessment

scope: supported. Targets: GO:0005796.

Explicit current VRG4-dependent GDP-mannose import and lumenal glycosylation triggers assessment. Original check is an unsupported expression-only exclusion, not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module query or unrelated-organism proxy is justified. Historical unavailable runner is separately dated; source fallback is complete within declared tiers.

### Yeast species and experimental scope

scope: supported. Targets: GO:0005796.

NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured prevalence. Primary Dean abstract supports the yeast Golgi vesicle/canonical nucleotide-sugar example; exact experimental strain and quantitative transport data are not independently certified.

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0000139.

Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. Both actual native commands exit0; no hidden family or necessity certification.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0000139.

Original pair validates/renders; all 17 historical inputs match its source; target unchanged. No historical group/neighbor/category finding is terminally resolved. Exact cisterna F1 lineage retained where applicable.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0000139.

All current fields, evidence, history, discussions and graphs inspected. No target image assets, quantitative properties, associated_traits or verbatim snippets. Empty optional accession inventories and unset exact lipid chemistry are not invented completeness defects. PROPOSED remains unchanged.

### Positive pathway trigger and matched-host assessment

scope: supported. Targets: GO:0000139.

Explicit current COPI coat assembly and COPI-dependent vesicle budding triggers assessment. Original check is an unsupported expression-only exclusion, not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module query or unrelated-organism proxy is justified. Historical unavailable runner is separately dated; source fallback is complete within declared tiers.

### Yeast species and experimental scope

scope: supported. Targets: GO:0000139.

NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured prevalence. Losev and Matsuura-Tokita directly examine budding-yeast cisternal marker transitions; canonical imaging example is supported. Exact supplement strain constructions and universal all-eukaryote dynamics are not inferred.

### Whole cisterna versus membrane

identity: supported. Targets: GO:0031985.

GO0031985 denotes a flattened membrane-bounded Golgi subcompartment, matching native kind and definition; its boundary GO0032580 remains distinct. Parent0098791 and part_of0005794/has_part0032580 are appropriately scoped.

### Reviewed label-only aggregate bilayer

grounding: supported. Targets: GO:0031985.

The LIPID row deliberately names aggregate boundary material without guessing a chemical CURIE or individual lipid necessity. ESSENTIAL denotes collective membrane boundary at this coarse level. This valid material row does not make the whole cisterna its identity.

### Whole-compartment component_ref mismatch

graph: concern. Targets: GO:0031985.

The graph node golgi_cisterna denotes the complete membrane-bounded compartment GO0031985 but component_ref points to golgi_cisternal_lipid_bilayer. That component denotes boundary lipid material, while the separate golgi_cisterna_membrane node already denotes the correct GO0032580 boundary. The schema defines component_ref as identifying a node that is one of the record’s components, so this join incorrectly equates whole compartment and lipid constituent.

### Source-supported cisternal maturation

evidence: supported. Targets: GO:0031985.

Early-to-late resident-marker transitions, membrane bounding and Golgi parthood are supported. Primary imaging supports the described yeast maturation sequence; not exclusive cargo transport, exact molecular recycling or all-Golgi kinetics. The component_ref mismatch does not invalidate these biological edges.

### Specific cisternal membrane and broader generic parent

identity: supported. Targets: GO:0032580.

GO0032580 is the membrane surrounding a flattened central Golgi cisterna; part_of0031985 is supported. Parent0000139 is supported by definitions as a membrane of a Golgi compartment, although current is_a-only native ancestry does not explicitly include it; no direct GO edge asserted.

### Boundary component correspondence

grounding: supported. Targets: GO:0032580.

Reviewed-label-only bilayer constituent and the membrane-node component_ref describe the boundary material. Unlike whole-cisterna F1, this does not equate a whole compartment with lipid. No arbitrary specific chemical identity or universal lipid species is supplied.

### Boundary topology and maturation context

graph: supported. Targets: GO:0032580.

NONMECHANISTIC membrane-bounds-cisterna, cisterna-part-of-Golgi and cisterna-undergoes-marker-maturation edges are supported by exact authority and inspected yeast primary PDFs. Broad maturation does not assert membrane fusion molecular mechanism.

### Golgi lumen identity and synonyms

identity: supported. Targets: GO:0005796.

GO0005796 and SL0133 identify Golgi apparatus/complex lumen, the interior bounded by Golgi compartments including networks. SUBCELLULAR_REGION, is_a0070013 and part_of0005794 are consistent. It is neither whole Golgi nor membrane.

### Sparse lumen with boundary transporter context

grounding: supported. Targets: GO:0005796.

No stable constituent inventory is asserted. Vrg4 is properly described as membrane-localized transport support supplying lumen substrate; it is not fabricated as stable lumen material. The existing resolved boundary discussion is consistent with current source but no historical issue completion is re-certified.

### GDP-mannose import and glycosylation access

evidence: supported. Targets: GO:0005796.

Dean primary abstract supports Golgi-vesicle GDP-mannose import defects in vrg4 mutants and corresponding mannosylation defects. This supports lumenal substrate access and the canonical example without claiming purified Vrg4 sufficiency or unique formation necessity.

### Three purely descriptive lumen relations

graph: supported. Targets: GO:0005796.

Lumen is_a organelle lumen, part_of Golgi and bounded by Golgi membrane are supported by current GO and SL0133 definitions. No uninspected molecular transport mechanism is encoded by these three NONMECHANISTIC edges.

### Generic Golgi membrane scope

identity: supported. Targets: GO:0000139.

GO0000139 denotes membranes surrounding any Golgi compartment, matching generic definition and exact apparatus synonym; parent0016020 is supported by ancestry and part_of0005794 by authority. Specific cisternal membrane remains a narrower boundary.

### Generic bilayer constituent correspondence

grounding: supported. Targets: GO:0000139.

Reviewed-label-only aggregate LIPID avoids guessing chemistry; the membrane-node component_ref remains at boundary material scope rather than whole-organelle identity. ESSENTIAL is collective boundary necessity, not every individual lipid species.

### Generic example retains budding-yeast scope

evidence: supported. Targets: GO:0000139.

Canonical Losev/Matsuura-Tokita yeast marker maturation remains supported by complete inspected primary text and captions. Generic membrane identity does not universalize experimental kinetics or imply every Golgi membrane matures identically.

### Coat assembly, budding and descriptive topology

graph: supported. Targets: GO:0000139.

Membrane part_of Golgi and bounds cisterna are valid topology. ARF/COPI recruitment and coat participation in budding are supported by Serafini primary abstract, GO and conditional Bremser reconstitution abstract. Broad mediates/drives language is read as functional participation, not coat-alone sufficiency, yeast-specific reconstitution, every Golgi compartment or a complete molecular mechanism.

### Explicit access and mechanism limits

evidence: unknown. Targets: GO:0031985.

Primary microscopy PDFs were read as main text/Methods/captions, not figure pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level where used; short DOI landing HTML is not body. Papanikou is secondary selected-section context. Exact lipid chemistry, exclusive transport route, quantitative generalization and individual component formation necessity remain unestablished.

### Explicit access and mechanism limits

evidence: unknown. Targets: GO:0032580.

Primary microscopy PDFs were read as main text/Methods/captions, not figure pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level where used; short DOI landing HTML is not body. Papanikou is secondary selected-section context. Exact lipid chemistry, exclusive transport route, quantitative generalization and individual component formation necessity remain unestablished.

### Explicit access and mechanism limits

evidence: unknown. Targets: GO:0005796.

Primary microscopy PDFs were read as main text/Methods/captions, not figure pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level where used; short DOI landing HTML is not body. Papanikou is secondary selected-section context. Exact lipid chemistry, exclusive transport route, quantitative generalization and individual component formation necessity remain unestablished.

### Explicit access and mechanism limits

evidence: unknown. Targets: GO:0000139.

Primary microscopy PDFs were read as main text/Methods/captions, not figure pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level where used; short DOI landing HTML is not body. Papanikou is secondary selected-section context. Exact lipid chemistry, exclusive transport route, quantitative generalization and individual component formation necessity remain unestablished.

### Exact whole/membrane identity and hierarchy

identity: supported. Targets: GO:0005794.

Current native GO names, definitions, synonyms and typed relations support the exact target and its broader parent/parthood. Apparatus/cisternae, complete vesicle and its membrane remain distinct. COPI and TGN are bounded child examples, not universal generic-class attributes.

### Yeast canonical scope and protein strain identity

scope: supported. Targets: GO:0005794.

Saccharomyces4932 is the named canonical species with qualitative COMMON occurrence. Native protein examples are S288C559292 identities, not proof every imaging/transport experiment used that strain. Yeast imaging and retrieval are kept separate from generic Golgi-derived coated-vesicle biochemical context.

### Components, physical assembly scope and grounding

grounding: concern. Targets: GO:0005794.

Six reviewed examples and bounded uniqueness claims match. Broad glycosylation-enzyme class remains allowed and label-only across distinct enzyme families. SNARE source attribution F1 remains; new complex retyping F3 needs correction because retained broad cohort is not the specific named physical assembly.

### Formation necessity versus function and boundary identity

evidence: unknown. Targets: GO:0005794.

Apparatus machinery has UNKNOWN essentiality. A defining membrane boundary is constitutive of the named membrane-bounded class, but this is not evidence each lipid species, coatomer subunit or SNARE is individually required for organelle assembly. Native annotations and transport-mutant assays are not exhaustive formation tests.

### Every current graph node and edge

graph: concern. Targets: GO:0005794.

Five NONMECHANISTIC FUNCTION edges checked. Membrane bounds cisterna, cisterna part_of apparatus and early-to-late marker transitions are supported. Glycosylation-enzyme compartment context is supported by review. The SNARE supports-maturation edge retains F1 source-attribution problem; it does not independently demonstrate each named actor is necessary.

### Entire maintained scope and optional slots

completeness: supported. Targets: GO:0005794.

Entire current file/history/discussions and original observation read. No tracked target image, quantitative physical property, trait link or snippet asserted. Unresolved exact lipid/family terms are not automatic defects. PROPOSED status retained and no historical/group/category issue is terminally disposed.

### Primary body, abstract and secondary scopes

evidence: supported. Targets: GO:0005794.

Losev/Matsuura genuine primary PDF main texts/Methods/captions were read independently from shared fresh snapshots, without pixels/movies/supplements. Papanikou full main BioC text is secondary review. Letourneur/Waters/Serafini and OCH1/SNARE supporting papers are complete primary abstracts only; exact access/assay limits retained.

### Frozen originals and actual native coverage

schema: supported. Targets: GO:0005794.

Original native validate/render passed with byte-identical Markdown, original target hash confirmed from frozen revision. Current verify/causal receipts are source-head bound; their actual nonempty or zero inventories are explicitly limited, not scientific proof.

### Explicit expression-only exclusion is unsupported

provenance: concern. Targets: GO:0005794.

Original check is present, not omitted, but excludes applicability because no expression-module inference is used. Current named proteins, coatomer/COPI retrieval and membrane-budding pathway assertions trigger actual coverage assessment under native policy. This is a bundle defect.

### Current exact-organism catalogue applicability

evidence: not_applicable. Targets: GO:0005794.

Complete fresh official catalogue has no Saccharomyces/cerevisiae/S288C organism/dataset match. No matched gene/module key or downstream summarize applies; an unrelated bacterial proxy would be inappropriate. Historical00:49Z runner limitation remains historical.

### Exact whole/membrane identity and hierarchy

identity: supported. Targets: GO:0005798.

Current native GO names, definitions, synonyms and typed relations support the exact target and its broader parent/parthood. Apparatus/cisternae, complete vesicle and its membrane remain distinct. COPI and TGN are bounded child examples, not universal generic-class attributes.

### Yeast canonical scope and protein strain identity

scope: supported. Targets: GO:0005798.

Saccharomyces4932 is the named canonical species with qualitative COMMON occurrence. Native protein examples are S288C559292 identities, not proof every imaging/transport experiment used that strain. Yeast imaging and retrieval are kept separate from generic Golgi-derived coated-vesicle biochemical context.

### Components, physical assembly scope and grounding

grounding: concern. Targets: GO:0005798.

F2 remains: molecular LIPID row is grounded to complete membrane GO0030660, which also propagates through component_ref. Correct has_part and membrane topology do not repair the distinct molecular/structure identity.

### Formation necessity versus function and boundary identity

evidence: unknown. Targets: GO:0005798.

Apparatus machinery has UNKNOWN essentiality. A defining membrane boundary is constitutive of the named membrane-bounded class, but this is not evidence each lipid species, coatomer subunit or SNARE is individually required for organelle assembly. Native annotations and transport-mutant assays are not exhaustive formation tests.

### Every current graph node and edge

graph: concern. Targets: GO:0005798.

Four NONMECHANISTIC FUNCTION edges preserve membrane parthood, GO-defined Golgi evagination, COPI is_a child and bounded retrograde retrieval. GO/primary abstract scopes support these descriptions; membrane component_ref identity propagates F2.

### Entire maintained scope and optional slots

completeness: supported. Targets: GO:0005798.

Entire current file/history/discussions and original observation read. No tracked target image, quantitative physical property, trait link or snippet asserted. Unresolved exact lipid/family terms are not automatic defects. PROPOSED status retained and no historical/group/category issue is terminally disposed.

### Primary body, abstract and secondary scopes

evidence: supported. Targets: GO:0005798.

Losev/Matsuura genuine primary PDF main texts/Methods/captions were read independently from shared fresh snapshots, without pixels/movies/supplements. Papanikou full main BioC text is secondary review. Letourneur/Waters/Serafini and OCH1/SNARE supporting papers are complete primary abstracts only; exact access/assay limits retained.

### Frozen originals and actual native coverage

schema: supported. Targets: GO:0005798.

Original native validate/render passed with byte-identical Markdown, original target hash confirmed from frozen revision. Current verify/causal receipts are source-head bound; their actual nonempty or zero inventories are explicitly limited, not scientific proof.

### Explicit expression-only exclusion is unsupported

provenance: concern. Targets: GO:0005798.

Original check is present, not omitted, but excludes applicability because no expression-module inference is used. Current named proteins, coatomer/COPI retrieval and membrane-budding pathway assertions trigger actual coverage assessment under native policy. This is a bundle defect.

### Current exact-organism catalogue applicability

evidence: not_applicable. Targets: GO:0005798.

Complete fresh official catalogue has no Saccharomyces/cerevisiae/S288C organism/dataset match. No matched gene/module key or downstream summarize applies; an unrelated bacterial proxy would be inappropriate. Historical00:49Z runner limitation remains historical.

### Exact whole/membrane identity and hierarchy

identity: supported. Targets: GO:0030660.

Current native GO names, definitions, synonyms and typed relations support the exact target and its broader parent/parthood. Apparatus/cisternae, complete vesicle and its membrane remain distinct. COPI and TGN are bounded child examples, not universal generic-class attributes.

### Yeast canonical scope and protein strain identity

scope: supported. Targets: GO:0030660.

Saccharomyces4932 is the named canonical species with qualitative COMMON occurrence. Native protein examples are S288C559292 identities, not proof every imaging/transport experiment used that strain. Yeast imaging and retrieval are kept separate from generic Golgi-derived coated-vesicle biochemical context.

### Components, physical assembly scope and grounding

grounding: supported. Targets: GO:0030660.

Generic lipid-bilayer constituent intentionally withholds the complete-membrane GO term as molecular grounding, retaining REVIEWED_LABEL_ONLY. No exact lipid mixture, coat constituent or arbitrary protein inventory is invented.

### Formation necessity versus function and boundary identity

evidence: unknown. Targets: GO:0030660.

Apparatus machinery has UNKNOWN essentiality. A defining membrane boundary is constitutive of the named membrane-bounded class, but this is not evidence each lipid species, coatomer subunit or SNARE is individually required for organelle assembly. Native annotations and transport-mutant assays are not exhaustive formation tests.

### Every current graph node and edge

graph: supported. Targets: GO:0030660.

Five NONMECHANISTIC FUNCTION edges preserve membrane parthood/enclosure, both direct COPI and TGN child classes and Golgi-bilayer donation during GO-defined evagination. No unique lipid-transfer mechanism, all-vesicles COPI coat or additional standalone membrane function is asserted.

### Entire maintained scope and optional slots

completeness: supported. Targets: GO:0030660.

Entire current file/history/discussions and original observation read. No tracked target image, quantitative physical property, trait link or snippet asserted. Unresolved exact lipid/family terms are not automatic defects. PROPOSED status retained and no historical/group/category issue is terminally disposed.

### Primary body, abstract and secondary scopes

evidence: supported. Targets: GO:0030660.

Losev/Matsuura genuine primary PDF main texts/Methods/captions were read independently from shared fresh snapshots, without pixels/movies/supplements. Papanikou full main BioC text is secondary review. Letourneur/Waters/Serafini and OCH1/SNARE supporting papers are complete primary abstracts only; exact access/assay limits retained.

### Frozen originals and actual native coverage

schema: supported. Targets: GO:0030660.

Original native validate/render passed with byte-identical Markdown, original target hash confirmed from frozen revision. Current verify/causal receipts are source-head bound; their actual nonempty or zero inventories are explicitly limited, not scientific proof.

### Explicit expression-only exclusion is unsupported

provenance: concern. Targets: GO:0030660.

Original check is present, not omitted, but excludes applicability because no expression-module inference is used. Current named proteins, coatomer/COPI retrieval and membrane-budding pathway assertions trigger actual coverage assessment under native policy. This is a bundle defect.

### Current exact-organism catalogue applicability

evidence: not_applicable. Targets: GO:0030660.

Complete fresh official catalogue has no Saccharomyces/cerevisiae/S288C organism/dataset match. No matched gene/module key or downstream summarize applies; an unrelated bacterial proxy would be inappropriate. Historical00:49Z runner limitation remains historical.

### Substantive current-record reassessment

provenance: concern. Targets: GO:0005794.

Stale input b064dc11 is replaced by assessed current e3df76cd only through a new linked observation. Retyping retained SED5/TLG2/SEC22 cohort to a physical complex creates F3 despite valid individual examples and native checks; inherited F1 attribution also persists. Closed2462 is historical context, not evidence that present assembly scope is correct or a whole grouped issue resolution.

### Original schema/render and frozen input

schema: supported. Targets: GO:0009514.

Original validate/render pass and historical frozen target hash verifies. Current glyoxysome is unchanged; scientific claims are independently reassessed. Native validity does not itself certify source fidelity.

### Actual identifier and graph coverage

provenance: supported. Targets: GO:0009514.

Zero protein examples, zero represented UniProtKB graph xrefs and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory, not all narrative pathway claims.

### Images, snippets, quantitative traits

scope: not_applicable. Targets: GO:0009514.

No maintained image, quantitative physical-property field, associated trait or verbatim snippet is present. Reading scientific text or captions does not constitute figure-pixel or raw-data reanalysis.

### History and immutable original observations

provenance: supported. Targets: GO:0009514.

Current status/history and original source observations are distinct. No record or original bundle was edited; no neighboring or grouped historical issue is newly resolved by this review.

### Original schema/render and frozen input

schema: supported. Targets: GO:0046859.

Original validate/render pass and historical frozen target hash verifies. Current hydrogenosomal_membrane is unchanged; scientific claims are independently reassessed. Native validity does not itself certify source fidelity.

### Actual identifier and graph coverage

provenance: supported. Targets: GO:0046859.

Zero protein examples, zero represented UniProtKB graph xrefs and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory, not all narrative pathway claims.

### Images, snippets, quantitative traits

scope: not_applicable. Targets: GO:0046859.

No maintained image, quantitative physical-property field, associated trait or verbatim snippet is present. Reading scientific text or captions does not constitute figure-pixel or raw-data reanalysis.

### History and immutable original observations

provenance: supported. Targets: GO:0046859.

Current status/history and original source observations are distinct. No record or original bundle was edited; no neighboring or grouped historical issue is newly resolved by this review.

### Original schema/render and frozen input

schema: supported. Targets: GO:0042566.

Original validate/render pass and historical frozen target hash verifies. Current hydrogenosome is stale; its added topology and localization evidence are substantively reassessed below. Native validity does not itself certify source fidelity.

### Actual identifier and graph coverage

provenance: supported. Targets: GO:0042566.

Zero protein examples and three anchored GENE_OR_PROTEIN nodes classified NO_GENE_SYMBOLS for import, pyruvate/energy and ISC classes. This is not an empty typed-node inventory. No accession-specific membership or necessity is certified.

### Images, snippets, quantitative traits

scope: not_applicable. Targets: GO:0042566.

No maintained image, quantitative physical-property field, associated trait or verbatim snippet is present. Reading scientific text or captions does not constitute figure-pixel or raw-data reanalysis.

### History and immutable original observations

provenance: supported. Targets: GO:0042566.

Current status/history and original source observations are distinct. No record or original bundle was edited; no neighboring or grouped historical issue is newly resolved by this review.

### Positive molecular/pathway assertions and actual dataset applicability

scope: supported. Targets: GO:0009514.

The complete narrative makes glyoxylate-cycle/matrix-import assertions, so expression-only exclusion is insufficient. Fresh official catalogue has no relevant eukaryotic host coverage; downstream queries are not applicable for this bounded catalogue. No heterologous bacterial-host substitution, threshold-as-absence or fresh runner invocation.

### Positive molecular/pathway assertions and actual dataset applicability

scope: supported. Targets: GO:0046859.

The complete narrative makes membrane-boundary and anaerobic metabolic-enzyme assertions, so expression-only exclusion is insufficient. Fresh official catalogue has no relevant eukaryotic host coverage; downstream queries are not applicable for this bounded catalogue. No heterologous bacterial-host substitution, threshold-as-absence or fresh runner invocation.

### Positive molecular/pathway assertions and actual dataset applicability

scope: supported. Targets: GO:0042566.

The complete narrative makes anaerobic metabolic-enzyme/protein-import/ISC assertions, so expression-only exclusion is insufficient. Fresh official catalogue has no relevant eukaryotic host coverage; downstream queries are not applicable for this bounded catalogue. No heterologous bacterial-host substitution, threshold-as-absence or fresh runner invocation.

### Exact organelle identity and boundaries

identity: supported. Targets: GO:0009514.

GO0009514/peroxisome ancestry and separate membrane/lumen identities agree with current authorities and frozen neighbors. Plant-seed emphasis in GO does not prevent the explicitly primary-supported Neurospora case; broad exact identity is not inferred from a protein.

### Fungal occurrence and canonical context

scope: supported. Targets: GO:0009514.

Neurospora crassa identity is verified. deZoysa1994 directly supports nutritionally acetate-induced fungal glyoxysomes and targeted CAT reporters. COMMON and canonical are context-qualified, not all-media frequency measurements; plant/catalase authority prose is not transferred to this fungus.

### Whole membrane versus molecular lipid identity

grounding: concern. Targets: GO:0009514.

Inherited F1 remains: LIPID glyoxysomal_membrane is grounded to complete GO0046861 and propagated through a component_ref. Supported bilayer topology does not make this chemical identity exact; molecular material can remain explicitly label-only if exact composition is unsupported.

### Glyoxylate-cycle compartment and matrix import

evidence: supported. Targets: GO:0009514.

Current primary abstract supports glyoxylate-cycle-enzyme-containing microbodies and C-terminal reporter targeting under defined nutrient induction. This is not proof of exclusive localization of every glyoxylate-cycle reaction, complete enzyme inventory, all possible targeting motifs or a directly imaged translocation mechanism.

### Descriptive topology and cycle-support graph

graph: concern. Targets: GO:0009514.

The three NONMECHANISTIC relations are supported descriptive membrane/lumen/cycle context; the inherited molecular-to-whole-membrane component_ref mismatch remains F1. No perturbation mechanism or enzyme-formation necessity is inferred.

### Boundary essentiality and optional functional inventory

evidence: supported. Targets: GO:0009514.

A bounding membrane is definitionally part of the organelle; source-supported material representation must be corrected independently. Excluding optional matrix enzyme examples from a structural inventory does not assert that enzymes are absent or globally prohibit class components. No enzyme knockout/formation claim is made.

### Actual literature tier and bibliography

provenance: supported. Targets: GO:0009514.

deZoysa identity and complete abstract are current; full publisher PDF is inaccessible and old full-body assertions are not relabeled as freshly inspected. The currently claimed fungal induction/import/compartment scope fits the abstract.

### Membrane identity and organelle relation

identity: supported. Targets: GO:0046859.

GO0046859 and exact SL0144 match; GO0016020 is a valid broad is_a ancestor. Complete membrane part_of hydrogenosome and lumen enclosure are distinct from whole-organelle identity; synonyms and boundaries agree.

### Patchy eukaryotic distribution and T.vaginalis case

scope: supported. Targets: GO:0046859.

ENA verifies Eukaryota and T.vaginalis. Broad rare occurrence is qualitative patchiness; the canonical mechanistic case is T.vaginalis, not all eukaryotes. Authority/review syntheses are not quantitative prevalence experiments.

### Label-only bilayer lipid material

grounding: supported. Targets: GO:0046859.

This record explicitly avoids using whole GO0046859 as molecular grounding. Generic bilayer lipid material can remain label-only; neither current source nor schema justifies inventing exact lipid species/ratios. Its constitutional boundary role does not require every candidate import protein for formation.

### Matrix boundary and anaerobic enzyme compartment

evidence: supported. Targets: GO:0046859.

The membrane bounds the hydrogenosomal matrix supporting anaerobic metabolic machinery. Schneider primary fractionation/proteome and organelle authorities support this context; no fixed membrane proteome, complete transport system or universal lipid composition is claimed.

### Two descriptive boundary relations

graph: supported. Targets: GO:0046859.

NONMECHANISTIC membrane part_of whole and lumen enclosed_by membrane are supported. Material component correspondence remains distinct from whole membrane identity; no mechanistic perturbation or all-lineage necessity is inferred.

### Tachezy2022 title fidelity

provenance: concern. Targets: GO:0046859.

Inherited F1 remains: DOIjeu.12922 is The hydrogenosome of Trichomonas vaginalis, not Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. Correct DOI and broad relevance do not repair the wrong title; source remains secondary.

### Whole organelle identity, topology and stale parthood

identity: supported. Targets: GO:0042566.

GO0042566 whole organelle is distinct from its membrane and GO0034492 lumen. Current added lumen part_of relation agrees with current authority and frozen lumen neighbor. GO says membrane enclosure; interpreting the matrix as inside the inner membrane is biological context, not a quoted GO phrase.

### Experimental species and qualitative occurrence

scope: supported. Targets: GO:0042566.

T.vaginalis current primary studies support the canonical case, while Lindmark1973 concerns Tritrichomonas foetus and is currently metadata-only. Broad Eukaryota RARE is patchy, not measured prevalence. Other hydrogenosome lineages need not share every T.vaginalis genomic/metabolic property.

### Whole membrane used as lipid component identity

grounding: concern. Targets: GO:0042566.

Inherited F1 remains: GO0046859 is the assembled membrane and cannot be exact molecular grounding for LIPID. Correct has_part/topology must be preserved while correcting molecular material and graph component_ref.

### Heterogeneous protein classes and incomplete inventories

scope: supported. Targets: GO:0042566.

Energy, ISC and import entries are explicitly broad functional/localization classes with UNKNOWN essentiality, not one family or asserted fixed complex. Native family-or-class guidance permits this scope. Zero examples and three NO_GENE_SYMBOLS nodes remain explicit; no unsupported precise family, complex, accession or formation necessity is added.

### Pyruvate-linked ATP and hydrogen production

evidence: supported. Targets: GO:0042566.

Current Schneider main text supports PFO/ferredoxin/hydrogenase and substrate-level-phosphorylation machinery in T.vaginalis hydrogenosomes. Lindmark bibliography is verified but its original assay body is not freshly accessed. Functional pathway support is not a measured universal stoichiometry or requirement for organelle formation.

### ISC activity and member-specific localization

evidence: concern. Targets: GO:0042566.

Sutak directly localizes TvIscS-2 and measures lysate-dependent FeS reconstitution. Schneider later detects IscU in the hydrogenosomal proteome, with fractionation/contamination limits. The new edge note overattributes demonstrated lumenal IscS/IscU localization to Sutak alone; retain pathway support and narrow that source claim.

### Presequences, internal signals and reporter scope

evidence: concern. Targets: GO:0042566.

Inherited F3 remains: N-terminal targeting is one demonstrated route, not an unqualified requirement. Dolezal heterologous GiIscS fragments target T.vaginalis hydrogenosomes without an N-terminal presequence; Schneider3.8 confirms internal/presequence-independent possibilities while retaining stringent motif prediction as an alternative. Bui Hsp60 processing is a particular example.

### Mechanistic synthesis versus specific assays

graph: concern. Targets: GO:0042566.

The nine edges combine supported topology, energy/ISC pathway and import contexts. Dolezal reporters do not independently test every native pyruvate enzyme cargo; Schneider supplies cohort/fraction context. Inherited membrane correspondence and new Sutak attribution defects are scoped findings. The new lumen parthood is supported, and no IscU absence or wholesale pathway rejection follows.

### Formation necessity and operational function

evidence: supported. Targets: GO:0042566.

Generic protein classes retain UNKNOWN essentiality. Biochemical activity, reporter import and fraction localization do not establish organelle-formation necessity of each class/member. Constitutional membrane requirement is separate from wrong lipid grounding.

### Tachezy bibliographic identity and source tiers

provenance: concern. Targets: GO:0042566.

Inherited F2 wrong Tachezy title remains. Bui and deZoysa are current primary abstract tiers; Lindmark metadata only; Tachezy secondary abstract; Schneider selected genuine body sections; Sutak rendered main text; Dolezal detailed indexed main text. No failed route is promoted to full-body access.

### Current scoped verdict and unresolved curation

completeness: concern. Targets: GO:0009514.

needs_curation: 1 confirmed finding(s) remain for this maintained record. Original lineage is preserved; new hydrogenosome attribution is independently supported and has no predecessor. Bundle applicability corrections and stale refresh do not silently curate the record or resolve neighbors.

### Current scoped verdict and unresolved curation

completeness: concern. Targets: GO:0046859.

needs_curation: 1 confirmed finding(s) remain for this maintained record. Original lineage is preserved; new hydrogenosome attribution is independently supported and has no predecessor. Bundle applicability corrections and stale refresh do not silently curate the record or resolve neighbors.

### Current scoped verdict and unresolved curation

completeness: concern. Targets: GO:0042566.

needs_curation: 4 confirmed finding(s) remain for this maintained record. Original lineage is preserved; new hydrogenosome attribution is independently supported and has no predecessor. Bundle applicability corrections and stale refresh do not silently curate the record or resolve neighbors.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0009514, GO:0005794, GO:0005798, GO:0030660, GO:0031985, GO:0032580, GO:0005796, GO:0000139, GO:0046859, GO:0042566.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t4-F1: Remove the whole-cisterna correspondence to its lipid component

major / open / confirmed; issue key: golgi-cisterna-whole-compartment-lipid-component-ref.

The graph node golgi_cisterna denotes the complete membrane-bounded compartment GO0031985 but component_ref points to golgi_cisternal_lipid_bilayer. That component denotes boundary lipid material, while the separate golgi_cisterna_membrane node already denotes the correct GO0032580 boundary. The schema defines component_ref as identifying a node that is one of the record’s components, so this join incorrectly equates whole compartment and lipid constituent.

### micro-F1: Correct the source attribution for SNARE pairing and cycling

minor / open / confirmed; issue key: golgi-apparatus-snare-review-attribution.

The component note, graph-edge note and discussion attribute SNARE pairing/cycling to Papanikou and Glick2014. Its complete main text reviews compartment traffic, coats, tethers and GTPases but does not supply those SNARE-specific statements. Native SED5/TLG2/SEC22 entries and the already cited imaging papers support relevant SNARE context, so this is a bounded source-placement problem rather than a claim that these proteins have no Golgi role.

### micro-F2: Separate the complete vesicle membrane from molecular lipid identity

major / open / confirmed; issue key: golgi-associated-vesicle-membrane-molecular-grounding.

The golgi_associated_vesicle_membrane component is typed LIPID and grounded to GO0030660, which identifies the complete assembled membrane surrounding the vesicle. The frozen schema defines StructuralComponent as a molecular building block and distinguishes lipid chemical identity from substructure identity. The graph correctly calls this object STRUCTURE but repeats the molecular correspondence through component_ref. Correct has_part and topology do not resolve that mismatch.

### micro-F3: Keep the broad Golgi SNARE cohort distinct from a defined Sed5 complex

major / open / confirmed; issue key: golgi-apparatus-snare-cohort-complex-conflation.

The stale delta retypes the unchanged SED5/TLG2/SEC22 cohort as PROTEIN_COMPLEX and calls it a Sed5-containing cis-Golgi complex in history, while its current label and grounding notes still describe general Golgi trafficking machinery. Fresh native SEC22 and primary Parlati2000/Mossessova2003 abstracts identify Sed5/Bos1/Bet1/Sec22 or Sed5/Bos1/Sec22 fusion assemblies; Tlg2 has a distinct late-Golgi/endosome role and Tlg1/Tlg2/Vps45 association in Nichols1998. This does not support one named subcomplex encompassing the retained cohort. Individual accessions remain correct. Native policy permits generic protein classes, so the concern is unsupported physical-complex scope, not mere heterogeneity or a requirement to invent an exact family. GENE_OR_PROTEIN is explicitly legal for complexes and is not a separate node-type defect.

### septin-glyoxysome-F1: Separate the complete membrane identity from its molecular lipid constituent

major / open / confirmed; issue key: glyoxysome-lipid-whole-membrane-grounding.

The glyoxysomal_membrane component is typed LIPID but grounded to GO:0046861, which identifies the complete organelle membrane. The schema requires a molecular building block and chemical grounding for a lipid, while GO can identify a sub-complex. Correct membrane parthood and bilayer topology do not make the entire membrane term an exact lipid molecular identity. The graph component_ref propagates this mismatch.

### septin-hydrogenosomal_membrane-F1: Correct the title of the cited Tachezy2022 review

minor / open / confirmed; issue key: hydrogenosomal-membrane-tachezy-title.

DOI:10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdý, not the title Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes recorded in evidence.notes. The DOI and broad scientific relevance remain correct.

### septin-hydrogenosome-F1: Separate the complete membrane identity from its molecular lipid constituent

major / open / confirmed; issue key: hydrogenosome-lipid-whole-membrane-grounding.

The hydrogenosomal_membrane component is typed LIPID but grounded to GO:0046859, which identifies the complete organelle membrane. The schema requires a molecular building block and chemical grounding for a lipid, while GO can identify a sub-complex. Correct membrane parthood and bilayer topology do not make the entire membrane term an exact lipid molecular identity. The graph component_ref propagates this mismatch.

### septin-hydrogenosome-F2: Correct the title of the cited Tachezy2022 review

minor / open / confirmed; issue key: hydrogenosome-tachezy-title.

DOI:10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdý, not the title Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes recorded in evidence.notes. The DOI and broad scientific relevance remain correct.

### septin-hydrogenosome-F3: Qualify N-terminal presequence targeting as one demonstrated import route

minor / open / confirmed; issue key: hydrogenosome-import-route-qualification.

The matrix-import function says nuclear-encoded matrix proteins are targeted through N-terminal presequences without qualification. Its cited Dolezal2005 paper demonstrates internal targeting signals in GiIscS expressed in T. vaginalis as well as N-terminal targeting; Schneider2011 §3.8 also states that targeting without an N-terminal presequence has been demonstrated. The evidence supports the route but not an unqualified common requirement.

### septin-hydrogenosome-F4: Narrow the new Sutak2004 localization attribution to the measured ISC member

minor / open / confirmed; issue key: hydrogenosome-sutak-iscu-localization-attribution.

The newly added localization edge describes IscS/IscU machinery and its Sutak2004 evidence note says the paper demonstrated lumenal IscS/IscU machinery. Sutak directly assays TvIscS-2 hydrogenosomal fractionation/immunolocalization and lysate-dependent FeS reconstitution; IscU appears in yeast/bacterial model/interaction context, not a native T.vaginalis IscU localization experiment. Schneider2011 later detects IscU in a hydrogenosomal proteome, but fraction detection is not the same source or a separate precise lumenal localization assay. General ISC biology remains supported; the defect is this source-specific overattribution, not evidence that IscU is absent.

## Recommended Actions And Acceptance Checks

### plaque-t4-A1

In separately authorized curation, remove the lipid component_ref from the whole-cisterna node and, if justified by the existing material model, associate the bilayer component only with the membrane-boundary node. Preserve the cisterna identity, native membrane grounding and source-supported maturation/topology edges.

- Verify that each component_ref denotes the same object as its component and does not equate a whole compartment with lipid material.
- Preserve supported native hierarchy, subtype and primary-source experimental scope.
- Run focused schema, strict and graph/product checks after separately authorized scientific curation.

### micro-A1

In separately authorized curation, remove the inaccurate Papanikou-specific SNARE wording and attach directly inspected evidence to the exact SNARE traffic or maturation assertion, or narrow that assertion to the support actually available. Retain broad machinery scope and avoid implying that all three examples form one complex.

- Re-read each revised source at the exact component/edge/discussion placement.
- Preserve the directly observed yeast marker-maturation scope and reference-strain identity distinction.
- Run focused schema, strict and relevant native graph/protein checks after curation.

### micro-A2

In separately authorized curation, keep the complete membrane in has_part and as the grounded graph structure, and remove its molecular component_ref if removing the whole-membrane component. Any replacement lipid material must have source-supported identity and justified chemical or reviewed-label-only grounding; do not invent a lipid mixture.

- Verify that each component_ref denotes the same object as its component and does not equate a whole compartment with lipid material.
- Preserve supported native hierarchy, subtype and primary-source experimental scope.
- Run focused schema, strict and graph/product checks after separately authorized scientific curation.

### micro-A3

In separately authorized curation, explicitly retain a source-supported generic protein-class cohort under the native family-or-class policy, or split/narrow it to independently supported named assemblies with matching participants and evidence. Do not automatically force every broad cohort into PROTEIN_COMPLEX, impose an exhaustive subunit inventory, or infer Tlg2 never interacts with other SNAREs. Preserve correct individual accessions and immutable historical events; append a new curation/history event.

- The component label, type, scope, gene/examples and evidence denote the same generic class or exact physical assembly.
- Verify chosen assembly participants against directly inspected sources; explain treatment of Tlg2 separately from a Sed5/Bos1/Bet1/Sec22 identity.
- Run native focused schema/strict, graph/protein and relevant product checks after authorized curation.

### septin-glyoxysome-A1

In a separately authorized curation change, preserve the complete membrane in structural parthood/topology and represent only source-supported lipid material in the component row, with exact chemical grounding if justified or an explicitly reviewed label-only material; correct the graph component_ref correspondence.

- Do not use the complete membrane GO term as chemical lipid identity or invent an exact lipid mixture.
- Preserve correct organelle identity, has_part, membrane STRUCTURE node and supported topology; any component_ref must denote the actual molecular component.
- Run focused schema, grounding/product and graph checks after separately authorized curation.

### septin-hydrogenosomal_membrane-A1

In a separately authorized curation change, replace the incorrect citation title and author attribution with the exact native bibliographic identity while retaining the correct DOI and review evidence tier.

- Verify DOI, exact title, three authors, year2022 and Journal of Eukaryotic Microbiology against the native metadata.
- Do not replace the correct DOI, claim that this review is a primary experiment, or generalize its T. vaginalis focus solely from the incorrect broad title.

### septin-hydrogenosome-A1

In a separately authorized curation change, preserve the complete membrane in structural parthood/topology and represent only source-supported lipid material in the component row, with exact chemical grounding if justified or an explicitly reviewed label-only material; correct the graph component_ref correspondence.

- Do not use the complete membrane GO term as chemical lipid identity or invent an exact lipid mixture.
- Preserve correct organelle identity, has_part, membrane STRUCTURE node and supported topology; any component_ref must denote the actual molecular component.
- Run focused schema, grounding/product and graph checks after separately authorized curation.

### septin-hydrogenosome-A2

In a separately authorized curation change, replace the incorrect citation title and author attribution with the exact native bibliographic identity while retaining the correct DOI and review evidence tier.

- Verify DOI, exact title, three authors, year2022 and Journal of Eukaryotic Microbiology against the native metadata.
- Do not replace the correct DOI, claim that this review is a primary experiment, or generalize its T. vaginalis focus solely from the incorrect broad title.

### septin-hydrogenosome-A3

In a separately authorized curation change, qualify the function to state that some matrix proteins use N-terminal presequences and that internal/presequence-independent targeting also occurs; retain the supported import machinery and generic import pathway.

- Bind the qualification to the actual Dolezal Results and retain the heterologous-reporter context.
- Do not infer that all proteins lacking a predicted motif lack a targeting signal; Schneider explicitly gives stringent prediction as an alternative.
- Do not remove the validated N-terminal route or convert import activity into organelle-assembly necessity.

### septin-hydrogenosome-A4

In separately authorized record curation, narrow the Sutak2004 note to the directly measured TvIscS-2 localization and lysate activity, or add an appropriate later member-specific source with its actual fraction/subcompartment scope. Keep the edge description and source note consistent without discarding supported ISC biology.

- Check the actual Sutak Methods, Results and Discussion; distinguish TvIscS-2 immunolocalization from yeast/bacterial IscU context.
- If retaining IscU, cite its actual evidence and preserve proteomic fraction versus direct lumen-localization limitations.
- Do not infer IscU absence, invent a new accession or delete the supported pathway merely because this source attribution is too broad.
- Run focused schema and relevant graph/source checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/glyoxysome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4; current SHA256 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T015623Z-glyoxysome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/golgi_apparatus.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b064dc1116ec2814e2ecb946d8ebd554a4b176494c2259ff7e458bac0d3e5eb1; current SHA256 e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261022T015625Z-golgi-apparatus-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/golgi_associated_vesicle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba; current SHA256 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T015627Z-golgi-associated-vesicle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413; current SHA256 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T015629Z-golgi-associated-vesicle-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/golgi_cisterna.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a; current SHA256 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T015631Z-golgi-cisterna-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/golgi_cisterna_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e; current SHA256 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T015633Z-golgi-cisterna-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/golgi_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b; current SHA256 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T015635Z-golgi-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/golgi_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c; current SHA256 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T015637Z-golgi-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/hydrogenosomal_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56; current SHA256 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T015639Z-hydrogenosomal-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/hydrogenosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 cbe6ff879b7bc2477e475394c4361107d4d033bfeba79e4a85c03787b27b8b70; current SHA256 6d295ad6b0bb5066ddec461e6c2ffa142de9d8590d705eff6a3648bc6c01e77a. Changed record reassessed against current sources. |
| original-review-9 | reviews/structured/20261022T015641Z-hydrogenosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-4 | data/structures/membrane_organelle/golgi_cisterna.yaml; Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14; all fields, histories, discussions and graphs | supports | Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific record curation performed. |
| plaque-original-4 | reviews/structured/20261022T015631Z-golgi-cisterna-audit/review.yaml; Exact staleness-listed authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders exactly; all 14 historical inputs match its source. Historical verdict independently reassessed; original remains immutable. |
| plaque-current-5 | data/structures/membrane_organelle/golgi_cisterna_membrane.yaml; Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14; all fields, histories, discussions and graphs | supports | Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific record curation performed. |
| plaque-original-5 | reviews/structured/20261022T015633Z-golgi-cisterna-membrane-audit/review.yaml; Exact staleness-listed authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders exactly; all 17 historical inputs match its source. Historical verdict independently reassessed; original remains immutable. |
| plaque-current-6 | data/structures/membrane_organelle/golgi_lumen.yaml; Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14; all fields, histories, discussions and graphs | supports | Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific record curation performed. |
| plaque-original-6 | reviews/structured/20261022T015635Z-golgi-lumen-audit/review.yaml; Exact staleness-listed authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders exactly; all 16 historical inputs match its source. Historical verdict independently reassessed; original remains immutable. |
| plaque-current-7 | data/structures/membrane_organelle/golgi_membrane.yaml; Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14; all fields, histories, discussions and graphs | supports | Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific record curation performed. |
| plaque-original-7 | reviews/structured/20261022T015637Z-golgi-membrane-audit/review.yaml; Exact staleness-listed authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders exactly; all 17 historical inputs match its source. Historical verdict independently reassessed; original remains immutable. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native contract and relevant definitions | context_only | Genes, proteins, regulators, pathways, stress responses and traits trigger structured-source assessment. Empty inventories or lack of transcriptomic assertions do not waive positive pathway claims. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native contract and relevant definitions | context_only | Exact identity, source scope, taxonomy, molecular composition and necessity require separate assessment; optional empty inventories are not themselves defects. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native contract and relevant definitions | context_only | Physical topology and broad descriptive function remain distinct from exact molecular mechanism, and each directed claim requires inspected support. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen native contract and relevant definitions | context_only | Native protein commands verify represented accessions and typed graph actors; their scope does not independently certify narrative pathways. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native contract and relevant definitions | context_only | StructuralComponent denotes a molecular building block; CausalNode.component_ref identifies a node that is one of the structure own components. A whole compartment is not identical to its lipid constituent. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031985,GO:0032580,GO:0005796,GO:0000139,GO:0098791,GO:0005794,GO:0016020,GO:0070013,GO:0030126,GO:0035964; Complete exact responses for GO0031985,0032580,0005796,0000139,0098791,0005794,0016020,0070013,0030126,0035964: names, definitions, synonyms and typed children | supports | GO separates whole cisterna, its membrane, lumen and generic Golgi membrane. Cisterna is a Golgi subcompartment; membrane/lumen are parts of Golgi. GO0070013 lists Golgi lumen as is_a. COPI coat and COPI budding definitions support generic coat-associated vesicle formation. Ontology membership is not a species-specific necessity experiment. |
| plaque-ancestors-0031985 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031985/ancestors?relations=is_a; Exact current QuickGO is_a-only ancestor response | supports | GO0031985 is_a ancestry includes Golgi subcompartment0098791. |
| plaque-ancestors-0032580 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032580/ancestors?relations=is_a; Exact current QuickGO is_a-only ancestor response | supports | GO0032580 is_a ancestry includes generic membrane0016020 but does not contain Golgi membrane0000139. The record broader parent0000139 is definition-supported; no direct native GO edge is claimed. |
| plaque-ancestors-0005796 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005796/ancestors?relations=is_a; Exact current QuickGO is_a-only ancestor response | supports | GO0005796 is_a ancestry includes organelle lumen0070013. |
| plaque-ancestors-0000139 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139/ancestors?relations=is_a; Exact current QuickGO is_a-only ancestor response | supports | GO0000139 is_a ancestry includes membrane0016020. |
| plaque-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA native taxonomy response: taxId/scientificName/rank/lineage | supports | NCBITaxon4932 is Saccharomyces cerevisiae. Species identity is not a measured prevalence or interchangeable experimental strain. |
| plaque-SL0133 | https://rest.uniprot.org/locations/SL-0133.json; Complete native subcellular-location definition/synonyms and exact GO cross-reference | supports | SL0133 denotes Golgi apparatus lumen with Golgi complex lumen synonym and GO0005796 cross-reference. It is distinct from Golgi membrane; no protein inventory inferred. |
| plaque-losev2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nature04717&amp;pageSize=25; Exact PMID16699524 primary metadata and complete abstract | supports | Losev et al.2006 DOI10.1038/nature04717 reports cisternal maturation directly visualized in S. cerevisiae. Bibliographic attribution matches; detailed scope separately checked against primary PDF. |
| plaque-matsuura2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nature04737&amp;pageSize=25; Exact PMID16699523 primary metadata and complete abstract | supports | Matsuura-Tokita et al.2006 DOI10.1038/nature04737 reports live imaging of yeast Golgi cisternal maturation. Exact author/year/source identity matches; detailed scope separately checked against primary PDF. |
| plaque-losev2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf; Fresh university-hosted primary PDF, complete scientific main text pp1002–1005, Methods and Figure1–4 captions read via text extraction; no figure pixels/movies/supplements | supports | Individually resolved budding-yeast cisternae transition resident markers including Vrg4 to Sec7; additional marker pairs support changing identity. Four-dimensional microscopy and pulse-chase consistency support maturation. Direct cargo residence and specific recycling mechanism remain unresolved. Unstacked yeast cisternae are not evidence that all Golgi stacks or all eukaryotic compartments use an exclusive route. |
| plaque-matsuura2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf; Fresh university-hosted primary PDF, scientific main pp1007–1009, Methods continuation paragraph p1010 and Figure1–4 captions; no figure pixels/movies/supplements | supports | S. cerevisiae Rer1/Gos1 and Sed5/Sec7 markers change during individual cisternal maturation. ret1-1 alpha-COP mutation slows but does not abolish changes under stated temperature conditions. Primary observations support scoped maturation; proposed tubular/vesicular contacts do not uniquely establish the mechanism or universal cargo route. |
| plaque-dean1997-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9395539%20AND%20SRC%3AMED&amp;pageSize=25; Exact PMID9395539 primary bibliographic match and complete abstract only | supports | Dean, Zhang and Poster1997 DOI10.1074/jbc.272.50.31908 describes specific GDP-mannose transport defects in Golgi vesicles from vrg4 mutants, altered mannosylation and Vrg4 localization to Golgi membranes. Supports nucleotide-sugar access to the lumen and boundary transporter context, not purified-protein reconstitution, individual organelle-formation necessity or stable lumen residency. |
| plaque-serafini1991-quoted | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22&amp;pageSize=25; Exact quoted DOI match PMID1680566: complete primary abstract and bibliographic/MESH context only | supports | Serafini et al.1991 DOI10.1016/0092-8674(91)90176-y identifies ARF in Golgi-derived vesicle coats, GTP-dependent membrane recruitment and release during uncoating. Supports coat assembly/regulatory context. Mammalian source context is not a yeast-specific experiment, and abstract does not prove coat-alone force generation. |
| plaque-go-budding-primary-10052452 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10052452%20AND%20SRC%3AMED&amp;pageSize=25; Exact PMID10052452 primary abstract; primary reference linked from GO0035964 | supports | Bremser et al.1999 DOI10.1016/s0092-8674(00)80654-6 reconstitutes coat assembly/budding on liposomes resembling mammalian Golgi membranes with coatomer, ARF, GTP and cargo-receptor tails. Conditional reconstitution supports COPI participation, not isolated coat sufficiency or direct yeast experimentation. |
| plaque-papanikou2014-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4130901.1/PMC4130901.1.xml; Genuine PMC secondary-review JATS; complete sections S1 Introduction, S3 cisternal assembly, S4 carbohydrate synthesis, S5 carrier formation, independently read; other sections and figure pixels not certified | supports | Papanikou and Glick2014 review supports compartment identity, cisternal maturation and carrier-recycling context while retaining unresolved directions, cargo roles and compartment differences. Secondary synthesis is not a fresh primary experiment; broad COPI participation is not generalized to every Golgi compartment or a unique maturation mechanism. |
| plaque-dean1997-publisher | https://doi.org/10.1074/jbc.272.50.31908; HTTP200 DOI route returned short HTML meta-refresh landing, not an article body | context_only | Full publisher body was not obtained on this route. Actual scientific assessment uses the separately inspected complete primary abstract; no full-body inspection inferred from HTTP200. |
| plaque-serafini1991-publisher | https://doi.org/10.1016/0092-8674(91)90176-y; HTTP200 DOI route returned short HTML meta-refresh landing, not an article body | context_only | Full publisher body was not obtained on this route. Actual scientific assessment uses the separately inspected complete primary abstract; no full-body inspection inferred from HTTP200. |
| plaque-serafini1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/0092-8674(91)90176-y&amp;pageSize=25; Initial unquoted exact-DOI query, pageSize25, zero returned matches | context_only | This unsuccessful query was corrected with an exact quoted DOI query yielding PMID1680566. Zero results were not interpreted as absence of the article or biological evidence. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh official /api/datasets response; every returned organism row/dataset listing inspected, no pagination | supports | No S. cerevisiae host appears in the returned catalogue. Cisternal maturation, VRG4/GDP-mannose glycosylation and COPI budding are genuine triggers, but no matched downstream gene/module query applies. Unrelated bacterial/archaeal datasets are not proxies; noncoverage is not negative biology and generated module prose is excluded. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt; stdout/stderr reread and hashes verified | context_only | Historical runner failed before retrieval with PermissionError reading pyvenv.cfg. No current invocation or success claimed; fresh official source catalogue and inspected primary/authority evidence supply bounded fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/original-checks.json; Four actual original native validate/render results and historical-source input hashes | supports | All four original pairs validate and render exactly; historical input counts14/17/16/17 match source commits. All four current targets are unchanged from originals; no stale target in this slice. |
| plaque-native-golgi_cisterna-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_cisterna-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_cisterna_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna_membrane.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_cisterna_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna_membrane.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_lumen.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_lumen.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| plaque-native-golgi_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions require independent scientific assessment. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Current skill/profile/config/shared contract and scientific checklist; CURATION identity, narrow evidence, family-or-class and molecular grounding rules | context_only | Named proteins and pathways trigger source-adapter applicability, even without transcriptomics assertions. Evidence is claim-specific; current review does not rewrite original history. |
| micro-component-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, ComponentTypeEnum, CausalNode and essentiality; CURATION108-110 family-or-class and UniProt skill Step2 generic-class guidance | context_only | Generic protein classes are permitted by native guidance; PROTEIN_COMPLEX denotes a named subcomplex with its own identity. ProteinExample identity is not membership proof. CausalNode explicitly allows protein complexes as GENE_OR_PROTEIN, so no graph-node-type defect is inferred from complex typing. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Complete graph skill and add-cell-structure evidence/graph contract; NONMECHANISTIC scope | context_only | Identity, topology, experimental context and narrow edge-level evidence must agree; no complete assembly mechanism or necessary individual composition inferred from marker localization. |
| micro-record-golgi_apparatus | data/structures/membrane_organelle/golgi_apparatus.yaml; Entire maintained target: all fields, current component types/examples, graph nodes/edges, discussions, history and evidence notes | supports | Current bytes independently read; stale old input substantively reassessed after SNARE cohort retyping. |
| micro-prior-golgi_apparatus | reviews/structured/20261022T015625Z-golgi-apparatus-audit/review.yaml; Original assessments/findings/actions, source scopes, checks, limitations; paired Markdown verified with native renderer | context_only | Original verdict needs_curation; 1 original finding(s). Expression-only applicability exclusion exists and requires correction. Historical scientific checks/accesses remain historical. |
| micro-native-golgi_apparatus-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml --verify; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Six reviewed S288C examples OCH1/MNN1/KRE2 and SED5/TLG2/SEC22; two COVERED nodes. The check verifies declared identities and coverage, not that all examples form one physical complex or directly determine maturation. |
| micro-native-golgi_apparatus-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml --causal-graphs; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-causal.log SHA256 c43cea8c606cb2810b4f9b7c7a5c88f1dfd70ae0fb115897019bc9f86a673fad | supports | Exit0 at source head. Six reviewed S288C examples OCH1/MNN1/KRE2 and SED5/TLG2/SEC22; two COVERED nodes. The check verifies declared identities and coverage, not that all examples form one physical complex or directly determine maturation. |
| micro-record-golgi_associated_vesicle | data/structures/membrane_organelle/golgi_associated_vesicle.yaml; Entire maintained target: all fields, current component types/examples, graph nodes/edges, discussions, history and evidence notes | supports | Current bytes independently read; target equals original frozen input. |
| micro-prior-golgi_associated_vesicle | reviews/structured/20261022T015627Z-golgi-associated-vesicle-audit/review.yaml; Original assessments/findings/actions, source scopes, checks, limitations; paired Markdown verified with native renderer | context_only | Original verdict needs_curation; 1 original finding(s). Expression-only applicability exclusion exists and requires correction. Historical scientific checks/accesses remain historical. |
| micro-native-golgi_associated_vesicle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle.yaml --verify; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN nodes; generic verify-success text is an empty protein inventory, not a composition/localization experiment. |
| micro-native-golgi_associated_vesicle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle.yaml --causal-graphs; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN nodes; generic verify-success text is an empty protein inventory, not a composition/localization experiment. |
| micro-record-golgi_associated_vesicle_membrane | data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml; Entire maintained target: all fields, current component types/examples, graph nodes/edges, discussions, history and evidence notes | supports | Current bytes independently read; target equals original frozen input. |
| micro-prior-golgi_associated_vesicle_membrane | reviews/structured/20261022T015629Z-golgi-associated-vesicle-membrane-audit/review.yaml; Original assessments/findings/actions, source scopes, checks, limitations; paired Markdown verified with native renderer | context_only | Original verdict pass_with_limitations; 0 original finding(s). Expression-only applicability exclusion exists and requires correction. Historical scientific checks/accesses remain historical. |
| micro-native-golgi_associated_vesicle_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml --verify; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN nodes; generic verify-success text is an empty protein inventory, not a composition/localization experiment. |
| micro-native-golgi_associated_vesicle_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml --causal-graphs; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN nodes; generic verify-success text is an empty protein inventory, not a composition/localization experiment. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-microtubule/original-validation-receipt.json; Three native validate and three render --content runs; exact original Markdown equality; original git-show input hashes | supports | All three original pairs validate and render byte-identically. Historical frozen target hashes verified; only apparatus differs from old input. |
| micro-stale-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-microtubule/golgi-apparatus-stale.diff; Entire original frozen revision to current-source diff | context_only | Only October30 history and PROTEIN to PROTEIN_COMPLEX change for the SED5/TLG2/SEC22 cohort. No narrowing of cohort label, notes, examples or edge evidence accompanied the change. Historical issue2462 mention is context, not an endorsement or whole-issue disposition. |
| micro-historical-2462 | https://github.com/CultureBotAI/CellStructureMech/issues/2462; Root-retained issue packet /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/historical-issue-2462.json; complete body/comments/state read, only historical context | context_only | Grouped issue2462 prescribed a Golgi SED5/TLG2/SEC22 type change among11 records and reports prior remediation. This is not independent molecular membership evidence; no exact category predecessor is reassessed or terminally disposed, and the new current-record finding does not reopen the grouped issue. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005794,GO:0043231,GO:0012505,GO:0000139,GO:0031985,GO:0005798,GO:0030660,GO:0031410,GO:0030659,GO:0030663,GO:0012510,GO:0030137,GO:0030126,GO:0035964,GO:0006890; All15 exact active terms; complete names/definitions/synonyms/typed child relations | supports | Exact apparatus5794, vesicle5798 and membrane30660 identities agree. Apparatus is direct is_a43231 and part_of12505; membrane139 is part_of apparatus. Vesicle is direct is_a31410; membrane30660 part_of5798, with direct COPI30663 and TGN12510 is_a children. COPI30137 is child of5798; coat30126 is distinct from membrane. Budding35964 is Golgi-membrane evagination;6890 is directed retrograde transport. Cisterna31985 definition supports a Golgi compartment without claiming a direct ontology part_of edge not returned. |
| micro-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete exact ENA taxId/scientificName/rank/lineage | supports | Taxon4932 is Saccharomyces cerevisiae at species rank. Canonical species occurrence is qualitative; reference-strain protein identity does not rename experimental strains. |
| micro-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete exact ENA taxId/scientificName/rank/lineage | supports | Taxon559292 is Saccharomyces cerevisiae S288C at strain rank. Canonical species occurrence is qualitative; reference-strain protein identity does not rename experimental strains. |
| micro-protein-P31755 | https://rest.uniprot.org/uniprotkb/P31755.json; Exact native accession/name/status/gene/organism and complete relevant comments with ECO/PMID attribution | supports | P31755 is reviewed, primary gene OCH1, tax559292; exact recommended protein name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments inspected. ER-membrane ECO0000269 cites14676282/1628616; Golgi-membrane ECO0000269 includes15229219, matching target provenance. Recycling context preserved. |
| micro-query-OCH1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AOCH1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete response with primary/synonym tokens, total-results1 and no next-page Link | supports | Exactly P31755 returned and actual primary gene OCH1 agrees. Bounded current uniqueness wording is supported. |
| micro-protein-P39106 | https://rest.uniprot.org/uniprotkb/P39106.json; Exact native accession/name/status/gene/organism and complete relevant comments with ECO/PMID attribution | supports | P39106 is reviewed, primary gene MNN1, tax559292; exact recommended protein name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments inspected. Golgi membrane annotation is ECO0000305; terminal mannosylation is native function, not fresh microscopy. |
| micro-query-MNN1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMNN1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete response with primary/synonym tokens, total-results1 and no next-page Link | supports | Exactly P39106 returned and actual primary gene MNN1 agrees. Bounded current uniqueness wording is supported. |
| micro-protein-P27809 | https://rest.uniprot.org/uniprotkb/P27809.json; Exact native accession/name/status/gene/organism and complete relevant comments with ECO/PMID attribution | supports | P27809 is reviewed, primary gene KRE2, tax559292; exact recommended protein name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments inspected. KRE2/MNT1 native Golgi localization and glycosyltransferase15 context do not establish universal organelle necessity. |
| micro-query-KRE2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AKRE2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete response with primary/synonym tokens, total-results1 and no next-page Link | supports | Exactly P27809 returned and actual primary gene KRE2 agrees. Bounded current uniqueness wording is supported. |
| micro-protein-Q01590 | https://rest.uniprot.org/uniprotkb/Q01590.json; Exact native accession/name/status/gene/organism and complete relevant comments with ECO/PMID attribution | supports | Q01590 is reviewed, primary gene SED5, tax559292; exact recommended protein name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments inspected. Sed5 t-SNARE supports ER-Golgi transport; interaction and localization annotations do not define the full broad cohort as one assembly. |
| micro-query-SED5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASED5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete response with primary/synonym tokens, total-results1 and no next-page Link | supports | Exactly Q01590 returned and actual primary gene SED5 agrees. Bounded current uniqueness wording is supported. |
| micro-protein-Q08144 | https://rest.uniprot.org/uniprotkb/Q08144.json; Exact native accession/name/status/gene/organism and complete relevant comments with ECO/PMID attribution | supports | Q08144 is reviewed, primary gene TLG2, tax559292; exact recommended protein name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments inspected. Tlg2 functions in endosome-to-late-Golgi/endocytic traffic, with trans-Golgi/endosome membrane locations and Vps45 interaction. |
| micro-query-TLG2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATLG2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete response with primary/synonym tokens, total-results1 and no next-page Link | supports | Exactly Q08144 returned and actual primary gene TLG2 agrees. Bounded current uniqueness wording is supported. |
| micro-protein-P22214 | https://rest.uniprot.org/uniprotkb/P22214.json; Exact native accession/name/status/gene/organism and complete relevant comments with ECO/PMID attribution | supports | P22214 is reviewed, primary gene SEC22, tax559292; exact recommended protein name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments inspected. SUBUNIT explicitly names distinct Sed5/Bos1/Bet1/Sec22 and Ufe1/Use1/Sec20/Sec22 complexes. SEC22 is nonessential for cell viability in native function context, not established essential for Golgi formation. |
| micro-query-SEC22 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC22%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete response with primary/synonym tokens, total-results1 and no next-page Link | supports | Exactly P22214 returned and actual primary gene SEC22 agrees. Bounded current uniqueness wording is supported. |
| micro-papanikou2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.ceb.2014.04.010%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID24840895 DOI10.1016/j.ceb.2014.04.010 Golgi compartmentation and identity. Secondary review proposes a three-stage model; not a primary experiment. Its author-manuscript BioC header year is not substituted for the exact MED2014 citation. |
| micro-letourneur1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8001155+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID8001155 DOI10.1016/0092-8674(94)90011-6 Coatomer is essential for retrieval of dilysine-tagged proteins to the endoplasmic reticulum. Complete primary abstract describes dilysine-tagged Ste2 retrieval in yeast, selective coatomer-mutant defects and RET1 complementation; supports scoped COPI retrieval, not universal generic-vesicle coat or direct budding movie. |
| micro-waters1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2F349248a0%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID1898986 DOI10.1038/349248a0 'Coatomer': a cytosolic protein complex containing subunits of non-clathrin-coated Golgi transport vesicles. Complete primary abstract reports purified cytosolic coatomer sharing Golgi-coated-vesicle subunits; no generic-vesicle molecular census or yeast-specific experiment inferred. |
| micro-karhinen2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14676282+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID14676282 DOI10.1242/jcs.00858 Activity of recycling Golgi mannosyltransferases in the yeast endoplasmic reticulum. Complete primary abstract supports Och1 ER accumulation/activity when COPII export is blocked, plus recycling; conditional ER localization does not negate Golgi residence. |
| micro-nakayama1992-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1628616+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID1628616 DOI10.1002/j.1460-2075.1992.tb05316.x OCH1 encodes a novel membrane bound mannosyltransferase: outer chain elongation of asparagine-linked oligosaccharides. Complete primary abstract supports OCH1 cloning, typeII membrane topology and outer-chain mannosyltransferase function; no fresh body/pixel read. |
| micro-bruinsma2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15229219+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID15229219 DOI10.1074/jbc.m405500200 Retrograde transport of the mannosyltransferase Och1p to the early Golgi requires a component of the COG transport complex. Complete primary abstract distinguishes Och1/Mnn1 mislocalization in cog3-202, Sed5/Sft1 retrograde-vesicle context and intra-Golgi cycling from vacuolar degradation routes. |
| micro-pmid11001058 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11001058+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID11001058 DOI10.1038/35025076 Topological restriction of SNARE-dependent membrane fusion. Parlati2000 complete primary abstract explicitly reconstitutes Sed5/Bos1/Sec22 on one bilayer and Bet1 on the other; eight nonredundant permutations tested. This is a defined ER-Golgi fusion assembly, not the SED5/TLG2/SEC22 cohort. No full body or pixels read. |
| micro-pmid9930650 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9930650+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID9930650 DOI10.1016/s0171-9335(98)80084-8 The Sec1p homologue Vps45p binds to the syntaxin Tlg2p. Nichols1998 complete primary abstract reports Tlg2 as principal Vps45 binding site and a Tlg1/Tlg2/Vps45 triple association, with late-Golgi/endosomal scope. It does not state that Tlg2 belongs to the Sed5/Bos1/Bet1/Sec22 complex. |
| micro-pmid9755865 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9755865+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID9755865 DOI10.1016/s0014-5793(98)01044-8 Gos1p, a Saccharomyces cerevisiae SNARE protein involved in Golgi transport. McNew1998 complete primary abstract describes direct Sed5/Gos1 binding and viable gos1 deletion with modest transport defects. This is another bounded SNARE context, not an exhaustive no-interaction theorem. |
| micro-pmid12941276 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12941276+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact one MED bibliographic record and complete abstract; bodies separately scoped | context_only | PMID12941276 DOI10.1016/s0092-8674(03)00608-1 SNARE selectivity of the COPII coat. Mossessova2003 complete primary abstract distinguishes three COPII binding sites for Bet1/Sed5/Sec22 and favors the Sed5/Bos1/Sec22 t-SNARE assembly. No exact current cohort identity or universal fusion mechanism is inferred. |
| micro-papanikou2014-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4130901/unicode; Genuine NCBI BioC author-manuscript full text; all main paragraphs/passages2-33 and embedded captions150-151, front/abstract0-1; no figure pixels/underlying datasets | context_only | Complete main review supports glycan-processing cohorts, membrane traffic and Rab/Arf coordination while retaining unresolved COPI directionality and cargo questions. It does not attribute SNARE pairing/cycling or the SED5/TLG2/SEC22 set. Secondary model/synthesis remains context, not primary experimental proof. |
| micro-snare-attribution-search | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4130901/unicode; Complete already-read main text BioC passages2-33 plus both captions150-151; excludes bibliography-only references | context_only | Case-insensitive SNARE,SED5,TLG2,SEC22 counts are each0 in the bounded full main text/captions. Manual contextual reading also finds no pairing/cycling claim. This supports only source-placement F1, not biological absence. |
| micro-access-papanikou2014-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC4130901/; Actual attempted route response only | context_only | HTTP200: recaptcha challenge, not body; genuine BioC route separately read. |
| micro-access-papanikou2014-numeric | https://pmc.ncbi.nlm.nih.gov/articles/4130901/; Actual attempted route response only | context_only | HTTP200: recaptcha challenge, not body; genuine BioC route separately read. |
| micro-access-papanikou2014-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4130901/fullTextXML; Actual attempted route response only | context_only | HTTP500: server/access response, not scientific full text. |
| micro-access-letourneur1994-access | https://www.cell.com/cell/fulltext/0092-8674(94)90011-6; Actual attempted route response only | context_only | HTTP403: server/access response, not scientific full text. |
| micro-losev2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf; Complete genuine PDF mainpp1002-1005/Methods/embeddedFig1-4captions; no figure pixels/movies/supplements; independently read shared fresh snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/losev2006-pdf.source | supports | Primary yeast23C4D imaging of Sec7/Vrg4 and additional markers supports transient early-to-late cisternal identity; pulse-chase kinetics are consistent with maturation. Only unambiguously resolved cisternae quantified. Direct cargo tracking and exact recycling pathway remain unresolved. |
| micro-matsuura2006-pdf | https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf; Complete genuine PDF mainpp1007-1009 plus Methods continuation1010 and Fig1-4captions; no pixels/movies/supplements; independently read shared fresh snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/matsuura2006-pdf.source | supports | Primary functional Rer1/Gos1 and Sed5/Sec7 fusions change resident marker distribution in yeast. ret1-1 slows but does not abolish transitions at37C; physical membrane transfer and cargo retention remain unresolved. |
| micro-serafini1991-quoted | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22&amp;pageSize=25; Complete exact MED bibliography and primary abstract only; independently read shared fresh snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/serafini1991-quoted.source | supports | PMID1680566 DOI10.1016/0092-8674(91)90176-y identifies Serafini1991. Abstract reports ARF enrichment on Golgi-derived COP-coated vesicles, removal with uncoating and GTP-dependent membrane binding. Hypothesized GTP-hydrolysis regulation is not promoted to direct universal budding/yeast evidence. |
| micro-datasets | https://imodulondb.org/api/datasets; Complete official /api/datasets response, all20 organism rows/28 organism-dataset pairs; IDs,names,descriptions and lists | context_only | No Saccharomyces/cerevisiae/S288C matching organism or dataset in current bounded catalogue. All three actual pathway-bearing targets require this assessment; no unmatched bacterial proxy or downstream matched-gene/module query applies. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual00:49Z historical datasets invocation; exit1 PermissionError pyvenv.cfg; no fresh execution | context_only | Historical adapter runner unavailable; fresh official catalogue supplies present fallback applicability. Not counted as a newly executed successful adapter command. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record assertions, structured sources and severity rubric | supports | Positive molecular/pathway assertions require a real applicability assessment; absence of expression claims alone is not an exemption. Keep source scope, uncertainty and original finding identity; record curation is separate. |
| septin-curation-policy | docs/CURATION.md; Structural components, molecular grounding and family-or-class guidance | supports | Whole assembled membranes are structures; a LIPID component denotes molecular material and cannot use a complete membrane identity as exact chemical grounding. Taxon-agnostic protein families OR classes are permitted. An optional example inventory is not automatically required for every generic class. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum and grounding contract | supports | Molecular components and whole structures have different identities. Label-only supported lipid material is possible without inventing exact chemical composition. PROTEIN enum prose is interpreted with explicit CURATION generic-class permission; no automatic complex assertion follows from a heterogeneous class. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph nodes, component correspondence, source scope and necessity | supports | Descriptive boundary graphs can remain NONMECHANISTIC; source-specific localization, molecular identity and organelle-formation necessity must not be conflated. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Step2 generic classes and native coverage report | supports | Generic class components are explicitly recognized. A zero-example inventory or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein class does not exist or that its members form one stable complex. |
| septin-record-glyoxysome | data/structures/membrane_organelle/glyoxysome.yaml; Complete current record at f23e1970804e4f93de15a4ae275af84d48e6ce14 | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, taxonomic and canonical scopes, all components and functions, all evidence/graph edges, discussions and history. No images, physical-property measurements, associated traits or verbatim snippets are declared. |
| septin-original-glyoxysome | reviews/structured/20261022T015623Z-glyoxysome-audit/review.yaml; Complete original YAML and deterministic Markdown; source hashes/checks/assessments/findings/actions | supports | Original bytes and historical source observations are preserved. Current target is byte-unchanged. Original finding identities are retained; the new hydrogenosome attribution finding has no invented predecessor. |
| septin-original-validation-glyoxysome | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/original-checks.json; Original native validate/render and git-show historical target SHA | supports | Both native commands exit zero; rendered Markdown is byte-identical and the original frozen hash matches its historical revision. |
| septin-native-glyoxysome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-verify-receipt.json; Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-verify.log | supports | Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory, not all narrative pathway claims. |
| septin-native-glyoxysome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-causal-receipt.json; Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-causal.log | supports | Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory, not all narrative pathway claims. |
| septin-record-hydrogenosomal_membrane | data/structures/membrane_organelle/hydrogenosomal_membrane.yaml; Complete current record at f23e1970804e4f93de15a4ae275af84d48e6ce14 | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, taxonomic and canonical scopes, all components and functions, all evidence/graph edges, discussions and history. No images, physical-property measurements, associated traits or verbatim snippets are declared. |
| septin-original-hydrogenosomal_membrane | reviews/structured/20261022T015639Z-hydrogenosomal-membrane-audit/review.yaml; Complete original YAML and deterministic Markdown; source hashes/checks/assessments/findings/actions | supports | Original bytes and historical source observations are preserved. Current target is byte-unchanged. Original finding identities are retained; the new hydrogenosome attribution finding has no invented predecessor. |
| septin-original-validation-hydrogenosomal_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/original-checks.json; Original native validate/render and git-show historical target SHA | supports | Both native commands exit zero; rendered Markdown is byte-identical and the original frozen hash matches its historical revision. |
| septin-native-hydrogenosomal_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-verify-receipt.json; Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-verify.log | supports | Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory, not all narrative pathway claims. |
| septin-native-hydrogenosomal_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-causal-receipt.json; Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-causal.log | supports | Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory, not all narrative pathway claims. |
| septin-record-hydrogenosome | data/structures/membrane_organelle/hydrogenosome.yaml; Complete current record at f23e1970804e4f93de15a4ae275af84d48e6ce14 | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, taxonomic and canonical scopes, all components and functions, all evidence/graph edges, discussions and history. No images, physical-property measurements, associated traits or verbatim snippets are declared. |
| septin-original-hydrogenosome | reviews/structured/20261022T015641Z-hydrogenosome-audit/review.yaml; Complete original YAML and deterministic Markdown; source hashes/checks/assessments/findings/actions | supports | Original bytes and historical source observations are preserved. Current target is stale and substantively refreshed. Original finding identities are retained; the new hydrogenosome attribution finding has no invented predecessor. |
| septin-original-validation-hydrogenosome | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/original-checks.json; Original native validate/render and git-show historical target SHA | supports | Both native commands exit zero; rendered Markdown is byte-identical and the original frozen hash matches its historical revision. |
| septin-native-hydrogenosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-verify-receipt.json; Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-verify.log | supports | Exit zero. Zero protein examples and three anchored GENE_OR_PROTEIN nodes classified NO_GENE_SYMBOLS for import, pyruvate/energy and ISC classes. This is not an empty typed-node inventory. No accession-specific membership or necessity is certified. |
| septin-native-hydrogenosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-causal-receipt.json; Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-causal.log | supports | Exit zero. Zero protein examples and three anchored GENE_OR_PROTEIN nodes classified NO_GENE_SYMBOLS for import, pyruvate/energy and ISC classes. This is not an empty typed-node inventory. No accession-specific membership or necessity is certified. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009514,GO:0046861,GO:0031908,GO:0005777,GO:0006097,GO:0042566,GO:0046859,GO:0034492,GO:0016020,GO:0043231,GO:0005737; Eleven active exact GO entries: definitions and relation-bearing children | supports | GO0009514 is whole glyoxysome, GO0046861 its complete membrane and GO0031908 its lumen. GO0042566 is hydrogenosome, GO0046859 its complete membrane and GO0034492 its lumen. These assembled membranes are not chemical lipid identities. GO0034492 states the volume enclosed by a hydrogenosome membrane; the word inner is biological contextual interpretation, not verbatim GO wording. Parent and part_of relationships are distinguished. |
| septin-ancestors-0009514 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009514/ancestors?relations=is_a; Exact GO ancestors endpoint with relations=is_a only | supports | Glyoxysome is_a peroxisome GO0005777. |
| septin-ancestors-0042566 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042566/ancestors?relations=is_a; Exact GO ancestors endpoint with relations=is_a only | supports | Hydrogenosome has GO0043231 organelle is_a ancestry; cytoplasm parthood is a separate relationship. |
| septin-ancestors-0046859 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046859/ancestors?relations=is_a; Exact GO ancestors endpoint with relations=is_a only | supports | Hydrogenosomal membrane has broad GO0016020 membrane is_a ancestry, not necessarily a direct named parent edge. |
| septin-SL-0131 | https://rest.uniprot.org/locations/SL-0131.json; Exact location entry, direct GO mapping, names/synonyms and relation-bearing parents | supports | Whole glyoxysome GO0009514; plant/catalase-oriented authority narrative is not independent evidence for Neurospora-specific composition. Nested mappings do not become exact xrefs of the queried structure. |
| septin-SL-0130 | https://rest.uniprot.org/locations/SL-0130.json; Exact location entry, direct GO mapping, names/synonyms and relation-bearing parents | supports | Complete glyoxysome membrane GO0046861, membrane synonym and whole-organelle parthood. Nested mappings do not become exact xrefs of the queried structure. |
| septin-SL-0333 | https://rest.uniprot.org/locations/SL-0333.json; Exact location entry, direct GO mapping, names/synonyms and relation-bearing parents | supports | Glyoxysome matrix GO0031908, lumen synonym and parthood. Nested mappings do not become exact xrefs of the queried structure. |
| septin-SL-0145 | https://rest.uniprot.org/locations/SL-0145.json; Exact location entry, direct GO mapping, names/synonyms and relation-bearing parents | supports | Whole hydrogenosome GO0042566; patchy flagellate/fungal/ciliate scope and hydrogen-producing ATP organelle. Some ciliate examples retain genomes; do not generalize T.vaginalis genome loss universally. Nested mappings do not become exact xrefs of the queried structure. |
| septin-SL-0144 | https://rest.uniprot.org/locations/SL-0144.json; Exact location entry, direct GO mapping, names/synonyms and relation-bearing parents | supports | Complete hydrogenosome membrane GO0046859, hydrogenosomal membrane synonym and organelle parthood. Nested mappings do not become exact xrefs of the queried structure. |
| septin-SL-0335 | https://rest.uniprot.org/locations/SL-0335.json; Exact location entry, direct GO mapping, names/synonyms and relation-bearing parents | supports | Hydrogenosome matrix GO0034492, lumen synonym and parthood. Nested mappings do not become exact xrefs of the queried structure. |
| septin-tax5141 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141; Exact ENA taxonomy entry/rank/lineage/synonyms | supports | Species Neurospora crassa. |
| septin-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Exact ENA taxonomy entry/rank/lineage/synonyms | supports | Domain Eukaryota; broad RARE occurrence means patchy qualitative distribution, not an experimentally measured frequency. |
| septin-tax5722 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5722; Exact ENA taxonomy entry/rank/lineage/synonyms | supports | Species Trichomonas vaginalis, with historical Tritrichomonas vaginalis synonym. This is distinct from Tritrichomonas foetus used in the original Lindmark study. |
| septin-dezoysa1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/BF00309930&amp;pageSize=25; Exact native bibliographic identity and complete abstractText | supports | Complete primary abstract: de Zoysa and Connerton1994 demonstrate nutritionally acetate-induced glyoxysomes in Neurospora crassa and targeting of C-terminally modified CAT reporters. They distinguish glyoxylate-cycle-containing microbodies from catalase-containing peroxisome-like bodies; ARM is ineffective. The publisher PDF is not newly accessible; no uninspected methods/table/strain detail is certified. |
| septin-tachezy2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12922&amp;pageSize=25; Exact native bibliographic identity and complete abstractText | supports | Exact current title is The hydrogenosome of Trichomonas vaginalis, by Tachezy, Makki and Hrdý, year2022. Complete secondary-review abstract supports organelle background, not a new primary experiment. Both assigned hydrogenosomal records carry the wrong title. |
| septin-schneider2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ijpara.2011.10.001&amp;pageSize=25; Exact native bibliographic identity and complete abstractText | supports | Complete primary abstract and exact publication identity/PMID22079833. Year2011 is publication metadata; a later repository manuscript-release date is not a different experiment. |
| septin-bui1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.93.18.9651&amp;pageSize=25; Exact native bibliographic identity and complete abstractText | supports | Complete primary abstract: Hsp70/Hsp60/Hsp10 mitochondrial-family affinity and short N-terminal processing of mature Hsp60 support mitochondrial-type protein ancestry/processing. This does not demonstrate an exclusive universal targeting route; historical early-branching phylogenetic rhetoric is not adopted. |
| septin-sutak2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0401319101&amp;pageSize=25; Exact native bibliographic identity and complete abstractText | supports | Complete primary abstract: TvIscS-2 localizes to hydrogenosomes and hydrogenosomal extracts support FeS reconstitution of apoferredoxin; this does not independently localize every ISC member. |
| septin-dolezal2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0500349102&amp;pageSize=25; Exact native bibliographic identity and complete abstractText | supports | Complete primary abstract: Giardia/T.vaginalis targeting and processing recognize N-terminal and internal signals; shared machinery does not imply every native cargo requires a cleavable presequence. |
| septin-lindmark1973-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A4750424%20AND%20SRC%3AMED&amp;pageSize=25; Exact native bibliographic identity and metadata only, no abstractText | supports | Exact title, authors, year1973, PMID4750424 and DOI10.1016/s0021-9258(19)43249-3 verified. The native record has no abstract; current access is bibliography only. Detailed original Tritrichomonas foetus experiments are not freshly certified. |
| septin-schneider2011-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4437511/unicode; NCBI BioC primary body: complete Introduction and Methods2.1–2.7; Results/Discussion3.1,3.5,3.7,3.8,3.9,3.10; no figure pixels, separate supplements or raw spectra | supports | T.vaginalis T1 hydrogenosome fractionation and mass spectrometry support energy enzymes and ISC proteins, including IscU. The proteome has external associations, potential contaminants and family-level indistinguishable peptides; fraction detection does not independently prove every subcompartment location. Section3.8 explicitly preserves targeting without an N-terminal presequence and stringent motif prediction as an alternative to true signal absence. Translocase candidates/models are not all functionally demonstrated; nondetection is not absence. |
| septin-sutak2004-maintext | https://pmc.ncbi.nlm.nih.gov/articles/PMC478578/; Retained web-reader primary main text: abstract/introduction; Methods lines131–144; Results145–200; Discussion201–209; Fig1–7 caption text, not pixels | supports | Fresh rendered primary text retained in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/primary-web-reader-receipt.json. C-1:NIH30001 T.vaginalis cells, iron-rich/restricted culture, fractionation and immunolocalization directly examine TvIscS-2. FeS reconstitution uses hydrogenosomal lysate and apoferredoxin with cysteine/iron and controls. IscU appears in yeast/bacterial model/interaction discussion, not a T.vaginalis IscU localization experiment. No IscU biological absence inference follows. |
| septin-dolezal2005-indexed-maintext | https://pmc.ncbi.nlm.nih.gov/articles/PMC1182405/; Detailed web-index primary text: returned abstract/introduction, main Methods, Results/Discussion and Fig1–5 caption text; no fresh raw HTML/PDF or figure pixels | supports | Retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/dolezal-indexed-body-receipt.json. Giardia WB, T.vaginalis T1 and yeast YPH499 are distinct experimental systems. Heterologous Giardia GiIscU/Gifdx N-terminal deletions impair targeting; GiIscS has no N-terminal extension and both N-terminal202aa and C-terminal232aa fragments enter hydrogenosomes, supporting internal signals. Processing/EDTA and Pam18 localization support selected machinery properties, not every native cargo or complete functional translocase mechanism. Search-index crawl was reported as six days old; retrieval now does not imply fresh publisher body access. |
| septin-source-access-limits | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/source-receipts.json; Actual fresh route receipts and retained files | supports | Direct/canonical PMC routes returned browser challenges; Sutak/Dolezal BioC returned no-result help pages, not bodies. EuropePMC fullTextXML returned500; S3 guesses returned404. deZoysa PDF endpoint returned HTML Client Challenge; Lindmark PDF returned403; Dolezal UMass download timed out. These routes are not evidence of biological absence or freshly read full text. Successful Schneider BioC, Sutak rendered body and Dolezal indexed body have separately identified scopes. |
| septin-context-glyoxysomal_lumen | data/structures/membrane_organelle/glyoxysomal_lumen.yaml; Frozen boundary context only | supports | Read identity, whole/lumen/membrane distinctions and reciprocal parthood to check assigned record boundaries. This is not a full review or issue disposition of this neighbor. |
| septin-context-glyoxysomal_membrane | data/structures/membrane_organelle/glyoxysomal_membrane.yaml; Frozen boundary context only | supports | Read identity, whole/lumen/membrane distinctions and reciprocal parthood to check assigned record boundaries. This is not a full review or issue disposition of this neighbor. |
| septin-context-hydrogenosome_lumen | data/structures/membrane_organelle/hydrogenosome_lumen.yaml; Frozen boundary context only | supports | Read identity, whole/lumen/membrane distinctions and reciprocal parthood to check assigned record boundaries. This is not a full review or issue disposition of this neighbor. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official iModulonDB catalogue response; all returned organism id/name/dataset-key fields scanned | supports | No returned dataset host matches Neurospora crassa, Trichomonas vaginalis or the other eukaryotic experimental/organellar contexts considered here. No matched-host downstream gene/module query is justified; E.coli recombinant expression is not an organelle-host substitute. This is catalogue noncoverage, not biological absence. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical00:49Z actual runner attempt; not a new invocation | supports | Actual attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z exited1 with PermissionError reading pyvenv.cfg. Runner was unavailable in this environment. Current official HTTP catalogue/source fallback is recorded separately; no successful runner execution is claimed. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2367 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Four assigned targets only, unchanged from original inputs. One inherited major cisterna F1 remains open with exact key, severity and repository-review-finding lineage. Other three qualified passes. No new scientific finding, scientific record curation or terminal neighbor/group/category disposition.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Losev primary PDF: scientific main pp1002–1005, Methods and Figure1–4 captions. Matsuura-Tokita PDF: main pp1007–1009, Methods continuation p1010 and Figure1–4 captions. No figure pixels, movies, supplements or raw microscopy reanalysis. Strain constructions and overexpression/temperature details remain source-bounded; yeast observations do not establish universal kinetics or exclusive cargo routes.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Dean1997 PMID9395539, Serafini1991 PMID1680566 and Bremser1999 PMID10052452 are primary complete-abstract evidence only. Publisher DOI routes for Dean/Serafini yielded short meta-refresh landings, not body. Mammalian ARF/COPI and liposome reconstitution contexts are not silently converted to yeast experiments or coat-alone sufficiency.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Papanikou2014 secondary review JATS sections S1, S3, S4, S5 were independently inspected; other sections and images not certified. This retains unresolved recycling direction, cargo and compartment differences rather than claiming a unique complete maturation mechanism.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Current GO0032580 is_a ancestry lacks0000139; the generic parent is supported by membrane-of-Golgi-compartment definitions, not advertised as a direct native GO assertion. GO/SL topology does not experimentally establish molecular necessity.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: All four targets have empty protein_examples and zero typed GENE_OR_PROTEIN nodes; all eight actual native commands pass in that scope. Explicit maturation, VRG4/GDP-mannose glycosylation and COPI budding narratives still trigger structured-source assessment.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Fresh complete official catalogue contains no S. cerevisiae host; no matched gene/module queries or unrelated-host proxies apply. Noncoverage is not biological absence. Historical runner00:49Z PermissionError remains unavailable; no new runner invocation or successful adapter execution claimed. Initial unquoted Serafini DOI miss was corrected by quoted DOI lookup and not treated as article absence.
- Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Root owns global QC, issues and publication. Read-only source reviewer made no repository/GitHub/record writes. Scratch native preflight validates report shape, not independent proof of every biological claim. Existing unrelated cis-Golgi/coated-vesicle issues remain outside this slice.
- Golgi apparatus and associated vesicle/membrane independent subreview: Assigned Golgi slice: three whole records, original observations and every current edge assessed. One stale apparatus substantively refreshed. Two original request-curation findings persist with exact repository/review/F1 lineages; one new changed-record assembly-scope finding has no invented predecessor. Closed2462/group/category history is not resolved or reopened by this report.
- Golgi apparatus and associated vesicle/membrane independent subreview: Primary imaging scope: shared fresh Losev2006 mainpp1002-1005/Methods/captions and Matsuura2006 mainpp1007-1009 plus Methods continuation1010/captions read independently. No figure pixels, movies, supplements or raw data. Marker transitions do not uniquely establish cargo retention, all recycling routes or a complete molecular determinant set.
- Golgi apparatus and associated vesicle/membrane independent subreview: Papanikou2014 is secondary review; official NCBI BioC main passages2-33 and captions150-151 genuinely read after PMC canonical/numeric challenge and EPMC500. BioC author-manuscript front metadata year differs from exact MED2014 bibliography; no scientific content date substitution. No underlying primary dataset reanalysis.
- Golgi apparatus and associated vesicle/membrane independent subreview: Other source scope: Letourneur1994,Waters1991,Serafini1991,Karhinen2004,Nakayama1992,Bruinsma2004,Parlati2000,Nichols1998,McNew1998,Mossessova2003 complete primary abstracts only. Publisher Letourneur403 response is not a body. No absence of all possible SNARE interactions inferred; finding concerns exact retained physical-complex scope.
- Golgi apparatus and associated vesicle/membrane independent subreview: Native protein scope: six apparatus reviewed S288C examples and two COVERED nodes; other two records empty protein inventories and zero typed nodes. Generic successful verify output is not independently sufficient to infer inventory size or biology. Native CausalNode explicitly permits complexes as GENE_OR_PROTEIN.
- Golgi apparatus and associated vesicle/membrane independent subreview: All three original applicability rows are explicit unsupported expression-only exclusions. Fresh full official catalogue has no matching Saccharomyces dataset, so downstream searches are inapplicable; no biological absence or unmatched proxy. Runner failure is actual historical00:49Z, not new execution. Root globalQC/finalCI remain independently owned and are not borrowed into this source report.
- Golgi apparatus and associated vesicle/membrane independent subreview: Review-only: no record, repository, Git or GitHub mutation. Exact local instructions/config/schema bytes frozen before use; script bytes participate in actual native checks, not a claimed full implementation audit. Scientific curation actions remain proposed and require later owner changes.
- Glyoxysome and hydrogenosome/membrane independent subreview: Read-only source review of three assigned records at exact source head. Root owns all repository/GitHub mutations, dedup/publication, full QC, CI and merge checks; these are not pre-certified here. No record or original review bytes were changed.
- Glyoxysome and hydrogenosome/membrane independent subreview: Current glyoxysome and hydrogenosomal membrane are unchanged. Hydrogenosome is stale: added lumen parthood is supported; the new IscS/IscU source attribution is too broad and is independently filed as a new minor finding with no invented predecessor.
- Glyoxysome and hydrogenosome/membrane independent subreview: Sutak is actual web-reader main text and caption text, not raw publisher HTML or source pixels. Schneider is fresh genuine BioC selected main-text sections (Introduction, all Methods,3.1,3.5,3.7–3.10), not all article sections, supplements, raw spectra or pixels. Dolezal is detailed indexed primary main text read now with reported six-day-old crawl, not a fresh raw body/PDF download; its actual returned Methods/Results/Discussion and caption scopes are explicit.
- Glyoxysome and hydrogenosome/membrane independent subreview: deZoysa1994 and Bui1996 are complete primary-abstract tiers only; the old review body scopes are not claimed as newly reread. Lindmark1973 is exact metadata with no available native abstract; Tachezy2022 is a complete secondary-review abstract. Failed browser/PDF/API routes are retained and are not biological negative evidence.
- Glyoxysome and hydrogenosome/membrane independent subreview: Sutak directly measures TvIscS-2 localization and hydrogenosomal lysate FeS reconstitution. IscU model discussion is not a T.vaginalis localization experiment; Schneider later proteome detection has fractionation/association limits. No claim that IscU is absent follows.
- Glyoxysome and hydrogenosome/membrane independent subreview: Dolezal Giardia proteins expressed in T.vaginalis and yeast/rat processing comparators are distinct experimental systems. Internal signals and N-terminal signals coexist. Lack of predicted motif, lack of proteomic detection, fraction membership and organelle-formation necessity are distinct.
- Glyoxysome and hydrogenosome/membrane independent subreview: All six assigned native protein checks exit0. Glyoxysome/membrane have zero examples and zero typed nodes; hydrogenosome has zero examples and three NO_GENE_SYMBOLS nodes, not zero typed coverage. Generic functional classes are explicitly permitted by the native combined policy; no unsupported single-family/complex identity or mandatory example finding is invented.
- Glyoxysome and hydrogenosome/membrane independent subreview: All three original adapter checks are explicit expression-only exclusions, not omissions. Whole-record pathway/molecular narratives require actual applicability review. Fresh official catalogue lacks relevant eukaryotic host coverage; no foreign-host downstream query or biological absence inference. Historical runner failure is exactly00:49Z, not a newly executed attempt.
- Glyoxysome and hydrogenosome/membrane independent subreview: Twenty-nine frozen repository inputs were actually used:17 common policy/schema/native files,3targets,6original artifacts,3boundary neighbors. Neighbors are context only; no whole-group or historical issue resolution is inferred. No maintained images, quantitative physical properties, traits or verbatim snippets require asset checks.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities. New findings have no invented predecessor.
- Issue #2702 tracks two stale target inputs. Golgi apparatus retypes its existing SNARE cohort to PROTEIN_COMPLEX; the current members and scope are assessed against primary complex evidence and native class guidance. Hydrogenosome adds lumen parthood and FeS-machinery localization edges; topology and source-specific localization claims are reassessed independently.
- Issue #2703 tracks ten unsupported applicability exclusions. All ten original reviews contain an explicit expression-only not_applicable row; none omits it. Actual glyoxylate-cycle/import, glycosylation/SNARE/vesicle trafficking, marker-defined maturation, GDP-mannose transport, COPI budding and energy/FeS/import assertions require bounded catalogue coverage assessment.
- Source commit f23e1970804e4f93de15a4ae275af84d48e6ce14 is retained by tag review-base/pr2367-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. All 50 used local inputs were frozen before assessment. Glyoxysomal lumen, glyoxysomal membrane and hydrogenosome lumen are bounded context only, not additional review targets or dispositions.
- Fresh and reused sources retain actual access times and inspection tiers. Authority identity does not independently establish structure membership, mechanistic action, complex co-membership, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Golgi apparatus has six reviewed yeast examples and two COVERED typed nodes. Hydrogenosome has no examples and three NO_GENE_SYMBOLS nodes anchored to import, pyruvate-metabolism and FeS-machinery class components. The other eight records have no examples or typed molecular nodes. Command success does not certify narrative molecular or source-attribution claims.
- Closed grouped issue #2462 is historical context for the Golgi component-type change, without a disposition of other grouped records. Native-validator issue #2514 remains open and reused. Six related Golgi issue candidates were read fully and concern distinct records/findings.
- Native class-level guidance permits heterogeneous molecular classes when represented honestly. A specific claim that a broad SNARE cohort is one complex is assessed on source-supported membership; enum wording alone is not treated as proof of a defect.
- Ten scientific findings remain open: eight inherited findings concerning whole-membrane/lipid correspondences, whole-cisterna/component correspondence, citation title or SNARE attribution, and import-route qualification; two new changed-record findings concern physical-complex scope and Sutak-specific IscU localization attribution. These map to #2704, #2705, #2706, #2707, #2708, #2709, #2710, #2711, #2712, #2713. Six targets need curation; the associated-vesicle membrane, cisterna membrane, Golgi lumen and Golgi membrane have qualified positive assessments.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T150238Z-pr2367-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2367: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T14:50:16.680122Z'
finished_at: '2026-11-03T15:02:38Z'
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
summary: 'Current-input reassessment of the complete ten-record PR2367 cohort. Two
  stale records are substantively refreshed and ten explicit structured-source applicability
  exclusions corrected. Eight inherited and two new scientific findings remain open
  (five major, five minor), with exact source scopes and lineage: six targets need
  curation and four receive qualified positive assessments. Original review observations
  and all scientific records remain unchanged.'
source:
  git_revision: f23e1970804e4f93de15a4ae275af84d48e6ce14
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
  - path: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
    sha256: 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b
    role: context
  - path: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
    sha256: acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c
    role: context
  - path: data/structures/membrane_organelle/glyoxysome.yaml
    sha256: 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4
    role: target
  - path: data/structures/membrane_organelle/golgi_apparatus.yaml
    sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
    role: target
  - path: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    sha256: 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba
    role: target
  - path: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    sha256: 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413
    role: target
  - path: data/structures/membrane_organelle/golgi_cisterna.yaml
    sha256: 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a
    role: target
  - path: data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
    sha256: 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e
    role: target
  - path: data/structures/membrane_organelle/golgi_lumen.yaml
    sha256: 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b
    role: target
  - path: data/structures/membrane_organelle/golgi_membrane.yaml
    sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
    role: target
  - path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    sha256: 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56
    role: target
  - path: data/structures/membrane_organelle/hydrogenosome.yaml
    sha256: 6d295ad6b0bb5066ddec461e6c2ffa142de9d8590d705eff6a3648bc6c01e77a
    role: target
  - path: data/structures/membrane_organelle/hydrogenosome_lumen.yaml
    sha256: 30c5139da8ac02b5d677b314f371d09b1a64fa10a6bb45352d3b8b76c298fd40
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
  - path: reviews/structured/20261022T015623Z-glyoxysome-audit/review.md
    sha256: 9129675608fae01c7485a9ee2be06b3379d77eae618e1407ecb1daecd755545d
    role: context
  - path: reviews/structured/20261022T015623Z-glyoxysome-audit/review.yaml
    sha256: d8001c6c4dae6eb0a72cb217399091bd4f5e908e9b2d90a6d989f49067e3be87
    role: context
  - path: reviews/structured/20261022T015625Z-golgi-apparatus-audit/review.md
    sha256: 7c94548b5be09bcd6b712bb460c2426e2684cc1676cbd2900431c552fe65df11
    role: context
  - path: reviews/structured/20261022T015625Z-golgi-apparatus-audit/review.yaml
    sha256: cb166fb37e26b8d9adf35fa778621d967b784d539ec33132af70c72a2b27629c
    role: context
  - path: reviews/structured/20261022T015627Z-golgi-associated-vesicle-audit/review.md
    sha256: 3657da3f9812730e335ae513eaf38463300ca925e9ee2eeb4a189044f5c783d2
    role: context
  - path: reviews/structured/20261022T015627Z-golgi-associated-vesicle-audit/review.yaml
    sha256: 33f0b26a7e2e46f7ceb29252cffc584836231b7847812af9c8db112538aa81da
    role: context
  - path: reviews/structured/20261022T015629Z-golgi-associated-vesicle-membrane-audit/review.md
    sha256: 0bc6786057ccb503160270db6a9a53fa04066d31774236177379a710f6aea6eb
    role: context
  - path: reviews/structured/20261022T015629Z-golgi-associated-vesicle-membrane-audit/review.yaml
    sha256: dd9c7ba2848fed56c12bbb5c85532edf92fa1710542bb8d5c6d7f2905a754f02
    role: context
  - path: reviews/structured/20261022T015631Z-golgi-cisterna-audit/review.md
    sha256: 4743fa3b915e223354492874c71aece8912bb1d660365dca2f68f0ff7758821f
    role: context
  - path: reviews/structured/20261022T015631Z-golgi-cisterna-audit/review.yaml
    sha256: bd50be966e334641fc2782a1c7698bdb97ba4399c0510c6cde76a56eacfba209
    role: context
  - path: reviews/structured/20261022T015633Z-golgi-cisterna-membrane-audit/review.md
    sha256: 005f9b01ce3e1dbadf8db4fc184f4d46722d11e95b85671dae4348cdde6a2ab6
    role: context
  - path: reviews/structured/20261022T015633Z-golgi-cisterna-membrane-audit/review.yaml
    sha256: 85ffb40585d78de3deda18781b3969635f205174f533ff6aea32c19ecac73af0
    role: context
  - path: reviews/structured/20261022T015635Z-golgi-lumen-audit/review.md
    sha256: fa423200df3c599238a997bbd5fd8396b2e5c62c844deeca6a4a91ffc3b3d22b
    role: context
  - path: reviews/structured/20261022T015635Z-golgi-lumen-audit/review.yaml
    sha256: c68d31506cd1e80a4417568f57fa3c37ba20d8c10d49a392b7bec48c9e5fc45d
    role: context
  - path: reviews/structured/20261022T015637Z-golgi-membrane-audit/review.md
    sha256: 5c9270fce5a1cc52206b8232e5eda72f5b5d697da0264b23e0c0dd2ebafe4ad5
    role: context
  - path: reviews/structured/20261022T015637Z-golgi-membrane-audit/review.yaml
    sha256: 61b9f8288eed3c489af4ccec038e29c6e990aaee55b6020faa673fa1392ad829
    role: context
  - path: reviews/structured/20261022T015639Z-hydrogenosomal-membrane-audit/review.md
    sha256: 92c8711c2722109be2a1d159c3b225135733e4be816c71050f421c3bc7ad7c3a
    role: context
  - path: reviews/structured/20261022T015639Z-hydrogenosomal-membrane-audit/review.yaml
    sha256: d85c84493415c834ae784d33ec2e6906566d942c4880d08fd1f1e6b20df06acf
    role: context
  - path: reviews/structured/20261022T015641Z-hydrogenosome-audit/review.md
    sha256: f31bc3f2660703023c978fb27a8eebe0d0ecb98e9bb63a9aaaa8a0a138f36571
    role: context
  - path: reviews/structured/20261022T015641Z-hydrogenosome-audit/review.yaml
    sha256: 4c3ed7f07ba46d5c587c8697067749c64005bd04d54b2306fbfea35ef8c9df17
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
- target_id: GO:0009514
  path: data/structures/membrane_organelle/glyoxysome.yaml
  label: glyoxysome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glyoxysome.yaml
    role: maintained scientific record
- target_id: GO:0005794
  path: data/structures/membrane_organelle/golgi_apparatus.yaml
  label: Golgi apparatus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
- target_id: GO:0005798
  path: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
  label: Golgi-associated vesicle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    role: maintained scientific record
- target_id: GO:0030660
  path: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  label: Golgi-associated vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031985
  path: data/structures/membrane_organelle/golgi_cisterna.yaml
  label: Golgi cisterna
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_cisterna.yaml
    role: maintained scientific record
- target_id: GO:0032580
  path: data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
  label: Golgi cisterna membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
    role: maintained scientific record
- target_id: GO:0005796
  path: data/structures/membrane_organelle/golgi_lumen.yaml
  label: Golgi lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_lumen.yaml
    role: maintained scientific record
- target_id: GO:0000139
  path: data/structures/membrane_organelle/golgi_membrane.yaml
  label: Golgi membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_membrane.yaml
    role: maintained scientific record
- target_id: GO:0046859
  path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  label: hydrogenosomal membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    role: maintained scientific record
- target_id: GO:0042566
  path: data/structures/membrane_organelle/hydrogenosome.yaml
  label: hydrogenosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 144d19dec1ea5ad91cc299a6711e3fec9c157056.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    07860cdd96065310a36fb2173dbcee46b957e995.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head f23e1970804e4f93de15a4ae275af84d48e6ce14.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head f23e1970804e4f93de15a4ae275af84d48e6ce14.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head f23e1970804e4f93de15a4ae275af84d48e6ce14.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head f23e1970804e4f93de15a4ae275af84d48e6ce14.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head f23e1970804e4f93de15a4ae275af84d48e6ce14.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0009514
  status: passed
  required: true
  target_ids:
  - GO:0009514
  command: just validate data/structures/membrane_organelle/glyoxysome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0009514
  status: passed
  required: true
  target_ids:
  - GO:0009514
  command: just validate-strict data/structures/membrane_organelle/glyoxysome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0005794
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just validate data/structures/membrane_organelle/golgi_apparatus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0005794
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: just validate-strict data/structures/membrane_organelle/golgi_apparatus.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0005798
  status: passed
  required: true
  target_ids:
  - GO:0005798
  command: just validate data/structures/membrane_organelle/golgi_associated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0005798
  status: passed
  required: true
  target_ids:
  - GO:0005798
  command: just validate-strict data/structures/membrane_organelle/golgi_associated_vesicle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0030660
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just validate data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0030660
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: just validate-strict data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0031985
  status: passed
  required: true
  target_ids:
  - GO:0031985
  command: just validate data/structures/membrane_organelle/golgi_cisterna.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0031985
  status: passed
  required: true
  target_ids:
  - GO:0031985
  command: just validate-strict data/structures/membrane_organelle/golgi_cisterna.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0032580
  status: passed
  required: true
  target_ids:
  - GO:0032580
  command: just validate data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0032580
  status: passed
  required: true
  target_ids:
  - GO:0032580
  command: just validate-strict data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0005796
  status: passed
  required: true
  target_ids:
  - GO:0005796
  command: just validate data/structures/membrane_organelle/golgi_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0005796
  status: passed
  required: true
  target_ids:
  - GO:0005796
  command: just validate-strict data/structures/membrane_organelle/golgi_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0000139
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just validate data/structures/membrane_organelle/golgi_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0000139
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: just validate-strict data/structures/membrane_organelle/golgi_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0046859
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just validate data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0046859
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just validate-strict data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0042566
  status: passed
  required: true
  target_ids:
  - GO:0042566
  command: just validate data/structures/membrane_organelle/hydrogenosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0042566
  status: passed
  required: true
  target_ids:
  - GO:0042566
  command: just validate-strict data/structures/membrane_organelle/hydrogenosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367
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
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  summary: All ten explicit expression-only exclusions are corrected using complete-record
    molecular/pathway assertions. Fresh complete official catalogue responses and
    bounded searches for Saccharomyces, Neurospora and Trichomonas host coverage yield
    no matching datasets. No unmatched host proxy or unsupported downstream query
    is used. Noncoverage is not biological absence. Historical adapter-runner unavailability
    keeps its actual timestamp and is not represented as a fresh execution.
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-datasets
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-rubric
  - plaque-protein-contract
  - plaque-schema-policy
  - plaque-go
  - plaque-ancestors-0031985
  - plaque-ancestors-0032580
  - plaque-ancestors-0005796
  - plaque-ancestors-0000139
  - plaque-tax4932
  - plaque-SL0133
  - plaque-losev2006-meta
  - plaque-matsuura2006-meta
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
  - plaque-dean1997-meta
  - plaque-serafini1991-quoted
  - plaque-go-budding-primary-10052452
  - plaque-papanikou2014-s3
  - plaque-dean1997-publisher
  - plaque-serafini1991-publisher
  - plaque-catalogue
  - micro-policy
  - micro-component-policy
  - micro-graph-policy
  - micro-go
  - micro-tax4932
  - micro-tax559292
  - micro-protein-P31755
  - micro-protein-P39106
  - micro-protein-P27809
  - micro-protein-Q01590
  - micro-protein-Q08144
  - micro-protein-P22214
  - micro-papanikou2014-bioc
  - micro-access-papanikou2014-body
  - micro-access-papanikou2014-numeric
  - micro-access-papanikou2014-xml
  - micro-access-letourneur1994-access
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-serafini1991-quoted
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-graph-policy
  - septin-protein-policy
  - septin-go
  - septin-ancestors-0009514
  - septin-ancestors-0042566
  - septin-ancestors-0046859
  - septin-SL-0131
  - septin-SL-0130
  - septin-SL-0333
  - septin-SL-0145
  - septin-SL-0144
  - septin-SL-0335
  - septin-tax5141
  - septin-tax2759
  - septin-tax5722
  - septin-dezoysa1994-meta
  - septin-tachezy2022-meta
  - septin-schneider2011-meta
  - septin-bui1996-meta
  - septin-sutak2004-meta
  - septin-dolezal2005-meta
  - septin-lindmark1973-meta
  - septin-schneider2011-bioc
  - septin-sutak2004-maintext
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
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
- check_id: glyoxysome-uniprot-verify
  name: Native glyoxysome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009514
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glyoxysome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glyoxysome-verify
- check_id: glyoxysome-uniprot-causal
  name: Native glyoxysome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009514
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glyoxysome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glyoxysome-causal
- check_id: golgi_apparatus-uniprot-verify
  name: Native Golgi apparatus UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Six reviewed S. cerevisiae S288C
    examples (OCH1/P31755, MNN1/P39106, KRE2/P27809, SED5/Q01590, TLG2/Q08144, SEC22/P22214)
    and two COVERED nodes. Identity does not establish that the SNARE cohort is one
    complex or certify every mechanistic assertion.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-golgi_apparatus-verify
- check_id: golgi_apparatus-uniprot-causal
  name: Native Golgi apparatus UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005794
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Six reviewed S. cerevisiae S288C
    examples (OCH1/P31755, MNN1/P39106, KRE2/P27809, SED5/Q01590, TLG2/Q08144, SEC22/P22214)
    and two COVERED nodes. Identity does not establish that the SNARE cohort is one
    complex or certify every mechanistic assertion.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-golgi_apparatus-causal
- check_id: golgi_associated_vesicle-uniprot-verify
  name: Native Golgi-associated vesicle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005798
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-golgi_associated_vesicle-verify
- check_id: golgi_associated_vesicle-uniprot-causal
  name: Native Golgi-associated vesicle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005798
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-golgi_associated_vesicle-causal
- check_id: golgi_associated_vesicle_membrane-uniprot-verify
  name: Native Golgi-associated vesicle membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-golgi_associated_vesicle_membrane-verify
- check_id: golgi_associated_vesicle_membrane-uniprot-causal
  name: Native Golgi-associated vesicle membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030660
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-golgi_associated_vesicle_membrane-causal
- check_id: golgi_cisterna-uniprot-verify
  name: Native Golgi cisterna UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031985
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_cisterna-verify
- check_id: golgi_cisterna-uniprot-causal
  name: Native Golgi cisterna UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031985
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_cisterna-causal
- check_id: golgi_cisterna_membrane-uniprot-verify
  name: Native Golgi cisterna membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0032580
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_cisterna_membrane-verify
- check_id: golgi_cisterna_membrane-uniprot-causal
  name: Native Golgi cisterna membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0032580
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_cisterna_membrane-causal
- check_id: golgi_lumen-uniprot-verify
  name: Native Golgi lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005796
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_lumen-verify
- check_id: golgi_lumen-uniprot-causal
  name: Native Golgi lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005796
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_lumen-causal
- check_id: golgi_membrane-uniprot-verify
  name: Native Golgi membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_membrane-verify
- check_id: golgi_membrane-uniprot-causal
  name: Native Golgi membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000139
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-golgi_membrane-causal
- check_id: hydrogenosomal_membrane-uniprot-verify
  name: Native hydrogenosomal membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-hydrogenosomal_membrane-verify
- check_id: hydrogenosomal_membrane-uniprot-causal
  name: Native hydrogenosomal membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. This record has no represented
    protein examples and no typed molecular nodes; narrative molecular/pathway assertions
    are assessed separately.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-hydrogenosomal_membrane-causal
- check_id: hydrogenosome-uniprot-verify
  name: Native hydrogenosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042566
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/hydrogenosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples; three NO_GENE_SYMBOLS
    typed nodes are anchored to import machinery, pyruvate-metabolism enzymes and
    FeS machinery class components. This is not individual protein verification or
    source-level localization proof.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-hydrogenosome-verify
- check_id: hydrogenosome-uniprot-causal
  name: Native hydrogenosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042566
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/hydrogenosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No protein examples; three NO_GENE_SYMBOLS
    typed nodes are anchored to import machinery, pyruvate-metabolism enzymes and
    FeS machinery class components. This is not individual protein verification or
    source-level localization proof.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-hydrogenosome-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4;
    current SHA256 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T015623Z-glyoxysome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d8001c6c4dae6eb0a72cb217399091bd4f5e908e9b2d90a6d989f49067e3be87
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 b064dc1116ec2814e2ecb946d8ebd554a4b176494c2259ff7e458bac0d3e5eb1;
    current SHA256 e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca.
    Changed record reassessed against current sources.
  snapshot_sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T015625Z-golgi-apparatus-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: cb166fb37e26b8d9adf35fa778621d967b784d539ec33132af70c72a2b27629c
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba;
    current SHA256 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba.
    Record bytes unchanged since the original review.
  snapshot_sha256: 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T015627Z-golgi-associated-vesicle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 33f0b26a7e2e46f7ceb29252cffc584836231b7847812af9c8db112538aa81da
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413;
    current SHA256 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T015629Z-golgi-associated-vesicle-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: dd9c7ba2848fed56c12bbb5c85532edf92fa1710542bb8d5c6d7f2905a754f02
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_cisterna.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a;
    current SHA256 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a.
    Record bytes unchanged since the original review.
  snapshot_sha256: 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T015631Z-golgi-cisterna-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: bd50be966e334641fc2782a1c7698bdb97ba4399c0510c6cde76a56eacfba209
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e;
    current SHA256 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T015633Z-golgi-cisterna-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 85ffb40585d78de3deda18781b3969635f205174f533ff6aea32c19ecac73af0
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b;
    current SHA256 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b.
    Record bytes unchanged since the original review.
  snapshot_sha256: 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T015635Z-golgi-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c68d31506cd1e80a4417568f57fa3c37ba20d8c10d49a392b7bec48c9e5fc45d
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c;
    current SHA256 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c.
    Record bytes unchanged since the original review.
  snapshot_sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T015637Z-golgi-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 61b9f8288eed3c489af4ccec038e29c6e990aaee55b6020faa673fa1392ad829
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56;
    current SHA256 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T015639Z-hydrogenosomal-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d85c84493415c834ae784d33ec2e6906566d942c4880d08fd1f1e6b20df06acf
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Original frozen SHA256 cbe6ff879b7bc2477e475394c4361107d4d033bfeba79e4a85c03787b27b8b70;
    current SHA256 6d295ad6b0bb5066ddec461e6c2ffa142de9d8590d705eff6a3648bc6c01e77a.
    Changed record reassessed against current sources.
  snapshot_sha256: 6d295ad6b0bb5066ddec461e6c2ffa142de9d8590d705eff6a3648bc6c01e77a
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T015641Z-hydrogenosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T15:02:38Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 4c3ed7f07ba46d5c587c8697067749c64005bd04d54b2306fbfea35ef8c9df17
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_cisterna.yaml
  locator: Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14;
    all fields, histories, discussions and graphs
  summary: Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific
    record curation performed.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: 09ebdf2a8646a8f51638cd933e9523e9e9170e0610567ad3e09efa7a97c6de7a
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261022T015631Z-golgi-cisterna-audit/review.yaml
  locator: Exact staleness-listed authoritative YAML/Markdown, input hashes, checks,
    assessments, findings/actions and limitations
  summary: Original pair validates and renders exactly; all 14 historical inputs match
    its source. Historical verdict independently reassessed; original remains immutable.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: bd50be966e334641fc2782a1c7698bdb97ba4399c0510c6cde76a56eacfba209
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
  locator: Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14;
    all fields, histories, discussions and graphs
  summary: Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific
    record curation performed.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: 4157a0d579677dd5e6e32cb11bb215bfc414f18833e120abf0a19b892029b62e
- evidence_id: plaque-original-5
  kind: prior_review
  reference: reviews/structured/20261022T015633Z-golgi-cisterna-membrane-audit/review.yaml
  locator: Exact staleness-listed authoritative YAML/Markdown, input hashes, checks,
    assessments, findings/actions and limitations
  summary: Original pair validates and renders exactly; all 17 historical inputs match
    its source. Historical verdict independently reassessed; original remains immutable.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: 85ffb40585d78de3deda18781b3969635f205174f533ff6aea32c19ecac73af0
- evidence_id: plaque-current-6
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_lumen.yaml
  locator: Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14;
    all fields, histories, discussions and graphs
  summary: Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific
    record curation performed.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: 609cac48e5a5d75c55ed731b281a531dbe76e9db2ad105b228f17194399f608b
- evidence_id: plaque-original-6
  kind: prior_review
  reference: reviews/structured/20261022T015635Z-golgi-lumen-audit/review.yaml
  locator: Exact staleness-listed authoritative YAML/Markdown, input hashes, checks,
    assessments, findings/actions and limitations
  summary: Original pair validates and renders exactly; all 16 historical inputs match
    its source. Historical verdict independently reassessed; original remains immutable.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: c68d31506cd1e80a4417568f57fa3c37ba20d8c10d49a392b7bec48c9e5fc45d
- evidence_id: plaque-current-7
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_membrane.yaml
  locator: Entire maintained record at source f23e1970804e4f93de15a4ae275af84d48e6ce14;
    all fields, histories, discussions and graphs
  summary: Target unchanged from original frozen bytes. PROPOSED unchanged; no scientific
    record curation performed.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: 22a35f67a05738d876923e98adfe54cde34ee23c9009667f48676dca83ba708c
- evidence_id: plaque-original-7
  kind: prior_review
  reference: reviews/structured/20261022T015637Z-golgi-membrane-audit/review.yaml
  locator: Exact staleness-listed authoritative YAML/Markdown, input hashes, checks,
    assessments, findings/actions and limitations
  summary: Original pair validates and renders exactly; all 17 historical inputs match
    its source. Historical verdict independently reassessed; original remains immutable.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: supports
  snapshot_sha256: 61b9f8288eed3c489af4ccec038e29c6e990aaee55b6020faa673fa1392ad829
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Genes, proteins, regulators, pathways, stress responses and traits trigger
    structured-source assessment. Empty inventories or lack of transcriptomic assertions
    do not waive positive pathway claims.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native contract and relevant definitions
  summary: Exact identity, source scope, taxonomy, molecular composition and necessity
    require separate assessment; optional empty inventories are not themselves defects.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Physical topology and broad descriptive function remain distinct from exact
    molecular mechanism, and each directed claim requires inspected support.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Native protein commands verify represented accessions and typed graph actors;
    their scope does not independently certify narrative pathways.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native contract and relevant definitions
  summary: StructuralComponent denotes a molecular building block; CausalNode.component_ref
    identifies a node that is one of the structure own components. A whole compartment
    is not identical to its lipid constituent.
  accessed_at: '2026-11-03T14:58:26.861908Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031985,GO:0032580,GO:0005796,GO:0000139,GO:0098791,GO:0005794,GO:0016020,GO:0070013,GO:0030126,GO:0035964
  locator: 'Complete exact responses for GO0031985,0032580,0005796,0000139,0098791,0005794,0016020,0070013,0030126,0035964:
    names, definitions, synonyms and typed children'
  summary: GO separates whole cisterna, its membrane, lumen and generic Golgi membrane.
    Cisterna is a Golgi subcompartment; membrane/lumen are parts of Golgi. GO0070013
    lists Golgi lumen as is_a. COPI coat and COPI budding definitions support generic
    coat-associated vesicle formation. Ontology membership is not a species-specific
    necessity experiment.
  accessed_at: '2026-11-03T14:52:02.136910Z'
  support: supports
  snapshot_sha256: 154a8c56ad14ed63db426195a16677a15191919d23d92493aaefbbe8fc728403
- evidence_id: plaque-ancestors-0031985
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031985/ancestors?relations=is_a
  locator: Exact current QuickGO is_a-only ancestor response
  summary: GO0031985 is_a ancestry includes Golgi subcompartment0098791.
  accessed_at: '2026-11-03T14:52:02.788879Z'
  support: supports
  snapshot_sha256: 8d6901234fe5a2f3d5615449632512415d3ac5d349606b7cbad27cf47a0923b9
- evidence_id: plaque-ancestors-0032580
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032580/ancestors?relations=is_a
  locator: Exact current QuickGO is_a-only ancestor response
  summary: GO0032580 is_a ancestry includes generic membrane0016020 but does not contain
    Golgi membrane0000139. The record broader parent0000139 is definition-supported;
    no direct native GO edge is claimed.
  accessed_at: '2026-11-03T14:52:02.798521Z'
  support: supports
  snapshot_sha256: 12288291f9a9c628cee797ad00a70433e34a730fc26e111546432babcd575627
- evidence_id: plaque-ancestors-0005796
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005796/ancestors?relations=is_a
  locator: Exact current QuickGO is_a-only ancestor response
  summary: GO0005796 is_a ancestry includes organelle lumen0070013.
  accessed_at: '2026-11-03T14:52:02.804014Z'
  support: supports
  snapshot_sha256: ed577af5530e753012ed42f9eb1f728aed57cb6b565eb588c56213dfa530c865
- evidence_id: plaque-ancestors-0000139
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139/ancestors?relations=is_a
  locator: Exact current QuickGO is_a-only ancestor response
  summary: GO0000139 is_a ancestry includes membrane0016020.
  accessed_at: '2026-11-03T14:52:02.857496Z'
  support: supports
  snapshot_sha256: c423ff74b8b8b7ad57c67c74cd15a0603fade2086c012fa2e6c23cd5fe928851
- evidence_id: plaque-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: 'Complete ENA native taxonomy response: taxId/scientificName/rank/lineage'
  summary: NCBITaxon4932 is Saccharomyces cerevisiae. Species identity is not a measured
    prevalence or interchangeable experimental strain.
  accessed_at: '2026-11-03T14:52:02.137108Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-SL0133
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0133.json
  locator: Complete native subcellular-location definition/synonyms and exact GO cross-reference
  summary: SL0133 denotes Golgi apparatus lumen with Golgi complex lumen synonym and
    GO0005796 cross-reference. It is distinct from Golgi membrane; no protein inventory
    inferred.
  accessed_at: '2026-11-03T14:52:02.137202Z'
  support: supports
  snapshot_sha256: db090af725f66e8271ad2dd917ebf991d77934ca4ebb51897390e3aee1760354
- evidence_id: plaque-losev2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature04717&pageSize=25
  locator: Exact PMID16699524 primary metadata and complete abstract
  summary: Losev et al.2006 DOI10.1038/nature04717 reports cisternal maturation directly
    visualized in S. cerevisiae. Bibliographic attribution matches; detailed scope
    separately checked against primary PDF.
  accessed_at: '2026-11-03T14:52:02.137257Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI or PMID lookup at 2026-11-03T14:52:02.137257Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature04717&pageSize=25;
    pageSize25; inspected 1 returned metadata/abstract matches. No open-ended bibliography
    or full-body inference.
  snapshot_sha256: 006f568bfaef358b1d74f64e1d3f13148a8d5fe4fb9f10078695139e79be6fe3
- evidence_id: plaque-matsuura2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature04737&pageSize=25
  locator: Exact PMID16699523 primary metadata and complete abstract
  summary: Matsuura-Tokita et al.2006 DOI10.1038/nature04737 reports live imaging
    of yeast Golgi cisternal maturation. Exact author/year/source identity matches;
    detailed scope separately checked against primary PDF.
  accessed_at: '2026-11-03T14:52:02.137303Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI or PMID lookup at 2026-11-03T14:52:02.137303Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature04737&pageSize=25;
    pageSize25; inspected 1 returned metadata/abstract matches. No open-ended bibliography
    or full-body inference.
  snapshot_sha256: ae337df2a99b977611cc9b7a73babf2c1c65045c0559cdad157dba77cf467655
- evidence_id: plaque-losev2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf
  locator: Fresh university-hosted primary PDF, complete scientific main text pp1002–1005,
    Methods and Figure1–4 captions read via text extraction; no figure pixels/movies/supplements
  summary: Individually resolved budding-yeast cisternae transition resident markers
    including Vrg4 to Sec7; additional marker pairs support changing identity. Four-dimensional
    microscopy and pulse-chase consistency support maturation. Direct cargo residence
    and specific recycling mechanism remain unresolved. Unstacked yeast cisternae
    are not evidence that all Golgi stacks or all eukaryotic compartments use an exclusive
    route.
  accessed_at: '2026-11-03T14:52:02.143799Z'
  support: supports
  snapshot_sha256: 9cd6a98c307575ce19f0b88a5943b10dc7732d655c2b75a9d34228a4fbbc188f
- evidence_id: plaque-matsuura2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf
  locator: Fresh university-hosted primary PDF, scientific main pp1007–1009, Methods
    continuation paragraph p1010 and Figure1–4 captions; no figure pixels/movies/supplements
  summary: S. cerevisiae Rer1/Gos1 and Sed5/Sec7 markers change during individual
    cisternal maturation. ret1-1 alpha-COP mutation slows but does not abolish changes
    under stated temperature conditions. Primary observations support scoped maturation;
    proposed tubular/vesicular contacts do not uniquely establish the mechanism or
    universal cargo route.
  accessed_at: '2026-11-03T14:52:02.743056Z'
  support: supports
  snapshot_sha256: e0e393bc775432869db495e2a836df223a0be5128ab04aae51a9d31bbf323583
- evidence_id: plaque-dean1997-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9395539%20AND%20SRC%3AMED&pageSize=25
  locator: Exact PMID9395539 primary bibliographic match and complete abstract only
  summary: Dean, Zhang and Poster1997 DOI10.1074/jbc.272.50.31908 describes specific
    GDP-mannose transport defects in Golgi vesicles from vrg4 mutants, altered mannosylation
    and Vrg4 localization to Golgi membranes. Supports nucleotide-sugar access to
    the lumen and boundary transporter context, not purified-protein reconstitution,
    individual organelle-formation necessity or stable lumen residency.
  accessed_at: '2026-11-03T14:52:02.141645Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI or PMID lookup at 2026-11-03T14:52:02.141645Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9395539%20AND%20SRC%3AMED&pageSize=25;
    pageSize25; inspected 1 returned metadata/abstract matches. No open-ended bibliography
    or full-body inference.
  snapshot_sha256: eec644e5832215346c59d07f1d69c0b3fde10ab6f26b1973b32007ed6af663be
- evidence_id: plaque-serafini1991-quoted
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22&pageSize=25
  locator: 'Exact quoted DOI match PMID1680566: complete primary abstract and bibliographic/MESH
    context only'
  summary: Serafini et al.1991 DOI10.1016/0092-8674(91)90176-y identifies ARF in Golgi-derived
    vesicle coats, GTP-dependent membrane recruitment and release during uncoating.
    Supports coat assembly/regulatory context. Mammalian source context is not a yeast-specific
    experiment, and abstract does not prove coat-alone force generation.
  accessed_at: '2026-11-03T14:52:21.515779Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI or PMID lookup at 2026-11-03T14:52:21.515779Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22&pageSize=25;
    pageSize25; inspected 1 returned metadata/abstract matches. No open-ended bibliography
    or full-body inference.
  snapshot_sha256: dea8968c03304cd9777691eda5c7ba9969cbd3d2e353a2a5c9ac6ff2ac69538f
- evidence_id: plaque-go-budding-primary-10052452
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10052452%20AND%20SRC%3AMED&pageSize=25
  locator: Exact PMID10052452 primary abstract; primary reference linked from GO0035964
  summary: Bremser et al.1999 DOI10.1016/s0092-8674(00)80654-6 reconstitutes coat
    assembly/budding on liposomes resembling mammalian Golgi membranes with coatomer,
    ARF, GTP and cargo-receptor tails. Conditional reconstitution supports COPI participation,
    not isolated coat sufficiency or direct yeast experimentation.
  accessed_at: '2026-11-03T14:53:56.193247Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI or PMID lookup at 2026-11-03T14:53:56.193247Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10052452%20AND%20SRC%3AMED&pageSize=25;
    pageSize25; inspected 1 returned metadata/abstract matches. No open-ended bibliography
    or full-body inference.
  snapshot_sha256: 139f283582c68acdce01f7dbf72eeb3ba64403ad3a55436d561edec7dd344131
- evidence_id: plaque-papanikou2014-s3
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4130901.1/PMC4130901.1.xml
  locator: Genuine PMC secondary-review JATS; complete sections S1 Introduction, S3
    cisternal assembly, S4 carbohydrate synthesis, S5 carrier formation, independently
    read; other sections and figure pixels not certified
  summary: Papanikou and Glick2014 review supports compartment identity, cisternal
    maturation and carrier-recycling context while retaining unresolved directions,
    cargo roles and compartment differences. Secondary synthesis is not a fresh primary
    experiment; broad COPI participation is not generalized to every Golgi compartment
    or a unique maturation mechanism.
  accessed_at: '2026-11-03T14:53:56.189004Z'
  support: supports
  snapshot_sha256: a31a9bdff52328a13063bad92ce03bdfcee7eff623b23b6b1a27d7509a1441e4
- evidence_id: plaque-dean1997-publisher
  kind: authority
  reference: https://doi.org/10.1074/jbc.272.50.31908
  locator: HTTP200 DOI route returned short HTML meta-refresh landing, not an article
    body
  summary: Full publisher body was not obtained on this route. Actual scientific assessment
    uses the separately inspected complete primary abstract; no full-body inspection
    inferred from HTTP200.
  accessed_at: '2026-11-03T14:53:56.190547Z'
  support: context_only
  snapshot_sha256: 87e3592c76047caa42a5601093177e51a5a521a6f1ab6a42703b56565b440896
- evidence_id: plaque-serafini1991-publisher
  kind: authority
  reference: https://doi.org/10.1016/0092-8674(91)90176-y
  locator: HTTP200 DOI route returned short HTML meta-refresh landing, not an article
    body
  summary: Full publisher body was not obtained on this route. Actual scientific assessment
    uses the separately inspected complete primary abstract; no full-body inspection
    inferred from HTTP200.
  accessed_at: '2026-11-03T14:53:56.191721Z'
  support: context_only
  snapshot_sha256: 7810a8111f1ca0ae9de5cf39f90bea54f17dce8020453ce48512880b5270f117
- evidence_id: plaque-serafini1991-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/0092-8674(91)90176-y&pageSize=25
  locator: Initial unquoted exact-DOI query, pageSize25, zero returned matches
  summary: This unsuccessful query was corrected with an exact quoted DOI query yielding
    PMID1680566. Zero results were not interpreted as absence of the article or biological
    evidence.
  accessed_at: '2026-11-03T14:52:02.137661Z'
  support: context_only
  search_scope: Bounded EuropePMC core exact DOI or PMID lookup at 2026-11-03T14:52:02.137661Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/0092-8674(91)90176-y&pageSize=25;
    pageSize25; inspected 0 returned metadata/abstract matches. No open-ended bibliography
    or full-body inference.
  snapshot_sha256: 219f997dad697df57b193eecb00886f62172fb25ab570a38363c0630739da99b
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official /api/datasets response; every returned organism
    row/dataset listing inspected, no pagination
  summary: No S. cerevisiae host appears in the returned catalogue. Cisternal maturation,
    VRG4/GDP-mannose glycosylation and COPI budding are genuine triggers, but no matched
    downstream gene/module query applies. Unrelated bacterial/archaeal datasets are
    not proxies; noncoverage is not negative biology and generated module prose is
    excluded.
  accessed_at: '2026-11-03T14:52:02.863090Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt; stdout/stderr reread and hashes verified
  summary: Historical runner failed before retrieval with PermissionError reading
    pyvenv.cfg. No current invocation or success claimed; fresh official source catalogue
    and inspected primary/authority evidence supply bounded fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/original-checks.json
  locator: Four actual original native validate/render results and historical-source
    input hashes
  summary: All four original pairs validate and render exactly; historical input counts14/17/16/17
    match source commits. All four current targets are unchanged from originals; no
    stale target in this slice.
  accessed_at: '2026-11-03T14:53:14.339529Z'
  support: supports
  snapshot_sha256: ef5edfd6921a41502400a08778198f2e1d9239d3798e23042a0f254e3cde4a87
- evidence_id: plaque-native-golgi_cisterna-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes.
    Mechanical coverage is empty-inventory scope; narrative pathway assertions require
    independent scientific assessment.'
  accessed_at: '2026-11-03T14:51:21.280249Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-golgi_cisterna-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component\
    \ protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory\
    \ scope; narrative pathway assertions require independent scientific assessment."
  accessed_at: '2026-11-03T14:51:21.691119Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-golgi_cisterna_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes.
    Mechanical coverage is empty-inventory scope; narrative pathway assertions require
    independent scientific assessment.'
  accessed_at: '2026-11-03T14:51:22.095956Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-golgi_cisterna_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_cisterna_membrane.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component\
    \ protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory\
    \ scope; narrative pathway assertions require independent scientific assessment."
  accessed_at: '2026-11-03T14:51:22.525081Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-golgi_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_lumen.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes.
    Mechanical coverage is empty-inventory scope; narrative pathway assertions require
    independent scientific assessment.'
  accessed_at: '2026-11-03T14:51:22.963054Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-golgi_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_lumen.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component\
    \ protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory\
    \ scope; narrative pathway assertions require independent scientific assessment."
  accessed_at: '2026-11-03T14:51:23.415024Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-golgi_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes.
    Mechanical coverage is empty-inventory scope; narrative pathway assertions require
    independent scientific assessment.'
  accessed_at: '2026-11-03T14:51:23.874871Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-golgi_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_membrane.yaml
    --causal-graphs
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
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
    \  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component\
    \ protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory\
    \ scope; narrative pathway assertions require independent scientific assessment."
  accessed_at: '2026-11-03T14:51:24.336929Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current skill/profile/config/shared contract and scientific checklist;
    CURATION identity, narrow evidence, family-or-class and molecular grounding rules
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named proteins and pathways trigger source-adapter applicability, even
    without transcriptomics assertions. Evidence is claim-specific; current review
    does not rewrite original history.
  support: context_only
- evidence_id: micro-component-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, ComponentTypeEnum, CausalNode and
    essentiality; CURATION108-110 family-or-class and UniProt skill Step2 generic-class
    guidance
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Generic protein classes are permitted by native guidance; PROTEIN_COMPLEX
    denotes a named subcomplex with its own identity. ProteinExample identity is not
    membership proof. CausalNode explicitly allows protein complexes as GENE_OR_PROTEIN,
    so no graph-node-type defect is inferred from complex typing.
  support: context_only
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Complete graph skill and add-cell-structure evidence/graph contract; NONMECHANISTIC
    scope
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Identity, topology, experimental context and narrow edge-level evidence
    must agree; no complete assembly mechanism or necessary individual composition
    inferred from marker localization.
  support: context_only
- evidence_id: micro-record-golgi_apparatus
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_apparatus.yaml
  locator: 'Entire maintained target: all fields, current component types/examples,
    graph nodes/edges, discussions, history and evidence notes'
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: e3df76cd9d71ba04df9e5349475bd4191c31f93156acd422ef6b0223b88facca
  summary: Current bytes independently read; stale old input substantively reassessed
    after SNARE cohort retyping.
  support: supports
- evidence_id: micro-prior-golgi_apparatus
  kind: prior_review
  reference: reviews/structured/20261022T015625Z-golgi-apparatus-audit/review.yaml
  locator: Original assessments/findings/actions, source scopes, checks, limitations;
    paired Markdown verified with native renderer
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: cb166fb37e26b8d9adf35fa778621d967b784d539ec33132af70c72a2b27629c
  summary: Original verdict needs_curation; 1 original finding(s). Expression-only
    applicability exclusion exists and requires correction. Historical scientific
    checks/accesses remain historical.
  support: context_only
- evidence_id: micro-native-golgi_apparatus-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --verify; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T14:51:18.780806Z'
  snapshot_sha256: 967b992cec19e77f20e2be0ab3ea25562bb23a1e77c495c48c0f64719da22c5d
  summary: Exit0 at source head. Six reviewed S288C examples OCH1/MNN1/KRE2 and SED5/TLG2/SEC22;
    two COVERED nodes. The check verifies declared identities and coverage, not that
    all examples form one physical complex or directly determine maturation.
  support: supports
- evidence_id: micro-native-golgi_apparatus-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_apparatus.yaml
    --causal-graphs; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_apparatus-uniprot-causal.log
    SHA256 c43cea8c606cb2810b4f9b7c7a5c88f1dfd70ae0fb115897019bc9f86a673fad
  accessed_at: '2026-11-03T14:51:19.189231Z'
  snapshot_sha256: 5a74ac8b4f49a504d5d567e22a00f843aefeab55c1f9f00ec1489d3e5e49f0ef
  summary: Exit0 at source head. Six reviewed S288C examples OCH1/MNN1/KRE2 and SED5/TLG2/SEC22;
    two COVERED nodes. The check verifies declared identities and coverage, not that
    all examples form one physical complex or directly determine maturation.
  support: supports
- evidence_id: micro-record-golgi_associated_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
  locator: 'Entire maintained target: all fields, current component types/examples,
    graph nodes/edges, discussions, history and evidence notes'
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: 71af7287ce915ee5a16cef9a81c36b2c46e1b0cb7622a3f5c445fe308bbd81ba
  summary: Current bytes independently read; target equals original frozen input.
  support: supports
- evidence_id: micro-prior-golgi_associated_vesicle
  kind: prior_review
  reference: reviews/structured/20261022T015627Z-golgi-associated-vesicle-audit/review.yaml
  locator: Original assessments/findings/actions, source scopes, checks, limitations;
    paired Markdown verified with native renderer
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: 33f0b26a7e2e46f7ceb29252cffc584836231b7847812af9c8db112538aa81da
  summary: Original verdict needs_curation; 1 original finding(s). Expression-only
    applicability exclusion exists and requires correction. Historical scientific
    checks/accesses remain historical.
  support: context_only
- evidence_id: micro-native-golgi_associated_vesicle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    --verify; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T14:51:19.599114Z'
  snapshot_sha256: af7ce642ccc300b52c4273e99a9137105dc8c5c51ba955ae96c1bf89036c6f2b
  summary: Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN
    nodes; generic verify-success text is an empty protein inventory, not a composition/localization
    experiment.
  support: supports
- evidence_id: micro-native-golgi_associated_vesicle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    --causal-graphs; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T14:51:20.013958Z'
  snapshot_sha256: 11e1582dd5b4fed573cb64afc7981ede3cce82e02f93ede8f187119c07eb932c
  summary: Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN
    nodes; generic verify-success text is an empty protein inventory, not a composition/localization
    experiment.
  support: supports
- evidence_id: micro-record-golgi_associated_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
  locator: 'Entire maintained target: all fields, current component types/examples,
    graph nodes/edges, discussions, history and evidence notes'
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: 6467fb8e64210d44c66f32b8c6f654c6bdada08ecd35edc36f074667d4ce4413
  summary: Current bytes independently read; target equals original frozen input.
  support: supports
- evidence_id: micro-prior-golgi_associated_vesicle_membrane
  kind: prior_review
  reference: reviews/structured/20261022T015629Z-golgi-associated-vesicle-membrane-audit/review.yaml
  locator: Original assessments/findings/actions, source scopes, checks, limitations;
    paired Markdown verified with native renderer
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: dd9c7ba2848fed56c12bbb5c85532edf92fa1710542bb8d5c6d7f2905a754f02
  summary: Original verdict pass_with_limitations; 0 original finding(s). Expression-only
    applicability exclusion exists and requires correction. Historical scientific
    checks/accesses remain historical.
  support: context_only
- evidence_id: micro-native-golgi_associated_vesicle_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    --verify; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T14:51:20.432516Z'
  snapshot_sha256: 2d93b0542c4a48cf22fbdab167243f1e20c09e2f15e146e3421709e318f27bac
  summary: Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN
    nodes; generic verify-success text is an empty protein inventory, not a composition/localization
    experiment.
  support: supports
- evidence_id: micro-native-golgi_associated_vesicle_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/golgi_associated_vesicle_membrane.yaml
    --causal-graphs; entire stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/golgi_associated_vesicle_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T14:51:20.863915Z'
  snapshot_sha256: e2aa4f0a655e205981ec771f12e7b0fdede040a50b873ed54727f932945ba319
  summary: Exit0 at source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN
    nodes; generic verify-success text is an empty protein inventory, not a composition/localization
    experiment.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-microtubule/original-validation-receipt.json
  locator: Three native validate and three render --content runs; exact original Markdown
    equality; original git-show input hashes
  accessed_at: '2026-11-03T14:55:04.426432Z'
  snapshot_sha256: fc2d25978df51a90c6f671790a2aa273a58c29b07ace36467b2c1d2af5720c61
  summary: All three original pairs validate and render byte-identically. Historical
    frozen target hashes verified; only apparatus differs from old input.
  support: supports
- evidence_id: micro-stale-delta
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-microtubule/golgi-apparatus-stale.diff
  locator: Entire original frozen revision to current-source diff
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: 12d194ad4613040bbb31224c2875dab6bd90da582a839373c8ac308703e3e25e
  summary: Only October30 history and PROTEIN to PROTEIN_COMPLEX change for the SED5/TLG2/SEC22
    cohort. No narrowing of cohort label, notes, examples or edge evidence accompanied
    the change. Historical issue2462 mention is context, not an endorsement or whole-issue
    disposition.
  support: context_only
- evidence_id: micro-historical-2462
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2462
  locator: Root-retained issue packet /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/historical-issue-2462.json;
    complete body/comments/state read, only historical context
  accessed_at: '2026-11-03T14:59:38.890495Z'
  snapshot_sha256: abe5bab7f2b60e9179facfec2f469e19784b43d024dccd303e2fa5298b220ed4
  summary: Grouped issue2462 prescribed a Golgi SED5/TLG2/SEC22 type change among11
    records and reports prior remediation. This is not independent molecular membership
    evidence; no exact category predecessor is reassessed or terminally disposed,
    and the new current-record finding does not reopen the grouped issue.
  support: context_only
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005794,GO:0043231,GO:0012505,GO:0000139,GO:0031985,GO:0005798,GO:0030660,GO:0031410,GO:0030659,GO:0030663,GO:0012510,GO:0030137,GO:0030126,GO:0035964,GO:0006890
  locator: All15 exact active terms; complete names/definitions/synonyms/typed child
    relations
  accessed_at: '2026-11-03T14:52:01.772537Z'
  snapshot_sha256: c933d831774ac7bd945e46f8e6f181ba9af6330303bb1b85c12f186455cbf77e
  summary: Exact apparatus5794, vesicle5798 and membrane30660 identities agree. Apparatus
    is direct is_a43231 and part_of12505; membrane139 is part_of apparatus. Vesicle
    is direct is_a31410; membrane30660 part_of5798, with direct COPI30663 and TGN12510
    is_a children. COPI30137 is child of5798; coat30126 is distinct from membrane.
    Budding35964 is Golgi-membrane evagination;6890 is directed retrograde transport.
    Cisterna31985 definition supports a Golgi compartment without claiming a direct
    ontology part_of edge not returned.
  support: supports
- evidence_id: micro-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete exact ENA taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T14:52:01.772839Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: Taxon4932 is Saccharomyces cerevisiae at species rank. Canonical species
    occurrence is qualitative; reference-strain protein identity does not rename experimental
    strains.
  support: supports
- evidence_id: micro-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete exact ENA taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T14:52:01.772927Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: Taxon559292 is Saccharomyces cerevisiae S288C at strain rank. Canonical
    species occurrence is qualitative; reference-strain protein identity does not
    rename experimental strains.
  support: supports
- evidence_id: micro-protein-P31755
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31755.json
  locator: Exact native accession/name/status/gene/organism and complete relevant
    comments with ECO/PMID attribution
  accessed_at: '2026-11-03T14:52:01.772980Z'
  snapshot_sha256: d9e08176a5ae755fb9f2e831db8e914751b10ccd12df96c404604bcbbc0c1666
  summary: P31755 is reviewed, primary gene OCH1, tax559292; exact recommended protein
    name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments
    inspected. ER-membrane ECO0000269 cites14676282/1628616; Golgi-membrane ECO0000269
    includes15229219, matching target provenance. Recycling context preserved.
  support: supports
- evidence_id: micro-query-OCH1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AOCH1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete response with primary/synonym tokens, total-results1 and no next-page
    Link
  accessed_at: '2026-11-03T14:52:01.773025Z'
  snapshot_sha256: 5c298b13b6c9d94db63caba59445b1eaaef38067995a0185d904ec30231ac69e
  summary: Exactly P31755 returned and actual primary gene OCH1 agrees. Bounded current
    uniqueness wording is supported.
  support: supports
  search_scope: UniProtKB native search 2026-11-03T14:52:01.773025Z; literal query
    '(gene_exact:OCH1) AND (organism_id:559292) AND (reviewed:true)'; format=json,size100;
    complete one result, X-Total-Results1, no Link pagination. This is exact reviewed
    S288C identity scope, not pan-taxon membership or experimental necessity.
- evidence_id: micro-protein-P39106
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39106.json
  locator: Exact native accession/name/status/gene/organism and complete relevant
    comments with ECO/PMID attribution
  accessed_at: '2026-11-03T14:52:01.773064Z'
  snapshot_sha256: 06df97f0147ff075bde02c34aa2a1f4ea35267ef88dc3c5b40fa7b885a692157
  summary: P39106 is reviewed, primary gene MNN1, tax559292; exact recommended protein
    name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments
    inspected. Golgi membrane annotation is ECO0000305; terminal mannosylation is
    native function, not fresh microscopy.
  support: supports
- evidence_id: micro-query-MNN1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMNN1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete response with primary/synonym tokens, total-results1 and no next-page
    Link
  accessed_at: '2026-11-03T14:52:02.372835Z'
  snapshot_sha256: 5c0845db2c21c7f6eb20c6c0414a9b3541d56b12a058bd870e9b8f9019001938
  summary: Exactly P39106 returned and actual primary gene MNN1 agrees. Bounded current
    uniqueness wording is supported.
  support: supports
  search_scope: UniProtKB native search 2026-11-03T14:52:02.372835Z; literal query
    '(gene_exact:MNN1) AND (organism_id:559292) AND (reviewed:true)'; format=json,size100;
    complete one result, X-Total-Results1, no Link pagination. This is exact reviewed
    S288C identity scope, not pan-taxon membership or experimental necessity.
- evidence_id: micro-protein-P27809
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27809.json
  locator: Exact native accession/name/status/gene/organism and complete relevant
    comments with ECO/PMID attribution
  accessed_at: '2026-11-03T14:52:02.372944Z'
  snapshot_sha256: d9937a8a2c1e27de6fdfa747c81fd72399fd0d750110e39cd65fc3c8e2d6ae4c
  summary: P27809 is reviewed, primary gene KRE2, tax559292; exact recommended protein
    name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments
    inspected. KRE2/MNT1 native Golgi localization and glycosyltransferase15 context
    do not establish universal organelle necessity.
  support: supports
- evidence_id: micro-query-KRE2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AKRE2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete response with primary/synonym tokens, total-results1 and no next-page
    Link
  accessed_at: '2026-11-03T14:52:02.414302Z'
  snapshot_sha256: cca74c6799561ef94fb7fa6734b44830e22fc10edcee3b241c4d7a8655ffc5cd
  summary: Exactly P27809 returned and actual primary gene KRE2 agrees. Bounded current
    uniqueness wording is supported.
  support: supports
  search_scope: UniProtKB native search 2026-11-03T14:52:02.414302Z; literal query
    '(gene_exact:KRE2) AND (organism_id:559292) AND (reviewed:true)'; format=json,size100;
    complete one result, X-Total-Results1, no Link pagination. This is exact reviewed
    S288C identity scope, not pan-taxon membership or experimental necessity.
- evidence_id: micro-protein-Q01590
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01590.json
  locator: Exact native accession/name/status/gene/organism and complete relevant
    comments with ECO/PMID attribution
  accessed_at: '2026-11-03T14:52:02.552483Z'
  snapshot_sha256: 586b494279d831cbe36781c791833fd8b3f93022d69dc6872ed00753a71f4843
  summary: Q01590 is reviewed, primary gene SED5, tax559292; exact recommended protein
    name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments
    inspected. Sed5 t-SNARE supports ER-Golgi transport; interaction and localization
    annotations do not define the full broad cohort as one assembly.
  support: supports
- evidence_id: micro-query-SED5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASED5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete response with primary/synonym tokens, total-results1 and no next-page
    Link
  accessed_at: '2026-11-03T14:52:02.745111Z'
  snapshot_sha256: c501ae657b04d3b2311646ce8008d132de39cf5aa217c9c93c95ec878669ef78
  summary: Exactly Q01590 returned and actual primary gene SED5 agrees. Bounded current
    uniqueness wording is supported.
  support: supports
  search_scope: UniProtKB native search 2026-11-03T14:52:02.745111Z; literal query
    '(gene_exact:SED5) AND (organism_id:559292) AND (reviewed:true)'; format=json,size100;
    complete one result, X-Total-Results1, no Link pagination. This is exact reviewed
    S288C identity scope, not pan-taxon membership or experimental necessity.
- evidence_id: micro-protein-Q08144
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08144.json
  locator: Exact native accession/name/status/gene/organism and complete relevant
    comments with ECO/PMID attribution
  accessed_at: '2026-11-03T14:52:03.385619Z'
  snapshot_sha256: 001ba611c8d23e65cf9d6665abaf092e799b3dedc8141843990f8a60a442499c
  summary: Q08144 is reviewed, primary gene TLG2, tax559292; exact recommended protein
    name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments
    inspected. Tlg2 functions in endosome-to-late-Golgi/endocytic traffic, with trans-Golgi/endosome
    membrane locations and Vps45 interaction.
  support: supports
- evidence_id: micro-query-TLG2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATLG2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete response with primary/synonym tokens, total-results1 and no next-page
    Link
  accessed_at: '2026-11-03T14:52:04.174657Z'
  snapshot_sha256: 804ee1ab086ef0138ad3a6c861b568dfd39f0653348d51ecd05593ad222fdc50
  summary: Exactly Q08144 returned and actual primary gene TLG2 agrees. Bounded current
    uniqueness wording is supported.
  support: supports
  search_scope: UniProtKB native search 2026-11-03T14:52:04.174657Z; literal query
    '(gene_exact:TLG2) AND (organism_id:559292) AND (reviewed:true)'; format=json,size100;
    complete one result, X-Total-Results1, no Link pagination. This is exact reviewed
    S288C identity scope, not pan-taxon membership or experimental necessity.
- evidence_id: micro-protein-P22214
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22214.json
  locator: Exact native accession/name/status/gene/organism and complete relevant
    comments with ECO/PMID attribution
  accessed_at: '2026-11-03T14:52:04.350434Z'
  snapshot_sha256: 259b6c9a371007a3b8942f52581ace55de61b0a721bc20799833d764de1d0c10
  summary: P22214 is reviewed, primary gene SEC22, tax559292; exact recommended protein
    name matches. Complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments
    inspected. SUBUNIT explicitly names distinct Sed5/Bos1/Bet1/Sec22 and Ufe1/Use1/Sec20/Sec22
    complexes. SEC22 is nonessential for cell viability in native function context,
    not established essential for Golgi formation.
  support: supports
- evidence_id: micro-query-SEC22
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC22%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete response with primary/synonym tokens, total-results1 and no next-page
    Link
  accessed_at: '2026-11-03T14:52:05.303401Z'
  snapshot_sha256: 2f02196a0b43a4c1d97d3618433076a62c67a6538708bd3330f9ca0f186986a2
  summary: Exactly P22214 returned and actual primary gene SEC22 agrees. Bounded current
    uniqueness wording is supported.
  support: supports
  search_scope: UniProtKB native search 2026-11-03T14:52:05.303401Z; literal query
    '(gene_exact:SEC22) AND (organism_id:559292) AND (reviewed:true)'; format=json,size100;
    complete one result, X-Total-Results1, no Link pagination. This is exact reviewed
    S288C identity scope, not pan-taxon membership or experimental necessity.
- evidence_id: micro-papanikou2014-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.ceb.2014.04.010%22&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:05.699999Z'
  snapshot_sha256: ba7187953d6c506e4b90affacffe43518ec9a494b86895f5362e014bfc5212c9
  summary: PMID24840895 DOI10.1016/j.ceb.2014.04.010 Golgi compartmentation and identity.
    Secondary review proposes a three-stage model; not a primary experiment. Its author-manuscript
    BioC header year is not substituted for the exact MED2014 citation.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:05.699999Z; literal query
    'DOI:"10.1016/j.ceb.2014.04.010"'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-letourneur1994-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8001155+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:06.373621Z'
  snapshot_sha256: 384eefb7e07293956272cd85db7c93da276ef14cd34f62fbc4206f7b52870e6f
  summary: PMID8001155 DOI10.1016/0092-8674(94)90011-6 Coatomer is essential for retrieval
    of dilysine-tagged proteins to the endoplasmic reticulum. Complete primary abstract
    describes dilysine-tagged Ste2 retrieval in yeast, selective coatomer-mutant defects
    and RET1 complementation; supports scoped COPI retrieval, not universal generic-vesicle
    coat or direct budding movie.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:06.373621Z; literal query
    'EXT_ID:8001155 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-waters1991-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2F349248a0%22&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:06.550086Z'
  snapshot_sha256: ac32800adf1e8ed6055077c11015ccadde8032d32a8e9f4ab146e4543d498b2a
  summary: 'PMID1898986 DOI10.1038/349248a0 ''Coatomer'': a cytosolic protein complex
    containing subunits of non-clathrin-coated Golgi transport vesicles. Complete
    primary abstract reports purified cytosolic coatomer sharing Golgi-coated-vesicle
    subunits; no generic-vesicle molecular census or yeast-specific experiment inferred.'
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:06.550086Z; literal query
    'DOI:"10.1038/349248a0"'; formatjson/resultTypecore/pageSize100; hitCount1, one
    MED record fully inspected. Exact-source lookup, not exhaustive literature absence.
- evidence_id: micro-karhinen2004-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14676282+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:06.787447Z'
  snapshot_sha256: ab27b6bc6f68390d213778b5ee06172d1243ce0f00920ab4e3b4307fe0858ed8
  summary: PMID14676282 DOI10.1242/jcs.00858 Activity of recycling Golgi mannosyltransferases
    in the yeast endoplasmic reticulum. Complete primary abstract supports Och1 ER
    accumulation/activity when COPII export is blocked, plus recycling; conditional
    ER localization does not negate Golgi residence.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:06.787447Z; literal query
    'EXT_ID:14676282 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-nakayama1992-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A1628616+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:07.009742Z'
  snapshot_sha256: 4e20cd0333e06cd145a7d57aafdba2f6dd777476767dd396d480d44db835f02c
  summary: 'PMID1628616 DOI10.1002/j.1460-2075.1992.tb05316.x OCH1 encodes a novel
    membrane bound mannosyltransferase: outer chain elongation of asparagine-linked
    oligosaccharides. Complete primary abstract supports OCH1 cloning, typeII membrane
    topology and outer-chain mannosyltransferase function; no fresh body/pixel read.'
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:07.009742Z; literal query
    'EXT_ID:1628616 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-bruinsma2004-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15229219+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:07.236955Z'
  snapshot_sha256: b3a2ff387185dc82b96fc586bf7500524e9f7a9b9eaa33a961635ebed67f7dc9
  summary: PMID15229219 DOI10.1074/jbc.m405500200 Retrograde transport of the mannosyltransferase
    Och1p to the early Golgi requires a component of the COG transport complex. Complete
    primary abstract distinguishes Och1/Mnn1 mislocalization in cog3-202, Sed5/Sft1
    retrograde-vesicle context and intra-Golgi cycling from vacuolar degradation routes.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:07.236955Z; literal query
    'EXT_ID:15229219 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-pmid11001058
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11001058+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:30.781322Z'
  snapshot_sha256: 4815da01157bf1c260643a4cae22f35d5882643f284504587a3c4ba9743e005b
  summary: PMID11001058 DOI10.1038/35025076 Topological restriction of SNARE-dependent
    membrane fusion. Parlati2000 complete primary abstract explicitly reconstitutes
    Sed5/Bos1/Sec22 on one bilayer and Bet1 on the other; eight nonredundant permutations
    tested. This is a defined ER-Golgi fusion assembly, not the SED5/TLG2/SEC22 cohort.
    No full body or pixels read.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:30.781322Z; literal query
    'EXT_ID:11001058 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-pmid9930650
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9930650+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:30.781374Z'
  snapshot_sha256: ed0e0442de414d999ba86b4f0acd11fd86c52ebd5970aa1657945338b57b6f09
  summary: PMID9930650 DOI10.1016/s0171-9335(98)80084-8 The Sec1p homologue Vps45p
    binds to the syntaxin Tlg2p. Nichols1998 complete primary abstract reports Tlg2
    as principal Vps45 binding site and a Tlg1/Tlg2/Vps45 triple association, with
    late-Golgi/endosomal scope. It does not state that Tlg2 belongs to the Sed5/Bos1/Bet1/Sec22
    complex.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:30.781374Z; literal query
    'EXT_ID:9930650 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-pmid9755865
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9755865+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:30.781431Z'
  snapshot_sha256: 46448f250e911cdb9d1785f59304bf71a4e5785278dd4b6480a581354d3fd589
  summary: PMID9755865 DOI10.1016/s0014-5793(98)01044-8 Gos1p, a Saccharomyces cerevisiae
    SNARE protein involved in Golgi transport. McNew1998 complete primary abstract
    describes direct Sed5/Gos1 binding and viable gos1 deletion with modest transport
    defects. This is another bounded SNARE context, not an exhaustive no-interaction
    theorem.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:30.781431Z; literal query
    'EXT_ID:9755865 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-pmid12941276
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12941276+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact one MED bibliographic record and complete abstract; bodies separately
    scoped
  accessed_at: '2026-11-03T14:52:30.833842Z'
  snapshot_sha256: 269d94df0e37e77c21fa9e78f7f334be3a3a96eeae9e4537ec467dc03e87e5be
  summary: PMID12941276 DOI10.1016/s0092-8674(03)00608-1 SNARE selectivity of the
    COPII coat. Mossessova2003 complete primary abstract distinguishes three COPII
    binding sites for Bet1/Sed5/Sec22 and favors the Sed5/Bos1/Sec22 t-SNARE assembly.
    No exact current cohort identity or universal fusion mechanism is inferred.
  support: context_only
  search_scope: Europe PMC native search 2026-11-03T14:52:30.833842Z; literal query
    'EXT_ID:12941276 AND SRC:MED'; formatjson/resultTypecore/pageSize100; hitCount1,
    one MED record fully inspected. Exact-source lookup, not exhaustive literature
    absence.
- evidence_id: micro-papanikou2014-bioc
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4130901/unicode
  locator: Genuine NCBI BioC author-manuscript full text; all main paragraphs/passages2-33
    and embedded captions150-151, front/abstract0-1; no figure pixels/underlying datasets
  accessed_at: '2026-11-03T14:53:39.832781Z'
  snapshot_sha256: 04d40aa66c031e3e077c046fb1d37a3b76261833220d40ccdef4165c7db3ca94
  summary: Complete main review supports glycan-processing cohorts, membrane traffic
    and Rab/Arf coordination while retaining unresolved COPI directionality and cargo
    questions. It does not attribute SNARE pairing/cycling or the SED5/TLG2/SEC22
    set. Secondary model/synthesis remains context, not primary experimental proof.
  support: context_only
- evidence_id: micro-snare-attribution-search
  kind: search
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4130901/unicode
  locator: Complete already-read main text BioC passages2-33 plus both captions150-151;
    excludes bibliography-only references
  accessed_at: '2026-11-03T14:53:39.832781Z'
  snapshot_sha256: 04d40aa66c031e3e077c046fb1d37a3b76261833220d40ccdef4165c7db3ca94
  summary: Case-insensitive SNARE,SED5,TLG2,SEC22 counts are each0 in the bounded
    full main text/captions. Manual contextual reading also finds no pairing/cycling
    claim. This supports only source-placement F1, not biological absence.
  support: context_only
  search_scope: On 2026-11-03T14:59:38.890495Z searched complete retained NCBI BioC
    main passages2-33 and captions150-151 for literal SNARE,SED5,TLG2,SEC22, alongside
    full contextual reading; all four zero. Input retrieved 2026-11-03T14:53:39.832781Z.
    Search bound is this article/version only; no internet-wide absence inference.
- evidence_id: micro-access-papanikou2014-body
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4130901/
  locator: Actual attempted route response only
  accessed_at: '2026-11-03T14:52:30.780848Z'
  snapshot_sha256: 2c1ac5331b19311d0b47de953cb2388d4a4a92e5481a35e314aa2de649346fb2
  summary: 'HTTP200: recaptcha challenge, not body; genuine BioC route separately
    read.'
  support: context_only
- evidence_id: micro-access-papanikou2014-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4130901/
  locator: Actual attempted route response only
  accessed_at: '2026-11-03T14:53:02.142423Z'
  snapshot_sha256: 4bb2c6c9e95466791a589297f1cfde834751bf958e3399402ed8d616ea562f26
  summary: 'HTTP200: recaptcha challenge, not body; genuine BioC route separately
    read.'
  support: context_only
- evidence_id: micro-access-papanikou2014-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4130901/fullTextXML
  locator: Actual attempted route response only
  accessed_at: '2026-11-03T14:52:30.781125Z'
  snapshot_sha256: 2e773e8f55c325c19686b2b640285a58c9f2336e87bbd70db3af7f68b05e79fa
  summary: 'HTTP500: server/access response, not scientific full text.'
  support: context_only
- evidence_id: micro-access-letourneur1994-access
  kind: authority
  reference: https://www.cell.com/cell/fulltext/0092-8674(94)90011-6
  locator: Actual attempted route response only
  accessed_at: '2026-11-03T14:52:30.781237Z'
  snapshot_sha256: efd254c956beeead2f0e73b870d2e2fe5ac09a5b9fbdf473e0308ce1a6a38a73
  summary: 'HTTP403: server/access response, not scientific full text.'
  support: context_only
- evidence_id: micro-losev2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized-Nature-2006.pdf
  locator: Complete genuine PDF mainpp1002-1005/Methods/embeddedFig1-4captions; no
    figure pixels/movies/supplements; independently read shared fresh snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/losev2006-pdf.source
  accessed_at: '2026-11-03T14:52:02.143799Z'
  snapshot_sha256: 9cd6a98c307575ce19f0b88a5943b10dc7732d655c2b75a9d34228a4fbbc188f
  summary: Primary yeast23C4D imaging of Sec7/Vrg4 and additional markers supports
    transient early-to-late cisternal identity; pulse-chase kinetics are consistent
    with maturation. Only unambiguously resolved cisternae quantified. Direct cargo
    tracking and exact recycling pathway remain unresolved.
  support: supports
- evidence_id: micro-matsuura2006-pdf
  kind: primary_source
  reference: https://biophys.w3.kanazawa-u.ac.jp/References/Cell/Golgi-maturation-visualized(2)-Nature-2006.pdf
  locator: Complete genuine PDF mainpp1007-1009 plus Methods continuation1010 and
    Fig1-4captions; no pixels/movies/supplements; independently read shared fresh
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/matsuura2006-pdf.source
  accessed_at: '2026-11-03T14:52:02.743056Z'
  snapshot_sha256: e0e393bc775432869db495e2a836df223a0be5128ab04aae51a9d31bbf323583
  summary: Primary functional Rer1/Gos1 and Sed5/Sec7 fusions change resident marker
    distribution in yeast. ret1-1 slows but does not abolish transitions at37C; physical
    membrane transfer and cargo retention remain unresolved.
  support: supports
- evidence_id: micro-serafini1991-quoted
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/0092-8674%2891%2990176-y%22&pageSize=25
  locator: Complete exact MED bibliography and primary abstract only; independently
    read shared fresh snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-plaque/serafini1991-quoted.source
  accessed_at: '2026-11-03T14:52:21.515779Z'
  snapshot_sha256: dea8968c03304cd9777691eda5c7ba9969cbd3d2e353a2a5c9ac6ff2ac69538f
  summary: PMID1680566 DOI10.1016/0092-8674(91)90176-y identifies Serafini1991. Abstract
    reports ARF enrichment on Golgi-derived COP-coated vesicles, removal with uncoating
    and GTP-dependent membrane binding. Hypothesized GTP-hydrolysis regulation is
    not promoted to direct universal budding/yeast evidence.
  support: supports
- evidence_id: micro-datasets
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official /api/datasets response, all20 organism rows/28 organism-dataset
    pairs; IDs,names,descriptions and lists
  accessed_at: '2026-11-03T14:52:07.372713Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Saccharomyces/cerevisiae/S288C matching organism or dataset in current
    bounded catalogue. All three actual pathway-bearing targets require this assessment;
    no unmatched bacterial proxy or downstream matched-gene/module query applies.
  support: context_only
  search_scope: Official iModulonDB /api/datasets retrieved 2026-11-03T14:52:07.372713Z;
    no server filter or page parameter. Entire20 rows/28 pairs inspected with case-insensitive
    Saccharomyces,cerevisiae,S288C,4932,559292 checks. No matched dataset; no biological
    absence or exhaustive transcriptomics claim.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual00:49Z historical datasets invocation; exit1 PermissionError pyvenv.cfg;
    no fresh execution
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical adapter runner unavailable; fresh official catalogue supplies
    present fallback applicability. Not counted as a newly executed successful adapter
    command.
  support: context_only
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record assertions, structured sources and severity rubric
  summary: Positive molecular/pathway assertions require a real applicability assessment;
    absence of expression claims alone is not an exemption. Keep source scope, uncertainty
    and original finding identity; record curation is separate.
  accessed_at: '2026-11-03T15:00:59.984309Z'
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
  accessed_at: '2026-11-03T15:00:59.984309Z'
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
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph nodes, component correspondence, source scope and necessity
  summary: Descriptive boundary graphs can remain NONMECHANISTIC; source-specific
    localization, molecular identity and organelle-formation necessity must not be
    conflated.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Step2 generic classes and native coverage report
  summary: Generic class components are explicitly recognized. A zero-example inventory
    or NO_GENE_SYMBOLS node is a stated coverage limit, not proof that the protein
    class does not exist or that its members form one stable complex.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-record-glyoxysome
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysome.yaml
  locator: Complete current record at f23e1970804e4f93de15a4ae275af84d48e6ce14
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, taxonomic
    and canonical scopes, all components and functions, all evidence/graph edges,
    discussions and history. No images, physical-property measurements, associated
    traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4
- evidence_id: septin-original-glyoxysome
  kind: prior_review
  reference: reviews/structured/20261022T015623Z-glyoxysome-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; source hashes/checks/assessments/findings/actions
  summary: Original bytes and historical source observations are preserved. Current
    target is byte-unchanged. Original finding identities are retained; the new hydrogenosome
    attribution finding has no invented predecessor.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: d8001c6c4dae6eb0a72cb217399091bd4f5e908e9b2d90a6d989f49067e3be87
- evidence_id: septin-original-validation-glyoxysome
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/original-checks.json
  locator: Original native validate/render and git-show historical target SHA
  summary: Both native commands exit zero; rendered Markdown is byte-identical and
    the original frozen hash matches its historical revision.
  accessed_at: '2026-11-03T14:54:28.063705Z'
  support: supports
  snapshot_sha256: 67e12ae441e841ca5bdf38fd617d6792a91a4f7a8ed8c0587ced878dba582a3d
- evidence_id: septin-native-glyoxysome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-verify-receipt.json
  locator: Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-verify.log
  summary: Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs
    and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier
    inventory, not all narrative pathway claims.
  accessed_at: '2026-11-03T14:51:17.120917Z'
  support: supports
  snapshot_sha256: 1b2ef21a8814d1f93f80b6198d4622837dfed9b1700134f442ab2edc23ccf55a
- evidence_id: septin-native-glyoxysome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-causal-receipt.json
  locator: Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/glyoxysome-uniprot-causal.log
  summary: Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs
    and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier
    inventory, not all narrative pathway claims.
  accessed_at: '2026-11-03T14:51:17.522370Z'
  support: supports
  snapshot_sha256: 0c63df1a41f0cbbedbb57ec71213bbf204d1e8d4ff2779ba2a98ee05c118b2ac
- evidence_id: septin-record-hydrogenosomal_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  locator: Complete current record at f23e1970804e4f93de15a4ae275af84d48e6ce14
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, taxonomic
    and canonical scopes, all components and functions, all evidence/graph edges,
    discussions and history. No images, physical-property measurements, associated
    traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56
- evidence_id: septin-original-hydrogenosomal_membrane
  kind: prior_review
  reference: reviews/structured/20261022T015639Z-hydrogenosomal-membrane-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; source hashes/checks/assessments/findings/actions
  summary: Original bytes and historical source observations are preserved. Current
    target is byte-unchanged. Original finding identities are retained; the new hydrogenosome
    attribution finding has no invented predecessor.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: d85c84493415c834ae784d33ec2e6906566d942c4880d08fd1f1e6b20df06acf
- evidence_id: septin-original-validation-hydrogenosomal_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/original-checks.json
  locator: Original native validate/render and git-show historical target SHA
  summary: Both native commands exit zero; rendered Markdown is byte-identical and
    the original frozen hash matches its historical revision.
  accessed_at: '2026-11-03T14:54:29.307202Z'
  support: supports
  snapshot_sha256: 67e12ae441e841ca5bdf38fd617d6792a91a4f7a8ed8c0587ced878dba582a3d
- evidence_id: septin-native-hydrogenosomal_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-verify-receipt.json
  locator: Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-verify.log
  summary: Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs
    and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier
    inventory, not all narrative pathway claims.
  accessed_at: '2026-11-03T14:51:24.806692Z'
  support: supports
  snapshot_sha256: b5bcd3fc099b9e35d7b916b0fabaaf9531aa9c9d2c5aca8ca3799e8bcc1e3447
- evidence_id: septin-native-hydrogenosomal_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-causal-receipt.json
  locator: Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosomal_membrane-uniprot-causal.log
  summary: Exit zero. Zero protein examples, zero represented UniProtKB graph xrefs
    and zero GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier
    inventory, not all narrative pathway claims.
  accessed_at: '2026-11-03T14:51:25.253820Z'
  support: supports
  snapshot_sha256: f855e3e95151e2b8d3a537da40660f9b321fc9e403ee73f12f088279231f3448
- evidence_id: septin-record-hydrogenosome
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosome.yaml
  locator: Complete current record at f23e1970804e4f93de15a4ae275af84d48e6ce14
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, taxonomic
    and canonical scopes, all components and functions, all evidence/graph edges,
    discussions and history. No images, physical-property measurements, associated
    traits or verbatim snippets are declared.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 6d295ad6b0bb5066ddec461e6c2ffa142de9d8590d705eff6a3648bc6c01e77a
- evidence_id: septin-original-hydrogenosome
  kind: prior_review
  reference: reviews/structured/20261022T015641Z-hydrogenosome-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; source hashes/checks/assessments/findings/actions
  summary: Original bytes and historical source observations are preserved. Current
    target is stale and substantively refreshed. Original finding identities are retained;
    the new hydrogenosome attribution finding has no invented predecessor.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 4c3ed7f07ba46d5c587c8697067749c64005bd04d54b2306fbfea35ef8c9df17
- evidence_id: septin-original-validation-hydrogenosome
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/original-checks.json
  locator: Original native validate/render and git-show historical target SHA
  summary: Both native commands exit zero; rendered Markdown is byte-identical and
    the original frozen hash matches its historical revision.
  accessed_at: '2026-11-03T14:54:30.524171Z'
  support: supports
  snapshot_sha256: 67e12ae441e841ca5bdf38fd617d6792a91a4f7a8ed8c0587ced878dba582a3d
- evidence_id: septin-native-hydrogenosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-verify-receipt.json
  locator: Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-verify.log
  summary: Exit zero. Zero protein examples and three anchored GENE_OR_PROTEIN nodes
    classified NO_GENE_SYMBOLS for import, pyruvate/energy and ISC classes. This is
    not an empty typed-node inventory. No accession-specific membership or necessity
    is certified.
  accessed_at: '2026-11-03T14:51:25.713642Z'
  support: supports
  snapshot_sha256: f11a27a770c100a7144c3c91a12a96c8ccf0b814e2dd117db4ccfac0cfbd2d7a
- evidence_id: septin-native-hydrogenosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-causal-receipt.json
  locator: Actual receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/hydrogenosome-uniprot-causal.log
  summary: Exit zero. Zero protein examples and three anchored GENE_OR_PROTEIN nodes
    classified NO_GENE_SYMBOLS for import, pyruvate/energy and ISC classes. This is
    not an empty typed-node inventory. No accession-specific membership or necessity
    is certified.
  accessed_at: '2026-11-03T14:51:26.166327Z'
  support: supports
  snapshot_sha256: 69d8b03ad74f7e2550e0a339c7df8caa32c4c664a193a8cc8411568480854a19
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009514,GO:0046861,GO:0031908,GO:0005777,GO:0006097,GO:0042566,GO:0046859,GO:0034492,GO:0016020,GO:0043231,GO:0005737
  locator: 'Eleven active exact GO entries: definitions and relation-bearing children'
  summary: GO0009514 is whole glyoxysome, GO0046861 its complete membrane and GO0031908
    its lumen. GO0042566 is hydrogenosome, GO0046859 its complete membrane and GO0034492
    its lumen. These assembled membranes are not chemical lipid identities. GO0034492
    states the volume enclosed by a hydrogenosome membrane; the word inner is biological
    contextual interpretation, not verbatim GO wording. Parent and part_of relationships
    are distinguished.
  accessed_at: '2026-11-03T14:51:37.203911Z'
  support: supports
  snapshot_sha256: 2bbfe3bc9e8cf53323ba8463244882c4a9090562975e41121202360747d67479
- evidence_id: septin-ancestors-0009514
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009514/ancestors?relations=is_a
  locator: Exact GO ancestors endpoint with relations=is_a only
  summary: Glyoxysome is_a peroxisome GO0005777.
  accessed_at: '2026-11-03T14:51:37.204246Z'
  support: supports
  snapshot_sha256: 8609f60b2bdc81e4e6f6b71bf40863df9922e1b00e6d8c9e73f786005de2db0e
- evidence_id: septin-ancestors-0042566
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042566/ancestors?relations=is_a
  locator: Exact GO ancestors endpoint with relations=is_a only
  summary: Hydrogenosome has GO0043231 organelle is_a ancestry; cytoplasm parthood
    is a separate relationship.
  accessed_at: '2026-11-03T14:51:37.204342Z'
  support: supports
  snapshot_sha256: dfab9eea2f76c933c9e123c9dea011d3751586701bdc0cc4e6c0c724bc9ce735
- evidence_id: septin-ancestors-0046859
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046859/ancestors?relations=is_a
  locator: Exact GO ancestors endpoint with relations=is_a only
  summary: Hydrogenosomal membrane has broad GO0016020 membrane is_a ancestry, not
    necessarily a direct named parent edge.
  accessed_at: '2026-11-03T14:51:37.204417Z'
  support: supports
  snapshot_sha256: 9002815c1491286b538071c5e7d15aba8f6ecbd6002aa54d4bf9fb0684711728
- evidence_id: septin-SL-0131
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0131.json
  locator: Exact location entry, direct GO mapping, names/synonyms and relation-bearing
    parents
  summary: Whole glyoxysome GO0009514; plant/catalase-oriented authority narrative
    is not independent evidence for Neurospora-specific composition. Nested mappings
    do not become exact xrefs of the queried structure.
  accessed_at: '2026-11-03T14:51:37.204475Z'
  support: supports
  snapshot_sha256: cf99e708d621df3115ac0a2989d8db95df1e7c7fa23f4f9d6c83d60b64952e64
- evidence_id: septin-SL-0130
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0130.json
  locator: Exact location entry, direct GO mapping, names/synonyms and relation-bearing
    parents
  summary: Complete glyoxysome membrane GO0046861, membrane synonym and whole-organelle
    parthood. Nested mappings do not become exact xrefs of the queried structure.
  accessed_at: '2026-11-03T14:51:37.916093Z'
  support: supports
  snapshot_sha256: 0bcde00617f838f8f0289d03c8684bef62b2d5b471ee28148b796b7294176e3e
- evidence_id: septin-SL-0333
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0333.json
  locator: Exact location entry, direct GO mapping, names/synonyms and relation-bearing
    parents
  summary: Glyoxysome matrix GO0031908, lumen synonym and parthood. Nested mappings
    do not become exact xrefs of the queried structure.
  accessed_at: '2026-11-03T14:51:37.933130Z'
  support: supports
  snapshot_sha256: f72cb3a1f7b5389a3224af2407dc7e4c8f90f7fe7afd53280565f7a62c8b97b5
- evidence_id: septin-SL-0145
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0145.json
  locator: Exact location entry, direct GO mapping, names/synonyms and relation-bearing
    parents
  summary: Whole hydrogenosome GO0042566; patchy flagellate/fungal/ciliate scope and
    hydrogen-producing ATP organelle. Some ciliate examples retain genomes; do not
    generalize T.vaginalis genome loss universally. Nested mappings do not become
    exact xrefs of the queried structure.
  accessed_at: '2026-11-03T14:52:13.655266Z'
  support: supports
  snapshot_sha256: 1619e9ef3c91874dca28de406dea777156d72b9bb70ae533300ba50b56deaf60
- evidence_id: septin-SL-0144
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0144.json
  locator: Exact location entry, direct GO mapping, names/synonyms and relation-bearing
    parents
  summary: Complete hydrogenosome membrane GO0046859, hydrogenosomal membrane synonym
    and organelle parthood. Nested mappings do not become exact xrefs of the queried
    structure.
  accessed_at: '2026-11-03T14:51:37.959470Z'
  support: supports
  snapshot_sha256: fccca371507283bd774e05a93feda2a3bc58eee39bb06c0b458c57786a80456a
- evidence_id: septin-SL-0335
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0335.json
  locator: Exact location entry, direct GO mapping, names/synonyms and relation-bearing
    parents
  summary: Hydrogenosome matrix GO0034492, lumen synonym and parthood. Nested mappings
    do not become exact xrefs of the queried structure.
  accessed_at: '2026-11-03T14:51:37.962327Z'
  support: supports
  snapshot_sha256: 96793a2ae46ab05de07492a336d115179a5cf644697d96c5e5d3c4f4daf25c7d
- evidence_id: septin-tax5141
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141
  locator: Exact ENA taxonomy entry/rank/lineage/synonyms
  summary: Species Neurospora crassa.
  accessed_at: '2026-11-03T14:51:38.499328Z'
  support: supports
  snapshot_sha256: 574584705a280fad9f1e98d4f83398508b511c50023ca90be837a4a72c20911c
- evidence_id: septin-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Exact ENA taxonomy entry/rank/lineage/synonyms
  summary: Domain Eukaryota; broad RARE occurrence means patchy qualitative distribution,
    not an experimentally measured frequency.
  accessed_at: '2026-11-03T14:51:38.518415Z'
  support: supports
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: septin-tax5722
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5722
  locator: Exact ENA taxonomy entry/rank/lineage/synonyms
  summary: Species Trichomonas vaginalis, with historical Tritrichomonas vaginalis
    synonym. This is distinct from Tritrichomonas foetus used in the original Lindmark
    study.
  accessed_at: '2026-11-03T14:51:39.097242Z'
  support: supports
  snapshot_sha256: 187c33fcc8a5be0659d37aa99eb3c11f74b2e42cab385cd8ff38b2ba0175e47f
- evidence_id: septin-dezoysa1994-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/BF00309930&pageSize=25
  locator: Exact native bibliographic identity and complete abstractText
  summary: 'Complete primary abstract: de Zoysa and Connerton1994 demonstrate nutritionally
    acetate-induced glyoxysomes in Neurospora crassa and targeting of C-terminally
    modified CAT reporters. They distinguish glyoxylate-cycle-containing microbodies
    from catalase-containing peroxisome-like bodies; ARM is ineffective. The publisher
    PDF is not newly accessible; no uninspected methods/table/strain detail is certified.'
  accessed_at: '2026-11-03T14:51:39.106988Z'
  support: supports
  snapshot_sha256: a249a609ce7cf4d9663970634e9e7685e35d40958c2b927c1f479af8b2610485
  search_scope: Europe PMC exact 10.1007/BF00309930 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:39.106988Z.
    This is not an exhaustive literature search.
- evidence_id: septin-tachezy2022-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12922&pageSize=25
  locator: Exact native bibliographic identity and complete abstractText
  summary: Exact current title is The hydrogenosome of Trichomonas vaginalis, by Tachezy,
    Makki and Hrdý, year2022. Complete secondary-review abstract supports organelle
    background, not a new primary experiment. Both assigned hydrogenosomal records
    carry the wrong title.
  accessed_at: '2026-11-03T14:51:39.165701Z'
  support: supports
  snapshot_sha256: f5df47ab6345453693117f507582cd8e121784da785f1bd57dcd69cdea829ba3
  search_scope: Europe PMC exact 10.1111/jeu.12922 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:39.165701Z.
    This is not an exhaustive literature search.
- evidence_id: septin-schneider2011-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ijpara.2011.10.001&pageSize=25
  locator: Exact native bibliographic identity and complete abstractText
  summary: Complete primary abstract and exact publication identity/PMID22079833.
    Year2011 is publication metadata; a later repository manuscript-release date is
    not a different experiment.
  accessed_at: '2026-11-03T14:51:39.279395Z'
  support: supports
  snapshot_sha256: f4fda6bc22338b0fd07a9b81ebc99336b62eab19c18354b378368786a30905bb
  search_scope: Europe PMC exact 10.1016/j.ijpara.2011.10.001 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:39.279395Z.
    This is not an exhaustive literature search.
- evidence_id: septin-bui1996-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.93.18.9651&pageSize=25
  locator: Exact native bibliographic identity and complete abstractText
  summary: 'Complete primary abstract: Hsp70/Hsp60/Hsp10 mitochondrial-family affinity
    and short N-terminal processing of mature Hsp60 support mitochondrial-type protein
    ancestry/processing. This does not demonstrate an exclusive universal targeting
    route; historical early-branching phylogenetic rhetoric is not adopted.'
  accessed_at: '2026-11-03T14:51:39.699918Z'
  support: supports
  snapshot_sha256: 8f55f9c258ed021697f73dfcacd4daad4fd4bfec9bf7e368272157d03f7d56e3
  search_scope: Europe PMC exact 10.1073/pnas.93.18.9651 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:39.699918Z.
    This is not an exhaustive literature search.
- evidence_id: septin-sutak2004-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0401319101&pageSize=25
  locator: Exact native bibliographic identity and complete abstractText
  summary: 'Complete primary abstract: TvIscS-2 localizes to hydrogenosomes and hydrogenosomal
    extracts support FeS reconstitution of apoferredoxin; this does not independently
    localize every ISC member.'
  accessed_at: '2026-11-03T14:51:39.849209Z'
  support: supports
  snapshot_sha256: 084690cec8acd56239378a6ba2e8ebb31ff08a03d8c00ef5f70d52d1040a874d
  search_scope: Europe PMC exact 10.1073/pnas.0401319101 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:39.849209Z.
    This is not an exhaustive literature search.
- evidence_id: septin-dolezal2005-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0500349102&pageSize=25
  locator: Exact native bibliographic identity and complete abstractText
  summary: 'Complete primary abstract: Giardia/T.vaginalis targeting and processing
    recognize N-terminal and internal signals; shared machinery does not imply every
    native cargo requires a cleavable presequence.'
  accessed_at: '2026-11-03T14:51:39.955697Z'
  support: supports
  snapshot_sha256: b3d3a2f14bcd1b8bae2a3f2d39b8d40daaa65dedb5e730c3b2c93c22bcf41230
  search_scope: Europe PMC exact 10.1073/pnas.0500349102 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:39.955697Z.
    This is not an exhaustive literature search.
- evidence_id: septin-lindmark1973-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A4750424%20AND%20SRC%3AMED&pageSize=25
  locator: Exact native bibliographic identity and metadata only, no abstractText
  summary: Exact title, authors, year1973, PMID4750424 and DOI10.1016/s0021-9258(19)43249-3
    verified. The native record has no abstract; current access is bibliography only.
    Detailed original Tritrichomonas foetus experiments are not freshly certified.
  accessed_at: '2026-11-03T14:51:40.152045Z'
  support: supports
  snapshot_sha256: 54299eb5e6aac224dab7a77f15f64ebd0993ca373a700d8070620e5b493b4227
  search_scope: Europe PMC exact PMID4750424 identifier query; format=json,resultType=core,pageSize25,one
    returned MED article,no date restriction; actual fetch 2026-11-03T14:51:40.152045Z.
    This is not an exhaustive literature search.
- evidence_id: septin-schneider2011-bioc
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC4437511/unicode
  locator: 'NCBI BioC primary body: complete Introduction and Methods2.1–2.7; Results/Discussion3.1,3.5,3.7,3.8,3.9,3.10;
    no figure pixels, separate supplements or raw spectra'
  summary: T.vaginalis T1 hydrogenosome fractionation and mass spectrometry support
    energy enzymes and ISC proteins, including IscU. The proteome has external associations,
    potential contaminants and family-level indistinguishable peptides; fraction detection
    does not independently prove every subcompartment location. Section3.8 explicitly
    preserves targeting without an N-terminal presequence and stringent motif prediction
    as an alternative to true signal absence. Translocase candidates/models are not
    all functionally demonstrated; nondetection is not absence.
  accessed_at: '2026-11-03T14:53:16.413225Z'
  support: supports
  snapshot_sha256: 146aa456a4fbaef150a91822d6a006cd33815d8e6eb515f648f2fd597f345ed6
- evidence_id: septin-sutak2004-maintext
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC478578/
  locator: 'Retained web-reader primary main text: abstract/introduction; Methods
    lines131–144; Results145–200; Discussion201–209; Fig1–7 caption text, not pixels'
  summary: Fresh rendered primary text retained in /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/primary-web-reader-receipt.json.
    C-1:NIH30001 T.vaginalis cells, iron-rich/restricted culture, fractionation and
    immunolocalization directly examine TvIscS-2. FeS reconstitution uses hydrogenosomal
    lysate and apoferredoxin with cysteine/iron and controls. IscU appears in yeast/bacterial
    model/interaction discussion, not a T.vaginalis IscU localization experiment.
    No IscU biological absence inference follows.
  accessed_at: '2026-11-03T14:54:07Z'
  support: supports
  snapshot_sha256: 38d3ee0b7ecdbf6ed2c852179f3cebdacba8b8b9f56dddd037b69430760cac09
- evidence_id: septin-dolezal2005-indexed-maintext
  kind: search
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1182405/
  locator: 'Detailed web-index primary text: returned abstract/introduction, main
    Methods, Results/Discussion and Fig1–5 caption text; no fresh raw HTML/PDF or
    figure pixels'
  summary: Retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/dolezal-indexed-body-receipt.json.
    Giardia WB, T.vaginalis T1 and yeast YPH499 are distinct experimental systems.
    Heterologous Giardia GiIscU/Gifdx N-terminal deletions impair targeting; GiIscS
    has no N-terminal extension and both N-terminal202aa and C-terminal232aa fragments
    enter hydrogenosomes, supporting internal signals. Processing/EDTA and Pam18 localization
    support selected machinery properties, not every native cargo or complete functional
    translocase mechanism. Search-index crawl was reported as six days old; retrieval
    now does not imply fresh publisher body access.
  accessed_at: '2026-11-03T14:55:41Z'
  support: supports
  snapshot_sha256: 621a696e6762c70bd41812b58162a187422c1499271f5dd84b4306735ad9c808
  search_scope: Web index; one query containing exact PMC1182405 URL and quoted GiiscS/Internal
    terms; default returned set, no date restriction; actual retrieval 2026-11-03T14:55:41Z.
    The returned detailed primary-body passages were read; no global literature absence
    claim or unreturned passage is certified.
- evidence_id: septin-source-access-limits
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/adversary-septin/source-receipts.json
  locator: Actual fresh route receipts and retained files
  summary: Direct/canonical PMC routes returned browser challenges; Sutak/Dolezal
    BioC returned no-result help pages, not bodies. EuropePMC fullTextXML returned500;
    S3 guesses returned404. deZoysa PDF endpoint returned HTML Client Challenge; Lindmark
    PDF returned403; Dolezal UMass download timed out. These routes are not evidence
    of biological absence or freshly read full text. Successful Schneider BioC, Sutak
    rendered body and Dolezal indexed body have separately identified scopes.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 74ae6347a9461ed9aa62bb3bce437e84f9a3f35791c1634709385e8dd17d9213
- evidence_id: septin-context-glyoxysomal_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
  locator: Frozen boundary context only
  summary: Read identity, whole/lumen/membrane distinctions and reciprocal parthood
    to check assigned record boundaries. This is not a full review or issue disposition
    of this neighbor.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b
- evidence_id: septin-context-glyoxysomal_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
  locator: Frozen boundary context only
  summary: Read identity, whole/lumen/membrane distinctions and reciprocal parthood
    to check assigned record boundaries. This is not a full review or issue disposition
    of this neighbor.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c
- evidence_id: septin-context-hydrogenosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosome_lumen.yaml
  locator: Frozen boundary context only
  summary: Read identity, whole/lumen/membrane distinctions and reciprocal parthood
    to check assigned record boundaries. This is not a full review or issue disposition
    of this neighbor.
  accessed_at: '2026-11-03T15:00:59.984309Z'
  support: supports
  snapshot_sha256: 30c5139da8ac02b5d677b314f371d09b1a64fa10a6bb45352d3b8b76c298fd40
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official iModulonDB catalogue response; all returned organism
    id/name/dataset-key fields scanned
  summary: No returned dataset host matches Neurospora crassa, Trichomonas vaginalis
    or the other eukaryotic experimental/organellar contexts considered here. No matched-host
    downstream gene/module query is justified; E.coli recombinant expression is not
    an organelle-host substitute. This is catalogue noncoverage, not biological absence.
  accessed_at: '2026-11-03T14:51:40.302644Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official GET https://imodulondb.org/api/datasets at 2026-11-03T14:51:40.302644Z;
    complete response of20 organism rows, no date filter or pagination truncation;
    scan id/name/dataset keys for Neurospora/crassa, Trichomonas/vaginalis, Tritrichomonas/foetus,
    Giardia and eukaryotic fungal/plant/ciliate contexts. No claim about exhaustive
    biological absence or equivalence of organism/dataset pairs and unique keys.
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical00:49Z actual runner attempt; not a new invocation
  summary: Actual attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z exited1 with
    PermissionError reading pyvenv.cfg. Runner was unavailable in this environment.
    Current official HTTP catalogue/source fallback is recorded separately; no successful
    runner execution is claimed.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:56:48.539933Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: ec9d71bac25b4f843dcdb4d988135369611c76d12c16d3ab3de13bf4785ed17b
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:51:48.418568Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:51:28.362177Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:51:22.338249Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:51:18.154949Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T15:02:38Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: cc98c3961138a5eea3b92c69a41d9570380d6fab06e75fe8329447766c5b6d53
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2367/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T14:53:29.181896Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 37d0c158f41cac2e771f689ea008ac954a510910942e5d05e62893c11128d5e4
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2367
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t4-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: Complete target has no component protein_examples and zero GENE_OR_PROTEIN
    nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions
    require independent scientific assessment. Both actual native commands exit0;
    no hidden family or necessity certification.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-native-golgi_cisterna-verify
  - plaque-native-golgi_cisterna-causal
  - plaque-protein-contract
- assessment_id: plaque-t4-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Original pair validates/renders; all 14 historical inputs match its source;
    target unchanged. No historical group/neighbor/category finding is terminally
    resolved. Exact cisterna F1 lineage retained where applicable.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-checks
- assessment_id: plaque-t4-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: All current fields, evidence, history, discussions and graphs inspected.
    No target image assets, quantitative properties, associated_traits or verbatim
    snippets. Empty optional accession inventories and unset exact lipid chemistry
    are not invented completeness defects. PROPOSED remains unchanged.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-rubric
- assessment_id: plaque-t4-adapter
  area: scope
  topic: Positive pathway trigger and matched-host assessment
  outcome: supported
  summary: Explicit current cisternal maturation with resident-marker identity transitions
    triggers assessment. Original check is an unsupported expression-only exclusion,
    not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module
    query or unrelated-organism proxy is justified. Historical unavailable runner
    is separately dated; source fallback is complete within declared tiers.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-taxonomy
  area: scope
  topic: Yeast species and experimental scope
  outcome: supported
  summary: NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured
    prevalence. Losev and Matsuura-Tokita directly examine budding-yeast cisternal
    marker transitions; canonical imaging example is supported. Exact supplement strain
    constructions and universal all-eukaryote dynamics are not inferred.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-tax4932
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
- assessment_id: plaque-t5-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: Complete target has no component protein_examples and zero GENE_OR_PROTEIN
    nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions
    require independent scientific assessment. Both actual native commands exit0;
    no hidden family or necessity certification.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-native-golgi_cisterna_membrane-verify
  - plaque-native-golgi_cisterna_membrane-causal
  - plaque-protein-contract
- assessment_id: plaque-t5-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Original pair validates/renders; all 17 historical inputs match its source;
    target unchanged. No historical group/neighbor/category finding is terminally
    resolved. Exact cisterna F1 lineage retained where applicable.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-original-checks
- assessment_id: plaque-t5-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: All current fields, evidence, history, discussions and graphs inspected.
    No target image assets, quantitative properties, associated_traits or verbatim
    snippets. Empty optional accession inventories and unset exact lipid chemistry
    are not invented completeness defects. PROPOSED remains unchanged.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-rubric
- assessment_id: plaque-t5-adapter
  area: scope
  topic: Positive pathway trigger and matched-host assessment
  outcome: supported
  summary: Explicit current cisternal maturation with resident-marker identity transitions
    triggers assessment. Original check is an unsupported expression-only exclusion,
    not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module
    query or unrelated-organism proxy is justified. Historical unavailable runner
    is separately dated; source fallback is complete within declared tiers.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-original-5
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t5-taxonomy
  area: scope
  topic: Yeast species and experimental scope
  outcome: supported
  summary: NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured
    prevalence. Losev and Matsuura-Tokita directly examine budding-yeast cisternal
    marker transitions; canonical imaging example is supported. Exact supplement strain
    constructions and universal all-eukaryote dynamics are not inferred.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-tax4932
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
- assessment_id: plaque-t6-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: Complete target has no component protein_examples and zero GENE_OR_PROTEIN
    nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions
    require independent scientific assessment. Both actual native commands exit0;
    no hidden family or necessity certification.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-native-golgi_lumen-verify
  - plaque-native-golgi_lumen-causal
  - plaque-protein-contract
- assessment_id: plaque-t6-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Original pair validates/renders; all 16 historical inputs match its source;
    target unchanged. No historical group/neighbor/category finding is terminally
    resolved. Exact cisterna F1 lineage retained where applicable.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-original-checks
- assessment_id: plaque-t6-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: All current fields, evidence, history, discussions and graphs inspected.
    No target image assets, quantitative properties, associated_traits or verbatim
    snippets. Empty optional accession inventories and unset exact lipid chemistry
    are not invented completeness defects. PROPOSED remains unchanged.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-rubric
- assessment_id: plaque-t6-adapter
  area: scope
  topic: Positive pathway trigger and matched-host assessment
  outcome: supported
  summary: Explicit current VRG4-dependent GDP-mannose import and lumenal glycosylation
    triggers assessment. Original check is an unsupported expression-only exclusion,
    not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module
    query or unrelated-organism proxy is justified. Historical unavailable runner
    is separately dated; source fallback is complete within declared tiers.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t6-taxonomy
  area: scope
  topic: Yeast species and experimental scope
  outcome: supported
  summary: NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured
    prevalence. Primary Dean abstract supports the yeast Golgi vesicle/canonical nucleotide-sugar
    example; exact experimental strain and quantitative transport data are not independently
    certified.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-tax4932
  - plaque-dean1997-meta
- assessment_id: plaque-t7-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: Complete target has no component protein_examples and zero GENE_OR_PROTEIN
    nodes. Mechanical coverage is empty-inventory scope; narrative pathway assertions
    require independent scientific assessment. Both actual native commands exit0;
    no hidden family or necessity certification.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-native-golgi_membrane-verify
  - plaque-native-golgi_membrane-causal
  - plaque-protein-contract
- assessment_id: plaque-t7-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Original pair validates/renders; all 17 historical inputs match its source;
    target unchanged. No historical group/neighbor/category finding is terminally
    resolved. Exact cisterna F1 lineage retained where applicable.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-original-checks
- assessment_id: plaque-t7-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: All current fields, evidence, history, discussions and graphs inspected.
    No target image assets, quantitative properties, associated_traits or verbatim
    snippets. Empty optional accession inventories and unset exact lipid chemistry
    are not invented completeness defects. PROPOSED remains unchanged.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-rubric
- assessment_id: plaque-t7-adapter
  area: scope
  topic: Positive pathway trigger and matched-host assessment
  outcome: supported
  summary: Explicit current COPI coat assembly and COPI-dependent vesicle budding
    triggers assessment. Original check is an unsupported expression-only exclusion,
    not an omitted row. Fresh catalogue contains no yeast host, so no matched gene/module
    query or unrelated-organism proxy is justified. Historical unavailable runner
    is separately dated; source fallback is complete within declared tiers.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t7-taxonomy
  area: scope
  topic: Yeast species and experimental scope
  outcome: supported
  summary: NCBITaxon4932 denotes S. cerevisiae; COMMON is qualitative, not measured
    prevalence. Losev and Matsuura-Tokita directly examine budding-yeast cisternal
    marker transitions; canonical imaging example is supported. Exact supplement strain
    constructions and universal all-eukaryote dynamics are not inferred.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-tax4932
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
- assessment_id: plaque-t4-identity
  area: identity
  topic: Whole cisterna versus membrane
  outcome: supported
  summary: GO0031985 denotes a flattened membrane-bounded Golgi subcompartment, matching
    native kind and definition; its boundary GO0032580 remains distinct. Parent0098791
    and part_of0005794/has_part0032580 are appropriately scoped.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-ancestors-0031985
- assessment_id: plaque-t4-composition
  area: grounding
  topic: Reviewed label-only aggregate bilayer
  outcome: supported
  summary: The LIPID row deliberately names aggregate boundary material without guessing
    a chemical CURIE or individual lipid necessity. ESSENTIAL denotes collective membrane
    boundary at this coarse level. This valid material row does not make the whole
    cisterna its identity.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-schema-policy
- assessment_id: plaque-t4-graph
  area: graph
  topic: Whole-compartment component_ref mismatch
  outcome: concern
  summary: The graph node golgi_cisterna denotes the complete membrane-bounded compartment
    GO0031985 but component_ref points to golgi_cisternal_lipid_bilayer. That component
    denotes boundary lipid material, while the separate golgi_cisterna_membrane node
    already denotes the correct GO0032580 boundary. The schema defines component_ref
    as identifying a node that is one of the record’s components, so this join incorrectly
    equates whole compartment and lipid constituent.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-schema-policy
- assessment_id: plaque-t4-function
  area: evidence
  topic: Source-supported cisternal maturation
  outcome: supported
  summary: Early-to-late resident-marker transitions, membrane bounding and Golgi
    parthood are supported. Primary imaging supports the described yeast maturation
    sequence; not exclusive cargo transport, exact molecular recycling or all-Golgi
    kinetics. The component_ref mismatch does not invalidate these biological edges.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
  - plaque-go
- assessment_id: plaque-t5-identity
  area: identity
  topic: Specific cisternal membrane and broader generic parent
  outcome: supported
  summary: GO0032580 is the membrane surrounding a flattened central Golgi cisterna;
    part_of0031985 is supported. Parent0000139 is supported by definitions as a membrane
    of a Golgi compartment, although current is_a-only native ancestry does not explicitly
    include it; no direct GO edge asserted.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-ancestors-0032580
- assessment_id: plaque-t5-composition
  area: grounding
  topic: Boundary component correspondence
  outcome: supported
  summary: Reviewed-label-only bilayer constituent and the membrane-node component_ref
    describe the boundary material. Unlike whole-cisterna F1, this does not equate
    a whole compartment with lipid. No arbitrary specific chemical identity or universal
    lipid species is supplied.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-current-4
  - plaque-schema-policy
  - plaque-go
- assessment_id: plaque-t5-graph
  area: graph
  topic: Boundary topology and maturation context
  outcome: supported
  summary: NONMECHANISTIC membrane-bounds-cisterna, cisterna-part-of-Golgi and cisterna-undergoes-marker-maturation
    edges are supported by exact authority and inspected yeast primary PDFs. Broad
    maturation does not assert membrane fusion molecular mechanism.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
- assessment_id: plaque-t6-identity
  area: identity
  topic: Golgi lumen identity and synonyms
  outcome: supported
  summary: GO0005796 and SL0133 identify Golgi apparatus/complex lumen, the interior
    bounded by Golgi compartments including networks. SUBCELLULAR_REGION, is_a0070013
    and part_of0005794 are consistent. It is neither whole Golgi nor membrane.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-go
  - plaque-SL0133
  - plaque-ancestors-0005796
- assessment_id: plaque-t6-composition
  area: grounding
  topic: Sparse lumen with boundary transporter context
  outcome: supported
  summary: No stable constituent inventory is asserted. Vrg4 is properly described
    as membrane-localized transport support supplying lumen substrate; it is not fabricated
    as stable lumen material. The existing resolved boundary discussion is consistent
    with current source but no historical issue completion is re-certified.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-dean1997-meta
  - plaque-schema-policy
- assessment_id: plaque-t6-function
  area: evidence
  topic: GDP-mannose import and glycosylation access
  outcome: supported
  summary: Dean primary abstract supports Golgi-vesicle GDP-mannose import defects
    in vrg4 mutants and corresponding mannosylation defects. This supports lumenal
    substrate access and the canonical example without claiming purified Vrg4 sufficiency
    or unique formation necessity.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-dean1997-meta
- assessment_id: plaque-t6-graph
  area: graph
  topic: Three purely descriptive lumen relations
  outcome: supported
  summary: Lumen is_a organelle lumen, part_of Golgi and bounded by Golgi membrane
    are supported by current GO and SL0133 definitions. No uninspected molecular transport
    mechanism is encoded by these three NONMECHANISTIC edges.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-go
  - plaque-SL0133
  - plaque-ancestors-0005796
- assessment_id: plaque-t7-identity
  area: identity
  topic: Generic Golgi membrane scope
  outcome: supported
  summary: GO0000139 denotes membranes surrounding any Golgi compartment, matching
    generic definition and exact apparatus synonym; parent0016020 is supported by
    ancestry and part_of0005794 by authority. Specific cisternal membrane remains
    a narrower boundary.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-ancestors-0000139
  - plaque-current-5
- assessment_id: plaque-t7-composition
  area: grounding
  topic: Generic bilayer constituent correspondence
  outcome: supported
  summary: Reviewed-label-only aggregate LIPID avoids guessing chemistry; the membrane-node
    component_ref remains at boundary material scope rather than whole-organelle identity.
    ESSENTIAL is collective boundary necessity, not every individual lipid species.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-schema-policy
  - plaque-go
- assessment_id: plaque-t7-maturation
  area: evidence
  topic: Generic example retains budding-yeast scope
  outcome: supported
  summary: Canonical Losev/Matsuura-Tokita yeast marker maturation remains supported
    by complete inspected primary text and captions. Generic membrane identity does
    not universalize experimental kinetics or imply every Golgi membrane matures identically.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
- assessment_id: plaque-t7-graph
  area: graph
  topic: Coat assembly, budding and descriptive topology
  outcome: supported
  summary: Membrane part_of Golgi and bounds cisterna are valid topology. ARF/COPI
    recruitment and coat participation in budding are supported by Serafini primary
    abstract, GO and conditional Bremser reconstitution abstract. Broad mediates/drives
    language is read as functional participation, not coat-alone sufficiency, yeast-specific
    reconstitution, every Golgi compartment or a complete molecular mechanism.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-serafini1991-quoted
  - plaque-go-budding-primary-10052452
  - plaque-papanikou2014-s3
  - plaque-graph-rubric
- assessment_id: plaque-t4-limits
  area: evidence
  topic: Explicit access and mechanism limits
  outcome: unknown
  summary: Primary microscopy PDFs were read as main text/Methods/captions, not figure
    pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level
    where used; short DOI landing HTML is not body. Papanikou is secondary selected-section
    context. Exact lipid chemistry, exclusive transport route, quantitative generalization
    and individual component formation necessity remain unestablished.
  target_ids:
  - GO:0031985
  evidence_ids:
  - plaque-current-4
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
  - plaque-dean1997-meta
  - plaque-serafini1991-quoted
  - plaque-go-budding-primary-10052452
  - plaque-papanikou2014-s3
- assessment_id: plaque-t5-limits
  area: evidence
  topic: Explicit access and mechanism limits
  outcome: unknown
  summary: Primary microscopy PDFs were read as main text/Methods/captions, not figure
    pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level
    where used; short DOI landing HTML is not body. Papanikou is secondary selected-section
    context. Exact lipid chemistry, exclusive transport route, quantitative generalization
    and individual component formation necessity remain unestablished.
  target_ids:
  - GO:0032580
  evidence_ids:
  - plaque-current-5
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
  - plaque-dean1997-meta
  - plaque-serafini1991-quoted
  - plaque-go-budding-primary-10052452
  - plaque-papanikou2014-s3
- assessment_id: plaque-t6-limits
  area: evidence
  topic: Explicit access and mechanism limits
  outcome: unknown
  summary: Primary microscopy PDFs were read as main text/Methods/captions, not figure
    pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level
    where used; short DOI landing HTML is not body. Papanikou is secondary selected-section
    context. Exact lipid chemistry, exclusive transport route, quantitative generalization
    and individual component formation necessity remain unestablished.
  target_ids:
  - GO:0005796
  evidence_ids:
  - plaque-current-6
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
  - plaque-dean1997-meta
  - plaque-serafini1991-quoted
  - plaque-go-budding-primary-10052452
  - plaque-papanikou2014-s3
- assessment_id: plaque-t7-limits
  area: evidence
  topic: Explicit access and mechanism limits
  outcome: unknown
  summary: Primary microscopy PDFs were read as main text/Methods/captions, not figure
    pixels, movies or supplements. Dean/Serafini/Bremser support remains primary abstract-level
    where used; short DOI landing HTML is not body. Papanikou is secondary selected-section
    context. Exact lipid chemistry, exclusive transport route, quantitative generalization
    and individual component formation necessity remain unestablished.
  target_ids:
  - GO:0000139
  evidence_ids:
  - plaque-current-7
  - plaque-losev2006-pdf
  - plaque-matsuura2006-pdf
  - plaque-dean1997-meta
  - plaque-serafini1991-quoted
  - plaque-go-budding-primary-10052452
  - plaque-papanikou2014-s3
- assessment_id: micro-golgi_apparatus-identity
  area: identity
  topic: Exact whole/membrane identity and hierarchy
  outcome: supported
  summary: Current native GO names, definitions, synonyms and typed relations support
    the exact target and its broader parent/parthood. Apparatus/cisternae, complete
    vesicle and its membrane remain distinct. COPI and TGN are bounded child examples,
    not universal generic-class attributes.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-go
  - micro-policy
- assessment_id: micro-golgi_apparatus-taxon
  area: scope
  topic: Yeast canonical scope and protein strain identity
  outcome: supported
  summary: Saccharomyces4932 is the named canonical species with qualitative COMMON
    occurrence. Native protein examples are S288C559292 identities, not proof every
    imaging/transport experiment used that strain. Yeast imaging and retrieval are
    kept separate from generic Golgi-derived coated-vesicle biochemical context.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-tax4932
  - micro-tax559292
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-letourneur1994-meta
  - micro-serafini1991-quoted
- assessment_id: micro-golgi_apparatus-composition
  area: grounding
  topic: Components, physical assembly scope and grounding
  outcome: concern
  summary: Six reviewed examples and bounded uniqueness claims match. Broad glycosylation-enzyme
    class remains allowed and label-only across distinct enzyme families. SNARE source
    attribution F1 remains; new complex retyping F3 needs correction because retained
    broad cohort is not the specific named physical assembly.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-component-policy
  - micro-go
  - micro-protein-P31755
  - micro-protein-P39106
  - micro-protein-P27809
  - micro-protein-Q01590
  - micro-protein-Q08144
  - micro-protein-P22214
  - micro-pmid11001058
  - micro-pmid9930650
  - micro-papanikou2014-bioc
- assessment_id: micro-golgi_apparatus-necessity
  area: evidence
  topic: Formation necessity versus function and boundary identity
  outcome: unknown
  summary: Apparatus machinery has UNKNOWN essentiality. A defining membrane boundary
    is constitutive of the named membrane-bounded class, but this is not evidence
    each lipid species, coatomer subunit or SNARE is individually required for organelle
    assembly. Native annotations and transport-mutant assays are not exhaustive formation
    tests.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-component-policy
  - micro-letourneur1994-meta
  - micro-matsuura2006-pdf
  - micro-protein-P22214
- assessment_id: micro-golgi_apparatus-graph
  area: graph
  topic: Every current graph node and edge
  outcome: concern
  summary: Five NONMECHANISTIC FUNCTION edges checked. Membrane bounds cisterna, cisterna
    part_of apparatus and early-to-late marker transitions are supported. Glycosylation-enzyme
    compartment context is supported by review. The SNARE supports-maturation edge
    retains F1 source-attribution problem; it does not independently demonstrate each
    named actor is necessary.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-go
  - micro-graph-policy
  - micro-component-policy
  - micro-papanikou2014-bioc
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-serafini1991-quoted
  - micro-letourneur1994-meta
- assessment_id: micro-golgi_apparatus-coverage
  area: completeness
  topic: Entire maintained scope and optional slots
  outcome: supported
  summary: Entire current file/history/discussions and original observation read.
    No tracked target image, quantitative physical property, trait link or snippet
    asserted. Unresolved exact lipid/family terms are not automatic defects. PROPOSED
    status retained and no historical/group/category issue is terminally disposed.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-prior-golgi_apparatus
  - micro-policy
- assessment_id: micro-golgi_apparatus-source-tiers
  area: evidence
  topic: Primary body, abstract and secondary scopes
  outcome: supported
  summary: Losev/Matsuura genuine primary PDF main texts/Methods/captions were read
    independently from shared fresh snapshots, without pixels/movies/supplements.
    Papanikou full main BioC text is secondary review. Letourneur/Waters/Serafini
    and OCH1/SNARE supporting papers are complete primary abstracts only; exact access/assay
    limits retained.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-papanikou2014-bioc
  - micro-letourneur1994-meta
  - micro-waters1991-meta
  - micro-serafini1991-quoted
  - micro-karhinen2004-meta
  - micro-nakayama1992-meta
  - micro-bruinsma2004-meta
- assessment_id: micro-golgi_apparatus-native
  area: schema
  topic: Frozen originals and actual native coverage
  outcome: supported
  summary: Original native validate/render passed with byte-identical Markdown, original
    target hash confirmed from frozen revision. Current verify/causal receipts are
    source-head bound; their actual nonempty or zero inventories are explicitly limited,
    not scientific proof.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-prior-golgi_apparatus
  - micro-original-pairs
  - micro-native-golgi_apparatus-verify
  - micro-native-golgi_apparatus-causal
- assessment_id: micro-golgi_apparatus-adapter-defect
  area: provenance
  topic: Explicit expression-only exclusion is unsupported
  outcome: concern
  summary: Original check is present, not omitted, but excludes applicability because
    no expression-module inference is used. Current named proteins, coatomer/COPI
    retrieval and membrane-budding pathway assertions trigger actual coverage assessment
    under native policy. This is a bundle defect.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-prior-golgi_apparatus
  - micro-policy
- assessment_id: micro-golgi_apparatus-adapter-current
  area: evidence
  topic: Current exact-organism catalogue applicability
  outcome: not_applicable
  summary: Complete fresh official catalogue has no Saccharomyces/cerevisiae/S288C
    organism/dataset match. No matched gene/module key or downstream summarize applies;
    an unrelated bacterial proxy would be inappropriate. Historical00:49Z runner limitation
    remains historical.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-policy
  - micro-datasets
  - micro-historical-runner
- assessment_id: micro-golgi_associated_vesicle-identity
  area: identity
  topic: Exact whole/membrane identity and hierarchy
  outcome: supported
  summary: Current native GO names, definitions, synonyms and typed relations support
    the exact target and its broader parent/parthood. Apparatus/cisternae, complete
    vesicle and its membrane remain distinct. COPI and TGN are bounded child examples,
    not universal generic-class attributes.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-go
  - micro-policy
- assessment_id: micro-golgi_associated_vesicle-taxon
  area: scope
  topic: Yeast canonical scope and protein strain identity
  outcome: supported
  summary: Saccharomyces4932 is the named canonical species with qualitative COMMON
    occurrence. Native protein examples are S288C559292 identities, not proof every
    imaging/transport experiment used that strain. Yeast imaging and retrieval are
    kept separate from generic Golgi-derived coated-vesicle biochemical context.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-tax4932
  - micro-tax559292
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-letourneur1994-meta
  - micro-serafini1991-quoted
- assessment_id: micro-golgi_associated_vesicle-composition
  area: grounding
  topic: Components, physical assembly scope and grounding
  outcome: concern
  summary: 'F2 remains: molecular LIPID row is grounded to complete membrane GO0030660,
    which also propagates through component_ref. Correct has_part and membrane topology
    do not repair the distinct molecular/structure identity.'
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-component-policy
  - micro-go
- assessment_id: micro-golgi_associated_vesicle-necessity
  area: evidence
  topic: Formation necessity versus function and boundary identity
  outcome: unknown
  summary: Apparatus machinery has UNKNOWN essentiality. A defining membrane boundary
    is constitutive of the named membrane-bounded class, but this is not evidence
    each lipid species, coatomer subunit or SNARE is individually required for organelle
    assembly. Native annotations and transport-mutant assays are not exhaustive formation
    tests.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-component-policy
  - micro-letourneur1994-meta
  - micro-matsuura2006-pdf
  - micro-protein-P22214
- assessment_id: micro-golgi_associated_vesicle-graph
  area: graph
  topic: Every current graph node and edge
  outcome: concern
  summary: Four NONMECHANISTIC FUNCTION edges preserve membrane parthood, GO-defined
    Golgi evagination, COPI is_a child and bounded retrograde retrieval. GO/primary
    abstract scopes support these descriptions; membrane component_ref identity propagates
    F2.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-go
  - micro-graph-policy
  - micro-component-policy
  - micro-papanikou2014-bioc
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-serafini1991-quoted
  - micro-letourneur1994-meta
- assessment_id: micro-golgi_associated_vesicle-coverage
  area: completeness
  topic: Entire maintained scope and optional slots
  outcome: supported
  summary: Entire current file/history/discussions and original observation read.
    No tracked target image, quantitative physical property, trait link or snippet
    asserted. Unresolved exact lipid/family terms are not automatic defects. PROPOSED
    status retained and no historical/group/category issue is terminally disposed.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-prior-golgi_associated_vesicle
  - micro-policy
- assessment_id: micro-golgi_associated_vesicle-source-tiers
  area: evidence
  topic: Primary body, abstract and secondary scopes
  outcome: supported
  summary: Losev/Matsuura genuine primary PDF main texts/Methods/captions were read
    independently from shared fresh snapshots, without pixels/movies/supplements.
    Papanikou full main BioC text is secondary review. Letourneur/Waters/Serafini
    and OCH1/SNARE supporting papers are complete primary abstracts only; exact access/assay
    limits retained.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-papanikou2014-bioc
  - micro-letourneur1994-meta
  - micro-waters1991-meta
  - micro-serafini1991-quoted
  - micro-karhinen2004-meta
  - micro-nakayama1992-meta
  - micro-bruinsma2004-meta
- assessment_id: micro-golgi_associated_vesicle-native
  area: schema
  topic: Frozen originals and actual native coverage
  outcome: supported
  summary: Original native validate/render passed with byte-identical Markdown, original
    target hash confirmed from frozen revision. Current verify/causal receipts are
    source-head bound; their actual nonempty or zero inventories are explicitly limited,
    not scientific proof.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-prior-golgi_associated_vesicle
  - micro-original-pairs
  - micro-native-golgi_associated_vesicle-verify
  - micro-native-golgi_associated_vesicle-causal
- assessment_id: micro-golgi_associated_vesicle-adapter-defect
  area: provenance
  topic: Explicit expression-only exclusion is unsupported
  outcome: concern
  summary: Original check is present, not omitted, but excludes applicability because
    no expression-module inference is used. Current named proteins, coatomer/COPI
    retrieval and membrane-budding pathway assertions trigger actual coverage assessment
    under native policy. This is a bundle defect.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-prior-golgi_associated_vesicle
  - micro-policy
- assessment_id: micro-golgi_associated_vesicle-adapter-current
  area: evidence
  topic: Current exact-organism catalogue applicability
  outcome: not_applicable
  summary: Complete fresh official catalogue has no Saccharomyces/cerevisiae/S288C
    organism/dataset match. No matched gene/module key or downstream summarize applies;
    an unrelated bacterial proxy would be inappropriate. Historical00:49Z runner limitation
    remains historical.
  target_ids:
  - GO:0005798
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-policy
  - micro-datasets
  - micro-historical-runner
- assessment_id: micro-golgi_associated_vesicle_membrane-identity
  area: identity
  topic: Exact whole/membrane identity and hierarchy
  outcome: supported
  summary: Current native GO names, definitions, synonyms and typed relations support
    the exact target and its broader parent/parthood. Apparatus/cisternae, complete
    vesicle and its membrane remain distinct. COPI and TGN are bounded child examples,
    not universal generic-class attributes.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-go
  - micro-policy
- assessment_id: micro-golgi_associated_vesicle_membrane-taxon
  area: scope
  topic: Yeast canonical scope and protein strain identity
  outcome: supported
  summary: Saccharomyces4932 is the named canonical species with qualitative COMMON
    occurrence. Native protein examples are S288C559292 identities, not proof every
    imaging/transport experiment used that strain. Yeast imaging and retrieval are
    kept separate from generic Golgi-derived coated-vesicle biochemical context.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-tax4932
  - micro-tax559292
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-letourneur1994-meta
  - micro-serafini1991-quoted
- assessment_id: micro-golgi_associated_vesicle_membrane-composition
  area: grounding
  topic: Components, physical assembly scope and grounding
  outcome: supported
  summary: Generic lipid-bilayer constituent intentionally withholds the complete-membrane
    GO term as molecular grounding, retaining REVIEWED_LABEL_ONLY. No exact lipid
    mixture, coat constituent or arbitrary protein inventory is invented.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-component-policy
  - micro-go
- assessment_id: micro-golgi_associated_vesicle_membrane-necessity
  area: evidence
  topic: Formation necessity versus function and boundary identity
  outcome: unknown
  summary: Apparatus machinery has UNKNOWN essentiality. A defining membrane boundary
    is constitutive of the named membrane-bounded class, but this is not evidence
    each lipid species, coatomer subunit or SNARE is individually required for organelle
    assembly. Native annotations and transport-mutant assays are not exhaustive formation
    tests.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-component-policy
  - micro-letourneur1994-meta
  - micro-matsuura2006-pdf
  - micro-protein-P22214
- assessment_id: micro-golgi_associated_vesicle_membrane-graph
  area: graph
  topic: Every current graph node and edge
  outcome: supported
  summary: Five NONMECHANISTIC FUNCTION edges preserve membrane parthood/enclosure,
    both direct COPI and TGN child classes and Golgi-bilayer donation during GO-defined
    evagination. No unique lipid-transfer mechanism, all-vesicles COPI coat or additional
    standalone membrane function is asserted.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-go
  - micro-graph-policy
  - micro-component-policy
  - micro-papanikou2014-bioc
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-serafini1991-quoted
  - micro-letourneur1994-meta
- assessment_id: micro-golgi_associated_vesicle_membrane-coverage
  area: completeness
  topic: Entire maintained scope and optional slots
  outcome: supported
  summary: Entire current file/history/discussions and original observation read.
    No tracked target image, quantitative physical property, trait link or snippet
    asserted. Unresolved exact lipid/family terms are not automatic defects. PROPOSED
    status retained and no historical/group/category issue is terminally disposed.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-prior-golgi_associated_vesicle_membrane
  - micro-policy
- assessment_id: micro-golgi_associated_vesicle_membrane-source-tiers
  area: evidence
  topic: Primary body, abstract and secondary scopes
  outcome: supported
  summary: Losev/Matsuura genuine primary PDF main texts/Methods/captions were read
    independently from shared fresh snapshots, without pixels/movies/supplements.
    Papanikou full main BioC text is secondary review. Letourneur/Waters/Serafini
    and OCH1/SNARE supporting papers are complete primary abstracts only; exact access/assay
    limits retained.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  - micro-papanikou2014-bioc
  - micro-letourneur1994-meta
  - micro-waters1991-meta
  - micro-serafini1991-quoted
  - micro-karhinen2004-meta
  - micro-nakayama1992-meta
  - micro-bruinsma2004-meta
- assessment_id: micro-golgi_associated_vesicle_membrane-native
  area: schema
  topic: Frozen originals and actual native coverage
  outcome: supported
  summary: Original native validate/render passed with byte-identical Markdown, original
    target hash confirmed from frozen revision. Current verify/causal receipts are
    source-head bound; their actual nonempty or zero inventories are explicitly limited,
    not scientific proof.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-prior-golgi_associated_vesicle_membrane
  - micro-original-pairs
  - micro-native-golgi_associated_vesicle_membrane-verify
  - micro-native-golgi_associated_vesicle_membrane-causal
- assessment_id: micro-golgi_associated_vesicle_membrane-adapter-defect
  area: provenance
  topic: Explicit expression-only exclusion is unsupported
  outcome: concern
  summary: Original check is present, not omitted, but excludes applicability because
    no expression-module inference is used. Current named proteins, coatomer/COPI
    retrieval and membrane-budding pathway assertions trigger actual coverage assessment
    under native policy. This is a bundle defect.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-prior-golgi_associated_vesicle_membrane
  - micro-policy
- assessment_id: micro-golgi_associated_vesicle_membrane-adapter-current
  area: evidence
  topic: Current exact-organism catalogue applicability
  outcome: not_applicable
  summary: Complete fresh official catalogue has no Saccharomyces/cerevisiae/S288C
    organism/dataset match. No matched gene/module key or downstream summarize applies;
    an unrelated bacterial proxy would be inappropriate. Historical00:49Z runner limitation
    remains historical.
  target_ids:
  - GO:0030660
  evidence_ids:
  - micro-record-golgi_associated_vesicle_membrane
  - micro-policy
  - micro-datasets
  - micro-historical-runner
- assessment_id: micro-apparatus-stale-refresh
  area: provenance
  topic: Substantive current-record reassessment
  outcome: concern
  summary: Stale input b064dc11 is replaced by assessed current e3df76cd only through
    a new linked observation. Retyping retained SED5/TLG2/SEC22 cohort to a physical
    complex creates F3 despite valid individual examples and native checks; inherited
    F1 attribution also persists. Closed2462 is historical context, not evidence that
    present assembly scope is correct or a whole grouped issue resolution.
  target_ids:
  - GO:0005794
  evidence_ids:
  - micro-stale-delta
  - micro-record-golgi_apparatus
  - micro-prior-golgi_apparatus
  - micro-component-policy
  - micro-protein-P22214
  - micro-protein-Q08144
  - micro-pmid11001058
  - micro-pmid9930650
- assessment_id: septin-glyoxysome-schema
  area: schema
  topic: Original schema/render and frozen input
  outcome: supported
  summary: Original validate/render pass and historical frozen target hash verifies.
    Current glyoxysome is unchanged; scientific claims are independently reassessed.
    Native validity does not itself certify source fidelity.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-original-validation-glyoxysome
- assessment_id: septin-glyoxysome-native-coverage
  area: provenance
  topic: Actual identifier and graph coverage
  outcome: supported
  summary: Zero protein examples, zero represented UniProtKB graph xrefs and zero
    GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory,
    not all narrative pathway claims.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-native-glyoxysome-verify
  - septin-native-glyoxysome-causal
- assessment_id: septin-glyoxysome-nonasserted
  area: scope
  topic: Images, snippets, quantitative traits
  outcome: not_applicable
  summary: No maintained image, quantitative physical-property field, associated trait
    or verbatim snippet is present. Reading scientific text or captions does not constitute
    figure-pixel or raw-data reanalysis.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
- assessment_id: septin-glyoxysome-history
  area: provenance
  topic: History and immutable original observations
  outcome: supported
  summary: Current status/history and original source observations are distinct. No
    record or original bundle was edited; no neighboring or grouped historical issue
    is newly resolved by this review.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-original-glyoxysome
- assessment_id: septin-hydrogenosomal_membrane-schema
  area: schema
  topic: Original schema/render and frozen input
  outcome: supported
  summary: Original validate/render pass and historical frozen target hash verifies.
    Current hydrogenosomal_membrane is unchanged; scientific claims are independently
    reassessed. Native validity does not itself certify source fidelity.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-original-validation-hydrogenosomal_membrane
- assessment_id: septin-hydrogenosomal_membrane-native-coverage
  area: provenance
  topic: Actual identifier and graph coverage
  outcome: supported
  summary: Zero protein examples, zero represented UniProtKB graph xrefs and zero
    GENE_OR_PROTEIN nodes. Exit zero validates the represented empty identifier inventory,
    not all narrative pathway claims.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-native-hydrogenosomal_membrane-verify
  - septin-native-hydrogenosomal_membrane-causal
- assessment_id: septin-hydrogenosomal_membrane-nonasserted
  area: scope
  topic: Images, snippets, quantitative traits
  outcome: not_applicable
  summary: No maintained image, quantitative physical-property field, associated trait
    or verbatim snippet is present. Reading scientific text or captions does not constitute
    figure-pixel or raw-data reanalysis.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
- assessment_id: septin-hydrogenosomal_membrane-history
  area: provenance
  topic: History and immutable original observations
  outcome: supported
  summary: Current status/history and original source observations are distinct. No
    record or original bundle was edited; no neighboring or grouped historical issue
    is newly resolved by this review.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-original-hydrogenosomal_membrane
- assessment_id: septin-hydrogenosome-schema
  area: schema
  topic: Original schema/render and frozen input
  outcome: supported
  summary: Original validate/render pass and historical frozen target hash verifies.
    Current hydrogenosome is stale; its added topology and localization evidence are
    substantively reassessed below. Native validity does not itself certify source
    fidelity.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-original-validation-hydrogenosome
- assessment_id: septin-hydrogenosome-native-coverage
  area: provenance
  topic: Actual identifier and graph coverage
  outcome: supported
  summary: Zero protein examples and three anchored GENE_OR_PROTEIN nodes classified
    NO_GENE_SYMBOLS for import, pyruvate/energy and ISC classes. This is not an empty
    typed-node inventory. No accession-specific membership or necessity is certified.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-native-hydrogenosome-verify
  - septin-native-hydrogenosome-causal
- assessment_id: septin-hydrogenosome-nonasserted
  area: scope
  topic: Images, snippets, quantitative traits
  outcome: not_applicable
  summary: No maintained image, quantitative physical-property field, associated trait
    or verbatim snippet is present. Reading scientific text or captions does not constitute
    figure-pixel or raw-data reanalysis.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
- assessment_id: septin-hydrogenosome-history
  area: provenance
  topic: History and immutable original observations
  outcome: supported
  summary: Current status/history and original source observations are distinct. No
    record or original bundle was edited; no neighboring or grouped historical issue
    is newly resolved by this review.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-original-hydrogenosome
- assessment_id: septin-glyoxysome-adapter
  area: scope
  topic: Positive molecular/pathway assertions and actual dataset applicability
  outcome: supported
  summary: The complete narrative makes glyoxylate-cycle/matrix-import assertions,
    so expression-only exclusion is insufficient. Fresh official catalogue has no
    relevant eukaryotic host coverage; downstream queries are not applicable for this
    bounded catalogue. No heterologous bacterial-host substitution, threshold-as-absence
    or fresh runner invocation.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-hydrogenosomal_membrane-adapter
  area: scope
  topic: Positive molecular/pathway assertions and actual dataset applicability
  outcome: supported
  summary: The complete narrative makes membrane-boundary and anaerobic metabolic-enzyme
    assertions, so expression-only exclusion is insufficient. Fresh official catalogue
    has no relevant eukaryotic host coverage; downstream queries are not applicable
    for this bounded catalogue. No heterologous bacterial-host substitution, threshold-as-absence
    or fresh runner invocation.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-hydrogenosome-adapter
  area: scope
  topic: Positive molecular/pathway assertions and actual dataset applicability
  outcome: supported
  summary: The complete narrative makes anaerobic metabolic-enzyme/protein-import/ISC
    assertions, so expression-only exclusion is insufficient. Fresh official catalogue
    has no relevant eukaryotic host coverage; downstream queries are not applicable
    for this bounded catalogue. No heterologous bacterial-host substitution, threshold-as-absence
    or fresh runner invocation.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-glyoxysome-identity
  area: identity
  topic: Exact organelle identity and boundaries
  outcome: supported
  summary: GO0009514/peroxisome ancestry and separate membrane/lumen identities agree
    with current authorities and frozen neighbors. Plant-seed emphasis in GO does
    not prevent the explicitly primary-supported Neurospora case; broad exact identity
    is not inferred from a protein.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-go
  - septin-ancestors-0009514
  - septin-SL-0131
  - septin-context-glyoxysomal_lumen
  - septin-context-glyoxysomal_membrane
- assessment_id: septin-glyoxysome-taxon
  area: scope
  topic: Fungal occurrence and canonical context
  outcome: supported
  summary: Neurospora crassa identity is verified. deZoysa1994 directly supports nutritionally
    acetate-induced fungal glyoxysomes and targeted CAT reporters. COMMON and canonical
    are context-qualified, not all-media frequency measurements; plant/catalase authority
    prose is not transferred to this fungus.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-tax5141
  - septin-dezoysa1994-meta
  - septin-SL-0131
- assessment_id: septin-glyoxysome-lipid
  area: grounding
  topic: Whole membrane versus molecular lipid identity
  outcome: concern
  summary: 'Inherited F1 remains: LIPID glyoxysomal_membrane is grounded to complete
    GO0046861 and propagated through a component_ref. Supported bilayer topology does
    not make this chemical identity exact; molecular material can remain explicitly
    label-only if exact composition is unsupported.'
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-glyoxysome-function
  area: evidence
  topic: Glyoxylate-cycle compartment and matrix import
  outcome: supported
  summary: Current primary abstract supports glyoxylate-cycle-enzyme-containing microbodies
    and C-terminal reporter targeting under defined nutrient induction. This is not
    proof of exclusive localization of every glyoxylate-cycle reaction, complete enzyme
    inventory, all possible targeting motifs or a directly imaged translocation mechanism.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-dezoysa1994-meta
  - septin-go
- assessment_id: septin-glyoxysome-graph
  area: graph
  topic: Descriptive topology and cycle-support graph
  outcome: concern
  summary: The three NONMECHANISTIC relations are supported descriptive membrane/lumen/cycle
    context; the inherited molecular-to-whole-membrane component_ref mismatch remains
    F1. No perturbation mechanism or enzyme-formation necessity is inferred.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-graph-policy
  - septin-go
  - septin-dezoysa1994-meta
  - septin-curation-policy
- assessment_id: septin-glyoxysome-necessity
  area: evidence
  topic: Boundary essentiality and optional functional inventory
  outcome: supported
  summary: A bounding membrane is definitionally part of the organelle; source-supported
    material representation must be corrected independently. Excluding optional matrix
    enzyme examples from a structural inventory does not assert that enzymes are absent
    or globally prohibit class components. No enzyme knockout/formation claim is made.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-curation-policy
  - septin-protein-policy
  - septin-dezoysa1994-meta
- assessment_id: septin-glyoxysome-sources
  area: provenance
  topic: Actual literature tier and bibliography
  outcome: supported
  summary: deZoysa identity and complete abstract are current; full publisher PDF
    is inaccessible and old full-body assertions are not relabeled as freshly inspected.
    The currently claimed fungal induction/import/compartment scope fits the abstract.
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-dezoysa1994-meta
  - septin-source-access-limits
- assessment_id: septin-hydrogenosomal_membrane-identity
  area: identity
  topic: Membrane identity and organelle relation
  outcome: supported
  summary: GO0046859 and exact SL0144 match; GO0016020 is a valid broad is_a ancestor.
    Complete membrane part_of hydrogenosome and lumen enclosure are distinct from
    whole-organelle identity; synonyms and boundaries agree.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-go
  - septin-ancestors-0046859
  - septin-SL-0144
  - septin-SL-0335
  - septin-context-hydrogenosome_lumen
- assessment_id: septin-hydrogenosomal_membrane-taxon
  area: scope
  topic: Patchy eukaryotic distribution and T.vaginalis case
  outcome: supported
  summary: ENA verifies Eukaryota and T.vaginalis. Broad rare occurrence is qualitative
    patchiness; the canonical mechanistic case is T.vaginalis, not all eukaryotes.
    Authority/review syntheses are not quantitative prevalence experiments.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-tax2759
  - septin-tax5722
  - septin-SL-0145
  - septin-tachezy2022-meta
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosomal_membrane-material
  area: grounding
  topic: Label-only bilayer lipid material
  outcome: supported
  summary: This record explicitly avoids using whole GO0046859 as molecular grounding.
    Generic bilayer lipid material can remain label-only; neither current source nor
    schema justifies inventing exact lipid species/ratios. Its constitutional boundary
    role does not require every candidate import protein for formation.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-curation-policy
  - septin-schema-policy
  - septin-go
- assessment_id: septin-hydrogenosomal_membrane-function
  area: evidence
  topic: Matrix boundary and anaerobic enzyme compartment
  outcome: supported
  summary: The membrane bounds the hydrogenosomal matrix supporting anaerobic metabolic
    machinery. Schneider primary fractionation/proteome and organelle authorities
    support this context; no fixed membrane proteome, complete transport system or
    universal lipid composition is claimed.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-schneider2011-bioc
  - septin-SL-0144
  - septin-SL-0335
- assessment_id: septin-hydrogenosomal_membrane-graph
  area: graph
  topic: Two descriptive boundary relations
  outcome: supported
  summary: NONMECHANISTIC membrane part_of whole and lumen enclosed_by membrane are
    supported. Material component correspondence remains distinct from whole membrane
    identity; no mechanistic perturbation or all-lineage necessity is inferred.
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-graph-policy
  - septin-go
  - septin-context-hydrogenosome_lumen
- assessment_id: septin-hydrogenosomal_membrane-citation
  area: provenance
  topic: Tachezy2022 title fidelity
  outcome: concern
  summary: 'Inherited F1 remains: DOIjeu.12922 is The hydrogenosome of Trichomonas
    vaginalis, not Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes.
    Correct DOI and broad relevance do not repair the wrong title; source remains
    secondary.'
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-tachezy2022-meta
- assessment_id: septin-hydrogenosome-identity
  area: identity
  topic: Whole organelle identity, topology and stale parthood
  outcome: supported
  summary: GO0042566 whole organelle is distinct from its membrane and GO0034492 lumen.
    Current added lumen part_of relation agrees with current authority and frozen
    lumen neighbor. GO says membrane enclosure; interpreting the matrix as inside
    the inner membrane is biological context, not a quoted GO phrase.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-go
  - septin-ancestors-0042566
  - septin-SL-0145
  - septin-SL-0335
  - septin-context-hydrogenosome_lumen
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosome-taxon
  area: scope
  topic: Experimental species and qualitative occurrence
  outcome: supported
  summary: T.vaginalis current primary studies support the canonical case, while Lindmark1973
    concerns Tritrichomonas foetus and is currently metadata-only. Broad Eukaryota
    RARE is patchy, not measured prevalence. Other hydrogenosome lineages need not
    share every T.vaginalis genomic/metabolic property.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-tax5722
  - septin-tax2759
  - septin-SL-0145
  - septin-lindmark1973-meta
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosome-lipid
  area: grounding
  topic: Whole membrane used as lipid component identity
  outcome: concern
  summary: 'Inherited F1 remains: GO0046859 is the assembled membrane and cannot be
    exact molecular grounding for LIPID. Correct has_part/topology must be preserved
    while correcting molecular material and graph component_ref.'
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-hydrogenosome-classes
  area: scope
  topic: Heterogeneous protein classes and incomplete inventories
  outcome: supported
  summary: Energy, ISC and import entries are explicitly broad functional/localization
    classes with UNKNOWN essentiality, not one family or asserted fixed complex. Native
    family-or-class guidance permits this scope. Zero examples and three NO_GENE_SYMBOLS
    nodes remain explicit; no unsupported precise family, complex, accession or formation
    necessity is added.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-curation-policy
  - septin-protein-policy
  - septin-native-hydrogenosome-causal
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosome-energy
  area: evidence
  topic: Pyruvate-linked ATP and hydrogen production
  outcome: supported
  summary: Current Schneider main text supports PFO/ferredoxin/hydrogenase and substrate-level-phosphorylation
    machinery in T.vaginalis hydrogenosomes. Lindmark bibliography is verified but
    its original assay body is not freshly accessed. Functional pathway support is
    not a measured universal stoichiometry or requirement for organelle formation.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-schneider2011-bioc
  - septin-lindmark1973-meta
- assessment_id: septin-hydrogenosome-isc
  area: evidence
  topic: ISC activity and member-specific localization
  outcome: concern
  summary: Sutak directly localizes TvIscS-2 and measures lysate-dependent FeS reconstitution.
    Schneider later detects IscU in the hydrogenosomal proteome, with fractionation/contamination
    limits. The new edge note overattributes demonstrated lumenal IscS/IscU localization
    to Sutak alone; retain pathway support and narrow that source claim.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-sutak2004-maintext
  - septin-sutak2004-meta
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosome-import
  area: evidence
  topic: Presequences, internal signals and reporter scope
  outcome: concern
  summary: 'Inherited F3 remains: N-terminal targeting is one demonstrated route,
    not an unqualified requirement. Dolezal heterologous GiIscS fragments target T.vaginalis
    hydrogenosomes without an N-terminal presequence; Schneider3.8 confirms internal/presequence-independent
    possibilities while retaining stringent motif prediction as an alternative. Bui
    Hsp60 processing is a particular example.'
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-dolezal2005-indexed-maintext
  - septin-schneider2011-bioc
  - septin-bui1996-meta
- assessment_id: septin-hydrogenosome-graph
  area: graph
  topic: Mechanistic synthesis versus specific assays
  outcome: concern
  summary: The nine edges combine supported topology, energy/ISC pathway and import
    contexts. Dolezal reporters do not independently test every native pyruvate enzyme
    cargo; Schneider supplies cohort/fraction context. Inherited membrane correspondence
    and new Sutak attribution defects are scoped findings. The new lumen parthood
    is supported, and no IscU absence or wholesale pathway rejection follows.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-graph-policy
  - septin-go
  - septin-dolezal2005-indexed-maintext
  - septin-sutak2004-maintext
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosome-necessity
  area: evidence
  topic: Formation necessity and operational function
  outcome: supported
  summary: Generic protein classes retain UNKNOWN essentiality. Biochemical activity,
    reporter import and fraction localization do not establish organelle-formation
    necessity of each class/member. Constitutional membrane requirement is separate
    from wrong lipid grounding.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-curation-policy
  - septin-sutak2004-maintext
  - septin-dolezal2005-indexed-maintext
  - septin-schneider2011-bioc
- assessment_id: septin-hydrogenosome-citation
  area: provenance
  topic: Tachezy bibliographic identity and source tiers
  outcome: concern
  summary: Inherited F2 wrong Tachezy title remains. Bui and deZoysa are current primary
    abstract tiers; Lindmark metadata only; Tachezy secondary abstract; Schneider
    selected genuine body sections; Sutak rendered main text; Dolezal detailed indexed
    main text. No failed route is promoted to full-body access.
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-tachezy2022-meta
  - septin-bui1996-meta
  - septin-lindmark1973-meta
  - septin-source-access-limits
  - septin-sutak2004-maintext
  - septin-dolezal2005-indexed-maintext
  - septin-schneider2011-bioc
- assessment_id: septin-glyoxysome-verdict
  area: completeness
  topic: Current scoped verdict and unresolved curation
  outcome: concern
  summary: 'needs_curation: 1 confirmed finding(s) remain for this maintained record.
    Original lineage is preserved; new hydrogenosome attribution is independently
    supported and has no predecessor. Bundle applicability corrections and stale refresh
    do not silently curate the record or resolve neighbors.'
  target_ids:
  - GO:0009514
  evidence_ids:
  - septin-record-glyoxysome
  - septin-original-glyoxysome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-hydrogenosomal_membrane-verdict
  area: completeness
  topic: Current scoped verdict and unresolved curation
  outcome: concern
  summary: 'needs_curation: 1 confirmed finding(s) remain for this maintained record.
    Original lineage is preserved; new hydrogenosome attribution is independently
    supported and has no predecessor. Bundle applicability corrections and stale refresh
    do not silently curate the record or resolve neighbors.'
  target_ids:
  - GO:0046859
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-original-hydrogenosomal_membrane
  - septin-tachezy2022-meta
- assessment_id: septin-hydrogenosome-verdict
  area: completeness
  topic: Current scoped verdict and unresolved curation
  outcome: concern
  summary: 'needs_curation: 4 confirmed finding(s) remain for this maintained record.
    Original lineage is preserved; new hydrogenosome attribution is independently
    supported and has no predecessor. Bundle applicability corrections and stale refresh
    do not silently curate the record or resolve neighbors.'
  target_ids:
  - GO:0042566
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-original-hydrogenosome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
  - septin-tachezy2022-meta
  - septin-dolezal2005-indexed-maintext
  - septin-schneider2011-bioc
  - septin-bui1996-meta
  - septin-sutak2004-maintext
  - septin-sutak2004-meta
  - septin-graph-policy
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0009514
  - GO:0005794
  - GO:0005798
  - GO:0030660
  - GO:0031985
  - GO:0032580
  - GO:0005796
  - GO:0000139
  - GO:0046859
  - GO:0042566
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
  issue_key: golgi-cisterna-whole-compartment-lipid-component-ref
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Remove the whole-cisterna correspondence to its lipid component
  description: The graph node golgi_cisterna denotes the complete membrane-bounded
    compartment GO0031985 but component_ref points to golgi_cisternal_lipid_bilayer.
    That component denotes boundary lipid material, while the separate golgi_cisterna_membrane
    node already denotes the correct GO0032580 boundary. The schema defines component_ref
    as identifying a node that is one of the record’s components, so this join incorrectly
    equates whole compartment and lipid constituent.
  target_ids:
  - GO:0031985
  field_paths:
  - causal_graphs#golgi_cisterna_maturation.nodes#golgi_cisterna.component_ref
  evidence_ids:
  - plaque-current-4
  - plaque-schema-policy
  - plaque-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_cisterna.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact grounding and component
    identity
  native_severity: major
  normalization_reason: 'Major bounded identity correspondence error: the graph formally
    identifies a whole compartment with one material constituent. Its biological edge
    descriptions and the cisternal-maturation evidence are supported; no incorrect
    maturation mechanism is alleged.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015631Z-golgi-cisterna-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2704
- finding_id: micro-F1
  issue_key: golgi-apparatus-snare-review-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the source attribution for SNARE pairing and cycling
  description: The component note, graph-edge note and discussion attribute SNARE
    pairing/cycling to Papanikou and Glick2014. Its complete main text reviews compartment
    traffic, coats, tethers and GTPases but does not supply those SNARE-specific statements.
    Native SED5/TLG2/SEC22 entries and the already cited imaging papers support relevant
    SNARE context, so this is a bounded source-placement problem rather than a claim
    that these proteins have no Golgi role.
  target_ids:
  - GO:0005794
  field_paths:
  - components#golgi_snare_trafficking_machinery.evidence
  - causal_graphs#yeast_golgi_cisternal_maturation.edges
  - discussions#ground_golgi_resident_machinery.evidence
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-prior-golgi_apparatus
  - micro-papanikou2014-bioc
  - micro-snare-attribution-search
  - micro-protein-Q01590
  - micro-protein-Q08144
  - micro-protein-P22214
  - micro-losev2006-pdf
  - micro-matsuura2006-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level source support
  native_severity: minor
  normalization_reason: Bounded incorrect source attribution; organelle identity,
    observed yeast maturation and native protein identities remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015625Z-golgi-apparatus-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2705
- finding_id: micro-F2
  issue_key: golgi-associated-vesicle-membrane-molecular-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the complete vesicle membrane from molecular lipid identity
  description: The golgi_associated_vesicle_membrane component is typed LIPID and
    grounded to GO0030660, which identifies the complete assembled membrane surrounding
    the vesicle. The frozen schema defines StructuralComponent as a molecular building
    block and distinguishes lipid chemical identity from substructure identity. The
    graph correctly calls this object STRUCTURE but repeats the molecular correspondence
    through component_ref. Correct has_part and topology do not resolve that mismatch.
  target_ids:
  - GO:0005798
  field_paths:
  - components#golgi_associated_vesicle_membrane
  - causal_graphs#golgi_associated_vesicle_topology.nodes#golgi_associated_vesicle_membrane.component_ref
  evidence_ids:
  - micro-record-golgi_associated_vesicle
  - micro-prior-golgi_associated_vesicle
  - micro-component-policy
  - micro-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact grounding and component
    identity
  native_severity: major
  normalization_reason: Major because an asserted molecular lipid constituent is grounded
    to a different complete structure and its graph correspondence propagates that
    identity mismatch. The whole-vesicle identity, subtype scope and biological topology
    remain valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015627Z-golgi-associated-vesicle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2706
- finding_id: micro-F3
  issue_key: golgi-apparatus-snare-cohort-complex-conflation
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Keep the broad Golgi SNARE cohort distinct from a defined Sed5 complex
  description: The stale delta retypes the unchanged SED5/TLG2/SEC22 cohort as PROTEIN_COMPLEX
    and calls it a Sed5-containing cis-Golgi complex in history, while its current
    label and grounding notes still describe general Golgi trafficking machinery.
    Fresh native SEC22 and primary Parlati2000/Mossessova2003 abstracts identify Sed5/Bos1/Bet1/Sec22
    or Sed5/Bos1/Sec22 fusion assemblies; Tlg2 has a distinct late-Golgi/endosome
    role and Tlg1/Tlg2/Vps45 association in Nichols1998. This does not support one
    named subcomplex encompassing the retained cohort. Individual accessions remain
    correct. Native policy permits generic protein classes, so the concern is unsupported
    physical-complex scope, not mere heterogeneity or a requirement to invent an exact
    family. GENE_OR_PROTEIN is explicitly legal for complexes and is not a separate
    node-type defect.
  target_ids:
  - GO:0005794
  field_paths:
  - components#golgi_snare_trafficking_machinery.component_type
  - components#golgi_snare_trafficking_machinery.grounding_notes
  - components#golgi_snare_trafficking_machinery.gene_symbols
  - components#golgi_snare_trafficking_machinery.protein_examples
  evidence_ids:
  - micro-record-golgi_apparatus
  - micro-stale-delta
  - micro-component-policy
  - micro-protein-Q01590
  - micro-protein-Q08144
  - micro-protein-P22214
  - micro-pmid11001058
  - micro-pmid9930650
  - micro-pmid12941276
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; StructuralComponent/ComponentTypeEnum; review-yaml-record
    exact scope
  native_severity: major
  normalization_reason: Major because the changed field promotes a multi-route protein
    cohort into a physical subcomplex identity unsupported by its retained participants
    and inspected source scopes. It is bounded to the machinery row, not the whole
    organelle identity.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2707
- finding_id: septin-glyoxysome-F1
  issue_key: glyoxysome-lipid-whole-membrane-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the complete membrane identity from its molecular lipid constituent
  description: The glyoxysomal_membrane component is typed LIPID but grounded to GO:0046861,
    which identifies the complete organelle membrane. The schema requires a molecular
    building block and chemical grounding for a lipid, while GO can identify a sub-complex.
    Correct membrane parthood and bilayer topology do not make the entire membrane
    term an exact lipid molecular identity. The graph component_ref propagates this
    mismatch.
  target_ids:
  - GO:0009514
  field_paths:
  - components#glyoxysomal_membrane.component_type
  - components#glyoxysomal_membrane.grounding
  - causal_graphs#glyoxysome_glyoxylate_cycle_compartment.nodes#glyoxysomal_membrane.component_ref
  evidence_ids:
  - septin-record-glyoxysome
  - septin-original-glyoxysome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glyoxysome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity, scoped evidence
    and severity rubric
  native_severity: major
  normalization_reason: Major because a molecular component is assigned a distinct
    complete-structure identity and the mismatch propagates into its graph correspondence.
    This does not make the accepted whole-organelle identity or membrane topology
    wrong.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015623Z-glyoxysome-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2708
- finding_id: septin-hydrogenosomal_membrane-F1
  issue_key: hydrogenosomal-membrane-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title of the cited Tachezy2022 review
  description: 'DOI:10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas
    vaginalis by Tachezy, Makki and Hrdý, not the title Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes recorded in evidence.notes. The DOI and broad
    scientific relevance remain correct.'
  target_ids:
  - GO:0046859
  field_paths:
  - evidence[reference=DOI:10.1111/jeu.12922].notes
  evidence_ids:
  - septin-record-hydrogenosomal_membrane
  - septin-original-hydrogenosomal_membrane
  - septin-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity, scoped evidence
    and severity rubric
  native_severity: minor
  normalization_reason: 'Minor bibliographic provenance error: the resolvable source
    identifier and relevant organelle topic are correct; no wrong organelle identity
    follows from the title correction.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015639Z-hydrogenosomal-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2709
- finding_id: septin-hydrogenosome-F1
  issue_key: hydrogenosome-lipid-whole-membrane-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the complete membrane identity from its molecular lipid constituent
  description: The hydrogenosomal_membrane component is typed LIPID but grounded to
    GO:0046859, which identifies the complete organelle membrane. The schema requires
    a molecular building block and chemical grounding for a lipid, while GO can identify
    a sub-complex. Correct membrane parthood and bilayer topology do not make the
    entire membrane term an exact lipid molecular identity. The graph component_ref
    propagates this mismatch.
  target_ids:
  - GO:0042566
  field_paths:
  - components#hydrogenosomal_membrane.component_type
  - components#hydrogenosomal_membrane.grounding
  - causal_graphs#hydrogenosomal_pyruvate_to_atp_and_hydrogen.nodes#hydrogenosomal_membrane.component_ref
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-original-hydrogenosome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity, scoped evidence
    and severity rubric
  native_severity: major
  normalization_reason: Major because a molecular component is assigned a distinct
    complete-structure identity and the mismatch propagates into its graph correspondence.
    This does not make the accepted whole-organelle identity or membrane topology
    wrong.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015641Z-hydrogenosome-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2710
- finding_id: septin-hydrogenosome-F2
  issue_key: hydrogenosome-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title of the cited Tachezy2022 review
  description: 'DOI:10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas
    vaginalis by Tachezy, Makki and Hrdý, not the title Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes recorded in evidence.notes. The DOI and broad
    scientific relevance remain correct.'
  target_ids:
  - GO:0042566
  field_paths:
  - evidence[reference=DOI:10.1111/jeu.12922].notes
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-original-hydrogenosome
  - septin-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity, scoped evidence
    and severity rubric
  native_severity: minor
  normalization_reason: 'Minor bibliographic provenance error: the resolvable source
    identifier and relevant organelle topic are correct; no wrong organelle identity
    follows from the title correction.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015641Z-hydrogenosome-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2711
- finding_id: septin-hydrogenosome-F3
  issue_key: hydrogenosome-import-route-qualification
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify N-terminal presequence targeting as one demonstrated import route
  description: The matrix-import function says nuclear-encoded matrix proteins are
    targeted through N-terminal presequences without qualification. Its cited Dolezal2005
    paper demonstrates internal targeting signals in GiIscS expressed in T. vaginalis
    as well as N-terminal targeting; Schneider2011 §3.8 also states that targeting
    without an N-terminal presequence has been demonstrated. The evidence supports
    the route but not an unqualified common requirement.
  target_ids:
  - GO:0042566
  field_paths:
  - functions#hydrogenosomal_protein_import.description
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-original-hydrogenosome
  - septin-dolezal2005-indexed-maintext
  - septin-schneider2011-bioc
  - septin-bui1996-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity, scoped evidence
    and severity rubric
  native_severity: minor
  normalization_reason: 'Minor scope/wording overgeneralization within an otherwise
    supported import function: the named route is experimentally real and the record
    does not explicitly deny alternatives, but the unqualified formulation omits alternatives
    demonstrated by its own source.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T015641Z-hydrogenosome-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2712
- finding_id: septin-hydrogenosome-F4
  issue_key: hydrogenosome-sutak-iscu-localization-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Narrow the new Sutak2004 localization attribution to the measured ISC member
  description: The newly added localization edge describes IscS/IscU machinery and
    its Sutak2004 evidence note says the paper demonstrated lumenal IscS/IscU machinery.
    Sutak directly assays TvIscS-2 hydrogenosomal fractionation/immunolocalization
    and lysate-dependent FeS reconstitution; IscU appears in yeast/bacterial model/interaction
    context, not a native T.vaginalis IscU localization experiment. Schneider2011
    later detects IscU in a hydrogenosomal proteome, but fraction detection is not
    the same source or a separate precise lumenal localization assay. General ISC
    biology remains supported; the defect is this source-specific overattribution,
    not evidence that IscU is absent.
  target_ids:
  - GO:0042566
  field_paths:
  - causal_graphs#hydrogenosomal_pyruvate_to_atp_and_hydrogen.edges[subject=hydrogenosomal_fe_s_machinery,predicate=localizes
    to,object=hydrogenosome_lumen].description
  - causal_graphs#hydrogenosomal_pyruvate_to_atp_and_hydrogen.edges[subject=hydrogenosomal_fe_s_machinery,predicate=localizes
    to,object=hydrogenosome_lumen].evidence[reference=DOI:10.1073/pnas.0401319101].notes
  evidence_ids:
  - septin-record-hydrogenosome
  - septin-sutak2004-maintext
  - septin-sutak2004-meta
  - septin-schneider2011-bioc
  - septin-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level source fidelity
    and severity rubric
  native_severity: minor
  normalization_reason: Minor source-attribution overscope in an otherwise supported
    ISC localization/pathway context. The finding does not reject the organelle identity,
    ISC activity or possible IscU localization.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2713
actions:
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0031985
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_cisterna.yaml
    role: maintained scientific record
  description: In separately authorized curation, remove the lipid component_ref from
    the whole-cisterna node and, if justified by the existing material model, associate
    the bilayer component only with the membrane-boundary node. Preserve the cisterna
    identity, native membrane grounding and source-supported maturation/topology edges.
  acceptance_checks:
  - Verify that each component_ref denotes the same object as its component and does
    not equate a whole compartment with lipid material.
  - Preserve supported native hierarchy, subtype and primary-source experimental scope.
  - Run focused schema, strict and graph/product checks after separately authorized
    scientific curation.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0005794
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
  description: In separately authorized curation, remove the inaccurate Papanikou-specific
    SNARE wording and attach directly inspected evidence to the exact SNARE traffic
    or maturation assertion, or narrow that assertion to the support actually available.
    Retain broad machinery scope and avoid implying that all three examples form one
    complex.
  acceptance_checks:
  - Re-read each revised source at the exact component/edge/discussion placement.
  - Preserve the directly observed yeast marker-maturation scope and reference-strain
    identity distinction.
  - Run focused schema, strict and relevant native graph/protein checks after curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0005798
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_associated_vesicle.yaml
    role: maintained scientific record
  description: In separately authorized curation, keep the complete membrane in has_part
    and as the grounded graph structure, and remove its molecular component_ref if
    removing the whole-membrane component. Any replacement lipid material must have
    source-supported identity and justified chemical or reviewed-label-only grounding;
    do not invent a lipid mixture.
  acceptance_checks:
  - Verify that each component_ref denotes the same object as its component and does
    not equate a whole compartment with lipid material.
  - Preserve supported native hierarchy, subtype and primary-source experimental scope.
  - Run focused schema, strict and graph/product checks after separately authorized
    scientific curation.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0005794
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/golgi_apparatus.yaml
    role: maintained scientific record
  description: In separately authorized curation, explicitly retain a source-supported
    generic protein-class cohort under the native family-or-class policy, or split/narrow
    it to independently supported named assemblies with matching participants and
    evidence. Do not automatically force every broad cohort into PROTEIN_COMPLEX,
    impose an exhaustive subunit inventory, or infer Tlg2 never interacts with other
    SNAREs. Preserve correct individual accessions and immutable historical events;
    append a new curation/history event.
  acceptance_checks:
  - The component label, type, scope, gene/examples and evidence denote the same generic
    class or exact physical assembly.
  - Verify chosen assembly participants against directly inspected sources; explain
    treatment of Tlg2 separately from a Sed5/Bos1/Bet1/Sec22 identity.
  - Run native focused schema/strict, graph/protein and relevant product checks after
    authorized curation.
- action_id: septin-glyoxysome-A1
  finding_ids:
  - septin-glyoxysome-F1
  target_ids:
  - GO:0009514
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glyoxysome.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, preserve the complete membrane
    in structural parthood/topology and represent only source-supported lipid material
    in the component row, with exact chemical grounding if justified or an explicitly
    reviewed label-only material; correct the graph component_ref correspondence.
  acceptance_checks:
  - Do not use the complete membrane GO term as chemical lipid identity or invent
    an exact lipid mixture.
  - Preserve correct organelle identity, has_part, membrane STRUCTURE node and supported
    topology; any component_ref must denote the actual molecular component.
  - Run focused schema, grounding/product and graph checks after separately authorized
    curation.
- action_id: septin-hydrogenosomal_membrane-A1
  finding_ids:
  - septin-hydrogenosomal_membrane-F1
  target_ids:
  - GO:0046859
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, replace the incorrect citation
    title and author attribution with the exact native bibliographic identity while
    retaining the correct DOI and review evidence tier.
  acceptance_checks:
  - Verify DOI, exact title, three authors, year2022 and Journal of Eukaryotic Microbiology
    against the native metadata.
  - Do not replace the correct DOI, claim that this review is a primary experiment,
    or generalize its T. vaginalis focus solely from the incorrect broad title.
- action_id: septin-hydrogenosome-A1
  finding_ids:
  - septin-hydrogenosome-F1
  target_ids:
  - GO:0042566
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, preserve the complete membrane
    in structural parthood/topology and represent only source-supported lipid material
    in the component row, with exact chemical grounding if justified or an explicitly
    reviewed label-only material; correct the graph component_ref correspondence.
  acceptance_checks:
  - Do not use the complete membrane GO term as chemical lipid identity or invent
    an exact lipid mixture.
  - Preserve correct organelle identity, has_part, membrane STRUCTURE node and supported
    topology; any component_ref must denote the actual molecular component.
  - Run focused schema, grounding/product and graph checks after separately authorized
    curation.
- action_id: septin-hydrogenosome-A2
  finding_ids:
  - septin-hydrogenosome-F2
  target_ids:
  - GO:0042566
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, replace the incorrect citation
    title and author attribution with the exact native bibliographic identity while
    retaining the correct DOI and review evidence tier.
  acceptance_checks:
  - Verify DOI, exact title, three authors, year2022 and Journal of Eukaryotic Microbiology
    against the native metadata.
  - Do not replace the correct DOI, claim that this review is a primary experiment,
    or generalize its T. vaginalis focus solely from the incorrect broad title.
- action_id: septin-hydrogenosome-A3
  finding_ids:
  - septin-hydrogenosome-F3
  target_ids:
  - GO:0042566
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, qualify the function to
    state that some matrix proteins use N-terminal presequences and that internal/presequence-independent
    targeting also occurs; retain the supported import machinery and generic import
    pathway.
  acceptance_checks:
  - Bind the qualification to the actual Dolezal Results and retain the heterologous-reporter
    context.
  - Do not infer that all proteins lacking a predicted motif lack a targeting signal;
    Schneider explicitly gives stringent prediction as an alternative.
  - Do not remove the validated N-terminal route or convert import activity into organelle-assembly
    necessity.
- action_id: septin-hydrogenosome-A4
  finding_ids:
  - septin-hydrogenosome-F4
  target_ids:
  - GO:0042566
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosome.yaml
    role: maintained scientific record
  description: In separately authorized record curation, narrow the Sutak2004 note
    to the directly measured TvIscS-2 localization and lysate activity, or add an
    appropriate later member-specific source with its actual fraction/subcompartment
    scope. Keep the edge description and source note consistent without discarding
    supported ISC biology.
  acceptance_checks:
  - Check the actual Sutak Methods, Results and Discussion; distinguish TvIscS-2 immunolocalization
    from yeast/bacterial IscU context.
  - If retaining IscU, cite its actual evidence and preserve proteomic fraction versus
    direct lumen-localization limitations.
  - Do not infer IscU absence, invent a new accession or delete the supported pathway
    merely because this source attribution is too broad.
  - Run focused schema and relevant graph/source checks after separately authorized
    curation.
limitations:
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Four
  assigned targets only, unchanged from original inputs. One inherited major cisterna
  F1 remains open with exact key, severity and repository-review-finding lineage.
  Other three qualified passes. No new scientific finding, scientific record curation
  or terminal neighbor/group/category disposition.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Losev
  primary PDF: scientific main pp1002–1005, Methods and Figure1–4 captions. Matsuura-Tokita
  PDF: main pp1007–1009, Methods continuation p1010 and Figure1–4 captions. No figure
  pixels, movies, supplements or raw microscopy reanalysis. Strain constructions and
  overexpression/temperature details remain source-bounded; yeast observations do
  not establish universal kinetics or exclusive cargo routes.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Dean1997
  PMID9395539, Serafini1991 PMID1680566 and Bremser1999 PMID10052452 are primary complete-abstract
  evidence only. Publisher DOI routes for Dean/Serafini yielded short meta-refresh
  landings, not body. Mammalian ARF/COPI and liposome reconstitution contexts are
  not silently converted to yeast experiments or coat-alone sufficiency.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Papanikou2014
  secondary review JATS sections S1, S3, S4, S5 were independently inspected; other
  sections and images not certified. This retains unresolved recycling direction,
  cargo and compartment differences rather than claiming a unique complete maturation
  mechanism.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Current
  GO0032580 is_a ancestry lacks0000139; the generic parent is supported by membrane-of-Golgi-compartment
  definitions, not advertised as a direct native GO assertion. GO/SL topology does
  not experimentally establish molecular necessity.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: All
  four targets have empty protein_examples and zero typed GENE_OR_PROTEIN nodes; all
  eight actual native commands pass in that scope. Explicit maturation, VRG4/GDP-mannose
  glycosylation and COPI budding narratives still trigger structured-source assessment.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Fresh
  complete official catalogue contains no S. cerevisiae host; no matched gene/module
  queries or unrelated-host proxies apply. Noncoverage is not biological absence.
  Historical runner00:49Z PermissionError remains unavailable; no new runner invocation
  or successful adapter execution claimed. Initial unquoted Serafini DOI miss was
  corrected by quoted DOI lookup and not treated as article absence.'
- 'Golgi cisterna, cisterna membrane, lumen and membrane independent subreview: Root
  owns global QC, issues and publication. Read-only source reviewer made no repository/GitHub/record
  writes. Scratch native preflight validates report shape, not independent proof of
  every biological claim. Existing unrelated cis-Golgi/coated-vesicle issues remain
  outside this slice.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: Assigned
  Golgi slice: three whole records, original observations and every current edge assessed.
  One stale apparatus substantively refreshed. Two original request-curation findings
  persist with exact repository/review/F1 lineages; one new changed-record assembly-scope
  finding has no invented predecessor. Closed2462/group/category history is not resolved
  or reopened by this report.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: Primary
  imaging scope: shared fresh Losev2006 mainpp1002-1005/Methods/captions and Matsuura2006
  mainpp1007-1009 plus Methods continuation1010/captions read independently. No figure
  pixels, movies, supplements or raw data. Marker transitions do not uniquely establish
  cargo retention, all recycling routes or a complete molecular determinant set.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: Papanikou2014
  is secondary review; official NCBI BioC main passages2-33 and captions150-151 genuinely
  read after PMC canonical/numeric challenge and EPMC500. BioC author-manuscript front
  metadata year differs from exact MED2014 bibliography; no scientific content date
  substitution. No underlying primary dataset reanalysis.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: Other source
  scope: Letourneur1994,Waters1991,Serafini1991,Karhinen2004,Nakayama1992,Bruinsma2004,Parlati2000,Nichols1998,McNew1998,Mossessova2003
  complete primary abstracts only. Publisher Letourneur403 response is not a body.
  No absence of all possible SNARE interactions inferred; finding concerns exact retained
  physical-complex scope.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: Native protein
  scope: six apparatus reviewed S288C examples and two COVERED nodes; other two records
  empty protein inventories and zero typed nodes. Generic successful verify output
  is not independently sufficient to infer inventory size or biology. Native CausalNode
  explicitly permits complexes as GENE_OR_PROTEIN.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: All three
  original applicability rows are explicit unsupported expression-only exclusions.
  Fresh full official catalogue has no matching Saccharomyces dataset, so downstream
  searches are inapplicable; no biological absence or unmatched proxy. Runner failure
  is actual historical00:49Z, not new execution. Root globalQC/finalCI remain independently
  owned and are not borrowed into this source report.'
- 'Golgi apparatus and associated vesicle/membrane independent subreview: Review-only:
  no record, repository, Git or GitHub mutation. Exact local instructions/config/schema
  bytes frozen before use; script bytes participate in actual native checks, not a
  claimed full implementation audit. Scientific curation actions remain proposed and
  require later owner changes.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: Read-only source review
  of three assigned records at exact source head. Root owns all repository/GitHub
  mutations, dedup/publication, full QC, CI and merge checks; these are not pre-certified
  here. No record or original review bytes were changed.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: Current glyoxysome
  and hydrogenosomal membrane are unchanged. Hydrogenosome is stale: added lumen parthood
  is supported; the new IscS/IscU source attribution is too broad and is independently
  filed as a new minor finding with no invented predecessor.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: Sutak is actual web-reader
  main text and caption text, not raw publisher HTML or source pixels. Schneider is
  fresh genuine BioC selected main-text sections (Introduction, all Methods,3.1,3.5,3.7–3.10),
  not all article sections, supplements, raw spectra or pixels. Dolezal is detailed
  indexed primary main text read now with reported six-day-old crawl, not a fresh
  raw body/PDF download; its actual returned Methods/Results/Discussion and caption
  scopes are explicit.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: deZoysa1994 and Bui1996
  are complete primary-abstract tiers only; the old review body scopes are not claimed
  as newly reread. Lindmark1973 is exact metadata with no available native abstract;
  Tachezy2022 is a complete secondary-review abstract. Failed browser/PDF/API routes
  are retained and are not biological negative evidence.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: Sutak directly measures
  TvIscS-2 localization and hydrogenosomal lysate FeS reconstitution. IscU model discussion
  is not a T.vaginalis localization experiment; Schneider later proteome detection
  has fractionation/association limits. No claim that IscU is absent follows.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: Dolezal Giardia proteins
  expressed in T.vaginalis and yeast/rat processing comparators are distinct experimental
  systems. Internal signals and N-terminal signals coexist. Lack of predicted motif,
  lack of proteomic detection, fraction membership and organelle-formation necessity
  are distinct.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: All six assigned native
  protein checks exit0. Glyoxysome/membrane have zero examples and zero typed nodes;
  hydrogenosome has zero examples and three NO_GENE_SYMBOLS nodes, not zero typed
  coverage. Generic functional classes are explicitly permitted by the native combined
  policy; no unsupported single-family/complex identity or mandatory example finding
  is invented.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: All three original
  adapter checks are explicit expression-only exclusions, not omissions. Whole-record
  pathway/molecular narratives require actual applicability review. Fresh official
  catalogue lacks relevant eukaryotic host coverage; no foreign-host downstream query
  or biological absence inference. Historical runner failure is exactly00:49Z, not
  a newly executed attempt.'
- 'Glyoxysome and hydrogenosome/membrane independent subreview: Twenty-nine frozen
  repository inputs were actually used:17 common policy/schema/native files,3targets,6original
  artifacts,3boundary neighbors. Neighbors are context only; no whole-group or historical
  issue resolution is inferred. No maintained images, quantitative physical properties,
  traits or verbatim snippets require asset checks.'
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
  Inherited scientific findings retain stable keys and exact predecessor repository/review/finding
  identities. New findings have no invented predecessor.
- 'Issue #2702 tracks two stale target inputs. Golgi apparatus retypes its existing
  SNARE cohort to PROTEIN_COMPLEX; the current members and scope are assessed against
  primary complex evidence and native class guidance. Hydrogenosome adds lumen parthood
  and FeS-machinery localization edges; topology and source-specific localization
  claims are reassessed independently.'
- 'Issue #2703 tracks ten unsupported applicability exclusions. All ten original reviews
  contain an explicit expression-only not_applicable row; none omits it. Actual glyoxylate-cycle/import,
  glycosylation/SNARE/vesicle trafficking, marker-defined maturation, GDP-mannose
  transport, COPI budding and energy/FeS/import assertions require bounded catalogue
  coverage assessment.'
- Source commit f23e1970804e4f93de15a4ae275af84d48e6ce14 is retained by tag review-base/pr2367-current-record-followup-20261103.
- CLAUDE.md aliases AGENTS.md; canonical regular AGENTS.md bytes are frozen. All 50
  used local inputs were frozen before assessment. Glyoxysomal lumen, glyoxysomal
  membrane and hydrogenosome lumen are bounded context only, not additional review
  targets or dispositions.
- Fresh and reused sources retain actual access times and inspection tiers. Authority
  identity does not independently establish structure membership, mechanistic action,
  complex co-membership, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Golgi apparatus has six reviewed
  yeast examples and two COVERED typed nodes. Hydrogenosome has no examples and three
  NO_GENE_SYMBOLS nodes anchored to import, pyruvate-metabolism and FeS-machinery
  class components. The other eight records have no examples or typed molecular nodes.
  Command success does not certify narrative molecular or source-attribution claims.
- 'Closed grouped issue #2462 is historical context for the Golgi component-type change,
  without a disposition of other grouped records. Native-validator issue #2514 remains
  open and reused. Six related Golgi issue candidates were read fully and concern
  distinct records/findings.'
- Native class-level guidance permits heterogeneous molecular classes when represented
  honestly. A specific claim that a broad SNARE cohort is one complex is assessed
  on source-supported membership; enum wording alone is not treated as proof of a
  defect.
- 'Ten scientific findings remain open: eight inherited findings concerning whole-membrane/lipid
  correspondences, whole-cisterna/component correspondence, citation title or SNARE
  attribution, and import-route qualification; two new changed-record findings concern
  physical-complex scope and Sutak-specific IscU localization attribution. These map
  to #2704, #2705, #2706, #2707, #2708, #2709, #2710, #2711, #2712, #2713. Six targets
  need curation; the associated-vesicle membrane, cisterna membrane, Golgi lumen and
  Golgi membrane have qualified positive assessments.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015623Z-glyoxysome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015625Z-golgi-apparatus-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015627Z-golgi-associated-vesicle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015629Z-golgi-associated-vesicle-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015631Z-golgi-cisterna-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015633Z-golgi-cisterna-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015635Z-golgi-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015637Z-golgi-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015639Z-hydrogenosomal-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T015641Z-hydrogenosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2367
- https://github.com/CultureBotAI/CellStructureMech/issues/2462
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2702
- https://github.com/CultureBotAI/CellStructureMech/issues/2703
- https://github.com/CultureBotAI/CellStructureMech/issues/2704
- https://github.com/CultureBotAI/CellStructureMech/issues/2705
- https://github.com/CultureBotAI/CellStructureMech/issues/2706
- https://github.com/CultureBotAI/CellStructureMech/issues/2707
- https://github.com/CultureBotAI/CellStructureMech/issues/2708
- https://github.com/CultureBotAI/CellStructureMech/issues/2709
- https://github.com/CultureBotAI/CellStructureMech/issues/2710
- https://github.com/CultureBotAI/CellStructureMech/issues/2711
- https://github.com/CultureBotAI/CellStructureMech/issues/2712
- https://github.com/CultureBotAI/CellStructureMech/issues/2713
```
