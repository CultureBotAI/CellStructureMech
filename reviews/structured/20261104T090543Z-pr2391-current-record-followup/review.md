# PR 2391: current-input review of ten records and adversarial follow-up

- Review: 20261104T090543Z-pr2391-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T08:44:33.752584Z
- Finished UTC: 2026-11-04T09:05:43Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input successor for all ten PR2391 records. EmrKY-TolC is the sole stale target and its four new graph edges are substantively reassessed. Eight inherited minor findings remain open and one new minor CPX-attribution finding is added. The original EmrKY major is rejected as formulated after independent source review and a second challenge; this does not certify experimentally demonstrated necessity. ER Sec, the ESCRT umbrella and ESCRT-III retain qualified passes. Ten applicability exclusions and four historical access-kind occurrences are corrected without changing the twenty original artifacts or any scientific record.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 0d46f4dcafa33fe2e307874818552e76933abb7a.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base a38c89d6665997cbf5972462345df67f09b41009.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml | maintained | EmrKY-TolC multidrug efflux transport complex |
| GO:0031205 | data/structures/other/endoplasmic_reticulum_sec_complex.yaml | maintained | endoplasmic reticulum Sec complex |
| GO:0008622 | data/structures/other/epsilon_dna_polymerase_complex.yaml | maintained | epsilon DNA polymerase complex |
| GO:0032865 | data/structures/other/ermes_complex.yaml | maintained | ERMES complex |
| GO:0033565 | data/structures/other/escrt_0_complex.yaml | maintained | ESCRT-0 complex |
| GO:0036452 | data/structures/other/escrt_complex.yaml | maintained | ESCRT complex |
| GO:0000813 | data/structures/other/escrt_i_complex.yaml | maintained | ESCRT I complex |
| GO:0000814 | data/structures/other/escrt_ii_complex.yaml | maintained | ESCRT II complex |
| GO:0000815 | data/structures/other/escrt_iii_complex.yaml | maintained | ESCRT III complex |
| GO:1990621 | data/structures/other/escrt_iv_complex.yaml | maintained | ESCRT IV complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | Documented focused command passed. |
| validate-strict cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | Documented focused command passed. |
| validate GO:0031205 | passed | True | GO:0031205 | Documented focused command passed. |
| validate-strict GO:0031205 | passed | True | GO:0031205 | Documented focused command passed. |
| validate GO:0008622 | passed | True | GO:0008622 | Documented focused command passed. |
| validate-strict GO:0008622 | passed | True | GO:0008622 | Documented focused command passed. |
| validate GO:0032865 | passed | True | GO:0032865 | Documented focused command passed. |
| validate-strict GO:0032865 | passed | True | GO:0032865 | Documented focused command passed. |
| validate GO:0033565 | passed | True | GO:0033565 | Documented focused command passed. |
| validate-strict GO:0033565 | passed | True | GO:0033565 | Documented focused command passed. |
| validate GO:0036452 | passed | True | GO:0036452 | Documented focused command passed. |
| validate-strict GO:0036452 | passed | True | GO:0036452 | Documented focused command passed. |
| validate GO:0000813 | passed | True | GO:0000813 | Documented focused command passed. |
| validate-strict GO:0000813 | passed | True | GO:0000813 | Documented focused command passed. |
| validate GO:0000814 | passed | True | GO:0000814 | Documented focused command passed. |
| validate-strict GO:0000814 | passed | True | GO:0000814 | Documented focused command passed. |
| validate GO:0000815 | passed | True | GO:0000815 | Documented focused command passed. |
| validate-strict GO:0000815 | passed | True | GO:0000815 | Documented focused command passed. |
| validate GO:1990621 | passed | True | GO:1990621 | Documented focused command passed. |
| validate-strict GO:1990621 | passed | True | GO:1990621 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | All ten records contain positive molecular/pathway assertions and require the native applicability assessment. The complete current official catalogue supplies no matching yeast/human natural-host dataset. EmrKY E. coli K-12 is checked against precise1k:4257 genes,201 modules and BW25113/DGF-298/GMOS/MG1655/W3110 strains. Current bounded joins associate EmrK/b2368 and EmrY/b2367 with EvgA k38 (15 members), and TolC/b3035 with SoxS k22 (117 members). Dataset-strain context differs from May2009 modified OCL62. Module membership is expression context, not direct regulation or assembly evidence. Historical unavailable runner is retained separately; no fresh runner execution or proxy expression-host query is claimed. |
| Independent claim-level source review | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native EmrKY-TolC multidrug efflux transport complex UniProt verify check | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native EmrKY-TolC multidrug efflux transport complex UniProt causal check | passed | True | cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native endoplasmic reticulum Sec complex UniProt verify check | passed | True | GO:0031205 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native endoplasmic reticulum Sec complex UniProt causal check | passed | True | GO:0031205 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native epsilon DNA polymerase complex UniProt verify check | passed | True | GO:0008622 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native epsilon DNA polymerase complex UniProt causal check | passed | True | GO:0008622 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ERMES complex UniProt verify check | passed | True | GO:0032865 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ERMES complex UniProt causal check | passed | True | GO:0032865 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT-0 complex UniProt verify check | passed | True | GO:0033565 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT-0 complex UniProt causal check | passed | True | GO:0033565 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT complex UniProt verify check | passed | True | GO:0036452 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT complex UniProt causal check | passed | True | GO:0036452 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT I complex UniProt verify check | passed | True | GO:0000813 | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT I complex UniProt causal check | passed | True | GO:0000813 | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT II complex UniProt verify check | passed | True | GO:0000814 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT II complex UniProt causal check | passed | True | GO:0000814 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT III complex UniProt verify check | passed | True | GO:0000815 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT III complex UniProt causal check | passed | True | GO:0000815 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT IV complex UniProt verify check | passed | True | GO:1990621 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ESCRT IV complex UniProt causal check | passed | True | GO:1990621 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact pump boundary and reference strain

identity: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

Minted identity denotes the specific EmrK/EmrY/TolC assembly, whereas GO1990281 is broader. CPX4273 is exact organism-specific composition, not a source-neutral protein family. K12 reference annotation is distinct from each May experimental construct.

### Curator inference and by-similarity participant annotations

evidence: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

CPX ECO0005547 and native EmrK/EmrY ECO0000250 are explicitly inferential. Null EmrK/Y counts and TolC3 are retained. Neither current source asserts a constituent-specific deletion/assembly experiment; other TolC pumps are not substituted.

### Substantive stale-edge reassessment

graph: concern. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

The three new contributes-to edges preserve supported inferred participant membership, and the new transport-to-export edge is a coarse function relation at declared NONMECHANISTIC scope. Their CPX evidence notes independently overstate source-annotated essentiality; this narrow new attribution defect does not invalidate the membership edges or require automatic changes to older component values.

### Independent disposition of inherited formation finding

evidence: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

Reject the inherited major as formulated: absence of an isolated formation assay does not establish that defining members of this explicitly inferred tripartite complex must be UNKNOWN. The original allowed added evidence, but its mandatory correction treats the lack of measured component-specific necessity as a demonstrated major defect. Rejection does not certify experimental necessity, infer dispensability, rewrite history or resolve the separate new source-attribution problem.

### Exact TolC family and broader adaptor/transporter families

grounding: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

IPR058622 exactly grounds TolC. IPR005694/TIGR00998 include multiple membrane-fusion proteins; IPR004638/TIGR00711 include broader EmrB-like transporters. These inspected candidates do not force exact EmrK-only or EmrY-only mappings. The remaining source-neutral task stays open without a universal claim that no family could exist.

### May experimental readout and limitations

evidence: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

The actual Methods and Results distinguish MG1655/pBR322 from modified OCL62 and multiple changed loci/regulation. Expression, biofilm and drug response are not direct assembly readouts. Maintained source-tier qualifications are appropriate; the paper does not provide each subunit formation necessity or exact EmrK/Y counts.

### Whole-system export versus microscopic mechanism

graph: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

The original coupling, whole-pump transport and exterior-target edges plus new coarse export link are supported at the retained inferred/nonmechanistic boundary. No residue-level antiport states, gating cycle or experimentally resolved architecture is claimed. GO0140330 is process identity, not direct proof of every molecular step.

### Parent Sec complex and two subcomplexes

identity: supported. Targets: GO:0031205.

GO0031205 exactly denotes the parent ER Sec complex; GO0140534 is an is-a ancestor and GO0005789 the membrane location. Sec61 GO0005784 and Sec62/Sec63 GO0031207 are legitimate subcomplexes. Individual subunit duplication is not required at this parent level.

### Reconstitution and precursor interaction sources

evidence: supported. Targets: GO:0031205.

Panzner is presently complete indexed abstract only and supports the purified yeast Sec/Kar2 reconstitution summary at that tier. Genuine Plath Methods/Results independently show specific precursor-Sec61/Sec62 crosslinks and distinguish initial binding from later Kar2-dependent transport. No inaccessible Panzner body is certified.

### Structural extent and source strain

evidence: supported. Targets: GO:0031205.

Wu BY4741 purification and overall seven-component architecture support the subcomplex topology. Sec62 has limited density/model coverage; the current generic structurally-resolved wording is not treated as an assertion that all residues/subunits were atomically resolved. Reference yeast species is appropriately broader than the preparation.

### Coarse import and membrane placement

graph: supported. Targets: GO:0031205.

Four graph edges describe two subcomplex memberships, ER-membrane placement and support for posttranslational import. Kar2/BiP is a separate coupled factor, not automatically a constituent. No universal individual-subunit essentiality, missing optional examples or absent complete mechanism is manufactured as a finding.

### Resolved nonduplication discussion

scope: supported. Targets: GO:0031205.

The existing resolved discussion documents the chosen parent/subcomplex boundary. Current evidence supports that representation; it is not a new terminal disposition of unrelated lower-level records or historical issues.

### Heterotetrameric Pol-epsilon identity

identity: supported. Targets: GO:0008622.

GO0008622 is exact and GO0042575 a genuine broader class. The definition is faithfully GO-derived, including cautious historical leading-strand wording and PCNA stimulation. The current graph explicitly withholds detailed leading-strand assignment, replisome engagement and repair mechanisms.

### Four-subunit preparation and structural scope

evidence: supported. Targets: GO:0008622.

The complete Chilkova indexed abstract explicitly supports the purified yeast1:1:1:1 heterotetramer. Correct publisher PDF route is blocked and no body is newly certified. Asturias abstract/publisher metadata and Ganai inspected biochemical sections supply separate architecture/activity context without transferring assay conditions to all species.

### Available Pol2, Dpb2 and Dpb4 family mappings

grounding: concern. Targets: GO:0008622.

Native IPR029703 and IPR016266 match Pol2 and Dpb2; IPR051377 and its complete reviewed-member list match the homologous Dpb4/POLE3 class, corroborated by Q04603. These available mappings support narrowing the open task. LLM-flagged prose is not primary support; broad IPR050568/shared histone folds do not settle exact Dpb3.

### Condition-scoped Dpb4 physical stability

evidence: concern. Targets: GO:0008622.

Ohya sec15 directly shows easier Dpb2/Dpb3 dissociation from Pol2 after MonoQ purification of dpb4-deletion extracts, with active-fraction mixture and degradation limits. The current role/graph omits this bounded physical stability observation. Add it without forcing global ESSENTIAL, a new assay, or equating viability/activity with assembly.

### Example annotations and independent source tiers

evidence: supported. Targets: GO:0008622.

Reviewed S288C identities match the four maintained genes/loci. Dpb2 Cytoplasm/Nucleus native annotations and Huh abstract, plus Dpb3/4 Ohya-associated annotation context, are not blanket proof of the whole complex at every listed location. Individual localization supplement rows were not freshly inspected.

### Membership and DNA replication boundary

graph: supported. Targets: GO:0008622.

Four membership edges and whole-complex DNA replication support are valid at declared NONMECHANISTIC scope. Ganai whole-enzyme versus truncated Pol2 comparisons do not isolate necessity of each accessory protein. Current UNKNOWN values may remain alongside the bounded Dpb4 evidence.

### Exact ERMES identity and spanning contact topology

identity: supported. Targets: GO:0032865.

GO0032865 exact identity and its four synonyms are confirmed. Both ER and outer mitochondrial complex ancestry are native; tether topology spans the organelles and does not mean every constituent is exclusively mitochondrial. Mmm1 ER localization and Mdm10 shared SAM membership remain distinct.

### Known core versus exact-family prerequisite

completeness: concern. Targets: GO:0032865.

The current prompt expressly defers all Mmm1/Mdm10/Mdm12/Mdm34 rows until exact family groundings. Kornmann and Kawano directly identify this core; native reviewed-label-only representation permits honest known membership before every exact family is resolved. This is an explicit current prerequisite gap, not a generic demand to fill every optional inventory.

### Mmm1-Mdm12 module versus whole in-vivo ERMES

evidence: supported. Targets: GO:0032865.

The maintained graph already restricts direct lipid transfer to an in-vitro Mmm1-Mdm12 module. Kawano model-membrane, K.lactis recombinant and S.cerevisiae heavy-membrane-fraction experiments remain distinct; carrier/conduit interpretations and complete in-vivo exchange are not asserted as settled.

### Synthetic-tether and mutant preparation bounds

scope: supported. Targets: GO:0032865.

Kornmann synthetic-tether screen, localization/rescue and loss-of-puncta observations support the identified yeast core and tether role. These are not an exhaustive copy-number inventory or universal necessity classifications; peripheral Gem1/Tom7 and optional protein instances are not required by this finding.

### Structure-level tether and module relations

graph: supported. Targets: GO:0032865.

Three edges describe native outer-membrane classification, ER linking and an explicitly limited lipid-transfer module. Current coarse FUNCTION/NONMECHANISTIC graph is scientifically bounded. No automatic GENE_OR_PROTEIN conversion or added mechanistic chain is required.

### Current example inventory and identity scope

grounding: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

3 reviewed maintained examples match native genes/loci/taxa and current bounded queries. Current singleton results do not reconstruct historical selection queries. Family-level grounding and primary biological evidence remain separate.

### Whole-record structured-source applicability

scope: concern. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

Original formal exclusion incorrectly relies on absence of expression claims despite positive named protein/pathway assertions. Fresh E.coli precise1k five-strain metadata and exact three locus/native-accession joins were inspected across201 modules: EmrK/EmrY in15-member EvgA38 and TolC in117-member SoxS22. This is not the May construct or assembly evidence. Historical runner unavailability remains separately dated.

### Immutable historical provenance and current finding lineage

scope: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

One inherited major is rejected as formulated, with exact lineage and no curation action for it; a distinct new minor source-attribution finding has no invented predecessor. Preserve rationale, posed_date, dated curation events and all original artifacts; no records are edited here.

### Actual native checks and original artifacts

schema: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

3 reviewed examples and 3 COVERED typed nodes. Actual source-head verify/causal commands exit0; original native validate/render and recorded historical hashes pass. These checks do not certify source completeness or future successor/CI gates.

### Images, measurements and optional scope

scope: not_applicable. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex.

No maintained image or quantitative physical-property assertion requires pixel inspection. Paper text captions were read only at declared extents; no microscopy pixels, supplementary movies, coordinate analysis or optional imaging requirement is claimed.

### Current example inventory and identity scope

grounding: not_applicable. Targets: GO:0031205.

No maintained protein examples or typed protein nodes. Native success has empty coverage; no optional examples are required solely from that absence. Family-level grounding and primary biological evidence remain separate.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0031205.

Original formal exclusion incorrectly relies on absence of expression claims despite positive named protein/pathway assertions. Fresh complete catalogue has no matching Saccharomyces dataset; no unrelated bacterial proxy or invented downstream query is used. Historical runner unavailability remains separately dated.

### Immutable historical provenance and current finding lineage

scope: supported. Targets: GO:0031205.

Original qualified-pass result remains supported within stated source limits. Preserve rationale, posed_date, dated curation events and all original artifacts; no records are edited here.

### Actual native checks and original artifacts

schema: supported. Targets: GO:0031205.

0 reviewed examples and 0 COVERED typed nodes. Actual source-head verify/causal commands exit0; original native validate/render and recorded historical hashes pass. These checks do not certify source completeness or future successor/CI gates.

### Images, measurements and optional scope

scope: not_applicable. Targets: GO:0031205.

No maintained image or quantitative physical-property assertion requires pixel inspection. Paper text captions were read only at declared extents; no microscopy pixels, supplementary movies, coordinate analysis or optional imaging requirement is claimed.

### Current example inventory and identity scope

grounding: supported. Targets: GO:0008622.

4 reviewed maintained examples match native genes/loci/taxa and current bounded queries. Current singleton results do not reconstruct historical selection queries. Family-level grounding and primary biological evidence remain separate.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0008622.

Original formal exclusion incorrectly relies on absence of expression claims despite positive named protein/pathway assertions. Fresh complete catalogue has no matching Saccharomyces dataset; no unrelated bacterial proxy or invented downstream query is used. Historical runner unavailability remains separately dated.

### Immutable historical provenance and current finding lineage

scope: supported. Targets: GO:0008622.

Two inherited minors remain with exact lineage, available class mapping and bounded Dpb4 stability action. Preserve rationale, posed_date, dated curation events and all original artifacts; no records are edited here.

### Actual native checks and original artifacts

schema: supported. Targets: GO:0008622.

4 reviewed examples and 4 COVERED typed nodes. Actual source-head verify/causal commands exit0; original native validate/render and recorded historical hashes pass. These checks do not certify source completeness or future successor/CI gates.

### Images, measurements and optional scope

scope: not_applicable. Targets: GO:0008622.

No maintained image or quantitative physical-property assertion requires pixel inspection. Paper text captions were read only at declared extents; no microscopy pixels, supplementary movies, coordinate analysis or optional imaging requirement is claimed.

### Current example inventory and identity scope

grounding: not_applicable. Targets: GO:0032865.

No maintained protein examples or typed protein nodes. Native success has empty coverage; no optional examples are required solely from that absence. Family-level grounding and primary biological evidence remain separate.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0032865.

Original prose exclusion incorrectly relies on absence of expression claims despite positive named protein/pathway assertions. Fresh complete catalogue has no matching Saccharomyces dataset; no unrelated bacterial proxy or invented downstream query is used. Historical runner unavailability remains separately dated.

### Immutable historical provenance and current finding lineage

scope: supported. Targets: GO:0032865.

Inherited minor targets the explicit current prerequisite in the prompt, not the truth or wording of the dated rationale. Preserve rationale, posed_date, dated curation events and all original artifacts; no records are edited here.

### Actual native checks and original artifacts

schema: supported. Targets: GO:0032865.

0 reviewed examples and 0 COVERED typed nodes. Actual source-head verify/causal commands exit0; original native validate/render and recorded historical hashes pass. These checks do not certify source completeness or future successor/CI gates.

### Images, measurements and optional scope

scope: not_applicable. Targets: GO:0032865.

No maintained image or quantitative physical-property assertion requires pixel inspection. Paper text captions were read only at declared extents; no microscopy pixels, supplementary movies, coordinate analysis or optional imaging requirement is claimed.

### identity-and-definition

identity: concern. Targets: GO:0033565.

Correct ESCRT-0 identity is retained, but the active definition faithfully copies the current GO Vps1 error. Exact synonym, Bilodeau abstract, current Vps27/Hse1 identities and the record own resolved discussion contradict that localized name. Correct active wording/source transparency without rewriting dated rationale.

### hierarchy-and-topology

scope: supported. Targets: GO:0033565.

Native is_a-only ancestors and typed parent children support the maintained hierarchy. Direct endosome/endosome-membrane parthood is checked separately against typed relations; none is inferred from mere ancestry.

### components-and-family-grounding

grounding: concern. Targets: GO:0033565.

Vps27/Hse1 membership is supported. Exact IPR017073 resolves the already-open Vps27/Hrs mapping; mixed IPR050670/PTHR45929 is not forced onto Hse1. This is a bounded existing task, not an optional-inventory mandate.

### protein-identity-and-native-coverage

grounding: supported. Targets: GO:0033565.

Two reviewed protein_examples and two COVERED typed protein nodes. Native success is identifier/coverage evidence only; current protein names, aliases, loci, review status and taxa are independently checked. Reference S288C is not silently equated with experimental SEY6210.

### taxon-and-experimental-scope

scope: supported. Targets: GO:0033565.

S. cerevisiae species and S288C reference-strain identifiers are current. Katzmann/Chu/Curtiss selected Methods identify SEY6210 derivatives; E.coli expression is not the natural host. COMMON retains the native majority-occurrence meaning, but these studies supply qualitative support rather than a prevalence census. Mammalian synonyms do not export yeast perturbations universally.

### function-and-primary-support

evidence: supported. Targets: GO:0033565.

Bilodeau primary abstract supports Ub recognition and sorting; Katzmann directly supports the specifically represented Vps27 recruitment actor. UIM sorting defects are not conflated with loss of all lumenal membrane production.

### localisation-and-provenance

provenance: supported. Targets: GO:0033565.

Native endosome-membrane annotations retain the cited ECO/PMIDs. Stahelin supports isolated FYVE-domain binding; Huh abstract establishes survey provenance, not fresh viewing of individual microscopy.

### graph-and-formation-boundaries

graph: supported. Targets: GO:0033565.

NONMECHANISTIC graph correctly separates two memberships, Ub binding, Vps27-specific recruitment and MVB participation. Hse1 universal recruitment dependence is not asserted.

### necessity-and-inventory-limits

evidence: unknown. Targets: GO:0033565.

Sorting, localization, Ub binding, viability and subcomplex recovery do not establish a universal individual formation table. Both UNKNOWN rows remain legitimate.

### structured-source-applicability

evidence: supported. Targets: GO:0033565.

Positive protein constituent and Ub-sorting/recruitment assertions trigger the native broad structured-source policy. Complete fresh official catalogue has no matching natural-host dataset; no proxy downstream query is warranted. The old notes[1] expression-only exclusion is unsupported even though present bounded catalogue noncoverage is legitimate. Historical runner unavailability remains historical; no fresh runner invocation or negative biological conclusion is claimed.

### schema-history-and-verdict

schema: concern. Targets: GO:0033565.

All47 current frozen inputs and41 own historical input occurrences match;3 originals validate/render exactly and own targets are unchanged. Needs_curation retained for two reconfirmed inherited minor finding(s). Historical rationale and prior corrections remain intact; no terminal disposition of unrelated issues or future CI/queue/merge certification is made. Three historical access-kind occurrence(s) require successor classification correction; old context_only disclosures were honest.

### identity-and-definition

identity: supported. Targets: GO:0036452.

The generic ESCRT parent denotes a class of distinct complexes, not one combined fixed-stoichiometry supercomplex. Its broad membrane-fission definition and five child identities are consistent.

### hierarchy-and-topology

scope: supported. Targets: GO:0036452.

Native is_a-only ancestors and typed parent children support the maintained hierarchy. Direct endosome/endosome-membrane parthood is checked separately against typed relations; none is inferred from mere ancestry.

### components-and-family-grounding

grounding: supported. Targets: GO:0036452.

The deliberately empty parent component/example table preserves distinct child assemblies. Historical future-record wording is not treated as a present corpus-absence claim.

### protein-identity-and-native-coverage

grounding: supported. Targets: GO:0036452.

Zero protein_examples and zero typed protein nodes; positive pathway assertions remain subject to source review. Native success is identifier/coverage evidence only; current protein names, aliases, loci, review status and taxa are independently checked. Reference S288C is not silently equated with experimental SEY6210.

### taxon-and-experimental-scope

scope: supported. Targets: GO:0036452.

S. cerevisiae species and S288C reference-strain identifiers are current. Katzmann/Chu/Curtiss selected Methods identify SEY6210 derivatives; E.coli expression is not the natural host. COMMON retains the native majority-occurrence meaning, but these studies supply qualitative support rather than a prevalence census. Mammalian synonyms do not export yeast perturbations universally.

### function-and-primary-support

evidence: supported. Targets: GO:0036452.

GO and Henne complete secondary abstract support broad MVB sorting and membrane remodeling; Katzmann provides supplementary primary yeast context. Detailed Henne main-body mechanisms remain unread, and child-specific primary assays are not reassigned to the review.

### localisation-and-provenance

provenance: supported. Targets: GO:0036452.

Generic endosomal context is supported by typed GO and the scoped review abstract; no parent-wide fixed subunit or location mechanism is added.

### graph-and-formation-boundaries

graph: supported. Targets: GO:0036452.

NONMECHANISTIC graph contains five is_a child edges, typed endosome parthood and coarse MVB participation. It does not assert that all ESCRT subcomplexes always form one assembly or a universal handoff mechanism.

### necessity-and-inventory-limits

evidence: unknown. Targets: GO:0036452.

Sorting, localization, Ub binding, viability and subcomplex recovery do not establish a universal individual formation table. No generic constituent necessity or fixed stoichiometry is asserted.

### structured-source-applicability

evidence: supported. Targets: GO:0036452.

Positive MVB-sorting and named ESCRT pathway assertions trigger the native broad structured-source policy. Complete fresh official catalogue has no matching natural-host dataset; no proxy downstream query is warranted. The old notes[1] expression-only exclusion is unsupported even though present bounded catalogue noncoverage is legitimate. Historical runner unavailability remains historical; no fresh runner invocation or negative biological conclusion is claimed.

### schema-history-and-verdict

schema: supported. Targets: GO:0036452.

All47 current frozen inputs and41 own historical input occurrences match;3 originals validate/render exactly and own targets are unchanged. Qualified pass retained with explicit abstract/body and class-boundary limits. Historical rationale and prior corrections remain intact; no terminal disposition of unrelated issues or future CI/queue/merge certification is made. One historical access-kind occurrence(s) require successor classification correction; old context_only disclosures were honest.

### identity-and-definition

identity: supported. Targets: GO:0000813.

GO0000813 identifies ESCRT-I; three supported yeast core proteins are historically scoped and the current Mvb12 discussion expressly acknowledges later composition. No exhaustive three-protein assertion is inferred.

### hierarchy-and-topology

scope: supported. Targets: GO:0000813.

Native is_a-only ancestors and typed parent children support the maintained hierarchy. Direct endosome/endosome-membrane parthood is checked separately against typed relations; none is inferred from mere ancestry.

### components-and-family-grounding

grounding: concern. Targets: GO:0000813.

Current exact type/member joins support Vps23 IPR052070, Vps28 IPR007143 and explicitly fungal Vps37 IPR017435. Generated descriptions, shared UEV/Modr domains and contradictory old stoichiometry prose are not used as class evidence.

### protein-identity-and-native-coverage

grounding: supported. Targets: GO:0000813.

Three reviewed protein_examples; four typed protein nodes comprise three COVERED constituents and the external Vps27 recruiter UNANCHORED_WITH_UNIPROT P40343. This intentional external actor is not a missing constituent. Native success is identifier/coverage evidence only; current protein names, aliases, loci, review status and taxa are independently checked. Reference S288C is not silently equated with experimental SEY6210.

### taxon-and-experimental-scope

scope: supported. Targets: GO:0000813.

S. cerevisiae species and S288C reference-strain identifiers are current. Katzmann/Chu/Curtiss selected Methods identify SEY6210 derivatives; E.coli expression is not the natural host. COMMON retains the native majority-occurrence meaning, but these studies supply qualitative support rather than a prevalence census. Mammalian synonyms do not export yeast perturbations universally.

### function-and-primary-support

evidence: supported. Targets: GO:0000813.

Katzmann2001 complete primary abstract and Katzmann2003 selected body support Ub cargo recognition, external Vps27 recruitment and MVB sorting. Apparent350kDa characterization is not an exact copy-number or modern exhaustive inventory claim.

### localisation-and-provenance

provenance: supported. Targets: GO:0000813.

Native Vps37/SRN2 cytoplasmic ECO0000269 citation matches Hong1998 abstract; inferred endosomal annotations are not promoted to direct images. External Vps27 remains a recruiter, not a stable ESCRT-I constituent.

### graph-and-formation-boundaries

graph: supported. Targets: GO:0000813.

NONMECHANISTIC graph correctly separates three historical core memberships, external Vps27 recruitment, endosomal localization and sorting. Correct node diagnostics do not establish stronger causal necessity.

### necessity-and-inventory-limits

evidence: unknown. Targets: GO:0000813.

Sorting, localization, Ub binding, viability and subcomplex recovery do not establish a universal individual formation table. Mvb12 is positively acknowledged, and the cited deletion experiments retain partial subcomplexes. The optional unlisted Mvb12 row is not described as biological absence; no compulsory complete inventory or universal ESSENTIAL value is invented.

### structured-source-applicability

evidence: supported. Targets: GO:0000813.

Positive protein constituent, Ub-cargo and recruitment assertions trigger the native broad structured-source policy. Complete fresh official catalogue has no matching natural-host dataset; no proxy downstream query is warranted. The old formal exclusion is unsupported even though present bounded catalogue noncoverage is legitimate. Historical runner unavailability remains historical; no fresh runner invocation or negative biological conclusion is claimed.

### schema-history-and-verdict

schema: concern. Targets: GO:0000813.

All47 current frozen inputs and41 own historical input occurrences match;3 originals validate/render exactly and own targets are unchanged. Needs_curation retained for one grouped reconfirmed inherited minor finding(s). Historical rationale and prior corrections remain intact; no terminal disposition of unrelated issues or future CI/queue/merge certification is made. No historical access-kind occurrence(s) require successor classification correction; old context_only disclosures were honest.

### Exact structure and hierarchy

identity: supported. Targets: GO:0000814.

GO0000814 denotes the ESCRT-II complex; yeast three constituent classes and source-specific1:2:1 architecture are supported. Parent is_a and endosome part_of remain distinct.

### Exact full-component classes versus domains and paralog groups

grounding: concern. Targets: GO:0000814.

Current native family/protein joins independently resolve Vps22/Snf8 IPR016689,Q12483; Vps25 IPR008570,P47142; Vps36 IPR037855,Q06696. The inherited bounded exact-mapping finding remains open.

### Accession, primary name, aliases and status

grounding: supported. Targets: GO:0000814.

All 3 native reviewed S288C examples and current exact-gene queries match. VPS22 is synonym of primary SNF8. Identity joins do not themselves establish membership.

### Experimental source tier and actual read scope

evidence: supported. Targets: GO:0000814.

Fresh Teo author PDF and Im2008/2009 bodies support anatomy, direct interactions and activation; Hierro and Babst limited to full primary abstracts. Human constructs, yeast assays and recombinant expression remain separate.

### Counts and assembly interpretation

grounding: supported. Targets: GO:0000814.

One Vps22, two Vps25 and one Vps36 are supported in source-specific cores. Existing optional stoichiometry TODO is acknowledged; no mandatory-field defect is invented.

### Formation versus activity and targeting

grounding: unknown. Targets: GO:0000814.

UNKNOWN formation values remain justified within this source scope. Targeting defects, direct interface binding and cargo sorting do not establish blanket whole-protein formation necessity; Teo truncation and Im activation contexts are kept explicit.

### Complete coarse function graph

graph: supported. Targets: GO:0000814.

ESCRT-II membership, transient endosomal association and activation of downstream ESCRT-III are supported. Im2009 retained membrane localization of Vps20 lacking ESCRT-II binding distinguishes single-protein targeting from activation of the machinery.

### Biological, reference and expression-host scope

scope: supported. Targets: GO:0000814.

Canonical S.cerevisiae species is correct; Teo ATCC9763D material expressed in C41/B834 differs from S288C reference entries. Im2008 human proteins/BY4741 and Im2009 human fragment/BY4742 and yeast GUV reagents remain separate. COMMON is qualitative source-supported species scope, not a measured population census.

### Current host-sensitive structured-source assessment

evidence: supported. Targets: GO:0000814.

Named proteins and positive sorting/recycling pathway claims trigger policy assessment. Complete fresh official catalogue has no yeast or human host; downstream module queries are not applicable. Bacterial recombinant expression hosts are not biological-host substitutes. Historical unavailable runner is distinct from current catalogue fallback; no expression-to-assembly inference.

### Original validation, provenance and native coverage

schema: supported. Targets: GO:0000814.

Three original validate/render pairs pass with exact Markdown and39 frozen historical occurrences. Current target is unchanged. Actual focused native protein checks exit0 with populated inventory; native coverage is not biological proof. Root global/future gates are separate.

### Append-only history and exact finding lineage

provenance: supported. Targets: GO:0000814.

Historical rationale and all dated entries remain immutable. Separately authorized curation may update current notes/status or append clarification; inherited finding references preserve exact repository/review/finding identity.

### Full maintained record and bounded external evidence

completeness: supported. Targets: GO:0000814.

All fields, named evidence, examples, functions, graphs and discussions read. No maintained images. Captions are text only; no raw coordinates, unseen pixels or supplemental experiments certified. No automatic optional inventory or universal formation requirement.

### Current independent disposition

consistency: concern. Targets: GO:0000814.

Needs curation for one inherited grouped minor exact-family finding; correct identities and biological boundaries remain supported.

### Exact structure and hierarchy

identity: supported. Targets: GO:0000815.

GO0000815 denotes ESCRT-III, with explicitly yeast endosomal four-class component/graph scope; general definition legitimately includes broader membrane-remodeling settings.

### Exact full-component classes versus domains and paralog groups

grounding: supported. Targets: GO:0000815.

IPR005024 spans several CHMP paralogs and archaeal CdvB; it cannot uniquely replace each of the four named class groundings. Native current xrefs establish broader membership, not absence of any finer family elsewhere.

### Accession, primary name, aliases and status

grounding: supported. Targets: GO:0000815.

All 4 native reviewed S288C examples and current exact-gene queries match. VPS2 is synonym of primary DID4; SNF7 also has VPS32 alias. Identity joins do not themselves establish membership.

### Experimental source tier and actual read scope

evidence: supported. Targets: GO:0000815.

Babst complete primary abstract directly supports the four constituents/subcomplexes. Im2009 GUV activation and Lata engineered human polymer disassembly provide separately scoped body evidence; Henne is secondary context only.

### Counts and assembly interpretation

grounding: supported. Targets: GO:0000815.

Four core protein classes do not imply one copy each in a universal fixed tetramer. Polymers and functional subcomplexes retain source scope.

### Formation versus activity and targeting

grounding: unknown. Targets: GO:0000815.

UNKNOWN formation values remain justified within this source scope. Sorting, domain-truncation polymerization and reconstituted activation are not equated with universal individual formation necessity.

### Complete coarse function graph

graph: supported. Targets: GO:0000815.

NONMECHANISTIC graph asserts four constituents, endosomal remodeling and MVB participation; no fixed polymer geometry or complete force-generation cycle. Vps4 is a separate recycling factor.

### Biological, reference and expression-host scope

scope: supported. Targets: GO:0000815.

Yeast core and S288C native proteins are supported; broader GO biology and human CHMP truncations are comparative context, not native yeast tube measurements. COMMON is qualitative source-supported species scope, not a measured population census.

### Current host-sensitive structured-source assessment

evidence: supported. Targets: GO:0000815.

Named proteins and positive sorting/recycling pathway claims trigger policy assessment. Complete fresh official catalogue has no yeast or human host; downstream module queries are not applicable. Bacterial recombinant expression hosts are not biological-host substitutes. Historical unavailable runner is distinct from current catalogue fallback; no expression-to-assembly inference.

### Original validation, provenance and native coverage

schema: supported. Targets: GO:0000815.

Three original validate/render pairs pass with exact Markdown and39 frozen historical occurrences. Current target is unchanged. Actual focused native protein checks exit0 with populated inventory; native coverage is not biological proof. Root global/future gates are separate.

### Append-only history and exact finding lineage

provenance: supported. Targets: GO:0000815.

Historical rationale and all dated entries remain immutable. Separately authorized curation may update current notes/status or append clarification; inherited finding references preserve exact repository/review/finding identity.

### Full maintained record and bounded external evidence

completeness: supported. Targets: GO:0000815.

All fields, named evidence, examples, functions, graphs and discussions read. No maintained images. Captions are text only; no raw coordinates, unseen pixels or supplemental experiments certified. No automatic optional inventory or universal formation requirement.

### Current independent disposition

consistency: supported. Targets: GO:0000815.

Pass with limitations: positive identity, membership and function assessments, bounded family candidate search and unresolved individual formation necessity. No scientific finding manufactured.

### Exact structure and hierarchy

identity: supported. Targets: GO:1990621.

GO1990621 denotes ATP-driven ESCRT-IV recycling; yeast Vps4/Vta1 scope and exact/narrow/related synonyms agree with the native authority.

### Exact full-component classes versus domains and paralog groups

grounding: concern. Targets: GO:1990621.

IPR044538 is a complete Vta1-like family joined to Q06263. Vps4 IPR045253 is a MIT domain and IPR050304 is a broader AAA ATPase family with unchecked LLM prose; neither justifies an exact Vps4 mapping.

### Accession, primary name, aliases and status

grounding: supported. Targets: GO:1990621.

All 2 native reviewed S288C examples and current exact-gene queries match. VPS4 and VTA1 primary names match. Identity joins do not themselves establish membership.

### Experimental source tier and actual read scope

evidence: supported. Targets: GO:1990621.

Yang genuine body directly tests fragment binding and cargo sorting; planar higher arrays are speculative modeling. Lata directly disassembles engineered human polymers; Huh/Shiflett are abstract/native annotation joins only.

### Counts and assembly interpretation

grounding: supported. Targets: GO:1990621.

Two constituent classes do not establish a universal fixed Vps4 oligomer count. Fragment crystal stoichiometry and speculative planar arrays are not full-complex anatomy.

### Formation versus activity and targeting

grounding: unknown. Targets: GO:1990621.

UNKNOWN formation values remain justified within this source scope. Fragment-binding mutations and Cps1 mislocalization do not prove each complete protein is universally required for every Vps4 oligomeric state.

### Complete coarse function graph

graph: supported. Targets: GO:1990621.

Membership, proposed Vta1 stabilization, ATP-driven disassembly and recycling are appropriately coarse. Proposed arrays are not asserted as a solved lattice; external regulators are scoped out rather than claimed absent.

### Biological, reference and expression-host scope

scope: supported. Targets: GO:1990621.

Yeast Vta1/Vps4 fragments expressed in BL21/Rosetta2 differ from yeast deletion cargo assays. Native reference strain is S288C; exact assay-strain identity is not inferred. COMMON is qualitative source-supported species scope, not a measured population census.

### Current host-sensitive structured-source assessment

evidence: supported. Targets: GO:1990621.

Named proteins and positive sorting/recycling pathway claims trigger policy assessment. Complete fresh official catalogue has no yeast or human host; downstream module queries are not applicable. Bacterial recombinant expression hosts are not biological-host substitutes. Historical unavailable runner is distinct from current catalogue fallback; no expression-to-assembly inference.

### Original validation, provenance and native coverage

schema: supported. Targets: GO:1990621.

Three original validate/render pairs pass with exact Markdown and39 frozen historical occurrences. Current target is unchanged. Actual focused native protein checks exit0 with populated inventory; native coverage is not biological proof. Root global/future gates are separate.

### Append-only history and exact finding lineage

provenance: supported. Targets: GO:1990621.

Historical rationale and all dated entries remain immutable. Separately authorized curation may update current notes/status or append clarification; inherited finding references preserve exact repository/review/finding identity.

### Full maintained record and bounded external evidence

completeness: supported. Targets: GO:1990621.

All fields, named evidence, examples, functions, graphs and discussions read. No maintained images. Captions are text only; no raw coordinates, unseen pixels or supplemental experiments certified. No automatic optional inventory or universal formation requirement.

### Current independent disposition

consistency: concern. Targets: GO:1990621.

Needs curation for one inherited minor Vta1 family mapping; unresolved Vps4 exact class and speculative array scope remain explicit.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex, GO:0031205, GO:0008622, GO:0032865, GO:0033565, GO:0036452, GO:0000813, GO:0000814, GO:0000815, GO:1990621.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Qualify the three unsupported formation-essentiality assertions

major / rejected / confirmed; issue key: emrky-tolc-unsupported-formation-essentiality.

Each constituent is marked ESSENTIAL, while CPX4273 is curator-inferred and the EmrK/EmrY subunit annotations are by similarity. The cited May2009 experiment changes multiple loci and TetA(C) regulation and measures expression/biofilms; it is not a constituent-specific structural absence assay. The record supplies no source-scoped inference explaining these categorical formation requirements.

Disposition: Independent current review and peer challenge reject the original mandatory UNKNOWN-or-component-specific-formation-proof requirement as formulated. The record explicitly defines this inferred tripartite assembly and retains its source tier. Missing isolated necessity assays do not alone establish a major defect or invalidate defining constituent interpretation. This is not certification of experimentally measured necessity, evidence of dispensability, or resolution of the separate new CPX source-attribution defect. No action is retained for the rejected finding.

### micro-F2: Resolve the Pol2, Dpb2 and Dpb4 family mappings

minor / open / confirmed; issue key: epsilon-pol2-dpb2-dpb4-exact-families.

Pol2, Dpb2 and Dpb4 remain REVIEWED_LABEL_ONLY under the open exact-grounding task although fresh native IPR029703, IPR016266 and IPR051377 identify their full-protein homologous classes, supported by the maintained reference xrefs and complete IPR051377 reviewed-member list. The Dpb4-family description is LLM-flagged and is not used as primary biological evidence; membership and native metadata independently support the mapping. This does not settle the broader Dpb3 task.

### micro-F3: Record the directly observed Dpb4 stability contribution

minor / open / confirmed; issue key: epsilon-dpb4-bounded-complex-stability.

The current Dpb4 role and graph only state membership. The already cited Ohya2000 source directly reports easier Dpb2/Dpb3 dissociation from Pol2 in dpb4-deletion extracts after MonoQ chromatography. This concrete structure-level dependence can be recorded without replacing UNKNOWN with an unsupported universal ESSENTIAL.

### micro-F4: Record the established ERMES core before exact family resolution

minor / open / confirmed; issue key: ermes-known-core-inventory-deferral.

The current ermes_subunit_boundaries prompt explicitly requires exact family CURIEs before adding any Mmm1/Mdm10/Mdm12/Mdm34 rows. Freshly inspected Kornmann main body and Kawano Introduction directly identify this core. Native source-backed reviewed-label-only representation permits its known composition while exact family boundaries remain open. The inherited rationale is historical provenance and is not itself a current error.

### micro-F5: Correct CPX essential-subunit attribution in the new EmrKY edges

minor / open / confirmed; issue key: emrky-cpx-essential-subunit-attribution.

The three newly added constituent edges explicitly say CPX-4273 curates each participant as an essential stoichiometric subunit. The complete native response supplies curator-inferred participant composition with unspecified biological roles, null EmrK/EmrY counts and TolC count3, but no essentiality annotation. The formal contributes-to relations and defined tripartite membership remain supported; the defect is the specific source attribution, not a demonstration that components are dispensable or that older essentiality enums must change.

### plaque-t4-F1: Reconcile the copied Vps1 definition with the curated Vps27 complex

minor / open / confirmed; issue key: escrt-0-copied-vps1-definition-conflict.

The definition says Vps1p and Hse1p, faithfully reproducing the current GO text, while the exact synonym, Bilodeau abstract, native subunit identities and the record's resolved discussion identify Vps27p/Hse1p. The resolved discussion protects the component table but leaves the misleading definition visible.

### plaque-t4-F2: Resolve the verified Vps27/Hrs family grounding

minor / open / confirmed; issue key: escrt-0-vps27-hrs-exact-family-grounding.

The current Vps27 row is REVIEWED_LABEL_ONLY with an open exact-family task. Native IPR017073 explicitly covers Hrs/Vps27 and native P40343 corroborates membership. In contrast, the independently inspected Hse1 candidate is broader and is not part of this correction.

### plaque-t6-F1: Resolve the three verified yeast ESCRT-I families

minor / open / confirmed; issue key: escrt-i-exact-families.

The current label-only notes defer exact source-neutral family review. Native type/signature/member evidence now resolves the Vps23/TSG101 and Vps28 classes and the explicitly fungal Vps37 class without relying on a UEV/Modr domain.

### septin-escrt_ii_complex-F1: Ground the three ESCRT-II constituent classes

minor / open / confirmed; issue key: escrt-ii-exact-families.

All three named yeast subunits remain label-only although exact full families IPR016689, IPR008570 and IPR037855 are verified with independent protein membership joins. Current native family type/signature/hierarchy and independent protein cross-references reconfirm this bounded open mapping. Preserve historical rationale; correct current notes/status or append a dated clarification during separately authorized curation.

### septin-escrt_iv_complex-F1: Ground the Vta1 cofactor to its verified family

minor / open / confirmed; issue key: escrt-iv-vta1-exact-family.

The Vta1 row remains reviewed label-only despite exact full-family IPR044538 and an independent Q06263 membership join. The Vps4 candidate limitations do not justify deferring this separately resolved constituent. Current native family type/signature/hierarchy and independent protein cross-references reconfirm this bounded open mapping. Preserve historical rationale; correct current notes/status or append a dated clarification during separately authorized curation.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, ground Pol2 with IPR029703, Dpb2 with IPR016266 and Dpb4 with IPR051377, keeping the reference accession/taxon pairs separate and narrowing the open task to classes not yet securely resolved.

- Verify exact family identity/type and separate representative membership.
- Do not substitute a shared histone fold or broad transcription-factor family for an unresolved subunit.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Retain homologous family scope and shared-complex membership; do not use LLM-generated family prose as a primary experiment or conflate Dpb3/POLE4 with Dpb4/POLE3.
- Preserve dated discussions.rationale, posed_date and curation history; narrow only current prompt/notes as supported.
- No record edits occur in this review PR.

### micro-A2

In separately authorized record curation, add a source-scoped Dpb4 contribution to stability/retention of Dpb2 and Dpb3 with Pol2, explicitly tied to the mutant-extract chromatography experiment. Preserve UNKNOWN where whole-complex formation necessity remains unestablished.

- Cite Results sec15 and Figure1 for the physical readout.
- Distinguish observed association/stability from cell viability, replication timing and intrinsic polymerase activity.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Global UNKNOWN may remain; no universal ESSENTIAL, complete intracellular absence or new experiment is required.
- Preserve dated discussions.rationale, posed_date and curation history; narrow only current prompt/notes as supported.
- No record edits occur in this review PR.

### micro-A3

In separately authorized record curation, add source-backed named core rows with honest unresolved family grounding and formation necessity where appropriate; revise the TODO to concern exact mappings rather than block known membership. Do not infer peripheral-factor inventory, copy counts or universal ESSENTIAL labels from this review.

- All four core identities and their roles cite the appropriate primary passages.
- Species examples, if added later, remain distinct from class-level grounding.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; narrow only current prompt/notes as supported.
- No record edits occur in this review PR.

### micro-A4

In separately authorized record curation, qualify the three CPX evidence notes as curator-inferred participant composition, retaining unspecified EmrK/EmrY copy numbers and TolC3. If a separate defining-assembly necessity inference is explained, label it as an inference rather than an explicit CPX essentiality annotation.

- Correct only the unsupported CPX attribution at edges5–7 evidence[0].notes; preserve supported contributes-to relations and the defined tripartite boundary.
- Do not automatically retype older component ESSENTIAL values, infer dispensability or demand a new depletion/assembly experiment.
- Preserve ECO0005547/source-tier limits, unknown EmrK/EmrY counts and historical rationale/events.
- Run applicable native schema, strict, identifier and graph checks after separately authorized curation; no record edits occur here.

### plaque-t4-A1

Correct the local definition to Vps27p with an appropriate primary-source attribution or explicit qualifier documenting the native GO discrepancy. Preserve GO0033565 identity, correct component rows and historical evidence rather than silently rewriting the external source.

- The visible definition no longer presents Vps1 as the curated ESCRT-0 constituent.
- The source relationship and known GO discrepancy remain explicit.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated discussion rationale and history verbatim; append current evidence/notes or update an active decision only within the separately authorized record curation.

### plaque-t4-A2

Add InterPro:IPR017073 to the existing Vps27 class with exact source evidence and update its grounding state/task. Keep P40343 as the taxon-paired example and retain Hse1 label-only unless a genuinely exact class is separately verified.

- The new grounding denotes the Hrs/Vps27 whole-protein family, not its domains.
- The mixed Hse1 candidate is not adopted as an exact substitute.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated discussion rationale and history verbatim; append current evidence/notes or update an active decision only within the separately authorized record curation.

### plaque-t6-A1

Use IPR052070 for Vps23, IPR007143 for Vps28 and IPR017435 for the explicitly yeast/fungal Vps37 constituent; align current grounding notes/TODO while preserving Mvb12 follow-up.

- Keep Vps37 fungal scope explicit rather than claiming one family covers all metazoan paralogs.
- Retain correct gene aliases and the separate Mvb12 inventory discussion.
- Preserve supported identities and biological scope; pass applicable native gates.
- Preserve dated discussion rationale and history verbatim; append current evidence/notes or update an active decision only within the separately authorized record curation.

### septin-escrt_ii_complex-A1

Use IPR016689 for Vps22/Snf8, IPR008570 for Vps25 and IPR037855 for Vps36, aligning current notes/TODO. Preserve dated rationale/history and exact inherited finding lineage; update current notes or append clarification. This review PR edits no record.

- Do not substitute a shared winged-helix or GLUE/NZF domain.
- Preserve two Vps25 copies where source-scoped stoichiometry is later curated; keep reference-strain/experimental-system distinctions.
- Preserve supported identities and biological scope; pass applicable native gates.
- Do not rewrite historical rationale, force unresolved paralog/domain mappings, or infer universal formation necessity from membership.

### septin-escrt_iv_complex-A1

Use IPR044538 for Vta1 and narrow the current family TODO to genuinely unresolved Vps4 boundaries. Preserve dated rationale/history and exact inherited finding lineage; update current notes or append clarification. This review PR edits no record.

- Preserve the Vps4 label-only row until an exact full-class mapping is established.
- Do not promote the speculative lattice model or inferred oligomeric count to fixed whole-complex anatomy.
- Preserve supported identities and biological scope; pass applicable native gates.
- Do not rewrite historical rationale, force unresolved paralog/domain mappings, or infer universal formation necessity from membership.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1db4b3ec61bb37a31a2c8888ca43d294cbd73241734f58891d8b3bbc4bac53b1; current SHA256 7537240a1770406c3b0b6272ef277be10afa2a64fe43e40d9e75729ae00bae4a. Changed record reassessed against current sources. |
| original-review-0 | reviews/structured/20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/endoplasmic_reticulum_sec_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f; current SHA256 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T063719Z-endoplasmic-reticulum-sec-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/epsilon_dna_polymerase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635; current SHA256 d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T063720Z-epsilon-dna-polymerase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/ermes_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9; current SHA256 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T063721Z-ermes-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/escrt_0_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d; current SHA256 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/escrt_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e; current SHA256 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T063722Z-escrt-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/escrt_i_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc; current SHA256 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/escrt_ii_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7; current SHA256 e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T063724Z-escrt-ii-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/escrt_iii_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8; current SHA256 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T063725Z-escrt-iii-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/escrt_iv_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2; current SHA256 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T063726Z-escrt-iv-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml; Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target differs by four added graph edges and dated history. |
| micro-prior-0 | reviews/structured/20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, source tiers, assessments, verdict, findings and actions inspected. Historical checks and access observations are not new executions or new body reads. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/0-stale.diff; Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446 | supports | Three constituent contributes-to edges and one transport-to-export edge were added with dated history. Formal membership and coarse export are reassessed separately from the new evidence-note attribution. |
| micro-record-1 | data/structures/other/endoplasmic_reticulum_sec_complex.yaml; Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target unchanged from original frozen input. |
| micro-prior-1 | reviews/structured/20261022T063719Z-endoplasmic-reticulum-sec-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, source tiers, assessments, verdict, findings and actions inspected. Historical checks and access observations are not new executions or new body reads. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/1-stale.diff; Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446 | supports | Empty diff; current bytes equal original frozen target. |
| micro-record-2 | data/structures/other/epsilon_dna_polymerase_complex.yaml; Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target unchanged from original frozen input. |
| micro-prior-2 | reviews/structured/20261022T063720Z-epsilon-dna-polymerase-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, source tiers, assessments, verdict, findings and actions inspected. Historical checks and access observations are not new executions or new body reads. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/2-stale.diff; Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446 | supports | Empty diff; current bytes equal original frozen target. |
| micro-record-3 | data/structures/other/ermes_complex.yaml; Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or quantitative physical measurements. Current target unchanged from original frozen input. |
| micro-prior-3 | reviews/structured/20261022T063721Z-ermes-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, source tiers, assessments, verdict, findings and actions inspected. Historical checks and access observations are not new executions or new body reads. |
| micro-delta-3 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/3-stale.diff; Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446 | supports | Empty diff; current bytes equal original frozen target. |
| micro-policy | docs/CURATION.md; Components and Discussions clauses | supports | Taxon-neutral families/classes and honest reviewed-label-only constituents are valid. Formation differs from function and viability. Dated rationale and posed_date are preserved; current prompt/notes may be narrowed only as supported. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, ComponentGroundingStatusEnum and causal node types | supports | ESSENTIAL means the defined structure does not form without the constituent; policy does not require a particular deletion assay for every defining subunit. This is distinct from attributing an essentiality annotation to a source that supplies only membership. UNKNOWN may coexist with condition-scoped stability evidence. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record review, Structured Source Cross-Checks and source-evidence contract | supports | Positive named proteins/regulators/pathways trigger applicability assessment even without transcriptomic claims or populated examples. Exact matched dataset context is bounded and does not establish physical assembly. |
| micro-profile | docs/record-review-profile.md; Native persistence and source provenance | supports | Only concrete review or scientific defects are findings. Unavailable routes, optional empty fields and retained uncertainty alone do not constitute scientific defects. Root owns successor save and global/future gates. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Claim-scoped constituents, function and assembly relations | supports | Membership, coarse function, measured stability and mechanistic transitions remain distinct. No compulsory universal necessity, exact count or new experiment is imposed. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/original-audit.json; Eight actual original native validate/render commands; 56 historical input occurrences; eight original artifacts | supports | All four original YAMLs validate and render exactly the retained Markdown; historical hashes match recorded revisions and eight artifacts match original PR head. |
| micro-protein-P02930 | https://rest.uniprot.org/uniprotkb/P02930.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P02930.raw | supports | P02930: UniProtKB reviewed (Swiss-Prot); Outer membrane protein TolC; genes ['tolC']; loci ['b3035', 'JW5503']; taxon 83333; InterPro ['IPR003423', 'IPR010130', 'IPR058622', 'IPR051906']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-protein-P21951 | https://rest.uniprot.org/uniprotkb/P21951.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P21951.raw | supports | P21951: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon catalytic subunit A; genes ['POL2']; loci ['YNL262W', 'N0825']; taxon 559292; InterPro ['IPR006172', 'IPR006133', 'IPR043502', 'IPR042087', 'IPR013697', 'IPR023211', 'IPR029703', 'IPR055191', 'IPR012337', 'IPR036397', 'IPR063197', 'IPR054475']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-protein-P24482 | https://rest.uniprot.org/uniprotkb/P24482.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P24482.raw | supports | P24482: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon subunit B; genes ['DPB2']; loci ['YPR175W', 'P9705.7']; taxon 559292; InterPro ['IPR007185', 'IPR063374', 'IPR016266']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-protein-P27344 | https://rest.uniprot.org/uniprotkb/P27344.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P27344.raw | supports | P27344: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon subunit C; genes ['DPB3']; loci ['YBR278W', 'YBR2015']; taxon 559292; InterPro ['IPR009072', 'IPR050568']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-protein-P52599 | https://rest.uniprot.org/uniprotkb/P52599.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P52599.raw | supports | P52599: UniProtKB reviewed (Swiss-Prot); Probable multidrug resistance protein EmrK; genes ['emrK']; loci ['b2368', 'JW2365']; taxon 83333; InterPro ['IPR058634', 'IPR058633', 'IPR050739', 'IPR005694']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-protein-P52600 | https://rest.uniprot.org/uniprotkb/P52600.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P52600.raw | supports | P52600: UniProtKB reviewed (Swiss-Prot); Probable multidrug resistance protein EmrY; genes ['emrY']; loci ['b2367', 'JW2364']; taxon 83333; InterPro ['IPR004638', 'IPR011701', 'IPR020846', 'IPR036259']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-protein-Q04603 | https://rest.uniprot.org/uniprotkb/Q04603.json; Native identity/status/name, complete gene aliases/loci/taxon, InterPro xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-Q04603.raw | supports | Q04603: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon subunit D; genes ['DPB4']; loci ['YDR121W']; taxon 559292; InterPro ['IPR051377', 'IPR009072']. Annotation evidence tiers and organism-specific examples remain separate from primary body and family-level claims. |
| micro-query-DPB2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-DPB2.raw | supports | Current bounded query returns ['P24482']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-query-DPB3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-DPB3.raw | supports | Current bounded query returns ['P27344']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-query-DPB4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-DPB4.raw | supports | Current bounded query returns ['Q04603']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-query-POL2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-POL2.raw | supports | Current bounded query returns ['P21951']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-query-emrK | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrK%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-emrK.raw | supports | Current bounded query returns ['P52599']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-query-emrY | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrY%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-emrY.raw | supports | Current bounded query returns ['P52600']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-query-tolC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-tolC.raw | supports | Current bounded query returns ['P02930']; primary genes and aliases separately inspected. This does not reconstruct or disprove a dated historical selection query. |
| micro-taxon-4932 | https://rest.uniprot.org/taxonomy/4932; Scientific name, rank, parent, lineage and strain context; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/taxon-4932.raw | supports | 4932: Saccharomyces cerevisiae; rank species. Species, reference strain and exact experimental preparation are distinct. |
| micro-taxon-559292 | https://rest.uniprot.org/taxonomy/559292; Scientific name, rank, parent, lineage and strain context; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/taxon-559292.raw | supports | 559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c); rank strain. Species, reference strain and exact experimental preparation are distinct. |
| micro-taxon-83333 | https://rest.uniprot.org/taxonomy/83333; Scientific name, rank, parent, lineage and strain context; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/taxon-83333.raw | supports | 83333: Escherichia coli (strain K12); rank strain. Species, reference strain and exact experimental preparation are distinct. |
| micro-ancestors-GO0008622 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008622/ancestors?relations=is_a; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/ancestors-GO0008622.raw | supports | GO:0008622 epsilon DNA polymerase complex; obsolete=False. A heterotetrameric DNA polymerase complex that catalyzes processive DNA synthesis in the absence of PCNA, but is further stimulated in the presence of PCNA. The complex contains a large catalytic subunit and three small subunits, and is best characterized in Saccharomyces, in which the subunits are named Pol2p, Dpb2p, Dpb3p, and Dpb4p. Some evidence suggests that DNA polymerase epsilon is the leading strand polymerase; it is also involved in nucleotide-excision repair and mismatch repair. Ancestors ['GO:0061695', 'GO:1902494', 'GO:1990234', 'GO:0140535', 'GO:0140513', 'GO:0032991', 'GO:0042575', 'GO:0005575', 'GO:0008622'] |
| micro-ancestors-GO0031205 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205/ancestors?relations=is_a; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/ancestors-GO0031205.raw | supports | GO:0031205 endoplasmic reticulum Sec complex; obsolete=False. An endoplasmic reticulum membrane-associated complex involved in the translocation of proteins that are targeted to the ER. In yeast, this complex consists of two subcomplexes, namely, the Sec61 complex and the Sec62/Sec63 complex. Ancestors ['GO:0098796', 'GO:0032991', 'GO:0140534', 'GO:0005575', 'GO:0031205'] |
| micro-ancestors-GO0032865 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032865/ancestors?relations=is_a; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/ancestors-GO0032865.raw | supports | GO:0032865 ERMES complex; obsolete=False. A protein complex that links the endoplasmic reticulum with mitochondria and may have a role in promoting exchange of calcium and phospholipids between the two organelles. Ancestors ['GO:0098796', 'GO:0098799', 'GO:0098798', 'GO:0032991', 'GO:0140534', 'GO:0032865', 'GO:0005575'] |
| micro-go-0005741 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005741; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005741.raw | supports | GO:0005741 mitochondrial outer membrane; obsolete=False. The outer, i.e. cytoplasm-facing, lipid bilayer of the mitochondrial envelope. |
| micro-go-0005783 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005783.raw | supports | GO:0005783 endoplasmic reticulum; obsolete=False. The irregular network of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm of many eukaryotic cells. The membranes form a complex meshwork of tubular channels, which are often expanded into slitlike cavities called cisternae. The ER takes two forms, rough (or granular), with ribosomes adhering to the outer surface, and smooth (with no ribosomes attached). |
| micro-go-0005784 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005784; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005784.raw | supports | GO:0005784 Sec61 translocon complex; obsolete=False. A translocon complex that contains a core heterotrimer of conserved alpha, beta and gamma subunits, and may contain additional proteins (translocon-associated proteins or TRAPs); in budding yeast the core proteins are Sec61p, Sbh1p, and Sss1p. The Sec61 translocon complex functions in cotranslational and posttranslational translocation events. |
| micro-go-0005789 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005789; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005789.raw | supports | GO:0005789 endoplasmic reticulum membrane; obsolete=False. The lipid bilayer surrounding the endoplasmic reticulum. |
| micro-go-0006260 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0006260.raw | supports | GO:0006260 DNA replication; obsolete=False. The cellular metabolic process in which a cell duplicates one or more molecules of DNA. DNA replication begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, and ends when the original DNA molecule has been completely duplicated and the copies topologically separated. The unit of replication usually corresponds to the genome of the cell, an organelle, or a virus. The template for replication can either be an existing DNA molecule or RNA. |
| micro-go-0008622 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008622; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0008622.raw | supports | GO:0008622 epsilon DNA polymerase complex; obsolete=False. A heterotetrameric DNA polymerase complex that catalyzes processive DNA synthesis in the absence of PCNA, but is further stimulated in the presence of PCNA. The complex contains a large catalytic subunit and three small subunits, and is best characterized in Saccharomyces, in which the subunits are named Pol2p, Dpb2p, Dpb3p, and Dpb4p. Some evidence suggests that DNA polymerase epsilon is the leading strand polymerase; it is also involved in nucleotide-excision repair and mismatch repair. |
| micro-go-0031205 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0031205.raw | supports | GO:0031205 endoplasmic reticulum Sec complex; obsolete=False. An endoplasmic reticulum membrane-associated complex involved in the translocation of proteins that are targeted to the ER. In yeast, this complex consists of two subcomplexes, namely, the Sec61 complex and the Sec62/Sec63 complex. |
| micro-go-0031207 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031207; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0031207.raw | supports | GO:0031207 Sec62/Sec63 complex; obsolete=False. A protein complex involved in the posttranslational targeting of proteins to the ER. In yeast, it is a tetrameric complex consisting of Sec62p, Sec63p, Sec71p and Sec72p. |
| micro-go-0032865 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032865; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0032865.raw | supports | GO:0032865 ERMES complex; obsolete=False. A protein complex that links the endoplasmic reticulum with mitochondria and may have a role in promoting exchange of calcium and phospholipids between the two organelles. |
| micro-go-0042575 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042575; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0042575.raw | supports | GO:0042575 DNA polymerase complex; obsolete=False. A protein complex that possesses DNA polymerase activity and is involved in template directed synthesis of DNA. |
| micro-go-0042910 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042910; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0042910.raw | supports | GO:0042910 xenobiotic transmembrane transporter activity; obsolete=False. Enables the directed movement of a xenobiotic from one side of a membrane to the other. A xenobiotic is a compound foreign to the organism exposed to it. It may be synthesized by another organism (like ampicilin) or it can be a synthetic chemical. |
| micro-go-0098799 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098799; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0098799.raw | supports | GO:0098799 outer mitochondrial membrane protein complex; obsolete=False. Any protein complex that is part of the outer mitochondrial membrane. |
| micro-go-0140330 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140330; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0140330.raw | supports | GO:0140330 xenobiotic detoxification by transmembrane export across the cell outer membrane; obsolete=False. A process that reduces or removes the toxicity of a xenobiotic by exporting it outside the cell through the outer membrane. |
| micro-go-0140534 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140534; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0140534.raw | supports | GO:0140534 endoplasmic reticulum protein-containing complex; obsolete=False. A protein complex that is part of an endoplasmic reticulum. |
| micro-go-1990281 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990281; Exact active term definition and, where requested, complete returned is_a ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-1990281.raw | supports | GO:1990281 efflux pump complex; obsolete=False. A protein complex that is capable of efflux transmembrane transporter activity. |
| micro-family-IPR004638 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004638/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR004638.raw | supports | IPR004638: Drug resistance transporter EmrB-like; native type family. Broader homologous class is distinguished from the narrower named component; it is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping. |
| micro-family-IPR005694-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005694/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR005694-retry.raw | supports | IPR005694: Membrane fusion proteins, proteobacteria; native type family. Broader homologous class is distinguished from the narrower named component; it is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping. |
| micro-family-IPR016266 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016266/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR016266.raw | supports | IPR016266: DNA polymerase epsilon, subunit B; native type family. Native family identity/type and example membership assessed separately; database prose is authority context, not a new primary experiment. |
| micro-family-IPR029703 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029703/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR029703.raw | supports | IPR029703: DNA polymerase epsilon catalytic subunit; native type family. Native family identity/type and example membership assessed separately; database prose is authority context, not a new primary experiment. |
| micro-family-IPR050568 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050568/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR050568.raw | supports | IPR050568: Transcription/DNA replication regulator; native type family. Broader homologous class is distinguished from the narrower named component; it is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping. |
| micro-family-IPR050739 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050739/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR050739.raw | supports | IPR050739: Membrane Fusion Protein; native type family. Native family identity/type and example membership assessed separately; database prose is authority context, not a new primary experiment. |
| micro-family-IPR051377 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051377/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR051377.raw | supports | IPR051377: DNA Polymerase Epsilon Subunit; native type family. Dpb4/POLE3-family membership is corroborated by the complete reviewed-member response and Q04603 native xref. LLM-flagged description is not used as primary biological evidence. |
| micro-family-IPR058622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR058622.raw | supports | IPR058622: Outer membrane channel protein TolC; native type family. Native family identity/type and example membership assessed separately; database prose is authority context, not a new primary experiment. |
| micro-family-TIGR00711 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR00711/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-TIGR00711.raw | supports | TIGR00711: DHA2 family efflux MFS transporter permease subunit; native type family. Broader homologous class is distinguished from the narrower named component; it is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping. |
| micro-family-TIGR00998 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR00998/; Complete entry metadata/type, description flags and integrated signatures; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-TIGR00998.raw | supports | TIGR00998: EmrA/EmrK family multidrug efflux transporter periplasmic adaptor subunit; native type family. Broader homologous class is distinguished from the narrower named component; it is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping. |
| micro-IPR051377-reviewed-retry | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051377/?page_size=200; Complete 15 reviewed-member identities, names, taxa and native genes; no next page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/IPR051377-reviewed-retry.raw | supports | Current family membership includes Q04603/DPB4 and homologous Dpb4/POLE3 class members. Other complex associations and species-specific names are not erased; the family is not an exclusive Pol-epsilon membership assay. |
| micro-complex-CPX-4273 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4273; Complete Complex Portal response: identity, organism, evidence, participant identifiers/roles/counts, properties and references; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/complex-CPX-4273.raw | supports | CPX-4273 defines the E.coli K12 EmrKY-TolC tripartite efflux system using ECO0005547 curator inference. EmrK P52599 and EmrY P52600 have null copy numbers, TolC P02930 has count3; biological roles are unspecified. No constituent essentiality annotation is supplied. Source membership/inference does not equal direct experimental formation necessity. |
| micro-eco-0005547 | https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FECO_0005547; Complete native ECO identity, definition and explanatory description; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/eco-0005547.raw | supports | ECO0005547 is biological-system reconstruction based on background scientific knowledge in manual assertion; its description explicitly distinguishes inference from physical-interaction evidence. It is not an experimental assembly assay. |
| micro-doi-0 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0092-8674%2895%2990077-2%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-0.raw | supports | PMID 7758110; DOI 10.1016/0092-8674(95)90077-2; Posttranslational protein transport in yeast reconstituted with a purified complex of Sec proteins and Kar2p.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e03-06-0390%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-1.raw | supports | PMID 14617809; DOI 10.1091/mbc.e03-06-0390; Interactions between Sec complex and prepro-alpha-factor during posttranslational protein transport into the endoplasmic reticulum.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-doi-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-018-0856-x%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-2.raw | supports | PMID 30644436; DOI 10.1038/s41586-018-0856-x; Structure of the post-translational protein translocation machinery of the ER membrane.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1175088%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-3.raw | supports | PMID 19556461; DOI 10.1126/science.1175088; An ER-mitochondria tethering complex revealed by a synthetic biology screen.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-doi-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201704119%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-4.raw | supports | PMID 29279306; DOI 10.1083/jcb.201704119; Structure-function insights into direct lipid transfer between membranes by Mmm1-Mdm12 of ERMES.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-11024162 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11024162+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-11024162.raw | supports | PMID 11024162; DOI 10.1093/nar/28.20.3846; Structure and function of the fourth subunit (Dpb4p) of DNA polymerase epsilon in Saccharomyces cerevisiae.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-12571237 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12571237+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-12571237.raw | supports | PMID 12571237; DOI 10.1074/jbc.m211818200; The quaternary structure of DNA polymerase epsilon from Saccharomyces cerevisiae.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-14562095.raw | supports | PMID 14562095; DOI 10.1038/nature02026; Global analysis of protein localization in budding yeast.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-15814431 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15814431+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-15814431.raw | supports | PMID 15814431; DOI 10.1080/10409230590935433; DNA polymerases that propagate the eukaryotic DNA replication fork.. Secondary review abstract only; not a primary experiment. |
| micro-pmid-16369485 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16369485+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-16369485.raw | supports | PMID 16369485; DOI 10.1038/nsmb1040; Structure of Saccharomyces cerevisiae DNA polymerase epsilon by cryo-electron microscopy.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-19721076 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19721076+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-19721076.raw | supports | PMID 19721076; DOI 10.1128/aac.00454-09; Induction of multidrug resistance mechanism in Escherichia coli biofilms by interplay between tetracycline and ampicillin resistance genes.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-25538242 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25538242+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-25538242.raw | supports | PMID 25538242; DOI 10.1074/jbc.m114.615278; Yeast DNA polymerase ϵ catalytic core and holoenzyme have comparable catalytic rates.. Primary-study indexed abstract/metadata tier. Genuine separately inspected body evidence is named separately. |
| micro-pmid-9745046 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9745046+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact identifier metadata and complete indexed abstract; no article body inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-9745046.raw | supports | PMID 9745046; DOI 10.1007/s004120050300; Eukaryotic DNA polymerases in DNA replication and DNA repair.. Secondary review abstract only; not a primary experiment. |
| micro-PMC2772303-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2772303/; Methods sec2 strains and sec7 qPCR, complete Results/Discussion sec14 and sec15 with Figure4/5 text captions; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2772303-legacy.raw | supports | May2009 tests MG1655/pBR322 and a multi-locus modified OCL62 background with TetA(C) regulatory changes. EmrKY expression, biofilm and resistance phenotypes are context-specific; no isolated three-subunit formation assay is established. These limits do not establish component dispensability. |
| micro-PMC110797-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC110797/; Methods sec3/Table1 and sec5 purification, Results sec13–16 with Figure1/2 captions, Discussion sec19; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC110797-legacy.raw | supports | Ohya identifies Dpb4 and tests dpb4-deletion preparations. After MonoQ chromatography Dpb2 and Dpb3 dissociate more readily from Pol2, with degradation/mixture limitations. This supports a bounded stability annotation, not universal ESSENTIAL, organism viability equivalence or complete intracellular complex absence. |
| micro-PMC307522-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC307522/; Methods sec3 purification/strains, sec6 binding, sec7 transport intermediates, sec8 denaturing immunoprecipitation; complete Results sec11 and Figure1/2 captions/Table1; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC307522-legacy.raw | supports | Plath directly tests precursor interactions with Sec61 and Sec62, including a discriminating denaturing immunoprecipitation despite Sec62/Sec71 comigration. Initial binding and Kar2-dependent subsequent translocation are distinct. This supports the parent subcomplex topology without duplicating all individual proteins. |
| micro-PMC6367035-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6367035/; Main paragraphs5–19 including Figure1–3 text captions; Methods S2, S3, S4 and S6; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC6367035-legacy.raw | supports | Wu2019 purifies the seven-component yeast Sec assembly from BY4741 and resolves its overall architecture at4.1Angstrom. Sec62 density/model coverage is limited, including docking/one membrane helix; the paper does not completely atomically resolve every Sec62 segment. No pixels, coordinates or supplementary methods were reanalyzed. |
| micro-PMC2933203-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2933203/; Complete scientific main paragraphs4–29 and Figure1–4 text captions; paragraphs25–37 additionally checked for terminal limits/reference boundary; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2933203-legacy.raw | supports | Kornmann identifies the Mmm1/Mdm10/Mdm12/Mdm34 core through the synthetic-tether screen and subsequent localization/rescue/association evidence. Mmm1 is ER-localized, Mdm10 also participates in SAM, and loss of core puncta is condition-scoped. Genetic lipid-flux and calcium context is not direct proof of every whole-complex transport mechanism. |
| micro-PMC5839780-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5839780/; Introduction s01, complete Results s06 and s07 with Figure4–6 captions, Discussion s08/Figure7, Methods s11 strains and s18 lipid assays; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC5839780-legacy.raw | supports | Kawano tests recombinant Mmm1-Mdm12 lipid transfer between model membranes, and separate yeast mutant heavy-membrane-fraction assays. K.lactis recombinant modules, S.cerevisiae Vps13-suppressed mutants and full in-vivo ERMES function remain distinct; carrier/conduit models are not settled universal mechanisms. |
| micro-PMC4319046-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4319046/; Methods sec5–7 and Results sec16–18, sec20–21 including embedded Figure1–4/6–7 captions and tables; text/captions only, no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC4319046-legacy.raw | supports | Ganai compares purified whole Pol-epsilon with Pol2 core1–1228 in biochemical assays. Catalysis/processivity and loading effects are assay-specific; changes in accessory subunits and C-terminal sequence are not an isolated necessity test for each constituent. |
| micro-asturias2006-publisher | https://www.nature.com/articles/nsmb1040; Genuine publisher abstract/metadata only; article body is paywalled; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/asturias2006-publisher.raw | supports | Publisher page exposes abstract, citations and author metadata; it is not a fresh full-body read. The indexed abstract supports the broad Pol-epsilon architecture observation at its stated EM scope. |
| micro-access-PMC2772303-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2772303.1/PMC2772303.1.xml; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2772303-jats.receipt.json and response content | context_only | HTTP 404; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-PMC110797-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC110797.1/PMC110797.1.xml; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC110797-jats.receipt.json and response content | context_only | HTTP 404; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-PMC2772303-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2772303/fullTextXML; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2772303-epmc.receipt.json and response content | context_only | HTTP 500; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-PMC110797-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC110797/fullTextXML; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC110797-epmc.receipt.json and response content | context_only | HTTP 500; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-PMC307522-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC307522/fullTextXML; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC307522-epmc.receipt.json and response content | context_only | HTTP 500; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-PMC2933203-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2933203/fullTextXML; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2933203-epmc.receipt.json and response content | context_only | HTTP 500; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-PMC4319046-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4319046/fullTextXML; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC4319046-epmc.receipt.json and response content | context_only | HTTP 500; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-panzner1995-publisher | https://doi.org/10.1016/0092-8674(95)90077-2; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/panzner1995-publisher.receipt.json and response content | context_only | HTTP 200; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-panzner1995-pii | https://www.cell.com/cell/fulltext/0092-8674(95)90077-2; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/panzner1995-pii.receipt.json and response content | context_only | HTTP 403; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-chilkova2003-doi | https://doi.org/10.1074/jbc.M211818200; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/chilkova2003-doi.receipt.json and response content | context_only | HTTP 200; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-chilkova2003-correct-pdf | https://www.jbc.org/article/S0021-9258(19)64558-8/pdf; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/chilkova2003-correct-pdf.receipt.json and response content | context_only | HTTP 403; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-family-IPR005694 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005694/; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR005694.receipt.json and response content | context_only | HTTP 429; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-access-IPR051377-reviewed | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051377/?page_size=200; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/IPR051377-reviewed.receipt.json and response content | context_only | HTTP 429; access/status-only observation. Redirect, challenge, unavailable full text or rate limit is not scientific evidence. Successful genuine body or retried authority response is separately cited; no failed-route absence inference. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/catalogue.raw | context_only | Twenty organism rows and28 organism/dataset pairs read. E.coli precise1k is covered; no Saccharomyces dataset appears in this exact response. No foreign-host proxy is used for the three yeast records. |
| micro-dataset-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete e_coli/precise1k metadata; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/dataset-meta.raw | context_only | Five strains BW25113,DGF-298,GMOS,MG1655,W3110;201 modules,1035 samples,518 conditions,4257 genes. This is mixed-strain expression context, not the specific May OCL62/pBR322 experiment. |
| micro-dataset-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 module identifiers and native metadata; AI-generated summaries and activities excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/dataset-modules.raw | context_only | Complete inventory defines the bounded membership population. It does not supply direct binding, assembly, causal regulation or resistance assays. |
| micro-dataset-genes | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;limit=5000; Complete4257 reference-gene table, exact three maintained-locus joins; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/dataset-genes.raw | context_only | b2368=emrK/P52599,b2367=emrY/P52600,b3035=tolC/P02930. Only these exact joins are scientifically used; no all-gene functional audit is claimed. |
| micro-membership-b2368 | https://imodulondb.org/api/genes/b2368/imodulons?organism=e_coli&amp;dataset=precise1k; All201 returned membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/membership-b2368.raw | context_only | Exact b2368 has one thresholded hit: [{'k': 38, 'weight': 0.167808741, 'threshold': 0.087369631}]. Other nonhits are not biological absence or dispensability. |
| micro-membership-b2367 | https://imodulondb.org/api/genes/b2367/imodulons?organism=e_coli&amp;dataset=precise1k; All201 returned membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/membership-b2367.raw | context_only | Exact b2367 has one thresholded hit: [{'k': 38, 'weight': 0.122770016, 'threshold': 0.087369631}]. Other nonhits are not biological absence or dispensability. |
| micro-membership-b3035 | https://imodulondb.org/api/genes/b3035/imodulons?organism=e_coli&amp;dataset=precise1k; All201 returned membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/membership-b3035.raw | context_only | Exact b3035 has one thresholded hit: [{'k': 22, 'weight': 0.033449641, 'threshold': 0.030026006}]. Other nonhits are not biological absence or dispensability. |
| micro-module-22 | https://imodulondb.org/api/imodulons/e_coli/precise1k/22; Native metadata, threshold and all member IDs/weights; generated prose and activity vectors excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-22.raw | context_only | SoxS module22: 117 members. Exact retained loci corroborate bounded expression context only, not assembly, stoichiometry or component necessity. |
| micro-module-22-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes; All117 member identity/weight/threshold rows; exact selected-locus native accessions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-22-genes.raw | context_only | Member IDs and weights agree with module22 metadata; selected native identity joins agree with maintained examples. No direct regulatory or mechanistic inference. |
| micro-module-38 | https://imodulondb.org/api/imodulons/e_coli/precise1k/38; Native metadata, threshold and all member IDs/weights; generated prose and activity vectors excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-38.raw | context_only | EvgA module38: 15 members. Exact retained loci corroborate bounded expression context only, not assembly, stoichiometry or component necessity. |
| micro-module-38-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/38/genes; All15 member identity/weight/threshold rows; exact selected-locus native accessions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-38-genes.raw | context_only | Member IDs and weights agree with module38 metadata; selected native identity joins agree with maintained examples. No direct regulatory or mechanistic inference. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z receipt | context_only | Historical runner unavailable with exit1/PermissionError reading pyvenv.cfg; no new runner invocation. Actual present direct-source fallback is separate. |
| micro-native-emrky_tolc_multidrug_efflux_transport_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 3 maintained reviewed examples and 3 COVERED typed GENE_OR_PROTEIN nodes; all declared native node symbols are covered. Native success does not establish complete biological scope or exact family identity. |
| micro-native-emrky_tolc_multidrug_efflux_transport_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal.log SHA256 8c7e3458522c33d3bce89abbe58b15f4f8f468d3b01f0625bd807e3e464c9a6c | supports | Actual exit0; 3 maintained reviewed examples and 3 COVERED typed GENE_OR_PROTEIN nodes; all declared native node symbols are covered. Native success does not establish complete biological scope or exact family identity. |
| micro-native-endoplasmic_reticulum_sec_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN nodes; empty native inventory is not biological completeness. Native success does not establish complete biological scope or exact family identity. |
| micro-native-endoplasmic_reticulum_sec_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN nodes; empty native inventory is not biological completeness. Native success does not establish complete biological scope or exact family identity. |
| micro-native-epsilon_dna_polymerase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 4 maintained reviewed examples and 4 COVERED typed GENE_OR_PROTEIN nodes; all declared native node symbols are covered. Native success does not establish complete biological scope or exact family identity. |
| micro-native-epsilon_dna_polymerase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-causal.log SHA256 6f8e9867949e29c1044c6f57d6788b7d019afd1c2891b5256df95d0edf86a29d | supports | Actual exit0; 4 maintained reviewed examples and 4 COVERED typed GENE_OR_PROTEIN nodes; all declared native node symbols are covered. Native success does not establish complete biological scope or exact family identity. |
| micro-native-ermes_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN nodes; empty native inventory is not biological completeness. Native success does not establish complete biological scope or exact family identity. |
| micro-native-ermes_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN nodes; empty native inventory is not biological completeness. Native success does not establish complete biological scope or exact family identity. |
| micro-emrky-independent-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/emrky-formation-attribution-challenge.json; Complete separate independent challenge, frozen inputs and actual source receipt bindings | supports | Independent reviewer corroborates rejection of the original blanket mandatory-UNKNOWN/isolated-proof major as formulated, while confirming the new narrow CPX attribution defect. No experimental necessity or dispensability certification and no automatic enum change. |
| plaque-curation | docs/CURATION.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-field-guide | docs/SCHEMA.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-protein-skill | .claude/skills/uniprot-protein-examples/SKILL.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-graph-skill | .claude/skills/curate-causal-graphs/SKILL.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-review-profile | docs/record-review-profile.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-review-contract | docs/record-reviews.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-review-schema | schema/record_review.yaml; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-structure-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-agents | AGENTS.md; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-review-config | conf/record_review.yaml; Frozen native policy/schema, including component-class identity, source applicability, formation versus function and append-only rationale | context_only | Apply current native contract without inventing mandatory examples, universal formation assays or a prohibition on broad protein groups. Preserve dated rationale; assess current claims separately. |
| plaque-record-4 | data/structures/other/escrt_0_complex.yaml; Complete current definition, components, taxa, examples, functions, graphs, discussions and history | supports | All maintained assertions read; current target bytes equal the original frozen target. No scientific record was changed. |
| plaque-original-4-yaml | reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.yaml; Complete immutable original, historical inputs/checks/evidence/findings/actions and exact rendered Markdown | context_only | Original scope and timestamp are historical. Source findings are independently reassessed at the present source head. |
| plaque-original-4-md | reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.md; Complete immutable original, historical inputs/checks/evidence/findings/actions and exact rendered Markdown | context_only | Original scope and timestamp are historical. Source findings are independently reassessed at the present source head. |
| plaque-record-5 | data/structures/other/escrt_complex.yaml; Complete current definition, components, taxa, examples, functions, graphs, discussions and history | supports | All maintained assertions read; current target bytes equal the original frozen target. No scientific record was changed. |
| plaque-original-5-yaml | reviews/structured/20261022T063722Z-escrt-complex-audit/review.yaml; Complete immutable original, historical inputs/checks/evidence/findings/actions and exact rendered Markdown | context_only | Original scope and timestamp are historical. Source findings are independently reassessed at the present source head. |
| plaque-original-5-md | reviews/structured/20261022T063722Z-escrt-complex-audit/review.md; Complete immutable original, historical inputs/checks/evidence/findings/actions and exact rendered Markdown | context_only | Original scope and timestamp are historical. Source findings are independently reassessed at the present source head. |
| plaque-record-6 | data/structures/other/escrt_i_complex.yaml; Complete current definition, components, taxa, examples, functions, graphs, discussions and history | supports | All maintained assertions read; current target bytes equal the original frozen target. No scientific record was changed. |
| plaque-original-6-yaml | reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.yaml; Complete immutable original, historical inputs/checks/evidence/findings/actions and exact rendered Markdown | context_only | Original scope and timestamp are historical. Source findings are independently reassessed at the present source head. |
| plaque-original-6-md | reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.md; Complete immutable original, historical inputs/checks/evidence/findings/actions and exact rendered Markdown | context_only | Original scope and timestamp are historical. Source findings are independently reassessed at the present source head. |
| plaque-input-original-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/input-original-proof.json; Actual explicit-commit proof;47 current source/worktree inputs,41 historical input occurrences and3 native original validate/render pairs | supports | All hashes match; own3 target hashes are nonstale. All3 original YAML files natively validate and exactly reproduce saved Markdown. Other cohort inputs are checked for provenance only. |
| plaque-native-escrt_0_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-verify-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-verify.log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Two reviewed protein_examples and two COVERED typed protein nodes. Identifier and node-coverage checks do not independently establish biological assembly, localization or necessity. |
| plaque-native-escrt_0_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-causal-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-causal.log; stdout SHA256 8d965b4762c6f13e759cf9a9f2c993dde6bd0f8922fe5998302d843e0f3efa5e | supports | Exit0. Two reviewed protein_examples and two COVERED typed protein nodes. Identifier and node-coverage checks do not independently establish biological assembly, localization or necessity. |
| plaque-native-escrt_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-verify-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-verify.log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Zero protein_examples and zero typed protein nodes; positive pathway assertions remain subject to source review. Identifier and node-coverage checks do not independently establish biological assembly, localization or necessity. |
| plaque-native-escrt_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-causal-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-causal.log; stdout SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Exit0. Zero protein_examples and zero typed protein nodes; positive pathway assertions remain subject to source review. Identifier and node-coverage checks do not independently establish biological assembly, localization or necessity. |
| plaque-native-escrt_i_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-verify-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-verify.log; stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Three reviewed protein_examples; four typed protein nodes comprise three COVERED constituents and the external Vps27 recruiter UNANCHORED_WITH_UNIPROT P40343. This intentional external actor is not a missing constituent. Identifier and node-coverage checks do not independently establish biological assembly, localization or necessity. |
| plaque-native-escrt_i_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-causal-receipt.json; Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-causal.log; stdout SHA256 aac6b7401b494f165148fbd63ff7a1fd22fde5cb5693ccd03f0e928f51a82f2e | supports | Exit0. Three reviewed protein_examples; four typed protein nodes comprise three COVERED constituents and the external Vps27 recruiter UNANCHORED_WITH_UNIPROT P40343. This intentional external actor is not a missing constituent. Identifier and node-coverage checks do not independently establish biological assembly, localization or necessity. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033565,GO:0036452,GO:0000813,GO:0005768,GO:0010008,GO:0032991,GO:0071985,GO:0000814,GO:0000815,GO:1990621; Complete10-term response: exact names/definitions/synonyms and selected typed children for all target, parent, localization, function and five child identities; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go.raw | supports | Current GO0033565 still says Vps1p while its exact synonym names Vps27p-Hse1p. Generic ESCRT has five distinct is_a child classes; the typed GO0005768 children confirm generic ESCRT part_of endosome, and GO0010008 confirms ESCRT-I part_of endosome membrane. GO0071985 defines MVB sorting; no direct parthood is inferred merely from an ancestor list. |
| plaque-go-0033565-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033565/ancestors?relations=is_a; Complete relations=is_a array for GO:0033565; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go-0033565-ancestors.raw | supports | The is_a-only ancestor response supports the target hierarchy; it supplies no independent direct parthood assertion. |
| plaque-go-0036452-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036452/ancestors?relations=is_a; Complete relations=is_a array for GO:0036452; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go-0036452-ancestors.raw | supports | The is_a-only ancestor response supports the target hierarchy; it supplies no independent direct parthood assertion. |
| plaque-go-0000813-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813/ancestors?relations=is_a; Complete relations=is_a array for GO:0000813; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go-0000813-ancestors.raw | supports | The is_a-only ancestor response supports the target hierarchy; it supplies no independent direct parthood assertion. |
| plaque-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native ENA response: ID/name/rank/lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/tax-4932.raw | supports | S. cerevisiae species4932 and S288C reference strain559292 are distinct from the SEY6210-derived experimental preparations. No quantitative prevalence census follows. |
| plaque-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native ENA response: ID/name/rank/lineage; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/tax-559292.raw | supports | S. cerevisiae species4932 and S288C reference strain559292 are distinct from the SEY6210-derived experimental preparations. No quantitative prevalence census follows. |
| plaque-pmid-12006563 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12006563+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:12006563 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-12006563.raw | supports | Stahelin2002 primary abstract concerns isolated yeast Vps27 and Drosophila Hrs FYVE-domain membrane binding, SPR and monolayer penetration; not whole-cell ESCRT assembly. |
| plaque-pmid-12055639 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12055639+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:12055639 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-12055639.raw | supports | Bilodeau2002 primary abstract explicitly identifies the yeast Vps27p/Hse1p complex, endosomal localization, Ub binding, Golgi recycling/lumenal-membrane function and UIM-mutant sorting separation. This directly contradicts the copied Vps1 constituent wording. |
| plaque-pmid-12900393 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12900393+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:12900393 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-12900393.raw | supports | Katzmann2003 primary abstract identifies Vps27-specific endosomal ESCRT-I recruitment; separately inspected body sections give the actual strain and assay scope. |
| plaque-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:14562095 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-14562095.raw | supports | Huh2003 primary abstract describes tagged-yeast protein localization survey. Individual images were not inspected; exact annotation provenance is checked in native UniProt instead. |
| plaque-pmid-21763610 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21763610+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:21763610 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-21763610.raw | supports | Henne2011 is a secondary review. Its complete abstract supports the broad cargo-recognition/membrane-sculpting framework, MVB biogenesis, retroviral budding and cytokinetic abscission; it does not certify detailed main-body subunit mechanisms. |
| plaque-pmid-11511343 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11511343+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:11511343 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-11511343.raw | supports | Katzmann2001 primary abstract identifies the original Vps23/Vps28/Vps37 yeast core and a reported350kDa complex. This is historically scoped apparent-complex characterization, not modern exhaustive composition or an exact physical copy-number claim. |
| plaque-pmid-9790597 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9790597+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:9790597 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-9790597.raw | supports | Hong1998 primary abstract identifies Srn10/Srn2 suppressor and cytoplasmic localization by immunofluorescence. Viability dispensability is not identical to ESCRT-I assembly necessity. |
| plaque-pmid-17145965 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17145965+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:17145965 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-17145965.raw | supports | Chu2006 primary abstract positively identifies Mvb12 and assembly-regulation context; selected body sections below independently confirm membership and experimental strains. |
| plaque-pmid-17135292 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17135292+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact EXT_ID:17135292 AND SRC:MED; pageSize1/resultType core; full unique returned bibliography and abstract only, not linked body; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-17135292.raw | supports | Curtiss2007 primary abstract positively identifies Mvb12 and its association/sorting/release functions; selected body sections below bound the physical evidence. |
| plaque-bilodeau-publisher | https://www.nature.com/articles/ncb815; Publisher title/authors/DOI, complete Abstract, access notice and section headings; no Results/Methods or pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/bilodeau-publisher.raw | supports | The current Nature page exposes a genuine abstract and bibliography, followed by a subscription-preview notice. It is not the historical challenge response and does not grant full-body access. |
| plaque-henne-publisher | https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00240-3; Actual HTTP403 transport response and adjacent receipt only; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/henne-publisher.raw | context_only | The attempted publisher fulltext route returned403. No Henne main-body reading is claimed; the exact native MED abstract is separate secondary evidence. |
| plaque-PMC2172707-body | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2172707/; Genuine NCBI legacy HTML; Abstract, Results sec3–7, Discussion sec9–10, Methods sec12–15; embedded text captions Figs1–7. SEY6210 and explicit derivatives; no figure pixels or raw experiments reanalysed.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/PMC2172707-body.raw | supports | Katzmann2003 supports independent Ub binding, Vps27/PI3P-dependent ESCRT-I recruitment, membrane-specific reciprocal association and C-terminal recruitment defects. Hse1-dependent whole-complex recruitment is not substituted for the specifically tested Vps27 actor. Discussion distinguishes model proposals from measured interactions and labels selected observations unpublished. |
| plaque-PMC2064680-body | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2064680/; Genuine NCBI legacy HTML; Abstract, Results sec3 with Figs1/2 text captions; Methods sec9/11/13. Other oligomer-model Results/Discussion, supplemental alignment and pixels not inspected.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/PMC2064680-body.raw | supports | Chu2006 gel filtration/co-IP identify Mvb12 as an additional ESCRT-I member; partial cargo-sorting defects differ from core deletions. The current record acknowledges this later member. SEY6210-derived assays and recombinant E.coli production are distinct; expression host is not the natural record taxon. |
| plaque-PMC1783790-body | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1783790/; Genuine NCBI legacy HTML; Abstract, Methods sec4/Table1 and sec6, Results sec10–11 with embedded Figs2/3/4/7 text captions. Specific SEY6210 derivatives and control strains read; no figure pixels, supplement or complete other Results certified.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/PMC1783790-body.raw | supports | Curtiss2007 reciprocal purification and gel filtration support Mvb12 membership. In vps37 deletion, a Vps23/Vps28 subcomplex persists while Mvb12 becomes unstable and fails to associate in the tested assays; localization/sorting and individual universal formation necessity remain separate. Apparent gel-filtration masses are not exact stoichiometry. |
| plaque-up-P40343 | https://rest.uniprot.org/uniprotkb/P40343.json; Native primaryAccession, entryType, genes/locus/taxon, comments and family cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-P40343.raw | supports | Reviewed S288C559292 P40343 has primary gene VPS27, matching VPS27 name/alias and locus YNR006W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family cross-references were inspected. Native annotation provenance is distinguished from fresh primary experiments and reference strain from assay strains. |
| plaque-gene-VPS27 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-result response; no identity inferred from search rank; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS27.raw | supports | Exactly one reviewed S288C result matches P40343, with correct primary name, aliases and locus. |
| plaque-up-P38753 | https://rest.uniprot.org/uniprotkb/P38753.json; Native primaryAccession, entryType, genes/locus/taxon, comments and family cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-P38753.raw | supports | Reviewed S288C559292 P38753 has primary gene HSE1, matching HSE1 name/alias and locus YHL002W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family cross-references were inspected. Native annotation provenance is distinguished from fresh primary experiments and reference strain from assay strains. |
| plaque-gene-HSE1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHSE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-result response; no identity inferred from search rank; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-HSE1.raw | supports | Exactly one reviewed S288C result matches P38753, with correct primary name, aliases and locus. |
| plaque-up-P25604 | https://rest.uniprot.org/uniprotkb/P25604.json; Native primaryAccession, entryType, genes/locus/taxon, comments and family cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-P25604.raw | supports | Reviewed S288C559292 P25604 has primary gene STP22, matching VPS23 name/alias and locus YCL008C. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family cross-references were inspected. Native annotation provenance is distinguished from fresh primary experiments and reference strain from assay strains. |
| plaque-gene-VPS23 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS23%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-result response; no identity inferred from search rank; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS23.raw | supports | Exactly one reviewed S288C result matches P25604, with correct primary name, aliases and locus. |
| plaque-up-Q02767 | https://rest.uniprot.org/uniprotkb/Q02767.json; Native primaryAccession, entryType, genes/locus/taxon, comments and family cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-Q02767.raw | supports | Reviewed S288C559292 Q02767 has primary gene VPS28, matching VPS28 name/alias and locus YPL065W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family cross-references were inspected. Native annotation provenance is distinguished from fresh primary experiments and reference strain from assay strains. |
| plaque-gene-VPS28 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS28%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-result response; no identity inferred from search rank; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS28.raw | supports | Exactly one reviewed S288C result matches Q02767, with correct primary name, aliases and locus. |
| plaque-up-Q99176 | https://rest.uniprot.org/uniprotkb/Q99176.json; Native primaryAccession, entryType, genes/locus/taxon, comments and family cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-Q99176.raw | supports | Reviewed S288C559292 Q99176 has primary gene SRN2, matching VPS37 name/alias and locus YLR119W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family cross-references were inspected. Native annotation provenance is distinguished from fresh primary experiments and reference strain from assay strains. |
| plaque-gene-VPS37 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS37%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-result response; no identity inferred from search rank; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS37.raw | supports | Exactly one reviewed S288C result matches Q99176, with correct primary name, aliases and locus. |
| plaque-ipr-IPR017073 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017073/; Complete native InterPro accession/type/name/member signatures/hierarchy and description flags; full-protein membership joined to native UniProt where claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR017073.raw | supports | Whole Hrs/Vps27 protein family, not the shared VHS/FYVE/UIM domains. Current native P40343 independently carries the exact cross-reference. |
| plaque-ipr-IPR050670 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050670/; Complete native InterPro accession/type/name/member signatures/hierarchy and description flags; full-protein membership joined to native UniProt where claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR050670.raw | supports | STAM-labelled family integrates PTHR45929 but generated unchecked narrative is excluded; actual reviewed membership includes other named protein classes, so it is not forced as exact Hse1/STAM-only grounding. |
| plaque-ipr-IPR052070 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052070/; Complete native InterPro accession/type/name/member signatures/hierarchy and description flags; full-protein membership joined to native UniProt where claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR052070.raw | supports | Typed family with PTHR23306 despite the UEV-domain-containing label. Unchecked generated text is excluded; native P25604 and bounded seven-member reviewed query establish the Vps23/TSG101 class. |
| plaque-ipr-IPR007143 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007143/; Complete native InterPro accession/type/name/member signatures/hierarchy and description flags; full-protein membership joined to native UniProt where claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR007143.raw | supports | Vps28 full-protein family with PTHR12937/PIRSF017535/PF03997 and native Q02767 match. Its older three-member prose is not used to deny Mvb12. |
| plaque-ipr-IPR017435 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017435/; Complete native InterPro accession/type/name/member signatures/hierarchy and description flags; full-protein membership joined to native UniProt where claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR017435.raw | supports | Fungal Vps37 family with PIRSF038214 and Q99176 membership matches the explicitly yeast component. It is not advertised as encompassing all metazoan paralogs; internally inconsistent heterotrimer/four-name prose is not stoichiometry evidence. |
| plaque-ipr-IPR009851 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009851/; Complete native InterPro accession/type/name/member signatures/hierarchy and description flags; full-protein membership joined to native UniProt where claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR009851.raw | supports | Modr/Vps37 C-terminal domain; not an exact whole Vps37 family substitute. |
| plaque-panther-PTHR45929 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/; Native name/integration/member metadata and LLM flags; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/panther-PTHR45929.raw | context_only | Broad STAM family metadata does not override the independently observed mixed reviewed-member boundary. Unchecked generated narrative is excluded. |
| plaque-members-IPR050670 | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR050670/?page_size=200; Complete38 metadata identities, next=null; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/members-IPR050670.raw | context_only | All38 reviewed returned members include Hse1/STAM but also SHO1, LSB1, PIN3, csh3, mug137 and SH3D21 identities. This establishes a broader returned boundary, not a proposed exact Hse1 class. |
| plaque-members-IPR052070 | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR052070/?page_size=200; Actual HTTP429 response/receipt only; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/members-IPR052070.raw | context_only | The InterPro reviewed-members endpoint returned429; no identity or absence finding rests on that transport response. A separate bounded UniProt query succeeds. |
| plaque-family-query-IPR052070 | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR052070%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id&amp;size=500; All7 accession/name/gene/taxon rows; no next-page link; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/family-query-IPR052070.raw | supports | All7 reviewed returned entries are Vps23/TSG101/ELC homolog identities: Q99816,P25604,Q61187,Q6IRE4,Q9LHG8,Q54LJ3,Q9FFY6. This supports class scope independently of unchecked family prose. |
| plaque-catalogue | https://imodulondb.org/api/datasets; All20 organism rows/28 organism-dataset pairs independently reread from same-PR micro snapshot; actual original fetch time retained; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/catalogue.raw | context_only | Complete current catalogue contains no Saccharomyces, S288C, SEY6210 or mammalian natural-host dataset. No matching downstream gene/module dataset was selected and recombinant E.coli is not used as a proxy. This is bounded catalogue noncoverage, not absence of ESCRT biology. |
| plaque-historical-4-micro54-panther-PTHR45929-subfamilies | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/?extra_fields=subfamilies; Original request/response diagnostic only. Historical row from 20261022T063722Z-escrt-0-complex-audit/micro54-panther-PTHR45929-subfamilies; old time/hash retained from immutable original YAML; original raw transport response not independently reconstructed. | context_only | The attempted extra_fields=subfamilies request returned HTTP404 and establishes no exact subfamily identity. |
| plaque-historical-4-micro54-bilodeau2002-publisher | https://www.nature.com/articles/ncb815; Retained3038-byte challenge HTML and original access receipt. Historical row from 20261022T063722Z-escrt-0-complex-audit/micro54-bilodeau2002-publisher; old time/hash retained from immutable original YAML; original raw transport response not independently reconstructed. | context_only | The native Nature route returned HTTP200 with a Client Challenge page, not the Bilodeau main body. The complete primary abstract is independently available in the native MED entry. |
| plaque-historical-4-micro54-henne2011-citeseer | https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&amp;repid=rep1&amp;type=pdf; Retained native request and404 response. Historical row from 20261022T063722Z-escrt-0-complex-audit/micro54-henne2011-citeseer; old time/hash retained from immutable original YAML; original raw transport response not independently reconstructed. | context_only | The candidate public PDF URL returned HTTP404 HTML, not the Henne review. No main-body scope is inferred. |
| plaque-historical-5-micro54-henne2011-citeseer | https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&amp;repid=rep1&amp;type=pdf; Original request and response diagnostic; not a main body. Historical row from 20261022T063722Z-escrt-complex-audit/micro54-henne2011-citeseer; old time/hash retained from immutable original YAML; original raw transport response not independently reconstructed. | context_only | The candidate public Henne PDF route returned HTTP404 HTML. The actual review reading remains limited to the complete native abstract. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Complete review and structured-source policy | supports | Positive molecular and pathway assertions trigger actual host coverage assessment; absence of expression-module claims is insufficient. |
| septin-curation-policy | docs/CURATION.md; Exact family/class grounding and append-only discussions | supports | Exact whole-component identities differ from domains or broad paralog groups; label-only is valid while the specific class is unresolved. Preserve dated rationale and history. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component, essentiality, taxonomic and graph types | supports | Functional requirement, localization, membership and formation necessity are distinct. Optional fields and valid family/class components are not automatic defects. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Primary names, synonyms, exact taxon and identity checks | supports | Accessions, reference strains and gene aliases require native authority joins; they do not establish an experimental assembly mechanism. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope and evidence rules | supports | Coarse function graphs are valid when explicitly nonmechanistic; avoid promoting targeting or fragment models into a universal complete assembly mechanism. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Source accessibility and precise read extent | supports | Native metadata, complete primary abstracts, genuine primary bodies and secondary syntheses are different evidence tiers; captions are not image pixels. |
| septin-review-schema | schema/record_review.yaml; Evidence, findings and lineage contract | supports | Keep inherited stable keys with exact repository/review/finding identity and actual current evidence; a supported qualified pass remains scope limited. |
| septin-yang2010-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3124813/fullTextXML; Actual returned HTTP status/body and access barrier, not scientific text | context_only | Bounded current access attempt: HTTP500 endpoint error. This packet cannot certify a primary body; independent successful or abstract evidence is separately listed. |
| septin-yang2010-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC3124813/?pdf=1; Genuine PMC3124813 Results S3–S6 and Discussion S7; Tables1/2 and main Fig1–7 captions; Methods S9/S12/S13, no S10/S11 crystallographic-method or coordinate reanalysis | supports | Yeast Vta1-VSL/Vps4-SAB fragment crystal interface, SPR mutations and Cps1 sorting are directly measured. The proposed planar Vps4 arrays remain explicitly speculative. Recombinant BL21/Rosetta2 expression is distinct from Open Biosystems yeast deletion assays; exact experimental reference-strain equivalence is not established. |
| septin-hierro2004-publisher | https://www.nature.com/articles/nature02914; Publisher title/authors and complete displayed abstract; explicit subscription-preview boundary | supports | The current reachable abstract describes a Y-shaped yeast core with Vps22, two Vps25 copies and C-terminal Vps36. The page exposes an abstract/preview, not full scientific body; historical client challenge is not represented as a new result. |
| septin-babst2002-publisher | https://www.sciencedirect.com/science/article/pii/S1534580702002204; Actual returned HTTP status/body and access barrier, not scientific text | context_only | Bounded current access attempt: HTTP403 publisher block. This packet cannot certify a primary body; independent successful or abstract evidence is separately listed. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621; Complete requested terms; assigned active names/definitions/synonyms and typed child relationships only | supports | ESCRT-II/III/IV identities and parent class are exact. Endosome-membrane part_of differs from is_a ESCRT. GO II recruitment wording is interpreted as complex activation, not mandatory localization of every Vps20 molecule. General III remodeling definition and IV ATP-driven recycling remain broader than the yeast experimental example. |
| septin-GO0000814-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000814/ancestors?relations=is_a; Complete is_a-only ancestor closure | supports | Exact ESCRT parent is present; this query does not establish a parthood relation. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxonomy response | supports | Saccharomyces cerevisiae, rank species. Species and reference strain differ from recombinant expression hosts and exact experimental strain identities. |
| septin-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxonomy response | supports | Saccharomyces cerevisiae S288C, rank strain. Species and reference strain differ from recombinant expression hosts and exact experimental strain identities. |
| septin-protein-P47142 | https://rest.uniprot.org/uniprotkb/P47142.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed P47142: Vacuolar protein-sorting-associated protein 25; primary VPS25; synonyms ['VPT25']; ordered loci ['YJR102C']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-protein-Q06696 | https://rest.uniprot.org/uniprotkb/Q06696.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed Q06696: Vacuolar protein-sorting-associated protein 36; primary VPS36; synonyms ['GRD12', 'VAC3', 'VPL11']; ordered loci ['YLR417W']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-protein-Q12483 | https://rest.uniprot.org/uniprotkb/Q12483.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed Q12483: Vacuolar-sorting protein SNF8; primary SNF8; synonyms ['VPS22']; ordered loci ['YPL002C']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-gene-VPS22-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS22%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry Q12483 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-gene-VPS25-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS25%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry P47142 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-gene-VPS36-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS36%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry Q06696 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-pmid-12194858 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194858+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Endosome-associated complex, ESCRT-II, recruits transport machinery for protein sorting at the multivesicular body. Authors Babst M, Katzmann DJ, Snyder WB, Wendland B, Emr SD. DOI 10.1016/s1534-5807(02)00219-8. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-doi-j_devcel_2004_09_003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2004.09.003%22&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation ESCRT-II, an endosome-associated complex required for protein sorting: crystal structure and interactions with ESCRT-III and membranes. Authors Teo H, Perisic O, González B, Williams RL. DOI 10.1016/j.devcel.2004.09.003. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-doi-j_devcel_2008_04_004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2008.04.004%22&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Integrated structural model and membrane targeting mechanism of the human ESCRT-II complex. Authors Im YJ, Hurley JH. DOI 10.1016/j.devcel.2008.04.004. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-doi-j_devcel_2009_07_008 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2009.07.008%22&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Structure and function of the ESCRT-II-III interface in multivesicular body biogenesis. Authors Im YJ, Wollert T, Boura E, Hurley JH. DOI 10.1016/j.devcel.2009.07.008. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-doi-nature02914 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature02914%22&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Structure of the ESCRT-II endosomal trafficking complex. Authors Hierro A, Sun J, Rusnak AS, Kim J, Prag G, Emr SD, Hurley JH. DOI 10.1038/nature02914. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-doi-science_1161070 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1161070%22&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Helical structures of ESCRT-III are disassembled by VPS4. Authors Lata S, Schoehn G, Jain A, Pires R, Piehler J, Gottlinger HG, Weissenhorn W. DOI 10.1126/science.1161070. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-teo2004-primary-pdf | https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf; Printed p559 summary/Introduction; p564–567 direct-interaction/liposome Results, Fig4/5/6 caption text, Conclusions and plasmid/expression/purification/pull-down Methods. Other crystallographic Results/Methods not independently used. | supports | Teo2004 resolves the yeast core with one Vps22, two Vps25 and truncated Vps36; purified ESCRT-II and isolated Vps25 bind Vps20 directly and enhance liposome binding. Removal of Vps22 residues1–40 or Vps36 residues1–370 does not abolish the Vps20 interaction. ATCC9763D yeast genomic material was expressed in C41(DE3)/B834(DE3); this is recombinant yeast anatomy, not native bacterial ESCRT. Freshly retrieved and independently read in this review; no figure pixels or supplementary experiments certified. |
| septin-primary-PMC2475506 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2475506/; Results S4/S6/S7 with Fig4/5 captions; Methods S10/S16; complete native abstract supplies structural stoichiometry. No figure pixels or supplement files. | supports | Im/Hurley2008 examines human recombinant complexes and yeast BY4741-derived sorting/localization mutants. GLUE/Vps22-H0 jointly contribute to membrane targeting; the pseudo-intact liposome construct lacks VPS25-WH2. Its membrane-binding defects are not whole-complex formation experiments. Freshly retrieved and independently read in this review; no figure pixels or supplementary experiments certified. |
| septin-primary-PMC2749878 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2749878/; Results S2/S5/S6/S7/S8, Discussion S10; Methods S12/S16/S17/S18/S20, Table1/Fig1–4 captions. No pixels or supplements. | supports | Im2009 directly activates yeast ESCRT-III budding/scission with ESCRT-II in synthetic GUV assays; VPS25/VPS20 interface mutants fail in activation and yeast cargo sorting. Strong Vps20 membrane binding is distinguished from complex activation. Freshly retrieved and independently read in this review; no figure pixels or supplementary experiments certified. |
| septin-primary-PMC2758909 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2758909/; Complete main scientific text S1 and Fig1–4 captions; supplementary Methods/data and pixels not independently read. | supports | Lata2008 directly observes ATP/Mg-dependent VPS4B disassembly of engineered CHMP2A/CHMP3 tubes. This supports the disassembly principle while retaining human-protein/truncation context and a proposed rather than directly observed final scission model. Freshly retrieved and independently read in this review; no figure pixels or supplementary experiments certified. |
| septin-ipr-IPR016689 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016689/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR016689 identifies the complete Snf8/Vps22 family, with exact PIRSF017215/PTHR12806 signatures; its hierarchy separates it from Vps36 under the broader Snf8/Vps36 parent. Current independent authority/protein joins reconfirm the stated scope. |
| septin-ipr-IPR008570 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008570/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR008570 identifies the complete Vps25 family with PF05871/PTHR13149 signatures. Its incidental Vps35 wording is not adopted as an interaction claim. Current independent authority/protein joins reconfirm the stated scope. |
| septin-ipr-IPR037855 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037855/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR037855 identifies Vps36 with PTHR13128, distinct from its GLUE/NZF domains and from sister Snf8/Vps22. Current independent authority/protein joins reconfirm the stated scope. |
| septin-GO0000815-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000815/ancestors?relations=is_a; Complete is_a-only ancestor closure | supports | Exact ESCRT parent is present; this query does not establish a parthood relation. |
| septin-protein-P36095 | https://rest.uniprot.org/uniprotkb/P36095.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed P36095: Vacuolar protein-sorting-associated protein 24; primary VPS24; synonyms ['DID3']; ordered loci ['YKL041W']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-protein-P36108 | https://rest.uniprot.org/uniprotkb/P36108.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed P36108: DOA4-independent degradation protein 4; primary DID4; synonyms ['CHM2', 'GRD7', 'REN1', 'VPL2', 'VPS2', 'VPT14']; ordered loci ['YKL002W']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-protein-P39929 | https://rest.uniprot.org/uniprotkb/P39929.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed P39929: Vacuolar-sorting protein SNF7; primary SNF7; synonyms ['DID1', 'VPS32']; ordered loci ['YLR025W']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-protein-Q04272 | https://rest.uniprot.org/uniprotkb/Q04272.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed Q04272: Vacuolar protein sorting-associated protein 20; primary VPS20; synonyms ['ASI10', 'CHM6', 'VPT20']; ordered loci ['YMR077C']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-gene-VPS20-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry Q04272 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-gene-SNF7-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASNF7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry P39929 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-gene-VPS24-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS24%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry P36095 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-gene-VPS2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry P36108 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-pmid-12194857 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194857+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Authors Babst M, Katzmann DJ, Estepa-Sabal EJ, Meerloo T, Emr SD. DOI 10.1016/s1534-5807(02)00220-4. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-pmid-24139821 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24139821+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Essential N-terminal insertion motif anchors the ESCRT-III filament during MVB vesicle formation. Authors Buchkovich NJ, Henne WM, Tang S, Emr SD. DOI 10.1016/j.devcel.2013.09.009. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-pmid-25303532 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25303532+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Surveillance of nuclear pore complex assembly by ESCRT-III/Vps4. Authors Webster BM, Colombi P, Jäger J, Lusk CP. DOI 10.1016/j.cell.2014.09.012. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-ipr-IPR005024 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005024/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR005024 is the broad Snf7-like family covering multiple CHMP paralogs, yeast Did4/Did2 and archaeal CdvB. Its PTHR10476/PTHR22761/PF03357 signatures do not distinguish each of the four named yeast constituents. Current independent authority/protein joins reconfirm the stated scope. |
| septin-GO1990621-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990621/ancestors?relations=is_a; Complete is_a-only ancestor closure | supports | Exact ESCRT parent is present; this query does not establish a parthood relation. |
| septin-protein-P52917 | https://rest.uniprot.org/uniprotkb/P52917.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed P52917: Vacuolar protein sorting-associated protein 4; primary VPS4; synonyms ['CSC1', 'DID6', 'END13', 'GRD13', 'VPL4', 'VPT10']; ordered loci ['YPR173C']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-protein-Q06263 | https://rest.uniprot.org/uniprotkb/Q06263.json; Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments, cited evidence and family xrefs | supports | Reviewed Q06263: Vacuolar protein sorting-associated protein VTA1; primary VTA1; synonyms []; ordered loci ['YLR181C']; taxon 559292. Native annotation evidence is not an independently repeated experiment. Exact family membership joins checked separately from the family-entry definition. |
| septin-gene-VPS4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry P52917 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-gene-VTA1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVTA1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned reviewed native result, primary names, synonyms and taxon | supports | One current reviewed entry Q06263 for the declared gene query; primary-name versus alias distinctions are preserved. This does not reconstruct an unspecified historical query. |
| septin-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Global analysis of protein localization in budding yeast. Authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. DOI 10.1038/nature02026. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-pmid-14701806 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14701806+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Characterization of Vta1p, a class E Vps protein in Saccharomyces cerevisiae. Authors Shiflett SL, Ward DM, Huynh D, Vaughn MB, Simmons JC, Kaplan J. DOI 10.1074/jbc.m312669200. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-pmid-20696398 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20696398+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native EuropePMC CORE citation and abstractText | supports | Exact citation Structural role of the Vps4-Vta1 interface in ESCRT-III recycling. Authors Yang D, Hurley JH. DOI 10.1016/j.str.2010.04.014. Complete primary abstract inspected; this evidence row alone does not certify full text. Native UniProt localization-reference joins are retained as annotations, not atlas reanalysis. |
| septin-primary-PMC3124813 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3124813/; Actual returned HTTP status/body and access barrier, not scientific text | context_only | Bounded current access attempt: HTTP200 browser challenge. This packet cannot certify a primary body; independent successful or abstract evidence is separately listed. |
| septin-ipr-IPR044538 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044538/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR044538 is the Vta1-like full protein family, explicitly including yeast Vta1 and animal/plant homologs. PTHR46009 identifies the constituent class rather than only its VSL or MIT domain. Current independent authority/protein joins reconfirm the stated scope. |
| septin-ipr-IPR045253 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045253/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR045253 is only the Vps4 MIT domain; it does not identify the complete ATPase constituent. Current independent authority/protein joins reconfirm the stated scope. |
| septin-ipr-IPR050304 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050304/; Current native name/type, complete descriptions and curation flags, member signatures, hierarchy and overlap fields; separate member accession join | supports | IPR050304 is the broader microtubule-severing AAA ATPase family with PTHR23074. Its LLM-generated unchecked prose is not primary functional evidence and does not establish exact Vps4 specificity. Current response independently read; unchecked LLM prose is excluded from scientific support. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete unpaginated official catalogue: all20 organism rows and advertised dataset keys | supports | No Saccharomyces cerevisiae or human host appears. Bacterial expression hosts for recombinant yeast proteins are not substitutes for the biological complex host. Host noncoverage is not biological absence. |
| septin-henne2011-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21763610+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete native bibliographic identity and secondary-review abstract | supports | Henne, Buchkovich and Emr2011 is a secondary review of cargo recognition, membrane sculpting, MVBs and related pathways. Only its complete abstract and citation are inspected; no detailed review-body mechanism certified. |
| septin-henne2011-access | https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00240-3; Actual current publisher403 access response | context_only | Publisher route returned a challenge/403, not a primary or secondary scientific body. Missing access is not refutation. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical Nov3 00:49Z command receipt | context_only | Actual prior exit1 PermissionError reading runner pyvenv.cfg; no current invocation claimed. Current official catalogue fallback is separate evidence. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-septin/original-checks.json; Three actual native validate/render pairs and39 historical input occurrences | supports | All three original YAML documents validate0 and render0 to exact original Markdown. All39 input occurrences match their frozen Git source, and all three current targets are unchanged. |
| septin-record-escrt_ii_complex | data/structures/other/escrt_ii_complex.yaml; Entire current maintained record including all history, discussions, examples, functions and graph edges | context_only | Current target read in full; unchanged from original frozen input. Historical rationale is provenance, not a new scientific experiment. |
| septin-original-escrt_ii_complex | reviews/structured/20261022T063724Z-escrt-ii-complex-audit/review.yaml; Complete original YAML and deterministic Markdown, all evidence/checks/findings/actions/limitations | context_only | Original scientific scopes, exact predecessor identities and formal expression-only exclusion inspected; historical failed-access limitations are not relabeled as current successful source reads. No own original access-only evidence-kind defect established. |
| septin-native-escrt_ii_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-verify-receipt.json; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-verify.log; receipt SHA256 f40096c949e6b2183128d4a256b5e662941df0b775ae3533505ebe5cd7f8ad2d | supports | 3 reviewed examples and 3 COVERED typed component nodes; identity/coverage validation does not establish scientific membership or formation necessity. |
| septin-native-escrt_ii_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-causal-receipt.json; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-causal.log; receipt SHA256 6021ed5e78399e7c10d736a4e6bda9eedcc4c534ebc7cf3c50b9316318a43f4f | supports | 3 reviewed examples and 3 COVERED typed component nodes; identity/coverage validation does not establish scientific membership or formation necessity. |
| septin-record-escrt_iii_complex | data/structures/other/escrt_iii_complex.yaml; Entire current maintained record including all history, discussions, examples, functions and graph edges | context_only | Current target read in full; unchanged from original frozen input. Historical rationale is provenance, not a new scientific experiment. |
| septin-original-escrt_iii_complex | reviews/structured/20261022T063725Z-escrt-iii-complex-audit/review.yaml; Complete original YAML and deterministic Markdown, all evidence/checks/findings/actions/limitations | context_only | Original scientific scopes, exact predecessor identities and formal expression-only exclusion inspected; historical failed-access limitations are not relabeled as current successful source reads. No own original access-only evidence-kind defect established. |
| septin-native-escrt_iii_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iii_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-verify-receipt.json; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-verify.log; receipt SHA256 1eebb5dffcec704661a1a721540193a5b432a7fe8662cac2e298b7dd11cea5a5 | supports | 4 reviewed examples and 4 COVERED typed component nodes; identity/coverage validation does not establish scientific membership or formation necessity. |
| septin-native-escrt_iii_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iii_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-causal-receipt.json; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-causal.log; receipt SHA256 749aecb1980db6082b235e896f87f0ef19633be41ad5dbeaa2c03f9932ec2b3c | supports | 4 reviewed examples and 4 COVERED typed component nodes; identity/coverage validation does not establish scientific membership or formation necessity. |
| septin-record-escrt_iv_complex | data/structures/other/escrt_iv_complex.yaml; Entire current maintained record including all history, discussions, examples, functions and graph edges | context_only | Current target read in full; unchanged from original frozen input. Historical rationale is provenance, not a new scientific experiment. |
| septin-original-escrt_iv_complex | reviews/structured/20261022T063726Z-escrt-iv-complex-audit/review.yaml; Complete original YAML and deterministic Markdown, all evidence/checks/findings/actions/limitations | context_only | Original scientific scopes, exact predecessor identities and formal expression-only exclusion inspected; historical failed-access limitations are not relabeled as current successful source reads. No own original access-only evidence-kind defect established. |
| septin-native-escrt_iv_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iv_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-verify-receipt.json; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-verify.log; receipt SHA256 16f87c2eec5baafa61d58b602705a34626ee06ececdf5f8e01d2a8f2d603d793 | supports | 2 reviewed examples and 2 COVERED typed component nodes; identity/coverage validation does not establish scientific membership or formation necessity. |
| septin-native-escrt_iv_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iv_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-causal-receipt.json; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-causal.log; receipt SHA256 b34de9d2d3e66cc973d94cf09dc4c82bd0e96b9e73703b007cab0d4e8490ae2d | supports | 2 reviewed examples and 2 COVERED typed component nodes; identity/coverage validation does not establish scientific membership or formation necessity. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2391 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-endoplasmic_reticulum_sec_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-endoplasmic_reticulum_sec_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-epsilon_dna_polymerase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-epsilon_dna_polymerase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ermes_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ermes_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_0_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_0_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_i_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_i_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_ii_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_ii_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_iii_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_iii_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_iv_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-escrt_iv_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Own scientific scope is four complete current EmrKY-TolC, ER Sec, Pol-epsilon and ERMES records. EmrKY is the sole stale own target. All29 used local inputs were frozen before use and match the source; no extra maintained neighbor was read. Originals are immutable.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: EmrKY: actual complete native CPX4273 and ECO authority, reviewed protein annotations and May primary Methods2/7 plus Results14/15 were read. Curator inference, by-similarity annotations, null EmrK/EmrY counts, TolC3 and multi-locus/TetA(C) experimental confounds are retained. No isolated constituent necessity assay, direct full pump architecture or universal dispensability is certified.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: ER Sec: Panzner remains complete indexed primary abstract only after publisher redirect/block; Plath genuine Methods/Results and Wu declared main/method/caption scopes were read. BY4741 source, limited Sec62 density/model coverage, initial binding versus Kar2-coupled translocation and parent/subcomplex representation remain distinct. No direct individual-protein inventory or optional example is forced.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Pol-epsilon: Chilkova remains complete indexed abstract after correct publisher PDF route403; Asturias is indexed/publisher abstract tier, not body. Ohya actual mutant-purification and Ganai declared biochemical sections were read. Reference S288C, W303/CG379/CB001 and Py116 preparations are not conflated. Localization annotations and Huh abstract do not certify unread supplement rows. Secondary PMID15814431/9745046 reviews are not primary experiments.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Pol-epsilon exact family mappings use native metadata, reference xrefs and the complete15-member IPR051377 reviewed list. LLM-flagged family description is excluded as primary biological support. Broad histone-fold/transcription-related families do not resolve exact Dpb3. Shared-complex membership does not invalidate a homologous family.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: ERMES: Kornmann main text/captions and Kawano declared Introduction/Results/Discussion/strain/lipid-assay sections were read. No SupplementaryMethods, images, movies or coordinates were inspected. K.lactis recombinant Mmm1-Mdm12, yeast mutant heavy-membrane fractions and full in-vivo ERMES transfer remain separate. No peripheral-factor inventory, exact copy count or universal ESSENTIAL is imposed.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Official catalogue has20 organisms/28 organism-dataset pairs and no Saccharomyces match. E.coli precise1k is a five-strain dataset: BW25113,DGF-298,GMOS,MG1655,W3110. All201 memberships were checked for three native loci. EmrK/EmrY hit EvgA38 with15 members; TolC hits SoxS22 with117 members; complete selected module IDs/weights/native accession joins verified. No AI summaries or activity vectors used; expression context and nonhits do not prove assembly, causal regulation or absence.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Historical runner failure remains the actual Nov3 00:49Z PermissionError receipt, not a new invocation. Current failed/redirect/rate-limit routes are access diagnostics only; successful body/authority retries are separate. An initial guessed Chilkova PII was unverified and is not cited as evidence for that paper; the DOI-derived correct PII route also failed. Sandbox DNS attempts were retained separately and are not scientific sources.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Eight actual current native protein commands pass with7 reviewed examples/7 COVERED typed protein nodes; Sec and ERMES inventories are empty. Eight original native validate/render commands and56 historical input occurrences pass. No future successor/post-save/CI/queue certification is made; root owns global gates.
- EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Current finding disposition is three inherited minor/open findings plus one new minor CPX-attribution finding, and one inherited major explicitly rejected with exact lineage/no action. Rejection does not claim record edits or measured necessity. All four open actions are bounded future curation, preserve append-only history and avoid mandatory new experiments. No related/group/category issue is terminally resolved by inference.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Bilodeau2002, Stahelin2002, Huh2003, Katzmann2001 and Hong1998 are read at complete primary abstract/metadata tier only. The current Bilodeau Nature page exposes abstract/subscription preview; no full body or individual localization images are certified.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Henne2011 remains secondary complete-abstract context. A publisher route returned403; the author publication page does not supply an independently inspected body of this exact paper. No detailed Henne main-body passage or figure reading is claimed.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Katzmann2003 selected Results3–7, Discussion9–10, Methods12–15 and text captions were read from genuine primary HTML. Chu2006 and Curtiss2007 are restricted to the explicitly enumerated membership/strain/association sections. No source figure pixels, supplemental experiments or raw measurements were independently reanalysed.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: S288C reference protein identities differ from SEY6210 experimental derivatives. COMMON is a qualitative native taxonomic assertion, not an independently measured population census. Recombinant E.coli is not a natural-host proxy.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Exact Hrs/Vps27, Vps23/TSG101, Vps28 and fungal Vps37 mappings are supported by native family types, signatures and protein joins. Generated unchecked family prose and contradictory old composition descriptions are excluded. Hse1 mixed-family scope remains unresolved; no exact class is forced.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: The InterPro IPR052070 member endpoint returned429, but a separate current bounded UniProt reviewed-member query returned7 matching identities. Negative access is not negative biology; no evolutionary exhaustiveness or unreviewed-member survey is claimed.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: The current catalogue fallback is distinct from the historical runner-unavailable observation at2026-11-03 00:49Z. No fresh runner execution is claimed. Complete catalogue noncoverage precludes a justified same-host downstream dataset; it does not establish absence of the biology.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Four corrected historical access rows preserve original URLs, timestamps, hashes and context_only disclosures from the immutable originals. Historical transport bytes were not independently reconstructed; current successful/failed routes are separate dated observations.
- ESCRT-0, ESCRT umbrella and ESCRT-I independent review: No maintained images are present in these three records. No optional missing-example or universal formation requirement is invented. Parent-owned corpus gates, CI, queue admission, merge and cleanup are outside this source-slice certification.
- ESCRT-II, III and IV independent review: Three unchanged ESCRT II/III/IV targets reviewed in full. Two inherited minor exact-family findings remain open; III has a positive qualified pass. Three formal original no-expression applicability exclusions require successor correction. No own original evidence-kind defect found after all evidence rows were inspected.
- ESCRT-II, III and IV independent review: Fresh Teo2004 PDF, Im2008/2009, Lata2008 and Yang2010 genuine bodies were read only at declared locators. No figure pixels, atomic coordinates or supplementary experiments were independently analyzed. Native metadata and abstract evidence do not imply full-body access. Henne2011 secondary review is complete-abstract-only after a current publisher403; no detailed review-body claim is independently certified. Hierro publisher is abstract/subscription preview; Babst2002 publisher403, Yang canonical browser challenge and EuropePMC500 are access context only, independently distinguished from a successful Yang alternate PMC body.
- ESCRT-II, III and IV independent review: Yeast species4932 and S288C559292 reference proteins differ from Teo ATCC9763D genomic source, bacterial recombinant expression and Im BY4741/BY4742 assays. Human recombinant interfaces and engineered CHMP polymers are not native yeast assembly geometry. COMMON is qualitative scope, not an organism-frequency census.
- ESCRT-II, III and IV independent review: Im2009 experimentally separates ESCRT-II-driven activation from membrane localization of individual Vps20. Yang Vta1/Vps4 fragment interface and cargo tests do not turn speculative planar arrays into solved whole assemblies. Lata ATP-driven disassembly is direct, while final membrane fission mechanism is proposed. No fixed Vps4 oligomer count or universal formation flags imposed.
- ESCRT-II, III and IV independent review: Exact Vps22/Vps25/Vps36 and Vta1 family joins are resolved independently. The bounded III/Vps4 candidate review uses current example xrefs and inspected family/domain hierarchy; it does not prove no finer mapping exists elsewhere. IPR050304 unchecked LLM prose is excluded as scientific support. Existing optional stoichiometry discussion is not fabricated into a required-field defect.
- ESCRT-II, III and IV independent review: Complete current official catalogue has no matching yeast/human host. No unrelated bacterial expression-host dataset is queried as a biological proxy. Historical runner unavailable is actual Nov3 00:49Z; no fresh invocation claimed. Current public catalogue receipt is independent evidence with actual Nov4 timestamp.
- ESCRT-II, III and IV independent review: Actual six root native commands passed: II3 reviewed examples/3COVERED nodes, III4/4, IV2/2. These are identity/coverage checks, not independent experimental membership or necessity evidence. Original native validation/render0 and39 historical hashes verified. Root corpus gates, final successor validation, CI and queue are separate and are not pre-certified here.
- ESCRT-II, III and IV independent review: Only26 explicitly listed maintained inputs informed this source report. No repository, original bundle, record, Git or GitHub mutation. Exact search scopes are limited to the actual issuing-authority requests; no exhaustive literature-absence claim.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- One changed EmrKY target is substantively refreshed; all nine other current target hashes match their original frozen inputs. All used maintained context is frozen before synthesis.
- Four review-bundle issues track ten applicability corrections, four failed-access evidence-kind corrections, the stale-input refresh and supported rejection of the original EmrKY blanket formation-essentiality finding. Scientific curation remains separately filed.
- Preserve inferred EmrK/EmrY/TolC membership, absent EmrK/EmrY source counts and TolC3. The new minor concerns explicit CPX attribution in added edge evidence notes, not an automatic instruction to change all essentiality enums.
- Twenty current native protein commands passed across21 protein examples and22 typed protein nodes:21 COVERED and one external Vps27 recruiter UNANCHORED_WITH_UNIPROT. The recruiter is not a missing ESCRT-I constituent; identity and coverage checks are not experimental membership or necessity evidence.
- Historical source access and adapter-runner unavailability retain their actual dates. Successful current body retrievals, primary abstracts, secondary abstracts, database annotations and failed-access diagnostics retain distinct scopes.
- Dated rationale/history remain append-only. Exact family findings do not force broad domains or unresolved paralog boundaries; the existing Mvb12 and stoichiometry discussions are not automatic optional-inventory defects.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T090543Z-pr2391-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2391: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T08:44:33.752584Z'
finished_at: '2026-11-04T09:05:43Z'
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
summary: Current-input successor for all ten PR2391 records. EmrKY-TolC is the sole
  stale target and its four new graph edges are substantively reassessed. Eight inherited
  minor findings remain open and one new minor CPX-attribution finding is added. The
  original EmrKY major is rejected as formulated after independent source review and
  a second challenge; this does not certify experimentally demonstrated necessity.
  ER Sec, the ESCRT umbrella and ESCRT-III retain qualified passes. Ten applicability
  exclusions and four historical access-kind occurrences are corrected without changing
  the twenty original artifacts or any scientific record.
source:
  git_revision: a38c89d6665997cbf5972462345df67f09b41009
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
  - path: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    sha256: 7537240a1770406c3b0b6272ef277be10afa2a64fe43e40d9e75729ae00bae4a
    role: target
  - path: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    sha256: 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f
    role: target
  - path: data/structures/other/epsilon_dna_polymerase_complex.yaml
    sha256: d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635
    role: target
  - path: data/structures/other/ermes_complex.yaml
    sha256: 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9
    role: target
  - path: data/structures/other/escrt_0_complex.yaml
    sha256: 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d
    role: target
  - path: data/structures/other/escrt_complex.yaml
    sha256: 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e
    role: target
  - path: data/structures/other/escrt_i_complex.yaml
    sha256: 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc
    role: target
  - path: data/structures/other/escrt_ii_complex.yaml
    sha256: e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7
    role: target
  - path: data/structures/other/escrt_iii_complex.yaml
    sha256: 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8
    role: target
  - path: data/structures/other/escrt_iv_complex.yaml
    sha256: 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2
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
  - path: reviews/structured/20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit/review.md
    sha256: cfe7d81af53af36cac59c218c5772ed0b168b847007b636927dd58381b8db532
    role: context
  - path: reviews/structured/20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit/review.yaml
    sha256: 1adf341165055cbed4c477f90d8204420b8447952f1bcf02d2b7637e674d630e
    role: context
  - path: reviews/structured/20261022T063719Z-endoplasmic-reticulum-sec-complex-audit/review.md
    sha256: 6b52409b597d9ae875f7bcea78f6677d55a2c0a81e363699195b2b8b4cdff578
    role: context
  - path: reviews/structured/20261022T063719Z-endoplasmic-reticulum-sec-complex-audit/review.yaml
    sha256: 9349bd98523505b32afb975085db87010e602782874e91f59b908ad65d8449e1
    role: context
  - path: reviews/structured/20261022T063720Z-epsilon-dna-polymerase-complex-audit/review.md
    sha256: 3ca499513ce8b4504a00e7a7f7647f6f9d614bce0fe080f813f2003bd18ec7c3
    role: context
  - path: reviews/structured/20261022T063720Z-epsilon-dna-polymerase-complex-audit/review.yaml
    sha256: f3fe0d8d81b30870e463939bfdc55d9b47989e3c93ed4aac048b8ba17c63a362
    role: context
  - path: reviews/structured/20261022T063721Z-ermes-complex-audit/review.md
    sha256: 98674e6e742f85e9e2baef0d81dd4c1ae1794880877457486d46c1f808a9f61e
    role: context
  - path: reviews/structured/20261022T063721Z-ermes-complex-audit/review.yaml
    sha256: fa9c2aa5f07e521321a3f3984cb6d40a2bfa657382582075dd15d0853c6550ba
    role: context
  - path: reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.md
    sha256: dd332a4830bc278269eef9f8ac5d2b9f3e8cd4f44d9d65851a84083c7bc08207
    role: context
  - path: reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.yaml
    sha256: f6cdeb862fc3fd639002e5b6ff1261ec9ac6ff4ebd447255157bacc24d051e97
    role: context
  - path: reviews/structured/20261022T063722Z-escrt-complex-audit/review.md
    sha256: 0855139ad291ec4234fd24b0199db8193af11798cebfd6504669b4c1105f66cc
    role: context
  - path: reviews/structured/20261022T063722Z-escrt-complex-audit/review.yaml
    sha256: 1d2c52c200d099f4cedcfd01f46ee022bfffeeade757a64c49e42beb4dccb6de
    role: context
  - path: reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.md
    sha256: 2d3e9d37421d323c120a6e11f2f0c71697fc34b9044c827989bc86966c5696ea
    role: context
  - path: reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.yaml
    sha256: 3022dba13fbac6b42465e752dfc072bafb8981a6a446d32263da703330406382
    role: context
  - path: reviews/structured/20261022T063724Z-escrt-ii-complex-audit/review.md
    sha256: e609396c654f0a23e1e599da95a8b63c169cd49bd87a5d4b15b71f25789f0235
    role: context
  - path: reviews/structured/20261022T063724Z-escrt-ii-complex-audit/review.yaml
    sha256: 6d5e731969e3179af4bd46787846a7469aa55404254febdb4af446968f1dd355
    role: context
  - path: reviews/structured/20261022T063725Z-escrt-iii-complex-audit/review.md
    sha256: 127bc71edf4c08e840184de824f8a5eebaad7e3bce5f39d141fde4822db2472e
    role: context
  - path: reviews/structured/20261022T063725Z-escrt-iii-complex-audit/review.yaml
    sha256: 5e9542977e056076935f1e7228ab4c4be362fb773cec542bdc584c2ce84ad893
    role: context
  - path: reviews/structured/20261022T063726Z-escrt-iv-complex-audit/review.md
    sha256: c739138df2ecc946da6953a7426f481e4e29eb032cd4212b7878735172330cfc
    role: context
  - path: reviews/structured/20261022T063726Z-escrt-iv-complex-audit/review.yaml
    sha256: 3694de58856d7aade6fcbf380366c30518bf0fe0f938a34b645682101e00bc57
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
- target_id: cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  path: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
  label: EmrKY-TolC multidrug efflux transport complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
- target_id: GO:0031205
  path: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  label: endoplasmic reticulum Sec complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    role: maintained scientific record
- target_id: GO:0008622
  path: data/structures/other/epsilon_dna_polymerase_complex.yaml
  label: epsilon DNA polymerase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/epsilon_dna_polymerase_complex.yaml
    role: maintained scientific record
- target_id: GO:0032865
  path: data/structures/other/ermes_complex.yaml
  label: ERMES complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ermes_complex.yaml
    role: maintained scientific record
- target_id: GO:0033565
  path: data/structures/other/escrt_0_complex.yaml
  label: ESCRT-0 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
- target_id: GO:0036452
  path: data/structures/other/escrt_complex.yaml
  label: ESCRT complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_complex.yaml
    role: maintained scientific record
- target_id: GO:0000813
  path: data/structures/other/escrt_i_complex.yaml
  label: ESCRT I complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_i_complex.yaml
    role: maintained scientific record
- target_id: GO:0000814
  path: data/structures/other/escrt_ii_complex.yaml
  label: ESCRT II complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_ii_complex.yaml
    role: maintained scientific record
- target_id: GO:0000815
  path: data/structures/other/escrt_iii_complex.yaml
  label: ESCRT III complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_iii_complex.yaml
    role: maintained scientific record
- target_id: GO:1990621
  path: data/structures/other/escrt_iv_complex.yaml
  label: ESCRT IV complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_iv_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    0d46f4dcafa33fe2e307874818552e76933abb7a.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head a38c89d6665997cbf5972462345df67f09b41009.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head a38c89d6665997cbf5972462345df67f09b41009.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head a38c89d6665997cbf5972462345df67f09b41009.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head a38c89d6665997cbf5972462345df67f09b41009.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head a38c89d6665997cbf5972462345df67f09b41009.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  command: just validate data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  command: just validate-strict data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0031205
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just validate data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0031205
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: just validate-strict data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0008622
  status: passed
  required: true
  target_ids:
  - GO:0008622
  command: just validate data/structures/other/epsilon_dna_polymerase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0008622
  status: passed
  required: true
  target_ids:
  - GO:0008622
  command: just validate-strict data/structures/other/epsilon_dna_polymerase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0032865
  status: passed
  required: true
  target_ids:
  - GO:0032865
  command: just validate data/structures/other/ermes_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0032865
  status: passed
  required: true
  target_ids:
  - GO:0032865
  command: just validate-strict data/structures/other/ermes_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0033565
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just validate data/structures/other/escrt_0_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0033565
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just validate-strict data/structures/other/escrt_0_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0036452
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just validate data/structures/other/escrt_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0036452
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: just validate-strict data/structures/other/escrt_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0000813
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: just validate data/structures/other/escrt_i_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0000813
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: just validate-strict data/structures/other/escrt_i_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0000814
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just validate data/structures/other/escrt_ii_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0000814
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just validate-strict data/structures/other/escrt_ii_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0000815
  status: passed
  required: true
  target_ids:
  - GO:0000815
  command: just validate data/structures/other/escrt_iii_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0000815
  status: passed
  required: true
  target_ids:
  - GO:0000815
  command: just validate-strict data/structures/other/escrt_iii_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:1990621
  status: passed
  required: true
  target_ids:
  - GO:1990621
  command: just validate data/structures/other/escrt_iv_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:1990621
  status: passed
  required: true
  target_ids:
  - GO:1990621
  command: just validate-strict data/structures/other/escrt_iv_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391
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
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  summary: All ten records contain positive molecular/pathway assertions and require
    the native applicability assessment. The complete current official catalogue supplies
    no matching yeast/human natural-host dataset. EmrKY E. coli K-12 is checked against
    precise1k:4257 genes,201 modules and BW25113/DGF-298/GMOS/MG1655/W3110 strains.
    Current bounded joins associate EmrK/b2368 and EmrY/b2367 with EvgA k38 (15 members),
    and TolC/b3035 with SoxS k22 (117 members). Dataset-strain context differs from
    May2009 modified OCL62. Module membership is expression context, not direct regulation
    or assembly evidence. Historical unavailable runner is retained separately; no
    fresh runner execution or proxy expression-host query is claimed.
  evidence_ids:
  - micro-catalogue
  - micro-dataset-meta
  - micro-dataset-modules
  - micro-dataset-genes
  - micro-membership-b2368
  - micro-membership-b2367
  - micro-membership-b3035
  - micro-module-22
  - micro-module-22-genes
  - micro-module-38
  - micro-module-38-genes
  - plaque-catalogue
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-profile
  - micro-graph-policy
  - micro-protein-P02930
  - micro-protein-P21951
  - micro-protein-P24482
  - micro-protein-P27344
  - micro-protein-P52599
  - micro-protein-P52600
  - micro-protein-Q04603
  - micro-taxon-4932
  - micro-taxon-559292
  - micro-taxon-83333
  - micro-ancestors-GO0008622
  - micro-ancestors-GO0031205
  - micro-ancestors-GO0032865
  - micro-go-0005741
  - micro-go-0005783
  - micro-go-0005784
  - micro-go-0005789
  - micro-go-0006260
  - micro-go-0008622
  - micro-go-0031205
  - micro-go-0031207
  - micro-go-0032865
  - micro-go-0042575
  - micro-go-0042910
  - micro-go-0098799
  - micro-go-0140330
  - micro-go-0140534
  - micro-go-1990281
  - micro-family-IPR004638
  - micro-family-IPR005694-retry
  - micro-family-IPR016266
  - micro-family-IPR029703
  - micro-family-IPR050568
  - micro-family-IPR050739
  - micro-family-IPR051377
  - micro-family-IPR058622
  - micro-family-TIGR00711
  - micro-family-TIGR00998
  - micro-complex-CPX-4273
  - micro-eco-0005547
  - micro-doi-0
  - micro-doi-1
  - micro-doi-2
  - micro-doi-3
  - micro-doi-4
  - micro-pmid-11024162
  - micro-pmid-12571237
  - micro-pmid-14562095
  - micro-pmid-15814431
  - micro-pmid-16369485
  - micro-pmid-19721076
  - micro-pmid-25538242
  - micro-pmid-9745046
  - micro-PMC2772303-legacy
  - micro-PMC110797-legacy
  - micro-PMC307522-legacy
  - micro-PMC6367035-legacy
  - micro-PMC2933203-legacy
  - micro-PMC5839780-legacy
  - micro-PMC4319046-legacy
  - micro-asturias2006-publisher
  - micro-dataset-meta
  - micro-dataset-modules
  - micro-module-22
  - micro-module-22-genes
  - micro-module-38
  - micro-module-38-genes
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
  - plaque-go-0033565-ancestors
  - plaque-go-0036452-ancestors
  - plaque-go-0000813-ancestors
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-pmid-12006563
  - plaque-pmid-12055639
  - plaque-pmid-12900393
  - plaque-pmid-14562095
  - plaque-pmid-21763610
  - plaque-pmid-11511343
  - plaque-pmid-9790597
  - plaque-pmid-17145965
  - plaque-pmid-17135292
  - plaque-bilodeau-publisher
  - plaque-PMC2172707-body
  - plaque-PMC2064680-body
  - plaque-PMC1783790-body
  - plaque-up-P40343
  - plaque-up-P38753
  - plaque-up-P25604
  - plaque-up-Q02767
  - plaque-up-Q99176
  - plaque-ipr-IPR017073
  - plaque-ipr-IPR050670
  - plaque-ipr-IPR052070
  - plaque-ipr-IPR007143
  - plaque-ipr-IPR017435
  - plaque-ipr-IPR009851
  - plaque-panther-PTHR45929
  - plaque-catalogue
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-yang2010-legacy
  - septin-hierro2004-publisher
  - septin-go
  - septin-GO0000814-ancestors
  - septin-tax4932
  - septin-tax559292
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-protein-Q12483
  - septin-pmid-12194858
  - septin-doi-j_devcel_2004_09_003
  - septin-doi-j_devcel_2008_04_004
  - septin-doi-j_devcel_2009_07_008
  - septin-doi-nature02914
  - septin-doi-science_1161070
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-ipr-IPR016689
  - septin-ipr-IPR008570
  - septin-ipr-IPR037855
  - septin-GO0000815-ancestors
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-protein-P39929
  - septin-protein-Q04272
  - septin-pmid-12194857
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-ipr-IPR005024
  - septin-GO1990621-ancestors
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-pmid-14562095
  - septin-pmid-14701806
  - septin-pmid-20696398
  - septin-ipr-IPR044538
  - septin-ipr-IPR045253
  - septin-ipr-IPR050304
  - septin-catalogue
  - septin-henne2011-abstract
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
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
- check_id: emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify
  name: Native EmrKY-TolC multidrug efflux transport complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify
- check_id: emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal
  name: Native EmrKY-TolC multidrug efflux transport complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal
- check_id: endoplasmic_reticulum_sec_complex-uniprot-verify
  name: Native endoplasmic reticulum Sec complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-endoplasmic_reticulum_sec_complex-uniprot-verify
- check_id: endoplasmic_reticulum_sec_complex-uniprot-causal
  name: Native endoplasmic reticulum Sec complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031205
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/endoplasmic_reticulum_sec_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-endoplasmic_reticulum_sec_complex-uniprot-causal
- check_id: epsilon_dna_polymerase_complex-uniprot-verify
  name: Native epsilon DNA polymerase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0008622
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/epsilon_dna_polymerase_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-epsilon_dna_polymerase_complex-uniprot-verify
- check_id: epsilon_dna_polymerase_complex-uniprot-causal
  name: Native epsilon DNA polymerase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0008622
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/epsilon_dna_polymerase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-epsilon_dna_polymerase_complex-uniprot-causal
- check_id: ermes_complex-uniprot-verify
  name: Native ERMES complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0032865
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ermes_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ermes_complex-uniprot-verify
- check_id: ermes_complex-uniprot-causal
  name: Native ERMES complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0032865
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ermes_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ermes_complex-uniprot-causal
- check_id: escrt_0_complex-uniprot-verify
  name: Native ESCRT-0 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_0_complex-uniprot-verify
- check_id: escrt_0_complex-uniprot-causal
  name: Native ESCRT-0 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_0_complex-uniprot-causal
- check_id: escrt_complex-uniprot-verify
  name: Native ESCRT complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_complex-uniprot-verify
- check_id: escrt_complex-uniprot-causal
  name: Native ESCRT complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036452
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_complex-uniprot-causal
- check_id: escrt_i_complex-uniprot-verify
  name: Native ESCRT I complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_i_complex-uniprot-verify
- check_id: escrt_i_complex-uniprot-causal
  name: Native ESCRT I complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_i_complex-uniprot-causal
- check_id: escrt_ii_complex-uniprot-verify
  name: Native ESCRT II complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_ii_complex-uniprot-verify
- check_id: escrt_ii_complex-uniprot-causal
  name: Native ESCRT II complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_ii_complex-uniprot-causal
- check_id: escrt_iii_complex-uniprot-verify
  name: Native ESCRT III complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000815
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iii_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_iii_complex-uniprot-verify
- check_id: escrt_iii_complex-uniprot-causal
  name: Native ESCRT III complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000815
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iii_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_iii_complex-uniprot-causal
- check_id: escrt_iv_complex-uniprot-verify
  name: Native ESCRT IV complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990621
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iv_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_iv_complex-uniprot-verify
- check_id: escrt_iv_complex-uniprot-causal
  name: Native ESCRT IV complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990621
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iv_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-escrt_iv_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 1db4b3ec61bb37a31a2c8888ca43d294cbd73241734f58891d8b3bbc4bac53b1;
    current SHA256 7537240a1770406c3b0b6272ef277be10afa2a64fe43e40d9e75729ae00bae4a.
    Changed record reassessed against current sources.
  snapshot_sha256: 7537240a1770406c3b0b6272ef277be10afa2a64fe43e40d9e75729ae00bae4a
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1adf341165055cbed4c477f90d8204420b8447952f1bcf02d2b7637e674d630e
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f;
    current SHA256 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T063719Z-endoplasmic-reticulum-sec-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9349bd98523505b32afb975085db87010e602782874e91f59b908ad65d8449e1
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/epsilon_dna_polymerase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635;
    current SHA256 d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635.
    Record bytes unchanged since the original review.
  snapshot_sha256: d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T063720Z-epsilon-dna-polymerase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f3fe0d8d81b30870e463939bfdc55d9b47989e3c93ed4aac048b8ba17c63a362
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/ermes_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9;
    current SHA256 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9.
    Record bytes unchanged since the original review.
  snapshot_sha256: 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T063721Z-ermes-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: fa9c2aa5f07e521321a3f3984cb6d40a2bfa657382582075dd15d0853c6550ba
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/escrt_0_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d;
    current SHA256 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f6cdeb862fc3fd639002e5b6ff1261ec9ac6ff4ebd447255157bacc24d051e97
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/escrt_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e;
    current SHA256 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T063722Z-escrt-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1d2c52c200d099f4cedcfd01f46ee022bfffeeade757a64c49e42beb4dccb6de
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/escrt_i_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc;
    current SHA256 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3022dba13fbac6b42465e752dfc072bafb8981a6a446d32263da703330406382
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/escrt_ii_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7;
    current SHA256 e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7.
    Record bytes unchanged since the original review.
  snapshot_sha256: e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T063724Z-escrt-ii-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6d5e731969e3179af4bd46787846a7469aa55404254febdb4af446968f1dd355
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/escrt_iii_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8;
    current SHA256 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8.
    Record bytes unchanged since the original review.
  snapshot_sha256: 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T063725Z-escrt-iii-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5e9542977e056076935f1e7228ab4c4be362fb773cec542bdc584c2ce84ad893
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/escrt_iv_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Original frozen SHA256 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2;
    current SHA256 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2.
    Record bytes unchanged since the original review.
  snapshot_sha256: 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T063726Z-escrt-iv-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T09:05:43Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3694de58856d7aade6fcbf380366c30518bf0fe0f938a34b645682101e00bc57
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
  locator: Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009
  accessed_at: '2026-11-04T09:01:57.508650Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target differs by four added graph
    edges and dated history.
  snapshot_sha256: 7537240a1770406c3b0b6272ef277be10afa2a64fe43e40d9e75729ae00bae4a
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T09:01:57.508728Z'
  support: supports
  summary: Original source inputs, checks, source tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access observations are not new executions
    or new body reads.
  snapshot_sha256: 1adf341165055cbed4c477f90d8204420b8447952f1bcf02d2b7637e674d630e
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/0-stale.diff
  locator: Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446
  accessed_at: '2026-11-04T09:01:57.508767Z'
  support: supports
  summary: Three constituent contributes-to edges and one transport-to-export edge
    were added with dated history. Formal membership and coarse export are reassessed
    separately from the new evidence-note attribution.
  snapshot_sha256: 1016abce6cc8dda2d05bb6a1459d7b3ebb9cec0d85ce69b69acf15e9921cbc6e
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/endoplasmic_reticulum_sec_complex.yaml
  locator: Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009
  accessed_at: '2026-11-04T09:01:57.508887Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target unchanged from original
    frozen input.
  snapshot_sha256: 9c518bbd838470051ecd41f44fade19a7575e189a7ee995022f6447240cbae4f
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T063719Z-endoplasmic-reticulum-sec-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T09:01:57.508910Z'
  support: supports
  summary: Original source inputs, checks, source tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access observations are not new executions
    or new body reads.
  snapshot_sha256: 9349bd98523505b32afb975085db87010e602782874e91f59b908ad65d8449e1
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/1-stale.diff
  locator: Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446
  accessed_at: '2026-11-04T09:01:57.508941Z'
  support: supports
  summary: Empty diff; current bytes equal original frozen target.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/epsilon_dna_polymerase_complex.yaml
  locator: Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009
  accessed_at: '2026-11-04T09:01:57.508970Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target unchanged from original
    frozen input.
  snapshot_sha256: d2ba24b44d526b14423e20d02b567e0564f8cf162bc811572fa69fce15878635
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T063720Z-epsilon-dna-polymerase-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T09:01:57.508992Z'
  support: supports
  summary: Original source inputs, checks, source tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access observations are not new executions
    or new body reads.
  snapshot_sha256: f3fe0d8d81b30870e463939bfdc55d9b47989e3c93ed4aac048b8ba17c63a362
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/2-stale.diff
  locator: Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446
  accessed_at: '2026-11-04T09:01:57.509029Z'
  support: supports
  summary: Empty diff; current bytes equal original frozen target.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-3
  kind: record_content
  reference: data/structures/other/ermes_complex.yaml
  locator: Complete maintained YAML at a38c89d6665997cbf5972462345df67f09b41009
  accessed_at: '2026-11-04T09:01:57.509059Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or quantitative physical measurements. Current target unchanged from original
    frozen input.
  snapshot_sha256: 461d942cf1aedc1f89e6ed617555ce0e3377d103e971b63c8902bcccc66e31f9
- evidence_id: micro-prior-3
  kind: prior_review
  reference: reviews/structured/20261022T063721Z-ermes-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T09:01:57.509077Z'
  support: supports
  summary: Original source inputs, checks, source tiers, assessments, verdict, findings
    and actions inspected. Historical checks and access observations are not new executions
    or new body reads.
  snapshot_sha256: fa9c2aa5f07e521321a3f3984cb6d40a2bfa657382582075dd15d0853c6550ba
- evidence_id: micro-delta-3
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/3-stale.diff
  locator: Original frozen target versus current main 2bd129722cd521b9ce6663c3c8c108d8d01d0446
  accessed_at: '2026-11-04T09:01:57.509107Z'
  support: supports
  summary: Empty diff; current bytes equal original frozen target.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components and Discussions clauses
  accessed_at: '2026-11-04T09:01:57.509137Z'
  support: supports
  summary: Taxon-neutral families/classes and honest reviewed-label-only constituents
    are valid. Formation differs from function and viability. Dated rationale and
    posed_date are preserved; current prompt/notes may be narrowed only as supported.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, ComponentGroundingStatusEnum and
    causal node types
  accessed_at: '2026-11-04T09:01:57.509162Z'
  support: supports
  summary: ESSENTIAL means the defined structure does not form without the constituent;
    policy does not require a particular deletion assay for every defining subunit.
    This is distinct from attributing an essentiality annotation to a source that
    supplies only membership. UNKNOWN may coexist with condition-scoped stability
    evidence.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record review, Structured Source Cross-Checks and source-evidence
    contract
  accessed_at: '2026-11-04T09:01:57.509193Z'
  support: supports
  summary: Positive named proteins/regulators/pathways trigger applicability assessment
    even without transcriptomic claims or populated examples. Exact matched dataset
    context is bounded and does not establish physical assembly.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Native persistence and source provenance
  accessed_at: '2026-11-04T09:01:57.509216Z'
  support: supports
  summary: Only concrete review or scientific defects are findings. Unavailable routes,
    optional empty fields and retained uncertainty alone do not constitute scientific
    defects. Root owns successor save and global/future gates.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Claim-scoped constituents, function and assembly relations
  accessed_at: '2026-11-04T09:01:57.509235Z'
  support: supports
  summary: Membership, coarse function, measured stability and mechanistic transitions
    remain distinct. No compulsory universal necessity, exact count or new experiment
    is imposed.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/original-audit.json
  locator: Eight actual original native validate/render commands; 56 historical input
    occurrences; eight original artifacts
  accessed_at: '2026-11-04T08:50:53.172802Z'
  support: supports
  summary: All four original YAMLs validate and render exactly the retained Markdown;
    historical hashes match recorded revisions and eight artifacts match original
    PR head.
  snapshot_sha256: 4e7890726ec87640065012141ceb4abfbc93d942636a9bbbf65757785c213726
- evidence_id: micro-protein-P02930
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P02930.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P02930.raw
  accessed_at: '2026-11-04T08:49:09.260691Z'
  support: supports
  summary: 'P02930: UniProtKB reviewed (Swiss-Prot); Outer membrane protein TolC;
    genes [''tolC'']; loci [''b3035'', ''JW5503'']; taxon 83333; InterPro [''IPR003423'',
    ''IPR010130'', ''IPR058622'', ''IPR051906'']. Annotation evidence tiers and organism-specific
    examples remain separate from primary body and family-level claims.'
  snapshot_sha256: cef14f6af1999fe0b5218d959cca8788ec00afc1b145201ba48344a4b15bbb04
- evidence_id: micro-protein-P21951
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P21951.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P21951.raw
  accessed_at: '2026-11-04T08:49:13.650416Z'
  support: supports
  summary: 'P21951: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon catalytic
    subunit A; genes [''POL2'']; loci [''YNL262W'', ''N0825'']; taxon 559292; InterPro
    [''IPR006172'', ''IPR006133'', ''IPR043502'', ''IPR042087'', ''IPR013697'', ''IPR023211'',
    ''IPR029703'', ''IPR055191'', ''IPR012337'', ''IPR036397'', ''IPR063197'', ''IPR054475''].
    Annotation evidence tiers and organism-specific examples remain separate from
    primary body and family-level claims.'
  snapshot_sha256: 93f959f4353502db7273f103877fba046b94397be479ee785e2ab018a104a4c6
- evidence_id: micro-protein-P24482
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P24482.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P24482.raw
  accessed_at: '2026-11-04T08:49:12.078371Z'
  support: supports
  summary: 'P24482: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon subunit
    B; genes [''DPB2'']; loci [''YPR175W'', ''P9705.7'']; taxon 559292; InterPro [''IPR007185'',
    ''IPR063374'', ''IPR016266'']. Annotation evidence tiers and organism-specific
    examples remain separate from primary body and family-level claims.'
  snapshot_sha256: 5e9c208313068eeb7e8a9ba38e8acb9fdabe4eb238cc6bcb52e26f3649d38683
- evidence_id: micro-protein-P27344
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P27344.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P27344.raw
  accessed_at: '2026-11-04T08:49:13.554763Z'
  support: supports
  summary: 'P27344: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon subunit
    C; genes [''DPB3'']; loci [''YBR278W'', ''YBR2015'']; taxon 559292; InterPro [''IPR009072'',
    ''IPR050568'']. Annotation evidence tiers and organism-specific examples remain
    separate from primary body and family-level claims.'
  snapshot_sha256: 813a343e236dd50328b6b92db68f7a188f1f7c23ffc79f9829bd283f3b97357a
- evidence_id: micro-protein-P52599
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P52599.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P52599.raw
  accessed_at: '2026-11-04T08:49:09.781129Z'
  support: supports
  summary: 'P52599: UniProtKB reviewed (Swiss-Prot); Probable multidrug resistance
    protein EmrK; genes [''emrK'']; loci [''b2368'', ''JW2365'']; taxon 83333; InterPro
    [''IPR058634'', ''IPR058633'', ''IPR050739'', ''IPR005694'']. Annotation evidence
    tiers and organism-specific examples remain separate from primary body and family-level
    claims.'
  snapshot_sha256: 73d8b15e32b36811389905fe157087caa8db607f214ddaa847d1bfa2ac5da303
- evidence_id: micro-protein-P52600
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P52600.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-P52600.raw
  accessed_at: '2026-11-04T08:49:09.147439Z'
  support: supports
  summary: 'P52600: UniProtKB reviewed (Swiss-Prot); Probable multidrug resistance
    protein EmrY; genes [''emrY'']; loci [''b2367'', ''JW2364'']; taxon 83333; InterPro
    [''IPR004638'', ''IPR011701'', ''IPR020846'', ''IPR036259'']. Annotation evidence
    tiers and organism-specific examples remain separate from primary body and family-level
    claims.'
  snapshot_sha256: 3f181e1d711d29b67e08b91b88cc9036d45788d3217d69446b60152005a21921
- evidence_id: micro-protein-Q04603
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04603.json
  locator: Native identity/status/name, complete gene aliases/loci/taxon, InterPro
    xrefs and relevant FUNCTION/SUBUNIT/LOCATION annotations; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/protein-Q04603.raw
  accessed_at: '2026-11-04T08:49:09.787665Z'
  support: supports
  summary: 'Q04603: UniProtKB reviewed (Swiss-Prot); DNA polymerase epsilon subunit
    D; genes [''DPB4'']; loci [''YDR121W'']; taxon 559292; InterPro [''IPR051377'',
    ''IPR009072'']. Annotation evidence tiers and organism-specific examples remain
    separate from primary body and family-level claims.'
  snapshot_sha256: bc6495bed9da52fb9fd473800c575ee298e2bc5cac981a70b218ddd5ca507944
- evidence_id: micro-query-DPB2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-DPB2.raw
  accessed_at: '2026-11-04T08:49:58.931709Z'
  support: supports
  summary: Current bounded query returns ['P24482']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: f3324b19b03ab6c1cc4195389444fa0d48c1a69a42a0bc8e7f334e6f8cbfc5b5
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:49:58.931709Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-query-DPB3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-DPB3.raw
  accessed_at: '2026-11-04T08:50:00.026408Z'
  support: supports
  summary: Current bounded query returns ['P27344']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: e340f607e1f62ce868849b03af903413a50178691c9063f9fd0e5ee0571391db
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:50:00.026408Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-query-DPB4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-DPB4.raw
  accessed_at: '2026-11-04T08:50:00.934971Z'
  support: supports
  summary: Current bounded query returns ['Q04603']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: 832a7fb8258ecf2347addedf27fe8c0cf6df41aaf016ee00ef78a5e8fe759233
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:50:00.934971Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-query-POL2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-POL2.raw
  accessed_at: '2026-11-04T08:50:00.829699Z'
  support: supports
  summary: Current bounded query returns ['P21951']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: 47d1fa9f1e1fce809e4c93659a9a89d5ebd5f6a9a2ce5f441d758eefdbc130ac
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:50:00.829699Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-query-emrK
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrK%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-emrK.raw
  accessed_at: '2026-11-04T08:49:58.297771Z'
  support: supports
  summary: Current bounded query returns ['P52599']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: a7fbbf1bcf29b644cd4a992c79b779ffb9d8eb0fd6dc758825e76a9f2a227121
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrK%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:49:58.297771Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-query-emrY
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrY%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-emrY.raw
  accessed_at: '2026-11-04T08:49:58.497143Z'
  support: supports
  summary: Current bounded query returns ['P52600']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: 43c6be5c7d064c5aa9379d8f12345a1f4618256ee823cb50ccf72c84984969d4
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AemrY%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:49:58.497143Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-query-tolC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned reviewed exact-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/query-tolC.raw
  accessed_at: '2026-11-04T08:49:59.141989Z'
  support: supports
  summary: Current bounded query returns ['P02930']; primary genes and aliases separately
    inspected. This does not reconstruct or disprove a dated historical selection
    query.
  snapshot_sha256: 3e284eede466d8aa6d6eac091b434ce033083e18848c220476a3bdb06463365a
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T08:49:59.141989Z; reviewed:true and stated exact gene/taxon,
    requested size100, complete returned page. No universal alias or historical uniqueness
    inference.
- evidence_id: micro-taxon-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932
  locator: Scientific name, rank, parent, lineage and strain context; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/taxon-4932.raw
  accessed_at: '2026-11-04T08:49:10.795212Z'
  support: supports
  summary: '4932: Saccharomyces cerevisiae; rank species. Species, reference strain
    and exact experimental preparation are distinct.'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
- evidence_id: micro-taxon-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292
  locator: Scientific name, rank, parent, lineage and strain context; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/taxon-559292.raw
  accessed_at: '2026-11-04T08:49:10.921792Z'
  support: supports
  summary: '559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c); rank strain.
    Species, reference strain and exact experimental preparation are distinct.'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: micro-taxon-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333
  locator: Scientific name, rank, parent, lineage and strain context; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/taxon-83333.raw
  accessed_at: '2026-11-04T08:49:12.851981Z'
  support: supports
  summary: '83333: Escherichia coli (strain K12); rank strain. Species, reference
    strain and exact experimental preparation are distinct.'
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-ancestors-GO0008622
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008622/ancestors?relations=is_a
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/ancestors-GO0008622.raw
  accessed_at: '2026-11-04T08:49:59.767227Z'
  support: supports
  summary: GO:0008622 epsilon DNA polymerase complex; obsolete=False. A heterotetrameric
    DNA polymerase complex that catalyzes processive DNA synthesis in the absence
    of PCNA, but is further stimulated in the presence of PCNA. The complex contains
    a large catalytic subunit and three small subunits, and is best characterized
    in Saccharomyces, in which the subunits are named Pol2p, Dpb2p, Dpb3p, and Dpb4p.
    Some evidence suggests that DNA polymerase epsilon is the leading strand polymerase;
    it is also involved in nucleotide-excision repair and mismatch repair. Ancestors
    ['GO:0061695', 'GO:1902494', 'GO:1990234', 'GO:0140535', 'GO:0140513', 'GO:0032991',
    'GO:0042575', 'GO:0005575', 'GO:0008622']
  snapshot_sha256: 89a33f2beac0f62b1f2d0e1ef7c88b50e1c004182f25ca3a2dabc51071cc5d09
- evidence_id: micro-ancestors-GO0031205
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205/ancestors?relations=is_a
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/ancestors-GO0031205.raw
  accessed_at: '2026-11-04T08:49:59.521136Z'
  support: supports
  summary: GO:0031205 endoplasmic reticulum Sec complex; obsolete=False. An endoplasmic
    reticulum membrane-associated complex involved in the translocation of proteins
    that are targeted to the ER. In yeast, this complex consists of two subcomplexes,
    namely, the Sec61 complex and the Sec62/Sec63 complex. Ancestors ['GO:0098796',
    'GO:0032991', 'GO:0140534', 'GO:0005575', 'GO:0031205']
  snapshot_sha256: 4e5d21b49907c6724767f7807f4fec33d49c7648c26f2224dc85f0754af9e3d1
- evidence_id: micro-ancestors-GO0032865
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032865/ancestors?relations=is_a
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/ancestors-GO0032865.raw
  accessed_at: '2026-11-04T08:50:00.121048Z'
  support: supports
  summary: GO:0032865 ERMES complex; obsolete=False. A protein complex that links
    the endoplasmic reticulum with mitochondria and may have a role in promoting exchange
    of calcium and phospholipids between the two organelles. Ancestors ['GO:0098796',
    'GO:0098799', 'GO:0098798', 'GO:0032991', 'GO:0140534', 'GO:0032865', 'GO:0005575']
  snapshot_sha256: 85706fcf397d605c37b4da7182400c7a12a0a14747c9741efff69ca3407ddee7
- evidence_id: micro-go-0005741
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005741
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005741.raw
  accessed_at: '2026-11-04T08:49:11.996519Z'
  support: supports
  summary: GO:0005741 mitochondrial outer membrane; obsolete=False. The outer, i.e.
    cytoplasm-facing, lipid bilayer of the mitochondrial envelope.
  snapshot_sha256: 701047b3a306f8b0b4bb945bce5d7e5e99dafe21be3fc7a97c10b63f9cbe2ca6
- evidence_id: micro-go-0005783
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005783.raw
  accessed_at: '2026-11-04T08:49:11.777273Z'
  support: supports
  summary: GO:0005783 endoplasmic reticulum; obsolete=False. The irregular network
    of unit membranes, visible only by electron microscopy, that occurs in the cytoplasm
    of many eukaryotic cells. The membranes form a complex meshwork of tubular channels,
    which are often expanded into slitlike cavities called cisternae. The ER takes
    two forms, rough (or granular), with ribosomes adhering to the outer surface,
    and smooth (with no ribosomes attached).
  snapshot_sha256: 109f8b91a82edb8029dce3068738ce319d7a35059ca1fcdb6a545364ddbdb02d
- evidence_id: micro-go-0005784
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005784
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005784.raw
  accessed_at: '2026-11-04T08:49:11.059251Z'
  support: supports
  summary: GO:0005784 Sec61 translocon complex; obsolete=False. A translocon complex
    that contains a core heterotrimer of conserved alpha, beta and gamma subunits,
    and may contain additional proteins (translocon-associated proteins or TRAPs);
    in budding yeast the core proteins are Sec61p, Sbh1p, and Sss1p. The Sec61 translocon
    complex functions in cotranslational and posttranslational translocation events.
  snapshot_sha256: d2adf207f76fef758e1633a354691b2a3f1f06cec8bc2b9ab1ba4c4dd36ed916
- evidence_id: micro-go-0005789
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005789
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0005789.raw
  accessed_at: '2026-11-04T08:49:10.980484Z'
  support: supports
  summary: GO:0005789 endoplasmic reticulum membrane; obsolete=False. The lipid bilayer
    surrounding the endoplasmic reticulum.
  snapshot_sha256: 42bc1561cbde62c6bc58b28e5f0dc104be16608d5ea008d0dc439a556e513fac
- evidence_id: micro-go-0006260
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0006260.raw
  accessed_at: '2026-11-04T08:49:11.578206Z'
  support: supports
  summary: GO:0006260 DNA replication; obsolete=False. The cellular metabolic process
    in which a cell duplicates one or more molecules of DNA. DNA replication begins
    when specific sequences, known as origins of replication, are recognized and bound
    by the origin recognition complex, and ends when the original DNA molecule has
    been completely duplicated and the copies topologically separated. The unit of
    replication usually corresponds to the genome of the cell, an organelle, or a
    virus. The template for replication can either be an existing DNA molecule or
    RNA.
  snapshot_sha256: dc45c0feccd11a684f3d3f838297ef32f5b69a7b59a61d655120b7ac89ec8fba
- evidence_id: micro-go-0008622
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008622
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0008622.raw
  accessed_at: '2026-11-04T08:49:11.381423Z'
  support: supports
  summary: GO:0008622 epsilon DNA polymerase complex; obsolete=False. A heterotetrameric
    DNA polymerase complex that catalyzes processive DNA synthesis in the absence
    of PCNA, but is further stimulated in the presence of PCNA. The complex contains
    a large catalytic subunit and three small subunits, and is best characterized
    in Saccharomyces, in which the subunits are named Pol2p, Dpb2p, Dpb3p, and Dpb4p.
    Some evidence suggests that DNA polymerase epsilon is the leading strand polymerase;
    it is also involved in nucleotide-excision repair and mismatch repair.
  snapshot_sha256: 25263621ab9842f8df04ae07d7bca2aeb31a98b793c53fb729b3698f77c4aea0
- evidence_id: micro-go-0031205
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031205
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0031205.raw
  accessed_at: '2026-11-04T08:49:10.576040Z'
  support: supports
  summary: GO:0031205 endoplasmic reticulum Sec complex; obsolete=False. An endoplasmic
    reticulum membrane-associated complex involved in the translocation of proteins
    that are targeted to the ER. In yeast, this complex consists of two subcomplexes,
    namely, the Sec61 complex and the Sec62/Sec63 complex.
  snapshot_sha256: c136b647370c79519dd0b8b94d40156c3596a6dc3a63fb0021c0348c23f0d321
- evidence_id: micro-go-0031207
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031207
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0031207.raw
  accessed_at: '2026-11-04T08:49:11.155427Z'
  support: supports
  summary: GO:0031207 Sec62/Sec63 complex; obsolete=False. A protein complex involved
    in the posttranslational targeting of proteins to the ER. In yeast, it is a tetrameric
    complex consisting of Sec62p, Sec63p, Sec71p and Sec72p.
  snapshot_sha256: 3851297b49d06a925a0f7e662782392d81588bad7b2ab30a87366be6c9df7fc3
- evidence_id: micro-go-0032865
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032865
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0032865.raw
  accessed_at: '2026-11-04T08:49:11.594402Z'
  support: supports
  summary: GO:0032865 ERMES complex; obsolete=False. A protein complex that links
    the endoplasmic reticulum with mitochondria and may have a role in promoting exchange
    of calcium and phospholipids between the two organelles.
  snapshot_sha256: d2ab67513a252ea0ad99ee596014c99f6769c68e6ed40e1789b75c85244c2a21
- evidence_id: micro-go-0042575
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042575
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0042575.raw
  accessed_at: '2026-11-04T08:49:11.937595Z'
  support: supports
  summary: GO:0042575 DNA polymerase complex; obsolete=False. A protein complex that
    possesses DNA polymerase activity and is involved in template directed synthesis
    of DNA.
  snapshot_sha256: 03e6fe0dd8263f1e7fca5a967f126141e378a6b572bed7ab152452b57a4c727f
- evidence_id: micro-go-0042910
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042910
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0042910.raw
  accessed_at: '2026-11-04T08:49:10.381403Z'
  support: supports
  summary: GO:0042910 xenobiotic transmembrane transporter activity; obsolete=False.
    Enables the directed movement of a xenobiotic from one side of a membrane to the
    other. A xenobiotic is a compound foreign to the organism exposed to it. It may
    be synthesized by another organism (like ampicilin) or it can be a synthetic chemical.
  snapshot_sha256: 76cbec1d89ce72bdc0641b6589f6371ab3aac3701e7df06d5314e7a974ef9101
- evidence_id: micro-go-0098799
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098799
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0098799.raw
  accessed_at: '2026-11-04T08:49:11.646841Z'
  support: supports
  summary: GO:0098799 outer mitochondrial membrane protein complex; obsolete=False.
    Any protein complex that is part of the outer mitochondrial membrane.
  snapshot_sha256: 91e7dcb5172450141beb63b1231dd018f7f517db9c5cf1c0fc4699d8a4f0654c
- evidence_id: micro-go-0140330
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140330
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0140330.raw
  accessed_at: '2026-11-04T08:49:10.448227Z'
  support: supports
  summary: GO:0140330 xenobiotic detoxification by transmembrane export across the
    cell outer membrane; obsolete=False. A process that reduces or removes the toxicity
    of a xenobiotic by exporting it outside the cell through the outer membrane.
  snapshot_sha256: d6f5d7728a0cefa6f69c1c80e1d0869d05dc046a118c238d55f9f40d68615ed6
- evidence_id: micro-go-0140534
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140534
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-0140534.raw
  accessed_at: '2026-11-04T08:49:10.980443Z'
  support: supports
  summary: GO:0140534 endoplasmic reticulum protein-containing complex; obsolete=False.
    A protein complex that is part of an endoplasmic reticulum.
  snapshot_sha256: 8dfd81ec6bbf457d3110ef292a97b1b578f913fe012851646fdba92843ab54e3
- evidence_id: micro-go-1990281
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990281
  locator: Exact active term definition and, where requested, complete returned is_a
    ancestors; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/go-1990281.raw
  accessed_at: '2026-11-04T08:49:10.385450Z'
  support: supports
  summary: GO:1990281 efflux pump complex; obsolete=False. A protein complex that
    is capable of efflux transmembrane transporter activity.
  snapshot_sha256: 05723b3fa7f27617c119b11cbf637ac6297f15b9f5ad5c2746ec6a47b382b89e
- evidence_id: micro-family-IPR004638
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004638/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR004638.raw
  accessed_at: '2026-11-04T08:52:01.736645Z'
  support: supports
  summary: 'IPR004638: Drug resistance transporter EmrB-like; native type family.
    Broader homologous class is distinguished from the narrower named component; it
    is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping.'
  snapshot_sha256: 633ee99cb1562d934fe7f86ce75875bc69f1394a42250bdf6a58ce6a0fc00caf
- evidence_id: micro-family-IPR005694-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005694/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR005694-retry.raw
  accessed_at: '2026-11-04T08:56:47.373817Z'
  support: supports
  summary: 'IPR005694: Membrane fusion proteins, proteobacteria; native type family.
    Broader homologous class is distinguished from the narrower named component; it
    is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping.'
  snapshot_sha256: 2a06789ed6f0e233d35d7d3e1848aecc8646a06959cd8cb470d2086c6133afea
- evidence_id: micro-family-IPR016266
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016266/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR016266.raw
  accessed_at: '2026-11-04T08:49:09.858224Z'
  support: supports
  summary: 'IPR016266: DNA polymerase epsilon, subunit B; native type family. Native
    family identity/type and example membership assessed separately; database prose
    is authority context, not a new primary experiment.'
  snapshot_sha256: fe69489e66565a275d910dbdf6d6ecdc8c9906a06f70df0c785051fba5a13432
- evidence_id: micro-family-IPR029703
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029703/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR029703.raw
  accessed_at: '2026-11-04T08:49:09.758221Z'
  support: supports
  summary: 'IPR029703: DNA polymerase epsilon catalytic subunit; native type family.
    Native family identity/type and example membership assessed separately; database
    prose is authority context, not a new primary experiment.'
  snapshot_sha256: b80776af3402c4cd286ab6bb2c65fa27e91a155fd759fbe22de2c1ef72567dd6
- evidence_id: micro-family-IPR050568
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050568/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR050568.raw
  accessed_at: '2026-11-04T08:52:01.706039Z'
  support: supports
  summary: 'IPR050568: Transcription/DNA replication regulator; native type family.
    Broader homologous class is distinguished from the narrower named component; it
    is not silently substituted as an exact unresolved EmrK, EmrY or Dpb3 mapping.'
  snapshot_sha256: 11f3355159a9e41625de92336d1d3d830ae1f087f1a4ed5ff9a86470bca3ef83
- evidence_id: micro-family-IPR050739
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050739/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR050739.raw
  accessed_at: '2026-11-04T08:52:01.680256Z'
  support: supports
  summary: 'IPR050739: Membrane Fusion Protein; native type family. Native family
    identity/type and example membership assessed separately; database prose is authority
    context, not a new primary experiment.'
  snapshot_sha256: 09777ecee81e4a86375105705c31afe25c2f5f254e1e9dbf4513720dd3c17f9d
- evidence_id: micro-family-IPR051377
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051377/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR051377.raw
  accessed_at: '2026-11-04T08:49:09.950665Z'
  support: supports
  summary: 'IPR051377: DNA Polymerase Epsilon Subunit; native type family. Dpb4/POLE3-family
    membership is corroborated by the complete reviewed-member response and Q04603
    native xref. LLM-flagged description is not used as primary biological evidence.'
  snapshot_sha256: 9bdfe311b53f978a624fea4228263d4408ef60630986f7a2e4649c9474aa9c95
- evidence_id: micro-family-IPR058622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR058622.raw
  accessed_at: '2026-11-04T08:49:09.462914Z'
  support: supports
  summary: 'IPR058622: Outer membrane channel protein TolC; native type family. Native
    family identity/type and example membership assessed separately; database prose
    is authority context, not a new primary experiment.'
  snapshot_sha256: d3c58cbb9737d5f395f703b634f84df048f355555af2b817f321a5e474b8e310
- evidence_id: micro-family-TIGR00711
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR00711/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-TIGR00711.raw
  accessed_at: '2026-11-04T08:52:01.684840Z'
  support: supports
  summary: 'TIGR00711: DHA2 family efflux MFS transporter permease subunit; native
    type family. Broader homologous class is distinguished from the narrower named
    component; it is not silently substituted as an exact unresolved EmrK, EmrY or
    Dpb3 mapping.'
  snapshot_sha256: 64ebca0523316cf2b3a8f28d0002d62b30d42fdc4d08f0185bd0dac38d11296c
- evidence_id: micro-family-TIGR00998
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR00998/
  locator: Complete entry metadata/type, description flags and integrated signatures;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-TIGR00998.raw
  accessed_at: '2026-11-04T08:52:01.652616Z'
  support: supports
  summary: 'TIGR00998: EmrA/EmrK family multidrug efflux transporter periplasmic adaptor
    subunit; native type family. Broader homologous class is distinguished from the
    narrower named component; it is not silently substituted as an exact unresolved
    EmrK, EmrY or Dpb3 mapping.'
  snapshot_sha256: 6653c029cd39ecfce72b96666d4c2839fc67058ff8b4a91a1215825cb6ade00d
- evidence_id: micro-IPR051377-reviewed-retry
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051377/?page_size=200
  locator: Complete 15 reviewed-member identities, names, taxa and native genes; no
    next page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/IPR051377-reviewed-retry.raw
  accessed_at: '2026-11-04T08:56:22.524206Z'
  support: supports
  summary: Current family membership includes Q04603/DPB4 and homologous Dpb4/POLE3
    class members. Other complex associations and species-specific names are not erased;
    the family is not an exclusive Pol-epsilon membership assay.
  snapshot_sha256: 328683d246ad79b5e3568faf6c1f0774b6b07f3a1b60d4f1aabcbde50b793a3a
  search_scope: InterPro literal https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051377/?page_size=200;
    actual 2026-11-04T08:56:22.524206Z; IPR051377 reviewed proteins, page_size200,
    actual count15 with next=null. All15 identities read, bounded to this maintained
    response.
- evidence_id: micro-complex-CPX-4273
  kind: authority
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4273
  locator: 'Complete Complex Portal response: identity, organism, evidence, participant
    identifiers/roles/counts, properties and references; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/complex-CPX-4273.raw'
  accessed_at: '2026-11-04T08:49:09.344400Z'
  support: supports
  summary: CPX-4273 defines the E.coli K12 EmrKY-TolC tripartite efflux system using
    ECO0005547 curator inference. EmrK P52599 and EmrY P52600 have null copy numbers,
    TolC P02930 has count3; biological roles are unspecified. No constituent essentiality
    annotation is supplied. Source membership/inference does not equal direct experimental
    formation necessity.
  snapshot_sha256: bd52e87eee7859fba78183d5dfab8a1e0c5a8fd9edc2461d046bd629667f4aee
- evidence_id: micro-eco-0005547
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FECO_0005547
  locator: Complete native ECO identity, definition and explanatory description; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/eco-0005547.raw
  accessed_at: '2026-11-04T08:52:01.791716Z'
  support: supports
  summary: ECO0005547 is biological-system reconstruction based on background scientific
    knowledge in manual assertion; its description explicitly distinguishes inference
    from physical-interaction evidence. It is not an experimental assembly assay.
  snapshot_sha256: 5e079c708429feead41b2264cd1bf4f73131b706add51786aeaa9ad1f0de949b
- evidence_id: micro-doi-0
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2F0092-8674%2895%2990077-2%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-0.raw
  accessed_at: '2026-11-04T08:49:17.885284Z'
  support: supports
  summary: PMID 7758110; DOI 10.1016/0092-8674(95)90077-2; Posttranslational protein
    transport in yeast reconstituted with a purified complex of Sec proteins and Kar2p..
    Primary-study indexed abstract/metadata tier. Genuine separately inspected body
    evidence is named separately.
  snapshot_sha256: c078d3c76c438d15172456297b95b19e9844b678513e38084966bf6d9a4b0f0f
- evidence_id: micro-doi-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e03-06-0390%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-1.raw
  accessed_at: '2026-11-04T08:49:13.040864Z'
  support: supports
  summary: PMID 14617809; DOI 10.1091/mbc.e03-06-0390; Interactions between Sec complex
    and prepro-alpha-factor during posttranslational protein transport into the endoplasmic
    reticulum.. Primary-study indexed abstract/metadata tier. Genuine separately inspected
    body evidence is named separately.
  snapshot_sha256: 30a8c3d3db9ba0310378948fd91d3e0038e599bb029d4d13e0a4e0dfe6a56eda
- evidence_id: micro-doi-2
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-018-0856-x%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-2.raw
  accessed_at: '2026-11-04T08:49:13.178760Z'
  support: supports
  summary: PMID 30644436; DOI 10.1038/s41586-018-0856-x; Structure of the post-translational
    protein translocation machinery of the ER membrane.. Primary-study indexed abstract/metadata
    tier. Genuine separately inspected body evidence is named separately.
  snapshot_sha256: 5b83b3161de7d814cb1c107d97469c0f3b06a624305fc127efcdcd58528a7a94
- evidence_id: micro-doi-3
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1175088%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-3.raw
  accessed_at: '2026-11-04T08:49:13.252183Z'
  support: supports
  summary: PMID 19556461; DOI 10.1126/science.1175088; An ER-mitochondria tethering
    complex revealed by a synthetic biology screen.. Primary-study indexed abstract/metadata
    tier. Genuine separately inspected body evidence is named separately.
  snapshot_sha256: 2cb49ad8e51f8e4a3f83d22205ad06732177f9677e71755eb667f83940037237
- evidence_id: micro-doi-4
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.201704119%22&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/doi-4.raw
  accessed_at: '2026-11-04T08:49:13.366346Z'
  support: supports
  summary: PMID 29279306; DOI 10.1083/jcb.201704119; Structure-function insights into
    direct lipid transfer between membranes by Mmm1-Mdm12 of ERMES.. Primary-study
    indexed abstract/metadata tier. Genuine separately inspected body evidence is
    named separately.
  snapshot_sha256: 5999a2fff8c4ed6403eecabcdeb5f039bbb39e77fdd49027d40a2ba0af191063
- evidence_id: micro-pmid-11024162
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11024162+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-11024162.raw
  accessed_at: '2026-11-04T08:49:12.263634Z'
  support: supports
  summary: PMID 11024162; DOI 10.1093/nar/28.20.3846; Structure and function of the
    fourth subunit (Dpb4p) of DNA polymerase epsilon in Saccharomyces cerevisiae..
    Primary-study indexed abstract/metadata tier. Genuine separately inspected body
    evidence is named separately.
  snapshot_sha256: c52193fd1476f2e07313a65bfed7cdb9f36950bb667f27b0d229e791f70e21fe
- evidence_id: micro-pmid-12571237
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12571237+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-12571237.raw
  accessed_at: '2026-11-04T08:49:17.416220Z'
  support: supports
  summary: PMID 12571237; DOI 10.1074/jbc.m211818200; The quaternary structure of
    DNA polymerase epsilon from Saccharomyces cerevisiae.. Primary-study indexed abstract/metadata
    tier. Genuine separately inspected body evidence is named separately.
  snapshot_sha256: 9d96d112c7fa1c54ee17ff3ef0982445ff1bd8702fbe7f39ed87c2e20f130925
- evidence_id: micro-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-14562095.raw
  accessed_at: '2026-11-04T08:49:12.389657Z'
  support: supports
  summary: PMID 14562095; DOI 10.1038/nature02026; Global analysis of protein localization
    in budding yeast.. Primary-study indexed abstract/metadata tier. Genuine separately
    inspected body evidence is named separately.
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
- evidence_id: micro-pmid-15814431
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15814431+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-15814431.raw
  accessed_at: '2026-11-04T08:49:12.563166Z'
  support: supports
  summary: PMID 15814431; DOI 10.1080/10409230590935433; DNA polymerases that propagate
    the eukaryotic DNA replication fork.. Secondary review abstract only; not a primary
    experiment.
  snapshot_sha256: c77ff2fc9adad0c9e52e8918a491a053ae3fe0b8ea2ed637e0471942c77a6673
- evidence_id: micro-pmid-16369485
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16369485+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-16369485.raw
  accessed_at: '2026-11-04T08:49:12.711078Z'
  support: supports
  summary: PMID 16369485; DOI 10.1038/nsmb1040; Structure of Saccharomyces cerevisiae
    DNA polymerase epsilon by cryo-electron microscopy.. Primary-study indexed abstract/metadata
    tier. Genuine separately inspected body evidence is named separately.
  snapshot_sha256: 0f9769151808f49bcd65459c3b5bc2ca2c02f6dfdd8a51940ba7766f7d7fdf19
- evidence_id: micro-pmid-19721076
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19721076+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-19721076.raw
  accessed_at: '2026-11-04T08:49:12.190319Z'
  support: supports
  summary: PMID 19721076; DOI 10.1128/aac.00454-09; Induction of multidrug resistance
    mechanism in Escherichia coli biofilms by interplay between tetracycline and ampicillin
    resistance genes.. Primary-study indexed abstract/metadata tier. Genuine separately
    inspected body evidence is named separately.
  snapshot_sha256: a222692a71c69539635f7236da8bc111a5d50825385551ebda84afb7df4adf5a
- evidence_id: micro-pmid-25538242
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25538242+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-25538242.raw
  accessed_at: '2026-11-04T08:49:12.829423Z'
  support: supports
  summary: PMID 25538242; DOI 10.1074/jbc.m114.615278; Yeast DNA polymerase ϵ catalytic
    core and holoenzyme have comparable catalytic rates.. Primary-study indexed abstract/metadata
    tier. Genuine separately inspected body evidence is named separately.
  snapshot_sha256: dffdfcdb2721bbc950abc00df561b55a3d7a22b6baed26c8e7aceba9a7307530
- evidence_id: micro-pmid-9745046
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9745046+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact identifier metadata and complete indexed abstract; no article body
    inferred; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/pmid-9745046.raw
  accessed_at: '2026-11-04T08:49:12.611859Z'
  support: supports
  summary: PMID 9745046; DOI 10.1007/s004120050300; Eukaryotic DNA polymerases in
    DNA replication and DNA repair.. Secondary review abstract only; not a primary
    experiment.
  snapshot_sha256: b38d1baa2a4296cdb7b4d87ea5f642061e444f6f26599ec631e89c20c06f0950
- evidence_id: micro-PMC2772303-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2772303/
  locator: Methods sec2 strains and sec7 qPCR, complete Results/Discussion sec14 and
    sec15 with Figure4/5 text captions; text/captions only, no pixels, movies, supplements
    or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2772303-legacy.raw
  accessed_at: '2026-11-04T08:49:57.266214Z'
  support: supports
  summary: May2009 tests MG1655/pBR322 and a multi-locus modified OCL62 background
    with TetA(C) regulatory changes. EmrKY expression, biofilm and resistance phenotypes
    are context-specific; no isolated three-subunit formation assay is established.
    These limits do not establish component dispensability.
  snapshot_sha256: 2da93d85cfb8c578915258981cc9cf794cd5200a84245e7c0b4d6ad673c1dc66
- evidence_id: micro-PMC110797-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC110797/
  locator: Methods sec3/Table1 and sec5 purification, Results sec13–16 with Figure1/2
    captions, Discussion sec19; text/captions only, no pixels, movies, supplements
    or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC110797-legacy.raw
  accessed_at: '2026-11-04T08:49:57.251386Z'
  support: supports
  summary: Ohya identifies Dpb4 and tests dpb4-deletion preparations. After MonoQ
    chromatography Dpb2 and Dpb3 dissociate more readily from Pol2, with degradation/mixture
    limitations. This supports a bounded stability annotation, not universal ESSENTIAL,
    organism viability equivalence or complete intracellular complex absence.
  snapshot_sha256: 5d474eaa749f4f73c8aac6584ba74db7049e98ac0cb6b2990745e107c20c6c71
- evidence_id: micro-PMC307522-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC307522/
  locator: Methods sec3 purification/strains, sec6 binding, sec7 transport intermediates,
    sec8 denaturing immunoprecipitation; complete Results sec11 and Figure1/2 captions/Table1;
    text/captions only, no pixels, movies, supplements or atomic-data reanalysis;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC307522-legacy.raw
  accessed_at: '2026-11-04T08:49:57.238254Z'
  support: supports
  summary: Plath directly tests precursor interactions with Sec61 and Sec62, including
    a discriminating denaturing immunoprecipitation despite Sec62/Sec71 comigration.
    Initial binding and Kar2-dependent subsequent translocation are distinct. This
    supports the parent subcomplex topology without duplicating all individual proteins.
  snapshot_sha256: 0be85eaddef80770f9bbf182a292a312caf88fa7c3324baf54cc6486f80f1e91
- evidence_id: micro-PMC6367035-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6367035/
  locator: Main paragraphs5–19 including Figure1–3 text captions; Methods S2, S3,
    S4 and S6; text/captions only, no pixels, movies, supplements or atomic-data reanalysis;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC6367035-legacy.raw
  accessed_at: '2026-11-04T08:49:57.242380Z'
  support: supports
  summary: Wu2019 purifies the seven-component yeast Sec assembly from BY4741 and
    resolves its overall architecture at4.1Angstrom. Sec62 density/model coverage
    is limited, including docking/one membrane helix; the paper does not completely
    atomically resolve every Sec62 segment. No pixels, coordinates or supplementary
    methods were reanalyzed.
  snapshot_sha256: 3dc7e12338bb45f512d55c26b5caab8e7e9c15627fdbe9790b620139231631db
- evidence_id: micro-PMC2933203-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2933203/
  locator: Complete scientific main paragraphs4–29 and Figure1–4 text captions; paragraphs25–37
    additionally checked for terminal limits/reference boundary; text/captions only,
    no pixels, movies, supplements or atomic-data reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2933203-legacy.raw
  accessed_at: '2026-11-04T08:49:57.153851Z'
  support: supports
  summary: Kornmann identifies the Mmm1/Mdm10/Mdm12/Mdm34 core through the synthetic-tether
    screen and subsequent localization/rescue/association evidence. Mmm1 is ER-localized,
    Mdm10 also participates in SAM, and loss of core puncta is condition-scoped. Genetic
    lipid-flux and calcium context is not direct proof of every whole-complex transport
    mechanism.
  snapshot_sha256: 8afd424b147a38c5aef6ed4637c7eedcbc1bd1765fc17c35df6f62f8c7116082
- evidence_id: micro-PMC5839780-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5839780/
  locator: Introduction s01, complete Results s06 and s07 with Figure4–6 captions,
    Discussion s08/Figure7, Methods s11 strains and s18 lipid assays; text/captions
    only, no pixels, movies, supplements or atomic-data reanalysis; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC5839780-legacy.raw
  accessed_at: '2026-11-04T08:49:57.548153Z'
  support: supports
  summary: Kawano tests recombinant Mmm1-Mdm12 lipid transfer between model membranes,
    and separate yeast mutant heavy-membrane-fraction assays. K.lactis recombinant
    modules, S.cerevisiae Vps13-suppressed mutants and full in-vivo ERMES function
    remain distinct; carrier/conduit models are not settled universal mechanisms.
  snapshot_sha256: d64b554cdcedfb2582b299b65d88ffa136927284d35d2111405a44e94caa38a8
- evidence_id: micro-PMC4319046-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4319046/
  locator: Methods sec5–7 and Results sec16–18, sec20–21 including embedded Figure1–4/6–7
    captions and tables; text/captions only, no pixels, movies, supplements or atomic-data
    reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC4319046-legacy.raw
  accessed_at: '2026-11-04T08:49:57.700874Z'
  support: supports
  summary: Ganai compares purified whole Pol-epsilon with Pol2 core1–1228 in biochemical
    assays. Catalysis/processivity and loading effects are assay-specific; changes
    in accessory subunits and C-terminal sequence are not an isolated necessity test
    for each constituent.
  snapshot_sha256: 44bd21e229c2f31a703355872565c33cc683a578dc2926d08c4490fabbacd767
- evidence_id: micro-asturias2006-publisher
  kind: database
  reference: https://www.nature.com/articles/nsmb1040
  locator: Genuine publisher abstract/metadata only; article body is paywalled; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/asturias2006-publisher.raw
  accessed_at: '2026-11-04T08:52:02.884471Z'
  support: supports
  summary: Publisher page exposes abstract, citations and author metadata; it is not
    a fresh full-body read. The indexed abstract supports the broad Pol-epsilon architecture
    observation at its stated EM scope.
  snapshot_sha256: f279538d4ec18a1ee9d7fb2e83f0dbf33c6e131208b1e58d5749ffeaa6bb7130
- evidence_id: micro-access-PMC2772303-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2772303.1/PMC2772303.1.xml
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2772303-jats.receipt.json
    and response content
  accessed_at: '2026-11-04T08:49:13.112506Z'
  support: context_only
  summary: HTTP 404; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 34c2481d435671a5fe47cd0da242f2f00b792b6e1f9bd5c6a8be8b705c9173bf
- evidence_id: micro-access-PMC110797-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC110797.1/PMC110797.1.xml
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC110797-jats.receipt.json
    and response content
  accessed_at: '2026-11-04T08:49:13.114899Z'
  support: context_only
  summary: HTTP 404; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: b614f003db8620fa2c11b5161688626e38a85136da010fa449ec9f7e148dbe60
- evidence_id: micro-access-PMC2772303-epmc
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2772303/fullTextXML
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2772303-epmc.receipt.json
    and response content
  accessed_at: '2026-11-04T08:49:58.123952Z'
  support: context_only
  summary: HTTP 500; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 667915d520366632f0f4715f4857cb768f33d6e46091bfdd43e12a3d0fd35d1d
- evidence_id: micro-access-PMC110797-epmc
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC110797/fullTextXML
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC110797-epmc.receipt.json
    and response content
  accessed_at: '2026-11-04T08:50:03.170084Z'
  support: context_only
  summary: HTTP 500; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 3ea0265f6fee7a41829ecba7bd93f8c793e012318e45d29d03c3d84620d3e401
- evidence_id: micro-access-PMC307522-epmc
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC307522/fullTextXML
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC307522-epmc.receipt.json
    and response content
  accessed_at: '2026-11-04T08:49:57.710004Z'
  support: context_only
  summary: HTTP 500; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 5874aa893c9a79c10687494f87cfc684f19305f7b0e2fc9fea8ed781049c40ac
- evidence_id: micro-access-PMC2933203-epmc
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2933203/fullTextXML
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC2933203-epmc.receipt.json
    and response content
  accessed_at: '2026-11-04T08:50:15.329720Z'
  support: context_only
  summary: HTTP 500; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 79edda8730a9644b686ff29aba30bb9c231bb4aeaabf524bd2cd05e66319d6ca
- evidence_id: micro-access-PMC4319046-epmc
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4319046/fullTextXML
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/PMC4319046-epmc.receipt.json
    and response content
  accessed_at: '2026-11-04T08:50:03.768646Z'
  support: context_only
  summary: HTTP 500; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: c7ea47adcc8ba8bb6abd9652a25cca1a0966cb8918fdb2b56cf81d5acfbb45ee
- evidence_id: micro-access-panzner1995-publisher
  kind: validation
  reference: https://doi.org/10.1016/0092-8674(95)90077-2
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/panzner1995-publisher.receipt.json
    and response content
  accessed_at: '2026-11-04T08:49:57.950529Z'
  support: context_only
  summary: HTTP 200; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: d62d6ee5cca0a82a7b104f87b6d1535a6d4a5afa6cfff5bd98442dd6acb77cbe
- evidence_id: micro-access-panzner1995-pii
  kind: validation
  reference: https://www.cell.com/cell/fulltext/0092-8674(95)90077-2
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/panzner1995-pii.receipt.json
    and response content
  accessed_at: '2026-11-04T08:52:01.697862Z'
  support: context_only
  summary: HTTP 403; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 7adf95c72c175aab17af231f9927fb6a1c82fc9cf65d3bac9d8f80fcd95a1f83
- evidence_id: micro-access-chilkova2003-doi
  kind: validation
  reference: https://doi.org/10.1074/jbc.M211818200
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/chilkova2003-doi.receipt.json
    and response content
  accessed_at: '2026-11-04T08:52:01.635543Z'
  support: context_only
  summary: HTTP 200; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 7773de415306c5bf799f8f8f9a8f760a14a0c0f66bc7f25d150675a684554614
- evidence_id: micro-access-chilkova2003-correct-pdf
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(19)64558-8/pdf
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/chilkova2003-correct-pdf.receipt.json
    and response content
  accessed_at: '2026-11-04T08:56:20.644916Z'
  support: context_only
  summary: HTTP 403; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: dcc6bdec1341b976f4723b83157e8c33bd9bf675d07c15d76893d3f1dcf73b6d
- evidence_id: micro-access-family-IPR005694
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005694/
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/family-IPR005694.receipt.json
    and response content
  accessed_at: '2026-11-04T08:52:01.703901Z'
  support: context_only
  summary: HTTP 429; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-access-IPR051377-reviewed
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051377/?page_size=200
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/IPR051377-reviewed.receipt.json
    and response content
  accessed_at: '2026-11-04T08:52:01.785643Z'
  support: context_only
  summary: HTTP 429; access/status-only observation. Redirect, challenge, unavailable
    full text or rate limit is not scientific evidence. Successful genuine body or
    retried authority response is separately cited; no failed-route absence inference.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T08:49:08.706914Z'
  support: context_only
  summary: Twenty organism rows and28 organism/dataset pairs read. E.coli precise1k
    is covered; no Saccharomyces dataset appears in this exact response. No foreign-host
    proxy is used for the three yeast records.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB /api/datasets at 2026-11-04T08:49:08.706914Z;
    entire20-organism/28-pair response, exact maintained host matching. No biological-absence
    or future-coverage inference.
- evidence_id: micro-dataset-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete e_coli/precise1k metadata; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/dataset-meta.raw
  accessed_at: '2026-11-04T08:49:09.348690Z'
  support: context_only
  summary: Five strains BW25113,DGF-298,GMOS,MG1655,W3110;201 modules,1035 samples,518
    conditions,4257 genes. This is mixed-strain expression context, not the specific
    May OCL62/pBR322 experiment.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-dataset-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 module identifiers and native metadata; AI-generated summaries and
    activities excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/dataset-modules.raw
  accessed_at: '2026-11-04T08:49:08.707498Z'
  support: context_only
  summary: Complete inventory defines the bounded membership population. It does not
    supply direct binding, assembly, causal regulation or resistance assays.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: micro-dataset-genes
  kind: search
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=5000
  locator: Complete4257 reference-gene table, exact three maintained-locus joins;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/dataset-genes.raw
  accessed_at: '2026-11-04T08:49:08.836016Z'
  support: context_only
  summary: b2368=emrK/P52599,b2367=emrY/P52600,b3035=tolC/P02930. Only these exact
    joins are scientifically used; no all-gene functional audit is claimed.
  snapshot_sha256: db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27
  search_scope: Official iModulonDB literal https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=5000;
    actual 2026-11-04T08:49:08.836016Z; requested limit5000, actual4257 rows fully
    parsed, selected exact native loci b2368,b2367,b3035. No truncated-page absence
    inference.
- evidence_id: micro-membership-b2368
  kind: search
  reference: https://imodulondb.org/api/genes/b2368/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 returned membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/membership-b2368.raw
  accessed_at: '2026-11-04T08:49:59.814974Z'
  support: context_only
  summary: 'Exact b2368 has one thresholded hit: [{''k'': 38, ''weight'': 0.167808741,
    ''threshold'': 0.087369631}]. Other nonhits are not biological absence or dispensability.'
  snapshot_sha256: 499533a815fd0fe19bd94059ee21226aebd9a0e7ecdc9283b4137eaa904b7d74
  search_scope: Official iModulonDB literal https://imodulondb.org/api/genes/b2368/imodulons?organism=e_coli&dataset=precise1k;
    actual 2026-11-04T08:49:59.814974Z; exact e_coli/precise1k locus b2368, complete201-row
    response. No alias, organism-wide or historical extrapolation.
- evidence_id: micro-membership-b2367
  kind: search
  reference: https://imodulondb.org/api/genes/b2367/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 returned membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/membership-b2367.raw
  accessed_at: '2026-11-04T08:49:59.866136Z'
  support: context_only
  summary: 'Exact b2367 has one thresholded hit: [{''k'': 38, ''weight'': 0.122770016,
    ''threshold'': 0.087369631}]. Other nonhits are not biological absence or dispensability.'
  snapshot_sha256: b168874b29904ec9e4a2cd4c26b0576010624657572005e3c7293067a27e3745
  search_scope: Official iModulonDB literal https://imodulondb.org/api/genes/b2367/imodulons?organism=e_coli&dataset=precise1k;
    actual 2026-11-04T08:49:59.866136Z; exact e_coli/precise1k locus b2367, complete201-row
    response. No alias, organism-wide or historical extrapolation.
- evidence_id: micro-membership-b3035
  kind: search
  reference: https://imodulondb.org/api/genes/b3035/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 returned membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/membership-b3035.raw
  accessed_at: '2026-11-04T08:49:59.917184Z'
  support: context_only
  summary: 'Exact b3035 has one thresholded hit: [{''k'': 22, ''weight'': 0.033449641,
    ''threshold'': 0.030026006}]. Other nonhits are not biological absence or dispensability.'
  snapshot_sha256: 5db135045efa59ff66876f57b3e6ebe3c25375196fac7f1a410c36cb4befced3
  search_scope: Official iModulonDB literal https://imodulondb.org/api/genes/b3035/imodulons?organism=e_coli&dataset=precise1k;
    actual 2026-11-04T08:49:59.917184Z; exact e_coli/precise1k locus b3035, complete201-row
    response. No alias, organism-wide or historical extrapolation.
- evidence_id: micro-module-22
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22
  locator: Native metadata, threshold and all member IDs/weights; generated prose
    and activity vectors excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-22.raw
  accessed_at: '2026-11-04T08:52:01.177056Z'
  support: context_only
  summary: 'SoxS module22: 117 members. Exact retained loci corroborate bounded expression
    context only, not assembly, stoichiometry or component necessity.'
  snapshot_sha256: 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703
- evidence_id: micro-module-22-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes
  locator: All117 member identity/weight/threshold rows; exact selected-locus native
    accessions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-22-genes.raw
  accessed_at: '2026-11-04T08:52:01.183765Z'
  support: context_only
  summary: Member IDs and weights agree with module22 metadata; selected native identity
    joins agree with maintained examples. No direct regulatory or mechanistic inference.
  snapshot_sha256: 6e779e25e705f68403277aa34683af16a8dddfd4dc5fbe96fb6bdfc7117e20f0
- evidence_id: micro-module-38
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/38
  locator: Native metadata, threshold and all member IDs/weights; generated prose
    and activity vectors excluded; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-38.raw
  accessed_at: '2026-11-04T08:52:01.170321Z'
  support: context_only
  summary: 'EvgA module38: 15 members. Exact retained loci corroborate bounded expression
    context only, not assembly, stoichiometry or component necessity.'
  snapshot_sha256: 213e4645fd5ccc6f0cf5121180eb1e1531b7f19f40cb89c2a46474cebcf1cd83
- evidence_id: micro-module-38-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/38/genes
  locator: All15 member identity/weight/threshold rows; exact selected-locus native
    accessions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/module-38-genes.raw
  accessed_at: '2026-11-04T08:52:01.168297Z'
  support: context_only
  summary: Member IDs and weights agree with module38 metadata; selected native identity
    joins agree with maintained examples. No direct regulatory or mechanistic inference.
  snapshot_sha256: 4f5e72ffe840017401d6061df947ca60bd19f755f98105d3425b70b5fc6614f2
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z receipt
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical runner unavailable with exit1/PermissionError reading pyvenv.cfg;
    no new runner invocation. Actual present direct-source fallback is separate.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-emrky_tolc_multidrug_efflux_transport_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:38.410725Z'
  support: supports
  summary: Actual exit0; 3 maintained reviewed examples and 3 COVERED typed GENE_OR_PROTEIN
    nodes; all declared native node symbols are covered. Native success does not establish
    complete biological scope or exact family identity.
  snapshot_sha256: fb80174c5989232d6b217ecf063573b41d2950776f53aeb9647afabd699407ef
- evidence_id: micro-native-emrky_tolc_multidrug_efflux_transport_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal.log
    SHA256 8c7e3458522c33d3bce89abbe58b15f4f8f468d3b01f0625bd807e3e464c9a6c
  accessed_at: '2026-11-04T08:46:38.844933Z'
  support: supports
  summary: Actual exit0; 3 maintained reviewed examples and 3 COVERED typed GENE_OR_PROTEIN
    nodes; all declared native node symbols are covered. Native success does not establish
    complete biological scope or exact family identity.
  snapshot_sha256: 065e9c2878f170976fec2a17b171f1c185483c39c4bed34dfc8868919867f181
- evidence_id: micro-native-endoplasmic_reticulum_sec_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:39.270125Z'
  support: supports
  summary: Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN
    nodes; empty native inventory is not biological completeness. Native success does
    not establish complete biological scope or exact family identity.
  snapshot_sha256: be5eadca9efaf84653213ad12b97ebd43d701135a499dd2719073236536f33e7
- evidence_id: micro-native-endoplasmic_reticulum_sec_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T08:46:39.677275Z'
  support: supports
  summary: Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN
    nodes; empty native inventory is not biological completeness. Native success does
    not establish complete biological scope or exact family identity.
  snapshot_sha256: 5b4062d13eea1e0bc6472c87ece8413a362637a03c96e7efa10716219da0a82f
- evidence_id: micro-native-epsilon_dna_polymerase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:40.785727Z'
  support: supports
  summary: Actual exit0; 4 maintained reviewed examples and 4 COVERED typed GENE_OR_PROTEIN
    nodes; all declared native node symbols are covered. Native success does not establish
    complete biological scope or exact family identity.
  snapshot_sha256: 837689279a7f91d53ac11c8965c5bb15cea897553df75166ed8eb817a2132472
- evidence_id: micro-native-epsilon_dna_polymerase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-causal.log
    SHA256 6f8e9867949e29c1044c6f57d6788b7d019afd1c2891b5256df95d0edf86a29d
  accessed_at: '2026-11-04T08:46:41.197780Z'
  support: supports
  summary: Actual exit0; 4 maintained reviewed examples and 4 COVERED typed GENE_OR_PROTEIN
    nodes; all declared native node symbols are covered. Native success does not establish
    complete biological scope or exact family identity.
  snapshot_sha256: 5f55c1a0c57c1ed19b325a2610967d083feb752c435502eda34af81020f36164
- evidence_id: micro-native-ermes_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:41.611039Z'
  support: supports
  summary: Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN
    nodes; empty native inventory is not biological completeness. Native success does
    not establish complete biological scope or exact family identity.
  snapshot_sha256: 6f25a512fb3d7d518aafb5d24edef8655be98109ab5d8e8b794a9d2219db944d
- evidence_id: micro-native-ermes_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T08:46:42.015018Z'
  support: supports
  summary: Actual exit0; 0 maintained reviewed examples and 0 COVERED typed GENE_OR_PROTEIN
    nodes; empty native inventory is not biological completeness. Native success does
    not establish complete biological scope or exact family identity.
  snapshot_sha256: 4b550cdbfc82f3e8d1cbb0b494943a62dd23b8cb475173827ddef31d660ff5c9
- evidence_id: micro-emrky-independent-challenge
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/emrky-formation-attribution-challenge.json
  locator: Complete separate independent challenge, frozen inputs and actual source
    receipt bindings
  accessed_at: '2026-11-04T08:57:48.543938Z'
  support: supports
  summary: Independent reviewer corroborates rejection of the original blanket mandatory-UNKNOWN/isolated-proof
    major as formulated, while confirming the new narrow CPX attribution defect. No
    experimental necessity or dispensability certification and no automatic enum change.
  snapshot_sha256: 11450c71dd784d621af7721da96709cc256c5e71444f77bd30ebb3a108d7fbc5
- evidence_id: plaque-curation
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-field-guide
  kind: authority
  reference: docs/SCHEMA.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-protein-skill
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-graph-skill
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: plaque-review-contract
  kind: authority
  reference: docs/record-reviews.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: plaque-structure-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-agents
  kind: authority
  reference: AGENTS.md
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
- evidence_id: plaque-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Frozen native policy/schema, including component-class identity, source
    applicability, formation versus function and append-only rationale
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Apply current native contract without inventing mandatory examples, universal
    formation assays or a prohibition on broad protein groups. Preserve dated rationale;
    assess current claims separately.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: plaque-record-4
  kind: record_content
  reference: data/structures/other/escrt_0_complex.yaml
  locator: Complete current definition, components, taxa, examples, functions, graphs,
    discussions and history
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: supports
  summary: All maintained assertions read; current target bytes equal the original
    frozen target. No scientific record was changed.
  snapshot_sha256: 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d
- evidence_id: plaque-original-4-yaml
  kind: prior_review
  reference: reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.yaml
  locator: Complete immutable original, historical inputs/checks/evidence/findings/actions
    and exact rendered Markdown
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Original scope and timestamp are historical. Source findings are independently
    reassessed at the present source head.
  snapshot_sha256: f6cdeb862fc3fd639002e5b6ff1261ec9ac6ff4ebd447255157bacc24d051e97
- evidence_id: plaque-original-4-md
  kind: prior_review
  reference: reviews/structured/20261022T063722Z-escrt-0-complex-audit/review.md
  locator: Complete immutable original, historical inputs/checks/evidence/findings/actions
    and exact rendered Markdown
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Original scope and timestamp are historical. Source findings are independently
    reassessed at the present source head.
  snapshot_sha256: dd332a4830bc278269eef9f8ac5d2b9f3e8cd4f44d9d65851a84083c7bc08207
- evidence_id: plaque-record-5
  kind: record_content
  reference: data/structures/other/escrt_complex.yaml
  locator: Complete current definition, components, taxa, examples, functions, graphs,
    discussions and history
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: supports
  summary: All maintained assertions read; current target bytes equal the original
    frozen target. No scientific record was changed.
  snapshot_sha256: 355f25710a97cee7e56f5b1438b71d21194f6130f84904091250df6e695bd17e
- evidence_id: plaque-original-5-yaml
  kind: prior_review
  reference: reviews/structured/20261022T063722Z-escrt-complex-audit/review.yaml
  locator: Complete immutable original, historical inputs/checks/evidence/findings/actions
    and exact rendered Markdown
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Original scope and timestamp are historical. Source findings are independently
    reassessed at the present source head.
  snapshot_sha256: 1d2c52c200d099f4cedcfd01f46ee022bfffeeade757a64c49e42beb4dccb6de
- evidence_id: plaque-original-5-md
  kind: prior_review
  reference: reviews/structured/20261022T063722Z-escrt-complex-audit/review.md
  locator: Complete immutable original, historical inputs/checks/evidence/findings/actions
    and exact rendered Markdown
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Original scope and timestamp are historical. Source findings are independently
    reassessed at the present source head.
  snapshot_sha256: 0855139ad291ec4234fd24b0199db8193af11798cebfd6504669b4c1105f66cc
- evidence_id: plaque-record-6
  kind: record_content
  reference: data/structures/other/escrt_i_complex.yaml
  locator: Complete current definition, components, taxa, examples, functions, graphs,
    discussions and history
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: supports
  summary: All maintained assertions read; current target bytes equal the original
    frozen target. No scientific record was changed.
  snapshot_sha256: 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc
- evidence_id: plaque-original-6-yaml
  kind: prior_review
  reference: reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.yaml
  locator: Complete immutable original, historical inputs/checks/evidence/findings/actions
    and exact rendered Markdown
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Original scope and timestamp are historical. Source findings are independently
    reassessed at the present source head.
  snapshot_sha256: 3022dba13fbac6b42465e752dfc072bafb8981a6a446d32263da703330406382
- evidence_id: plaque-original-6-md
  kind: prior_review
  reference: reviews/structured/20261022T063723Z-escrt-i-complex-audit/review.md
  locator: Complete immutable original, historical inputs/checks/evidence/findings/actions
    and exact rendered Markdown
  accessed_at: '2026-11-04T08:56:36.750325Z'
  support: context_only
  summary: Original scope and timestamp are historical. Source findings are independently
    reassessed at the present source head.
  snapshot_sha256: 2d3e9d37421d323c120a6e11f2f0c71697fc34b9044c827989bc86966c5696ea
- evidence_id: plaque-input-original-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/input-original-proof.json
  locator: Actual explicit-commit proof;47 current source/worktree inputs,41 historical
    input occurrences and3 native original validate/render pairs
  accessed_at: '2026-11-04T08:50:42.592695Z'
  support: supports
  summary: All hashes match; own3 target hashes are nonstale. All3 original YAML files
    natively validate and exactly reproduce saved Markdown. Other cohort inputs are
    checked for provenance only.
  snapshot_sha256: 1733d91a456e57162dae4a6c77b94acab62541a80b8099a9dbf17b98cbf34596
- evidence_id: plaque-native-escrt_0_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-verify.log;
    stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:43.148381Z'
  support: supports
  summary: Exit0. Two reviewed protein_examples and two COVERED typed protein nodes.
    Identifier and node-coverage checks do not independently establish biological
    assembly, localization or necessity.
  snapshot_sha256: 5da12f6992c0aaf9198aabe0e8cca520d70ae1fb7360217b3e75350dbd770489
- evidence_id: plaque-native-escrt_0_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-causal.log;
    stdout SHA256 8d965b4762c6f13e759cf9a9f2c993dde6bd0f8922fe5998302d843e0f3efa5e
  accessed_at: '2026-11-04T08:46:43.558182Z'
  support: supports
  summary: Exit0. Two reviewed protein_examples and two COVERED typed protein nodes.
    Identifier and node-coverage checks do not independently establish biological
    assembly, localization or necessity.
  snapshot_sha256: 8ece0dac3ce9e9d83d9e224fc738fc824b230a9c27d94285f73796b405b4f292
- evidence_id: plaque-native-escrt_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-verify.log;
    stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:43.968124Z'
  support: supports
  summary: Exit0. Zero protein_examples and zero typed protein nodes; positive pathway
    assertions remain subject to source review. Identifier and node-coverage checks
    do not independently establish biological assembly, localization or necessity.
  snapshot_sha256: 29b3135a55b260fa5945888bfcbc0b9b7b3b987eea7460da5926e758e57c2a13
- evidence_id: plaque-native-escrt_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-causal.log;
    stdout SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T08:46:44.371047Z'
  support: supports
  summary: Exit0. Zero protein_examples and zero typed protein nodes; positive pathway
    assertions remain subject to source review. Identifier and node-coverage checks
    do not independently establish biological assembly, localization or necessity.
  snapshot_sha256: e65d455671a750d3daee265dc8f82c22177f6092b44ba69197cbb511261ef292
- evidence_id: plaque-native-escrt_i_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-verify-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-verify.log;
    stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T08:46:45.868230Z'
  support: supports
  summary: Exit0. Three reviewed protein_examples; four typed protein nodes comprise
    three COVERED constituents and the external Vps27 recruiter UNANCHORED_WITH_UNIPROT
    P40343. This intentional external actor is not a missing constituent. Identifier
    and node-coverage checks do not independently establish biological assembly, localization
    or necessity.
  snapshot_sha256: 305599a0d9fa39933405870f7d3fa42e2d083a1e34af22de003debab6be08511
- evidence_id: plaque-native-escrt_i_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-causal-receipt.json
  locator: Actual command receipt; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-causal.log;
    stdout SHA256 aac6b7401b494f165148fbd63ff7a1fd22fde5cb5693ccd03f0e928f51a82f2e
  accessed_at: '2026-11-04T08:46:46.276063Z'
  support: supports
  summary: Exit0. Three reviewed protein_examples; four typed protein nodes comprise
    three COVERED constituents and the external Vps27 recruiter UNANCHORED_WITH_UNIPROT
    P40343. This intentional external actor is not a missing constituent. Identifier
    and node-coverage checks do not independently establish biological assembly, localization
    or necessity.
  snapshot_sha256: cab0d39542fd91c866946528e74898efeafddbaa997cf22b553929c67c858f01
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033565,GO:0036452,GO:0000813,GO:0005768,GO:0010008,GO:0032991,GO:0071985,GO:0000814,GO:0000815,GO:1990621
  locator: 'Complete10-term response: exact names/definitions/synonyms and selected
    typed children for all target, parent, localization, function and five child identities;
    retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go.raw'
  accessed_at: '2026-11-04T08:50:30.353310Z'
  support: supports
  summary: Current GO0033565 still says Vps1p while its exact synonym names Vps27p-Hse1p.
    Generic ESCRT has five distinct is_a child classes; the typed GO0005768 children
    confirm generic ESCRT part_of endosome, and GO0010008 confirms ESCRT-I part_of
    endosome membrane. GO0071985 defines MVB sorting; no direct parthood is inferred
    merely from an ancestor list.
  snapshot_sha256: 8120697c94bfde5b749ca494a9d5ed8040f23bb617c3b16f93ecfe6e13676467
- evidence_id: plaque-go-0033565-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033565/ancestors?relations=is_a
  locator: Complete relations=is_a array for GO:0033565; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go-0033565-ancestors.raw
  accessed_at: '2026-11-04T08:50:30.353617Z'
  support: supports
  summary: The is_a-only ancestor response supports the target hierarchy; it supplies
    no independent direct parthood assertion.
  snapshot_sha256: c3f01e5a48d89d949fd4ce84c08c674afb30f56499442c1604ec361e62f72aa7
- evidence_id: plaque-go-0036452-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036452/ancestors?relations=is_a
  locator: Complete relations=is_a array for GO:0036452; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go-0036452-ancestors.raw
  accessed_at: '2026-11-04T08:50:30.353716Z'
  support: supports
  summary: The is_a-only ancestor response supports the target hierarchy; it supplies
    no independent direct parthood assertion.
  snapshot_sha256: 670982463b4374a0bbf92d464fc2199259f236006ccaec317228e17444f294c5
- evidence_id: plaque-go-0000813-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813/ancestors?relations=is_a
  locator: Complete relations=is_a array for GO:0000813; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/go-0000813-ancestors.raw
  accessed_at: '2026-11-04T08:50:30.353786Z'
  support: supports
  summary: The is_a-only ancestor response supports the target hierarchy; it supplies
    no independent direct parthood assertion.
  snapshot_sha256: fa49f433545d7947ef44e9ec5541c54ab9935ff19ee26462ac2bbb9f45f1a4a5
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: 'Complete native ENA response: ID/name/rank/lineage; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/tax-4932.raw'
  accessed_at: '2026-11-04T08:50:30.353838Z'
  support: supports
  summary: S. cerevisiae species4932 and S288C reference strain559292 are distinct
    from the SEY6210-derived experimental preparations. No quantitative prevalence
    census follows.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: 'Complete native ENA response: ID/name/rank/lineage; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/tax-559292.raw'
  accessed_at: '2026-11-04T08:50:30.353878Z'
  support: supports
  summary: S. cerevisiae species4932 and S288C reference strain559292 are distinct
    from the SEY6210-derived experimental preparations. No quantitative prevalence
    census follows.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-pmid-12006563
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12006563+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:12006563 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-12006563.raw
  accessed_at: '2026-11-04T08:50:33.906046Z'
  support: supports
  summary: Stahelin2002 primary abstract concerns isolated yeast Vps27 and Drosophila
    Hrs FYVE-domain membrane binding, SPR and monolayer penetration; not whole-cell
    ESCRT assembly.
  snapshot_sha256: 721ff7b1e8be0aac07a3f1b805172fedecf83c94d87959279537e770104f762c
- evidence_id: plaque-pmid-12055639
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12055639+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:12055639 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-12055639.raw
  accessed_at: '2026-11-04T08:50:34.435108Z'
  support: supports
  summary: Bilodeau2002 primary abstract explicitly identifies the yeast Vps27p/Hse1p
    complex, endosomal localization, Ub binding, Golgi recycling/lumenal-membrane
    function and UIM-mutant sorting separation. This directly contradicts the copied
    Vps1 constituent wording.
  snapshot_sha256: ee827af6d2fca666872d3e3bf3af29383b0c71ef89f1b113bc2820543668b7f0
- evidence_id: plaque-pmid-12900393
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12900393+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:12900393 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-12900393.raw
  accessed_at: '2026-11-04T08:50:34.524715Z'
  support: supports
  summary: Katzmann2003 primary abstract identifies Vps27-specific endosomal ESCRT-I
    recruitment; separately inspected body sections give the actual strain and assay
    scope.
  snapshot_sha256: cc2f9af2f12eaf48b6e58d237b18a769e342731ff79c963dc48a4aa40c7dd903
- evidence_id: plaque-pmid-14562095
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:14562095 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-14562095.raw
  accessed_at: '2026-11-04T08:50:34.876943Z'
  support: supports
  summary: Huh2003 primary abstract describes tagged-yeast protein localization survey.
    Individual images were not inspected; exact annotation provenance is checked in
    native UniProt instead.
  snapshot_sha256: 29fa7e6d8ea5e645642a360565a0b71b2fb9041aab05012b6826702cf86793b1
- evidence_id: plaque-pmid-21763610
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21763610+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:21763610 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-21763610.raw
  accessed_at: '2026-11-04T08:50:34.989603Z'
  support: supports
  summary: Henne2011 is a secondary review. Its complete abstract supports the broad
    cargo-recognition/membrane-sculpting framework, MVB biogenesis, retroviral budding
    and cytokinetic abscission; it does not certify detailed main-body subunit mechanisms.
  snapshot_sha256: 54062d7e12cf799adc9a421b8b6ca0ecfdad7bd7cdc485618d875a99974e4a4e
- evidence_id: plaque-pmid-11511343
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11511343+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:11511343 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-11511343.raw
  accessed_at: '2026-11-04T08:50:35.040080Z'
  support: supports
  summary: Katzmann2001 primary abstract identifies the original Vps23/Vps28/Vps37
    yeast core and a reported350kDa complex. This is historically scoped apparent-complex
    characterization, not modern exhaustive composition or an exact physical copy-number
    claim.
  snapshot_sha256: 5ed037f07800fc0b7b503243aea71978a08f57673877534beea080fd6fc31aae
- evidence_id: plaque-pmid-9790597
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9790597+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:9790597 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-9790597.raw
  accessed_at: '2026-11-04T08:50:35.143283Z'
  support: supports
  summary: Hong1998 primary abstract identifies Srn10/Srn2 suppressor and cytoplasmic
    localization by immunofluorescence. Viability dispensability is not identical
    to ESCRT-I assembly necessity.
  snapshot_sha256: a592ae79f8f1f96610e7a3a80802aa3240abc21263f36560e8d3bd099786ae82
- evidence_id: plaque-pmid-17145965
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17145965+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:17145965 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-17145965.raw
  accessed_at: '2026-11-04T08:50:35.598552Z'
  support: supports
  summary: Chu2006 primary abstract positively identifies Mvb12 and assembly-regulation
    context; selected body sections below independently confirm membership and experimental
    strains.
  snapshot_sha256: 034c686ca6cf3924f79aa0a17569c0617fc803b4e0778abed325f45a7cd90002
- evidence_id: plaque-pmid-17135292
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17135292+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact EXT_ID:17135292 AND SRC:MED; pageSize1/resultType core;
    full unique returned bibliography and abstract only, not linked body; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/pmid-17135292.raw
  accessed_at: '2026-11-04T08:50:35.685886Z'
  support: supports
  summary: Curtiss2007 primary abstract positively identifies Mvb12 and its association/sorting/release
    functions; selected body sections below bound the physical evidence.
  snapshot_sha256: a17776e7dc66fd60d4e43eaeedcb29dec325369e0cb52e7eeecff98c4d104ac5
- evidence_id: plaque-bilodeau-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/ncb815
  locator: Publisher title/authors/DOI, complete Abstract, access notice and section
    headings; no Results/Methods or pixels; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/bilodeau-publisher.raw
  accessed_at: '2026-11-04T08:50:36.206669Z'
  support: supports
  summary: The current Nature page exposes a genuine abstract and bibliography, followed
    by a subscription-preview notice. It is not the historical challenge response
    and does not grant full-body access.
  snapshot_sha256: 0e6e57d4b3a048924c4cee5b6875e7bf31b59b34ca47ddd24a610f46b4626843
- evidence_id: plaque-henne-publisher
  kind: validation
  reference: https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00240-3
  locator: Actual HTTP403 transport response and adjacent receipt only; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/henne-publisher.raw
  accessed_at: '2026-11-04T08:51:47.580928Z'
  support: context_only
  summary: The attempted publisher fulltext route returned403. No Henne main-body
    reading is claimed; the exact native MED abstract is separate secondary evidence.
  snapshot_sha256: 1eb9c026fd2420f9323e33e82d8e943c0dafc0b163326a1a41465d03894d6db0
- evidence_id: plaque-PMC2172707-body
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2172707/
  locator: Genuine NCBI legacy HTML; Abstract, Results sec3–7, Discussion sec9–10,
    Methods sec12–15; embedded text captions Figs1–7. SEY6210 and explicit derivatives;
    no figure pixels or raw experiments reanalysed.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/PMC2172707-body.raw
  accessed_at: '2026-11-04T08:50:35.991499Z'
  support: supports
  summary: Katzmann2003 supports independent Ub binding, Vps27/PI3P-dependent ESCRT-I
    recruitment, membrane-specific reciprocal association and C-terminal recruitment
    defects. Hse1-dependent whole-complex recruitment is not substituted for the specifically
    tested Vps27 actor. Discussion distinguishes model proposals from measured interactions
    and labels selected observations unpublished.
  snapshot_sha256: c7e6302d011ecaa0cc18fa56e9c0df30936209b6031ba9cb11f613d65238cd15
- evidence_id: plaque-PMC2064680-body
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2064680/
  locator: Genuine NCBI legacy HTML; Abstract, Results sec3 with Figs1/2 text captions;
    Methods sec9/11/13. Other oligomer-model Results/Discussion, supplemental alignment
    and pixels not inspected.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/PMC2064680-body.raw
  accessed_at: '2026-11-04T08:50:36.001867Z'
  support: supports
  summary: Chu2006 gel filtration/co-IP identify Mvb12 as an additional ESCRT-I member;
    partial cargo-sorting defects differ from core deletions. The current record acknowledges
    this later member. SEY6210-derived assays and recombinant E.coli production are
    distinct; expression host is not the natural record taxon.
  snapshot_sha256: 09fe0734cff46087c6126092d0f8628fbf8e9e8f464a912ce7abbef58e2f5f84
- evidence_id: plaque-PMC1783790-body
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1783790/
  locator: Genuine NCBI legacy HTML; Abstract, Methods sec4/Table1 and sec6, Results
    sec10–11 with embedded Figs2/3/4/7 text captions. Specific SEY6210 derivatives
    and control strains read; no figure pixels, supplement or complete other Results
    certified.; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/PMC1783790-body.raw
  accessed_at: '2026-11-04T08:50:36.103606Z'
  support: supports
  summary: Curtiss2007 reciprocal purification and gel filtration support Mvb12 membership.
    In vps37 deletion, a Vps23/Vps28 subcomplex persists while Mvb12 becomes unstable
    and fails to associate in the tested assays; localization/sorting and individual
    universal formation necessity remain separate. Apparent gel-filtration masses
    are not exact stoichiometry.
  snapshot_sha256: c21d1d40b5e3ccbad5cd8513f56bda61f0ae27ece562655612d057e4eb43c864
- evidence_id: plaque-up-P40343
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40343.json
  locator: Native primaryAccession, entryType, genes/locus/taxon, comments and family
    cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-P40343.raw
  accessed_at: '2026-11-04T08:50:30.353914Z'
  support: supports
  summary: Reviewed S288C559292 P40343 has primary gene VPS27, matching VPS27 name/alias
    and locus YNR006W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family
    cross-references were inspected. Native annotation provenance is distinguished
    from fresh primary experiments and reference strain from assay strains.
  snapshot_sha256: 9722b86a9641dd5d053f0babc34f530ea7656e19571069c2eb081537e836c344
- evidence_id: plaque-gene-VPS27
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-result response; no identity inferred from search rank; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS27.raw
  accessed_at: '2026-11-04T08:50:30.975812Z'
  support: supports
  summary: Exactly one reviewed S288C result matches P40343, with correct primary
    name, aliases and locus.
  snapshot_sha256: f10595f20fb986f3ccc9d43fbbf528da993ebe082fa89523582413ba156507f3
  search_scope: UniProt REST; query=(gene_exact:VPS27) AND (organism_id:559292) AND
    (reviewed:true); size500; actual date 2026-11-04T08:50:30.975812Z; full returned
    result read, no unreviewed or descendant-taxon expansion. Database search, not
    filesystem absence.
- evidence_id: plaque-up-P38753
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38753.json
  locator: Native primaryAccession, entryType, genes/locus/taxon, comments and family
    cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-P38753.raw
  accessed_at: '2026-11-04T08:50:30.353949Z'
  support: supports
  summary: Reviewed S288C559292 P38753 has primary gene HSE1, matching HSE1 name/alias
    and locus YHL002W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family
    cross-references were inspected. Native annotation provenance is distinguished
    from fresh primary experiments and reference strain from assay strains.
  snapshot_sha256: 1f241d071d6810f0ea8db2fc2c85bf81395fe6b26fc4478f857d489959df64df
- evidence_id: plaque-gene-HSE1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHSE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-result response; no identity inferred from search rank; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-HSE1.raw
  accessed_at: '2026-11-04T08:50:31.004090Z'
  support: supports
  summary: Exactly one reviewed S288C result matches P38753, with correct primary
    name, aliases and locus.
  snapshot_sha256: ca4f65f91959cfcb0c0c1d6967f5920310daf04d297b98e47dd1fd739f33f8a8
  search_scope: UniProt REST; query=(gene_exact:HSE1) AND (organism_id:559292) AND
    (reviewed:true); size500; actual date 2026-11-04T08:50:31.004090Z; full returned
    result read, no unreviewed or descendant-taxon expansion. Database search, not
    filesystem absence.
- evidence_id: plaque-up-P25604
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P25604.json
  locator: Native primaryAccession, entryType, genes/locus/taxon, comments and family
    cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-P25604.raw
  accessed_at: '2026-11-04T08:50:30.952715Z'
  support: supports
  summary: Reviewed S288C559292 P25604 has primary gene STP22, matching VPS23 name/alias
    and locus YCL008C. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family
    cross-references were inspected. Native annotation provenance is distinguished
    from fresh primary experiments and reference strain from assay strains.
  snapshot_sha256: b0de38ad67a24e89fe41e94bc13c5f5b5ea036f0d6ccb504d5ce622bf3577414
- evidence_id: plaque-gene-VPS23
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS23%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-result response; no identity inferred from search rank; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS23.raw
  accessed_at: '2026-11-04T08:50:31.019796Z'
  support: supports
  summary: Exactly one reviewed S288C result matches P25604, with correct primary
    name, aliases and locus.
  snapshot_sha256: 78cf1cdca34d69ad9d69d07c9a9dccc711cf406e25b50ee2c0525a4ba80b3f92
  search_scope: UniProt REST; query=(gene_exact:VPS23) AND (organism_id:559292) AND
    (reviewed:true); size500; actual date 2026-11-04T08:50:31.019796Z; full returned
    result read, no unreviewed or descendant-taxon expansion. Database search, not
    filesystem absence.
- evidence_id: plaque-up-Q02767
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q02767.json
  locator: Native primaryAccession, entryType, genes/locus/taxon, comments and family
    cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-Q02767.raw
  accessed_at: '2026-11-04T08:50:30.967685Z'
  support: supports
  summary: Reviewed S288C559292 Q02767 has primary gene VPS28, matching VPS28 name/alias
    and locus YPL065W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family
    cross-references were inspected. Native annotation provenance is distinguished
    from fresh primary experiments and reference strain from assay strains.
  snapshot_sha256: 56eebce70745b9c33357034221b182eb78ae00ce98a3b799854449f0374a0109
- evidence_id: plaque-gene-VPS28
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS28%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-result response; no identity inferred from search rank; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS28.raw
  accessed_at: '2026-11-04T08:50:31.205267Z'
  support: supports
  summary: Exactly one reviewed S288C result matches Q02767, with correct primary
    name, aliases and locus.
  snapshot_sha256: 9fdd0fc16a9ff02fd6fff17d3d0e65fd12df239b284b1bcef5e197468b39d640
  search_scope: UniProt REST; query=(gene_exact:VPS28) AND (organism_id:559292) AND
    (reviewed:true); size500; actual date 2026-11-04T08:50:31.205267Z; full returned
    result read, no unreviewed or descendant-taxon expansion. Database search, not
    filesystem absence.
- evidence_id: plaque-up-Q99176
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q99176.json
  locator: Native primaryAccession, entryType, genes/locus/taxon, comments and family
    cross-references; locality ECO/PMID attribution read; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/up-Q99176.raw
  accessed_at: '2026-11-04T08:50:30.967778Z'
  support: supports
  summary: Reviewed S288C559292 Q99176 has primary gene SRN2, matching VPS37 name/alias
    and locus YLR119W. Full relevant FUNCTION/SUBUNIT/LOCATION/SIMILARITY and family
    cross-references were inspected. Native annotation provenance is distinguished
    from fresh primary experiments and reference strain from assay strains.
  snapshot_sha256: bea0740414b183a72cc53af6a86151fd0d79fcb6e3dc8984e880eef4ccc34322
- evidence_id: plaque-gene-VPS37
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS37%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-result response; no identity inferred from search rank; retained
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/gene-VPS37.raw
  accessed_at: '2026-11-04T08:50:31.711116Z'
  support: supports
  summary: Exactly one reviewed S288C result matches Q99176, with correct primary
    name, aliases and locus.
  snapshot_sha256: 66cf662eb6731268cc492fcc3e7732b758ceea8a6bf835e99c96079810b423ec
  search_scope: UniProt REST; query=(gene_exact:VPS37) AND (organism_id:559292) AND
    (reviewed:true); size500; actual date 2026-11-04T08:50:31.711116Z; full returned
    result read, no unreviewed or descendant-taxon expansion. Database search, not
    filesystem absence.
- evidence_id: plaque-ipr-IPR017073
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017073/
  locator: Complete native InterPro accession/type/name/member signatures/hierarchy
    and description flags; full-protein membership joined to native UniProt where
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR017073.raw
  accessed_at: '2026-11-04T08:50:32.049002Z'
  support: supports
  summary: Whole Hrs/Vps27 protein family, not the shared VHS/FYVE/UIM domains. Current
    native P40343 independently carries the exact cross-reference.
  snapshot_sha256: 8e903eb9fb7c4c985f359ae9bf3a22fb5ff31bc932b898e9f77e68cbcaf23f05
- evidence_id: plaque-ipr-IPR050670
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050670/
  locator: Complete native InterPro accession/type/name/member signatures/hierarchy
    and description flags; full-protein membership joined to native UniProt where
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR050670.raw
  accessed_at: '2026-11-04T08:50:32.081240Z'
  support: supports
  summary: STAM-labelled family integrates PTHR45929 but generated unchecked narrative
    is excluded; actual reviewed membership includes other named protein classes,
    so it is not forced as exact Hse1/STAM-only grounding.
  snapshot_sha256: 65084d8e26b85f7e864b9f77d99a0742b7b6a3f3de014b6a1d9472081fa4ab47
- evidence_id: plaque-ipr-IPR052070
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052070/
  locator: Complete native InterPro accession/type/name/member signatures/hierarchy
    and description flags; full-protein membership joined to native UniProt where
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR052070.raw
  accessed_at: '2026-11-04T08:50:32.657155Z'
  support: supports
  summary: Typed family with PTHR23306 despite the UEV-domain-containing label. Unchecked
    generated text is excluded; native P25604 and bounded seven-member reviewed query
    establish the Vps23/TSG101 class.
  snapshot_sha256: f7143f6883f4fc55f1725e57924b274e8b641a7ac8c6dac96c0f3cd5a893ca52
- evidence_id: plaque-ipr-IPR007143
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007143/
  locator: Complete native InterPro accession/type/name/member signatures/hierarchy
    and description flags; full-protein membership joined to native UniProt where
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR007143.raw
  accessed_at: '2026-11-04T08:50:32.679975Z'
  support: supports
  summary: Vps28 full-protein family with PTHR12937/PIRSF017535/PF03997 and native
    Q02767 match. Its older three-member prose is not used to deny Mvb12.
  snapshot_sha256: 621f858f83fc3e354313fc64712b5662381288c28e559bbe14d01f7478671392
- evidence_id: plaque-ipr-IPR017435
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017435/
  locator: Complete native InterPro accession/type/name/member signatures/hierarchy
    and description flags; full-protein membership joined to native UniProt where
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR017435.raw
  accessed_at: '2026-11-04T08:50:33.064676Z'
  support: supports
  summary: Fungal Vps37 family with PIRSF038214 and Q99176 membership matches the
    explicitly yeast component. It is not advertised as encompassing all metazoan
    paralogs; internally inconsistent heterotrimer/four-name prose is not stoichiometry
    evidence.
  snapshot_sha256: f2d3d4e441882ac4060dc165dd83002031f749a5dd4133885bfecddaee9c1b8c
- evidence_id: plaque-ipr-IPR009851
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009851/
  locator: Complete native InterPro accession/type/name/member signatures/hierarchy
    and description flags; full-protein membership joined to native UniProt where
    claimed; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/ipr-IPR009851.raw
  accessed_at: '2026-11-04T08:50:33.253992Z'
  support: supports
  summary: Modr/Vps37 C-terminal domain; not an exact whole Vps37 family substitute.
  snapshot_sha256: c2d25396c63d914ec06fc97ba1cd581577695fc05a27b11e9a4646b7c87b830d
- evidence_id: plaque-panther-PTHR45929
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/
  locator: Native name/integration/member metadata and LLM flags; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/panther-PTHR45929.raw
  accessed_at: '2026-11-04T08:50:33.304457Z'
  support: context_only
  summary: Broad STAM family metadata does not override the independently observed
    mixed reviewed-member boundary. Unchecked generated narrative is excluded.
  snapshot_sha256: 18df9f78e94f3b6f49a8a05e5c4f8f75b864b76e262e038520e77d309fdb8d11
- evidence_id: plaque-members-IPR050670
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR050670/?page_size=200
  locator: Complete38 metadata identities, next=null; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/members-IPR050670.raw
  accessed_at: '2026-11-04T08:50:33.687496Z'
  support: context_only
  summary: All38 reviewed returned members include Hse1/STAM but also SHO1, LSB1,
    PIN3, csh3, mug137 and SH3D21 identities. This establishes a broader returned
    boundary, not a proposed exact Hse1 class.
  snapshot_sha256: 403af0a94db6054becb0842d813a37911fea6dfc551d0b6b7d45c86bdd078547
  search_scope: InterPro reviewed-protein endpoint restricted to entry IPR050670;
    page_size200; actual date 2026-11-04T08:50:33.687496Z; all38 returned accession/name/gene/taxon
    rows read, next=null. No sequence or unreviewed search; no global absence conclusion.
- evidence_id: plaque-members-IPR052070
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR052070/?page_size=200
  locator: Actual HTTP429 response/receipt only; retained snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/members-IPR052070.raw
  accessed_at: '2026-11-04T08:50:33.854354Z'
  support: context_only
  summary: The InterPro reviewed-members endpoint returned429; no identity or absence
    finding rests on that transport response. A separate bounded UniProt query succeeds.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: plaque-family-query-IPR052070
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR052070%29+AND+%28reviewed%3Atrue%29&format=json&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id&size=500
  locator: All7 accession/name/gene/taxon rows; no next-page link; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-plaque/family-query-IPR052070.raw
  accessed_at: '2026-11-04T08:51:47.581308Z'
  support: supports
  summary: 'All7 reviewed returned entries are Vps23/TSG101/ELC homolog identities:
    Q99816,P25604,Q61187,Q6IRE4,Q9LHG8,Q54LJ3,Q9FFY6. This supports class scope independently
    of unchecked family prose.'
  snapshot_sha256: 18c36a9a61ee3d0dbe1c0a2844ce3978e2f02079830eb2b6e01b299aade8ae2f
  search_scope: UniProt REST query=(xref:interpro-IPR052070) AND (reviewed:true);
    fields accession,id,protein_name,gene_names,organism_id; size500; actual date
    2026-11-04T08:51:47.581308Z; all7 results read; no unreviewed or evolutionary-exhaustiveness
    claim.
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: All20 organism rows/28 organism-dataset pairs independently reread from
    same-PR micro snapshot; actual original fetch time retained; retained snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T08:49:08.706914Z'
  support: context_only
  summary: Complete current catalogue contains no Saccharomyces, S288C, SEY6210 or
    mammalian natural-host dataset. No matching downstream gene/module dataset was
    selected and recombinant E.coli is not used as a proxy. This is bounded catalogue
    noncoverage, not absence of ESCRT biology.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-historical-4-micro54-panther-PTHR45929-subfamilies
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/?extra_fields=subfamilies
  locator: Original request/response diagnostic only. Historical row from 20261022T063722Z-escrt-0-complex-audit/micro54-panther-PTHR45929-subfamilies;
    old time/hash retained from immutable original YAML; original raw transport response
    not independently reconstructed.
  accessed_at: '2026-10-22T06:24:25.663635Z'
  support: context_only
  summary: The attempted extra_fields=subfamilies request returned HTTP404 and establishes
    no exact subfamily identity.
  snapshot_sha256: aab5b774f3b6987ec232409161bc212533cc4383f53a47babfbc4dc3aaaf729c
- evidence_id: plaque-historical-4-micro54-bilodeau2002-publisher
  kind: validation
  reference: https://www.nature.com/articles/ncb815
  locator: Retained3038-byte challenge HTML and original access receipt. Historical
    row from 20261022T063722Z-escrt-0-complex-audit/micro54-bilodeau2002-publisher;
    old time/hash retained from immutable original YAML; original raw transport response
    not independently reconstructed.
  accessed_at: '2026-10-22T06:23:59.007405Z'
  support: context_only
  summary: The native Nature route returned HTTP200 with a Client Challenge page,
    not the Bilodeau main body. The complete primary abstract is independently available
    in the native MED entry.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: plaque-historical-4-micro54-henne2011-citeseer
  kind: validation
  reference: https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&repid=rep1&type=pdf
  locator: Retained native request and404 response. Historical row from 20261022T063722Z-escrt-0-complex-audit/micro54-henne2011-citeseer;
    old time/hash retained from immutable original YAML; original raw transport response
    not independently reconstructed.
  accessed_at: '2026-10-22T06:27:03.280566Z'
  support: context_only
  summary: The candidate public PDF URL returned HTTP404 HTML, not the Henne review.
    No main-body scope is inferred.
  snapshot_sha256: 687dd819f7af05e60aee60b6885521ddf2373a3eebf141975e936763a929a0bd
- evidence_id: plaque-historical-5-micro54-henne2011-citeseer
  kind: validation
  reference: https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&repid=rep1&type=pdf
  locator: Original request and response diagnostic; not a main body. Historical row
    from 20261022T063722Z-escrt-complex-audit/micro54-henne2011-citeseer; old time/hash
    retained from immutable original YAML; original raw transport response not independently
    reconstructed.
  accessed_at: '2026-10-22T06:27:03.280566Z'
  support: context_only
  summary: The candidate public Henne PDF route returned HTTP404 HTML. The actual
    review reading remains limited to the complete native abstract.
  snapshot_sha256: 687dd819f7af05e60aee60b6885521ddf2373a3eebf141975e936763a929a0bd
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete review and structured-source policy
  summary: Positive molecular and pathway assertions trigger actual host coverage
    assessment; absence of expression-module claims is insufficient.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Exact family/class grounding and append-only discussions
  summary: Exact whole-component identities differ from domains or broad paralog groups;
    label-only is valid while the specific class is unresolved. Preserve dated rationale
    and history.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component, essentiality, taxonomic and graph types
  summary: Functional requirement, localization, membership and formation necessity
    are distinct. Optional fields and valid family/class components are not automatic
    defects.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Primary names, synonyms, exact taxon and identity checks
  summary: Accessions, reference strains and gene aliases require native authority
    joins; they do not establish an experimental assembly mechanism.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope and evidence rules
  summary: Coarse function graphs are valid when explicitly nonmechanistic; avoid
    promoting targeting or fragment models into a universal complete assembly mechanism.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Source accessibility and precise read extent
  summary: Native metadata, complete primary abstracts, genuine primary bodies and
    secondary syntheses are different evidence tiers; captions are not image pixels.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Evidence, findings and lineage contract
  summary: Keep inherited stable keys with exact repository/review/finding identity
    and actual current evidence; a supported qualified pass remains scope limited.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-yang2010-epmc
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3124813/fullTextXML
  locator: Actual returned HTTP status/body and access barrier, not scientific text
  summary: 'Bounded current access attempt: HTTP500 endpoint error. This packet cannot
    certify a primary body; independent successful or abstract evidence is separately
    listed.'
  accessed_at: '2026-11-04T08:48:00.680811Z'
  support: context_only
  snapshot_sha256: b6ac63a8cbc84b3a14cbaaa494ddfc80244d64c1b542e2614c8122d33b62f136
- evidence_id: septin-yang2010-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3124813/?pdf=1
  locator: Genuine PMC3124813 Results S3–S6 and Discussion S7; Tables1/2 and main
    Fig1–7 captions; Methods S9/S12/S13, no S10/S11 crystallographic-method or coordinate
    reanalysis
  summary: Yeast Vta1-VSL/Vps4-SAB fragment crystal interface, SPR mutations and Cps1
    sorting are directly measured. The proposed planar Vps4 arrays remain explicitly
    speculative. Recombinant BL21/Rosetta2 expression is distinct from Open Biosystems
    yeast deletion assays; exact experimental reference-strain equivalence is not
    established.
  accessed_at: '2026-11-04T08:48:00.228706Z'
  support: supports
  snapshot_sha256: 4646a31cfc776c3b03aae787fdd1b7d1d6cc5f420802ed96928fec8c7a147479
- evidence_id: septin-hierro2004-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/nature02914
  locator: Publisher title/authors and complete displayed abstract; explicit subscription-preview
    boundary
  summary: The current reachable abstract describes a Y-shaped yeast core with Vps22,
    two Vps25 copies and C-terminal Vps36. The page exposes an abstract/preview, not
    full scientific body; historical client challenge is not represented as a new
    result.
  accessed_at: '2026-11-04T08:48:01.657493Z'
  support: supports
  snapshot_sha256: 4a52222bcea27761d539795b0b3d17349743b28a9c27bdf9d1215a243fed77fa
- evidence_id: septin-babst2002-publisher
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/S1534580702002204
  locator: Actual returned HTTP status/body and access barrier, not scientific text
  summary: 'Bounded current access attempt: HTTP403 publisher block. This packet cannot
    certify a primary body; independent successful or abstract evidence is separately
    listed.'
  accessed_at: '2026-11-04T08:47:59.916718Z'
  support: context_only
  snapshot_sha256: b61df3877b2f7793d5bbc2c6c5698b346870e7dda68a9c32514fda5b0dafec46
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621
  locator: Complete requested terms; assigned active names/definitions/synonyms and
    typed child relationships only
  summary: ESCRT-II/III/IV identities and parent class are exact. Endosome-membrane
    part_of differs from is_a ESCRT. GO II recruitment wording is interpreted as complex
    activation, not mandatory localization of every Vps20 molecule. General III remodeling
    definition and IV ATP-driven recycling remain broader than the yeast experimental
    example.
  accessed_at: '2026-11-04T08:47:14.618169Z'
  support: supports
  snapshot_sha256: 563ffa6dea1c58c1c92024214051980b0b5f3eefd7984f1ef56cb02432f9999b
- evidence_id: septin-GO0000814-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000814/ancestors?relations=is_a
  locator: Complete is_a-only ancestor closure
  summary: Exact ESCRT parent is present; this query does not establish a parthood
    relation.
  accessed_at: '2026-11-04T08:47:14.551119Z'
  support: supports
  snapshot_sha256: a829eb5d826b213e431920de398b9fbfc86638d1b2c04bde4d67034101ad65d2
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxonomy response
  summary: Saccharomyces cerevisiae, rank species. Species and reference strain differ
    from recombinant expression hosts and exact experimental strain identities.
  accessed_at: '2026-11-04T08:47:14.613302Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxonomy response
  summary: Saccharomyces cerevisiae S288C, rank strain. Species and reference strain
    differ from recombinant expression hosts and exact experimental strain identities.
  accessed_at: '2026-11-04T08:47:14.585919Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-protein-P47142
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47142.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed P47142: Vacuolar protein-sorting-associated protein 25; primary
    VPS25; synonyms [''VPT25'']; ordered loci [''YJR102C'']; taxon 559292. Native
    annotation evidence is not an independently repeated experiment. Exact family
    membership joins checked separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:15.730237Z'
  support: supports
  snapshot_sha256: d2a16d3f9839384e78be24a7b4e0f21f1e3ed2223f7aab79b09ab1b567057257
- evidence_id: septin-protein-Q06696
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06696.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed Q06696: Vacuolar protein-sorting-associated protein 36; primary
    VPS36; synonyms [''GRD12'', ''VAC3'', ''VPL11'']; ordered loci [''YLR417W''];
    taxon 559292. Native annotation evidence is not an independently repeated experiment.
    Exact family membership joins checked separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:15.537360Z'
  support: supports
  snapshot_sha256: 0fbc4ab1a3fa68f1a3c78fb9b0ff864be16758cd681d50f55101e05f129f5ddb
- evidence_id: septin-protein-Q12483
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12483.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed Q12483: Vacuolar-sorting protein SNF8; primary SNF8; synonyms
    [''VPS22'']; ordered loci [''YPL002C'']; taxon 559292. Native annotation evidence
    is not an independently repeated experiment. Exact family membership joins checked
    separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:14.826324Z'
  support: supports
  snapshot_sha256: 41764f2dc6af4a6d21a77ae0e0ffa32f449ca9c48a4f60a86cb9e618d05ef59e
- evidence_id: septin-gene-VPS22-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS22%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry Q12483 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:16.517733Z'
  support: supports
  snapshot_sha256: acd580440b9baa4add3267b00c726fe7a4472a23f82335561d55e0fe63ac2309
  search_scope: UniProt gene_exact:VPS22 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:16.517733Z.
- evidence_id: septin-gene-VPS25-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS25%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry P47142 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:16.019955Z'
  support: supports
  snapshot_sha256: 167d5536a57df56413adb410d44531c449843c5e91ec318c3129957479893427
  search_scope: UniProt gene_exact:VPS25 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:16.019955Z.
- evidence_id: septin-gene-VPS36-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS36%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry Q06696 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:15.959372Z'
  support: supports
  snapshot_sha256: 7ce9197c96302edd9f2cd77c4da31c570480ee6d6a95517b58cd363f449c08dd
  search_scope: UniProt gene_exact:VPS36 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:15.959372Z.
- evidence_id: septin-pmid-12194858
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194858+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Endosome-associated complex, ESCRT-II, recruits transport
    machinery for protein sorting at the multivesicular body. Authors Babst M, Katzmann
    DJ, Snyder WB, Wendland B, Emr SD. DOI 10.1016/s1534-5807(02)00219-8. Complete
    primary abstract inspected; this evidence row alone does not certify full text.
    Native UniProt localization-reference joins are retained as annotations, not atlas
    reanalysis.
  accessed_at: '2026-11-04T08:47:20.252968Z'
  support: supports
  snapshot_sha256: 57dd49a98d02e16ca29906fb961e45f855e43c38f56a94dd26e953a05636dbad
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:20.252968Z.
- evidence_id: septin-doi-j_devcel_2004_09_003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2004.09.003%22&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: 'Exact citation ESCRT-II, an endosome-associated complex required for protein
    sorting: crystal structure and interactions with ESCRT-III and membranes. Authors
    Teo H, Perisic O, González B, Williams RL. DOI 10.1016/j.devcel.2004.09.003. Complete
    primary abstract inspected; this evidence row alone does not certify full text.
    Native UniProt localization-reference joins are retained as annotations, not atlas
    reanalysis.'
  accessed_at: '2026-11-04T08:47:14.638064Z'
  support: supports
  snapshot_sha256: 4f3790f773f82e02d8f37e5998526d4175a42bfccbd913f1ebfe0bf7700b28e2
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:14.638064Z.
- evidence_id: septin-doi-j_devcel_2008_04_004
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2008.04.004%22&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Integrated structural model and membrane targeting mechanism
    of the human ESCRT-II complex. Authors Im YJ, Hurley JH. DOI 10.1016/j.devcel.2008.04.004.
    Complete primary abstract inspected; this evidence row alone does not certify
    full text. Native UniProt localization-reference joins are retained as annotations,
    not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:15.228204Z'
  support: supports
  snapshot_sha256: 09656870b230be8331f71ac31d6702bf960c3dc8417094a2e5e89ba85024b1e7
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:15.228204Z.
- evidence_id: septin-doi-j_devcel_2009_07_008
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2009.07.008%22&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Structure and function of the ESCRT-II-III interface in
    multivesicular body biogenesis. Authors Im YJ, Wollert T, Boura E, Hurley JH.
    DOI 10.1016/j.devcel.2009.07.008. Complete primary abstract inspected; this evidence
    row alone does not certify full text. Native UniProt localization-reference joins
    are retained as annotations, not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:15.223955Z'
  support: supports
  snapshot_sha256: 7e56ff822ec9da1728abaa2b139fdfbcc4ca2eae66e52c3c55ed07b041438ff5
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:15.223955Z.
- evidence_id: septin-doi-nature02914
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature02914%22&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Structure of the ESCRT-II endosomal trafficking complex.
    Authors Hierro A, Sun J, Rusnak AS, Kim J, Prag G, Emr SD, Hurley JH. DOI 10.1038/nature02914.
    Complete primary abstract inspected; this evidence row alone does not certify
    full text. Native UniProt localization-reference joins are retained as annotations,
    not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:20.830692Z'
  support: supports
  snapshot_sha256: 27d08a5c335e8982f8dc3eaa95690c647d4cbdc20ce57fa684daf4b61606faf5
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:20.830692Z.
- evidence_id: septin-doi-science_1161070
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1161070%22&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Helical structures of ESCRT-III are disassembled by VPS4.
    Authors Lata S, Schoehn G, Jain A, Pires R, Piehler J, Gottlinger HG, Weissenhorn
    W. DOI 10.1126/science.1161070. Complete primary abstract inspected; this evidence
    row alone does not certify full text. Native UniProt localization-reference joins
    are retained as annotations, not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:15.310827Z'
  support: supports
  snapshot_sha256: 94989d282d11a3c4cbdc975b56e14959a8d219174d72608515c369055e4058b5
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:15.310827Z.
- evidence_id: septin-teo2004-primary-pdf
  kind: primary_source
  reference: https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf
  locator: Printed p559 summary/Introduction; p564–567 direct-interaction/liposome
    Results, Fig4/5/6 caption text, Conclusions and plasmid/expression/purification/pull-down
    Methods. Other crystallographic Results/Methods not independently used.
  summary: Teo2004 resolves the yeast core with one Vps22, two Vps25 and truncated
    Vps36; purified ESCRT-II and isolated Vps25 bind Vps20 directly and enhance liposome
    binding. Removal of Vps22 residues1–40 or Vps36 residues1–370 does not abolish
    the Vps20 interaction. ATCC9763D yeast genomic material was expressed in C41(DE3)/B834(DE3);
    this is recombinant yeast anatomy, not native bacterial ESCRT. Freshly retrieved
    and independently read in this review; no figure pixels or supplementary experiments
    certified.
  accessed_at: '2026-11-04T08:47:16.341560Z'
  support: supports
  snapshot_sha256: 9a62830da92c7a92939524b134a277cf6381382e5539dfdfb47ab58e22817dce
- evidence_id: septin-primary-PMC2475506
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2475506/
  locator: Results S4/S6/S7 with Fig4/5 captions; Methods S10/S16; complete native
    abstract supplies structural stoichiometry. No figure pixels or supplement files.
  summary: Im/Hurley2008 examines human recombinant complexes and yeast BY4741-derived
    sorting/localization mutants. GLUE/Vps22-H0 jointly contribute to membrane targeting;
    the pseudo-intact liposome construct lacks VPS25-WH2. Its membrane-binding defects
    are not whole-complex formation experiments. Freshly retrieved and independently
    read in this review; no figure pixels or supplementary experiments certified.
  accessed_at: '2026-11-04T08:47:15.215209Z'
  support: supports
  snapshot_sha256: 70553381866291665d52488e9146f6f467bd52d7d8ac0bfa4e3af08bb11086f1
- evidence_id: septin-primary-PMC2749878
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2749878/
  locator: Results S2/S5/S6/S7/S8, Discussion S10; Methods S12/S16/S17/S18/S20, Table1/Fig1–4
    captions. No pixels or supplements.
  summary: Im2009 directly activates yeast ESCRT-III budding/scission with ESCRT-II
    in synthetic GUV assays; VPS25/VPS20 interface mutants fail in activation and
    yeast cargo sorting. Strong Vps20 membrane binding is distinguished from complex
    activation. Freshly retrieved and independently read in this review; no figure
    pixels or supplementary experiments certified.
  accessed_at: '2026-11-04T08:47:15.604175Z'
  support: supports
  snapshot_sha256: bbb2d3f056ef3bcf6ea39981fa32bbb0eb77a727a784b67c4edac9122beb93a9
- evidence_id: septin-primary-PMC2758909
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2758909/
  locator: Complete main scientific text S1 and Fig1–4 captions; supplementary Methods/data
    and pixels not independently read.
  summary: Lata2008 directly observes ATP/Mg-dependent VPS4B disassembly of engineered
    CHMP2A/CHMP3 tubes. This supports the disassembly principle while retaining human-protein/truncation
    context and a proposed rather than directly observed final scission model. Freshly
    retrieved and independently read in this review; no figure pixels or supplementary
    experiments certified.
  accessed_at: '2026-11-04T08:47:15.636482Z'
  support: supports
  snapshot_sha256: f24761e7ced198b5a37d2b9a5ae4ce8fe7d38c18ec7f7227de9643f40e8ad57f
- evidence_id: septin-ipr-IPR016689
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016689/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR016689 identifies the complete Snf8/Vps22 family, with exact PIRSF017215/PTHR12806
    signatures; its hierarchy separates it from Vps36 under the broader Snf8/Vps36
    parent. Current independent authority/protein joins reconfirm the stated scope.
  accessed_at: '2026-11-04T08:47:15.848670Z'
  support: supports
  snapshot_sha256: 21d49936fd534f5d56fed35c60d3044d204f5c27c7dad02ee033ce3ca5032418
- evidence_id: septin-ipr-IPR008570
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008570/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR008570 identifies the complete Vps25 family with PF05871/PTHR13149 signatures.
    Its incidental Vps35 wording is not adopted as an interaction claim. Current independent
    authority/protein joins reconfirm the stated scope.
  accessed_at: '2026-11-04T08:47:15.927689Z'
  support: supports
  snapshot_sha256: 59342a0d75cb4488b4e3dc04de325d2d86049267dec3373c593728ee2b18d72b
- evidence_id: septin-ipr-IPR037855
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037855/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR037855 identifies Vps36 with PTHR13128, distinct from its GLUE/NZF domains
    and from sister Snf8/Vps22. Current independent authority/protein joins reconfirm
    the stated scope.
  accessed_at: '2026-11-04T08:47:16.152861Z'
  support: supports
  snapshot_sha256: c5b91d705a08cc381af4134f3cf2c870d85259a8426f2d64a48566963f5ef6a0
- evidence_id: septin-GO0000815-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000815/ancestors?relations=is_a
  locator: Complete is_a-only ancestor closure
  summary: Exact ESCRT parent is present; this query does not establish a parthood
    relation.
  accessed_at: '2026-11-04T08:47:16.218510Z'
  support: supports
  snapshot_sha256: 397c1b4a0743d24299b9286f3083d4658b6b632181689f1e23e8c00d5ce9b9c5
- evidence_id: septin-protein-P36095
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36095.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed P36095: Vacuolar protein-sorting-associated protein 24; primary
    VPS24; synonyms [''DID3'']; ordered loci [''YKL041W'']; taxon 559292. Native annotation
    evidence is not an independently repeated experiment. Exact family membership
    joins checked separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:16.971394Z'
  support: supports
  snapshot_sha256: 546160a365db5fc7af42b69ea6477e932a0cb22ad1fe581bb54a5e75ddf3a319
- evidence_id: septin-protein-P36108
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36108.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed P36108: DOA4-independent degradation protein 4; primary DID4;
    synonyms [''CHM2'', ''GRD7'', ''REN1'', ''VPL2'', ''VPS2'', ''VPT14'']; ordered
    loci [''YKL002W'']; taxon 559292. Native annotation evidence is not an independently
    repeated experiment. Exact family membership joins checked separately from the
    family-entry definition.'
  accessed_at: '2026-11-04T08:47:17.869739Z'
  support: supports
  snapshot_sha256: f8332fcf2b6227fdc2d82dbec3c36d8811daae347fc8b9ab6f41116fe18b1033
- evidence_id: septin-protein-P39929
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39929.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed P39929: Vacuolar-sorting protein SNF7; primary SNF7; synonyms
    [''DID1'', ''VPS32'']; ordered loci [''YLR025W'']; taxon 559292. Native annotation
    evidence is not an independently repeated experiment. Exact family membership
    joins checked separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:18.947946Z'
  support: supports
  snapshot_sha256: 90f61580337df38fe20f8e438c2841ed824b58bf7aab5eb544b61dd066302555
- evidence_id: septin-protein-Q04272
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04272.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed Q04272: Vacuolar protein sorting-associated protein 20; primary
    VPS20; synonyms [''ASI10'', ''CHM6'', ''VPT20'']; ordered loci [''YMR077C''];
    taxon 559292. Native annotation evidence is not an independently repeated experiment.
    Exact family membership joins checked separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:20.886131Z'
  support: supports
  snapshot_sha256: d4bae2c9bf193fc100dc349bcd9533b85ac171d3b8ea960a5677d80b1a6445b6
- evidence_id: septin-gene-VPS20-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry Q04272 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:18.019570Z'
  support: supports
  snapshot_sha256: 6a9160968fcdd1d04d0cf4495b60511de9ce21a0465d84513bf285cb8a7eda12
  search_scope: UniProt gene_exact:VPS20 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:18.019570Z.
- evidence_id: septin-gene-SNF7-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASNF7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry P39929 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:24.299524Z'
  support: supports
  snapshot_sha256: cee6077f0c5269faecb7d6aa2fdfd10a166243a4ff1e63ad64e272e38a0a7a38
  search_scope: UniProt gene_exact:SNF7 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:24.299524Z.
- evidence_id: septin-gene-VPS24-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS24%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry P36095 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:22.066935Z'
  support: supports
  snapshot_sha256: b7e1e1651a0cd21968ce32558e843b350c965b719ab6695c776bbdf15ad97181
  search_scope: UniProt gene_exact:VPS24 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:22.066935Z.
- evidence_id: septin-gene-VPS2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry P36108 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:17.974923Z'
  support: supports
  snapshot_sha256: 9bcc02d6f67da2b9e5ac9160be6c24df5c08c2b2e354bba4c9f22d1f213ddead
  search_scope: UniProt gene_exact:VPS2 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:17.974923Z.
- evidence_id: septin-pmid-12194857
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194857+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: 'Exact citation Escrt-III: an endosome-associated heterooligomeric protein
    complex required for mvb sorting. Authors Babst M, Katzmann DJ, Estepa-Sabal EJ,
    Meerloo T, Emr SD. DOI 10.1016/s1534-5807(02)00220-4. Complete primary abstract
    inspected; this evidence row alone does not certify full text. Native UniProt
    localization-reference joins are retained as annotations, not atlas reanalysis.'
  accessed_at: '2026-11-04T08:47:16.947169Z'
  support: supports
  snapshot_sha256: fb4cf9223f5eeb6ef65116513b561cd88d8b4e52fac850f906db9d7b538a2319
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:16.947169Z.
- evidence_id: septin-pmid-24139821
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24139821+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Essential N-terminal insertion motif anchors the ESCRT-III
    filament during MVB vesicle formation. Authors Buchkovich NJ, Henne WM, Tang S,
    Emr SD. DOI 10.1016/j.devcel.2013.09.009. Complete primary abstract inspected;
    this evidence row alone does not certify full text. Native UniProt localization-reference
    joins are retained as annotations, not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:17.128412Z'
  support: supports
  snapshot_sha256: c93adc60e61375791acab61b61697ada70a882c531561c82bc58fe2260fda127
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:17.128412Z.
- evidence_id: septin-pmid-25303532
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25303532+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Surveillance of nuclear pore complex assembly by ESCRT-III/Vps4.
    Authors Webster BM, Colombi P, Jäger J, Lusk CP. DOI 10.1016/j.cell.2014.09.012.
    Complete primary abstract inspected; this evidence row alone does not certify
    full text. Native UniProt localization-reference joins are retained as annotations,
    not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:17.545546Z'
  support: supports
  snapshot_sha256: 6c06dffe14ef5e28eeb1f6dbc7caf7bda0cbcf1c11e2e686aac39bdfcfbd82db
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:17.545546Z.
- evidence_id: septin-ipr-IPR005024
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005024/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR005024 is the broad Snf7-like family covering multiple CHMP paralogs,
    yeast Did4/Did2 and archaeal CdvB. Its PTHR10476/PTHR22761/PF03357 signatures
    do not distinguish each of the four named yeast constituents. Current independent
    authority/protein joins reconfirm the stated scope.
  accessed_at: '2026-11-04T08:47:17.566795Z'
  support: supports
  snapshot_sha256: e118d2c54cfb0f83512b2fc57060bbec6363da1411db74ebf481701426716448
- evidence_id: septin-GO1990621-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990621/ancestors?relations=is_a
  locator: Complete is_a-only ancestor closure
  summary: Exact ESCRT parent is present; this query does not establish a parthood
    relation.
  accessed_at: '2026-11-04T08:47:17.760823Z'
  support: supports
  snapshot_sha256: 3a8d70c9919ca9dfd744f4e21be9ae573b2122eb69f5c527cf164f1e43cfb153
- evidence_id: septin-protein-P52917
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P52917.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed P52917: Vacuolar protein sorting-associated protein 4; primary
    VPS4; synonyms [''CSC1'', ''DID6'', ''END13'', ''GRD13'', ''VPL4'', ''VPT10''];
    ordered loci [''YPR173C'']; taxon 559292. Native annotation evidence is not an
    independently repeated experiment. Exact family membership joins checked separately
    from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:24.900892Z'
  support: supports
  snapshot_sha256: 3f3963995e5a9c1e2e6169f19791378a430a63fa5c1011f38504b560012cdeee
- evidence_id: septin-protein-Q06263
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06263.json
  locator: Native accession/status/name, complete gene/locus tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments, cited evidence and family xrefs
  summary: 'Reviewed Q06263: Vacuolar protein sorting-associated protein VTA1; primary
    VTA1; synonyms []; ordered loci [''YLR181C'']; taxon 559292. Native annotation
    evidence is not an independently repeated experiment. Exact family membership
    joins checked separately from the family-entry definition.'
  accessed_at: '2026-11-04T08:47:19.014420Z'
  support: supports
  snapshot_sha256: e59e17eca16f6cfd1e1ceb622fdfc15ac2c4c20a468595bea57a3b9fc7fe3a1f
- evidence_id: septin-gene-VPS4-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry P52917 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:21.300905Z'
  support: supports
  snapshot_sha256: 0e9925d47367129e7a66a1019a4246c7c7df2f02c6bb4d7de54b8dc04b8f2dc1
  search_scope: UniProt gene_exact:VPS4 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:21.300905Z.
- evidence_id: septin-gene-VTA1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVTA1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned reviewed native result, primary names, synonyms and taxon
  summary: One current reviewed entry Q06263 for the declared gene query; primary-name
    versus alias distinctions are preserved. This does not reconstruct an unspecified
    historical query.
  accessed_at: '2026-11-04T08:47:22.911658Z'
  support: supports
  snapshot_sha256: 23490571e507dd4e4b53e1bab21a2bea3c1b34b9f9e66a2aac8b791a88eb5fce
  search_scope: UniProt gene_exact:VTA1 AND organism_id:559292 AND reviewed:true;
    size500, no date filter; all returned result read at 2026-11-04T08:47:22.911658Z.
- evidence_id: septin-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Global analysis of protein localization in budding yeast.
    Authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea
    EK. DOI 10.1038/nature02026. Complete primary abstract inspected; this evidence
    row alone does not certify full text. Native UniProt localization-reference joins
    are retained as annotations, not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:18.600930Z'
  support: supports
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:18.600930Z.
- evidence_id: septin-pmid-14701806
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14701806+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Characterization of Vta1p, a class E Vps protein in Saccharomyces
    cerevisiae. Authors Shiflett SL, Ward DM, Huynh D, Vaughn MB, Simmons JC, Kaplan
    J. DOI 10.1074/jbc.m312669200. Complete primary abstract inspected; this evidence
    row alone does not certify full text. Native UniProt localization-reference joins
    are retained as annotations, not atlas reanalysis.
  accessed_at: '2026-11-04T08:47:23.654336Z'
  support: supports
  snapshot_sha256: 29e4ccbdf46457f0869b293ed9d59b94f1373583fbeb32880f3c2d11153c669e
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:23.654336Z.
- evidence_id: septin-pmid-20696398
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20696398+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native EuropePMC CORE citation and abstractText
  summary: Exact citation Structural role of the Vps4-Vta1 interface in ESCRT-III
    recycling. Authors Yang D, Hurley JH. DOI 10.1016/j.str.2010.04.014. Complete
    primary abstract inspected; this evidence row alone does not certify full text.
    Native UniProt localization-reference joins are retained as annotations, not atlas
    reanalysis.
  accessed_at: '2026-11-04T08:47:19.205168Z'
  support: supports
  snapshot_sha256: 67998b61966da788949e0569e87dd0b119aa53fa1f997fe0d8d5d29db045594f
  search_scope: Exact DOI or PMID query in URL; CORE format, no date filter, unique
    result fully inspected at 2026-11-04T08:47:19.205168Z.
- evidence_id: septin-primary-PMC3124813
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3124813/
  locator: Actual returned HTTP status/body and access barrier, not scientific text
  summary: 'Bounded current access attempt: HTTP200 browser challenge. This packet
    cannot certify a primary body; independent successful or abstract evidence is
    separately listed.'
  accessed_at: '2026-11-04T08:47:19.105964Z'
  support: context_only
  snapshot_sha256: d61ef30849f9fd3aec3c44a2b8703613bd997b67c2d050224fb4d1343fafe221
- evidence_id: septin-ipr-IPR044538
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044538/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR044538 is the Vta1-like full protein family, explicitly including yeast
    Vta1 and animal/plant homologs. PTHR46009 identifies the constituent class rather
    than only its VSL or MIT domain. Current independent authority/protein joins reconfirm
    the stated scope.
  accessed_at: '2026-11-04T08:47:19.613720Z'
  support: supports
  snapshot_sha256: 0a315ff90ca36720a6769f7b8107881376332f329f19744b74aa553f581c2541
- evidence_id: septin-ipr-IPR045253
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045253/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR045253 is only the Vps4 MIT domain; it does not identify the complete
    ATPase constituent. Current independent authority/protein joins reconfirm the
    stated scope.
  accessed_at: '2026-11-04T08:47:19.710579Z'
  support: supports
  snapshot_sha256: fabe7935f45abf376ea681ab9172cdcd866abd4221cce5cadd4e3d7330bfc535
- evidence_id: septin-ipr-IPR050304
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050304/
  locator: Current native name/type, complete descriptions and curation flags, member
    signatures, hierarchy and overlap fields; separate member accession join
  summary: IPR050304 is the broader microtubule-severing AAA ATPase family with PTHR23074.
    Its LLM-generated unchecked prose is not primary functional evidence and does
    not establish exact Vps4 specificity. Current response independently read; unchecked
    LLM prose is excluded from scientific support.
  accessed_at: '2026-11-04T08:47:19.800277Z'
  support: supports
  snapshot_sha256: edc71f6a3c68bcf69adf8c7e78aa9025600bc070e41c6c8917ee6071ef19cef3
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete unpaginated official catalogue: all20 organism rows and advertised
    dataset keys'
  summary: No Saccharomyces cerevisiae or human host appears. Bacterial expression
    hosts for recombinant yeast proteins are not substitutes for the biological complex
    host. Host noncoverage is not biological absence.
  accessed_at: '2026-11-04T08:49:08.706914Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official /api/datasets complete20 organism rows inspected for Saccharomyces
    cerevisiae, S288C, BY4741/BY4742 and Homo sapiens; no date filter; actual 2026-11-04T08:49:08.706914Z.
- evidence_id: septin-henne2011-abstract
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21763610+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Complete native bibliographic identity and secondary-review abstract
  summary: Henne, Buchkovich and Emr2011 is a secondary review of cargo recognition,
    membrane sculpting, MVBs and related pathways. Only its complete abstract and
    citation are inspected; no detailed review-body mechanism certified.
  accessed_at: '2026-11-04T08:50:35.598446Z'
  support: supports
  snapshot_sha256: 54062d7e12cf799adc9a421b8b6ca0ecfdad7bd7cdc485618d875a99974e4a4e
  search_scope: EuropePMC exact EXT_ID21763610 AND SRCMED, CORE,pageSize1,no date
    filter; unique result at 2026-11-04T08:50:35.598446Z.
- evidence_id: septin-henne2011-access
  kind: validation
  reference: https://www.cell.com/developmental-cell/fulltext/S1534-5807(11)00240-3
  locator: Actual current publisher403 access response
  summary: Publisher route returned a challenge/403, not a primary or secondary scientific
    body. Missing access is not refutation.
  accessed_at: '2026-11-04T08:51:47.631802Z'
  support: context_only
  snapshot_sha256: 1eb9c026fd2420f9323e33e82d8e943c0dafc0b163326a1a41465d03894d6db0
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical Nov3 00:49Z command receipt
  summary: Actual prior exit1 PermissionError reading runner pyvenv.cfg; no current
    invocation claimed. Current official catalogue fallback is separate evidence.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/adversary-septin/original-checks.json
  locator: Three actual native validate/render pairs and39 historical input occurrences
  summary: All three original YAML documents validate0 and render0 to exact original
    Markdown. All39 input occurrences match their frozen Git source, and all three
    current targets are unchanged.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: supports
  snapshot_sha256: 4bde1f96b84e59c04738ba34ce742bfcb8d51d9bc467f54937907c19f3640bfe
- evidence_id: septin-record-escrt_ii_complex
  kind: record_content
  reference: data/structures/other/escrt_ii_complex.yaml
  locator: Entire current maintained record including all history, discussions, examples,
    functions and graph edges
  summary: Current target read in full; unchanged from original frozen input. Historical
    rationale is provenance, not a new scientific experiment.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: context_only
  snapshot_sha256: e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7
- evidence_id: septin-original-escrt_ii_complex
  kind: prior_review
  reference: reviews/structured/20261022T063724Z-escrt-ii-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown, all evidence/checks/findings/actions/limitations
  summary: Original scientific scopes, exact predecessor identities and formal expression-only
    exclusion inspected; historical failed-access limitations are not relabeled as
    current successful source reads. No own original access-only evidence-kind defect
    established.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: context_only
  snapshot_sha256: 6d5e731969e3179af4bd46787846a7469aa55404254febdb4af446968f1dd355
- evidence_id: septin-native-escrt_ii_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-verify-receipt.json;
    complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-verify.log;
    receipt SHA256 f40096c949e6b2183128d4a256b5e662941df0b775ae3533505ebe5cd7f8ad2d
  summary: 3 reviewed examples and 3 COVERED typed component nodes; identity/coverage
    validation does not establish scientific membership or formation necessity.
  accessed_at: '2026-11-04T08:46:47.443162Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-escrt_ii_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-causal-receipt.json;
    complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-causal.log;
    receipt SHA256 6021ed5e78399e7c10d736a4e6bda9eedcc4c534ebc7cf3c50b9316318a43f4f
  summary: 3 reviewed examples and 3 COVERED typed component nodes; identity/coverage
    validation does not establish scientific membership or formation necessity.
  accessed_at: '2026-11-04T08:46:47.856401Z'
  support: supports
  snapshot_sha256: 60759d4c40ce1830fe803c161ca1781c61fb986ff0f374f0aea3909d75974588
- evidence_id: septin-record-escrt_iii_complex
  kind: record_content
  reference: data/structures/other/escrt_iii_complex.yaml
  locator: Entire current maintained record including all history, discussions, examples,
    functions and graph edges
  summary: Current target read in full; unchanged from original frozen input. Historical
    rationale is provenance, not a new scientific experiment.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: context_only
  snapshot_sha256: 9e1b8327f85a97301be8e84633176829e518d1272b35d43515e85cce4a2ceaa8
- evidence_id: septin-original-escrt_iii_complex
  kind: prior_review
  reference: reviews/structured/20261022T063725Z-escrt-iii-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown, all evidence/checks/findings/actions/limitations
  summary: Original scientific scopes, exact predecessor identities and formal expression-only
    exclusion inspected; historical failed-access limitations are not relabeled as
    current successful source reads. No own original access-only evidence-kind defect
    established.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: context_only
  snapshot_sha256: 5e9542977e056076935f1e7228ab4c4be362fb773cec542bdc584c2ce84ad893
- evidence_id: septin-native-escrt_iii_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iii_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-verify-receipt.json;
    complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-verify.log;
    receipt SHA256 1eebb5dffcec704661a1a721540193a5b432a7fe8662cac2e298b7dd11cea5a5
  summary: 4 reviewed examples and 4 COVERED typed component nodes; identity/coverage
    validation does not establish scientific membership or formation necessity.
  accessed_at: '2026-11-04T08:46:49.048050Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-escrt_iii_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iii_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-causal-receipt.json;
    complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-causal.log;
    receipt SHA256 749aecb1980db6082b235e896f87f0ef19633be41ad5dbeaa2c03f9932ec2b3c
  summary: 4 reviewed examples and 4 COVERED typed component nodes; identity/coverage
    validation does not establish scientific membership or formation necessity.
  accessed_at: '2026-11-04T08:46:49.452556Z'
  support: supports
  snapshot_sha256: 8aa31fbbeddf41d755cce99b19d1cf0a904d965a3b5b726ed0af0bccb5986625
- evidence_id: septin-record-escrt_iv_complex
  kind: record_content
  reference: data/structures/other/escrt_iv_complex.yaml
  locator: Entire current maintained record including all history, discussions, examples,
    functions and graph edges
  summary: Current target read in full; unchanged from original frozen input. Historical
    rationale is provenance, not a new scientific experiment.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: context_only
  snapshot_sha256: 54158602625f36ee41851b9d01628d95d5147bc2f27bf4b23bc47f5f2a1f41e2
- evidence_id: septin-original-escrt_iv_complex
  kind: prior_review
  reference: reviews/structured/20261022T063726Z-escrt-iv-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown, all evidence/checks/findings/actions/limitations
  summary: Original scientific scopes, exact predecessor identities and formal expression-only
    exclusion inspected; historical failed-access limitations are not relabeled as
    current successful source reads. No own original access-only evidence-kind defect
    established.
  accessed_at: '2026-11-04T08:55:18.651278Z'
  support: context_only
  snapshot_sha256: 3694de58856d7aade6fcbf380366c30518bf0fe0f938a34b645682101e00bc57
- evidence_id: septin-native-escrt_iv_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iv_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-verify-receipt.json;
    complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-verify.log;
    receipt SHA256 16f87c2eec5baafa61d58b602705a34626ee06ececdf5f8e01d2a8f2d603d793
  summary: 2 reviewed examples and 2 COVERED typed component nodes; identity/coverage
    validation does not establish scientific membership or formation necessity.
  accessed_at: '2026-11-04T08:46:51.896547Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-escrt_iv_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/escrt_iv_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-causal-receipt.json;
    complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-causal.log;
    receipt SHA256 b34de9d2d3e66cc973d94cf09dc4c82bd0e96b9e73703b007cab0d4e8490ae2d
  summary: 2 reviewed examples and 2 COVERED typed component nodes; identity/coverage
    validation does not establish scientific membership or formation necessity.
  accessed_at: '2026-11-04T08:46:52.290314Z'
  support: supports
  snapshot_sha256: 121863bc029421c26ea38ac4139dfb14ac6c34250ad3ac307708f29e157ff2e4
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T08:51:58.133578Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 8b61637ed4fe8a0060f624880a568620ecd4341205e5cec6bcc1881ccecfdea4
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T08:46:43.888957Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T08:46:24.704507Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T08:46:23.676507Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T08:46:50.320939Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T09:05:43Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 4e01698204d4d125f7410ccd73f660e0d05a09da06df056ceb5628f91dd311e2
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T08:48:28.609367Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 6aa3e331bb537083b05a098a05fc199b81526043251ad9ef9ba91218e2009ff5
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2391 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:38.410725Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/emrky_tolc_multidrug_efflux_transport_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:38.844933Z'
  support: context_only
  snapshot_sha256: 8c7e3458522c33d3bce89abbe58b15f4f8f468d3b01f0625bd807e3e464c9a6c
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-endoplasmic_reticulum_sec_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:39.270125Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-endoplasmic_reticulum_sec_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/endoplasmic_reticulum_sec_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:39.677275Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-epsilon_dna_polymerase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:40.785727Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-epsilon_dna_polymerase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/epsilon_dna_polymerase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:41.197780Z'
  support: context_only
  snapshot_sha256: 6f8e9867949e29c1044c6f57d6788b7d019afd1c2891b5256df95d0edf86a29d
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ermes_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:41.611039Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ermes_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/ermes_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:42.015018Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_0_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:43.148381Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_0_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_0_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:43.558182Z'
  support: context_only
  snapshot_sha256: 8d965b4762c6f13e759cf9a9f2c993dde6bd0f8922fe5998302d843e0f3efa5e
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:43.968124Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:44.371047Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_i_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:45.868230Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_i_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_i_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:46.276063Z'
  support: context_only
  snapshot_sha256: aac6b7401b494f165148fbd63ff7a1fd22fde5cb5693ccd03f0e928f51a82f2e
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_ii_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:47.443162Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_ii_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_ii_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:47.856401Z'
  support: context_only
  snapshot_sha256: 60759d4c40ce1830fe803c161ca1781c61fb986ff0f374f0aea3909d75974588
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_iii_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:49.048050Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_iii_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iii_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:49.452556Z'
  support: context_only
  snapshot_sha256: 8aa31fbbeddf41d755cce99b19d1cf0a904d965a3b5b726ed0af0bccb5986625
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_iv_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:51.896547Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-escrt_iv_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2391/escrt_iv_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T08:46:52.290314Z'
  support: context_only
  snapshot_sha256: 121863bc029421c26ea38ac4139dfb14ac6c34250ad3ac307708f29e157ff2e4
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-emrky-identity
  area: identity
  topic: Exact pump boundary and reference strain
  outcome: supported
  summary: Minted identity denotes the specific EmrK/EmrY/TolC assembly, whereas GO1990281
    is broader. CPX4273 is exact organism-specific composition, not a source-neutral
    protein family. K12 reference annotation is distinct from each May experimental
    construct.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-complex-CPX-4273
  - micro-go-1990281
  - micro-taxon-83333
  - micro-PMC2772303-legacy
- assessment_id: micro-emrky-tier
  area: evidence
  topic: Curator inference and by-similarity participant annotations
  outcome: supported
  summary: CPX ECO0005547 and native EmrK/EmrY ECO0000250 are explicitly inferential.
    Null EmrK/Y counts and TolC3 are retained. Neither current source asserts a constituent-specific
    deletion/assembly experiment; other TolC pumps are not substituted.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-complex-CPX-4273
  - micro-eco-0005547
  - micro-protein-P52599
  - micro-protein-P52600
  - micro-protein-P02930
- assessment_id: micro-emrky-refresh
  area: graph
  topic: Substantive stale-edge reassessment
  outcome: concern
  summary: The three new contributes-to edges preserve supported inferred participant
    membership, and the new transport-to-export edge is a coarse function relation
    at declared NONMECHANISTIC scope. Their CPX evidence notes independently overstate
    source-annotated essentiality; this narrow new attribution defect does not invalidate
    the membership edges or require automatic changes to older component values.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-delta-0
  - micro-complex-CPX-4273
  - micro-go-0042910
  - micro-go-0140330
  - micro-graph-policy
  - micro-emrky-independent-challenge
- assessment_id: micro-emrky-old-major
  area: evidence
  topic: Independent disposition of inherited formation finding
  outcome: supported
  summary: 'Reject the inherited major as formulated: absence of an isolated formation
    assay does not establish that defining members of this explicitly inferred tripartite
    complex must be UNKNOWN. The original allowed added evidence, but its mandatory
    correction treats the lack of measured component-specific necessity as a demonstrated
    major defect. Rejection does not certify experimental necessity, infer dispensability,
    rewrite history or resolve the separate new source-attribution problem.'
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-schema
  - micro-complex-CPX-4273
  - micro-PMC2772303-legacy
  - micro-emrky-independent-challenge
- assessment_id: micro-emrky-families
  area: grounding
  topic: Exact TolC family and broader adaptor/transporter families
  outcome: supported
  summary: IPR058622 exactly grounds TolC. IPR005694/TIGR00998 include multiple membrane-fusion
    proteins; IPR004638/TIGR00711 include broader EmrB-like transporters. These inspected
    candidates do not force exact EmrK-only or EmrY-only mappings. The remaining source-neutral
    task stays open without a universal claim that no family could exist.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-family-IPR058622
  - micro-family-IPR005694-retry
  - micro-family-TIGR00998
  - micro-family-IPR004638
  - micro-family-TIGR00711
  - micro-policy
- assessment_id: micro-emrky-primary
  area: evidence
  topic: May experimental readout and limitations
  outcome: supported
  summary: The actual Methods and Results distinguish MG1655/pBR322 from modified
    OCL62 and multiple changed loci/regulation. Expression, biofilm and drug response
    are not direct assembly readouts. Maintained source-tier qualifications are appropriate;
    the paper does not provide each subunit formation necessity or exact EmrK/Y counts.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-PMC2772303-legacy
  - micro-pmid-19721076
  - micro-complex-CPX-4273
- assessment_id: micro-emrky-function
  area: graph
  topic: Whole-system export versus microscopic mechanism
  outcome: supported
  summary: The original coupling, whole-pump transport and exterior-target edges plus
    new coarse export link are supported at the retained inferred/nonmechanistic boundary.
    No residue-level antiport states, gating cycle or experimentally resolved architecture
    is claimed. GO0140330 is process identity, not direct proof of every molecular
    step.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-complex-CPX-4273
  - micro-go-0042910
  - micro-go-0140330
  - micro-graph-policy
- assessment_id: micro-sec-identity
  area: identity
  topic: Parent Sec complex and two subcomplexes
  outcome: supported
  summary: GO0031205 exactly denotes the parent ER Sec complex; GO0140534 is an is-a
    ancestor and GO0005789 the membrane location. Sec61 GO0005784 and Sec62/Sec63
    GO0031207 are legitimate subcomplexes. Individual subunit duplication is not required
    at this parent level.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
  - micro-go-0031205
  - micro-ancestors-GO0031205
  - micro-go-0140534
  - micro-go-0005789
  - micro-go-0005784
  - micro-go-0031207
  - micro-policy
- assessment_id: micro-sec-primary
  area: evidence
  topic: Reconstitution and precursor interaction sources
  outcome: supported
  summary: Panzner is presently complete indexed abstract only and supports the purified
    yeast Sec/Kar2 reconstitution summary at that tier. Genuine Plath Methods/Results
    independently show specific precursor-Sec61/Sec62 crosslinks and distinguish initial
    binding from later Kar2-dependent transport. No inaccessible Panzner body is certified.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
  - micro-doi-0
  - micro-doi-1
  - micro-PMC307522-legacy
  - micro-access-panzner1995-publisher
  - micro-access-panzner1995-pii
- assessment_id: micro-sec-structure
  area: evidence
  topic: Structural extent and source strain
  outcome: supported
  summary: Wu BY4741 purification and overall seven-component architecture support
    the subcomplex topology. Sec62 has limited density/model coverage; the current
    generic structurally-resolved wording is not treated as an assertion that all
    residues/subunits were atomically resolved. Reference yeast species is appropriately
    broader than the preparation.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
  - micro-doi-2
  - micro-PMC6367035-legacy
  - micro-taxon-4932
  - micro-taxon-559292
- assessment_id: micro-sec-graph
  area: graph
  topic: Coarse import and membrane placement
  outcome: supported
  summary: Four graph edges describe two subcomplex memberships, ER-membrane placement
    and support for posttranslational import. Kar2/BiP is a separate coupled factor,
    not automatically a constituent. No universal individual-subunit essentiality,
    missing optional examples or absent complete mechanism is manufactured as a finding.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
  - micro-PMC307522-legacy
  - micro-PMC6367035-legacy
  - micro-doi-0
  - micro-graph-policy
- assessment_id: micro-sec-history
  area: scope
  topic: Resolved nonduplication discussion
  outcome: supported
  summary: The existing resolved discussion documents the chosen parent/subcomplex
    boundary. Current evidence supports that representation; it is not a new terminal
    disposition of unrelated lower-level records or historical issues.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-go-0031205
  - micro-policy
- assessment_id: micro-pol-identity
  area: identity
  topic: Heterotetrameric Pol-epsilon identity
  outcome: supported
  summary: GO0008622 is exact and GO0042575 a genuine broader class. The definition
    is faithfully GO-derived, including cautious historical leading-strand wording
    and PCNA stimulation. The current graph explicitly withholds detailed leading-strand
    assignment, replisome engagement and repair mechanisms.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-go-0008622
  - micro-ancestors-GO0008622
  - micro-go-0042575
  - micro-go-0006260
- assessment_id: micro-pol-stoichiometry
  area: evidence
  topic: Four-subunit preparation and structural scope
  outcome: supported
  summary: The complete Chilkova indexed abstract explicitly supports the purified
    yeast1:1:1:1 heterotetramer. Correct publisher PDF route is blocked and no body
    is newly certified. Asturias abstract/publisher metadata and Ganai inspected biochemical
    sections supply separate architecture/activity context without transferring assay
    conditions to all species.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-pmid-12571237
  - micro-access-chilkova2003-correct-pdf
  - micro-pmid-16369485
  - micro-asturias2006-publisher
  - micro-PMC4319046-legacy
- assessment_id: micro-pol-families
  area: grounding
  topic: Available Pol2, Dpb2 and Dpb4 family mappings
  outcome: concern
  summary: Native IPR029703 and IPR016266 match Pol2 and Dpb2; IPR051377 and its complete
    reviewed-member list match the homologous Dpb4/POLE3 class, corroborated by Q04603.
    These available mappings support narrowing the open task. LLM-flagged prose is
    not primary support; broad IPR050568/shared histone folds do not settle exact
    Dpb3.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-family-IPR029703
  - micro-family-IPR016266
  - micro-family-IPR051377
  - micro-IPR051377-reviewed-retry
  - micro-family-IPR050568
  - micro-protein-P21951
  - micro-protein-P24482
  - micro-protein-P27344
  - micro-protein-Q04603
  - micro-policy
- assessment_id: micro-pol-stability
  area: evidence
  topic: Condition-scoped Dpb4 physical stability
  outcome: concern
  summary: Ohya sec15 directly shows easier Dpb2/Dpb3 dissociation from Pol2 after
    MonoQ purification of dpb4-deletion extracts, with active-fraction mixture and
    degradation limits. The current role/graph omits this bounded physical stability
    observation. Add it without forcing global ESSENTIAL, a new assay, or equating
    viability/activity with assembly.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-PMC110797-legacy
  - micro-schema
  - micro-graph-policy
- assessment_id: micro-pol-localization
  area: evidence
  topic: Example annotations and independent source tiers
  outcome: supported
  summary: Reviewed S288C identities match the four maintained genes/loci. Dpb2 Cytoplasm/Nucleus
    native annotations and Huh abstract, plus Dpb3/4 Ohya-associated annotation context,
    are not blanket proof of the whole complex at every listed location. Individual
    localization supplement rows were not freshly inspected.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-protein-P21951
  - micro-protein-P24482
  - micro-protein-P27344
  - micro-protein-Q04603
  - micro-pmid-14562095
  - micro-pmid-11024162
  - micro-PMC110797-legacy
- assessment_id: micro-pol-graph
  area: graph
  topic: Membership and DNA replication boundary
  outcome: supported
  summary: Four membership edges and whole-complex DNA replication support are valid
    at declared NONMECHANISTIC scope. Ganai whole-enzyme versus truncated Pol2 comparisons
    do not isolate necessity of each accessory protein. Current UNKNOWN values may
    remain alongside the bounded Dpb4 evidence.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-go-0008622
  - micro-pmid-12571237
  - micro-PMC4319046-legacy
  - micro-schema
- assessment_id: micro-ermes-identity
  area: identity
  topic: Exact ERMES identity and spanning contact topology
  outcome: supported
  summary: GO0032865 exact identity and its four synonyms are confirmed. Both ER and
    outer mitochondrial complex ancestry are native; tether topology spans the organelles
    and does not mean every constituent is exclusively mitochondrial. Mmm1 ER localization
    and Mdm10 shared SAM membership remain distinct.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
  - micro-go-0032865
  - micro-ancestors-GO0032865
  - micro-go-0098799
  - micro-PMC2933203-legacy
  - micro-go-0005783
  - micro-go-0005741
- assessment_id: micro-ermes-core
  area: completeness
  topic: Known core versus exact-family prerequisite
  outcome: concern
  summary: The current prompt expressly defers all Mmm1/Mdm10/Mdm12/Mdm34 rows until
    exact family groundings. Kornmann and Kawano directly identify this core; native
    reviewed-label-only representation permits honest known membership before every
    exact family is resolved. This is an explicit current prerequisite gap, not a
    generic demand to fill every optional inventory.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
  - micro-PMC2933203-legacy
  - micro-PMC5839780-legacy
  - micro-policy
  - micro-schema
- assessment_id: micro-ermes-lipid
  area: evidence
  topic: Mmm1-Mdm12 module versus whole in-vivo ERMES
  outcome: supported
  summary: The maintained graph already restricts direct lipid transfer to an in-vitro
    Mmm1-Mdm12 module. Kawano model-membrane, K.lactis recombinant and S.cerevisiae
    heavy-membrane-fraction experiments remain distinct; carrier/conduit interpretations
    and complete in-vivo exchange are not asserted as settled.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
  - micro-PMC5839780-legacy
  - micro-doi-4
  - micro-go-0032865
- assessment_id: micro-ermes-primary
  area: scope
  topic: Synthetic-tether and mutant preparation bounds
  outcome: supported
  summary: Kornmann synthetic-tether screen, localization/rescue and loss-of-puncta
    observations support the identified yeast core and tether role. These are not
    an exhaustive copy-number inventory or universal necessity classifications; peripheral
    Gem1/Tom7 and optional protein instances are not required by this finding.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
  - micro-PMC2933203-legacy
  - micro-PMC5839780-legacy
  - micro-doi-3
  - micro-taxon-4932
- assessment_id: micro-ermes-graph
  area: graph
  topic: Structure-level tether and module relations
  outcome: supported
  summary: Three edges describe native outer-membrane classification, ER linking and
    an explicitly limited lipid-transfer module. Current coarse FUNCTION/NONMECHANISTIC
    graph is scientifically bounded. No automatic GENE_OR_PROTEIN conversion or added
    mechanistic chain is required.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
  - micro-go-0032865
  - micro-ancestors-GO0032865
  - micro-PMC2933203-legacy
  - micro-PMC5839780-legacy
  - micro-graph-policy
- assessment_id: micro-proteins-0
  area: grounding
  topic: Current example inventory and identity scope
  outcome: supported
  summary: 3 reviewed maintained examples match native genes/loci/taxa and current
    bounded queries. Current singleton results do not reconstruct historical selection
    queries. Family-level grounding and primary biological evidence remain separate.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-protein-P52599
  - micro-protein-P52600
  - micro-protein-P02930
  - micro-query-emrK
  - micro-query-emrY
  - micro-query-tolC
- assessment_id: micro-adapter-0
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: 'Original formal exclusion incorrectly relies on absence of expression
    claims despite positive named protein/pathway assertions. Fresh E.coli precise1k
    five-strain metadata and exact three locus/native-accession joins were inspected
    across201 modules: EmrK/EmrY in15-member EvgA38 and TolC in117-member SoxS22.
    This is not the May construct or assembly evidence. Historical runner unavailability
    remains separately dated.'
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-dataset-meta
  - micro-dataset-genes
  - micro-membership-b2368
  - micro-membership-b2367
  - micro-membership-b3035
  - micro-module-22-genes
  - micro-module-38-genes
- assessment_id: micro-history-0
  area: scope
  topic: Immutable historical provenance and current finding lineage
  outcome: supported
  summary: One inherited major is rejected as formulated, with exact lineage and no
    curation action for it; a distinct new minor source-attribution finding has no
    invented predecessor. Preserve rationale, posed_date, dated curation events and
    all original artifacts; no records are edited here.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-prior-0
  - micro-delta-0
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-0
  area: schema
  topic: Actual native checks and original artifacts
  outcome: supported
  summary: 3 reviewed examples and 3 COVERED typed nodes. Actual source-head verify/causal
    commands exit0; original native validate/render and recorded historical hashes
    pass. These checks do not certify source completeness or future successor/CI gates.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-native-emrky_tolc_multidrug_efflux_transport_complex-verify
  - micro-native-emrky_tolc_multidrug_efflux_transport_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-0
  area: scope
  topic: Images, measurements and optional scope
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    pixel inspection. Paper text captions were read only at declared extents; no microscopy
    pixels, supplementary movies, coordinate analysis or optional imaging requirement
    is claimed.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-0
  - micro-policy
- assessment_id: micro-proteins-1
  area: grounding
  topic: Current example inventory and identity scope
  outcome: not_applicable
  summary: No maintained protein examples or typed protein nodes. Native success has
    empty coverage; no optional examples are required solely from that absence. Family-level
    grounding and primary biological evidence remain separate.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
- assessment_id: micro-adapter-1
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal exclusion incorrectly relies on absence of expression claims
    despite positive named protein/pathway assertions. Fresh complete catalogue has
    no matching Saccharomyces dataset; no unrelated bacterial proxy or invented downstream
    query is used. Historical runner unavailability remains separately dated.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-1
  area: scope
  topic: Immutable historical provenance and current finding lineage
  outcome: supported
  summary: Original qualified-pass result remains supported within stated source limits.
    Preserve rationale, posed_date, dated curation events and all original artifacts;
    no records are edited here.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-prior-1
  - micro-delta-1
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-1
  area: schema
  topic: Actual native checks and original artifacts
  outcome: supported
  summary: 0 reviewed examples and 0 COVERED typed nodes. Actual source-head verify/causal
    commands exit0; original native validate/render and recorded historical hashes
    pass. These checks do not certify source completeness or future successor/CI gates.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-native-endoplasmic_reticulum_sec_complex-verify
  - micro-native-endoplasmic_reticulum_sec_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-1
  area: scope
  topic: Images, measurements and optional scope
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    pixel inspection. Paper text captions were read only at declared extents; no microscopy
    pixels, supplementary movies, coordinate analysis or optional imaging requirement
    is claimed.
  target_ids:
  - GO:0031205
  evidence_ids:
  - micro-record-1
  - micro-policy
- assessment_id: micro-proteins-2
  area: grounding
  topic: Current example inventory and identity scope
  outcome: supported
  summary: 4 reviewed maintained examples match native genes/loci/taxa and current
    bounded queries. Current singleton results do not reconstruct historical selection
    queries. Family-level grounding and primary biological evidence remain separate.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-protein-P21951
  - micro-protein-P24482
  - micro-protein-P27344
  - micro-protein-Q04603
  - micro-query-DPB2
  - micro-query-DPB3
  - micro-query-DPB4
  - micro-query-POL2
- assessment_id: micro-adapter-2
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal exclusion incorrectly relies on absence of expression claims
    despite positive named protein/pathway assertions. Fresh complete catalogue has
    no matching Saccharomyces dataset; no unrelated bacterial proxy or invented downstream
    query is used. Historical runner unavailability remains separately dated.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-2
  area: scope
  topic: Immutable historical provenance and current finding lineage
  outcome: supported
  summary: Two inherited minors remain with exact lineage, available class mapping
    and bounded Dpb4 stability action. Preserve rationale, posed_date, dated curation
    events and all original artifacts; no records are edited here.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-prior-2
  - micro-delta-2
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-2
  area: schema
  topic: Actual native checks and original artifacts
  outcome: supported
  summary: 4 reviewed examples and 4 COVERED typed nodes. Actual source-head verify/causal
    commands exit0; original native validate/render and recorded historical hashes
    pass. These checks do not certify source completeness or future successor/CI gates.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-native-epsilon_dna_polymerase_complex-verify
  - micro-native-epsilon_dna_polymerase_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-2
  area: scope
  topic: Images, measurements and optional scope
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    pixel inspection. Paper text captions were read only at declared extents; no microscopy
    pixels, supplementary movies, coordinate analysis or optional imaging requirement
    is claimed.
  target_ids:
  - GO:0008622
  evidence_ids:
  - micro-record-2
  - micro-policy
- assessment_id: micro-proteins-3
  area: grounding
  topic: Current example inventory and identity scope
  outcome: not_applicable
  summary: No maintained protein examples or typed protein nodes. Native success has
    empty coverage; no optional examples are required solely from that absence. Family-level
    grounding and primary biological evidence remain separate.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
- assessment_id: micro-adapter-3
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original prose exclusion incorrectly relies on absence of expression claims
    despite positive named protein/pathway assertions. Fresh complete catalogue has
    no matching Saccharomyces dataset; no unrelated bacterial proxy or invented downstream
    query is used. Historical runner unavailability remains separately dated.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-prior-3
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-3
  area: scope
  topic: Immutable historical provenance and current finding lineage
  outcome: supported
  summary: Inherited minor targets the explicit current prerequisite in the prompt,
    not the truth or wording of the dated rationale. Preserve rationale, posed_date,
    dated curation events and all original artifacts; no records are edited here.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-prior-3
  - micro-delta-3
  - micro-policy
  - micro-original-audit
- assessment_id: micro-native-3
  area: schema
  topic: Actual native checks and original artifacts
  outcome: supported
  summary: 0 reviewed examples and 0 COVERED typed nodes. Actual source-head verify/causal
    commands exit0; original native validate/render and recorded historical hashes
    pass. These checks do not certify source completeness or future successor/CI gates.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-native-ermes_complex-verify
  - micro-native-ermes_complex-causal
  - micro-original-audit
- assessment_id: micro-physical-3
  area: scope
  topic: Images, measurements and optional scope
  outcome: not_applicable
  summary: No maintained image or quantitative physical-property assertion requires
    pixel inspection. Paper text captions were read only at declared extents; no microscopy
    pixels, supplementary movies, coordinate analysis or optional imaging requirement
    is claimed.
  target_ids:
  - GO:0032865
  evidence_ids:
  - micro-record-3
  - micro-policy
- assessment_id: plaque-t4-identity-and-definition
  area: identity
  topic: identity-and-definition
  outcome: concern
  summary: Correct ESCRT-0 identity is retained, but the active definition faithfully
    copies the current GO Vps1 error. Exact synonym, Bilodeau abstract, current Vps27/Hse1
    identities and the record own resolved discussion contradict that localized name.
    Correct active wording/source transparency without rewriting dated rationale.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-go
  - plaque-pmid-12055639
  - plaque-up-P40343
  - plaque-up-P38753
- assessment_id: plaque-t4-hierarchy-and-topology
  area: scope
  topic: hierarchy-and-topology
  outcome: supported
  summary: Native is_a-only ancestors and typed parent children support the maintained
    hierarchy. Direct endosome/endosome-membrane parthood is checked separately against
    typed relations; none is inferred from mere ancestry.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-go
  - plaque-go-0033565-ancestors
- assessment_id: plaque-t4-components-and-family-grounding
  area: grounding
  topic: components-and-family-grounding
  outcome: concern
  summary: Vps27/Hse1 membership is supported. Exact IPR017073 resolves the already-open
    Vps27/Hrs mapping; mixed IPR050670/PTHR45929 is not forced onto Hse1. This is
    a bounded existing task, not an optional-inventory mandate.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-curation
  - plaque-ipr-IPR017073
  - plaque-up-P40343
  - plaque-ipr-IPR050670
  - plaque-members-IPR050670
  - plaque-panther-PTHR45929
- assessment_id: plaque-t4-protein-identity-and-native-coverage
  area: grounding
  topic: protein-identity-and-native-coverage
  outcome: supported
  summary: Two reviewed protein_examples and two COVERED typed protein nodes. Native
    success is identifier/coverage evidence only; current protein names, aliases,
    loci, review status and taxa are independently checked. Reference S288C is not
    silently equated with experimental SEY6210.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-native-escrt_0_complex-verify
  - plaque-native-escrt_0_complex-causal
  - plaque-up-P40343
  - plaque-up-P38753
  - plaque-gene-VPS27
  - plaque-gene-HSE1
- assessment_id: plaque-t4-taxon-and-experimental-scope
  area: scope
  topic: taxon-and-experimental-scope
  outcome: supported
  summary: S. cerevisiae species and S288C reference-strain identifiers are current.
    Katzmann/Chu/Curtiss selected Methods identify SEY6210 derivatives; E.coli expression
    is not the natural host. COMMON retains the native majority-occurrence meaning,
    but these studies supply qualitative support rather than a prevalence census.
    Mammalian synonyms do not export yeast perturbations universally.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-PMC2172707-body
  - plaque-PMC2064680-body
  - plaque-PMC1783790-body
  - plaque-structure-schema
- assessment_id: plaque-t4-function-and-primary-support
  area: evidence
  topic: function-and-primary-support
  outcome: supported
  summary: Bilodeau primary abstract supports Ub recognition and sorting; Katzmann
    directly supports the specifically represented Vps27 recruitment actor. UIM sorting
    defects are not conflated with loss of all lumenal membrane production.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-go
  - plaque-pmid-12055639
  - plaque-pmid-21763610
  - plaque-pmid-11511343
  - plaque-PMC2172707-body
- assessment_id: plaque-t4-localisation-and-provenance
  area: provenance
  topic: localisation-and-provenance
  outcome: supported
  summary: Native endosome-membrane annotations retain the cited ECO/PMIDs. Stahelin
    supports isolated FYVE-domain binding; Huh abstract establishes survey provenance,
    not fresh viewing of individual microscopy.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-go
  - plaque-pmid-12006563
  - plaque-pmid-14562095
  - plaque-up-P40343
  - plaque-up-P38753
- assessment_id: plaque-t4-graph-and-formation-boundaries
  area: graph
  topic: graph-and-formation-boundaries
  outcome: supported
  summary: NONMECHANISTIC graph correctly separates two memberships, Ub binding, Vps27-specific
    recruitment and MVB participation. Hse1 universal recruitment dependence is not
    asserted.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-graph-skill
  - plaque-go
  - plaque-PMC2172707-body
  - plaque-native-escrt_0_complex-verify
  - plaque-native-escrt_0_complex-causal
- assessment_id: plaque-t4-necessity-and-inventory-limits
  area: evidence
  topic: necessity-and-inventory-limits
  outcome: unknown
  summary: Sorting, localization, Ub binding, viability and subcomplex recovery do
    not establish a universal individual formation table. Both UNKNOWN rows remain
    legitimate.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-curation
  - plaque-structure-schema
  - plaque-PMC2172707-body
  - plaque-PMC1783790-body
- assessment_id: plaque-t4-structured-source-applicability
  area: evidence
  topic: structured-source-applicability
  outcome: supported
  summary: Positive protein constituent and Ub-sorting/recruitment assertions trigger
    the native broad structured-source policy. Complete fresh official catalogue has
    no matching natural-host dataset; no proxy downstream query is warranted. The
    old notes[1] expression-only exclusion is unsupported even though present bounded
    catalogue noncoverage is legitimate. Historical runner unavailability remains
    historical; no fresh runner invocation or negative biological conclusion is claimed.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-review-skill
  - plaque-rubric
  - plaque-catalogue
- assessment_id: plaque-t4-schema-history-and-verdict
  area: schema
  topic: schema-history-and-verdict
  outcome: concern
  summary: All47 current frozen inputs and41 own historical input occurrences match;3
    originals validate/render exactly and own targets are unchanged. Needs_curation
    retained for two reconfirmed inherited minor finding(s). Historical rationale
    and prior corrections remain intact; no terminal disposition of unrelated issues
    or future CI/queue/merge certification is made. Three historical access-kind occurrence(s)
    require successor classification correction; old context_only disclosures were
    honest.
  target_ids:
  - GO:0033565
  evidence_ids:
  - plaque-record-4
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-review-contract
  - plaque-curation
  - plaque-original-4-yaml
  - plaque-native-escrt_0_complex-verify
  - plaque-native-escrt_0_complex-causal
- assessment_id: plaque-t5-identity-and-definition
  area: identity
  topic: identity-and-definition
  outcome: supported
  summary: The generic ESCRT parent denotes a class of distinct complexes, not one
    combined fixed-stoichiometry supercomplex. Its broad membrane-fission definition
    and five child identities are consistent.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-pmid-21763610
- assessment_id: plaque-t5-hierarchy-and-topology
  area: scope
  topic: hierarchy-and-topology
  outcome: supported
  summary: Native is_a-only ancestors and typed parent children support the maintained
    hierarchy. Direct endosome/endosome-membrane parthood is checked separately against
    typed relations; none is inferred from mere ancestry.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-go-0036452-ancestors
- assessment_id: plaque-t5-components-and-family-grounding
  area: grounding
  topic: components-and-family-grounding
  outcome: supported
  summary: The deliberately empty parent component/example table preserves distinct
    child assemblies. Historical future-record wording is not treated as a present
    corpus-absence claim.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-curation
  - plaque-go
- assessment_id: plaque-t5-protein-identity-and-native-coverage
  area: grounding
  topic: protein-identity-and-native-coverage
  outcome: supported
  summary: Zero protein_examples and zero typed protein nodes; positive pathway assertions
    remain subject to source review. Native success is identifier/coverage evidence
    only; current protein names, aliases, loci, review status and taxa are independently
    checked. Reference S288C is not silently equated with experimental SEY6210.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-native-escrt_complex-verify
  - plaque-native-escrt_complex-causal
  - plaque-go
- assessment_id: plaque-t5-taxon-and-experimental-scope
  area: scope
  topic: taxon-and-experimental-scope
  outcome: supported
  summary: S. cerevisiae species and S288C reference-strain identifiers are current.
    Katzmann/Chu/Curtiss selected Methods identify SEY6210 derivatives; E.coli expression
    is not the natural host. COMMON retains the native majority-occurrence meaning,
    but these studies supply qualitative support rather than a prevalence census.
    Mammalian synonyms do not export yeast perturbations universally.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-PMC2172707-body
  - plaque-PMC2064680-body
  - plaque-PMC1783790-body
  - plaque-structure-schema
- assessment_id: plaque-t5-function-and-primary-support
  area: evidence
  topic: function-and-primary-support
  outcome: supported
  summary: GO and Henne complete secondary abstract support broad MVB sorting and
    membrane remodeling; Katzmann provides supplementary primary yeast context. Detailed
    Henne main-body mechanisms remain unread, and child-specific primary assays are
    not reassigned to the review.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-pmid-12055639
  - plaque-pmid-21763610
  - plaque-pmid-11511343
  - plaque-PMC2172707-body
- assessment_id: plaque-t5-localisation-and-provenance
  area: provenance
  topic: localisation-and-provenance
  outcome: supported
  summary: Generic endosomal context is supported by typed GO and the scoped review
    abstract; no parent-wide fixed subunit or location mechanism is added.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-pmid-21763610
- assessment_id: plaque-t5-graph-and-formation-boundaries
  area: graph
  topic: graph-and-formation-boundaries
  outcome: supported
  summary: NONMECHANISTIC graph contains five is_a child edges, typed endosome parthood
    and coarse MVB participation. It does not assert that all ESCRT subcomplexes always
    form one assembly or a universal handoff mechanism.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-graph-skill
  - plaque-go
  - plaque-PMC2172707-body
  - plaque-native-escrt_complex-verify
  - plaque-native-escrt_complex-causal
- assessment_id: plaque-t5-necessity-and-inventory-limits
  area: evidence
  topic: necessity-and-inventory-limits
  outcome: unknown
  summary: Sorting, localization, Ub binding, viability and subcomplex recovery do
    not establish a universal individual formation table. No generic constituent necessity
    or fixed stoichiometry is asserted.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-curation
  - plaque-structure-schema
  - plaque-PMC2172707-body
  - plaque-PMC1783790-body
- assessment_id: plaque-t5-structured-source-applicability
  area: evidence
  topic: structured-source-applicability
  outcome: supported
  summary: Positive MVB-sorting and named ESCRT pathway assertions trigger the native
    broad structured-source policy. Complete fresh official catalogue has no matching
    natural-host dataset; no proxy downstream query is warranted. The old notes[1]
    expression-only exclusion is unsupported even though present bounded catalogue
    noncoverage is legitimate. Historical runner unavailability remains historical;
    no fresh runner invocation or negative biological conclusion is claimed.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-review-skill
  - plaque-rubric
  - plaque-catalogue
- assessment_id: plaque-t5-schema-history-and-verdict
  area: schema
  topic: schema-history-and-verdict
  outcome: supported
  summary: All47 current frozen inputs and41 own historical input occurrences match;3
    originals validate/render exactly and own targets are unchanged. Qualified pass
    retained with explicit abstract/body and class-boundary limits. Historical rationale
    and prior corrections remain intact; no terminal disposition of unrelated issues
    or future CI/queue/merge certification is made. One historical access-kind occurrence(s)
    require successor classification correction; old context_only disclosures were
    honest.
  target_ids:
  - GO:0036452
  evidence_ids:
  - plaque-record-5
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-review-contract
  - plaque-curation
  - plaque-original-5-yaml
  - plaque-native-escrt_complex-verify
  - plaque-native-escrt_complex-causal
- assessment_id: plaque-t6-identity-and-definition
  area: identity
  topic: identity-and-definition
  outcome: supported
  summary: GO0000813 identifies ESCRT-I; three supported yeast core proteins are historically
    scoped and the current Mvb12 discussion expressly acknowledges later composition.
    No exhaustive three-protein assertion is inferred.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-go
  - plaque-pmid-11511343
  - plaque-PMC2064680-body
  - plaque-PMC1783790-body
- assessment_id: plaque-t6-hierarchy-and-topology
  area: scope
  topic: hierarchy-and-topology
  outcome: supported
  summary: Native is_a-only ancestors and typed parent children support the maintained
    hierarchy. Direct endosome/endosome-membrane parthood is checked separately against
    typed relations; none is inferred from mere ancestry.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-go
  - plaque-go-0000813-ancestors
- assessment_id: plaque-t6-components-and-family-grounding
  area: grounding
  topic: components-and-family-grounding
  outcome: concern
  summary: Current exact type/member joins support Vps23 IPR052070, Vps28 IPR007143
    and explicitly fungal Vps37 IPR017435. Generated descriptions, shared UEV/Modr
    domains and contradictory old stoichiometry prose are not used as class evidence.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-curation
  - plaque-ipr-IPR052070
  - plaque-family-query-IPR052070
  - plaque-ipr-IPR007143
  - plaque-ipr-IPR017435
  - plaque-ipr-IPR009851
  - plaque-up-P25604
  - plaque-up-Q02767
  - plaque-up-Q99176
- assessment_id: plaque-t6-protein-identity-and-native-coverage
  area: grounding
  topic: protein-identity-and-native-coverage
  outcome: supported
  summary: Three reviewed protein_examples; four typed protein nodes comprise three
    COVERED constituents and the external Vps27 recruiter UNANCHORED_WITH_UNIPROT
    P40343. This intentional external actor is not a missing constituent. Native success
    is identifier/coverage evidence only; current protein names, aliases, loci, review
    status and taxa are independently checked. Reference S288C is not silently equated
    with experimental SEY6210.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-native-escrt_i_complex-verify
  - plaque-native-escrt_i_complex-causal
  - plaque-up-P25604
  - plaque-up-Q02767
  - plaque-up-Q99176
  - plaque-up-P40343
  - plaque-gene-VPS23
  - plaque-gene-VPS28
  - plaque-gene-VPS37
- assessment_id: plaque-t6-taxon-and-experimental-scope
  area: scope
  topic: taxon-and-experimental-scope
  outcome: supported
  summary: S. cerevisiae species and S288C reference-strain identifiers are current.
    Katzmann/Chu/Curtiss selected Methods identify SEY6210 derivatives; E.coli expression
    is not the natural host. COMMON retains the native majority-occurrence meaning,
    but these studies supply qualitative support rather than a prevalence census.
    Mammalian synonyms do not export yeast perturbations universally.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-PMC2172707-body
  - plaque-PMC2064680-body
  - plaque-PMC1783790-body
  - plaque-structure-schema
- assessment_id: plaque-t6-function-and-primary-support
  area: evidence
  topic: function-and-primary-support
  outcome: supported
  summary: Katzmann2001 complete primary abstract and Katzmann2003 selected body support
    Ub cargo recognition, external Vps27 recruitment and MVB sorting. Apparent350kDa
    characterization is not an exact copy-number or modern exhaustive inventory claim.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-go
  - plaque-pmid-12055639
  - plaque-pmid-21763610
  - plaque-pmid-11511343
  - plaque-PMC2172707-body
- assessment_id: plaque-t6-localisation-and-provenance
  area: provenance
  topic: localisation-and-provenance
  outcome: supported
  summary: Native Vps37/SRN2 cytoplasmic ECO0000269 citation matches Hong1998 abstract;
    inferred endosomal annotations are not promoted to direct images. External Vps27
    remains a recruiter, not a stable ESCRT-I constituent.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-up-Q99176
  - plaque-pmid-9790597
  - plaque-PMC2172707-body
- assessment_id: plaque-t6-graph-and-formation-boundaries
  area: graph
  topic: graph-and-formation-boundaries
  outcome: supported
  summary: NONMECHANISTIC graph correctly separates three historical core memberships,
    external Vps27 recruitment, endosomal localization and sorting. Correct node diagnostics
    do not establish stronger causal necessity.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-graph-skill
  - plaque-go
  - plaque-PMC2172707-body
  - plaque-native-escrt_i_complex-verify
  - plaque-native-escrt_i_complex-causal
- assessment_id: plaque-t6-necessity-and-inventory-limits
  area: evidence
  topic: necessity-and-inventory-limits
  outcome: unknown
  summary: Sorting, localization, Ub binding, viability and subcomplex recovery do
    not establish a universal individual formation table. Mvb12 is positively acknowledged,
    and the cited deletion experiments retain partial subcomplexes. The optional unlisted
    Mvb12 row is not described as biological absence; no compulsory complete inventory
    or universal ESSENTIAL value is invented.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-curation
  - plaque-structure-schema
  - plaque-PMC2172707-body
  - plaque-PMC1783790-body
- assessment_id: plaque-t6-structured-source-applicability
  area: evidence
  topic: structured-source-applicability
  outcome: supported
  summary: Positive protein constituent, Ub-cargo and recruitment assertions trigger
    the native broad structured-source policy. Complete fresh official catalogue has
    no matching natural-host dataset; no proxy downstream query is warranted. The
    old formal exclusion is unsupported even though present bounded catalogue noncoverage
    is legitimate. Historical runner unavailability remains historical; no fresh runner
    invocation or negative biological conclusion is claimed.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-review-skill
  - plaque-rubric
  - plaque-catalogue
- assessment_id: plaque-t6-schema-history-and-verdict
  area: schema
  topic: schema-history-and-verdict
  outcome: concern
  summary: All47 current frozen inputs and41 own historical input occurrences match;3
    originals validate/render exactly and own targets are unchanged. Needs_curation
    retained for one grouped reconfirmed inherited minor finding(s). Historical rationale
    and prior corrections remain intact; no terminal disposition of unrelated issues
    or future CI/queue/merge certification is made. No historical access-kind occurrence(s)
    require successor classification correction; old context_only disclosures were
    honest.
  target_ids:
  - GO:0000813
  evidence_ids:
  - plaque-record-6
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-review-contract
  - plaque-curation
  - plaque-original-6-yaml
  - plaque-native-escrt_i_complex-verify
  - plaque-native-escrt_i_complex-causal
- assessment_id: septin-escrt_ii_complex-identity
  area: identity
  topic: Exact structure and hierarchy
  outcome: supported
  summary: GO0000814 denotes the ESCRT-II complex; yeast three constituent classes
    and source-specific1:2:1 architecture are supported. Parent is_a and endosome
    part_of remain distinct.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-GO0000814-ancestors
- assessment_id: septin-escrt_ii_complex-families
  area: grounding
  topic: Exact full-component classes versus domains and paralog groups
  outcome: concern
  summary: Current native family/protein joins independently resolve Vps22/Snf8 IPR016689,Q12483;
    Vps25 IPR008570,P47142; Vps36 IPR037855,Q06696. The inherited bounded exact-mapping
    finding remains open.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-ipr-IPR016689
  - septin-ipr-IPR008570
  - septin-ipr-IPR037855
  - septin-curation-policy
- assessment_id: septin-escrt_ii_complex-protein-identity
  area: grounding
  topic: Accession, primary name, aliases and status
  outcome: supported
  summary: All 3 native reviewed S288C examples and current exact-gene queries match.
    VPS22 is synonym of primary SNF8. Identity joins do not themselves establish membership.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-gene-VPS22-559292
  - septin-gene-VPS25-559292
  - septin-gene-VPS36-559292
  - septin-protein-policy
- assessment_id: septin-escrt_ii_complex-sources
  area: evidence
  topic: Experimental source tier and actual read scope
  outcome: supported
  summary: Fresh Teo author PDF and Im2008/2009 bodies support anatomy, direct interactions
    and activation; Hierro and Babst limited to full primary abstracts. Human constructs,
    yeast assays and recombinant expression remain separate.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-literature-policy
- assessment_id: septin-escrt_ii_complex-stoichiometry
  area: grounding
  topic: Counts and assembly interpretation
  outcome: supported
  summary: One Vps22, two Vps25 and one Vps36 are supported in source-specific cores.
    Existing optional stoichiometry TODO is acknowledged; no mandatory-field defect
    is invented.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
- assessment_id: septin-escrt_ii_complex-formation
  area: grounding
  topic: Formation versus activity and targeting
  outcome: unknown
  summary: UNKNOWN formation values remain justified within this source scope. Targeting
    defects, direct interface binding and cargo sorting do not establish blanket whole-protein
    formation necessity; Teo truncation and Im activation contexts are kept explicit.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-schema-policy
- assessment_id: septin-escrt_ii_complex-graph
  area: graph
  topic: Complete coarse function graph
  outcome: supported
  summary: ESCRT-II membership, transient endosomal association and activation of
    downstream ESCRT-III are supported. Im2009 retained membrane localization of Vps20
    lacking ESCRT-II binding distinguishes single-protein targeting from activation
    of the machinery.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-graph-policy
- assessment_id: septin-escrt_ii_complex-taxa
  area: scope
  topic: Biological, reference and expression-host scope
  outcome: supported
  summary: Canonical S.cerevisiae species is correct; Teo ATCC9763D material expressed
    in C41/B834 differs from S288C reference entries. Im2008 human proteins/BY4741
    and Im2009 human fragment/BY4742 and yeast GUV reagents remain separate. COMMON
    is qualitative source-supported species scope, not a measured population census.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-tax4932
  - septin-tax559292
- assessment_id: septin-escrt_ii_complex-applicability
  area: evidence
  topic: Current host-sensitive structured-source assessment
  outcome: supported
  summary: Named proteins and positive sorting/recycling pathway claims trigger policy
    assessment. Complete fresh official catalogue has no yeast or human host; downstream
    module queries are not applicable. Bacterial recombinant expression hosts are
    not biological-host substitutes. Historical unavailable runner is distinct from
    current catalogue fallback; no expression-to-assembly inference.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-escrt_ii_complex-schema
  area: schema
  topic: Original validation, provenance and native coverage
  outcome: supported
  summary: Three original validate/render pairs pass with exact Markdown and39 frozen
    historical occurrences. Current target is unchanged. Actual focused native protein
    checks exit0 with populated inventory; native coverage is not biological proof.
    Root global/future gates are separate.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-original-native-checks
  - septin-native-escrt_ii_complex-verify
  - septin-native-escrt_ii_complex-causal
- assessment_id: septin-escrt_ii_complex-history
  area: provenance
  topic: Append-only history and exact finding lineage
  outcome: supported
  summary: Historical rationale and all dated entries remain immutable. Separately
    authorized curation may update current notes/status or append clarification; inherited
    finding references preserve exact repository/review/finding identity.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-curation-policy
- assessment_id: septin-escrt_ii_complex-coverage
  area: completeness
  topic: Full maintained record and bounded external evidence
  outcome: supported
  summary: All fields, named evidence, examples, functions, graphs and discussions
    read. No maintained images. Captions are text only; no raw coordinates, unseen
    pixels or supplemental experiments certified. No automatic optional inventory
    or universal formation requirement.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-literature-policy
- assessment_id: septin-escrt_ii_complex-verdict
  area: consistency
  topic: Current independent disposition
  outcome: concern
  summary: Needs curation for one inherited grouped minor exact-family finding; correct
    identities and biological boundaries remain supported.
  target_ids:
  - GO:0000814
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-go
  - septin-teo2004-primary-pdf
  - septin-primary-PMC2475506
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-doi-nature02914
  - septin-pmid-12194858
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  - septin-ipr-IPR016689
  - septin-ipr-IPR008570
  - septin-ipr-IPR037855
- assessment_id: septin-escrt_iii_complex-identity
  area: identity
  topic: Exact structure and hierarchy
  outcome: supported
  summary: GO0000815 denotes ESCRT-III, with explicitly yeast endosomal four-class
    component/graph scope; general definition legitimately includes broader membrane-remodeling
    settings.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-GO0000815-ancestors
- assessment_id: septin-escrt_iii_complex-families
  area: grounding
  topic: Exact full-component classes versus domains and paralog groups
  outcome: supported
  summary: IPR005024 spans several CHMP paralogs and archaeal CdvB; it cannot uniquely
    replace each of the four named class groundings. Native current xrefs establish
    broader membership, not absence of any finer family elsewhere.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-ipr-IPR005024
  - septin-curation-policy
- assessment_id: septin-escrt_iii_complex-protein-identity
  area: grounding
  topic: Accession, primary name, aliases and status
  outcome: supported
  summary: All 4 native reviewed S288C examples and current exact-gene queries match.
    VPS2 is synonym of primary DID4; SNF7 also has VPS32 alias. Identity joins do
    not themselves establish membership.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-gene-VPS20-559292
  - septin-gene-SNF7-559292
  - septin-gene-VPS24-559292
  - septin-gene-VPS2-559292
  - septin-protein-policy
- assessment_id: septin-escrt_iii_complex-sources
  area: evidence
  topic: Experimental source tier and actual read scope
  outcome: supported
  summary: Babst complete primary abstract directly supports the four constituents/subcomplexes.
    Im2009 GUV activation and Lata engineered human polymer disassembly provide separately
    scoped body evidence; Henne is secondary context only.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-literature-policy
- assessment_id: septin-escrt_iii_complex-stoichiometry
  area: grounding
  topic: Counts and assembly interpretation
  outcome: supported
  summary: Four core protein classes do not imply one copy each in a universal fixed
    tetramer. Polymers and functional subcomplexes retain source scope.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
- assessment_id: septin-escrt_iii_complex-formation
  area: grounding
  topic: Formation versus activity and targeting
  outcome: unknown
  summary: UNKNOWN formation values remain justified within this source scope. Sorting,
    domain-truncation polymerization and reconstituted activation are not equated
    with universal individual formation necessity.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-schema-policy
- assessment_id: septin-escrt_iii_complex-graph
  area: graph
  topic: Complete coarse function graph
  outcome: supported
  summary: NONMECHANISTIC graph asserts four constituents, endosomal remodeling and
    MVB participation; no fixed polymer geometry or complete force-generation cycle.
    Vps4 is a separate recycling factor.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-graph-policy
- assessment_id: septin-escrt_iii_complex-taxa
  area: scope
  topic: Biological, reference and expression-host scope
  outcome: supported
  summary: Yeast core and S288C native proteins are supported; broader GO biology
    and human CHMP truncations are comparative context, not native yeast tube measurements.
    COMMON is qualitative source-supported species scope, not a measured population
    census.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-tax4932
  - septin-tax559292
- assessment_id: septin-escrt_iii_complex-applicability
  area: evidence
  topic: Current host-sensitive structured-source assessment
  outcome: supported
  summary: Named proteins and positive sorting/recycling pathway claims trigger policy
    assessment. Complete fresh official catalogue has no yeast or human host; downstream
    module queries are not applicable. Bacterial recombinant expression hosts are
    not biological-host substitutes. Historical unavailable runner is distinct from
    current catalogue fallback; no expression-to-assembly inference.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-escrt_iii_complex-schema
  area: schema
  topic: Original validation, provenance and native coverage
  outcome: supported
  summary: Three original validate/render pairs pass with exact Markdown and39 frozen
    historical occurrences. Current target is unchanged. Actual focused native protein
    checks exit0 with populated inventory; native coverage is not biological proof.
    Root global/future gates are separate.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-original-native-checks
  - septin-native-escrt_iii_complex-verify
  - septin-native-escrt_iii_complex-causal
- assessment_id: septin-escrt_iii_complex-history
  area: provenance
  topic: Append-only history and exact finding lineage
  outcome: supported
  summary: Historical rationale and all dated entries remain immutable. Separately
    authorized curation may update current notes/status or append clarification; inherited
    finding references preserve exact repository/review/finding identity.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-curation-policy
- assessment_id: septin-escrt_iii_complex-coverage
  area: completeness
  topic: Full maintained record and bounded external evidence
  outcome: supported
  summary: All fields, named evidence, examples, functions, graphs and discussions
    read. No maintained images. Captions are text only; no raw coordinates, unseen
    pixels or supplemental experiments certified. No automatic optional inventory
    or universal formation requirement.
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-literature-policy
- assessment_id: septin-escrt_iii_complex-verdict
  area: consistency
  topic: Current independent disposition
  outcome: supported
  summary: 'Pass with limitations: positive identity, membership and function assessments,
    bounded family candidate search and unresolved individual formation necessity.
    No scientific finding manufactured.'
  target_ids:
  - GO:0000815
  evidence_ids:
  - septin-record-escrt_iii_complex
  - septin-original-escrt_iii_complex
  - septin-go
  - septin-pmid-12194857
  - septin-primary-PMC2749878
  - septin-primary-PMC2758909
  - septin-pmid-24139821
  - septin-pmid-25303532
  - septin-henne2011-abstract
  - septin-protein-Q04272
  - septin-protein-P39929
  - septin-protein-P36095
  - septin-protein-P36108
  - septin-ipr-IPR005024
- assessment_id: septin-escrt_iv_complex-identity
  area: identity
  topic: Exact structure and hierarchy
  outcome: supported
  summary: GO1990621 denotes ATP-driven ESCRT-IV recycling; yeast Vps4/Vta1 scope
    and exact/narrow/related synonyms agree with the native authority.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-GO1990621-ancestors
- assessment_id: septin-escrt_iv_complex-families
  area: grounding
  topic: Exact full-component classes versus domains and paralog groups
  outcome: concern
  summary: IPR044538 is a complete Vta1-like family joined to Q06263. Vps4 IPR045253
    is a MIT domain and IPR050304 is a broader AAA ATPase family with unchecked LLM
    prose; neither justifies an exact Vps4 mapping.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-ipr-IPR044538
  - septin-ipr-IPR045253
  - septin-ipr-IPR050304
  - septin-curation-policy
- assessment_id: septin-escrt_iv_complex-protein-identity
  area: grounding
  topic: Accession, primary name, aliases and status
  outcome: supported
  summary: All 2 native reviewed S288C examples and current exact-gene queries match.
    VPS4 and VTA1 primary names match. Identity joins do not themselves establish
    membership.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-gene-VPS4-559292
  - septin-gene-VTA1-559292
  - septin-protein-policy
- assessment_id: septin-escrt_iv_complex-sources
  area: evidence
  topic: Experimental source tier and actual read scope
  outcome: supported
  summary: Yang genuine body directly tests fragment binding and cargo sorting; planar
    higher arrays are speculative modeling. Lata directly disassembles engineered
    human polymers; Huh/Shiflett are abstract/native annotation joins only.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-literature-policy
- assessment_id: septin-escrt_iv_complex-stoichiometry
  area: grounding
  topic: Counts and assembly interpretation
  outcome: supported
  summary: Two constituent classes do not establish a universal fixed Vps4 oligomer
    count. Fragment crystal stoichiometry and speculative planar arrays are not full-complex
    anatomy.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
- assessment_id: septin-escrt_iv_complex-formation
  area: grounding
  topic: Formation versus activity and targeting
  outcome: unknown
  summary: UNKNOWN formation values remain justified within this source scope. Fragment-binding
    mutations and Cps1 mislocalization do not prove each complete protein is universally
    required for every Vps4 oligomeric state.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-schema-policy
- assessment_id: septin-escrt_iv_complex-graph
  area: graph
  topic: Complete coarse function graph
  outcome: supported
  summary: Membership, proposed Vta1 stabilization, ATP-driven disassembly and recycling
    are appropriately coarse. Proposed arrays are not asserted as a solved lattice;
    external regulators are scoped out rather than claimed absent.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-graph-policy
- assessment_id: septin-escrt_iv_complex-taxa
  area: scope
  topic: Biological, reference and expression-host scope
  outcome: supported
  summary: Yeast Vta1/Vps4 fragments expressed in BL21/Rosetta2 differ from yeast
    deletion cargo assays. Native reference strain is S288C; exact assay-strain identity
    is not inferred. COMMON is qualitative source-supported species scope, not a measured
    population census.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-tax4932
  - septin-tax559292
- assessment_id: septin-escrt_iv_complex-applicability
  area: evidence
  topic: Current host-sensitive structured-source assessment
  outcome: supported
  summary: Named proteins and positive sorting/recycling pathway claims trigger policy
    assessment. Complete fresh official catalogue has no yeast or human host; downstream
    module queries are not applicable. Bacterial recombinant expression hosts are
    not biological-host substitutes. Historical unavailable runner is distinct from
    current catalogue fallback; no expression-to-assembly inference.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-escrt_iv_complex-schema
  area: schema
  topic: Original validation, provenance and native coverage
  outcome: supported
  summary: Three original validate/render pairs pass with exact Markdown and39 frozen
    historical occurrences. Current target is unchanged. Actual focused native protein
    checks exit0 with populated inventory; native coverage is not biological proof.
    Root global/future gates are separate.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-original-native-checks
  - septin-native-escrt_iv_complex-verify
  - septin-native-escrt_iv_complex-causal
- assessment_id: septin-escrt_iv_complex-history
  area: provenance
  topic: Append-only history and exact finding lineage
  outcome: supported
  summary: Historical rationale and all dated entries remain immutable. Separately
    authorized curation may update current notes/status or append clarification; inherited
    finding references preserve exact repository/review/finding identity.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-curation-policy
- assessment_id: septin-escrt_iv_complex-coverage
  area: completeness
  topic: Full maintained record and bounded external evidence
  outcome: supported
  summary: All fields, named evidence, examples, functions, graphs and discussions
    read. No maintained images. Captions are text only; no raw coordinates, unseen
    pixels or supplemental experiments certified. No automatic optional inventory
    or universal formation requirement.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-literature-policy
- assessment_id: septin-escrt_iv_complex-verdict
  area: consistency
  topic: Current independent disposition
  outcome: concern
  summary: Needs curation for one inherited minor Vta1 family mapping; unresolved
    Vps4 exact class and speculative array scope remain explicit.
  target_ids:
  - GO:1990621
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-go
  - septin-yang2010-legacy
  - septin-primary-PMC2758909
  - septin-pmid-20696398
  - septin-pmid-14701806
  - septin-pmid-14562095
  - septin-henne2011-abstract
  - septin-protein-P52917
  - septin-protein-Q06263
  - septin-ipr-IPR044538
  - septin-ipr-IPR045253
  - septin-ipr-IPR050304
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  - GO:0031205
  - GO:0008622
  - GO:0032865
  - GO:0033565
  - GO:0036452
  - GO:0000813
  - GO:0000814
  - GO:0000815
  - GO:1990621
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
  issue_key: emrky-tolc-unsupported-formation-essentiality
  category: evidence
  severity: major
  status: rejected
  certainty: confirmed
  title: Qualify the three unsupported formation-essentiality assertions
  description: Each constituent is marked ESSENTIAL, while CPX4273 is curator-inferred
    and the EmrK/EmrY subunit annotations are by similarity. The cited May2009 experiment
    changes multiple loci and TetA(C) regulation and measures expression/biofilms;
    it is not a constituent-specific structural absence assay. The record supplies
    no source-scoped inference explaining these categorical formation requirements.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  field_paths:
  - components[0].essentiality
  - components[1].essentiality
  - components[2].essentiality
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-schema
  - micro-complex-CPX-4273
  - micro-eco-0005547
  - micro-PMC2772303-legacy
  - micro-emrky-independent-challenge
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Formation essentiality requires appropriately scoped support
  native_severity: major
  normalization_reason: The unsupported values make categorical causal claims for
    every component; this materially exceeds the supplied evidence rather than merely
    omitting optional enrichment.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit
    finding_id: F1
  disposition_reason: Independent current review and peer challenge reject the original
    mandatory UNKNOWN-or-component-specific-formation-proof requirement as formulated.
    The record explicitly defines this inferred tripartite assembly and retains its
    source tier. Missing isolated necessity assays do not alone establish a major
    defect or invalidate defining constituent interpretation. This is not certification
    of experimentally measured necessity, evidence of dispensability, or resolution
    of the separate new CPX source-attribution defect. No action is retained for the
    rejected finding.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2976
- finding_id: micro-F2
  issue_key: epsilon-pol2-dpb2-dpb4-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Pol2, Dpb2 and Dpb4 family mappings
  description: Pol2, Dpb2 and Dpb4 remain REVIEWED_LABEL_ONLY under the open exact-grounding
    task although fresh native IPR029703, IPR016266 and IPR051377 identify their full-protein
    homologous classes, supported by the maintained reference xrefs and complete IPR051377
    reviewed-member list. The Dpb4-family description is LLM-flagged and is not used
    as primary biological evidence; membership and native metadata independently support
    the mapping. This does not settle the broader Dpb3 task.
  target_ids:
  - GO:0008622
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-family-IPR029703
  - micro-family-IPR016266
  - micro-family-IPR051377
  - micro-IPR051377-reviewed-retry
  - micro-protein-P21951
  - micro-protein-P24482
  - micro-protein-Q04603
  - micro-family-IPR050568
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/epsilon_dna_polymerase_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein class grounding
  native_severity: minor
  normalization_reason: This is a bounded available class mapping; supported complex
    identity and composition remain intact.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063720Z-epsilon-dna-polymerase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2977
- finding_id: micro-F3
  issue_key: epsilon-dpb4-bounded-complex-stability
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record the directly observed Dpb4 stability contribution
  description: The current Dpb4 role and graph only state membership. The already
    cited Ohya2000 source directly reports easier Dpb2/Dpb3 dissociation from Pol2
    in dpb4-deletion extracts after MonoQ chromatography. This concrete structure-level
    dependence can be recorded without replacing UNKNOWN with an unsupported universal
    ESSENTIAL.
  target_ids:
  - GO:0008622
  field_paths:
  - components[3].role
  - causal_graphs[0]
  evidence_ids:
  - micro-record-2
  - micro-schema
  - micro-PMC110797-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/epsilon_dna_polymerase_complex.yaml
    role: maintained scientific record
  rule_id: Resolvable source-backed structure-level dependency
  native_severity: minor
  normalization_reason: This is a bounded missing assembly-stability claim in an otherwise
    correct complex; no whole-complex identity error or universal necessity is inferred.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063720Z-epsilon-dna-polymerase-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2978
- finding_id: micro-F4
  issue_key: ermes-known-core-inventory-deferral
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record the established ERMES core before exact family resolution
  description: The current ermes_subunit_boundaries prompt explicitly requires exact
    family CURIEs before adding any Mmm1/Mdm10/Mdm12/Mdm34 rows. Freshly inspected
    Kornmann main body and Kawano Introduction directly identify this core. Native
    source-backed reviewed-label-only representation permits its known composition
    while exact family boundaries remain open. The inherited rationale is historical
    provenance and is not itself a current error.
  target_ids:
  - GO:0032865
  field_paths:
  - components
  - discussions[0].prompt
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-schema
  - micro-PMC2933203-legacy
  - micro-PMC5839780-legacy
  - micro-go-0032865
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ermes_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and component representation
  native_severity: minor
  normalization_reason: The correct whole-complex identity and science are retained.
    This is a bounded known-inventory deferral under an explicit prerequisite, not
    a major identity error or an automatic empty-optional-slot finding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063721Z-ermes-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2979
- finding_id: micro-F5
  issue_key: emrky-cpx-essential-subunit-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct CPX essential-subunit attribution in the new EmrKY edges
  description: The three newly added constituent edges explicitly say CPX-4273 curates
    each participant as an essential stoichiometric subunit. The complete native response
    supplies curator-inferred participant composition with unspecified biological
    roles, null EmrK/EmrY counts and TolC count3, but no essentiality annotation.
    The formal contributes-to relations and defined tripartite membership remain supported;
    the defect is the specific source attribution, not a demonstration that components
    are dispensable or that older essentiality enums must change.
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  field_paths:
  - causal_graphs[0].edges[5].evidence[0].notes
  - causal_graphs[0].edges[6].evidence[0].notes
  - causal_graphs[0].edges[7].evidence[0].notes
  evidence_ids:
  - micro-record-0
  - micro-delta-0
  - micro-complex-CPX-4273
  - micro-eco-0005547
  - micro-emrky-independent-challenge
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Source-scoped evidence attribution
  native_severity: minor
  normalization_reason: A narrow provenance overstatement in three notes; supported
    participant identity, inferred composition and formal membership edges remain
    intact. No universal biological dispensability or assembly failure is inferred.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2980
- finding_id: plaque-t4-F1
  issue_key: escrt-0-copied-vps1-definition-conflict
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile the copied Vps1 definition with the curated Vps27 complex
  description: The definition says Vps1p and Hse1p, faithfully reproducing the current
    GO text, while the exact synonym, Bilodeau abstract, native subunit identities
    and the record's resolved discussion identify Vps27p/Hse1p. The resolved discussion
    protects the component table but leaves the misleading definition visible.
  target_ids:
  - GO:0033565
  field_paths:
  - definition
  - definition_source
  - discussions[1]
  evidence_ids:
  - plaque-record-4
  - plaque-original-4-yaml
  - plaque-curation
  - plaque-go
  - plaque-pmid-12055639
  - plaque-up-P40343
  - plaque-up-P38753
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and component representation
  native_severity: minor
  normalization_reason: This is a localized wording/source conflict in an otherwise
    correctly identified and explicitly discussed complex. The component table, examples
    and graph already use Vps27, so it does not make the whole record denote a different
    complex.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063722Z-escrt-0-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2973
- finding_id: plaque-t4-F2
  issue_key: escrt-0-vps27-hrs-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the verified Vps27/Hrs family grounding
  description: The current Vps27 row is REVIEWED_LABEL_ONLY with an open exact-family
    task. Native IPR017073 explicitly covers Hrs/Vps27 and native P40343 corroborates
    membership. In contrast, the independently inspected Hse1 candidate is broader
    and is not part of this correction.
  target_ids:
  - GO:0033565
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - discussions#resolve_escrt_0_family_groundings.notes
  evidence_ids:
  - plaque-record-4
  - plaque-original-4-yaml
  - plaque-curation
  - plaque-ipr-IPR017073
  - plaque-up-P40343
  - plaque-members-IPR050670
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and component representation
  native_severity: minor
  normalization_reason: The named subunit and protein example are correct. This is
    a bounded actionable class-grounding gap under the existing explicit task, not
    missing optional inventory or a mandate to force every candidate.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063722Z-escrt-0-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2974
- finding_id: plaque-t6-F1
  issue_key: escrt-i-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the three verified yeast ESCRT-I families
  description: The current label-only notes defer exact source-neutral family review.
    Native type/signature/member evidence now resolves the Vps23/TSG101 and Vps28
    classes and the explicitly fungal Vps37 class without relying on a UEV/Modr domain.
  target_ids:
  - GO:0000813
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - discussions#resolve_escrt_i_family_groundings.notes
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-curation
  - plaque-ipr-IPR052070
  - plaque-family-query-IPR052070
  - plaque-ipr-IPR007143
  - plaque-ipr-IPR017435
  - plaque-ipr-IPR009851
  - plaque-up-P25604
  - plaque-up-Q02767
  - plaque-up-Q99176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_i_complex.yaml
    role: maintained scientific record
  rule_id: Exact full-component grounding
  native_severity: minor
  normalization_reason: The correct structure and protein identities remain intact.
    The available exact family mappings resolve a bounded existing label-only deferral
    without changing complex membership or mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063723Z-escrt-i-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2975
- finding_id: septin-escrt_ii_complex-F1
  issue_key: escrt-ii-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the three ESCRT-II constituent classes
  description: All three named yeast subunits remain label-only although exact full
    families IPR016689, IPR008570 and IPR037855 are verified with independent protein
    membership joins. Current native family type/signature/hierarchy and independent
    protein cross-references reconfirm this bounded open mapping. Preserve historical
    rationale; correct current notes/status or append a dated clarification during
    separately authorized curation.
  target_ids:
  - GO:0000814
  field_paths:
  - components[*].grounding_status
  - discussions#resolve_escrt_ii_family_groundings
  evidence_ids:
  - septin-record-escrt_ii_complex
  - septin-original-escrt_ii_complex
  - septin-curation-policy
  - septin-ipr-IPR016689
  - septin-ipr-IPR008570
  - septin-ipr-IPR037855
  - septin-protein-Q12483
  - septin-protein-P47142
  - septin-protein-Q06696
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_ii_complex.yaml
    role: maintained scientific record
  rule_id: Exact full-component grounding
  native_severity: minor
  normalization_reason: The correct structure and protein identities remain intact.
    The available exact family mappings resolve a bounded existing label-only deferral
    without changing complex membership or mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063724Z-escrt-ii-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2971
- finding_id: septin-escrt_iv_complex-F1
  issue_key: escrt-iv-vta1-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the Vta1 cofactor to its verified family
  description: The Vta1 row remains reviewed label-only despite exact full-family
    IPR044538 and an independent Q06263 membership join. The Vps4 candidate limitations
    do not justify deferring this separately resolved constituent. Current native
    family type/signature/hierarchy and independent protein cross-references reconfirm
    this bounded open mapping. Preserve historical rationale; correct current notes/status
    or append a dated clarification during separately authorized curation.
  target_ids:
  - GO:1990621
  field_paths:
  - components#vta1_vps4_cofactor.grounding_status
  - discussions#resolve_escrt_iv_family_groundings
  evidence_ids:
  - septin-record-escrt_iv_complex
  - septin-original-escrt_iv_complex
  - septin-curation-policy
  - septin-ipr-IPR044538
  - septin-ipr-IPR045253
  - septin-ipr-IPR050304
  - septin-protein-P52917
  - septin-protein-Q06263
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_iv_complex.yaml
    role: maintained scientific record
  rule_id: Exact full-component grounding
  native_severity: minor
  normalization_reason: The correct structure and protein identities remain intact.
    The available exact family mappings resolve a bounded existing label-only deferral
    without changing complex membership or mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T063726Z-escrt-iv-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2972
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0008622
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/epsilon_dna_polymerase_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground Pol2 with IPR029703,
    Dpb2 with IPR016266 and Dpb4 with IPR051377, keeping the reference accession/taxon
    pairs separate and narrowing the open task to classes not yet securely resolved.
  acceptance_checks:
  - Verify exact family identity/type and separate representative membership.
  - Do not substitute a shared histone fold or broad transcription-factor family for
    an unresolved subunit.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Retain homologous family scope and shared-complex membership; do not use LLM-generated
    family prose as a primary experiment or conflate Dpb3/POLE4 with Dpb4/POLE3.
  - Preserve dated discussions.rationale, posed_date and curation history; narrow
    only current prompt/notes as supported.
  - No record edits occur in this review PR.
- action_id: micro-A2
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0008622
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/epsilon_dna_polymerase_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add a source-scoped Dpb4
    contribution to stability/retention of Dpb2 and Dpb3 with Pol2, explicitly tied
    to the mutant-extract chromatography experiment. Preserve UNKNOWN where whole-complex
    formation necessity remains unestablished.
  acceptance_checks:
  - Cite Results sec15 and Figure1 for the physical readout.
  - Distinguish observed association/stability from cell viability, replication timing
    and intrinsic polymerase activity.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Global UNKNOWN may remain; no universal ESSENTIAL, complete intracellular absence
    or new experiment is required.
  - Preserve dated discussions.rationale, posed_date and curation history; narrow
    only current prompt/notes as supported.
  - No record edits occur in this review PR.
- action_id: micro-A3
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0032865
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ermes_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add source-backed named core
    rows with honest unresolved family grounding and formation necessity where appropriate;
    revise the TODO to concern exact mappings rather than block known membership.
    Do not infer peripheral-factor inventory, copy counts or universal ESSENTIAL labels
    from this review.
  acceptance_checks:
  - All four core identities and their roles cite the appropriate primary passages.
  - Species examples, if added later, remain distinct from class-level grounding.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; narrow
    only current prompt/notes as supported.
  - No record edits occur in this review PR.
- action_id: micro-A4
  finding_ids:
  - micro-F5
  target_ids:
  - cellstructuremech:emrky_tolc_multidrug_efflux_transport_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/emrky_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, qualify the three CPX evidence
    notes as curator-inferred participant composition, retaining unspecified EmrK/EmrY
    copy numbers and TolC3. If a separate defining-assembly necessity inference is
    explained, label it as an inference rather than an explicit CPX essentiality annotation.
  acceptance_checks:
  - Correct only the unsupported CPX attribution at edges5–7 evidence[0].notes; preserve
    supported contributes-to relations and the defined tripartite boundary.
  - Do not automatically retype older component ESSENTIAL values, infer dispensability
    or demand a new depletion/assembly experiment.
  - Preserve ECO0005547/source-tier limits, unknown EmrK/EmrY counts and historical
    rationale/events.
  - Run applicable native schema, strict, identifier and graph checks after separately
    authorized curation; no record edits occur here.
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0033565
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  description: Correct the local definition to Vps27p with an appropriate primary-source
    attribution or explicit qualifier documenting the native GO discrepancy. Preserve
    GO0033565 identity, correct component rows and historical evidence rather than
    silently rewriting the external source.
  acceptance_checks:
  - The visible definition no longer presents Vps1 as the curated ESCRT-0 constituent.
  - The source relationship and known GO discrepancy remain explicit.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated discussion rationale and history verbatim; append current evidence/notes
    or update an active decision only within the separately authorized record curation.
- action_id: plaque-t4-A2
  finding_ids:
  - plaque-t4-F2
  target_ids:
  - GO:0033565
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  description: Add InterPro:IPR017073 to the existing Vps27 class with exact source
    evidence and update its grounding state/task. Keep P40343 as the taxon-paired
    example and retain Hse1 label-only unless a genuinely exact class is separately
    verified.
  acceptance_checks:
  - The new grounding denotes the Hrs/Vps27 whole-protein family, not its domains.
  - The mixed Hse1 candidate is not adopted as an exact substitute.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated discussion rationale and history verbatim; append current evidence/notes
    or update an active decision only within the separately authorized record curation.
- action_id: plaque-t6-A1
  finding_ids:
  - plaque-t6-F1
  target_ids:
  - GO:0000813
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_i_complex.yaml
    role: maintained scientific record
  description: Use IPR052070 for Vps23, IPR007143 for Vps28 and IPR017435 for the
    explicitly yeast/fungal Vps37 constituent; align current grounding notes/TODO
    while preserving Mvb12 follow-up.
  acceptance_checks:
  - Keep Vps37 fungal scope explicit rather than claiming one family covers all metazoan
    paralogs.
  - Retain correct gene aliases and the separate Mvb12 inventory discussion.
  - Preserve supported identities and biological scope; pass applicable native gates.
  - Preserve dated discussion rationale and history verbatim; append current evidence/notes
    or update an active decision only within the separately authorized record curation.
- action_id: septin-escrt_ii_complex-A1
  finding_ids:
  - septin-escrt_ii_complex-F1
  target_ids:
  - GO:0000814
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_ii_complex.yaml
    role: maintained scientific record
  description: Use IPR016689 for Vps22/Snf8, IPR008570 for Vps25 and IPR037855 for
    Vps36, aligning current notes/TODO. Preserve dated rationale/history and exact
    inherited finding lineage; update current notes or append clarification. This
    review PR edits no record.
  acceptance_checks:
  - Do not substitute a shared winged-helix or GLUE/NZF domain.
  - Preserve two Vps25 copies where source-scoped stoichiometry is later curated;
    keep reference-strain/experimental-system distinctions.
  - Preserve supported identities and biological scope; pass applicable native gates.
  - Do not rewrite historical rationale, force unresolved paralog/domain mappings,
    or infer universal formation necessity from membership.
- action_id: septin-escrt_iv_complex-A1
  finding_ids:
  - septin-escrt_iv_complex-F1
  target_ids:
  - GO:1990621
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_iv_complex.yaml
    role: maintained scientific record
  description: Use IPR044538 for Vta1 and narrow the current family TODO to genuinely
    unresolved Vps4 boundaries. Preserve dated rationale/history and exact inherited
    finding lineage; update current notes or append clarification. This review PR
    edits no record.
  acceptance_checks:
  - Preserve the Vps4 label-only row until an exact full-class mapping is established.
  - Do not promote the speculative lattice model or inferred oligomeric count to fixed
    whole-complex anatomy.
  - Preserve supported identities and biological scope; pass applicable native gates.
  - Do not rewrite historical rationale, force unresolved paralog/domain mappings,
    or infer universal formation necessity from membership.
limitations:
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Own scientific
  scope is four complete current EmrKY-TolC, ER Sec, Pol-epsilon and ERMES records.
  EmrKY is the sole stale own target. All29 used local inputs were frozen before use
  and match the source; no extra maintained neighbor was read. Originals are immutable.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: EmrKY: actual
  complete native CPX4273 and ECO authority, reviewed protein annotations and May
  primary Methods2/7 plus Results14/15 were read. Curator inference, by-similarity
  annotations, null EmrK/EmrY counts, TolC3 and multi-locus/TetA(C) experimental confounds
  are retained. No isolated constituent necessity assay, direct full pump architecture
  or universal dispensability is certified.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: ER Sec: Panzner
  remains complete indexed primary abstract only after publisher redirect/block; Plath
  genuine Methods/Results and Wu declared main/method/caption scopes were read. BY4741
  source, limited Sec62 density/model coverage, initial binding versus Kar2-coupled
  translocation and parent/subcomplex representation remain distinct. No direct individual-protein
  inventory or optional example is forced.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Pol-epsilon:
  Chilkova remains complete indexed abstract after correct publisher PDF route403;
  Asturias is indexed/publisher abstract tier, not body. Ohya actual mutant-purification
  and Ganai declared biochemical sections were read. Reference S288C, W303/CG379/CB001
  and Py116 preparations are not conflated. Localization annotations and Huh abstract
  do not certify unread supplement rows. Secondary PMID15814431/9745046 reviews are
  not primary experiments.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Pol-epsilon
  exact family mappings use native metadata, reference xrefs and the complete15-member
  IPR051377 reviewed list. LLM-flagged family description is excluded as primary biological
  support. Broad histone-fold/transcription-related families do not resolve exact
  Dpb3. Shared-complex membership does not invalidate a homologous family.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: ERMES: Kornmann
  main text/captions and Kawano declared Introduction/Results/Discussion/strain/lipid-assay
  sections were read. No SupplementaryMethods, images, movies or coordinates were
  inspected. K.lactis recombinant Mmm1-Mdm12, yeast mutant heavy-membrane fractions
  and full in-vivo ERMES transfer remain separate. No peripheral-factor inventory,
  exact copy count or universal ESSENTIAL is imposed.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Official catalogue
  has20 organisms/28 organism-dataset pairs and no Saccharomyces match. E.coli precise1k
  is a five-strain dataset: BW25113,DGF-298,GMOS,MG1655,W3110. All201 memberships
  were checked for three native loci. EmrK/EmrY hit EvgA38 with15 members; TolC hits
  SoxS22 with117 members; complete selected module IDs/weights/native accession joins
  verified. No AI summaries or activity vectors used; expression context and nonhits
  do not prove assembly, causal regulation or absence.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Historical
  runner failure remains the actual Nov3 00:49Z PermissionError receipt, not a new
  invocation. Current failed/redirect/rate-limit routes are access diagnostics only;
  successful body/authority retries are separate. An initial guessed Chilkova PII
  was unverified and is not cited as evidence for that paper; the DOI-derived correct
  PII route also failed. Sandbox DNS attempts were retained separately and are not
  scientific sources.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Eight actual
  current native protein commands pass with7 reviewed examples/7 COVERED typed protein
  nodes; Sec and ERMES inventories are empty. Eight original native validate/render
  commands and56 historical input occurrences pass. No future successor/post-save/CI/queue
  certification is made; root owns global gates.'
- 'EmrKY-TolC, ER Sec, epsilon polymerase and ERMES independent review: Current finding
  disposition is three inherited minor/open findings plus one new minor CPX-attribution
  finding, and one inherited major explicitly rejected with exact lineage/no action.
  Rejection does not claim record edits or measured necessity. All four open actions
  are bounded future curation, preserve append-only history and avoid mandatory new
  experiments. No related/group/category issue is terminally resolved by inference.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Bilodeau2002, Stahelin2002,
  Huh2003, Katzmann2001 and Hong1998 are read at complete primary abstract/metadata
  tier only. The current Bilodeau Nature page exposes abstract/subscription preview;
  no full body or individual localization images are certified.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Henne2011 remains secondary
  complete-abstract context. A publisher route returned403; the author publication
  page does not supply an independently inspected body of this exact paper. No detailed
  Henne main-body passage or figure reading is claimed.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Katzmann2003 selected Results3–7,
  Discussion9–10, Methods12–15 and text captions were read from genuine primary HTML.
  Chu2006 and Curtiss2007 are restricted to the explicitly enumerated membership/strain/association
  sections. No source figure pixels, supplemental experiments or raw measurements
  were independently reanalysed.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: S288C reference protein
  identities differ from SEY6210 experimental derivatives. COMMON is a qualitative
  native taxonomic assertion, not an independently measured population census. Recombinant
  E.coli is not a natural-host proxy.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Exact Hrs/Vps27, Vps23/TSG101,
  Vps28 and fungal Vps37 mappings are supported by native family types, signatures
  and protein joins. Generated unchecked family prose and contradictory old composition
  descriptions are excluded. Hse1 mixed-family scope remains unresolved; no exact
  class is forced.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: The InterPro IPR052070
  member endpoint returned429, but a separate current bounded UniProt reviewed-member
  query returned7 matching identities. Negative access is not negative biology; no
  evolutionary exhaustiveness or unreviewed-member survey is claimed.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: The current catalogue fallback
  is distinct from the historical runner-unavailable observation at2026-11-03 00:49Z.
  No fresh runner execution is claimed. Complete catalogue noncoverage precludes a
  justified same-host downstream dataset; it does not establish absence of the biology.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: Four corrected historical
  access rows preserve original URLs, timestamps, hashes and context_only disclosures
  from the immutable originals. Historical transport bytes were not independently
  reconstructed; current successful/failed routes are separate dated observations.'
- 'ESCRT-0, ESCRT umbrella and ESCRT-I independent review: No maintained images are
  present in these three records. No optional missing-example or universal formation
  requirement is invented. Parent-owned corpus gates, CI, queue admission, merge and
  cleanup are outside this source-slice certification.'
- 'ESCRT-II, III and IV independent review: Three unchanged ESCRT II/III/IV targets
  reviewed in full. Two inherited minor exact-family findings remain open; III has
  a positive qualified pass. Three formal original no-expression applicability exclusions
  require successor correction. No own original evidence-kind defect found after all
  evidence rows were inspected.'
- 'ESCRT-II, III and IV independent review: Fresh Teo2004 PDF, Im2008/2009, Lata2008
  and Yang2010 genuine bodies were read only at declared locators. No figure pixels,
  atomic coordinates or supplementary experiments were independently analyzed. Native
  metadata and abstract evidence do not imply full-body access. Henne2011 secondary
  review is complete-abstract-only after a current publisher403; no detailed review-body
  claim is independently certified. Hierro publisher is abstract/subscription preview;
  Babst2002 publisher403, Yang canonical browser challenge and EuropePMC500 are access
  context only, independently distinguished from a successful Yang alternate PMC body.'
- 'ESCRT-II, III and IV independent review: Yeast species4932 and S288C559292 reference
  proteins differ from Teo ATCC9763D genomic source, bacterial recombinant expression
  and Im BY4741/BY4742 assays. Human recombinant interfaces and engineered CHMP polymers
  are not native yeast assembly geometry. COMMON is qualitative scope, not an organism-frequency
  census.'
- 'ESCRT-II, III and IV independent review: Im2009 experimentally separates ESCRT-II-driven
  activation from membrane localization of individual Vps20. Yang Vta1/Vps4 fragment
  interface and cargo tests do not turn speculative planar arrays into solved whole
  assemblies. Lata ATP-driven disassembly is direct, while final membrane fission
  mechanism is proposed. No fixed Vps4 oligomer count or universal formation flags
  imposed.'
- 'ESCRT-II, III and IV independent review: Exact Vps22/Vps25/Vps36 and Vta1 family
  joins are resolved independently. The bounded III/Vps4 candidate review uses current
  example xrefs and inspected family/domain hierarchy; it does not prove no finer
  mapping exists elsewhere. IPR050304 unchecked LLM prose is excluded as scientific
  support. Existing optional stoichiometry discussion is not fabricated into a required-field
  defect.'
- 'ESCRT-II, III and IV independent review: Complete current official catalogue has
  no matching yeast/human host. No unrelated bacterial expression-host dataset is
  queried as a biological proxy. Historical runner unavailable is actual Nov3 00:49Z;
  no fresh invocation claimed. Current public catalogue receipt is independent evidence
  with actual Nov4 timestamp.'
- 'ESCRT-II, III and IV independent review: Actual six root native commands passed:
  II3 reviewed examples/3COVERED nodes, III4/4, IV2/2. These are identity/coverage
  checks, not independent experimental membership or necessity evidence. Original
  native validation/render0 and39 historical hashes verified. Root corpus gates, final
  successor validation, CI and queue are separate and are not pre-certified here.'
- 'ESCRT-II, III and IV independent review: Only26 explicitly listed maintained inputs
  informed this source report. No repository, original bundle, record, Git or GitHub
  mutation. Exact search scopes are limited to the actual issuing-authority requests;
  no exhaustive literature-absence claim.'
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
- One changed EmrKY target is substantively refreshed; all nine other current target
  hashes match their original frozen inputs. All used maintained context is frozen
  before synthesis.
- Four review-bundle issues track ten applicability corrections, four failed-access
  evidence-kind corrections, the stale-input refresh and supported rejection of the
  original EmrKY blanket formation-essentiality finding. Scientific curation remains
  separately filed.
- Preserve inferred EmrK/EmrY/TolC membership, absent EmrK/EmrY source counts and
  TolC3. The new minor concerns explicit CPX attribution in added edge evidence notes,
  not an automatic instruction to change all essentiality enums.
- Twenty current native protein commands passed across21 protein examples and22 typed
  protein nodes:21 COVERED and one external Vps27 recruiter UNANCHORED_WITH_UNIPROT.
  The recruiter is not a missing ESCRT-I constituent; identity and coverage checks
  are not experimental membership or necessity evidence.
- Historical source access and adapter-runner unavailability retain their actual dates.
  Successful current body retrievals, primary abstracts, secondary abstracts, database
  annotations and failed-access diagnostics retain distinct scopes.
- Dated rationale/history remain append-only. Exact family findings do not force broad
  domains or unresolved paralog boundaries; the existing Mvb12 and stoichiometry discussions
  are not automatic optional-inventory defects.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063718Z-emrky-tolc-multidrug-efflux-transport-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063719Z-endoplasmic-reticulum-sec-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063720Z-epsilon-dna-polymerase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063721Z-ermes-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063722Z-escrt-0-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063722Z-escrt-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063723Z-escrt-i-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063724Z-escrt-ii-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063725Z-escrt-iii-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T063726Z-escrt-iv-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2391
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2968
- https://github.com/CultureBotAI/CellStructureMech/issues/2969
- https://github.com/CultureBotAI/CellStructureMech/issues/2970
- https://github.com/CultureBotAI/CellStructureMech/issues/2971
- https://github.com/CultureBotAI/CellStructureMech/issues/2972
- https://github.com/CultureBotAI/CellStructureMech/issues/2973
- https://github.com/CultureBotAI/CellStructureMech/issues/2974
- https://github.com/CultureBotAI/CellStructureMech/issues/2975
- https://github.com/CultureBotAI/CellStructureMech/issues/2976
- https://github.com/CultureBotAI/CellStructureMech/issues/2977
- https://github.com/CultureBotAI/CellStructureMech/issues/2978
- https://github.com/CultureBotAI/CellStructureMech/issues/2979
- https://github.com/CultureBotAI/CellStructureMech/issues/2980
```
