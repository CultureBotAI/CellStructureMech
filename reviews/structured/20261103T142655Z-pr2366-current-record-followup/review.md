# PR 2366: current-input review of ten records and adversarial follow-up

- Review: 20261103T142655Z-pr2366-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T14:09:49.269959Z
- Finished UTC: 2026-11-03T14:26:55Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2366. Three stale reviews are substantively refreshed and all ten structured-source applicability exclusions are corrected. Five inherited scientific findings, two major and three minor, remain open for separate record curation; no records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 31ddf488bda650f463921061d848027b8ebf74e9. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 51825f94f13ad8ed893319d04d4b4a8041b6a161.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 85122489fca6bd0f63b1a6b276d138f847405e3e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020016 | data/structures/membrane_organelle/flagellar_pocket.yaml | maintained | flagellar pocket |
| GO:0020020 | data/structures/membrane_organelle/food_vacuole.yaml | maintained | food vacuole |
| GO:0000324 | data/structures/membrane_organelle/fungal_type_vacuole.yaml | maintained | fungal-type vacuole |
| GO:0000328 | data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml | maintained | fungal-type vacuole lumen |
| GO:0000329 | data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml | maintained | fungal-type vacuole membrane |
| GO:0020015 | data/structures/membrane_organelle/glycosome.yaml | maintained | glycosome |
| GO:0034468 | data/structures/membrane_organelle/glycosome_lumen.yaml | maintained | glycosome lumen |
| GO:0046860 | data/structures/membrane_organelle/glycosome_membrane.yaml | maintained | glycosome membrane |
| GO:0031908 | data/structures/membrane_organelle/glyoxysomal_lumen.yaml | maintained | glyoxysomal lumen |
| GO:0046861 | data/structures/membrane_organelle/glyoxysomal_membrane.yaml | maintained | glyoxysomal membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0020016 | passed | True | GO:0020016 | Documented focused command passed. |
| validate-strict GO:0020016 | passed | True | GO:0020016 | Documented focused command passed. |
| validate GO:0020020 | passed | True | GO:0020020 | Documented focused command passed. |
| validate-strict GO:0020020 | passed | True | GO:0020020 | Documented focused command passed. |
| validate GO:0000324 | passed | True | GO:0000324 | Documented focused command passed. |
| validate-strict GO:0000324 | passed | True | GO:0000324 | Documented focused command passed. |
| validate GO:0000328 | passed | True | GO:0000328 | Documented focused command passed. |
| validate-strict GO:0000328 | passed | True | GO:0000328 | Documented focused command passed. |
| validate GO:0000329 | passed | True | GO:0000329 | Documented focused command passed. |
| validate-strict GO:0000329 | passed | True | GO:0000329 | Documented focused command passed. |
| validate GO:0020015 | passed | True | GO:0020015 | Documented focused command passed. |
| validate-strict GO:0020015 | passed | True | GO:0020015 | Documented focused command passed. |
| validate GO:0034468 | passed | True | GO:0034468 | Documented focused command passed. |
| validate-strict GO:0034468 | passed | True | GO:0034468 | Documented focused command passed. |
| validate GO:0046860 | passed | True | GO:0046860 | Documented focused command passed. |
| validate-strict GO:0046860 | passed | True | GO:0046860 | Documented focused command passed. |
| validate GO:0031908 | passed | True | GO:0031908 | Documented focused command passed. |
| validate-strict GO:0031908 | passed | True | GO:0031908 | Documented focused command passed. |
| validate GO:0046861 | passed | True | GO:0046861 | Documented focused command passed. |
| validate-strict GO:0046861 | passed | True | GO:0046861 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | All ten explicit expression-only exclusions are corrected based on the complete records: BILBO1 and endo/exocytosis, hemoglobin/heme processing, hydrolase/V-ATPase functions, glycolysis/peroxin import, and glyoxylate-cycle/import context. Official complete catalogue responses and bounded host/strain searches establish no matching coverage for the reviewed hosts. No foreign-host proxy or unsupported downstream query is used. Noncoverage is not biological absence. Historical adapter-runner unavailability retains its actual time and is not a fresh invocation. |
| Independent claim-level source review | passed | True | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native flagellar pocket UniProt verify check | passed | True | GO:0020016 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative BILBO1/trafficking claims remain separately assessed. |
| Native flagellar pocket UniProt causal check | passed | True | GO:0020016 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative BILBO1/trafficking claims remain separately assessed. |
| Native food vacuole UniProt verify check | passed | True | GO:0020020 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; digestion/hemozoin and boundary claims remain separately assessed. |
| Native food vacuole UniProt causal check | passed | True | GO:0020020 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; digestion/hemozoin and boundary claims remain separately assessed. |
| Native fungal-type vacuole UniProt verify check | passed | True | GO:0000324 | Read-only native command returned zero. Three reviewed S. cerevisiae S288C examples PEP4/P07267, PRB1/P09232 and PRC1/P00729 are verified; one typed node is COVERED. Identity does not prove assembly necessity. |
| Native fungal-type vacuole UniProt causal check | passed | True | GO:0000324 | Read-only native command returned zero. Three reviewed S. cerevisiae S288C examples PEP4/P07267, PRB1/P09232 and PRC1/P00729 are verified; one typed node is COVERED. Identity does not prove assembly necessity. |
| Native fungal-type vacuole lumen UniProt verify check | passed | True | GO:0000328 | Read-only native command returned zero. No component protein examples are represented; one UNANCHORED_WITH_UNIPROT hydrolase-cohort node carries verified P07267/P00729/P09232 xrefs. This is not full component coverage or individual necessity. |
| Native fungal-type vacuole lumen UniProt causal check | passed | True | GO:0000328 | Read-only native command returned zero. No component protein examples are represented; one UNANCHORED_WITH_UNIPROT hydrolase-cohort node carries verified P07267/P00729/P09232 xrefs. This is not full component coverage or individual necessity. |
| Native fungal-type vacuole membrane UniProt verify check | passed | True | GO:0000329 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative V-ATPase acidification remains separately assessed. |
| Native fungal-type vacuole membrane UniProt causal check | passed | True | GO:0000329 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; narrative V-ATPase acidification remains separately assessed. |
| Native glycosome UniProt verify check | passed | True | GO:0020015 | Read-only native command returned zero. Nine protein examples are verified: six reviewed and three unreviewed, spanning glycolytic enzymes and peroxin machinery; two typed nodes are COVERED. TIM is assessed using the actual protein alias and primary context, not an invented UniProt indexed gene symbol. Membership and mechanism remain separate. |
| Native glycosome UniProt causal check | passed | True | GO:0020015 | Read-only native command returned zero. Nine protein examples are verified: six reviewed and three unreviewed, spanning glycolytic enzymes and peroxin machinery; two typed nodes are COVERED. TIM is assessed using the actual protein alias and primary context, not an invented UniProt indexed gene symbol. Membership and mechanism remain separate. |
| Native glycosome lumen UniProt verify check | passed | True | GO:0034468 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; glycolytic narrative claims remain separately assessed. |
| Native glycosome lumen UniProt causal check | passed | True | GO:0034468 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; glycolytic narrative claims remain separately assessed. |
| Native glycosome membrane UniProt verify check | passed | True | GO:0046860 | Read-only native command returned zero. No component protein examples are represented; one UNANCHORED_WITH_UNIPROT PEX14 node carries verified Q38CL4. This is not full component coverage or proof of all import mechanism. |
| Native glycosome membrane UniProt causal check | passed | True | GO:0046860 | Read-only native command returned zero. No component protein examples are represented; one UNANCHORED_WITH_UNIPROT PEX14 node carries verified Q38CL4. This is not full component coverage or proof of all import mechanism. |
| Native glyoxysomal lumen UniProt verify check | passed | True | GO:0031908 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; glyoxylate-cycle targeting claims remain separately assessed. |
| Native glyoxysomal lumen UniProt causal check | passed | True | GO:0031908 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; glyoxylate-cycle targeting claims remain separately assessed. |
| Native glyoxysomal membrane UniProt verify check | passed | True | GO:0046861 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; matrix-import and glyoxylate-cycle context remain separately assessed. |
| Native glyoxysomal membrane UniProt causal check | passed | True | GO:0046861 | Read-only native command returned zero. Represented protein inventory and typed molecular-node coverage are empty; matrix-import and glyoxylate-cycle context remain separately assessed. |

## Scientific And Domain Assessments

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0020016.

Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions are independently assessed. Both native commands exit0; these do not establish scientific mechanism, exact molecular families or formation necessity.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0020016.

Original validates/renders and all 15 historical inputs match its source. Current target unchanged; exact inherited F1 lineage retained. No historical group/neighbor/category issue is terminally resolved.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0020016.

All current evidence, histories, discussions and graphs inspected. No target image assets, verbatim snippets, trait links or quantitative properties to audit. Optional enzymes/transporters/cytoskeletal features do not justify invented accessions or completeness defects. PROPOSED unchanged.

### Actual molecular/pathway trigger and catalogue noncoverage

scope: supported. Targets: GO:0020016.

BILBO1 and endo/exocytic trafficking are explicit current assertions. Original check explicitly excluded iModulonDB on an expression-only rationale, not an omission. Fresh complete catalogue has no relevant host, so no downstream matched-gene/module query applies. Primary/authority fallback is complete within declared tiers; historical runner remains separately dated unavailable.

### Represented protein inventory and graph actor coverage

schema: supported. Targets: GO:0020020.

Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions are independently assessed. Both native commands exit0; these do not establish scientific mechanism, exact molecular families or formation necessity.

### Original immutable pair and frozen-input currentness

provenance: supported. Targets: GO:0020020.

Original validates/renders and all 14 historical inputs match its source. Current target changed; membrane boundary delta and history substantively reassessed against current sources. No historical group/neighbor/category issue is terminally resolved.

### Complete current fields and optional inventories

completeness: supported. Targets: GO:0020020.

All current evidence, histories, discussions and graphs inspected. No target image assets, verbatim snippets, trait links or quantitative properties to audit. Optional enzymes/transporters/cytoskeletal features do not justify invented accessions or completeness defects. PROPOSED unchanged.

### Actual molecular/pathway trigger and catalogue noncoverage

scope: supported. Targets: GO:0020020.

Hemoglobin catabolism/heme detoxification and named digestive-vacuole transporters are explicit current assertions. Original check explicitly excluded iModulonDB on an expression-only rationale, not an omission. Fresh complete catalogue has no relevant host, so no downstream matched-gene/module query applies. Primary/authority fallback is complete within declared tiers; historical runner remains separately dated unavailable.

### Whole pocket versus membrane and collar

identity: supported. Targets: GO:0020016.

GO0020016 is the plasma-membrane invagination with exact flagellar-pocket synonym. SUBCELLULAR_REGION is appropriate for this invagination, distinct from whole membrane0020018 and collar1990900. The identity is not changed by the molecular component defect.

### T. brucei life-stage and strain scopes

scope: supported. Targets: GO:0020016.

Species5691 is T. brucei. Lacomble uses procyclic427, Gadelha bloodstream forms, Bonhivers distinct procyclic/bloodstream lines. COMMON is qualitative, not a measured prevalence. Single-pocket description is read in routine cell architecture with duplication explicitly retained; no all-cell-cycle one-pocket exclusion inferred.

### Molecular lipid row incorrectly grounded to whole membrane

grounding: concern. Targets: GO:0020016.

The ciliary_pocket_membrane row has component_type LIPID but grounding GO:0020018, whose native identity is the complete ciliary pocket membrane. Schema StructuralComponent requires a molecular building block and distinguishes chemical lipid grounding from GO sub-complex grounding. The graph component_ref repeats the same invalid molecular correspondence. Correct membrane topology and membrane/collar membership do not resolve this field-level identity mismatch.

### Collar membership and new-pocket formation

evidence: supported. Targets: GO:0020016.

GO1990900 identifies a collar protein complex at the neck; Bonhivers primary localization and RNAi support BILBO1-dependent formation of a new collar/pocket. The old pocket persists during knockdown, so this is not total absence of all pockets or universal necessity of every collar protein.

### Scoped architecture and trafficking

evidence: supported. Targets: GO:0020016.

Lacomble primary architecture and Gadelha membrane/uptake observations support pocket/neck domains and trafficking context. Field/Halliday are explicitly secondary abstract-level review support for endo/exocytosis, not fresh experimental proof. Lacomble selected discussion cites Bonhivers for collar BILBO1/biogenesis; that source is inspected directly.

### Three descriptive boundary/traffic edges and invalid material correspondence

graph: concern. Targets: GO:0020016.

All three NONMECHANISTIC relations remain supported: membrane lines pocket, collar localizes at neck and pocket supports trafficking. Whole membrane STRUCTURE grounding is valid; its component_ref propagates the invalid GO-whole-membrane to LIPID correspondence. Correct topology does not repair F1.

### Boundary mechanism and chemical necessity

evidence: unknown. Targets: GO:0020016.

Exact lipid mixture, molecular mechanisms establishing domains and complete collar constituent necessity are not established here. No figure pixels, raw tomograms or supplemental quantitative reanalysis performed; caption/text inspection remains distinct.

### Parasite digestive vacuole

identity: supported. Targets: GO:0020020.

GO0020020 exact identity and digestive-vacuole synonym match the defined host-cytoplasm digestion compartment. MEMBRANE_BOUNDED_ORGANELLE matches reviewed anatomy; not a generic endosome, lysosome or separate membrane record.

### Explicit P. falciparum blood-stage scope

scope: supported. Targets: GO:0020020.

NCBITaxon5833 is P. falciparum. Lamarque primary abstract directly supports its FV-enriched proteomic fraction and the canonical example. Current occurrence note explicitly declines broader Plasmodium/Apicomplexa occurrence claims; COMMON is qualitative. Fractions are not treated as pure/exhaustive constituent inventories.

### Reviewed label-only aggregate membrane

grounding: supported. Targets: GO:0020020.

Generic LIPID constituent is an explicitly REVIEWED_LABEL_ONLY aggregate with no false whole-membrane GO grounding or guessed chemical identity. Cowman directly localizes Pgh1 to its membrane; Wiser supplies secondary acidic-boundary/transport context. Exact lipid/protein-family composition and individual necessity are deliberately unasserted.

### Hemoglobin digestion and heme detoxification

evidence: supported. Targets: GO:0020020.

Wiser inspected review sections3.2/4 support acid-compartment proteolysis, heme release and sequestration as hemozoin. Lamarque supports the experimental FV-fraction context. These remain broad functions; no exact enzyme sequence, stoichiometry or fully resolved biocrystallization mechanism is claimed.

### Three original NONMECHANISTIC digestion/hemozoin relations

graph: supported. Targets: GO:0020020.

Vacuole digests hemoglobin, hemoglobin releases heme during proteolysis and heme crystallizes into hemozoin are supported by inspected secondary review text. No unverified CHEBI IDs are restored; chemical labels and descriptive graph scope do not assert direct molecular catalytic mechanism.

### Substantive refresh of new membrane STRUCTURE node and bounds edge

graph: supported. Targets: GO:0020020.

Current delta adds membrane STRUCTURE with existing reviewed-label-only component_ref and a bounds edge separating acidic lumen from parasite cytosol. Cowman primary abstract directly locates Pgh1 on the digestive-vacuole membrane; Wiser inspected body explicitly discusses compartment properties and transport across that boundary. This supports topology, not novel transporter direction or formation mechanism. The changed record can be accurately reviewed in this PR without record edits.

### Exact membrane chemistry and primary proteome/biocrystallization detail

evidence: unknown. Targets: GO:0020020.

Cowman/Lamarque access is primary abstract only; exact underlying images, fraction purity beyond stated abstract limits and raw proteome were not reanalysed. Wiser is secondary body support. Optional PfCRT/Pgh1/protease/proton-pump accessions and exact hemozoin mechanism are not inferred or fabricated.

### Exact structure and boundary identity

identity: supported. Targets: GO:0000324.

Exact fungal-type vacuole identity denotes the membrane-bounded whole, both lytic and storage; exact recorded morphology synonym matches. Whole/lumen/membrane remain separate identities.

### Species, reference strain and experimental scope

scope: supported. Targets: GO:0000324.

Saccharomyces species4932 supports canonical example and qualitative COMMON occurrence. UniProt559292 is reference S288C; Parzych SEY6210 derivatives are retained as experimental context and not renamed S288C. No prevalence percentage or universal fungal distribution asserted.

### Component class, instances and necessity boundary

grounding: supported. Targets: GO:0000324.

Heterogeneous soluble acid hydrolases span A1/S8/S10 families, so class-level reviewed-label-only grounding and UNKNOWN formation essentiality are appropriate. Three exact reviewed taxon-paired examples are supported; PRC1 is correctly representative despite PRE10 alias collision.

### Storage, hydrolysis and acidification source scope

evidence: supported. Targets: GO:0000324.

Storage/degradative functions are supported by exact GO definition and Li/Kane secondary synthesis. Named soluble protease roles agree with primary Parzych and native identities. Delivery routes do not make all delivered cargo a stable resident.

### Every current graph node and edge

graph: supported. Targets: GO:0000324.

All seven current NONMECHANISTIC FUNCTION edges checked: membrane bounds lumen; whole is a vacuole; lumen stores small molecules; hydrolases act there; lumen compartmentalizes degradation; new membrane and lumen part_of whole. Both new direct GO parthood notes are exact.

### Experimental and molecular completeness limits

evidence: unknown. Targets: GO:0000324.

Neither exact identity nor a localization annotation establishes individual formation necessity or a complete molecular inventory. Primary Parzych single/double-mutant results preserve redundancy; lower pH is optimal but not universally essential for hydrolase activity. Secondary review synthesis and current abstract-only evidence remain explicitly scoped.

### Entire record, discussions and optional evidence

completeness: supported. Targets: GO:0000324.

All current fields/history/discussions read. No target image, quantitative physical property, trait link or verbatim snippet is asserted. PROPOSED status retained. Optional family/lipid/machinery groundings and acknowledged unknowns are not fabricated findings; no historical issue or category-wide disposition is made.

### Original immutability and actual native protein coverage

schema: supported. Targets: GO:0000324.

Original YAML validates and exact Markdown render agrees; original frozen target verified through git source bytes. Current source-head native verify/causal commands passed with separately documented inventories; deterministic success is not scientific membership proof.

### Original expression-only exclusion requires correction

provenance: concern. Targets: GO:0000324.

Original check exists but excludes iModulonDB solely because expression-module inference is unused. The target asserts named proteins, hydrolase pathways or V-ATPase acidification; native policy requires coverage assessment. This is a review-bundle defect, not a scientific record curation finding.

### Current exact-organism catalogue applicability

evidence: not_applicable. Targets: GO:0000324.

Fresh complete official catalogue has no Saccharomyces/cerevisiae/S288C match. No downstream gene/module query is applicable without an unmatched organism proxy. Historical runner failure remains separately dated; bounded noncoverage is not negative biological evidence.

### Exact structure and boundary identity

identity: supported. Targets: GO:0000328.

Exact internal volume is a SUBCELLULAR_REGION; enclosing membrane is boundary, not the lumen substance. Direct lumen is_a and part_of are confirmed.

### Species, reference strain and experimental scope

scope: supported. Targets: GO:0000328.

Saccharomyces species4932 supports canonical example and qualitative COMMON occurrence. UniProt559292 is reference S288C; Parzych SEY6210 derivatives are retained as experimental context and not renamed S288C. No prevalence percentage or universal fungal distribution asserted.

### Component class, instances and necessity boundary

grounding: supported. Targets: GO:0000328.

No component inventory is required for a volume. Three reviewed xrefs identify hydrolase actors within it; native UNANCHORED_WITH_UNIPROT is the explicit permitted route, not a broken component_ref. The resolved membrane-as-boundary discussion agrees.

### Storage, hydrolysis and acidification source scope

evidence: supported. Targets: GO:0000328.

Storage/degradative functions are supported by exact GO definition and Li/Kane secondary synthesis. Named soluble protease roles agree with primary Parzych and native identities. Delivery routes do not make all delivered cargo a stable resident.

### Every current graph node and edge

graph: supported. Targets: GO:0000328.

All six NONMECHANISTIC FUNCTION edges checked: lumen is_a broader lumen; part_of whole; membrane bounds it; lumen stores molecules; hydrolases act there; lumen compartmentalizes degradation. Xrefs ground actors without inventing a complete enzyme inventory.

### Experimental and molecular completeness limits

evidence: unknown. Targets: GO:0000328.

Neither exact identity nor a localization annotation establishes individual formation necessity or a complete molecular inventory. Primary Parzych single/double-mutant results preserve redundancy; lower pH is optimal but not universally essential for hydrolase activity. Secondary review synthesis and current abstract-only evidence remain explicitly scoped.

### Entire record, discussions and optional evidence

completeness: supported. Targets: GO:0000328.

All current fields/history/discussions read. No target image, quantitative physical property, trait link or verbatim snippet is asserted. PROPOSED status retained. Optional family/lipid/machinery groundings and acknowledged unknowns are not fabricated findings; no historical issue or category-wide disposition is made.

### Original immutability and actual native protein coverage

schema: supported. Targets: GO:0000328.

Original YAML validates and exact Markdown render agrees; original frozen target verified through git source bytes. Current source-head native verify/causal commands passed with separately documented inventories; deterministic success is not scientific membership proof.

### Original expression-only exclusion requires correction

provenance: concern. Targets: GO:0000328.

Original check exists but excludes iModulonDB solely because expression-module inference is unused. The target asserts named proteins, hydrolase pathways or V-ATPase acidification; native policy requires coverage assessment. This is a review-bundle defect, not a scientific record curation finding.

### Current exact-organism catalogue applicability

evidence: not_applicable. Targets: GO:0000328.

Fresh complete official catalogue has no Saccharomyces/cerevisiae/S288C match. No downstream gene/module query is applicable without an unmatched organism proxy. Historical runner failure remains separately dated; bounded noncoverage is not negative biological evidence.

### Exact structure and boundary identity

identity: supported. Targets: GO:0000329.

Exact fungal vacuole lipid boundary is MEMBRANE, distinct from its internal volume and whole organelle. Broader vacuolar membrane parentage is transitive, not claimed a direct GO subclass edge.

### Species, reference strain and experimental scope

scope: supported. Targets: GO:0000329.

Saccharomyces species4932 supports canonical example and qualitative COMMON occurrence. UniProt559292 is reference S288C; Parzych SEY6210 derivatives are retained as experimental context and not renamed S288C. No prevalence percentage or universal fungal distribution asserted.

### Component class, instances and necessity boundary

grounding: supported. Targets: GO:0000329.

The single lipid-bilayer constituent describes defining boundary material; ESSENTIAL is collective boundary constitution, not molecular knockout proof. The separate V-ATPase is correctly a STRUCTURE complex node, not a protein-family lipid component.

### Storage, hydrolysis and acidification source scope

evidence: supported. Targets: GO:0000329.

Vacuolar membrane houses vacuolar V-ATPase proton pumps, supported by GO0016471/GO0007035 and scoped Kane/Li reviews. No complete composition, assembly mechanism or claim that every V-type complex is vacuolar is asserted.

### Every current graph node and edge

graph: supported. Targets: GO:0000329.

All five NONMECHANISTIC FUNCTION edges checked: membrane is_a broader membrane; part_of whole; bounds lumen; vacuolar V-ATPase resides there and participates in acidification. Edges express bounded topology/function, not a complete causal assembly model.

### Experimental and molecular completeness limits

evidence: unknown. Targets: GO:0000329.

Neither exact identity nor a localization annotation establishes individual formation necessity or a complete molecular inventory. Primary Parzych single/double-mutant results preserve redundancy; lower pH is optimal but not universally essential for hydrolase activity. Secondary review synthesis and current abstract-only evidence remain explicitly scoped.

### Entire record, discussions and optional evidence

completeness: supported. Targets: GO:0000329.

All current fields/history/discussions read. No target image, quantitative physical property, trait link or verbatim snippet is asserted. PROPOSED status retained. Optional family/lipid/machinery groundings and acknowledged unknowns are not fabricated findings; no historical issue or category-wide disposition is made.

### Original immutability and actual native protein coverage

schema: supported. Targets: GO:0000329.

Original YAML validates and exact Markdown render agrees; original frozen target verified through git source bytes. Current source-head native verify/causal commands passed with separately documented inventories; deterministic success is not scientific membership proof.

### Original expression-only exclusion requires correction

provenance: concern. Targets: GO:0000329.

Original check exists but excludes iModulonDB solely because expression-module inference is unused. The target asserts named proteins, hydrolase pathways or V-ATPase acidification; native policy requires coverage assessment. This is a review-bundle defect, not a scientific record curation finding.

### Current exact-organism catalogue applicability

evidence: not_applicable. Targets: GO:0000329.

Fresh complete official catalogue has no Saccharomyces/cerevisiae/S288C match. No downstream gene/module query is applicable without an unmatched organism proxy. Historical runner failure remains separately dated; bounded noncoverage is not negative biological evidence.

### Substantive current-input reassessment

provenance: supported. Targets: GO:0000324.

Original whole review froze d447fe7b… and assessed five graph edges. Current1dc8607f… adds history plus two direct part_of edges. Both native GO children and OLS direct BFO0000050 graphs support lumen328/membrane329→whole324. All seven current edges and unchanged science were reassessed; original observation is preserved, not relabeled current.

### Original validation/render and frozen-input staleness

schema: supported. Targets: GO:0020015.

Original native schema and deterministic rendering pass. The frozen historical target hash verifies; current whole glycosome changes are substantively reassessed below, while the other four targets are byte-unchanged. Native schema validity does not certify semantic scientific typing.

### Actual represented inventory

provenance: supported. Targets: GO:0020015.

Nine current protein examples: six glycolytic enzymes including reviewed P04789/TIM, plus three PEX proteins; six reviewed and three unreviewed entries. Both represented GENE_OR_PROTEIN nodes are COVERED. These checks establish declared identifier/symbol coverage, not exact cohort type, family grounding, source membership or necessity.

### Images, physical properties, traits and snippets

scope: not_applicable. Targets: GO:0020015.

No maintained image asset, quantitative physical-property field, associated trait or verbatim snippet is declared. Source text/caption inspection does not constitute raw data or figure-pixel reanalysis.

### Status, immutable observations and scoped history

provenance: supported. Targets: GO:0020015.

PROPOSED status and history remain unchanged. Original findings retain exact lineage; absent original findings are not invented. Closed grouped issue2462 is historical context for the peroxin-type change only, not a current disposition of other records or the whole group.

### Original validation/render and frozen-input staleness

schema: supported. Targets: GO:0034468.

Original native schema and deterministic rendering pass. The frozen historical target hash verifies; current whole glycosome changes are substantively reassessed below, while the other four targets are byte-unchanged. Native schema validity does not certify semantic scientific typing.

### Actual represented inventory

provenance: supported. Targets: GO:0034468.

No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment.

### Images, physical properties, traits and snippets

scope: not_applicable. Targets: GO:0034468.

No maintained image asset, quantitative physical-property field, associated trait or verbatim snippet is declared. Source text/caption inspection does not constitute raw data or figure-pixel reanalysis.

### Status, immutable observations and scoped history

provenance: supported. Targets: GO:0034468.

PROPOSED status and history remain unchanged. Original findings retain exact lineage; absent original findings are not invented. Closed grouped issue2462 is historical context for the peroxin-type change only, not a current disposition of other records or the whole group.

### Original validation/render and frozen-input staleness

schema: supported. Targets: GO:0046860.

Original native schema and deterministic rendering pass. The frozen historical target hash verifies; current whole glycosome changes are substantively reassessed below, while the other four targets are byte-unchanged. Native schema validity does not certify semantic scientific typing.

### Actual represented inventory

provenance: supported. Targets: GO:0046860.

Zero protein examples, but one UNANCHORED_WITH_UNIPROT molecular node with verified PEX14 Q38CL4 xref. This is not an empty molecular inventory; it validates the represented identifier without establishing complete docking machinery or formation necessity.

### Images, physical properties, traits and snippets

scope: not_applicable. Targets: GO:0046860.

No maintained image asset, quantitative physical-property field, associated trait or verbatim snippet is declared. Source text/caption inspection does not constitute raw data or figure-pixel reanalysis.

### Status, immutable observations and scoped history

provenance: supported. Targets: GO:0046860.

PROPOSED status and history remain unchanged. Original findings retain exact lineage; absent original findings are not invented. Closed grouped issue2462 is historical context for the peroxin-type change only, not a current disposition of other records or the whole group.

### Original validation/render and frozen-input staleness

schema: supported. Targets: GO:0031908.

Original native schema and deterministic rendering pass. The frozen historical target hash verifies; current whole glycosome changes are substantively reassessed below, while the other four targets are byte-unchanged. Native schema validity does not certify semantic scientific typing.

### Actual represented inventory

provenance: supported. Targets: GO:0031908.

No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment.

### Images, physical properties, traits and snippets

scope: not_applicable. Targets: GO:0031908.

No maintained image asset, quantitative physical-property field, associated trait or verbatim snippet is declared. Source text/caption inspection does not constitute raw data or figure-pixel reanalysis.

### Status, immutable observations and scoped history

provenance: supported. Targets: GO:0031908.

PROPOSED status and history remain unchanged. Original findings retain exact lineage; absent original findings are not invented. Closed grouped issue2462 is historical context for the peroxin-type change only, not a current disposition of other records or the whole group.

### Original validation/render and frozen-input staleness

schema: supported. Targets: GO:0046861.

Original native schema and deterministic rendering pass. The frozen historical target hash verifies; current whole glycosome changes are substantively reassessed below, while the other four targets are byte-unchanged. Native schema validity does not certify semantic scientific typing.

### Actual represented inventory

provenance: supported. Targets: GO:0046861.

No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment.

### Images, physical properties, traits and snippets

scope: not_applicable. Targets: GO:0046861.

No maintained image asset, quantitative physical-property field, associated trait or verbatim snippet is declared. Source text/caption inspection does not constitute raw data or figure-pixel reanalysis.

### Status, immutable observations and scoped history

provenance: supported. Targets: GO:0046861.

PROPOSED status and history remain unchanged. Original findings retain exact lineage; absent original findings are not invented. Closed grouped issue2462 is historical context for the peroxin-type change only, not a current disposition of other records or the whole group.

### Claim-sensitive pathway applicability and exact-host coverage

scope: not_applicable. Targets: GO:0020015.

The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import pathways. An expression-only exemption is insufficient even when the graph is descriptive. Fresh complete official catalogue lacks matching actual hosts, so downstream module queries are not applicable; no negative biology or engineered-host substitution is inferred.

### Claim-sensitive pathway applicability and exact-host coverage

scope: not_applicable. Targets: GO:0034468.

The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import pathways. An expression-only exemption is insufficient even when the graph is descriptive. Fresh complete official catalogue lacks matching actual hosts, so downstream module queries are not applicable; no negative biology or engineered-host substitution is inferred.

### Claim-sensitive pathway applicability and exact-host coverage

scope: not_applicable. Targets: GO:0046860.

The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import pathways. An expression-only exemption is insufficient even when the graph is descriptive. Fresh complete official catalogue lacks matching actual hosts, so downstream module queries are not applicable; no negative biology or engineered-host substitution is inferred.

### Claim-sensitive pathway applicability and exact-host coverage

scope: not_applicable. Targets: GO:0031908.

The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import pathways. An expression-only exemption is insufficient even when the graph is descriptive. Fresh complete official catalogue lacks matching actual hosts, so downstream module queries are not applicable; no negative biology or engineered-host substitution is inferred.

### Claim-sensitive pathway applicability and exact-host coverage

scope: not_applicable. Targets: GO:0046861.

The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import pathways. An expression-only exemption is insufficient even when the graph is descriptive. Fresh complete official catalogue lacks matching actual hosts, so downstream module queries are not applicable; no negative biology or engineered-host substitution is inferred.

### Exact glycosome structure and compartment boundaries

identity: supported. Targets: GO:0020015.

Native GO/UniProt verify whole organelle, surrounding membrane and enclosed matrix separately. Glycosome is_a peroxisome; membrane is_a peroxisomal membrane; lumen has broad organelle-lumen is_a ancestry. Exact direct mappings are separated from nested parent identities.

### Kinetoplastid scope and experimental versus reference strains

scope: supported. Targets: GO:0020015.

Kinetoplastea5653 is a class with Kinetoplastida synonym, so legacy GO order wording is not a different taxon. Review synthesis supports examined kinetoplastids and variable enzyme content across taxa/stages. T.brucei experiments in29–13/PF449 and bloodstream contexts are not relabeled TREU927 because exemplar accessions use that strain. COMMON does not assert an experiment measured population prevalence.

### Import or survival requirement versus organelle formation

grounding: unknown. Targets: GO:0020015.

Constitutive bilayer is distinguished from individual lipid/protein formation requirements. Import defects, growth loss and metabolic toxicity do not alone prove failed organelle assembly; Galland reports apparently intact procyclic glycosomes after receptor depletion. Protein UNKNOWN essentiality remains appropriate.

### Exact glycosome structure and compartment boundaries

identity: supported. Targets: GO:0034468.

Native GO/UniProt verify whole organelle, surrounding membrane and enclosed matrix separately. Glycosome is_a peroxisome; membrane is_a peroxisomal membrane; lumen has broad organelle-lumen is_a ancestry. Exact direct mappings are separated from nested parent identities.

### Kinetoplastid scope and experimental versus reference strains

scope: supported. Targets: GO:0034468.

Kinetoplastea5653 is a class with Kinetoplastida synonym, so legacy GO order wording is not a different taxon. Review synthesis supports examined kinetoplastids and variable enzyme content across taxa/stages. T.brucei experiments in29–13/PF449 and bloodstream contexts are not relabeled TREU927 because exemplar accessions use that strain. COMMON does not assert an experiment measured population prevalence.

### Import or survival requirement versus organelle formation

grounding: unknown. Targets: GO:0034468.

Constitutive bilayer is distinguished from individual lipid/protein formation requirements. Import defects, growth loss and metabolic toxicity do not alone prove failed organelle assembly; Galland reports apparently intact procyclic glycosomes after receptor depletion. Protein UNKNOWN essentiality remains appropriate.

### Exact glycosome structure and compartment boundaries

identity: supported. Targets: GO:0046860.

Native GO/UniProt verify whole organelle, surrounding membrane and enclosed matrix separately. Glycosome is_a peroxisome; membrane is_a peroxisomal membrane; lumen has broad organelle-lumen is_a ancestry. Exact direct mappings are separated from nested parent identities.

### Kinetoplastid scope and experimental versus reference strains

scope: supported. Targets: GO:0046860.

Kinetoplastea5653 is a class with Kinetoplastida synonym, so legacy GO order wording is not a different taxon. Review synthesis supports examined kinetoplastids and variable enzyme content across taxa/stages. T.brucei experiments in29–13/PF449 and bloodstream contexts are not relabeled TREU927 because exemplar accessions use that strain. COMMON does not assert an experiment measured population prevalence.

### Import or survival requirement versus organelle formation

grounding: unknown. Targets: GO:0046860.

Constitutive bilayer is distinguished from individual lipid/protein formation requirements. Import defects, growth loss and metabolic toxicity do not alone prove failed organelle assembly; Galland reports apparently intact procyclic glycosomes after receptor depletion. Protein UNKNOWN essentiality remains appropriate.

### Substantive refresh of added TIM example

grounding: supported. Targets: GO:0020015.

Current reviewed P04789 is glycosomal triosephosphate isomerase in taxon5702 and has protein short name TIM, with no indexed geneName. Literal gene_exact query returns zero while the reviewed protein-name query returns only P04789. Misset abstract and Haanstra TIM activity fractionation support glycosomal enzyme context independently of accession identity. Native represented coverage is now complete; this is not a new proof of an indexed gene symbol.

### Substantive refresh of import-apparatus retyping

schema: supported. Targets: GO:0020015.

The current PROTEIN_COMPLEX type describes multi-protein import apparatus rather than one family. Primary PEX5/PEX7 interaction and PEX13/PEX14 docking evidence supports the apparatus context, without asserting all listed proteins form one permanent stoichiometric unit. Closed2462 is historical only; this review neither reopens that correction nor resolves other grouped targets.

### Nine exact exemplar identities and source placement

grounding: supported. Targets: GO:0020015.

All nine accession/status/taxon pairs agree; six are reviewed and three unreviewed. GAPDH O96429 is an unreviewed fragment. PEX5/PEX7 cytosolic/cycling annotations and PEX14 membrane localization remain distinct; PEX14-specific edge description does not make every receptor permanently membrane resident. Identity/automatic family annotations are not direct localization experiments for every modern accession.

### Explicit heterogeneous enzyme class under native modeling guidance

schema: supported. Targets: GO:0020015.

The glycolytic_enzymes row transparently declares unrelated families grouped by pathway and localization, with UNKNOWN formation necessity. Although the enum prose is narrower, CURATION explicitly permits a taxon-agnostic family or class and the UniProt skill recognizes generic class components. This policy tension does not establish a confirmed record defect. Retaining this qualified class does not assert one homologous family or a stable protein complex; no automatic PROTEIN_COMPLEX conversion is justified.

### Peroxin and enzyme family scope

grounding: supported. Targets: GO:0020015.

Individual PEX families are distinct and do not each identify the entire import apparatus. No single family denotes the heterogeneous glycolytic set, which is explicitly labeled as a class. Native family-or-class and generic-class guidance supports retaining that qualification; no confirmed component-type defect, forced split, invented broad family or automatic complex classification follows from the narrower enum prose alone.

### Whole membrane encoded as molecular lipid identity

grounding: concern. Targets: GO:0020015.

Inherited F3 persists: component glycosome_membrane is LIPID grounded to assembled membrane GO0046860, with graph component_ref. The correct substructure is already represented by has_part and its STRUCTURE node. Preserve that topology while correcting the molecular/material representation; no exact lipid composition is established here.

