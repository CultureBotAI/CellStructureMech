# PR 2390: current-input review of ten records and adversarial follow-up

- Review: 20261104T081641Z-pr2390-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T07:55:05.450748Z
- Finished UTC: 2026-11-04T08:16:41Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

All ten records reassessed against current main; two stale reviews (eisosome and EmrAB-TolC) substantively refreshed. Ten inherited scientific findings are retained with current source scope, and one new minor EmrAB-TolC CPX attribution finding is filed separately. Seven formal and three prose structured-source applicability exclusions and six access-only evidence kinds are corrected in this linked successor. No scientific record or original review artifact is changed.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 9ec44ab9323f1ebe881d7de8f25276ac75e78b88.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 6d564c8d647868414ddf025c64068d9ac990abc8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070939 | data/structures/other/dsl1_nzr_complex.yaml | maintained | Dsl1/NZR complex |
| GO:0071819 | data/structures/other/dubm_complex.yaml | maintained | DUBm complex |
| GO:1990065 | data/structures/other/dxr_protein_complex.yaml | maintained | Dxr protein complex |
| GO:0032126 | data/structures/other/eisosome.yaml | maintained | eisosome |
| cellstructuremech:ejectisome | data/structures/other/ejectisome.yaml | maintained | ejectisome |
| GO:0031391 | data/structures/other/elg1_rfc_like_complex.yaml | maintained | Elg1 RFC-like complex |
| GO:0033588 | data/structures/other/elongator_holoenzyme_complex.yaml | maintained | elongator holoenzyme complex |
| GO:0072546 | data/structures/other/emc_complex.yaml | maintained | EMC complex |
| cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml | maintained | EmrAB-TolC multidrug efflux transport complex |
| GO:1990207 | data/structures/other/emre_multidrug_transporter_complex.yaml | maintained | EmrE multidrug transporter complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0070939 | passed | True | GO:0070939 | Documented focused command passed. |
| validate-strict GO:0070939 | passed | True | GO:0070939 | Documented focused command passed. |
| validate GO:0071819 | passed | True | GO:0071819 | Documented focused command passed. |
| validate-strict GO:0071819 | passed | True | GO:0071819 | Documented focused command passed. |
| validate GO:1990065 | passed | True | GO:1990065 | Documented focused command passed. |
| validate-strict GO:1990065 | passed | True | GO:1990065 | Documented focused command passed. |
| validate GO:0032126 | passed | True | GO:0032126 | Documented focused command passed. |
| validate-strict GO:0032126 | passed | True | GO:0032126 | Documented focused command passed. |
| validate cellstructuremech:ejectisome | passed | True | cellstructuremech:ejectisome | Documented focused command passed. |
| validate-strict cellstructuremech:ejectisome | passed | True | cellstructuremech:ejectisome | Documented focused command passed. |
| validate GO:0031391 | passed | True | GO:0031391 | Documented focused command passed. |
| validate-strict GO:0031391 | passed | True | GO:0031391 | Documented focused command passed. |
| validate GO:0033588 | passed | True | GO:0033588 | Documented focused command passed. |
| validate-strict GO:0033588 | passed | True | GO:0033588 | Documented focused command passed. |
| validate GO:0072546 | passed | True | GO:0072546 | Documented focused command passed. |
| validate-strict GO:0072546 | passed | True | GO:0072546 | Documented focused command passed. |
| validate cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | passed | True | cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | Documented focused command passed. |
| validate-strict cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | passed | True | cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | Documented focused command passed. |
| validate GO:1990207 | passed | True | GO:1990207 | Documented focused command passed. |
| validate-strict GO:1990207 | passed | True | GO:1990207 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | All ten records have positive molecular triggers. Fresh complete official catalogue coverage is assessed against actual natural/reference hosts. Yeast and cryptophycean hosts are not covered; unrelated hosts are not proxies. Matched E. coli precise1k metadata and bounded gene/module endpoints provide Dxr UC-2/167, TolC SoxS/22 and EmrE ROS TALE Amp/9 context. EmrA/EmrB nonhits are not absence evidence. Five advertised strains do not cover every engineered expression host, and module membership does not establish complex assembly, direct regulation or essentiality. Historical runner unavailability is retained separately from current direct-source fallback. |
| Independent claim-level source review | passed | True | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native Dsl1/NZR complex UniProt verify check | passed | True | GO:0070939 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Dsl1/NZR complex UniProt causal check | passed | True | GO:0070939 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DUBm complex UniProt verify check | passed | True | GO:0071819 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DUBm complex UniProt causal check | passed | True | GO:0071819 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Dxr protein complex UniProt verify check | passed | True | GO:1990065 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Dxr protein complex UniProt causal check | passed | True | GO:1990065 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native eisosome UniProt verify check | passed | True | GO:0032126 | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native eisosome UniProt causal check | passed | True | GO:0032126 | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ejectisome UniProt verify check | passed | True | cellstructuremech:ejectisome | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ejectisome UniProt causal check | passed | True | cellstructuremech:ejectisome | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Elg1 RFC-like complex UniProt verify check | passed | True | GO:0031391 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Elg1 RFC-like complex UniProt causal check | passed | True | GO:0031391 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native elongator holoenzyme complex UniProt verify check | passed | True | GO:0033588 | 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native elongator holoenzyme complex UniProt causal check | passed | True | GO:0033588 | 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EMC complex UniProt verify check | passed | True | GO:0072546 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EMC complex UniProt causal check | passed | True | GO:0072546 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EmrAB-TolC multidrug efflux transport complex UniProt verify check | passed | True | cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EmrAB-TolC multidrug efflux transport complex UniProt causal check | passed | True | cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EmrE multidrug transporter complex UniProt verify check | passed | True | GO:1990207 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EmrE multidrug transporter complex UniProt causal check | passed | True | GO:1990207 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact tether identity and boundary

identity: supported. Targets: GO:0070939.

GO0070939 exactly denotes the ternary Dsl1/NZR tether. GO0099023 is is-a and GO0005783 is ER parthood/localization; COPI and ER SNARE interactions do not make every binding partner a constituent.

### Current primary composition and transport evidence

evidence: supported. Targets: GO:0070939.

Fresh Tripathi body supports recombinant ternary composition, contacts and transport-tether interpretation. Fresh Meiringer/Kraynack complete abstracts support the stated core/SNARE context; their current full bodies were not obtained. Historical body readings are not newly certified.

### Tip20 exact family versus domain alternatives

grounding: concern. Targets: GO:0070939.

Tip20 IPR007528 is the exact RINT1/Tip20 family and P33891 has that xref. The current three-constituent task can be narrowed for Tip20 after curation. Inspected Dsl1 N/C and Sec39 identifiers are domains, not exact whole-protein replacements; no exhaustive absence claim.

### Purified Dsl1 bridging evidence

evidence: concern. Targets: GO:0070939.

Tripathi S6/Figure4 directly compares pairwise binding and ternary reconstitution: Dsl1 links Tip20 and Sec39. Current component evidence lacks that bounded association/formation observation. A global UNKNOWN essentiality value may remain; domain-mutant growth and universal in-vivo absence are different questions.

### Coarse NONMECHANISTIC FUNCTION graph

graph: supported. Targets: GO:0070939.

Three constituent-to-complex contributions, ER localization and retrograde-transport function are proportionate to the graph scope. It does not claim a solved fusion mechanism or make transient coat/SNARE partners members.

### Example localization and historical names

evidence: supported. Targets: GO:0070939.

Current native DSL1/TIP20/SEC39 primary names and TIP1/DSL3 aliases support intended examples. Fresh complete abstracts for PMID11493604/11739780 support peripheral ER and retrograde context; PMID8334998 supplies historical Tip1/Sec20 association. No unread strain-level full methods are certified.

### Four-protein DUB module and SAGA/SLIK boundaries

identity: supported. Targets: GO:0071819.

GO0071819 is the four-constituent DUB module within SAGA and SLIK. Parent nuclear-complex and two parthood relations are consistent; the entire19-subunit SAGA structure is not the record identity.

### Primary structural and biochemical scope

evidence: supported. Targets: GO:0071819.

Wang supports Ubp8/Sgf11/Sus1/N-terminal Sgf73 and Sgf73 tether to the larger core. Adamus directly identifies SLIK/SAGA components and compares DUB activity, with Ub-AMC and low-resolution EM limits. Reference S288C examples are not substituted for every experimental strain.

### Three exact constituent families

grounding: concern. Targets: GO:0071819.

Current complete family entries IPR013246, IPR018783 and IPR037804 independently match Sgf11, Sus1 and Sgf73 native xrefs. These resolve three existing class-grounding tasks; Ubp8 catalytic USP domain and broad hydrolase family do not resolve its exact class. LLM-flagged broad-family prose is not biological evidence.

### UNKNOWN requirement and partial association data

evidence: unknown. Targets: GO:0071819.

Kohler complete abstract concerns Sus1 association with SAGA and a high-salt three-protein subcomplex; it does not directly establish every four-member module formation requirement. No universal essentiality or new experiment is imposed.

### Native example locations versus whole module

evidence: supported. Targets: GO:0071819.

Native annotations and complete indexed abstracts retain nuclear/cytoplasmic contexts. Sus1 overexpression/P-body localization and Sgf73 hypoxia-source annotation are example-level evidence, not independent proof that the whole DUB module occupies every such site. Huh and Dastidar abstracts do not expose all individual supplement rows.

### Coarse membership and deubiquitination graph

graph: supported. Targets: GO:0071819.

Four membership edges, SAGA/SLIK parthood and deubiquitinase function are supported at declared NONMECHANISTIC FUNCTION scope; no complete catalytic sequence, universal substrate specificity or fixed activity equivalence is asserted.

### Exact Dxr complex and homodimer scope

identity: supported. Targets: GO:1990065.

GO1990065 denotes the Dxr enzyme complex; IPR003821 exactly grounds its constituent family. Author biological assembly1Q0Q has two protein copies, not one record per monomer.

### Substrate/cofactor deposition and abstract limits

evidence: supported. Targets: GO:1990065.

PDB1Q0Q independently contains DXP and NADPH despite the associated paper title emphasizing fosmidomycin. Primary complete abstract distinguishes substrate and inhibitor structures and a possible minor substrate stereoisomer. No full article body or coordinates were reanalyzed.

### Reference protein versus experimental host

scope: supported. Targets: GO:1990065.

P45568 is reviewed E.coli K12 dxr/ispC b0173. Deposited source species562 and recombinant BL21(DE3) host are distinct from tax83333 reference annotation; current species-level canonical example does not falsely assert a living K12 experiment.

### NADPH reaction and coarse dimer function

graph: supported. Targets: GO:1990065.

Explicit maintained functional wording uses NADPH reduction of DXP to MEP; native GO0030604 writes the reversible redox reaction in the opposite direction. Graph describes dimer assembly/function without asserting every chemical intermediate or universal formation necessity.

### Formation and missing physical measurements

evidence: unknown. Targets: GO:1990065.

UNKNOWN component formation requirement is preserved; a dimer deposition does not establish a universal deletion phenotype. No optional imaging, molecular mass or additional instance is required.

### Whole eisosome versus filament and MCC

identity: supported. Targets: GO:0032126.

GO0032126 includes the membrane/MCC domain and cytoplasmic scaffolding filaments. The two maintained neighbors and GO0036286/GO0090512 are genuine child boundaries, not alternate identities for the whole.

### Substantive current stale-field reassessment

scope: supported. Targets: GO:0032126.

Current PROTEIN_COMPLEX core plus IPR028245 graph grounding is supported by native Pil1/Lsp1 family identity and primary assembled scaffold/copurification observations. GENE_OR_PROTEIN permits complexes. The record does not require an obligate Pil1-Lsp1 heterodimer; Karotki explicitly leaves heterodimer versus mixed homodimer architecture unresolved.

### Discovery, scaffold and membrane-domain evidence

evidence: supported. Targets: GO:0032126.

Walther supports immobile assemblies and colocalization; Karotki and Olivera supply later self-assembly/membrane-binding/mutant evidence. Current organization wording does not assert an exhaustive endocytosis mechanism. Douglas is secondary abstract context, not a fresh publisher body.

### Yeast experiments and fungal variability

scope: supported. Targets: GO:0032126.

Native examples are reviewed S288C; primary experiments include W303/S288C and recombinant expression/COS7 tests. Fungi VARIABLE is not a prevalence census or a claim that every fungus has the same assembly.

### Core family and Sur7 task

grounding: supported. Targets: GO:0032126.

IPR028245 maps the Pil1/Lsp1 constituent class. IPR009571 is broad SUR7/Rim9-like context and does not automatically settle an exact Sur7 family task. Preserved source-neutral task and historical rationale are not defects merely because taxon-specific examples exist.

### Scaffold assembly and localization edges

graph: supported. Targets: GO:0032126.

Primary assembly and membrane-interaction experiments support core-to-filament, core-to-MCC scaffold and Sur7 localization edges at current granularity. They do not specify an obligatory native heterodimer, every nucleation partner or a full signaling mechanism.

### Current example-level localization context

evidence: supported. Targets: GO:0032126.

PIL1 native lipid-droplet annotation is retained as cited native localization context; it does not override independent direct eisosome microscopy. Sur7 membrane and Lsp1/core locations have separate primary/authority scope. Moreira abstract supports regulated bud assembly, not all molecular details.

### Honest historical failure with incorrect evidence kind

schema: concern. Targets: GO:0032126.

Original micro53-douglas2014-publisher explicitly says HTTP403/no body, but kind authority is inappropriate for an access diagnostic. Successor validation/context_only preserves its actual historical time/hash. This is not an allegation of fabricated full-text access.

### Current example identity and bounded queries

grounding: supported. Targets: GO:0070939.

3 maintained reviewed examples match native primary genes/aliases, loci and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness reconstruction. Example annotations do not substitute for source-neutral class grounding or entire primary methods.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0070939.

Original formal expression-only exclusion overlooks positive named proteins/pathways. Fresh complete catalogue contains no matching yeast dataset; no foreign organism proxy or downstream query is invented. Historical runner unavailability is separately dated; direct source fallback is actual current work.

### Historical discussion and finding lineage

scope: supported. Targets: GO:0070939.

Two exact original minor findings persist, with the Dsl1 bridge action explicitly condition-scoped and global UNKNOWN permitted. Preserve rationale/posed_date and all immutable original artifacts; no record edits occur here.

### Actual native schema/render and protein coverage

schema: supported. Targets: GO:0070939.

3 reviewed examples and 3 COVERED typed protein nodes. Both source-head native commands exit0; original native validate/render and hashes pass. Success is not scientific completeness or a future successor/CI certificate.

### Imaging, measurements and unsupported optional completion

scope: not_applicable. Targets: GO:0070939.

No maintained image or quantitative physical-property assertion requires a pixel/measurement audit. Paper text captions and structural deposit metadata are used only at the stated scope. No missing optional physical field is manufactured as a finding.

### Current example identity and bounded queries

grounding: supported. Targets: GO:0071819.

4 maintained reviewed examples match native primary genes/aliases, loci and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness reconstruction. Example annotations do not substitute for source-neutral class grounding or entire primary methods.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0071819.

Original formal expression-only exclusion overlooks positive named proteins/pathways. Fresh complete catalogue contains no matching yeast dataset; no foreign organism proxy or downstream query is invented. Historical runner unavailability is separately dated; direct source fallback is actual current work.

### Historical discussion and finding lineage

scope: supported. Targets: GO:0071819.

One exact original minor family-grounding finding persists; broader Ubp8 task and historical rationale remain open. Preserve rationale/posed_date and all immutable original artifacts; no record edits occur here.

### Actual native schema/render and protein coverage

schema: supported. Targets: GO:0071819.

4 reviewed examples and 4 COVERED typed protein nodes. Both source-head native commands exit0; original native validate/render and hashes pass. Success is not scientific completeness or a future successor/CI certificate.

### Imaging, measurements and unsupported optional completion

scope: not_applicable. Targets: GO:0071819.

No maintained image or quantitative physical-property assertion requires a pixel/measurement audit. Paper text captions and structural deposit metadata are used only at the stated scope. No missing optional physical field is manufactured as a finding.

### Current example identity and bounded queries

grounding: supported. Targets: GO:1990065.

1 maintained reviewed examples match native primary genes/aliases, loci and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness reconstruction. Example annotations do not substitute for source-neutral class grounding or entire primary methods.

### Whole-record structured-source applicability

scope: concern. Targets: GO:1990065.

Original formal expression-only exclusion overlooks positive named proteins/pathways. Fresh five-strain E.coli precise1k context selects b0173 dxr/P45568; one UC-2 hit among201, Unknown function, verified in96-member list. Expression context does not establish physical dimerization or necessity. Historical runner unavailability is separately dated; direct source fallback is actual current work.

### Historical discussion and finding lineage

scope: supported. Targets: GO:1990065.

Original qualified-pass outcome remains supported within present access limits; no new scientific finding. Preserve rationale/posed_date and all immutable original artifacts; no record edits occur here.

### Actual native schema/render and protein coverage

schema: supported. Targets: GO:1990065.

1 reviewed examples and 1 COVERED typed protein nodes. Both source-head native commands exit0; original native validate/render and hashes pass. Success is not scientific completeness or a future successor/CI certificate.

### Imaging, measurements and unsupported optional completion

scope: not_applicable. Targets: GO:1990065.

No maintained image or quantitative physical-property assertion requires a pixel/measurement audit. Paper text captions and structural deposit metadata are used only at the stated scope. No missing optional physical field is manufactured as a finding.

### Current example identity and bounded queries

grounding: supported. Targets: GO:0032126.

3 maintained reviewed examples match native primary genes/aliases, loci and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness reconstruction. Example annotations do not substitute for source-neutral class grounding or entire primary methods.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0032126.

Original unsupported prose exclusion overlooks positive named proteins/pathways. Fresh complete catalogue contains no matching yeast dataset; no foreign organism proxy or downstream query is invented. Historical runner unavailability is separately dated; direct source fallback is actual current work.

### Historical discussion and finding lineage

scope: supported. Targets: GO:0032126.

Stale changes are substantively accepted within explicit native architecture limits; historical issue mentions are provenance only, not broad group closure. Preserve rationale/posed_date and all immutable original artifacts; no record edits occur here.

### Actual native schema/render and protein coverage

schema: supported. Targets: GO:0032126.

3 reviewed examples and 2 COVERED typed protein nodes. Both source-head native commands exit0; original native validate/render and hashes pass. Success is not scientific completeness or a future successor/CI certificate.

### Imaging, measurements and unsupported optional completion

scope: not_applicable. Targets: GO:0032126.

No maintained image or quantitative physical-property assertion requires a pixel/measurement audit. Paper text captions and structural deposit metadata are used only at the stated scope. No missing optional physical field is manufactured as a finding.

### identity-hierarchy

identity: supported. Targets: cellstructuremech:ejectisome.

The minted ejectisome identity and broad membrane-bounded parent are consistent with the described cryptophyte organelle. A bounded zero-result GO name search is not exhaustive absence proof.

### composition-and-grounding

grounding: supported. Targets: cellstructuremech:ejectisome.

Ejectisin is a measured small-polypeptide constituent class; the bounded native query did not establish an exact full-class CURIE. Preserve REVIEWED_LABEL_ONLY and its TODO rather than guess an accession or demand an optional example.

### native-protein-identity

grounding: supported. Targets: cellstructuremech:ejectisome.

Zero protein_examples; one GENE_OR_PROTEIN ejectisin node is NO_GENE_SYMBOLS. This honest diagnostic is not an optional-example defect. Native exact gene/locus identities are correct, but a generic verification pass does not independently establish source-stage support.

### primary-source-scope

evidence: supported. Targets: cellstructuremech:ejectisome.

Rhiel is assessed at complete abstract/metadata tier. Ammermann additionally has bounded author-text Methods/Results inspection of purified discharged fragments and reconstituted filaments; older resting-organelle statements in its Introduction are secondary context. No image-pixel claim is made.

### taxon-and-experimental-context

scope: supported. Targets: cellstructuremech:ejectisome.

Cryptophyceae and Chroomonas IDs have class/genus ranks. Chroomonas LT and Cryptomonas S2/LT experimental labels are not a verified species/strain CURIE; Guillardia sequence correspondence does not define every cryptophyte ejectisome.

### quantity-and-architecture

quantity: supported. Targets: cellstructuremech:ejectisome.

The approximately6kDa ejectisin statement is bounded to biochemical preparations; no molecular copy count or intact-organelle assembly is inferred from the isolated filament experiment.

### formation-versus-function

evidence: unknown. Targets: cellstructuremech:ejectisome.

Ejectisin purification/reaggregation supports a filament material role, not necessity for formation of the complete intact organelle. UNKNOWN is retained without an invented mandatory experiment.

### causal-graph-and-localisation

graph: supported. Targets: cellstructuremech:ejectisome.

The NON_MECHANISTIC graph links a protein constituent class and discharge-associated structure without a detailed molecular mechanism. Native NO_GENE_SYMBOLS is a scoped diagnostic, not an unsupported optional-field finding.

### structured-source-applicability

evidence: supported. Targets: cellstructuremech:ejectisome.

Positive ejectisin protein/sequence and typed constituent assertions trigger the broad native structured-source policy. The complete fresh catalogue has no matching natural host; no downstream dataset is invented and no recombinant E.coli proxy is substituted. The old expression-only notes[1] exclusion is unsupported, even though the present bounded no-coverage outcome is legitimate. Historical runner unavailability remains historical; no fresh runner invocation is claimed.

### history-and-source-classification

provenance: concern. Targets: cellstructuremech:ejectisome.

All three target hashes remain unchanged; no historical record correction or terminal predecessor disposition is inferred. Two historical HTTP200 Client Challenge observations are honestly context_only but incorrectly typed authority; correct only the successor kind, retaining actual old URL/time/hash. Current successful routes are separate evidence.

### schema-provenance-and-verdict

schema: supported. Targets: cellstructuremech:ejectisome.

Original YAML validates and exactly renders its immutable Markdown;41 historical occurrences and49 current frozen inputs match. Qualified pass retained, with source-access and mapping limits; no scientific finding is manufactured. This is not certification of future CI, queue or merge.

### identity-hierarchy

identity: supported. Targets: GO:0031391.

GO0031391 identifies the Elg1/RFC2–5 alternative complex, not canonical RFC or the Ctf18/Rad24 alternatives.

### composition-and-grounding

grounding: supported. Targets: GO:0031391.

Five intended protein classes and individual examples agree. New Elg1 domain entries and broad small-RFC families are not exact full-protein mappings; this review does not fabricate an exact-grounding correction.

### native-protein-identity

grounding: supported. Targets: GO:0031391.

Five reviewed protein_examples; five typed protein nodes are COVERED. Native exact gene/locus identities are correct, but a generic verification pass does not independently establish source-stage support.

### primary-source-scope

evidence: supported. Targets: GO:0031391.

Kubota primary abstract directly supports PCNA unloading/degron-restoration and purified-complex function; full body access remains blocked. Kim/MacNeill and Kupiec are secondary abstracts, not primary experiments. No unread assay detail is supplied.

### taxon-and-experimental-context

scope: supported. Targets: GO:0031391.

S. cerevisiae species4932 and S288C reference559292 are distinguished. Exact reference accessions do not silently identify experimental strain backgrounds. The accessed Kubota abstract does not establish a precise experimental strain.

### quantity-and-architecture

quantity: supported. Targets: GO:0031391.

The five distinct subunits support the stated pentameric Elg1-RFC class; no unsupported universal kinetics or absolute unloading mechanism is added.

### formation-versus-function

evidence: unknown. Targets: GO:0031391.

PCNA unloading and genome-stability outcomes are functional evidence. The accessed abstract does not establish individual-subunit requirements for formation; UNKNOWN rows are not automatically defects.

### causal-graph-and-localisation

graph: supported. Targets: GO:0031391.

The NON_MECHANISTIC graph keeps membership and PCNA unloading separate; reviewed examples anchor five typed nodes. Identity and function are supported within native authority/abstract limits.

### structured-source-applicability

evidence: supported. Targets: GO:0031391.

Positive named protein components and PCNA-unloading pathway claims trigger the broad native structured-source policy. The complete fresh catalogue has no matching natural host; no downstream dataset is invented and no recombinant E.coli proxy is substituted. The old expression-only notes[1] exclusion is unsupported, even though the present bounded no-coverage outcome is legitimate. Historical runner unavailability remains historical; no fresh runner invocation is claimed.

### history-and-source-classification

provenance: concern. Targets: GO:0031391.

All three target hashes remain unchanged; no historical record correction or terminal predecessor disposition is inferred. Three historical TLS/browser403/publisher403 observations are honestly context_only but incorrectly typed authority; correct only the successor kind, retaining actual old URL/time/hash. Current successful routes are separate evidence.

### schema-provenance-and-verdict

schema: supported. Targets: GO:0031391.

Original YAML validates and exactly renders its immutable Markdown;41 historical occurrences and49 current frozen inputs match. Qualified pass retained, with source-access and mapping limits; no scientific finding is manufactured. This is not certification of future CI, queue or merge.

### identity-hierarchy

identity: concern. Targets: GO:0033588.

GO0033588 is the correct complex identifier and is quoted faithfully; its old heterohexamer/two-trimer architecture conflicts with newer measured assembly stoichiometry. Keep identity while distinguishing six protein species from copy number.

### composition-and-grounding

grounding: concern. Targets: GO:0033588.

All six exact full-protein family mappings are independently confirmed by native family types and correct example memberships: Elp1 IPR006849, Elp2 IPR037289, Elp3 IPR034687, Elp4 IPR008728, Elp5 IPR019519, Elp6 IPR018627. Broader domains and IPR039661 are not substitutes.

### native-protein-identity

grounding: supported. Targets: GO:0033588.

Six reviewed protein_examples; six typed protein nodes are COVERED. Correct references are S288C; ELP1/ELP5 are aliases of native primary names IKI3/IKI1, not mismatches. Exact-organism searches establish bounded identity only.

### primary-source-scope

evidence: supported. Targets: GO:0033588.

Krogan2001 six-species inventory and Huang2005 tRNA modification evidence are distinguished from later Setiaputra/Dauden physical architecture. Full selected primary Methods/Results and text captions were read; no figure-pixel or raw-data reanalysis.

### taxon-and-experimental-context

scope: supported. Targets: GO:0033588.

S. cerevisiae species4932 and S288C reference559292 are distinguished. Exact reference accessions do not silently identify experimental strain backgrounds. Krogan uses W303-derived strains; Dauden BS1173/BSY2369; Setiaputra supplementary strain table was not inspected. E.coli recombinant expression is not natural taxon evidence.

### quantity-and-architecture

quantity: concern. Targets: GO:0033588.

Two Elp123 units plus a majority one Elp456 heterohexamer support the characterized12-subunit assembly, while lower salt and added recombinant ring conditions allow two Elp456 rings. Six distinct proteins is not an invariant six-copy holoenzyme, and replacement wording must preserve variable ring occupancy.

### formation-versus-function

evidence: concern. Targets: GO:0033588.

FLAG-Elp4 purification after elp1 deletion loses Elp2/3 association while Elp456 persists. Record this measured condition-specific assembly association, separate from Huang catalytic-output loss and viability. A global UNKNOWN may remain if its enum cannot express the tested scope; no universal six-subunit necessity is required.

### causal-graph-and-localisation

graph: concern. Targets: GO:0033588.

Six covered typed nodes preserve component identities and broad tRNA-wobble function. Graph description must distinguish identities from physical copy number. Historical transcription/localisation citations are not all formation evidence; Huh individual images were not viewed.

### structured-source-applicability

evidence: supported. Targets: GO:0033588.

Positive protein components and tRNA-modification pathway claims trigger the broad native structured-source policy. The complete fresh catalogue has no matching natural host; no downstream dataset is invented and no recombinant E.coli proxy is substituted. The old expression-only formal check is unsupported, even though the present bounded no-coverage outcome is legitimate. Historical runner unavailability remains historical; no fresh runner invocation is claimed.

### history-and-source-classification

provenance: concern. Targets: GO:0033588.

All three target hashes remain unchanged; no historical record correction or terminal predecessor disposition is inferred. No additional historical failed-access kind defect was found in this assigned original. Preserve the dated rationale and append current architecture/family evidence; do not rewrite the historical why.

### schema-provenance-and-verdict

schema: concern. Targets: GO:0033588.

Original YAML validates and exactly renders its immutable Markdown;41 historical occurrences and49 current frozen inputs match. Needs_curation retained for the three reconfirmed inherited findings, one major architecture and two minor bounded mapping/association corrections. Record curation remains outside this PR. This is not certification of future CI, queue or merge.

### Exact complex identity and anatomical boundary

identity: supported. Targets: GO:0072546.

Exact EMC GO identity retained; eight-member yeast source differs from the older six-name definition and mammalian source complexes.

### Parents,parthood and synonyms

identity: supported. Targets: GO:0072546.

Membrane-protein parent and ER membrane parthood preserve distinct is-a/part-of relations; BROAD synonyms remain explicitly qualified.

### Inventory and exact molecular scope

completeness: concern. Targets: GO:0072546.

Deferral of all eight source-established yeast constituents is actionable; unresolved exact families or individual necessity do not require suppressing supported label-only membership. This is an explicit deferral,not a universal optional-field mandate.

### Accession,primary name,alias and native inventory

grounding: concern. Targets: GO:0072546.

EMC has no native examples/nodes. Independent reviewed reference identities are EMC3/AIM27/P36039/YKL207W and EMC5/KRE27/P40540/YIL027C; dated rationale reverses aliases. Append correction without rewriting history.

### Primary experiments and access scope

evidence: supported. Targets: GO:0072546.

Bai yeast native purification/mass spectrometry/structure, Guna selected TA reconstitution and Chitwood selected first-TMD insertion support bounded record claims. Human O'Donnell pathway remains a proposed structural model,not a complete measured cycle.

### Stoichiometry and measured scope

grounding: supported. Targets: GO:0072546.

Eight yeast subunits established in Bai preparation; no single fixed mammalian count is imposed.

### Formation necessity versus membership and activity

grounding: unknown. Targets: GO:0072546.

Transport/insertion,growth and structural membership do not automatically establish a universal formation requirement. Bai Emc3K26L complex stays intact despite function defects; prospective constituent rows may retain UNKNOWN.

### Whole causal graph and substantive stale refresh

graph: supported. Targets: GO:0072546.

NONMECHANISTIC/FUNCTION insertion/Sec61 graph is appropriately coarse; selected substrates and sequence of tested TMDs constrain interpretation.

### Biological and experimental host scope

scope: supported. Targets: GO:0072546.

Yeast4932 canonical source is W303-1a in Bai; reference aliases are S288c559292. Human/HEK/U2OS functional papers are comparative,not yeast experiments. Qualitative COMMON/VARIABLE labels are not prevalence surveys.

### Citation and evidence attribution

provenance: supported. Targets: GO:0072546.

Exact cited authors/DOIs/PMIDs match current authority metadata. Primary scientific support is limited to the expressly inspected bodies/abstracts and native authority fields.

### Complete-record structured-source applicability

evidence: supported. Targets: GO:0072546.

Positive protein/insertion/transport narratives require actual assessment; original no-expression exclusion is unsupported. Complete fresh catalogue has no yeast/human host; unrelated bacterial data are not proxies.

### Original native validation/render and current inputs

schema: supported. Targets: GO:0072546.

Original pair native validate/render0 and historical hashes match. Current target remains byte-identical to its frozen input. Native protein checks0 are scope-limited; CI is separate.

### Append-only rationale and old finding lineage

provenance: supported. Targets: GO:0072546.

Preserve all dated rationale/history. Exact inherited keys remain traceable; update current notes/status or append clarification during separately authorized curation. No history rewrite is requested.

### Complete record and limitations

completeness: supported. Targets: GO:0072546.

All definition,aliases,parents,components/examples,taxa,functions,quantities,source notes,graph edges,discussions/history read. No maintained images; captions are not pixels. No exhaustive literature-absence claim or automatic optional-field demand.

### Current independent scientific disposition

consistency: concern. Targets: GO:0072546.

Needs curation for two inherited minor inventory/alias findings, with append-only correction.

### Exact complex identity and anatomical boundary

identity: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Specific local EmrAB-TolC identity justified by CPX4268; broader GO1990281 retained as class,not exact replacement.

### Parents,parthood and synonyms

identity: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Efflux-pump parent,CPXxref and functional synonyms remain correctly scoped to tripartite complex.

### Inventory and exact molecular scope

completeness: concern. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Current EmrA label-only and broad EmrB grounding remain actionable given exact NF011715/NF000391 and native joins; TolC exact family remains supported.

### Accession,primary name,alias and native inventory

grounding: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

3 reviewed K12 examples and 3 COVERED nodes match exact primary gene/status/accession and current singleton queries. Reference annotation does not identify every experimental expression strain.

### Primary experiments and access scope

evidence: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Modern Zhong complete pump6:1:3 architecture and native CPX composition are distinct from Borges-Walmsley proposed EmrA trimer and Yousefian low-resolution whole-pump abstract. Modern engineered EA is inactive; FA and wild-type assays provide separate functional evidence.

### Stoichiometry and measured scope

grounding: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

CPX explicit participants and8ZAL deposited model agree EmrA6,EmrB1,TolC3,total10. Engineered EA modeled chain count is not a universal native-state experimental stoichiometry guarantee.

### Formation necessity versus membership and activity

grounding: unknown. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Transport/insertion,growth and structural membership do not automatically establish a universal formation requirement. Existing ESSENTIAL components denote defining tripartite membership, but new CPX evidence notes must not attribute an unprovided essentiality classification; no blanket retyping of these older values is demanded by this narrow finding.

### Whole causal graph and substantive stale refresh

graph: concern. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

All four new edges substantively refreshed. Three protein contributions and coupled outer export remain supported, but their CPX notes falsely credit native authority with essentiality classification. Scope correction concerns attribution,not denial of pump assembly or efflux.

### Biological and experimental host scope

scope: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

CPX/native examplesK12; Zhong gene sourceMG1655 differs from C43(DE3)delta-acrAB assay host and engineered constructs. Qualitative COMMON/VARIABLE labels are not prevalence surveys.

### Citation and evidence attribution

provenance: concern. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Exact cited authors/DOIs/PMIDs match current authority metadata. New CPX essentiality notes are the separate concrete source-attribution defect; old and new measured sources remain distinguished.

### Complete-record structured-source applicability

evidence: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Positive protein/insertion/transport narratives require actual assessment; original no-expression exclusion is unsupported. Matched reference E.coli precise1k bounds: tolC has SoxS22 membership; emrA/emrB no thresholded hit. No expression→assembly inference.

### Original native validation/render and current inputs

schema: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Original pair native validate/render0 and historical hashes match. Current target is stale and all four new edges/history assessed independently. Native protein checks0 are scope-limited; CI is separate.

### Append-only rationale and old finding lineage

provenance: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Preserve all dated rationale/history. Exact inherited keys remain traceable; update current notes/status or append clarification during separately authorized curation. No history rewrite is requested.

### Complete record and limitations

completeness: supported. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

All definition,aliases,parents,components/examples,taxa,functions,quantities,source notes,graph edges,discussions/history read. No maintained images; captions are not pixels. No exhaustive literature-absence claim or automatic optional-field demand.

### Current independent scientific disposition

consistency: concern. Targets: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex.

Needs curation for inherited exact-family minor and narrow new CPX attribution minor; stale review can be refreshed within review bundles without record edits.

### Exact complex identity and anatomical boundary

identity: supported. Targets: GO:1990207.

Exact GO1990207 and TPP-bound EmrE homodimer retained; broad SMR family is not the whole complex.

### Parents,parthood and synonyms

identity: supported. Targets: GO:1990207.

Transmembrane-transporter parent and narrow EmrE synonym remain appropriate.

### Inventory and exact molecular scope

completeness: concern. Targets: GO:1990207.

Exact NF042984 supports named EmrE constituent; broader NF007087/IPR045324 do not justify permanent label-only deferral.

### Accession,primary name,alias and native inventory

grounding: supported. Targets: GO:1990207.

1 reviewed K12 examples and 1 COVERED nodes match exact primary gene/status/accession and current singleton queries. Reference annotation does not identify every experimental expression strain.

### Primary experiments and access scope

evidence: supported. Targets: GO:1990207.

Chen corrected TPP-bound dimer supports orientation and drug-binding scope; earlier distorted acidic apo and defunct structures are not substituted. No all-SMR or full kinetic mechanism asserted.

### Stoichiometry and measured scope

grounding: supported. Targets: GO:1990207.

Two EmrE subunits verified in3B5D assembly; binding protein:drug ratio2:1 is a different quantity.

### Formation necessity versus membership and activity

grounding: unknown. Targets: GO:1990207.

Transport/insertion,growth and structural membership do not automatically establish a universal formation requirement. Current UNKNOWN is preserved; corrected dimer structure and binding assays do not force a universal formation flag.

### Whole causal graph and substantive stale refresh

graph: supported. Targets: GO:1990207.

FUNCTION/MECHANISTIC graph describes directly supported antiparallel assembly and coarse drug transport; no detailed alternating-access/proton cycle is inferred from coordinates.

### Biological and experimental host scope

scope: supported. Targets: GO:1990207.

GO common-bacterial wording does not imply universalBacteria2 presence; K12 reference protein differs from BL21(DE3) recombinant and cell-free sources. Qualitative COMMON/VARIABLE labels are not prevalence surveys.

### Citation and evidence attribution

provenance: supported. Targets: GO:1990207.

Exact cited authors/DOIs/PMIDs match current authority metadata. Primary scientific support is limited to the expressly inspected bodies/abstracts and native authority fields.

### Complete-record structured-source applicability

evidence: supported. Targets: GO:1990207.

Positive protein/insertion/transport narratives require actual assessment; original no-expression exclusion is unsupported. Matched E.coli precise1k emrE belongs to ROS TALE Amp9; this expression context does not establish homodimer topology or necessity.

### Original native validation/render and current inputs

schema: supported. Targets: GO:1990207.

Original pair native validate/render0 and historical hashes match. Current target remains byte-identical to its frozen input. Native protein checks0 are scope-limited; CI is separate.

### Append-only rationale and old finding lineage

provenance: supported. Targets: GO:1990207.

Preserve all dated rationale/history. Exact inherited keys remain traceable; update current notes/status or append clarification during separately authorized curation. No history rewrite is requested.

### Complete record and limitations

completeness: supported. Targets: GO:1990207.

All definition,aliases,parents,components/examples,taxa,functions,quantities,source notes,graph edges,discussions/history read. No maintained images; captions are not pixels. No exhaustive literature-absence claim or automatic optional-field demand.

### Current independent scientific disposition

consistency: concern. Targets: GO:1990207.

Needs curation for inherited exact-family minor, retaining correct dimer/source biology.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0070939, GO:0071819, GO:1990065, GO:0032126, cellstructuremech:ejectisome, GO:0031391, GO:0033588, GO:0072546, cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex, GO:1990207.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Resolve the Tip20 family mapping

minor / open / confirmed; issue key: dsl1-nzr-tip20-exact-family.

Tip20 remains REVIEWED_LABEL_ONLY under an open three-subunit mapping task, but native IPR007528 is a whole-protein RINT1/Tip20 family and P33891 independently has that cross-reference. The inspected Dsl1/Sec39 domain identifiers do not resolve their whole-protein classes.

### micro-F2: Record the demonstrated Dsl1 assembly dependency

minor / open / confirmed; issue key: dsl1-nzr-dsl1-reconstitution-formation-dependency.

The current Dsl1 component evidence omits the direct purified-system bridging/association observation demonstrated in freshly inspected Tripathi Results S6 and Figure 4: Tip20 and Sec39 do not associate directly, whereas Dsl1 binds both and links the reconstituted ternary core. This is a bounded evidence/annotation gap, not a demand to replace global UNKNOWN essentiality with universal ESSENTIAL. Fresh Meiringer support is abstract tier only; its historical body reading is not newly certified.

### micro-F3: Resolve three DUB constituent family mappings

minor / open / confirmed; issue key: dubm-sgf11-sus1-sgf73-exact-families.

The open mapping task leaves Sgf11, Sus1 and Sgf73 as REVIEWED_LABEL_ONLY despite exact full-protein families IPR013246, IPR018783 and IPR037804, independently present in their example cross-references. The broader UBP8 candidates checked here do not justify a fourth mapping.

### plaque-t6-F1: Separate six subunit identities from holoenzyme stoichiometry

major / open / confirmed; issue key: elongator-copy-number.

The active definition equates six distinct proteins with a heterohexamer of two heterotrimers. Current GO repeats this old wording, but later primary yeast structures resolve two Elp123 lobes and a majority one Elp456 heterohexamer. Setiaputra also measures alternate double-ring loading under specific preparations. Correct the active copy-number account without imposing invariant occupancy or rewriting dated discussion rationale; append a current evidence note.

### plaque-t6-F2: Resolve the six exact Elongator protein families

minor / open / confirmed; issue key: elongator-exact-families.

All six rows remain label-only merely because exact full-class mappings were deferred. Current native family records and independent protein memberships resolve those mappings without using WD, GNAT, radical-SAM or RecA-like domains.

### plaque-t6-F3: Record the measured Elp1 assembly requirement

minor / open / confirmed; issue key: elongator-elp1-formation.

The Elp1 row lacks the directly measured condition-scoped association evidence: in the reported FLAG-Elp4 experiment, elp1 deletion eliminates Elp2/3 recovery while the Elp456 assembly remains. Add this source-scoped formation/association result; a global UNKNOWN may remain where an enum cannot express the tested scope. Neither universal essentiality, viability nor a new experiment follows.

### septin-emc_complex-F1: Represent the source-established yeast EMC constituents

minor / open / confirmed; issue key: emc-known-constituent-deferral.

The record explicitly withholds all eight named yeast subunits pending exact-family/core-accessory curation, although its defining primary structure establishes their membership and the schema permits supported label-only constituents with unresolved essentiality. This is a specific avoidable inventory deferral, not a demand to fill every optional field. Current source review reconfirms the bounded correction. Preserve dated rationale/history; separately authorized curation may append a dated clarification or update current notes/status.

### septin-emc_complex-F2: Correct the reversed EMC3 and EMC5 aliases

minor / open / confirmed; issue key: emc3-emc5-alias-reversal.

The retained dated subunit-boundary rationale reverses EMC3/EMC5 aliases, risking propagation into the expressly deferred constituent curation. Current reviewed authority establishes EMC3/AIM27 and EMC5/KRE27. Preserve the original rationale and dated history; append correct current identity clarification and use it in future rows. OPEN status alone does not make the historical rationale editable. The original acceptance already preserved history; no separate historical-erasure bundle defect is asserted.

### septin-emrab_tolc_multidrug_efflux_transport_complex-F1: Use exact EmrA and EmrB family identities

minor / open / confirmed; issue key: emrab-exact-component-families.

EmrA remains label-only although NF011715 names the exact adaptor family; EmrB is grounded to broader DHA2/EmrB-like IPR004638 while NF000391 resolves exact EmrB. Separate UniProt xrefs corroborate each protein-family join. Current source review reconfirms the bounded correction. Preserve dated rationale/history; separately authorized curation may append a dated clarification or update current notes/status.

### septin-emrab_tolc_multidrug_efflux_transport_complex-new-cpx-attribution: Distinguish CPX stoichiometric membership from an essentiality annotation

minor / open / confirmed; issue key: emrab-cpx-essential-subunit-attribution.

Three newly added protein-to-complex contribution edges say CPX4268 curates EmrA,EmrB and TolC as essential stoichiometric subunits. The complete current authority object identifies participants and6:1:3 stoichiometries with unspecified biological roles and ECO0005547 curator inference; it does not classify their assembly essentiality. Zhong2026 separately establishes engineered assembly and functional assays, including assembled but inactive pump-EA. Preserve the supported contributions and counts, but narrow these CPX notes to membership/stoichiometry or cite and qualify any necessity claim using its actual experimental evidence. This finding does not automatically overturn preexisting ESSENTIAL component values or deny defining membership.

### septin-emre_multidrug_transporter_complex-F1: Ground the EmrE constituent to its exact family

minor / open / confirmed; issue key: emre-exact-protein-family.

The EmrE row remains REVIEWED_LABEL_ONLY because the SMR class is broad, but NF042984 specifically identifies the full EmrE protein family and independent P23895 metadata verifies membership. Current source review reconfirms the bounded correction. Preserve dated rationale/history; separately authorized curation may append a dated clarification or update current notes/status.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, ground Tip20 with IPR007528 and narrow the open mapping task to genuinely unresolved whole-protein classes. Preserve source-scoped homologous-family identity and yeast examples.

- Verify family type and exact example membership.
- Do not substitute Dsl1 or Sec39 domain accessions for whole proteins.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; narrow current prompt/notes only as supported.
- No record edits occur in this review PR.

### micro-A2

In separately authorized record curation, add the directly tested purified Dsl1 bridging/association evidence with its recombinant-protein and pairwise/ternary reconstitution context. Keep global UNKNOWN if broader formation necessity remains unresolved. Preserve distinctions between the ternary core, pairwise subcomplexes, function, domain-mutant growth and organism viability.

- Cite the actually inspected Tripathi Results S6 and Figure 4 with bounded purified-system context; obtain and independently read Meiringer body if making any new body-specific claim from it.
- Do not infer identical Tip20/Sec39 requirements, universal in-vivo absence or globally depleted partners; do not require a new experiment.
- A global UNKNOWN classification may coexist with the added condition-scoped evidence.
- Run applicable native record/schema/identifier/graph gates after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; narrow current prompt/notes only as supported.
- No record edits occur in this review PR.

### micro-A3

In separately authorized record curation, ground the three verified constituent classes and narrow the remaining task to unresolved Ubp8 identity. Retain four-component module boundaries and taxon-paired examples.

- Verify class names/types and each separate accession cross-reference.
- Do not substitute a generic USP domain or hydrolase family for Ubp8.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; narrow current prompt/notes only as supported.
- No record edits occur in this review PR.

### plaque-t6-A1

Retain GO0033588 and six protein identities; correct active definition/roles/graph copy-number wording using the measured two-Elp123 plus Elp456-ring assemblies, explicitly allowing condition-dependent ring occupancy. Append current discussion notes, preserving the dated rationale.

- Do not rewrite historical titles or make a universal occupancy claim beyond the characterized yeast assembly.
- Keep the valid tRNA function and reference protein identities.
- Preserve correct identities and supported biology; pass applicable native validation.
- Preserve dated rationale and curation history verbatim; append current evidence notes or qualify the active decision without rewriting historical provenance.
- Acknowledge the majority single-ring assembly and the documented alternate double-Elp456 loading; do not replace the old universal count with another universal count.

### plaque-t6-A2

Use the six verified full-protein families and align current grounding notes/TODO.

- Treat IPR034687 as Elp3 protein identity, not evidence that every microbial homolog joins a yeast-type complex.
- Preserve correct identities and supported biology; pass applicable native validation.
- Preserve dated rationale and curation history verbatim; append current evidence notes or qualify the active decision without rewriting historical provenance.

### plaque-t6-A3

Attach the primary condition-scoped Elp1-deletion/FLAG-Elp4 association evidence to the Elp1 component; distinguish lost Elp2/3 association from surviving Elp456. Qualify the formation annotation only to the supported scope; a global UNKNOWN may remain where needed.

- Do not equate formation with growth or tRNA catalytic output.
- Preserve independent Elp456 assembly and do not promote all six component enums.
- Preserve correct identities and supported biology; pass applicable native validation.
- Preserve dated rationale and curation history verbatim; append current evidence notes or qualify the active decision without rewriting historical provenance.
- Do not require a universal ESSENTIAL enum or new experiments; capturing the observed bounded assembly association is sufficient.

### septin-emc_complex-A1

Add source-scoped constituent rows for the verified yeast Emc1–6,Emc7,Emc10 inventory, using exact families only where independently verified and otherwise honest label-only notes. Preserve unresolved cross-species core/accessory and formation questions. Preserve dated rationale/history; append clarification or update current notes/status, without rewriting old rationale. This PR changes no record.

- Use the verified aliases EMC3/AIM27 and EMC5/KRE27.
- Do not copy the old GO six-member list or treat all mammalian members as yeast constituents.
- Do not infer individual assembly necessity from growth or insertase phenotypes.
- Preserve correct identities and supported biology; pass applicable native validation.
- Preserve exact inherited finding lineage and dated rationale/history; no automatic review-status promotion.

### septin-emc_complex-A2

Append a dated clarification with verified EMC3/AIM27/P36039/YKL207W and EMC5/KRE27/P40540/YIL027C, and use these mappings in current/future constituent notes; preserve the original rationale and all dated history byte-for-byte.

- Confirm P36039/EMC3/AIM27/YKL207W and P40540/EMC5/KRE27/YIL027C against native identity sources.
- Use the corrected aliases in any separately authorized constituent curation.
- Preserve correct EMC identity and primary membership evidence.
- Preserve exact inherited finding lineage and dated rationale/history; no automatic review-status promotion.

### septin-emrab_tolc_multidrug_efflux_transport_complex-A1

Ground EmrA to verified NF011715 and use exact EmrB NF000391 consistently in component and graph; align current TODO/notes and retain exact TolC, protein examples and source composition. Preserve dated rationale/history; append clarification or update current notes/status, without rewriting old rationale. This PR changes no record.

- Do not treat a shared hairpin/beta-barrel domain as EmrA identity.
- Keep broader DHA2 membership only as contextual classification.
- Preserve correct identities and supported biology; pass applicable native validation.
- Preserve exact inherited finding lineage and dated rationale/history; no automatic review-status promotion.

### septin-emrab_tolc_multidrug_efflux_transport_complex-new-cpx-attribution-action

Narrow the three CPX evidence notes to curated participant membership and stoichiometry; if necessity is retained, distinguish structural definition from tested functional/assembly claims and cite the exact supporting experiment. Preserve correct contributions and6:1:3 counts.

- Do not state CPX4268 supplies an essentiality classification absent from the current source.
- Keep CPX curator inference,engineered8ZAL pump-EA and separate active FA/functional assays distinct.
- Do not infer universal formation necessity from resistance,antiport or membership alone; do not automatically retype older component flags.
- Preserve dated history and pass applicable native gates in separately authorized record curation.

### septin-emre_multidrug_transporter_complex-A1

Use verified NF042984 for the named EmrE constituent and align current grounding rationale/TODO, while preserving GO1990207 for the assembled complex. Preserve dated rationale/history; append clarification or update current notes/status, without rewriting old rationale. This PR changes no record.

- Do not substitute the broad SMR family or infer every SMR protein is an EmrE homodimer.
- Preserve correct identities and supported biology; pass applicable native validation.
- Preserve exact inherited finding lineage and dated rationale/history; no automatic review-status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/dsl1_nzr_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0; current SHA256 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T062447Z-dsl1-nzr-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/dubm_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591; current SHA256 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T062448Z-dubm-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/dxr_protein_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e; current SHA256 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T062449Z-dxr-protein-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/eisosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 032c3bd7a0cc1b125515740752e69d06e4b8bf20529cad61cd62b9559e4f0b72; current SHA256 3f96297240ba46e169dab4e79338949cf92ac200ffd75c509938b12240b1b89c. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261022T062450Z-eisosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/ejectisome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8; current SHA256 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T062451Z-ejectisome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/elg1_rfc_like_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837; current SHA256 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/elongator_holoenzyme_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d; current SHA256 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/emc_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54; current SHA256 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T062453Z-emc-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3f2fc12842c13b847a6c930d89242a164a83e37cfc8840f59fa90fe2c71f0d2c; current SHA256 2ecd59317bfeae525a312c7ba1427b4ad561dfb25b621ff647b42e2205c150d6. Changed record reassessed against current sources. |
| original-review-8 | reviews/structured/20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/emre_multidrug_transporter_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0; current SHA256 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T062455Z-emre-multidrug-transporter-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/dsl1_nzr_complex.yaml; Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target unchanged from original frozen input. |
| micro-prior-0 | reviews/structured/20261022T062447Z-dsl1-nzr-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence tiers, assessments, verdict, findings and actions inspected. Historical checks and access times are not newly executed or fetched. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/0-stale.diff; Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7 | supports | Empty diff. |
| micro-record-1 | data/structures/other/dubm_complex.yaml; Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target unchanged from original frozen input. |
| micro-prior-1 | reviews/structured/20261022T062448Z-dubm-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence tiers, assessments, verdict, findings and actions inspected. Historical checks and access times are not newly executed or fetched. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/1-stale.diff; Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7 | supports | Empty diff. |
| micro-record-2 | data/structures/other/dxr_protein_complex.yaml; Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target unchanged from original frozen input. |
| micro-prior-2 | reviews/structured/20261022T062449Z-dxr-protein-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence tiers, assessments, verdict, findings and actions inspected. Historical checks and access times are not newly executed or fetched. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/2-stale.diff; Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7 | supports | Empty diff. |
| micro-record-3 | data/structures/other/eisosome.yaml; Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target differs by the Pil1/Lsp1 core type, graph family grounding and append-only history. |
| micro-prior-3 | reviews/structured/20261022T062450Z-eisosome-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence tiers, assessments, verdict, findings and actions inspected. Historical checks and access times are not newly executed or fetched. |
| micro-delta-3 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/3-stale.diff; Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7 | supports | Two substantive updates: pil1_lsp1_bar_core component PROTEIN to PROTEIN_COMPLEX and its graph grounding to IPR028245; two dated history events cite earlier corrections. This is reassessed using actual native family and primary assembled-scaffold evidence, without resolving broad historical issues. |
| micro-policy | docs/CURATION.md; Components and Discussions clauses | supports | Taxon-neutral families/classes are valid; formation differs from function and viability. Preserve dated rationale and posed_date; current prompt/notes may be narrowed after separately authorized grounded curation. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; ComponentTypeEnum, EssentialityEnum, causal node types | supports | GENE_OR_PROTEIN permits molecular complexes. A specific assembled core can be PROTEIN_COMPLEX without requiring an obligate heterodimer. UNKNOWN formation can remain when evidence is condition-scoped. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks, full record and evidence contract | supports | Positive named genes/proteins/pathways trigger applicability assessment even without an expression claim. Catalogue coverage and matched gene/module evidence are bounded contextual observations, not assembly evidence. |
| micro-profile | docs/record-review-profile.md; Issue-only persistence, native checks and source provenance | supports | The explicit mixed batch has concrete scientific and bundle issues. No empty optional field, unavailable route or acknowledged unknown alone is a scientific finding. Root owns successor save and global gates. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Claim-scoped constituents and coarse function/assembly graphs | supports | Descriptive membership/function and tested assembly relations are assessed at their declared granularity; exact stoichiometry, universal necessity and mandatory new experiments are not imposed. |
| micro-neighbor-filament | data/structures/cytoskeleton/eisosome_filament.yaml; Complete already-frozen boundary neighbor | supports | Whole eisosome is distinct from the filament and membrane-domain children. Neighbor content is boundary context, not primary evidence or a terminal disposition of its findings. |
| micro-neighbor-mcc | data/structures/envelope/eisosome_membrane_domain_mcc.yaml; Complete already-frozen boundary neighbor | supports | Whole eisosome is distinct from the filament and membrane-domain children. Neighbor content is boundary context, not primary evidence or a terminal disposition of its findings. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/original-audit.json; Eight actual original native validate/render commands; 56 historical input occurrences; eight original artifacts | supports | All four original YAMLs validate and render exactly their retained Markdown; historical input hashes match their recorded revisions, and all eight artifacts equal the original PR head. |
| micro-protein-P33891 | https://rest.uniprot.org/uniprotkb/P33891.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P33891.raw | supports | P33891: UniProtKB reviewed (Swiss-Prot); Protein transport protein TIP20; primary genes ['TIP20']; loci ['YGL145W']; taxon 559292; InterPro ['IPR042044', 'IPR007528', 'IPR042041', 'IPR042042', 'IPR042043', 'IPR042040']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-P45568 | https://rest.uniprot.org/uniprotkb/P45568.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P45568.raw | supports | P45568: UniProtKB reviewed (Swiss-Prot); 1-deoxy-D-xylulose 5-phosphate reductoisomerase; primary genes ['dxr']; loci ['b0173', 'JW0168']; taxon 83333; InterPro ['IPR003821', 'IPR013644', 'IPR013512', 'IPR026877', 'IPR036169', 'IPR036291']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-P50102 | https://rest.uniprot.org/uniprotkb/P50102.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P50102.raw | supports | P50102: UniProtKB reviewed (Swiss-Prot); Ubiquitin carboxyl-terminal hydrolase 8; primary genes ['UBP8']; loci ['YMR223W', 'YM9959.05']; taxon 559292; InterPro ['IPR038765', 'IPR001394', 'IPR050185', 'IPR028889', 'IPR018200', 'IPR013083', 'IPR001607']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-P53165 | https://rest.uniprot.org/uniprotkb/P53165.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P53165.raw | supports | P53165: UniProtKB reviewed (Swiss-Prot); SAGA complex subunit SGF73; primary genes ['SGF73']; loci ['YGL066W']; taxon 559292; InterPro ['IPR013243', 'IPR037804', 'IPR041251']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-P53252 | https://rest.uniprot.org/uniprotkb/P53252.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P53252.raw | supports | P53252: UniProtKB reviewed (Swiss-Prot); Sphingolipid long chain base-responsive protein PIL1; primary genes ['PIL1']; loci ['YGR086C']; taxon 559292; InterPro ['IPR027267', 'IPR028245']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-P53847 | https://rest.uniprot.org/uniprotkb/P53847.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P53847.raw | supports | P53847: UniProtKB reviewed (Swiss-Prot); Protein transport protein DSL1; primary genes ['DSL1']; loci ['YNL258C', 'N0842']; taxon 559292; InterPro ['IPR021876', 'IPR021875', 'IPR038442', 'IPR046362']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-P54003 | https://rest.uniprot.org/uniprotkb/P54003.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P54003.raw | supports | P54003: UniProtKB reviewed (Swiss-Prot); Protein SUR7; primary genes ['SUR7']; loci ['YML052W', 'YM9958.11']; taxon 559292; InterPro ['IPR009571']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-Q03067 | https://rest.uniprot.org/uniprotkb/Q03067.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q03067.raw | supports | Q03067: UniProtKB reviewed (Swiss-Prot); SAGA complex subunit SGF11; primary genes ['SGF11']; loci ['YPL047W']; taxon 559292; InterPro ['IPR013246', 'IPR060617', 'IPR041216']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-Q12230 | https://rest.uniprot.org/uniprotkb/Q12230.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q12230.raw | supports | Q12230: UniProtKB reviewed (Swiss-Prot); Sphingolipid long chain base-responsive protein LSP1; primary genes ['LSP1']; loci ['YPL004C']; taxon 559292; InterPro ['IPR027267', 'IPR028245']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-Q12745 | https://rest.uniprot.org/uniprotkb/Q12745.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q12745.raw | supports | Q12745: UniProtKB reviewed (Swiss-Prot); Protein transport protein SEC39; primary genes ['SEC39']; loci ['YLR440C']; taxon 559292; InterPro ['IPR013244']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-protein-Q6WNK7 | https://rest.uniprot.org/uniprotkb/Q6WNK7.json; Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q6WNK7.raw | supports | Q6WNK7: UniProtKB reviewed (Swiss-Prot); SAGA complex subunit SUS1; primary genes ['SUS1']; loci ['YBR111W-A']; taxon 559292; InterPro ['IPR018783', 'IPR038212']. Native annotation sources are distinct from freshly inspected primary bodies and do not independently certify every linked experiment. |
| micro-query-DSL1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-DSL1-559292.raw | supports | Current bounded query returns ['P53847']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-DSL3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-DSL3-559292.raw | supports | Current bounded query returns ['Q12745']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-LSP1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALSP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-LSP1-559292.raw | supports | Current bounded query returns ['Q12230']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-PIL1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-PIL1-559292.raw | supports | Current bounded query returns ['P53252']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-SEC39-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SEC39-559292.raw | supports | Current bounded query returns ['Q12745']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-SGF11-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SGF11-559292.raw | supports | Current bounded query returns ['Q03067']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-SGF73-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF73%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SGF73-559292.raw | supports | Current bounded query returns ['P53165']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-SUR7-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUR7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SUR7-559292.raw | supports | Current bounded query returns ['P54003']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-SUS1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SUS1-559292.raw | supports | Current bounded query returns ['Q6WNK7']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-TIP20-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATIP20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-TIP20-559292.raw | supports | Current bounded query returns ['P33891']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-UBP8-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AUBP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-UBP8-559292.raw | supports | Current bounded query returns ['P50102']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-dxr-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adxr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-dxr-83333.raw | supports | Current bounded query returns ['P45568']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-query-ispC-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AispC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-ispC-83333.raw | supports | Current bounded query returns ['P45568']; native primary genes and aliases independently inspected. This is current reproducibility, not reconstruction or refutation of a historical selection query. |
| micro-taxon-4751 | https://rest.uniprot.org/taxonomy/4751.json; Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-4751.raw | supports | 4751: Fungi; rank kingdom. Species, reference strain and particular experimental preparation remain distinct. |
| micro-taxon-4932 | https://rest.uniprot.org/taxonomy/4932.json; Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-4932.raw | supports | 4932: Saccharomyces cerevisiae; rank species. Species, reference strain and particular experimental preparation remain distinct. |
| micro-taxon-559292 | https://rest.uniprot.org/taxonomy/559292.json; Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-559292.raw | supports | 559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c); rank strain. Species, reference strain and particular experimental preparation remain distinct. |
| micro-taxon-562 | https://rest.uniprot.org/taxonomy/562.json; Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-562.raw | supports | 562: Escherichia coli; rank species. Species, reference strain and particular experimental preparation remain distinct. |
| micro-taxon-83333 | https://rest.uniprot.org/taxonomy/83333.json; Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-83333.raw | supports | 83333: Escherichia coli (strain K12); rank strain. Species, reference strain and particular experimental preparation remain distinct. |
| micro-go-0000124 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0000124.raw | supports | GO:0000124 SAGA complex; isObsolete=False. A SAGA-type histone acetyltransferase complex that deubiquitinates H2A and/or H2B. This complex is organized into several functional submodules: a structural core including the activator binding module and consisting of ADA1 or a homolog, members of the SPT and TAF protein families as well as promotor recruitment factor TRRAP/TRA1, a histone acetyltransferase (HAT) module consisting of GCN5/KAT2A or PCAF/KAT2B, ADA2, ADA3/NGG1, and SGF29 or homologues thereof, a histone deubiquitinase (DUB) module consisting of ATXN7/SGF73, ATXN7L3/SGF11, ENY2/SUS1 and USP22/UBP8 or homologues thereof, and in some taxa a splicing module consisting of SF3B3 and SF3B5 or homologues thereof (not in fungi). In budding yeast also contains Spt8 which distinguishes it from SAGA-like (SLIK) complex (GO:0046695). |
| micro-go-0004843 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004843; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0004843.raw | supports | GO:0004843 cysteine-type deubiquitinase activity; isObsolete=False. An thiol-dependent isopeptidase activity that cleaves ubiquitin from a target protein to which it is conjugated. |
| micro-go-0005783 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0005783.raw | supports | GO:0005783 endoplasmic reticulum; isObsolete=False. The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached). |
| micro-go-0006890 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006890; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0006890.raw | supports | GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum; isObsolete=False. The directed movement of substances from the Golgi back to the endoplasmic reticulum, mediated by vesicles bearing specific protein coats such as COPI or COG. |
| micro-go-0030604 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030604; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0030604.raw | supports | GO:0030604 1-deoxy-D-xylulose-5-phosphate reductoisomerase activity; isObsolete=False. Catalysis of the reaction: 2-C-methyl-D-erythritol 4-phosphate + NADP+ = 1-deoxy-D-xylulose 5-phosphate + H+ + NADPH. |
| micro-go-0032126-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126/ancestors?relations=is_a; Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032126-ancestors.raw | supports | GO:0032126 eisosome; isObsolete=False. A cell part that is composed of the eisosome membrane or MCC domain, a furrow-like plasma membrane sub-domain and associated integral transmembrane proteins, and the proteins (eisosome filaments) that form a scaffolding lattice on the cytoplasmic face. Eisosomes broadly affect overall plasma membrane organization. Returned ancestors ['GO:0110165', 'GO:0005575', 'GO:0032126'] |
| micro-go-0032126-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126/constraints; Exact term and returned taxon-constraint response; no prevalence census; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032126-constraints.raw | supports | GO:0032126 eisosome; isObsolete=False. A cell part that is composed of the eisosome membrane or MCC domain, a furrow-like plasma membrane sub-domain and associated integral transmembrane proteins, and the proteins (eisosome filaments) that form a scaffolding lattice on the cytoplasmic face. Eisosomes broadly affect overall plasma membrane organization. |
| micro-go-0032126 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032126.raw | supports | GO:0032126 eisosome; isObsolete=False. A cell part that is composed of the eisosome membrane or MCC domain, a furrow-like plasma membrane sub-domain and associated integral transmembrane proteins, and the proteins (eisosome filaments) that form a scaffolding lattice on the cytoplasmic face. Eisosomes broadly affect overall plasma membrane organization. |
| micro-go-0032991 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032991.raw | supports | GO:0032991 protein-containing complex; isObsolete=False. A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together. |
| micro-go-0036286 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036286; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0036286.raw | supports | GO:0036286 eisosome filament; isObsolete=False. A filamentous cortical structure formed, in S. pombe, by the eisosome component Pil1. |
| micro-go-0046695 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046695; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0046695.raw | supports | GO:0046695 SLIK (SAGA-like) complex; isObsolete=False. A SAGA-type histone acetyltransferase complex that contains a smaller form of Spt7 (lacking the SPT8 binding region) than the fungal SAGA complex, and consequently lacks Spt8. The complex is involved in the yeast retrograde response pathway, which is important for gene expression changes during mitochondrial dysfunction. |
| micro-go-0070939-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/ancestors?relations=is_a; Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0070939-ancestors.raw | supports | GO:0070939 Dsl1/NZR complex; isObsolete=False. A multisubunit tethering complex, i.e. a protein complex involved in mediating the initial interaction between vesicles and the membranes with which they fuse, that is involved in trafficking from the Golgi apparatus to the ER. In Saccharomyces cerevisiae the Dsl1p complex contains Dsl1p, Tip20p, and Sec39p. Returned ancestors ['GO:0070939', 'GO:0032991', 'GO:0140534', 'GO:0099023', 'GO:0005575'] |
| micro-go-0070939-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/constraints; Exact term and returned taxon-constraint response; no prevalence census; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0070939-constraints.raw | supports | GO:0070939 Dsl1/NZR complex; isObsolete=False. A multisubunit tethering complex, i.e. a protein complex involved in mediating the initial interaction between vesicles and the membranes with which they fuse, that is involved in trafficking from the Golgi apparatus to the ER. In Saccharomyces cerevisiae the Dsl1p complex contains Dsl1p, Tip20p, and Sec39p. |
| micro-go-0070939 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0070939.raw | supports | GO:0070939 Dsl1/NZR complex; isObsolete=False. A multisubunit tethering complex, i.e. a protein complex involved in mediating the initial interaction between vesicles and the membranes with which they fuse, that is involved in trafficking from the Golgi apparatus to the ER. In Saccharomyces cerevisiae the Dsl1p complex contains Dsl1p, Tip20p, and Sec39p. |
| micro-go-0071819-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/ancestors?relations=is_a; Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0071819-ancestors.raw | supports | GO:0071819 DUBm complex; isObsolete=False. A protein complex that forms part of SAGA-type complexes SAGA and SLIK, and mediates deubiquitination of histone H2B. In S. cerevisiae, the DUBm consists of the proteins Ubp8p, Sgf11p, Sus1p, and Sgf73p. Returned ancestors ['GO:0140513', 'GO:0071819', 'GO:0032991', 'GO:0005575'] |
| micro-go-0071819-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/constraints; Exact term and returned taxon-constraint response; no prevalence census; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0071819-constraints.raw | supports | GO:0071819 DUBm complex; isObsolete=False. A protein complex that forms part of SAGA-type complexes SAGA and SLIK, and mediates deubiquitination of histone H2B. In S. cerevisiae, the DUBm consists of the proteins Ubp8p, Sgf11p, Sus1p, and Sgf73p. |
| micro-go-0071819 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0071819.raw | supports | GO:0071819 DUBm complex; isObsolete=False. A protein complex that forms part of SAGA-type complexes SAGA and SLIK, and mediates deubiquitination of histone H2B. In S. cerevisiae, the DUBm consists of the proteins Ubp8p, Sgf11p, Sus1p, and Sgf73p. |
| micro-go-0090512 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0090512; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0090512.raw | supports | GO:0090512 eisosome membrane domain/MCC; isObsolete=False. A plasma membrane part that is composed of a furrow-like plasma membrane domain and associated integral transmembrane proteins. |
| micro-go-0099023 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0099023; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0099023.raw | supports | GO:0099023 vesicle tethering complex; isObsolete=False. Any protein complex that plays a role in vesicle tethering. |
| micro-go-0140513 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140513; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0140513.raw | supports | GO:0140513 nuclear protein-containing complex; isObsolete=False. A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together in the nucleus. |
| micro-go-1990065-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/ancestors?relations=is_a; Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-1990065-ancestors.raw | supports | GO:1990065 Dxr protein complex; isObsolete=False. A protein complex that is involved in the MEP pathway of IPP biosynthesis. It catalyzes the NADP-dependent rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol 4-phosphate (MEP). Returned ancestors ['GO:0032991', 'GO:0005575', 'GO:1990065'] |
| micro-go-1990065-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/constraints; Exact term and returned taxon-constraint response; no prevalence census; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-1990065-constraints.raw | supports | GO:1990065 Dxr protein complex; isObsolete=False. A protein complex that is involved in the MEP pathway of IPP biosynthesis. It catalyzes the NADP-dependent rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol 4-phosphate (MEP). |
| micro-go-1990065 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065; Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-1990065.raw | supports | GO:1990065 Dxr protein complex; isObsolete=False. A protein complex that is involved in the MEP pathway of IPP biosynthesis. It catalyzes the NADP-dependent rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol 4-phosphate (MEP). |
| micro-ipr-IPR003821-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003821/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR003821-retry.raw | supports | IPR003821: 1-deoxy-D-xylulose 5-phosphate reductoisomerase; native type family. Native family identity/type and maintained example xrefs assessed; database prose is authority context, not a primary experiment. |
| micro-ipr-IPR007528 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007528/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR007528.raw | supports | IPR007528: RINT-1/Tip20; native type family. Native family identity/type and maintained example xrefs assessed; database prose is authority context, not a primary experiment. |
| micro-ipr-IPR009571 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009571/; Complete native entry metadata/type/description and flags [False, False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR009571.raw | supports | IPR009571: Membrane protein SUR7/Rim9-like, fungi; native type family. Broad SUR7/Rim9-like family, including other proteins; no automatic exact Sur7-only mapping. |
| micro-ipr-IPR013244-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013244/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR013244-retry.raw | supports | IPR013244: Sec39 domain; native type domain. A domain is not substituted for the complete named constituent class. |
| micro-ipr-IPR013246 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013246/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR013246.raw | supports | IPR013246: SAGA complex, Sgf11 subunit; native type family. Native family identity/type and maintained example xrefs assessed; database prose is authority context, not a primary experiment. |
| micro-ipr-IPR018783 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018783/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR018783.raw | supports | IPR018783: Transcription factor, enhancer of yellow 2; native type family. Native family identity/type and maintained example xrefs assessed; database prose is authority context, not a primary experiment. |
| micro-ipr-IPR021875 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021875/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR021875.raw | supports | IPR021875: Retrograde transport protein Dsl1 N-terminal domain; native type domain. A domain is not substituted for the complete named constituent class. |
| micro-ipr-IPR021876 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021876/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR021876.raw | supports | IPR021876: Retrograde transport protein Dsl1, C-terminal domain; native type domain. A domain is not substituted for the complete named constituent class. |
| micro-ipr-IPR028245-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028245/; Complete native entry metadata/type/description and flags [False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR028245-retry.raw | supports | IPR028245: Eisosome component PIL1/LSP1; native type family. Native family identity/type and maintained example xrefs assessed; database prose is authority context, not a primary experiment. |
| micro-ipr-IPR028889 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028889/; Complete native entry metadata/type/description and flags [False, False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR028889.raw | supports | IPR028889: Ubiquitin specific protease USP, catalytic domain; native type domain. A domain is not substituted for the complete named constituent class. |
| micro-ipr-IPR037804 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037804/; Complete native entry metadata/type/description and flags [False, False]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR037804.raw | supports | IPR037804: SAGA-associated factor 73; native type family. Native family identity/type and maintained example xrefs assessed; database prose is authority context, not a primary experiment. |
| micro-ipr-IPR050185 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050185/; Complete native entry metadata/type/description and flags [True]; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR050185.raw | supports | IPR050185: Ubiquitin carboxyl-terminal hydrolase; native type family. Broad ubiquitin carboxyl-terminal hydrolase family; description is flagged LLM-generated and is excluded as biological support. Native metadata does not establish exact Ubp8 identity. |
| micro-meta-10.1016_j.jbc.2021.100671 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jbc.2021.100671%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1016_j.jbc.2021.100671.raw | supports | PMID 33864814; DOI 10.1016/j.jbc.2021.100671; SAGA and SAGA-like SLIK transcriptional coactivators are structurally and biochemically equivalent.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1016_j.jmb.2004.10.030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jmb.2004.10.030%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1016_j.jmb.2004.10.030.raw | supports | PMID 15567415; DOI 10.1016/j.jmb.2004.10.030; The crystal structure of E.coli 1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with the antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed enzyme conformation.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1038_nature04472 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature04472%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1038_nature04472.raw | supports | PMID 16496001; DOI 10.1038/nature04472; Eisosomes mark static sites of endocytosis.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1038_nsmb.1548 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb.1548%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1038_nsmb.1548.raw | supports | PMID 19151722; DOI 10.1038/nsmb.1548; Structural characterization of Tip20p and Dsl1p, subunits of the Dsl1p vesicle tethering complex.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1038_s41586-020-1933-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-020-1933-5%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1038_s41586-020-1933-5.raw | supports | PMID 31969703; DOI 10.1038/s41586-020-1933-5; Structure of the transcription coactivator SAGA.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1074_jbc.M110.215327 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.215327%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1074_jbc.M110.215327.raw | supports | PMID 21550981; DOI 10.1074/jbc.m110.215327; The Dsl1 protein tethering complex is a resident endoplasmic reticulum complex, which interacts with five soluble NSF (N-ethylmaleimide-sensitive factor) attachment protein receptors (SNAREs): implications for fusion and fusion regulation.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1083_jcb.201104040 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201104040%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1083_jcb.201104040.raw | supports | PMID 22123866; DOI 10.1083/jcb.201104040; Eisosome proteins assemble into a membrane scaffold.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1091_mbc.e05-01-0056 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e05-01-0056%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1091_mbc.e05-01-0056.raw | supports | PMID 15958492; DOI 10.1091/mbc.e05-01-0056; Dsl1p, Tip20p, and the novel Dsl3(Sec39) protein are required for the stability of the Q/t-SNARE complex at the endoplasmic reticulum in yeast.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1091_mbc.e08-03-0313 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e08-03-0313%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1091_mbc.e08-03-0313.raw | supports | PMID 19037108; DOI 10.1091/mbc.e08-03-0313; Pil1 controls eisosome biogenesis.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1091_mbc.e10-12-1021 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e10-12-1021%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1091_mbc.e10-12-1021.raw | supports | PMID 21593205; DOI 10.1091/mbc.e10-12-1021; The eisosome core is composed of BAR domain proteins.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-10.1101_gad.1144003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144003%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1101_gad.1144003.raw | supports | PMID 14563679; DOI 10.1101/gad.1144003; Transcriptional activation via sequential histone H2B ubiquitylation and deubiquitylation, mediated by SAGA-associated Ubp8.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-11493604 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11493604+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-11493604.raw | supports | PMID 11493604; DOI 10.1074/jbc.m105833200; The coatomer-interacting protein Dsl1p is required for Golgi-to-endoplasmic reticulum retrieval in yeast.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-11739780 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11739780+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-11739780.raw | supports | PMID 11739780; DOI 10.1091/mbc.12.12.3783; Golgi-to-endoplasmic reticulum (ER) retrograde traffic in yeast requires Dsl1p, a component of the ER target site that interacts with a COPI coat subunit.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-11784867 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11784867+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-11784867.raw | supports | PMID 11784867; DOI 10.1128/mcb.22.3.927-934.2002; The Sur7p family defines novel cortical domains in Saccharomyces cerevisiae, affects sphingolipid metabolism, and is involved in sporulation.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-12469340 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12469340+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-12469340.raw | supports | PMID 12469340; DOI 10.1002/1615-9861(200212)2:12&lt;1706::aid-prot1706&gt;3.0.co;2-k; Subproteomics: identification of plasma membrane proteins from the yeast Saccharomyces cerevisiae.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-14562095.raw | supports | PMID 14562095; DOI 10.1038/nature02026; Global analysis of protein localization in budding yeast.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-15567415 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15567415+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-15567415.raw | supports | PMID 15567415; DOI 10.1016/j.jmb.2004.10.030; The crystal structure of E.coli 1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with the antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed enzyme conformation.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-15958492 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15958492+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-15958492.raw | supports | PMID 15958492; DOI 10.1091/mbc.e05-01-0056; Dsl1p, Tip20p, and the novel Dsl3(Sec39) protein are required for the stability of the Q/t-SNARE complex at the endoplasmic reticulum in yeast.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-16496001 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16496001+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-16496001.raw | supports | PMID 16496001; DOI 10.1038/nature04472; Eisosomes mark static sites of endocytosis.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-16855026 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16855026+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-16855026.raw | supports | PMID 16855026; DOI 10.1091/mbc.e06-02-0098; The mRNA export factor Sus1 is involved in Spt/Ada/Gcn5 acetyltransferase-mediated H2B deubiquitinylation through its interaction with Ubp8 and Sgf11.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-20230609 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20230609+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-20230609.raw | supports | PMID 20230609; DOI 10.1186/1471-2121-11-19; A novel link between Sus1 and the cytoplasmic mRNA decay machinery suggests a broad role in mRNA metabolism.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-22932476 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22932476+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-22932476.raw | supports | PMID 22932476; DOI 10.1186/2045-3701-2-30; The nuclear localization of SWI/SNF proteins is subjected to oxygen regulation.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-meta-25002088 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25002088+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-25002088.raw | context_only | PMID 25002088; DOI 10.1146/annurev-micro-091313-103507; Fungal membrane organization: the eisosome concept.. Douglas/Konopka is secondary review context only. |
| micro-meta-8334998 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8334998+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-8334998.raw | supports | PMID 8334998; DOI 10.1002/j.1460-2075.1993.tb05944.x; The TIP1 gene of Saccharomyces cerevisiae encodes an 80 kDa cytoplasmic protein that interacts with the cytoplasmic domain of Sec20p.. Primary study metadata/abstract tier; separately cited body evidence is used only where genuinely retrieved. |
| micro-tripathi | https://pmc-oa-opendata.s3.amazonaws.com/PMC2635920.1/PMC2635920.1.xml; Introduction S1, Results S5 and S6, Figure 4 caption, Methods S10 protein production and S13 binding assays; first three S7 paragraphs only; no figure pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/tripathi.raw | supports | Purified recombinant yeast Dsl1 links Tip20 and Sec39: Sec39 does not bind Tip20 directly, and full-length proteins reconstitute a stoichiometric ternary complex. N/C contacts, domain mutants, growth phenotypes and reconstitution are distinct. No universal in-vivo absence conclusion. |
| micro-wang | https://pmc-oa-opendata.s3.amazonaws.com/PMC6994259.1/PMC6994259.1.xml; Complete 13 direct main-body paragraphs; Methods S2 purification, S4 sample preparation, S5 image processing and S7 model building; no figure pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/wang.raw | supports | Primary SAGA structural study supports the four-subunit DUB module, Sgf73 N-terminal module incorporation and central core anchoring. CB010 preparation is not identical to all S288C example strains. Apo DUB low-resolution fit and nucleosome-bound map have different structural limits. |
| micro-adamus | https://pmc-oa-opendata.s3.amazonaws.com/PMC8131915.1/PMC8131915.1.xml; Results sec1.1 purification, sec1.2 XL-MS, sec1.4 DUB activity, sec1.7 EM and embedded Figures 1/2/6 captions; Methods sec3.1,3.4,3.11; no figure pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adamus.raw | supports | Primary SAGA/SLIK purification, mass spectrometry, cross-linking and activity support shared DUB composition/function in the tested yeast preparations. Low-resolution EM cannot resolve all orientations; Ub-AMC assay is not every physiological histone substrate. |
| micro-karotki | https://pmc-oa-opendata.s3.amazonaws.com/PMC3257569.1/PMC3257569.1.xml; Complete main-body section indices 2,4,8,10,11,13,14,18,19: recombinant assembly, membrane binding, native purification/localization, Discussion and stated methods; no figure pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/karotki.raw | supports | Pil1/Lsp1 self-assembly and membrane scaffolding are directly supported. Native yeast cores contain both proteins; the paper leaves heterodimer versus mixed homodimer arrangement unresolved. W303/S288C native preparations and recombinant bacterial production remain distinct. |
| micro-olivera | https://pmc-oa-opendata.s3.amazonaws.com/PMC3128537.1/PMC3128537.1.xml; Complete main-body section indices 2,3,4,5,8,9,12,16,17: structural modeling, BAR-domain tests, mutant organization, Discussion and stated methods; no figure pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/olivera.raw | supports | Primary experiments support Pil1/Lsp1 BAR-like membrane interaction, tubulation and eisosome organization. Homology models, COS7 coexpression and yeast mutants are not a universally fixed native heterodimer or full assembly mechanism. |
| micro-walther-html | https://www.nature.com/articles/nature04472; Genuine publisher main article paragraphs 0–17 and included Figure 1–3 text captions; no figure pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/walther-html.raw | supports | Primary discovery paper supports immobile yeast assemblies, Pil1/Lsp1 copurification and Sur7 colocalization. Later morphology/membrane-domain work bounds the current stable-organization claim; early endocytosis interpretation is not promoted to a universal causal mechanism. |
| micro-pdb-entry | https://data.rcsb.org/rest/v1/core/entry/1Q0Q; Complete entry identity, method/resolution and primary citation; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-entry.raw | supports | 1Q0Q is the deposited Dxr substrate/NADPH complex at 1.9 Angstrom, linked to PMID15567415; the paper title emphasizing fosmidomycin does not make this deposition an inhibitor-only structure. |
| micro-pdb-polymer | https://data.rcsb.org/rest/v1/core/polymer_entity/1Q0Q/1; Entity 1 source organism, expression host, chain identifiers and SIFTS reference; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-polymer.raw | supports | Dxr entity maps P45568; source E. coli species562, recombinant expression BL21(DE3), two protein chains A/B. Reference K12 identity is not an assertion that every experiment used that strain. |
| micro-pdb-assembly | https://data.rcsb.org/rest/v1/core/assembly/1Q0Q/1; Assembly 1 author/software assignments, protein count and symmetry; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-assembly.raw | supports | Author/software-supported C2 dimer with two protein copies. Additional ligand asym IDs are not additional protein subunits. |
| micro-pdb-ligand-2 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/2; Complete nonpolymer entity 2; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-ligand-2.raw | supports | DXP substrate is present, two molecules. |
| micro-pdb-ligand-3 | https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/3; Complete nonpolymer entity 3; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-ligand-3.raw | supports | NDP is reduced NADPH, two molecules; deposition supports the canonical substrate/cofactor note. |
| micro-access-meiringer | https://pmc-oa-opendata.s3.amazonaws.com/PMC3137077.1/PMC3137077.1.xml; Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meiringer.receipt.json | context_only | Actual HTTP 404; failed route or challenge HTML, not an inspected primary article body. Successful metadata/abstract or separate primary routes are separately recorded. |
| micro-access-meiringer-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC3137077/; Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meiringer-html.receipt.json | context_only | Actual HTTP 200; failed route or challenge HTML, not an inspected primary article body. Successful metadata/abstract or separate primary routes are separately recorded. |
| micro-access-meiringer-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3137077/; Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meiringer-legacy.receipt.json | context_only | Actual HTTP 200; failed route or challenge HTML, not an inspected primary article body. Successful metadata/abstract or separate primary routes are separately recorded. |
| micro-access-kraynack-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1196311/; Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/kraynack-legacy.receipt.json | context_only | Actual HTTP 200; failed route or challenge HTML, not an inspected primary article body. Successful metadata/abstract or separate primary routes are separately recorded. |
| micro-access-henry-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC280615/; Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/henry-legacy.receipt.json | context_only | Actual HTTP 200; failed route or challenge HTML, not an inspected primary article body. Successful metadata/abstract or separate primary routes are separately recorded. |
| micro-access-adapter-genes | https://imodulondb.org/api/datasets/e_coli/precise1k/genes; Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-genes.receipt.json | context_only | Actual HTTP 200; misrouted application HTML, not the requested gene data. |
| micro-historical-3-micro53-douglas2014-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507; Original retained observation reviews/structured/20261022T062450Z-eisosome-audit/review.yaml evidence micro53-douglas2014-publisher; historical fetch, not newly refetched | context_only | Historical publisher HTTP403 challenge explicitly provided no article body. Original authority kind is corrected to validation/context_only; original URL/time/hash retained without alleging false access. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/catalogue.raw | context_only | Twenty returned organism rows and 28 organism/dataset entries inspected. E. coli precise1k is covered; no yeast or other eukaryotic dataset appears in this complete response. Catalogue absence is not biological absence. |
| micro-adapter-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete e_coli/precise1k dataset metadata; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-meta.raw | context_only | Five strains BW25113, DGF-298, GMOS, MG1655 and W3110; 201 modules, 1,035 samples, 518 conditions and 4,257 reference genes. Not a matched claim for every recombinant preparation or species. |
| micro-adapter-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 module identifiers/names/metadata; generated summaries excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-modules.raw | context_only | Complete dataset module inventory establishes the bounded search population; no expression activity contrast or inferred binding/formation claim. |
| micro-adapter-dxr-memberships | https://imodulondb.org/api/genes/b0173/imodulons?organism=e_coli&amp;dataset=precise1k; All201 b0173 membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-dxr-memberships.raw | context_only | Dxr b0173 has one thresholded hit: UC-2/module167, weight0.061854521, threshold0.042864802; its functional annotation is Unknown. Other200 nonhits do not imply absence or dispensability. |
| micro-adapter-gene-dxr | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;search=b0173&amp;limit=5000; Complete returned 4,257 reference-gene rows; exact b0173 identity join; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-gene-dxr.raw | context_only | Endpoint returned the complete 4,257-gene table despite search parameter. Exact b0173 row is dxr/P45568, matching the maintained example. Only the bounded identity join is used, not a claim that every unrelated gene was scientifically assessed. |
| micro-adapter-module167 | https://imodulondb.org/api/imodulons/e_coli/precise1k/167; Module167 metadata, all96 member IDs/weights and threshold; activities/AI summary excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-module167.raw | context_only | UC-2 has Unknown function/regulator, 96 members and threshold0.042864802. Membership corroborates the exact Dxr hit without providing a mechanistic interpretation. |
| micro-adapter-module167-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/167/genes; All96 member identity/weight rows and threshold; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-module167-genes.raw | context_only | b0173 dxr/P45568 has weight0.061854521 and true membership. Complete membership IDs match module metadata. This is computational expression context, not complex stoichiometry, formation or essentiality. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical 2026-11-03T00:49:00.848907–00:49:00.863225Z receipt | context_only | Historical runner unavailable/exit1 permission limitation; no fresh runner invocation. Current official direct-source catalogue/gene/module fallback is separately documented. |
| micro-native-dsl1_nzr_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 3 reviewed maintained examples and 3 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-dsl1_nzr_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-causal.log SHA256 087c7ae1c1ed5570e68b1849441b8171b6fc5520408fe4812cd3c9d4cd6d205a | supports | Actual exit0; 3 reviewed maintained examples and 3 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-dubm_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 4 reviewed maintained examples and 4 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-dubm_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-causal.log SHA256 41ef97ef6e5f7ed9b222fedc877f99f969f29044d849f5f84419f75ca162120e | supports | Actual exit0; 4 reviewed maintained examples and 4 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-dxr_protein_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 1 reviewed maintained examples and 1 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-dxr_protein_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-causal.log SHA256 df2ee219a494b4e317e88c9b090a533138fc496c62bc029f1baba3b3c92f069c | supports | Actual exit0; 1 reviewed maintained examples and 1 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-eisosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 3 reviewed maintained examples and 2 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| micro-native-eisosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-causal.log SHA256 b0e108f81d2b02fa358798328d9b302fd746704f610e9c3665ab02ca281b9d99 | supports | Actual exit0; 3 reviewed maintained examples and 2 COVERED typed protein nodes; no partial or unanchored typed nodes in this assigned record. This verifies implemented identity/xref coverage, not complete biology or exact family scope. |
| plaque-curation | docs/CURATION.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-field-guide | docs/SCHEMA.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-protein-skill | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-graph-skill | .claude/skills/curate-causal-graphs/SKILL.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-review-profile | docs/record-review-profile.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-review-contract | docs/record-reviews.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-review-schema | schema/record_review.yaml; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-structure-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-agents | AGENTS.md; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-review-config | conf/record_review.yaml; Frozen current policy/schema; relevant component identity, grounding, source applicability, formation, graph and append-only historical discussion rules | context_only | Native review and modelling rules; formation differs from viability, optional protein examples are not mandatory, current evidence must be scoped, and historical rationale is preserved rather than rewritten. |
| plaque-record-4 | data/structures/other/ejectisome.yaml; Complete current record including definition, components, taxa, examples, graph, discussions and history | supports | Current bytes independently read and unchanged from the original frozen input; no record edits or status promotion. |
| plaque-original-4-yaml | reviews/structured/20261022T062451Z-ejectisome-audit/review.yaml; Complete immutable original; frozen inputs, checks, scientific assessments, findings, actions and limitations | context_only | Historical review independently reassessed. Historical commands and access timestamps are not represented as current executions. |
| plaque-original-4-md | reviews/structured/20261022T062451Z-ejectisome-audit/review.md; Complete immutable original; frozen inputs, checks, scientific assessments, findings, actions and limitations | context_only | Historical review independently reassessed. Historical commands and access timestamps are not represented as current executions. |
| plaque-record-5 | data/structures/other/elg1_rfc_like_complex.yaml; Complete current record including definition, components, taxa, examples, graph, discussions and history | supports | Current bytes independently read and unchanged from the original frozen input; no record edits or status promotion. |
| plaque-original-5-yaml | reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.yaml; Complete immutable original; frozen inputs, checks, scientific assessments, findings, actions and limitations | context_only | Historical review independently reassessed. Historical commands and access timestamps are not represented as current executions. |
| plaque-original-5-md | reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.md; Complete immutable original; frozen inputs, checks, scientific assessments, findings, actions and limitations | context_only | Historical review independently reassessed. Historical commands and access timestamps are not represented as current executions. |
| plaque-record-6 | data/structures/other/elongator_holoenzyme_complex.yaml; Complete current record including definition, components, taxa, examples, graph, discussions and history | supports | Current bytes independently read and unchanged from the original frozen input; no record edits or status promotion. |
| plaque-original-6-yaml | reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.yaml; Complete immutable original; frozen inputs, checks, scientific assessments, findings, actions and limitations | context_only | Historical review independently reassessed. Historical commands and access timestamps are not represented as current executions. |
| plaque-original-6-md | reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.md; Complete immutable original; frozen inputs, checks, scientific assessments, findings, actions and limitations | context_only | Historical review independently reassessed. Historical commands and access timestamps are not represented as current executions. |
| plaque-input-original-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/input-original-proof.json; All49 current source/worktree inputs;41 original frozen-input occurrences;3 native original validations and deterministic Markdown comparisons | supports | All49 current frozen inputs and41 historical occurrences match. All3 original YAML files validate and reproduce their committed Markdown exactly; all3 assigned target hashes are unchanged. |
| plaque-native-ejectisome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-verify-receipt.json; Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-verify.log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero protein_examples; one GENE_OR_PROTEIN ejectisin node is NO_GENE_SYMBOLS. This honest diagnostic is not an optional-example defect. Generic verify success establishes identifier consistency, not assembly or necessity. |
| plaque-native-ejectisome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-causal-receipt.json; Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-causal.log; stdout SHA256 dc516d6ef3fa342c638df335b97de8ae4de12b60f9910f0eb3e1305d4856adf8 | supports | Exit0. Zero protein_examples; one GENE_OR_PROTEIN ejectisin node is NO_GENE_SYMBOLS. This honest diagnostic is not an optional-example defect. Generic verify success establishes identifier consistency, not assembly or necessity. |
| plaque-native-elg1_rfc_like_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-verify-receipt.json; Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-verify.log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Five reviewed protein_examples; five typed protein nodes are COVERED. Generic verify success establishes identifier consistency, not assembly or necessity. |
| plaque-native-elg1_rfc_like_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-causal-receipt.json; Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-causal.log; stdout SHA256 cb8359551acfa102a3c4984a50cf8f76ee180be1c9809dd6edf16b50c1432672 | supports | Exit0. Five reviewed protein_examples; five typed protein nodes are COVERED. Generic verify success establishes identifier consistency, not assembly or necessity. |
| plaque-native-elongator_holoenzyme_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-verify-receipt.json; Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-verify.log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Six reviewed protein_examples; six typed protein nodes are COVERED. Generic verify success establishes identifier consistency, not assembly or necessity. |
| plaque-native-elongator_holoenzyme_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-causal-receipt.json; Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-causal.log; stdout SHA256 29a516440ea13c22756b229da3ae60ec5478f31193cc9d8912c5317484dd5a63 | supports | Exit0. Six reviewed protein_examples; six typed protein nodes are COVERED. Generic verify success establishes identifier consistency, not assembly or necessity. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043231,GO:0031391,GO:0032991,GO:0061860,GO:0033588,GO:0140535,GO:1902494,GO:0002097; Complete eight-term response: GO0043231,0031391,0032991,0061860,0033588,0140535,1902494,0002097; definitions and typed children/relations, distinguishing is_a from capability; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/go.raw | supports | Current GO supports the native identities, protein-complex and functional hierarchy. GO0033588 still uses the older heterohexamer/two-heterotrimer wording; accurate quotation does not remove the source-supported stoichiometry conflict. |
| plaque-go-elg1-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031391/ancestors?relations=is_a; Complete GO0031391 ancestors restricted to is_a; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/go-elg1-ancestors.raw | supports | The exact is_a ancestor response supports Elg1 RFC-like class hierarchy; it is not evidence of direct parthood. |
| plaque-go-ejectisome-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ejectisome&amp;limit=25; Complete returned exact keyword query; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/go-ejectisome-search.raw | supports | No result in this exact bounded GO name query; this does not exhaust all ontology synonyms or establish global absence. The minted identity is retained. |
| plaque-tax-3027 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3027; Complete native ENA taxonomy response: exact ID, rank, name and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-3027.raw | supports | Cryptophyceae class identity/rank; not a claim every species has the same ejectisin system. |
| plaque-tax-3028 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3028; Complete native ENA taxonomy response: exact ID, rank, name and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-3028.raw | supports | Chroomonas genus identity/rank; not an exact strain or species accession. |
| plaque-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native ENA taxonomy response: exact ID, rank, name and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-4932.raw | supports | Saccharomyces cerevisiae species identity. |
| plaque-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native ENA taxonomy response: exact ID, rank, name and lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-559292.raw | supports | S. cerevisiae S288C reference strain identity, distinct from experimental W303, BS1173 or BSY2369 preparations. |
| plaque-pmid-21336864 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21336864+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-21336864.raw | supports | Rhiel and Westermann2012 primary abstract: discharged Chroomonas/Cryptomonas fragments and paracrystalline ultrastructure; no intact-organelle formation assay. |
| plaque-pmid-22868567 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22868567+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-22868567.raw | supports | Ammermann2013 primary abstract: small ejectisin polypeptides and a 20-residue N-terminal sequence correspondence; fragment reaggregation does not prove intact organelle formation. |
| plaque-pmid-14614842 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-14614842.raw | supports | Kim and MacNeill2003 secondary abstract only, RFC-like clamp-loader diversity context. |
| plaque-pmid-23499004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23499004+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-23499004.raw | supports | Kubota2013 primary abstract directly describes Elg1-dependent PCNA unloading, degron restoration and purified-complex unloading; full body/figures/Methods not inspected. |
| plaque-pmid-27664980 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27664980+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-27664980.raw | supports | Kupiec2016 secondary review abstract only; genome-stability and PCNA-unloading context, not a separately inspected primary experiment. |
| plaque-pmid-11435442 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11435442+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-11435442.raw | supports | Winkler2001 primary abstract identifies six polypeptide species and two labile subcomplexes; not an invariant absolute six-copy holoenzyme measurement. |
| plaque-pmid-11689709 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11689709+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-11689709.raw | supports | Krogan and Greenblatt2001 primary abstract and bibliographic identity; main-body evidence is separately bounded below. |
| plaque-pmid-15769872 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15769872+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-15769872.raw | supports | Huang2005 primary abstract identifies Elongator-dependent wobble-uridine modification; catalytic-output loss is not assembly-essentiality evidence. |
| plaque-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-14562095.raw | supports | Huh2003 primary abstract establishes the GFP localisation survey provenance; individual protein images were not inspected. |
| plaque-pmid-15780940 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15780940+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-15780940.raw | supports | Rahl2005 primary abstract concerns Elp1/Sec2 and polarised exocytosis, not measured full Elongator assembly. |
| plaque-pmid-10024884 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10024884+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-10024884.raw | supports | Otero1999 primary abstract identifies early Elongator/polII transcription association; later functional scope is not replaced by this initial association. |
| plaque-pmid-24750273 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24750273+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-24750273.raw | supports | DiSanto2014 primary abstract describes Elp1 tRNA-binding/basic-region function, not a universal nuclear-localisation requirement. |
| plaque-rhiel-publisher | https://link.springer.com/article/10.1007/s00709-011-0267-4; Springer page title/authors/DOI/abstract and access notice; no primary body or image pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/rhiel-publisher.raw | supports | Current genuine publisher landing page exposes abstract and bibliography, with subscription access limits. It is not full article access. |
| plaque-ammermann-publisher | https://link.springer.com/article/10.1007/s00709-012-0440-4; Springer page title/authors/DOI/abstract and access notice; full body not claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-publisher.raw | supports | Current genuine publisher landing page exposes the primary abstract and bibliography; full paper is not available through this route. |
| plaque-ammermann-web1 | https://www.researchgate.net/publication/230622947_Ejectisins_Tough_and_tiny_polypeptides_are_a_major_component_of_cryptophycean_ejectisomes; Web-reader extraction lines45–390: title/bibliography, Introduction and culture/initial Methods text; saved provider response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-web1.json; provider crawl age retained, no native HTTP success invented | supports | Author-distributed primary text was inspected through the web reader. Introductory membrane/resting-ribbon statements cite older studies and are secondary context within this paper; cultures are Chroomonas LT and Cryptomonas S2/LT. |
| plaque-ammermann-web2 | https://www.researchgate.net/publication/230622947_Ejectisins_Tough_and_tiny_polypeptides_are_a_major_component_of_cryptophycean_ejectisomes; Web-reader extraction lines387–1099: fragment purification/reconstitution, TEM and sequence Methods; Results and text captions; saved provider response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-web2.json; provider crawl age retained, no native HTTP success invented | supports | The experiments concern detergent/Percoll-enriched fragments and reconstituted ejectisin filaments. Antibody and preparation controls support that bounded scope; figure pixels and the complete later sequence-alignment discussion were not inspected. |
| plaque-PMC5286391-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5286391/; Genuine NCBI legacy HTML; sec0003/0004/0007, text captions Figs1/2A/6/EV1/EV2/EV5; Methods sec0010/0011/0017. No figure pixels, raw MS, supplementary strain TableEV4 or universal exact experimental S288C identity.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286391-legacy.raw | supports | Setiaputra2017 (online2016): native yeast Elongator has two Elp123 lobes and a majority single Elp456 hexameric ring. Elp1 deletion loses Elp2/3 association with FLAG-Elp4 while Elp456 persists; elp2 deletion retains other associations. Low-salt and added-ring conditions also allow double Elp456 loading, so fixed universal occupancy is unwarranted. |
| plaque-PMC5286394-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5286394/; Genuine NCBI legacy HTML; sec0003/0004/0005, figure1/2 and EV2–4 text captions, Methods sec0012/0013. Yeast BS1173/BSY2369, 27/31Å negative stain and glutaraldehyde stabilization; no pixels or raw reconstruction reanalysis.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286394-legacy.raw | supports | Dauden2017 (online2016) resolves two Elp123 copies with one asymmetrically bound Elp456 heterohexamer. Native yeast purification and negative-stain reconstructions support that preparation; recombinant E.coli is an expression host, not the natural record taxon. |
| plaque-PMC99985-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC99985/; Genuine NCBI legacy HTML; sec2/3 purification/strain Methods and Table1 W303-1A background; sec7/8 and Fig1/2 text captions. No individual image-pixel interpretation or uninspected phenotypic sections.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC99985-legacy.raw | supports | Krogan2001 identifies six distinct proteins with roughly equimolar recovery and separable Elp123/456 associations. This inventory is not an absolute one-copy-per-protein determination of the complete assembly. |
| plaque-PMC1370732-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1370732/; Genuine NCBI legacy HTML; sec7/8 with Fig4 text caption; Methods sec21 HPLC and sec22 UV crosslink/IP. No figure pixels or full strain Table2 inspection.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC1370732-legacy.raw | supports | Huang2005 deletion/rescue and tRNA-nucleoside measurements support Elongator-dependent mcm5/ncm5 wobble modifications. Elp1/3 tRNA co-IP supports association; catalytic-output loss is not automatically failure to form the full complex. |
| plaque-PMC5286391-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC5286391/?pdf=render; Actual retained transport response and adjacent receipt; HTTP200 Recaptcha for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286391-body.raw | context_only | This route supplied access-control/challenge content, not readable primary article text. Successful alternative routes, if any, are separate observations with their own scope and time. |
| plaque-PMC5286394-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC5286394/?pdf=render; Actual retained transport response and adjacent receipt; HTTP200 Recaptcha for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286394-body.raw | context_only | This route supplied access-control/challenge content, not readable primary article text. Successful alternative routes, if any, are separate observations with their own scope and time. |
| plaque-PMC99985-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC99985/?pdf=render; Actual retained transport response and adjacent receipt; HTTP200 Recaptcha for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC99985-body.raw | context_only | This route supplied access-control/challenge content, not readable primary article text. Successful alternative routes, if any, are separate observations with their own scope and time. |
| plaque-PMC1370732-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC1370732/?pdf=render; Actual retained transport response and adjacent receipt; HTTP200 Recaptcha for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC1370732-body.raw | context_only | This route supplied access-control/challenge content, not readable primary article text. Successful alternative routes, if any, are separate observations with their own scope and time. |
| plaque-kubota-publisher | https://www.cell.com/molecular-cell/fulltext/S1097-2765(13)00140-8; Actual retained transport response and adjacent receipt; HTTP200 Recaptcha for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/kubota-publisher.raw | context_only | This route supplied access-control/challenge content, not readable primary article text. Successful alternative routes, if any, are separate observations with their own scope and time. |
| plaque-ammermann-rg | https://www.researchgate.net/publication/230622947_Ejectisins_Tough_and_tiny_polypeptides_are_a_major_component_of_cryptophycean_ejectisomes; Actual retained transport response and adjacent receipt; HTTP200 Recaptcha for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-rg.raw | context_only | This route supplied access-control/challenge content, not readable primary article text. Successful alternative routes, if any, are separate observations with their own scope and time. |
| plaque-up-Q12050 | https://rest.uniprot.org/uniprotkb/Q12050.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q12050.raw | supports | Reviewed S288C tax559292 entry Q12050, exact locus YOR144C, matches the maintained ELG1 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELG1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELG1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELG1.raw | supports | The exact reviewed gene/taxon query returns one matching entry Q12050; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-P40348 | https://rest.uniprot.org/uniprotkb/P40348.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P40348.raw | supports | Reviewed S288C tax559292 entry P40348, exact locus YJR068W, matches the maintained RFC2 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-RFC2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC2.raw | supports | The exact reviewed gene/taxon query returns one matching entry P40348; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-P38629 | https://rest.uniprot.org/uniprotkb/P38629.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P38629.raw | supports | Reviewed S288C tax559292 entry P38629, exact locus YNL290W, matches the maintained RFC3 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-RFC3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC3.raw | supports | The exact reviewed gene/taxon query returns one matching entry P38629; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-P40339 | https://rest.uniprot.org/uniprotkb/P40339.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P40339.raw | supports | Reviewed S288C tax559292 entry P40339, exact locus YOL094C, matches the maintained RFC4 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-RFC4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC4.raw | supports | The exact reviewed gene/taxon query returns one matching entry P40339; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-P38251 | https://rest.uniprot.org/uniprotkb/P38251.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P38251.raw | supports | Reviewed S288C tax559292 entry P38251, exact locus YBR087W, matches the maintained RFC5 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-RFC5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC5.raw | supports | The exact reviewed gene/taxon query returns one matching entry P38251; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-Q06706 | https://rest.uniprot.org/uniprotkb/Q06706.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q06706.raw | supports | Reviewed S288C tax559292 entry Q06706, exact locus YLR384C, matches the maintained ELP1 instance. Primary name is IKI3 with ELP1 alias. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELP1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP1.raw | supports | The exact reviewed gene/taxon query returns one matching entry Q06706; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-P42935 | https://rest.uniprot.org/uniprotkb/P42935.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P42935.raw | supports | Reviewed S288C tax559292 entry P42935, exact locus YGR200C, matches the maintained ELP2 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELP2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP2.raw | supports | The exact reviewed gene/taxon query returns one matching entry P42935; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-Q02908 | https://rest.uniprot.org/uniprotkb/Q02908.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q02908.raw | supports | Reviewed S288C tax559292 entry Q02908, exact locus YPL086C, matches the maintained ELP3 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELP3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP3.raw | supports | The exact reviewed gene/taxon query returns one matching entry Q02908; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-Q02884 | https://rest.uniprot.org/uniprotkb/Q02884.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q02884.raw | supports | Reviewed S288C tax559292 entry Q02884, exact locus YPL101W, matches the maintained ELP4 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELP4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP4.raw | supports | The exact reviewed gene/taxon query returns one matching entry Q02884; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-P38874 | https://rest.uniprot.org/uniprotkb/P38874.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P38874.raw | supports | Reviewed S288C tax559292 entry P38874, exact locus YHR187W, matches the maintained ELP5 instance. Primary name is IKI1 with ELP5 alias. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELP5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP5.raw | supports | The exact reviewed gene/taxon query returns one matching entry P38874; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-up-Q04868 | https://rest.uniprot.org/uniprotkb/Q04868.json; Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus, comments and cross-references; reference strain is not silently equated with experimental strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q04868.raw | supports | Reviewed S288C tax559292 entry Q04868, exact locus YMR312W, matches the maintained ELP6 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and family cross-references were inspected; identity is not direct experimental assembly evidence. |
| plaque-gene-ELP6 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP6.raw | supports | The exact reviewed gene/taxon query returns one matching entry Q04868; primary name, alias and locus were read rather than inferred from search rank. |
| plaque-ipr-IPR006849 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006849/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR006849.raw | supports | Elp1 full-protein family, independently linked by Q06706. |
| plaque-ipr-IPR037289 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037289/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR037289.raw | supports | Elp2 full-protein family, independently linked by P42935. |
| plaque-ipr-IPR034687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034687/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR034687.raw | supports | Elp3-like full-protein family, independently linked by Q02908; homologous bacterial/archaeal proteins do not thereby become constituents of a yeast-type holoenzyme. |
| plaque-ipr-IPR008728 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008728/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR008728.raw | supports | Elp4 full-protein family, independently linked by Q02884. |
| plaque-ipr-IPR019519 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019519/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR019519.raw | supports | Elp5 full-protein family, independently linked by P38874. |
| plaque-ipr-IPR018627 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018627/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR018627.raw | supports | Elp6 full-protein family, independently linked by Q04868. |
| plaque-ipr-IPR039661 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039661/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR039661.raw | supports | Broader Elp3/YhcC grouping is distinguished from the more precise Elp3-like family. |
| plaque-ipr-IPR050238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR050238.raw | supports | Broad DNA replication/repair clamp-loader family is not a distinct RFC2,3,4 or5 class; its explicitly LLM-generated unchecked description was excluded. |
| plaque-ipr-IPR062598 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062598/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR062598.raw | supports | Elg1 middle domain, not a full-protein Elg1 family. |
| plaque-ipr-IPR062602 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062602/; Complete native InterPro metadata: accession/name/type, member signatures and available non-LLM description; cross-checked against individual UniProt membership where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR062602.raw | supports | Elg1 C-terminal domain2, not a full-protein Elg1 family. |
| plaque-ipr-search-ejectisin | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=ejectisin&amp;page_size=20; Exact native keyword route and actual response/receipt; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-search-ejectisin.raw | context_only | HTTP204 with empty body; exact ejectisin mapping remains unresolved, not globally disproved. |
| plaque-ipr-search-Elg1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=Elg1&amp;page_size=20; Exact native keyword route and actual response/receipt; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-search-Elg1.raw | context_only | HTTP429 access limitation: no current family-absence conclusion is drawn. Separately readable Elg1 domain metadata does not establish a full-class mapping. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete20 organism rows/28 organism-dataset pairs, independently reread from same-PR micro reviewer snapshot; retain actual retrieval timestamp; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/catalogue.raw | context_only | Complete current catalogue contains no Saccharomyces cerevisiae, cryptophyte, Chroomonas, Cryptomonas or Guillardia host entry. No matching downstream dataset was selected; recombinant E.coli expression is not a proxy for these natural hosts. |
| plaque-historical-micro53-rhiel-publisher | https://link.springer.com/article/10.1007/s00709-011-0267-4; Complete3038-byte native HTML access diagnostic. Historical observation carried from 20261022T062451Z-ejectisome-audit/micro53-rhiel-publisher; old time/hash retained; original raw transport snapshot not independently refetched as historical bytes. | context_only | HTTP200 returned a Client Challenge JavaScript page, not the article body. The original transport receipt is retained without upgrading readability. |
| plaque-historical-micro53-ammermann-publisher | https://link.springer.com/article/10.1007/s00709-012-0440-4; Complete3038-byte native HTML access diagnostic. Historical observation carried from 20261022T062451Z-ejectisome-audit/micro53-ammermann-publisher; old time/hash retained; original raw transport snapshot not independently refetched as historical bytes. | context_only | HTTP200 returned a Client Challenge JavaScript page, not the article body. The original transport receipt is retained without upgrading readability. |
| plaque-historical-micro53-kubota-publisher | https://doi.org/10.1016/j.molcel.2013.02.012; Original urllib exception response and request receipt. Historical observation carried from 20261022T062451Z-elg1-rfc-like-complex-audit/micro53-kubota-publisher; old time/hash retained; original raw transport snapshot not independently refetched as historical bytes. | context_only | The native DOI attempt failed with a TLS certificate-verification error and status0; no article body was obtained. The separate native MED abstract remains readable. |
| plaque-historical-micro53-kubota-browser | https://www.sciencedirect.com/science/article/pii/S1097276513001408; Browser diagnostic representation, status null, exact S1097276513001408 route. Historical observation carried from 20261022T062451Z-elg1-rfc-like-complex-audit/micro53-kubota-browser; old time/hash retained; original raw transport snapshot not independently refetched as historical bytes. | context_only | The exact ScienceDirect paper route also returned a browser403 diagnostic. No primary body, figure or Methods inspection is claimed. |
| plaque-historical-micro53-kupiec-publisher | https://academic.oup.com/femsyr/article/16/7/fow084/2399204; Retained403 response; no review body claim. Historical observation carried from 20261022T062451Z-elg1-rfc-like-complex-audit/micro53-kupiec-publisher; old time/hash retained; original raw transport snapshot not independently refetched as historical bytes. | context_only | The attempted publisher route returned HTTP403 challenge content. The Kupiec review is independently assessed only through its complete native abstract. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Complete scientific review and required structured-source applicability | supports | Positive molecular/pathway assertions require actual coverage assessment; absence of expression claims is insufficient. Official-source fallback must preserve actual dataset and runner scope. |
| septin-curation-policy | docs/CURATION.md; Exact component identities, scientific evidence and append-only Discussions | supports | Supported named constituents may be label-only when exact identity is unresolved; protein examples do not substitute for family grounding. Preserve historical rationale and append any current clarification. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Formation essentiality, Component, protein and graph schema | supports | Family/class components and appropriate complex nodes are allowed. Membership, transport activity, growth and formation necessity are different assertions. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native primary names, aliases, source taxa and independent verification | supports | Native accession/status/gene/strain and family joins require actual data; source and expression strains are not interchangeable. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Evidence-scoped graph edges | supports | Coarse contribution edges are permitted; source-attribution notes must accurately describe what the source establishes. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Actual source access and experimental scope | supports | Authority metadata, primary abstract and genuine primary body are distinct. Figure captions do not certify unseen pixels or supplements. |
| septin-review-schema | schema/record_review.yaml; Native finding and evidence contracts | supports | Inherited findings retain exact repository/review/finding lineage; a new source-attribution finding has no invented predecessor. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0002097,GO:0005784,GO:0005789,GO:0033588,GO:0042910,GO:0045048,GO:0072546,GO:0098796,GO:0140330,GO:0140535,GO:1902494,GO:1902495,GO:1990207,GO:1990281; Requested native terms: active status, names, definitions, synonyms and typed relation context; only assigned target relations used | supports | GO0072546 is EMC and its current definition still lists six older yeast member names; Bai independently establishes eight in the measured yeast preparation. GO1990207 is EmrE homodimer with generic bacterial distribution. GO1990281 is a broader efflux-pump class, not an exact EmrAB identity. GO0140330 describes outer-membrane export; GO0042910 and GO0045048 retain their process/function scope. Unrelated terms in the combined response are not reviewed targets. |
| septin-ncbifam-NF011715 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF011715/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Exact full EmrA periplasmic adaptor family, independently joined through P27303; shared hairpin/beta-barrel domains are not equivalent. |
| septin-ncbifam-NF000391 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF000391/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Exact EmrB permease family, independently joined through P0AEJ0. |
| septin-ipr-IPR004638 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004638/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Broader DHA2/EmrB-like family explicitly includes EmrB, FarB, TcmA and RibZ; this scope exceeds exact named EmrB. |
| septin-ipr-IPR058622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Exact TolC family with NF007002 signature and independent P02930 join; no correction required for this component. |
| septin-ncbifam-NF042984 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF042984/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Exact full EmrE family with independent P23895 join. |
| septin-ncbifam-NF007087 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF007087/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Broader EmrE family entry explicitly also matches a 77%-identical homolog that probably needs another name; not exact EmrE replacement. |
| septin-ipr-IPR045324 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045324/; Native name/type, signatures, hierarchy, curated description and provenance flags; no sequence alignment reanalysis | supports | Broad small multidrug resistance family includes distinct MdtI/MdtJ children; native description is not LLM generated. Family breadth does not prevent using a verified narrower exact entry. |
| septin-peer-protein-P36039 | https://rest.uniprot.org/uniprotkb/P36039.json; Native identity, primary gene, synonyms, ordered loci, taxon, status and complete relevant family xrefs | supports | Reviewed P36039: ER membrane protein complex subunit 3; primary EMC3; aliases ['AIM27']; loci ['YKL207W']; taxon 559292. Exact native family xrefs checked. Identity annotations are not new assembly experiments. Fresh current retrieval despite legacy filename prefix; S288c reference identity is not the W303-1a experimental strain. |
| septin-peer-protein-P40540 | https://rest.uniprot.org/uniprotkb/P40540.json; Native identity, primary gene, synonyms, ordered loci, taxon, status and complete relevant family xrefs | supports | Reviewed P40540: ER membrane protein complex subunit 5; primary EMC5; aliases ['KRE27']; loci ['YIL027C']; taxon 559292. Exact native family xrefs checked. Identity annotations are not new assembly experiments. Fresh current retrieval despite legacy filename prefix; S288c reference identity is not the W303-1a experimental strain. |
| septin-protein-P27303 | https://rest.uniprot.org/uniprotkb/P27303.json; Native identity, primary gene, synonyms, ordered loci, taxon, status and complete relevant family xrefs | supports | Reviewed P27303: Multidrug export protein EmrA; primary emrA; aliases []; loci ['b2685', 'JW2660']; taxon 83333. Exact native family xrefs checked. Identity annotations are not new assembly experiments. |
| septin-protein-P0AEJ0 | https://rest.uniprot.org/uniprotkb/P0AEJ0.json; Native identity, primary gene, synonyms, ordered loci, taxon, status and complete relevant family xrefs | supports | Reviewed P0AEJ0: Multidrug export protein EmrB; primary emrB; aliases []; loci ['b2686', 'JW2661']; taxon 83333. Exact native family xrefs checked. Identity annotations are not new assembly experiments. |
| septin-protein-P02930 | https://rest.uniprot.org/uniprotkb/P02930.json; Native identity, primary gene, synonyms, ordered loci, taxon, status and complete relevant family xrefs | supports | Reviewed P02930: Outer membrane protein TolC; primary tolC; aliases ['colE1-i', 'mtcB', 'mukA', 'refI', 'toc', 'weeA']; loci ['b3035', 'JW5503']; taxon 83333. Exact native family xrefs checked. Identity annotations are not new assembly experiments. |
| septin-protein-P23895 | https://rest.uniprot.org/uniprotkb/P23895.json; Native identity, primary gene, synonyms, ordered loci, taxon, status and complete relevant family xrefs | supports | Reviewed P23895: Multidrug transporter EmrE; primary emrE; aliases ['eb', 'mvrC']; loci ['b0543', 'JW0531']; taxon 83333. Exact native family xrefs checked. Identity annotations are not new assembly experiments. |
| septin-gene-emrA-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed entries and primary-name/identity joins | supports | One returned reviewed native entry P27303, with primary gene emrA, confirms the present bounded selection. No reconstruction of an unspecified past search. |
| septin-gene-emrB-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed entries and primary-name/identity joins | supports | One returned reviewed native entry P0AEJ0, with primary gene emrB, confirms the present bounded selection. No reconstruction of an unspecified past search. |
| septin-gene-tolC-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed entries and primary-name/identity joins | supports | One returned reviewed native entry P02930, with primary gene tolC, confirms the present bounded selection. No reconstruction of an unspecified past search. |
| septin-gene-emrE-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed entries and primary-name/identity joins | supports | One returned reviewed native entry P23895, with primary gene emrE, confirms the present bounded selection. No reconstruction of an unspecified past search. |
| septin-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete native ENA taxon response | supports | Taxon 2: Bacteria, rank domain. Species, reference strain and recombinant expression host remain distinguished. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native ENA taxon response | supports | Taxon 4932: Saccharomyces cerevisiae, rank species. Species, reference strain and recombinant expression host remain distinguished. |
| septin-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native ENA taxon response | supports | Taxon 562: Escherichia coli, rank species. Species, reference strain and recombinant expression host remain distinguished. |
| septin-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native ENA taxon response | supports | Taxon 83333: Escherichia coli K-12, rank strain. Species, reference strain and recombinant expression host remain distinguished. |
| septin-doi-science_aao3099 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.aao3099%22&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: The ER membrane protein complex is a transmembrane domain insertase. Authors: Guna A, Volkmar N, Christianson JC, Hegde RS. DOI 10.1126/science.aao3099. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. |
| septin-doi-j_cell_2018_10_009 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2018.10.009%22&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: EMC Is Required to Initiate Accurate Membrane Protein Topogenesis. Authors: Chitwood PJ, Juszkiewicz S, Guna A, Shao S, Hegde RS. DOI 10.1016/j.cell.2018.10.009. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. |
| septin-doi-s41586-020-2389-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-020-2389-3%22&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: Structure of the ER membrane complex, a transmembrane-domain insertase. Authors: Bai L, You Q, Feng X, Kovach A, Li H. DOI 10.1038/s41586-020-2389-3. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. |
| septin-doi-eLife_57887 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.57887%22&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: The architecture of EMC reveals a path for membrane protein insertion. Authors: O'Donnell JP, Phillips BP, Yagita Y, Juszkiewicz S, Wagner A, Malinverni D, Keenan RJ, Miller EA, Hegde RS. DOI 10.7554/elife.57887. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. |
| septin-pmid-12482849 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12482849+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: Identification of oligomerization and drug-binding domains of the membrane fusion protein EmrA. Authors: Borges-Walmsley MI, Beauchamp J, Kelly SM, Jumel K, Candlish D, Harding SE, Price NC, Walmsley AR. DOI 10.1074/jbc.m209457200. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. Borges-Walmsley2003 tests EmrA oligomerization/drug binding and proposes a trimeric model; it is not the modern whole-complex6:1:3 count source. |
| septin-pmid-33065135 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A33065135+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: Structural characterization of the EmrAB-TolC efflux complex from E. coli. Authors: Yousefian N, Ornik-Cha A, Poussard S, Decossas M, Berbon M, Daury L, Taveau JC, Dupuy JW, Đorđević-Marquardt S, Lambert O, Pos KM. DOI 10.1016/j.bbamem.2020.183488. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. Yousefian2021 abstract supports coexpression/purification and EM of native tripartite pump, 33nm and probable tip-to-tip canal; full body not obtained or certified in this review. |
| septin-pmid-41839863 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A41839863+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: A model for drug transport across two membranes of Gram-negative bacteria by an MFS tripartite assembly. Authors: Zhong Z, Maimaiti T, Jackson ML, Dong R, Gao X, Ouyang Q, Wang W, Guo J, Li S, Shang W, Liu H, Jiang H, Zhang S, Zachariae U, Luisi BF, Chao Y, Du D. DOI 10.1038/s41467-026-70500-5. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. |
| septin-pmid-18024586 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18024586+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete EuropePMC CORE metadata and primary abstractText | supports | Native exact citation: X-ray structure of EmrE supports dual topology model. Authors: Chen YJ, Pornillos O, Lieu S, Ma C, Chen AP, Chang G. DOI 10.1073/pnas.0709387104. Complete primary abstract read; bibliographic authority is not by itself full-body evidence. |
| septin-bai2020-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC7442705/; Genuine PMC7442705 body sections S2–S5 and S7 purification, associated main captions; no figure pixels or supplementary datasets | supports | Native yeast Emc5-FLAG purification in W303-1a plus mass spectrometry/cryo-EM establishes Emc1–6,Emc7,Emc10. Growth and client defects are distinct from assembly: Emc3 K26L mutant complex remains intact despite functional defects. Eight yeast constituents must not be replaced by old GO six-member text or mammalian composition. |
| septin-guna2018-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC5788257/; Genuine PMC5788257 unsectioned main scientific paragraphs and Figures1–4 captions, through conclusion before acknowledgments; no supplementary methods/data or pixels | supports | Selected moderately hydrophobic TA substrates such as SQS require EMC in U2OS/HEK assays; purified intact mammalian EMC in liposomes is sufficient for insertion. VAMP2/TRC40 contrasts bound scope. This is insertase activity, not individual yeast-subunit assembly necessity. |
| septin-chitwood2018-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC6269167/; Genuine PMC6269167 Results2.5–2.7 plus full native abstract; other results/methods and supplements not certified | supports | Sec61-depleted and purified EMC/SRP-receptor proteoliposomes support selected Nexo signal-anchor insertion. Beta1AR TMD1 and TMD2 distinguish sequential EMC/Sec61 roles. Not universal EMC dependence of every transmembrane segment. |
| septin-odonnell2020-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC7292650/; Genuine PMC7292650 main article Results2.4–2.6 with embedded captions and Methods4.7; no image pixels or supplement experiments independently reanalyzed | supports | Human EMC architecture combines native HEK293 purification, moderate6.5Angstrom map, docking/prediction and crosslinks. Vestibule and lipid-exposed groove provide a proposed insertion path requiring further tests, not a measured complete insertion trajectory or fixed yeast inventory. |
| septin-zhong2026-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC13139468/; Genuine PMC13139468 Sections3,4,6,8,11 and Methods14–17 with relevant main captions; Discussion12 inspected for proposed-model scope, not all supplements or pixels | supports | MG1655 genes expressed in engineered C43(DE3) delta-acrAB constructs yield EmrA6:EmrB1:TolC3. Pump-EA is assembled but inactive in resistance assays; pump-FA is active. Structural, omission/mutant resistance and everted-vesicle antiport experiments are distinguished. These measurements do not mean CPX labels each member assembly-essential; the supported complete-pump architecture and coupling remain intact. |
| septin-chen2007-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2141897/; Genuine PMC2141897 Results2–5 and7–8, Methods10/12 plus relevant main captions; no coordinate/raw-data or figure-pixel reanalysis | supports | Corrected TPP-bound EmrE structures and anomalous markers support antiparallel homodimer; acidic apo form is distorted and not the accepted transport conformation. Recombinant BL21(DE3)/cell-free expression and binding assays remain distinct from native K12 identity. No full kinetic transport cycle or all-SMR homodimer conclusion. |
| septin-complex-CPX-4268 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4268; Complete object including functions/properties, all three participants/stoichiometries/bioRoles, complexAssemblies, xrefs and evidenceType | supports | Native K12 EmrAB-TolC identity; six EmrA P27303,one EmrB P0AEJ0,three TolC P02930; heterodecamer. Participant bioRoles are unspecified; evidenceType ECO0005547 is inferred by curator. No participant essentiality classification is present in this complete response. Native systematicName retains an older short notation and is not used instead of explicit participant counts. |
| septin-eco0005547 | https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FECO_0005547; Native ECO identity/definition response | supports | ECO0005547 is inferred by curator, not an experimental assembly-necessity assay. |
| septin-pdb-8ZAL-entry | https://data.rcsb.org/rest/v1/core/entry/8ZAL; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | Entry is engineered pump-EA; EM entry with ten deposited protein instances and Zhong2026 citation. Source body, not mere entry title, supplies functional limitations. |
| septin-pdb-8ZAL-assembly | https://data.rcsb.org/rest/v1/core/assembly/8ZAL/1; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | Author/software assembly1 is a heterodecamer with ten protein instances; no essentiality field is inferred. |
| septin-pdb-8ZAL-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/8ZAL/1; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | EmrA chainsA–F map to P27303; model omits the native N-terminal region and comes from engineered EA. |
| septin-pdb-8ZAL-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/8ZAL/2; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | TolC chainsG–I map to P02930; native biological K12 differs from expression E.coliB. |
| septin-pdb-8ZAL-entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/8ZAL/3; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | EmrB chainJ maps to P0AEJ0; biological K12 and expression E.coliB are distinct. |
| septin-pdb-3B5D-entry | https://data.rcsb.org/rest/v1/core/entry/3B5D; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | Entry is TPP-bound C2 EmrE structure,Chen2007,3.8Angstrom; not the distorted apo form. |
| septin-pdb-3B5D-assembly | https://data.rcsb.org/rest/v1/core/assembly/3B5D/1; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | Author-defined assembly1 is dimeric with two protein instances. |
| septin-pdb-3B5D-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/3B5D/1; Actual RCSB entry/assembly/entity metadata and native accession/source-host joins; no coordinate reanalysis | supports | ChainsA/B both map to P23895; source K12 and expression BL21(DE3) differ. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete20-organism official catalogue independently read | supports | E.coli covered; no yeast or human row. Other eukaryotic/microbial hosts are not substituted. Coverage is not biological presence or absence. |
| septin-adapter-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete precise1k metadata and strain list | supports | E.coli precise1k advertises BW25113,DGF-298,GMOS,MG1655,W3110,201 modules and1035samples. It supports reference-host context, not C43(DE3)delta-acrAB,BL21 or every primary assay. |
| septin-adapter-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 module identities/names/regulators/categories; no generated summaries/activity traces | supports | Native SoxS22 and ROS TALE Amp9 are bounded expression-context annotations. Dataset coverage does not establish structural membership, topology or formation necessity. |
| septin-modulegene-emrA | https://imodulondb.org/api/genes/e_coli/precise1k/b2685; Exact gene_id/gene_name/product/UniProt identity join | supports | Dataset locus b2685 maps emrA to the independently verified accession; imported function prose is not a separately read primary paper. |
| septin-modulemembers-emrA | https://imodulondb.org/api/genes/e_coli/precise1k/b2685/imodulons; Complete201 threshold/weight/membership rows | supports | Thresholded hits: none. False flags do not imply absent expression,gene or structural role; positive hits do not establish assembly. |
| septin-modulegene-emrB | https://imodulondb.org/api/genes/e_coli/precise1k/b2686; Exact gene_id/gene_name/product/UniProt identity join | supports | Dataset locus b2686 maps emrB to the independently verified accession; imported function prose is not a separately read primary paper. |
| septin-modulemembers-emrB | https://imodulondb.org/api/genes/e_coli/precise1k/b2686/imodulons; Complete201 threshold/weight/membership rows | supports | Thresholded hits: none. False flags do not imply absent expression,gene or structural role; positive hits do not establish assembly. |
| septin-modulegene-tolC | https://imodulondb.org/api/genes/e_coli/precise1k/b3035; Exact gene_id/gene_name/product/UniProt identity join | supports | Dataset locus b3035 maps tolC to the independently verified accession; imported function prose is not a separately read primary paper. |
| septin-modulemembers-tolC | https://imodulondb.org/api/genes/e_coli/precise1k/b3035/imodulons; Complete201 threshold/weight/membership rows | supports | Thresholded hits: 22 SoxS. False flags do not imply absent expression,gene or structural role; positive hits do not establish assembly. |
| septin-modulegene-emrE | https://imodulondb.org/api/genes/e_coli/precise1k/b0543; Exact gene_id/gene_name/product/UniProt identity join | supports | Dataset locus b0543 maps emrE to the independently verified accession; imported function prose is not a separately read primary paper. |
| septin-modulemembers-emrE | https://imodulondb.org/api/genes/e_coli/precise1k/b0543/imodulons; Complete201 threshold/weight/membership rows | supports | Thresholded hits: 9 ROS TALE Amp. False flags do not imply absent expression,gene or structural role; positive hits do not establish assembly. |
| septin-module-9 | https://imodulondb.org/api/imodulons/e_coli/precise1k/9; Native module metadata/threshold/category/regulator fields; ai_summary excluded | supports | Module 9 has 9 thresholded genes; emrE matches the native gene-membership endpoint. Expression clustering is not physical complex evidence. |
| septin-module-9-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/9/genes; Complete9 member IDs and focal emrE row/weight/accession; no imported prose promoted to primary evidence | supports | Independent member list confirms emrE; emrE weight0.284604907 exceeds0.109226946 for9, tolC0.033449641 exceeds0.030026006 for22. No condition/activity or causal interpretation is added. |
| septin-module-22 | https://imodulondb.org/api/imodulons/e_coli/precise1k/22; Native module metadata/threshold/category/regulator fields; ai_summary excluded | supports | Module 22 has 117 thresholded genes; tolC matches the native gene-membership endpoint. Expression clustering is not physical complex evidence. |
| septin-module-22-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes; Complete117 member IDs and focal tolC row/weight/accession; no imported prose promoted to primary evidence | supports | Independent member list confirms tolC; emrE weight0.284604907 exceeds0.109226946 for9, tolC0.033449641 exceeds0.030026006 for22. No condition/activity or causal interpretation is added. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical Nov3 00:49Z invocation receipt | context_only | Actual prior exit1 PermissionError reading pyvenv.cfg; no current invocation/success is claimed. Current official-source fallback separately evidenced. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-septin/original-checks.json; Actual original validate/render commands and all39 historical input occurrences | supports | Three original pairs validate/render0 with exact Markdown. All historical inputs match; EmrAB current target changed by four edges/history, while EMC/EmrE remain unchanged. Historical corpus checks are not current-head CI. |
| septin-emrab-stale-diff | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-septin/emrab-stale.diff; Exact old frozen-source to current-source target diff | context_only | Four new contributions/outer-export edges plus curation history substantively reassessed. New CPX essentiality-attribution concern is not assigned an invented old occurrence. |
| septin-record-emc_complex | data/structures/other/emc_complex.yaml; Complete current frozen record,all fields and history | context_only | Every current field independently reviewed; dated rationale is retained as provenance,with corrections appended when warranted. |
| septin-original-emc_complex | reviews/structured/20261022T062453Z-emc-complex-audit/review.yaml; Complete original YAML and exact deterministic Markdown | context_only | Original scientific findings/actions/scopes and historical hashes inspected; original files remain immutable. |
| septin-native-emc_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-verify-receipt.json; Actual command/head/time and complete log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 0 actual protein examples; zero typed protein nodes,so exit0 is an empty-inventory check rather than constituent coverage. |
| septin-native-emc_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-causal-receipt.json; Actual command/head/time and complete log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | 0 actual protein examples; zero typed protein nodes,so exit0 is an empty-inventory check rather than constituent coverage. |
| septin-record-emrab_tolc_multidrug_efflux_transport_complex | data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml; Complete current frozen record,all fields and history | context_only | Every current field independently reviewed; dated rationale is retained as provenance,with corrections appended when warranted. |
| septin-original-emrab_tolc_multidrug_efflux_transport_complex | reviews/structured/20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml; Complete original YAML and exact deterministic Markdown | context_only | Original scientific findings/actions/scopes and historical hashes inspected; original files remain immutable. |
| septin-native-emrab_tolc_multidrug_efflux_transport_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify-receipt.json; Actual command/head/time and complete log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 3 actual protein examples; 3 typed nodes,all COVERED; identity/coverage does not independently establish membership or necessity. |
| septin-native-emrab_tolc_multidrug_efflux_transport_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal-receipt.json; Actual command/head/time and complete log SHA256 470e07d0a056cc012469c5825c184baff91f5d1a6fc33adc4c368013cc58f268 | supports | 3 actual protein examples; 3 typed nodes,all COVERED; identity/coverage does not independently establish membership or necessity. |
| septin-record-emre_multidrug_transporter_complex | data/structures/other/emre_multidrug_transporter_complex.yaml; Complete current frozen record,all fields and history | context_only | Every current field independently reviewed; dated rationale is retained as provenance,with corrections appended when warranted. |
| septin-original-emre_multidrug_transporter_complex | reviews/structured/20261022T062455Z-emre-multidrug-transporter-complex-audit/review.yaml; Complete original YAML and exact deterministic Markdown | context_only | Original scientific findings/actions/scopes and historical hashes inspected; original files remain immutable. |
| septin-native-emre_multidrug_transporter_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-verify-receipt.json; Actual command/head/time and complete log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 1 actual protein examples; 1 typed nodes,all COVERED; identity/coverage does not independently establish membership or necessity. |
| septin-native-emre_multidrug_transporter_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-causal-receipt.json; Actual command/head/time and complete log SHA256 0ba2585e9162a17ba8731cba84e13eb7e577ea344263773afa6c906b12c8e38c | supports | 1 actual protein examples; 1 typed nodes,all COVERED; identity/coverage does not independently establish membership or necessity. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2390 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-dsl1_nzr_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dsl1_nzr_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dubm_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dubm_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dxr_protein_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dxr_protein_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-eisosome-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-eisosome-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ejectisome-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ejectisome-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-elg1_rfc_like_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-elg1_rfc_like_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-elongator_holoenzyme_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-elongator_holoenzyme_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emc_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emc_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emre_multidrug_transporter_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emre_multidrug_transporter_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Own scientific scope is the four complete Dsl1/NZR, DUBm, Dxr and eisosome records only. Eisosome is the sole stale own target; the other three current hashes are unchanged. Two additional frozen eisosome neighbors establish boundaries; frozen Elongator and EmrAB records are used only for separate auxiliary challenges, not own-slice dispositions.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Dsl1: fresh Tripathi genuine primary JATS read at declared Introduction/Results/Methods and Figure4-caption scopes, without images/supplements. Meiringer and Kraynack fresh complete abstracts only; current body routes failed/challenged and no new body-specific certification is made. Bounded purified bridge evidence does not force global ESSENTIAL.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: DUBm: fresh Wang and Adamus genuine primary bodies read at declared main-text/method/caption extents. Different purification strains, apo/nucleosome-bound maps, minimal Ub-AMC substrate and low-resolution SLIK/SAGA architecture remain distinct. Henry and localization/association studies are complete indexed abstracts/native annotations only; individual supplement data and every localization experiment were not reanalyzed.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Dxr: primary article remains complete indexed abstract plus genuine RCSB entry/polymer/assembly/ligand metadata. Coordinates/full article were not inspected. Source species, recombinant BL21(DE3) expression and K12 reference annotation differ. Substrate stereoisomer caveat and two protein copies remain bounded to the deposition.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Eisosome: fresh Walther main paragraphs0–17 and text captions, Karotki/Olivera declared primary body sections and methods were read. No pixels, movies, supplements or exhaustive fungal survey. Native Pil1/Lsp1 heterodimer versus mixed-homodimer organization remains unresolved; no universal endocytosis or complete assembly pathway is claimed. Moreira and Douglas remain indexed abstracts, Douglas explicitly secondary.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Protein authority annotations and current reviewed exact-gene queries do not certify every linked primary experiment or reconstruct historical query results. Broad family/domain candidates are not exact whole-protein mappings. InterPro IPR050185 LLM-flagged description is excluded as biological support; only its native broad identity/type informs the bounded non-mapping.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Fresh official catalogue includes no matched yeast dataset. E.coli precise1k has five stated strains; exact b0173 is joined to P45568 and checked across201 modules, with one UC-2/167 hit corroborated by96-member metadata/identity rows. Unknown module function, nonhits and expression membership are not assembly, direct regulation, essentiality or biological absence. Activity vectors and AI summaries are unused.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Historical adapter unavailability is the actual Nov3 00:49Z receipt, not a fresh execution. The retained Douglas403 observation preserves its original Oct21 time/hash and corrects only its kind. Present failed routes and successful indexed/body sources are separated. A default50-row gene page and misrouted app HTML were not treated as complete dataset evidence.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: Eight current native protein commands actually pass for11 reviewed examples and10 COVERED typed protein nodes. Eight original native validate/render commands and56 historical input occurrences also pass. Root owns global QC, successor save, post-save checks, final CI and merge queue; none of those future gates is precertified here.
- Dsl1/NZR, DUBm, Dxr and eisosome independent review: All three inherited findings remain minor/open with exact repository/review/finding lineage. No new own scientific finding, invented predecessor, forced optional example, record mutation, history rewrite, neighbor/group closure or status promotion is introduced.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Rhiel2012 and Kubota2013 are assessed at native complete abstract/metadata tier; current Springer landings are abstract/paywall pages and Kubota body retrieval is blocked. Kim/MacNeill2003 and Kupiec2016 are secondary abstract context only.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Ammermann author text was read through saved web-reader extractions with actual observation times and provider crawl metadata; no native HTTP200 body success is invented. Bounded Methods/Results concern discharged fragments and reconstituted filaments. Introduction citations for intact resting organelles are secondary context. No image pixels or complete later sequence alignment were inspected.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Setiaputra and Dauden selected genuine main-body Results/Methods and text captions were read. No figure pixels, raw EM/MS reanalysis or Setiaputra supplementary strain TableEV4 was inspected. Dauden and Krogan experimental strain identities are separate from S288C reference examples.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Huang tRNA-modification loss is a functional phenotype, not direct full-complex formation evidence. The Elp1 association finding is restricted to the observed deletion/pull-down condition; it does not mandate a universal essentiality enum or all-six-subunit necessity.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Exact ejectisin family remains unresolved after one bounded empty native query; Elg1 keyword query was HTTP429-limited, and separately verified domains are not full-class groundings. Generated unchecked InterPro IPR050238 prose was excluded. These limits are not global negative biology or mandatory optional protein-example findings.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Current official catalogue fallback is independent of the historical structured-runner failure at2026-11-03 00:49Z. No fresh runner success/failure is claimed. No matching natural host was found in the complete catalogue and no foreign-host module proxy was used; this does not establish biological absence.
- Ejectisome, Elg1 RFC-like and Elongator independent review: Five corrected historical transport rows retain old timestamps/hashes and honest context_only scope. Their original raw transport bytes were not reconstructed; this report binds the immutable original YAML carrying those observations and distinguishes current retrievable sources.
- Ejectisome, Elg1 RFC-like and Elongator independent review: No maintained local image was present for the three targets. Source captions/abstracts do not certify image pixels. This slice does not certify parent-owned corpus checks, final CI, queue admission, merge or cleanup.
- EMC, EmrAB-TolC and EmrE independent review: Three records: EMC/EmrE unchanged,EmrAB stale four-edge/history addition substantively refreshed. Four inherited minor findings and one new localized minor CPX-attribution finding remain open; all three need curation. Three original formal applicability exclusions require successor correction. No own access-kind misclassification established after inspecting all original evidence rows.
- EMC, EmrAB-TolC and EmrE independent review: Genuine Bai,Guna,Chitwood,O'Donnell,Zhong and Chen bodies were freshly retrieved and read only at exact stated sections/captions. No figure pixels,raw structural data or unread supplementary experiments certified. Borges-Walmsley2003 and Yousefian2021 limited to complete primary abstracts and exact metadata; unavailable full-body scope is not a refutation.
- EMC, EmrAB-TolC and EmrE independent review: Yeast Bai preparation is W303-1a; native EMC alias reference is S288c; human HEK/U2OS insertion evidence remains comparative. Preserve older rationale,append current alias clarification,do not substitute mammalian constituents or infer assembly necessity from growth/function. Native old GO six-member text is not used to override eight experimentally isolated yeast subunits.
- EMC, EmrAB-TolC and EmrE independent review: Zhong2026 gene sourceMG1655 differs from engineered C43(DE3)delta-acrAB expression/assays;8ZAL is pump-EA,assembled but inactive in resistance tests,while FA provides separate activity context. CPX participant roles are unspecified and its evidence is curator inference. New attribution correction does not deny defining membership or impose blanket changes to older ESSENTIAL flags.
- EMC, EmrAB-TolC and EmrE independent review: Chen2007 correctedTPP-bound structure is distinct from distorted acidic apo/defunct prior structures. BiologicalK12 differs fromBL21(DE3)/cell-free expression;2:1 protein:drug binding differs from two-subunit assembly. No all-SMR or fully resolved transport-cycle claim.
- EMC, EmrAB-TolC and EmrE independent review: Fresh complete official catalogue has no yeast/human host. Matched E.coli precise1k advertises five strains,not all experimental hosts. Four exact loci independently checked across201 modules; tolC inSoxS22 andemrE inROS TALE Amp9 confirmed by member endpoints. emrA/emrB false flags are not biological absence. AI module summaries,activity traces and imported functional prose are not primary evidence.
- EMC, EmrAB-TolC and EmrE independent review: Historical runner unavailable receipt is actualNov3 00:49Z; no fresh invocation claimed. Shared current catalogue/meta/module packet keeps actualNov4 access times and independent read scope. Own fresh retrievals are distinct from original immutable review provenance.
- EMC, EmrAB-TolC and EmrE independent review: Actual six native protein commands exit0: EMC0examples/0typed nodes (empty coverage),EmrAB3reviewed examples/3COVERED nodes,EmrE1reviewed/1COVERED. Native identity/coverage is not independent experimental membership/necessity proof. Three originals validate/render exactly and39 historical input occurrences match. Root corpus gates,successor/finalheadCI and merge attestations are separate.
- EMC, EmrAB-TolC and EmrE independent review: Only26 listed frozen maintained inputs used; two other reviewer neighbors in final49-input manifest were not used here. No record,original bundle,Git or GitHub mutation. Source-locality notes do not claim exhaustive absence across the literature.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All 49 maintained inputs were frozen before substantive use, including two neighboring eisosome records consulted only to assess boundaries. The original twenty artifacts remain immutable and traceable; the ten current record hashes are frozen separately from their historical review inputs.
- Two stale targets are refreshed: eisosome gained a Pil1/Lsp1 family grounding and PROTEIN_COMPLEX classification; EmrAB-TolC gained four causal edges and history. Current source and neighboring-boundary assessment supports the eisosome refresh without an enum-only defect. The EmrAB contribution edges remain supported while three new CPX evidence notes overstate the authority's essentiality annotation.
- Ten inherited scientific findings remain open: Dsl1/NZR two minor, DUBm one minor, Elongator one major and two minor, EMC two minor, EmrAB-TolC one minor and EmrE one minor. The new CPX attribution finding is minor. Dxr, eisosome, ejectisome and Elg1 RFC-like retain qualified passes. All scientific curation stays in separate issues.
- Formation findings preserve experimental scope: purified Dsl1 bridging and Elp1-dependent co-purification are not universal organismal essentiality claims; a global UNKNOWN may remain with explicit tested association evidence. Elongator subunit identities and state-dependent copy numbers are distinguished. Dated rationale and history are preserved rather than overwritten.
- Actual native protein checks cover 26 represented examples and 26 typed nodes: 25 COVERED and one ejectisin NO_GENE_SYMBOLS diagnostic. These command outcomes do not themselves establish scientific membership, exact family scope or formation necessity.
- Deduplication inspected all 377 open issue titles and full bodies and 103 bounded open title/body/comment searches for the ten current record labels, IDs, paths, stems, inherited keys, genes, families and review-evidence identities. The 19 related open issue bodies match already inspected accepted payloads; complete comment collections are empty. Issues #2626 and #2627 concern MCC and plasma membrane records; #2838–#2839 and #2850–#2854 concern AcrAB/AcrAD/AcrEF-TolC records; #2842–#2849 match shared footer terms for unrelated records; #2897 and #2927 concern Ctf18-RFC and canonical RFC. Those distinct maintained owners are not duplicates of this cohort. Closed historical eisosome issues #2432 and #2462 and their complete comments were inspected as provenance, without reopening them. Existing resolver issue #2514 and all 27 comments were inspected or verified byte-identical to prior read text and are reused. No matching open same-record/finding issue was found within this scope.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T081641Z-pr2390-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2390: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T07:55:05.450748Z'
finished_at: '2026-11-04T08:16:41Z'
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
summary: All ten records reassessed against current main; two stale reviews (eisosome
  and EmrAB-TolC) substantively refreshed. Ten inherited scientific findings are retained
  with current source scope, and one new minor EmrAB-TolC CPX attribution finding
  is filed separately. Seven formal and three prose structured-source applicability
  exclusions and six access-only evidence kinds are corrected in this linked successor.
  No scientific record or original review artifact is changed.
source:
  git_revision: 6d564c8d647868414ddf025c64068d9ac990abc8
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
  - path: data/structures/cytoskeleton/eisosome_filament.yaml
    sha256: 0a59cc075da50578f12a4950252cb8f7133ba55c99703a0843bf3f8651e366c0
    role: context
  - path: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
    sha256: cf0490c93ccba7b66f5f9fc3f6e108981620ba71eb7635fb3c7582dd7dfb1a1f
    role: context
  - path: data/structures/other/dsl1_nzr_complex.yaml
    sha256: 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0
    role: target
  - path: data/structures/other/dubm_complex.yaml
    sha256: 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591
    role: target
  - path: data/structures/other/dxr_protein_complex.yaml
    sha256: 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e
    role: target
  - path: data/structures/other/eisosome.yaml
    sha256: 3f96297240ba46e169dab4e79338949cf92ac200ffd75c509938b12240b1b89c
    role: target
  - path: data/structures/other/ejectisome.yaml
    sha256: 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8
    role: target
  - path: data/structures/other/elg1_rfc_like_complex.yaml
    sha256: 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837
    role: target
  - path: data/structures/other/elongator_holoenzyme_complex.yaml
    sha256: 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d
    role: target
  - path: data/structures/other/emc_complex.yaml
    sha256: 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54
    role: target
  - path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    sha256: 2ecd59317bfeae525a312c7ba1427b4ad561dfb25b621ff647b42e2205c150d6
    role: target
  - path: data/structures/other/emre_multidrug_transporter_complex.yaml
    sha256: 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0
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
  - path: reviews/structured/20261022T062447Z-dsl1-nzr-complex-audit/review.md
    sha256: 8ad0ed38251873f185e28fc406c4b0182f44abe122d228b6eab5095ba969e1a1
    role: context
  - path: reviews/structured/20261022T062447Z-dsl1-nzr-complex-audit/review.yaml
    sha256: b3e24dbf5ee127c2c3debd8e36d6e700306769b174374ed4e10d733c5096f473
    role: context
  - path: reviews/structured/20261022T062448Z-dubm-complex-audit/review.md
    sha256: ee0f5fa3bb21a943867283510d296b7e26fcac456ca6ac8ae736349b50c75296
    role: context
  - path: reviews/structured/20261022T062448Z-dubm-complex-audit/review.yaml
    sha256: 83feeddf50b6f9e216eeea13d49bcbd8aea883bf6358d222c7332931e0030e06
    role: context
  - path: reviews/structured/20261022T062449Z-dxr-protein-complex-audit/review.md
    sha256: faf91e6ed0eb320200d08bcee4b61b5448985aad028d2325caf5a70f1cbbe0e4
    role: context
  - path: reviews/structured/20261022T062449Z-dxr-protein-complex-audit/review.yaml
    sha256: 5b4a43814269c2a28e95e685aac9442e063b06c73a0a1e250ae9eb131bbbfdde
    role: context
  - path: reviews/structured/20261022T062450Z-eisosome-audit/review.md
    sha256: 260fc083f99a207e804c3d5092f44a8854871184f774694189841d507d321bf9
    role: context
  - path: reviews/structured/20261022T062450Z-eisosome-audit/review.yaml
    sha256: d4d070ac50b8017da55afd07474aea922d3e4de1e6c07dacfc748d348700ab94
    role: context
  - path: reviews/structured/20261022T062451Z-ejectisome-audit/review.md
    sha256: 136edde8922d26807cfee2ccf559c82db670d90bc1c99c75e2a8af7e51fc753f
    role: context
  - path: reviews/structured/20261022T062451Z-ejectisome-audit/review.yaml
    sha256: da8eef14b223c9cc319915c9a36cba41c42f0ddc25567f6ad3de77748df1d224
    role: context
  - path: reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.md
    sha256: 61ee1112cfb7ddbf12dffe77bfdf5118b87b1f149a70410a505feb0703a13acb
    role: context
  - path: reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.yaml
    sha256: 2898cc2d84349c73ed45e709954187c571d78a453216ca5bf959d2c4cf75bd9e
    role: context
  - path: reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.md
    sha256: cdad4b630c21247468aefd0792344bea501bd06ae9cbc64c5fefd557cc730a16
    role: context
  - path: reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.yaml
    sha256: 54f6e4272ddcc3727da6820b7a4db4dbc4ac842c8e43f78bb8974ac8c5c6d3de
    role: context
  - path: reviews/structured/20261022T062453Z-emc-complex-audit/review.md
    sha256: 9ec803c8faf55a943e6a9b4cd5ffd991edbfd855f1d2e593fb74fe0af239c293
    role: context
  - path: reviews/structured/20261022T062453Z-emc-complex-audit/review.yaml
    sha256: 51a8529eb2eabe5bb7c7305dc18975bebe0de1c23f7c66b09b4743cd344bf9f1
    role: context
  - path: reviews/structured/20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit/review.md
    sha256: 712256d26d1edc8a0c379977d0f94f5a8691b3bbff7021729a7dc425795b4663
    role: context
  - path: reviews/structured/20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml
    sha256: 22bc7fe7167e8a7cd3913e0a30fa883d9572ed33df3d51bb9faa241d333162a9
    role: context
  - path: reviews/structured/20261022T062455Z-emre-multidrug-transporter-complex-audit/review.md
    sha256: 39cb17546fe7db724a03e0e1795eef50538d2cdb4d3fc84062c12c0c23db0920
    role: context
  - path: reviews/structured/20261022T062455Z-emre-multidrug-transporter-complex-audit/review.yaml
    sha256: 5b0e8d7e997bb78f75aa39cdd58ee292e45f99c2ed2b7cb918ee2f7a0e1c6efb
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
- target_id: GO:0070939
  path: data/structures/other/dsl1_nzr_complex.yaml
  label: Dsl1/NZR complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
- target_id: GO:0071819
  path: data/structures/other/dubm_complex.yaml
  label: DUBm complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dubm_complex.yaml
    role: maintained scientific record
- target_id: GO:1990065
  path: data/structures/other/dxr_protein_complex.yaml
  label: Dxr protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dxr_protein_complex.yaml
    role: maintained scientific record
- target_id: GO:0032126
  path: data/structures/other/eisosome.yaml
  label: eisosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/eisosome.yaml
    role: maintained scientific record
- target_id: cellstructuremech:ejectisome
  path: data/structures/other/ejectisome.yaml
  label: ejectisome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ejectisome.yaml
    role: maintained scientific record
- target_id: GO:0031391
  path: data/structures/other/elg1_rfc_like_complex.yaml
  label: Elg1 RFC-like complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elg1_rfc_like_complex.yaml
    role: maintained scientific record
- target_id: GO:0033588
  path: data/structures/other/elongator_holoenzyme_complex.yaml
  label: elongator holoenzyme complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
- target_id: GO:0072546
  path: data/structures/other/emc_complex.yaml
  label: EMC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emc_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
  label: EmrAB-TolC multidrug efflux transport complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
- target_id: GO:1990207
  path: data/structures/other/emre_multidrug_transporter_complex.yaml
  label: EmrE multidrug transporter complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emre_multidrug_transporter_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    9ec44ab9323f1ebe881d7de8f25276ac75e78b88.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 6d564c8d647868414ddf025c64068d9ac990abc8.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 6d564c8d647868414ddf025c64068d9ac990abc8.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 6d564c8d647868414ddf025c64068d9ac990abc8.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 6d564c8d647868414ddf025c64068d9ac990abc8.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 6d564c8d647868414ddf025c64068d9ac990abc8.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0070939
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: just validate data/structures/other/dsl1_nzr_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0070939
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: just validate-strict data/structures/other/dsl1_nzr_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0071819
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just validate data/structures/other/dubm_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0071819
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just validate-strict data/structures/other/dubm_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:1990065
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just validate data/structures/other/dxr_protein_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:1990065
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: just validate-strict data/structures/other/dxr_protein_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0032126
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: just validate data/structures/other/eisosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0032126
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: just validate-strict data/structures/other/eisosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate cellstructuremech:ejectisome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ejectisome
  command: just validate data/structures/other/ejectisome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict cellstructuremech:ejectisome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ejectisome
  command: just validate-strict data/structures/other/ejectisome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0031391
  status: passed
  required: true
  target_ids:
  - GO:0031391
  command: just validate data/structures/other/elg1_rfc_like_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0031391
  status: passed
  required: true
  target_ids:
  - GO:0031391
  command: just validate-strict data/structures/other/elg1_rfc_like_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0033588
  status: passed
  required: true
  target_ids:
  - GO:0033588
  command: just validate data/structures/other/elongator_holoenzyme_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0033588
  status: passed
  required: true
  target_ids:
  - GO:0033588
  command: just validate-strict data/structures/other/elongator_holoenzyme_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0072546
  status: passed
  required: true
  target_ids:
  - GO:0072546
  command: just validate data/structures/other/emc_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0072546
  status: passed
  required: true
  target_ids:
  - GO:0072546
  command: just validate-strict data/structures/other/emc_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  command: just validate data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  command: just validate-strict data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:1990207
  status: passed
  required: true
  target_ids:
  - GO:1990207
  command: just validate data/structures/other/emre_multidrug_transporter_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:1990207
  status: passed
  required: true
  target_ids:
  - GO:1990207
  command: just validate-strict data/structures/other/emre_multidrug_transporter_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390
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
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  summary: All ten records have positive molecular triggers. Fresh complete official
    catalogue coverage is assessed against actual natural/reference hosts. Yeast and
    cryptophycean hosts are not covered; unrelated hosts are not proxies. Matched
    E. coli precise1k metadata and bounded gene/module endpoints provide Dxr UC-2/167,
    TolC SoxS/22 and EmrE ROS TALE Amp/9 context. EmrA/EmrB nonhits are not absence
    evidence. Five advertised strains do not cover every engineered expression host,
    and module membership does not establish complex assembly, direct regulation or
    essentiality. Historical runner unavailability is retained separately from current
    direct-source fallback.
  evidence_ids:
  - micro-access-adapter-genes
  - micro-catalogue
  - micro-adapter-meta
  - micro-adapter-modules
  - micro-adapter-dxr-memberships
  - micro-adapter-gene-dxr
  - micro-adapter-module167
  - micro-adapter-module167-genes
  - plaque-catalogue
  - septin-catalogue
  - septin-adapter-meta
  - septin-adapter-modules
  - septin-modulegene-emrA
  - septin-modulemembers-emrA
  - septin-modulegene-emrB
  - septin-modulemembers-emrB
  - septin-modulegene-tolC
  - septin-modulemembers-tolC
  - septin-modulegene-emrE
  - septin-modulemembers-emrE
  - septin-module-9
  - septin-module-9-genes
  - septin-module-22
  - septin-module-22-genes
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-profile
  - micro-graph-policy
  - micro-protein-P33891
  - micro-protein-P45568
  - micro-protein-P50102
  - micro-protein-P53165
  - micro-protein-P53252
  - micro-protein-P53847
  - micro-protein-P54003
  - micro-protein-Q03067
  - micro-protein-Q12230
  - micro-protein-Q12745
  - micro-protein-Q6WNK7
  - micro-taxon-4751
  - micro-taxon-4932
  - micro-taxon-559292
  - micro-taxon-562
  - micro-taxon-83333
  - micro-go-0000124
  - micro-go-0004843
  - micro-go-0005783
  - micro-go-0006890
  - micro-go-0030604
  - micro-go-0032126-ancestors
  - micro-go-0032126-constraints
  - micro-go-0032126
  - micro-go-0032991
  - micro-go-0036286
  - micro-go-0046695
  - micro-go-0070939-ancestors
  - micro-go-0070939-constraints
  - micro-go-0070939
  - micro-go-0071819-ancestors
  - micro-go-0071819-constraints
  - micro-go-0071819
  - micro-go-0090512
  - micro-go-0099023
  - micro-go-0140513
  - micro-go-1990065-ancestors
  - micro-go-1990065-constraints
  - micro-go-1990065
  - micro-ipr-IPR003821-retry
  - micro-ipr-IPR007528
  - micro-ipr-IPR009571
  - micro-ipr-IPR013244-retry
  - micro-ipr-IPR013246
  - micro-ipr-IPR018783
  - micro-ipr-IPR021875
  - micro-ipr-IPR021876
  - micro-ipr-IPR028245-retry
  - micro-ipr-IPR028889
  - micro-ipr-IPR037804
  - micro-ipr-IPR050185
  - micro-meta-10.1016_j.jbc.2021.100671
  - micro-meta-10.1016_j.jmb.2004.10.030
  - micro-meta-10.1038_nature04472
  - micro-meta-10.1038_nsmb.1548
  - micro-meta-10.1038_s41586-020-1933-5
  - micro-meta-10.1074_jbc.M110.215327
  - micro-meta-10.1083_jcb.201104040
  - micro-meta-10.1091_mbc.e05-01-0056
  - micro-meta-10.1091_mbc.e08-03-0313
  - micro-meta-10.1091_mbc.e10-12-1021
  - micro-meta-10.1101_gad.1144003
  - micro-meta-11493604
  - micro-meta-11739780
  - micro-meta-11784867
  - micro-meta-12469340
  - micro-meta-14562095
  - micro-meta-15567415
  - micro-meta-15958492
  - micro-meta-16496001
  - micro-meta-16855026
  - micro-meta-20230609
  - micro-meta-22932476
  - micro-meta-25002088
  - micro-meta-8334998
  - micro-tripathi
  - micro-wang
  - micro-adamus
  - micro-karotki
  - micro-olivera
  - micro-walther-html
  - micro-pdb-entry
  - micro-pdb-polymer
  - micro-pdb-assembly
  - micro-pdb-ligand-2
  - micro-pdb-ligand-3
  - micro-adapter-meta
  - micro-adapter-modules
  - micro-adapter-module167
  - micro-adapter-module167-genes
  - plaque-curation
  - plaque-field-guide
  - plaque-rubric
  - plaque-review-skill
  - plaque-protein-skill
  - plaque-graph-skill
  - plaque-review-profile
  - plaque-review-contract
  - plaque-review-schema
  - plaque-structure-schema
  - plaque-agents
  - plaque-review-config
  - plaque-go
  - plaque-go-elg1-ancestors
  - plaque-tax-3027
  - plaque-tax-3028
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-pmid-21336864
  - plaque-pmid-22868567
  - plaque-pmid-14614842
  - plaque-pmid-23499004
  - plaque-pmid-27664980
  - plaque-pmid-11435442
  - plaque-pmid-11689709
  - plaque-pmid-15769872
  - plaque-pmid-14562095
  - plaque-pmid-15780940
  - plaque-pmid-10024884
  - plaque-pmid-24750273
  - plaque-rhiel-publisher
  - plaque-ammermann-publisher
  - plaque-ammermann-web1
  - plaque-ammermann-web2
  - plaque-PMC5286391-legacy
  - plaque-PMC5286394-legacy
  - plaque-PMC99985-legacy
  - plaque-PMC1370732-legacy
  - plaque-up-Q12050
  - plaque-up-P40348
  - plaque-up-P38629
  - plaque-up-P40339
  - plaque-up-P38251
  - plaque-up-Q06706
  - plaque-up-P42935
  - plaque-up-Q02908
  - plaque-up-Q02884
  - plaque-up-P38874
  - plaque-up-Q04868
  - plaque-ipr-IPR006849
  - plaque-ipr-IPR037289
  - plaque-ipr-IPR034687
  - plaque-ipr-IPR008728
  - plaque-ipr-IPR019519
  - plaque-ipr-IPR018627
  - plaque-ipr-IPR039661
  - plaque-ipr-IPR050238
  - plaque-ipr-IPR062598
  - plaque-ipr-IPR062602
  - plaque-catalogue
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-go
  - septin-ncbifam-NF011715
  - septin-ncbifam-NF000391
  - septin-ipr-IPR004638
  - septin-ipr-IPR058622
  - septin-ncbifam-NF042984
  - septin-ncbifam-NF007087
  - septin-ipr-IPR045324
  - septin-peer-protein-P36039
  - septin-peer-protein-P40540
  - septin-protein-P27303
  - septin-protein-P0AEJ0
  - septin-protein-P02930
  - septin-protein-P23895
  - septin-tax2
  - septin-tax4932
  - septin-tax562
  - septin-tax83333
  - septin-doi-science_aao3099
  - septin-doi-j_cell_2018_10_009
  - septin-doi-s41586-020-2389-3
  - septin-doi-eLife_57887
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pmid-41839863
  - septin-pmid-18024586
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-zhong2026-legacy
  - septin-chen2007-legacy
  - septin-complex-CPX-4268
  - septin-eco0005547
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-catalogue
  - septin-adapter-meta
  - septin-adapter-modules
  - septin-modulegene-emrA
  - septin-modulegene-emrB
  - septin-modulegene-tolC
  - septin-modulegene-emrE
  - septin-module-9
  - septin-module-9-genes
  - septin-module-22
  - septin-module-22-genes
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
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
- check_id: dsl1_nzr_complex-uniprot-verify
  name: Native Dsl1/NZR complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dsl1_nzr_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dsl1_nzr_complex-uniprot-verify
- check_id: dsl1_nzr_complex-uniprot-causal
  name: Native Dsl1/NZR complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dsl1_nzr_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dsl1_nzr_complex-uniprot-causal
- check_id: dubm_complex-uniprot-verify
  name: Native DUBm complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dubm_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dubm_complex-uniprot-verify
- check_id: dubm_complex-uniprot-causal
  name: Native DUBm complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dubm_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dubm_complex-uniprot-causal
- check_id: dxr_protein_complex-uniprot-verify
  name: Native Dxr protein complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dxr_protein_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dxr_protein_complex-uniprot-verify
- check_id: dxr_protein_complex-uniprot-causal
  name: Native Dxr protein complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990065
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dxr_protein_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dxr_protein_complex-uniprot-causal
- check_id: eisosome-uniprot-verify
  name: Native eisosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-eisosome-uniprot-verify
- check_id: eisosome-uniprot-causal
  name: Native eisosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-eisosome-uniprot-causal
- check_id: ejectisome-uniprot-verify
  name: Native ejectisome UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ejectisome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ejectisome.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ejectisome-uniprot-verify
- check_id: ejectisome-uniprot-causal
  name: Native ejectisome UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:ejectisome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ejectisome.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ejectisome-uniprot-causal
- check_id: elg1_rfc_like_complex-uniprot-verify
  name: Native Elg1 RFC-like complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031391
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/elg1_rfc_like_complex.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-elg1_rfc_like_complex-uniprot-verify
- check_id: elg1_rfc_like_complex-uniprot-causal
  name: Native Elg1 RFC-like complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031391
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/elg1_rfc_like_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-elg1_rfc_like_complex-uniprot-causal
- check_id: elongator_holoenzyme_complex-uniprot-verify
  name: Native elongator holoenzyme complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033588
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/elongator_holoenzyme_complex.yaml
    --verify
  exit_code: 0
  summary: 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-elongator_holoenzyme_complex-uniprot-verify
- check_id: elongator_holoenzyme_complex-uniprot-causal
  name: Native elongator holoenzyme complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033588
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/elongator_holoenzyme_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-elongator_holoenzyme_complex-uniprot-causal
- check_id: emc_complex-uniprot-verify
  name: Native EMC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0072546
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emc_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emc_complex-uniprot-verify
- check_id: emc_complex-uniprot-causal
  name: Native EMC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0072546
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emc_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emc_complex-uniprot-causal
- check_id: emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify
  name: Native EmrAB-TolC multidrug efflux transport complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify
- check_id: emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal
  name: Native EmrAB-TolC multidrug efflux transport complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal
- check_id: emre_multidrug_transporter_complex-uniprot-verify
  name: Native EmrE multidrug transporter complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990207
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emre_multidrug_transporter_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emre_multidrug_transporter_complex-uniprot-verify
- check_id: emre_multidrug_transporter_complex-uniprot-causal
  name: Native EmrE multidrug transporter complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990207
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emre_multidrug_transporter_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emre_multidrug_transporter_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/dsl1_nzr_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0;
    current SHA256 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0.
    Record bytes unchanged since the original review.
  snapshot_sha256: 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T062447Z-dsl1-nzr-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b3e24dbf5ee127c2c3debd8e36d6e700306769b174374ed4e10d733c5096f473
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/dubm_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591;
    current SHA256 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T062448Z-dubm-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 83feeddf50b6f9e216eeea13d49bcbd8aea883bf6358d222c7332931e0030e06
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/dxr_protein_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e;
    current SHA256 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T062449Z-dxr-protein-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5b4a43814269c2a28e95e685aac9442e063b06c73a0a1e250ae9eb131bbbfdde
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/eisosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 032c3bd7a0cc1b125515740752e69d06e4b8bf20529cad61cd62b9559e4f0b72;
    current SHA256 3f96297240ba46e169dab4e79338949cf92ac200ffd75c509938b12240b1b89c.
    Changed record reassessed against current sources.
  snapshot_sha256: 3f96297240ba46e169dab4e79338949cf92ac200ffd75c509938b12240b1b89c
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T062450Z-eisosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d4d070ac50b8017da55afd07474aea922d3e4de1e6c07dacfc748d348700ab94
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/ejectisome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8;
    current SHA256 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T062451Z-ejectisome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: da8eef14b223c9cc319915c9a36cba41c42f0ddc25567f6ad3de77748df1d224
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/elg1_rfc_like_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837;
    current SHA256 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837.
    Record bytes unchanged since the original review.
  snapshot_sha256: 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2898cc2d84349c73ed45e709954187c571d78a453216ca5bf959d2c4cf75bd9e
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/elongator_holoenzyme_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d;
    current SHA256 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 54f6e4272ddcc3727da6820b7a4db4dbc4ac842c8e43f78bb8974ac8c5c6d3de
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/emc_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54;
    current SHA256 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T062453Z-emc-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 51a8529eb2eabe5bb7c7305dc18975bebe0de1c23f7c66b09b4743cd344bf9f1
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 3f2fc12842c13b847a6c930d89242a164a83e37cfc8840f59fa90fe2c71f0d2c;
    current SHA256 2ecd59317bfeae525a312c7ba1427b4ad561dfb25b621ff647b42e2205c150d6.
    Changed record reassessed against current sources.
  snapshot_sha256: 2ecd59317bfeae525a312c7ba1427b4ad561dfb25b621ff647b42e2205c150d6
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 22bc7fe7167e8a7cd3913e0a30fa883d9572ed33df3d51bb9faa241d333162a9
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/emre_multidrug_transporter_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Original frozen SHA256 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0;
    current SHA256 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T062455Z-emre-multidrug-transporter-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T08:16:41Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5b0e8d7e997bb78f75aa39cdd58ee292e45f99c2ed2b7cb918ee2f7a0e1c6efb
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/dsl1_nzr_complex.yaml
  locator: Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8
  accessed_at: '2026-11-04T08:14:42.850819Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target unchanged from original
    frozen input.
  snapshot_sha256: 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T062447Z-dsl1-nzr-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T08:14:42.850902Z'
  support: supports
  summary: Original source inputs, checks, evidence tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access times are not newly executed
    or fetched.
  snapshot_sha256: b3e24dbf5ee127c2c3debd8e36d6e700306769b174374ed4e10d733c5096f473
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/0-stale.diff
  locator: Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7
  accessed_at: '2026-11-04T08:14:42.850941Z'
  support: supports
  summary: Empty diff.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/dubm_complex.yaml
  locator: Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8
  accessed_at: '2026-11-04T08:14:42.850965Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target unchanged from original
    frozen input.
  snapshot_sha256: 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T062448Z-dubm-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T08:14:42.850988Z'
  support: supports
  summary: Original source inputs, checks, evidence tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access times are not newly executed
    or fetched.
  snapshot_sha256: 83feeddf50b6f9e216eeea13d49bcbd8aea883bf6358d222c7332931e0030e06
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/1-stale.diff
  locator: Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7
  accessed_at: '2026-11-04T08:14:42.851024Z'
  support: supports
  summary: Empty diff.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/dxr_protein_complex.yaml
  locator: Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8
  accessed_at: '2026-11-04T08:14:42.851046Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target unchanged from original
    frozen input.
  snapshot_sha256: 0a9e8c00028f315a781db6e7d819a864d844254eaa639b885573f818907bae5e
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T062449Z-dxr-protein-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T08:14:42.851065Z'
  support: supports
  summary: Original source inputs, checks, evidence tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access times are not newly executed
    or fetched.
  snapshot_sha256: 5b4a43814269c2a28e95e685aac9442e063b06c73a0a1e250ae9eb131bbbfdde
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/2-stale.diff
  locator: Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7
  accessed_at: '2026-11-04T08:14:42.851096Z'
  support: supports
  summary: Empty diff.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-3
  kind: record_content
  reference: data/structures/other/eisosome.yaml
  locator: Complete maintained YAML at 6d564c8d647868414ddf025c64068d9ac990abc8
  accessed_at: '2026-11-04T08:14:42.851119Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target differs by the Pil1/Lsp1
    core type, graph family grounding and append-only history.
  snapshot_sha256: 3f96297240ba46e169dab4e79338949cf92ac200ffd75c509938b12240b1b89c
- evidence_id: micro-prior-3
  kind: prior_review
  reference: reviews/structured/20261022T062450Z-eisosome-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T08:14:42.851140Z'
  support: supports
  summary: Original source inputs, checks, evidence tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access times are not newly executed
    or fetched.
  snapshot_sha256: d4d070ac50b8017da55afd07474aea922d3e4de1e6c07dacfc748d348700ab94
- evidence_id: micro-delta-3
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/3-stale.diff
  locator: Original frozen target versus current main 7d8fe7f460f7b4af05368893a7e9fa8271345bd7
  accessed_at: '2026-11-04T08:14:42.851180Z'
  support: supports
  summary: 'Two substantive updates: pil1_lsp1_bar_core component PROTEIN to PROTEIN_COMPLEX
    and its graph grounding to IPR028245; two dated history events cite earlier corrections.
    This is reassessed using actual native family and primary assembled-scaffold evidence,
    without resolving broad historical issues.'
  snapshot_sha256: 7c49df3e3ffaefb5f35633d5b460e49819ac999e98678c14716a850cccbdb1ae
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components and Discussions clauses
  accessed_at: '2026-11-04T08:14:42.851204Z'
  support: supports
  summary: Taxon-neutral families/classes are valid; formation differs from function
    and viability. Preserve dated rationale and posed_date; current prompt/notes may
    be narrowed after separately authorized grounded curation.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: ComponentTypeEnum, EssentialityEnum, causal node types
  accessed_at: '2026-11-04T08:14:42.851227Z'
  support: supports
  summary: GENE_OR_PROTEIN permits molecular complexes. A specific assembled core
    can be PROTEIN_COMPLEX without requiring an obligate heterodimer. UNKNOWN formation
    can remain when evidence is condition-scoped.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks, full record and evidence contract
  accessed_at: '2026-11-04T08:14:42.851258Z'
  support: supports
  summary: Positive named genes/proteins/pathways trigger applicability assessment
    even without an expression claim. Catalogue coverage and matched gene/module evidence
    are bounded contextual observations, not assembly evidence.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Issue-only persistence, native checks and source provenance
  accessed_at: '2026-11-04T08:14:42.851280Z'
  support: supports
  summary: The explicit mixed batch has concrete scientific and bundle issues. No
    empty optional field, unavailable route or acknowledged unknown alone is a scientific
    finding. Root owns successor save and global gates.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Claim-scoped constituents and coarse function/assembly graphs
  accessed_at: '2026-11-04T08:14:42.851298Z'
  support: supports
  summary: Descriptive membership/function and tested assembly relations are assessed
    at their declared granularity; exact stoichiometry, universal necessity and mandatory
    new experiments are not imposed.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-neighbor-filament
  kind: record_content
  reference: data/structures/cytoskeleton/eisosome_filament.yaml
  locator: Complete already-frozen boundary neighbor
  accessed_at: '2026-11-04T08:14:42.851315Z'
  support: supports
  summary: Whole eisosome is distinct from the filament and membrane-domain children.
    Neighbor content is boundary context, not primary evidence or a terminal disposition
    of its findings.
  snapshot_sha256: 0a59cc075da50578f12a4950252cb8f7133ba55c99703a0843bf3f8651e366c0
- evidence_id: micro-neighbor-mcc
  kind: record_content
  reference: data/structures/envelope/eisosome_membrane_domain_mcc.yaml
  locator: Complete already-frozen boundary neighbor
  accessed_at: '2026-11-04T08:14:42.851337Z'
  support: supports
  summary: Whole eisosome is distinct from the filament and membrane-domain children.
    Neighbor content is boundary context, not primary evidence or a terminal disposition
    of its findings.
  snapshot_sha256: cf0490c93ccba7b66f5f9fc3f6e108981620ba71eb7635fb3c7582dd7dfb1a1f
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/original-audit.json
  locator: Eight actual original native validate/render commands; 56 historical input
    occurrences; eight original artifacts
  accessed_at: '2026-11-04T07:59:12.394605Z'
  support: supports
  summary: All four original YAMLs validate and render exactly their retained Markdown;
    historical input hashes match their recorded revisions, and all eight artifacts
    equal the original PR head.
  snapshot_sha256: 4be91dff292d820c362be5c7bdc32a5fb5c9c2799e0e12425d5de665e9875e50
- evidence_id: micro-protein-P33891
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P33891.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P33891.raw
  accessed_at: '2026-11-04T07:59:27.089850Z'
  support: supports
  summary: 'P33891: UniProtKB reviewed (Swiss-Prot); Protein transport protein TIP20;
    primary genes [''TIP20'']; loci [''YGL145W'']; taxon 559292; InterPro [''IPR042044'',
    ''IPR007528'', ''IPR042041'', ''IPR042042'', ''IPR042043'', ''IPR042040'']. Native
    annotation sources are distinct from freshly inspected primary bodies and do not
    independently certify every linked experiment.'
  snapshot_sha256: 17fde0f47f341173ded9336df2821fdc5949d223d9ccfcb8401e39a424d925ea
- evidence_id: micro-protein-P45568
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P45568.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P45568.raw
  accessed_at: '2026-11-04T07:59:25.621184Z'
  support: supports
  summary: 'P45568: UniProtKB reviewed (Swiss-Prot); 1-deoxy-D-xylulose 5-phosphate
    reductoisomerase; primary genes [''dxr'']; loci [''b0173'', ''JW0168'']; taxon
    83333; InterPro [''IPR003821'', ''IPR013644'', ''IPR013512'', ''IPR026877'', ''IPR036169'',
    ''IPR036291'']. Native annotation sources are distinct from freshly inspected
    primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: 3cc676d623cb06e717c43f25cfe46cd3972378877ebb100d5fbf9951f39c4aa8
- evidence_id: micro-protein-P50102
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P50102.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P50102.raw
  accessed_at: '2026-11-04T07:59:24.465737Z'
  support: supports
  summary: 'P50102: UniProtKB reviewed (Swiss-Prot); Ubiquitin carboxyl-terminal hydrolase
    8; primary genes [''UBP8'']; loci [''YMR223W'', ''YM9959.05'']; taxon 559292;
    InterPro [''IPR038765'', ''IPR001394'', ''IPR050185'', ''IPR028889'', ''IPR018200'',
    ''IPR013083'', ''IPR001607'']. Native annotation sources are distinct from freshly
    inspected primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: 6e1bebc73faae35a7d10d85e423978880a3c99ee0867b7e9b9f45a1c42535a69
- evidence_id: micro-protein-P53165
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53165.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P53165.raw
  accessed_at: '2026-11-04T07:59:23.722024Z'
  support: supports
  summary: 'P53165: UniProtKB reviewed (Swiss-Prot); SAGA complex subunit SGF73; primary
    genes [''SGF73'']; loci [''YGL066W'']; taxon 559292; InterPro [''IPR013243'',
    ''IPR037804'', ''IPR041251'']. Native annotation sources are distinct from freshly
    inspected primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: 4d6bb37039a2002505921506d07c6bd82cd5ff3a7d62d28ec45ecc541450afc9
- evidence_id: micro-protein-P53252
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53252.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P53252.raw
  accessed_at: '2026-11-04T07:59:26.400362Z'
  support: supports
  summary: 'P53252: UniProtKB reviewed (Swiss-Prot); Sphingolipid long chain base-responsive
    protein PIL1; primary genes [''PIL1'']; loci [''YGR086C'']; taxon 559292; InterPro
    [''IPR027267'', ''IPR028245'']. Native annotation sources are distinct from freshly
    inspected primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: f4f742a1eab8a34224819b63169967aac3323244aa49ccfb6fb6f258bd78e2de
- evidence_id: micro-protein-P53847
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53847.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P53847.raw
  accessed_at: '2026-11-04T07:59:28.513437Z'
  support: supports
  summary: 'P53847: UniProtKB reviewed (Swiss-Prot); Protein transport protein DSL1;
    primary genes [''DSL1'']; loci [''YNL258C'', ''N0842'']; taxon 559292; InterPro
    [''IPR021876'', ''IPR021875'', ''IPR038442'', ''IPR046362'']. Native annotation
    sources are distinct from freshly inspected primary bodies and do not independently
    certify every linked experiment.'
  snapshot_sha256: 1a5ab310843a1ace362d203aa58924fdd75bfd18eeeebafe8fdf2267c1799732
- evidence_id: micro-protein-P54003
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P54003.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-P54003.raw
  accessed_at: '2026-11-04T07:59:29.524141Z'
  support: supports
  summary: 'P54003: UniProtKB reviewed (Swiss-Prot); Protein SUR7; primary genes [''SUR7''];
    loci [''YML052W'', ''YM9958.11'']; taxon 559292; InterPro [''IPR009571'']. Native
    annotation sources are distinct from freshly inspected primary bodies and do not
    independently certify every linked experiment.'
  snapshot_sha256: 9f26f2c5a9984a2a9a67dd5fe8478290ec8522abbc75595d2829145fa791b25d
- evidence_id: micro-protein-Q03067
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q03067.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q03067.raw
  accessed_at: '2026-11-04T07:59:25.534528Z'
  support: supports
  summary: 'Q03067: UniProtKB reviewed (Swiss-Prot); SAGA complex subunit SGF11; primary
    genes [''SGF11'']; loci [''YPL047W'']; taxon 559292; InterPro [''IPR013246'',
    ''IPR060617'', ''IPR041216'']. Native annotation sources are distinct from freshly
    inspected primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: 700291af57b16839d1636cabf1913ac5ec904985aba2d2d29e46170c7e28814f
- evidence_id: micro-protein-Q12230
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12230.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q12230.raw
  accessed_at: '2026-11-04T07:59:25.318172Z'
  support: supports
  summary: 'Q12230: UniProtKB reviewed (Swiss-Prot); Sphingolipid long chain base-responsive
    protein LSP1; primary genes [''LSP1'']; loci [''YPL004C'']; taxon 559292; InterPro
    [''IPR027267'', ''IPR028245'']. Native annotation sources are distinct from freshly
    inspected primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: 5f0c82d657897c50f60bfe700506437ddc2cb428bb6772074e9196aaef8f68ce
- evidence_id: micro-protein-Q12745
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12745.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q12745.raw
  accessed_at: '2026-11-04T07:59:29.489923Z'
  support: supports
  summary: 'Q12745: UniProtKB reviewed (Swiss-Prot); Protein transport protein SEC39;
    primary genes [''SEC39'']; loci [''YLR440C'']; taxon 559292; InterPro [''IPR013244''].
    Native annotation sources are distinct from freshly inspected primary bodies and
    do not independently certify every linked experiment.'
  snapshot_sha256: c651ab454f0bc46e264fca6e399e679febd27fc8a67ce8bf795e266a715b01b2
- evidence_id: micro-protein-Q6WNK7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q6WNK7.json
  locator: Native identity/status/name, gene aliases/loci/taxon, InterPro and relevant
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/protein-Q6WNK7.raw
  accessed_at: '2026-11-04T07:59:28.404910Z'
  support: supports
  summary: 'Q6WNK7: UniProtKB reviewed (Swiss-Prot); SAGA complex subunit SUS1; primary
    genes [''SUS1'']; loci [''YBR111W-A'']; taxon 559292; InterPro [''IPR018783'',
    ''IPR038212'']. Native annotation sources are distinct from freshly inspected
    primary bodies and do not independently certify every linked experiment.'
  snapshot_sha256: fe94c71a434c59a7bf47d758eeb5455593b5917dc385277f4acb67c7f919c7c3
- evidence_id: micro-query-DSL1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-DSL1-559292.raw
  accessed_at: '2026-11-04T08:00:23.943463Z'
  support: supports
  summary: Current bounded query returns ['P53847']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: dc74aeb59a47a0828e178dcdbcad9a3324ced8aab894b59ac922ef9f2b905c73
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:23.943463Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-DSL3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-DSL3-559292.raw
  accessed_at: '2026-11-04T08:01:23.928296Z'
  support: supports
  summary: Current bounded query returns ['Q12745']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 60fc3ef9ae7f2a89aa17c98b55a62ae07f979e012b80a78e1a21ebfeb920ef4d
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:01:23.928296Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-LSP1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALSP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-LSP1-559292.raw
  accessed_at: '2026-11-04T08:00:19.826914Z'
  support: supports
  summary: Current bounded query returns ['Q12230']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 60c5d64be1e8207cd60ba91e1a26c45f1a408e6512acc4547d2829f667c43a21
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALSP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:19.826914Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-PIL1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-PIL1-559292.raw
  accessed_at: '2026-11-04T08:00:21.889461Z'
  support: supports
  summary: Current bounded query returns ['P53252']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 2d13418365ff6b7b41298917a401bbe0ed436ddc7563af8f13bc10c7d5722b2a
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:21.889461Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-SEC39-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SEC39-559292.raw
  accessed_at: '2026-11-04T08:00:17.724156Z'
  support: supports
  summary: Current bounded query returns ['Q12745']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 60fc3ef9ae7f2a89aa17c98b55a62ae07f979e012b80a78e1a21ebfeb920ef4d
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:17.724156Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-SGF11-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SGF11-559292.raw
  accessed_at: '2026-11-04T08:00:18.562171Z'
  support: supports
  summary: Current bounded query returns ['Q03067']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: d84fc08150e2ed10c54646bdb17168b99641ac8950397618b074eacaac883769
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:18.562171Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-SGF73-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF73%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SGF73-559292.raw
  accessed_at: '2026-11-04T08:00:20.650768Z'
  support: supports
  summary: Current bounded query returns ['P53165']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: f9556c4862e406e37a9ece3b71cfb86ecf82a18a77ecd576539734b8cb080b36
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF73%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:20.650768Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-SUR7-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUR7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SUR7-559292.raw
  accessed_at: '2026-11-04T08:00:20.958687Z'
  support: supports
  summary: Current bounded query returns ['P54003']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 4c29ffd344834d92aed34a0900a95b054e4b46ae7d25df3866413488437ae518
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUR7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:20.958687Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-SUS1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-SUS1-559292.raw
  accessed_at: '2026-11-04T08:00:20.047972Z'
  support: supports
  summary: Current bounded query returns ['Q6WNK7']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 8f1b694d2387950128b6fbe42ba576cd99e52d43e0a7cd8177f5803cc66f5fbf
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:20.047972Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-TIP20-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATIP20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-TIP20-559292.raw
  accessed_at: '2026-11-04T08:00:17.532642Z'
  support: supports
  summary: Current bounded query returns ['P33891']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: eaf60ba4b2cdb7e7f9cd38459d97de6c9db3cbf7763c81b62ea407f6ab52f734
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATIP20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:17.532642Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-UBP8-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AUBP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-UBP8-559292.raw
  accessed_at: '2026-11-04T08:00:19.518074Z'
  support: supports
  summary: Current bounded query returns ['P50102']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 2a06c64ba1bdc6848dc60295e96f0618cc231bc1a4557b292183492b05422ade
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AUBP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:19.518074Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-dxr-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adxr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-dxr-83333.raw
  accessed_at: '2026-11-04T08:00:22.159939Z'
  support: supports
  summary: Current bounded query returns ['P45568']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 72aa997329fd9ec39c983db4b58a3a87fab2b868cf67e2d50316a456264bece2
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adxr%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:00:22.159939Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-query-ispC-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AispC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/query-ispC-83333.raw
  accessed_at: '2026-11-04T08:01:22.194547Z'
  support: supports
  summary: Current bounded query returns ['P45568']; native primary genes and aliases
    independently inspected. This is current reproducibility, not reconstruction or
    refutation of a historical selection query.
  snapshot_sha256: 72aa997329fd9ec39c983db4b58a3a87fab2b868cf67e2d50316a456264bece2
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AispC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:01:22.194547Z; reviewed:true, stated exact gene/taxon, requested
    size100 and complete returned page. No all-alias universal or historical uniqueness
    inference.
- evidence_id: micro-taxon-4751
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4751.json
  locator: Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-4751.raw
  accessed_at: '2026-11-04T07:59:31.006642Z'
  support: supports
  summary: '4751: Fungi; rank kingdom. Species, reference strain and particular experimental
    preparation remain distinct.'
  snapshot_sha256: 7878dac8e24944f55fe55c4711fbfc0e51b6a7de47d701a553b8e6ec2ea1d243
- evidence_id: micro-taxon-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-4932.raw
  accessed_at: '2026-11-04T07:59:27.367321Z'
  support: supports
  summary: '4932: Saccharomyces cerevisiae; rank species. Species, reference strain
    and particular experimental preparation remain distinct.'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
- evidence_id: micro-taxon-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-559292.raw
  accessed_at: '2026-11-04T07:59:26.382255Z'
  support: supports
  summary: '559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c); rank strain.
    Species, reference strain and particular experimental preparation remain distinct.'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: micro-taxon-562
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/562.json
  locator: Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-562.raw
  accessed_at: '2026-11-04T07:59:31.003772Z'
  support: supports
  summary: '562: Escherichia coli; rank species. Species, reference strain and particular
    experimental preparation remain distinct.'
  snapshot_sha256: 20aa358053d2fae1e2cd74636ed5aca1efbc372e5b8bcfdb10d3fa80be6789a1
- evidence_id: micro-taxon-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Scientific name, rank and lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/taxon-83333.raw
  accessed_at: '2026-11-04T07:59:27.729035Z'
  support: supports
  summary: '83333: Escherichia coli (strain K12); rank strain. Species, reference
    strain and particular experimental preparation remain distinct.'
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-go-0000124
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0000124.raw
  accessed_at: '2026-11-04T07:59:27.003025Z'
  support: supports
  summary: 'GO:0000124 SAGA complex; isObsolete=False. A SAGA-type histone acetyltransferase
    complex that deubiquitinates H2A and/or H2B. This complex is organized into several
    functional submodules: a structural core including the activator binding module
    and consisting of ADA1 or a homolog, members of the SPT and TAF protein families
    as well as promotor recruitment factor TRRAP/TRA1, a histone acetyltransferase
    (HAT) module consisting of GCN5/KAT2A or PCAF/KAT2B, ADA2, ADA3/NGG1, and SGF29
    or homologues thereof, a histone deubiquitinase (DUB) module consisting of ATXN7/SGF73,
    ATXN7L3/SGF11, ENY2/SUS1 and USP22/UBP8 or homologues thereof, and in some taxa
    a splicing module consisting of SF3B3 and SF3B5 or homologues thereof (not in
    fungi). In budding yeast also contains Spt8 which distinguishes it from SAGA-like
    (SLIK) complex (GO:0046695).'
  snapshot_sha256: 63ad3e9380d8ef26b9acfc5f370363a515b92385bf97cc5bfaa38abc63e39f7e
- evidence_id: micro-go-0004843
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004843
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0004843.raw
  accessed_at: '2026-11-04T07:59:27.589734Z'
  support: supports
  summary: GO:0004843 cysteine-type deubiquitinase activity; isObsolete=False. An
    thiol-dependent isopeptidase activity that cleaves ubiquitin from a target protein
    to which it is conjugated.
  snapshot_sha256: e887105669224a902e0f7aecbe1767883e2ac29623af6e34124a8f0c3cf62f84
- evidence_id: micro-go-0005783
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0005783.raw
  accessed_at: '2026-11-04T07:59:27.694917Z'
  support: supports
  summary: GO:0005783 endoplasmic reticulum; isObsolete=False. The irregular network
    of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm
    of many eukaryotic cells. The membranes form a complex meshwork of tubular channels,
    which are often expanded into slitlike cavities called cisternae. The ER takes
    two forms, rough (or granular), with ribosomes adhering to the outer surface,
    and smooth (with no ribosomes attached).
  snapshot_sha256: 109f8b91a82edb8029dce3068738ce319d7a35059ca1fcdb6a545364ddbdb02d
- evidence_id: micro-go-0006890
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006890
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0006890.raw
  accessed_at: '2026-11-04T07:59:27.980475Z'
  support: supports
  summary: GO:0006890 retrograde vesicle-mediated transport, Golgi to endoplasmic
    reticulum; isObsolete=False. The directed movement of substances from the Golgi
    back to the endoplasmic reticulum, mediated by vesicles bearing specific protein
    coats such as COPI or COG.
  snapshot_sha256: 6a545616700c8dbb99bb30c2ec9cc8baeb50063d5fa9302156ffe73574f1796b
- evidence_id: micro-go-0030604
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030604
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0030604.raw
  accessed_at: '2026-11-04T07:59:28.179731Z'
  support: supports
  summary: 'GO:0030604 1-deoxy-D-xylulose-5-phosphate reductoisomerase activity; isObsolete=False.
    Catalysis of the reaction: 2-C-methyl-D-erythritol 4-phosphate + NADP+ = 1-deoxy-D-xylulose
    5-phosphate + H+ + NADPH.'
  snapshot_sha256: eef1b54fb9b5f615c4423a2999256c3503940d7bf95107806067a67755ab55c6
- evidence_id: micro-go-0032126-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126/ancestors?relations=is_a
  locator: Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032126-ancestors.raw
  accessed_at: '2026-11-04T08:00:17.298230Z'
  support: supports
  summary: GO:0032126 eisosome; isObsolete=False. A cell part that is composed of
    the eisosome membrane or MCC domain, a furrow-like plasma membrane sub-domain
    and associated integral transmembrane proteins, and the proteins (eisosome filaments)
    that form a scaffolding lattice on the cytoplasmic face. Eisosomes broadly affect
    overall plasma membrane organization. Returned ancestors ['GO:0110165', 'GO:0005575',
    'GO:0032126']
  snapshot_sha256: 71a47a7c125b2266f533e8683a5f8a6c058ff7e39e97a6cab86938678d538d14
- evidence_id: micro-go-0032126-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126/constraints
  locator: Exact term and returned taxon-constraint response; no prevalence census;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032126-constraints.raw
  accessed_at: '2026-11-04T08:00:17.295978Z'
  support: supports
  summary: GO:0032126 eisosome; isObsolete=False. A cell part that is composed of
    the eisosome membrane or MCC domain, a furrow-like plasma membrane sub-domain
    and associated integral transmembrane proteins, and the proteins (eisosome filaments)
    that form a scaffolding lattice on the cytoplasmic face. Eisosomes broadly affect
    overall plasma membrane organization.
  snapshot_sha256: c8a05ae216f7bec3ca011002eb8fb602ea81dd0d2fa84a64da339157b45159bc
- evidence_id: micro-go-0032126
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032126.raw
  accessed_at: '2026-11-04T07:59:28.288658Z'
  support: supports
  summary: GO:0032126 eisosome; isObsolete=False. A cell part that is composed of
    the eisosome membrane or MCC domain, a furrow-like plasma membrane sub-domain
    and associated integral transmembrane proteins, and the proteins (eisosome filaments)
    that form a scaffolding lattice on the cytoplasmic face. Eisosomes broadly affect
    overall plasma membrane organization.
  snapshot_sha256: dbae9fb801773beac0ef3c748e0e453a8d3da80362a8562fbc9fcf66d0ce8d4d
- evidence_id: micro-go-0032991
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0032991.raw
  accessed_at: '2026-11-04T07:59:28.350927Z'
  support: supports
  summary: GO:0032991 protein-containing complex; isObsolete=False. A stable assembly
    of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or
    lipids, in which at least one component is a protein and the constituent parts
    function together.
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
- evidence_id: micro-go-0036286
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036286
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0036286.raw
  accessed_at: '2026-11-04T07:59:28.561789Z'
  support: supports
  summary: GO:0036286 eisosome filament; isObsolete=False. A filamentous cortical
    structure formed, in S. pombe, by the eisosome component Pil1.
  snapshot_sha256: f3d69bd037b85ca71f020393780377ec68de97d5e47039f253514ba274cdc7ca
- evidence_id: micro-go-0046695
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046695
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0046695.raw
  accessed_at: '2026-11-04T07:59:28.776718Z'
  support: supports
  summary: GO:0046695 SLIK (SAGA-like) complex; isObsolete=False. A SAGA-type histone
    acetyltransferase complex that contains a smaller form of Spt7 (lacking the SPT8
    binding region) than the fungal SAGA complex, and consequently lacks Spt8. The
    complex is involved in the yeast retrograde response pathway, which is important
    for gene expression changes during mitochondrial dysfunction.
  snapshot_sha256: 6cad97294e1267f4d0640e65ba628bc6269e1d0da8f98b2f6e016677931f3bb0
- evidence_id: micro-go-0070939-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/ancestors?relations=is_a
  locator: Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0070939-ancestors.raw
  accessed_at: '2026-11-04T08:00:16.801566Z'
  support: supports
  summary: GO:0070939 Dsl1/NZR complex; isObsolete=False. A multisubunit tethering
    complex, i.e. a protein complex involved in mediating the initial interaction
    between vesicles and the membranes with which they fuse, that is involved in trafficking
    from the Golgi apparatus to the ER. In Saccharomyces cerevisiae the Dsl1p complex
    contains Dsl1p, Tip20p, and Sec39p. Returned ancestors ['GO:0070939', 'GO:0032991',
    'GO:0140534', 'GO:0099023', 'GO:0005575']
  snapshot_sha256: a7fce74e35bc6ca1d05c98ed49a01d880de65a108211c83d2dac5b3e71535286
- evidence_id: micro-go-0070939-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/constraints
  locator: Exact term and returned taxon-constraint response; no prevalence census;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0070939-constraints.raw
  accessed_at: '2026-11-04T08:00:17.070105Z'
  support: supports
  summary: GO:0070939 Dsl1/NZR complex; isObsolete=False. A multisubunit tethering
    complex, i.e. a protein complex involved in mediating the initial interaction
    between vesicles and the membranes with which they fuse, that is involved in trafficking
    from the Golgi apparatus to the ER. In Saccharomyces cerevisiae the Dsl1p complex
    contains Dsl1p, Tip20p, and Sec39p.
  snapshot_sha256: 8104aae88fa5bbcb62f782ec7f407424914aa626317ae59c385e9f9f98bcfcf1
- evidence_id: micro-go-0070939
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0070939.raw
  accessed_at: '2026-11-04T07:59:29.307024Z'
  support: supports
  summary: GO:0070939 Dsl1/NZR complex; isObsolete=False. A multisubunit tethering
    complex, i.e. a protein complex involved in mediating the initial interaction
    between vesicles and the membranes with which they fuse, that is involved in trafficking
    from the Golgi apparatus to the ER. In Saccharomyces cerevisiae the Dsl1p complex
    contains Dsl1p, Tip20p, and Sec39p.
  snapshot_sha256: 9d573e8a655de9867ccf196f5833b59c5327b99fb16171c1f8898fb71775d9fa
- evidence_id: micro-go-0071819-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/ancestors?relations=is_a
  locator: Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0071819-ancestors.raw
  accessed_at: '2026-11-04T08:00:16.998432Z'
  support: supports
  summary: GO:0071819 DUBm complex; isObsolete=False. A protein complex that forms
    part of SAGA-type complexes SAGA and SLIK, and mediates deubiquitination of histone
    H2B. In S. cerevisiae, the DUBm consists of the proteins Ubp8p, Sgf11p, Sus1p,
    and Sgf73p. Returned ancestors ['GO:0140513', 'GO:0071819', 'GO:0032991', 'GO:0005575']
  snapshot_sha256: af30f0fc4f26edbf10072d95a2232901023c93f0a25cb2a3e806e4ff648f6315
- evidence_id: micro-go-0071819-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/constraints
  locator: Exact term and returned taxon-constraint response; no prevalence census;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0071819-constraints.raw
  accessed_at: '2026-11-04T08:00:17.542738Z'
  support: supports
  summary: GO:0071819 DUBm complex; isObsolete=False. A protein complex that forms
    part of SAGA-type complexes SAGA and SLIK, and mediates deubiquitination of histone
    H2B. In S. cerevisiae, the DUBm consists of the proteins Ubp8p, Sgf11p, Sus1p,
    and Sgf73p.
  snapshot_sha256: 8fe1072f4c20e5fbe6f56e408ce4a573edf16b04799b994937a8f3d7c6c452a1
- evidence_id: micro-go-0071819
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0071819.raw
  accessed_at: '2026-11-04T07:59:28.937936Z'
  support: supports
  summary: GO:0071819 DUBm complex; isObsolete=False. A protein complex that forms
    part of SAGA-type complexes SAGA and SLIK, and mediates deubiquitination of histone
    H2B. In S. cerevisiae, the DUBm consists of the proteins Ubp8p, Sgf11p, Sus1p,
    and Sgf73p.
  snapshot_sha256: 7e801f75fedb65ad0db65550991850d183f008ac86cac6e3a6831a5364c7d828
- evidence_id: micro-go-0090512
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0090512
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0090512.raw
  accessed_at: '2026-11-04T07:59:29.004087Z'
  support: supports
  summary: GO:0090512 eisosome membrane domain/MCC; isObsolete=False. A plasma membrane
    part that is composed of a furrow-like plasma membrane domain and associated integral
    transmembrane proteins.
  snapshot_sha256: cd47b07926424718181070a2da3fe12bb01ff8bf58e3dfa4c06bde473e61d9c6
- evidence_id: micro-go-0099023
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0099023
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0099023.raw
  accessed_at: '2026-11-04T07:59:29.109739Z'
  support: supports
  summary: GO:0099023 vesicle tethering complex; isObsolete=False. Any protein complex
    that plays a role in vesicle tethering.
  snapshot_sha256: 01832c9f3bb878942b42f07440745bcce33c8f2db6eb8eb7773ca0d89c89f7fb
- evidence_id: micro-go-0140513
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140513
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-0140513.raw
  accessed_at: '2026-11-04T07:59:29.227296Z'
  support: supports
  summary: GO:0140513 nuclear protein-containing complex; isObsolete=False. A stable
    assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates
    or lipids, in which at least one component is a protein and the constituent parts
    function together in the nucleus.
  snapshot_sha256: 61c31928c6fb33a97da0bafa0beafb5392a27dac53b617f92ba08fb5cf0511b7
- evidence_id: micro-go-1990065-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/ancestors?relations=is_a
  locator: Exact term and returned is_a ancestor identifiers; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-1990065-ancestors.raw
  accessed_at: '2026-11-04T08:00:17.308142Z'
  support: supports
  summary: GO:1990065 Dxr protein complex; isObsolete=False. A protein complex that
    is involved in the MEP pathway of IPP biosynthesis. It catalyzes the NADP-dependent
    rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol
    4-phosphate (MEP). Returned ancestors ['GO:0032991', 'GO:0005575', 'GO:1990065']
  snapshot_sha256: 9b7b56bd21c9039545b6bb1c56b0bed9f02238c1f52583ba80beb1dc9a6bf7a2
- evidence_id: micro-go-1990065-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065/constraints
  locator: Exact term and returned taxon-constraint response; no prevalence census;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-1990065-constraints.raw
  accessed_at: '2026-11-04T08:00:17.288801Z'
  support: supports
  summary: GO:1990065 Dxr protein complex; isObsolete=False. A protein complex that
    is involved in the MEP pathway of IPP biosynthesis. It catalyzes the NADP-dependent
    rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol
    4-phosphate (MEP).
  snapshot_sha256: 69479b43ae0ea84b767eac640779af8d8ef72e70acd00c073e774c8ad439156d
- evidence_id: micro-go-1990065
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990065
  locator: Exact active term identity/definition; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/go-1990065.raw
  accessed_at: '2026-11-04T07:59:29.374918Z'
  support: supports
  summary: GO:1990065 Dxr protein complex; isObsolete=False. A protein complex that
    is involved in the MEP pathway of IPP biosynthesis. It catalyzes the NADP-dependent
    rearrangement and reduction of 1-deoxy-D-xylulose-5-phosphate (DXP) to 2-C-methyl-D-erythritol
    4-phosphate (MEP).
  snapshot_sha256: a18154dc0f64aa6225ba40f97a5556ae22f551d541c9b16e8a77fa1ab0823c44
- evidence_id: micro-ipr-IPR003821-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003821/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR003821-retry.raw
  accessed_at: '2026-11-04T08:00:16.531460Z'
  support: supports
  summary: 'IPR003821: 1-deoxy-D-xylulose 5-phosphate reductoisomerase; native type
    family. Native family identity/type and maintained example xrefs assessed; database
    prose is authority context, not a primary experiment.'
  snapshot_sha256: a3fbe1c1ff8c08bfe94fb7f6c3b1e116dc3a025d6e96adba27e2d2e62b79b6d4
- evidence_id: micro-ipr-IPR007528
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007528/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR007528.raw
  accessed_at: '2026-11-04T07:59:29.595707Z'
  support: supports
  summary: 'IPR007528: RINT-1/Tip20; native type family. Native family identity/type
    and maintained example xrefs assessed; database prose is authority context, not
    a primary experiment.'
  snapshot_sha256: 65941631edcc70f1e82f3beba6f3323cda1bdb7e20b53fc7880dcde43e26b795
- evidence_id: micro-ipr-IPR009571
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009571/
  locator: Complete native entry metadata/type/description and flags [False, False];
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR009571.raw
  accessed_at: '2026-11-04T08:00:16.586202Z'
  support: supports
  summary: 'IPR009571: Membrane protein SUR7/Rim9-like, fungi; native type family.
    Broad SUR7/Rim9-like family, including other proteins; no automatic exact Sur7-only
    mapping.'
  snapshot_sha256: c74c73d3bc87f92f276f050b86fd528fb0fab53e131f1afa34bc2ad80c075262
- evidence_id: micro-ipr-IPR013244-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013244/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR013244-retry.raw
  accessed_at: '2026-11-04T08:06:41.226681Z'
  support: supports
  summary: 'IPR013244: Sec39 domain; native type domain. A domain is not substituted
    for the complete named constituent class.'
  snapshot_sha256: e27da0c1dbbe835c548fccac3186b8e828f9915c474c876c2fa734a464603ecb
- evidence_id: micro-ipr-IPR013246
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013246/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR013246.raw
  accessed_at: '2026-11-04T07:59:29.609269Z'
  support: supports
  summary: 'IPR013246: SAGA complex, Sgf11 subunit; native type family. Native family
    identity/type and maintained example xrefs assessed; database prose is authority
    context, not a primary experiment.'
  snapshot_sha256: 19e61ef02df71f24ece84502d7c487596e0146f44ae9820867ce251e8122e546
- evidence_id: micro-ipr-IPR018783
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018783/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR018783.raw
  accessed_at: '2026-11-04T07:59:29.802684Z'
  support: supports
  summary: 'IPR018783: Transcription factor, enhancer of yellow 2; native type family.
    Native family identity/type and maintained example xrefs assessed; database prose
    is authority context, not a primary experiment.'
  snapshot_sha256: 95b932aadb7a43b64f7714f593fca731839e603abbdf3e1946889426f699d24c
- evidence_id: micro-ipr-IPR021875
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021875/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR021875.raw
  accessed_at: '2026-11-04T08:01:22.247049Z'
  support: supports
  summary: 'IPR021875: Retrograde transport protein Dsl1 N-terminal domain; native
    type domain. A domain is not substituted for the complete named constituent class.'
  snapshot_sha256: 9da4a43e1a9eef1bc85656f706a703084666d19ed6fe9dd7518f115a2484e851
- evidence_id: micro-ipr-IPR021876
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021876/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR021876.raw
  accessed_at: '2026-11-04T08:01:23.273344Z'
  support: supports
  summary: 'IPR021876: Retrograde transport protein Dsl1, C-terminal domain; native
    type domain. A domain is not substituted for the complete named constituent class.'
  snapshot_sha256: eed5f734db9c4050435ed6cb8535ce9f93070c6fe1f91994ad5306e5b806e0fd
- evidence_id: micro-ipr-IPR028245-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028245/
  locator: Complete native entry metadata/type/description and flags [False]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR028245-retry.raw
  accessed_at: '2026-11-04T08:00:16.528719Z'
  support: supports
  summary: 'IPR028245: Eisosome component PIL1/LSP1; native type family. Native family
    identity/type and maintained example xrefs assessed; database prose is authority
    context, not a primary experiment.'
  snapshot_sha256: 48661066f7cb3d1fbe562bed3579aa2c4fcefca32c88c4af18443694274cfdf2
- evidence_id: micro-ipr-IPR028889
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028889/
  locator: Complete native entry metadata/type/description and flags [False, False];
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR028889.raw
  accessed_at: '2026-11-04T08:01:22.308275Z'
  support: supports
  summary: 'IPR028889: Ubiquitin specific protease USP, catalytic domain; native type
    domain. A domain is not substituted for the complete named constituent class.'
  snapshot_sha256: 987df85f85dc326871a2520fe381c81f16ba533afa9779bc00e37d969f3c602d
- evidence_id: micro-ipr-IPR037804
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037804/
  locator: Complete native entry metadata/type/description and flags [False, False];
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR037804.raw
  accessed_at: '2026-11-04T07:59:29.829286Z'
  support: supports
  summary: 'IPR037804: SAGA-associated factor 73; native type family. Native family
    identity/type and maintained example xrefs assessed; database prose is authority
    context, not a primary experiment.'
  snapshot_sha256: a57d32fbdc3ee041327bea0d8e2fbd36aaf8973b058da9a8b96b25031b899ead
- evidence_id: micro-ipr-IPR050185
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050185/
  locator: Complete native entry metadata/type/description and flags [True]; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/ipr-IPR050185.raw
  accessed_at: '2026-11-04T08:01:22.214136Z'
  support: supports
  summary: 'IPR050185: Ubiquitin carboxyl-terminal hydrolase; native type family.
    Broad ubiquitin carboxyl-terminal hydrolase family; description is flagged LLM-generated
    and is excluded as biological support. Native metadata does not establish exact
    Ubp8 identity.'
  snapshot_sha256: 5bfe72e631d777b27d95335c387204030e37e00942bce6cb49172853bdad88d6
- evidence_id: micro-meta-10.1016_j.jbc.2021.100671
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jbc.2021.100671%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1016_j.jbc.2021.100671.raw
  accessed_at: '2026-11-04T07:59:30.108678Z'
  support: supports
  summary: PMID 33864814; DOI 10.1016/j.jbc.2021.100671; SAGA and SAGA-like SLIK transcriptional
    coactivators are structurally and biochemically equivalent.. Primary study metadata/abstract
    tier; separately cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: 5fa300918e7c20da7493b545d9a48b10aa0a9b66d5152cd27718a5f2f660040e
- evidence_id: micro-meta-10.1016_j.jmb.2004.10.030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jmb.2004.10.030%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1016_j.jmb.2004.10.030.raw
  accessed_at: '2026-11-04T07:59:30.151477Z'
  support: supports
  summary: PMID 15567415; DOI 10.1016/j.jmb.2004.10.030; The crystal structure of
    E.coli 1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with
    the antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed
    enzyme conformation.. Primary study metadata/abstract tier; separately cited body
    evidence is used only where genuinely retrieved.
  snapshot_sha256: 40f98c43091f3955c3825b1189eb99859bff7fecc59f0527e7fb54b2cbc3093b
- evidence_id: micro-meta-10.1038_nature04472
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature04472%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1038_nature04472.raw
  accessed_at: '2026-11-04T07:59:30.210776Z'
  support: supports
  summary: PMID 16496001; DOI 10.1038/nature04472; Eisosomes mark static sites of
    endocytosis.. Primary study metadata/abstract tier; separately cited body evidence
    is used only where genuinely retrieved.
  snapshot_sha256: 6133a644af211a7d7496ceeb59e48af203f6f6801eca5b79aed7db126d614c95
- evidence_id: micro-meta-10.1038_nsmb.1548
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb.1548%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1038_nsmb.1548.raw
  accessed_at: '2026-11-04T07:59:32.510997Z'
  support: supports
  summary: PMID 19151722; DOI 10.1038/nsmb.1548; Structural characterization of Tip20p
    and Dsl1p, subunits of the Dsl1p vesicle tethering complex.. Primary study metadata/abstract
    tier; separately cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: 9640f05b709d305b4ed8cadaec3f9fdff023053acd50148af4b129b0f97e301f
- evidence_id: micro-meta-10.1038_s41586-020-1933-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-020-1933-5%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1038_s41586-020-1933-5.raw
  accessed_at: '2026-11-04T07:59:30.508161Z'
  support: supports
  summary: PMID 31969703; DOI 10.1038/s41586-020-1933-5; Structure of the transcription
    coactivator SAGA.. Primary study metadata/abstract tier; separately cited body
    evidence is used only where genuinely retrieved.
  snapshot_sha256: 91b0d916bc94f838c994fb869eed47a9549dc7a4a4b0d6f96ebd537765611c44
- evidence_id: micro-meta-10.1074_jbc.M110.215327
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.215327%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1074_jbc.M110.215327.raw
  accessed_at: '2026-11-04T07:59:30.508117Z'
  support: supports
  summary: 'PMID 21550981; DOI 10.1074/jbc.m110.215327; The Dsl1 protein tethering
    complex is a resident endoplasmic reticulum complex, which interacts with five
    soluble NSF (N-ethylmaleimide-sensitive factor) attachment protein receptors (SNAREs):
    implications for fusion and fusion regulation.. Primary study metadata/abstract
    tier; separately cited body evidence is used only where genuinely retrieved.'
  snapshot_sha256: 9107077d7523dd7078d4b8ef349acbf7bab2257854a95ba646e7b06247923547
- evidence_id: micro-meta-10.1083_jcb.201104040
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201104040%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1083_jcb.201104040.raw
  accessed_at: '2026-11-04T07:59:30.563491Z'
  support: supports
  summary: PMID 22123866; DOI 10.1083/jcb.201104040; Eisosome proteins assemble into
    a membrane scaffold.. Primary study metadata/abstract tier; separately cited body
    evidence is used only where genuinely retrieved.
  snapshot_sha256: 799f521a79aef5637485b8c1add6913230a4107dc806227b88cc3a10836cae6b
- evidence_id: micro-meta-10.1091_mbc.e05-01-0056
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e05-01-0056%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1091_mbc.e05-01-0056.raw
  accessed_at: '2026-11-04T07:59:30.625347Z'
  support: supports
  summary: PMID 15958492; DOI 10.1091/mbc.e05-01-0056; Dsl1p, Tip20p, and the novel
    Dsl3(Sec39) protein are required for the stability of the Q/t-SNARE complex at
    the endoplasmic reticulum in yeast.. Primary study metadata/abstract tier; separately
    cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: da90f24b2efbfae30694910158312fb280985b7bbef86d7bf0b32f53288204f4
- evidence_id: micro-meta-10.1091_mbc.e08-03-0313
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e08-03-0313%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1091_mbc.e08-03-0313.raw
  accessed_at: '2026-11-04T07:59:30.720001Z'
  support: supports
  summary: PMID 19037108; DOI 10.1091/mbc.e08-03-0313; Pil1 controls eisosome biogenesis..
    Primary study metadata/abstract tier; separately cited body evidence is used only
    where genuinely retrieved.
  snapshot_sha256: fefcaa20a583151076c2cd4b74bfce14dce2fc8d2f803e4a033bdcee19d5d090
- evidence_id: micro-meta-10.1091_mbc.e10-12-1021
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e10-12-1021%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1091_mbc.e10-12-1021.raw
  accessed_at: '2026-11-04T07:59:30.752184Z'
  support: supports
  summary: PMID 21593205; DOI 10.1091/mbc.e10-12-1021; The eisosome core is composed
    of BAR domain proteins.. Primary study metadata/abstract tier; separately cited
    body evidence is used only where genuinely retrieved.
  snapshot_sha256: 803b9da68e86ce5a9684bf9004087c3960fb9aa878fdbf8db94353a96467f25a
- evidence_id: micro-meta-10.1101_gad.1144003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144003%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-10.1101_gad.1144003.raw
  accessed_at: '2026-11-04T07:59:30.875288Z'
  support: supports
  summary: PMID 14563679; DOI 10.1101/gad.1144003; Transcriptional activation via
    sequential histone H2B ubiquitylation and deubiquitylation, mediated by SAGA-associated
    Ubp8.. Primary study metadata/abstract tier; separately cited body evidence is
    used only where genuinely retrieved.
  snapshot_sha256: 6ebe9a490205ef8555b224a8ce3ab746e91902c39a344f7e3bbe9e4a2bb15409
- evidence_id: micro-meta-11493604
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11493604+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-11493604.raw
  accessed_at: '2026-11-04T07:59:31.133807Z'
  support: supports
  summary: PMID 11493604; DOI 10.1074/jbc.m105833200; The coatomer-interacting protein
    Dsl1p is required for Golgi-to-endoplasmic reticulum retrieval in yeast.. Primary
    study metadata/abstract tier; separately cited body evidence is used only where
    genuinely retrieved.
  snapshot_sha256: 7d7d541e6300283c11aa786be3f36814ce46bc2f87339f2fdbac5b725a52c432
- evidence_id: micro-meta-11739780
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11739780+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-11739780.raw
  accessed_at: '2026-11-04T07:59:33.016690Z'
  support: supports
  summary: PMID 11739780; DOI 10.1091/mbc.12.12.3783; Golgi-to-endoplasmic reticulum
    (ER) retrograde traffic in yeast requires Dsl1p, a component of the ER target
    site that interacts with a COPI coat subunit.. Primary study metadata/abstract
    tier; separately cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: b7b5e299d285e43b5a4f0a7c72e9ec60147392e9e98311d7c3d2558a1f997cb8
- evidence_id: micro-meta-11784867
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11784867+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-11784867.raw
  accessed_at: '2026-11-04T07:59:31.174833Z'
  support: supports
  summary: PMID 11784867; DOI 10.1128/mcb.22.3.927-934.2002; The Sur7p family defines
    novel cortical domains in Saccharomyces cerevisiae, affects sphingolipid metabolism,
    and is involved in sporulation.. Primary study metadata/abstract tier; separately
    cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: 7d396e59af51b3e33220a8f85a1b86a3b5152aaa4a1812809673b4f1f3f30fb4
- evidence_id: micro-meta-12469340
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12469340+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-12469340.raw
  accessed_at: '2026-11-04T07:59:33.458661Z'
  support: supports
  summary: 'PMID 12469340; DOI 10.1002/1615-9861(200212)2:12<1706::aid-prot1706>3.0.co;2-k;
    Subproteomics: identification of plasma membrane proteins from the yeast Saccharomyces
    cerevisiae.. Primary study metadata/abstract tier; separately cited body evidence
    is used only where genuinely retrieved.'
  snapshot_sha256: da0221d0d53eef3424a68cb1cd40b990f2ee711fe41d9a91c926b06e168d562b
- evidence_id: micro-meta-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-14562095.raw
  accessed_at: '2026-11-04T07:59:33.250539Z'
  support: supports
  summary: PMID 14562095; DOI 10.1038/nature02026; Global analysis of protein localization
    in budding yeast.. Primary study metadata/abstract tier; separately cited body
    evidence is used only where genuinely retrieved.
  snapshot_sha256: 2ca60d2255a2d3bbc82faa247ab30b1c6d1fee57858075f22a949bf82e01bf23
- evidence_id: micro-meta-15567415
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15567415+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-15567415.raw
  accessed_at: '2026-11-04T07:59:31.409704Z'
  support: supports
  summary: PMID 15567415; DOI 10.1016/j.jmb.2004.10.030; The crystal structure of
    E.coli 1-deoxy-D-xylulose-5-phosphate reductoisomerase in a ternary complex with
    the antimalarial compound fosmidomycin and NADPH reveals a tight-binding closed
    enzyme conformation.. Primary study metadata/abstract tier; separately cited body
    evidence is used only where genuinely retrieved.
  snapshot_sha256: 1b57f38bcea4695d8f0bcc6f21f36c6f2005d023c500029422665a14cd3d5065
- evidence_id: micro-meta-15958492
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15958492+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-15958492.raw
  accessed_at: '2026-11-04T07:59:31.467549Z'
  support: supports
  summary: PMID 15958492; DOI 10.1091/mbc.e05-01-0056; Dsl1p, Tip20p, and the novel
    Dsl3(Sec39) protein are required for the stability of the Q/t-SNARE complex at
    the endoplasmic reticulum in yeast.. Primary study metadata/abstract tier; separately
    cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: 621762e0e7aeb51cb436e96811d2926179ff967908fbf8d4d79fd41c6f6d9ed9
- evidence_id: micro-meta-16496001
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16496001+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-16496001.raw
  accessed_at: '2026-11-04T07:59:31.608255Z'
  support: supports
  summary: PMID 16496001; DOI 10.1038/nature04472; Eisosomes mark static sites of
    endocytosis.. Primary study metadata/abstract tier; separately cited body evidence
    is used only where genuinely retrieved.
  snapshot_sha256: 3144e772cba60c389f7b0eb3617969894e092b8b22e401bd740de774354a7c0c
- evidence_id: micro-meta-16855026
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16855026+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-16855026.raw
  accessed_at: '2026-11-04T07:59:31.621483Z'
  support: supports
  summary: PMID 16855026; DOI 10.1091/mbc.e06-02-0098; The mRNA export factor Sus1
    is involved in Spt/Ada/Gcn5 acetyltransferase-mediated H2B deubiquitinylation
    through its interaction with Ubp8 and Sgf11.. Primary study metadata/abstract
    tier; separately cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: 8a55d056f0b02ba399ae66206490fde8ae735d2fda8d6f580d40ceefef176a30
- evidence_id: micro-meta-20230609
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20230609+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-20230609.raw
  accessed_at: '2026-11-04T07:59:34.045907Z'
  support: supports
  summary: PMID 20230609; DOI 10.1186/1471-2121-11-19; A novel link between Sus1 and
    the cytoplasmic mRNA decay machinery suggests a broad role in mRNA metabolism..
    Primary study metadata/abstract tier; separately cited body evidence is used only
    where genuinely retrieved.
  snapshot_sha256: 2f7667ca712664cf0491e759e76b5f5213090c899a069a2d1a8ca32a7c79144e
- evidence_id: micro-meta-22932476
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22932476+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-22932476.raw
  accessed_at: '2026-11-04T07:59:31.774171Z'
  support: supports
  summary: PMID 22932476; DOI 10.1186/2045-3701-2-30; The nuclear localization of
    SWI/SNF proteins is subjected to oxygen regulation.. Primary study metadata/abstract
    tier; separately cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: cae6e53d04d26f86ff1d8844138ac6af9a0630cfeba30bc4392bfd1e0b3ea4b4
- evidence_id: micro-meta-25002088
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25002088+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-25002088.raw
  accessed_at: '2026-11-04T07:59:34.286414Z'
  support: context_only
  summary: 'PMID 25002088; DOI 10.1146/annurev-micro-091313-103507; Fungal membrane
    organization: the eisosome concept.. Douglas/Konopka is secondary review context
    only.'
  snapshot_sha256: 5a4ed54fa42ab87735f8ef2b8eb4b5f74fbca299d0a854ca78ea81fb34e11e42
- evidence_id: micro-meta-8334998
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8334998+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no body inferred;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meta-8334998.raw
  accessed_at: '2026-11-04T07:59:32.085021Z'
  support: supports
  summary: PMID 8334998; DOI 10.1002/j.1460-2075.1993.tb05944.x; The TIP1 gene of
    Saccharomyces cerevisiae encodes an 80 kDa cytoplasmic protein that interacts
    with the cytoplasmic domain of Sec20p.. Primary study metadata/abstract tier;
    separately cited body evidence is used only where genuinely retrieved.
  snapshot_sha256: 3d72f598b1f4466c7398326b7fb5ccff094461549c31ab6a5bb7db352aaf8464
- evidence_id: micro-tripathi
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2635920.1/PMC2635920.1.xml
  locator: Introduction S1, Results S5 and S6, Figure 4 caption, Methods S10 protein
    production and S13 binding assays; first three S7 paragraphs only; no figure pixels,
    movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/tripathi.raw
  accessed_at: '2026-11-04T07:59:32.157117Z'
  support: supports
  summary: 'Purified recombinant yeast Dsl1 links Tip20 and Sec39: Sec39 does not
    bind Tip20 directly, and full-length proteins reconstitute a stoichiometric ternary
    complex. N/C contacts, domain mutants, growth phenotypes and reconstitution are
    distinct. No universal in-vivo absence conclusion.'
  snapshot_sha256: 05bf0e10f42a362b9df7b3440555a84208204ada617d4752fd34cdfa1de53fdf
- evidence_id: micro-wang
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6994259.1/PMC6994259.1.xml
  locator: Complete 13 direct main-body paragraphs; Methods S2 purification, S4 sample
    preparation, S5 image processing and S7 model building; no figure pixels, movies,
    supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/wang.raw
  accessed_at: '2026-11-04T08:00:16.410328Z'
  support: supports
  summary: Primary SAGA structural study supports the four-subunit DUB module, Sgf73
    N-terminal module incorporation and central core anchoring. CB010 preparation
    is not identical to all S288C example strains. Apo DUB low-resolution fit and
    nucleosome-bound map have different structural limits.
  snapshot_sha256: f7df057414f961aad482bd36ef03060cdbf1fb7bc0662f66fc03d12b3987f4ac
- evidence_id: micro-adamus
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8131915.1/PMC8131915.1.xml
  locator: Results sec1.1 purification, sec1.2 XL-MS, sec1.4 DUB activity, sec1.7
    EM and embedded Figures 1/2/6 captions; Methods sec3.1,3.4,3.11; no figure pixels,
    movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adamus.raw
  accessed_at: '2026-11-04T08:00:16.508955Z'
  support: supports
  summary: Primary SAGA/SLIK purification, mass spectrometry, cross-linking and activity
    support shared DUB composition/function in the tested yeast preparations. Low-resolution
    EM cannot resolve all orientations; Ub-AMC assay is not every physiological histone
    substrate.
  snapshot_sha256: 37a2586cc8ad87184b6b57c5dd7953fac862148066ece56614a58e780f3b01e9
- evidence_id: micro-karotki
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3257569.1/PMC3257569.1.xml
  locator: 'Complete main-body section indices 2,4,8,10,11,13,14,18,19: recombinant
    assembly, membrane binding, native purification/localization, Discussion and stated
    methods; no figure pixels, movies, supplementary files or atomic reanalysis; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/karotki.raw'
  accessed_at: '2026-11-04T08:00:16.405999Z'
  support: supports
  summary: Pil1/Lsp1 self-assembly and membrane scaffolding are directly supported.
    Native yeast cores contain both proteins; the paper leaves heterodimer versus
    mixed homodimer arrangement unresolved. W303/S288C native preparations and recombinant
    bacterial production remain distinct.
  snapshot_sha256: 9b777c1d5dcc235346ae3c398d9a77ca92b802e8541d61a2af4b5e43d7f1c3de
- evidence_id: micro-olivera
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3128537.1/PMC3128537.1.xml
  locator: 'Complete main-body section indices 2,3,4,5,8,9,12,16,17: structural modeling,
    BAR-domain tests, mutant organization, Discussion and stated methods; no figure
    pixels, movies, supplementary files or atomic reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/olivera.raw'
  accessed_at: '2026-11-04T08:00:16.436451Z'
  support: supports
  summary: Primary experiments support Pil1/Lsp1 BAR-like membrane interaction, tubulation
    and eisosome organization. Homology models, COS7 coexpression and yeast mutants
    are not a universally fixed native heterodimer or full assembly mechanism.
  snapshot_sha256: 454fef3bf22e2d7a766643c2ddbac9d6803bc6f3d9753877e74f8bb475d61d60
- evidence_id: micro-walther-html
  kind: primary_source
  reference: https://www.nature.com/articles/nature04472
  locator: Genuine publisher main article paragraphs 0–17 and included Figure 1–3
    text captions; no figure pixels, movies, supplementary files or atomic reanalysis;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/walther-html.raw
  accessed_at: '2026-11-04T08:00:17.238449Z'
  support: supports
  summary: Primary discovery paper supports immobile yeast assemblies, Pil1/Lsp1 copurification
    and Sur7 colocalization. Later morphology/membrane-domain work bounds the current
    stable-organization claim; early endocytosis interpretation is not promoted to
    a universal causal mechanism.
  snapshot_sha256: d3480753509158c14303ac4dbeba033c04a6f871c57f62dc5e151cef7c30c2b0
- evidence_id: micro-pdb-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1Q0Q
  locator: Complete entry identity, method/resolution and primary citation; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-entry.raw
  accessed_at: '2026-11-04T07:59:31.847418Z'
  support: supports
  summary: 1Q0Q is the deposited Dxr substrate/NADPH complex at 1.9 Angstrom, linked
    to PMID15567415; the paper title emphasizing fosmidomycin does not make this deposition
    an inhibitor-only structure.
  snapshot_sha256: cd09cbe75bd95d779c6a1c3f8442aab0c4de5475703e856330974b088b1da0dc
- evidence_id: micro-pdb-polymer
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1Q0Q/1
  locator: Entity 1 source organism, expression host, chain identifiers and SIFTS
    reference; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-polymer.raw
  accessed_at: '2026-11-04T07:59:31.915448Z'
  support: supports
  summary: Dxr entity maps P45568; source E. coli species562, recombinant expression
    BL21(DE3), two protein chains A/B. Reference K12 identity is not an assertion
    that every experiment used that strain.
  snapshot_sha256: 699e8d714ab73399c4580e0825562da4dc24a8248a27e4772c41165ec291add6
- evidence_id: micro-pdb-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1Q0Q/1
  locator: Assembly 1 author/software assignments, protein count and symmetry; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-assembly.raw
  accessed_at: '2026-11-04T07:59:31.989533Z'
  support: supports
  summary: Author/software-supported C2 dimer with two protein copies. Additional
    ligand asym IDs are not additional protein subunits.
  snapshot_sha256: a652f9f8739e0d113e77502e95fe955aaa57a69fbcd2ddf43f182608655191d2
- evidence_id: micro-pdb-ligand-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/2
  locator: Complete nonpolymer entity 2; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-ligand-2.raw
  accessed_at: '2026-11-04T08:00:17.832368Z'
  support: supports
  summary: DXP substrate is present, two molecules.
  snapshot_sha256: 2e9d2a9da7a3640e0d1f73b91adcbd16e214a1913dd02f38795e90e3fdb97468
- evidence_id: micro-pdb-ligand-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/nonpolymer_entity/1Q0Q/3
  locator: Complete nonpolymer entity 3; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/pdb-ligand-3.raw
  accessed_at: '2026-11-04T08:00:17.899959Z'
  support: supports
  summary: NDP is reduced NADPH, two molecules; deposition supports the canonical
    substrate/cofactor note.
  snapshot_sha256: 32dd31ca5a3bd0c7f58e8a0c822498cd0149e957ad086a41cf2105b93939760a
- evidence_id: micro-access-meiringer
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3137077.1/PMC3137077.1.xml
  locator: Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meiringer.receipt.json
  accessed_at: '2026-11-04T07:59:31.911636Z'
  support: context_only
  summary: Actual HTTP 404; failed route or challenge HTML, not an inspected primary
    article body. Successful metadata/abstract or separate primary routes are separately
    recorded.
  snapshot_sha256: eba597b42bbf22e936497c7791f48074bbdd72623ba5cef4c4ed7f5e95f20bd2
- evidence_id: micro-access-meiringer-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3137077/
  locator: Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meiringer-html.receipt.json
  accessed_at: '2026-11-04T08:00:15.934201Z'
  support: context_only
  summary: Actual HTTP 200; failed route or challenge HTML, not an inspected primary
    article body. Successful metadata/abstract or separate primary routes are separately
    recorded.
  snapshot_sha256: 7e968023b0aec962bb8cbf329be0ecda3e3a22ae657499e48a8cac038d205a6c
- evidence_id: micro-access-meiringer-legacy
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3137077/
  locator: Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/meiringer-legacy.receipt.json
  accessed_at: '2026-11-04T08:01:21.949040Z'
  support: context_only
  summary: Actual HTTP 200; failed route or challenge HTML, not an inspected primary
    article body. Successful metadata/abstract or separate primary routes are separately
    recorded.
  snapshot_sha256: eed1e909c8bc9b9b076f48705efa37b859058e8598eca416a3e32c8c67ef0c06
- evidence_id: micro-access-kraynack-legacy
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1196311/
  locator: Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/kraynack-legacy.receipt.json
  accessed_at: '2026-11-04T08:01:21.940729Z'
  support: context_only
  summary: Actual HTTP 200; failed route or challenge HTML, not an inspected primary
    article body. Successful metadata/abstract or separate primary routes are separately
    recorded.
  snapshot_sha256: cec13def5a3bdac47edd439067746483f8873add09d7edae6fdf1e94a53bdcef
- evidence_id: micro-access-henry-legacy
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC280615/
  locator: Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/henry-legacy.receipt.json
  accessed_at: '2026-11-04T08:01:21.934446Z'
  support: context_only
  summary: Actual HTTP 200; failed route or challenge HTML, not an inspected primary
    article body. Successful metadata/abstract or separate primary routes are separately
    recorded.
  snapshot_sha256: 625c1ea1e9ab6ad452d025a1dc88dc77891f27f422ed8f80a5bd64993de82f93
- evidence_id: micro-access-adapter-genes
  kind: validation
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/genes
  locator: Actual response status/content and retrieval receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-genes.receipt.json
  accessed_at: '2026-11-04T07:59:23.194611Z'
  support: context_only
  summary: Actual HTTP 200; misrouted application HTML, not the requested gene data.
  snapshot_sha256: 372db3e7392f2779f2d46aef5c4f7786399705355520de485f6c37ee92bf0478
- evidence_id: micro-historical-3-micro53-douglas2014-publisher
  kind: validation
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507
  locator: Original retained observation reviews/structured/20261022T062450Z-eisosome-audit/review.yaml
    evidence micro53-douglas2014-publisher; historical fetch, not newly refetched
  accessed_at: '2026-10-21T10:00:34.701299Z'
  support: context_only
  summary: Historical publisher HTTP403 challenge explicitly provided no article body.
    Original authority kind is corrected to validation/context_only; original URL/time/hash
    retained without alleging false access.
  snapshot_sha256: b1f4711f6f03e0c79150315105c200a454323178003dcc32b35f9bb6d4e03e1d
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T07:59:23.235917Z'
  support: context_only
  summary: Twenty returned organism rows and 28 organism/dataset entries inspected.
    E. coli precise1k is covered; no yeast or other eukaryotic dataset appears in
    this complete response. Catalogue absence is not biological absence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB complete /api/datasets response at 2026-11-04T07:59:23.235917Z;
    all20 organism rows/28 pairs; exact Saccharomyces/E.coli host matching only, not
    a universal future-coverage claim.
- evidence_id: micro-adapter-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete e_coli/precise1k dataset metadata; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-meta.raw
  accessed_at: '2026-11-04T07:59:23.785789Z'
  support: context_only
  summary: Five strains BW25113, DGF-298, GMOS, MG1655 and W3110; 201 modules, 1,035
    samples, 518 conditions and 4,257 reference genes. Not a matched claim for every
    recombinant preparation or species.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-adapter-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 module identifiers/names/metadata; generated summaries excluded;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-modules.raw
  accessed_at: '2026-11-04T07:59:23.197515Z'
  support: context_only
  summary: Complete dataset module inventory establishes the bounded search population;
    no expression activity contrast or inferred binding/formation claim.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: micro-adapter-dxr-memberships
  kind: search
  reference: https://imodulondb.org/api/genes/b0173/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 b0173 membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-dxr-memberships.raw
  accessed_at: '2026-11-04T08:00:17.766830Z'
  support: context_only
  summary: 'Dxr b0173 has one thresholded hit: UC-2/module167, weight0.061854521,
    threshold0.042864802; its functional annotation is Unknown. Other200 nonhits do
    not imply absence or dispensability.'
  snapshot_sha256: 2bafb47e7718278dc2ce9e20e810b31744f853d98c5ba4939efabc74be769224
  search_scope: Official iModulonDB literal https://imodulondb.org/api/genes/b0173/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T08:00:17.766830Z; e_coli/precise1k exact maintained native locus
    b0173, all201 returned rows. No all-alias, historical or universal-negative inference.
- evidence_id: micro-adapter-gene-dxr
  kind: search
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&search=b0173&limit=5000
  locator: Complete returned 4,257 reference-gene rows; exact b0173 identity join;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-gene-dxr.raw
  accessed_at: '2026-11-04T08:06:40.792344Z'
  support: context_only
  summary: Endpoint returned the complete 4,257-gene table despite search parameter.
    Exact b0173 row is dxr/P45568, matching the maintained example. Only the bounded
    identity join is used, not a claim that every unrelated gene was scientifically
    assessed.
  snapshot_sha256: db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27
  search_scope: Official iModulonDB literal https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&search=b0173&limit=5000
    at 2026-11-04T08:06:40.792344Z; requested search=b0173, limit5000; actual4257
    rows parsed, exact gene_id b0173 selected. Default50-row preliminary page was
    not treated as exhaustive.
- evidence_id: micro-adapter-module167
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/167
  locator: Module167 metadata, all96 member IDs/weights and threshold; activities/AI
    summary excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-module167.raw
  accessed_at: '2026-11-04T08:06:40.763165Z'
  support: context_only
  summary: UC-2 has Unknown function/regulator, 96 members and threshold0.042864802.
    Membership corroborates the exact Dxr hit without providing a mechanistic interpretation.
  snapshot_sha256: 49c7e478867c20e407e8929c8a92872f8eeb679c4a835f5344b90ba5bad34292
- evidence_id: micro-adapter-module167-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/167/genes
  locator: All96 member identity/weight rows and threshold; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/adapter-module167-genes.raw
  accessed_at: '2026-11-04T08:06:40.771531Z'
  support: context_only
  summary: b0173 dxr/P45568 has weight0.061854521 and true membership. Complete membership
    IDs match module metadata. This is computational expression context, not complex
    stoichiometry, formation or essentiality.
  snapshot_sha256: cd9b96081fad9fd906870f03c736d6a152bb04c3927ad7c4c910a5b5884c69fb
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical 2026-11-03T00:49:00.848907–00:49:00.863225Z receipt
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical runner unavailable/exit1 permission limitation; no fresh runner
    invocation. Current official direct-source catalogue/gene/module fallback is separately
    documented.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-dsl1_nzr_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:35.561623Z'
  support: supports
  summary: Actual exit0; 3 reviewed maintained examples and 3 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: 298f3bfbfaf4b16b8dca9801539cc891f13fe1a992dab5115e576cd4b9fd0497
- evidence_id: micro-native-dsl1_nzr_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-causal.log
    SHA256 087c7ae1c1ed5570e68b1849441b8171b6fc5520408fe4812cd3c9d4cd6d205a
  accessed_at: '2026-11-04T07:56:36.015697Z'
  support: supports
  summary: Actual exit0; 3 reviewed maintained examples and 3 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: 2f9fd7138d4edb706b9c8bedd1c10536d0e90aee130855cf0110880e04639860
- evidence_id: micro-native-dubm_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:37.188415Z'
  support: supports
  summary: Actual exit0; 4 reviewed maintained examples and 4 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: 9c5e0912ae7cfcd006e5706c3878ff2f8d3f55ec16c63b30af8c1f734d8a94aa
- evidence_id: micro-native-dubm_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-causal.log
    SHA256 41ef97ef6e5f7ed9b222fedc877f99f969f29044d849f5f84419f75ca162120e
  accessed_at: '2026-11-04T07:56:37.656482Z'
  support: supports
  summary: Actual exit0; 4 reviewed maintained examples and 4 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: c4a325c657dc38e5501a850d843147f62e27197bc9509ff7100e1ece5b173c53
- evidence_id: micro-native-dxr_protein_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:38.906867Z'
  support: supports
  summary: Actual exit0; 1 reviewed maintained examples and 1 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: 3842f4931c398ec3b1e7d4ed74e728586c1e0ee75260602b33c7c574d95445d2
- evidence_id: micro-native-dxr_protein_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-causal.log
    SHA256 df2ee219a494b4e317e88c9b090a533138fc496c62bc029f1baba3b3c92f069c
  accessed_at: '2026-11-04T07:56:39.347400Z'
  support: supports
  summary: Actual exit0; 1 reviewed maintained examples and 1 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: fa04f5575e07321da81b222949dd0d8752e138e0f11948b7c48dc4592412a110
- evidence_id: micro-native-eisosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:40.501675Z'
  support: supports
  summary: Actual exit0; 3 reviewed maintained examples and 2 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: 9b11efe4e11db2daa5a1efc6aae93a1a2fb1dcb4c49ba654cdc887c28ee66e8f
- evidence_id: micro-native-eisosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-causal.log
    SHA256 b0e108f81d2b02fa358798328d9b302fd746704f610e9c3665ab02ca281b9d99
  accessed_at: '2026-11-04T07:56:40.936084Z'
  support: supports
  summary: Actual exit0; 3 reviewed maintained examples and 2 COVERED typed protein
    nodes; no partial or unanchored typed nodes in this assigned record. This verifies
    implemented identity/xref coverage, not complete biology or exact family scope.
  snapshot_sha256: 8c5684259d0b597df42d08b662e12cea7fa714086094079305c26a5339cd4370
- evidence_id: plaque-curation
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-field-guide
  kind: authority
  reference: docs/SCHEMA.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-protein-skill
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-graph-skill
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: plaque-review-contract
  kind: authority
  reference: docs/record-reviews.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: plaque-structure-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-agents
  kind: authority
  reference: AGENTS.md
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
- evidence_id: plaque-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Frozen current policy/schema; relevant component identity, grounding, source
    applicability, formation, graph and append-only historical discussion rules
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Native review and modelling rules; formation differs from viability, optional
    protein examples are not mandatory, current evidence must be scoped, and historical
    rationale is preserved rather than rewritten.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: plaque-record-4
  kind: record_content
  reference: data/structures/other/ejectisome.yaml
  locator: Complete current record including definition, components, taxa, examples,
    graph, discussions and history
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: supports
  summary: Current bytes independently read and unchanged from the original frozen
    input; no record edits or status promotion.
  snapshot_sha256: 1ae5e8bacf85f2f83a40e9b76f75ac829ccf490bf1765498abeb2efa3be829a8
- evidence_id: plaque-original-4-yaml
  kind: prior_review
  reference: reviews/structured/20261022T062451Z-ejectisome-audit/review.yaml
  locator: Complete immutable original; frozen inputs, checks, scientific assessments,
    findings, actions and limitations
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Historical review independently reassessed. Historical commands and access
    timestamps are not represented as current executions.
  snapshot_sha256: da8eef14b223c9cc319915c9a36cba41c42f0ddc25567f6ad3de77748df1d224
- evidence_id: plaque-original-4-md
  kind: prior_review
  reference: reviews/structured/20261022T062451Z-ejectisome-audit/review.md
  locator: Complete immutable original; frozen inputs, checks, scientific assessments,
    findings, actions and limitations
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Historical review independently reassessed. Historical commands and access
    timestamps are not represented as current executions.
  snapshot_sha256: 136edde8922d26807cfee2ccf559c82db670d90bc1c99c75e2a8af7e51fc753f
- evidence_id: plaque-record-5
  kind: record_content
  reference: data/structures/other/elg1_rfc_like_complex.yaml
  locator: Complete current record including definition, components, taxa, examples,
    graph, discussions and history
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: supports
  summary: Current bytes independently read and unchanged from the original frozen
    input; no record edits or status promotion.
  snapshot_sha256: 15926e2b4d166dd9d443b67080b160309d5d9bf7fa3c7db299ab0d386f509837
- evidence_id: plaque-original-5-yaml
  kind: prior_review
  reference: reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.yaml
  locator: Complete immutable original; frozen inputs, checks, scientific assessments,
    findings, actions and limitations
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Historical review independently reassessed. Historical commands and access
    timestamps are not represented as current executions.
  snapshot_sha256: 2898cc2d84349c73ed45e709954187c571d78a453216ca5bf959d2c4cf75bd9e
- evidence_id: plaque-original-5-md
  kind: prior_review
  reference: reviews/structured/20261022T062451Z-elg1-rfc-like-complex-audit/review.md
  locator: Complete immutable original; frozen inputs, checks, scientific assessments,
    findings, actions and limitations
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Historical review independently reassessed. Historical commands and access
    timestamps are not represented as current executions.
  snapshot_sha256: 61ee1112cfb7ddbf12dffe77bfdf5118b87b1f149a70410a505feb0703a13acb
- evidence_id: plaque-record-6
  kind: record_content
  reference: data/structures/other/elongator_holoenzyme_complex.yaml
  locator: Complete current record including definition, components, taxa, examples,
    graph, discussions and history
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: supports
  summary: Current bytes independently read and unchanged from the original frozen
    input; no record edits or status promotion.
  snapshot_sha256: 3071ca4a7c4adde264f84e0613da05118ef23a2d9ffcfbdd74a37897ba8f3c1d
- evidence_id: plaque-original-6-yaml
  kind: prior_review
  reference: reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.yaml
  locator: Complete immutable original; frozen inputs, checks, scientific assessments,
    findings, actions and limitations
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Historical review independently reassessed. Historical commands and access
    timestamps are not represented as current executions.
  snapshot_sha256: 54f6e4272ddcc3727da6820b7a4db4dbc4ac842c8e43f78bb8974ac8c5c6d3de
- evidence_id: plaque-original-6-md
  kind: prior_review
  reference: reviews/structured/20261022T062452Z-elongator-holoenzyme-complex-audit/review.md
  locator: Complete immutable original; frozen inputs, checks, scientific assessments,
    findings, actions and limitations
  accessed_at: '2026-11-04T08:10:31.021243Z'
  support: context_only
  summary: Historical review independently reassessed. Historical commands and access
    timestamps are not represented as current executions.
  snapshot_sha256: cdad4b630c21247468aefd0792344bea501bd06ae9cbc64c5fefd557cc730a16
- evidence_id: plaque-input-original-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/input-original-proof.json
  locator: All49 current source/worktree inputs;41 original frozen-input occurrences;3
    native original validations and deterministic Markdown comparisons
  accessed_at: '2026-11-04T08:02:51.011740Z'
  support: supports
  summary: All49 current frozen inputs and41 historical occurrences match. All3 original
    YAML files validate and reproduce their committed Markdown exactly; all3 assigned
    target hashes are unchanged.
  snapshot_sha256: 61e84bc3c64e3fbf3ab493d78b65475b128f7b2fec509c01f7d319752993903d
- evidence_id: plaque-native-ejectisome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-verify-receipt.json
  locator: Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-verify.log;
    stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:41.372528Z'
  support: supports
  summary: Exit0. Zero protein_examples; one GENE_OR_PROTEIN ejectisin node is NO_GENE_SYMBOLS.
    This honest diagnostic is not an optional-example defect. Generic verify success
    establishes identifier consistency, not assembly or necessity.
  snapshot_sha256: 96154855d5f0003870fbaf8fbe618860162f46c154a040ecc9f8da0341dd99b5
- evidence_id: plaque-native-ejectisome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-causal-receipt.json
  locator: Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-causal.log;
    stdout SHA256 dc516d6ef3fa342c638df335b97de8ae4de12b60f9910f0eb3e1305d4856adf8
  accessed_at: '2026-11-04T07:56:41.816643Z'
  support: supports
  summary: Exit0. Zero protein_examples; one GENE_OR_PROTEIN ejectisin node is NO_GENE_SYMBOLS.
    This honest diagnostic is not an optional-example defect. Generic verify success
    establishes identifier consistency, not assembly or necessity.
  snapshot_sha256: b43aad42aa8675e2108284abec0f64ff27878bbe2b609d219dee119f794f93b3
- evidence_id: plaque-native-elg1_rfc_like_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-verify.log;
    stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:43.057231Z'
  support: supports
  summary: Exit0. Five reviewed protein_examples; five typed protein nodes are COVERED.
    Generic verify success establishes identifier consistency, not assembly or necessity.
  snapshot_sha256: cf49b8a6659befdd34aaf21b72fcfc1ed232421eb91858737a4a2b1a0cd8ba43
- evidence_id: plaque-native-elg1_rfc_like_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-causal.log;
    stdout SHA256 cb8359551acfa102a3c4984a50cf8f76ee180be1c9809dd6edf16b50c1432672
  accessed_at: '2026-11-04T07:56:43.500731Z'
  support: supports
  summary: Exit0. Five reviewed protein_examples; five typed protein nodes are COVERED.
    Generic verify success establishes identifier consistency, not assembly or necessity.
  snapshot_sha256: 35355b80f3e57202313af6704f3b89883b7de90a784e9868f59dc5866f92eb05
- evidence_id: plaque-native-elongator_holoenzyme_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-verify.log;
    stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:56:44.725933Z'
  support: supports
  summary: Exit0. Six reviewed protein_examples; six typed protein nodes are COVERED.
    Generic verify success establishes identifier consistency, not assembly or necessity.
  snapshot_sha256: 687b644e78799a838909875f9a5b004fec9162820c3fecac705cfdeaa273f7b3
- evidence_id: plaque-native-elongator_holoenzyme_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-causal.log;
    stdout SHA256 29a516440ea13c22756b229da3ae60ec5478f31193cc9d8912c5317484dd5a63
  accessed_at: '2026-11-04T07:56:45.178098Z'
  support: supports
  summary: Exit0. Six reviewed protein_examples; six typed protein nodes are COVERED.
    Generic verify success establishes identifier consistency, not assembly or necessity.
  snapshot_sha256: 8eac08b75870cb5bd01086c772c4a5ddc2901b719ba335716e2916823baff2ab
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043231,GO:0031391,GO:0032991,GO:0061860,GO:0033588,GO:0140535,GO:1902494,GO:0002097
  locator: 'Complete eight-term response: GO0043231,0031391,0032991,0061860,0033588,0140535,1902494,0002097;
    definitions and typed children/relations, distinguishing is_a from capability;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/go.raw'
  accessed_at: '2026-11-04T08:00:03.400627Z'
  support: supports
  summary: Current GO supports the native identities, protein-complex and functional
    hierarchy. GO0033588 still uses the older heterohexamer/two-heterotrimer wording;
    accurate quotation does not remove the source-supported stoichiometry conflict.
  snapshot_sha256: 147d0fbb20d3f6e682bbf2e4d54823235c1ff0f1b2ac14aae798754de8b6224f
- evidence_id: plaque-go-elg1-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031391/ancestors?relations=is_a
  locator: Complete GO0031391 ancestors restricted to is_a; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/go-elg1-ancestors.raw
  accessed_at: '2026-11-04T08:00:03.400938Z'
  support: supports
  summary: The exact is_a ancestor response supports Elg1 RFC-like class hierarchy;
    it is not evidence of direct parthood.
  snapshot_sha256: 12150b976a9de7f4ea1a19f53adacbb8e341455439e10514552d6e02513c47f5
- evidence_id: plaque-go-ejectisome-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=ejectisome&limit=25
  locator: Complete returned exact keyword query; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/go-ejectisome-search.raw
  accessed_at: '2026-11-04T08:00:03.401140Z'
  support: supports
  summary: No result in this exact bounded GO name query; this does not exhaust all
    ontology synonyms or establish global absence. The minted identity is retained.
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
  search_scope: QuickGO ontology search; query=ejectisome; limit25; date 2026-11-04T08:00:03.401140Z;
    complete zero-result response; no synonym expansion or other ontology searched;
    database search, not a filesystem absence claim.
- evidence_id: plaque-tax-3027
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3027
  locator: 'Complete native ENA taxonomy response: exact ID, rank, name and lineage;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-3027.raw'
  accessed_at: '2026-11-04T08:00:03.401189Z'
  support: supports
  summary: Cryptophyceae class identity/rank; not a claim every species has the same
    ejectisin system.
  snapshot_sha256: f624d05f33982a22b2c682cfe868b67bdb16080e93877d3cf3182e2fb4760df7
- evidence_id: plaque-tax-3028
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3028
  locator: 'Complete native ENA taxonomy response: exact ID, rank, name and lineage;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-3028.raw'
  accessed_at: '2026-11-04T08:00:03.401235Z'
  support: supports
  summary: Chroomonas genus identity/rank; not an exact strain or species accession.
  snapshot_sha256: 66a4f54339d0093a3194b459eab928d75e9d6c5e11bd93c58d4d7586d08f8077
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: 'Complete native ENA taxonomy response: exact ID, rank, name and lineage;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-4932.raw'
  accessed_at: '2026-11-04T08:00:03.401273Z'
  support: supports
  summary: Saccharomyces cerevisiae species identity.
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: 'Complete native ENA taxonomy response: exact ID, rank, name and lineage;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/tax-559292.raw'
  accessed_at: '2026-11-04T08:00:03.401309Z'
  support: supports
  summary: S. cerevisiae S288C reference strain identity, distinct from experimental
    W303, BS1173 or BSY2369 preparations.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-pmid-21336864
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21336864+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-21336864.raw
  accessed_at: '2026-11-04T08:00:09.569724Z'
  support: supports
  summary: 'Rhiel and Westermann2012 primary abstract: discharged Chroomonas/Cryptomonas
    fragments and paracrystalline ultrastructure; no intact-organelle formation assay.'
  snapshot_sha256: 964898b6b0bfadf2a4bbde7fbdd0b227f686a63558cd18bb6f56155274899e79
- evidence_id: plaque-pmid-22868567
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22868567+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-22868567.raw
  accessed_at: '2026-11-04T08:00:10.073917Z'
  support: supports
  summary: 'Ammermann2013 primary abstract: small ejectisin polypeptides and a 20-residue
    N-terminal sequence correspondence; fragment reaggregation does not prove intact
    organelle formation.'
  snapshot_sha256: 62e73d543722dd4a973716309a27043c94afc4a01c0b6625cb02dea941bb1170
- evidence_id: plaque-pmid-14614842
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-14614842.raw
  accessed_at: '2026-11-04T08:00:10.197043Z'
  support: supports
  summary: Kim and MacNeill2003 secondary abstract only, RFC-like clamp-loader diversity
    context.
  snapshot_sha256: c9b9403c5f1e4600482e910459907ef878c2dd5b8ceb0453ae1b237dd60901d1
- evidence_id: plaque-pmid-23499004
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23499004+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-23499004.raw
  accessed_at: '2026-11-04T08:00:10.462567Z'
  support: supports
  summary: Kubota2013 primary abstract directly describes Elg1-dependent PCNA unloading,
    degron restoration and purified-complex unloading; full body/figures/Methods not
    inspected.
  snapshot_sha256: 0fbddcfc920c9a4c958a75e96ddc61efa7212c5af47c56fe97088d1eb7616ed0
- evidence_id: plaque-pmid-27664980
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A27664980+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-27664980.raw
  accessed_at: '2026-11-04T08:00:10.523161Z'
  support: supports
  summary: Kupiec2016 secondary review abstract only; genome-stability and PCNA-unloading
    context, not a separately inspected primary experiment.
  snapshot_sha256: 8e86d7b3a1c804701ca224741740d6e1de1730c3e96674863f043e7a493618f7
- evidence_id: plaque-pmid-11435442
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11435442+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-11435442.raw
  accessed_at: '2026-11-04T08:00:10.794735Z'
  support: supports
  summary: Winkler2001 primary abstract identifies six polypeptide species and two
    labile subcomplexes; not an invariant absolute six-copy holoenzyme measurement.
  snapshot_sha256: ed63e7092f27a819e7ae49facd3c950b2ec27e1838881f3128abc702aad14c25
- evidence_id: plaque-pmid-11689709
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11689709+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-11689709.raw
  accessed_at: '2026-11-04T08:00:11.013631Z'
  support: supports
  summary: Krogan and Greenblatt2001 primary abstract and bibliographic identity;
    main-body evidence is separately bounded below.
  snapshot_sha256: 0831a00ac3991cccea3f22d7430c6dc3b3df75da4682150ffdfef62be54499d4
- evidence_id: plaque-pmid-15769872
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15769872+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-15769872.raw
  accessed_at: '2026-11-04T08:00:11.112656Z'
  support: supports
  summary: Huang2005 primary abstract identifies Elongator-dependent wobble-uridine
    modification; catalytic-output loss is not assembly-essentiality evidence.
  snapshot_sha256: f104674a5ab1286c2ca8fed6bc022aae802f29bbc07fc97948220af860148627
- evidence_id: plaque-pmid-14562095
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-14562095.raw
  accessed_at: '2026-11-04T08:00:10.666210Z'
  support: supports
  summary: Huh2003 primary abstract establishes the GFP localisation survey provenance;
    individual protein images were not inspected.
  snapshot_sha256: 29fa7e6d8ea5e645642a360565a0b71b2fb9041aab05012b6826702cf86793b1
- evidence_id: plaque-pmid-15780940
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15780940+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-15780940.raw
  accessed_at: '2026-11-04T08:00:11.137508Z'
  support: supports
  summary: Rahl2005 primary abstract concerns Elp1/Sec2 and polarised exocytosis,
    not measured full Elongator assembly.
  snapshot_sha256: 61bfafe743080801ff38ee9a1fd9519f23b6548f4a9f6deb6c5814e5ed4a8ae3
- evidence_id: plaque-pmid-10024884
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10024884+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-10024884.raw
  accessed_at: '2026-11-04T08:00:11.300912Z'
  support: supports
  summary: Otero1999 primary abstract identifies early Elongator/polII transcription
    association; later functional scope is not replaced by this initial association.
  snapshot_sha256: 4bbaff5a1ecdae30180d136efd9bd0c3ef93085d9f3ee229d848b9373e8c5ff8
- evidence_id: plaque-pmid-24750273
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24750273+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED EXT_ID query; pageSize1/resultType core; full returned
    abstract and bibliography only, not linked full text; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/pmid-24750273.raw
  accessed_at: '2026-11-04T08:00:11.425577Z'
  support: supports
  summary: DiSanto2014 primary abstract describes Elp1 tRNA-binding/basic-region function,
    not a universal nuclear-localisation requirement.
  snapshot_sha256: d8b1eaf45efebc4e8a51ec3d2de23fe1e68f02f6c8ebfe26796d77028134558c
- evidence_id: plaque-rhiel-publisher
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/s00709-011-0267-4
  locator: Springer page title/authors/DOI/abstract and access notice; no primary
    body or image pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/rhiel-publisher.raw
  accessed_at: '2026-11-04T08:00:11.799455Z'
  support: supports
  summary: Current genuine publisher landing page exposes abstract and bibliography,
    with subscription access limits. It is not full article access.
  snapshot_sha256: 145f23851e70b54ac13b0102279a62592097f9e9fb6217923d2df3b94513b3a0
- evidence_id: plaque-ammermann-publisher
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/s00709-012-0440-4
  locator: Springer page title/authors/DOI/abstract and access notice; full body not
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-publisher.raw
  accessed_at: '2026-11-04T08:00:11.845900Z'
  support: supports
  summary: Current genuine publisher landing page exposes the primary abstract and
    bibliography; full paper is not available through this route.
  snapshot_sha256: 45611a483f26c82ad0ee9df436333f45dd2b7ac281f25141ea2e6c9f6de9792f
- evidence_id: plaque-ammermann-web1
  kind: primary_source
  reference: https://www.researchgate.net/publication/230622947_Ejectisins_Tough_and_tiny_polypeptides_are_a_major_component_of_cryptophycean_ejectisomes
  locator: 'Web-reader extraction lines45–390: title/bibliography, Introduction and
    culture/initial Methods text; saved provider response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-web1.json;
    provider crawl age retained, no native HTTP success invented'
  accessed_at: '2026-11-04T08:01:57Z'
  support: supports
  summary: Author-distributed primary text was inspected through the web reader. Introductory
    membrane/resting-ribbon statements cite older studies and are secondary context
    within this paper; cultures are Chroomonas LT and Cryptomonas S2/LT.
  snapshot_sha256: 4b9f0ae3743595d17b095c991bf2aca1363484a37224156343d2170400d53daf
- evidence_id: plaque-ammermann-web2
  kind: primary_source
  reference: https://www.researchgate.net/publication/230622947_Ejectisins_Tough_and_tiny_polypeptides_are_a_major_component_of_cryptophycean_ejectisomes
  locator: 'Web-reader extraction lines387–1099: fragment purification/reconstitution,
    TEM and sequence Methods; Results and text captions; saved provider response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-web2.json;
    provider crawl age retained, no native HTTP success invented'
  accessed_at: '2026-11-04T08:01:49Z'
  support: supports
  summary: The experiments concern detergent/Percoll-enriched fragments and reconstituted
    ejectisin filaments. Antibody and preparation controls support that bounded scope;
    figure pixels and the complete later sequence-alignment discussion were not inspected.
  snapshot_sha256: a5654a3d7fb056cf9bffe6c48afac8d5b9d3b95c1c730d4e8d0feae77d9a1747
- evidence_id: plaque-PMC5286391-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5286391/
  locator: Genuine NCBI legacy HTML; sec0003/0004/0007, text captions Figs1/2A/6/EV1/EV2/EV5;
    Methods sec0010/0011/0017. No figure pixels, raw MS, supplementary strain TableEV4
    or universal exact experimental S288C identity.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286391-legacy.raw
  accessed_at: '2026-11-04T08:00:56.575078Z'
  support: supports
  summary: 'Setiaputra2017 (online2016): native yeast Elongator has two Elp123 lobes
    and a majority single Elp456 hexameric ring. Elp1 deletion loses Elp2/3 association
    with FLAG-Elp4 while Elp456 persists; elp2 deletion retains other associations.
    Low-salt and added-ring conditions also allow double Elp456 loading, so fixed
    universal occupancy is unwarranted.'
  snapshot_sha256: dfddf6c198c3e5f85e5d203317f327473d2c35f2872ccc43cba373dc722a48c3
- evidence_id: plaque-PMC5286394-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5286394/
  locator: Genuine NCBI legacy HTML; sec0003/0004/0005, figure1/2 and EV2–4 text captions,
    Methods sec0012/0013. Yeast BS1173/BSY2369, 27/31Å negative stain and glutaraldehyde
    stabilization; no pixels or raw reconstruction reanalysis.; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286394-legacy.raw
  accessed_at: '2026-11-04T08:00:56.575475Z'
  support: supports
  summary: Dauden2017 (online2016) resolves two Elp123 copies with one asymmetrically
    bound Elp456 heterohexamer. Native yeast purification and negative-stain reconstructions
    support that preparation; recombinant E.coli is an expression host, not the natural
    record taxon.
  snapshot_sha256: f9740bc6c249217bae392a662d886afd18e56804afe684a50830771613d435ae
- evidence_id: plaque-PMC99985-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC99985/
  locator: Genuine NCBI legacy HTML; sec2/3 purification/strain Methods and Table1
    W303-1A background; sec7/8 and Fig1/2 text captions. No individual image-pixel
    interpretation or uninspected phenotypic sections.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC99985-legacy.raw
  accessed_at: '2026-11-04T08:00:56.575602Z'
  support: supports
  summary: Krogan2001 identifies six distinct proteins with roughly equimolar recovery
    and separable Elp123/456 associations. This inventory is not an absolute one-copy-per-protein
    determination of the complete assembly.
  snapshot_sha256: c70507bf01a3782c5603dca0b01a85e13aea29080b7aa654c695321dbff86185
- evidence_id: plaque-PMC1370732-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1370732/
  locator: Genuine NCBI legacy HTML; sec7/8 with Fig4 text caption; Methods sec21
    HPLC and sec22 UV crosslink/IP. No figure pixels or full strain Table2 inspection.;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC1370732-legacy.raw
  accessed_at: '2026-11-04T08:00:56.806430Z'
  support: supports
  summary: Huang2005 deletion/rescue and tRNA-nucleoside measurements support Elongator-dependent
    mcm5/ncm5 wobble modifications. Elp1/3 tRNA co-IP supports association; catalytic-output
    loss is not automatically failure to form the full complex.
  snapshot_sha256: e46a537b2f8936385fb248439de36c18e9dd15af86351e6465491c7743101d53
- evidence_id: plaque-PMC5286391-body
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5286391/?pdf=render
  locator: Actual retained transport response and adjacent receipt; HTTP200 Recaptcha
    for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate
    Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286391-body.raw
  accessed_at: '2026-11-04T08:00:11.638271Z'
  support: context_only
  summary: This route supplied access-control/challenge content, not readable primary
    article text. Successful alternative routes, if any, are separate observations
    with their own scope and time.
  snapshot_sha256: e30cf68b3d9187f681174a295ae38c788aba55c29199d8a4ea6f23a8cb17e27f
- evidence_id: plaque-PMC5286394-body
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5286394/?pdf=render
  locator: Actual retained transport response and adjacent receipt; HTTP200 Recaptcha
    for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate
    Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC5286394-body.raw
  accessed_at: '2026-11-04T08:00:11.685635Z'
  support: context_only
  summary: This route supplied access-control/challenge content, not readable primary
    article text. Successful alternative routes, if any, are separate observations
    with their own scope and time.
  snapshot_sha256: 2fc267e977076863eb53ffbb13d9c0e07d531ba9bd00125cbb6d9b57214a1de3
- evidence_id: plaque-PMC99985-body
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC99985/?pdf=render
  locator: Actual retained transport response and adjacent receipt; HTTP200 Recaptcha
    for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate
    Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC99985-body.raw
  accessed_at: '2026-11-04T08:00:11.726038Z'
  support: context_only
  summary: This route supplied access-control/challenge content, not readable primary
    article text. Successful alternative routes, if any, are separate observations
    with their own scope and time.
  snapshot_sha256: 821afe19f60939eb93d5efb77f48059398998628b754d5c0ee5fd5acefcddcc2
- evidence_id: plaque-PMC1370732-body
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1370732/?pdf=render
  locator: Actual retained transport response and adjacent receipt; HTTP200 Recaptcha
    for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate
    Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/PMC1370732-body.raw
  accessed_at: '2026-11-04T08:00:11.742335Z'
  support: context_only
  summary: This route supplied access-control/challenge content, not readable primary
    article text. Successful alternative routes, if any, are separate observations
    with their own scope and time.
  snapshot_sha256: 43e4c33d8ccdc1dc20a9a362a87ef5857af4fa54c7d9a6104e28b62b44d70426
- evidence_id: plaque-kubota-publisher
  kind: validation
  reference: https://www.cell.com/molecular-cell/fulltext/S1097-2765(13)00140-8
  locator: Actual retained transport response and adjacent receipt; HTTP200 Recaptcha
    for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate
    Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/kubota-publisher.raw
  accessed_at: '2026-11-04T08:00:11.889373Z'
  support: context_only
  summary: This route supplied access-control/challenge content, not readable primary
    article text. Successful alternative routes, if any, are separate observations
    with their own scope and time.
  snapshot_sha256: 54828c71f02a1fedefad33855673913b3147561606a0d4126b63bedbff050a59
- evidence_id: plaque-ammermann-rg
  kind: validation
  reference: https://www.researchgate.net/publication/230622947_Ejectisins_Tough_and_tiny_polypeptides_are_a_major_component_of_cryptophycean_ejectisomes
  locator: Actual retained transport response and adjacent receipt; HTTP200 Recaptcha
    for the four PMC pdf=render routes; HTTP403 for Kubota publisher/ResearchGate
    Terminal route; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ammermann-rg.raw
  accessed_at: '2026-11-04T08:00:56.984101Z'
  support: context_only
  summary: This route supplied access-control/challenge content, not readable primary
    article text. Successful alternative routes, if any, are separate observations
    with their own scope and time.
  snapshot_sha256: c61cf0a049f4de329d759a396de997c6b2e43ce4a6de471222d1e2bab7ab8908
- evidence_id: plaque-up-Q12050
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12050.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q12050.raw'
  accessed_at: '2026-11-04T08:00:03.401348Z'
  support: supports
  summary: Reviewed S288C tax559292 entry Q12050, exact locus YOR144C, matches the
    maintained ELG1 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: 82f625adf4ced51c38d16b0e5dfb77d4920b99307013c3271c34661f9749fece
- evidence_id: plaque-gene-ELG1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELG1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELG1.raw
  accessed_at: '2026-11-04T08:02:17.842860Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry Q12050;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: ac3aa052c25986d1d92b9f540c079b90ccfde30b602c1a2cc97d5d0eb41154f3
  search_scope: UniProt REST; query=(gene_exact:ELG1) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:17.842860Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-P40348
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40348.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P40348.raw'
  accessed_at: '2026-11-04T08:00:04.003153Z'
  support: supports
  summary: Reviewed S288C tax559292 entry P40348, exact locus YJR068W, matches the
    maintained RFC2 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: cd48db2abc9d05e4a2f8f7736b0aced77e8baa2465fb6a839d4f9e8ed95db94e
- evidence_id: plaque-gene-RFC2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC2.raw
  accessed_at: '2026-11-04T08:02:17.843174Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry P40348;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: 5d37684d32d00b6803a2cbe7289849926576cd3f08cc74f6dd6ee2b3c1821068
  search_scope: UniProt REST; query=(gene_exact:RFC2) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:17.843174Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-P38629
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38629.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P38629.raw'
  accessed_at: '2026-11-04T08:00:04.026610Z'
  support: supports
  summary: Reviewed S288C tax559292 entry P38629, exact locus YNL290W, matches the
    maintained RFC3 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: 057ded2799f8c2aaf4cd34a49b0bd062aae33e6e6aa9ab81ec59b7c7d74937dd
- evidence_id: plaque-gene-RFC3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC3.raw
  accessed_at: '2026-11-04T08:02:17.843277Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry P38629;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: a84d7bf13eddb61707649c22403a1d9540d4585cd07d07bb31fcbd5f54cff2c3
  search_scope: UniProt REST; query=(gene_exact:RFC3) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:17.843277Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-P40339
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40339.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P40339.raw'
  accessed_at: '2026-11-04T08:00:04.035644Z'
  support: supports
  summary: Reviewed S288C tax559292 entry P40339, exact locus YOL094C, matches the
    maintained RFC4 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: 09609fcf78c540ff8073114b66b849691895e1fc7de9e81219d81dc51fcc35d7
- evidence_id: plaque-gene-RFC4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC4.raw
  accessed_at: '2026-11-04T08:02:17.843348Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry P40339;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: e4ac27ef43308dc3dd4c47939cb4856e61e23e412f8815e785cfb8d758e80a5c
  search_scope: UniProt REST; query=(gene_exact:RFC4) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:17.843348Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-P38251
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38251.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P38251.raw'
  accessed_at: '2026-11-04T08:00:04.049458Z'
  support: supports
  summary: Reviewed S288C tax559292 entry P38251, exact locus YBR087W, matches the
    maintained RFC5 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: bebaced0b8314c495257a26b5d1357bde108a903ac25fc337c51d4970294ff06
- evidence_id: plaque-gene-RFC5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-RFC5.raw
  accessed_at: '2026-11-04T08:02:17.843400Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry P38251;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: 7cfa80c9ae09adeac609a00eb5e3ddcecb79fc26d7ce7848ce2f6f772cfcaabb
  search_scope: UniProt REST; query=(gene_exact:RFC5) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:17.843400Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-Q06706
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q06706.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q06706.raw'
  accessed_at: '2026-11-04T08:00:04.065695Z'
  support: supports
  summary: Reviewed S288C tax559292 entry Q06706, exact locus YLR384C, matches the
    maintained ELP1 instance. Primary name is IKI3 with ELP1 alias. Native SUBUNIT,
    FUNCTION, SIMILARITY, localisation and family cross-references were inspected;
    identity is not direct experimental assembly evidence.
  snapshot_sha256: ed56b6004eaf9bf52b23861b9d2f69e3082c16ab8c1f63d0f91a84900c036062
- evidence_id: plaque-gene-ELP1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP1.raw
  accessed_at: '2026-11-04T08:02:17.843438Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry Q06706;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: a6e6a3a1ba2f3a565750ac4a18c998265059a993118ce58de41efb6afa5af238
  search_scope: UniProt REST; query=(gene_exact:ELP1) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:17.843438Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-P42935
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P42935.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P42935.raw'
  accessed_at: '2026-11-04T08:00:04.121373Z'
  support: supports
  summary: Reviewed S288C tax559292 entry P42935, exact locus YGR200C, matches the
    maintained ELP2 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: f8112e6f19eca34cc83885fa7bd02a8e0395e2f1f44468086f63cf23baf26491
- evidence_id: plaque-gene-ELP2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP2.raw
  accessed_at: '2026-11-04T08:02:19.783055Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry P42935;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: b4202c8b44f7d33276db97da7dd2fd75dbb0decf1932e82921758facf67656c2
  search_scope: UniProt REST; query=(gene_exact:ELP2) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:19.783055Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-Q02908
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q02908.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q02908.raw'
  accessed_at: '2026-11-04T08:00:04.148327Z'
  support: supports
  summary: Reviewed S288C tax559292 entry Q02908, exact locus YPL086C, matches the
    maintained ELP3 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: e08c72b12b04708161c0088483f93b49e4969cc2ca5e8950b304df093a7555c4
- evidence_id: plaque-gene-ELP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP3.raw
  accessed_at: '2026-11-04T08:02:19.838738Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry Q02908;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: 0a7a5842879210a2d085bad21aea480ec09423091679f85e11a664bbc411a784
  search_scope: UniProt REST; query=(gene_exact:ELP3) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:19.838738Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-Q02884
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q02884.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q02884.raw'
  accessed_at: '2026-11-04T08:00:04.454225Z'
  support: supports
  summary: Reviewed S288C tax559292 entry Q02884, exact locus YPL101W, matches the
    maintained ELP4 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: 154d952b5407aae5695092525b624b93255182bfb80b92cb518cdecd617dfc81
- evidence_id: plaque-gene-ELP4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP4.raw
  accessed_at: '2026-11-04T08:02:21.018020Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry Q02884;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: 613dc657d854da99ba0656f663477e1ce712b05d697d680756c4a2ad52f21c56
  search_scope: UniProt REST; query=(gene_exact:ELP4) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:21.018020Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-P38874
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38874.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-P38874.raw'
  accessed_at: '2026-11-04T08:00:05.629172Z'
  support: supports
  summary: Reviewed S288C tax559292 entry P38874, exact locus YHR187W, matches the
    maintained ELP5 instance. Primary name is IKI1 with ELP5 alias. Native SUBUNIT,
    FUNCTION, SIMILARITY, localisation and family cross-references were inspected;
    identity is not direct experimental assembly evidence.
  snapshot_sha256: 3f8b3fd0ad4c2933dcd6ff52628428ee6a51999725295d97f1a1e01499fd7062
- evidence_id: plaque-gene-ELP5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP5.raw
  accessed_at: '2026-11-04T08:02:21.020450Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry P38874;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: 1d48c1cf088376671e6b0173fd323c2b52eefb23acb8646e4846b1d35487c178
  search_scope: UniProt REST; query=(gene_exact:ELP5) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:21.020450Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-up-Q04868
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04868.json
  locator: 'Full native UniProt JSON: primaryAccession/entryType/organism/genes/locus,
    comments and cross-references; reference strain is not silently equated with experimental
    strains; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/up-Q04868.raw'
  accessed_at: '2026-11-04T08:00:05.942415Z'
  support: supports
  summary: Reviewed S288C tax559292 entry Q04868, exact locus YMR312W, matches the
    maintained ELP6 instance. Native SUBUNIT, FUNCTION, SIMILARITY, localisation and
    family cross-references were inspected; identity is not direct experimental assembly
    evidence.
  snapshot_sha256: 57a867a3e9e2c007ddc68ed402b1c12037d930c0c98a9d44b052cd4e0a896e88
- evidence_id: plaque-gene-ELP6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AELP6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete one-hit native response; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/gene-ELP6.raw
  accessed_at: '2026-11-04T08:02:21.881442Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one matching entry Q04868;
    primary name, alias and locus were read rather than inferred from search rank.
  snapshot_sha256: 450213b9dbab635de9129bb07b5a96b17af0f73ac853dfe62eedb8a7845204ea
  search_scope: UniProt REST; query=(gene_exact:ELP6) AND (organism_id:559292) AND
    (reviewed:true); size100; date 2026-11-04T08:02:21.881442Z; all returned results
    read, no descendant-taxon or unreviewed expansion; database search, not filesystem
    absence.
- evidence_id: plaque-ipr-IPR006849
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006849/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR006849.raw'
  accessed_at: '2026-11-04T08:00:07.588461Z'
  support: supports
  summary: Elp1 full-protein family, independently linked by Q06706.
  snapshot_sha256: 76382506dc8a8f7ef5c21c1b759f75faa5f9cd0115dc4be0426615686ad1398b
- evidence_id: plaque-ipr-IPR037289
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037289/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR037289.raw'
  accessed_at: '2026-11-04T08:00:07.705961Z'
  support: supports
  summary: Elp2 full-protein family, independently linked by P42935.
  snapshot_sha256: 2c97a32ff23da0f1c8286371f5476c7b7db57d88bbfb5262b623da87d9c2d979
- evidence_id: plaque-ipr-IPR034687
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR034687/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR034687.raw'
  accessed_at: '2026-11-04T08:00:08.074973Z'
  support: supports
  summary: Elp3-like full-protein family, independently linked by Q02908; homologous
    bacterial/archaeal proteins do not thereby become constituents of a yeast-type
    holoenzyme.
  snapshot_sha256: 6597b4b1e49df7e9f2df978867aa55068660cf5115686914698bac1ccf01cade
- evidence_id: plaque-ipr-IPR008728
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008728/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR008728.raw'
  accessed_at: '2026-11-04T08:00:08.237993Z'
  support: supports
  summary: Elp4 full-protein family, independently linked by Q02884.
  snapshot_sha256: 40a1c831e0b195a3e412fb98b798e22ee45d19d8d0012f3feb59c374e5145d35
- evidence_id: plaque-ipr-IPR019519
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019519/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR019519.raw'
  accessed_at: '2026-11-04T08:00:08.326832Z'
  support: supports
  summary: Elp5 full-protein family, independently linked by P38874.
  snapshot_sha256: 3fffeb698c8df6a5bdc80119fd3f1b546d1c82803e5552aa2dbb61010a56f0b1
- evidence_id: plaque-ipr-IPR018627
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018627/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR018627.raw'
  accessed_at: '2026-11-04T08:00:08.706322Z'
  support: supports
  summary: Elp6 full-protein family, independently linked by Q04868.
  snapshot_sha256: 4c47036ce43070e3555ca723507f0f45a873380139cb70999c9ab3db4a7292e7
- evidence_id: plaque-ipr-IPR039661
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039661/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR039661.raw'
  accessed_at: '2026-11-04T08:00:08.855447Z'
  support: supports
  summary: Broader Elp3/YhcC grouping is distinguished from the more precise Elp3-like
    family.
  snapshot_sha256: 65404b7adca1b549577d3f3a8727c6d990537ccdd524028733dbad4520134a23
- evidence_id: plaque-ipr-IPR050238
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR050238.raw'
  accessed_at: '2026-11-04T08:00:08.982273Z'
  support: supports
  summary: Broad DNA replication/repair clamp-loader family is not a distinct RFC2,3,4
    or5 class; its explicitly LLM-generated unchecked description was excluded.
  snapshot_sha256: 20cc681dc2b5aa75e096f21d298105d7ac05cc910f786be9e1f63ae05a72dbc0
- evidence_id: plaque-ipr-IPR062598
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062598/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR062598.raw'
  accessed_at: '2026-11-04T08:02:22.508177Z'
  support: supports
  summary: Elg1 middle domain, not a full-protein Elg1 family.
  snapshot_sha256: a2233392270ec06bf4bd41e56708507c5beda35bcac8d43dd334016b9294b525
- evidence_id: plaque-ipr-IPR062602
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062602/
  locator: 'Complete native InterPro metadata: accession/name/type, member signatures
    and available non-LLM description; cross-checked against individual UniProt membership
    where applicable; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-IPR062602.raw'
  accessed_at: '2026-11-04T08:02:21.895918Z'
  support: supports
  summary: Elg1 C-terminal domain2, not a full-protein Elg1 family.
  snapshot_sha256: 36e41bbde3830f48d5e5bab677eddf8c68728e81c851332258201c7f670b26d9
- evidence_id: plaque-ipr-search-ejectisin
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=ejectisin&page_size=20
  locator: Exact native keyword route and actual response/receipt; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-search-ejectisin.raw
  accessed_at: '2026-11-04T08:00:09.325863Z'
  support: context_only
  summary: HTTP204 with empty body; exact ejectisin mapping remains unresolved, not
    globally disproved.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: InterPro API entry search=ejectisin, page_size20; date 2026-11-04T08:00:09.325863Z;
    one bounded request, no pagination or broader synonym/sequence search. 204 empty
    response is not exhaustive absence evidence; no filesystem search.
- evidence_id: plaque-ipr-search-Elg1
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=Elg1&page_size=20
  locator: Exact native keyword route and actual response/receipt; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-plaque/ipr-search-Elg1.raw
  accessed_at: '2026-11-04T08:00:09.463534Z'
  support: context_only
  summary: 'HTTP429 access limitation: no current family-absence conclusion is drawn.
    Separately readable Elg1 domain metadata does not establish a full-class mapping.'
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
  search_scope: InterPro API entry search=Elg1, page_size20; date 2026-11-04T08:00:09.463534Z;
    one bounded request, no pagination or broader synonym/sequence search. 429 limited
    response is not exhaustive absence evidence; no filesystem search.
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete20 organism rows/28 organism-dataset pairs, independently reread
    from same-PR micro reviewer snapshot; retain actual retrieval timestamp; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T07:59:23.235917Z'
  support: context_only
  summary: Complete current catalogue contains no Saccharomyces cerevisiae, cryptophyte,
    Chroomonas, Cryptomonas or Guillardia host entry. No matching downstream dataset
    was selected; recombinant E.coli expression is not a proxy for these natural hosts.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-micro53-rhiel-publisher
  kind: validation
  reference: https://link.springer.com/article/10.1007/s00709-011-0267-4
  locator: Complete3038-byte native HTML access diagnostic. Historical observation
    carried from 20261022T062451Z-ejectisome-audit/micro53-rhiel-publisher; old time/hash
    retained; original raw transport snapshot not independently refetched as historical
    bytes.
  accessed_at: '2026-10-22T06:09:46.141744Z'
  support: context_only
  summary: HTTP200 returned a Client Challenge JavaScript page, not the article body.
    The original transport receipt is retained without upgrading readability.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: plaque-historical-micro53-ammermann-publisher
  kind: validation
  reference: https://link.springer.com/article/10.1007/s00709-012-0440-4
  locator: Complete3038-byte native HTML access diagnostic. Historical observation
    carried from 20261022T062451Z-ejectisome-audit/micro53-ammermann-publisher; old
    time/hash retained; original raw transport snapshot not independently refetched
    as historical bytes.
  accessed_at: '2026-10-22T06:09:46.141785Z'
  support: context_only
  summary: HTTP200 returned a Client Challenge JavaScript page, not the article body.
    The original transport receipt is retained without upgrading readability.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: plaque-historical-micro53-kubota-publisher
  kind: validation
  reference: https://doi.org/10.1016/j.molcel.2013.02.012
  locator: Original urllib exception response and request receipt. Historical observation
    carried from 20261022T062451Z-elg1-rfc-like-complex-audit/micro53-kubota-publisher;
    old time/hash retained; original raw transport snapshot not independently refetched
    as historical bytes.
  accessed_at: '2026-10-22T06:09:46.141811Z'
  support: context_only
  summary: The native DOI attempt failed with a TLS certificate-verification error
    and status0; no article body was obtained. The separate native MED abstract remains
    readable.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: plaque-historical-micro53-kubota-browser
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/S1097276513001408
  locator: Browser diagnostic representation, status null, exact S1097276513001408
    route. Historical observation carried from 20261022T062451Z-elg1-rfc-like-complex-audit/micro53-kubota-browser;
    old time/hash retained; original raw transport snapshot not independently refetched
    as historical bytes.
  accessed_at: '2026-10-22T06:13:08.787843Z'
  support: context_only
  summary: The exact ScienceDirect paper route also returned a browser403 diagnostic.
    No primary body, figure or Methods inspection is claimed.
  snapshot_sha256: 4d0ed0be0a35798bd187023dadf05366cd8455530459cf3be1df5219b50294b7
- evidence_id: plaque-historical-micro53-kupiec-publisher
  kind: validation
  reference: https://academic.oup.com/femsyr/article/16/7/fow084/2399204
  locator: Retained403 response; no review body claim. Historical observation carried
    from 20261022T062451Z-elg1-rfc-like-complex-audit/micro53-kupiec-publisher; old
    time/hash retained; original raw transport snapshot not independently refetched
    as historical bytes.
  accessed_at: '2026-10-22T06:09:46.364631Z'
  support: context_only
  summary: The attempted publisher route returned HTTP403 challenge content. The Kupiec
    review is independently assessed only through its complete native abstract.
  snapshot_sha256: a2a9b94c0c6a09ba630da01263b8f466c61f107c8c13b052a6f336a3c077d9c2
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete scientific review and required structured-source applicability
  summary: Positive molecular/pathway assertions require actual coverage assessment;
    absence of expression claims is insufficient. Official-source fallback must preserve
    actual dataset and runner scope.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Exact component identities, scientific evidence and append-only Discussions
  summary: Supported named constituents may be label-only when exact identity is unresolved;
    protein examples do not substitute for family grounding. Preserve historical rationale
    and append any current clarification.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Formation essentiality, Component, protein and graph schema
  summary: Family/class components and appropriate complex nodes are allowed. Membership,
    transport activity, growth and formation necessity are different assertions.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native primary names, aliases, source taxa and independent verification
  summary: Native accession/status/gene/strain and family joins require actual data;
    source and expression strains are not interchangeable.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Evidence-scoped graph edges
  summary: Coarse contribution edges are permitted; source-attribution notes must
    accurately describe what the source establishes.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Actual source access and experimental scope
  summary: Authority metadata, primary abstract and genuine primary body are distinct.
    Figure captions do not certify unseen pixels or supplements.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Native finding and evidence contracts
  summary: Inherited findings retain exact repository/review/finding lineage; a new
    source-attribution finding has no invented predecessor.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0002097,GO:0005784,GO:0005789,GO:0033588,GO:0042910,GO:0045048,GO:0072546,GO:0098796,GO:0140330,GO:0140535,GO:1902494,GO:1902495,GO:1990207,GO:1990281
  locator: 'Requested native terms: active status, names, definitions, synonyms and
    typed relation context; only assigned target relations used'
  summary: GO0072546 is EMC and its current definition still lists six older yeast
    member names; Bai independently establishes eight in the measured yeast preparation.
    GO1990207 is EmrE homodimer with generic bacterial distribution. GO1990281 is
    a broader efflux-pump class, not an exact EmrAB identity. GO0140330 describes
    outer-membrane export; GO0042910 and GO0045048 retain their process/function scope.
    Unrelated terms in the combined response are not reviewed targets.
  accessed_at: '2026-11-04T07:56:51.015300Z'
  support: supports
  snapshot_sha256: ff946a7735c549a3a05a73c3dfaaaa7d501546c65d21a07ca7e5e8474cb827b2
- evidence_id: septin-ncbifam-NF011715
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF011715/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Exact full EmrA periplasmic adaptor family, independently joined through
    P27303; shared hairpin/beta-barrel domains are not equivalent.
  accessed_at: '2026-11-04T07:56:52.610128Z'
  support: supports
  snapshot_sha256: 769e1484b7cb220f4f9d8ced45408d463a0256d540b04783f8691e1f0d969114
- evidence_id: septin-ncbifam-NF000391
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF000391/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Exact EmrB permease family, independently joined through P0AEJ0.
  accessed_at: '2026-11-04T07:56:52.634510Z'
  support: supports
  snapshot_sha256: cafbbbd9187ec1b56c7ca1190c035777ea704caa2bbcf460e1bbbaf5b11adf78
- evidence_id: septin-ipr-IPR004638
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004638/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Broader DHA2/EmrB-like family explicitly includes EmrB, FarB, TcmA and
    RibZ; this scope exceeds exact named EmrB.
  accessed_at: '2026-11-04T07:56:52.811388Z'
  support: supports
  snapshot_sha256: 633ee99cb1562d934fe7f86ce75875bc69f1394a42250bdf6a58ce6a0fc00caf
- evidence_id: septin-ipr-IPR058622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Exact TolC family with NF007002 signature and independent P02930 join;
    no correction required for this component.
  accessed_at: '2026-11-04T07:56:52.889903Z'
  support: supports
  snapshot_sha256: d3c58cbb9737d5f395f703b634f84df048f355555af2b817f321a5e474b8e310
- evidence_id: septin-ncbifam-NF042984
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF042984/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Exact full EmrE family with independent P23895 join.
  accessed_at: '2026-11-04T07:56:54.532619Z'
  support: supports
  snapshot_sha256: 6e2c3977a0db9592fa4498e2d34152c7bcc5ab0fe77cb3811f5aee7e52523596
- evidence_id: septin-ncbifam-NF007087
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF007087/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Broader EmrE family entry explicitly also matches a 77%-identical homolog
    that probably needs another name; not exact EmrE replacement.
  accessed_at: '2026-11-04T07:56:53.548524Z'
  support: supports
  snapshot_sha256: fdd122cc8b2b8af1335c5a8acee768b033e1193c186371e9414cdd450b1809db
- evidence_id: septin-ipr-IPR045324
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045324/
  locator: Native name/type, signatures, hierarchy, curated description and provenance
    flags; no sequence alignment reanalysis
  summary: Broad small multidrug resistance family includes distinct MdtI/MdtJ children;
    native description is not LLM generated. Family breadth does not prevent using
    a verified narrower exact entry.
  accessed_at: '2026-11-04T07:56:53.628515Z'
  support: supports
  snapshot_sha256: fc9e8aa77fa57d0e0fac9ab79b8906ffda24817ce0c10036eaa66041ba51a6c4
- evidence_id: septin-peer-protein-P36039
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36039.json
  locator: Native identity, primary gene, synonyms, ordered loci, taxon, status and
    complete relevant family xrefs
  summary: 'Reviewed P36039: ER membrane protein complex subunit 3; primary EMC3;
    aliases [''AIM27'']; loci [''YKL207W'']; taxon 559292. Exact native family xrefs
    checked. Identity annotations are not new assembly experiments. Fresh current
    retrieval despite legacy filename prefix; S288c reference identity is not the
    W303-1a experimental strain.'
  accessed_at: '2026-11-04T07:56:51.138802Z'
  support: supports
  snapshot_sha256: e7cdb798f184bd60f9c0ab04f2c247c0f777fdfcc2f8e4c7ded766abd8de00d9
- evidence_id: septin-peer-protein-P40540
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40540.json
  locator: Native identity, primary gene, synonyms, ordered loci, taxon, status and
    complete relevant family xrefs
  summary: 'Reviewed P40540: ER membrane protein complex subunit 5; primary EMC5;
    aliases [''KRE27'']; loci [''YIL027C'']; taxon 559292. Exact native family xrefs
    checked. Identity annotations are not new assembly experiments. Fresh current
    retrieval despite legacy filename prefix; S288c reference identity is not the
    W303-1a experimental strain.'
  accessed_at: '2026-11-04T07:56:51.520109Z'
  support: supports
  snapshot_sha256: 1dff586fee9090587d422276277b9860e745b1ced24a7b20085c52c7dbce7808
- evidence_id: septin-protein-P27303
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27303.json
  locator: Native identity, primary gene, synonyms, ordered loci, taxon, status and
    complete relevant family xrefs
  summary: 'Reviewed P27303: Multidrug export protein EmrA; primary emrA; aliases
    []; loci [''b2685'', ''JW2660'']; taxon 83333. Exact native family xrefs checked.
    Identity annotations are not new assembly experiments.'
  accessed_at: '2026-11-04T07:56:51.531151Z'
  support: supports
  snapshot_sha256: d7638d10e5bd07cc5b1c923730bb205e1ee6647425b833cc7dd3c0392995e329
- evidence_id: septin-protein-P0AEJ0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEJ0.json
  locator: Native identity, primary gene, synonyms, ordered loci, taxon, status and
    complete relevant family xrefs
  summary: 'Reviewed P0AEJ0: Multidrug export protein EmrB; primary emrB; aliases
    []; loci [''b2686'', ''JW2661'']; taxon 83333. Exact native family xrefs checked.
    Identity annotations are not new assembly experiments.'
  accessed_at: '2026-11-04T07:56:52.647697Z'
  support: supports
  snapshot_sha256: 28e94d51d54ca95bd1deded6498d7456ec9b3b550970d1bb376b28cd1d0c5284
- evidence_id: septin-protein-P02930
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02930.json
  locator: Native identity, primary gene, synonyms, ordered loci, taxon, status and
    complete relevant family xrefs
  summary: 'Reviewed P02930: Outer membrane protein TolC; primary tolC; aliases [''colE1-i'',
    ''mtcB'', ''mukA'', ''refI'', ''toc'', ''weeA'']; loci [''b3035'', ''JW5503''];
    taxon 83333. Exact native family xrefs checked. Identity annotations are not new
    assembly experiments.'
  accessed_at: '2026-11-04T07:56:54.667477Z'
  support: supports
  snapshot_sha256: cef14f6af1999fe0b5218d959cca8788ec00afc1b145201ba48344a4b15bbb04
- evidence_id: septin-protein-P23895
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23895.json
  locator: Native identity, primary gene, synonyms, ordered loci, taxon, status and
    complete relevant family xrefs
  summary: 'Reviewed P23895: Multidrug transporter EmrE; primary emrE; aliases [''eb'',
    ''mvrC'']; loci [''b0543'', ''JW0531'']; taxon 83333. Exact native family xrefs
    checked. Identity annotations are not new assembly experiments.'
  accessed_at: '2026-11-04T07:56:53.651028Z'
  support: supports
  snapshot_sha256: 16b0232f2fa91b8aa82030bd23bc100956391cb5072213492783c1c9de46f3e4
- evidence_id: septin-gene-emrA-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed entries and primary-name/identity joins
  summary: One returned reviewed native entry P27303, with primary gene emrA, confirms
    the present bounded selection. No reconstruction of an unspecified past search.
  accessed_at: '2026-11-04T07:56:51.823163Z'
  support: supports
  snapshot_sha256: 53daa4a1a9e4fe8791823830645ae0c25651dceb217d4e76af0336c1042fe83e
  search_scope: UniProt gene_exact:emrA AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned entry read at 2026-11-04T07:56:51.823163Z.
- evidence_id: septin-gene-emrB-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed entries and primary-name/identity joins
  summary: One returned reviewed native entry P0AEJ0, with primary gene emrB, confirms
    the present bounded selection. No reconstruction of an unspecified past search.
  accessed_at: '2026-11-04T07:56:54.625957Z'
  support: supports
  snapshot_sha256: 53c835b77fdb599222e36e600094db1b6e028876b16cd1baabb6dc8c9edd192e
  search_scope: UniProt gene_exact:emrB AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned entry read at 2026-11-04T07:56:54.625957Z.
- evidence_id: septin-gene-tolC-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed entries and primary-name/identity joins
  summary: One returned reviewed native entry P02930, with primary gene tolC, confirms
    the present bounded selection. No reconstruction of an unspecified past search.
  accessed_at: '2026-11-04T07:56:53.539811Z'
  support: supports
  snapshot_sha256: 3e284eede466d8aa6d6eac091b434ce033083e18848c220476a3bdb06463365a
  search_scope: UniProt gene_exact:tolC AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned entry read at 2026-11-04T07:56:53.539811Z.
- evidence_id: septin-gene-emrE-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed entries and primary-name/identity joins
  summary: One returned reviewed native entry P23895, with primary gene emrE, confirms
    the present bounded selection. No reconstruction of an unspecified past search.
  accessed_at: '2026-11-04T07:56:53.717437Z'
  support: supports
  snapshot_sha256: bcd9fba167947871800476e31915aedb64508a81733cd6c2253e8472df2268ca
  search_scope: UniProt gene_exact:emrE AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned entry read at 2026-11-04T07:56:53.717437Z.
- evidence_id: septin-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete native ENA taxon response
  summary: 'Taxon 2: Bacteria, rank domain. Species, reference strain and recombinant
    expression host remain distinguished.'
  accessed_at: '2026-11-04T07:56:52.913215Z'
  support: supports
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native ENA taxon response
  summary: 'Taxon 4932: Saccharomyces cerevisiae, rank species. Species, reference
    strain and recombinant expression host remain distinguished.'
  accessed_at: '2026-11-04T07:56:50.936335Z'
  support: supports
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
- evidence_id: septin-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native ENA taxon response
  summary: 'Taxon 562: Escherichia coli, rank species. Species, reference strain and
    recombinant expression host remain distinguished.'
  accessed_at: '2026-11-04T07:56:53.087056Z'
  support: supports
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: septin-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native ENA taxon response
  summary: 'Taxon 83333: Escherichia coli K-12, rank strain. Species, reference strain
    and recombinant expression host remain distinguished.'
  accessed_at: '2026-11-04T07:56:51.325874Z'
  support: supports
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: septin-doi-science_aao3099
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.aao3099%22&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: The ER membrane protein complex is a transmembrane
    domain insertase. Authors: Guna A, Volkmar N, Christianson JC, Hegde RS. DOI 10.1126/science.aao3099.
    Complete primary abstract read; bibliographic authority is not by itself full-body
    evidence.'
  accessed_at: '2026-11-04T07:56:50.986097Z'
  support: supports
  snapshot_sha256: 83cd3d2db41c1b4562afd587d667682ecfc026cccb3b0d92db642fe51fe34a50
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:50.986097Z.
- evidence_id: septin-doi-j_cell_2018_10_009
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2018.10.009%22&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: EMC Is Required to Initiate Accurate Membrane Protein
    Topogenesis. Authors: Chitwood PJ, Juszkiewicz S, Guna A, Shao S, Hegde RS. DOI
    10.1016/j.cell.2018.10.009. Complete primary abstract read; bibliographic authority
    is not by itself full-body evidence.'
  accessed_at: '2026-11-04T07:56:51.005909Z'
  support: supports
  snapshot_sha256: 4bb193bad91c52516f0ed6479472774477aa84c851260599b50bafb54657d686
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:51.005909Z.
- evidence_id: septin-doi-s41586-020-2389-3
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-020-2389-3%22&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: Structure of the ER membrane complex, a transmembrane-domain
    insertase. Authors: Bai L, You Q, Feng X, Kovach A, Li H. DOI 10.1038/s41586-020-2389-3.
    Complete primary abstract read; bibliographic authority is not by itself full-body
    evidence.'
  accessed_at: '2026-11-04T07:56:51.001516Z'
  support: supports
  snapshot_sha256: 8edb9d22ac510ab0caab56f5cd2e51043790aace4873b6de04eb41bd015ef179
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:51.001516Z.
- evidence_id: septin-doi-eLife_57887
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.57887%22&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: The architecture of EMC reveals a path for membrane
    protein insertion. Authors: O''Donnell JP, Phillips BP, Yagita Y, Juszkiewicz
    S, Wagner A, Malinverni D, Keenan RJ, Miller EA, Hegde RS. DOI 10.7554/elife.57887.
    Complete primary abstract read; bibliographic authority is not by itself full-body
    evidence.'
  accessed_at: '2026-11-04T07:56:51.632359Z'
  support: supports
  snapshot_sha256: e7c2099808542422cbb4543e8b8ff10d923250b0cb01d9afedd1c0596ed502d3
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:51.632359Z.
- evidence_id: septin-pmid-12482849
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12482849+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: Identification of oligomerization and drug-binding
    domains of the membrane fusion protein EmrA. Authors: Borges-Walmsley MI, Beauchamp
    J, Kelly SM, Jumel K, Candlish D, Harding SE, Price NC, Walmsley AR. DOI 10.1074/jbc.m209457200.
    Complete primary abstract read; bibliographic authority is not by itself full-body
    evidence. Borges-Walmsley2003 tests EmrA oligomerization/drug binding and proposes
    a trimeric model; it is not the modern whole-complex6:1:3 count source.'
  accessed_at: '2026-11-04T07:56:52.491156Z'
  support: supports
  snapshot_sha256: a1371a1e352145cb70838ea905392c5169553c2cc4d1ace978eb9cfc69311fc3
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:52.491156Z.
- evidence_id: septin-pmid-33065135
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A33065135+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: Structural characterization of the EmrAB-TolC efflux
    complex from E. coli. Authors: Yousefian N, Ornik-Cha A, Poussard S, Decossas
    M, Berbon M, Daury L, Taveau JC, Dupuy JW, Đorđević-Marquardt S, Lambert O, Pos
    KM. DOI 10.1016/j.bbamem.2020.183488. Complete primary abstract read; bibliographic
    authority is not by itself full-body evidence. Yousefian2021 abstract supports
    coexpression/purification and EM of native tripartite pump, 33nm and probable
    tip-to-tip canal; full body not obtained or certified in this review.'
  accessed_at: '2026-11-04T07:56:51.638339Z'
  support: supports
  snapshot_sha256: 999f84c8ac5773506c7501227d64dd010caacc1f23c72b6c1f260402dd5fed24
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:51.638339Z.
- evidence_id: septin-pmid-41839863
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A41839863+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: A model for drug transport across two membranes
    of Gram-negative bacteria by an MFS tripartite assembly. Authors: Zhong Z, Maimaiti
    T, Jackson ML, Dong R, Gao X, Ouyang Q, Wang W, Guo J, Li S, Shang W, Liu H, Jiang
    H, Zhang S, Zachariae U, Luisi BF, Chao Y, Du D. DOI 10.1038/s41467-026-70500-5.
    Complete primary abstract read; bibliographic authority is not by itself full-body
    evidence.'
  accessed_at: '2026-11-04T07:56:51.768936Z'
  support: supports
  snapshot_sha256: 25e4f1487a39a2cb96921cf7eba12edc4953ef873969e64ff1ab79cc46f67d11
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:51.768936Z.
- evidence_id: septin-pmid-18024586
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18024586+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete EuropePMC CORE metadata and primary abstractText
  summary: 'Native exact citation: X-ray structure of EmrE supports dual topology
    model. Authors: Chen YJ, Pornillos O, Lieu S, Ma C, Chen AP, Chang G. DOI 10.1073/pnas.0709387104.
    Complete primary abstract read; bibliographic authority is not by itself full-body
    evidence.'
  accessed_at: '2026-11-04T07:56:53.626311Z'
  support: supports
  snapshot_sha256: cdf0b6a4e684d755b45c64e18fdb06ca540fdae1311534ba4f9be6976c8c8635
  search_scope: Exact DOI or PMID query shown in URL, CORE JSON, no date filter; unique
    result at 2026-11-04T07:56:53.626311Z.
- evidence_id: septin-bai2020-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7442705/
  locator: Genuine PMC7442705 body sections S2–S5 and S7 purification, associated
    main captions; no figure pixels or supplementary datasets
  summary: 'Native yeast Emc5-FLAG purification in W303-1a plus mass spectrometry/cryo-EM
    establishes Emc1–6,Emc7,Emc10. Growth and client defects are distinct from assembly:
    Emc3 K26L mutant complex remains intact despite functional defects. Eight yeast
    constituents must not be replaced by old GO six-member text or mammalian composition.'
  accessed_at: '2026-11-04T07:56:50.770911Z'
  support: supports
  snapshot_sha256: c3b36156809e45cfa1d305deef2a555a7e411f3db4f41230e05677d28c858f84
- evidence_id: septin-guna2018-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5788257/
  locator: Genuine PMC5788257 unsectioned main scientific paragraphs and Figures1–4
    captions, through conclusion before acknowledgments; no supplementary methods/data
    or pixels
  summary: Selected moderately hydrophobic TA substrates such as SQS require EMC in
    U2OS/HEK assays; purified intact mammalian EMC in liposomes is sufficient for
    insertion. VAMP2/TRC40 contrasts bound scope. This is insertase activity, not
    individual yeast-subunit assembly necessity.
  accessed_at: '2026-11-04T07:56:50.720054Z'
  support: supports
  snapshot_sha256: a281d547095505ba3794acf287b2347f7ed4561f1df32177bb7139b952a3a7d4
- evidence_id: septin-chitwood2018-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6269167/
  locator: Genuine PMC6269167 Results2.5–2.7 plus full native abstract; other results/methods
    and supplements not certified
  summary: Sec61-depleted and purified EMC/SRP-receptor proteoliposomes support selected
    Nexo signal-anchor insertion. Beta1AR TMD1 and TMD2 distinguish sequential EMC/Sec61
    roles. Not universal EMC dependence of every transmembrane segment.
  accessed_at: '2026-11-04T07:56:50.787352Z'
  support: supports
  snapshot_sha256: d20fd843292836d13d94b11a22511582d9c43c3df4245435ee5f497d9ab5af65
- evidence_id: septin-odonnell2020-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7292650/
  locator: Genuine PMC7292650 main article Results2.4–2.6 with embedded captions and
    Methods4.7; no image pixels or supplement experiments independently reanalyzed
  summary: Human EMC architecture combines native HEK293 purification, moderate6.5Angstrom
    map, docking/prediction and crosslinks. Vestibule and lipid-exposed groove provide
    a proposed insertion path requiring further tests, not a measured complete insertion
    trajectory or fixed yeast inventory.
  accessed_at: '2026-11-04T07:56:50.860114Z'
  support: supports
  snapshot_sha256: 448e2cb19bd4bf3e79708f2e561e76715508b9b69f22197ee98569bae5012f6c
- evidence_id: septin-zhong2026-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13139468/
  locator: Genuine PMC13139468 Sections3,4,6,8,11 and Methods14–17 with relevant main
    captions; Discussion12 inspected for proposed-model scope, not all supplements
    or pixels
  summary: MG1655 genes expressed in engineered C43(DE3) delta-acrAB constructs yield
    EmrA6:EmrB1:TolC3. Pump-EA is assembled but inactive in resistance assays; pump-FA
    is active. Structural, omission/mutant resistance and everted-vesicle antiport
    experiments are distinguished. These measurements do not mean CPX labels each
    member assembly-essential; the supported complete-pump architecture and coupling
    remain intact.
  accessed_at: '2026-11-04T07:56:52.324095Z'
  support: supports
  snapshot_sha256: af4196d5405230e0058f669b232226b416548b921e6c8883e3181b2f62622925
- evidence_id: septin-chen2007-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2141897/
  locator: Genuine PMC2141897 Results2–5 and7–8, Methods10/12 plus relevant main captions;
    no coordinate/raw-data or figure-pixel reanalysis
  summary: Corrected TPP-bound EmrE structures and anomalous markers support antiparallel
    homodimer; acidic apo form is distorted and not the accepted transport conformation.
    Recombinant BL21(DE3)/cell-free expression and binding assays remain distinct
    from native K12 identity. No full kinetic transport cycle or all-SMR homodimer
    conclusion.
  accessed_at: '2026-11-04T07:56:53.160678Z'
  support: supports
  snapshot_sha256: 804f3180b3915d1e3c10fa2f188619217b1f1b05fc944677e7fa0cb0a5ab8412
- evidence_id: septin-complex-CPX-4268
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4268
  locator: Complete object including functions/properties, all three participants/stoichiometries/bioRoles,
    complexAssemblies, xrefs and evidenceType
  summary: Native K12 EmrAB-TolC identity; six EmrA P27303,one EmrB P0AEJ0,three TolC
    P02930; heterodecamer. Participant bioRoles are unspecified; evidenceType ECO0005547
    is inferred by curator. No participant essentiality classification is present
    in this complete response. Native systematicName retains an older short notation
    and is not used instead of explicit participant counts.
  accessed_at: '2026-11-04T07:56:52.534178Z'
  support: supports
  snapshot_sha256: 4dd8d1075159c44c779141de7e6ffb8cf4824ef3830e3704223626dbfecadab6
- evidence_id: septin-eco0005547
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FECO_0005547
  locator: Native ECO identity/definition response
  summary: ECO0005547 is inferred by curator, not an experimental assembly-necessity
    assay.
  accessed_at: '2026-11-04T07:56:52.272948Z'
  support: supports
  snapshot_sha256: 5e079c708429feead41b2264cd1bf4f73131b706add51786aeaa9ad1f0de949b
- evidence_id: septin-pdb-8ZAL-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/8ZAL
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: Entry is engineered pump-EA; EM entry with ten deposited protein instances
    and Zhong2026 citation. Source body, not mere entry title, supplies functional
    limitations.
  accessed_at: '2026-11-04T07:56:51.844775Z'
  support: supports
  snapshot_sha256: ed624267153d201ad3c5d23ac9d33b577f429f011f6858bc83ca940cd75948aa
- evidence_id: septin-pdb-8ZAL-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/8ZAL/1
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: Author/software assembly1 is a heterodecamer with ten protein instances;
    no essentiality field is inferred.
  accessed_at: '2026-11-04T07:56:51.888452Z'
  support: supports
  snapshot_sha256: 0ef4b90f32f9f356a7192a19657db57ea195454471080e849d5b9fd9b3ef4515
- evidence_id: septin-pdb-8ZAL-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/8ZAL/1
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: EmrA chainsA–F map to P27303; model omits the native N-terminal region
    and comes from engineered EA.
  accessed_at: '2026-11-04T07:56:51.931105Z'
  support: supports
  snapshot_sha256: 7fe4c3cafca5ae5c1ed0680e52baefc1cbadfebca38d80893739e68830196d63
- evidence_id: septin-pdb-8ZAL-entity2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/8ZAL/2
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: TolC chainsG–I map to P02930; native biological K12 differs from expression
    E.coliB.
  accessed_at: '2026-11-04T07:56:51.981342Z'
  support: supports
  snapshot_sha256: ec940664938a4fab4173a5bffbf15451377bba0e1b78f6b7644bf3ffdcefbe1c
- evidence_id: septin-pdb-8ZAL-entity3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/8ZAL/3
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: EmrB chainJ maps to P0AEJ0; biological K12 and expression E.coliB are distinct.
  accessed_at: '2026-11-04T07:56:52.019209Z'
  support: supports
  snapshot_sha256: e26e44a6a3c6edda52d778da6c6d6fa692a53173a88a6a61d6525818f88b736c
- evidence_id: septin-pdb-3B5D-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/3B5D
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: Entry is TPP-bound C2 EmrE structure,Chen2007,3.8Angstrom; not the distorted
    apo form.
  accessed_at: '2026-11-04T07:56:52.871952Z'
  support: supports
  snapshot_sha256: 180a81cf875bddfb701664e093dd237e83d38c8f61b97379d30615a54c9ece97
- evidence_id: septin-pdb-3B5D-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/3B5D/1
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: Author-defined assembly1 is dimeric with two protein instances.
  accessed_at: '2026-11-04T07:56:52.929431Z'
  support: supports
  snapshot_sha256: 6299f333ad1fd84e594661efb0f716401c6edd97cb4a316ad14ddec961e701e3
- evidence_id: septin-pdb-3B5D-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/3B5D/1
  locator: Actual RCSB entry/assembly/entity metadata and native accession/source-host
    joins; no coordinate reanalysis
  summary: ChainsA/B both map to P23895; source K12 and expression BL21(DE3) differ.
  accessed_at: '2026-11-04T07:56:52.976696Z'
  support: supports
  snapshot_sha256: b432e7c75599f9065f94566d3e92ddee012d50bc992309855f045863bb706fc0
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete20-organism official catalogue independently read
  summary: E.coli covered; no yeast or human row. Other eukaryotic/microbial hosts
    are not substituted. Coverage is not biological presence or absence.
  accessed_at: '2026-11-04T07:59:23.235917Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official unpaginated /api/datasets; all20 organism rows checked for
    Saccharomyces cerevisiae,Homo sapiens,Escherichia coli; no date filter; actual
    2026-11-04T07:59:23.235917Z.
- evidence_id: septin-adapter-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete precise1k metadata and strain list
  summary: E.coli precise1k advertises BW25113,DGF-298,GMOS,MG1655,W3110,201 modules
    and1035samples. It supports reference-host context, not C43(DE3)delta-acrAB,BL21
    or every primary assay.
  accessed_at: '2026-11-04T07:59:23.785789Z'
  support: supports
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: septin-adapter-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 module identities/names/regulators/categories; no generated summaries/activity
    traces
  summary: Native SoxS22 and ROS TALE Amp9 are bounded expression-context annotations.
    Dataset coverage does not establish structural membership, topology or formation
    necessity.
  accessed_at: '2026-11-04T07:59:23.197515Z'
  support: supports
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: Official e_coli/precise1k module inventory,all201 rows,no date filter
    or other dataset; exact returned IDs independently checked.
- evidence_id: septin-modulegene-emrA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2685
  locator: Exact gene_id/gene_name/product/UniProt identity join
  summary: Dataset locus b2685 maps emrA to the independently verified accession;
    imported function prose is not a separately read primary paper.
  accessed_at: '2026-11-04T08:01:19.941488Z'
  support: supports
  snapshot_sha256: 4a00e2d20e82ead12ae06936c01112aa5ca3e4e5f9a106e377bc949fb5d102f7
- evidence_id: septin-modulemembers-emrA
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2685/imodulons
  locator: Complete201 threshold/weight/membership rows
  summary: 'Thresholded hits: none. False flags do not imply absent expression,gene
    or structural role; positive hits do not establish assembly.'
  accessed_at: '2026-11-04T08:01:19.906923Z'
  support: supports
  snapshot_sha256: 07be576d65e2e25d74578425178ba00a22d5033d991bb78b1110e4d13ce56dcb
  search_scope: Official e_coli/precise1k/gene b2685 (emrA) /imodulons; all201 returned
    rows,no date filter; actual 2026-11-04T08:01:19.906923Z.
- evidence_id: septin-modulegene-emrB
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2686
  locator: Exact gene_id/gene_name/product/UniProt identity join
  summary: Dataset locus b2686 maps emrB to the independently verified accession;
    imported function prose is not a separately read primary paper.
  accessed_at: '2026-11-04T08:01:19.941463Z'
  support: supports
  snapshot_sha256: 112b7f88151a11f630a7eae64550d0bd29cb558b408705b784db91b992a32dad
- evidence_id: septin-modulemembers-emrB
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b2686/imodulons
  locator: Complete201 threshold/weight/membership rows
  summary: 'Thresholded hits: none. False flags do not imply absent expression,gene
    or structural role; positive hits do not establish assembly.'
  accessed_at: '2026-11-04T08:01:19.936880Z'
  support: supports
  snapshot_sha256: 6465f188bc9d794f7eda02fc2c3440b572edc8ddae668d2997ea82efa0d49317
  search_scope: Official e_coli/precise1k/gene b2686 (emrB) /imodulons; all201 returned
    rows,no date filter; actual 2026-11-04T08:01:19.936880Z.
- evidence_id: septin-modulegene-tolC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3035
  locator: Exact gene_id/gene_name/product/UniProt identity join
  summary: Dataset locus b3035 maps tolC to the independently verified accession;
    imported function prose is not a separately read primary paper.
  accessed_at: '2026-11-04T08:01:19.906892Z'
  support: supports
  snapshot_sha256: 3c1072490b201aff8b31f919b89d538017fabee3272bdf9115b4949ad8844a7a
- evidence_id: septin-modulemembers-tolC
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3035/imodulons
  locator: Complete201 threshold/weight/membership rows
  summary: 'Thresholded hits: 22 SoxS. False flags do not imply absent expression,gene
    or structural role; positive hits do not establish assembly.'
  accessed_at: '2026-11-04T08:01:19.964611Z'
  support: supports
  snapshot_sha256: c65a4d314d71a084b2bf80376d7a091196d354d2d4cbc86c6b07b60952e15988
  search_scope: Official e_coli/precise1k/gene b3035 (tolC) /imodulons; all201 returned
    rows,no date filter; actual 2026-11-04T08:01:19.964611Z.
- evidence_id: septin-modulegene-emrE
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0543
  locator: Exact gene_id/gene_name/product/UniProt identity join
  summary: Dataset locus b0543 maps emrE to the independently verified accession;
    imported function prose is not a separately read primary paper.
  accessed_at: '2026-11-04T08:01:19.944591Z'
  support: supports
  snapshot_sha256: 82e187756af9fe3ba5781c6edf7a649543b3177792938741129271f1290db664
- evidence_id: septin-modulemembers-emrE
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0543/imodulons
  locator: Complete201 threshold/weight/membership rows
  summary: 'Thresholded hits: 9 ROS TALE Amp. False flags do not imply absent expression,gene
    or structural role; positive hits do not establish assembly.'
  accessed_at: '2026-11-04T08:01:19.913918Z'
  support: supports
  snapshot_sha256: a7d9600643688d3246047d42a2eac0ce48d35c46510a01a7a432116033137441
  search_scope: Official e_coli/precise1k/gene b0543 (emrE) /imodulons; all201 returned
    rows,no date filter; actual 2026-11-04T08:01:19.913918Z.
- evidence_id: septin-module-9
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/9
  locator: Native module metadata/threshold/category/regulator fields; ai_summary
    excluded
  summary: Module 9 has 9 thresholded genes; emrE matches the native gene-membership
    endpoint. Expression clustering is not physical complex evidence.
  accessed_at: '2026-11-04T08:01:34.253363Z'
  support: supports
  snapshot_sha256: 16abb48f637152fbc67781b55d806f7bb6638dd7d8a8ca8e66adcdcd9facda29
- evidence_id: septin-module-9-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/9/genes
  locator: Complete9 member IDs and focal emrE row/weight/accession; no imported prose
    promoted to primary evidence
  summary: Independent member list confirms emrE; emrE weight0.284604907 exceeds0.109226946
    for9, tolC0.033449641 exceeds0.030026006 for22. No condition/activity or causal
    interpretation is added.
  accessed_at: '2026-11-04T08:01:34.231186Z'
  support: supports
  snapshot_sha256: f006a8865e8ad37e1d31600ea389258deecb8b223824d18cedb2bef16d9a7fb2
- evidence_id: septin-module-22
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22
  locator: Native module metadata/threshold/category/regulator fields; ai_summary
    excluded
  summary: Module 22 has 117 thresholded genes; tolC matches the native gene-membership
    endpoint. Expression clustering is not physical complex evidence.
  accessed_at: '2026-11-04T08:01:34.233183Z'
  support: supports
  snapshot_sha256: 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703
- evidence_id: septin-module-22-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes
  locator: Complete117 member IDs and focal tolC row/weight/accession; no imported
    prose promoted to primary evidence
  summary: Independent member list confirms tolC; emrE weight0.284604907 exceeds0.109226946
    for9, tolC0.033449641 exceeds0.030026006 for22. No condition/activity or causal
    interpretation is added.
  accessed_at: '2026-11-04T08:01:34.278401Z'
  support: supports
  snapshot_sha256: 6e779e25e705f68403277aa34683af16a8dddfd4dc5fbe96fb6bdfc7117e20f0
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical Nov3 00:49Z invocation receipt
  summary: Actual prior exit1 PermissionError reading pyvenv.cfg; no current invocation/success
    is claimed. Current official-source fallback separately evidenced.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-septin/original-checks.json
  locator: Actual original validate/render commands and all39 historical input occurrences
  summary: Three original pairs validate/render0 with exact Markdown. All historical
    inputs match; EmrAB current target changed by four edges/history, while EMC/EmrE
    remain unchanged. Historical corpus checks are not current-head CI.
  accessed_at: '2026-11-04T07:57:09.618239Z'
  support: supports
  snapshot_sha256: 471292493ffebcea8f108818260bcf5bb47efa7855e8bc673e48144e1dc29fc8
- evidence_id: septin-emrab-stale-diff
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/adversary-septin/emrab-stale.diff
  locator: Exact old frozen-source to current-source target diff
  summary: Four new contributions/outer-export edges plus curation history substantively
    reassessed. New CPX essentiality-attribution concern is not assigned an invented
    old occurrence.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: f6aa0cd9919e9c1ed9f5016f7e3f236bba75c3f06d39513530aa2a1a13908227
- evidence_id: septin-record-emc_complex
  kind: record_content
  reference: data/structures/other/emc_complex.yaml
  locator: Complete current frozen record,all fields and history
  summary: Every current field independently reviewed; dated rationale is retained
    as provenance,with corrections appended when warranted.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: 5b6483b187c333f4d7499642810417cc509133fa247436a8907f1263e0d07f54
- evidence_id: septin-original-emc_complex
  kind: record_content
  reference: reviews/structured/20261022T062453Z-emc-complex-audit/review.yaml
  locator: Complete original YAML and exact deterministic Markdown
  summary: Original scientific findings/actions/scopes and historical hashes inspected;
    original files remain immutable.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: 51a8529eb2eabe5bb7c7305dc18975bebe0de1c23f7c66b09b4743cd344bf9f1
- evidence_id: septin-native-emc_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-verify-receipt.json
  locator: Actual command/head/time and complete log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 actual protein examples; zero typed protein nodes,so exit0 is an empty-inventory
    check rather than constituent coverage.
  accessed_at: '2026-11-04T07:56:45.639693Z'
  support: supports
  snapshot_sha256: 3b3fd42f632886c33190f11c8b38db26c7820bc6c0d543623aca312fa5e49e2b
- evidence_id: septin-native-emc_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-causal-receipt.json
  locator: Actual command/head/time and complete log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 actual protein examples; zero typed protein nodes,so exit0 is an empty-inventory
    check rather than constituent coverage.
  accessed_at: '2026-11-04T07:56:46.093343Z'
  support: supports
  snapshot_sha256: bd2c1cf94730040dad396c92d223da425c86d0152af97d421b8b9e7b06b64bb0
- evidence_id: septin-record-emrab_tolc_multidrug_efflux_transport_complex
  kind: record_content
  reference: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Complete current frozen record,all fields and history
  summary: Every current field independently reviewed; dated rationale is retained
    as provenance,with corrections appended when warranted.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: 2ecd59317bfeae525a312c7ba1427b4ad561dfb25b621ff647b42e2205c150d6
- evidence_id: septin-original-emrab_tolc_multidrug_efflux_transport_complex
  kind: record_content
  reference: reviews/structured/20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml
  locator: Complete original YAML and exact deterministic Markdown
  summary: Original scientific findings/actions/scopes and historical hashes inspected;
    original files remain immutable.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: 22bc7fe7167e8a7cd3913e0a30fa883d9572ed33df3d51bb9faa241d333162a9
- evidence_id: septin-native-emrab_tolc_multidrug_efflux_transport_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify-receipt.json
  locator: Actual command/head/time and complete log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 actual protein examples; 3 typed nodes,all COVERED; identity/coverage
    does not independently establish membership or necessity.
  accessed_at: '2026-11-04T07:56:47.563608Z'
  support: supports
  snapshot_sha256: 539009e524c81f447fa577e526f5790ac9da2c6904d266f26e76fb37c1843abc
- evidence_id: septin-native-emrab_tolc_multidrug_efflux_transport_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal-receipt.json
  locator: Actual command/head/time and complete log SHA256 470e07d0a056cc012469c5825c184baff91f5d1a6fc33adc4c368013cc58f268
  summary: 3 actual protein examples; 3 typed nodes,all COVERED; identity/coverage
    does not independently establish membership or necessity.
  accessed_at: '2026-11-04T07:56:48.018423Z'
  support: supports
  snapshot_sha256: 93fab481e7a9d65095939b62b66847cb14b0812b6986546af6bf9f705af8d045
- evidence_id: septin-record-emre_multidrug_transporter_complex
  kind: record_content
  reference: data/structures/other/emre_multidrug_transporter_complex.yaml
  locator: Complete current frozen record,all fields and history
  summary: Every current field independently reviewed; dated rationale is retained
    as provenance,with corrections appended when warranted.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: 7a4055fadb4512ab96308689f737202f1b82dfd99e0fe4046fa82e1e22f6a0e0
- evidence_id: septin-original-emre_multidrug_transporter_complex
  kind: record_content
  reference: reviews/structured/20261022T062455Z-emre-multidrug-transporter-complex-audit/review.yaml
  locator: Complete original YAML and exact deterministic Markdown
  summary: Original scientific findings/actions/scopes and historical hashes inspected;
    original files remain immutable.
  accessed_at: '2026-11-04T08:06:02.901760Z'
  support: context_only
  snapshot_sha256: 5b0e8d7e997bb78f75aa39cdd58ee292e45f99c2ed2b7cb918ee2f7a0e1c6efb
- evidence_id: septin-native-emre_multidrug_transporter_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-verify-receipt.json
  locator: Actual command/head/time and complete log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 actual protein examples; 1 typed nodes,all COVERED; identity/coverage
    does not independently establish membership or necessity.
  accessed_at: '2026-11-04T07:56:49.564180Z'
  support: supports
  snapshot_sha256: 41230d66fdcbd4a83d4a48da6b5d379dc8baf1589bc232bf3932ee2e4ee768f1
- evidence_id: septin-native-emre_multidrug_transporter_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-causal-receipt.json
  locator: Actual command/head/time and complete log SHA256 0ba2585e9162a17ba8731cba84e13eb7e577ea344263773afa6c906b12c8e38c
  summary: 1 actual protein examples; 1 typed nodes,all COVERED; identity/coverage
    does not independently establish membership or necessity.
  accessed_at: '2026-11-04T07:56:49.982886Z'
  support: supports
  snapshot_sha256: 6e45f29e338dc99f421d75e0b005ec50de368925d4c10161c14c016e0d999405
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T08:02:21.906961Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 151cad05a00d426e5a51ef179b276eb110ea7ab698f017b7e543d842e093ac64
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:57:01.832962Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:56:37.684835Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:56:33.587358Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:56:57.908604Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T08:16:41Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 02fc1cda4f0b45a7eba410c02f6c4de856aeb766c08253efb65d28c4b10e45f8
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T07:58:50.511534Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 166ca6b08cbeb3583fdcd0c7503f133f6df00e79bbc220fbba2bf595c64f68b6
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2390 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-dsl1_nzr_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:35.561623Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dsl1_nzr_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dsl1_nzr_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:36.015697Z'
  support: context_only
  snapshot_sha256: 087c7ae1c1ed5570e68b1849441b8171b6fc5520408fe4812cd3c9d4cd6d205a
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dubm_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:37.188415Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dubm_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dubm_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:37.656482Z'
  support: context_only
  snapshot_sha256: 41ef97ef6e5f7ed9b222fedc877f99f969f29044d849f5f84419f75ca162120e
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dxr_protein_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:38.906867Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dxr_protein_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/dxr_protein_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:39.347400Z'
  support: context_only
  snapshot_sha256: df2ee219a494b4e317e88c9b090a533138fc496c62bc029f1baba3b3c92f069c
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-eisosome-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:40.501675Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-eisosome-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/eisosome-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:40.936084Z'
  support: context_only
  snapshot_sha256: b0e108f81d2b02fa358798328d9b302fd746704f610e9c3665ab02ca281b9d99
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ejectisome-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:41.372528Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ejectisome-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/ejectisome-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:41.816643Z'
  support: context_only
  snapshot_sha256: dc516d6ef3fa342c638df335b97de8ae4de12b60f9910f0eb3e1305d4856adf8
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-elg1_rfc_like_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:43.057231Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-elg1_rfc_like_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elg1_rfc_like_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:43.500731Z'
  support: context_only
  snapshot_sha256: cb8359551acfa102a3c4984a50cf8f76ee180be1c9809dd6edf16b50c1432672
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-elongator_holoenzyme_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:44.725933Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-elongator_holoenzyme_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/elongator_holoenzyme_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:45.178098Z'
  support: context_only
  snapshot_sha256: 29a516440ea13c22756b229da3ae60ec5478f31193cc9d8912c5317484dd5a63
  summary: 6 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emc_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:45.639693Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emc_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emc_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:46.093343Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:47.563608Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emrab_tolc_multidrug_efflux_transport_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:48.018423Z'
  support: context_only
  snapshot_sha256: 470e07d0a056cc012469c5825c184baff91f5d1a6fc33adc4c368013cc58f268
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emre_multidrug_transporter_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:49.564180Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emre_multidrug_transporter_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2390/emre_multidrug_transporter_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:56:49.982886Z'
  support: context_only
  snapshot_sha256: 0ba2585e9162a17ba8731cba84e13eb7e577ea344263773afa6c906b12c8e38c
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-dsl-identity
  area: identity
  topic: Exact tether identity and boundary
  outcome: supported
  summary: GO0070939 exactly denotes the ternary Dsl1/NZR tether. GO0099023 is is-a
    and GO0005783 is ER parthood/localization; COPI and ER SNARE interactions do not
    make every binding partner a constituent.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-go-0070939
  - micro-go-0070939-ancestors
  - micro-go-0099023
  - micro-go-0005783
  - micro-tripathi
- assessment_id: micro-dsl-primary
  area: evidence
  topic: Current primary composition and transport evidence
  outcome: supported
  summary: Fresh Tripathi body supports recombinant ternary composition, contacts
    and transport-tether interpretation. Fresh Meiringer/Kraynack complete abstracts
    support the stated core/SNARE context; their current full bodies were not obtained.
    Historical body readings are not newly certified.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-tripathi
  - micro-meta-10.1074_jbc.M110.215327
  - micro-meta-10.1091_mbc.e05-01-0056
  - micro-access-meiringer-legacy
  - micro-access-kraynack-legacy
- assessment_id: micro-dsl-family
  area: grounding
  topic: Tip20 exact family versus domain alternatives
  outcome: concern
  summary: Tip20 IPR007528 is the exact RINT1/Tip20 family and P33891 has that xref.
    The current three-constituent task can be narrowed for Tip20 after curation. Inspected
    Dsl1 N/C and Sec39 identifiers are domains, not exact whole-protein replacements;
    no exhaustive absence claim.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-ipr-IPR007528
  - micro-protein-P33891
  - micro-ipr-IPR021875
  - micro-ipr-IPR021876
  - micro-ipr-IPR013244-retry
  - micro-policy
- assessment_id: micro-dsl-formation
  area: evidence
  topic: Purified Dsl1 bridging evidence
  outcome: concern
  summary: 'Tripathi S6/Figure4 directly compares pairwise binding and ternary reconstitution:
    Dsl1 links Tip20 and Sec39. Current component evidence lacks that bounded association/formation
    observation. A global UNKNOWN essentiality value may remain; domain-mutant growth
    and universal in-vivo absence are different questions.'
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-tripathi
  - micro-policy
  - micro-schema
- assessment_id: micro-dsl-graph
  area: graph
  topic: Coarse NONMECHANISTIC FUNCTION graph
  outcome: supported
  summary: Three constituent-to-complex contributions, ER localization and retrograde-transport
    function are proportionate to the graph scope. It does not claim a solved fusion
    mechanism or make transient coat/SNARE partners members.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-tripathi
  - micro-go-0006890
  - micro-graph-policy
- assessment_id: micro-dsl-localization
  area: evidence
  topic: Example localization and historical names
  outcome: supported
  summary: Current native DSL1/TIP20/SEC39 primary names and TIP1/DSL3 aliases support
    intended examples. Fresh complete abstracts for PMID11493604/11739780 support
    peripheral ER and retrograde context; PMID8334998 supplies historical Tip1/Sec20
    association. No unread strain-level full methods are certified.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-protein-P53847
  - micro-protein-P33891
  - micro-protein-Q12745
  - micro-meta-11493604
  - micro-meta-11739780
  - micro-meta-8334998
- assessment_id: micro-dub-identity
  area: identity
  topic: Four-protein DUB module and SAGA/SLIK boundaries
  outcome: supported
  summary: GO0071819 is the four-constituent DUB module within SAGA and SLIK. Parent
    nuclear-complex and two parthood relations are consistent; the entire19-subunit
    SAGA structure is not the record identity.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-go-0071819
  - micro-go-0071819-ancestors
  - micro-go-0000124
  - micro-go-0046695
  - micro-wang
  - micro-adamus
- assessment_id: micro-dub-primary
  area: evidence
  topic: Primary structural and biochemical scope
  outcome: supported
  summary: Wang supports Ubp8/Sgf11/Sus1/N-terminal Sgf73 and Sgf73 tether to the
    larger core. Adamus directly identifies SLIK/SAGA components and compares DUB
    activity, with Ub-AMC and low-resolution EM limits. Reference S288C examples are
    not substituted for every experimental strain.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-wang
  - micro-adamus
  - micro-meta-10.1101_gad.1144003
  - micro-taxon-559292
- assessment_id: micro-dub-family
  area: grounding
  topic: Three exact constituent families
  outcome: concern
  summary: Current complete family entries IPR013246, IPR018783 and IPR037804 independently
    match Sgf11, Sus1 and Sgf73 native xrefs. These resolve three existing class-grounding
    tasks; Ubp8 catalytic USP domain and broad hydrolase family do not resolve its
    exact class. LLM-flagged broad-family prose is not biological evidence.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-ipr-IPR013246
  - micro-ipr-IPR018783
  - micro-ipr-IPR037804
  - micro-protein-Q03067
  - micro-protein-Q6WNK7
  - micro-protein-P53165
  - micro-ipr-IPR028889
  - micro-ipr-IPR050185
  - micro-policy
- assessment_id: micro-dub-formation
  area: evidence
  topic: UNKNOWN requirement and partial association data
  outcome: unknown
  summary: Kohler complete abstract concerns Sus1 association with SAGA and a high-salt
    three-protein subcomplex; it does not directly establish every four-member module
    formation requirement. No universal essentiality or new experiment is imposed.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-meta-16855026
  - micro-policy
- assessment_id: micro-dub-localization
  area: evidence
  topic: Native example locations versus whole module
  outcome: supported
  summary: Native annotations and complete indexed abstracts retain nuclear/cytoplasmic
    contexts. Sus1 overexpression/P-body localization and Sgf73 hypoxia-source annotation
    are example-level evidence, not independent proof that the whole DUB module occupies
    every such site. Huh and Dastidar abstracts do not expose all individual supplement
    rows.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-protein-Q6WNK7
  - micro-protein-P53165
  - micro-meta-20230609
  - micro-meta-22932476
  - micro-meta-14562095
- assessment_id: micro-dub-graph
  area: graph
  topic: Coarse membership and deubiquitination graph
  outcome: supported
  summary: Four membership edges, SAGA/SLIK parthood and deubiquitinase function are
    supported at declared NONMECHANISTIC FUNCTION scope; no complete catalytic sequence,
    universal substrate specificity or fixed activity equivalence is asserted.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-wang
  - micro-adamus
  - micro-go-0004843
  - micro-graph-policy
- assessment_id: micro-dxr-identity
  area: identity
  topic: Exact Dxr complex and homodimer scope
  outcome: supported
  summary: GO1990065 denotes the Dxr enzyme complex; IPR003821 exactly grounds its
    constituent family. Author biological assembly1Q0Q has two protein copies, not
    one record per monomer.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-go-1990065
  - micro-go-1990065-ancestors
  - micro-ipr-IPR003821-retry
  - micro-pdb-assembly
  - micro-protein-P45568
- assessment_id: micro-dxr-primary
  area: evidence
  topic: Substrate/cofactor deposition and abstract limits
  outcome: supported
  summary: PDB1Q0Q independently contains DXP and NADPH despite the associated paper
    title emphasizing fosmidomycin. Primary complete abstract distinguishes substrate
    and inhibitor structures and a possible minor substrate stereoisomer. No full
    article body or coordinates were reanalyzed.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-pdb-entry
  - micro-pdb-ligand-2
  - micro-pdb-ligand-3
  - micro-meta-15567415
- assessment_id: micro-dxr-taxon
  area: scope
  topic: Reference protein versus experimental host
  outcome: supported
  summary: P45568 is reviewed E.coli K12 dxr/ispC b0173. Deposited source species562
    and recombinant BL21(DE3) host are distinct from tax83333 reference annotation;
    current species-level canonical example does not falsely assert a living K12 experiment.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-protein-P45568
  - micro-taxon-83333
  - micro-taxon-562
  - micro-pdb-polymer
- assessment_id: micro-dxr-chemistry
  area: graph
  topic: NADPH reaction and coarse dimer function
  outcome: supported
  summary: Explicit maintained functional wording uses NADPH reduction of DXP to MEP;
    native GO0030604 writes the reversible redox reaction in the opposite direction.
    Graph describes dimer assembly/function without asserting every chemical intermediate
    or universal formation necessity.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-go-0030604
  - micro-go-1990065
  - micro-pdb-ligand-3
  - micro-graph-policy
- assessment_id: micro-dxr-unknown
  area: evidence
  topic: Formation and missing physical measurements
  outcome: unknown
  summary: UNKNOWN component formation requirement is preserved; a dimer deposition
    does not establish a universal deletion phenotype. No optional imaging, molecular
    mass or additional instance is required.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-pdb-assembly
  - micro-policy
- assessment_id: micro-eiso-identity
  area: identity
  topic: Whole eisosome versus filament and MCC
  outcome: supported
  summary: GO0032126 includes the membrane/MCC domain and cytoplasmic scaffolding
    filaments. The two maintained neighbors and GO0036286/GO0090512 are genuine child
    boundaries, not alternate identities for the whole.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-go-0032126
  - micro-go-0036286
  - micro-go-0090512
  - micro-neighbor-filament
  - micro-neighbor-mcc
- assessment_id: micro-eiso-refresh
  area: scope
  topic: Substantive current stale-field reassessment
  outcome: supported
  summary: Current PROTEIN_COMPLEX core plus IPR028245 graph grounding is supported
    by native Pil1/Lsp1 family identity and primary assembled scaffold/copurification
    observations. GENE_OR_PROTEIN permits complexes. The record does not require an
    obligate Pil1-Lsp1 heterodimer; Karotki explicitly leaves heterodimer versus mixed
    homodimer architecture unresolved.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-delta-3
  - micro-ipr-IPR028245-retry
  - micro-protein-P53252
  - micro-protein-Q12230
  - micro-walther-html
  - micro-karotki
  - micro-schema
- assessment_id: micro-eiso-primary
  area: evidence
  topic: Discovery, scaffold and membrane-domain evidence
  outcome: supported
  summary: Walther supports immobile assemblies and colocalization; Karotki and Olivera
    supply later self-assembly/membrane-binding/mutant evidence. Current organization
    wording does not assert an exhaustive endocytosis mechanism. Douglas is secondary
    abstract context, not a fresh publisher body.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-walther-html
  - micro-karotki
  - micro-olivera
  - micro-meta-25002088
  - micro-historical-3-micro53-douglas2014-publisher
- assessment_id: micro-eiso-taxon
  area: scope
  topic: Yeast experiments and fungal variability
  outcome: supported
  summary: Native examples are reviewed S288C; primary experiments include W303/S288C
    and recombinant expression/COS7 tests. Fungi VARIABLE is not a prevalence census
    or a claim that every fungus has the same assembly.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-taxon-4751
  - micro-taxon-4932
  - micro-taxon-559292
  - micro-karotki
  - micro-olivera
- assessment_id: micro-eiso-family
  area: grounding
  topic: Core family and Sur7 task
  outcome: supported
  summary: IPR028245 maps the Pil1/Lsp1 constituent class. IPR009571 is broad SUR7/Rim9-like
    context and does not automatically settle an exact Sur7 family task. Preserved
    source-neutral task and historical rationale are not defects merely because taxon-specific
    examples exist.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-ipr-IPR028245-retry
  - micro-ipr-IPR009571
  - micro-protein-P54003
  - micro-policy
- assessment_id: micro-eiso-graph
  area: graph
  topic: Scaffold assembly and localization edges
  outcome: supported
  summary: Primary assembly and membrane-interaction experiments support core-to-filament,
    core-to-MCC scaffold and Sur7 localization edges at current granularity. They
    do not specify an obligatory native heterodimer, every nucleation partner or a
    full signaling mechanism.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-karotki
  - micro-olivera
  - micro-walther-html
  - micro-graph-policy
- assessment_id: micro-eiso-localization
  area: evidence
  topic: Current example-level localization context
  outcome: supported
  summary: PIL1 native lipid-droplet annotation is retained as cited native localization
    context; it does not override independent direct eisosome microscopy. Sur7 membrane
    and Lsp1/core locations have separate primary/authority scope. Moreira abstract
    supports regulated bud assembly, not all molecular details.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-protein-P53252
  - micro-protein-Q12230
  - micro-protein-P54003
  - micro-meta-14562095
  - micro-meta-11784867
  - micro-meta-12469340
  - micro-meta-10.1091_mbc.e08-03-0313
  - micro-karotki
- assessment_id: micro-eiso-kind
  area: schema
  topic: Honest historical failure with incorrect evidence kind
  outcome: concern
  summary: Original micro53-douglas2014-publisher explicitly says HTTP403/no body,
    but kind authority is inappropriate for an access diagnostic. Successor validation/context_only
    preserves its actual historical time/hash. This is not an allegation of fabricated
    full-text access.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-historical-3-micro53-douglas2014-publisher
- assessment_id: micro-proteins-0
  area: grounding
  topic: Current example identity and bounded queries
  outcome: supported
  summary: 3 maintained reviewed examples match native primary genes/aliases, loci
    and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness
    reconstruction. Example annotations do not substitute for source-neutral class
    grounding or entire primary methods.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-protein-P53847
  - micro-protein-P33891
  - micro-protein-Q12745
  - micro-query-DSL1-559292
  - micro-query-DSL3-559292
  - micro-query-SEC39-559292
  - micro-query-TIP20-559292
- assessment_id: micro-adapter-0
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal expression-only exclusion overlooks positive named proteins/pathways.
    Fresh complete catalogue contains no matching yeast dataset; no foreign organism
    proxy or downstream query is invented. Historical runner unavailability is separately
    dated; direct source fallback is actual current work.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-0
  area: scope
  topic: Historical discussion and finding lineage
  outcome: supported
  summary: Two exact original minor findings persist, with the Dsl1 bridge action
    explicitly condition-scoped and global UNKNOWN permitted. Preserve rationale/posed_date
    and all immutable original artifacts; no record edits occur here.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-prior-0
  - micro-delta-0
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-0
  area: schema
  topic: Actual native schema/render and protein coverage
  outcome: supported
  summary: 3 reviewed examples and 3 COVERED typed protein nodes. Both source-head
    native commands exit0; original native validate/render and hashes pass. Success
    is not scientific completeness or a future successor/CI certificate.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-native-dsl1_nzr_complex-verify
  - micro-native-dsl1_nzr_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-0
  area: scope
  topic: Imaging, measurements and unsupported optional completion
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    a pixel/measurement audit. Paper text captions and structural deposit metadata
    are used only at the stated scope. No missing optional physical field is manufactured
    as a finding.
  target_ids:
  - GO:0070939
  evidence_ids:
  - micro-record-0
  - micro-policy
- assessment_id: micro-proteins-1
  area: grounding
  topic: Current example identity and bounded queries
  outcome: supported
  summary: 4 maintained reviewed examples match native primary genes/aliases, loci
    and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness
    reconstruction. Example annotations do not substitute for source-neutral class
    grounding or entire primary methods.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-protein-P50102
  - micro-protein-Q03067
  - micro-protein-Q6WNK7
  - micro-protein-P53165
  - micro-query-SGF11-559292
  - micro-query-SGF73-559292
  - micro-query-SUS1-559292
  - micro-query-UBP8-559292
- assessment_id: micro-adapter-1
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal expression-only exclusion overlooks positive named proteins/pathways.
    Fresh complete catalogue contains no matching yeast dataset; no foreign organism
    proxy or downstream query is invented. Historical runner unavailability is separately
    dated; direct source fallback is actual current work.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-1
  area: scope
  topic: Historical discussion and finding lineage
  outcome: supported
  summary: One exact original minor family-grounding finding persists; broader Ubp8
    task and historical rationale remain open. Preserve rationale/posed_date and all
    immutable original artifacts; no record edits occur here.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-prior-1
  - micro-delta-1
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-1
  area: schema
  topic: Actual native schema/render and protein coverage
  outcome: supported
  summary: 4 reviewed examples and 4 COVERED typed protein nodes. Both source-head
    native commands exit0; original native validate/render and hashes pass. Success
    is not scientific completeness or a future successor/CI certificate.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-native-dubm_complex-verify
  - micro-native-dubm_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-1
  area: scope
  topic: Imaging, measurements and unsupported optional completion
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    a pixel/measurement audit. Paper text captions and structural deposit metadata
    are used only at the stated scope. No missing optional physical field is manufactured
    as a finding.
  target_ids:
  - GO:0071819
  evidence_ids:
  - micro-record-1
  - micro-policy
- assessment_id: micro-proteins-2
  area: grounding
  topic: Current example identity and bounded queries
  outcome: supported
  summary: 1 maintained reviewed examples match native primary genes/aliases, loci
    and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness
    reconstruction. Example annotations do not substitute for source-neutral class
    grounding or entire primary methods.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-protein-P45568
  - micro-query-dxr-83333
  - micro-query-ispC-83333
- assessment_id: micro-adapter-2
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal expression-only exclusion overlooks positive named proteins/pathways.
    Fresh five-strain E.coli precise1k context selects b0173 dxr/P45568; one UC-2
    hit among201, Unknown function, verified in96-member list. Expression context
    does not establish physical dimerization or necessity. Historical runner unavailability
    is separately dated; direct source fallback is actual current work.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-adapter-meta
  - micro-adapter-dxr-memberships
  - micro-adapter-gene-dxr
  - micro-adapter-module167
  - micro-adapter-module167-genes
- assessment_id: micro-history-2
  area: scope
  topic: Historical discussion and finding lineage
  outcome: supported
  summary: Original qualified-pass outcome remains supported within present access
    limits; no new scientific finding. Preserve rationale/posed_date and all immutable
    original artifacts; no record edits occur here.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-prior-2
  - micro-delta-2
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-2
  area: schema
  topic: Actual native schema/render and protein coverage
  outcome: supported
  summary: 1 reviewed examples and 1 COVERED typed protein nodes. Both source-head
    native commands exit0; original native validate/render and hashes pass. Success
    is not scientific completeness or a future successor/CI certificate.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-native-dxr_protein_complex-verify
  - micro-native-dxr_protein_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-2
  area: scope
  topic: Imaging, measurements and unsupported optional completion
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    a pixel/measurement audit. Paper text captions and structural deposit metadata
    are used only at the stated scope. No missing optional physical field is manufactured
    as a finding.
  target_ids:
  - GO:1990065
  evidence_ids:
  - micro-record-2
  - micro-policy
- assessment_id: micro-proteins-3
  area: grounding
  topic: Current example identity and bounded queries
  outcome: supported
  summary: 3 maintained reviewed examples match native primary genes/aliases, loci
    and taxon. Exact current reviewed-gene queries are singleton; no historical uniqueness
    reconstruction. Example annotations do not substitute for source-neutral class
    grounding or entire primary methods.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-protein-P53252
  - micro-protein-Q12230
  - micro-protein-P54003
  - micro-query-LSP1-559292
  - micro-query-PIL1-559292
  - micro-query-SUR7-559292
- assessment_id: micro-adapter-3
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original unsupported prose exclusion overlooks positive named proteins/pathways.
    Fresh complete catalogue contains no matching yeast dataset; no foreign organism
    proxy or downstream query is invented. Historical runner unavailability is separately
    dated; direct source fallback is actual current work.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-3
  area: scope
  topic: Historical discussion and finding lineage
  outcome: supported
  summary: Stale changes are substantively accepted within explicit native architecture
    limits; historical issue mentions are provenance only, not broad group closure.
    Preserve rationale/posed_date and all immutable original artifacts; no record
    edits occur here.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-prior-3
  - micro-delta-3
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-3
  area: schema
  topic: Actual native schema/render and protein coverage
  outcome: supported
  summary: 3 reviewed examples and 2 COVERED typed protein nodes. Both source-head
    native commands exit0; original native validate/render and hashes pass. Success
    is not scientific completeness or a future successor/CI certificate.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-native-eisosome-verify
  - micro-native-eisosome-causal
  - micro-original-audit
- assessment_id: micro-physical-3
  area: scope
  topic: Imaging, measurements and unsupported optional completion
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    a pixel/measurement audit. Paper text captions and structural deposit metadata
    are used only at the stated scope. No missing optional physical field is manufactured
    as a finding.
  target_ids:
  - GO:0032126
  evidence_ids:
  - micro-record-3
  - micro-policy
- assessment_id: plaque-t4-identity-hierarchy
  area: identity
  topic: identity-hierarchy
  outcome: supported
  summary: The minted ejectisome identity and broad membrane-bounded parent are consistent
    with the described cryptophyte organelle. A bounded zero-result GO name search
    is not exhaustive absence proof.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-go
  - plaque-go-ejectisome-search
  - plaque-curation
- assessment_id: plaque-t4-composition-and-grounding
  area: grounding
  topic: composition-and-grounding
  outcome: supported
  summary: Ejectisin is a measured small-polypeptide constituent class; the bounded
    native query did not establish an exact full-class CURIE. Preserve REVIEWED_LABEL_ONLY
    and its TODO rather than guess an accession or demand an optional example.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-pmid-22868567
  - plaque-ipr-search-ejectisin
  - plaque-curation
- assessment_id: plaque-t4-native-protein-identity
  area: grounding
  topic: native-protein-identity
  outcome: supported
  summary: Zero protein_examples; one GENE_OR_PROTEIN ejectisin node is NO_GENE_SYMBOLS.
    This honest diagnostic is not an optional-example defect. Native exact gene/locus
    identities are correct, but a generic verification pass does not independently
    establish source-stage support.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-native-ejectisome-verify
  - plaque-native-ejectisome-causal
  - plaque-protein-skill
- assessment_id: plaque-t4-primary-source-scope
  area: evidence
  topic: primary-source-scope
  outcome: supported
  summary: Rhiel is assessed at complete abstract/metadata tier. Ammermann additionally
    has bounded author-text Methods/Results inspection of purified discharged fragments
    and reconstituted filaments; older resting-organelle statements in its Introduction
    are secondary context. No image-pixel claim is made.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-pmid-21336864
  - plaque-pmid-22868567
  - plaque-ammermann-web1
  - plaque-ammermann-web2
  - plaque-rhiel-publisher
- assessment_id: plaque-t4-taxon-and-experimental-context
  area: scope
  topic: taxon-and-experimental-context
  outcome: supported
  summary: Cryptophyceae and Chroomonas IDs have class/genus ranks. Chroomonas LT
    and Cryptomonas S2/LT experimental labels are not a verified species/strain CURIE;
    Guillardia sequence correspondence does not define every cryptophyte ejectisome.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-tax-3027
  - plaque-tax-3028
  - plaque-ammermann-web1
  - plaque-pmid-22868567
- assessment_id: plaque-t4-quantity-and-architecture
  area: quantity
  topic: quantity-and-architecture
  outcome: supported
  summary: The approximately6kDa ejectisin statement is bounded to biochemical preparations;
    no molecular copy count or intact-organelle assembly is inferred from the isolated
    filament experiment.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-pmid-22868567
- assessment_id: plaque-t4-formation-versus-function
  area: evidence
  topic: formation-versus-function
  outcome: unknown
  summary: Ejectisin purification/reaggregation supports a filament material role,
    not necessity for formation of the complete intact organelle. UNKNOWN is retained
    without an invented mandatory experiment.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-curation
  - plaque-structure-schema
  - plaque-pmid-22868567
- assessment_id: plaque-t4-causal-graph-and-localisation
  area: graph
  topic: causal-graph-and-localisation
  outcome: supported
  summary: The NON_MECHANISTIC graph links a protein constituent class and discharge-associated
    structure without a detailed molecular mechanism. Native NO_GENE_SYMBOLS is a
    scoped diagnostic, not an unsupported optional-field finding.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-native-ejectisome-verify
  - plaque-native-ejectisome-causal
  - plaque-graph-skill
  - plaque-structure-schema
  - plaque-pmid-22868567
- assessment_id: plaque-t4-structured-source-applicability
  area: evidence
  topic: structured-source-applicability
  outcome: supported
  summary: Positive ejectisin protein/sequence and typed constituent assertions trigger
    the broad native structured-source policy. The complete fresh catalogue has no
    matching natural host; no downstream dataset is invented and no recombinant E.coli
    proxy is substituted. The old expression-only notes[1] exclusion is unsupported,
    even though the present bounded no-coverage outcome is legitimate. Historical
    runner unavailability remains historical; no fresh runner invocation is claimed.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-review-skill
  - plaque-catalogue
  - plaque-rubric
- assessment_id: plaque-t4-history-and-source-classification
  area: provenance
  topic: history-and-source-classification
  outcome: concern
  summary: All three target hashes remain unchanged; no historical record correction
    or terminal predecessor disposition is inferred. Two historical HTTP200 Client
    Challenge observations are honestly context_only but incorrectly typed authority;
    correct only the successor kind, retaining actual old URL/time/hash. Current successful
    routes are separate evidence.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-original-4-yaml
  - plaque-original-4-md
  - plaque-curation
  - plaque-review-contract
  - plaque-input-original-proof
- assessment_id: plaque-t4-schema-provenance-and-verdict
  area: schema
  topic: schema-provenance-and-verdict
  outcome: supported
  summary: Original YAML validates and exactly renders its immutable Markdown;41 historical
    occurrences and49 current frozen inputs match. Qualified pass retained, with source-access
    and mapping limits; no scientific finding is manufactured. This is not certification
    of future CI, queue or merge.
  target_ids:
  - cellstructuremech:ejectisome
  evidence_ids:
  - plaque-record-4
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-original-4-yaml
  - plaque-native-ejectisome-verify
  - plaque-native-ejectisome-causal
- assessment_id: plaque-t5-identity-hierarchy
  area: identity
  topic: identity-hierarchy
  outcome: supported
  summary: GO0031391 identifies the Elg1/RFC2–5 alternative complex, not canonical
    RFC or the Ctf18/Rad24 alternatives.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-go-elg1-ancestors
  - plaque-curation
- assessment_id: plaque-t5-composition-and-grounding
  area: grounding
  topic: composition-and-grounding
  outcome: supported
  summary: Five intended protein classes and individual examples agree. New Elg1 domain
    entries and broad small-RFC families are not exact full-protein mappings; this
    review does not fabricate an exact-grounding correction.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-ipr-IPR062598
  - plaque-ipr-IPR062602
  - plaque-ipr-IPR050238
  - plaque-ipr-search-Elg1
  - plaque-up-Q12050
  - plaque-up-P40348
  - plaque-up-P38629
  - plaque-up-P40339
  - plaque-up-P38251
  - plaque-curation
- assessment_id: plaque-t5-native-protein-identity
  area: grounding
  topic: native-protein-identity
  outcome: supported
  summary: Five reviewed protein_examples; five typed protein nodes are COVERED. Native
    exact gene/locus identities are correct, but a generic verification pass does
    not independently establish source-stage support.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-native-elg1_rfc_like_complex-verify
  - plaque-native-elg1_rfc_like_complex-causal
  - plaque-up-Q12050
  - plaque-up-P40348
  - plaque-up-P38629
  - plaque-up-P40339
  - plaque-up-P38251
  - plaque-gene-ELG1
  - plaque-gene-RFC2
  - plaque-gene-RFC3
  - plaque-gene-RFC4
  - plaque-gene-RFC5
  - plaque-tax-559292
- assessment_id: plaque-t5-primary-source-scope
  area: evidence
  topic: primary-source-scope
  outcome: supported
  summary: Kubota primary abstract directly supports PCNA unloading/degron-restoration
    and purified-complex function; full body access remains blocked. Kim/MacNeill
    and Kupiec are secondary abstracts, not primary experiments. No unread assay detail
    is supplied.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-pmid-23499004
  - plaque-pmid-14614842
  - plaque-pmid-27664980
  - plaque-kubota-publisher
- assessment_id: plaque-t5-taxon-and-experimental-context
  area: scope
  topic: taxon-and-experimental-context
  outcome: supported
  summary: S. cerevisiae species4932 and S288C reference559292 are distinguished.
    Exact reference accessions do not silently identify experimental strain backgrounds.
    The accessed Kubota abstract does not establish a precise experimental strain.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-pmid-23499004
- assessment_id: plaque-t5-quantity-and-architecture
  area: quantity
  topic: quantity-and-architecture
  outcome: supported
  summary: The five distinct subunits support the stated pentameric Elg1-RFC class;
    no unsupported universal kinetics or absolute unloading mechanism is added.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-pmid-23499004
- assessment_id: plaque-t5-formation-versus-function
  area: evidence
  topic: formation-versus-function
  outcome: unknown
  summary: PCNA unloading and genome-stability outcomes are functional evidence. The
    accessed abstract does not establish individual-subunit requirements for formation;
    UNKNOWN rows are not automatically defects.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-curation
  - plaque-structure-schema
  - plaque-pmid-23499004
- assessment_id: plaque-t5-causal-graph-and-localisation
  area: graph
  topic: causal-graph-and-localisation
  outcome: supported
  summary: The NON_MECHANISTIC graph keeps membership and PCNA unloading separate;
    reviewed examples anchor five typed nodes. Identity and function are supported
    within native authority/abstract limits.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-native-elg1_rfc_like_complex-verify
  - plaque-native-elg1_rfc_like_complex-causal
  - plaque-graph-skill
  - plaque-structure-schema
  - plaque-pmid-23499004
- assessment_id: plaque-t5-structured-source-applicability
  area: evidence
  topic: structured-source-applicability
  outcome: supported
  summary: Positive named protein components and PCNA-unloading pathway claims trigger
    the broad native structured-source policy. The complete fresh catalogue has no
    matching natural host; no downstream dataset is invented and no recombinant E.coli
    proxy is substituted. The old expression-only notes[1] exclusion is unsupported,
    even though the present bounded no-coverage outcome is legitimate. Historical
    runner unavailability remains historical; no fresh runner invocation is claimed.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-review-skill
  - plaque-catalogue
  - plaque-rubric
- assessment_id: plaque-t5-history-and-source-classification
  area: provenance
  topic: history-and-source-classification
  outcome: concern
  summary: All three target hashes remain unchanged; no historical record correction
    or terminal predecessor disposition is inferred. Three historical TLS/browser403/publisher403
    observations are honestly context_only but incorrectly typed authority; correct
    only the successor kind, retaining actual old URL/time/hash. Current successful
    routes are separate evidence.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-original-5-yaml
  - plaque-original-5-md
  - plaque-curation
  - plaque-review-contract
  - plaque-input-original-proof
- assessment_id: plaque-t5-schema-provenance-and-verdict
  area: schema
  topic: schema-provenance-and-verdict
  outcome: supported
  summary: Original YAML validates and exactly renders its immutable Markdown;41 historical
    occurrences and49 current frozen inputs match. Qualified pass retained, with source-access
    and mapping limits; no scientific finding is manufactured. This is not certification
    of future CI, queue or merge.
  target_ids:
  - GO:0031391
  evidence_ids:
  - plaque-record-5
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-original-5-yaml
  - plaque-native-elg1_rfc_like_complex-verify
  - plaque-native-elg1_rfc_like_complex-causal
- assessment_id: plaque-t6-identity-hierarchy
  area: identity
  topic: identity-hierarchy
  outcome: concern
  summary: GO0033588 is the correct complex identifier and is quoted faithfully; its
    old heterohexamer/two-trimer architecture conflicts with newer measured assembly
    stoichiometry. Keep identity while distinguishing six protein species from copy
    number.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-go
  - plaque-PMC5286391-legacy
  - plaque-curation
- assessment_id: plaque-t6-composition-and-grounding
  area: grounding
  topic: composition-and-grounding
  outcome: concern
  summary: 'All six exact full-protein family mappings are independently confirmed
    by native family types and correct example memberships: Elp1 IPR006849, Elp2 IPR037289,
    Elp3 IPR034687, Elp4 IPR008728, Elp5 IPR019519, Elp6 IPR018627. Broader domains
    and IPR039661 are not substitutes.'
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-ipr-IPR006849
  - plaque-ipr-IPR037289
  - plaque-ipr-IPR034687
  - plaque-ipr-IPR008728
  - plaque-ipr-IPR019519
  - plaque-ipr-IPR018627
  - plaque-ipr-IPR039661
  - plaque-up-Q06706
  - plaque-up-P42935
  - plaque-up-Q02908
  - plaque-up-Q02884
  - plaque-up-P38874
  - plaque-up-Q04868
  - plaque-curation
- assessment_id: plaque-t6-native-protein-identity
  area: grounding
  topic: native-protein-identity
  outcome: supported
  summary: Six reviewed protein_examples; six typed protein nodes are COVERED. Correct
    references are S288C; ELP1/ELP5 are aliases of native primary names IKI3/IKI1,
    not mismatches. Exact-organism searches establish bounded identity only.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-native-elongator_holoenzyme_complex-verify
  - plaque-native-elongator_holoenzyme_complex-causal
  - plaque-up-Q06706
  - plaque-up-P42935
  - plaque-up-Q02908
  - plaque-up-Q02884
  - plaque-up-P38874
  - plaque-up-Q04868
  - plaque-gene-ELP1
  - plaque-gene-ELP2
  - plaque-gene-ELP3
  - plaque-gene-ELP4
  - plaque-gene-ELP5
  - plaque-gene-ELP6
  - plaque-tax-559292
- assessment_id: plaque-t6-primary-source-scope
  area: evidence
  topic: primary-source-scope
  outcome: supported
  summary: Krogan2001 six-species inventory and Huang2005 tRNA modification evidence
    are distinguished from later Setiaputra/Dauden physical architecture. Full selected
    primary Methods/Results and text captions were read; no figure-pixel or raw-data
    reanalysis.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-PMC5286391-legacy
  - plaque-PMC5286394-legacy
  - plaque-PMC99985-legacy
  - plaque-PMC1370732-legacy
- assessment_id: plaque-t6-taxon-and-experimental-context
  area: scope
  topic: taxon-and-experimental-context
  outcome: supported
  summary: S. cerevisiae species4932 and S288C reference559292 are distinguished.
    Exact reference accessions do not silently identify experimental strain backgrounds.
    Krogan uses W303-derived strains; Dauden BS1173/BSY2369; Setiaputra supplementary
    strain table was not inspected. E.coli recombinant expression is not natural taxon
    evidence.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-PMC99985-legacy
  - plaque-PMC5286394-legacy
  - plaque-PMC5286391-legacy
- assessment_id: plaque-t6-quantity-and-architecture
  area: quantity
  topic: quantity-and-architecture
  outcome: concern
  summary: Two Elp123 units plus a majority one Elp456 heterohexamer support the characterized12-subunit
    assembly, while lower salt and added recombinant ring conditions allow two Elp456
    rings. Six distinct proteins is not an invariant six-copy holoenzyme, and replacement
    wording must preserve variable ring occupancy.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-PMC5286391-legacy
  - plaque-PMC5286394-legacy
  - plaque-PMC99985-legacy
- assessment_id: plaque-t6-formation-versus-function
  area: evidence
  topic: formation-versus-function
  outcome: concern
  summary: FLAG-Elp4 purification after elp1 deletion loses Elp2/3 association while
    Elp456 persists. Record this measured condition-specific assembly association,
    separate from Huang catalytic-output loss and viability. A global UNKNOWN may
    remain if its enum cannot express the tested scope; no universal six-subunit necessity
    is required.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-curation
  - plaque-structure-schema
  - plaque-PMC5286391-legacy
  - plaque-PMC1370732-legacy
- assessment_id: plaque-t6-causal-graph-and-localisation
  area: graph
  topic: causal-graph-and-localisation
  outcome: concern
  summary: Six covered typed nodes preserve component identities and broad tRNA-wobble
    function. Graph description must distinguish identities from physical copy number.
    Historical transcription/localisation citations are not all formation evidence;
    Huh individual images were not viewed.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-native-elongator_holoenzyme_complex-verify
  - plaque-native-elongator_holoenzyme_complex-causal
  - plaque-graph-skill
  - plaque-structure-schema
  - plaque-PMC1370732-legacy
  - plaque-PMC5286391-legacy
  - plaque-pmid-14562095
  - plaque-pmid-15780940
  - plaque-pmid-10024884
  - plaque-pmid-24750273
- assessment_id: plaque-t6-structured-source-applicability
  area: evidence
  topic: structured-source-applicability
  outcome: supported
  summary: Positive protein components and tRNA-modification pathway claims trigger
    the broad native structured-source policy. The complete fresh catalogue has no
    matching natural host; no downstream dataset is invented and no recombinant E.coli
    proxy is substituted. The old expression-only formal check is unsupported, even
    though the present bounded no-coverage outcome is legitimate. Historical runner
    unavailability remains historical; no fresh runner invocation is claimed.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-review-skill
  - plaque-catalogue
  - plaque-rubric
- assessment_id: plaque-t6-history-and-source-classification
  area: provenance
  topic: history-and-source-classification
  outcome: concern
  summary: All three target hashes remain unchanged; no historical record correction
    or terminal predecessor disposition is inferred. No additional historical failed-access
    kind defect was found in this assigned original. Preserve the dated rationale
    and append current architecture/family evidence; do not rewrite the historical
    why.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-original-6-md
  - plaque-curation
  - plaque-review-contract
  - plaque-input-original-proof
- assessment_id: plaque-t6-schema-provenance-and-verdict
  area: schema
  topic: schema-provenance-and-verdict
  outcome: concern
  summary: Original YAML validates and exactly renders its immutable Markdown;41 historical
    occurrences and49 current frozen inputs match. Needs_curation retained for the
    three reconfirmed inherited findings, one major architecture and two minor bounded
    mapping/association corrections. Record curation remains outside this PR. This
    is not certification of future CI, queue or merge.
  target_ids:
  - GO:0033588
  evidence_ids:
  - plaque-record-6
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-original-6-yaml
  - plaque-native-elongator_holoenzyme_complex-verify
  - plaque-native-elongator_holoenzyme_complex-causal
- assessment_id: septin-emc_complex-identity
  area: identity
  topic: Exact complex identity and anatomical boundary
  outcome: supported
  summary: Exact EMC GO identity retained; eight-member yeast source differs from
    the older six-name definition and mammalian source complexes.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
- assessment_id: septin-emc_complex-hierarchy
  area: identity
  topic: Parents,parthood and synonyms
  outcome: supported
  summary: Membrane-protein parent and ER membrane parthood preserve distinct is-a/part-of
    relations; BROAD synonyms remain explicitly qualified.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
- assessment_id: septin-emc_complex-components
  area: completeness
  topic: Inventory and exact molecular scope
  outcome: concern
  summary: Deferral of all eight source-established yeast constituents is actionable;
    unresolved exact families or individual necessity do not require suppressing supported
    label-only membership. This is an explicit deferral,not a universal optional-field
    mandate.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-curation-policy
- assessment_id: septin-emc_complex-protein-identity
  area: grounding
  topic: Accession,primary name,alias and native inventory
  outcome: concern
  summary: EMC has no native examples/nodes. Independent reviewed reference identities
    are EMC3/AIM27/P36039/YKL207W and EMC5/KRE27/P40540/YIL027C; dated rationale reverses
    aliases. Append correction without rewriting history.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-native-emc_complex-verify
  - septin-native-emc_complex-causal
  - septin-peer-protein-P36039
  - septin-peer-protein-P40540
  - septin-protein-policy
- assessment_id: septin-emc_complex-source-experiments
  area: evidence
  topic: Primary experiments and access scope
  outcome: supported
  summary: Bai yeast native purification/mass spectrometry/structure, Guna selected
    TA reconstitution and Chitwood selected first-TMD insertion support bounded record
    claims. Human O'Donnell pathway remains a proposed structural model,not a complete
    measured cycle.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-literature-policy
- assessment_id: septin-emc_complex-quantities
  area: grounding
  topic: Stoichiometry and measured scope
  outcome: supported
  summary: Eight yeast subunits established in Bai preparation; no single fixed mammalian
    count is imposed.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
- assessment_id: septin-emc_complex-formation
  area: grounding
  topic: Formation necessity versus membership and activity
  outcome: unknown
  summary: Transport/insertion,growth and structural membership do not automatically
    establish a universal formation requirement. Bai Emc3K26L complex stays intact
    despite function defects; prospective constituent rows may retain UNKNOWN.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-schema-policy
- assessment_id: septin-emc_complex-graph
  area: graph
  topic: Whole causal graph and substantive stale refresh
  outcome: supported
  summary: NONMECHANISTIC/FUNCTION insertion/Sec61 graph is appropriately coarse;
    selected substrates and sequence of tested TMDs constrain interpretation.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-graph-policy
- assessment_id: septin-emc_complex-taxa
  area: scope
  topic: Biological and experimental host scope
  outcome: supported
  summary: Yeast4932 canonical source is W303-1a in Bai; reference aliases are S288c559292.
    Human/HEK/U2OS functional papers are comparative,not yeast experiments. Qualitative
    COMMON/VARIABLE labels are not prevalence surveys.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-tax4932
- assessment_id: septin-emc_complex-citations
  area: provenance
  topic: Citation and evidence attribution
  outcome: supported
  summary: Exact cited authors/DOIs/PMIDs match current authority metadata. Primary
    scientific support is limited to the expressly inspected bodies/abstracts and
    native authority fields.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-literature-policy
- assessment_id: septin-emc_complex-adapter
  area: evidence
  topic: Complete-record structured-source applicability
  outcome: supported
  summary: Positive protein/insertion/transport narratives require actual assessment;
    original no-expression exclusion is unsupported. Complete fresh catalogue has
    no yeast/human host; unrelated bacterial data are not proxies.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-meta
  - septin-adapter-modules
  - septin-adapter-runner-historical
- assessment_id: septin-emc_complex-schema
  area: schema
  topic: Original native validation/render and current inputs
  outcome: supported
  summary: Original pair native validate/render0 and historical hashes match. Current
    target remains byte-identical to its frozen input. Native protein checks0 are
    scope-limited; CI is separate.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-original-native-checks
  - septin-native-emc_complex-verify
  - septin-native-emc_complex-causal
- assessment_id: septin-emc_complex-history
  area: provenance
  topic: Append-only rationale and old finding lineage
  outcome: supported
  summary: Preserve all dated rationale/history. Exact inherited keys remain traceable;
    update current notes/status or append clarification during separately authorized
    curation. No history rewrite is requested.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-curation-policy
- assessment_id: septin-emc_complex-coverage
  area: completeness
  topic: Complete record and limitations
  outcome: supported
  summary: All definition,aliases,parents,components/examples,taxa,functions,quantities,source
    notes,graph edges,discussions/history read. No maintained images; captions are
    not pixels. No exhaustive literature-absence claim or automatic optional-field
    demand.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-literature-policy
- assessment_id: septin-emc_complex-verdict
  area: consistency
  topic: Current independent scientific disposition
  outcome: concern
  summary: Needs curation for two inherited minor inventory/alias findings, with append-only
    correction.
  target_ids:
  - GO:0072546
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-go
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-curation-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-identity
  area: identity
  topic: Exact complex identity and anatomical boundary
  outcome: supported
  summary: Specific local EmrAB-TolC identity justified by CPX4268; broader GO1990281
    retained as class,not exact replacement.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-hierarchy
  area: identity
  topic: Parents,parthood and synonyms
  outcome: supported
  summary: Efflux-pump parent,CPXxref and functional synonyms remain correctly scoped
    to tripartite complex.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-components
  area: completeness
  topic: Inventory and exact molecular scope
  outcome: concern
  summary: Current EmrA label-only and broad EmrB grounding remain actionable given
    exact NF011715/NF000391 and native joins; TolC exact family remains supported.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-ncbifam-NF011715
  - septin-ncbifam-NF000391
  - septin-ipr-IPR004638
  - septin-ipr-IPR058622
  - septin-curation-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-protein-identity
  area: grounding
  topic: Accession,primary name,alias and native inventory
  outcome: supported
  summary: 3 reviewed K12 examples and 3 COVERED nodes match exact primary gene/status/accession
    and current singleton queries. Reference annotation does not identify every experimental
    expression strain.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-native-emrab_tolc_multidrug_efflux_transport_complex-verify
  - septin-native-emrab_tolc_multidrug_efflux_transport_complex-causal
  - septin-protein-P27303
  - septin-protein-P0AEJ0
  - septin-protein-P02930
  - septin-gene-emrA-83333
  - septin-gene-emrB-83333
  - septin-gene-tolC-83333
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-source-experiments
  area: evidence
  topic: Primary experiments and access scope
  outcome: supported
  summary: Modern Zhong complete pump6:1:3 architecture and native CPX composition
    are distinct from Borges-Walmsley proposed EmrA trimer and Yousefian low-resolution
    whole-pump abstract. Modern engineered EA is inactive; FA and wild-type assays
    provide separate functional evidence.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-literature-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-quantities
  area: grounding
  topic: Stoichiometry and measured scope
  outcome: supported
  summary: CPX explicit participants and8ZAL deposited model agree EmrA6,EmrB1,TolC3,total10.
    Engineered EA modeled chain count is not a universal native-state experimental
    stoichiometry guarantee.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-formation
  area: grounding
  topic: Formation necessity versus membership and activity
  outcome: unknown
  summary: Transport/insertion,growth and structural membership do not automatically
    establish a universal formation requirement. Existing ESSENTIAL components denote
    defining tripartite membership, but new CPX evidence notes must not attribute
    an unprovided essentiality classification; no blanket retyping of these older
    values is demanded by this narrow finding.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-schema-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-graph
  area: graph
  topic: Whole causal graph and substantive stale refresh
  outcome: concern
  summary: All four new edges substantively refreshed. Three protein contributions
    and coupled outer export remain supported, but their CPX notes falsely credit
    native authority with essentiality classification. Scope correction concerns attribution,not
    denial of pump assembly or efflux.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-graph-policy
  - septin-emrab-stale-diff
  - septin-eco0005547
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-taxa
  area: scope
  topic: Biological and experimental host scope
  outcome: supported
  summary: CPX/native examplesK12; Zhong gene sourceMG1655 differs from C43(DE3)delta-acrAB
    assay host and engineered constructs. Qualitative COMMON/VARIABLE labels are not
    prevalence surveys.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-tax562
  - septin-tax83333
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-citations
  area: provenance
  topic: Citation and evidence attribution
  outcome: concern
  summary: Exact cited authors/DOIs/PMIDs match current authority metadata. New CPX
    essentiality notes are the separate concrete source-attribution defect; old and
    new measured sources remain distinguished.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-literature-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-adapter
  area: evidence
  topic: Complete-record structured-source applicability
  outcome: supported
  summary: 'Positive protein/insertion/transport narratives require actual assessment;
    original no-expression exclusion is unsupported. Matched reference E.coli precise1k
    bounds: tolC has SoxS22 membership; emrA/emrB no thresholded hit. No expression→assembly
    inference.'
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-meta
  - septin-adapter-modules
  - septin-adapter-runner-historical
  - septin-modulegene-emrA
  - septin-modulegene-emrB
  - septin-modulegene-tolC
  - septin-modulemembers-emrA
  - septin-modulemembers-emrB
  - septin-modulemembers-tolC
  - septin-module-22
  - septin-module-22-genes
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-schema
  area: schema
  topic: Original native validation/render and current inputs
  outcome: supported
  summary: Original pair native validate/render0 and historical hashes match. Current
    target is stale and all four new edges/history assessed independently. Native
    protein checks0 are scope-limited; CI is separate.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-native-checks
  - septin-native-emrab_tolc_multidrug_efflux_transport_complex-verify
  - septin-native-emrab_tolc_multidrug_efflux_transport_complex-causal
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-history
  area: provenance
  topic: Append-only rationale and old finding lineage
  outcome: supported
  summary: Preserve all dated rationale/history. Exact inherited keys remain traceable;
    update current notes/status or append clarification during separately authorized
    curation. No history rewrite is requested.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-curation-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-coverage
  area: completeness
  topic: Complete record and limitations
  outcome: supported
  summary: All definition,aliases,parents,components/examples,taxa,functions,quantities,source
    notes,graph edges,discussions/history read. No maintained images; captions are
    not pixels. No exhaustive literature-absence claim or automatic optional-field
    demand.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-literature-policy
- assessment_id: septin-emrab_tolc_multidrug_efflux_transport_complex-verdict
  area: consistency
  topic: Current independent scientific disposition
  outcome: concern
  summary: Needs curation for inherited exact-family minor and narrow new CPX attribution
    minor; stale review can be refreshed within review bundles without record edits.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-go
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-ncbifam-NF011715
  - septin-ncbifam-NF000391
  - septin-ipr-IPR004638
  - septin-ipr-IPR058622
  - septin-curation-policy
- assessment_id: septin-emre_multidrug_transporter_complex-identity
  area: identity
  topic: Exact complex identity and anatomical boundary
  outcome: supported
  summary: Exact GO1990207 and TPP-bound EmrE homodimer retained; broad SMR family
    is not the whole complex.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
- assessment_id: septin-emre_multidrug_transporter_complex-hierarchy
  area: identity
  topic: Parents,parthood and synonyms
  outcome: supported
  summary: Transmembrane-transporter parent and narrow EmrE synonym remain appropriate.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
- assessment_id: septin-emre_multidrug_transporter_complex-components
  area: completeness
  topic: Inventory and exact molecular scope
  outcome: concern
  summary: Exact NF042984 supports named EmrE constituent; broader NF007087/IPR045324
    do not justify permanent label-only deferral.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-ncbifam-NF042984
  - septin-ncbifam-NF007087
  - septin-ipr-IPR045324
  - septin-curation-policy
- assessment_id: septin-emre_multidrug_transporter_complex-protein-identity
  area: grounding
  topic: Accession,primary name,alias and native inventory
  outcome: supported
  summary: 1 reviewed K12 examples and 1 COVERED nodes match exact primary gene/status/accession
    and current singleton queries. Reference annotation does not identify every experimental
    expression strain.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-native-emre_multidrug_transporter_complex-verify
  - septin-native-emre_multidrug_transporter_complex-causal
  - septin-protein-P23895
  - septin-gene-emrE-83333
- assessment_id: septin-emre_multidrug_transporter_complex-source-experiments
  area: evidence
  topic: Primary experiments and access scope
  outcome: supported
  summary: Chen corrected TPP-bound dimer supports orientation and drug-binding scope;
    earlier distorted acidic apo and defunct structures are not substituted. No all-SMR
    or full kinetic mechanism asserted.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-literature-policy
- assessment_id: septin-emre_multidrug_transporter_complex-quantities
  area: grounding
  topic: Stoichiometry and measured scope
  outcome: supported
  summary: Two EmrE subunits verified in3B5D assembly; binding protein:drug ratio2:1
    is a different quantity.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
- assessment_id: septin-emre_multidrug_transporter_complex-formation
  area: grounding
  topic: Formation necessity versus membership and activity
  outcome: unknown
  summary: Transport/insertion,growth and structural membership do not automatically
    establish a universal formation requirement. Current UNKNOWN is preserved; corrected
    dimer structure and binding assays do not force a universal formation flag.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-schema-policy
- assessment_id: septin-emre_multidrug_transporter_complex-graph
  area: graph
  topic: Whole causal graph and substantive stale refresh
  outcome: supported
  summary: FUNCTION/MECHANISTIC graph describes directly supported antiparallel assembly
    and coarse drug transport; no detailed alternating-access/proton cycle is inferred
    from coordinates.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-graph-policy
- assessment_id: septin-emre_multidrug_transporter_complex-taxa
  area: scope
  topic: Biological and experimental host scope
  outcome: supported
  summary: GO common-bacterial wording does not imply universalBacteria2 presence;
    K12 reference protein differs from BL21(DE3) recombinant and cell-free sources.
    Qualitative COMMON/VARIABLE labels are not prevalence surveys.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-tax2
  - septin-tax83333
- assessment_id: septin-emre_multidrug_transporter_complex-citations
  area: provenance
  topic: Citation and evidence attribution
  outcome: supported
  summary: Exact cited authors/DOIs/PMIDs match current authority metadata. Primary
    scientific support is limited to the expressly inspected bodies/abstracts and
    native authority fields.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-literature-policy
- assessment_id: septin-emre_multidrug_transporter_complex-adapter
  area: evidence
  topic: Complete-record structured-source applicability
  outcome: supported
  summary: Positive protein/insertion/transport narratives require actual assessment;
    original no-expression exclusion is unsupported. Matched E.coli precise1k emrE
    belongs to ROS TALE Amp9; this expression context does not establish homodimer
    topology or necessity.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-meta
  - septin-adapter-modules
  - septin-adapter-runner-historical
  - septin-modulegene-emrE
  - septin-modulemembers-emrE
  - septin-module-9
  - septin-module-9-genes
- assessment_id: septin-emre_multidrug_transporter_complex-schema
  area: schema
  topic: Original native validation/render and current inputs
  outcome: supported
  summary: Original pair native validate/render0 and historical hashes match. Current
    target remains byte-identical to its frozen input. Native protein checks0 are
    scope-limited; CI is separate.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-original-native-checks
  - septin-native-emre_multidrug_transporter_complex-verify
  - septin-native-emre_multidrug_transporter_complex-causal
- assessment_id: septin-emre_multidrug_transporter_complex-history
  area: provenance
  topic: Append-only rationale and old finding lineage
  outcome: supported
  summary: Preserve all dated rationale/history. Exact inherited keys remain traceable;
    update current notes/status or append clarification during separately authorized
    curation. No history rewrite is requested.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-curation-policy
- assessment_id: septin-emre_multidrug_transporter_complex-coverage
  area: completeness
  topic: Complete record and limitations
  outcome: supported
  summary: All definition,aliases,parents,components/examples,taxa,functions,quantities,source
    notes,graph edges,discussions/history read. No maintained images; captions are
    not pixels. No exhaustive literature-absence claim or automatic optional-field
    demand.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-literature-policy
- assessment_id: septin-emre_multidrug_transporter_complex-verdict
  area: consistency
  topic: Current independent scientific disposition
  outcome: concern
  summary: Needs curation for inherited exact-family minor, retaining correct dimer/source
    biology.
  target_ids:
  - GO:1990207
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-go
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-ncbifam-NF042984
  - septin-ncbifam-NF007087
  - septin-ipr-IPR045324
  - septin-curation-policy
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0070939
  - GO:0071819
  - GO:1990065
  - GO:0032126
  - cellstructuremech:ejectisome
  - GO:0031391
  - GO:0033588
  - GO:0072546
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  - GO:1990207
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
  issue_key: dsl1-nzr-tip20-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Tip20 family mapping
  description: Tip20 remains REVIEWED_LABEL_ONLY under an open three-subunit mapping
    task, but native IPR007528 is a whole-protein RINT1/Tip20 family and P33891 independently
    has that cross-reference. The inspected Dsl1/Sec39 domain identifiers do not resolve
    their whole-protein classes.
  target_ids:
  - GO:0070939
  field_paths:
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR007528
  - micro-protein-P33891
  - micro-ipr-IPR021875
  - micro-ipr-IPR021876
  - micro-ipr-IPR013244-retry
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein class grounding
  native_severity: minor
  normalization_reason: Identity and supported composition remain intact; this is
    a bounded available class mapping that can resolve an existing task.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062447Z-dsl1-nzr-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2964
- finding_id: micro-F2
  issue_key: dsl1-nzr-dsl1-reconstitution-formation-dependency
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Record the demonstrated Dsl1 assembly dependency
  description: 'The current Dsl1 component evidence omits the direct purified-system
    bridging/association observation demonstrated in freshly inspected Tripathi Results
    S6 and Figure 4: Tip20 and Sec39 do not associate directly, whereas Dsl1 binds
    both and links the reconstituted ternary core. This is a bounded evidence/annotation
    gap, not a demand to replace global UNKNOWN essentiality with universal ESSENTIAL.
    Fresh Meiringer support is abstract tier only; its historical body reading is
    not newly certified.'
  target_ids:
  - GO:0070939
  field_paths:
  - components[0].essentiality
  - components[0].evidence
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-schema
  - micro-tripathi
  - micro-meta-10.1074_jbc.M110.215327
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  rule_id: Formation necessity must follow a directly tested assembly dependency
  native_severity: minor
  normalization_reason: Identity and composition are correct; the missing condition-scoped
    association evidence is a minor curation gap. Global formation UNKNOWN may remain
    because purified reconstitution does not establish universal in-vivo necessity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062447Z-dsl1-nzr-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2965
- finding_id: micro-F3
  issue_key: dubm-sgf11-sus1-sgf73-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve three DUB constituent family mappings
  description: The open mapping task leaves Sgf11, Sus1 and Sgf73 as REVIEWED_LABEL_ONLY
    despite exact full-protein families IPR013246, IPR018783 and IPR037804, independently
    present in their example cross-references. The broader UBP8 candidates checked
    here do not justify a fourth mapping.
  target_ids:
  - GO:0071819
  field_paths:
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-ipr-IPR013246
  - micro-ipr-IPR018783
  - micro-ipr-IPR037804
  - micro-protein-Q03067
  - micro-protein-Q6WNK7
  - micro-protein-P53165
  - micro-ipr-IPR028889
  - micro-ipr-IPR050185
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dubm_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein class grounding
  native_severity: minor
  normalization_reason: Identity and supported composition remain intact; this is
    a bounded available class mapping that can resolve an existing task.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062448Z-dubm-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2966
- finding_id: plaque-t6-F1
  issue_key: elongator-copy-number
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Separate six subunit identities from holoenzyme stoichiometry
  description: The active definition equates six distinct proteins with a heterohexamer
    of two heterotrimers. Current GO repeats this old wording, but later primary yeast
    structures resolve two Elp123 lobes and a majority one Elp456 heterohexamer. Setiaputra
    also measures alternate double-ring loading under specific preparations. Correct
    the active copy-number account without imposing invariant occupancy or rewriting
    dated discussion rationale; append a current evidence note.
  target_ids:
  - GO:0033588
  field_paths:
  - definition
  - components[*].role
  - causal_graphs#yeast_elongator_trna_wobble_modification.description
  - discussions#resolve_elongator_family_groundings.notes
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-curation
  - plaque-go
  - plaque-PMC99985-legacy
  - plaque-PMC5286391-legacy
  - plaque-PMC5286394-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: major
  normalization_reason: The defining molecular architecture assigns the wrong total
    copy number and subassembly stoichiometry. This changes the described physical
    assembly even though its ontology identifier remains correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062452Z-elongator-holoenzyme-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2961
- finding_id: plaque-t6-F2
  issue_key: elongator-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the six exact Elongator protein families
  description: All six rows remain label-only merely because exact full-class mappings
    were deferred. Current native family records and independent protein memberships
    resolve those mappings without using WD, GNAT, radical-SAM or RecA-like domains.
  target_ids:
  - GO:0033588
  field_paths:
  - components[*].grounding_status
  - discussions#resolve_elongator_family_groundings
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-curation
  - plaque-ipr-IPR006849
  - plaque-ipr-IPR037289
  - plaque-ipr-IPR034687
  - plaque-ipr-IPR008728
  - plaque-ipr-IPR019519
  - plaque-ipr-IPR018627
  - plaque-ipr-IPR039661
  - plaque-up-Q06706
  - plaque-up-P42935
  - plaque-up-Q02908
  - plaque-up-Q02884
  - plaque-up-P38874
  - plaque-up-Q04868
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correctly identified proteins remain
    intact; this is a bounded actionable grounding, inventory or condition-specific
    annotation correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062452Z-elongator-holoenzyme-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2962
- finding_id: plaque-t6-F3
  issue_key: elongator-elp1-formation
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record the measured Elp1 assembly requirement
  description: 'The Elp1 row lacks the directly measured condition-scoped association
    evidence: in the reported FLAG-Elp4 experiment, elp1 deletion eliminates Elp2/3
    recovery while the Elp456 assembly remains. Add this source-scoped formation/association
    result; a global UNKNOWN may remain where an enum cannot express the tested scope.
    Neither universal essentiality, viability nor a new experiment follows.'
  target_ids:
  - GO:0033588
  field_paths:
  - components#elp1_elongator_subunit.essentiality
  - components#elp1_elongator_subunit.evidence
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-curation
  - plaque-PMC5286391-legacy
  - plaque-structure-schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correctly identified proteins remain
    intact; this is a bounded actionable grounding, inventory or condition-specific
    annotation correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062452Z-elongator-holoenzyme-complex-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2963
- finding_id: septin-emc_complex-F1
  issue_key: emc-known-constituent-deferral
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the source-established yeast EMC constituents
  description: The record explicitly withholds all eight named yeast subunits pending
    exact-family/core-accessory curation, although its defining primary structure
    establishes their membership and the schema permits supported label-only constituents
    with unresolved essentiality. This is a specific avoidable inventory deferral,
    not a demand to fill every optional field. Current source review reconfirms the
    bounded correction. Preserve dated rationale/history; separately authorized curation
    may append a dated clarification or update current notes/status.
  target_ids:
  - GO:0072546
  field_paths:
  - components
  - discussions#emc_subunit_boundaries
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-peer-protein-P36039
  - septin-peer-protein-P40540
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emc_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correctly identified proteins remain
    intact; this is a bounded actionable grounding, inventory or condition-specific
    annotation correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062453Z-emc-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2956
- finding_id: septin-emc_complex-F2
  issue_key: emc3-emc5-alias-reversal
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the reversed EMC3 and EMC5 aliases
  description: The retained dated subunit-boundary rationale reverses EMC3/EMC5 aliases,
    risking propagation into the expressly deferred constituent curation. Current
    reviewed authority establishes EMC3/AIM27 and EMC5/KRE27. Preserve the original
    rationale and dated history; append correct current identity clarification and
    use it in future rows. OPEN status alone does not make the historical rationale
    editable. The original acceptance already preserved history; no separate historical-erasure
    bundle defect is asserted.
  target_ids:
  - GO:0072546
  field_paths:
  - discussions#emc_subunit_boundaries
  evidence_ids:
  - septin-record-emc_complex
  - septin-original-emc_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-bai2020-legacy
  - septin-guna2018-legacy
  - septin-chitwood2018-legacy
  - septin-odonnell2020-legacy
  - septin-peer-protein-P36039
  - septin-peer-protein-P40540
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emc_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: minor
  normalization_reason: The wrong aliases are localized to the current curation rationale;
    no component accession or overall complex identity is replaced. Correcting this
    mapping prevents future inventory rows from inheriting swapped identities.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062453Z-emc-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2957
- finding_id: septin-emrab_tolc_multidrug_efflux_transport_complex-F1
  issue_key: emrab-exact-component-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use exact EmrA and EmrB family identities
  description: EmrA remains label-only although NF011715 names the exact adaptor family;
    EmrB is grounded to broader DHA2/EmrB-like IPR004638 while NF000391 resolves exact
    EmrB. Separate UniProt xrefs corroborate each protein-family join. Current source
    review reconfirms the bounded correction. Preserve dated rationale/history; separately
    authorized curation may append a dated clarification or update current notes/status.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  field_paths:
  - components#emra_membrane_fusion_protein.grounding_status
  - components#emrb_inner_membrane_transporter.grounding
  - causal_graphs#emrab_tolc_xenobiotic_efflux.nodes#emrb.grounding
  - discussions#emrab_tolc_component_family_grounding
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-original-emrab_tolc_multidrug_efflux_transport_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-complex-CPX-4268
  - septin-zhong2026-legacy
  - septin-pmid-12482849
  - septin-pmid-33065135
  - septin-pdb-8ZAL-entry
  - septin-pdb-8ZAL-assembly
  - septin-pdb-8ZAL-entity1
  - septin-pdb-8ZAL-entity2
  - septin-pdb-8ZAL-entity3
  - septin-ncbifam-NF011715
  - septin-ncbifam-NF000391
  - septin-ipr-IPR004638
  - septin-ipr-IPR058622
  - septin-protein-P27303
  - septin-protein-P0AEJ0
  - septin-protein-P02930
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correctly identified proteins remain
    intact; this is a bounded actionable grounding, inventory or condition-specific
    annotation correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2958
- finding_id: septin-emrab_tolc_multidrug_efflux_transport_complex-new-cpx-attribution
  issue_key: emrab-cpx-essential-subunit-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish CPX stoichiometric membership from an essentiality annotation
  description: Three newly added protein-to-complex contribution edges say CPX4268
    curates EmrA,EmrB and TolC as essential stoichiometric subunits. The complete
    current authority object identifies participants and6:1:3 stoichiometries with
    unspecified biological roles and ECO0005547 curator inference; it does not classify
    their assembly essentiality. Zhong2026 separately establishes engineered assembly
    and functional assays, including assembled but inactive pump-EA. Preserve the
    supported contributions and counts, but narrow these CPX notes to membership/stoichiometry
    or cite and qualify any necessity claim using its actual experimental evidence.
    This finding does not automatically overturn preexisting ESSENTIAL component values
    or deny defining membership.
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  field_paths:
  - causal_graphs#emrab_tolc_xenobiotic_efflux.edges[subject=emrb,predicate=contributes
    to].evidence[reference=ComplexPortal:CPX-4268].notes
  - causal_graphs#emrab_tolc_xenobiotic_efflux.edges[subject=emra,predicate=contributes
    to].evidence[reference=ComplexPortal:CPX-4268].notes
  - causal_graphs#emrab_tolc_xenobiotic_efflux.edges[subject=tolc,predicate=contributes
    to].evidence[reference=ComplexPortal:CPX-4268].notes
  evidence_ids:
  - septin-record-emrab_tolc_multidrug_efflux_transport_complex
  - septin-emrab-stale-diff
  - septin-complex-CPX-4268
  - septin-eco0005547
  - septin-zhong2026-legacy
  - septin-graph-policy
  - septin-schema-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Accurate attribution and experimental scope
  native_severity: minor
  normalization_reason: Localized overstatement of one authority annotation repeated
    in three new edge notes; supported complex identity,counts and physical contributions
    remain intact.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2959
- finding_id: septin-emre_multidrug_transporter_complex-F1
  issue_key: emre-exact-protein-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the EmrE constituent to its exact family
  description: The EmrE row remains REVIEWED_LABEL_ONLY because the SMR class is broad,
    but NF042984 specifically identifies the full EmrE protein family and independent
    P23895 metadata verifies membership. Current source review reconfirms the bounded
    correction. Preserve dated rationale/history; separately authorized curation may
    append a dated clarification or update current notes/status.
  target_ids:
  - GO:1990207
  field_paths:
  - components#emre_multidrug_transporter.grounding_status
  - discussions
  evidence_ids:
  - septin-record-emre_multidrug_transporter_complex
  - septin-original-emre_multidrug_transporter_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-chen2007-legacy
  - septin-pmid-18024586
  - septin-pdb-3B5D-entry
  - septin-pdb-3B5D-assembly
  - septin-pdb-3B5D-entity1
  - septin-ncbifam-NF042984
  - septin-ncbifam-NF007087
  - septin-ipr-IPR045324
  - septin-protein-P23895
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emre_multidrug_transporter_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific biological scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correctly identified proteins remain
    intact; this is a bounded actionable grounding, inventory or condition-specific
    annotation correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T062455Z-emre-multidrug-transporter-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2960
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0070939
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground Tip20 with IPR007528
    and narrow the open mapping task to genuinely unresolved whole-protein classes.
    Preserve source-scoped homologous-family identity and yeast examples.
  acceptance_checks:
  - Verify family type and exact example membership.
  - Do not substitute Dsl1 or Sec39 domain accessions for whole proteins.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; narrow
    current prompt/notes only as supported.
  - No record edits occur in this review PR.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0070939
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add the directly tested purified
    Dsl1 bridging/association evidence with its recombinant-protein and pairwise/ternary
    reconstitution context. Keep global UNKNOWN if broader formation necessity remains
    unresolved. Preserve distinctions between the ternary core, pairwise subcomplexes,
    function, domain-mutant growth and organism viability.
  acceptance_checks:
  - Cite the actually inspected Tripathi Results S6 and Figure 4 with bounded purified-system
    context; obtain and independently read Meiringer body if making any new body-specific
    claim from it.
  - Do not infer identical Tip20/Sec39 requirements, universal in-vivo absence or
    globally depleted partners; do not require a new experiment.
  - A global UNKNOWN classification may coexist with the added condition-scoped evidence.
  - Run applicable native record/schema/identifier/graph gates after separately authorized
    curation.
  - Preserve dated discussions.rationale, posed_date and curation history; narrow
    current prompt/notes only as supported.
  - No record edits occur in this review PR.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0071819
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dubm_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground the three verified
    constituent classes and narrow the remaining task to unresolved Ubp8 identity.
    Retain four-component module boundaries and taxon-paired examples.
  acceptance_checks:
  - Verify class names/types and each separate accession cross-reference.
  - Do not substitute a generic USP domain or hydrolase family for Ubp8.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; narrow
    current prompt/notes only as supported.
  - No record edits occur in this review PR.
- action_id: plaque-t6-A1
  finding_ids:
  - plaque-t6-F1
  target_ids:
  - GO:0033588
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
  description: Retain GO0033588 and six protein identities; correct active definition/roles/graph
    copy-number wording using the measured two-Elp123 plus Elp456-ring assemblies,
    explicitly allowing condition-dependent ring occupancy. Append current discussion
    notes, preserving the dated rationale.
  acceptance_checks:
  - Do not rewrite historical titles or make a universal occupancy claim beyond the
    characterized yeast assembly.
  - Keep the valid tRNA function and reference protein identities.
  - Preserve correct identities and supported biology; pass applicable native validation.
  - Preserve dated rationale and curation history verbatim; append current evidence
    notes or qualify the active decision without rewriting historical provenance.
  - Acknowledge the majority single-ring assembly and the documented alternate double-Elp456
    loading; do not replace the old universal count with another universal count.
- action_id: plaque-t6-A2
  finding_ids:
  - plaque-t6-F2
  target_ids:
  - GO:0033588
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
  description: Use the six verified full-protein families and align current grounding
    notes/TODO.
  acceptance_checks:
  - Treat IPR034687 as Elp3 protein identity, not evidence that every microbial homolog
    joins a yeast-type complex.
  - Preserve correct identities and supported biology; pass applicable native validation.
  - Preserve dated rationale and curation history verbatim; append current evidence
    notes or qualify the active decision without rewriting historical provenance.
- action_id: plaque-t6-A3
  finding_ids:
  - plaque-t6-F3
  target_ids:
  - GO:0033588
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/elongator_holoenzyme_complex.yaml
    role: maintained scientific record
  description: Attach the primary condition-scoped Elp1-deletion/FLAG-Elp4 association
    evidence to the Elp1 component; distinguish lost Elp2/3 association from surviving
    Elp456. Qualify the formation annotation only to the supported scope; a global
    UNKNOWN may remain where needed.
  acceptance_checks:
  - Do not equate formation with growth or tRNA catalytic output.
  - Preserve independent Elp456 assembly and do not promote all six component enums.
  - Preserve correct identities and supported biology; pass applicable native validation.
  - Preserve dated rationale and curation history verbatim; append current evidence
    notes or qualify the active decision without rewriting historical provenance.
  - Do not require a universal ESSENTIAL enum or new experiments; capturing the observed
    bounded assembly association is sufficient.
- action_id: septin-emc_complex-A1
  finding_ids:
  - septin-emc_complex-F1
  target_ids:
  - GO:0072546
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emc_complex.yaml
    role: maintained scientific record
  description: Add source-scoped constituent rows for the verified yeast Emc1–6,Emc7,Emc10
    inventory, using exact families only where independently verified and otherwise
    honest label-only notes. Preserve unresolved cross-species core/accessory and
    formation questions. Preserve dated rationale/history; append clarification or
    update current notes/status, without rewriting old rationale. This PR changes
    no record.
  acceptance_checks:
  - Use the verified aliases EMC3/AIM27 and EMC5/KRE27.
  - Do not copy the old GO six-member list or treat all mammalian members as yeast
    constituents.
  - Do not infer individual assembly necessity from growth or insertase phenotypes.
  - Preserve correct identities and supported biology; pass applicable native validation.
  - Preserve exact inherited finding lineage and dated rationale/history; no automatic
    review-status promotion.
- action_id: septin-emc_complex-A2
  finding_ids:
  - septin-emc_complex-F2
  target_ids:
  - GO:0072546
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emc_complex.yaml
    role: maintained scientific record
  description: Append a dated clarification with verified EMC3/AIM27/P36039/YKL207W
    and EMC5/KRE27/P40540/YIL027C, and use these mappings in current/future constituent
    notes; preserve the original rationale and all dated history byte-for-byte.
  acceptance_checks:
  - Confirm P36039/EMC3/AIM27/YKL207W and P40540/EMC5/KRE27/YIL027C against native
    identity sources.
  - Use the corrected aliases in any separately authorized constituent curation.
  - Preserve correct EMC identity and primary membership evidence.
  - Preserve exact inherited finding lineage and dated rationale/history; no automatic
    review-status promotion.
- action_id: septin-emrab_tolc_multidrug_efflux_transport_complex-A1
  finding_ids:
  - septin-emrab_tolc_multidrug_efflux_transport_complex-F1
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  description: Ground EmrA to verified NF011715 and use exact EmrB NF000391 consistently
    in component and graph; align current TODO/notes and retain exact TolC, protein
    examples and source composition. Preserve dated rationale/history; append clarification
    or update current notes/status, without rewriting old rationale. This PR changes
    no record.
  acceptance_checks:
  - Do not treat a shared hairpin/beta-barrel domain as EmrA identity.
  - Keep broader DHA2 membership only as contextual classification.
  - Preserve correct identities and supported biology; pass applicable native validation.
  - Preserve exact inherited finding lineage and dated rationale/history; no automatic
    review-status promotion.
- action_id: septin-emrab_tolc_multidrug_efflux_transport_complex-new-cpx-attribution-action
  finding_ids:
  - septin-emrab_tolc_multidrug_efflux_transport_complex-new-cpx-attribution
  target_ids:
  - cellstructuremech:emrab_tolc_multidrug_efflux_transport_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  description: Narrow the three CPX evidence notes to curated participant membership
    and stoichiometry; if necessity is retained, distinguish structural definition
    from tested functional/assembly claims and cite the exact supporting experiment.
    Preserve correct contributions and6:1:3 counts.
  acceptance_checks:
  - Do not state CPX4268 supplies an essentiality classification absent from the current
    source.
  - Keep CPX curator inference,engineered8ZAL pump-EA and separate active FA/functional
    assays distinct.
  - Do not infer universal formation necessity from resistance,antiport or membership
    alone; do not automatically retype older component flags.
  - Preserve dated history and pass applicable native gates in separately authorized
    record curation.
- action_id: septin-emre_multidrug_transporter_complex-A1
  finding_ids:
  - septin-emre_multidrug_transporter_complex-F1
  target_ids:
  - GO:1990207
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emre_multidrug_transporter_complex.yaml
    role: maintained scientific record
  description: Use verified NF042984 for the named EmrE constituent and align current
    grounding rationale/TODO, while preserving GO1990207 for the assembled complex.
    Preserve dated rationale/history; append clarification or update current notes/status,
    without rewriting old rationale. This PR changes no record.
  acceptance_checks:
  - Do not substitute the broad SMR family or infer every SMR protein is an EmrE homodimer.
  - Preserve correct identities and supported biology; pass applicable native validation.
  - Preserve exact inherited finding lineage and dated rationale/history; no automatic
    review-status promotion.
limitations:
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Own scientific scope is the
  four complete Dsl1/NZR, DUBm, Dxr and eisosome records only. Eisosome is the sole
  stale own target; the other three current hashes are unchanged. Two additional frozen
  eisosome neighbors establish boundaries; frozen Elongator and EmrAB records are
  used only for separate auxiliary challenges, not own-slice dispositions.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Dsl1: fresh Tripathi genuine
  primary JATS read at declared Introduction/Results/Methods and Figure4-caption scopes,
  without images/supplements. Meiringer and Kraynack fresh complete abstracts only;
  current body routes failed/challenged and no new body-specific certification is
  made. Bounded purified bridge evidence does not force global ESSENTIAL.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: DUBm: fresh Wang and Adamus
  genuine primary bodies read at declared main-text/method/caption extents. Different
  purification strains, apo/nucleosome-bound maps, minimal Ub-AMC substrate and low-resolution
  SLIK/SAGA architecture remain distinct. Henry and localization/association studies
  are complete indexed abstracts/native annotations only; individual supplement data
  and every localization experiment were not reanalyzed.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Dxr: primary article remains
  complete indexed abstract plus genuine RCSB entry/polymer/assembly/ligand metadata.
  Coordinates/full article were not inspected. Source species, recombinant BL21(DE3)
  expression and K12 reference annotation differ. Substrate stereoisomer caveat and
  two protein copies remain bounded to the deposition.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Eisosome: fresh Walther main
  paragraphs0–17 and text captions, Karotki/Olivera declared primary body sections
  and methods were read. No pixels, movies, supplements or exhaustive fungal survey.
  Native Pil1/Lsp1 heterodimer versus mixed-homodimer organization remains unresolved;
  no universal endocytosis or complete assembly pathway is claimed. Moreira and Douglas
  remain indexed abstracts, Douglas explicitly secondary.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Protein authority annotations
  and current reviewed exact-gene queries do not certify every linked primary experiment
  or reconstruct historical query results. Broad family/domain candidates are not
  exact whole-protein mappings. InterPro IPR050185 LLM-flagged description is excluded
  as biological support; only its native broad identity/type informs the bounded non-mapping.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Fresh official catalogue includes
  no matched yeast dataset. E.coli precise1k has five stated strains; exact b0173
  is joined to P45568 and checked across201 modules, with one UC-2/167 hit corroborated
  by96-member metadata/identity rows. Unknown module function, nonhits and expression
  membership are not assembly, direct regulation, essentiality or biological absence.
  Activity vectors and AI summaries are unused.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Historical adapter unavailability
  is the actual Nov3 00:49Z receipt, not a fresh execution. The retained Douglas403
  observation preserves its original Oct21 time/hash and corrects only its kind. Present
  failed routes and successful indexed/body sources are separated. A default50-row
  gene page and misrouted app HTML were not treated as complete dataset evidence.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: Eight current native protein
  commands actually pass for11 reviewed examples and10 COVERED typed protein nodes.
  Eight original native validate/render commands and56 historical input occurrences
  also pass. Root owns global QC, successor save, post-save checks, final CI and merge
  queue; none of those future gates is precertified here.'
- 'Dsl1/NZR, DUBm, Dxr and eisosome independent review: All three inherited findings
  remain minor/open with exact repository/review/finding lineage. No new own scientific
  finding, invented predecessor, forced optional example, record mutation, history
  rewrite, neighbor/group closure or status promotion is introduced.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Rhiel2012 and Kubota2013
  are assessed at native complete abstract/metadata tier; current Springer landings
  are abstract/paywall pages and Kubota body retrieval is blocked. Kim/MacNeill2003
  and Kupiec2016 are secondary abstract context only.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Ammermann author text
  was read through saved web-reader extractions with actual observation times and
  provider crawl metadata; no native HTTP200 body success is invented. Bounded Methods/Results
  concern discharged fragments and reconstituted filaments. Introduction citations
  for intact resting organelles are secondary context. No image pixels or complete
  later sequence alignment were inspected.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Setiaputra and Dauden
  selected genuine main-body Results/Methods and text captions were read. No figure
  pixels, raw EM/MS reanalysis or Setiaputra supplementary strain TableEV4 was inspected.
  Dauden and Krogan experimental strain identities are separate from S288C reference
  examples.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Huang tRNA-modification
  loss is a functional phenotype, not direct full-complex formation evidence. The
  Elp1 association finding is restricted to the observed deletion/pull-down condition;
  it does not mandate a universal essentiality enum or all-six-subunit necessity.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Exact ejectisin family
  remains unresolved after one bounded empty native query; Elg1 keyword query was
  HTTP429-limited, and separately verified domains are not full-class groundings.
  Generated unchecked InterPro IPR050238 prose was excluded. These limits are not
  global negative biology or mandatory optional protein-example findings.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Current official catalogue
  fallback is independent of the historical structured-runner failure at2026-11-03
  00:49Z. No fresh runner success/failure is claimed. No matching natural host was
  found in the complete catalogue and no foreign-host module proxy was used; this
  does not establish biological absence.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: Five corrected historical
  transport rows retain old timestamps/hashes and honest context_only scope. Their
  original raw transport bytes were not reconstructed; this report binds the immutable
  original YAML carrying those observations and distinguishes current retrievable
  sources.'
- 'Ejectisome, Elg1 RFC-like and Elongator independent review: No maintained local
  image was present for the three targets. Source captions/abstracts do not certify
  image pixels. This slice does not certify parent-owned corpus checks, final CI,
  queue admission, merge or cleanup.'
- 'EMC, EmrAB-TolC and EmrE independent review: Three records: EMC/EmrE unchanged,EmrAB
  stale four-edge/history addition substantively refreshed. Four inherited minor findings
  and one new localized minor CPX-attribution finding remain open; all three need
  curation. Three original formal applicability exclusions require successor correction.
  No own access-kind misclassification established after inspecting all original evidence
  rows.'
- 'EMC, EmrAB-TolC and EmrE independent review: Genuine Bai,Guna,Chitwood,O''Donnell,Zhong
  and Chen bodies were freshly retrieved and read only at exact stated sections/captions.
  No figure pixels,raw structural data or unread supplementary experiments certified.
  Borges-Walmsley2003 and Yousefian2021 limited to complete primary abstracts and
  exact metadata; unavailable full-body scope is not a refutation.'
- 'EMC, EmrAB-TolC and EmrE independent review: Yeast Bai preparation is W303-1a;
  native EMC alias reference is S288c; human HEK/U2OS insertion evidence remains comparative.
  Preserve older rationale,append current alias clarification,do not substitute mammalian
  constituents or infer assembly necessity from growth/function. Native old GO six-member
  text is not used to override eight experimentally isolated yeast subunits.'
- 'EMC, EmrAB-TolC and EmrE independent review: Zhong2026 gene sourceMG1655 differs
  from engineered C43(DE3)delta-acrAB expression/assays;8ZAL is pump-EA,assembled
  but inactive in resistance tests,while FA provides separate activity context. CPX
  participant roles are unspecified and its evidence is curator inference. New attribution
  correction does not deny defining membership or impose blanket changes to older
  ESSENTIAL flags.'
- 'EMC, EmrAB-TolC and EmrE independent review: Chen2007 correctedTPP-bound structure
  is distinct from distorted acidic apo/defunct prior structures. BiologicalK12 differs
  fromBL21(DE3)/cell-free expression;2:1 protein:drug binding differs from two-subunit
  assembly. No all-SMR or fully resolved transport-cycle claim.'
- 'EMC, EmrAB-TolC and EmrE independent review: Fresh complete official catalogue
  has no yeast/human host. Matched E.coli precise1k advertises five strains,not all
  experimental hosts. Four exact loci independently checked across201 modules; tolC
  inSoxS22 andemrE inROS TALE Amp9 confirmed by member endpoints. emrA/emrB false
  flags are not biological absence. AI module summaries,activity traces and imported
  functional prose are not primary evidence.'
- 'EMC, EmrAB-TolC and EmrE independent review: Historical runner unavailable receipt
  is actualNov3 00:49Z; no fresh invocation claimed. Shared current catalogue/meta/module
  packet keeps actualNov4 access times and independent read scope. Own fresh retrievals
  are distinct from original immutable review provenance.'
- 'EMC, EmrAB-TolC and EmrE independent review: Actual six native protein commands
  exit0: EMC0examples/0typed nodes (empty coverage),EmrAB3reviewed examples/3COVERED
  nodes,EmrE1reviewed/1COVERED. Native identity/coverage is not independent experimental
  membership/necessity proof. Three originals validate/render exactly and39 historical
  input occurrences match. Root corpus gates,successor/finalheadCI and merge attestations
  are separate.'
- 'EMC, EmrAB-TolC and EmrE independent review: Only26 listed frozen maintained inputs
  used; two other reviewer neighbors in final49-input manifest were not used here.
  No record,original bundle,Git or GitHub mutation. Source-locality notes do not claim
  exhaustive absence across the literature.'
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
- All 49 maintained inputs were frozen before substantive use, including two neighboring
  eisosome records consulted only to assess boundaries. The original twenty artifacts
  remain immutable and traceable; the ten current record hashes are frozen separately
  from their historical review inputs.
- 'Two stale targets are refreshed: eisosome gained a Pil1/Lsp1 family grounding and
  PROTEIN_COMPLEX classification; EmrAB-TolC gained four causal edges and history.
  Current source and neighboring-boundary assessment supports the eisosome refresh
  without an enum-only defect. The EmrAB contribution edges remain supported while
  three new CPX evidence notes overstate the authority''s essentiality annotation.'
- 'Ten inherited scientific findings remain open: Dsl1/NZR two minor, DUBm one minor,
  Elongator one major and two minor, EMC two minor, EmrAB-TolC one minor and EmrE
  one minor. The new CPX attribution finding is minor. Dxr, eisosome, ejectisome and
  Elg1 RFC-like retain qualified passes. All scientific curation stays in separate
  issues.'
- 'Formation findings preserve experimental scope: purified Dsl1 bridging and Elp1-dependent
  co-purification are not universal organismal essentiality claims; a global UNKNOWN
  may remain with explicit tested association evidence. Elongator subunit identities
  and state-dependent copy numbers are distinguished. Dated rationale and history
  are preserved rather than overwritten.'
- 'Actual native protein checks cover 26 represented examples and 26 typed nodes:
  25 COVERED and one ejectisin NO_GENE_SYMBOLS diagnostic. These command outcomes
  do not themselves establish scientific membership, exact family scope or formation
  necessity.'
- 'Deduplication inspected all 377 open issue titles and full bodies and 103 bounded
  open title/body/comment searches for the ten current record labels, IDs, paths,
  stems, inherited keys, genes, families and review-evidence identities. The 19 related
  open issue bodies match already inspected accepted payloads; complete comment collections
  are empty. Issues #2626 and #2627 concern MCC and plasma membrane records; #2838–#2839
  and #2850–#2854 concern AcrAB/AcrAD/AcrEF-TolC records; #2842–#2849 match shared
  footer terms for unrelated records; #2897 and #2927 concern Ctf18-RFC and canonical
  RFC. Those distinct maintained owners are not duplicates of this cohort. Closed
  historical eisosome issues #2432 and #2462 and their complete comments were inspected
  as provenance, without reopening them. Existing resolver issue #2514 and all 27
  comments were inspected or verified byte-identical to prior read text and are reused.
  No matching open same-record/finding issue was found within this scope.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062447Z-dsl1-nzr-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062448Z-dubm-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062449Z-dxr-protein-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062450Z-eisosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062451Z-ejectisome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062451Z-elg1-rfc-like-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062452Z-elongator-holoenzyme-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062453Z-emc-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062454Z-emrab-tolc-multidrug-efflux-transport-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T062455Z-emre-multidrug-transporter-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2390
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2954
- https://github.com/CultureBotAI/CellStructureMech/issues/2955
- https://github.com/CultureBotAI/CellStructureMech/issues/2956
- https://github.com/CultureBotAI/CellStructureMech/issues/2957
- https://github.com/CultureBotAI/CellStructureMech/issues/2958
- https://github.com/CultureBotAI/CellStructureMech/issues/2959
- https://github.com/CultureBotAI/CellStructureMech/issues/2960
- https://github.com/CultureBotAI/CellStructureMech/issues/2961
- https://github.com/CultureBotAI/CellStructureMech/issues/2962
- https://github.com/CultureBotAI/CellStructureMech/issues/2963
- https://github.com/CultureBotAI/CellStructureMech/issues/2964
- https://github.com/CultureBotAI/CellStructureMech/issues/2965
- https://github.com/CultureBotAI/CellStructureMech/issues/2966
- https://github.com/CultureBotAI/CellStructureMech/issues/2967
```
