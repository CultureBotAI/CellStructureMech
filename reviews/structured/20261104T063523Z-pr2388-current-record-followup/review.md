# PR 2388: current-input review of ten records and adversarial follow-up

- Review: 20261104T063523Z-pr2388-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T06:14:47.131005Z
- Finished UTC: 2026-11-04T06:35:23Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Independent current-input review of ten DNA replication and initiation complexes preserves all twenty original artifacts and refreshes the two stale RPA and preinitiation records. Thirteen inherited scientific findings remain open (one major and twelve minor) across eight records; the Pol III holoenzyme and topoisomerase IV retain qualified positive verdicts. The successor corrects seven formal and three prose structured-source applicability assessments and twelve access-only evidence-kind occurrences. The 28 current protein examples and 28 typed protein nodes all pass actual native coverage checks. Records remain unchanged; separately linked record-curation issues retain exact predecessor lineage and bounded source scopes.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 8dff0f68c5ca75d5b6d78d6d577b9d09426eb7a3.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0043846 | data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml | maintained | DNA polymerase III, clamp loader complex |
| GO:0009360 | data/structures/other/dna_polymerase_iii_complex.yaml | maintained | DNA polymerase III complex |
| GO:0044776 | data/structures/other/dna_polymerase_iii_core_complex.yaml | maintained | DNA polymerase III, core complex |
| GO:0005662 | data/structures/other/dna_replication_factor_a_complex.yaml | maintained | DNA replication factor A complex |
| GO:0005663 | data/structures/other/dna_replication_factor_c_complex.yaml | maintained | DNA replication factor C complex |
| GO:0031261 | data/structures/other/dna_replication_preinitiation_complex.yaml | maintained | DNA replication preinitiation complex |
| GO:0009340 | data/structures/other/dna_topoisomerase_iv_complex.yaml | maintained | DNA topoisomerase IV complex |
| GO:1990102 | data/structures/other/dnaa_diaa_complex.yaml | maintained | DnaA-DiaA complex |
| GO:1990157 | data/structures/other/dnaa_dnab_dnac_complex.yaml | maintained | DnaA-DnaB-DnaC complex |
| GO:1990084 | data/structures/other/dnaa_dps_complex.yaml | maintained | DnaA-Dps complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0043846 | passed | True | GO:0043846 | Documented focused command passed. |
| validate-strict GO:0043846 | passed | True | GO:0043846 | Documented focused command passed. |
| validate GO:0009360 | passed | True | GO:0009360 | Documented focused command passed. |
| validate-strict GO:0009360 | passed | True | GO:0009360 | Documented focused command passed. |
| validate GO:0044776 | passed | True | GO:0044776 | Documented focused command passed. |
| validate-strict GO:0044776 | passed | True | GO:0044776 | Documented focused command passed. |
| validate GO:0005662 | passed | True | GO:0005662 | Documented focused command passed. |
| validate-strict GO:0005662 | passed | True | GO:0005662 | Documented focused command passed. |
| validate GO:0005663 | passed | True | GO:0005663 | Documented focused command passed. |
| validate-strict GO:0005663 | passed | True | GO:0005663 | Documented focused command passed. |
| validate GO:0031261 | passed | True | GO:0031261 | Documented focused command passed. |
| validate-strict GO:0031261 | passed | True | GO:0031261 | Documented focused command passed. |
| validate GO:0009340 | passed | True | GO:0009340 | Documented focused command passed. |
| validate-strict GO:0009340 | passed | True | GO:0009340 | Documented focused command passed. |
| validate GO:1990102 | passed | True | GO:1990102 | Documented focused command passed. |
| validate-strict GO:1990102 | passed | True | GO:1990102 | Documented focused command passed. |
| validate GO:1990157 | passed | True | GO:1990157 | Documented focused command passed. |
| validate-strict GO:1990157 | passed | True | GO:1990157 | Documented focused command passed. |
| validate GO:1990084 | passed | True | GO:1990084 | Documented focused command passed. |
| validate-strict GO:1990084 | passed | True | GO:1990084 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | All ten positive molecular or replication narratives trigger structured-source applicability. Fresh official catalogue and metadata support bounded E.coli precise1k context for seven bacterial records; exact-locus/module checks retain five-strain scope, threshold hits and nonhit limits without inferring direct regulation, assembly or necessity. HolD ppGpp145, HolE PAL26Del147 and Dps OxyR3/RpoS51 contexts are recorded at their inspected scope. The catalogue has no matched natural yeast host for RPA, RFC or preinitiation; bacterial expression hosts are not proxies. The actual historical adapter-runner failure is preserved separately from fresh official-source fallback. |
| Independent claim-level source review | passed | True | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native DNA polymerase III, clamp loader complex UniProt verify check | passed | True | GO:0043846 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, clamp loader complex UniProt causal check | passed | True | GO:0043846 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III complex UniProt verify check | passed | True | GO:0009360 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III complex UniProt causal check | passed | True | GO:0009360 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, core complex UniProt verify check | passed | True | GO:0044776 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA polymerase III, core complex UniProt causal check | passed | True | GO:0044776 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA replication factor A complex UniProt verify check | passed | True | GO:0005662 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA replication factor A complex UniProt causal check | passed | True | GO:0005662 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA replication factor C complex UniProt verify check | passed | True | GO:0005663 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA replication factor C complex UniProt causal check | passed | True | GO:0005663 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA replication preinitiation complex UniProt verify check | passed | True | GO:0031261 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA replication preinitiation complex UniProt causal check | passed | True | GO:0031261 | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA topoisomerase IV complex UniProt verify check | passed | True | GO:0009340 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DNA topoisomerase IV complex UniProt causal check | passed | True | GO:0009340 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-DiaA complex UniProt verify check | passed | True | GO:1990102 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-DiaA complex UniProt causal check | passed | True | GO:1990102 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-DnaB-DnaC complex UniProt verify check | passed | True | GO:1990157 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-DnaB-DnaC complex UniProt causal check | passed | True | GO:1990157 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-Dps complex UniProt verify check | passed | True | GO:1990084 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-Dps complex UniProt causal check | passed | True | GO:1990084 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Full heptamer versus crystallized pentamer

identity: concern. Targets: GO:0043846.

Exact GO identity/protein-complex parent and holoenzyme parthood are sound. GO is faithfully quoted, but unconditional tau AND gamma wording compresses its cited source distinction: DnaX3 can contain either or both products for clamp loading. Retain heptamer scope and separate tau-dependent fork organization from minimal pentamer activity.

### Three exact families and excluded domain/broad alternatives

grounding: concern. Targets: GO:0043846.

HolA IPR005790,HolC IPR007459 andHolD IPR004615 are exact whole-protein families with independent matching example xrefs, yet remain REVIEWED_LABEL_ONLY. DnaX IPR012763/IPR045085 andHolB IPR004622/IPR048731 are domains; IPR050238 is broader and generated prose cannot establish exact identity. Do not import HolA proofreading or historical HolD unknown-function prose.

### Five current reviewed K12 identities

grounding: supported. Targets: GO:0043846.

DnaX P06710/HolA P28630/HolB P28631/HolC P28905/HolD P28632 match exact primary genes, ordered loci and tax83333. Eight full current gene queries overall are singletons; no reconstruction of historical query results. DnaX tau/gamma are frameshift products, not two unrelated genes.

### Canonical species and actual structural preparation

scope: supported. Targets: GO:0043846.

Canonical species562 is appropriate for the E.coli gamma-complex study. Jeruzalmi used purified delta/delta-prime and truncated gamma1–373 reconstitution; structure is nucleotide-free pentamer, not full heptamer or an unmodified native K12 preparation. Fig1 caption and Methods read without pixel/coordinate analysis.

### Nine coarse membership/function edges

graph: supported. Targets: GO:0043846.

Five component membership edges, delta-beta contact, beta loading, DNA substrate and replication outcome remain source-scoped NONMECHANISTIC FUNCTION. Static crystal and authors speculative transition model are not a measured ATP cycle; chi/psi membership comes from the heptamer review and Maki primary abstract, not the pentamer crystal. Scope notes appropriately withhold detailed geometry/switching.

### Formation versus function/viability

grounding: unknown. Targets: GO:0043846.

Active minimal pentamer and alternative DnaX products do not establish loss-of-formation requirements for the named full heptamer in all conditions. Global UNKNOWN component formation remains permissible. Native tau viability and gamma viability clauses do not impose universal loader-assembly classifications.

### Modular holoenzyme and class hierarchy

identity: supported. Targets: GO:0009360.

GO0009360 exact identity/synonym and DNA-polymerase-complex parent match its tripartite core/beta/loader model. The record does not copy the neighboring beta cross-class oligomerization sentence or impose a fixed modern two-versus-three-core stoichiometry.

### Three correctly grounded subcomplexes

grounding: supported. Targets: GO:0009360.

Core GO0044776,beta GO0044775 andloader GO0043846 are structure-level components. No artificial single-protein inventory is required. The clamp-component note explicitly attributes compressed tau/gamma wording to GO; this is retained as an accurately scoped authority quotation, not independently asserted universal DnaX stoichiometry.

### E.coli reconstitution at complete abstract tier

scope: supported. Targets: GO:0009360.

Maki/Kornberg complete primary abstract directly reports reconstitution of ten polypeptide types and processive replication from core/auxiliary subunits, supporting species562 canonical wording. Publisher HTML/PDF403 and API metadata only leave exact methods/strain/figures unread; reference K12 DnaX is not proof of that preparation strain.

### Six descriptive processive-synthesis edges

graph: supported. Targets: GO:0009360.

Core contributes polymerase activity,beta tethers catalytic subunit,loader loads beta,template-directed activity extends DNA and whole supports replication. Maki primary abstract separates core polymerase/proofreading from auxiliary processivity. NONMECHANISTIC scope excludes detailed ATP transitions, exchange and fork coordination, so no static-structure mechanism inflation is established.

### Functionally necessary modules versus formation

grounding: unknown. Targets: GO:0009360.

Functional contribution and successful purified reconstitution do not determine every component physical-formation necessity across contexts. UNKNOWN is not a defect; no fixed subunit-copy model or obligatory individual-protein examples proposed.

### Alpha/epsilon/theta catalytic subassembly

identity: supported. Targets: GO:0044776.

GO0044776 and complete Maki abstract support alpha/epsilon/theta core identity and holoenzyme parthood. DNA-polymerase-complex parent is semantically supported by catalytic activity rather than claimed as a current direct GO is-a edge. Polymerase and proofreading remain distinct activities.

### Exact theta family and other class boundaries

grounding: concern. Targets: GO:0044776.

HolE IPR009052/PF06440 is an exact full-protein family with P0ABS8 xref, so continued REVIEWED_LABEL_ONLY is a bounded grounding gap. DnaQ IPR006309 is proteobacterial, IPR006054 is a domain, and IPR004805 includes DnaE2/DnaE/PolC. PHP and OB-fold candidates are domains. No forced broad/domain mapping follows.

### Three current reviewed reference examples

grounding: supported. Targets: GO:0044776.

P10443/dnaE,b0184;P03007/dnaQ,b0215;P0ABS8/holE,b1842 are reviewed K12 references with current singleton queries. E.coli dnaE synonym polC does not conflate distinct Gram-positive PolC. Membership is separately supported by Maki abstract and native GO; theta is not individually credited with either catalytic activity.

### Species versus unread reconstitution strain

scope: supported. Targets: GO:0044776.

Species562 canonical note matches primary abstract. K12 accession labels identify examples only. Maki exact assay methods, experimental strain and figures remain unverified because only complete abstract and publisher metadata were reached.

### Membership and separated polymerase/proofreading

graph: supported. Targets: GO:0044776.

Three constituent membership edges and separate core enables-polymerase/enables-proofreading edges match primary abstract and exact activity scope. No assertion that theta alone polymerizes/proofreads, that proofreading is GO0003887, or that graph ordering is a measured assembly sequence.

### Defined components versus universal physical necessity

grounding: unknown. Targets: GO:0044776.

Core composition and activity reconstitution do not establish a complete conditional loss-of-assembly series. UNKNOWN remains appropriate, while uncertainty over theta function is not evidence of its absence. No new experiment or universal ESSENTIAL classification required.

### Current upstream nuclear ancestry/taxon discrepancy

scope: unknown. Targets: GO:0043846.

Current native GO routes the term through nuclear protein-containing complex and marks Eukaryota-only, conflicting with its named bacterial identity and cited E.coli evidence. These assertions are absent from the maintained record; retain exact named identity and bacterial scope, without importing upstream restriction or creating a local false-misquotation finding.

### Current upstream nuclear ancestry/taxon discrepancy

scope: unknown. Targets: GO:0044776.

Current native GO routes the term through nuclear protein-containing complex and marks Eukaryota-only, conflicting with its named bacterial identity and cited E.coli evidence. These assertions are absent from the maintained record; retain exact named identity and bacterial scope, without importing upstream restriction or creating a local false-misquotation finding.

### Original source versus current target

provenance: supported. Targets: GO:0043846.

Original frozen record is unchanged on current main. Original source revision/hashes and immutable YAML/Markdown were verified; current source reassessment does not erase historical limitations or invent refreshed stale fields.

### Positive molecular claims require matched structured-source context

scope: concern. Targets: GO:0043846.

Original formal expression-only exclusion is unsupported: positive replication, clamp-loading or core catalytic claims trigger applicability. Fresh complete catalogue selects E.coli precise1k; nine exact reference loci each checked against201 module rows. Only HolD→ppGpp145 andHolE→PAL26Del147 cross thresholds, confirmed by actual module gene lists. Five-strain context does not certify source assay strains; nonhits are not absence and hits are not assembly/formation/direct regulation.

### Actual native coverage and semantic limits

schema: supported. Targets: GO:0043846.

Five reviewed examples and5 COVERED typed nodes. Both current root native commands actually exit0. This does not settle exact family mapping or biological completeness. Original native validation/render also pass.

### Historical discussions and past corrections

provenance: supported. Targets: GO:0043846.

Dated histories and discussions.rationale are retained as provenance; optional current-state clarification alone is not a defect. Any later family-mapping action must append evidence, preserve posed_date/rationale and narrow only current prompt/notes. No neighboring or grouped issue is terminally resolved here.

### All assigned maintained fields

completeness: supported. Targets: GO:0043846.

Entire current record/original pair reviewed. No maintained image or measurement demands pixel/unit assessment. Optional blank slots are not findings; primary body, abstract, secondary review and authority tiers remain separate.

### Current independent scientific verdict

other: concern. Targets: GO:0043846.

needs_curation: two inherited minor composition/family findings remain; supported full-heptamer identity and graph retained.

### Original source versus current target

provenance: supported. Targets: GO:0009360.

Original frozen record is unchanged on current main. Original source revision/hashes and immutable YAML/Markdown were verified; current source reassessment does not erase historical limitations or invent refreshed stale fields.

### Positive molecular claims require matched structured-source context

scope: concern. Targets: GO:0009360.

Original formal expression-only exclusion is unsupported: positive replication, clamp-loading or core catalytic claims trigger applicability. Fresh complete catalogue selects E.coli precise1k; nine exact reference loci each checked against201 module rows. Only HolD→ppGpp145 andHolE→PAL26Del147 cross thresholds, confirmed by actual module gene lists. Five-strain context does not certify source assay strains; nonhits are not absence and hits are not assembly/formation/direct regulation.

### Actual native coverage and semantic limits

schema: supported. Targets: GO:0009360.

Zero examples/typed protein nodes is deliberate complex-level scope; three STRUCTURE groundings checked independently. Both current root native commands actually exit0. This does not settle exact family mapping or biological completeness. Original native validation/render also pass.

### Historical discussions and past corrections

provenance: supported. Targets: GO:0009360.

Dated histories and discussions.rationale are retained as provenance; optional current-state clarification alone is not a defect. Any later family-mapping action must append evidence, preserve posed_date/rationale and narrow only current prompt/notes. No neighboring or grouped issue is terminally resolved here.

### All assigned maintained fields

completeness: supported. Targets: GO:0009360.

Entire current record/original pair reviewed. No maintained image or measurement demands pixel/unit assessment. Optional blank slots are not findings; primary body, abstract, secondary review and authority tiers remain separate.

### Current independent scientific verdict

other: supported. Targets: GO:0009360.

pass_with_limitations: supported modular identity/components/function; Maki abstract-only methods limit and formation unknown retained. No scientific finding invented.

### Original source versus current target

provenance: supported. Targets: GO:0044776.

Original frozen record is unchanged on current main. Original source revision/hashes and immutable YAML/Markdown were verified; current source reassessment does not erase historical limitations or invent refreshed stale fields.

### Positive molecular claims require matched structured-source context

scope: concern. Targets: GO:0044776.

Original formal expression-only exclusion is unsupported: positive replication, clamp-loading or core catalytic claims trigger applicability. Fresh complete catalogue selects E.coli precise1k; nine exact reference loci each checked against201 module rows. Only HolD→ppGpp145 andHolE→PAL26Del147 cross thresholds, confirmed by actual module gene lists. Five-strain context does not certify source assay strains; nonhits are not absence and hits are not assembly/formation/direct regulation.

### Actual native coverage and semantic limits

schema: supported. Targets: GO:0044776.

Three reviewed examples and3 COVERED typed nodes. Both current root native commands actually exit0. This does not settle exact family mapping or biological completeness. Original native validation/render also pass.

### Historical discussions and past corrections

provenance: supported. Targets: GO:0044776.

Dated histories and discussions.rationale are retained as provenance; optional current-state clarification alone is not a defect. Any later family-mapping action must append evidence, preserve posed_date/rationale and narrow only current prompt/notes. No neighboring or grouped issue is terminally resolved here.

### All assigned maintained fields

completeness: supported. Targets: GO:0044776.

Entire current record/original pair reviewed. No maintained image or measurement demands pixel/unit assessment. Optional blank slots are not findings; primary body, abstract, secondary review and authority tiers remain separate.

### Current independent scientific verdict

other: concern. Targets: GO:0044776.

needs_curation: inherited minor exact theta-family mapping remains; correct examples and distinct activities retained.

### Historical failed-access evidence kind

provenance: concern. Targets: GO:0009360.

Original HTTP403/body-access limit and context_only scope were honest, but evidence kind database is inappropriate for a failed-access diagnostic. Successor retains exact historical time/hash under validation/context_only without implying a new body read or refutation.

### Historical failed-access evidence kind

provenance: concern. Targets: GO:0009360.

Original HTTP403/body-access limit and context_only scope were honest, but evidence kind database is inappropriate for a failed-access diagnostic. Successor retains exact historical time/hash under validation/context_only without implying a new body read or refutation.

### Historical failed-access evidence kind

provenance: concern. Targets: GO:0044776.

Original HTTP403/body-access limit and context_only scope were honest, but evidence kind database is inappropriate for a failed-access diagnostic. Successor retains exact historical time/hash under validation/context_only without implying a new body read or refutation.

### Historical failed-access evidence kind

provenance: concern. Targets: GO:0044776.

Original HTTP403/body-access limit and context_only scope were honest, but evidence kind database is inappropriate for a failed-access diagnostic. Successor retains exact historical time/hash under validation/context_only without implying a new body read or refutation.

### native identities

grounding: supported. Targets: GO:0005662.

Current primary symbols/loci/reviewed accessions and S288C559292 match exactly; each bounded gene query returned one reviewed hit. Protein examples remain organism-specific instances rather than class groundings. Current native covered counts are 3/3, not the old frozen inventory.

### structured source

evidence: concern. Targets: GO:0005662.

Complete positive protein/replication/binding or loading narrative triggers native structured-source applicability. Original notes[1] provides unsupported no-established-dataset prose, with no formal check; it is not a pure unexplained omission or formal exclusion. Fresh complete catalogue independently lacks the natural yeast host. No expression-to-assembly inference, bacterial expression-host proxy or fabricated downstream run.

### taxonomy

scope: supported. Targets: GO:0005662.

Species-level budding yeast biology and S288C reference identities are distinct. No numeric prevalence census or arbitrary universal formation requirement is imposed. Experiments in BJ926/W303 derivatives, recombinant bacteria or archaeal RFC do not establish identical reference-strain provenance.

### complete fields

completeness: supported. Targets: GO:0005662.

Complete current/original fields reviewed; no maintained images or quantitative organelle measurements asserted. Optional fields/examples are not mandatory enrichment. Current proposed status and dated historical rationale are preserved.

### native provenance

schema: supported. Targets: GO:0005662.

Original native validate/render and42 historical input occurrences pass; all47 current inputs frozen. Six current protein commands actually passed. Source membership/necessity findings are not disproven by schema success.

### native identities

grounding: supported. Targets: GO:0005663.

Current primary symbols/loci/reviewed accessions and S288C559292 match exactly; each bounded gene query returned one reviewed hit. Protein examples remain organism-specific instances rather than class groundings. Current native covered counts are 5/5, not the old frozen inventory.

### structured source

evidence: concern. Targets: GO:0005663.

Complete positive protein/replication/binding or loading narrative triggers native structured-source applicability. Original notes[1] provides unsupported no-established-dataset prose, with no formal check; it is not a pure unexplained omission or formal exclusion. Fresh complete catalogue independently lacks the natural yeast host. No expression-to-assembly inference, bacterial expression-host proxy or fabricated downstream run.

### taxonomy

scope: supported. Targets: GO:0005663.

Species-level budding yeast biology and S288C reference identities are distinct. No numeric prevalence census or arbitrary universal formation requirement is imposed. Experiments in BJ926/W303 derivatives, recombinant bacteria or archaeal RFC do not establish identical reference-strain provenance.

### complete fields

completeness: supported. Targets: GO:0005663.

Complete current/original fields reviewed; no maintained images or quantitative organelle measurements asserted. Optional fields/examples are not mandatory enrichment. Current proposed status and dated historical rationale are preserved.

### native provenance

schema: supported. Targets: GO:0005663.

Original native validate/render and42 historical input occurrences pass; all47 current inputs frozen. Six current protein commands actually passed. Source membership/necessity findings are not disproven by schema success.

### native identities

grounding: supported. Targets: GO:0031261.

Current primary symbols/loci/reviewed accessions and S288C559292 match exactly; each bounded gene query returned one reviewed hit. Protein examples remain organism-specific instances rather than class groundings. Current native covered counts are 5/5, not the old frozen inventory.

### structured source

evidence: concern. Targets: GO:0031261.

Complete positive protein/replication/binding or loading narrative triggers native structured-source applicability. Original notes[1] provides unsupported no-established-dataset prose, with no formal check; it is not a pure unexplained omission or formal exclusion. Fresh complete catalogue independently lacks the natural yeast host. No expression-to-assembly inference, bacterial expression-host proxy or fabricated downstream run.

### taxonomy

scope: supported. Targets: GO:0031261.

Species-level budding yeast biology and S288C reference identities are distinct. No numeric prevalence census or arbitrary universal formation requirement is imposed. Experiments in BJ926/W303 derivatives, recombinant bacteria or archaeal RFC do not establish identical reference-strain provenance.

### complete fields

completeness: supported. Targets: GO:0031261.

Complete current/original fields reviewed; no maintained images or quantitative organelle measurements asserted. Optional fields/examples are not mandatory enrichment. Current proposed status and dated historical rationale are preserved.

### native provenance

schema: supported. Targets: GO:0031261.

Original native validate/render and42 historical input occurrences pass; all47 current inputs frozen. Six current protein commands actually passed. Source membership/necessity findings are not disproven by schema success.

### identity composition

identity: supported. Targets: GO:0005662.

Native GO/Wold review abstract supports heterotrimeric nonspecific ssDNA-binding RPA. Fresh Brill/Stillman primary abstract supports three yeast gene products; reviewed native entries corroborate heterotrimer identities. The approximate generic70/30/14classes need not equal precise yeast gel masses69/36/13.

### stale refresh

provenance: supported. Targets: GO:0005662.

Compared original frozen record with current additions: RFA1/2/3 examples, gene symbols, Wold component/edge evidence and yeast canonical context. Native identities and independent yeast primary abstract support the biological additions. Wold full body remains unavailable; no precise S288C experimental-strain confirmation is inferred. Prior2470 repair does not resolve unchanged exact-family F1.

### family

grounding: concern. Targets: GO:0005662.

Exact native whole-protein families IPR004591/014646/013970 agree with current RFA1/2/3 xrefs; existing REVIEWED_LABEL_ONLY/open family task remains actionable despite new examples. Narrow yeast subgroup IPR016588 is not substituted for generic14kDa family.

### graph necessity

graph: supported. Targets: GO:0005662.

NONMECHANISTIC three membership edges plus ssDNA-binding relation match supported composition/function. UNKNOWN formation values remain honest; Brill viability or cell-cycle transcription is not physical assembly necessity.

### identity function

identity: supported. Targets: GO:0005663.

RFC identity/fork parthood/five-polypeptide eukaryotic scope and PCNA loading are supported by GO plus directly read Cullmann yeast source. Referenced archaeal Kitabayashi/Nishida contexts are not passed off as yeast RFC1–5 experiments.

### family

grounding: concern. Targets: GO:0005663.

Exact RFC1 IPR012178 native family agrees with reviewed P38630; its label-only/open task remains unresolved. Broad IPR050238 and C-terminal IPR013748 do not establish exact individual RFC2–5 groundings; generated IPR050238 prose excluded.

### graph necessity

graph: supported. Targets: GO:0005663.

NONMECHANISTIC membership/loading/function graph stays within current source scope. Cullmann disruption/tetrad tests establish viability, so UNKNOWN assembly values are not automatically upgraded; no mandatory new assay.

### unchanged history

provenance: supported. Targets: GO:0005663.

Current RFC bytes equal original frozen target. Existing canonical example is species-level, not an invented S288C experimental strain. Historical rationale remains append-only; native current checks do not erase original access failures.

### identity mechanism

identity: concern. Targets: GO:0031261.

GO0031261 exactly denotes the protein-DNA preinitiation class. Its definition does not contain appended loaded-double-hexamer/kinase-target/CMG/bridge details. Takayama primary results support GINS identity and condition-scoped recruitment; detailed modern physical mechanism remains mismatched to supplied source.

### stale refresh

provenance: supported. Targets: GO:0031261.

Only CDC45 example/history changed: current Q08032 reviewed primaryCDC45/S288C559292 and nucleus ECO0000269 PMID8901577 join match native entry. Correct Hopwood primary abstract corroborates localization/complex context; no original scan pixels/body read asserted. This addition neither changes old mechanistic prose nor resolves exact-family or formation/graph findings.

### composition families

grounding: concern. Targets: GO:0031261.

Fresh GINS purification supports four distinct subunits; reviewed five examples and native exact families agree. Sld5IPR008591/Psf1IPR005339 retry responses succeeded after429; Psf2IPR007257/Psf3IPR010492/Cdc45IPR003874 verify whole-protein classes. Current missing grounding is distinct from optional examples and MCM is already GO-grounded.

### formation

scope: concern. Targets: GO:0031261.

Takayama tests conditional GINS recovery, origin occupancy and replication; Hopwood abstract reports Cdc45-Mcm5 association/initiation. These supplied citations do not establish both current pre-IC MCM/Cdc45 physical-formation ESSENTIAL assertions at their stated scope. Retain a localized evidence qualification; do not infer dispensability, require a universal all-species assay or downgrade defining constituents solely because they are constituents.

### graph scope

graph: concern. Targets: GO:0031261.

Eight edges encode six memberships, nucleoplasm placement and generic replication; MECHANISTIC assembly/function label overstates the encoded topology. GO0006260 identifies the process but does not alone support pre-IC-specific causation. Source-supported conditional recruitment could be separately encoded; no automatic structural-node type finding.

### access kind historical micro51 wold1997 publisher

provenance: concern. Targets: GO:0005662.

Historical access-only observation is database/context_only; successor should use validation/context_only. Original source scopes explicitly disclose blocked/redirect/download-shell access, so no allegation of false fulltext reading.

### access kind historical micro51 kim2003 publisher

provenance: concern. Targets: GO:0005663.

Historical access-only observation is database/context_only; successor should use validation/context_only. Original source scopes explicitly disclose blocked/redirect/download-shell access, so no allegation of false fulltext reading.

### access kind historical micro51 kitabayashi2003 publisher

provenance: concern. Targets: GO:0005663.

Historical access-only observation is database/context_only; successor should use validation/context_only. Original source scopes explicitly disclose blocked/redirect/download-shell access, so no allegation of false fulltext reading.

### access kind historical micro51 cullmann1995 pdf

provenance: concern. Targets: GO:0005663.

Historical access-only observation is database/context_only; successor should use validation/context_only. Original source scopes explicitly disclose blocked/redirect/download-shell access, so no allegation of false fulltext reading.

### access kind historical micro51 gary1995 pdf

provenance: concern. Targets: GO:0005663.

Historical access-only observation is database/context_only; successor should use validation/context_only. Original source scopes explicitly disclose blocked/redirect/download-shell access, so no allegation of false fulltext reading.

### Exact identity and assembly boundary

identity: supported. Targets: GO:0009340.

Exact ParC/ParE TopoIV identity and typeIIA function; correct generic bacterial scope without copying the upstream heterodimer error.

### Native parents and parthood

identity: supported. Targets: GO:0009340.

Typed parent and named subassembly claims match current GO. Is-a, has-part and interaction are not conflated, and unrelated adjacent components are not mandatory additions.

### Component class versus protein example

grounding: supported. Targets: GO:0009340.

Inspected ParC/ParE candidates are narrower taxonomic families or broader topoisomerase classes; existing label-only scope remains justified.

### Reviewed accessions and native coverage

grounding: supported. Targets: GO:0009340.

2 reviewed example occurrences and 2 COVERED protein nodes agree with native accession/gene/taxon data. Identity and family provenance do not themselves demonstrate complex membership.

### Formation evidence versus activity or viability

grounding: unknown. Targets: GO:0009340.

Truncation-sensitive association is measured, but no optional formation enum is asserted by this target; catalytic ATP use is not an assembly requirement.

### Coarse function and mechanistic boundaries

graph: supported. Targets: GO:0009340.

Explicit NONMECHANISTIC activity graph is supported; detailed cleavage/strand-passage/ATPase states are not asserted.

### Measured numbers and scope

grounding: not_applicable. Targets: GO:0009340.

No invariant complex copy-number field is asserted. Assay-specific ratios do not force optional stoichiometry or universal structure counts.

### Species and experimental strain boundaries

scope: supported. Targets: GO:0009340.

E.coli species562 and K12 reference83333 identities are correct. Reference accessions do not equate all mutants/recombinant preparations with precise1k strains. No distribution prevalence row is asserted.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:0009340.

Positive protein/pathway assertions trigger the policy. Original formal exclusion solely because no expression-module claim is unsupported. Current official catalogue covers E.coli; bounded precise1k gene/module checks provide context only. All assigned queried loci have false membership flags across201 modules; this does not refute their genes, expression or structure roles.

### Original native validity and frozen inputs

schema: supported. Targets: GO:0009340.

Original validate/render0 and exact Markdown; all13 frozen historical inputs match. Current target hash unchanged; actual native protein checks0. Historical batch26 corpus runs remain valid scoped provenance, not current-head/CI success.

### Historical questions and current corrective scope

provenance: supported. Targets: GO:0009340.

Dated discussion rationale and curation history remain intact. Any future curation updates current notes/status or appends a dated clarification; no historical rewriting, automatic status promotion or neighboring issue disposition.

### Complete current record and explicit access limits

completeness: supported. Targets: GO:0009340.

Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all graph edges and discussions/history assessed. No maintained images; no figure pixels,supplements,coordinates or independent data reanalysis claimed. Optional fields do not automatically create findings.

### Independent current scientific disposition

consistency: supported. Targets: GO:0009340.

Qualified positive pass; exact family boundary,reference identities and coarse function remain supported.

### Exact identity and assembly boundary

identity: supported. Targets: GO:1990102.

Exact DiaA-DnaA-oriC nucleoprotein identity and named subassemblies; later helicase-loading machinery remains a separate boundary.

### Native parents and parthood

identity: supported. Targets: GO:1990102.

Typed parent and named subassembly claims match current GO. Is-a, has-part and interaction are not conflated, and unrelated adjacent components are not mandatory additions.

### Component class versus protein example

grounding: concern. Targets: GO:1990102.

Current exact authority family/oriC terms match declared classes. Existing REVIEWED_LABEL_ONLY notes merely defer curation; this remains the inherited localized grounding finding, not a missing optional-example demand.

### Reviewed accessions and native coverage

grounding: supported. Targets: GO:1990102.

2 reviewed example occurrences and 2 COVERED protein nodes agree with native accession/gene/taxon data. Identity and family provenance do not themselves demonstrate complex membership.

### Formation evidence versus activity or viability

grounding: unknown. Targets: GO:1990102.

Tetramer/interface assays support particular binding/stimulation effects, not a universal requirement for every constituent under every condition.

### Coarse function and mechanistic boundaries

graph: supported. Targets: GO:1990102.

Assembly and initiation-promotion graph remains coarse; phosphosugar control and later helicase loading are not established edges.

### Measured numbers and scope

grounding: supported. Targets: GO:1990102.

Four copies are explicitly per DiaA tetramer, not a fixed total for the whole origin assembly.

### Species and experimental strain boundaries

scope: supported. Targets: GO:1990102.

E.coli species562 and K12 reference83333 identities are correct. Reference accessions do not equate all mutants/recombinant preparations with precise1k strains. COMMON is qualitative curation, not a numerical strain-prevalence census established by these experiments.

### DnaA experimental annotation provenance

provenance: supported. Targets: GO:1990102.

Native P03004 explicitly links the three localization citations. Regev uses membrane-association context; Schenk includes B.subtilis and E.coli; Garner is artificial-bilayer insertion. These support their annotation provenance at abstract/native tier, not whole-complex localization or identical reference-strain experiments.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:1990102.

Positive protein/pathway assertions trigger the policy. Original formal exclusion solely because no expression-module claim is unsupported. Current official catalogue covers E.coli; bounded precise1k gene/module checks provide context only. All assigned queried loci have false membership flags across201 modules; this does not refute their genes, expression or structure roles.

### Original native validity and frozen inputs

schema: supported. Targets: GO:1990102.

Original validate/render0 and exact Markdown; all13 frozen historical inputs match. Current target hash unchanged; actual native protein checks0. Historical batch26 corpus runs remain valid scoped provenance, not current-head/CI success.

### Historical questions and current corrective scope

provenance: supported. Targets: GO:1990102.

Dated discussion rationale and curation history remain intact. Any future curation updates current notes/status or appends a dated clarification; no historical rewriting, automatic status promotion or neighboring issue disposition.

### Complete current record and explicit access limits

completeness: supported. Targets: GO:1990102.

Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all graph edges and discussions/history assessed. No maintained images; no figure pixels,supplements,coordinates or independent data reanalysis claimed. Optional fields do not automatically create findings.

### Independent current scientific disposition

consistency: concern. Targets: GO:1990102.

Needs curation for 1 independently reconfirmed inherited minor finding(s); supported identity,function and source boundaries remain intact.

### Exact identity and assembly boundary

identity: supported. Targets: GO:1990157.

Exact primase-free prepriming intermediate with DnaA,originDNA and whole DnaB-DnaC loading subcomplex. Primase triggers a later transition.

### Native parents and parthood

identity: supported. Targets: GO:1990157.

Typed parent and named subassembly claims match current GO. Is-a, has-part and interaction are not conflated, and unrelated adjacent components are not mandatory additions.

### Component class versus protein example

grounding: concern. Targets: GO:1990157.

Current exact authority family/oriC terms match declared classes. Existing REVIEWED_LABEL_ONLY notes merely defer curation; this remains the inherited localized grounding finding, not a missing optional-example demand.

### Reviewed accessions and native coverage

grounding: supported. Targets: GO:1990157.

1 reviewed example occurrences and 1 COVERED protein nodes agree with native accession/gene/taxon data. Identity and family provenance do not themselves demonstrate complex membership.

### Formation evidence versus activity or viability

grounding: concern. Targets: GO:1990157.

S8 oriC-versus-vector comparison directly tests DnaB retention in an isolated prepriming preparation. Blanket UNKNOWN omits this condition-scoped formation evidence; no universal viability or every-subunit requirement follows.

### Coarse function and mechanistic boundaries

graph: supported. Targets: GO:1990157.

Loading/initiation graph excludes ring opening,DnaC-release chemistry and later primase recruitment; assembled mutant complexes can lack later replication activity.

### Measured numbers and scope

grounding: not_applicable. Targets: GO:1990157.

No invariant complex copy-number field is asserted. Assay-specific ratios do not force optional stoichiometry or universal structure counts.

### Species and experimental strain boundaries

scope: supported. Targets: GO:1990157.

E.coli species562 and K12 reference83333 identities are correct. Reference accessions do not equate all mutants/recombinant preparations with precise1k strains. COMMON is qualitative curation, not a numerical strain-prevalence census established by these experiments.

### DnaA experimental annotation provenance

provenance: supported. Targets: GO:1990157.

Native P03004 explicitly links the three localization citations. Regev uses membrane-association context; Schenk includes B.subtilis and E.coli; Garner is artificial-bilayer insertion. These support their annotation provenance at abstract/native tier, not whole-complex localization or identical reference-strain experiments.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:1990157.

Positive protein/pathway assertions trigger the policy. Original formal exclusion solely because no expression-module claim is unsupported. Current official catalogue covers E.coli; bounded precise1k gene/module checks provide context only. All assigned queried loci have false membership flags across201 modules; this does not refute their genes, expression or structure roles.

### Original native validity and frozen inputs

schema: supported. Targets: GO:1990157.

Original validate/render0 and exact Markdown; all13 frozen historical inputs match. Current target hash unchanged; actual native protein checks0. Historical batch26 corpus runs remain valid scoped provenance, not current-head/CI success.

### Historical questions and current corrective scope

provenance: supported. Targets: GO:1990157.

Dated discussion rationale and curation history remain intact. Any future curation updates current notes/status or appends a dated clarification; no historical rewriting, automatic status promotion or neighboring issue disposition.

### Complete current record and explicit access limits

completeness: supported. Targets: GO:1990157.

Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all graph edges and discussions/history assessed. No maintained images; no figure pixels,supplements,coordinates or independent data reanalysis claimed. Optional fields do not automatically create findings.

### Independent current scientific disposition

consistency: concern. Targets: GO:1990157.

Needs curation for 2 independently reconfirmed inherited minor finding(s); supported identity,function and source boundaries remain intact.

### Exact identity and assembly boundary

identity: supported. Targets: GO:1990084.

Direct DnaA-Dps protein association defines this complex; RIDA/Hda/beta-clamp neighbors remain distinct.

### Native parents and parthood

identity: supported. Targets: GO:1990084.

Typed parent and named subassembly claims match current GO. Is-a, has-part and interaction are not conflated, and unrelated adjacent components are not mandatory additions.

### Component class versus protein example

grounding: concern. Targets: GO:1990084.

Current exact authority family/oriC terms match declared classes. Existing REVIEWED_LABEL_ONLY notes merely defer curation; this remains the inherited localized grounding finding, not a missing optional-example demand.

### Reviewed accessions and native coverage

grounding: supported. Targets: GO:1990084.

2 reviewed example occurrences and 2 COVERED protein nodes agree with native accession/gene/taxon data. Identity and family provenance do not themselves demonstrate complex membership.

### Formation evidence versus activity or viability

grounding: unknown. Targets: GO:1990084.

Binding/inhibition evidence does not establish universal formation necessity or invariant DnaA:Dps stoichiometry.

### Coarse function and mechanistic boundaries

graph: supported. Targets: GO:1990084.

Negative initiation graph remains conditional; oxidative-stress checkpoint and adaptive mutation are not established detailed pathways.

### Measured numbers and scope

grounding: not_applicable. Targets: GO:1990084.

No invariant complex copy-number field is asserted. Assay-specific ratios do not force optional stoichiometry or universal structure counts.

### Species and experimental strain boundaries

scope: supported. Targets: GO:1990084.

E.coli species562 and K12 reference83333 identities are correct. Reference accessions do not equate all mutants/recombinant preparations with precise1k strains. COMMON is qualitative curation, not a numerical strain-prevalence census established by these experiments.

### DnaA experimental annotation provenance

provenance: supported. Targets: GO:1990084.

Native P03004 explicitly links the three localization citations. Regev uses membrane-association context; Schenk includes B.subtilis and E.coli; Garner is artificial-bilayer insertion. These support their annotation provenance at abstract/native tier, not whole-complex localization or identical reference-strain experiments.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:1990084.

Positive protein/pathway assertions trigger the policy. Original formal exclusion solely because no expression-module claim is unsupported. Current official catalogue covers E.coli; bounded precise1k gene/module checks provide context only. dps is above threshold in OxyR3/RpoS51; other named queried loci are below all201 thresholds, not biologically absent.

### Original native validity and frozen inputs

schema: supported. Targets: GO:1990084.

Original validate/render0 and exact Markdown; all13 frozen historical inputs match. Current target hash unchanged; actual native protein checks0. Historical batch26 corpus runs remain valid scoped provenance, not current-head/CI success.

### Historical questions and current corrective scope

provenance: supported. Targets: GO:1990084.

Dated discussion rationale and curation history remain intact. Any future curation updates current notes/status or appends a dated clarification; no historical rewriting, automatic status promotion or neighboring issue disposition.

### Complete current record and explicit access limits

completeness: supported. Targets: GO:1990084.

Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all graph edges and discussions/history assessed. No maintained images; no figure pixels,supplements,coordinates or independent data reanalysis claimed. Optional fields do not automatically create findings.

### Independent current scientific disposition

consistency: concern. Targets: GO:1990084.

Needs curation for 1 independently reconfirmed inherited minor finding(s); supported identity,function and source boundaries remain intact.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0043846, GO:0009360, GO:0044776, GO:0005662, GO:0005663, GO:0031261, GO:0009340, GO:1990102, GO:1990157, GO:1990084.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: State the three DnaX copies and their alternatives

minor / open / confirmed; issue key: pol-iii-clamp-loader-dnax-mixture.

The definition unconditionally says the heptamer includes tau and gamma. Its cited McHenry2003 body p1158 instead specifies DnaX3-delta-delta-prime-chi-psi with any mixture of tau and gamma for clamp loading, and native DnaX annotations agree. The original GO sentence matches the record but compresses the source distinction.

### micro-F2: Resolve the available HolA, HolC and HolD families

minor / open / confirmed; issue key: pol-iii-clamp-loader-exact-family.

HolA, HolC and HolD remain REVIEWED_LABEL_ONLY despite current exact whole-protein families IPR005790, IPR007459 and IPR004615 with matching maintained-example xrefs. Inspected DnaX/HolB alternatives are domains or broader shared families and do not justify a forced whole-protein mapping.

### micro-F3: Ground the theta subunit with its exact family

minor / open / confirmed; issue key: pol-iii-core-theta-exact-family.

HolE remains REVIEWED_LABEL_ONLY and the current TODO defers all three core classes, although native IPR009052 is an exact full-protein theta family and P0ABS8 independently carries that family xref. Other inspected candidates are broader or taxon-limited.

### plaque-t3-F1: Resolve verified exact subunit family grounding

minor / open / confirmed; issue key: dna-replication-factor-a-complex-exact-family-grounding.

The three existing RPA size-defined protein classes have exact source-neutral whole-protein families:70kDa IPR004591, approximately30/32kDa IPR014646 and14kDa IPR013970. Native family type/name/signatures plus independent reviewed RFA1/2/3 xrefs establish the matches. The narrower yeast Rfa3 subgroup is not substituted for the generic14kDa class. Historical statements about what was curated in an earlier pass are preserved as history, not declared fabricated.

### plaque-t4-F1: Resolve verified exact subunit family grounding

minor / open / confirmed; issue key: dna-replication-factor-c-complex-exact-family-grounding.

The named RFC1 large-subunit class exactly matches IPR012178, verified from native family metadata/signature and the maintained P38630 UniProt cross-reference. The current REVIEWED_LABEL_ONLY row and OPEN task leave this resolvable match unrepresented. No exact RFC2–5 mapping is established by broad IPR050238 or C-terminal IPR013748. Historical statements about what was curated in an earlier pass are preserved as history, not declared fabricated.

### plaque-t5-F1: Source or qualify the added modern preinitiation mechanism

major / open / confirmed; issue key: dna-preinitiation-modern-mechanism-source-overstatement.

The definition names GO0031261 but appends loaded MCM double-hexamer/kinase-target/CMG details outside that definition. MCM/Cdc45 roles and repeated graph prose attribute these details, including a Mcm2–Mcm5 bridge, to Takayama2003. The inspected source identifies GINS and conditional origin-recruitment dependencies; it does not demonstrate that detailed physical and phosphorylation mechanism. The supported partial observations should remain distinct from later mechanistic knowledge.

### plaque-t5-F2: Resolve exact GINS and Cdc45 protein-family classes

minor / open / confirmed; issue key: dna-preinitiation-exact-five-protein-families.

Exact whole-protein families are available for Sld5 IPR008591, Psf1 IPR005339, Psf2 IPR007257, Psf3 IPR010492 and Cdc45 IPR003874. Separate native family metadata and reviewed UniProt xrefs corroborate them. The four label-only GINS rows and ungrounded named Cdc45 class can be resolved; this does not require extra optional protein examples.

### plaque-t5-F3: Do not substitute initiation function for formation necessity

minor / open / confirmed; issue key: dna-preinitiation-formation-essentiality-source-gap.

MCM and Cdc45 carry ESSENTIAL physical-formation assertions, while supplied Takayama evidence demonstrates conditional GINS/recruitment/replication effects and the newly added Hopwood-linked Cdc45 example supports identity/localization. These do not establish both stated whole-pre-IC formation assertions. Clarify the evidence and condition scope or retain uncertainty; this is not a claim of biological dispensability, a requirement for universal all-species experiments, or a rejection of valid defining constituent status.

### plaque-t5-F4: Calibrate the descriptive graph and final process citation

minor / open / confirmed; issue key: dna-preinitiation-descriptive-graph-mechanistic-scope.

The eight edges represent six part-membership relations, nucleoplasm placement and a generic replication relation. MECHANISTIC and the assembly/function title overstate what is encoded. GO0006260 on the final edge identifies DNA replication but does not establish the pre-IC-specific causal assertion.

### septin-dnaa_diaa_complex-F1: Ground the two proteins and oriC with exact classes

minor / open / confirmed; issue key: dnaa-diaa-exact-groundings.

The existing DiaA/DnaA/oriC rows remain REVIEWED_LABEL_ONLY solely because exact terms were not curated. Native IPR023070, IPR001957 and SO0000953 respectively match these declared classes, with the protein-family membership independently corroborated by the correct reviewed examples. Independently reconfirmed against the current unchanged record and fresh scoped source evidence. Preserve dated discussion rationale; current notes/status may be corrected or a dated clarification appended.

### septin-dnaa_dnab_dnac_complex-F1: Ground DnaA and chromosomal origin DNA

minor / open / confirmed; issue key: dnaa-dnab-dnac-exact-groundings.

IPR001957 and SO0000953 exactly match the two label-only DnaA and chromosomal-origin rows, whose current notes defer curation rather than identify a genuine unmatched class. Independently reconfirmed against the current unchanged record and fresh scoped source evidence. Preserve dated discussion rationale; current notes/status may be corrected or a dated clarification appended.

### septin-dnaa_dnab_dnac_complex-F2: Record the tested origin-DNA formation requirement

minor / open / confirmed; issue key: dnaa-dnab-dnac-origin-formation.

The origin-DNA component remains blanket UNKNOWN even though the cited primary S8 directly tests the assembly endpoint: replacing oriC plasmid with empty vector prevents retained DnaB in the isolated prepriming-complex preparation. This is measured origin-dependent formation, not merely a replication-function defect. Independently reconfirmed against the current unchanged record and fresh scoped source evidence. Preserve dated discussion rationale; current notes/status may be corrected or a dated clarification appended.

### septin-dnaa_dps_complex-F1: Ground DnaA and Dps with their exact families

minor / open / confirmed; issue key: dnaa-dps-exact-families.

The existing DnaA/Dps components remain REVIEWED_LABEL_ONLY despite exact full-protein IPR001957 and IPR002177 family identities and independent reviewed-example membership. Independently reconfirmed against the current unchanged record and fresh scoped source evidence. Preserve dated discussion rationale; current notes/status may be corrected or a dated clarification appended.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, qualify the E.coli heptamer model as three DnaX products, tau and/or gamma, plus delta, delta-prime, chi and psi. Keep additional tau-dependent fork organization separate from minimum clamp loading.

- Do not universalize one tau:gamma ratio or require both products in every assembly.
- Do not replace the full heptamer identity with the crystallized pentamer.
- Preserve source scope and correct current protein examples; pass applicable native validators.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR; retain primary-body/abstract/secondary/authority distinctions and do not force universal formation necessity.

### micro-A2

In separately authorized record curation, map the three verified exact families and narrow the current unresolved TODO to genuinely unresolved classes. Preserve the five correct protein examples.

- Keep IPR004622/IPR012763 domain matches separate from whole-protein identity.
- Do not import a family description claiming delta proofreading activity.
- Preserve source scope and correct current protein examples; pass applicable native validators.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR; retain primary-body/abstract/secondary/authority distinctions and do not force universal formation necessity.

### micro-A3

In separately authorized record curation, use IPR009052 for the theta class and narrow the current TODO. Preserve correct DnaE/DnaQ examples and unresolved exact taxon-neutral class boundaries.

- Verify family type/name/PF06440 and separate example membership.
- Do not substitute the DnaQ domain or broad DnaE2/DnaE/PolC family.
- Preserve source scope and correct current protein examples; pass applicable native validators.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR; retain primary-body/abstract/secondary/authority distinctions and do not force universal formation necessity.

### plaque-t3-A1

Ground the verified classes to IPR004591/014646/013970 with source-backed family evidence and update the corresponding open task/status. Preserve unresolved classes and historical provenance; keep organism accessions as examples.

- Each added family denotes the existing whole-protein class rather than a domain, broader homolog group or species accession.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history; any record curation uses guarded writer and appended history in a separately authorized change, not this review-only PR.

### plaque-t4-A1

Ground the verified class RFC1 to IPR012178 with source-backed family evidence and update the corresponding open task/status. Preserve unresolved classes and historical provenance; keep organism accessions as examples.

- Each added family denotes the existing whole-protein class rather than a domain, broader homolog group or species accession.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history; any record curation uses guarded writer and appended history in a separately authorized change, not this review-only PR.

### plaque-t5-A1

Separate the native GO definition and directly demonstrated2003 observations from later mechanistic claims. Either inspect and attach appropriate modern primary sources at each claim or qualify/remove the unsupported detail; preserve conditional recruitment and strain context.

- Every double-hexamer, kinase-target, CMG and bridge assertion has a directly inspected source at the actual field.
- Takayama2003 is not presented as demonstrating mechanisms beyond its experiments.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history; any record curation uses guarded writer and appended history in a separately authorized change, not this review-only PR.

### plaque-t5-A2

Add the exact five class groundings with source-specific evidence and appropriate grounding states. Keep the MCM GO complex separate and retain existing correctly taxon-paired examples.

- Each family is checked against the same named whole-protein class and the native reviewed-protein cross-reference.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history; any record curation uses guarded writer and appended history in a separately authorized change, not this review-only PR.

### plaque-t5-A3

Clarify the physical-formation basis and experimental scope for current MCM/Cdc45 ESSENTIAL assertions, using source-backed defining assembly or condition-specific evidence where justified; otherwise retain UNKNOWN. Preserve established functional/recruitment roles and do not infer dispensability or mandate new universal assays.

- Formation necessity is assessed separately from viability, replication activity, protein abundance and conditional recruitment.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history; any record curation uses guarded writer and appended history in a separately authorized change, not this review-only PR.

### plaque-t5-A4

Mark the present topology/function graph NONMECHANISTIC with an honest scope note and claim-appropriate final-edge evidence, or build separately sourced causal recruitment edges preserving experimental conditions.

- The graph label matches the relations actually encoded.
- The final biological edge cites a source supporting the structure-specific assertion, not only a process identifier.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history; any record curation uses guarded writer and appended history in a separately authorized change, not this review-only PR.

### septin-dnaa_diaa_complex-A1

Use these verified exact class groundings and align current status/notes/TODO; retain correct proteins and per-DiaA-tetramer stoichiometry. In separately authorized record curation, preserve dated rationale/history and add a dated clarification where needed; this review PR edits no scientific record.

- Do not substitute the broader GmhA/SIS classes or a generic DNA chemical entity.
- Keep strain accessions separate from family and sequence-feature groundings.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Keep exact original finding lineage and experimental limits; do not rewrite historical rationale.

### septin-dnaa_dnab_dnac_complex-A1

Apply the exact DnaA family and oriC sequence-feature class and update current grounding notes/TODO. In separately authorized record curation, preserve dated rationale/history and add a dated clarification where needed; this review PR edits no scientific record.

- Keep the existing GO1990100 whole-subcomplex grounding.
- Preserve P03004 and the primase-free intermediate boundary.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Keep exact original finding lineage and experimental limits; do not rewrite historical rationale.

### septin-dnaa_dnab_dnac_complex-A2

Replace blanket UNKNOWN with a source-backed, explicitly condition-scoped formation requirement for oriC DNA in this E.coli reconstitution; choose the appropriate enum with the assay qualification in evidence/notes. In separately authorized record curation, preserve dated rationale/history and add a dated clarification where needed; this review PR edits no scientific record.

- Cite S8 empty-vector control and the S20 preparation.
- Do not infer organism viability, universal in-vivo necessity or all-subunit requirements.
- Retain the distinction between DnaC mutants that assemble and their defective later function.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Keep exact original finding lineage and experimental limits; do not rewrite historical rationale.

### septin-dnaa_dps_complex-A1

Use the exact DnaA and Dps families and align current grounding notes/TODO while preserving correct examples and the qualified oxidative-stress model. In separately authorized record curation, preserve dated rationale/history and add a dated clarification where needed; this review PR edits no scientific record.

- Do not substitute broad AAAATPase/ferritin folds or force a narrower gammaproteobacterial subgroup.
- Do not infer direct DnaA binding for every Dps-family member.
- Preserve supported identifiers, examples and biological scope; pass applicable native validation.
- Keep exact original finding lineage and experimental limits; do not rewrite historical rationale.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a; current SHA256 d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/dna_polymerase_iii_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d; current SHA256 c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T055920Z-dna-polymerase-iii-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/dna_polymerase_iii_core_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b; current SHA256 d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T055921Z-dna-polymerase-iii-core-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/dna_replication_factor_a_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a3cfb2654e3e82b6d841247eb4580f288e2bb1d082ff6d5a06ae5f363019f7a9; current SHA256 875ef33eba1336b1bfd61e3c5bc9f0ade5f2c37a93d25793797fa5b9ac34c133. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/dna_replication_factor_c_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f; current SHA256 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/dna_replication_preinitiation_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1948bbd3828f9736b6dcf1151e9621969b9e0214863e42b559d21e7fff67c2ba; current SHA256 d38de0da7f792e34b56e5ef225160a88221fb8a9b64e309e2b28f34bc7038b88. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/dna_topoisomerase_iv_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070; current SHA256 fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/dnaa_diaa_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4; current SHA256 fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/dnaa_dnab_dnac_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56; current SHA256 a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T055925Z-dnaa-dnab-dnac-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/dnaa_dps_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87; current SHA256 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml; Complete maintained YAML at 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected; no maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-0 | reviews/structured/20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence scopes, assessments, verdicts, findings and proposed actions inspected. Historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/0-stale.diff; Original frozen target versus current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8 | supports | Empty target diff: no stale scientific field in this assigned slice. Current primary and authority reassessment was nevertheless performed. |
| micro-record-1 | data/structures/other/dna_polymerase_iii_complex.yaml; Complete maintained YAML at 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected; no maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-1 | reviews/structured/20261022T055920Z-dna-polymerase-iii-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence scopes, assessments, verdicts, findings and proposed actions inspected. Historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/1-stale.diff; Original frozen target versus current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8 | supports | Empty target diff: no stale scientific field in this assigned slice. Current primary and authority reassessment was nevertheless performed. |
| micro-record-2 | data/structures/other/dna_polymerase_iii_core_complex.yaml; Complete maintained YAML at 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected; no maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-2 | reviews/structured/20261022T055921Z-dna-polymerase-iii-core-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs, checks, evidence scopes, assessments, verdicts, findings and proposed actions inspected. Historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/2-stale.diff; Original frozen target versus current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8 | supports | Empty target diff: no stale scientific field in this assigned slice. Current primary and authority reassessment was nevertheless performed. |
| micro-policy | docs/CURATION.md; Components and exact family grounding; formation versus function; discussions append-only contract | supports | Verified taxon-neutral whole-protein families are distinct from reference-strain examples and domains. UNKNOWN formation is not inherently defective. Preserve historical rationale/posed_date; current prompts/notes may be narrowed after supported curation. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component classes, complex identity/hierarchy and graph scopes | supports | Generic classes/subcomplex components and bounded NONMECHANISTIC FUNCTION outlines are valid. No optional individual-protein inventory is required for a correctly GO-grounded subcomplex record. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks; current profile, config and shared review contract | supports | Positive molecular/pathway claims trigger source applicability even without an expression assertion. Official catalogue and actual matched gene/module checks require strain and computational limits. Seventeen common local inputs are hash-identical to prior reads; skill/profile/config/review contract and pertinent curation clauses reread. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Constituent references, direct versus contextual evidence, bounded function outlines | supports | Physical identity and descriptive membership/function are assessed separately from formation necessity, a complete reaction sequence, kinetic transition measurements and mandatory new experiments. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/original-audit.json; Six actual original validate/render commands;42 historical input occurrences;6 original artifacts | supports | All three original YAMLs validate and render exactly their retained Markdown. All42 historical input hashes match recorded source revisions; all6 artifacts equal the original PR head. |
| micro-up-P03007 | https://rest.uniprot.org/uniprotkb/P03007.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P03007.raw | supports | P03007: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit epsilon; genes ['dnaQ']; loci ['b0215', 'JW0205']; taxon 83333; InterPro ['IPR006054', 'IPR006309', 'IPR013520', 'IPR012337', 'IPR036397']. Native annotations are authority evidence, not independent body reads of every linked paper. |
| micro-up-P06710 | https://rest.uniprot.org/uniprotkb/P06710.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P06710.raw | supports | P06710: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit tau; genes ['dnaX']; loci ['b0470', 'JW0459']; taxon 83333; InterPro ['IPR003593', 'IPR001270', 'IPR008921', 'IPR022001', 'IPR022754', 'IPR012763', 'IPR021029', 'IPR050238', 'IPR045085', 'IPR027417', 'IPR038249']. Native annotations are authority evidence, not independent body reads of every linked paper. Programmed frameshifting distinguishes tau/gamma, and SUBUNIT explicitly permits three copies of either or both; cellular viability annotations are not formation measurements for every isolated loader. |
| micro-up-P0A988 | https://rest.uniprot.org/uniprotkb/P0A988.json; Current native identity/status/name/primary gene/loci/taxon only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P0A988.raw | supports | P0A988: UniProtKB reviewed (Swiss-Prot); Beta sliding clamp; genes ['dnaN']; loci ['b3701', 'JW3678']; taxon 83333; InterPro ['IPR046938', 'IPR001001', 'IPR022635', 'IPR022637', 'IPR022634']. External beta reference used only to select dnaN locus for whole-holoenzyme dataset context; not added as a maintained example or used to certify additional functional literature. |
| micro-up-P0ABS8 | https://rest.uniprot.org/uniprotkb/P0ABS8.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P0ABS8.raw | supports | P0ABS8: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit theta; genes ['holE']; loci ['b1842', 'JW1831']; taxon 83333; InterPro ['IPR009052', 'IPR036745']. Native annotations are authority evidence, not independent body reads of every linked paper. Native uncertainty about exact theta function does not negate its core membership; no theta-specific polymerase or proofreading catalysis is asserted. |
| micro-up-P10443 | https://rest.uniprot.org/uniprotkb/P10443.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P10443.raw | supports | P10443: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit alpha; genes ['dnaE']; loci ['b0184', 'JW0179']; taxon 83333; InterPro ['IPR011708', 'IPR041931', 'IPR040982', 'IPR048472', 'IPR004805', 'IPR029460', 'IPR012340', 'IPR004365', 'IPR004013', 'IPR003141', 'IPR016195', 'IPR049821']. Native annotations are authority evidence, not independent body reads of every linked paper. Historical E.coli polC synonym does not equate DnaE with the separate Gram-positive PolC class. |
| micro-up-P28630 | https://rest.uniprot.org/uniprotkb/P28630.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28630.raw | supports | P28630: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit delta; genes ['holA']; loci ['b0640', 'JW0635']; taxon 83333; InterPro ['IPR008921', 'IPR032780', 'IPR010372', 'IPR005790', 'IPR027417']. Native annotations are authority evidence, not independent body reads of every linked paper. |
| micro-up-P28631 | https://rest.uniprot.org/uniprotkb/P28631.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28631.raw | supports | P28631: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit delta'; genes ['holB']; loci ['b1099', 'JW1085']; taxon 83333; InterPro ['IPR008921', 'IPR004622', 'IPR015199', 'IPR050238', 'IPR048731', 'IPR027417']. Native annotations are authority evidence, not independent body reads of every linked paper. |
| micro-up-P28632 | https://rest.uniprot.org/uniprotkb/P28632.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28632.raw | supports | P28632: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit psi; genes ['holD']; loci ['b4372', 'JW4334']; taxon 83333; InterPro ['IPR004615', 'IPR036654', 'IPR018382']. Native annotations are authority evidence, not independent body reads of every linked paper. |
| micro-up-P28905 | https://rest.uniprot.org/uniprotkb/P28905.json; Native identity/status/name/primary gene/loci/taxon/InterPro plus complete relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28905.raw | supports | P28905: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit chi; genes ['holC']; loci ['b4259', 'JW4216']; taxon 83333; InterPro ['IPR007459', 'IPR036768']. Native annotations are authority evidence, not independent body reads of every linked paper. |
| micro-query-dnaE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-dnaE.raw | supports | Current bounded query returns ['P10443']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-dnaQ | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaQ%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-dnaQ.raw | supports | Current bounded query returns ['P03007']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-dnaX | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaX%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-dnaX.raw | supports | Current bounded query returns ['P06710']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-holA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holA.raw | supports | Current bounded query returns ['P28630']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-holB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holB.raw | supports | Current bounded query returns ['P28631']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-holC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holC.raw | supports | Current bounded query returns ['P28905']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-holD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holD.raw | supports | Current bounded query returns ['P28632']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-query-holE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holE.raw | supports | Current bounded query returns ['P0ABS8']; singleton agrees with maintained identity. This does not reconstruct an October query or prove membership/formation. |
| micro-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/tax-562.raw | supports | 562: Escherichia coli; rank species. Species562 is distinct from reference strain83333; this does not identify unread source experimental strains. |
| micro-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/tax-83333.raw | supports | 83333: Escherichia coli K-12; rank strain. Species562 is distinct from reference strain83333; this does not identify unread source experimental strains. |
| micro-go-0003689 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003689; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0003689.raw | supports | GO:0003689: DNA clamp loader activity; obsolete=False; definition {'text': 'Facilitating the opening of the ring structure of the PCNA complex, or any of the related sliding clamp complexes, and their closing around the DNA duplex, driven by ATP hydrolysis.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '16082778'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0003887 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003887; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0003887.raw | supports | GO:0003887: DNA-directed DNA polymerase activity; obsolete=False; definition {'text': "Catalysis of the reaction: deoxynucleoside triphosphate + DNA(n) = diphosphate + DNA(n+1); DNA-template-directed extension of the 3'-end of a DNA strand by one nucleotide at a time.", 'xrefs': [{'dbCode': 'EC', 'dbId': '2.7.7.7'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0006260 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0006260.raw | supports | GO:0006260: DNA replication; obsolete=False; definition {'text': 'The cellular metabolic process in which a cell duplicates one or more molecules of DNA. DNA replication begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, and ends when the original DNA molecule has been completely duplicated and the copies topologically separated. The unit of replication usually corresponds to the genome of the cell, an organelle, or a virus. The template for replication can either be an existing DNA molecule or RNA.'}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0009360 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009360; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0009360.raw | supports | GO:0009360: DNA polymerase III complex; obsolete=False; definition {'text': "The DNA polymerase III holoenzyme is a complex that contains 10 different types of subunits. These subunits are organized into 3 functionally essential sub-assemblies: the pol III core, the beta sliding clamp processivity factor and the clamp-loading complex. The pol III core carries out the polymerase and the 3'-5' exonuclease proofreading activities. The polymerase is tethered to the template via the sliding clamp processivity factor. The clamp-loading complex assembles the beta processivity factor onto the primer template and plays a central role in the organization and communication at the replication fork.", 'xrefs': [{'dbCode': 'PMID', 'dbId': '11525729'}, {'dbCode': 'PMID', 'dbId': '12940977'}, {'dbCode': 'UniProt', 'dbId': 'P06710'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0032991 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0032991.raw | supports | GO:0032991: protein-containing complex; obsolete=False; definition {'text': 'A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.'}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0042575 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042575; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0042575.raw | supports | GO:0042575: DNA polymerase complex; obsolete=False; definition {'text': 'A protein complex that possesses DNA polymerase activity and is involved in template directed synthesis of DNA.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '12045093'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0043846 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0043846.raw | supports | GO:0043846: DNA polymerase III, clamp loader complex; obsolete=False; definition {'text': 'A heptamer that includes the tau and gamma products of the dnaX gene and the chi/psi subcomplex. Confers structural asymmetry that allows the polymerase to replicate both leading and lagging strands.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '12940977'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0043847 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043847; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0043847.raw | supports | GO:0043847: DNA polymerase III, clamp loader chi/psi subcomplex; obsolete=False; definition {'text': 'A dimer composed of the chi and psi subunits which is a subassembly of the DNA polymerase III clamp loader complex and serves as a bridge between the DnaX complex and the single-stranded DNA-binding protein (SSB).', 'xrefs': [{'dbCode': 'PMID', 'dbId': '12940977'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0044775 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044775; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0044775.raw | supports | GO:0044775: DNA polymerase III, beta sliding clamp processivity factor complex; obsolete=False; definition {'text': 'A subcomplex of the DNA polymerase III holoenzyme which is responsible for tethering the catalytic subunit of DNA polymerase to DNA during high-speed replication. The complex is homodimeric in prokaryotes, and homotrimeric in other species.', 'xrefs': [{'dbCode': 'UniProt', 'dbId': 'O73947'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-go-0044776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0044776.raw | supports | GO:0044776: DNA polymerase III, core complex; obsolete=False; definition {'text': "The DNA polymerase III core complex consists of the alpha,epsilon and theta subunits and is carries out the polymerase and the 3'-5' exonuclease proofreading activities.", 'xrefs': [{'dbCode': 'UniProt', 'dbId': 'P06710'}]}. Ontology wording is checked separately against biological source scope, not adopted as infallible experiment evidence. |
| micro-isa-0043846 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/isa-0043846.raw | supports | Ancestors ['GO:0043846', 'GO:0140513', 'GO:0032991', 'GO:0005575']; children [{'id': 'GO:0043847', 'relation': 'part_of'}]. Core parent GO0042575 is a biological activity-based class assertion, not claimed as a direct current GO edge. Loader/core nuclear-complex ancestry is an upstream mismatch with bacterial source evidence, not imported into records. |
| micro-isa-0009360 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009360/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/isa-0009360.raw | supports | Ancestors ['GO:1902494', 'GO:0061695', 'GO:0009360', 'GO:1990234', 'GO:0140535', 'GO:0032991', 'GO:0042575', 'GO:0005575']; children [{'id': 'GO:0043846', 'relation': 'part_of'}, {'id': 'GO:0044776', 'relation': 'part_of'}, {'id': 'GO:0044775', 'relation': 'part_of'}]. Core parent GO0042575 is a biological activity-based class assertion, not claimed as a direct current GO edge. Loader/core nuclear-complex ancestry is an upstream mismatch with bacterial source evidence, not imported into records. |
| micro-isa-0044776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/isa-0044776.raw | supports | Ancestors ['GO:0140513', 'GO:0032991', 'GO:0005575', 'GO:0044776']; children [{'id': 'GO:0043845', 'relation': 'part_of'}]. Core parent GO0042575 is a biological activity-based class assertion, not claimed as a direct current GO edge. Loader/core nuclear-complex ancestry is an upstream mismatch with bacterial source evidence, not imported into records. |
| micro-constraints-0043846 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/constraints; Exact taxonConstraints field only; unrelated blacklist entries not used; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/constraints-0043846.raw | context_only | Current only-in-Eukaryota constraint [{'ancestorId': 'GO:0043846', 'ancestorName': 'DNA polymerase III, clamp loader complex', 'relationship': 'only_in_taxon', 'taxId': '2759', 'taxIdType': 'NCBITaxon', 'taxName': 'Eukaryota'}] conflicts with named bacterial identity and primary E.coli evidence. No such restriction is asserted in the maintained record; not a new record finding. |
| micro-constraints-0044776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/constraints; Exact taxonConstraints field only; unrelated blacklist entries not used; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/constraints-0044776.raw | context_only | Current only-in-Eukaryota constraint [{'ancestorId': 'GO:0044776', 'ancestorName': 'DNA polymerase III, core complex', 'relationship': 'only_in_taxon', 'taxId': '2759', 'taxIdType': 'NCBITaxon', 'taxName': 'Eukaryota'}] conflicts with named bacterial identity and primary E.coli evidence. No such restriction is asserted in the maintained record; not a new record finding. |
| micro-ipr-IPR005790 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005790/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR005790.raw | supports | IPR005790: {'name': 'DNA polymerase III, delta subunit', 'short': 'DNA_polIII_delta'}; type family; signatures {'panther': {'PTHR34388': 'DNA POLYMERASE III SUBUNIT DELTA'}, 'ncbifam': {'TIGR01128': 'DNA polymerase III subunit delta'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. Exact HolA family; llm=true checked=true generated sentence attributing proofreading is not used as delta activity evidence. |
| micro-ipr-IPR007459 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007459/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR007459.raw | supports | IPR007459: {'name': 'DNA polymerase III chi subunit, HolC', 'short': 'DNA_pol3_chi'}; type family; signatures {'panther': {'PTHR38767': 'DNA POLYMERASE III SUBUNIT CHI'}, 'pfam': {'PF04364': 'DNA polymerase III chi subunit, HolC'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR004615 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004615/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004615.raw | supports | IPR004615: {'name': 'DNA polymerase III, psi subunit', 'short': 'DNA_pol_III_psi'}; type family; signatures {'pirsf': {'PIRSF029225': 'DNA polymerase III, psi subunit'}, 'pfam': {'PF03603': 'DNA polymerase III psi subunit'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. Exact HolD family; historical unknown-function wording does not refute primary biochemistry. |
| micro-ipr-IPR004622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004622/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004622.raw | supports | IPR004622: {'name': 'DNA polymerase III, delta prime subunit', 'short': 'DNA_pol_HolB'}; type domain; signatures {'ncbifam': {'TIGR00678': "DNA polymerase III subunit delta'"}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR012763-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012763/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR012763-retry.raw | supports | IPR012763: {'name': 'DNA polymerase III, subunit gamma/ tau, N-terminal', 'short': 'DNA_pol_III_sug/sutau_N'}; type domain; signatures {'ncbifam': {'TIGR02397': 'DNA polymerase III subunit gamma/tau'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR009052-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009052/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR009052-retry.raw | supports | IPR009052: {'name': 'DNA polymerase III-theta, bacterial', 'short': 'DNA_pol_III_theta_bac'}; type family; signatures {'pfam': {'PF06440': 'DNA polymerase III, theta subunit'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR006309-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006309/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR006309-retry.raw | supports | IPR006309: {'name': 'DNA polymerase 3, epsilon subunit', 'short': 'DnaQ_proteo'}; type family; signatures {'cdd': {'cd06131': "DEDDh 3'-5' exonuclease domain of the epsilon subunit of Escherichia coli DNA polymerase III and similar proteins"}, 'ncbifam': {'TIGR01406': 'DNA polymerase III subunit epsilon'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. Full family is explicitly proteobacterial, not silently generalized to every epsilon-class taxon. |
| micro-ipr-IPR006054 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006054/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR006054.raw | supports | IPR006054: {'name': 'DNA polymerase III epsilon subunit, exonuclease domain', 'short': 'DnaQ'}; type domain; signatures {'ncbifam': {'TIGR00573': 'exonuclease, DNA polymerase III, epsilon subunit family'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR004805 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004805/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004805.raw | supports | IPR004805: {'name': 'Error-prone DNA polymerase/DNA polymerase III subunit alpha DnaE/PolC', 'short': 'DnaE2/DnaE/PolC'}; type family; signatures {'panther': {'PTHR32294': 'DNA POLYMERASE III SUBUNIT ALPHA'}, 'ncbifam': {'TIGR00594': 'DNA polymerase III subunit alpha'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. Broader DnaE2/DnaE/PolC family is not an exact DnaE-only substitute. |
| micro-ipr-IPR050238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR050238.raw | supports | IPR050238: {'name': 'DNA Replication and Repair Clamp Loader Complex', 'short': 'DNA_Rep/Repair_Clamp_Loader'}; type family; signatures {'panther': {'PTHR11669': 'DNA Replication and Repair Clamp Loader Complex'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. Broad shared clamp-loader family also contains eukaryotic/plant proteins; llm=true checked=false prose not primary evidence or exact DnaX/HolB identity. |
| micro-ipr-IPR045085 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045085/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR045085.raw | supports | IPR045085: {'name': 'DNA polymerase III, subunit gamma/tau, helical lid domain', 'short': 'HLD_clamp_pol_III_gamma_tau'}; type domain; signatures {'pfam': {'PF22608': 'DNA polymerase III clamp loader subunit, ATPase lid domain'}, 'cdd': {'cd18137': 'helical lid domain of DNA polymerase III subunits gamma and tau'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR048731-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048731/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR048731-retry.raw | supports | IPR048731: {'name': "DNA polymerase III subunit delta', AAA+ ATPase lid domain, gammaproteobacteria", 'short': 'HolB_lid-gammaproteobact'}; type domain; signatures {'pfam': {'PF21500': "DNA polymerase III subunit delta', AAA+ ATPase lid domain"}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR004365 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004365/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004365.raw | supports | IPR004365: {'name': 'OB-fold nucleic acid binding domain, AA-tRNA synthetase-type', 'short': 'NA-bd_OB_tRNA'}; type domain; signatures {'pfam': {'PF01336': 'OB-fold nucleic acid binding domain'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-ipr-IPR004013 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004013/; Complete native name/type/hierarchy/signatures/description and generated-prose flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004013.raw | supports | IPR004013: {'name': 'PHP domain', 'short': 'PHP_dom'}; type domain; signatures {'pfam': {'PF02811': 'PHP domain'}}. Complete metadata description/type/hierarchy/integrated signatures inspected; matching UniProt example xref is separate membership evidence. |
| micro-pmid-11525729 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11525729+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED metadata and deposited abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/pmid-11525729.raw | supports | 11525729: Crystal structure of the processivity clamp loader gamma (gamma) complex of E. coli DNA polymerase III.; DOI 10.1016/s0092-8674(01)00463-9. Primary-study abstract completely read; no body claim from this response alone. |
| micro-pmid-12940977 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12940977+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED metadata and deposited abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/pmid-12940977.raw | context_only | 12940977: Chromosomal replicases as asymmetric dimers: studies of subunit arrangement and functional consequences.; DOI 10.1046/j.1365-2958.2003.03645.x. Secondary review abstract, with body scope separately stated. |
| micro-pmid-3283127 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3283127+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1000; Complete exact MED metadata and deposited abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/pmid-3283127.raw | supports | 3283127: DNA polymerase III holoenzyme of Escherichia coli. III. Distinctive processive polymerases reconstituted from purified subunits.; DOI 10.1016/s0021-9258(18)68678-8. Primary-study abstract completely read; no body claim from this response alone. |
| micro-jeruzalmi2001-pdf | https://odonnell.rockefeller.edu/assets/pdfs/119.pdf; Genuine author-hosted PDF pp429–431 Summary/Introduction/Results structure determination/general description and Fig1 text caption; pp439–440 conclusion and Experimental Procedures; no pixels/coordinates/supplements; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/jeruzalmi2001-pdf.raw | supports | Observed nucleotide-free gamma3-delta-delta-prime pentamer uses truncated gamma1–373, purified reconstitution and anisotropic2.7/3.0Å diffraction. Authors distinguish observed structure from speculative ATP-transition models; activity of the truncated preparation is reported with data not shown. Tau/chi/psi are not crystallized constituents. Source species E.coli does not certify a living unmodified K12 heptamer preparation. |
| micro-mchenry2003-pdf | https://www.sbs.utexas.edu/psaxena/bio226r/articles/dna_replication_mchenry_2003.pdf; Genuine secondary-review PDF pp1157–1159 and opening p1160: organization/DnaX alternatives, tau coupling/helicase/processivity discussion, Fig1 text caption; no complete-review or pixel claim; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/mchenry2003-pdf.raw | supports | Secondary review describes full DnaX3-delta-delta-prime-chi-psi heptamer: any tau/gamma mixture can load beta with similar efficiency before polymerase; tau contributes additional polymerase/helicase contacts. Mixed tau/gamma in-vivo model is distinguished from minimum clamp-loading composition. No invariant in-vivo ratio, full-review body read or primary new assay claimed. |
| micro-maki1988-api | https://api.elsevier.com/content/article/pii/S0021925818686788?httpAccept=text/xml; Publisher core XML metadata only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/maki1988-api.raw | supports | Exact title/year/journal/DOI corroborated; response name full-text-retrieval does not mean primary body was delivered. Maki/Kornberg assessed only at complete primary-abstract tier. |
| micro-maki1988-html-access | https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/maki1988-html.raw | context_only | HTTP403 diagnostic only. No inaccessible body or family metadata certified; independent complete abstract or later successful exact-authority response is recorded separately. |
| micro-maki1988-pdf-access | https://www.jbc.org/article/S0021-9258(18)68678-8/pdf; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/maki1988-pdf.raw | context_only | HTTP403 diagnostic only. No inaccessible body or family metadata certified; independent complete abstract or later successful exact-authority response is recorded separately. |
| micro-ipr-IPR012763-access | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012763/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR012763.raw | context_only | HTTP429 diagnostic only. No inaccessible body or family metadata certified; independent complete abstract or later successful exact-authority response is recorded separately. |
| micro-ipr-IPR009052-access | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009052/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR009052.raw | context_only | HTTP429 diagnostic only. No inaccessible body or family metadata certified; independent complete abstract or later successful exact-authority response is recorded separately. |
| micro-ipr-IPR006309-access | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006309/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR006309.raw | context_only | HTTP429 diagnostic only. No inaccessible body or family metadata certified; independent complete abstract or later successful exact-authority response is recorded separately. |
| micro-ipr-IPR048731-access | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048731/; Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR048731.raw | context_only | HTTP429 diagnostic only. No inaccessible body or family metadata certified; independent complete abstract or later successful exact-authority response is recorded separately. |
| micro-historical-1-root51-maki1988-publisher | https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext; Retained publisher403 response | context_only | The publisher route did not yield the primary body; this paper is assessed at complete native abstract tier. Historical access time/hash preserved; no fresh retrieval. Correct kind only from database to validation/context_only; original already admitted body-access limitation. |
| micro-historical-1-root51-maki1988-pdf | https://www.jbc.org/article/S0021-9258(18)68678-8/pdf; Retained publisher403 response | context_only | The publisher route did not yield the primary body; this paper is assessed at complete native abstract tier. Historical access time/hash preserved; no fresh retrieval. Correct kind only from database to validation/context_only; original already admitted body-access limitation. |
| micro-historical-2-root51-maki1988-publisher | https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext; Retained publisher403 response | context_only | The publisher route did not yield the primary body; this paper is assessed at complete native abstract tier. Historical access time/hash preserved; no fresh retrieval. Correct kind only from database to validation/context_only; original already admitted body-access limitation. |
| micro-historical-2-root51-maki1988-pdf | https://www.jbc.org/article/S0021-9258(18)68678-8/pdf; Retained publisher403 response | context_only | The publisher route did not yield the primary body; this paper is assessed at complete native abstract tier. Historical access time/hash preserved; no fresh retrieval. Correct kind only from database to validation/context_only; original already admitted body-access limitation. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official20-organism catalogue and all dataset entries; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/catalogue.raw | supports | Actual E.coli host has precise1k among listed datasets. Selection is a bounded current catalogue check, not universal or future coverage. |
| micro-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete selected precise1k metadata and five-strain list; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-meta.raw | context_only | BW25113,DGF-298,GMOS,MG1655,W3110;1035samples/518conditions/201modules/4257genes. K12-related reference context is not exact Jeruzalmi recombinant-preparation coverage or Maki experimental strain identification. |
| micro-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 returned module names/regulators/functions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-modules.raw | context_only | Complete selected module inventory inspected; names and inferred regulator labels are not proof of physical assembly or direct regulation. |
| micro-ecoli-gene-b0470 | https://imodulondb.org/api/genes/b0470/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0470.raw | context_only | b0470 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b0640 | https://imodulondb.org/api/genes/b0640/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0640.raw | context_only | b0640 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b1099 | https://imodulondb.org/api/genes/b1099/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b1099.raw | context_only | b1099 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b4259 | https://imodulondb.org/api/genes/b4259/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b4259.raw | context_only | b4259 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b4372 | https://imodulondb.org/api/genes/b4372/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b4372.raw | context_only | b4372 yields201 rows and hits [{"k": 145, "name": "ppGpp", "regulator": ["ppGpp"], "function": "Stringent response", "category": "Global Stress", "weight": 0.055361181, "threshold": 0.048379363, "in_imodulon": true}]. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b0184 | https://imodulondb.org/api/genes/b0184/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0184.raw | context_only | b0184 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b0215 | https://imodulondb.org/api/genes/b0215/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0215.raw | context_only | b0215 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b1842 | https://imodulondb.org/api/genes/b1842/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b1842.raw | context_only | b1842 yields201 rows and hits [{"k": 147, "name": "PAL 26 Del", "regulator": null, "function": "Unknown", "category": "Unknown", "weight": 0.124483338, "threshold": 0.058096464, "in_imodulon": true}]. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-gene-b3701 | https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus weights/thresholds/membership rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b3701.raw | context_only | b3701 yields201 rows and hits []. Negative threshold membership is not gene absence or dispensability; positive membership does not establish assembly, localization, direct regulation or formation. |
| micro-ecoli-module-145 | https://imodulondb.org/api/imodulons/e_coli/precise1k/145; Actual module metadata and complete gene-weight list; generated AI prose and activities not used; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-module-145.raw | context_only | Module145 ppGpp; function Stringent response; 70 genes; b4372 weight 0.055361181 exceeds threshold 0.048379363. Computational context only. Module147 has no regulator annotation and function Unknown; no mechanistic inference from its name. |
| micro-ecoli-module-147 | https://imodulondb.org/api/imodulons/e_coli/precise1k/147; Actual module metadata and complete gene-weight list; generated AI prose and activities not used; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-module-147.raw | context_only | Module147 PAL 26 Del; function Unknown; 43 genes; b1842 weight 0.124483338 exceeds threshold 0.058096464. Computational context only. Module147 has no regulator annotation and function Unknown; no mechanistic inference from its name. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z receipt | context_only | Historical runner unavailable/exit1 permission limitation; no fresh execution claimed. Fresh official API applicability/gene/module fallback above is separate. |
| micro-native-dna_polymerase_iii_clamp_loader_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-verify-receipt.json; Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 5 reviewed examples and5 COVERED typed nodes. Implemented identity/example coverage does not certify exact family grounding or full biological completeness. |
| micro-native-dna_polymerase_iii_clamp_loader_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-causal-receipt.json; Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-causal.log SHA256 aca3b51abc154a55cd6b3d81b01fc8a21768e3ec3940102586a9945621646d06 | supports | Actual exit0; 5 reviewed examples and5 COVERED typed nodes. Implemented identity/example coverage does not certify exact family grounding or full biological completeness. |
| micro-native-dna_polymerase_iii_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-verify-receipt.json; Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 0 examples and0 typed GENE_OR_PROTEIN nodes; three STRUCTURE component nodes checked separately. Implemented identity/example coverage does not certify exact family grounding or full biological completeness. |
| micro-native-dna_polymerase_iii_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-causal-receipt.json; Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual exit0; 0 examples and0 typed GENE_OR_PROTEIN nodes; three STRUCTURE component nodes checked separately. Implemented identity/example coverage does not certify exact family grounding or full biological completeness. |
| micro-native-dna_polymerase_iii_core_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-verify-receipt.json; Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 3 reviewed examples and3 COVERED typed nodes. Implemented identity/example coverage does not certify exact family grounding or full biological completeness. |
| micro-native-dna_polymerase_iii_core_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-causal-receipt.json; Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-causal.log SHA256 622c34a9d261773a36cbd6c978ead78ec02d5fe3b0cb7c2e0e1c6688ceff466d | supports | Actual exit0; 3 reviewed examples and3 COVERED typed nodes. Implemented identity/example coverage does not certify exact family grounding or full biological completeness. |
| plaque-current-3 | data/structures/other/dna_replication_factor_a_complex.yaml; Entire maintained record at frozen source 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e | supports | Complete current definition, hierarchy, components, all examples, taxonomy, functions, graphs, discussions and history independently read. RFA new examples/component and edge evidence/history substantively reassessed. |
| plaque-original-3-yaml | reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml; Complete historical paired observation and deterministic Markdown equivalence | supports | Original scientific findings, actions and evidence scopes independently challenged against current sources; all old corpus commands remain historical. |
| plaque-original-3-md | reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.md; Complete historical paired observation and deterministic Markdown equivalence | supports | Original scientific findings, actions and evidence scopes independently challenged against current sources; all old corpus commands remain historical. |
| plaque-current-4 | data/structures/other/dna_replication_factor_c_complex.yaml; Entire maintained record at frozen source 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e | supports | Complete current definition, hierarchy, components, all examples, taxonomy, functions, graphs, discussions and history independently read. RFC target is byte-unchanged. |
| plaque-original-4-yaml | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml; Complete historical paired observation and deterministic Markdown equivalence | supports | Original scientific findings, actions and evidence scopes independently challenged against current sources; all old corpus commands remain historical. |
| plaque-original-4-md | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.md; Complete historical paired observation and deterministic Markdown equivalence | supports | Original scientific findings, actions and evidence scopes independently challenged against current sources; all old corpus commands remain historical. |
| plaque-current-5 | data/structures/other/dna_replication_preinitiation_complex.yaml; Entire maintained record at frozen source 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e | supports | Complete current definition, hierarchy, components, all examples, taxonomy, functions, graphs, discussions and history independently read. New Cdc45 example/history substantively reassessed; existing mechanistic prose remains unchanged. |
| plaque-original-5-yaml | reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.yaml; Complete historical paired observation and deterministic Markdown equivalence | supports | Original scientific findings, actions and evidence scopes independently challenged against current sources; all old corpus commands remain historical. |
| plaque-original-5-md | reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.md; Complete historical paired observation and deterministic Markdown equivalence | supports | Original scientific findings, actions and evidence scopes independently challenged against current sources; all old corpus commands remain historical. |
| plaque-policy | docs/CURATION.md; Frozen local instructions/schema applied | supports | Exact structure/class grounding, formation versus viability, source scope and append-only history rules. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen local instructions/schema applied | supports | Protein/complex identity, essentiality and graph semantics; complexes permitted under GENE_OR_PROTEIN. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen local instructions/schema applied | supports | Positive molecular/pathway assertions trigger structured-source applicability regardless of expression wording. |
| plaque-review-profile | docs/record-review-profile.md; Frozen local instructions/schema applied | supports | Issue-bearing immutable review successor and exact scoped historical lineage. |
| plaque-review-schema | schema/record_review.yaml; Frozen local instructions/schema applied | supports | Native evidence/assessment/lineage enums. |
| plaque-checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen local instructions/schema applied | supports | Complete bounded field-by-field evidence review; no forced optional examples. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen local instructions/schema applied | supports | Distinguish descriptive membership/placement from sourced causal mechanisms. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662,GO:0005663,GO:0031261,GO:0140513,GO:0003697,GO:0032991,GO:0005657,GO:0003689,GO:0006260,GO:0032993,GO:0005654,GO:0042555,GO:0000811; Thirteen requested terms: identities/definitions/synonyms/xrefs and relevant direct typed children only; unrelated children not judged; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go.raw | supports | Fresh active GO0005662/0005663/0031261 identities and exact definitions agree with their generic RFA/RFC/pre-IC classes. Direct relevant parent children support nuclear/protein-DNA class and fork/nucleoplasm parthood. GO0031261 lacks the record appended double-hexamer/kinase/CMG/bridge mechanism. GO0006260 is a process identity, not pre-IC-specific causal evidence. |
| plaque-go-0005662-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/ancestors; Complete focal ancestor array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005662-ancestors.raw | supports | Focal current ancestor identity corroborates declared hierarchy; an ancestor list alone does not prove a direct edge. |
| plaque-go-0005662-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/constraints; Complete focal taxonConstraints; negative blacklist entries not interpreted as biological experiment; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005662-constraints.raw | supports | Focal native taxon constraints inspected; eukaryotic RFA/pre-IC scope and generic RFC scope are distinguished. This is not a prevalence census or a claim that archaeal RFC lacks homologous function. |
| plaque-go-0005663-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/ancestors; Complete focal ancestor array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005663-ancestors.raw | supports | Focal current ancestor identity corroborates declared hierarchy; an ancestor list alone does not prove a direct edge. |
| plaque-go-0005663-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/constraints; Complete focal taxonConstraints; negative blacklist entries not interpreted as biological experiment; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005663-constraints.raw | supports | Focal native taxon constraints inspected; eukaryotic RFA/pre-IC scope and generic RFC scope are distinguished. This is not a prevalence census or a claim that archaeal RFC lacks homologous function. |
| plaque-go-0031261-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031261/ancestors; Complete focal ancestor array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0031261-ancestors.raw | supports | Focal current ancestor identity corroborates declared hierarchy; an ancestor list alone does not prove a direct edge. |
| plaque-go-0031261-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031261/constraints; Complete focal taxonConstraints; negative blacklist entries not interpreted as biological experiment; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0031261-constraints.raw | supports | Focal native taxon constraints inspected; eukaryotic RFA/pre-IC scope and generic RFC scope are distinguished. This is not a prevalence census or a claim that archaeal RFC lacks homologous function. |
| plaque-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete identity, rank, aliases and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/tax-2759.raw | supports | Verified Eukaryota broad clade. Reference-strain accession does not identify every cited experimental strain. |
| plaque-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete identity, rank, aliases and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/tax-4932.raw | supports | Verified Saccharomyces cerevisiae species. Reference-strain accession does not identify every cited experimental strain. |
| plaque-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete identity, rank, aliases and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/tax-559292.raw | supports | Verified Saccharomyces cerevisiae S288C reference strain. Reference-strain accession does not identify every cited experimental strain. |
| plaque-pmid-9242902 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9242902+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-9242902.raw | supports | Wold1997 secondary-review abstract supports conserved heterotrimer, approximate70/30/14 size classes and nonspecific ssDNA binding/replication-repair roles. It is not a newly read review body or strain-specific yeast experiment. |
| plaque-pmid-7651383 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7651383+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-7651383.raw | supports | Cullmann1995 primary abstract reports five yeast RFC genes and homologous ATPase/PCNA role; gene-essential cell proliferation is not physical assembly necessity. |
| plaque-pmid-8559655 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8559655+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-8559655.raw | supports | Gary/Burgers1995 primary abstract identifies RFC5/YBR0810 as integral fifth yeast subunit via co-overexpression of RFC1–5; viability and E.coli overexpression do not define natural-host formation necessity. |
| plaque-pmid-14614842 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-14614842.raw | supports | Kim/MacNeill2003 is a secondary review on RFC family variants; used as bibliographic/context evidence, not five-gene yeast experiment. |
| plaque-pmid-14646196 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14646196+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-14646196.raw | supports | Kitabayashi2003 primary abstract studies Thermococcus kodakaraensis KOD1 recombinant RFC; archaeal host is not substituted for budding yeast. |
| plaque-pmid-16172520 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16172520+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-16172520.raw | supports | Nishida2005 primary abstract studies Pyrococcus furiosus RFC subunit C-terminal truncations, ternary-complex stability and loading, not yeast RFC1–5 assembly. |
| plaque-pmid-12730134 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12730134+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-12730134.raw | supports | Takayama2003 primary abstract identifies budding-yeast GINS and conditional origin recruitment; full body is separately evidenced. |
| plaque-pmid-8901577 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8901577+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract; no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-8901577.raw | supports | Hopwood/Dalton1996 primary abstract reports Cdc45 replication initiation, physical association with Cdc46/Mcm5 and cell-cycle-independent localization; not a direct Mcm2–Mcm5 bridge or full pre-IC depletion assay. |
| plaque-brill1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:1885001%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=5; Unique MED1885001, complete primary abstract and metadata; publisher fulltext403; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/brill1991-meta.raw | supports | Brill/Stillman1991 primary abstract independently identifies the three yeast RFA genes and homologous three-subunit complex, gene essentiality and regulated transcription. It supports the added yeast gene/composition context, not precise S288C experimental provenance or physical formation necessity. |
| plaque-takayama2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC196052/; Complete Results sec2–9 including Fig1–7 text captions, Discussion sec11–13, Methods sec15–22; no figure pixels, Supplementary Table1 or raw data; strain identifiers retained as declared cultures without assigning S288C; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/takayama2003-pmc.raw | supports | Fresh genuine primary HTML: GINS four-member purification and conditional Sld5 mutant recovery/viability/replication, Psf1-origin recruitment and dependencies on Sld3/Dpb11, Cdc45 chromatin binding in psf1-1. Discussion explicitly distinguishes observed recruitment from proposed macromolecular model and alternative elongation explanations. No demonstrated loaded double-hexamer, specific modern kinase-target chain or Mcm2–Mcm5 bridging mechanism. |
| plaque-cullmann1995-pdf | https://repository.cshl.edu/id/eprint/24950/1/Characterization%20of%20the%20five%20replication%20factor%20C.pdf; Extracted text pp4661–4663,4665 and4668–4669 incl Table1/Fig8 text captions; no alignment image analysis or figure pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/cullmann1995-pdf.raw | supports | Fresh genuine author-repository PDF independently confirms yeast five-subunit cloning, RFC1/CDC44 identity, subunit homologs and PCNA function. Methods uses BJ926 purification and W303/W937 derivatives; gene disruptions test viability, not universal structure formation. Broad RFC2–5 similarity is not exact individual family grounding. |
| plaque-gary1995-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC307503/; Title/authors/DOI/complete abstract only; scan links not equivalent to reading scans; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gary1995-pmc.raw | supports | Correct legacy primary landing contains complete RFC5 abstract and scan links; no newly inspected page pixels or full Methods certified. |
| plaque-hopwood1996-correct-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC37987/; Exact title/metadata and complete abstract only; no full paper pages or image measurement; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/hopwood1996-correct-pmc.raw | supports | Correct legacy PMC37987 title/abstract matches PMID8901577 and nucleus annotation context; body scan links were not inspected as pixels. |
| plaque-wold1997-publisher | https://www.annualreviews.org/doi/10.1146/annurev.biochem.66.1.61; Actual status/response identity only; excluded from scientific support; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/wold1997-publisher.raw | context_only | 403 challenge, not secondary-review body |
| plaque-brill1991-pdf | https://genesdev.cshlp.org/content/5/9/1589.full.pdf; Actual status/response identity only; excluded from scientific support; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/brill1991-pdf.raw | context_only | 403 challenge, not primary PDF |
| plaque-takayama2003-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC196052.1/PMC196052.1.xml; Actual status/response identity only; excluded from scientific support; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/takayama2003-s3.raw | context_only | 404 response; genuine PMC HTML separately retrieved |
| plaque-ipr-IPR008591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008591/; Actual status/response identity only; excluded from scientific support; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR008591.raw | context_only | initial429; subsequent distinct retry succeeded |
| plaque-ipr-IPR005339 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005339/; Actual status/response identity only; excluded from scientific support; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR005339.raw | context_only | initial429; subsequent distinct retry succeeded |
| plaque-hopwood1996-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC26461/; Actual status/response identity only; excluded from scientific support; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/hopwood1996-pmc.raw | context_only | initial mistaken PMC26461 lead resolves to an unrelated GPCR paper; title check rejected it and no scientific content from it is used |
| plaque-up-P22336 | https://rest.uniprot.org/uniprotkb/P22336.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P22336.raw | supports | Current reviewed P22336 primary gene RFA1, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFA1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFA1.raw | supports | Exactly one current reviewed primary-gene query hit: P22336; identity only, not physical assembly evidence. |
| plaque-up-P26754 | https://rest.uniprot.org/uniprotkb/P26754.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P26754.raw | supports | Current reviewed P26754 primary gene RFA2, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFA2.raw | supports | Exactly one current reviewed primary-gene query hit: P26754; identity only, not physical assembly evidence. |
| plaque-up-P26755 | https://rest.uniprot.org/uniprotkb/P26755.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P26755.raw | supports | Current reviewed P26755 primary gene RFA3, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFA3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFA3.raw | supports | Exactly one current reviewed primary-gene query hit: P26755; identity only, not physical assembly evidence. |
| plaque-up-P38630 | https://rest.uniprot.org/uniprotkb/P38630.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P38630.raw | supports | Current reviewed P38630 primary gene RFC1, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC1.raw | supports | Exactly one current reviewed primary-gene query hit: P38630; identity only, not physical assembly evidence. |
| plaque-up-P40348 | https://rest.uniprot.org/uniprotkb/P40348.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P40348.raw | supports | Current reviewed P40348 primary gene RFC2, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFC2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC2.raw | supports | Exactly one current reviewed primary-gene query hit: P40348; identity only, not physical assembly evidence. |
| plaque-up-P38629 | https://rest.uniprot.org/uniprotkb/P38629.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P38629.raw | supports | Current reviewed P38629 primary gene RFC3, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFC3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC3.raw | supports | Exactly one current reviewed primary-gene query hit: P38629; identity only, not physical assembly evidence. |
| plaque-up-P40339 | https://rest.uniprot.org/uniprotkb/P40339.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P40339.raw | supports | Current reviewed P40339 primary gene RFC4, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFC4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC4%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC4.raw | supports | Exactly one current reviewed primary-gene query hit: P40339; identity only, not physical assembly evidence. |
| plaque-up-P38251 | https://rest.uniprot.org/uniprotkb/P38251.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P38251.raw | supports | Current reviewed P38251 primary gene RFC5, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-RFC5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC5.raw | supports | Exactly one current reviewed primary-gene query hit: P38251; identity only, not physical assembly evidence. |
| plaque-up-Q08032 | https://rest.uniprot.org/uniprotkb/Q08032.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q08032.raw | supports | Current reviewed Q08032 primary gene CDC45, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-CDC45 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACDC45%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-CDC45.raw | supports | Exactly one current reviewed primary-gene query hit: Q08032; identity only, not physical assembly evidence. |
| plaque-up-Q03406 | https://rest.uniprot.org/uniprotkb/Q03406.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q03406.raw | supports | Current reviewed Q03406 primary gene SLD5, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-SLD5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASLD5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-SLD5.raw | supports | Exactly one current reviewed primary-gene query hit: Q03406; identity only, not physical assembly evidence. |
| plaque-up-Q12488 | https://rest.uniprot.org/uniprotkb/Q12488.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q12488.raw | supports | Current reviewed Q12488 primary gene PSF1, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-PSF1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-PSF1.raw | supports | Exactly one current reviewed primary-gene query hit: Q12488; identity only, not physical assembly evidence. |
| plaque-up-P40359 | https://rest.uniprot.org/uniprotkb/P40359.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P40359.raw | supports | Current reviewed P40359 primary gene PSF2, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-PSF2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-PSF2.raw | supports | Exactly one current reviewed primary-gene query hit: P40359; identity only, not physical assembly evidence. |
| plaque-up-Q12146 | https://rest.uniprot.org/uniprotkb/Q12146.json; Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR LOCATION evidence; exact InterPro entries; no inference from unrelated functions; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q12146.raw | supports | Current reviewed Q12146 primary gene PSF3, exact S288C559292, locus and whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro xrefs independently read. Native localization or reference accession alone is not formation proof. |
| plaque-gene-PSF3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-PSF3.raw | supports | Exactly one current reviewed primary-gene query hit: Q12146; identity only, not physical assembly evidence. |
| plaque-ipr-IPR004591 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004591/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR004591.raw | supports | Native type family and name Replication factor A protein 1 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR014646 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014646/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR014646.raw | supports | Native type family and name Replication factor A protein 2 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR013970 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013970/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR013970.raw | supports | Native type family and name Replication factor A protein 3 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR012178 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012178/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR012178.raw | supports | Native type family and name Replication factor C subunit 1 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR050238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR050238.raw | supports | Native type family and name DNA Replication and Repair Clamp Loader Complex independently checked against same-class UniProt xrefs. Broad clamp-loader family is not exact RFC2–5 identity; llm-marked descriptive paragraph excluded as scientific evidence. |
| plaque-ipr-IPR013748 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013748/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR013748.raw | supports | Native type domain and name Replication factor C, C-terminal independently checked against same-class UniProt xrefs. C-terminal domain is not an entire RFC subunit class. |
| plaque-ipr-IPR008591-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008591/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR008591-retry.raw | supports | Native type family and name GINS complex subunit Sld5 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR005339-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005339/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR005339-retry.raw | supports | Native type family and name GINS complex, subunit Psf1 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR007257 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007257/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR007257.raw | supports | Native type family and name DNA replication complex GINS protein Psf2 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR010492 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010492/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR010492.raw | supports | Native type family and name GINS complex, subunit Psf3 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-ipr-IPR003874 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003874/; Native accession/type/name/integrated signatures and exact reviewed-protein xrefs; broad/obsolete historical explanatory prose not used to support modern mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR003874.raw | supports | Native type family and name CDC45 independently checked against same-class UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup or mechanistic prose substituted for the class. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Fresh same-PR complete official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/catalogue.raw | context_only | All20 current organism rows/28 organism-dataset pairs independently read. No Saccharomyces/eukaryotic matched natural host; bacterial expression hosts and unrelated archaeal taxa are not proxies. |
| plaque-catalogue-search | https://imodulondb.org/api/datasets; Fresh same-PR complete official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/catalogue.raw | context_only | No covered yeast dataset in this bounded official catalogue. This is coverage limitation, not biological absence, and no foreign-host downstream module query was made. |
| plaque-historical-adapter-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Original historical runner receipt only | context_only | Historical Nov3 00:49Z exit1 PermissionError reading pyvenv.cfg; no fresh runner invocation claimed. Current source fallback is independently evidenced. |
| plaque-original-current-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/originals-current-proof.json; Three original validate/render pairs;42 historical input occurrences;47 current source/worktree input hashes | supports | Original YAML validation and deterministic Markdown match; historical inputs hash against original source, including canonical CLAUDE symlink. RFA/pre-IC stale deltas are independently assessed, RFC unchanged. |
| plaque-historical-micro51-wold1997-publisher | reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml; Original evidence#micro51-wold1997-publisher; historical URL https://doi.org/10.1146/annurev.biochem.66.1.61; historical responseSHA 4b1b1d39c74c3569e6ff00ffd6acd584d2cfd08cd32629ce3d45b6f10af463d9 | context_only | Historical recorded observation: The retained publisher request returned HTTP403 challenge content, not a review main body. Original kind database/context_only is access-log misclassification; correct to validation/context_only in successor. Original response bytes are not newly certified by rereading YAML. |
| plaque-historical-micro51-kim2003-publisher | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml; Original evidence#micro51-kim2003-publisher; historical URL https://doi.org/10.1016/j.cub.2003.10.048; historical responseSHA 35892ac737a1148299b5602719dc71f7b24628eca283b1e019befde45d6f5911 | context_only | Historical recorded observation: HTTP200 contains a LinkingHub Redirecting locator page, not the article body. Original kind database/context_only is access-log misclassification; correct to validation/context_only in successor. Original response bytes are not newly certified by rereading YAML. |
| plaque-historical-micro51-kitabayashi2003-publisher | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml; Original evidence#micro51-kitabayashi2003-publisher; historical URL https://doi.org/10.1271/bbb.67.2373; historical responseSHA f5174970bceb22789d2ba517951ddb719092eedd77cb453303ff8c74c6592e73 | context_only | Historical recorded observation: HTTP403 challenge response does not supply the article main body. Original kind database/context_only is access-log misclassification; correct to validation/context_only in successor. Original response bytes are not newly certified by rereading YAML. |
| plaque-historical-micro51-cullmann1995-pdf | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml; Original evidence#micro51-cullmann1995-pdf; historical URL https://www.ncbi.nlm.nih.gov/pmc/articles/PMC230709/pdf/154661.pdf; historical responseSHA cf16e9fdeee914a3db18be8e6daebbba224fbb62b67af4b24cf2e553b6c2c46b | context_only | Historical recorded observation: HTTP200 contains Preparing to download proof-of-work HTML, not PDF pages; the separately captured CSHL PDF is the genuine body. Original kind database/context_only is access-log misclassification; correct to validation/context_only in successor. Original response bytes are not newly certified by rereading YAML. |
| plaque-historical-micro51-gary1995-pdf | reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml; Original evidence#micro51-gary1995-pdf; historical URL https://www.ncbi.nlm.nih.gov/pmc/articles/PMC307503/pdf/nar00024-0060.pdf; historical responseSHA 9831ae1d0a9d6412e90a59379b4c358a0c6fcc28dd4e260c0798239cb76604d9 | context_only | Historical recorded observation: HTTP200 contains Preparing to download proof-of-work HTML, not PDF pages; original page scans provide the actually inspected body. Original kind database/context_only is access-log misclassification; correct to validation/context_only in successor. Original response bytes are not newly certified by rereading YAML. |
| plaque-native-dna_replication_factor_a_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dna_replication_factor_a_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual source-bound exit0. Direct current inventory 3 reviewed examples/3 typed nodes; all COVERED. This verifies identity/coverage, not class grounding, mechanism or formation necessity. |
| plaque-native-dna_replication_factor_a_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dna_replication_factor_a_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-causal.log SHA256 7aa8052a4e7f0766e31305e034ff3844deb0b33aa46c8859caf42dad6b98b57c | supports | Actual source-bound exit0. Direct current inventory 3 reviewed examples/3 typed nodes; all COVERED. This verifies identity/coverage, not class grounding, mechanism or formation necessity. |
| plaque-native-dna_replication_factor_c_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dna_replication_factor_c_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual source-bound exit0. Direct current inventory 5 reviewed examples/5 typed nodes; all COVERED. This verifies identity/coverage, not class grounding, mechanism or formation necessity. |
| plaque-native-dna_replication_factor_c_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dna_replication_factor_c_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-causal.log SHA256 8fe53b9e87565355d70e5600509e38c4dfda6fcd88d47a294b9dfde6859f89f1 | supports | Actual source-bound exit0. Direct current inventory 5 reviewed examples/5 typed nodes; all COVERED. This verifies identity/coverage, not class grounding, mechanism or formation necessity. |
| plaque-native-dna_replication_preinitiation_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dna_replication_preinitiation_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual source-bound exit0. Direct current inventory 5 reviewed examples/5 typed nodes; all COVERED. This verifies identity/coverage, not class grounding, mechanism or formation necessity. |
| plaque-native-dna_replication_preinitiation_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/dna_replication_preinitiation_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-causal.log SHA256 c74a99b2a3d0d028e6c80171343313ea4b2db7f9424ad9185ccfed9c2f89fba7 | supports | Actual source-bound exit0. Direct current inventory 5 reviewed examples/5 typed nodes; all COVERED. This verifies identity/coverage, not class grounding, mechanism or formation necessity. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Full-record scientific evidence and structured-source cross-checks | supports | Positive named genes, protein classes, pathways and stress responses trigger coverage assessment; expression-only exemptions are insufficient. Official source fallback may be used when the runner is unavailable. |
| septin-curation-policy | docs/CURATION.md; Components and Discussions | supports | REVIEWED_LABEL_ONLY means an exact term remains unresolved; verified exact families differ from taxon-specific examples. Essentiality concerns formation, not viability. Dated rationale/history is append-only. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component, protein example, essentiality, graph and presence contracts | supports | Protein families/classes and whole subcomplexes are legitimate distinct objects. Native GENE_OR_PROTEIN permits appropriate protein-complex scope; no enum-only or optional-example defect is manufactured. Formation necessity must retain experimental conditions. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph endpoints, causal scope and nonmechanistic boundaries | supports | Membership, localization, enzymatic function, complex formation and organism viability are distinct claims. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Actual source scope and access tiers | supports | Authority metadata, primary body/abstract, secondary review and failed access are distinct evidence scopes; uninspected images and supplements are not certified. |
| septin-review-schema | schema/record_review.yaml; ReviewEvidence and FindingReference | supports | HTTP failure is validation context. Inherited findings retain exact repository/review/finding identity and current disposition. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009340,GO%3A0009330,GO%3A0032991,GO%3A0003918,GO%3A1990102,GO%3A1990077,GO%3A1990101,GO%3A1990125,GO%3A0006270,GO%3A1990157,GO%3A1990099,GO%3A1990100,GO%3A1990084,GO%3A1990078,GO%3A1990083,GO%3A1990085,GO%3A0032297; All17 requested current IDs, labels, active statuses, definitions, synonyms, citation xrefs and relevant typed children; unrelated children not used | supports | Exact four complex classes, typed parents, DiaA/DnaA-oriC/DnaB-DnaC boundaries and function terms match. GO0009340 retains heterodimeric wording contradicted by the primary 2:2 result; the maintained definition avoids it. GO1990099 excludes primase from the pre-primosome; primosome parentage does not add DnaG to every early intermediate. |
| septin-so | https://www.ebi.ac.uk/ols4/api/ontologies/so/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0000953; Complete native SO0000953 OLS label, definition, active status and synonym | supports | SO0000953 oriC is an origin of bacterial chromosome replication, matching the two declared origin-DNA classes, rather than generic DNA material. |
| septin-ipr-IPR001957 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Full DnaA family, distinct from its broader DnaA-like parent and Hda sibling. |
| septin-retry-IPR023070 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023070/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Exact DiaA family, distinct from broader GmhA/DiaA and its phosphoheptose-isomerase sibling. |
| septin-ipr-IPR002177 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002177/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Full Dps family, with narrower gammaproteobacterial child; ferritin-like fold alone is broader. Family membership does not prove every member binds DnaA. |
| septin-retry-IPR005742 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005742/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Gram-negative ParC family is narrower than the generic bacterial ParC component. |
| septin-ipr-IPR005737 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005737/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Gram-negative ParE family is narrower than generic ParE; hierarchy separately includes Firmicutes/Mollicutes and gyrase families. |
| septin-retry-IPR050220 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050220/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Type II DNA topoisomerase family is broader than ParC. Its llm=true/checked=false description is excluded from biological support; only native identity/type/hierarchy metadata is used. |
| septin-ipr-IPR001241 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001241/; Native name/type, description provenance flags, hierarchy and signatures; no sequence analysis | supports | Broad typeIIA family spans gyrase and topoisomerase classes and is not an exact generic ParE identity. |
| septin-up-P0AFI2 | https://rest.uniprot.org/uniprotkb/P0AFI2.json; Accession, reviewed status, recommended name, gene names/loci, organism; relevant function/subunit/localization/evidence and complete InterPro xrefs | supports | Reviewed P0AFI2: DNA topoisomerase 4 subunit A; gene parC; loci b3019, JW2987; E. coli K12 taxon83333. Family annotations and experimental citation provenance inspected. Identity/localization annotations alone do not establish membership in a DnaA-containing complex.  |
| septin-query-parC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact-organism reviewed gene response | supports | One returned reviewed entry, P0AFI2, supports the specific current single-entry identity claim; descendants or other organism IDs are not conflated. |
| septin-up-P20083 | https://rest.uniprot.org/uniprotkb/P20083.json; Accession, reviewed status, recommended name, gene names/loci, organism; relevant function/subunit/localization/evidence and complete InterPro xrefs | supports | Reviewed P20083: DNA topoisomerase 4 subunit B; gene parE; loci b3030, JW2998; E. coli K12 taxon83333. Family annotations and experimental citation provenance inspected. Identity/localization annotations alone do not establish membership in a DnaA-containing complex.  |
| septin-query-parE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparE%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact-organism reviewed gene response | supports | One returned reviewed entry, P20083, supports the specific current single-entry identity claim; descendants or other organism IDs are not conflated. |
| septin-up-P66817 | https://rest.uniprot.org/uniprotkb/P66817.json; Accession, reviewed status, recommended name, gene names/loci, organism; relevant function/subunit/localization/evidence and complete InterPro xrefs | supports | Reviewed P66817: DnaA initiator-associating protein DiaA; gene diaA; loci b3149, JW3118; E. coli K12 taxon83333. Family annotations and experimental citation provenance inspected. Identity/localization annotations alone do not establish membership in a DnaA-containing complex.  |
| septin-query-diaA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdiaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact-organism reviewed gene response | supports | One returned reviewed entry, P66817, supports the specific current single-entry identity claim; descendants or other organism IDs are not conflated. |
| septin-up-P03004 | https://rest.uniprot.org/uniprotkb/P03004.json; Accession, reviewed status, recommended name, gene names/loci, organism; relevant function/subunit/localization/evidence and complete InterPro xrefs | supports | Reviewed P03004: Chromosomal replication initiator protein DnaA; gene dnaA; loci b3702, JW3679; E. coli K12 taxon83333. Family annotations and experimental citation provenance inspected. Identity/localization annotations alone do not establish membership in a DnaA-containing complex. P03004 location citations retain BL21(DE3) annotation context and Schenk mixed E.coli/B.subtilis experimental scope. |
| septin-query-dnaA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact-organism reviewed gene response | supports | One returned reviewed entry, P03004, supports the specific current single-entry identity claim; descendants or other organism IDs are not conflated. |
| septin-up-P0ABT2 | https://rest.uniprot.org/uniprotkb/P0ABT2.json; Accession, reviewed status, recommended name, gene names/loci, organism; relevant function/subunit/localization/evidence and complete InterPro xrefs | supports | Reviewed P0ABT2: DNA protection during starvation protein; gene dps; loci b0812, JW0797; E. coli K12 taxon83333. Family annotations and experimental citation provenance inspected. Identity/localization annotations alone do not establish membership in a DnaA-containing complex.  |
| septin-query-dps | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact-organism reviewed gene response | supports | One returned reviewed entry, P0ABT2, supports the specific current single-entry identity claim; descendants or other organism IDs are not conflated. |
| septin-up-dnaB-context | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaB%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&amp;format=json&amp;size=500; Complete exact gene response; native identity/locus/status for named loading-subcomplex context only | supports | P0ACB0 dnaB b4052,JW4012 is reviewed E.coli K12. Not an added maintained protein example or mandatory inventory finding. |
| septin-up-dnaC-context | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaC%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&amp;format=json&amp;size=500; Complete exact gene response; native identity/locus/status for named loading-subcomplex context only | supports | P0AEF0 dnaC b4361,JW4325 is reviewed E.coli K12. Not an added maintained protein example or mandatory inventory finding. |
| septin-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete ENA native response | supports | Taxon562 is Escherichia coli species. Reference-strain annotations do not silently identify every experimental expression strain or mutant. |
| septin-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete ENA native response | supports | Taxon83333 is Escherichia coli K-12 strain. Reference-strain annotations do not silently identify every experimental expression strain or mutant. |
| septin-pmid-8227000 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8227000%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 8227000, Escherichia coli topoisomerase IV. Purification, characterization, subunit structure, and subunit interactions. DOI 10.1016/s0021-9258(20)80551-1. Complete abstract read; primary-paper abstract, not a claim of complete body access. |
| septin-pmid-7783632 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7783632%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 7783632, The twisted 'life' of DNA in the cell: bacterial topoisomerases. DOI 10.1111/j.1365-2958.1995.tb02369.x. Complete abstract read; secondary review abstract, not a direct assembly experiment. |
| septin-pmid-15326179 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15326179%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 15326179, DiaA, a novel DnaA-binding protein, ensures the timely initiation of Escherichia coli chromosome replication. DOI 10.1074/jbc.m402762200. Complete abstract read; primary-paper abstract, not a claim of complete body access. Earlier dimer result is retained alongside later DiaA tetramer/equilibrium evidence. |
| septin-pmid-17699754 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:17699754%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 17699754, The interaction of DiaA and DnaA regulates the replication cycle in E. coli by directly promoting ATP DnaA-specific initiation complexes. DOI 10.1101/gad.1561207. Complete abstract read; primary-paper abstract, not a claim of complete body access. |
| septin-pmid-20129058 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20129058%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 20129058, Primase directs the release of DnaC from DnaB. DOI 10.1016/j.molcel.2009.12.031. Complete abstract read; primary-paper abstract, not a claim of complete body access. |
| septin-pmid-18284581 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18284581%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 18284581, Escherichia coli Dps interacts with DnaA protein to impede initiation: a model of adaptive mutation. DOI 10.1111/j.1365-2958.2008.06127.x. Complete abstract read; primary-paper abstract, not a claim of complete body access. |
| septin-pmid-22574163 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22574163%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 22574163, Association of the chromosome replication initiator DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding. DOI 10.1371/journal.pone.0036441. Complete abstract read; primary-paper abstract, not a claim of complete body access. |
| septin-pmid-28166228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:28166228%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 28166228, Rapid turnover of DnaA at replication origin regions contributes to initiation control of DNA replication. DOI 10.1371/journal.pgen.1006561. Complete abstract read; primary-paper abstract, not a claim of complete body access. Explicitly includes B.subtilis FRAP and E.coli single-molecule observations; the bacterial systems are not collapsed. |
| septin-pmid-9478970 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9478970%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native title/authors/year/DOI and full abstractText | supports | Exact PMID 9478970, Membrane-mediated release of nucleotide from an initiator of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a distinct region of the protein into the lipid bilayer. DOI 10.1074/jbc.273.9.5167. Complete abstract read; primary-paper abstract, not a claim of complete body access. Artificial-bilayer insertion and nucleotide release are not direct membership evidence for the three complexes. |
| septin-makowska-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2819048.1/PMC2819048.1.xml; Genuine PMC2819048.1 JATS: Results S8–S10, Discussion S14–S16, Methods S18/S20/S21; no supplement, figure pixels or uninspected raw data | supports | S8 directly compares oriC plasmid with M13ΔE101: retained DnaB requires oriC under the isolated prepriming assay. S20 supplies DnaA/DnaB/DnaC,HU,SSB and incubation/gel-filtration conditions. Loading-competent DnaC mutants can remain replication-defective; primase-dependent release is subsequent. Stoichiometry is conditional. S18 names K12 strains but refers exact constructs to unread TableS1. |
| septin-keyamura-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC1948862/; Current indexed primary article excerpts; displayed lines240–352 plus previously read lines156–277 in web-third.json; Results and captions, Discussion opening. No Methods/supplements/pixels | supports | DiaA tetramer and multiple-DnaA interaction support its defined origin assembly. Tetramer-copy number differs from tetramers per whole oriC assembly. Mutations separate stimulation from unconditional necessity; source strains/constructs shown in captions are not assumed identical to dataset strains. Timestamp is current retained-reader inspection; underlying crawl instant is not independently exposed. |
| septin-keyamura-primary-early | https://pmc.ncbi.nlm.nih.gov/articles/PMC1948862/; Displayed primary lines156–277, including crystal/tetramer, mutant assays and pull-down captions; no pixels | supports | Actual current reader supplies Results text, including primary tetramer architecture and association assays. Exact sections are primary indexed text despite terminal challenge/500/404 routes; no complete downloaded body claim. Timestamp is current retained-reader inspection; underlying crawl instant is not independently exposed. |
| septin-chodavarapu-primary | https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2008.06127.x; Current displayed primary lines157–271, with initial109–196 retained in web-first.json; Results/captions and Discussion opening, no complete Methods/pixels | supports | Specific binding and origin-opening inhibition are supported. Inhibition depends on assay magnesium; induction experiments avoid H2O2 pleiotropy, so oxidative-stress checkpoint remains a model. W3110,MC1061,ZK2471 and synchronized dnaC2 experiments are distinct preparations; dataset coverage is not experimental equivalence. Timestamp is current retained-reader inspection; underlying crawl instant is not independently exposed. |
| septin-chodavarapu-primary-binding | https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2008.06127.x; Displayed primary lines109–196; affinity/ELISA and N-terminal interaction assays, no pixels | supports | Dps-DnaA binding was tested independently from cellular expression context. Conditional origin inhibition supports the coarse function; no absolute block or universal viability requirement is inferred. Timestamp is current retained-reader inspection; underlying crawl instant is not independently exposed. |
| septin-peng-primary | https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions; Displayed genuine article front matter/abstract/opening lines0–575; no complete PDF or pixels | supports | ParC2ParE2 activity and terminal-truncation association result corroborate the correct complex identity. The abstract specifies T7 expression preparations, not every native K12 strain. Timestamp is current retained-reader inspection; underlying crawl instant is not independently exposed. |
| septin-peng-primary-context | https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions; Displayed article Results lines2700–2912 and late Discussion4859–4992; no intervening unshown body or pixels | supports | Primary text separates ATP/dATP-supported activity from assembly without ATP or DNA. The maintained coarse graph does not assert ATP is needed for heterotetramer formation. Timestamp is current retained-reader inspection; underlying crawl instant is not independently exposed. |
| septin-makowska-legacy | https://pmc.ncbi.nlm.nih.gov/articles/instance/2819048/; Actual current response body/error; 200 | context_only | HTTP200 browser challenge rather than article content. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-makowska-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2819048/fullTextXML; Actual current response body/error; 500 | context_only | HTTP500 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-keyamura-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1948862/fullTextXML; Actual current response body/error; 500 | context_only | HTTP500 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-keyamura-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC1948862.1/PMC1948862.1.xml; Actual current response body/error; 404 | context_only | HTTP404 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-chodavarapu-publisher | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06127.x; Actual current response body/error; 403 | context_only | HTTP403 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-peng-publisher | https://www.jbc.org/article/S0021-9258(20)80551-1/pdf; Actual current response body/error; 403 | context_only | HTTP403 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-ishida-publisher | https://www.jbc.org/article/S0021925820724841/pdf; Actual current response body/error; 403 | context_only | HTTP403 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-ipr-IPR023070 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023070/; Actual current response body/error; 429 | context_only | HTTP429 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-ipr-IPR005742 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005742/; Actual current response body/error; 429 | context_only | HTTP429 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-ipr-IPR050220 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050220/; Actual current response body/error; 429 | context_only | HTTP429 did not supply the requested scientific body/authority object. Successful alternate routes are independently scoped; failure is not biological refutation or global unavailability. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete fresh20-organism catalogue and all keys, independently read from peer packet | supports | E.coli has five advertised datasets; precise1k is selected for a bounded matched reference-strain context. Other bacterial catalogue organisms do not establish the universal distribution of generic TopoIV. |
| septin-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete exact organism/dataset metadata | supports | precise1k covers BW25113,DGF-298,GMOS,MG1655,W3110, with201 modules/1035samples. This is relevant E.coli reference context, not claimed coverage of BL21(DE3),NA141,MC1061 or every recombinant/mutant preparation. |
| septin-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 module identity/regulator/category rows; actual finite search, not full activity inspection | supports | Exact OxyR3 and RpoS51 annotations provide bounded stress-response context; complete catalogue is not an assembly or localization experiment. |
| septin-modulegene-parC | https://imodulondb.org/api/genes/e_coli/precise1k/b3019; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b3019 maps parC to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-parC | https://imodulondb.org/api/genes/e_coli/precise1k/b3019/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: none. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-modulegene-parE | https://imodulondb.org/api/genes/e_coli/precise1k/b3030; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b3030 maps parE to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-parE | https://imodulondb.org/api/genes/e_coli/precise1k/b3030/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: none. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-modulegene-dnaA | https://imodulondb.org/api/genes/e_coli/precise1k/b3702; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b3702 maps dnaA to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-dnaA | https://imodulondb.org/api/genes/e_coli/precise1k/b3702/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: none. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-modulegene-diaA | https://imodulondb.org/api/genes/e_coli/precise1k/b3149; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b3149 maps diaA to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-diaA | https://imodulondb.org/api/genes/e_coli/precise1k/b3149/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: none. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-modulegene-dps | https://imodulondb.org/api/genes/e_coli/precise1k/b0812; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b0812 maps dps to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-dps | https://imodulondb.org/api/genes/e_coli/precise1k/b0812/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: 3 OxyR, 51 RpoS. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-modulegene-dnaB | https://imodulondb.org/api/genes/e_coli/precise1k/b4052; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b4052 maps dnaB to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-dnaB | https://imodulondb.org/api/genes/e_coli/precise1k/b4052/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: none. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-modulegene-dnaC | https://imodulondb.org/api/genes/e_coli/precise1k/b4361; Exact gene_id/name/product/UniProt and locus response | supports | Covered e_coli/precise1k/b4361 maps dnaC to independently verified native identity. Imported function prose is annotation context, not a direct experimental statement. |
| septin-modulemembers-dnaC | https://imodulondb.org/api/genes/e_coli/precise1k/b4361/imodulons; All201 weight/threshold/is_in_imodulon rows for one exact locus | supports | Thresholded hits: none. These are computational expression memberships; false flags do not mean absent expression, absent gene, no regulation or no structural role. |
| septin-module-3 | https://imodulondb.org/api/imodulons/e_coli/precise1k/3; Native module identity/regulator/threshold/member fields only; ai_summary excluded; activity vectors not biologically interpreted | supports | OxyR3/RpoS51 native metadata corroborates the dps thresholded hit. Explicit generated prose is not scientific evidence; module assignment does not prove direct DnaA binding, localization or complex formation. |
| septin-module-3-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/3/genes; Complete member identities/threshold and exact dps b0812 row | supports | dps is a thresholded member of OxyR3 among38 members. This bounded expression context is consistent with a stress narrative but does not independently establish the oxidative checkpoint model. |
| septin-module-51 | https://imodulondb.org/api/imodulons/e_coli/precise1k/51; Native module identity/regulator/threshold/member fields only; ai_summary excluded; activity vectors not biologically interpreted | supports | OxyR3/RpoS51 native metadata corroborates the dps thresholded hit. Explicit generated prose is not scientific evidence; module assignment does not prove direct DnaA binding, localization or complex formation. |
| septin-module-51-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/51/genes; Complete member identities/threshold and exact dps b0812 row | supports | dps is a thresholded member of RpoS51 among122 members. This bounded expression context is consistent with a stress narrative but does not independently establish the oxidative checkpoint model. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Prior actual Nov3 00:49Z command receipt | context_only | Historical invocation exited1 with PermissionError reading pyvenv.cfg. No fresh invocation or runner success claimed; current official source fallback is separate. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-septin/original-checks.json; Actual four validate/render runs and all52 historical input occurrences | supports | All four original pairs validate0/render0 and Markdown is byte-identical; all13 historical inputs each match retained revision, and current targets are nonstale. Historical batch26 execution cohort is accurate reused provenance, not a current-head gate. |
| septin-record-dna_topoisomerase_iv_complex | data/structures/other/dna_topoisomerase_iv_complex.yaml; Entire frozen current record including all examples/evidence/graphs/discussions/history | context_only | Complete nonstale maintained record independently assessed. Historical rationale is provenance, not automatically a current scientific claim. |
| septin-original-dna_topoisomerase_iv_complex | reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml; Complete original YAML and deterministic Markdown; original verdict/findings/actions/check scope | context_only | Exact inherited lineage and limits assessed independently; old global runs remain scoped to their actual historical batch26 execution and source. |
| septin-native-dna_topoisomerase_iv_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-verify-receipt.json receiptSHA256 bddf353955ba8e79976193a4f1c1818bcf6a83a2f2bf88e9fa6932e8f2c53d51; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-native-dna_topoisomerase_iv_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-causal-receipt.json receiptSHA256 ba3ac6ef01f0ec2647bf9306cdaa64d510a2ca609a6f8952ca3dfb976f98e89c; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-historical-failure-dna_topoisomerase_iv_complex | reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml#replication51-agent-peng1993-publisher; Historical original403 row, not recovered original response bytes | context_only | Original database-typed row correctly says HTTP403/context_only/no body; only its evidence kind requires correction. Original snapshot 9fc7ab8d1025f66a87cf5348de1b52b4aee5c751864a6c6c6f0a3115140b4713 and timestamp retained. |
| septin-record-dnaa_diaa_complex | data/structures/other/dnaa_diaa_complex.yaml; Entire frozen current record including all examples/evidence/graphs/discussions/history | context_only | Complete nonstale maintained record independently assessed. Historical rationale is provenance, not automatically a current scientific claim. |
| septin-original-dnaa_diaa_complex | reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml; Complete original YAML and deterministic Markdown; original verdict/findings/actions/check scope | context_only | Exact inherited lineage and limits assessed independently; old global runs remain scoped to their actual historical batch26 execution and source. |
| septin-native-dnaa_diaa_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_diaa_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-verify-receipt.json receiptSHA256 1e38b4905c5721a24c30b3435b33425e9ef8bdbfa41239e2de5fd0053ec880f0; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-native-dnaa_diaa_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_diaa_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-causal-receipt.json receiptSHA256 51bea0370996928bd58bea9ca8876e9782a55521a47af153830c568cef751fa2; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-historical-failure-dnaa_diaa_complex | reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml#replication51-agent-ishida2004-publisher; Historical original403 row, not recovered original response bytes | context_only | Original database-typed row correctly says HTTP403/context_only/no body; only its evidence kind requires correction. Original snapshot 28c406032a0757333faddce6d77ef0b153fb5b2b9012be60e5abf4d653eef711 and timestamp retained. |
| septin-record-dnaa_dnab_dnac_complex | data/structures/other/dnaa_dnab_dnac_complex.yaml; Entire frozen current record including all examples/evidence/graphs/discussions/history | context_only | Complete nonstale maintained record independently assessed. Historical rationale is provenance, not automatically a current scientific claim. |
| septin-original-dnaa_dnab_dnac_complex | reviews/structured/20261022T055925Z-dnaa-dnab-dnac-complex-audit/review.yaml; Complete original YAML and deterministic Markdown; original verdict/findings/actions/check scope | context_only | Exact inherited lineage and limits assessed independently; old global runs remain scoped to their actual historical batch26 execution and source. |
| septin-native-dnaa_dnab_dnac_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dnab_dnac_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-verify-receipt.json receiptSHA256 1138a974cedd0c0503906557b48672e50de4893902f85c928a77e4e14c026c9b; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-native-dnaa_dnab_dnac_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dnab_dnac_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-causal-receipt.json receiptSHA256 6a74b5819b490b2454731f265e33e3cc62c8670bc3cca033b1fabd7f083d0556; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-record-dnaa_dps_complex | data/structures/other/dnaa_dps_complex.yaml; Entire frozen current record including all examples/evidence/graphs/discussions/history | context_only | Complete nonstale maintained record independently assessed. Historical rationale is provenance, not automatically a current scientific claim. |
| septin-original-dnaa_dps_complex | reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml; Complete original YAML and deterministic Markdown; original verdict/findings/actions/check scope | context_only | Exact inherited lineage and limits assessed independently; old global runs remain scoped to their actual historical batch26 execution and source. |
| septin-native-dnaa_dps_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-verify-receipt.json receiptSHA256 a7eb006eb0008f9277481326c8d11855c8018b18a9f6cbcbc0154b17da3d24a7; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-native-dnaa_dps_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-causal-receipt.json receiptSHA256 514021ec09992e73d93759d7bce7dd350cd7b613f87361ab8a3cac3b9bb40c99; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage syntax, not independent experimental membership or assembly necessity. |
| septin-historical-failure-dnaa_dps_complex | reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml#replication51-agent-chodavarapu2008-publisher; Historical original403 row, not recovered original response bytes | context_only | Original database-typed row correctly says HTTP403/context_only/no body; only its evidence kind requires correction. Original snapshot 642d8d8f811c382ca3b937b715e0110c74ae36df8f9e4156873923a1e910e850 and timestamp retained. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2388 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-dna_polymerase_iii_clamp_loader_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_clamp_loader_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_core_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_polymerase_iii_core_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_replication_factor_a_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_replication_factor_a_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_replication_factor_c_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_replication_factor_c_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_replication_preinitiation_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_replication_preinitiation_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_topoisomerase_iv_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dna_topoisomerase_iv_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_diaa_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_diaa_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_dnab_dnac_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_dnab_dnac_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_dps_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_dps_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Pol III clamp loader, holoenzyme and core independent review: This slice judges only PolIII clamp loader, whole complex and core. All three frozen target hashes are unchanged; other seven targets and neighboring/group/category issues are not disposed. No repository/Git/GitHub mutation.
- Pol III clamp loader, holoenzyme and core independent review: Jeruzalmi2001 genuine primary PDF read at pp429–431 and439–440 Summary/Introduction/structural Results/Conclusion/Methods plus Fig1 text caption only. No figure pixels, coordinates, supplements, raw kinetics or full-paper certification. Truncated gamma1–373 pentamer/reconstitution is distinct from full heptamer/native cell and speculative transitions.
- Pol III clamp loader, holoenzyme and core independent review: McHenry2003 is a secondary-review PDF read pp1157–1159, opening p1160 and Fig1 text caption, not the complete review. Its mixed in-vivo model and additional tau coupling are distinct from any-mixture isolated loading; no invariant in-vivo ratio or complete body read is claimed.
- Pol III clamp loader, holoenzyme and core independent review: Maki/Kornberg1988 is complete primary-abstract and publisher-metadata only. Fresh HTML/PDF403 and metadata-only API leave exact experimental strains, methods, figures and physical-formation assays unverified, not disproved.
- Pol III clamp loader, holoenzyme and core independent review: GO0043846 andGO0044776 current nuclear ancestry/Eukaryota-only constraints conflict with their bacterial source evidence; neither is a maintained target assertion. The core DNA-polymerase parent is activity-supported, not claimed as a direct native GO is-a edge.
- Pol III clamp loader, holoenzyme and core independent review: Native reviewed UniProt identities, current singleton queries and InterPro metadata do not certify every annotation-linked experiment. HolA generated proofreading prose and broad generated IPR050238 text are excluded from biological support; exact families are distinguished from domains/broad or taxon-limited classes.
- Pol III clamp loader, holoenzyme and core independent review: Current precise1k comprises five K12-related strains, not an identified exact Jeruzalmi/Maki assay strain. Nine exact loci each have201 checked module rows; only holD145 andholE147 cross thresholds, corroborated by70- and43-gene module lists. Nonhits are not absence; hits/names are not assembly, localization, direct regulation or formation. Generated AI summaries and activity contrasts not used.
- Pol III clamp loader, holoenzyme and core independent review: Historical adapter runner unavailability is the actual2026-11-03T00:49Z failure, not a fresh invocation. Current manual official API fallback is separate. Six source-head native protein commands pass with8examples/8COVERED typednodes; the whole-complex0/0 outcome does not assess STRUCTURE nodes, checked separately.
- Pol III clamp loader, holoenzyme and core independent review: Three inherited minor findings remain open with exact predecessor identities and bounded future curation actions. Historical rationale/history remain append-only. No optional examples, new experiments, forced domain-to-family mapping or universal essentiality classification are required.
- Pol III clamp loader, holoenzyme and core independent review: Root owns global QC and later saved-head/CI/queue gates. These future stages are not certified by this source report. Original failure-kind corrections retain exact historical timestamps/hashes and never invent body access.
- RPA, RFC and replication preinitiation independent review: Wold1997 and Kim2003 are secondary complete abstract/metadata tiers, not newly inspected review bodies. Wold publisher403 and Brill primary PDF403 are retained access limitations; Brill complete primary abstract independently supports yeast three-gene composition, not exact S288C experimental strain.
- RPA, RFC and replication preinitiation independent review: Takayama genuine fresh primary HTML Results sec2–9/Discussion11–13/Methods15–22 and text captions were read; no figure pixels, raw data or Supplementary Table1. No W303/S288C strain equivalence is invented. Modern mechanistic details require their own appropriate source; ontology/family prose does not substitute.
- RPA, RFC and replication preinitiation independent review: Cullmann genuine author-repository PDF text pp4661–4663/4665/4668–4669 and selected text captions were read. No alignment image or figure-pixel analysis. Gary/Hopwood remain complete primary abstracts on correct legacy PMC surfaces; scan links are not body review. Kitabayashi/Nishida are full primary abstracts only, with their exact archaeal hosts preserved.
- RPA, RFC and replication preinitiation independent review: Initial mistaken PMC26461 Hopwood lead was rejected after title inspection; unrelated GPCR content is excluded. Correct PMC37987 identity/abstract subsequently verified. Two initial InterPro429 responses are retained separately from successful retries; no negative-family inference.
- RPA, RFC and replication preinitiation independent review: Current13 reviewed S288C examples/13 typed nodes allCOVERED independently checked; reference identities/localization do not prove every claimed mechanism/formation requirement. No optional example inventory, forced RFC2–5 exact families or protein-complex enum finding.
- RPA, RFC and replication preinitiation independent review: Fresh complete official catalogue lacks matched natural yeast/eukaryotic hosts. No unrelated E.coli or archaeal dataset proxy, no module-query run or biological absence inferred. Historical Nov3 00:49Z runner failure is not a fresh invocation; current source fallback is separately evidenced.
- RPA, RFC and replication preinitiation independent review: Three original pairs/42 historical input occurrences and47 current inputs verified. RFA/pre-IC stale deltas substantively refreshed and RFC unchanged; original files immutable. Root owns corpus QC/final saved-head/CI/queue/merge gates, none precertified by source review.
- RPA, RFC and replication preinitiation independent review: Six inherited scientific findings remain open: one major/five minor. Added examples and prior2470 RFA evidence repair do not resolve exact-family F1; no terminal grouped/category issue resolution inferred. Five access-kind occurrences and three prose applicability exclusions are bundle-only corrections.
- Topoisomerase IV and DnaA complexes independent review: Four nonstale targets; four inherited minor scientific findings remain (three exact-grounding findings plus one condition-scoped origin-formation finding). TopoIV retains a qualified positive pass; no new scientific finding.
- Topoisomerase IV and DnaA complexes independent review: Makowska2010 genuine fresh JATS was read only at named Results/Discussion/Methods sections. The empty-vector result is reported text, not independently reanalyzed pixels or raw data. Exact plasmid/strain details delegated to unread TableS1 are not certified. Keyamura2007,Chodavarapu2008 and Peng1993 are current indexed primary excerpts with exact displayed extents; terminal failures remain separate. No complete downloaded bodies for those three, no figure pixels,supplements or deposited-coordinate analysis.
- Topoisomerase IV and DnaA complexes independent review: Ishida2004 and DnaA localization papers were read at complete native abstract/metadata plus relevant UniProt annotation tier. Luttinger1995 is a secondary-review abstract. Schenk includes both B.subtilis and E.coli; native reference strain is not synonymous with every experimental preparation. Earlier DiaA dimer and later tetramer/equilibrium evidence are preserved.
- Topoisomerase IV and DnaA complexes independent review: GO0009340 heterodimer language conflicts with inspected 2:2 evidence; current maintained definition avoids it. IPR050220 LLM-generated unchecked prose and iModulon ai_summary prose are excluded from biological evidence. Family/type/hierarchy metadata remain distinct from primary experiments.
- Topoisomerase IV and DnaA complexes independent review: All four original formal expression-only exclusions require correction. Fresh complete official catalogue and precise1k metadata support E.coli context; seven exact loci were checked across201 module memberships. dps has OxyR3/RpoS51 hits; six others below threshold do not establish absent expression/regulation/structure. Generated module prose,uninspected activities and nonmatching experimental strains are not promoted to direct mechanistic evidence. Historical runner failure remains Nov3 00:49Z, with no fresh invocation.
- Topoisomerase IV and DnaA complexes independent review: Own native inventory has7 reviewed example occurrences (5 distinct accessions) and7 typed nodes, all COVERED; eight actual native command successes do not establish direct membership,necessity or localization. Four original pairs validate/render exactly with52 historical input occurrences verified. Historical batch26 execution provenance is retained accurately.
- Topoisomerase IV and DnaA complexes independent review: Three original HTTP403 context_only evidence rows need only database→validation reclassification; their historical timestamps,explicit no-body statements and original bytes are preserved. Current500/404/429/challenge responses are truthful access context; alternate successes are separately scoped.
- Topoisomerase IV and DnaA complexes independent review: Only29 listed frozen maintained inputs used; no additional local record or prior-review context. Bounded ignored-inclusive scratch filename search located a prior Keyamura reader but no prior scientific bundle was used as biological authority; fresh current sources suffice. Search failures/unrelated hits are not negative biological evidence. Root global gates,successor validation,final CI,queue and merge remain separate attestations.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- This ten-record successor preserves all 20 original artifacts and exact predecessor finding lineage. Bundle issues #2920, #2921 and #2922 cover two stale targets, seven formal plus three prose applicability assessments, and twelve access-only evidence-kind occurrences.
- RPA adds three budding-yeast examples and source-specific component/graph citations. Preinitiation adds the CDC45 Q08032 example. These changes require substantive source reassessment separately from the inherited findings.
- The current native inventory has 28 component protein examples and 28 typed GENE_OR_PROTEIN nodes, all classified COVERED in the actual native logs. The Pol III holoenzyme remains a deliberately grounded subcomplex-level record with zero protein examples and zero typed protein nodes; this is not a required-inventory defect.
- Historical failed publisher responses already disclose failed access and context_only support. The successor uses validation for those access observations and preserves actual timestamps and hashes; successful current source scopes remain distinct.
- Record curation stays in separate issues. Preserve dated rationale/history and append supported clarification; no scientific record is edited. Final post-save validation, saved-head independent acceptance, final-head CI and merge-group CI are later gates.
- The RPA refresh supports current RFA1/2/3 reference identities and three-gene composition at native-entry and primary-abstract scope, while Wold full-body and exact experimental-strain limits remain explicit. The preinitiation refresh supports the new CDC45 Q08032 identity and nucleus annotation via the current native reference and Hopwood abstract; the four pre-existing source, grounding, formation and graph findings remain open.
- DnaX composition is a bounded generic-heptamer versus tau-dependent holoenzyme distinction; it does not replace the full heptamer with the truncated crystal pentamer or mandate a tau:gamma ratio. The DnaA-DnaB-DnaC origin-DNA finding is explicitly limited to the isolated-complex assay, not universal viability or in-vivo essentiality.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T063523Z-pr2388-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2388: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T06:14:47.131005Z'
finished_at: '2026-11-04T06:35:23Z'
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
summary: Independent current-input review of ten DNA replication and initiation complexes
  preserves all twenty original artifacts and refreshes the two stale RPA and preinitiation
  records. Thirteen inherited scientific findings remain open (one major and twelve
  minor) across eight records; the Pol III holoenzyme and topoisomerase IV retain
  qualified positive verdicts. The successor corrects seven formal and three prose
  structured-source applicability assessments and twelve access-only evidence-kind
  occurrences. The 28 current protein examples and 28 typed protein nodes all pass
  actual native coverage checks. Records remain unchanged; separately linked record-curation
  issues retain exact predecessor lineage and bounded source scopes.
source:
  git_revision: 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
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
  - path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    sha256: d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a
    role: target
  - path: data/structures/other/dna_polymerase_iii_complex.yaml
    sha256: c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d
    role: target
  - path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    sha256: d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b
    role: target
  - path: data/structures/other/dna_replication_factor_a_complex.yaml
    sha256: 875ef33eba1336b1bfd61e3c5bc9f0ade5f2c37a93d25793797fa5b9ac34c133
    role: target
  - path: data/structures/other/dna_replication_factor_c_complex.yaml
    sha256: 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f
    role: target
  - path: data/structures/other/dna_replication_preinitiation_complex.yaml
    sha256: d38de0da7f792e34b56e5ef225160a88221fb8a9b64e309e2b28f34bc7038b88
    role: target
  - path: data/structures/other/dna_topoisomerase_iv_complex.yaml
    sha256: fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070
    role: target
  - path: data/structures/other/dnaa_diaa_complex.yaml
    sha256: fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4
    role: target
  - path: data/structures/other/dnaa_dnab_dnac_complex.yaml
    sha256: a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56
    role: target
  - path: data/structures/other/dnaa_dps_complex.yaml
    sha256: 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87
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
  - path: reviews/structured/20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit/review.md
    sha256: 3ab94ec648eadd7df1e6a0d1402fb556982b5a81940b658d3138912d5bb14f80
    role: context
  - path: reviews/structured/20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit/review.yaml
    sha256: be1948ad5ab70bdcec12e8bed2a7d82c3137fb5f68caafcd2a23d50c8b223c1f
    role: context
  - path: reviews/structured/20261022T055920Z-dna-polymerase-iii-complex-audit/review.md
    sha256: d90813b57e832f9cf6764b06b16a673fbed8294f68599112b5cf24cee053572c
    role: context
  - path: reviews/structured/20261022T055920Z-dna-polymerase-iii-complex-audit/review.yaml
    sha256: 8d6bee94d6883ee608284a00645339c60ee1f4746516dcdeb16ea14aea9317ae
    role: context
  - path: reviews/structured/20261022T055921Z-dna-polymerase-iii-core-complex-audit/review.md
    sha256: e6817d57b1fcbfe7c684f18ba29f657a97ac412092b382cf94bc14700d9e80b7
    role: context
  - path: reviews/structured/20261022T055921Z-dna-polymerase-iii-core-complex-audit/review.yaml
    sha256: 7e4cb02a04eac7dfa78f910030008db27dab2269a40d2f750b03b258928b8491
    role: context
  - path: reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.md
    sha256: 0f727e5db676f2120d360b9115d0081c405dbbdd9ceeb92d7b2bf9eb975c8626
    role: context
  - path: reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml
    sha256: 32bc2458f21adb0704d23ce69748bab13f6086cecaa7226cbd7af8d93bf3f1a2
    role: context
  - path: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.md
    sha256: 42bf5580aa7b792128642e6023dbf12944a8c59d1ba3cdec6310d4c9144ac60d
    role: context
  - path: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
    sha256: 157b78894391f59a60728857bb07e85213b854d02c8a6be3e16cb1a3bc912ecc
    role: context
  - path: reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.md
    sha256: 5b00d000e58ff9288539a656bcbfc7ba53591e1dfa410ade943d555d6bf731ab
    role: context
  - path: reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.yaml
    sha256: 77ac82339e48756ab3ecfbc24de8ea5209e698ad430f9dc6ddc2f7c0ea60b963
    role: context
  - path: reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.md
    sha256: 51e37e8ddd5193999bafd1680c4534af4d959521e19cf50659bbb2956421d269
    role: context
  - path: reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml
    sha256: b2a67f0185810b26fb35419ab15c773de0a1daf6d8a9ebf53b248380aa159dc2
    role: context
  - path: reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.md
    sha256: 4ba7af88f839ffa8769bc79de033d881ba3ac180d07b44ddcc172e1b6de7461e
    role: context
  - path: reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml
    sha256: 42d73a83ac80abf0e7081f8263e0c5cd5d25608ac689f9f4618583220dcdc62a
    role: context
  - path: reviews/structured/20261022T055925Z-dnaa-dnab-dnac-complex-audit/review.md
    sha256: 44af62ced0b11e42d3b7d0012630f611e1f4933d2c8f8c1fcb4698c59e0cb5ea
    role: context
  - path: reviews/structured/20261022T055925Z-dnaa-dnab-dnac-complex-audit/review.yaml
    sha256: b72282c71638516e097bc0d1e5e8b8eaab8d6820a207155ffba541d63c804ee0
    role: context
  - path: reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.md
    sha256: 09fceb2dae037114f3e601a15044b9092b889e025d891e1cff846fa1d293f113
    role: context
  - path: reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml
    sha256: 17a6d0ebaeb2b67c1a3c0d574e5fb72fffc7d6b4406d454dbdeff1587035cf4e
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
- target_id: GO:0043846
  path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  label: DNA polymerase III, clamp loader complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
- target_id: GO:0009360
  path: data/structures/other/dna_polymerase_iii_complex.yaml
  label: DNA polymerase III complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_complex.yaml
    role: maintained scientific record
- target_id: GO:0044776
  path: data/structures/other/dna_polymerase_iii_core_complex.yaml
  label: DNA polymerase III, core complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    role: maintained scientific record
- target_id: GO:0005662
  path: data/structures/other/dna_replication_factor_a_complex.yaml
  label: DNA replication factor A complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_a_complex.yaml
    role: maintained scientific record
- target_id: GO:0005663
  path: data/structures/other/dna_replication_factor_c_complex.yaml
  label: DNA replication factor C complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_c_complex.yaml
    role: maintained scientific record
- target_id: GO:0031261
  path: data/structures/other/dna_replication_preinitiation_complex.yaml
  label: DNA replication preinitiation complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
- target_id: GO:0009340
  path: data/structures/other/dna_topoisomerase_iv_complex.yaml
  label: DNA topoisomerase IV complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_topoisomerase_iv_complex.yaml
    role: maintained scientific record
- target_id: GO:1990102
  path: data/structures/other/dnaa_diaa_complex.yaml
  label: DnaA-DiaA complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_diaa_complex.yaml
    role: maintained scientific record
- target_id: GO:1990157
  path: data/structures/other/dnaa_dnab_dnac_complex.yaml
  label: DnaA-DnaB-DnaC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dnab_dnac_complex.yaml
    role: maintained scientific record
- target_id: GO:1990084
  path: data/structures/other/dnaa_dps_complex.yaml
  label: DnaA-Dps complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dps_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    8dff0f68c5ca75d5b6d78d6d577b9d09426eb7a3.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0043846
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just validate data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0043846
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: just validate-strict data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0009360
  status: passed
  required: true
  target_ids:
  - GO:0009360
  command: just validate data/structures/other/dna_polymerase_iii_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0009360
  status: passed
  required: true
  target_ids:
  - GO:0009360
  command: just validate-strict data/structures/other/dna_polymerase_iii_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0044776
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just validate data/structures/other/dna_polymerase_iii_core_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0044776
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: just validate-strict data/structures/other/dna_polymerase_iii_core_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0005662
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: just validate data/structures/other/dna_replication_factor_a_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0005662
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: just validate-strict data/structures/other/dna_replication_factor_a_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0005663
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: just validate data/structures/other/dna_replication_factor_c_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0005663
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: just validate-strict data/structures/other/dna_replication_factor_c_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0031261
  status: passed
  required: true
  target_ids:
  - GO:0031261
  command: just validate data/structures/other/dna_replication_preinitiation_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0031261
  status: passed
  required: true
  target_ids:
  - GO:0031261
  command: just validate-strict data/structures/other/dna_replication_preinitiation_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0009340
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: just validate data/structures/other/dna_topoisomerase_iv_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0009340
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: just validate-strict data/structures/other/dna_topoisomerase_iv_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:1990102
  status: passed
  required: true
  target_ids:
  - GO:1990102
  command: just validate data/structures/other/dnaa_diaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:1990102
  status: passed
  required: true
  target_ids:
  - GO:1990102
  command: just validate-strict data/structures/other/dnaa_diaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:1990157
  status: passed
  required: true
  target_ids:
  - GO:1990157
  command: just validate data/structures/other/dnaa_dnab_dnac_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:1990157
  status: passed
  required: true
  target_ids:
  - GO:1990157
  command: just validate-strict data/structures/other/dnaa_dnab_dnac_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:1990084
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just validate data/structures/other/dnaa_dps_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:1990084
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: just validate-strict data/structures/other/dnaa_dps_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388
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
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  summary: All ten positive molecular or replication narratives trigger structured-source
    applicability. Fresh official catalogue and metadata support bounded E.coli precise1k
    context for seven bacterial records; exact-locus/module checks retain five-strain
    scope, threshold hits and nonhit limits without inferring direct regulation, assembly
    or necessity. HolD ppGpp145, HolE PAL26Del147 and Dps OxyR3/RpoS51 contexts are
    recorded at their inspected scope. The catalogue has no matched natural yeast
    host for RPA, RFC or preinitiation; bacterial expression hosts are not proxies.
    The actual historical adapter-runner failure is preserved separately from fresh
    official-source fallback.
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b0640
  - micro-ecoli-gene-b1099
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0184
  - micro-ecoli-gene-b0215
  - micro-ecoli-gene-b1842
  - micro-ecoli-gene-b3701
  - micro-ecoli-module-145
  - micro-ecoli-module-147
  - plaque-catalogue
  - plaque-catalogue-search
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-modulegene-parC
  - septin-modulemembers-parC
  - septin-modulegene-parE
  - septin-modulemembers-parE
  - septin-modulegene-dnaA
  - septin-modulemembers-dnaA
  - septin-modulegene-diaA
  - septin-modulemembers-diaA
  - septin-modulegene-dps
  - septin-modulemembers-dps
  - septin-modulegene-dnaB
  - septin-modulemembers-dnaB
  - septin-modulegene-dnaC
  - septin-modulemembers-dnaC
  - septin-module-3
  - septin-module-3-genes
  - septin-module-51
  - septin-module-51-genes
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-graph-policy
  - micro-up-P03007
  - micro-up-P06710
  - micro-up-P0A988
  - micro-up-P0ABS8
  - micro-up-P10443
  - micro-up-P28630
  - micro-up-P28631
  - micro-up-P28632
  - micro-up-P28905
  - micro-tax-562
  - micro-tax-83333
  - micro-go-0003689
  - micro-go-0003887
  - micro-go-0006260
  - micro-go-0009360
  - micro-go-0032991
  - micro-go-0042575
  - micro-go-0043846
  - micro-go-0043847
  - micro-go-0044775
  - micro-go-0044776
  - micro-isa-0043846
  - micro-isa-0009360
  - micro-isa-0044776
  - micro-constraints-0043846
  - micro-constraints-0044776
  - micro-ipr-IPR005790
  - micro-ipr-IPR007459
  - micro-ipr-IPR004615
  - micro-ipr-IPR004622
  - micro-ipr-IPR012763-retry
  - micro-ipr-IPR009052-retry
  - micro-ipr-IPR006309-retry
  - micro-ipr-IPR006054
  - micro-ipr-IPR004805
  - micro-ipr-IPR050238
  - micro-ipr-IPR045085
  - micro-ipr-IPR048731-retry
  - micro-ipr-IPR004365
  - micro-ipr-IPR004013
  - micro-pmid-11525729
  - micro-pmid-12940977
  - micro-pmid-3283127
  - micro-jeruzalmi2001-pdf
  - micro-mchenry2003-pdf
  - micro-maki1988-api
  - micro-ecoli-meta
  - micro-ecoli-module-145
  - micro-ecoli-module-147
  - plaque-policy
  - plaque-schema
  - plaque-review-skill
  - plaque-review-profile
  - plaque-review-schema
  - plaque-checklist
  - plaque-graph-policy
  - plaque-go
  - plaque-go-0005662-ancestors
  - plaque-go-0005662-constraints
  - plaque-go-0005663-ancestors
  - plaque-go-0005663-constraints
  - plaque-go-0031261-ancestors
  - plaque-go-0031261-constraints
  - plaque-tax-2759
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-pmid-9242902
  - plaque-pmid-7651383
  - plaque-pmid-8559655
  - plaque-pmid-14614842
  - plaque-pmid-14646196
  - plaque-pmid-16172520
  - plaque-pmid-12730134
  - plaque-pmid-8901577
  - plaque-brill1991-meta
  - plaque-takayama2003-pmc
  - plaque-cullmann1995-pdf
  - plaque-gary1995-pmc
  - plaque-hopwood1996-correct-pmc
  - plaque-up-P22336
  - plaque-up-P26754
  - plaque-up-P26755
  - plaque-up-P38630
  - plaque-up-P40348
  - plaque-up-P38629
  - plaque-up-P40339
  - plaque-up-P38251
  - plaque-up-Q08032
  - plaque-up-Q03406
  - plaque-up-Q12488
  - plaque-up-P40359
  - plaque-up-Q12146
  - plaque-ipr-IPR004591
  - plaque-ipr-IPR014646
  - plaque-ipr-IPR013970
  - plaque-ipr-IPR012178
  - plaque-ipr-IPR050238
  - plaque-ipr-IPR013748
  - plaque-ipr-IPR008591-retry
  - plaque-ipr-IPR005339-retry
  - plaque-ipr-IPR007257
  - plaque-ipr-IPR010492
  - plaque-ipr-IPR003874
  - plaque-catalogue
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-go
  - septin-so
  - septin-ipr-IPR001957
  - septin-retry-IPR023070
  - septin-ipr-IPR002177
  - septin-retry-IPR005742
  - septin-ipr-IPR005737
  - septin-retry-IPR050220
  - septin-ipr-IPR001241
  - septin-up-P0AFI2
  - septin-up-P20083
  - septin-up-P66817
  - septin-up-P03004
  - septin-up-P0ABT2
  - septin-tax-562
  - septin-tax-83333
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-pmid-15326179
  - septin-pmid-17699754
  - septin-pmid-20129058
  - septin-pmid-18284581
  - septin-pmid-22574163
  - septin-pmid-28166228
  - septin-pmid-9478970
  - septin-makowska-s3
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-modulegene-parC
  - septin-modulegene-parE
  - septin-modulegene-dnaA
  - septin-modulegene-diaA
  - septin-modulegene-dps
  - septin-modulegene-dnaB
  - septin-modulegene-dnaC
  - septin-module-3
  - septin-module-3-genes
  - septin-module-51
  - septin-module-51-genes
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
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
- check_id: dna_polymerase_iii_clamp_loader_complex-uniprot-verify
  name: Native DNA polymerase III, clamp loader complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_clamp_loader_complex-uniprot-verify
- check_id: dna_polymerase_iii_clamp_loader_complex-uniprot-causal
  name: Native DNA polymerase III, clamp loader complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0043846
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_clamp_loader_complex-uniprot-causal
- check_id: dna_polymerase_iii_complex-uniprot-verify
  name: Native DNA polymerase III complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009360
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_complex.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_complex-uniprot-verify
- check_id: dna_polymerase_iii_complex-uniprot-causal
  name: Native DNA polymerase III complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009360
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_complex-uniprot-causal
- check_id: dna_polymerase_iii_core_complex-uniprot-verify
  name: Native DNA polymerase III, core complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_core_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_core_complex-uniprot-verify
- check_id: dna_polymerase_iii_core_complex-uniprot-causal
  name: Native DNA polymerase III, core complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044776
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_polymerase_iii_core_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_polymerase_iii_core_complex-uniprot-causal
- check_id: dna_replication_factor_a_complex-uniprot-verify
  name: Native DNA replication factor A complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_replication_factor_a_complex-uniprot-verify
- check_id: dna_replication_factor_a_complex-uniprot-causal
  name: Native DNA replication factor A complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005662
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_a_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_replication_factor_a_complex-uniprot-causal
- check_id: dna_replication_factor_c_complex-uniprot-verify
  name: Native DNA replication factor C complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_replication_factor_c_complex-uniprot-verify
- check_id: dna_replication_factor_c_complex-uniprot-causal
  name: Native DNA replication factor C complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005663
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_replication_factor_c_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_replication_factor_c_complex-uniprot-causal
- check_id: dna_replication_preinitiation_complex-uniprot-verify
  name: Native DNA replication preinitiation complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031261
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_replication_preinitiation_complex.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_replication_preinitiation_complex-uniprot-verify
- check_id: dna_replication_preinitiation_complex-uniprot-causal
  name: Native DNA replication preinitiation complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031261
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_replication_preinitiation_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_replication_preinitiation_complex-uniprot-causal
- check_id: dna_topoisomerase_iv_complex-uniprot-verify
  name: Native DNA topoisomerase IV complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_topoisomerase_iv_complex-uniprot-verify
- check_id: dna_topoisomerase_iv_complex-uniprot-causal
  name: Native DNA topoisomerase IV complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009340
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dna_topoisomerase_iv_complex-uniprot-causal
- check_id: dnaa_diaa_complex-uniprot-verify
  name: Native DnaA-DiaA complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990102
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_diaa_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_diaa_complex-uniprot-verify
- check_id: dnaa_diaa_complex-uniprot-causal
  name: Native DnaA-DiaA complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990102
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_diaa_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_diaa_complex-uniprot-causal
- check_id: dnaa_dnab_dnac_complex-uniprot-verify
  name: Native DnaA-DnaB-DnaC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990157
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dnab_dnac_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_dnab_dnac_complex-uniprot-verify
- check_id: dnaa_dnab_dnac_complex-uniprot-causal
  name: Native DnaA-DnaB-DnaC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990157
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dnab_dnac_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_dnab_dnac_complex-uniprot-causal
- check_id: dnaa_dps_complex-uniprot-verify
  name: Native DnaA-Dps complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_dps_complex-uniprot-verify
- check_id: dnaa_dps_complex-uniprot-causal
  name: Native DnaA-Dps complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990084
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_dps_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a;
    current SHA256 d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a.
    Record bytes unchanged since the original review.
  snapshot_sha256: d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: be1948ad5ab70bdcec12e8bed2a7d82c3137fb5f68caafcd2a23d50c8b223c1f
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d;
    current SHA256 c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d.
    Record bytes unchanged since the original review.
  snapshot_sha256: c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T055920Z-dna-polymerase-iii-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8d6bee94d6883ee608284a00645339c60ee1f4746516dcdeb16ea14aea9317ae
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_core_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b;
    current SHA256 d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b.
    Record bytes unchanged since the original review.
  snapshot_sha256: d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T055921Z-dna-polymerase-iii-core-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 7e4cb02a04eac7dfa78f910030008db27dab2269a40d2f750b03b258928b8491
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/dna_replication_factor_a_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 a3cfb2654e3e82b6d841247eb4580f288e2bb1d082ff6d5a06ae5f363019f7a9;
    current SHA256 875ef33eba1336b1bfd61e3c5bc9f0ade5f2c37a93d25793797fa5b9ac34c133.
    Changed record reassessed against current sources.
  snapshot_sha256: 875ef33eba1336b1bfd61e3c5bc9f0ade5f2c37a93d25793797fa5b9ac34c133
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 32bc2458f21adb0704d23ce69748bab13f6086cecaa7226cbd7af8d93bf3f1a2
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/dna_replication_factor_c_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f;
    current SHA256 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 157b78894391f59a60728857bb07e85213b854d02c8a6be3e16cb1a3bc912ecc
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/dna_replication_preinitiation_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 1948bbd3828f9736b6dcf1151e9621969b9e0214863e42b559d21e7fff67c2ba;
    current SHA256 d38de0da7f792e34b56e5ef225160a88221fb8a9b64e309e2b28f34bc7038b88.
    Changed record reassessed against current sources.
  snapshot_sha256: d38de0da7f792e34b56e5ef225160a88221fb8a9b64e309e2b28f34bc7038b88
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 77ac82339e48756ab3ecfbc24de8ea5209e698ad430f9dc6ddc2f7c0ea60b963
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/dna_topoisomerase_iv_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070;
    current SHA256 fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070.
    Record bytes unchanged since the original review.
  snapshot_sha256: fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b2a67f0185810b26fb35419ab15c773de0a1daf6d8a9ebf53b248380aa159dc2
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/dnaa_diaa_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4;
    current SHA256 fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4.
    Record bytes unchanged since the original review.
  snapshot_sha256: fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 42d73a83ac80abf0e7081f8263e0c5cd5d25608ac689f9f4618583220dcdc62a
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/dnaa_dnab_dnac_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56;
    current SHA256 a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56.
    Record bytes unchanged since the original review.
  snapshot_sha256: a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T055925Z-dnaa-dnab-dnac-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b72282c71638516e097bc0d1e5e8b8eaab8d6820a207155ffba541d63c804ee0
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/dnaa_dps_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Original frozen SHA256 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87;
    current SHA256 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T06:35:23Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 17a6d0ebaeb2b67c1a3c0d574e5fb72fffc7d6b4406d454dbdeff1587035cf4e
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
  locator: Complete maintained YAML at 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
  accessed_at: '2026-11-04T06:26:22.353362Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected; no maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: d577d4fffb8f72d79620d78bfc245c04ed3481af7ab41b626ea4b7f21f0b166a
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T06:26:22.353449Z'
  support: supports
  summary: Original source inputs, checks, evidence scopes, assessments, verdicts,
    findings and proposed actions inspected. Historical checks and access timestamps
    are not newly executed or fetched.
  snapshot_sha256: be1948ad5ab70bdcec12e8bed2a7d82c3137fb5f68caafcd2a23d50c8b223c1f
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/0-stale.diff
  locator: Original frozen target versus current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8
  accessed_at: '2026-11-04T06:26:22.353485Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned slice. Current
    primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_complex.yaml
  locator: Complete maintained YAML at 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
  accessed_at: '2026-11-04T06:26:22.353512Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected; no maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: c807793b2a1531837a29634bbc50dcbf9e75f9c5e812c495086756a755baa55d
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T055920Z-dna-polymerase-iii-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T06:26:22.353531Z'
  support: supports
  summary: Original source inputs, checks, evidence scopes, assessments, verdicts,
    findings and proposed actions inspected. Historical checks and access timestamps
    are not newly executed or fetched.
  snapshot_sha256: 8d6bee94d6883ee608284a00645339c60ee1f4746516dcdeb16ea14aea9317ae
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/1-stale.diff
  locator: Original frozen target versus current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8
  accessed_at: '2026-11-04T06:26:22.353560Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned slice. Current
    primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/dna_polymerase_iii_core_complex.yaml
  locator: Complete maintained YAML at 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
  accessed_at: '2026-11-04T06:26:22.353580Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected; no maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: d3f7d2562674074de9eac445b01e2e20a566e590840dba0edac515a22b02d47b
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T055921Z-dna-polymerase-iii-core-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T06:26:22.353598Z'
  support: supports
  summary: Original source inputs, checks, evidence scopes, assessments, verdicts,
    findings and proposed actions inspected. Historical checks and access timestamps
    are not newly executed or fetched.
  snapshot_sha256: 7e4cb02a04eac7dfa78f910030008db27dab2269a40d2f750b03b258928b8491
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/2-stale.diff
  locator: Original frozen target versus current main 67507eedbb48c8977ac4bde3452fdfd3e4d6acb8
  accessed_at: '2026-11-04T06:26:22.353628Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned slice. Current
    primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components and exact family grounding; formation versus function; discussions
    append-only contract
  accessed_at: '2026-11-04T06:26:22.353648Z'
  support: supports
  summary: Verified taxon-neutral whole-protein families are distinct from reference-strain
    examples and domains. UNKNOWN formation is not inherently defective. Preserve
    historical rationale/posed_date; current prompts/notes may be narrowed after supported
    curation.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component classes, complex identity/hierarchy and graph scopes
  accessed_at: '2026-11-04T06:26:22.353669Z'
  support: supports
  summary: Generic classes/subcomplex components and bounded NONMECHANISTIC FUNCTION
    outlines are valid. No optional individual-protein inventory is required for a
    correctly GO-grounded subcomplex record.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks; current profile, config and shared review
    contract
  accessed_at: '2026-11-04T06:26:22.353696Z'
  support: supports
  summary: Positive molecular/pathway claims trigger source applicability even without
    an expression assertion. Official catalogue and actual matched gene/module checks
    require strain and computational limits. Seventeen common local inputs are hash-identical
    to prior reads; skill/profile/config/review contract and pertinent curation clauses
    reread.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Constituent references, direct versus contextual evidence, bounded function
    outlines
  accessed_at: '2026-11-04T06:26:22.353714Z'
  support: supports
  summary: Physical identity and descriptive membership/function are assessed separately
    from formation necessity, a complete reaction sequence, kinetic transition measurements
    and mandatory new experiments.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/original-audit.json
  locator: Six actual original validate/render commands;42 historical input occurrences;6
    original artifacts
  accessed_at: '2026-11-04T06:25:58.952101Z'
  support: supports
  summary: All three original YAMLs validate and render exactly their retained Markdown.
    All42 historical input hashes match recorded source revisions; all6 artifacts
    equal the original PR head.
  snapshot_sha256: 69228448c1fe5dee90f0bb349d41fe8a897c892896c218d58350927512ac02ec
- evidence_id: micro-up-P03007
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P03007.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P03007.raw
  accessed_at: '2026-11-04T06:16:19.651751Z'
  support: supports
  summary: 'P03007: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit epsilon;
    genes [''dnaQ'']; loci [''b0215'', ''JW0205'']; taxon 83333; InterPro [''IPR006054'',
    ''IPR006309'', ''IPR013520'', ''IPR012337'', ''IPR036397'']. Native annotations
    are authority evidence, not independent body reads of every linked paper.'
  snapshot_sha256: 21e6df3ed69332415da811c4d066d8ea6b0a2234a0d4c3dbcb2ff4d3613f7aef
- evidence_id: micro-up-P06710
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P06710.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P06710.raw
  accessed_at: '2026-11-04T06:16:20.672346Z'
  support: supports
  summary: 'P06710: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit tau;
    genes [''dnaX'']; loci [''b0470'', ''JW0459'']; taxon 83333; InterPro [''IPR003593'',
    ''IPR001270'', ''IPR008921'', ''IPR022001'', ''IPR022754'', ''IPR012763'', ''IPR021029'',
    ''IPR050238'', ''IPR045085'', ''IPR027417'', ''IPR038249'']. Native annotations
    are authority evidence, not independent body reads of every linked paper. Programmed
    frameshifting distinguishes tau/gamma, and SUBUNIT explicitly permits three copies
    of either or both; cellular viability annotations are not formation measurements
    for every isolated loader.'
  snapshot_sha256: 9dda9544a27ae2699f7d77382a528089a2ff9fff43ab2d5106c4b1817d3db291
- evidence_id: micro-up-P0A988
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A988.json
  locator: Current native identity/status/name/primary gene/loci/taxon only; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P0A988.raw
  accessed_at: '2026-11-04T06:20:36.344626Z'
  support: supports
  summary: 'P0A988: UniProtKB reviewed (Swiss-Prot); Beta sliding clamp; genes [''dnaN''];
    loci [''b3701'', ''JW3678'']; taxon 83333; InterPro [''IPR046938'', ''IPR001001'',
    ''IPR022635'', ''IPR022637'', ''IPR022634'']. External beta reference used only
    to select dnaN locus for whole-holoenzyme dataset context; not added as a maintained
    example or used to certify additional functional literature.'
  snapshot_sha256: 41e5cead43ae6b73cc4fedfee2b9e111259e12f217532aba8590e487ea82f65f
- evidence_id: micro-up-P0ABS8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ABS8.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P0ABS8.raw
  accessed_at: '2026-11-04T06:16:18.611339Z'
  support: supports
  summary: 'P0ABS8: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit theta;
    genes [''holE'']; loci [''b1842'', ''JW1831'']; taxon 83333; InterPro [''IPR009052'',
    ''IPR036745'']. Native annotations are authority evidence, not independent body
    reads of every linked paper. Native uncertainty about exact theta function does
    not negate its core membership; no theta-specific polymerase or proofreading catalysis
    is asserted.'
  snapshot_sha256: 0cce0044d1aa6208572485d8e5c538603e9fe638aa1bafcb67fca6bb9c3f0673
- evidence_id: micro-up-P10443
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P10443.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P10443.raw
  accessed_at: '2026-11-04T06:16:21.689887Z'
  support: supports
  summary: 'P10443: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit alpha;
    genes [''dnaE'']; loci [''b0184'', ''JW0179'']; taxon 83333; InterPro [''IPR011708'',
    ''IPR041931'', ''IPR040982'', ''IPR048472'', ''IPR004805'', ''IPR029460'', ''IPR012340'',
    ''IPR004365'', ''IPR004013'', ''IPR003141'', ''IPR016195'', ''IPR049821'']. Native
    annotations are authority evidence, not independent body reads of every linked
    paper. Historical E.coli polC synonym does not equate DnaE with the separate Gram-positive
    PolC class.'
  snapshot_sha256: b7b6bd780313462cb8f38d4a595395fa1a25b608f07fb9610d6bf8b894a202e9
- evidence_id: micro-up-P28630
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28630.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28630.raw
  accessed_at: '2026-11-04T06:16:22.698514Z'
  support: supports
  summary: 'P28630: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit delta;
    genes [''holA'']; loci [''b0640'', ''JW0635'']; taxon 83333; InterPro [''IPR008921'',
    ''IPR032780'', ''IPR010372'', ''IPR005790'', ''IPR027417'']. Native annotations
    are authority evidence, not independent body reads of every linked paper.'
  snapshot_sha256: 5e2a1e19871db4c2fed6d09113fd509529216b53773a162e7f1d6e6961f60934
- evidence_id: micro-up-P28631
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28631.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28631.raw
  accessed_at: '2026-11-04T06:16:23.766864Z'
  support: supports
  summary: 'P28631: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit delta'';
    genes [''holB'']; loci [''b1099'', ''JW1085'']; taxon 83333; InterPro [''IPR008921'',
    ''IPR004622'', ''IPR015199'', ''IPR050238'', ''IPR048731'', ''IPR027417'']. Native
    annotations are authority evidence, not independent body reads of every linked
    paper.'
  snapshot_sha256: ec3b56d7d2bc891f94eaa40f752d2ce89ad6777698e8d4b729626fed970de38a
- evidence_id: micro-up-P28632
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28632.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28632.raw
  accessed_at: '2026-11-04T06:16:25.639293Z'
  support: supports
  summary: 'P28632: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit psi;
    genes [''holD'']; loci [''b4372'', ''JW4334'']; taxon 83333; InterPro [''IPR004615'',
    ''IPR036654'', ''IPR018382'']. Native annotations are authority evidence, not
    independent body reads of every linked paper.'
  snapshot_sha256: 5b0d2927c696ac3aee8304d1e0bca6ff313e6655c90a21fa618a247a7e1dc7b2
- evidence_id: micro-up-P28905
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P28905.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro plus complete
    relevant FUNCTION/SUBUNIT/alternative-products comments; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/up-P28905.raw
  accessed_at: '2026-11-04T06:16:24.771366Z'
  support: supports
  summary: 'P28905: UniProtKB reviewed (Swiss-Prot); DNA polymerase III subunit chi;
    genes [''holC'']; loci [''b4259'', ''JW4216'']; taxon 83333; InterPro [''IPR007459'',
    ''IPR036768'']. Native annotations are authority evidence, not independent body
    reads of every linked paper.'
  snapshot_sha256: 7b36f4f87de6692ef228e17ced56294a628188d88a248f1debd62a912eef5f57
- evidence_id: micro-query-dnaE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-dnaE.raw
  accessed_at: '2026-11-04T06:16:24.883836Z'
  support: supports
  summary: Current bounded query returns ['P10443']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 24a7c7506484b0c644f37cd46d3060a98b52c24a536dc774afdcbc7ba2c4e5e4
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:24.883836Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-dnaQ
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaQ%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-dnaQ.raw
  accessed_at: '2026-11-04T06:16:25.860404Z'
  support: supports
  summary: Current bounded query returns ['P03007']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 2cc26f272453252c03d79d4ceba13fa02254b94b95d2501d84300b975d38f6ba
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaQ%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:25.860404Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-dnaX
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaX%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-dnaX.raw
  accessed_at: '2026-11-04T06:16:19.740756Z'
  support: supports
  summary: Current bounded query returns ['P06710']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 4e78670a6d5108938c60e146feb18662a8b7a5a943ceb4726382ad7b35f257a8
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaX%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:19.740756Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-holA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holA.raw
  accessed_at: '2026-11-04T06:16:18.923805Z'
  support: supports
  summary: Current bounded query returns ['P28630']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 6461857914d6912e6053148a39a941b5d47155f2970fade624132a2a0b742874
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholA%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:18.923805Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-holB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holB.raw
  accessed_at: '2026-11-04T06:16:20.725873Z'
  support: supports
  summary: Current bounded query returns ['P28631']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 7963053af8c79623841085f31a8a582d8d2a320210556aa12f612e166d8af7b3
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholB%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:20.725873Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-holC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holC.raw
  accessed_at: '2026-11-04T06:16:22.685283Z'
  support: supports
  summary: Current bounded query returns ['P28905']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 9ffe9c8d9221032fc7915464e2c8e9e9ab26683e7b264268b35ffe517dc856f0
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholC%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:22.685283Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-holD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holD.raw
  accessed_at: '2026-11-04T06:16:23.617052Z'
  support: supports
  summary: Current bounded query returns ['P28632']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 7a9744a2b70bad7c77358c27cbde2c7602185f088d552801264210ebf52453c5
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholD%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:23.617052Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-query-holE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/query-holE.raw
  accessed_at: '2026-11-04T06:16:21.705103Z'
  support: supports
  summary: Current bounded query returns ['P0ABS8']; singleton agrees with maintained
    identity. This does not reconstruct an October query or prove membership/formation.
  snapshot_sha256: 0eb3d97acbb204347081e21cec2bf1265cd6b21eda9d8a31ba83a8c96df42680
  search_scope: UniProtKB REST literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AholE%29+AND+%28taxonomy_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    actual 2026-11-04T06:16:21.705103Z; requested size500; complete returned singleton
    page. Exact reviewed gene/taxon83333 only, no all-alias/all-taxon or historical
    uniqueness assertion.
- evidence_id: micro-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/tax-562.raw
  accessed_at: '2026-11-04T06:16:25.922090Z'
  support: supports
  summary: '562: Escherichia coli; rank species. Species562 is distinct from reference
    strain83333; this does not identify unread source experimental strains.'
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-04T06:16:26.005177Z'
  support: supports
  summary: '83333: Escherichia coli K-12; rank strain. Species562 is distinct from
    reference strain83333; this does not identify unread source experimental strains.'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro-go-0003689
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003689
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0003689.raw
  accessed_at: '2026-11-04T06:16:23.955513Z'
  support: supports
  summary: 'GO:0003689: DNA clamp loader activity; obsolete=False; definition {''text'':
    ''Facilitating the opening of the ring structure of the PCNA complex, or any of
    the related sliding clamp complexes, and their closing around the DNA duplex,
    driven by ATP hydrolysis.'', ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''16082778''}]}.
    Ontology wording is checked separately against biological source scope, not adopted
    as infallible experiment evidence.'
  snapshot_sha256: f123eb12d15e9440d784ac0cef214c66c2920ac3fa33e908178e8da7c454a5b8
- evidence_id: micro-go-0003887
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003887
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0003887.raw
  accessed_at: '2026-11-04T06:16:23.670910Z'
  support: supports
  summary: 'GO:0003887: DNA-directed DNA polymerase activity; obsolete=False; definition
    {''text'': "Catalysis of the reaction: deoxynucleoside triphosphate + DNA(n) =
    diphosphate + DNA(n+1); DNA-template-directed extension of the 3''-end of a DNA
    strand by one nucleotide at a time.", ''xrefs'': [{''dbCode'': ''EC'', ''dbId'':
    ''2.7.7.7''}]}. Ontology wording is checked separately against biological source
    scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: ff00aa579383590a41647ad9ced1a2df44314b37ea582543037f28531b4681cb
- evidence_id: micro-go-0006260
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006260
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0006260.raw
  accessed_at: '2026-11-04T06:16:23.969457Z'
  support: supports
  summary: 'GO:0006260: DNA replication; obsolete=False; definition {''text'': ''The
    cellular metabolic process in which a cell duplicates one or more molecules of
    DNA. DNA replication begins when specific sequences, known as origins of replication,
    are recognized and bound by the origin recognition complex, and ends when the
    original DNA molecule has been completely duplicated and the copies topologically
    separated. The unit of replication usually corresponds to the genome of the cell,
    an organelle, or a virus. The template for replication can either be an existing
    DNA molecule or RNA.''}. Ontology wording is checked separately against biological
    source scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: dc45c0feccd11a684f3d3f838297ef32f5b69a7b59a61d655120b7ac89ec8fba
- evidence_id: micro-go-0009360
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009360
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0009360.raw
  accessed_at: '2026-11-04T06:16:22.365337Z'
  support: supports
  summary: 'GO:0009360: DNA polymerase III complex; obsolete=False; definition {''text'':
    "The DNA polymerase III holoenzyme is a complex that contains 10 different types
    of subunits. These subunits are organized into 3 functionally essential sub-assemblies:
    the pol III core, the beta sliding clamp processivity factor and the clamp-loading
    complex. The pol III core carries out the polymerase and the 3''-5'' exonuclease
    proofreading activities. The polymerase is tethered to the template via the sliding
    clamp processivity factor. The clamp-loading complex assembles the beta processivity
    factor onto the primer template and plays a central role in the organization and
    communication at the replication fork.", ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'':
    ''11525729''}, {''dbCode'': ''PMID'', ''dbId'': ''12940977''}, {''dbCode'': ''UniProt'',
    ''dbId'': ''P06710''}]}. Ontology wording is checked separately against biological
    source scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: 4b5038b620c1b4a860e4500335d17a12aec81b36fa6def186d4716389e3ba757
- evidence_id: micro-go-0032991
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032991
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0032991.raw
  accessed_at: '2026-11-04T06:16:23.336456Z'
  support: supports
  summary: 'GO:0032991: protein-containing complex; obsolete=False; definition {''text'':
    ''A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids,
    carbohydrates or lipids, in which at least one component is a protein and the
    constituent parts function together.''}. Ontology wording is checked separately
    against biological source scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
- evidence_id: micro-go-0042575
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042575
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0042575.raw
  accessed_at: '2026-11-04T06:16:23.545881Z'
  support: supports
  summary: 'GO:0042575: DNA polymerase complex; obsolete=False; definition {''text'':
    ''A protein complex that possesses DNA polymerase activity and is involved in
    template directed synthesis of DNA.'', ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'':
    ''12045093''}]}. Ontology wording is checked separately against biological source
    scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: 03e6fe0dd8263f1e7fca5a967f126141e378a6b572bed7ab152452b57a4c727f
- evidence_id: micro-go-0043846
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0043846.raw
  accessed_at: '2026-11-04T06:16:22.330744Z'
  support: supports
  summary: 'GO:0043846: DNA polymerase III, clamp loader complex; obsolete=False;
    definition {''text'': ''A heptamer that includes the tau and gamma products of
    the dnaX gene and the chi/psi subcomplex. Confers structural asymmetry that allows
    the polymerase to replicate both leading and lagging strands.'', ''xrefs'': [{''dbCode'':
    ''PMID'', ''dbId'': ''12940977''}]}. Ontology wording is checked separately against
    biological source scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: eeed7abe4e2c1402377d625d38b7f0dbe90bea19418a5da79d8f232ed383c447
- evidence_id: micro-go-0043847
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043847
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0043847.raw
  accessed_at: '2026-11-04T06:16:23.356891Z'
  support: supports
  summary: 'GO:0043847: DNA polymerase III, clamp loader chi/psi subcomplex; obsolete=False;
    definition {''text'': ''A dimer composed of the chi and psi subunits which is
    a subassembly of the DNA polymerase III clamp loader complex and serves as a bridge
    between the DnaX complex and the single-stranded DNA-binding protein (SSB).'',
    ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''12940977''}]}. Ontology wording
    is checked separately against biological source scope, not adopted as infallible
    experiment evidence.'
  snapshot_sha256: 272d831705e0da87c0327899fd1d5ca431768e874ce856a4457759d74b11a45f
- evidence_id: micro-go-0044775
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044775
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0044775.raw
  accessed_at: '2026-11-04T06:16:22.950709Z'
  support: supports
  summary: 'GO:0044775: DNA polymerase III, beta sliding clamp processivity factor
    complex; obsolete=False; definition {''text'': ''A subcomplex of the DNA polymerase
    III holoenzyme which is responsible for tethering the catalytic subunit of DNA
    polymerase to DNA during high-speed replication. The complex is homodimeric in
    prokaryotes, and homotrimeric in other species.'', ''xrefs'': [{''dbCode'': ''UniProt'',
    ''dbId'': ''O73947''}]}. Ontology wording is checked separately against biological
    source scope, not adopted as infallible experiment evidence.'
  snapshot_sha256: aab63fe0f13574e5cdb4285ac6c21025c42bd555213b4bdd48c4fe1328c9dba8
- evidence_id: micro-go-0044776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/go-0044776.raw
  accessed_at: '2026-11-04T06:16:22.924095Z'
  support: supports
  summary: 'GO:0044776: DNA polymerase III, core complex; obsolete=False; definition
    {''text'': "The DNA polymerase III core complex consists of the alpha,epsilon
    and theta subunits and is carries out the polymerase and the 3''-5'' exonuclease
    proofreading activities.", ''xrefs'': [{''dbCode'': ''UniProt'', ''dbId'': ''P06710''}]}.
    Ontology wording is checked separately against biological source scope, not adopted
    as infallible experiment evidence.'
  snapshot_sha256: 982b73157eba30d19078e0d907e9bfbf961c71042efafc23c62aec999f229282
- evidence_id: micro-isa-0043846
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/isa-0043846.raw
  accessed_at: '2026-11-04T06:16:24.218234Z'
  support: supports
  summary: 'Ancestors [''GO:0043846'', ''GO:0140513'', ''GO:0032991'', ''GO:0005575''];
    children [{''id'': ''GO:0043847'', ''relation'': ''part_of''}]. Core parent GO0042575
    is a biological activity-based class assertion, not claimed as a direct current
    GO edge. Loader/core nuclear-complex ancestry is an upstream mismatch with bacterial
    source evidence, not imported into records.'
  snapshot_sha256: 1128025335da2d8d3aa0304ebfbdd748618e7038b4623a85e7354099f7155a2b
- evidence_id: micro-isa-0009360
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009360/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/isa-0009360.raw
  accessed_at: '2026-11-04T06:16:24.440250Z'
  support: supports
  summary: 'Ancestors [''GO:1902494'', ''GO:0061695'', ''GO:0009360'', ''GO:1990234'',
    ''GO:0140535'', ''GO:0032991'', ''GO:0042575'', ''GO:0005575'']; children [{''id'':
    ''GO:0043846'', ''relation'': ''part_of''}, {''id'': ''GO:0044776'', ''relation'':
    ''part_of''}, {''id'': ''GO:0044775'', ''relation'': ''part_of''}]. Core parent
    GO0042575 is a biological activity-based class assertion, not claimed as a direct
    current GO edge. Loader/core nuclear-complex ancestry is an upstream mismatch
    with bacterial source evidence, not imported into records.'
  snapshot_sha256: 81e1e0b35d523903f5f118e838e3bc4c1132f27abfa1ae01da2c17958c45da04
- evidence_id: micro-isa-0044776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/isa-0044776.raw
  accessed_at: '2026-11-04T06:16:24.875778Z'
  support: supports
  summary: 'Ancestors [''GO:0140513'', ''GO:0032991'', ''GO:0005575'', ''GO:0044776''];
    children [{''id'': ''GO:0043845'', ''relation'': ''part_of''}]. Core parent GO0042575
    is a biological activity-based class assertion, not claimed as a direct current
    GO edge. Loader/core nuclear-complex ancestry is an upstream mismatch with bacterial
    source evidence, not imported into records.'
  snapshot_sha256: ab4cb6cea7010b6cf36cc956057da7b449aa48a3c9b48064faa49923274a58ab
- evidence_id: micro-constraints-0043846
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043846/constraints
  locator: Exact taxonConstraints field only; unrelated blacklist entries not used;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/constraints-0043846.raw
  accessed_at: '2026-11-04T06:16:24.466384Z'
  support: context_only
  summary: 'Current only-in-Eukaryota constraint [{''ancestorId'': ''GO:0043846'',
    ''ancestorName'': ''DNA polymerase III, clamp loader complex'', ''relationship'':
    ''only_in_taxon'', ''taxId'': ''2759'', ''taxIdType'': ''NCBITaxon'', ''taxName'':
    ''Eukaryota''}] conflicts with named bacterial identity and primary E.coli evidence.
    No such restriction is asserted in the maintained record; not a new record finding.'
  snapshot_sha256: f205df2be188d25bee5993a261d00b35ef2445e8a8567653f6e6bf733a906124
- evidence_id: micro-constraints-0044776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044776/constraints
  locator: Exact taxonConstraints field only; unrelated blacklist entries not used;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/constraints-0044776.raw
  accessed_at: '2026-11-04T06:16:25.222446Z'
  support: context_only
  summary: 'Current only-in-Eukaryota constraint [{''ancestorId'': ''GO:0044776'',
    ''ancestorName'': ''DNA polymerase III, core complex'', ''relationship'': ''only_in_taxon'',
    ''taxId'': ''2759'', ''taxIdType'': ''NCBITaxon'', ''taxName'': ''Eukaryota''}]
    conflicts with named bacterial identity and primary E.coli evidence. No such restriction
    is asserted in the maintained record; not a new record finding.'
  snapshot_sha256: e70c1e9bafcda161d87935729c4dfa60dcd64a8e4c324c92063982fe305f2af1
- evidence_id: micro-ipr-IPR005790
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005790/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR005790.raw
  accessed_at: '2026-11-04T06:16:25.161393Z'
  support: supports
  summary: 'IPR005790: {''name'': ''DNA polymerase III, delta subunit'', ''short'':
    ''DNA_polIII_delta''}; type family; signatures {''panther'': {''PTHR34388'': ''DNA
    POLYMERASE III SUBUNIT DELTA''}, ''ncbifam'': {''TIGR01128'': ''DNA polymerase
    III subunit delta''}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.
    Exact HolA family; llm=true checked=true generated sentence attributing proofreading
    is not used as delta activity evidence.'
  snapshot_sha256: 32531e23cefcda3d6c8294919dc4689ba859fbed120049da273ec2a452b1594f
- evidence_id: micro-ipr-IPR007459
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007459/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR007459.raw
  accessed_at: '2026-11-04T06:16:25.270335Z'
  support: supports
  summary: 'IPR007459: {''name'': ''DNA polymerase III chi subunit, HolC'', ''short'':
    ''DNA_pol3_chi''}; type family; signatures {''panther'': {''PTHR38767'': ''DNA
    POLYMERASE III SUBUNIT CHI''}, ''pfam'': {''PF04364'': ''DNA polymerase III chi
    subunit, HolC''}}. Complete metadata description/type/hierarchy/integrated signatures
    inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 5f9af2b066940512eac57ef0e983bf79616c8e00846a7fdaf4ac3eeacc116d12
- evidence_id: micro-ipr-IPR004615
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004615/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004615.raw
  accessed_at: '2026-11-04T06:16:25.354580Z'
  support: supports
  summary: 'IPR004615: {''name'': ''DNA polymerase III, psi subunit'', ''short'':
    ''DNA_pol_III_psi''}; type family; signatures {''pirsf'': {''PIRSF029225'': ''DNA
    polymerase III, psi subunit''}, ''pfam'': {''PF03603'': ''DNA polymerase III psi
    subunit''}}. Complete metadata description/type/hierarchy/integrated signatures
    inspected; matching UniProt example xref is separate membership evidence. Exact
    HolD family; historical unknown-function wording does not refute primary biochemistry.'
  snapshot_sha256: 2c70542817958052c37c630066b6135d817759e1421ab5d91b21e0af5118a654
- evidence_id: micro-ipr-IPR004622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004622/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004622.raw
  accessed_at: '2026-11-04T06:16:25.468969Z'
  support: supports
  summary: 'IPR004622: {''name'': ''DNA polymerase III, delta prime subunit'', ''short'':
    ''DNA_pol_HolB''}; type domain; signatures {''ncbifam'': {''TIGR00678'': "DNA
    polymerase III subunit delta''"}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 1b80554d4eaa9095866a4e2ffd3b7c94281dbf076d6f123ff5346318a04a9188
- evidence_id: micro-ipr-IPR012763-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012763/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR012763-retry.raw
  accessed_at: '2026-11-04T06:19:57.224337Z'
  support: supports
  summary: 'IPR012763: {''name'': ''DNA polymerase III, subunit gamma/ tau, N-terminal'',
    ''short'': ''DNA_pol_III_sug/sutau_N''}; type domain; signatures {''ncbifam'':
    {''TIGR02397'': ''DNA polymerase III subunit gamma/tau''}}. Complete metadata
    description/type/hierarchy/integrated signatures inspected; matching UniProt example
    xref is separate membership evidence.'
  snapshot_sha256: 6c8943d9fc9b647cbd674de5cdb97eb79ca5180af0898055995e986bd4cdca6b
- evidence_id: micro-ipr-IPR009052-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009052/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR009052-retry.raw
  accessed_at: '2026-11-04T06:19:57.260911Z'
  support: supports
  summary: 'IPR009052: {''name'': ''DNA polymerase III-theta, bacterial'', ''short'':
    ''DNA_pol_III_theta_bac''}; type family; signatures {''pfam'': {''PF06440'': ''DNA
    polymerase III, theta subunit''}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 45912f79b5935dd572120ecb8fcf31e9a8343e5e8539ccbc69483c268708432b
- evidence_id: micro-ipr-IPR006309-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006309/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR006309-retry.raw
  accessed_at: '2026-11-04T06:19:57.335017Z'
  support: supports
  summary: 'IPR006309: {''name'': ''DNA polymerase 3, epsilon subunit'', ''short'':
    ''DnaQ_proteo''}; type family; signatures {''cdd'': {''cd06131'': "DEDDh 3''-5''
    exonuclease domain of the epsilon subunit of Escherichia coli DNA polymerase III
    and similar proteins"}, ''ncbifam'': {''TIGR01406'': ''DNA polymerase III subunit
    epsilon''}}. Complete metadata description/type/hierarchy/integrated signatures
    inspected; matching UniProt example xref is separate membership evidence. Full
    family is explicitly proteobacterial, not silently generalized to every epsilon-class
    taxon.'
  snapshot_sha256: 7a5dca1c5c7696f56079daf029888fd3b04af5cd59190ad06c3c1c1e9aebacbf
- evidence_id: micro-ipr-IPR006054
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006054/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR006054.raw
  accessed_at: '2026-11-04T06:16:25.854089Z'
  support: supports
  summary: 'IPR006054: {''name'': ''DNA polymerase III epsilon subunit, exonuclease
    domain'', ''short'': ''DnaQ''}; type domain; signatures {''ncbifam'': {''TIGR00573'':
    ''exonuclease, DNA polymerase III, epsilon subunit family''}}. Complete metadata
    description/type/hierarchy/integrated signatures inspected; matching UniProt example
    xref is separate membership evidence.'
  snapshot_sha256: 319bb97f2f94ae18c1a3f2bcbad55764516d14a4cd05ded2abaf1e45cfc9aaf8
- evidence_id: micro-ipr-IPR004805
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004805/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004805.raw
  accessed_at: '2026-11-04T06:16:25.907680Z'
  support: supports
  summary: 'IPR004805: {''name'': ''Error-prone DNA polymerase/DNA polymerase III
    subunit alpha DnaE/PolC'', ''short'': ''DnaE2/DnaE/PolC''}; type family; signatures
    {''panther'': {''PTHR32294'': ''DNA POLYMERASE III SUBUNIT ALPHA''}, ''ncbifam'':
    {''TIGR00594'': ''DNA polymerase III subunit alpha''}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.
    Broader DnaE2/DnaE/PolC family is not an exact DnaE-only substitute.'
  snapshot_sha256: 570a9854bc1ebd4db316953b55a0d871d2d11cd2449df72aa370eb9cab8ff7a1
- evidence_id: micro-ipr-IPR050238
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR050238.raw
  accessed_at: '2026-11-04T06:20:36.310357Z'
  support: supports
  summary: 'IPR050238: {''name'': ''DNA Replication and Repair Clamp Loader Complex'',
    ''short'': ''DNA_Rep/Repair_Clamp_Loader''}; type family; signatures {''panther'':
    {''PTHR11669'': ''DNA Replication and Repair Clamp Loader Complex''}}. Complete
    metadata description/type/hierarchy/integrated signatures inspected; matching
    UniProt example xref is separate membership evidence. Broad shared clamp-loader
    family also contains eukaryotic/plant proteins; llm=true checked=false prose not
    primary evidence or exact DnaX/HolB identity.'
  snapshot_sha256: 20cc681dc2b5aa75e096f21d298105d7ac05cc910f786be9e1f63ae05a72dbc0
- evidence_id: micro-ipr-IPR045085
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045085/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR045085.raw
  accessed_at: '2026-11-04T06:20:36.336763Z'
  support: supports
  summary: 'IPR045085: {''name'': ''DNA polymerase III, subunit gamma/tau, helical
    lid domain'', ''short'': ''HLD_clamp_pol_III_gamma_tau''}; type domain; signatures
    {''pfam'': {''PF22608'': ''DNA polymerase III clamp loader subunit, ATPase lid
    domain''}, ''cdd'': {''cd18137'': ''helical lid domain of DNA polymerase III subunits
    gamma and tau''}}. Complete metadata description/type/hierarchy/integrated signatures
    inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 112928e4357ef16955bab9b183f5b66f3e01647738cb314138044f3283cc3285
- evidence_id: micro-ipr-IPR048731-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048731/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR048731-retry.raw
  accessed_at: '2026-11-04T06:21:47.311790Z'
  support: supports
  summary: 'IPR048731: {''name'': "DNA polymerase III subunit delta'', AAA+ ATPase
    lid domain, gammaproteobacteria", ''short'': ''HolB_lid-gammaproteobact''}; type
    domain; signatures {''pfam'': {''PF21500'': "DNA polymerase III subunit delta'',
    AAA+ ATPase lid domain"}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 2890268ac9625b2a79c093c7638b39a8bd1de4db454555ec9cd8438c3a7713b8
- evidence_id: micro-ipr-IPR004365
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004365/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004365.raw
  accessed_at: '2026-11-04T06:20:36.317490Z'
  support: supports
  summary: 'IPR004365: {''name'': ''OB-fold nucleic acid binding domain, AA-tRNA synthetase-type'',
    ''short'': ''NA-bd_OB_tRNA''}; type domain; signatures {''pfam'': {''PF01336'':
    ''OB-fold nucleic acid binding domain''}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 273284e506ea5c1d0029a8470a2fbc7fe8bb037a89185154dc92998bdc6d9e54
- evidence_id: micro-ipr-IPR004013
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004013/
  locator: Complete native name/type/hierarchy/signatures/description and generated-prose
    flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR004013.raw
  accessed_at: '2026-11-04T06:20:36.341566Z'
  support: supports
  summary: 'IPR004013: {''name'': ''PHP domain'', ''short'': ''PHP_dom''}; type domain;
    signatures {''pfam'': {''PF02811'': ''PHP domain''}}. Complete metadata description/type/hierarchy/integrated
    signatures inspected; matching UniProt example xref is separate membership evidence.'
  snapshot_sha256: 12f42ec9e5f8c9781f872a0fbc3cec71f7c648717ab4906b5639cd1fba5d3e9d
- evidence_id: micro-pmid-11525729
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11525729+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED metadata and deposited abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/pmid-11525729.raw
  accessed_at: '2026-11-04T06:16:26.103431Z'
  support: supports
  summary: '11525729: Crystal structure of the processivity clamp loader gamma (gamma)
    complex of E. coli DNA polymerase III.; DOI 10.1016/s0092-8674(01)00463-9. Primary-study
    abstract completely read; no body claim from this response alone.'
  snapshot_sha256: 4ff4511cda4f650117a9af44622022e8ec92ea5951155252038e13cf35083111
- evidence_id: micro-pmid-12940977
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12940977+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED metadata and deposited abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/pmid-12940977.raw
  accessed_at: '2026-11-04T06:16:26.190433Z'
  support: context_only
  summary: '12940977: Chromosomal replicases as asymmetric dimers: studies of subunit
    arrangement and functional consequences.; DOI 10.1046/j.1365-2958.2003.03645.x.
    Secondary review abstract, with body scope separately stated.'
  snapshot_sha256: aad6b63ace81a7445d5853ff89368388b265ca915696bd7d874152b36eb89d1b
- evidence_id: micro-pmid-3283127
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3283127+AND+SRC%3AMED&format=json&resultType=core&pageSize=1000
  locator: Complete exact MED metadata and deposited abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/pmid-3283127.raw
  accessed_at: '2026-11-04T06:16:26.199462Z'
  support: supports
  summary: '3283127: DNA polymerase III holoenzyme of Escherichia coli. III. Distinctive
    processive polymerases reconstituted from purified subunits.; DOI 10.1016/s0021-9258(18)68678-8.
    Primary-study abstract completely read; no body claim from this response alone.'
  snapshot_sha256: 330528745d6f0892bafc33acb9a108f43203e43fc2e3e4be10b2723b152f8cec
- evidence_id: micro-jeruzalmi2001-pdf
  kind: primary_source
  reference: https://odonnell.rockefeller.edu/assets/pdfs/119.pdf
  locator: Genuine author-hosted PDF pp429–431 Summary/Introduction/Results structure
    determination/general description and Fig1 text caption; pp439–440 conclusion
    and Experimental Procedures; no pixels/coordinates/supplements; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/jeruzalmi2001-pdf.raw
  accessed_at: '2026-11-04T06:16:26.597495Z'
  support: supports
  summary: Observed nucleotide-free gamma3-delta-delta-prime pentamer uses truncated
    gamma1–373, purified reconstitution and anisotropic2.7/3.0Å diffraction. Authors
    distinguish observed structure from speculative ATP-transition models; activity
    of the truncated preparation is reported with data not shown. Tau/chi/psi are
    not crystallized constituents. Source species E.coli does not certify a living
    unmodified K12 heptamer preparation.
  snapshot_sha256: b024aaa1d316c18a39e7f86ec5730dcd7078d94567157ca5df00d40eb7cf7211
- evidence_id: micro-mchenry2003-pdf
  kind: authority
  reference: https://www.sbs.utexas.edu/psaxena/bio226r/articles/dna_replication_mchenry_2003.pdf
  locator: 'Genuine secondary-review PDF pp1157–1159 and opening p1160: organization/DnaX
    alternatives, tau coupling/helicase/processivity discussion, Fig1 text caption;
    no complete-review or pixel claim; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/mchenry2003-pdf.raw'
  accessed_at: '2026-11-04T06:16:26.605880Z'
  support: supports
  summary: 'Secondary review describes full DnaX3-delta-delta-prime-chi-psi heptamer:
    any tau/gamma mixture can load beta with similar efficiency before polymerase;
    tau contributes additional polymerase/helicase contacts. Mixed tau/gamma in-vivo
    model is distinguished from minimum clamp-loading composition. No invariant in-vivo
    ratio, full-review body read or primary new assay claimed.'
  snapshot_sha256: 943b7e0a6435e55da1766d5c567ff47410ece005e4ff3d137f150f30b2cb40d8
- evidence_id: micro-maki1988-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/S0021925818686788?httpAccept=text/xml
  locator: Publisher core XML metadata only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/maki1988-api.raw
  accessed_at: '2026-11-04T06:16:26.307690Z'
  support: supports
  summary: Exact title/year/journal/DOI corroborated; response name full-text-retrieval
    does not mean primary body was delivered. Maki/Kornberg assessed only at complete
    primary-abstract tier.
  snapshot_sha256: c1bed0605d12c6dc3ac2272a61b03286e8fecae29104f90c2efb114058984b53
- evidence_id: micro-maki1988-html-access
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/maki1988-html.raw
  accessed_at: '2026-11-04T06:16:26.006468Z'
  support: context_only
  summary: HTTP403 diagnostic only. No inaccessible body or family metadata certified;
    independent complete abstract or later successful exact-authority response is
    recorded separately.
  snapshot_sha256: a6d50c1bdab5aba8927ca408fed4a6339bae964306b9ab1a49f8eda9f706e13d
- evidence_id: micro-maki1988-pdf-access
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/pdf
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/maki1988-pdf.raw
  accessed_at: '2026-11-04T06:16:26.026408Z'
  support: context_only
  summary: HTTP403 diagnostic only. No inaccessible body or family metadata certified;
    independent complete abstract or later successful exact-authority response is
    recorded separately.
  snapshot_sha256: 2d4efa6a6d6b078b00ed885346cd87033c0cf1cb6d315ceb08bf561d88748388
- evidence_id: micro-ipr-IPR012763-access
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012763/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR012763.raw
  accessed_at: '2026-11-04T06:16:25.524647Z'
  support: context_only
  summary: HTTP429 diagnostic only. No inaccessible body or family metadata certified;
    independent complete abstract or later successful exact-authority response is
    recorded separately.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-ipr-IPR009052-access
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009052/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR009052.raw
  accessed_at: '2026-11-04T06:16:25.540285Z'
  support: context_only
  summary: HTTP429 diagnostic only. No inaccessible body or family metadata certified;
    independent complete abstract or later successful exact-authority response is
    recorded separately.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-ipr-IPR006309-access
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006309/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR006309.raw
  accessed_at: '2026-11-04T06:16:25.745232Z'
  support: context_only
  summary: HTTP429 diagnostic only. No inaccessible body or family metadata certified;
    independent complete abstract or later successful exact-authority response is
    recorded separately.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-ipr-IPR048731-access
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048731/
  locator: Actual retained access response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ipr-IPR048731.raw
  accessed_at: '2026-11-04T06:20:36.330403Z'
  support: context_only
  summary: HTTP429 diagnostic only. No inaccessible body or family metadata certified;
    independent complete abstract or later successful exact-authority response is
    recorded separately.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-historical-1-root51-maki1988-publisher
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:39:47.294023Z'
  support: context_only
  summary: The publisher route did not yield the primary body; this paper is assessed
    at complete native abstract tier. Historical access time/hash preserved; no fresh
    retrieval. Correct kind only from database to validation/context_only; original
    already admitted body-access limitation.
  snapshot_sha256: 7db7b0f002f2747181469b72daf45bf858d9125401da12cca2f8a09cc97961bd
- evidence_id: micro-historical-1-root51-maki1988-pdf
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/pdf
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:39:47.294276Z'
  support: context_only
  summary: The publisher route did not yield the primary body; this paper is assessed
    at complete native abstract tier. Historical access time/hash preserved; no fresh
    retrieval. Correct kind only from database to validation/context_only; original
    already admitted body-access limitation.
  snapshot_sha256: ebfcff9aa58d658572a47664652741787c4a534e9002f88f76d98e3daa9d8735
- evidence_id: micro-historical-2-root51-maki1988-publisher
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/fulltext
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:39:47.294023Z'
  support: context_only
  summary: The publisher route did not yield the primary body; this paper is assessed
    at complete native abstract tier. Historical access time/hash preserved; no fresh
    retrieval. Correct kind only from database to validation/context_only; original
    already admitted body-access limitation.
  snapshot_sha256: 7db7b0f002f2747181469b72daf45bf858d9125401da12cca2f8a09cc97961bd
- evidence_id: micro-historical-2-root51-maki1988-pdf
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)68678-8/pdf
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:39:47.294276Z'
  support: context_only
  summary: The publisher route did not yield the primary body; this paper is assessed
    at complete native abstract tier. Historical access time/hash preserved; no fresh
    retrieval. Correct kind only from database to validation/context_only; original
    already admitted body-access limitation.
  snapshot_sha256: ebfcff9aa58d658572a47664652741787c4a534e9002f88f76d98e3daa9d8735
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official20-organism catalogue and all dataset entries; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T06:16:25.827407Z'
  support: supports
  summary: Actual E.coli host has precise1k among listed datasets. Selection is a
    bounded current catalogue check, not universal or future coverage.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB GET /api/datasets at 2026-11-04T06:16:25.827407Z; all20
    returned organism rows and all listed dataset entries; no pagination/truncation.
    Exact E.coli host selection; no foreign-host proxy.
- evidence_id: micro-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete selected precise1k metadata and five-strain list; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T06:16:26.387064Z'
  support: context_only
  summary: BW25113,DGF-298,GMOS,MG1655,W3110;1035samples/518conditions/201modules/4257genes.
    K12-related reference context is not exact Jeruzalmi recombinant-preparation coverage
    or Maki experimental strain identification.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-ecoli-modules
  kind: search
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 returned module names/regulators/functions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T06:16:25.939241Z'
  support: context_only
  summary: Complete selected module inventory inspected; names and inferred regulator
    labels are not proof of physical assembly or direct regulation.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: iModulonDB e_coli/precise1k module listing at 2026-11-04T06:16:25.939241Z;
    all201 returned entries, selected dataset only; no other dataset or experimental
    activity contrast examined.
- evidence_id: micro-ecoli-gene-b0470
  kind: search
  reference: https://imodulondb.org/api/genes/b0470/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0470.raw
  accessed_at: '2026-11-04T06:19:56.752408Z'
  support: context_only
  summary: b0470 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: 310f63e12eaf82829d04b8ada01acc7a111b5db11ccd96401f264ab62e66a758
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b0470/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.752408Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b0640
  kind: search
  reference: https://imodulondb.org/api/genes/b0640/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0640.raw
  accessed_at: '2026-11-04T06:19:56.697542Z'
  support: context_only
  summary: b0640 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: 56e0c959ad4604bf02ecb29f4a4e508a3e08bb89de6b2bffd7186019577c899d
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b0640/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.697542Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b1099
  kind: search
  reference: https://imodulondb.org/api/genes/b1099/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b1099.raw
  accessed_at: '2026-11-04T06:19:56.729422Z'
  support: context_only
  summary: b1099 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: 1592b42bf4ba2b2b865f67a6ba7db110f690705fd15c583f2b8b21325ecb7720
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b1099/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.729422Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b4259
  kind: search
  reference: https://imodulondb.org/api/genes/b4259/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b4259.raw
  accessed_at: '2026-11-04T06:19:56.738444Z'
  support: context_only
  summary: b4259 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: be8fe859fb1c07c2e7a323c11e0c60e1a95b628d87875b7b37124f5bef8caf9b
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b4259/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.738444Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b4372
  kind: search
  reference: https://imodulondb.org/api/genes/b4372/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b4372.raw
  accessed_at: '2026-11-04T06:19:56.736198Z'
  support: context_only
  summary: 'b4372 yields201 rows and hits [{"k": 145, "name": "ppGpp", "regulator":
    ["ppGpp"], "function": "Stringent response", "category": "Global Stress", "weight":
    0.055361181, "threshold": 0.048379363, "in_imodulon": true}]. Negative threshold
    membership is not gene absence or dispensability; positive membership does not
    establish assembly, localization, direct regulation or formation.'
  snapshot_sha256: a7d1d16bb4c67ee5f721614cf65f823f0c6ee5764843fb782934a3033180ad8a
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b4372/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.736198Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b0184
  kind: search
  reference: https://imodulondb.org/api/genes/b0184/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0184.raw
  accessed_at: '2026-11-04T06:19:56.729485Z'
  support: context_only
  summary: b0184 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: 143d5a62bb5189ba1ab1d99d38aea82efea3515bdf647e09d19897dbbe3ad94e
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b0184/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.729485Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b0215
  kind: search
  reference: https://imodulondb.org/api/genes/b0215/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b0215.raw
  accessed_at: '2026-11-04T06:19:56.733847Z'
  support: context_only
  summary: b0215 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: 1c9c83401344556f11384a534a0b4ae6e5d4324e90f30a37f7b9805c7bec86a5
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b0215/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.733847Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b1842
  kind: search
  reference: https://imodulondb.org/api/genes/b1842/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b1842.raw
  accessed_at: '2026-11-04T06:19:56.733818Z'
  support: context_only
  summary: 'b1842 yields201 rows and hits [{"k": 147, "name": "PAL 26 Del", "regulator":
    null, "function": "Unknown", "category": "Unknown", "weight": 0.124483338, "threshold":
    0.058096464, "in_imodulon": true}]. Negative threshold membership is not gene
    absence or dispensability; positive membership does not establish assembly, localization,
    direct regulation or formation.'
  snapshot_sha256: 9106a3b793b069ca1e94bdad9d4215b575ad5a9bd6ff170f853681bd3bddb4d3
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b1842/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:19:56.733818Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-gene-b3701
  kind: search
  reference: https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus weights/thresholds/membership rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-gene-b3701.raw
  accessed_at: '2026-11-04T06:20:35.691077Z'
  support: context_only
  summary: b3701 yields201 rows and hits []. Negative threshold membership is not
    gene absence or dispensability; positive membership does not establish assembly,
    localization, direct regulation or formation.
  snapshot_sha256: d5e604543410b34561ac751e5b38c067a221e6ff1983dc41a90a52a22cc6670a
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T06:20:35.691077Z; exact reference locus, all201 returned rows. Five-strain
    precise1k only, no alias/all-dataset/universal absence claim.
- evidence_id: micro-ecoli-module-145
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/145
  locator: Actual module metadata and complete gene-weight list; generated AI prose
    and activities not used; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-module-145.raw
  accessed_at: '2026-11-04T06:20:35.701571Z'
  support: context_only
  summary: Module145 ppGpp; function Stringent response; 70 genes; b4372 weight 0.055361181
    exceeds threshold 0.048379363. Computational context only. Module147 has no regulator
    annotation and function Unknown; no mechanistic inference from its name.
  snapshot_sha256: 830f9a931fa5b6577f9ad87c99a4cbc198961cbd72c61ad8ff4d42812846f2dd
- evidence_id: micro-ecoli-module-147
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/147
  locator: Actual module metadata and complete gene-weight list; generated AI prose
    and activities not used; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/ecoli-module-147.raw
  accessed_at: '2026-11-04T06:20:35.701606Z'
  support: context_only
  summary: Module147 PAL 26 Del; function Unknown; 43 genes; b1842 weight 0.124483338
    exceeds threshold 0.058096464. Computational context only. Module147 has no regulator
    annotation and function Unknown; no mechanistic inference from its name.
  snapshot_sha256: e8e5afd15bd90077c45242d5060d3b2aa27b01269012b0be0ae0beb424caa2c5
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z receipt
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical runner unavailable/exit1 permission limitation; no fresh execution
    claimed. Fresh official API applicability/gene/module fallback above is separate.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-dna_polymerase_iii_clamp_loader_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-verify-receipt.json
  locator: Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T06:16:01.523240Z'
  support: supports
  summary: Actual exit0; 5 reviewed examples and5 COVERED typed nodes. Implemented
    identity/example coverage does not certify exact family grounding or full biological
    completeness.
  snapshot_sha256: 73f0e147bbe7d2d9eb0ae3db58eba6014b7b0505f86d0704fd47185d07eaf945
- evidence_id: micro-native-dna_polymerase_iii_clamp_loader_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-causal-receipt.json
  locator: Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-causal.log
    SHA256 aca3b51abc154a55cd6b3d81b01fc8a21768e3ec3940102586a9945621646d06
  accessed_at: '2026-11-04T06:16:01.974041Z'
  support: supports
  summary: Actual exit0; 5 reviewed examples and5 COVERED typed nodes. Implemented
    identity/example coverage does not certify exact family grounding or full biological
    completeness.
  snapshot_sha256: 7050e27a44b474ec4fe85b763705fc0008ffee0dd9df4771e3620998290bfbbd
- evidence_id: micro-native-dna_polymerase_iii_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-verify-receipt.json
  locator: Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T06:16:02.411476Z'
  support: supports
  summary: Actual exit0; 0 examples and0 typed GENE_OR_PROTEIN nodes; three STRUCTURE
    component nodes checked separately. Implemented identity/example coverage does
    not certify exact family grounding or full biological completeness.
  snapshot_sha256: 12af9d94a206260c5bf863caa49dc8d8235bf51ee739195120930d3d03088b39
- evidence_id: micro-native-dna_polymerase_iii_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-causal-receipt.json
  locator: Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-04T06:16:02.834438Z'
  support: supports
  summary: Actual exit0; 0 examples and0 typed GENE_OR_PROTEIN nodes; three STRUCTURE
    component nodes checked separately. Implemented identity/example coverage does
    not certify exact family grounding or full biological completeness.
  snapshot_sha256: e40f8baa69ecd571d319d54495ebc3ad8a5f34b8886a3408d17b57e9f3082a02
- evidence_id: micro-native-dna_polymerase_iii_core_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-verify-receipt.json
  locator: Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T06:16:04.590205Z'
  support: supports
  summary: Actual exit0; 3 reviewed examples and3 COVERED typed nodes. Implemented
    identity/example coverage does not certify exact family grounding or full biological
    completeness.
  snapshot_sha256: 764f2fd2c5f3f31bf2ab986dfe0ddfdb91537a59ad38c68e02dec27f3e942dc1
- evidence_id: micro-native-dna_polymerase_iii_core_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-causal-receipt.json
  locator: Actual command; complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-causal.log
    SHA256 622c34a9d261773a36cbd6c978ead78ec02d5fe3b0cb7c2e0e1c6688ceff466d
  accessed_at: '2026-11-04T06:16:05.020550Z'
  support: supports
  summary: Actual exit0; 3 reviewed examples and3 COVERED typed nodes. Implemented
    identity/example coverage does not certify exact family grounding or full biological
    completeness.
  snapshot_sha256: 46ec67f218bd34cec08991ecaa1172b61aa051a3826db004e4c805e8257ae48f
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/other/dna_replication_factor_a_complex.yaml
  locator: Entire maintained record at frozen source 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 875ef33eba1336b1bfd61e3c5bc9f0ade5f2c37a93d25793797fa5b9ac34c133
  summary: Complete current definition, hierarchy, components, all examples, taxonomy,
    functions, graphs, discussions and history independently read. RFA new examples/component
    and edge evidence/history substantively reassessed.
  support: supports
- evidence_id: plaque-original-3-yaml
  kind: prior_review
  reference: reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml
  locator: Complete historical paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 32bc2458f21adb0704d23ce69748bab13f6086cecaa7226cbd7af8d93bf3f1a2
  summary: Original scientific findings, actions and evidence scopes independently
    challenged against current sources; all old corpus commands remain historical.
  support: supports
- evidence_id: plaque-original-3-md
  kind: prior_review
  reference: reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.md
  locator: Complete historical paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 0f727e5db676f2120d360b9115d0081c405dbbdd9ceeb92d7b2bf9eb975c8626
  summary: Original scientific findings, actions and evidence scopes independently
    challenged against current sources; all old corpus commands remain historical.
  support: supports
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/other/dna_replication_factor_c_complex.yaml
  locator: Entire maintained record at frozen source 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 2b0c2b755fa48c66cfe831211cc2eb3abeb7691e2d7c16ddb938d3ff2698aa1f
  summary: Complete current definition, hierarchy, components, all examples, taxonomy,
    functions, graphs, discussions and history independently read. RFC target is byte-unchanged.
  support: supports
- evidence_id: plaque-original-4-yaml
  kind: prior_review
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
  locator: Complete historical paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 157b78894391f59a60728857bb07e85213b854d02c8a6be3e16cb1a3bc912ecc
  summary: Original scientific findings, actions and evidence scopes independently
    challenged against current sources; all old corpus commands remain historical.
  support: supports
- evidence_id: plaque-original-4-md
  kind: prior_review
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.md
  locator: Complete historical paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 42bf5580aa7b792128642e6023dbf12944a8c59d1ba3cdec6310d4c9144ac60d
  summary: Original scientific findings, actions and evidence scopes independently
    challenged against current sources; all old corpus commands remain historical.
  support: supports
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/other/dna_replication_preinitiation_complex.yaml
  locator: Entire maintained record at frozen source 25e2caa735be21e308f0eb02b9dc1bbdc3fb844e
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: d38de0da7f792e34b56e5ef225160a88221fb8a9b64e309e2b28f34bc7038b88
  summary: Complete current definition, hierarchy, components, all examples, taxonomy,
    functions, graphs, discussions and history independently read. New Cdc45 example/history
    substantively reassessed; existing mechanistic prose remains unchanged.
  support: supports
- evidence_id: plaque-original-5-yaml
  kind: prior_review
  reference: reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.yaml
  locator: Complete historical paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 77ac82339e48756ab3ecfbc24de8ea5209e698ad430f9dc6ddc2f7c0ea60b963
  summary: Original scientific findings, actions and evidence scopes independently
    challenged against current sources; all old corpus commands remain historical.
  support: supports
- evidence_id: plaque-original-5-md
  kind: prior_review
  reference: reviews/structured/20261022T055923Z-dna-replication-preinitiation-complex-audit/review.md
  locator: Complete historical paired observation and deterministic Markdown equivalence
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 5b00d000e58ff9288539a656bcbfc7ba53591e1dfa410ade943d555d6bf731ab
  summary: Original scientific findings, actions and evidence scopes independently
    challenged against current sources; all old corpus commands remain historical.
  support: supports
- evidence_id: plaque-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Exact structure/class grounding, formation versus viability, source scope
    and append-only history rules.
  support: supports
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Protein/complex identity, essentiality and graph semantics; complexes permitted
    under GENE_OR_PROTEIN.
  support: supports
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Positive molecular/pathway assertions trigger structured-source applicability
    regardless of expression wording.
  support: supports
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Issue-bearing immutable review successor and exact scoped historical lineage.
  support: supports
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Native evidence/assessment/lineage enums.
  support: supports
- evidence_id: plaque-checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
  summary: Complete bounded field-by-field evidence review; no forced optional examples.
  support: supports
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen local instructions/schema applied
  accessed_at: '2026-11-04T06:27:40.737917Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Distinguish descriptive membership/placement from sourced causal mechanisms.
  support: supports
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662,GO:0005663,GO:0031261,GO:0140513,GO:0003697,GO:0032991,GO:0005657,GO:0003689,GO:0006260,GO:0032993,GO:0005654,GO:0042555,GO:0000811
  locator: 'Thirteen requested terms: identities/definitions/synonyms/xrefs and relevant
    direct typed children only; unrelated children not judged; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go.raw'
  accessed_at: '2026-11-04T06:18:34.495361Z'
  snapshot_sha256: aa2de8390a1ee6ed65c370de3a77e03161506b64eace1416883667eb013d002e
  summary: Fresh active GO0005662/0005663/0031261 identities and exact definitions
    agree with their generic RFA/RFC/pre-IC classes. Direct relevant parent children
    support nuclear/protein-DNA class and fork/nucleoplasm parthood. GO0031261 lacks
    the record appended double-hexamer/kinase/CMG/bridge mechanism. GO0006260 is a
    process identity, not pre-IC-specific causal evidence.
  support: supports
- evidence_id: plaque-go-0005662-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/ancestors
  locator: Complete focal ancestor array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005662-ancestors.raw
  accessed_at: '2026-11-04T06:18:34.278810Z'
  snapshot_sha256: 0ffdf25679f5783a08c5219845d309fcaebd2648b4f7b96d98738da379ba0675
  summary: Focal current ancestor identity corroborates declared hierarchy; an ancestor
    list alone does not prove a direct edge.
  support: supports
- evidence_id: plaque-go-0005662-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005662/constraints
  locator: Complete focal taxonConstraints; negative blacklist entries not interpreted
    as biological experiment; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005662-constraints.raw
  accessed_at: '2026-11-04T06:18:34.649200Z'
  snapshot_sha256: 3e03b6425e2a7ecab10a7e02aa60db8121ced5b6d31ebc212d8f88725c2c4952
  summary: Focal native taxon constraints inspected; eukaryotic RFA/pre-IC scope and
    generic RFC scope are distinguished. This is not a prevalence census or a claim
    that archaeal RFC lacks homologous function.
  support: supports
- evidence_id: plaque-go-0005663-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/ancestors
  locator: Complete focal ancestor array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005663-ancestors.raw
  accessed_at: '2026-11-04T06:18:34.278769Z'
  snapshot_sha256: aad0653248faec07c468ea578bf8f6e034b9b7673ba9cbb2fc9b43c0f04de229
  summary: Focal current ancestor identity corroborates declared hierarchy; an ancestor
    list alone does not prove a direct edge.
  support: supports
- evidence_id: plaque-go-0005663-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005663/constraints
  locator: Complete focal taxonConstraints; negative blacklist entries not interpreted
    as biological experiment; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0005663-constraints.raw
  accessed_at: '2026-11-04T06:18:34.296892Z'
  snapshot_sha256: df450f113911ee9f69c32deb4a0a02218b21738e4d92ccec2f7891e1efea9931
  summary: Focal native taxon constraints inspected; eukaryotic RFA/pre-IC scope and
    generic RFC scope are distinguished. This is not a prevalence census or a claim
    that archaeal RFC lacks homologous function.
  support: supports
- evidence_id: plaque-go-0031261-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031261/ancestors
  locator: Complete focal ancestor array; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0031261-ancestors.raw
  accessed_at: '2026-11-04T06:18:34.299070Z'
  snapshot_sha256: d8fc6c672a0c0fcc01caa975dd0a2c9a251c5ec462359a3132e0739aaed2ea0a
  summary: Focal current ancestor identity corroborates declared hierarchy; an ancestor
    list alone does not prove a direct edge.
  support: supports
- evidence_id: plaque-go-0031261-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031261/constraints
  locator: Complete focal taxonConstraints; negative blacklist entries not interpreted
    as biological experiment; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/go-0031261-constraints.raw
  accessed_at: '2026-11-04T06:18:35.084591Z'
  snapshot_sha256: 1833ee1eb4e282fb7393c3e28ee00c29aab41b5b9192d393b43429399c799a00
  summary: Focal native taxon constraints inspected; eukaryotic RFA/pre-IC scope and
    generic RFC scope are distinguished. This is not a prevalence census or a claim
    that archaeal RFC lacks homologous function.
  support: supports
- evidence_id: plaque-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete identity, rank, aliases and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/tax-2759.raw
  accessed_at: '2026-11-04T06:18:34.910097Z'
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
  summary: Verified Eukaryota broad clade. Reference-strain accession does not identify
    every cited experimental strain.
  support: supports
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete identity, rank, aliases and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/tax-4932.raw
  accessed_at: '2026-11-04T06:18:34.923448Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: Verified Saccharomyces cerevisiae species. Reference-strain accession does
    not identify every cited experimental strain.
  support: supports
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete identity, rank, aliases and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/tax-559292.raw
  accessed_at: '2026-11-04T06:18:34.940359Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: Verified Saccharomyces cerevisiae S288C reference strain. Reference-strain
    accession does not identify every cited experimental strain.
  support: supports
- evidence_id: plaque-pmid-9242902
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9242902+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-9242902.raw
  accessed_at: '2026-11-04T06:18:35.099696Z'
  snapshot_sha256: 9bacde0d599fc0e13acf40d3ddb8af0e40091d5c7e843507a35e6285a63d2d96
  summary: Wold1997 secondary-review abstract supports conserved heterotrimer, approximate70/30/14
    size classes and nonspecific ssDNA binding/replication-repair roles. It is not
    a newly read review body or strain-specific yeast experiment.
  support: supports
- evidence_id: plaque-pmid-7651383
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7651383+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-7651383.raw
  accessed_at: '2026-11-04T06:18:35.282057Z'
  snapshot_sha256: 4a28be76289ba2b21d403c7c84f7874be3c59e9bc4549672d8ee140aa4778ce0
  summary: Cullmann1995 primary abstract reports five yeast RFC genes and homologous
    ATPase/PCNA role; gene-essential cell proliferation is not physical assembly necessity.
  support: supports
- evidence_id: plaque-pmid-8559655
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8559655+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-8559655.raw
  accessed_at: '2026-11-04T06:18:35.547936Z'
  snapshot_sha256: 3620a1b1363c05a553a0d416fffaa77afc9dfb87dfecce21b49db72a98a92afa
  summary: Gary/Burgers1995 primary abstract identifies RFC5/YBR0810 as integral fifth
    yeast subunit via co-overexpression of RFC1–5; viability and E.coli overexpression
    do not define natural-host formation necessity.
  support: supports
- evidence_id: plaque-pmid-14614842
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-14614842.raw
  accessed_at: '2026-11-04T06:18:35.546904Z'
  snapshot_sha256: ec83bbe95827445112114e28dc9585ab36351100842feb0e84d23002dd45fc58
  summary: Kim/MacNeill2003 is a secondary review on RFC family variants; used as
    bibliographic/context evidence, not five-gene yeast experiment.
  support: supports
- evidence_id: plaque-pmid-14646196
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14646196+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-14646196.raw
  accessed_at: '2026-11-04T06:18:35.563213Z'
  snapshot_sha256: 538e0893cc937ef02de3d231611406d606989ee46936bab7f0bbade861ee2c38
  summary: Kitabayashi2003 primary abstract studies Thermococcus kodakaraensis KOD1
    recombinant RFC; archaeal host is not substituted for budding yeast.
  support: supports
- evidence_id: plaque-pmid-16172520
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16172520+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-16172520.raw
  accessed_at: '2026-11-04T06:18:35.692417Z'
  snapshot_sha256: 3db8442e0a2a2c849b731da0ef752f1aee07cc4f8ca5f0dfb0622e3f269f682c
  summary: Nishida2005 primary abstract studies Pyrococcus furiosus RFC subunit C-terminal
    truncations, ternary-complex stability and loading, not yeast RFC1–5 assembly.
  support: supports
- evidence_id: plaque-pmid-12730134
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12730134+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-12730134.raw
  accessed_at: '2026-11-04T06:18:35.728532Z'
  snapshot_sha256: d3e75c6acc87221e503a7112fa6aefe92baa817ab9d90d744dc28cdc52f1634c
  summary: Takayama2003 primary abstract identifies budding-yeast GINS and conditional
    origin recruitment; full body is separately evidenced.
  support: supports
- evidence_id: plaque-pmid-8901577
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8901577+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact MED PMID query, metadata/authors/year/DOI and complete indexed abstract;
    no body or figures from this query; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/pmid-8901577.raw
  accessed_at: '2026-11-04T06:18:35.886331Z'
  snapshot_sha256: 7682552d636070825401643f711ec1bc56db116047f4e23e34ff23e7d12ae99c
  summary: Hopwood/Dalton1996 primary abstract reports Cdc45 replication initiation,
    physical association with Cdc46/Mcm5 and cell-cycle-independent localization;
    not a direct Mcm2–Mcm5 bridge or full pre-IC depletion assay.
  support: supports
- evidence_id: plaque-brill1991-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:1885001%20AND%20SRC:MED&format=json&resultType=core&pageSize=5
  locator: Unique MED1885001, complete primary abstract and metadata; publisher fulltext403;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/brill1991-meta.raw
  accessed_at: '2026-11-04T06:24:21.398996Z'
  snapshot_sha256: c05d89feaac4ad21edc39425eebbbd470788e637d74fbaf46bba23d0d58643a4
  summary: Brill/Stillman1991 primary abstract independently identifies the three
    yeast RFA genes and homologous three-subunit complex, gene essentiality and regulated
    transcription. It supports the added yeast gene/composition context, not precise
    S288C experimental provenance or physical formation necessity.
  support: supports
- evidence_id: plaque-takayama2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC196052/
  locator: Complete Results sec2–9 including Fig1–7 text captions, Discussion sec11–13,
    Methods sec15–22; no figure pixels, Supplementary Table1 or raw data; strain identifiers
    retained as declared cultures without assigning S288C; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/takayama2003-pmc.raw
  accessed_at: '2026-11-04T06:18:48.126890Z'
  snapshot_sha256: f785ef8cc3d4bf3539dcbb0f0ff4ca74d524cdd193e4bf3562599ce6907daca5
  summary: 'Fresh genuine primary HTML: GINS four-member purification and conditional
    Sld5 mutant recovery/viability/replication, Psf1-origin recruitment and dependencies
    on Sld3/Dpb11, Cdc45 chromatin binding in psf1-1. Discussion explicitly distinguishes
    observed recruitment from proposed macromolecular model and alternative elongation
    explanations. No demonstrated loaded double-hexamer, specific modern kinase-target
    chain or Mcm2–Mcm5 bridging mechanism.'
  support: supports
- evidence_id: plaque-cullmann1995-pdf
  kind: primary_source
  reference: https://repository.cshl.edu/id/eprint/24950/1/Characterization%20of%20the%20five%20replication%20factor%20C.pdf
  locator: Extracted text pp4661–4663,4665 and4668–4669 incl Table1/Fig8 text captions;
    no alignment image analysis or figure pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/cullmann1995-pdf.raw
  accessed_at: '2026-11-04T06:18:55.390976Z'
  snapshot_sha256: 87555bf179702af221aec2fb878236eaeebc20821fb52ad62d1e9c2eb1f9253f
  summary: Fresh genuine author-repository PDF independently confirms yeast five-subunit
    cloning, RFC1/CDC44 identity, subunit homologs and PCNA function. Methods uses
    BJ926 purification and W303/W937 derivatives; gene disruptions test viability,
    not universal structure formation. Broad RFC2–5 similarity is not exact individual
    family grounding.
  support: supports
- evidence_id: plaque-gary1995-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC307503/
  locator: Title/authors/DOI/complete abstract only; scan links not equivalent to
    reading scans; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gary1995-pmc.raw
  accessed_at: '2026-11-04T06:18:48.426376Z'
  snapshot_sha256: b00d4f2dfb512c4feaf722cfb676bab225bce0dcc9540145ef21ff0cc41405d4
  summary: Correct legacy primary landing contains complete RFC5 abstract and scan
    links; no newly inspected page pixels or full Methods certified.
  support: supports
- evidence_id: plaque-hopwood1996-correct-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC37987/
  locator: Exact title/metadata and complete abstract only; no full paper pages or
    image measurement; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/hopwood1996-correct-pmc.raw
  accessed_at: '2026-11-04T06:22:40.103547Z'
  snapshot_sha256: 1405909b67c7e2b611fc1dd0ddeb368145e9245a2860431443f05ec80459cb45
  summary: Correct legacy PMC37987 title/abstract matches PMID8901577 and nucleus
    annotation context; body scan links were not inspected as pixels.
  support: supports
- evidence_id: plaque-wold1997-publisher
  kind: validation
  reference: https://www.annualreviews.org/doi/10.1146/annurev.biochem.66.1.61
  locator: Actual status/response identity only; excluded from scientific support;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/wold1997-publisher.raw
  accessed_at: '2026-11-04T06:18:48.301102Z'
  snapshot_sha256: 60e1a437c2d9352aecac91dea5878eafd447a7514777f6347a391e881df53f23
  summary: 403 challenge, not secondary-review body
  support: context_only
- evidence_id: plaque-brill1991-pdf
  kind: validation
  reference: https://genesdev.cshlp.org/content/5/9/1589.full.pdf
  locator: Actual status/response identity only; excluded from scientific support;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/brill1991-pdf.raw
  accessed_at: '2026-11-04T06:24:21.475723Z'
  snapshot_sha256: f1ad3fe8d6dd3003c8599575b3d3228f9ef20674fdde9b74b899c3e3b819a65e
  summary: 403 challenge, not primary PDF
  support: context_only
- evidence_id: plaque-takayama2003-s3
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC196052.1/PMC196052.1.xml
  locator: Actual status/response identity only; excluded from scientific support;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/takayama2003-s3.raw
  accessed_at: '2026-11-04T06:18:48.171753Z'
  snapshot_sha256: 7f4d13dea4ddab2a86702e7fb60497d52361f80e8a1f4ae07ee5b03f336e2c23
  summary: 404 response; genuine PMC HTML separately retrieved
  support: context_only
- evidence_id: plaque-ipr-IPR008591
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008591/
  locator: Actual status/response identity only; excluded from scientific support;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR008591.raw
  accessed_at: '2026-11-04T06:18:47.624313Z'
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
  summary: initial429; subsequent distinct retry succeeded
  support: context_only
- evidence_id: plaque-ipr-IPR005339
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005339/
  locator: Actual status/response identity only; excluded from scientific support;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR005339.raw
  accessed_at: '2026-11-04T06:18:47.723208Z'
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
  summary: initial429; subsequent distinct retry succeeded
  support: context_only
- evidence_id: plaque-hopwood1996-pmc
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC26461/
  locator: Actual status/response identity only; excluded from scientific support;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/hopwood1996-pmc.raw
  accessed_at: '2026-11-04T06:18:48.498274Z'
  snapshot_sha256: 19e56e99b1972243dcd314afc619901d80f2159fa81beb48c15bcf9dbe76f0c8
  summary: initial mistaken PMC26461 lead resolves to an unrelated GPCR paper; title
    check rejected it and no scientific content from it is used
  support: context_only
- evidence_id: plaque-up-P22336
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P22336.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P22336.raw
  accessed_at: '2026-11-04T06:18:36.193613Z'
  snapshot_sha256: 1106364d2762bb4e4fb85393258363f7e5cdad809a7edc46880dc0ee2ffe27ca
  summary: Current reviewed P22336 primary gene RFA1, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFA1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFA1.raw
  accessed_at: '2026-11-04T06:18:44.082492Z'
  snapshot_sha256: 8c2fe65f740f70e9fd298baac32dd53a42217d897ee00182b104a29fa5b8519a
  summary: 'Exactly one current reviewed primary-gene query hit: P22336; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFA1) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:44.082492Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P26754
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P26754.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P26754.raw
  accessed_at: '2026-11-04T06:18:36.202949Z'
  snapshot_sha256: 2abc063b70810945fce1f75089d5189929456b87e05b6d337bf626587e37a295
  summary: Current reviewed P26754 primary gene RFA2, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFA2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFA2.raw
  accessed_at: '2026-11-04T06:18:40.864008Z'
  snapshot_sha256: 4f1cb7721a54564cc98d6b67c540fdce864cee0eb6143552ccf7c1720572ea5f
  summary: 'Exactly one current reviewed primary-gene query hit: P26754; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFA2) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:40.864008Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P26755
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P26755.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P26755.raw
  accessed_at: '2026-11-04T06:18:38.754339Z'
  snapshot_sha256: 27c4e73fb9d25a0c9f14e5fee50a233c6082eedb17503d0f6005e15d422251b8
  summary: Current reviewed P26755 primary gene RFA3, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFA3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFA3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFA3.raw
  accessed_at: '2026-11-04T06:18:44.774319Z'
  snapshot_sha256: 49c4cd5589604dc7e1bf6f22536bd4a4530a8aefae36bc90b625396d76de3d0a
  summary: 'Exactly one current reviewed primary-gene query hit: P26755; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFA3) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:44.774319Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P38630
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38630.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P38630.raw
  accessed_at: '2026-11-04T06:18:39.765648Z'
  snapshot_sha256: 455f56fd2d2492ed2be545915de9082d562a479ed379d6de1a161759d46326f4
  summary: Current reviewed P38630 primary gene RFC1, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC1.raw
  accessed_at: '2026-11-04T06:18:41.930781Z'
  snapshot_sha256: c81cae2d85f5ab0ed99a79f10d8ec002beba901230284d143d22c2314b05b096
  summary: 'Exactly one current reviewed primary-gene query hit: P38630; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFC1) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:41.930781Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P40348
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40348.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P40348.raw
  accessed_at: '2026-11-04T06:18:36.727677Z'
  snapshot_sha256: cd48db2abc9d05e4a2f8f7736b0aced77e8baa2465fb6a839d4f9e8ed95db94e
  summary: Current reviewed P40348 primary gene RFC2, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFC2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC2.raw
  accessed_at: '2026-11-04T06:18:45.887830Z'
  snapshot_sha256: 5d37684d32d00b6803a2cbe7289849926576cd3f08cc74f6dd6ee2b3c1821068
  summary: 'Exactly one current reviewed primary-gene query hit: P40348; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFC2) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:45.887830Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P38629
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38629.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P38629.raw
  accessed_at: '2026-11-04T06:18:36.725482Z'
  snapshot_sha256: 057ded2799f8c2aaf4cd34a49b0bd062aae33e6e6aa9ab81ec59b7c7d74937dd
  summary: Current reviewed P38629 primary gene RFC3, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFC3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC3.raw
  accessed_at: '2026-11-04T06:18:42.757741Z'
  snapshot_sha256: a84d7bf13eddb61707649c22403a1d9540d4585cd07d07bb31fcbd5f54cff2c3
  summary: 'Exactly one current reviewed primary-gene query hit: P38629; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFC3) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:42.757741Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P40339
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40339.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P40339.raw
  accessed_at: '2026-11-04T06:18:37.731764Z'
  snapshot_sha256: 09609fcf78c540ff8073114b66b849691895e1fc7de9e81219d81dc51fcc35d7
  summary: Current reviewed P40339 primary gene RFC4, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFC4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC4%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC4.raw
  accessed_at: '2026-11-04T06:18:46.849209Z'
  snapshot_sha256: e4ac27ef43308dc3dd4c47939cb4856e61e23e412f8815e785cfb8d758e80a5c
  summary: 'Exactly one current reviewed primary-gene query hit: P40339; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFC4) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:46.849209Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P38251
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38251.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P38251.raw
  accessed_at: '2026-11-04T06:18:38.654970Z'
  snapshot_sha256: bebaced0b8314c495257a26b5d1357bde108a903ac25fc337c51d4970294ff06
  summary: Current reviewed P38251 primary gene RFC5, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-RFC5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARFC5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-RFC5.raw
  accessed_at: '2026-11-04T06:18:47.895411Z'
  snapshot_sha256: 7cfa80c9ae09adeac609a00eb5e3ddcecb79fc26d7ce7848ce2f6f772cfcaabb
  summary: 'Exactly one current reviewed primary-gene query hit: P38251; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:RFC5) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:47.895411Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-Q08032
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08032.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q08032.raw
  accessed_at: '2026-11-04T06:18:40.870599Z'
  snapshot_sha256: 3db4d998bc94ca58f1b2551d53a37bad9e4f52f76ee7958ab7dc75ad6e8c2bde
  summary: Current reviewed Q08032 primary gene CDC45, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-CDC45
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACDC45%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-CDC45.raw
  accessed_at: '2026-11-04T06:18:43.964431Z'
  snapshot_sha256: efc064cfd5d81f5633b581bb83454b905eccdc8d46a8cb5d0430872c3bee9dc7
  summary: 'Exactly one current reviewed primary-gene query hit: Q08032; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:CDC45) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:43.964431Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-Q03406
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03406.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q03406.raw
  accessed_at: '2026-11-04T06:18:37.937976Z'
  snapshot_sha256: 0f0ab1e1af41bb24cee36f864ebc31dd7545b0bb29a248a5cc47c3d3e1af1494
  summary: Current reviewed Q03406 primary gene SLD5, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-SLD5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASLD5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-SLD5.raw
  accessed_at: '2026-11-04T06:18:44.942431Z'
  snapshot_sha256: 7368ce9776d8376e6b65508a94e4db0a020b1e79807eee71b6f045dddcbd3721
  summary: 'Exactly one current reviewed primary-gene query hit: Q03406; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:SLD5) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:44.942431Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-Q12488
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12488.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q12488.raw
  accessed_at: '2026-11-04T06:18:39.765686Z'
  snapshot_sha256: d2bc83c4f49cb856f2fbf59ea40455ddc5180c1d30345c829f945ba34ea5cf42
  summary: Current reviewed Q12488 primary gene PSF1, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-PSF1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-PSF1.raw
  accessed_at: '2026-11-04T06:18:45.844643Z'
  snapshot_sha256: e80a00344596c83719b3207a5bdf34a416aa42fef76201dfe48cd6f4943922cc
  summary: 'Exactly one current reviewed primary-gene query hit: Q12488; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:PSF1) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:45.844643Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-P40359
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40359.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-P40359.raw
  accessed_at: '2026-11-04T06:18:41.730228Z'
  snapshot_sha256: a0372e9adda4d46ee4b088e3bac6455b0dcfa50df134106ee25d61c0a2c82689
  summary: Current reviewed P40359 primary gene PSF2, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-PSF2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-PSF2.raw
  accessed_at: '2026-11-04T06:18:46.760835Z'
  snapshot_sha256: f623cb2d7331785b5dc3c72117083190c48927b7e740098a750f9d4f52698512
  summary: 'Exactly one current reviewed primary-gene query hit: P40359; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:PSF2) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:46.760835Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-up-Q12146
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12146.json
  locator: Identity/status/primary gene and aliases/locus/taxon; SUBUNIT and SUBCELLULAR
    LOCATION evidence; exact InterPro entries; no inference from unrelated functions;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/up-Q12146.raw
  accessed_at: '2026-11-04T06:18:42.690517Z'
  snapshot_sha256: 72fc7e1d00fc0c8dee9b0e065a7683decb0c78a9cba00cf8252da2fe27c3bf3c
  summary: Current reviewed Q12146 primary gene PSF3, exact S288C559292, locus and
    whole-protein identity checked; SUBUNIT/localization/evidence joins and InterPro
    xrefs independently read. Native localization or reference accession alone is
    not formation proof.
  support: supports
- evidence_id: plaque-gene-PSF3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APSF3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete bounded native query response; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/gene-PSF3.raw
  accessed_at: '2026-11-04T06:18:47.827706Z'
  snapshot_sha256: d7cd7f8989fc603bab14abc9c2d052cb1bd46a9090022b39abba5a11cdaf1887
  summary: 'Exactly one current reviewed primary-gene query hit: Q12146; identity
    only, not physical assembly evidence.'
  support: supports
  search_scope: UniProtKB query (gene_exact:PSF3) AND (taxonomy_id:559292) AND (reviewed:true);
    size100; actual 2026-11-04T06:18:47.827706Z; returned one result, no pagination
    omitted or other organism/strain claimed.
- evidence_id: plaque-ipr-IPR004591
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004591/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR004591.raw
  accessed_at: '2026-11-04T06:18:46.443538Z'
  snapshot_sha256: 76b40296040dc3366ab7f658ee76399d1bfa7318da5a079ac9e43c593a03fa4f
  summary: Native type family and name Replication factor A protein 1 independently
    checked against same-class UniProt xrefs. Exact named whole-protein family; no
    domain, narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR014646
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014646/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR014646.raw
  accessed_at: '2026-11-04T06:18:46.491255Z'
  snapshot_sha256: e9df1d9b162d769daf0d3d97fecbaabf3f3152db6cb8ee07c9a11369095f387f
  summary: Native type family and name Replication factor A protein 2 independently
    checked against same-class UniProt xrefs. Exact named whole-protein family; no
    domain, narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR013970
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013970/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR013970.raw
  accessed_at: '2026-11-04T06:18:47.043785Z'
  snapshot_sha256: 594508b691b6fc97c2ca6d1beb10fb5996aaa7c468f730873c4e4d02f7bbc7a2
  summary: Native type family and name Replication factor A protein 3 independently
    checked against same-class UniProt xrefs. Exact named whole-protein family; no
    domain, narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR012178
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012178/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR012178.raw
  accessed_at: '2026-11-04T06:18:47.114105Z'
  snapshot_sha256: e9520dc4e483905f19cbb30aeae7961e8dd49e1c102d88869da21b19b7dcc4e5
  summary: Native type family and name Replication factor C subunit 1 independently
    checked against same-class UniProt xrefs. Exact named whole-protein family; no
    domain, narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR050238
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR050238.raw
  accessed_at: '2026-11-04T06:18:47.356709Z'
  snapshot_sha256: 20cc681dc2b5aa75e096f21d298105d7ac05cc910f786be9e1f63ae05a72dbc0
  summary: Native type family and name DNA Replication and Repair Clamp Loader Complex
    independently checked against same-class UniProt xrefs. Broad clamp-loader family
    is not exact RFC2–5 identity; llm-marked descriptive paragraph excluded as scientific
    evidence.
  support: supports
- evidence_id: plaque-ipr-IPR013748
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013748/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR013748.raw
  accessed_at: '2026-11-04T06:19:08.702448Z'
  snapshot_sha256: 57bf4734514098173ad40fec18cbe6616de4603df0cd5226f6c97ffb42f339a7
  summary: Native type domain and name Replication factor C, C-terminal independently
    checked against same-class UniProt xrefs. C-terminal domain is not an entire RFC
    subunit class.
  support: supports
- evidence_id: plaque-ipr-IPR008591-retry
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008591/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR008591-retry.raw
  accessed_at: '2026-11-04T06:22:40.760012Z'
  snapshot_sha256: 85e8cd86a991862236bac423a4b78a8657b441ab90bfc81b4db9fe4962302caf
  summary: Native type family and name GINS complex subunit Sld5 independently checked
    against same-class UniProt xrefs. Exact named whole-protein family; no domain,
    narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR005339-retry
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005339/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR005339-retry.raw
  accessed_at: '2026-11-04T06:22:41.364718Z'
  snapshot_sha256: 121f89ec73f3f03cd822ae44de3d8f88b8d0c03e2d0cace8bdbec8dc8a758196
  summary: Native type family and name GINS complex, subunit Psf1 independently checked
    against same-class UniProt xrefs. Exact named whole-protein family; no domain,
    narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR007257
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007257/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR007257.raw
  accessed_at: '2026-11-04T06:18:47.991132Z'
  snapshot_sha256: da6e464787aa773567fa1b673d8d7428ffc4637302a642144f0fd11d389636a4
  summary: Native type family and name DNA replication complex GINS protein Psf2 independently
    checked against same-class UniProt xrefs. Exact named whole-protein family; no
    domain, narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR010492
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010492/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR010492.raw
  accessed_at: '2026-11-04T06:18:48.227640Z'
  snapshot_sha256: fc7bab38aac1ebe05715d0a7a9ff819d2de8abb1c981d9f1813c8064229268eb
  summary: Native type family and name GINS complex, subunit Psf3 independently checked
    against same-class UniProt xrefs. Exact named whole-protein family; no domain,
    narrow species subgroup or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-ipr-IPR003874
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003874/
  locator: Native accession/type/name/integrated signatures and exact reviewed-protein
    xrefs; broad/obsolete historical explanatory prose not used to support modern
    mechanism; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/ipr-IPR003874.raw
  accessed_at: '2026-11-04T06:18:48.329748Z'
  snapshot_sha256: 580caef553ebf001a0fece61778bae151bde22735cc960091381b8c90b4a4646
  summary: Native type family and name CDC45 independently checked against same-class
    UniProt xrefs. Exact named whole-protein family; no domain, narrow species subgroup
    or mechanistic prose substituted for the class.
  support: supports
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Fresh same-PR complete official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T06:16:25.827407Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: All20 current organism rows/28 organism-dataset pairs independently read.
    No Saccharomyces/eukaryotic matched natural host; bacterial expression hosts and
    unrelated archaeal taxa are not proxies.
  support: context_only
- evidence_id: plaque-catalogue-search
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Fresh same-PR complete official catalogue independently reread; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T06:16:25.827407Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No covered yeast dataset in this bounded official catalogue. This is coverage
    limitation, not biological absence, and no foreign-host downstream module query
    was made.
  support: context_only
  search_scope: Official iModulonDB /api/datasets complete20rows/28pairs at 2026-11-04T06:16:25.827407Z;
    screen Saccharomyces,cerevisiae,S288C,W303,W937,BJ926 and eukaryotic hosts; no
    broader database claim.
- evidence_id: plaque-historical-adapter-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Original historical runner receipt only
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Historical Nov3 00:49Z exit1 PermissionError reading pyvenv.cfg; no fresh
    runner invocation claimed. Current source fallback is independently evidenced.
  support: context_only
- evidence_id: plaque-original-current-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-plaque/originals-current-proof.json
  locator: Three original validate/render pairs;42 historical input occurrences;47
    current source/worktree input hashes
  accessed_at: '2026-11-04T06:19:31.070280Z'
  snapshot_sha256: b637bc042268cd0f34f7099e6ad9fda9620407c461a51bc46298b986f5f2762e
  summary: Original YAML validation and deterministic Markdown match; historical inputs
    hash against original source, including canonical CLAUDE symlink. RFA/pre-IC stale
    deltas are independently assessed, RFC unchanged.
  support: supports
- evidence_id: plaque-historical-micro51-wold1997-publisher
  kind: validation
  reference: reviews/structured/20261022T055922Z-dna-replication-factor-a-complex-audit/review.yaml
  locator: Original evidence#micro51-wold1997-publisher; historical URL https://doi.org/10.1146/annurev.biochem.66.1.61;
    historical responseSHA 4b1b1d39c74c3569e6ff00ffd6acd584d2cfd08cd32629ce3d45b6f10af463d9
  accessed_at: '2026-10-22T05:42:48.434702Z'
  snapshot_sha256: 4b1b1d39c74c3569e6ff00ffd6acd584d2cfd08cd32629ce3d45b6f10af463d9
  summary: 'Historical recorded observation: The retained publisher request returned
    HTTP403 challenge content, not a review main body. Original kind database/context_only
    is access-log misclassification; correct to validation/context_only in successor.
    Original response bytes are not newly certified by rereading YAML.'
  support: context_only
- evidence_id: plaque-historical-micro51-kim2003-publisher
  kind: validation
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
  locator: Original evidence#micro51-kim2003-publisher; historical URL https://doi.org/10.1016/j.cub.2003.10.048;
    historical responseSHA 35892ac737a1148299b5602719dc71f7b24628eca283b1e019befde45d6f5911
  accessed_at: '2026-10-22T05:42:48.439943Z'
  snapshot_sha256: 35892ac737a1148299b5602719dc71f7b24628eca283b1e019befde45d6f5911
  summary: 'Historical recorded observation: HTTP200 contains a LinkingHub Redirecting
    locator page, not the article body. Original kind database/context_only is access-log
    misclassification; correct to validation/context_only in successor. Original response
    bytes are not newly certified by rereading YAML.'
  support: context_only
- evidence_id: plaque-historical-micro51-kitabayashi2003-publisher
  kind: validation
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
  locator: Original evidence#micro51-kitabayashi2003-publisher; historical URL https://doi.org/10.1271/bbb.67.2373;
    historical responseSHA f5174970bceb22789d2ba517951ddb719092eedd77cb453303ff8c74c6592e73
  accessed_at: '2026-10-22T05:42:48.634215Z'
  snapshot_sha256: f5174970bceb22789d2ba517951ddb719092eedd77cb453303ff8c74c6592e73
  summary: 'Historical recorded observation: HTTP403 challenge response does not supply
    the article main body. Original kind database/context_only is access-log misclassification;
    correct to validation/context_only in successor. Original response bytes are not
    newly certified by rereading YAML.'
  support: context_only
- evidence_id: plaque-historical-micro51-cullmann1995-pdf
  kind: validation
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
  locator: Original evidence#micro51-cullmann1995-pdf; historical URL https://www.ncbi.nlm.nih.gov/pmc/articles/PMC230709/pdf/154661.pdf;
    historical responseSHA cf16e9fdeee914a3db18be8e6daebbba224fbb62b67af4b24cf2e553b6c2c46b
  accessed_at: '2026-10-22T05:44:01.248943Z'
  snapshot_sha256: cf16e9fdeee914a3db18be8e6daebbba224fbb62b67af4b24cf2e553b6c2c46b
  summary: 'Historical recorded observation: HTTP200 contains Preparing to download
    proof-of-work HTML, not PDF pages; the separately captured CSHL PDF is the genuine
    body. Original kind database/context_only is access-log misclassification; correct
    to validation/context_only in successor. Original response bytes are not newly
    certified by rereading YAML.'
  support: context_only
- evidence_id: plaque-historical-micro51-gary1995-pdf
  kind: validation
  reference: reviews/structured/20261022T055923Z-dna-replication-factor-c-complex-audit/review.yaml
  locator: Original evidence#micro51-gary1995-pdf; historical URL https://www.ncbi.nlm.nih.gov/pmc/articles/PMC307503/pdf/nar00024-0060.pdf;
    historical responseSHA 9831ae1d0a9d6412e90a59379b4c358a0c6fcc28dd4e260c0798239cb76604d9
  accessed_at: '2026-10-22T05:44:01.249493Z'
  snapshot_sha256: 9831ae1d0a9d6412e90a59379b4c358a0c6fcc28dd4e260c0798239cb76604d9
  summary: 'Historical recorded observation: HTTP200 contains Preparing to download
    proof-of-work HTML, not PDF pages; original page scans provide the actually inspected
    body. Original kind database/context_only is access-log misclassification; correct
    to validation/context_only in successor. Original response bytes are not newly
    certified by rereading YAML.'
  support: context_only
- evidence_id: plaque-native-dna_replication_factor_a_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/dna_replication_factor_a_complex.yaml', '--verify']; log
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T06:16:06.274483Z'
  snapshot_sha256: f2d20e15986a2d073dc179d8a7cafd0eb10cdb89403ed3ac421dc0c23fedacd7
  summary: Actual source-bound exit0. Direct current inventory 3 reviewed examples/3
    typed nodes; all COVERED. This verifies identity/coverage, not class grounding,
    mechanism or formation necessity.
  support: supports
- evidence_id: plaque-native-dna_replication_factor_a_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/dna_replication_factor_a_complex.yaml', '--causal-graphs'];
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-causal.log
    SHA256 7aa8052a4e7f0766e31305e034ff3844deb0b33aa46c8859caf42dad6b98b57c
  accessed_at: '2026-11-04T06:16:06.731473Z'
  snapshot_sha256: f5adb694437d6b5ee9ed62de3049bf6e1774ff6b9e84811f95fe4276819c7ce1
  summary: Actual source-bound exit0. Direct current inventory 3 reviewed examples/3
    typed nodes; all COVERED. This verifies identity/coverage, not class grounding,
    mechanism or formation necessity.
  support: supports
- evidence_id: plaque-native-dna_replication_factor_c_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/dna_replication_factor_c_complex.yaml', '--verify']; log
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T06:16:08.125330Z'
  snapshot_sha256: b8bda3c43ec756f2161dbcfecd19fca321000a69c027b987401592e96285863a
  summary: Actual source-bound exit0. Direct current inventory 5 reviewed examples/5
    typed nodes; all COVERED. This verifies identity/coverage, not class grounding,
    mechanism or formation necessity.
  support: supports
- evidence_id: plaque-native-dna_replication_factor_c_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/dna_replication_factor_c_complex.yaml', '--causal-graphs'];
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-causal.log
    SHA256 8fe53b9e87565355d70e5600509e38c4dfda6fcd88d47a294b9dfde6859f89f1
  accessed_at: '2026-11-04T06:16:08.598249Z'
  snapshot_sha256: b4daf8b76bec3d07ccd5179ac80279a622c215af9180f7776345080173126df4
  summary: Actual source-bound exit0. Direct current inventory 5 reviewed examples/5
    typed nodes; all COVERED. This verifies identity/coverage, not class grounding,
    mechanism or formation necessity.
  support: supports
- evidence_id: plaque-native-dna_replication_preinitiation_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/dna_replication_preinitiation_complex.yaml', '--verify'];
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T06:16:10.125946Z'
  snapshot_sha256: 0ac4996ea1f4af413effce8c63e409de14b92c43263069cc405b08e9e1a3200b
  summary: Actual source-bound exit0. Direct current inventory 5 reviewed examples/5
    typed nodes; all COVERED. This verifies identity/coverage, not class grounding,
    mechanism or formation necessity.
  support: supports
- evidence_id: plaque-native-dna_replication_preinitiation_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/dna_replication_preinitiation_complex.yaml', '--causal-graphs'];
    log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-causal.log
    SHA256 c74a99b2a3d0d028e6c80171343313ea4b2db7f9424ad9185ccfed9c2f89fba7
  accessed_at: '2026-11-04T06:16:10.579658Z'
  snapshot_sha256: e2e7dadf739af8275173174673c51eaf758378bbac680d50b37f1dd7c717531f
  summary: Actual source-bound exit0. Direct current inventory 5 reviewed examples/5
    typed nodes; all COVERED. This verifies identity/coverage, not class grounding,
    mechanism or formation necessity.
  support: supports
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Full-record scientific evidence and structured-source cross-checks
  summary: Positive named genes, protein classes, pathways and stress responses trigger
    coverage assessment; expression-only exemptions are insufficient. Official source
    fallback may be used when the runner is unavailable.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components and Discussions
  summary: REVIEWED_LABEL_ONLY means an exact term remains unresolved; verified exact
    families differ from taxon-specific examples. Essentiality concerns formation,
    not viability. Dated rationale/history is append-only.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component, protein example, essentiality, graph and presence contracts
  summary: Protein families/classes and whole subcomplexes are legitimate distinct
    objects. Native GENE_OR_PROTEIN permits appropriate protein-complex scope; no
    enum-only or optional-example defect is manufactured. Formation necessity must
    retain experimental conditions.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph endpoints, causal scope and nonmechanistic boundaries
  summary: Membership, localization, enzymatic function, complex formation and organism
    viability are distinct claims.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Actual source scope and access tiers
  summary: Authority metadata, primary body/abstract, secondary review and failed
    access are distinct evidence scopes; uninspected images and supplements are not
    certified.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: ReviewEvidence and FindingReference
  summary: HTTP failure is validation context. Inherited findings retain exact repository/review/finding
    identity and current disposition.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0009340,GO%3A0009330,GO%3A0032991,GO%3A0003918,GO%3A1990102,GO%3A1990077,GO%3A1990101,GO%3A1990125,GO%3A0006270,GO%3A1990157,GO%3A1990099,GO%3A1990100,GO%3A1990084,GO%3A1990078,GO%3A1990083,GO%3A1990085,GO%3A0032297
  locator: All17 requested current IDs, labels, active statuses, definitions, synonyms,
    citation xrefs and relevant typed children; unrelated children not used
  summary: Exact four complex classes, typed parents, DiaA/DnaA-oriC/DnaB-DnaC boundaries
    and function terms match. GO0009340 retains heterodimeric wording contradicted
    by the primary 2:2 result; the maintained definition avoids it. GO1990099 excludes
    primase from the pre-primosome; primosome parentage does not add DnaG to every
    early intermediate.
  accessed_at: '2026-11-04T06:18:30.572391Z'
  support: supports
  snapshot_sha256: 20acc6fb4f33b15254c0883eb10baca7a549febfef3948d31b5eafda0771038b
- evidence_id: septin-so
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/so/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FSO_0000953
  locator: Complete native SO0000953 OLS label, definition, active status and synonym
  summary: SO0000953 oriC is an origin of bacterial chromosome replication, matching
    the two declared origin-DNA classes, rather than generic DNA material.
  accessed_at: '2026-11-04T06:18:30.473288Z'
  support: supports
  snapshot_sha256: d64a9c22b7c52cef08f25cfbe676d3c88458ac7ec7f09850d25f3ebc82051030
- evidence_id: septin-ipr-IPR001957
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Full DnaA family, distinct from its broader DnaA-like parent and Hda sibling.
  accessed_at: '2026-11-04T06:18:30.469599Z'
  support: supports
  snapshot_sha256: 364ea5ab4304d290b099574c7f9527e5577eefec2872f8fc2adde34de7eb2fc2
- evidence_id: septin-retry-IPR023070
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023070/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Exact DiaA family, distinct from broader GmhA/DiaA and its phosphoheptose-isomerase
    sibling.
  accessed_at: '2026-11-04T06:19:17.832599Z'
  support: supports
  snapshot_sha256: c5275aa409e4b1a32d39fa8f2a4391a55b775b1ae202b101e475f3b14d298ca2
- evidence_id: septin-ipr-IPR002177
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002177/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Full Dps family, with narrower gammaproteobacterial child; ferritin-like
    fold alone is broader. Family membership does not prove every member binds DnaA.
  accessed_at: '2026-11-04T06:18:30.464299Z'
  support: supports
  snapshot_sha256: 6b6fa5016c1c5e5c3eff6fadd9b113bf86cd6b1de554c8e2d485546ef95617a7
- evidence_id: septin-retry-IPR005742
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005742/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Gram-negative ParC family is narrower than the generic bacterial ParC component.
  accessed_at: '2026-11-04T06:19:18.203009Z'
  support: supports
  snapshot_sha256: 6071e1005b83c8ef30ac399047c0feb257d967ad29b3b14ee8732e150c447946
- evidence_id: septin-ipr-IPR005737
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005737/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Gram-negative ParE family is narrower than generic ParE; hierarchy separately
    includes Firmicutes/Mollicutes and gyrase families.
  accessed_at: '2026-11-04T06:18:30.453466Z'
  support: supports
  snapshot_sha256: b8cc98f01329dff69753daf4d9fa545fa7da26c791f6de0df07b8928853c4b40
- evidence_id: septin-retry-IPR050220
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050220/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Type II DNA topoisomerase family is broader than ParC. Its llm=true/checked=false
    description is excluded from biological support; only native identity/type/hierarchy
    metadata is used.
  accessed_at: '2026-11-04T06:19:18.483458Z'
  support: supports
  snapshot_sha256: 6e0a444bf2047aca694717d1dab349a1fea6ed034f48c6a854555b50e3cac224
- evidence_id: septin-ipr-IPR001241
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001241/
  locator: Native name/type, description provenance flags, hierarchy and signatures;
    no sequence analysis
  summary: Broad typeIIA family spans gyrase and topoisomerase classes and is not
    an exact generic ParE identity.
  accessed_at: '2026-11-04T06:18:30.464286Z'
  support: supports
  snapshot_sha256: d61fcaf53fbc962df1bd2ef49b6c8988637eca6ab75ae7f1d4e119f16926dc1e
- evidence_id: septin-up-P0AFI2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AFI2.json
  locator: Accession, reviewed status, recommended name, gene names/loci, organism;
    relevant function/subunit/localization/evidence and complete InterPro xrefs
  summary: 'Reviewed P0AFI2: DNA topoisomerase 4 subunit A; gene parC; loci b3019,
    JW2987; E. coli K12 taxon83333. Family annotations and experimental citation provenance
    inspected. Identity/localization annotations alone do not establish membership
    in a DnaA-containing complex. '
  accessed_at: '2026-11-04T06:18:30.855546Z'
  support: supports
  snapshot_sha256: c4fc919de9d73e0d96e4a47ee12eff2b031d7a2e927aa9033082b8e3c6caf1d4
- evidence_id: septin-query-parC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact-organism reviewed gene response
  summary: One returned reviewed entry, P0AFI2, supports the specific current single-entry
    identity claim; descendants or other organism IDs are not conflated.
  accessed_at: '2026-11-04T06:18:33.056601Z'
  support: supports
  snapshot_sha256: 5f1885061e1cbd160c0a16d8e638641a25f23f40bdd535e1a0287a35c5bb7e9d
  search_scope: UniProt gene_exact:parC AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity read at 2026-11-04T06:18:33.056601Z.
- evidence_id: septin-up-P20083
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20083.json
  locator: Accession, reviewed status, recommended name, gene names/loci, organism;
    relevant function/subunit/localization/evidence and complete InterPro xrefs
  summary: 'Reviewed P20083: DNA topoisomerase 4 subunit B; gene parE; loci b3030,
    JW2998; E. coli K12 taxon83333. Family annotations and experimental citation provenance
    inspected. Identity/localization annotations alone do not establish membership
    in a DnaA-containing complex. '
  accessed_at: '2026-11-04T06:18:30.635630Z'
  support: supports
  snapshot_sha256: 018fe3a977ac2df60e8ccf94ea6ceec53c7b80c32b7616e380be45989b0ea97c
- evidence_id: septin-query-parE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AparE%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact-organism reviewed gene response
  summary: One returned reviewed entry, P20083, supports the specific current single-entry
    identity claim; descendants or other organism IDs are not conflated.
  accessed_at: '2026-11-04T06:18:32.071393Z'
  support: supports
  snapshot_sha256: 7cae2215f3d27b62d077ee0ba4d48d096dd0c5bff2a113e90a7b14db1c259032
  search_scope: UniProt gene_exact:parE AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity read at 2026-11-04T06:18:32.071393Z.
- evidence_id: septin-up-P66817
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P66817.json
  locator: Accession, reviewed status, recommended name, gene names/loci, organism;
    relevant function/subunit/localization/evidence and complete InterPro xrefs
  summary: 'Reviewed P66817: DnaA initiator-associating protein DiaA; gene diaA; loci
    b3149, JW3118; E. coli K12 taxon83333. Family annotations and experimental citation
    provenance inspected. Identity/localization annotations alone do not establish
    membership in a DnaA-containing complex. '
  accessed_at: '2026-11-04T06:18:30.575020Z'
  support: supports
  snapshot_sha256: 4683e244126b2c70e7a2e7e1d333b5afabd6bf0da217c4bfba240a016b1a3180
- evidence_id: septin-query-diaA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdiaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact-organism reviewed gene response
  summary: One returned reviewed entry, P66817, supports the specific current single-entry
    identity claim; descendants or other organism IDs are not conflated.
  accessed_at: '2026-11-04T06:18:33.829086Z'
  support: supports
  snapshot_sha256: c9bd1e6f2fd8d4086f1d0286c2f89fb17a06eb3ea02870af9f9b2331b29a5b63
  search_scope: UniProt gene_exact:diaA AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity read at 2026-11-04T06:18:33.829086Z.
- evidence_id: septin-up-P03004
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P03004.json
  locator: Accession, reviewed status, recommended name, gene names/loci, organism;
    relevant function/subunit/localization/evidence and complete InterPro xrefs
  summary: 'Reviewed P03004: Chromosomal replication initiator protein DnaA; gene
    dnaA; loci b3702, JW3679; E. coli K12 taxon83333. Family annotations and experimental
    citation provenance inspected. Identity/localization annotations alone do not
    establish membership in a DnaA-containing complex. P03004 location citations retain
    BL21(DE3) annotation context and Schenk mixed E.coli/B.subtilis experimental scope.'
  accessed_at: '2026-11-04T06:18:31.311157Z'
  support: supports
  snapshot_sha256: 20b9ed0385942a0aebc3645f0f499a77e9aab0741218e2327ee80b6ae7590dca
- evidence_id: septin-query-dnaA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact-organism reviewed gene response
  summary: One returned reviewed entry, P03004, supports the specific current single-entry
    identity claim; descendants or other organism IDs are not conflated.
  accessed_at: '2026-11-04T06:18:32.959244Z'
  support: supports
  snapshot_sha256: 3db63cf0e2bda46f5e0d2292b32f98621aa2da23fba568a428d8ad2f1fb148a0
  search_scope: UniProt gene_exact:dnaA AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity read at 2026-11-04T06:18:32.959244Z.
- evidence_id: septin-up-P0ABT2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABT2.json
  locator: Accession, reviewed status, recommended name, gene names/loci, organism;
    relevant function/subunit/localization/evidence and complete InterPro xrefs
  summary: 'Reviewed P0ABT2: DNA protection during starvation protein; gene dps; loci
    b0812, JW0797; E. coli K12 taxon83333. Family annotations and experimental citation
    provenance inspected. Identity/localization annotations alone do not establish
    membership in a DnaA-containing complex. '
  accessed_at: '2026-11-04T06:18:31.862030Z'
  support: supports
  snapshot_sha256: 5bc26c2d3491d422d27034cfa9f4afb128bbe8403d8b097b9e36bf810df038dc
- evidence_id: septin-query-dps
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact-organism reviewed gene response
  summary: One returned reviewed entry, P0ABT2, supports the specific current single-entry
    identity claim; descendants or other organism IDs are not conflated.
  accessed_at: '2026-11-04T06:18:34.064177Z'
  support: supports
  snapshot_sha256: 55916ff15491526e1713c2c33dd025ca4d012ffc4a8ed2f8a596f6dcad3c0619
  search_scope: UniProt gene_exact:dps AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity read at 2026-11-04T06:18:34.064177Z.
- evidence_id: septin-up-dnaB-context
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaB%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&format=json&size=500
  locator: Complete exact gene response; native identity/locus/status for named loading-subcomplex
    context only
  summary: P0ACB0 dnaB b4052,JW4012 is reviewed E.coli K12. Not an added maintained
    protein example or mandatory inventory finding.
  accessed_at: '2026-11-04T06:20:05.167564Z'
  support: supports
  snapshot_sha256: a82408ab2f13701ec5f77df653333e6715273c2cc3fcfad9fe06ad2a5cccb089
  search_scope: UniProt exact dnaB AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity inspected at 2026-11-04T06:20:05.167564Z.
- evidence_id: septin-up-dnaC-context
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaC%20AND%20organism_id%3A83333%20AND%20reviewed%3Atrue&format=json&size=500
  locator: Complete exact gene response; native identity/locus/status for named loading-subcomplex
    context only
  summary: P0AEF0 dnaC b4361,JW4325 is reviewed E.coli K12. Not an added maintained
    protein example or mandatory inventory finding.
  accessed_at: '2026-11-04T06:20:05.313618Z'
  support: supports
  snapshot_sha256: fc27864cb545ea3c9b7a3c83dc91170c0e5705fa1cbbde16caf3aed18c97205b
  search_scope: UniProt exact dnaC AND organism_id:83333 AND reviewed:true; size500;
    no date filter; all one returned identity inspected at 2026-11-04T06:20:05.313618Z.
- evidence_id: septin-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete ENA native response
  summary: Taxon562 is Escherichia coli species. Reference-strain annotations do not
    silently identify every experimental expression strain or mutant.
  accessed_at: '2026-11-04T06:18:31.464208Z'
  support: supports
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: septin-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete ENA native response
  summary: Taxon83333 is Escherichia coli K-12 strain. Reference-strain annotations
    do not silently identify every experimental expression strain or mutant.
  accessed_at: '2026-11-04T06:18:31.691690Z'
  support: supports
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: septin-pmid-8227000
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:8227000%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: Exact PMID 8227000, Escherichia coli topoisomerase IV. Purification, characterization,
    subunit structure, and subunit interactions. DOI 10.1016/s0021-9258(20)80551-1.
    Complete abstract read; primary-paper abstract, not a claim of complete body access.
  accessed_at: '2026-11-04T06:18:31.092164Z'
  support: supports
  snapshot_sha256: a7588b24911ff0cb86d5fd9d58d20f83d45d77f04f5771ac3a2a73fa54d4f7ef
  search_scope: EuropePMC exact EXT_ID:8227000 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.092164Z.
- evidence_id: septin-pmid-7783632
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7783632%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: 'Exact PMID 7783632, The twisted ''life'' of DNA in the cell: bacterial
    topoisomerases. DOI 10.1111/j.1365-2958.1995.tb02369.x. Complete abstract read;
    secondary review abstract, not a direct assembly experiment.'
  accessed_at: '2026-11-04T06:18:31.089118Z'
  support: supports
  snapshot_sha256: 81e005b8cf9425789b2f3a32a1540b6fe6f98888c04c495e7c898e73a3b0c980
  search_scope: EuropePMC exact EXT_ID:7783632 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.089118Z.
- evidence_id: septin-pmid-15326179
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15326179%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: Exact PMID 15326179, DiaA, a novel DnaA-binding protein, ensures the timely
    initiation of Escherichia coli chromosome replication. DOI 10.1074/jbc.m402762200.
    Complete abstract read; primary-paper abstract, not a claim of complete body access.
    Earlier dimer result is retained alongside later DiaA tetramer/equilibrium evidence.
  accessed_at: '2026-11-04T06:18:31.092088Z'
  support: supports
  snapshot_sha256: 1ed5b64f3348c7ee51289683134779199494af4e7b2ba24bacb40a3bb2fffbd0
  search_scope: EuropePMC exact EXT_ID:15326179 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.092088Z.
- evidence_id: septin-pmid-17699754
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:17699754%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: Exact PMID 17699754, The interaction of DiaA and DnaA regulates the replication
    cycle in E. coli by directly promoting ATP DnaA-specific initiation complexes.
    DOI 10.1101/gad.1561207. Complete abstract read; primary-paper abstract, not a
    claim of complete body access.
  accessed_at: '2026-11-04T06:18:31.141171Z'
  support: supports
  snapshot_sha256: 38473457523db83c14359d1a068103a26af3a0979f7fcf11002dccb97852b237
  search_scope: EuropePMC exact EXT_ID:17699754 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.141171Z.
- evidence_id: septin-pmid-20129058
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20129058%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: Exact PMID 20129058, Primase directs the release of DnaC from DnaB. DOI
    10.1016/j.molcel.2009.12.031. Complete abstract read; primary-paper abstract,
    not a claim of complete body access.
  accessed_at: '2026-11-04T06:18:31.114290Z'
  support: supports
  snapshot_sha256: 1945641c2f7c9bb7a9e6b17801ac402a6f3396688b0b8f9d2101d41683d03e5c
  search_scope: EuropePMC exact EXT_ID:20129058 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.114290Z.
- evidence_id: septin-pmid-18284581
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18284581%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: 'Exact PMID 18284581, Escherichia coli Dps interacts with DnaA protein
    to impede initiation: a model of adaptive mutation. DOI 10.1111/j.1365-2958.2008.06127.x.
    Complete abstract read; primary-paper abstract, not a claim of complete body access.'
  accessed_at: '2026-11-04T06:18:31.129036Z'
  support: supports
  snapshot_sha256: 3928fbe96e19572173f01b8341228489c157e93c4fc35d0f3c8db6afdc1066f7
  search_scope: EuropePMC exact EXT_ID:18284581 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.129036Z.
- evidence_id: septin-pmid-22574163
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22574163%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: 'Exact PMID 22574163, Association of the chromosome replication initiator
    DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding.
    DOI 10.1371/journal.pone.0036441. Complete abstract read; primary-paper abstract,
    not a claim of complete body access.'
  accessed_at: '2026-11-04T06:18:31.625127Z'
  support: supports
  snapshot_sha256: fd33317acb1781447b6ed1e6a43d7611734cd9e10ce74f576c5f7eeae0476a2b
  search_scope: EuropePMC exact EXT_ID:22574163 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.625127Z.
- evidence_id: septin-pmid-28166228
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:28166228%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: Exact PMID 28166228, Rapid turnover of DnaA at replication origin regions
    contributes to initiation control of DNA replication. DOI 10.1371/journal.pgen.1006561.
    Complete abstract read; primary-paper abstract, not a claim of complete body access.
    Explicitly includes B.subtilis FRAP and E.coli single-molecule observations; the
    bacterial systems are not collapsed.
  accessed_at: '2026-11-04T06:18:31.186535Z'
  support: supports
  snapshot_sha256: c2cf1f4b680a86ca9c2e2a95b7aa9c9085bd9e098af93c3cc2e03cd77c6af61c
  search_scope: EuropePMC exact EXT_ID:28166228 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.186535Z.
- evidence_id: septin-pmid-9478970
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9478970%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Native title/authors/year/DOI and full abstractText
  summary: Exact PMID 9478970, Membrane-mediated release of nucleotide from an initiator
    of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a
    distinct region of the protein into the lipid bilayer. DOI 10.1074/jbc.273.9.5167.
    Complete abstract read; primary-paper abstract, not a claim of complete body access.
    Artificial-bilayer insertion and nucleotide release are not direct membership
    evidence for the three complexes.
  accessed_at: '2026-11-04T06:18:31.285956Z'
  support: supports
  snapshot_sha256: 0d925c28720688573ccb3cce467229234d27d826ddf3b78e08c60ec202738f0b
  search_scope: EuropePMC exact EXT_ID:9478970 AND SRC:MED,CORE JSON,pageSize1,no
    date filter; unique complete result read at 2026-11-04T06:18:31.285956Z.
- evidence_id: septin-makowska-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2819048.1/PMC2819048.1.xml
  locator: 'Genuine PMC2819048.1 JATS: Results S8–S10, Discussion S14–S16, Methods
    S18/S20/S21; no supplement, figure pixels or uninspected raw data'
  summary: 'S8 directly compares oriC plasmid with M13ΔE101: retained DnaB requires
    oriC under the isolated prepriming assay. S20 supplies DnaA/DnaB/DnaC,HU,SSB and
    incubation/gel-filtration conditions. Loading-competent DnaC mutants can remain
    replication-defective; primase-dependent release is subsequent. Stoichiometry
    is conditional. S18 names K12 strains but refers exact constructs to unread TableS1.'
  accessed_at: '2026-11-04T06:20:04.562782Z'
  support: supports
  snapshot_sha256: 5fcbaee1771dea962cc886249ce7c58b45e384d1ec29a04feac327193760aeb5
- evidence_id: septin-keyamura-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1948862/
  locator: Current indexed primary article excerpts; displayed lines240–352 plus previously
    read lines156–277 in web-third.json; Results and captions, Discussion opening.
    No Methods/supplements/pixels
  summary: DiaA tetramer and multiple-DnaA interaction support its defined origin
    assembly. Tetramer-copy number differs from tetramers per whole oriC assembly.
    Mutations separate stimulation from unconditional necessity; source strains/constructs
    shown in captions are not assumed identical to dataset strains. Timestamp is current
    retained-reader inspection; underlying crawl instant is not independently exposed.
  accessed_at: '2026-11-04T06:22:58.392941Z'
  support: supports
  snapshot_sha256: d91c4efc8db67ae87ca7fc0d00a56d4f28c8ba3e8ab20ef4b518425d9689ee95
- evidence_id: septin-keyamura-primary-early
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1948862/
  locator: Displayed primary lines156–277, including crystal/tetramer, mutant assays
    and pull-down captions; no pixels
  summary: Actual current reader supplies Results text, including primary tetramer
    architecture and association assays. Exact sections are primary indexed text despite
    terminal challenge/500/404 routes; no complete downloaded body claim. Timestamp
    is current retained-reader inspection; underlying crawl instant is not independently
    exposed.
  accessed_at: '2026-11-04T06:22:58.392903Z'
  support: supports
  snapshot_sha256: 6536bbfb07c2c0341dd1709a8dd3c1cb66e9e38c2b0f90742b2210d072f49e89
- evidence_id: septin-chodavarapu-primary
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2008.06127.x
  locator: Current displayed primary lines157–271, with initial109–196 retained in
    web-first.json; Results/captions and Discussion opening, no complete Methods/pixels
  summary: Specific binding and origin-opening inhibition are supported. Inhibition
    depends on assay magnesium; induction experiments avoid H2O2 pleiotropy, so oxidative-stress
    checkpoint remains a model. W3110,MC1061,ZK2471 and synchronized dnaC2 experiments
    are distinct preparations; dataset coverage is not experimental equivalence. Timestamp
    is current retained-reader inspection; underlying crawl instant is not independently
    exposed.
  accessed_at: '2026-11-04T06:22:58.392976Z'
  support: supports
  snapshot_sha256: 729175d66e8ecae433957e822ca0f54ee6f854d73c5e6c547a107d3d05815023
- evidence_id: septin-chodavarapu-primary-binding
  kind: primary_source
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2008.06127.x
  locator: Displayed primary lines109–196; affinity/ELISA and N-terminal interaction
    assays, no pixels
  summary: Dps-DnaA binding was tested independently from cellular expression context.
    Conditional origin inhibition supports the coarse function; no absolute block
    or universal viability requirement is inferred. Timestamp is current retained-reader
    inspection; underlying crawl instant is not independently exposed.
  accessed_at: '2026-11-04T06:22:58.392766Z'
  support: supports
  snapshot_sha256: fee584e9c3be12a048a69ccf5f20ec4ad1e1d1e06f554325b7998eaf32292280
- evidence_id: septin-peng-primary
  kind: primary_source
  reference: https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions
  locator: Displayed genuine article front matter/abstract/opening lines0–575; no
    complete PDF or pixels
  summary: ParC2ParE2 activity and terminal-truncation association result corroborate
    the correct complex identity. The abstract specifies T7 expression preparations,
    not every native K12 strain. Timestamp is current retained-reader inspection;
    underlying crawl instant is not independently exposed.
  accessed_at: '2026-11-04T06:22:58.393028Z'
  support: supports
  snapshot_sha256: 0aadc1a22689e16b933c5af4bdc50a288379afa89c08f2f40017bfd5dc59b563
- evidence_id: septin-peng-primary-context
  kind: primary_source
  reference: https://www.researchgate.net/publication/14972288_Escherichia_coli_topoisomerase_IV_Purification_characterization_subunit_structure_and_subunit_interactions
  locator: Displayed article Results lines2700–2912 and late Discussion4859–4992;
    no intervening unshown body or pixels
  summary: Primary text separates ATP/dATP-supported activity from assembly without
    ATP or DNA. The maintained coarse graph does not assert ATP is needed for heterotetramer
    formation. Timestamp is current retained-reader inspection; underlying crawl instant
    is not independently exposed.
  accessed_at: '2026-11-04T06:22:58.393082Z'
  support: supports
  snapshot_sha256: aa451cd8aac667451650de6a6d8aa3a181120c92f1d0c4797c89a763add029a8
- evidence_id: septin-makowska-legacy
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/2819048/
  locator: Actual current response body/error; 200
  summary: HTTP200 browser challenge rather than article content. Successful alternate
    routes are independently scoped; failure is not biological refutation or global
    unavailability.
  accessed_at: '2026-11-04T06:19:16.922290Z'
  support: context_only
  snapshot_sha256: 5ff5e3d92d813a6f0b7a07b8c3dfb3cb69a13187fbf5d5c424a452be57366132
- evidence_id: septin-makowska-jats
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2819048/fullTextXML
  locator: Actual current response body/error; 500
  summary: HTTP500 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:19:17.610327Z'
  support: context_only
  snapshot_sha256: 7d9e03460a8a3af0f4a9d39feccb42f8bc4d9db63f42461d6f1002418639de0c
- evidence_id: septin-keyamura-jats
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC1948862/fullTextXML
  locator: Actual current response body/error; 500
  summary: HTTP500 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:19:21.451086Z'
  support: context_only
  snapshot_sha256: d2f8b0beac8800cb11226a91392362395686f2ddad6864c2472d71dba30588b4
- evidence_id: septin-keyamura-s3
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC1948862.1/PMC1948862.1.xml
  locator: Actual current response body/error; 404
  summary: HTTP404 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:20:04.348543Z'
  support: context_only
  snapshot_sha256: ce99965dbc9eb71556f93e47cb53b76aa4d81933087166069884cce57bd9b156
- evidence_id: septin-chodavarapu-publisher
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2958.2008.06127.x
  locator: Actual current response body/error; 403
  summary: HTTP403 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:19:17.039871Z'
  support: context_only
  snapshot_sha256: bbbe67506b36f47c4574833cacd677c1961a9db660092ed91ba6015a973f6b85
- evidence_id: septin-peng-publisher
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(20)80551-1/pdf
  locator: Actual current response body/error; 403
  summary: HTTP403 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:19:17.163794Z'
  support: context_only
  snapshot_sha256: 4d54db0d13bfce5a905fc1ed6ef1de6aa414824106e80f2e73a19c46e6d3234e
- evidence_id: septin-ishida-publisher
  kind: validation
  reference: https://www.jbc.org/article/S0021925820724841/pdf
  locator: Actual current response body/error; 403
  summary: HTTP403 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:19:17.237074Z'
  support: context_only
  snapshot_sha256: 6d42b7a43b809af5b45bc59836d2fb9ae8c40c4cdea0ff4148b634797821533b
- evidence_id: septin-ipr-IPR023070
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023070/
  locator: Actual current response body/error; 429
  summary: HTTP429 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:18:30.461931Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR005742
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005742/
  locator: Actual current response body/error; 429
  summary: HTTP429 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:18:30.453577Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR050220
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050220/
  locator: Actual current response body/error; 429
  summary: HTTP429 did not supply the requested scientific body/authority object.
    Successful alternate routes are independently scoped; failure is not biological
    refutation or global unavailability.
  accessed_at: '2026-11-04T06:18:30.462034Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh20-organism catalogue and all keys, independently read from
    peer packet
  summary: E.coli has five advertised datasets; precise1k is selected for a bounded
    matched reference-strain context. Other bacterial catalogue organisms do not establish
    the universal distribution of generic TopoIV.
  accessed_at: '2026-11-04T06:16:25.827407Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official complete unpaginated /api/datasets; all20 organism names/IDs/keys
    read for Escherichia coli and named hosts; no date filter; actual 2026-11-04T06:16:25.827407Z.
- evidence_id: septin-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete exact organism/dataset metadata
  summary: precise1k covers BW25113,DGF-298,GMOS,MG1655,W3110, with201 modules/1035samples.
    This is relevant E.coli reference context, not claimed coverage of BL21(DE3),NA141,MC1061
    or every recombinant/mutant preparation.
  accessed_at: '2026-11-04T06:16:26.387064Z'
  support: supports
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: septin-ecoli-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 module identity/regulator/category rows; actual finite search, not
    full activity inspection
  summary: Exact OxyR3 and RpoS51 annotations provide bounded stress-response context;
    complete catalogue is not an assembly or localization experiment.
  accessed_at: '2026-11-04T06:16:25.939241Z'
  support: supports
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: Official e_coli/precise1k/imodulons; all201 returned IDs/names/regulators
    checked for named genes/stress modules; no other dataset, no date filter.
- evidence_id: septin-modulegene-parC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3019
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b3019 maps parC to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:20:04.116147Z'
  support: supports
  snapshot_sha256: 757393bd3acb89212c98d7ede361c1e6260fac0942620a23ac20474f78bb3f35
- evidence_id: septin-modulemembers-parC
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3019/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: none. These are computational expression memberships;
    false flags do not mean absent expression, absent gene, no regulation or no structural
    role.'
  accessed_at: '2026-11-04T06:21:02.319840Z'
  support: supports
  snapshot_sha256: 2fdecfab2d14026202bc2e6c0210f68be917719abbddf02680f89770a5906801
  search_scope: Official e_coli/precise1k/gene b3019 (parC) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.319840Z.
- evidence_id: septin-modulegene-parE
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3030
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b3030 maps parE to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:20:04.160250Z'
  support: supports
  snapshot_sha256: 4bc604d66604c235a0d9600e850693b2475e2960b87c48be4d7b23a7713be8a7
- evidence_id: septin-modulemembers-parE
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3030/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: none. These are computational expression memberships;
    false flags do not mean absent expression, absent gene, no regulation or no structural
    role.'
  accessed_at: '2026-11-04T06:21:02.319753Z'
  support: supports
  snapshot_sha256: 8dbac9c4ce9e4a0bec64b78a2587a68e3bd62f6b69a08de4dcfc4a2f4848b952
  search_scope: Official e_coli/precise1k/gene b3030 (parE) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.319753Z.
- evidence_id: septin-modulegene-dnaA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3702
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b3702 maps dnaA to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:20:04.196839Z'
  support: supports
  snapshot_sha256: 46e591a9c235c1af1777c7d581f27c7fa84f09a41de0e3d945d3a9aab6dcbb4a
- evidence_id: septin-modulemembers-dnaA
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3702/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: none. These are computational expression memberships;
    false flags do not mean absent expression, absent gene, no regulation or no structural
    role.'
  accessed_at: '2026-11-04T06:21:02.319736Z'
  support: supports
  snapshot_sha256: f777d7bb66ff9be4d6f0a5ddb0c9152032c3f3bcf37ca482471654c4bd083661
  search_scope: Official e_coli/precise1k/gene b3702 (dnaA) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.319736Z.
- evidence_id: septin-modulegene-diaA
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3149
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b3149 maps diaA to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:20:04.238548Z'
  support: supports
  snapshot_sha256: 701ec79011d3ab048b97859921553ca06e4003cbd92c4e4335234e3708c77153
- evidence_id: septin-modulemembers-diaA
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3149/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: none. These are computational expression memberships;
    false flags do not mean absent expression, absent gene, no regulation or no structural
    role.'
  accessed_at: '2026-11-04T06:21:02.275072Z'
  support: supports
  snapshot_sha256: ab1db101b17716dd1a5221b93c485078e3d1cf2eb5bca6ae945d8b134b300d30
  search_scope: Official e_coli/precise1k/gene b3149 (diaA) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.275072Z.
- evidence_id: septin-modulegene-dps
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0812
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b0812 maps dps to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:20:04.268091Z'
  support: supports
  snapshot_sha256: 884791963f2d48da38c11a21c767a55201f6997f978c02976e0ed5ac7db50871
- evidence_id: septin-modulemembers-dps
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0812/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: 3 OxyR, 51 RpoS. These are computational expression
    memberships; false flags do not mean absent expression, absent gene, no regulation
    or no structural role.'
  accessed_at: '2026-11-04T06:21:02.680786Z'
  support: supports
  snapshot_sha256: 6e22deeb24f50dcae23f9476907de7878c8c159961d1f1753f18f02b39712ad5
  search_scope: Official e_coli/precise1k/gene b0812 (dps) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.680786Z.
- evidence_id: septin-modulegene-dnaB
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4052
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b4052 maps dnaB to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:21:02.519547Z'
  support: supports
  snapshot_sha256: 69896d62515436606275f0b2e3ed0b33e80762e8a3163edc9e36943f57d4d914
- evidence_id: septin-modulemembers-dnaB
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4052/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: none. These are computational expression memberships;
    false flags do not mean absent expression, absent gene, no regulation or no structural
    role.'
  accessed_at: '2026-11-04T06:21:02.724488Z'
  support: supports
  snapshot_sha256: 6857269f74e8531f6428bda4ac5183118a493f1701320ba44a2cf201bfd496e7
  search_scope: Official e_coli/precise1k/gene b4052 (dnaB) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.724488Z.
- evidence_id: septin-modulegene-dnaC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4361
  locator: Exact gene_id/name/product/UniProt and locus response
  summary: Covered e_coli/precise1k/b4361 maps dnaC to independently verified native
    identity. Imported function prose is annotation context, not a direct experimental
    statement.
  accessed_at: '2026-11-04T06:21:03.021024Z'
  support: supports
  snapshot_sha256: 75a6c5fd6f380adc936a56d2c4e8fd36093b6200f2d633eac924977e923d27da
- evidence_id: septin-modulemembers-dnaC
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4361/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows for one exact locus
  summary: 'Thresholded hits: none. These are computational expression memberships;
    false flags do not mean absent expression, absent gene, no regulation or no structural
    role.'
  accessed_at: '2026-11-04T06:21:02.724478Z'
  support: supports
  snapshot_sha256: a7b4b55c42c06bf29f9141c8cec55e2c8a9f552c4dce2c7c75aa0f07232029df
  search_scope: Official e_coli/precise1k/gene b4361 (dnaC) /imodulons; complete201
    returned records, no cross-dataset extrapolation, no date filter; actual 2026-11-04T06:21:02.724478Z.
- evidence_id: septin-module-3
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/3
  locator: Native module identity/regulator/threshold/member fields only; ai_summary
    excluded; activity vectors not biologically interpreted
  summary: OxyR3/RpoS51 native metadata corroborates the dps thresholded hit. Explicit
    generated prose is not scientific evidence; module assignment does not prove direct
    DnaA binding, localization or complex formation.
  accessed_at: '2026-11-04T06:22:29.730306Z'
  support: supports
  snapshot_sha256: 8f13d013b44e8d7cc9c4f7a17131b26bacd92039947bd13be57aadffea91f49e
- evidence_id: septin-module-3-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/3/genes
  locator: Complete member identities/threshold and exact dps b0812 row
  summary: dps is a thresholded member of OxyR3 among38 members. This bounded expression
    context is consistent with a stress narrative but does not independently establish
    the oxidative checkpoint model.
  accessed_at: '2026-11-04T06:22:29.805375Z'
  support: supports
  snapshot_sha256: 8fae909df3edad29ece92bc0b0ba57f1ee27edd0ce9069aa1c4ef475a0d02173
- evidence_id: septin-module-51
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/51
  locator: Native module identity/regulator/threshold/member fields only; ai_summary
    excluded; activity vectors not biologically interpreted
  summary: OxyR3/RpoS51 native metadata corroborates the dps thresholded hit. Explicit
    generated prose is not scientific evidence; module assignment does not prove direct
    DnaA binding, localization or complex formation.
  accessed_at: '2026-11-04T06:22:29.805335Z'
  support: supports
  snapshot_sha256: 0178f2450c16c9f77f3c57a250537106ec85c4ddf6d1771458a534245b109fee
- evidence_id: septin-module-51-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/51/genes
  locator: Complete member identities/threshold and exact dps b0812 row
  summary: dps is a thresholded member of RpoS51 among122 members. This bounded expression
    context is consistent with a stress narrative but does not independently establish
    the oxidative checkpoint model.
  accessed_at: '2026-11-04T06:22:29.831565Z'
  support: supports
  snapshot_sha256: 86941409a047683d84128e65d7f8894bb91685a948486e7e8a747359f87da38b
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Prior actual Nov3 00:49Z command receipt
  summary: Historical invocation exited1 with PermissionError reading pyvenv.cfg.
    No fresh invocation or runner success claimed; current official source fallback
    is separate.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/adversary-septin/original-checks.json
  locator: Actual four validate/render runs and all52 historical input occurrences
  summary: All four original pairs validate0/render0 and Markdown is byte-identical;
    all13 historical inputs each match retained revision, and current targets are
    nonstale. Historical batch26 execution cohort is accurate reused provenance, not
    a current-head gate.
  accessed_at: '2026-11-04T06:18:24.151979Z'
  support: supports
  snapshot_sha256: 0c2b75d2dfbbf6a4b364043235f8b018fefb498e804cddada838da80cd0b0561
- evidence_id: septin-record-dna_topoisomerase_iv_complex
  kind: record_content
  reference: data/structures/other/dna_topoisomerase_iv_complex.yaml
  locator: Entire frozen current record including all examples/evidence/graphs/discussions/history
  summary: Complete nonstale maintained record independently assessed. Historical
    rationale is provenance, not automatically a current scientific claim.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: fb14ab25e6bf5e766d86b767a0f20597e77782d62fae6c5b48ed82dcee0ef070
- evidence_id: septin-original-dna_topoisomerase_iv_complex
  kind: record_content
  reference: reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; original verdict/findings/actions/check
    scope
  summary: Exact inherited lineage and limits assessed independently; old global runs
    remain scoped to their actual historical batch26 execution and source.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: b2a67f0185810b26fb35419ab15c773de0a1daf6d8a9ebf53b248380aa159dc2
- evidence_id: septin-native-dna_topoisomerase_iv_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-verify-receipt.json
    receiptSHA256 bddf353955ba8e79976193a4f1c1818bcf6a83a2f2bf88e9fa6932e8f2c53d51;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:12.177390Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dna_topoisomerase_iv_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dna_topoisomerase_iv_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-causal-receipt.json
    receiptSHA256 ba3ac6ef01f0ec2647bf9306cdaa64d510a2ca609a6f8952ca3dfb976f98e89c;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:12.638602Z'
  support: supports
  snapshot_sha256: 6de87a107b6e984920696fdc44e3c3d1a38f70dc028887322f39804be0c9c0af
- evidence_id: septin-historical-failure-dna_topoisomerase_iv_complex
  kind: validation
  reference: reviews/structured/20261022T055924Z-dna-topoisomerase-iv-complex-audit/review.yaml#replication51-agent-peng1993-publisher
  locator: Historical original403 row, not recovered original response bytes
  summary: Original database-typed row correctly says HTTP403/context_only/no body;
    only its evidence kind requires correction. Original snapshot 9fc7ab8d1025f66a87cf5348de1b52b4aee5c751864a6c6c6f0a3115140b4713
    and timestamp retained.
  accessed_at: '2026-10-22T05:43:16.589132Z'
  support: context_only
  snapshot_sha256: b2a67f0185810b26fb35419ab15c773de0a1daf6d8a9ebf53b248380aa159dc2
- evidence_id: septin-record-dnaa_diaa_complex
  kind: record_content
  reference: data/structures/other/dnaa_diaa_complex.yaml
  locator: Entire frozen current record including all examples/evidence/graphs/discussions/history
  summary: Complete nonstale maintained record independently assessed. Historical
    rationale is provenance, not automatically a current scientific claim.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: fc2f791efd2e63545ba7786349b16f68ed0655623cac1e8e4fea5e39ba1c43f4
- evidence_id: septin-original-dnaa_diaa_complex
  kind: record_content
  reference: reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; original verdict/findings/actions/check
    scope
  summary: Exact inherited lineage and limits assessed independently; old global runs
    remain scoped to their actual historical batch26 execution and source.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: 42d73a83ac80abf0e7081f8263e0c5cd5d25608ac689f9f4618583220dcdc62a
- evidence_id: septin-native-dnaa_diaa_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_diaa_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-verify-receipt.json
    receiptSHA256 1e38b4905c5721a24c30b3435b33425e9ef8bdbfa41239e2de5fd0053ec880f0;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:14.020370Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dnaa_diaa_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_diaa_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-causal-receipt.json
    receiptSHA256 51bea0370996928bd58bea9ca8876e9782a55521a47af153830c568cef751fa2;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:14.493978Z'
  support: supports
  snapshot_sha256: de72169f746704b3731bd19c7b60f2ad75d6f987aed3854beec390ec08ee23fe
- evidence_id: septin-historical-failure-dnaa_diaa_complex
  kind: validation
  reference: reviews/structured/20261022T055925Z-dnaa-diaa-complex-audit/review.yaml#replication51-agent-ishida2004-publisher
  locator: Historical original403 row, not recovered original response bytes
  summary: Original database-typed row correctly says HTTP403/context_only/no body;
    only its evidence kind requires correction. Original snapshot 28c406032a0757333faddce6d77ef0b153fb5b2b9012be60e5abf4d653eef711
    and timestamp retained.
  accessed_at: '2026-10-22T05:43:16.588938Z'
  support: context_only
  snapshot_sha256: 42d73a83ac80abf0e7081f8263e0c5cd5d25608ac689f9f4618583220dcdc62a
- evidence_id: septin-record-dnaa_dnab_dnac_complex
  kind: record_content
  reference: data/structures/other/dnaa_dnab_dnac_complex.yaml
  locator: Entire frozen current record including all examples/evidence/graphs/discussions/history
  summary: Complete nonstale maintained record independently assessed. Historical
    rationale is provenance, not automatically a current scientific claim.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: a49c1990539aacfc5c45ca3e85ad447d25d1de1e4608396c5233d16bf5ec4e56
- evidence_id: septin-original-dnaa_dnab_dnac_complex
  kind: record_content
  reference: reviews/structured/20261022T055925Z-dnaa-dnab-dnac-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; original verdict/findings/actions/check
    scope
  summary: Exact inherited lineage and limits assessed independently; old global runs
    remain scoped to their actual historical batch26 execution and source.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: b72282c71638516e097bc0d1e5e8b8eaab8d6820a207155ffba541d63c804ee0
- evidence_id: septin-native-dnaa_dnab_dnac_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dnab_dnac_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-verify-receipt.json
    receiptSHA256 1138a974cedd0c0503906557b48672e50de4893902f85c928a77e4e14c026c9b;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:16.035077Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dnaa_dnab_dnac_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dnab_dnac_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-causal-receipt.json
    receiptSHA256 6a74b5819b490b2454731f265e33e3cc62c8670bc3cca033b1fabd7f083d0556;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:16.497282Z'
  support: supports
  snapshot_sha256: 51ed8c963a301a182bcea61e6cb3eab637e3b35581509eeff3f634caf21404ae
- evidence_id: septin-record-dnaa_dps_complex
  kind: record_content
  reference: data/structures/other/dnaa_dps_complex.yaml
  locator: Entire frozen current record including all examples/evidence/graphs/discussions/history
  summary: Complete nonstale maintained record independently assessed. Historical
    rationale is provenance, not automatically a current scientific claim.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: 2b89c667acb0f20b397cc83da72c84987b12fbddcf156f5159fd6225a8b35f87
- evidence_id: septin-original-dnaa_dps_complex
  kind: record_content
  reference: reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown; original verdict/findings/actions/check
    scope
  summary: Exact inherited lineage and limits assessed independently; old global runs
    remain scoped to their actual historical batch26 execution and source.
  accessed_at: '2026-11-04T06:26:14.577654Z'
  support: context_only
  snapshot_sha256: 17a6d0ebaeb2b67c1a3c0d574e5fb72fffc7d6b4406d454dbdeff1587035cf4e
- evidence_id: septin-native-dnaa_dps_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-verify-receipt.json
    receiptSHA256 a7eb006eb0008f9277481326c8d11855c8018b18a9f6cbcbc0154b17da3d24a7;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:18.233378Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dnaa_dps_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_dps_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-causal-receipt.json
    receiptSHA256 514021ec09992e73d93759d7bce7dd350cd7b613f87361ab8a3cac3b9bb40c99;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED by declared examples. Native success verifies identifier/coverage
    syntax, not independent experimental membership or assembly necessity.
  accessed_at: '2026-11-04T06:16:18.705266Z'
  support: supports
  snapshot_sha256: 9c32ad64b248777c65ff4967c2fceec4a6976c91d56e141e5cc47ff0cdbbe226
- evidence_id: septin-historical-failure-dnaa_dps_complex
  kind: validation
  reference: reviews/structured/20261022T055926Z-dnaa-dps-complex-audit/review.yaml#replication51-agent-chodavarapu2008-publisher
  locator: Historical original403 row, not recovered original response bytes
  summary: Original database-typed row correctly says HTTP403/context_only/no body;
    only its evidence kind requires correction. Original snapshot 642d8d8f811c382ca3b937b715e0110c74ae36df8f9e4156873923a1e910e850
    and timestamp retained.
  accessed_at: '2026-10-22T05:43:16.589100Z'
  support: context_only
  snapshot_sha256: 17a6d0ebaeb2b67c1a3c0d574e5fb72fffc7d6b4406d454dbdeff1587035cf4e
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T06:21:45.527060Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 4d8066c42a0fa6a0af6b1cc8023900d6619aeacbbd61501a4a67e05b631b82b3
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T06:16:24.980270Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T06:16:02.168928Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T06:16:05.361001Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T06:16:34.263126Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T06:35:23Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: da547289ce8922308654958d60266f2653f5cdacc621ac500a7b4fb43af23fe2
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T06:17:30.052311Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: c7805f691245902bc75ffd4e6a38f8e0d7b21853f7f4b9c98e0b4782bcd5ecde
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2388 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-dna_polymerase_iii_clamp_loader_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:01.523240Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_clamp_loader_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_clamp_loader_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:01.974041Z'
  support: context_only
  snapshot_sha256: aca3b51abc154a55cd6b3d81b01fc8a21768e3ec3940102586a9945621646d06
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:02.411476Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:02.834438Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_core_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:04.590205Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_polymerase_iii_core_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_polymerase_iii_core_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:05.020550Z'
  support: context_only
  snapshot_sha256: 622c34a9d261773a36cbd6c978ead78ec02d5fe3b0cb7c2e0e1c6688ceff466d
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_replication_factor_a_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:06.274483Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_replication_factor_a_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_a_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:06.731473Z'
  support: context_only
  snapshot_sha256: 7aa8052a4e7f0766e31305e034ff3844deb0b33aa46c8859caf42dad6b98b57c
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_replication_factor_c_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:08.125330Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_replication_factor_c_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_factor_c_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:08.598249Z'
  support: context_only
  snapshot_sha256: 8fe53b9e87565355d70e5600509e38c4dfda6fcd88d47a294b9dfde6859f89f1
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_replication_preinitiation_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:10.125946Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_replication_preinitiation_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_replication_preinitiation_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:10.579658Z'
  support: context_only
  snapshot_sha256: c74a99b2a3d0d028e6c80171343313ea4b2db7f9424ad9185ccfed9c2f89fba7
  summary: 5 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_topoisomerase_iv_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:12.177390Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dna_topoisomerase_iv_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dna_topoisomerase_iv_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:12.638602Z'
  support: context_only
  snapshot_sha256: 6de87a107b6e984920696fdc44e3c3d1a38f70dc028887322f39804be0c9c0af
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_diaa_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:14.020370Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_diaa_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_diaa_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:14.493978Z'
  support: context_only
  snapshot_sha256: de72169f746704b3731bd19c7b60f2ad75d6f987aed3854beec390ec08ee23fe
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_dnab_dnac_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:16.035077Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_dnab_dnac_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dnab_dnac_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:16.497282Z'
  support: context_only
  snapshot_sha256: 51ed8c963a301a182bcea61e6cb3eab637e3b35581509eeff3f634caf21404ae
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_dps_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:18.233378Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_dps_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2388/dnaa_dps_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T06:16:18.705266Z'
  support: context_only
  snapshot_sha256: 9c32ad64b248777c65ff4967c2fceec4a6976c91d56e141e5cc47ff0cdbbe226
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-loader-identity
  area: identity
  topic: Full heptamer versus crystallized pentamer
  outcome: concern
  summary: 'Exact GO identity/protein-complex parent and holoenzyme parthood are sound.
    GO is faithfully quoted, but unconditional tau AND gamma wording compresses its
    cited source distinction: DnaX3 can contain either or both products for clamp
    loading. Retain heptamer scope and separate tau-dependent fork organization from
    minimal pentamer activity.'
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-go-0043846
  - micro-go-0009360
  - micro-isa-0043846
  - micro-mchenry2003-pdf
  - micro-jeruzalmi2001-pdf
  - micro-up-P06710
  - micro-pmid-3283127
- assessment_id: micro-loader-grounding
  area: grounding
  topic: Three exact families and excluded domain/broad alternatives
  outcome: concern
  summary: HolA IPR005790,HolC IPR007459 andHolD IPR004615 are exact whole-protein
    families with independent matching example xrefs, yet remain REVIEWED_LABEL_ONLY.
    DnaX IPR012763/IPR045085 andHolB IPR004622/IPR048731 are domains; IPR050238 is
    broader and generated prose cannot establish exact identity. Do not import HolA
    proofreading or historical HolD unknown-function prose.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR005790
  - micro-ipr-IPR007459
  - micro-ipr-IPR004615
  - micro-ipr-IPR012763-retry
  - micro-ipr-IPR045085
  - micro-ipr-IPR004622
  - micro-ipr-IPR048731-retry
  - micro-ipr-IPR050238
  - micro-up-P28630
  - micro-up-P28905
  - micro-up-P28632
- assessment_id: micro-loader-proteins
  area: grounding
  topic: Five current reviewed K12 identities
  outcome: supported
  summary: DnaX P06710/HolA P28630/HolB P28631/HolC P28905/HolD P28632 match exact
    primary genes, ordered loci and tax83333. Eight full current gene queries overall
    are singletons; no reconstruction of historical query results. DnaX tau/gamma
    are frameshift products, not two unrelated genes.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-tax-83333
  - micro-up-P06710
  - micro-up-P28630
  - micro-up-P28631
  - micro-up-P28905
  - micro-up-P28632
  - micro-query-dnaX
  - micro-query-holA
  - micro-query-holB
  - micro-query-holC
  - micro-query-holD
- assessment_id: micro-loader-source
  area: scope
  topic: Canonical species and actual structural preparation
  outcome: supported
  summary: Canonical species562 is appropriate for the E.coli gamma-complex study.
    Jeruzalmi used purified delta/delta-prime and truncated gamma1–373 reconstitution;
    structure is nucleotide-free pentamer, not full heptamer or an unmodified native
    K12 preparation. Fig1 caption and Methods read without pixel/coordinate analysis.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-tax-562
  - micro-tax-83333
  - micro-jeruzalmi2001-pdf
  - micro-pmid-11525729
- assessment_id: micro-loader-graph
  area: graph
  topic: Nine coarse membership/function edges
  outcome: supported
  summary: Five component membership edges, delta-beta contact, beta loading, DNA
    substrate and replication outcome remain source-scoped NONMECHANISTIC FUNCTION.
    Static crystal and authors speculative transition model are not a measured ATP
    cycle; chi/psi membership comes from the heptamer review and Maki primary abstract,
    not the pentamer crystal. Scope notes appropriately withhold detailed geometry/switching.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-jeruzalmi2001-pdf
  - micro-mchenry2003-pdf
  - micro-pmid-3283127
  - micro-go-0003689
  - micro-go-0006260
- assessment_id: micro-loader-formation
  area: grounding
  topic: Formation versus function/viability
  outcome: unknown
  summary: Active minimal pentamer and alternative DnaX products do not establish
    loss-of-formation requirements for the named full heptamer in all conditions.
    Global UNKNOWN component formation remains permissible. Native tau viability and
    gamma viability clauses do not impose universal loader-assembly classifications.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-up-P06710
  - micro-jeruzalmi2001-pdf
  - micro-pmid-3283127
- assessment_id: micro-whole-identity
  area: identity
  topic: Modular holoenzyme and class hierarchy
  outcome: supported
  summary: GO0009360 exact identity/synonym and DNA-polymerase-complex parent match
    its tripartite core/beta/loader model. The record does not copy the neighboring
    beta cross-class oligomerization sentence or impose a fixed modern two-versus-three-core
    stoichiometry.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-go-0009360
  - micro-go-0042575
  - micro-isa-0009360
  - micro-pmid-3283127
- assessment_id: micro-whole-components
  area: grounding
  topic: Three correctly grounded subcomplexes
  outcome: supported
  summary: Core GO0044776,beta GO0044775 andloader GO0043846 are structure-level components.
    No artificial single-protein inventory is required. The clamp-component note explicitly
    attributes compressed tau/gamma wording to GO; this is retained as an accurately
    scoped authority quotation, not independently asserted universal DnaX stoichiometry.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-schema
  - micro-go-0044776
  - micro-go-0044775
  - micro-go-0043846
  - micro-mchenry2003-pdf
  - micro-up-P06710
- assessment_id: micro-whole-canonical
  area: scope
  topic: E.coli reconstitution at complete abstract tier
  outcome: supported
  summary: Maki/Kornberg complete primary abstract directly reports reconstitution
    of ten polypeptide types and processive replication from core/auxiliary subunits,
    supporting species562 canonical wording. Publisher HTML/PDF403 and API metadata
    only leave exact methods/strain/figures unread; reference K12 DnaX is not proof
    of that preparation strain.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-pmid-3283127
  - micro-maki1988-api
  - micro-maki1988-html-access
  - micro-maki1988-pdf-access
  - micro-tax-562
  - micro-tax-83333
- assessment_id: micro-whole-graph
  area: graph
  topic: Six descriptive processive-synthesis edges
  outcome: supported
  summary: Core contributes polymerase activity,beta tethers catalytic subunit,loader
    loads beta,template-directed activity extends DNA and whole supports replication.
    Maki primary abstract separates core polymerase/proofreading from auxiliary processivity.
    NONMECHANISTIC scope excludes detailed ATP transitions, exchange and fork coordination,
    so no static-structure mechanism inflation is established.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-graph-policy
  - micro-pmid-3283127
  - micro-go-0003887
  - micro-go-0006260
  - micro-jeruzalmi2001-pdf
  - micro-mchenry2003-pdf
- assessment_id: micro-whole-formation
  area: grounding
  topic: Functionally necessary modules versus formation
  outcome: unknown
  summary: Functional contribution and successful purified reconstitution do not determine
    every component physical-formation necessity across contexts. UNKNOWN is not a
    defect; no fixed subunit-copy model or obligatory individual-protein examples
    proposed.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-pmid-3283127
- assessment_id: micro-core-identity
  area: identity
  topic: Alpha/epsilon/theta catalytic subassembly
  outcome: supported
  summary: GO0044776 and complete Maki abstract support alpha/epsilon/theta core identity
    and holoenzyme parthood. DNA-polymerase-complex parent is semantically supported
    by catalytic activity rather than claimed as a current direct GO is-a edge. Polymerase
    and proofreading remain distinct activities.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-go-0044776
  - micro-go-0009360
  - micro-go-0042575
  - micro-isa-0044776
  - micro-pmid-3283127
- assessment_id: micro-core-grounding
  area: grounding
  topic: Exact theta family and other class boundaries
  outcome: concern
  summary: HolE IPR009052/PF06440 is an exact full-protein family with P0ABS8 xref,
    so continued REVIEWED_LABEL_ONLY is a bounded grounding gap. DnaQ IPR006309 is
    proteobacterial, IPR006054 is a domain, and IPR004805 includes DnaE2/DnaE/PolC.
    PHP and OB-fold candidates are domains. No forced broad/domain mapping follows.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR009052-retry
  - micro-up-P0ABS8
  - micro-ipr-IPR006309-retry
  - micro-ipr-IPR006054
  - micro-ipr-IPR004805
  - micro-ipr-IPR004365
  - micro-ipr-IPR004013
- assessment_id: micro-core-proteins
  area: grounding
  topic: Three current reviewed reference examples
  outcome: supported
  summary: P10443/dnaE,b0184;P03007/dnaQ,b0215;P0ABS8/holE,b1842 are reviewed K12
    references with current singleton queries. E.coli dnaE synonym polC does not conflate
    distinct Gram-positive PolC. Membership is separately supported by Maki abstract
    and native GO; theta is not individually credited with either catalytic activity.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-up-P10443
  - micro-up-P03007
  - micro-up-P0ABS8
  - micro-query-dnaE
  - micro-query-dnaQ
  - micro-query-holE
  - micro-tax-83333
  - micro-pmid-3283127
- assessment_id: micro-core-canonical
  area: scope
  topic: Species versus unread reconstitution strain
  outcome: supported
  summary: Species562 canonical note matches primary abstract. K12 accession labels
    identify examples only. Maki exact assay methods, experimental strain and figures
    remain unverified because only complete abstract and publisher metadata were reached.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-pmid-3283127
  - micro-maki1988-api
  - micro-maki1988-html-access
  - micro-maki1988-pdf-access
  - micro-tax-562
  - micro-tax-83333
- assessment_id: micro-core-graph
  area: graph
  topic: Membership and separated polymerase/proofreading
  outcome: supported
  summary: Three constituent membership edges and separate core enables-polymerase/enables-proofreading
    edges match primary abstract and exact activity scope. No assertion that theta
    alone polymerizes/proofreads, that proofreading is GO0003887, or that graph ordering
    is a measured assembly sequence.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-graph-policy
  - micro-go-0003887
  - micro-pmid-3283127
  - micro-up-P10443
  - micro-up-P03007
  - micro-up-P0ABS8
- assessment_id: micro-core-formation
  area: grounding
  topic: Defined components versus universal physical necessity
  outcome: unknown
  summary: Core composition and activity reconstitution do not establish a complete
    conditional loss-of-assembly series. UNKNOWN remains appropriate, while uncertainty
    over theta function is not evidence of its absence. No new experiment or universal
    ESSENTIAL classification required.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-pmid-3283127
  - micro-up-P0ABS8
- assessment_id: micro-upstream-scope-0
  area: scope
  topic: Current upstream nuclear ancestry/taxon discrepancy
  outcome: unknown
  summary: Current native GO routes the term through nuclear protein-containing complex
    and marks Eukaryota-only, conflicting with its named bacterial identity and cited
    E.coli evidence. These assertions are absent from the maintained record; retain
    exact named identity and bacterial scope, without importing upstream restriction
    or creating a local false-misquotation finding.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-isa-0043846
  - micro-constraints-0043846
  - micro-pmid-11525729
- assessment_id: micro-upstream-scope-2
  area: scope
  topic: Current upstream nuclear ancestry/taxon discrepancy
  outcome: unknown
  summary: Current native GO routes the term through nuclear protein-containing complex
    and marks Eukaryota-only, conflicting with its named bacterial identity and cited
    E.coli evidence. These assertions are absent from the maintained record; retain
    exact named identity and bacterial scope, without importing upstream restriction
    or creating a local false-misquotation finding.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-isa-0044776
  - micro-constraints-0044776
  - micro-pmid-3283127
- assessment_id: micro-inputs-0
  area: provenance
  topic: Original source versus current target
  outcome: supported
  summary: Original frozen record is unchanged on current main. Original source revision/hashes
    and immutable YAML/Markdown were verified; current source reassessment does not
    erase historical limitations or invent refreshed stale fields.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-original-audit
- assessment_id: micro-adapter-0
  area: scope
  topic: Positive molecular claims require matched structured-source context
  outcome: concern
  summary: 'Original formal expression-only exclusion is unsupported: positive replication,
    clamp-loading or core catalytic claims trigger applicability. Fresh complete catalogue
    selects E.coli precise1k; nine exact reference loci each checked against201 module
    rows. Only HolD→ppGpp145 andHolE→PAL26Del147 cross thresholds, confirmed by actual
    module gene lists. Five-strain context does not certify source assay strains;
    nonhits are not absence and hits are not assembly/formation/direct regulation.'
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-module-145
  - micro-ecoli-module-147
  - micro-historical-runner
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b0640
  - micro-ecoli-gene-b1099
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0184
  - micro-ecoli-gene-b0215
  - micro-ecoli-gene-b1842
  - micro-ecoli-gene-b3701
- assessment_id: micro-native-0
  area: schema
  topic: Actual native coverage and semantic limits
  outcome: supported
  summary: Five reviewed examples and5 COVERED typed nodes. Both current root native
    commands actually exit0. This does not settle exact family mapping or biological
    completeness. Original native validation/render also pass.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-native-dna_polymerase_iii_clamp_loader_complex-verify
  - micro-native-dna_polymerase_iii_clamp_loader_complex-causal
  - micro-original-audit
- assessment_id: micro-history-0
  area: provenance
  topic: Historical discussions and past corrections
  outcome: supported
  summary: Dated histories and discussions.rationale are retained as provenance; optional
    current-state clarification alone is not a defect. Any later family-mapping action
    must append evidence, preserve posed_date/rationale and narrow only current prompt/notes.
    No neighboring or grouped issue is terminally resolved here.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-prior-0
- assessment_id: micro-coverage-0
  area: completeness
  topic: All assigned maintained fields
  outcome: supported
  summary: Entire current record/original pair reviewed. No maintained image or measurement
    demands pixel/unit assessment. Optional blank slots are not findings; primary
    body, abstract, secondary review and authority tiers remain separate.
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-schema
- assessment_id: micro-verdict-0
  area: other
  topic: Current independent scientific verdict
  outcome: concern
  summary: 'needs_curation: two inherited minor composition/family findings remain;
    supported full-heptamer identity and graph retained.'
  target_ids:
  - GO:0043846
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-inputs-1
  area: provenance
  topic: Original source versus current target
  outcome: supported
  summary: Original frozen record is unchanged on current main. Original source revision/hashes
    and immutable YAML/Markdown were verified; current source reassessment does not
    erase historical limitations or invent refreshed stale fields.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-delta-1
  - micro-original-audit
- assessment_id: micro-adapter-1
  area: scope
  topic: Positive molecular claims require matched structured-source context
  outcome: concern
  summary: 'Original formal expression-only exclusion is unsupported: positive replication,
    clamp-loading or core catalytic claims trigger applicability. Fresh complete catalogue
    selects E.coli precise1k; nine exact reference loci each checked against201 module
    rows. Only HolD→ppGpp145 andHolE→PAL26Del147 cross thresholds, confirmed by actual
    module gene lists. Five-strain context does not certify source assay strains;
    nonhits are not absence and hits are not assembly/formation/direct regulation.'
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-module-145
  - micro-ecoli-module-147
  - micro-historical-runner
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b0640
  - micro-ecoli-gene-b1099
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0184
  - micro-ecoli-gene-b0215
  - micro-ecoli-gene-b1842
  - micro-ecoli-gene-b3701
- assessment_id: micro-native-1
  area: schema
  topic: Actual native coverage and semantic limits
  outcome: supported
  summary: Zero examples/typed protein nodes is deliberate complex-level scope; three
    STRUCTURE groundings checked independently. Both current root native commands
    actually exit0. This does not settle exact family mapping or biological completeness.
    Original native validation/render also pass.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-native-dna_polymerase_iii_complex-verify
  - micro-native-dna_polymerase_iii_complex-causal
  - micro-original-audit
- assessment_id: micro-history-1
  area: provenance
  topic: Historical discussions and past corrections
  outcome: supported
  summary: Dated histories and discussions.rationale are retained as provenance; optional
    current-state clarification alone is not a defect. Any later family-mapping action
    must append evidence, preserve posed_date/rationale and narrow only current prompt/notes.
    No neighboring or grouped issue is terminally resolved here.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-prior-1
- assessment_id: micro-coverage-1
  area: completeness
  topic: All assigned maintained fields
  outcome: supported
  summary: Entire current record/original pair reviewed. No maintained image or measurement
    demands pixel/unit assessment. Optional blank slots are not findings; primary
    body, abstract, secondary review and authority tiers remain separate.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-schema
- assessment_id: micro-verdict-1
  area: other
  topic: Current independent scientific verdict
  outcome: supported
  summary: 'pass_with_limitations: supported modular identity/components/function;
    Maki abstract-only methods limit and formation unknown retained. No scientific
    finding invented.'
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-inputs-2
  area: provenance
  topic: Original source versus current target
  outcome: supported
  summary: Original frozen record is unchanged on current main. Original source revision/hashes
    and immutable YAML/Markdown were verified; current source reassessment does not
    erase historical limitations or invent refreshed stale fields.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-delta-2
  - micro-original-audit
- assessment_id: micro-adapter-2
  area: scope
  topic: Positive molecular claims require matched structured-source context
  outcome: concern
  summary: 'Original formal expression-only exclusion is unsupported: positive replication,
    clamp-loading or core catalytic claims trigger applicability. Fresh complete catalogue
    selects E.coli precise1k; nine exact reference loci each checked against201 module
    rows. Only HolD→ppGpp145 andHolE→PAL26Del147 cross thresholds, confirmed by actual
    module gene lists. Five-strain context does not certify source assay strains;
    nonhits are not absence and hits are not assembly/formation/direct regulation.'
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-module-145
  - micro-ecoli-module-147
  - micro-historical-runner
  - micro-ecoli-gene-b0470
  - micro-ecoli-gene-b0640
  - micro-ecoli-gene-b1099
  - micro-ecoli-gene-b4259
  - micro-ecoli-gene-b4372
  - micro-ecoli-gene-b0184
  - micro-ecoli-gene-b0215
  - micro-ecoli-gene-b1842
  - micro-ecoli-gene-b3701
- assessment_id: micro-native-2
  area: schema
  topic: Actual native coverage and semantic limits
  outcome: supported
  summary: Three reviewed examples and3 COVERED typed nodes. Both current root native
    commands actually exit0. This does not settle exact family mapping or biological
    completeness. Original native validation/render also pass.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-native-dna_polymerase_iii_core_complex-verify
  - micro-native-dna_polymerase_iii_core_complex-causal
  - micro-original-audit
- assessment_id: micro-history-2
  area: provenance
  topic: Historical discussions and past corrections
  outcome: supported
  summary: Dated histories and discussions.rationale are retained as provenance; optional
    current-state clarification alone is not a defect. Any later family-mapping action
    must append evidence, preserve posed_date/rationale and narrow only current prompt/notes.
    No neighboring or grouped issue is terminally resolved here.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-prior-2
- assessment_id: micro-coverage-2
  area: completeness
  topic: All assigned maintained fields
  outcome: supported
  summary: Entire current record/original pair reviewed. No maintained image or measurement
    demands pixel/unit assessment. Optional blank slots are not findings; primary
    body, abstract, secondary review and authority tiers remain separate.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-schema
- assessment_id: micro-verdict-2
  area: other
  topic: Current independent scientific verdict
  outcome: concern
  summary: 'needs_curation: inherited minor exact theta-family mapping remains; correct
    examples and distinct activities retained.'
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-kind-1-root51-maki1988-publisher
  area: provenance
  topic: Historical failed-access evidence kind
  outcome: concern
  summary: Original HTTP403/body-access limit and context_only scope were honest,
    but evidence kind database is inappropriate for a failed-access diagnostic. Successor
    retains exact historical time/hash under validation/context_only without implying
    a new body read or refutation.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-prior-1
  - micro-historical-1-root51-maki1988-publisher
- assessment_id: micro-kind-1-root51-maki1988-pdf
  area: provenance
  topic: Historical failed-access evidence kind
  outcome: concern
  summary: Original HTTP403/body-access limit and context_only scope were honest,
    but evidence kind database is inappropriate for a failed-access diagnostic. Successor
    retains exact historical time/hash under validation/context_only without implying
    a new body read or refutation.
  target_ids:
  - GO:0009360
  evidence_ids:
  - micro-prior-1
  - micro-historical-1-root51-maki1988-pdf
- assessment_id: micro-kind-2-root51-maki1988-publisher
  area: provenance
  topic: Historical failed-access evidence kind
  outcome: concern
  summary: Original HTTP403/body-access limit and context_only scope were honest,
    but evidence kind database is inappropriate for a failed-access diagnostic. Successor
    retains exact historical time/hash under validation/context_only without implying
    a new body read or refutation.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-prior-2
  - micro-historical-2-root51-maki1988-publisher
- assessment_id: micro-kind-2-root51-maki1988-pdf
  area: provenance
  topic: Historical failed-access evidence kind
  outcome: concern
  summary: Original HTTP403/body-access limit and context_only scope were honest,
    but evidence kind database is inappropriate for a failed-access diagnostic. Successor
    retains exact historical time/hash under validation/context_only without implying
    a new body read or refutation.
  target_ids:
  - GO:0044776
  evidence_ids:
  - micro-prior-2
  - micro-historical-2-root51-maki1988-pdf
- assessment_id: plaque-t3-native-identities
  area: grounding
  topic: native identities
  outcome: supported
  summary: Current primary symbols/loci/reviewed accessions and S288C559292 match
    exactly; each bounded gene query returned one reviewed hit. Protein examples remain
    organism-specific instances rather than class groundings. Current native covered
    counts are 3/3, not the old frozen inventory.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-up-P22336
  - plaque-up-P26754
  - plaque-up-P26755
  - plaque-gene-RFA1
  - plaque-gene-RFA2
  - plaque-gene-RFA3
- assessment_id: plaque-t3-structured-source
  area: evidence
  topic: structured source
  outcome: concern
  summary: Complete positive protein/replication/binding or loading narrative triggers
    native structured-source applicability. Original notes[1] provides unsupported
    no-established-dataset prose, with no formal check; it is not a pure unexplained
    omission or formal exclusion. Fresh complete catalogue independently lacks the
    natural yeast host. No expression-to-assembly inference, bacterial expression-host
    proxy or fabricated downstream run.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t3-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Species-level budding yeast biology and S288C reference identities are
    distinct. No numeric prevalence census or arbitrary universal formation requirement
    is imposed. Experiments in BJ926/W303 derivatives, recombinant bacteria or archaeal
    RFC do not establish identical reference-strain provenance.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-tax-2759
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-cullmann1995-pdf
  - plaque-takayama2003-pmc
- assessment_id: plaque-t3-complete-fields
  area: completeness
  topic: complete fields
  outcome: supported
  summary: Complete current/original fields reviewed; no maintained images or quantitative
    organelle measurements asserted. Optional fields/examples are not mandatory enrichment.
    Current proposed status and dated historical rationale are preserved.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-original-3-yaml
  - plaque-checklist
- assessment_id: plaque-t3-native-provenance
  area: schema
  topic: native provenance
  outcome: supported
  summary: Original native validate/render and42 historical input occurrences pass;
    all47 current inputs frozen. Six current protein commands actually passed. Source
    membership/necessity findings are not disproven by schema success.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-original-current-validation
  - plaque-native-dna_replication_factor_a_complex-verify
  - plaque-native-dna_replication_factor_a_complex-causal
  - plaque-review-schema
- assessment_id: plaque-t4-native-identities
  area: grounding
  topic: native identities
  outcome: supported
  summary: Current primary symbols/loci/reviewed accessions and S288C559292 match
    exactly; each bounded gene query returned one reviewed hit. Protein examples remain
    organism-specific instances rather than class groundings. Current native covered
    counts are 5/5, not the old frozen inventory.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-up-P38630
  - plaque-up-P40348
  - plaque-up-P38629
  - plaque-up-P40339
  - plaque-up-P38251
  - plaque-gene-RFC1
  - plaque-gene-RFC2
  - plaque-gene-RFC3
  - plaque-gene-RFC4
  - plaque-gene-RFC5
- assessment_id: plaque-t4-structured-source
  area: evidence
  topic: structured source
  outcome: concern
  summary: Complete positive protein/replication/binding or loading narrative triggers
    native structured-source applicability. Original notes[1] provides unsupported
    no-established-dataset prose, with no formal check; it is not a pure unexplained
    omission or formal exclusion. Fresh complete catalogue independently lacks the
    natural yeast host. No expression-to-assembly inference, bacterial expression-host
    proxy or fabricated downstream run.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-original-4-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t4-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Species-level budding yeast biology and S288C reference identities are
    distinct. No numeric prevalence census or arbitrary universal formation requirement
    is imposed. Experiments in BJ926/W303 derivatives, recombinant bacteria or archaeal
    RFC do not establish identical reference-strain provenance.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-tax-2759
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-cullmann1995-pdf
  - plaque-takayama2003-pmc
- assessment_id: plaque-t4-complete-fields
  area: completeness
  topic: complete fields
  outcome: supported
  summary: Complete current/original fields reviewed; no maintained images or quantitative
    organelle measurements asserted. Optional fields/examples are not mandatory enrichment.
    Current proposed status and dated historical rationale are preserved.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-original-4-yaml
  - plaque-checklist
- assessment_id: plaque-t4-native-provenance
  area: schema
  topic: native provenance
  outcome: supported
  summary: Original native validate/render and42 historical input occurrences pass;
    all47 current inputs frozen. Six current protein commands actually passed. Source
    membership/necessity findings are not disproven by schema success.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-original-current-validation
  - plaque-native-dna_replication_factor_c_complex-verify
  - plaque-native-dna_replication_factor_c_complex-causal
  - plaque-review-schema
- assessment_id: plaque-t5-native-identities
  area: grounding
  topic: native identities
  outcome: supported
  summary: Current primary symbols/loci/reviewed accessions and S288C559292 match
    exactly; each bounded gene query returned one reviewed hit. Protein examples remain
    organism-specific instances rather than class groundings. Current native covered
    counts are 5/5, not the old frozen inventory.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-up-Q08032
  - plaque-up-Q03406
  - plaque-up-Q12488
  - plaque-up-P40359
  - plaque-up-Q12146
  - plaque-gene-CDC45
  - plaque-gene-SLD5
  - plaque-gene-PSF1
  - plaque-gene-PSF2
  - plaque-gene-PSF3
- assessment_id: plaque-t5-structured-source
  area: evidence
  topic: structured source
  outcome: concern
  summary: Complete positive protein/replication/binding or loading narrative triggers
    native structured-source applicability. Original notes[1] provides unsupported
    no-established-dataset prose, with no formal check; it is not a pure unexplained
    omission or formal exclusion. Fresh complete catalogue independently lacks the
    natural yeast host. No expression-to-assembly inference, bacterial expression-host
    proxy or fabricated downstream run.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-original-5-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-search
  - plaque-historical-adapter-unavailable
- assessment_id: plaque-t5-taxonomy
  area: scope
  topic: taxonomy
  outcome: supported
  summary: Species-level budding yeast biology and S288C reference identities are
    distinct. No numeric prevalence census or arbitrary universal formation requirement
    is imposed. Experiments in BJ926/W303 derivatives, recombinant bacteria or archaeal
    RFC do not establish identical reference-strain provenance.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-tax-2759
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-cullmann1995-pdf
  - plaque-takayama2003-pmc
- assessment_id: plaque-t5-complete-fields
  area: completeness
  topic: complete fields
  outcome: supported
  summary: Complete current/original fields reviewed; no maintained images or quantitative
    organelle measurements asserted. Optional fields/examples are not mandatory enrichment.
    Current proposed status and dated historical rationale are preserved.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-policy
  - plaque-schema
  - plaque-original-5-yaml
  - plaque-checklist
- assessment_id: plaque-t5-native-provenance
  area: schema
  topic: native provenance
  outcome: supported
  summary: Original native validate/render and42 historical input occurrences pass;
    all47 current inputs frozen. Six current protein commands actually passed. Source
    membership/necessity findings are not disproven by schema success.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-original-current-validation
  - plaque-native-dna_replication_preinitiation_complex-verify
  - plaque-native-dna_replication_preinitiation_complex-causal
  - plaque-review-schema
- assessment_id: plaque-t3-identity-composition
  area: identity
  topic: identity composition
  outcome: supported
  summary: Native GO/Wold review abstract supports heterotrimeric nonspecific ssDNA-binding
    RPA. Fresh Brill/Stillman primary abstract supports three yeast gene products;
    reviewed native entries corroborate heterotrimer identities. The approximate generic70/30/14classes
    need not equal precise yeast gel masses69/36/13.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-pmid-9242902
  - plaque-brill1991-meta
  - plaque-up-P22336
  - plaque-up-P26754
  - plaque-up-P26755
- assessment_id: plaque-t3-stale-refresh
  area: provenance
  topic: stale refresh
  outcome: supported
  summary: 'Compared original frozen record with current additions: RFA1/2/3 examples,
    gene symbols, Wold component/edge evidence and yeast canonical context. Native
    identities and independent yeast primary abstract support the biological additions.
    Wold full body remains unavailable; no precise S288C experimental-strain confirmation
    is inferred. Prior2470 repair does not resolve unchanged exact-family F1.'
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-original-current-validation
  - plaque-pmid-9242902
  - plaque-brill1991-meta
  - plaque-wold1997-publisher
  - plaque-up-P22336
  - plaque-up-P26754
  - plaque-up-P26755
- assessment_id: plaque-t3-family
  area: grounding
  topic: family
  outcome: concern
  summary: Exact native whole-protein families IPR004591/014646/013970 agree with
    current RFA1/2/3 xrefs; existing REVIEWED_LABEL_ONLY/open family task remains
    actionable despite new examples. Narrow yeast subgroup IPR016588 is not substituted
    for generic14kDa family.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-ipr-IPR004591
  - plaque-ipr-IPR014646
  - plaque-ipr-IPR013970
  - plaque-up-P22336
  - plaque-up-P26754
  - plaque-up-P26755
- assessment_id: plaque-t3-graph-necessity
  area: graph
  topic: graph necessity
  outcome: supported
  summary: NONMECHANISTIC three membership edges plus ssDNA-binding relation match
    supported composition/function. UNKNOWN formation values remain honest; Brill
    viability or cell-cycle transcription is not physical assembly necessity.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-brill1991-meta
  - plaque-pmid-9242902
  - plaque-graph-policy
- assessment_id: plaque-t4-identity-function
  area: identity
  topic: identity function
  outcome: supported
  summary: RFC identity/fork parthood/five-polypeptide eukaryotic scope and PCNA loading
    are supported by GO plus directly read Cullmann yeast source. Referenced archaeal
    Kitabayashi/Nishida contexts are not passed off as yeast RFC1–5 experiments.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-go
  - plaque-cullmann1995-pdf
  - plaque-pmid-8559655
  - plaque-pmid-14646196
  - plaque-pmid-16172520
- assessment_id: plaque-t4-family
  area: grounding
  topic: family
  outcome: concern
  summary: Exact RFC1 IPR012178 native family agrees with reviewed P38630; its label-only/open
    task remains unresolved. Broad IPR050238 and C-terminal IPR013748 do not establish
    exact individual RFC2–5 groundings; generated IPR050238 prose excluded.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-ipr-IPR012178
  - plaque-ipr-IPR050238
  - plaque-ipr-IPR013748
  - plaque-up-P38630
- assessment_id: plaque-t4-graph-necessity
  area: graph
  topic: graph necessity
  outcome: supported
  summary: NONMECHANISTIC membership/loading/function graph stays within current source
    scope. Cullmann disruption/tetrad tests establish viability, so UNKNOWN assembly
    values are not automatically upgraded; no mandatory new assay.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-cullmann1995-pdf
  - plaque-pmid-8559655
  - plaque-graph-policy
  - plaque-schema
- assessment_id: plaque-t4-unchanged-history
  area: provenance
  topic: unchanged history
  outcome: supported
  summary: Current RFC bytes equal original frozen target. Existing canonical example
    is species-level, not an invented S288C experimental strain. Historical rationale
    remains append-only; native current checks do not erase original access failures.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-current-4
  - plaque-original-4-yaml
  - plaque-original-current-validation
  - plaque-cullmann1995-pdf
- assessment_id: plaque-t5-identity-mechanism
  area: identity
  topic: identity mechanism
  outcome: concern
  summary: GO0031261 exactly denotes the protein-DNA preinitiation class. Its definition
    does not contain appended loaded-double-hexamer/kinase-target/CMG/bridge details.
    Takayama primary results support GINS identity and condition-scoped recruitment;
    detailed modern physical mechanism remains mismatched to supplied source.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-takayama2003-pmc
  - plaque-graph-policy
- assessment_id: plaque-t5-stale-refresh
  area: provenance
  topic: stale refresh
  outcome: supported
  summary: 'Only CDC45 example/history changed: current Q08032 reviewed primaryCDC45/S288C559292
    and nucleus ECO0000269 PMID8901577 join match native entry. Correct Hopwood primary
    abstract corroborates localization/complex context; no original scan pixels/body
    read asserted. This addition neither changes old mechanistic prose nor resolves
    exact-family or formation/graph findings.'
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-original-5-yaml
  - plaque-original-current-validation
  - plaque-up-Q08032
  - plaque-gene-CDC45
  - plaque-pmid-8901577
  - plaque-hopwood1996-correct-pmc
- assessment_id: plaque-t5-composition-families
  area: grounding
  topic: composition families
  outcome: concern
  summary: Fresh GINS purification supports four distinct subunits; reviewed five
    examples and native exact families agree. Sld5IPR008591/Psf1IPR005339 retry responses
    succeeded after429; Psf2IPR007257/Psf3IPR010492/Cdc45IPR003874 verify whole-protein
    classes. Current missing grounding is distinct from optional examples and MCM
    is already GO-grounded.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-takayama2003-pmc
  - plaque-ipr-IPR008591-retry
  - plaque-ipr-IPR005339-retry
  - plaque-ipr-IPR007257
  - plaque-ipr-IPR010492
  - plaque-ipr-IPR003874
  - plaque-up-Q08032
  - plaque-up-Q03406
  - plaque-up-Q12488
  - plaque-up-P40359
  - plaque-up-Q12146
- assessment_id: plaque-t5-formation
  area: scope
  topic: formation
  outcome: concern
  summary: Takayama tests conditional GINS recovery, origin occupancy and replication;
    Hopwood abstract reports Cdc45-Mcm5 association/initiation. These supplied citations
    do not establish both current pre-IC MCM/Cdc45 physical-formation ESSENTIAL assertions
    at their stated scope. Retain a localized evidence qualification; do not infer
    dispensability, require a universal all-species assay or downgrade defining constituents
    solely because they are constituents.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-schema
  - plaque-policy
  - plaque-takayama2003-pmc
  - plaque-pmid-8901577
- assessment_id: plaque-t5-graph-scope
  area: graph
  topic: graph scope
  outcome: concern
  summary: Eight edges encode six memberships, nucleoplasm placement and generic replication;
    MECHANISTIC assembly/function label overstates the encoded topology. GO0006260
    identifies the process but does not alone support pre-IC-specific causation. Source-supported
    conditional recruitment could be separately encoded; no automatic structural-node
    type finding.
  target_ids:
  - GO:0031261
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-graph-policy
  - plaque-takayama2003-pmc
- assessment_id: plaque-t3-access-kind-historical-micro51-wold1997-publisher
  area: provenance
  topic: access kind historical micro51 wold1997 publisher
  outcome: concern
  summary: Historical access-only observation is database/context_only; successor
    should use validation/context_only. Original source scopes explicitly disclose
    blocked/redirect/download-shell access, so no allegation of false fulltext reading.
  target_ids:
  - GO:0005662
  evidence_ids:
  - plaque-historical-micro51-wold1997-publisher
  - plaque-original-3-yaml
  - plaque-review-schema
- assessment_id: plaque-t4-access-kind-historical-micro51-kim2003-publisher
  area: provenance
  topic: access kind historical micro51 kim2003 publisher
  outcome: concern
  summary: Historical access-only observation is database/context_only; successor
    should use validation/context_only. Original source scopes explicitly disclose
    blocked/redirect/download-shell access, so no allegation of false fulltext reading.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-historical-micro51-kim2003-publisher
  - plaque-original-4-yaml
  - plaque-review-schema
- assessment_id: plaque-t4-access-kind-historical-micro51-kitabayashi2003-publisher
  area: provenance
  topic: access kind historical micro51 kitabayashi2003 publisher
  outcome: concern
  summary: Historical access-only observation is database/context_only; successor
    should use validation/context_only. Original source scopes explicitly disclose
    blocked/redirect/download-shell access, so no allegation of false fulltext reading.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-historical-micro51-kitabayashi2003-publisher
  - plaque-original-4-yaml
  - plaque-review-schema
- assessment_id: plaque-t4-access-kind-historical-micro51-cullmann1995-pdf
  area: provenance
  topic: access kind historical micro51 cullmann1995 pdf
  outcome: concern
  summary: Historical access-only observation is database/context_only; successor
    should use validation/context_only. Original source scopes explicitly disclose
    blocked/redirect/download-shell access, so no allegation of false fulltext reading.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-historical-micro51-cullmann1995-pdf
  - plaque-original-4-yaml
  - plaque-review-schema
- assessment_id: plaque-t4-access-kind-historical-micro51-gary1995-pdf
  area: provenance
  topic: access kind historical micro51 gary1995 pdf
  outcome: concern
  summary: Historical access-only observation is database/context_only; successor
    should use validation/context_only. Original source scopes explicitly disclose
    blocked/redirect/download-shell access, so no allegation of false fulltext reading.
  target_ids:
  - GO:0005663
  evidence_ids:
  - plaque-historical-micro51-gary1995-pdf
  - plaque-original-4-yaml
  - plaque-review-schema
- assessment_id: septin-dna_topoisomerase_iv_complex-identity
  area: identity
  topic: Exact identity and assembly boundary
  outcome: supported
  summary: Exact ParC/ParE TopoIV identity and typeIIA function; correct generic bacterial
    scope without copying the upstream heterodimer error.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
- assessment_id: septin-dna_topoisomerase_iv_complex-hierarchy
  area: identity
  topic: Native parents and parthood
  outcome: supported
  summary: Typed parent and named subassembly claims match current GO. Is-a, has-part
    and interaction are not conflated, and unrelated adjacent components are not mandatory
    additions.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
- assessment_id: septin-dna_topoisomerase_iv_complex-grounding
  area: grounding
  topic: Component class versus protein example
  outcome: supported
  summary: Inspected ParC/ParE candidates are narrower taxonomic families or broader
    topoisomerase classes; existing label-only scope remains justified.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-retry-IPR005742
  - septin-ipr-IPR005737
  - septin-retry-IPR050220
  - septin-ipr-IPR001241
  - septin-curation-policy
  - septin-up-P0AFI2
  - septin-up-P20083
- assessment_id: septin-dna_topoisomerase_iv_complex-protein-identity
  area: grounding
  topic: Reviewed accessions and native coverage
  outcome: supported
  summary: 2 reviewed example occurrences and 2 COVERED protein nodes agree with native
    accession/gene/taxon data. Identity and family provenance do not themselves demonstrate
    complex membership.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-up-P0AFI2
  - septin-up-P20083
  - septin-query-parC
  - septin-query-parE
  - septin-native-dna_topoisomerase_iv_complex-verify
  - septin-native-dna_topoisomerase_iv_complex-causal
- assessment_id: septin-dna_topoisomerase_iv_complex-formation
  area: grounding
  topic: Formation evidence versus activity or viability
  outcome: unknown
  summary: Truncation-sensitive association is measured, but no optional formation
    enum is asserted by this target; catalytic ATP use is not an assembly requirement.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-schema-policy
- assessment_id: septin-dna_topoisomerase_iv_complex-graph
  area: graph
  topic: Coarse function and mechanistic boundaries
  outcome: supported
  summary: Explicit NONMECHANISTIC activity graph is supported; detailed cleavage/strand-passage/ATPase
    states are not asserted.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-graph-policy
- assessment_id: septin-dna_topoisomerase_iv_complex-stoichiometry
  area: grounding
  topic: Measured numbers and scope
  outcome: not_applicable
  summary: No invariant complex copy-number field is asserted. Assay-specific ratios
    do not force optional stoichiometry or universal structure counts.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-schema-policy
- assessment_id: septin-dna_topoisomerase_iv_complex-taxa
  area: scope
  topic: Species and experimental strain boundaries
  outcome: supported
  summary: E.coli species562 and K12 reference83333 identities are correct. Reference
    accessions do not equate all mutants/recombinant preparations with precise1k strains.
    No distribution prevalence row is asserted.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-tax-562
  - septin-tax-83333
  - septin-up-P0AFI2
  - septin-up-P20083
- assessment_id: septin-dna_topoisomerase_iv_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger the policy. Original formal
    exclusion solely because no expression-module claim is unsupported. Current official
    catalogue covers E.coli; bounded precise1k gene/module checks provide context
    only. All assigned queried loci have false membership flags across201 modules;
    this does not refute their genes, expression or structure roles.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-original-dna_topoisomerase_iv_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
  - septin-modulemembers-parC
  - septin-modulemembers-parE
  - septin-modulegene-parC
  - septin-modulegene-parE
- assessment_id: septin-dna_topoisomerase_iv_complex-schema
  area: schema
  topic: Original native validity and frozen inputs
  outcome: supported
  summary: Original validate/render0 and exact Markdown; all13 frozen historical inputs
    match. Current target hash unchanged; actual native protein checks0. Historical
    batch26 corpus runs remain valid scoped provenance, not current-head/CI success.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-original-dna_topoisomerase_iv_complex
  - septin-original-native-checks
  - septin-native-dna_topoisomerase_iv_complex-verify
  - septin-native-dna_topoisomerase_iv_complex-causal
- assessment_id: septin-dna_topoisomerase_iv_complex-history
  area: provenance
  topic: Historical questions and current corrective scope
  outcome: supported
  summary: Dated discussion rationale and curation history remain intact. Any future
    curation updates current notes/status or appends a dated clarification; no historical
    rewriting, automatic status promotion or neighboring issue disposition.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-original-dna_topoisomerase_iv_complex
  - septin-curation-policy
- assessment_id: septin-dna_topoisomerase_iv_complex-coverage
  area: completeness
  topic: Complete current record and explicit access limits
  outcome: supported
  summary: Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all
    graph edges and discussions/history assessed. No maintained images; no figure
    pixels,supplements,coordinates or independent data reanalysis claimed. Optional
    fields do not automatically create findings.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-literature-policy
- assessment_id: septin-dna_topoisomerase_iv_complex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: supported
  summary: Qualified positive pass; exact family boundary,reference identities and
    coarse function remain supported.
  target_ids:
  - GO:0009340
  evidence_ids:
  - septin-record-dna_topoisomerase_iv_complex
  - septin-go
  - septin-peng-primary
  - septin-peng-primary-context
  - septin-pmid-8227000
  - septin-pmid-7783632
  - septin-retry-IPR005742
  - septin-ipr-IPR005737
  - septin-retry-IPR050220
  - septin-ipr-IPR001241
  - septin-curation-policy
- assessment_id: septin-dnaa_diaa_complex-identity
  area: identity
  topic: Exact identity and assembly boundary
  outcome: supported
  summary: Exact DiaA-DnaA-oriC nucleoprotein identity and named subassemblies; later
    helicase-loading machinery remains a separate boundary.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
- assessment_id: septin-dnaa_diaa_complex-hierarchy
  area: identity
  topic: Native parents and parthood
  outcome: supported
  summary: Typed parent and named subassembly claims match current GO. Is-a, has-part
    and interaction are not conflated, and unrelated adjacent components are not mandatory
    additions.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
- assessment_id: septin-dnaa_diaa_complex-grounding
  area: grounding
  topic: Component class versus protein example
  outcome: concern
  summary: Current exact authority family/oriC terms match declared classes. Existing
    REVIEWED_LABEL_ONLY notes merely defer curation; this remains the inherited localized
    grounding finding, not a missing optional-example demand.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-retry-IPR023070
  - septin-ipr-IPR001957
  - septin-so
  - septin-curation-policy
  - septin-up-P66817
  - septin-up-P03004
- assessment_id: septin-dnaa_diaa_complex-protein-identity
  area: grounding
  topic: Reviewed accessions and native coverage
  outcome: supported
  summary: 2 reviewed example occurrences and 2 COVERED protein nodes agree with native
    accession/gene/taxon data. Identity and family provenance do not themselves demonstrate
    complex membership.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-up-P66817
  - septin-up-P03004
  - septin-query-dnaA
  - septin-query-diaA
  - septin-native-dnaa_diaa_complex-verify
  - septin-native-dnaa_diaa_complex-causal
- assessment_id: septin-dnaa_diaa_complex-formation
  area: grounding
  topic: Formation evidence versus activity or viability
  outcome: unknown
  summary: Tetramer/interface assays support particular binding/stimulation effects,
    not a universal requirement for every constituent under every condition.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-schema-policy
- assessment_id: septin-dnaa_diaa_complex-graph
  area: graph
  topic: Coarse function and mechanistic boundaries
  outcome: supported
  summary: Assembly and initiation-promotion graph remains coarse; phosphosugar control
    and later helicase loading are not established edges.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-graph-policy
- assessment_id: septin-dnaa_diaa_complex-stoichiometry
  area: grounding
  topic: Measured numbers and scope
  outcome: supported
  summary: Four copies are explicitly per DiaA tetramer, not a fixed total for the
    whole origin assembly.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-schema-policy
- assessment_id: septin-dnaa_diaa_complex-taxa
  area: scope
  topic: Species and experimental strain boundaries
  outcome: supported
  summary: E.coli species562 and K12 reference83333 identities are correct. Reference
    accessions do not equate all mutants/recombinant preparations with precise1k strains.
    COMMON is qualitative curation, not a numerical strain-prevalence census established
    by these experiments.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-tax-562
  - septin-tax-83333
  - septin-up-P66817
  - septin-up-P03004
- assessment_id: septin-dnaa_diaa_complex-localization-provenance
  area: provenance
  topic: DnaA experimental annotation provenance
  outcome: supported
  summary: Native P03004 explicitly links the three localization citations. Regev
    uses membrane-association context; Schenk includes B.subtilis and E.coli; Garner
    is artificial-bilayer insertion. These support their annotation provenance at
    abstract/native tier, not whole-complex localization or identical reference-strain
    experiments.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-up-P03004
  - septin-pmid-22574163
  - septin-pmid-28166228
  - septin-pmid-9478970
- assessment_id: septin-dnaa_diaa_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger the policy. Original formal
    exclusion solely because no expression-module claim is unsupported. Current official
    catalogue covers E.coli; bounded precise1k gene/module checks provide context
    only. All assigned queried loci have false membership flags across201 modules;
    this does not refute their genes, expression or structure roles.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-original-dnaa_diaa_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
  - septin-modulemembers-dnaA
  - septin-modulemembers-diaA
  - septin-modulegene-dnaA
  - septin-modulegene-diaA
- assessment_id: septin-dnaa_diaa_complex-schema
  area: schema
  topic: Original native validity and frozen inputs
  outcome: supported
  summary: Original validate/render0 and exact Markdown; all13 frozen historical inputs
    match. Current target hash unchanged; actual native protein checks0. Historical
    batch26 corpus runs remain valid scoped provenance, not current-head/CI success.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-original-dnaa_diaa_complex
  - septin-original-native-checks
  - septin-native-dnaa_diaa_complex-verify
  - septin-native-dnaa_diaa_complex-causal
- assessment_id: septin-dnaa_diaa_complex-history
  area: provenance
  topic: Historical questions and current corrective scope
  outcome: supported
  summary: Dated discussion rationale and curation history remain intact. Any future
    curation updates current notes/status or appends a dated clarification; no historical
    rewriting, automatic status promotion or neighboring issue disposition.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-original-dnaa_diaa_complex
  - septin-curation-policy
- assessment_id: septin-dnaa_diaa_complex-coverage
  area: completeness
  topic: Complete current record and explicit access limits
  outcome: supported
  summary: Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all
    graph edges and discussions/history assessed. No maintained images; no figure
    pixels,supplements,coordinates or independent data reanalysis claimed. Optional
    fields do not automatically create findings.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-literature-policy
- assessment_id: septin-dnaa_diaa_complex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: Needs curation for 1 independently reconfirmed inherited minor finding(s);
    supported identity,function and source boundaries remain intact.
  target_ids:
  - GO:1990102
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-go
  - septin-keyamura-primary
  - septin-keyamura-primary-early
  - septin-pmid-17699754
  - septin-pmid-15326179
  - septin-retry-IPR023070
  - septin-ipr-IPR001957
  - septin-so
  - septin-curation-policy
- assessment_id: septin-dnaa_dnab_dnac_complex-identity
  area: identity
  topic: Exact identity and assembly boundary
  outcome: supported
  summary: Exact primase-free prepriming intermediate with DnaA,originDNA and whole
    DnaB-DnaC loading subcomplex. Primase triggers a later transition.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
- assessment_id: septin-dnaa_dnab_dnac_complex-hierarchy
  area: identity
  topic: Native parents and parthood
  outcome: supported
  summary: Typed parent and named subassembly claims match current GO. Is-a, has-part
    and interaction are not conflated, and unrelated adjacent components are not mandatory
    additions.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
- assessment_id: septin-dnaa_dnab_dnac_complex-grounding
  area: grounding
  topic: Component class versus protein example
  outcome: concern
  summary: Current exact authority family/oriC terms match declared classes. Existing
    REVIEWED_LABEL_ONLY notes merely defer curation; this remains the inherited localized
    grounding finding, not a missing optional-example demand.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-ipr-IPR001957
  - septin-so
  - septin-curation-policy
  - septin-up-P03004
- assessment_id: septin-dnaa_dnab_dnac_complex-protein-identity
  area: grounding
  topic: Reviewed accessions and native coverage
  outcome: supported
  summary: 1 reviewed example occurrences and 1 COVERED protein nodes agree with native
    accession/gene/taxon data. Identity and family provenance do not themselves demonstrate
    complex membership.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-up-P03004
  - septin-query-dnaA
  - septin-native-dnaa_dnab_dnac_complex-verify
  - septin-native-dnaa_dnab_dnac_complex-causal
- assessment_id: septin-dnaa_dnab_dnac_complex-formation
  area: grounding
  topic: Formation evidence versus activity or viability
  outcome: concern
  summary: S8 oriC-versus-vector comparison directly tests DnaB retention in an isolated
    prepriming preparation. Blanket UNKNOWN omits this condition-scoped formation
    evidence; no universal viability or every-subunit requirement follows.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-schema-policy
- assessment_id: septin-dnaa_dnab_dnac_complex-graph
  area: graph
  topic: Coarse function and mechanistic boundaries
  outcome: supported
  summary: Loading/initiation graph excludes ring opening,DnaC-release chemistry and
    later primase recruitment; assembled mutant complexes can lack later replication
    activity.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-graph-policy
- assessment_id: septin-dnaa_dnab_dnac_complex-stoichiometry
  area: grounding
  topic: Measured numbers and scope
  outcome: not_applicable
  summary: No invariant complex copy-number field is asserted. Assay-specific ratios
    do not force optional stoichiometry or universal structure counts.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-schema-policy
- assessment_id: septin-dnaa_dnab_dnac_complex-taxa
  area: scope
  topic: Species and experimental strain boundaries
  outcome: supported
  summary: E.coli species562 and K12 reference83333 identities are correct. Reference
    accessions do not equate all mutants/recombinant preparations with precise1k strains.
    COMMON is qualitative curation, not a numerical strain-prevalence census established
    by these experiments.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-tax-562
  - septin-tax-83333
  - septin-up-P03004
- assessment_id: septin-dnaa_dnab_dnac_complex-localization-provenance
  area: provenance
  topic: DnaA experimental annotation provenance
  outcome: supported
  summary: Native P03004 explicitly links the three localization citations. Regev
    uses membrane-association context; Schenk includes B.subtilis and E.coli; Garner
    is artificial-bilayer insertion. These support their annotation provenance at
    abstract/native tier, not whole-complex localization or identical reference-strain
    experiments.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-up-P03004
  - septin-pmid-22574163
  - septin-pmid-28166228
  - septin-pmid-9478970
- assessment_id: septin-dnaa_dnab_dnac_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger the policy. Original formal
    exclusion solely because no expression-module claim is unsupported. Current official
    catalogue covers E.coli; bounded precise1k gene/module checks provide context
    only. All assigned queried loci have false membership flags across201 modules;
    this does not refute their genes, expression or structure roles.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-original-dnaa_dnab_dnac_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
  - septin-modulemembers-dnaA
  - septin-modulemembers-dnaB
  - septin-modulemembers-dnaC
  - septin-modulegene-dnaA
  - septin-modulegene-dnaB
  - septin-modulegene-dnaC
- assessment_id: septin-dnaa_dnab_dnac_complex-schema
  area: schema
  topic: Original native validity and frozen inputs
  outcome: supported
  summary: Original validate/render0 and exact Markdown; all13 frozen historical inputs
    match. Current target hash unchanged; actual native protein checks0. Historical
    batch26 corpus runs remain valid scoped provenance, not current-head/CI success.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-original-dnaa_dnab_dnac_complex
  - septin-original-native-checks
  - septin-native-dnaa_dnab_dnac_complex-verify
  - septin-native-dnaa_dnab_dnac_complex-causal
- assessment_id: septin-dnaa_dnab_dnac_complex-history
  area: provenance
  topic: Historical questions and current corrective scope
  outcome: supported
  summary: Dated discussion rationale and curation history remain intact. Any future
    curation updates current notes/status or appends a dated clarification; no historical
    rewriting, automatic status promotion or neighboring issue disposition.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-original-dnaa_dnab_dnac_complex
  - septin-curation-policy
- assessment_id: septin-dnaa_dnab_dnac_complex-coverage
  area: completeness
  topic: Complete current record and explicit access limits
  outcome: supported
  summary: Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all
    graph edges and discussions/history assessed. No maintained images; no figure
    pixels,supplements,coordinates or independent data reanalysis claimed. Optional
    fields do not automatically create findings.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-literature-policy
- assessment_id: septin-dnaa_dnab_dnac_complex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: Needs curation for 2 independently reconfirmed inherited minor finding(s);
    supported identity,function and source boundaries remain intact.
  target_ids:
  - GO:1990157
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-go
  - septin-makowska-s3
  - septin-pmid-20129058
  - septin-ipr-IPR001957
  - septin-so
  - septin-curation-policy
- assessment_id: septin-dnaa_dps_complex-identity
  area: identity
  topic: Exact identity and assembly boundary
  outcome: supported
  summary: Direct DnaA-Dps protein association defines this complex; RIDA/Hda/beta-clamp
    neighbors remain distinct.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
- assessment_id: septin-dnaa_dps_complex-hierarchy
  area: identity
  topic: Native parents and parthood
  outcome: supported
  summary: Typed parent and named subassembly claims match current GO. Is-a, has-part
    and interaction are not conflated, and unrelated adjacent components are not mandatory
    additions.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
- assessment_id: septin-dnaa_dps_complex-grounding
  area: grounding
  topic: Component class versus protein example
  outcome: concern
  summary: Current exact authority family/oriC terms match declared classes. Existing
    REVIEWED_LABEL_ONLY notes merely defer curation; this remains the inherited localized
    grounding finding, not a missing optional-example demand.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-ipr-IPR001957
  - septin-ipr-IPR002177
  - septin-curation-policy
  - septin-up-P03004
  - septin-up-P0ABT2
- assessment_id: septin-dnaa_dps_complex-protein-identity
  area: grounding
  topic: Reviewed accessions and native coverage
  outcome: supported
  summary: 2 reviewed example occurrences and 2 COVERED protein nodes agree with native
    accession/gene/taxon data. Identity and family provenance do not themselves demonstrate
    complex membership.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-up-P03004
  - septin-up-P0ABT2
  - septin-query-dnaA
  - septin-query-dps
  - septin-native-dnaa_dps_complex-verify
  - septin-native-dnaa_dps_complex-causal
- assessment_id: septin-dnaa_dps_complex-formation
  area: grounding
  topic: Formation evidence versus activity or viability
  outcome: unknown
  summary: Binding/inhibition evidence does not establish universal formation necessity
    or invariant DnaA:Dps stoichiometry.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-schema-policy
- assessment_id: septin-dnaa_dps_complex-graph
  area: graph
  topic: Coarse function and mechanistic boundaries
  outcome: supported
  summary: Negative initiation graph remains conditional; oxidative-stress checkpoint
    and adaptive mutation are not established detailed pathways.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-graph-policy
- assessment_id: septin-dnaa_dps_complex-stoichiometry
  area: grounding
  topic: Measured numbers and scope
  outcome: not_applicable
  summary: No invariant complex copy-number field is asserted. Assay-specific ratios
    do not force optional stoichiometry or universal structure counts.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-schema-policy
- assessment_id: septin-dnaa_dps_complex-taxa
  area: scope
  topic: Species and experimental strain boundaries
  outcome: supported
  summary: E.coli species562 and K12 reference83333 identities are correct. Reference
    accessions do not equate all mutants/recombinant preparations with precise1k strains.
    COMMON is qualitative curation, not a numerical strain-prevalence census established
    by these experiments.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-tax-562
  - septin-tax-83333
  - septin-up-P03004
  - septin-up-P0ABT2
- assessment_id: septin-dnaa_dps_complex-localization-provenance
  area: provenance
  topic: DnaA experimental annotation provenance
  outcome: supported
  summary: Native P03004 explicitly links the three localization citations. Regev
    uses membrane-association context; Schenk includes B.subtilis and E.coli; Garner
    is artificial-bilayer insertion. These support their annotation provenance at
    abstract/native tier, not whole-complex localization or identical reference-strain
    experiments.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-up-P03004
  - septin-pmid-22574163
  - septin-pmid-28166228
  - septin-pmid-9478970
- assessment_id: septin-dnaa_dps_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger the policy. Original formal
    exclusion solely because no expression-module claim is unsupported. Current official
    catalogue covers E.coli; bounded precise1k gene/module checks provide context
    only. dps is above threshold in OxyR3/RpoS51; other named queried loci are below
    all201 thresholds, not biologically absent.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-original-dnaa_dps_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
  - septin-modulemembers-dnaA
  - septin-modulemembers-dps
  - septin-modulegene-dnaA
  - septin-modulegene-dps
  - septin-module-3
  - septin-module-3-genes
  - septin-module-51
  - septin-module-51-genes
- assessment_id: septin-dnaa_dps_complex-schema
  area: schema
  topic: Original native validity and frozen inputs
  outcome: supported
  summary: Original validate/render0 and exact Markdown; all13 frozen historical inputs
    match. Current target hash unchanged; actual native protein checks0. Historical
    batch26 corpus runs remain valid scoped provenance, not current-head/CI success.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-original-dnaa_dps_complex
  - septin-original-native-checks
  - septin-native-dnaa_dps_complex-verify
  - septin-native-dnaa_dps_complex-causal
- assessment_id: septin-dnaa_dps_complex-history
  area: provenance
  topic: Historical questions and current corrective scope
  outcome: supported
  summary: Dated discussion rationale and curation history remain intact. Any future
    curation updates current notes/status or appends a dated clarification; no historical
    rewriting, automatic status promotion or neighboring issue disposition.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-original-dnaa_dps_complex
  - septin-curation-policy
- assessment_id: septin-dnaa_dps_complex-coverage
  area: completeness
  topic: Complete current record and explicit access limits
  outcome: supported
  summary: Definition,aliases,parents,parts,components/examples,taxa,functions,evidence,all
    graph edges and discussions/history assessed. No maintained images; no figure
    pixels,supplements,coordinates or independent data reanalysis claimed. Optional
    fields do not automatically create findings.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-literature-policy
- assessment_id: septin-dnaa_dps_complex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: Needs curation for 1 independently reconfirmed inherited minor finding(s);
    supported identity,function and source boundaries remain intact.
  target_ids:
  - GO:1990084
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-go
  - septin-chodavarapu-primary
  - septin-chodavarapu-primary-binding
  - septin-pmid-18284581
  - septin-ipr-IPR001957
  - septin-ipr-IPR002177
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
  - GO:0043846
  - GO:0009360
  - GO:0044776
  - GO:0005662
  - GO:0005663
  - GO:0031261
  - GO:0009340
  - GO:1990102
  - GO:1990157
  - GO:1990084
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
  issue_key: pol-iii-clamp-loader-dnax-mixture
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: State the three DnaX copies and their alternatives
  description: The definition unconditionally says the heptamer includes tau and gamma.
    Its cited McHenry2003 body p1158 instead specifies DnaX3-delta-delta-prime-chi-psi
    with any mixture of tau and gamma for clamp loading, and native DnaX annotations
    agree. The original GO sentence matches the record but compresses the source distinction.
  target_ids:
  - GO:0043846
  field_paths:
  - definition
  - components#dnax_tau_gamma_subunit.role
  evidence_ids:
  - micro-record-0
  - micro-go-0043846
  - micro-mchenry2003-pdf
  - micro-jeruzalmi2001-pdf
  - micro-pmid-3283127
  - micro-up-P06710
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-scoped composition
  native_severity: minor
  normalization_reason: Correct structure identity, supported protein examples and
    core functional model remain intact; the defect is a bounded mapping or composition-wording
    gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2923
- finding_id: micro-F2
  issue_key: pol-iii-clamp-loader-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the available HolA, HolC and HolD families
  description: HolA, HolC and HolD remain REVIEWED_LABEL_ONLY despite current exact
    whole-protein families IPR005790, IPR007459 and IPR004615 with matching maintained-example
    xrefs. Inspected DnaX/HolB alternatives are domains or broader shared families
    and do not justify a forced whole-protein mapping.
  target_ids:
  - GO:0043846
  field_paths:
  - components#delta_subunit.grounding_status
  - components#chi_subunit.grounding_status
  - components#psi_subunit.grounding_status
  - discussions#resolve_pol_iii_clamp_loader_groundings
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR005790
  - micro-ipr-IPR007459
  - micro-ipr-IPR004615
  - micro-up-P28630
  - micro-up-P28905
  - micro-up-P28632
  - micro-ipr-IPR004622
  - micro-ipr-IPR012763-retry
  - micro-ipr-IPR050238
  - micro-ipr-IPR048731-retry
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-scoped composition
  native_severity: minor
  normalization_reason: Correct structure identity, supported protein examples and
    core functional model remain intact; the defect is a bounded mapping or composition-wording
    gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2924
- finding_id: micro-F3
  issue_key: pol-iii-core-theta-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the theta subunit with its exact family
  description: HolE remains REVIEWED_LABEL_ONLY and the current TODO defers all three
    core classes, although native IPR009052 is an exact full-protein theta family
    and P0ABS8 independently carries that family xref. Other inspected candidates
    are broader or taxon-limited.
  target_ids:
  - GO:0044776
  field_paths:
  - components#theta_subunit.grounding_status
  - discussions#resolve_pol_iii_core_subunit_groundings
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR009052-retry
  - micro-up-P0ABS8
  - micro-ipr-IPR006309-retry
  - micro-ipr-IPR006054
  - micro-ipr-IPR004805
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-scoped composition
  native_severity: minor
  normalization_reason: Correct structure identity, supported protein examples and
    core functional model remain intact; the defect is a bounded mapping or composition-wording
    gap.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055921Z-dna-polymerase-iii-core-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2925
- finding_id: plaque-t3-F1
  issue_key: dna-replication-factor-a-complex-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified exact subunit family grounding
  description: The three existing RPA size-defined protein classes have exact source-neutral
    whole-protein families:70kDa IPR004591, approximately30/32kDa IPR014646 and14kDa
    IPR013970. Native family type/name/signatures plus independent reviewed RFA1/2/3
    xrefs establish the matches. The narrower yeast Rfa3 subgroup is not substituted
    for the generic14kDa class. Historical statements about what was curated in an
    earlier pass are preserved as history, not declared fabricated.
  target_ids:
  - GO:0005662
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-ipr-IPR004591
  - plaque-ipr-IPR014646
  - plaque-ipr-IPR013970
  - plaque-up-P22336
  - plaque-up-P26754
  - plaque-up-P26755
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_a_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: The biological class, composition and protein identities remain
    correct. This is a bounded actionable class-grounding gap under the explicit REVIEWED_LABEL_ONLY
    contract, not a missing optional example inventory.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055922Z-dna-replication-factor-a-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2926
- finding_id: plaque-t4-F1
  issue_key: dna-replication-factor-c-complex-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified exact subunit family grounding
  description: The named RFC1 large-subunit class exactly matches IPR012178, verified
    from native family metadata/signature and the maintained P38630 UniProt cross-reference.
    The current REVIEWED_LABEL_ONLY row and OPEN task leave this resolvable match
    unrepresented. No exact RFC2–5 mapping is established by broad IPR050238 or C-terminal
    IPR013748. Historical statements about what was curated in an earlier pass are
    preserved as history, not declared fabricated.
  target_ids:
  - GO:0005663
  field_paths:
  - components[0].grounding_status
  - discussions[0]
  evidence_ids:
  - plaque-current-4
  - plaque-policy
  - plaque-ipr-IPR012178
  - plaque-up-P38630
  - plaque-ipr-IPR050238
  - plaque-ipr-IPR013748
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_c_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: The biological class, composition and protein identities remain
    correct. This is a bounded actionable class-grounding gap under the explicit REVIEWED_LABEL_ONLY
    contract, not a missing optional example inventory.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055923Z-dna-replication-factor-c-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2927
- finding_id: plaque-t5-F1
  issue_key: dna-preinitiation-modern-mechanism-source-overstatement
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Source or qualify the added modern preinitiation mechanism
  description: The definition names GO0031261 but appends loaded MCM double-hexamer/kinase-target/CMG
    details outside that definition. MCM/Cdc45 roles and repeated graph prose attribute
    these details, including a Mcm2–Mcm5 bridge, to Takayama2003. The inspected source
    identifies GINS and conditional origin-recruitment dependencies; it does not demonstrate
    that detailed physical and phosphorylation mechanism. The supported partial observations
    should remain distinct from later mechanistic knowledge.
  target_ids:
  - GO:0031261
  field_paths:
  - definition
  - definition_source
  - components[0].role
  - components[0].evidence[0].notes
  - components[1].role
  - components[1].evidence[0].notes
  - causal_graphs[0].nodes[1].description
  - causal_graphs[0].nodes[2].description
  - causal_graphs[0].edges[0]
  - causal_graphs[0].edges[1]
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-takayama2003-pmc
  - plaque-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: major
  normalization_reason: This is a substantive source-support expansion in the defining
    mechanism and component roles, not merely a bibliographic typo. Exact pre-IC identity
    and the paper’s observed recruitment biology remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055923Z-dna-replication-preinitiation-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2928
- finding_id: plaque-t5-F2
  issue_key: dna-preinitiation-exact-five-protein-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve exact GINS and Cdc45 protein-family classes
  description: Exact whole-protein families are available for Sld5 IPR008591, Psf1
    IPR005339, Psf2 IPR007257, Psf3 IPR010492 and Cdc45 IPR003874. Separate native
    family metadata and reviewed UniProt xrefs corroborate them. The four label-only
    GINS rows and ungrounded named Cdc45 class can be resolved; this does not require
    extra optional protein examples.
  target_ids:
  - GO:0031261
  field_paths:
  - components[1]
  - components[2].grounding_status
  - components[3].grounding_status
  - components[4].grounding_status
  - components[5].grounding_status
  evidence_ids:
  - plaque-current-5
  - plaque-policy
  - plaque-ipr-IPR008591-retry
  - plaque-ipr-IPR005339-retry
  - plaque-ipr-IPR007257
  - plaque-ipr-IPR010492
  - plaque-ipr-IPR003874
  - plaque-up-Q08032
  - plaque-up-Q03406
  - plaque-up-Q12488
  - plaque-up-P40359
  - plaque-up-Q12146
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: These are correctly named protein classes with an actionable
    identifier gap; neither whole-complex identity nor the verified GINS examples
    are wrong.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055923Z-dna-replication-preinitiation-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2929
- finding_id: plaque-t5-F3
  issue_key: dna-preinitiation-formation-essentiality-source-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Do not substitute initiation function for formation necessity
  description: MCM and Cdc45 carry ESSENTIAL physical-formation assertions, while
    supplied Takayama evidence demonstrates conditional GINS/recruitment/replication
    effects and the newly added Hopwood-linked Cdc45 example supports identity/localization.
    These do not establish both stated whole-pre-IC formation assertions. Clarify
    the evidence and condition scope or retain uncertainty; this is not a claim of
    biological dispensability, a requirement for universal all-species experiments,
    or a rejection of valid defining constituent status.
  target_ids:
  - GO:0031261
  field_paths:
  - components[0].essentiality
  - components[1].essentiality
  evidence_ids:
  - plaque-current-5
  - plaque-schema
  - plaque-policy
  - plaque-takayama2003-pmc
  - plaque-pmid-8901577
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: The correct constituent identities and broad initiation biology
    remain intact; the unsupported categorical formation labels are a localized model/evidence
    precision defect.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055923Z-dna-replication-preinitiation-complex-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2930
- finding_id: plaque-t5-F4
  issue_key: dna-preinitiation-descriptive-graph-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Calibrate the descriptive graph and final process citation
  description: The eight edges represent six part-membership relations, nucleoplasm
    placement and a generic replication relation. MECHANISTIC and the assembly/function
    title overstate what is encoded. GO0006260 on the final edge identifies DNA replication
    but does not establish the pre-IC-specific causal assertion.
  target_ids:
  - GO:0031261
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].title
  - causal_graphs[0].description
  - causal_graphs[0].edges[7].evidence
  evidence_ids:
  - plaque-current-5
  - plaque-go
  - plaque-graph-policy
  - plaque-takayama2003-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  rule_id: Claim-level evidence, exact class grounding and local formation/graph contracts
  native_severity: minor
  normalization_reason: Supported composition and location remain valid. The correction
    concerns graph scope and narrow edge evidence, separate from the detailed mechanistic
    prose finding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055923Z-dna-replication-preinitiation-complex-audit
    finding_id: F4
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2931
- finding_id: septin-dnaa_diaa_complex-F1
  issue_key: dnaa-diaa-exact-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the two proteins and oriC with exact classes
  description: The existing DiaA/DnaA/oriC rows remain REVIEWED_LABEL_ONLY solely
    because exact terms were not curated. Native IPR023070, IPR001957 and SO0000953
    respectively match these declared classes, with the protein-family membership
    independently corroborated by the correct reviewed examples. Independently reconfirmed
    against the current unchanged record and fresh scoped source evidence. Preserve
    dated discussion rationale; current notes/status may be corrected or a dated clarification
    appended.
  target_ids:
  - GO:1990102
  field_paths:
  - components#diaa_regulator.grounding_status
  - components#dnaa_initiator.grounding_status
  - components#oric_origin_dna.grounding_status
  - discussions#resolve_dnaa_diaa_component_groundings
  evidence_ids:
  - septin-record-dnaa_diaa_complex
  - septin-original-dnaa_diaa_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-retry-IPR023070
  - septin-ipr-IPR001957
  - septin-so
  - septin-up-P66817
  - septin-up-P03004
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_diaa_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055925Z-dnaa-diaa-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2932
- finding_id: septin-dnaa_dnab_dnac_complex-F1
  issue_key: dnaa-dnab-dnac-exact-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground DnaA and chromosomal origin DNA
  description: IPR001957 and SO0000953 exactly match the two label-only DnaA and chromosomal-origin
    rows, whose current notes defer curation rather than identify a genuine unmatched
    class. Independently reconfirmed against the current unchanged record and fresh
    scoped source evidence. Preserve dated discussion rationale; current notes/status
    may be corrected or a dated clarification appended.
  target_ids:
  - GO:1990157
  field_paths:
  - components#dnaa_initiator.grounding_status
  - components#chromosomal_origin_dna.grounding_status
  - discussions#resolve_dnaa_origin_component_groundings
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-original-dnaa_dnab_dnac_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR001957
  - septin-so
  - septin-up-P03004
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dnab_dnac_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055925Z-dnaa-dnab-dnac-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2933
- finding_id: septin-dnaa_dnab_dnac_complex-F2
  issue_key: dnaa-dnab-dnac-origin-formation
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record the tested origin-DNA formation requirement
  description: 'The origin-DNA component remains blanket UNKNOWN even though the cited
    primary S8 directly tests the assembly endpoint: replacing oriC plasmid with empty
    vector prevents retained DnaB in the isolated prepriming-complex preparation.
    This is measured origin-dependent formation, not merely a replication-function
    defect. Independently reconfirmed against the current unchanged record and fresh
    scoped source evidence. Preserve dated discussion rationale; current notes/status
    may be corrected or a dated clarification appended.'
  target_ids:
  - GO:1990157
  field_paths:
  - components#chromosomal_origin_dna.essentiality
  - components#chromosomal_origin_dna.evidence
  evidence_ids:
  - septin-record-dnaa_dnab_dnac_complex
  - septin-original-dnaa_dnab_dnac_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-makowska-s3
  - septin-pmid-20129058
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dnab_dnac_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055925Z-dnaa-dnab-dnac-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2934
- finding_id: septin-dnaa_dps_complex-F1
  issue_key: dnaa-dps-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground DnaA and Dps with their exact families
  description: The existing DnaA/Dps components remain REVIEWED_LABEL_ONLY despite
    exact full-protein IPR001957 and IPR002177 family identities and independent reviewed-example
    membership. Independently reconfirmed against the current unchanged record and
    fresh scoped source evidence. Preserve dated discussion rationale; current notes/status
    may be corrected or a dated clarification appended.
  target_ids:
  - GO:1990084
  field_paths:
  - components#dnaa_initiator.grounding_status
  - components#dps_protein.grounding_status
  - discussions#resolve_dnaa_dps_component_groundings
  evidence_ids:
  - septin-record-dnaa_dps_complex
  - septin-original-dnaa_dps_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR001957
  - septin-ipr-IPR002177
  - septin-up-P03004
  - septin-up-P0ABT2
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dps_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific identity, scope and exact component grounding
  native_severity: minor
  normalization_reason: The maintained complex identity, correct protein examples
    and supported coarse function remain intact; the defect is localized source precision
    or exact family grounding.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T055926Z-dnaa-dps-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2935
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0043846
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, qualify the E.coli heptamer
    model as three DnaX products, tau and/or gamma, plus delta, delta-prime, chi and
    psi. Keep additional tau-dependent fork organization separate from minimum clamp
    loading.
  acceptance_checks:
  - Do not universalize one tau:gamma ratio or require both products in every assembly.
  - Do not replace the full heptamer identity with the crystallized pentamer.
  - Preserve source scope and correct current protein examples; pass applicable native
    validators.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR; retain primary-body/abstract/secondary/authority
    distinctions and do not force universal formation necessity.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0043846
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_clamp_loader_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, map the three verified exact
    families and narrow the current unresolved TODO to genuinely unresolved classes.
    Preserve the five correct protein examples.
  acceptance_checks:
  - Keep IPR004622/IPR012763 domain matches separate from whole-protein identity.
  - Do not import a family description claiming delta proofreading activity.
  - Preserve source scope and correct current protein examples; pass applicable native
    validators.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR; retain primary-body/abstract/secondary/authority
    distinctions and do not force universal formation necessity.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0044776
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_polymerase_iii_core_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, use IPR009052 for the theta
    class and narrow the current TODO. Preserve correct DnaE/DnaQ examples and unresolved
    exact taxon-neutral class boundaries.
  acceptance_checks:
  - Verify family type/name/PF06440 and separate example membership.
  - Do not substitute the DnaQ domain or broad DnaE2/DnaE/PolC family.
  - Preserve source scope and correct current protein examples; pass applicable native
    validators.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR; retain primary-body/abstract/secondary/authority
    distinctions and do not force universal formation necessity.
- action_id: plaque-t3-A1
  finding_ids:
  - plaque-t3-F1
  target_ids:
  - GO:0005662
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_a_complex.yaml
    role: maintained scientific record
  description: Ground the verified classes to IPR004591/014646/013970 with source-backed
    family evidence and update the corresponding open task/status. Preserve unresolved
    classes and historical provenance; keep organism accessions as examples.
  acceptance_checks:
  - Each added family denotes the existing whole-protein class rather than a domain,
    broader homolog group or species accession.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history; any record curation uses guarded writer and
    appended history in a separately authorized change, not this review-only PR.
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0005663
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_factor_c_complex.yaml
    role: maintained scientific record
  description: Ground the verified class RFC1 to IPR012178 with source-backed family
    evidence and update the corresponding open task/status. Preserve unresolved classes
    and historical provenance; keep organism accessions as examples.
  acceptance_checks:
  - Each added family denotes the existing whole-protein class rather than a domain,
    broader homolog group or species accession.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history; any record curation uses guarded writer and
    appended history in a separately authorized change, not this review-only PR.
- action_id: plaque-t5-A1
  finding_ids:
  - plaque-t5-F1
  target_ids:
  - GO:0031261
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  description: Separate the native GO definition and directly demonstrated2003 observations
    from later mechanistic claims. Either inspect and attach appropriate modern primary
    sources at each claim or qualify/remove the unsupported detail; preserve conditional
    recruitment and strain context.
  acceptance_checks:
  - Every double-hexamer, kinase-target, CMG and bridge assertion has a directly inspected
    source at the actual field.
  - Takayama2003 is not presented as demonstrating mechanisms beyond its experiments.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history; any record curation uses guarded writer and
    appended history in a separately authorized change, not this review-only PR.
- action_id: plaque-t5-A2
  finding_ids:
  - plaque-t5-F2
  target_ids:
  - GO:0031261
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  description: Add the exact five class groundings with source-specific evidence and
    appropriate grounding states. Keep the MCM GO complex separate and retain existing
    correctly taxon-paired examples.
  acceptance_checks:
  - Each family is checked against the same named whole-protein class and the native
    reviewed-protein cross-reference.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history; any record curation uses guarded writer and
    appended history in a separately authorized change, not this review-only PR.
- action_id: plaque-t5-A3
  finding_ids:
  - plaque-t5-F3
  target_ids:
  - GO:0031261
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  description: Clarify the physical-formation basis and experimental scope for current
    MCM/Cdc45 ESSENTIAL assertions, using source-backed defining assembly or condition-specific
    evidence where justified; otherwise retain UNKNOWN. Preserve established functional/recruitment
    roles and do not infer dispensability or mandate new universal assays.
  acceptance_checks:
  - Formation necessity is assessed separately from viability, replication activity,
    protein abundance and conditional recruitment.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history; any record curation uses guarded writer and
    appended history in a separately authorized change, not this review-only PR.
- action_id: plaque-t5-A4
  finding_ids:
  - plaque-t5-F4
  target_ids:
  - GO:0031261
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dna_replication_preinitiation_complex.yaml
    role: maintained scientific record
  description: Mark the present topology/function graph NONMECHANISTIC with an honest
    scope note and claim-appropriate final-edge evidence, or build separately sourced
    causal recruitment edges preserving experimental conditions.
  acceptance_checks:
  - The graph label matches the relations actually encoded.
  - The final biological edge cites a source supporting the structure-specific assertion,
    not only a process identifier.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history; any record curation uses guarded writer and
    appended history in a separately authorized change, not this review-only PR.
- action_id: septin-dnaa_diaa_complex-A1
  finding_ids:
  - septin-dnaa_diaa_complex-F1
  target_ids:
  - GO:1990102
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_diaa_complex.yaml
    role: maintained scientific record
  description: Use these verified exact class groundings and align current status/notes/TODO;
    retain correct proteins and per-DiaA-tetramer stoichiometry. In separately authorized
    record curation, preserve dated rationale/history and add a dated clarification
    where needed; this review PR edits no scientific record.
  acceptance_checks:
  - Do not substitute the broader GmhA/SIS classes or a generic DNA chemical entity.
  - Keep strain accessions separate from family and sequence-feature groundings.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Keep exact original finding lineage and experimental limits; do not rewrite historical
    rationale.
- action_id: septin-dnaa_dnab_dnac_complex-A1
  finding_ids:
  - septin-dnaa_dnab_dnac_complex-F1
  target_ids:
  - GO:1990157
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dnab_dnac_complex.yaml
    role: maintained scientific record
  description: Apply the exact DnaA family and oriC sequence-feature class and update
    current grounding notes/TODO. In separately authorized record curation, preserve
    dated rationale/history and add a dated clarification where needed; this review
    PR edits no scientific record.
  acceptance_checks:
  - Keep the existing GO1990100 whole-subcomplex grounding.
  - Preserve P03004 and the primase-free intermediate boundary.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Keep exact original finding lineage and experimental limits; do not rewrite historical
    rationale.
- action_id: septin-dnaa_dnab_dnac_complex-A2
  finding_ids:
  - septin-dnaa_dnab_dnac_complex-F2
  target_ids:
  - GO:1990157
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dnab_dnac_complex.yaml
    role: maintained scientific record
  description: Replace blanket UNKNOWN with a source-backed, explicitly condition-scoped
    formation requirement for oriC DNA in this E.coli reconstitution; choose the appropriate
    enum with the assay qualification in evidence/notes. In separately authorized
    record curation, preserve dated rationale/history and add a dated clarification
    where needed; this review PR edits no scientific record.
  acceptance_checks:
  - Cite S8 empty-vector control and the S20 preparation.
  - Do not infer organism viability, universal in-vivo necessity or all-subunit requirements.
  - Retain the distinction between DnaC mutants that assemble and their defective
    later function.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Keep exact original finding lineage and experimental limits; do not rewrite historical
    rationale.
- action_id: septin-dnaa_dps_complex-A1
  finding_ids:
  - septin-dnaa_dps_complex-F1
  target_ids:
  - GO:1990084
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_dps_complex.yaml
    role: maintained scientific record
  description: Use the exact DnaA and Dps families and align current grounding notes/TODO
    while preserving correct examples and the qualified oxidative-stress model. In
    separately authorized record curation, preserve dated rationale/history and add
    a dated clarification where needed; this review PR edits no scientific record.
  acceptance_checks:
  - Do not substitute broad AAAATPase/ferritin folds or force a narrower gammaproteobacterial
    subgroup.
  - Do not infer direct DnaA binding for every Dps-family member.
  - Preserve supported identifiers, examples and biological scope; pass applicable
    native validation.
  - Keep exact original finding lineage and experimental limits; do not rewrite historical
    rationale.
limitations:
- 'Pol III clamp loader, holoenzyme and core independent review: This slice judges
  only PolIII clamp loader, whole complex and core. All three frozen target hashes
  are unchanged; other seven targets and neighboring/group/category issues are not
  disposed. No repository/Git/GitHub mutation.'
- 'Pol III clamp loader, holoenzyme and core independent review: Jeruzalmi2001 genuine
  primary PDF read at pp429–431 and439–440 Summary/Introduction/structural Results/Conclusion/Methods
  plus Fig1 text caption only. No figure pixels, coordinates, supplements, raw kinetics
  or full-paper certification. Truncated gamma1–373 pentamer/reconstitution is distinct
  from full heptamer/native cell and speculative transitions.'
- 'Pol III clamp loader, holoenzyme and core independent review: McHenry2003 is a
  secondary-review PDF read pp1157–1159, opening p1160 and Fig1 text caption, not
  the complete review. Its mixed in-vivo model and additional tau coupling are distinct
  from any-mixture isolated loading; no invariant in-vivo ratio or complete body read
  is claimed.'
- 'Pol III clamp loader, holoenzyme and core independent review: Maki/Kornberg1988
  is complete primary-abstract and publisher-metadata only. Fresh HTML/PDF403 and
  metadata-only API leave exact experimental strains, methods, figures and physical-formation
  assays unverified, not disproved.'
- 'Pol III clamp loader, holoenzyme and core independent review: GO0043846 andGO0044776
  current nuclear ancestry/Eukaryota-only constraints conflict with their bacterial
  source evidence; neither is a maintained target assertion. The core DNA-polymerase
  parent is activity-supported, not claimed as a direct native GO is-a edge.'
- 'Pol III clamp loader, holoenzyme and core independent review: Native reviewed UniProt
  identities, current singleton queries and InterPro metadata do not certify every
  annotation-linked experiment. HolA generated proofreading prose and broad generated
  IPR050238 text are excluded from biological support; exact families are distinguished
  from domains/broad or taxon-limited classes.'
- 'Pol III clamp loader, holoenzyme and core independent review: Current precise1k
  comprises five K12-related strains, not an identified exact Jeruzalmi/Maki assay
  strain. Nine exact loci each have201 checked module rows; only holD145 andholE147
  cross thresholds, corroborated by70- and43-gene module lists. Nonhits are not absence;
  hits/names are not assembly, localization, direct regulation or formation. Generated
  AI summaries and activity contrasts not used.'
- 'Pol III clamp loader, holoenzyme and core independent review: Historical adapter
  runner unavailability is the actual2026-11-03T00:49Z failure, not a fresh invocation.
  Current manual official API fallback is separate. Six source-head native protein
  commands pass with8examples/8COVERED typednodes; the whole-complex0/0 outcome does
  not assess STRUCTURE nodes, checked separately.'
- 'Pol III clamp loader, holoenzyme and core independent review: Three inherited minor
  findings remain open with exact predecessor identities and bounded future curation
  actions. Historical rationale/history remain append-only. No optional examples,
  new experiments, forced domain-to-family mapping or universal essentiality classification
  are required.'
- 'Pol III clamp loader, holoenzyme and core independent review: Root owns global
  QC and later saved-head/CI/queue gates. These future stages are not certified by
  this source report. Original failure-kind corrections retain exact historical timestamps/hashes
  and never invent body access.'
- 'RPA, RFC and replication preinitiation independent review: Wold1997 and Kim2003
  are secondary complete abstract/metadata tiers, not newly inspected review bodies.
  Wold publisher403 and Brill primary PDF403 are retained access limitations; Brill
  complete primary abstract independently supports yeast three-gene composition, not
  exact S288C experimental strain.'
- 'RPA, RFC and replication preinitiation independent review: Takayama genuine fresh
  primary HTML Results sec2–9/Discussion11–13/Methods15–22 and text captions were
  read; no figure pixels, raw data or Supplementary Table1. No W303/S288C strain equivalence
  is invented. Modern mechanistic details require their own appropriate source; ontology/family
  prose does not substitute.'
- 'RPA, RFC and replication preinitiation independent review: Cullmann genuine author-repository
  PDF text pp4661–4663/4665/4668–4669 and selected text captions were read. No alignment
  image or figure-pixel analysis. Gary/Hopwood remain complete primary abstracts on
  correct legacy PMC surfaces; scan links are not body review. Kitabayashi/Nishida
  are full primary abstracts only, with their exact archaeal hosts preserved.'
- 'RPA, RFC and replication preinitiation independent review: Initial mistaken PMC26461
  Hopwood lead was rejected after title inspection; unrelated GPCR content is excluded.
  Correct PMC37987 identity/abstract subsequently verified. Two initial InterPro429
  responses are retained separately from successful retries; no negative-family inference.'
- 'RPA, RFC and replication preinitiation independent review: Current13 reviewed S288C
  examples/13 typed nodes allCOVERED independently checked; reference identities/localization
  do not prove every claimed mechanism/formation requirement. No optional example
  inventory, forced RFC2–5 exact families or protein-complex enum finding.'
- 'RPA, RFC and replication preinitiation independent review: Fresh complete official
  catalogue lacks matched natural yeast/eukaryotic hosts. No unrelated E.coli or archaeal
  dataset proxy, no module-query run or biological absence inferred. Historical Nov3
  00:49Z runner failure is not a fresh invocation; current source fallback is separately
  evidenced.'
- 'RPA, RFC and replication preinitiation independent review: Three original pairs/42
  historical input occurrences and47 current inputs verified. RFA/pre-IC stale deltas
  substantively refreshed and RFC unchanged; original files immutable. Root owns corpus
  QC/final saved-head/CI/queue/merge gates, none precertified by source review.'
- 'RPA, RFC and replication preinitiation independent review: Six inherited scientific
  findings remain open: one major/five minor. Added examples and prior2470 RFA evidence
  repair do not resolve exact-family F1; no terminal grouped/category issue resolution
  inferred. Five access-kind occurrences and three prose applicability exclusions
  are bundle-only corrections.'
- 'Topoisomerase IV and DnaA complexes independent review: Four nonstale targets;
  four inherited minor scientific findings remain (three exact-grounding findings
  plus one condition-scoped origin-formation finding). TopoIV retains a qualified
  positive pass; no new scientific finding.'
- 'Topoisomerase IV and DnaA complexes independent review: Makowska2010 genuine fresh
  JATS was read only at named Results/Discussion/Methods sections. The empty-vector
  result is reported text, not independently reanalyzed pixels or raw data. Exact
  plasmid/strain details delegated to unread TableS1 are not certified. Keyamura2007,Chodavarapu2008
  and Peng1993 are current indexed primary excerpts with exact displayed extents;
  terminal failures remain separate. No complete downloaded bodies for those three,
  no figure pixels,supplements or deposited-coordinate analysis.'
- 'Topoisomerase IV and DnaA complexes independent review: Ishida2004 and DnaA localization
  papers were read at complete native abstract/metadata plus relevant UniProt annotation
  tier. Luttinger1995 is a secondary-review abstract. Schenk includes both B.subtilis
  and E.coli; native reference strain is not synonymous with every experimental preparation.
  Earlier DiaA dimer and later tetramer/equilibrium evidence are preserved.'
- 'Topoisomerase IV and DnaA complexes independent review: GO0009340 heterodimer language
  conflicts with inspected 2:2 evidence; current maintained definition avoids it.
  IPR050220 LLM-generated unchecked prose and iModulon ai_summary prose are excluded
  from biological evidence. Family/type/hierarchy metadata remain distinct from primary
  experiments.'
- 'Topoisomerase IV and DnaA complexes independent review: All four original formal
  expression-only exclusions require correction. Fresh complete official catalogue
  and precise1k metadata support E.coli context; seven exact loci were checked across201
  module memberships. dps has OxyR3/RpoS51 hits; six others below threshold do not
  establish absent expression/regulation/structure. Generated module prose,uninspected
  activities and nonmatching experimental strains are not promoted to direct mechanistic
  evidence. Historical runner failure remains Nov3 00:49Z, with no fresh invocation.'
- 'Topoisomerase IV and DnaA complexes independent review: Own native inventory has7
  reviewed example occurrences (5 distinct accessions) and7 typed nodes, all COVERED;
  eight actual native command successes do not establish direct membership,necessity
  or localization. Four original pairs validate/render exactly with52 historical input
  occurrences verified. Historical batch26 execution provenance is retained accurately.'
- 'Topoisomerase IV and DnaA complexes independent review: Three original HTTP403
  context_only evidence rows need only database→validation reclassification; their
  historical timestamps,explicit no-body statements and original bytes are preserved.
  Current500/404/429/challenge responses are truthful access context; alternate successes
  are separately scoped.'
- 'Topoisomerase IV and DnaA complexes independent review: Only29 listed frozen maintained
  inputs used; no additional local record or prior-review context. Bounded ignored-inclusive
  scratch filename search located a prior Keyamura reader but no prior scientific
  bundle was used as biological authority; fresh current sources suffice. Search failures/unrelated
  hits are not negative biological evidence. Root global gates,successor validation,final
  CI,queue and merge remain separate attestations.'
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
- 'This ten-record successor preserves all 20 original artifacts and exact predecessor
  finding lineage. Bundle issues #2920, #2921 and #2922 cover two stale targets, seven
  formal plus three prose applicability assessments, and twelve access-only evidence-kind
  occurrences.'
- RPA adds three budding-yeast examples and source-specific component/graph citations.
  Preinitiation adds the CDC45 Q08032 example. These changes require substantive source
  reassessment separately from the inherited findings.
- The current native inventory has 28 component protein examples and 28 typed GENE_OR_PROTEIN
  nodes, all classified COVERED in the actual native logs. The Pol III holoenzyme
  remains a deliberately grounded subcomplex-level record with zero protein examples
  and zero typed protein nodes; this is not a required-inventory defect.
- Historical failed publisher responses already disclose failed access and context_only
  support. The successor uses validation for those access observations and preserves
  actual timestamps and hashes; successful current source scopes remain distinct.
- Record curation stays in separate issues. Preserve dated rationale/history and append
  supported clarification; no scientific record is edited. Final post-save validation,
  saved-head independent acceptance, final-head CI and merge-group CI are later gates.
- The RPA refresh supports current RFA1/2/3 reference identities and three-gene composition
  at native-entry and primary-abstract scope, while Wold full-body and exact experimental-strain
  limits remain explicit. The preinitiation refresh supports the new CDC45 Q08032
  identity and nucleus annotation via the current native reference and Hopwood abstract;
  the four pre-existing source, grounding, formation and graph findings remain open.
- DnaX composition is a bounded generic-heptamer versus tau-dependent holoenzyme distinction;
  it does not replace the full heptamer with the truncated crystal pentamer or mandate
  a tau:gamma ratio. The DnaA-DnaB-DnaC origin-DNA finding is explicitly limited to
  the isolated-complex assay, not universal viability or in-vivo essentiality.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055920Z-dna-polymerase-iii-clamp-loader-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055920Z-dna-polymerase-iii-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055921Z-dna-polymerase-iii-core-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055922Z-dna-replication-factor-a-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055923Z-dna-replication-factor-c-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055923Z-dna-replication-preinitiation-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055924Z-dna-topoisomerase-iv-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055925Z-dnaa-diaa-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055925Z-dnaa-dnab-dnac-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T055926Z-dnaa-dps-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2388
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2920
- https://github.com/CultureBotAI/CellStructureMech/issues/2921
- https://github.com/CultureBotAI/CellStructureMech/issues/2922
- https://github.com/CultureBotAI/CellStructureMech/issues/2923
- https://github.com/CultureBotAI/CellStructureMech/issues/2924
- https://github.com/CultureBotAI/CellStructureMech/issues/2925
- https://github.com/CultureBotAI/CellStructureMech/issues/2926
- https://github.com/CultureBotAI/CellStructureMech/issues/2927
- https://github.com/CultureBotAI/CellStructureMech/issues/2928
- https://github.com/CultureBotAI/CellStructureMech/issues/2929
- https://github.com/CultureBotAI/CellStructureMech/issues/2930
- https://github.com/CultureBotAI/CellStructureMech/issues/2931
- https://github.com/CultureBotAI/CellStructureMech/issues/2932
- https://github.com/CultureBotAI/CellStructureMech/issues/2933
- https://github.com/CultureBotAI/CellStructureMech/issues/2934
- https://github.com/CultureBotAI/CellStructureMech/issues/2935
```