### Glucose phenotype and qualified mechanistic inference

evidence: concern. Targets: GO:0020015.

Inherited F2 persists in function description/evidence and final graph edge. Haanstra2008 measured Glc6P accumulation in29–13 after glucose but explicitly could not exclude PGI-pathway truncation; PF449 lacked significant Glc6P accumulation. Glycerol/Gly3P plus GK-rescue supplies the stronger mechanism test. Preserve the observed phenotype and general compartmentation function while qualifying the glucose-specific causal claim.

### Supported import/localization sequence with bounded endpoint

graph: concern. Targets: GO:0020015.

PEX14 membrane docking/import and enzyme matrix localization are supported at the read primary tiers. Receptor cycling remains distinct from permanent membrane residency; the membrane component grounding and glucose-specific causal endpoint require the stated corrections. Model membrane removal is not a directly performed cellular membrane-deletion experiment.

### Repeated PEX14 first-author attribution

evidence: concern. Targets: GO:0020015.

The repeatedly cited DOI belongs to Moyersoen et al.2003, with Choe second. Correct the repeated Choe et al. notes while retaining the exact DOI/title and supported import/localization biology. The inherited stable key and predecessor for this maintained record are preserved.

### Repeated PEX14 first-author attribution

evidence: concern. Targets: GO:0046860.

The repeatedly cited DOI belongs to Moyersoen et al.2003, with Choe second. Correct the repeated Choe et al. notes while retaining the exact DOI/title and supported import/localization biology. The inherited stable key and predecessor for this maintained record are preserved.

### General compartmentation and two descriptive boundaries

graph: supported. Targets: GO:0034468.

The lumen houses major glycolytic enzymes and provides a compartment for flux control. The general statement does not claim Haanstra uniquely resolves the glucose-specific mechanism. Lumen parthood and membrane enclosure are NONMECHANISTIC, and the membrane is not inserted as lumen material.

### Collective bilayer versus exact lipid chemistry

grounding: supported. Targets: GO:0046860.

The label-only lipid constituent denotes collective bilayer material; no whole-membrane GO term is asserted as its exact molecular grounding. The structural graph node refers to its constituting material without claiming an exact lipid species or complete mixture.

### Four descriptive membrane/import-placement edges

graph: supported. Targets: GO:0046860.

Native definitions support membrane parthood/enclosure. Complete Moyersoen abstract and Furuya body support PEX14 membrane docking and import, with Q38CL4 identity independently current. NONMECHANISTIC scope does not pretend to model the entire receptor cycle; biological relations remain supported despite the attribution correction.

### Glyoxysomal exact identity and relation typing

identity: supported. Targets: GO:0031908.

GO/UniProt distinguish matrix volume, bounding membrane and whole glyoxysome. Broad lumen parent GO0043233 is an is_a ancestor; membrane parent is peroxisomal membrane. Exact synonyms/direct mappings and parthood are verified without treating nested mappings as identity. The frozen whole neighbor supplies boundary context only.

### Actual fungal acetate-induced targeting assay

scope: supported. Targets: GO:0031908.

Current complete de Zoysa/Connerton primary abstract directly supports acetate-induced N.crassa glyoxysomes and C-terminally modified CAT reporter import. This supplies fungal occurrence independently of plant-oriented GO/UniProt descriptions. Native identity is5141; reporter efficacy is condition/sequence dependent and not a universal route for every matrix protein. Current source access is abstract only, so detailed strains, medium values, original plots or endogenous-enzyme exceptions from the old full-body review are not freshly certified.

### Unestablished molecular assembly requirements

grounding: unknown. Targets: GO:0031908.

The enclosing bilayer defines the membrane compartment; individual lipid-removal/substitution or protein necessities for organelle formation are not established. Reporter targeting and pathway activity do not establish these requirements. No complete chemical or protein inventory is inferred.

### Glyoxysomal exact identity and relation typing

identity: supported. Targets: GO:0046861.

GO/UniProt distinguish matrix volume, bounding membrane and whole glyoxysome. Broad lumen parent GO0043233 is an is_a ancestor; membrane parent is peroxisomal membrane. Exact synonyms/direct mappings and parthood are verified without treating nested mappings as identity. The frozen whole neighbor supplies boundary context only.

### Actual fungal acetate-induced targeting assay

scope: supported. Targets: GO:0046861.

Current complete de Zoysa/Connerton primary abstract directly supports acetate-induced N.crassa glyoxysomes and C-terminally modified CAT reporter import. This supplies fungal occurrence independently of plant-oriented GO/UniProt descriptions. Native identity is5141; reporter efficacy is condition/sequence dependent and not a universal route for every matrix protein. Current source access is abstract only, so detailed strains, medium values, original plots or endogenous-enzyme exceptions from the old full-body review are not freshly certified.

### Unestablished molecular assembly requirements

grounding: unknown. Targets: GO:0046861.

The enclosing bilayer defines the membrane compartment; individual lipid-removal/substitution or protein necessities for organelle formation are not established. Reporter targeting and pathway activity do not establish these requirements. No complete chemical or protein inventory is inferred.

### Matrix pathway context and three descriptive edges

graph: supported. Targets: GO:0031908.

The function and cycle edge description assert that glyoxylate-pathway enzymes are contained in the matrix, not that every reaction is exclusively luminal or every endogenous enzyme uses one C-terminal signal. GO and the primary abstract support this compartment context; parthood/enclosure edges are descriptive. Empty optional components are compatible with enclosed-volume identity.

### Collective membrane material and boundary topology

graph: supported. Targets: GO:0046861.

Reviewed-label-only bilayer, organelle parthood and enclosure of matrix follow exact membrane/lumen definitions. The canonical import example is bounded to the primary reporter assay; no transport pore mechanism, direct translocation movie, individual membrane factor or chemical lipid inventory is asserted.

### Current independent scientific verdict

evidence: concern. Targets: GO:0020015.

Whole glycosome retains three inherited findings; membrane retains its own inherited first-author finding. The proposed heterogeneous-class typing concern was not confirmed after checking both native class policies; it is not a finding or curation action. Exact stable keys and predecessors remain scoped to their records. Bundle applicability repairs are separate. No neighbor/group/historical issue is terminally disposed of by this review.

### Current independent scientific verdict

evidence: supported. Targets: GO:0034468.

No concrete scientific correction established for this complete assigned compartment/membrane target; retain source-tier, pathway, assay and empty-inventory limitations. Bundle applicability repairs are separate. No neighbor/group/historical issue is terminally disposed of by this review.

### Current independent scientific verdict

evidence: concern. Targets: GO:0046860.

Whole glycosome retains three inherited findings; membrane retains its own inherited first-author finding. The proposed heterogeneous-class typing concern was not confirmed after checking both native class policies; it is not a finding or curation action. Exact stable keys and predecessors remain scoped to their records. Bundle applicability repairs are separate. No neighbor/group/historical issue is terminally disposed of by this review.

### Current independent scientific verdict

evidence: supported. Targets: GO:0031908.

No concrete scientific correction established for this complete assigned compartment/membrane target; retain source-tier, pathway, assay and empty-inventory limitations. Bundle applicability repairs are separate. No neighbor/group/historical issue is terminally disposed of by this review.

### Current independent scientific verdict

evidence: supported. Targets: GO:0046861.

No concrete scientific correction established for this complete assigned compartment/membrane target; retain source-tier, pathway, assay and empty-inventory limitations. Bundle applicability repairs are separate. No neighbor/group/historical issue is terminally disposed of by this review.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0020016, GO:0020020, GO:0000324, GO:0000328, GO:0000329, GO:0020015, GO:0034468, GO:0046860, GO:0031908, GO:0046861.

3 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t0-F1: Separate the complete pocket membrane from its molecular lipid constituent

major / open / confirmed; issue key: flagellar-pocket-lipid-whole-membrane-grounding.

The ciliary_pocket_membrane row has component_type LIPID but grounding GO:0020018, whose native identity is the complete ciliary pocket membrane. Schema StructuralComponent requires a molecular building block and distinguishes chemical lipid grounding from GO sub-complex grounding. The graph component_ref repeats the same invalid molecular correspondence. Correct membrane topology and membrane/collar membership do not resolve this field-level identity mismatch.

### septin-glycosome-F1: Correct the PEX14 paper’s first-author attribution

minor / open / confirmed; issue key: glycosome-pex14-first-author-attribution.

DOI10.1046/j.1432-1033.2003.03582.x is Moyersoen et al.2003, with Choe second. Several source notes call it Choe et al.2003. The DOI/title and relevant import biology are correct; the first-author attribution is not.

### septin-glycosome-F2: Retain the paper’s glucose-mechanism qualification

minor / open / confirmed; issue key: glycosome-glucose-mechanism-evidence-scope.

The function evidence says Haanstra2008 showed compartmentation prevents toxic Glc6P accumulation, and the final graph edge states that causal endpoint without the paper’s qualification. Its Results and Discussion explicitly say the glucose experiment is not a stringent test: PGI truncation is an alternative, PF449 lacked significant Glc6P accumulation, and glycerol/GK rescue provides the stronger mechanistic test. The observed29–13 glucose phenotype is valid but does not uniquely resolve that mechanism.

### septin-glycosome-F3: Separate the membrane substructure from molecular lipid composition

major / open / confirmed; issue key: glycosome-membrane-molecular-component-grounding.

The glycosome_membrane component names the complete membrane, declares type LIPID, and grounds it to GO0046860, which identifies the assembled bilayer surrounding a glycosome. The frozen schema defines StructuralComponent as a molecular building block, with lipid grounding to chemical classes. The graph itself correctly types this object as STRUCTURE but attaches the molecular component_ref. Correct has_part and boundary topology already represent the membrane; they do not make the whole structure a lipid identity.

### septin-glycosome_membrane-F1: Correct the PEX14 paper’s first-author attribution

minor / open / confirmed; issue key: glycosome_membrane-pex14-first-author-attribution.

DOI10.1046/j.1432-1033.2003.03582.x is Moyersoen et al.2003, with Choe second. Several source notes call it Choe et al.2003. The DOI/title and relevant import biology are correct; the first-author attribution is not.

## Recommended Actions And Acceptance Checks

### plaque-t0-A1

In a separately authorized curation change, retain the complete membrane as structural topology and represent only a source-supported molecular lipid material in components, using exact chemical grounding where justified or an explicitly reviewed label-only material. Correct/remove the graph component_ref so it does not equate the whole membrane with that molecular entry.

- Confirm that every LIPID grounding identifies lipid material, not GO0020018 as the whole membrane; do not invent an exact lipid mixture or assign an arbitrary CHEBI term.
- Preserve the correctly grounded membrane STRUCTURE node and descriptive edges, the pocket identity, and the GO-grounded protein-complex collar.
- Run focused schema, grounding/product and graph checks after separately authorized scientific curation.

### septin-glycosome-A1

In separately authorized curation, change the repeated author attribution to Moyersoen et al.2003 while retaining the verified DOI and supported claim scopes.

- Preserve supported structure, protein identities and source-specific experimental boundaries.
- Run focused schema, strict and relevant native graph checks after separately authorized curation.

### septin-glycosome-A2

In separately authorized curation, distinguish the observed glucose-addition phenotype and competing PGI explanation from the stronger glycerol proof; qualify the glucose-specific causal wording and source note while preserving supported import and pathway compartmentation.

- Preserve supported structure, protein identities and source-specific experimental boundaries.
- Run focused schema, strict and relevant native graph checks after separately authorized curation.

### septin-glycosome-A3

In separately authorized curation, retain GO0046860 in has_part and as the grounded membrane graph node; remove its molecular component_ref if removing the whole-membrane component, or replace that component only with an independently supported molecular/material lipid description and appropriate grounding. Do not invent a lipid composition.

- Preserve supported structure, protein identities and source-specific experimental boundaries.
- Run focused schema, strict and relevant native graph checks after separately authorized curation.

### septin-glycosome_membrane-A1

In separately authorized curation, change the repeated author attribution to Moyersoen et al.2003 while retaining the verified DOI and supported claim scopes.

