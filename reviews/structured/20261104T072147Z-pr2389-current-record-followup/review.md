# PR 2389: current-input review of ten records and adversarial follow-up

- Review: 20261104T072147Z-pr2389-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T07:05:06.244734Z
- Finished UTC: 2026-11-04T07:21:47Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input independent reassessment of all ten records: all original target hashes match current main, so no stale record requires refresh. Fifteen inherited scientific findings remain open (four major, eleven minor), with fifteen bounded record-curation actions and all ten targets needing curation. The original Rep query-uniqueness finding is rejected with exact predecessor lineage, an explicit disposition reason and no record-curation action: a present alias-inclusive query cannot establish the historical unstated search or invalidate the correct primary Rep accession. The successor corrects seven formal and three prose structured-source applicability exclusions and four historical failed-access evidence classifications, preserving all twenty original artifacts and all scientific records. Independent source scopes distinguish primary bodies, complete abstracts, authority metadata, experimental stages, biological strains and expression hosts. Every open scientific finding is linked to a deduplicated issue; bundle corrections and existing resolver tooling are tracked separately.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main dbad8ee30de8ed1a1a2b2d828b471248232119ed. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 5232267fcf66b8911d0c40e386913bd3a3a0f06d.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 14475ecacc26d4832351bb4974cfa23bd4ec7b02.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990083 | data/structures/other/dnaa_hda_complex.yaml | maintained | DnaA-Hda complex |
| GO:1990103 | data/structures/other/dnaa_hu_complex.yaml | maintained | DnaA-HU complex |
| GO:1990082 | data/structures/other/dnaa_l2_complex.yaml | maintained | DnaA-L2 complex |
| GO:1990101 | data/structures/other/dnaa_oric_complex.yaml | maintained | DnaA-oriC complex |
| GO:1990100 | data/structures/other/dnab_dnac_complex.yaml | maintained | DnaB-DnaC complex |
| GO:1990158 | data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml | maintained | DnaB-DnaC-DnaT-PriA-PriB complex |
| GO:1990159 | data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml | maintained | DnaB-DnaC-DnaT-PriA-PriC complex |
| GO:1990160 | data/structures/other/dnab_dnac_rep_pric_complex.yaml | maintained | DnaB-DnaC-Rep-PriC complex |
| GO:1990156 | data/structures/other/dnab_dnag_complex.yaml | maintained | DnaB-DnaG complex |
| GO:1990161 | data/structures/other/dnab_helicase_complex.yaml | maintained | DnaB helicase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:1990083 | passed | True | GO:1990083 | Documented focused command passed. |
| validate-strict GO:1990083 | passed | True | GO:1990083 | Documented focused command passed. |
| validate GO:1990103 | passed | True | GO:1990103 | Documented focused command passed. |
| validate-strict GO:1990103 | passed | True | GO:1990103 | Documented focused command passed. |
| validate GO:1990082 | passed | True | GO:1990082 | Documented focused command passed. |
| validate-strict GO:1990082 | passed | True | GO:1990082 | Documented focused command passed. |
| validate GO:1990101 | passed | True | GO:1990101 | Documented focused command passed. |
| validate-strict GO:1990101 | passed | True | GO:1990101 | Documented focused command passed. |
| validate GO:1990100 | passed | True | GO:1990100 | Documented focused command passed. |
| validate-strict GO:1990100 | passed | True | GO:1990100 | Documented focused command passed. |
| validate GO:1990158 | passed | True | GO:1990158 | Documented focused command passed. |
| validate-strict GO:1990158 | passed | True | GO:1990158 | Documented focused command passed. |
| validate GO:1990159 | passed | True | GO:1990159 | Documented focused command passed. |
| validate-strict GO:1990159 | passed | True | GO:1990159 | Documented focused command passed. |
| validate GO:1990160 | passed | True | GO:1990160 | Documented focused command passed. |
| validate-strict GO:1990160 | passed | True | GO:1990160 | Documented focused command passed. |
| validate GO:1990156 | passed | True | GO:1990156 | Documented focused command passed. |
| validate-strict GO:1990156 | passed | True | GO:1990156 | Documented focused command passed. |
| validate GO:1990161 | passed | True | GO:1990161 | Documented focused command passed. |
| validate-strict GO:1990161 | passed | True | GO:1990161 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Whole-record molecular and pathway assertions trigger applicability for all ten targets. Fresh official iModulonDB catalogue coverage identifies E. coli precise1k for nine records and no biological-source Geobacillus stearothermophilus dataset for the DnaB homohexamer; Bacillus subtilis and E. coli expression-host data are not proxies. Exact native loci were checked against all 201 module membership rows in the selected five-strain precise1k dataset. Positive rplB and priB Translation module 1 memberships and dnaG Nucleotide Stress module 10 membership were corroborated in complete member lists; remaining threshold nonhits do not imply absence. These are bounded expression contexts, not physical complex formation, direct regulation, necessity or current experimental-strain matches. No generated summaries or activity contrasts are used. The historical unavailable structured runner receipt is retained separately; direct official API access is not a fresh runner invocation. |
| Independent claim-level source review | passed | True | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native DnaA-Hda complex UniProt verify check | passed | True | GO:1990083 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-Hda complex UniProt causal check | passed | True | GO:1990083 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-HU complex UniProt verify check | passed | True | GO:1990103 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-HU complex UniProt causal check | passed | True | GO:1990103 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-L2 complex UniProt verify check | passed | True | GO:1990082 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-L2 complex UniProt causal check | passed | True | GO:1990082 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-oriC complex UniProt verify check | passed | True | GO:1990101 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaA-oriC complex UniProt causal check | passed | True | GO:1990101 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC complex UniProt verify check | passed | True | GO:1990100 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC complex UniProt causal check | passed | True | GO:1990100 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC-DnaT-PriA-PriB complex UniProt verify check | passed | True | GO:1990158 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC-DnaT-PriA-PriB complex UniProt causal check | passed | True | GO:1990158 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC-DnaT-PriA-PriC complex UniProt verify check | passed | True | GO:1990159 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC-DnaT-PriA-PriC complex UniProt causal check | passed | True | GO:1990159 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC-Rep-PriC complex UniProt verify check | passed | True | GO:1990160 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaC-Rep-PriC complex UniProt causal check | passed | True | GO:1990160 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaG complex UniProt verify check | passed | True | GO:1990156 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB-DnaG complex UniProt causal check | passed | True | GO:1990156 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB helicase complex UniProt verify check | passed | True | GO:1990161 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native DnaB helicase complex UniProt causal check | passed | True | GO:1990161 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Binary DnaA-Hda versus full RIDA system

identity: supported. Targets: GO:1990083.

GO1990083 and replication-inhibiting protein-complex parent are exact. Keyamura direct contacts and staged assay support DnaA-Hda participation; DNA-loaded beta clamp and ADP-Hda context do not force a clamp constituent into the separately scoped binary record. Hda-beta-clamp GO1990085 remains distinct.

### ATP hydrolysis versus inherited phosphorylation wording

evidence: concern. Targets: GO:1990083.

Current definition faithfully copies current GO but contradicts the staged primary assay and its own graph/canonical hydrolysis text: RIDA promotes hydrolysis of DnaA-bound ATP to ADP, not inhibition of ADP-to-ATP phosphorylation. DARS exchange is a separate reactivation pathway. Correct chemistry while explicitly retaining upstream attribution and exact complex identity.

### Exact DnaA/Hda classes

grounding: concern. Targets: GO:1990083.

IPR001957 DnaA and IPR017788 Hda are verified whole-protein families with matching P03004/P69931 xrefs. They can resolve existing label-only mapping tasks. IPR022864 is Enterobacteriaceae-specific and not the generic Hda class. No optional protein inventory is demanded.

### Three descriptive membership/function edges

graph: supported. Targets: GO:1990083.

Two constituent edges and RIDA-support relation agree with authority and primary contact/hydrolysis assays. NONMECHANISTIC scope openly excludes clamp loading and detailed hydrolysis chemistry. Mutation-dependent reduced binding/activity is not proof that every missing partner prevents all binary complex formation.

### K12-derived assays versus reference protein/localization contexts

scope: supported. Targets: GO:1990083.

Primary Methods enumerate KH5402-1/WM433/YT411/KA451/KA429/KA450 contexts and defined purified reactions; reviewed K12 examples are valid annotations, not an assertion that all assays use an unmodified reference strain. Native DnaA/Hda localization references have separate abstract/annotation tiers. Proposed contact model is not a solved structure.

### HU-bound DnaA-origin complex and alternatives

identity: supported. Targets: GO:1990103.

Exact GO1990103 nucleoprotein identity is distinct from plain DnaA-oriC, DiaA stimulation and helicase loading. Complete Chodavarapu2008 primary abstract supports DnaA-HU interaction, oriC oligomer stabilization and relative alpha-dimer activity. Do not impose an invariant alpha-beta heterodimer.

### DnaA and oriC exact classes; HU complex boundary

grounding: concern. Targets: GO:1990103.

DnaA IPR001957 and oriC SO0000953 are exact source-neutral mappings for existing constituents. HU dimer is a PROTEIN_COMPLEX, so neither individual HU family nor one compulsory subunit combination replaces its unresolved whole-complex identity. hupa/hupb queries used only as contextual native loci.

### Four coarse initiation edges

graph: supported. Targets: GO:1990103.

DnaA/HU membership, oriC scaffold and initiation support agree with exact GO and complete primary abstract. Scope explicitly withholds subunit choice, oligomerization and later loading mechanics, and does not restore an unverified bending mechanism.

### Abstract-supported E.coli assays and unverified broad necessity

scope: unknown. Targets: GO:1990103.

Species-level E.coli context and HU alternatives/stimulation are supported. Fresh publisher and PDF403 leave full methods, experimental strain and universal bacterial-necessity wording unverified, not disproved. The essential-in-bacteria sentence is accurately GO-attributed but is not independently certified as a taxon-wide formation or viability conclusion.

### Binary inhibitory contact rather than whole ribosome

identity: supported. Targets: GO:1990082.

GO1990082 and inhibitory protein-complex parent agree with measured mature/truncated L2 contact with DnaA. Generic ribosomal membership/functions do not imply a ribosome constituent or prove DnaA interaction without the primary contact study.

### DnaA and bacterial/organellar uL2 exact families

grounding: concern. Targets: GO:1990082.

Existing label-only classes have exact whole-protein IPR001957 and IPR005880, independently corroborated by P03004/P60422. Universal uL2 IPR002171 is a broader parent with separate archaeal/eukaryotic branch. Keep native gene rplB, reviewed K12 identity and historical 50S-L2 label correspondence.

### Direct contact and inhibited in-vitro initiation

graph: supported. Targets: GO:1990082.

Three edges accurately describe constituent contact and inhibitory function. Primary ELISA, oriC-unwinding and prepriming assays support these statements; reduced recovered DnaA/DnaB supports proposed oligomer destabilization, not a solved interface, fixed stoichiometry or detailed cleavage mechanism. NONMECHANISTIC scope keeps these distinctions.

### Mature/truncated preparations and physiological uncertainty

scope: supported. Targets: GO:1990082.

The tL2 purification is from DM700, with separate MG1655/W3110 observations and defined reactions; reference K12 accession does not identify every preparation. Discussion leaves physiological regulation proposed and reports a negative tested tL2 in-vivo initiation assay. Current graph explicitly excludes in-vivo stringent-response context; no broader in-vivo checkpoint is certified.

### Initial DnaA-origin assembly boundary

identity: supported. Targets: GO:1990101.

Exact GO1990101 nucleoprotein identity and initiation-complex parent are appropriate; plain DnaA/oriC scope does not require DiaA, DnaB-DnaC, HU or later primosome components. Current GO definitions and Miller primary binding/assembly assays support the named early complex.

### Existing protein family and origin feature classes

grounding: concern. Targets: GO:1990101.

DnaA IPR001957 and oriC SO0000953 exactly ground the maintained classes and can resolve/narrow the existing mapping task. Correct P03004 taxon example is separate from family identity; no single origin-sequence accession or broad homolog/domain substitute is required.

### Three bounded origin-seeding edges

graph: supported. Targets: GO:1990101.

DnaA membership, oriC scaffold and initiation support match the current source. Miller high-affinity-site mutants affect normal-concentration assembly but elevated DnaA can restore weak-site filling; the record does not claim universal loss of formation. Coarse NONMECHANISTIC scope does not overstate exact oligomer geometry or later loading.

### Actual strain/protein/mutant contexts

scope: supported. Targets: GO:1990101.

Miller Methods distinguish P3478/isogenic W3110, PC2 dnaCts and purified tagged DnaA. DMS footprints, crosslinks and EMSA support bounded site-assisted assembly; no raw footprint reanalysis or pixel interpretation was performed. Reference K12 annotation and localization abstracts do not substitute for these experiment contexts.

### Current reviewed example identities and query bounds

grounding: supported. Targets: GO:1990083.

Maintained P03004 DnaA, P69931 Hda identities agree with native reviewed status, primary genes/ordered loci and taxon83333. Current exact reviewed queries are singleton; no historical query reconstruction. Localization papers are abstract/native-annotation tier and do not prove physical membership by themselves.

### Physical formation distinct from activity and viability

grounding: unknown. Targets: GO:1990083.

Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition, origin function and organism viability are not universal constituent-absence formation assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL classification is requested.

### Original frozen inputs versus current target

provenance: supported. Targets: GO:1990083.

Record is unchanged on current main. Original source revisions/hashes and immutable YAML/Markdown were verified; independent present source reading does not invent a stale refresh or erase historical access limits.

### Positive replication pathways require matched structured-source context

scope: concern. Targets: GO:1990083.

Original formal expression-only exclusion is unsupported for named molecular replication narratives. Fresh catalogue selects actual E.coli precise1k; five exact native loci each checked against201 modules. Only rplB b3317 passes module1 Translation threshold, confirmed in53-member list. Five-strain coverage differs from particular mutant/reconstitution preparations. Hits are not assembly/direct regulation; nonhits are not absence. No generated AI summaries or activities used.

### Actual native validation and protein coverage

schema: supported. Targets: GO:1990083.

2 reviewed examples/2 COVERED typed protein nodes; both current native commands actually exit0. HU complex and origin feature nodes are outside the protein-only inventory and separately assessed. Native success does not settle exact class mapping or full scientific completeness; original validate/render also pass.

### Append-only prior rationale and scope resolutions

provenance: supported. Targets: GO:1990083.

Earlier reference-protein additions and historical deferral statements are preserved as provenance, not treated as false current inventories. Existing interpretation boundaries are supported; exact family/feature actions append evidence and narrow current prompts/notes while preserving rationale/posed_date. No grouped or neighboring issue is terminally resolved.

### Complete maintained record and access bounds

completeness: supported. Targets: GO:1990083.

All current fields/original review examined. No maintained image or physical measurement requires pixel/unit review. Source-body, complete-abstract, native ontology/family/protein and failed-access tiers remain distinct; optional omissions and unknowns alone are not findings.

### Current independent scientific disposition

other: concern. Targets: GO:1990083.

needs_curation: inherited major chemistry and minor exact-family findings retained; supported binary identity and bounded RIDA graph preserved.

### Current reviewed example identities and query bounds

grounding: supported. Targets: GO:1990103.

Maintained P03004 DnaA identities agree with native reviewed status, primary genes/ordered loci and taxon83333. Current exact reviewed queries are singleton; no historical query reconstruction. Localization papers are abstract/native-annotation tier and do not prove physical membership by themselves.

### Physical formation distinct from activity and viability

grounding: unknown. Targets: GO:1990103.

Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition, origin function and organism viability are not universal constituent-absence formation assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL classification is requested.

### Original frozen inputs versus current target

provenance: supported. Targets: GO:1990103.

Record is unchanged on current main. Original source revisions/hashes and immutable YAML/Markdown were verified; independent present source reading does not invent a stale refresh or erase historical access limits.

### Positive replication pathways require matched structured-source context

scope: concern. Targets: GO:1990103.

Original formal expression-only exclusion is unsupported for named molecular replication narratives. Fresh catalogue selects actual E.coli precise1k; five exact native loci each checked against201 modules. Only rplB b3317 passes module1 Translation threshold, confirmed in53-member list. Five-strain coverage differs from particular mutant/reconstitution preparations. Hits are not assembly/direct regulation; nonhits are not absence. No generated AI summaries or activities used.

### Actual native validation and protein coverage

schema: supported. Targets: GO:1990103.

1 reviewed examples/1 COVERED typed protein nodes; both current native commands actually exit0. HU complex and origin feature nodes are outside the protein-only inventory and separately assessed. Native success does not settle exact class mapping or full scientific completeness; original validate/render also pass.

### Append-only prior rationale and scope resolutions

provenance: supported. Targets: GO:1990103.

Earlier reference-protein additions and historical deferral statements are preserved as provenance, not treated as false current inventories. Existing interpretation boundaries are supported; exact family/feature actions append evidence and narrow current prompts/notes while preserving rationale/posed_date. No grouped or neighboring issue is terminally resolved.

### Complete maintained record and access bounds

completeness: supported. Targets: GO:1990103.

All current fields/original review examined. No maintained image or physical measurement requires pixel/unit review. Source-body, complete-abstract, native ontology/family/protein and failed-access tiers remain distinct; optional omissions and unknowns alone are not findings.

### Current independent scientific disposition

other: concern. Targets: GO:1990103.

needs_curation: inherited minor DnaA/oriC exact mappings retained; HU alternatives and abstract-only/universal-necessity limitations preserved.

### Current reviewed example identities and query bounds

grounding: supported. Targets: GO:1990082.

Maintained P03004 DnaA, P60422 rplB/uL2 identities agree with native reviewed status, primary genes/ordered loci and taxon83333. Current exact reviewed queries are singleton; no historical query reconstruction. Localization papers are abstract/native-annotation tier and do not prove physical membership by themselves.

### Physical formation distinct from activity and viability

grounding: unknown. Targets: GO:1990082.

Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition, origin function and organism viability are not universal constituent-absence formation assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL classification is requested.

### Original frozen inputs versus current target

provenance: supported. Targets: GO:1990082.

Record is unchanged on current main. Original source revisions/hashes and immutable YAML/Markdown were verified; independent present source reading does not invent a stale refresh or erase historical access limits.

### Positive replication pathways require matched structured-source context

scope: concern. Targets: GO:1990082.

Original formal expression-only exclusion is unsupported for named molecular replication narratives. Fresh catalogue selects actual E.coli precise1k; five exact native loci each checked against201 modules. Only rplB b3317 passes module1 Translation threshold, confirmed in53-member list. Five-strain coverage differs from particular mutant/reconstitution preparations. Hits are not assembly/direct regulation; nonhits are not absence. No generated AI summaries or activities used.

### Actual native validation and protein coverage

schema: supported. Targets: GO:1990082.

2 reviewed examples/2 COVERED typed protein nodes; both current native commands actually exit0. HU complex and origin feature nodes are outside the protein-only inventory and separately assessed. Native success does not settle exact class mapping or full scientific completeness; original validate/render also pass.

### Append-only prior rationale and scope resolutions

provenance: supported. Targets: GO:1990082.

Earlier reference-protein additions and historical deferral statements are preserved as provenance, not treated as false current inventories. Existing interpretation boundaries are supported; exact family/feature actions append evidence and narrow current prompts/notes while preserving rationale/posed_date. No grouped or neighboring issue is terminally resolved.

### Complete maintained record and access bounds

completeness: supported. Targets: GO:1990082.

All current fields/original review examined. No maintained image or physical measurement requires pixel/unit review. Source-body, complete-abstract, native ontology/family/protein and failed-access tiers remain distinct; optional omissions and unknowns alone are not findings.

### Current independent scientific disposition

other: concern. Targets: GO:1990082.

needs_curation: inherited minor exact DnaA/uL2 family mapping retained; in-vitro contact/function and physiological uncertainty preserved.

### Current reviewed example identities and query bounds

grounding: supported. Targets: GO:1990101.

Maintained P03004 DnaA identities agree with native reviewed status, primary genes/ordered loci and taxon83333. Current exact reviewed queries are singleton; no historical query reconstruction. Localization papers are abstract/native-annotation tier and do not prove physical membership by themselves.

### Physical formation distinct from activity and viability

grounding: unknown. Targets: GO:1990101.

Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition, origin function and organism viability are not universal constituent-absence formation assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL classification is requested.

### Original frozen inputs versus current target

provenance: supported. Targets: GO:1990101.

Record is unchanged on current main. Original source revisions/hashes and immutable YAML/Markdown were verified; independent present source reading does not invent a stale refresh or erase historical access limits.

### Positive replication pathways require matched structured-source context

scope: concern. Targets: GO:1990101.

Original prose-only adapter exclusion is unsupported for named molecular replication narratives. Fresh catalogue selects actual E.coli precise1k; five exact native loci each checked against201 modules. Only rplB b3317 passes module1 Translation threshold, confirmed in53-member list. Five-strain coverage differs from particular mutant/reconstitution preparations. Hits are not assembly/direct regulation; nonhits are not absence. No generated AI summaries or activities used.

### Actual native validation and protein coverage

schema: supported. Targets: GO:1990101.

1 reviewed examples/1 COVERED typed protein nodes; both current native commands actually exit0. HU complex and origin feature nodes are outside the protein-only inventory and separately assessed. Native success does not settle exact class mapping or full scientific completeness; original validate/render also pass.

### Append-only prior rationale and scope resolutions

provenance: supported. Targets: GO:1990101.

Earlier reference-protein additions and historical deferral statements are preserved as provenance, not treated as false current inventories. Existing interpretation boundaries are supported; exact family/feature actions append evidence and narrow current prompts/notes while preserving rationale/posed_date. No grouped or neighboring issue is terminally resolved.

### Complete maintained record and access bounds

completeness: supported. Targets: GO:1990101.

All current fields/original review examined. No maintained image or physical measurement requires pixel/unit review. Source-body, complete-abstract, native ontology/family/protein and failed-access tiers remain distinct; optional omissions and unknowns alone are not findings.

### Current independent scientific disposition

other: concern. Targets: GO:1990101.

needs_curation: inherited minor exact DnaA/oriC class mappings retained; correct early-complex scope and source-bounded assembly model preserved.

### Historical failed-access classification

provenance: concern. Targets: GO:1990083.

Original access failure and context_only limits were honest, but a failed/challenge diagnostic is incorrectly typed database. Successor retains exact original observation time/hash as validation/context_only; no new body-read assertion or biological refutation follows.

### Historical failed-access classification

provenance: concern. Targets: GO:1990083.

Original access failure and context_only limits were honest, but a failed/challenge diagnostic is incorrectly typed database. Successor retains exact original observation time/hash as validation/context_only; no new body-read assertion or biological refutation follows.

### Historical failed-access classification

provenance: concern. Targets: GO:1990103.

Original access failure and context_only limits were honest, but a failed/challenge diagnostic is incorrectly typed database. Successor retains exact original observation time/hash as validation/context_only; no new body-read assertion or biological refutation follows.

### Historical failed-access classification

provenance: concern. Targets: GO:1990103.

Original access failure and context_only limits were honest, but a failed/challenge diagnostic is incorrectly typed database. Successor retains exact original observation time/hash as validation/context_only; no new body-read assertion or biological refutation follows.

### identity hierarchy

identity: supported. Targets: GO:1990100.

The maintained ID, label and parent distinguish the exact native GO class. Direct hierarchy is not inferred from broad ancestry; retaining the correct ontology identity does not erase separately identified source-stage conflicts.

### family groundings

grounding: concern. Targets: GO:1990100.

DnaB IPR007692 and exact unintegrated DnaC NCBIfamNF005931 are available; broad IPR028350 is not substituted. Correct individual examples remain instances rather than class groundings.

### protein identities

grounding: supported. Targets: GO:1990100.

2 current examples are reviewed exact gene/taxon83333 entries with matching primary symbols and locus tokens; exact-organism searches each return one reviewed entry. Native commands passed with 2 COVERED typed protein nodes. Identity consistency is not independent experimental membership proof.

### source assembly stage

evidence: supported. Targets: GO:1990100.

Makowska-Grzyska/Kaguni directly supports DnaC-dependent DnaB delivery and staged release at oriC. Mutant loading and primase/rNTP effects are condition-scoped, not a universal stoichiometric or necessity rule.

### taxon source boundaries

scope: supported. Targets: GO:1990100.

E. coli species562 and reference K-12 taxon83333 are correctly separated. Protein reference identities do not identify every experimental derivative. The inspected sources concern purified E. coli proteins and the stated oriC or PhiX174 substrates; ontology taxon constraints and one study do not measure broad prevalence.

### stoichiometry formation

quantity: supported. Targets: GO:1990100.

Six DnaB subunits are supported; leaving DnaC count uncommitted respects multiple loading contexts and measured versus modeled ratios. UNKNOWN formation is not a viability inference.

### graph mechanism

graph: supported. Targets: GO:1990100.

The NON_MECHANISTIC graph keeps proteins, structure and biological processes distinct; broad protein families/complexes are allowed by native GENE_OR_PROTEIN policy. Its membership and delivery/initiation associations are supported without inventing quantitative kinetics.

### structured source applicability

evidence: supported. Targets: GO:1990100.

Positive named molecular components, loading/restart functions and gene examples trigger the broad structured-source policy. Current E. coli precise1k coverage and exact matched loci were inspected: five-strain context, 201 membership rows per locus, and priB module1/53-member context where applicable. These are expression context only; absence of an expression-module claim never established the original exclusion. No fresh adapter runner execution is claimed.

### history and original verdict

provenance: concern. Targets: GO:1990100.

Current record bytes match the original frozen target. Existing needs_curation verdict and exact inherited finding lineage are reconfirmed with fresh independent evidence. The unsupported notes[1] prose exclusion is a bundle assessment defect to correct additively. Dated rationale/history remain append-only; no record status promotion or terminal disposition is inferred.

### schema input integrity

schema: supported. Targets: GO:1990100.

The original native YAML validates and its renderer reproduces the committed Markdown exactly. All historical input occurrences and current frozen hashes were checked. These deterministic results do not certify scientific claims, future CI, or merge readiness.

### coverage and verdict

completeness: concern. Targets: GO:1990100.

Whole record and all original findings/actions were reviewed. Needs_curation is retained for the bounded exact-family grounding gap. No optional protein inventory, unresolved PAS-DNA class, unread figure or unmeasured universal necessity was manufactured as an additional finding.

### identity hierarchy

identity: supported. Targets: GO:1990158.

The maintained ID, label and parent distinguish the exact native GO class. Direct hierarchy is not inferred from broad ancestry; retaining the correct ontology identity does not erase separately identified source-stage conflicts.

### family groundings

grounding: concern. Targets: GO:1990158.

DnaT IPR020917 and PriA IPR005259 plus PriB IPR023646 are verified exact families. Current REVIEWED_LABEL_ONLY and active TODO remain actionable; historical earlier-pass statements need not be rewritten. Correct individual examples remain instances rather than class groundings.

### protein identities

grounding: supported. Targets: GO:1990158.

3 current examples are reviewed exact gene/taxon83333 entries with matching primary symbols and locus tokens; exact-organism searches each return one reviewed entry. Native commands passed with 3 COVERED typed protein nodes. Identity consistency is not independent experimental membership proof.

### source assembly stage

evidence: concern. Targets: GO:1990158.

NgI short PAS and NgII intact PhiX174 products must be distinguished from the GO-defined DnaC-containing loading intermediate. NgII retains PriB/PriC and excludes stable DnaC; supplied factors are not isolated constituents. The canonical example and unqualified has_part/component/graph claim conflate these stages.

### taxon source boundaries

scope: supported. Targets: GO:1990158.

E. coli species562 and reference K-12 taxon83333 are correctly separated. Protein reference identities do not identify every experimental derivative. The inspected sources concern purified E. coli proteins and the stated oriC or PhiX174 substrates; ontology taxon constraints and one study do not measure broad prevalence.

### stoichiometry formation

quantity: unknown. Targets: GO:1990158.

No new universal essentiality claim is justified for the exact maintained intermediate from a different isolated cohort. NgII PriA-omission and PriC-dependent effects have stated substrate/assay scope. Unknown PAS-DNA grounding and unresolved copy numbers are retained, not forced into oriC or an invariant oligomer.

### graph mechanism

graph: concern. Targets: GO:1990158.

The NON_MECHANISTIC graph keeps proteins, structure and biological processes distinct; broad protein families/complexes are allowed by native GENE_OR_PROTEIN policy. Correct node types and covered examples do not cure the source-stage/cohort issue in membership and downstream source notes; qualify those edges while preserving identity.

### structured source applicability

evidence: supported. Targets: GO:1990158.

Positive named molecular components, loading/restart functions and gene examples trigger the broad structured-source policy. Current E. coli precise1k coverage and exact matched loci were inspected: five-strain context, 201 membership rows per locus, and priB module1/53-member context where applicable. These are expression context only; absence of an expression-module claim never established the original exclusion. No fresh adapter runner execution is claimed.

### history and original verdict

provenance: concern. Targets: GO:1990158.

Current record bytes match the original frozen target. Existing needs_curation verdict and exact inherited finding lineage are reconfirmed with fresh independent evidence. The unsupported notes[1] prose exclusion is a bundle assessment defect to correct additively. Dated rationale/history remain append-only; no record status promotion or terminal disposition is inferred.

### schema input integrity

schema: supported. Targets: GO:1990158.

The original native YAML validates and its renderer reproduces the committed Markdown exactly. All historical input occurrences and current frozen hashes were checked. These deterministic results do not certify scientific claims, future CI, or merge readiness.

### coverage and verdict

completeness: concern. Targets: GO:1990158.

Whole record and all original findings/actions were reviewed. Needs_curation is retained for the material source-stage/cohort conflict and bounded exact-family grounding gap. No optional protein inventory, unresolved PAS-DNA class, unread figure or unmeasured universal necessity was manufactured as an additional finding.

### identity hierarchy

identity: supported. Targets: GO:1990159.

The maintained ID, label and parent distinguish the exact native GO class. Direct hierarchy is not inferred from broad ancestry; retaining the correct ontology identity does not erase separately identified source-stage conflicts.

### family groundings

grounding: concern. Targets: GO:1990159.

DnaT IPR020917 and PriA IPR005259 plus PriC IPR010890 are verified exact families. Current REVIEWED_LABEL_ONLY and active TODO remain actionable; historical earlier-pass statements need not be rewritten. Correct individual examples remain instances rather than class groundings.

### protein identities

grounding: supported. Targets: GO:1990159.

3 current examples are reviewed exact gene/taxon83333 entries with matching primary symbols and locus tokens; exact-organism searches each return one reviewed entry. Native commands passed with 3 COVERED typed protein nodes. Identity consistency is not independent experimental membership proof.

### source assembly stage

evidence: concern. Targets: GO:1990159.

NgI short PAS and NgII intact PhiX174 products must be distinguished from the GO-defined DnaC-containing loading intermediate. NgII retains PriB/PriC and excludes stable DnaC; supplied factors are not isolated constituents. The PriB-excluded canonical cohort and directly attributed replication-through-restart outcome overstate this study.

### taxon source boundaries

scope: supported. Targets: GO:1990159.

E. coli species562 and reference K-12 taxon83333 are correctly separated. Protein reference identities do not identify every experimental derivative. The inspected sources concern purified E. coli proteins and the stated oriC or PhiX174 substrates; ontology taxon constraints and one study do not measure broad prevalence.

### stoichiometry formation

quantity: unknown. Targets: GO:1990159.

No new universal essentiality claim is justified for the exact maintained intermediate from a different isolated cohort. NgII PriA-omission and PriC-dependent effects have stated substrate/assay scope. Unknown PAS-DNA grounding and unresolved copy numbers are retained, not forced into oriC or an invariant oligomer.

### graph mechanism

graph: concern. Targets: GO:1990159.

The NON_MECHANISTIC graph keeps proteins, structure and biological processes distinct; broad protein families/complexes are allowed by native GENE_OR_PROTEIN policy. Correct node types and covered examples do not cure the source-stage/cohort issue in membership and downstream source notes; qualify those edges while preserving identity.

### structured source applicability

evidence: supported. Targets: GO:1990159.

Positive named molecular components, loading/restart functions and gene examples trigger the broad structured-source policy. Current E. coli precise1k coverage and exact matched loci were inspected: five-strain context, 201 membership rows per locus, and priB module1/53-member context where applicable. These are expression context only; absence of an expression-module claim never established the original exclusion. No fresh adapter runner execution is claimed.

### history and original verdict

provenance: concern. Targets: GO:1990159.

Current record bytes match the original frozen target. Existing needs_curation verdict and exact inherited finding lineage are reconfirmed with fresh independent evidence. The unsupported formal check is a bundle assessment defect to correct additively. Dated rationale/history remain append-only; no record status promotion or terminal disposition is inferred.

### schema input integrity

schema: supported. Targets: GO:1990159.

The original native YAML validates and its renderer reproduces the committed Markdown exactly. All historical input occurrences and current frozen hashes were checked. These deterministic results do not certify scientific claims, future CI, or merge readiness.

### coverage and verdict

completeness: concern. Targets: GO:1990159.

Whole record and all original findings/actions were reviewed. Needs_curation is retained for the material source-stage/cohort conflict and bounded exact-family grounding gap. No optional protein inventory, unresolved PAS-DNA class, unread figure or unmeasured universal necessity was manufactured as an additional finding.

### Exact structural identity and boundary

identity: supported. Targets: GO:1990160.

Exact DnaB-DnaC-Rep-PriC/PAS-DNA pre-primosome ontology identity is coherent; canonical active-fork experiment is a different measured stage.

### Typed parents, parthood and aliases

identity: supported. Targets: GO:1990160.

Current GO confirms stated class relations. Primase-free pre-primosome parent and related PhiX174 synonym do not collapse PriA/PriB/PriC/DnaT alternatives or add DnaG.

### Full-family mappings versus domain and example

grounding: concern. Targets: GO:1990160.

Exact full-protein family authority mappings and native example memberships reconfirm the inherited localized grounding finding. Existing label-only notes defer curation rather than identify a scope mismatch. PAS-DNA remains unresolved and is not automatically oriC.

### Native accession, gene and taxon

grounding: supported. Targets: GO:1990160.

2 reviewed examples and 2 COVERED nodes retain correct current identities. Primary Rep P09980 differs from plasmid RepE P03856 carrying synonym rep; current alias-inclusive query does not negate correct primary-name selection or dated provenance.

### Measured experimental assembly and source scope

evidence: concern. Targets: GO:1990160.

Guy tests accessory action on active oriC-initiated forks without PriC and places Rep-DnaB binding after loading; Ng retained a different PriA/PriB/PriC/DnaT/DnaB assembly. Neither directly establishes the maintained quartet canonical example; native restart identity is not denied.

### Citation identity and authors

provenance: supported. Targets: GO:1990160.

Inspected publication identities,author lists,year and DOI match the cited sources; source-stage concerns are separate.

### Measured quantities and conditional scope

grounding: not_applicable. Targets: GO:1990160.

No invariant quartet stoichiometry is asserted; individual protein associations do not establish a whole-quartet count.

### Formation necessity versus function

grounding: unknown. Targets: GO:1990160.

UNKNOWN formation essentiality is not contradicted by catalytic output or activity measurements. PriA/PriC omission results in Ng concern a different cohort; no universal Rep/PriC-quartet necessity follows.

### Whole nonmechanistic graph and stage limits

graph: supported. Targets: GO:1990160.

Graph remains explicitly NONMECHANISTIC/FUNCTION at GO-level loading/restart and PAS scaffold, not a claimed kinetic reconstruction of Guy active-fork experiments.

### Biological source and experimental host

scope: supported. Targets: GO:1990160.

Species562 and K12 reference83333 are correct; COMMON is qualitative, not a measured prevalence census. Guy uvrD-cloning MG1655 and unread supplementary strains are not equated with every assay.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:1990160.

Positive molecular/pathway assertions require coverage evaluation; original formal no-expression exclusion is unsupported. Fresh E.coli precise1k exact loci have no thresholded memberships across201 modules, which is not absence of expression or structural participation.

### Native originals and historical/current hashes

schema: supported. Targets: GO:1990160.

All three original pairs validate/render0 with exact Markdown and all39 historical input occurrences verified. Current targets remain byte-identical to frozen originals. Native protein checks0 at current source; historical corpus checks are not current CI.

### Historical rationale and future corrective scope

provenance: supported. Targets: GO:1990160.

Historical discussions/actions remain unchanged. Future record curation may update current notes/status or append dated clarification, without rewriting original rationale or promoting review status automatically.

### Complete record and access limits

completeness: supported. Targets: GO:1990160.

Every current definition,alias,parent,component/example,taxon,function,evidence,graph edge,discussion and history assessed. No maintained images; no figure pixels,raw-data reanalysis,unread supplements or full Bailey/Mitkova body certified. Optional fields do not automatically require additions.

### Current independent disposition

consistency: concern. Targets: GO:1990160.

Needs curation for inherited canonical-stage major and exact-family minor; original Rep query F3 is rejected, not a record-curation requirement.

### Exact structural identity and boundary

identity: supported. Targets: GO:1990156.

Exact DnaB-DnaG helicase-primase complex, distinct from DNA-containing whole core primosome.

### Typed parents, parthood and aliases

identity: supported. Targets: GO:1990156.

Current GO confirms stated class relations. DnaB-DnaG part_of core primosome is explicit; is_a helicase-complex relation remains distinct.

### Full-family mappings versus domain and example

grounding: concern. Targets: GO:1990156.

Exact full-protein family authority mappings and native example memberships reconfirm the inherited localized grounding finding. Existing label-only notes defer curation rather than identify a scope mismatch. Domain-only or unchecked broader generated descriptions are not substitutes.

### Native accession, gene and taxon

grounding: supported. Targets: GO:1990156.

2 reviewed examples and 2 COVERED nodes retain correct current identities. Reference accessions do not silently identify every experimental reagent or strain.

### Measured experimental assembly and source scope

evidence: supported. Targets: GO:1990156.

Primary Mitkova abstract directly supports isolated stabilized E.coli DnaB-DnaG binding/stoichiometry; no unseen full-body or supplement claims.

### Citation identity and authors

provenance: concern. Targets: GO:1990156.

PMID14557266/DOI10.1074/jbc.M308956200 identify Mitkova,Khopde,Biswas2003; repeated current Tougu/Marians attribution is incorrect. Supported measurements and exact DOI/PMID remain valid.

### Measured quantities and conditional scope

grounding: supported. Targets: GO:1990156.

Six DnaB and three DnaG are explicitly scoped to stabilized E.coli complex; no universal in-vivo ratio inferred.

### Formation necessity versus function

grounding: unknown. Targets: GO:1990156.

UNKNOWN formation essentiality is not contradicted by catalytic output or activity measurements. Primase ssDNA binding for primer synthesis does not itself prove universal complex-formation necessity.

### Whole nonmechanistic graph and stage limits

graph: supported. Targets: GO:1990156.

Coarse nonmechanistic primer-output graph is supported; chemical crosslinks do not create a detailed loading/release model.

### Biological source and experimental host

scope: supported. Targets: GO:1990156.

E.coli/K12 annotation and stabilized experimental species are correct; exact expression strain is not established by the abstract.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:1990156.

Positive molecular/pathway assertions require coverage evaluation; original formal no-expression exclusion is unsupported. Fresh E.coli precise1k dnaG is in Nucleotide Stress10; dnaB has no thresholded hit. Expression membership is not binding/formation evidence.

### Native originals and historical/current hashes

schema: supported. Targets: GO:1990156.

All three original pairs validate/render0 with exact Markdown and all39 historical input occurrences verified. Current targets remain byte-identical to frozen originals. Native protein checks0 at current source; historical corpus checks are not current CI.

### Historical rationale and future corrective scope

provenance: supported. Targets: GO:1990156.

Historical discussions/actions remain unchanged. Future record curation may update current notes/status or append dated clarification, without rewriting original rationale or promoting review status automatically.

### Complete record and access limits

completeness: supported. Targets: GO:1990156.

Every current definition,alias,parent,component/example,taxon,function,evidence,graph edge,discussion and history assessed. No maintained images; no figure pixels,raw-data reanalysis,unread supplements or full Bailey/Mitkova body certified. Optional fields do not automatically require additions.

### Current independent disposition

consistency: concern. Targets: GO:1990156.

Needs curation for two inherited minor findings: exact families and repeated author attribution.

### Exact structural identity and boundary

identity: supported. Targets: GO:1990161.

Exact DnaB homohexamer, distinct from DnaB-DnaG or loading complexes.

### Typed parents, parthood and aliases

identity: supported. Targets: GO:1990161.

Current GO confirms stated class relations. The generic DNA-helicase parent does not add loading or primase subunits to this homohexamer.

### Full-family mappings versus domain and example

grounding: concern. Targets: GO:1990161.

Exact full-protein family authority mappings and native example memberships reconfirm the inherited localized grounding finding. Existing label-only notes defer curation rather than identify a scope mismatch. Domain-only or unchecked broader generated descriptions are not substitutes.

### Native accession, gene and taxon

grounding: supported. Targets: GO:1990161.

1 reviewed examples and 1 COVERED nodes retain correct current identities. Reference accessions do not silently identify every experimental reagent or strain.

### Measured experimental assembly and source scope

evidence: supported. Targets: GO:1990161.

Bailey primary abstract plus exact2R6D entry/entity/assembly metadata support DnaB-alone six-subunit form; DnaG-domain structures are separately described.

### Citation identity and authors

provenance: supported. Targets: GO:1990161.

Inspected publication identities,author lists,year and DOI match the cited sources; source-stage concerns are separate.

### Measured quantities and conditional scope

grounding: supported. Targets: GO:1990161.

Six identical DnaB subunits are directly represented by exact2R6D assembly1; no DnaG is present in that deposited form.

### Formation necessity versus function

grounding: unknown. Targets: GO:1990161.

UNKNOWN formation essentiality is not contradicted by catalytic output or activity measurements. Observed homohexamer and helicase activity do not by themselves establish a component-removal phenotype for all conditions.

### Whole nonmechanistic graph and stage limits

graph: supported. Targets: GO:1990161.

Coarse ATP-dependent DNA-unwinding graph is supported at native/abstract tier; no newly inferred conformational sequence.

### Biological source and experimental host

scope: supported. Targets: GO:1990161.

Biological Geobacillus1422/Bacillus old synonym is correct; E.coli BL21(DE3) is the expression host, not the maintained biological taxon. COMMON is not a population prevalence estimate.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:1990161.

Positive molecular/pathway assertions require coverage evaluation; original formal no-expression exclusion is unsupported. Fresh complete catalogue has no Geobacillus stearothermophilus dataset; unrelated Bacillus subtilis or E.coli expression-host data are not substituted. Coverage nonmatch does not mean biology absent.

### Native originals and historical/current hashes

schema: supported. Targets: GO:1990161.

All three original pairs validate/render0 with exact Markdown and all39 historical input occurrences verified. Current targets remain byte-identical to frozen originals. Native protein checks0 at current source; historical corpus checks are not current CI.

### Historical rationale and future corrective scope

provenance: supported. Targets: GO:1990161.

Historical discussions/actions remain unchanged. Future record curation may update current notes/status or append dated clarification, without rewriting original rationale or promoting review status automatically.

### Complete record and access limits

completeness: supported. Targets: GO:1990161.

Every current definition,alias,parent,component/example,taxon,function,evidence,graph edge,discussion and history assessed. No maintained images; no figure pixels,raw-data reanalysis,unread supplements or full Bailey/Mitkova body certified. Optional fields do not automatically require additions.

### Current independent disposition

consistency: concern. Targets: GO:1990161.

Needs curation for inherited minor exact-family mapping, preserving correct homohexamer identity and protein source.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:1990083, GO:1990103, GO:1990082, GO:1990101, GO:1990100, GO:1990158, GO:1990159, GO:1990160, GO:1990156, GO:1990161.

0 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Correct the inherited RIDA chemistry

major / open / confirmed; issue key: dnaa-hda-definition-phosphorylation-versus-hydrolysis.

The definition says Hda inactivates DnaA by inhibiting phosphorylation of DnaA-ADP to DnaA-ATP. This matches current GO1990083 but conflicts with the cited Keyamura/Katayama2011 staged hydrolysis assay and the target’s own ATP-hydrolysis canonical/graph text. RIDA promotes hydrolysis of bound ATP; reactivation by DARS uses nucleotide exchange.

### micro-F2: Resolve the exact DnaA and Hda families

minor / open / confirmed; issue key: dnaa-hda-exact-component-families.

DnaA IPR001957 and Hda IPR017788 are available exact whole-protein families and are independently present in the verified examples. The current REVIEWED_LABEL_ONLY rows and open TODO can therefore be resolved; narrower Hda IPR022864 is not the generic class.

### micro-F3: Resolve DnaA and oriC class mappings

minor / open / confirmed; issue key: dnaa-hu-dnaa-oric-exact-groundings.

The DnaA constituent has exact whole-protein family IPR001957 and the origin-DNA scaffold has exact SO0000953. Both remain REVIEWED_LABEL_ONLY with an open mapping task. The HU dimer boundary is a separate unresolved complex class, not a reason to defer these two exact matches.

### micro-F4: Resolve the DnaA and50S-L2 family mappings

minor / open / confirmed; issue key: dnaa-l2-exact-component-families.

The two named classes have exact whole-protein families DnaA IPR001957 and bacterial/organellar uL2 IPR005880, independently corroborated by current examples. The universal IPR002171 parent is broader than the declared50S-L2 class; current label-only states and mapping task can be narrowed.

### micro-F5: Resolve verified existing component-class groundings

minor / open / confirmed; issue key: dnaa-oric-complex-exact-component-groundings.

DnaA exactly maps to InterProIPR001957 and oriC to SO0000953. Native family/ontology identities plus independently inspected protein cross-references establish the matches. The current reviewed-label-only/open-task representation leaves these actionable classes unresolved. Historical earlier-pass statements are not declared false merely because current verification is available.

### plaque-t4-F1: Resolve verified existing component-class groundings

minor / open / confirmed; issue key: dnab-dnac-complex-exact-component-groundings.

DnaB exactly maps to InterProIPR007692 and DnaC to the unintegrated but exact NCBIfamNF005931. Broad DnaC/IstBIPR028350 is not the proposed match. Native family/ontology identities plus independently inspected protein cross-references establish the matches. The current reviewed-label-only/open-task representation leaves these actionable classes unresolved. Historical earlier-pass statements are not declared false merely because current verification is available.

### plaque-t5-F1: Separate the loader-containing model from isolated preprimosome composition

major / open / confirmed; issue key: dnab-dnac-dnat-pria-prib-source-stage-conflation.

Current GO1990158 names a DnaB-DnaC-containing complex, and the record turns that model into an unqualified constituent/has_part and graph claim while treating Ng experiments as its canonical source. NgI explicitly reports final PriA/PriB/DnaT/DnaB without DnaC. NgII pp15653–54 likewise rejects stable DnaC membership and retains PriC on intact PhiX174 DNA, unlike the short PAS substrate. Input proteins, transient loading and stable isolated composition are therefore conflated. Native authority and experimental observation must both remain visible.

### plaque-t5-F2: Resolve verified existing component-class groundings

minor / open / confirmed; issue key: dnab-dnac-dnat-pria-prib-complex-exact-component-groundings.

DnaT, PriA and PriB exactly map to InterProIPR020917, IPR005259 and IPR023646, respectively. DnaT natural proteobacterial scope is stated; the PriB/SSB parent and helicase domains are not substituted. Native family/ontology identities plus independently inspected protein cross-references establish the matches. The current reviewed-label-only/open-task representation leaves these actionable classes unresolved. Historical earlier-pass statements are not declared false merely because current verification is available.

### plaque-t6-F1: Separate the cited PhiX product from the maintained loading intermediate

major / open / confirmed; issue key: pria-pric-source-cohort.

The record treats NgII as direct evidence for a PriB-excluded DnaB-DnaC-DnaT-PriA-PriC assembly, including its canonical example, constituent notes and replication-through-restart function. NgII pp15653–54 explicitly reports a stable PriA/PriB/PriC/DnaT/DnaB complex and rejects DnaC as a stable constituent; its repair/restart extension is proposed. The correct GO identifier does not make the experimentally different cohort equivalent.

### plaque-t6-F2: Ground DnaT, PriA and PriC with exact families

minor / open / confirmed; issue key: pria-pric-exact-families.

The three REVIEWED_LABEL_ONLY protein rows defer mapping despite exact full-protein families IPR020917, IPR005259 and IPR010890 and independent membership of their correct K12 examples.

### septin-dnab_dnac_rep_pric_complex-F1: Use an exact Rep-PriC loading example rather than the active-fork experiment

major / open / confirmed; issue key: rep-pric-canonical-stage.

Guy2009 is the canonical example for this four-protein preprimosome, but its main replication assay omits PriC and studies Rep-assisted movement of oriC-initiated forks. Its Results explicitly show DnaC inhibition of Rep-DnaB binding and place that interaction after loading. NgII also does not supply the missing quartet: its retained PhiX assembly contains PriA/PriB/PriC/DnaT/DnaB. Independently reconfirmed against the current unchanged record and exact scoped source evidence. Preserve historical rationale; update current notes/status or append a dated clarification only in separately authorized curation.

### septin-dnab_dnac_rep_pric_complex-F2: Ground Rep and PriC with exact families

minor / open / confirmed; issue key: rep-pric-exact-families.

Two reviewed-label-only rows defer exact mappings despite Rep IPR005752 and PriC IPR010890, supported by exact family signatures and the separately verified examples. Independently reconfirmed against the current unchanged record and exact scoped source evidence. Preserve historical rationale; update current notes/status or append a dated clarification only in separately authorized curation.

### septin-dnab_dnac_rep_pric_complex-F3: Reject unsupported inference from the alias-inclusive Rep search

minor / rejected / confirmed; issue key: rep-query-alias-uniqueness.

Original F3 overstated that the current single-reviewed-Rep claim was false at a stated query scope. The record names correct Rep helicase P09980 and primary gene rep but does not specify an alias-inclusive endpoint. The fresh exact-gene query also returns primary repE/P03856 because rep is its synonym. That current ambiguity does not negate correct primary-name/protein-identity selection or reconstruct the dated query. Automatic ambiguous seeding should abstain, but manual disambiguation is valid. Optional alias clarification is not a demonstrated mandatory correction; preserve current accession and dated history.

Disposition: Current alias-inclusive search does not establish the record used that endpoint or invalidate the correctly identified primary Rep helicase; it cannot reconstruct a dated query. Mandatory record correction is unsupported.

### septin-dnab_dnag_complex-F1: Ground the DnaB and bacterial DnaG constituents

minor / open / confirmed; issue key: dnab-dnag-exact-families.

IPR007692 and IPR030846 are exact full-protein families for the maintained helicase and bacterial primase, with independent native example membership. The label-only notes merely defer curation. Independently reconfirmed against the current unchanged record and exact scoped source evidence. Preserve historical rationale; update current notes/status or append a dated clarification only in separately authorized curation.

### septin-dnab_dnag_complex-F2: Correct the repeated 2003 author attribution

minor / open / confirmed; issue key: dnab-dnag-citation-authors.

PMID14557266 and DOI10.1074/jbc.M308956200 identify Mitkova, Khopde and Biswas2003. The target repeatedly attributes this exact paper and its measurements to Tougu and Marians. Independently reconfirmed against the current unchanged record and exact scoped source evidence. Preserve historical rationale; update current notes/status or append a dated clarification only in separately authorized curation.

### septin-dnab_helicase_complex-F1: Ground the DnaB monomer with its exact family

minor / open / confirmed; issue key: dnab-helicase-exact-family.

The monomeric DnaB component remains REVIEWED_LABEL_ONLY although IPR007692 is the exact full DnaB-type helicase family and native Q9X4C9 independently carries this family. Independently reconfirmed against the current unchanged record and exact scoped source evidence. Preserve historical rationale; update current notes/status or append a dated clarification only in separately authorized curation.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, replace the mechanism sentence with source-backed DnaA-bound ATP hydrolysis in its DNA-loaded-clamp/ADP-Hda context. Preserve exact GO identity and record the upstream definition conflict; do not silently describe a revised primary-source definition as a verbatim GO definition.

- The corrected text distinguishes hydrolysis from nucleotide exchange and phosphorylation.
- Retain the binary contact versus full active RIDA-system boundary.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR. Keep actual experimental/body/abstract/authority scopes and do not force universal formation necessity or optional examples.

### micro-A2

In separately authorized record curation, ground DnaA and Hda with the exact families and narrow/resolve the corresponding mapping task, retaining the taxon-paired examples.

- Check native family types/signatures and separate example cross-references.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR. Keep actual experimental/body/abstract/authority scopes and do not force universal formation necessity or optional examples.

### micro-A3

In separately authorized record curation, ground DnaA and oriC with their verified class identifiers and narrow the open task to any remaining HU-complex identity. Preserve the dimer and its context-dependent subunit alternatives.

- Do not ground a whole HU dimer to an individual-protein family.
- Do not substitute a single origin sequence accession for the oriC feature class.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR. Keep actual experimental/body/abstract/authority scopes and do not force universal formation necessity or optional examples.

### micro-A4

In separately authorized record curation, ground the two protein classes with the verified exact families, retain correct examples, and resolve/narrow the mapping task without importing unrelated ribosomal mechanisms.

- Verify class scope and integrated full-protein signatures.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR. Keep actual experimental/body/abstract/authority scopes and do not force universal formation necessity or optional examples.

### micro-A5

In separately authorized record curation, add the verified exact class CURIEs with source-specific evidence, update the corresponding grounding states/open task, and preserve organism accessions as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.

- Every added CURIE denotes the existing class at the stated scope, not an individual species protein.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated discussions.rationale, posed_date and curation history; append provenance and narrow current notes/prompt only as supported.
- No record edits occur in this review PR. Keep actual experimental/body/abstract/authority scopes and do not force universal formation necessity or optional examples.

### plaque-t4-A1

Add the verified exact class CURIEs with source-specific evidence, update the corresponding grounding states/open task, and preserve organism accessions as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.

- Every added CURIE denotes the existing class at the stated scope, not an individual species protein.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale and curation history; append source-specific current notes or reopen/qualify the active decision without rewriting historical provenance.

### plaque-t5-A1

Preserve GO1990158 and explicitly distinguish its loader-containing assembly model from the Ng isolated complexes. Qualify the stage/source of DnaC parthood and graph membership, identify which substrate/stage the canonical example demonstrates, and retain the PriC-dependent intact-DNA versus short-PAS distinction. Inspect an appropriate primary source before claiming direct observation of the exact DnaC-containing assembly.

- Stable composition is not inferred from proteins supplied to the reaction.
- The action preserves current identity and reports the authority/source conflict without silently replacing it.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale and curation history; append source-specific current notes or reopen/qualify the active decision without rewriting historical provenance.

### plaque-t5-A2

Add the verified exact class CURIEs with source-specific evidence, update the corresponding grounding states/open task, and preserve organism accessions as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.

- Every added CURIE denotes the existing class at the stated scope, not an individual species protein.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale and curation history; append source-specific current notes or reopen/qualify the active decision without rewriting historical provenance.

### plaque-t6-A1

Keep the intended GO1990159 identity, but separate GO-defined loading/restart scope from NgI/II experimental context. Replace or qualify the canonical example and affected source notes with evidence for the exact PriA/PriC intermediate; explicitly distinguish loading factors from isolated product composition.

- Do not add PriB or remove DnaC solely to turn this record into a different assembly.
- Do not present NgII as a directly measured repaired-fork restart experiment.
- Retain correct protein identities and the genuinely supported PhiX study context.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Preserve dated rationale and curation history; append source-specific current notes or reopen/qualify the active decision without rewriting historical provenance.

### plaque-t6-A2

Use the verified DnaT/PriA/PriC family mappings and align current grounding notes/TODO, retaining unresolved PAS-DNA grounding.

- Do not substitute a generic helicase/ATPase or DnaT domain.
- Do not convert PAS DNA to chromosomal oriC.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Preserve dated rationale and curation history; append source-specific current notes or reopen/qualify the active decision without rewriting historical provenance.

### septin-dnab_dnac_rep_pric_complex-A1

Replace or explicitly contextualize Guy2009 as accessory-fork evidence, and use an independently verified exact Rep/PriC loading/restart source for the canonical quartet. Preserve the ontology identity and distinguish sequential loading from the active-fork complex. Preserve dated rationale/history and source-specific limits; this review PR edits no scientific record.

- Do not deny the native Rep/PriC restart pathway or infer that no such intermediate exists.
- Do not claim Guy tested PriC or directly isolated the maintained quartet.
- Keep the correct E.coli and reference-protein identifiers.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Keep exact original finding lineage; preserve dated rationale with any clarification appended rather than rewritten.

### septin-dnab_dnac_rep_pric_complex-A2

Apply the exact Rep/PriC protein-family identities and align current notes/TODO while retaining unresolved PAS DNA. Preserve dated rationale/history and source-specific limits; this review PR edits no scientific record.

- Do not import the erroneous Rep hexamer prose or substitute the generic UvrD/helicase domain.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Keep exact original finding lineage; preserve dated rationale with any clarification appended rather than rewritten.

### septin-dnab_dnag_complex-A1

Use the exact DnaB and bacterial DnaG family mappings and align grounding notes/TODO. Preserve dated rationale/history and source-specific limits; this review PR edits no scientific record.

- Do not substitute domain IPR006295 or broaden to unchecked archaeal/exosome descriptions.
- Retain qualified three-DnaG stabilized-complex stoichiometry.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Keep exact original finding lineage; preserve dated rationale with any clarification appended rather than rewritten.

### septin-dnab_dnag_complex-A2

Replace the incorrect author names with Mitkova etal2003 in current scientific/evidence notes, preserving the correct PMID/DOI/title and supported measurements. Preserve dated rationale/history and source-specific limits; this review PR edits no scientific record.

- Check every current author mention consistently.
- Do not reinterpret the legitimate condition-scoped stoichiometry as erroneous.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Keep exact original finding lineage; preserve dated rationale with any clarification appended rather than rewritten.

### septin-dnab_helicase_complex-A1

Ground the protein constituent with IPR007692 and align its current notes/TODO, retaining the homohexamer identity and six-copy stoichiometry. Preserve dated rationale/history and source-specific limits; this review PR edits no scientific record.

- Keep Q9X4C9 and biological source1422, distinct from the expression host.
- Do not substitute a DnaB domain or broad ATPase fold.
- Preserve correct identifiers and source-supported biology; pass applicable native validation.
- Keep exact original finding lineage; preserve dated rationale with any clarification appended rather than rewritten.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/dnaa_hda_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e; current SHA256 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T060738Z-dnaa-hda-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/dnaa_hu_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3; current SHA256 c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T060739Z-dnaa-hu-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/dnaa_l2_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd; current SHA256 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T060740Z-dnaa-l2-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/dnaa_oric_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976; current SHA256 af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T060740Z-dnaa-oric-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/dnab_dnac_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180; current SHA256 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5; current SHA256 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43; current SHA256 af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/dnab_dnac_rep_pric_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f; current SHA256 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T060743Z-dnab-dnac-rep-pric-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/dnab_dnag_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c; current SHA256 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T060744Z-dnab-dnag-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/dnab_helicase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99; current SHA256 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T060744Z-dnab-helicase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/dnaa_hda_complex.yaml; Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-0 | reviews/structured/20261022T060738Z-dnaa-hda-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions inspected; historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/0-stale.diff; Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed | supports | Empty target diff: no stale scientific field in this assigned four-record slice. Current primary and authority reassessment was nevertheless performed. |
| micro-record-1 | data/structures/other/dnaa_hu_complex.yaml; Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-1 | reviews/structured/20261022T060739Z-dnaa-hu-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions inspected; historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/1-stale.diff; Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed | supports | Empty target diff: no stale scientific field in this assigned four-record slice. Current primary and authority reassessment was nevertheless performed. |
| micro-record-2 | data/structures/other/dnaa_l2_complex.yaml; Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-2 | reviews/structured/20261022T060740Z-dnaa-l2-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions inspected; historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/2-stale.diff; Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed | supports | Empty target diff: no stale scientific field in this assigned four-record slice. Current primary and authority reassessment was nevertheless performed. |
| micro-record-3 | data/structures/other/dnaa_oric_complex.yaml; Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02 | supports | All identity, hierarchy, components/examples, functions, canonical taxa, graph edges, evidence, discussions and history inspected. No maintained images or measurements. Current record is byte-identical to its original frozen target. |
| micro-prior-3 | reviews/structured/20261022T060740Z-dnaa-oric-complex-audit/review.yaml; Complete immutable original YAML and deterministic Markdown | supports | Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions inspected; historical checks and access timestamps are not newly executed or fetched. |
| micro-delta-3 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/3-stale.diff; Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed | supports | Empty target diff: no stale scientific field in this assigned four-record slice. Current primary and authority reassessment was nevertheless performed. |
| micro-policy | docs/CURATION.md; Exact taxon-neutral family/class grounding, formation versus function and append-only discussions | supports | Current verified exact mappings are consequential class-grounding gaps under the local contract, not demands for optional examples. UNKNOWN formation is valid. Preserve historical rationale/posed_date; narrow current prompt/notes only after supported separate curation. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; ComponentTypeEnum, exact grounding, essentiality, complex/feature and graph scopes | supports | HU dimer is a complex, not a single HU-family protein; oriC is a feature class, not one strain sequence. Generic named classes and NONMECHANISTIC FUNCTION outlines are valid; physical formation is distinct from viability, initiation activity or depletion experiments. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks; current profile, config, rubric and shared review contract | supports | Positive molecular/pathway claims require structured-source applicability even without expression assertions. Seventeen common inputs retain exact prior-read hashes; AGENTS, skill, profile, config, review contract and pertinent family/history/graph clauses reread for this task. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Constituent references, direct versus contextual evidence, scoped function outlines | supports | Descriptive membership/function can be supported without a full mechanistic reaction sequence, exact stoichiometry, universal essentiality or mandatory new experiments. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/original-audit.json; Eight actual original validate/render commands;56 historical input occurrences;8 original artifacts | supports | All four original YAMLs validate and render exactly their retained Markdown. All56 historical input hashes match recorded source revisions; all8 original artifacts equal the original PR head. |
| micro-protein-P03004 | https://rest.uniprot.org/uniprotkb/P03004.json; Native identity/status/name/primary gene/loci/taxon/InterPro and stated annotation sections; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/protein-P03004.raw | supports | P03004: UniProtKB reviewed (Swiss-Prot); Chromosomal replication initiator protein DnaA; genes ['dnaA']; loci ['b3702', 'JW3679']; taxon 83333; InterPro ['IPR003593', 'IPR001957', 'IPR020591', 'IPR018312', 'IPR013159', 'IPR013317', 'IPR024633', 'IPR038454', 'IPR027417', 'IPR010921']. Complete relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY annotations read; native references do not imply every linked primary body was read. DnaA localization papers are independently complete abstract tier only; the native 10-percent membrane example explicitly concerns BL21(DE3), not an exact K12 complex assay. |
| micro-protein-P60422 | https://rest.uniprot.org/uniprotkb/P60422.json; Native identity/status/name/primary gene/loci/taxon/InterPro and stated annotation sections; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/protein-P60422.raw | supports | P60422: UniProtKB reviewed (Swiss-Prot); Large ribosomal subunit protein uL2; genes ['rplB']; loci ['b3317', 'JW3279']; taxon 83333; InterPro ['IPR012340', 'IPR014722', 'IPR002171', 'IPR005880', 'IPR022669', 'IPR022671', 'IPR014726', 'IPR022666', 'IPR008991']. Complete relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY annotations read; native references do not imply every linked primary body was read. Current recommended uL2 name and rplB primary gene match historical 50S-L2 wording; generic ribosomal functions are not evidence of DnaA binding, which has its own primary paper. |
| micro-protein-P69931 | https://rest.uniprot.org/uniprotkb/P69931.json; Native identity/status/name/primary gene/loci/taxon/InterPro and stated annotation sections; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/protein-P69931.raw | supports | P69931: UniProtKB reviewed (Swiss-Prot); DnaA regulatory inactivator Hda; genes ['hda']; loci ['b2496', 'JW5397', 'f248c']; taxon 83333; InterPro ['IPR020591', 'IPR013317', 'IPR017788', 'IPR022864', 'IPR055199', 'IPR027417']. Complete relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY annotations read; native references do not imply every linked primary body was read. hda primary name and idaB/yfgE aliases support the intended K12 example; Hda-TrfA annotation and Hda-beta-clamp state do not make TrfA or beta constitutive members of the separately scoped binary record. |
| micro-gene-dnaA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-dnaA.raw | supports | Current bounded query returns ['P03004']; primary gene/locus/status/taxon inspected. The hupA/hupB results are contextual dimer alternatives for dataset selection, not required new maintained examples. No historical-query reconstruction. |
| micro-gene-hda | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-hda.raw | supports | Current bounded query returns ['P69931']; primary gene/locus/status/taxon inspected. The hupA/hupB results are contextual dimer alternatives for dataset selection, not required new maintained examples. No historical-query reconstruction. |
| micro-gene-hupA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-hupA.raw | supports | Current bounded query returns ['P0ACF0']; primary gene/locus/status/taxon inspected. The hupA/hupB results are contextual dimer alternatives for dataset selection, not required new maintained examples. No historical-query reconstruction. |
| micro-gene-hupB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-hupB.raw | supports | Current bounded query returns ['P0ACF4']; primary gene/locus/status/taxon inspected. The hupA/hupB results are contextual dimer alternatives for dataset selection, not required new maintained examples. No historical-query reconstruction. |
| micro-gene-rplB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArplB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-rplB.raw | supports | Current bounded query returns ['P60422']; primary gene/locus/status/taxon inspected. The hupA/hupB results are contextual dimer alternatives for dataset selection, not required new maintained examples. No historical-query reconstruction. |
| micro-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/tax-562.raw | supports | 562: Escherichia coli; rank species. Species562 is distinct from K12 reference-strain83333; this does not identify an unread experimental strain. |
| micro-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/tax-83333.raw | supports | 83333: Escherichia coli K-12; rank strain. Species562 is distinct from K12 reference-strain83333; this does not identify an unread experimental strain. |
| micro-go-0006270 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006270; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-0006270.raw | supports | GO:0006270: DNA replication initiation; obsolete=False; definition {'text': 'The process in which DNA-dependent DNA replication is started; it begins when specific sequences, known as origins of replication, are recognized and bound by the origin recognition complex, followed by DNA unwinding.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '28209641'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-0032297 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032297; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-0032297.raw | supports | GO:0032297: negative regulation of DNA-templated DNA replication initiation; obsolete=False; definition {'text': 'Any process that stops, prevents, or reduces the frequency, rate or extent of initiation of DNA-dependent DNA replication.'}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990077 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990077; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990077.raw | supports | GO:1990077: primosome complex; obsolete=False; definition {'text': 'Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '21856207'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990078 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990078; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990078.raw | supports | GO:1990078: replication inhibiting complex; obsolete=False; definition {'text': 'A protein complex that inhibits multiple events of replication initiation during one replication cycle.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '21708944'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990082-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990082/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990082-ancestors.raw | supports | Ancestors ['GO:1990078', 'GO:1990082', 'GO:0032991', 'GO:0005575']; children None. Exact parent classes checked without substituting parthood. |
| micro-go-1990082-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990082/constraints; Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990082-constraints.raw | context_only | Current taxonConstraints [{'ancestorId': 'GO:1990082', 'ancestorName': 'DnaA-L2 complex', 'relationship': 'only_in_taxon', 'taxId': '131567', 'taxIdType': 'NCBITaxon', 'taxName': 'cellular organisms'}]; this is ontology scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist rows are not used. |
| micro-go-1990082 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990082; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990082.raw | supports | GO:1990082: DnaA-L2 complex; obsolete=False; definition {'text': 'A protein complex that inhibits unwinding of DNA at the origin of replication and assembly of the pre-primosome. In E. coli, this complex is composed of DnaA and of the ribosomal protein L2.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '21288885'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990083-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990083-ancestors.raw | supports | Ancestors ['GO:1990078', 'GO:1990083', 'GO:0032991', 'GO:0005575']; children None. Exact parent classes checked without substituting parthood. |
| micro-go-1990083-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083/constraints; Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990083-constraints.raw | context_only | Current taxonConstraints [{'ancestorId': 'GO:1990083', 'ancestorName': 'DnaA-Hda complex', 'relationship': 'only_in_taxon', 'taxId': '131567', 'taxIdType': 'NCBITaxon', 'taxName': 'cellular organisms'}]; this is ontology scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist rows are not used. |
| micro-go-1990083 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990083.raw | supports | GO:1990083: DnaA-Hda complex; obsolete=False; definition {'text': 'A protein complex that inactivates the function of DnaA by inhibiting the phosphorylation of DnaA-ADP to DnaA-ATP and thereby preventing multiple events of replication initiation. In E. coli, this complex is composed of DnaA and Hda.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '21708944'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990084 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990084; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990084.raw | supports | GO:1990084: DnaA-Dps complex; obsolete=False; definition {'text': 'A protein complex that negatively regulates strand-opening at the origin of replication, thereby interfering with replication initiation. This complex is thought to be involved in the regulation of replication under oxidative stress conditions. In E. coli, this complex is composed of DnaA and Dps.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '18284581'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990085 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990085; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990085.raw | supports | GO:1990085: Hda-beta clamp complex; obsolete=False; definition {'text': 'A protein complex involved in inactivating the function of DnaA and thereby preventing multiple events of replication initiation. In E. coli, this complex is composed of the beta clamp (DnaN) and Hda.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '15150238'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990100 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990100; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990100.raw | supports | GO:1990100: DnaB-DnaC complex; obsolete=False; definition {'text': 'A protein complex containing homohexameric DNA helicase DnaB, and the DNA helicase loader DnaC. The helicase loader DnaC delivers DnaB to the chromosomal origin (oriC).', 'xrefs': [{'dbCode': 'PMID', 'dbId': '20129058'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990101-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990101-ancestors.raw | supports | Ancestors ['GO:1990101', 'GO:0032993', 'GO:0032991', 'GO:0005575', 'GO:1990077']; children None. Exact parent classes checked without substituting parthood. |
| micro-go-1990101-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101/constraints; Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990101-constraints.raw | context_only | Current taxonConstraints [{'ancestorId': 'GO:1990101', 'ancestorName': 'DnaA-oriC complex', 'relationship': 'only_in_taxon', 'taxId': '2, 2157', 'taxIdType': 'NCBITaxon_Union', 'taxName': 'Prokaryota'}]; this is ontology scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist rows are not used. |
| micro-go-1990101 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990101.raw | supports | GO:1990101: DnaA-oriC complex; obsolete=False; definition {'text': 'A protein-DNA complex containing the initiator protein DnaA bound to high-affinity recognition sites in the unique origin of replication, oriC. DnaA-oriC binding is the first step in assembly of a bacterial pre-replicative complex (pre-RC) and is responsible for the timely initiation of replication once per cell cycle.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '19833870'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990102 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990102; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990102.raw | supports | GO:1990102: DnaA-DiaA complex; obsolete=False; definition {'text': 'A protein-DNA complex containing a tetramer of DiaA attached to multiple DnaA molecule bound to oriC DNA. Regulates timely initiation of chromosomal replication during the cell cycle by stimulating assembly of DnaA-oriC complexes, conformational changes in ATP-DnaA initiation complexes, and unwinding of oriC duplex DNA.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '15326179'}, {'dbCode': 'PMID', 'dbId': '17699754'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-go-1990103-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103/ancestors?relations=is_a; Complete explicit is_a-only ancestor response and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990103-ancestors.raw | supports | Ancestors ['GO:1990103', 'GO:0032993', 'GO:0032991', 'GO:0005575', 'GO:1990077']; children None. Exact parent classes checked without substituting parthood. |
| micro-go-1990103-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103/constraints; Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990103-constraints.raw | context_only | Current taxonConstraints [{'ancestorId': 'GO:1990103', 'ancestorName': 'DnaA-HU complex', 'relationship': 'only_in_taxon', 'taxId': '2, 2157', 'taxIdType': 'NCBITaxon_Union', 'taxName': 'Prokaryota'}]; this is ontology scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist rows are not used. |
| micro-go-1990103 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103; Exact active identity/definition/synonyms and typed children; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990103.raw | supports | GO:1990103: DnaA-HU complex; obsolete=False; definition {'text': 'A protein-DNA complex containing DNA-bound DnaA attached to HU. HU is a dimer encoded by two closely related genes. Essential for the initiation of replication in bacteria; stimulates the DnaA-dependent unwinding of oriC.', 'xrefs': [{'dbCode': 'PMID', 'dbId': '18179598'}]}. Native wording is tested against primary scope, not treated as infallible experiment evidence. |
| micro-ipr-IPR001957 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/; Complete native name/type/hierarchy/integrated signatures/description flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR001957.raw | supports | IPR001957: {'name': 'Chromosomal replication control, initiator DnaA', 'short': 'Chromosome_initiator_DnaA'}; type family; signatures {'hamap': {'MF_00377': 'Chromosomal replication initiator protein DnaA [dnaA]'}, 'ncbifam': {'TIGR00362': 'chromosomal replication initiator protein DnaA'}}. Native whole-family type, integrated signatures, hierarchy and description inspected; separate maintained-example xrefs independently corroborate scope. No domain or homologous-superfamily substitution. |
| micro-ipr-IPR017788 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/; Complete native name/type/hierarchy/integrated signatures/description flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR017788.raw | supports | IPR017788: {'name': 'DnaA regulatory inactivator Hda', 'short': 'Hda'}; type family; signatures {'ncbifam': {'TIGR03420': 'DnaA regulatory inactivator Hda'}}. Native whole-family type, integrated signatures, hierarchy and description inspected; separate maintained-example xrefs independently corroborate scope. No domain or homologous-superfamily substitution. |
| micro-ipr-IPR022864 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/; Complete native name/type/hierarchy/integrated signatures/description flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR022864.raw | supports | IPR022864: {'name': 'DnaA regulatory inactivator Hda, Enterobacteriaceae', 'short': 'Hda_Enterobact'}; type family; signatures {'hamap': {'MF_01158': 'DnaA regulatory inactivator Hda [hda]'}}. Native whole-family type, integrated signatures, hierarchy and description inspected; separate maintained-example xrefs independently corroborate scope. No domain or homologous-superfamily substitution. Enterobacteriaceae Hda is narrower than generic Hda IPR017788. |
| micro-ipr-IPR005880 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005880/; Complete native name/type/hierarchy/integrated signatures/description flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR005880.raw | supports | IPR005880: {'name': 'Large ribosomal subunit protein uL2, bacteria/organella', 'short': 'Ribosomal_uL2_bact_org'}; type family; signatures {'hamap': {'MF_01320_B': 'Large ribosomal subunit protein uL2 [rplB]'}, 'ncbifam': {'TIGR01171': '50S ribosomal protein L2'}}. Native whole-family type, integrated signatures, hierarchy and description inspected; separate maintained-example xrefs independently corroborate scope. No domain or homologous-superfamily substitution. Bacterial/organellar uL2 class is narrower than universal uL2 IPR002171 and fits the declared 50S-L2 component. |
| micro-ipr-IPR002171-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002171/; Complete native name/type/hierarchy/integrated signatures/description flags; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR002171-retry.raw | supports | IPR002171: {'name': 'Large ribosomal subunit protein uL2', 'short': 'Ribosomal_uL2'}; type family; signatures {'pirsf': {'PIRSF002158': 'Ribosomal protein, L2p/L2a/L8e/organellar L2 types'}, 'panther': {'PTHR13691': 'RIBOSOMAL PROTEIN L2'}}. Native whole-family type, integrated signatures, hierarchy and description inspected; separate maintained-example xrefs independently corroborate scope. No domain or homologous-superfamily substitution. Universal parent has distinct bacteria/organella and archaea/eukaryota child families. Broader parent is not silently substituted for the explicit bacterial/organellar class. |
| micro-so-0000953 | https://www.ebi.ac.uk/ols4/api/ontologies/so/terms?obo_id=SO%3A0000953; Complete exact OLS term identity/definition/obsolete flag; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/so-0000953.raw | supports | Active oriC feature class: an origin of bacterial chromosome replication. Exact source-neutral scaffold class, not a single strain origin sequence. |
| micro-pmid-12618445 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12618445%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-12618445.raw | supports | 12618445: Identification of a novel membrane-associated gene product that suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship to the DnaA host initiation protein.; DOI 10.1128/jb.185.6.1817-1824.2003. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-15150238 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15150238%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-15150238.raw | supports | 15150238: Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related protein.; DOI 10.1128/jb.186.11.3508-3515.2004. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-18179598 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18179598%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-18179598.raw | supports | 18179598: Escherichia coli DnaA interacts with HU in initiation at the E. coli replication origin.; DOI 10.1111/j.1365-2958.2007.06094.x. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-19833870 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:19833870%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-19833870.raw | supports | 19833870: Bacterial origin recognition complexes direct assembly of higher-order DnaA oligomeric structures.; DOI 10.1073/pnas.0909472106. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-21288885 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21288885%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-21288885.raw | supports | 21288885: Two forms of ribosomal protein L2 of Escherichia coli that inhibit DnaA in DNA replication.; DOI 10.1093/nar/gkq1203. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-21708944 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21708944%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-21708944.raw | supports | 21708944: DnaA protein DNA-binding domain binds to Hda protein to promote inter-AAA+ domain interaction involved in regulatory inactivation of DnaA.; DOI 10.1074/jbc.m111.233403. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-22574163 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22574163%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-22574163.raw | supports | 22574163: Association of the chromosome replication initiator DnaA with the Escherichia coli inner membrane in vivo: quantity and mode of binding.; DOI 10.1371/journal.pone.0036441. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-28166228 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:28166228%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-28166228.raw | supports | 28166228: Rapid turnover of DnaA at replication origin regions contributes to initiation control of DNA replication.; DOI 10.1371/journal.pgen.1006561. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-pmid-9478970 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9478970%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED metadata and deposited primary-study abstract; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-9478970.raw | supports | 9478970: Membrane-mediated release of nucleotide from an initiator of chromosomal replication, Escherichia coli DnaA, occurs with insertion of a distinct region of the protein into the lipid bilayer.; DOI 10.1074/jbc.273.9.5167. Complete primary abstract read; this response alone does not certify full methods, source strain, figure pixels or supplements. |
| micro-keyamura2011-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC3190739/; Genuine PMC3190739 HTML; complete Introduction/Experimental Procedures/Results/Discussion, Table1 and Fig1–7 text captions; extracted P20 strains, P23 staged RIDA, P26–27 contact assays, P37 Fig2, P45–49 pulldown/SPR, P54 DARS, P68–75 discussion; no pixels/supplements; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/keyamura2011-pmc.raw | supports | K12-derived strains and purified/reconstituted DNA-loaded-clamp/ADP-Hda system support DnaA-bound ATP hydrolysis to ADP, not phosphorylation inhibition. DARS reactivation uses exchange as cited background. Mutant contact/RIDA effects and weak clamp-free SPR support interaction; precise clamp-free kinetics were not measurable at tested concentrations. Proposed structural model is not a solved cocrystal; binary identity is distinct from full active RIDA machinery. |
| micro-chodavarapu2011-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3105425.1/PMC3105425.1.xml; Genuine PMC3105425 JATS; complete Introduction/Materials and Methods/Results/Discussion and Fig1–8 text captions; extracted P10/26 source strains, P20 binding, P22/54/57 prepriming, P44 unwinding, P46 ATP, P50 contact, P61/68 physiological limits; no pixels/supplements; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/chodavarapu2011-jats.raw | supports | Purified mature/truncated L2 contacts the DnaA N terminus and inhibits oriC unwinding and prepriming assembly in vitro; reduced retained DnaA/DnaB supports proposed oligomer destabilization, not a solved interface. tL2 preparation from DM700 is not synonymous with K12 reference accession. Physiological regulation remains proposed; tested tL2 in-vivo initiation assay was negative under its conditions, not universal disproval. |
| micro-miller2009-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2773971/; Genuine PMC2773971 HTML; complete Introduction/Results/Discussion/Methods and Fig1–6 text captions; extracted P21–37 affinity/mutant assembly assays, P48 strains, P52 DMS, P54 crosslink, P56 EMSA; no pixels/raw footprint reanalysis; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/miller2009-pmc.raw | supports | High-affinity oriC sites assist DnaA assembly at low-affinity sites in E.coli; P3478/W3110 and PC2 dnaCts contexts and purified proteins are distinguished. At elevated DnaA, weak-site filling can occur despite mutated high-affinity sites. Crosslinks/footprints and model support bounded seeding/oligomerization, not a universal absence or exact stoichiometric claim. |
| micro-keyamura2011-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC3190739.1/PMC3190739.1.xml; Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/keyamura2011-jats.raw | context_only | HTTP404 diagnostic only. No blocked body or unavailable authority metadata certified; separate successful body/authority or complete abstract is explicitly identified. |
| micro-miller2009-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC2773971.1/PMC2773971.1.xml; Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/miller2009-jats.raw | context_only | HTTP404 diagnostic only. No blocked body or unavailable authority metadata certified; separate successful body/authority or complete abstract is explicitly identified. |
| micro-chodavarapu2008-publisher-access | https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2007.06094.x; Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/chodavarapu2008-publisher.raw | context_only | HTTP403 diagnostic only. No blocked body or unavailable authority metadata certified; separate successful body/authority or complete abstract is explicitly identified. |
| micro-chodavarapu2008-pdf-access | https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1365-2958.2007.06094.x; Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/chodavarapu2008-pdf.raw | context_only | HTTP403 diagnostic only. No blocked body or unavailable authority metadata certified; separate successful body/authority or complete abstract is explicitly identified. |
| micro-ipr-IPR002171-access | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002171/; Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR002171.raw | context_only | HTTP429 diagnostic only. No blocked body or unavailable authority metadata certified; separate successful body/authority or complete abstract is explicitly identified. |
| micro-historical-0-keyamura2011-legacy-access | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3190739/; Retained failed/challenge route | context_only | Legacy HTTP200 returned a reCAPTCHA challenge, not the paper. Historical original-observation time/hash retained, not freshly fetched or claimed as a renewed raw-response read. Original honestly admitted access limitations; successor corrects classification only to validation/context_only. |
| micro-historical-0-keyamura2011-xml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3190739/fullTextXML; Retained failed/challenge route | context_only | EuropePMC fullTextXML route returned500; the separate modern PMC HTML supplied the genuine body. Historical original-observation time/hash retained, not freshly fetched or claimed as a renewed raw-response read. Original honestly admitted access limitations; successor corrects classification only to validation/context_only. |
| micro-historical-1-chodavarapu2008-publisher-access | https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2007.06094.x; Retained publisher403 response | context_only | Publisher route did not provide the article body; the complete native abstract was read. Historical original-observation time/hash retained, not freshly fetched or claimed as a renewed raw-response read. Original honestly admitted access limitations; successor corrects classification only to validation/context_only. |
| micro-historical-1-chodavarapu2008-pdf-access | https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1365-2958.2007.06094.x; Retained publisher403 response | context_only | Publisher route did not provide the article body; the complete native abstract was read. Historical original-observation time/hash retained, not freshly fetched or claimed as a renewed raw-response read. Original honestly admitted access limitations; successor corrects classification only to validation/context_only. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official20-organism catalogue and every returned dataset entry; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/catalogue.raw | supports | E.coli has actual precise1k coverage among listed datasets. This is bounded current catalogue scope, not universal or future coverage. |
| micro-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete selected precise1k metadata and five-strain list; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-meta.raw | context_only | Dataset contains BW25113,DGF-298,GMOS,MG1655,W3110;1035 samples,518 conditions,201 modules,4257 genes. Mixed K12-related strains are not identical to every Keyamura mutant, DM700 preparation or Miller assay strain; source-specific experiments remain independently scoped. |
| micro-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 returned module names/regulators/functions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-modules.raw | context_only | Complete selected module inventory inspected; computational labels do not demonstrate direct regulation or physical complex formation. |
| micro-ecoli-gene-b3702 | https://imodulondb.org/api/genes/b3702/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b3702.raw | context_only | b3702: []. Zero thresholded memberships do not mean absence or dispensability; a positive expression module does not prove binding, assembly or direct regulation. |
| micro-ecoli-gene-b2496 | https://imodulondb.org/api/genes/b2496/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b2496.raw | context_only | b2496: []. Zero thresholded memberships do not mean absence or dispensability; a positive expression module does not prove binding, assembly or direct regulation. |
| micro-ecoli-gene-b3317 | https://imodulondb.org/api/genes/b3317/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b3317.raw | context_only | b3317: [{"k": 1, "name": "Translation", "weight": 0.130149946, "threshold": 0.057970804, "in_imodulon": true}]. Zero thresholded memberships do not mean absence or dispensability; a positive expression module does not prove binding, assembly or direct regulation. |
| micro-ecoli-gene-b4000 | https://imodulondb.org/api/genes/b4000/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b4000.raw | context_only | b4000: []. Zero thresholded memberships do not mean absence or dispensability; a positive expression module does not prove binding, assembly or direct regulation. |
| micro-ecoli-gene-b0440 | https://imodulondb.org/api/genes/b0440/imodulons?organism=e_coli&amp;dataset=precise1k; All201 exact-native-locus membership/weight/threshold rows; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b0440.raw | context_only | b0440: []. Zero thresholded memberships do not mean absence or dispensability; a positive expression module does not prove binding, assembly or direct regulation. |
| micro-adapter-module1 | https://imodulondb.org/api/imodulons/e_coli/precise1k/1; Independently read same-PR response: actual metadata,53-gene IDs/weights and complete member identity columns; rplB full row. AI summary/activity fields excluded. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1.raw | context_only | Module1 Translation/DksA, ribosome-biogenesis annotation; rplB b3317/P60422 weight0.130149946 exceeds threshold0.057970804 in complete53-member list. Five-strain computational context only, not DnaA-L2 assembly or direct DksA regulation evidence. Reused actual fetch timestamp, not a new request. |
| micro-adapter-module1-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/1/genes; Independently read same-PR response: actual metadata,53-gene IDs/weights and complete member identity columns; rplB full row. AI summary/activity fields excluded. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1-genes.raw | context_only | Module1 Translation/DksA, ribosome-biogenesis annotation; rplB b3317/P60422 weight0.130149946 exceeds threshold0.057970804 in complete53-member list. Five-strain computational context only, not DnaA-L2 assembly or direct DksA regulation evidence. Reused actual fetch timestamp, not a new request. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z receipt | context_only | Historical runner unavailable/exit1 permission limitation; no fresh invocation. Current official API catalogue/gene/module fallback is separately documented. |
| micro-native-dnaa_hda_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_hda_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-causal.log SHA256 c1b02a106da2af87da59359f83b31b146fdd3ba83f7f8364b563ee0084a53520 | supports | Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_hu_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes; HU dimer STRUCTURE node and oriC GENETIC_ELEMENT are outside this typed-protein inventory and checked independently. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_hu_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-causal.log SHA256 ca286fe8a9cd7bb445c53da08a7fb8bc6512f82af088da76999eb9dbc8fc6787 | supports | Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes; HU dimer STRUCTURE node and oriC GENETIC_ELEMENT are outside this typed-protein inventory and checked independently. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_l2_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_l2_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-causal.log SHA256 b5af99c8180d083ab55ba1f343531d77f1fddc4e7b84189669a4457b4b36d46a | supports | Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_oric_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-verify-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes; oriC GENETIC_ELEMENT is checked independently. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| micro-native-dnaa_oric_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-causal-receipt.json; Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-causal.log SHA256 13807089fc975c18288a1f1c653e3484de53f3588a33d875dda00c8ba20e577e | supports | Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes; oriC GENETIC_ELEMENT is checked independently. This validates implemented identity/xref coverage, not exact family grounding or full biological completeness. |
| plaque-curation | docs/CURATION.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-protein-skill | .claude/skills/uniprot-protein-examples/SKILL.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-graph-skill | .claude/skills/curate-causal-graphs/SKILL.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-review-profile | docs/record-review-profile.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-review-contract | docs/record-reviews.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-review-schema | schema/record_review.yaml; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-structure-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-agents | AGENTS.md; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-review-config | conf/record_review.yaml; Current frozen policy/schema; relevant component-class, evidence, source applicability, graph, history and review-contract sections | context_only | Native review and modelling rules; historical rationale is append-only, formation is distinct from viability, optional inventory is not mandatory, and expression data are context rather than assembly proof. |
| plaque-record-4 | data/structures/other/dnab_dnac_complex.yaml; Complete maintained record including every component, example, graph, discussion and history entry | supports | Whole current record independently read; same SHA-256 as the original review target input, without staleness or scientific edits. |
| plaque-original-4-yaml | reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.yaml; Complete immutable original; source, checks, scientific assessments, findings, actions, limits and notes | context_only | Original historical review; its claims and frozen inputs were independently checked. This observation does not treat historical commands as newly executed. |
| plaque-original-4-md | reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.md; Complete immutable original; source, checks, scientific assessments, findings, actions, limits and notes | context_only | Original historical review; its claims and frozen inputs were independently checked. This observation does not treat historical commands as newly executed. |
| plaque-record-5 | data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml; Complete maintained record including every component, example, graph, discussion and history entry | supports | Whole current record independently read; same SHA-256 as the original review target input, without staleness or scientific edits. |
| plaque-original-5-yaml | reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.yaml; Complete immutable original; source, checks, scientific assessments, findings, actions, limits and notes | context_only | Original historical review; its claims and frozen inputs were independently checked. This observation does not treat historical commands as newly executed. |
| plaque-original-5-md | reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.md; Complete immutable original; source, checks, scientific assessments, findings, actions, limits and notes | context_only | Original historical review; its claims and frozen inputs were independently checked. This observation does not treat historical commands as newly executed. |
| plaque-record-6 | data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml; Complete maintained record including every component, example, graph, discussion and history entry | supports | Whole current record independently read; same SHA-256 as the original review target input, without staleness or scientific edits. |
| plaque-original-6-yaml | reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.yaml; Complete immutable original; source, checks, scientific assessments, findings, actions, limits and notes | context_only | Original historical review; its claims and frozen inputs were independently checked. This observation does not treat historical commands as newly executed. |
| plaque-original-6-md | reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.md; Complete immutable original; source, checks, scientific assessments, findings, actions, limits and notes | context_only | Original historical review; its claims and frozen inputs were independently checked. This observation does not treat historical commands as newly executed. |
| plaque-input-original-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/input-original-proof.json; 47 current source/worktree hashes; 41 historical input occurrences; three original native validations and exact Markdown render comparisons | supports | All 47 frozen current inputs match source and working tree. All 41 historical input occurrences match their original Git revisions. Three original pairs validate and render exactly; assigned targets are unchanged. |
| plaque-native-dnab_dnac_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-verify-receipt.json; Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-verify.log; log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit 0. Current record contains 2 reviewed protein examples and 2 GENE_OR_PROTEIN nodes, all COVERED in the causal log. The verify log confirms identifier consistency, not independent assembly or source-stage support. |
| plaque-native-dnab_dnac_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-causal-receipt.json; Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-causal.log; log SHA256 1a5fd2b44858b3af069fb75cc2842754b9f929dcbcc7335cc4034fd26fcf138e | supports | Exit 0. Current record contains 2 reviewed protein examples and 2 GENE_OR_PROTEIN nodes, all COVERED in the causal log. The verify log confirms identifier consistency, not independent assembly or source-stage support. |
| plaque-native-dnab_dnac_dnat_pria_prib_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-verify-receipt.json; Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-verify.log; log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN nodes, all COVERED in the causal log. The verify log confirms identifier consistency, not independent assembly or source-stage support. |
| plaque-native-dnab_dnac_dnat_pria_prib_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-causal-receipt.json; Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-causal.log; log SHA256 da3be8302e150b5f1f300995c5bc908eaf804b9ec237b319e4ed1e1937955d35 | supports | Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN nodes, all COVERED in the causal log. The verify log confirms identifier consistency, not independent assembly or source-stage support. |
| plaque-native-dnab_dnac_dnat_pria_pric_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-verify-receipt.json; Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-verify.log; log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN nodes, all COVERED in the causal log. The verify log confirms identifier consistency, not independent assembly or source-stage support. |
| plaque-native-dnab_dnac_dnat_pria_pric_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-causal-receipt.json; Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-causal.log; log SHA256 a61be5ffd377d729d7aee4e31668d88690314dce25c4496b9f83c9d4636e782c | supports | Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN nodes, all COVERED in the causal log. The verify log confirms identifier consistency, not independent assembly or source-stage support. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100,GO:1990158,GO:1990159,GO:1990099,GO:0032991,GO:0006270,GO:0031297,GO:1990160,GO:1990077; Full nine-term response; exact definitions/synonyms and typed children/relations for GO1990100, GO1990158, GO1990159, GO1990099, GO0032991, GO0006270, GO0031297, GO1990160 and GO1990077; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go.raw | supports | Current active GO identities and definitions support the intended three classes, distinct loader versus preprimosome hierarchy, and native function terms. Correct ontology quotation does not resolve conflict with experimentally isolated composition. |
| plaque-go-1990100-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/ancestors?relations=is_a; Exact is_a ancestor result for GO:1990100; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990100-ancestors.raw | supports | Current is-a ancestor response confirms class hierarchy without converting ancestry into direct experimental parthood. |
| plaque-go-1990100-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/constraints; Exact taxon-constraint response for GO:1990100; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990100-constraints.raw | supports | Current taxon constraint is an ontology scope condition, not prevalence evidence or a verified experimental archaeal example. |
| plaque-go-1990158-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/ancestors?relations=is_a; Exact is_a ancestor result for GO:1990158; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990158-ancestors.raw | supports | Current is-a ancestor response confirms class hierarchy without converting ancestry into direct experimental parthood. |
| plaque-go-1990158-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/constraints; Exact taxon-constraint response for GO:1990158; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990158-constraints.raw | supports | Current taxon constraint is an ontology scope condition, not prevalence evidence or a verified experimental archaeal example. |
| plaque-go-1990159-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990159/ancestors?relations=is_a; Exact is_a ancestor result for GO:1990159; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990159-ancestors.raw | supports | Current is-a ancestor response confirms class hierarchy without converting ancestry into direct experimental parthood. |
| plaque-go-1990159-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990159/constraints; Exact taxon-constraint response for GO:1990159; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990159-constraints.raw | supports | Current taxon constraint is an ontology scope condition, not prevalence evidence or a verified experimental archaeal example. |
| plaque-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Full ENA taxonomy XML identity/rank/lineage, taxon 562; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/tax-562.raw | supports | Current authority identifies Escherichia coli species and its K-12 strain taxon separately; neither proves an unspecified experimental derivative is precisely the reference strain. |
| plaque-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Full ENA taxonomy XML identity/rank/lineage, taxon 83333; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/tax-83333.raw | supports | Current authority identifies Escherichia coli species and its K-12 strain taxon separately; neither proves an unspecified experimental derivative is precisely the reference strain. |
| plaque-pmid-20129058 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20129058+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED PMID query, pageSize=1/resultType=core; complete abstract and bibliography only; no full body inferred from this response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/pmid-20129058.raw | supports | Complete primary abstract and metadata identify Makowska-Grzyska and Kaguni 2010, DnaC delivery/release experiments and exact DOI. |
| plaque-pmid-8663104 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663104+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED PMID query, pageSize=1/resultType=core; complete abstract and bibliography only; no full body inferred from this response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/pmid-8663104.raw | supports | Complete primary abstract identifies the short PAS-substrate assembly: retained PriA/PriB/DnaT/DnaB, with DnaC not part of the final complex. The indexed erratum and full article body were not inspected. |
| plaque-pmid-8663105 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Europe PMC exact MED PMID query, pageSize=1/resultType=core; complete abstract and bibliography only; no full body inferred from this response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/pmid-8663105.raw | supports | Complete primary abstract identifies intact PhiX174 template experiments retaining PriA/PriB/PriC/DnaT/DnaB, no stable DnaC, and proposed repair/restart relevance. |
| plaque-makowska2010-body | https://pmc.ncbi.nlm.nih.gov/articles/instance/2819048/; Genuine PMC article; Results S8–S10, Discussion S14–S16 and Experimental Procedures S18/S20/S21, with captions for Figures 5–7. No figure pixels, raw measurements, or supplementary strain Table S1 inspected.; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/makowska2010-body.raw | supports | Primary results distinguish DnaC-dependent helicase delivery, DnaC retention before priming, and primase/rNTP-associated release. The approximately three-loader-per-hexamer interpretation in the measured oriC complex does not make every DnaB-DnaC assembly invariant. Mutant delivery without successful initiation separates presence from function. |
| plaque-ng1996ii-pdf | https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf; Genuine JBC PDF pp15649–15654: main Results/Discussion/Methods, Table I and figure captions 1–9, especially pp15653–15654; text extracted with pdftotext. No figure-pixel or Western reanalysis; bibliography is not independently read studies.; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ng1996ii-pdf.raw | supports | Primary full main text separates supplied loading factors from isolated products: intact PhiX174 complexes retain PriA, PriB, PriC, DnaT and DnaB; DnaC is not a stable constituent. PriC is retained here unlike short PAS substrates; repair/restart is a proposed extension rather than a directly measured repaired-fork outcome. |
| plaque-up-P0ACB0 | https://rest.uniprot.org/uniprotkb/P0ACB0.json; Native UniProt complete JSON: primaryAccession/entryType/organism/genes, ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P0ACB0.raw | supports | Reviewed exact K-12 taxon83333 entry P0ACB0 has primary gene dnaB and locus b4052. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION comments were checked; annotation alone is not experimental proof of the maintained complex. |
| plaque-gene-dnaB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned native results; exact organism node and reviewed filter; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-dnaB.raw | supports | The exact reviewed gene/taxon search returns one entry, P0ACB0, whose own gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy queries are outside this exact-organism result. |
| plaque-up-P0AEF0 | https://rest.uniprot.org/uniprotkb/P0AEF0.json; Native UniProt complete JSON: primaryAccession/entryType/organism/genes, ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P0AEF0.raw | supports | Reviewed exact K-12 taxon83333 entry P0AEF0 has primary gene dnaC and locus b4361. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION comments were checked; annotation alone is not experimental proof of the maintained complex. |
| plaque-gene-dnaC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned native results; exact organism node and reviewed filter; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-dnaC.raw | supports | The exact reviewed gene/taxon search returns one entry, P0AEF0, whose own gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy queries are outside this exact-organism result. |
| plaque-up-P0A8J2 | https://rest.uniprot.org/uniprotkb/P0A8J2.json; Native UniProt complete JSON: primaryAccession/entryType/organism/genes, ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P0A8J2.raw | supports | Reviewed exact K-12 taxon83333 entry P0A8J2 has primary gene dnaT and locus b4362. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION comments were checked; annotation alone is not experimental proof of the maintained complex. |
| plaque-gene-dnaT | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned native results; exact organism node and reviewed filter; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-dnaT.raw | supports | The exact reviewed gene/taxon search returns one entry, P0A8J2, whose own gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy queries are outside this exact-organism result. |
| plaque-up-P17888 | https://rest.uniprot.org/uniprotkb/P17888.json; Native UniProt complete JSON: primaryAccession/entryType/organism/genes, ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P17888.raw | supports | Reviewed exact K-12 taxon83333 entry P17888 has primary gene priA and locus b3935. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION comments were checked; annotation alone is not experimental proof of the maintained complex. |
| plaque-gene-priA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned native results; exact organism node and reviewed filter; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-priA.raw | supports | The exact reviewed gene/taxon search returns one entry, P17888, whose own gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy queries are outside this exact-organism result. |
| plaque-up-P07013 | https://rest.uniprot.org/uniprotkb/P07013.json; Native UniProt complete JSON: primaryAccession/entryType/organism/genes, ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P07013.raw | supports | Reviewed exact K-12 taxon83333 entry P07013 has primary gene priB and locus b4201. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION comments were checked; annotation alone is not experimental proof of the maintained complex. |
| plaque-gene-priB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned native results; exact organism node and reviewed filter; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-priB.raw | supports | The exact reviewed gene/taxon search returns one entry, P07013, whose own gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy queries are outside this exact-organism result. |
| plaque-up-P23862 | https://rest.uniprot.org/uniprotkb/P23862.json; Native UniProt complete JSON: primaryAccession/entryType/organism/genes, ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P23862.raw | supports | Reviewed exact K-12 taxon83333 entry P23862 has primary gene priC and locus b0467. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION comments were checked; annotation alone is not experimental proof of the maintained complex. |
| plaque-gene-priC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All returned native results; exact organism node and reviewed filter; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-priC.raw | supports | The exact reviewed gene/taxon search returns one entry, P23862, whose own gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy queries are outside this exact-organism result. |
| plaque-ipr-IPR007692 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR007692.raw | supports | DnaB-type helicase family, distinct from its individual domains; native DnaB entry cross-reference independently agrees. |
| plaque-ncbifam-NF005931 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF005931/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ncbifam-NF005931.raw | supports | Exact unintegrated NCBIfam DnaC replicative helicase loader family; native DnaC cross-reference agrees. |
| plaque-ipr-IPR028350 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028350/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR028350.raw | supports | Broader DnaC/IstB homolog family includes a paralogous class and is not the proposed exact DnaC grounding. |
| plaque-ipr-IPR020917 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020917/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR020917.raw | supports | Exact DnaT/primosomal protein 1 family, with natural proteobacterial scope; not its narrower C-terminal domain. |
| plaque-ipr-IPR005259 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005259/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR005259.raw | supports | Exact full PriA family, distinct from generic helicase/ATPase domains. |
| plaque-ipr-IPR023646 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023646/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR023646.raw | supports | Exact PriB family below broader PriB/SSB; native PriB cross-reference independently agrees. |
| plaque-ipr-IPR010890 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/; Full current InterPro/NCBIfam native metadata: accession/name/type, native non-LLM description, integration/hierarchy and member signatures; independently cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR010890.raw | supports | Exact PriC family, distinct from its broader structural superfamily; native PriC cross-reference agrees. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Fresh same-PR public API response fetched by independent micro reviewer, independently reread here; exact retrieval timestamp retained; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/catalogue.raw | context_only | Complete current catalogue contains E. coli and precise1k; an applicable host/dataset exists for the represented molecular records. |
| plaque-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Fresh same-PR public API response fetched by independent micro reviewer, independently reread here; exact retrieval timestamp retained; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-meta.raw | context_only | precise1k metadata lists BW25113, DGF-298, GMOS, MG1655 and W3110; 201 modules, 4257 genes and 1035 samples. This is a five-strain dataset, not proof of exact experimental strain equivalence. |
| plaque-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Fresh same-PR public API response fetched by independent micro reviewer, independently reread here; exact retrieval timestamp retained; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-modules.raw | context_only | Complete 201-module list was inspected for the bounded matched-locus context. No generated explanatory prose is used as evidence. |
| plaque-adapter-b4052-gene | https://imodulondb.org/api/genes/b4052?organism=e_coli&amp;dataset=precise1k; Full exact gene response; primary identity/locus/product and source organism/dataset fields; embedded annotations not treated as independently reviewed primary papers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4052-gene.raw | context_only | Exact precise1k native gene record identifies dnaB/b4052, UniProt P0ACB0, and MG1655 coordinate STRING511145.b4052; this does not turn the multi-strain dataset into one experimental strain. |
| plaque-adapter-b4052-modules | https://imodulondb.org/api/genes/b4052/imodulons?organism=e_coli&amp;dataset=precise1k; Exact locus membership response restricted to e_coli/precise1k; all201 returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4052-modules.raw | context_only | No true membership flag among all 201 returned module rows. This threshold result does not establish biological absence, nonfunction or lack of physical assembly. |
| plaque-adapter-b4361-gene | https://imodulondb.org/api/genes/b4361?organism=e_coli&amp;dataset=precise1k; Full exact gene response; primary identity/locus/product and source organism/dataset fields; embedded annotations not treated as independently reviewed primary papers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4361-gene.raw | context_only | Exact precise1k native gene record identifies dnaC/b4361, UniProt P0AEF0, and MG1655 coordinate STRING511145.b4361; this does not turn the multi-strain dataset into one experimental strain. |
| plaque-adapter-b4361-modules | https://imodulondb.org/api/genes/b4361/imodulons?organism=e_coli&amp;dataset=precise1k; Exact locus membership response restricted to e_coli/precise1k; all201 returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4361-modules.raw | context_only | No true membership flag among all 201 returned module rows. This threshold result does not establish biological absence, nonfunction or lack of physical assembly. |
| plaque-adapter-b4362-gene | https://imodulondb.org/api/genes/b4362?organism=e_coli&amp;dataset=precise1k; Full exact gene response; primary identity/locus/product and source organism/dataset fields; embedded annotations not treated as independently reviewed primary papers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4362-gene.raw | context_only | Exact precise1k native gene record identifies dnaT/b4362, UniProt P0A8J2, and MG1655 coordinate STRING511145.b4362; this does not turn the multi-strain dataset into one experimental strain. |
| plaque-adapter-b4362-modules | https://imodulondb.org/api/genes/b4362/imodulons?organism=e_coli&amp;dataset=precise1k; Exact locus membership response restricted to e_coli/precise1k; all201 returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4362-modules.raw | context_only | No true membership flag among all 201 returned module rows. This threshold result does not establish biological absence, nonfunction or lack of physical assembly. |
| plaque-adapter-b3935-gene | https://imodulondb.org/api/genes/b3935?organism=e_coli&amp;dataset=precise1k; Full exact gene response; primary identity/locus/product and source organism/dataset fields; embedded annotations not treated as independently reviewed primary papers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b3935-gene.raw | context_only | Exact precise1k native gene record identifies priA/b3935, UniProt P17888, and MG1655 coordinate STRING511145.b3935; this does not turn the multi-strain dataset into one experimental strain. |
| plaque-adapter-b3935-modules | https://imodulondb.org/api/genes/b3935/imodulons?organism=e_coli&amp;dataset=precise1k; Exact locus membership response restricted to e_coli/precise1k; all201 returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b3935-modules.raw | context_only | No true membership flag among all 201 returned module rows. This threshold result does not establish biological absence, nonfunction or lack of physical assembly. |
| plaque-adapter-b4201-gene | https://imodulondb.org/api/genes/b4201?organism=e_coli&amp;dataset=precise1k; Full exact gene response; primary identity/locus/product and source organism/dataset fields; embedded annotations not treated as independently reviewed primary papers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4201-gene.raw | context_only | Exact precise1k native gene record identifies priB/b4201, UniProt P07013, and MG1655 coordinate STRING511145.b4201; this does not turn the multi-strain dataset into one experimental strain. |
| plaque-adapter-b4201-modules | https://imodulondb.org/api/genes/b4201/imodulons?organism=e_coli&amp;dataset=precise1k; Exact locus membership response restricted to e_coli/precise1k; all201 returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4201-modules.raw | context_only | One true flag among all 201 module rows: k1 Translation, weight0.099397177 &gt; threshold0.057970804. This is computational expression membership, not preprimosome membership. |
| plaque-adapter-b0467-gene | https://imodulondb.org/api/genes/b0467?organism=e_coli&amp;dataset=precise1k; Full exact gene response; primary identity/locus/product and source organism/dataset fields; embedded annotations not treated as independently reviewed primary papers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b0467-gene.raw | context_only | Exact precise1k native gene record identifies priC/b0467, UniProt P23862, and MG1655 coordinate STRING511145.b0467; this does not turn the multi-strain dataset into one experimental strain. |
| plaque-adapter-b0467-modules | https://imodulondb.org/api/genes/b0467/imodulons?organism=e_coli&amp;dataset=precise1k; Exact locus membership response restricted to e_coli/precise1k; all201 returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b0467-modules.raw | context_only | No true membership flag among all 201 returned module rows. This threshold result does not establish biological absence, nonfunction or lack of physical assembly. |
| plaque-adapter-module1 | https://imodulondb.org/api/imodulons/e_coli/precise1k/1; e_coli/precise1k/k1 native metadata and complete53 member-weight entries only; generated summary and its model metadata excluded; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1.raw | context_only | Exact k1 Translation metadata identifies DksA annotation and 53 gene-weight entries including priB. Generated ai_summary fields were excluded from all judgments. |
| plaque-adapter-module1-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/1/genes; Full53-row native member table; exact priB identity/weight/threshold row and row-count reconciliation with module metadata; embedded UniProt prose not treated as newly inspected publications; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1-genes.raw | context_only | All53 distinct returned member rows are true; priB/b4201/P07013 has weight0.099397177 against threshold0.057970804. This corroborates only transcriptomic membership and does not support physical association with translation machinery or assembly of the reviewed complexes. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record review and structured sources | supports | Positive protein/pathway claims require actual structured-source applicability; lack of an expression claim is insufficient. Official source fallback may be used with actual coverage and runner limits. |
| septin-curation-policy | docs/CURATION.md; Component identities and Discussions | supports | Verified exact full families differ from protein examples; historical rationale is append-only. Essentiality concerns formation, not catalytic function or viability. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component, protein-example, formation and causal-graph contracts | supports | Classes and appropriate complexes are permitted. No optional-example or enum-only finding is manufactured; experimental membership and formation necessity are distinct. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Primary gene names, ambiguity, native verification and manual curation | supports | Automatic ambiguous-query seeding must abstain; correct manual accession selection can use actual protein identity. Current alias-inclusive query ambiguity does not reconstruct an unspecified historical query. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Nonmechanistic scope and endpoints | supports | Membership, staged loading, catalytic output and universal formation necessity are distinct claims. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Actual access scopes | supports | Primary body, primary abstract, authority metadata and failed access are distinct tiers. No unseen figure pixels or supplements are certified. |
| septin-review-schema | schema/record_review.yaml; FindingStatus and FindingReference | supports | Rejected is a supported native terminal disposition with exact previous occurrence; inherited rejected findings do not require record-curation actions. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003678,GO:0006269,GO:0031297,GO:0033202,GO:1990098,GO:1990099,GO:1990100,GO:1990156,GO:1990158,GO:1990159,GO:1990160,GO:1990161; All12 requested exact terms: labels, active status, definitions, synonyms, xrefs and relevant typed children | supports | GO1990160 is the DnaB-DnaC-Rep-PriC protein-DNA pre-primosome, distinct from PriA/PriB and PriA/PriC alternatives; pre-primosomes lack primase. GO1990156 is DnaB-DnaG and explicitly part_of GO1990098; GO1990161 is the DnaB hexamer. Both latter classes are is_a DNA-helicase complex. Native broad Prokaryotes wording is not extended into an untested archaeal mechanism. |
| septin-ipr-IPR005752 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005752/; Native name/type, signatures, hierarchy and description provenance; no sequence alignment performed | supports | Exact Rep family supported by MF01920/TIGR01074 and independently mapped P09980; broad UvrD-like parent and PcrA/UvrD siblings are not substitutes. Its erroneous hexamer sentence is excluded from biological support; native P09980 reports DNA-associated homodimer. |
| septin-ipr-IPR010890 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/; Native name/type, signatures, hierarchy and description provenance; no sequence alignment performed | supports | Exact PriC family, PF07445, with independent native P23862 membership. |
| septin-ipr-IPR007692 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/; Native name/type, signatures, hierarchy and description provenance; no sequence alignment performed | supports | Full DnaB-type helicase family, TIGR00665, with P0ACB0 and Q9X4C9 membership; not merely a domain or broad ATPase fold. |
| septin-ipr-IPR030846 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030846/; Native name/type, signatures, hierarchy and description provenance; no sequence alignment performed | supports | Bacterial DnaG full-family identity, HAMAP MF00974/PIRSF002811, independently mapped by P0ABS5. |
| septin-retry-IPR006295 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006295/; Native name/type, signatures, hierarchy and description provenance; no sequence alignment performed | supports | Native type is domain: DNA primase bacterial core does not denote the complete DnaG protein. |
| septin-retry-IPR050219 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050219/; Native name/type, signatures, hierarchy and description provenance; no sequence alignment performed | supports | Broader Panther family metadata is inspected; llm=true/checked=false description is excluded from biological support, including archaeal/exosome prose. |
| septin-up-P09980 | https://rest.uniprot.org/uniprotkb/P09980.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed P09980: ATP-dependent DNA helicase Rep; primary gene rep; taxon83333; loci b3778, JW5604. Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. |
| septin-up-P23862 | https://rest.uniprot.org/uniprotkb/P23862.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed P23862: Replication restart protein PriC; primary gene priC; taxon83333; loci b0467, JW0456. Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. |
| septin-up-P0ACB0 | https://rest.uniprot.org/uniprotkb/P0ACB0.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed P0ACB0: Replicative DNA helicase DnaB; primary gene dnaB; taxon83333; loci b4052, JW4012. Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. |
| septin-up-P0ABS5 | https://rest.uniprot.org/uniprotkb/P0ABS5.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed P0ABS5: DNA primase; primary gene dnaG; taxon83333; loci b3066, JW3038. Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. |
| septin-up-Q9X4C9 | https://rest.uniprot.org/uniprotkb/Q9X4C9.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed Q9X4C9: Replicative DNA helicase DnaB; primary gene dnaB; taxon1422; loci . Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. Biological Geobacillus source remains distinct from recombinant E.coli BL21(DE3). |
| septin-up-P03856 | https://rest.uniprot.org/uniprotkb/P03856.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed P03856: Replication initiation protein; primary gene repE; taxon83333; loci ECOK12F045. Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. RepE has synonym rep and is not Rep helicase; this explains current alias-inclusive query ambiguity without disproving the maintained P09980 selection. |
| septin-up-P0AEF0 | https://rest.uniprot.org/uniprotkb/P0AEF0.json; Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence; family xrefs | supports | Reviewed P0AEF0: Replicative helicase loader DnaC; primary gene dnaC; taxon83333; loci b4361, JW4325. Native function/subunit annotations and complete InterPro xrefs inspected; identity annotation is not a new independent assembly experiment. Named loading-subcomplex context only, not a mandatory missing example. |
| septin-query-rep-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arep%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity/primary gene/synonym/organism/status rows | supports | Current returned accessions P09980, P03856. Only P09980 is primary rep/Rep helicase; P03856 is primary repE with alias rep. Current search does not expose the earlier unstated endpoint or establish a historical error. |
| septin-query-priC-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity/primary gene/synonym/organism/status rows | supports | Current returned accessions P23862. Singleton supports current native reference-identity wording at this exact bounded query. |
| septin-query-dnaB-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity/primary gene/synonym/organism/status rows | supports | Current returned accessions P0ACB0. Singleton supports current native reference-identity wording at this exact bounded query. |
| septin-query-dnaG-83333 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity/primary gene/synonym/organism/status rows | supports | Current returned accessions P0ABS5. Singleton supports current native reference-identity wording at this exact bounded query. |
| septin-query-dnaB-1422 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28organism_id%3A1422%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity/primary gene/synonym/organism/status rows | supports | Current returned accessions Q9X4C9. Singleton supports current native reference-identity wording at this exact bounded query. |
| septin-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native ENA name/rank/synonyms/lineage response | supports | Taxon562 is Escherichia coli (species). Biological source and experimental expression strain are not interchangeable. |
| septin-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native ENA name/rank/synonyms/lineage response | supports | Taxon83333 is Escherichia coli K-12 (strain). Biological source and experimental expression strain are not interchangeable. |
| septin-tax-1422 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1422; Complete native ENA name/rank/synonyms/lineage response | supports | Taxon1422 is Geobacillus stearothermophilus (species). Biological source and experimental expression strain are not interchangeable. |
| septin-pmid-19941825 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19941825+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native complete CORE metadata and abstractText; no full-body inference from abstract | supports | Exact native title, authors, year and DOI checked; complete primary abstract read. Rep provides a second motor at the replisome to promote duplication of protein-bound DNA. DOI 10.1016/j.molcel.2009.11.009. |
| septin-pmid-8663105 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native complete CORE metadata and abstractText; no full-body inference from abstract | supports | Exact native title, authors, year and DOI checked; complete primary abstract read. The ordered assembly of the phiX174-type primosome. II. Preservation of primosome composition from assembly through replication. DOI 10.1074/jbc.271.26.15649. |
| septin-pmid-14557266 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14557266+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native complete CORE metadata and abstractText; no full-body inference from abstract | supports | Exact native title, authors, year and DOI checked; complete primary abstract read. Mechanism and stoichiometry of interaction of DnaG primase with DnaB helicase of Escherichia coli in RNA primer synthesis. DOI 10.1074/jbc.m308956200. Authors are Mitkova, Khopde and Biswas2003, not Tougu/Marians. Chemical crosslinking/gel filtration and anisotropy/Scatchard support three DnaG per DnaB hexamer in a stabilized E.coli complex; this is not invariant in-vivo stoichiometry or universal formation necessity. |
| septin-pmid-17947583 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17947583+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=1; Native complete CORE metadata and abstractText; no full-body inference from abstract | supports | Exact native title, authors, year and DOI checked; complete primary abstract read. Structure of hexameric DnaB helicase and its complex with a domain of DnaG primase. DOI 10.1126/science.1147353. DnaB-alone and DnaG-binding-domain structures are separate forms; full body unavailable on attempted publisher route. No supplementary experiment claim. |
| septin-guy2009-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2807033/; Genuine PMC2807033 HTML: Introduction sec1; Results sec2.1 and2.6 with Fig1/6/7 captions; all Discussion sec3 and Experimental Procedures sec4. Not Results2.2–2.5 in full; no supplementary TableS1 or pixels | supports | Primary assays examine oriC-initiated forks and add Rep after blockage; stated reaction includes DnaA/DnaB/DnaC/DnaG/HU/SSB/PolIII/beta, not PriC. Rep-DnaB binding is inhibited by DnaC; authors place binding after loading. Introduction separately cites a Rep/PriC restart pathway. These measured stages do not directly isolate the maintained quartet; they do not refute its existence. MG1655 appears in uvrD cloning, not proof of every preparation strain. |
| septin-ng1996ii-pdf | https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf; Genuine publisher-formatted primary PDF pp15649–15654: Introduction, Methods, Results, Discussion, TableI and Fig1–9 captions; references not treated as independently read studies; no figure pixels | supports | Retained PhiX174 ssDNA assembly contains PriA/PriB/PriC/DnaT/DnaB; DnaG associates for priming and DnaC is not a stable major constituent. PriA omission and PriC partial effects concern that different cohort, not the Rep/PriC quartet. Methods rely on prior preparations and do not certify a current reference strain for every reagent. No exhaustive assertion that no quartet experiment exists. |
| septin-pdb-entry | https://data.rcsb.org/rest/v1/core/entry/2R6D; Actual RCSB entry/assembly/entity fields; no coordinate or density reanalysis | supports | 2R6D primary citation Bailey/Eliason/Steitz2007; experimental X-ray3.7Angstrom entry, one protein entity and six protein instances. |
| septin-pdb-assembly | https://data.rcsb.org/rest/v1/core/assembly/2R6D/1; Actual RCSB entry/assembly/entity fields; no coordinate or density reanalysis | supports | Assembly1 is an author/software-defined homohexamer with six monomers, supporting the maintained six-copy DnaB stoichiometry. |
| septin-pdb-entity | https://data.rcsb.org/rest/v1/core/polymer_entity/2R6D/1; Actual RCSB entry/assembly/entity fields; no coordinate or density reanalysis | supports | ChainsA–F map completely to Q9X4C9; native biological source Bacillus/Geobacillus stearothermophilus1422 is distinct from E.coli BL21(DE3) expression host. This entry does not contain the DnaG-binding domain. |
| septin-ipr-IPR006295 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006295/; Actual current HTTP429 response only | context_only | The attempted route did not supply its requested scientific object/body. Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain bounded to primary abstract and native structural/identity data. Failure is not negative biology. |
| septin-ipr-IPR050219 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050219/; Actual current HTTP429 response only | context_only | The attempted route did not supply its requested scientific object/body. Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain bounded to primary abstract and native structural/identity data. Failure is not negative biology. |
| septin-mitkova-pdf | https://www.jbc.org/article/S0021925820752282/pdf; Actual current HTTP403 response only | context_only | The attempted route did not supply its requested scientific object/body. Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain bounded to primary abstract and native structural/identity data. Failure is not negative biology. |
| septin-bailey-publisher | https://www.science.org/doi/10.1126/science.1147353; Actual current HTTP403 response only | context_only | The attempted route did not supply its requested scientific object/body. Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain bounded to primary abstract and native structural/identity data. Failure is not negative biology. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete20-organism official catalogue; all organism names/keys independently inspected | supports | E.coli is covered; Geobacillus stearothermophilus is not listed. Bacillus subtilis is a different organism and is not used as a substitute. Catalogue coverage does not establish biological presence or absence. |
| septin-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete e_coli/precise1k metadata and strain list | supports | Five advertised strains BW25113,DGF-298,GMOS,MG1655,W3110;201 modules,1035samples. Appropriate reference-species context, not coverage of BL21(DE3), all mutants, every preparation in Ng/Guy or Geobacillus. |
| septin-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; All201 returned module ID/name/regulator/category rows; not activity traces or generated prose | supports | Nucleotide Stress module10 is a native annotated expression module; complete list supports a bounded gene-membership cross-check only. |
| septin-modulegene-rep | https://imodulondb.org/api/genes/e_coli/precise1k/b3778; Exact gene_id/name/product/UniProt mapping | supports | Dataset locus b3778 maps rep to the independently inspected native accession. Imported functional prose is annotation context, not a newly read primary paper. |
| septin-modulemembers-rep | https://imodulondb.org/api/genes/e_coli/precise1k/b3778/imodulons; All201 weight/threshold/is_in_imodulon rows | supports | Thresholded hits: none. False membership flags do not imply absent expression, gene, regulation or structural role; a positive hit does not establish assembly. |
| septin-modulegene-priC | https://imodulondb.org/api/genes/e_coli/precise1k/b0467; Exact gene_id/name/product/UniProt mapping | supports | Dataset locus b0467 maps priC to the independently inspected native accession. Imported functional prose is annotation context, not a newly read primary paper. |
| septin-modulemembers-priC | https://imodulondb.org/api/genes/e_coli/precise1k/b0467/imodulons; All201 weight/threshold/is_in_imodulon rows | supports | Thresholded hits: none. False membership flags do not imply absent expression, gene, regulation or structural role; a positive hit does not establish assembly. |
| septin-modulegene-dnaB | https://imodulondb.org/api/genes/e_coli/precise1k/b4052; Exact gene_id/name/product/UniProt mapping | supports | Dataset locus b4052 maps dnaB to the independently inspected native accession. Imported functional prose is annotation context, not a newly read primary paper. |
| septin-modulemembers-dnaB | https://imodulondb.org/api/genes/e_coli/precise1k/b4052/imodulons; All201 weight/threshold/is_in_imodulon rows | supports | Thresholded hits: none. False membership flags do not imply absent expression, gene, regulation or structural role; a positive hit does not establish assembly. |
| septin-modulegene-dnaC | https://imodulondb.org/api/genes/e_coli/precise1k/b4361; Exact gene_id/name/product/UniProt mapping | supports | Dataset locus b4361 maps dnaC to the independently inspected native accession. Imported functional prose is annotation context, not a newly read primary paper. |
| septin-modulemembers-dnaC | https://imodulondb.org/api/genes/e_coli/precise1k/b4361/imodulons; All201 weight/threshold/is_in_imodulon rows | supports | Thresholded hits: none. False membership flags do not imply absent expression, gene, regulation or structural role; a positive hit does not establish assembly. |
| septin-modulegene-dnaG | https://imodulondb.org/api/genes/e_coli/precise1k/b3066; Exact gene_id/name/product/UniProt mapping | supports | Dataset locus b3066 maps dnaG to the independently inspected native accession. Imported functional prose is annotation context, not a newly read primary paper. |
| septin-modulemembers-dnaG | https://imodulondb.org/api/genes/e_coli/precise1k/b3066/imodulons; All201 weight/threshold/is_in_imodulon rows | supports | Thresholded hits: 10 Nucleotide Stress. False membership flags do not imply absent expression, gene, regulation or structural role; a positive hit does not establish assembly. |
| septin-module-10 | https://imodulondb.org/api/imodulons/e_coli/precise1k/10; Native module name/category/threshold/member IDs; ai_summary and activity interpretation excluded | supports | Nucleotide Stress module10 threshold0.077432849 includes dnaG b3066 weight0.082144995; fifteen members. No regulator assigned; the expression cluster does not demonstrate physical DnaB-DnaG binding, localization or formation necessity. |
| septin-module-10-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/10/genes; Complete15 member identity rows; exact dnaG b3066 weight/threshold/native accession | supports | Independent member endpoint agrees dnaG/P0ABS5 belongs to the thresholded module. Other imported function prose is not primary evidence and does not expand this review to those proteins. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical actual Nov3 00:49Z invocation receipt | context_only | Actual prior exit1 PermissionError reading pyvenv.cfg; no fresh invocation or successful runner claimed. Current official source fallback is separately evidenced. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-septin/original-checks.json; Actual3 original validate/render runs and39 historical input occurrences | supports | All original native validate/render exit0; derived Markdown byte-identical. All13 historical inputs per original match retained source; all three current targets nonstale. Historical global gate provenance is not current-head CI. |
| septin-record-dnab_dnac_rep_pric_complex | data/structures/other/dnab_dnac_rep_pric_complex.yaml; Complete current frozen record, every field and history | context_only | Current full record independently assessed; historical rationale is not automatically current scientific evidence. |
| septin-original-dnab_dnac_rep_pric_complex | reviews/structured/20261022T060743Z-dnab-dnac-rep-pric-complex-audit/review.yaml; Complete original YAML and deterministic Markdown | context_only | Original scopes/findings/actions and exact historical input hashes independently reviewed; original bytes remain immutable. |
| septin-native-dnab_dnac_rep_pric_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-verify-receipt.json receiptSHA256 1cd9000424560e3d66e55f2816d7f74dcaa1ab7ad02be9937723130d76cdbe2c; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED. Native identifier/coverage success does not establish direct complex membership, experimental strain equivalence or formation necessity. |
| septin-native-dnab_dnac_rep_pric_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-causal-receipt.json receiptSHA256 731f7b0a133b6feac8c1dadca926613382e260b958ca80dc8ad36dcdc18851f7; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED. Native identifier/coverage success does not establish direct complex membership, experimental strain equivalence or formation necessity. |
| septin-record-dnab_dnag_complex | data/structures/other/dnab_dnag_complex.yaml; Complete current frozen record, every field and history | context_only | Current full record independently assessed; historical rationale is not automatically current scientific evidence. |
| septin-original-dnab_dnag_complex | reviews/structured/20261022T060744Z-dnab-dnag-complex-audit/review.yaml; Complete original YAML and deterministic Markdown | context_only | Original scopes/findings/actions and exact historical input hashes independently reviewed; original bytes remain immutable. |
| septin-native-dnab_dnag_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnag_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-verify-receipt.json receiptSHA256 408ddeb8dd1f44920bd990b56eebeba9b96b5b587579a4cbbc4b561687f4ee82; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED. Native identifier/coverage success does not establish direct complex membership, experimental strain equivalence or formation necessity. |
| septin-native-dnab_dnag_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnag_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-causal-receipt.json receiptSHA256 b5da46d0ccfe4371433722dc9ceddffd9aa706b61072346b24d56bb6bcb61b92; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed protein nodes, all COVERED. Native identifier/coverage success does not establish direct complex membership, experimental strain equivalence or formation necessity. |
| septin-record-dnab_helicase_complex | data/structures/other/dnab_helicase_complex.yaml; Complete current frozen record, every field and history | context_only | Current full record independently assessed; historical rationale is not automatically current scientific evidence. |
| septin-original-dnab_helicase_complex | reviews/structured/20261022T060744Z-dnab-helicase-complex-audit/review.yaml; Complete original YAML and deterministic Markdown | context_only | Original scopes/findings/actions and exact historical input hashes independently reviewed; original bytes remain immutable. |
| septin-native-dnab_helicase_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_helicase_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-verify-receipt.json receiptSHA256 362792eeccd1e8020b0332007e1e3689fc1beff368504630f7c26d9bc1bf63ce; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-verify.log | supports | Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed protein nodes, all COVERED. Native identifier/coverage success does not establish direct complex membership, experimental strain equivalence or formation necessity. |
| septin-native-dnab_helicase_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_helicase_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-causal-receipt.json receiptSHA256 e50ecb0daa3219354a84177889a6ea94c643c0797cff00637c4b282cdcd0c27f; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-causal.log | supports | Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed protein nodes, all COVERED. Native identifier/coverage success does not establish direct complex membership, experimental strain equivalence or formation necessity. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2388 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-dnaa_hda_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_hda_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_hu_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_hu_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_l2_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_l2_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_oric_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnaa_oric_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_dnat_pria_prib_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_dnat_pria_prib_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_dnat_pria_pric_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_dnat_pria_pric_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_rep_pric_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnac_rep_pric_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnag_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_dnag_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_helicase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-dnab_helicase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: This scientific slice covers only DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC. All four current hashes are unchanged from original frozen inputs. Auxiliary row7 Rep-query challenge is separately scoped and owned by the other reviewer; no outside-slice scientific disposition is added here. No repository/Git/GitHub mutation.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Keyamura2011 genuine primary main HTML, Methods/Results/Discussion and all text captions were read freshly; no figure pixels, supplement, sequence alignments or coordinates. DNA-loaded-clamp/ADP-Hda staged hydrolysis and contact assays differ from binary identity; proposed structural model is not a solved cocrystal. Kurz2004 remains complete primary-abstract tier.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Chodavarapu2008 HU work remains complete primary-abstract tier after fresh Wiley HTML/PDF403. Exact experimental strains/full methods/images and taxon-wide bacterial necessity are not certified or refuted. HUalpha and alphabeta alternatives are retained, not an invariant heterodimer.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Chodavarapu2011 L2 genuine main JATS and captions were read freshly. In-vitro contacts/inhibition, DM700 tL2 preparation and tested negative in-vivo tL2 initiation result remain distinct; no general in-vivo checkpoint, fixed stoichiometry, solved interface or cleavage mechanism is asserted.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Miller2009 genuine main HTML including Introduction/Results/Discussion/Methods and captions was read freshly. No raw footprints/pixels were reanalyzed. Elevated-DnaA rescue of low-affinity filling limits universal absence interpretations; actual mutant/strain/purified-protein contexts remain explicit.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Three DnaA-localization papers and Hda-localization paper are complete primary-abstract/native-annotation tier only. Current native UniProt identities/xrefs and family metadata do not certify every linked experiment. Reference taxon83333, species562, BL21(DE3) localization context and specific experimental strains are not conflated.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: InterPro family versus domain/broader/taxon-limited alternatives are distinguished. HdaIPR022864 is narrower; uL2IPR002171 is broader. Exact oriC SO class is not one strain sequence; HU whole-dimer identity is not a single protein family. Five inherited findings remain1major4minor with exact lineage; historical rationale is append-only.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Official precise1k contains five K12-related strains, not every primary mutant/preparation. Five exact loci each have201 inspected membership rows; only rplB crosses Translation module1 threshold, corroborated in all53 member IDs/weights/identity columns. Negative rows are not gene absence; positive expression context is not physical assembly/direct regulation/necessity. Generated AI summaries and activity contrasts are not used.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Historical adapter runner is the actual2026-11-03T00:49Z unavailable invocation, not new execution. Four retained old failed-access observations preserve their originalOct22time/hash/classification correction; they are not claimed as new raw-response fetches. Present blocked routes and separate successful bodies are distinguished.
- DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Eight actual source-head native protein commands pass with6reviewed examples and6COVERED typed protein nodes; HU STRUCTURE and oriC feature nodes are outside that inventory and assessed separately. Original8native validate/render commands and56historical hashes pass. Root owns globalQC and future successor/postsave/CI/queue gates; none is newly certified by this source report.
- DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: NgI is assessed at its complete native primary abstract/metadata tier only; its full body and indexed erratum contents were not inspected. NgII main PDF text, Methods, Table I and captions were read, without pixels, Western reanalysis or uninspected cited studies.
- DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: Makowska-Grzyska/Kaguni selected main Results/Discussion/Methods and figure captions were read; supplementary strain Table S1 and raw data were not inspected. No exact experimental K-12 derivative is inferred from reference accessions.
- DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: The fresh public iModulonDB source fallback is not an invocation of the structured runner. The separate retained 2026-11-03 00:49Z unavailable-runner receipt remains historical; no fresh runner success or failure is asserted here. Five-strain precise1k context and above-threshold flags do not establish localization, physical membership, necessity or absence. Generated module summaries were excluded.
- DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: No exact source-neutral PAS-DNA mapping was established; this uncertainty is retained without an optional-field finding. No universal copy-number or formation requirement is inferred from viability, membership annotations or another experimental assembly.
- DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: The current GO labels/definitions are copied accurately; the two source-scope findings distinguish experimental stage and retained composition rather than declaring transient loading intermediates impossible or replacing the maintained identities.
- DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: Native local gate receipts are scoped to their actual commands. This independent slice does not certify corpus gates, GitHub CI, queue admission, merge or branch cleanup.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Three unchanged targets; five inherited open scientific findings (one major,four minor) and one exact-lineage rejected minor Rep-query finding. All three records still need localized curation; no new scientific finding. Three original formal applicability exclusions and one unsupported original finding need successor correction.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Guy2009 fresh genuine body inspected only at stated sections/captions; no full reading of Results2.2–2.5,supplementary TableS1 or figure pixels. Ng1996II genuine primary PDF scientific body pp15649–15654 read with captions/TableI,not independent raw-data or pixel analysis. Its PhiX/PriA cohort is not the Rep/PriC quartet. No claim of exhaustive literature absence.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Mitkova2003 and Bailey2007 access is full native abstract/metadata plus native UniProt/PDB authority scope,not full article bodies. Actual publisher403 responses remain validation context. Mitkova stabilized E.coli3:6 ratio is conditional; Bailey2R6D exact assembly has six Q9X4C9 chains and no DnaG domain. Biological1422 differs from BL21(DE3) expression host.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: InterPro IPR005752 erroneous Rep-hexamer prose and IPR050219 unchecked LLM-generated description are excluded from biology; verified family/type/signature metadata remains usable. IPR006295 is a domain,not a full DnaG class. PAS-DNA remains unresolved rather than silently oriC.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Current Rep gene_exact query returns primary rep/P09980 plus primary repE/P03856 with rep alias. This does not establish the exact past query or negate correct maintained Rep-helicase identity. Native ambiguous automatic seeding is distinct from manual identity disambiguation; optional alias explanation is not a mandatory record correction.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Fresh official catalogue has20organism rows; E.coli precise1k supports bounded reference context,five advertised strains and201modules. Five exact loci checked; only dnaG has thresholded Nucleotide Stress10 membership,confirmed in fifteen-member endpoint. Other false flags are not biological absence; no activity-vector interpretation or generated module prose used. No Geobacillus dataset; Bacillus subtilis/E.coli expression host is not a proxy.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Historical runner failed Nov3 00:49Z with PermissionError; no fresh runner invocation. Shared current catalogue/metadata packet uses its actual Nov4 retrieval dates and independently inspected scope. Authority retries after429 are distinct from initial failed responses.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Actual own native inventory has five reviewed examples and five COVERED protein nodes; six commands exit0 at current source. This verifies native identity/coverage,not experimental membership or necessity. Original three pairs validate/render exactly with39 historical input occurrences verified. Root global gates,successor/final-head validation,CI,queue and merge are separate attestations.
- Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Only26 listed frozen maintained inputs used; no extra neighbor or prior-review bundle used as biological authority. Original historical source receipts are inspected as original provenance,not falsely claimed fresh body access. No source-kind defect is established in these three originals: their Mitkova/Bailey access limitations do not constitute misclassified failed-response evidence rows.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- The original ten target hashes all match current main; no stale record required refresh. The successor still provides current independent scientific reassessment and preserves all20 original artifacts.
- Bundle issues #2936 and #2937 cover seven formal and three prose applicability exclusions and four historical access-only evidence-kind corrections. Issue #2938 rejects the original Rep query-uniqueness finding with exact lineage, preserving the correct P09980 identity and dated record history without requiring record curation.
- Current native commands verify19 protein example occurrences and19 typed GENE_OR_PROTEIN nodes, all COVERED. Complex-level constituents remain separately scoped; optional protein inventories and universally essential formation labels are not compelled.
- Fifteen inherited open scientific findings (four major, eleven minor) retain exact predecessor lineage and bounded curation actions. The sixteenth inherited finding, Rep query F3, is explicitly rejected and linked to bundle issue #2938, with no corresponding record-curation action. Current primary-gene selection, search-alias behavior and historical query provenance remain distinct. All ten targets retain needs_curation for their remaining findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T072147Z-pr2389-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2389: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T07:05:06.244734Z'
finished_at: '2026-11-04T07:21:47Z'
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
summary: 'Current-input independent reassessment of all ten records: all original
  target hashes match current main, so no stale record requires refresh. Fifteen inherited
  scientific findings remain open (four major, eleven minor), with fifteen bounded
  record-curation actions and all ten targets needing curation. The original Rep query-uniqueness
  finding is rejected with exact predecessor lineage, an explicit disposition reason
  and no record-curation action: a present alias-inclusive query cannot establish
  the historical unstated search or invalidate the correct primary Rep accession.
  The successor corrects seven formal and three prose structured-source applicability
  exclusions and four historical failed-access evidence classifications, preserving
  all twenty original artifacts and all scientific records. Independent source scopes
  distinguish primary bodies, complete abstracts, authority metadata, experimental
  stages, biological strains and expression hosts. Every open scientific finding is
  linked to a deduplicated issue; bundle corrections and existing resolver tooling
  are tracked separately.'
source:
  git_revision: 14475ecacc26d4832351bb4974cfa23bd4ec7b02
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
  - path: data/structures/other/dnaa_hda_complex.yaml
    sha256: 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e
    role: target
  - path: data/structures/other/dnaa_hu_complex.yaml
    sha256: c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3
    role: target
  - path: data/structures/other/dnaa_l2_complex.yaml
    sha256: 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd
    role: target
  - path: data/structures/other/dnaa_oric_complex.yaml
    sha256: af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976
    role: target
  - path: data/structures/other/dnab_dnac_complex.yaml
    sha256: 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180
    role: target
  - path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    sha256: 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5
    role: target
  - path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    sha256: af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43
    role: target
  - path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    sha256: 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f
    role: target
  - path: data/structures/other/dnab_dnag_complex.yaml
    sha256: 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c
    role: target
  - path: data/structures/other/dnab_helicase_complex.yaml
    sha256: 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99
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
  - path: reviews/structured/20261022T060738Z-dnaa-hda-complex-audit/review.md
    sha256: 5d8cfea3cd73e99ba0b04816c27ac2ae16a554313bff4c1bf733ff497cc63dc5
    role: context
  - path: reviews/structured/20261022T060738Z-dnaa-hda-complex-audit/review.yaml
    sha256: ab37d8620bd788bd65624706799df13a913de1f25f6b8a328ab14d81ea2e924e
    role: context
  - path: reviews/structured/20261022T060739Z-dnaa-hu-complex-audit/review.md
    sha256: cac2064ff76e6411e51f4c259f1e79e08ca92957c500af4d56e9cf55f6dd1d98
    role: context
  - path: reviews/structured/20261022T060739Z-dnaa-hu-complex-audit/review.yaml
    sha256: 99611445e0c493a2b559d4906c71d15f88952caadde91f10bb0892a040ee2a29
    role: context
  - path: reviews/structured/20261022T060740Z-dnaa-l2-complex-audit/review.md
    sha256: ddf304bd5091a52b03e74563720dbc000621f89a8630ffc224922e3e1d250938
    role: context
  - path: reviews/structured/20261022T060740Z-dnaa-l2-complex-audit/review.yaml
    sha256: 0ec280ca6db6bccc63f4c70a767f70769ddccd0c7b452c2a355d57cc3e52b52b
    role: context
  - path: reviews/structured/20261022T060740Z-dnaa-oric-complex-audit/review.md
    sha256: 78d99047e56684986dab4c0ab81f3e389998519317da68e657ce25d6c1aaa309
    role: context
  - path: reviews/structured/20261022T060740Z-dnaa-oric-complex-audit/review.yaml
    sha256: a3199212cc260132a131abc4885422a4db90a07e16b5e003d9528208117f15b3
    role: context
  - path: reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.md
    sha256: 33923abc4393609c3edb42f954dc2d4131310484e856400e0eca43f1e0ee3160
    role: context
  - path: reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.yaml
    sha256: 643aaee2288fb0858a7dd8484509816f8419bf2b948ada3020e321ec06eb84e8
    role: context
  - path: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.md
    sha256: e5152fdea2e9547498cb597c9b3fcc8cdc9313f97cfa9ca78c8bfa4e89e63f84
    role: context
  - path: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.yaml
    sha256: a8ea503d08d2cc9f59bac77f0351b77e37b49d4b1fac7590685f013833f1346d
    role: context
  - path: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.md
    sha256: 2ce73b853f1d9eddcd3a98a654592ee6ab8bd9219c46ae39d6c6fecd60826d26
    role: context
  - path: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.yaml
    sha256: 18e1b3c70520f2d1651f55adabbf733c4e5c7d04d6ae4b78a67a4dcc5e775b60
    role: context
  - path: reviews/structured/20261022T060743Z-dnab-dnac-rep-pric-complex-audit/review.md
    sha256: 9998750d04218c9c57bf09cbc4b0529e5a795d1455e096de2cac2b5ce8e7fcb6
    role: context
  - path: reviews/structured/20261022T060743Z-dnab-dnac-rep-pric-complex-audit/review.yaml
    sha256: 1e4077fc36e5c5ecf3b5dda71df6dd60ef532fafa2c798da60e019b95f4d41c3
    role: context
  - path: reviews/structured/20261022T060744Z-dnab-dnag-complex-audit/review.md
    sha256: a09a25717c23fa6c5400a005837bd2466910711477bf5c767c6e94efda448b49
    role: context
  - path: reviews/structured/20261022T060744Z-dnab-dnag-complex-audit/review.yaml
    sha256: 67a40ef8cbee52e94d9386a29ab3d712b8ae87e2f00f7adb8f452e898db9badd
    role: context
  - path: reviews/structured/20261022T060744Z-dnab-helicase-complex-audit/review.md
    sha256: 2586070a4992c1a268baa84538cfb446cee5938c94e572ecac53b8282db8adb4
    role: context
  - path: reviews/structured/20261022T060744Z-dnab-helicase-complex-audit/review.yaml
    sha256: acfe6847ede731a7cb548b259beeb69ed0222ecfa2d547cd70c3183269b8ff19
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
- target_id: GO:1990083
  path: data/structures/other/dnaa_hda_complex.yaml
  label: DnaA-Hda complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
- target_id: GO:1990103
  path: data/structures/other/dnaa_hu_complex.yaml
  label: DnaA-HU complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hu_complex.yaml
    role: maintained scientific record
- target_id: GO:1990082
  path: data/structures/other/dnaa_l2_complex.yaml
  label: DnaA-L2 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_l2_complex.yaml
    role: maintained scientific record
- target_id: GO:1990101
  path: data/structures/other/dnaa_oric_complex.yaml
  label: DnaA-oriC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_oric_complex.yaml
    role: maintained scientific record
- target_id: GO:1990100
  path: data/structures/other/dnab_dnac_complex.yaml
  label: DnaB-DnaC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_complex.yaml
    role: maintained scientific record
- target_id: GO:1990158
  path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  label: DnaB-DnaC-DnaT-PriA-PriB complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
- target_id: GO:1990159
  path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  label: DnaB-DnaC-DnaT-PriA-PriC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
- target_id: GO:1990160
  path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
  label: DnaB-DnaC-Rep-PriC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
- target_id: GO:1990156
  path: data/structures/other/dnab_dnag_complex.yaml
  label: DnaB-DnaG complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnag_complex.yaml
    role: maintained scientific record
- target_id: GO:1990161
  path: data/structures/other/dnab_helicase_complex.yaml
  label: DnaB helicase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_helicase_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main dbad8ee30de8ed1a1a2b2d828b471248232119ed.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    5232267fcf66b8911d0c40e386913bd3a3a0f06d.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 14475ecacc26d4832351bb4974cfa23bd4ec7b02.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 14475ecacc26d4832351bb4974cfa23bd4ec7b02.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 14475ecacc26d4832351bb4974cfa23bd4ec7b02.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 14475ecacc26d4832351bb4974cfa23bd4ec7b02.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 14475ecacc26d4832351bb4974cfa23bd4ec7b02.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:1990083
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just validate data/structures/other/dnaa_hda_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:1990083
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: just validate-strict data/structures/other/dnaa_hda_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:1990103
  status: passed
  required: true
  target_ids:
  - GO:1990103
  command: just validate data/structures/other/dnaa_hu_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:1990103
  status: passed
  required: true
  target_ids:
  - GO:1990103
  command: just validate-strict data/structures/other/dnaa_hu_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:1990082
  status: passed
  required: true
  target_ids:
  - GO:1990082
  command: just validate data/structures/other/dnaa_l2_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:1990082
  status: passed
  required: true
  target_ids:
  - GO:1990082
  command: just validate-strict data/structures/other/dnaa_l2_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:1990101
  status: passed
  required: true
  target_ids:
  - GO:1990101
  command: just validate data/structures/other/dnaa_oric_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:1990101
  status: passed
  required: true
  target_ids:
  - GO:1990101
  command: just validate-strict data/structures/other/dnaa_oric_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:1990100
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just validate data/structures/other/dnab_dnac_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:1990100
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: just validate-strict data/structures/other/dnab_dnac_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:1990158
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: just validate data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:1990158
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: just validate-strict data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:1990159
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just validate data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:1990159
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: just validate-strict data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:1990160
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: just validate data/structures/other/dnab_dnac_rep_pric_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:1990160
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: just validate-strict data/structures/other/dnab_dnac_rep_pric_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:1990156
  status: passed
  required: true
  target_ids:
  - GO:1990156
  command: just validate data/structures/other/dnab_dnag_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:1990156
  status: passed
  required: true
  target_ids:
  - GO:1990156
  command: just validate-strict data/structures/other/dnab_dnag_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:1990161
  status: passed
  required: true
  target_ids:
  - GO:1990161
  command: just validate data/structures/other/dnab_helicase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:1990161
  status: passed
  required: true
  target_ids:
  - GO:1990161
  command: just validate-strict data/structures/other/dnab_helicase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389
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
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  summary: Whole-record molecular and pathway assertions trigger applicability for
    all ten targets. Fresh official iModulonDB catalogue coverage identifies E. coli
    precise1k for nine records and no biological-source Geobacillus stearothermophilus
    dataset for the DnaB homohexamer; Bacillus subtilis and E. coli expression-host
    data are not proxies. Exact native loci were checked against all 201 module membership
    rows in the selected five-strain precise1k dataset. Positive rplB and priB Translation
    module 1 memberships and dnaG Nucleotide Stress module 10 membership were corroborated
    in complete member lists; remaining threshold nonhits do not imply absence. These
    are bounded expression contexts, not physical complex formation, direct regulation,
    necessity or current experimental-strain matches. No generated summaries or activity
    contrasts are used. The historical unavailable structured runner receipt is retained
    separately; direct official API access is not a fresh runner invocation.
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-gene-b3702
  - micro-ecoli-gene-b2496
  - micro-ecoli-gene-b3317
  - micro-ecoli-gene-b4000
  - micro-ecoli-gene-b0440
  - micro-adapter-module1
  - micro-adapter-module1-genes
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-modules
  - plaque-adapter-b4052-gene
  - plaque-adapter-b4052-modules
  - plaque-adapter-b4361-gene
  - plaque-adapter-b4361-modules
  - plaque-adapter-b4362-gene
  - plaque-adapter-b4362-modules
  - plaque-adapter-b3935-gene
  - plaque-adapter-b3935-modules
  - plaque-adapter-b4201-gene
  - plaque-adapter-b4201-modules
  - plaque-adapter-b0467-gene
  - plaque-adapter-b0467-modules
  - plaque-adapter-module1
  - plaque-adapter-module1-genes
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-modulegene-rep
  - septin-modulemembers-rep
  - septin-modulegene-priC
  - septin-modulemembers-priC
  - septin-modulegene-dnaB
  - septin-modulemembers-dnaB
  - septin-modulegene-dnaC
  - septin-modulemembers-dnaC
  - septin-modulegene-dnaG
  - septin-modulemembers-dnaG
  - septin-module-10
  - septin-module-10-genes
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-graph-policy
  - micro-protein-P03004
  - micro-protein-P60422
  - micro-protein-P69931
  - micro-tax-562
  - micro-tax-83333
  - micro-go-0006270
  - micro-go-0032297
  - micro-go-1990077
  - micro-go-1990078
  - micro-go-1990082-ancestors
  - micro-go-1990082-constraints
  - micro-go-1990082
  - micro-go-1990083-ancestors
  - micro-go-1990083-constraints
  - micro-go-1990083
  - micro-go-1990084
  - micro-go-1990085
  - micro-go-1990100
  - micro-go-1990101-ancestors
  - micro-go-1990101-constraints
  - micro-go-1990101
  - micro-go-1990102
  - micro-go-1990103-ancestors
  - micro-go-1990103-constraints
  - micro-go-1990103
  - micro-ipr-IPR001957
  - micro-ipr-IPR017788
  - micro-ipr-IPR022864
  - micro-ipr-IPR005880
  - micro-ipr-IPR002171-retry
  - micro-so-0000953
  - micro-pmid-12618445
  - micro-pmid-15150238
  - micro-pmid-18179598
  - micro-pmid-19833870
  - micro-pmid-21288885
  - micro-pmid-21708944
  - micro-pmid-22574163
  - micro-pmid-28166228
  - micro-pmid-9478970
  - micro-keyamura2011-pmc
  - micro-chodavarapu2011-jats
  - micro-miller2009-pmc
  - micro-ecoli-meta
  - micro-adapter-module1
  - micro-adapter-module1-genes
  - plaque-curation
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
  - plaque-go-1990100-ancestors
  - plaque-go-1990100-constraints
  - plaque-go-1990158-ancestors
  - plaque-go-1990158-constraints
  - plaque-go-1990159-ancestors
  - plaque-go-1990159-constraints
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-pmid-20129058
  - plaque-pmid-8663104
  - plaque-pmid-8663105
  - plaque-makowska2010-body
  - plaque-ng1996ii-pdf
  - plaque-up-P0ACB0
  - plaque-up-P0AEF0
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P07013
  - plaque-up-P23862
  - plaque-ipr-IPR007692
  - plaque-ncbifam-NF005931
  - plaque-ipr-IPR028350
  - plaque-ipr-IPR020917
  - plaque-ipr-IPR005259
  - plaque-ipr-IPR023646
  - plaque-ipr-IPR010890
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-modules
  - plaque-adapter-b4052-gene
  - plaque-adapter-b4361-gene
  - plaque-adapter-b4362-gene
  - plaque-adapter-b3935-gene
  - plaque-adapter-b4201-gene
  - plaque-adapter-b0467-gene
  - plaque-adapter-module1
  - plaque-adapter-module1-genes
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-go
  - septin-ipr-IPR005752
  - septin-ipr-IPR010890
  - septin-ipr-IPR007692
  - septin-ipr-IPR030846
  - septin-retry-IPR006295
  - septin-retry-IPR050219
  - septin-up-P09980
  - septin-up-P23862
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-up-Q9X4C9
  - septin-up-P03856
  - septin-up-P0AEF0
  - septin-tax-562
  - septin-tax-83333
  - septin-tax-1422
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-pmid-14557266
  - septin-pmid-17947583
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-modulegene-rep
  - septin-modulegene-priC
  - septin-modulegene-dnaB
  - septin-modulegene-dnaC
  - septin-modulegene-dnaG
  - septin-module-10
  - septin-module-10-genes
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
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
- check_id: dnaa_hda_complex-uniprot-verify
  name: Native DnaA-Hda complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_hda_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_hda_complex-uniprot-verify
- check_id: dnaa_hda_complex-uniprot-causal
  name: Native DnaA-Hda complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990083
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_hda_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_hda_complex-uniprot-causal
- check_id: dnaa_hu_complex-uniprot-verify
  name: Native DnaA-HU complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990103
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_hu_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_hu_complex-uniprot-verify
- check_id: dnaa_hu_complex-uniprot-causal
  name: Native DnaA-HU complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990103
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_hu_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_hu_complex-uniprot-causal
- check_id: dnaa_l2_complex-uniprot-verify
  name: Native DnaA-L2 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990082
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_l2_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_l2_complex-uniprot-verify
- check_id: dnaa_l2_complex-uniprot-causal
  name: Native DnaA-L2 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990082
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_l2_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_l2_complex-uniprot-causal
- check_id: dnaa_oric_complex-uniprot-verify
  name: Native DnaA-oriC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990101
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_oric_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_oric_complex-uniprot-verify
- check_id: dnaa_oric_complex-uniprot-causal
  name: Native DnaA-oriC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990101
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnaa_oric_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnaa_oric_complex-uniprot-causal
- check_id: dnab_dnac_complex-uniprot-verify
  name: Native DnaB-DnaC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_complex-uniprot-verify
- check_id: dnab_dnac_complex-uniprot-causal
  name: Native DnaB-DnaC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990100
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_complex-uniprot-causal
- check_id: dnab_dnac_dnat_pria_prib_complex-uniprot-verify
  name: Native DnaB-DnaC-DnaT-PriA-PriB complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_dnat_pria_prib_complex-uniprot-verify
- check_id: dnab_dnac_dnat_pria_prib_complex-uniprot-causal
  name: Native DnaB-DnaC-DnaT-PriA-PriB complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990158
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_dnat_pria_prib_complex-uniprot-causal
- check_id: dnab_dnac_dnat_pria_pric_complex-uniprot-verify
  name: Native DnaB-DnaC-DnaT-PriA-PriC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_dnat_pria_pric_complex-uniprot-verify
- check_id: dnab_dnac_dnat_pria_pric_complex-uniprot-causal
  name: Native DnaB-DnaC-DnaT-PriA-PriC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990159
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_dnat_pria_pric_complex-uniprot-causal
- check_id: dnab_dnac_rep_pric_complex-uniprot-verify
  name: Native DnaB-DnaC-Rep-PriC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_rep_pric_complex-uniprot-verify
- check_id: dnab_dnac_rep_pric_complex-uniprot-causal
  name: Native DnaB-DnaC-Rep-PriC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990160
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnac_rep_pric_complex-uniprot-causal
- check_id: dnab_dnag_complex-uniprot-verify
  name: Native DnaB-DnaG complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990156
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnag_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnag_complex-uniprot-verify
- check_id: dnab_dnag_complex-uniprot-causal
  name: Native DnaB-DnaG complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990156
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnag_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_dnag_complex-uniprot-causal
- check_id: dnab_helicase_complex-uniprot-verify
  name: Native DnaB helicase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990161
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_helicase_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_helicase_complex-uniprot-verify
- check_id: dnab_helicase_complex-uniprot-causal
  name: Native DnaB helicase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990161
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_helicase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-dnab_helicase_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/dnaa_hda_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e;
    current SHA256 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T060738Z-dnaa-hda-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ab37d8620bd788bd65624706799df13a913de1f25f6b8a328ab14d81ea2e924e
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/dnaa_hu_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3;
    current SHA256 c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3.
    Record bytes unchanged since the original review.
  snapshot_sha256: c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T060739Z-dnaa-hu-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 99611445e0c493a2b559d4906c71d15f88952caadde91f10bb0892a040ee2a29
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/dnaa_l2_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd;
    current SHA256 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd.
    Record bytes unchanged since the original review.
  snapshot_sha256: 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T060740Z-dnaa-l2-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 0ec280ca6db6bccc63f4c70a767f70769ddccd0c7b452c2a355d57cc3e52b52b
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/dnaa_oric_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976;
    current SHA256 af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976.
    Record bytes unchanged since the original review.
  snapshot_sha256: af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T060740Z-dnaa-oric-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a3199212cc260132a131abc4885422a4db90a07e16b5e003d9528208117f15b3
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/dnab_dnac_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180;
    current SHA256 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180.
    Record bytes unchanged since the original review.
  snapshot_sha256: 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 643aaee2288fb0858a7dd8484509816f8419bf2b948ada3020e321ec06eb84e8
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5;
    current SHA256 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5.
    Record bytes unchanged since the original review.
  snapshot_sha256: 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a8ea503d08d2cc9f59bac77f0351b77e37b49d4b1fac7590685f013833f1346d
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43;
    current SHA256 af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43.
    Record bytes unchanged since the original review.
  snapshot_sha256: af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 18e1b3c70520f2d1651f55adabbf733c4e5c7d04d6ae4b78a67a4dcc5e775b60
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/dnab_dnac_rep_pric_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f;
    current SHA256 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f.
    Record bytes unchanged since the original review.
  snapshot_sha256: 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T060743Z-dnab-dnac-rep-pric-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1e4077fc36e5c5ecf3b5dda71df6dd60ef532fafa2c798da60e019b95f4d41c3
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/dnab_dnag_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c;
    current SHA256 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T060744Z-dnab-dnag-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 67a40ef8cbee52e94d9386a29ab3d712b8ae87e2f00f7adb8f452e898db9badd
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/dnab_helicase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Original frozen SHA256 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99;
    current SHA256 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99.
    Record bytes unchanged since the original review.
  snapshot_sha256: 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T060744Z-dnab-helicase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T07:21:47Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: acfe6847ede731a7cb548b259beeb69ed0222ecfa2d547cd70c3183269b8ff19
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/dnaa_hda_complex.yaml
  locator: Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02
  accessed_at: '2026-11-04T07:17:45.243122Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: 483a497d765d330fb525a7294da3190f44406843dd7acf5e563fedd971533a8e
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T060738Z-dnaa-hda-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T07:17:45.243217Z'
  support: supports
  summary: Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions
    inspected; historical checks and access timestamps are not newly executed or fetched.
  snapshot_sha256: ab37d8620bd788bd65624706799df13a913de1f25f6b8a328ab14d81ea2e924e
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/0-stale.diff
  locator: Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed
  accessed_at: '2026-11-04T07:17:45.243256Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned four-record
    slice. Current primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/dnaa_hu_complex.yaml
  locator: Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02
  accessed_at: '2026-11-04T07:17:45.243289Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: c1a75c31a02371a7ae84e7732e2f45e97398bcb9ddf28247bec3026cd6f802f3
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T060739Z-dnaa-hu-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T07:17:45.243311Z'
  support: supports
  summary: Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions
    inspected; historical checks and access timestamps are not newly executed or fetched.
  snapshot_sha256: 99611445e0c493a2b559d4906c71d15f88952caadde91f10bb0892a040ee2a29
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/1-stale.diff
  locator: Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed
  accessed_at: '2026-11-04T07:17:45.243343Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned four-record
    slice. Current primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/dnaa_l2_complex.yaml
  locator: Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02
  accessed_at: '2026-11-04T07:17:45.243373Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: 02922dc2d03f7d1dce3a07650d55d6ac6e827b61b9c09ebc3b5dee50a58e8afd
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T060740Z-dnaa-l2-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T07:17:45.243393Z'
  support: supports
  summary: Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions
    inspected; historical checks and access timestamps are not newly executed or fetched.
  snapshot_sha256: 0ec280ca6db6bccc63f4c70a767f70769ddccd0c7b452c2a355d57cc3e52b52b
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/2-stale.diff
  locator: Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed
  accessed_at: '2026-11-04T07:17:45.243426Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned four-record
    slice. Current primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-3
  kind: record_content
  reference: data/structures/other/dnaa_oric_complex.yaml
  locator: Complete maintained YAML at 14475ecacc26d4832351bb4974cfa23bd4ec7b02
  accessed_at: '2026-11-04T07:17:45.243452Z'
  support: supports
  summary: All identity, hierarchy, components/examples, functions, canonical taxa,
    graph edges, evidence, discussions and history inspected. No maintained images
    or measurements. Current record is byte-identical to its original frozen target.
  snapshot_sha256: af3deef66bb9816ea02f79adee17921b145d8170bd97434ab260f709fa346976
- evidence_id: micro-prior-3
  kind: prior_review
  reference: reviews/structured/20261022T060740Z-dnaa-oric-complex-audit/review.yaml
  locator: Complete immutable original YAML and deterministic Markdown
  accessed_at: '2026-11-04T07:17:45.243472Z'
  support: supports
  summary: Original source inputs/checks/evidence scopes/assessments/verdict/findings/actions
    inspected; historical checks and access timestamps are not newly executed or fetched.
  snapshot_sha256: a3199212cc260132a131abc4885422a4db90a07e16b5e003d9528208117f15b3
- evidence_id: micro-delta-3
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/3-stale.diff
  locator: Original frozen target versus current main dbad8ee30de8ed1a1a2b2d828b471248232119ed
  accessed_at: '2026-11-04T07:17:45.243505Z'
  support: supports
  summary: 'Empty target diff: no stale scientific field in this assigned four-record
    slice. Current primary and authority reassessment was nevertheless performed.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Exact taxon-neutral family/class grounding, formation versus function and
    append-only discussions
  accessed_at: '2026-11-04T07:17:45.243530Z'
  support: supports
  summary: Current verified exact mappings are consequential class-grounding gaps
    under the local contract, not demands for optional examples. UNKNOWN formation
    is valid. Preserve historical rationale/posed_date; narrow current prompt/notes
    only after supported separate curation.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: ComponentTypeEnum, exact grounding, essentiality, complex/feature and graph
    scopes
  accessed_at: '2026-11-04T07:17:45.243554Z'
  support: supports
  summary: HU dimer is a complex, not a single HU-family protein; oriC is a feature
    class, not one strain sequence. Generic named classes and NONMECHANISTIC FUNCTION
    outlines are valid; physical formation is distinct from viability, initiation
    activity or depletion experiments.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks; current profile, config, rubric and shared
    review contract
  accessed_at: '2026-11-04T07:17:45.243584Z'
  support: supports
  summary: Positive molecular/pathway claims require structured-source applicability
    even without expression assertions. Seventeen common inputs retain exact prior-read
    hashes; AGENTS, skill, profile, config, review contract and pertinent family/history/graph
    clauses reread for this task.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Constituent references, direct versus contextual evidence, scoped function
    outlines
  accessed_at: '2026-11-04T07:17:45.243604Z'
  support: supports
  summary: Descriptive membership/function can be supported without a full mechanistic
    reaction sequence, exact stoichiometry, universal essentiality or mandatory new
    experiments.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/original-audit.json
  locator: Eight actual original validate/render commands;56 historical input occurrences;8
    original artifacts
  accessed_at: '2026-11-04T07:06:52.481031Z'
  support: supports
  summary: All four original YAMLs validate and render exactly their retained Markdown.
    All56 historical input hashes match recorded source revisions; all8 original artifacts
    equal the original PR head.
  snapshot_sha256: b46d0b9d9d07620d59b8707ed1080558b7093c43a0ab0cf767699dd4b9eef736
- evidence_id: micro-protein-P03004
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P03004.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro and stated
    annotation sections; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/protein-P03004.raw
  accessed_at: '2026-11-04T07:06:55.110202Z'
  support: supports
  summary: 'P03004: UniProtKB reviewed (Swiss-Prot); Chromosomal replication initiator
    protein DnaA; genes [''dnaA'']; loci [''b3702'', ''JW3679'']; taxon 83333; InterPro
    [''IPR003593'', ''IPR001957'', ''IPR020591'', ''IPR018312'', ''IPR013159'', ''IPR013317'',
    ''IPR024633'', ''IPR038454'', ''IPR027417'', ''IPR010921'']. Complete relevant
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY annotations read; native references
    do not imply every linked primary body was read. DnaA localization papers are
    independently complete abstract tier only; the native 10-percent membrane example
    explicitly concerns BL21(DE3), not an exact K12 complex assay.'
  snapshot_sha256: 20b9ed0385942a0aebc3645f0f499a77e9aab0741218e2327ee80b6ae7590dca
- evidence_id: micro-protein-P60422
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P60422.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro and stated
    annotation sections; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/protein-P60422.raw
  accessed_at: '2026-11-04T07:06:57.106100Z'
  support: supports
  summary: 'P60422: UniProtKB reviewed (Swiss-Prot); Large ribosomal subunit protein
    uL2; genes [''rplB'']; loci [''b3317'', ''JW3279'']; taxon 83333; InterPro [''IPR012340'',
    ''IPR014722'', ''IPR002171'', ''IPR005880'', ''IPR022669'', ''IPR022671'', ''IPR014726'',
    ''IPR022666'', ''IPR008991'']. Complete relevant FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY annotations read; native references do not imply every linked
    primary body was read. Current recommended uL2 name and rplB primary gene match
    historical 50S-L2 wording; generic ribosomal functions are not evidence of DnaA
    binding, which has its own primary paper.'
  snapshot_sha256: 8b5482c3eae315c50a348a064a8c581fc1d721ce36d218c990a085d52733b63b
- evidence_id: micro-protein-P69931
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P69931.json
  locator: Native identity/status/name/primary gene/loci/taxon/InterPro and stated
    annotation sections; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/protein-P69931.raw
  accessed_at: '2026-11-04T07:06:56.034491Z'
  support: supports
  summary: 'P69931: UniProtKB reviewed (Swiss-Prot); DnaA regulatory inactivator Hda;
    genes [''hda'']; loci [''b2496'', ''JW5397'', ''f248c'']; taxon 83333; InterPro
    [''IPR020591'', ''IPR013317'', ''IPR017788'', ''IPR022864'', ''IPR055199'', ''IPR027417''].
    Complete relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY annotations
    read; native references do not imply every linked primary body was read. hda primary
    name and idaB/yfgE aliases support the intended K12 example; Hda-TrfA annotation
    and Hda-beta-clamp state do not make TrfA or beta constitutive members of the
    separately scoped binary record.'
  snapshot_sha256: 426a92b935654ddf255d7bb462d2bd0bce6ab02033aed38b8e324916751c0b1d
- evidence_id: micro-gene-dnaA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-dnaA.raw
  accessed_at: '2026-11-04T07:06:58.307038Z'
  support: supports
  summary: Current bounded query returns ['P03004']; primary gene/locus/status/taxon
    inspected. The hupA/hupB results are contextual dimer alternatives for dataset
    selection, not required new maintained examples. No historical-query reconstruction.
  snapshot_sha256: 3db63cf0e2bda46f5e0d2292b32f98621aa2da23fba568a428d8ad2f1fb148a0
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T07:06:58.307038Z; requested size100; complete returned singleton
    page, reviewed:true and organism_id:83333. Current exact-gene query only, not
    universal or retrospective uniqueness.
- evidence_id: micro-gene-hda
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-hda.raw
  accessed_at: '2026-11-04T07:06:57.085056Z'
  support: supports
  summary: Current bounded query returns ['P69931']; primary gene/locus/status/taxon
    inspected. The hupA/hupB results are contextual dimer alternatives for dataset
    selection, not required new maintained examples. No historical-query reconstruction.
  snapshot_sha256: eb8af1bf9d21c98c3becc40e269fbb9fd003455df2925d8b91c12c8d659df4c1
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T07:06:57.085056Z; requested size100; complete returned singleton
    page, reviewed:true and organism_id:83333. Current exact-gene query only, not
    universal or retrospective uniqueness.
- evidence_id: micro-gene-hupA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-hupA.raw
  accessed_at: '2026-11-04T07:07:01.107430Z'
  support: supports
  summary: Current bounded query returns ['P0ACF0']; primary gene/locus/status/taxon
    inspected. The hupA/hupB results are contextual dimer alternatives for dataset
    selection, not required new maintained examples. No historical-query reconstruction.
  snapshot_sha256: f5131b360ffafed8326ba4a6f8e49aa8075273ef04bdd0fe77f4fd2f9a8a6244
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T07:07:01.107430Z; requested size100; complete returned singleton
    page, reviewed:true and organism_id:83333. Current exact-gene query only, not
    universal or retrospective uniqueness.
- evidence_id: micro-gene-hupB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-hupB.raw
  accessed_at: '2026-11-04T07:07:01.265635Z'
  support: supports
  summary: Current bounded query returns ['P0ACF4']; primary gene/locus/status/taxon
    inspected. The hupA/hupB results are contextual dimer alternatives for dataset
    selection, not required new maintained examples. No historical-query reconstruction.
  snapshot_sha256: f6f7f2b99d298b9b720156fbf955840feedd854accfe6be153ab49ce49b73b18
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T07:07:01.265635Z; requested size100; complete returned singleton
    page, reviewed:true and organism_id:83333. Current exact-gene query only, not
    universal or retrospective uniqueness.
- evidence_id: micro-gene-rplB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArplB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact reviewed-gene/taxon page; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/gene-rplB.raw
  accessed_at: '2026-11-04T07:06:56.270736Z'
  support: supports
  summary: Current bounded query returns ['P60422']; primary gene/locus/status/taxon
    inspected. The hupA/hupB results are contextual dimer alternatives for dataset
    selection, not required new maintained examples. No historical-query reconstruction.
  snapshot_sha256: b4879a4491bd613c1c0190874e0810276121bc3e0015189b706538f3cba944c2
  search_scope: UniProtKB literal URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ArplB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100;
    actual 2026-11-04T07:06:56.270736Z; requested size100; complete returned singleton
    page, reviewed:true and organism_id:83333. Current exact-gene query only, not
    universal or retrospective uniqueness.
- evidence_id: micro-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/tax-562.raw
  accessed_at: '2026-11-04T07:06:54.469071Z'
  support: supports
  summary: '562: Escherichia coli; rank species. Species562 is distinct from K12 reference-strain83333;
    this does not identify an unread experimental strain.'
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Exact taxonomy scientific name/rank/lineage; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-04T07:06:54.578588Z'
  support: supports
  summary: '83333: Escherichia coli K-12; rank strain. Species562 is distinct from
    K12 reference-strain83333; this does not identify an unread experimental strain.'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro-go-0006270
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006270
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-0006270.raw
  accessed_at: '2026-11-04T07:06:54.523876Z'
  support: supports
  summary: 'GO:0006270: DNA replication initiation; obsolete=False; definition {''text'':
    ''The process in which DNA-dependent DNA replication is started; it begins when
    specific sequences, known as origins of replication, are recognized and bound
    by the origin recognition complex, followed by DNA unwinding.'', ''xrefs'': [{''dbCode'':
    ''PMID'', ''dbId'': ''28209641''}]}. Native wording is tested against primary
    scope, not treated as infallible experiment evidence.'
  snapshot_sha256: e0ea96216a022971fca313127bdae0280af832afc23734001e734b67973c6601
- evidence_id: micro-go-0032297
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032297
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-0032297.raw
  accessed_at: '2026-11-04T07:06:54.525597Z'
  support: supports
  summary: 'GO:0032297: negative regulation of DNA-templated DNA replication initiation;
    obsolete=False; definition {''text'': ''Any process that stops, prevents, or reduces
    the frequency, rate or extent of initiation of DNA-dependent DNA replication.''}.
    Native wording is tested against primary scope, not treated as infallible experiment
    evidence.'
  snapshot_sha256: c73376493ff3e2bc86db2af907d7e2ff2b05b7188137d4a20fdc6ef7376bf876
- evidence_id: micro-go-1990077
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990077
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990077.raw
  accessed_at: '2026-11-04T07:06:53.819694Z'
  support: supports
  summary: 'GO:1990077: primosome complex; obsolete=False; definition {''text'': ''Any
    of a family of protein complexes that form at the origin of replication or stalled
    replication forks and function in replication primer synthesis in all organisms.
    Early complexes initiate double-stranded DNA unwinding. The core unit consists
    of a replicative helicase and a primase. The helicase further unwinds the DNA
    and recruits the polymerase machinery. The primase synthesizes RNA primers that
    act as templates for complementary stand replication by the polymerase machinery.
    The primosome contains a number of associated proteins and protein complexes and
    contributes to the processes of replication initiation, lagging strand elongation,
    and replication restart.'', ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''21856207''}]}.
    Native wording is tested against primary scope, not treated as infallible experiment
    evidence.'
  snapshot_sha256: 39e7c5542064bdf7ca68df76b5b42c8671196b04198bdef4a2b74fe51729070f
- evidence_id: micro-go-1990078
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990078
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990078.raw
  accessed_at: '2026-11-04T07:06:53.853399Z'
  support: supports
  summary: 'GO:1990078: replication inhibiting complex; obsolete=False; definition
    {''text'': ''A protein complex that inhibits multiple events of replication initiation
    during one replication cycle.'', ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'':
    ''21708944''}]}. Native wording is tested against primary scope, not treated as
    infallible experiment evidence.'
  snapshot_sha256: 08c3d556dd3deeb3ca44662a13f9a1ec91fe795e9c1f611da59b212e417f7be7
- evidence_id: micro-go-1990082-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990082/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990082-ancestors.raw
  accessed_at: '2026-11-04T07:07:57.503569Z'
  support: supports
  summary: Ancestors ['GO:1990078', 'GO:1990082', 'GO:0032991', 'GO:0005575']; children
    None. Exact parent classes checked without substituting parthood.
  snapshot_sha256: e272e7478a8dcf0f669064e2d1368ff0d2282a2872df7abbc7ad829d779cbe9e
- evidence_id: micro-go-1990082-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990082/constraints
  locator: Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990082-constraints.raw
  accessed_at: '2026-11-04T07:07:57.512050Z'
  support: context_only
  summary: 'Current taxonConstraints [{''ancestorId'': ''GO:1990082'', ''ancestorName'':
    ''DnaA-L2 complex'', ''relationship'': ''only_in_taxon'', ''taxId'': ''131567'',
    ''taxIdType'': ''NCBITaxon'', ''taxName'': ''cellular organisms''}]; this is ontology
    scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist
    rows are not used.'
  snapshot_sha256: d6e233dc3c385266a5753ebd8135ef6d9c097f0eb41f4ed520da09d01ee1a7ca
- evidence_id: micro-go-1990082
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990082
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990082.raw
  accessed_at: '2026-11-04T07:06:53.810846Z'
  support: supports
  summary: 'GO:1990082: DnaA-L2 complex; obsolete=False; definition {''text'': ''A
    protein complex that inhibits unwinding of DNA at the origin of replication and
    assembly of the pre-primosome. In E. coli, this complex is composed of DnaA and
    of the ribosomal protein L2.'', ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''21288885''}]}.
    Native wording is tested against primary scope, not treated as infallible experiment
    evidence.'
  snapshot_sha256: af8f29fc2f5620ab6ffef58356d67a3a94544389ceca61a0907834280993a248
- evidence_id: micro-go-1990083-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990083-ancestors.raw
  accessed_at: '2026-11-04T07:07:57.142414Z'
  support: supports
  summary: Ancestors ['GO:1990078', 'GO:1990083', 'GO:0032991', 'GO:0005575']; children
    None. Exact parent classes checked without substituting parthood.
  snapshot_sha256: e81bfbf274efd5ccb3b50567d9d897c45c85f66a5c9a36cfc594b04a9dab927f
- evidence_id: micro-go-1990083-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083/constraints
  locator: Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990083-constraints.raw
  accessed_at: '2026-11-04T07:07:57.154116Z'
  support: context_only
  summary: 'Current taxonConstraints [{''ancestorId'': ''GO:1990083'', ''ancestorName'':
    ''DnaA-Hda complex'', ''relationship'': ''only_in_taxon'', ''taxId'': ''131567'',
    ''taxIdType'': ''NCBITaxon'', ''taxName'': ''cellular organisms''}]; this is ontology
    scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist
    rows are not used.'
  snapshot_sha256: bdead7778d39cd2467b2b48b37f5754f41b9c213f7c0865c9bc105f450dac3ee
- evidence_id: micro-go-1990083
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990083.raw
  accessed_at: '2026-11-04T07:06:53.812912Z'
  support: supports
  summary: 'GO:1990083: DnaA-Hda complex; obsolete=False; definition {''text'': ''A
    protein complex that inactivates the function of DnaA by inhibiting the phosphorylation
    of DnaA-ADP to DnaA-ATP and thereby preventing multiple events of replication
    initiation. In E. coli, this complex is composed of DnaA and Hda.'', ''xrefs'':
    [{''dbCode'': ''PMID'', ''dbId'': ''21708944''}]}. Native wording is tested against
    primary scope, not treated as infallible experiment evidence.'
  snapshot_sha256: d2f85f0916eaaed8c29b3898467c57d9f17770b9f5e1017b8069735db70f4e6b
- evidence_id: micro-go-1990084
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990084
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990084.raw
  accessed_at: '2026-11-04T07:06:53.875463Z'
  support: supports
  summary: 'GO:1990084: DnaA-Dps complex; obsolete=False; definition {''text'': ''A
    protein complex that negatively regulates strand-opening at the origin of replication,
    thereby interfering with replication initiation. This complex is thought to be
    involved in the regulation of replication under oxidative stress conditions. In
    E. coli, this complex is composed of DnaA and Dps.'', ''xrefs'': [{''dbCode'':
    ''PMID'', ''dbId'': ''18284581''}]}. Native wording is tested against primary
    scope, not treated as infallible experiment evidence.'
  snapshot_sha256: 5c43d23aa7d8f548db894874fdd4e2588e0fab86debbc23fffebc499dbe23958
- evidence_id: micro-go-1990085
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990085
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990085.raw
  accessed_at: '2026-11-04T07:06:53.847746Z'
  support: supports
  summary: 'GO:1990085: Hda-beta clamp complex; obsolete=False; definition {''text'':
    ''A protein complex involved in inactivating the function of DnaA and thereby
    preventing multiple events of replication initiation. In E. coli, this complex
    is composed of the beta clamp (DnaN) and Hda.'', ''xrefs'': [{''dbCode'': ''PMID'',
    ''dbId'': ''15150238''}]}. Native wording is tested against primary scope, not
    treated as infallible experiment evidence.'
  snapshot_sha256: e0af87ab4d38b582534f2aaf03bf33758e35d33e546d1607bd6b93477ed6570e
- evidence_id: micro-go-1990100
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990100
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990100.raw
  accessed_at: '2026-11-04T07:06:53.861422Z'
  support: supports
  summary: 'GO:1990100: DnaB-DnaC complex; obsolete=False; definition {''text'': ''A
    protein complex containing homohexameric DNA helicase DnaB, and the DNA helicase
    loader DnaC. The helicase loader DnaC delivers DnaB to the chromosomal origin
    (oriC).'', ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''20129058''}]}. Native
    wording is tested against primary scope, not treated as infallible experiment
    evidence.'
  snapshot_sha256: 14aade75f1106c27c76f8328692e6163b9f5747df82f2666322cb2f7b668725d
- evidence_id: micro-go-1990101-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990101-ancestors.raw
  accessed_at: '2026-11-04T07:07:57.502553Z'
  support: supports
  summary: Ancestors ['GO:1990101', 'GO:0032993', 'GO:0032991', 'GO:0005575', 'GO:1990077'];
    children None. Exact parent classes checked without substituting parthood.
  snapshot_sha256: 67b1fcf7f9ce58ca2995e5f9156effc38c6f4c9fc81649785df7506851289a11
- evidence_id: micro-go-1990101-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101/constraints
  locator: Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990101-constraints.raw
  accessed_at: '2026-11-04T07:07:57.636505Z'
  support: context_only
  summary: 'Current taxonConstraints [{''ancestorId'': ''GO:1990101'', ''ancestorName'':
    ''DnaA-oriC complex'', ''relationship'': ''only_in_taxon'', ''taxId'': ''2, 2157'',
    ''taxIdType'': ''NCBITaxon_Union'', ''taxName'': ''Prokaryota''}]; this is ontology
    scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist
    rows are not used.'
  snapshot_sha256: 718f91ab3c11f3a5914d0fe33dacac94c1900061be31ecf08c05ba76132a44d8
- evidence_id: micro-go-1990101
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990101
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990101.raw
  accessed_at: '2026-11-04T07:06:53.812856Z'
  support: supports
  summary: 'GO:1990101: DnaA-oriC complex; obsolete=False; definition {''text'': ''A
    protein-DNA complex containing the initiator protein DnaA bound to high-affinity
    recognition sites in the unique origin of replication, oriC. DnaA-oriC binding
    is the first step in assembly of a bacterial pre-replicative complex (pre-RC)
    and is responsible for the timely initiation of replication once per cell cycle.'',
    ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''19833870''}]}. Native wording is
    tested against primary scope, not treated as infallible experiment evidence.'
  snapshot_sha256: 0a23d28413a48d3195664bac9a2d0f0c0fd55fb4be3062eddcc3561867fc4342
- evidence_id: micro-go-1990102
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990102
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990102.raw
  accessed_at: '2026-11-04T07:06:54.324507Z'
  support: supports
  summary: 'GO:1990102: DnaA-DiaA complex; obsolete=False; definition {''text'': ''A
    protein-DNA complex containing a tetramer of DiaA attached to multiple DnaA molecule
    bound to oriC DNA. Regulates timely initiation of chromosomal replication during
    the cell cycle by stimulating assembly of DnaA-oriC complexes, conformational
    changes in ATP-DnaA initiation complexes, and unwinding of oriC duplex DNA.'',
    ''xrefs'': [{''dbCode'': ''PMID'', ''dbId'': ''15326179''}, {''dbCode'': ''PMID'',
    ''dbId'': ''17699754''}]}. Native wording is tested against primary scope, not
    treated as infallible experiment evidence.'
  snapshot_sha256: dabec07dbf0f550e085d5eca8f679ec7c974d9f3b7d0c402c801e8ca02876715
- evidence_id: micro-go-1990103-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103/ancestors?relations=is_a
  locator: Complete explicit is_a-only ancestor response and typed children; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990103-ancestors.raw
  accessed_at: '2026-11-04T07:07:57.225300Z'
  support: supports
  summary: Ancestors ['GO:1990103', 'GO:0032993', 'GO:0032991', 'GO:0005575', 'GO:1990077'];
    children None. Exact parent classes checked without substituting parthood.
  snapshot_sha256: 2562e1a1ee8dd4fd7da2eed33e9cb7df10252d44a9adefd6ce96da61f226b2e7
- evidence_id: micro-go-1990103-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103/constraints
  locator: Exact taxonConstraints field only; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990103-constraints.raw
  accessed_at: '2026-11-04T07:07:57.452835Z'
  support: context_only
  summary: 'Current taxonConstraints [{''ancestorId'': ''GO:1990103'', ''ancestorName'':
    ''DnaA-HU complex'', ''relationship'': ''only_in_taxon'', ''taxId'': ''2, 2157'',
    ''taxIdType'': ''NCBITaxon_Union'', ''taxName'': ''Prokaryota''}]; this is ontology
    scope, not an experimental survey or actual strain identification. Unrelated constraint-blacklist
    rows are not used.'
  snapshot_sha256: 58077ff267c85308363e28e8aa72c6472934df2d3fe7a9f7b9898997ded5ac8a
- evidence_id: micro-go-1990103
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990103
  locator: Exact active identity/definition/synonyms and typed children; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/go-1990103.raw
  accessed_at: '2026-11-04T07:06:53.840784Z'
  support: supports
  summary: 'GO:1990103: DnaA-HU complex; obsolete=False; definition {''text'': ''A
    protein-DNA complex containing DNA-bound DnaA attached to HU. HU is a dimer encoded
    by two closely related genes. Essential for the initiation of replication in bacteria;
    stimulates the DnaA-dependent unwinding of oriC.'', ''xrefs'': [{''dbCode'': ''PMID'',
    ''dbId'': ''18179598''}]}. Native wording is tested against primary scope, not
    treated as infallible experiment evidence.'
  snapshot_sha256: 433297d5c7b21f84956999f2541404720751083b9bf905f22cd353f5bf4d6017
- evidence_id: micro-ipr-IPR001957
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001957/
  locator: Complete native name/type/hierarchy/integrated signatures/description flags;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR001957.raw
  accessed_at: '2026-11-04T07:06:54.615440Z'
  support: supports
  summary: 'IPR001957: {''name'': ''Chromosomal replication control, initiator DnaA'',
    ''short'': ''Chromosome_initiator_DnaA''}; type family; signatures {''hamap'':
    {''MF_00377'': ''Chromosomal replication initiator protein DnaA [dnaA]''}, ''ncbifam'':
    {''TIGR00362'': ''chromosomal replication initiator protein DnaA''}}. Native whole-family
    type, integrated signatures, hierarchy and description inspected; separate maintained-example
    xrefs independently corroborate scope. No domain or homologous-superfamily substitution.'
  snapshot_sha256: 364ea5ab4304d290b099574c7f9527e5577eefec2872f8fc2adde34de7eb2fc2
- evidence_id: micro-ipr-IPR017788
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/
  locator: Complete native name/type/hierarchy/integrated signatures/description flags;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR017788.raw
  accessed_at: '2026-11-04T07:06:54.617868Z'
  support: supports
  summary: 'IPR017788: {''name'': ''DnaA regulatory inactivator Hda'', ''short'':
    ''Hda''}; type family; signatures {''ncbifam'': {''TIGR03420'': ''DnaA regulatory
    inactivator Hda''}}. Native whole-family type, integrated signatures, hierarchy
    and description inspected; separate maintained-example xrefs independently corroborate
    scope. No domain or homologous-superfamily substitution.'
  snapshot_sha256: 7e9d3b5937bd2091b11b482deda5c5328592a0121f84c369e97a6ba8390abb6c
- evidence_id: micro-ipr-IPR022864
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/
  locator: Complete native name/type/hierarchy/integrated signatures/description flags;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR022864.raw
  accessed_at: '2026-11-04T07:06:54.675461Z'
  support: supports
  summary: 'IPR022864: {''name'': ''DnaA regulatory inactivator Hda, Enterobacteriaceae'',
    ''short'': ''Hda_Enterobact''}; type family; signatures {''hamap'': {''MF_01158'':
    ''DnaA regulatory inactivator Hda [hda]''}}. Native whole-family type, integrated
    signatures, hierarchy and description inspected; separate maintained-example xrefs
    independently corroborate scope. No domain or homologous-superfamily substitution.
    Enterobacteriaceae Hda is narrower than generic Hda IPR017788.'
  snapshot_sha256: a3300bce98be51679d5018b6ad7ad5dc4ad5108f0c7c19c006f084c8f43425f0
- evidence_id: micro-ipr-IPR005880
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005880/
  locator: Complete native name/type/hierarchy/integrated signatures/description flags;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR005880.raw
  accessed_at: '2026-11-04T07:06:54.601199Z'
  support: supports
  summary: 'IPR005880: {''name'': ''Large ribosomal subunit protein uL2, bacteria/organella'',
    ''short'': ''Ribosomal_uL2_bact_org''}; type family; signatures {''hamap'': {''MF_01320_B'':
    ''Large ribosomal subunit protein uL2 [rplB]''}, ''ncbifam'': {''TIGR01171'':
    ''50S ribosomal protein L2''}}. Native whole-family type, integrated signatures,
    hierarchy and description inspected; separate maintained-example xrefs independently
    corroborate scope. No domain or homologous-superfamily substitution. Bacterial/organellar
    uL2 class is narrower than universal uL2 IPR002171 and fits the declared 50S-L2
    component.'
  snapshot_sha256: c58dd4e4e903ecf8063de5273531584ac284ddad6ec4d866d77da625631d94a5
- evidence_id: micro-ipr-IPR002171-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002171/
  locator: Complete native name/type/hierarchy/integrated signatures/description flags;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR002171-retry.raw
  accessed_at: '2026-11-04T07:07:57.186742Z'
  support: supports
  summary: 'IPR002171: {''name'': ''Large ribosomal subunit protein uL2'', ''short'':
    ''Ribosomal_uL2''}; type family; signatures {''pirsf'': {''PIRSF002158'': ''Ribosomal
    protein, L2p/L2a/L8e/organellar L2 types''}, ''panther'': {''PTHR13691'': ''RIBOSOMAL
    PROTEIN L2''}}. Native whole-family type, integrated signatures, hierarchy and
    description inspected; separate maintained-example xrefs independently corroborate
    scope. No domain or homologous-superfamily substitution. Universal parent has
    distinct bacteria/organella and archaea/eukaryota child families. Broader parent
    is not silently substituted for the explicit bacterial/organellar class.'
  snapshot_sha256: 6256eb79c52c2351405c9ff6f097004a12a8637185c00a54f2fe87623deabcdb
- evidence_id: micro-so-0000953
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/so/terms?obo_id=SO%3A0000953
  locator: Complete exact OLS term identity/definition/obsolete flag; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/so-0000953.raw
  accessed_at: '2026-11-04T07:06:54.935989Z'
  support: supports
  summary: 'Active oriC feature class: an origin of bacterial chromosome replication.
    Exact source-neutral scaffold class, not a single strain origin sequence.'
  snapshot_sha256: ef6519c66754a488b20d7720b774efff30553619a8d431fb75a6caa9667756dd
- evidence_id: micro-pmid-12618445
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12618445%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-12618445.raw
  accessed_at: '2026-11-04T07:06:56.804917Z'
  support: supports
  summary: '12618445: Identification of a novel membrane-associated gene product that
    suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship to
    the DnaA host initiation protein.; DOI 10.1128/jb.185.6.1817-1824.2003. Complete
    primary abstract read; this response alone does not certify full methods, source
    strain, figure pixels or supplements.'
  snapshot_sha256: 3fb10a34d2c2e076298ac23addce2277f5d50180ee3c7a00c14153252375d395
- evidence_id: micro-pmid-15150238
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15150238%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-15150238.raw
  accessed_at: '2026-11-04T07:06:55.569286Z'
  support: supports
  summary: '15150238: Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related
    protein.; DOI 10.1128/jb.186.11.3508-3515.2004. Complete primary abstract read;
    this response alone does not certify full methods, source strain, figure pixels
    or supplements.'
  snapshot_sha256: 172a39c1decf7071850da52fd439c228fc3dc383641bb40599cbe102af0e9fd5
- evidence_id: micro-pmid-18179598
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18179598%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-18179598.raw
  accessed_at: '2026-11-04T07:06:55.711819Z'
  support: supports
  summary: '18179598: Escherichia coli DnaA interacts with HU in initiation at the
    E. coli replication origin.; DOI 10.1111/j.1365-2958.2007.06094.x. Complete primary
    abstract read; this response alone does not certify full methods, source strain,
    figure pixels or supplements.'
  snapshot_sha256: 191edbd19eaead5d06bc5a816797b597420451d9ce33c7446d596eebc0a7756d
- evidence_id: micro-pmid-19833870
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:19833870%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-19833870.raw
  accessed_at: '2026-11-04T07:06:56.181907Z'
  support: supports
  summary: '19833870: Bacterial origin recognition complexes direct assembly of higher-order
    DnaA oligomeric structures.; DOI 10.1073/pnas.0909472106. Complete primary abstract
    read; this response alone does not certify full methods, source strain, figure
    pixels or supplements.'
  snapshot_sha256: f43be6d64081917dc470114814b4074f2218f98de054c1c371aec9ab1cd934de
- evidence_id: micro-pmid-21288885
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21288885%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-21288885.raw
  accessed_at: '2026-11-04T07:06:56.007749Z'
  support: supports
  summary: '21288885: Two forms of ribosomal protein L2 of Escherichia coli that inhibit
    DnaA in DNA replication.; DOI 10.1093/nar/gkq1203. Complete primary abstract read;
    this response alone does not certify full methods, source strain, figure pixels
    or supplements.'
  snapshot_sha256: b9355f9299515638ef84641d449ed90f2f52be2d228601ceaec2d77b17943386
- evidence_id: micro-pmid-21708944
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21708944%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-21708944.raw
  accessed_at: '2026-11-04T07:06:55.281083Z'
  support: supports
  summary: '21708944: DnaA protein DNA-binding domain binds to Hda protein to promote
    inter-AAA+ domain interaction involved in regulatory inactivation of DnaA.; DOI
    10.1074/jbc.m111.233403. Complete primary abstract read; this response alone does
    not certify full methods, source strain, figure pixels or supplements.'
  snapshot_sha256: e366c38c9033b11d926d13447494b73ddc2c45c0bab67b2ba83afd19739f8da6
- evidence_id: micro-pmid-22574163
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22574163%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-22574163.raw
  accessed_at: '2026-11-04T07:06:56.310353Z'
  support: supports
  summary: '22574163: Association of the chromosome replication initiator DnaA with
    the Escherichia coli inner membrane in vivo: quantity and mode of binding.; DOI
    10.1371/journal.pone.0036441. Complete primary abstract read; this response alone
    does not certify full methods, source strain, figure pixels or supplements.'
  snapshot_sha256: 3f8e6cf736bae4a359c4f0bdfbe99616714f9ddab7a4636d401c42a3edb7fa57
- evidence_id: micro-pmid-28166228
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:28166228%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-28166228.raw
  accessed_at: '2026-11-04T07:06:56.619245Z'
  support: supports
  summary: '28166228: Rapid turnover of DnaA at replication origin regions contributes
    to initiation control of DNA replication.; DOI 10.1371/journal.pgen.1006561. Complete
    primary abstract read; this response alone does not certify full methods, source
    strain, figure pixels or supplements.'
  snapshot_sha256: 2052dbc0e07dc95722363191599ca0682a8cd6b9b9cbb05a0ba1fc529cd442cb
- evidence_id: micro-pmid-9478970
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:9478970%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Complete exact MED metadata and deposited primary-study abstract; exact
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/pmid-9478970.raw
  accessed_at: '2026-11-04T07:06:56.662967Z'
  support: supports
  summary: '9478970: Membrane-mediated release of nucleotide from an initiator of
    chromosomal replication, Escherichia coli DnaA, occurs with insertion of a distinct
    region of the protein into the lipid bilayer.; DOI 10.1074/jbc.273.9.5167. Complete
    primary abstract read; this response alone does not certify full methods, source
    strain, figure pixels or supplements.'
  snapshot_sha256: d266d48e7047c10c1686b3507d839210f5c39073dfa4e9f40e455e926dced425
- evidence_id: micro-keyamura2011-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3190739/
  locator: Genuine PMC3190739 HTML; complete Introduction/Experimental Procedures/Results/Discussion,
    Table1 and Fig1–7 text captions; extracted P20 strains, P23 staged RIDA, P26–27
    contact assays, P37 Fig2, P45–49 pulldown/SPR, P54 DARS, P68–75 discussion; no
    pixels/supplements; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/keyamura2011-pmc.raw
  accessed_at: '2026-11-04T07:07:56.846867Z'
  support: supports
  summary: K12-derived strains and purified/reconstituted DNA-loaded-clamp/ADP-Hda
    system support DnaA-bound ATP hydrolysis to ADP, not phosphorylation inhibition.
    DARS reactivation uses exchange as cited background. Mutant contact/RIDA effects
    and weak clamp-free SPR support interaction; precise clamp-free kinetics were
    not measurable at tested concentrations. Proposed structural model is not a solved
    cocrystal; binary identity is distinct from full active RIDA machinery.
  snapshot_sha256: b5bda5bcb882e86f35610cb65f93b4eb9f75ec40dc4a2718c9ea2cc03a2aa488
- evidence_id: micro-chodavarapu2011-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3105425.1/PMC3105425.1.xml
  locator: Genuine PMC3105425 JATS; complete Introduction/Materials and Methods/Results/Discussion
    and Fig1–8 text captions; extracted P10/26 source strains, P20 binding, P22/54/57
    prepriming, P44 unwinding, P46 ATP, P50 contact, P61/68 physiological limits;
    no pixels/supplements; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/chodavarapu2011-jats.raw
  accessed_at: '2026-11-04T07:07:57.073382Z'
  support: supports
  summary: Purified mature/truncated L2 contacts the DnaA N terminus and inhibits
    oriC unwinding and prepriming assembly in vitro; reduced retained DnaA/DnaB supports
    proposed oligomer destabilization, not a solved interface. tL2 preparation from
    DM700 is not synonymous with K12 reference accession. Physiological regulation
    remains proposed; tested tL2 in-vivo initiation assay was negative under its conditions,
    not universal disproval.
  snapshot_sha256: 8de431108de72c720992f2bea31c9899b5d695e8e7d41b067555bfa0006b8265
- evidence_id: micro-miller2009-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2773971/
  locator: Genuine PMC2773971 HTML; complete Introduction/Results/Discussion/Methods
    and Fig1–6 text captions; extracted P21–37 affinity/mutant assembly assays, P48
    strains, P52 DMS, P54 crosslink, P56 EMSA; no pixels/raw footprint reanalysis;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/miller2009-pmc.raw
  accessed_at: '2026-11-04T07:07:56.868305Z'
  support: supports
  summary: High-affinity oriC sites assist DnaA assembly at low-affinity sites in
    E.coli; P3478/W3110 and PC2 dnaCts contexts and purified proteins are distinguished.
    At elevated DnaA, weak-site filling can occur despite mutated high-affinity sites.
    Crosslinks/footprints and model support bounded seeding/oligomerization, not a
    universal absence or exact stoichiometric claim.
  snapshot_sha256: 3f1a9d25be75c7b16421560d435f9729779af83b6ed9c56c71fba7635f077f11
- evidence_id: micro-keyamura2011-jats-access
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3190739.1/PMC3190739.1.xml
  locator: Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/keyamura2011-jats.raw
  accessed_at: '2026-11-04T07:07:56.867858Z'
  support: context_only
  summary: HTTP404 diagnostic only. No blocked body or unavailable authority metadata
    certified; separate successful body/authority or complete abstract is explicitly
    identified.
  snapshot_sha256: 2c5bd182c025a695b77cc6a0ebf5e0f6965e7ca63c804533a1589c5eae11e11a
- evidence_id: micro-miller2009-jats-access
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2773971.1/PMC2773971.1.xml
  locator: Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/miller2009-jats.raw
  accessed_at: '2026-11-04T07:07:56.862764Z'
  support: context_only
  summary: HTTP404 diagnostic only. No blocked body or unavailable authority metadata
    certified; separate successful body/authority or complete abstract is explicitly
    identified.
  snapshot_sha256: ae028c217b67d962433f5bc66a03c2735a7bc3d1b3bbf4fd2c634ab4f2072f7a
- evidence_id: micro-chodavarapu2008-publisher-access
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2007.06094.x
  locator: Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/chodavarapu2008-publisher.raw
  accessed_at: '2026-11-04T07:07:56.625245Z'
  support: context_only
  summary: HTTP403 diagnostic only. No blocked body or unavailable authority metadata
    certified; separate successful body/authority or complete abstract is explicitly
    identified.
  snapshot_sha256: d17828b27af3d826f546823323aa0dace89eb116de182028d59607e87807eb47
- evidence_id: micro-chodavarapu2008-pdf-access
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1365-2958.2007.06094.x
  locator: Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/chodavarapu2008-pdf.raw
  accessed_at: '2026-11-04T07:07:56.574064Z'
  support: context_only
  summary: HTTP403 diagnostic only. No blocked body or unavailable authority metadata
    certified; separate successful body/authority or complete abstract is explicitly
    identified.
  snapshot_sha256: 404f94cff4e5466bcc7a2f61e5663845eda8edf2f68b9493a086af20d9770be4
- evidence_id: micro-ipr-IPR002171-access
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002171/
  locator: Actual retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ipr-IPR002171.raw
  accessed_at: '2026-11-04T07:06:54.617949Z'
  support: context_only
  summary: HTTP429 diagnostic only. No blocked body or unavailable authority metadata
    certified; separate successful body/authority or complete abstract is explicitly
    identified.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-historical-0-keyamura2011-legacy-access
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3190739/
  locator: Retained failed/challenge route
  accessed_at: '2026-10-22T05:53:59.700989Z'
  support: context_only
  summary: Legacy HTTP200 returned a reCAPTCHA challenge, not the paper. Historical
    original-observation time/hash retained, not freshly fetched or claimed as a renewed
    raw-response read. Original honestly admitted access limitations; successor corrects
    classification only to validation/context_only.
  snapshot_sha256: a174414fa66636d2fc2c092b7be9cbd7570dc05fd40d2bec4e03d2e2f6a62c30
- evidence_id: micro-historical-0-keyamura2011-xml-access
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3190739/fullTextXML
  locator: Retained failed/challenge route
  accessed_at: '2026-10-22T05:55:00.428545Z'
  support: context_only
  summary: EuropePMC fullTextXML route returned500; the separate modern PMC HTML supplied
    the genuine body. Historical original-observation time/hash retained, not freshly
    fetched or claimed as a renewed raw-response read. Original honestly admitted
    access limitations; successor corrects classification only to validation/context_only.
  snapshot_sha256: 65650040210570c95714538412d01052ede574689048a0655cb16319c4acd2bc
- evidence_id: micro-historical-1-chodavarapu2008-publisher-access
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2958.2007.06094.x
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:55:00.599052Z'
  support: context_only
  summary: Publisher route did not provide the article body; the complete native abstract
    was read. Historical original-observation time/hash retained, not freshly fetched
    or claimed as a renewed raw-response read. Original honestly admitted access limitations;
    successor corrects classification only to validation/context_only.
  snapshot_sha256: 9683d5783baca9e62308c11ca86bce1e5bf5ecabc55f4ae3ba70882177d3fcfe
- evidence_id: micro-historical-1-chodavarapu2008-pdf-access
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1365-2958.2007.06094.x
  locator: Retained publisher403 response
  accessed_at: '2026-10-22T05:55:00.606412Z'
  support: context_only
  summary: Publisher route did not provide the article body; the complete native abstract
    was read. Historical original-observation time/hash retained, not freshly fetched
    or claimed as a renewed raw-response read. Original honestly admitted access limitations;
    successor corrects classification only to validation/context_only.
  snapshot_sha256: 15a617a9c8c61d6f04b2cb06aa6cdfa1309d82d63501b24dccd0a9c1cf42540d
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official20-organism catalogue and every returned dataset entry;
    exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T07:06:53.166338Z'
  support: supports
  summary: E.coli has actual precise1k coverage among listed datasets. This is bounded
    current catalogue scope, not universal or future coverage.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB GET /api/datasets at 2026-11-04T07:06:53.166338Z; all20
    organism rows and every returned dataset entry; no pagination/truncation. Exact
    E.coli host match, no foreign-host proxy.
- evidence_id: micro-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete selected precise1k metadata and five-strain list; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T07:06:53.737977Z'
  support: context_only
  summary: Dataset contains BW25113,DGF-298,GMOS,MG1655,W3110;1035 samples,518 conditions,201
    modules,4257 genes. Mixed K12-related strains are not identical to every Keyamura
    mutant, DM700 preparation or Miller assay strain; source-specific experiments
    remain independently scoped.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-ecoli-modules
  kind: search
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 returned module names/regulators/functions; exact response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T07:06:53.119675Z'
  support: context_only
  summary: Complete selected module inventory inspected; computational labels do not
    demonstrate direct regulation or physical complex formation.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: iModulonDB e_coli/precise1k module inventory at 2026-11-04T07:06:53.119675Z;
    all201 returned entries, selected dataset only, no activity contrasts or all-dataset
    absence claim.
- evidence_id: micro-ecoli-gene-b3702
  kind: search
  reference: https://imodulondb.org/api/genes/b3702/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus membership/weight/threshold rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b3702.raw
  accessed_at: '2026-11-04T07:07:57.118629Z'
  support: context_only
  summary: 'b3702: []. Zero thresholded memberships do not mean absence or dispensability;
    a positive expression module does not prove binding, assembly or direct regulation.'
  snapshot_sha256: f88e8e1cc78f58e88b8e2e1bce66d3b576f85ac167c41cad5b4030aaf2f333fb
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b3702/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T07:07:57.118629Z; exact native reference locus, all201 rows; selected
    five-strain precise1k only. No historical, all-alias or universal-negative inference.
- evidence_id: micro-ecoli-gene-b2496
  kind: search
  reference: https://imodulondb.org/api/genes/b2496/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus membership/weight/threshold rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b2496.raw
  accessed_at: '2026-11-04T07:07:57.231220Z'
  support: context_only
  summary: 'b2496: []. Zero thresholded memberships do not mean absence or dispensability;
    a positive expression module does not prove binding, assembly or direct regulation.'
  snapshot_sha256: 6a09cbbfc4e76bfb73b1d264e6230d893455b9c1efb1ceae2104d29ff64eabec
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b2496/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T07:07:57.231220Z; exact native reference locus, all201 rows; selected
    five-strain precise1k only. No historical, all-alias or universal-negative inference.
- evidence_id: micro-ecoli-gene-b3317
  kind: search
  reference: https://imodulondb.org/api/genes/b3317/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus membership/weight/threshold rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b3317.raw
  accessed_at: '2026-11-04T07:07:57.243351Z'
  support: context_only
  summary: 'b3317: [{"k": 1, "name": "Translation", "weight": 0.130149946, "threshold":
    0.057970804, "in_imodulon": true}]. Zero thresholded memberships do not mean absence
    or dispensability; a positive expression module does not prove binding, assembly
    or direct regulation.'
  snapshot_sha256: 846f927808d5d324146ac02cbef9ac18eec4b7859bf7468c7930239b3dbc71f1
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b3317/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T07:07:57.243351Z; exact native reference locus, all201 rows; selected
    five-strain precise1k only. No historical, all-alias or universal-negative inference.
- evidence_id: micro-ecoli-gene-b4000
  kind: search
  reference: https://imodulondb.org/api/genes/b4000/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus membership/weight/threshold rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b4000.raw
  accessed_at: '2026-11-04T07:07:57.243324Z'
  support: context_only
  summary: 'b4000: []. Zero thresholded memberships do not mean absence or dispensability;
    a positive expression module does not prove binding, assembly or direct regulation.'
  snapshot_sha256: c2f129a91929e357d58e41e21d86e1320276c99cf0cf27ee4f6b8fbe4f7c68d2
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b4000/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T07:07:57.243324Z; exact native reference locus, all201 rows; selected
    five-strain precise1k only. No historical, all-alias or universal-negative inference.
- evidence_id: micro-ecoli-gene-b0440
  kind: search
  reference: https://imodulondb.org/api/genes/b0440/imodulons?organism=e_coli&dataset=precise1k
  locator: All201 exact-native-locus membership/weight/threshold rows; exact response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-gene-b0440.raw
  accessed_at: '2026-11-04T07:07:57.246468Z'
  support: context_only
  summary: 'b0440: []. Zero thresholded memberships do not mean absence or dispensability;
    a positive expression module does not prove binding, assembly or direct regulation.'
  snapshot_sha256: e6568ac39514051e311c404ed7bc5d3942aaac35217d4fb4ad1940cd7df7297a
  search_scope: iModulonDB literal https://imodulondb.org/api/genes/b0440/imodulons?organism=e_coli&dataset=precise1k
    at 2026-11-04T07:07:57.246468Z; exact native reference locus, all201 rows; selected
    five-strain precise1k only. No historical, all-alias or universal-negative inference.
- evidence_id: micro-adapter-module1
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/1
  locator: 'Independently read same-PR response: actual metadata,53-gene IDs/weights
    and complete member identity columns; rplB full row. AI summary/activity fields
    excluded. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1.raw'
  accessed_at: '2026-11-04T07:09:56.533655Z'
  support: context_only
  summary: Module1 Translation/DksA, ribosome-biogenesis annotation; rplB b3317/P60422
    weight0.130149946 exceeds threshold0.057970804 in complete53-member list. Five-strain
    computational context only, not DnaA-L2 assembly or direct DksA regulation evidence.
    Reused actual fetch timestamp, not a new request.
  snapshot_sha256: fdfaf557fdb00a92cb050f1f802cdf0270fc1ce1b64e892a3ed0ba43cea2dd04
- evidence_id: micro-adapter-module1-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/1/genes
  locator: 'Independently read same-PR response: actual metadata,53-gene IDs/weights
    and complete member identity columns; rplB full row. AI summary/activity fields
    excluded. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1-genes.raw'
  accessed_at: '2026-11-04T07:09:56.621116Z'
  support: context_only
  summary: Module1 Translation/DksA, ribosome-biogenesis annotation; rplB b3317/P60422
    weight0.130149946 exceeds threshold0.057970804 in complete53-member list. Five-strain
    computational context only, not DnaA-L2 assembly or direct DksA regulation evidence.
    Reused actual fetch timestamp, not a new request.
  snapshot_sha256: ea6bfc49819118fe70ec422b827aa521bf064f30cf6ab5362a1195af11303ff0
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907–00:49:00.863225Z receipt
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical runner unavailable/exit1 permission limitation; no fresh invocation.
    Current official API catalogue/gene/module fallback is separately documented.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-dnaa_hda_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:31.455252Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes.
    This validates implemented identity/xref coverage, not exact family grounding
    or full biological completeness.
  snapshot_sha256: d7afb0e7f9cef7173fe65ff2c8c015063a57aee92fa6b663b7a5f970a2494e7c
- evidence_id: micro-native-dnaa_hda_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-causal.log
    SHA256 c1b02a106da2af87da59359f83b31b146fdd3ba83f7f8364b563ee0084a53520
  accessed_at: '2026-11-04T07:05:31.894556Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes.
    This validates implemented identity/xref coverage, not exact family grounding
    or full biological completeness.
  snapshot_sha256: 8289565f4cc76a25ecbb38c50b114209a6d143084aa0112626ad23bf1efc0d20
- evidence_id: micro-native-dnaa_hu_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:32.907561Z'
  support: supports
  summary: Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes;
    HU dimer STRUCTURE node and oriC GENETIC_ELEMENT are outside this typed-protein
    inventory and checked independently. This validates implemented identity/xref
    coverage, not exact family grounding or full biological completeness.
  snapshot_sha256: b4d1a623448f67da318e5cf9f382ef5e960ebc1b11379446cb20dd8d949c0bd8
- evidence_id: micro-native-dnaa_hu_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-causal.log
    SHA256 ca286fe8a9cd7bb445c53da08a7fb8bc6512f82af088da76999eb9dbc8fc6787
  accessed_at: '2026-11-04T07:05:33.340523Z'
  support: supports
  summary: Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes;
    HU dimer STRUCTURE node and oriC GENETIC_ELEMENT are outside this typed-protein
    inventory and checked independently. This validates implemented identity/xref
    coverage, not exact family grounding or full biological completeness.
  snapshot_sha256: d07004c0b46b5f14c8e8822ffe1c094323228a007276d196574424b0b634341e
- evidence_id: micro-native-dnaa_l2_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:35.073354Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes.
    This validates implemented identity/xref coverage, not exact family grounding
    or full biological completeness.
  snapshot_sha256: ea48f793ea93c2a0292307c150c446edaafb37d81a82fee12e89be89fdf9806c
- evidence_id: micro-native-dnaa_l2_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-causal.log
    SHA256 b5af99c8180d083ab55ba1f343531d77f1fddc4e7b84189669a4457b4b36d46a
  accessed_at: '2026-11-04T07:05:35.480019Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples and2 COVERED typed GENE_OR_PROTEIN nodes.
    This validates implemented identity/xref coverage, not exact family grounding
    or full biological completeness.
  snapshot_sha256: 5f67175e79e649fb384fbcc62c816a9d23adf6f3bae8d224a96d319633385624
- evidence_id: micro-native-dnaa_oric_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-verify-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:36.528903Z'
  support: supports
  summary: Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes;
    oriC GENETIC_ELEMENT is checked independently. This validates implemented identity/xref
    coverage, not exact family grounding or full biological completeness.
  snapshot_sha256: 2ee72a11791fa96419bb9d9525cec96438e35ca02c136b5903242cbd72c98088
- evidence_id: micro-native-dnaa_oric_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-causal-receipt.json
  locator: Actual command and complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-causal.log
    SHA256 13807089fc975c18288a1f1c653e3484de53f3588a33d875dda00c8ba20e577e
  accessed_at: '2026-11-04T07:05:36.939971Z'
  support: supports
  summary: Actual exit0; 1 reviewed examples and1 COVERED typed GENE_OR_PROTEIN nodes;
    oriC GENETIC_ELEMENT is checked independently. This validates implemented identity/xref
    coverage, not exact family grounding or full biological completeness.
  snapshot_sha256: 969899b418d888df57b17fe9bcc71377d56d5a0779f3a784b43c0a67272c01c1
- evidence_id: plaque-curation
  kind: authority
  reference: docs/CURATION.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-protein-skill
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-graph-skill
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: plaque-review-contract
  kind: authority
  reference: docs/record-reviews.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: plaque-structure-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-agents
  kind: authority
  reference: AGENTS.md
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
- evidence_id: plaque-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Current frozen policy/schema; relevant component-class, evidence, source
    applicability, graph, history and review-contract sections
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Native review and modelling rules; historical rationale is append-only,
    formation is distinct from viability, optional inventory is not mandatory, and
    expression data are context rather than assembly proof.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: plaque-record-4
  kind: record_content
  reference: data/structures/other/dnab_dnac_complex.yaml
  locator: Complete maintained record including every component, example, graph, discussion
    and history entry
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: supports
  summary: Whole current record independently read; same SHA-256 as the original review
    target input, without staleness or scientific edits.
  snapshot_sha256: 049bf3ed905aec42853fdf025e35d4cb71ecd89a7b8b89328042c39491aaa180
- evidence_id: plaque-original-4-yaml
  kind: prior_review
  reference: reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.yaml
  locator: Complete immutable original; source, checks, scientific assessments, findings,
    actions, limits and notes
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Original historical review; its claims and frozen inputs were independently
    checked. This observation does not treat historical commands as newly executed.
  snapshot_sha256: 643aaee2288fb0858a7dd8484509816f8419bf2b948ada3020e321ec06eb84e8
- evidence_id: plaque-original-4-md
  kind: prior_review
  reference: reviews/structured/20261022T060741Z-dnab-dnac-complex-audit/review.md
  locator: Complete immutable original; source, checks, scientific assessments, findings,
    actions, limits and notes
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Original historical review; its claims and frozen inputs were independently
    checked. This observation does not treat historical commands as newly executed.
  snapshot_sha256: 33923abc4393609c3edb42f954dc2d4131310484e856400e0eca43f1e0ee3160
- evidence_id: plaque-record-5
  kind: record_content
  reference: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
  locator: Complete maintained record including every component, example, graph, discussion
    and history entry
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: supports
  summary: Whole current record independently read; same SHA-256 as the original review
    target input, without staleness or scientific edits.
  snapshot_sha256: 587fd3510ffd8ae95259dff336a7f2e984b50d34417d746277a41081a5b4ddb5
- evidence_id: plaque-original-5-yaml
  kind: prior_review
  reference: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.yaml
  locator: Complete immutable original; source, checks, scientific assessments, findings,
    actions, limits and notes
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Original historical review; its claims and frozen inputs were independently
    checked. This observation does not treat historical commands as newly executed.
  snapshot_sha256: a8ea503d08d2cc9f59bac77f0351b77e37b49d4b1fac7590685f013833f1346d
- evidence_id: plaque-original-5-md
  kind: prior_review
  reference: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit/review.md
  locator: Complete immutable original; source, checks, scientific assessments, findings,
    actions, limits and notes
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Original historical review; its claims and frozen inputs were independently
    checked. This observation does not treat historical commands as newly executed.
  snapshot_sha256: e5152fdea2e9547498cb597c9b3fcc8cdc9313f97cfa9ca78c8bfa4e89e63f84
- evidence_id: plaque-record-6
  kind: record_content
  reference: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
  locator: Complete maintained record including every component, example, graph, discussion
    and history entry
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: supports
  summary: Whole current record independently read; same SHA-256 as the original review
    target input, without staleness or scientific edits.
  snapshot_sha256: af55566f43167e28b8f1cca9fc819d6914d7281179845fc6f3bfb153e67cae43
- evidence_id: plaque-original-6-yaml
  kind: prior_review
  reference: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.yaml
  locator: Complete immutable original; source, checks, scientific assessments, findings,
    actions, limits and notes
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Original historical review; its claims and frozen inputs were independently
    checked. This observation does not treat historical commands as newly executed.
  snapshot_sha256: 18e1b3c70520f2d1651f55adabbf733c4e5c7d04d6ae4b78a67a4dcc5e775b60
- evidence_id: plaque-original-6-md
  kind: prior_review
  reference: reviews/structured/20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit/review.md
  locator: Complete immutable original; source, checks, scientific assessments, findings,
    actions, limits and notes
  accessed_at: '2026-11-04T07:16:37.637394Z'
  support: context_only
  summary: Original historical review; its claims and frozen inputs were independently
    checked. This observation does not treat historical commands as newly executed.
  snapshot_sha256: 2ce73b853f1d9eddcd3a98a654592ee6ab8bd9219c46ae39d6c6fecd60826d26
- evidence_id: plaque-input-original-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/input-original-proof.json
  locator: 47 current source/worktree hashes; 41 historical input occurrences; three
    original native validations and exact Markdown render comparisons
  accessed_at: '2026-11-04T07:13:49.447375Z'
  support: supports
  summary: All 47 frozen current inputs match source and working tree. All 41 historical
    input occurrences match their original Git revisions. Three original pairs validate
    and render exactly; assigned targets are unchanged.
  snapshot_sha256: 68b0587d5c86c7ea19566d7041975af0f6beba73f2421be0afc84778d2fdb137
- evidence_id: plaque-native-dnab_dnac_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-verify.log;
    log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:38.897929Z'
  support: supports
  summary: Exit 0. Current record contains 2 reviewed protein examples and 2 GENE_OR_PROTEIN
    nodes, all COVERED in the causal log. The verify log confirms identifier consistency,
    not independent assembly or source-stage support.
  snapshot_sha256: 5de2d43a277947d7b40b762bc0e6b5cb27c90958daad1cb05b2e5d2e9270ea0c
- evidence_id: plaque-native-dnab_dnac_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-causal.log;
    log SHA256 1a5fd2b44858b3af069fb75cc2842754b9f929dcbcc7335cc4034fd26fcf138e
  accessed_at: '2026-11-04T07:05:39.301111Z'
  support: supports
  summary: Exit 0. Current record contains 2 reviewed protein examples and 2 GENE_OR_PROTEIN
    nodes, all COVERED in the causal log. The verify log confirms identifier consistency,
    not independent assembly or source-stage support.
  snapshot_sha256: 3068281bff280cf5933696a179e0622e39a8c4d2bd41c94af5a1caaadbae8152
- evidence_id: plaque-native-dnab_dnac_dnat_pria_prib_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-verify.log;
    log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:40.597126Z'
  support: supports
  summary: Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN
    nodes, all COVERED in the causal log. The verify log confirms identifier consistency,
    not independent assembly or source-stage support.
  snapshot_sha256: 5900aaf6a5947f49a537cfdb49ad991155dc62c2737ad4b8089123c16bd59c26
- evidence_id: plaque-native-dnab_dnac_dnat_pria_prib_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-causal.log;
    log SHA256 da3be8302e150b5f1f300995c5bc908eaf804b9ec237b319e4ed1e1937955d35
  accessed_at: '2026-11-04T07:05:41.016178Z'
  support: supports
  summary: Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN
    nodes, all COVERED in the causal log. The verify log confirms identifier consistency,
    not independent assembly or source-stage support.
  snapshot_sha256: ec3defbc56295ba55b454ca5c96c164c221e6e09ccddf6d868adec2630f99fe9
- evidence_id: plaque-native-dnab_dnac_dnat_pria_pric_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-verify-receipt.json
  locator: Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-verify.log;
    log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T07:05:42.252627Z'
  support: supports
  summary: Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN
    nodes, all COVERED in the causal log. The verify log confirms identifier consistency,
    not independent assembly or source-stage support.
  snapshot_sha256: f11491e31c29fbec39c3f191fc78828880c46c948a0ab9c014fe713ed50a1e22
- evidence_id: plaque-native-dnab_dnac_dnat_pria_pric_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-causal-receipt.json
  locator: Actual command receipt and log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-causal.log;
    log SHA256 a61be5ffd377d729d7aee4e31668d88690314dce25c4496b9f83c9d4636e782c
  accessed_at: '2026-11-04T07:05:42.666946Z'
  support: supports
  summary: Exit 0. Current record contains 3 reviewed protein examples and 3 GENE_OR_PROTEIN
    nodes, all COVERED in the causal log. The verify log confirms identifier consistency,
    not independent assembly or source-stage support.
  snapshot_sha256: 8d89de880b227166326b8a0f21fdedd9ddfd8a729b5a4ef2f73466fb2c5c7e1c
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100,GO:1990158,GO:1990159,GO:1990099,GO:0032991,GO:0006270,GO:0031297,GO:1990160,GO:1990077
  locator: Full nine-term response; exact definitions/synonyms and typed children/relations
    for GO1990100, GO1990158, GO1990159, GO1990099, GO0032991, GO0006270, GO0031297,
    GO1990160 and GO1990077; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go.raw
  accessed_at: '2026-11-04T07:07:46.583278Z'
  support: supports
  summary: Current active GO identities and definitions support the intended three
    classes, distinct loader versus preprimosome hierarchy, and native function terms.
    Correct ontology quotation does not resolve conflict with experimentally isolated
    composition.
  snapshot_sha256: c5d37258120eb804772afdb6ee8e5c77991b0b49679655581f1f93eaea736212
- evidence_id: plaque-go-1990100-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/ancestors?relations=is_a
  locator: Exact is_a ancestor result for GO:1990100; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990100-ancestors.raw
  accessed_at: '2026-11-04T07:07:46.515403Z'
  support: supports
  summary: Current is-a ancestor response confirms class hierarchy without converting
    ancestry into direct experimental parthood.
  snapshot_sha256: 4fa6a40537e61ff0fb8751d5ff147043038497216cbfb44ea0493a4e552e8696
- evidence_id: plaque-go-1990100-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990100/constraints
  locator: Exact taxon-constraint response for GO:1990100; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990100-constraints.raw
  accessed_at: '2026-11-04T07:07:46.517648Z'
  support: supports
  summary: Current taxon constraint is an ontology scope condition, not prevalence
    evidence or a verified experimental archaeal example.
  snapshot_sha256: 1ed36968402927e59bf9175919bb91b6393bd0db507b2ba40f32be3f4b645b97
- evidence_id: plaque-go-1990158-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/ancestors?relations=is_a
  locator: Exact is_a ancestor result for GO:1990158; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990158-ancestors.raw
  accessed_at: '2026-11-04T07:07:46.522278Z'
  support: supports
  summary: Current is-a ancestor response confirms class hierarchy without converting
    ancestry into direct experimental parthood.
  snapshot_sha256: be9d22aa2b9a391faf36fb1d3a526bdbd8a544d3ee424d19778acb5108b97416
- evidence_id: plaque-go-1990158-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990158/constraints
  locator: Exact taxon-constraint response for GO:1990158; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990158-constraints.raw
  accessed_at: '2026-11-04T07:07:46.517697Z'
  support: supports
  summary: Current taxon constraint is an ontology scope condition, not prevalence
    evidence or a verified experimental archaeal example.
  snapshot_sha256: 05a80c3c70f81d8862490d2b66d6aa79e60ab75ce80cab308ac66b39e9f69d68
- evidence_id: plaque-go-1990159-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990159/ancestors?relations=is_a
  locator: Exact is_a ancestor result for GO:1990159; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990159-ancestors.raw
  accessed_at: '2026-11-04T07:07:47.102538Z'
  support: supports
  summary: Current is-a ancestor response confirms class hierarchy without converting
    ancestry into direct experimental parthood.
  snapshot_sha256: 34fccdfacb6d337c92b64b85b8a3cf20545f80f42ab5b875bdec28d283248514
- evidence_id: plaque-go-1990159-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990159/constraints
  locator: Exact taxon-constraint response for GO:1990159; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/go-1990159-constraints.raw
  accessed_at: '2026-11-04T07:07:47.107032Z'
  support: supports
  summary: Current taxon constraint is an ontology scope condition, not prevalence
    evidence or a verified experimental archaeal example.
  snapshot_sha256: 9c15dcfc8a8fde9a1e8a8f85021cab725d4c7af22b0d409d05c15d3022eee1d6
- evidence_id: plaque-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Full ENA taxonomy XML identity/rank/lineage, taxon 562; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/tax-562.raw
  accessed_at: '2026-11-04T07:07:47.099302Z'
  support: supports
  summary: Current authority identifies Escherichia coli species and its K-12 strain
    taxon separately; neither proves an unspecified experimental derivative is precisely
    the reference strain.
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: plaque-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Full ENA taxonomy XML identity/rank/lineage, taxon 83333; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/tax-83333.raw
  accessed_at: '2026-11-04T07:07:47.326672Z'
  support: supports
  summary: Current authority identifies Escherichia coli species and its K-12 strain
    taxon separately; neither proves an unspecified experimental derivative is precisely
    the reference strain.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: plaque-pmid-20129058
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20129058+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED PMID query, pageSize=1/resultType=core; complete abstract
    and bibliography only; no full body inferred from this response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/pmid-20129058.raw
  accessed_at: '2026-11-04T07:07:47.215291Z'
  support: supports
  summary: Complete primary abstract and metadata identify Makowska-Grzyska and Kaguni
    2010, DnaC delivery/release experiments and exact DOI.
  snapshot_sha256: 1945641c2f7c9bb7a9e6b17801ac402a6f3396688b0b8f9d2101d41683d03e5c
- evidence_id: plaque-pmid-8663104
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663104+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED PMID query, pageSize=1/resultType=core; complete abstract
    and bibliography only; no full body inferred from this response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/pmid-8663104.raw
  accessed_at: '2026-11-04T07:07:47.777528Z'
  support: supports
  summary: 'Complete primary abstract identifies the short PAS-substrate assembly:
    retained PriA/PriB/DnaT/DnaB, with DnaC not part of the final complex. The indexed
    erratum and full article body were not inspected.'
  snapshot_sha256: cf368ca685467ca9b841e51172defa297ef82b761b51f56cbe54525821ce3ec4
- evidence_id: plaque-pmid-8663105
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Europe PMC exact MED PMID query, pageSize=1/resultType=core; complete abstract
    and bibliography only; no full body inferred from this response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/pmid-8663105.raw
  accessed_at: '2026-11-04T07:07:47.730623Z'
  support: supports
  summary: Complete primary abstract identifies intact PhiX174 template experiments
    retaining PriA/PriB/PriC/DnaT/DnaB, no stable DnaC, and proposed repair/restart
    relevance.
  snapshot_sha256: 9ae7f296d9ad9b8fbd64592682e3f1db9299add2f94878340766746ace0e1989
- evidence_id: plaque-makowska2010-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/2819048/
  locator: Genuine PMC article; Results S8–S10, Discussion S14–S16 and Experimental
    Procedures S18/S20/S21, with captions for Figures 5–7. No figure pixels, raw measurements,
    or supplementary strain Table S1 inspected.; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/makowska2010-body.raw
  accessed_at: '2026-11-04T07:07:52.689000Z'
  support: supports
  summary: Primary results distinguish DnaC-dependent helicase delivery, DnaC retention
    before priming, and primase/rNTP-associated release. The approximately three-loader-per-hexamer
    interpretation in the measured oriC complex does not make every DnaB-DnaC assembly
    invariant. Mutant delivery without successful initiation separates presence from
    function.
  snapshot_sha256: 82c5387f4119bdad5f48738ff2b548536bfe73d00e23b0e7aca81b69ec3421de
- evidence_id: plaque-ng1996ii-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf
  locator: 'Genuine JBC PDF pp15649–15654: main Results/Discussion/Methods, Table
    I and figure captions 1–9, especially pp15653–15654; text extracted with pdftotext.
    No figure-pixel or Western reanalysis; bibliography is not independently read
    studies.; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ng1996ii-pdf.raw'
  accessed_at: '2026-11-04T07:07:52.419230Z'
  support: supports
  summary: 'Primary full main text separates supplied loading factors from isolated
    products: intact PhiX174 complexes retain PriA, PriB, PriC, DnaT and DnaB; DnaC
    is not a stable constituent. PriC is retained here unlike short PAS substrates;
    repair/restart is a proposed extension rather than a directly measured repaired-fork
    outcome.'
  snapshot_sha256: 1789a6bf1cfb26aeeacf73f6ba45b732d43eb3576268435c1736b357e3be6755
- evidence_id: plaque-up-P0ACB0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ACB0.json
  locator: 'Native UniProt complete JSON: primaryAccession/entryType/organism/genes,
    ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P0ACB0.raw'
  accessed_at: '2026-11-04T07:07:48.021210Z'
  support: supports
  summary: Reviewed exact K-12 taxon83333 entry P0ACB0 has primary gene dnaB and locus
    b4052. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION
    comments were checked; annotation alone is not experimental proof of the maintained
    complex.
  snapshot_sha256: edebd0e1411d58b0f8593f28aec4b2a227356105e8ab65e8095652ff58c1c3ea
- evidence_id: plaque-gene-dnaB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned native results; exact organism node and reviewed filter; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-dnaB.raw
  accessed_at: '2026-11-04T07:07:48.221013Z'
  support: supports
  summary: The exact reviewed gene/taxon search returns one entry, P0ACB0, whose own
    gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy
    queries are outside this exact-organism result.
  snapshot_sha256: a82408ab2f13701ec5f77df653333e6715273c2cc3fcfad9fe06ad2a5cccb089
  search_scope: UniProt REST; query (gene_exact:dnaB) AND (organism_id:83333) AND
    (reviewed:true); date 2026-11-04T07:07:48.221013Z; size=100; complete one-hit
    response inspected, no pagination or descendant-taxonomy expansion; database query,
    not filesystem absence search.
- evidence_id: plaque-up-P0AEF0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AEF0.json
  locator: 'Native UniProt complete JSON: primaryAccession/entryType/organism/genes,
    ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P0AEF0.raw'
  accessed_at: '2026-11-04T07:07:48.242439Z'
  support: supports
  summary: Reviewed exact K-12 taxon83333 entry P0AEF0 has primary gene dnaC and locus
    b4361. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION
    comments were checked; annotation alone is not experimental proof of the maintained
    complex.
  snapshot_sha256: 826b0c0f0c64c52ba43ae5cf0a1292b8080a58ce673cace11d83bd30075609a4
- evidence_id: plaque-gene-dnaC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned native results; exact organism node and reviewed filter; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-dnaC.raw
  accessed_at: '2026-11-04T07:07:48.774415Z'
  support: supports
  summary: The exact reviewed gene/taxon search returns one entry, P0AEF0, whose own
    gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy
    queries are outside this exact-organism result.
  snapshot_sha256: fc27864cb545ea3c9b7a3c83dc91170c0e5705fa1cbbde16caf3aed18c97205b
  search_scope: UniProt REST; query (gene_exact:dnaC) AND (organism_id:83333) AND
    (reviewed:true); date 2026-11-04T07:07:48.774415Z; size=100; complete one-hit
    response inspected, no pagination or descendant-taxonomy expansion; database query,
    not filesystem absence search.
- evidence_id: plaque-up-P0A8J2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A8J2.json
  locator: 'Native UniProt complete JSON: primaryAccession/entryType/organism/genes,
    ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P0A8J2.raw'
  accessed_at: '2026-11-04T07:07:49.167488Z'
  support: supports
  summary: Reviewed exact K-12 taxon83333 entry P0A8J2 has primary gene dnaT and locus
    b4362. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION
    comments were checked; annotation alone is not experimental proof of the maintained
    complex.
  snapshot_sha256: 0386cc1a24225bd2163f02bb9321fd59c773a862df700e6e11a442f2478a0eb8
- evidence_id: plaque-gene-dnaT
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaT%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned native results; exact organism node and reviewed filter; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-dnaT.raw
  accessed_at: '2026-11-04T07:07:50.402033Z'
  support: supports
  summary: The exact reviewed gene/taxon search returns one entry, P0A8J2, whose own
    gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy
    queries are outside this exact-organism result.
  snapshot_sha256: 098bbb792557c7cee62ac410f631525fb18878c8a368f6dc6a608934b785ac70
  search_scope: UniProt REST; query (gene_exact:dnaT) AND (organism_id:83333) AND
    (reviewed:true); date 2026-11-04T07:07:50.402033Z; size=100; complete one-hit
    response inspected, no pagination or descendant-taxonomy expansion; database query,
    not filesystem absence search.
- evidence_id: plaque-up-P17888
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P17888.json
  locator: 'Native UniProt complete JSON: primaryAccession/entryType/organism/genes,
    ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P17888.raw'
  accessed_at: '2026-11-04T07:07:49.306821Z'
  support: supports
  summary: Reviewed exact K-12 taxon83333 entry P17888 has primary gene priA and locus
    b3935. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION
    comments were checked; annotation alone is not experimental proof of the maintained
    complex.
  snapshot_sha256: 17504956503542663f62e0d18d9f987a50081497aa0daea13b6b7d96496536aa
- evidence_id: plaque-gene-priA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned native results; exact organism node and reviewed filter; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-priA.raw
  accessed_at: '2026-11-04T07:07:51.423161Z'
  support: supports
  summary: The exact reviewed gene/taxon search returns one entry, P17888, whose own
    gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy
    queries are outside this exact-organism result.
  snapshot_sha256: c618bd342375bdeea25c1ad6bad58c8a2e1caa6e8251a59b765619b44080f160
  search_scope: UniProt REST; query (gene_exact:priA) AND (organism_id:83333) AND
    (reviewed:true); date 2026-11-04T07:07:51.423161Z; size=100; complete one-hit
    response inspected, no pagination or descendant-taxonomy expansion; database query,
    not filesystem absence search.
- evidence_id: plaque-up-P07013
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P07013.json
  locator: 'Native UniProt complete JSON: primaryAccession/entryType/organism/genes,
    ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P07013.raw'
  accessed_at: '2026-11-04T07:07:50.222378Z'
  support: supports
  summary: Reviewed exact K-12 taxon83333 entry P07013 has primary gene priB and locus
    b4201. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION
    comments were checked; annotation alone is not experimental proof of the maintained
    complex.
  snapshot_sha256: 4a41331cb82a1040808d6b83f0be752e25dbea2320b60a6651bc862b9bac484f
- evidence_id: plaque-gene-priB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned native results; exact organism node and reviewed filter; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-priB.raw
  accessed_at: '2026-11-04T07:07:52.342088Z'
  support: supports
  summary: The exact reviewed gene/taxon search returns one entry, P07013, whose own
    gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy
    queries are outside this exact-organism result.
  snapshot_sha256: 44c93321a9d747492d7001566d8c7bd806b825ed3153821ac0c51ff7d20c58df
  search_scope: UniProt REST; query (gene_exact:priB) AND (organism_id:83333) AND
    (reviewed:true); date 2026-11-04T07:07:52.342088Z; size=100; complete one-hit
    response inspected, no pagination or descendant-taxonomy expansion; database query,
    not filesystem absence search.
- evidence_id: plaque-up-P23862
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P23862.json
  locator: 'Native UniProt complete JSON: primaryAccession/entryType/organism/genes,
    ordered loci, SUBUNIT and SIMILARITY/FUNCTION comments, InterPro/NCBIfam cross-references;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/up-P23862.raw'
  accessed_at: '2026-11-04T07:07:52.656638Z'
  support: supports
  summary: Reviewed exact K-12 taxon83333 entry P23862 has primary gene priC and locus
    b0467. Identity, aliases, family cross-references and bounded SUBUNIT/FUNCTION
    comments were checked; annotation alone is not experimental proof of the maintained
    complex.
  snapshot_sha256: 96930e6dc73122793f5d39f5c396641a24b6699043a4c497e2dfd2ab41051f13
- evidence_id: plaque-gene-priC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: All returned native results; exact organism node and reviewed filter; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/gene-priC.raw
  accessed_at: '2026-11-04T07:07:51.369562Z'
  support: supports
  summary: The exact reviewed gene/taxon search returns one entry, P23862, whose own
    gene/locus/taxon fields were inspected. Descendant strains and broader taxonomy
    queries are outside this exact-organism result.
  snapshot_sha256: bc4010a8d7187e308ab78e6895a971fdf39dc06b77d51b9164ca15db0550f673
  search_scope: UniProt REST; query (gene_exact:priC) AND (organism_id:83333) AND
    (reviewed:true); date 2026-11-04T07:07:51.369562Z; size=100; complete one-hit
    response inspected, no pagination or descendant-taxonomy expansion; database query,
    not filesystem absence search.
- evidence_id: plaque-ipr-IPR007692
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR007692.raw'
  accessed_at: '2026-11-04T07:07:51.001561Z'
  support: supports
  summary: DnaB-type helicase family, distinct from its individual domains; native
    DnaB entry cross-reference independently agrees.
  snapshot_sha256: 88b9a5d41c0b3d6be01e7510bcdc6f5b03d5f0de15075277d153421c33818e10
- evidence_id: plaque-ncbifam-NF005931
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF005931/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ncbifam-NF005931.raw'
  accessed_at: '2026-11-04T07:07:52.644858Z'
  support: supports
  summary: Exact unintegrated NCBIfam DnaC replicative helicase loader family; native
    DnaC cross-reference agrees.
  snapshot_sha256: 63575711031577fefad416d402b34107e8ddf4c110d6d81236f592c32d5a2d0c
- evidence_id: plaque-ipr-IPR028350
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028350/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR028350.raw'
  accessed_at: '2026-11-04T07:07:51.652457Z'
  support: supports
  summary: Broader DnaC/IstB homolog family includes a paralogous class and is not
    the proposed exact DnaC grounding.
  snapshot_sha256: 3be29cf2303dad6fad08a9b29568378f2b24bf038d4478219dc538b1cc52721d
- evidence_id: plaque-ipr-IPR020917
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020917/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR020917.raw'
  accessed_at: '2026-11-04T07:07:51.982542Z'
  support: supports
  summary: Exact DnaT/primosomal protein 1 family, with natural proteobacterial scope;
    not its narrower C-terminal domain.
  snapshot_sha256: 6737844952628c1e6c0e30133e8134728c11a4bc28c213dedc4afd497ef082cd
- evidence_id: plaque-ipr-IPR005259
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005259/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR005259.raw'
  accessed_at: '2026-11-04T07:07:52.031864Z'
  support: supports
  summary: Exact full PriA family, distinct from generic helicase/ATPase domains.
  snapshot_sha256: fd26c216e78be07f400f25ecd11062366714b19eda510840dbb92be4fb1e9db2
- evidence_id: plaque-ipr-IPR023646
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023646/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR023646.raw'
  accessed_at: '2026-11-04T07:07:52.268470Z'
  support: supports
  summary: Exact PriB family below broader PriB/SSB; native PriB cross-reference independently
    agrees.
  snapshot_sha256: 9dc0552a7f882fde8e6cadc6ce070085b2587a417f05e6ef9320c059cd8b4603
- evidence_id: plaque-ipr-IPR010890
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/
  locator: 'Full current InterPro/NCBIfam native metadata: accession/name/type, native
    non-LLM description, integration/hierarchy and member signatures; independently
    cross-checked to correct protein examples; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/ipr-IPR010890.raw'
  accessed_at: '2026-11-04T07:07:52.572669Z'
  support: supports
  summary: Exact PriC family, distinct from its broader structural superfamily; native
    PriC cross-reference agrees.
  snapshot_sha256: 0c8cb9aa7f1d6e1f45397fce72a6935dd2151706a90f512c92628c92bbc0217c
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Fresh same-PR public API response fetched by independent micro reviewer,
    independently reread here; exact retrieval timestamp retained; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T07:06:53.166338Z'
  support: context_only
  summary: Complete current catalogue contains E. coli and precise1k; an applicable
    host/dataset exists for the represented molecular records.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Fresh same-PR public API response fetched by independent micro reviewer,
    independently reread here; exact retrieval timestamp retained; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T07:06:53.737977Z'
  support: context_only
  summary: precise1k metadata lists BW25113, DGF-298, GMOS, MG1655 and W3110; 201
    modules, 4257 genes and 1035 samples. This is a five-strain dataset, not proof
    of exact experimental strain equivalence.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: plaque-ecoli-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Fresh same-PR public API response fetched by independent micro reviewer,
    independently reread here; exact retrieval timestamp retained; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T07:06:53.119675Z'
  support: context_only
  summary: Complete 201-module list was inspected for the bounded matched-locus context.
    No generated explanatory prose is used as evidence.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: plaque-adapter-b4052-gene
  kind: database
  reference: https://imodulondb.org/api/genes/b4052?organism=e_coli&dataset=precise1k
  locator: Full exact gene response; primary identity/locus/product and source organism/dataset
    fields; embedded annotations not treated as independently reviewed primary papers;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4052-gene.raw
  accessed_at: '2026-11-04T07:09:09.833909Z'
  support: context_only
  summary: Exact precise1k native gene record identifies dnaB/b4052, UniProt P0ACB0,
    and MG1655 coordinate STRING511145.b4052; this does not turn the multi-strain
    dataset into one experimental strain.
  snapshot_sha256: 407bd2abebaddf3c381f5c4e690cc26f20793cccdd06ab1d295398bd71f7f63f
- evidence_id: plaque-adapter-b4052-modules
  kind: search
  reference: https://imodulondb.org/api/genes/b4052/imodulons?organism=e_coli&dataset=precise1k
  locator: Exact locus membership response restricted to e_coli/precise1k; all201
    returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4052-modules.raw
  accessed_at: '2026-11-04T07:09:09.848987Z'
  support: context_only
  summary: No true membership flag among all 201 returned module rows. This threshold
    result does not establish biological absence, nonfunction or lack of physical
    assembly.
  snapshot_sha256: 64621a51f7ebc4c85af52da8de15f02c918736f01272f2b04ffdd82e306191ca
  search_scope: Official iModulonDB API exact locus b4052, organism=e_coli, dataset=precise1k;
    date 2026-11-04T07:09:09.848987Z; complete 201-row response, no other organism/dataset
    or sequence-neighbor search. Negative threshold flags are not negative biology;
    database query, no filesystem search.
- evidence_id: plaque-adapter-b4361-gene
  kind: database
  reference: https://imodulondb.org/api/genes/b4361?organism=e_coli&dataset=precise1k
  locator: Full exact gene response; primary identity/locus/product and source organism/dataset
    fields; embedded annotations not treated as independently reviewed primary papers;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4361-gene.raw
  accessed_at: '2026-11-04T07:09:09.829356Z'
  support: context_only
  summary: Exact precise1k native gene record identifies dnaC/b4361, UniProt P0AEF0,
    and MG1655 coordinate STRING511145.b4361; this does not turn the multi-strain
    dataset into one experimental strain.
  snapshot_sha256: 32c337d0bff0845a62f8b8bd65a75779499d94795341018fec8397c00af65fa1
- evidence_id: plaque-adapter-b4361-modules
  kind: search
  reference: https://imodulondb.org/api/genes/b4361/imodulons?organism=e_coli&dataset=precise1k
  locator: Exact locus membership response restricted to e_coli/precise1k; all201
    returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4361-modules.raw
  accessed_at: '2026-11-04T07:09:09.848006Z'
  support: context_only
  summary: No true membership flag among all 201 returned module rows. This threshold
    result does not establish biological absence, nonfunction or lack of physical
    assembly.
  snapshot_sha256: fe9c6ffe4d294787259f7be9d7d876716255ed143578e6898a745b11fa667c6d
  search_scope: Official iModulonDB API exact locus b4361, organism=e_coli, dataset=precise1k;
    date 2026-11-04T07:09:09.848006Z; complete 201-row response, no other organism/dataset
    or sequence-neighbor search. Negative threshold flags are not negative biology;
    database query, no filesystem search.
- evidence_id: plaque-adapter-b4362-gene
  kind: database
  reference: https://imodulondb.org/api/genes/b4362?organism=e_coli&dataset=precise1k
  locator: Full exact gene response; primary identity/locus/product and source organism/dataset
    fields; embedded annotations not treated as independently reviewed primary papers;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4362-gene.raw
  accessed_at: '2026-11-04T07:09:09.871460Z'
  support: context_only
  summary: Exact precise1k native gene record identifies dnaT/b4362, UniProt P0A8J2,
    and MG1655 coordinate STRING511145.b4362; this does not turn the multi-strain
    dataset into one experimental strain.
  snapshot_sha256: a78b4ace47489f776f34125ee6462a730db0788c779cf47bd45817bc7dc9ab4e
- evidence_id: plaque-adapter-b4362-modules
  kind: search
  reference: https://imodulondb.org/api/genes/b4362/imodulons?organism=e_coli&dataset=precise1k
  locator: Exact locus membership response restricted to e_coli/precise1k; all201
    returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4362-modules.raw
  accessed_at: '2026-11-04T07:09:09.906036Z'
  support: context_only
  summary: No true membership flag among all 201 returned module rows. This threshold
    result does not establish biological absence, nonfunction or lack of physical
    assembly.
  snapshot_sha256: 2a065917c6e70868af98baa0eab21c047c72fb3ad854e973dd727c03d4a20cd3
  search_scope: Official iModulonDB API exact locus b4362, organism=e_coli, dataset=precise1k;
    date 2026-11-04T07:09:09.906036Z; complete 201-row response, no other organism/dataset
    or sequence-neighbor search. Negative threshold flags are not negative biology;
    database query, no filesystem search.
- evidence_id: plaque-adapter-b3935-gene
  kind: database
  reference: https://imodulondb.org/api/genes/b3935?organism=e_coli&dataset=precise1k
  locator: Full exact gene response; primary identity/locus/product and source organism/dataset
    fields; embedded annotations not treated as independently reviewed primary papers;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b3935-gene.raw
  accessed_at: '2026-11-04T07:09:09.899964Z'
  support: context_only
  summary: Exact precise1k native gene record identifies priA/b3935, UniProt P17888,
    and MG1655 coordinate STRING511145.b3935; this does not turn the multi-strain
    dataset into one experimental strain.
  snapshot_sha256: 82e472f5d5d08a40a9c5d2b111bdc26ea527b82b171f7bfe080a2b372dbd5257
- evidence_id: plaque-adapter-b3935-modules
  kind: search
  reference: https://imodulondb.org/api/genes/b3935/imodulons?organism=e_coli&dataset=precise1k
  locator: Exact locus membership response restricted to e_coli/precise1k; all201
    returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b3935-modules.raw
  accessed_at: '2026-11-04T07:09:09.924360Z'
  support: context_only
  summary: No true membership flag among all 201 returned module rows. This threshold
    result does not establish biological absence, nonfunction or lack of physical
    assembly.
  snapshot_sha256: cde2f5ec2b967c3850a0275225e164e5107137ecca455dab1e4f275825d02e49
  search_scope: Official iModulonDB API exact locus b3935, organism=e_coli, dataset=precise1k;
    date 2026-11-04T07:09:09.924360Z; complete 201-row response, no other organism/dataset
    or sequence-neighbor search. Negative threshold flags are not negative biology;
    database query, no filesystem search.
- evidence_id: plaque-adapter-b4201-gene
  kind: database
  reference: https://imodulondb.org/api/genes/b4201?organism=e_coli&dataset=precise1k
  locator: Full exact gene response; primary identity/locus/product and source organism/dataset
    fields; embedded annotations not treated as independently reviewed primary papers;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4201-gene.raw
  accessed_at: '2026-11-04T07:09:09.921840Z'
  support: context_only
  summary: Exact precise1k native gene record identifies priB/b4201, UniProt P07013,
    and MG1655 coordinate STRING511145.b4201; this does not turn the multi-strain
    dataset into one experimental strain.
  snapshot_sha256: 2444d9e7125f865f3a448c7e0cd62196fc437a278ae415b8719f4d93cab6edc2
- evidence_id: plaque-adapter-b4201-modules
  kind: search
  reference: https://imodulondb.org/api/genes/b4201/imodulons?organism=e_coli&dataset=precise1k
  locator: Exact locus membership response restricted to e_coli/precise1k; all201
    returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b4201-modules.raw
  accessed_at: '2026-11-04T07:09:09.945052Z'
  support: context_only
  summary: 'One true flag among all 201 module rows: k1 Translation, weight0.099397177
    > threshold0.057970804. This is computational expression membership, not preprimosome
    membership.'
  snapshot_sha256: c2bb6e5f2bd2f30f0271a69f0f3d63e545f6a83febb9cb604f0c5d629f6ce553
  search_scope: Official iModulonDB API exact locus b4201, organism=e_coli, dataset=precise1k;
    date 2026-11-04T07:09:09.945052Z; complete 201-row response, no other organism/dataset
    or sequence-neighbor search. Negative threshold flags are not negative biology;
    database query, no filesystem search.
- evidence_id: plaque-adapter-b0467-gene
  kind: database
  reference: https://imodulondb.org/api/genes/b0467?organism=e_coli&dataset=precise1k
  locator: Full exact gene response; primary identity/locus/product and source organism/dataset
    fields; embedded annotations not treated as independently reviewed primary papers;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b0467-gene.raw
  accessed_at: '2026-11-04T07:09:09.937447Z'
  support: context_only
  summary: Exact precise1k native gene record identifies priC/b0467, UniProt P23862,
    and MG1655 coordinate STRING511145.b0467; this does not turn the multi-strain
    dataset into one experimental strain.
  snapshot_sha256: fdf7150247b857d0d5e3bb8d613be4745eb5142c24d1fc564ed3a634b36f5f97
- evidence_id: plaque-adapter-b0467-modules
  kind: search
  reference: https://imodulondb.org/api/genes/b0467/imodulons?organism=e_coli&dataset=precise1k
  locator: Exact locus membership response restricted to e_coli/precise1k; all201
    returned rows inspected; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-b0467-modules.raw
  accessed_at: '2026-11-04T07:09:09.964548Z'
  support: context_only
  summary: No true membership flag among all 201 returned module rows. This threshold
    result does not establish biological absence, nonfunction or lack of physical
    assembly.
  snapshot_sha256: febb27f40272c3c9f73b08782a2ace1135553116cb159c64f643ca7bc6badd6e
  search_scope: Official iModulonDB API exact locus b0467, organism=e_coli, dataset=precise1k;
    date 2026-11-04T07:09:09.964548Z; complete 201-row response, no other organism/dataset
    or sequence-neighbor search. Negative threshold flags are not negative biology;
    database query, no filesystem search.
- evidence_id: plaque-adapter-module1
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/1
  locator: e_coli/precise1k/k1 native metadata and complete53 member-weight entries
    only; generated summary and its model metadata excluded; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1.raw
  accessed_at: '2026-11-04T07:09:56.533655Z'
  support: context_only
  summary: Exact k1 Translation metadata identifies DksA annotation and 53 gene-weight
    entries including priB. Generated ai_summary fields were excluded from all judgments.
  snapshot_sha256: fdfaf557fdb00a92cb050f1f802cdf0270fc1ce1b64e892a3ed0ba43cea2dd04
- evidence_id: plaque-adapter-module1-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/1/genes
  locator: Full53-row native member table; exact priB identity/weight/threshold row
    and row-count reconciliation with module metadata; embedded UniProt prose not
    treated as newly inspected publications; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-plaque/adapter-module1-genes.raw
  accessed_at: '2026-11-04T07:09:56.621116Z'
  support: context_only
  summary: All53 distinct returned member rows are true; priB/b4201/P07013 has weight0.099397177
    against threshold0.057970804. This corroborates only transcriptomic membership
    and does not support physical association with translation machinery or assembly
    of the reviewed complexes.
  snapshot_sha256: ea6bfc49819118fe70ec422b827aa521bf064f30cf6ab5362a1195af11303ff0
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record review and structured sources
  summary: Positive protein/pathway claims require actual structured-source applicability;
    lack of an expression claim is insufficient. Official source fallback may be used
    with actual coverage and runner limits.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Component identities and Discussions
  summary: Verified exact full families differ from protein examples; historical rationale
    is append-only. Essentiality concerns formation, not catalytic function or viability.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component, protein-example, formation and causal-graph contracts
  summary: Classes and appropriate complexes are permitted. No optional-example or
    enum-only finding is manufactured; experimental membership and formation necessity
    are distinct.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Primary gene names, ambiguity, native verification and manual curation
  summary: Automatic ambiguous-query seeding must abstain; correct manual accession
    selection can use actual protein identity. Current alias-inclusive query ambiguity
    does not reconstruct an unspecified historical query.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Nonmechanistic scope and endpoints
  summary: Membership, staged loading, catalytic output and universal formation necessity
    are distinct claims.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Actual access scopes
  summary: Primary body, primary abstract, authority metadata and failed access are
    distinct tiers. No unseen figure pixels or supplements are certified.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: FindingStatus and FindingReference
  summary: Rejected is a supported native terminal disposition with exact previous
    occurrence; inherited rejected findings do not require record-curation actions.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003678,GO:0006269,GO:0031297,GO:0033202,GO:1990098,GO:1990099,GO:1990100,GO:1990156,GO:1990158,GO:1990159,GO:1990160,GO:1990161
  locator: 'All12 requested exact terms: labels, active status, definitions, synonyms,
    xrefs and relevant typed children'
  summary: GO1990160 is the DnaB-DnaC-Rep-PriC protein-DNA pre-primosome, distinct
    from PriA/PriB and PriA/PriC alternatives; pre-primosomes lack primase. GO1990156
    is DnaB-DnaG and explicitly part_of GO1990098; GO1990161 is the DnaB hexamer.
    Both latter classes are is_a DNA-helicase complex. Native broad Prokaryotes wording
    is not extended into an untested archaeal mechanism.
  accessed_at: '2026-11-04T07:06:53.660901Z'
  support: supports
  snapshot_sha256: 86f76f1170ba0ae06e64efedbe695c9dcbed34ee35821eb6229ab8f12eda1d32
- evidence_id: septin-ipr-IPR005752
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005752/
  locator: Native name/type, signatures, hierarchy and description provenance; no
    sequence alignment performed
  summary: Exact Rep family supported by MF01920/TIGR01074 and independently mapped
    P09980; broad UvrD-like parent and PcrA/UvrD siblings are not substitutes. Its
    erroneous hexamer sentence is excluded from biological support; native P09980
    reports DNA-associated homodimer.
  accessed_at: '2026-11-04T07:06:53.668368Z'
  support: supports
  snapshot_sha256: b91a95d3c03328d5bc9aed574996b6c0e5cef2c6a40bfc72039baa4cb8810562
- evidence_id: septin-ipr-IPR010890
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010890/
  locator: Native name/type, signatures, hierarchy and description provenance; no
    sequence alignment performed
  summary: Exact PriC family, PF07445, with independent native P23862 membership.
  accessed_at: '2026-11-04T07:06:53.673513Z'
  support: supports
  snapshot_sha256: 0c8cb9aa7f1d6e1f45397fce72a6935dd2151706a90f512c92628c92bbc0217c
- evidence_id: septin-ipr-IPR007692
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/
  locator: Native name/type, signatures, hierarchy and description provenance; no
    sequence alignment performed
  summary: Full DnaB-type helicase family, TIGR00665, with P0ACB0 and Q9X4C9 membership;
    not merely a domain or broad ATPase fold.
  accessed_at: '2026-11-04T07:06:53.663581Z'
  support: supports
  snapshot_sha256: 88b9a5d41c0b3d6be01e7510bcdc6f5b03d5f0de15075277d153421c33818e10
- evidence_id: septin-ipr-IPR030846
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030846/
  locator: Native name/type, signatures, hierarchy and description provenance; no
    sequence alignment performed
  summary: Bacterial DnaG full-family identity, HAMAP MF00974/PIRSF002811, independently
    mapped by P0ABS5.
  accessed_at: '2026-11-04T07:06:53.665752Z'
  support: supports
  snapshot_sha256: 73ccf9f437a4fa95533a5e36df6ad06b521e497cc825f2c566738850b2fb8e7e
- evidence_id: septin-retry-IPR006295
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006295/
  locator: Native name/type, signatures, hierarchy and description provenance; no
    sequence alignment performed
  summary: 'Native type is domain: DNA primase bacterial core does not denote the
    complete DnaG protein.'
  accessed_at: '2026-11-04T07:08:25.541848Z'
  support: supports
  snapshot_sha256: 24e4589413c8efb43f18433fac55d19aa80d3b100e8779daeff1ac983314d6d3
- evidence_id: septin-retry-IPR050219
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050219/
  locator: Native name/type, signatures, hierarchy and description provenance; no
    sequence alignment performed
  summary: Broader Panther family metadata is inspected; llm=true/checked=false description
    is excluded from biological support, including archaeal/exosome prose.
  accessed_at: '2026-11-04T07:08:25.536614Z'
  support: supports
  snapshot_sha256: 1fcc18624f8fa54ab1f5a0e7586855160ecaa26b28ae4f13e725103b6a8c8ee7
- evidence_id: septin-up-P09980
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09980.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed P09980: ATP-dependent DNA helicase Rep; primary gene rep; taxon83333;
    loci b3778, JW5604. Native function/subunit annotations and complete InterPro
    xrefs inspected; identity annotation is not a new independent assembly experiment.'
  accessed_at: '2026-11-04T07:06:53.726543Z'
  support: supports
  snapshot_sha256: dae98d308334bb9a6a702afcdc378176d04b73345251906c02cc3560d8ccb5e7
- evidence_id: septin-up-P23862
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23862.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed P23862: Replication restart protein PriC; primary gene priC;
    taxon83333; loci b0467, JW0456. Native function/subunit annotations and complete
    InterPro xrefs inspected; identity annotation is not a new independent assembly
    experiment.'
  accessed_at: '2026-11-04T07:06:54.224842Z'
  support: supports
  snapshot_sha256: 96930e6dc73122793f5d39f5c396641a24b6699043a4c497e2dfd2ab41051f13
- evidence_id: septin-up-P0ACB0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACB0.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed P0ACB0: Replicative DNA helicase DnaB; primary gene dnaB; taxon83333;
    loci b4052, JW4012. Native function/subunit annotations and complete InterPro
    xrefs inspected; identity annotation is not a new independent assembly experiment.'
  accessed_at: '2026-11-04T07:06:55.393130Z'
  support: supports
  snapshot_sha256: edebd0e1411d58b0f8593f28aec4b2a227356105e8ab65e8095652ff58c1c3ea
- evidence_id: septin-up-P0ABS5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABS5.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed P0ABS5: DNA primase; primary gene dnaG; taxon83333; loci b3066,
    JW3038. Native function/subunit annotations and complete InterPro xrefs inspected;
    identity annotation is not a new independent assembly experiment.'
  accessed_at: '2026-11-04T07:06:54.353012Z'
  support: supports
  snapshot_sha256: 3dd4cfacccc5ec8470c469ca2c8962c6ea0c433124507a5921eb70ab0c7aac9e
- evidence_id: septin-up-Q9X4C9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9X4C9.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed Q9X4C9: Replicative DNA helicase DnaB; primary gene dnaB; taxon1422;
    loci . Native function/subunit annotations and complete InterPro xrefs inspected;
    identity annotation is not a new independent assembly experiment. Biological Geobacillus
    source remains distinct from recombinant E.coli BL21(DE3).'
  accessed_at: '2026-11-04T07:06:53.717846Z'
  support: supports
  snapshot_sha256: bbbd338f62abcee5b0864390b841d89b091fc629b465468d013b8a359e5621f6
- evidence_id: septin-up-P03856
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P03856.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed P03856: Replication initiation protein; primary gene repE; taxon83333;
    loci ECOK12F045. Native function/subunit annotations and complete InterPro xrefs
    inspected; identity annotation is not a new independent assembly experiment. RepE
    has synonym rep and is not Rep helicase; this explains current alias-inclusive
    query ambiguity without disproving the maintained P09980 selection.'
  accessed_at: '2026-11-04T07:08:25.619744Z'
  support: supports
  snapshot_sha256: 40f14edc08c52e9878f7d9247dbab7948570dda0cd13e7da1ee429db8d41765d
- evidence_id: septin-up-P0AEF0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEF0.json
  locator: Complete identity/gene/taxon/status and relevant FUNCTION/SUBUNIT/evidence;
    family xrefs
  summary: 'Reviewed P0AEF0: Replicative helicase loader DnaC; primary gene dnaC;
    taxon83333; loci b4361, JW4325. Native function/subunit annotations and complete
    InterPro xrefs inspected; identity annotation is not a new independent assembly
    experiment. Named loading-subcomplex context only, not a mandatory missing example.'
  accessed_at: '2026-11-04T07:08:25.626923Z'
  support: supports
  snapshot_sha256: 826b0c0f0c64c52ba43ae5cf0a1292b8080a58ce673cace11d83bd30075609a4
- evidence_id: septin-query-rep-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Arep%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity/primary gene/synonym/organism/status rows
  summary: Current returned accessions P09980, P03856. Only P09980 is primary rep/Rep
    helicase; P03856 is primary repE with alias rep. Current search does not expose
    the earlier unstated endpoint or establish a historical error.
  accessed_at: '2026-11-04T07:07:00.430863Z'
  support: supports
  snapshot_sha256: ba41b4d4eabcc6162cb859ac819e7489fd4fc8bb0671638f4fa069569c4b0fe8
  search_scope: UniProt gene_exact:rep AND organism_id:83333 AND reviewed:true, size500,
    no date filter; all 2 returned entries independently read at 2026-11-04T07:07:00.430863Z.
- evidence_id: septin-query-priC-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ApriC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity/primary gene/synonym/organism/status rows
  summary: Current returned accessions P23862. Singleton supports current native reference-identity
    wording at this exact bounded query.
  accessed_at: '2026-11-04T07:06:58.445676Z'
  support: supports
  snapshot_sha256: bc4010a8d7187e308ab78e6895a971fdf39dc06b77d51b9164ca15db0550f673
  search_scope: UniProt gene_exact:priC AND organism_id:83333 AND reviewed:true, size500,
    no date filter; all 1 returned entries independently read at 2026-11-04T07:06:58.445676Z.
- evidence_id: septin-query-dnaB-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity/primary gene/synonym/organism/status rows
  summary: Current returned accessions P0ACB0. Singleton supports current native reference-identity
    wording at this exact bounded query.
  accessed_at: '2026-11-04T07:06:59.490314Z'
  support: supports
  snapshot_sha256: a82408ab2f13701ec5f77df653333e6715273c2cc3fcfad9fe06ad2a5cccb089
  search_scope: UniProt gene_exact:dnaB AND organism_id:83333 AND reviewed:true, size500,
    no date filter; all 1 returned entries independently read at 2026-11-04T07:06:59.490314Z.
- evidence_id: septin-query-dnaG-83333
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity/primary gene/synonym/organism/status rows
  summary: Current returned accessions P0ABS5. Singleton supports current native reference-identity
    wording at this exact bounded query.
  accessed_at: '2026-11-04T07:07:00.447297Z'
  support: supports
  snapshot_sha256: 8c4d7768ca4c12de32448cc28f5fc09c1fdb9401446fa05fc5cc991d07100e5a
  search_scope: UniProt gene_exact:dnaG AND organism_id:83333 AND reviewed:true, size500,
    no date filter; all 1 returned entries independently read at 2026-11-04T07:07:00.447297Z.
- evidence_id: septin-query-dnaB-1422
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaB%29+AND+%28organism_id%3A1422%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity/primary gene/synonym/organism/status rows
  summary: Current returned accessions Q9X4C9. Singleton supports current native reference-identity
    wording at this exact bounded query.
  accessed_at: '2026-11-04T07:06:59.342975Z'
  support: supports
  snapshot_sha256: a930ed2e03ac00c1e96d304fbd85ed4fe22b2500488ca79651c98ba66a28ecd8
  search_scope: UniProt gene_exact:dnaB AND organism_id:1422 AND reviewed:true, size500,
    no date filter; all 1 returned entries independently read at 2026-11-04T07:06:59.342975Z.
- evidence_id: septin-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native ENA name/rank/synonyms/lineage response
  summary: Taxon562 is Escherichia coli (species). Biological source and experimental
    expression strain are not interchangeable.
  accessed_at: '2026-11-04T07:06:54.320117Z'
  support: supports
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: septin-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native ENA name/rank/synonyms/lineage response
  summary: Taxon83333 is Escherichia coli K-12 (strain). Biological source and experimental
    expression strain are not interchangeable.
  accessed_at: '2026-11-04T07:06:54.342229Z'
  support: supports
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: septin-tax-1422
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1422
  locator: Complete native ENA name/rank/synonyms/lineage response
  summary: Taxon1422 is Geobacillus stearothermophilus (species). Biological source
    and experimental expression strain are not interchangeable.
  accessed_at: '2026-11-04T07:06:54.501308Z'
  support: supports
  snapshot_sha256: 3d1d8c266b4f8563c8cc8b9721b44c03982ca636d836eb7a56d49ca7272d11c8
- evidence_id: septin-pmid-19941825
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19941825+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Native complete CORE metadata and abstractText; no full-body inference
    from abstract
  summary: Exact native title, authors, year and DOI checked; complete primary abstract
    read. Rep provides a second motor at the replisome to promote duplication of protein-bound
    DNA. DOI 10.1016/j.molcel.2009.11.009.
  accessed_at: '2026-11-04T07:06:54.481976Z'
  support: supports
  snapshot_sha256: 227256bcb5cd57bbdf624459065a7a7e859727e86c450c23390453efba625ee4
  search_scope: EuropePMC EXT_ID:19941825 AND SRC:MED, CORE JSON/pageSize1, no date
    filter; unique complete result at 2026-11-04T07:06:54.481976Z.
- evidence_id: septin-pmid-8663105
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663105+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Native complete CORE metadata and abstractText; no full-body inference
    from abstract
  summary: Exact native title, authors, year and DOI checked; complete primary abstract
    read. The ordered assembly of the phiX174-type primosome. II. Preservation of
    primosome composition from assembly through replication. DOI 10.1074/jbc.271.26.15649.
  accessed_at: '2026-11-04T07:06:54.845079Z'
  support: supports
  snapshot_sha256: 9ae7f296d9ad9b8fbd64592682e3f1db9299add2f94878340766746ace0e1989
  search_scope: EuropePMC EXT_ID:8663105 AND SRC:MED, CORE JSON/pageSize1, no date
    filter; unique complete result at 2026-11-04T07:06:54.845079Z.
- evidence_id: septin-pmid-14557266
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14557266+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Native complete CORE metadata and abstractText; no full-body inference
    from abstract
  summary: Exact native title, authors, year and DOI checked; complete primary abstract
    read. Mechanism and stoichiometry of interaction of DnaG primase with DnaB helicase
    of Escherichia coli in RNA primer synthesis. DOI 10.1074/jbc.m308956200. Authors
    are Mitkova, Khopde and Biswas2003, not Tougu/Marians. Chemical crosslinking/gel
    filtration and anisotropy/Scatchard support three DnaG per DnaB hexamer in a stabilized
    E.coli complex; this is not invariant in-vivo stoichiometry or universal formation
    necessity.
  accessed_at: '2026-11-04T07:06:54.942815Z'
  support: supports
  snapshot_sha256: b1ed71edc04c9590ee3fc3b3eed9cdeaf922ade155352f24bbdc2e9e204a89be
  search_scope: EuropePMC EXT_ID:14557266 AND SRC:MED, CORE JSON/pageSize1, no date
    filter; unique complete result at 2026-11-04T07:06:54.942815Z.
- evidence_id: septin-pmid-17947583
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17947583+AND+SRC%3AMED&format=json&resultType=core&pageSize=1
  locator: Native complete CORE metadata and abstractText; no full-body inference
    from abstract
  summary: Exact native title, authors, year and DOI checked; complete primary abstract
    read. Structure of hexameric DnaB helicase and its complex with a domain of DnaG
    primase. DOI 10.1126/science.1147353. DnaB-alone and DnaG-binding-domain structures
    are separate forms; full body unavailable on attempted publisher route. No supplementary
    experiment claim.
  accessed_at: '2026-11-04T07:06:54.963281Z'
  support: supports
  snapshot_sha256: d59936d9325a4ecb4069bc25f119ec848ad9edcfc22469f82d739888ecd19a8a
  search_scope: EuropePMC EXT_ID:17947583 AND SRC:MED, CORE JSON/pageSize1, no date
    filter; unique complete result at 2026-11-04T07:06:54.963281Z.
- evidence_id: septin-guy2009-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2807033/
  locator: 'Genuine PMC2807033 HTML: Introduction sec1; Results sec2.1 and2.6 with
    Fig1/6/7 captions; all Discussion sec3 and Experimental Procedures sec4. Not Results2.2–2.5
    in full; no supplementary TableS1 or pixels'
  summary: Primary assays examine oriC-initiated forks and add Rep after blockage;
    stated reaction includes DnaA/DnaB/DnaC/DnaG/HU/SSB/PolIII/beta, not PriC. Rep-DnaB
    binding is inhibited by DnaC; authors place binding after loading. Introduction
    separately cites a Rep/PriC restart pathway. These measured stages do not directly
    isolate the maintained quartet; they do not refute its existence. MG1655 appears
    in uvrD cloning, not proof of every preparation strain.
  accessed_at: '2026-11-04T07:06:53.287150Z'
  support: supports
  snapshot_sha256: c8e21593702d726902b2d93d8bdae01faee4251748811b77f2c2274a9cc1c484
- evidence_id: septin-ng1996ii-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/7cc3/a0885916eebe17fede5346ad9e4d97fab747.pdf
  locator: 'Genuine publisher-formatted primary PDF pp15649–15654: Introduction, Methods,
    Results, Discussion, TableI and Fig1–9 captions; references not treated as independently
    read studies; no figure pixels'
  summary: Retained PhiX174 ssDNA assembly contains PriA/PriB/PriC/DnaT/DnaB; DnaG
    associates for priming and DnaC is not a stable major constituent. PriA omission
    and PriC partial effects concern that different cohort, not the Rep/PriC quartet.
    Methods rely on prior preparations and do not certify a current reference strain
    for every reagent. No exhaustive assertion that no quartet experiment exists.
  accessed_at: '2026-11-04T07:06:53.279641Z'
  support: supports
  snapshot_sha256: 1789a6bf1cfb26aeeacf73f6ba45b732d43eb3576268435c1736b357e3be6755
- evidence_id: septin-pdb-entry
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/2R6D
  locator: Actual RCSB entry/assembly/entity fields; no coordinate or density reanalysis
  summary: 2R6D primary citation Bailey/Eliason/Steitz2007; experimental X-ray3.7Angstrom
    entry, one protein entity and six protein instances.
  accessed_at: '2026-11-04T07:06:54.433684Z'
  support: supports
  snapshot_sha256: e33605a7ef8b5aeb7809a5f96502ecd1562b4be9c3ed11c594ba515a67424610
- evidence_id: septin-pdb-assembly
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/2R6D/1
  locator: Actual RCSB entry/assembly/entity fields; no coordinate or density reanalysis
  summary: Assembly1 is an author/software-defined homohexamer with six monomers,
    supporting the maintained six-copy DnaB stoichiometry.
  accessed_at: '2026-11-04T07:06:54.494562Z'
  support: supports
  snapshot_sha256: d81271bf6023f82d8129430650f9111b530c923755fceea486883c668e8c52ec
- evidence_id: septin-pdb-entity
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/2R6D/1
  locator: Actual RCSB entry/assembly/entity fields; no coordinate or density reanalysis
  summary: ChainsA–F map completely to Q9X4C9; native biological source Bacillus/Geobacillus
    stearothermophilus1422 is distinct from E.coli BL21(DE3) expression host. This
    entry does not contain the DnaG-binding domain.
  accessed_at: '2026-11-04T07:06:54.562255Z'
  support: supports
  snapshot_sha256: 047f1b556d6fa8ec14dfeb9c17a3ce7f40c7bf942a4fb4c8ee6832b4956d7575
- evidence_id: septin-ipr-IPR006295
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006295/
  locator: Actual current HTTP429 response only
  summary: The attempted route did not supply its requested scientific object/body.
    Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain
    bounded to primary abstract and native structural/identity data. Failure is not
    negative biology.
  accessed_at: '2026-11-04T07:06:53.861419Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR050219
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050219/
  locator: Actual current HTTP429 response only
  summary: The attempted route did not supply its requested scientific object/body.
    Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain
    bounded to primary abstract and native structural/identity data. Failure is not
    negative biology.
  accessed_at: '2026-11-04T07:06:53.871180Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-mitkova-pdf
  kind: validation
  reference: https://www.jbc.org/article/S0021925820752282/pdf
  locator: Actual current HTTP403 response only
  summary: The attempted route did not supply its requested scientific object/body.
    Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain
    bounded to primary abstract and native structural/identity data. Failure is not
    negative biology.
  accessed_at: '2026-11-04T07:08:24.841430Z'
  support: context_only
  snapshot_sha256: cdba6da0010cb8c75713148a24d428fab7899fa8d80df816184bc828171cd208
- evidence_id: septin-bailey-publisher
  kind: validation
  reference: https://www.science.org/doi/10.1126/science.1147353
  locator: Actual current HTTP403 response only
  summary: The attempted route did not supply its requested scientific object/body.
    Exact authority retries succeeded separately; Mitkova/Bailey conclusions remain
    bounded to primary abstract and native structural/identity data. Failure is not
    negative biology.
  accessed_at: '2026-11-04T07:08:24.860203Z'
  support: context_only
  snapshot_sha256: 6f86ff01c35e03137033afcc39390848c9145b9ea4f26de910a43cb4232ab993
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete20-organism official catalogue; all organism names/keys independently
    inspected
  summary: E.coli is covered; Geobacillus stearothermophilus is not listed. Bacillus
    subtilis is a different organism and is not used as a substitute. Catalogue coverage
    does not establish biological presence or absence.
  accessed_at: '2026-11-04T07:06:53.166338Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official unpaginated /api/datasets; complete20 rows checked for Escherichia
    coli and Geobacillus/Bacillus stearothermophilus; no date filter, actual 2026-11-04T07:06:53.166338Z.
- evidence_id: septin-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete e_coli/precise1k metadata and strain list
  summary: Five advertised strains BW25113,DGF-298,GMOS,MG1655,W3110;201 modules,1035samples.
    Appropriate reference-species context, not coverage of BL21(DE3), all mutants,
    every preparation in Ng/Guy or Geobacillus.
  accessed_at: '2026-11-04T07:06:53.737977Z'
  support: supports
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: septin-ecoli-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: All201 returned module ID/name/regulator/category rows; not activity traces
    or generated prose
  summary: Nucleotide Stress module10 is a native annotated expression module; complete
    list supports a bounded gene-membership cross-check only.
  accessed_at: '2026-11-04T07:06:53.119675Z'
  support: supports
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: Official e_coli/precise1k/imodulons; all201 rows, no date filter or
    other dataset; read for named replication loci and returned module IDs.
- evidence_id: septin-modulegene-rep
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3778
  locator: Exact gene_id/name/product/UniProt mapping
  summary: Dataset locus b3778 maps rep to the independently inspected native accession.
    Imported functional prose is annotation context, not a newly read primary paper.
  accessed_at: '2026-11-04T07:08:24.870383Z'
  support: supports
  snapshot_sha256: 7c0d565be3e91e041f4830949fab3e3fa8a9b287ee1a1f9849d972a9a31d8927
- evidence_id: septin-modulemembers-rep
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3778/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows
  summary: 'Thresholded hits: none. False membership flags do not imply absent expression,
    gene, regulation or structural role; a positive hit does not establish assembly.'
  accessed_at: '2026-11-04T07:08:24.899758Z'
  support: supports
  snapshot_sha256: a874c9cd3abdce4c781a5726d54c18d22ce3311787af74940959bf44134d1145
  search_scope: Official e_coli/precise1k/gene b3778 (rep) /imodulons; complete201
    returned rows,no date filter,no cross-dataset extrapolation; actual 2026-11-04T07:08:24.899758Z.
- evidence_id: septin-modulegene-priC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0467
  locator: Exact gene_id/name/product/UniProt mapping
  summary: Dataset locus b0467 maps priC to the independently inspected native accession.
    Imported functional prose is annotation context, not a newly read primary paper.
  accessed_at: '2026-11-04T07:08:24.839689Z'
  support: supports
  snapshot_sha256: 807c5508a4f6e6b831cf9d32029d3df914be80c743b9585041734c3b3f677b04
- evidence_id: septin-modulemembers-priC
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0467/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows
  summary: 'Thresholded hits: none. False membership flags do not imply absent expression,
    gene, regulation or structural role; a positive hit does not establish assembly.'
  accessed_at: '2026-11-04T07:08:24.877148Z'
  support: supports
  snapshot_sha256: c6dc2c20873b549b3acccafd1d8d46b69ba26dd5f630545e76f676a1df842b85
  search_scope: Official e_coli/precise1k/gene b0467 (priC) /imodulons; complete201
    returned rows,no date filter,no cross-dataset extrapolation; actual 2026-11-04T07:08:24.877148Z.
- evidence_id: septin-modulegene-dnaB
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4052
  locator: Exact gene_id/name/product/UniProt mapping
  summary: Dataset locus b4052 maps dnaB to the independently inspected native accession.
    Imported functional prose is annotation context, not a newly read primary paper.
  accessed_at: '2026-11-04T07:08:24.870347Z'
  support: supports
  snapshot_sha256: 69896d62515436606275f0b2e3ed0b33e80762e8a3163edc9e36943f57d4d914
- evidence_id: septin-modulemembers-dnaB
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4052/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows
  summary: 'Thresholded hits: none. False membership flags do not imply absent expression,
    gene, regulation or structural role; a positive hit does not establish assembly.'
  accessed_at: '2026-11-04T07:08:24.886421Z'
  support: supports
  snapshot_sha256: 6857269f74e8531f6428bda4ac5183118a493f1701320ba44a2cf201bfd496e7
  search_scope: Official e_coli/precise1k/gene b4052 (dnaB) /imodulons; complete201
    returned rows,no date filter,no cross-dataset extrapolation; actual 2026-11-04T07:08:24.886421Z.
- evidence_id: septin-modulegene-dnaC
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4361
  locator: Exact gene_id/name/product/UniProt mapping
  summary: Dataset locus b4361 maps dnaC to the independently inspected native accession.
    Imported functional prose is annotation context, not a newly read primary paper.
  accessed_at: '2026-11-04T07:08:24.839614Z'
  support: supports
  snapshot_sha256: 75a6c5fd6f380adc936a56d2c4e8fd36093b6200f2d633eac924977e923d27da
- evidence_id: septin-modulemembers-dnaC
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4361/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows
  summary: 'Thresholded hits: none. False membership flags do not imply absent expression,
    gene, regulation or structural role; a positive hit does not establish assembly.'
  accessed_at: '2026-11-04T07:08:24.898750Z'
  support: supports
  snapshot_sha256: a7b4b55c42c06bf29f9141c8cec55e2c8a9f552c4dce2c7c75aa0f07232029df
  search_scope: Official e_coli/precise1k/gene b4361 (dnaC) /imodulons; complete201
    returned rows,no date filter,no cross-dataset extrapolation; actual 2026-11-04T07:08:24.898750Z.
- evidence_id: septin-modulegene-dnaG
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3066
  locator: Exact gene_id/name/product/UniProt mapping
  summary: Dataset locus b3066 maps dnaG to the independently inspected native accession.
    Imported functional prose is annotation context, not a newly read primary paper.
  accessed_at: '2026-11-04T07:08:24.886394Z'
  support: supports
  snapshot_sha256: 8ad9ade8c5525f716974bdabec6475682db5a5ea85afa568f162d15c834b16fa
- evidence_id: septin-modulemembers-dnaG
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3066/imodulons
  locator: All201 weight/threshold/is_in_imodulon rows
  summary: 'Thresholded hits: 10 Nucleotide Stress. False membership flags do not
    imply absent expression, gene, regulation or structural role; a positive hit does
    not establish assembly.'
  accessed_at: '2026-11-04T07:08:24.930998Z'
  support: supports
  snapshot_sha256: c55795e5d23410354cd1b717a2b23eb83c1ac907eb5e51e7b2ab082299b8fcf5
  search_scope: Official e_coli/precise1k/gene b3066 (dnaG) /imodulons; complete201
    returned rows,no date filter,no cross-dataset extrapolation; actual 2026-11-04T07:08:24.930998Z.
- evidence_id: septin-module-10
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/10
  locator: Native module name/category/threshold/member IDs; ai_summary and activity
    interpretation excluded
  summary: Nucleotide Stress module10 threshold0.077432849 includes dnaG b3066 weight0.082144995;
    fifteen members. No regulator assigned; the expression cluster does not demonstrate
    physical DnaB-DnaG binding, localization or formation necessity.
  accessed_at: '2026-11-04T07:11:51.041129Z'
  support: supports
  snapshot_sha256: 2b2a79ee13351d914b0fa98d0aa767843b467db1c4b79cc17681affde8f2d11b
- evidence_id: septin-module-10-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/10/genes
  locator: Complete15 member identity rows; exact dnaG b3066 weight/threshold/native
    accession
  summary: Independent member endpoint agrees dnaG/P0ABS5 belongs to the thresholded
    module. Other imported function prose is not primary evidence and does not expand
    this review to those proteins.
  accessed_at: '2026-11-04T07:11:51.033258Z'
  support: supports
  snapshot_sha256: bc5e61046c802b535fd526571c29a48357ecd06020aabd881768f49e75d596b0
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical actual Nov3 00:49Z invocation receipt
  summary: Actual prior exit1 PermissionError reading pyvenv.cfg; no fresh invocation
    or successful runner claimed. Current official source fallback is separately evidenced.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/adversary-septin/original-checks.json
  locator: Actual3 original validate/render runs and39 historical input occurrences
  summary: All original native validate/render exit0; derived Markdown byte-identical.
    All13 historical inputs per original match retained source; all three current
    targets nonstale. Historical global gate provenance is not current-head CI.
  accessed_at: '2026-11-04T07:07:05.782448Z'
  support: supports
  snapshot_sha256: afe7c371162ea264b1258cd24e99788fec3cffda6ed87c4220c18f7ccc3ca312
- evidence_id: septin-record-dnab_dnac_rep_pric_complex
  kind: record_content
  reference: data/structures/other/dnab_dnac_rep_pric_complex.yaml
  locator: Complete current frozen record, every field and history
  summary: Current full record independently assessed; historical rationale is not
    automatically current scientific evidence.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: context_only
  snapshot_sha256: 50dccdc4d855065a8319372f4350453a2628309608fad038483bbf6524b0bb8f
- evidence_id: septin-original-dnab_dnac_rep_pric_complex
  kind: record_content
  reference: reviews/structured/20261022T060743Z-dnab-dnac-rep-pric-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown
  summary: Original scopes/findings/actions and exact historical input hashes independently
    reviewed; original bytes remain immutable.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: context_only
  snapshot_sha256: 1e4077fc36e5c5ecf3b5dda71df6dd60ef532fafa2c798da60e019b95f4d41c3
- evidence_id: septin-native-dnab_dnac_rep_pric_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-verify-receipt.json
    receiptSHA256 1cd9000424560e3d66e55f2816d7f74dcaa1ab7ad02be9937723130d76cdbe2c;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED. Native identifier/coverage success does not establish
    direct complex membership, experimental strain equivalence or formation necessity.
  accessed_at: '2026-11-04T07:05:44.325762Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dnab_dnac_rep_pric_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnac_rep_pric_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-causal-receipt.json
    receiptSHA256 731f7b0a133b6feac8c1dadca926613382e260b958ca80dc8ad36dcdc18851f7;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED. Native identifier/coverage success does not establish
    direct complex membership, experimental strain equivalence or formation necessity.
  accessed_at: '2026-11-04T07:05:44.731018Z'
  support: supports
  snapshot_sha256: 6e9daeea33d397f83257ca4de9aacdc420b905a89c38bf3d23a0a5b10a4a6358
- evidence_id: septin-record-dnab_dnag_complex
  kind: record_content
  reference: data/structures/other/dnab_dnag_complex.yaml
  locator: Complete current frozen record, every field and history
  summary: Current full record independently assessed; historical rationale is not
    automatically current scientific evidence.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: context_only
  snapshot_sha256: 6dae9176d717fa24dc9f2f32f9af9f307bd12111d249a4cd164d5f6e29ea917c
- evidence_id: septin-original-dnab_dnag_complex
  kind: record_content
  reference: reviews/structured/20261022T060744Z-dnab-dnag-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown
  summary: Original scopes/findings/actions and exact historical input hashes independently
    reviewed; original bytes remain immutable.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: context_only
  snapshot_sha256: 67a40ef8cbee52e94d9386a29ab3d712b8ae87e2f00f7adb8f452e898db9badd
- evidence_id: septin-native-dnab_dnag_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnag_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-verify-receipt.json
    receiptSHA256 408ddeb8dd1f44920bd990b56eebeba9b96b5b587579a4cbbc4b561687f4ee82;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED. Native identifier/coverage success does not establish
    direct complex membership, experimental strain equivalence or formation necessity.
  accessed_at: '2026-11-04T07:05:45.854437Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dnab_dnag_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_dnag_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-causal-receipt.json
    receiptSHA256 b5da46d0ccfe4371433722dc9ceddffd9aa706b61072346b24d56bb6bcb61b92;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 2 reviewed example occurrences and 2 typed
    protein nodes, all COVERED. Native identifier/coverage success does not establish
    direct complex membership, experimental strain equivalence or formation necessity.
  accessed_at: '2026-11-04T07:05:46.253065Z'
  support: supports
  snapshot_sha256: 678bd1bf9f8076805fae7422583c6b42be13e85b6d4dd79eb4960dddbb3d93b9
- evidence_id: septin-record-dnab_helicase_complex
  kind: record_content
  reference: data/structures/other/dnab_helicase_complex.yaml
  locator: Complete current frozen record, every field and history
  summary: Current full record independently assessed; historical rationale is not
    automatically current scientific evidence.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: context_only
  snapshot_sha256: 2d0d0d647439c6e937f1aeb202b477fffc50813668a1c8ac5d42dd5b76932e99
- evidence_id: septin-original-dnab_helicase_complex
  kind: record_content
  reference: reviews/structured/20261022T060744Z-dnab-helicase-complex-audit/review.yaml
  locator: Complete original YAML and deterministic Markdown
  summary: Original scopes/findings/actions and exact historical input hashes independently
    reviewed; original bytes remain immutable.
  accessed_at: '2026-11-04T07:15:14.484946Z'
  support: context_only
  snapshot_sha256: acfe6847ede731a7cb548b259beeb69ed0222ecfa2d547cd70c3183269b8ff19
- evidence_id: septin-native-dnab_helicase_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_helicase_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-verify-receipt.json
    receiptSHA256 362792eeccd1e8020b0332007e1e3689fc1beff368504630f7c26d9bc1bf63ce;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-verify.log
  summary: Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed
    protein nodes, all COVERED. Native identifier/coverage success does not establish
    direct complex membership, experimental strain equivalence or formation necessity.
  accessed_at: '2026-11-04T07:05:47.824969Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-dnab_helicase_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/dnab_helicase_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-causal-receipt.json
    receiptSHA256 e50ecb0daa3219354a84177889a6ea94c643c0797cff00637c4b282cdcd0c27f;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-causal.log
  summary: Actual exit0. Actual inventory 1 reviewed example occurrences and 1 typed
    protein nodes, all COVERED. Native identifier/coverage success does not establish
    direct complex membership, experimental strain equivalence or formation necessity.
  accessed_at: '2026-11-04T07:05:48.297845Z'
  support: supports
  snapshot_sha256: eb223ac083f57391ce0c3803caa2a5c83521d20ce6567dd4328061be11d34f60
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:11:09.661354Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 7ddca4deca40ade7b18c99c15e1f12e0b96b5ee7c8380ee423bdc5a8543815db
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:05:57.036978Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:05:35.013273Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:05:31.598614Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T07:05:59.540798Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T07:21:47Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 0f0ace16a57ba45f74a53cacb1480e5c253108c4f0ca50db2183d0009610229d
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T07:08:40.675011Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 8aebfee2ecac7b379a6b9b5f71a98d1b2288f1cd1b7c63cf1db3534e36f37301
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
- evidence_id: root-native-dnaa_hda_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:31.455252Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_hda_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hda_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:31.894556Z'
  support: context_only
  snapshot_sha256: c1b02a106da2af87da59359f83b31b146fdd3ba83f7f8364b563ee0084a53520
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_hu_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:32.907561Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_hu_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_hu_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:33.340523Z'
  support: context_only
  snapshot_sha256: ca286fe8a9cd7bb445c53da08a7fb8bc6512f82af088da76999eb9dbc8fc6787
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_l2_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:35.073354Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_l2_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_l2_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:35.480019Z'
  support: context_only
  snapshot_sha256: b5af99c8180d083ab55ba1f343531d77f1fddc4e7b84189669a4457b4b36d46a
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_oric_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:36.528903Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnaa_oric_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnaa_oric_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:36.939971Z'
  support: context_only
  snapshot_sha256: 13807089fc975c18288a1f1c653e3484de53f3588a33d875dda00c8ba20e577e
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:38.897929Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:39.301111Z'
  support: context_only
  snapshot_sha256: 1a5fd2b44858b3af069fb75cc2842754b9f929dcbcc7335cc4034fd26fcf138e
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_dnat_pria_prib_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:40.597126Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_dnat_pria_prib_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_prib_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:41.016178Z'
  support: context_only
  snapshot_sha256: da3be8302e150b5f1f300995c5bc908eaf804b9ec237b319e4ed1e1937955d35
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_dnat_pria_pric_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:42.252627Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_dnat_pria_pric_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_dnat_pria_pric_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:42.666946Z'
  support: context_only
  snapshot_sha256: a61be5ffd377d729d7aee4e31668d88690314dce25c4496b9f83c9d4636e782c
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_rep_pric_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:44.325762Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnac_rep_pric_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnac_rep_pric_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:44.731018Z'
  support: context_only
  snapshot_sha256: 6e9daeea33d397f83257ca4de9aacdc420b905a89c38bf3d23a0a5b10a4a6358
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnag_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:45.854437Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_dnag_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_dnag_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:46.253065Z'
  support: context_only
  snapshot_sha256: 678bd1bf9f8076805fae7422583c6b42be13e85b6d4dd79eb4960dddbb3d93b9
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_helicase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:47.824969Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-dnab_helicase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2389/dnab_helicase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T07:05:48.297845Z'
  support: context_only
  snapshot_sha256: eb223ac083f57391ce0c3803caa2a5c83521d20ce6567dd4328061be11d34f60
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-hda-identity
  area: identity
  topic: Binary DnaA-Hda versus full RIDA system
  outcome: supported
  summary: GO1990083 and replication-inhibiting protein-complex parent are exact.
    Keyamura direct contacts and staged assay support DnaA-Hda participation; DNA-loaded
    beta clamp and ADP-Hda context do not force a clamp constituent into the separately
    scoped binary record. Hda-beta-clamp GO1990085 remains distinct.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-go-1990083
  - micro-go-1990078
  - micro-go-1990085
  - micro-go-1990083-ancestors
  - micro-keyamura2011-pmc
  - micro-pmid-15150238
- assessment_id: micro-hda-chemistry
  area: evidence
  topic: ATP hydrolysis versus inherited phosphorylation wording
  outcome: concern
  summary: 'Current definition faithfully copies current GO but contradicts the staged
    primary assay and its own graph/canonical hydrolysis text: RIDA promotes hydrolysis
    of DnaA-bound ATP to ADP, not inhibition of ADP-to-ATP phosphorylation. DARS exchange
    is a separate reactivation pathway. Correct chemistry while explicitly retaining
    upstream attribution and exact complex identity.'
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-go-1990083
  - micro-keyamura2011-pmc
  - micro-pmid-21708944
- assessment_id: micro-hda-families
  area: grounding
  topic: Exact DnaA/Hda classes
  outcome: concern
  summary: IPR001957 DnaA and IPR017788 Hda are verified whole-protein families with
    matching P03004/P69931 xrefs. They can resolve existing label-only mapping tasks.
    IPR022864 is Enterobacteriaceae-specific and not the generic Hda class. No optional
    protein inventory is demanded.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR001957
  - micro-ipr-IPR017788
  - micro-ipr-IPR022864
  - micro-protein-P03004
  - micro-protein-P69931
- assessment_id: micro-hda-graph
  area: graph
  topic: Three descriptive membership/function edges
  outcome: supported
  summary: Two constituent edges and RIDA-support relation agree with authority and
    primary contact/hydrolysis assays. NONMECHANISTIC scope openly excludes clamp
    loading and detailed hydrolysis chemistry. Mutation-dependent reduced binding/activity
    is not proof that every missing partner prevents all binary complex formation.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-go-1990083
  - micro-go-0032297
  - micro-keyamura2011-pmc
- assessment_id: micro-hda-scope
  area: scope
  topic: K12-derived assays versus reference protein/localization contexts
  outcome: supported
  summary: Primary Methods enumerate KH5402-1/WM433/YT411/KA451/KA429/KA450 contexts
    and defined purified reactions; reviewed K12 examples are valid annotations, not
    an assertion that all assays use an unmodified reference strain. Native DnaA/Hda
    localization references have separate abstract/annotation tiers. Proposed contact
    model is not a solved structure.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-keyamura2011-pmc
  - micro-tax-562
  - micro-tax-83333
  - micro-protein-P03004
  - micro-protein-P69931
  - micro-pmid-12618445
- assessment_id: micro-hu-identity
  area: identity
  topic: HU-bound DnaA-origin complex and alternatives
  outcome: supported
  summary: Exact GO1990103 nucleoprotein identity is distinct from plain DnaA-oriC,
    DiaA stimulation and helicase loading. Complete Chodavarapu2008 primary abstract
    supports DnaA-HU interaction, oriC oligomer stabilization and relative alpha-dimer
    activity. Do not impose an invariant alpha-beta heterodimer.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-go-1990103
  - micro-go-1990103-ancestors
  - micro-go-1990101
  - micro-go-1990102
  - micro-go-1990100
  - micro-pmid-18179598
- assessment_id: micro-hu-grounding
  area: grounding
  topic: DnaA and oriC exact classes; HU complex boundary
  outcome: concern
  summary: DnaA IPR001957 and oriC SO0000953 are exact source-neutral mappings for
    existing constituents. HU dimer is a PROTEIN_COMPLEX, so neither individual HU
    family nor one compulsory subunit combination replaces its unresolved whole-complex
    identity. hupa/hupb queries used only as contextual native loci.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-schema
  - micro-ipr-IPR001957
  - micro-so-0000953
  - micro-protein-P03004
  - micro-gene-hupA
  - micro-gene-hupB
  - micro-pmid-18179598
- assessment_id: micro-hu-graph
  area: graph
  topic: Four coarse initiation edges
  outcome: supported
  summary: DnaA/HU membership, oriC scaffold and initiation support agree with exact
    GO and complete primary abstract. Scope explicitly withholds subunit choice, oligomerization
    and later loading mechanics, and does not restore an unverified bending mechanism.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-graph-policy
  - micro-go-1990103
  - micro-go-0006270
  - micro-pmid-18179598
- assessment_id: micro-hu-scope
  area: scope
  topic: Abstract-supported E.coli assays and unverified broad necessity
  outcome: unknown
  summary: Species-level E.coli context and HU alternatives/stimulation are supported.
    Fresh publisher and PDF403 leave full methods, experimental strain and universal
    bacterial-necessity wording unverified, not disproved. The essential-in-bacteria
    sentence is accurately GO-attributed but is not independently certified as a taxon-wide
    formation or viability conclusion.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-go-1990103
  - micro-go-1990103-constraints
  - micro-pmid-18179598
  - micro-chodavarapu2008-publisher-access
  - micro-chodavarapu2008-pdf-access
  - micro-tax-562
  - micro-tax-83333
- assessment_id: micro-l2-identity
  area: identity
  topic: Binary inhibitory contact rather than whole ribosome
  outcome: supported
  summary: GO1990082 and inhibitory protein-complex parent agree with measured mature/truncated
    L2 contact with DnaA. Generic ribosomal membership/functions do not imply a ribosome
    constituent or prove DnaA interaction without the primary contact study.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-go-1990082
  - micro-go-1990078
  - micro-go-1990082-ancestors
  - micro-chodavarapu2011-jats
- assessment_id: micro-l2-grounding
  area: grounding
  topic: DnaA and bacterial/organellar uL2 exact families
  outcome: concern
  summary: Existing label-only classes have exact whole-protein IPR001957 and IPR005880,
    independently corroborated by P03004/P60422. Universal uL2 IPR002171 is a broader
    parent with separate archaeal/eukaryotic branch. Keep native gene rplB, reviewed
    K12 identity and historical 50S-L2 label correspondence.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR001957
  - micro-ipr-IPR005880
  - micro-ipr-IPR002171-retry
  - micro-protein-P03004
  - micro-protein-P60422
- assessment_id: micro-l2-graph
  area: graph
  topic: Direct contact and inhibited in-vitro initiation
  outcome: supported
  summary: Three edges accurately describe constituent contact and inhibitory function.
    Primary ELISA, oriC-unwinding and prepriming assays support these statements;
    reduced recovered DnaA/DnaB supports proposed oligomer destabilization, not a
    solved interface, fixed stoichiometry or detailed cleavage mechanism. NONMECHANISTIC
    scope keeps these distinctions.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-graph-policy
  - micro-go-1990082
  - micro-go-0032297
  - micro-chodavarapu2011-jats
- assessment_id: micro-l2-scope
  area: scope
  topic: Mature/truncated preparations and physiological uncertainty
  outcome: supported
  summary: The tL2 purification is from DM700, with separate MG1655/W3110 observations
    and defined reactions; reference K12 accession does not identify every preparation.
    Discussion leaves physiological regulation proposed and reports a negative tested
    tL2 in-vivo initiation assay. Current graph explicitly excludes in-vivo stringent-response
    context; no broader in-vivo checkpoint is certified.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-chodavarapu2011-jats
  - micro-pmid-21288885
  - micro-tax-562
  - micro-tax-83333
  - micro-protein-P60422
- assessment_id: micro-oric-identity
  area: identity
  topic: Initial DnaA-origin assembly boundary
  outcome: supported
  summary: Exact GO1990101 nucleoprotein identity and initiation-complex parent are
    appropriate; plain DnaA/oriC scope does not require DiaA, DnaB-DnaC, HU or later
    primosome components. Current GO definitions and Miller primary binding/assembly
    assays support the named early complex.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-go-1990101
  - micro-go-1990077
  - micro-go-1990101-ancestors
  - micro-go-1990102
  - micro-go-1990100
  - micro-miller2009-pmc
- assessment_id: micro-oric-grounding
  area: grounding
  topic: Existing protein family and origin feature classes
  outcome: concern
  summary: DnaA IPR001957 and oriC SO0000953 exactly ground the maintained classes
    and can resolve/narrow the existing mapping task. Correct P03004 taxon example
    is separate from family identity; no single origin-sequence accession or broad
    homolog/domain substitute is required.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-schema
  - micro-ipr-IPR001957
  - micro-so-0000953
  - micro-protein-P03004
- assessment_id: micro-oric-graph
  area: graph
  topic: Three bounded origin-seeding edges
  outcome: supported
  summary: DnaA membership, oriC scaffold and initiation support match the current
    source. Miller high-affinity-site mutants affect normal-concentration assembly
    but elevated DnaA can restore weak-site filling; the record does not claim universal
    loss of formation. Coarse NONMECHANISTIC scope does not overstate exact oligomer
    geometry or later loading.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-graph-policy
  - micro-go-1990101
  - micro-go-0006270
  - micro-miller2009-pmc
- assessment_id: micro-oric-scope
  area: scope
  topic: Actual strain/protein/mutant contexts
  outcome: supported
  summary: Miller Methods distinguish P3478/isogenic W3110, PC2 dnaCts and purified
    tagged DnaA. DMS footprints, crosslinks and EMSA support bounded site-assisted
    assembly; no raw footprint reanalysis or pixel interpretation was performed. Reference
    K12 annotation and localization abstracts do not substitute for these experiment
    contexts.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-miller2009-pmc
  - micro-tax-562
  - micro-tax-83333
  - micro-protein-P03004
- assessment_id: micro-proteins-0
  area: grounding
  topic: Current reviewed example identities and query bounds
  outcome: supported
  summary: Maintained P03004 DnaA, P69931 Hda identities agree with native reviewed
    status, primary genes/ordered loci and taxon83333. Current exact reviewed queries
    are singleton; no historical query reconstruction. Localization papers are abstract/native-annotation
    tier and do not prove physical membership by themselves.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-tax-83333
  - micro-protein-P03004
  - micro-gene-dnaA
  - micro-pmid-22574163
  - micro-pmid-28166228
  - micro-pmid-9478970
  - micro-protein-P69931
  - micro-gene-hda
  - micro-pmid-12618445
- assessment_id: micro-formation-0
  area: grounding
  topic: Physical formation distinct from activity and viability
  outcome: unknown
  summary: 'Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition,
    origin function and organism viability are not universal constituent-absence formation
    assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL
    classification is requested.'
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-schema
  - micro-policy
  - micro-keyamura2011-pmc
- assessment_id: micro-inputs-0
  area: provenance
  topic: Original frozen inputs versus current target
  outcome: supported
  summary: Record is unchanged on current main. Original source revisions/hashes and
    immutable YAML/Markdown were verified; independent present source reading does
    not invent a stale refresh or erase historical access limits.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-original-audit
- assessment_id: micro-adapter-0
  area: scope
  topic: Positive replication pathways require matched structured-source context
  outcome: concern
  summary: Original formal expression-only exclusion is unsupported for named molecular
    replication narratives. Fresh catalogue selects actual E.coli precise1k; five
    exact native loci each checked against201 modules. Only rplB b3317 passes module1
    Translation threshold, confirmed in53-member list. Five-strain coverage differs
    from particular mutant/reconstitution preparations. Hits are not assembly/direct
    regulation; nonhits are not absence. No generated AI summaries or activities used.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-adapter-module1
  - micro-adapter-module1-genes
  - micro-historical-runner
  - micro-ecoli-gene-b3702
  - micro-ecoli-gene-b2496
  - micro-ecoli-gene-b3317
  - micro-ecoli-gene-b4000
  - micro-ecoli-gene-b0440
- assessment_id: micro-native-0
  area: schema
  topic: Actual native validation and protein coverage
  outcome: supported
  summary: 2 reviewed examples/2 COVERED typed protein nodes; both current native
    commands actually exit0. HU complex and origin feature nodes are outside the protein-only
    inventory and separately assessed. Native success does not settle exact class
    mapping or full scientific completeness; original validate/render also pass.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-native-dnaa_hda_complex-verify
  - micro-native-dnaa_hda_complex-causal
  - micro-original-audit
- assessment_id: micro-history-0
  area: provenance
  topic: Append-only prior rationale and scope resolutions
  outcome: supported
  summary: Earlier reference-protein additions and historical deferral statements
    are preserved as provenance, not treated as false current inventories. Existing
    interpretation boundaries are supported; exact family/feature actions append evidence
    and narrow current prompts/notes while preserving rationale/posed_date. No grouped
    or neighboring issue is terminally resolved.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-prior-0
- assessment_id: micro-coverage-0
  area: completeness
  topic: Complete maintained record and access bounds
  outcome: supported
  summary: All current fields/original review examined. No maintained image or physical
    measurement requires pixel/unit review. Source-body, complete-abstract, native
    ontology/family/protein and failed-access tiers remain distinct; optional omissions
    and unknowns alone are not findings.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-schema
- assessment_id: micro-verdict-0
  area: other
  topic: Current independent scientific disposition
  outcome: concern
  summary: 'needs_curation: inherited major chemistry and minor exact-family findings
    retained; supported binary identity and bounded RIDA graph preserved.'
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-proteins-1
  area: grounding
  topic: Current reviewed example identities and query bounds
  outcome: supported
  summary: Maintained P03004 DnaA identities agree with native reviewed status, primary
    genes/ordered loci and taxon83333. Current exact reviewed queries are singleton;
    no historical query reconstruction. Localization papers are abstract/native-annotation
    tier and do not prove physical membership by themselves.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-tax-83333
  - micro-protein-P03004
  - micro-gene-dnaA
  - micro-pmid-22574163
  - micro-pmid-28166228
  - micro-pmid-9478970
- assessment_id: micro-formation-1
  area: grounding
  topic: Physical formation distinct from activity and viability
  outcome: unknown
  summary: 'Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition,
    origin function and organism viability are not universal constituent-absence formation
    assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL
    classification is requested.'
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-schema
  - micro-policy
  - micro-pmid-18179598
- assessment_id: micro-inputs-1
  area: provenance
  topic: Original frozen inputs versus current target
  outcome: supported
  summary: Record is unchanged on current main. Original source revisions/hashes and
    immutable YAML/Markdown were verified; independent present source reading does
    not invent a stale refresh or erase historical access limits.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-delta-1
  - micro-original-audit
- assessment_id: micro-adapter-1
  area: scope
  topic: Positive replication pathways require matched structured-source context
  outcome: concern
  summary: Original formal expression-only exclusion is unsupported for named molecular
    replication narratives. Fresh catalogue selects actual E.coli precise1k; five
    exact native loci each checked against201 modules. Only rplB b3317 passes module1
    Translation threshold, confirmed in53-member list. Five-strain coverage differs
    from particular mutant/reconstitution preparations. Hits are not assembly/direct
    regulation; nonhits are not absence. No generated AI summaries or activities used.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-adapter-module1
  - micro-adapter-module1-genes
  - micro-historical-runner
  - micro-ecoli-gene-b3702
  - micro-ecoli-gene-b2496
  - micro-ecoli-gene-b3317
  - micro-ecoli-gene-b4000
  - micro-ecoli-gene-b0440
- assessment_id: micro-native-1
  area: schema
  topic: Actual native validation and protein coverage
  outcome: supported
  summary: 1 reviewed examples/1 COVERED typed protein nodes; both current native
    commands actually exit0. HU complex and origin feature nodes are outside the protein-only
    inventory and separately assessed. Native success does not settle exact class
    mapping or full scientific completeness; original validate/render also pass.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-native-dnaa_hu_complex-verify
  - micro-native-dnaa_hu_complex-causal
  - micro-original-audit
- assessment_id: micro-history-1
  area: provenance
  topic: Append-only prior rationale and scope resolutions
  outcome: supported
  summary: Earlier reference-protein additions and historical deferral statements
    are preserved as provenance, not treated as false current inventories. Existing
    interpretation boundaries are supported; exact family/feature actions append evidence
    and narrow current prompts/notes while preserving rationale/posed_date. No grouped
    or neighboring issue is terminally resolved.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-prior-1
- assessment_id: micro-coverage-1
  area: completeness
  topic: Complete maintained record and access bounds
  outcome: supported
  summary: All current fields/original review examined. No maintained image or physical
    measurement requires pixel/unit review. Source-body, complete-abstract, native
    ontology/family/protein and failed-access tiers remain distinct; optional omissions
    and unknowns alone are not findings.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-schema
- assessment_id: micro-verdict-1
  area: other
  topic: Current independent scientific disposition
  outcome: concern
  summary: 'needs_curation: inherited minor DnaA/oriC exact mappings retained; HU
    alternatives and abstract-only/universal-necessity limitations preserved.'
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-proteins-2
  area: grounding
  topic: Current reviewed example identities and query bounds
  outcome: supported
  summary: Maintained P03004 DnaA, P60422 rplB/uL2 identities agree with native reviewed
    status, primary genes/ordered loci and taxon83333. Current exact reviewed queries
    are singleton; no historical query reconstruction. Localization papers are abstract/native-annotation
    tier and do not prove physical membership by themselves.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-tax-83333
  - micro-protein-P03004
  - micro-gene-dnaA
  - micro-pmid-22574163
  - micro-pmid-28166228
  - micro-pmid-9478970
  - micro-protein-P60422
  - micro-gene-rplB
- assessment_id: micro-formation-2
  area: grounding
  topic: Physical formation distinct from activity and viability
  outcome: unknown
  summary: 'Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition,
    origin function and organism viability are not universal constituent-absence formation
    assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL
    classification is requested.'
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-schema
  - micro-policy
  - micro-chodavarapu2011-jats
- assessment_id: micro-inputs-2
  area: provenance
  topic: Original frozen inputs versus current target
  outcome: supported
  summary: Record is unchanged on current main. Original source revisions/hashes and
    immutable YAML/Markdown were verified; independent present source reading does
    not invent a stale refresh or erase historical access limits.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-delta-2
  - micro-original-audit
- assessment_id: micro-adapter-2
  area: scope
  topic: Positive replication pathways require matched structured-source context
  outcome: concern
  summary: Original formal expression-only exclusion is unsupported for named molecular
    replication narratives. Fresh catalogue selects actual E.coli precise1k; five
    exact native loci each checked against201 modules. Only rplB b3317 passes module1
    Translation threshold, confirmed in53-member list. Five-strain coverage differs
    from particular mutant/reconstitution preparations. Hits are not assembly/direct
    regulation; nonhits are not absence. No generated AI summaries or activities used.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-adapter-module1
  - micro-adapter-module1-genes
  - micro-historical-runner
  - micro-ecoli-gene-b3702
  - micro-ecoli-gene-b2496
  - micro-ecoli-gene-b3317
  - micro-ecoli-gene-b4000
  - micro-ecoli-gene-b0440
- assessment_id: micro-native-2
  area: schema
  topic: Actual native validation and protein coverage
  outcome: supported
  summary: 2 reviewed examples/2 COVERED typed protein nodes; both current native
    commands actually exit0. HU complex and origin feature nodes are outside the protein-only
    inventory and separately assessed. Native success does not settle exact class
    mapping or full scientific completeness; original validate/render also pass.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-native-dnaa_l2_complex-verify
  - micro-native-dnaa_l2_complex-causal
  - micro-original-audit
- assessment_id: micro-history-2
  area: provenance
  topic: Append-only prior rationale and scope resolutions
  outcome: supported
  summary: Earlier reference-protein additions and historical deferral statements
    are preserved as provenance, not treated as false current inventories. Existing
    interpretation boundaries are supported; exact family/feature actions append evidence
    and narrow current prompts/notes while preserving rationale/posed_date. No grouped
    or neighboring issue is terminally resolved.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-prior-2
- assessment_id: micro-coverage-2
  area: completeness
  topic: Complete maintained record and access bounds
  outcome: supported
  summary: All current fields/original review examined. No maintained image or physical
    measurement requires pixel/unit review. Source-body, complete-abstract, native
    ontology/family/protein and failed-access tiers remain distinct; optional omissions
    and unknowns alone are not findings.
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-schema
- assessment_id: micro-verdict-2
  area: other
  topic: Current independent scientific disposition
  outcome: concern
  summary: 'needs_curation: inherited minor exact DnaA/uL2 family mapping retained;
    in-vitro contact/function and physiological uncertainty preserved.'
  target_ids:
  - GO:1990082
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-proteins-3
  area: grounding
  topic: Current reviewed example identities and query bounds
  outcome: supported
  summary: Maintained P03004 DnaA identities agree with native reviewed status, primary
    genes/ordered loci and taxon83333. Current exact reviewed queries are singleton;
    no historical query reconstruction. Localization papers are abstract/native-annotation
    tier and do not prove physical membership by themselves.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-tax-83333
  - micro-protein-P03004
  - micro-gene-dnaA
  - micro-pmid-22574163
  - micro-pmid-28166228
  - micro-pmid-9478970
- assessment_id: micro-formation-3
  area: grounding
  topic: Physical formation distinct from activity and viability
  outcome: unknown
  summary: 'Maintained UNKNOWN essentiality is defensible: contact, stimulation/inhibition,
    origin function and organism viability are not universal constituent-absence formation
    assays. No compulsory new depletion experiment, optional inventory or global ESSENTIAL
    classification is requested.'
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-schema
  - micro-policy
  - micro-miller2009-pmc
- assessment_id: micro-inputs-3
  area: provenance
  topic: Original frozen inputs versus current target
  outcome: supported
  summary: Record is unchanged on current main. Original source revisions/hashes and
    immutable YAML/Markdown were verified; independent present source reading does
    not invent a stale refresh or erase historical access limits.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-delta-3
  - micro-original-audit
- assessment_id: micro-adapter-3
  area: scope
  topic: Positive replication pathways require matched structured-source context
  outcome: concern
  summary: Original prose-only adapter exclusion is unsupported for named molecular
    replication narratives. Fresh catalogue selects actual E.coli precise1k; five
    exact native loci each checked against201 modules. Only rplB b3317 passes module1
    Translation threshold, confirmed in53-member list. Five-strain coverage differs
    from particular mutant/reconstitution preparations. Hits are not assembly/direct
    regulation; nonhits are not absence. No generated AI summaries or activities used.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-native-policy
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-adapter-module1
  - micro-adapter-module1-genes
  - micro-historical-runner
  - micro-ecoli-gene-b3702
  - micro-ecoli-gene-b2496
  - micro-ecoli-gene-b3317
  - micro-ecoli-gene-b4000
  - micro-ecoli-gene-b0440
- assessment_id: micro-native-3
  area: schema
  topic: Actual native validation and protein coverage
  outcome: supported
  summary: 1 reviewed examples/1 COVERED typed protein nodes; both current native
    commands actually exit0. HU complex and origin feature nodes are outside the protein-only
    inventory and separately assessed. Native success does not settle exact class
    mapping or full scientific completeness; original validate/render also pass.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-native-dnaa_oric_complex-verify
  - micro-native-dnaa_oric_complex-causal
  - micro-original-audit
- assessment_id: micro-history-3
  area: provenance
  topic: Append-only prior rationale and scope resolutions
  outcome: supported
  summary: Earlier reference-protein additions and historical deferral statements
    are preserved as provenance, not treated as false current inventories. Existing
    interpretation boundaries are supported; exact family/feature actions append evidence
    and narrow current prompts/notes while preserving rationale/posed_date. No grouped
    or neighboring issue is terminally resolved.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-prior-3
- assessment_id: micro-coverage-3
  area: completeness
  topic: Complete maintained record and access bounds
  outcome: supported
  summary: All current fields/original review examined. No maintained image or physical
    measurement requires pixel/unit review. Source-body, complete-abstract, native
    ontology/family/protein and failed-access tiers remain distinct; optional omissions
    and unknowns alone are not findings.
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-schema
- assessment_id: micro-verdict-3
  area: other
  topic: Current independent scientific disposition
  outcome: concern
  summary: 'needs_curation: inherited minor exact DnaA/oriC class mappings retained;
    correct early-complex scope and source-bounded assembly model preserved.'
  target_ids:
  - GO:1990101
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-policy
- assessment_id: micro-kind-0-keyamura2011-legacy-access
  area: provenance
  topic: Historical failed-access classification
  outcome: concern
  summary: Original access failure and context_only limits were honest, but a failed/challenge
    diagnostic is incorrectly typed database. Successor retains exact original observation
    time/hash as validation/context_only; no new body-read assertion or biological
    refutation follows.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-prior-0
  - micro-historical-0-keyamura2011-legacy-access
- assessment_id: micro-kind-0-keyamura2011-xml-access
  area: provenance
  topic: Historical failed-access classification
  outcome: concern
  summary: Original access failure and context_only limits were honest, but a failed/challenge
    diagnostic is incorrectly typed database. Successor retains exact original observation
    time/hash as validation/context_only; no new body-read assertion or biological
    refutation follows.
  target_ids:
  - GO:1990083
  evidence_ids:
  - micro-prior-0
  - micro-historical-0-keyamura2011-xml-access
- assessment_id: micro-kind-1-chodavarapu2008-publisher-access
  area: provenance
  topic: Historical failed-access classification
  outcome: concern
  summary: Original access failure and context_only limits were honest, but a failed/challenge
    diagnostic is incorrectly typed database. Successor retains exact original observation
    time/hash as validation/context_only; no new body-read assertion or biological
    refutation follows.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-prior-1
  - micro-historical-1-chodavarapu2008-publisher-access
- assessment_id: micro-kind-1-chodavarapu2008-pdf-access
  area: provenance
  topic: Historical failed-access classification
  outcome: concern
  summary: Original access failure and context_only limits were honest, but a failed/challenge
    diagnostic is incorrectly typed database. Successor retains exact original observation
    time/hash as validation/context_only; no new body-read assertion or biological
    refutation follows.
  target_ids:
  - GO:1990103
  evidence_ids:
  - micro-prior-1
  - micro-historical-1-chodavarapu2008-pdf-access
- assessment_id: plaque-t4-identity-hierarchy
  area: identity
  topic: identity hierarchy
  outcome: supported
  summary: The maintained ID, label and parent distinguish the exact native GO class.
    Direct hierarchy is not inferred from broad ancestry; retaining the correct ontology
    identity does not erase separately identified source-stage conflicts.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-go
  - plaque-go-1990100-ancestors
  - plaque-go-1990100-constraints
- assessment_id: plaque-t4-family-groundings
  area: grounding
  topic: family groundings
  outcome: concern
  summary: DnaB IPR007692 and exact unintegrated DnaC NCBIfamNF005931 are available;
    broad IPR028350 is not substituted. Correct individual examples remain instances
    rather than class groundings.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-ipr-IPR007692
  - plaque-ncbifam-NF005931
  - plaque-ipr-IPR028350
  - plaque-curation
  - plaque-up-P0ACB0
  - plaque-up-P0AEF0
- assessment_id: plaque-t4-protein-identities
  area: grounding
  topic: protein identities
  outcome: supported
  summary: 2 current examples are reviewed exact gene/taxon83333 entries with matching
    primary symbols and locus tokens; exact-organism searches each return one reviewed
    entry. Native commands passed with 2 COVERED typed protein nodes. Identity consistency
    is not independent experimental membership proof.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-native-dnab_dnac_complex-verify
  - plaque-native-dnab_dnac_complex-causal
  - plaque-tax-83333
  - plaque-up-P0ACB0
  - plaque-up-P0AEF0
  - plaque-gene-dnaB
  - plaque-gene-dnaC
- assessment_id: plaque-t4-source-assembly-stage
  area: evidence
  topic: source assembly stage
  outcome: supported
  summary: Makowska-Grzyska/Kaguni directly supports DnaC-dependent DnaB delivery
    and staged release at oriC. Mutant loading and primase/rNTP effects are condition-scoped,
    not a universal stoichiometric or necessity rule.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-pmid-20129058
  - plaque-makowska2010-body
  - plaque-go
  - plaque-rubric
- assessment_id: plaque-t4-taxon-source-boundaries
  area: scope
  topic: taxon source boundaries
  outcome: supported
  summary: E. coli species562 and reference K-12 taxon83333 are correctly separated.
    Protein reference identities do not identify every experimental derivative. The
    inspected sources concern purified E. coli proteins and the stated oriC or PhiX174
    substrates; ontology taxon constraints and one study do not measure broad prevalence.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-makowska2010-body
  - plaque-go-1990100-constraints
- assessment_id: plaque-t4-stoichiometry-formation
  area: quantity
  topic: stoichiometry formation
  outcome: supported
  summary: Six DnaB subunits are supported; leaving DnaC count uncommitted respects
    multiple loading contexts and measured versus modeled ratios. UNKNOWN formation
    is not a viability inference.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-curation
  - plaque-makowska2010-body
  - plaque-go
- assessment_id: plaque-t4-graph-mechanism
  area: graph
  topic: graph mechanism
  outcome: supported
  summary: The NON_MECHANISTIC graph keeps proteins, structure and biological processes
    distinct; broad protein families/complexes are allowed by native GENE_OR_PROTEIN
    policy. Its membership and delivery/initiation associations are supported without
    inventing quantitative kinetics.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-structure-schema
  - plaque-graph-skill
  - plaque-native-dnab_dnac_complex-verify
  - plaque-native-dnab_dnac_complex-causal
  - plaque-makowska2010-body
- assessment_id: plaque-t4-structured-source-applicability
  area: evidence
  topic: structured source applicability
  outcome: supported
  summary: 'Positive named molecular components, loading/restart functions and gene
    examples trigger the broad structured-source policy. Current E. coli precise1k
    coverage and exact matched loci were inspected: five-strain context, 201 membership
    rows per locus, and priB module1/53-member context where applicable. These are
    expression context only; absence of an expression-module claim never established
    the original exclusion. No fresh adapter runner execution is claimed.'
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-review-skill
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-modules
  - plaque-adapter-b4052-gene
  - plaque-adapter-b4052-modules
  - plaque-adapter-b4361-gene
  - plaque-adapter-b4361-modules
- assessment_id: plaque-t4-history-and-original-verdict
  area: provenance
  topic: history and original verdict
  outcome: concern
  summary: Current record bytes match the original frozen target. Existing needs_curation
    verdict and exact inherited finding lineage are reconfirmed with fresh independent
    evidence. The unsupported notes[1] prose exclusion is a bundle assessment defect
    to correct additively. Dated rationale/history remain append-only; no record status
    promotion or terminal disposition is inferred.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-original-4-yaml
  - plaque-original-4-md
  - plaque-input-original-proof
  - plaque-curation
  - plaque-review-contract
- assessment_id: plaque-t4-schema-input-integrity
  area: schema
  topic: schema input integrity
  outcome: supported
  summary: The original native YAML validates and its renderer reproduces the committed
    Markdown exactly. All historical input occurrences and current frozen hashes were
    checked. These deterministic results do not certify scientific claims, future
    CI, or merge readiness.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-native-dnab_dnac_complex-verify
  - plaque-native-dnab_dnac_complex-causal
- assessment_id: plaque-t4-coverage-and-verdict
  area: completeness
  topic: coverage and verdict
  outcome: concern
  summary: Whole record and all original findings/actions were reviewed. Needs_curation
    is retained for the bounded exact-family grounding gap. No optional protein inventory,
    unresolved PAS-DNA class, unread figure or unmeasured universal necessity was
    manufactured as an additional finding.
  target_ids:
  - GO:1990100
  evidence_ids:
  - plaque-record-4
  - plaque-original-4-yaml
  - plaque-rubric
  - plaque-curation
  - plaque-input-original-proof
- assessment_id: plaque-t5-identity-hierarchy
  area: identity
  topic: identity hierarchy
  outcome: supported
  summary: The maintained ID, label and parent distinguish the exact native GO class.
    Direct hierarchy is not inferred from broad ancestry; retaining the correct ontology
    identity does not erase separately identified source-stage conflicts.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-go
  - plaque-go-1990158-ancestors
  - plaque-go-1990158-constraints
- assessment_id: plaque-t5-family-groundings
  area: grounding
  topic: family groundings
  outcome: concern
  summary: DnaT IPR020917 and PriA IPR005259 plus PriB IPR023646 are verified exact
    families. Current REVIEWED_LABEL_ONLY and active TODO remain actionable; historical
    earlier-pass statements need not be rewritten. Correct individual examples remain
    instances rather than class groundings.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-ipr-IPR020917
  - plaque-ipr-IPR005259
  - plaque-ipr-IPR023646
  - plaque-curation
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P07013
- assessment_id: plaque-t5-protein-identities
  area: grounding
  topic: protein identities
  outcome: supported
  summary: 3 current examples are reviewed exact gene/taxon83333 entries with matching
    primary symbols and locus tokens; exact-organism searches each return one reviewed
    entry. Native commands passed with 3 COVERED typed protein nodes. Identity consistency
    is not independent experimental membership proof.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-native-dnab_dnac_dnat_pria_prib_complex-verify
  - plaque-native-dnab_dnac_dnat_pria_prib_complex-causal
  - plaque-tax-83333
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P07013
  - plaque-gene-dnaT
  - plaque-gene-priA
  - plaque-gene-priB
- assessment_id: plaque-t5-source-assembly-stage
  area: evidence
  topic: source assembly stage
  outcome: concern
  summary: NgI short PAS and NgII intact PhiX174 products must be distinguished from
    the GO-defined DnaC-containing loading intermediate. NgII retains PriB/PriC and
    excludes stable DnaC; supplied factors are not isolated constituents. The canonical
    example and unqualified has_part/component/graph claim conflate these stages.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-pmid-8663104
  - plaque-pmid-8663105
  - plaque-ng1996ii-pdf
  - plaque-go
  - plaque-rubric
- assessment_id: plaque-t5-taxon-source-boundaries
  area: scope
  topic: taxon source boundaries
  outcome: supported
  summary: E. coli species562 and reference K-12 taxon83333 are correctly separated.
    Protein reference identities do not identify every experimental derivative. The
    inspected sources concern purified E. coli proteins and the stated oriC or PhiX174
    substrates; ontology taxon constraints and one study do not measure broad prevalence.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-ng1996ii-pdf
  - plaque-go-1990158-constraints
- assessment_id: plaque-t5-stoichiometry-formation
  area: quantity
  topic: stoichiometry formation
  outcome: unknown
  summary: No new universal essentiality claim is justified for the exact maintained
    intermediate from a different isolated cohort. NgII PriA-omission and PriC-dependent
    effects have stated substrate/assay scope. Unknown PAS-DNA grounding and unresolved
    copy numbers are retained, not forced into oriC or an invariant oligomer.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-curation
  - plaque-ng1996ii-pdf
  - plaque-go
- assessment_id: plaque-t5-graph-mechanism
  area: graph
  topic: graph mechanism
  outcome: concern
  summary: The NON_MECHANISTIC graph keeps proteins, structure and biological processes
    distinct; broad protein families/complexes are allowed by native GENE_OR_PROTEIN
    policy. Correct node types and covered examples do not cure the source-stage/cohort
    issue in membership and downstream source notes; qualify those edges while preserving
    identity.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-structure-schema
  - plaque-graph-skill
  - plaque-native-dnab_dnac_dnat_pria_prib_complex-verify
  - plaque-native-dnab_dnac_dnat_pria_prib_complex-causal
  - plaque-ng1996ii-pdf
  - plaque-pmid-8663104
- assessment_id: plaque-t5-structured-source-applicability
  area: evidence
  topic: structured source applicability
  outcome: supported
  summary: 'Positive named molecular components, loading/restart functions and gene
    examples trigger the broad structured-source policy. Current E. coli precise1k
    coverage and exact matched loci were inspected: five-strain context, 201 membership
    rows per locus, and priB module1/53-member context where applicable. These are
    expression context only; absence of an expression-module claim never established
    the original exclusion. No fresh adapter runner execution is claimed.'
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-review-skill
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-modules
  - plaque-adapter-b4362-gene
  - plaque-adapter-b4362-modules
  - plaque-adapter-b3935-gene
  - plaque-adapter-b3935-modules
  - plaque-adapter-b4201-gene
  - plaque-adapter-b4201-modules
  - plaque-adapter-module1
  - plaque-adapter-module1-genes
- assessment_id: plaque-t5-history-and-original-verdict
  area: provenance
  topic: history and original verdict
  outcome: concern
  summary: Current record bytes match the original frozen target. Existing needs_curation
    verdict and exact inherited finding lineage are reconfirmed with fresh independent
    evidence. The unsupported notes[1] prose exclusion is a bundle assessment defect
    to correct additively. Dated rationale/history remain append-only; no record status
    promotion or terminal disposition is inferred.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-original-5-yaml
  - plaque-original-5-md
  - plaque-input-original-proof
  - plaque-curation
  - plaque-review-contract
- assessment_id: plaque-t5-schema-input-integrity
  area: schema
  topic: schema input integrity
  outcome: supported
  summary: The original native YAML validates and its renderer reproduces the committed
    Markdown exactly. All historical input occurrences and current frozen hashes were
    checked. These deterministic results do not certify scientific claims, future
    CI, or merge readiness.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-native-dnab_dnac_dnat_pria_prib_complex-verify
  - plaque-native-dnab_dnac_dnat_pria_prib_complex-causal
- assessment_id: plaque-t5-coverage-and-verdict
  area: completeness
  topic: coverage and verdict
  outcome: concern
  summary: Whole record and all original findings/actions were reviewed. Needs_curation
    is retained for the material source-stage/cohort conflict and bounded exact-family
    grounding gap. No optional protein inventory, unresolved PAS-DNA class, unread
    figure or unmeasured universal necessity was manufactured as an additional finding.
  target_ids:
  - GO:1990158
  evidence_ids:
  - plaque-record-5
  - plaque-original-5-yaml
  - plaque-rubric
  - plaque-curation
  - plaque-input-original-proof
- assessment_id: plaque-t6-identity-hierarchy
  area: identity
  topic: identity hierarchy
  outcome: supported
  summary: The maintained ID, label and parent distinguish the exact native GO class.
    Direct hierarchy is not inferred from broad ancestry; retaining the correct ontology
    identity does not erase separately identified source-stage conflicts.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-go
  - plaque-go-1990159-ancestors
  - plaque-go-1990159-constraints
- assessment_id: plaque-t6-family-groundings
  area: grounding
  topic: family groundings
  outcome: concern
  summary: DnaT IPR020917 and PriA IPR005259 plus PriC IPR010890 are verified exact
    families. Current REVIEWED_LABEL_ONLY and active TODO remain actionable; historical
    earlier-pass statements need not be rewritten. Correct individual examples remain
    instances rather than class groundings.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-ipr-IPR020917
  - plaque-ipr-IPR005259
  - plaque-ipr-IPR010890
  - plaque-curation
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P23862
- assessment_id: plaque-t6-protein-identities
  area: grounding
  topic: protein identities
  outcome: supported
  summary: 3 current examples are reviewed exact gene/taxon83333 entries with matching
    primary symbols and locus tokens; exact-organism searches each return one reviewed
    entry. Native commands passed with 3 COVERED typed protein nodes. Identity consistency
    is not independent experimental membership proof.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-native-dnab_dnac_dnat_pria_pric_complex-verify
  - plaque-native-dnab_dnac_dnat_pria_pric_complex-causal
  - plaque-tax-83333
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P23862
  - plaque-gene-dnaT
  - plaque-gene-priA
  - plaque-gene-priC
- assessment_id: plaque-t6-source-assembly-stage
  area: evidence
  topic: source assembly stage
  outcome: concern
  summary: NgI short PAS and NgII intact PhiX174 products must be distinguished from
    the GO-defined DnaC-containing loading intermediate. NgII retains PriB/PriC and
    excludes stable DnaC; supplied factors are not isolated constituents. The PriB-excluded
    canonical cohort and directly attributed replication-through-restart outcome overstate
    this study.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-pmid-8663104
  - plaque-pmid-8663105
  - plaque-ng1996ii-pdf
  - plaque-go
  - plaque-rubric
- assessment_id: plaque-t6-taxon-source-boundaries
  area: scope
  topic: taxon source boundaries
  outcome: supported
  summary: E. coli species562 and reference K-12 taxon83333 are correctly separated.
    Protein reference identities do not identify every experimental derivative. The
    inspected sources concern purified E. coli proteins and the stated oriC or PhiX174
    substrates; ontology taxon constraints and one study do not measure broad prevalence.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-ng1996ii-pdf
  - plaque-go-1990159-constraints
- assessment_id: plaque-t6-stoichiometry-formation
  area: quantity
  topic: stoichiometry formation
  outcome: unknown
  summary: No new universal essentiality claim is justified for the exact maintained
    intermediate from a different isolated cohort. NgII PriA-omission and PriC-dependent
    effects have stated substrate/assay scope. Unknown PAS-DNA grounding and unresolved
    copy numbers are retained, not forced into oriC or an invariant oligomer.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-curation
  - plaque-ng1996ii-pdf
  - plaque-go
- assessment_id: plaque-t6-graph-mechanism
  area: graph
  topic: graph mechanism
  outcome: concern
  summary: The NON_MECHANISTIC graph keeps proteins, structure and biological processes
    distinct; broad protein families/complexes are allowed by native GENE_OR_PROTEIN
    policy. Correct node types and covered examples do not cure the source-stage/cohort
    issue in membership and downstream source notes; qualify those edges while preserving
    identity.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-structure-schema
  - plaque-graph-skill
  - plaque-native-dnab_dnac_dnat_pria_pric_complex-verify
  - plaque-native-dnab_dnac_dnat_pria_pric_complex-causal
  - plaque-ng1996ii-pdf
  - plaque-pmid-8663104
- assessment_id: plaque-t6-structured-source-applicability
  area: evidence
  topic: structured source applicability
  outcome: supported
  summary: 'Positive named molecular components, loading/restart functions and gene
    examples trigger the broad structured-source policy. Current E. coli precise1k
    coverage and exact matched loci were inspected: five-strain context, 201 membership
    rows per locus, and priB module1/53-member context where applicable. These are
    expression context only; absence of an expression-module claim never established
    the original exclusion. No fresh adapter runner execution is claimed.'
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-review-skill
  - plaque-catalogue
  - plaque-ecoli-meta
  - plaque-ecoli-modules
  - plaque-adapter-b4362-gene
  - plaque-adapter-b4362-modules
  - plaque-adapter-b3935-gene
  - plaque-adapter-b3935-modules
  - plaque-adapter-b0467-gene
  - plaque-adapter-b0467-modules
- assessment_id: plaque-t6-history-and-original-verdict
  area: provenance
  topic: history and original verdict
  outcome: concern
  summary: Current record bytes match the original frozen target. Existing needs_curation
    verdict and exact inherited finding lineage are reconfirmed with fresh independent
    evidence. The unsupported formal check is a bundle assessment defect to correct
    additively. Dated rationale/history remain append-only; no record status promotion
    or terminal disposition is inferred.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-original-6-md
  - plaque-input-original-proof
  - plaque-curation
  - plaque-review-contract
- assessment_id: plaque-t6-schema-input-integrity
  area: schema
  topic: schema input integrity
  outcome: supported
  summary: The original native YAML validates and its renderer reproduces the committed
    Markdown exactly. All historical input occurrences and current frozen hashes were
    checked. These deterministic results do not certify scientific claims, future
    CI, or merge readiness.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-input-original-proof
  - plaque-review-schema
  - plaque-native-dnab_dnac_dnat_pria_pric_complex-verify
  - plaque-native-dnab_dnac_dnat_pria_pric_complex-causal
- assessment_id: plaque-t6-coverage-and-verdict
  area: completeness
  topic: coverage and verdict
  outcome: concern
  summary: Whole record and all original findings/actions were reviewed. Needs_curation
    is retained for the material source-stage/cohort conflict and bounded exact-family
    grounding gap. No optional protein inventory, unresolved PAS-DNA class, unread
    figure or unmeasured universal necessity was manufactured as an additional finding.
  target_ids:
  - GO:1990159
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-rubric
  - plaque-curation
  - plaque-input-original-proof
- assessment_id: septin-dnab_dnac_rep_pric_complex-identity
  area: identity
  topic: Exact structural identity and boundary
  outcome: supported
  summary: Exact DnaB-DnaC-Rep-PriC/PAS-DNA pre-primosome ontology identity is coherent;
    canonical active-fork experiment is a different measured stage.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
- assessment_id: septin-dnab_dnac_rep_pric_complex-hierarchy
  area: identity
  topic: Typed parents, parthood and aliases
  outcome: supported
  summary: Current GO confirms stated class relations. Primase-free pre-primosome
    parent and related PhiX174 synonym do not collapse PriA/PriB/PriC/DnaT alternatives
    or add DnaG.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
- assessment_id: septin-dnab_dnac_rep_pric_complex-grounding
  area: grounding
  topic: Full-family mappings versus domain and example
  outcome: concern
  summary: Exact full-protein family authority mappings and native example memberships
    reconfirm the inherited localized grounding finding. Existing label-only notes
    defer curation rather than identify a scope mismatch. PAS-DNA remains unresolved
    and is not automatically oriC.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-curation-policy
  - septin-ipr-IPR005752
  - septin-ipr-IPR010890
  - septin-up-P09980
  - septin-up-P23862
- assessment_id: septin-dnab_dnac_rep_pric_complex-protein-identity
  area: grounding
  topic: Native accession, gene and taxon
  outcome: supported
  summary: 2 reviewed examples and 2 COVERED nodes retain correct current identities.
    Primary Rep P09980 differs from plasmid RepE P03856 carrying synonym rep; current
    alias-inclusive query does not negate correct primary-name selection or dated
    provenance.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-up-P09980
  - septin-up-P23862
  - septin-query-rep-83333
  - septin-query-priC-83333
  - septin-native-dnab_dnac_rep_pric_complex-verify
  - septin-native-dnab_dnac_rep_pric_complex-causal
  - septin-up-P03856
  - septin-protein-policy
- assessment_id: septin-dnab_dnac_rep_pric_complex-canonical-source
  area: evidence
  topic: Measured experimental assembly and source scope
  outcome: concern
  summary: Guy tests accessory action on active oriC-initiated forks without PriC
    and places Rep-DnaB binding after loading; Ng retained a different PriA/PriB/PriC/DnaT/DnaB
    assembly. Neither directly establishes the maintained quartet canonical example;
    native restart identity is not denied.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
- assessment_id: septin-dnab_dnac_rep_pric_complex-authors
  area: provenance
  topic: Citation identity and authors
  outcome: supported
  summary: Inspected publication identities,author lists,year and DOI match the cited
    sources; source-stage concerns are separate.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
- assessment_id: septin-dnab_dnac_rep_pric_complex-stoichiometry
  area: grounding
  topic: Measured quantities and conditional scope
  outcome: not_applicable
  summary: No invariant quartet stoichiometry is asserted; individual protein associations
    do not establish a whole-quartet count.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-schema-policy
- assessment_id: septin-dnab_dnac_rep_pric_complex-formation
  area: grounding
  topic: Formation necessity versus function
  outcome: unknown
  summary: UNKNOWN formation essentiality is not contradicted by catalytic output
    or activity measurements. PriA/PriC omission results in Ng concern a different
    cohort; no universal Rep/PriC-quartet necessity follows.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-schema-policy
- assessment_id: septin-dnab_dnac_rep_pric_complex-graph
  area: graph
  topic: Whole nonmechanistic graph and stage limits
  outcome: supported
  summary: Graph remains explicitly NONMECHANISTIC/FUNCTION at GO-level loading/restart
    and PAS scaffold, not a claimed kinetic reconstruction of Guy active-fork experiments.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-graph-policy
- assessment_id: septin-dnab_dnac_rep_pric_complex-taxa
  area: scope
  topic: Biological source and experimental host
  outcome: supported
  summary: Species562 and K12 reference83333 are correct; COMMON is qualitative, not
    a measured prevalence census. Guy uvrD-cloning MG1655 and unread supplementary
    strains are not equated with every assay.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-tax-562
  - septin-tax-83333
  - septin-up-P09980
  - septin-up-P23862
- assessment_id: septin-dnab_dnac_rep_pric_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive molecular/pathway assertions require coverage evaluation; original
    formal no-expression exclusion is unsupported. Fresh E.coli precise1k exact loci
    have no thresholded memberships across201 modules, which is not absence of expression
    or structural participation.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
  - septin-modulemembers-rep
  - septin-modulemembers-priC
  - septin-modulemembers-dnaB
  - septin-modulemembers-dnaC
  - septin-modulegene-rep
  - septin-modulegene-priC
  - septin-modulegene-dnaB
  - septin-modulegene-dnaC
- assessment_id: septin-dnab_dnac_rep_pric_complex-schema
  area: schema
  topic: Native originals and historical/current hashes
  outcome: supported
  summary: All three original pairs validate/render0 with exact Markdown and all39
    historical input occurrences verified. Current targets remain byte-identical to
    frozen originals. Native protein checks0 at current source; historical corpus
    checks are not current CI.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-original-native-checks
  - septin-native-dnab_dnac_rep_pric_complex-verify
  - septin-native-dnab_dnac_rep_pric_complex-causal
- assessment_id: septin-dnab_dnac_rep_pric_complex-history
  area: provenance
  topic: Historical rationale and future corrective scope
  outcome: supported
  summary: Historical discussions/actions remain unchanged. Future record curation
    may update current notes/status or append dated clarification, without rewriting
    original rationale or promoting review status automatically.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-curation-policy
- assessment_id: septin-dnab_dnac_rep_pric_complex-coverage
  area: completeness
  topic: Complete record and access limits
  outcome: supported
  summary: Every current definition,alias,parent,component/example,taxon,function,evidence,graph
    edge,discussion and history assessed. No maintained images; no figure pixels,raw-data
    reanalysis,unread supplements or full Bailey/Mitkova body certified. Optional
    fields do not automatically require additions.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-literature-policy
- assessment_id: septin-dnab_dnac_rep_pric_complex-verdict
  area: consistency
  topic: Current independent disposition
  outcome: concern
  summary: Needs curation for inherited canonical-stage major and exact-family minor;
    original Rep query F3 is rejected, not a record-curation requirement.
  target_ids:
  - GO:1990160
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-go
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-ipr-IPR005752
  - septin-ipr-IPR010890
  - septin-curation-policy
- assessment_id: septin-dnab_dnag_complex-identity
  area: identity
  topic: Exact structural identity and boundary
  outcome: supported
  summary: Exact DnaB-DnaG helicase-primase complex, distinct from DNA-containing
    whole core primosome.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
- assessment_id: septin-dnab_dnag_complex-hierarchy
  area: identity
  topic: Typed parents, parthood and aliases
  outcome: supported
  summary: Current GO confirms stated class relations. DnaB-DnaG part_of core primosome
    is explicit; is_a helicase-complex relation remains distinct.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
- assessment_id: septin-dnab_dnag_complex-grounding
  area: grounding
  topic: Full-family mappings versus domain and example
  outcome: concern
  summary: Exact full-protein family authority mappings and native example memberships
    reconfirm the inherited localized grounding finding. Existing label-only notes
    defer curation rather than identify a scope mismatch. Domain-only or unchecked
    broader generated descriptions are not substitutes.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-original-dnab_dnag_complex
  - septin-curation-policy
  - septin-ipr-IPR007692
  - septin-ipr-IPR030846
  - septin-retry-IPR006295
  - septin-retry-IPR050219
  - septin-up-P0ACB0
  - septin-up-P0ABS5
- assessment_id: septin-dnab_dnag_complex-protein-identity
  area: grounding
  topic: Native accession, gene and taxon
  outcome: supported
  summary: 2 reviewed examples and 2 COVERED nodes retain correct current identities.
    Reference accessions do not silently identify every experimental reagent or strain.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-query-dnaB-83333
  - septin-query-dnaG-83333
  - septin-native-dnab_dnag_complex-verify
  - septin-native-dnab_dnag_complex-causal
- assessment_id: septin-dnab_dnag_complex-canonical-source
  area: evidence
  topic: Measured experimental assembly and source scope
  outcome: supported
  summary: Primary Mitkova abstract directly supports isolated stabilized E.coli DnaB-DnaG
    binding/stoichiometry; no unseen full-body or supplement claims.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
- assessment_id: septin-dnab_dnag_complex-authors
  area: provenance
  topic: Citation identity and authors
  outcome: concern
  summary: PMID14557266/DOI10.1074/jbc.M308956200 identify Mitkova,Khopde,Biswas2003;
    repeated current Tougu/Marians attribution is incorrect. Supported measurements
    and exact DOI/PMID remain valid.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
- assessment_id: septin-dnab_dnag_complex-stoichiometry
  area: grounding
  topic: Measured quantities and conditional scope
  outcome: supported
  summary: Six DnaB and three DnaG are explicitly scoped to stabilized E.coli complex;
    no universal in-vivo ratio inferred.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-schema-policy
- assessment_id: septin-dnab_dnag_complex-formation
  area: grounding
  topic: Formation necessity versus function
  outcome: unknown
  summary: UNKNOWN formation essentiality is not contradicted by catalytic output
    or activity measurements. Primase ssDNA binding for primer synthesis does not
    itself prove universal complex-formation necessity.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-schema-policy
- assessment_id: septin-dnab_dnag_complex-graph
  area: graph
  topic: Whole nonmechanistic graph and stage limits
  outcome: supported
  summary: Coarse nonmechanistic primer-output graph is supported; chemical crosslinks
    do not create a detailed loading/release model.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-graph-policy
- assessment_id: septin-dnab_dnag_complex-taxa
  area: scope
  topic: Biological source and experimental host
  outcome: supported
  summary: E.coli/K12 annotation and stabilized experimental species are correct;
    exact expression strain is not established by the abstract.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-tax-562
  - septin-tax-83333
- assessment_id: septin-dnab_dnag_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive molecular/pathway assertions require coverage evaluation; original
    formal no-expression exclusion is unsupported. Fresh E.coli precise1k dnaG is
    in Nucleotide Stress10; dnaB has no thresholded hit. Expression membership is
    not binding/formation evidence.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-original-dnab_dnag_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
  - septin-modulemembers-dnaB
  - septin-modulemembers-dnaG
  - septin-modulegene-dnaB
  - septin-modulegene-dnaG
  - septin-module-10
  - septin-module-10-genes
- assessment_id: septin-dnab_dnag_complex-schema
  area: schema
  topic: Native originals and historical/current hashes
  outcome: supported
  summary: All three original pairs validate/render0 with exact Markdown and all39
    historical input occurrences verified. Current targets remain byte-identical to
    frozen originals. Native protein checks0 at current source; historical corpus
    checks are not current CI.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-original-dnab_dnag_complex
  - septin-original-native-checks
  - septin-native-dnab_dnag_complex-verify
  - septin-native-dnab_dnag_complex-causal
- assessment_id: septin-dnab_dnag_complex-history
  area: provenance
  topic: Historical rationale and future corrective scope
  outcome: supported
  summary: Historical discussions/actions remain unchanged. Future record curation
    may update current notes/status or append dated clarification, without rewriting
    original rationale or promoting review status automatically.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-original-dnab_dnag_complex
  - septin-curation-policy
- assessment_id: septin-dnab_dnag_complex-coverage
  area: completeness
  topic: Complete record and access limits
  outcome: supported
  summary: Every current definition,alias,parent,component/example,taxon,function,evidence,graph
    edge,discussion and history assessed. No maintained images; no figure pixels,raw-data
    reanalysis,unread supplements or full Bailey/Mitkova body certified. Optional
    fields do not automatically require additions.
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-literature-policy
- assessment_id: septin-dnab_dnag_complex-verdict
  area: consistency
  topic: Current independent disposition
  outcome: concern
  summary: 'Needs curation for two inherited minor findings: exact families and repeated
    author attribution.'
  target_ids:
  - GO:1990156
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-go
  - septin-pmid-14557266
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  - septin-ipr-IPR007692
  - septin-ipr-IPR030846
  - septin-retry-IPR006295
  - septin-retry-IPR050219
  - septin-curation-policy
- assessment_id: septin-dnab_helicase_complex-identity
  area: identity
  topic: Exact structural identity and boundary
  outcome: supported
  summary: Exact DnaB homohexamer, distinct from DnaB-DnaG or loading complexes.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
- assessment_id: septin-dnab_helicase_complex-hierarchy
  area: identity
  topic: Typed parents, parthood and aliases
  outcome: supported
  summary: Current GO confirms stated class relations. The generic DNA-helicase parent
    does not add loading or primase subunits to this homohexamer.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
- assessment_id: septin-dnab_helicase_complex-grounding
  area: grounding
  topic: Full-family mappings versus domain and example
  outcome: concern
  summary: Exact full-protein family authority mappings and native example memberships
    reconfirm the inherited localized grounding finding. Existing label-only notes
    defer curation rather than identify a scope mismatch. Domain-only or unchecked
    broader generated descriptions are not substitutes.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-original-dnab_helicase_complex
  - septin-curation-policy
  - septin-ipr-IPR007692
  - septin-up-Q9X4C9
- assessment_id: septin-dnab_helicase_complex-protein-identity
  area: grounding
  topic: Native accession, gene and taxon
  outcome: supported
  summary: 1 reviewed examples and 1 COVERED nodes retain correct current identities.
    Reference accessions do not silently identify every experimental reagent or strain.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-up-Q9X4C9
  - septin-query-dnaB-1422
  - septin-native-dnab_helicase_complex-verify
  - septin-native-dnab_helicase_complex-causal
- assessment_id: septin-dnab_helicase_complex-canonical-source
  area: evidence
  topic: Measured experimental assembly and source scope
  outcome: supported
  summary: Bailey primary abstract plus exact2R6D entry/entity/assembly metadata support
    DnaB-alone six-subunit form; DnaG-domain structures are separately described.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
- assessment_id: septin-dnab_helicase_complex-authors
  area: provenance
  topic: Citation identity and authors
  outcome: supported
  summary: Inspected publication identities,author lists,year and DOI match the cited
    sources; source-stage concerns are separate.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
- assessment_id: septin-dnab_helicase_complex-stoichiometry
  area: grounding
  topic: Measured quantities and conditional scope
  outcome: supported
  summary: Six identical DnaB subunits are directly represented by exact2R6D assembly1;
    no DnaG is present in that deposited form.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-schema-policy
- assessment_id: septin-dnab_helicase_complex-formation
  area: grounding
  topic: Formation necessity versus function
  outcome: unknown
  summary: UNKNOWN formation essentiality is not contradicted by catalytic output
    or activity measurements. Observed homohexamer and helicase activity do not by
    themselves establish a component-removal phenotype for all conditions.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-schema-policy
- assessment_id: septin-dnab_helicase_complex-graph
  area: graph
  topic: Whole nonmechanistic graph and stage limits
  outcome: supported
  summary: Coarse ATP-dependent DNA-unwinding graph is supported at native/abstract
    tier; no newly inferred conformational sequence.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-graph-policy
- assessment_id: septin-dnab_helicase_complex-taxa
  area: scope
  topic: Biological source and experimental host
  outcome: supported
  summary: Biological Geobacillus1422/Bacillus old synonym is correct; E.coli BL21(DE3)
    is the expression host, not the maintained biological taxon. COMMON is not a population
    prevalence estimate.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-tax-1422
  - septin-up-Q9X4C9
- assessment_id: septin-dnab_helicase_complex-adapter
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Positive molecular/pathway assertions require coverage evaluation; original
    formal no-expression exclusion is unsupported. Fresh complete catalogue has no
    Geobacillus stearothermophilus dataset; unrelated Bacillus subtilis or E.coli
    expression-host data are not substituted. Coverage nonmatch does not mean biology
    absent.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-original-dnab_helicase_complex
  - septin-review-policy
  - septin-catalogue
  - septin-ecoli-meta
  - septin-ecoli-modules
  - septin-adapter-runner-historical
- assessment_id: septin-dnab_helicase_complex-schema
  area: schema
  topic: Native originals and historical/current hashes
  outcome: supported
  summary: All three original pairs validate/render0 with exact Markdown and all39
    historical input occurrences verified. Current targets remain byte-identical to
    frozen originals. Native protein checks0 at current source; historical corpus
    checks are not current CI.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-original-dnab_helicase_complex
  - septin-original-native-checks
  - septin-native-dnab_helicase_complex-verify
  - septin-native-dnab_helicase_complex-causal
- assessment_id: septin-dnab_helicase_complex-history
  area: provenance
  topic: Historical rationale and future corrective scope
  outcome: supported
  summary: Historical discussions/actions remain unchanged. Future record curation
    may update current notes/status or append dated clarification, without rewriting
    original rationale or promoting review status automatically.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-original-dnab_helicase_complex
  - septin-curation-policy
- assessment_id: septin-dnab_helicase_complex-coverage
  area: completeness
  topic: Complete record and access limits
  outcome: supported
  summary: Every current definition,alias,parent,component/example,taxon,function,evidence,graph
    edge,discussion and history assessed. No maintained images; no figure pixels,raw-data
    reanalysis,unread supplements or full Bailey/Mitkova body certified. Optional
    fields do not automatically require additions.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-literature-policy
- assessment_id: septin-dnab_helicase_complex-verdict
  area: consistency
  topic: Current independent disposition
  outcome: concern
  summary: Needs curation for inherited minor exact-family mapping, preserving correct
    homohexamer identity and protein source.
  target_ids:
  - GO:1990161
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-go
  - septin-pmid-17947583
  - septin-pdb-entry
  - septin-pdb-assembly
  - septin-pdb-entity
  - septin-ipr-IPR007692
  - septin-curation-policy
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 0 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:1990083
  - GO:1990103
  - GO:1990082
  - GO:1990101
  - GO:1990100
  - GO:1990158
  - GO:1990159
  - GO:1990160
  - GO:1990156
  - GO:1990161
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
  issue_key: dnaa-hda-definition-phosphorylation-versus-hydrolysis
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the inherited RIDA chemistry
  description: The definition says Hda inactivates DnaA by inhibiting phosphorylation
    of DnaA-ADP to DnaA-ATP. This matches current GO1990083 but conflicts with the
    cited Keyamura/Katayama2011 staged hydrolysis assay and the target’s own ATP-hydrolysis
    canonical/graph text. RIDA promotes hydrolysis of bound ATP; reactivation by DARS
    uses nucleotide exchange.
  target_ids:
  - GO:1990083
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - micro-record-0
  - micro-go-1990083
  - micro-keyamura2011-pmc
  - micro-pmid-21708944
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-scoped scientific assertions
  native_severity: major
  normalization_reason: The defining chemistry contradicts the cited primary experiment
    and the record’s own hydrolysis description; this is a substantive mechanism error
    while complex identity remains correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060738Z-dnaa-hda-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2939
- finding_id: micro-F2
  issue_key: dnaa-hda-exact-component-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the exact DnaA and Hda families
  description: DnaA IPR001957 and Hda IPR017788 are available exact whole-protein
    families and are independently present in the verified examples. The current REVIEWED_LABEL_ONLY
    rows and open TODO can therefore be resolved; narrower Hda IPR022864 is not the
    generic class.
  target_ids:
  - GO:1990083
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR001957
  - micro-ipr-IPR017788
  - micro-ipr-IPR022864
  - micro-protein-P03004
  - micro-protein-P69931
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-scoped scientific assertions
  native_severity: minor
  normalization_reason: Correct complex identity and supported membership remain intact;
    this is a bounded actionable class-grounding gap, not a requirement to fill optional
    examples.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060738Z-dnaa-hda-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2940
- finding_id: micro-F3
  issue_key: dnaa-hu-dnaa-oric-exact-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve DnaA and oriC class mappings
  description: The DnaA constituent has exact whole-protein family IPR001957 and the
    origin-DNA scaffold has exact SO0000953. Both remain REVIEWED_LABEL_ONLY with
    an open mapping task. The HU dimer boundary is a separate unresolved complex class,
    not a reason to defer these two exact matches.
  target_ids:
  - GO:1990103
  field_paths:
  - components[0].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-schema
  - micro-ipr-IPR001957
  - micro-so-0000953
  - micro-protein-P03004
  - micro-pmid-18179598
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hu_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-scoped scientific assertions
  native_severity: minor
  normalization_reason: Correct complex identity and supported membership remain intact;
    this is a bounded actionable class-grounding gap, not a requirement to fill optional
    examples.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060739Z-dnaa-hu-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2941
- finding_id: micro-F4
  issue_key: dnaa-l2-exact-component-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the DnaA and50S-L2 family mappings
  description: The two named classes have exact whole-protein families DnaA IPR001957
    and bacterial/organellar uL2 IPR005880, independently corroborated by current
    examples. The universal IPR002171 parent is broader than the declared50S-L2 class;
    current label-only states and mapping task can be narrowed.
  target_ids:
  - GO:1990082
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR001957
  - micro-ipr-IPR005880
  - micro-ipr-IPR002171-retry
  - micro-protein-P03004
  - micro-protein-P60422
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_l2_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and source-scoped scientific assertions
  native_severity: minor
  normalization_reason: Correct complex identity and supported membership remain intact;
    this is a bounded actionable class-grounding gap, not a requirement to fill optional
    examples.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060740Z-dnaa-l2-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2942
- finding_id: micro-F5
  issue_key: dnaa-oric-complex-exact-component-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified existing component-class groundings
  description: DnaA exactly maps to InterProIPR001957 and oriC to SO0000953. Native
    family/ontology identities plus independently inspected protein cross-references
    establish the matches. The current reviewed-label-only/open-task representation
    leaves these actionable classes unresolved. Historical earlier-pass statements
    are not declared false merely because current verification is available.
  target_ids:
  - GO:1990101
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-schema
  - micro-ipr-IPR001957
  - micro-so-0000953
  - micro-protein-P03004
  - micro-miller2009-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_oric_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: minor
  normalization_reason: The correct named classes and example identities are retained.
    This is a bounded exact-grounding gap under the explicit local contract, not missing
    optional inventory.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060740Z-dnaa-oric-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2943
- finding_id: plaque-t4-F1
  issue_key: dnab-dnac-complex-exact-component-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified existing component-class groundings
  description: DnaB exactly maps to InterProIPR007692 and DnaC to the unintegrated
    but exact NCBIfamNF005931. Broad DnaC/IstBIPR028350 is not the proposed match.
    Native family/ontology identities plus independently inspected protein cross-references
    establish the matches. The current reviewed-label-only/open-task representation
    leaves these actionable classes unresolved. Historical earlier-pass statements
    are not declared false merely because current verification is available.
  target_ids:
  - GO:1990100
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - plaque-record-4
  - plaque-original-4-yaml
  - plaque-curation
  - plaque-ipr-IPR007692
  - plaque-ncbifam-NF005931
  - plaque-ipr-IPR028350
  - plaque-up-P0ACB0
  - plaque-up-P0AEF0
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: minor
  normalization_reason: The correct named classes and example identities are retained.
    This is a bounded exact-grounding gap under the explicit local contract, not missing
    optional inventory.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060741Z-dnab-dnac-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2944
- finding_id: plaque-t5-F1
  issue_key: dnab-dnac-dnat-pria-prib-source-stage-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate the loader-containing model from isolated preprimosome composition
  description: Current GO1990158 names a DnaB-DnaC-containing complex, and the record
    turns that model into an unqualified constituent/has_part and graph claim while
    treating Ng experiments as its canonical source. NgI explicitly reports final
    PriA/PriB/DnaT/DnaB without DnaC. NgII pp15653–54 likewise rejects stable DnaC
    membership and retains PriC on intact PhiX174 DNA, unlike the short PAS substrate.
    Input proteins, transient loading and stable isolated composition are therefore
    conflated. Native authority and experimental observation must both remain visible.
  target_ids:
  - GO:1990158
  field_paths:
  - definition
  - has_part
  - components[0]
  - canonical_examples[0]
  - causal_graphs[0].description
  - causal_graphs[0].edges[0]
  - discussions[1]
  evidence_ids:
  - plaque-record-5
  - plaque-original-5-yaml
  - plaque-curation
  - plaque-go
  - plaque-pmid-8663104
  - plaque-pmid-8663105
  - plaque-ng1996ii-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: major
  normalization_reason: This is a material composition/assembly-stage conflict in
    the cited experimental support, even though the current ontology text is copied
    accurately. It does not establish that transient DnaC-containing intermediates
    are impossible or authorize renaming the record.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2945
- finding_id: plaque-t5-F2
  issue_key: dnab-dnac-dnat-pria-prib-complex-exact-component-groundings
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve verified existing component-class groundings
  description: DnaT, PriA and PriB exactly map to InterProIPR020917, IPR005259 and
    IPR023646, respectively. DnaT natural proteobacterial scope is stated; the PriB/SSB
    parent and helicase domains are not substituted. Native family/ontology identities
    plus independently inspected protein cross-references establish the matches. The
    current reviewed-label-only/open-task representation leaves these actionable classes
    unresolved. Historical earlier-pass statements are not declared false merely because
    current verification is available.
  target_ids:
  - GO:1990158
  field_paths:
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - plaque-record-5
  - plaque-original-5-yaml
  - plaque-curation
  - plaque-ipr-IPR020917
  - plaque-ipr-IPR005259
  - plaque-ipr-IPR023646
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P07013
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  rule_id: Exact class grounding and claim-level primary-source scope
  native_severity: minor
  normalization_reason: The correct named classes and example identities are retained.
    This is a bounded exact-grounding gap under the explicit local contract, not missing
    optional inventory.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2946
- finding_id: plaque-t6-F1
  issue_key: pria-pric-source-cohort
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate the cited PhiX product from the maintained loading intermediate
  description: The record treats NgII as direct evidence for a PriB-excluded DnaB-DnaC-DnaT-PriA-PriC
    assembly, including its canonical example, constituent notes and replication-through-restart
    function. NgII pp15653–54 explicitly reports a stable PriA/PriB/PriC/DnaT/DnaB
    complex and rejects DnaC as a stable constituent; its repair/restart extension
    is proposed. The correct GO identifier does not make the experimentally different
    cohort equivalent.
  target_ids:
  - GO:1990159
  field_paths:
  - canonical_examples[0]
  - components#dnab_dnac_complex.evidence
  - functions#replication_fork_processing.evidence
  - causal_graphs#dnab_dnac_dnat_pria_pric_restart
  - discussions#exclude_prib_rep_and_dnag_from_pric_preprimosome
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-curation
  - plaque-go
  - plaque-pmid-8663104
  - plaque-pmid-8663105
  - plaque-ng1996ii-pdf
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: major
  normalization_reason: The cited experiment is used to substantiate the defining
    molecular cohort and canonical example, but its retained composition differs in
    two named proteins and its repair extension is hypothetical. This is material
    source-to-structure scope transfer, not a citation-format defect.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2947
- finding_id: plaque-t6-F2
  issue_key: pria-pric-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground DnaT, PriA and PriC with exact families
  description: The three REVIEWED_LABEL_ONLY protein rows defer mapping despite exact
    full-protein families IPR020917, IPR005259 and IPR010890 and independent membership
    of their correct K12 examples.
  target_ids:
  - GO:1990159
  field_paths:
  - components#dnat_restart_protein.grounding_status
  - components#pria_restart_protein.grounding_status
  - components#pric_restart_protein.grounding_status
  - discussions#resolve_pric_restart_component_groundings
  evidence_ids:
  - plaque-record-6
  - plaque-original-6-yaml
  - plaque-curation
  - plaque-ipr-IPR020917
  - plaque-ipr-IPR005259
  - plaque-ipr-IPR010890
  - plaque-up-P0A8J2
  - plaque-up-P17888
  - plaque-up-P23862
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2948
- finding_id: septin-dnab_dnac_rep_pric_complex-F1
  issue_key: rep-pric-canonical-stage
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Use an exact Rep-PriC loading example rather than the active-fork experiment
  description: 'Guy2009 is the canonical example for this four-protein preprimosome,
    but its main replication assay omits PriC and studies Rep-assisted movement of
    oriC-initiated forks. Its Results explicitly show DnaC inhibition of Rep-DnaB
    binding and place that interaction after loading. NgII also does not supply the
    missing quartet: its retained PhiX assembly contains PriA/PriB/PriC/DnaT/DnaB.
    Independently reconfirmed against the current unchanged record and exact scoped
    source evidence. Preserve historical rationale; update current notes/status or
    append a dated clarification only in separately authorized curation.'
  target_ids:
  - GO:1990160
  field_paths:
  - canonical_examples[0]
  - taxonomic_distribution[0].reference
  - evidence
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-guy2009-legacy
  - septin-ng1996ii-pdf
  - septin-pmid-19941825
  - septin-pmid-8663105
  - septin-go
  - septin-up-P09980
  - septin-up-P23862
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: major
  normalization_reason: A different experimental cohort and stage currently serves
    as the canonical exemplar of the entire structure. Correcting the citation alone
    is insufficient; the structure-to-experiment association must be reconciled.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060743Z-dnab-dnac-rep-pric-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2949
- finding_id: septin-dnab_dnac_rep_pric_complex-F2
  issue_key: rep-pric-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Rep and PriC with exact families
  description: Two reviewed-label-only rows defer exact mappings despite Rep IPR005752
    and PriC IPR010890, supported by exact family signatures and the separately verified
    examples. Independently reconfirmed against the current unchanged record and exact
    scoped source evidence. Preserve historical rationale; update current notes/status
    or append a dated clarification only in separately authorized curation.
  target_ids:
  - GO:1990160
  field_paths:
  - components#rep_helicase.grounding_status
  - components#pric_restart_protein.grounding_status
  - discussions#resolve_rep_pric_component_groundings
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR005752
  - septin-ipr-IPR010890
  - septin-up-P09980
  - septin-up-P23862
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060743Z-dnab-dnac-rep-pric-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2950
- finding_id: septin-dnab_dnac_rep_pric_complex-F3
  issue_key: rep-query-alias-uniqueness
  category: evidence
  severity: minor
  status: rejected
  certainty: confirmed
  title: Reject unsupported inference from the alias-inclusive Rep search
  description: Original F3 overstated that the current single-reviewed-Rep claim was
    false at a stated query scope. The record names correct Rep helicase P09980 and
    primary gene rep but does not specify an alias-inclusive endpoint. The fresh exact-gene
    query also returns primary repE/P03856 because rep is its synonym. That current
    ambiguity does not negate correct primary-name/protein-identity selection or reconstruct
    the dated query. Automatic ambiguous seeding should abstain, but manual disambiguation
    is valid. Optional alias clarification is not a demonstrated mandatory correction;
    preserve current accession and dated history.
  target_ids:
  - GO:1990160
  field_paths:
  - components#rep_helicase.protein_examples[0].evidence
  evidence_ids:
  - septin-record-dnab_dnac_rep_pric_complex
  - septin-original-dnab_dnac_rep_pric_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-up-P09980
  - septin-up-P03856
  - septin-query-rep-83333
  - septin-protein-policy
  - septin-review-schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: Original minor severity is retained solely for traceable rejected
    lineage; no current scientific record defect is established by this query evidence.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060743Z-dnab-dnac-rep-pric-complex-audit
    finding_id: F3
  disposition_reason: Current alias-inclusive search does not establish the record
    used that endpoint or invalidate the correctly identified primary Rep helicase;
    it cannot reconstruct a dated query. Mandatory record correction is unsupported.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2938
- finding_id: septin-dnab_dnag_complex-F1
  issue_key: dnab-dnag-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the DnaB and bacterial DnaG constituents
  description: IPR007692 and IPR030846 are exact full-protein families for the maintained
    helicase and bacterial primase, with independent native example membership. The
    label-only notes merely defer curation. Independently reconfirmed against the
    current unchanged record and exact scoped source evidence. Preserve historical
    rationale; update current notes/status or append a dated clarification only in
    separately authorized curation.
  target_ids:
  - GO:1990156
  field_paths:
  - components#dnab_helicase.grounding_status
  - components#dnag_primase.grounding_status
  - discussions#resolve_dnab_dnag_family_groundings
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-original-dnab_dnag_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR007692
  - septin-ipr-IPR030846
  - septin-retry-IPR006295
  - septin-retry-IPR050219
  - septin-up-P0ACB0
  - septin-up-P0ABS5
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnag_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060744Z-dnab-dnag-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2951
- finding_id: septin-dnab_dnag_complex-F2
  issue_key: dnab-dnag-citation-authors
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the repeated 2003 author attribution
  description: PMID14557266 and DOI10.1074/jbc.M308956200 identify Mitkova, Khopde
    and Biswas2003. The target repeatedly attributes this exact paper and its measurements
    to Tougu and Marians. Independently reconfirmed against the current unchanged
    record and exact scoped source evidence. Preserve historical rationale; update
    current notes/status or append a dated clarification only in separately authorized
    curation.
  target_ids:
  - GO:1990156
  field_paths:
  - components#dnab_helicase.evidence
  - components#dnag_primase.evidence
  - taxonomic_distribution[0].note
  - canonical_examples[0].note
  - functions#dna_replication_synthesis_of_primer.evidence
  - evidence
  - causal_graphs#dnab_dnag_primer_synthesis
  evidence_ids:
  - septin-record-dnab_dnag_complex
  - septin-original-dnab_dnag_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-pmid-14557266
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnag_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060744Z-dnab-dnag-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2952
- finding_id: septin-dnab_helicase_complex-F1
  issue_key: dnab-helicase-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the DnaB monomer with its exact family
  description: The monomeric DnaB component remains REVIEWED_LABEL_ONLY although IPR007692
    is the exact full DnaB-type helicase family and native Q9X4C9 independently carries
    this family. Independently reconfirmed against the current unchanged record and
    exact scoped source evidence. Preserve historical rationale; update current notes/status
    or append a dated clarification only in separately authorized curation.
  target_ids:
  - GO:1990161
  field_paths:
  - components#dnab_helicase.grounding_status
  - discussions#resolve_dnab_family_grounding
  evidence_ids:
  - septin-record-dnab_helicase_complex
  - septin-original-dnab_helicase_complex
  - septin-curation-policy
  - septin-schema-policy
  - septin-ipr-IPR007692
  - septin-up-Q9X4C9
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_helicase_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific scientific scope and exact component grounding
  native_severity: minor
  normalization_reason: The complex identity and correct protein identifiers remain
    intact; the issue is a bounded exact-family or evidence-attribution correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T060744Z-dnab-helicase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2953
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:1990083
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, replace the mechanism sentence
    with source-backed DnaA-bound ATP hydrolysis in its DNA-loaded-clamp/ADP-Hda context.
    Preserve exact GO identity and record the upstream definition conflict; do not
    silently describe a revised primary-source definition as a verbatim GO definition.
  acceptance_checks:
  - The corrected text distinguishes hydrolysis from nucleotide exchange and phosphorylation.
  - Retain the binary contact versus full active RIDA-system boundary.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep actual experimental/body/abstract/authority
    scopes and do not force universal formation necessity or optional examples.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:1990083
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hda_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground DnaA and Hda with
    the exact families and narrow/resolve the corresponding mapping task, retaining
    the taxon-paired examples.
  acceptance_checks:
  - Check native family types/signatures and separate example cross-references.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep actual experimental/body/abstract/authority
    scopes and do not force universal formation necessity or optional examples.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:1990103
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_hu_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground DnaA and oriC with
    their verified class identifiers and narrow the open task to any remaining HU-complex
    identity. Preserve the dimer and its context-dependent subunit alternatives.
  acceptance_checks:
  - Do not ground a whole HU dimer to an individual-protein family.
  - Do not substitute a single origin sequence accession for the oriC feature class.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep actual experimental/body/abstract/authority
    scopes and do not force universal formation necessity or optional examples.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:1990082
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_l2_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground the two protein classes
    with the verified exact families, retain correct examples, and resolve/narrow
    the mapping task without importing unrelated ribosomal mechanisms.
  acceptance_checks:
  - Verify class scope and integrated full-protein signatures.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep actual experimental/body/abstract/authority
    scopes and do not force universal formation necessity or optional examples.
- action_id: micro-A5
  finding_ids:
  - micro-F5
  target_ids:
  - GO:1990101
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnaa_oric_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add the verified exact class
    CURIEs with source-specific evidence, update the corresponding grounding states/open
    task, and preserve organism accessions as examples. Do not force a broader homolog/domain
    or unresolved PAS-DNA mapping.
  acceptance_checks:
  - Every added CURIE denotes the existing class at the stated scope, not an individual
    species protein.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated discussions.rationale, posed_date and curation history; append
    provenance and narrow current notes/prompt only as supported.
  - No record edits occur in this review PR. Keep actual experimental/body/abstract/authority
    scopes and do not force universal formation necessity or optional examples.
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:1990100
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_complex.yaml
    role: maintained scientific record
  description: Add the verified exact class CURIEs with source-specific evidence,
    update the corresponding grounding states/open task, and preserve organism accessions
    as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.
  acceptance_checks:
  - Every added CURIE denotes the existing class at the stated scope, not an individual
    species protein.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale and curation history; append source-specific current
    notes or reopen/qualify the active decision without rewriting historical provenance.
- action_id: plaque-t5-A1
  finding_ids:
  - plaque-t5-F1
  target_ids:
  - GO:1990158
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  description: Preserve GO1990158 and explicitly distinguish its loader-containing
    assembly model from the Ng isolated complexes. Qualify the stage/source of DnaC
    parthood and graph membership, identify which substrate/stage the canonical example
    demonstrates, and retain the PriC-dependent intact-DNA versus short-PAS distinction.
    Inspect an appropriate primary source before claiming direct observation of the
    exact DnaC-containing assembly.
  acceptance_checks:
  - Stable composition is not inferred from proteins supplied to the reaction.
  - The action preserves current identity and reports the authority/source conflict
    without silently replacing it.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale and curation history; append source-specific current
    notes or reopen/qualify the active decision without rewriting historical provenance.
- action_id: plaque-t5-A2
  finding_ids:
  - plaque-t5-F2
  target_ids:
  - GO:1990158
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml
    role: maintained scientific record
  description: Add the verified exact class CURIEs with source-specific evidence,
    update the corresponding grounding states/open task, and preserve organism accessions
    as examples. Do not force a broader homolog/domain or unresolved PAS-DNA mapping.
  acceptance_checks:
  - Every added CURIE denotes the existing class at the stated scope, not an individual
    species protein.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale and curation history; append source-specific current
    notes or reopen/qualify the active decision without rewriting historical provenance.
- action_id: plaque-t6-A1
  finding_ids:
  - plaque-t6-F1
  target_ids:
  - GO:1990159
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  description: Keep the intended GO1990159 identity, but separate GO-defined loading/restart
    scope from NgI/II experimental context. Replace or qualify the canonical example
    and affected source notes with evidence for the exact PriA/PriC intermediate;
    explicitly distinguish loading factors from isolated product composition.
  acceptance_checks:
  - Do not add PriB or remove DnaC solely to turn this record into a different assembly.
  - Do not present NgII as a directly measured repaired-fork restart experiment.
  - Retain correct protein identities and the genuinely supported PhiX study context.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Preserve dated rationale and curation history; append source-specific current
    notes or reopen/qualify the active decision without rewriting historical provenance.
- action_id: plaque-t6-A2
  finding_ids:
  - plaque-t6-F2
  target_ids:
  - GO:1990159
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_dnat_pria_pric_complex.yaml
    role: maintained scientific record
  description: Use the verified DnaT/PriA/PriC family mappings and align current grounding
    notes/TODO, retaining unresolved PAS-DNA grounding.
  acceptance_checks:
  - Do not substitute a generic helicase/ATPase or DnaT domain.
  - Do not convert PAS DNA to chromosomal oriC.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Preserve dated rationale and curation history; append source-specific current
    notes or reopen/qualify the active decision without rewriting historical provenance.
- action_id: septin-dnab_dnac_rep_pric_complex-A1
  finding_ids:
  - septin-dnab_dnac_rep_pric_complex-F1
  target_ids:
  - GO:1990160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  description: Replace or explicitly contextualize Guy2009 as accessory-fork evidence,
    and use an independently verified exact Rep/PriC loading/restart source for the
    canonical quartet. Preserve the ontology identity and distinguish sequential loading
    from the active-fork complex. Preserve dated rationale/history and source-specific
    limits; this review PR edits no scientific record.
  acceptance_checks:
  - Do not deny the native Rep/PriC restart pathway or infer that no such intermediate
    exists.
  - Do not claim Guy tested PriC or directly isolated the maintained quartet.
  - Keep the correct E.coli and reference-protein identifiers.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Keep exact original finding lineage; preserve dated rationale with any clarification
    appended rather than rewritten.
- action_id: septin-dnab_dnac_rep_pric_complex-A2
  finding_ids:
  - septin-dnab_dnac_rep_pric_complex-F2
  target_ids:
  - GO:1990160
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnac_rep_pric_complex.yaml
    role: maintained scientific record
  description: Apply the exact Rep/PriC protein-family identities and align current
    notes/TODO while retaining unresolved PAS DNA. Preserve dated rationale/history
    and source-specific limits; this review PR edits no scientific record.
  acceptance_checks:
  - Do not import the erroneous Rep hexamer prose or substitute the generic UvrD/helicase
    domain.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Keep exact original finding lineage; preserve dated rationale with any clarification
    appended rather than rewritten.
- action_id: septin-dnab_dnag_complex-A1
  finding_ids:
  - septin-dnab_dnag_complex-F1
  target_ids:
  - GO:1990156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnag_complex.yaml
    role: maintained scientific record
  description: Use the exact DnaB and bacterial DnaG family mappings and align grounding
    notes/TODO. Preserve dated rationale/history and source-specific limits; this
    review PR edits no scientific record.
  acceptance_checks:
  - Do not substitute domain IPR006295 or broaden to unchecked archaeal/exosome descriptions.
  - Retain qualified three-DnaG stabilized-complex stoichiometry.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Keep exact original finding lineage; preserve dated rationale with any clarification
    appended rather than rewritten.
- action_id: septin-dnab_dnag_complex-A2
  finding_ids:
  - septin-dnab_dnag_complex-F2
  target_ids:
  - GO:1990156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_dnag_complex.yaml
    role: maintained scientific record
  description: Replace the incorrect author names with Mitkova etal2003 in current
    scientific/evidence notes, preserving the correct PMID/DOI/title and supported
    measurements. Preserve dated rationale/history and source-specific limits; this
    review PR edits no scientific record.
  acceptance_checks:
  - Check every current author mention consistently.
  - Do not reinterpret the legitimate condition-scoped stoichiometry as erroneous.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Keep exact original finding lineage; preserve dated rationale with any clarification
    appended rather than rewritten.
- action_id: septin-dnab_helicase_complex-A1
  finding_ids:
  - septin-dnab_helicase_complex-F1
  target_ids:
  - GO:1990161
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dnab_helicase_complex.yaml
    role: maintained scientific record
  description: Ground the protein constituent with IPR007692 and align its current
    notes/TODO, retaining the homohexamer identity and six-copy stoichiometry. Preserve
    dated rationale/history and source-specific limits; this review PR edits no scientific
    record.
  acceptance_checks:
  - Keep Q9X4C9 and biological source1422, distinct from the expression host.
  - Do not substitute a DnaB domain or broad ATPase fold.
  - Preserve correct identifiers and source-supported biology; pass applicable native
    validation.
  - Keep exact original finding lineage; preserve dated rationale with any clarification
    appended rather than rewritten.
limitations:
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: This scientific slice
  covers only DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC. All four current hashes are
  unchanged from original frozen inputs. Auxiliary row7 Rep-query challenge is separately
  scoped and owned by the other reviewer; no outside-slice scientific disposition
  is added here. No repository/Git/GitHub mutation.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Keyamura2011 genuine
  primary main HTML, Methods/Results/Discussion and all text captions were read freshly;
  no figure pixels, supplement, sequence alignments or coordinates. DNA-loaded-clamp/ADP-Hda
  staged hydrolysis and contact assays differ from binary identity; proposed structural
  model is not a solved cocrystal. Kurz2004 remains complete primary-abstract tier.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Chodavarapu2008 HU
  work remains complete primary-abstract tier after fresh Wiley HTML/PDF403. Exact
  experimental strains/full methods/images and taxon-wide bacterial necessity are
  not certified or refuted. HUalpha and alphabeta alternatives are retained, not an
  invariant heterodimer.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Chodavarapu2011 L2
  genuine main JATS and captions were read freshly. In-vitro contacts/inhibition,
  DM700 tL2 preparation and tested negative in-vivo tL2 initiation result remain distinct;
  no general in-vivo checkpoint, fixed stoichiometry, solved interface or cleavage
  mechanism is asserted.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Miller2009 genuine
  main HTML including Introduction/Results/Discussion/Methods and captions was read
  freshly. No raw footprints/pixels were reanalyzed. Elevated-DnaA rescue of low-affinity
  filling limits universal absence interpretations; actual mutant/strain/purified-protein
  contexts remain explicit.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Three DnaA-localization
  papers and Hda-localization paper are complete primary-abstract/native-annotation
  tier only. Current native UniProt identities/xrefs and family metadata do not certify
  every linked experiment. Reference taxon83333, species562, BL21(DE3) localization
  context and specific experimental strains are not conflated.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: InterPro family versus
  domain/broader/taxon-limited alternatives are distinguished. HdaIPR022864 is narrower;
  uL2IPR002171 is broader. Exact oriC SO class is not one strain sequence; HU whole-dimer
  identity is not a single protein family. Five inherited findings remain1major4minor
  with exact lineage; historical rationale is append-only.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Official precise1k
  contains five K12-related strains, not every primary mutant/preparation. Five exact
  loci each have201 inspected membership rows; only rplB crosses Translation module1
  threshold, corroborated in all53 member IDs/weights/identity columns. Negative rows
  are not gene absence; positive expression context is not physical assembly/direct
  regulation/necessity. Generated AI summaries and activity contrasts are not used.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Historical adapter
  runner is the actual2026-11-03T00:49Z unavailable invocation, not new execution.
  Four retained old failed-access observations preserve their originalOct22time/hash/classification
  correction; they are not claimed as new raw-response fetches. Present blocked routes
  and separate successful bodies are distinguished.'
- 'DnaA-Hda, DnaA-HU, DnaA-L2 and DnaA-oriC independent review: Eight actual source-head
  native protein commands pass with6reviewed examples and6COVERED typed protein nodes;
  HU STRUCTURE and oriC feature nodes are outside that inventory and assessed separately.
  Original8native validate/render commands and56historical hashes pass. Root owns
  globalQC and future successor/postsave/CI/queue gates; none is newly certified by
  this source report.'
- 'DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: NgI is assessed
  at its complete native primary abstract/metadata tier only; its full body and indexed
  erratum contents were not inspected. NgII main PDF text, Methods, Table I and captions
  were read, without pixels, Western reanalysis or uninspected cited studies.'
- 'DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: Makowska-Grzyska/Kaguni
  selected main Results/Discussion/Methods and figure captions were read; supplementary
  strain Table S1 and raw data were not inspected. No exact experimental K-12 derivative
  is inferred from reference accessions.'
- 'DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: The fresh public
  iModulonDB source fallback is not an invocation of the structured runner. The separate
  retained 2026-11-03 00:49Z unavailable-runner receipt remains historical; no fresh
  runner success or failure is asserted here. Five-strain precise1k context and above-threshold
  flags do not establish localization, physical membership, necessity or absence.
  Generated module summaries were excluded.'
- 'DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: No exact source-neutral
  PAS-DNA mapping was established; this uncertainty is retained without an optional-field
  finding. No universal copy-number or formation requirement is inferred from viability,
  membership annotations or another experimental assembly.'
- 'DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: The current
  GO labels/definitions are copied accurately; the two source-scope findings distinguish
  experimental stage and retained composition rather than declaring transient loading
  intermediates impossible or replacing the maintained identities.'
- 'DnaB-DnaC and PriA/PriB/PriC restart complexes independent review: Native local
  gate receipts are scoped to their actual commands. This independent slice does not
  certify corpus gates, GitHub CI, queue admission, merge or branch cleanup.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Three unchanged targets;
  five inherited open scientific findings (one major,four minor) and one exact-lineage
  rejected minor Rep-query finding. All three records still need localized curation;
  no new scientific finding. Three original formal applicability exclusions and one
  unsupported original finding need successor correction.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Guy2009 fresh genuine
  body inspected only at stated sections/captions; no full reading of Results2.2–2.5,supplementary
  TableS1 or figure pixels. Ng1996II genuine primary PDF scientific body pp15649–15654
  read with captions/TableI,not independent raw-data or pixel analysis. Its PhiX/PriA
  cohort is not the Rep/PriC quartet. No claim of exhaustive literature absence.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Mitkova2003 and Bailey2007
  access is full native abstract/metadata plus native UniProt/PDB authority scope,not
  full article bodies. Actual publisher403 responses remain validation context. Mitkova
  stabilized E.coli3:6 ratio is conditional; Bailey2R6D exact assembly has six Q9X4C9
  chains and no DnaG domain. Biological1422 differs from BL21(DE3) expression host.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: InterPro IPR005752 erroneous
  Rep-hexamer prose and IPR050219 unchecked LLM-generated description are excluded
  from biology; verified family/type/signature metadata remains usable. IPR006295
  is a domain,not a full DnaG class. PAS-DNA remains unresolved rather than silently
  oriC.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Current Rep gene_exact
  query returns primary rep/P09980 plus primary repE/P03856 with rep alias. This does
  not establish the exact past query or negate correct maintained Rep-helicase identity.
  Native ambiguous automatic seeding is distinct from manual identity disambiguation;
  optional alias explanation is not a mandatory record correction.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Fresh official catalogue
  has20organism rows; E.coli precise1k supports bounded reference context,five advertised
  strains and201modules. Five exact loci checked; only dnaG has thresholded Nucleotide
  Stress10 membership,confirmed in fifteen-member endpoint. Other false flags are
  not biological absence; no activity-vector interpretation or generated module prose
  used. No Geobacillus dataset; Bacillus subtilis/E.coli expression host is not a
  proxy.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Historical runner failed
  Nov3 00:49Z with PermissionError; no fresh runner invocation. Shared current catalogue/metadata
  packet uses its actual Nov4 retrieval dates and independently inspected scope. Authority
  retries after429 are distinct from initial failed responses.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Actual own native inventory
  has five reviewed examples and five COVERED protein nodes; six commands exit0 at
  current source. This verifies native identity/coverage,not experimental membership
  or necessity. Original three pairs validate/render exactly with39 historical input
  occurrences verified. Root global gates,successor/final-head validation,CI,queue
  and merge are separate attestations.'
- 'Rep/PriC, DnaB-DnaG and DnaB helicase independent review: Only26 listed frozen
  maintained inputs used; no extra neighbor or prior-review bundle used as biological
  authority. Original historical source receipts are inspected as original provenance,not
  falsely claimed fresh body access. No source-kind defect is established in these
  three originals: their Mitkova/Bailey access limitations do not constitute misclassified
  failed-response evidence rows.'
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
- The original ten target hashes all match current main; no stale record required
  refresh. The successor still provides current independent scientific reassessment
  and preserves all20 original artifacts.
- 'Bundle issues #2936 and #2937 cover seven formal and three prose applicability
  exclusions and four historical access-only evidence-kind corrections. Issue #2938
  rejects the original Rep query-uniqueness finding with exact lineage, preserving
  the correct P09980 identity and dated record history without requiring record curation.'
- Current native commands verify19 protein example occurrences and19 typed GENE_OR_PROTEIN
  nodes, all COVERED. Complex-level constituents remain separately scoped; optional
  protein inventories and universally essential formation labels are not compelled.
- 'Fifteen inherited open scientific findings (four major, eleven minor) retain exact
  predecessor lineage and bounded curation actions. The sixteenth inherited finding,
  Rep query F3, is explicitly rejected and linked to bundle issue #2938, with no corresponding
  record-curation action. Current primary-gene selection, search-alias behavior and
  historical query provenance remain distinct. All ten targets retain needs_curation
  for their remaining findings.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060738Z-dnaa-hda-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060739Z-dnaa-hu-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060740Z-dnaa-l2-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060740Z-dnaa-oric-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060741Z-dnab-dnac-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060742Z-dnab-dnac-dnat-pria-prib-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060742Z-dnab-dnac-dnat-pria-pric-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060743Z-dnab-dnac-rep-pric-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060744Z-dnab-dnag-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T060744Z-dnab-helicase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2389
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2936
- https://github.com/CultureBotAI/CellStructureMech/issues/2937
- https://github.com/CultureBotAI/CellStructureMech/issues/2938
- https://github.com/CultureBotAI/CellStructureMech/issues/2939
- https://github.com/CultureBotAI/CellStructureMech/issues/2940
- https://github.com/CultureBotAI/CellStructureMech/issues/2941
- https://github.com/CultureBotAI/CellStructureMech/issues/2942
- https://github.com/CultureBotAI/CellStructureMech/issues/2943
- https://github.com/CultureBotAI/CellStructureMech/issues/2944
- https://github.com/CultureBotAI/CellStructureMech/issues/2945
- https://github.com/CultureBotAI/CellStructureMech/issues/2946
- https://github.com/CultureBotAI/CellStructureMech/issues/2947
- https://github.com/CultureBotAI/CellStructureMech/issues/2948
- https://github.com/CultureBotAI/CellStructureMech/issues/2949
- https://github.com/CultureBotAI/CellStructureMech/issues/2950
- https://github.com/CultureBotAI/CellStructureMech/issues/2951
- https://github.com/CultureBotAI/CellStructureMech/issues/2952
- https://github.com/CultureBotAI/CellStructureMech/issues/2953
```
