# PR 2386: current-input review of ten records and adversarial follow-up

- Review: 20261104T050305Z-pr2386-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T04:47:59.512379Z
- Finished UTC: 2026-11-04T05:03:05Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input successor for all ten PR2386 records. Cytostome and DASH were stale and substantively refreshed: the former hierarchy finding is resolved by prior curation tracked in closed #2461, while the latter new constituent edges do not resolve its grounding or bounded association-evidence findings. Seven inherited scientific findings remain open across six records (three major, four minor); four records retain qualified positive outcomes. Seven formal expression-only applicability exclusions and five failed-access evidence-kind occurrences are corrected, while the three justified dinoflagellate morphology exclusions are retained. All 20 original artifacts remain immutable; only this linked review pair is added.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 063ec99b63d964ef35acc14be323160a50835634. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 9a46ecafa001228b8ebdc17ebb7868e725711493.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base e1e8bf616b2ed45741e993b1993cb69017cf2e61.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:cullin_e_ubiquitin_ligase_complex | data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml | maintained | Cullin-E ubiquitin ligase complex |
| GO:0034270 | data/structures/other/cvt_complex.yaml | maintained | Cvt complex |
| GO:0031910 | data/structures/other/cytostome.yaml | maintained | cytostome |
| GO:0042729 | data/structures/other/dash_complex.yaml | maintained | DASH complex |
| GO:0031431 | data/structures/other/dbf4_dependent_protein_kinase_complex.yaml | maintained | Dbf4-dependent protein kinase complex |
| GO:0043625 | data/structures/other/delta_dna_polymerase_complex.yaml | maintained | delta DNA polymerase complex |
| GO:1990125 | data/structures/other/diaa_complex.yaml | maintained | DiaA complex |
| GO:0097684 | data/structures/other/dinoflagellate_antapex.yaml | maintained | dinoflagellate antapex |
| GO:0097687 | data/structures/other/dinoflagellate_antapical_horn.yaml | maintained | dinoflagellate antapical horn |
| GO:0097683 | data/structures/other/dinoflagellate_apex.yaml | maintained | dinoflagellate apex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate cellstructuremech:cullin_e_ubiquitin_ligase_complex | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex | Documented focused command passed. |
| validate-strict cellstructuremech:cullin_e_ubiquitin_ligase_complex | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex | Documented focused command passed. |
| validate GO:0034270 | passed | True | GO:0034270 | Documented focused command passed. |
| validate-strict GO:0034270 | passed | True | GO:0034270 | Documented focused command passed. |
| validate GO:0031910 | passed | True | GO:0031910 | Documented focused command passed. |
| validate-strict GO:0031910 | passed | True | GO:0031910 | Documented focused command passed. |
| validate GO:0042729 | passed | True | GO:0042729 | Documented focused command passed. |
| validate-strict GO:0042729 | passed | True | GO:0042729 | Documented focused command passed. |
| validate GO:0031431 | passed | True | GO:0031431 | Documented focused command passed. |
| validate-strict GO:0031431 | passed | True | GO:0031431 | Documented focused command passed. |
| validate GO:0043625 | passed | True | GO:0043625 | Documented focused command passed. |
| validate-strict GO:0043625 | passed | True | GO:0043625 | Documented focused command passed. |
| validate GO:1990125 | passed | True | GO:1990125 | Documented focused command passed. |
| validate-strict GO:1990125 | passed | True | GO:1990125 | Documented focused command passed. |
| validate GO:0097684 | passed | True | GO:0097684 | Documented focused command passed. |
| validate-strict GO:0097684 | passed | True | GO:0097684 | Documented focused command passed. |
| validate GO:0097687 | passed | True | GO:0097687 | Documented focused command passed. |
| validate-strict GO:0097687 | passed | True | GO:0097687 | Documented focused command passed. |
| validate GO:0097683 | passed | True | GO:0097683 | Documented focused command passed. |
| validate-strict GO:0097683 | passed | True | GO:0097683 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Whole-record applicability was assessed for all ten targets. Seven positive molecular or pathway narratives require source-coverage assessment, correcting their formal expression-only exclusions. The three dinoflagellate records make morphology/topology claims and explicitly defer molecular claims, so their prose exclusions remain justified. Actual official catalogue coverage is separate from biological applicability: no matching yeast or Trypanosoma dataset is substituted with a foreign host. DiaA is checked in the real five-strain E. coli precise1k dataset; absence of above-threshold membership is bounded computational noncoverage, not biological absence or assembly evidence. The historical unavailable runner receipt is not presented as a fresh invocation. |
| Independent claim-level source review | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native Cullin-E ubiquitin ligase complex UniProt verify check | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Cullin-E ubiquitin ligase complex UniProt causal check | passed | True | cellstructuremech:cullin_e_ubiquitin_ligase_complex | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Cvt complex UniProt verify check | passed | True | GO:0034270 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Cvt complex UniProt causal check | passed | True | GO:0034270 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native cytostome UniProt verify check | passed | True | GO:0031910 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native cytostome UniProt causal check | passed | True | GO:0031910 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DASH complex UniProt verify check | passed | True | GO:0042729 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DASH complex UniProt causal check | passed | True | GO:0042729 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Dbf4-dependent protein kinase complex UniProt verify check | passed | True | GO:0031431 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Dbf4-dependent protein kinase complex UniProt causal check | passed | True | GO:0031431 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native delta DNA polymerase complex UniProt verify check | passed | True | GO:0043625 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native delta DNA polymerase complex UniProt causal check | passed | True | GO:0043625 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DiaA complex UniProt verify check | passed | True | GO:1990125 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DiaA complex UniProt causal check | passed | True | GO:1990125 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate antapex UniProt verify check | passed | True | GO:0097684 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate antapex UniProt causal check | passed | True | GO:0097684 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate antapical horn UniProt verify check | passed | True | GO:0097687 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate antapical horn UniProt causal check | passed | True | GO:0097687 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate apex UniProt verify check | passed | True | GO:0097683 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native dinoflagellate apex UniProt causal check | passed | True | GO:0097683 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact DASH/DDD complex boundary

identity: supported. Targets: GO:0042729.

GO0042729 and primary purification identify the same fungal outer-kinetochore assembly. Nuclear complex parent and kinetochore/outer-kinetochore parthood are supported. The declared seven curated subunits do not imply an exhaustive ten-subunit closure; explicit Dad3/Dad4/Hsk boundary work remains.

### Substantive seven-node and seven-edge stale refresh

provenance: supported. Targets: GO:0042729.

DASH alone differs from its frozen original: dated history plus seven component_ref nodes and constituent contributes-to edges. Current reviewed identities and independent Cheeseman/Janke native complex purifications support each new edge. No atomic interface, all-subunit necessity or ring-force mechanism is added; F1/F2 remain independent unresolved curation.

### Seven exact full-protein families

grounding: concern. Targets: GO:0042729.

Seven exact DASH family identities and their reviewed example xrefs are independently verified. All seven current component classes remain label-only, so inherited minor F1 remains. This is a supported class mapping, not an inference from optional missing examples or broad domains.

### Seven exact S288c reference proteins

grounding: supported. Targets: GO:0042729.

All seven maintained accessions, primary symbols/loci, reviewed status and reference taxon559292 agree with native authorities and fresh singleton gene queries. DAD2 has HSK1 synonym, which does not silently identify all omitted Hsk microproteins. Species4932 and reference559292 are distinguished.

### Source-adjacent localization evidence

evidence: supported. Targets: GO:0042729.

Native location notes/evidence codes support the declared nuclear/spindle/kinetochore and Ask1-origin contexts. Cheeseman/Janke localization text is independently body-read; Huh, Hofmann, later attachment/oligomerization and Ask1-origin papers are complete abstract/native-annotation tier only, without raw-image certification.

### Conditional Spc34 association/recovery evidence

grounding: concern. Targets: GO:0042729.

Janke p182/Fig1B directly compares Dad2-ProA recovery after4h37C: spc34-3 yields bait alone while SPC34 yields the complete reported complex. Inherited F2 remains a narrow association/stability-evidence gap. UNKNOWN alone is not defective; viability, microtubule binding and universal formation are not equivalent, and no new experiment is required.

### Attachment and ring evidence scope

evidence: supported. Targets: GO:0042729.

Purified native complex binds microtubules; localized complex and genetics support outer-kinetochore attachment context. Miranda complete primary abstract supports recombinant ten-subunit rings/helices, not a newly inspected EM dataset or quantified coupling model. The NONMECHANISTIC assembly/function outline stays within this scope.

### Cdc7-Dbf4 heterodimer

identity: supported. Targets: GO:0031431.

GO0031431 exact DDK identity and nuclear protein-complex parent agree with Cdc7 catalytic and Dbf4 regulatory roles. Species-qualified narrow synonyms are not universal paralogue labels. GO/native annotations support origin activation; Bell-Dutta is secondary abstract-only.

### Exact Dbf4 versus kinase-domain candidates

grounding: concern. Targets: GO:0031431.

IPR051590 is an exact Dbf4 family with native P32325 xref/signature, while current Dbf4 row remains label-only. IPR013939 is only a central-region domain, and native Cdc7 xrefs are broad kinase annotations. Retain inherited minor F1 without promoting generated description or declaring universal absence of another Cdc7 family.

### Current exact Cdc7 and Dbf4 references

grounding: supported. Targets: GO:0031431.

P06243 CDC7/YDL017W and P32325 DBF4/YDR052C are reviewed559292 references; each exact reviewed gene query is a singleton. These identities corroborate class examples without proving detailed phosphorylation chemistry.

### Origin activation remains coarse

graph: supported. Targets: GO:0031431.

GO0006270/0031431 and native curated roles support the declared two-constituent FUNCTION/NONMECHANISTIC outline. No MCM-site phosphorylation sequence or Cdc45 loading edge is asserted, and no fresh Bell full-body or its cited primary experiments are claimed.

### Formation unknown distinct from function

grounding: unknown. Targets: GO:0031431.

Two constituents and origin-activation function do not establish a complete cross-condition assembly-depletion matrix. UNKNOWN remains appropriately bounded outside the concrete exact-family finding; no optional assay requirement is invented.

### Generic Polδ and scoped yeast trimer

identity: supported. Targets: GO:0043625.

GO0043625 denotes a variable-composition polymerase complex; current record explicitly scopes Pol3/Pol31/Pol32 to budding yeast. OLS confirms DNA-polymerase/nuclear-complex is_a, nuclear-replisome part_of and Eukaryota constraint; no species-specific composition is universalized.

### Preserved conflict resolved with later primary abstract

evidence: supported. Targets: GO:0043625.

Gerik/Burgers1998 primary abstracts support three subunits/reconstitution but older dimer inference. Johansson2001 abstract explicitly revises this to1:1:1 monomeric Polδ, with tested concentration range0.1–20µM and hydrodynamic/two-hybrid evidence. Current resolved discussion correctly preserves the GO conflict; no raw-data or full-body read is claimed.

### Bounded candidate scope without invented exact assignments

grounding: supported. Targets: GO:0043625.

Pol3 type-B family is broader; Pol31 IPR024826 covers both eukaryotic Polδ and archaeal PolII; POLD3/Cdc27 IPR019038 is named but native P47110 lacks an InterPro xref. Retain label-only class uncertainty rather than force those candidates or assert exhaustive family absence. No new confirmed finding follows.

### Three exact references and localization tiers

grounding: supported. Targets: GO:0043625.

P15436 POL3/YDL102W, P46957 POL31/YJR006W and P47110 POL32/YJR043C are reviewed559292 examples and singleton exact queries. P15436 nuclear/Huh link is experimental annotation; Pol31/32 nuclear annotations are by similarity and are not promoted to newly observed microscopy.

### Reconstitution and dispensability remain scoped

grounding: unknown. Targets: GO:0043625.

Primary abstracts distinguish Polδ* two-subunit enzyme, three-subunit reconstitution and pol32 deletion growth/function effects. They do not force every current constituent into a universal formation-essential category. UNKNOWN fields are not independently defects; no additional experimental requirement.

### Broad DNA-replication functional outline

graph: supported. Targets: GO:0043625.

Three component_ref contributions and broad GO0006260 function are consistent with sources and FUNCTION/NONMECHANISTIC scope. PCNA/RFC clients, catalytic fidelity and detailed strand-specific order are not silently asserted as graph constituents or steps.

### Free homotetramer separated from larger DNA complex

identity: supported. Targets: GO:1990125.

GO1990125 exact identity is a pair of DiaA homodimers; GO1990102 separately contains free DiaA as has_part. The current boundary correctly excludes DnaA and oriC from the free tetramer constituents while allowing their functional interaction context.

### Exact DiaA family distinct from GmhA

grounding: concern. Targets: GO:1990125.

IPR023070 is the exact DiaA family with specific HAMAP/NCBIfam signatures and native P66817 xref; current class remains label-only. Broader IPR035461/IPR050099 are not exact substitutes. Retain inherited minor F1.

### Correct reviewed K12 reference and locus

grounding: supported. Targets: GO:1990125.

P66817 is reviewed diaA/yraO, loci b3149/JW3118, tax83333, and the current exact gene query returns only that accession. Species562 canonical evidence differs from the reference annotation and named K12 experimental derivatives.

### Tetramer function without invariant solution or universal necessity

evidence: supported. Targets: GO:1990125.

Complete primary abstract and bounded retained PDF text support the active homotetramer and promoted DnaA assembly/initiation. Dilution-dependent dimer/tetramer interpretation and speculative phosphosugar regulation remain explicit; UNKNOWN does not become a universal essentiality claim. No missing passages, pixels or coordinates are certified.

### Initiation facilitation is nonmechanistic

graph: supported. Targets: GO:1990125.

Single DiaA constituent→tetramer→replication-initiation outline is bounded by GO and primary evidence. Larger DnaA-DNA assembly is deliberately outside constituent inventory; no ordered chemical sequence or direct DNA binding by free DiaA is asserted.

### Matched dataset and threshold-negative result

scope: supported. Targets: GO:1990125.

Official precise1k is a five-strain E.coli dataset, not the exact K12 mutant panel. Verified b3149 is present across201 returned rows with no above-threshold membership; there is no hit to summarize as a supporting module. This neither refutes DiaA biology nor establishes absence, localization, formation or causal regulation.

### Actual whole-record applicability

scope: concern. Targets: GO:0042729.

Original formal check exempts source cross-checks because no expression assertion exists, despite positive molecular content. Fresh catalogue gives no natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k locus/threshold data. Historical runner failure is separately dated and is not a new execution.

### Taxon and canonical experiment boundaries

scope: supported. Targets: GO:0042729.

Species and reference-strain authorities agree. COMMON is qualitative and no universal strain census is inferred. Yeast examples are S288c references, whereas native paper preparations/derivatives retain their stated scope; DiaA computational five-strain context is distinct from experimental K12 derivatives.

### Append-only history and exact predecessor continuity

provenance: supported. Targets: GO:0042729.

Current discussions and original findings/actions were read. Historical rationale/posed_date remain provenance, not mandatory current-state inventory; current notes/prompt may be narrowed after separately authorized supported curation. No neighboring/category/group issue is resolved by inference.

### Actual original/native checks

schema: supported. Targets: GO:0042729.

All four original pairs pass native validate/render with52 historical inputs and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological or family-completeness certificates.

### Complete record scope with tier limits

completeness: supported. Targets: GO:0042729.

Complete current record and immutable original pair reviewed. No maintained images or measured-property rows require pixel/units work. Positive identity/function assessments and source-access limits remain explicit, without treating inaccessible sources as false.

### Current independent verdict

other: concern. Targets: GO:0042729.

needs_curation: two inherited minor findings confirmed; current seven-node/edge additions supported.

### Actual whole-record applicability

scope: concern. Targets: GO:0031431.

Original formal check exempts source cross-checks because no expression assertion exists, despite positive molecular content. Fresh catalogue gives no natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k locus/threshold data. Historical runner failure is separately dated and is not a new execution.

### Taxon and canonical experiment boundaries

scope: supported. Targets: GO:0031431.

Species and reference-strain authorities agree. COMMON is qualitative and no universal strain census is inferred. Yeast examples are S288c references, whereas native paper preparations/derivatives retain their stated scope; DiaA computational five-strain context is distinct from experimental K12 derivatives.

### Append-only history and exact predecessor continuity

provenance: supported. Targets: GO:0031431.

Current discussions and original findings/actions were read. Historical rationale/posed_date remain provenance, not mandatory current-state inventory; current notes/prompt may be narrowed after separately authorized supported curation. No neighboring/category/group issue is resolved by inference.

### Actual original/native checks

schema: supported. Targets: GO:0031431.

All four original pairs pass native validate/render with52 historical inputs and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological or family-completeness certificates.

### Complete record scope with tier limits

completeness: supported. Targets: GO:0031431.

Complete current record and immutable original pair reviewed. No maintained images or measured-property rows require pixel/units work. Positive identity/function assessments and source-access limits remain explicit, without treating inaccessible sources as false.

### Current independent verdict

other: concern. Targets: GO:0031431.

needs_curation: inherited minor exact-family finding independently confirmed; supported identity/function and remaining unknowns preserved.

### Actual whole-record applicability

scope: concern. Targets: GO:0043625.

Original formal check exempts source cross-checks because no expression assertion exists, despite positive molecular content. Fresh catalogue gives no natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k locus/threshold data. Historical runner failure is separately dated and is not a new execution.

### Taxon and canonical experiment boundaries

scope: supported. Targets: GO:0043625.

Species and reference-strain authorities agree. COMMON is qualitative and no universal strain census is inferred. Yeast examples are S288c references, whereas native paper preparations/derivatives retain their stated scope; DiaA computational five-strain context is distinct from experimental K12 derivatives.

### Append-only history and exact predecessor continuity

provenance: supported. Targets: GO:0043625.

Current discussions and original findings/actions were read. Historical rationale/posed_date remain provenance, not mandatory current-state inventory; current notes/prompt may be narrowed after separately authorized supported curation. No neighboring/category/group issue is resolved by inference.

### Actual original/native checks

schema: supported. Targets: GO:0043625.

All four original pairs pass native validate/render with52 historical inputs and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological or family-completeness certificates.

### Complete record scope with tier limits

completeness: supported. Targets: GO:0043625.

Complete current record and immutable original pair reviewed. No maintained images or measured-property rows require pixel/units work. Positive identity/function assessments and source-access limits remain explicit, without treating inaccessible sources as false.

### Current independent verdict

other: supported. Targets: GO:0043625.

pass_with_limitations: no supported scientific finding; identity/composition/function positive, exact-family and access limits retained.

### Actual whole-record applicability

scope: concern. Targets: GO:1990125.

Original formal check exempts source cross-checks because no expression assertion exists, despite positive molecular content. Fresh catalogue gives no natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k locus/threshold data. Historical runner failure is separately dated and is not a new execution.

### Taxon and canonical experiment boundaries

scope: supported. Targets: GO:1990125.

Species and reference-strain authorities agree. COMMON is qualitative and no universal strain census is inferred. Yeast examples are S288c references, whereas native paper preparations/derivatives retain their stated scope; DiaA computational five-strain context is distinct from experimental K12 derivatives.

### Append-only history and exact predecessor continuity

provenance: supported. Targets: GO:1990125.

Current discussions and original findings/actions were read. Historical rationale/posed_date remain provenance, not mandatory current-state inventory; current notes/prompt may be narrowed after separately authorized supported curation. No neighboring/category/group issue is resolved by inference.

### Actual original/native checks

schema: supported. Targets: GO:1990125.

All four original pairs pass native validate/render with52 historical inputs and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological or family-completeness certificates.

### Complete record scope with tier limits

completeness: supported. Targets: GO:1990125.

Complete current record and immutable original pair reviewed. No maintained images or measured-property rows require pixel/units work. Positive identity/function assessments and source-access limits remain explicit, without treating inaccessible sources as false.

### Current independent verdict

other: concern. Targets: GO:1990125.

needs_curation: inherited minor exact-family finding independently confirmed; supported identity/function and remaining unknowns preserved.

### Historical failed access kind correction

provenance: concern. Targets: GO:0031431.

Original response honestly says failed body access and context_only, but is typed database. Correct only to validation/context_only; do not accuse the original of an unread-body claim, replace its timestamp or infer a scientific contradiction.

### Historical failed access kind correction

provenance: concern. Targets: GO:0043625.

Original response honestly says failed body access and context_only, but is typed database. Correct only to validation/context_only; do not accuse the original of an unread-body claim, replace its timestamp or infer a scientific contradiction.

### Historical failed access kind correction

provenance: concern. Targets: GO:0043625.

Original response honestly says failed body access and context_only, but is typed database. Correct only to validation/context_only; do not accuse the original of an unread-body claim, replace its timestamp or infer a scientific contradiction.

### native validation

schema: supported. Targets: GO:0034270.

One REVIEWED P14904 example and one COVERED typed node. Original native pair/historical provenance and current frozen inputs all pass.

### structured source

evidence: supported. Targets: GO:0034270.

The original checks[4] formal exemption is based solely on absence of an expression-module assertion. Whole-record positive APE1/Atg19/Atg11/Cvt pathway claims trigger native applicability assessment. Fresh official coverage has no matching biological host; no downstream foreign-host proxy. Historical runner failure remains separately dated.

### completeness

completeness: supported. Targets: GO:0034270.

Full maintained fields read. No images or quantitative physical properties occur. No optional protein inventory, image, broader family mapping or new experiment is mandated solely because a slot is empty.

### evidence access

evidence: supported. Targets: GO:0034270.

All direct cited DOI/PMID identities and complete indexed abstracts read; actual genuine primary body scopes are separately named. Unavailable routes and retained retrieval times are explicit; no snippets, figure pixels, supplementary or raw-data analyses invented.

### taxon scope

scope: supported. Targets: GO:0034270.

Natural S.cerevisiae species scope is supported; S288C accession reference is not conflated with SEY6210-derived primary experiments or recombinant E.coli/rabbit systems.

### native validation

schema: supported. Targets: GO:0031910.

Zero protein_examples and zero typed GENE_OR_PROTEIN nodes; empty-inventory pass is not molecular completeness evidence. Original native pair/historical provenance and current frozen inputs all pass.

### structured source

evidence: supported. Targets: GO:0031910.

The original checks[4] formal exemption is based solely on absence of an expression-module assertion. Whole-record positive endocytic pathway and localized-protein discussion claims trigger native applicability assessment. Fresh official coverage has no matching biological host; no downstream foreign-host proxy. Historical runner failure remains separately dated.

### completeness

completeness: supported. Targets: GO:0031910.

Full maintained fields read. No images or quantitative physical properties occur. No optional protein inventory, image, broader family mapping or new experiment is mandated solely because a slot is empty.

### evidence access

evidence: supported. Targets: GO:0031910.

All direct cited DOI/PMID identities and complete indexed abstracts read; actual genuine primary body scopes are separately named. Unavailable routes and retained retrieval times are explicit; no snippets, figure pixels, supplementary or raw-data analyses invented.

### taxon scope

scope: supported. Targets: GO:0031910.

T.cruzi epimastigote structural/canonical claim matches Alcantara abstract; Chasen Y-strain epimastigotes and replicative amastigotes are scoped, without requiring record expansion to every life stage or universal exclusivity.

### identity boundary

identity: concern. Targets: GO:0034270.

GO0034270 is exactly the Cvt complex, parent protein-containing complex/cytoplasm parthood supported. Its short preApe1-only wording is genuinely copied from GO, but the active Atg19/Atg11 categorical exclusion conflicts with cited Shintani and GO0032258. Preserve the authority-text conflict rather than call the definition fabricated.

### cargo receptor composition

representation: concern. Targets: GO:0034270.

Shintani S8 calls Atg19-Ape1 the Cvt complex; S10 includes Ape1/Ams1/Atg19 and distinguishes Atg11 recruitment machinery. Scott shows precursor-specific association and cotransport/degradation. Receptor binding is not merely a transient before-assembly chaperone action; a blanket constituent exclusion needs correction, without adding every Atg factor.

### protein grounding

grounding: supported. Targets: GO:0034270.

P14904 reviewed S288C APE1/precursor identity and exact gene query are correct. The three vacuolar-localization PMID joins are real and support localization, not automatically Cvt membership. Broad M18 family/domain2 candidates do not force an exact cargo-class grounding.

### necessity

scope: unknown. Targets: GO:0034270.

Ape1 is the defining cargo core, supporting its constitutive membership. PAS organization/transport under growing conditions and starvation contrasts do not establish universal physical assembly necessity for every receptor/scaffold or require a new assay. This bounded uncertainty does not create a second finding.

### graph

graph: concern. Targets: GO:0034270.

Coarse membership, double-membrane enclosure and vacuolar delivery topology are supported; the graph description should distinguish Ape1 self-assembly from Atg19-containing complex formation. NONMECHANISTIC scope does not cure an explicit constituent boundary error.

### history

provenance: supported. Targets: GO:0034270.

Retain exact original F1 lineage. The current active resolution_note is challenged; dated rationale/posed_date/history must be preserved with appended evidence and an updated active status/note. No rewriting historical failed searches or inferring a prior issue resolution.

### identity hierarchy refresh

identity: supported. Targets: GO:0031910.

Fresh GO directly supports is_a GO0110165 and part_of GO0005886. Current changed parent/parthood/evidence/history removes precisely the old hierarchy error. Definition remains the stable ingestion structure, with larger cytopharynx boundary explicitly deferred.

### resolved lineage

provenance: supported. Targets: GO:0031910.

Original F1 cytostome-plasma-membrane-parthood is resolved on inspected current bytes. Already-closed2461 documents prior curation, not a fix made by this PR; no terminal disposition of the other grouped2461 records or uninspected prior category observations.

### composition

grounding: supported. Targets: GO:0031910.

Chasen establishes endogenous CP1 localization and associated/overexpressed CP2/3 across the larger complex. Predicted coiled-coil/SMC regions are not exact entire-protein classes or proof of a three-component opening assembly; existing targeted TODO is legitimate.

### necessity

scope: supported. Targets: GO:0031910.

No molecular essentiality is asserted; localization, co-isolation and cytochalasin uptake inhibition do not alone establish protein-deletion assembly necessity. No mandatory empty protein example finding.

### uptake graph

graph: supported. Targets: GO:0031910.

Porto complete abstract supports the coarse cytostome/cytopharynx entry to an early vesicular-tubular network and reservosome storage; Chasen protein feeding reinforces entry. Frozen local reservosome destination is exact. The NONMECHANISTIC graph does not claim universal kinetics, molecular machinery or exclusive uptake in all stages. Lipid-specific experimental details remain outside the inspected Porto abstract; no unread body is certified.

### Exact structure identity and boundaries

identity: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Local CulE association identity and broader CRLparent preserve the divergent source-defined scaffold; Hu2017 WDR1 complex has another cullin locus.

### Molecular identity and scoped inventory

grounding: concern. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Q383D5→sourceCulE andQ38C61→sourceRbx1 verified by native locus bridges; Q384S1/Tb11.02.5340/212aa is wrong for sourceSkp1.2/Tb927.9.8370/158aa. Q38ED0 nativeVEuPathDB/Ensembl bridge identifies replacement. ORF names differ from formal primary genes; generated names are not membership evidence.

### Family and class boundaries

grounding: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Broad Cullin,RING-box,SKP1-like families do not discriminate the source paralogs or establish one obligatory four-kelch cassette; generated IPR051031 prose excluded. Generic scaffold/adaptor classes are permitted and UNKNOWN necessities are honest.

### Formation necessity and untested mechanisms

evidence: unknown. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Co-isolation and RNAi cellular outputs do not test persistence of a complete complex without each constituent. UNKNOWN formation necessities remain appropriate; no direct contact,simultaneous occupancy or absolute stoichiometry inferred.

### Every maintained graph actor and edge

graph: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Five intervention-output edges preserve distinct24hLFQ,0–36h1K2N and representative Golgi observations. Increased KKT9/decreasedTb927.10.8810 are abundance readouts, not direct substrates or degradation rates; no PLK/WDR1 mechanism imported.

### Taxonomy, canonical examples and experimental scopes

scope: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Tbrucei5691/TREU927185431 resolve. PCF Lister427 isolation,2T1qPCR,incompletely specifiedRNAi stage and Fig6bloodstream schematic remain distinct. Reference927release42 database is not cultured strain; no scope transfer from bacterial recombinant hosts.

### Quantities, timing and dimensions

quantity: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Four enriched kelch loci do not imply four copies or simultaneous occupancy. ActualFig6timepoints0/12/24/36h,Fig7threeinduced/threeuninduced and representative Golgi images remain distinct; no pie rounding recast as rawcounts. PRIDEsixWT versusMethods/S3sevenWT controls preserved. No physical complex dimensions inferred.

### Source tiers and exact read extents

evidence: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Genuine2025JATS,S3boundedrows and actualFig2/6/7pixels support the scoped claims. Hu2017sec004/Methods delineate conflicting olderCullin4 association. Metadata/nativeaccession resolution is not direct ligase activity; no raw spectra or full-workbook reanalysis.

### Image access and attribution

evidence: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

No maintained image. Fresh externalFig2allpanels/Fig6A–D/Fig7actualpixels viewed against captions and CC-BY4.0 source; these depict enrichment/phenotype/proteomics, not an imaged CulE particle. Fig8onlycaption read, generic human model remains explicitly excluded as exact structure.

### Complete record and native inventory coverage

completeness: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Three unreviewed example occurrences/three distinct accessions and one native COVERED Cullin-E node. Native pass does not establish the disputed Skp1.2 biological assignment. Four constituent classes,assay outputs,dataset and unresolved architecture well scoped; wrongSkp1.2 and current staleexample discussion are addressed by inherited action. No extra unrelated coisolates promoted to mandatory subunits.

### Historical rationale and prior observations

provenance: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Dated rationale/history and actual earlier source-access observations remain append-only. Current notes/prompts may be corrected or dated clarification appended. No neighboring/group issue resolution, false historical search claim, or rewriting original bundles.

### Frozen inputs and deterministic original pair

schema: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Native original validate/render0 and exact Markdown; 14 historical input occurrences match source. Current target unchanged. Original batch26 global gate scope is a valid historical execution origin, not current-head attestation.

### Whole-record structured-source applicability

evidence: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Positive molecular,source-locus,ubiquitylation and proteomics assertions trigger coverage assessment. Fresh complete official catalogue lacks matchingTrypanosoma/strains; no relevant downstream module query and no unrelated host proxy. Historicalrunnerunavailable remains separate from currentfallback; original expression-only exclusion corrected.

### Independent current scientific disposition

consistency: concern. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex.

Needs curation for one independently confirmed inherited major wrongSkp1.2accession; other positive scoped assessments and uncertainty retained.

### Exact structure identity and boundaries

identity: concern. Targets: GO:0097684.

Exact GO antapex class is intended, but maintained anterior definition repeats GO0097684 error and conflicts with expert posterior orientation and its own posterior notch edge.

### Molecular identity and scoped inventory

grounding: supported. Targets: GO:0097684.

No components/gene symbols/protein instances are asserted. Historical OPEN discussion requests specifically localized constituents; generic whole-cell membranes/cellulose/proteins are not automatically regional constituents. No missing optional field or family/complex typing defect manufactured.

### Family and class boundaries

grounding: supported. Targets: GO:0097684.

Horn versus general regional class and parent compartment remain separate. No generic dinoflagellate molecular family is assigned to the regional point; no exact-family requirement invented.

### Formation necessity and untested mechanisms

evidence: unknown. Targets: GO:0097684.

Morphological topology and class constraints do not establish localized constituent formation requirements or molecular mechanism. No component essentiality claim exists to validate.

### Every maintained graph actor and edge

graph: supported. Targets: GO:0097684.

Six structure nodes/five edges retain class,hypocone parthood,horn subclass,notch-to-sulcus and posterior extension; posterior edge remains correct despite contradictory top-level definition.

### Taxonomy, canonical examples and experimental scopes

scope: supported. Targets: GO:0097684.

GO only_in_taxon2864 and ENA Dinophyceaeclass support taxonomic restriction. VARIABLE is qualitative; no quantitative census established. Horn thecate qualifier and optional morphological features remain bounded.

### Quantities, timing and dimensions

quantity: supported. Targets: GO:0097684.

No size,stoichiometry or rate asserted; topological/morphological wording does not supply quantitative population frequency or universal horn/groove presence.

### Source tiers and exact read extents

evidence: supported. Targets: GO:0097684.

Current GO/ENA and authored expert morphology are authority evidence. Taylor1980, where cited, is complete native abstract/bibliographic corroboration only; publisher403 is validation context, not primary body support. No morphology figure pixels or uninspected paper body claimed.

### Image access and attribution

evidence: not_applicable. Targets: GO:0097684.

No maintained image; expert-page captions and text inspected, no dinoflagellate pixels or uninspected Taylor figures certified.

### Complete record and native inventory coverage

completeness: supported. Targets: GO:0097684.

Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation.No automatic optionalprotein,canonicalspecies,image,dimension or molecularmechanism requirement. Correct regional boundaries and uncertainty remain positively assessed.

### Historical rationale and prior observations

provenance: supported. Targets: GO:0097684.

Dated rationale/history and actual earlier source-access observations remain append-only. Current notes/prompts may be corrected or dated clarification appended. No neighboring/group issue resolution, false historical search claim, or rewriting original bundles.

### Frozen inputs and deterministic original pair

schema: supported. Targets: GO:0097684.

Native original validate/render0 and exact Markdown; 15 historical input occurrences match source. Current target unchanged. Original batch26 global gate scope is a valid historical execution origin, not current-head attestation.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0097684.

Complete record makes morphology/topology claims and explicitly defers molecular constituents/mechanisms. Original prose physical-scope exclusion is legitimate; absent formal adapter row is not a defect. Catalogue also has no matchingDinophyceae, but actual morphology scope—not biological absence—establishes exclusion.

### Independent current scientific disposition

consistency: concern. Targets: GO:0097684.

Needs curation for one independently confirmed inherited major anterior/posterior definition reversal; other positive scoped assessments and uncertainty retained.

### Exact structure identity and boundaries

identity: supported. Targets: GO:0097687.

Exact GO0097687 horn is the thecate specialization of antapex; direct class relation and inherited hypocone containment are correctly distinguished. It does not repeat parent anterior error.

### Molecular identity and scoped inventory

grounding: supported. Targets: GO:0097687.

No components/gene symbols/protein instances are asserted. Historical OPEN discussion requests specifically localized constituents; generic whole-cell membranes/cellulose/proteins are not automatically regional constituents. No missing optional field or family/complex typing defect manufactured.

### Family and class boundaries

grounding: supported. Targets: GO:0097687.

Horn versus general regional class and parent compartment remain separate. No generic dinoflagellate molecular family is assigned to the regional point; no exact-family requirement invented.

### Formation necessity and untested mechanisms

evidence: unknown. Targets: GO:0097687.

Morphological topology and class constraints do not establish localized constituent formation requirements or molecular mechanism. No component essentiality claim exists to validate.

### Every maintained graph actor and edge

graph: supported. Targets: GO:0097687.

Three structure nodes/three edges distinguish direct horn is_a antapex,parent part_of hypocone and inferred horn parthood; nonmechanistic and no falsely direct ontology parthood assertion.

### Taxonomy, canonical examples and experimental scopes

scope: supported. Targets: GO:0097687.

GO only_in_taxon2864 and ENA Dinophyceaeclass support taxonomic restriction. VARIABLE is qualitative; no quantitative census established. Horn thecate qualifier and optional morphological features remain bounded.

### Quantities, timing and dimensions

quantity: supported. Targets: GO:0097687.

No size,stoichiometry or rate asserted; topological/morphological wording does not supply quantitative population frequency or universal horn/groove presence.

### Source tiers and exact read extents

evidence: supported. Targets: GO:0097687.

Current GO/ENA and authored expert morphology are authority evidence. Taylor1980, where cited, is complete native abstract/bibliographic corroboration only; publisher403 is validation context, not primary body support. No morphology figure pixels or uninspected paper body claimed.

### Image access and attribution

evidence: not_applicable. Targets: GO:0097687.

No maintained image; expert-page captions and text inspected, no dinoflagellate pixels or uninspected Taylor figures certified.

### Complete record and native inventory coverage

completeness: supported. Targets: GO:0097687.

Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation.No automatic optionalprotein,canonicalspecies,image,dimension or molecularmechanism requirement. Correct regional boundaries and uncertainty remain positively assessed.

### Historical rationale and prior observations

provenance: supported. Targets: GO:0097687.

Dated rationale/history and actual earlier source-access observations remain append-only. Current notes/prompts may be corrected or dated clarification appended. No neighboring/group issue resolution, false historical search claim, or rewriting original bundles.

### Frozen inputs and deterministic original pair

schema: supported. Targets: GO:0097687.

Native original validate/render0 and exact Markdown; 15 historical input occurrences match source. Current target unchanged. Original batch26 global gate scope is a valid historical execution origin, not current-head attestation.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0097687.

Complete record makes morphology/topology claims and explicitly defers molecular constituents/mechanisms. Original prose physical-scope exclusion is legitimate; absent formal adapter row is not a defect. Catalogue also has no matchingDinophyceae, but actual morphology scope—not biological absence—establishes exclusion.

### Independent current scientific disposition

consistency: supported. Targets: GO:0097687.

Pass with limitations: exact morphology/topology positively supported; no confirmed record finding. Parent antapex definition issue is not duplicated because this target does not repeat the erroneous direction; no molecular/quantitative scope invented.

### Exact structure identity and boundaries

identity: supported. Targets: GO:0097683.

Exact GO0097683 anterior apex of epicone and broader cellular-anatomical parent are supported. Narrower horn and possible groove remain distinct, not universal features.

### Molecular identity and scoped inventory

grounding: supported. Targets: GO:0097683.

No components/gene symbols/protein instances are asserted. Historical OPEN discussion requests specifically localized constituents; generic whole-cell membranes/cellulose/proteins are not automatically regional constituents. No missing optional field or family/complex typing defect manufactured.

### Family and class boundaries

grounding: supported. Targets: GO:0097683.

Horn versus general regional class and parent compartment remain separate. No generic dinoflagellate molecular family is assigned to the regional point; no exact-family requirement invented.

### Formation necessity and untested mechanisms

evidence: unknown. Targets: GO:0097683.

Morphological topology and class constraints do not establish localized constituent formation requirements or molecular mechanism. No component essentiality claim exists to validate.

### Every maintained graph actor and edge

graph: supported. Targets: GO:0097683.

Five structure nodes/four edges retain apexclass,epiconeparthood,hornsubclass and groovefound-on relation; no groove presence in every dinoflagellate is asserted.

### Taxonomy, canonical examples and experimental scopes

scope: supported. Targets: GO:0097683.

GO only_in_taxon2864 and ENA Dinophyceaeclass support taxonomic restriction. VARIABLE is qualitative; no quantitative census established. Horn thecate qualifier and optional morphological features remain bounded.

### Quantities, timing and dimensions

quantity: supported. Targets: GO:0097683.

No size,stoichiometry or rate asserted; topological/morphological wording does not supply quantitative population frequency or universal horn/groove presence.

### Source tiers and exact read extents

evidence: supported. Targets: GO:0097683.

Current GO/ENA and authored expert morphology are authority evidence. Taylor1980, where cited, is complete native abstract/bibliographic corroboration only; publisher403 is validation context, not primary body support. No morphology figure pixels or uninspected paper body claimed.

### Image access and attribution

evidence: not_applicable. Targets: GO:0097683.

No maintained image; expert-page captions and text inspected, no dinoflagellate pixels or uninspected Taylor figures certified.

### Complete record and native inventory coverage

completeness: supported. Targets: GO:0097683.

Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation.No automatic optionalprotein,canonicalspecies,image,dimension or molecularmechanism requirement. Correct regional boundaries and uncertainty remain positively assessed.

### Historical rationale and prior observations

provenance: supported. Targets: GO:0097683.

Dated rationale/history and actual earlier source-access observations remain append-only. Current notes/prompts may be corrected or dated clarification appended. No neighboring/group issue resolution, false historical search claim, or rewriting original bundles.

### Frozen inputs and deterministic original pair

schema: supported. Targets: GO:0097683.

Native original validate/render0 and exact Markdown; 15 historical input occurrences match source. Current target unchanged. Original batch26 global gate scope is a valid historical execution origin, not current-head attestation.

### Whole-record structured-source applicability

evidence: not_applicable. Targets: GO:0097683.

Complete record makes morphology/topology claims and explicitly defers molecular constituents/mechanisms. Original prose physical-scope exclusion is legitimate; absent formal adapter row is not a defect. Catalogue also has no matchingDinophyceae, but actual morphology scope—not biological absence—establishes exclusion.

### Independent current scientific disposition

consistency: supported. Targets: GO:0097683.

Pass with limitations: exact morphology/topology positively supported; no confirmed record finding. Parent antapex definition issue is not duplicated because this target does not repeat the erroneous direction; no molecular/quantitative scope invented.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: cellstructuremech:cullin_e_ubiquitin_ligase_complex, GO:0034270, GO:0031910, GO:0042729, GO:0031431, GO:0043625, GO:1990125, GO:0097684, GO:0097687, GO:0097683.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Ground the seven named DASH subunit classes

minor / open / confirmed; issue key: dash-seven-exact-families.

Seven exact family entries are available: DUO1 IPR013960, DAM1 IPR013962, DAD1 IPR013958, DAD2 IPR013963, ASK1 IPR013964, SPC19 IPR013251, SPC34 IPR013966. Their reviewed examples independently carry these family xrefs, while current rows defer exact mappings.

### micro-F2: Capture the tested Spc34 formation requirement

minor / open / confirmed; issue key: dash-spc34-tested-association.

Current Spc34 row omits the directly inspected Janke2002 p182/Fig1B condition-specific physical-association/recovery result: after4h37C, spc34-3 Dad2-ProA purification yields only bait, while matched SPC34 recovers the reported DDD complex. The minor gap is this concrete association/stability evidence, not UNKNOWN alone or a universal viability/formation claim.

### micro-F3: Use the exact Dbf4 regulatory-subunit family

minor / open / confirmed; issue key: ddk-dbf4-exact-family.

The Dbf4 row remains REVIEWED_LABEL_ONLY even though IPR051590 directly identifies the DDK regulatory family and is linked to the correct reviewed example. Its generated description is not used as primary evidence. Cdc7 kinase-domain candidates remain broader.

### micro-F4: Ground DiaA with its verified exact family

minor / open / confirmed; issue key: diaa-exact-family.

The sole DiaA row remains REVIEWED_LABEL_ONLY despite exact family IPR023070 and the native P66817 xref. DiaA-specific integrated signatures distinguish it from broader GmhA/DiaA and SIS families.

### plaque-t1-F1: Distinguish the Ape1 cargo core from the Atg19-containing Cvt complex

major / open / confirmed; issue key: cvt-cargo-receptor-boundary.

The current active RESOLVED discussion excludes Atg19 with Atg11. Independently inspected Shintani S8/S10 explicitly distinguishes the Atg19-containing Cvt cargo-receptor complex from Ape1 cargo self-assembly and Atg11 delivery machinery; Scott native association/cotransport and fresh GO0032258/P14904 corroborate. The short GO0034270 definition is accurately copied but incomplete relative to these sources. Reconcile current constituent/graph boundaries while preserving historical rationale and not requiring every Atg factor as a constituent.

### plaque-t2-F1: Prior cytostome plasma-membrane hierarchy error is corrected

major / resolved / confirmed; issue key: cytostome-plasma-membrane-parthood.

The old frozen target incorrectly used GO0005886 as an is-a parent. Current source instead uses GO0110165 parent and GO0005886 part_of with corresponding evidence/history; fresh exact GO children/path confirms both typed relations.

Disposition: Resolved by the already-present current record correction associated with closed issue2461/PR2464, independently verified against current bytes and fresh GO. This successor records resolution of this one inherited target/finding only; it does not claim this PR performed the scientific edit or close all grouped historical findings.

### septin-cullin_e_ubiquitin_ligase_complex-F1: Replace the Skp1.2 example with the source-locus-matched protein

major / open / confirmed; issue key: cullin-e-skp1-2-wrong-accession.

The record explicitly identifies Skp1.2 as Tb927.9.8370 but gives UniProtKB:Q384S1, ORF Tb11.02.5340,212aa. Source Table1 and S3 specify Tb927.9.8370,158aa. Native Q38ED0 has historical ORF Tb09.211.0300 and the exact VEuPathDB Tb927.9.8370 cross-reference; independent Ensembl lookup also maps that locus to Q38ED0 and158aa. Correct Q383D5/Q38C61 mappings are retained. Their historical ORF names should not be called primary gene names. Fresh current authority and genuine primary/terminology sources independently confirm the inherited issue. Dated rationale/history must be preserved; current scientific fields or appended clarification are the correction surface.

### septin-dinoflagellate_antapex-F1: Correct the antapex definition’s anterior/posterior reversal

major / open / confirmed; issue key: dinoflagellate-antapex-anterior-posterior-definition.

The record defines the antapex as the anterior-most point of the hypocone, faithfully copying current GO0097684. Yet the same record’s sulcal-notch edge and GO0097618 place the antapex at the posterior end. The directly linked Tree of Life orientation note defines the antapex at the bottom of the hyposome and below-cingulum positions as posterior; the specialist INA orientation glossary agrees. The definition therefore mislocates the defining region even though its GO identifier, label and parthood are correct. The upstream GO discrepancy must be retained explicitly rather than treated as an invented or misquoted source. Fresh current authority and genuine primary/terminology sources independently confirm the inherited issue. Dated rationale/history must be preserved; current scientific fields or appended clarification are the correction surface.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, curate the seven verified exact family mappings and update current status/notes and the grounding portion of the TODO; retain the distinct open small-subunit boundary work.

- Verify exact family type/name and matching example xref; do not substitute general domains.
- Preserve source-specific taxa, supported component IDs and protein examples; pass applicable native curation checks.
- Preserve discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers, experimental host/condition and unknown formation scope explicit.

### micro-A2

In separately authorized record curation, add the exact Janke Dad2-ProA/spc34-3 versus matched SPC34 recovery assessment at37°C for4h, distinguishing physical association/stability from viability, direct binding and biorientation. Qualify any formation interpretation; global UNKNOWN may remain. Do not infer intracellular depletion of unrecovered partners, force universal ESSENTIAL or demand new experiments.

- Distinguish recovery/stability of the complete reported assembly from viability and direct binding.
- Do not generalize the mutant result to all subunits or all organisms.
- Preserve source-specific taxa, supported component IDs and protein examples; pass applicable native curation checks.
- Preserve discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers, experimental host/condition and unknown formation scope explicit.

### micro-A3

In separately authorized record curation, map the Dbf4 row to the verified exact family and narrow the remaining TODO to unresolved Cdc7 mapping; retain the correct examples and UNKNOWN formation necessity.

- Verify native family type/name/signature and the P32325 xref.
- Do not promote unchecked generated family prose to experimental mechanism evidence.
- Preserve source-specific taxa, supported component IDs and protein examples; pass applicable native curation checks.
- Preserve discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers, experimental host/condition and unknown formation scope explicit.

### micro-A4

In separately authorized record curation, use IPR023070 for the existing DiaA class and update current status/notes/TODO; preserve four-copy stoichiometry, correct example and the separation from DnaA/oriC.

- Confirm the exact family type/name and DiaA-specific signatures.
- Do not substitute broad GmhA/DiaA or SIS mappings.
- Preserve source-specific taxa, supported component IDs and protein examples; pass applicable native curation checks.
- Preserve discussions.rationale, posed_date and dated history; append provenance and update current notes/prompt only as supported.
- No record edits occur in this review PR. Keep primary body/abstract/authority tiers, experimental host/condition and unknown formation scope explicit.

### plaque-t1-A1

Reconcile the current Ape1-core versus Atg19-containing Cvt-complex boundary in definition, components and descriptive graph, retaining Atg11 as separately scoped trafficking machinery and Ams1 as source-scoped additional cargo. Reopen or qualify the active blanket exclusion with appended evidence; preserve dated rationale, posed_date and curation history.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Preserve the short GO definition as accurately sourced context while stating the primary-source boundary explicitly.
- Do not infer universal formation ESSENTIAL labels from PAS/transport phenotypes or force every pathway factor into the constituent list.
- Use the guarded record writer and append history only in separately authorized curation; this PR changes reviews only.

### septin-cullin_e_ubiquitin_ligase_complex-A1

Replace the Skp1.2 example with verified Q38ED0 and its actual native identity/status/taxon fields, documenting the paper-locus versus historical-ORF bridge. Retain Q383D5/Q38C61 with verified locus bridges and precise ORF wording. Reconcile stale example-related discussion text without treating family names as exact paralog identity. Record curation remains outside this review-only PR. Preserve all dated rationale/history, correcting current fields/notes or appending clarification.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Use separately authorized guarded record curation and append-only record/repository history; preserve exact source scope and do not silently misquote current GO or generated protein names.

### septin-dinoflagellate_antapex-A1

Correct the definition to the posterior tip/end of the hypocone. Cite the directly read orientation authority for that correction and explicitly record that current GO0097684 still contains the contradictory anterior wording; retain the GO identifier, correct hypocone parthood and posterior sulcal-notch relation, and preserve historical provenance. Do not silently present the corrected wording as an exact current GO quotation. Record curation remains outside this review-only PR. Preserve all dated rationale/history, correcting current fields/notes or appending clarification.

- Definition consistently identifies the posterior antapex, with the anterior apex kept separate.
- Definition source and nearest evidence explain the correction and upstream discrepancy.
- Native schema, strict, CURIE and graph checks pass as applicable.
- Use separately authorized guarded record curation and append-only record/repository history; preserve exact source scope and do not silently misquote current GO or generated protein names.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96; current SHA256 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/cvt_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902; current SHA256 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T052917Z-cvt-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/cytostome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e098724aea296245130198ea537eab00b38dd2429c7d91aeac78d09efab7d735; current SHA256 083f8800483f67a23bdb303aaf95d8d853d3bf67240e7ac2926e87ab66c89926. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261022T052918Z-cytostome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/dash_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 97116204b79a4211411541b5db8c6bba2c892906521c2b754fa796b516bdfa91; current SHA256 068456fa61be361559f04a3267867351f2adda6537a706aa6b152f62439f81fb. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261022T052919Z-dash-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/dbf4_dependent_protein_kinase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433; current SHA256 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/delta_dna_polymerase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf; current SHA256 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T052920Z-delta-dna-polymerase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/diaa_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158; current SHA256 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T052921Z-diaa-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/dinoflagellate_antapex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9; current SHA256 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T052921Z-dinoflagellate-antapex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/dinoflagellate_antapical_horn.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7; current SHA256 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T052922Z-dinoflagellate-antapical-horn-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/dinoflagellate_apex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749; current SHA256 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T052923Z-dinoflagellate-apex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/dash_complex.yaml; Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | Complete identity, hierarchy, seven/two/three/one-component inventories as appropriate, protein examples, taxonomy, functions, graph, historical discussions and curation events read. No maintained images or measured physical-property rows. |
| micro-prior-0 | reviews/structured/20261022T052919Z-dash-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original source/check/assessment/finding/action/limitation/notes content inspected; original body reads and old command results remain historical, not recertified merely by preservation. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/3-stale.diff; Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634 | supports | DASH adds seven constituent component_ref nodes/edges and dated history; other three assigned records have no content delta. New edges are independently reassessed below. |
| micro-record-1 | data/structures/other/dbf4_dependent_protein_kinase_complex.yaml; Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | Complete identity, hierarchy, seven/two/three/one-component inventories as appropriate, protein examples, taxonomy, functions, graph, historical discussions and curation events read. No maintained images or measured physical-property rows. |
| micro-prior-1 | reviews/structured/20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original source/check/assessment/finding/action/limitation/notes content inspected; original body reads and old command results remain historical, not recertified merely by preservation. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/4-stale.diff; Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634 | supports | DASH adds seven constituent component_ref nodes/edges and dated history; other three assigned records have no content delta. New edges are independently reassessed below. |
| micro-record-2 | data/structures/other/delta_dna_polymerase_complex.yaml; Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | Complete identity, hierarchy, seven/two/three/one-component inventories as appropriate, protein examples, taxonomy, functions, graph, historical discussions and curation events read. No maintained images or measured physical-property rows. |
| micro-prior-2 | reviews/structured/20261022T052920Z-delta-dna-polymerase-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original source/check/assessment/finding/action/limitation/notes content inspected; original body reads and old command results remain historical, not recertified merely by preservation. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/5-stale.diff; Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634 | supports | DASH adds seven constituent component_ref nodes/edges and dated history; other three assigned records have no content delta. New edges are independently reassessed below. |
| micro-record-3 | data/structures/other/diaa_complex.yaml; Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | Complete identity, hierarchy, seven/two/three/one-component inventories as appropriate, protein examples, taxonomy, functions, graph, historical discussions and curation events read. No maintained images or measured physical-property rows. |
| micro-prior-3 | reviews/structured/20261022T052921Z-diaa-complex-audit/review.yaml; Complete immutable original YAML and derived Markdown | supports | Original source/check/assessment/finding/action/limitation/notes content inspected; original body reads and old command results remain historical, not recertified merely by preservation. |
| micro-delta-3 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/6-stale.diff; Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634 | supports | DASH adds seven constituent component_ref nodes/edges and dated history; other three assigned records have no content delta. New edges are independently reassessed below. |
| micro-policy | docs/CURATION.md; Components exact class/family identities and formation essentiality; Discussions append-only rationale/posed_date | supports | Class grounding differs from taxon-specific example xrefs. Formation is not viability or function; UNKNOWN alone is not a defect. Preserve dated rationale/history; update current notes/prompt only when supported. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component role/grounding_status/essentiality, taxonomic presence, graph actors and scope | supports | Generic families/classes and nonmechanistic outlines are valid. Concrete exact-family or condition-specific association gaps are bounded minor findings, not compulsory optional fields or experiments. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and native profile/config/checklist | supports | Positive genes/proteins/pathways trigger applicability; no-expression wording alone is insufficient. Catalogue and gene/module searches must retain host and computational limits. Seventeen common inputs hash-identical to previously read bytes; current skill/profile/config/shared contract/checklist and component/discussion rules reread. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Component references and nonmechanistic assembly/function outlines | supports | Constituent contributions and coarse function edges do not require invented atomic interaction or reaction-order claims. Exact declared graph scopes remain binding. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/original-audit.json; Eight actual native validate/render commands;52 historical frozen inputs;8 immutable original artifacts | supports | All four original YAMLs validate and render byte-identical Markdown. Every historical input hash matches its recorded Git revision, and all eight original files match original PR commit. |
| micro-up-P06243 | https://rest.uniprot.org/uniprotkb/P06243.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P06243.raw | supports | P06243: UniProtKB reviewed (Swiss-Prot); Cell division control protein 7; primary genes ['CDC7']; loci ['YDL017W', 'D2855']; taxon 559292; InterPro ['IPR011009', 'IPR000719', 'IPR008271']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P15436 | https://rest.uniprot.org/uniprotkb/P15436.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P15436.raw | supports | P15436: UniProtKB reviewed (Swiss-Prot); DNA polymerase delta catalytic subunit; primary genes ['POL3']; loci ['YDL102W', 'D2366']; taxon 559292; InterPro ['IPR006172', 'IPR017964', 'IPR006133', 'IPR006134', 'IPR043502', 'IPR042087', 'IPR023211', 'IPR050240', 'IPR056435', 'IPR012337', 'IPR036397', 'IPR025687']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P32325 | https://rest.uniprot.org/uniprotkb/P32325.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P32325.raw | supports | P32325: UniProtKB reviewed (Swiss-Prot); DDK kinase regulatory subunit DBF4; primary genes ['DBF4']; loci ['YDR052C', 'D4205', 'YD9609.07C']; taxon 559292; InterPro ['IPR036420', 'IPR055116', 'IPR013939', 'IPR051590', 'IPR006572', 'IPR038545']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P35734 | https://rest.uniprot.org/uniprotkb/P35734.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P35734.raw | supports | P35734: UniProtKB reviewed (Swiss-Prot); DASH complex subunit ASK1; primary genes ['ASK1']; loci ['YKL052C', 'YKL306']; taxon 559292; InterPro ['IPR013964']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P36131 | https://rest.uniprot.org/uniprotkb/P36131.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P36131.raw | supports | P36131: UniProtKB reviewed (Swiss-Prot); DASH complex subunit SPC34; primary genes ['SPC34']; loci ['YKR037C']; taxon 559292; InterPro ['IPR013966']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P36162 | https://rest.uniprot.org/uniprotkb/P36162.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P36162.raw | supports | P36162: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DAD2; primary genes ['DAD2']; loci ['YKR083C', 'YKR403']; taxon 559292; InterPro ['IPR013963']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P46957 | https://rest.uniprot.org/uniprotkb/P46957.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P46957.raw | supports | P46957: UniProtKB reviewed (Swiss-Prot); DNA polymerase delta small subunit; primary genes ['POL31']; loci ['YJR006W', 'J1427', 'YJR83.7']; taxon 559292; InterPro ['IPR007185', 'IPR040663', 'IPR024826', 'IPR041863']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P47110 | https://rest.uniprot.org/uniprotkb/P47110.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P47110.raw | supports | P47110: UniProtKB reviewed (Swiss-Prot); DNA polymerase delta subunit 3; primary genes ['POL32']; loci ['YJR043C', 'J1626']; taxon 559292; InterPro []. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P53168 | https://rest.uniprot.org/uniprotkb/P53168.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P53168.raw | supports | P53168: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DUO1; primary genes ['DUO1']; loci ['YGL061C']; taxon 559292; InterPro ['IPR013960']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P53267 | https://rest.uniprot.org/uniprotkb/P53267.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P53267.raw | supports | P53267: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DAM1; primary genes ['DAM1']; loci ['YGR113W', 'G6153']; taxon 559292; InterPro ['IPR013962']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-P66817 | https://rest.uniprot.org/uniprotkb/P66817.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P66817.raw | supports | P66817: UniProtKB reviewed (Swiss-Prot); DnaA initiator-associating protein DiaA; primary genes ['diaA']; loci ['b3149', 'JW3118']; taxon 83333; InterPro ['IPR023070', 'IPR035461', 'IPR001347', 'IPR046348', 'IPR050099']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-Q03954 | https://rest.uniprot.org/uniprotkb/Q03954.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-Q03954.raw | supports | Q03954: UniProtKB reviewed (Swiss-Prot); DASH complex subunit SPC19; primary genes ['SPC19']; loci ['YDR201W']; taxon 559292; InterPro ['IPR013251']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-up-Q12248 | https://rest.uniprot.org/uniprotkb/Q12248.json; Native status/product/primary genes/synonyms/loci/taxon, complete location annotations/evidence codes and InterPro links; relevant subunit/function clauses, not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-Q12248.raw | supports | Q12248: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DAD1; primary genes ['DAD1']; loci ['YDR016C']; taxon 559292; InterPro ['IPR013958']. Reference annotations are distinguished from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike the experimental P15436/Huh join. |
| micro-query-ASK1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AASK1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-ASK1.raw | supports | Current bounded query returns 1 accession(s): ['P35734']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-CDC7 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACDC7+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-CDC7.raw | supports | Current bounded query returns 1 accession(s): ['P06243']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-DAD1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAD1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DAD1.raw | supports | Current bounded query returns 1 accession(s): ['Q12248']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-DAD2 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAD2+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DAD2.raw | supports | Current bounded query returns 1 accession(s): ['P36162']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-DAM1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAM1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DAM1.raw | supports | Current bounded query returns 1 accession(s): ['P53267']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-DBF4 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADBF4+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DBF4.raw | supports | Current bounded query returns 1 accession(s): ['P32325']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-DUO1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADUO1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DUO1.raw | supports | Current bounded query returns 1 accession(s): ['P53168']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-POL3 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL3+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-POL3.raw | supports | Current bounded query returns 1 accession(s): ['P15436']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-POL31 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL31+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-POL31.raw | supports | Current bounded query returns 1 accession(s): ['P46957']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-POL32 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL32+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-POL32.raw | supports | Current bounded query returns 1 accession(s): ['P47110']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-SPC19 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASPC19+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-SPC19.raw | supports | Current bounded query returns 1 accession(s): ['Q03954']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-SPC34 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASPC34+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-SPC34.raw | supports | Current bounded query returns 1 accession(s): ['P36131']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-query-diaA | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdiaA+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete exact reviewed gene/taxon result page and returned identities; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-diaA.raw | supports | Current bounded query returns 1 accession(s): ['P66817']. All13 exact queries return their intended singleton; this does not reconstruct a historical search or prove causal membership. |
| micro-tax-2759 | https://rest.uniprot.org/taxonomy/2759.json; Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-2759.raw | supports | 2759: Eukaryota, domain; parent {'scientificName': 'cellular organisms', 'taxonId': 131567}. Species examples, S288c/K12 protein references and experimental derivatives are not conflated. |
| micro-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-4932.raw | supports | 4932: Saccharomyces cerevisiae, species; parent {'scientificName': 'Saccharomyces', 'taxonId': 4930}. Species examples, S288c/K12 protein references and experimental derivatives are not conflated. |
| micro-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-559292.raw | supports | 559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c), strain; parent {'scientificName': 'Saccharomyces cerevisiae', 'commonName': "Baker's yeast", 'taxonId': 4932}. Species examples, S288c/K12 protein references and experimental derivatives are not conflated. |
| micro-tax-562 | https://rest.uniprot.org/taxonomy/562.json; Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-562.raw | supports | 562: Escherichia coli, species; parent {'scientificName': 'Escherichia', 'taxonId': 561}. Species examples, S288c/K12 protein references and experimental derivatives are not conflated. |
| micro-tax-83333 | https://rest.uniprot.org/taxonomy/83333.json; Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-83333.raw | supports | 83333: Escherichia coli (strain K12), strain; parent {'scientificName': 'Escherichia coli', 'taxonId': 562}. Species examples, S288c/K12 protein references and experimental derivatives are not conflated. |
| micro-go-0000776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0000776.raw | supports | [{"id": "GO:0000776", "name": "kinetochore", "isObsolete": false, "definition": {"text": "A multisubunit complex that is located at the centromeric region of DNA and provides an attachment point for the spindle microtubules."}, "comment": "Note that the kinetochore overlaps the centromeric DNA, but centromeric DNA is not part of the kinetochore.", "synonyms": [{"name": "condensed chromosome kinetochore", "type": "exact"}, {"name": "condensed nuclear chromosome kinetochore", "type": "exact"}, {"name": "NMS complex", "type": "narrow"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0000940 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000940; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0000940.raw | supports | [{"id": "GO:0000940", "name": "outer kinetochore", "isObsolete": false, "definition": {"text": "The region of a kinetochore most external to centromeric DNA; this outer region mediates kinetochore-microtubule interactions.", "xrefs": [{"dbCode": "PMID", "dbId": "11483983"}]}, "comment": null, "synonyms": [{"name": "condensed chromosome outer kinetochore", "type": "exact"}, {"name": "condensed nuclear chromosome outer kinetochore", "type": "exact"}, {"name": "outer kinetochore of condensed chromosome", "type": "exact"}, {"name": "outer kinetochore of condensed nuclear chromosome", "type": "exact"}, {"name": "outer kinetochore plate", "type": "narrow"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0006260 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0006260.raw | supports | [{"id": "GO:0006260", "name": "DNA replication", "isObsolete": false, "definition": {"text": "The cellular metabolic process in which a cell duplicates one or more molecules of DNA. DNA replication begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, and ends when the original DNA molecule has been completely duplicated and the copies topologically separated. The unit of replication usually corresponds to the genome of the cell, an organelle, or a virus. The template for replication can either be an existing DNA molecule or RNA."}, "comment": "DNA biosynthesis is only part of this process. See also the biological process terms 'DNA-dependent DNA replication ; GO:0006261' and 'RNA-dependent DNA replication ; GO:0006278'.", "synonyms": null}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0006270 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006270; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0006270.raw | supports | [{"id": "GO:0006270", "name": "DNA replication initiation", "isObsolete": false, "definition": {"text": "The process in which DNA-dependent DNA replication is started; it begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, followed by DNA unwinding.", "xrefs": [{"dbCode": "PMID", "dbId": "28209641"}]}, "comment": null, "synonyms": [{"name": "DNA-dependent DNA replication initiation", "type": "exact"}, {"name": "DNA endoreduplication initiation", "type": "narrow"}, {"name": "DNA re-replication initiation", "type": "narrow"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0008608 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008608; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0008608.raw | supports | [{"id": "GO:0008608", "name": "attachment of spindle microtubules to kinetochore", "isObsolete": false, "definition": {"text": "The process in which spindle microtubules become physically associated with the proteins making up the kinetochore complex.", "xrefs": [{"dbCode": "PMID", "dbId": "10322137"}]}, "comment": "This class covers all attachments of spindle microtubules to the kinetochore, including the many incorrect attachments which initially form and are later corrected to stable attachments with the correct orientation for segregation to proceed (sister chromatid biorientation).", "synonyms": [{"name": "amphotelic attachment", "type": "related"}, {"name": "attachment of spindle microtubules to chromosome", "type": "exact"}, {"name": "bipolar attachment", "type": "related"}, {"name": "kinetochore-microtubule attachment", "type": "exact"}, {"name": "kinetochore microtubule interaction", "type": "broad"}, {"name": "kinetochore-microtubule interaction", "type": "broad"}, {"name": "microtubule anchoring at kinetochore", "type": "exact"}, {"name": "microtubule and chromosome interaction", "type": "broad"}, {"name": "microtubule and kinetochore interaction", "type": "related"}, {"name": "microtubule capture", "type": "narrow"}, {"name": "spindle chromosome attachment", "type": "exact"}, {"name": "spindle-chromosome interaction", "type": "broad"}, {"name": "spindle kinetochore attachment", "type": "exact"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0031431 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031431; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0031431.raw | supports | [{"id": "GO:0031431", "name": "Dbf4-dependent protein kinase complex", "isObsolete": false, "definition": {"text": "A heterodimeric protein complex required for the activation of DNA replication origins; comprises a catalytic subunit and a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes identified in other species generally contain proteins related to the Saccharomyces proteins.", "xrefs": [{"dbCode": "PMID", "dbId": "12045100"}]}, "comment": null, "synonyms": [{"name": "Cdc7-Dbf4 complex", "type": "narrow"}, {"name": "DDK", "type": "exact"}, {"name": "Hsk1-Dfp1 kinase complex", "type": "narrow"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0032991 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0032991.raw | supports | [{"id": "GO:0032991", "name": "protein-containing complex", "isObsolete": false, "definition": {"text": "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together."}, "comment": "A protein complex in this context is meant as a stable set of interacting proteins which can be co-purified by an acceptable method, and where the complex has been shown to exist as an isolated, functional unit in vivo. Acceptable experimental methods include stringent protein purification followed by detection of protein interaction. The following methods should be considered non-acceptable: simple immunoprecipitation, pull-down experiments from cell extracts without further purification, colocalization and 2-hybrid screening. Interactions that should not be captured as protein complexes include: 1) enzyme/substrate, receptor/ligand or any similar transient interactions, unless these are a critical part of the complex assembly or are required e.g. for the receptor to be functional; 2) proteins associated in a pull-down/co-immunoprecipitation assay with no functional link or any evidence that this is a defined biological entity rather than a loose-affinity complex; 3) any complex where the only evidence is based on genetic interaction data; 4) partial complexes, where some subunits (e.g. transmembrane ones) cannot be expressed as recombinant proteins and are excluded from experiments (in this case, independent evidence is necessary to find out the composition of the full complex, if known). Interactions that may be captured as protein complexes include: 1) enzyme/substrate or receptor/ligand if the complex can only assemble and become functional in the presence of both classes of subunits; 2) complexes where one of the members has not been shown to be physically linked to the other(s), but is a homologue of, and has the same functionality as, a protein that has been experimentally demonstrated to form a complex with the other member(s); 3) complexes whose existence is accepted based on localization and pharmacological studies, but for which experimental evidence is not yet available for the complex as a whole.", "synonyms": [{"name": "macromolecular complex", "type": "exact"}, {"name": "macromolecule complex", "type": "exact"}, {"name": "protein complex", "type": "narrow"}, {"name": "protein containing complex", "type": "exact"}, {"name": "protein-protein complex", "type": "narrow"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0042575 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042575; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0042575.raw | supports | [{"id": "GO:0042575", "name": "DNA polymerase complex", "isObsolete": false, "definition": {"text": "A protein complex that possesses DNA polymerase activity and is involved in template directed synthesis of DNA.", "xrefs": [{"dbCode": "PMID", "dbId": "12045093"}]}, "comment": null, "synonyms": null}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0042729 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042729; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0042729.raw | supports | [{"id": "GO:0042729", "name": "DASH complex", "isObsolete": false, "definition": {"text": "A large protein complex, containing around 8-10 subunits in yeast, including Duo1p, Dam1p, Dad1p and Ask1p. The complex forms part of the outer kinetochore, associates with microtubules when the kinetochore attaches to the spindle, and plays a role in spindle attachment, chromosome segregation and spindle stability.", "xrefs": [{"dbCode": "PMID", "dbId": "11782438"}, {"dbCode": "PMID", "dbId": "11799062"}, {"dbCode": "PMID", "dbId": "15632076"}, {"dbCode": "PMID", "dbId": "15640796"}]}, "comment": "Note that this complex is conserved in fungi but has not been observed in metazoans.", "synonyms": [{"name": "condensed nuclear chromosome kinetochore-associated DASH complex", "type": "exact"}, {"name": "Dam1 complex", "type": "exact"}, {"name": "DDD complex", "type": "exact"}, {"name": "Duo1p-Dam1p-Dad1p complex", "type": "exact"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0043601 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043601; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0043601.raw | supports | [{"id": "GO:0043601", "name": "nuclear replisome", "isObsolete": false, "definition": {"text": "A multi-component enzymatic machine at the nuclear replication fork, which mediates DNA replication. Includes DNA primase, one or more DNA polymerases, DNA helicases, and other proteins."}, "comment": null, "synonyms": null}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0043625 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043625; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0043625.raw | supports | [{"id": "GO:0043625", "name": "delta DNA polymerase complex", "isObsolete": false, "definition": {"text": "A multimeric DNA polymerase enzyme complex which differs in composition amongst species; in humans it is a heterotetramer of four subunits of approximately 125, 50, 68 and 12kDa, while in S. cerevisiae, it has three different subunits which form a heterotrimer, and the active enzyme is a dimer of this heterotrimer. Functions in DNA replication, mismatch repair and excision repair.", "xrefs": [{"dbCode": "ISBN", "dbId": "0198547684"}, {"dbCode": "PMID", "dbId": "11205330"}, {"dbCode": "PMID", "dbId": "12403614"}]}, "comment": null, "synonyms": [{"name": "delta-DNA polymerase complex", "type": "exact"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-0140513 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140513; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0140513.raw | supports | [{"id": "GO:0140513", "name": "nuclear protein-containing complex", "isObsolete": false, "definition": {"text": "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together in the nucleus."}, "comment": null, "synonyms": [{"name": "nuclear complex", "type": "exact"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-1990102 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990102; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-1990102.raw | supports | [{"id": "GO:1990102", "name": "DnaA-DiaA complex", "isObsolete": false, "definition": {"text": "A protein-DNA complex containing a tetramer of DiaA attached to multiple DnaA molecule bound to oriC DNA. Regulates timely initiation of chromosomal replication during the cell cycle by stimulating assembly of DnaA-oriC complexes, conformational changes in ATP-DnaA initiation complexes, and unwinding of oriC duplex DNA.", "xrefs": [{"dbCode": "PMID", "dbId": "15326179"}, {"dbCode": "PMID", "dbId": "17699754"}]}, "comment": null, "synonyms": [{"name": "DnaA-DiaA-DNA complex", "type": "exact"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-go-1990125 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990125; Complete exact term identity/active status/definition/synonyms/comments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-1990125.raw | supports | [{"id": "GO:1990125", "name": "DiaA complex", "isObsolete": false, "definition": {"text": "A homotetrameric protein complex consisting of a symmetrical pair of DiaA homodimers. Facilitates DnaA binding to the origin of replication during replication initiation.", "xrefs": [{"dbCode": "PMID", "dbId": "17699754"}]}, "comment": null, "synonyms": [{"name": "DiaA homotetramer", "type": "exact"}]}]. GO identity is separate from primary source interpretation; Polδ retained dimeric GO wording is explicitly overridden by the inspected later primary abstract. |
| micro-ols-0043625 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0043625/graph; Complete native OLS typed graph nodes/edges; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ols-0043625.raw | supports | {"nodes": [{"iri": "http://purl.obolibrary.org/obo/GO_0043625", "label": "delta DNA polymerase complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_0042575", "label": "DNA polymerase complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_0140513", "label": "nuclear protein-containing complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_0043601", "label": "nuclear replisome"}, {"iri": "http://purl.obolibrary.org/obo/NCBITaxon_2759", "label": "Eukaryota"}], "edges": [{"source": "http://purl.obolibrary.org/obo/GO_0043625", "target": "http://purl.obolibrary.org/obo/GO_0042575", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/GO_0043625", "target": "http://purl.obolibrary.org/obo/GO_0140513", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/GO_0043625", "target": "http://purl.obolibrary.org/obo/GO_0043601", "uri": "http://purl.obolibrary.org/obo/BFO_0000050", "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/GO_0043625", "target": "http://purl.obolibrary.org/obo/NCBITaxon_2759", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}]}. is_a and part/has_part remain distinct. |
| micro-ols-1990102 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1990102/graph; Complete native OLS typed graph nodes/edges; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ols-1990102.raw | supports | {"nodes": [{"iri": "http://purl.obolibrary.org/obo/GO_1990102", "label": "DnaA-DiaA complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_1990077", "label": "primosome complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_1990101", "label": "DnaA-oriC complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_1990125", "label": "DiaA complex"}, {"iri": "http://purl.obolibrary.org/obo/NCBITaxon_Union_0000004", "label": "Prokaryota"}], "edges": [{"source": "http://purl.obolibrary.org/obo/GO_1990102", "target": "http://purl.obolibrary.org/obo/GO_1990077", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf", "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/GO_1990102", "target": "http://purl.obolibrary.org/obo/GO_1990101", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/GO_1990102", "target": "http://purl.obolibrary.org/obo/GO_1990125", "uri": "http://purl.obolibrary.org/obo/BFO_0000051", "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/GO_1990102", "target": "http://purl.obolibrary.org/obo/NCBITaxon_Union_0000004", "uri": "http://purl.obolibrary.org/obo/RO_0002162", "label": "in taxon"}]}. is_a and part/has_part remain distinct. |
| micro-ipr-IPR013960 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013960/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013960.raw | supports | IPR013960: {'name': 'DASH complex subunit Duo1', 'short': 'DASH_Duo1'}; type family; signatures {'panther': {'PTHR28216': 'DASH COMPLEX SUBUNIT DUO1'}, 'pfam': {'PF08651': 'DASH complex subunit Duo1'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR013962-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013962/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013962-retry.raw | supports | IPR013962: {'name': 'DASH complex subunit Dam1', 'short': 'DASH_Dam1'}; type family; signatures {'panther': {'PTHR28113': 'DASH COMPLEX SUBUNIT DAM1'}, 'pfam': {'PF08653': 'DASH complex subunit Dam1'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR013958 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013958/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013958.raw | supports | IPR013958: {'name': 'DASH complex subunit Dad1', 'short': 'DASH_Dad1'}; type family; signatures {'panther': {'PTHR28025': 'DASH COMPLEX SUBUNIT DAD1'}, 'pfam': {'PF08649': 'DASH complex subunit Dad1'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR013963-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013963/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013963-retry.raw | supports | IPR013963: {'name': 'DASH complex subunit Dad2', 'short': 'DASH_Dad2'}; type family; signatures {'panther': {'PTHR28036': 'DASH COMPLEX SUBUNIT DAD2'}, 'pfam': {'PF08654': 'DASH complex subunit Dad2'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR013964 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013964/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013964.raw | supports | IPR013964: {'name': 'DASH complex subunit Ask1', 'short': 'DASH_Ask1'}; type family; signatures {'panther': {'PTHR28200': 'DASH COMPLEX SUBUNIT ASK1'}, 'pfam': {'PF08655': 'DASH complex subunit Ask1'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR013251 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013251/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013251.raw | supports | IPR013251: {'name': 'DASH complex subunit Spc19', 'short': 'DASH_Spc19'}; type family; signatures {'panther': {'PTHR28262': 'DASH COMPLEX SUBUNIT SPC19'}, 'pfam': {'PF08287': 'Spc19'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR013966-retry2 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013966/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013966-retry2.raw | supports | IPR013966: {'name': 'DASH complex subunit Spc34', 'short': 'Spc34'}; type family; signatures {'pfam': {'PF08657': 'DASH complex subunit Spc34'}}. Exact DASH subunit family, corroborated by its maintained reviewed example xref. |
| micro-ipr-IPR051590 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051590/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR051590.raw | supports | IPR051590: {'name': 'DDK kinase regulatory subunit Dbf4', 'short': 'Dbf4'}; type family; signatures {'panther': {'PTHR15375': 'DNA Replication Regulatory Kinase Subunit'}}. Exact Dbf4 family/signature with P32325 xref; generated description is not used as experimental evidence. |
| micro-ipr-IPR013939 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013939/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013939.raw | context_only | IPR013939: {'name': 'Regulatory subunit Dfp1/Him1, central region', 'short': 'Regulatory_Dfp1/Him1'}; type domain; signatures {'pfam': {'PF08630': 'Dfp1/Him1, central region'}}. Dbf4 central-region domain, not an exact whole-protein family. |
| micro-ipr-IPR024826-retry2 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024826/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR024826-retry2.raw | context_only | IPR024826: {'name': 'DNA polymerase delta/II small subunit family', 'short': 'DNA_pol_delta/II_ssu'}; type family; signatures {'panther': {'PTHR10416': 'DNA POLYMERASE DELTA SUBUNIT 2'}}. Family explicitly spans eukaryotic Polδ and archaeal PolII small subunits; broader than the specifically named Pol31 class despite the P46957 xref. No new confirmed finding. |
| micro-ipr-IPR050240 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050240/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR050240.raw | context_only | IPR050240: {'name': 'DNA polymerase type-B', 'short': 'DNA_pol_type-B'}; type family; signatures {'panther': {'PTHR10322': 'DNA polymerase type-B'}}. Type-B polymerase family is broader than Pol3; generated biological prose not used. |
| micro-ipr-IPR019038-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019038/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR019038-retry.raw | context_only | IPR019038: {'name': 'DNA polymerase delta subunit 3', 'short': 'POLD3'}; type family; signatures {'pfam': {'PF09507': 'DNA polymerase subunit Cdc27'}, 'panther': {'PTHR17598': 'DNA POLYMERASE DELTA SUBUNIT 3'}}. Named POLD3/Cdc27 family is a candidate, but no current P47110 xref establishes the budding-yeast Pol32 assignment. No exhaustive absence claim. |
| micro-ipr-IPR023070-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023070/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR023070-retry.raw | supports | IPR023070: {'name': 'DnaA initiator-associating protein', 'short': 'DiaA'}; type family; signatures {'ncbifam': {'NF008138': 'DnaA initiator-associating protein DiaA'}, 'hamap': {'MF_01157': 'DnaA initiator-associating protein DiaA [diaA]'}}. Exact DiaA family with DiaA-specific HAMAP/NCBIfam signatures and P66817 xref. |
| micro-ipr-IPR035461 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035461/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR035461.raw | context_only | IPR035461: {'name': 'GmhA/DiaA', 'short': 'GmhA/DiaA'}; type family; signatures {'cdd': {'cd05006': 'SIS_GmhA'}}. Broader GmhA/DiaA grouping, not a substitute for the exact DiaA family. |
| micro-ipr-IPR050099-retry2 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050099/; Complete native name/type/hierarchy/integrated signatures and description scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR050099-retry2.raw | context_only | IPR050099: {'name': 'SIS family GmhA and DiaA subfamilies', 'short': 'SIS_GmhA/DiaA_subfam'}; type family; signatures {'panther': {'PTHR30390': 'SIS family GmhA and DiaA subfamilies'}}. Broader GmhA/DiaA grouping, not a substitute for the exact DiaA family. |
| micro-pmid-11568188 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11568188+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-11568188.raw | supports | 11568188: Structure of DNA polymerase delta from Saccharomyces cerevisiae.; DOI 10.1074/jbc.m108842200. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-11698664 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11698664+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-11698664.raw | supports | 11698664: Yeast Dam1p has a role at the kinetochore in assembly of the mitotic spindle.; DOI 10.1073/pnas.241417098. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-11782438 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11782438+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-11782438.raw | supports | 11782438: Four new subunits of the Dam1-Duo1 complex reveal novel functions in sister kinetochore biorientation.; DOI 10.1093/emboj/21.1.181. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-12045100 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12045100+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-12045100.raw | supports | 12045100: DNA replication in eukaryotic cells.; DOI 10.1146/annurev.biochem.71.110601.135425. Secondary review abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-14562095.raw | supports | 14562095: Global analysis of protein localization in budding yeast.; DOI 10.1038/nature02026. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-17699754 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17699754+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-17699754.raw | supports | 17699754: The interaction of DiaA and DnaA regulates the replication cycle in E. coli by directly promoting ATP DnaA-specific initiation complexes.; DOI 10.1101/gad.1561207. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-21256019 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21256019+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-21256019.raw | supports | 21256019: The Ndc80 loop region facilitates formation of kinetochore attachment to the dynamic microtubule plus end.; DOI 10.1016/j.cub.2010.12.050. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-25236177 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25236177+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-25236177.raw | supports | 25236177: Kinetochores require oligomerization of Dam1 complex to maintain microtubule attachments against tension and promote biorientation.; DOI 10.1038/ncomms5951. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-36701236 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36701236+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-36701236.raw | supports | 36701236: Single-copy locus proteomics of early- and late-firing DNA replication origins identifies a role of Ask1/DASH complex in replication timing control.; DOI 10.1016/j.celrep.2023.112045. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-9677405 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677405+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-9677405.raw | supports | 9677405: Characterization of the two small subunits of Saccharomyces cerevisiae DNA polymerase delta.; DOI 10.1074/jbc.273.31.19747. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-9677406 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677406+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-9677406.raw | supports | 9677406: Structure and processivity of two forms of Saccharomyces cerevisiae DNA polymerase delta.; DOI 10.1074/jbc.273.31.19756. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-pmid-9817759 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9817759+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete exact MED title/authors/year/DOI and full deposited abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-9817759.raw | supports | 9817759: Saccharomyces cerevisiae Duo1p and Dam1p, novel proteins involved in mitotic spindle function.; DOI 10.1083/jcb.143.4.1029. Primary-study abstract read completely. This metadata/abstract tier does not certify the full body, raw images or detailed experimental preparations. |
| micro-miranda2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb896%22&amp;format=json&amp;resultType=core&amp;pageSize=25; Exact DOI-selected MED metadata and complete primary abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/miranda2005-meta.raw | supports | 15640796: The yeast DASH complex forms closed rings on microtubules.. Recombinant ten-subunit E.coli expression and microtubule-associated rings/helices support bounded DASH assembly context; no raw EM inspected. |
| micro-li2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FMCB.25.2.767-778.2005%22&amp;format=json&amp;resultType=core; Exact DOI-selected MED metadata and complete primary abstract; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-meta.raw | supports | 15632076: Genetic analysis of the kinetochore DASH complex reveals an antagonistic relationship with the ras/protein kinase A pathway and a novel subunit required for Ask1 association.. Hsk2/Hsk3 microproteins and reduced Ask1-associated complex recovery in hsk3 mutants support the retained small-subunit boundary question. No new universal microprotein identity or current full-body read is claimed. |
| micro-cheeseman2001-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2199314.1/PMC2199314.1.xml; Genuine JATS Introduction; Results first composition/stoichiometry, phosphorylation, microtubule-binding, localization subsections; Discussion; Methods strains/TableII, purification, mass spectrometry, microscopy and binding assay; Figures1–3/6 text captions, no pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/cheeseman2001-jats.raw | supports | S288C-derived yeast purifications recover the seven declared proteins; approximate gel/biochemical stoichiometry and direct binding assay support the current constituent and outer-kinetochore outline. Unidentified small bands remain explicitly unresolved. Direct binding to bovine brain microtubules in vitro differs from native attachment and genetic-function inference. |
| micro-janke2002-publisherpdf | https://www.embopress.org/doi/pdf/10.1093/emboj/21.1.181; Genuine publisher PDF pp181–183 Introduction/first Results/Fig1 text caption; pp189–192 Discussion and TableI/Methods strain/purification sections. Extracted text, no figure pixels or supplementary experiments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-publisherpdf.raw | supports | Dad2-ProA purification after4h37C from spc34-3 recovers only the bait while matched SPC34 recovers the seven-protein DDD assembly (p182 Fig1B). This is condition-specific association/recovery evidence, not universal essentiality, direct binding or viability. Subunit/kinetochore findings substantively support the seven new DASH constituent edges; strain derivatives and conditional-mutant context remain scoped. |
| micro-keyamura-retained-reader | https://genesdev.cshlp.org/content/21/16/2083.full.pdf; Retained publisher-PDF web-reader text: lines0–44,257,290–296,323–347,370,373–379,417–446; only those supplied passages were reread. Reader reports older cached PDF; original network-fetch instant was not exposed/recorded. This timestamp is the current retained-text inspection, not fresh HTTP200. Terminal publisher routes returned403; later reader retry502.; retained /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-earlier-web-reader.json | context_only | Scoped cached text corroborates active tetramer, DnaA/oriC binding and dilution-dependent dimer/tetramer interpretation. Methods names K12 derivatives; computational dataset strains are not that experimental panel. Phosphosugar regulation is explicitly speculative. No pixels, coordinates, full body or missing passages certified. |
| micro-janke2002-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC125813.1/PMC125813.1.xml; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-jats.raw | context_only | HTTP404; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-janke2002-canonical-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC125813/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-canonical.raw | context_only | HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-janke2002-epxml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC125813/fullTextXML; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-epxml.raw | context_only | HTTP500; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-janke2002-bioc-access | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC125813/unicode; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-bioc.raw | context_only | HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-li2005-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC543429.1/PMC543429.1.xml; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-jats.raw | context_only | HTTP404; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-li2005-canonical-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC543429/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-canonical.raw | context_only | HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-li2005-epxml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC543429/fullTextXML; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-epxml.raw | context_only | HTTP500; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-li2005-bioc-access | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC543429/unicode; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-bioc.raw | context_only | HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC1948862.1/PMC1948862.1.xml; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-jats.raw | context_only | HTTP404; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-canonical-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC1948862/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-canonical.raw | context_only | HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-epxml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1948862/fullTextXML; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-epxml.raw | context_only | HTTP500; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-bioc-access | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC1948862/unicode; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-bioc.raw | context_only | HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-publisherpdf-access | https://genesdev.cshlp.org/content/21/16/2083.full.pdf; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-publisherpdf.raw | context_only | HTTP403; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-publisherhtml-access | https://genesdev.cshlp.org/content/21/16/2083.full; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-publisherhtml.raw | context_only | HTTP403; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-keyamura2007-pdf-query-access | https://genesdev.cshlp.org/content/21/16/2083.full.pdf?download=1; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-pdf-query.raw | context_only | HTTP403; absent S3 object, browser challenge, XML server error, BioC no-result or publisher403 as applicable. This response is not scientific body evidence; alternate genuine source reads are separately specified. |
| micro-historical-complex49-agent-bell2002-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev.biochem.71.110601.135425; Exact retained unsuccessful full-body access response | context_only | Publisher HTML returnedHTTP403; no Bell/Dutta body is certified. Native GO directly supports the maintained DDK definition and coarse function. Retained original timestamp/hash only; no new retrieval claimed. Original database kind is corrected to validation/context_only in this successor source report. |
| micro-historical-complex49-agent-burgers1998-pdf | https://www.jbc.org/article/S0021925818491673/pdf; Exact retained unsuccessful full-body access response | context_only | Publisher PDF route returnedHTTP403 rather than PDF. Only the complete native Burgers/Gerik abstract is certified here. Retained original timestamp/hash only; no new retrieval claimed. Original database kind is corrected to validation/context_only in this successor source report. |
| micro-historical-complex49-agent-johansson2001-doi | https://doi.org/10.1074/jbc.M108842200; Exact retained unsuccessful full-body access response | context_only | The DOI route failed TLS certificate verification with status0; no Johansson full body is certified. Its complete native abstract directly states the 1:1:1 monomer conclusion and the tested concentration range. Retained original timestamp/hash only; no new retrieval claimed. Original database kind is corrected to validation/context_only in this successor source report. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/catalogue.raw | supports | All20 organism rows inspected: no natural Saccharomyces/yeast match, while E.coli precise1k is available. Catalogue noncoverage does not refute biology; no bacterial proxy for yeast. |
| micro-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete e_coli/precise1k metadata; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ecoli-meta.raw | context_only | Five strains BW25113,DGF-298,GMOS,MG1655,W3110;1035 samples,201 modules,4257 genes. This selected K12-related dataset is not the Keyamura KH5402-1/NA/KA mutant panel and does not establish assembly. |
| micro-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete201 module-list metadata, names/regulators/functions; activity/generated narratives not assessed; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ecoli-modules.raw | context_only | Selected precise1k list contains201 entries; no title-only inference of DiaA regulation. Exact gene membership is separately evaluated. |
| micro-ecoli-gene-b3149 | https://imodulondb.org/api/genes/b3149/imodulons?organism=e_coli&amp;dataset=precise1k; All201 actual weight/threshold/in_imodulon rows for verified b3149/diaA; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ecoli-gene-b3149.raw | context_only | b3149 is returned but none of201 module flags is positive. Largest absolute weight is -0.037670615 for module112 versus threshold0.060574417; no matched module warrants a causal or assembly conclusion. This is bounded computational nonmembership, not gene absence or physiological dispensability. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z command receipt | context_only | Historical unavailable runner/exit1 permission limitation only; no new invocation claimed. Fresh official source API fallback is separately inspected. |
| micro-native-dash_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-verify-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0: 7 reviewed examples and 7 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-dash_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-causal-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-causal.log SHA256 35cc550c1a6115a14b841486e6313e1c723b4a77074deb16b03f416b463ef28f | supports | Actual exit0: 7 reviewed examples and 7 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-dbf4_dependent_protein_kinase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-verify-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0: 2 reviewed examples and 2 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-dbf4_dependent_protein_kinase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-causal-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-causal.log SHA256 69d4848530843f3d8b7c8651b0f217032da1f2bf11e09fa36969ee325d9ef6df | supports | Actual exit0: 2 reviewed examples and 2 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-delta_dna_polymerase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-verify-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0: 3 reviewed examples and 3 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-delta_dna_polymerase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-causal-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-causal.log SHA256 9d47952c8ac17bd446c4fab095faa0a2308bb3d31ccca4a3cc88179ae930d58e | supports | Actual exit0: 3 reviewed examples and 3 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-diaa_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-verify-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0: 1 reviewed examples and 1 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| micro-native-diaa_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-causal-receipt.json; Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-causal.log SHA256 5003812ac51deab9d43f38ec02f6deacaac1afb55770013f583b65a26c758057 | supports | Actual exit0: 1 reviewed examples and 1 COVERED typed nodes. Implemented accession/graph-example coverage is not full biological verification or exact family completeness. |
| plaque-current-1 | data/structures/other/cvt_complex.yaml; Entire current maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | Entire target read including definition, component/examples, taxon/functional scope, graph, discussions and append-only history. Unchanged original target bytes. |
| plaque-original-1-yaml | reviews/structured/20261022T052917Z-cvt-complex-audit/review.yaml; Complete historical pair and native deterministic-render comparison | supports | Original source scope, verdict, F1 and actions independently reassessed. Historical checks are not claimed as fresh executions. |
| plaque-original-1-md | reviews/structured/20261022T052917Z-cvt-complex-audit/review.md; Complete historical pair and native deterministic-render comparison | supports | Original source scope, verdict, F1 and actions independently reassessed. Historical checks are not claimed as fresh executions. |
| plaque-current-2 | data/structures/other/cytostome.yaml; Entire current maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | Entire target read including definition, component/examples, taxon/functional scope, graph, discussions and append-only history. Changed hierarchy/evidence/history substantively reassessed against fresh GO; other fields unchanged. |
| plaque-original-2-yaml | reviews/structured/20261022T052918Z-cytostome-audit/review.yaml; Complete historical pair and native deterministic-render comparison | supports | Original source scope, verdict, F1 and actions independently reassessed. Historical checks are not claimed as fresh executions. |
| plaque-original-2-md | reviews/structured/20261022T052918Z-cytostome-audit/review.md; Complete historical pair and native deterministic-render comparison | supports | Original source scope, verdict, F1 and actions independently reassessed. Historical checks are not claimed as fresh executions. |
| plaque-policy | docs/CURATION.md; Frozen native policy read and applied | supports | Exact classes, constituent versus machinery, formation versus function, optional fields and append-only rationale. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native policy read and applied | supports | Native parent is-a versus part_of, component/example and graph-type rules. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen native policy read and applied | supports | Positive molecular or pathway claims trigger bounded structured-source applicability assessment. |
| plaque-review-profile | docs/record-review-profile.md; Frozen native policy read and applied | supports | Issue-bearing and evidence-backed-disposition batch route; immutable originals. |
| plaque-review-schema | schema/record_review.yaml; Frozen native policy read and applied | supports | Native evidence kinds, assessment enums, exact predecessor and disposition requirements. |
| plaque-checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native policy read and applied | supports | Whole-record field-by-field claims, scope and completeness; no mandatory optional enrichment. |
| plaque-reservosome-context | data/structures/membrane_organelle/reservosome.yaml; Identifier/definition and cargo-receiving graph boundary; frozen before reading | context_only | Exact minted destination resolves to posterior membrane-bounded endocytic organelle receiving T.cruzi epimastigote cargo. Bounded dependency check only; no other reservosome findings or historical issue dispositions inferred. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034270,GO:0032991,GO:0005737,GO:0032258,GO:0033107,GO:0031910,GO:0110165,GO:0005886; All requested id/name/isObsolete/definition/synonym fields; exact relevant typed children, not every descendant; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/go.raw | supports | Eight active exact GO identities and definitions inspected. GO0031910 is a direct is_a child of GO0110165 and part_of child of GO0005886. GO0034270 short preApe1 definition is preserved as an authority scope conflict with GO0032258 explicit Atg19-containing Cvt complex definition, not alleged to be a misquotation. |
| plaque-cytostome-path | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031910/paths/GO:0005886; Complete exact endpoint path response; one path/one edge; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/cytostome-path.raw | supports | The exact returned path has one direct part_of edge from cytostome GO0031910 to plasma membrane GO0005886. |
| plaque-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; Complete requested taxon native identity and lineage; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/tax-4932.raw | supports | Exact taxon identity/name/rank/lineage verified; S.cerevisiae S288C is the accession reference strain, not silently the experimental SEY6210 background, and T.cruzi Y is the Chasen experimental strain. |
| plaque-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; Complete requested taxon native identity and lineage; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/tax-559292.raw | supports | Exact taxon identity/name/rank/lineage verified; S.cerevisiae S288C is the accession reference strain, not silently the experimental SEY6210 background, and T.cruzi Y is the Chasen experimental strain. |
| plaque-tax-5693 | https://rest.uniprot.org/taxonomy/5693.json; Complete requested taxon native identity and lineage; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/tax-5693.raw | supports | Exact taxon identity/name/rank/lineage verified; S.cerevisiae S288C is the accession reference strain, not silently the experimental SEY6210 background, and T.cruzi Y is the Chasen experimental strain. |
| plaque-protein-P14904 | https://rest.uniprot.org/uniprotkb/P14904.json; Full identity/genes/taxon/status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/PTM/SIMILARITY comments and evidence joins; sequence length and InterPro cross-references; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/protein-P14904.raw | supports | Reviewed P14904, APE1 primary symbol, API/LAP4/YSC1 aliases and YKL103C locus, 514aa precursor in strain559292 agree. FUNCTION and SUBUNIT independently distinguish precursor multimers, ATG19 binding/cargo-receptor complex and mature vacuolar enzyme. Exact three localization PMID joins are present. |
| plaque-gene-APE1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned exact gene-query rows; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/gene-APE1.raw | supports | Exact reviewed S288C APE1 query returns P14904 alone; identity does not itself prove Cvt membership. |
| plaque-ipr-IPR001948 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001948/; Complete metadata/name/type/hierarchy/curated description; compared to P14904 native xrefs; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/ipr-IPR001948.raw | supports | Peptidase M18 is a broad family encompassing aminopeptidases; it does not exactly denote the yeast precursor Cvt cargo subclass. Existing deferred exact grounding remains bounded, not a missing-family finding. |
| plaque-ipr-IPR023358 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023358/; Complete metadata/name/type/description/hierarchy; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/ipr-IPR023358.raw | supports | Peptidase M18 domain2 is a homologous superfamily/structural domain, not exact whole-protein precursor-cargo identity. |
| plaque-paper-0 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fs1097-2765%2801%2900263-5%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-0.raw | supports | Scott2001 primary abstract: Cvt19 binds precursor API, travels with it to vacuole, and is selectively required for Cvt cargo transport. |
| plaque-paper-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M404399200%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-1.raw | supports | Shintani2004 primary abstract explicitly defines the Ape1 plus Atg19 cargo-receptor Cvt complex and separates Atg11 PAS delivery; nutrient/vesicle scope is retained. |
| plaque-paper-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24493041+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-2.raw | supports | Matile1971 abstract supports a vacuolar aminopeptidase isozyme and growth-condition effects; not a specific Cvt-complex assembly assay. |
| plaque-paper-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A363165+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-3.raw | supports | Frey1978 abstract supports vacuolar aminopeptidaseI localization and distinguishes aminopeptidaseII; no Cvt receptor membership inferred. |
| plaque-paper-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8601598+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-4.raw | supports | Oda1996 abstract supports precursor propeptide-dependent vacuolar targeting and distinguishes transport defects from folding; body/scans not inspected. |
| plaque-paper-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1006%2Fexpr.1999.4419%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-5.raw | supports | Okuda1999 abstract supports T.cruzi epimastigote cytostome-associated flagellar/cytoskeletal region; broad complex and opening not equated. |
| plaque-paper-6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1078%2F0171-9335-00112%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-6.raw | supports | Porto-Carreiro2000 complete primary abstract supports protein-cargo cytostome/cytopharynx entry, vesicular-tubular intermediate network and later reservosome storage. Early-endosome interpretation is based on uptake kinetics and pH; no new detailed lipid assay certified. |
| plaque-paper-7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.135491%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-7.raw | supports | Alcantara2014 complete primary abstract explicitly identifies serial electron tomography/FIB-SEM and epimastigote complex reconstruction. No figure pixels or detailed Methods/strain beyond abstract certified. |
| plaque-paper-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.3389%2Ffcimb.2019.00445%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID matched complete MED identity/authors/year/title and indexed primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-8.raw | supports | Chasen2020 primary abstract identifies endogenous CP1 tagging and CP1-associated CP2/3 localization across the broader cytostome-cytopharynx complex; detailed body scope separately inspected. |
| plaque-scott2001-retained-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC2767243/; Results S6/S8 with Fig4/6 captions, Discussion S12/S14, Methods S18/Table1/S24/S25; independently reread retained genuine HTML /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/scott2001-pmc-prefixed.html; no pixels/supplements | supports | Native co-IP and heterologous binding support precursor-specific Cvt19 association and cotransport/degradation, unlike recycling receptors. SEY6210-derived experiments are distinguished from E.coli lysate/rabbit-reticulocyte binding, which is not a purified binary reconstitution. Actual retained retrieval was Nov3, not a fresh Nov4 body download. |
| plaque-shintani2004-retained-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC1712665/; Introduction S1; Methods S3/Table1; Results S8/S9 including Fig1-3 text captions; Discussion S10; independently reread retained genuine HTML /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/shintani2004-pmc-prefixed.html; no pixels/supplements | supports | Ape1 cargo core recruits Atg19 to form the Cvt complex; Ams1 is additional cargo, whereas Atg11 links cargo to PAS machinery. Nutrient-rich cargo/receptor deletion impairs PAS organization and vesicle transport, while starvation/rapamycin changes dependencies. This does not make every Atg factor a constituent. Actual retained retrieval was Nov3, not a fresh Nov4 body download. |
| plaque-chasen2020-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6978632.1/PMC6978632.1.xml; Genuine JATS Results s5/all four subsections with Fig1-4 text captions; Discussion s6; Methods Parasite Cultures, Generation of Cloning Constructs, Endocytosis Assays, Immunoelectron Microscopy, s3 co-IP/MS; no figure pixels/supplement reanalysis; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/chasen2020-s3.raw | supports | Y-strain CP1 endogenous tagging/immunoelectron localization and protein feeding support the broader endocytic complex. CP2/CP3 co-IP and overexpression localization do not establish an invariant three-subunit cytostome opening or deletion-based assembly necessity; predicted SMC/coiled-coil regions are not exact whole-protein families. Methods distinguish host-cell culture from parasite biological scope. |
| plaque-porto2000-doi | https://api.crossref.org/v1/works/10.1078%2F0171-9335-00112/transform; Complete bibliographic response, not primary full text; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/porto2000-doi.raw | context_only | Content negotiation returned Crossref bibliographic JSON, not article Results/Methods. It corroborates DOI identity only. |
| plaque-access-limitations | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/access-limitations.json; Actual attempted route receipts/body hashes; inspect response content, not HTTP200 alone | context_only | Fresh Scott/Shintani PMC routes were recaptcha, S3 guesses404, EPMC406; Scott BioC no-result HTML and Shintani BioC429. Chasen PMC challenge was replaced by genuine S3 JATS. Alcantara publisher403. Retained genuine Scott/Shintani bodies independently reread at original timestamps. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete same-PR fresh official /api/datasets catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/catalogue.raw | supports | All20 organism rows/28 organism-dataset pairs inspected: no Saccharomyces/S288C or Trypanosoma cruzi/Y biological host match; bacterial experimental protein-expression hosts are not proxies. |
| plaque-catalogue-search | https://imodulondb.org/api/datasets; Complete returned organism ID/name/dataset fields independently screened | context_only | Bounded lack of matched dataset coverage only; not negative biological evidence and no unrelated bacterial module query. |
| plaque-historical-adapter-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner command ['/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources', 'imodulondb', 'datasets']; original receipt only | context_only | Actual historical Nov3 00:49Z exit1 PermissionError reading pyvenv.cfg; not a fresh invocation or a successful adapter run. Current official source fallback is separately evidenced. |
| plaque-original-current-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/originals-current-proof.json; Two native original validate/render pairs;29 historical input occurrences and48 current source/worktree input hashes | supports | All original pairs validate and render byte-identically; historical hashes match exact source commits including symlink resolution. Cvt unchanged; cytostome stale hierarchy delta inspected rather than silently rehashed. |
| plaque-cytostome-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/cytostome-substantive-delta.diff; Exact historical frozen cytostome bytes versus current source; full diff | context_only | Only hierarchy change GO0005886 parent to part_of plus GO0110165 parent, corresponding evidence and historical curation event. Scientific geometry/uptake text otherwise unchanged. |
| plaque-issue2461-context | https://github.com/CultureBotAI/CellStructureMech/issues/2461; Root-fetched complete issue body/comments/current CLOSED state independently read from /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/existing-issue-2461.json | context_only | Already-closed grouped issue explicitly includes other-cytostome-plasma-membrane-parthood; resolution comment cites prior commit31fd33d9556ea5627b36d50ab608ccb9464f9353/PR2464. Only this matching cytostome finding is dispositioned; other group targets and verification bundle are not independently reassessed here. |
| plaque-native-cvt_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cvt_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source exit0. One REVIEWED P14904 example and one COVERED typed node. Identifier/coverage gates do not certify source-specific membership or necessity. |
| plaque-native-cvt_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cvt_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-causal.log SHA256 eb5b3bedce12a4c7f1373712d261d4b8605539a9f12256f743631fbe68f75567 | supports | Actual current-source exit0. One REVIEWED P14904 example and one COVERED typed node. Identifier/coverage gates do not certify source-specific membership or necessity. |
| plaque-native-cytostome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cytostome.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source exit0. Zero protein_examples and zero typed GENE_OR_PROTEIN nodes; empty-inventory pass is not molecular completeness evidence. Identifier/coverage gates do not certify source-specific membership or necessity. |
| plaque-native-cytostome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cytostome.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source exit0. Zero protein_examples and zero typed GENE_OR_PROTEIN nodes; empty-inventory pass is not molecular completeness evidence. Identifier/coverage gates do not certify source-specific membership or necessity. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Scientific review and structured-source applicability | supports | Actual whole-record molecular/pathway assertions require host/source coverage assessment; lack of expression-module claims is not sufficient exemption. |
| septin-curation-policy | docs/CURATION.md; Components and Discussions | supports | Exact family identity differs from complex-specific role. Family or class is permitted. Dated rationale/history are append-only; optional examples or broad groups alone do not establish defects. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component identity/essentiality and graph fields | supports | Formation essentiality is distinct from functional activity, localization or cellular viability. FUNCTION/NONMECHANISTIC graphs may describe coarse associations without a complete molecular assembly mechanism. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native accession/name/status/taxon and query rules | supports | Native primary genes versus ORF names and bounded query coverage are distinct from biological source membership, necessity and source-strain equivalence. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Evidence placement and descriptive graph scope | supports | Constituent relationships, perturbation outputs and co-isolation retain experiment scope; graph coverage alone does not establish molecular identity or direct ubiquitination. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Source access, image and read extents | supports | Native metadata/abstract, genuine body/captions, pixels and failed responses are separate tiers. Generated authority prose is excluded as independent biological evidence. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684,GO:0097687,GO:0097683,GO:0097614,GO:0097613,GO:0110165,GO:0097618,GO:0097612,GO:0097685,GO:0097686,GO:0031461; All11 requested identities/names/definitions/synonyms and relevant typed child relationships; not an exhaustive descendant audit | supports | Cullin-RING GO0031461 is a broader parent. Dinoflagellate0097684/87/83 denote antapex/horn/apex. GO0097684 still says anterior, conflicting with GO0097618 posterior antapex and GO0097614 posterior hypocone. Exact identifiers and typed topology remain valid; source transcription is not biological correctness. |
| septin-go-0097684-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684/history; Complete current native history response | supports | History independently distinguishes direct apex/antapex cellular-anatomical parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence census. Historical Bad taxon ID events are not current constraint identities. |
| septin-go-0097684-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684/constraints; Complete current native constraints response | supports | History independently distinguishes direct apex/antapex cellular-anatomical parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence census. Historical Bad taxon ID events are not current constraint identities. |
| septin-go-0097687-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/history; Complete current native history response | supports | History independently distinguishes direct apex/antapex cellular-anatomical parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence census. Historical Bad taxon ID events are not current constraint identities. |
| septin-go-0097687-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/constraints; Complete current native constraints response | supports | History independently distinguishes direct apex/antapex cellular-anatomical parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence census. Historical Bad taxon ID events are not current constraint identities. |
| septin-go-0097683-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097683/history; Complete current native history response | supports | History independently distinguishes direct apex/antapex cellular-anatomical parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence census. Historical Bad taxon ID events are not current constraint identities. |
| septin-go-0097683-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097683/constraints; Complete current native constraints response | supports | History independently distinguishes direct apex/antapex cellular-anatomical parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence census. Historical Bad taxon ID events are not current constraint identities. |
| septin-tol-orientation | https://tolweb.org/articles/?article_id=4756; Complete authored main text, embedded overview caption and About This Page authorship/license; no image pixels | supports | Mona Hoppenrath2008 directly identifies apex at top of episome and antapex at bottom of hyposome, with below-cingulum orientation posterior. Athecate/thecate terminology and possible apical groove are explicitly scoped. Expert morphological authority, not a molecular formation experiment. Text CC-BY-NC3.0 is distinct from per-image rights; no image reused. |
| septin-tol-dino | https://tolweb.org/Dinoflagellates/2445; Authorship block, Introduction and Characteristics through Flagella/Nucleus/Amphiesma/Vacuoles and Pusules; later sections not used | supports | GO-cited Hoppenrath/Saldarriaga branch page links the separate Cell Orientation note and describes varied motile morphologies. Whole-cell cellulose/protein content is not reassigned to a regional point. General whole-cell sizes, genomic statements and prevalence estimates are not imported into these records; no pixels inspected. |
| septin-ina-orientation | https://ina.tmsoc.org/terminology/calcispheres.htm; Complete Orientation section and adjacent calcisphere/cyst scope; remaining glossary read as context | supports | Orientation independently maps apex/anterior front and antapex/posterior rear. Cyst-oriented supplementary terminology is not treated as a universal motile-cell molecular mechanism or prevalence census. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete fresh official20-organism catalogue and all returned dataset keys, independently read from peer packet | supports | No Trypanosoma/TREU927/Lister427/2T1 or Dinophyceae/dinoflagellate dataset occurs in this finite response. Cullin-E positive molecular claims require this assessment, but no matching downstream gene/module query applies. Dinoflagellate records have genuine physical scope independent of noncoverage. Other listed taxa are not proxies; absence is not negative biology. Actual peer retrieval timestamp retained. |
| septin-tax-185431 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431; Complete native ENA taxId/name/rank/lineage/otherNames | supports | TREU927185431 is a strain/reference annotation, T.brucei5691 a species; neither identifies Lister427/2T1 experimental specimens. Dinophyceae2864 is a class with native dinoflagellate/Dinophyta/Dinoflagellata aliases; no population-frequency inference. |
| septin-tax-5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete native ENA taxId/name/rank/lineage/otherNames | supports | TREU927185431 is a strain/reference annotation, T.brucei5691 a species; neither identifies Lister427/2T1 experimental specimens. Dinophyceae2864 is a class with native dinoflagellate/Dinophyta/Dinoflagellata aliases; no population-frequency inference. |
| septin-tax-2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native ENA taxId/name/rank/lineage/otherNames | supports | TREU927185431 is a strain/reference annotation, T.brucei5691 a species; neither identifies Lister427/2T1 experimental specimens. Dinophyceae2864 is a class with native dinoflagellate/Dinophyta/Dinoflagellata aliases; no population-frequency inference. |
| septin-up-Q383D5 | https://rest.uniprot.org/uniprotkb/Q383D5.json; Complete accession/status/protein names with evidence codes,genes,organism,length,available function/subunit/location comments and VEuPathDB/InterPro xrefs | supports | 805aa, unreviewed Cullin1 putative; ORF Tb11.01.3260 and VEuPathDB Tb927.11.11430 agree with source scaffold. Native ORF names are not formal primary geneName fields. No sequence alignment or new experimental localization assay performed. |
| septin-up-Q38C61 | https://rest.uniprot.org/uniprotkb/Q38C61.json; Complete accession/status/protein names with evidence codes,genes,organism,length,available function/subunit/location comments and VEuPathDB/InterPro xrefs | supports | 106aa, unreviewed RING-type protein; ORF Tb10.70.6035 and VEuPathDB Tb927.10.1810 agree with source Rbx1. Native ORF names are not formal primary geneName fields. No sequence alignment or new experimental localization assay performed. |
| septin-up-Q384S1 | https://rest.uniprot.org/uniprotkb/Q384S1.json; Complete accession/status/protein names with evidence codes,genes,organism,length,available function/subunit/location comments and VEuPathDB/InterPro xrefs | supports | 212aa, unreviewed ORF Tb11.02.5340; no exact source Skp1.2 locus bridge. Generated SKP1/POZ name cannot establish membership. Native ORF names are not formal primary geneName fields. No sequence alignment or new experimental localization assay performed. |
| septin-up-Q38ED0 | https://rest.uniprot.org/uniprotkb/Q38ED0.json; Complete accession/status/protein names with evidence codes,genes,organism,length,available function/subunit/location comments and VEuPathDB/InterPro xrefs | supports | 158aa, unreviewed ORF Tb09.211.0300 and VEuPathDB Tb927.9.8370 agree exactly with source Skp1.2. Generated Elongin-C name is not independent biological evidence and does not invalidate the exact source-locus bridge. Native ORF names are not formal primary geneName fields. No sequence alignment or new experimental localization assay performed. |
| septin-ensembl-skp12 | https://rest.ensembl.org/lookup/id/Tb927.9.8370?expand=1;content-type=application/json; Complete exact gene/transcript/translation lookup | supports | Tb927.9.8370 is protein coding and independently maps to Q38ED0 with158aa translation; current assembly coordinate differences are not used to infer a different source protein. |
| septin-query-Tb927.11.11430 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb927.11.11430%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 0 entries. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-query-Tb927.10.1810 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb927.10.1810%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 0 entries. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-query-Tb927.9.8370 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb927.9.8370%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 0 entries. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-query-Tb11.01.3260 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb11.01.3260%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 1 entries Q383D5. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-query-Tb10.70.6035 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb10.70.6035%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 1 entries Q38C61. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-query-Tb11.02.5340 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb11.02.5340%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 1 entries Q384S1. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-query-Tb09.211.0300 | https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb09.211.0300%29&amp;format=json&amp;size=100; Complete returned page and accession/status/name/ORF/taxon identities | supports | Current exact gene/taxon search returns 1 entries Q38ED0. Empty current-locus searches do not negate the protein; historical ORF identifiers and authority xrefs provide the verified bridge. This does not reconstruct an October search. |
| septin-ipr-045093 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045093/; Native accession/name/type/description flags and complete description; no inferred exact-paralog mapping | supports | Cullin broad family does not distinguish the divergent E paralog. Family/class components are permitted; broad identity or absent optional exact grounding alone is not a new defect. |
| septin-ipr-051031 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051031/; Native accession/name/type/description flags and complete description; no inferred exact-paralog mapping | supports | RING-box family is broader than exact source Rbx1; llm=true/checked=false functional prose is excluded from biological support. Family/class components are permitted; broad identity or absent optional exact grounding alone is not a new defect. |
| septin-ipr-001232 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001232/; Native accession/name/type/description flags and complete description; no inferred exact-paralog mapping | supports | SKP1-like includes SKP1 and Elongin-C; broad family does not distinguish source Skp1.2 from other paralogs. Family/class components are permitted; broad identity or absent optional exact grounding alone is not a new defect. |
| septin-ipr-016897 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016897/; Native accession/name/type/description flags and complete description; no inferred exact-paralog mapping | supports | SKP1 family description restricts background examples to yeast/animals/plants, not exact source Skp1.2. Family/class components are permitted; broad identity or absent optional exact grounding alone is not a new defect. |
| septin-pmid-41413177 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A41413177+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique native MED identity/authors/title/year/DOI/PMCID and complete abstract | supports | Exact bibliographic identity resolves. Primary paper abstract/metadata; genuine full-body read extents are separately recorded. |
| septin-pmid-28052114 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28052114+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique native MED identity/authors/title/year/DOI/PMCID and complete abstract | supports | Exact bibliographic identity resolves. Primary paper abstract/metadata; genuine full-body read extents are separately recorded. |
| septin-pmid-7002229 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7002229+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique native MED identity/authors/title/year/DOI/PMCID and complete abstract | supports | Exact bibliographic identity resolves. Taylor1980 is a secondary evolutionary review, read only at complete abstract/metadata; not independent primary evidence for exact horn/apex anatomy or a molecular mechanism. |
| septin-PMC12816148-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12816148/fullTextXML; Genuine JATS front/permissions, completeTable1,ResultsSec4/5/6/9,DiscussionSec10,MethodsSec12/13/15/17/18/19/21; captionsFig2/6/7/8 | supports | Table1 and S3 define Cul-E Tb927.11.11430,Rbx1 Tb927.10.1810,Skp1.2 Tb927.9.8370,four kelch loci. Co-enrichment does not establish simultaneous occupancy, stoichiometry, direct recognition or obligatory formation. RNAi1K2N/Golgi/24hLFQ readouts remain separate from direct substrate claims. Isolation PCF Lister427, incompletely restated RNAi stage,2T1qPCR and927database are distinct; Methods seven WTcontrols versus PRIDE six remains unresolved. Discussion olderPLK→CulE attribution conflicts with Hu source locus and is not imported. Figure8 is a generic humanCullin1-based scheme; CC-BY4.0 license verified. |
| septin-PMC5241021-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5241021/fullTextXML; Genuine JATS front, completeResultssec004 and embeddedFig2/3 captions; Methodssec011/015/016; no pixels/supplements in this pass | supports | Hu2017 maps source WDR1 Tb927.10.15080 with TbCUL4 Tb927.3.1290 and DDB1 Tb927.6.5110. TbCUL1 Tb927.11.11430 did not co-precipitate WDR1 in the specified assay. This establishes a cross-paper attribution conflict, not universal disproof of any future CulE/PLK relationship. 29-13 RNAi and Lister427 tagging/co-IP are not TREU927 specimens; in-vitro fragment/lysate and co-IP scopes preserved. |
| septin-cullin-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12816148.1/41598_2025_32077_MOESM3_ESM.xlsx; Genuine XLSX Legend all nonempty rows; complete CULE headerA–AZ and columnsA–Z of rows2,3,4,5,7,9,10 only | supports | Seven source-defined bait/Skp1.2/Rbx1/kelch rows carry both significance flags. Row3 is Tb927.9.8370,158aa; rows2/7 are805/106aa. HeaderWT1–7 independently verifies seven controls. No full-workbook statistics, raw spectra, quantitative replication or irrelevant database-annotation inference. |
| septin-pride | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD042022; Complete accession/title/project description,sample/data protocols,submission type,organism and publication fields | supports | PXD042022 PARTIAL submission links PMID41413177/DOI10.1038/s41598-025-32077-9 and Tbrucei5691. Native sample protocol says six WTcontrols; paper/S3 seven. CulE12/24hLFQ and CulA SILAC are distinct. Landing-page metadata/protocol inspected, no raw spectra or bulk download analysis. |
| septin-fig2 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2663/12816148/60c8f8921df5/41598_2025_32077_Fig2_HTML.jpg; Actual fresh image viewed with view_image; entire pixels and corresponding full JATS caption inspected | supports | Actual complete pixels A–E; panelB shows CulE,Rbx1,Skp1.2,four kelch associations above depicted cutoff; not copy numbers/direct contacts. Publisher/PMC media under article CC-BY4.0; no maintained image is added or redistributed, no new physical-dimension measurement. |
| septin-fig6 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2663/12816148/55fe1026949a/41598_2025_32077_Fig6_HTML.jpg; Actual fresh image viewed with view_image; entire pixels and corresponding full JATS caption inspected | supports | Actual complete pixels A–D;0/12/24/36h pie plots have increased1K2N fraction and representative GRASP/MitoTracker images; no population-frequency calculation or localization of CulE itself. Publisher/PMC media under article CC-BY4.0; no maintained image is added or redistributed, no new physical-dimension measurement. |
| septin-fig7 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2663/12816148/748152b87b25/41598_2025_32077_Fig7_HTML.jpg; Actual fresh image viewed with view_image; entire pixels and corresponding full JATS caption inspected | supports | Actual complete pixels show24h statistical-difference plot: CulE and point8 decreased,point7 increased. Caption maps point8Tb927.10.8810/point7KKT9; duplicate point2/3Tb927.1.4900 attribution remains excluded from graph. Publisher/PMC media under article CC-BY4.0; no maintained image is added or redistributed, no new physical-dimension measurement. |
| septin-taylor-publisher | https://www.sciencedirect.com/science/article/pii/0303264780900064; Exact fresh ScienceDirect HTTP403 response; no article body inspected | context_only | Failed current access is context only. Original October403 is separately dated historical provenance. Neither provides primary source body evidence; target already limits Taylor to bibliography. |
| septin-source-packet | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-septin/source-receipts.json; Actual fresh HTTP URLs/status/types/timestamps/byte hashes | context_only | Only genuine JATS/workbook/authority data and viewed images support declared scientific scope; Taylor403 is not body access. Scratch text-extraction first attempt lacked bs4; corrected stdlib parser succeeded, not a repository/scientific test failure. |
| septin-shared-catalogue-packet | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-septin/shared-receipts.json; Actual peer catalogue fetch receipt independently hash checked and reread | context_only | Catalogue source timestamp retained; no new adapter invocation claimed. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907Z–00:49:00.863225Z; exit1 PermissionError reading pyvenv.cfg | context_only | Historical unavailable runner only; no fresh execution. Current official catalogue and native/primary source fallback are independently inspected. |
| septin-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-septin/original-checks.json; Four actual native validate/render executions and59 historical input occurrences | supports | All original native validations/renders exit0 and exact paired Markdown; all historical source hashes match, all four target hashes unchanged. Historical batch26 execution explicitly scoped in originalchecks is valid reuse, not a mislabeled batch49 run. |
| septin-record-cullin_e_ubiquitin_ligase_complex | data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml; Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,datasets,graphs,discussions/history read. Target nonstale. |
| septin-original-cullin_e_ubiquitin_ligase_complex | reviews/structured/20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Original batch26 execution origin and dated observations retained. |
| septin-native-cullin_e_ubiquitin_ligase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Three unreviewed example occurrences/three distinct accessions and one native COVERED Cullin-E node. Native pass does not establish the disputed Skp1.2 biological assignment. |
| septin-native-cullin_e_ubiquitin_ligase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml --causal-graphs; logSHA256 541d8ce82ac8de035386b41bcda3588ae6f68e6299387757256e00060caf6729 | supports | Exit0. Three unreviewed example occurrences/three distinct accessions and one native COVERED Cullin-E node. Native pass does not establish the disputed Skp1.2 biological assignment. |
| septin-record-dinoflagellate_antapex | data/structures/other/dinoflagellate_antapex.yaml; Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,datasets,graphs,discussions/history read. Target nonstale. |
| septin-original-dinoflagellate_antapex | reviews/structured/20261022T052921Z-dinoflagellate-antapex-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Original batch26 execution origin and dated observations retained. |
| septin-native-dinoflagellate_antapex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapex.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation. |
| septin-native-dinoflagellate_antapex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapex.yaml --causal-graphs; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation. |
| septin-record-dinoflagellate_antapical_horn | data/structures/other/dinoflagellate_antapical_horn.yaml; Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,datasets,graphs,discussions/history read. Target nonstale. |
| septin-original-dinoflagellate_antapical_horn | reviews/structured/20261022T052922Z-dinoflagellate-antapical-horn-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Original batch26 execution origin and dated observations retained. |
| septin-native-dinoflagellate_antapical_horn-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation. |
| septin-native-dinoflagellate_antapical_horn-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml --causal-graphs; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation. |
| septin-record-dinoflagellate_apex | data/structures/other/dinoflagellate_apex.yaml; Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,datasets,graphs,discussions/history read. Target nonstale. |
| septin-original-dinoflagellate_apex | reviews/structured/20261022T052923Z-dinoflagellate-apex-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Original batch26 execution origin and dated observations retained. |
| septin-native-dinoflagellate_apex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apex.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation. |
| septin-native-dinoflagellate_apex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apex.yaml --causal-graphs; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native checks cover this empty molecular inventory, not unasserted localization/formation. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2386 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-cullin_e_ubiquitin_ligase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cullin_e_ubiquitin_ligase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cvt_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cvt_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cytostome-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cytostome-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dash_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dash_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dbf4_dependent_protein_kinase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dbf4_dependent_protein_kinase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-delta_dna_polymerase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-delta_dna_polymerase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-diaa_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-diaa_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_antapex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_antapex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_antapical_horn-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_antapical_horn-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_apex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dinoflagellate_apex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- DASH, DDK, delta DNA polymerase and DiaA independent review: Only DASH, DDK, Polδ and DiaA are scientifically judged here; other cohort targets and newly frozen reservosome context are not read/disposed by this slice. No neighboring/category/group historical issue is terminally resolved.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Cheeseman genuine JATS and Janke genuine publisher PDF are body-read only at declared sections/tables/text captions. No figure pixels, raw gels/EM, sequence alignment, supplementary experiments or complete mechanistic reanalysis; new DASH constituent edges are not atomic interaction claims.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Li2005 and Miranda2005 current access is complete primary abstract only; Li current body routes failed, and the original older body reading remains historical. The small-subunit inventory remains an acknowledged bounded question; no unverified Hsk/Dad alias or compulsory optional component is invented.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Bell-Dutta2002 is a secondary-review abstract only; current DDK coarse definition/function also rests on exact GO/native authorities. Gerik/Burgers1998 and Johansson2001 are complete primary abstracts only. Historical403/TLS failures are retained with corrected kinds, not recertified body reads.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Keyamura current primary abstract was freshly fetched; retained publisher PDF web-reader text was independently reread only at explicit delivered line spans. Its exact original network fetch instant was not exposed/recorded, so evidence time is the current retained-text inspection and explicitly not freshHTTP200. Cached source version is older; Terminal routes returned403 and later reader retries502. No complete-body/pixel/coordinate claim.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Native protein identity/location annotations and linked abstracts do not certify all cited full primary studies. Pol31/Pol32 nuclear annotations are by similarity; no fabricated experimental localization joins. Generated InterPro descriptions are not primary biological evidence. Exact current singleton gene queries do not reconstruct old query uniqueness.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Broader Pol31/Pol3 families and unverified Pol32 candidate assignment remain uncertainty; no new false-positive mapping issue or exhaustive family-absence assertion. Formation UNKNOWN alone is not a curation defect. Spc34 finding is restricted to the directly inspected conditional recovery assay.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Fresh catalogue lacks natural yeast hosts in complete returned20 rows. DiaA precise1k spans five strains; b3149 is present but not above threshold in any201 returned modules. This is not absence, dispensability, physical assembly, localization or causal regulation evidence, and not an exact Keyamura mutant-panel match. No positive module hit exists to summarize as evidence.
- DASH, DDK, delta DNA polymerase and DiaA independent review: Historical runner unavailable/exit1 is explicitly dated2026-11-03T00:49:00Z, not a fresh invocation. Eight current own native protein receipts are actual source-head commands. Root owns globalQC/final saved-head checks/CI/queue; no pending stage is certified here.
- DASH, DDK, delta DNA polymerase and DiaA independent review: All records, original reviews, Git state and GitHub remain untouched. Four inherited minor findings propose later bounded record curation; stale/applicability/type bundle defects require linked immutable successor corrections only.
- Cvt and cytostome independent review: Scott2001/Shintani2004 genuine retained bodies were independently reread with their actual2026-11-03T11:52:44.702094Z/11:52:44.427793Z retrieval timestamps; fresh Nov4 PMC/S3/BioC/EPMC routes were challenge/error/no-result and are not body evidence. Fresh Chasen2020 S3 JATS was read at the exact stated sections.
- Cvt and cytostome independent review: Matile1971,Frey1978,Oda1996,Okuda1999,Porto-Carreiro2000 and Alcantara2014 remain complete indexed-primary-abstract/metadata tiers. Alcantara publisher403 and Porto DOI bibliographic JSON do not certify full Methods or figure data. Detailed lipid-specific Porto assays, exact tomography images and all experimental strains beyond the declared body scopes are not certified.
- Cvt and cytostome independent review: No maintained images or physical-property measurements in these two targets; no external figure pixels, movie/supplement content or raw-data reanalysis certified. Read text captions are not pixel inspection.
- Cvt and cytostome independent review: Cvt natural yeast scope is distinct from S288C reference accession, SEY6210-derived experimental cultures and recombinant bacterial/rabbit assays. T.cruzi Y parasite scope is distinct from human host-cell culture. No foreign-host expression module proxy used.
- Cvt and cytostome independent review: Current official catalogue lacks biological yeast/T.cruzi coverage; this is no claim that pathways or proteins are biologically absent. No fresh adapter-runner execution claimed; retained Nov3 00:49Z PermissionError remains historical.
- Cvt and cytostome independent review: Two original pairs/29 historical input occurrences and all48 current source/worktree hashes verified. Cvt unchanged; cytostome hierarchy delta substantively refreshed. Root global QC/final saved-head/CI/queue are separately owned and not precertified.
- Cvt and cytostome independent review: One inherited major Cvt boundary finding remains open; one inherited major cytostome hierarchy finding is resolved from preexisting curation. No new scientific finding or terminal resolution of other2461 records/category observations. Broad M18/domain mappings and optional molecular inventories are not forced.
- Cullin-E and three dinoflagellate morphology records independent review: All four current targets unchanged from original frozen inputs; two inherited confirmed major findings remain open: wrong Skp1.2 accession and antapex direction reversal. Horn/apex retain qualified positive support; no new scientific finding or unrelated issue disposition.
- Cullin-E and three dinoflagellate morphology records independent review: Cullin-E has3unreviewed examples and1nativeCOVERED scaffold node; other3 have0examples/0typedprotein nodes. Native verification does not establish biological membership of disputedSkp1.2, formation necessity or specimen identity.
- Cullin-E and three dinoflagellate morphology records independent review: 2025 genuine JATS read at front/permissions,Table1,Sec4/5/6/9/10/12/13/15/17/18/19/21 andFig2/6/7/8captions. ActualFig2allpanels,Fig6A–D andFig7pixels inspected. S3Legend,completeCULEheaderA–AZ and rows2/3/4/5/7/9/10columnsA–Z inspected; no raw spectra,whole-workbook statistical reanalysis or physicaldimension measurement. Figures are external scratch sources, none maintained or redistributed.
- Cullin-E and three dinoflagellate morphology records independent review: Hu2017 current genuine JATS read at front,Resultssec004 with embeddedFig2/3captions,Methodssec011/015/016 only; no currentHu figurepixels/supplements or universalCulE/PLK absence claim. Older sourceTbCUL4locus3.1290 differs fromCulE11.11430;2025Discussion conflict remains explicit.
- Cullin-E and three dinoflagellate morphology records independent review: PCF Lister427 isolation,2T1qPCR,Fig6bloodstream schematic and RNAi stage not uniformly restated are not collapsed. TREU927 reference proteins/database are not culturedstrain. PRIDE sixWTcontrols versus paper/S3 seven preserved; distinct endpoints and duplicateFig7locus remain scoped.
- Cullin-E and three dinoflagellate morphology records independent review: UniProtQ38ED0 Elongin-C andQ384S1 SKP1/POZ generated names are not independent mechanistic evidence. Exact VEuPathDB/Ensembl/source length and locus mapping support the identity correction. Current-locus gene query misses are bounded alias-index limitations, not protein absence. IPR051031 unchecked LLM functional prose excluded.
- Cullin-E and three dinoflagellate morphology records independent review: Dinoflagellate support is GO/ENA and authored expert terminology, not new primary formation experiments. GO0097684 still retains anterior error; correct posterior wording must be independently cited, not represented as exact currentGOquotation. Only_in_taxon and VARIABLE do not establish prevalence. No generic whole-cell materials reassigned to regional points.
- Cullin-E and three dinoflagellate morphology records independent review: Taylor1980 current access is complete native abstract/metadata only; fresh publisher403 is validation context. Two original publisher403 rows were typed database but explicitly context_only/failed; correction is kind-only. OriginalOctoberaccess dates remain historical. NoTaylorbody or dinoflagellate image pixels inspected.
- Cullin-E and three dinoflagellate morphology records independent review: One own historical expression-only adapter exclusion needs correction; three morphology exclusions are genuinely applicable. Fresh official complete catalogue contains no matchingTrypanosoma orDinophyceae dataset. No unrelated-host downstream proxy or biologicalabsence inference; runner unavailable receipt remains Nov3 00:49Z with no fresh invocation.
- Cullin-E and three dinoflagellate morphology records independent review: All59 original input occurrences and4original deterministic pairs verified. Valid historical batch26 gate execution reused across originalbatch49 remains explicit. Scratch parser dependency error was corrected without changing repo; parent global/postsave/finalCI/queue/merge/deletion are separate attestations.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- This explicit ten-record successor preserves all original review observations and exact predecessor findings. Scientific record curation stays outside this PR. Bundle issues #2902, #2903 and #2904 cover the stale inputs, seven formal applicability exclusions and five failed-access kind occurrences, respectively.
- Two target hashes changed: cytostome hierarchy/parthood/evidence/history and seven DASH constituent nodes/edges. Cytostome F1 is resolved from existing record bytes and linked to already-closed #2461; this PR neither performed that record correction nor resolves the other records in the grouped issue. DASH current graph membership is distinguished from exact family grounding and condition-specific association evidence.
- The complete native protein inventory is 17 represented examples and 15 typed GENE_OR_PROTEIN nodes, all classified COVERED by the actual native commands. An accession/coverage pass does not establish a disputed source-locus assignment or formation necessity. Empty inventories in morphology records are not automatic defects.
- Fresh, retained and unavailable source observations keep their actual access dates and inspection scopes. Failed responses are validation/context_only; the five old rows already disclosed their failure and are not alleged to have falsely claimed article-body access. Current citations distinguish indexed abstracts, actually inspected genuine bodies, expert authorities, figure text and actual external pixels.
- Preserve the current GO antapex wording as an explicitly documented upstream discrepancy while requesting a separately sourced posterior correction. For Cvt, distinguish Ape1 cargo self-assembly, Atg19-containing complex and Atg11 delivery machinery, preserving dated rationale with appended clarification. DASH Spc34 evidence is restricted to spc34-3, 37 C for four hours, Dad2-ProA recovery and its matched control; global UNKNOWN may remain, with no universal ESSENTIAL, partner-depletion or new-assay requirement.
- Full local QC, all 20 focused schema/strict checks and all 20 native protein checks passed before saving. Final trusted-base post-save review-check, saved-head independent acceptance, final-head CI and merge-group CI remain subsequent gates. Existing #2514 retains the native bulk-PMID reporting limitation; bounded supplemental native requests verified all 909 affected PMIDs without changing the original report or cache.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T050305Z-pr2386-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2386: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T04:47:59.512379Z'
finished_at: '2026-11-04T05:03:05Z'
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
summary: 'Current-input successor for all ten PR2386 records. Cytostome and DASH were
  stale and substantively refreshed: the former hierarchy finding is resolved by prior
  curation tracked in closed #2461, while the latter new constituent edges do not
  resolve its grounding or bounded association-evidence findings. Seven inherited
  scientific findings remain open across six records (three major, four minor); four
  records retain qualified positive outcomes. Seven formal expression-only applicability
  exclusions and five failed-access evidence-kind occurrences are corrected, while
  the three justified dinoflagellate morphology exclusions are retained. All 20 original
  artifacts remain immutable; only this linked review pair is added.'
source:
  git_revision: e1e8bf616b2ed45741e993b1993cb69017cf2e61
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
  - path: data/structures/membrane_organelle/reservosome.yaml
    sha256: c1a9daf798668ddf44d05a61e4ef589754275f4d385f1560ce38ccab0c07cdfa
    role: context
  - path: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    sha256: 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96
    role: target
  - path: data/structures/other/cvt_complex.yaml
    sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
    role: target
  - path: data/structures/other/cytostome.yaml
    sha256: 083f8800483f67a23bdb303aaf95d8d853d3bf67240e7ac2926e87ab66c89926
    role: target
  - path: data/structures/other/dash_complex.yaml
    sha256: 068456fa61be361559f04a3267867351f2adda6537a706aa6b152f62439f81fb
    role: target
  - path: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
    sha256: 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433
    role: target
  - path: data/structures/other/delta_dna_polymerase_complex.yaml
    sha256: 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf
    role: target
  - path: data/structures/other/diaa_complex.yaml
    sha256: 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158
    role: target
  - path: data/structures/other/dinoflagellate_antapex.yaml
    sha256: 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9
    role: target
  - path: data/structures/other/dinoflagellate_antapical_horn.yaml
    sha256: 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7
    role: target
  - path: data/structures/other/dinoflagellate_apex.yaml
    sha256: 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749
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
  - path: reviews/structured/20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit/review.md
    sha256: 0977058665ace58b4a28deb77e7894e0e3b751179683c6525ee7ea37a4d8c033
    role: context
  - path: reviews/structured/20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit/review.yaml
    sha256: 742d59158e7220ac8ffa6199a3ab027e15b158576a0da2a139ca9479c7629093
    role: context
  - path: reviews/structured/20261022T052917Z-cvt-complex-audit/review.md
    sha256: ce55b72871f05e0922e794e1f161ddd615a33d96a96c6e199df773105a58564e
    role: context
  - path: reviews/structured/20261022T052917Z-cvt-complex-audit/review.yaml
    sha256: 2fb8cfb272e8afe4f72557d1cddc970c9b22bdefa5d8f478b5c2e41f7fc6cfdf
    role: context
  - path: reviews/structured/20261022T052918Z-cytostome-audit/review.md
    sha256: ec3b6bc61fb8a056080290217cde937a82411545ac2753c11d1ab08a80fcac7a
    role: context
  - path: reviews/structured/20261022T052918Z-cytostome-audit/review.yaml
    sha256: e7269333148c97132c8c73c1855585cb68f1d167318c06ba613d84088df732d8
    role: context
  - path: reviews/structured/20261022T052919Z-dash-complex-audit/review.md
    sha256: 7fa77ab2afc72df50cbbe5294c91f38e490757ee27899d10de1524c58584a4f4
    role: context
  - path: reviews/structured/20261022T052919Z-dash-complex-audit/review.yaml
    sha256: 899f17ab75c00aadfcf0d0e6a58a757e85eadc24c33b4d087ea595cfc4a77569
    role: context
  - path: reviews/structured/20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit/review.md
    sha256: b9e1b2865f67bb565faa7acabb9f58e9a5c651b5eefd8574ef550d504d62cd57
    role: context
  - path: reviews/structured/20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit/review.yaml
    sha256: e80744f347bee2daefcf0487d1ffeb4e8064939f2d411457055fbbf101ec6b46
    role: context
  - path: reviews/structured/20261022T052920Z-delta-dna-polymerase-complex-audit/review.md
    sha256: a278229e68b60855c834e1f0525329dfe4348fb2efa10065fe9350d4cdc5cbfc
    role: context
  - path: reviews/structured/20261022T052920Z-delta-dna-polymerase-complex-audit/review.yaml
    sha256: 3e098cc257f297744751b0e1898e7631eda7018970d810416524f6a209a6f228
    role: context
  - path: reviews/structured/20261022T052921Z-diaa-complex-audit/review.md
    sha256: d46dd9f7081ea65aad26e57f1600d74a892df7cc9e8a1ba29578d673177e1c5a
    role: context
  - path: reviews/structured/20261022T052921Z-diaa-complex-audit/review.yaml
    sha256: 5566e163a1f37a1d88f3f7c2d489e3390cfd8b0456080453fb8a1f9aacd07b72
    role: context
  - path: reviews/structured/20261022T052921Z-dinoflagellate-antapex-audit/review.md
    sha256: a84ccd98862020b6cfc157a931c3f9039badbc07c9dc8a68d2f13cf1d218ab7d
    role: context
  - path: reviews/structured/20261022T052921Z-dinoflagellate-antapex-audit/review.yaml
    sha256: 441da86d4f9fb76d9b3f6fe8084b735ecec5296d87db3588acb89c3dd24e5897
    role: context
  - path: reviews/structured/20261022T052922Z-dinoflagellate-antapical-horn-audit/review.md
    sha256: c39953f74c2ac974ffc11f1b4b5d8028de9d2c283b1ffd6e87c5d7669682b52b
    role: context
  - path: reviews/structured/20261022T052922Z-dinoflagellate-antapical-horn-audit/review.yaml
    sha256: 48f171d804a7a5eb69760c6fac5ae6e7115bbf9ea175414f95f9a076e4f18e40
    role: context
  - path: reviews/structured/20261022T052923Z-dinoflagellate-apex-audit/review.md
    sha256: 74fbd71d713a1d5def17762f1427b3595b2f5563a3d89f37816e3e9409b685c4
    role: context
  - path: reviews/structured/20261022T052923Z-dinoflagellate-apex-audit/review.yaml
    sha256: 77e09e5ed1b57473aa2f10c398d35dacbb9d074006cb64981a567af12271c99f
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
- target_id: cellstructuremech:cullin_e_ubiquitin_ligase_complex
  path: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
  label: Cullin-E ubiquitin ligase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
- target_id: GO:0034270
  path: data/structures/other/cvt_complex.yaml
  label: Cvt complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cvt_complex.yaml
    role: maintained scientific record
- target_id: GO:0031910
  path: data/structures/other/cytostome.yaml
  label: cytostome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cytostome.yaml
    role: maintained scientific record
- target_id: GO:0042729
  path: data/structures/other/dash_complex.yaml
  label: DASH complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dash_complex.yaml
    role: maintained scientific record
- target_id: GO:0031431
  path: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
  label: Dbf4-dependent protein kinase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
    role: maintained scientific record
- target_id: GO:0043625
  path: data/structures/other/delta_dna_polymerase_complex.yaml
  label: delta DNA polymerase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/delta_dna_polymerase_complex.yaml
    role: maintained scientific record
- target_id: GO:1990125
  path: data/structures/other/diaa_complex.yaml
  label: DiaA complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/diaa_complex.yaml
    role: maintained scientific record
- target_id: GO:0097684
  path: data/structures/other/dinoflagellate_antapex.yaml
  label: dinoflagellate antapex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_antapex.yaml
    role: maintained scientific record
- target_id: GO:0097687
  path: data/structures/other/dinoflagellate_antapical_horn.yaml
  label: dinoflagellate antapical horn
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_antapical_horn.yaml
    role: maintained scientific record
- target_id: GO:0097683
  path: data/structures/other/dinoflagellate_apex.yaml
  label: dinoflagellate apex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_apex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 063ec99b63d964ef35acc14be323160a50835634.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    9a46ecafa001228b8ebdc17ebb7868e725711493.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head e1e8bf616b2ed45741e993b1993cb69017cf2e61.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head e1e8bf616b2ed45741e993b1993cb69017cf2e61.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head e1e8bf616b2ed45741e993b1993cb69017cf2e61.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head e1e8bf616b2ed45741e993b1993cb69017cf2e61.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head e1e8bf616b2ed45741e993b1993cb69017cf2e61.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate cellstructuremech:cullin_e_ubiquitin_ligase_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  command: just validate data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict cellstructuremech:cullin_e_ubiquitin_ligase_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  command: just validate-strict data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0034270
  status: passed
  required: true
  target_ids:
  - GO:0034270
  command: just validate data/structures/other/cvt_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0034270
  status: passed
  required: true
  target_ids:
  - GO:0034270
  command: just validate-strict data/structures/other/cvt_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0031910
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just validate data/structures/other/cytostome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0031910
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: just validate-strict data/structures/other/cytostome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0042729
  status: passed
  required: true
  target_ids:
  - GO:0042729
  command: just validate data/structures/other/dash_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0042729
  status: passed
  required: true
  target_ids:
  - GO:0042729
  command: just validate-strict data/structures/other/dash_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0031431
  status: passed
  required: true
  target_ids:
  - GO:0031431
  command: just validate data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0031431
  status: passed
  required: true
  target_ids:
  - GO:0031431
  command: just validate-strict data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0043625
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just validate data/structures/other/delta_dna_polymerase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0043625
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: just validate-strict data/structures/other/delta_dna_polymerase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:1990125
  status: passed
  required: true
  target_ids:
  - GO:1990125
  command: just validate data/structures/other/diaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:1990125
  status: passed
  required: true
  target_ids:
  - GO:1990125
  command: just validate-strict data/structures/other/diaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0097684
  status: passed
  required: true
  target_ids:
  - GO:0097684
  command: just validate data/structures/other/dinoflagellate_antapex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0097684
  status: passed
  required: true
  target_ids:
  - GO:0097684
  command: just validate-strict data/structures/other/dinoflagellate_antapex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0097687
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just validate data/structures/other/dinoflagellate_antapical_horn.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0097687
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: just validate-strict data/structures/other/dinoflagellate_antapical_horn.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0097683
  status: passed
  required: true
  target_ids:
  - GO:0097683
  command: just validate data/structures/other/dinoflagellate_apex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0097683
  status: passed
  required: true
  target_ids:
  - GO:0097683
  command: just validate-strict data/structures/other/dinoflagellate_apex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386
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
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  summary: 'Whole-record applicability was assessed for all ten targets. Seven positive
    molecular or pathway narratives require source-coverage assessment, correcting
    their formal expression-only exclusions. The three dinoflagellate records make
    morphology/topology claims and explicitly defer molecular claims, so their prose
    exclusions remain justified. Actual official catalogue coverage is separate from
    biological applicability: no matching yeast or Trypanosoma dataset is substituted
    with a foreign host. DiaA is checked in the real five-strain E. coli precise1k
    dataset; absence of above-threshold membership is bounded computational noncoverage,
    not biological absence or assembly evidence. The historical unavailable runner
    receipt is not presented as a fresh invocation.'
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b3149
  - plaque-catalogue
  - plaque-catalogue-search
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-graph-policy
  - micro-up-P06243
  - micro-up-P15436
  - micro-up-P32325
  - micro-up-P35734
  - micro-up-P36131
  - micro-up-P36162
  - micro-up-P46957
  - micro-up-P47110
  - micro-up-P53168
  - micro-up-P53267
  - micro-up-P66817
  - micro-up-Q03954
  - micro-up-Q12248
  - micro-tax-2759
  - micro-tax-4932
  - micro-tax-559292
  - micro-tax-562
  - micro-tax-83333
  - micro-go-0000776
  - micro-go-0000940
  - micro-go-0006260
  - micro-go-0006270
  - micro-go-0008608
  - micro-go-0031431
  - micro-go-0032991
  - micro-go-0042575
  - micro-go-0042729
  - micro-go-0043601
  - micro-go-0043625
  - micro-go-0140513
  - micro-go-1990102
  - micro-go-1990125
  - micro-ols-0043625
  - micro-ols-1990102
  - micro-ipr-IPR013960
  - micro-ipr-IPR013962-retry
  - micro-ipr-IPR013958
  - micro-ipr-IPR013963-retry
  - micro-ipr-IPR013964
  - micro-ipr-IPR013251
  - micro-ipr-IPR013966-retry2
  - micro-ipr-IPR051590
  - micro-ipr-IPR013939
  - micro-ipr-IPR024826-retry2
  - micro-ipr-IPR050240
  - micro-ipr-IPR019038-retry
  - micro-ipr-IPR023070-retry
  - micro-ipr-IPR035461
  - micro-ipr-IPR050099-retry2
  - micro-pmid-11568188
  - micro-pmid-11698664
  - micro-pmid-11782438
  - micro-pmid-12045100
  - micro-pmid-14562095
  - micro-pmid-17699754
  - micro-pmid-21256019
  - micro-pmid-25236177
  - micro-pmid-36701236
  - micro-pmid-9677405
  - micro-pmid-9677406
  - micro-pmid-9817759
  - micro-miranda2005-meta
  - micro-li2005-meta
  - micro-cheeseman2001-jats
  - micro-janke2002-publisherpdf
  - micro-keyamura-retained-reader
  - micro-ecoli-meta
  - plaque-policy
  - plaque-schema
  - plaque-review-skill
  - plaque-review-profile
  - plaque-review-schema
  - plaque-checklist
  - plaque-go
  - plaque-cytostome-path
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-tax-5693
  - plaque-protein-P14904
  - plaque-ipr-IPR001948
  - plaque-ipr-IPR023358
  - plaque-paper-0
  - plaque-paper-1
  - plaque-paper-2
  - plaque-paper-3
  - plaque-paper-4
  - plaque-paper-5
  - plaque-paper-6
  - plaque-paper-7
  - plaque-paper-8
  - plaque-scott2001-retained-body
  - plaque-shintani2004-retained-body
  - plaque-chasen2020-s3
  - plaque-porto2000-doi
  - plaque-catalogue
  - plaque-issue2461-context
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-go
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-catalogue
  - septin-tax-185431
  - septin-tax-5691
  - septin-tax-2864
  - septin-up-Q383D5
  - septin-up-Q38C61
  - septin-up-Q384S1
  - septin-up-Q38ED0
  - septin-ensembl-skp12
  - septin-ipr-045093
  - septin-ipr-051031
  - septin-ipr-001232
  - septin-ipr-016897
  - septin-pmid-41413177
  - septin-pmid-28052114
  - septin-pmid-7002229
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-fig2
  - septin-fig6
  - septin-fig7
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
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
- check_id: cullin_e_ubiquitin_ligase_complex-uniprot-verify
  name: Native Cullin-E ubiquitin ligase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cullin_e_ubiquitin_ligase_complex-uniprot-verify
- check_id: cullin_e_ubiquitin_ligase_complex-uniprot-causal
  name: Native Cullin-E ubiquitin ligase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cullin_e_ubiquitin_ligase_complex-uniprot-causal
- check_id: cvt_complex-uniprot-verify
  name: Native Cvt complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034270
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cvt_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cvt_complex-uniprot-verify
- check_id: cvt_complex-uniprot-causal
  name: Native Cvt complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034270
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cvt_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cvt_complex-uniprot-causal
- check_id: cytostome-uniprot-verify
  name: Native cytostome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cytostome.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cytostome-uniprot-verify
- check_id: cytostome-uniprot-causal
  name: Native cytostome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031910
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cytostome.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cytostome-uniprot-causal
- check_id: dash_complex-uniprot-verify
  name: Native DASH complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042729
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dash_complex.yaml
    --verify
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dash_complex-uniprot-verify
- check_id: dash_complex-uniprot-causal
  name: Native DASH complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042729
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dash_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dash_complex-uniprot-causal
- check_id: dbf4_dependent_protein_kinase_complex-uniprot-verify
  name: Native Dbf4-dependent protein kinase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031431
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dbf4_dependent_protein_kinase_complex-uniprot-verify
- check_id: dbf4_dependent_protein_kinase_complex-uniprot-causal
  name: Native Dbf4-dependent protein kinase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031431
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dbf4_dependent_protein_kinase_complex-uniprot-causal
- check_id: delta_dna_polymerase_complex-uniprot-verify
  name: Native delta DNA polymerase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-delta_dna_polymerase_complex-uniprot-verify
- check_id: delta_dna_polymerase_complex-uniprot-causal
  name: Native delta DNA polymerase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0043625
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/delta_dna_polymerase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-delta_dna_polymerase_complex-uniprot-causal
- check_id: diaa_complex-uniprot-verify
  name: Native DiaA complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990125
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/diaa_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-diaa_complex-uniprot-verify
- check_id: diaa_complex-uniprot-causal
  name: Native DiaA complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990125
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/diaa_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-diaa_complex-uniprot-causal
- check_id: dinoflagellate_antapex-uniprot-verify
  name: Native dinoflagellate antapex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097684
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_antapex-uniprot-verify
- check_id: dinoflagellate_antapex-uniprot-causal
  name: Native dinoflagellate antapex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097684
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_antapex-uniprot-causal
- check_id: dinoflagellate_antapical_horn-uniprot-verify
  name: Native dinoflagellate antapical horn UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_antapical_horn-uniprot-verify
- check_id: dinoflagellate_antapical_horn-uniprot-causal
  name: Native dinoflagellate antapical horn UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097687
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_antapical_horn-uniprot-causal
- check_id: dinoflagellate_apex-uniprot-verify
  name: Native dinoflagellate apex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097683
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_apex-uniprot-verify
- check_id: dinoflagellate_apex-uniprot-causal
  name: Native dinoflagellate apex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097683
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dinoflagellate_apex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96;
    current SHA256 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96.
    Record bytes unchanged since the original review.
  snapshot_sha256: 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 742d59158e7220ac8ffa6199a3ab027e15b158576a0da2a139ca9479c7629093
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/cvt_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902;
    current SHA256 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902.
    Record bytes unchanged since the original review.
  snapshot_sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T052917Z-cvt-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2fb8cfb272e8afe4f72557d1cddc970c9b22bdefa5d8f478b5c2e41f7fc6cfdf
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/cytostome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 e098724aea296245130198ea537eab00b38dd2429c7d91aeac78d09efab7d735;
    current SHA256 083f8800483f67a23bdb303aaf95d8d853d3bf67240e7ac2926e87ab66c89926.
    Changed record reassessed against current sources.
  snapshot_sha256: 083f8800483f67a23bdb303aaf95d8d853d3bf67240e7ac2926e87ab66c89926
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T052918Z-cytostome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e7269333148c97132c8c73c1855585cb68f1d167318c06ba613d84088df732d8
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/dash_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 97116204b79a4211411541b5db8c6bba2c892906521c2b754fa796b516bdfa91;
    current SHA256 068456fa61be361559f04a3267867351f2adda6537a706aa6b152f62439f81fb.
    Changed record reassessed against current sources.
  snapshot_sha256: 068456fa61be361559f04a3267867351f2adda6537a706aa6b152f62439f81fb
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T052919Z-dash-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 899f17ab75c00aadfcf0d0e6a58a757e85eadc24c33b4d087ea595cfc4a77569
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433;
    current SHA256 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e80744f347bee2daefcf0487d1ffeb4e8064939f2d411457055fbbf101ec6b46
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/delta_dna_polymerase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf;
    current SHA256 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T052920Z-delta-dna-polymerase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3e098cc257f297744751b0e1898e7631eda7018970d810416524f6a209a6f228
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/diaa_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158;
    current SHA256 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158.
    Record bytes unchanged since the original review.
  snapshot_sha256: 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T052921Z-diaa-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5566e163a1f37a1d88f3f7c2d489e3390cfd8b0456080453fb8a1f9aacd07b72
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/dinoflagellate_antapex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9;
    current SHA256 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T052921Z-dinoflagellate-antapex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 441da86d4f9fb76d9b3f6fe8084b735ecec5296d87db3588acb89c3dd24e5897
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/dinoflagellate_antapical_horn.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7;
    current SHA256 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7.
    Record bytes unchanged since the original review.
  snapshot_sha256: 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T052922Z-dinoflagellate-antapical-horn-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 48f171d804a7a5eb69760c6fac5ae6e7115bbf9ea175414f95f9a076e4f18e40
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/dinoflagellate_apex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Original frozen SHA256 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749;
    current SHA256 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T052923Z-dinoflagellate-apex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T05:03:05Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 77e09e5ed1b57473aa2f10c398d35dacbb9d074006cb64981a567af12271c99f
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/dash_complex.yaml
  locator: Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  accessed_at: '2026-11-04T04:58:49.639706Z'
  support: supports
  summary: Complete identity, hierarchy, seven/two/three/one-component inventories
    as appropriate, protein examples, taxonomy, functions, graph, historical discussions
    and curation events read. No maintained images or measured physical-property rows.
  snapshot_sha256: 068456fa61be361559f04a3267867351f2adda6537a706aa6b152f62439f81fb
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T052919Z-dash-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T04:58:49.639801Z'
  support: supports
  summary: Original source/check/assessment/finding/action/limitation/notes content
    inspected; original body reads and old command results remain historical, not
    recertified merely by preservation.
  snapshot_sha256: 899f17ab75c00aadfcf0d0e6a58a757e85eadc24c33b4d087ea595cfc4a77569
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/3-stale.diff
  locator: Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634
  accessed_at: '2026-11-04T04:58:49.639845Z'
  support: supports
  summary: DASH adds seven constituent component_ref nodes/edges and dated history;
    other three assigned records have no content delta. New edges are independently
    reassessed below.
  snapshot_sha256: e676fb303255629de6e5037efe10a6864a4a1b9683630d29c84a26fe8f6e7b8d
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
  locator: Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  accessed_at: '2026-11-04T04:58:49.639875Z'
  support: supports
  summary: Complete identity, hierarchy, seven/two/three/one-component inventories
    as appropriate, protein examples, taxonomy, functions, graph, historical discussions
    and curation events read. No maintained images or measured physical-property rows.
  snapshot_sha256: 5b0ecddabbb2373c35df54bb5993715956ea5d74dd7e42d6b3e37f6a2271a433
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T04:58:49.639895Z'
  support: supports
  summary: Original source/check/assessment/finding/action/limitation/notes content
    inspected; original body reads and old command results remain historical, not
    recertified merely by preservation.
  snapshot_sha256: e80744f347bee2daefcf0487d1ffeb4e8064939f2d411457055fbbf101ec6b46
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/4-stale.diff
  locator: Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634
  accessed_at: '2026-11-04T04:58:49.639928Z'
  support: supports
  summary: DASH adds seven constituent component_ref nodes/edges and dated history;
    other three assigned records have no content delta. New edges are independently
    reassessed below.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/delta_dna_polymerase_complex.yaml
  locator: Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  accessed_at: '2026-11-04T04:58:49.639952Z'
  support: supports
  summary: Complete identity, hierarchy, seven/two/three/one-component inventories
    as appropriate, protein examples, taxonomy, functions, graph, historical discussions
    and curation events read. No maintained images or measured physical-property rows.
  snapshot_sha256: 4669ff292f802ea0157d1496279723caa0330ddb676bb6fa63a6f1399b414fdf
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T052920Z-delta-dna-polymerase-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T04:58:49.639974Z'
  support: supports
  summary: Original source/check/assessment/finding/action/limitation/notes content
    inspected; original body reads and old command results remain historical, not
    recertified merely by preservation.
  snapshot_sha256: 3e098cc257f297744751b0e1898e7631eda7018970d810416524f6a209a6f228
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/5-stale.diff
  locator: Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634
  accessed_at: '2026-11-04T04:58:49.640007Z'
  support: supports
  summary: DASH adds seven constituent component_ref nodes/edges and dated history;
    other three assigned records have no content delta. New edges are independently
    reassessed below.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-3
  kind: record_content
  reference: data/structures/other/diaa_complex.yaml
  locator: Entire current maintained YAML at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  accessed_at: '2026-11-04T04:58:49.640029Z'
  support: supports
  summary: Complete identity, hierarchy, seven/two/three/one-component inventories
    as appropriate, protein examples, taxonomy, functions, graph, historical discussions
    and curation events read. No maintained images or measured physical-property rows.
  snapshot_sha256: 69949691e84f66d54da7945f2c9b0bd20d109d4a2ebea4931b72dc5829e5f158
- evidence_id: micro-prior-3
  kind: prior_review
  reference: reviews/structured/20261022T052921Z-diaa-complex-audit/review.yaml
  locator: Complete immutable original YAML and derived Markdown
  accessed_at: '2026-11-04T04:58:49.640047Z'
  support: supports
  summary: Original source/check/assessment/finding/action/limitation/notes content
    inspected; original body reads and old command results remain historical, not
    recertified merely by preservation.
  snapshot_sha256: 5566e163a1f37a1d88f3f7c2d489e3390cfd8b0456080453fb8a1f9aacd07b72
- evidence_id: micro-delta-3
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/6-stale.diff
  locator: Original frozen target revision versus current main 063ec99b63d964ef35acc14be323160a50835634
  accessed_at: '2026-11-04T04:58:49.640076Z'
  support: supports
  summary: DASH adds seven constituent component_ref nodes/edges and dated history;
    other three assigned records have no content delta. New edges are independently
    reassessed below.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components exact class/family identities and formation essentiality; Discussions
    append-only rationale/posed_date
  accessed_at: '2026-11-04T04:58:49.640098Z'
  support: supports
  summary: Class grounding differs from taxon-specific example xrefs. Formation is
    not viability or function; UNKNOWN alone is not a defect. Preserve dated rationale/history;
    update current notes/prompt only when supported.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component role/grounding_status/essentiality, taxonomic presence, graph
    actors and scope
  accessed_at: '2026-11-04T04:58:49.640121Z'
  support: supports
  summary: Generic families/classes and nonmechanistic outlines are valid. Concrete
    exact-family or condition-specific association gaps are bounded minor findings,
    not compulsory optional fields or experiments.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and native profile/config/checklist
  accessed_at: '2026-11-04T04:58:49.640151Z'
  support: supports
  summary: Positive genes/proteins/pathways trigger applicability; no-expression wording
    alone is insufficient. Catalogue and gene/module searches must retain host and
    computational limits. Seventeen common inputs hash-identical to previously read
    bytes; current skill/profile/config/shared contract/checklist and component/discussion
    rules reread.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Component references and nonmechanistic assembly/function outlines
  accessed_at: '2026-11-04T04:58:49.640171Z'
  support: supports
  summary: Constituent contributions and coarse function edges do not require invented
    atomic interaction or reaction-order claims. Exact declared graph scopes remain
    binding.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/original-audit.json
  locator: Eight actual native validate/render commands;52 historical frozen inputs;8
    immutable original artifacts
  accessed_at: '2026-11-04T04:54:30.072237Z'
  support: supports
  summary: All four original YAMLs validate and render byte-identical Markdown. Every
    historical input hash matches its recorded Git revision, and all eight original
    files match original PR commit.
  snapshot_sha256: 8a9c144f3e9701126e30c3104f06f2ffd5d585bd113e600938336ba9190665cf
- evidence_id: micro-up-P06243
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P06243.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P06243.raw
  accessed_at: '2026-11-04T04:49:28.531331Z'
  support: supports
  summary: 'P06243: UniProtKB reviewed (Swiss-Prot); Cell division control protein
    7; primary genes [''CDC7'']; loci [''YDL017W'', ''D2855'']; taxon 559292; InterPro
    [''IPR011009'', ''IPR000719'', ''IPR008271'']. Reference annotations are distinguished
    from newly read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32
    nuclear location is by similarity, unlike the experimental P15436/Huh join.'
  snapshot_sha256: 2fe80227ec5a07ef6de970843085fad4d227a0563ee62ebbb88a15ad44a951fa
- evidence_id: micro-up-P15436
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P15436.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P15436.raw
  accessed_at: '2026-11-04T04:49:30.140580Z'
  support: supports
  summary: 'P15436: UniProtKB reviewed (Swiss-Prot); DNA polymerase delta catalytic
    subunit; primary genes [''POL3'']; loci [''YDL102W'', ''D2366'']; taxon 559292;
    InterPro [''IPR006172'', ''IPR017964'', ''IPR006133'', ''IPR006134'', ''IPR043502'',
    ''IPR042087'', ''IPR023211'', ''IPR050240'', ''IPR056435'', ''IPR012337'', ''IPR036397'',
    ''IPR025687'']. Reference annotations are distinguished from newly read primary
    experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear location
    is by similarity, unlike the experimental P15436/Huh join.'
  snapshot_sha256: c140646e1adb54eb6cbf96d96e007313c655e93b2ecd7dc1a8999d036f8846ee
- evidence_id: micro-up-P32325
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32325.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P32325.raw
  accessed_at: '2026-11-04T04:49:21.117676Z'
  support: supports
  summary: 'P32325: UniProtKB reviewed (Swiss-Prot); DDK kinase regulatory subunit
    DBF4; primary genes [''DBF4'']; loci [''YDR052C'', ''D4205'', ''YD9609.07C''];
    taxon 559292; InterPro [''IPR036420'', ''IPR055116'', ''IPR013939'', ''IPR051590'',
    ''IPR006572'', ''IPR038545'']. Reference annotations are distinguished from newly
    read primary experiments; P47110 has no current InterPro xref; Pol31/Pol32 nuclear
    location is by similarity, unlike the experimental P15436/Huh join.'
  snapshot_sha256: 0546ee25f8f1a6282e15dd0ef4154db5a7b7d777367e65dc1ce0702681ed8ebc
- evidence_id: micro-up-P35734
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P35734.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P35734.raw
  accessed_at: '2026-11-04T04:49:25.162827Z'
  support: supports
  summary: 'P35734: UniProtKB reviewed (Swiss-Prot); DASH complex subunit ASK1; primary
    genes [''ASK1'']; loci [''YKL052C'', ''YKL306'']; taxon 559292; InterPro [''IPR013964''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: b96ef8693b0fbc9b4094da03e2e57778c268519dd5ec0ca91df73027eb16ffa7
- evidence_id: micro-up-P36131
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P36131.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P36131.raw
  accessed_at: '2026-11-04T04:49:22.234308Z'
  support: supports
  summary: 'P36131: UniProtKB reviewed (Swiss-Prot); DASH complex subunit SPC34; primary
    genes [''SPC34'']; loci [''YKR037C'']; taxon 559292; InterPro [''IPR013966''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: 640da80460ca5ea12895a918e97afb042793d677c937f5fcd99f3f2b08e5da69
- evidence_id: micro-up-P36162
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P36162.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P36162.raw
  accessed_at: '2026-11-04T04:49:24.158710Z'
  support: supports
  summary: 'P36162: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DAD2; primary
    genes [''DAD2'']; loci [''YKR083C'', ''YKR403'']; taxon 559292; InterPro [''IPR013963''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: e23dcad53b83e2fdc36d9c72bdbb578a31680222132e656aa6d7cd26ab91bd5a
- evidence_id: micro-up-P46957
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P46957.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P46957.raw
  accessed_at: '2026-11-04T04:49:23.039062Z'
  support: supports
  summary: 'P46957: UniProtKB reviewed (Swiss-Prot); DNA polymerase delta small subunit;
    primary genes [''POL31'']; loci [''YJR006W'', ''J1427'', ''YJR83.7'']; taxon 559292;
    InterPro [''IPR007185'', ''IPR040663'', ''IPR024826'', ''IPR041863'']. Reference
    annotations are distinguished from newly read primary experiments; P47110 has
    no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: 934e41ac083022ce27adac013243afb66b3504ae34bb288fed4a759b4bf3a7b2
- evidence_id: micro-up-P47110
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P47110.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P47110.raw
  accessed_at: '2026-11-04T04:49:24.144290Z'
  support: supports
  summary: 'P47110: UniProtKB reviewed (Swiss-Prot); DNA polymerase delta subunit
    3; primary genes [''POL32'']; loci [''YJR043C'', ''J1626'']; taxon 559292; InterPro
    []. Reference annotations are distinguished from newly read primary experiments;
    P47110 has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity,
    unlike the experimental P15436/Huh join.'
  snapshot_sha256: e977ad040fbc43ef434b2f25805fbddabea676641681c5a4cc50da8fa35fa70e
- evidence_id: micro-up-P53168
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53168.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P53168.raw
  accessed_at: '2026-11-04T04:49:26.254348Z'
  support: supports
  summary: 'P53168: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DUO1; primary
    genes [''DUO1'']; loci [''YGL061C'']; taxon 559292; InterPro [''IPR013960''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: 6100ef8f503d4b576c0d09bc568ae67cbd32ae1b968fa66617fcd96190447662
- evidence_id: micro-up-P53267
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53267.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P53267.raw
  accessed_at: '2026-11-04T04:49:31.223872Z'
  support: supports
  summary: 'P53267: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DAM1; primary
    genes [''DAM1'']; loci [''YGR113W'', ''G6153'']; taxon 559292; InterPro [''IPR013962''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: aead3323bb934ebe25eb40ed9e87b68cf322bafe66e709a24b2fc8b1ea061414
- evidence_id: micro-up-P66817
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P66817.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-P66817.raw
  accessed_at: '2026-11-04T04:49:25.128259Z'
  support: supports
  summary: 'P66817: UniProtKB reviewed (Swiss-Prot); DnaA initiator-associating protein
    DiaA; primary genes [''diaA'']; loci [''b3149'', ''JW3118'']; taxon 83333; InterPro
    [''IPR023070'', ''IPR035461'', ''IPR001347'', ''IPR046348'', ''IPR050099'']. Reference
    annotations are distinguished from newly read primary experiments; P47110 has
    no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: 4683e244126b2c70e7a2e7e1d333b5afabd6bf0da217c4bfba240a016b1a3180
- evidence_id: micro-up-Q03954
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q03954.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-Q03954.raw
  accessed_at: '2026-11-04T04:49:27.186664Z'
  support: supports
  summary: 'Q03954: UniProtKB reviewed (Swiss-Prot); DASH complex subunit SPC19; primary
    genes [''SPC19'']; loci [''YDR201W'']; taxon 559292; InterPro [''IPR013251''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: 9ca6829c61fc7ee08f97a6e242029f568e064a4085f3b81b7d12a4fb7a7eeeef
- evidence_id: micro-up-Q12248
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12248.json
  locator: Native status/product/primary genes/synonyms/loci/taxon, complete location
    annotations/evidence codes and InterPro links; relevant subunit/function clauses,
    not all linked papers; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/up-Q12248.raw
  accessed_at: '2026-11-04T04:49:28.141590Z'
  support: supports
  summary: 'Q12248: UniProtKB reviewed (Swiss-Prot); DASH complex subunit DAD1; primary
    genes [''DAD1'']; loci [''YDR016C'']; taxon 559292; InterPro [''IPR013958''].
    Reference annotations are distinguished from newly read primary experiments; P47110
    has no current InterPro xref; Pol31/Pol32 nuclear location is by similarity, unlike
    the experimental P15436/Huh join.'
  snapshot_sha256: 0c09a8bee2b94f61ae48fd54d5f6b7d2c233da56e3ee663dc1efb3ebd1d3c3a2
- evidence_id: micro-query-ASK1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AASK1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-ASK1.raw
  accessed_at: '2026-11-04T04:49:26.420156Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P35734'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 8bc9fe87eca27c89beadb19f203e50492e35137cbf18bbf902a61fc3c95a9d74
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AASK1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:26.420156Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-CDC7
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACDC7+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-CDC7.raw
  accessed_at: '2026-11-04T04:49:18.270043Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P06243'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 54ba6b3287b7c1caf6f8f81b535f8a5b26ace9433613f389a6ba862b76243c2d
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACDC7+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:18.270043Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-DAD1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAD1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DAD1.raw
  accessed_at: '2026-11-04T04:49:17.714684Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''Q12248'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: baa474c2eee8024b56f93971ecef68425f8a0fafed10d76b31ba4552842ce70a
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAD1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:17.714684Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-DAD2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAD2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DAD2.raw
  accessed_at: '2026-11-04T04:49:20.330783Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P36162'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: bb53e083c968aa74e8a72f974d5957c93f72f51653d95faaab7ffe195699d40d
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAD2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:20.330783Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-DAM1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAM1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DAM1.raw
  accessed_at: '2026-11-04T04:49:28.519734Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P53267'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 53a3563b4637f0517167871643d9659d8e7b56dd91291fe4f1e5c8b7e6f55443
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADAM1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:28.519734Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-DBF4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADBF4+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DBF4.raw
  accessed_at: '2026-11-04T04:49:23.323811Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P32325'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 82a8ddf9ab23f95ed7871614309b13b085bb78e7d6a6f0e1b0c1c7920f991c88
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADBF4+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:23.323811Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-DUO1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADUO1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-DUO1.raw
  accessed_at: '2026-11-04T04:49:22.297197Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P53168'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: b05fc4e36c6241b1fab7e4ec6ff121f9893a208311882223111206ee93854f94
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADUO1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:22.297197Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-POL3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL3+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-POL3.raw
  accessed_at: '2026-11-04T04:49:18.408006Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P15436'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: eacd36eab01d3405332f56c954439292aefca3c09475342840a7b19314a162a0
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL3+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:18.408006Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-POL31
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL31+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-POL31.raw
  accessed_at: '2026-11-04T04:49:19.214940Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P46957'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 32f913817a94215af6f28e9f8b688d6e1534cf8b4174548ab9e0f6ec0972e3a9
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL31+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:19.214940Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-POL32
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL32+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-POL32.raw
  accessed_at: '2026-11-04T04:49:20.294491Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P47110'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 6a69f3ac8c260450d0a83bdd9f3f6656308b3403da906581e6eea352d6e83037
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3APOL32+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:20.294491Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-SPC19
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASPC19+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-SPC19.raw
  accessed_at: '2026-11-04T04:49:17.975516Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''Q03954'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 38e8df39deacaca10d78e5e49dce97fc8900aea8c7fb1610d9e4e99aeeda876c
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASPC19+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:17.975516Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-SPC34
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASPC34+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-SPC34.raw
  accessed_at: '2026-11-04T04:49:19.589147Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P36131'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: 7ac3f7031831194919c73cd2f2f3d766ce05d05d8255786504946703ec45a622
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ASPC34+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:19.589147Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-query-diaA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdiaA+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete exact reviewed gene/taxon result page and returned identities;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/query-diaA.raw
  accessed_at: '2026-11-04T04:49:21.218681Z'
  support: supports
  summary: 'Current bounded query returns 1 accession(s): [''P66817'']. All13 exact
    queries return their intended singleton; this does not reconstruct a historical
    search or prove causal membership.'
  snapshot_sha256: c9bd1e6f2fd8d4086f1d0286c2f89fb17a06eb3ea02870af9f9b2331b29a5b63
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdiaA+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=100;
    actual 2026-11-04T04:49:21.218681Z; size100, complete returned page, no pagination
    link recorded. Exact reviewed gene and specified reference taxon only, not all
    aliases/taxa/past versions.
- evidence_id: micro-tax-2759
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-2759.raw
  accessed_at: '2026-11-04T04:49:29.155904Z'
  support: supports
  summary: '2759: Eukaryota, domain; parent {''scientificName'': ''cellular organisms'',
    ''taxonId'': 131567}. Species examples, S288c/K12 protein references and experimental
    derivatives are not conflated.'
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-4932.raw
  accessed_at: '2026-11-04T04:49:31.098588Z'
  support: supports
  summary: '4932: Saccharomyces cerevisiae, species; parent {''scientificName'': ''Saccharomyces'',
    ''taxonId'': 4930}. Species examples, S288c/K12 protein references and experimental
    derivatives are not conflated.'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
- evidence_id: micro-tax-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-559292.raw
  accessed_at: '2026-11-04T04:49:29.149301Z'
  support: supports
  summary: '559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c), strain;
    parent {''scientificName'': ''Saccharomyces cerevisiae'', ''commonName'': "Baker''s
    yeast", ''taxonId'': 4932}. Species examples, S288c/K12 protein references and
    experimental derivatives are not conflated.'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: micro-tax-562
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/562.json
  locator: Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-562.raw
  accessed_at: '2026-11-04T04:49:30.066443Z'
  support: supports
  summary: '562: Escherichia coli, species; parent {''scientificName'': ''Escherichia'',
    ''taxonId'': 561}. Species examples, S288c/K12 protein references and experimental
    derivatives are not conflated.'
  snapshot_sha256: 20aa358053d2fae1e2cd74636ed5aca1efbc372e5b8bcfdb10d3fa80be6789a1
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Exact taxon ID/name/rank/parent; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-04T04:49:32.055363Z'
  support: supports
  summary: '83333: Escherichia coli (strain K12), strain; parent {''scientificName'':
    ''Escherichia coli'', ''taxonId'': 562}. Species examples, S288c/K12 protein references
    and experimental derivatives are not conflated.'
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-go-0000776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0000776.raw
  accessed_at: '2026-11-04T04:49:25.847149Z'
  support: supports
  summary: '[{"id": "GO:0000776", "name": "kinetochore", "isObsolete": false, "definition":
    {"text": "A multisubunit complex that is located at the centromeric region of
    DNA and provides an attachment point for the spindle microtubules."}, "comment":
    "Note that the kinetochore overlaps the centromeric DNA, but centromeric DNA is
    not part of the kinetochore.", "synonyms": [{"name": "condensed chromosome kinetochore",
    "type": "exact"}, {"name": "condensed nuclear chromosome kinetochore", "type":
    "exact"}, {"name": "NMS complex", "type": "narrow"}]}]. GO identity is separate
    from primary source interpretation; Polδ retained dimeric GO wording is explicitly
    overridden by the inspected later primary abstract.'
  snapshot_sha256: 1b1d92f2f3ec584f7fe8d61021ebb433586609a130c97e9ec37a07cfda864c76
- evidence_id: micro-go-0000940
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000940
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0000940.raw
  accessed_at: '2026-11-04T04:49:26.042252Z'
  support: supports
  summary: '[{"id": "GO:0000940", "name": "outer kinetochore", "isObsolete": false,
    "definition": {"text": "The region of a kinetochore most external to centromeric
    DNA; this outer region mediates kinetochore-microtubule interactions.", "xrefs":
    [{"dbCode": "PMID", "dbId": "11483983"}]}, "comment": null, "synonyms": [{"name":
    "condensed chromosome outer kinetochore", "type": "exact"}, {"name": "condensed
    nuclear chromosome outer kinetochore", "type": "exact"}, {"name": "outer kinetochore
    of condensed chromosome", "type": "exact"}, {"name": "outer kinetochore of condensed
    nuclear chromosome", "type": "exact"}, {"name": "outer kinetochore plate", "type":
    "narrow"}]}]. GO identity is separate from primary source interpretation; Polδ
    retained dimeric GO wording is explicitly overridden by the inspected later primary
    abstract.'
  snapshot_sha256: 10873acde0d686071f570f5abe217c347fff5836f301f7f9b1e05ceab4ded9e8
- evidence_id: micro-go-0006260
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0006260.raw
  accessed_at: '2026-11-04T04:49:26.746593Z'
  support: supports
  summary: '[{"id": "GO:0006260", "name": "DNA replication", "isObsolete": false,
    "definition": {"text": "The cellular metabolic process in which a cell duplicates
    one or more molecules of DNA. DNA replication begins when specific sequences,
    known as origins of replication, are recognized and bound by the origin recognition
    complex, and ends when the original DNA molecule has been completely duplicated
    and the copies topologically separated. The unit of replication usually corresponds
    to the genome of the cell, an organelle, or a virus. The template for replication
    can either be an existing DNA molecule or RNA."}, "comment": "DNA biosynthesis
    is only part of this process. See also the biological process terms ''DNA-dependent
    DNA replication ; GO:0006261'' and ''RNA-dependent DNA replication ; GO:0006278''.",
    "synonyms": null}]. GO identity is separate from primary source interpretation;
    Polδ retained dimeric GO wording is explicitly overridden by the inspected later
    primary abstract.'
  snapshot_sha256: dc45c0feccd11a684f3d3f838297ef32f5b69a7b59a61d655120b7ac89ec8fba
- evidence_id: micro-go-0006270
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006270
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0006270.raw
  accessed_at: '2026-11-04T04:49:27.221671Z'
  support: supports
  summary: '[{"id": "GO:0006270", "name": "DNA replication initiation", "isObsolete":
    false, "definition": {"text": "The process in which DNA-dependent DNA replication
    is started; it begins when specific sequences, known as origins of replication,
    are recognized and bound by the origin recognition complex, followed by DNA unwinding.",
    "xrefs": [{"dbCode": "PMID", "dbId": "28209641"}]}, "comment": null, "synonyms":
    [{"name": "DNA-dependent DNA replication initiation", "type": "exact"}, {"name":
    "DNA endoreduplication initiation", "type": "narrow"}, {"name": "DNA re-replication
    initiation", "type": "narrow"}]}]. GO identity is separate from primary source
    interpretation; Polδ retained dimeric GO wording is explicitly overridden by the
    inspected later primary abstract.'
  snapshot_sha256: e0ea96216a022971fca313127bdae0280af832afc23734001e734b67973c6601
- evidence_id: micro-go-0008608
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008608
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0008608.raw
  accessed_at: '2026-11-04T04:49:26.883856Z'
  support: supports
  summary: '[{"id": "GO:0008608", "name": "attachment of spindle microtubules to kinetochore",
    "isObsolete": false, "definition": {"text": "The process in which spindle microtubules
    become physically associated with the proteins making up the kinetochore complex.",
    "xrefs": [{"dbCode": "PMID", "dbId": "10322137"}]}, "comment": "This class covers
    all attachments of spindle microtubules to the kinetochore, including the many
    incorrect attachments which initially form and are later corrected to stable attachments
    with the correct orientation for segregation to proceed (sister chromatid biorientation).",
    "synonyms": [{"name": "amphotelic attachment", "type": "related"}, {"name": "attachment
    of spindle microtubules to chromosome", "type": "exact"}, {"name": "bipolar attachment",
    "type": "related"}, {"name": "kinetochore-microtubule attachment", "type": "exact"},
    {"name": "kinetochore microtubule interaction", "type": "broad"}, {"name": "kinetochore-microtubule
    interaction", "type": "broad"}, {"name": "microtubule anchoring at kinetochore",
    "type": "exact"}, {"name": "microtubule and chromosome interaction", "type": "broad"},
    {"name": "microtubule and kinetochore interaction", "type": "related"}, {"name":
    "microtubule capture", "type": "narrow"}, {"name": "spindle chromosome attachment",
    "type": "exact"}, {"name": "spindle-chromosome interaction", "type": "broad"},
    {"name": "spindle kinetochore attachment", "type": "exact"}]}]. GO identity is
    separate from primary source interpretation; Polδ retained dimeric GO wording
    is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: c20d36ea8364cd9ab8f7397b4c2301e513f1cd4f380bcbbd1da5c3546c9e66b1
- evidence_id: micro-go-0031431
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031431
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0031431.raw
  accessed_at: '2026-11-04T04:49:27.343753Z'
  support: supports
  summary: '[{"id": "GO:0031431", "name": "Dbf4-dependent protein kinase complex",
    "isObsolete": false, "definition": {"text": "A heterodimeric protein complex required
    for the activation of DNA replication origins; comprises a catalytic subunit and
    a regulatory subunit (in Saccharomyces, Cdc7p and Dbf4p, respectively); complexes
    identified in other species generally contain proteins related to the Saccharomyces
    proteins.", "xrefs": [{"dbCode": "PMID", "dbId": "12045100"}]}, "comment": null,
    "synonyms": [{"name": "Cdc7-Dbf4 complex", "type": "narrow"}, {"name": "DDK",
    "type": "exact"}, {"name": "Hsk1-Dfp1 kinase complex", "type": "narrow"}]}]. GO
    identity is separate from primary source interpretation; Polδ retained dimeric
    GO wording is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 39305488cbbdefae2828f3de1b50fb7350f0fab6ae6a9004c2227c3ec1468af8
- evidence_id: micro-go-0032991
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0032991.raw
  accessed_at: '2026-11-04T04:49:27.734457Z'
  support: supports
  summary: '[{"id": "GO:0032991", "name": "protein-containing complex", "isObsolete":
    false, "definition": {"text": "A stable assembly of two or more macromolecules,
    i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component
    is a protein and the constituent parts function together."}, "comment": "A protein
    complex in this context is meant as a stable set of interacting proteins which
    can be co-purified by an acceptable method, and where the complex has been shown
    to exist as an isolated, functional unit in vivo. Acceptable experimental methods
    include stringent protein purification followed by detection of protein interaction.
    The following methods should be considered non-acceptable: simple immunoprecipitation,
    pull-down experiments from cell extracts without further purification, colocalization
    and 2-hybrid screening. Interactions that should not be captured as protein complexes
    include: 1) enzyme/substrate, receptor/ligand or any similar transient interactions,
    unless these are a critical part of the complex assembly or are required e.g.
    for the receptor to be functional; 2) proteins associated in a pull-down/co-immunoprecipitation
    assay with no functional link or any evidence that this is a defined biological
    entity rather than a loose-affinity complex; 3) any complex where the only evidence
    is based on genetic interaction data; 4) partial complexes, where some subunits
    (e.g. transmembrane ones) cannot be expressed as recombinant proteins and are
    excluded from experiments (in this case, independent evidence is necessary to
    find out the composition of the full complex, if known). Interactions that may
    be captured as protein complexes include: 1) enzyme/substrate or receptor/ligand
    if the complex can only assemble and become functional in the presence of both
    classes of subunits; 2) complexes where one of the members has not been shown
    to be physically linked to the other(s), but is a homologue of, and has the same
    functionality as, a protein that has been experimentally demonstrated to form
    a complex with the other member(s); 3) complexes whose existence is accepted based
    on localization and pharmacological studies, but for which experimental evidence
    is not yet available for the complex as a whole.", "synonyms": [{"name": "macromolecular
    complex", "type": "exact"}, {"name": "macromolecule complex", "type": "exact"},
    {"name": "protein complex", "type": "narrow"}, {"name": "protein containing complex",
    "type": "exact"}, {"name": "protein-protein complex", "type": "narrow"}]}]. GO
    identity is separate from primary source interpretation; Polδ retained dimeric
    GO wording is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
- evidence_id: micro-go-0042575
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042575
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0042575.raw
  accessed_at: '2026-11-04T04:49:27.537881Z'
  support: supports
  summary: '[{"id": "GO:0042575", "name": "DNA polymerase complex", "isObsolete":
    false, "definition": {"text": "A protein complex that possesses DNA polymerase
    activity and is involved in template directed synthesis of DNA.", "xrefs": [{"dbCode":
    "PMID", "dbId": "12045093"}]}, "comment": null, "synonyms": null}]. GO identity
    is separate from primary source interpretation; Polδ retained dimeric GO wording
    is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 03e6fe0dd8263f1e7fca5a967f126141e378a6b572bed7ab152452b57a4c727f
- evidence_id: micro-go-0042729
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042729
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0042729.raw
  accessed_at: '2026-11-04T04:49:28.079492Z'
  support: supports
  summary: '[{"id": "GO:0042729", "name": "DASH complex", "isObsolete": false, "definition":
    {"text": "A large protein complex, containing around 8-10 subunits in yeast, including
    Duo1p, Dam1p, Dad1p and Ask1p. The complex forms part of the outer kinetochore,
    associates with microtubules when the kinetochore attaches to the spindle, and
    plays a role in spindle attachment, chromosome segregation and spindle stability.",
    "xrefs": [{"dbCode": "PMID", "dbId": "11782438"}, {"dbCode": "PMID", "dbId": "11799062"},
    {"dbCode": "PMID", "dbId": "15632076"}, {"dbCode": "PMID", "dbId": "15640796"}]},
    "comment": "Note that this complex is conserved in fungi but has not been observed
    in metazoans.", "synonyms": [{"name": "condensed nuclear chromosome kinetochore-associated
    DASH complex", "type": "exact"}, {"name": "Dam1 complex", "type": "exact"}, {"name":
    "DDD complex", "type": "exact"}, {"name": "Duo1p-Dam1p-Dad1p complex", "type":
    "exact"}]}]. GO identity is separate from primary source interpretation; Polδ
    retained dimeric GO wording is explicitly overridden by the inspected later primary
    abstract.'
  snapshot_sha256: 230c5612c279fc493e90fa49000308b3cfa2aa2efda78c34cbe062f5d701930b
- evidence_id: micro-go-0043601
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043601
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0043601.raw
  accessed_at: '2026-11-04T04:49:28.094830Z'
  support: supports
  summary: '[{"id": "GO:0043601", "name": "nuclear replisome", "isObsolete": false,
    "definition": {"text": "A multi-component enzymatic machine at the nuclear replication
    fork, which mediates DNA replication. Includes DNA primase, one or more DNA polymerases,
    DNA helicases, and other proteins."}, "comment": null, "synonyms": null}]. GO
    identity is separate from primary source interpretation; Polδ retained dimeric
    GO wording is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 08b8ce158267e4b7b2816959e1c08b3f42c2a3e4ca6a817dbef323679c8528bf
- evidence_id: micro-go-0043625
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043625
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0043625.raw
  accessed_at: '2026-11-04T04:49:28.031153Z'
  support: supports
  summary: '[{"id": "GO:0043625", "name": "delta DNA polymerase complex", "isObsolete":
    false, "definition": {"text": "A multimeric DNA polymerase enzyme complex which
    differs in composition amongst species; in humans it is a heterotetramer of four
    subunits of approximately 125, 50, 68 and 12kDa, while in S. cerevisiae, it has
    three different subunits which form a heterotrimer, and the active enzyme is a
    dimer of this heterotrimer. Functions in DNA replication, mismatch repair and
    excision repair.", "xrefs": [{"dbCode": "ISBN", "dbId": "0198547684"}, {"dbCode":
    "PMID", "dbId": "11205330"}, {"dbCode": "PMID", "dbId": "12403614"}]}, "comment":
    null, "synonyms": [{"name": "delta-DNA polymerase complex", "type": "exact"}]}].
    GO identity is separate from primary source interpretation; Polδ retained dimeric
    GO wording is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 3339f8366efbb980f04254b77030e784dc7af3ee6cda0ac068a4b284d504b01f
- evidence_id: micro-go-0140513
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140513
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-0140513.raw
  accessed_at: '2026-11-04T04:49:28.377764Z'
  support: supports
  summary: '[{"id": "GO:0140513", "name": "nuclear protein-containing complex", "isObsolete":
    false, "definition": {"text": "A stable assembly of two or more macromolecules,
    i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component
    is a protein and the constituent parts function together in the nucleus."}, "comment":
    null, "synonyms": [{"name": "nuclear complex", "type": "exact"}]}]. GO identity
    is separate from primary source interpretation; Polδ retained dimeric GO wording
    is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 61c31928c6fb33a97da0bafa0beafb5392a27dac53b617f92ba08fb5cf0511b7
- evidence_id: micro-go-1990102
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990102
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-1990102.raw
  accessed_at: '2026-11-04T04:49:28.738402Z'
  support: supports
  summary: '[{"id": "GO:1990102", "name": "DnaA-DiaA complex", "isObsolete": false,
    "definition": {"text": "A protein-DNA complex containing a tetramer of DiaA attached
    to multiple DnaA molecule bound to oriC DNA. Regulates timely initiation of chromosomal
    replication during the cell cycle by stimulating assembly of DnaA-oriC complexes,
    conformational changes in ATP-DnaA initiation complexes, and unwinding of oriC
    duplex DNA.", "xrefs": [{"dbCode": "PMID", "dbId": "15326179"}, {"dbCode": "PMID",
    "dbId": "17699754"}]}, "comment": null, "synonyms": [{"name": "DnaA-DiaA-DNA complex",
    "type": "exact"}]}]. GO identity is separate from primary source interpretation;
    Polδ retained dimeric GO wording is explicitly overridden by the inspected later
    primary abstract.'
  snapshot_sha256: dabec07dbf0f550e085d5eca8f679ec7c974d9f3b7d0c402c801e8ca02876715
- evidence_id: micro-go-1990125
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990125
  locator: Complete exact term identity/active status/definition/synonyms/comments;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/go-1990125.raw
  accessed_at: '2026-11-04T04:49:28.997037Z'
  support: supports
  summary: '[{"id": "GO:1990125", "name": "DiaA complex", "isObsolete": false, "definition":
    {"text": "A homotetrameric protein complex consisting of a symmetrical pair of
    DiaA homodimers. Facilitates DnaA binding to the origin of replication during
    replication initiation.", "xrefs": [{"dbCode": "PMID", "dbId": "17699754"}]},
    "comment": null, "synonyms": [{"name": "DiaA homotetramer", "type": "exact"}]}].
    GO identity is separate from primary source interpretation; Polδ retained dimeric
    GO wording is explicitly overridden by the inspected later primary abstract.'
  snapshot_sha256: 9cf199a142fbbf9b19c38e98777b40734fd99268ad12f37728a5490cbc3d3fe3
- evidence_id: micro-ols-0043625
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_0043625/graph
  locator: Complete native OLS typed graph nodes/edges; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ols-0043625.raw
  accessed_at: '2026-11-04T04:49:33.765554Z'
  support: supports
  summary: '{"nodes": [{"iri": "http://purl.obolibrary.org/obo/GO_0043625", "label":
    "delta DNA polymerase complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_0042575",
    "label": "DNA polymerase complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_0140513",
    "label": "nuclear protein-containing complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_0043601",
    "label": "nuclear replisome"}, {"iri": "http://purl.obolibrary.org/obo/NCBITaxon_2759",
    "label": "Eukaryota"}], "edges": [{"source": "http://purl.obolibrary.org/obo/GO_0043625",
    "target": "http://purl.obolibrary.org/obo/GO_0042575", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/GO_0043625",
    "target": "http://purl.obolibrary.org/obo/GO_0140513", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/GO_0043625",
    "target": "http://purl.obolibrary.org/obo/GO_0043601", "uri": "http://purl.obolibrary.org/obo/BFO_0000050",
    "label": "part of"}, {"source": "http://purl.obolibrary.org/obo/GO_0043625", "target":
    "http://purl.obolibrary.org/obo/NCBITaxon_2759", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}]}. is_a and part/has_part remain distinct.'
  snapshot_sha256: 1967625e1ab1c42fd1f492800c7d38c84f577a12abb3c6e6d782399a566cbd84
- evidence_id: micro-ols-1990102
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1990102/graph
  locator: Complete native OLS typed graph nodes/edges; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ols-1990102.raw
  accessed_at: '2026-11-04T04:49:33.453189Z'
  support: supports
  summary: '{"nodes": [{"iri": "http://purl.obolibrary.org/obo/GO_1990102", "label":
    "DnaA-DiaA complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_1990077", "label":
    "primosome complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_1990101", "label":
    "DnaA-oriC complex"}, {"iri": "http://purl.obolibrary.org/obo/GO_1990125", "label":
    "DiaA complex"}, {"iri": "http://purl.obolibrary.org/obo/NCBITaxon_Union_0000004",
    "label": "Prokaryota"}], "edges": [{"source": "http://purl.obolibrary.org/obo/GO_1990102",
    "target": "http://purl.obolibrary.org/obo/GO_1990077", "uri": "http://www.w3.org/2000/01/rdf-schema#subClassOf",
    "label": "subClassOf"}, {"source": "http://purl.obolibrary.org/obo/GO_1990102",
    "target": "http://purl.obolibrary.org/obo/GO_1990101", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/GO_1990102",
    "target": "http://purl.obolibrary.org/obo/GO_1990125", "uri": "http://purl.obolibrary.org/obo/BFO_0000051",
    "label": "has part"}, {"source": "http://purl.obolibrary.org/obo/GO_1990102",
    "target": "http://purl.obolibrary.org/obo/NCBITaxon_Union_0000004", "uri": "http://purl.obolibrary.org/obo/RO_0002162",
    "label": "in taxon"}]}. is_a and part/has_part remain distinct.'
  snapshot_sha256: 72308b1a6fcee2b685c35114fe032d849fde7563724c48fc3282f8d5f2c9f609
- evidence_id: micro-ipr-IPR013960
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013960/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013960.raw
  accessed_at: '2026-11-04T04:49:31.504669Z'
  support: supports
  summary: 'IPR013960: {''name'': ''DASH complex subunit Duo1'', ''short'': ''DASH_Duo1''};
    type family; signatures {''panther'': {''PTHR28216'': ''DASH COMPLEX SUBUNIT DUO1''},
    ''pfam'': {''PF08651'': ''DASH complex subunit Duo1''}}. Exact DASH subunit family,
    corroborated by its maintained reviewed example xref.'
  snapshot_sha256: dc49b81735a919fb95e01072696d4e934071d88d5ac04a11b1c8ffa3c035803c
- evidence_id: micro-ipr-IPR013962-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013962/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013962-retry.raw
  accessed_at: '2026-11-04T04:49:54.603560Z'
  support: supports
  summary: 'IPR013962: {''name'': ''DASH complex subunit Dam1'', ''short'': ''DASH_Dam1''};
    type family; signatures {''panther'': {''PTHR28113'': ''DASH COMPLEX SUBUNIT DAM1''},
    ''pfam'': {''PF08653'': ''DASH complex subunit Dam1''}}. Exact DASH subunit family,
    corroborated by its maintained reviewed example xref.'
  snapshot_sha256: 03679715a1405b6ac0cf16387d2d44580ad0881978fb27e6a6d2e73b28238741
- evidence_id: micro-ipr-IPR013958
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013958/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013958.raw
  accessed_at: '2026-11-04T04:49:31.279369Z'
  support: supports
  summary: 'IPR013958: {''name'': ''DASH complex subunit Dad1'', ''short'': ''DASH_Dad1''};
    type family; signatures {''panther'': {''PTHR28025'': ''DASH COMPLEX SUBUNIT DAD1''},
    ''pfam'': {''PF08649'': ''DASH complex subunit Dad1''}}. Exact DASH subunit family,
    corroborated by its maintained reviewed example xref.'
  snapshot_sha256: e4e0c0579face568e6684609690c5c0064b841b0182860973dae0030d8395ad0
- evidence_id: micro-ipr-IPR013963-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013963/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013963-retry.raw
  accessed_at: '2026-11-04T04:49:54.742934Z'
  support: supports
  summary: 'IPR013963: {''name'': ''DASH complex subunit Dad2'', ''short'': ''DASH_Dad2''};
    type family; signatures {''panther'': {''PTHR28036'': ''DASH COMPLEX SUBUNIT DAD2''},
    ''pfam'': {''PF08654'': ''DASH complex subunit Dad2''}}. Exact DASH subunit family,
    corroborated by its maintained reviewed example xref.'
  snapshot_sha256: 3043213ccc4a851ac47e28170c2eacd0bc18116c2270c997be26607d7378f9b6
- evidence_id: micro-ipr-IPR013964
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013964/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013964.raw
  accessed_at: '2026-11-04T04:49:31.569969Z'
  support: supports
  summary: 'IPR013964: {''name'': ''DASH complex subunit Ask1'', ''short'': ''DASH_Ask1''};
    type family; signatures {''panther'': {''PTHR28200'': ''DASH COMPLEX SUBUNIT ASK1''},
    ''pfam'': {''PF08655'': ''DASH complex subunit Ask1''}}. Exact DASH subunit family,
    corroborated by its maintained reviewed example xref.'
  snapshot_sha256: 0d0e1b5de722b3a91425d4cee025dc6042d341c59f4f038d5869bc97fa4156b3
- evidence_id: micro-ipr-IPR013251
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013251/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013251.raw
  accessed_at: '2026-11-04T04:49:31.049437Z'
  support: supports
  summary: 'IPR013251: {''name'': ''DASH complex subunit Spc19'', ''short'': ''DASH_Spc19''};
    type family; signatures {''panther'': {''PTHR28262'': ''DASH COMPLEX SUBUNIT SPC19''},
    ''pfam'': {''PF08287'': ''Spc19''}}. Exact DASH subunit family, corroborated by
    its maintained reviewed example xref.'
  snapshot_sha256: 7f5599d0bbf370bd1b881f7efb0b2175864aafc607e8b7402b24c3884191a0e3
- evidence_id: micro-ipr-IPR013966-retry2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013966/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013966-retry2.raw
  accessed_at: '2026-11-04T04:52:50.441743Z'
  support: supports
  summary: 'IPR013966: {''name'': ''DASH complex subunit Spc34'', ''short'': ''Spc34''};
    type family; signatures {''pfam'': {''PF08657'': ''DASH complex subunit Spc34''}}.
    Exact DASH subunit family, corroborated by its maintained reviewed example xref.'
  snapshot_sha256: 1fed3846b15e95eb45ce7af34fea0477cc8d759e6966a894d139b1d69752dfd3
- evidence_id: micro-ipr-IPR051590
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051590/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR051590.raw
  accessed_at: '2026-11-04T04:49:32.947807Z'
  support: supports
  summary: 'IPR051590: {''name'': ''DDK kinase regulatory subunit Dbf4'', ''short'':
    ''Dbf4''}; type family; signatures {''panther'': {''PTHR15375'': ''DNA Replication
    Regulatory Kinase Subunit''}}. Exact Dbf4 family/signature with P32325 xref; generated
    description is not used as experimental evidence.'
  snapshot_sha256: 71598035654916de449d61ac770f59cd4c3f98162e6fc56b7c793b03c7891e85
- evidence_id: micro-ipr-IPR013939
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013939/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR013939.raw
  accessed_at: '2026-11-04T04:49:31.404383Z'
  support: context_only
  summary: 'IPR013939: {''name'': ''Regulatory subunit Dfp1/Him1, central region'',
    ''short'': ''Regulatory_Dfp1/Him1''}; type domain; signatures {''pfam'': {''PF08630'':
    ''Dfp1/Him1, central region''}}. Dbf4 central-region domain, not an exact whole-protein
    family.'
  snapshot_sha256: 6c60bd0155bc50711d42b3a15809d8eeaff6ce63784134859a2e9b3482f800f4
- evidence_id: micro-ipr-IPR024826-retry2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024826/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR024826-retry2.raw
  accessed_at: '2026-11-04T04:52:50.252821Z'
  support: context_only
  summary: 'IPR024826: {''name'': ''DNA polymerase delta/II small subunit family'',
    ''short'': ''DNA_pol_delta/II_ssu''}; type family; signatures {''panther'': {''PTHR10416'':
    ''DNA POLYMERASE DELTA SUBUNIT 2''}}. Family explicitly spans eukaryotic Polδ
    and archaeal PolII small subunits; broader than the specifically named Pol31 class
    despite the P46957 xref. No new confirmed finding.'
  snapshot_sha256: 44ca7da0d7b46dfaba6049af96e41bb15c0054421278767145190c5705bc57a2
- evidence_id: micro-ipr-IPR050240
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050240/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR050240.raw
  accessed_at: '2026-11-04T04:49:32.488205Z'
  support: context_only
  summary: 'IPR050240: {''name'': ''DNA polymerase type-B'', ''short'': ''DNA_pol_type-B''};
    type family; signatures {''panther'': {''PTHR10322'': ''DNA polymerase type-B''}}.
    Type-B polymerase family is broader than Pol3; generated biological prose not
    used.'
  snapshot_sha256: e4d65d9f86a12d9090e4c96e9859946f2b53deb1241bb4aeddf412b12feaa574
- evidence_id: micro-ipr-IPR019038-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019038/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR019038-retry.raw
  accessed_at: '2026-11-04T04:49:54.635844Z'
  support: context_only
  summary: 'IPR019038: {''name'': ''DNA polymerase delta subunit 3'', ''short'': ''POLD3''};
    type family; signatures {''pfam'': {''PF09507'': ''DNA polymerase subunit Cdc27''},
    ''panther'': {''PTHR17598'': ''DNA POLYMERASE DELTA SUBUNIT 3''}}. Named POLD3/Cdc27
    family is a candidate, but no current P47110 xref establishes the budding-yeast
    Pol32 assignment. No exhaustive absence claim.'
  snapshot_sha256: b98b2422d08e00f80f798e6dedf126c172d2b6e15794074efe67f0a8449db212
- evidence_id: micro-ipr-IPR023070-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023070/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR023070-retry.raw
  accessed_at: '2026-11-04T04:49:54.547333Z'
  support: supports
  summary: 'IPR023070: {''name'': ''DnaA initiator-associating protein'', ''short'':
    ''DiaA''}; type family; signatures {''ncbifam'': {''NF008138'': ''DnaA initiator-associating
    protein DiaA''}, ''hamap'': {''MF_01157'': ''DnaA initiator-associating protein
    DiaA [diaA]''}}. Exact DiaA family with DiaA-specific HAMAP/NCBIfam signatures
    and P66817 xref.'
  snapshot_sha256: c5275aa409e4b1a32d39fa8f2a4391a55b775b1ae202b101e475f3b14d298ca2
- evidence_id: micro-ipr-IPR035461
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035461/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR035461.raw
  accessed_at: '2026-11-04T04:49:32.297234Z'
  support: context_only
  summary: 'IPR035461: {''name'': ''GmhA/DiaA'', ''short'': ''GmhA/DiaA''}; type family;
    signatures {''cdd'': {''cd05006'': ''SIS_GmhA''}}. Broader GmhA/DiaA grouping,
    not a substitute for the exact DiaA family.'
  snapshot_sha256: 66390747d279a9b308ba9fad6f8831cc3f1c7a3f92bfe906c4222e9262956c9b
- evidence_id: micro-ipr-IPR050099-retry2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050099/
  locator: Complete native name/type/hierarchy/integrated signatures and description
    scope/curation flags; generated prose excluded; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ipr-IPR050099-retry2.raw
  accessed_at: '2026-11-04T04:52:50.299227Z'
  support: context_only
  summary: 'IPR050099: {''name'': ''SIS family GmhA and DiaA subfamilies'', ''short'':
    ''SIS_GmhA/DiaA_subfam''}; type family; signatures {''panther'': {''PTHR30390'':
    ''SIS family GmhA and DiaA subfamilies''}}. Broader GmhA/DiaA grouping, not a
    substitute for the exact DiaA family.'
  snapshot_sha256: f58928e6efc4480cce5a0e6edee93c650fbca6a5edbd8503e5047db9ddb67b37
- evidence_id: micro-pmid-11568188
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11568188+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-11568188.raw
  accessed_at: '2026-11-04T04:49:29.556061Z'
  support: supports
  summary: '11568188: Structure of DNA polymerase delta from Saccharomyces cerevisiae.;
    DOI 10.1074/jbc.m108842200. Primary-study abstract read completely. This metadata/abstract
    tier does not certify the full body, raw images or detailed experimental preparations.'
  snapshot_sha256: 256fc07acc82a5985112cb121126c935b00e428df37c9eed1dede4a8ec358392
- evidence_id: micro-pmid-11698664
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11698664+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-11698664.raw
  accessed_at: '2026-11-04T04:49:29.594774Z'
  support: supports
  summary: '11698664: Yeast Dam1p has a role at the kinetochore in assembly of the
    mitotic spindle.; DOI 10.1073/pnas.241417098. Primary-study abstract read completely.
    This metadata/abstract tier does not certify the full body, raw images or detailed
    experimental preparations.'
  snapshot_sha256: b3afb2200c3fff31ce3066e3b6e6ae9d7c355e69811afda68b1a89c2e2b9180d
- evidence_id: micro-pmid-11782438
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11782438+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-11782438.raw
  accessed_at: '2026-11-04T04:49:29.901882Z'
  support: supports
  summary: '11782438: Four new subunits of the Dam1-Duo1 complex reveal novel functions
    in sister kinetochore biorientation.; DOI 10.1093/emboj/21.1.181. Primary-study
    abstract read completely. This metadata/abstract tier does not certify the full
    body, raw images or detailed experimental preparations.'
  snapshot_sha256: 4350b5ecf421f14674d6203f3772194b72175cd47bafc4489fa5081cc3dc72de
- evidence_id: micro-pmid-12045100
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12045100+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-12045100.raw
  accessed_at: '2026-11-04T04:49:29.926022Z'
  support: supports
  summary: '12045100: DNA replication in eukaryotic cells.; DOI 10.1146/annurev.biochem.71.110601.135425.
    Secondary review abstract read completely. This metadata/abstract tier does not
    certify the full body, raw images or detailed experimental preparations.'
  snapshot_sha256: 68bda6f2c681d72ccb11810dd38b22ea6a10bbf813103e271e0e49bd5835eeb0
- evidence_id: micro-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-14562095.raw
  accessed_at: '2026-11-04T04:49:30.249997Z'
  support: supports
  summary: '14562095: Global analysis of protein localization in budding yeast.; DOI
    10.1038/nature02026. Primary-study abstract read completely. This metadata/abstract
    tier does not certify the full body, raw images or detailed experimental preparations.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: micro-pmid-17699754
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17699754+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-17699754.raw
  accessed_at: '2026-11-04T04:49:30.403479Z'
  support: supports
  summary: '17699754: The interaction of DiaA and DnaA regulates the replication cycle
    in E. coli by directly promoting ATP DnaA-specific initiation complexes.; DOI
    10.1101/gad.1561207. Primary-study abstract read completely. This metadata/abstract
    tier does not certify the full body, raw images or detailed experimental preparations.'
  snapshot_sha256: 003c2681f7e0c0626862cc558c5b27d0d1ec39e97a212b775824a063be0b12ae
- evidence_id: micro-pmid-21256019
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21256019+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-21256019.raw
  accessed_at: '2026-11-04T04:49:30.648020Z'
  support: supports
  summary: '21256019: The Ndc80 loop region facilitates formation of kinetochore attachment
    to the dynamic microtubule plus end.; DOI 10.1016/j.cub.2010.12.050. Primary-study
    abstract read completely. This metadata/abstract tier does not certify the full
    body, raw images or detailed experimental preparations.'
  snapshot_sha256: ff41545ee6d5006c893b01515da4af1c67d0f8f12f11b6ec00643e16dde16c41
- evidence_id: micro-pmid-25236177
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25236177+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-25236177.raw
  accessed_at: '2026-11-04T04:49:30.537596Z'
  support: supports
  summary: '25236177: Kinetochores require oligomerization of Dam1 complex to maintain
    microtubule attachments against tension and promote biorientation.; DOI 10.1038/ncomms5951.
    Primary-study abstract read completely. This metadata/abstract tier does not certify
    the full body, raw images or detailed experimental preparations.'
  snapshot_sha256: 879c9a3686343705c5b0b05211a4ba2fed0463e5648bad7f70ee1df301078528
- evidence_id: micro-pmid-36701236
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36701236+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-36701236.raw
  accessed_at: '2026-11-04T04:49:30.580054Z'
  support: supports
  summary: '36701236: Single-copy locus proteomics of early- and late-firing DNA replication
    origins identifies a role of Ask1/DASH complex in replication timing control.;
    DOI 10.1016/j.celrep.2023.112045. Primary-study abstract read completely. This
    metadata/abstract tier does not certify the full body, raw images or detailed
    experimental preparations.'
  snapshot_sha256: 0b0c3e697d62907e38f2a44265059e3cf35df7dc3b43b174a12213895561387d
- evidence_id: micro-pmid-9677405
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677405+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-9677405.raw
  accessed_at: '2026-11-04T04:49:30.914363Z'
  support: supports
  summary: '9677405: Characterization of the two small subunits of Saccharomyces cerevisiae
    DNA polymerase delta.; DOI 10.1074/jbc.273.31.19747. Primary-study abstract read
    completely. This metadata/abstract tier does not certify the full body, raw images
    or detailed experimental preparations.'
  snapshot_sha256: 958083a29a982747b4315a52b8e765ffaa18dd47627d79ae9e9a23d6f3b922ab
- evidence_id: micro-pmid-9677406
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9677406+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-9677406.raw
  accessed_at: '2026-11-04T04:49:30.782619Z'
  support: supports
  summary: '9677406: Structure and processivity of two forms of Saccharomyces cerevisiae
    DNA polymerase delta.; DOI 10.1074/jbc.273.31.19756. Primary-study abstract read
    completely. This metadata/abstract tier does not certify the full body, raw images
    or detailed experimental preparations.'
  snapshot_sha256: 82bbadf8d9bffe7057bc8336f446ce6a785c671a35c87e6728381e199c43a355
- evidence_id: micro-pmid-9817759
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9817759+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete exact MED title/authors/year/DOI and full deposited abstract;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/pmid-9817759.raw
  accessed_at: '2026-11-04T04:49:30.905513Z'
  support: supports
  summary: '9817759: Saccharomyces cerevisiae Duo1p and Dam1p, novel proteins involved
    in mitotic spindle function.; DOI 10.1083/jcb.143.4.1029. Primary-study abstract
    read completely. This metadata/abstract tier does not certify the full body, raw
    images or detailed experimental preparations.'
  snapshot_sha256: 7a635c8f6e45fe9fca5a097acaf025734768d10ce492024e50f75672154fbeb5
- evidence_id: micro-miranda2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb896%22&format=json&resultType=core&pageSize=25
  locator: Exact DOI-selected MED metadata and complete primary abstract; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/miranda2005-meta.raw
  accessed_at: '2026-11-04T04:49:55.002751Z'
  support: supports
  summary: '15640796: The yeast DASH complex forms closed rings on microtubules..
    Recombinant ten-subunit E.coli expression and microtubule-associated rings/helices
    support bounded DASH assembly context; no raw EM inspected.'
  snapshot_sha256: fed2bc12e1c579714f4d187e4e7d59c4a7f50c671e9d3be9751ea24059e151ee
- evidence_id: micro-li2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FMCB.25.2.767-778.2005%22&format=json&resultType=core
  locator: Exact DOI-selected MED metadata and complete primary abstract; exact retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-meta.raw
  accessed_at: '2026-11-04T04:54:57.729215Z'
  support: supports
  summary: '15632076: Genetic analysis of the kinetochore DASH complex reveals an
    antagonistic relationship with the ras/protein kinase A pathway and a novel subunit
    required for Ask1 association.. Hsk2/Hsk3 microproteins and reduced Ask1-associated
    complex recovery in hsk3 mutants support the retained small-subunit boundary question.
    No new universal microprotein identity or current full-body read is claimed.'
  snapshot_sha256: 23b24e706aa69e8d8241bc4324a372628458097c73e84f52152353f6a14074bc
- evidence_id: micro-cheeseman2001-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2199314.1/PMC2199314.1.xml
  locator: Genuine JATS Introduction; Results first composition/stoichiometry, phosphorylation,
    microtubule-binding, localization subsections; Discussion; Methods strains/TableII,
    purification, mass spectrometry, microscopy and binding assay; Figures1–3/6 text
    captions, no pixels; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/cheeseman2001-jats.raw
  accessed_at: '2026-11-04T04:49:32.792577Z'
  support: supports
  summary: S288C-derived yeast purifications recover the seven declared proteins;
    approximate gel/biochemical stoichiometry and direct binding assay support the
    current constituent and outer-kinetochore outline. Unidentified small bands remain
    explicitly unresolved. Direct binding to bovine brain microtubules in vitro differs
    from native attachment and genetic-function inference.
  snapshot_sha256: a26c3a736836c2773adaa7641f1685d9869f767dafb8bdf25392dd269c55816b
- evidence_id: micro-janke2002-publisherpdf
  kind: primary_source
  reference: https://www.embopress.org/doi/pdf/10.1093/emboj/21.1.181
  locator: Genuine publisher PDF pp181–183 Introduction/first Results/Fig1 text caption;
    pp189–192 Discussion and TableI/Methods strain/purification sections. Extracted
    text, no figure pixels or supplementary experiments; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-publisherpdf.raw
  accessed_at: '2026-11-04T04:52:58.425360Z'
  support: supports
  summary: Dad2-ProA purification after4h37C from spc34-3 recovers only the bait while
    matched SPC34 recovers the seven-protein DDD assembly (p182 Fig1B). This is condition-specific
    association/recovery evidence, not universal essentiality, direct binding or viability.
    Subunit/kinetochore findings substantively support the seven new DASH constituent
    edges; strain derivatives and conditional-mutant context remain scoped.
  snapshot_sha256: 20ff5aa83ca106f519b03b39ea6c3133aa00129f88547d7f671ae8d3a393fe43
- evidence_id: micro-keyamura-retained-reader
  kind: primary_source
  reference: https://genesdev.cshlp.org/content/21/16/2083.full.pdf
  locator: 'Retained publisher-PDF web-reader text: lines0–44,257,290–296,323–347,370,373–379,417–446;
    only those supplied passages were reread. Reader reports older cached PDF; original
    network-fetch instant was not exposed/recorded. This timestamp is the current
    retained-text inspection, not fresh HTTP200. Terminal publisher routes returned403;
    later reader retry502.; retained /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-earlier-web-reader.json'
  accessed_at: '2026-11-04T04:58:49.655743Z'
  support: context_only
  summary: Scoped cached text corroborates active tetramer, DnaA/oriC binding and
    dilution-dependent dimer/tetramer interpretation. Methods names K12 derivatives;
    computational dataset strains are not that experimental panel. Phosphosugar regulation
    is explicitly speculative. No pixels, coordinates, full body or missing passages
    certified.
  snapshot_sha256: 2f96c9e6015173422747cceefa08b1aca9e3e2fa50e5d1367047504ae238ccdb
- evidence_id: micro-janke2002-jats-access
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC125813.1/PMC125813.1.xml
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-jats.raw
  accessed_at: '2026-11-04T04:49:32.684506Z'
  support: context_only
  summary: HTTP404; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: ab1588a5fc66342e67086dd8a3262d623c21b9b451dbd02bffbeecf550d0a9fc
- evidence_id: micro-janke2002-canonical-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC125813/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-canonical.raw
  accessed_at: '2026-11-04T04:49:53.772085Z'
  support: context_only
  summary: HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 4d33444edfc45f9eaf3bf26704415eab5ef6470ac983f52c6e6c279591bf4fbf
- evidence_id: micro-janke2002-epxml-access
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC125813/fullTextXML
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-epxml.raw
  accessed_at: '2026-11-04T04:49:54.233876Z'
  support: context_only
  summary: HTTP500; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: d3e75a0c621781f6411a1fd4ac3d2555f9fb9458fc3b02546aa98002f6355004
- evidence_id: micro-janke2002-bioc-access
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC125813/unicode
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/janke2002-bioc.raw
  accessed_at: '2026-11-04T04:49:53.768373Z'
  support: context_only
  summary: HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-li2005-jats-access
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC543429.1/PMC543429.1.xml
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-jats.raw
  accessed_at: '2026-11-04T04:49:32.887009Z'
  support: context_only
  summary: HTTP404; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: a56c73c5577cef2d7a0da9e15702d012ec8ea885036174ef44082c4fe9593bbb
- evidence_id: micro-li2005-canonical-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC543429/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-canonical.raw
  accessed_at: '2026-11-04T04:49:53.772129Z'
  support: context_only
  summary: HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 5eb838fe90487b70d507d23fd47fb1c5236e2ef9ba495bda2f0642c1cdcc40a1
- evidence_id: micro-li2005-epxml-access
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC543429/fullTextXML
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-epxml.raw
  accessed_at: '2026-11-04T04:49:54.344691Z'
  support: context_only
  summary: HTTP500; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: f35a64f4a4f6b3807aeb6468211256ab4dbe29cc61285c047d80acfdbabed17c
- evidence_id: micro-li2005-bioc-access
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC543429/unicode
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/li2005-bioc.raw
  accessed_at: '2026-11-04T04:49:53.866968Z'
  support: context_only
  summary: HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-keyamura2007-jats-access
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC1948862.1/PMC1948862.1.xml
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-jats.raw
  accessed_at: '2026-11-04T04:49:32.815331Z'
  support: context_only
  summary: HTTP404; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 6084bc8a0e9ea98f036aeba4608742df66895e8617efa78216ef656c5315d0b7
- evidence_id: micro-keyamura2007-canonical-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1948862/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-canonical.raw
  accessed_at: '2026-11-04T04:49:53.786556Z'
  support: context_only
  summary: HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 5b7f6ca517946a0c65fdfa49bcc1252f2c7050078c82e02b6417bbedc703671b
- evidence_id: micro-keyamura2007-epxml-access
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1948862/fullTextXML
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-epxml.raw
  accessed_at: '2026-11-04T04:49:55.752354Z'
  support: context_only
  summary: HTTP500; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 45838e6651adcbd40a1818b7dd3dc60438c2a7566a8ed0261b1d74b8b25c5985
- evidence_id: micro-keyamura2007-bioc-access
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC1948862/unicode
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-bioc.raw
  accessed_at: '2026-11-04T04:49:54.148470Z'
  support: context_only
  summary: HTTP200; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-keyamura2007-publisherpdf-access
  kind: validation
  reference: https://genesdev.cshlp.org/content/21/16/2083.full.pdf
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-publisherpdf.raw
  accessed_at: '2026-11-04T04:52:49.825401Z'
  support: context_only
  summary: HTTP403; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 55144a2baa402558a04b340f939603627be3d4a842563febd9d833074ded2941
- evidence_id: micro-keyamura2007-publisherhtml-access
  kind: validation
  reference: https://genesdev.cshlp.org/content/21/16/2083.full
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-publisherhtml.raw
  accessed_at: '2026-11-04T04:54:56.711568Z'
  support: context_only
  summary: HTTP403; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: f6f9c64c4e8baf7bcac0518a8e39673e2e97084ca48d3101874d7a2a50b4d0b7
- evidence_id: micro-keyamura2007-pdf-query-access
  kind: validation
  reference: https://genesdev.cshlp.org/content/21/16/2083.full.pdf?download=1
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/keyamura2007-pdf-query.raw
  accessed_at: '2026-11-04T04:54:56.719372Z'
  support: context_only
  summary: HTTP403; absent S3 object, browser challenge, XML server error, BioC no-result
    or publisher403 as applicable. This response is not scientific body evidence;
    alternate genuine source reads are separately specified.
  snapshot_sha256: 83c22ca6d5a7f86a69e420f368b8f7a4ba5d8bd9b45ca54e09a354ad0a01b9ac
- evidence_id: micro-historical-complex49-agent-bell2002-publisher
  kind: validation
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev.biochem.71.110601.135425
  locator: Exact retained unsuccessful full-body access response
  accessed_at: '2026-10-22T05:18:09.394793Z'
  support: context_only
  summary: Publisher HTML returnedHTTP403; no Bell/Dutta body is certified. Native
    GO directly supports the maintained DDK definition and coarse function. Retained
    original timestamp/hash only; no new retrieval claimed. Original database kind
    is corrected to validation/context_only in this successor source report.
  snapshot_sha256: bd10bd4fd536a09aa73eaa6742583324d58d75ad9a8eaa36271de5ebefdc1fde
- evidence_id: micro-historical-complex49-agent-burgers1998-pdf
  kind: validation
  reference: https://www.jbc.org/article/S0021925818491673/pdf
  locator: Exact retained unsuccessful full-body access response
  accessed_at: '2026-10-22T05:18:09.394275Z'
  support: context_only
  summary: Publisher PDF route returnedHTTP403 rather than PDF. Only the complete
    native Burgers/Gerik abstract is certified here. Retained original timestamp/hash
    only; no new retrieval claimed. Original database kind is corrected to validation/context_only
    in this successor source report.
  snapshot_sha256: d58db1e26234f9fb77a679cc7bbf637b97222748503d7ad270bca9da99c06144
- evidence_id: micro-historical-complex49-agent-johansson2001-doi
  kind: validation
  reference: https://doi.org/10.1074/jbc.M108842200
  locator: Exact retained unsuccessful full-body access response
  accessed_at: '2026-10-22T05:18:09.394671Z'
  support: context_only
  summary: The DOI route failed TLS certificate verification with status0; no Johansson
    full body is certified. Its complete native abstract directly states the 1:1:1
    monomer conclusion and the tested concentration range. Retained original timestamp/hash
    only; no new retrieval claimed. Original database kind is corrected to validation/context_only
    in this successor source report.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T04:49:31.986519Z'
  support: supports
  summary: 'All20 organism rows inspected: no natural Saccharomyces/yeast match, while
    E.coli precise1k is available. Catalogue noncoverage does not refute biology;
    no bacterial proxy for yeast.'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB GET /api/datasets at 2026-11-04T04:49:31.986519Z; complete20
    returned organism rows and all named datasets, no pagination/truncation; literal
    yeast/Saccharomyces/E.coli host names/keys checked. Scope is this snapshot only.
- evidence_id: micro-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete e_coli/precise1k metadata; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T04:49:55.057751Z'
  support: context_only
  summary: Five strains BW25113,DGF-298,GMOS,MG1655,W3110;1035 samples,201 modules,4257
    genes. This selected K12-related dataset is not the Keyamura KH5402-1/NA/KA mutant
    panel and does not establish assembly.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-ecoli-modules
  kind: search
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete201 module-list metadata, names/regulators/functions; activity/generated
    narratives not assessed; exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T04:49:54.811461Z'
  support: context_only
  summary: Selected precise1k list contains201 entries; no title-only inference of
    DiaA regulation. Exact gene membership is separately evaluated.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: iModulonDB e_coli/precise1k /imodulons at 2026-11-04T04:49:54.811461Z,
    all201 returned entries; no other dataset, experimental activity condition or
    future state covered.
- evidence_id: micro-ecoli-gene-b3149
  kind: search
  reference: https://imodulondb.org/api/genes/b3149/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 actual weight/threshold/in_imodulon rows for verified b3149/diaA;
    exact retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/ecoli-gene-b3149.raw
  accessed_at: '2026-11-04T04:52:49.654380Z'
  support: context_only
  summary: b3149 is returned but none of201 module flags is positive. Largest absolute
    weight is -0.037670615 for module112 versus threshold0.060574417; no matched module
    warrants a causal or assembly conclusion. This is bounded computational nonmembership,
    not gene absence or physiological dispensability.
  snapshot_sha256: c94cd2e4f0f8b59ff34426409a64d7d08a0aabc948e32a5d2e461ed4bf59f838
  search_scope: iModulonDB GET https://imodulondb.org/api/genes/b3149/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T04:52:49.654380Z; exact native locus b3149 selected from P66817,
    all201 returned rows inspected/evaluated; five-strain precise1k only. No alias,
    other dataset or universal nonmembership claim.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z command receipt
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical unavailable runner/exit1 permission limitation only; no new
    invocation claimed. Fresh official source API fallback is separately inspected.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-dash_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:49:06.912873Z'
  support: supports
  summary: 'Actual exit0: 7 reviewed examples and 7 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: e43db5ccd928659f376f3fe6c7e6fb0b228d2968f8f729b32c2f084ac95e6ff6
- evidence_id: micro-native-dash_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-causal.log
    SHA256 35cc550c1a6115a14b841486e6313e1c723b4a77074deb16b03f416b463ef28f
  accessed_at: '2026-11-04T04:49:07.395326Z'
  support: supports
  summary: 'Actual exit0: 7 reviewed examples and 7 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: 94a6b73883add982d796dbc05276898169ff1108106d61d0de903a6a0801274f
- evidence_id: micro-native-dbf4_dependent_protein_kinase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:49:09.144538Z'
  support: supports
  summary: 'Actual exit0: 2 reviewed examples and 2 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: 7feb431c7926bd7afa4cfb06c13440b7aa7517c42b8bcc37425d70ffc53d0b1b
- evidence_id: micro-native-dbf4_dependent_protein_kinase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-causal.log
    SHA256 69d4848530843f3d8b7c8651b0f217032da1f2bf11e09fa36969ee325d9ef6df
  accessed_at: '2026-11-04T04:49:09.610072Z'
  support: supports
  summary: 'Actual exit0: 2 reviewed examples and 2 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: ba389e0e6d0c803b7f56bc554b56708414f0f40dad4243b807d68f3f9f906bfe
- evidence_id: micro-native-delta_dna_polymerase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:49:12.737597Z'
  support: supports
  summary: 'Actual exit0: 3 reviewed examples and 3 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: d2b74c44445a96868059f9ece3bc56c86c86cf1c2bcde0e2bdf4563ad80a1d3f
- evidence_id: micro-native-delta_dna_polymerase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-causal.log
    SHA256 9d47952c8ac17bd446c4fab095faa0a2308bb3d31ccca4a3cc88179ae930d58e
  accessed_at: '2026-11-04T04:49:13.162852Z'
  support: supports
  summary: 'Actual exit0: 3 reviewed examples and 3 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: 3b37480267489500b755f8754057cf2cda1127da9bac2cd0c4fb766e724735e0
- evidence_id: micro-native-diaa_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:49:14.737192Z'
  support: supports
  summary: 'Actual exit0: 1 reviewed examples and 1 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: ef3cb10bd845f97404fcdf2fd93edc32937dc280b2fa224326e7c42e64273953
- evidence_id: micro-native-diaa_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-causal.log
    SHA256 5003812ac51deab9d43f38ec02f6deacaac1afb55770013f583b65a26c758057
  accessed_at: '2026-11-04T04:49:15.158734Z'
  support: supports
  summary: 'Actual exit0: 1 reviewed examples and 1 COVERED typed nodes. Implemented
    accession/graph-example coverage is not full biological verification or exact
    family completeness.'
  snapshot_sha256: 165aa0014021fe59fb330203105c10b5067a9da800b7855bc7e3aec6eabe44e3
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/other/cvt_complex.yaml
  locator: Entire current maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
  summary: Entire target read including definition, component/examples, taxon/functional
    scope, graph, discussions and append-only history. Unchanged original target bytes.
  support: supports
- evidence_id: plaque-original-1-yaml
  kind: prior_review
  reference: reviews/structured/20261022T052917Z-cvt-complex-audit/review.yaml
  locator: Complete historical pair and native deterministic-render comparison
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 2fb8cfb272e8afe4f72557d1cddc970c9b22bdefa5d8f478b5c2e41f7fc6cfdf
  summary: Original source scope, verdict, F1 and actions independently reassessed.
    Historical checks are not claimed as fresh executions.
  support: supports
- evidence_id: plaque-original-1-md
  kind: prior_review
  reference: reviews/structured/20261022T052917Z-cvt-complex-audit/review.md
  locator: Complete historical pair and native deterministic-render comparison
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: ce55b72871f05e0922e794e1f161ddd615a33d96a96c6e199df773105a58564e
  summary: Original source scope, verdict, F1 and actions independently reassessed.
    Historical checks are not claimed as fresh executions.
  support: supports
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/other/cytostome.yaml
  locator: Entire current maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 083f8800483f67a23bdb303aaf95d8d853d3bf67240e7ac2926e87ab66c89926
  summary: Entire target read including definition, component/examples, taxon/functional
    scope, graph, discussions and append-only history. Changed hierarchy/evidence/history
    substantively reassessed against fresh GO; other fields unchanged.
  support: supports
- evidence_id: plaque-original-2-yaml
  kind: prior_review
  reference: reviews/structured/20261022T052918Z-cytostome-audit/review.yaml
  locator: Complete historical pair and native deterministic-render comparison
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: e7269333148c97132c8c73c1855585cb68f1d167318c06ba613d84088df732d8
  summary: Original source scope, verdict, F1 and actions independently reassessed.
    Historical checks are not claimed as fresh executions.
  support: supports
- evidence_id: plaque-original-2-md
  kind: prior_review
  reference: reviews/structured/20261022T052918Z-cytostome-audit/review.md
  locator: Complete historical pair and native deterministic-render comparison
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: ec3b6bc61fb8a056080290217cde937a82411545ac2753c11d1ab08a80fcac7a
  summary: Original source scope, verdict, F1 and actions independently reassessed.
    Historical checks are not claimed as fresh executions.
  support: supports
- evidence_id: plaque-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen native policy read and applied
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Exact classes, constituent versus machinery, formation versus function,
    optional fields and append-only rationale.
  support: supports
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native policy read and applied
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Native parent is-a versus part_of, component/example and graph-type rules.
  support: supports
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native policy read and applied
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Positive molecular or pathway claims trigger bounded structured-source
    applicability assessment.
  support: supports
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen native policy read and applied
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Issue-bearing and evidence-backed-disposition batch route; immutable originals.
  support: supports
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen native policy read and applied
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Native evidence kinds, assessment enums, exact predecessor and disposition
    requirements.
  support: supports
- evidence_id: plaque-checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native policy read and applied
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
  summary: Whole-record field-by-field claims, scope and completeness; no mandatory
    optional enrichment.
  support: supports
- evidence_id: plaque-reservosome-context
  kind: record_content
  reference: data/structures/membrane_organelle/reservosome.yaml
  locator: Identifier/definition and cargo-receiving graph boundary; frozen before
    reading
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: c1a9daf798668ddf44d05a61e4ef589754275f4d385f1560ce38ccab0c07cdfa
  summary: Exact minted destination resolves to posterior membrane-bounded endocytic
    organelle receiving T.cruzi epimastigote cargo. Bounded dependency check only;
    no other reservosome findings or historical issue dispositions inferred.
  support: context_only
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034270,GO:0032991,GO:0005737,GO:0032258,GO:0033107,GO:0031910,GO:0110165,GO:0005886
  locator: All requested id/name/isObsolete/definition/synonym fields; exact relevant
    typed children, not every descendant; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/go.raw
  accessed_at: '2026-11-04T04:51:44.546359Z'
  snapshot_sha256: 772bb743a6091dbcef417bd96a96c81e1e4145b8e36cf08d74f0e479a5908de7
  summary: Eight active exact GO identities and definitions inspected. GO0031910 is
    a direct is_a child of GO0110165 and part_of child of GO0005886. GO0034270 short
    preApe1 definition is preserved as an authority scope conflict with GO0032258
    explicit Atg19-containing Cvt complex definition, not alleged to be a misquotation.
  support: supports
- evidence_id: plaque-cytostome-path
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031910/paths/GO:0005886
  locator: Complete exact endpoint path response; one path/one edge; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/cytostome-path.raw
  accessed_at: '2026-11-04T04:51:45.838745Z'
  snapshot_sha256: cfc6d89a6d75870297d55a78f47aa041ddc15ee58aa145f35fb405adc491bdbb
  summary: The exact returned path has one direct part_of edge from cytostome GO0031910
    to plasma membrane GO0005886.
  support: supports
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Complete requested taxon native identity and lineage; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/tax-4932.raw
  accessed_at: '2026-11-04T04:51:45.086123Z'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
  summary: Exact taxon identity/name/rank/lineage verified; S.cerevisiae S288C is
    the accession reference strain, not silently the experimental SEY6210 background,
    and T.cruzi Y is the Chasen experimental strain.
  support: supports
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Complete requested taxon native identity and lineage; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/tax-559292.raw
  accessed_at: '2026-11-04T04:51:45.089539Z'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
  summary: Exact taxon identity/name/rank/lineage verified; S.cerevisiae S288C is
    the accession reference strain, not silently the experimental SEY6210 background,
    and T.cruzi Y is the Chasen experimental strain.
  support: supports
- evidence_id: plaque-tax-5693
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5693.json
  locator: Complete requested taxon native identity and lineage; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/tax-5693.raw
  accessed_at: '2026-11-04T04:51:44.170349Z'
  snapshot_sha256: 2e618b0b54c95e80c64d166e7612664c9f41e9c60c0b54aaeb6aebcd764d210a
  summary: Exact taxon identity/name/rank/lineage verified; S.cerevisiae S288C is
    the accession reference strain, not silently the experimental SEY6210 background,
    and T.cruzi Y is the Chasen experimental strain.
  support: supports
- evidence_id: plaque-protein-P14904
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P14904.json
  locator: Full identity/genes/taxon/status, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/PTM/SIMILARITY
    comments and evidence joins; sequence length and InterPro cross-references; response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/protein-P14904.raw
  accessed_at: '2026-11-04T04:51:44.505001Z'
  snapshot_sha256: 101800e42ac6ed3ee037cd16805c1cfa9d77c5a48d953dee6ee62bd4b47df10e
  summary: Reviewed P14904, APE1 primary symbol, API/LAP4/YSC1 aliases and YKL103C
    locus, 514aa precursor in strain559292 agree. FUNCTION and SUBUNIT independently
    distinguish precursor multimers, ATG19 binding/cargo-receptor complex and mature
    vacuolar enzyme. Exact three localization PMID joins are present.
  support: supports
- evidence_id: plaque-gene-APE1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned exact gene-query rows; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/gene-APE1.raw
  accessed_at: '2026-11-04T04:51:46.317977Z'
  snapshot_sha256: 9b1594b5e048a7edb46f843511071f749498af749ea42a1a972c16aa12787720
  summary: Exact reviewed S288C APE1 query returns P14904 alone; identity does not
    itself prove Cvt membership.
  support: supports
  search_scope: UniProtKB REST; https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    exact gene APE1, organism559292, reviewed:true, size100; fetched 2026-11-04T04:51:46.317977Z;
    one returned row independently inspected, no other taxon or unreviewed search
    asserted.
- evidence_id: plaque-ipr-IPR001948
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001948/
  locator: Complete metadata/name/type/hierarchy/curated description; compared to
    P14904 native xrefs; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/ipr-IPR001948.raw
  accessed_at: '2026-11-04T04:51:46.284067Z'
  snapshot_sha256: 37c628cee1eaedb989894d8b4f1a708c4a5d59cd626c2a7c0d2b456d1bdee3e8
  summary: Peptidase M18 is a broad family encompassing aminopeptidases; it does not
    exactly denote the yeast precursor Cvt cargo subclass. Existing deferred exact
    grounding remains bounded, not a missing-family finding.
  support: supports
- evidence_id: plaque-ipr-IPR023358
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023358/
  locator: Complete metadata/name/type/description/hierarchy; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/ipr-IPR023358.raw
  accessed_at: '2026-11-04T04:51:45.706105Z'
  snapshot_sha256: 495ead89923cda97bb3458f3f175f7f5c1343394ca5b70b3e1854f88b9a6d8cb
  summary: Peptidase M18 domain2 is a homologous superfamily/structural domain, not
    exact whole-protein precursor-cargo identity.
  support: supports
- evidence_id: plaque-paper-0
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fs1097-2765%2801%2900263-5%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-0.raw
  accessed_at: '2026-11-04T04:51:44.443441Z'
  snapshot_sha256: a43530586c2de8d532f438e285ed7d16b057a4156fdd5e8c6e3d868cec72b4e5
  summary: 'Scott2001 primary abstract: Cvt19 binds precursor API, travels with it
    to vacuole, and is selectively required for Cvt cargo transport.'
  support: supports
- evidence_id: plaque-paper-1
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M404399200%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-1.raw
  accessed_at: '2026-11-04T04:51:44.477933Z'
  snapshot_sha256: 87f3082de9e7fee410092bea397638e1100324642c73264ceaec2f843700bee8
  summary: Shintani2004 primary abstract explicitly defines the Ape1 plus Atg19 cargo-receptor
    Cvt complex and separates Atg11 PAS delivery; nutrient/vesicle scope is retained.
  support: supports
- evidence_id: plaque-paper-2
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24493041+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-2.raw
  accessed_at: '2026-11-04T04:51:44.463600Z'
  snapshot_sha256: 367444d8ce04b924410a0ecc69dd9130cc9aef0adee07af7a87ce423c136316a
  summary: Matile1971 abstract supports a vacuolar aminopeptidase isozyme and growth-condition
    effects; not a specific Cvt-complex assembly assay.
  support: supports
- evidence_id: plaque-paper-3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A363165+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-3.raw
  accessed_at: '2026-11-04T04:51:45.077615Z'
  snapshot_sha256: 24b5bc4c297cec8c588ac185b053f9445f716462c9485d233c677842a65ff6b7
  summary: Frey1978 abstract supports vacuolar aminopeptidaseI localization and distinguishes
    aminopeptidaseII; no Cvt receptor membership inferred.
  support: supports
- evidence_id: plaque-paper-4
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8601598+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-4.raw
  accessed_at: '2026-11-04T04:51:45.624986Z'
  snapshot_sha256: a93c91151b73d7217b999b523bcaf51e6da5485d09a09a1765eb88c24376931c
  summary: Oda1996 abstract supports precursor propeptide-dependent vacuolar targeting
    and distinguishes transport defects from folding; body/scans not inspected.
  support: supports
- evidence_id: plaque-paper-5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1006%2Fexpr.1999.4419%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-5.raw
  accessed_at: '2026-11-04T04:51:45.398193Z'
  snapshot_sha256: 2ff8559123e88cc74ca5c66fed4d4ba1b16d5e17838b00fe33af1ef85f7cc2cc
  summary: Okuda1999 abstract supports T.cruzi epimastigote cytostome-associated flagellar/cytoskeletal
    region; broad complex and opening not equated.
  support: supports
- evidence_id: plaque-paper-6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1078%2F0171-9335-00112%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-6.raw
  accessed_at: '2026-11-04T04:51:45.749240Z'
  snapshot_sha256: bcf34479d4be43dd6359c2d7be7fc0933c7b19c400e0ee8023d799f921e4fc59
  summary: Porto-Carreiro2000 complete primary abstract supports protein-cargo cytostome/cytopharynx
    entry, vesicular-tubular intermediate network and later reservosome storage. Early-endosome
    interpretation is based on uptake kinetics and pH; no new detailed lipid assay
    certified.
  support: supports
- evidence_id: plaque-paper-7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1242%2Fjcs.135491%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-7.raw
  accessed_at: '2026-11-04T04:51:45.702594Z'
  snapshot_sha256: b0564677f5a4161b57240d3647c96ba4c74c2cdc1c15bdfbaa415d33b27adad8
  summary: Alcantara2014 complete primary abstract explicitly identifies serial electron
    tomography/FIB-SEM and epimastigote complex reconstruction. No figure pixels or
    detailed Methods/strain beyond abstract certified.
  support: supports
- evidence_id: plaque-paper-8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.3389%2Ffcimb.2019.00445%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID matched complete MED identity/authors/year/title and indexed
    primary abstract; not a full-body claim; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/paper-8.raw
  accessed_at: '2026-11-04T04:51:45.199439Z'
  snapshot_sha256: 154bd82c7669ec41a40d5e6effee81ba6b7aca8ef56d6f63444f192e12c7616d
  summary: Chasen2020 primary abstract identifies endogenous CP1 tagging and CP1-associated
    CP2/3 localization across the broader cytostome-cytopharynx complex; detailed
    body scope separately inspected.
  support: supports
- evidence_id: plaque-scott2001-retained-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2767243/
  locator: Results S6/S8 with Fig4/6 captions, Discussion S12/S14, Methods S18/Table1/S24/S25;
    independently reread retained genuine HTML /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/scott2001-pmc-prefixed.html;
    no pixels/supplements
  accessed_at: '2026-11-03T11:52:44.702094Z'
  snapshot_sha256: a9adfeccab0e78afcae666a34064d14af638feb99cccb8ff591c114ecb03c8f1
  summary: Native co-IP and heterologous binding support precursor-specific Cvt19
    association and cotransport/degradation, unlike recycling receptors. SEY6210-derived
    experiments are distinguished from E.coli lysate/rabbit-reticulocyte binding,
    which is not a purified binary reconstitution. Actual retained retrieval was Nov3,
    not a fresh Nov4 body download.
  support: supports
- evidence_id: plaque-shintani2004-retained-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1712665/
  locator: Introduction S1; Methods S3/Table1; Results S8/S9 including Fig1-3 text
    captions; Discussion S10; independently reread retained genuine HTML /private/tmp/cellstructure-batches-2346-2397-20261103/pr2362/adversary-septin/shintani2004-pmc-prefixed.html;
    no pixels/supplements
  accessed_at: '2026-11-03T11:52:44.427793Z'
  snapshot_sha256: 034ed88ed78ea5ce5ac9e3d0a32d92406cb483b159c8326a0131af538d6efe15
  summary: Ape1 cargo core recruits Atg19 to form the Cvt complex; Ams1 is additional
    cargo, whereas Atg11 links cargo to PAS machinery. Nutrient-rich cargo/receptor
    deletion impairs PAS organization and vesicle transport, while starvation/rapamycin
    changes dependencies. This does not make every Atg factor a constituent. Actual
    retained retrieval was Nov3, not a fresh Nov4 body download.
  support: supports
- evidence_id: plaque-chasen2020-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6978632.1/PMC6978632.1.xml
  locator: Genuine JATS Results s5/all four subsections with Fig1-4 text captions;
    Discussion s6; Methods Parasite Cultures, Generation of Cloning Constructs, Endocytosis
    Assays, Immunoelectron Microscopy, s3 co-IP/MS; no figure pixels/supplement reanalysis;
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/chasen2020-s3.raw
  accessed_at: '2026-11-04T04:52:16.472337Z'
  snapshot_sha256: 8bcd86a574a7ec3e72cdefef0e9188ad08319a3d67579f2d4b74d6fc76274301
  summary: Y-strain CP1 endogenous tagging/immunoelectron localization and protein
    feeding support the broader endocytic complex. CP2/CP3 co-IP and overexpression
    localization do not establish an invariant three-subunit cytostome opening or
    deletion-based assembly necessity; predicted SMC/coiled-coil regions are not exact
    whole-protein families. Methods distinguish host-cell culture from parasite biological
    scope.
  support: supports
- evidence_id: plaque-porto2000-doi
  kind: database
  reference: https://api.crossref.org/v1/works/10.1078%2F0171-9335-00112/transform
  locator: Complete bibliographic response, not primary full text; response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/porto2000-doi.raw
  accessed_at: '2026-11-04T04:52:16.032022Z'
  snapshot_sha256: 2442c7a4ad59adbe75d6445ddaa785a8c88a46a02c6595f3c3bef9122f4c4a67
  summary: Content negotiation returned Crossref bibliographic JSON, not article Results/Methods.
    It corroborates DOI identity only.
  support: context_only
- evidence_id: plaque-access-limitations
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/access-limitations.json
  locator: Actual attempted route receipts/body hashes; inspect response content,
    not HTTP200 alone
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: c54be2f01fadf5453072068e09ab36818057eaef4711f01da4f7a1d81764e6f4
  summary: Fresh Scott/Shintani PMC routes were recaptcha, S3 guesses404, EPMC406;
    Scott BioC no-result HTML and Shintani BioC429. Chasen PMC challenge was replaced
    by genuine S3 JATS. Alcantara publisher403. Retained genuine Scott/Shintani bodies
    independently reread at original timestamps.
  support: context_only
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete same-PR fresh official /api/datasets catalogue independently reread;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T04:49:31.986519Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: 'All20 organism rows/28 organism-dataset pairs inspected: no Saccharomyces/S288C
    or Trypanosoma cruzi/Y biological host match; bacterial experimental protein-expression
    hosts are not proxies.'
  support: supports
- evidence_id: plaque-catalogue-search
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned organism ID/name/dataset fields independently screened
  accessed_at: '2026-11-04T04:49:31.986519Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Bounded lack of matched dataset coverage only; not negative biological
    evidence and no unrelated bacterial module query.
  support: context_only
  search_scope: Official iModulonDB /api/datasets; all20 returned organisms/28 organism-dataset
    pairs at 2026-11-04T04:49:31.986519Z; exact/lexical screen Saccharomyces,cerevisiae,S288C,SEY6210,Trypanosoma,cruzi,Y-strain.
    No outside database or unmatched-host proxy.
- evidence_id: plaque-historical-adapter-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner command ['/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources',
    'imodulondb', 'datasets']; original receipt only
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual historical Nov3 00:49Z exit1 PermissionError reading pyvenv.cfg;
    not a fresh invocation or a successful adapter run. Current official source fallback
    is separately evidenced.
  support: context_only
- evidence_id: plaque-original-current-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/originals-current-proof.json
  locator: Two native original validate/render pairs;29 historical input occurrences
    and48 current source/worktree input hashes
  accessed_at: '2026-11-04T04:51:58.468303Z'
  snapshot_sha256: 85d28ee79c75226a050c16187bfbfc21a8bccc67b2bd2c7ed80f58cbed8d6fe3
  summary: All original pairs validate and render byte-identically; historical hashes
    match exact source commits including symlink resolution. Cvt unchanged; cytostome
    stale hierarchy delta inspected rather than silently rehashed.
  support: supports
- evidence_id: plaque-cytostome-delta
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-plaque/cytostome-substantive-delta.diff
  locator: Exact historical frozen cytostome bytes versus current source; full diff
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: b76d18306bab0e4f8d00743afa292e1d729ce9199f918633d30b5993a81d3dd2
  summary: Only hierarchy change GO0005886 parent to part_of plus GO0110165 parent,
    corresponding evidence and historical curation event. Scientific geometry/uptake
    text otherwise unchanged.
  support: context_only
- evidence_id: plaque-issue2461-context
  kind: database
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2461
  locator: Root-fetched complete issue body/comments/current CLOSED state independently
    read from /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/existing-issue-2461.json
  accessed_at: '2026-11-04T04:56:33.453773Z'
  snapshot_sha256: 702e30967973d3961dd2c5b6fd8cb249b5751d88bd29b57440b591cf55bafbb8
  summary: Already-closed grouped issue explicitly includes other-cytostome-plasma-membrane-parthood;
    resolution comment cites prior commit31fd33d9556ea5627b36d50ab608ccb9464f9353/PR2464.
    Only this matching cytostome finding is dispositioned; other group targets and
    verification bundle are not independently reassessed here.
  support: context_only
- evidence_id: plaque-native-cvt_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cvt_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:49:02.118708Z'
  snapshot_sha256: e375e4bd0b2c96e3b76b2ee944f2876cd07b9b9a495f9e3f502469971462d203
  summary: Actual current-source exit0. One REVIEWED P14904 example and one COVERED
    typed node. Identifier/coverage gates do not certify source-specific membership
    or necessity.
  support: supports
- evidence_id: plaque-native-cvt_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cvt_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-causal.log
    SHA256 eb5b3bedce12a4c7f1373712d261d4b8605539a9f12256f743631fbe68f75567
  accessed_at: '2026-11-04T04:49:02.656100Z'
  snapshot_sha256: 2cc78eda08fa150c38ad7be6f99c902768091c3dbd3e42c7f0beeedd134a1a96
  summary: Actual current-source exit0. One REVIEWED P14904 example and one COVERED
    typed node. Identifier/coverage gates do not certify source-specific membership
    or necessity.
  support: supports
- evidence_id: plaque-native-cytostome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cytostome.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:49:03.114796Z'
  snapshot_sha256: a1864fdce7b77dd8209d78a0c50434506558441daed1ecc82e985b89fab790ad
  summary: Actual current-source exit0. Zero protein_examples and zero typed GENE_OR_PROTEIN
    nodes; empty-inventory pass is not molecular completeness evidence. Identifier/coverage
    gates do not certify source-specific membership or necessity.
  support: supports
- evidence_id: plaque-native-cytostome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cytostome.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T04:49:03.544813Z'
  snapshot_sha256: 99ede2b21f42004e59370581bdef265734444d317f06d00f4805dcc9d58e76f9
  summary: Actual current-source exit0. Zero protein_examples and zero typed GENE_OR_PROTEIN
    nodes; empty-inventory pass is not molecular completeness evidence. Identifier/coverage
    gates do not certify source-specific membership or necessity.
  support: supports
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Scientific review and structured-source applicability
  summary: Actual whole-record molecular/pathway assertions require host/source coverage
    assessment; lack of expression-module claims is not sufficient exemption.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components and Discussions
  summary: Exact family identity differs from complex-specific role. Family or class
    is permitted. Dated rationale/history are append-only; optional examples or broad
    groups alone do not establish defects.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component identity/essentiality and graph fields
  summary: Formation essentiality is distinct from functional activity, localization
    or cellular viability. FUNCTION/NONMECHANISTIC graphs may describe coarse associations
    without a complete molecular assembly mechanism.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native accession/name/status/taxon and query rules
  summary: Native primary genes versus ORF names and bounded query coverage are distinct
    from biological source membership, necessity and source-strain equivalence.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Evidence placement and descriptive graph scope
  summary: Constituent relationships, perturbation outputs and co-isolation retain
    experiment scope; graph coverage alone does not establish molecular identity or
    direct ubiquitination.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Source access, image and read extents
  summary: Native metadata/abstract, genuine body/captions, pixels and failed responses
    are separate tiers. Generated authority prose is excluded as independent biological
    evidence.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684,GO:0097687,GO:0097683,GO:0097614,GO:0097613,GO:0110165,GO:0097618,GO:0097612,GO:0097685,GO:0097686,GO:0031461
  locator: All11 requested identities/names/definitions/synonyms and relevant typed
    child relationships; not an exhaustive descendant audit
  summary: Cullin-RING GO0031461 is a broader parent. Dinoflagellate0097684/87/83
    denote antapex/horn/apex. GO0097684 still says anterior, conflicting with GO0097618
    posterior antapex and GO0097614 posterior hypocone. Exact identifiers and typed
    topology remain valid; source transcription is not biological correctness.
  accessed_at: '2026-11-04T04:51:28.338072Z'
  support: supports
  snapshot_sha256: e9ee91297077b404316ba7bdf7caaee8e2c22b76cc165459633afe9f962cefc5
- evidence_id: septin-go-0097684-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684/history
  locator: Complete current native history response
  summary: History independently distinguishes direct apex/antapex cellular-anatomical
    parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits
    hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence
    census. Historical Bad taxon ID events are not current constraint identities.
  accessed_at: '2026-11-04T04:51:30.252649Z'
  support: supports
  snapshot_sha256: a1000a5866a870ab923d364c16654f113a7a3138bf93b2c089f299fbb30501a5
- evidence_id: septin-go-0097684-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097684/constraints
  locator: Complete current native constraints response
  summary: History independently distinguishes direct apex/antapex cellular-anatomical
    parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits
    hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence
    census. Historical Bad taxon ID events are not current constraint identities.
  accessed_at: '2026-11-04T04:51:30.383435Z'
  support: supports
  snapshot_sha256: f136335a571e7251092d8bc12a0a8cead9f29fae558fe8f02d44c2209e3c6aaf
- evidence_id: septin-go-0097687-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/history
  locator: Complete current native history response
  summary: History independently distinguishes direct apex/antapex cellular-anatomical
    parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits
    hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence
    census. Historical Bad taxon ID events are not current constraint identities.
  accessed_at: '2026-11-04T04:51:30.705890Z'
  support: supports
  snapshot_sha256: 70fea0d8875ec84768ec659b43a15c8da4c02685293b1ace96939663dc52b408
- evidence_id: septin-go-0097687-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097687/constraints
  locator: Complete current native constraints response
  summary: History independently distinguishes direct apex/antapex cellular-anatomical
    parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits
    hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence
    census. Historical Bad taxon ID events are not current constraint identities.
  accessed_at: '2026-11-04T04:51:30.579537Z'
  support: supports
  snapshot_sha256: c1ac2d6dd676fa882d195bb473ce1a577eae8a20453c4adf06a7bc85e26d416a
- evidence_id: septin-go-0097683-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097683/history
  locator: Complete current native history response
  summary: History independently distinguishes direct apex/antapex cellular-anatomical
    parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits
    hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence
    census. Historical Bad taxon ID events are not current constraint identities.
  accessed_at: '2026-11-04T04:51:30.476061Z'
  support: supports
  snapshot_sha256: b2332e48b505942cb6de93ff58088ffd9566853ecdf62551a73e3b4f489f45e0
- evidence_id: septin-go-0097683-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097683/constraints
  locator: Complete current native constraints response
  summary: History independently distinguishes direct apex/antapex cellular-anatomical
    parent and respective epicone/hypocone parthood; horn direct is_a antapex inherits
    hypocone parthood. Only_in_taxon2864 is a taxonomic restriction, not a prevalence
    census. Historical Bad taxon ID events are not current constraint identities.
  accessed_at: '2026-11-04T04:51:30.808627Z'
  support: supports
  snapshot_sha256: 31d92ef485cd54fd735b7e22109e2a0b4a5a9b061f25b3dde7153d303e4596e2
- evidence_id: septin-tol-orientation
  kind: authority
  reference: https://tolweb.org/articles/?article_id=4756
  locator: Complete authored main text, embedded overview caption and About This Page
    authorship/license; no image pixels
  summary: Mona Hoppenrath2008 directly identifies apex at top of episome and antapex
    at bottom of hyposome, with below-cingulum orientation posterior. Athecate/thecate
    terminology and possible apical groove are explicitly scoped. Expert morphological
    authority, not a molecular formation experiment. Text CC-BY-NC3.0 is distinct
    from per-image rights; no image reused.
  accessed_at: '2026-11-04T04:51:28.054442Z'
  support: supports
  snapshot_sha256: 406916e9c83d51de4ec6f7dee8a7b129c6ab8e1781a65a3ec28d83734970370e
- evidence_id: septin-tol-dino
  kind: authority
  reference: https://tolweb.org/Dinoflagellates/2445
  locator: Authorship block, Introduction and Characteristics through Flagella/Nucleus/Amphiesma/Vacuoles
    and Pusules; later sections not used
  summary: GO-cited Hoppenrath/Saldarriaga branch page links the separate Cell Orientation
    note and describes varied motile morphologies. Whole-cell cellulose/protein content
    is not reassigned to a regional point. General whole-cell sizes, genomic statements
    and prevalence estimates are not imported into these records; no pixels inspected.
  accessed_at: '2026-11-04T04:51:28.249979Z'
  support: supports
  snapshot_sha256: 5957a1388500247ac00f15d5ffaccc4df3ee19b07daf5986bd7a96fa5fc3df47
- evidence_id: septin-ina-orientation
  kind: authority
  reference: https://ina.tmsoc.org/terminology/calcispheres.htm
  locator: Complete Orientation section and adjacent calcisphere/cyst scope; remaining
    glossary read as context
  summary: Orientation independently maps apex/anterior front and antapex/posterior
    rear. Cyst-oriented supplementary terminology is not treated as a universal motile-cell
    molecular mechanism or prevalence census.
  accessed_at: '2026-11-04T04:51:28.668575Z'
  support: supports
  snapshot_sha256: 2c70cd60e66d957b040d2d1068314faab3316cea0c93ae2e83d0658d2cda2b98
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh official20-organism catalogue and all returned dataset keys,
    independently read from peer packet
  summary: No Trypanosoma/TREU927/Lister427/2T1 or Dinophyceae/dinoflagellate dataset
    occurs in this finite response. Cullin-E positive molecular claims require this
    assessment, but no matching downstream gene/module query applies. Dinoflagellate
    records have genuine physical scope independent of noncoverage. Other listed taxa
    are not proxies; absence is not negative biology. Actual peer retrieval timestamp
    retained.
  accessed_at: '2026-11-04T04:49:31.986519Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-tax-185431
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431
  locator: Complete native ENA taxId/name/rank/lineage/otherNames
  summary: TREU927185431 is a strain/reference annotation, T.brucei5691 a species;
    neither identifies Lister427/2T1 experimental specimens. Dinophyceae2864 is a
    class with native dinoflagellate/Dinophyta/Dinoflagellata aliases; no population-frequency
    inference.
  accessed_at: '2026-11-04T04:51:28.893372Z'
  support: supports
  snapshot_sha256: 37f4acd608d79bb144d706335e37a83a0f97a94595aca5175855c8c390ec652d
- evidence_id: septin-tax-5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete native ENA taxId/name/rank/lineage/otherNames
  summary: TREU927185431 is a strain/reference annotation, T.brucei5691 a species;
    neither identifies Lister427/2T1 experimental specimens. Dinophyceae2864 is a
    class with native dinoflagellate/Dinophyta/Dinoflagellata aliases; no population-frequency
    inference.
  accessed_at: '2026-11-04T04:51:29.113874Z'
  support: supports
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: septin-tax-2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native ENA taxId/name/rank/lineage/otherNames
  summary: TREU927185431 is a strain/reference annotation, T.brucei5691 a species;
    neither identifies Lister427/2T1 experimental specimens. Dinophyceae2864 is a
    class with native dinoflagellate/Dinophyta/Dinoflagellata aliases; no population-frequency
    inference.
  accessed_at: '2026-11-04T04:51:29.248478Z'
  support: supports
  snapshot_sha256: da7d6dfa6d6784e4eb22bc3f3e05878f3aae5a281a4996ee25a2012d580f27d4
- evidence_id: septin-up-Q383D5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q383D5.json
  locator: Complete accession/status/protein names with evidence codes,genes,organism,length,available
    function/subunit/location comments and VEuPathDB/InterPro xrefs
  summary: 805aa, unreviewed Cullin1 putative; ORF Tb11.01.3260 and VEuPathDB Tb927.11.11430
    agree with source scaffold. Native ORF names are not formal primary geneName fields.
    No sequence alignment or new experimental localization assay performed.
  accessed_at: '2026-11-04T04:51:29.890821Z'
  support: supports
  snapshot_sha256: 152a4a4bd8f8f33b3ba49f17c8caa5134d28363c5a500eb0e7565dced9fb763c
- evidence_id: septin-up-Q38C61
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q38C61.json
  locator: Complete accession/status/protein names with evidence codes,genes,organism,length,available
    function/subunit/location comments and VEuPathDB/InterPro xrefs
  summary: 106aa, unreviewed RING-type protein; ORF Tb10.70.6035 and VEuPathDB Tb927.10.1810
    agree with source Rbx1. Native ORF names are not formal primary geneName fields.
    No sequence alignment or new experimental localization assay performed.
  accessed_at: '2026-11-04T04:51:30.482783Z'
  support: supports
  snapshot_sha256: 78fe97e60a37095c4aa6e599bf63d145c366255c9577179761ecffc93cc40782
- evidence_id: septin-up-Q384S1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q384S1.json
  locator: Complete accession/status/protein names with evidence codes,genes,organism,length,available
    function/subunit/location comments and VEuPathDB/InterPro xrefs
  summary: 212aa, unreviewed ORF Tb11.02.5340; no exact source Skp1.2 locus bridge.
    Generated SKP1/POZ name cannot establish membership. Native ORF names are not
    formal primary geneName fields. No sequence alignment or new experimental localization
    assay performed.
  accessed_at: '2026-11-04T04:51:29.480022Z'
  support: supports
  snapshot_sha256: 1391c6ae29806ecef62c8d00049662c0cb4efe398752d7345226a55dffc145bd
- evidence_id: septin-up-Q38ED0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q38ED0.json
  locator: Complete accession/status/protein names with evidence codes,genes,organism,length,available
    function/subunit/location comments and VEuPathDB/InterPro xrefs
  summary: 158aa, unreviewed ORF Tb09.211.0300 and VEuPathDB Tb927.9.8370 agree exactly
    with source Skp1.2. Generated Elongin-C name is not independent biological evidence
    and does not invalidate the exact source-locus bridge. Native ORF names are not
    formal primary geneName fields. No sequence alignment or new experimental localization
    assay performed.
  accessed_at: '2026-11-04T04:51:30.487607Z'
  support: supports
  snapshot_sha256: f62ef0e39d903ebf16a805be44e4a1f598dfc72ef3d6803d10983685a936bfc0
- evidence_id: septin-ensembl-skp12
  kind: database
  reference: https://rest.ensembl.org/lookup/id/Tb927.9.8370?expand=1;content-type=application/json
  locator: Complete exact gene/transcript/translation lookup
  summary: Tb927.9.8370 is protein coding and independently maps to Q38ED0 with158aa
    translation; current assembly coordinate differences are not used to infer a different
    source protein.
  accessed_at: '2026-11-04T04:51:35.970577Z'
  support: supports
  snapshot_sha256: 0925155ab6d45af152e6e2277092f8f7b630c370f128ffe6187277d1d7091efc
- evidence_id: septin-query-Tb927.11.11430
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb927.11.11430%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 0 entries. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:32.420856Z'
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb927.11.11430);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:32.420856Z.
- evidence_id: septin-query-Tb927.10.1810
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb927.10.1810%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 0 entries. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:31.672469Z'
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb927.10.1810);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:31.672469Z.
- evidence_id: septin-query-Tb927.9.8370
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb927.9.8370%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 0 entries. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:34.229313Z'
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb927.9.8370);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:34.229313Z.
- evidence_id: septin-query-Tb11.01.3260
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb11.01.3260%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 1 entries Q383D5. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:33.249774Z'
  support: supports
  snapshot_sha256: 53476065c4397e87a405cccd47451050589c263135a3c9d1e76f5f4e425803b1
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb11.01.3260);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:33.249774Z.
- evidence_id: septin-query-Tb10.70.6035
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb10.70.6035%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 1 entries Q38C61. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:31.746983Z'
  support: supports
  snapshot_sha256: c0446b7e2c052654bc8700b43c690a9dc71bec365e5c811985bae9258a23cf36
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb10.70.6035);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:31.746983Z.
- evidence_id: septin-query-Tb11.02.5340
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb11.02.5340%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 1 entries Q384S1. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:33.326270Z'
  support: supports
  snapshot_sha256: 1cd95dc4118fe4e5318b41367a17ae9cbed28b119af4cd95fa03698b795afa8a
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb11.02.5340);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:33.326270Z.
- evidence_id: septin-query-Tb09.211.0300
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28organism_id%3A185431%29+AND+%28gene_exact%3ATb09.211.0300%29&format=json&size=100
  locator: Complete returned page and accession/status/name/ORF/taxon identities
  summary: Current exact gene/taxon search returns 1 entries Q38ED0. Empty current-locus
    searches do not negate the protein; historical ORF identifiers and authority xrefs
    provide the verified bridge. This does not reconstruct an October search.
  accessed_at: '2026-11-04T04:51:32.139764Z'
  support: supports
  snapshot_sha256: b48f0fa8d30945a9133faa616bd45d5b454819ea11873d72bdb6445039a09ed7
  search_scope: UniProt REST query (organism_id:185431) AND (gene_exact:Tb09.211.0300);
    size100,formatjson,no date filter; complete returned page read at 2026-11-04T04:51:32.139764Z.
- evidence_id: septin-ipr-045093
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045093/
  locator: Native accession/name/type/description flags and complete description;
    no inferred exact-paralog mapping
  summary: Cullin broad family does not distinguish the divergent E paralog. Family/class
    components are permitted; broad identity or absent optional exact grounding alone
    is not a new defect.
  accessed_at: '2026-11-04T04:51:29.352966Z'
  support: supports
  snapshot_sha256: 3c1fabca973d9704f4e57ccb886f8ae6284079c9178bdf627cccc8bb35bac5aa
- evidence_id: septin-ipr-051031
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051031/
  locator: Native accession/name/type/description flags and complete description;
    no inferred exact-paralog mapping
  summary: RING-box family is broader than exact source Rbx1; llm=true/checked=false
    functional prose is excluded from biological support. Family/class components
    are permitted; broad identity or absent optional exact grounding alone is not
    a new defect.
  accessed_at: '2026-11-04T04:51:29.515275Z'
  support: supports
  snapshot_sha256: d08c2762d364d25fa692b43c86e131a812cd93c8008d5978ef4531027b694e91
- evidence_id: septin-ipr-001232
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001232/
  locator: Native accession/name/type/description flags and complete description;
    no inferred exact-paralog mapping
  summary: SKP1-like includes SKP1 and Elongin-C; broad family does not distinguish
    source Skp1.2 from other paralogs. Family/class components are permitted; broad
    identity or absent optional exact grounding alone is not a new defect.
  accessed_at: '2026-11-04T04:51:30.062154Z'
  support: supports
  snapshot_sha256: b53bf5571f84de756d3b93f4d5a19006dbf485dee5970c88249fdd202ec46c71
- evidence_id: septin-ipr-016897
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016897/
  locator: Native accession/name/type/description flags and complete description;
    no inferred exact-paralog mapping
  summary: SKP1 family description restricts background examples to yeast/animals/plants,
    not exact source Skp1.2. Family/class components are permitted; broad identity
    or absent optional exact grounding alone is not a new defect.
  accessed_at: '2026-11-04T04:51:30.178157Z'
  support: supports
  snapshot_sha256: e47550d5dfd19baea033f543ef6823c3e10ca974faaae5d49d823b994c794df7
- evidence_id: septin-pmid-41413177
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A41413177+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique native MED identity/authors/title/year/DOI/PMCID and complete abstract
  summary: Exact bibliographic identity resolves. Primary paper abstract/metadata;
    genuine full-body read extents are separately recorded.
  accessed_at: '2026-11-04T04:51:30.986250Z'
  support: supports
  snapshot_sha256: d132503874db913053d6ac3423e8c1389c2bc5f46363e74ed5711d3c7b41bd22
  search_scope: EuropePMC exact query EXT_ID:41413177 AND SRC:MED; resultTypecore,formatjson,pageSize10,no
    date filter; unique result read at 2026-11-04T04:51:30.986250Z.
- evidence_id: septin-pmid-28052114
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28052114+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique native MED identity/authors/title/year/DOI/PMCID and complete abstract
  summary: Exact bibliographic identity resolves. Primary paper abstract/metadata;
    genuine full-body read extents are separately recorded.
  accessed_at: '2026-11-04T04:51:30.990908Z'
  support: supports
  snapshot_sha256: 966b95e10332f491c7a01b925cfe39af28a94fe1b75d4fcc8395c10cafda811d
  search_scope: EuropePMC exact query EXT_ID:28052114 AND SRC:MED; resultTypecore,formatjson,pageSize10,no
    date filter; unique result read at 2026-11-04T04:51:30.990908Z.
- evidence_id: septin-pmid-7002229
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7002229+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique native MED identity/authors/title/year/DOI/PMCID and complete abstract
  summary: Exact bibliographic identity resolves. Taylor1980 is a secondary evolutionary
    review, read only at complete abstract/metadata; not independent primary evidence
    for exact horn/apex anatomy or a molecular mechanism.
  accessed_at: '2026-11-04T04:51:31.088726Z'
  support: supports
  snapshot_sha256: b2590cee542c07d002fa3651d6950be20b04af19df6df2fe84acc48ac5285a1d
  search_scope: EuropePMC exact query EXT_ID:7002229 AND SRC:MED; resultTypecore,formatjson,pageSize10,no
    date filter; unique result read at 2026-11-04T04:51:31.088726Z.
- evidence_id: septin-PMC12816148-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12816148/fullTextXML
  locator: Genuine JATS front/permissions, completeTable1,ResultsSec4/5/6/9,DiscussionSec10,MethodsSec12/13/15/17/18/19/21;
    captionsFig2/6/7/8
  summary: Table1 and S3 define Cul-E Tb927.11.11430,Rbx1 Tb927.10.1810,Skp1.2 Tb927.9.8370,four
    kelch loci. Co-enrichment does not establish simultaneous occupancy, stoichiometry,
    direct recognition or obligatory formation. RNAi1K2N/Golgi/24hLFQ readouts remain
    separate from direct substrate claims. Isolation PCF Lister427, incompletely restated
    RNAi stage,2T1qPCR and927database are distinct; Methods seven WTcontrols versus
    PRIDE six remains unresolved. Discussion olderPLK→CulE attribution conflicts with
    Hu source locus and is not imported. Figure8 is a generic humanCullin1-based scheme;
    CC-BY4.0 license verified.
  accessed_at: '2026-11-04T04:51:29.863510Z'
  support: supports
  snapshot_sha256: e8e06fecd846a0ceda847b73614fdf72ca794a565399b729fdd2298339b41bd3
- evidence_id: septin-PMC5241021-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5241021/fullTextXML
  locator: Genuine JATS front, completeResultssec004 and embeddedFig2/3 captions;
    Methodssec011/015/016; no pixels/supplements in this pass
  summary: Hu2017 maps source WDR1 Tb927.10.15080 with TbCUL4 Tb927.3.1290 and DDB1
    Tb927.6.5110. TbCUL1 Tb927.11.11430 did not co-precipitate WDR1 in the specified
    assay. This establishes a cross-paper attribution conflict, not universal disproof
    of any future CulE/PLK relationship. 29-13 RNAi and Lister427 tagging/co-IP are
    not TREU927 specimens; in-vitro fragment/lysate and co-IP scopes preserved.
  accessed_at: '2026-11-04T04:51:29.672310Z'
  support: supports
  snapshot_sha256: 14db45e5df4366741ab57052076df20ea7453b39d4fa719632051406a30efe9e
- evidence_id: septin-cullin-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12816148.1/41598_2025_32077_MOESM3_ESM.xlsx
  locator: Genuine XLSX Legend all nonempty rows; complete CULE headerA–AZ and columnsA–Z
    of rows2,3,4,5,7,9,10 only
  summary: Seven source-defined bait/Skp1.2/Rbx1/kelch rows carry both significance
    flags. Row3 is Tb927.9.8370,158aa; rows2/7 are805/106aa. HeaderWT1–7 independently
    verifies seven controls. No full-workbook statistics, raw spectra, quantitative
    replication or irrelevant database-annotation inference.
  accessed_at: '2026-11-04T04:51:30.061576Z'
  support: supports
  snapshot_sha256: 626696993829fdc5cc4f09a9f8ce2cf2cb2549c70aaac34731cd5b39fa86e0df
- evidence_id: septin-pride
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD042022
  locator: Complete accession/title/project description,sample/data protocols,submission
    type,organism and publication fields
  summary: PXD042022 PARTIAL submission links PMID41413177/DOI10.1038/s41598-025-32077-9
    and Tbrucei5691. Native sample protocol says six WTcontrols; paper/S3 seven. CulE12/24hLFQ
    and CulA SILAC are distinct. Landing-page metadata/protocol inspected, no raw
    spectra or bulk download analysis.
  accessed_at: '2026-11-04T04:51:28.216669Z'
  support: supports
  snapshot_sha256: 721d9e5e65021043b62e7d0834951a3fb9020d5384dd579e90bdc1f54161fc9c
- evidence_id: septin-fig2
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2663/12816148/60c8f8921df5/41598_2025_32077_Fig2_HTML.jpg
  locator: Actual fresh image viewed with view_image; entire pixels and corresponding
    full JATS caption inspected
  summary: Actual complete pixels A–E; panelB shows CulE,Rbx1,Skp1.2,four kelch associations
    above depicted cutoff; not copy numbers/direct contacts. Publisher/PMC media under
    article CC-BY4.0; no maintained image is added or redistributed, no new physical-dimension
    measurement.
  accessed_at: '2026-11-04T04:51:31.222590Z'
  support: supports
  snapshot_sha256: 13daf221f68f2bc7c8e1b63ff4983f479f049717645561e27f6da295607ab996
- evidence_id: septin-fig6
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2663/12816148/55fe1026949a/41598_2025_32077_Fig6_HTML.jpg
  locator: Actual fresh image viewed with view_image; entire pixels and corresponding
    full JATS caption inspected
  summary: Actual complete pixels A–D;0/12/24/36h pie plots have increased1K2N fraction
    and representative GRASP/MitoTracker images; no population-frequency calculation
    or localization of CulE itself. Publisher/PMC media under article CC-BY4.0; no
    maintained image is added or redistributed, no new physical-dimension measurement.
  accessed_at: '2026-11-04T04:51:31.263915Z'
  support: supports
  snapshot_sha256: 62e3270920d35279077ac04a9766900897d113a1f502e993220c834522bf6d15
- evidence_id: septin-fig7
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/2663/12816148/748152b87b25/41598_2025_32077_Fig7_HTML.jpg
  locator: Actual fresh image viewed with view_image; entire pixels and corresponding
    full JATS caption inspected
  summary: 'Actual complete pixels show24h statistical-difference plot: CulE and point8
    decreased,point7 increased. Caption maps point8Tb927.10.8810/point7KKT9; duplicate
    point2/3Tb927.1.4900 attribution remains excluded from graph. Publisher/PMC media
    under article CC-BY4.0; no maintained image is added or redistributed, no new
    physical-dimension measurement.'
  accessed_at: '2026-11-04T04:51:31.186039Z'
  support: supports
  snapshot_sha256: b1d42ffcb258c107925e7fdd0b77f3238662a6a6672d2872baba0bd31ac14ede
- evidence_id: septin-taylor-publisher
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/0303264780900064
  locator: Exact fresh ScienceDirect HTTP403 response; no article body inspected
  summary: Failed current access is context only. Original October403 is separately
    dated historical provenance. Neither provides primary source body evidence; target
    already limits Taylor to bibliography.
  accessed_at: '2026-11-04T04:51:30.940027Z'
  support: context_only
  snapshot_sha256: cc08c6aa57598266bc39e968a22c0def3d79e6646f8c3fd21920dfe49e5d3173
- evidence_id: septin-source-packet
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-septin/source-receipts.json
  locator: Actual fresh HTTP URLs/status/types/timestamps/byte hashes
  summary: Only genuine JATS/workbook/authority data and viewed images support declared
    scientific scope; Taylor403 is not body access. Scratch text-extraction first
    attempt lacked bs4; corrected stdlib parser succeeded, not a repository/scientific
    test failure.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: context_only
  snapshot_sha256: 725e78bd05aa6c3b61c3b93823bf996256a195f7fd6b9ae1491df5ddeba1a894
- evidence_id: septin-shared-catalogue-packet
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-septin/shared-receipts.json
  locator: Actual peer catalogue fetch receipt independently hash checked and reread
  summary: Catalogue source timestamp retained; no new adapter invocation claimed.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: context_only
  snapshot_sha256: 8cd76103b6eb692e00c3ea1fc855d74625ec24e13c4f0307fb46cbc6acb48823
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907Z–00:49:00.863225Z; exit1 PermissionError
    reading pyvenv.cfg
  summary: Historical unavailable runner only; no fresh execution. Current official
    catalogue and native/primary source fallback are independently inspected.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/adversary-septin/original-checks.json
  locator: Four actual native validate/render executions and59 historical input occurrences
  summary: All original native validations/renders exit0 and exact paired Markdown;
    all historical source hashes match, all four target hashes unchanged. Historical
    batch26 execution explicitly scoped in originalchecks is valid reuse, not a mislabeled
    batch49 run.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: ee06a2f39237e6cdf3611b5884fa1e1b6e6506d1d095395b09b5eecd147556cb
- evidence_id: septin-record-cullin_e_ubiquitin_ligase_complex
  kind: record_content
  reference: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
  locator: Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,datasets,graphs,discussions/history read. Target nonstale.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 24cfaf2e2cd189ff59a4b9889fbbb3fe13e8f30fed4d282f41323e21c78e4c96
- evidence_id: septin-original-cullin_e_ubiquitin_ligase_complex
  kind: record_content
  reference: reviews/structured/20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Original
    batch26 execution origin and dated observations retained.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 742d59158e7220ac8ffa6199a3ab027e15b158576a0da2a139ca9479c7629093
- evidence_id: septin-native-cullin_e_ubiquitin_ligase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Three unreviewed example occurrences/three distinct accessions and
    one native COVERED Cullin-E node. Native pass does not establish the disputed
    Skp1.2 biological assignment.
  accessed_at: '2026-11-04T04:49:00.497916Z'
  support: supports
  snapshot_sha256: 63ff907a0f7270072835bde7a606127bb015a32c0d9e2c6360c7c0100f13744b
- evidence_id: septin-native-cullin_e_ubiquitin_ligase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    --causal-graphs; logSHA256 541d8ce82ac8de035386b41bcda3588ae6f68e6299387757256e00060caf6729
  summary: Exit0. Three unreviewed example occurrences/three distinct accessions and
    one native COVERED Cullin-E node. Native pass does not establish the disputed
    Skp1.2 biological assignment.
  accessed_at: '2026-11-04T04:49:00.914425Z'
  support: supports
  snapshot_sha256: d02cafcda7c784f778b456d4c0045f9f5554206e76fdc7cbc455c5a83dcadd91
- evidence_id: septin-record-dinoflagellate_antapex
  kind: record_content
  reference: data/structures/other/dinoflagellate_antapex.yaml
  locator: Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,datasets,graphs,discussions/history read. Target nonstale.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 1379be0377e9b86e39f36a4a2a8946b02ab5aa9004aa2576e25b8691147c7fb9
- evidence_id: septin-original-dinoflagellate_antapex
  kind: record_content
  reference: reviews/structured/20261022T052921Z-dinoflagellate-antapex-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Original
    batch26 execution origin and dated observations retained.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 441da86d4f9fb76d9b3f6fe8084b735ecec5296d87db3588acb89c3dd24e5897
- evidence_id: septin-native-dinoflagellate_antapex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapex.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful
    native checks cover this empty molecular inventory, not unasserted localization/formation.
  accessed_at: '2026-11-04T04:49:15.583648Z'
  support: supports
  snapshot_sha256: 440a364ac0dc53eaf7bfaf74d1408555f4d4748efc8d6d09b863a0e72d727cdb
- evidence_id: septin-native-dinoflagellate_antapex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapex.yaml
    --causal-graphs; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful
    native checks cover this empty molecular inventory, not unasserted localization/formation.
  accessed_at: '2026-11-04T04:49:16.009760Z'
  support: supports
  snapshot_sha256: e8c2ad9f1a4ab084b68cd844f47944d28fc56236c7030776e10c3a467038d494
- evidence_id: septin-record-dinoflagellate_antapical_horn
  kind: record_content
  reference: data/structures/other/dinoflagellate_antapical_horn.yaml
  locator: Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,datasets,graphs,discussions/history read. Target nonstale.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 17b0c9dcaaa5110c51d7120d3d7fb6bf6ac9a483981418b9ada4be51b700ccc7
- evidence_id: septin-original-dinoflagellate_antapical_horn
  kind: record_content
  reference: reviews/structured/20261022T052922Z-dinoflagellate-antapical-horn-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Original
    batch26 execution origin and dated observations retained.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 48f171d804a7a5eb69760c6fac5ae6e7115bbf9ea175414f95f9a076e4f18e40
- evidence_id: septin-native-dinoflagellate_antapical_horn-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful
    native checks cover this empty molecular inventory, not unasserted localization/formation.
  accessed_at: '2026-11-04T04:49:16.427275Z'
  support: supports
  snapshot_sha256: 11451e7c03779707f15b1887656787a2f0f15d4e291e255c9f61ef9f046fa400
- evidence_id: septin-native-dinoflagellate_antapical_horn-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_antapical_horn.yaml
    --causal-graphs; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful
    native checks cover this empty molecular inventory, not unasserted localization/formation.
  accessed_at: '2026-11-04T04:49:16.860628Z'
  support: supports
  snapshot_sha256: a917165be95ed0a964e270ca132ddd30722d6f2f8791261d7accbd9908f2edbb
- evidence_id: septin-record-dinoflagellate_apex
  kind: record_content
  reference: data/structures/other/dinoflagellate_apex.yaml
  locator: Complete maintained record at e1e8bf616b2ed45741e993b1993cb69017cf2e61
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,datasets,graphs,discussions/history read. Target nonstale.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 5c8d91554cc820c9434886f0022093eff4f766f4ad608fed12ded740860d0749
- evidence_id: septin-original-dinoflagellate_apex
  kind: record_content
  reference: reviews/structured/20261022T052923Z-dinoflagellate-apex-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Original
    batch26 execution origin and dated observations retained.
  accessed_at: '2026-11-04T04:55:38.023589Z'
  support: supports
  snapshot_sha256: 77e09e5ed1b57473aa2f10c398d35dacbb9d074006cb64981a567af12271c99f
- evidence_id: septin-native-dinoflagellate_apex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apex.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful
    native checks cover this empty molecular inventory, not unasserted localization/formation.
  accessed_at: '2026-11-04T04:49:17.316285Z'
  support: supports
  snapshot_sha256: 53242edd9ad812edeea30ed085b077161ab8d0650b6a8abb2413969c55b2adab
- evidence_id: septin-native-dinoflagellate_apex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dinoflagellate_apex.yaml
    --causal-graphs; logSHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Exit0. Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful
    native checks cover this empty molecular inventory, not unasserted localization/formation.
  accessed_at: '2026-11-04T04:49:17.736380Z'
  support: supports
  snapshot_sha256: 0cb3fd56d4e48aaecfaad08ed1e3577070f38ef75a2b870b937e0b592346d768
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:54:33.999999Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: dd7549e47f06b6d5c1d4dc83c817d1131b8f85f7b8a6780ab7013409f2c4a63e
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:49:26.974610Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:49:08.013047Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:49:10.587527Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:49:40.061141Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T05:03:05Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 62d97c2a6bcd2d635a845962561ffadc7cc8275d1864b73bea9c65ba271b7495
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T04:51:06.513080Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 8237939364bef2f214371b64567499b35a6d007c33fbe36c204b711c5b91347f
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2386 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-cullin_e_ubiquitin_ligase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:00.497916Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cullin_e_ubiquitin_ligase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cullin_e_ubiquitin_ligase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:00.914425Z'
  support: context_only
  snapshot_sha256: 541d8ce82ac8de035386b41bcda3588ae6f68e6299387757256e00060caf6729
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cvt_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:02.118708Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cvt_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cvt_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:02.656100Z'
  support: context_only
  snapshot_sha256: eb5b3bedce12a4c7f1373712d261d4b8605539a9f12256f743631fbe68f75567
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cytostome-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:03.114796Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cytostome-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/cytostome-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:03.544813Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dash_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:06.912873Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dash_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dash_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:07.395326Z'
  support: context_only
  snapshot_sha256: 35cc550c1a6115a14b841486e6313e1c723b4a77074deb16b03f416b463ef28f
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dbf4_dependent_protein_kinase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:09.144538Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dbf4_dependent_protein_kinase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dbf4_dependent_protein_kinase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:09.610072Z'
  support: context_only
  snapshot_sha256: 69d4848530843f3d8b7c8651b0f217032da1f2bf11e09fa36969ee325d9ef6df
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-delta_dna_polymerase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:12.737597Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-delta_dna_polymerase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/delta_dna_polymerase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:13.162852Z'
  support: context_only
  snapshot_sha256: 9d47952c8ac17bd446c4fab095faa0a2308bb3d31ccca4a3cc88179ae930d58e
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-diaa_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:14.737192Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-diaa_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/diaa_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:15.158734Z'
  support: context_only
  snapshot_sha256: 5003812ac51deab9d43f38ec02f6deacaac1afb55770013f583b65a26c758057
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_antapex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:15.583648Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_antapex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:16.009760Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_antapical_horn-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:16.427275Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_antapical_horn-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_antapical_horn-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:16.860628Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_apex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:17.316285Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dinoflagellate_apex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2386/dinoflagellate_apex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:49:17.736380Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-dash-identity
  area: identity
  topic: Exact DASH/DDD complex boundary
  outcome: supported
  summary: GO0042729 and primary purification identify the same fungal outer-kinetochore
    assembly. Nuclear complex parent and kinetochore/outer-kinetochore parthood are
    supported. The declared seven curated subunits do not imply an exhaustive ten-subunit
    closure; explicit Dad3/Dad4/Hsk boundary work remains.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-go-0042729
  - micro-go-0140513
  - micro-go-0000940
  - micro-go-0000776
  - micro-cheeseman2001-jats
  - micro-janke2002-publisherpdf
  - micro-li2005-meta
- assessment_id: micro-dash-refresh
  area: provenance
  topic: Substantive seven-node and seven-edge stale refresh
  outcome: supported
  summary: 'DASH alone differs from its frozen original: dated history plus seven
    component_ref nodes and constituent contributes-to edges. Current reviewed identities
    and independent Cheeseman/Janke native complex purifications support each new
    edge. No atomic interface, all-subunit necessity or ring-force mechanism is added;
    F1/F2 remain independent unresolved curation.'
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-cheeseman2001-jats
  - micro-janke2002-publisherpdf
  - micro-native-dash_complex-causal
- assessment_id: micro-dash-families
  area: grounding
  topic: Seven exact full-protein families
  outcome: concern
  summary: Seven exact DASH family identities and their reviewed example xrefs are
    independently verified. All seven current component classes remain label-only,
    so inherited minor F1 remains. This is a supported class mapping, not an inference
    from optional missing examples or broad domains.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR013960
  - micro-ipr-IPR013962-retry
  - micro-ipr-IPR013958
  - micro-ipr-IPR013963-retry
  - micro-ipr-IPR013964
  - micro-ipr-IPR013251
  - micro-ipr-IPR013966-retry2
  - micro-up-P53168
  - micro-up-P53267
  - micro-up-Q12248
  - micro-up-P36162
  - micro-up-P35734
  - micro-up-Q03954
  - micro-up-P36131
- assessment_id: micro-dash-examples
  area: grounding
  topic: Seven exact S288c reference proteins
  outcome: supported
  summary: All seven maintained accessions, primary symbols/loci, reviewed status
    and reference taxon559292 agree with native authorities and fresh singleton gene
    queries. DAD2 has HSK1 synonym, which does not silently identify all omitted Hsk
    microproteins. Species4932 and reference559292 are distinguished.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-tax-4932
  - micro-tax-559292
  - micro-up-P53168
  - micro-up-P53267
  - micro-up-Q12248
  - micro-up-P36162
  - micro-up-P35734
  - micro-up-Q03954
  - micro-up-P36131
  - micro-query-DUO1
  - micro-query-DAM1
  - micro-query-DAD1
  - micro-query-DAD2
  - micro-query-ASK1
  - micro-query-SPC19
  - micro-query-SPC34
- assessment_id: micro-dash-localization
  area: evidence
  topic: Source-adjacent localization evidence
  outcome: supported
  summary: Native location notes/evidence codes support the declared nuclear/spindle/kinetochore
    and Ask1-origin contexts. Cheeseman/Janke localization text is independently body-read;
    Huh, Hofmann, later attachment/oligomerization and Ask1-origin papers are complete
    abstract/native-annotation tier only, without raw-image certification.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-cheeseman2001-jats
  - micro-janke2002-publisherpdf
  - micro-up-P53168
  - micro-up-P53267
  - micro-up-Q12248
  - micro-up-P36162
  - micro-up-P35734
  - micro-up-Q03954
  - micro-up-P36131
  - micro-pmid-14562095
  - micro-pmid-9817759
  - micro-pmid-11698664
  - micro-pmid-21256019
  - micro-pmid-25236177
  - micro-pmid-36701236
- assessment_id: micro-dash-formation
  area: grounding
  topic: Conditional Spc34 association/recovery evidence
  outcome: concern
  summary: 'Janke p182/Fig1B directly compares Dad2-ProA recovery after4h37C: spc34-3
    yields bait alone while SPC34 yields the complete reported complex. Inherited
    F2 remains a narrow association/stability-evidence gap. UNKNOWN alone is not defective;
    viability, microtubule binding and universal formation are not equivalent, and
    no new experiment is required.'
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-schema
  - micro-policy
  - micro-janke2002-publisherpdf
- assessment_id: micro-dash-functions
  area: evidence
  topic: Attachment and ring evidence scope
  outcome: supported
  summary: Purified native complex binds microtubules; localized complex and genetics
    support outer-kinetochore attachment context. Miranda complete primary abstract
    supports recombinant ten-subunit rings/helices, not a newly inspected EM dataset
    or quantified coupling model. The NONMECHANISTIC assembly/function outline stays
    within this scope.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-go-0008608
  - micro-cheeseman2001-jats
  - micro-janke2002-publisherpdf
  - micro-miranda2005-meta
  - micro-graph-policy
- assessment_id: micro-ddk-identity
  area: identity
  topic: Cdc7-Dbf4 heterodimer
  outcome: supported
  summary: GO0031431 exact DDK identity and nuclear protein-complex parent agree with
    Cdc7 catalytic and Dbf4 regulatory roles. Species-qualified narrow synonyms are
    not universal paralogue labels. GO/native annotations support origin activation;
    Bell-Dutta is secondary abstract-only.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-go-0031431
  - micro-go-0140513
  - micro-up-P06243
  - micro-up-P32325
  - micro-pmid-12045100
- assessment_id: micro-ddk-family
  area: grounding
  topic: Exact Dbf4 versus kinase-domain candidates
  outcome: concern
  summary: IPR051590 is an exact Dbf4 family with native P32325 xref/signature, while
    current Dbf4 row remains label-only. IPR013939 is only a central-region domain,
    and native Cdc7 xrefs are broad kinase annotations. Retain inherited minor F1
    without promoting generated description or declaring universal absence of another
    Cdc7 family.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-ipr-IPR051590
  - micro-ipr-IPR013939
  - micro-up-P32325
  - micro-up-P06243
- assessment_id: micro-ddk-examples
  area: grounding
  topic: Current exact Cdc7 and Dbf4 references
  outcome: supported
  summary: P06243 CDC7/YDL017W and P32325 DBF4/YDR052C are reviewed559292 references;
    each exact reviewed gene query is a singleton. These identities corroborate class
    examples without proving detailed phosphorylation chemistry.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-up-P06243
  - micro-up-P32325
  - micro-query-CDC7
  - micro-query-DBF4
  - micro-tax-559292
- assessment_id: micro-ddk-function-graph
  area: graph
  topic: Origin activation remains coarse
  outcome: supported
  summary: GO0006270/0031431 and native curated roles support the declared two-constituent
    FUNCTION/NONMECHANISTIC outline. No MCM-site phosphorylation sequence or Cdc45
    loading edge is asserted, and no fresh Bell full-body or its cited primary experiments
    are claimed.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-go-0006270
  - micro-go-0031431
  - micro-up-P32325
  - micro-pmid-12045100
  - micro-graph-policy
  - micro-native-dbf4_dependent_protein_kinase_complex-causal
- assessment_id: micro-ddk-formation
  area: grounding
  topic: Formation unknown distinct from function
  outcome: unknown
  summary: Two constituents and origin-activation function do not establish a complete
    cross-condition assembly-depletion matrix. UNKNOWN remains appropriately bounded
    outside the concrete exact-family finding; no optional assay requirement is invented.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-schema
  - micro-go-0031431
  - micro-up-P06243
  - micro-up-P32325
- assessment_id: micro-delta-identity
  area: identity
  topic: Generic Polδ and scoped yeast trimer
  outcome: supported
  summary: GO0043625 denotes a variable-composition polymerase complex; current record
    explicitly scopes Pol3/Pol31/Pol32 to budding yeast. OLS confirms DNA-polymerase/nuclear-complex
    is_a, nuclear-replisome part_of and Eukaryota constraint; no species-specific
    composition is universalized.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-go-0043625
  - micro-ols-0043625
  - micro-go-0042575
  - micro-go-0140513
  - micro-go-0043601
  - micro-tax-2759
- assessment_id: micro-delta-stoichiometry
  area: evidence
  topic: Preserved conflict resolved with later primary abstract
  outcome: supported
  summary: Gerik/Burgers1998 primary abstracts support three subunits/reconstitution
    but older dimer inference. Johansson2001 abstract explicitly revises this to1:1:1
    monomeric Polδ, with tested concentration range0.1–20µM and hydrodynamic/two-hybrid
    evidence. Current resolved discussion correctly preserves the GO conflict; no
    raw-data or full-body read is claimed.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-pmid-9677405
  - micro-pmid-9677406
  - micro-pmid-11568188
  - micro-go-0043625
- assessment_id: micro-delta-grounding
  area: grounding
  topic: Bounded candidate scope without invented exact assignments
  outcome: supported
  summary: Pol3 type-B family is broader; Pol31 IPR024826 covers both eukaryotic Polδ
    and archaeal PolII; POLD3/Cdc27 IPR019038 is named but native P47110 lacks an
    InterPro xref. Retain label-only class uncertainty rather than force those candidates
    or assert exhaustive family absence. No new confirmed finding follows.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR050240
  - micro-ipr-IPR024826-retry2
  - micro-ipr-IPR019038-retry
  - micro-up-P15436
  - micro-up-P46957
  - micro-up-P47110
- assessment_id: micro-delta-examples
  area: grounding
  topic: Three exact references and localization tiers
  outcome: supported
  summary: P15436 POL3/YDL102W, P46957 POL31/YJR006W and P47110 POL32/YJR043C are
    reviewed559292 examples and singleton exact queries. P15436 nuclear/Huh link is
    experimental annotation; Pol31/32 nuclear annotations are by similarity and are
    not promoted to newly observed microscopy.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-up-P15436
  - micro-up-P46957
  - micro-up-P47110
  - micro-query-POL3
  - micro-query-POL31
  - micro-query-POL32
  - micro-tax-559292
  - micro-pmid-14562095
- assessment_id: micro-delta-formation
  area: grounding
  topic: Reconstitution and dispensability remain scoped
  outcome: unknown
  summary: Primary abstracts distinguish Polδ* two-subunit enzyme, three-subunit reconstitution
    and pol32 deletion growth/function effects. They do not force every current constituent
    into a universal formation-essential category. UNKNOWN fields are not independently
    defects; no additional experimental requirement.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-schema
  - micro-pmid-9677405
  - micro-pmid-9677406
  - micro-pmid-11568188
- assessment_id: micro-delta-function-graph
  area: graph
  topic: Broad DNA-replication functional outline
  outcome: supported
  summary: Three component_ref contributions and broad GO0006260 function are consistent
    with sources and FUNCTION/NONMECHANISTIC scope. PCNA/RFC clients, catalytic fidelity
    and detailed strand-specific order are not silently asserted as graph constituents
    or steps.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-go-0006260
  - micro-graph-policy
  - micro-pmid-9677406
  - micro-native-delta_dna_polymerase_complex-causal
- assessment_id: micro-diaa-identity
  area: identity
  topic: Free homotetramer separated from larger DNA complex
  outcome: supported
  summary: GO1990125 exact identity is a pair of DiaA homodimers; GO1990102 separately
    contains free DiaA as has_part. The current boundary correctly excludes DnaA and
    oriC from the free tetramer constituents while allowing their functional interaction
    context.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-go-1990125
  - micro-go-1990102
  - micro-ols-1990102
  - micro-go-0032991
  - micro-pmid-17699754
- assessment_id: micro-diaa-family
  area: grounding
  topic: Exact DiaA family distinct from GmhA
  outcome: concern
  summary: IPR023070 is the exact DiaA family with specific HAMAP/NCBIfam signatures
    and native P66817 xref; current class remains label-only. Broader IPR035461/IPR050099
    are not exact substitutes. Retain inherited minor F1.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-ipr-IPR023070-retry
  - micro-ipr-IPR035461
  - micro-ipr-IPR050099-retry2
  - micro-up-P66817
- assessment_id: micro-diaa-example
  area: grounding
  topic: Correct reviewed K12 reference and locus
  outcome: supported
  summary: P66817 is reviewed diaA/yraO, loci b3149/JW3118, tax83333, and the current
    exact gene query returns only that accession. Species562 canonical evidence differs
    from the reference annotation and named K12 experimental derivatives.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-up-P66817
  - micro-query-diaA
  - micro-tax-83333
  - micro-tax-562
  - micro-pmid-17699754
- assessment_id: micro-diaa-function-formation
  area: evidence
  topic: Tetramer function without invariant solution or universal necessity
  outcome: supported
  summary: Complete primary abstract and bounded retained PDF text support the active
    homotetramer and promoted DnaA assembly/initiation. Dilution-dependent dimer/tetramer
    interpretation and speculative phosphosugar regulation remain explicit; UNKNOWN
    does not become a universal essentiality claim. No missing passages, pixels or
    coordinates are certified.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-pmid-17699754
  - micro-keyamura-retained-reader
  - micro-schema
- assessment_id: micro-diaa-graph
  area: graph
  topic: Initiation facilitation is nonmechanistic
  outcome: supported
  summary: Single DiaA constituent→tetramer→replication-initiation outline is bounded
    by GO and primary evidence. Larger DnaA-DNA assembly is deliberately outside constituent
    inventory; no ordered chemical sequence or direct DNA binding by free DiaA is
    asserted.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-graph-policy
  - micro-go-1990125
  - micro-go-0006270
  - micro-pmid-17699754
  - micro-native-diaa_complex-causal
- assessment_id: micro-diaa-module
  area: scope
  topic: Matched dataset and threshold-negative result
  outcome: supported
  summary: Official precise1k is a five-strain E.coli dataset, not the exact K12 mutant
    panel. Verified b3149 is present across201 returned rows with no above-threshold
    membership; there is no hit to summarize as a supporting module. This neither
    refutes DiaA biology nor establishes absence, localization, formation or causal
    regulation.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b3149
- assessment_id: micro-adapter-0
  area: scope
  topic: Actual whole-record applicability
  outcome: concern
  summary: Original formal check exempts source cross-checks because no expression
    assertion exists, despite positive molecular content. Fresh catalogue gives no
    natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k
    locus/threshold data. Historical runner failure is separately dated and is not
    a new execution.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-taxonomy-0
  area: scope
  topic: Taxon and canonical experiment boundaries
  outcome: supported
  summary: Species and reference-strain authorities agree. COMMON is qualitative and
    no universal strain census is inferred. Yeast examples are S288c references, whereas
    native paper preparations/derivatives retain their stated scope; DiaA computational
    five-strain context is distinct from experimental K12 derivatives.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-tax-4932
  - micro-tax-559292
- assessment_id: micro-history-0
  area: provenance
  topic: Append-only history and exact predecessor continuity
  outcome: supported
  summary: Current discussions and original findings/actions were read. Historical
    rationale/posed_date remain provenance, not mandatory current-state inventory;
    current notes/prompt may be narrowed after separately authorized supported curation.
    No neighboring/category/group issue is resolved by inference.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-original-audit
  - micro-delta-0
- assessment_id: micro-schema-0
  area: schema
  topic: Actual original/native checks
  outcome: supported
  summary: All four original pairs pass native validate/render with52 historical inputs
    and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed
    examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological
    or family-completeness certificates.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-original-audit
  - micro-native-dash_complex-verify
  - micro-native-dash_complex-causal
- assessment_id: micro-coverage-0
  area: completeness
  topic: Complete record scope with tier limits
  outcome: supported
  summary: Complete current record and immutable original pair reviewed. No maintained
    images or measured-property rows require pixel/units work. Positive identity/function
    assessments and source-access limits remain explicit, without treating inaccessible
    sources as false.
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-prior-0
- assessment_id: micro-verdict-0
  area: other
  topic: Current independent verdict
  outcome: concern
  summary: 'needs_curation: two inherited minor findings confirmed; current seven-node/edge
    additions supported.'
  target_ids:
  - GO:0042729
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-adapter-1
  area: scope
  topic: Actual whole-record applicability
  outcome: concern
  summary: Original formal check exempts source cross-checks because no expression
    assertion exists, despite positive molecular content. Fresh catalogue gives no
    natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k
    locus/threshold data. Historical runner failure is separately dated and is not
    a new execution.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-taxonomy-1
  area: scope
  topic: Taxon and canonical experiment boundaries
  outcome: supported
  summary: Species and reference-strain authorities agree. COMMON is qualitative and
    no universal strain census is inferred. Yeast examples are S288c references, whereas
    native paper preparations/derivatives retain their stated scope; DiaA computational
    five-strain context is distinct from experimental K12 derivatives.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-tax-4932
  - micro-tax-559292
- assessment_id: micro-history-1
  area: provenance
  topic: Append-only history and exact predecessor continuity
  outcome: supported
  summary: Current discussions and original findings/actions were read. Historical
    rationale/posed_date remain provenance, not mandatory current-state inventory;
    current notes/prompt may be narrowed after separately authorized supported curation.
    No neighboring/category/group issue is resolved by inference.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
  - micro-original-audit
  - micro-delta-1
- assessment_id: micro-schema-1
  area: schema
  topic: Actual original/native checks
  outcome: supported
  summary: All four original pairs pass native validate/render with52 historical inputs
    and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed
    examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological
    or family-completeness certificates.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-original-audit
  - micro-native-dbf4_dependent_protein_kinase_complex-verify
  - micro-native-dbf4_dependent_protein_kinase_complex-causal
- assessment_id: micro-coverage-1
  area: completeness
  topic: Complete record scope with tier limits
  outcome: supported
  summary: Complete current record and immutable original pair reviewed. No maintained
    images or measured-property rows require pixel/units work. Positive identity/function
    assessments and source-access limits remain explicit, without treating inaccessible
    sources as false.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-prior-1
- assessment_id: micro-verdict-1
  area: other
  topic: Current independent verdict
  outcome: concern
  summary: 'needs_curation: inherited minor exact-family finding independently confirmed;
    supported identity/function and remaining unknowns preserved.'
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-adapter-2
  area: scope
  topic: Actual whole-record applicability
  outcome: concern
  summary: Original formal check exempts source cross-checks because no expression
    assertion exists, despite positive molecular content. Fresh catalogue gives no
    natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k
    locus/threshold data. Historical runner failure is separately dated and is not
    a new execution.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-taxonomy-2
  area: scope
  topic: Taxon and canonical experiment boundaries
  outcome: supported
  summary: Species and reference-strain authorities agree. COMMON is qualitative and
    no universal strain census is inferred. Yeast examples are S288c references, whereas
    native paper preparations/derivatives retain their stated scope; DiaA computational
    five-strain context is distinct from experimental K12 derivatives.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-tax-4932
  - micro-tax-559292
- assessment_id: micro-history-2
  area: provenance
  topic: Append-only history and exact predecessor continuity
  outcome: supported
  summary: Current discussions and original findings/actions were read. Historical
    rationale/posed_date remain provenance, not mandatory current-state inventory;
    current notes/prompt may be narrowed after separately authorized supported curation.
    No neighboring/category/group issue is resolved by inference.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
  - micro-original-audit
  - micro-delta-2
- assessment_id: micro-schema-2
  area: schema
  topic: Actual original/native checks
  outcome: supported
  summary: All four original pairs pass native validate/render with52 historical inputs
    and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed
    examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological
    or family-completeness certificates.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-original-audit
  - micro-native-delta_dna_polymerase_complex-verify
  - micro-native-delta_dna_polymerase_complex-causal
- assessment_id: micro-coverage-2
  area: completeness
  topic: Complete record scope with tier limits
  outcome: supported
  summary: Complete current record and immutable original pair reviewed. No maintained
    images or measured-property rows require pixel/units work. Positive identity/function
    assessments and source-access limits remain explicit, without treating inaccessible
    sources as false.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-prior-2
- assessment_id: micro-verdict-2
  area: other
  topic: Current independent verdict
  outcome: supported
  summary: 'pass_with_limitations: no supported scientific finding; identity/composition/function
    positive, exact-family and access limits retained.'
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-adapter-3
  area: scope
  topic: Actual whole-record applicability
  outcome: concern
  summary: Original formal check exempts source cross-checks because no expression
    assertion exists, despite positive molecular content. Fresh catalogue gives no
    natural yeast match for DASH/DDK/Polδ; DiaA is assessed against actual precise1k
    locus/threshold data. Historical runner failure is separately dated and is not
    a new execution.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-ecoli-meta
  - micro-ecoli-gene-b3149
- assessment_id: micro-taxonomy-3
  area: scope
  topic: Taxon and canonical experiment boundaries
  outcome: supported
  summary: Species and reference-strain authorities agree. COMMON is qualitative and
    no universal strain census is inferred. Yeast examples are S288c references, whereas
    native paper preparations/derivatives retain their stated scope; DiaA computational
    five-strain context is distinct from experimental K12 derivatives.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-tax-562
  - micro-tax-83333
  - micro-pmid-17699754
- assessment_id: micro-history-3
  area: provenance
  topic: Append-only history and exact predecessor continuity
  outcome: supported
  summary: Current discussions and original findings/actions were read. Historical
    rationale/posed_date remain provenance, not mandatory current-state inventory;
    current notes/prompt may be narrowed after separately authorized supported curation.
    No neighboring/category/group issue is resolved by inference.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-policy
  - micro-original-audit
  - micro-delta-3
- assessment_id: micro-schema-3
  area: schema
  topic: Actual original/native checks
  outcome: supported
  summary: All four original pairs pass native validate/render with52 historical inputs
    and8 original artifact hashes checked. Own current inventories are7/2/3/1 reviewed
    examples and7/2/3/1 COVERED typed nodes, respectively; these checks are not biological
    or family-completeness certificates.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-original-audit
  - micro-native-diaa_complex-verify
  - micro-native-diaa_complex-causal
- assessment_id: micro-coverage-3
  area: completeness
  topic: Complete record scope with tier limits
  outcome: supported
  summary: Complete current record and immutable original pair reviewed. No maintained
    images or measured-property rows require pixel/units work. Positive identity/function
    assessments and source-access limits remain explicit, without treating inaccessible
    sources as false.
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-prior-3
- assessment_id: micro-verdict-3
  area: other
  topic: Current independent verdict
  outcome: concern
  summary: 'needs_curation: inherited minor exact-family finding independently confirmed;
    supported identity/function and remaining unknowns preserved.'
  target_ids:
  - GO:1990125
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-policy
- assessment_id: micro-kind-complex49-agent-bell2002-publisher
  area: provenance
  topic: Historical failed access kind correction
  outcome: concern
  summary: Original response honestly says failed body access and context_only, but
    is typed database. Correct only to validation/context_only; do not accuse the
    original of an unread-body claim, replace its timestamp or infer a scientific
    contradiction.
  target_ids:
  - GO:0031431
  evidence_ids:
  - micro-prior-1
  - micro-historical-complex49-agent-bell2002-publisher
- assessment_id: micro-kind-complex49-agent-burgers1998-pdf
  area: provenance
  topic: Historical failed access kind correction
  outcome: concern
  summary: Original response honestly says failed body access and context_only, but
    is typed database. Correct only to validation/context_only; do not accuse the
    original of an unread-body claim, replace its timestamp or infer a scientific
    contradiction.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-prior-2
  - micro-historical-complex49-agent-burgers1998-pdf
- assessment_id: micro-kind-complex49-agent-johansson2001-doi
  area: provenance
  topic: Historical failed access kind correction
  outcome: concern
  summary: Original response honestly says failed body access and context_only, but
    is typed database. Correct only to validation/context_only; do not accuse the
    original of an unread-body claim, replace its timestamp or infer a scientific
    contradiction.
  target_ids:
  - GO:0043625
  evidence_ids:
  - micro-prior-2
  - micro-historical-complex49-agent-johansson2001-doi
- assessment_id: plaque-t1-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: One REVIEWED P14904 example and one COVERED typed node. Original native
    pair/historical provenance and current frozen inputs all pass.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-original-current-validation
  - plaque-schema
  - plaque-native-cvt_complex-verify
  - plaque-native-cvt_complex-causal
- assessment_id: plaque-t1-structured-source
  area: evidence
  topic: structured source
  outcome: supported
  summary: The original checks[4] formal exemption is based solely on absence of an
    expression-module assertion. Whole-record positive APE1/Atg19/Atg11/Cvt pathway
    claims trigger native applicability assessment. Fresh official coverage has no
    matching biological host; no downstream foreign-host proxy. Historical runner
    failure remains separately dated.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-original-1-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t1-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Full maintained fields read. No images or quantitative physical properties
    occur. No optional protein inventory, image, broader family mapping or new experiment
    is mandated solely because a slot is empty.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t1-evidence-access
  area: evidence
  topic: evidence access
  outcome: supported
  summary: All direct cited DOI/PMID identities and complete indexed abstracts read;
    actual genuine primary body scopes are separately named. Unavailable routes and
    retained retrieval times are explicit; no snippets, figure pixels, supplementary
    or raw-data analyses invented.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-access-limitations
  - plaque-scott2001-retained-body
  - plaque-shintani2004-retained-body
- assessment_id: plaque-t1-taxon-scope
  area: scope
  topic: taxon scope
  outcome: supported
  summary: Natural S.cerevisiae species scope is supported; S288C accession reference
    is not conflated with SEY6210-derived primary experiments or recombinant E.coli/rabbit
    systems.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-scott2001-retained-body
  - plaque-shintani2004-retained-body
- assessment_id: plaque-t2-native-validation
  area: schema
  topic: native validation
  outcome: supported
  summary: Zero protein_examples and zero typed GENE_OR_PROTEIN nodes; empty-inventory
    pass is not molecular completeness evidence. Original native pair/historical provenance
    and current frozen inputs all pass.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-original-current-validation
  - plaque-schema
  - plaque-native-cytostome-verify
  - plaque-native-cytostome-causal
- assessment_id: plaque-t2-structured-source
  area: evidence
  topic: structured source
  outcome: supported
  summary: The original checks[4] formal exemption is based solely on absence of an
    expression-module assertion. Whole-record positive endocytic pathway and localized-protein
    discussion claims trigger native applicability assessment. Fresh official coverage
    has no matching biological host; no downstream foreign-host proxy. Historical
    runner failure remains separately dated.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t2-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Full maintained fields read. No images or quantitative physical properties
    occur. No optional protein inventory, image, broader family mapping or new experiment
    is mandated solely because a slot is empty.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t2-evidence-access
  area: evidence
  topic: evidence access
  outcome: supported
  summary: All direct cited DOI/PMID identities and complete indexed abstracts read;
    actual genuine primary body scopes are separately named. Unavailable routes and
    retained retrieval times are explicit; no snippets, figure pixels, supplementary
    or raw-data analyses invented.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-access-limitations
  - plaque-chasen2020-s3
  - plaque-paper-5
  - plaque-paper-6
  - plaque-paper-7
- assessment_id: plaque-t2-taxon-scope
  area: scope
  topic: taxon scope
  outcome: supported
  summary: T.cruzi epimastigote structural/canonical claim matches Alcantara abstract;
    Chasen Y-strain epimastigotes and replicative amastigotes are scoped, without
    requiring record expansion to every life stage or universal exclusivity.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-tax-5693
  - plaque-paper-7
  - plaque-chasen2020-s3
- assessment_id: plaque-t1-identity-boundary
  area: identity
  topic: identity boundary
  outcome: concern
  summary: GO0034270 is exactly the Cvt complex, parent protein-containing complex/cytoplasm
    parthood supported. Its short preApe1-only wording is genuinely copied from GO,
    but the active Atg19/Atg11 categorical exclusion conflicts with cited Shintani
    and GO0032258. Preserve the authority-text conflict rather than call the definition
    fabricated.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-protein-P14904
  - plaque-shintani2004-retained-body
  - plaque-scott2001-retained-body
- assessment_id: plaque-t1-cargo-receptor-composition
  area: representation
  topic: cargo receptor composition
  outcome: concern
  summary: Shintani S8 calls Atg19-Ape1 the Cvt complex; S10 includes Ape1/Ams1/Atg19
    and distinguishes Atg11 recruitment machinery. Scott shows precursor-specific
    association and cotransport/degradation. Receptor binding is not merely a transient
    before-assembly chaperone action; a blanket constituent exclusion needs correction,
    without adding every Atg factor.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-policy
  - plaque-shintani2004-retained-body
  - plaque-scott2001-retained-body
- assessment_id: plaque-t1-protein-grounding
  area: grounding
  topic: protein grounding
  outcome: supported
  summary: P14904 reviewed S288C APE1/precursor identity and exact gene query are
    correct. The three vacuolar-localization PMID joins are real and support localization,
    not automatically Cvt membership. Broad M18 family/domain2 candidates do not force
    an exact cargo-class grounding.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-protein-P14904
  - plaque-gene-APE1
  - plaque-ipr-IPR001948
  - plaque-ipr-IPR023358
  - plaque-paper-2
  - plaque-paper-3
  - plaque-paper-4
  - plaque-policy
- assessment_id: plaque-t1-necessity
  area: scope
  topic: necessity
  outcome: unknown
  summary: Ape1 is the defining cargo core, supporting its constitutive membership.
    PAS organization/transport under growing conditions and starvation contrasts do
    not establish universal physical assembly necessity for every receptor/scaffold
    or require a new assay. This bounded uncertainty does not create a second finding.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-schema
  - plaque-shintani2004-retained-body
  - plaque-scott2001-retained-body
- assessment_id: plaque-t1-graph
  area: graph
  topic: graph
  outcome: concern
  summary: Coarse membership, double-membrane enclosure and vacuolar delivery topology
    are supported; the graph description should distinguish Ape1 self-assembly from
    Atg19-containing complex formation. NONMECHANISTIC scope does not cure an explicit
    constituent boundary error.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-shintani2004-retained-body
- assessment_id: plaque-t1-history
  area: provenance
  topic: history
  outcome: supported
  summary: Retain exact original F1 lineage. The current active resolution_note is
    challenged; dated rationale/posed_date/history must be preserved with appended
    evidence and an updated active status/note. No rewriting historical failed searches
    or inferring a prior issue resolution.
  target_ids:
  - GO:0034270
  evidence_ids:
  - plaque-original-1-yaml
  - plaque-current-1
  - plaque-policy
- assessment_id: plaque-t2-identity-hierarchy-refresh
  area: identity
  topic: identity hierarchy refresh
  outcome: supported
  summary: Fresh GO directly supports is_a GO0110165 and part_of GO0005886. Current
    changed parent/parthood/evidence/history removes precisely the old hierarchy error.
    Definition remains the stable ingestion structure, with larger cytopharynx boundary
    explicitly deferred.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-cytostome-delta
  - plaque-go
  - plaque-cytostome-path
  - plaque-schema
- assessment_id: plaque-t2-resolved-lineage
  area: provenance
  topic: resolved lineage
  outcome: supported
  summary: Original F1 cytostome-plasma-membrane-parthood is resolved on inspected
    current bytes. Already-closed2461 documents prior curation, not a fix made by
    this PR; no terminal disposition of the other grouped2461 records or uninspected
    prior category observations.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-cytostome-delta
  - plaque-go
  - plaque-cytostome-path
  - plaque-issue2461-context
- assessment_id: plaque-t2-composition
  area: grounding
  topic: composition
  outcome: supported
  summary: Chasen establishes endogenous CP1 localization and associated/overexpressed
    CP2/3 across the larger complex. Predicted coiled-coil/SMC regions are not exact
    entire-protein classes or proof of a three-component opening assembly; existing
    targeted TODO is legitimate.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-chasen2020-s3
  - plaque-policy
- assessment_id: plaque-t2-necessity
  area: scope
  topic: necessity
  outcome: supported
  summary: No molecular essentiality is asserted; localization, co-isolation and cytochalasin
    uptake inhibition do not alone establish protein-deletion assembly necessity.
    No mandatory empty protein example finding.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-chasen2020-s3
  - plaque-schema
- assessment_id: plaque-t2-uptake-graph
  area: graph
  topic: uptake graph
  outcome: supported
  summary: Porto complete abstract supports the coarse cytostome/cytopharynx entry
    to an early vesicular-tubular network and reservosome storage; Chasen protein
    feeding reinforces entry. Frozen local reservosome destination is exact. The NONMECHANISTIC
    graph does not claim universal kinetics, molecular machinery or exclusive uptake
    in all stages. Lipid-specific experimental details remain outside the inspected
    Porto abstract; no unread body is certified.
  target_ids:
  - GO:0031910
  evidence_ids:
  - plaque-current-2
  - plaque-paper-6
  - plaque-chasen2020-s3
  - plaque-reservosome-context
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: supported
  summary: Local CulE association identity and broader CRLparent preserve the divergent
    source-defined scaffold; Hu2017 WDR1 complex has another cullin locus.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-molecules
  area: grounding
  topic: Molecular identity and scoped inventory
  outcome: concern
  summary: Q383D5→sourceCulE andQ38C61→sourceRbx1 verified by native locus bridges;
    Q384S1/Tb11.02.5340/212aa is wrong for sourceSkp1.2/Tb927.9.8370/158aa. Q38ED0
    nativeVEuPathDB/Ensembl bridge identifies replacement. ORF names differ from formal
    primary genes; generated names are not membership evidence.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-up-Q383D5
  - septin-up-Q38C61
  - septin-up-Q384S1
  - septin-up-Q38ED0
  - septin-ensembl-skp12
  - septin-protein-policy
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-families
  area: grounding
  topic: Family and class boundaries
  outcome: supported
  summary: Broad Cullin,RING-box,SKP1-like families do not discriminate the source
    paralogs or establish one obligatory four-kelch cassette; generated IPR051031
    prose excluded. Generic scaffold/adaptor classes are permitted and UNKNOWN necessities
    are honest.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-curation-policy
  - septin-ipr-045093
  - septin-ipr-051031
  - septin-ipr-001232
  - septin-ipr-016897
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-formation
  area: evidence
  topic: Formation necessity and untested mechanisms
  outcome: unknown
  summary: Co-isolation and RNAi cellular outputs do not test persistence of a complete
    complex without each constituent. UNKNOWN formation necessities remain appropriate;
    no direct contact,simultaneous occupancy or absolute stoichiometry inferred.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-schema-policy
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-graph
  area: graph
  topic: Every maintained graph actor and edge
  outcome: supported
  summary: Five intervention-output edges preserve distinct24hLFQ,0–36h1K2N and representative
    Golgi observations. Increased KKT9/decreasedTb927.10.8810 are abundance readouts,
    not direct substrates or degradation rates; no PLK/WDR1 mechanism imported.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-graph-policy
  - septin-fig6
  - septin-fig7
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-taxon
  area: scope
  topic: Taxonomy, canonical examples and experimental scopes
  outcome: supported
  summary: Tbrucei5691/TREU927185431 resolve. PCF Lister427 isolation,2T1qPCR,incompletely
    specifiedRNAi stage and Fig6bloodstream schematic remain distinct. Reference927release42
    database is not cultured strain; no scope transfer from bacterial recombinant
    hosts.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-tax-5691
  - septin-tax-185431
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-quantity
  area: quantity
  topic: Quantities, timing and dimensions
  outcome: supported
  summary: Four enriched kelch loci do not imply four copies or simultaneous occupancy.
    ActualFig6timepoints0/12/24/36h,Fig7threeinduced/threeuninduced and representative
    Golgi images remain distinct; no pie rounding recast as rawcounts. PRIDEsixWT
    versusMethods/S3sevenWT controls preserved. No physical complex dimensions inferred.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-fig2
  - septin-fig6
  - septin-fig7
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-sources
  area: evidence
  topic: Source tiers and exact read extents
  outcome: supported
  summary: Genuine2025JATS,S3boundedrows and actualFig2/6/7pixels support the scoped
    claims. Hu2017sec004/Methods delineate conflicting olderCullin4 association. Metadata/nativeaccession
    resolution is not direct ligase activity; no raw spectra or full-workbook reanalysis.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-literature-policy
  - septin-pmid-41413177
  - septin-pmid-28052114
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-image
  area: evidence
  topic: Image access and attribution
  outcome: supported
  summary: No maintained image. Fresh externalFig2allpanels/Fig6A–D/Fig7actualpixels
    viewed against captions and CC-BY4.0 source; these depict enrichment/phenotype/proteomics,
    not an imaged CulE particle. Fig8onlycaption read, generic human model remains
    explicitly excluded as exact structure.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-fig2
  - septin-fig6
  - septin-fig7
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-coverage
  area: completeness
  topic: Complete record and native inventory coverage
  outcome: supported
  summary: Three unreviewed example occurrences/three distinct accessions and one
    native COVERED Cullin-E node. Native pass does not establish the disputed Skp1.2
    biological assignment. Four constituent classes,assay outputs,dataset and unresolved
    architecture well scoped; wrongSkp1.2 and current staleexample discussion are
    addressed by inherited action. No extra unrelated coisolates promoted to mandatory
    subunits.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-native-cullin_e_ubiquitin_ligase_complex-verify
  - septin-native-cullin_e_ubiquitin_ligase_complex-causal
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-history
  area: provenance
  topic: Historical rationale and prior observations
  outcome: supported
  summary: Dated rationale/history and actual earlier source-access observations remain
    append-only. Current notes/prompts may be corrected or dated clarification appended.
    No neighboring/group issue resolution, false historical search claim, or rewriting
    original bundles.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-curation-policy
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-schema
  area: schema
  topic: Frozen inputs and deterministic original pair
  outcome: supported
  summary: Native original validate/render0 and exact Markdown; 14 historical input
    occurrences match source. Current target unchanged. Original batch26 global gate
    scope is a valid historical execution origin, not current-head attestation.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-original-validation
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive molecular,source-locus,ubiquitylation and proteomics assertions
    trigger coverage assessment. Fresh complete official catalogue lacks matchingTrypanosoma/strains;
    no relevant downstream module query and no unrelated host proxy. Historicalrunnerunavailable
    remains separate from currentfallback; original expression-only exclusion corrected.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-cullin_e_ubiquitin_ligase_complex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: Needs curation for one independently confirmed inherited major wrongSkp1.2accession;
    other positive scoped assessments and uncertainty retained.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
- assessment_id: septin-dinoflagellate_antapex-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: concern
  summary: Exact GO antapex class is intended, but maintained anterior definition
    repeats GO0097684 error and conflicts with expert posterior orientation and its
    own posterior notch edge.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
- assessment_id: septin-dinoflagellate_antapex-molecules
  area: grounding
  topic: Molecular identity and scoped inventory
  outcome: supported
  summary: No components/gene symbols/protein instances are asserted. Historical OPEN
    discussion requests specifically localized constituents; generic whole-cell membranes/cellulose/proteins
    are not automatically regional constituents. No missing optional field or family/complex
    typing defect manufactured.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_antapex-families
  area: grounding
  topic: Family and class boundaries
  outcome: supported
  summary: Horn versus general regional class and parent compartment remain separate.
    No generic dinoflagellate molecular family is assigned to the regional point;
    no exact-family requirement invented.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_antapex-formation
  area: evidence
  topic: Formation necessity and untested mechanisms
  outcome: unknown
  summary: Morphological topology and class constraints do not establish localized
    constituent formation requirements or molecular mechanism. No component essentiality
    claim exists to validate.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_antapex-graph
  area: graph
  topic: Every maintained graph actor and edge
  outcome: supported
  summary: Six structure nodes/five edges retain class,hypocone parthood,horn subclass,notch-to-sulcus
    and posterior extension; posterior edge remains correct despite contradictory
    top-level definition.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-graph-policy
- assessment_id: septin-dinoflagellate_antapex-taxon
  area: scope
  topic: Taxonomy, canonical examples and experimental scopes
  outcome: supported
  summary: GO only_in_taxon2864 and ENA Dinophyceaeclass support taxonomic restriction.
    VARIABLE is qualitative; no quantitative census established. Horn thecate qualifier
    and optional morphological features remain bounded.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
- assessment_id: septin-dinoflagellate_antapex-quantity
  area: quantity
  topic: Quantities, timing and dimensions
  outcome: supported
  summary: No size,stoichiometry or rate asserted; topological/morphological wording
    does not supply quantitative population frequency or universal horn/groove presence.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
- assessment_id: septin-dinoflagellate_antapex-sources
  area: evidence
  topic: Source tiers and exact read extents
  outcome: supported
  summary: Current GO/ENA and authored expert morphology are authority evidence. Taylor1980,
    where cited, is complete native abstract/bibliographic corroboration only; publisher403
    is validation context, not primary body support. No morphology figure pixels or
    uninspected paper body claimed.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-literature-policy
- assessment_id: septin-dinoflagellate_antapex-image
  area: evidence
  topic: Image access and attribution
  outcome: not_applicable
  summary: No maintained image; expert-page captions and text inspected, no dinoflagellate
    pixels or uninspected Taylor figures certified.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
- assessment_id: septin-dinoflagellate_antapex-coverage
  area: completeness
  topic: Complete record and native inventory coverage
  outcome: supported
  summary: Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native
    checks cover this empty molecular inventory, not unasserted localization/formation.No
    automatic optionalprotein,canonicalspecies,image,dimension or molecularmechanism
    requirement. Correct regional boundaries and uncertainty remain positively assessed.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  - septin-native-dinoflagellate_antapex-verify
  - septin-native-dinoflagellate_antapex-causal
- assessment_id: septin-dinoflagellate_antapex-history
  area: provenance
  topic: Historical rationale and prior observations
  outcome: supported
  summary: Dated rationale/history and actual earlier source-access observations remain
    append-only. Current notes/prompts may be corrected or dated clarification appended.
    No neighboring/group issue resolution, false historical search claim, or rewriting
    original bundles.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_antapex-schema
  area: schema
  topic: Frozen inputs and deterministic original pair
  outcome: supported
  summary: Native original validate/render0 and exact Markdown; 15 historical input
    occurrences match source. Current target unchanged. Original batch26 global gate
    scope is a valid historical execution origin, not current-head attestation.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-original-validation
- assessment_id: septin-dinoflagellate_antapex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Complete record makes morphology/topology claims and explicitly defers
    molecular constituents/mechanisms. Original prose physical-scope exclusion is
    legitimate; absent formal adapter row is not a defect. Catalogue also has no matchingDinophyceae,
    but actual morphology scope—not biological absence—establishes exclusion.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-dinoflagellate_antapex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: Needs curation for one independently confirmed inherited major anterior/posterior
    definition reversal; other positive scoped assessments and uncertainty retained.
  target_ids:
  - GO:0097684
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
- assessment_id: septin-dinoflagellate_antapical_horn-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: supported
  summary: Exact GO0097687 horn is the thecate specialization of antapex; direct class
    relation and inherited hypocone containment are correctly distinguished. It does
    not repeat parent anterior error.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
- assessment_id: septin-dinoflagellate_antapical_horn-molecules
  area: grounding
  topic: Molecular identity and scoped inventory
  outcome: supported
  summary: No components/gene symbols/protein instances are asserted. Historical OPEN
    discussion requests specifically localized constituents; generic whole-cell membranes/cellulose/proteins
    are not automatically regional constituents. No missing optional field or family/complex
    typing defect manufactured.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_antapical_horn-families
  area: grounding
  topic: Family and class boundaries
  outcome: supported
  summary: Horn versus general regional class and parent compartment remain separate.
    No generic dinoflagellate molecular family is assigned to the regional point;
    no exact-family requirement invented.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_antapical_horn-formation
  area: evidence
  topic: Formation necessity and untested mechanisms
  outcome: unknown
  summary: Morphological topology and class constraints do not establish localized
    constituent formation requirements or molecular mechanism. No component essentiality
    claim exists to validate.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_antapical_horn-graph
  area: graph
  topic: Every maintained graph actor and edge
  outcome: supported
  summary: Three structure nodes/three edges distinguish direct horn is_a antapex,parent
    part_of hypocone and inferred horn parthood; nonmechanistic and no falsely direct
    ontology parthood assertion.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-graph-policy
- assessment_id: septin-dinoflagellate_antapical_horn-taxon
  area: scope
  topic: Taxonomy, canonical examples and experimental scopes
  outcome: supported
  summary: GO only_in_taxon2864 and ENA Dinophyceaeclass support taxonomic restriction.
    VARIABLE is qualitative; no quantitative census established. Horn thecate qualifier
    and optional morphological features remain bounded.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
- assessment_id: septin-dinoflagellate_antapical_horn-quantity
  area: quantity
  topic: Quantities, timing and dimensions
  outcome: supported
  summary: No size,stoichiometry or rate asserted; topological/morphological wording
    does not supply quantitative population frequency or universal horn/groove presence.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
- assessment_id: septin-dinoflagellate_antapical_horn-sources
  area: evidence
  topic: Source tiers and exact read extents
  outcome: supported
  summary: Current GO/ENA and authored expert morphology are authority evidence. Taylor1980,
    where cited, is complete native abstract/bibliographic corroboration only; publisher403
    is validation context, not primary body support. No morphology figure pixels or
    uninspected paper body claimed.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-literature-policy
  - septin-pmid-7002229
  - septin-taylor-publisher
- assessment_id: septin-dinoflagellate_antapical_horn-image
  area: evidence
  topic: Image access and attribution
  outcome: not_applicable
  summary: No maintained image; expert-page captions and text inspected, no dinoflagellate
    pixels or uninspected Taylor figures certified.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
- assessment_id: septin-dinoflagellate_antapical_horn-coverage
  area: completeness
  topic: Complete record and native inventory coverage
  outcome: supported
  summary: Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native
    checks cover this empty molecular inventory, not unasserted localization/formation.No
    automatic optionalprotein,canonicalspecies,image,dimension or molecularmechanism
    requirement. Correct regional boundaries and uncertainty remain positively assessed.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
  - septin-native-dinoflagellate_antapical_horn-verify
  - septin-native-dinoflagellate_antapical_horn-causal
- assessment_id: septin-dinoflagellate_antapical_horn-history
  area: provenance
  topic: Historical rationale and prior observations
  outcome: supported
  summary: Dated rationale/history and actual earlier source-access observations remain
    append-only. Current notes/prompts may be corrected or dated clarification appended.
    No neighboring/group issue resolution, false historical search claim, or rewriting
    original bundles.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_antapical_horn-schema
  area: schema
  topic: Frozen inputs and deterministic original pair
  outcome: supported
  summary: Native original validate/render0 and exact Markdown; 15 historical input
    occurrences match source. Current target unchanged. Original batch26 global gate
    scope is a valid historical execution origin, not current-head attestation.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-original-validation
- assessment_id: septin-dinoflagellate_antapical_horn-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Complete record makes morphology/topology claims and explicitly defers
    molecular constituents/mechanisms. Original prose physical-scope exclusion is
    legitimate; absent formal adapter row is not a defect. Catalogue also has no matchingDinophyceae,
    but actual morphology scope—not biological absence—establishes exclusion.
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-dinoflagellate_antapical_horn-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: supported
  summary: 'Pass with limitations: exact morphology/topology positively supported;
    no confirmed record finding. Parent antapex definition issue is not duplicated
    because this target does not repeat the erroneous direction; no molecular/quantitative
    scope invented.'
  target_ids:
  - GO:0097687
  evidence_ids:
  - septin-record-dinoflagellate_antapical_horn
  - septin-original-dinoflagellate_antapical_horn
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097687-history
  - septin-go-0097687-constraints
- assessment_id: septin-dinoflagellate_apex-identity
  area: identity
  topic: Exact structure identity and boundaries
  outcome: supported
  summary: Exact GO0097683 anterior apex of epicone and broader cellular-anatomical
    parent are supported. Narrower horn and possible groove remain distinct, not universal
    features.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
- assessment_id: septin-dinoflagellate_apex-molecules
  area: grounding
  topic: Molecular identity and scoped inventory
  outcome: supported
  summary: No components/gene symbols/protein instances are asserted. Historical OPEN
    discussion requests specifically localized constituents; generic whole-cell membranes/cellulose/proteins
    are not automatically regional constituents. No missing optional field or family/complex
    typing defect manufactured.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_apex-families
  area: grounding
  topic: Family and class boundaries
  outcome: supported
  summary: Horn versus general regional class and parent compartment remain separate.
    No generic dinoflagellate molecular family is assigned to the regional point;
    no exact-family requirement invented.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_apex-formation
  area: evidence
  topic: Formation necessity and untested mechanisms
  outcome: unknown
  summary: Morphological topology and class constraints do not establish localized
    constituent formation requirements or molecular mechanism. No component essentiality
    claim exists to validate.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-schema-policy
- assessment_id: septin-dinoflagellate_apex-graph
  area: graph
  topic: Every maintained graph actor and edge
  outcome: supported
  summary: Five structure nodes/four edges retain apexclass,epiconeparthood,hornsubclass
    and groovefound-on relation; no groove presence in every dinoflagellate is asserted.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-graph-policy
- assessment_id: septin-dinoflagellate_apex-taxon
  area: scope
  topic: Taxonomy, canonical examples and experimental scopes
  outcome: supported
  summary: GO only_in_taxon2864 and ENA Dinophyceaeclass support taxonomic restriction.
    VARIABLE is qualitative; no quantitative census established. Horn thecate qualifier
    and optional morphological features remain bounded.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
- assessment_id: septin-dinoflagellate_apex-quantity
  area: quantity
  topic: Quantities, timing and dimensions
  outcome: supported
  summary: No size,stoichiometry or rate asserted; topological/morphological wording
    does not supply quantitative population frequency or universal horn/groove presence.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
- assessment_id: septin-dinoflagellate_apex-sources
  area: evidence
  topic: Source tiers and exact read extents
  outcome: supported
  summary: Current GO/ENA and authored expert morphology are authority evidence. Taylor1980,
    where cited, is complete native abstract/bibliographic corroboration only; publisher403
    is validation context, not primary body support. No morphology figure pixels or
    uninspected paper body claimed.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-literature-policy
  - septin-pmid-7002229
  - septin-taylor-publisher
- assessment_id: septin-dinoflagellate_apex-image
  area: evidence
  topic: Image access and attribution
  outcome: not_applicable
  summary: No maintained image; expert-page captions and text inspected, no dinoflagellate
    pixels or uninspected Taylor figures certified.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
- assessment_id: septin-dinoflagellate_apex-coverage
  area: completeness
  topic: Complete record and native inventory coverage
  outcome: supported
  summary: Zero example occurrences and zero GENE_OR_PROTEIN nodes; successful native
    checks cover this empty molecular inventory, not unasserted localization/formation.No
    automatic optionalprotein,canonicalspecies,image,dimension or molecularmechanism
    requirement. Correct regional boundaries and uncertainty remain positively assessed.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
  - septin-native-dinoflagellate_apex-verify
  - septin-native-dinoflagellate_apex-causal
- assessment_id: septin-dinoflagellate_apex-history
  area: provenance
  topic: Historical rationale and prior observations
  outcome: supported
  summary: Dated rationale/history and actual earlier source-access observations remain
    append-only. Current notes/prompts may be corrected or dated clarification appended.
    No neighboring/group issue resolution, false historical search claim, or rewriting
    original bundles.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-curation-policy
- assessment_id: septin-dinoflagellate_apex-schema
  area: schema
  topic: Frozen inputs and deterministic original pair
  outcome: supported
  summary: Native original validate/render0 and exact Markdown; 15 historical input
    occurrences match source. Current target unchanged. Original batch26 global gate
    scope is a valid historical execution origin, not current-head attestation.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-original-validation
- assessment_id: septin-dinoflagellate_apex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: not_applicable
  summary: Complete record makes morphology/topology claims and explicitly defers
    molecular constituents/mechanisms. Original prose physical-scope exclusion is
    legitimate; absent formal adapter row is not a defect. Catalogue also has no matchingDinophyceae,
    but actual morphology scope—not biological absence—establishes exclusion.
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-dinoflagellate_apex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: supported
  summary: 'Pass with limitations: exact morphology/topology positively supported;
    no confirmed record finding. Parent antapex definition issue is not duplicated
    because this target does not repeat the erroneous direction; no molecular/quantitative
    scope invented.'
  target_ids:
  - GO:0097683
  evidence_ids:
  - septin-record-dinoflagellate_apex
  - septin-original-dinoflagellate_apex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097683-history
  - septin-go-0097683-constraints
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  - GO:0034270
  - GO:0031910
  - GO:0042729
  - GO:0031431
  - GO:0043625
  - GO:1990125
  - GO:0097684
  - GO:0097687
  - GO:0097683
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
  issue_key: dash-seven-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the seven named DASH subunit classes
  description: 'Seven exact family entries are available: DUO1 IPR013960, DAM1 IPR013962,
    DAD1 IPR013958, DAD2 IPR013963, ASK1 IPR013964, SPC19 IPR013251, SPC34 IPR013966.
    Their reviewed examples independently carry these family xrefs, while current
    rows defer exact mappings.'
  target_ids:
  - GO:0042729
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - components[4].grounding_status
  - components[5].grounding_status
  - components[6].grounding_status
  - discussions#resolve_dash_subunit_boundaries
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR013960
  - micro-ipr-IPR013962-retry
  - micro-ipr-IPR013958
  - micro-ipr-IPR013963-retry
  - micro-ipr-IPR013964
  - micro-ipr-IPR013251
  - micro-ipr-IPR013966-retry2
  - micro-up-P53168
  - micro-up-P53267
  - micro-up-Q12248
  - micro-up-P36162
  - micro-up-P35734
  - micro-up-Q03954
  - micro-up-P36131
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dash_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and condition-scoped formation evidence
  native_severity: minor
  normalization_reason: The complex identity, correct protein examples and supported
    function remain intact; this is a bounded current grounding or explicitly tested
    formation-evidence gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052919Z-dash-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2908
- finding_id: micro-F2
  issue_key: dash-spc34-tested-association
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Capture the tested Spc34 formation requirement
  description: 'Current Spc34 row omits the directly inspected Janke2002 p182/Fig1B
    condition-specific physical-association/recovery result: after4h37C, spc34-3 Dad2-ProA
    purification yields only bait, while matched SPC34 recovers the reported DDD complex.
    The minor gap is this concrete association/stability evidence, not UNKNOWN alone
    or a universal viability/formation claim.'
  target_ids:
  - GO:0042729
  field_paths:
  - components#spc34_dash_subunit.essentiality
  - components#spc34_dash_subunit.evidence
  evidence_ids:
  - micro-record-0
  - micro-schema
  - micro-policy
  - micro-janke2002-publisherpdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dash_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and condition-scoped formation evidence
  native_severity: minor
  normalization_reason: The complex identity, correct protein examples and supported
    function remain intact; this is a bounded current grounding or explicitly tested
    formation-evidence gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052919Z-dash-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2909
- finding_id: micro-F3
  issue_key: ddk-dbf4-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use the exact Dbf4 regulatory-subunit family
  description: The Dbf4 row remains REVIEWED_LABEL_ONLY even though IPR051590 directly
    identifies the DDK regulatory family and is linked to the correct reviewed example.
    Its generated description is not used as primary evidence. Cdc7 kinase-domain
    candidates remain broader.
  target_ids:
  - GO:0031431
  field_paths:
  - components#dbf4_regulatory_subunit.grounding_status
  - discussions#resolve_ddk_subunit_groundings
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-ipr-IPR051590
  - micro-up-P32325
  - micro-up-P06243
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and condition-scoped formation evidence
  native_severity: minor
  normalization_reason: The complex identity, correct protein examples and supported
    function remain intact; this is a bounded current grounding or explicitly tested
    formation-evidence gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2910
- finding_id: micro-F4
  issue_key: diaa-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground DiaA with its verified exact family
  description: The sole DiaA row remains REVIEWED_LABEL_ONLY despite exact family
    IPR023070 and the native P66817 xref. DiaA-specific integrated signatures distinguish
    it from broader GmhA/DiaA and SIS families.
  target_ids:
  - GO:1990125
  field_paths:
  - components#diaa_regulator.grounding_status
  - discussions#resolve_diaa_grounding
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-ipr-IPR023070-retry
  - micro-ipr-IPR035461
  - micro-ipr-IPR050099-retry2
  - micro-up-P66817
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/diaa_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and condition-scoped formation evidence
  native_severity: minor
  normalization_reason: The complex identity, correct protein examples and supported
    function remain intact; this is a bounded current grounding or explicitly tested
    formation-evidence gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052921Z-diaa-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2911
- finding_id: plaque-t1-F1
  issue_key: cvt-cargo-receptor-boundary
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Distinguish the Ape1 cargo core from the Atg19-containing Cvt complex
  description: The current active RESOLVED discussion excludes Atg19 with Atg11. Independently
    inspected Shintani S8/S10 explicitly distinguishes the Atg19-containing Cvt cargo-receptor
    complex from Ape1 cargo self-assembly and Atg11 delivery machinery; Scott native
    association/cotransport and fresh GO0032258/P14904 corroborate. The short GO0034270
    definition is accurately copied but incomplete relative to these sources. Reconcile
    current constituent/graph boundaries while preserving historical rationale and
    not requiring every Atg factor as a constituent.
  target_ids:
  - GO:0034270
  field_paths:
  - definition
  - components
  - causal_graphs#cvt_complex_vacuolar_delivery
  - discussions#atg_receptor_scaffold_boundary
  evidence_ids:
  - plaque-current-1
  - plaque-go
  - plaque-protein-P14904
  - plaque-scott2001-retained-body
  - plaque-shintani2004-retained-body
  - plaque-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cvt_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: major
  normalization_reason: The asserted molecular identity, structural boundary or typed
    hierarchy is materially incorrect, rather than an optional enrichment.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052917Z-cvt-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2907
- finding_id: plaque-t2-F1
  issue_key: cytostome-plasma-membrane-parthood
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Prior cytostome plasma-membrane hierarchy error is corrected
  description: The old frozen target incorrectly used GO0005886 as an is-a parent.
    Current source instead uses GO0110165 parent and GO0005886 part_of with corresponding
    evidence/history; fresh exact GO children/path confirms both typed relations.
  target_ids:
  - GO:0031910
  field_paths:
  - parent_structures
  - part_of
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-cytostome-delta
  - plaque-go
  - plaque-cytostome-path
  - plaque-issue2461-context
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cytostome.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: major
  normalization_reason: The asserted molecular identity, structural boundary or typed
    hierarchy is materially incorrect, rather than an optional enrichment.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052918Z-cytostome-audit
    finding_id: F1
  disposition_reason: Resolved by the already-present current record correction associated
    with closed issue2461/PR2464, independently verified against current bytes and
    fresh GO. This successor records resolution of this one inherited target/finding
    only; it does not claim this PR performed the scientific edit or close all grouped
    historical findings.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2461
- finding_id: septin-cullin_e_ubiquitin_ligase_complex-F1
  issue_key: cullin-e-skp1-2-wrong-accession
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Replace the Skp1.2 example with the source-locus-matched protein
  description: The record explicitly identifies Skp1.2 as Tb927.9.8370 but gives UniProtKB:Q384S1,
    ORF Tb11.02.5340,212aa. Source Table1 and S3 specify Tb927.9.8370,158aa. Native
    Q38ED0 has historical ORF Tb09.211.0300 and the exact VEuPathDB Tb927.9.8370 cross-reference;
    independent Ensembl lookup also maps that locus to Q38ED0 and158aa. Correct Q383D5/Q38C61
    mappings are retained. Their historical ORF names should not be called primary
    gene names. Fresh current authority and genuine primary/terminology sources independently
    confirm the inherited issue. Dated rationale/history must be preserved; current
    scientific fields or appended clarification are the correction surface.
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  field_paths:
  - components#skp1_2.protein_examples
  - components#cullin_e.protein_examples
  - components#rbx1.protein_examples
  - discussions
  evidence_ids:
  - septin-record-cullin_e_ubiquitin_ligase_complex
  - septin-original-cullin_e_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC12816148-jats
  - septin-PMC5241021-jats
  - septin-cullin-s3
  - septin-pride
  - septin-up-Q384S1
  - septin-up-Q38ED0
  - septin-up-Q383D5
  - septin-up-Q38C61
  - septin-ensembl-skp12
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: major
  normalization_reason: The asserted molecular identity, structural boundary or typed
    hierarchy is materially incorrect, rather than an optional enrichment.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2905
- finding_id: septin-dinoflagellate_antapex-F1
  issue_key: dinoflagellate-antapex-anterior-posterior-definition
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Correct the antapex definition’s anterior/posterior reversal
  description: The record defines the antapex as the anterior-most point of the hypocone,
    faithfully copying current GO0097684. Yet the same record’s sulcal-notch edge
    and GO0097618 place the antapex at the posterior end. The directly linked Tree
    of Life orientation note defines the antapex at the bottom of the hyposome and
    below-cingulum positions as posterior; the specialist INA orientation glossary
    agrees. The definition therefore mislocates the defining region even though its
    GO identifier, label and parthood are correct. The upstream GO discrepancy must
    be retained explicitly rather than treated as an invented or misquoted source.
    Fresh current authority and genuine primary/terminology sources independently
    confirm the inherited issue. Dated rationale/history must be preserved; current
    scientific fields or appended clarification are the correction surface.
  target_ids:
  - GO:0097684
  field_paths:
  - definition
  - definition_source
  - evidence[0].notes
  evidence_ids:
  - septin-record-dinoflagellate_antapex
  - septin-original-dinoflagellate_antapex
  - septin-go
  - septin-tol-orientation
  - septin-tol-dino
  - septin-ina-orientation
  - septin-tax-2864
  - septin-go-0097684-history
  - septin-go-0097684-constraints
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_antapex.yaml
    role: maintained scientific record
  rule_id: Biologically accurate regional definition and source-specific provenance
  native_severity: major
  normalization_reason: The error reverses the defining location along the cell axis,
    rather than merely changing style. The GO identifier, label and posterior graph
    endpoint remain correct, so this is a bounded major definition defect rather than
    a blocker or a demand to replace the structure identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T052921Z-dinoflagellate-antapex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2906
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0042729
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dash_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, curate the seven verified
    exact family mappings and update current status/notes and the grounding portion
    of the TODO; retain the distinct open small-subunit boundary work.
  acceptance_checks:
  - Verify exact family type/name and matching example xref; do not substitute general
    domains.
  - Preserve source-specific taxa, supported component IDs and protein examples; pass
    applicable native curation checks.
  - Preserve discussions.rationale, posed_date and dated history; append provenance
    and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers, experimental host/condition and unknown formation scope explicit.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0042729
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dash_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add the exact Janke Dad2-ProA/spc34-3
    versus matched SPC34 recovery assessment at37°C for4h, distinguishing physical
    association/stability from viability, direct binding and biorientation. Qualify
    any formation interpretation; global UNKNOWN may remain. Do not infer intracellular
    depletion of unrecovered partners, force universal ESSENTIAL or demand new experiments.
  acceptance_checks:
  - Distinguish recovery/stability of the complete reported assembly from viability
    and direct binding.
  - Do not generalize the mutant result to all subunits or all organisms.
  - Preserve source-specific taxa, supported component IDs and protein examples; pass
    applicable native curation checks.
  - Preserve discussions.rationale, posed_date and dated history; append provenance
    and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers, experimental host/condition and unknown formation scope explicit.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0031431
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dbf4_dependent_protein_kinase_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, map the Dbf4 row to the verified
    exact family and narrow the remaining TODO to unresolved Cdc7 mapping; retain
    the correct examples and UNKNOWN formation necessity.
  acceptance_checks:
  - Verify native family type/name/signature and the P32325 xref.
  - Do not promote unchecked generated family prose to experimental mechanism evidence.
  - Preserve source-specific taxa, supported component IDs and protein examples; pass
    applicable native curation checks.
  - Preserve discussions.rationale, posed_date and dated history; append provenance
    and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers, experimental host/condition and unknown formation scope explicit.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:1990125
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/diaa_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, use IPR023070 for the existing
    DiaA class and update current status/notes/TODO; preserve four-copy stoichiometry,
    correct example and the separation from DnaA/oriC.
  acceptance_checks:
  - Confirm the exact family type/name and DiaA-specific signatures.
  - Do not substitute broad GmhA/DiaA or SIS mappings.
  - Preserve source-specific taxa, supported component IDs and protein examples; pass
    applicable native curation checks.
  - Preserve discussions.rationale, posed_date and dated history; append provenance
    and update current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep primary body/abstract/authority
    tiers, experimental host/condition and unknown formation scope explicit.
- action_id: plaque-t1-A1
  finding_ids:
  - plaque-t1-F1
  target_ids:
  - GO:0034270
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cvt_complex.yaml
    role: maintained scientific record
  description: Reconcile the current Ape1-core versus Atg19-containing Cvt-complex
    boundary in definition, components and descriptive graph, retaining Atg11 as separately
    scoped trafficking machinery and Ams1 as source-scoped additional cargo. Reopen
    or qualify the active blanket exclusion with appended evidence; preserve dated
    rationale, posed_date and curation history.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Preserve the short GO definition as accurately sourced context while stating the
    primary-source boundary explicitly.
  - Do not infer universal formation ESSENTIAL labels from PAS/transport phenotypes
    or force every pathway factor into the constituent list.
  - Use the guarded record writer and append history only in separately authorized
    curation; this PR changes reviews only.
- action_id: septin-cullin_e_ubiquitin_ligase_complex-A1
  finding_ids:
  - septin-cullin_e_ubiquitin_ligase_complex-F1
  target_ids:
  - cellstructuremech:cullin_e_ubiquitin_ligase_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cullin_e_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
  description: Replace the Skp1.2 example with verified Q38ED0 and its actual native
    identity/status/taxon fields, documenting the paper-locus versus historical-ORF
    bridge. Retain Q383D5/Q38C61 with verified locus bridges and precise ORF wording.
    Reconcile stale example-related discussion text without treating family names
    as exact paralog identity. Record curation remains outside this review-only PR.
    Preserve all dated rationale/history, correcting current fields/notes or appending
    clarification.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Use separately authorized guarded record curation and append-only record/repository
    history; preserve exact source scope and do not silently misquote current GO or
    generated protein names.
- action_id: septin-dinoflagellate_antapex-A1
  finding_ids:
  - septin-dinoflagellate_antapex-F1
  target_ids:
  - GO:0097684
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_antapex.yaml
    role: maintained scientific record
  description: Correct the definition to the posterior tip/end of the hypocone. Cite
    the directly read orientation authority for that correction and explicitly record
    that current GO0097684 still contains the contradictory anterior wording; retain
    the GO identifier, correct hypocone parthood and posterior sulcal-notch relation,
    and preserve historical provenance. Do not silently present the corrected wording
    as an exact current GO quotation. Record curation remains outside this review-only
    PR. Preserve all dated rationale/history, correcting current fields/notes or appending
    clarification.
  acceptance_checks:
  - Definition consistently identifies the posterior antapex, with the anterior apex
    kept separate.
  - Definition source and nearest evidence explain the correction and upstream discrepancy.
  - Native schema, strict, CURIE and graph checks pass as applicable.
  - Use separately authorized guarded record curation and append-only record/repository
    history; preserve exact source scope and do not silently misquote current GO or
    generated protein names.
limitations:
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Only DASH, DDK, Polδ
  and DiaA are scientifically judged here; other cohort targets and newly frozen reservosome
  context are not read/disposed by this slice. No neighboring/category/group historical
  issue is terminally resolved.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Cheeseman genuine
  JATS and Janke genuine publisher PDF are body-read only at declared sections/tables/text
  captions. No figure pixels, raw gels/EM, sequence alignment, supplementary experiments
  or complete mechanistic reanalysis; new DASH constituent edges are not atomic interaction
  claims.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Li2005 and Miranda2005
  current access is complete primary abstract only; Li current body routes failed,
  and the original older body reading remains historical. The small-subunit inventory
  remains an acknowledged bounded question; no unverified Hsk/Dad alias or compulsory
  optional component is invented.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Bell-Dutta2002 is
  a secondary-review abstract only; current DDK coarse definition/function also rests
  on exact GO/native authorities. Gerik/Burgers1998 and Johansson2001 are complete
  primary abstracts only. Historical403/TLS failures are retained with corrected kinds,
  not recertified body reads.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Keyamura current primary
  abstract was freshly fetched; retained publisher PDF web-reader text was independently
  reread only at explicit delivered line spans. Its exact original network fetch instant
  was not exposed/recorded, so evidence time is the current retained-text inspection
  and explicitly not freshHTTP200. Cached source version is older; Terminal routes
  returned403 and later reader retries502. No complete-body/pixel/coordinate claim.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Native protein identity/location
  annotations and linked abstracts do not certify all cited full primary studies.
  Pol31/Pol32 nuclear annotations are by similarity; no fabricated experimental localization
  joins. Generated InterPro descriptions are not primary biological evidence. Exact
  current singleton gene queries do not reconstruct old query uniqueness.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Broader Pol31/Pol3
  families and unverified Pol32 candidate assignment remain uncertainty; no new false-positive
  mapping issue or exhaustive family-absence assertion. Formation UNKNOWN alone is
  not a curation defect. Spc34 finding is restricted to the directly inspected conditional
  recovery assay.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Fresh catalogue lacks
  natural yeast hosts in complete returned20 rows. DiaA precise1k spans five strains;
  b3149 is present but not above threshold in any201 returned modules. This is not
  absence, dispensability, physical assembly, localization or causal regulation evidence,
  and not an exact Keyamura mutant-panel match. No positive module hit exists to summarize
  as evidence.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: Historical runner
  unavailable/exit1 is explicitly dated2026-11-03T00:49:00Z, not a fresh invocation.
  Eight current own native protein receipts are actual source-head commands. Root
  owns globalQC/final saved-head checks/CI/queue; no pending stage is certified here.'
- 'DASH, DDK, delta DNA polymerase and DiaA independent review: All records, original
  reviews, Git state and GitHub remain untouched. Four inherited minor findings propose
  later bounded record curation; stale/applicability/type bundle defects require linked
  immutable successor corrections only.'
- 'Cvt and cytostome independent review: Scott2001/Shintani2004 genuine retained bodies
  were independently reread with their actual2026-11-03T11:52:44.702094Z/11:52:44.427793Z
  retrieval timestamps; fresh Nov4 PMC/S3/BioC/EPMC routes were challenge/error/no-result
  and are not body evidence. Fresh Chasen2020 S3 JATS was read at the exact stated
  sections.'
- 'Cvt and cytostome independent review: Matile1971,Frey1978,Oda1996,Okuda1999,Porto-Carreiro2000
  and Alcantara2014 remain complete indexed-primary-abstract/metadata tiers. Alcantara
  publisher403 and Porto DOI bibliographic JSON do not certify full Methods or figure
  data. Detailed lipid-specific Porto assays, exact tomography images and all experimental
  strains beyond the declared body scopes are not certified.'
- 'Cvt and cytostome independent review: No maintained images or physical-property
  measurements in these two targets; no external figure pixels, movie/supplement content
  or raw-data reanalysis certified. Read text captions are not pixel inspection.'
- 'Cvt and cytostome independent review: Cvt natural yeast scope is distinct from
  S288C reference accession, SEY6210-derived experimental cultures and recombinant
  bacterial/rabbit assays. T.cruzi Y parasite scope is distinct from human host-cell
  culture. No foreign-host expression module proxy used.'
- 'Cvt and cytostome independent review: Current official catalogue lacks biological
  yeast/T.cruzi coverage; this is no claim that pathways or proteins are biologically
  absent. No fresh adapter-runner execution claimed; retained Nov3 00:49Z PermissionError
  remains historical.'
- 'Cvt and cytostome independent review: Two original pairs/29 historical input occurrences
  and all48 current source/worktree hashes verified. Cvt unchanged; cytostome hierarchy
  delta substantively refreshed. Root global QC/final saved-head/CI/queue are separately
  owned and not precertified.'
- 'Cvt and cytostome independent review: One inherited major Cvt boundary finding
  remains open; one inherited major cytostome hierarchy finding is resolved from preexisting
  curation. No new scientific finding or terminal resolution of other2461 records/category
  observations. Broad M18/domain mappings and optional molecular inventories are not
  forced.'
- 'Cullin-E and three dinoflagellate morphology records independent review: All four
  current targets unchanged from original frozen inputs; two inherited confirmed major
  findings remain open: wrong Skp1.2 accession and antapex direction reversal. Horn/apex
  retain qualified positive support; no new scientific finding or unrelated issue
  disposition.'
- 'Cullin-E and three dinoflagellate morphology records independent review: Cullin-E
  has3unreviewed examples and1nativeCOVERED scaffold node; other3 have0examples/0typedprotein
  nodes. Native verification does not establish biological membership of disputedSkp1.2,
  formation necessity or specimen identity.'
- 'Cullin-E and three dinoflagellate morphology records independent review: 2025 genuine
  JATS read at front/permissions,Table1,Sec4/5/6/9/10/12/13/15/17/18/19/21 andFig2/6/7/8captions.
  ActualFig2allpanels,Fig6A–D andFig7pixels inspected. S3Legend,completeCULEheaderA–AZ
  and rows2/3/4/5/7/9/10columnsA–Z inspected; no raw spectra,whole-workbook statistical
  reanalysis or physicaldimension measurement. Figures are external scratch sources,
  none maintained or redistributed.'
- 'Cullin-E and three dinoflagellate morphology records independent review: Hu2017
  current genuine JATS read at front,Resultssec004 with embeddedFig2/3captions,Methodssec011/015/016
  only; no currentHu figurepixels/supplements or universalCulE/PLK absence claim.
  Older sourceTbCUL4locus3.1290 differs fromCulE11.11430;2025Discussion conflict remains
  explicit.'
- 'Cullin-E and three dinoflagellate morphology records independent review: PCF Lister427
  isolation,2T1qPCR,Fig6bloodstream schematic and RNAi stage not uniformly restated
  are not collapsed. TREU927 reference proteins/database are not culturedstrain. PRIDE
  sixWTcontrols versus paper/S3 seven preserved; distinct endpoints and duplicateFig7locus
  remain scoped.'
- 'Cullin-E and three dinoflagellate morphology records independent review: UniProtQ38ED0
  Elongin-C andQ384S1 SKP1/POZ generated names are not independent mechanistic evidence.
  Exact VEuPathDB/Ensembl/source length and locus mapping support the identity correction.
  Current-locus gene query misses are bounded alias-index limitations, not protein
  absence. IPR051031 unchecked LLM functional prose excluded.'
- 'Cullin-E and three dinoflagellate morphology records independent review: Dinoflagellate
  support is GO/ENA and authored expert terminology, not new primary formation experiments.
  GO0097684 still retains anterior error; correct posterior wording must be independently
  cited, not represented as exact currentGOquotation. Only_in_taxon and VARIABLE do
  not establish prevalence. No generic whole-cell materials reassigned to regional
  points.'
- 'Cullin-E and three dinoflagellate morphology records independent review: Taylor1980
  current access is complete native abstract/metadata only; fresh publisher403 is
  validation context. Two original publisher403 rows were typed database but explicitly
  context_only/failed; correction is kind-only. OriginalOctoberaccess dates remain
  historical. NoTaylorbody or dinoflagellate image pixels inspected.'
- 'Cullin-E and three dinoflagellate morphology records independent review: One own
  historical expression-only adapter exclusion needs correction; three morphology
  exclusions are genuinely applicable. Fresh official complete catalogue contains
  no matchingTrypanosoma orDinophyceae dataset. No unrelated-host downstream proxy
  or biologicalabsence inference; runner unavailable receipt remains Nov3 00:49Z with
  no fresh invocation.'
- 'Cullin-E and three dinoflagellate morphology records independent review: All59
  original input occurrences and4original deterministic pairs verified. Valid historical
  batch26 gate execution reused across originalbatch49 remains explicit. Scratch parser
  dependency error was corrected without changing repo; parent global/postsave/finalCI/queue/merge/deletion
  are separate attestations.'
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
- 'This explicit ten-record successor preserves all original review observations and
  exact predecessor findings. Scientific record curation stays outside this PR. Bundle
  issues #2902, #2903 and #2904 cover the stale inputs, seven formal applicability
  exclusions and five failed-access kind occurrences, respectively.'
- 'Two target hashes changed: cytostome hierarchy/parthood/evidence/history and seven
  DASH constituent nodes/edges. Cytostome F1 is resolved from existing record bytes
  and linked to already-closed #2461; this PR neither performed that record correction
  nor resolves the other records in the grouped issue. DASH current graph membership
  is distinguished from exact family grounding and condition-specific association
  evidence.'
- The complete native protein inventory is 17 represented examples and 15 typed GENE_OR_PROTEIN
  nodes, all classified COVERED by the actual native commands. An accession/coverage
  pass does not establish a disputed source-locus assignment or formation necessity.
  Empty inventories in morphology records are not automatic defects.
- Fresh, retained and unavailable source observations keep their actual access dates
  and inspection scopes. Failed responses are validation/context_only; the five old
  rows already disclosed their failure and are not alleged to have falsely claimed
  article-body access. Current citations distinguish indexed abstracts, actually inspected
  genuine bodies, expert authorities, figure text and actual external pixels.
- Preserve the current GO antapex wording as an explicitly documented upstream discrepancy
  while requesting a separately sourced posterior correction. For Cvt, distinguish
  Ape1 cargo self-assembly, Atg19-containing complex and Atg11 delivery machinery,
  preserving dated rationale with appended clarification. DASH Spc34 evidence is restricted
  to spc34-3, 37 C for four hours, Dad2-ProA recovery and its matched control; global
  UNKNOWN may remain, with no universal ESSENTIAL, partner-depletion or new-assay
  requirement.
- 'Full local QC, all 20 focused schema/strict checks and all 20 native protein checks
  passed before saving. Final trusted-base post-save review-check, saved-head independent
  acceptance, final-head CI and merge-group CI remain subsequent gates. Existing #2514
  retains the native bulk-PMID reporting limitation; bounded supplemental native requests
  verified all 909 affected PMIDs without changing the original report or cache.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052917Z-cullin-e-ubiquitin-ligase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052917Z-cvt-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052918Z-cytostome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052919Z-dash-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052919Z-dbf4-dependent-protein-kinase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052920Z-delta-dna-polymerase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052921Z-diaa-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052921Z-dinoflagellate-antapex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052922Z-dinoflagellate-antapical-horn-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T052923Z-dinoflagellate-apex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2386
- https://github.com/CultureBotAI/CellStructureMech/issues/2461
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2902
- https://github.com/CultureBotAI/CellStructureMech/issues/2903
- https://github.com/CultureBotAI/CellStructureMech/issues/2904
- https://github.com/CultureBotAI/CellStructureMech/issues/2905
- https://github.com/CultureBotAI/CellStructureMech/issues/2906
- https://github.com/CultureBotAI/CellStructureMech/issues/2907
- https://github.com/CultureBotAI/CellStructureMech/issues/2908
- https://github.com/CultureBotAI/CellStructureMech/issues/2909
- https://github.com/CultureBotAI/CellStructureMech/issues/2910
- https://github.com/CultureBotAI/CellStructureMech/issues/2911
```