- Preserve supported structure, protein identities and source-specific experimental boundaries.
- Run focused schema, strict and relevant native graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/membrane_organelle/flagellar_pocket.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8; current SHA256 d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T014651Z-flagellar-pocket-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/membrane_organelle/food_vacuole.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 956ec0d47253c51f7931d89e9308f1be821836cb87de96410327f374e30d5ac0; current SHA256 834e2ee1d3c5f37ca9f20f2541cccfcc755cc94621c864ab84c0a4687a2baa1f. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261022T014653Z-food-vacuole-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/fungal_type_vacuole.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d447fe7bc41bcf0749629f12affde731c10286f9efbb170efbf81bc27b975016; current SHA256 1dc8607faa4099575b74222bd6303877b27107ec0d2bbdcf13ceadbb839e4559. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261022T014654Z-fungal-type-vacuole-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa; current SHA256 ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T014656Z-fungal-type-vacuole-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51; current SHA256 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T014657Z-fungal-type-vacuole-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/glycosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e4e8d4917968433f370c60a2f571b3c3e1f11034b01373015911772e014d2b1e; current SHA256 c31397edde14cca6a35fa8574d38fdd77f1c6d49bbe95f145d6f1a8e872b033b. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261022T014658Z-glycosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/glycosome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544; current SHA256 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T014659Z-glycosome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/glycosome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9; current SHA256 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T014700Z-glycosome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/glyoxysomal_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b; current SHA256 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T014701Z-glyoxysomal-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/glyoxysomal_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c; current SHA256 acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T014701Z-glyoxysomal-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-0 | data/structures/membrane_organelle/flagellar_pocket.yaml; Entire maintained record at source 85122489fca6bd0f63b1a6b276d138f847405e3e; all fields, histories, discussions and graphs | supports | Unchanged from original frozen target. PROPOSED unchanged. No scientific record curation performed by this reviewer. |
| plaque-original-0 | reviews/structured/20261022T014651Z-flagellar-pocket-audit/review.yaml; Exact staleness-listed original authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders byte-exactly; all 15 historical frozen inputs match its source. Historical scientific verdict independently reassessed; original content remains immutable. |
| plaque-current-1 | data/structures/membrane_organelle/food_vacuole.yaml; Entire maintained record at source 85122489fca6bd0f63b1a6b276d138f847405e3e; all fields, histories, discussions and graphs | supports | Changed from original frozen target: new membrane STRUCTURE node/component_ref and bounds edge, plus curation history; current delta substantively reassessed. PROPOSED unchanged. No scientific record curation performed by this reviewer. |
| plaque-original-1 | reviews/structured/20261022T014653Z-food-vacuole-audit/review.yaml; Exact staleness-listed original authoritative YAML/Markdown, input hashes, checks, assessments, findings/actions and limitations | supports | Original pair validates and renders byte-exactly; all 14 historical frozen inputs match its source. Historical scientific verdict independently reassessed; original content remains immutable. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen native contract and relevant definitions | context_only | Named genes/proteins/regulators/pathways/stress responses/traits trigger structured-source assessment. Empty accession inventories do not waive narrative pathway claims. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native contract and relevant definitions | context_only | Exact identity, source scope, grounding, taxonomy and necessity must be assessed; missing optional inventories alone are not findings. |
| plaque-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native contract and relevant definitions | context_only | Mechanistic claims require inspected primary support; descriptive identity/topology alone is not a molecular causal sequence. |
| plaque-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen native contract and relevant definitions | context_only | Native protein checks assess represented accession inventories and typed graph actors; narrative protein claims still require source assessment. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native contract and relevant definitions | context_only | StructuralComponent represents a molecular building block. A whole membrane GO identity does not identify lipid material; GO may ground a protein subcomplex. Structural topology and molecular material remain distinct. |
| plaque-neighbor-membrane | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; Entire frozen neighbor read for bounded identity/material/boundary context only | context_only | Whole GO0020018 membrane is distinguished from its reviewed-label-only lipid-bilayer constituent; structural boundary is valid without treating whole GO membrane as lipid identity. Other neighbor protein examples and claims are not independently certified; no terminal historical disposition. |
| plaque-neighbor-collar | data/structures/cytoskeleton/ciliary_pocket_collar.yaml; Entire frozen neighbor read for bounded identity/material/boundary context only | context_only | Whole GO1990900 collar is a protein-complex structure at the pocket neck, distinct from pocket, membrane and flagellum. Other neighbor protein examples and claims are not independently certified; no terminal historical disposition. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900,GO:0020020; All five exact active term names/definitions/synonyms and typed children in complete returned JSON | supports | GO0020016 ciliary pocket has exact flagellar pocket synonym and is a plasma-membrane invagination;0020018 denotes its complete plasma-membrane domain, not lipid material;1990900 is its neck collar.0020016 lists membrane/collar part_of children;0060170 lists0020018 is_a.0020020 is a parasite food vacuole digesting host cytoplasm, with digestive vacuole exact synonym. Authority identities are not species-specific necessity experiments. |
| plaque-tax-5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete native taxId/scientificName/rank/lineage | supports | Species5691 is Trypanosoma brucei. Taxon identity does not establish measured prevalence or silently equate experimental strains/life stages. |
| plaque-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Complete native taxId/scientificName/rank/lineage | supports | Species5833 is Plasmodium falciparum. Taxon identity does not establish measured prevalence or silently equate experimental strains/life stages. |
| plaque-doi-10.1038_nrmicro2221 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrmicro2221; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Field and Carrington2009 PMID19806154 is a review. Complete abstract supports the trypanosome pocket as a plasma-membrane invagination and endo/exocytosis site. Secondary abstract scope; no publisher full body inspected. |
| plaque-doi-10.1242_jcs.045740 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242/jcs.045740; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Lacomble et al.2009 PMID19299460, exact primary article identity and complete abstract; architecture and boundaries independently inspected in body. |
| plaque-doi-10.1073_pnas.0909289106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0909289106; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Gadelha et al.2009 PMID19805090, exact primary article identity and complete abstract; membrane domains and boundary experiments inspected in body. |
| plaque-doi-10.1016_j.pt.2020.11.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.pt.2020.11.005; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Halliday et al.2021 PMID33308952 is a review comparing trypanosomatid pocket structure/functions. Complete abstract supports scoped endo/exocytic trafficking; no publisher full body or primary intervention claimed. |
| plaque-bonhivers2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pbio.0060105; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Bonhivers et al.2008 PMID18462016, exact primary article identity and complete abstract; BILBO1 perturbation and collar localization independently inspected in primary manuscript. |
| plaque-cowman1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083/jcb.113.5.1033%22; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Cowman et al.1991 PMID1674943 complete primary abstract. Immunofluorescence/immunoelectron microscopy localizes Pgh1 to the digestive-vacuole membrane of mature P. falciparum parasites. This supports membrane localization and boundary context; resistance mechanism is proposed, not demonstrated individual formation necessity. No body/figure pixels inspected. |
| plaque-lamarque2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1002/prca.200700112%22; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Exact MED PMID21136929 entry from two returned DOI matches; Lamarque et al.2008 complete primary abstract describes FV-enriched P. falciparum fraction and 116 identified proteins. EM and immunoblot support major FV contribution, not purification to homogeneity or universal required constituents. No primary full body/figure pixels inspected. |
| plaque-wiser2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.3390/pathogens13030182%22; Exact EuropePMC core bibliographic match and complete abstract; additional body tier separately stated | supports | Wiser2024 PMID38535526 is explicitly a review, not a new primary experiment; exact identity/complete abstract. Detailed digestion and membrane context inspected in review body. |
| plaque-pmc-PMC2714436 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/; Genuine PMC primary HTML Resultssec3/4 and Methodssec10; selected Introduction/Discussion paragraphs explicitly mentioning Bonhivers/BILBO1; embedded captions as text, no figure pixels/movies | supports | Procyclic T. brucei brucei427 tomography defines an asymmetric pocket, membrane domains, collar and neck boundaries. The selected Discussion explicitly cites Bonhivers for BILBO1/collar and lost-pocket RNAi phenotypes, so the canonical architecture/biogenesis context is appropriately linked to that primary study separately. Pocket duplication/cell-cycle context is retained; routine single-pocket wording is not treated as denial of duplication. No biochemical lipid identity or universal unique collar mechanism follows from morphology. |
| plaque-pmc-PMC2755463 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/; Genuine PMC primary HTML Resultssec2/3/5/6 and Methodssec12 with embedded caption text; no SI Methods, supplements, movies or figure pixels | supports | Bloodstream-form trypanosome cold-marker uptake, physiological-temperature tomography and freeze-fracture distinguish FP, cell-surface and flagellar membranes and their boundaries. Clathrin distribution and neck-channel observations support broad trafficking/domain context. A marker accumulation at low temperature is not proof of active transport mechanism, and membrane particle/domain organization does not ground a whole membrane as lipid material. |
| plaque-bonhivers2008-plos | https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0060105&amp;type=manuscript; Genuine primary publisher XML sections s2a/s2b/s2c/s3a/s3d/s4a/s4e/s4i; figure captions embedded as text, no figure pixels or supplementary raw data | supports | BILBO1 localizes to FPC; RNAi prevents new FPC/FP formation while the preexisting pocket persists, with positioning/cytokinesis defects. Methods distinguish genomic TREU927/4 GUTat10.1, procyclic EATRO1125-T7T and bloodstream427 90-13 lines. This directly supports new-pocket biogenesis wording; do not equate all strain contexts, generalize to every collar constituent, or infer exact bilayer chemistry. |
| plaque-wiser2024-numeric | https://pmc.ncbi.nlm.nih.gov/articles/10974218/; Genuine PMC review body section3.2 includingTable2 and complete section4 with4.1/4.2/4.3 and Fig2caption; no figure pixels or referenced primary experiments reanalysis | supports | Secondary synthesis supports an acidic digestive compartment, membrane separation/transport between digestive lumen and parasite cytoplasm, hemoglobin proteolysis, heme release and hemozoin crystallization. Transporter directions and exact hemozoin molecular mechanism remain incompletely resolved. The newly added boundary edge is descriptive topology; no primary causal mechanism or protein necessity is inferred from this review. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh official /api/datasets response; all20 organism rows and their listed organism/dataset pairs read, no pagination | supports | Returned catalogue contains no Trypanosoma brucei or Plasmodium falciparum host. BILBO1/endo-exocytic trafficking and hemoglobin/heme pathways trigger assessment, but no matched downstream gene/module query applies. Unrelated bacterial/archaeal datasets are not proxies. Catalogue noncoverage is not biological absence; generated module prose is not used. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical00:49Z receipt with stdout/stderr reread and hashes verified | context_only | Historical runner failed before dataset retrieval with PermissionError reading pyvenv.cfg. No current invocation or success claimed; fresh official catalogue and scoped primary/authority sources are the permitted fallback. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-plaque/original-checks.json; Both original native validation/render results and historical-source input hashes | supports | Both original pairs validate/render exactly; historical input counts15/14 all match their source commits. Flagellar pocket unchanged, food vacuole genuinely stale; historical validation does not certify current bytes. |
| plaque-native-flagellar_pocket-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/flagellar_pocket.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions are independently assessed. |
| plaque-native-flagellar_pocket-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/flagellar_pocket.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions are independently assessed. |
| plaque-native-food_vacuole-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/food_vacuole.yaml --verify; Root-owned actual command receipt/stdout independently read and hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions are independently assessed. |
| plaque-native-food_vacuole-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/food_vacuole.yaml --causal-graphs; Root-owned actual command receipt/stdout independently read and hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes Scope: Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions are independently assessed. |
| micro-policy | .claude/skills/review-yaml-record/SKILL.md; Entire current skill; reread with profile/config/shared contract/checklist and CURATION identity/component/graph rules | context_only | Scientific claims require narrow inspected source support. Named proteins/pathways trigger structured-source applicability; absence of expression inference is not an exemption. Original observations remain immutable. |
| micro-protein-contract | .claude/skills/uniprot-protein-examples/SKILL.md; Entire native protein skill and StructuralComponent/ProteinExample/CausalNode schema definitions; verifier coverage labels inspected | context_only | Distinguish identity from membership, canonical species from reference strain, constituent components from allowed external/region actor xrefs, and structure-formation necessity from enzyme activity. |
| micro-graph-contract | .claude/skills/curate-causal-graphs/SKILL.md; Entire graph skill and linked add-cell-structure graph/evidence contract; NONMECHANISTIC scope retained | context_only | Topology/function graphs retain bounded source scope; no fabricated molecular assembly path, component inventory, or new status promotion. |
| micro-record-fungal_type_vacuole | data/structures/membrane_organelle/fungal_type_vacuole.yaml; Entire maintained current YAML, including all graph edges, history, discussions, examples and source notes | supports | Current target read independently. Original input is stale: only the October31 history event and two direct part_of edges were added. |
| micro-prior-fungal_type_vacuole | reviews/structured/20261022T014654Z-fungal-type-vacuole-audit/review.yaml; Original full scientific assessments, evidence scopes, checks, findings/actions and limitations; deterministic paired Markdown checked | context_only | Original qualified pass with no findings or curation actions. Explicit expression-only iModulonDB exclusion is deficient. Historical accesses/checks are not claimed freshly executed. |
| micro-native-fungal_type_vacuole-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole.yaml --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source head. Three reviewed component examples P07267/PEP4,P09232/PRB1,P00729/PRC1 at tax559292; one COVERED acid-hydrolase node. Coverage verifies declared examples, not an exhaustive vacuolar proteome or membership by itself. |
| micro-native-fungal_type_vacuole-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole.yaml --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-causal.log SHA256 e7efbc62941a2ec7ab1762a1b02eecc60e7822f33d2a0374f1e9f672d833eba7 | supports | Exit0 at exact source head. Three reviewed component examples P07267/PEP4,P09232/PRB1,P00729/PRC1 at tax559292; one COVERED acid-hydrolase node. Coverage verifies declared examples, not an exhaustive vacuolar proteome or membership by itself. |
| micro-record-fungal_type_vacuole_lumen | data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml; Entire maintained current YAML, including all graph edges, history, discussions, examples and source notes | supports | Current target read independently. Current target bytes equal original frozen input. |
| micro-prior-fungal_type_vacuole_lumen | reviews/structured/20261022T014656Z-fungal-type-vacuole-lumen-audit/review.yaml; Original full scientific assessments, evidence scopes, checks, findings/actions and limitations; deterministic paired Markdown checked | context_only | Original qualified pass with no findings or curation actions. Explicit expression-only iModulonDB exclusion is deficient. Historical accesses/checks are not claimed freshly executed. |
| micro-native-fungal_type_vacuole_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source head. Zero component examples but three exact graph xrefs P07267/P00729/P09232 on one UNANCHORED_WITH_UNIPROT hydrolase actor. This is the documented xref route for actors within a region, not a dangling component or empty molecular check. |
| micro-native-fungal_type_vacuole_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-causal.log SHA256 2de30b5d9b2d9220d3ede9b9735fb20738120d09199197e7860aed297ab11440 | supports | Exit0 at exact source head. Zero component examples but three exact graph xrefs P07267/P00729/P09232 on one UNANCHORED_WITH_UNIPROT hydrolase actor. This is the documented xref route for actors within a region, not a dangling component or empty molecular check. |
| micro-record-fungal_type_vacuole_membrane | data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml; Entire maintained current YAML, including all graph edges, history, discussions, examples and source notes | supports | Current target read independently. Current target bytes equal original frozen input. |
| micro-prior-fungal_type_vacuole_membrane | reviews/structured/20261022T014657Z-fungal-type-vacuole-membrane-audit/review.yaml; Original full scientific assessments, evidence scopes, checks, findings/actions and limitations; deterministic paired Markdown checked | context_only | Original qualified pass with no findings or curation actions. Explicit expression-only iModulonDB exclusion is deficient. Historical accesses/checks are not claimed freshly executed. |
| micro-native-fungal_type_vacuole_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at exact source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN nodes; the vacuolar V-ATPase complex is typed STRUCTURE. Generic success is an empty protein inventory, not a biochemical composition test. |
| micro-native-fungal_type_vacuole_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0 at exact source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN nodes; the vacuolar V-ATPase complex is typed STRUCTURE. Generic success is an empty protein inventory, not a biochemical composition test. |
| micro-original-pairs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-microtubule/original-validation-receipt.json; Three native validate and three render --content executions; six actual outputs hashed; historical git-show target hashes rechecked | supports | All three original YAMLs validate and their deterministic Markdown matches exactly. Historical target hashes match frozen inputs; only whole vacuole changed. |
| micro-stale-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-microtubule/fungal-vacuole-stale.diff; Complete historical-frozen to current-source diff for fungal_type_vacuole only | context_only | The only delta adds one history event and membrane/lumen direct parthood edges, each with exact GO evidence. No proteins, definitions or earlier edges changed. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000324,GO:0000328,GO:0000329,GO:0005773,GO:0005774,GO:0005775,GO:0016471,GO:0007035; Complete eight-term native QuickGO response, active flags, names, definitions, synonyms and children | supports | All eight current identifiers resolve with correct distinctions: whole GO0000324; lumen328; membrane329; broader vacuole5773/lumen5775/membrane5774; vacuolar V-ATPase0016471; acidification0007035. Whole definition explicitly supports storage, hydrolases and degradation. Exact morphology synonym agrees. |
| micro-ols-0000324 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0000324/graph; Complete native OLS GO graph nodes/edges for exact GO:0000324 | supports | Current direct BFO0000050 edges from both fungal lumen328 and membrane329 to whole324 are explicit. Lumen is directly subclass of vacuolar lumen5775; whole and membrane broader parentage are checked separately by is_a ancestry. |
| micro-ols-0000328 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0000328/graph; Complete native OLS GO graph nodes/edges for exact GO:0000328 | supports | Current direct BFO0000050 edges from both fungal lumen328 and membrane329 to whole324 are explicit. Lumen is directly subclass of vacuolar lumen5775; whole and membrane broader parentage are checked separately by is_a ancestry. |
| micro-ols-0000329 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0000329/graph; Complete native OLS GO graph nodes/edges for exact GO:0000329 | supports | Current direct BFO0000050 edges from both fungal lumen328 and membrane329 to whole324 are explicit. Lumen is directly subclass of vacuolar lumen5775; whole and membrane broader parentage are checked separately by is_a ancestry. |
| micro-ancestors-whole | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000324/ancestors?relations=is_a; Complete native QuickGO ancestors response with relations=is_a | supports | GO0000324 includes GO0005773 in the is_a ancestors. This confirms compatible broader record parentage without relabeling it a direct ontology subclass edge. |
| micro-ancestors-membrane | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329/ancestors?relations=is_a; Complete native QuickGO ancestors response with relations=is_a | supports | GO0000329 includes GO0005774 in the is_a ancestors. This confirms compatible broader record parentage without relabeling it a direct ontology subclass edge. |
| micro-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxId/scientificName/rank/lineage fields | supports | NCBITaxon:4932 is Saccharomyces cerevisiae, species. This is authority identity, not measured prevalence or identification of the experimental strain in every paper. |
| micro-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxId/scientificName/rank/lineage fields | supports | NCBITaxon:559292 is Saccharomyces cerevisiae S288C, strain. This is authority identity, not measured prevalence or identification of the experimental strain in every paper. |
| micro-up-P07267 | https://rest.uniprot.org/uniprotkb/P07267.json; Primary accession, entryType, recommended names, all gene tokens, organism; complete FUNCTION/SUBCELLULAR LOCATION/SIMILARITY comments; relevant cited PubMed records | supports | P07267 is reviewed Saccharopepsin, primary gene PEP4, tax559292; native function/location and peptidase A1 annotation inspected. Distinct enzyme families support the heterogeneous acid-hydrolase class rather than one arbitrary family accession. |
| micro-up-P00729 | https://rest.uniprot.org/uniprotkb/P00729.json; Primary accession, entryType, recommended names, all gene tokens, organism; complete FUNCTION/SUBCELLULAR LOCATION/SIMILARITY comments; relevant cited PubMed records | supports | P00729 is reviewed Carboxypeptidase Y, primary gene PRC1, tax559292; native function/location and peptidase S10 annotation inspected. Distinct enzyme families support the heterogeneous acid-hydrolase class rather than one arbitrary family accession. Vacuole lumen SL0270 explicitly carries ECO0000269 citations14562095,23708375,29514932, matching target attribution notes. Separate VPS10/ATG42 prose on this entry is not transferred to PRC1. |
| micro-up-P09232 | https://rest.uniprot.org/uniprotkb/P09232.json; Primary accession, entryType, recommended names, all gene tokens, organism; complete FUNCTION/SUBCELLULAR LOCATION/SIMILARITY comments; relevant cited PubMed records | supports | P09232 is reviewed Cerevisin, primary gene PRB1, tax559292; native function/location and peptidase S8 annotation inspected. Distinct enzyme families support the heterogeneous acid-hydrolase class rather than one arbitrary family accession. |
| micro-unique-PEP4 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3APEP4%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned page and actual primary/synonym tokens; X-Total-Results 1 and Link None | supports | PEP4 returns exactly P07267 in this bounded reviewed S288C query. |
| micro-unique-PRC1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3APRC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned page and actual primary/synonym tokens; X-Total-Results 2 and Link None | supports | PRC1 returns P00729 primary PRC1 and P21242 primary PRE10 with PRC1 synonym. Target correctly calls P00729 a representative, not the unique search result; no arbitrary seeding or gene synonym error is asserted. |
| micro-unique-PRB1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=100&amp;query=%28gene_exact%3APRB1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Complete returned page and actual primary/synonym tokens; X-Total-Results 1 and Link None | supports | PRB1 returns exactly P09232 in this bounded reviewed S288C query. |
| micro-li2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1016/j.bbamcr.2008.08.003%22; Exact selected MED core bibliographic record and complete abstract; full text separately scoped | context_only | PMID18786576, DOI10.1016/j.bbamcr.2008.08.003: The yeast lysosome-like vacuole: endpoint and crossroads. Explicit secondary review article, not primary experimental evidence. |
| micro-kane2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1128/MMBR.70.1.177-191.2006%22; Exact selected MED core bibliographic record and complete abstract; full text separately scoped | context_only | PMID16524922, DOI10.1128/mmbr.70.1.177-191.2006: The where, when, and how of organelle acidification by the yeast vacuolar H+-ATPase. Explicit secondary review article, not primary experimental evidence. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID%3A14562095%20AND%20SRC%3AMED; Exact selected MED core bibliographic record and complete abstract; full text separately scoped | context_only | PMID14562095, DOI10.1038/nature02026: Global analysis of protein localization in budding yeast. Primary abstract inspected; Huh and Matsumoto bodies/datasets not read in this pass. Parzych body scope is separately recorded. |
| micro-pmid-23708375 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID%3A23708375%20AND%20SRC%3AMED; Exact selected MED core bibliographic record and complete abstract; full text separately scoped | context_only | PMID23708375, DOI10.1007/s00709-013-0510-2: Organelle acidification is important for localisation of vacuolar proteins in Saccharomyces cerevisiae. Primary abstract inspected; Huh and Matsumoto bodies/datasets not read in this pass. Parzych body scope is separately recorded. |
| micro-pmid-29514932 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID%3A29514932%20AND%20SRC%3AMED; Exact selected MED core bibliographic record and complete abstract; full text separately scoped | context_only | PMID29514932, DOI10.1091/mbc.e17-08-0516: A newly characterized vacuolar serine carboxypeptidase, Atg42/Ybr139w, is required for normal vacuole function and the terminal steps of autophagy in the yeast Saccharomyces cerevisiae. Primary abstract inspected; Huh and Matsumoto bodies/datasets not read in this pass. Parzych body scope is separately recorded. |
| micro-li2009-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC2906225/; Complete secondary review sections2.1/4.2/5.1/6.1/6.2 (S3/S13/S16/S20/S21), including embedded Fig2/3 captions; no figure pixels or underlying dataset reanalysis | context_only | Review explicitly identifies soluble Pep4/CPY/Prb1, storage of amino acids/ions/polyphosphate, and endocytic/biosynthetic/autophagic routes. It separates resident proteins from transient cargo and vacuolar Vph1 pumps from Golgi/endosomal Stv1. Low pH optimizes proteolysis but is not absolutely required for every reaction. |
| micro-kane2006-body | https://pmc.ncbi.nlm.nih.gov/articles/1393255/; Complete secondary review Introduction(sec1), yeast V-ATPase structure(sec3) and V0-a isoform targeting(sec11), including Fig1 caption; no figure pixels | context_only | Secondary synthesis supports membrane-associated vacuolar proton pumping and Vph1/Stv1 localization differences. STV1 overexpression/trafficking caveats preclude all-V-ATPases-permanently-vacuolar wording. Historical subunit model is not certified as current complete stoichiometry. |
| micro-parzych2018-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC5921575/; Complete Results sec3 andsec4, Discussionsec7, Methodssec9 with Tables1/2 and fluorescence microscopysec11; included Fig1/2/3 captions read, no pixels or supplements | supports | Primary Prc1-GFP comparison shows diffuse soluble lumenal signal distinct from FM4-64 membrane in growing/starved SEY6210-derived strains. Double prc1/ybr139w loss and single mutants demonstrate compensatory proteolytic function, not each protein necessary for vacuole assembly. Reference S288C accession identity is not the experimental strain. Mechanism of terminal autophagic body breakdown remains unresolved. |
| micro-catalogue-api | https://imodulondb.org/api/datasets; Complete official /api/datasets response: all20 organism rows,28 organism/dataset pairs; names,IDs,descriptions and lists read | context_only | No matched Saccharomyces cerevisiae/S288C dataset exists in this bounded current catalogue. All three molecular/pathway-bearing targets require applicability assessment, but no organism/dataset/gene/module key can be constructed without an unmatched proxy. No biological absence inference. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical00:49Z datasets invocation; exit1 PermissionError reading runner pyvenv.cfg; no current invocation | context_only | Historical runner availability limitation retained honestly; current scientific applicability uses freshly inspected official catalogue fallback. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured-source applicability, source fidelity and severity rubric | supports | Positive molecular/pathway assertions require applicability assessment throughout the record. Lack of an expression claim is not an exemption. Exact source scopes and uncertainty must be preserved; record curation stays outside this review. |
| septin-curation-policy | docs/CURATION.md; Component identity, molecular grounding, protein-example and necessity contracts | supports | A component represents a taxon-agnostic family/class; molecular lipids use chemical grounding, while substructures use parthood. Protein identity is not membership evidence, and import/survival phenotypes do not prove organelle-formation necessity. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent description/grounding and ComponentTypeEnum.PROTEIN/PROTEIN_COMPLEX | supports | StructuralComponent is one molecular building block. LIPID grounding denotes a chemical class, not an assembled membrane GO identity. The enum describes PROTEIN as one family/paralogue group, while CURATION and the UniProt skill explicitly permit generic class components. That modeling-policy tension alone does not establish a defect in a transparently declared heterogeneous class. PROTEIN_COMPLEX denotes a named sub-complex, not any list of unrelated enzymes. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Mechanistic versus NONMECHANISTIC graph and evidence scope | supports | Supported descriptive boundaries can remain NONMECHANISTIC. Source qualification, whole versus molecular identity, receptor cycling and observed perturbation versus inferred causal mechanism must remain distinct. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Step 2, NO_GENE_SYMBOL guidance: generic class components | supports | The native skill explicitly recognizes generic class components such as ribosomal proteins, peptidoglycan hydrolases and cargo proteins. Together with CURATION family-or-class guidance, this prevents treating narrower enum prose alone as a confirmed type defect; neither class membership nor a list of examples asserts one stable protein complex. |
| septin-record-glycosome | data/structures/membrane_organelle/glycosome.yaml; Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components and examples, taxonomic/canonical scope, functions, all evidence and graph edges, discussions/history. No maintained images, physical measurements, traits or verbatim snippets are declared. |
| septin-original-glycosome | reviews/structured/20261022T014658Z-glycosome-audit/review.yaml; Complete immutable original YAML/Markdown, frozen inputs, checks, assessments, findings/actions and source limits | supports | Historical checks and source access remain historical. Original scientific finding identities are preserved where applicable; all five originals contain explicit imodulondb exclusions. Whole glycosome is stale; the other four target inputs are unchanged. |
| septin-original-validation-glycosome | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json; 20261022T014658Z-glycosome-audit native validate/render and historical-source hash | supports | Native validate and render exit zero; original Markdown is byte-identical. Historical-source hash equals the frozen original. Current staleness status is True. |
| septin-native-glycosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-verify-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-verify.log | supports | Exit zero. Nine current protein examples: six glycolytic enzymes including reviewed P04789/TIM, plus three PEX proteins; six reviewed and three unreviewed entries. Both represented GENE_OR_PROTEIN nodes are COVERED. These checks establish declared identifier/symbol coverage, not exact cohort type, family grounding, source membership or necessity. |
| septin-native-glycosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-causal-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-causal.log | supports | Exit zero. Nine current protein examples: six glycolytic enzymes including reviewed P04789/TIM, plus three PEX proteins; six reviewed and three unreviewed entries. Both represented GENE_OR_PROTEIN nodes are COVERED. These checks establish declared identifier/symbol coverage, not exact cohort type, family grounding, source membership or necessity. |
| septin-record-glycosome_lumen | data/structures/membrane_organelle/glycosome_lumen.yaml; Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components and examples, taxonomic/canonical scope, functions, all evidence and graph edges, discussions/history. No maintained images, physical measurements, traits or verbatim snippets are declared. |
| septin-original-glycosome_lumen | reviews/structured/20261022T014659Z-glycosome-lumen-audit/review.yaml; Complete immutable original YAML/Markdown, frozen inputs, checks, assessments, findings/actions and source limits | supports | Historical checks and source access remain historical. Original scientific finding identities are preserved where applicable; all five originals contain explicit imodulondb exclusions. Whole glycosome is stale; the other four target inputs are unchanged. |
| septin-original-validation-glycosome_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json; 20261022T014659Z-glycosome-lumen-audit native validate/render and historical-source hash | supports | Native validate and render exit zero; original Markdown is byte-identical. Historical-source hash equals the frozen original. Current staleness status is False. |
| septin-native-glycosome_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-verify-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-verify.log | supports | Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment. |
| septin-native-glycosome_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-causal-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-causal.log | supports | Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment. |
| septin-record-glycosome_membrane | data/structures/membrane_organelle/glycosome_membrane.yaml; Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components and examples, taxonomic/canonical scope, functions, all evidence and graph edges, discussions/history. No maintained images, physical measurements, traits or verbatim snippets are declared. |
| septin-original-glycosome_membrane | reviews/structured/20261022T014700Z-glycosome-membrane-audit/review.yaml; Complete immutable original YAML/Markdown, frozen inputs, checks, assessments, findings/actions and source limits | supports | Historical checks and source access remain historical. Original scientific finding identities are preserved where applicable; all five originals contain explicit imodulondb exclusions. Whole glycosome is stale; the other four target inputs are unchanged. |
| septin-original-validation-glycosome_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json; 20261022T014700Z-glycosome-membrane-audit native validate/render and historical-source hash | supports | Native validate and render exit zero; original Markdown is byte-identical. Historical-source hash equals the frozen original. Current staleness status is False. |
| septin-native-glycosome_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-verify-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-verify.log | supports | Exit zero. Zero protein examples, but one UNANCHORED_WITH_UNIPROT molecular node with verified PEX14 Q38CL4 xref. This is not an empty molecular inventory; it validates the represented identifier without establishing complete docking machinery or formation necessity. |
| septin-native-glycosome_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-causal-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-causal.log | supports | Exit zero. Zero protein examples, but one UNANCHORED_WITH_UNIPROT molecular node with verified PEX14 Q38CL4 xref. This is not an empty molecular inventory; it validates the represented identifier without establishing complete docking machinery or formation necessity. |
| septin-record-glyoxysomal_lumen | data/structures/membrane_organelle/glyoxysomal_lumen.yaml; Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components and examples, taxonomic/canonical scope, functions, all evidence and graph edges, discussions/history. No maintained images, physical measurements, traits or verbatim snippets are declared. |
| septin-original-glyoxysomal_lumen | reviews/structured/20261022T014701Z-glyoxysomal-lumen-audit/review.yaml; Complete immutable original YAML/Markdown, frozen inputs, checks, assessments, findings/actions and source limits | supports | Historical checks and source access remain historical. Original scientific finding identities are preserved where applicable; all five originals contain explicit imodulondb exclusions. Whole glycosome is stale; the other four target inputs are unchanged. |
| septin-original-validation-glyoxysomal_lumen | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json; 20261022T014701Z-glyoxysomal-lumen-audit native validate/render and historical-source hash | supports | Native validate and render exit zero; original Markdown is byte-identical. Historical-source hash equals the frozen original. Current staleness status is False. |
| septin-native-glyoxysomal_lumen-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-verify-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-verify.log | supports | Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment. |
| septin-native-glyoxysomal_lumen-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-causal-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-causal.log | supports | Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment. |
| septin-record-glyoxysomal_membrane | data/structures/membrane_organelle/glyoxysomal_membrane.yaml; Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e | supports | Read identity, definition, hierarchy/parthood, synonyms/xrefs, components and examples, taxonomic/canonical scope, functions, all evidence and graph edges, discussions/history. No maintained images, physical measurements, traits or verbatim snippets are declared. |
| septin-original-glyoxysomal_membrane | reviews/structured/20261022T014701Z-glyoxysomal-membrane-audit/review.yaml; Complete immutable original YAML/Markdown, frozen inputs, checks, assessments, findings/actions and source limits | supports | Historical checks and source access remain historical. Original scientific finding identities are preserved where applicable; all five originals contain explicit imodulondb exclusions. Whole glycosome is stale; the other four target inputs are unchanged. |
| septin-original-validation-glyoxysomal_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json; 20261022T014701Z-glyoxysomal-membrane-audit native validate/render and historical-source hash | supports | Native validate and render exit zero; original Markdown is byte-identical. Historical-source hash equals the frozen original. Current staleness status is False. |
| septin-native-glyoxysomal_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-verify-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-verify.log | supports | Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment. |
| septin-native-glyoxysomal_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-causal-receipt.json; Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-causal.log | supports | Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN nodes are represented. Exit zero validates this empty represented inventory only; pathway/import claims require separate scientific source assessment. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015,GO:0034468,GO:0046860,GO:0005777,GO:0005778,GO:0043233,GO:0031908,GO:0046861,GO:0009514,GO:0006097,GO:0005782; Eleven exact current active GO terms and typed child edges | supports | Exact whole glycosome/lumen/membrane and glyoxysome/lumen/membrane identities are distinct. Whole organelles subclass peroxisome, membranes subclass peroxisomal membrane and lumens subclass peroxisomal matrix. GO0046860/0046861 denote assembled lipid bilayers, not a chemical lipid class. GO0006097 is the glyoxylate cycle. Native plant-oriented glyoxysome examples do not independently establish fungal occurrence. |
| septin-ancestors-0020015 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015/ancestors?relations=is_a; Exact GO ancestors endpoint with relations=is_a only | supports | Glycosome is_a peroxisome GO0005777. This establishes ancestry rather than a falsely asserted direct edge or mixed parthood path. |
| septin-ancestors-0034468 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034468/ancestors?relations=is_a; Exact GO ancestors endpoint with relations=is_a only | supports | Glycosome lumen has broad GO0043233 is_a ancestry through peroxisomal matrix. This establishes ancestry rather than a falsely asserted direct edge or mixed parthood path. |
| septin-ancestors-0031908 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031908/ancestors?relations=is_a; Exact GO ancestors endpoint with relations=is_a only | supports | Glyoxysomal lumen has broad GO0043233 is_a ancestry through peroxisomal matrix. This establishes ancestry rather than a falsely asserted direct edge or mixed parthood path. |
| septin-tax5653 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653; Exact ENA taxId, scientificName, rank, lineage and synonyms | supports | Class Kinetoplastea; Kinetoplastida is a synonym, explaining the legacy order wording. Experimental strains and life stages are not inferred from a reference accession taxon. |
| septin-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Exact ENA taxId, scientificName, rank, lineage and synonyms | supports | Species Trypanosoma brucei. Experimental strains and life stages are not inferred from a reference accession taxon. |
| septin-tax5702 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5702; Exact ENA taxId, scientificName, rank, lineage and synonyms | supports | Subspecies Trypanosoma brucei brucei. Experimental strains and life stages are not inferred from a reference accession taxon. |
| septin-tax31285 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/31285; Exact ENA taxId, scientificName, rank, lineage and synonyms | supports | Subspecies Trypanosoma brucei gambiense. Experimental strains and life stages are not inferred from a reference accession taxon. |
| septin-tax185431 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431; Exact ENA taxId, scientificName, rank, lineage and synonyms | supports | Reference strain Trypanosoma brucei brucei TREU927;927/4 GUTat10.1 is a synonym. Experimental strains and life stages are not inferred from a reference accession taxon. |
| septin-tax5141 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141; Exact ENA taxId, scientificName, rank, lineage and synonyms | supports | Species Neurospora crassa. Experimental strains and life stages are not inferred from a reference accession taxon. |
| septin-SL-0128 | https://rest.uniprot.org/locations/SL-0128.json; Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing parents | supports | Glycosome membrane maps directly to GO0046860, has glycosomal membrane synonym, is_a peroxisomal membrane and part_of glycosome. Nested parent mappings are not additional exact matches. |
| septin-SL-0129 | https://rest.uniprot.org/locations/SL-0129.json; Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing parents | supports | Whole glycosome maps directly to GO0020015 and is_a peroxisome; glucose/glycerol enzymes and examined kinetoplastid scope are authority synthesis. Nested parent mappings are not additional exact matches. |
| septin-SL-0332 | https://rest.uniprot.org/locations/SL-0332.json; Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing parents | supports | Glycosome matrix maps directly to GO0034468, supplies lumen/matrix synonyms and is part_of glycosome. Nested parent mappings are not additional exact matches. |
| septin-SL-0130 | https://rest.uniprot.org/locations/SL-0130.json; Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing parents | supports | Glyoxysome membrane maps directly to GO0046861 and has glyoxysomal membrane synonym, peroxisomal membrane parent and whole-organelle parthood. Nested parent mappings are not additional exact matches. |
| septin-SL-0131 | https://rest.uniprot.org/locations/SL-0131.json; Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing parents | supports | Whole glyoxysome maps directly to GO0009514; its plant/catalase-oriented narrative must not be transferred uncritically to Neurospora. Nested parent mappings are not additional exact matches. |
| septin-SL-0333 | https://rest.uniprot.org/locations/SL-0333.json; Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing parents | supports | Glyoxysome matrix maps directly to GO0031908, supplies lumen/matrix synonyms and is part_of glyoxysome. Nested parent mappings are not additional exact matches. |
| septin-protein-P13377 | https://rest.uniprot.org/uniprotkb/P13377.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | P13377: Glucose-6-phosphate isomerase, glycosomal; UniProtKB reviewed (Swiss-Prot); taxon5702; indexed genes['PGI']. Identity and current annotation do not alone certify accession-specific localization or biological necessity. |
| septin-protein-O15648 | https://rest.uniprot.org/uniprotkb/O15648.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | O15648: ATP-dependent 6-phosphofructokinase; UniProtKB reviewed (Swiss-Prot); taxon5702; indexed genes['pfk']. Identity and current annotation do not alone certify accession-specific localization or biological necessity. |
| septin-protein-A0A3G1VTN5 | https://rest.uniprot.org/uniprotkb/A0A3G1VTN5.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | A0A3G1VTN5: Phosphotransferase; UniProtKB unreviewed (TrEMBL); taxon5702; indexed genes['Hk1']. Identity and current annotation do not alone certify accession-specific localization or biological necessity. |
| septin-protein-O96429 | https://rest.uniprot.org/uniprotkb/O96429.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | O96429: Glyceraldehyde-3-phosphate dehydrogenase; UniProtKB unreviewed (TrEMBL); taxon31285; indexed genes['GAPDH']. Unreviewed fragment; automatic family annotation is not an accession-specific localization experiment. |
| septin-protein-Q4GZG4 | https://rest.uniprot.org/uniprotkb/Q4GZG4.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | Q4GZG4: Phosphoglycerate kinase; UniProtKB unreviewed (TrEMBL); taxon185431; indexed genes['PGKC']. Identity and current annotation do not alone certify accession-specific localization or biological necessity. |
| septin-protein-P04789 | https://rest.uniprot.org/uniprotkb/P04789.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | P04789: Triosephosphate isomerase, glycosomal; UniProtKB reviewed (Swiss-Prot); taxon5702; indexed genes[]. TIM is a recommended protein short name, with no indexed geneName; it is not a newly verified gene-index field. Glycosomal localization is corroborated separately by primary enzyme evidence. |
| septin-protein-Q57W55 | https://rest.uniprot.org/uniprotkb/Q57W55.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | Q57W55: Glycosomal targeting signal receptor; UniProtKB reviewed (Swiss-Prot); taxon185431; indexed genes['PEX5']. Primary-cited cytosolic receptor/cycling context is not permanent membrane residency. |
| septin-protein-Q57W97 | https://rest.uniprot.org/uniprotkb/Q57W97.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | Q57W97: Glycosomal targeting signal 2 receptor; UniProtKB reviewed (Swiss-Prot); taxon185431; indexed genes['PEX7']. Cytosolic localization has primary support; glycosome-matrix annotation includes by-similarity evidence. |
| septin-protein-Q38CL4 | https://rest.uniprot.org/uniprotkb/Q38CL4.json; Exact accession/status/name/gene/organism and relevant family, localization and evidence-code fields | supports | Q38CL4: Glycosomal membrane protein PEX14; UniProtKB reviewed (Swiss-Prot); taxon185431; indexed genes['PEX14']. Exact PEX14 identity and primary-cited membrane annotation; large-pore dimensions and some translocation details are by similarity and are not promoted to direct trypanosome measurements. |
| septin-reviewed-TIM | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATIM%20AND%20taxonomy_id%3A5691%20AND%20reviewed%3Atrue&amp;format=json&amp;size=100; Complete bounded UniProt search response | supports | The literal indexed-gene query returns zero; this is not absence of the protein or its functional alias. |
| septin-reviewed-TIM-protein-alias | https://rest.uniprot.org/uniprotkb/search?query=protein_name%3A%22triosephosphate%20isomerase%22%20AND%20taxonomy_id%3A5702%20AND%20reviewed%3Atrue&amp;format=json&amp;size=100; Complete bounded UniProt search response | supports | The complementary exact taxon/reviewed protein-name query returns only P04789, whose recommended short name is TIM. This substantiates the added example while preserving the lack of indexed geneName. |
| septin-IPR024111 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024111/; Current accession/type/name and only non-LLM authority description | supports | Native family PEX5/PEX5L family is distinct from the other peroxin families. The exact current protein Q57W55 carries the corresponding InterPro xref. No one of these families denotes the whole multi-protein import apparatus; no uninspected complex identity or fixed stoichiometry is asserted. |
| septin-IPR044536 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044536/; Current accession/type/name and only non-LLM authority description | supports | Native family PEX7 family is distinct from the other peroxin families. The exact current protein Q57W97 carries the corresponding InterPro xref. No one of these families denotes the whole multi-protein import apparatus; no uninspected complex identity or fixed stoichiometry is asserted. |
| septin-IPR025655 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR025655/; Current accession/type/name and only non-LLM authority description | supports | Native family PEX14 family is distinct from the other peroxin families. The exact current protein Q38CL4 carries the corresponding InterPro xref. No one of these families denotes the whole multi-protein import apparatus; no uninspected complex identity or fixed stoichiometry is asserted. |
| septin-PMID142663 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A142663%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and metadata only; no abstractText | supports | Opperdoes and Borst1977, DOI10.1016/0014-5793(77)80476-6, exact title states localization of nine glycolytic enzymes. Native record has no abstract; detailed original fractionation tables/body were not inspected. |
| septin-PMID2940090 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A2940090%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | Misset, Bos and Opperdoes1986; complete primary abstract directly reports purification of nine enzymes from crude glycosomes, including phosphofructokinase and triosephosphate isomerase. This supports enzyme-cohort membership, not identity of every modern accession/strain or one assembled enzyme complex. |
| septin-PMID10589985 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10589985%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | de Walque et al.1999: complete primary abstract reports PEX5 primarily cytosolic and in-vitro binding to PGK-C, consistent with receptor cycling. |
| septin-PMID17320990 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A17320990%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | Galland et al.2007: complete primary abstract reports PEX5/PEX7 receptor interaction/import phenotypes and apparently intact procyclic glycosomes by EM after depletion. Growth/import requirement is distinct from organelle-formation necessity. |
| septin-PMID23994617 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A23994617%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | Gualdron-Lopez et al.2013: complete primary abstract reports cytosolic monoubiquitinated PEX5 and PEX4 recycling biology; it does not place all PEX5 permanently in the membrane. |
| septin-PMID12386344 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12386344%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | Furuya et al.2002: complete primary abstract identifies PEX14 docking factor and RNAi-dependent import defects/sugar-conditional procyclic toxicity. Detailed localization is assessed separately from its primary body. |
| septin-PMID12709066 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12709066%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | Moyersoen is first author and Choe second for DOI10.1046/j.1432-1033.2003.03582.x. Complete primary abstract supports glycosomal PEX14, N-terminal PEX5 binding and PTS1/PTS2/I-PTS matrix mislocalization after RNAi in bloodstream and procyclic forms; viability is not formation necessity. |
| septin-PMID22809509 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A22809509%20AND%20SRC%3AMED&amp;pageSize=25; Exact MED PMID, DOI, ordered authors, title and complete primary abstractText | supports | Verplaetse et al.2012: complete primary abstract describes PEX13.1/PEX13.2 docking complex and PEX13.1 anchoring or positioning PEX14. Cytosolic receptors and membrane docking apparatus are distinct participants. |
| septin-haanstra2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0806664105&amp;pageSize=25; Exact DOI/PMID/title/authors and complete primary abstract | supports | Haanstra et al.2008; primary abstract reports Glc6P accumulation and stronger glycerol/GK rescue support. The body qualifies the glucose mechanism. |
| septin-haanstra2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.bbamcr.2015.09.015&amp;pageSize=25; Exact DOI/PMID/title/authors and complete review abstract | supports | Haanstra et al.2016 is a secondary review. Complete review abstract supports specialized kinetoplastid peroxisomes, variable glycolytic enzyme content, peroxin import and life-stage remodeling; it is not a freshly inspected primary experiment. |
| septin-bauer2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pntd.0005333&amp;pageSize=25; Exact DOI/PMID/title/authors and complete review abstract | supports | Bauer and Morris2017 is a secondary review. Its complete abstract presents ER-derived de novo glycosome biogenesis as a supported hypothesis, not directly demonstrated at that time; no membrane-origin mechanism is added. |
| septin-dezoysa1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1007/BF00309930&amp;pageSize=25; Exact DOI/PMID/title/authors and complete primary abstract | supports | de Zoysa and Connerton1994; complete primary abstract directly demonstrates C-terminally modified CAT reporter targeting under nutritional acetate induction in Neurospora crassa, distinguishes glyoxysomes carrying glyoxylate-cycle enzymes from catalase-containing peroxisome-like microbodies, and reports sequence-dependent targeting with ARM ineffective. This is the current abstract tier, not a current full-body or direct translocation movie inspection. |
| septin-opperdoes1977-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/0014-5793%2877%2980476-6&amp;pageSize=25; Exact DOI query returned zero; separate native PMID retrieval succeeded | supports | This DOI-index miss is not publication absence. Native PMID142663 independently verifies DOI/title/authors; no abstract is available there. |
| septin-haanstra2008-pmc | https://pmc.ncbi.nlm.nih.gov/articles/2584722/; Complete Results sec1/sec2–4 with Fig2–5 captions, Discussion sec5, Experimental Procedures sec6/sec7–13; no source pixels, separate supplements or raw data | supports | Fresh genuine PMC body: procyclic29–13 PEX14-RNAi cells accumulate Glc6P after glucose, but the paper explicitly calls that an unstringent mechanism test because preferential PGI mislocalization can truncate the pathway; PF449 did not significantly accumulate Glc6P. Glycerol/Gly3P accumulation plus GK-knockdown rescue supplies the stronger test. TIM activity partially mislocalizes on digitonin fractionation. Models removing a membrane are distinct from biological partial-import perturbations; reference-strain protein examples are not the experimental strains. |
| septin-furuya2002-pmc | https://pmc.ncbi.nlm.nih.gov/articles/137857/; Complete Materials and Methods sec1/sec2–7, Results sec8/sec9–13 including Fig1–4 captions, and Discussion sec14; no pixels/raw data | supports | Fresh genuine PMC body supports PEX14 glycosomal membrane association by fractionation, carbonate extraction and punctate immunostaining; RNAi causes matrix-protein mislocalization and context-dependent lethality. Procyclic29–13 and bloodstream single-marker assays, recombinant EATRO110 sequence material and engineered E.coli protein expression are distinct. Proposed metabolic explanations and cross-species extension are not directly measured universals. |
| septin-access-haanstra2008-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2584722.1/PMC2584722.1.xml; Actual source-route error retained in scratch source-receipts.json | context_only | &lt;HTTPError 404: 'Not Found'&gt;; not scientific body evidence. Successful alternative bodies or metadata are separately scoped. |
| septin-access-furuya2002-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC137857.1/PMC137857.1.xml; Actual source-route error retained in scratch source-receipts.json | context_only | &lt;HTTPError 404: 'Not Found'&gt;; not scientific body evidence. Successful alternative bodies or metadata are separately scoped. |
| septin-access-opperdoes1977-pdf | https://febs.onlinelibrary.wiley.com/doi/pdf/10.1016/0014-5793%2877%2980476-6; Actual source-route error retained in scratch source-receipts.json | context_only | &lt;HTTPError 403: 'Forbidden'&gt;; not scientific body evidence. Successful alternative bodies or metadata are separately scoped. |
| septin-dezoysa1994-pdf | https://link.springer.com/content/pdf/10.1007/BF00309930.pdf; Publisher PDF route returned HTML Client Challenge despite HTTP200 | context_only | This is not a genuine PDF/article body. Current scientific support uses the complete primary abstract; the original review full-PDF claim remains historical and is not reused as a new body inspection. |
| septin-dezoysa1994-encoded-pdf | https://link.springer.com/content/pdf/10.1007%2FBF00309930.pdf; Publisher PDF route returned HTML Client Challenge despite HTTP200 | context_only | This is not a genuine PDF/article body. Current scientific support uses the complete primary abstract; the original review full-PDF claim remains historical and is not reused as a new body inspection. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue and actual target taxon scope | supports | No matched Trypanosoma, kinetoplastid or Neurospora host/dataset appears. All five complete records assert glycolysis/PEX import or glyoxylate-cycle/matrix-targeting pathways, so all require an applicability assessment even where their graphs are topological. No matched-host downstream gene/module query applies; heterologous E.coli protein expression is not the target organism. Catalogue noncoverage is not biological absence. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical canary datasets invocation00:49:00.848907Z–00:49:00.863225Z | context_only | Actual earlier exit1 PermissionError reading pyvenv.cfg. No fresh runner invocation/success is claimed; current official-catalogue fallback is a separate retrieval. |
| septin-glyoxysome-neighbor | data/structures/membrane_organelle/glyoxysome.yaml; Frozen whole-glyoxysome neighbor, boundary/identity context only | supports | Whole organelle, lumen and membrane identities/parthood are distinct. This context read does not independently review the whole-neighbor composition or dispose of its historical findings. |
| septin-stale-glycosome-diff | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/glycosome-stale.diff; Exact original-source to current-source diff | supports | Only scientific changes are addition of reviewed P04789/TIM example and peroxin apparatus PROTEIN to PROTEIN_COMPLEX retyping, plus associated history. Neither inherited attribution, glucose-mechanism qualification nor membrane molecular-grounding issue is fixed by those changes. |
| septin-historical-2462 | https://github.com/CultureBotAI/CellStructureMech/issues/2462; Current root-fetched issue body item4 and closure comment; historical context only | context_only | Closed grouped issue2462 includes the glycosome peroxin-type change alongside unrelated records. Closure cites PR2464/commit31fd33d9556ea5627b36d50ab608ccb9464f9353. This review checks the current glycosome change without newly resolving the entire group or reopening that peroxin item. |
| septin-source-access | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/source-receipts.json; Actual fresh source URLs/statuses/access timestamps/hashes | supports | Primary PMC bodies and complete abstract/authority tiers are separated. Two S3 XML routes returned404; canonical PMC routes yielded genuine bodies. Springer PDF routes yielded challenges, and Opperdoes publisher route403; current body access is not inferred from success status alone. |
| septin-common-policy-reuse | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/common-policy-hash-reuse.json; Seventeen frozen common policy/schema/native source byte comparisons | supports | Current common bytes match prior read inputs; structured-source and component/schema rules additionally reread. Only the explicitly frozen glyoxysome neighbor was added to this slice. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2366 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Flagellar pocket and food vacuole independent subreview: Assigned flagellar pocket and food vacuole only. One inherited major F1 remains open with exact original key/severity/repository-review-finding lineage. Food-vacuole stale membrane-node/bounds-edge delta is substantively refreshed; no scientific record correction or terminal neighbor/group/category disposition is claimed.
- Flagellar pocket and food vacuole independent subreview: Fresh Lacomble primary body scope: Resultssec3/4, Methodssec10, selected Introduction/Discussion paragraphs citing Bonhivers/BILBO1. Gadelha: Resultssec2/3/5/6 and Methodssec12. Bonhivers publisher XML:s2a/s2b/s2c/s3a/s3d/s4a/s4e/s4i. Captions read as text, no primary figure pixels, raw tomograms, movies or supplements inspected. Unlisted sections not certified.
- Flagellar pocket and food vacuole independent subreview: Lacomble procyclic427, Gadelha bloodstream forms and Bonhivers distinct genomic/procyclic/bloodstream lines remain separate contexts. New-pocket RNAi necessity is not universal collar-constituent necessity or total loss of old pockets; cell-cycle duplication is retained.
- Flagellar pocket and food vacuole independent subreview: Field2009/Halliday2021 are secondary review abstracts only. Cowman1991/Lamarque2008 are complete primary abstracts only. Lamarque MED PMID21136929 selected from two DOI results; FV enrichment does not imply pure/exhaustive/necessary inventory. No uninspected full-body or pixel claim for these sources.
- Flagellar pocket and food vacuole independent subreview: Wiser2024 is secondary review body, sections3.2/Table2 and4/4.1/4.2/4.3/Fig2caption. Boundary topology and broad digestion/hemozoin functions are supported; precise transporter direction, lipid composition and hemozoin molecular mechanism are not freshly demonstrated by this review.
- Flagellar pocket and food vacuole independent subreview: Both targets lack accession protein_examples and typed GENE_OR_PROTEIN nodes; four actual native commands pass within that empty-inventory scope. Positive BILBO1/trafficking and hemoglobin/heme/transporter narratives still trigger source applicability.
- Flagellar pocket and food vacuole independent subreview: Fresh official catalogue has no matching T. brucei or P. falciparum host; no matched downstream gene/module query or unrelated-host proxy applies. Noncoverage is not negative biological evidence. Historical runner failure remains actual00:49Z unavailable, not a current invocation or success.
- Flagellar pocket and food vacuole independent subreview: Two frozen neighbors were read only for membrane/material/collar identity and boundary context. Their other protein accessions/claims are not certified or terminally resolved. Root owns global QC, issues and publication; no repository/GitHub/record writes by this reviewer.
- Fungal-type vacuole, lumen and membrane independent subreview: Fungal-vacuole slice: three full records and original pairs independently reviewed, one stale whole target substantively refreshed. No scientific curation finding or predecessor disposition; original three findings/actions lists are empty. Three original expression-only adapter exclusions are concrete bundle defects, not missing optional scientific fields.
- Fungal-type vacuole, lumen and membrane independent subreview: Source tier: Li/Kane2009 is secondary review, complete sections2.1/4.2/5.1/6.1/6.2 and included captions read. Kane2006 is secondary review, complete Introduction/structure/a-isoform targeting sections and caption read. Historical subunit counts are not certified as current composition; underlying primary experiments are not all reanalyzed.
- Fungal-type vacuole, lumen and membrane independent subreview: Primary tier: Huh2003 and Matsumoto2013 complete abstracts/bibliography only; exact P00729 ECO citation attribution is independently checked in native UniProt. Parzych2018 Resultssec3/4, Discussionsec7, Methodssec9/11 including Tables1/2 and embedded captions read. No fresh figure pixels, movies or supplementary dataset inspection; no target image asset exists. SEY6210 experimental derivatives are not equated with reference S288C.
- Fungal-type vacuole, lumen and membrane independent subreview: Biological limits: COMMON is qualitative, not prevalence. Soluble protease localization differs from transient degradative cargo; partial functional redundancy precludes individual assembly necessity. Lumen actors are not forced into component material, and lipid boundary essentiality is not every lipid-species necessity.
- Fungal-type vacuole, lumen and membrane independent subreview: Structured-source limits: all three records trigger applicability by their actual protein/pathway assertions. Fresh official catalogue has no Saccharomyces strain match; no unmatched bacterial proxy or biological absence claim. Actual00:49Z runner unavailable receipt is historical, not a current invocation. Initial sandbox DNS attempts archived; subsequent permitted fresh downloads succeeded. Root20/10etc corpus gates and futureCI are not borrowed into this source report.
- Fungal-type vacuole, lumen and membrane independent subreview: Local provenance: applicable instructions/profile/config/rubrics reread; graph/protein schema and command recipe sections inspected. Native schema/helper bytes were used in validation, not a full program correctness audit. Root owns remaining cohort/global gates/issue publication; this reviewer made no repository or GitHub mutation.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Five complete assigned targets and their ten original artifacts reviewed. Whole glycosome is stale: reviewed P04789/TIM was added and peroxin import machinery retyped PROTEIN_COMPLEX. Both changes are substantively reassessed; other four target hashes are unchanged. Original validation/render passes and historical evidence/checks remain immutable.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Four inherited scientific occurrences retain exact stable keys, native severities and repository/review/finding lineage: whole glycosome first-author, glucose mechanism and whole-membrane molecular grounding; glycosome membrane first-author. No additional confirmed typing finding is established: the narrower enum prose must be read alongside explicit family-or-class and generic-class guidance. The record discloses the heterogeneous class and UNKNOWN formation necessity; no automatic complex conversion or invented predecessor is asserted.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: All current public sources were freshly fetched. Haanstra2008 complete Results/Discussion/main Experimental Procedures and Fig2–5 captions, and Furuya2002 complete Methods/Results/Discussion and Fig1–4 captions were read. No source pixels, separate supplements/raw data or quantitative reanalysis is claimed. Failed S3 routes are not body evidence.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Opperdoes1977 exact PMID metadata/title only; no abstract and publisher403. Its DOI search zero is not absence. Misset1986, Moyersoen2003, de Walque1999, Galland2007, Gualdron-Lopez2013 and Verplaetse2012 are complete-primary-abstract tiers only. Haanstra2016 and Bauer2017 are complete secondary review abstracts, not primary experiments.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Current de Zoysa1994 evidence is complete primary abstract only. Both publisher PDF routes returned HTML Client Challenge despite200; the historical original full-PDF review is not a current body reread. Abstract supports acetate-induced fungal CAT reporter targeting and pathway compartments; detailed old medium/strain/table/ICL statements are not newly certified.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Glucose-associated Glc6P accumulation in29–13 does not uniquely resolve the mechanism: PGI truncation remains an alternative and PF449 differs. Glycerol/Gly3P plus GK rescue is the stronger test. Model membrane removal, partial biological import defects, cell viability and organelle-formation necessity remain distinct.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Nine whole-glycosome examples comprise six reviewed and three unreviewed; GAPDH O96429 is a fragment. TIM is protein alias without indexed geneName; literal gene query zero is not protein absence. Reference strain/subspecies entries are not the experimental strains. Automated/by-similarity annotations are not direct localization evidence.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Peroxin apparatus type refresh is bounded to interacting import machinery, not a permanent stoichiometric assembly or membrane residence of every receptor. Closed2462 item4 is historical context only and is not reopened or newly disposed of across its other targets. The heterogeneous glycolytic set is not automatically a complex.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: All ten assigned native protein commands pass. Whole glycosome has nine examples/two COVERED nodes; membrane has no examples but one UNANCHORED_WITH_UNIPROT Q38CL4 node; other three have empty inventories/zero nodes. Identifier success does not certify semantic typing, mechanism, complete composition or necessity.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: All five narratives trigger pathway/molecular applicability despite some descriptive graphs. Fresh official catalogue has no actual target-host coverage; no unrelated or heterologous-host downstream query or biological absence inference. Historical runner failure remains00:49Z, not a fresh invocation.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Thirty-three local inputs were used:17 common unchanged policy/schema/native files, five targets, ten originals and frozen whole glyoxysome neighbor. The neighbor supplies boundary context only, not a complete scientific review or disposition. No maintained image, physical measurement, trait or verbatim snippet is present in assigned targets.
- Glycosome trio and glyoxysomal lumen/membrane independent subreview: Root owns global QC/CI, issue dedup/publication and repository/GitHub mutations. This report does not pre-certify final-head or queue outcomes. Record curation remains separate; no record or original bundle was edited.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Inherited scientific findings retain stable keys and exact predecessor repository/review/finding identities.
- Issue #2695 tracks three stale target inputs. Food vacuole adds a membrane STRUCTURE node/component_ref and enclosing boundary edge; fungal-type vacuole adds direct lumen/membrane part-of edges supported by current GO graph evidence; glycosome adds P04789/TIM and retypes peroxin machinery to PROTEIN_COMPLEX. All deltas receive substantive source and native-policy reassessment.
- Issue #2696 tracks ten unsupported applicability exclusions. Every original bundle has an explicit imodulondb not_applicable row; none omits it. Positive BILBO1/trafficking, hemoglobin/heme, hydrolase/V-ATPase, glycolysis/peroxin-import or glyoxylate-cycle/import assertions require coverage assessment despite narrow compartment titles or empty represented protein inventories.
- Source commit 85122489fca6bd0f63b1a6b276d138f847405e3e is retained by tag review-base/pr2366-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 50 local inputs were frozen before assessment. Ciliary-pocket membrane, ciliary-pocket collar and whole glyoxysome are bounded context only, not extra review targets or dispositions of their findings.
- Fresh and reused source snapshots retain actual access timestamps and inspection tiers. Authority identity does not independently establish structure membership, mechanistic action, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Fungal-type vacuole has three reviewed hydrolase examples and one COVERED node; its lumen has no component examples and one UNANCHORED_WITH_UNIPROT hydrolase-cohort node carrying those three accessions. Glycosome has nine examples (six reviewed and three unreviewed) and two COVERED nodes; glycosome membrane has no component examples and one UNANCHORED_WITH_UNIPROT PEX14 node. The other six records have empty inventories and zero typed molecular nodes. Transient xref-backed actors are distinguished from component coverage; checks do not certify every narrative claim.
- Closed grouped issue #2462 is historical context for the glycosome peroxin component-type change. This follow-up makes no disposition of other records or grouped findings covered there. Native-validator issue #2514 remains open and reused.
- Five inherited scientific findings remain: a major flagellar-pocket whole-membrane versus lipid grounding error; glycosome first-author attribution, qualified glucose-mechanism scope and major whole-membrane versus molecular-lipid grounding; and glycosome-membrane first-author attribution. Three targets need curation; the other seven have qualified positive assessments.
- A proposed additional glycosome enzyme-cohort typing defect was independently challenged against native class-level component guidance and was not established as a confirmed record error. The record explicitly describes a heterogeneous class. The narrower enum wording does not justify inventing a single family or automatically asserting a protein complex; no new scientific issue is claimed for that hypothesis.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T142655Z-pr2366-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2366: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T14:09:49.269959Z'
finished_at: '2026-11-03T14:26:55Z'
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
summary: Current-input reassessment of all ten records in PR2366. Three stale reviews
  are substantively refreshed and all ten structured-source applicability exclusions
  are corrected. Five inherited scientific findings, two major and three minor, remain
  open for separate record curation; no records are edited.
source:
  git_revision: 85122489fca6bd0f63b1a6b276d138f847405e3e
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
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
    role: context
  - path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
    role: context
  - path: data/structures/membrane_organelle/flagellar_pocket.yaml
    sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
    role: target
  - path: data/structures/membrane_organelle/food_vacuole.yaml
    sha256: 834e2ee1d3c5f37ca9f20f2541cccfcc755cc94621c864ab84c0a4687a2baa1f
    role: target
  - path: data/structures/membrane_organelle/fungal_type_vacuole.yaml
    sha256: 1dc8607faa4099575b74222bd6303877b27107ec0d2bbdcf13ceadbb839e4559
    role: target
  - path: data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    sha256: ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa
    role: target
  - path: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    sha256: 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51
    role: target
  - path: data/structures/membrane_organelle/glycosome.yaml
    sha256: c31397edde14cca6a35fa8574d38fdd77f1c6d49bbe95f145d6f1a8e872b033b
    role: target
  - path: data/structures/membrane_organelle/glycosome_lumen.yaml
    sha256: 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544
    role: target
  - path: data/structures/membrane_organelle/glycosome_membrane.yaml
    sha256: 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9
    role: target
  - path: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
    sha256: 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b
    role: target
  - path: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
    sha256: acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c
    role: target
  - path: data/structures/membrane_organelle/glyoxysome.yaml
    sha256: 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4
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
  - path: reviews/structured/20261022T014651Z-flagellar-pocket-audit/review.md
    sha256: 86b1495dde137507d45f3b9b0be32c18f2dcf90cc4c1b0c8f1ea6389ae937c47
    role: context
  - path: reviews/structured/20261022T014651Z-flagellar-pocket-audit/review.yaml
    sha256: 46cb98fedbbaff173393ad6a2ced8782d58b876915db382a2c3b623dfb9b4560
    role: context
  - path: reviews/structured/20261022T014653Z-food-vacuole-audit/review.md
    sha256: 210b156ab1aaaa95c2bf798eb2608d369d96b875ac049e1504e0a0c96ccad201
    role: context
  - path: reviews/structured/20261022T014653Z-food-vacuole-audit/review.yaml
    sha256: ce9ba4330d8490f16df6ad28334cb4a2c4f35edf3ec536a91ada7bddf5218a20
    role: context
  - path: reviews/structured/20261022T014654Z-fungal-type-vacuole-audit/review.md
    sha256: 9f32825b7c561d31ef898960a46f2411ef7b6cb5753b020638e58816a08e6fb2
    role: context
  - path: reviews/structured/20261022T014654Z-fungal-type-vacuole-audit/review.yaml
    sha256: 66b07afcf055b463e47b79f4eb078abc6122ad4d2cbb69bd299ed1f63ca40ad6
    role: context
  - path: reviews/structured/20261022T014656Z-fungal-type-vacuole-lumen-audit/review.md
    sha256: 0e1091045da9a3f9d805bb38e286c8035b709c38b14614f4ad437c0f4f0b6f87
    role: context
  - path: reviews/structured/20261022T014656Z-fungal-type-vacuole-lumen-audit/review.yaml
    sha256: 1970ed9588a167cae819f4b54e21827cf8164249c72c1db0d495398959ae897f
    role: context
  - path: reviews/structured/20261022T014657Z-fungal-type-vacuole-membrane-audit/review.md
    sha256: 87c7ec945a186aa3aa57d6baf19378b905046039367184a36d810e9dfcf4141b
    role: context
  - path: reviews/structured/20261022T014657Z-fungal-type-vacuole-membrane-audit/review.yaml
    sha256: 6efd353f4896fd9eeea03d0fd3d30a6fb77a86e0880bb4ea459eb64e0483e3bc
    role: context
  - path: reviews/structured/20261022T014658Z-glycosome-audit/review.md
    sha256: 16468b6a1c7f0c2f4113f19857d1821c1df672dc730b63093e6d6b7be6465e0b
    role: context
  - path: reviews/structured/20261022T014658Z-glycosome-audit/review.yaml
    sha256: 8ea631570b73dc73401a34b5e1bb6b5cf02f343bd7fa89904157bab132f516ae
    role: context
  - path: reviews/structured/20261022T014659Z-glycosome-lumen-audit/review.md
    sha256: 5d0a820bc22a67bb330aca3f1bae0ee21d0cdaaac0546835db2937545c1543ca
    role: context
  - path: reviews/structured/20261022T014659Z-glycosome-lumen-audit/review.yaml
    sha256: 8134befc132637c75f7238a344ae6ce7ddbc480255a12d907dccef43316ba2c0
    role: context
  - path: reviews/structured/20261022T014700Z-glycosome-membrane-audit/review.md
    sha256: d04b732e203c5924f6faefccd55056f431658e78352a19645d9e6a67bbc025b4
    role: context
  - path: reviews/structured/20261022T014700Z-glycosome-membrane-audit/review.yaml
    sha256: c4621537888d3ce79555c9b131fff31164c239257a7bd710b908eefd6b38fead
    role: context
  - path: reviews/structured/20261022T014701Z-glyoxysomal-lumen-audit/review.md
    sha256: d25a9cc9241ca54236ce58de4c36a87dc80128464bce6109a56c7a72ef072166
    role: context
  - path: reviews/structured/20261022T014701Z-glyoxysomal-lumen-audit/review.yaml
    sha256: 85067fb611fad53ee12afb5cbc2381b874adad30e0aca26e31361cf81c182a02
    role: context
  - path: reviews/structured/20261022T014701Z-glyoxysomal-membrane-audit/review.md
    sha256: c04ecc27ced5cc15ba475c9b535469decdf3c929a3d22f990ca1182a18464652
    role: context
  - path: reviews/structured/20261022T014701Z-glyoxysomal-membrane-audit/review.yaml
    sha256: ae2795bd9041cfda615c1d2f8ce65eb87438740c7ac43afba007073346bd1c31
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
- target_id: GO:0020016
  path: data/structures/membrane_organelle/flagellar_pocket.yaml
  label: flagellar pocket
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/flagellar_pocket.yaml
    role: maintained scientific record
- target_id: GO:0020020
  path: data/structures/membrane_organelle/food_vacuole.yaml
  label: food vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/food_vacuole.yaml
    role: maintained scientific record
- target_id: GO:0000324
  path: data/structures/membrane_organelle/fungal_type_vacuole.yaml
  label: fungal-type vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/fungal_type_vacuole.yaml
    role: maintained scientific record
- target_id: GO:0000328
  path: data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
  label: fungal-type vacuole lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    role: maintained scientific record
- target_id: GO:0000329
  path: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  label: fungal-type vacuole membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    role: maintained scientific record
- target_id: GO:0020015
  path: data/structures/membrane_organelle/glycosome.yaml
  label: glycosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
- target_id: GO:0034468
  path: data/structures/membrane_organelle/glycosome_lumen.yaml
  label: glycosome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_lumen.yaml
    role: maintained scientific record
- target_id: GO:0046860
  path: data/structures/membrane_organelle/glycosome_membrane.yaml
  label: glycosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_membrane.yaml
    role: maintained scientific record
- target_id: GO:0031908
  path: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
  label: glyoxysomal lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
    role: maintained scientific record
- target_id: GO:0046861
  path: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
  label: glyoxysomal membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 31ddf488bda650f463921061d848027b8ebf74e9.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    51825f94f13ad8ed893319d04d4b4a8041b6a161.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 85122489fca6bd0f63b1a6b276d138f847405e3e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 85122489fca6bd0f63b1a6b276d138f847405e3e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 85122489fca6bd0f63b1a6b276d138f847405e3e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 85122489fca6bd0f63b1a6b276d138f847405e3e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 85122489fca6bd0f63b1a6b276d138f847405e3e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0020016
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just validate data/structures/membrane_organelle/flagellar_pocket.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0020016
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: just validate-strict data/structures/membrane_organelle/flagellar_pocket.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0020020
  status: passed
  required: true
  target_ids:
  - GO:0020020
  command: just validate data/structures/membrane_organelle/food_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0020020
  status: passed
  required: true
  target_ids:
  - GO:0020020
  command: just validate-strict data/structures/membrane_organelle/food_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0000324
  status: passed
  required: true
  target_ids:
  - GO:0000324
  command: just validate data/structures/membrane_organelle/fungal_type_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0000324
  status: passed
  required: true
  target_ids:
  - GO:0000324
  command: just validate-strict data/structures/membrane_organelle/fungal_type_vacuole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0000328
  status: passed
  required: true
  target_ids:
  - GO:0000328
  command: just validate data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0000328
  status: passed
  required: true
  target_ids:
  - GO:0000328
  command: just validate-strict data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0000329
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just validate data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0000329
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just validate-strict data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0020015
  status: passed
  required: true
  target_ids:
  - GO:0020015
  command: just validate data/structures/membrane_organelle/glycosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0020015
  status: passed
  required: true
  target_ids:
  - GO:0020015
  command: just validate-strict data/structures/membrane_organelle/glycosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0034468
  status: passed
  required: true
  target_ids:
  - GO:0034468
  command: just validate data/structures/membrane_organelle/glycosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0034468
  status: passed
  required: true
  target_ids:
  - GO:0034468
  command: just validate-strict data/structures/membrane_organelle/glycosome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0046860
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just validate data/structures/membrane_organelle/glycosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0046860
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: just validate-strict data/structures/membrane_organelle/glycosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0031908
  status: passed
  required: true
  target_ids:
  - GO:0031908
  command: just validate data/structures/membrane_organelle/glyoxysomal_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0031908
  status: passed
  required: true
  target_ids:
  - GO:0031908
  command: just validate-strict data/structures/membrane_organelle/glyoxysomal_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0046861
  status: passed
  required: true
  target_ids:
  - GO:0046861
  command: just validate data/structures/membrane_organelle/glyoxysomal_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0046861
  status: passed
  required: true
  target_ids:
  - GO:0046861
  command: just validate-strict data/structures/membrane_organelle/glyoxysomal_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366
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
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
  summary: 'All ten explicit expression-only exclusions are corrected based on the
    complete records: BILBO1 and endo/exocytosis, hemoglobin/heme processing, hydrolase/V-ATPase
    functions, glycolysis/peroxin import, and glyoxylate-cycle/import context. Official
    complete catalogue responses and bounded host/strain searches establish no matching
    coverage for the reviewed hosts. No foreign-host proxy or unsupported downstream
    query is used. Noncoverage is not biological absence. Historical adapter-runner
    unavailability retains its actual time and is not a fresh invocation.'
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-catalogue-api
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
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
  - plaque-tax-5691
  - plaque-tax5833
  - plaque-doi-10.1038_nrmicro2221
  - plaque-doi-10.1242_jcs.045740
  - plaque-doi-10.1073_pnas.0909289106
  - plaque-doi-10.1016_j.pt.2020.11.005
  - plaque-bonhivers2008-meta
  - plaque-cowman1991-meta
  - plaque-lamarque2008-meta
  - plaque-wiser2024-meta
  - plaque-pmc-PMC2714436
  - plaque-pmc-PMC2755463
  - plaque-bonhivers2008-plos
  - plaque-wiser2024-numeric
  - plaque-catalogue
  - micro-policy
  - micro-protein-contract
  - micro-graph-contract
  - micro-go
  - micro-ols-0000324
  - micro-ols-0000328
  - micro-ols-0000329
  - micro-ancestors-whole
  - micro-ancestors-membrane
  - micro-tax-4932
  - micro-tax-559292
  - micro-up-P07267
  - micro-up-P00729
  - micro-up-P09232
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-graph-policy
  - septin-protein-policy
  - septin-go
  - septin-ancestors-0020015
  - septin-ancestors-0034468
  - septin-ancestors-0031908
  - septin-tax5653
  - septin-tax5691
  - septin-tax5702
  - septin-tax31285
  - septin-tax185431
  - septin-tax5141
  - septin-SL-0128
  - septin-SL-0129
  - septin-SL-0332
  - septin-SL-0130
  - septin-SL-0131
  - septin-SL-0333
  - septin-protein-P13377
  - septin-protein-O15648
  - septin-protein-A0A3G1VTN5
  - septin-protein-O96429
  - septin-protein-Q4GZG4
  - septin-protein-P04789
  - septin-protein-Q57W55
  - septin-protein-Q57W97
  - septin-protein-Q38CL4
  - septin-IPR024111
  - septin-IPR044536
  - septin-IPR025655
  - septin-PMID142663
  - septin-PMID2940090
  - septin-PMID10589985
  - septin-PMID17320990
  - septin-PMID23994617
  - septin-PMID12386344
  - septin-PMID12709066
  - septin-PMID22809509
  - septin-haanstra2008-meta
  - septin-haanstra2016-meta
  - septin-bauer2017-meta
  - septin-dezoysa1994-meta
  - septin-haanstra2008-pmc
  - septin-furuya2002-pmc
  - septin-access-haanstra2008-jats
  - septin-access-furuya2002-jats
  - septin-access-opperdoes1977-pdf
  - septin-dezoysa1994-pdf
  - septin-dezoysa1994-encoded-pdf
  - septin-historical-2462
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
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
- check_id: flagellar_pocket-uniprot-verify
  name: Native flagellar pocket UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/flagellar_pocket.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative BILBO1/trafficking claims remain
    separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-flagellar_pocket-verify
- check_id: flagellar_pocket-uniprot-causal
  name: Native flagellar pocket UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020016
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/flagellar_pocket.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative BILBO1/trafficking claims remain
    separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-flagellar_pocket-causal
- check_id: food_vacuole-uniprot-verify
  name: Native food vacuole UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020020
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/food_vacuole.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; digestion/hemozoin and boundary claims
    remain separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-food_vacuole-verify
- check_id: food_vacuole-uniprot-causal
  name: Native food vacuole UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020020
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/food_vacuole.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; digestion/hemozoin and boundary claims
    remain separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-food_vacuole-causal
- check_id: fungal_type_vacuole-uniprot-verify
  name: Native fungal-type vacuole UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000324
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Three reviewed S. cerevisiae S288C
    examples PEP4/P07267, PRB1/P09232 and PRC1/P00729 are verified; one typed node
    is COVERED. Identity does not prove assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-fungal_type_vacuole-verify
- check_id: fungal_type_vacuole-uniprot-causal
  name: Native fungal-type vacuole UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000324
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Three reviewed S. cerevisiae S288C
    examples PEP4/P07267, PRB1/P09232 and PRC1/P00729 are verified; one typed node
    is COVERED. Identity does not prove assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-fungal_type_vacuole-causal
- check_id: fungal_type_vacuole_lumen-uniprot-verify
  name: Native fungal-type vacuole lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000328
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No component protein examples are
    represented; one UNANCHORED_WITH_UNIPROT hydrolase-cohort node carries verified
    P07267/P00729/P09232 xrefs. This is not full component coverage or individual
    necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-fungal_type_vacuole_lumen-verify
- check_id: fungal_type_vacuole_lumen-uniprot-causal
  name: Native fungal-type vacuole lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000328
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No component protein examples are
    represented; one UNANCHORED_WITH_UNIPROT hydrolase-cohort node carries verified
    P07267/P00729/P09232 xrefs. This is not full component coverage or individual
    necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-fungal_type_vacuole_lumen-causal
- check_id: fungal_type_vacuole_membrane-uniprot-verify
  name: Native fungal-type vacuole membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative V-ATPase acidification remains
    separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-fungal_type_vacuole_membrane-verify
- check_id: fungal_type_vacuole_membrane-uniprot-causal
  name: Native fungal-type vacuole membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; narrative V-ATPase acidification remains
    separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-fungal_type_vacuole_membrane-causal
- check_id: glycosome-uniprot-verify
  name: Native glycosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020015
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glycosome.yaml
    --verify
  exit_code: 0
  summary: 'Read-only native command returned zero. Nine protein examples are verified:
    six reviewed and three unreviewed, spanning glycolytic enzymes and peroxin machinery;
    two typed nodes are COVERED. TIM is assessed using the actual protein alias and
    primary context, not an invented UniProt indexed gene symbol. Membership and mechanism
    remain separate.'
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glycosome-verify
- check_id: glycosome-uniprot-causal
  name: Native glycosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020015
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glycosome.yaml
    --causal-graphs
  exit_code: 0
  summary: 'Read-only native command returned zero. Nine protein examples are verified:
    six reviewed and three unreviewed, spanning glycolytic enzymes and peroxin machinery;
    two typed nodes are COVERED. TIM is assessed using the actual protein alias and
    primary context, not an invented UniProt indexed gene symbol. Membership and mechanism
    remain separate.'
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glycosome-causal
- check_id: glycosome_lumen-uniprot-verify
  name: Native glycosome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034468
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glycosome_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; glycolytic narrative claims remain separately
    assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glycosome_lumen-verify
- check_id: glycosome_lumen-uniprot-causal
  name: Native glycosome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034468
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glycosome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; glycolytic narrative claims remain separately
    assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glycosome_lumen-causal
- check_id: glycosome_membrane-uniprot-verify
  name: Native glycosome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glycosome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. No component protein examples are
    represented; one UNANCHORED_WITH_UNIPROT PEX14 node carries verified Q38CL4. This
    is not full component coverage or proof of all import mechanism.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glycosome_membrane-verify
- check_id: glycosome_membrane-uniprot-causal
  name: Native glycosome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0046860
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glycosome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. No component protein examples are
    represented; one UNANCHORED_WITH_UNIPROT PEX14 node carries verified Q38CL4. This
    is not full component coverage or proof of all import mechanism.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glycosome_membrane-causal
- check_id: glyoxysomal_lumen-uniprot-verify
  name: Native glyoxysomal lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031908
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glyoxysomal_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; glyoxylate-cycle targeting claims remain
    separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glyoxysomal_lumen-verify
- check_id: glyoxysomal_lumen-uniprot-causal
  name: Native glyoxysomal lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031908
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glyoxysomal_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; glyoxylate-cycle targeting claims remain
    separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glyoxysomal_lumen-causal
- check_id: glyoxysomal_membrane-uniprot-verify
  name: Native glyoxysomal membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0046861
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glyoxysomal_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; matrix-import and glyoxylate-cycle context
    remain separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glyoxysomal_membrane-verify
- check_id: glyoxysomal_membrane-uniprot-causal
  name: Native glyoxysomal membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0046861
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/glyoxysomal_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Represented protein inventory and
    typed molecular-node coverage are empty; matrix-import and glyoxylate-cycle context
    remain separately assessed.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-glyoxysomal_membrane-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/membrane_organelle/flagellar_pocket.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8;
    current SHA256 d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8.
    Record bytes unchanged since the original review.
  snapshot_sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T014651Z-flagellar-pocket-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 46cb98fedbbaff173393ad6a2ced8782d58b876915db382a2c3b623dfb9b4560
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/membrane_organelle/food_vacuole.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 956ec0d47253c51f7931d89e9308f1be821836cb87de96410327f374e30d5ac0;
    current SHA256 834e2ee1d3c5f37ca9f20f2541cccfcc755cc94621c864ab84c0a4687a2baa1f.
    Changed record reassessed against current sources.
  snapshot_sha256: 834e2ee1d3c5f37ca9f20f2541cccfcc755cc94621c864ab84c0a4687a2baa1f
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T014653Z-food-vacuole-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ce9ba4330d8490f16df6ad28334cb4a2c4f35edf3ec536a91ada7bddf5218a20
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 d447fe7bc41bcf0749629f12affde731c10286f9efbb170efbf81bc27b975016;
    current SHA256 1dc8607faa4099575b74222bd6303877b27107ec0d2bbdcf13ceadbb839e4559.
    Changed record reassessed against current sources.
  snapshot_sha256: 1dc8607faa4099575b74222bd6303877b27107ec0d2bbdcf13ceadbb839e4559
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T014654Z-fungal-type-vacuole-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 66b07afcf055b463e47b79f4eb078abc6122ad4d2cbb69bd299ed1f63ca40ad6
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa;
    current SHA256 ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa.
    Record bytes unchanged since the original review.
  snapshot_sha256: ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T014656Z-fungal-type-vacuole-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1970ed9588a167cae819f4b54e21827cf8164249c72c1db0d495398959ae897f
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51;
    current SHA256 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T014657Z-fungal-type-vacuole-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6efd353f4896fd9eeea03d0fd3d30a6fb77a86e0880bb4ea459eb64e0483e3bc
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 e4e8d4917968433f370c60a2f571b3c3e1f11034b01373015911772e014d2b1e;
    current SHA256 c31397edde14cca6a35fa8574d38fdd77f1c6d49bbe95f145d6f1a8e872b033b.
    Changed record reassessed against current sources.
  snapshot_sha256: c31397edde14cca6a35fa8574d38fdd77f1c6d49bbe95f145d6f1a8e872b033b
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T014658Z-glycosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8ea631570b73dc73401a34b5e1bb6b5cf02f343bd7fa89904157bab132f516ae
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544;
    current SHA256 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544.
    Record bytes unchanged since the original review.
  snapshot_sha256: 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T014659Z-glycosome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8134befc132637c75f7238a344ae6ce7ddbc480255a12d907dccef43316ba2c0
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9;
    current SHA256 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T014700Z-glycosome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c4621537888d3ce79555c9b131fff31164c239257a7bd710b908eefd6b38fead
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b;
    current SHA256 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b.
    Record bytes unchanged since the original review.
  snapshot_sha256: 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T014701Z-glyoxysomal-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 85067fb611fad53ee12afb5cbc2381b874adad30e0aca26e31361cf81c182a02
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Original frozen SHA256 acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c;
    current SHA256 acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c.
    Record bytes unchanged since the original review.
  snapshot_sha256: acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T014701Z-glyoxysomal-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T14:26:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ae2795bd9041cfda615c1d2f8ce65eb87438740c7ac43afba007073346bd1c31
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/membrane_organelle/flagellar_pocket.yaml
  locator: Entire maintained record at source 85122489fca6bd0f63b1a6b276d138f847405e3e;
    all fields, histories, discussions and graphs
  summary: Unchanged from original frozen target. PROPOSED unchanged. No scientific
    record curation performed by this reviewer.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: supports
  snapshot_sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
- evidence_id: plaque-original-0
  kind: prior_review
  reference: reviews/structured/20261022T014651Z-flagellar-pocket-audit/review.yaml
  locator: Exact staleness-listed original authoritative YAML/Markdown, input hashes,
    checks, assessments, findings/actions and limitations
  summary: Original pair validates and renders byte-exactly; all 15 historical frozen
    inputs match its source. Historical scientific verdict independently reassessed;
    original content remains immutable.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: supports
  snapshot_sha256: 46cb98fedbbaff173393ad6a2ced8782d58b876915db382a2c3b623dfb9b4560
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/membrane_organelle/food_vacuole.yaml
  locator: Entire maintained record at source 85122489fca6bd0f63b1a6b276d138f847405e3e;
    all fields, histories, discussions and graphs
  summary: 'Changed from original frozen target: new membrane STRUCTURE node/component_ref
    and bounds edge, plus curation history; current delta substantively reassessed.
    PROPOSED unchanged. No scientific record curation performed by this reviewer.'
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: supports
  snapshot_sha256: 834e2ee1d3c5f37ca9f20f2541cccfcc755cc94621c864ab84c0a4687a2baa1f
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261022T014653Z-food-vacuole-audit/review.yaml
  locator: Exact staleness-listed original authoritative YAML/Markdown, input hashes,
    checks, assessments, findings/actions and limitations
  summary: Original pair validates and renders byte-exactly; all 14 historical frozen
    inputs match its source. Historical scientific verdict independently reassessed;
    original content remains immutable.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: supports
  snapshot_sha256: ce9ba4330d8490f16df6ad28334cb4a2c4f35edf3ec536a91ada7bddf5218a20
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Named genes/proteins/regulators/pathways/stress responses/traits trigger
    structured-source assessment. Empty accession inventories do not waive narrative
    pathway claims.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native contract and relevant definitions
  summary: Exact identity, source scope, grounding, taxonomy and necessity must be
    assessed; missing optional inventories alone are not findings.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-rubric
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Mechanistic claims require inspected primary support; descriptive identity/topology
    alone is not a molecular causal sequence.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen native contract and relevant definitions
  summary: Native protein checks assess represented accession inventories and typed
    graph actors; narrative protein claims still require source assessment.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native contract and relevant definitions
  summary: StructuralComponent represents a molecular building block. A whole membrane
    GO identity does not identify lipid material; GO may ground a protein subcomplex.
    Structural topology and molecular material remain distinct.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-neighbor-membrane
  kind: record_content
  reference: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  locator: Entire frozen neighbor read for bounded identity/material/boundary context
    only
  summary: Whole GO0020018 membrane is distinguished from its reviewed-label-only
    lipid-bilayer constituent; structural boundary is valid without treating whole
    GO membrane as lipid identity. Other neighbor protein examples and claims are
    not independently certified; no terminal historical disposition.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
- evidence_id: plaque-neighbor-collar
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  locator: Entire frozen neighbor read for bounded identity/material/boundary context
    only
  summary: Whole GO1990900 collar is a protein-complex structure at the pocket neck,
    distinct from pocket, membrane and flagellum. Other neighbor protein examples
    and claims are not independently certified; no terminal historical disposition.
  accessed_at: '2026-11-03T14:16:51.728795Z'
  support: context_only
  snapshot_sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900,GO:0020020
  locator: All five exact active term names/definitions/synonyms and typed children
    in complete returned JSON
  summary: GO0020016 ciliary pocket has exact flagellar pocket synonym and is a plasma-membrane
    invagination;0020018 denotes its complete plasma-membrane domain, not lipid material;1990900
    is its neck collar.0020016 lists membrane/collar part_of children;0060170 lists0020018
    is_a.0020020 is a parasite food vacuole digesting host cytoplasm, with digestive
    vacuole exact synonym. Authority identities are not species-specific necessity
    experiments.
  accessed_at: '2026-11-03T14:11:05.415613Z'
  support: supports
  snapshot_sha256: 3e056d63c8bb1951dfa1ef421149fbd28f53d296c47aebfceb25dc3267db943c
- evidence_id: plaque-tax-5691
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete native taxId/scientificName/rank/lineage
  summary: Species5691 is Trypanosoma brucei. Taxon identity does not establish measured
    prevalence or silently equate experimental strains/life stages.
  accessed_at: '2026-11-03T14:11:04.628459Z'
  support: supports
  snapshot_sha256: 317715e340d7901b277169134b1d17bbbe5778a1b9c30c8d0e1b028d155f4cbb
- evidence_id: plaque-tax5833
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Complete native taxId/scientificName/rank/lineage
  summary: Species5833 is Plasmodium falciparum. Taxon identity does not establish
    measured prevalence or silently equate experimental strains/life stages.
  accessed_at: '2026-11-03T14:11:05.217069Z'
  support: supports
  snapshot_sha256: 2df2a0981f04c32092ca60753a3398e45ed0d84ac8c090ca31e269edd7fffd25
- evidence_id: plaque-doi-10.1038_nrmicro2221
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro2221
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Field and Carrington2009 PMID19806154 is a review. Complete abstract supports
    the trypanosome pocket as a plasma-membrane invagination and endo/exocytosis site.
    Secondary abstract scope; no publisher full body inspected.
  accessed_at: '2026-11-03T14:11:04.628627Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:04.628627Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro2221;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: be8dc997977d04a433ac9e5ca5535e3a8d36c02bc0b6a4f1e044cab801811906
- evidence_id: plaque-doi-10.1242_jcs.045740
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242/jcs.045740
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Lacomble et al.2009 PMID19299460, exact primary article identity and complete
    abstract; architecture and boundaries independently inspected in body.
  accessed_at: '2026-11-03T14:11:04.628716Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:04.628716Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242/jcs.045740;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: 40c5eb0b1ff7f3f4ddff42bbe7cfa29b8422d3920783c6428157cc0684b4d23c
- evidence_id: plaque-doi-10.1073_pnas.0909289106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0909289106
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Gadelha et al.2009 PMID19805090, exact primary article identity and complete
    abstract; membrane domains and boundary experiments inspected in body.
  accessed_at: '2026-11-03T14:11:04.628765Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:04.628765Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0909289106;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: 1e0d2e19103f1a6f98801b00012315427a396610d687351c10fecc37037093bb
- evidence_id: plaque-doi-10.1016_j.pt.2020.11.005
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2020.11.005
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Halliday et al.2021 PMID33308952 is a review comparing trypanosomatid pocket
    structure/functions. Complete abstract supports scoped endo/exocytic trafficking;
    no publisher full body or primary intervention claimed.
  accessed_at: '2026-11-03T14:11:04.628811Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:04.628811Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2020.11.005;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: 2a4a18b6628465221f28d38635b2102f5d1e05c4a635e4a18231d9d73dcdb3ad
- evidence_id: plaque-bonhivers2008-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.0060105
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Bonhivers et al.2008 PMID18462016, exact primary article identity and complete
    abstract; BILBO1 perturbation and collar localization independently inspected
    in primary manuscript.
  accessed_at: '2026-11-03T14:11:04.629170Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:04.629170Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.0060105;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: 8aac9d85fe19ea5e2c9aa42931cafadc60f408b34fc2ba23ed126eb1665a01e8
- evidence_id: plaque-cowman1991-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.113.5.1033%22
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Cowman et al.1991 PMID1674943 complete primary abstract. Immunofluorescence/immunoelectron
    microscopy localizes Pgh1 to the digestive-vacuole membrane of mature P. falciparum
    parasites. This supports membrane localization and boundary context; resistance
    mechanism is proposed, not demonstrated individual formation necessity. No body/figure
    pixels inspected.
  accessed_at: '2026-11-03T14:11:05.268655Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:05.268655Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.113.5.1033%22;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: c0ceed7b3503a15755e62d31fedb24048efbb3222226b6d06c4cea46a3fad41c
- evidence_id: plaque-lamarque2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1002/prca.200700112%22
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Exact MED PMID21136929 entry from two returned DOI matches; Lamarque et
    al.2008 complete primary abstract describes FV-enriched P. falciparum fraction
    and 116 identified proteins. EM and immunoblot support major FV contribution,
    not purification to homogeneity or universal required constituents. No primary
    full body/figure pixels inspected.
  accessed_at: '2026-11-03T14:11:05.289611Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:05.289611Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1002/prca.200700112%22;
    inspected 2 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: 72cf7685355e31cd7de969e6d68c2e598850d379f80ad0a976afdfbd1aa282b7
- evidence_id: plaque-wiser2024-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.3390/pathogens13030182%22
  locator: Exact EuropePMC core bibliographic match and complete abstract; additional
    body tier separately stated
  summary: Wiser2024 PMID38535526 is explicitly a review, not a new primary experiment;
    exact identity/complete abstract. Detailed digestion and membrane context inspected
    in review body.
  accessed_at: '2026-11-03T14:11:05.282017Z'
  support: supports
  search_scope: Bounded EuropePMC core exact DOI lookup at 2026-11-03T14:11:05.282017Z;
    exact query URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.3390/pathogens13030182%22;
    inspected 1 returned metadata/abstract matches; selected exact MED entry where
    duplicate indexing occurs. No open-ended bibliography or full-text search, and
    no full-body inference.
  snapshot_sha256: 3081b883a67f446bfed973a6920b3c543aa3dcfdf58591a22d6e3cb7ca842a09
- evidence_id: plaque-pmc-PMC2714436
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/
  locator: Genuine PMC primary HTML Resultssec3/4 and Methodssec10; selected Introduction/Discussion
    paragraphs explicitly mentioning Bonhivers/BILBO1; embedded captions as text,
    no figure pixels/movies
  summary: Procyclic T. brucei brucei427 tomography defines an asymmetric pocket,
    membrane domains, collar and neck boundaries. The selected Discussion explicitly
    cites Bonhivers for BILBO1/collar and lost-pocket RNAi phenotypes, so the canonical
    architecture/biogenesis context is appropriately linked to that primary study
    separately. Pocket duplication/cell-cycle context is retained; routine single-pocket
    wording is not treated as denial of duplication. No biochemical lipid identity
    or universal unique collar mechanism follows from morphology.
  accessed_at: '2026-11-03T14:11:04.635379Z'
  support: supports
  snapshot_sha256: 4877a9f35d831f142bfc4b81005de379f8e7424972eeeb184c6fa2a878da4d62
- evidence_id: plaque-pmc-PMC2755463
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/
  locator: Genuine PMC primary HTML Resultssec2/3/5/6 and Methodssec12 with embedded
    caption text; no SI Methods, supplements, movies or figure pixels
  summary: Bloodstream-form trypanosome cold-marker uptake, physiological-temperature
    tomography and freeze-fracture distinguish FP, cell-surface and flagellar membranes
    and their boundaries. Clathrin distribution and neck-channel observations support
    broad trafficking/domain context. A marker accumulation at low temperature is
    not proof of active transport mechanism, and membrane particle/domain organization
    does not ground a whole membrane as lipid material.
  accessed_at: '2026-11-03T14:11:04.637273Z'
  support: supports
  snapshot_sha256: fb065179ce1211d4d493a09fbbd66dcf2fd6dabf5cba0464ce0afd2aea97ca8c
- evidence_id: plaque-bonhivers2008-plos
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0060105&type=manuscript
  locator: Genuine primary publisher XML sections s2a/s2b/s2c/s3a/s3d/s4a/s4e/s4i;
    figure captions embedded as text, no figure pixels or supplementary raw data
  summary: BILBO1 localizes to FPC; RNAi prevents new FPC/FP formation while the preexisting
    pocket persists, with positioning/cytokinesis defects. Methods distinguish genomic
    TREU927/4 GUTat10.1, procyclic EATRO1125-T7T and bloodstream427 90-13 lines. This
    directly supports new-pocket biogenesis wording; do not equate all strain contexts,
    generalize to every collar constituent, or infer exact bilayer chemistry.
  accessed_at: '2026-11-03T14:11:05.136892Z'
  support: supports
  snapshot_sha256: 559b71fe763193b9f919a4d853e2242072ebaf0fd44bfece2c78b6ee925391aa
- evidence_id: plaque-wiser2024-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/10974218/
  locator: Genuine PMC review body section3.2 includingTable2 and complete section4
    with4.1/4.2/4.3 and Fig2caption; no figure pixels or referenced primary experiments
    reanalysis
  summary: Secondary synthesis supports an acidic digestive compartment, membrane
    separation/transport between digestive lumen and parasite cytoplasm, hemoglobin
    proteolysis, heme release and hemozoin crystallization. Transporter directions
    and exact hemozoin molecular mechanism remain incompletely resolved. The newly
    added boundary edge is descriptive topology; no primary causal mechanism or protein
    necessity is inferred from this review.
  accessed_at: '2026-11-03T14:11:05.316058Z'
  support: supports
  snapshot_sha256: d17b4e6a286435f6b6a7cafb705c129bdf0a92a6056cd19dd8a270ca99ba206d
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official /api/datasets response; all20 organism rows and
    their listed organism/dataset pairs read, no pagination
  summary: Returned catalogue contains no Trypanosoma brucei or Plasmodium falciparum
    host. BILBO1/endo-exocytic trafficking and hemoglobin/heme pathways trigger assessment,
    but no matched downstream gene/module query applies. Unrelated bacterial/archaeal
    datasets are not proxies. Catalogue noncoverage is not biological absence; generated
    module prose is not used.
  accessed_at: '2026-11-03T14:11:05.417095Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical00:49Z receipt with stdout/stderr reread and hashes verified
  summary: Historical runner failed before dataset retrieval with PermissionError
    reading pyvenv.cfg. No current invocation or success claimed; fresh official catalogue
    and scoped primary/authority sources are the permitted fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-plaque/original-checks.json
  locator: Both original native validation/render results and historical-source input
    hashes
  summary: Both original pairs validate/render exactly; historical input counts15/14
    all match their source commits. Flagellar pocket unchanged, food vacuole genuinely
    stale; historical validation does not certify current bytes.
  accessed_at: '2026-11-03T14:11:04.457580Z'
  support: supports
  snapshot_sha256: a1eb62b9c2fe5f7da3bbdb0c13a12b803c6a655764fba3f1d2d1b8a322aba241
- evidence_id: plaque-native-flagellar_pocket-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/flagellar_pocket.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes.
    Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions
    are independently assessed.'
  accessed_at: '2026-11-03T14:10:44.866231Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-flagellar_pocket-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/flagellar_pocket.yaml
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
    \ scope; narrative protein/pathway assertions are independently assessed."
  accessed_at: '2026-11-03T14:10:45.334851Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-food_vacuole-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/food_vacuole.yaml
    --verify
  locator: Root-owned actual command receipt/stdout independently read and hash-verified
  summary: 'all UniProtKB protein_examples and causal_graphs xrefs verified ok Scope:
    Complete target has no component protein_examples and zero GENE_OR_PROTEIN nodes.
    Mechanical coverage is empty-inventory scope; narrative protein/pathway assertions
    are independently assessed.'
  accessed_at: '2026-11-03T14:10:45.792254Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-food_vacuole-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/food_vacuole.yaml
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
    \ scope; narrative protein/pathway assertions are independently assessed."
  accessed_at: '2026-11-03T14:10:46.215132Z'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Entire current skill; reread with profile/config/shared contract/checklist
    and CURATION identity/component/graph rules
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Scientific claims require narrow inspected source support. Named proteins/pathways
    trigger structured-source applicability; absence of expression inference is not
    an exemption. Original observations remain immutable.
  support: context_only
- evidence_id: micro-protein-contract
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Entire native protein skill and StructuralComponent/ProteinExample/CausalNode
    schema definitions; verifier coverage labels inspected
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
  summary: Distinguish identity from membership, canonical species from reference
    strain, constituent components from allowed external/region actor xrefs, and structure-formation
    necessity from enzyme activity.
  support: context_only
- evidence_id: micro-graph-contract
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Entire graph skill and linked add-cell-structure graph/evidence contract;
    NONMECHANISTIC scope retained
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Topology/function graphs retain bounded source scope; no fabricated molecular
    assembly path, component inventory, or new status promotion.
  support: context_only
- evidence_id: micro-record-fungal_type_vacuole
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole.yaml
  locator: Entire maintained current YAML, including all graph edges, history, discussions,
    examples and source notes
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 1dc8607faa4099575b74222bd6303877b27107ec0d2bbdcf13ceadbb839e4559
  summary: 'Current target read independently. Original input is stale: only the October31
    history event and two direct part_of edges were added.'
  support: supports
- evidence_id: micro-prior-fungal_type_vacuole
  kind: prior_review
  reference: reviews/structured/20261022T014654Z-fungal-type-vacuole-audit/review.yaml
  locator: Original full scientific assessments, evidence scopes, checks, findings/actions
    and limitations; deterministic paired Markdown checked
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 66b07afcf055b463e47b79f4eb078abc6122ad4d2cbb69bd299ed1f63ca40ad6
  summary: Original qualified pass with no findings or curation actions. Explicit
    expression-only iModulonDB exclusion is deficient. Historical accesses/checks
    are not claimed freshly executed.
  support: context_only
- evidence_id: micro-native-fungal_type_vacuole-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole.yaml
    --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T14:10:47.467505Z'
  snapshot_sha256: f9eb3fadabd941d67d343dfce1ebcfb7d3ffecac266de0a058f571d89c405e29
  summary: Exit0 at exact source head. Three reviewed component examples P07267/PEP4,P09232/PRB1,P00729/PRC1
    at tax559292; one COVERED acid-hydrolase node. Coverage verifies declared examples,
    not an exhaustive vacuolar proteome or membership by itself.
  support: supports
- evidence_id: micro-native-fungal_type_vacuole-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole.yaml
    --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole-uniprot-causal.log
    SHA256 e7efbc62941a2ec7ab1762a1b02eecc60e7822f33d2a0374f1e9f672d833eba7
  accessed_at: '2026-11-03T14:10:47.876629Z'
  snapshot_sha256: 65d685a4624b2e6a77f29cab530db4916e65050331e0c35be587369a0afd4a9f
  summary: Exit0 at exact source head. Three reviewed component examples P07267/PEP4,P09232/PRB1,P00729/PRC1
    at tax559292; one COVERED acid-hydrolase node. Coverage verifies declared examples,
    not an exhaustive vacuolar proteome or membership by itself.
  support: supports
- evidence_id: micro-record-fungal_type_vacuole_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
  locator: Entire maintained current YAML, including all graph edges, history, discussions,
    examples and source notes
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa
  summary: Current target read independently. Current target bytes equal original
    frozen input.
  support: supports
- evidence_id: micro-prior-fungal_type_vacuole_lumen
  kind: prior_review
  reference: reviews/structured/20261022T014656Z-fungal-type-vacuole-lumen-audit/review.yaml
  locator: Original full scientific assessments, evidence scopes, checks, findings/actions
    and limitations; deterministic paired Markdown checked
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 1970ed9588a167cae819f4b54e21827cf8164249c72c1db0d495398959ae897f
  summary: Original qualified pass with no findings or curation actions. Explicit
    expression-only iModulonDB exclusion is deficient. Historical accesses/checks
    are not claimed freshly executed.
  support: context_only
- evidence_id: micro-native-fungal_type_vacuole_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T14:10:48.920845Z'
  snapshot_sha256: 43979789cfe5c654be23ac6c56e5d6d8d262d1223b1356dee0ee3f27de1f6e4c
  summary: Exit0 at exact source head. Zero component examples but three exact graph
    xrefs P07267/P00729/P09232 on one UNANCHORED_WITH_UNIPROT hydrolase actor. This
    is the documented xref route for actors within a region, not a dangling component
    or empty molecular check.
  support: supports
- evidence_id: micro-native-fungal_type_vacuole_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_lumen-uniprot-causal.log
    SHA256 2de30b5d9b2d9220d3ede9b9735fb20738120d09199197e7860aed297ab11440
  accessed_at: '2026-11-03T14:10:49.335894Z'
  snapshot_sha256: ff5450cb2f337b83616cab7fe0671c51a5ea9a892fc2baf3e81b7ab031417ac6
  summary: Exit0 at exact source head. Zero component examples but three exact graph
    xrefs P07267/P00729/P09232 on one UNANCHORED_WITH_UNIPROT hydrolase actor. This
    is the documented xref route for actors within a region, not a dangling component
    or empty molecular check.
  support: supports
- evidence_id: micro-record-fungal_type_vacuole_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  locator: Entire maintained current YAML, including all graph edges, history, discussions,
    examples and source notes
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51
  summary: Current target read independently. Current target bytes equal original
    frozen input.
  support: supports
- evidence_id: micro-prior-fungal_type_vacuole_membrane
  kind: prior_review
  reference: reviews/structured/20261022T014657Z-fungal-type-vacuole-membrane-audit/review.yaml
  locator: Original full scientific assessments, evidence scopes, checks, findings/actions
    and limitations; deterministic paired Markdown checked
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: 6efd353f4896fd9eeea03d0fd3d30a6fb77a86e0880bb4ea459eb64e0483e3bc
  summary: Original qualified pass with no findings or curation actions. Explicit
    expression-only iModulonDB exclusion is deficient. Historical accesses/checks
    are not claimed freshly executed.
  support: context_only
- evidence_id: micro-native-fungal_type_vacuole_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --verify; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T14:10:49.752037Z'
  snapshot_sha256: 0eb480ec22f5087db5d86aebd854d2d7ccdb87a3b522a0847c900f60fc153692
  summary: Exit0 at exact source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN
    nodes; the vacuolar V-ATPase complex is typed STRUCTURE. Generic success is an
    empty protein inventory, not a biochemical composition test.
  support: supports
- evidence_id: micro-native-fungal_type_vacuole_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --causal-graphs; complete stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/fungal_type_vacuole_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T14:10:50.190552Z'
  snapshot_sha256: 986170e858548fc39c23a0d4e39ba30fd1eb89632d13a5a28baa77b9d4dd8824
  summary: Exit0 at exact source head. Zero protein examples/xrefs and zero GENE_OR_PROTEIN
    nodes; the vacuolar V-ATPase complex is typed STRUCTURE. Generic success is an
    empty protein inventory, not a biochemical composition test.
  support: supports
- evidence_id: micro-original-pairs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-microtubule/original-validation-receipt.json
  locator: Three native validate and three render --content executions; six actual
    outputs hashed; historical git-show target hashes rechecked
  accessed_at: '2026-11-03T14:11:34.182140Z'
  snapshot_sha256: 001cbaaef53c504b43b058db5dc243237353943c9a68dd578dbd5e28c805bc67
  summary: All three original YAMLs validate and their deterministic Markdown matches
    exactly. Historical target hashes match frozen inputs; only whole vacuole changed.
  support: supports
- evidence_id: micro-stale-delta
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-microtubule/fungal-vacuole-stale.diff
  locator: Complete historical-frozen to current-source diff for fungal_type_vacuole
    only
  accessed_at: '2026-11-03T14:15:24.084665Z'
  snapshot_sha256: c8915cc4ab65f21c3159543a88672aa77a4eda4d2307451ced27341f7b15a528
  summary: The only delta adds one history event and membrane/lumen direct parthood
    edges, each with exact GO evidence. No proteins, definitions or earlier edges
    changed.
  support: context_only
- evidence_id: micro-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000324,GO:0000328,GO:0000329,GO:0005773,GO:0005774,GO:0005775,GO:0016471,GO:0007035
  locator: Complete eight-term native QuickGO response, active flags, names, definitions,
    synonyms and children
  accessed_at: '2026-11-03T14:11:20.614380Z'
  snapshot_sha256: d381e6b9e76ebf83e403984b36b412b48cc723858942799cf531d800aecc2470
  summary: 'All eight current identifiers resolve with correct distinctions: whole
    GO0000324; lumen328; membrane329; broader vacuole5773/lumen5775/membrane5774;
    vacuolar V-ATPase0016471; acidification0007035. Whole definition explicitly supports
    storage, hydrolases and degradation. Exact morphology synonym agrees.'
  support: supports
- evidence_id: micro-ols-0000324
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0000324/graph
  locator: Complete native OLS GO graph nodes/edges for exact GO:0000324
  accessed_at: '2026-11-03T14:11:20.614726Z'
  snapshot_sha256: 390136d6f19709769fb190c15fa50e37cc1f9815f53caf6003b72b35d753759b
  summary: Current direct BFO0000050 edges from both fungal lumen328 and membrane329
    to whole324 are explicit. Lumen is directly subclass of vacuolar lumen5775; whole
    and membrane broader parentage are checked separately by is_a ancestry.
  support: supports
- evidence_id: micro-ols-0000328
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0000328/graph
  locator: Complete native OLS GO graph nodes/edges for exact GO:0000328
  accessed_at: '2026-11-03T14:11:20.614883Z'
  snapshot_sha256: 2189d5bea5fee0d1ad701a20185bc278ec496b59ba7508e70e0abcb4fdf144a6
  summary: Current direct BFO0000050 edges from both fungal lumen328 and membrane329
    to whole324 are explicit. Lumen is directly subclass of vacuolar lumen5775; whole
    and membrane broader parentage are checked separately by is_a ancestry.
  support: supports
- evidence_id: micro-ols-0000329
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0000329/graph
  locator: Complete native OLS GO graph nodes/edges for exact GO:0000329
  accessed_at: '2026-11-03T14:11:20.615011Z'
  snapshot_sha256: a2745f3757d9e4d13fed7ff54b6b0a0621da3435d7f3ecb381fbe3341189589a
  summary: Current direct BFO0000050 edges from both fungal lumen328 and membrane329
    to whole324 are explicit. Lumen is directly subclass of vacuolar lumen5775; whole
    and membrane broader parentage are checked separately by is_a ancestry.
  support: supports
- evidence_id: micro-ancestors-whole
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000324/ancestors?relations=is_a
  locator: Complete native QuickGO ancestors response with relations=is_a
  accessed_at: '2026-11-03T14:12:22.880975Z'
  snapshot_sha256: 5bdf4d077666402b9a0811de3f14c3c6e1d3003e6a3846faeab7fd4234881232
  summary: GO0000324 includes GO0005773 in the is_a ancestors. This confirms compatible
    broader record parentage without relabeling it a direct ontology subclass edge.
  support: supports
- evidence_id: micro-ancestors-membrane
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329/ancestors?relations=is_a
  locator: Complete native QuickGO ancestors response with relations=is_a
  accessed_at: '2026-11-03T14:12:22.881085Z'
  snapshot_sha256: 284018be139505e9831a1934d7d7b076c3d809976816de14d5364eac78add038
  summary: GO0000329 includes GO0005774 in the is_a ancestors. This confirms compatible
    broader record parentage without relabeling it a direct ontology subclass edge.
  support: supports
- evidence_id: micro-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxId/scientificName/rank/lineage fields
  accessed_at: '2026-11-03T14:11:20.615125Z'
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
  summary: NCBITaxon:4932 is Saccharomyces cerevisiae, species. This is authority
    identity, not measured prevalence or identification of the experimental strain
    in every paper.
  support: supports
- evidence_id: micro-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxId/scientificName/rank/lineage fields
  accessed_at: '2026-11-03T14:11:20.615235Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: NCBITaxon:559292 is Saccharomyces cerevisiae S288C, strain. This is authority
    identity, not measured prevalence or identification of the experimental strain
    in every paper.
  support: supports
- evidence_id: micro-up-P07267
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07267.json
  locator: Primary accession, entryType, recommended names, all gene tokens, organism;
    complete FUNCTION/SUBCELLULAR LOCATION/SIMILARITY comments; relevant cited PubMed
    records
  accessed_at: '2026-11-03T14:11:21.223662Z'
  snapshot_sha256: 6ab8cf887f3658175bd074f93fc54b08d297cb408834631f9d245d7ef10664a2
  summary: P07267 is reviewed Saccharopepsin, primary gene PEP4, tax559292; native
    function/location and peptidase A1 annotation inspected. Distinct enzyme families
    support the heterogeneous acid-hydrolase class rather than one arbitrary family
    accession.
  support: supports
- evidence_id: micro-up-P00729
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P00729.json
  locator: Primary accession, entryType, recommended names, all gene tokens, organism;
    complete FUNCTION/SUBCELLULAR LOCATION/SIMILARITY comments; relevant cited PubMed
    records
  accessed_at: '2026-11-03T14:11:21.227971Z'
  snapshot_sha256: 454c42a3ff6f676dd8419bd405ed7e6a2fcb7fa1f7be3afdda99f73a28fd7941
  summary: P00729 is reviewed Carboxypeptidase Y, primary gene PRC1, tax559292; native
    function/location and peptidase S10 annotation inspected. Distinct enzyme families
    support the heterogeneous acid-hydrolase class rather than one arbitrary family
    accession. Vacuole lumen SL0270 explicitly carries ECO0000269 citations14562095,23708375,29514932,
    matching target attribution notes. Separate VPS10/ATG42 prose on this entry is
    not transferred to PRC1.
  support: supports
- evidence_id: micro-up-P09232
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09232.json
  locator: Primary accession, entryType, recommended names, all gene tokens, organism;
    complete FUNCTION/SUBCELLULAR LOCATION/SIMILARITY comments; relevant cited PubMed
    records
  accessed_at: '2026-11-03T14:11:21.273718Z'
  snapshot_sha256: 80f4737105eec9422743d80e1a80067478635f6d161007290de739d40875dc0b
  summary: P09232 is reviewed Cerevisin, primary gene PRB1, tax559292; native function/location
    and peptidase S8 annotation inspected. Distinct enzyme families support the heterogeneous
    acid-hydrolase class rather than one arbitrary family accession.
  support: supports
- evidence_id: micro-unique-PEP4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3APEP4%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned page and actual primary/synonym tokens; X-Total-Results
    1 and Link None
  accessed_at: '2026-11-03T14:11:21.295403Z'
  snapshot_sha256: c60151d7a91a385357f76bd63f62f5719500d420b37d8beabe4a5afa5d87e6c6
  summary: PEP4 returns exactly P07267 in this bounded reviewed S288C query.
  support: supports
  search_scope: UniProtKB native search at 2026-11-03T14:11:21.295403Z; literal query
    '(gene_exact:PEP4) AND (taxonomy_id:559292) AND (reviewed:true)'; format=json,size=100;
    all 1 returned records inspected, total header 1, next-page Link None. Scoped
    reviewed S288C identity lookup, not pan-taxon absence or experimental localization.
- evidence_id: micro-unique-PRC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3APRC1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned page and actual primary/synonym tokens; X-Total-Results
    2 and Link None
  accessed_at: '2026-11-03T14:11:21.297084Z'
  snapshot_sha256: 892d31f34b90ad6aae32bc6ab1289a4dbdf8248d7a514f3a2e8696c3d41b22d1
  summary: PRC1 returns P00729 primary PRC1 and P21242 primary PRE10 with PRC1 synonym.
    Target correctly calls P00729 a representative, not the unique search result;
    no arbitrary seeding or gene synonym error is asserted.
  support: supports
  search_scope: UniProtKB native search at 2026-11-03T14:11:21.297084Z; literal query
    '(gene_exact:PRC1) AND (taxonomy_id:559292) AND (reviewed:true)'; format=json,size=100;
    all 2 returned records inspected, total header 2, next-page Link None. Scoped
    reviewed S288C identity lookup, not pan-taxon absence or experimental localization.
- evidence_id: micro-unique-PRB1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=100&query=%28gene_exact%3APRB1%29%20AND%20%28taxonomy_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned page and actual primary/synonym tokens; X-Total-Results
    1 and Link None
  accessed_at: '2026-11-03T14:11:21.301831Z'
  snapshot_sha256: bee520e9e96c59f6e027078818963d74c583e93a54601826b6180ff486e80298
  summary: PRB1 returns exactly P09232 in this bounded reviewed S288C query.
  support: supports
  search_scope: UniProtKB native search at 2026-11-03T14:11:21.301831Z; literal query
    '(gene_exact:PRB1) AND (taxonomy_id:559292) AND (reviewed:true)'; format=json,size=100;
    all 1 returned records inspected, total header 1, next-page Link None. Scoped
    reviewed S288C identity lookup, not pan-taxon absence or experimental localization.
- evidence_id: micro-li2009-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1016/j.bbamcr.2008.08.003%22
  locator: Exact selected MED core bibliographic record and complete abstract; full
    text separately scoped
  accessed_at: '2026-11-03T14:11:22.008698Z'
  snapshot_sha256: d6fa0005edddf31ac471a9f8a28cd8907cef9ecb240c5b47d0d7dd46f0232c14
  summary: 'PMID18786576, DOI10.1016/j.bbamcr.2008.08.003: The yeast lysosome-like
    vacuole: endpoint and crossroads. Explicit secondary review article, not primary
    experimental evidence.'
  support: context_only
  search_scope: Europe PMC native search at 2026-11-03T14:11:22.008698Z; exact literal
    query 'DOI:"10.1016/j.bbamcr.2008.08.003"'; resultType=core,format=json,pageSize=100;
    hitCount1 and one MED record returned/read. This establishes exact citation identity
    and abstract scope, not exhaustive literature coverage.
- evidence_id: micro-kane2006-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1128/MMBR.70.1.177-191.2006%22
  locator: Exact selected MED core bibliographic record and complete abstract; full
    text separately scoped
  accessed_at: '2026-11-03T14:11:22.018050Z'
  snapshot_sha256: 4f8c531ebaab9a56b5aadebed18c6cc3445c11ab867f3919051ea2f160bb7641
  summary: 'PMID16524922, DOI10.1128/mmbr.70.1.177-191.2006: The where, when, and
    how of organelle acidification by the yeast vacuolar H+-ATPase. Explicit secondary
    review article, not primary experimental evidence.'
  support: context_only
  search_scope: Europe PMC native search at 2026-11-03T14:11:22.018050Z; exact literal
    query 'DOI:"10.1128/MMBR.70.1.177-191.2006"'; resultType=core,format=json,pageSize=100;
    hitCount1 and one MED record returned/read. This establishes exact citation identity
    and abstract scope, not exhaustive literature coverage.
- evidence_id: micro-pmid-14562095
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID%3A14562095%20AND%20SRC%3AMED
  locator: Exact selected MED core bibliographic record and complete abstract; full
    text separately scoped
  accessed_at: '2026-11-03T14:11:22.048130Z'
  snapshot_sha256: dbcfc72bde5dd2ef83f6815cecc6789552fd291f631918515e8b6c407dfb0674
  summary: 'PMID14562095, DOI10.1038/nature02026: Global analysis of protein localization
    in budding yeast. Primary abstract inspected; Huh and Matsumoto bodies/datasets
    not read in this pass. Parzych body scope is separately recorded.'
  support: context_only
  search_scope: Europe PMC native search at 2026-11-03T14:11:22.048130Z; exact literal
    query 'EXT_ID:14562095 AND SRC:MED'; resultType=core,format=json,pageSize=100;
    hitCount1 and one MED record returned/read. This establishes exact citation identity
    and abstract scope, not exhaustive literature coverage.
- evidence_id: micro-pmid-23708375
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID%3A23708375%20AND%20SRC%3AMED
  locator: Exact selected MED core bibliographic record and complete abstract; full
    text separately scoped
  accessed_at: '2026-11-03T14:11:22.454663Z'
  snapshot_sha256: ab2b0e3050995c08429d1c07e9de56b2dbbb468e6c1758d8f7b987303beb56d6
  summary: 'PMID23708375, DOI10.1007/s00709-013-0510-2: Organelle acidification is
    important for localisation of vacuolar proteins in Saccharomyces cerevisiae. Primary
    abstract inspected; Huh and Matsumoto bodies/datasets not read in this pass. Parzych
    body scope is separately recorded.'
  support: context_only
  search_scope: Europe PMC native search at 2026-11-03T14:11:22.454663Z; exact literal
    query 'EXT_ID:23708375 AND SRC:MED'; resultType=core,format=json,pageSize=100;
    hitCount1 and one MED record returned/read. This establishes exact citation identity
    and abstract scope, not exhaustive literature coverage.
- evidence_id: micro-pmid-29514932
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID%3A29514932%20AND%20SRC%3AMED
  locator: Exact selected MED core bibliographic record and complete abstract; full
    text separately scoped
  accessed_at: '2026-11-03T14:11:22.636883Z'
  snapshot_sha256: caf5801edf9ddec29722821363183a4ac15e6d8d4dadda8f77d04ff3dc8cb222
  summary: 'PMID29514932, DOI10.1091/mbc.e17-08-0516: A newly characterized vacuolar
    serine carboxypeptidase, Atg42/Ybr139w, is required for normal vacuole function
    and the terminal steps of autophagy in the yeast Saccharomyces cerevisiae. Primary
    abstract inspected; Huh and Matsumoto bodies/datasets not read in this pass. Parzych
    body scope is separately recorded.'
  support: context_only
  search_scope: Europe PMC native search at 2026-11-03T14:11:22.636883Z; exact literal
    query 'EXT_ID:29514932 AND SRC:MED'; resultType=core,format=json,pageSize=100;
    hitCount1 and one MED record returned/read. This establishes exact citation identity
    and abstract scope, not exhaustive literature coverage.
- evidence_id: micro-li2009-body
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2906225/
  locator: Complete secondary review sections2.1/4.2/5.1/6.1/6.2 (S3/S13/S16/S20/S21),
    including embedded Fig2/3 captions; no figure pixels or underlying dataset reanalysis
  accessed_at: '2026-11-03T14:11:22.638624Z'
  snapshot_sha256: 10f3bacdf66806730725db2788fe5a68ddfb240c023b5ee06b346f570131d0f1
  summary: Review explicitly identifies soluble Pep4/CPY/Prb1, storage of amino acids/ions/polyphosphate,
    and endocytic/biosynthetic/autophagic routes. It separates resident proteins from
    transient cargo and vacuolar Vph1 pumps from Golgi/endosomal Stv1. Low pH optimizes
    proteolysis but is not absolutely required for every reaction.
  support: context_only
- evidence_id: micro-kane2006-body
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1393255/
  locator: Complete secondary review Introduction(sec1), yeast V-ATPase structure(sec3)
    and V0-a isoform targeting(sec11), including Fig1 caption; no figure pixels
  accessed_at: '2026-11-03T14:11:22.662361Z'
  snapshot_sha256: 094f06d2fa6a191f098091ade56ccab7a290d940d6e59806ae25b6076f53c1d0
  summary: Secondary synthesis supports membrane-associated vacuolar proton pumping
    and Vph1/Stv1 localization differences. STV1 overexpression/trafficking caveats
    preclude all-V-ATPases-permanently-vacuolar wording. Historical subunit model
    is not certified as current complete stoichiometry.
  support: context_only
- evidence_id: micro-parzych2018-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5921575/
  locator: Complete Results sec3 andsec4, Discussionsec7, Methodssec9 with Tables1/2
    and fluorescence microscopysec11; included Fig1/2/3 captions read, no pixels or
    supplements
  accessed_at: '2026-11-03T14:12:22.880836Z'
  snapshot_sha256: a00789c43a450d0a72baba31226241b997c016ed197ab66ac2c1c9d93a872db7
  summary: Primary Prc1-GFP comparison shows diffuse soluble lumenal signal distinct
    from FM4-64 membrane in growing/starved SEY6210-derived strains. Double prc1/ybr139w
    loss and single mutants demonstrate compensatory proteolytic function, not each
    protein necessary for vacuole assembly. Reference S288C accession identity is
    not the experimental strain. Mechanism of terminal autophagic body breakdown remains
    unresolved.
  support: supports
- evidence_id: micro-catalogue-api
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete official /api/datasets response: all20 organism rows,28 organism/dataset
    pairs; names,IDs,descriptions and lists read'
  accessed_at: '2026-11-03T14:12:22.880497Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No matched Saccharomyces cerevisiae/S288C dataset exists in this bounded
    current catalogue. All three molecular/pathway-bearing targets require applicability
    assessment, but no organism/dataset/gene/module key can be constructed without
    an unmatched proxy. No biological absence inference.
  support: context_only
  search_scope: Official iModulonDB /api/datasets retrieved 2026-11-03T14:12:22.880497Z;
    no server filter or page parameter. Complete20 organism rows/28 organism-dataset
    pairs inspected; case-insensitive checks for Saccharomyces,cerevisiae,S288C,4932,559292
    in all names,IDs,descriptions,dataset lists. No matched catalogue entry; not an
    exhaustive transcriptomics search.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical00:49Z datasets invocation; exit1 PermissionError reading
    runner pyvenv.cfg; no current invocation
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical runner availability limitation retained honestly; current scientific
    applicability uses freshly inspected official catalogue fallback.
  support: context_only
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured-source applicability, source fidelity and severity rubric
  summary: Positive molecular/pathway assertions require applicability assessment
    throughout the record. Lack of an expression claim is not an exemption. Exact
    source scopes and uncertainty must be preserved; record curation stays outside
    this review.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Component identity, molecular grounding, protein-example and necessity
    contracts
  summary: A component represents a taxon-agnostic family/class; molecular lipids
    use chemical grounding, while substructures use parthood. Protein identity is
    not membership evidence, and import/survival phenotypes do not prove organelle-formation
    necessity.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent description/grounding and ComponentTypeEnum.PROTEIN/PROTEIN_COMPLEX
  summary: StructuralComponent is one molecular building block. LIPID grounding denotes
    a chemical class, not an assembled membrane GO identity. The enum describes PROTEIN
    as one family/paralogue group, while CURATION and the UniProt skill explicitly
    permit generic class components. That modeling-policy tension alone does not establish
    a defect in a transparently declared heterogeneous class. PROTEIN_COMPLEX denotes
    a named sub-complex, not any list of unrelated enzymes.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Mechanistic versus NONMECHANISTIC graph and evidence scope
  summary: Supported descriptive boundaries can remain NONMECHANISTIC. Source qualification,
    whole versus molecular identity, receptor cycling and observed perturbation versus
    inferred causal mechanism must remain distinct.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: 'Step 2, NO_GENE_SYMBOL guidance: generic class components'
  summary: The native skill explicitly recognizes generic class components such as
    ribosomal proteins, peptidoglycan hydrolases and cargo proteins. Together with
    CURATION family-or-class guidance, this prevents treating narrower enum prose
    alone as a confirmed type defect; neither class membership nor a list of examples
    asserts one stable protein complex.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-record-glycosome
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome.yaml
  locator: Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components
    and examples, taxonomic/canonical scope, functions, all evidence and graph edges,
    discussions/history. No maintained images, physical measurements, traits or verbatim
    snippets are declared.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: c31397edde14cca6a35fa8574d38fdd77f1c6d49bbe95f145d6f1a8e872b033b
- evidence_id: septin-original-glycosome
  kind: prior_review
  reference: reviews/structured/20261022T014658Z-glycosome-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, frozen inputs, checks, assessments,
    findings/actions and source limits
  summary: Historical checks and source access remain historical. Original scientific
    finding identities are preserved where applicable; all five originals contain
    explicit imodulondb exclusions. Whole glycosome is stale; the other four target
    inputs are unchanged.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 8ea631570b73dc73401a34b5e1bb6b5cf02f343bd7fa89904157bab132f516ae
- evidence_id: septin-original-validation-glycosome
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json
  locator: 20261022T014658Z-glycosome-audit native validate/render and historical-source
    hash
  summary: Native validate and render exit zero; original Markdown is byte-identical.
    Historical-source hash equals the frozen original. Current staleness status is
    True.
  accessed_at: '2026-11-03T14:14:46.184504Z'
  support: supports
  snapshot_sha256: 9e5a14de6ebd1f5b4e3f5d43a002707ebb475539585ac4e3071970b6782c000c
- evidence_id: septin-native-glycosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-verify-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-verify.log
  summary: 'Exit zero. Nine current protein examples: six glycolytic enzymes including
    reviewed P04789/TIM, plus three PEX proteins; six reviewed and three unreviewed
    entries. Both represented GENE_OR_PROTEIN nodes are COVERED. These checks establish
    declared identifier/symbol coverage, not exact cohort type, family grounding,
    source membership or necessity.'
  accessed_at: '2026-11-03T14:10:52.108831Z'
  support: supports
  snapshot_sha256: 3a408f97e711c2c13e580ced748e462b7b21ac0983917fddb0bd3feb6bfc8c2c
- evidence_id: septin-native-glycosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-causal-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome-uniprot-causal.log
  summary: 'Exit zero. Nine current protein examples: six glycolytic enzymes including
    reviewed P04789/TIM, plus three PEX proteins; six reviewed and three unreviewed
    entries. Both represented GENE_OR_PROTEIN nodes are COVERED. These checks establish
    declared identifier/symbol coverage, not exact cohort type, family grounding,
    source membership or necessity.'
  accessed_at: '2026-11-03T14:10:52.536523Z'
  support: supports
  snapshot_sha256: 802e592adcd4591f563ba1c64efaacb720cd1797962f685f3f30354106e89415
- evidence_id: septin-record-glycosome_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome_lumen.yaml
  locator: Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components
    and examples, taxonomic/canonical scope, functions, all evidence and graph edges,
    discussions/history. No maintained images, physical measurements, traits or verbatim
    snippets are declared.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 86388cc4813e19a29b617f1800e0499e8b280823c7f3240b75c45fa7d1b8b544
- evidence_id: septin-original-glycosome_lumen
  kind: prior_review
  reference: reviews/structured/20261022T014659Z-glycosome-lumen-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, frozen inputs, checks, assessments,
    findings/actions and source limits
  summary: Historical checks and source access remain historical. Original scientific
    finding identities are preserved where applicable; all five originals contain
    explicit imodulondb exclusions. Whole glycosome is stale; the other four target
    inputs are unchanged.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 8134befc132637c75f7238a344ae6ce7ddbc480255a12d907dccef43316ba2c0
- evidence_id: septin-original-validation-glycosome_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json
  locator: 20261022T014659Z-glycosome-lumen-audit native validate/render and historical-source
    hash
  summary: Native validate and render exit zero; original Markdown is byte-identical.
    Historical-source hash equals the frozen original. Current staleness status is
    False.
  accessed_at: '2026-11-03T14:14:47.296435Z'
  support: supports
  snapshot_sha256: 9e5a14de6ebd1f5b4e3f5d43a002707ebb475539585ac4e3071970b6782c000c
- evidence_id: septin-native-glycosome_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-verify-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-verify.log
  summary: Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  accessed_at: '2026-11-03T14:10:52.946122Z'
  support: supports
  snapshot_sha256: 6a09625760d3e4b57496ce63bae98bc831491c9b2d5cc374b1858d52e3f62583
- evidence_id: septin-native-glycosome_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-causal-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_lumen-uniprot-causal.log
  summary: Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  accessed_at: '2026-11-03T14:10:53.365745Z'
  support: supports
  snapshot_sha256: 1bdac82bcf1daa26f4c99c6dc85b73fb1d91bb944c43c7e6ca284eca0ec0d4bb
- evidence_id: septin-record-glycosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/glycosome_membrane.yaml
  locator: Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components
    and examples, taxonomic/canonical scope, functions, all evidence and graph edges,
    discussions/history. No maintained images, physical measurements, traits or verbatim
    snippets are declared.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 3d72e1e3fa6653b4d605c490e50da8b348c78773fa0e08947088b4e7ab2f43e9
- evidence_id: septin-original-glycosome_membrane
  kind: prior_review
  reference: reviews/structured/20261022T014700Z-glycosome-membrane-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, frozen inputs, checks, assessments,
    findings/actions and source limits
  summary: Historical checks and source access remain historical. Original scientific
    finding identities are preserved where applicable; all five originals contain
    explicit imodulondb exclusions. Whole glycosome is stale; the other four target
    inputs are unchanged.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: c4621537888d3ce79555c9b131fff31164c239257a7bd710b908eefd6b38fead
- evidence_id: septin-original-validation-glycosome_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json
  locator: 20261022T014700Z-glycosome-membrane-audit native validate/render and historical-source
    hash
  summary: Native validate and render exit zero; original Markdown is byte-identical.
    Historical-source hash equals the frozen original. Current staleness status is
    False.
  accessed_at: '2026-11-03T14:14:48.413366Z'
  support: supports
  snapshot_sha256: 9e5a14de6ebd1f5b4e3f5d43a002707ebb475539585ac4e3071970b6782c000c
- evidence_id: septin-native-glycosome_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-verify-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-verify.log
  summary: Exit zero. Zero protein examples, but one UNANCHORED_WITH_UNIPROT molecular
    node with verified PEX14 Q38CL4 xref. This is not an empty molecular inventory;
    it validates the represented identifier without establishing complete docking
    machinery or formation necessity.
  accessed_at: '2026-11-03T14:10:54.826906Z'
  support: supports
  snapshot_sha256: 35c994c87867a60fcb8205f52588ace990aab74748fae55f8efe55a41dede5be
- evidence_id: septin-native-glycosome_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-causal-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glycosome_membrane-uniprot-causal.log
  summary: Exit zero. Zero protein examples, but one UNANCHORED_WITH_UNIPROT molecular
    node with verified PEX14 Q38CL4 xref. This is not an empty molecular inventory;
    it validates the represented identifier without establishing complete docking
    machinery or formation necessity.
  accessed_at: '2026-11-03T14:10:55.233293Z'
  support: supports
  snapshot_sha256: 6227fe37c22ce4ef6bbbb707d2a734cf4cf59d73d64d533cc08fa13b2380ded0
- evidence_id: septin-record-glyoxysomal_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysomal_lumen.yaml
  locator: Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components
    and examples, taxonomic/canonical scope, functions, all evidence and graph edges,
    discussions/history. No maintained images, physical measurements, traits or verbatim
    snippets are declared.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 57bdc53bba889fb38dd511718cec3c0cab5013fa2029d21636f27da4ca97801b
- evidence_id: septin-original-glyoxysomal_lumen
  kind: prior_review
  reference: reviews/structured/20261022T014701Z-glyoxysomal-lumen-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, frozen inputs, checks, assessments,
    findings/actions and source limits
  summary: Historical checks and source access remain historical. Original scientific
    finding identities are preserved where applicable; all five originals contain
    explicit imodulondb exclusions. Whole glycosome is stale; the other four target
    inputs are unchanged.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 85067fb611fad53ee12afb5cbc2381b874adad30e0aca26e31361cf81c182a02
- evidence_id: septin-original-validation-glyoxysomal_lumen
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json
  locator: 20261022T014701Z-glyoxysomal-lumen-audit native validate/render and historical-source
    hash
  summary: Native validate and render exit zero; original Markdown is byte-identical.
    Historical-source hash equals the frozen original. Current staleness status is
    False.
  accessed_at: '2026-11-03T14:14:49.511039Z'
  support: supports
  snapshot_sha256: 9e5a14de6ebd1f5b4e3f5d43a002707ebb475539585ac4e3071970b6782c000c
- evidence_id: septin-native-glyoxysomal_lumen-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-verify-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-verify.log
  summary: Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  accessed_at: '2026-11-03T14:10:55.632376Z'
  support: supports
  snapshot_sha256: cd99035f6d324be116532f4203da6f7c76f57ab67cfb42d85381daeff6bf9229
- evidence_id: septin-native-glyoxysomal_lumen-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-causal-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_lumen-uniprot-causal.log
  summary: Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  accessed_at: '2026-11-03T14:10:56.048447Z'
  support: supports
  snapshot_sha256: b30ad4ea56232454cd2521fa38e3bca8fbbdb36cf345d38d6d4fd8658e0393ea
- evidence_id: septin-record-glyoxysomal_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysomal_membrane.yaml
  locator: Complete current record at 85122489fca6bd0f63b1a6b276d138f847405e3e
  summary: Read identity, definition, hierarchy/parthood, synonyms/xrefs, components
    and examples, taxonomic/canonical scope, functions, all evidence and graph edges,
    discussions/history. No maintained images, physical measurements, traits or verbatim
    snippets are declared.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: acf5b4c65edac5fd14c1a33ffa545fc5f7715162e84fdb59535e6a39d48be48c
- evidence_id: septin-original-glyoxysomal_membrane
  kind: prior_review
  reference: reviews/structured/20261022T014701Z-glyoxysomal-membrane-audit/review.yaml
  locator: Complete immutable original YAML/Markdown, frozen inputs, checks, assessments,
    findings/actions and source limits
  summary: Historical checks and source access remain historical. Original scientific
    finding identities are preserved where applicable; all five originals contain
    explicit imodulondb exclusions. Whole glycosome is stale; the other four target
    inputs are unchanged.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: ae2795bd9041cfda615c1d2f8ce65eb87438740c7ac43afba007073346bd1c31
- evidence_id: septin-original-validation-glyoxysomal_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/original-checks.json
  locator: 20261022T014701Z-glyoxysomal-membrane-audit native validate/render and
    historical-source hash
  summary: Native validate and render exit zero; original Markdown is byte-identical.
    Historical-source hash equals the frozen original. Current staleness status is
    False.
  accessed_at: '2026-11-03T14:14:50.635936Z'
  support: supports
  snapshot_sha256: 9e5a14de6ebd1f5b4e3f5d43a002707ebb475539585ac4e3071970b6782c000c
- evidence_id: septin-native-glyoxysomal_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-verify-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-verify.log
  summary: Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  accessed_at: '2026-11-03T14:10:56.451091Z'
  support: supports
  snapshot_sha256: 0e22b195a269cbbd447dda8213067dfc34c631db5864d8a1b4240303ce1a0072
- evidence_id: septin-native-glyoxysomal_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-causal-receipt.json
  locator: Actual root receipt and /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/glyoxysomal_membrane-uniprot-causal.log
  summary: Exit zero. No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  accessed_at: '2026-11-03T14:10:56.848666Z'
  support: supports
  snapshot_sha256: f74e9c74df4a715b294dc5a94363206734dd1f6ff8b2acd61806ce30954e6479
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015,GO:0034468,GO:0046860,GO:0005777,GO:0005778,GO:0043233,GO:0031908,GO:0046861,GO:0009514,GO:0006097,GO:0005782
  locator: Eleven exact current active GO terms and typed child edges
  summary: Exact whole glycosome/lumen/membrane and glyoxysome/lumen/membrane identities
    are distinct. Whole organelles subclass peroxisome, membranes subclass peroxisomal
    membrane and lumens subclass peroxisomal matrix. GO0046860/0046861 denote assembled
    lipid bilayers, not a chemical lipid class. GO0006097 is the glyoxylate cycle.
    Native plant-oriented glyoxysome examples do not independently establish fungal
    occurrence.
  accessed_at: '2026-11-03T14:12:29.201884Z'
  support: supports
  snapshot_sha256: 99471f26ba06a8b47a22a2a4a31a7c52de26274352ea9eb060eba9a09028dbfb
- evidence_id: septin-ancestors-0020015
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020015/ancestors?relations=is_a
  locator: Exact GO ancestors endpoint with relations=is_a only
  summary: Glycosome is_a peroxisome GO0005777. This establishes ancestry rather than
    a falsely asserted direct edge or mixed parthood path.
  accessed_at: '2026-11-03T14:12:29.202276Z'
  support: supports
  snapshot_sha256: 9425be9946b6ce52ccd4145f55fd33bc8e7160b5cb93a3dd8aab3bce522645d3
- evidence_id: septin-ancestors-0034468
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034468/ancestors?relations=is_a
  locator: Exact GO ancestors endpoint with relations=is_a only
  summary: Glycosome lumen has broad GO0043233 is_a ancestry through peroxisomal matrix.
    This establishes ancestry rather than a falsely asserted direct edge or mixed
    parthood path.
  accessed_at: '2026-11-03T14:12:29.202123Z'
  support: supports
  snapshot_sha256: d00024e9ab50105b15553a2ffb64a3bcae2a9c8abde352c5dd510f161e3f7e4d
- evidence_id: septin-ancestors-0031908
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031908/ancestors?relations=is_a
  locator: Exact GO ancestors endpoint with relations=is_a only
  summary: Glyoxysomal lumen has broad GO0043233 is_a ancestry through peroxisomal
    matrix. This establishes ancestry rather than a falsely asserted direct edge or
    mixed parthood path.
  accessed_at: '2026-11-03T14:12:29.202213Z'
  support: supports
  snapshot_sha256: 1004692222af5610c3419213cb31e2349892caca8f989095e880318be142d9a9
- evidence_id: septin-tax5653
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653
  locator: Exact ENA taxId, scientificName, rank, lineage and synonyms
  summary: Class Kinetoplastea; Kinetoplastida is a synonym, explaining the legacy
    order wording. Experimental strains and life stages are not inferred from a reference
    accession taxon.
  accessed_at: '2026-11-03T14:12:29.202329Z'
  support: supports
  snapshot_sha256: 6e467f5ff25d9bd8189b9c916942db46996eee6ad67fa41afd146096c2fb0556
- evidence_id: septin-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Exact ENA taxId, scientificName, rank, lineage and synonyms
  summary: Species Trypanosoma brucei. Experimental strains and life stages are not
    inferred from a reference accession taxon.
  accessed_at: '2026-11-03T14:12:29.909414Z'
  support: supports
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: septin-tax5702
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5702
  locator: Exact ENA taxId, scientificName, rank, lineage and synonyms
  summary: Subspecies Trypanosoma brucei brucei. Experimental strains and life stages
    are not inferred from a reference accession taxon.
  accessed_at: '2026-11-03T14:12:29.920216Z'
  support: supports
  snapshot_sha256: b962131faab3d27f27a24e467374345cf1d8e37d8802560cb9028eeda27ddfdc
- evidence_id: septin-tax31285
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/31285
  locator: Exact ENA taxId, scientificName, rank, lineage and synonyms
  summary: Subspecies Trypanosoma brucei gambiense. Experimental strains and life
    stages are not inferred from a reference accession taxon.
  accessed_at: '2026-11-03T14:12:29.924100Z'
  support: supports
  snapshot_sha256: 77ea2ba864ae768fa8d01d204eb39ece17e6f2837474f3709e37411570217c7f
- evidence_id: septin-tax185431
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431
  locator: Exact ENA taxId, scientificName, rank, lineage and synonyms
  summary: Reference strain Trypanosoma brucei brucei TREU927;927/4 GUTat10.1 is a
    synonym. Experimental strains and life stages are not inferred from a reference
    accession taxon.
  accessed_at: '2026-11-03T14:12:29.928125Z'
  support: supports
  snapshot_sha256: f8c6ea0ff00ea113c8c42e5ef0dae84505776d5dc7012f7950688e62639fea11
- evidence_id: septin-tax5141
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141
  locator: Exact ENA taxId, scientificName, rank, lineage and synonyms
  summary: Species Neurospora crassa. Experimental strains and life stages are not
    inferred from a reference accession taxon.
  accessed_at: '2026-11-03T14:12:29.953871Z'
  support: supports
  snapshot_sha256: 1e5524d77d1448765023e8b9b704ec3cfd7f70016410f33bd7e84a4aaed53ab9
- evidence_id: septin-SL-0128
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0128.json
  locator: Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing
    parents
  summary: Glycosome membrane maps directly to GO0046860, has glycosomal membrane
    synonym, is_a peroxisomal membrane and part_of glycosome. Nested parent mappings
    are not additional exact matches.
  accessed_at: '2026-11-03T14:12:30.505948Z'
  support: supports
  snapshot_sha256: b38283b04408b2c4ca030d1cd42c83316ef00566eb140f2fb5a758a82893987a
- evidence_id: septin-SL-0129
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0129.json
  locator: Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing
    parents
  summary: Whole glycosome maps directly to GO0020015 and is_a peroxisome; glucose/glycerol
    enzymes and examined kinetoplastid scope are authority synthesis. Nested parent
    mappings are not additional exact matches.
  accessed_at: '2026-11-03T14:12:30.523926Z'
  support: supports
  snapshot_sha256: 3ccdcd832fab1e23ae58f1c83d96fad980b02693753c9ad5b6d485bbcb86b509
- evidence_id: septin-SL-0332
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0332.json
  locator: Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing
    parents
  summary: Glycosome matrix maps directly to GO0034468, supplies lumen/matrix synonyms
    and is part_of glycosome. Nested parent mappings are not additional exact matches.
  accessed_at: '2026-11-03T14:12:30.534486Z'
  support: supports
  snapshot_sha256: e285497fc15ef710692ee1c0724633d21532888659475d2a1e4fcaf2d1146a56
- evidence_id: septin-SL-0130
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0130.json
  locator: Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing
    parents
  summary: Glyoxysome membrane maps directly to GO0046861 and has glyoxysomal membrane
    synonym, peroxisomal membrane parent and whole-organelle parthood. Nested parent
    mappings are not additional exact matches.
  accessed_at: '2026-11-03T14:12:30.536668Z'
  support: supports
  snapshot_sha256: 0bcde00617f838f8f0289d03c8684bef62b2d5b471ee28148b796b7294176e3e
- evidence_id: septin-SL-0131
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0131.json
  locator: Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing
    parents
  summary: Whole glyoxysome maps directly to GO0009514; its plant/catalase-oriented
    narrative must not be transferred uncritically to Neurospora. Nested parent mappings
    are not additional exact matches.
  accessed_at: '2026-11-03T14:12:30.538960Z'
  support: supports
  snapshot_sha256: cf99e708d621df3115ac0a2989d8db95df1e7c7fa23f4f9d6c83d60b64952e64
- evidence_id: septin-SL-0333
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0333.json
  locator: Exact UniProt location entry, direct geneOntologies, synonyms and relation-bearing
    parents
  summary: Glyoxysome matrix maps directly to GO0031908, supplies lumen/matrix synonyms
    and is part_of glyoxysome. Nested parent mappings are not additional exact matches.
  accessed_at: '2026-11-03T14:12:31.100795Z'
  support: supports
  snapshot_sha256: f72cb3a1f7b5389a3224af2407dc7e4c8f90f7fe7afd53280565f7a62c8b97b5
- evidence_id: septin-protein-P13377
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P13377.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'P13377: Glucose-6-phosphate isomerase, glycosomal; UniProtKB reviewed
    (Swiss-Prot); taxon5702; indexed genes[''PGI'']. Identity and current annotation
    do not alone certify accession-specific localization or biological necessity.'
  accessed_at: '2026-11-03T14:12:31.121661Z'
  support: supports
  snapshot_sha256: 42fadddb809c3f4130e04abd3167ac80fd16f8c7479ce88ac6dbd31bd3f92b48
- evidence_id: septin-protein-O15648
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O15648.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'O15648: ATP-dependent 6-phosphofructokinase; UniProtKB reviewed (Swiss-Prot);
    taxon5702; indexed genes[''pfk'']. Identity and current annotation do not alone
    certify accession-specific localization or biological necessity.'
  accessed_at: '2026-11-03T14:12:31.865422Z'
  support: supports
  snapshot_sha256: 61d5449c02f5dc485b684a62c989fc1640f8206df600dd68972f81eee11f4fd2
- evidence_id: septin-protein-A0A3G1VTN5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/A0A3G1VTN5.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'A0A3G1VTN5: Phosphotransferase; UniProtKB unreviewed (TrEMBL); taxon5702;
    indexed genes[''Hk1'']. Identity and current annotation do not alone certify accession-specific
    localization or biological necessity.'
  accessed_at: '2026-11-03T14:12:31.913234Z'
  support: supports
  snapshot_sha256: fac58372e414be455f3095b62bdc2402cd85976f3f472bbfb1e3d169e2231a21
- evidence_id: septin-protein-O96429
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O96429.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'O96429: Glyceraldehyde-3-phosphate dehydrogenase; UniProtKB unreviewed
    (TrEMBL); taxon31285; indexed genes[''GAPDH'']. Unreviewed fragment; automatic
    family annotation is not an accession-specific localization experiment.'
  accessed_at: '2026-11-03T14:12:32.880744Z'
  support: supports
  snapshot_sha256: 8f4147f5eb3585b5a7daa71d01bb24a371fdf99f610e9ea85c88e9d652bca093
- evidence_id: septin-protein-Q4GZG4
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q4GZG4.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'Q4GZG4: Phosphoglycerate kinase; UniProtKB unreviewed (TrEMBL); taxon185431;
    indexed genes[''PGKC'']. Identity and current annotation do not alone certify
    accession-specific localization or biological necessity.'
  accessed_at: '2026-11-03T14:12:32.921789Z'
  support: supports
  snapshot_sha256: 8c47c8b1cee6761bac8d749997f75a2291f5226ed122df0231039ecefc15bdae
- evidence_id: septin-protein-P04789
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P04789.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'P04789: Triosephosphate isomerase, glycosomal; UniProtKB reviewed (Swiss-Prot);
    taxon5702; indexed genes[]. TIM is a recommended protein short name, with no indexed
    geneName; it is not a newly verified gene-index field. Glycosomal localization
    is corroborated separately by primary enzyme evidence.'
  accessed_at: '2026-11-03T14:12:34.018259Z'
  support: supports
  snapshot_sha256: 1be81f7b52889ef0374df9431e2da5a284f36343191ce5d8dff503f9056a52d6
- evidence_id: septin-protein-Q57W55
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q57W55.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'Q57W55: Glycosomal targeting signal receptor; UniProtKB reviewed (Swiss-Prot);
    taxon185431; indexed genes[''PEX5'']. Primary-cited cytosolic receptor/cycling
    context is not permanent membrane residency.'
  accessed_at: '2026-11-03T14:12:34.066357Z'
  support: supports
  snapshot_sha256: 86ae923215ae2007a36fc6746e09d1ff2b6c4737b310356843a38ce166c758fa
- evidence_id: septin-protein-Q57W97
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q57W97.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'Q57W97: Glycosomal targeting signal 2 receptor; UniProtKB reviewed (Swiss-Prot);
    taxon185431; indexed genes[''PEX7'']. Cytosolic localization has primary support;
    glycosome-matrix annotation includes by-similarity evidence.'
  accessed_at: '2026-11-03T14:12:35.097261Z'
  support: supports
  snapshot_sha256: 17eb8f82547e20f56476e6c80dfcac6cfb12237dc0eb195d62c7a6a85b0c6eb7
- evidence_id: septin-protein-Q38CL4
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q38CL4.json
  locator: Exact accession/status/name/gene/organism and relevant family, localization
    and evidence-code fields
  summary: 'Q38CL4: Glycosomal membrane protein PEX14; UniProtKB reviewed (Swiss-Prot);
    taxon185431; indexed genes[''PEX14'']. Exact PEX14 identity and primary-cited
    membrane annotation; large-pore dimensions and some translocation details are
    by similarity and are not promoted to direct trypanosome measurements.'
  accessed_at: '2026-11-03T14:12:35.114962Z'
  support: supports
  snapshot_sha256: 8f717db05261f969fe531e7bd7a625eb994d4310b16be58bb9bbee0901f3ca25
- evidence_id: septin-reviewed-TIM
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATIM%20AND%20taxonomy_id%3A5691%20AND%20reviewed%3Atrue&format=json&size=100
  locator: Complete bounded UniProt search response
  summary: The literal indexed-gene query returns zero; this is not absence of the
    protein or its functional alias.
  accessed_at: '2026-11-03T14:12:38.583396Z'
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProt query gene_exact:TIM AND taxonomy_id:5691 AND reviewed:true;
    format=json,size100, no date filter; complete response inspected at 2026-11-03T14:12:38.583396Z.
    Gene-index zero and protein-alias match are different queries, not a negative
    biological inference.
- evidence_id: septin-reviewed-TIM-protein-alias
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=protein_name%3A%22triosephosphate%20isomerase%22%20AND%20taxonomy_id%3A5702%20AND%20reviewed%3Atrue&format=json&size=100
  locator: Complete bounded UniProt search response
  summary: The complementary exact taxon/reviewed protein-name query returns only
    P04789, whose recommended short name is TIM. This substantiates the added example
    while preserving the lack of indexed geneName.
  accessed_at: '2026-11-03T14:15:04.281893Z'
  support: supports
  snapshot_sha256: 3d148624c46b3e05f1c48d60b330c5b1cb860bc1cb234f36628c247602b69714
  search_scope: UniProt query protein_name:"triosephosphate isomerase" AND taxonomy_id:5702
    AND reviewed:true; format=json,size100, no date filter; complete response inspected
    at 2026-11-03T14:15:04.281893Z. Gene-index zero and protein-alias match are different
    queries, not a negative biological inference.
- evidence_id: septin-IPR024111
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024111/
  locator: Current accession/type/name and only non-LLM authority description
  summary: Native family PEX5/PEX5L family is distinct from the other peroxin families.
    The exact current protein Q57W55 carries the corresponding InterPro xref. No one
    of these families denotes the whole multi-protein import apparatus; no uninspected
    complex identity or fixed stoichiometry is asserted.
  accessed_at: '2026-11-03T14:12:38.642727Z'
  support: supports
  snapshot_sha256: c8de3b8e3989f7d4c8fd494b92cf8f4401a36f632eabbdf607f8e87771c0688e
- evidence_id: septin-IPR044536
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044536/
  locator: Current accession/type/name and only non-LLM authority description
  summary: Native family PEX7 family is distinct from the other peroxin families.
    The exact current protein Q57W97 carries the corresponding InterPro xref. No one
    of these families denotes the whole multi-protein import apparatus; no uninspected
    complex identity or fixed stoichiometry is asserted.
  accessed_at: '2026-11-03T14:12:38.668092Z'
  support: supports
  snapshot_sha256: e4f14b115e211e1f8006e9bc7bdfa4db45f54952c64966047c01a44bf59fd3e9
- evidence_id: septin-IPR025655
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR025655/
  locator: Current accession/type/name and only non-LLM authority description
  summary: Native family PEX14 family is distinct from the other peroxin families.
    The exact current protein Q38CL4 carries the corresponding InterPro xref. No one
    of these families denotes the whole multi-protein import apparatus; no uninspected
    complex identity or fixed stoichiometry is asserted.
  accessed_at: '2026-11-03T14:12:38.790662Z'
  support: supports
  snapshot_sha256: 40e1bf52261db079f7fe27c19bad2e60775de3e6c1b5da3e06d58d753af4f1d8
- evidence_id: septin-PMID142663
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A142663%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and metadata only; no abstractText
  summary: Opperdoes and Borst1977, DOI10.1016/0014-5793(77)80476-6, exact title states
    localization of nine glycolytic enzymes. Native record has no abstract; detailed
    original fractionation tables/body were not inspected.
  accessed_at: '2026-11-03T14:15:04.281610Z'
  support: supports
  snapshot_sha256: 14a0012c9e96a72518f268b8b2b096e003be6af48b75eb2c56b7de6e0616ea26
  search_scope: Europe PMC exact EXT_ID:142663 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:15:04.281610Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID2940090
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A2940090%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: Misset, Bos and Opperdoes1986; complete primary abstract directly reports
    purification of nine enzymes from crude glycosomes, including phosphofructokinase
    and triosephosphate isomerase. This supports enzyme-cohort membership, not identity
    of every modern accession/strain or one assembled enzyme complex.
  accessed_at: '2026-11-03T14:12:37.084980Z'
  support: supports
  snapshot_sha256: ce6444055b433224a388a9fd7c1c355366fdd1c6ad784fbe27c33c94f375724b
  search_scope: Europe PMC exact EXT_ID:2940090 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:37.084980Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID10589985
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10589985%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: 'de Walque et al.1999: complete primary abstract reports PEX5 primarily
    cytosolic and in-vitro binding to PGK-C, consistent with receptor cycling.'
  accessed_at: '2026-11-03T14:12:37.302352Z'
  support: supports
  snapshot_sha256: 9d905239e00930c783a06fe8d9829395ca6b8cbed25778b45ac67098ee1493b7
  search_scope: Europe PMC exact EXT_ID:10589985 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:37.302352Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID17320990
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A17320990%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: 'Galland et al.2007: complete primary abstract reports PEX5/PEX7 receptor
    interaction/import phenotypes and apparently intact procyclic glycosomes by EM
    after depletion. Growth/import requirement is distinct from organelle-formation
    necessity.'
  accessed_at: '2026-11-03T14:12:37.443320Z'
  support: supports
  snapshot_sha256: 3a166a3b380b8fddeec10d1dc0aa4cde4c4011b0f42e7a2b38fd7b0da079051c
  search_scope: Europe PMC exact EXT_ID:17320990 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:37.443320Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID23994617
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A23994617%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: 'Gualdron-Lopez et al.2013: complete primary abstract reports cytosolic
    monoubiquitinated PEX5 and PEX4 recycling biology; it does not place all PEX5
    permanently in the membrane.'
  accessed_at: '2026-11-03T14:12:37.711415Z'
  support: supports
  snapshot_sha256: b480abfc7db346160b62183c1d6a6b40c5d5ae62d6e09e84299ce928dca8e73c
  search_scope: Europe PMC exact EXT_ID:23994617 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:37.711415Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID12386344
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12386344%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: 'Furuya et al.2002: complete primary abstract identifies PEX14 docking
    factor and RNAi-dependent import defects/sugar-conditional procyclic toxicity.
    Detailed localization is assessed separately from its primary body.'
  accessed_at: '2026-11-03T14:12:37.784419Z'
  support: supports
  snapshot_sha256: 14ec39249c6941a9318f2a064e9be252cb1cc4619f6bfc63a8b89a51edc66e71
  search_scope: Europe PMC exact EXT_ID:12386344 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:37.784419Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID12709066
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12709066%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: Moyersoen is first author and Choe second for DOI10.1046/j.1432-1033.2003.03582.x.
    Complete primary abstract supports glycosomal PEX14, N-terminal PEX5 binding and
    PTS1/PTS2/I-PTS matrix mislocalization after RNAi in bloodstream and procyclic
    forms; viability is not formation necessity.
  accessed_at: '2026-11-03T14:12:37.904483Z'
  support: supports
  snapshot_sha256: 86403edb92c4efeebd302ba9f6786451f4037b43595779a56e3d42ee9264efc7
  search_scope: Europe PMC exact EXT_ID:12709066 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:37.904483Z. No uninspected
    full body is inferred.
- evidence_id: septin-PMID22809509
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22809509%20AND%20SRC%3AMED&pageSize=25
  locator: Exact MED PMID, DOI, ordered authors, title and complete primary abstractText
  summary: 'Verplaetse et al.2012: complete primary abstract describes PEX13.1/PEX13.2
    docking complex and PEX13.1 anchoring or positioning PEX14. Cytosolic receptors
    and membrane docking apparatus are distinct participants.'
  accessed_at: '2026-11-03T14:12:38.050833Z'
  support: supports
  snapshot_sha256: 02f0bdeb859cf0241b2aa29864c3b20b979fc8bfabd21c5710bf2fa32dcbe702
  search_scope: Europe PMC exact EXT_ID:22809509 AND SRC:MED; format=json,resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:38.050833Z. No uninspected
    full body is inferred.
- evidence_id: septin-haanstra2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0806664105&pageSize=25
  locator: Exact DOI/PMID/title/authors and complete primary abstract
  summary: Haanstra et al.2008; primary abstract reports Glc6P accumulation and stronger
    glycerol/GK rescue support. The body qualifies the glucose mechanism.
  accessed_at: '2026-11-03T14:12:36.149339Z'
  support: supports
  snapshot_sha256: f8d1a43be70c2a8f07b58c3a866f619c60cbfaab73a09f23cd462b3b458d0a54
  search_scope: Europe PMC exact DOI:10.1073/pnas.0806664105; resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:36.149339Z. Bounded identifier
    retrieval, not an exhaustive literature search.
- evidence_id: septin-haanstra2016-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.bbamcr.2015.09.015&pageSize=25
  locator: Exact DOI/PMID/title/authors and complete review abstract
  summary: Haanstra et al.2016 is a secondary review. Complete review abstract supports
    specialized kinetoplastid peroxisomes, variable glycolytic enzyme content, peroxin
    import and life-stage remodeling; it is not a freshly inspected primary experiment.
  accessed_at: '2026-11-03T14:12:36.670722Z'
  support: supports
  snapshot_sha256: 4833c49da3fad086172172c05f9381bdfa266c28e5231070ac29be668d661614
  search_scope: Europe PMC exact DOI:10.1016/j.bbamcr.2015.09.015; resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:36.670722Z. Bounded identifier
    retrieval, not an exhaustive literature search.
- evidence_id: septin-bauer2017-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pntd.0005333&pageSize=25
  locator: Exact DOI/PMID/title/authors and complete review abstract
  summary: Bauer and Morris2017 is a secondary review. Its complete abstract presents
    ER-derived de novo glycosome biogenesis as a supported hypothesis, not directly
    demonstrated at that time; no membrane-origin mechanism is added.
  accessed_at: '2026-11-03T14:12:36.769320Z'
  support: supports
  snapshot_sha256: 401453c839de0bcd385c6172e9238480cd49e7e6139de24768326ac06ad3747d
  search_scope: Europe PMC exact DOI:10.1371/journal.pntd.0005333; resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:36.769320Z. Bounded identifier
    retrieval, not an exhaustive literature search.
- evidence_id: septin-dezoysa1994-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1007/BF00309930&pageSize=25
  locator: Exact DOI/PMID/title/authors and complete primary abstract
  summary: de Zoysa and Connerton1994; complete primary abstract directly demonstrates
    C-terminally modified CAT reporter targeting under nutritional acetate induction
    in Neurospora crassa, distinguishes glyoxysomes carrying glyoxylate-cycle enzymes
    from catalase-containing peroxisome-like microbodies, and reports sequence-dependent
    targeting with ARM ineffective. This is the current abstract tier, not a current
    full-body or direct translocation movie inspection.
  accessed_at: '2026-11-03T14:12:36.932029Z'
  support: supports
  snapshot_sha256: a249a609ce7cf4d9663970634e9e7685e35d40958c2b927c1f479af8b2610485
  search_scope: Europe PMC exact DOI:10.1007/BF00309930; resultType=core,pageSize25,one
    result,no date filter; actual fetch 2026-11-03T14:12:36.932029Z. Bounded identifier
    retrieval, not an exhaustive literature search.
- evidence_id: septin-opperdoes1977-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/0014-5793%2877%2980476-6&pageSize=25
  locator: Exact DOI query returned zero; separate native PMID retrieval succeeded
  summary: This DOI-index miss is not publication absence. Native PMID142663 independently
    verifies DOI/title/authors; no abstract is available there.
  accessed_at: '2026-11-03T14:12:36.076039Z'
  support: supports
  snapshot_sha256: 74deeb8eecb605c09b4f4834b345e01eee10981f13d6db7c67e310a42be4638b
  search_scope: Europe PMC exact DOI:10.1016/0014-5793(77)80476-6; resultType=core,pageSize25,no
    date filter; returned zero at 2026-11-03T14:12:36.076039Z. Follow-up exact PMID142663
    returned the source; no negative existence conclusion.
- evidence_id: septin-haanstra2008-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2584722/
  locator: Complete Results sec1/sec2–4 with Fig2–5 captions, Discussion sec5, Experimental
    Procedures sec6/sec7–13; no source pixels, separate supplements or raw data
  summary: 'Fresh genuine PMC body: procyclic29–13 PEX14-RNAi cells accumulate Glc6P
    after glucose, but the paper explicitly calls that an unstringent mechanism test
    because preferential PGI mislocalization can truncate the pathway; PF449 did not
    significantly accumulate Glc6P. Glycerol/Gly3P accumulation plus GK-knockdown
    rescue supplies the stronger test. TIM activity partially mislocalizes on digitonin
    fractionation. Models removing a membrane are distinct from biological partial-import
    perturbations; reference-strain protein examples are not the experimental strains.'
  accessed_at: '2026-11-03T14:12:38.089900Z'
  support: supports
  snapshot_sha256: d9e20db7ccce3901dd9c7a91098ff12bb399e8e68da4fc443e80e11b0b42521b
- evidence_id: septin-furuya2002-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/137857/
  locator: Complete Materials and Methods sec1/sec2–7, Results sec8/sec9–13 including
    Fig1–4 captions, and Discussion sec14; no pixels/raw data
  summary: Fresh genuine PMC body supports PEX14 glycosomal membrane association by
    fractionation, carbonate extraction and punctate immunostaining; RNAi causes matrix-protein
    mislocalization and context-dependent lethality. Procyclic29–13 and bloodstream
    single-marker assays, recombinant EATRO110 sequence material and engineered E.coli
    protein expression are distinct. Proposed metabolic explanations and cross-species
    extension are not directly measured universals.
  accessed_at: '2026-11-03T14:12:38.467089Z'
  support: supports
  snapshot_sha256: bd05175d3ca6539da02455c6e95c1feb632c993b33565f59fc1fb82bbf431ace
- evidence_id: septin-access-haanstra2008-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2584722.1/PMC2584722.1.xml
  locator: Actual source-route error retained in scratch source-receipts.json
  summary: '<HTTPError 404: ''Not Found''>; not scientific body evidence. Successful
    alternative bodies or metadata are separately scoped.'
  accessed_at: '2026-11-03T14:12:38.322913Z'
  support: context_only
  snapshot_sha256: ce347547bddf6ad50cd419558a645766ac03a39a5416b4ed6c9b742761197b9c
- evidence_id: septin-access-furuya2002-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC137857.1/PMC137857.1.xml
  locator: Actual source-route error retained in scratch source-receipts.json
  summary: '<HTTPError 404: ''Not Found''>; not scientific body evidence. Successful
    alternative bodies or metadata are separately scoped.'
  accessed_at: '2026-11-03T14:12:38.526393Z'
  support: context_only
  snapshot_sha256: ce347547bddf6ad50cd419558a645766ac03a39a5416b4ed6c9b742761197b9c
- evidence_id: septin-access-opperdoes1977-pdf
  kind: authority
  reference: https://febs.onlinelibrary.wiley.com/doi/pdf/10.1016/0014-5793%2877%2980476-6
  locator: Actual source-route error retained in scratch source-receipts.json
  summary: '<HTTPError 403: ''Forbidden''>; not scientific body evidence. Successful
    alternative bodies or metadata are separately scoped.'
  accessed_at: '2026-11-03T14:15:04.282020Z'
  support: context_only
  snapshot_sha256: ce347547bddf6ad50cd419558a645766ac03a39a5416b4ed6c9b742761197b9c
- evidence_id: septin-dezoysa1994-pdf
  kind: authority
  reference: https://link.springer.com/content/pdf/10.1007/BF00309930.pdf
  locator: Publisher PDF route returned HTML Client Challenge despite HTTP200
  summary: This is not a genuine PDF/article body. Current scientific support uses
    the complete primary abstract; the original review full-PDF claim remains historical
    and is not reused as a new body inspection.
  accessed_at: '2026-11-03T14:12:38.543204Z'
  support: context_only
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: septin-dezoysa1994-encoded-pdf
  kind: authority
  reference: https://link.springer.com/content/pdf/10.1007%2FBF00309930.pdf
  locator: Publisher PDF route returned HTML Client Challenge despite HTTP200
  summary: This is not a genuine PDF/article body. Current scientific support uses
    the complete primary abstract; the original review full-PDF claim remains historical
    and is not reused as a new body inspection.
  accessed_at: '2026-11-03T14:15:04.281965Z'
  support: context_only
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue and actual target taxon scope
  summary: No matched Trypanosoma, kinetoplastid or Neurospora host/dataset appears.
    All five complete records assert glycolysis/PEX import or glyoxylate-cycle/matrix-targeting
    pathways, so all require an applicability assessment even where their graphs are
    topological. No matched-host downstream gene/module query applies; heterologous
    E.coli protein expression is not the target organism. Catalogue noncoverage is
    not biological absence.
  accessed_at: '2026-11-03T14:12:38.863573Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official GET /api/datasets at 2026-11-03T14:12:38.863573Z; complete
    returned organism names/IDs/dataset keys inspected for Trypanosoma/brucei/Kinetoplastea/Kinetoplastida/Neurospora/crassa
    and actual named subspecies/strain context, no date filter. No unrelated or engineered-host
    proxy and no downstream module query.
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical canary datasets invocation00:49:00.848907Z–00:49:00.863225Z
  summary: Actual earlier exit1 PermissionError reading pyvenv.cfg. No fresh runner
    invocation/success is claimed; current official-catalogue fallback is a separate
    retrieval.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-glyoxysome-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/glyoxysome.yaml
  locator: Frozen whole-glyoxysome neighbor, boundary/identity context only
  summary: Whole organelle, lumen and membrane identities/parthood are distinct. This
    context read does not independently review the whole-neighbor composition or dispose
    of its historical findings.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 4f1e29ea41f06149b1f638a6b94949e9f6c7246bfb5ed9b954eb5ded839858a4
- evidence_id: septin-stale-glycosome-diff
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/glycosome-stale.diff
  locator: Exact original-source to current-source diff
  summary: Only scientific changes are addition of reviewed P04789/TIM example and
    peroxin apparatus PROTEIN to PROTEIN_COMPLEX retyping, plus associated history.
    Neither inherited attribution, glucose-mechanism qualification nor membrane molecular-grounding
    issue is fixed by those changes.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 3aabb508ec2c6498bda2a693815d35ce5e1b22095c12684047f28953457e0e0b
- evidence_id: septin-historical-2462
  kind: authority
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2462
  locator: Current root-fetched issue body item4 and closure comment; historical context
    only
  summary: Closed grouped issue2462 includes the glycosome peroxin-type change alongside
    unrelated records. Closure cites PR2464/commit31fd33d9556ea5627b36d50ab608ccb9464f9353.
    This review checks the current glycosome change without newly resolving the entire
    group or reopening that peroxin item.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: context_only
  snapshot_sha256: abe5bab7f2b60e9179facfec2f469e19784b43d024dccd303e2fa5298b220ed4
- evidence_id: septin-source-access
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/source-receipts.json
  locator: Actual fresh source URLs/statuses/access timestamps/hashes
  summary: Primary PMC bodies and complete abstract/authority tiers are separated.
    Two S3 XML routes returned404; canonical PMC routes yielded genuine bodies. Springer
    PDF routes yielded challenges, and Opperdoes publisher route403; current body
    access is not inferred from success status alone.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: ce347547bddf6ad50cd419558a645766ac03a39a5416b4ed6c9b742761197b9c
- evidence_id: septin-common-policy-reuse
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/adversary-septin/common-policy-hash-reuse.json
  locator: Seventeen frozen common policy/schema/native source byte comparisons
  summary: Current common bytes match prior read inputs; structured-source and component/schema
    rules additionally reread. Only the explicitly frozen glyoxysome neighbor was
    added to this slice.
  accessed_at: '2026-11-03T14:25:02.256291Z'
  support: supports
  snapshot_sha256: 907dcf3b188dafeb9902bb7183fc7a1fbeb014db059b0e5ffedc0dc6c11e071d
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:16:18.244943Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: f05d032ef80ac16e4bc06fd47281e80507685096289e6331922edffa5c260548
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:11:08.893121Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:10:51.214640Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:10:47.093520Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T14:10:51.001675Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T14:26:55Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 5f4e2b9fe4f1c1fa4e62f28f6028fa6cf09088a04e5ce21fd3b154986a07ea43
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2366/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T14:12:34.000246Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: d9bcdd4cf2dcd6c22774e737d81c1ed6ae4eaa3ca5f613c4ababd2028bb8bae9
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2366
    synthesis
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
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: Complete target has no component protein_examples and zero GENE_OR_PROTEIN
    nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway
    assertions are independently assessed. Both native commands exit0; these do not
    establish scientific mechanism, exact molecular families or formation necessity.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-native-flagellar_pocket-verify
  - plaque-native-flagellar_pocket-causal
  - plaque-protein-contract
- assessment_id: plaque-t0-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Original validates/renders and all 15 historical inputs match its source.
    Current target unchanged; exact inherited F1 lineage retained. No historical group/neighbor/category
    issue is terminally resolved.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-original-checks
- assessment_id: plaque-t0-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: All current evidence, histories, discussions and graphs inspected. No target
    image assets, verbatim snippets, trait links or quantitative properties to audit.
    Optional enzymes/transporters/cytoskeletal features do not justify invented accessions
    or completeness defects. PROPOSED unchanged.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-rubric
- assessment_id: plaque-t0-adapter
  area: scope
  topic: Actual molecular/pathway trigger and catalogue noncoverage
  outcome: supported
  summary: BILBO1 and endo/exocytic trafficking are explicit current assertions. Original
    check explicitly excluded iModulonDB on an expression-only rationale, not an omission.
    Fresh complete catalogue has no relevant host, so no downstream matched-gene/module
    query applies. Primary/authority fallback is complete within declared tiers; historical
    runner remains separately dated unavailable.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t1-native
  area: schema
  topic: Represented protein inventory and graph actor coverage
  outcome: supported
  summary: Complete target has no component protein_examples and zero GENE_OR_PROTEIN
    nodes. Mechanical coverage is empty-inventory scope; narrative protein/pathway
    assertions are independently assessed. Both native commands exit0; these do not
    establish scientific mechanism, exact molecular families or formation necessity.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-native-food_vacuole-verify
  - plaque-native-food_vacuole-causal
  - plaque-protein-contract
- assessment_id: plaque-t1-provenance
  area: provenance
  topic: Original immutable pair and frozen-input currentness
  outcome: supported
  summary: Original validates/renders and all 14 historical inputs match its source.
    Current target changed; membrane boundary delta and history substantively reassessed
    against current sources. No historical group/neighbor/category issue is terminally
    resolved.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-original-checks
- assessment_id: plaque-t1-coverage
  area: completeness
  topic: Complete current fields and optional inventories
  outcome: supported
  summary: All current evidence, histories, discussions and graphs inspected. No target
    image assets, verbatim snippets, trait links or quantitative properties to audit.
    Optional enzymes/transporters/cytoskeletal features do not justify invented accessions
    or completeness defects. PROPOSED unchanged.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-rubric
- assessment_id: plaque-t1-adapter
  area: scope
  topic: Actual molecular/pathway trigger and catalogue noncoverage
  outcome: supported
  summary: Hemoglobin catabolism/heme detoxification and named digestive-vacuole transporters
    are explicit current assertions. Original check explicitly excluded iModulonDB
    on an expression-only rationale, not an omission. Fresh complete catalogue has
    no relevant host, so no downstream matched-gene/module query applies. Primary/authority
    fallback is complete within declared tiers; historical runner remains separately
    dated unavailable.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t0-identity
  area: identity
  topic: Whole pocket versus membrane and collar
  outcome: supported
  summary: GO0020016 is the plasma-membrane invagination with exact flagellar-pocket
    synonym. SUBCELLULAR_REGION is appropriate for this invagination, distinct from
    whole membrane0020018 and collar1990900. The identity is not changed by the molecular
    component defect.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-neighbor-membrane
  - plaque-neighbor-collar
- assessment_id: plaque-t0-taxonomy
  area: scope
  topic: T. brucei life-stage and strain scopes
  outcome: supported
  summary: Species5691 is T. brucei. Lacomble uses procyclic427, Gadelha bloodstream
    forms, Bonhivers distinct procyclic/bloodstream lines. COMMON is qualitative,
    not a measured prevalence. Single-pocket description is read in routine cell architecture
    with duplication explicitly retained; no all-cell-cycle one-pocket exclusion inferred.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-tax-5691
  - plaque-pmc-PMC2714436
  - plaque-pmc-PMC2755463
  - plaque-bonhivers2008-plos
- assessment_id: plaque-t0-membrane
  area: grounding
  topic: Molecular lipid row incorrectly grounded to whole membrane
  outcome: concern
  summary: The ciliary_pocket_membrane row has component_type LIPID but grounding
    GO:0020018, whose native identity is the complete ciliary pocket membrane. Schema
    StructuralComponent requires a molecular building block and distinguishes chemical
    lipid grounding from GO sub-complex grounding. The graph component_ref repeats
    the same invalid molecular correspondence. Correct membrane topology and membrane/collar
    membership do not resolve this field-level identity mismatch.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-schema-policy
  - plaque-go
  - plaque-pmc-PMC2755463
  - plaque-neighbor-membrane
- assessment_id: plaque-t0-collar
  area: evidence
  topic: Collar membership and new-pocket formation
  outcome: supported
  summary: GO1990900 identifies a collar protein complex at the neck; Bonhivers primary
    localization and RNAi support BILBO1-dependent formation of a new collar/pocket.
    The old pocket persists during knockdown, so this is not total absence of all
    pockets or universal necessity of every collar protein.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-bonhivers2008-plos
  - plaque-neighbor-collar
- assessment_id: plaque-t0-functions
  area: evidence
  topic: Scoped architecture and trafficking
  outcome: supported
  summary: Lacomble primary architecture and Gadelha membrane/uptake observations
    support pocket/neck domains and trafficking context. Field/Halliday are explicitly
    secondary abstract-level review support for endo/exocytosis, not fresh experimental
    proof. Lacomble selected discussion cites Bonhivers for collar BILBO1/biogenesis;
    that source is inspected directly.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-pmc-PMC2714436
  - plaque-pmc-PMC2755463
  - plaque-bonhivers2008-plos
  - plaque-doi-10.1038_nrmicro2221
  - plaque-doi-10.1016_j.pt.2020.11.005
- assessment_id: plaque-t0-graph
  area: graph
  topic: Three descriptive boundary/traffic edges and invalid material correspondence
  outcome: concern
  summary: 'All three NONMECHANISTIC relations remain supported: membrane lines pocket,
    collar localizes at neck and pocket supports trafficking. Whole membrane STRUCTURE
    grounding is valid; its component_ref propagates the invalid GO-whole-membrane
    to LIPID correspondence. Correct topology does not repair F1.'
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-pmc-PMC2714436
  - plaque-bonhivers2008-plos
  - plaque-doi-10.1016_j.pt.2020.11.005
  - plaque-schema-policy
- assessment_id: plaque-t0-limits
  area: evidence
  topic: Boundary mechanism and chemical necessity
  outcome: unknown
  summary: Exact lipid mixture, molecular mechanisms establishing domains and complete
    collar constituent necessity are not established here. No figure pixels, raw tomograms
    or supplemental quantitative reanalysis performed; caption/text inspection remains
    distinct.
  target_ids:
  - GO:0020016
  evidence_ids:
  - plaque-current-0
  - plaque-pmc-PMC2755463
  - plaque-bonhivers2008-plos
  - plaque-rubric
- assessment_id: plaque-t1-identity
  area: identity
  topic: Parasite digestive vacuole
  outcome: supported
  summary: GO0020020 exact identity and digestive-vacuole synonym match the defined
    host-cytoplasm digestion compartment. MEMBRANE_BOUNDED_ORGANELLE matches reviewed
    anatomy; not a generic endosome, lysosome or separate membrane record.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-wiser2024-numeric
- assessment_id: plaque-t1-taxonomy
  area: scope
  topic: Explicit P. falciparum blood-stage scope
  outcome: supported
  summary: NCBITaxon5833 is P. falciparum. Lamarque primary abstract directly supports
    its FV-enriched proteomic fraction and the canonical example. Current occurrence
    note explicitly declines broader Plasmodium/Apicomplexa occurrence claims; COMMON
    is qualitative. Fractions are not treated as pure/exhaustive constituent inventories.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-tax5833
  - plaque-lamarque2008-meta
- assessment_id: plaque-t1-composition
  area: grounding
  topic: Reviewed label-only aggregate membrane
  outcome: supported
  summary: Generic LIPID constituent is an explicitly REVIEWED_LABEL_ONLY aggregate
    with no false whole-membrane GO grounding or guessed chemical identity. Cowman
    directly localizes Pgh1 to its membrane; Wiser supplies secondary acidic-boundary/transport
    context. Exact lipid/protein-family composition and individual necessity are deliberately
    unasserted.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-cowman1991-meta
  - plaque-wiser2024-numeric
  - plaque-schema-policy
- assessment_id: plaque-t1-functions
  area: evidence
  topic: Hemoglobin digestion and heme detoxification
  outcome: supported
  summary: Wiser inspected review sections3.2/4 support acid-compartment proteolysis,
    heme release and sequestration as hemozoin. Lamarque supports the experimental
    FV-fraction context. These remain broad functions; no exact enzyme sequence, stoichiometry
    or fully resolved biocrystallization mechanism is claimed.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-wiser2024-numeric
  - plaque-lamarque2008-meta
- assessment_id: plaque-t1-graph
  area: graph
  topic: Three original NONMECHANISTIC digestion/hemozoin relations
  outcome: supported
  summary: Vacuole digests hemoglobin, hemoglobin releases heme during proteolysis
    and heme crystallizes into hemozoin are supported by inspected secondary review
    text. No unverified CHEBI IDs are restored; chemical labels and descriptive graph
    scope do not assert direct molecular catalytic mechanism.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-wiser2024-numeric
  - plaque-graph-rubric
- assessment_id: plaque-t1-stale-boundary
  area: graph
  topic: Substantive refresh of new membrane STRUCTURE node and bounds edge
  outcome: supported
  summary: Current delta adds membrane STRUCTURE with existing reviewed-label-only
    component_ref and a bounds edge separating acidic lumen from parasite cytosol.
    Cowman primary abstract directly locates Pgh1 on the digestive-vacuole membrane;
    Wiser inspected body explicitly discusses compartment properties and transport
    across that boundary. This supports topology, not novel transporter direction
    or formation mechanism. The changed record can be accurately reviewed in this
    PR without record edits.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-cowman1991-meta
  - plaque-wiser2024-numeric
  - plaque-original-checks
- assessment_id: plaque-t1-limits
  area: evidence
  topic: Exact membrane chemistry and primary proteome/biocrystallization detail
  outcome: unknown
  summary: Cowman/Lamarque access is primary abstract only; exact underlying images,
    fraction purity beyond stated abstract limits and raw proteome were not reanalysed.
    Wiser is secondary body support. Optional PfCRT/Pgh1/protease/proton-pump accessions
    and exact hemozoin mechanism are not inferred or fabricated.
  target_ids:
  - GO:0020020
  evidence_ids:
  - plaque-current-1
  - plaque-cowman1991-meta
  - plaque-lamarque2008-meta
  - plaque-wiser2024-numeric
  - plaque-rubric
- assessment_id: micro-fungal_type_vacuole-identity
  area: identity
  topic: Exact structure and boundary identity
  outcome: supported
  summary: Exact fungal-type vacuole identity denotes the membrane-bounded whole,
    both lytic and storage; exact recorded morphology synonym matches. Whole/lumen/membrane
    remain separate identities.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-go
  - micro-ols-0000324
  - micro-policy
  - micro-ancestors-whole
- assessment_id: micro-fungal_type_vacuole-taxon
  area: scope
  topic: Species, reference strain and experimental scope
  outcome: supported
  summary: Saccharomyces species4932 supports canonical example and qualitative COMMON
    occurrence. UniProt559292 is reference S288C; Parzych SEY6210 derivatives are
    retained as experimental context and not renamed S288C. No prevalence percentage
    or universal fungal distribution asserted.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-tax-4932
  - micro-tax-559292
  - micro-li2009-body
  - micro-parzych2018-body
- assessment_id: micro-fungal_type_vacuole-composition
  area: grounding
  topic: Component class, instances and necessity boundary
  outcome: supported
  summary: Heterogeneous soluble acid hydrolases span A1/S8/S10 families, so class-level
    reviewed-label-only grounding and UNKNOWN formation essentiality are appropriate.
    Three exact reviewed taxon-paired examples are supported; PRC1 is correctly representative
    despite PRE10 alias collision.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-protein-contract
  - micro-go
  - micro-up-P07267
  - micro-up-P00729
  - micro-up-P09232
  - micro-unique-PEP4
  - micro-unique-PRB1
  - micro-unique-PRC1
  - micro-li2009-body
- assessment_id: micro-fungal_type_vacuole-functions
  area: evidence
  topic: Storage, hydrolysis and acidification source scope
  outcome: supported
  summary: Storage/degradative functions are supported by exact GO definition and
    Li/Kane secondary synthesis. Named soluble protease roles agree with primary Parzych
    and native identities. Delivery routes do not make all delivered cargo a stable
    resident.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-go
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
- assessment_id: micro-fungal_type_vacuole-graph
  area: graph
  topic: Every current graph node and edge
  outcome: supported
  summary: 'All seven current NONMECHANISTIC FUNCTION edges checked: membrane bounds
    lumen; whole is a vacuole; lumen stores small molecules; hydrolases act there;
    lumen compartmentalizes degradation; new membrane and lumen part_of whole. Both
    new direct GO parthood notes are exact.'
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-go
  - micro-ols-0000324
  - micro-policy
  - micro-protein-contract
  - micro-li2009-body
  - micro-kane2006-body
  - micro-native-fungal_type_vacuole-causal
- assessment_id: micro-fungal_type_vacuole-limits
  area: evidence
  topic: Experimental and molecular completeness limits
  outcome: unknown
  summary: Neither exact identity nor a localization annotation establishes individual
    formation necessity or a complete molecular inventory. Primary Parzych single/double-mutant
    results preserve redundancy; lower pH is optimal but not universally essential
    for hydrolase activity. Secondary review synthesis and current abstract-only evidence
    remain explicitly scoped.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-protein-contract
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
  - micro-pmid-14562095
  - micro-pmid-23708375
- assessment_id: micro-fungal_type_vacuole-coverage
  area: completeness
  topic: Entire record, discussions and optional evidence
  outcome: supported
  summary: All current fields/history/discussions read. No target image, quantitative
    physical property, trait link or verbatim snippet is asserted. PROPOSED status
    retained. Optional family/lipid/machinery groundings and acknowledged unknowns
    are not fabricated findings; no historical issue or category-wide disposition
    is made.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-prior-fungal_type_vacuole
  - micro-policy
- assessment_id: micro-fungal_type_vacuole-schema
  area: schema
  topic: Original immutability and actual native protein coverage
  outcome: supported
  summary: Original YAML validates and exact Markdown render agrees; original frozen
    target verified through git source bytes. Current source-head native verify/causal
    commands passed with separately documented inventories; deterministic success
    is not scientific membership proof.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-original-pairs
  - micro-prior-fungal_type_vacuole
  - micro-native-fungal_type_vacuole-verify
  - micro-native-fungal_type_vacuole-causal
- assessment_id: micro-fungal_type_vacuole-adapter-defect
  area: provenance
  topic: Original expression-only exclusion requires correction
  outcome: concern
  summary: Original check exists but excludes iModulonDB solely because expression-module
    inference is unused. The target asserts named proteins, hydrolase pathways or
    V-ATPase acidification; native policy requires coverage assessment. This is a
    review-bundle defect, not a scientific record curation finding.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-prior-fungal_type_vacuole
  - micro-policy
- assessment_id: micro-fungal_type_vacuole-adapter-current
  area: evidence
  topic: Current exact-organism catalogue applicability
  outcome: not_applicable
  summary: Fresh complete official catalogue has no Saccharomyces/cerevisiae/S288C
    match. No downstream gene/module query is applicable without an unmatched organism
    proxy. Historical runner failure remains separately dated; bounded noncoverage
    is not negative biological evidence.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-record-fungal_type_vacuole
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
- assessment_id: micro-fungal_type_vacuole_lumen-identity
  area: identity
  topic: Exact structure and boundary identity
  outcome: supported
  summary: Exact internal volume is a SUBCELLULAR_REGION; enclosing membrane is boundary,
    not the lumen substance. Direct lumen is_a and part_of are confirmed.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-go
  - micro-ols-0000328
  - micro-policy
- assessment_id: micro-fungal_type_vacuole_lumen-taxon
  area: scope
  topic: Species, reference strain and experimental scope
  outcome: supported
  summary: Saccharomyces species4932 supports canonical example and qualitative COMMON
    occurrence. UniProt559292 is reference S288C; Parzych SEY6210 derivatives are
    retained as experimental context and not renamed S288C. No prevalence percentage
    or universal fungal distribution asserted.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-tax-4932
  - micro-tax-559292
  - micro-li2009-body
  - micro-parzych2018-body
- assessment_id: micro-fungal_type_vacuole_lumen-composition
  area: grounding
  topic: Component class, instances and necessity boundary
  outcome: supported
  summary: No component inventory is required for a volume. Three reviewed xrefs identify
    hydrolase actors within it; native UNANCHORED_WITH_UNIPROT is the explicit permitted
    route, not a broken component_ref. The resolved membrane-as-boundary discussion
    agrees.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-protein-contract
  - micro-go
  - micro-up-P07267
  - micro-up-P00729
  - micro-up-P09232
  - micro-unique-PEP4
  - micro-unique-PRB1
  - micro-unique-PRC1
  - micro-li2009-body
- assessment_id: micro-fungal_type_vacuole_lumen-functions
  area: evidence
  topic: Storage, hydrolysis and acidification source scope
  outcome: supported
  summary: Storage/degradative functions are supported by exact GO definition and
    Li/Kane secondary synthesis. Named soluble protease roles agree with primary Parzych
    and native identities. Delivery routes do not make all delivered cargo a stable
    resident.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-go
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
- assessment_id: micro-fungal_type_vacuole_lumen-graph
  area: graph
  topic: Every current graph node and edge
  outcome: supported
  summary: 'All six NONMECHANISTIC FUNCTION edges checked: lumen is_a broader lumen;
    part_of whole; membrane bounds it; lumen stores molecules; hydrolases act there;
    lumen compartmentalizes degradation. Xrefs ground actors without inventing a complete
    enzyme inventory.'
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-go
  - micro-ols-0000328
  - micro-policy
  - micro-protein-contract
  - micro-li2009-body
  - micro-kane2006-body
  - micro-native-fungal_type_vacuole_lumen-causal
- assessment_id: micro-fungal_type_vacuole_lumen-limits
  area: evidence
  topic: Experimental and molecular completeness limits
  outcome: unknown
  summary: Neither exact identity nor a localization annotation establishes individual
    formation necessity or a complete molecular inventory. Primary Parzych single/double-mutant
    results preserve redundancy; lower pH is optimal but not universally essential
    for hydrolase activity. Secondary review synthesis and current abstract-only evidence
    remain explicitly scoped.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-protein-contract
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
  - micro-pmid-14562095
  - micro-pmid-23708375
- assessment_id: micro-fungal_type_vacuole_lumen-coverage
  area: completeness
  topic: Entire record, discussions and optional evidence
  outcome: supported
  summary: All current fields/history/discussions read. No target image, quantitative
    physical property, trait link or verbatim snippet is asserted. PROPOSED status
    retained. Optional family/lipid/machinery groundings and acknowledged unknowns
    are not fabricated findings; no historical issue or category-wide disposition
    is made.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-prior-fungal_type_vacuole_lumen
  - micro-policy
- assessment_id: micro-fungal_type_vacuole_lumen-schema
  area: schema
  topic: Original immutability and actual native protein coverage
  outcome: supported
  summary: Original YAML validates and exact Markdown render agrees; original frozen
    target verified through git source bytes. Current source-head native verify/causal
    commands passed with separately documented inventories; deterministic success
    is not scientific membership proof.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-original-pairs
  - micro-prior-fungal_type_vacuole_lumen
  - micro-native-fungal_type_vacuole_lumen-verify
  - micro-native-fungal_type_vacuole_lumen-causal
- assessment_id: micro-fungal_type_vacuole_lumen-adapter-defect
  area: provenance
  topic: Original expression-only exclusion requires correction
  outcome: concern
  summary: Original check exists but excludes iModulonDB solely because expression-module
    inference is unused. The target asserts named proteins, hydrolase pathways or
    V-ATPase acidification; native policy requires coverage assessment. This is a
    review-bundle defect, not a scientific record curation finding.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-prior-fungal_type_vacuole_lumen
  - micro-policy
- assessment_id: micro-fungal_type_vacuole_lumen-adapter-current
  area: evidence
  topic: Current exact-organism catalogue applicability
  outcome: not_applicable
  summary: Fresh complete official catalogue has no Saccharomyces/cerevisiae/S288C
    match. No downstream gene/module query is applicable without an unmatched organism
    proxy. Historical runner failure remains separately dated; bounded noncoverage
    is not negative biological evidence.
  target_ids:
  - GO:0000328
  evidence_ids:
  - micro-record-fungal_type_vacuole_lumen
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
- assessment_id: micro-fungal_type_vacuole_membrane-identity
  area: identity
  topic: Exact structure and boundary identity
  outcome: supported
  summary: Exact fungal vacuole lipid boundary is MEMBRANE, distinct from its internal
    volume and whole organelle. Broader vacuolar membrane parentage is transitive,
    not claimed a direct GO subclass edge.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-go
  - micro-ols-0000329
  - micro-policy
  - micro-ancestors-membrane
- assessment_id: micro-fungal_type_vacuole_membrane-taxon
  area: scope
  topic: Species, reference strain and experimental scope
  outcome: supported
  summary: Saccharomyces species4932 supports canonical example and qualitative COMMON
    occurrence. UniProt559292 is reference S288C; Parzych SEY6210 derivatives are
    retained as experimental context and not renamed S288C. No prevalence percentage
    or universal fungal distribution asserted.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-tax-4932
  - micro-tax-559292
  - micro-li2009-body
  - micro-parzych2018-body
- assessment_id: micro-fungal_type_vacuole_membrane-composition
  area: grounding
  topic: Component class, instances and necessity boundary
  outcome: supported
  summary: The single lipid-bilayer constituent describes defining boundary material;
    ESSENTIAL is collective boundary constitution, not molecular knockout proof. The
    separate V-ATPase is correctly a STRUCTURE complex node, not a protein-family
    lipid component.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-protein-contract
  - micro-go
  - micro-up-P07267
  - micro-up-P00729
  - micro-up-P09232
  - micro-unique-PEP4
  - micro-unique-PRB1
  - micro-unique-PRC1
  - micro-li2009-body
- assessment_id: micro-fungal_type_vacuole_membrane-functions
  area: evidence
  topic: Storage, hydrolysis and acidification source scope
  outcome: supported
  summary: Vacuolar membrane houses vacuolar V-ATPase proton pumps, supported by GO0016471/GO0007035
    and scoped Kane/Li reviews. No complete composition, assembly mechanism or claim
    that every V-type complex is vacuolar is asserted.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-go
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
- assessment_id: micro-fungal_type_vacuole_membrane-graph
  area: graph
  topic: Every current graph node and edge
  outcome: supported
  summary: 'All five NONMECHANISTIC FUNCTION edges checked: membrane is_a broader
    membrane; part_of whole; bounds lumen; vacuolar V-ATPase resides there and participates
    in acidification. Edges express bounded topology/function, not a complete causal
    assembly model.'
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-go
  - micro-ols-0000329
  - micro-policy
  - micro-protein-contract
  - micro-li2009-body
  - micro-kane2006-body
  - micro-native-fungal_type_vacuole_membrane-causal
- assessment_id: micro-fungal_type_vacuole_membrane-limits
  area: evidence
  topic: Experimental and molecular completeness limits
  outcome: unknown
  summary: Neither exact identity nor a localization annotation establishes individual
    formation necessity or a complete molecular inventory. Primary Parzych single/double-mutant
    results preserve redundancy; lower pH is optimal but not universally essential
    for hydrolase activity. Secondary review synthesis and current abstract-only evidence
    remain explicitly scoped.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-protein-contract
  - micro-li2009-body
  - micro-kane2006-body
  - micro-parzych2018-body
  - micro-pmid-14562095
  - micro-pmid-23708375
- assessment_id: micro-fungal_type_vacuole_membrane-coverage
  area: completeness
  topic: Entire record, discussions and optional evidence
  outcome: supported
  summary: All current fields/history/discussions read. No target image, quantitative
    physical property, trait link or verbatim snippet is asserted. PROPOSED status
    retained. Optional family/lipid/machinery groundings and acknowledged unknowns
    are not fabricated findings; no historical issue or category-wide disposition
    is made.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-prior-fungal_type_vacuole_membrane
  - micro-policy
- assessment_id: micro-fungal_type_vacuole_membrane-schema
  area: schema
  topic: Original immutability and actual native protein coverage
  outcome: supported
  summary: Original YAML validates and exact Markdown render agrees; original frozen
    target verified through git source bytes. Current source-head native verify/causal
    commands passed with separately documented inventories; deterministic success
    is not scientific membership proof.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-original-pairs
  - micro-prior-fungal_type_vacuole_membrane
  - micro-native-fungal_type_vacuole_membrane-verify
  - micro-native-fungal_type_vacuole_membrane-causal
- assessment_id: micro-fungal_type_vacuole_membrane-adapter-defect
  area: provenance
  topic: Original expression-only exclusion requires correction
  outcome: concern
  summary: Original check exists but excludes iModulonDB solely because expression-module
    inference is unused. The target asserts named proteins, hydrolase pathways or
    V-ATPase acidification; native policy requires coverage assessment. This is a
    review-bundle defect, not a scientific record curation finding.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-prior-fungal_type_vacuole_membrane
  - micro-policy
- assessment_id: micro-fungal_type_vacuole_membrane-adapter-current
  area: evidence
  topic: Current exact-organism catalogue applicability
  outcome: not_applicable
  summary: Fresh complete official catalogue has no Saccharomyces/cerevisiae/S288C
    match. No downstream gene/module query is applicable without an unmatched organism
    proxy. Historical runner failure remains separately dated; bounded noncoverage
    is not negative biological evidence.
  target_ids:
  - GO:0000329
  evidence_ids:
  - micro-record-fungal_type_vacuole_membrane
  - micro-policy
  - micro-catalogue-api
  - micro-historical-runner
- assessment_id: micro-whole-stale-refresh
  area: provenance
  topic: Substantive current-input reassessment
  outcome: supported
  summary: Original whole review froze d447fe7b… and assessed five graph edges. Current1dc8607f…
    adds history plus two direct part_of edges. Both native GO children and OLS direct
    BFO0000050 graphs support lumen328/membrane329→whole324. All seven current edges
    and unchanged science were reassessed; original observation is preserved, not
    relabeled current.
  target_ids:
  - GO:0000324
  evidence_ids:
  - micro-stale-delta
  - micro-record-fungal_type_vacuole
  - micro-prior-fungal_type_vacuole
  - micro-go
  - micro-ols-0000324
  - micro-ols-0000328
  - micro-ols-0000329
- assessment_id: septin-glycosome-schema
  area: schema
  topic: Original validation/render and frozen-input staleness
  outcome: supported
  summary: Original native schema and deterministic rendering pass. The frozen historical
    target hash verifies; current whole glycosome changes are substantively reassessed
    below, while the other four targets are byte-unchanged. Native schema validity
    does not certify semantic scientific typing.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-original-validation-glycosome
- assessment_id: septin-glycosome-native-scope
  area: provenance
  topic: Actual represented inventory
  outcome: supported
  summary: 'Nine current protein examples: six glycolytic enzymes including reviewed
    P04789/TIM, plus three PEX proteins; six reviewed and three unreviewed entries.
    Both represented GENE_OR_PROTEIN nodes are COVERED. These checks establish declared
    identifier/symbol coverage, not exact cohort type, family grounding, source membership
    or necessity.'
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-native-glycosome-verify
  - septin-native-glycosome-causal
- assessment_id: septin-glycosome-nonasserted-surfaces
  area: scope
  topic: Images, physical properties, traits and snippets
  outcome: not_applicable
  summary: No maintained image asset, quantitative physical-property field, associated
    trait or verbatim snippet is declared. Source text/caption inspection does not
    constitute raw data or figure-pixel reanalysis.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
- assessment_id: septin-glycosome-history
  area: provenance
  topic: Status, immutable observations and scoped history
  outcome: supported
  summary: PROPOSED status and history remain unchanged. Original findings retain
    exact lineage; absent original findings are not invented. Closed grouped issue2462
    is historical context for the peroxin-type change only, not a current disposition
    of other records or the whole group.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-original-glycosome
- assessment_id: septin-glycosome_lumen-schema
  area: schema
  topic: Original validation/render and frozen-input staleness
  outcome: supported
  summary: Original native schema and deterministic rendering pass. The frozen historical
    target hash verifies; current whole glycosome changes are substantively reassessed
    below, while the other four targets are byte-unchanged. Native schema validity
    does not certify semantic scientific typing.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-original-validation-glycosome_lumen
- assessment_id: septin-glycosome_lumen-native-scope
  area: provenance
  topic: Actual represented inventory
  outcome: supported
  summary: No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-native-glycosome_lumen-verify
  - septin-native-glycosome_lumen-causal
- assessment_id: septin-glycosome_lumen-nonasserted-surfaces
  area: scope
  topic: Images, physical properties, traits and snippets
  outcome: not_applicable
  summary: No maintained image asset, quantitative physical-property field, associated
    trait or verbatim snippet is declared. Source text/caption inspection does not
    constitute raw data or figure-pixel reanalysis.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
- assessment_id: septin-glycosome_lumen-history
  area: provenance
  topic: Status, immutable observations and scoped history
  outcome: supported
  summary: PROPOSED status and history remain unchanged. Original findings retain
    exact lineage; absent original findings are not invented. Closed grouped issue2462
    is historical context for the peroxin-type change only, not a current disposition
    of other records or the whole group.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-original-glycosome_lumen
- assessment_id: septin-glycosome_membrane-schema
  area: schema
  topic: Original validation/render and frozen-input staleness
  outcome: supported
  summary: Original native schema and deterministic rendering pass. The frozen historical
    target hash verifies; current whole glycosome changes are substantively reassessed
    below, while the other four targets are byte-unchanged. Native schema validity
    does not certify semantic scientific typing.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-original-validation-glycosome_membrane
- assessment_id: septin-glycosome_membrane-native-scope
  area: provenance
  topic: Actual represented inventory
  outcome: supported
  summary: Zero protein examples, but one UNANCHORED_WITH_UNIPROT molecular node with
    verified PEX14 Q38CL4 xref. This is not an empty molecular inventory; it validates
    the represented identifier without establishing complete docking machinery or
    formation necessity.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-native-glycosome_membrane-verify
  - septin-native-glycosome_membrane-causal
- assessment_id: septin-glycosome_membrane-nonasserted-surfaces
  area: scope
  topic: Images, physical properties, traits and snippets
  outcome: not_applicable
  summary: No maintained image asset, quantitative physical-property field, associated
    trait or verbatim snippet is declared. Source text/caption inspection does not
    constitute raw data or figure-pixel reanalysis.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
- assessment_id: septin-glycosome_membrane-history
  area: provenance
  topic: Status, immutable observations and scoped history
  outcome: supported
  summary: PROPOSED status and history remain unchanged. Original findings retain
    exact lineage; absent original findings are not invented. Closed grouped issue2462
    is historical context for the peroxin-type change only, not a current disposition
    of other records or the whole group.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-original-glycosome_membrane
- assessment_id: septin-glyoxysomal_lumen-schema
  area: schema
  topic: Original validation/render and frozen-input staleness
  outcome: supported
  summary: Original native schema and deterministic rendering pass. The frozen historical
    target hash verifies; current whole glycosome changes are substantively reassessed
    below, while the other four targets are byte-unchanged. Native schema validity
    does not certify semantic scientific typing.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-original-validation-glyoxysomal_lumen
- assessment_id: septin-glyoxysomal_lumen-native-scope
  area: provenance
  topic: Actual represented inventory
  outcome: supported
  summary: No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-native-glyoxysomal_lumen-verify
  - septin-native-glyoxysomal_lumen-causal
- assessment_id: septin-glyoxysomal_lumen-nonasserted-surfaces
  area: scope
  topic: Images, physical properties, traits and snippets
  outcome: not_applicable
  summary: No maintained image asset, quantitative physical-property field, associated
    trait or verbatim snippet is declared. Source text/caption inspection does not
    constitute raw data or figure-pixel reanalysis.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
- assessment_id: septin-glyoxysomal_lumen-history
  area: provenance
  topic: Status, immutable observations and scoped history
  outcome: supported
  summary: PROPOSED status and history remain unchanged. Original findings retain
    exact lineage; absent original findings are not invented. Closed grouped issue2462
    is historical context for the peroxin-type change only, not a current disposition
    of other records or the whole group.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-original-glyoxysomal_lumen
- assessment_id: septin-glyoxysomal_membrane-schema
  area: schema
  topic: Original validation/render and frozen-input staleness
  outcome: supported
  summary: Original native schema and deterministic rendering pass. The frozen historical
    target hash verifies; current whole glycosome changes are substantively reassessed
    below, while the other four targets are byte-unchanged. Native schema validity
    does not certify semantic scientific typing.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-original-validation-glyoxysomal_membrane
- assessment_id: septin-glyoxysomal_membrane-native-scope
  area: provenance
  topic: Actual represented inventory
  outcome: supported
  summary: No protein examples, UniProtKB molecular graph xrefs or GENE_OR_PROTEIN
    nodes are represented. Exit zero validates this empty represented inventory only;
    pathway/import claims require separate scientific source assessment.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-native-glyoxysomal_membrane-verify
  - septin-native-glyoxysomal_membrane-causal
- assessment_id: septin-glyoxysomal_membrane-nonasserted-surfaces
  area: scope
  topic: Images, physical properties, traits and snippets
  outcome: not_applicable
  summary: No maintained image asset, quantitative physical-property field, associated
    trait or verbatim snippet is declared. Source text/caption inspection does not
    constitute raw data or figure-pixel reanalysis.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
- assessment_id: septin-glyoxysomal_membrane-history
  area: provenance
  topic: Status, immutable observations and scoped history
  outcome: supported
  summary: PROPOSED status and history remain unchanged. Original findings retain
    exact lineage; absent original findings are not invented. Closed grouped issue2462
    is historical context for the peroxin-type change only, not a current disposition
    of other records or the whole group.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-original-glyoxysomal_membrane
- assessment_id: septin-glycosome-adapter
  area: scope
  topic: Claim-sensitive pathway applicability and exact-host coverage
  outcome: not_applicable
  summary: The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import
    pathways. An expression-only exemption is insufficient even when the graph is
    descriptive. Fresh complete official catalogue lacks matching actual hosts, so
    downstream module queries are not applicable; no negative biology or engineered-host
    substitution is inferred.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-original-glycosome
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-glycosome_lumen-adapter
  area: scope
  topic: Claim-sensitive pathway applicability and exact-host coverage
  outcome: not_applicable
  summary: The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import
    pathways. An expression-only exemption is insufficient even when the graph is
    descriptive. Fresh complete official catalogue lacks matching actual hosts, so
    downstream module queries are not applicable; no negative biology or engineered-host
    substitution is inferred.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-original-glycosome_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-glycosome_membrane-adapter
  area: scope
  topic: Claim-sensitive pathway applicability and exact-host coverage
  outcome: not_applicable
  summary: The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import
    pathways. An expression-only exemption is insufficient even when the graph is
    descriptive. Fresh complete official catalogue lacks matching actual hosts, so
    downstream module queries are not applicable; no negative biology or engineered-host
    substitution is inferred.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-original-glycosome_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-glyoxysomal_lumen-adapter
  area: scope
  topic: Claim-sensitive pathway applicability and exact-host coverage
  outcome: not_applicable
  summary: The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import
    pathways. An expression-only exemption is insufficient even when the graph is
    descriptive. Fresh complete official catalogue lacks matching actual hosts, so
    downstream module queries are not applicable; no negative biology or engineered-host
    substitution is inferred.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-original-glyoxysomal_lumen
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-glyoxysomal_membrane-adapter
  area: scope
  topic: Claim-sensitive pathway applicability and exact-host coverage
  outcome: not_applicable
  summary: The complete record positively asserts glycolytic/PEX or glyoxylate-cycle/import
    pathways. An expression-only exemption is insufficient even when the graph is
    descriptive. Fresh complete official catalogue lacks matching actual hosts, so
    downstream module queries are not applicable; no negative biology or engineered-host
    substitution is inferred.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-original-glyoxysomal_membrane
  - septin-review-policy
  - septin-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-glycosome-identity
  area: identity
  topic: Exact glycosome structure and compartment boundaries
  outcome: supported
  summary: Native GO/UniProt verify whole organelle, surrounding membrane and enclosed
    matrix separately. Glycosome is_a peroxisome; membrane is_a peroxisomal membrane;
    lumen has broad organelle-lumen is_a ancestry. Exact direct mappings are separated
    from nested parent identities.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-go
  - septin-ancestors-0020015
  - septin-ancestors-0034468
  - septin-SL-0128
  - septin-SL-0129
  - septin-SL-0332
- assessment_id: septin-glycosome-taxon
  area: scope
  topic: Kinetoplastid scope and experimental versus reference strains
  outcome: supported
  summary: Kinetoplastea5653 is a class with Kinetoplastida synonym, so legacy GO
    order wording is not a different taxon. Review synthesis supports examined kinetoplastids
    and variable enzyme content across taxa/stages. T.brucei experiments in29–13/PF449
    and bloodstream contexts are not relabeled TREU927 because exemplar accessions
    use that strain. COMMON does not assert an experiment measured population prevalence.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-tax5653
  - septin-tax5691
  - septin-tax5702
  - septin-tax31285
  - septin-tax185431
  - septin-haanstra2016-meta
  - septin-haanstra2008-pmc
  - septin-furuya2002-pmc
- assessment_id: septin-glycosome-necessity
  area: grounding
  topic: Import or survival requirement versus organelle formation
  outcome: unknown
  summary: Constitutive bilayer is distinguished from individual lipid/protein formation
    requirements. Import defects, growth loss and metabolic toxicity do not alone
    prove failed organelle assembly; Galland reports apparently intact procyclic glycosomes
    after receptor depletion. Protein UNKNOWN essentiality remains appropriate.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-curation-policy
  - septin-PMID17320990
  - septin-PMID12709066
  - septin-furuya2002-pmc
  - septin-haanstra2008-pmc
- assessment_id: septin-glycosome_lumen-identity
  area: identity
  topic: Exact glycosome structure and compartment boundaries
  outcome: supported
  summary: Native GO/UniProt verify whole organelle, surrounding membrane and enclosed
    matrix separately. Glycosome is_a peroxisome; membrane is_a peroxisomal membrane;
    lumen has broad organelle-lumen is_a ancestry. Exact direct mappings are separated
    from nested parent identities.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-go
  - septin-ancestors-0020015
  - septin-ancestors-0034468
  - septin-SL-0128
  - septin-SL-0129
  - septin-SL-0332
- assessment_id: septin-glycosome_lumen-taxon
  area: scope
  topic: Kinetoplastid scope and experimental versus reference strains
  outcome: supported
  summary: Kinetoplastea5653 is a class with Kinetoplastida synonym, so legacy GO
    order wording is not a different taxon. Review synthesis supports examined kinetoplastids
    and variable enzyme content across taxa/stages. T.brucei experiments in29–13/PF449
    and bloodstream contexts are not relabeled TREU927 because exemplar accessions
    use that strain. COMMON does not assert an experiment measured population prevalence.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-tax5653
  - septin-tax5691
  - septin-tax5702
  - septin-tax31285
  - septin-tax185431
  - septin-haanstra2016-meta
  - septin-haanstra2008-pmc
  - septin-furuya2002-pmc
- assessment_id: septin-glycosome_lumen-necessity
  area: grounding
  topic: Import or survival requirement versus organelle formation
  outcome: unknown
  summary: Constitutive bilayer is distinguished from individual lipid/protein formation
    requirements. Import defects, growth loss and metabolic toxicity do not alone
    prove failed organelle assembly; Galland reports apparently intact procyclic glycosomes
    after receptor depletion. Protein UNKNOWN essentiality remains appropriate.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-curation-policy
  - septin-PMID17320990
  - septin-PMID12709066
  - septin-furuya2002-pmc
  - septin-haanstra2008-pmc
- assessment_id: septin-glycosome_membrane-identity
  area: identity
  topic: Exact glycosome structure and compartment boundaries
  outcome: supported
  summary: Native GO/UniProt verify whole organelle, surrounding membrane and enclosed
    matrix separately. Glycosome is_a peroxisome; membrane is_a peroxisomal membrane;
    lumen has broad organelle-lumen is_a ancestry. Exact direct mappings are separated
    from nested parent identities.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-go
  - septin-ancestors-0020015
  - septin-ancestors-0034468
  - septin-SL-0128
  - septin-SL-0129
  - septin-SL-0332
- assessment_id: septin-glycosome_membrane-taxon
  area: scope
  topic: Kinetoplastid scope and experimental versus reference strains
  outcome: supported
  summary: Kinetoplastea5653 is a class with Kinetoplastida synonym, so legacy GO
    order wording is not a different taxon. Review synthesis supports examined kinetoplastids
    and variable enzyme content across taxa/stages. T.brucei experiments in29–13/PF449
    and bloodstream contexts are not relabeled TREU927 because exemplar accessions
    use that strain. COMMON does not assert an experiment measured population prevalence.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-tax5653
  - septin-tax5691
  - septin-tax5702
  - septin-tax31285
  - septin-tax185431
  - septin-haanstra2016-meta
  - septin-haanstra2008-pmc
  - septin-furuya2002-pmc
- assessment_id: septin-glycosome_membrane-necessity
  area: grounding
  topic: Import or survival requirement versus organelle formation
  outcome: unknown
  summary: Constitutive bilayer is distinguished from individual lipid/protein formation
    requirements. Import defects, growth loss and metabolic toxicity do not alone
    prove failed organelle assembly; Galland reports apparently intact procyclic glycosomes
    after receptor depletion. Protein UNKNOWN essentiality remains appropriate.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-curation-policy
  - septin-PMID17320990
  - septin-PMID12709066
  - septin-furuya2002-pmc
  - septin-haanstra2008-pmc
- assessment_id: septin-glycosome-stale-TIM
  area: grounding
  topic: Substantive refresh of added TIM example
  outcome: supported
  summary: Current reviewed P04789 is glycosomal triosephosphate isomerase in taxon5702
    and has protein short name TIM, with no indexed geneName. Literal gene_exact query
    returns zero while the reviewed protein-name query returns only P04789. Misset
    abstract and Haanstra TIM activity fractionation support glycosomal enzyme context
    independently of accession identity. Native represented coverage is now complete;
    this is not a new proof of an indexed gene symbol.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-stale-glycosome-diff
  - septin-protein-P04789
  - septin-reviewed-TIM
  - septin-reviewed-TIM-protein-alias
  - septin-PMID2940090
  - septin-haanstra2008-pmc
  - septin-native-glycosome-causal
- assessment_id: septin-glycosome-stale-peroxin-type
  area: schema
  topic: Substantive refresh of import-apparatus retyping
  outcome: supported
  summary: The current PROTEIN_COMPLEX type describes multi-protein import apparatus
    rather than one family. Primary PEX5/PEX7 interaction and PEX13/PEX14 docking
    evidence supports the apparatus context, without asserting all listed proteins
    form one permanent stoichiometric unit. Closed2462 is historical only; this review
    neither reopens that correction nor resolves other grouped targets.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-stale-glycosome-diff
  - septin-schema-policy
  - septin-PMID12709066
  - septin-PMID17320990
  - septin-PMID22809509
  - septin-historical-2462
- assessment_id: septin-glycosome-protein-identities
  area: grounding
  topic: Nine exact exemplar identities and source placement
  outcome: supported
  summary: All nine accession/status/taxon pairs agree; six are reviewed and three
    unreviewed. GAPDH O96429 is an unreviewed fragment. PEX5/PEX7 cytosolic/cycling
    annotations and PEX14 membrane localization remain distinct; PEX14-specific edge
    description does not make every receptor permanently membrane resident. Identity/automatic
    family annotations are not direct localization experiments for every modern accession.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-protein-P13377
  - septin-protein-O15648
  - septin-protein-A0A3G1VTN5
  - septin-protein-O96429
  - septin-protein-Q4GZG4
  - septin-protein-P04789
  - septin-protein-Q57W55
  - septin-protein-Q57W97
  - septin-protein-Q38CL4
  - septin-PMID2940090
  - septin-PMID10589985
  - septin-PMID17320990
  - septin-PMID23994617
  - septin-PMID22809509
- assessment_id: septin-glycosome-enzyme-cohort-type
  area: schema
  topic: Explicit heterogeneous enzyme class under native modeling guidance
  outcome: supported
  summary: The glycolytic_enzymes row transparently declares unrelated families grouped
    by pathway and localization, with UNKNOWN formation necessity. Although the enum
    prose is narrower, CURATION explicitly permits a taxon-agnostic family or class
    and the UniProt skill recognizes generic class components. This policy tension
    does not establish a confirmed record defect. Retaining this qualified class does
    not assert one homologous family or a stable protein complex; no automatic PROTEIN_COMPLEX
    conversion is justified.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-schema-policy
  - septin-curation-policy
  - septin-protein-policy
  - septin-protein-P13377
  - septin-protein-O15648
  - septin-protein-P04789
  - septin-protein-O96429
  - septin-protein-Q4GZG4
  - septin-protein-A0A3G1VTN5
  - septin-PMID2940090
- assessment_id: septin-glycosome-family-scope
  area: grounding
  topic: Peroxin and enzyme family scope
  outcome: supported
  summary: Individual PEX families are distinct and do not each identify the entire
    import apparatus. No single family denotes the heterogeneous glycolytic set, which
    is explicitly labeled as a class. Native family-or-class and generic-class guidance
    supports retaining that qualification; no confirmed component-type defect, forced
    split, invented broad family or automatic complex classification follows from
    the narrower enum prose alone.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-IPR024111
  - septin-IPR044536
  - septin-IPR025655
  - septin-schema-policy
  - septin-curation-policy
  - septin-protein-policy
- assessment_id: septin-glycosome-membrane-grounding
  area: grounding
  topic: Whole membrane encoded as molecular lipid identity
  outcome: concern
  summary: 'Inherited F3 persists: component glycosome_membrane is LIPID grounded
    to assembled membrane GO0046860, with graph component_ref. The correct substructure
    is already represented by has_part and its STRUCTURE node. Preserve that topology
    while correcting the molecular/material representation; no exact lipid composition
    is established here.'
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-go
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-glycosome-glucose-mechanism
  area: evidence
  topic: Glucose phenotype and qualified mechanistic inference
  outcome: concern
  summary: Inherited F2 persists in function description/evidence and final graph
    edge. Haanstra2008 measured Glc6P accumulation in29–13 after glucose but explicitly
    could not exclude PGI-pathway truncation; PF449 lacked significant Glc6P accumulation.
    Glycerol/Gly3P plus GK-rescue supplies the stronger mechanism test. Preserve the
    observed phenotype and general compartmentation function while qualifying the
    glucose-specific causal claim.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-haanstra2008-meta
  - septin-haanstra2008-pmc
  - septin-haanstra2016-meta
- assessment_id: septin-glycosome-graph
  area: graph
  topic: Supported import/localization sequence with bounded endpoint
  outcome: concern
  summary: PEX14 membrane docking/import and enzyme matrix localization are supported
    at the read primary tiers. Receptor cycling remains distinct from permanent membrane
    residency; the membrane component grounding and glucose-specific causal endpoint
    require the stated corrections. Model membrane removal is not a directly performed
    cellular membrane-deletion experiment.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-PMID12709066
  - septin-PMID10589985
  - septin-PMID17320990
  - septin-PMID22809509
  - septin-furuya2002-pmc
  - septin-haanstra2008-pmc
  - septin-PMID2940090
  - septin-go
  - septin-schema-policy
- assessment_id: septin-glycosome-attribution
  area: evidence
  topic: Repeated PEX14 first-author attribution
  outcome: concern
  summary: The repeatedly cited DOI belongs to Moyersoen et al.2003, with Choe second.
    Correct the repeated Choe et al. notes while retaining the exact DOI/title and
    supported import/localization biology. The inherited stable key and predecessor
    for this maintained record are preserved.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-PMID12709066
- assessment_id: septin-glycosome_membrane-attribution
  area: evidence
  topic: Repeated PEX14 first-author attribution
  outcome: concern
  summary: The repeatedly cited DOI belongs to Moyersoen et al.2003, with Choe second.
    Correct the repeated Choe et al. notes while retaining the exact DOI/title and
    supported import/localization biology. The inherited stable key and predecessor
    for this maintained record are preserved.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-PMID12709066
- assessment_id: septin-glycosome_lumen-function-graph
  area: graph
  topic: General compartmentation and two descriptive boundaries
  outcome: supported
  summary: The lumen houses major glycolytic enzymes and provides a compartment for
    flux control. The general statement does not claim Haanstra uniquely resolves
    the glucose-specific mechanism. Lumen parthood and membrane enclosure are NONMECHANISTIC,
    and the membrane is not inserted as lumen material.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-go
  - septin-SL-0332
  - septin-PMID2940090
  - septin-haanstra2008-pmc
  - septin-graph-policy
- assessment_id: septin-glycosome_membrane-material
  area: grounding
  topic: Collective bilayer versus exact lipid chemistry
  outcome: supported
  summary: The label-only lipid constituent denotes collective bilayer material; no
    whole-membrane GO term is asserted as its exact molecular grounding. The structural
    graph node refers to its constituting material without claiming an exact lipid
    species or complete mixture.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-go
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-glycosome_membrane-function-graph
  area: graph
  topic: Four descriptive membrane/import-placement edges
  outcome: supported
  summary: Native definitions support membrane parthood/enclosure. Complete Moyersoen
    abstract and Furuya body support PEX14 membrane docking and import, with Q38CL4
    identity independently current. NONMECHANISTIC scope does not pretend to model
    the entire receptor cycle; biological relations remain supported despite the attribution
    correction.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-go
  - septin-PMID12709066
  - septin-furuya2002-pmc
  - septin-protein-Q38CL4
  - septin-graph-policy
- assessment_id: septin-glyoxysomal_lumen-identity
  area: identity
  topic: Glyoxysomal exact identity and relation typing
  outcome: supported
  summary: GO/UniProt distinguish matrix volume, bounding membrane and whole glyoxysome.
    Broad lumen parent GO0043233 is an is_a ancestor; membrane parent is peroxisomal
    membrane. Exact synonyms/direct mappings and parthood are verified without treating
    nested mappings as identity. The frozen whole neighbor supplies boundary context
    only.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-go
  - septin-ancestors-0031908
  - septin-SL-0130
  - septin-SL-0131
  - septin-SL-0333
  - septin-glyoxysome-neighbor
- assessment_id: septin-glyoxysomal_lumen-taxon-primary
  area: scope
  topic: Actual fungal acetate-induced targeting assay
  outcome: supported
  summary: Current complete de Zoysa/Connerton primary abstract directly supports
    acetate-induced N.crassa glyoxysomes and C-terminally modified CAT reporter import.
    This supplies fungal occurrence independently of plant-oriented GO/UniProt descriptions.
    Native identity is5141; reporter efficacy is condition/sequence dependent and
    not a universal route for every matrix protein. Current source access is abstract
    only, so detailed strains, medium values, original plots or endogenous-enzyme
    exceptions from the old full-body review are not freshly certified.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-tax5141
  - septin-dezoysa1994-meta
  - septin-SL-0131
  - septin-dezoysa1994-pdf
  - septin-dezoysa1994-encoded-pdf
- assessment_id: septin-glyoxysomal_lumen-necessity
  area: grounding
  topic: Unestablished molecular assembly requirements
  outcome: unknown
  summary: The enclosing bilayer defines the membrane compartment; individual lipid-removal/substitution
    or protein necessities for organelle formation are not established. Reporter targeting
    and pathway activity do not establish these requirements. No complete chemical
    or protein inventory is inferred.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-go
  - septin-dezoysa1994-meta
  - septin-curation-policy
- assessment_id: septin-glyoxysomal_membrane-identity
  area: identity
  topic: Glyoxysomal exact identity and relation typing
  outcome: supported
  summary: GO/UniProt distinguish matrix volume, bounding membrane and whole glyoxysome.
    Broad lumen parent GO0043233 is an is_a ancestor; membrane parent is peroxisomal
    membrane. Exact synonyms/direct mappings and parthood are verified without treating
    nested mappings as identity. The frozen whole neighbor supplies boundary context
    only.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-go
  - septin-ancestors-0031908
  - septin-SL-0130
  - septin-SL-0131
  - septin-SL-0333
  - septin-glyoxysome-neighbor
- assessment_id: septin-glyoxysomal_membrane-taxon-primary
  area: scope
  topic: Actual fungal acetate-induced targeting assay
  outcome: supported
  summary: Current complete de Zoysa/Connerton primary abstract directly supports
    acetate-induced N.crassa glyoxysomes and C-terminally modified CAT reporter import.
    This supplies fungal occurrence independently of plant-oriented GO/UniProt descriptions.
    Native identity is5141; reporter efficacy is condition/sequence dependent and
    not a universal route for every matrix protein. Current source access is abstract
    only, so detailed strains, medium values, original plots or endogenous-enzyme
    exceptions from the old full-body review are not freshly certified.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-tax5141
  - septin-dezoysa1994-meta
  - septin-SL-0131
  - septin-dezoysa1994-pdf
  - septin-dezoysa1994-encoded-pdf
- assessment_id: septin-glyoxysomal_membrane-necessity
  area: grounding
  topic: Unestablished molecular assembly requirements
  outcome: unknown
  summary: The enclosing bilayer defines the membrane compartment; individual lipid-removal/substitution
    or protein necessities for organelle formation are not established. Reporter targeting
    and pathway activity do not establish these requirements. No complete chemical
    or protein inventory is inferred.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-go
  - septin-dezoysa1994-meta
  - septin-curation-policy
- assessment_id: septin-glyoxysomal_lumen-function-graph
  area: graph
  topic: Matrix pathway context and three descriptive edges
  outcome: supported
  summary: The function and cycle edge description assert that glyoxylate-pathway
    enzymes are contained in the matrix, not that every reaction is exclusively luminal
    or every endogenous enzyme uses one C-terminal signal. GO and the primary abstract
    support this compartment context; parthood/enclosure edges are descriptive. Empty
    optional components are compatible with enclosed-volume identity.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-go
  - septin-SL-0333
  - septin-dezoysa1994-meta
  - septin-graph-policy
- assessment_id: septin-glyoxysomal_membrane-material-function-graph
  area: graph
  topic: Collective membrane material and boundary topology
  outcome: supported
  summary: Reviewed-label-only bilayer, organelle parthood and enclosure of matrix
    follow exact membrane/lumen definitions. The canonical import example is bounded
    to the primary reporter assay; no transport pore mechanism, direct translocation
    movie, individual membrane factor or chemical lipid inventory is asserted.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-go
  - septin-SL-0130
  - septin-SL-0333
  - septin-dezoysa1994-meta
  - septin-curation-policy
  - septin-graph-policy
- assessment_id: septin-glycosome-verdict
  area: evidence
  topic: Current independent scientific verdict
  outcome: concern
  summary: Whole glycosome retains three inherited findings; membrane retains its
    own inherited first-author finding. The proposed heterogeneous-class typing concern
    was not confirmed after checking both native class policies; it is not a finding
    or curation action. Exact stable keys and predecessors remain scoped to their
    records. Bundle applicability repairs are separate. No neighbor/group/historical
    issue is terminally disposed of by this review.
  target_ids:
  - GO:0020015
  evidence_ids:
  - septin-record-glycosome
  - septin-go
  - septin-review-policy
  - septin-PMID12709066
  - septin-haanstra2008-pmc
  - septin-schema-policy
- assessment_id: septin-glycosome_lumen-verdict
  area: evidence
  topic: Current independent scientific verdict
  outcome: supported
  summary: No concrete scientific correction established for this complete assigned
    compartment/membrane target; retain source-tier, pathway, assay and empty-inventory
    limitations. Bundle applicability repairs are separate. No neighbor/group/historical
    issue is terminally disposed of by this review.
  target_ids:
  - GO:0034468
  evidence_ids:
  - septin-record-glycosome_lumen
  - septin-go
  - septin-review-policy
  - septin-haanstra2008-pmc
- assessment_id: septin-glycosome_membrane-verdict
  area: evidence
  topic: Current independent scientific verdict
  outcome: concern
  summary: Whole glycosome retains three inherited findings; membrane retains its
    own inherited first-author finding. The proposed heterogeneous-class typing concern
    was not confirmed after checking both native class policies; it is not a finding
    or curation action. Exact stable keys and predecessors remain scoped to their
    records. Bundle applicability repairs are separate. No neighbor/group/historical
    issue is terminally disposed of by this review.
  target_ids:
  - GO:0046860
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-go
  - septin-review-policy
  - septin-PMID12709066
  - septin-haanstra2008-pmc
  - septin-schema-policy
- assessment_id: septin-glyoxysomal_lumen-verdict
  area: evidence
  topic: Current independent scientific verdict
  outcome: supported
  summary: No concrete scientific correction established for this complete assigned
    compartment/membrane target; retain source-tier, pathway, assay and empty-inventory
    limitations. Bundle applicability repairs are separate. No neighbor/group/historical
    issue is terminally disposed of by this review.
  target_ids:
  - GO:0031908
  evidence_ids:
  - septin-record-glyoxysomal_lumen
  - septin-go
  - septin-review-policy
  - septin-dezoysa1994-meta
- assessment_id: septin-glyoxysomal_membrane-verdict
  area: evidence
  topic: Current independent scientific verdict
  outcome: supported
  summary: No concrete scientific correction established for this complete assigned
    compartment/membrane target; retain source-tier, pathway, assay and empty-inventory
    limitations. Bundle applicability repairs are separate. No neighbor/group/historical
    issue is terminally disposed of by this review.
  target_ids:
  - GO:0046861
  evidence_ids:
  - septin-record-glyoxysomal_membrane
  - septin-go
  - septin-review-policy
  - septin-dezoysa1994-meta
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 3 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0020016
  - GO:0020020
  - GO:0000324
  - GO:0000328
  - GO:0000329
  - GO:0020015
  - GO:0034468
  - GO:0046860
  - GO:0031908
  - GO:0046861
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
- finding_id: plaque-t0-F1
  issue_key: flagellar-pocket-lipid-whole-membrane-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the complete pocket membrane from its molecular lipid constituent
  description: The ciliary_pocket_membrane row has component_type LIPID but grounding
    GO:0020018, whose native identity is the complete ciliary pocket membrane. Schema
    StructuralComponent requires a molecular building block and distinguishes chemical
    lipid grounding from GO sub-complex grounding. The graph component_ref repeats
    the same invalid molecular correspondence. Correct membrane topology and membrane/collar
    membership do not resolve this field-level identity mismatch.
  target_ids:
  - GO:0020016
  field_paths:
  - components#ciliary_pocket_membrane.component_type
  - components#ciliary_pocket_membrane.grounding
  - causal_graphs#pocket_boundary_and_traffic.nodes#ciliary_pocket_membrane.component_ref
  evidence_ids:
  - plaque-current-0
  - plaque-schema-policy
  - plaque-go
  - plaque-pmc-PMC2755463
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/flagellar_pocket.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity and source scope
  native_severity: major
  normalization_reason: Major because an asserted molecular component is grounded
    to a distinct complete structure and that correspondence propagates into the graph;
    the organelle identity and descriptive boundary are intact and are not the basis
    for a higher severity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T014651Z-flagellar-pocket-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2697
- finding_id: septin-glycosome-F1
  issue_key: glycosome-pex14-first-author-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the PEX14 paper’s first-author attribution
  description: DOI10.1046/j.1432-1033.2003.03582.x is Moyersoen et al.2003, with Choe
    second. Several source notes call it Choe et al.2003. The DOI/title and relevant
    import biology are correct; the first-author attribution is not.
  target_ids:
  - GO:0020015
  field_paths:
  - components#peroxin_import_machinery.evidence
  - functions#glycosomal_matrix_protein_import.evidence
  - evidence
  - causal_graphs#pex14_glycolytic_import_compartmentation.edges
  evidence_ids:
  - septin-record-glycosome
  - septin-PMID12709066
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level support and severity
    rubric
  native_severity: minor
  normalization_reason: Minor bibliographic provenance defect; source identity and
    the supported PEX14 mechanism are not invalidated.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T014658Z-glycosome-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2698
- finding_id: septin-glycosome-F2
  issue_key: glycosome-glucose-mechanism-evidence-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Retain the paper’s glucose-mechanism qualification
  description: 'The function evidence says Haanstra2008 showed compartmentation prevents
    toxic Glc6P accumulation, and the final graph edge states that causal endpoint
    without the paper’s qualification. Its Results and Discussion explicitly say the
    glucose experiment is not a stringent test: PGI truncation is an alternative,
    PF449 lacked significant Glc6P accumulation, and glycerol/GK rescue provides the
    stronger mechanistic test. The observed29–13 glucose phenotype is valid but does
    not uniquely resolve that mechanism.'
  target_ids:
  - GO:0020015
  field_paths:
  - functions#glycolytic_compartmentation.description
  - functions#glycolytic_compartmentation.evidence
  - causal_graphs#pex14_glycolytic_import_compartmentation.edges
  evidence_ids:
  - septin-record-glycosome
  - septin-haanstra2008-meta
  - septin-haanstra2008-pmc
  - septin-haanstra2016-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level support and severity
    rubric
  native_severity: minor
  normalization_reason: 'Minor source-specific wording overstatement: the general
    compartmentation function and measured Glc6P phenotype are supported; the correction
    preserves the study’s explicit limits instead of declaring that biology false.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T014658Z-glycosome-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2699
- finding_id: septin-glycosome-F3
  issue_key: glycosome-membrane-molecular-component-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate the membrane substructure from molecular lipid composition
  description: The glycosome_membrane component names the complete membrane, declares
    type LIPID, and grounds it to GO0046860, which identifies the assembled bilayer
    surrounding a glycosome. The frozen schema defines StructuralComponent as a molecular
    building block, with lipid grounding to chemical classes. The graph itself correctly
    types this object as STRUCTURE but attaches the molecular component_ref. Correct
    has_part and boundary topology already represent the membrane; they do not make
    the whole structure a lipid identity.
  target_ids:
  - GO:0020015
  field_paths:
  - components#glycosome_membrane
  - causal_graphs#pex14_glycolytic_import_compartmentation.nodes#glycosome_membrane.component_ref
  evidence_ids:
  - septin-record-glycosome
  - septin-schema-policy
  - septin-curation-policy
  - septin-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level support and severity
    rubric
  native_severity: major
  normalization_reason: 'Major incorrect molecular-component grounding: the encoded
    object is an assembled substructure rather than the claimed lipid building-block
    identity. The whole organelle identity and membrane topology remain supported.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T014658Z-glycosome-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2700
- finding_id: septin-glycosome_membrane-F1
  issue_key: glycosome_membrane-pex14-first-author-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the PEX14 paper’s first-author attribution
  description: DOI10.1046/j.1432-1033.2003.03582.x is Moyersoen et al.2003, with Choe
    second. Several source notes call it Choe et al.2003. The DOI/title and relevant
    import biology are correct; the first-author attribution is not.
  target_ids:
  - GO:0046860
  field_paths:
  - functions#glycosomal_matrix_import_boundary.evidence
  - evidence
  - causal_graphs#glycosome_membrane_import_boundary.edges
  evidence_ids:
  - septin-record-glycosome_membrane
  - septin-PMID12709066
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level support and severity
    rubric
  native_severity: minor
  normalization_reason: Minor bibliographic provenance defect; source identity and
    the supported PEX14 mechanism are not invalidated.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T014700Z-glycosome-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2701
actions:
- action_id: plaque-t0-A1
  finding_ids:
  - plaque-t0-F1
  target_ids:
  - GO:0020016
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/flagellar_pocket.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, retain the complete membrane
    as structural topology and represent only a source-supported molecular lipid material
    in components, using exact chemical grounding where justified or an explicitly
    reviewed label-only material. Correct/remove the graph component_ref so it does
    not equate the whole membrane with that molecular entry.
  acceptance_checks:
  - Confirm that every LIPID grounding identifies lipid material, not GO0020018 as
    the whole membrane; do not invent an exact lipid mixture or assign an arbitrary
    CHEBI term.
  - Preserve the correctly grounded membrane STRUCTURE node and descriptive edges,
    the pocket identity, and the GO-grounded protein-complex collar.
  - Run focused schema, grounding/product and graph checks after separately authorized
    scientific curation.
- action_id: septin-glycosome-A1
  finding_ids:
  - septin-glycosome-F1
  target_ids:
  - GO:0020015
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, change the repeated author attribution
    to Moyersoen et al.2003 while retaining the verified DOI and supported claim scopes.
  acceptance_checks:
  - Preserve supported structure, protein identities and source-specific experimental
    boundaries.
  - Run focused schema, strict and relevant native graph checks after separately authorized
    curation.
- action_id: septin-glycosome-A2
  finding_ids:
  - septin-glycosome-F2
  target_ids:
  - GO:0020015
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, distinguish the observed glucose-addition
    phenotype and competing PGI explanation from the stronger glycerol proof; qualify
    the glucose-specific causal wording and source note while preserving supported
    import and pathway compartmentation.
  acceptance_checks:
  - Preserve supported structure, protein identities and source-specific experimental
    boundaries.
  - Run focused schema, strict and relevant native graph checks after separately authorized
    curation.
- action_id: septin-glycosome-A3
  finding_ids:
  - septin-glycosome-F3
  target_ids:
  - GO:0020015
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome.yaml
    role: maintained scientific record
  description: In separately authorized curation, retain GO0046860 in has_part and
    as the grounded membrane graph node; remove its molecular component_ref if removing
    the whole-membrane component, or replace that component only with an independently
    supported molecular/material lipid description and appropriate grounding. Do not
    invent a lipid composition.
  acceptance_checks:
  - Preserve supported structure, protein identities and source-specific experimental
    boundaries.
  - Run focused schema, strict and relevant native graph checks after separately authorized
    curation.
- action_id: septin-glycosome_membrane-A1
  finding_ids:
  - septin-glycosome_membrane-F1
  target_ids:
  - GO:0046860
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/glycosome_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, change the repeated author attribution
    to Moyersoen et al.2003 while retaining the verified DOI and supported claim scopes.
  acceptance_checks:
  - Preserve supported structure, protein identities and source-specific experimental
    boundaries.
  - Run focused schema, strict and relevant native graph checks after separately authorized
    curation.
limitations:
- 'Flagellar pocket and food vacuole independent subreview: Assigned flagellar pocket
  and food vacuole only. One inherited major F1 remains open with exact original key/severity/repository-review-finding
  lineage. Food-vacuole stale membrane-node/bounds-edge delta is substantively refreshed;
  no scientific record correction or terminal neighbor/group/category disposition
  is claimed.'
- 'Flagellar pocket and food vacuole independent subreview: Fresh Lacomble primary
  body scope: Resultssec3/4, Methodssec10, selected Introduction/Discussion paragraphs
  citing Bonhivers/BILBO1. Gadelha: Resultssec2/3/5/6 and Methodssec12. Bonhivers
  publisher XML:s2a/s2b/s2c/s3a/s3d/s4a/s4e/s4i. Captions read as text, no primary
  figure pixels, raw tomograms, movies or supplements inspected. Unlisted sections
  not certified.'
- 'Flagellar pocket and food vacuole independent subreview: Lacomble procyclic427,
  Gadelha bloodstream forms and Bonhivers distinct genomic/procyclic/bloodstream lines
  remain separate contexts. New-pocket RNAi necessity is not universal collar-constituent
  necessity or total loss of old pockets; cell-cycle duplication is retained.'
- 'Flagellar pocket and food vacuole independent subreview: Field2009/Halliday2021
  are secondary review abstracts only. Cowman1991/Lamarque2008 are complete primary
  abstracts only. Lamarque MED PMID21136929 selected from two DOI results; FV enrichment
  does not imply pure/exhaustive/necessary inventory. No uninspected full-body or
  pixel claim for these sources.'
- 'Flagellar pocket and food vacuole independent subreview: Wiser2024 is secondary
  review body, sections3.2/Table2 and4/4.1/4.2/4.3/Fig2caption. Boundary topology
  and broad digestion/hemozoin functions are supported; precise transporter direction,
  lipid composition and hemozoin molecular mechanism are not freshly demonstrated
  by this review.'
- 'Flagellar pocket and food vacuole independent subreview: Both targets lack accession
  protein_examples and typed GENE_OR_PROTEIN nodes; four actual native commands pass
  within that empty-inventory scope. Positive BILBO1/trafficking and hemoglobin/heme/transporter
  narratives still trigger source applicability.'
- 'Flagellar pocket and food vacuole independent subreview: Fresh official catalogue
  has no matching T. brucei or P. falciparum host; no matched downstream gene/module
  query or unrelated-host proxy applies. Noncoverage is not negative biological evidence.
  Historical runner failure remains actual00:49Z unavailable, not a current invocation
  or success.'
- 'Flagellar pocket and food vacuole independent subreview: Two frozen neighbors were
  read only for membrane/material/collar identity and boundary context. Their other
  protein accessions/claims are not certified or terminally resolved. Root owns global
  QC, issues and publication; no repository/GitHub/record writes by this reviewer.'
- 'Fungal-type vacuole, lumen and membrane independent subreview: Fungal-vacuole slice:
  three full records and original pairs independently reviewed, one stale whole target
  substantively refreshed. No scientific curation finding or predecessor disposition;
  original three findings/actions lists are empty. Three original expression-only
  adapter exclusions are concrete bundle defects, not missing optional scientific
  fields.'
- 'Fungal-type vacuole, lumen and membrane independent subreview: Source tier: Li/Kane2009
  is secondary review, complete sections2.1/4.2/5.1/6.1/6.2 and included captions
  read. Kane2006 is secondary review, complete Introduction/structure/a-isoform targeting
  sections and caption read. Historical subunit counts are not certified as current
  composition; underlying primary experiments are not all reanalyzed.'
- 'Fungal-type vacuole, lumen and membrane independent subreview: Primary tier: Huh2003
  and Matsumoto2013 complete abstracts/bibliography only; exact P00729 ECO citation
  attribution is independently checked in native UniProt. Parzych2018 Resultssec3/4,
  Discussionsec7, Methodssec9/11 including Tables1/2 and embedded captions read. No
  fresh figure pixels, movies or supplementary dataset inspection; no target image
  asset exists. SEY6210 experimental derivatives are not equated with reference S288C.'
- 'Fungal-type vacuole, lumen and membrane independent subreview: Biological limits:
  COMMON is qualitative, not prevalence. Soluble protease localization differs from
  transient degradative cargo; partial functional redundancy precludes individual
  assembly necessity. Lumen actors are not forced into component material, and lipid
  boundary essentiality is not every lipid-species necessity.'
- 'Fungal-type vacuole, lumen and membrane independent subreview: Structured-source
  limits: all three records trigger applicability by their actual protein/pathway
  assertions. Fresh official catalogue has no Saccharomyces strain match; no unmatched
  bacterial proxy or biological absence claim. Actual00:49Z runner unavailable receipt
  is historical, not a current invocation. Initial sandbox DNS attempts archived;
  subsequent permitted fresh downloads succeeded. Root20/10etc corpus gates and futureCI
  are not borrowed into this source report.'
- 'Fungal-type vacuole, lumen and membrane independent subreview: Local provenance:
  applicable instructions/profile/config/rubrics reread; graph/protein schema and
  command recipe sections inspected. Native schema/helper bytes were used in validation,
  not a full program correctness audit. Root owns remaining cohort/global gates/issue
  publication; this reviewer made no repository or GitHub mutation.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Five complete
  assigned targets and their ten original artifacts reviewed. Whole glycosome is stale:
  reviewed P04789/TIM was added and peroxin import machinery retyped PROTEIN_COMPLEX.
  Both changes are substantively reassessed; other four target hashes are unchanged.
  Original validation/render passes and historical evidence/checks remain immutable.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Four inherited
  scientific occurrences retain exact stable keys, native severities and repository/review/finding
  lineage: whole glycosome first-author, glucose mechanism and whole-membrane molecular
  grounding; glycosome membrane first-author. No additional confirmed typing finding
  is established: the narrower enum prose must be read alongside explicit family-or-class
  and generic-class guidance. The record discloses the heterogeneous class and UNKNOWN
  formation necessity; no automatic complex conversion or invented predecessor is
  asserted.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: All current
  public sources were freshly fetched. Haanstra2008 complete Results/Discussion/main
  Experimental Procedures and Fig2–5 captions, and Furuya2002 complete Methods/Results/Discussion
  and Fig1–4 captions were read. No source pixels, separate supplements/raw data or
  quantitative reanalysis is claimed. Failed S3 routes are not body evidence.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Opperdoes1977
  exact PMID metadata/title only; no abstract and publisher403. Its DOI search zero
  is not absence. Misset1986, Moyersoen2003, de Walque1999, Galland2007, Gualdron-Lopez2013
  and Verplaetse2012 are complete-primary-abstract tiers only. Haanstra2016 and Bauer2017
  are complete secondary review abstracts, not primary experiments.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Current de
  Zoysa1994 evidence is complete primary abstract only. Both publisher PDF routes
  returned HTML Client Challenge despite200; the historical original full-PDF review
  is not a current body reread. Abstract supports acetate-induced fungal CAT reporter
  targeting and pathway compartments; detailed old medium/strain/table/ICL statements
  are not newly certified.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Glucose-associated
  Glc6P accumulation in29–13 does not uniquely resolve the mechanism: PGI truncation
  remains an alternative and PF449 differs. Glycerol/Gly3P plus GK rescue is the stronger
  test. Model membrane removal, partial biological import defects, cell viability
  and organelle-formation necessity remain distinct.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Nine whole-glycosome
  examples comprise six reviewed and three unreviewed; GAPDH O96429 is a fragment.
  TIM is protein alias without indexed geneName; literal gene query zero is not protein
  absence. Reference strain/subspecies entries are not the experimental strains. Automated/by-similarity
  annotations are not direct localization evidence.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Peroxin apparatus
  type refresh is bounded to interacting import machinery, not a permanent stoichiometric
  assembly or membrane residence of every receptor. Closed2462 item4 is historical
  context only and is not reopened or newly disposed of across its other targets.
  The heterogeneous glycolytic set is not automatically a complex.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: All ten assigned
  native protein commands pass. Whole glycosome has nine examples/two COVERED nodes;
  membrane has no examples but one UNANCHORED_WITH_UNIPROT Q38CL4 node; other three
  have empty inventories/zero nodes. Identifier success does not certify semantic
  typing, mechanism, complete composition or necessity.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: All five narratives
  trigger pathway/molecular applicability despite some descriptive graphs. Fresh official
  catalogue has no actual target-host coverage; no unrelated or heterologous-host
  downstream query or biological absence inference. Historical runner failure remains00:49Z,
  not a fresh invocation.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Thirty-three
  local inputs were used:17 common unchanged policy/schema/native files, five targets,
  ten originals and frozen whole glyoxysome neighbor. The neighbor supplies boundary
  context only, not a complete scientific review or disposition. No maintained image,
  physical measurement, trait or verbatim snippet is present in assigned targets.'
- 'Glycosome trio and glyoxysomal lumen/membrane independent subreview: Root owns
  global QC/CI, issue dedup/publication and repository/GitHub mutations. This report
  does not pre-certify final-head or queue outcomes. Record curation remains separate;
  no record or original bundle was edited.'
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
  identities.
- 'Issue #2695 tracks three stale target inputs. Food vacuole adds a membrane STRUCTURE
  node/component_ref and enclosing boundary edge; fungal-type vacuole adds direct
  lumen/membrane part-of edges supported by current GO graph evidence; glycosome adds
  P04789/TIM and retypes peroxin machinery to PROTEIN_COMPLEX. All deltas receive
  substantive source and native-policy reassessment.'
- 'Issue #2696 tracks ten unsupported applicability exclusions. Every original bundle
  has an explicit imodulondb not_applicable row; none omits it. Positive BILBO1/trafficking,
  hemoglobin/heme, hydrolase/V-ATPase, glycolysis/peroxin-import or glyoxylate-cycle/import
  assertions require coverage assessment despite narrow compartment titles or empty
  represented protein inventories.'
- Source commit 85122489fca6bd0f63b1a6b276d138f847405e3e is retained by tag review-base/pr2366-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- All 50 local inputs were frozen before assessment. Ciliary-pocket membrane, ciliary-pocket
  collar and whole glyoxysome are bounded context only, not extra review targets or
  dispositions of their findings.
- Fresh and reused source snapshots retain actual access timestamps and inspection
  tiers. Authority identity does not independently establish structure membership,
  mechanistic action, species-wide generalization or assembly necessity.
- All twenty native protein commands returned zero. Fungal-type vacuole has three
  reviewed hydrolase examples and one COVERED node; its lumen has no component examples
  and one UNANCHORED_WITH_UNIPROT hydrolase-cohort node carrying those three accessions.
  Glycosome has nine examples (six reviewed and three unreviewed) and two COVERED
  nodes; glycosome membrane has no component examples and one UNANCHORED_WITH_UNIPROT
  PEX14 node. The other six records have empty inventories and zero typed molecular
  nodes. Transient xref-backed actors are distinguished from component coverage; checks
  do not certify every narrative claim.
- 'Closed grouped issue #2462 is historical context for the glycosome peroxin component-type
  change. This follow-up makes no disposition of other records or grouped findings
  covered there. Native-validator issue #2514 remains open and reused.'
- 'Five inherited scientific findings remain: a major flagellar-pocket whole-membrane
  versus lipid grounding error; glycosome first-author attribution, qualified glucose-mechanism
  scope and major whole-membrane versus molecular-lipid grounding; and glycosome-membrane
  first-author attribution. Three targets need curation; the other seven have qualified
  positive assessments.'
- A proposed additional glycosome enzyme-cohort typing defect was independently challenged
  against native class-level component guidance and was not established as a confirmed
  record error. The record explicitly describes a heterogeneous class. The narrower
  enum wording does not justify inventing a single family or automatically asserting
  a protein complex; no new scientific issue is claimed for that hypothesis.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014651Z-flagellar-pocket-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014653Z-food-vacuole-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014654Z-fungal-type-vacuole-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014656Z-fungal-type-vacuole-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014657Z-fungal-type-vacuole-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014658Z-glycosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014659Z-glycosome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014700Z-glycosome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014701Z-glyoxysomal-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T014701Z-glyoxysomal-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2366
- https://github.com/CultureBotAI/CellStructureMech/issues/2462
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2695
- https://github.com/CultureBotAI/CellStructureMech/issues/2696
- https://github.com/CultureBotAI/CellStructureMech/issues/2697
- https://github.com/CultureBotAI/CellStructureMech/issues/2698
- https://github.com/CultureBotAI/CellStructureMech/issues/2699
- https://github.com/CultureBotAI/CellStructureMech/issues/2700
- https://github.com/CultureBotAI/CellStructureMech/issues/2701
```
