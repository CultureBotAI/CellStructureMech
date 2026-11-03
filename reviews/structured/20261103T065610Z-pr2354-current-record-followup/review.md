# PR 2354: current-input review of ten records and adversarial follow-up

- Review: 20261103T065610Z-pr2354-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T06:45:01.061703Z
- Finished UTC: 2026-11-03T06:56:10Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten energy-complex and envelope records in PR2354. The stale photosystem review is substantively refreshed against changed reaction-center component types and current primary/authority sources. Its single-target historical component-type finding is resolved with exact lineage; the independent review also identifies a current canonical-example taxon/source conflict. Seven targets retain scientific curation findings; cellular bud membrane, coccolith and coccosphere retain qualified passes. Eight original bundles require structured-source applicability correction. Scientific records are unchanged.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 56380c619e8356208b1b27c13edc4c6206b92443. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head e8bccd7c6a67ad41f4e044efbab4099dc09e2872.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base d7ee610a5d142b5961a6057e22437aabb68f191f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009326 | data/structures/energy_complex/formate_dehydrogenase_complex.yaml | maintained | formate dehydrogenase complex |
| GO:0009325 | data/structures/energy_complex/nitrate_reductase_complex.yaml | maintained | nitrate reductase complex |
| GO:0009521 | data/structures/energy_complex/photosystem.yaml | maintained | photosystem |
| GO:0033176 | data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml | maintained | proton-transporting V-type ATPase complex |
| GO:0033179 | data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml | maintained | proton-transporting V-type ATPase, V0 domain |
| GO:0033180 | data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml | maintained | proton-transporting V-type ATPase, V1 domain |
| GO:0030428 | data/structures/envelope/cell_septum.yaml | maintained | cell septum |
| GO:0033101 | data/structures/envelope/cellular_bud_membrane.yaml | maintained | cellular bud membrane |
| cellstructuremech:coccolith | data/structures/envelope/coccolith.yaml | maintained | coccolith |
| cellstructuremech:coccosphere | data/structures/envelope/coccosphere.yaml | maintained | coccosphere |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0009326 | passed | True | GO:0009326 | Documented focused command passed. |
| validate-strict GO:0009326 | passed | True | GO:0009326 | Documented focused command passed. |
| validate GO:0009325 | passed | True | GO:0009325 | Documented focused command passed. |
| validate-strict GO:0009325 | passed | True | GO:0009325 | Documented focused command passed. |
| validate GO:0009521 | passed | True | GO:0009521 | Documented focused command passed. |
| validate-strict GO:0009521 | passed | True | GO:0009521 | Documented focused command passed. |
| validate GO:0033176 | passed | True | GO:0033176 | Documented focused command passed. |
| validate-strict GO:0033176 | passed | True | GO:0033176 | Documented focused command passed. |
| validate GO:0033179 | passed | True | GO:0033179 | Documented focused command passed. |
| validate-strict GO:0033179 | passed | True | GO:0033179 | Documented focused command passed. |
| validate GO:0033180 | passed | True | GO:0033180 | Documented focused command passed. |
| validate-strict GO:0033180 | passed | True | GO:0033180 | Documented focused command passed. |
| validate GO:0030428 | passed | True | GO:0030428 | Documented focused command passed. |
| validate-strict GO:0030428 | passed | True | GO:0030428 | Documented focused command passed. |
| validate GO:0033101 | passed | True | GO:0033101 | Documented focused command passed. |
| validate-strict GO:0033101 | passed | True | GO:0033101 | Documented focused command passed. |
| validate cellstructuremech:coccolith | passed | True | cellstructuremech:coccolith | Documented focused command passed. |
| validate-strict cellstructuremech:coccolith | passed | True | cellstructuremech:coccolith | Documented focused command passed. |
| validate cellstructuremech:coccosphere | passed | True | cellstructuremech:coccosphere | Documented focused command passed. |
| validate-strict cellstructuremech:coccosphere | passed | True | cellstructuremech:coccosphere | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | Applicability was assessed against the complete official catalogue. Matched E. coli and B. subtilis gene/module requests are bounded to the named genes and datasets, with thresholded membership and source scopes retained. Photosystem PCC7942 data are computational context only and are not an exact-strain match for the thermophilic Jordan preparation. No S. cerevisiae dataset is in the returned catalogue; unrelated bacterial datasets are not substitutes. Morphology-only coccolith/coccosphere claims have no identified gene/locus/protein or molecular pathway to query. Eight original reviews require correction: six unsupported exemptions and two omissions. Historical native-runner unavailability is separate from these source checks, with no fresh runner success claimed. |
| Independent claim-level source review | passed | True | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native formate dehydrogenase complex UniProt verify check | passed | True | GO:0009326 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native formate dehydrogenase complex UniProt causal check | passed | True | GO:0009326 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native nitrate reductase complex UniProt verify check | passed | True | GO:0009325 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native nitrate reductase complex UniProt causal check | passed | True | GO:0009325 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native photosystem UniProt verify check | passed | True | GO:0009521 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native photosystem UniProt causal check | passed | True | GO:0009521 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proton-transporting V-type ATPase complex UniProt verify check | passed | True | GO:0033176 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proton-transporting V-type ATPase complex UniProt causal check | passed | True | GO:0033176 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proton-transporting V-type ATPase, V0 domain UniProt verify check | passed | True | GO:0033179 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proton-transporting V-type ATPase, V0 domain UniProt causal check | passed | True | GO:0033179 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proton-transporting V-type ATPase, V1 domain UniProt verify check | passed | True | GO:0033180 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proton-transporting V-type ATPase, V1 domain UniProt causal check | passed | True | GO:0033180 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cell septum UniProt verify check | passed | True | GO:0030428 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cell septum UniProt causal check | passed | True | GO:0030428 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cellular bud membrane UniProt verify check | passed | True | GO:0033101 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native cellular bud membrane UniProt causal check | passed | True | GO:0033101 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coccolith UniProt verify check | passed | True | cellstructuremech:coccolith | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coccolith UniProt causal check | passed | True | cellstructuremech:coccolith | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coccosphere UniProt verify check | passed | True | cellstructuremech:coccosphere | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native coccosphere UniProt causal check | passed | True | cellstructuremech:coccosphere | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. An empty inventory or zero molecular graph nodes does not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Generic FDH complex and respiratory example

identity: supported. Targets: GO:0009326.

GO0009326 is the exact generic complex and GO1990204 is its native is-a parent. The record explicitly frames FdnGHI/FdoGHI as respiratory examples; the generic identity must remain distinct from their particular composition and quinone coupling.

### FdnGHI membership and canonical stoichiometry

evidence: supported. Targets: GO:0009326.

Fresh CPX1975 and UniProt support three copies each of FdnG/H/I and scoped cofactors. Independently inspected author-uploaded Jormakka main text supports periplasmic alpha-site oxidation, beta Fe-S relay and membrane gamma hemes/quinone site. The text is browser-rendered author content, not a native curl article body; no universal soluble or archaeal FDH architecture is inferred.

### Assembly necessity of the conditional constituents

evidence: unknown. Targets: GO:0009326.

The record labels all three proteins CONDITIONAL. The inspected intact structures and electron-transfer functions establish membership and roles, but do not isolate removal of each protein or define assembly requirements across alternative FDH classes. Assembly necessity remains unverified; catalytic necessity is not substituted for it.

### Exact examples and bounded family withholding

grounding: supported. Targets: GO:0009326.

All three reviewed accession/name/gene/taxon pairs and bounded uniqueness queries agree. Checked Fdn and Fdo entries share candidate family mappings; IPR006471 also describes related hydrogenase/thiosulfate-reductase gamma subunits. Label-only status is defensible for these nitrate-inducible component labels, without claiming an exhaustive search or requiring optional additional examples.

### Bacterial and archaeal distribution references

scope: concern. Targets: GO:0009326.

Both broad taxonomic-distribution rows cite an unrelated viral/transcription study. E.coli FDH-N and the additional bacterial abstracts support bounded bacterial examples, but they cannot repair the declared broad bacterial frequency, methanogenic conservation or NAD+/F420-linked generalizations without appropriate sources.

### Respiratory reaction and PMF boundary

evidence: supported. Targets: GO:0009326.

GO0036397 and the native/primary evidence support formate oxidation with quinone reduction for the respiratory example. The definition explicitly invokes a redox loop, which is consistent with the primary discussion when read as the coupled FDH-N/Nar system; no standalone proton-pump claim is inferred. Broader soluble/NAD+/F420-dependent examples are outside the recovered experiment.

### Optional inventories and images

completeness: supported. Targets: GO:0009326.

The review identifies concrete existing evidence and graph defects. It does not require an image, measurement, exhaustive species inventory, or compulsory protein-family replacement merely because an optional slot is absent.

### Membership/activity summary versus mechanism

graph: concern. Targets: GO:0009326.

All five nodes and four edges were inspected. The component roles describe an electron-transfer sequence, but the graph connects each protein only by part-of and the complete structure to its activity. It does not represent transfer through the subunits or cofactor/quinone steps.

### Generic nitrate reductase versus NarGHI example

identity: supported. Targets: GO:0009325.

GO0009325 denotes the requested generic complex, GO1990204 is its parent, and GO0044799 is a narrower native NarGHI child. The identity and explicitly example-scoped NarGHI components are sound even though the copied broad definition reverses the reaction.

### Native ontology conflict and internal inconsistency

evidence: concern. Targets: GO:0009325.

The first definition sentence and structure-node description say nitrate is formed from nitrite. This wording is genuinely present in the inspected GO0009325 snapshot; it was not invented by the record. It conflicts with the record function, GO0160182, CPX1974 and Bertero primary abstract, which describe nitrate-to-nitrite reduction coupled to quinol oxidation. Preserve this source conflict while correcting the scientific wording.

### NarGHI membership and canonical stoichiometry

evidence: supported. Targets: GO:0009325.

The three named proteins, their catalytic/relay/anchor roles, two copies each in the CPX1974 canonical complex, and listed cofactors match native curation and protein annotations. The heterotrimeric functional unit is distinguished from the dimer-of-heterotrimers assembly. No NarGHI inventory is imposed on NapAB, Nas/Nia or all nitrate reductase complexes. The IPR006547 tetramer prose conflicts with the separately inspected CPX1974 and UniProt dimer-of-heterotrimers annotations; the canonical example follows the latter, preserving the source conflict.

### Assembly necessity of conditional subunits

evidence: unknown. Targets: GO:0009325.

CONDITIONAL is an assembly-necessity claim under the schema. The intact-complex/functional sources do not isolate the assembly requirements of each row across the generic alternatives. This remains unverified; the review does not reinterpret conditional as merely catalytic or taxon-specific membership.

### Exact protein and family identities

grounding: supported. Targets: GO:0009325.

All three reviewed accession/name/gene/taxon pairs and bounded exact-gene queries agree. NarG/NarH mappings match native family classes and named NCBIfam members; homolog examples do not narrow the full family to one K-12 sequence. No optional NarI family or additional inventory is forced.

### Unrelated domain-distribution citation

scope: concern. Targets: GO:0009325.

Both distribution rows cite health economics rather than nitrate reductases. The Richardson review abstract independently supports broad prokaryotic diversity at a secondary tier but is not the rows cited source and does not verify every haloarchaeal/hyperthermophile or frequency claim. The added generic eukaryotic/assimilatory cofactor scope is not established by the NarGHI structure.

### Reduction and redox-loop coupling

evidence: supported. Targets: GO:0009325.

Quinol oxidation and nitrate reduction are directly defined in GO0160182 and described in native CPX/UniProt and Bertero primary abstract. The study-specific electron-transfer route is supported at those tiers, while a detailed full-body assay or proton-pathway audit is unavailable.

### Known composition versus optional additions

completeness: supported. Targets: GO:0009325.

The existing NarGHI exemplar has complete stated subunit examples. No missing image, additional taxon, nonprotein component row, or generic inventory is itself a finding; the concrete corrections concern present claims.

### Membership/activity summary versus mechanism

graph: concern. Targets: GO:0009325.

All five nodes and four edges were inspected. The component roles describe an electron-transfer sequence, but the graph connects each protein only by part-of and the complete structure to its activity. It does not represent transfer through the subunits or cofactor/quinone steps.

### Generic photosystem and exact hierarchy

identity: supported. Targets: GO:0009521.

GO0009521 is an exact generic structure class with correct is-a, parthood and narrow synonym scopes. The appended oxygenic/anoxygenic language should remain broader than the two cyanobacterial exemplars. No single PSI/PSII structure is substituted for the generic identity.

### Cofactor allocation within oxygenic PSI

evidence: concern. Targets: GO:0009521.

PsaA/PsaB are valid oxygenic type-I constituents, but their stated binding of FX,FA,FB is wrong at the declared heterodimer scope. Jordan directly places only FX between PsaA/PsaB and assigns FA/FB to PsaC. Whole-PSI electron flow through all three centers does not make all three PsaA/PsaB-bound cofactors.

### Oxygenic type-II exemplar

evidence: supported. Targets: GO:0009521.

Umena supports the named D1/D2 reaction-center class and its P680-associated chlorophylls, pheophytins and quinones; D1 contributes most Mn4CaO5 ligands, with a direct CP43 ligand too. These named oxygenic components are examples, not a universal L/M description of all anoxygenic type-II centers. The broad generic class remains valid.

### Antenna inventory and mechanistic inference

evidence: supported. Targets: GO:0009521.

The primary PSI structure directly resolves chlorophyll and carotenoid architecture. Its excitation-transfer and triplet-quenching discussion combines structural distances with cited functional work and qualified inference. Bacteriochlorophyll is a generic anoxygenic class possibility, not a chemical observed in Jordan's chlorophyll-a preparation.

### Assembly necessity remains independent

evidence: unknown. Targets: GO:0009521.

Alternative photosystem types explain membership scope, but do not establish CONDITIONAL assembly necessity. Exact component-removal assembly endpoints were not established by these intact crystal structures. Likewise, ESSENTIAL for the grouped antenna-pigment class remains unverified as a class-wide formation requirement. Catalytic necessity, photoprotection, resolved membership and stable assembly are not interchangeable; no finding is made solely for an untested removal assay.

### Four reviewed accessions and bounded uniqueness

grounding: supported. Targets: GO:0009521.

All four declared accession/gene/status/taxon pairs and exact-node reviewed queries agree. These identity-only examples are distinct from crystallographic chain identity: RCSB1JB0 maps its PsaA/PsaB chains to P0A405/P0A407 at BP-1 tax197221, although its original source-organism field retains tax32046. That conflict affects the canonical example and is separately flagged; it does not make record P0A406/P0A408 identity annotations false.

### Primary versus annotation and abstract tiers

evidence: supported. Targets: GO:0009521.

Jordan was read from a genuine public HTTP PDF mirror after an HTTPS certificate failure; Umena from a genuine HTTPS PDF. Main-body/caption scopes are recorded. Kamiya2003/Kawakami2009 remain citation/abstract plus verified UniProt location-attribution tier because attempted JATS routes failed. No unread-body detail is credited.

### Cyanobacterial distribution and canonical preparations

scope: supported. Targets: GO:0009521.

The named taxa and historical vulcanus synonyms agree with native taxonomy. COMMON Cyanobacteriota is compatible with the native PSI definition and the oxygenic sources, without claiming universality or a measured prevalence. Jordan's source and PDB metadata use S.elongatus; Umena uses the native synonym T.vulcanus. Exact cultured stock equivalence is not independently reconstructed.

### Scoped electron transport

scope: supported. Targets: GO:0009521.

The function already restricts the P700/ferredoxin path to oxygenic/cyanobacterial PSI and explicitly excludes a universal bacterial type-I interpretation. This is supported. Coupling to ATP/reductant production belongs to the photosynthetic electron-transport system; neither PSI alone nor PSII alone is claimed as a complete ATP-synthesis enzyme.

### Membership and output versus causal path

graph: concern. Targets: GO:0009521.

All six nodes and five edges were inspected; two gene/protein nodes correctly inherit all four accessions. The graph contains three constituent edges, a membrane parthood edge and a whole-structure output. Correcting the PsaC cofactor allocation does not turn these relationships into a represented charge-separation/transfer causal path. MECHANISTIC therefore overstates its current explanatory detail.

### Bounded corrections

completeness: supported. Targets: GO:0009521.

The PsaC issue is an affirmative wrong binding allocation, not an automatic demand for an optional missing component row. No full accessory inventory, extra family identifier, image or measured-property field is required merely because it is absent. The whole maintained target and all declared stable identifiers/source identities were checked.

### Historical frozen input and current observation

provenance: supported. Targets: GO:0009326.

Original record hash is unchanged.

### Native identity and graph example gates

schema: supported. Targets: GO:0009326.

Actual native verify and causal-graphs commands passed at source head; declared component examples cover all named graph symbols. These checks do not establish mechanism or resolve the scientific findings.

### Historical frozen input and current observation

provenance: supported. Targets: GO:0009325.

Original record hash is unchanged.

### Native identity and graph example gates

schema: supported. Targets: GO:0009325.

Actual native verify and causal-graphs commands passed at source head; declared component examples cover all named graph symbols. These checks do not establish mechanism or resolve the scientific findings.

### Historical frozen input and current observation

provenance: supported. Targets: GO:0009521.

The only changed scientific fields are both reaction-center core types from PROTEIN to PROTEIN_COMPLEX, plus the dated #2420 history entry. Fresh primary/authority sources support both heterodimer groupings. Old cofactor and graph findings remain; this refresh does not edit records.

### Native identity and graph example gates

schema: supported. Targets: GO:0009521.

Actual native verify and causal-graphs commands passed at source head; declared component examples cover all named graph symbols. These checks do not establish mechanism or resolve the scientific findings.

### Bounded matching MG1655 expression context

evidence: supported. Targets: GO:0009326.

MG1655 gene searches resolve FdnG/H/I and FdoG/H/I; FdnG/H are thresholded in67, FdnG additionally69, while FdnI/Fdo genes have no above-threshold memberships in this dataset. Native module/member annotations were inspected and structural source claims separately checked. This corrects unsupported original no-expression N/A rationale. MG1655 is one K-12 context, not every strain/class; thresholds are not biological absence, and generated module prose/activity inference is excluded. The historical unavailable adapter runner was not rerun by this subreview.

### Bounded matching MG1655 expression context

evidence: supported. Targets: GO:0009325.

MG1655 NarG/H/I all occur in module67; NarG additionally69 and NarH/I additionally21. Native module/member annotations were inspected and structural source claims separately checked. This corrects unsupported original no-expression N/A rationale. MG1655 is one K-12 context, not every strain/class; thresholds are not biological absence, and generated module prose/activity inference is excluded. The historical unavailable adapter runner was not rerun by this subreview.

### PCC7942 computational context and thermophile exclusion

evidence: supported. Targets: GO:0009521.

Catalogue S.elongatus coverage resolves specifically to PCC7942. Bounded psaA/psaB searches give Synpcc7942_2049/2048 and module38 Photosystems; all44 returned members and the actual publication body support a computational expression context. The record gene names can be cross-checked there, but this is not Jordan BP-1 or Umena vulcanus evidence. No matching thermophilic dataset is listed in the retrieved catalogue; psbA/psbD paralog search hits from PCC7942 are excluded as substitutes for record tax32053. No new runner execution is claimed.

### Jordan thermophilic canonical example versus modern taxon

scope: concern. Targets: GO:0009521.

Jordan uses historical thermophilic S.elongatus naming. Later primary structural literature identifies its1JB0 preparation as Thermosynechococcus elongatus BP-1; current tax authority and SIFTS-linked P0A405/P0A407 resolve BP-1 to Thermosynechococcus vestitus tax197221. Canonical example tax32046 belongs to the separate Synechococcus lineage. Preserve the conflicting original RCSB source field rather than silently trusting or averaging it; correct the source-specific canonical mapping through curation.

### Scoped historical component-type resolution

representation: supported. Targets: GO:0009521.

Current record already types both named heterodimeric cores PROTEIN_COMPLEX; fresh primary structure evidence supports this grouping. Its existing2026-10-24 history and closed#2420 document a prior record correction. This resolves only this single-target category F1, not the seven other #2420 records or all37 category assessments; no record correction made by PR2354.

### Exact generic complex/sector identity, hierarchy and nomenclature

identity: supported. Targets: GO:0033176.

The generic GO identity and labelled parent/part relations resolve; generic versus vacuolar subtype distinctions are real. Correct identity is retained while the source/graph concerns below remain. No single protein is substituted for the structure.

### Original schema/render and unchanged frozen scientific input

schema: supported. Targets: GO:0033176.

Original native validate and render --content passed. The current target is byte-identical to the original frozen input and current main. Existing PROPOSED history is not promoted. This slice requires current reassessment but no stale-input refresh.

### Prose yeast gene identity and bounded native protein diagnostics

grounding: supported. Targets: GO:0033176.

All named yeast Vma/Vph1/Stv1 mappings inspected in the bounded reviewed UniProt result agree with the corresponding yeast subunit identities. Records maintain no protein_examples or GENE_OR_PROTEIN graph nodes: both native checks passed with empty scope. Neither these zero counts nor the prose-name query establish necessity, universal family coverage or protist nomenclature.

### Taxon, localization and reference tiers

evidence: supported. Targets: GO:0033176.

Taxon 4932 is S. cerevisiae. Kane 2006 is a secondary yeast-focused review and supports this canonical-organism context; Li/Kane and Forgac are secondary context at the sections actually read. Vph1 vacuolar and Stv1 Golgi/endosomal distinctions are retained. No independent population-frequency or universal protist composition claim follows from these sources.

### Structured-source applicability for named yeast examples

scope: not_applicable. Targets: GO:0033176.

Current iModulonDB catalogue inspection finds no organism/dataset match for named S. cerevisiae or other eukaryotic examples. No matched-gene/module summarization follows for those examples. The original no-expression-inference rationale is corrected by actual organism coverage. Historical runner unavailable; fresh direct catalogue fallback is distinct. The generic bacterial V/A extension is underdetermined because no species/strain/gene pair is named; this does not assert absence of bacterial ATPase datasets.

### Current primary access and historical source reuse

provenance: supported. Targets: GO:0033176.

Current Zhao2015 publisher access is abstract-only; its explicit yeast ten-proteolipid result, three eukaryotic stalks and rotor/stator distinction are sufficient for the retained bounded findings. Earlier full-body/Methods assertions belong only to the immutable original observation. No fresh JTY002, DDM, nucleotide-condition or subunit-e-loss audit is claimed. Secondary material and authority identities are labelled separately.

### Assembly, physiological activity and purification limits

scope: unknown. Targets: GO:0033176.

Evidence for proton pumping, vacuolar pH or localization is not automatically evidence of structural assembly necessity. Secondary assembly discussions distinguish incomplete/inactive complexes and preserve route uncertainty. No current inspection proves universal ESSENTIAL membership or exact assembly context across all fungi/protists; preparation-level facts outside the fresh primary abstract remain historical-only.

### Optional fields and representation coverage

completeness: not_applicable. Targets: GO:0033176.

No image, quantitative property, verbatim snippet, associated-trait assertion or maintained UniProt/family inventory occurs in these targets. Their absence is not converted into a quota-based finding. Native protein-check emptiness and the named-gene source audit are both disclosed.

### Broad acidocalcisome and unspecified bacterial extension

scope: unknown. Targets: GO:0033176.

The exact acidocalcisome extension is not established by the inspected primary abstract or the stated secondary sections; no contradictory biological claim is made. The broad bacterial V/A remark is not itself treated as a family error: Kane distinguishes related archaeal/bacterial enzymes and their functional diversity. Neither phrase supplies a particular bacterial adapter match.

### Qualify compartment-specific sector examples within the generic complex

scope: concern. Targets: GO:0033176.

The only component rows use vacuolar GO0000220/0000221 and are marked ESSENTIAL without an example scope, while the record identity includes organelle and plasma-membrane V-ATPases. Their labels and mappings are correct for vacuolar instances; the issue is their unqualified use as the broad class inventory.

### Match graph scope to the represented coupling

graph: concern. Targets: GO:0033176.

Parthood and whole-complex activity edges do not encode the ATP-hydrolysis, rotor and translocation transitions described in prose. MECHANISTIC promises more than this graph represents.

### Exact generic complex/sector identity, hierarchy and nomenclature

identity: supported. Targets: GO:0033179.

The generic GO identity and labelled parent/part relations resolve; generic versus vacuolar subtype distinctions are real. Correct identity is retained while the source/graph concerns below remain. No single protein is substituted for the structure.

### Original schema/render and unchanged frozen scientific input

schema: supported. Targets: GO:0033179.

Original native validate and render --content passed. The current target is byte-identical to the original frozen input and current main. Existing PROPOSED history is not promoted. This slice requires current reassessment but no stale-input refresh.

### Prose yeast gene identity and bounded native protein diagnostics

grounding: supported. Targets: GO:0033179.

All named yeast Vma/Vph1/Stv1 mappings inspected in the bounded reviewed UniProt result agree with the corresponding yeast subunit identities. Records maintain no protein_examples or GENE_OR_PROTEIN graph nodes: both native checks passed with empty scope. Neither these zero counts nor the prose-name query establish necessity, universal family coverage or protist nomenclature.

### Taxon, localization and reference tiers

evidence: supported. Targets: GO:0033179.

Taxon 4932 is S. cerevisiae. Kane 2006 is a secondary yeast-focused review and supports this canonical-organism context; Li/Kane and Forgac are secondary context at the sections actually read. Vph1 vacuolar and Stv1 Golgi/endosomal distinctions are retained. No independent population-frequency or universal protist composition claim follows from these sources.

### Structured-source applicability for named yeast examples

scope: not_applicable. Targets: GO:0033179.

Current iModulonDB catalogue inspection finds no organism/dataset match for named S. cerevisiae or other eukaryotic examples. No matched-gene/module summarization follows for those examples. The original no-expression-inference rationale is corrected by actual organism coverage. Historical runner unavailable; fresh direct catalogue fallback is distinct. No bacterial matched organism is asserted by this target.

### Current primary access and historical source reuse

provenance: supported. Targets: GO:0033179.

Current Zhao2015 publisher access is abstract-only; its explicit yeast ten-proteolipid result, three eukaryotic stalks and rotor/stator distinction are sufficient for the retained bounded findings. Earlier full-body/Methods assertions belong only to the immutable original observation. No fresh JTY002, DDM, nucleotide-condition or subunit-e-loss audit is claimed. Secondary material and authority identities are labelled separately.

### Assembly, physiological activity and purification limits

scope: unknown. Targets: GO:0033179.

Evidence for proton pumping, vacuolar pH or localization is not automatically evidence of structural assembly necessity. Secondary assembly discussions distinguish incomplete/inactive complexes and preserve route uncertainty. No current inspection proves universal ESSENTIAL membership or exact assembly context across all fungi/protists; preparation-level facts outside the fresh primary abstract remain historical-only.

### Optional fields and representation coverage

completeness: not_applicable. Targets: GO:0033179.

No image, quantitative property, verbatim snippet, associated-trait assertion or maintained UniProt/family inventory occurs in these targets. Their absence is not converted into a quota-based finding. Native protein-check emptiness and the named-gene source audit are both disclosed.

### Bind the decamer and assembly model to the source organism

scope: concern. Targets: GO:0033179.

The added definition exports a decameric proteolipid ring, yeast gene names and ER assembly account to yeasts, fungi and protists while naming only generic GO0033179 as its source. GO supplies a six-or-more description; inspected primary evidence establishes ten subunits in the particular yeast enzyme. The precise composition and assembly context need explicit source/taxon limits, without declaring the underlying yeast model false.

### Make the rotation endpoint agree with its c-ring description

graph: concern. Targets: GO:0033179.

The drives-rotation-of edge correctly describes the proteolipid c-ring moving relative to subunit a but points to the entire V0 domain. V0 includes stationary elements, so the typed endpoint should identify the rotor or use a relationship that preserves the explicitly correct substructure scope.

### Exact generic complex/sector identity, hierarchy and nomenclature

identity: supported. Targets: GO:0033180.

The generic GO identity and labelled parent/part relations resolve; generic versus vacuolar subtype distinctions are real. Correct identity is retained while the source/graph concerns below remain. No single protein is substituted for the structure.

### Original schema/render and unchanged frozen scientific input

schema: supported. Targets: GO:0033180.

Original native validate and render --content passed. The current target is byte-identical to the original frozen input and current main. Existing PROPOSED history is not promoted. This slice requires current reassessment but no stale-input refresh.

### Prose yeast gene identity and bounded native protein diagnostics

grounding: supported. Targets: GO:0033180.

All named yeast Vma/Vph1/Stv1 mappings inspected in the bounded reviewed UniProt result agree with the corresponding yeast subunit identities. Records maintain no protein_examples or GENE_OR_PROTEIN graph nodes: both native checks passed with empty scope. Neither these zero counts nor the prose-name query establish necessity, universal family coverage or protist nomenclature.

### Taxon, localization and reference tiers

evidence: supported. Targets: GO:0033180.

Taxon 4932 is S. cerevisiae. Kane 2006 is a secondary yeast-focused review and supports this canonical-organism context; Li/Kane and Forgac are secondary context at the sections actually read. Vph1 vacuolar and Stv1 Golgi/endosomal distinctions are retained. No independent population-frequency or universal protist composition claim follows from these sources.

### Structured-source applicability for named yeast examples

scope: not_applicable. Targets: GO:0033180.

Current iModulonDB catalogue inspection finds no organism/dataset match for named S. cerevisiae or other eukaryotic examples. No matched-gene/module summarization follows for those examples. The original no-expression-inference rationale is corrected by actual organism coverage. Historical runner unavailable; fresh direct catalogue fallback is distinct. No bacterial matched organism is asserted by this target.

### Current primary access and historical source reuse

provenance: supported. Targets: GO:0033180.

Current Zhao2015 publisher access is abstract-only; its explicit yeast ten-proteolipid result, three eukaryotic stalks and rotor/stator distinction are sufficient for the retained bounded findings. Earlier full-body/Methods assertions belong only to the immutable original observation. No fresh JTY002, DDM, nucleotide-condition or subunit-e-loss audit is claimed. Secondary material and authority identities are labelled separately.

### Assembly, physiological activity and purification limits

scope: unknown. Targets: GO:0033180.

Evidence for proton pumping, vacuolar pH or localization is not automatically evidence of structural assembly necessity. Secondary assembly discussions distinguish incomplete/inactive complexes and preserve route uncertainty. No current inspection proves universal ESSENTIAL membership or exact assembly context across all fungi/protists; preparation-level facts outside the fresh primary abstract remain historical-only.

### Optional fields and representation coverage

completeness: not_applicable. Targets: GO:0033180.

No image, quantitative property, verbatim snippet, associated-trait assertion or maintained UniProt/family inventory occurs in these targets. Their absence is not converted into a quota-based finding. Native protein-check emptiness and the named-gene source audit are both disclosed.

### Attach the expanded stalk description to the supporting literature

provenance: concern. Targets: GO:0033180.

The definition names only GO:0033180 as source while adding three peripheral stalks and yeast Vma protein names. The freshly accessible Zhao2015 primary abstract explicitly supports three stalks at its eukaryotic/yeast scopes, whereas the inspected older Kane2006 review retains less settled stalk models. Correct evidence placement and qualify yeast nomenclature instead of treating GO as the source of every detail.

### Match graph scope to its parthood and activity summary

graph: concern. Targets: GO:0033180.

The graph contains no represented hydrolysis-to-rotation or V0-coupling transition; its two edges give containment and whole-sector function. MECHANISTIC is stronger than the actual directed explanation.

### Generic septum versus completed division septum

identity: supported. Targets: GO:0030428.

The structure identity, broad parent and synonym types match native GO. The opening definition reproduces GO wording, including its unusual material phrasing; that inherited wording is not treated as an independently invented record error. The completed-division-septum function explicitly narrows its context. Division-site parthood is supported in the bacterial division context, without asserting a newly verified universal relation for every fungal cross-wall.

### Appended cross-domain claims lack matching cited support

scope: concern. Targets: GO:0030428.

The added definition assigns pseudomurein/S-layer septa to archaea, chitin/beta-glucan septa and actomyosin/septin control to fungi, and FtsZ-directed synthesis to prokaryotes. The sole definition_source is GO0030428, which supplies none of these extensions. The two literature sources are bacterial reviews. These source scopes do not establish the broad materials/mechanism formulation.

### Material identity and deposition context

grounding: concern. Targets: GO:0030428.

Septal peptidoglycan is a supported bacterial constituent. Its label-only rationale unnecessarily requires a septum-specific chemical identifier: native CHEBI8005 grounds the material class while role and evidence can preserve its bacterial septal location. CONDITIONAL is bounded by walled bacterial context; this audit does not infer an assembly knockout result or a particular cross-link composition.

### Qualified bacterial occurrence and model examples

scope: supported. Targets: GO:0030428.

The Bacteria row explicitly limits itself to walled FtsZ-dividing bacteria. The review supports septal synthesis in E.coli and B.subtilis; taxonomy receipts distinguish K-12 strain from B.subtilis species. COMMON is qualitative occurrence, not a surveyed proportion. Exact experimental stock identity is not inferred from the broad review.

### Completed septum compartmentalization

evidence: supported. Targets: GO:0030428.

The daughter-cell function cites the exact narrower GO0000935 definition and explicitly says completed division septum. It does not require every developmental septum or porous hyphal cross-wall to block all exchange. Bacterial septal material and its division-plane context remain supported independently of the definition-scope problem.

### Descriptive topology is overstated as mechanism

graph: concern. Targets: GO:0030428.

The graph contains two parthood edges and one whole-septum mediates compartmentalization edge. Those descriptions preserve useful bounded structural context but do not encode a causal transition from material deposition or closure to the function. MECHANISTIC overstates the represented explanation.

### Optional inventories and state

completeness: supported. Targets: GO:0030428.

No universal protein inventory, stoichiometry, dimensions, image or trait link is required. Further fungal/archaeal components need their own scoped evidence. No verbatim snippet is present to verify. PROPOSED status and historical events are preserved; this review does not certify historical authorship.

### Bounded structured-source applicability

evidence: supported. Targets: GO:0030428.

FtsZ wording triggers applicability. Fresh catalogue matches E. coli precise1k and B. subtilis modulome. Exact ftsZ searches and gene records identify b0095 and BSU_15290. Returned memberships are all below stored module thresholds (201/72 rows), so no positive module requires summary. This contextual result neither proves nor refutes septal function and does not repair cross-domain definition sourcing.

### Current native checks and frozen original provenance

schema: supported. Targets: GO:0030428.

Original native schema/render and target hashes pass. Root current protein verification/causal commands exit0 with empty inventory and zero gene-protein nodes; these checks do not independently validate narrative molecules or assembly necessity.

### Specialized region of the plasma membrane

identity: supported. Targets: GO:0033101.

The GO identity, membrane parent, cellular-bud/plasma-membrane parthood and UniProt location xref agree. The exact bud membrane synonym is supported. A membrane region is distinguished from the bud as a whole and the growth machinery.

### Collective lipid boundary and protein boundary

grounding: supported. Targets: GO:0033101.

The component denotes the collective lipid bilayer surrounding the bud, not one identified lipid molecule. Leaving this assemblage label-only is justified; a generic individual lipid CURIE would not name its composition. ESSENTIAL is interpretable here as the defining lipid boundary required for a membrane to exist, not as evidence that any particular lipid species or recruited factor is individually necessary. The resolved exocyst/Pea2/Spa2 discussion is a representation boundary, not a claim of no protein association.

### Budding yeast and polarized membrane growth

evidence: supported. Targets: GO:0033101.

Valtz supports S.cerevisiae budding/polarity context; Finger supports polarized secretion sites at bud cortex. The growth function combines this directly observed site organization with the study introduction/discussion account of membrane delivery. It does not claim a measured membrane-growth rate, complete exocyst mechanism or a prevalence census.

### Explicitly nonmechanistic membrane topology

graph: supported. Targets: GO:0033101.

The surrounds and plasma-membrane parthood edges match GO/UniProt. NONMECHANISTIC and its scope note accurately limit the graph to topology, while leaving secretion and polarity machinery in cited discussion.

### Bounded clean review

completeness: supported. Targets: GO:0033101.

No concrete scientific-record corrective issue was observed. Exact lipid species, quantities, protein examples, image, trait link and full mechanism are not mandatory optional inventories. Evidence uses notes, not unverifiable quotations. PROPOSED state and history are preserved.

### Bounded structured-source applicability

evidence: not_applicable. Targets: GO:0033101.

Specific Sec3/Pea2/Spa2 localization and polarity claims trigger molecular applicability despite exclusion from the lipid-boundary inventory. Fresh catalogue contains no S. cerevisiae dataset; downstream organism-matched gene/module requests are not applicable. No expression-claim exemption or bacterial taxon substitution is used.

### Current native checks and frozen original provenance

schema: supported. Targets: GO:0033101.

Original native schema/render and target hashes pass. Root current protein verification/causal commands exit0 with empty inventory and zero gene-protein nodes; these checks do not independently validate narrative molecules or assembly necessity.

### Individual mineral scale, distinct from covering and vesicle

identity: supported. Targets: cellstructuremech:coccolith.

The local identifier uniquely resolves to the maintained scale record. OTHER kind avoids calling one scale a continuous layer. The broad GO parent is appropriate, while vesicle, entire coccosphere and narrower holo-/heterococcolith types retain separate identities. No unconditional vesicle parthood or exclusively extracellular development is asserted.

### Mineral grounding and unresolved organic chemistry

grounding: supported. Targets: cellstructuremech:coccolith.

The calcite grounding is exact at mineral-material level. Associated organic material is experimentally supported, but oxidation and morphology do not identify one polymer or protein family. REVIEWED_LABEL_ONLY and UNKNOWN necessity correctly preserve that limit. Post-assembly persistence after oxidation does not establish dispensability for formation.

### Two species examples retain their experimental preparation

scope: supported. Targets: cellstructuremech:coccolith.

Native taxa match the named species. RCC1130 is established by the supplement; CCMP374 calcified donor identity is established separately from naked recipient cultures in Johns. No generic crystal count, size, shape, broad prevalence or single-morphotype adsorption rule is promoted.

### Covering element and scoped adsorption

evidence: supported. Targets: cellstructuremech:coccolith.

Individual scales demonstrably contribute to an external covering. The adsorption function is limited to the tested E.huxleyi system and organic-removal comparison. The record does not infer universal adaptive protection, exact adhesion chemistry or nucleation-template mechanism.

### Exact image, license and preparation

provenance: supported. Targets: cellstructuremech:coccolith.

The local unmodified Figure1 byte hashes, PMC accession and media locator agree. JATS licenses the article under CC BY4.0, and attribution agrees with author metadata. Mixed SEM/diagram/AFM content is explicitly described; species and sample preparation remain scoped.

### Boundaries and optional omissions are justified

completeness: supported. Targets: cellstructuremech:coccolith.

No concrete scientific-record corrective issue was observed. Unidentified vesicle particles are not imported as scale constituents; unresolved organic inventory and crystal-ordering mechanisms remain explicit. No causal graph, trait link or numeric property is required solely because the source contains one. No verbatim snippet or status promotion is present.

### Bounded structured-source applicability

evidence: not_applicable. Targets: cellstructuremech:coccolith.

The target contains calcite and unresolved mixed organic material, without an identified gene/locus/protein constituent or named molecular pathway assertion. Generic unidentified vesicle densities/full-ATPase comparison is explicitly excluded from the target composition. The sparse material/morphology scope does not require gene/module searches. Fresh catalogue additionally has no matching named haptophyte dataset; no expression or biological absence inferred.

### Current native checks and frozen original provenance

schema: supported. Targets: cellstructuremech:coccolith.

Original native schema/render and target hashes pass. Root current protein verification/causal commands exit0 with empty inventory and zero gene-protein nodes; these checks do not independently validate narrative molecules or assembly necessity.

### Whole covering and structural parthood

identity: supported. Targets: cellstructuremech:coccosphere.

The local coccosphere identity uniquely resolves. External encapsulating structure is a broader parent; has_part points to the separately frozen individual-scale record. Scale, whole covering, vesicle and organic matrix are kept distinct. ENVELOPE_LAYER does not assert exactly one geometric layer.

### Calcite and mixed extracellular material

grounding: supported. Targets: cellstructuremech:coccosphere.

Calcite is correctly grounded. The matrix is supported by lectin staining and retained pattern after decalcification but is not a chemically identified polymer or protein family. Label-only identity and UNKNOWN formation necessity are appropriate. Intracellular tubulin imaged during division is not thereby a constituent of the external covering.

### CS-369 and PLY182g contexts

scope: supported. Targets: cellstructuremech:coccosphere.

Taxon authorities match each species and the older C.pelagicus-subspecies name. Xu documents CS-369 and pooled light/CO2 conditions; Walker documents PLY182g. Counting assumptions, preparation, species differences and treatment context are accurately retained instead of promoting universal plate numbers or layer counts.

### Covering organization and daughter-cell separation

evidence: supported. Targets: cellstructuremech:coccosphere.

SEM supports the collective-covering function. Walker supports rearrangement during division and an association between disrupted covering and failure of daughter-cell separation in Ge/HEDP-treated C.braarudii. The record explicitly distinguishes this from failure of initial cytokinesis, low-Ca effects and universal calcification requirements; it retains confounding-treatment and adhesion-mechanism uncertainty.

### Scale origin and ecological boundaries

scope: supported. Targets: cellstructuremech:coccosphere.

Johns establishes adsorption from external donor scales, including mixed morphotypes/species. Structural has_part does not imply same-host biosynthesis. The record avoids treating every attached scale as a reconstructed covering or assigning a universal antiviral, grazing-protection or photosynthetic benefit.

### Exact SEM figure and source-specific license

provenance: supported. Targets: cellstructuremech:coccosphere.

Local Figure2 SHA-256 and media MD5 match the record and native PMC package. The source caption identifies white1micrometre bars and red neighboring counts. Culture/SEM preparation and estimated whole-sphere counts are correctly qualified. Full source-specific attribution satisfies the inspected CC BY4.0 statement.

### Supported boundaries with acknowledged unknowns

completeness: supported. Targets: cellstructuremech:coccosphere.

No concrete scientific-record corrective issue was observed. Exact matrix chemistry, assembly mechanism, counts, causal graph and traits are not mandatory inventories. Omitted intracellular cytoskeleton is an explicit boundary decision, not a claim that it cannot affect division or trafficking. PROPOSED status and historical events remain unchanged.

### Bounded structured-source applicability

evidence: not_applicable. Targets: cellstructuremech:coccosphere.

The target contains calcite and unresolved mixed organic material, without an identified gene/locus/protein constituent or named molecular pathway assertion. Generic intracellular tubulin imaging is explicitly excluded from the target composition. The sparse material/morphology scope does not require gene/module searches. Fresh catalogue additionally has no matching named haptophyte dataset; no expression or biological absence inferred.

### Current native checks and frozen original provenance

schema: supported. Targets: cellstructuremech:coccosphere.

Original native schema/render and target hashes pass. Root current protein verification/causal commands exit0 with empty inventory and zero gene-protein nodes; these checks do not independently validate narrative molecules or assembly necessity.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0009326, GO:0009325, GO:0009521, GO:0033176, GO:0033179, GO:0033180, GO:0030428, GO:0033101, cellstructuremech:coccolith, cellstructuremech:coccosphere.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t0-F1: Replace the unrelated taxonomic-distribution citation

major / open / confirmed; issue key: formate-dehydrogenase-complex-unrelated-distribution-reference.

Both bacterial and archaeal distribution claims cite PMID11884601, which resolves to a study of HA95/PKA and EBV-mediated transcription. It provides no support for formate-dehydrogenase occurrence, frequency, or conservation in either domain. The E.coli FDH-N structure supports a specific bacterial example, not the uncited archaeal/general-frequency claims.

### plaque-t0-F2: Represent the supported electron-transfer steps or narrow graph scope

minor / open / confirmed; issue key: formate-dehydrogenase-complex-graph-explanatory-scope.

The FUNCTION graph is marked MECHANISTIC but contains only three constituent part-of edges and one whole-complex activity edge. These relationships are sound for the named example, yet they do not express the causal transfer route described in the prose. Preserve them as NONMECHANISTIC or add experimentally scoped electron-transfer transitions. Do not infer that a generic class always has this species-specific subunit set.

### plaque-t1-F1: Correct the reversed nitrate/nitrite reaction while preserving the upstream conflict

major / open / confirmed; issue key: nitrate-reductase-complex-reversed-definition-reaction.

The definition opening and structure-node description assert formation of nitrate from nitrite. Native GO0009325 currently contains that same wording, but the record itself and independent GO0160182/CPX1974/Bertero abstract evidence describe the nitrate-to-nitrite reaction. This is a material direction contradiction, not an identity mismatch or proof that every nitrite-oxidizing enzyme is the target.

### plaque-t1-F2: Replace the unrelated taxonomic-distribution citation

major / open / confirmed; issue key: nitrate-reductase-complex-unrelated-distribution-reference.

Both bacterial and archaeal rows cite PMID12950096, a health-economics study of willingness to pay. It cannot support nitrate-reductase occurrence or frequency. Other readable secondary/native sources provide bounded context, but do not validate that attached citation or all detailed taxon claims.

### plaque-t1-F3: Represent the supported electron-transfer steps or narrow graph scope

minor / open / confirmed; issue key: nitrate-reductase-complex-graph-explanatory-scope.

The FUNCTION graph is marked MECHANISTIC but contains only three constituent part-of edges and one whole-complex activity edge. These relationships are sound for the named example, yet they do not express the causal transfer route described in the prose. Preserve them as NONMECHANISTIC or add experimentally scoped electron-transfer transitions. Do not infer that a generic class always has this species-specific subunit set.

### plaque-t2-F1: Assign FA and FB to PsaC rather than the PsaA/PsaB heterodimer

major / open / confirmed; issue key: photosystem-psaa-psab-terminal-cluster-allocation.

The type-I core role and duplicated graph descriptions say the PsaA/PsaB heterodimer binds FX,FA,FB. Jordan2001 pp911 and913 explicitly place FA/FB in the separate stromal PsaC subunit, while FX is jointly ligated by PsaA/PsaB. The full PSI electron-transfer sequence is correct but has been conflated with the binding inventory of one component.

### plaque-t2-F2: Align graph scope with the represented relationships

minor / open / confirmed; issue key: photosystem-membership-output-graph-scope.

The FUNCTION graph is marked MECHANISTIC but consists of constituent/compartment parthood and photosystem-to-electron-transport output. The process description names P700 excitation and electron transfer, but the graph does not represent a directed causal transition among those events. Preserve the supported summary as NONMECHANISTIC or encode a bounded source-supported transfer path.

### plaque-t2-F3: Reconcile the thermophilic Jordan PSI example with current BP-1 taxonomy

major / open / confirmed; issue key: photosystem-jordan-canonical-example-taxon-conflation.

The canonical example attaches Jordan2001 to modern Synechococcus elongatus tax32046. The original paper uses historical thermophilic S.elongatus naming, but later primary structural literature explicitly identifies its1JB0 preparation as Thermosynechococcus elongatus BP-1. Current ENA and the deposition SIFTS-linked P0A405/P0A407 identify that strain as Thermosynechococcus vestitus BP-1 tax197221, a separate lineage. The original RCSB source-organism field still says32046, so the conflict must remain explicit. Identity-only record examples P0A406/P0A408 correctly resolve to32046 and must not be mislabeled as the exact crystal chains. PCC7942 coexpression data cannot support the thermophilic preparation.

### plaque-historical-core-types: Heterodimeric reaction-center core components in photosystem.yaml (GO:0009521) are typed PROTEIN instead of PROTEIN_COMPLEX

minor / resolved / confirmed; issue key: photosystem-reaction-center-core-component-types.

In data/structures/energy_complex/photosystem.yaml (GO:0009521), components#type_i_reaction_center_core (label: 'Type I (Fe-S type) photosystem reaction center core (PsaA/PsaB)', gene_symbols: [psaA, psaB]) and components#type_ii_reaction_center_core (label: 'Type II (pheophytin-quinone type) photosystem reaction center core (D1/PsbA and D2/PsbD)', gene_symbols: [psbA, psbD]) represent heterodimeric reaction-center core subcomplexes rather than a single protein family, and should be typed component_type: PROTEIN_COMPLEX.

Disposition: Current record already types both named heterodimeric cores PROTEIN_COMPLEX; fresh primary structure evidence supports this grouping. Its existing2026-10-24 history and closed#2420 document a prior record correction. This resolves only this single-target category F1, not the seven other #2420 records or all37 category assessments; no record correction made by PR2354.

### micro-F1: Qualify compartment-specific sector examples within the generic complex

minor / open / confirmed; issue key: generic-v-atpase-vacuolar-component-scope.

The only component rows use vacuolar GO0000220/0000221 and are marked ESSENTIAL without an example scope, while the record identity includes organelle and plasma-membrane V-ATPases. Their labels and mappings are correct for vacuolar instances; the issue is their unqualified use as the broad class inventory.

### micro-F2: Match graph scope to the represented coupling

minor / open / confirmed; issue key: generic-v-atpase-static-graph-scope.

Parthood and whole-complex activity edges do not encode the ATP-hydrolysis, rotor and translocation transitions described in prose. MECHANISTIC promises more than this graph represents.

### micro-F3: Bind the decamer and assembly model to the source organism

major / open / confirmed; issue key: generic-v0-yeast-decamer-assembly-scope.

The added definition exports a decameric proteolipid ring, yeast gene names and ER assembly account to yeasts, fungi and protists while naming only generic GO0033179 as its source. GO supplies a six-or-more description; inspected primary evidence establishes ten subunits in the particular yeast enzyme. The precise composition and assembly context need explicit source/taxon limits, without declaring the underlying yeast model false.

### micro-F4: Make the rotation endpoint agree with its c-ring description

minor / open / confirmed; issue key: generic-v0-rotating-substructure-endpoint.

The drives-rotation-of edge correctly describes the proteolipid c-ring moving relative to subunit a but points to the entire V0 domain. V0 includes stationary elements, so the typed endpoint should identify the rotor or use a relationship that preserves the explicitly correct substructure scope.

### micro-F5: Attach the expanded stalk description to the supporting literature

minor / open / confirmed; issue key: generic-v1-expanded-architecture-source.

The definition names only GO:0033180 as source while adding three peripheral stalks and yeast Vma protein names. The freshly accessible Zhao2015 primary abstract explicitly supports three stalks at its eukaryotic/yeast scopes, whereas the inspected older Kane2006 review retains less settled stalk models. Correct evidence placement and qualify yeast nomenclature instead of treating GO as the source of every detail.

### micro-F6: Match graph scope to its parthood and activity summary

minor / open / confirmed; issue key: generic-v1-static-graph-scope.

The graph contains no represented hydrolysis-to-rotation or V0-coupling transition; its two edges give containment and whole-sector function. MECHANISTIC is stronger than the actual directed explanation.

### septin-S2354-F1: Source the expanded definition at its actual domain scope

major / open / confirmed; issue key: cell-septum-definition-domain-scope.

The appended definition moves beyond native GO into cross-domain material assignments and a prokaryote-versus-fungus cytokinetic mechanism. GO0030428 does not contain those claims, and the cited reviews concern bacterial division. This is a material evidence-scope gap, not a claim that all fungal septation statements are false.

### septin-S2354-F2: Separate peptidoglycan identity from its septal location

minor / open / confirmed; issue key: cell-septum-peptidoglycan-material-grounding.

The component is explicitly bacterial peptidoglycan, but its grounding note requires a term that also encodes deposition at division septa. CHEBI8005 supplies the verified material-class identity. Septal placement and exclusion of fungal chitin/glucan can remain in the role and evidence.

### septin-S2354-F3: Match graph scope to its topology

minor / open / confirmed; issue key: cell-septum-static-graph-scope.

The MECHANISTIC graph consists of constituent and context parthood plus a whole-structure-to-function mediates edge. It does not represent the material-deposition, closure or other causal transition that explains compartmentalization. This concerns scope classification, not a demand for atomic detail.

## Recommended Actions And Acceptance Checks

### plaque-t0-A1

Attach relevant, directly inspected distribution sources or narrow/defer the unsupported rows.

- Preserve the verified broad complex identity and E.coli example.
- Each bacterial/archaeal occurrence and frequency claim must match its own source; do not use one bacterial structure paper to prove archaeal conservation.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

### plaque-t0-A2

Match graph scope to its actual explanatory content.

- Retain valid membership and activity statements.
- A mechanistic version must resolve the supported subunit/cofactor electron route and distinguish the specific E.coli holoenzyme from the generic class.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

### plaque-t1-A1

Use biologically correct reduction wording and document the source discrepancy rather than silently pretending GO already says it.

- Nitrate is the reduced substrate and nitrite the product for the stated NarGHI reaction.
- The source-specific GO quotation may remain as an attributed historical/current-source observation, but must not serve as an unqualified biological definition.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

### plaque-t1-A2

Source each actual distribution statement appropriately or narrow/defer it.

- Keep generic class, respiratory NarGHI, periplasmic Nap and assimilatory alternatives distinct.
- Use inspected taxon-specific or explicitly broad sources; retain the secondary tier of review-based generalizations.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

### plaque-t1-A3

Match graph scope to its actual explanatory content.

- Retain valid membership and activity statements.
- A mechanistic version must resolve the supported subunit/cofactor electron route and distinguish the specific E.coli holoenzyme from the generic class.
- Any scientific correction requires separately authorized guarded curation, append-only history, rendering and native validation.

### plaque-t2-A1

Narrow the PsaA/PsaB binding description to P700 and its actual acceptors, including shared FX; identify FA/FB as PsaC-bound when describing the complete PSI electron path. A new component row is optional, but the existing assignment must be corrected.

- Check the correction against Jordan Polypeptide subunits p911 and Electron transfer chain p913.
- Keep full-complex electron-transfer order separate from protein-specific coordination and reconcile all duplicated role text.
- Apply only through separately authorized curation with guarded writing/history and native focused validation.

### plaque-t2-A2

Retain supported membership and the existing oxygenic-PSI function restriction, and either narrow the scope label or represent the relevant charge-separation/transfer steps with correct subunit/cofactor actors.

- Do not turn every generic photosystem into the same oxygenic PSI mechanism.
- A source-supported causal transition is sufficient; no atomistic simulation is required.
- Apply only through separately authorized curation with guarded writing/history and native focused validation.

### plaque-t2-A3

Use the verified BP-1 canonical taxon and retain historical names plus the conflicting deposition metadata in source notes. Reassess whether identity-only protein examples should remain separate examples; do not silently relabel their existing accessions.

- Cited Jordan1JB0 preparation maps to the verified thermophilic BP-1 lineage, with historical naming explicitly explained.
- Distinguish record P0A406/P0A408 identity examples from deposition P0A405/P0A407; no PCC7942 transcriptome substitution.
- Separate guarded record curation, history and native validation; no record edit in this review PR.

### micro-A1

Use the generic sector identities for a generic inventory or explicitly retain the vacuolar rows as scoped examples; reconcile duplicate generic/vacuolar graph nodes.

- Native GO must preserve generic-versus-vacuolar subtype relations.
- Yeast vacuolar evidence must not imply universal compartment-specific constituents.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### micro-A2

Classify the current graph as descriptive or add a bounded source-supported hydrolysis-to-rotation-to-proton-transport path.

- Retain correct distinction between rotor and stationary V0 elements.
- No invented molecular-detail quota or universal taxon mechanism.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### micro-A3

Separate the generic V0 definition from a cited S.cerevisiae structural/assembly example; retain historical source uncertainty and obtain matched evidence before widening the exact count.

- Cite the source actually supporting ten proteolipids and its experimental preparation.
- Do not infer native subunit dispensability from purification losses; any particular preparation-level assertion requires inspection of matched primary Methods, which current abstract access does not provide.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### micro-A4

Introduce a source-supported c-ring/rotor node or change the relation to coupling with V0 while retaining the substructure explanation.

- The directed relation must not entail rigid-body rotation of all V0.
- Retain the existing correct functional qualification and real coupling path.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### micro-A5

Add narrow source attribution for the expanded architecture and mark the yeast protein names as a scoped example; preserve distinctions between EG stalks and other collar/stator elements.

- GO-supplied text and later structural evidence must be distinguishable.
- Do not export yeast gene tokens as independently established protist names.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### micro-A6

Narrow scope for the existing summary or add a source-supported catalytic/rotor coupling path.

- Preserve the intact-enzyme context and distinguish rotor from stator.
- No optional complete subunit inventory is required to repair scope.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### septin-S2354-C1

Retain the sourced generic definition or add directly inspected, explicitly taxon-bounded support for each added material/mechanism claim; avoid treating all prokaryotes as sharing one septation apparatus.

- Retained statements must be supported at their actual taxon scope.
- Preserve the narrower completed-division-septum function.
- Run focused schema and strict-reference checks.

### septin-S2354-C2

Ground the material class to verified CHEBI8005, using a class-level label if needed for label correspondence, and retain the septal/bacterial qualifier in role and evidence.

- Do not equate peptidoglycan with chitin or archaeal pseudomurein.
- Do not invent exact polymer chemistry or assembly necessity.
- Run identifier-label, schema and strict-reference checks.

### septin-S2354-C3

Mark the current graph NONMECHANISTIC with an explicit scope note, or represent a source-supported causal transition at its taxon and developmental scope.

- Preserve valid structural edges.
- Do not generalize bacterial FtsZ dynamics across domains.
- Run native graph coverage and focused validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/energy_complex/formate_dehydrogenase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e; current SHA256 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T100134Z-formate-dehydrogenase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/energy_complex/nitrate_reductase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459; current SHA256 ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T100137Z-nitrate-reductase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/energy_complex/photosystem.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ae1b5fe34147a0a1464e24943d5d8e1aca5cdd14e737af3ab0564fecabe65d35; current SHA256 c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261021T100138Z-photosystem-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4; current SHA256 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T100139Z-proton-transporting-v-type-atpase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c; current SHA256 f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300; current SHA256 a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/envelope/cell_septum.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54; current SHA256 feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T100142Z-cell-septum-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/envelope/cellular_bud_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f; current SHA256 e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T100144Z-cellular-bud-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/envelope/coccolith.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa; current SHA256 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T100145Z-coccolith-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/envelope/coccosphere.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299; current SHA256 b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T100146Z-coccosphere-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-formate-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009326,GO:1990204,GO:0098803,GO:0036397; results: id, name, definition and native relations | context_only | Verified exact native term identities and definitions: [('GO:1990204', 'oxidoreductase complex'), ('GO:0098803', 'respiratory chain complex'), ('GO:0009326', 'formate dehydrogenase complex'), ('GO:0036397', 'formate dehydrogenase (quinone) activity')]. Preserve nitrate GO0009325 reversed-reaction conflict and distinguish photosystem generic identity from oxygenic examples. |
| plaque-formate-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 83333 as Escherichia coli K-12; lineage Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae; Escherichia; ; historical names ['Escherichia coli K12:equivalent name']. |
| plaque-formate-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 2 as Bacteria; lineage root/domain lineage not supplied; historical names ['"Bacteriobiota" Luketa 2012:authority', '"Bacteria" Cavalier-Smith 1987:authority', 'Bacteriobiota:synonym', 'Bacteria (ex Cavalier-Smith 1987):synonym', 'Bacteria Woese et al. 2024:synonym', 'bacteria:genbank common name', 'bacteria &lt;genbank common name&gt;:genbank common name']. |
| plaque-formate-agent-tax-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 2157 as Archaea; lineage root/domain lineage not supplied; historical names ['Archaea Woese et al. 2024:authority', '"Archaea" Woese et al. 1990:authority', '"Archaebiota" Luketa 2012:authority', '"Archaebacteria" (sic) Woese and Fox 1977:authority', 'Archaebiota:synonym', 'Archaebacteria:synonym', 'Mendosicutes:synonym', 'Metabacteria:synonym']. |
| plaque-formate-agent-CPX-1975 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1975; participants, systematicName, complexAssemblies, functions and cofactors | context_only | Formate dehydrogenase N complex, source Escherichia coli (strain K12); 83333; 3xfdnG:3xfdnH:3xfdnI, assembly ['Heterononamer']. Participant identities, redox roles and source-specific cofactor inventory verified; not generic-class stoichiometry. |
| plaque-formate-agent-P24183 | https://rest.uniprot.org/uniprotkb/P24183.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P24183: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli (strain K12)); genes ['fdnG']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-formate-agent-query-fdnG | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P24183', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-formate-agent-P0AAJ3 | https://rest.uniprot.org/uniprotkb/P0AAJ3.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P0AAJ3: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli (strain K12)); genes ['fdnH']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-formate-agent-query-fdnH | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P0AAJ3', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-formate-agent-P0AEK7 | https://rest.uniprot.org/uniprotkb/P0AEK7.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P0AEK7: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli (strain K12)); genes ['fdnI']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-formate-agent-query-fdnI | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P0AEK7', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-formate-agent-chebi-60539 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_60539; Native ChEBI term identity | context_only | Verified [('CHEBI:60539', 'Mo(=O)-bis(molybdopterin guanine dinucleotide)(4-)')]. Chemical identifiers do not independently prove assembly necessity. |
| plaque-formate-agent-chebi-16374 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16374; Native ChEBI term identity | context_only | Verified [('CHEBI:16374', 'menaquinone')]. Chemical identifiers do not independently prove assembly necessity. |
| plaque-formate-agent-chebi-30413 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30413; Native ChEBI term identity | context_only | Verified [('CHEBI:30413', 'heme')]. Chemical identifiers do not independently prove assembly necessity. |
| plaque-formate-agent-chebi-33725 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33725; Native ChEBI term identity | context_only | Verified [('CHEBI:33725', 'tetra-mu3-sulfido-tetrairon(0)')]. Chemical identifiers do not independently prove assembly necessity. |
| plaque-formate-agent-pmid-11884747 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11884747+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('11884747', 'Molecular basis of proton motive force generation: structure of formate dehydrogenase-N.', '10.1126/science.1068186')]. Read abstract tier only in this response. |
| plaque-formate-agent-pmid-11884601 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11884601+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('11884601', 'Protein kinase A associates with HA95 and affects transcriptional coactivation by Epstein-Barr virus nuclear proteins.', '10.1128/mcb.22.7.2136-2146.2002')]. Read abstract tier only in this response. The HA95/PKA/EBV paper is unrelated to formate-dehydrogenase distribution. |
| plaque-formate-agent-jormakka2002-browser | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; Source transport/access attempt | context_only | Actual curl HTTP 403, exit 0; 21293 bytes. This attempt did not provide a usable scientific article body and supports no biological absence inference. |
| plaque-formate-agent-IPR006443 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006443/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Formate dehydrogenase-N, alpha subunit', 'short': 'Formate-DH-alph_fdnG'}; members {'ncbifam': {'TIGR01553': 'formate dehydrogenase-N subunit alpha'}}. Family identity inspected, without imposing an exact isoenzyme-only grounding or interpreting homolog coverage as assembly proof. |
| plaque-formate-agent-IPR006470 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006470/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Formate dehydrogenase iron-sulphur subunit, Proteobacteria', 'short': 'Formate_DH_bsu_Proteobacteria'}; members {'cdd': {'cd10558': 'The beta FeS subunit of formate dehydrogenase-N (FDH-N)'}, 'ncbifam': {'TIGR01582': 'formate dehydrogenase subunit beta'}}. Family identity inspected, without imposing an exact isoenzyme-only grounding or interpreting homolog coverage as assembly proof. |
| plaque-formate-agent-IPR006471 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006471/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Formate dehydrogenase, gamma subunit', 'short': 'Formate_DH_gsu'}; members {'ncbifam': {'TIGR01583': 'formate dehydrogenase subunit gamma'}}. Broader homologous gamma-subunit coverage includes hydrogenase/thiosulfate-reductase context; not an FdnI-only grounding. |
| plaque-formate-agent-IPR014603 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014603/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Formate dehydrogenase iron-sulphur subunit', 'short': 'Formate_DH_Fe-S_su'}; members {'pirsf': {'PIRSF036298': 'Formate dehydrogenase, iron-sulphur subunit'}}. Family identity inspected, without imposing an exact isoenzyme-only grounding or interpreting homolog coverage as assembly proof. |
| plaque-formate-agent-IPR051555 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051555/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Formate Dehydrogenase Electron Transfer Unit', 'short': 'FDH_Electron_Transfer_Unit'}; members {'panther': {'PTHR43545': 'Formate Dehydrogenase Electron Transfer Unit'}}. Description flagged llm:true/checked:false; generated prose is excluded as mechanism evidence. |
| plaque-formate-agent-IPR051817 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051817/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Formate dehydrogenase cytochrome b556 subunit', 'short': 'FDH_cytochrome_b556_subunit'}; members {'panther': {'PTHR30074': 'Formate dehydrogenase cytochrome b556 subunit'}}. Description flagged llm:true/checked:false; generated prose is excluded as mechanism evidence. |
| plaque-formate-agent-query-fdoG | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P32176', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-formate-agent-query-fdoH | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P0AAJ5', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-formate-agent-query-fdoI | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P0AEL0', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-formate-agent-pmid-1504073 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A1504073+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('1504073', 'A second phenazine methosulphate-linked formate dehydrogenase isoenzyme in Escherichia coli.', '10.1016/0005-2736(92)90417-k')]. Read abstract tier only in this response. |
| plaque-formate-agent-pmid-8566699 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8566699+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('8566699', 'Purification and characterization of the formate dehydrogenase from Desulfovibrio vulgaris Hildenborough.', '10.1111/j.1574-6968.1995.tb07875.x')]. Read abstract tier only in this response. |
| plaque-nitrate-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009325,GO:1990204,GO:0044799,GO:0160182; results: id, name, definition and native relations | context_only | Verified exact native term identities and definitions: [('GO:0044799', 'NarGHI complex'), ('GO:1990204', 'oxidoreductase complex'), ('GO:0009325', 'nitrate reductase complex'), ('GO:0160182', 'nitrate reductase (quinone) activity')]. Preserve nitrate GO0009325 reversed-reaction conflict and distinguish photosystem generic identity from oxygenic examples. |
| plaque-nitrate-agent-CPX-1974 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1974; participants, systematicName, complexAssemblies, functions and cofactors | context_only | Nitrate reductase A complex, source Escherichia coli (strain K12); 83333; 2xnarG:2xnarH:2xnarI, assembly ['Heterohexamer']. Participant identities, redox roles and source-specific cofactor inventory verified; not generic-class stoichiometry. |
| plaque-nitrate-agent-P09152 | https://rest.uniprot.org/uniprotkb/P09152.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P09152: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli (strain K12)); genes ['narG']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-nitrate-agent-query-narG | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P09152', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-nitrate-agent-P11349 | https://rest.uniprot.org/uniprotkb/P11349.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P11349: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli (strain K12)); genes ['narH']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-nitrate-agent-query-narH | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P11349', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-nitrate-agent-P11350 | https://rest.uniprot.org/uniprotkb/P11350.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P11350: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli (strain K12)); genes ['narI']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-nitrate-agent-query-narI | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P11350', 83333)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-nitrate-agent-chebi-21137 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_21137; Native ChEBI term identity | context_only | Verified [('CHEBI:21137', 'tri-mu-sulfido-mu3-sulfido-triiron')]. Chemical identifiers do not independently prove assembly necessity. |
| plaque-nitrate-agent-chebi-49883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49883; Native ChEBI term identity | context_only | Verified [('CHEBI:49883', 'tetra-mu3-sulfido-tetrairon')]. Chemical identifiers do not independently prove assembly necessity. |
| plaque-nitrate-agent-pmid-12910261 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12910261+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('12910261', 'Insights into the respiratory electron transfer pathway from the structure of nitrate reductase A.', '10.1038/nsb969')]. Read abstract tier only in this response. |
| plaque-nitrate-agent-pmid-12950096 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12950096+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('12950096', "Willingness to pay and size of health benefit: an integrated model to test for 'sensitivity to scale'.", '10.1002/hec.786')]. Read abstract tier only in this response. The willingness-to-pay health-economics paper is unrelated to nitrate-reductase distribution. |
| plaque-nitrate-agent-pmid-11289299 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11289299+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('11289299', 'Functional, biochemical and genetic diversity of prokaryotic nitrate reductases.', '10.1007/pl00000845')]. Read abstract tier only in this response. These are secondary review articles; no direct experimental claim is inferred from their abstract. |
| plaque-nitrate-agent-pmid-17964535 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A17964535+AND+SRC%3AMED; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('17964535', 'The prokaryotic complex iron-sulfur molybdoenzyme family.', '10.1016/j.bbamem.2007.09.002')]. Read abstract tier only in this response. These are secondary review articles; no direct experimental claim is inferred from their abstract. |
| plaque-nitrate-agent-IPR006468 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006468/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Nitrate reductase alpha subunit', 'short': 'NarG'}; members {'ncbifam': {'TIGR01580': 'nitrate reductase subunit alpha'}}. Family identity inspected, without imposing an exact isoenzyme-only grounding or interpreting homolog coverage as assembly proof. |
| plaque-nitrate-agent-IPR006547 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006547/; metadata.name/type/member_databases and source annotation flags | context_only | Native family: {'name': 'Nitrate reductase, beta subunit', 'short': 'NO3_Rdtase_bsu'}; members {'cdd': {'cd10557': 'beta subunit of nitrate reductase A (NarH) and similar proteins'}, 'ncbifam': {'TIGR01660': 'nitrate reductase subunit beta'}}. NarH/NarY family; its legacy tetramer prose conflicts with CPX1974/UniProt dimer-of-heterotrimers annotation and is not silently adopted. |
| plaque-nitrate-agent-bertero-rcsb | https://data.rcsb.org/rest/v1/core/entry/1Q16; PDB1Q16 deposition and citation metadata | context_only | Native author deposition identifies the E.coli NarGHI nitrate-reductase structure and Bertero2003 primary citation; no raw coordinates reanalyzed. |
| plaque-nitrate-agent-bertero-crossref | https://api.crossref.org/works/10.1038/nsb969; DOI/title/publication metadata | context_only | Verified Bertero DOI10.1038/nsb969 citation identity. Metadata is not full-body biological evidence. |
| plaque-nitrate-agent-bertero-publisher | https://www.nature.com/articles/nsb969; Actual HTML abstract and subscription/access markup | context_only | The HTTP200 response is abstract/metadata/subscription HTML, including the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson is a secondary review. |
| plaque-nitrate-agent-bertero-pdf | https://www.nature.com/articles/nsb969.pdf; Actual HTML abstract and subscription/access markup | context_only | The HTTP200 response is abstract/metadata/subscription HTML, including the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson is a secondary review. |
| plaque-nitrate-agent-richardson-publisher | https://link.springer.com/article/10.1007/PL00000845; Actual HTML abstract and subscription/access markup | context_only | The HTTP200 response is abstract/metadata/subscription HTML, including the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson is a secondary review. |
| plaque-nitrate-agent-rothery-elsevier | https://api.elsevier.com/content/article/doi/10.1016/j.bbamem.2007.09.002?httpAccept=text/xml; Actual XML response | context_only | HTTP200 is a metadata/entitlement stub for the Rothery review, not readable full body; abstract evidence comes from EuropePMC. |
| plaque-photosystem-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009521,GO:0098796,GO:0034357,GO:0009522,GO:0009523,GO:0009767; results: id, name, definition and native relations | context_only | Verified exact native term identities and definitions: [('GO:0098796', 'membrane protein complex'), ('GO:0034357', 'photosynthetic membrane'), ('GO:0009767', 'photosynthetic electron transport chain'), ('GO:0009523', 'photosystem II'), ('GO:0009522', 'photosystem I'), ('GO:0009521', 'photosystem')]. Preserve nitrate GO0009325 reversed-reaction conflict and distinguish photosystem generic identity from oxygenic examples. |
| plaque-photosystem-agent-jordan2001-pdf | https://dosequis.colorado.edu/Courses/InsaneMembrane/papers/PS1-PSII-LHC%27s/photosystem1.pdf; Source transport/access attempt | context_only | Actual curl HTTP 000, exit 60; 0 bytes. This attempt did not provide a usable scientific article body and supports no biological absence inference. |
| plaque-photosystem-agent-umena2011-pdf | https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/oec_2011.pdf; Genuine PDF main body pp55-59; overall structure, Mn4CaO5 ligands, cofactors and Methods | context_only | Inspected T.vulcanus PSII preparation and D1/D2 core/cofactors. D1 supplies most oxygen-evolving cluster ligands, with direct CP43 contribution. Structural proposals for proton/water channels remain proposals; no universal type-II or assembly-removal claim. |
| plaque-photosystem-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID%3A11418848%20OR%20EXT_ID%3A21499260%20OR%20EXT_ID%3A12518057%20OR%20EXT_ID%3A19433803; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('21499260', 'Crystal structure of oxygen-evolving photosystem II at a resolution of 1.9 Å.', '10.1038/nature09913'), ('19433803', 'Location of chloride and its possible functions in oxygen-evolving photosystem II revealed by X-ray crystallography.', '10.1073/pnas.0812797106'), ('12518057', 'Crystal structure of oxygen-evolving photosystem II from Thermosynechococcus vulcanus at 3.7-A resolution.', '10.1073/pnas.0135651100'), ('11418848', 'Three-dimensional structure of cyanobacterial photosystem I at 2.5 A resolution.', '10.1038/35082000')]. Read abstract tier only in this response. |
| plaque-photosystem-agent-jordan2001-publisher | https://www.nature.com/articles/35082000; Actual HTML abstract and subscription/access markup | context_only | The HTTP200 response is abstract/metadata/subscription HTML, including the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson is a secondary review. |
| plaque-photosystem-agent-P0A406 | https://rest.uniprot.org/uniprotkb/P0A406.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P0A406: UniProtKB reviewed (Swiss-Prot); taxon 32046 (Synechococcus elongatus); genes ['psaA']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-photosystem-agent-P0A408 | https://rest.uniprot.org/uniprotkb/P0A408.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P0A408: UniProtKB reviewed (Swiss-Prot); taxon 32046 (Synechococcus elongatus); genes ['psaB']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-photosystem-agent-P51765 | https://rest.uniprot.org/uniprotkb/P51765.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P51765: UniProtKB reviewed (Swiss-Prot); taxon 32053 (Thermostichus vulcanus); genes ['psbA']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-photosystem-agent-D0VWR8 | https://rest.uniprot.org/uniprotkb/D0VWR8.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | D0VWR8: UniProtKB reviewed (Swiss-Prot); taxon 32053 (Thermostichus vulcanus); genes ['psbD']. Native annotation was inspected; reviewed status does not itself prove experimental membership. |
| plaque-photosystem-agent-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 1117 as Cyanobacteriota; lineage Bacteria; Bacillati; ; historical names ['Oxygenic photosynthetic bacteria:equivalent name', 'Cyanobacteriophyta Oren, Mares &amp; Rippka, 2022:authority', 'Cyanobacteriota Oren et al. 2022:authority', '"Cyanobacteria" (ex Stanier 1974) Cavalier-Smith, 2002:authority', 'Cyanobacteriophyta:synonym', 'Cyanophyta:synonym', 'Cyanophycota:synonym', 'Oxyphotobacteria:synonym', 'cyanobacteria:genbank common name', 'cyanobacteria &lt;genbank common name&gt;:genbank common name']. |
| plaque-photosystem-agent-tax-32046 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32046; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 32046 as Synechococcus elongatus; lineage Bacteria; Bacillati; Cyanobacteriota; Cyanophyceae; Synechococcales; Synechococcaceae; Synechococcus; ; historical names ['Synechococcus elongatus Nageli 1849:authority']. |
| plaque-photosystem-agent-tax-32053 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 32053 as Thermostichus vulcanus; lineage Bacteria; Bacillati; Cyanobacteriota; Cyanophyceae; Thermostichales; Thermostichaceae; Thermostichus; ; historical names ['Synechococcus vulcanus J.J.Copeland, 1936:authority', 'Thermostichus vulcanus (J.J.Copeland, 1936) Komarek &amp; Strunecky, 2020:authority', 'Thermosynechococcus vulcanus (J.J.Copeland, 1936) Katoh et al., 2001:authority', 'Synechococcus vulcanus:synonym', 'Thermosynechococcus vulcanus:synonym']. |
| plaque-photosystem-agent-psi-unique | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29%20AND%20%28organism_id%3A32046%29%20AND%20%28gene_exact%3ApsaA%20OR%20gene_exact%3ApsaB%29&amp;format=json&amp;size=500; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('P0A408', 32046), ('P0A406', 32046)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-photosystem-agent-uniprot-unique | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&amp;format=json&amp;size=100; Bounded reviewed UniProt query at declared organism/taxonomy node | context_only | Returned accessions/taxa: [('D0VWR8', 32053), ('P51765', 32053)]. This verifies bounded query identity, not exhaustive species or family completeness. |
| plaque-photosystem-agent-pdb-1jb0 | https://data.rcsb.org/rest/v1/core/entry/1JB0; Native 1JB0 deposition identity, source organism and SIFTS chain mappings | context_only | PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field retains Synechococcus elongatus tax32046. Crystal preparation and source name cannot establish identity with PCC7942 merely by shared spelling. |
| plaque-photosystem-agent-pdb-1jb0-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1JB0/1; Native 1JB0 deposition identity, source organism and SIFTS chain mappings | context_only | PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field retains Synechococcus elongatus tax32046. SIFTS maps PsaA to P0A405 (current BP-1 tax197221), creating an important legacy-source versus current-mapping conflict. |
| plaque-photosystem-agent-pdb-1jb0-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1JB0/2; Native 1JB0 deposition identity, source organism and SIFTS chain mappings | context_only | PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field retains Synechococcus elongatus tax32046. SIFTS maps PsaB to P0A407 (current BP-1 tax197221); the record P0A408 is not the exact deposited chain mapping. |
| plaque-photosystem-agent-pdb-1jb0-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1JB0/3; Native 1JB0 deposition identity, source organism and SIFTS chain mappings | context_only | PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field retains Synechococcus elongatus tax32046. Entity3 is the separate PsaC iron-sulfur-center subunit; SIFTS maps P0A415. |
| plaque-access-kamiya2003-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140893/fullTextXML; Source transport/access attempt | context_only | Actual curl HTTP 500, exit 0; 149 bytes. This attempt did not provide a usable scientific article body and supports no biological absence inference. |
| plaque-access-kawakami2009-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2688974/fullTextXML; Source transport/access attempt | context_only | Actual curl HTTP 500, exit 0; 150 bytes. This attempt did not provide a usable scientific article body and supports no biological absence inference. |
| plaque-adapter-datasets | https://imodulondb.org/api/datasets; Complete returned organism/dataset catalogue | context_only | Catalogue contains e_coli/precise_mg1655 and s_elongatus/elprecise300. It lists no Thermosynechococcus vestitus/elongatus BP-1 or Thermostichus vulcanus dataset. Absence is limited to this retrieved catalogue, not biology. |
| plaque-adapter-meta | https://imodulondb.org/api/datasets/e_coli/precise_mg1655/meta; strains, dataset, sample/condition and publication fields | context_only | E.coli precise_mg1655 is MG1655 with 586 samples, 281 conditions and 115 components. publication_url is null. This is a bounded K-12 descendant context, not every strain or FDH/nitrate-reductase class. |
| plaque-adapter-search-fdnG | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=fdnG&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b1474', 'fdnG')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-fdnH | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=fdnH&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b1475', 'fdnH')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-fdnI | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=fdnI&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b1476', 'fdnI')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-fdoG | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=fdoG&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b3894', 'fdoG')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-fdoH | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=fdoH&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b3893', 'fdoH')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-fdoI | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=fdoI&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b3892', 'fdoI')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-narG | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=narG&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b1224', 'narG')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-narH | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=narH&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b1225', 'narH')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-search-narI | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise_mg1655&amp;query=narI&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('b1227', 'narI')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-gene-modules-fdnG | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1474/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(67, 'FDH-N_NRA', '0.123152544'), (69, 'Fnr-1', '0.093500904')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-fdnH | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1475/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(67, 'FDH-N_NRA', '0.114101792')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-fdnI | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1476/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): []. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-fdoG | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3894/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): []. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-fdoH | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3893/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): []. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-fdoI | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3892/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): []. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-narG | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1224/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(67, 'FDH-N_NRA', '0.266744246'), (69, 'Fnr-1', '0.089845386')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-narH | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1225/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(67, 'FDH-N_NRA', '0.240452882'), (21, 'N Reduction', '0.110831747')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-gene-modules-narI | https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1227/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(67, 'FDH-N_NRA', '0.220000914'), (21, 'N Reduction', '0.123743046')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-syn-meta | https://imodulondb.org/api/datasets/s_elongatus/elprecise300/meta; strains, publication_url and dataset fields | context_only | S.elongatus elprecise300 is specifically PCC7942, with 300 samples, 57 modules and DOI10.1073/pnas.2410492121. It is not the thermophilic Jordan BP-1 or Umena vulcanus preparation. |
| plaque-adapter-syn-search-psaA | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=psaA&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('Synpcc7942_2049', 'psaA')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-syn-search-psaB | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=psaB&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('Synpcc7942_2048', 'psaB')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-syn-search-psbA | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=psbA&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('Synpcc7942_0893', 'psbA3'), ('Synpcc7942_1389', 'psbA2'), ('Synpcc7942_0424', 'psbA1')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-syn-search-psbD | https://imodulondb.org/api/search?organism=s_elongatus&amp;dataset=elprecise300&amp;query=psbD&amp;limit=50; Bounded source gene/module search | context_only | Returned gene keys: [('Synpcc7942_0655', 'psbD1'), ('Synpcc7942_1637', 'psbD2')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus vulcanus examples. |
| plaque-adapter-summary-21 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/21; Native component annotation, threshold and member counts; generated narrative excluded | context_only | Module 21 (N Reduction), 26 thresholded genes, threshold 0.080605467; native annotation: electron transfer via nitrate reductases. AI-generated summary and activity-matrix inference excluded. Expression context only. |
| plaque-adapter-members-21 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/21/genes?limit=50; First 50 requested thresholded member rows | context_only | Inspected all 26 returned rows; relevant named members [('b1227', 'narI'), ('b1225', 'narH')]. No physical complex or mechanism is inferred. |
| plaque-adapter-summary-67 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/67; Native component annotation, threshold and member counts; generated narrative excluded | context_only | Module 67 (FDH-N_NRA), 11 thresholded genes, threshold 0.099373409; native annotation: anaerobic growth on nitrate; formate-to-nitrate electron transfer via formate dehydrogenase N and nitrate reductase A. AI-generated summary and activity-matrix inference excluded. Expression context only. |
| plaque-adapter-members-67 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/67/genes?limit=50; First 50 requested thresholded member rows | context_only | Inspected all 11 returned rows; relevant named members [('b1224', 'narG'), ('b1225', 'narH'), ('b1227', 'narI'), ('b1474', 'fdnG'), ('b1475', 'fdnH')]. No physical complex or mechanism is inferred. |
| plaque-adapter-summary-69 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/69; Native component annotation, threshold and member counts; generated narrative excluded | context_only | Module 69 (Fnr-1), 33 thresholded genes, threshold 0.070397694; native annotation: transition from aerobic to anaerobic growth. AI-generated summary and activity-matrix inference excluded. Expression context only. |
| plaque-adapter-members-69 | https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/69/genes?limit=50; First 50 requested thresholded member rows | context_only | Inspected all 33 returned rows; relevant named members [('b1474', 'fdnG'), ('b1224', 'narG')]. No physical complex or mechanism is inferred. |
| plaque-adapter-syn-modules-psaA | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(38, 'Photosystems', '0.076674881')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-syn-modules-psaB | https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2048/imodulons; Dataset-specific gene weights and is_in_imodulon flags | context_only | Thresholded memberships (component, name, weight): [(38, 'Photosystems', '0.089138166')]. Unselected weights are below dataset thresholds, not evidence against physical membership or biological presence. |
| plaque-adapter-syn-publication | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A10.1073%2Fpnas.2410492121; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('39269777', 'Machine learning reveals the transcriptional regulatory network and circadian dynamics of &amp;lt;i&amp;gt;Synechococcus elongatus&amp;lt;/i&amp;gt; PCC 7942.', '10.1073/pnas.2410492121')]. Read abstract tier only in this response. |
| plaque-photosystem-jordan-http | http://dosequis.colorado.edu/Courses/InsaneMembrane/papers/PS1-PSII-LHC%27s/photosystem1.pdf; Genuine PDF pp909-916, especially polypeptide subunits p911 and electron transfer p913 | context_only | Public HTTP mirror supplied the readable Jordan2001 PDF after HTTPS certificate failure. Main text and captions support PsaA/PsaB and antenna architecture; PsaC carries FA/FB, whereas FX is jointly ligated by PsaA/PsaB. Thermophilic historical source naming is kept distinct from current taxonomy. No raw diffraction or supplemental reanalysis. |
| plaque-semchonok2021-pdf | https://par.nsf.gov/servlets/purl/10308929; Author manuscript PDF, introduction p2, paragraph identifying Jordan2001 PDB1JB0 | context_only | This primary structural paper explicitly identifies the earlier 1JB0 PSI preparation as thermophilic Thermosynechococcus elongatus BP-1. This is comparative/background attribution within that paper, not a new isolation experiment on the 2001 material. |
| plaque-taxonomy-bp1 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/197221; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 197221 as Thermosynechococcus vestitus BP-1; lineage Bacteria; Bacillati; Cyanobacteriota; Cyanophyceae; Acaryochloridales; Thermosynechococcaceae; Thermosynechococcus; ; historical names ['Thermosynechococcus elongatus BP-1:equivalent name', 'Thermosynechococcus elongatus IAM M-273:equivalent name', 'Thermosynechococcus elongatus NIES-2133:equivalent name']. |
| plaque-taxonomy-pcc7942 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; taxId/scientificName/lineage/otherNames | context_only | Authority identifies 1140 as Synechococcus elongatus PCC 7942 = FACHB-805; lineage Bacteria; Bacillati; Cyanobacteriota; Cyanophyceae; Synechococcales; Synechococcaceae; Synechococcus; ; historical names ['Synechococcus sp. PCC 7942:equivalent name', 'Synechococcus elongatus PCC 7942:includes', 'Synechococcus sp. FACHB-805:includes', 'Synechococcus sp. IAM M-200:synonym', 'Synechococcus leopoliensis strain PCC 7942:synonym', 'Synechococcus leopoliensis UTEX 2434:synonym', 'Anacystis nidulans R2:synonym']. |
| plaque-adapter-syn-summary-38 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38; Native component annotation, threshold and member counts; generated narrative excluded | context_only | Module 38 (Photosystems), 44 thresholded genes, threshold 0.063088206; native annotation: Photosystems proteins. AI-generated summary and activity-matrix inference excluded. Expression context only. |
| plaque-adapter-syn-members-38 | https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38/genes?limit=50; First 50 requested thresholded member rows | context_only | Inspected all 44 returned rows; relevant named members [('Synpcc7942_2048', 'psaB'), ('Synpcc7942_2049', 'psaA')]. No physical complex or mechanism is inferred. |
| plaque-adapter-syn-primary | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11420160/fullTextXML; PMC11420160 JATS body: introduction, photosynthesis section and ICA methods | context_only | Read the actual paper body for PCC7942 scope and computational Photosystems-module provenance. ICA on 300 RNA-seq profiles identifies coexpression modules; this is not an assembly/localization experiment or a BP-1 dataset. |
| plaque-semchonok2021-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A10.1016%2Fj.xplc.2021.100248; EuropePMC exact query citation identity and abstracts; no body via this endpoint | context_only | Verified [('35059628', 'Cryo-EM structure of a tetrameric photosystem I from &lt;i&gt;Chroococcidiopsis&lt;/i&gt; TS-821, a thermophilic, unicellular, non-heterocyst-forming cyanobacterium.', '10.1016/j.xplc.2021.100248')]. Read abstract tier only in this response. |
| plaque-taxonomy-PSI-P0A405 | https://rest.uniprot.org/uniprotkb/P0A405.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P0A405: UniProtKB reviewed (Swiss-Prot); taxon 197221 (Thermosynechococcus vestitus (strain NIES-2133 / IAM M-273 / BP-1)); genes ['psaA']. Native annotation was inspected; reviewed status does not itself prove experimental membership. These are the SIFTS-linked 1JB0 chains, distinct from the record identity-only P0A406/P0A408 examples. |
| plaque-taxonomy-PSI-P0A407 | https://rest.uniprot.org/uniprotkb/P0A407.json; Reviewed entry identity, genes, organism, subunit/function/cofactor/location annotations and evidence attribution | context_only | P0A407: UniProtKB reviewed (Swiss-Prot); taxon 197221 (Thermosynechococcus vestitus (strain NIES-2133 / IAM M-273 / BP-1)); genes ['psaB']. Native annotation was inspected; reviewed status does not itself prove experimental membership. These are the SIFTS-linked 1JB0 chains, distinct from the record identity-only P0A406/P0A408 examples. |
| plaque-jormakka-browser-main | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; ResearchGate browser text lines48-980; article beginning at74, overall structure and electron-transfer sections | partial | Author-uploaded primary article text inspected for E.coli FdnGHI architecture and redox relay. This is preserved browser text, not the failed curl403 article response; HQNO/proton-pathway inference remains qualified. |
| plaque-jormakka-browser-later | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; ResearchGate browser text lines956-1518 plus beginning; ignore failed Jordan open entries | partial | Inspected gamma-subunit and quinone/proton pathway discussion; direct coordinates and figure pixels not reanalyzed. Native curl403 is retained separately and not treated as paper access. |
| plaque-jormakka-browser-beta | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; ResearchGate browser text lines524-1137; ignore separate Jordan intro response | partial | Inspected alpha/beta/gamma subunit discussion and captions. No supplementary Methods or direct proton-flux measurement audit. |
| plaque-current-0 | data/structures/energy_complex/formate_dehydrogenase_complex.yaml; Whole current maintained record | context_only | Full current record read; current SHA 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e. No scientific fields edited. |
| plaque-original-0 | reviews/structured/20261021T100134Z-formate-dehydrogenase-complex-audit/review.yaml; Original whole YAML and exact current native validation/render | context_only | Historical immutable review; target hash independently checked at its declared source revision. Findings and access tiers reassessed, not accepted merely because validation passes. |
| plaque-current-1 | data/structures/energy_complex/nitrate_reductase_complex.yaml; Whole current maintained record | context_only | Full current record read; current SHA ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459. No scientific fields edited. |
| plaque-original-1 | reviews/structured/20261021T100137Z-nitrate-reductase-complex-audit/review.yaml; Original whole YAML and exact current native validation/render | context_only | Historical immutable review; target hash independently checked at its declared source revision. Findings and access tiers reassessed, not accepted merely because validation passes. |
| plaque-current-2 | data/structures/energy_complex/photosystem.yaml; Whole current maintained record | context_only | Full current record read; current SHA c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8. No scientific fields edited. |
| plaque-original-2 | reviews/structured/20261021T100138Z-photosystem-audit/review.yaml; Original whole YAML and exact current native validation/render | context_only | Historical immutable review; target hash independently checked at its declared source revision. Findings and access tiers reassessed, not accepted merely because validation passes. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; ComponentTypeEnum, EssentialityEnum and graph representation | context_only | Grouped subcomplexes, protein instances, assembly necessity and catalytic roles remain distinct. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Scope, supported paths and evidence contract | context_only | Membership/activity summaries do not independently establish a represented causal route. |
| plaque-policy | docs/CURATION.md; Identity and source/evidence scope | context_only | Source-specific taxon, molecular role and condition must not be generalized silently; no optional-empty-field finding. |
| plaque-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks | context_only | Named genes/proteins trigger applicability assessment; lack of expression claims is not an exemption. Unavailable runner may use inspected source fallback. |
| plaque-energy-category-prior | reviews/structured/20261023T230504Z-energy-complex-category-review/review.yaml; Exact finding F1 and affected target GO0009521 | context_only | The sole affected target of F1 is this photosystem; reviewing this finding does not repeat or certify all37 category targets. |
| plaque-historical-issue2420 | https://github.com/CultureBotAI/CellStructureMech/issues/2420; Root-retrieved CLOSED issue body and resolution comment, independently reread | context_only | Already closed grouped issue includes the photosystem core-type finding. Resolution comment cites99e590eb7afb0e8251f6e81183e59ca1119987b9. This PR does not claim that prior record correction as new work or resolve other grouped targets. |
| plaque-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-plaque/original-validation.json; Actual native validate/render receipts and historical/current hashes for three assigned originals | supports | All three validate commands exit0, all native Markdown renders match exactly, all historical target SHA256s match declared input; formate/nitrate current bytes unchanged and photosystem stale delta independently assessed. |
| plaque-native-formate_dehydrogenase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/formate_dehydrogenase_complex-uniprot-verify-receipt.json; Actual root-run native command; independently inspected receipt and complete stdout | supports | Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/formate_dehydrogenase_complex.yaml', '--verify'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. Identity/xref coverage does not prove scientific mechanism. |
| plaque-native-formate_dehydrogenase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/formate_dehydrogenase_complex-uniprot-causal-receipt.json; Actual root-run native command; independently inspected receipt and complete stdout | supports | Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/formate_dehydrogenase_complex.yaml', '--causal-graphs'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA 0d1606e67e7adec4d9a42a5ba7bc7c8f70ecf7a91349686b0cb351992185d8f7. Identity/xref coverage does not prove scientific mechanism. |
| plaque-native-nitrate_reductase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/nitrate_reductase_complex-uniprot-verify-receipt.json; Actual root-run native command; independently inspected receipt and complete stdout | supports | Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/nitrate_reductase_complex.yaml', '--verify'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. Identity/xref coverage does not prove scientific mechanism. |
| plaque-native-nitrate_reductase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/nitrate_reductase_complex-uniprot-causal-receipt.json; Actual root-run native command; independently inspected receipt and complete stdout | supports | Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/nitrate_reductase_complex.yaml', '--causal-graphs'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA af74368d55b6de50d4008ce1b5142d396e34df4b1cfb8605bbac6ab3494ea707. Identity/xref coverage does not prove scientific mechanism. |
| plaque-native-photosystem-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/photosystem-uniprot-verify-receipt.json; Actual root-run native command; independently inspected receipt and complete stdout | supports | Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/photosystem.yaml', '--verify'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. Identity/xref coverage does not prove scientific mechanism. |
| plaque-native-photosystem-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/photosystem-uniprot-causal-receipt.json; Actual root-run native command; independently inspected receipt and complete stdout | supports | Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/photosystem.yaml', '--causal-graphs'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA 53824867a2aae786f4735345cb9c129de0b95944ab99f592d60014a87fcd2a37. Identity/xref coverage does not prove scientific mechanism. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0005774,GO:0005775,GO:0007035,GO:0016469,GO:0016471,GO:0033176,GO:0033177,GO:0033178,GO:0033179,GO:0033180,GO:0046961,GO:0090533,GO:1904949; QuickGO exact fifteen requested GO term objects: definitions, labels and returned parent/child relationships; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/go.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/go.receipt.json | supports | The exact generic complex/sector identities and their parent and part relationships resolve. GO:0033176 includes organelle and plasma-membrane V-ATPases; GO:0000220/0000221 are vacuolar sectors. Generic V0 GO:0033179 describes six or more c subunits, not an invariant decamer. Generic V1 GO:0033180 gives A3B3, D/F and C/E/G/H, without the added three-stalk detail. Function/compartment labels also resolve; this is ontology authority, not experimental confirmation of every appended statement. |
| micro-kane2006-secondary | https://pmc.ncbi.nlm.nih.gov/articles/PMC1393255/?pdf=render; Kane 2006, Introduction/Structure HTML paragraphs P7-P29, assembly/targeting/regulation P43-P64; paragraph offsets are zero-based in the retained derived text; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/kane2006.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/kane2006.receipt.json | context_only | Secondary review sections were read. They distinguish S. cerevisiae Vph1 vacuolar and Stv1 Golgi/endosomal isoforms, V1 and V0 subunits, central rotor/c-ring versus stationary elements, and activity/assembly/targeting phenotypes. Its Figure 1 caption retains older one/two-peripheral-stalk models; it is not a source for the later three-stalk result. Assembly routes and subunit-e placement retain uncertainty. Figure captions were read, not image pixels. Prose summaries are context, not a fresh primary experiment. |
| micro-zhao2015-abstract | https://www.nature.com/articles/nature14365; Zhao et al. 2015 Nature, DOI:10.1038/nature14365; accessible abstract HTML P7, subscription notice P8 and deposition-accession listing P20; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/zhao2015.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/zhao2015.receipt.json | partial | Fresh native publisher response exposes the abstract and gates the main text. The abstract explicitly states S. cerevisiae cryo-EM three rotational states, ten proteolipids in its c-ring, three peripheral stalks in eukaryotic V-ATPase, and central rotor versus stalks that prevent rotation of the membrane region. These results support the numerical/taxon and rotor/stator findings. No current main-text, Methods, figure-pixel, strain/preparation, detergent, nucleotide-condition or subunit-e-loss verification is claimed. |
| micro-li2009-secondary | https://pmc-oa-opendata.s3.amazonaws.com/PMC2906225.1/PMC2906225.1.xml; Li and Kane 2009, JATS sections S15-S18 / body paragraphs P27-P34 (V-ATPase and vacuolar pH regulation); response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/li2009.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/li2009.receipt.json | context_only | Read secondary context distinguishes V1 ATP hydrolysis and V0 proton transport, 14 yeast subunits, yeast Vph1/Stv1 compartment specificity, and vacuolar-pH regulation. Loss-of-activity or acidification phenotypes do not alone establish assembly necessity. Detached V1/V0 inhibition and counterion/exchanger/buffering contributions are not universal structure-inventory claims. |
| micro-forgac2007-summary | https://www.nature.com/articles/nrm2272; Forgac 2007 DOI:10.1038/nrm2272; accessible Key Points P8-P12 and abstract P13; subscription notice P14; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/forgac2007.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/forgac2007.receipt.json | context_only | Secondary Key Points and abstract only: ATP-driven V1 rotor and V0 proton transport, ER assembly/chaperone and targeting context, reversible dissociation, and organelle/plasma-membrane functions. Main text is gated; no fresh full-review-body audit claimed. |
| micro-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA taxonomy tax-id/4932 result: taxId, scientificName, rank; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/tax-4932.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/tax-4932.receipt.json | supports | NCBITaxon:4932 resolves to Saccharomyces cerevisiae at species rank. This validates the taxon, not strain, occurrence frequency, or universal molecular composition. |
| micro-literature-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=DOI%3A%2210.1128%2FMMBR.70.1.177-191.2006%22+OR+DOI%3A%2210.1038%2Fnature14365%22+OR+DOI%3A%2210.1016%2Fj.bbamcr.2008.08.003%22+OR+DOI%3A%2210.1038%2Fnrm2272%22; Europe PMC core records matching four exact DOIs; pageSize=100; title/authors/publication identifiers and abstracts only; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/metadata.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/metadata.receipt.json | context_only | The four cited DOIs match Kane 2006 (PMID:16524922), Zhao 2015 (PMID:25971514), Li/Kane 2009 (PMID:18786576) and Forgac 2007 (PMID:17912264). Metadata corroborates bibliographic identity, not unseen full text. |
| micro-named-yeast-genes | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A4932%29+AND+%28gene_exact%3AVPH1+OR+gene_exact%3ASTV1+OR+gene_exact%3AVMA3+OR+gene_exact%3AVMA11+OR+gene_exact%3AVMA16+OR+gene_exact%3AVMA6+OR+gene_exact%3AVMA9+OR+gene_exact%3AVMA1+OR+gene_exact%3AVMA2+OR+gene_exact%3AVMA8+OR+gene_exact%3AVMA7+OR+gene_exact%3AVMA4+OR+gene_exact%3AVMA10+OR+gene_exact%3AVMA5+OR+gene_exact%3AVMA13%29&amp;format=json&amp;size=500; UniProt reviewed result primary gene names, recommended protein names, accessions and organism IDs; 15 results, no next-page Link; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/genes/named-yeast-genes.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/genes/named-yeast-genes.receipt.json | supports | All fifteen queried yeast gene tokens have reviewed S. cerevisiae S288C (taxon 559292 within 4932) records: VPH1/P32563 and STV1/P37296 (a isoforms); VMA3/P25515, VMA11/P32842, VMA16/P23968 (c/c-prime/c-double-prime); VMA6/P32366 (d), VMA9/Q3E7B6 (e); VMA1/P17255 (A), VMA2/P16140 (B), VMA8/P32610 (D), VMA7/P39111 (F), VMA4/P22203 (E), VMA10/P48836 (G), VMA5/P31412 (C), VMA13/P41807 (H). This confirms the named yeast mappings, not a complete universal inventory, protist gene nomenclature, physical necessity or unasserted record accessions. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; iModulonDB /api/datasets complete returned JSON mapping: 20 organism keys and 28 dataset keys; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/datasets.raw / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/datasets.receipt.json | partial | Fresh returned catalogue has bacterial/archaeal datasets but no named Saccharomyces or other eukaryotic organism. The named yeast/fungal molecular examples have no covered organism/dataset match. The complex record also mentions unspecified bacterial V/A relatives; that wording supplies no particular matched organism/gene for a justified downstream module query. Unrelated bacterial F-type ATPase hits would not resolve that ambiguity. No universal absence of ATPase expression evidence is inferred. |
| micro-historical-adapter-runner | Retained earlier kg-microbe-sources imodulondb datasets invocation; /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json | context_only | Historical runner attempt at 2026-11-03T00:49:00.848907+00:00 through 00:49:00.863225+00:00 failed with OS PermissionError reading pyvenv.cfg (actual exit 1). It is retained unavailable-runner context, not a current execution or successful adapter run. The current direct source catalogue was inspected separately. |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks, lines 89-122; current frozen bytes and conf/record_review.yaml route | supports | Native policy triggers applicability for named genes/proteins/pathways and permits inspected source-page fallback if the runner is unavailable. Lack of an expression claim alone is not an exemption. These policy bytes were retained from earlier reads and their equality/current frozen hashes rechecked; the applicability section was reread for this report. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Native graph contract and add-cell-structure/review-checklist schema context | supports | Graph scope must reflect represented directed causal explanation. Membership and whole-structure activity do not by themselves represent hydrolysis-to-rotor coupling; identity, substructure membership, necessity and mechanistic activity remain distinct. Current frozen graph policy/schema were inspected, including retained byte-identical context. |
| micro-original-roundtrip | scripts/record_review.py validate; render --content; git show and SHA-256 input comparison; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/original-validation-inputs.json | supports | All three original YAML reviews validate and render byte-identically to their committed Markdown. Each original target hash matches its historical source revision, current main and reviewed head. No target is stale in this slice. This is local schema/render/input verification, not scientific validation by command. |
| micro-record-proton_transporting_v_type_atpase_complex | data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml; Whole current YAML record at d7ee610a5d142b5961a6057e22437aabb68f191f | supports | Entire current record inspected, including definition, hierarchy, functions, taxon/canonical-organism scope, references, graph nodes/edges and curation history. Target unchanged relative to original frozen input and current main. |
| micro-prior-proton_transporting_v_type_atpase_complex | reviews/structured/20261021T100139Z-proton-transporting-v-type-atpase-complex-audit/review.yaml; Whole immutable original YAML/Markdown, exact F1/F2, checks/limitations and frozen inputs | context_only | Original needs_curation verdict and two distinct findings remain relevant to this unchanged target. Earlier literature access claims are historical observations, not substituted for fresh source access. Original has an explicit expression-module not_applicable check; its rationale uses absence of needed transcriptomic inference rather than matched-dataset applicability. |
| micro-native-proton_transporting_v_type_atpase_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-verify-receipt.json | partial | Native --verify returned zero, but the maintained record has no protein_examples and no protein xrefs in GENE_OR_PROTEIN nodes; the empty inventory does not validate prose yeast gene names. |
| micro-native-proton_transporting_v_type_atpase_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-causal-receipt.json | partial | Native --causal-graphs returned zero with zero GENE_OR_PROTEIN nodes (all grounding counts zero). This is an empty protein-node diagnostic; it does not validate the biological graph mechanism or its whole-structure/component nodes. |
| micro-record-proton_transporting_v_type_atpase_v0_domain | data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml; Whole current YAML record at d7ee610a5d142b5961a6057e22437aabb68f191f | supports | Entire current record inspected, including definition, hierarchy, functions, taxon/canonical-organism scope, references, graph nodes/edges and curation history. Target unchanged relative to original frozen input and current main. |
| micro-prior-proton_transporting_v_type_atpase_v0_domain | reviews/structured/20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml; Whole immutable original YAML/Markdown, exact F1/F2, checks/limitations and frozen inputs | context_only | Original needs_curation verdict and two distinct findings remain relevant to this unchanged target. Earlier literature access claims are historical observations, not substituted for fresh source access. Original has an explicit expression-module not_applicable check; its rationale uses absence of needed transcriptomic inference rather than matched-dataset applicability. |
| micro-native-proton_transporting_v_type_atpase_v0_domain-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-verify-receipt.json | partial | Native --verify returned zero, but the maintained record has no protein_examples and no protein xrefs in GENE_OR_PROTEIN nodes; the empty inventory does not validate prose yeast gene names. |
| micro-native-proton_transporting_v_type_atpase_v0_domain-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-causal-receipt.json | partial | Native --causal-graphs returned zero with zero GENE_OR_PROTEIN nodes (all grounding counts zero). This is an empty protein-node diagnostic; it does not validate the biological graph mechanism or its whole-structure/component nodes. |
| micro-record-proton_transporting_v_type_atpase_v1_domain | data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml; Whole current YAML record at d7ee610a5d142b5961a6057e22437aabb68f191f | supports | Entire current record inspected, including definition, hierarchy, functions, taxon/canonical-organism scope, references, graph nodes/edges and curation history. Target unchanged relative to original frozen input and current main. |
| micro-prior-proton_transporting_v_type_atpase_v1_domain | reviews/structured/20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml; Whole immutable original YAML/Markdown, exact F1/F2, checks/limitations and frozen inputs | context_only | Original needs_curation verdict and two distinct findings remain relevant to this unchanged target. Earlier literature access claims are historical observations, not substituted for fresh source access. Original has an explicit expression-module not_applicable check; its rationale uses absence of needed transcriptomic inference rather than matched-dataset applicability. |
| micro-native-proton_transporting_v_type_atpase_v1_domain-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-verify-receipt.json | partial | Native --verify returned zero, but the maintained record has no protein_examples and no protein xrefs in GENE_OR_PROTEIN nodes; the empty inventory does not validate prose yeast gene names. |
| micro-native-proton_transporting_v_type_atpase_v1_domain-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-causal-receipt.json | partial | Native --causal-graphs returned zero with zero GENE_OR_PROTEIN nodes (all grounding counts zero). This is an empty protein-node diagnostic; it does not validate the biological graph mechanism or its whole-structure/component nodes. |
| septin-septum-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000935,GO:0030428,GO:0032153,GO:0110165; Definitions and synonyms of all four returned terms; GO0110165 child GO0030428; GO0030428 child GO0000935; GO0032153 part_of child GO0000935 | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-septum-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-septum-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-septum-agent-tax-1423 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1423; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-septum-agent-chebi-8005 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/8005/; Complete released three-star entry, name, definition, synonyms and ontology relations | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-septum-agent-doi-10.1111_j.1749-6632.2012.06818.x | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1111/j.1749-6632.2012.06818.x%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-septum-agent-doi-10.1146_annurev-biophys-121219-081703 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1146/annurev-biophys-121219-081703%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-septum-agent-jats-PMC8610174 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8610174.1/PMC8610174.1.xml; Fresh native secondary-review JATS, sections S1 Introduction, S2 Overview, S16 Scaffold, S17 Coordinator, S22 Cell Pole Shape Determinant and S23 Conclusions. | supports | Bacterial septal peptidoglycan and FtsZ-divisome context are supported. This secondary review does not source the maintained archaeal/fungal expansion, and its cited primary experiments were not independently audited. |
| septin-bud-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005886,GO:0005933,GO:0016020,GO:0033101; All four term definitions and relevant GO0033101 child relations under GO0005933/GO0005886 | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-bud-membrane-agent-SL-0028 | https://rest.uniprot.org/locations/SL-0028.json; Complete location name, definition, synonyms, cross-references and hierarchy | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-bud-membrane-agent-SL-0027 | https://rest.uniprot.org/locations/SL-0027.json; Complete location name, definition, synonyms, cross-references and hierarchy | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-bud-membrane-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-bud-membrane-agent-doi-10.1083_jcb.135.3.725 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083/jcb.135.3.725%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-bud-membrane-agent-doi-10.1016_S0092-8674_00_80948-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/S0092-8674%2800%2980948-4%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-bud-membrane-agent-valtz1996-pdf | https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf; Fresh genuine primary PDF: abstract, Introduction, Budding Pattern Assays and Immunofluorescence Methods, antibody specificity/Pea2p expression/localization Results pp731–732, and complex Discussion p739. | supports | S. cerevisiae Pea2/Spa2 localization and interdependence are studied; complex formation is a proposed interpretation, not direct physical colocalization in this paper. This is not an inventory of lipid-boundary constituents. |
| septin-coccolith-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110165; Native GO0110165 name and complete definition | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccolith-agent-chebi-46719 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/46719/; Released entry name, chemical data and ontology relations; no textual definition is supplied | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccolith-agent-tax-127549 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccolith-agent-tax-2903 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccolith-agent-doi-10.1021_jacs.6c02151 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1021/jacs.6c02151%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-coccolith-agent-doi-10.1093_pnasnexus_pgag104 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093/pnasnexus/pgag104%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-coccolith-agent-doi-10.1126_sciadv.adc8728 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1126/sciadv.adc8728%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-coccolith-agent-jats-PMC13067266 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml; Fresh native primary JATS: Introduction, complete Results, Figures1–5 captions, Discussion, Conclusions, author metadata and exact permissions. | supports | C. leptoporus mature scales and vesicle boundaries are distinct. SEM/AFM morphology and unresolved luminal particles support the record limits, without identifying a full ATPase or universal morphogenesis mechanism. |
| septin-coccolith-agent-avrahami2026-supp | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf; Fresh genuine supplementary PDF: Materials/Methods Cell cultures, Coccolith isolation for ex situ imaging, SEM, correlative AFM/SEM, and adjacent freeze-fracture/cryofixation context, first five PDF pages. | supports | RCC1130 and isolated/cleaned SEM/AFM preparation are explicit. These Figure1 samples are not native cryotomographic specimens. Downstream tomography processing and all supplementary figures were not audited. |
| septin-coccolith-agent-jats-PMC13089448 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13089448.1/PMC13089448.1.xml; Fresh native primary JATS: Introduction, Results, Figures1/3/5 captions, Discussion and Conclusion. | supports | Calyptrosphaera holococcoliths contain calcite rhombohedra and an organic base plate; the study does not establish universal base-plate nucleation and cannot exclude sufficiently small undetected nucleators. Methods supplement and raw data not audited. |
| septin-coccolith-agent-jats-PMC9858585 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9858585.1/PMC9858585.1.xml; Fresh native primary JATS: Introduction as prior context; Results Xenospheres, Free coccoliths, Adsorption mediated by organic matter and Multifaceted ecological roles; Figures1–3/6 captions; Methods Culture, Coccolith isolation/treatment, Exogenous additions and SEM. | supports | Calcified CCMP374 donor versus naked recipient, mixed-origin adsorption and oxidation response are supported. Organic removal reduces attachment without identifying a particular adhesion molecule. Detailed virus-encounter models, supplementary videos and raw data were not reanalysed. |
| septin-coccolith-agent-package-PMC13067266 | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC13067266.1.json; Complete article/package identity, license_code and matching media_urls entry | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccosphere-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030312; Complete term definition, comment and child-relation scope | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccosphere-agent-tax-221442 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/221442; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccosphere-agent-doi-10.7717_peerj.4608 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.7717/peerj.4608%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-coccosphere-agent-doi-10.1111_nph.15272 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1111/nph.15272%22; Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication type, DOI and available abstract only. | supports | Exact article identity verified. Abstract/metadata access does not imply current full-body inspection; direct primary or secondary body access is recorded separately. |
| septin-coccosphere-agent-jats-PMC5896503 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5896503.1/PMC5896503.1.xml; Fresh native primary JATS: Materials/Methods; Results one-layer definition, neighboring-coccolith geometry, daily-size and assembly passages; Figure2 caption; Conclusion; exact article permissions. | supports | CS-369 pooled growth conditions and doubling visible plates under uniform-distribution assumption remain explicit. Red figure labels count neighboring plates. The geometric model was not independently recalculated or promoted across species. |
| septin-coccosphere-agent-jats-PMC6175242 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6175242.1/PMC6175242.1.xml; Fresh native primary JATS: nph15272-sec-0003 through0014 relevant culture/perturbation/time-lapse/fluorescence/SEM/immunofluorescence Methods; sec0019–0023 Results/Discussion; Figures6/8/9 captions. | supports | PLY182g external lectin-positive layer is not one identified polymer. Ge/HEDP impair daughter separation after initial cytokinesis; low calcium differs. Intracellular tubulin is excluded from covering composition. No movie, Figure5–9 pixel or raw-data reanalysis. |
| septin-coccosphere-agent-package-PMC5896503 | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC5896503.1.json; Complete article/package identity, license_code and matching media_urls entry | supports | Exact authority identifier and returned annotations inspected within their scope; authority identity is not independent experimental evidence. |
| septin-coccolith-image-source | https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_0001.jpg; Fresh exact native PMC media bytes, SHA256 and corresponding metadata media MD5; local frozen image pixels independently viewed. | supports | Source media byte identity agrees with the frozen local image, record checksum and native package metadata. |
| septin-coccosphere-image-source | https://pmc-oa-opendata.s3.amazonaws.com/PMC5896503.1/peerj-06-4608-g002.jpg; Fresh exact native PMC media bytes, SHA256 and corresponding metadata media MD5; local frozen image pixels independently viewed. | supports | Source media byte identity agrees with the frozen local image, record checksum and native package metadata. |
| septin-current-adapter-catalogue | https://imodulondb.org/api/datasets; Entire fresh official /api/datasets response: all organism objects and dataset keys inspected. | supports | Catalogue matches E. coli and B. subtilis; it has no S. cerevisiae or named haptophyte dataset. Coverage is bounded to the returned catalogue, with no biological-absence inference. |
| septin-egan-access-access | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1749-6632.2012.06818.x; Actual fresh direct HTTP attempt at 2026-11-03T06:48:43.178263Z | context_only | &lt;HTTPError 403: 'Forbidden'&gt;; no native body inspection or successful retrieval claimed. Bibliographic/abstract or independently accessed indexed text supplies bounded fallback. |
| septin-bud-membrane-agent-finger-body-access | https://www.researchgate.net/publication/13739580_Sec3p_Is_a_Spatial_Landmark_for_Polarized_Secretion_in_Budding_Yeast; Actual fresh direct HTTP attempt at 2026-11-03T06:48:44.343669Z | context_only | &lt;HTTPError 403: 'Forbidden'&gt;; no native body inspection or successful retrieval claimed. Bibliographic/abstract or independently accessed indexed text supplies bounded fallback. |
| septin-bud-membrane-agent-finger-body | https://www.researchgate.net/publication/13739580_Sec3p_Is_a_Spatial_Landmark_for_Polarized_Secretion_in_Budding_Yeast; Browser-indexed primary author-uploaded text with declared crawl age three weeks: Introduction and Results localization in living cells, Figure1/2 captions and Sec3-GFP membrane-association passage; displayed lines124–388. | supports | Tagged yeast Sec3 occupies stage-dependent polarized sites. Membrane-growth interpretation uses source background plus measured site organization; no direct membrane-growth-rate measurement or exhaustive component inventory is asserted. |
| septin-bud-membrane-agent-finger-methods | https://www.researchgate.net/publication/13739580_Sec3p_Is_a_Spatial_Landmark_for_Polarized_Secretion_in_Budding_Yeast; Browser-indexed primary author-uploaded text: Experimental Procedures/fixation/indirect immunofluorescence and Microscopy passages, displayed lines1134–1336. No direct HTTP success attested. | supports | Tag function, fixation, optical sections and counting criteria constrain localization interpretations; whole article, all mutant comparisons and raw images were not audited. |
| septin-current-local-ids | rg --no-ignore --hidden -n ^identifier: cellstructuremech:(coccolith&#124;coccosphere)$ data/structures; Exact anchored top-level identifiers across data/structures, including ignored and hidden files. | supports | One matching maintained definition each for coccolith and coccosphere. No external exact-equivalence or GO-wide absence claim follows. |
| septin-record-cell_septum | data/structures/envelope/cell_septum.yaml; Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all definitions, fields, discussions, examples, images and graph edges. | supports | Current target hash equals original frozen input. Whole-record independent reassessment performed without changing records. |
| septin-record-cellular_bud_membrane | data/structures/envelope/cellular_bud_membrane.yaml; Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all definitions, fields, discussions, examples, images and graph edges. | supports | Current target hash equals original frozen input. Whole-record independent reassessment performed without changing records. |
| septin-record-coccolith | data/structures/envelope/coccolith.yaml; Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all definitions, fields, discussions, examples, images and graph edges. | supports | Current target hash equals original frozen input. Whole-record independent reassessment performed without changing records. |
| septin-record-coccosphere | data/structures/envelope/coccosphere.yaml; Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all definitions, fields, discussions, examples, images and graph edges. | supports | Current target hash equals original frozen input. Whole-record independent reassessment performed without changing records. |
| septin-coccolith-agent-image | data/images/envelope/coccolith/pmc13067266_fig1.jpg; Full frozen local image actually inspected with view_image, then compared to fresh native source bytes, figure caption, methods and exact JATS permissions. | supports | Figure1 A–F shows SEM cell/scales, a schematic and AFM height maps/projections. Mixed modalities and ex situ preparation are accurately described. CC BY4.0, listed authors and source-specific attribution verified. |
| septin-coccosphere-agent-image | data/images/envelope/coccosphere/pmc5896503_fig_2.jpg; Full frozen local image actually inspected with view_image, then compared to fresh native source bytes, figure caption, methods and exact JATS permissions. | supports | Figure2 A–F shows six SEM coverings, white bars and red neighboring-plate annotations. Native caption specifies 1 micrometre bars; counts do not mean every sphere has that many total scales. Exact CC BY4.0 and attribution verified. |
| septin-policy | docs/CURATION.md; Current frozen relevant policy passages. | supports | Evidence scope and structural identity remain distinct from specific mechanism and experimental necessity. |
| septin-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; Current frozen relevant policy passages. | supports | Named gene/protein or pathway claims trigger applicability. Unavailable runner permits inspected official source fallback; no covered organism means downstream non-applicability. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Current frozen relevant policy passages. | supports | Graph scope and directed edges must match source-supported causal explanation. |
| septin-graph-contract | .claude/skills/add-cell-structure/SKILL.md; Current frozen relevant policy passages. | supports | Mechanistic paths must represent source-backed structure, role and causal transitions; useful topology is distinct. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-septin/original-checks.json; Four original native validate/render runs and original/current frozen target hashes. | supports | All four validate and render exit0; Markdown exactly matches native rendering; all four target hashes unchanged. Historical corpus gates are not current CI. |
| septin-native-cell_septum-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cell_septum-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/cell_septum.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-cell_septum-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cell_septum-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/cell_septum.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-cellular_bud_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cellular_bud_membrane-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/cellular_bud_membrane.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-cellular_bud_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cellular_bud_membrane-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/cellular_bud_membrane.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-coccolith-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccolith-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/coccolith.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-coccolith-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccolith-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/coccolith.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-coccosphere-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccosphere-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/coccosphere.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-native-coccosphere-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccosphere-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/envelope/coccosphere.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f; receipt and log independently read and hash verified. | supports | Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved molecules. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical canary attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z, exit1 PermissionError reading pyvenv.cfg; no fresh invocation. | context_only | Historical OS unavailability is separated from current official API fallback. No current runner availability test or runner success claimed. |
| septin-adapter-e_coli-precise1k-ftsZ-search | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=ftsZ&amp;limit=50; Entire bounded native search response; exact FtsZ gene-name matches separated from incidental product-text matches. | context_only | E. coli precise1k returns exact ftsZ b0095 plus incidental kilR product match; B. subtilis modulome returns ftsZ BSU_15290. Only exact FtsZ matches followed. |
| septin-adapter-b_subtilis-modulome-ftsZ-search | https://imodulondb.org/api/search?organism=b_subtilis&amp;dataset=modulome&amp;query=ftsZ&amp;limit=50; Entire bounded native search response; exact FtsZ gene-name matches separated from incidental product-text matches. | context_only | E. coli precise1k returns exact ftsZ b0095 plus incidental kilR product match; B. subtilis modulome returns ftsZ BSU_15290. Only exact FtsZ matches followed. |
| septin-adapter-e_coli-precise1k-b0095 | https://imodulondb.org/api/genes/e_coli/precise1k/b0095; Exact gene entry: gene_id/name/product, organism-dataset context and imported UniProt annotation. | context_only | FtsZ identity verified within matched dataset. E. coli b0095 corresponds to imported P0A9A6; B. subtilis BSU_15290 to P17865. Imported annotations are not direct experimental evidence or whole-species coverage. |
| septin-adapter-e_coli-precise1k-b0095-imodulons | https://imodulondb.org/api/genes/e_coli/precise1k/b0095/imodulons; Entire returned gene-module membership list, including thresholds and is_in_imodulon flags. | context_only | All 201 returned component rows have is_in_imodulon=false. This thresholded membership output is not absence of gene expression, septal participation or biological function. No positive module hit informs this verdict. |
| septin-adapter-b_subtilis-modulome-BSU_15290 | https://imodulondb.org/api/genes/b_subtilis/modulome/BSU_15290; Exact gene entry: gene_id/name/product, organism-dataset context and imported UniProt annotation. | context_only | FtsZ identity verified within matched dataset. E. coli b0095 corresponds to imported P0A9A6; B. subtilis BSU_15290 to P17865. Imported annotations are not direct experimental evidence or whole-species coverage. |
| septin-adapter-b_subtilis-modulome-BSU_15290-imodulons | https://imodulondb.org/api/genes/b_subtilis/modulome/BSU_15290/imodulons; Entire returned gene-module membership list, including thresholds and is_in_imodulon flags. | context_only | All 72 returned component rows have is_in_imodulon=false. This thresholded membership output is not absence of gene expression, septal participation or biological function. No positive module hit informs this verdict. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2354 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Jormakka2002 is inspected at preserved browser-rendered author-uploaded main-text/caption tier. Native curl returned403; no supplementary Methods, raw diffraction, figure-pixel or proton-flux audit. Structure/HQNO-based proton-pathway proposals remain qualified.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Jordan2001 main text/captions were read from a genuine HTTP PDF after an HTTPS certificate failure; browser opens also partially failed and remain access receipts. Umena2011 was read as genuine HTTPS PDF main text/captions/Methods. No raw coordinates, supplementary data or image pixels were reanalyzed.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Bertero2003 remains primary abstract plus author-deposition/native-curation tier; both publisher and nominal PDF URLs returned subscription HTML. Richardson2001/Rothery2008 are secondary-review abstracts; Rothery HTTP200 XML was entitlement/metadata, not full body.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Kamiya2003/Kawakami2009 were verified at exact metadata/abstract and UniProt location-citation attribution tiers; attempted JATS responses500 do not prove global unreadability or biological error.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: No full domain-frequency census or component-removal assembly experiment was audited. Conditional/essential assembly-necessity values remain unverified where the cited intact structures do not establish them; no issue is manufactured from an optional empty field.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Bounded family comparisons and exact-node queries are not exhaustive. Generated InterPro descriptions marked llm:true and generated iModulon summaries are excluded from biological evidence.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Fresh iModulonDB source fallback covers MG1655 and bounded PCC7942 context only. The historical unavailable runner was not rerun. Thresholded nonmembership does not establish biological absence; module membership does not establish assembly, location or mechanism. The catalogue does not list a matching BP-1/vulcanus dataset.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: RCSB1JB0 retains legacy source tax32046 while current SIFTS proteins and primary comparative literature identify BP-1. This conflict is preserved as a canonical-example finding. PCC7942 context and identity-only P0A406/P0A408 annotations do not resolve the historical preparation identity.
- Formate dehydrogenase, nitrate reductase and photosystem independent subreview: Only the photosystem target of Oct23 category F1 is dispositioned; no whole-category or all-target#2420 resolution is claimed. Record correction was already present on main. Root owns current global QC/CI and scientific issue filing.
- Three generic V-type ATPase records independent subreview: Zhao2015 current publisher HTML is abstract/deposition-list only and subscription-gates main text. A browser attempt encountered Nature identity redirect failure. No current primary Methods, figure pixels, raw maps/coordinates, JTY002, detergent/nucleotide conditions or subunit-e-loss verification is claimed. Earlier original source access remains explicitly historical.
- Three generic V-type ATPase records independent subreview: Kane2006 is secondary: inspected Introduction/Structure and stated assembly/targeting sections; Figure1/2 captions were read without image-pixel review. Li/Kane2009 inspection covers JATS S15-S18/P27-P34. Forgac2007 is secondary Key Points/abstract only. Bibliographic metadata does not replace unseen full text.
- Three generic V-type ATPase records independent subreview: Native six UniProt commands passed on empty maintained protein_examples and zero GENE_OR_PROTEIN nodes. The separate bounded fifteen-name yeast UniProt query verifies those mappings only, not full family coverage, assembly necessity or protist gene names.
- Three generic V-type ATPase records independent subreview: Historical adapter runner unavailable receipt is reused with its actual 00:49Z time and exit1. Fresh direct catalogue has no yeast/eukaryotic match; unspecified bacterial V/A prose does not identify a matched species/gene. No unrelated bacterial F-type module evidence or universal absence inference is substituted.
- Three generic V-type ATPase records independent subreview: No independent frequency study, universal composition/assembly model, acidocalcisome-specific source, or population-level occurrence estimate was added. These limitations are distinguished from the six confirmed original findings.
- Three generic V-type ATPase records independent subreview: All three targets are unchanged and original frozen hashes/renderings validate. Original six findings retain exact predecessor occurrences; no category-wide or earlier vacuolar-record finding is resolved by this generic-record slice.
- Three generic V-type ATPase records independent subreview: Common policy/config/schema/verifier context was retained from prior reads, checked byte-identical to this frozen source, with applicable adapter/graph sections reread. The three current targets, six original YAML/Markdown files and source responses were inspected independently. No tracked image or energy-category review was used by this slice.
- Three generic V-type ATPase records independent subreview: Root owns full QC, final CI, issue deduplication/publication and immutable successor synthesis. This report does not claim their pending or external results.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Independent read-only reassessment of four unchanged targets. Historical bundles and receipts remain immutable; current checks and source accesses are separately dated. No record or GitHub mutation by reviewer.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Egan full text remains unavailable after an actual fresh Wiley pdfdirect HTTP403; exact Europe PMC metadata/abstract only. 2012 electronic publication versus 2013 issue year is not a separate identity defect. McQuillen is secondary review evidence at named body sections; underlying primary experiments were not independently audited.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: No exhaustive archaeal/fungal septation literature survey or direct assembly-removal experiment was performed. The definition finding concerns unsupported maintained scope, not proof that every appended statement is false.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Valtz genuine PDF was read at specified methods, localization and complex-interpretation passages, not every mating assay, strain-table row or image. Finger primary author-uploaded indexed body/methods were freshly accessed through browser with declared three-week crawl age while direct HTTP returned403. No direct full-text success or entire-paper audit claimed.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: The bud lipid bilayer is a collective defining material, not one measured lipid species; ESSENTIAL here does not assert an individual lipid knockout endpoint. Localization of associated machinery is not proof of complete membrane composition.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Both frozen local images were actually viewed and match fresh native PMC media bytes, metadata MD5, record SHA256, figure captions and exact CC BY4.0 permissions. Only these two images received pixel inspection. Other source figures are text/caption scopes.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Avrahami main text and culture/isolation/SEM/AFM supplement sections were read; downstream tomography processing and raw volumes were not reanalysed. Ben-Joseph holococcolith supplementary Methods were not audited. Johns detailed virus-encounter modelling and supplementary videos were not independently audited.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Walker claim-bearing Methods/Results/Discussion and Figure6/8/9 captions were read; movies, source image pixels and raw datasets were not reanalysed. Xu mathematical simulations and workbook were not recalculated. Morphology/counting assumptions and treatment-specific cell-separation endpoints are retained.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Historical ontology searches and exact current GO-wide absence were not reconstructed. Current repository-local exact identifiers were searched with ignored and hidden files included; broad GO parents are not asserted to be exact matches.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Mixed organic chemistry and formation necessity remain UNKNOWN. No issue is manufactured for optional missing molecule inventories, dimensions, protein examples, causal graph or trait links.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Fresh official dataset catalogue and exact organism-matched FtsZ queries are scoped to E. coli precise1k and B. subtilis modulome. All-false thresholded membership is not biological absence. No positive module hit informs the verdict; no unrelated taxon substitution. Runner failure is explicitly historical, not a fresh invocation.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: All eight current native protein commands pass with empty declared exact-protein inventories and zero gene-protein graph nodes; they establish neither scientific completeness nor narrative protein identity.
- Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview: Root owns global QC, issue deduplication/publication and final CI. Three cell-septum findings retain exact original lineage; the other targets remain scientifically supported with limitations.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Every inherited finding is reassessed and retains exact predecessor identity.
- Bundle issues #2601 (one stale review), #2602 (eight structured-source applicability defects) and #2603 (missed photosystem canonical-example source/taxon conflict) are addressed here. Separate scientific record-curation findings remain open. Existing validator #2514 remains open.
- The frozen October23 energy-category finding photosystem-reaction-center-core-component-types targets only GO:0009521. Its corrected current component types are substantively reassessed and this exact historical finding is resolved. Already-closed #2420 is reused for that scoped lineage; this does not resolve its other historical targets anew.
- Source commit d7ee610a5d142b5961a6057e22437aabb68f191f is retained by tag review-base/pr2354-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration, graph/protein policies, verifier source, two target images and the October23 energy-category review pair.
- Six energy-complex reviews used unsupported lack-expression exemptions. Cell septum and cellular bud membrane omitted applicable molecular-source checks. Coccolith and coccosphere morphology/material claims do not require invented gene/module evidence.
- Fresh source inspection retains actual access dates. Primary bodies, abstracts, secondary reviews, authority responses, captions and inspected image pixels have distinct evidence scopes.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not validate molecular mechanisms or names appearing only in prose.
- PCC7942 computational module context is not evidence for the thermophilic preparation in Jordan2001. The historical 1JB0 metadata/current taxon and protein mapping conflict remains explicit.
- Seventeen open scientific findings are linked to #2604–#2620; sixteen preserve exact original batch occurrences and one newly identifies the photosystem canonical-example taxon/source conflict. The separately resolved category finding retains its exact single-target predecessor and already-closed #2420.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T065610Z-pr2354-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2354: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T06:45:01.061703Z'
finished_at: '2026-11-03T06:56:10Z'
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
summary: Current-input reassessment of all ten energy-complex and envelope records
  in PR2354. The stale photosystem review is substantively refreshed against changed
  reaction-center component types and current primary/authority sources. Its single-target
  historical component-type finding is resolved with exact lineage; the independent
  review also identifies a current canonical-example taxon/source conflict. Seven
  targets retain scientific curation findings; cellular bud membrane, coccolith and
  coccosphere retain qualified passes. Eight original bundles require structured-source
  applicability correction. Scientific records are unchanged.
source:
  git_revision: d7ee610a5d142b5961a6057e22437aabb68f191f
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
  - path: data/images/envelope/coccolith/pmc13067266_fig1.jpg
    sha256: 35772c3d477f71c47c7c2e0d6e91fbd6086b9061126c7bee92cec70fcd95f939
    role: context
  - path: data/images/envelope/coccosphere/pmc5896503_fig_2.jpg
    sha256: 5f3b2473ff6c3e1e281c8ae71b4c2d72dd32536e8c9b80e08f761c72b0bff765
    role: context
  - path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    sha256: 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e
    role: target
  - path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    sha256: ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459
    role: target
  - path: data/structures/energy_complex/photosystem.yaml
    sha256: c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8
    role: target
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    sha256: 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4
    role: target
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    sha256: f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c
    role: target
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    sha256: a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300
    role: target
  - path: data/structures/envelope/cell_septum.yaml
    sha256: feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54
    role: target
  - path: data/structures/envelope/cellular_bud_membrane.yaml
    sha256: e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f
    role: target
  - path: data/structures/envelope/coccolith.yaml
    sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
    role: target
  - path: data/structures/envelope/coccosphere.yaml
    sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
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
  - path: reviews/structured/20261021T100134Z-formate-dehydrogenase-complex-audit/review.md
    sha256: fa8a81615edfe2d019f004d7b2c8291a530587e8f57d64084510dbe1c9f8f683
    role: context
  - path: reviews/structured/20261021T100134Z-formate-dehydrogenase-complex-audit/review.yaml
    sha256: f4cfd4f49344849a40137038c91693e4b928b4f5a7aa47beb7601f3e6ce77d53
    role: context
  - path: reviews/structured/20261021T100137Z-nitrate-reductase-complex-audit/review.md
    sha256: fcd8005c2b820d03f93fa68185255b4dac4b3fd5bf1ce8af811533757b8c536b
    role: context
  - path: reviews/structured/20261021T100137Z-nitrate-reductase-complex-audit/review.yaml
    sha256: 9f96c6bc78113211504b025b7e9e1db8cbe347319ba059226c181a55e22cf5aa
    role: context
  - path: reviews/structured/20261021T100138Z-photosystem-audit/review.md
    sha256: 09cfaeca545499834315bfebefe2c920a6a1bdd7cbf730dc8eb9676f2decf90c
    role: context
  - path: reviews/structured/20261021T100138Z-photosystem-audit/review.yaml
    sha256: 9276bcea3a332e256fc57d9a65cae0cc50f347925aa0748f3f7c4a3659e62bc5
    role: context
  - path: reviews/structured/20261021T100139Z-proton-transporting-v-type-atpase-complex-audit/review.md
    sha256: 24445e8c1efa2b95cf728ea60f747794e5757dd7b8668e03c2d836400aee1ea7
    role: context
  - path: reviews/structured/20261021T100139Z-proton-transporting-v-type-atpase-complex-audit/review.yaml
    sha256: 62f6ae2d760655e4df251bfcdb2d1e4a12d38e3bb46d8628a4f24144a046b45c
    role: context
  - path: reviews/structured/20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit/review.md
    sha256: 87630dc89a7c186e6e8deb2b71d3ed7f3665f33468d2aa6ce44bdc81d40627c0
    role: context
  - path: reviews/structured/20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml
    sha256: 03fab0285e5720a50dcad20a595888e3315d10355e0f6e0708c60a32a8a4c117
    role: context
  - path: reviews/structured/20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit/review.md
    sha256: a0affba46220acdd1c5f273a8055ce3544cc2ceb4dc4648bdee6afc7e6e071da
    role: context
  - path: reviews/structured/20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml
    sha256: 409a468b8d8d85c53714f0c7fdb5ed83ad987b2d3df377371ee6dfcca83af9e7
    role: context
  - path: reviews/structured/20261021T100142Z-cell-septum-audit/review.md
    sha256: 1fe7284386911659dc0a3cfa2940c62cddcb0c10aaf3623d2ddccfdf3f830a8c
    role: context
  - path: reviews/structured/20261021T100142Z-cell-septum-audit/review.yaml
    sha256: a9c31aefbbf3ff80a987971d0f6c859f60fce61c333c882a71e981291585b4c5
    role: context
  - path: reviews/structured/20261021T100144Z-cellular-bud-membrane-audit/review.md
    sha256: f643c32b1365e539fffd92a79078d264dc0eecaf9f2c7323c4531d69341ab583
    role: context
  - path: reviews/structured/20261021T100144Z-cellular-bud-membrane-audit/review.yaml
    sha256: 63cd504abe65beeb7f477cac5900300c8b0f1b4e26d7f563eb6b10f94e2bbafd
    role: context
  - path: reviews/structured/20261021T100145Z-coccolith-audit/review.md
    sha256: b4cd8090a108c3948737a330103e8cd3c0ba99c848a1d0ca165e3b2914c81ac5
    role: context
  - path: reviews/structured/20261021T100145Z-coccolith-audit/review.yaml
    sha256: 6e8580c2d4618f8033a2d5456b3e3f9a73aa2348a774e2f65aac9e74796e41bd
    role: context
  - path: reviews/structured/20261021T100146Z-coccosphere-audit/review.md
    sha256: a0c05cab9d0ab725a6d458babf674dbaa469dde667baed1849a237219ffe7615
    role: context
  - path: reviews/structured/20261021T100146Z-coccosphere-audit/review.yaml
    sha256: 76f35c597967b604453e12add5b9b1e07881dfefa2eaf76c31d91cb61c1e3270
    role: context
  - path: reviews/structured/20261023T230504Z-energy-complex-category-review/review.md
    sha256: e115393c3bda40bd6af28fbf747e8c5d4df02288042af69f29ffac2f8d895146
    role: context
  - path: reviews/structured/20261023T230504Z-energy-complex-category-review/review.yaml
    sha256: 07773b203fe7fea9d6b3fb750e634e896ea0e7c05e6678f62b6a096dbd0d093b
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
- target_id: GO:0009326
  path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  label: formate dehydrogenase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
- target_id: GO:0009325
  path: data/structures/energy_complex/nitrate_reductase_complex.yaml
  label: nitrate reductase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
- target_id: GO:0009521
  path: data/structures/energy_complex/photosystem.yaml
  label: photosystem
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
- target_id: GO:0033176
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  label: proton-transporting V-type ATPase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
- target_id: GO:0033179
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
  label: proton-transporting V-type ATPase, V0 domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
- target_id: GO:0033180
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
  label: proton-transporting V-type ATPase, V1 domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
- target_id: GO:0030428
  path: data/structures/envelope/cell_septum.yaml
  label: cell septum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
- target_id: GO:0033101
  path: data/structures/envelope/cellular_bud_membrane.yaml
  label: cellular bud membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cellular_bud_membrane.yaml
    role: maintained scientific record
- target_id: cellstructuremech:coccolith
  path: data/structures/envelope/coccolith.yaml
  label: coccolith
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/coccolith.yaml
    role: maintained scientific record
- target_id: cellstructuremech:coccosphere
  path: data/structures/envelope/coccosphere.yaml
  label: coccosphere
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/coccosphere.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 56380c619e8356208b1b27c13edc4c6206b92443.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    e8bccd7c6a67ad41f4e044efbab4099dc09e2872.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head d7ee610a5d142b5961a6057e22437aabb68f191f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head d7ee610a5d142b5961a6057e22437aabb68f191f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head d7ee610a5d142b5961a6057e22437aabb68f191f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head d7ee610a5d142b5961a6057e22437aabb68f191f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head d7ee610a5d142b5961a6057e22437aabb68f191f.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0009326
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: just validate data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0009326
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: just validate-strict data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0009325
  status: passed
  required: true
  target_ids:
  - GO:0009325
  command: just validate data/structures/energy_complex/nitrate_reductase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0009325
  status: passed
  required: true
  target_ids:
  - GO:0009325
  command: just validate-strict data/structures/energy_complex/nitrate_reductase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0009521
  status: passed
  required: true
  target_ids:
  - GO:0009521
  command: just validate data/structures/energy_complex/photosystem.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0009521
  status: passed
  required: true
  target_ids:
  - GO:0009521
  command: just validate-strict data/structures/energy_complex/photosystem.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0033176
  status: passed
  required: true
  target_ids:
  - GO:0033176
  command: just validate data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0033176
  status: passed
  required: true
  target_ids:
  - GO:0033176
  command: just validate-strict data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0033179
  status: passed
  required: true
  target_ids:
  - GO:0033179
  command: just validate data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0033179
  status: passed
  required: true
  target_ids:
  - GO:0033179
  command: just validate-strict data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0033180
  status: passed
  required: true
  target_ids:
  - GO:0033180
  command: just validate data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0033180
  status: passed
  required: true
  target_ids:
  - GO:0033180
  command: just validate-strict data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0030428
  status: passed
  required: true
  target_ids:
  - GO:0030428
  command: just validate data/structures/envelope/cell_septum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0030428
  status: passed
  required: true
  target_ids:
  - GO:0030428
  command: just validate-strict data/structures/envelope/cell_septum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0033101
  status: passed
  required: true
  target_ids:
  - GO:0033101
  command: just validate data/structures/envelope/cellular_bud_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0033101
  status: passed
  required: true
  target_ids:
  - GO:0033101
  command: just validate-strict data/structures/envelope/cellular_bud_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate cellstructuremech:coccolith
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  command: just validate data/structures/envelope/coccolith.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict cellstructuremech:coccolith
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  command: just validate-strict data/structures/envelope/coccolith.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:coccosphere
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  command: just validate data/structures/envelope/coccosphere.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:coccosphere
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  command: just validate-strict data/structures/envelope/coccosphere.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354
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
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  summary: 'Applicability was assessed against the complete official catalogue. Matched
    E. coli and B. subtilis gene/module requests are bounded to the named genes and
    datasets, with thresholded membership and source scopes retained. Photosystem
    PCC7942 data are computational context only and are not an exact-strain match
    for the thermophilic Jordan preparation. No S. cerevisiae dataset is in the returned
    catalogue; unrelated bacterial datasets are not substitutes. Morphology-only coccolith/coccosphere
    claims have no identified gene/locus/protein or molecular pathway to query. Eight
    original reviews require correction: six unsupported exemptions and two omissions.
    Historical native-runner unavailability is separate from these source checks,
    with no fresh runner success claimed.'
  evidence_ids:
  - plaque-adapter-datasets
  - plaque-adapter-meta
  - plaque-adapter-search-fdnG
  - plaque-adapter-search-fdnH
  - plaque-adapter-search-fdnI
  - plaque-adapter-search-fdoG
  - plaque-adapter-search-fdoH
  - plaque-adapter-search-fdoI
  - plaque-adapter-search-narG
  - plaque-adapter-search-narH
  - plaque-adapter-search-narI
  - plaque-adapter-gene-modules-fdnG
  - plaque-adapter-gene-modules-fdnH
  - plaque-adapter-gene-modules-fdnI
  - plaque-adapter-gene-modules-fdoG
  - plaque-adapter-gene-modules-fdoH
  - plaque-adapter-gene-modules-fdoI
  - plaque-adapter-gene-modules-narG
  - plaque-adapter-gene-modules-narH
  - plaque-adapter-gene-modules-narI
  - plaque-adapter-syn-meta
  - plaque-adapter-syn-search-psaA
  - plaque-adapter-syn-search-psaB
  - plaque-adapter-syn-search-psbA
  - plaque-adapter-syn-search-psbD
  - plaque-adapter-summary-21
  - plaque-adapter-members-21
  - plaque-adapter-summary-67
  - plaque-adapter-members-67
  - plaque-adapter-summary-69
  - plaque-adapter-members-69
  - plaque-adapter-syn-modules-psaA
  - plaque-adapter-syn-modules-psaB
  - plaque-adapter-syn-summary-38
  - plaque-adapter-syn-members-38
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - septin-current-adapter-catalogue
  - septin-adapter-e_coli-precise1k-ftsZ-search
  - septin-adapter-b_subtilis-modulome-ftsZ-search
  - septin-adapter-e_coli-precise1k-b0095
  - septin-adapter-e_coli-precise1k-b0095-imodulons
  - septin-adapter-b_subtilis-modulome-BSU_15290
  - septin-adapter-b_subtilis-modulome-BSU_15290-imodulons
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-formate-agent-go
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-formate-agent-CPX-1975
  - plaque-formate-agent-P24183
  - plaque-formate-agent-P0AAJ3
  - plaque-formate-agent-P0AEK7
  - plaque-formate-agent-chebi-60539
  - plaque-formate-agent-chebi-16374
  - plaque-formate-agent-chebi-30413
  - plaque-formate-agent-chebi-33725
  - plaque-formate-agent-pmid-11884747
  - plaque-formate-agent-pmid-11884601
  - plaque-formate-agent-IPR006443
  - plaque-formate-agent-IPR006470
  - plaque-formate-agent-IPR006471
  - plaque-formate-agent-IPR014603
  - plaque-formate-agent-IPR051555
  - plaque-formate-agent-IPR051817
  - plaque-formate-agent-pmid-1504073
  - plaque-formate-agent-pmid-8566699
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-nitrate-agent-chebi-21137
  - plaque-nitrate-agent-chebi-49883
  - plaque-nitrate-agent-pmid-12910261
  - plaque-nitrate-agent-pmid-12950096
  - plaque-nitrate-agent-pmid-11289299
  - plaque-nitrate-agent-pmid-17964535
  - plaque-nitrate-agent-IPR006468
  - plaque-nitrate-agent-IPR006547
  - plaque-nitrate-agent-bertero-rcsb
  - plaque-nitrate-agent-bertero-crossref
  - plaque-nitrate-agent-bertero-publisher
  - plaque-nitrate-agent-bertero-pdf
  - plaque-nitrate-agent-richardson-publisher
  - plaque-photosystem-agent-go
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-photosystem-agent-epmc
  - plaque-photosystem-agent-jordan2001-publisher
  - plaque-photosystem-agent-P0A406
  - plaque-photosystem-agent-P0A408
  - plaque-photosystem-agent-P51765
  - plaque-photosystem-agent-D0VWR8
  - plaque-photosystem-agent-tax-1117
  - plaque-photosystem-agent-tax-32046
  - plaque-photosystem-agent-tax-32053
  - plaque-photosystem-agent-pdb-1jb0
  - plaque-photosystem-agent-pdb-1jb0-1
  - plaque-photosystem-agent-pdb-1jb0-2
  - plaque-photosystem-agent-pdb-1jb0-3
  - plaque-adapter-datasets
  - plaque-adapter-meta
  - plaque-adapter-gene-modules-fdnG
  - plaque-adapter-gene-modules-fdnH
  - plaque-adapter-gene-modules-fdnI
  - plaque-adapter-gene-modules-fdoG
  - plaque-adapter-gene-modules-fdoH
  - plaque-adapter-gene-modules-fdoI
  - plaque-adapter-gene-modules-narG
  - plaque-adapter-gene-modules-narH
  - plaque-adapter-gene-modules-narI
  - plaque-adapter-syn-meta
  - plaque-adapter-summary-21
  - plaque-adapter-members-21
  - plaque-adapter-summary-67
  - plaque-adapter-members-67
  - plaque-adapter-summary-69
  - plaque-adapter-members-69
  - plaque-adapter-syn-modules-psaA
  - plaque-adapter-syn-modules-psaB
  - plaque-adapter-syn-publication
  - plaque-photosystem-jordan-http
  - plaque-semchonok2021-pdf
  - plaque-taxonomy-bp1
  - plaque-taxonomy-pcc7942
  - plaque-adapter-syn-summary-38
  - plaque-adapter-syn-members-38
  - plaque-adapter-syn-primary
  - plaque-semchonok2021-meta
  - plaque-taxonomy-PSI-P0A405
  - plaque-taxonomy-PSI-P0A407
  - plaque-jormakka-browser-main
  - plaque-jormakka-browser-later
  - plaque-jormakka-browser-beta
  - plaque-schema
  - plaque-graph-policy
  - plaque-policy
  - plaque-adapter-policy
  - micro-go
  - micro-kane2006-secondary
  - micro-zhao2015-abstract
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-tax-4932
  - micro-literature-metadata
  - micro-adapter-catalogue
  - micro-review-policy
  - micro-graph-policy
  - septin-septum-agent-go
  - septin-septum-agent-tax-2
  - septin-septum-agent-tax-83333
  - septin-septum-agent-tax-1423
  - septin-septum-agent-chebi-8005
  - septin-septum-agent-jats-PMC8610174
  - septin-bud-membrane-agent-go
  - septin-bud-membrane-agent-SL-0028
  - septin-bud-membrane-agent-SL-0027
  - septin-bud-membrane-agent-tax-4932
  - septin-bud-membrane-agent-valtz1996-pdf
  - septin-coccolith-agent-go
  - septin-coccolith-agent-chebi-46719
  - septin-coccolith-agent-tax-127549
  - septin-coccolith-agent-tax-2903
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-avrahami2026-supp
  - septin-coccolith-agent-jats-PMC13089448
  - septin-coccolith-agent-jats-PMC9858585
  - septin-coccolith-agent-package-PMC13067266
  - septin-coccosphere-agent-go
  - septin-coccosphere-agent-tax-221442
  - septin-coccosphere-agent-jats-PMC5896503
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-coccosphere-agent-package-PMC5896503
  - septin-coccolith-image-source
  - septin-coccosphere-image-source
  - septin-current-adapter-catalogue
  - septin-bud-membrane-agent-finger-body
  - septin-bud-membrane-agent-finger-methods
  - septin-policy
  - septin-adapter-policy
  - septin-graph-policy
  - septin-graph-contract
  - septin-adapter-e_coli-precise1k-b0095
  - septin-adapter-e_coli-precise1k-b0095-imodulons
  - septin-adapter-b_subtilis-modulome-BSU_15290
  - septin-adapter-b_subtilis-modulome-BSU_15290-imodulons
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
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
- check_id: formate_dehydrogenase_complex-uniprot-verify
  name: Native formate dehydrogenase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-formate_dehydrogenase_complex-verify
- check_id: formate_dehydrogenase_complex-uniprot-causal
  name: Native formate dehydrogenase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009326
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-formate_dehydrogenase_complex-causal
- check_id: nitrate_reductase_complex-uniprot-verify
  name: Native nitrate reductase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009325
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/nitrate_reductase_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nitrate_reductase_complex-verify
- check_id: nitrate_reductase_complex-uniprot-causal
  name: Native nitrate reductase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009325
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/nitrate_reductase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-nitrate_reductase_complex-causal
- check_id: photosystem-uniprot-verify
  name: Native photosystem UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009521
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-photosystem-verify
- check_id: photosystem-uniprot-causal
  name: Native photosystem UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009521
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/photosystem.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-photosystem-causal
- check_id: proton_transporting_v_type_atpase_complex-uniprot-verify
  name: Native proton-transporting V-type ATPase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033176
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proton_transporting_v_type_atpase_complex-verify
- check_id: proton_transporting_v_type_atpase_complex-uniprot-causal
  name: Native proton-transporting V-type ATPase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033176
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proton_transporting_v_type_atpase_complex-causal
- check_id: proton_transporting_v_type_atpase_v0_domain-uniprot-verify
  name: Native proton-transporting V-type ATPase, V0 domain UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033179
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proton_transporting_v_type_atpase_v0_domain-verify
- check_id: proton_transporting_v_type_atpase_v0_domain-uniprot-causal
  name: Native proton-transporting V-type ATPase, V0 domain UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033179
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proton_transporting_v_type_atpase_v0_domain-causal
- check_id: proton_transporting_v_type_atpase_v1_domain-uniprot-verify
  name: Native proton-transporting V-type ATPase, V1 domain UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033180
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proton_transporting_v_type_atpase_v1_domain-verify
- check_id: proton_transporting_v_type_atpase_v1_domain-uniprot-causal
  name: Native proton-transporting V-type ATPase, V1 domain UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033180
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proton_transporting_v_type_atpase_v1_domain-causal
- check_id: cell_septum-uniprot-verify
  name: Native cell septum UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030428
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cell_septum.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cell_septum-verify
- check_id: cell_septum-uniprot-causal
  name: Native cell septum UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030428
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cell_septum.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cell_septum-causal
- check_id: cellular_bud_membrane-uniprot-verify
  name: Native cellular bud membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033101
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cellular_bud_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cellular_bud_membrane-verify
- check_id: cellular_bud_membrane-uniprot-causal
  name: Native cellular bud membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033101
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cellular_bud_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-cellular_bud_membrane-causal
- check_id: coccolith-uniprot-verify
  name: Native coccolith UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/coccolith.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-coccolith-verify
- check_id: coccolith-uniprot-causal
  name: Native coccolith UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccolith
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/coccolith.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-coccolith-causal
- check_id: coccosphere-uniprot-verify
  name: Native coccosphere UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/coccosphere.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-coccosphere-verify
- check_id: coccosphere-uniprot-causal
  name: Native coccosphere UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:coccosphere
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/coccosphere.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. An empty inventory or zero molecular
    graph nodes does not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-coccosphere-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e;
    current SHA256 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T100134Z-formate-dehydrogenase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f4cfd4f49344849a40137038c91693e4b928b4f5a7aa47beb7601f3e6ce77d53
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/energy_complex/nitrate_reductase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459;
    current SHA256 ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459.
    Record bytes unchanged since the original review.
  snapshot_sha256: ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T100137Z-nitrate-reductase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9f96c6bc78113211504b025b7e9e1db8cbe347319ba059226c181a55e22cf5aa
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/energy_complex/photosystem.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 ae1b5fe34147a0a1464e24943d5d8e1aca5cdd14e737af3ab0564fecabe65d35;
    current SHA256 c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8.
    Changed record reassessed against current sources.
  snapshot_sha256: c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T100138Z-photosystem-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9276bcea3a332e256fc57d9a65cae0cc50f347925aa0748f3f7c4a3659e62bc5
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4;
    current SHA256 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T100139Z-proton-transporting-v-type-atpase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 62f6ae2d760655e4df251bfcdb2d1e4a12d38e3bb46d8628a4f24144a046b45c
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c;
    current SHA256 f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c.
    Record bytes unchanged since the original review.
  snapshot_sha256: f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 03fab0285e5720a50dcad20a595888e3315d10355e0f6e0708c60a32a8a4c117
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300;
    current SHA256 a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300.
    Record bytes unchanged since the original review.
  snapshot_sha256: a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 409a468b8d8d85c53714f0c7fdb5ed83ad987b2d3df377371ee6dfcca83af9e7
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/envelope/cell_septum.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54;
    current SHA256 feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54.
    Record bytes unchanged since the original review.
  snapshot_sha256: feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T100142Z-cell-septum-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a9c31aefbbf3ff80a987971d0f6c859f60fce61c333c882a71e981291585b4c5
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/envelope/cellular_bud_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f;
    current SHA256 e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f.
    Record bytes unchanged since the original review.
  snapshot_sha256: e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T100144Z-cellular-bud-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 63cd504abe65beeb7f477cac5900300c8b0f1b4e26d7f563eb6b10f94e2bbafd
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/envelope/coccolith.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa;
    current SHA256 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T100145Z-coccolith-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6e8580c2d4618f8033a2d5456b3e3f9a73aa2348a774e2f65aac9e74796e41bd
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/envelope/coccosphere.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Original frozen SHA256 b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299;
    current SHA256 b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299.
    Record bytes unchanged since the original review.
  snapshot_sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T100146Z-coccosphere-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:56:10Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 76f35c597967b604453e12add5b9b1e07881dfefa2eaf76c31d91cb61c1e3270
- evidence_id: plaque-formate-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009326,GO:1990204,GO:0098803,GO:0036397
  locator: 'results: id, name, definition and native relations'
  accessed_at: '2026-11-03T06:48:08.588313Z'
  snapshot_sha256: b831ec9219123db26f8d348c099a7acd8949e884e6965fa10ed49b393510bebc
  summary: 'Verified exact native term identities and definitions: [(''GO:1990204'',
    ''oxidoreductase complex''), (''GO:0098803'', ''respiratory chain complex''),
    (''GO:0009326'', ''formate dehydrogenase complex''), (''GO:0036397'', ''formate
    dehydrogenase (quinone) activity'')]. Preserve nitrate GO0009325 reversed-reaction
    conflict and distinguish photosystem generic identity from oxygenic examples.'
  support: context_only
- evidence_id: plaque-formate-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:48:08.589387Z'
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
  summary: Authority identifies 83333 as Escherichia coli K-12; lineage Bacteria;
    Pseudomonadati; Pseudomonadota; Gammaproteobacteria; Enterobacterales; Enterobacteriaceae;
    Escherichia; ; historical names ['Escherichia coli K12:equivalent name'].
  support: context_only
- evidence_id: plaque-formate-agent-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:48:08.590555Z'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
  summary: Authority identifies 2 as Bacteria; lineage root/domain lineage not supplied;
    historical names ['"Bacteriobiota" Luketa 2012:authority', '"Bacteria" Cavalier-Smith
    1987:authority', 'Bacteriobiota:synonym', 'Bacteria (ex Cavalier-Smith 1987):synonym',
    'Bacteria Woese et al. 2024:synonym', 'bacteria:genbank common name', 'bacteria
    <genbank common name>:genbank common name'].
  support: context_only
- evidence_id: plaque-formate-agent-tax-2157
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:48:08.591891Z'
  snapshot_sha256: 84a40b3fb3e403b1ab61ce4ab647c6eaa5526395605d947756d90105e0512a3d
  summary: Authority identifies 2157 as Archaea; lineage root/domain lineage not supplied;
    historical names ['Archaea Woese et al. 2024:authority', '"Archaea" Woese et al.
    1990:authority', '"Archaebiota" Luketa 2012:authority', '"Archaebacteria" (sic)
    Woese and Fox 1977:authority', 'Archaebiota:synonym', 'Archaebacteria:synonym',
    'Mendosicutes:synonym', 'Metabacteria:synonym'].
  support: context_only
- evidence_id: plaque-formate-agent-CPX-1975
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1975
  locator: participants, systematicName, complexAssemblies, functions and cofactors
  accessed_at: '2026-11-03T06:48:09.206042Z'
  snapshot_sha256: 75e2194688769d12f475e0af8d81020874906d3147da691350f7613934492b0a
  summary: Formate dehydrogenase N complex, source Escherichia coli (strain K12);
    83333; 3xfdnG:3xfdnH:3xfdnI, assembly ['Heterononamer']. Participant identities,
    redox roles and source-specific cofactor inventory verified; not generic-class
    stoichiometry.
  support: context_only
- evidence_id: plaque-formate-agent-P24183
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P24183.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:09.224870Z'
  snapshot_sha256: ba2315e5da95abf93454652ba95bbb88544bacfd880ab626d0de191d2a4bbcfd
  summary: 'P24183: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli
    (strain K12)); genes [''fdnG'']. Native annotation was inspected; reviewed status
    does not itself prove experimental membership.'
  support: context_only
- evidence_id: plaque-formate-agent-query-fdnG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:09.230400Z'
  snapshot_sha256: fd97d9165d2474db32a0256d5d281eee329201683eae5b7ebb318e64c155f782
  summary: 'Returned accessions/taxa: [(''P24183'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:09.230400Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-formate-agent-P0AAJ3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AAJ3.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:09.236449Z'
  snapshot_sha256: dfd5786fd27795f7864c49e371f7f6a2cf4a1be773a8fac4ea377a4a963ba349
  summary: 'P0AAJ3: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli
    (strain K12)); genes [''fdnH'']. Native annotation was inspected; reviewed status
    does not itself prove experimental membership.'
  support: context_only
- evidence_id: plaque-formate-agent-query-fdnH
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:09.995225Z'
  snapshot_sha256: 58db8e9048d4c7d73e40a9829a93684bab444f8f15ca2e739b71c55b70dad468
  summary: 'Returned accessions/taxa: [(''P0AAJ3'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:09.995225Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-formate-agent-P0AEK7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEK7.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:10.053840Z'
  snapshot_sha256: 944e58794aef18b85feefa6325421b4962db8fc0cc0dbb3a3c9c534b3bb00611
  summary: 'P0AEK7: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli
    (strain K12)); genes [''fdnI'']. Native annotation was inspected; reviewed status
    does not itself prove experimental membership.'
  support: context_only
- evidence_id: plaque-formate-agent-query-fdnI
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:10.467964Z'
  snapshot_sha256: b4349e8db16c10f14b726c577918be9e7ec446e677516d46ed531953dcc57150
  summary: 'Returned accessions/taxa: [(''P0AEK7'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdnI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:10.467964Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-formate-agent-chebi-60539
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_60539
  locator: Native ChEBI term identity
  accessed_at: '2026-11-03T06:48:10.827320Z'
  snapshot_sha256: d4af89178cd9f6d2d13474e41ce605ebf40f7984a52f488232f4cb42b10771b5
  summary: Verified [('CHEBI:60539', 'Mo(=O)-bis(molybdopterin guanine dinucleotide)(4-)')].
    Chemical identifiers do not independently prove assembly necessity.
  support: context_only
- evidence_id: plaque-formate-agent-chebi-16374
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16374
  locator: Native ChEBI term identity
  accessed_at: '2026-11-03T06:48:10.885127Z'
  snapshot_sha256: 2de776b9c8383ac4a359573a9d404e233ec52e5c4ce828ff580a436451466eac
  summary: Verified [('CHEBI:16374', 'menaquinone')]. Chemical identifiers do not
    independently prove assembly necessity.
  support: context_only
- evidence_id: plaque-formate-agent-chebi-30413
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30413
  locator: Native ChEBI term identity
  accessed_at: '2026-11-03T06:48:11.324954Z'
  snapshot_sha256: 674cfe9540f1509052fe3ca7d406154865585bac0d66e0663e1b4bdbb9e27d80
  summary: Verified [('CHEBI:30413', 'heme')]. Chemical identifiers do not independently
    prove assembly necessity.
  support: context_only
- evidence_id: plaque-formate-agent-chebi-33725
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33725
  locator: Native ChEBI term identity
  accessed_at: '2026-11-03T06:48:11.434072Z'
  snapshot_sha256: 3f443234ffd6663280774061bb05a66b042e5a19c07bc55713ed522ee5787371
  summary: Verified [('CHEBI:33725', 'tetra-mu3-sulfido-tetrairon(0)')]. Chemical
    identifiers do not independently prove assembly necessity.
  support: context_only
- evidence_id: plaque-formate-agent-pmid-11884747
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11884747+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:11.468243Z'
  snapshot_sha256: c3630641a9d191423be763666356908ab8263830b774c006fa2dcf87e86c1562
  summary: 'Verified [(''11884747'', ''Molecular basis of proton motive force generation:
    structure of formate dehydrogenase-N.'', ''10.1126/science.1068186'')]. Read abstract
    tier only in this response.'
  support: context_only
- evidence_id: plaque-formate-agent-pmid-11884601
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11884601+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:11.521208Z'
  snapshot_sha256: e26b54b63f1f7bb6d50fd13deaf093be0352ea02fc92bc35afe2ec68944fe012
  summary: Verified [('11884601', 'Protein kinase A associates with HA95 and affects
    transcriptional coactivation by Epstein-Barr virus nuclear proteins.', '10.1128/mcb.22.7.2136-2146.2002')].
    Read abstract tier only in this response. The HA95/PKA/EBV paper is unrelated
    to formate-dehydrogenase distribution.
  support: context_only
- evidence_id: plaque-formate-agent-jormakka2002-browser
  kind: validation
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: Source transport/access attempt
  accessed_at: '2026-11-03T06:48:11.936310Z'
  snapshot_sha256: 94bba8a882d7e5824f5724d98b60d49378912c8e54dbaf055a0c5a4a0bb76f72
  summary: Actual curl HTTP 403, exit 0; 21293 bytes. This attempt did not provide
    a usable scientific article body and supports no biological absence inference.
  support: context_only
- evidence_id: plaque-formate-agent-IPR006443
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006443/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:12.027356Z'
  snapshot_sha256: 24f4e300ffb3d9d955944ac1e052fc9f8fa01990be18ca8488598f57636b60d8
  summary: 'Native family: {''name'': ''Formate dehydrogenase-N, alpha subunit'',
    ''short'': ''Formate-DH-alph_fdnG''}; members {''ncbifam'': {''TIGR01553'': ''formate
    dehydrogenase-N subunit alpha''}}. Family identity inspected, without imposing
    an exact isoenzyme-only grounding or interpreting homolog coverage as assembly
    proof.'
  support: context_only
- evidence_id: plaque-formate-agent-IPR006470
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006470/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:12.028608Z'
  snapshot_sha256: 84eb09c9e62a1c1e495491e40225da1f78ff6a2058fd88392189ec969758187f
  summary: 'Native family: {''name'': ''Formate dehydrogenase iron-sulphur subunit,
    Proteobacteria'', ''short'': ''Formate_DH_bsu_Proteobacteria''}; members {''cdd'':
    {''cd10558'': ''The beta FeS subunit of formate dehydrogenase-N (FDH-N)''}, ''ncbifam'':
    {''TIGR01582'': ''formate dehydrogenase subunit beta''}}. Family identity inspected,
    without imposing an exact isoenzyme-only grounding or interpreting homolog coverage
    as assembly proof.'
  support: context_only
- evidence_id: plaque-formate-agent-IPR006471
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006471/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:12.093687Z'
  snapshot_sha256: 3d1551fd8933584086ab05290617b611d20f1703641048bbade7301cbe877851
  summary: 'Native family: {''name'': ''Formate dehydrogenase, gamma subunit'', ''short'':
    ''Formate_DH_gsu''}; members {''ncbifam'': {''TIGR01583'': ''formate dehydrogenase
    subunit gamma''}}. Broader homologous gamma-subunit coverage includes hydrogenase/thiosulfate-reductase
    context; not an FdnI-only grounding.'
  support: context_only
- evidence_id: plaque-formate-agent-IPR014603
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014603/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:12.144233Z'
  snapshot_sha256: 8bb0299ccaad43b41a404c591262616896e7787d67647ff3ab87de310c5fdd02
  summary: 'Native family: {''name'': ''Formate dehydrogenase iron-sulphur subunit'',
    ''short'': ''Formate_DH_Fe-S_su''}; members {''pirsf'': {''PIRSF036298'': ''Formate
    dehydrogenase, iron-sulphur subunit''}}. Family identity inspected, without imposing
    an exact isoenzyme-only grounding or interpreting homolog coverage as assembly
    proof.'
  support: context_only
- evidence_id: plaque-formate-agent-IPR051555
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051555/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:12.639725Z'
  snapshot_sha256: 0b9a9eff7be9ed6a6c783399f853c007079e2ce7f1d5797ee6f85f0e9997fd77
  summary: 'Native family: {''name'': ''Formate Dehydrogenase Electron Transfer Unit'',
    ''short'': ''FDH_Electron_Transfer_Unit''}; members {''panther'': {''PTHR43545'':
    ''Formate Dehydrogenase Electron Transfer Unit''}}. Description flagged llm:true/checked:false;
    generated prose is excluded as mechanism evidence.'
  support: context_only
- evidence_id: plaque-formate-agent-IPR051817
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051817/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:12.670096Z'
  snapshot_sha256: 9a9fde2804cf8d99257b1bc6434666fd667d70b4eda23fc484a9be2eb6f68331
  summary: 'Native family: {''name'': ''Formate dehydrogenase cytochrome b556 subunit'',
    ''short'': ''FDH_cytochrome_b556_subunit''}; members {''panther'': {''PTHR30074'':
    ''Formate dehydrogenase cytochrome b556 subunit''}}. Description flagged llm:true/checked:false;
    generated prose is excluded as mechanism evidence.'
  support: context_only
- evidence_id: plaque-formate-agent-query-fdoG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:12.705736Z'
  snapshot_sha256: 350efd301bc048134be70e6a58641f001e4b66b0c4a4f3fe7e1b63f5a4152fda
  summary: 'Returned accessions/taxa: [(''P32176'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:12.705736Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-formate-agent-query-fdoH
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:12.739556Z'
  snapshot_sha256: b8c2eb6df27a506406be65181d6b237534f629492ba3302c0156d208fa61a2c6
  summary: 'Returned accessions/taxa: [(''P0AAJ5'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:12.739556Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-formate-agent-query-fdoI
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:13.266741Z'
  snapshot_sha256: a3d914b2c3a4e07590693bb6a7cd668cebb58121df1ca5cc88a6c615f005d9f3
  summary: 'Returned accessions/taxa: [(''P0AEL0'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AfdoI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:13.266741Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-formate-agent-pmid-1504073
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A1504073+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:13.280807Z'
  snapshot_sha256: cad06f694023f37516b2d350ce62dc404fa9405fb28096b67dc7cfc9cd5fed7c
  summary: Verified [('1504073', 'A second phenazine methosulphate-linked formate
    dehydrogenase isoenzyme in Escherichia coli.', '10.1016/0005-2736(92)90417-k')].
    Read abstract tier only in this response.
  support: context_only
- evidence_id: plaque-formate-agent-pmid-8566699
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8566699+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:13.615921Z'
  snapshot_sha256: cf35cb31d99cf3559c458fea2ea884ffc595c4a055b1685c2ab6388da3bc4330
  summary: Verified [('8566699', 'Purification and characterization of the formate
    dehydrogenase from Desulfovibrio vulgaris Hildenborough.', '10.1111/j.1574-6968.1995.tb07875.x')].
    Read abstract tier only in this response.
  support: context_only
- evidence_id: plaque-nitrate-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009325,GO:1990204,GO:0044799,GO:0160182
  locator: 'results: id, name, definition and native relations'
  accessed_at: '2026-11-03T06:48:13.689220Z'
  snapshot_sha256: aed4d3846b881d6516b56b93ca8a3d940010e58f5befcff5401d26aff2c857d9
  summary: 'Verified exact native term identities and definitions: [(''GO:0044799'',
    ''NarGHI complex''), (''GO:1990204'', ''oxidoreductase complex''), (''GO:0009325'',
    ''nitrate reductase complex''), (''GO:0160182'', ''nitrate reductase (quinone)
    activity'')]. Preserve nitrate GO0009325 reversed-reaction conflict and distinguish
    photosystem generic identity from oxygenic examples.'
  support: context_only
- evidence_id: plaque-nitrate-agent-CPX-1974
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1974
  locator: participants, systematicName, complexAssemblies, functions and cofactors
  accessed_at: '2026-11-03T06:48:13.890417Z'
  snapshot_sha256: e54329b78adf152eaee67d083c8dee8befc5cbaedb92f76c2c97f65e1513cf13
  summary: Nitrate reductase A complex, source Escherichia coli (strain K12); 83333;
    2xnarG:2xnarH:2xnarI, assembly ['Heterohexamer']. Participant identities, redox
    roles and source-specific cofactor inventory verified; not generic-class stoichiometry.
  support: context_only
- evidence_id: plaque-nitrate-agent-P09152
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09152.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:14.240074Z'
  snapshot_sha256: 7f778f7b8ff4193fe7f00cc3aa7f2737daa8f2c9a19e07dded498ab5bb6057db
  summary: 'P09152: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli
    (strain K12)); genes [''narG'']. Native annotation was inspected; reviewed status
    does not itself prove experimental membership.'
  support: context_only
- evidence_id: plaque-nitrate-agent-query-narG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:14.338380Z'
  snapshot_sha256: daf163d13eb3ff94d6c6ee14d0f49d7b2038f280a9815995f99683e1f5de90bf
  summary: 'Returned accessions/taxa: [(''P09152'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:14.338380Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-nitrate-agent-P11349
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11349.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:14.390976Z'
  snapshot_sha256: 314bb10c12ffb383b607668b73a2019ba2544d880cf2c212bc1b5c863a73628a
  summary: 'P11349: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli
    (strain K12)); genes [''narH'']. Native annotation was inspected; reviewed status
    does not itself prove experimental membership.'
  support: context_only
- evidence_id: plaque-nitrate-agent-query-narH
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:14.964370Z'
  snapshot_sha256: d521e8563a530975a26e40f697d95649cdada4fe86617129af5da81367a77a59
  summary: 'Returned accessions/taxa: [(''P11349'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarH%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:14.964370Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-nitrate-agent-P11350
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11350.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:15.131849Z'
  snapshot_sha256: 691e2cdf24e90c807b1b8ef4b33286cd50bc7a6023bdd8103b9b6f33fb2aab50
  summary: 'P11350: UniProtKB reviewed (Swiss-Prot); taxon 83333 (Escherichia coli
    (strain K12)); genes [''narI'']. Native annotation was inspected; reviewed status
    does not itself prove experimental membership.'
  support: context_only
- evidence_id: plaque-nitrate-agent-query-narI
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:15.334483Z'
  snapshot_sha256: 4dd7ec0fdd2e151a499e372f9e3b53b4f9b96493316eac61a777e6a487aac18d
  summary: 'Returned accessions/taxa: [(''P11350'', 83333)]. This verifies bounded
    query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AnarI%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    fetched 2026-11-03T06:48:15.334483Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-nitrate-agent-chebi-21137
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_21137
  locator: Native ChEBI term identity
  accessed_at: '2026-11-03T06:48:15.561388Z'
  snapshot_sha256: 93c2ca9151015ab8984e07b82586b8b1c940d981921b7c787aaf6c301b2716c9
  summary: Verified [('CHEBI:21137', 'tri-mu-sulfido-mu3-sulfido-triiron')]. Chemical
    identifiers do not independently prove assembly necessity.
  support: context_only
- evidence_id: plaque-nitrate-agent-chebi-49883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49883
  locator: Native ChEBI term identity
  accessed_at: '2026-11-03T06:48:16.177774Z'
  snapshot_sha256: 9818554c687c361f5d3b2ab4e553bf4c708cbccf51059ce60d71ffe37a3590a6
  summary: Verified [('CHEBI:49883', 'tetra-mu3-sulfido-tetrairon')]. Chemical identifiers
    do not independently prove assembly necessity.
  support: context_only
- evidence_id: plaque-nitrate-agent-pmid-12910261
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12910261+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:16.343756Z'
  snapshot_sha256: 59a4bb58dc4873d917e983ecaf745b32b94571f117ae4fc9611bcd537256f633
  summary: Verified [('12910261', 'Insights into the respiratory electron transfer
    pathway from the structure of nitrate reductase A.', '10.1038/nsb969')]. Read
    abstract tier only in this response.
  support: context_only
- evidence_id: plaque-nitrate-agent-pmid-12950096
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12950096+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:16.599801Z'
  snapshot_sha256: 700b3368d67a2d0c8dd8bbdeb0f1833779b93c3c3cc5cf6eb1628702e85500c2
  summary: 'Verified [(''12950096'', "Willingness to pay and size of health benefit:
    an integrated model to test for ''sensitivity to scale''.", ''10.1002/hec.786'')].
    Read abstract tier only in this response. The willingness-to-pay health-economics
    paper is unrelated to nitrate-reductase distribution.'
  support: context_only
- evidence_id: plaque-nitrate-agent-pmid-11289299
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11289299+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:16.810098Z'
  snapshot_sha256: f9cdda5c771627b7c5134909d76dec68702d5a1a9a113f0a479a087b82c2ca57
  summary: Verified [('11289299', 'Functional, biochemical and genetic diversity of
    prokaryotic nitrate reductases.', '10.1007/pl00000845')]. Read abstract tier only
    in this response. These are secondary review articles; no direct experimental
    claim is inferred from their abstract.
  support: context_only
- evidence_id: plaque-nitrate-agent-pmid-17964535
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A17964535+AND+SRC%3AMED
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:16.954112Z'
  snapshot_sha256: 7d26f9626dfc9340445a20c530f215855fec5b6096a7f1478d8638f929b35838
  summary: Verified [('17964535', 'The prokaryotic complex iron-sulfur molybdoenzyme
    family.', '10.1016/j.bbamem.2007.09.002')]. Read abstract tier only in this response.
    These are secondary review articles; no direct experimental claim is inferred
    from their abstract.
  support: context_only
- evidence_id: plaque-nitrate-agent-IPR006468
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006468/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:17.224243Z'
  snapshot_sha256: b7ff761f4d7c377f1edba2465452109c179f823230f1df272865a5b064f15471
  summary: 'Native family: {''name'': ''Nitrate reductase alpha subunit'', ''short'':
    ''NarG''}; members {''ncbifam'': {''TIGR01580'': ''nitrate reductase subunit alpha''}}.
    Family identity inspected, without imposing an exact isoenzyme-only grounding
    or interpreting homolog coverage as assembly proof.'
  support: context_only
- evidence_id: plaque-nitrate-agent-IPR006547
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006547/
  locator: metadata.name/type/member_databases and source annotation flags
  accessed_at: '2026-11-03T06:48:17.406484Z'
  snapshot_sha256: 7f8019254a2670a952efcf9b03517c6102d768b9d5379bd784a2c9e563617335
  summary: 'Native family: {''name'': ''Nitrate reductase, beta subunit'', ''short'':
    ''NO3_Rdtase_bsu''}; members {''cdd'': {''cd10557'': ''beta subunit of nitrate
    reductase A (NarH) and similar proteins''}, ''ncbifam'': {''TIGR01660'': ''nitrate
    reductase subunit beta''}}. NarH/NarY family; its legacy tetramer prose conflicts
    with CPX1974/UniProt dimer-of-heterotrimers annotation and is not silently adopted.'
  support: context_only
- evidence_id: plaque-nitrate-agent-bertero-rcsb
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1Q16
  locator: PDB1Q16 deposition and citation metadata
  accessed_at: '2026-11-03T06:48:17.428543Z'
  snapshot_sha256: b805b8a79f09b6816646d2c33c49b31909ac51114ac33bb60b0ebaa23adae4a3
  summary: Native author deposition identifies the E.coli NarGHI nitrate-reductase
    structure and Bertero2003 primary citation; no raw coordinates reanalyzed.
  support: context_only
- evidence_id: plaque-nitrate-agent-bertero-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1038/nsb969
  locator: DOI/title/publication metadata
  accessed_at: '2026-11-03T06:48:17.526329Z'
  snapshot_sha256: 11af2094d2c8c94454bfefaf814818b6f8e8ba64c1b698c94684be2a7c17cfab
  summary: Verified Bertero DOI10.1038/nsb969 citation identity. Metadata is not full-body
    biological evidence.
  support: context_only
- evidence_id: plaque-nitrate-agent-bertero-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/nsb969
  locator: Actual HTML abstract and subscription/access markup
  accessed_at: '2026-11-03T06:48:17.567103Z'
  snapshot_sha256: 6200eeb44686eb0ef4ef499d68fd94aa74f366269aff96290eadcaa5c2471f67
  summary: The HTTP200 response is abstract/metadata/subscription HTML, including
    the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson
    is a secondary review.
  support: context_only
- evidence_id: plaque-nitrate-agent-bertero-pdf
  kind: primary_source
  reference: https://www.nature.com/articles/nsb969.pdf
  locator: Actual HTML abstract and subscription/access markup
  accessed_at: '2026-11-03T06:48:17.838013Z'
  snapshot_sha256: 9b95dd69f3397083b76b3381ae7450e3628c8b5f17d50b4ee3038f44a340b661
  summary: The HTTP200 response is abstract/metadata/subscription HTML, including
    the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson
    is a secondary review.
  support: context_only
- evidence_id: plaque-nitrate-agent-richardson-publisher
  kind: authority
  reference: https://link.springer.com/article/10.1007/PL00000845
  locator: Actual HTML abstract and subscription/access markup
  accessed_at: '2026-11-03T06:48:17.898399Z'
  snapshot_sha256: 3c1ba3bfff394e77ebb5cb4300f1f7b276cb34502b7a55c06aff4b043d06dbc8
  summary: The HTTP200 response is abstract/metadata/subscription HTML, including
    the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson
    is a secondary review.
  support: context_only
- evidence_id: plaque-nitrate-agent-rothery-elsevier
  kind: validation
  reference: https://api.elsevier.com/content/article/doi/10.1016/j.bbamem.2007.09.002?httpAccept=text/xml
  locator: Actual XML response
  accessed_at: '2026-11-03T06:48:18.015083Z'
  snapshot_sha256: 645ffcc3b6f190a90789dcd4b23e5c05c69a860e312e59b53f4226648ea084fe
  summary: HTTP200 is a metadata/entitlement stub for the Rothery review, not readable
    full body; abstract evidence comes from EuropePMC.
  support: context_only
- evidence_id: plaque-photosystem-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009521,GO:0098796,GO:0034357,GO:0009522,GO:0009523,GO:0009767
  locator: 'results: id, name, definition and native relations'
  accessed_at: '2026-11-03T06:48:18.461324Z'
  snapshot_sha256: ea7b23d65e53a895f8687c3945434aa4533be485a3a0af42b41f8649eb5f8a36
  summary: 'Verified exact native term identities and definitions: [(''GO:0098796'',
    ''membrane protein complex''), (''GO:0034357'', ''photosynthetic membrane''),
    (''GO:0009767'', ''photosynthetic electron transport chain''), (''GO:0009523'',
    ''photosystem II''), (''GO:0009522'', ''photosystem I''), (''GO:0009521'', ''photosystem'')].
    Preserve nitrate GO0009325 reversed-reaction conflict and distinguish photosystem
    generic identity from oxygenic examples.'
  support: context_only
- evidence_id: plaque-photosystem-agent-jordan2001-pdf
  kind: validation
  reference: https://dosequis.colorado.edu/Courses/InsaneMembrane/papers/PS1-PSII-LHC%27s/photosystem1.pdf
  locator: Source transport/access attempt
  accessed_at: '2026-11-03T06:48:19.056729Z'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  summary: Actual curl HTTP 000, exit 60; 0 bytes. This attempt did not provide a
    usable scientific article body and supports no biological absence inference.
  support: context_only
- evidence_id: plaque-photosystem-agent-umena2011-pdf
  kind: primary_source
  reference: https://chemie.uni-muenchen.de/ac/kluefers/homepage/L/bac/oec_2011.pdf
  locator: Genuine PDF main body pp55-59; overall structure, Mn4CaO5 ligands, cofactors
    and Methods
  accessed_at: '2026-11-03T06:48:19.102868Z'
  snapshot_sha256: 29e5d7be00bc7ccf1acf26fe3276d2176b6fe92fe5736280637602b52623f693
  summary: Inspected T.vulcanus PSII preparation and D1/D2 core/cofactors. D1 supplies
    most oxygen-evolving cluster ligands, with direct CP43 contribution. Structural
    proposals for proton/water channels remain proposals; no universal type-II or
    assembly-removal claim.
  support: context_only
- evidence_id: plaque-photosystem-agent-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID%3A11418848%20OR%20EXT_ID%3A21499260%20OR%20EXT_ID%3A12518057%20OR%20EXT_ID%3A19433803
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:48:19.185857Z'
  snapshot_sha256: 72f9e7cce062b8dbb97c1312241679301d1d137ae7f3af541db848ae8ee21f5d
  summary: Verified [('21499260', 'Crystal structure of oxygen-evolving photosystem
    II at a resolution of 1.9 Å.', '10.1038/nature09913'), ('19433803', 'Location
    of chloride and its possible functions in oxygen-evolving photosystem II revealed
    by X-ray crystallography.', '10.1073/pnas.0812797106'), ('12518057', 'Crystal
    structure of oxygen-evolving photosystem II from Thermosynechococcus vulcanus
    at 3.7-A resolution.', '10.1073/pnas.0135651100'), ('11418848', 'Three-dimensional
    structure of cyanobacterial photosystem I at 2.5 A resolution.', '10.1038/35082000')].
    Read abstract tier only in this response.
  support: context_only
- evidence_id: plaque-photosystem-agent-jordan2001-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/35082000
  locator: Actual HTML abstract and subscription/access markup
  accessed_at: '2026-11-03T06:48:19.703948Z'
  snapshot_sha256: 3f3e193508700b0b949703bd0f6bcf711b88dcd2dc32c21bb357be5fbff1d771
  summary: The HTTP200 response is abstract/metadata/subscription HTML, including
    the nominal Bertero PDF URL. No full article body was recovered or claimed; Richardson
    is a secondary review.
  support: context_only
- evidence_id: plaque-photosystem-agent-P0A406
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A406.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:20.037279Z'
  snapshot_sha256: 9cd0860c569373f26d108ec33b53494f110ea9ab2c065d255bae891fc91355fb
  summary: 'P0A406: UniProtKB reviewed (Swiss-Prot); taxon 32046 (Synechococcus elongatus);
    genes [''psaA'']. Native annotation was inspected; reviewed status does not itself
    prove experimental membership.'
  support: context_only
- evidence_id: plaque-photosystem-agent-P0A408
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A408.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:20.716351Z'
  snapshot_sha256: b3cd834e3b314a930603c5902dd69136ae1330b299dfb997a5c7a585969ac366
  summary: 'P0A408: UniProtKB reviewed (Swiss-Prot); taxon 32046 (Synechococcus elongatus);
    genes [''psaB'']. Native annotation was inspected; reviewed status does not itself
    prove experimental membership.'
  support: context_only
- evidence_id: plaque-photosystem-agent-P51765
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P51765.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:20.763782Z'
  snapshot_sha256: 04887fcce267947732efc1a8148837c6691f19aedf33874357ac93e63338b2f7
  summary: 'P51765: UniProtKB reviewed (Swiss-Prot); taxon 32053 (Thermostichus vulcanus);
    genes [''psbA'']. Native annotation was inspected; reviewed status does not itself
    prove experimental membership.'
  support: context_only
- evidence_id: plaque-photosystem-agent-D0VWR8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/D0VWR8.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:48:21.086239Z'
  snapshot_sha256: 3b383aa42a19d3fd926532422025ccb924def2c56cf45f212de3d50786155663
  summary: 'D0VWR8: UniProtKB reviewed (Swiss-Prot); taxon 32053 (Thermostichus vulcanus);
    genes [''psbD'']. Native annotation was inspected; reviewed status does not itself
    prove experimental membership.'
  support: context_only
- evidence_id: plaque-photosystem-agent-tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:48:21.448290Z'
  snapshot_sha256: 5f4919ad6f362a82291b587d27134147f277ffc5fa593f6076f1983a704cd985
  summary: Authority identifies 1117 as Cyanobacteriota; lineage Bacteria; Bacillati;
    ; historical names ['Oxygenic photosynthetic bacteria:equivalent name', 'Cyanobacteriophyta
    Oren, Mares & Rippka, 2022:authority', 'Cyanobacteriota Oren et al. 2022:authority',
    '"Cyanobacteria" (ex Stanier 1974) Cavalier-Smith, 2002:authority', 'Cyanobacteriophyta:synonym',
    'Cyanophyta:synonym', 'Cyanophycota:synonym', 'Oxyphotobacteria:synonym', 'cyanobacteria:genbank
    common name', 'cyanobacteria <genbank common name>:genbank common name'].
  support: context_only
- evidence_id: plaque-photosystem-agent-tax-32046
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32046
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:48:21.502776Z'
  snapshot_sha256: b7aac872a40661f808e3fa17a661bb4b29ea7c857fe30e1b636be882fed66e01
  summary: Authority identifies 32046 as Synechococcus elongatus; lineage Bacteria;
    Bacillati; Cyanobacteriota; Cyanophyceae; Synechococcales; Synechococcaceae; Synechococcus;
    ; historical names ['Synechococcus elongatus Nageli 1849:authority'].
  support: context_only
- evidence_id: plaque-photosystem-agent-tax-32053
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:48:21.596709Z'
  snapshot_sha256: 22e01d3cfa17a447e15eeb62ce0bc9e9f698799dc9e5e2586e3408b075a1829e
  summary: Authority identifies 32053 as Thermostichus vulcanus; lineage Bacteria;
    Bacillati; Cyanobacteriota; Cyanophyceae; Thermostichales; Thermostichaceae; Thermostichus;
    ; historical names ['Synechococcus vulcanus J.J.Copeland, 1936:authority', 'Thermostichus
    vulcanus (J.J.Copeland, 1936) Komarek & Strunecky, 2020:authority', 'Thermosynechococcus
    vulcanus (J.J.Copeland, 1936) Katoh et al., 2001:authority', 'Synechococcus vulcanus:synonym',
    'Thermosynechococcus vulcanus:synonym'].
  support: context_only
- evidence_id: plaque-photosystem-agent-psi-unique
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29%20AND%20%28organism_id%3A32046%29%20AND%20%28gene_exact%3ApsaA%20OR%20gene_exact%3ApsaB%29&format=json&size=500
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:22.044338Z'
  snapshot_sha256: 79044f1656731c11740051a53e31bc3f626d9044be97abfe11f7a21bf0a240b9
  summary: 'Returned accessions/taxa: [(''P0A408'', 32046), (''P0A406'', 32046)].
    This verifies bounded query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29%20AND%20%28organism_id%3A32046%29%20AND%20%28gene_exact%3ApsaA%20OR%20gene_exact%3ApsaB%29&format=json&size=500;
    fetched 2026-11-03T06:48:22.044338Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-photosystem-agent-uniprot-unique
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&format=json&size=100
  locator: Bounded reviewed UniProt query at declared organism/taxonomy node
  accessed_at: '2026-11-03T06:48:22.120864Z'
  snapshot_sha256: e384401ab283e369cbd5420ec28f61a00684b2868f42cb5b9b7a7bffb1dea974
  summary: 'Returned accessions/taxa: [(''D0VWR8'', 32053), (''P51765'', 32053)].
    This verifies bounded query identity, not exhaustive species or family completeness.'
  support: context_only
  search_scope: Database UniProtKB; exact query URL https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue%20AND%20taxonomy_id%3A32053%20AND%20%28gene_exact%3ApsbA%20OR%20gene_exact%3ApsbD%29&format=json&size=100;
    fetched 2026-11-03T06:48:22.120864Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-photosystem-agent-pdb-1jb0
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1JB0
  locator: Native 1JB0 deposition identity, source organism and SIFTS chain mappings
  accessed_at: '2026-11-03T06:48:22.211984Z'
  snapshot_sha256: 0607776f9e475c0c64d3ebbc906824cb850d0a5c61028e73d48995c2b4419cf2
  summary: PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field
    retains Synechococcus elongatus tax32046. Crystal preparation and source name
    cannot establish identity with PCC7942 merely by shared spelling.
  support: context_only
- evidence_id: plaque-photosystem-agent-pdb-1jb0-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1JB0/1
  locator: Native 1JB0 deposition identity, source organism and SIFTS chain mappings
  accessed_at: '2026-11-03T06:48:22.294419Z'
  snapshot_sha256: ac0514be380db893644429e45e2ce955f898de4c33cc71c216ca10a1304916c6
  summary: PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field
    retains Synechococcus elongatus tax32046. SIFTS maps PsaA to P0A405 (current BP-1
    tax197221), creating an important legacy-source versus current-mapping conflict.
  support: context_only
- evidence_id: plaque-photosystem-agent-pdb-1jb0-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1JB0/2
  locator: Native 1JB0 deposition identity, source organism and SIFTS chain mappings
  accessed_at: '2026-11-03T06:48:22.316446Z'
  snapshot_sha256: fced0ac178555a456f2e6d2c02e7260147d3b8e8ef997229325d0aedff3a7401
  summary: PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field
    retains Synechococcus elongatus tax32046. SIFTS maps PsaB to P0A407 (current BP-1
    tax197221); the record P0A408 is not the exact deposited chain mapping.
  support: context_only
- evidence_id: plaque-photosystem-agent-pdb-1jb0-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1JB0/3
  locator: Native 1JB0 deposition identity, source organism and SIFTS chain mappings
  accessed_at: '2026-11-03T06:48:22.382256Z'
  snapshot_sha256: b1d8c4528247652d63b49586d13ee8e77f5e27020417dd0b281fc79889d9f099
  summary: PDB1JB0 is the Jordan2001 PSI deposition; author source-organism field
    retains Synechococcus elongatus tax32046. Entity3 is the separate PsaC iron-sulfur-center
    subunit; SIFTS maps P0A415.
  support: context_only
- evidence_id: plaque-access-kamiya2003-jats
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140893/fullTextXML
  locator: Source transport/access attempt
  accessed_at: '2026-11-03T06:48:22.405401Z'
  snapshot_sha256: cda3b4f0638f5b563686a0a2ee163221ecebf40e0ce7f262b37c5a1e43a6289c
  summary: Actual curl HTTP 500, exit 0; 149 bytes. This attempt did not provide a
    usable scientific article body and supports no biological absence inference.
  support: context_only
- evidence_id: plaque-access-kawakami2009-jats
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2688974/fullTextXML
  locator: Source transport/access attempt
  accessed_at: '2026-11-03T06:48:22.465329Z'
  snapshot_sha256: c5306c72ae56bf6e0ddefd48d22fa3e9660671ddee79a05da831ffc92b10abaf
  summary: Actual curl HTTP 500, exit 0; 150 bytes. This attempt did not provide a
    usable scientific article body and supports no biological absence inference.
  support: context_only
- evidence_id: plaque-adapter-datasets
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned organism/dataset catalogue
  accessed_at: '2026-11-03T06:48:23.013689Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Catalogue contains e_coli/precise_mg1655 and s_elongatus/elprecise300.
    It lists no Thermosynechococcus vestitus/elongatus BP-1 or Thermostichus vulcanus
    dataset. Absence is limited to this retrieved catalogue, not biology.
  support: context_only
- evidence_id: plaque-adapter-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise_mg1655/meta
  locator: strains, dataset, sample/condition and publication fields
  accessed_at: '2026-11-03T06:48:23.099673Z'
  snapshot_sha256: 0722bb1ccec69ac0d7ebc2784fc7cbdf1cfe612d739b8fb66d54a441a8b3db91
  summary: E.coli precise_mg1655 is MG1655 with 586 samples, 281 conditions and 115
    components. publication_url is null. This is a bounded K-12 descendant context,
    not every strain or FDH/nitrate-reductase class.
  support: context_only
- evidence_id: plaque-adapter-search-fdnG
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdnG&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.146958Z'
  snapshot_sha256: 30002e999162bc8a0a05057d47e5557ca533cb979d136f52a57858304aa9d33b
  summary: 'Returned gene keys: [(''b1474'', ''fdnG'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdnG&limit=50;
    fetched 2026-11-03T06:48:23.146958Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-fdnH
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdnH&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.224458Z'
  snapshot_sha256: c43d2173b2652eaf4f86334dbc91cd4572e41803e2eeaf9cd2557beebd190d89
  summary: 'Returned gene keys: [(''b1475'', ''fdnH'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdnH&limit=50;
    fetched 2026-11-03T06:48:23.224458Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-fdnI
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdnI&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.282707Z'
  snapshot_sha256: 30c5e6695bb7c140a3d53048cd82c84a0d5a0bb27355432c7d7071f2311eb237
  summary: 'Returned gene keys: [(''b1476'', ''fdnI'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdnI&limit=50;
    fetched 2026-11-03T06:48:23.282707Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-fdoG
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdoG&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.345912Z'
  snapshot_sha256: 28ce60b6c6da7284d1df23f8b09c639986e0d1742311e053e79c9e877625ee4b
  summary: 'Returned gene keys: [(''b3894'', ''fdoG'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdoG&limit=50;
    fetched 2026-11-03T06:48:23.345912Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-fdoH
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdoH&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.402722Z'
  snapshot_sha256: 1fe4610f1a504bf9bcc47bff7d7a88bb302b46606d155778383fe3888e051248
  summary: 'Returned gene keys: [(''b3893'', ''fdoH'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdoH&limit=50;
    fetched 2026-11-03T06:48:23.402722Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-fdoI
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdoI&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.463713Z'
  snapshot_sha256: 5ad46bbbb2c8c3a1718f57ca9ed3ec51ed944359a57b33decd322da0616c9d3a
  summary: 'Returned gene keys: [(''b3892'', ''fdoI'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=fdoI&limit=50;
    fetched 2026-11-03T06:48:23.463713Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-narG
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=narG&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.523910Z'
  snapshot_sha256: 9b6f06c5042dc285f8b29cc63b077621cf33836414d6d468f5f442ab0b548b08
  summary: 'Returned gene keys: [(''b1224'', ''narG'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=narG&limit=50;
    fetched 2026-11-03T06:48:23.523910Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-narH
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=narH&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.586252Z'
  snapshot_sha256: 52fe5dcedf8c6f4d73f5bd0593bbb9d06bcb08842c6bf920e1ab39a009d089eb
  summary: 'Returned gene keys: [(''b1225'', ''narH'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=narH&limit=50;
    fetched 2026-11-03T06:48:23.586252Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-search-narI
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=narI&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:48:23.663161Z'
  snapshot_sha256: f76d785c11aaa27209ca35c714378d5c4b06e2fdfa9c19acc6c4be498082558f
  summary: 'Returned gene keys: [(''b1227'', ''narI'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=e_coli&dataset=precise_mg1655&query=narI&limit=50;
    fetched 2026-11-03T06:48:23.663161Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-gene-modules-fdnG
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1474/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.357086Z'
  snapshot_sha256: 23f46fe5a836e48d67a0bcd00ab0846cbfe92fbaa167b6f50fc7a01eee760a97
  summary: 'Thresholded memberships (component, name, weight): [(67, ''FDH-N_NRA'',
    ''0.123152544''), (69, ''Fnr-1'', ''0.093500904'')]. Unselected weights are below
    dataset thresholds, not evidence against physical membership or biological presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-fdnH
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1475/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.358344Z'
  snapshot_sha256: 50586a5da28fca2292643b8e398298dded5e6e4251aa41e38ad414f1a8eeeacd
  summary: 'Thresholded memberships (component, name, weight): [(67, ''FDH-N_NRA'',
    ''0.114101792'')]. Unselected weights are below dataset thresholds, not evidence
    against physical membership or biological presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-fdnI
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1476/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.359495Z'
  snapshot_sha256: e6bd1d0aed3c8299e4df8ed81ae40c7a0a7804b41504f1828de75e5160a055f3
  summary: 'Thresholded memberships (component, name, weight): []. Unselected weights
    are below dataset thresholds, not evidence against physical membership or biological
    presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-fdoG
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3894/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.360822Z'
  snapshot_sha256: 4e73a0cbc92abbdfb4d09f7e32a39ccbdcbf97877634f5b9ecdab050e371cd02
  summary: 'Thresholded memberships (component, name, weight): []. Unselected weights
    are below dataset thresholds, not evidence against physical membership or biological
    presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-fdoH
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3893/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.420062Z'
  snapshot_sha256: 5a6266bbe965d34521436e43273339557e24401b103797d9878c018c0f9eed1a
  summary: 'Thresholded memberships (component, name, weight): []. Unselected weights
    are below dataset thresholds, not evidence against physical membership or biological
    presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-fdoI
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b3892/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.430209Z'
  snapshot_sha256: cb35d1ec4a07e09038912f188af648deccb838ddfaa2e696a64ce0fe370b1b0c
  summary: 'Thresholded memberships (component, name, weight): []. Unselected weights
    are below dataset thresholds, not evidence against physical membership or biological
    presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-narG
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1224/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.431117Z'
  snapshot_sha256: af1557977f289d19580ea011c89e325cac78f95f290ae55754c15c4c4f1a521c
  summary: 'Thresholded memberships (component, name, weight): [(67, ''FDH-N_NRA'',
    ''0.266744246''), (69, ''Fnr-1'', ''0.089845386'')]. Unselected weights are below
    dataset thresholds, not evidence against physical membership or biological presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-narH
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1225/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.432331Z'
  snapshot_sha256: ed24dea30a0449b475eb2d23a6238e1bd5e6f05a804d11346a722116753b75e0
  summary: 'Thresholded memberships (component, name, weight): [(67, ''FDH-N_NRA'',
    ''0.240452882''), (21, ''N Reduction'', ''0.110831747'')]. Unselected weights
    are below dataset thresholds, not evidence against physical membership or biological
    presence.'
  support: context_only
- evidence_id: plaque-adapter-gene-modules-narI
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise_mg1655/b1227/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:49:27.476248Z'
  snapshot_sha256: e6eb2619e61ae07816edea03226e39bbb9d1f79b3a8e7644c9f0d8d6d4457e22
  summary: 'Thresholded memberships (component, name, weight): [(67, ''FDH-N_NRA'',
    ''0.220000914''), (21, ''N Reduction'', ''0.123743046'')]. Unselected weights
    are below dataset thresholds, not evidence against physical membership or biological
    presence.'
  support: context_only
- evidence_id: plaque-adapter-syn-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/s_elongatus/elprecise300/meta
  locator: strains, publication_url and dataset fields
  accessed_at: '2026-11-03T06:49:27.482035Z'
  snapshot_sha256: ab1cea70cad9bdb6214c6350d7a8bf92ddddf13bdc928620cbc5ba76badc947f
  summary: S.elongatus elprecise300 is specifically PCC7942, with 300 samples, 57
    modules and DOI10.1073/pnas.2410492121. It is not the thermophilic Jordan BP-1
    or Umena vulcanus preparation.
  support: context_only
- evidence_id: plaque-adapter-syn-search-psaA
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psaA&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:49:27.485331Z'
  snapshot_sha256: 7dc6bfe7c52ae3d4b1de3aae4ae68f3c6a5dbe28eed8f25ac6982dd568717e48
  summary: 'Returned gene keys: [(''Synpcc7942_2049'', ''psaA'')]. Module-name hits:
    []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact
    Thermostichus vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psaA&limit=50;
    fetched 2026-11-03T06:49:27.485331Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-syn-search-psaB
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psaB&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:49:27.489308Z'
  snapshot_sha256: 885224f69e7af8e68ec3a0343479489b03250c51666925b18587f5b3cc51d1ff
  summary: 'Returned gene keys: [(''Synpcc7942_2048'', ''psaB'')]. Module-name hits:
    []. Follow-up checks are separate; fuzzy psbA/psbD paralog hits are not exact
    Thermostichus vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psaB&limit=50;
    fetched 2026-11-03T06:49:27.489308Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-syn-search-psbA
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psbA&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:49:27.530773Z'
  snapshot_sha256: fb537cffc8aa148535bfcc947a4d1e0b6719fadae81d815a6365ae5d38c8dc69
  summary: 'Returned gene keys: [(''Synpcc7942_0893'', ''psbA3''), (''Synpcc7942_1389'',
    ''psbA2''), (''Synpcc7942_0424'', ''psbA1'')]. Module-name hits: []. Follow-up
    checks are separate; fuzzy psbA/psbD paralog hits are not exact Thermostichus
    vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psbA&limit=50;
    fetched 2026-11-03T06:49:27.530773Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-syn-search-psbD
  kind: search
  reference: https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psbD&limit=50
  locator: Bounded source gene/module search
  accessed_at: '2026-11-03T06:49:27.544138Z'
  snapshot_sha256: d41e9a3adbb83a814ca4bd1d582cc84ea2da3016b5f804a76a3927a0225704af
  summary: 'Returned gene keys: [(''Synpcc7942_0655'', ''psbD1''), (''Synpcc7942_1637'',
    ''psbD2'')]. Module-name hits: []. Follow-up checks are separate; fuzzy psbA/psbD
    paralog hits are not exact Thermostichus vulcanus examples.'
  support: context_only
  search_scope: Database iModulonDB; exact query URL https://imodulondb.org/api/search?organism=s_elongatus&dataset=elprecise300&query=psbD&limit=50;
    fetched 2026-11-03T06:49:27.544138Z; first response page only, limit/size exactly
    as encoded (50 for iModulonDB, 100 or 500 for UniProtKB); no negative biological
    inference.
- evidence_id: plaque-adapter-summary-21
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/21
  locator: Native component annotation, threshold and member counts; generated narrative
    excluded
  accessed_at: '2026-11-03T06:50:19.709232Z'
  snapshot_sha256: 59b55aae981f40f821a534fe42ac19cc36d9b25c10de17ac627f3a44b0adb850
  summary: 'Module 21 (N Reduction), 26 thresholded genes, threshold 0.080605467;
    native annotation: electron transfer via nitrate reductases. AI-generated summary
    and activity-matrix inference excluded. Expression context only.'
  support: context_only
- evidence_id: plaque-adapter-members-21
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/21/genes?limit=50
  locator: First 50 requested thresholded member rows
  accessed_at: '2026-11-03T06:50:19.710374Z'
  snapshot_sha256: 4b545a257cb6632f413f467f00e6eca00b2144786f846193bdcd5fcc2db7bca8
  summary: Inspected all 26 returned rows; relevant named members [('b1227', 'narI'),
    ('b1225', 'narH')]. No physical complex or mechanism is inferred.
  support: context_only
- evidence_id: plaque-adapter-summary-67
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/67
  locator: Native component annotation, threshold and member counts; generated narrative
    excluded
  accessed_at: '2026-11-03T06:50:19.710562Z'
  snapshot_sha256: 81fc2bf8ca4ab91f1cbc4f998113bcf826e9778f7f599e84a3dee41836b9c531
  summary: 'Module 67 (FDH-N_NRA), 11 thresholded genes, threshold 0.099373409; native
    annotation: anaerobic growth on nitrate; formate-to-nitrate electron transfer
    via formate dehydrogenase N and nitrate reductase A. AI-generated summary and
    activity-matrix inference excluded. Expression context only.'
  support: context_only
- evidence_id: plaque-adapter-members-67
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/67/genes?limit=50
  locator: First 50 requested thresholded member rows
  accessed_at: '2026-11-03T06:50:19.712296Z'
  snapshot_sha256: de19da7af6ba7df052db32e851e72f8d44f240da7b468ec18f7b9eeed49b5906
  summary: Inspected all 11 returned rows; relevant named members [('b1224', 'narG'),
    ('b1225', 'narH'), ('b1227', 'narI'), ('b1474', 'fdnG'), ('b1475', 'fdnH')]. No
    physical complex or mechanism is inferred.
  support: context_only
- evidence_id: plaque-adapter-summary-69
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/69
  locator: Native component annotation, threshold and member counts; generated narrative
    excluded
  accessed_at: '2026-11-03T06:50:19.780875Z'
  snapshot_sha256: 63b4e4dd026d2f0655de92c63ddf4419d189f26a42d6a33d3d5b0647c0d68036
  summary: 'Module 69 (Fnr-1), 33 thresholded genes, threshold 0.070397694; native
    annotation: transition from aerobic to anaerobic growth. AI-generated summary
    and activity-matrix inference excluded. Expression context only.'
  support: context_only
- evidence_id: plaque-adapter-members-69
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise_mg1655/69/genes?limit=50
  locator: First 50 requested thresholded member rows
  accessed_at: '2026-11-03T06:50:19.782937Z'
  snapshot_sha256: 2e9f3185b9de9e062f2c5ce7e5ea8cb1c8c3beeea87c74c63121a4350e43d711
  summary: Inspected all 33 returned rows; relevant named members [('b1474', 'fdnG'),
    ('b1224', 'narG')]. No physical complex or mechanism is inferred.
  support: context_only
- evidence_id: plaque-adapter-syn-modules-psaA
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2049/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:50:19.792988Z'
  snapshot_sha256: 0f0efec038067d4c2e41f6b6d825f909f836e06a77cb16d460c866e76aac4073
  summary: 'Thresholded memberships (component, name, weight): [(38, ''Photosystems'',
    ''0.076674881'')]. Unselected weights are below dataset thresholds, not evidence
    against physical membership or biological presence.'
  support: context_only
- evidence_id: plaque-adapter-syn-modules-psaB
  kind: database
  reference: https://imodulondb.org/api/genes/s_elongatus/elprecise300/Synpcc7942_2048/imodulons
  locator: Dataset-specific gene weights and is_in_imodulon flags
  accessed_at: '2026-11-03T06:50:19.802955Z'
  snapshot_sha256: 9e68451cb44fa5f53d40e62cf9a87f406a04b468741d2ba70af10c41910c4181
  summary: 'Thresholded memberships (component, name, weight): [(38, ''Photosystems'',
    ''0.089138166'')]. Unselected weights are below dataset thresholds, not evidence
    against physical membership or biological presence.'
  support: context_only
- evidence_id: plaque-adapter-syn-publication
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A10.1073%2Fpnas.2410492121
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:50:19.837038Z'
  snapshot_sha256: 89fe11111996e2a22dfec03e96e673342078068e122add4b9d45a91e19ca3d73
  summary: Verified [('39269777', 'Machine learning reveals the transcriptional regulatory
    network and circadian dynamics of &lt;i&gt;Synechococcus elongatus&lt;/i&gt; PCC
    7942.', '10.1073/pnas.2410492121')]. Read abstract tier only in this response.
  support: context_only
- evidence_id: plaque-photosystem-jordan-http
  kind: primary_source
  reference: http://dosequis.colorado.edu/Courses/InsaneMembrane/papers/PS1-PSII-LHC%27s/photosystem1.pdf
  locator: Genuine PDF pp909-916, especially polypeptide subunits p911 and electron
    transfer p913
  accessed_at: '2026-11-03T06:50:19.849745Z'
  snapshot_sha256: 9c4721ce9a022343cb7ec78458b73961c0858c73b82bf981f1b45fcc5447149a
  summary: Public HTTP mirror supplied the readable Jordan2001 PDF after HTTPS certificate
    failure. Main text and captions support PsaA/PsaB and antenna architecture; PsaC
    carries FA/FB, whereas FX is jointly ligated by PsaA/PsaB. Thermophilic historical
    source naming is kept distinct from current taxonomy. No raw diffraction or supplemental
    reanalysis.
  support: context_only
- evidence_id: plaque-semchonok2021-pdf
  kind: primary_source
  reference: https://par.nsf.gov/servlets/purl/10308929
  locator: Author manuscript PDF, introduction p2, paragraph identifying Jordan2001
    PDB1JB0
  accessed_at: '2026-11-03T06:51:25.698600Z'
  snapshot_sha256: 69f2bb454e905ece183fc17e4ac47ce3b9ac73742961970ed63b6b7de658fd5a
  summary: This primary structural paper explicitly identifies the earlier 1JB0 PSI
    preparation as thermophilic Thermosynechococcus elongatus BP-1. This is comparative/background
    attribution within that paper, not a new isolation experiment on the 2001 material.
  support: context_only
- evidence_id: plaque-taxonomy-bp1
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/197221
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:51:25.699681Z'
  snapshot_sha256: f30dcc28777baef3bbc3b81cbc0c94af4d350e9043dfb33913f0aab1b50601d0
  summary: Authority identifies 197221 as Thermosynechococcus vestitus BP-1; lineage
    Bacteria; Bacillati; Cyanobacteriota; Cyanophyceae; Acaryochloridales; Thermosynechococcaceae;
    Thermosynechococcus; ; historical names ['Thermosynechococcus elongatus BP-1:equivalent
    name', 'Thermosynechococcus elongatus IAM M-273:equivalent name', 'Thermosynechococcus
    elongatus NIES-2133:equivalent name'].
  support: context_only
- evidence_id: plaque-taxonomy-pcc7942
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: taxId/scientificName/lineage/otherNames
  accessed_at: '2026-11-03T06:51:25.701135Z'
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
  summary: Authority identifies 1140 as Synechococcus elongatus PCC 7942 = FACHB-805;
    lineage Bacteria; Bacillati; Cyanobacteriota; Cyanophyceae; Synechococcales; Synechococcaceae;
    Synechococcus; ; historical names ['Synechococcus sp. PCC 7942:equivalent name',
    'Synechococcus elongatus PCC 7942:includes', 'Synechococcus sp. FACHB-805:includes',
    'Synechococcus sp. IAM M-200:synonym', 'Synechococcus leopoliensis strain PCC
    7942:synonym', 'Synechococcus leopoliensis UTEX 2434:synonym', 'Anacystis nidulans
    R2:synonym'].
  support: context_only
- evidence_id: plaque-adapter-syn-summary-38
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38
  locator: Native component annotation, threshold and member counts; generated narrative
    excluded
  accessed_at: '2026-11-03T06:51:25.702189Z'
  snapshot_sha256: 7236e5234640b6a379fa25dc2ac44375ba96a07d69f7a020e06741bcd94c0965
  summary: 'Module 38 (Photosystems), 44 thresholded genes, threshold 0.063088206;
    native annotation: Photosystems proteins. AI-generated summary and activity-matrix
    inference excluded. Expression context only.'
  support: context_only
- evidence_id: plaque-adapter-syn-members-38
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_elongatus/elprecise300/38/genes?limit=50
  locator: First 50 requested thresholded member rows
  accessed_at: '2026-11-03T06:51:25.753723Z'
  snapshot_sha256: 4c8790c372c142c3fb6c0b72582164af9b1d29e1bb180245ce2b49c493b8b9dd
  summary: Inspected all 44 returned rows; relevant named members [('Synpcc7942_2048',
    'psaB'), ('Synpcc7942_2049', 'psaA')]. No physical complex or mechanism is inferred.
  support: context_only
- evidence_id: plaque-adapter-syn-primary
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11420160/fullTextXML
  locator: 'PMC11420160 JATS body: introduction, photosynthesis section and ICA methods'
  accessed_at: '2026-11-03T06:51:25.809340Z'
  snapshot_sha256: e9428e75ac5db3beaa87f41d6a68d2c8e184ef38f34d46f6c1bed9fdf01a4a53
  summary: Read the actual paper body for PCC7942 scope and computational Photosystems-module
    provenance. ICA on 300 RNA-seq profiles identifies coexpression modules; this
    is not an assembly/localization experiment or a BP-1 dataset.
  support: context_only
- evidence_id: plaque-semchonok2021-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A10.1016%2Fj.xplc.2021.100248
  locator: EuropePMC exact query citation identity and abstracts; no body via this
    endpoint
  accessed_at: '2026-11-03T06:51:26.328968Z'
  snapshot_sha256: 3424ae631372aac4e678c39a555500a84f0ec9fd705ef3195ac7d2a183709ebd
  summary: Verified [('35059628', 'Cryo-EM structure of a tetrameric photosystem I
    from <i>Chroococcidiopsis</i> TS-821, a thermophilic, unicellular, non-heterocyst-forming
    cyanobacterium.', '10.1016/j.xplc.2021.100248')]. Read abstract tier only in this
    response.
  support: context_only
- evidence_id: plaque-taxonomy-PSI-P0A405
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A405.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:52:11.693516Z'
  snapshot_sha256: 3f75a6d7039c196dbb903666fd04356a55d7a35713c6ae2aa897fd6ac5586d8a
  summary: 'P0A405: UniProtKB reviewed (Swiss-Prot); taxon 197221 (Thermosynechococcus
    vestitus (strain NIES-2133 / IAM M-273 / BP-1)); genes [''psaA'']. Native annotation
    was inspected; reviewed status does not itself prove experimental membership.
    These are the SIFTS-linked 1JB0 chains, distinct from the record identity-only
    P0A406/P0A408 examples.'
  support: context_only
- evidence_id: plaque-taxonomy-PSI-P0A407
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A407.json
  locator: Reviewed entry identity, genes, organism, subunit/function/cofactor/location
    annotations and evidence attribution
  accessed_at: '2026-11-03T06:52:11.694605Z'
  snapshot_sha256: 3433cedc457b54b8480127e24ca8f3f8d213529d7f6c8955bcf662eff64d4c92
  summary: 'P0A407: UniProtKB reviewed (Swiss-Prot); taxon 197221 (Thermosynechococcus
    vestitus (strain NIES-2133 / IAM M-273 / BP-1)); genes [''psaB'']. Native annotation
    was inspected; reviewed status does not itself prove experimental membership.
    These are the SIFTS-linked 1JB0 chains, distinct from the record identity-only
    P0A406/P0A408 examples.'
  support: context_only
- evidence_id: plaque-jormakka-browser-main
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: ResearchGate browser text lines48-980; article beginning at74, overall
    structure and electron-transfer sections
  accessed_at: '2026-11-03T06:53:03Z'
  snapshot_sha256: 6c284cb14532b7ecdc286aa4a6c582ff27abc397a0972713399c57aea875dbf3
  summary: Author-uploaded primary article text inspected for E.coli FdnGHI architecture
    and redox relay. This is preserved browser text, not the failed curl403 article
    response; HQNO/proton-pathway inference remains qualified.
  support: partial
- evidence_id: plaque-jormakka-browser-later
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: ResearchGate browser text lines956-1518 plus beginning; ignore failed Jordan
    open entries
  accessed_at: '2026-11-03T06:49:43Z'
  snapshot_sha256: 151731054f0c0e1875fe61563ae6a2fbf8d0ff65adbeab1a076219cdd8e68d00
  summary: Inspected gamma-subunit and quinone/proton pathway discussion; direct coordinates
    and figure pixels not reanalyzed. Native curl403 is retained separately and not
    treated as paper access.
  support: partial
- evidence_id: plaque-jormakka-browser-beta
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: ResearchGate browser text lines524-1137; ignore separate Jordan intro response
  accessed_at: '2026-11-03T06:48:54Z'
  snapshot_sha256: 878ee3f5f7cb4b646fddb98807104e30b43c9caa61d53a64a8c3071b5964ea48
  summary: Inspected alpha/beta/gamma subunit discussion and captions. No supplementary
    Methods or direct proton-flux measurement audit.
  support: partial
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  locator: Whole current maintained record
  accessed_at: '2026-11-03T06:55:22.031275Z'
  snapshot_sha256: 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e
  summary: Full current record read; current SHA 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e.
    No scientific fields edited.
  support: context_only
- evidence_id: plaque-original-0
  kind: prior_review
  reference: reviews/structured/20261021T100134Z-formate-dehydrogenase-complex-audit/review.yaml
  locator: Original whole YAML and exact current native validation/render
  accessed_at: '2026-11-03T06:55:22.031373Z'
  snapshot_sha256: f4cfd4f49344849a40137038c91693e4b928b4f5a7aa47beb7601f3e6ce77d53
  summary: Historical immutable review; target hash independently checked at its declared
    source revision. Findings and access tiers reassessed, not accepted merely because
    validation passes.
  support: context_only
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/energy_complex/nitrate_reductase_complex.yaml
  locator: Whole current maintained record
  accessed_at: '2026-11-03T06:55:22.031600Z'
  snapshot_sha256: ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459
  summary: Full current record read; current SHA ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459.
    No scientific fields edited.
  support: context_only
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261021T100137Z-nitrate-reductase-complex-audit/review.yaml
  locator: Original whole YAML and exact current native validation/render
  accessed_at: '2026-11-03T06:55:22.031631Z'
  snapshot_sha256: 9f96c6bc78113211504b025b7e9e1db8cbe347319ba059226c181a55e22cf5aa
  summary: Historical immutable review; target hash independently checked at its declared
    source revision. Findings and access tiers reassessed, not accepted merely because
    validation passes.
  support: context_only
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/energy_complex/photosystem.yaml
  locator: Whole current maintained record
  accessed_at: '2026-11-03T06:55:22.031859Z'
  snapshot_sha256: c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8
  summary: Full current record read; current SHA c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8.
    No scientific fields edited.
  support: context_only
- evidence_id: plaque-original-2
  kind: prior_review
  reference: reviews/structured/20261021T100138Z-photosystem-audit/review.yaml
  locator: Original whole YAML and exact current native validation/render
  accessed_at: '2026-11-03T06:55:22.031893Z'
  snapshot_sha256: 9276bcea3a332e256fc57d9a65cae0cc50f347925aa0748f3f7c4a3659e62bc5
  summary: Historical immutable review; target hash independently checked at its declared
    source revision. Findings and access tiers reassessed, not accepted merely because
    validation passes.
  support: context_only
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: ComponentTypeEnum, EssentialityEnum and graph representation
  accessed_at: '2026-11-03T06:55:22.032082Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Grouped subcomplexes, protein instances, assembly necessity and catalytic
    roles remain distinct.
  support: context_only
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope, supported paths and evidence contract
  accessed_at: '2026-11-03T06:55:22.032125Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Membership/activity summaries do not independently establish a represented
    causal route.
  support: context_only
- evidence_id: plaque-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Identity and source/evidence scope
  accessed_at: '2026-11-03T06:55:22.032153Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Source-specific taxon, molecular role and condition must not be generalized
    silently; no optional-empty-field finding.
  support: context_only
- evidence_id: plaque-adapter-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks
  accessed_at: '2026-11-03T06:55:22.032187Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named genes/proteins trigger applicability assessment; lack of expression
    claims is not an exemption. Unavailable runner may use inspected source fallback.
  support: context_only
- evidence_id: plaque-energy-category-prior
  kind: prior_review
  reference: reviews/structured/20261023T230504Z-energy-complex-category-review/review.yaml
  locator: Exact finding F1 and affected target GO0009521
  accessed_at: '2026-11-03T06:55:22.049326Z'
  snapshot_sha256: 07773b203fe7fea9d6b3fb750e634e896ea0e7c05e6678f62b6a096dbd0d093b
  summary: The sole affected target of F1 is this photosystem; reviewing this finding
    does not repeat or certify all37 category targets.
  support: context_only
- evidence_id: plaque-historical-issue2420
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2420
  locator: Root-retrieved CLOSED issue body and resolution comment, independently
    reread
  accessed_at: '2026-11-03T06:55:22.049396Z'
  snapshot_sha256: f459573d3815b7672af3a500c41e272d14c3c4fa07951d6e9fa74a97f4ebc57c
  summary: Already closed grouped issue includes the photosystem core-type finding.
    Resolution comment cites99e590eb7afb0e8251f6e81183e59ca1119987b9. This PR does
    not claim that prior record correction as new work or resolve other grouped targets.
  support: context_only
- evidence_id: plaque-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-plaque/original-validation.json
  locator: Actual native validate/render receipts and historical/current hashes for
    three assigned originals
  accessed_at: '2026-11-03T06:55:22.049444Z'
  snapshot_sha256: 2c6cd9802a785c97766a3694511ff910f1460a70d1691462c9f40989f357f7d0
  summary: All three validate commands exit0, all native Markdown renders match exactly,
    all historical target SHA256s match declared input; formate/nitrate current bytes
    unchanged and photosystem stale delta independently assessed.
  support: supports
- evidence_id: plaque-native-formate_dehydrogenase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/formate_dehydrogenase_complex-uniprot-verify-receipt.json
  locator: Actual root-run native command; independently inspected receipt and complete
    stdout
  accessed_at: '2026-11-03T06:47:05.784099Z'
  snapshot_sha256: 2012dbb3a5aa86c85948f8ff96938adfb59b5ef0db96a32aa6ce8fceca2337d8
  summary: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/formate_dehydrogenase_complex.yaml',
    '--verify'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA
    3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. Identity/xref
    coverage does not prove scientific mechanism.
  support: supports
- evidence_id: plaque-native-formate_dehydrogenase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/formate_dehydrogenase_complex-uniprot-causal-receipt.json
  locator: Actual root-run native command; independently inspected receipt and complete
    stdout
  accessed_at: '2026-11-03T06:47:06.246741Z'
  snapshot_sha256: 97ecf61a5bd96b443f29228b0f131e657bd3c9f6b2876932e0cb7874c9720212
  summary: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/formate_dehydrogenase_complex.yaml',
    '--causal-graphs'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f;
    stdoutSHA 0d1606e67e7adec4d9a42a5ba7bc7c8f70ecf7a91349686b0cb351992185d8f7. Identity/xref
    coverage does not prove scientific mechanism.
  support: supports
- evidence_id: plaque-native-nitrate_reductase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/nitrate_reductase_complex-uniprot-verify-receipt.json
  locator: Actual root-run native command; independently inspected receipt and complete
    stdout
  accessed_at: '2026-11-03T06:47:07.452772Z'
  snapshot_sha256: f96bac2e55f1df86d115be2ee90b1e74fffeedb029a157e9c9b89064c1adf1a9
  summary: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/nitrate_reductase_complex.yaml',
    '--verify'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA
    3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. Identity/xref
    coverage does not prove scientific mechanism.
  support: supports
- evidence_id: plaque-native-nitrate_reductase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/nitrate_reductase_complex-uniprot-causal-receipt.json
  locator: Actual root-run native command; independently inspected receipt and complete
    stdout
  accessed_at: '2026-11-03T06:47:07.917806Z'
  snapshot_sha256: 2b437123ace424de6651a1434e3040a2ac61b5595a96c29747fdcab0ed4b9fbe
  summary: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/nitrate_reductase_complex.yaml',
    '--causal-graphs'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f;
    stdoutSHA af74368d55b6de50d4008ce1b5142d396e34df4b1cfb8605bbac6ab3494ea707. Identity/xref
    coverage does not prove scientific mechanism.
  support: supports
- evidence_id: plaque-native-photosystem-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/photosystem-uniprot-verify-receipt.json
  locator: Actual root-run native command; independently inspected receipt and complete
    stdout
  accessed_at: '2026-11-03T06:47:09.341194Z'
  snapshot_sha256: 72d5b088e146074b05412d11da8dce6e0a979e91c99c0df66adfe561b564143b
  summary: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/photosystem.yaml',
    '--verify'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f; stdoutSHA
    3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. Identity/xref
    coverage does not prove scientific mechanism.
  support: supports
- evidence_id: plaque-native-photosystem-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/photosystem-uniprot-causal-receipt.json
  locator: Actual root-run native command; independently inspected receipt and complete
    stdout
  accessed_at: '2026-11-03T06:47:09.814155Z'
  snapshot_sha256: 59ada4d4feda227424ec75d8da39c294790db82eee3602ad19d4c5725f263497
  summary: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/energy_complex/photosystem.yaml',
    '--causal-graphs'] exit0 at source head d7ee610a5d142b5961a6057e22437aabb68f191f;
    stdoutSHA 53824867a2aae786f4735345cb9c129de0b95944ab99f592d60014a87fcd2a37. Identity/xref
    coverage does not prove scientific mechanism.
  support: supports
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0005774,GO:0005775,GO:0007035,GO:0016469,GO:0016471,GO:0033176,GO:0033177,GO:0033178,GO:0033179,GO:0033180,GO:0046961,GO:0090533,GO:1904949
  locator: 'QuickGO exact fifteen requested GO term objects: definitions, labels and
    returned parent/child relationships; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/go.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/go.receipt.json'
  accessed_at: '2026-11-03T06:46:59.816136Z'
  summary: The exact generic complex/sector identities and their parent and part relationships
    resolve. GO:0033176 includes organelle and plasma-membrane V-ATPases; GO:0000220/0000221
    are vacuolar sectors. Generic V0 GO:0033179 describes six or more c subunits,
    not an invariant decamer. Generic V1 GO:0033180 gives A3B3, D/F and C/E/G/H, without
    the added three-stalk detail. Function/compartment labels also resolve; this is
    ontology authority, not experimental confirmation of every appended statement.
  support: supports
  snapshot_sha256: fee810a704c77d2e075ad5d9aeca21bafad13836fae70e7b0aef5f76f718ccbf
- evidence_id: micro-kane2006-secondary
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1393255/?pdf=render
  locator: 'Kane 2006, Introduction/Structure HTML paragraphs P7-P29, assembly/targeting/regulation
    P43-P64; paragraph offsets are zero-based in the retained derived text; response
    and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/kane2006.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/kane2006.receipt.json'
  accessed_at: '2026-11-03T06:46:59.669212Z'
  summary: Secondary review sections were read. They distinguish S. cerevisiae Vph1
    vacuolar and Stv1 Golgi/endosomal isoforms, V1 and V0 subunits, central rotor/c-ring
    versus stationary elements, and activity/assembly/targeting phenotypes. Its Figure
    1 caption retains older one/two-peripheral-stalk models; it is not a source for
    the later three-stalk result. Assembly routes and subunit-e placement retain uncertainty.
    Figure captions were read, not image pixels. Prose summaries are context, not
    a fresh primary experiment.
  support: context_only
  snapshot_sha256: 3ff8128da35aec1056c7d06333b10f13b0d3883de865de39edf9f9f12229709f
- evidence_id: micro-zhao2015-abstract
  kind: primary_source
  reference: https://www.nature.com/articles/nature14365
  locator: 'Zhao et al. 2015 Nature, DOI:10.1038/nature14365; accessible abstract
    HTML P7, subscription notice P8 and deposition-accession listing P20; response
    and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/zhao2015.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/zhao2015.receipt.json'
  accessed_at: '2026-11-03T06:46:59.669526Z'
  summary: Fresh native publisher response exposes the abstract and gates the main
    text. The abstract explicitly states S. cerevisiae cryo-EM three rotational states,
    ten proteolipids in its c-ring, three peripheral stalks in eukaryotic V-ATPase,
    and central rotor versus stalks that prevent rotation of the membrane region.
    These results support the numerical/taxon and rotor/stator findings. No current
    main-text, Methods, figure-pixel, strain/preparation, detergent, nucleotide-condition
    or subunit-e-loss verification is claimed.
  support: partial
  snapshot_sha256: 3ca253e22160bde02daa0e1f3db0f7c41a603e2349a45bb2b184c9781426970f
- evidence_id: micro-li2009-secondary
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2906225.1/PMC2906225.1.xml
  locator: 'Li and Kane 2009, JATS sections S15-S18 / body paragraphs P27-P34 (V-ATPase
    and vacuolar pH regulation); response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/li2009.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/li2009.receipt.json'
  accessed_at: '2026-11-03T06:46:59.669605Z'
  summary: Read secondary context distinguishes V1 ATP hydrolysis and V0 proton transport,
    14 yeast subunits, yeast Vph1/Stv1 compartment specificity, and vacuolar-pH regulation.
    Loss-of-activity or acidification phenotypes do not alone establish assembly necessity.
    Detached V1/V0 inhibition and counterion/exchanger/buffering contributions are
    not universal structure-inventory claims.
  support: context_only
  snapshot_sha256: 13a3eb22e486987e2599a0e7c23b7677808cf35e07e8f558a3b559de5d6f86d4
- evidence_id: micro-forgac2007-summary
  kind: authority
  reference: https://www.nature.com/articles/nrm2272
  locator: 'Forgac 2007 DOI:10.1038/nrm2272; accessible Key Points P8-P12 and abstract
    P13; subscription notice P14; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/forgac2007.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/forgac2007.receipt.json'
  accessed_at: '2026-11-03T06:46:59.669702Z'
  summary: 'Secondary Key Points and abstract only: ATP-driven V1 rotor and V0 proton
    transport, ER assembly/chaperone and targeting context, reversible dissociation,
    and organelle/plasma-membrane functions. Main text is gated; no fresh full-review-body
    audit claimed.'
  support: context_only
  snapshot_sha256: ce9ac838f9964647e1254f7474c79a6b30d0433508fc23d6cbde45926121d22f
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: 'ENA taxonomy tax-id/4932 result: taxId, scientificName, rank; response
    and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/tax-4932.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/tax-4932.receipt.json'
  accessed_at: '2026-11-03T06:46:59.669779Z'
  summary: NCBITaxon:4932 resolves to Saccharomyces cerevisiae at species rank. This
    validates the taxon, not strain, occurrence frequency, or universal molecular
    composition.
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: micro-literature-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=DOI%3A%2210.1128%2FMMBR.70.1.177-191.2006%22+OR+DOI%3A%2210.1038%2Fnature14365%22+OR+DOI%3A%2210.1016%2Fj.bbamcr.2008.08.003%22+OR+DOI%3A%2210.1038%2Fnrm2272%22
  locator: 'Europe PMC core records matching four exact DOIs; pageSize=100; title/authors/publication
    identifiers and abstracts only; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/metadata.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/metadata.receipt.json'
  accessed_at: '2026-11-03T06:47:00.102473Z'
  summary: The four cited DOIs match Kane 2006 (PMID:16524922), Zhao 2015 (PMID:25971514),
    Li/Kane 2009 (PMID:18786576) and Forgac 2007 (PMID:17912264). Metadata corroborates
    bibliographic identity, not unseen full text.
  support: context_only
  snapshot_sha256: e93f76b1ac92f4482b4b75ff6e1129387f867915033cca990e1d2b43d7d1deff
- evidence_id: micro-named-yeast-genes
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28taxonomy_id%3A4932%29+AND+%28gene_exact%3AVPH1+OR+gene_exact%3ASTV1+OR+gene_exact%3AVMA3+OR+gene_exact%3AVMA11+OR+gene_exact%3AVMA16+OR+gene_exact%3AVMA6+OR+gene_exact%3AVMA9+OR+gene_exact%3AVMA1+OR+gene_exact%3AVMA2+OR+gene_exact%3AVMA8+OR+gene_exact%3AVMA7+OR+gene_exact%3AVMA4+OR+gene_exact%3AVMA10+OR+gene_exact%3AVMA5+OR+gene_exact%3AVMA13%29&format=json&size=500
  locator: 'UniProt reviewed result primary gene names, recommended protein names,
    accessions and organism IDs; 15 results, no next-page Link; response and receipt:
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/genes/named-yeast-genes.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/genes/named-yeast-genes.receipt.json'
  accessed_at: '2026-11-03T06:48:47.467125Z'
  summary: 'All fifteen queried yeast gene tokens have reviewed S. cerevisiae S288C
    (taxon 559292 within 4932) records: VPH1/P32563 and STV1/P37296 (a isoforms);
    VMA3/P25515, VMA11/P32842, VMA16/P23968 (c/c-prime/c-double-prime); VMA6/P32366
    (d), VMA9/Q3E7B6 (e); VMA1/P17255 (A), VMA2/P16140 (B), VMA8/P32610 (D), VMA7/P39111
    (F), VMA4/P22203 (E), VMA10/P48836 (G), VMA5/P31412 (C), VMA13/P41807 (H). This
    confirms the named yeast mappings, not a complete universal inventory, protist
    gene nomenclature, physical necessity or unasserted record accessions.'
  support: supports
  snapshot_sha256: 42e85906c8163829c6aeb1289fa90747910c804297856bdaefbfbe60e3278599
  search_scope: 'UniProtKB REST search, accessed 2026-11-03T06:48:47.467125+00:00:
    (reviewed:true) AND (taxonomy_id:4932) AND (gene_exact:VPH1 OR gene_exact:STV1
    OR gene_exact:VMA3 OR gene_exact:VMA11 OR gene_exact:VMA16 OR gene_exact:VMA6
    OR gene_exact:VMA9 OR gene_exact:VMA1 OR gene_exact:VMA2 OR gene_exact:VMA8 OR
    gene_exact:VMA7 OR gene_exact:VMA4 OR gene_exact:VMA10 OR gene_exact:VMA5 OR gene_exact:VMA13).
    JSON size=500, HTTP200, x-total-results=15, no next-page Link. Taxonomy filtering
    includes descendant strains; bounded to fifteen exact named genes and reviewed
    entries, not all V/A-ATPase homologues or other taxa.'
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'iModulonDB /api/datasets complete returned JSON mapping: 20 organism keys
    and 28 dataset keys; response and receipt: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/datasets.raw
    / /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/datasets.receipt.json'
  accessed_at: '2026-11-03T06:46:59.669835Z'
  summary: Fresh returned catalogue has bacterial/archaeal datasets but no named Saccharomyces
    or other eukaryotic organism. The named yeast/fungal molecular examples have no
    covered organism/dataset match. The complex record also mentions unspecified bacterial
    V/A relatives; that wording supplies no particular matched organism/gene for a
    justified downstream module query. Unrelated bacterial F-type ATPase hits would
    not resolve that ambiguity. No universal absence of ATPase expression evidence
    is inferred.
  support: partial
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: Retained earlier kg-microbe-sources imodulondb datasets invocation
  locator: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  accessed_at: '2026-11-03T00:49:00.863225Z'
  summary: Historical runner attempt at 2026-11-03T00:49:00.848907+00:00 through 00:49:00.863225+00:00
    failed with OS PermissionError reading pyvenv.cfg (actual exit 1). It is retained
    unavailable-runner context, not a current execution or successful adapter run.
    The current direct source catalogue was inspected separately.
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks, lines 89-122; current frozen bytes and
    conf/record_review.yaml route
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Native policy triggers applicability for named genes/proteins/pathways
    and permits inspected source-page fallback if the runner is unavailable. Lack
    of an expression claim alone is not an exemption. These policy bytes were retained
    from earlier reads and their equality/current frozen hashes rechecked; the applicability
    section was reread for this report.
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Native graph contract and add-cell-structure/review-checklist schema context
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Graph scope must reflect represented directed causal explanation. Membership
    and whole-structure activity do not by themselves represent hydrolysis-to-rotor
    coupling; identity, substructure membership, necessity and mechanistic activity
    remain distinct. Current frozen graph policy/schema were inspected, including
    retained byte-identical context.
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-roundtrip
  kind: validation
  reference: scripts/record_review.py validate; render --content; git show and SHA-256
    input comparison
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-microtubule/original-validation-inputs.json
  accessed_at: '2026-11-03T06:47:14.566006Z'
  summary: All three original YAML reviews validate and render byte-identically to
    their committed Markdown. Each original target hash matches its historical source
    revision, current main and reviewed head. No target is stale in this slice. This
    is local schema/render/input verification, not scientific validation by command.
  support: supports
  snapshot_sha256: 6e04db597f18702a306079313d21579a6beb6cb88c38c58f84a78acfbd4001a3
- evidence_id: micro-record-proton_transporting_v_type_atpase_complex
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  locator: Whole current YAML record at d7ee610a5d142b5961a6057e22437aabb68f191f
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Entire current record inspected, including definition, hierarchy, functions,
    taxon/canonical-organism scope, references, graph nodes/edges and curation history.
    Target unchanged relative to original frozen input and current main.
  support: supports
  snapshot_sha256: 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4
- evidence_id: micro-prior-proton_transporting_v_type_atpase_complex
  kind: prior_review
  reference: reviews/structured/20261021T100139Z-proton-transporting-v-type-atpase-complex-audit/review.yaml
  locator: Whole immutable original YAML/Markdown, exact F1/F2, checks/limitations
    and frozen inputs
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Original needs_curation verdict and two distinct findings remain relevant
    to this unchanged target. Earlier literature access claims are historical observations,
    not substituted for fresh source access. Original has an explicit expression-module
    not_applicable check; its rationale uses absence of needed transcriptomic inference
    rather than matched-dataset applicability.
  support: context_only
  snapshot_sha256: 62f6ae2d760655e4df251bfcdb2d1e4a12d38e3bb46d8628a4f24144a046b45c
- evidence_id: micro-native-proton_transporting_v_type_atpase_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-verify-receipt.json
  accessed_at: '2026-11-03T06:47:10.281568Z'
  summary: Native --verify returned zero, but the maintained record has no protein_examples
    and no protein xrefs in GENE_OR_PROTEIN nodes; the empty inventory does not validate
    prose yeast gene names.
  support: partial
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-proton_transporting_v_type_atpase_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_complex-uniprot-causal-receipt.json
  accessed_at: '2026-11-03T06:47:10.754811Z'
  summary: Native --causal-graphs returned zero with zero GENE_OR_PROTEIN nodes (all
    grounding counts zero). This is an empty protein-node diagnostic; it does not
    validate the biological graph mechanism or its whole-structure/component nodes.
  support: partial
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-record-proton_transporting_v_type_atpase_v0_domain
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
  locator: Whole current YAML record at d7ee610a5d142b5961a6057e22437aabb68f191f
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Entire current record inspected, including definition, hierarchy, functions,
    taxon/canonical-organism scope, references, graph nodes/edges and curation history.
    Target unchanged relative to original frozen input and current main.
  support: supports
  snapshot_sha256: f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c
- evidence_id: micro-prior-proton_transporting_v_type_atpase_v0_domain
  kind: prior_review
  reference: reviews/structured/20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit/review.yaml
  locator: Whole immutable original YAML/Markdown, exact F1/F2, checks/limitations
    and frozen inputs
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Original needs_curation verdict and two distinct findings remain relevant
    to this unchanged target. Earlier literature access claims are historical observations,
    not substituted for fresh source access. Original has an explicit expression-module
    not_applicable check; its rationale uses absence of needed transcriptomic inference
    rather than matched-dataset applicability.
  support: context_only
  snapshot_sha256: 03fab0285e5720a50dcad20a595888e3315d10355e0f6e0708c60a32a8a4c117
- evidence_id: micro-native-proton_transporting_v_type_atpase_v0_domain-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-verify-receipt.json
  accessed_at: '2026-11-03T06:47:11.245671Z'
  summary: Native --verify returned zero, but the maintained record has no protein_examples
    and no protein xrefs in GENE_OR_PROTEIN nodes; the empty inventory does not validate
    prose yeast gene names.
  support: partial
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-proton_transporting_v_type_atpase_v0_domain-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v0_domain-uniprot-causal-receipt.json
  accessed_at: '2026-11-03T06:47:11.726675Z'
  summary: Native --causal-graphs returned zero with zero GENE_OR_PROTEIN nodes (all
    grounding counts zero). This is an empty protein-node diagnostic; it does not
    validate the biological graph mechanism or its whole-structure/component nodes.
  support: partial
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-record-proton_transporting_v_type_atpase_v1_domain
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
  locator: Whole current YAML record at d7ee610a5d142b5961a6057e22437aabb68f191f
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Entire current record inspected, including definition, hierarchy, functions,
    taxon/canonical-organism scope, references, graph nodes/edges and curation history.
    Target unchanged relative to original frozen input and current main.
  support: supports
  snapshot_sha256: a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300
- evidence_id: micro-prior-proton_transporting_v_type_atpase_v1_domain
  kind: prior_review
  reference: reviews/structured/20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit/review.yaml
  locator: Whole immutable original YAML/Markdown, exact F1/F2, checks/limitations
    and frozen inputs
  accessed_at: '2026-11-03T06:54:11.199379Z'
  summary: Original needs_curation verdict and two distinct findings remain relevant
    to this unchanged target. Earlier literature access claims are historical observations,
    not substituted for fresh source access. Original has an explicit expression-module
    not_applicable check; its rationale uses absence of needed transcriptomic inference
    rather than matched-dataset applicability.
  support: context_only
  snapshot_sha256: 409a468b8d8d85c53714f0c7fdb5ed83ad987b2d3df377371ee6dfcca83af9e7
- evidence_id: micro-native-proton_transporting_v_type_atpase_v1_domain-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-verify-receipt.json
  accessed_at: '2026-11-03T06:47:12.202462Z'
  summary: Native --verify returned zero, but the maintained record has no protein_examples
    and no protein xrefs in GENE_OR_PROTEIN nodes; the empty inventory does not validate
    prose yeast gene names.
  support: partial
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-proton_transporting_v_type_atpase_v1_domain-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/proton_transporting_v_type_atpase_v1_domain-uniprot-causal-receipt.json
  accessed_at: '2026-11-03T06:47:12.670686Z'
  summary: Native --causal-graphs returned zero with zero GENE_OR_PROTEIN nodes (all
    grounding counts zero). This is an empty protein-node diagnostic; it does not
    validate the biological graph mechanism or its whole-structure/component nodes.
  support: partial
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: septin-septum-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000935,GO:0030428,GO:0032153,GO:0110165
  locator: Definitions and synonyms of all four returned terms; GO0110165 child GO0030428;
    GO0030428 child GO0000935; GO0032153 part_of child GO0000935
  accessed_at: '2026-11-03T06:48:42.395765Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: 74317511d15a26e9621c9267c22daa3fd3ccf6214fd45011a345547b28e0ba3d
- evidence_id: septin-septum-agent-tax-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:42.396028Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: septin-septum-agent-tax-83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:42.396117Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: septin-septum-agent-tax-1423
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1423
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:42.396176Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: cba62f34e18147fc64dac9d0b13c66a25f60ac516c43a451187d6787e3c7a07b
- evidence_id: septin-septum-agent-chebi-8005
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/8005/
  locator: Complete released three-star entry, name, definition, synonyms and ontology
    relations
  accessed_at: '2026-11-03T06:48:42.396220Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: e522d29047c83fadac704ac6c6a4bc6a6beab1c5f0f116d903c78536bca212c0
- evidence_id: septin-septum-agent-doi-10.1111_j.1749-6632.2012.06818.x
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111/j.1749-6632.2012.06818.x%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:43.123911Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: 9223d6468cb3fd82c0defeba074dfa46343ad8d8b92d9685553c81f47db5f538
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111/j.1749-6632.2012.06818.x%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:43.123911Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-septum-agent-doi-10.1146_annurev-biophys-121219-081703
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1146/annurev-biophys-121219-081703%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:43.135477Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: fde972273ed77393cfd4a111d968cefbdb92530aad4b8b911fcd058e27186d12
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1146/annurev-biophys-121219-081703%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:43.135477Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-septum-agent-jats-PMC8610174
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8610174.1/PMC8610174.1.xml
  locator: Fresh native secondary-review JATS, sections S1 Introduction, S2 Overview,
    S16 Scaffold, S17 Coordinator, S22 Cell Pole Shape Determinant and S23 Conclusions.
  accessed_at: '2026-11-03T06:48:43.156806Z'
  support: supports
  summary: Bacterial septal peptidoglycan and FtsZ-divisome context are supported.
    This secondary review does not source the maintained archaeal/fungal expansion,
    and its cited primary experiments were not independently audited.
  snapshot_sha256: 8a76b9af3fed1226ad5e9e6f00452499f9541ace397318b6d6ff1635dd0ca45d
- evidence_id: septin-bud-membrane-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005886,GO:0005933,GO:0016020,GO:0033101
  locator: All four term definitions and relevant GO0033101 child relations under
    GO0005933/GO0005886
  accessed_at: '2026-11-03T06:48:43.194102Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: 4996a70bf2d54e7fcc865bfbb17b800a2b20526ab73dde29dbc0f02712021d39
- evidence_id: septin-bud-membrane-agent-SL-0028
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0028.json
  locator: Complete location name, definition, synonyms, cross-references and hierarchy
  accessed_at: '2026-11-03T06:48:43.217345Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: de42296b0da87c46a5410f4d244378b490c2d8744bdf0cc134a5cb48100f79be
- evidence_id: septin-bud-membrane-agent-SL-0027
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0027.json
  locator: Complete location name, definition, synonyms, cross-references and hierarchy
  accessed_at: '2026-11-03T06:48:43.776816Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: 3367af44f7485396df649e631b15487f577a11026c6701fbbd535fec005f759d
- evidence_id: septin-bud-membrane-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:43.794410Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-bud-membrane-agent-doi-10.1083_jcb.135.3.725
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.135.3.725%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:43.806684Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: a4d183a1f49226a5b751b0431a85040ce25f8b9f7e7fcba230b65bdd7e7af34d
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.135.3.725%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:43.806684Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-bud-membrane-agent-doi-10.1016_S0092-8674_00_80948-4
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/S0092-8674%2800%2980948-4%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:43.834910Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: 20b875b3ff04b061ec6af5d6e6a56d95c1438aeefb9f9e63d8b1ed77cd0c6c1b
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/S0092-8674%2800%2980948-4%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:43.834910Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-bud-membrane-agent-valtz1996-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf
  locator: 'Fresh genuine primary PDF: abstract, Introduction, Budding Pattern Assays
    and Immunofluorescence Methods, antibody specificity/Pea2p expression/localization
    Results pp731–732, and complex Discussion p739.'
  accessed_at: '2026-11-03T06:48:43.841703Z'
  support: supports
  summary: S. cerevisiae Pea2/Spa2 localization and interdependence are studied; complex
    formation is a proposed interpretation, not direct physical colocalization in
    this paper. This is not an inventory of lipid-boundary constituents.
  snapshot_sha256: c06951939912dcb3700b5cd867b40a7d9c2a74f41460bb93f31839852509d9c9
- evidence_id: septin-coccolith-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0110165
  locator: Native GO0110165 name and complete definition
  accessed_at: '2026-11-03T06:48:44.362301Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: 8af7ebd70cc7d5662c02c9f11811d9e04292105c71f15ff9e79a283c2c9a240d
- evidence_id: septin-coccolith-agent-chebi-46719
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/46719/
  locator: Released entry name, chemical data and ontology relations; no textual definition
    is supplied
  accessed_at: '2026-11-03T06:48:44.391636Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: c60cfe36e7049d976e3ea21459220c6812bf04c4e7614ae4abb55afb5d975850
- evidence_id: septin-coccolith-agent-tax-127549
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/127549
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:44.395663Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: b40f70d18d46271a012610371904101819726ec1f4fc1054ca41a87a2b88e8c2
- evidence_id: septin-coccolith-agent-tax-2903
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2903
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:44.475818Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: dd94de64d5f0b4a22db3c88631c1c29f985b2856636530d16b404e913762054f
- evidence_id: septin-coccolith-agent-doi-10.1021_jacs.6c02151
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1021/jacs.6c02151%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:44.477809Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: 03427fde395095193fa6dd53b5575affa275cefb778fc30c041ab7bbe10bb373
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1021/jacs.6c02151%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:44.477809Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-coccolith-agent-doi-10.1093_pnasnexus_pgag104
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/pnasnexus/pgag104%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:44.992202Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: ff8b27a96f99ea4845e1d25d983e65f74434420824c1f994471da79c614a78a7
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/pnasnexus/pgag104%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:44.992202Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-coccolith-agent-doi-10.1126_sciadv.adc8728
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1126/sciadv.adc8728%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:44.993342Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: 20a1f09fbab45fd3a6c2164af6dfc37998b1551ea76baaee9592a20b7d876209
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1126/sciadv.adc8728%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:44.993342Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-coccolith-agent-jats-PMC13067266
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/PMC13067266.1.xml
  locator: 'Fresh native primary JATS: Introduction, complete Results, Figures1–5
    captions, Discussion, Conclusions, author metadata and exact permissions.'
  accessed_at: '2026-11-03T06:48:45.035709Z'
  support: supports
  summary: C. leptoporus mature scales and vesicle boundaries are distinct. SEM/AFM
    morphology and unresolved luminal particles support the record limits, without
    identifying a full ATPase or universal morphogenesis mechanism.
  snapshot_sha256: c65411d5c5adb24f2e42120962c24d0fd3ecaffda72f9f485a728a313f2acdef
- evidence_id: septin-coccolith-agent-avrahami2026-supp
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_si_001.pdf
  locator: 'Fresh genuine supplementary PDF: Materials/Methods Cell cultures, Coccolith
    isolation for ex situ imaging, SEM, correlative AFM/SEM, and adjacent freeze-fracture/cryofixation
    context, first five PDF pages.'
  accessed_at: '2026-11-03T06:48:45.100711Z'
  support: supports
  summary: RCC1130 and isolated/cleaned SEM/AFM preparation are explicit. These Figure1
    samples are not native cryotomographic specimens. Downstream tomography processing
    and all supplementary figures were not audited.
  snapshot_sha256: b919d05e8a48887245d56be37a7aa917366f68cdf058e6b742bae29d385a3248
- evidence_id: septin-coccolith-agent-jats-PMC13089448
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13089448.1/PMC13089448.1.xml
  locator: 'Fresh native primary JATS: Introduction, Results, Figures1/3/5 captions,
    Discussion and Conclusion.'
  accessed_at: '2026-11-03T06:48:45.101882Z'
  support: supports
  summary: Calyptrosphaera holococcoliths contain calcite rhombohedra and an organic
    base plate; the study does not establish universal base-plate nucleation and cannot
    exclude sufficiently small undetected nucleators. Methods supplement and raw data
    not audited.
  snapshot_sha256: 84016e30c9834977c7d3ab23851d8c595232e0b161027d97cf88556101007d30
- evidence_id: septin-coccolith-agent-jats-PMC9858585
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9858585.1/PMC9858585.1.xml
  locator: 'Fresh native primary JATS: Introduction as prior context; Results Xenospheres,
    Free coccoliths, Adsorption mediated by organic matter and Multifaceted ecological
    roles; Figures1–3/6 captions; Methods Culture, Coccolith isolation/treatment,
    Exogenous additions and SEM.'
  accessed_at: '2026-11-03T06:48:45.465278Z'
  support: supports
  summary: Calcified CCMP374 donor versus naked recipient, mixed-origin adsorption
    and oxidation response are supported. Organic removal reduces attachment without
    identifying a particular adhesion molecule. Detailed virus-encounter models, supplementary
    videos and raw data were not reanalysed.
  snapshot_sha256: 560f029155372cb75ad9eaef3c7fd554da9c6d5d2a4f90c929eabed0648160a5
- evidence_id: septin-coccolith-agent-package-PMC13067266
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC13067266.1.json
  locator: Complete article/package identity, license_code and matching media_urls
    entry
  accessed_at: '2026-11-03T06:48:45.560562Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: c0f3e27d29496c54202003a39fbd3ae7bd13a12d1e9dbc57e77bcdc05d8f4bc2
- evidence_id: septin-coccosphere-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030312
  locator: Complete term definition, comment and child-relation scope
  accessed_at: '2026-11-03T06:48:45.625560Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: ab65d98850dd6a2845a8b4697a5ad61328ce31f453366335f7b30b44e62ab6b6
- evidence_id: septin-coccosphere-agent-tax-221442
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/221442
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-11-03T06:48:45.644569Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: a69b1168a4b3803081384133161be038a6db4ca0629c9c3806c1d44f390dde6e
- evidence_id: septin-coccosphere-agent-doi-10.7717_peerj.4608
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.7717/peerj.4608%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:45.861719Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: a16d33329068b76cc1977dcc86925dc82ca894b25e772d569c77d8646409ad03
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.7717/peerj.4608%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:45.861719Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-coccosphere-agent-doi-10.1111_nph.15272
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111/nph.15272%22
  locator: 'Europe PMC exact DOI query: returned hitCount, bibliographic fields, publication
    type, DOI and available abstract only.'
  accessed_at: '2026-11-03T06:48:45.997149Z'
  support: supports
  summary: Exact article identity verified. Abstract/metadata access does not imply
    current full-body inspection; direct primary or secondary body access is recorded
    separately.
  snapshot_sha256: ed05012a649be9d7f459ee8b09f2342a775befac3986da86ae95c897b65a43a4
  search_scope: Europe PMC REST exact DOI query in URL https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1111/nph.15272%22;
    resultType core, pageSize25 server default, first page only; accessed 2026-11-03T06:48:45.997149Z;
    no publication-date restriction. Exact bibliographic identity check, not exhaustive
    literature absence search.
- evidence_id: septin-coccosphere-agent-jats-PMC5896503
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5896503.1/PMC5896503.1.xml
  locator: 'Fresh native primary JATS: Materials/Methods; Results one-layer definition,
    neighboring-coccolith geometry, daily-size and assembly passages; Figure2 caption;
    Conclusion; exact article permissions.'
  accessed_at: '2026-11-03T06:48:46.029981Z'
  support: supports
  summary: CS-369 pooled growth conditions and doubling visible plates under uniform-distribution
    assumption remain explicit. Red figure labels count neighboring plates. The geometric
    model was not independently recalculated or promoted across species.
  snapshot_sha256: 1cacc8199b6eef01b6199bbb1bc94a72f351908023aa776071e40db8d1b9606a
- evidence_id: septin-coccosphere-agent-jats-PMC6175242
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6175242.1/PMC6175242.1.xml
  locator: 'Fresh native primary JATS: nph15272-sec-0003 through0014 relevant culture/perturbation/time-lapse/fluorescence/SEM/immunofluorescence
    Methods; sec0019–0023 Results/Discussion; Figures6/8/9 captions.'
  accessed_at: '2026-11-03T06:48:46.206806Z'
  support: supports
  summary: PLY182g external lectin-positive layer is not one identified polymer. Ge/HEDP
    impair daughter separation after initial cytokinesis; low calcium differs. Intracellular
    tubulin is excluded from covering composition. No movie, Figure5–9 pixel or raw-data
    reanalysis.
  snapshot_sha256: 9c69e3449019fc71795394ac8771c330504f62aeb849f1234a8339a1e3fc0dba
- evidence_id: septin-coccosphere-agent-package-PMC5896503
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC5896503.1.json
  locator: Complete article/package identity, license_code and matching media_urls
    entry
  accessed_at: '2026-11-03T06:48:46.231530Z'
  support: supports
  summary: Exact authority identifier and returned annotations inspected within their
    scope; authority identity is not independent experimental evidence.
  snapshot_sha256: f40beaf82ceab05c10bc9aafe2cfe53281ccf87903430bba9d58f5358eb51103
- evidence_id: septin-coccolith-image-source
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13067266.1/ja6c02151_0001.jpg
  locator: Fresh exact native PMC media bytes, SHA256 and corresponding metadata media
    MD5; local frozen image pixels independently viewed.
  accessed_at: '2026-11-03T06:48:46.505655Z'
  support: supports
  summary: Source media byte identity agrees with the frozen local image, record checksum
    and native package metadata.
  snapshot_sha256: 35772c3d477f71c47c7c2e0d6e91fbd6086b9061126c7bee92cec70fcd95f939
- evidence_id: septin-coccosphere-image-source
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5896503.1/peerj-06-4608-g002.jpg
  locator: Fresh exact native PMC media bytes, SHA256 and corresponding metadata media
    MD5; local frozen image pixels independently viewed.
  accessed_at: '2026-11-03T06:48:46.519971Z'
  support: supports
  summary: Source media byte identity agrees with the frozen local image, record checksum
    and native package metadata.
  snapshot_sha256: 5f3b2473ff6c3e1e281c8ae71b4c2d72dd32536e8c9b80e08f761c72b0bff765
- evidence_id: septin-current-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire fresh official /api/datasets response: all organism objects and
    dataset keys inspected.'
  accessed_at: '2026-11-03T06:48:46.527222Z'
  support: supports
  summary: Catalogue matches E. coli and B. subtilis; it has no S. cerevisiae or named
    haptophyte dataset. Coverage is bounded to the returned catalogue, with no biological-absence
    inference.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-egan-access-access
  kind: validation
  reference: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1749-6632.2012.06818.x
  locator: Actual fresh direct HTTP attempt at 2026-11-03T06:48:43.178263Z
  accessed_at: '2026-11-03T06:48:43.178263Z'
  support: context_only
  summary: '<HTTPError 403: ''Forbidden''>; no native body inspection or successful
    retrieval claimed. Bibliographic/abstract or independently accessed indexed text
    supplies bounded fallback.'
  snapshot_sha256: b48225ca0894ebc9444a8a24f1a47f850e26d89dbd644b32e3c374bb89a1ffa3
- evidence_id: septin-bud-membrane-agent-finger-body-access
  kind: validation
  reference: https://www.researchgate.net/publication/13739580_Sec3p_Is_a_Spatial_Landmark_for_Polarized_Secretion_in_Budding_Yeast
  locator: Actual fresh direct HTTP attempt at 2026-11-03T06:48:44.343669Z
  accessed_at: '2026-11-03T06:48:44.343669Z'
  support: context_only
  summary: '<HTTPError 403: ''Forbidden''>; no native body inspection or successful
    retrieval claimed. Bibliographic/abstract or independently accessed indexed text
    supplies bounded fallback.'
  snapshot_sha256: b48225ca0894ebc9444a8a24f1a47f850e26d89dbd644b32e3c374bb89a1ffa3
- evidence_id: septin-bud-membrane-agent-finger-body
  kind: primary_source
  reference: https://www.researchgate.net/publication/13739580_Sec3p_Is_a_Spatial_Landmark_for_Polarized_Secretion_in_Budding_Yeast
  locator: 'Browser-indexed primary author-uploaded text with declared crawl age three
    weeks: Introduction and Results localization in living cells, Figure1/2 captions
    and Sec3-GFP membrane-association passage; displayed lines124–388.'
  accessed_at: '2026-11-03T06:51:57Z'
  support: supports
  summary: Tagged yeast Sec3 occupies stage-dependent polarized sites. Membrane-growth
    interpretation uses source background plus measured site organization; no direct
    membrane-growth-rate measurement or exhaustive component inventory is asserted.
  snapshot_sha256: 6eb890798f804e9d7d39601bcb0862c3612bfd354b68429f1fd9e641067c8f67
- evidence_id: septin-bud-membrane-agent-finger-methods
  kind: primary_source
  reference: https://www.researchgate.net/publication/13739580_Sec3p_Is_a_Spatial_Landmark_for_Polarized_Secretion_in_Budding_Yeast
  locator: 'Browser-indexed primary author-uploaded text: Experimental Procedures/fixation/indirect
    immunofluorescence and Microscopy passages, displayed lines1134–1336. No direct
    HTTP success attested.'
  accessed_at: '2026-11-03T06:50:56Z'
  support: supports
  summary: Tag function, fixation, optical sections and counting criteria constrain
    localization interpretations; whole article, all mutant comparisons and raw images
    were not audited.
  snapshot_sha256: b8241c5d639aa7e0c3b0c69d4bbf19e7f13709b09e075e582788d08676b1c29c
- evidence_id: septin-current-local-ids
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: cellstructuremech:(coccolith|coccosphere)$
    data/structures'
  locator: Exact anchored top-level identifiers across data/structures, including
    ignored and hidden files.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: One matching maintained definition each for coccolith and coccosphere.
    No external exact-equivalence or GO-wide absence claim follows.
  snapshot_sha256: 149f0e047f8dd03fe0a1df177955a15c9631f7e8129f67aa750abeb4fd7c9295
  search_scope: Entire local data/structures recursively, ignored and hidden files
    included, exact anchored identifier regex only, no pagination/date filters; executed
    2026-11-03T06:53:39.376532Z
- evidence_id: septin-record-cell_septum
  kind: record_content
  reference: data/structures/envelope/cell_septum.yaml
  locator: 'Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all
    definitions, fields, discussions, examples, images and graph edges.'
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Current target hash equals original frozen input. Whole-record independent
    reassessment performed without changing records.
  snapshot_sha256: feb3124957603d095f40d56b031828b135cdbd6b7d61f21c8bc6ec1d401b7e54
- evidence_id: septin-record-cellular_bud_membrane
  kind: record_content
  reference: data/structures/envelope/cellular_bud_membrane.yaml
  locator: 'Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all
    definitions, fields, discussions, examples, images and graph edges.'
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Current target hash equals original frozen input. Whole-record independent
    reassessment performed without changing records.
  snapshot_sha256: e90c632bd6b0247beed83ee5c7411f2083dae19765e149ae2475d4e35455127f
- evidence_id: septin-record-coccolith
  kind: record_content
  reference: data/structures/envelope/coccolith.yaml
  locator: 'Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all
    definitions, fields, discussions, examples, images and graph edges.'
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Current target hash equals original frozen input. Whole-record independent
    reassessment performed without changing records.
  snapshot_sha256: 8932b1ad635cf2e272c74fb8d4f00e6036b851ec2baa3daa3b5c3b52cc6979fa
- evidence_id: septin-record-coccosphere
  kind: record_content
  reference: data/structures/envelope/coccosphere.yaml
  locator: 'Complete current YAML at d7ee610a5d142b5961a6057e22437aabb68f191f: all
    definitions, fields, discussions, examples, images and graph edges.'
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Current target hash equals original frozen input. Whole-record independent
    reassessment performed without changing records.
  snapshot_sha256: b72167a6093a734226fc2c9458c475f7a05120e8d2077d5f7b7007ee0a5cd299
- evidence_id: septin-coccolith-agent-image
  kind: record_content
  reference: data/images/envelope/coccolith/pmc13067266_fig1.jpg
  locator: Full frozen local image actually inspected with view_image, then compared
    to fresh native source bytes, figure caption, methods and exact JATS permissions.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Figure1 A–F shows SEM cell/scales, a schematic and AFM height maps/projections.
    Mixed modalities and ex situ preparation are accurately described. CC BY4.0, listed
    authors and source-specific attribution verified.
  snapshot_sha256: 35772c3d477f71c47c7c2e0d6e91fbd6086b9061126c7bee92cec70fcd95f939
- evidence_id: septin-coccosphere-agent-image
  kind: record_content
  reference: data/images/envelope/coccosphere/pmc5896503_fig_2.jpg
  locator: Full frozen local image actually inspected with view_image, then compared
    to fresh native source bytes, figure caption, methods and exact JATS permissions.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Figure2 A–F shows six SEM coverings, white bars and red neighboring-plate
    annotations. Native caption specifies 1 micrometre bars; counts do not mean every
    sphere has that many total scales. Exact CC BY4.0 and attribution verified.
  snapshot_sha256: 5f3b2473ff6c3e1e281c8ae71b4c2d72dd32536e8c9b80e08f761c72b0bff765
- evidence_id: septin-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Evidence scope and structural identity remain distinct from specific mechanism
    and experimental necessity.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-adapter-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Named gene/protein or pathway claims trigger applicability. Unavailable
    runner permits inspected official source fallback; no covered organism means downstream
    non-applicability.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Graph scope and directed edges must match source-supported causal explanation.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-graph-contract
  kind: authority
  reference: .claude/skills/add-cell-structure/SKILL.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: Mechanistic paths must represent source-backed structure, role and causal
    transitions; useful topology is distinct.
  snapshot_sha256: eee04ee51d2c82c05df98570674084bdce9001e5aa67d6230ac1ed50064a3175
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/adversary-septin/original-checks.json
  locator: Four original native validate/render runs and original/current frozen target
    hashes.
  accessed_at: '2026-11-03T06:53:39.376532Z'
  support: supports
  summary: All four validate and render exit0; Markdown exactly matches native rendering;
    all four target hashes unchanged. Historical corpus gates are not current CI.
  snapshot_sha256: 574f8f36c76de1a047bd20fd73e1db1b3f2fc8d6106324449c700597ecc725c1
- evidence_id: septin-native-cell_septum-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cell_septum-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/cell_septum.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:13.123284Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: ff79f7fa1cb85fcb830a33a74a052e5b567aec9cd1fff5eff1ae01857ac64a3f
- evidence_id: septin-native-cell_septum-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cell_septum-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/cell_septum.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:13.572495Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: 996af8f4acd5f7f035d9d4f29bdf15df177fa38a9732f4ce5df004a9e2d5a9c9
- evidence_id: septin-native-cellular_bud_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cellular_bud_membrane-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/cellular_bud_membrane.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:14.022673Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: 23116faaf3c537056cf124fc9e0d79de0686d2b6eb3c8402d088447eb62b5e66
- evidence_id: septin-native-cellular_bud_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/cellular_bud_membrane-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/cellular_bud_membrane.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:14.475578Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: 6647e26adc89746560ab169d47e1ef6fbb1fcee51cd46d07f64f64e48874e9ea
- evidence_id: septin-native-coccolith-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccolith-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/coccolith.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:14.912148Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: 1e24ffb7aaaba27944b5edcaa3e719aa9224d7e7d9fea01163c6c1228fef344b
- evidence_id: septin-native-coccolith-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccolith-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/coccolith.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:15.341567Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: 13432a5b1a16dae0d3006f1f7036cfa3c520cc1fb009dc6e2f16e486d94a9217
- evidence_id: septin-native-coccosphere-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccosphere-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/coccosphere.yaml', '--verify'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:15.789243Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: 7fe1b33e84c0ed68874b7c23987f358d0496e68b6c56fa4f62e8791dc7d0f047
- evidence_id: septin-native-coccosphere-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/coccosphere-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/envelope/coccosphere.yaml', '--causal-graphs'] at d7ee610a5d142b5961a6057e22437aabb68f191f;
    receipt and log independently read and hash verified.
  accessed_at: '2026-11-03T06:47:16.226860Z'
  support: supports
  summary: Exit0 with empty declared exact-protein inventory and zero GENE_OR_PROTEIN
    graph nodes. This does not validate narrative FtsZ/Sec3/Pea2/Spa2 or unresolved
    molecules.
  snapshot_sha256: debd800c65f22bc691569c36e5bd4be23e112fd15ff1c4e6d27821c73c63a17c
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical canary attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z,
    exit1 PermissionError reading pyvenv.cfg; no fresh invocation.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical OS unavailability is separated from current official API fallback.
    No current runner availability test or runner success claimed.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-adapter-e_coli-precise1k-ftsZ-search
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ftsZ&limit=50
  locator: Entire bounded native search response; exact FtsZ gene-name matches separated
    from incidental product-text matches.
  accessed_at: '2026-11-03T06:49:49.342084Z'
  support: context_only
  summary: E. coli precise1k returns exact ftsZ b0095 plus incidental kilR product
    match; B. subtilis modulome returns ftsZ BSU_15290. Only exact FtsZ matches followed.
  snapshot_sha256: 3a5aa4d6bf2d6d5f21c7d335c20eb473e62be84b4780ae2707f73e3dbd264830
  search_scope: Official iModulonDB API; exact organism/dataset/query=ftsZ and limit50
    in https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ftsZ&limit=50;
    no date filter or pagination; executed 2026-11-03T06:49:49.342084Z. Only returned
    matches assessed; no biological absence inferred.
- evidence_id: septin-adapter-b_subtilis-modulome-ftsZ-search
  kind: search
  reference: https://imodulondb.org/api/search?organism=b_subtilis&dataset=modulome&query=ftsZ&limit=50
  locator: Entire bounded native search response; exact FtsZ gene-name matches separated
    from incidental product-text matches.
  accessed_at: '2026-11-03T06:49:49.342376Z'
  support: context_only
  summary: E. coli precise1k returns exact ftsZ b0095 plus incidental kilR product
    match; B. subtilis modulome returns ftsZ BSU_15290. Only exact FtsZ matches followed.
  snapshot_sha256: b5db6560900a5f4542e858a6c37347ab37c263a33651cfbc4f003b61f4f90555
  search_scope: Official iModulonDB API; exact organism/dataset/query=ftsZ and limit50
    in https://imodulondb.org/api/search?organism=b_subtilis&dataset=modulome&query=ftsZ&limit=50;
    no date filter or pagination; executed 2026-11-03T06:49:49.342376Z. Only returned
    matches assessed; no biological absence inferred.
- evidence_id: septin-adapter-e_coli-precise1k-b0095
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0095
  locator: 'Exact gene entry: gene_id/name/product, organism-dataset context and imported
    UniProt annotation.'
  accessed_at: '2026-11-03T06:50:17.531215Z'
  support: context_only
  summary: FtsZ identity verified within matched dataset. E. coli b0095 corresponds
    to imported P0A9A6; B. subtilis BSU_15290 to P17865. Imported annotations are
    not direct experimental evidence or whole-species coverage.
  snapshot_sha256: e4f8d2469b47fda365ac4bc1665ebca51bbbf0035ffc55588a8f7ff60e7a9a51
- evidence_id: septin-adapter-e_coli-precise1k-b0095-imodulons
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0095/imodulons
  locator: Entire returned gene-module membership list, including thresholds and is_in_imodulon
    flags.
  accessed_at: '2026-11-03T06:50:17.531561Z'
  support: context_only
  summary: All 201 returned component rows have is_in_imodulon=false. This thresholded
    membership output is not absence of gene expression, septal participation or biological
    function. No positive module hit informs this verdict.
  snapshot_sha256: eb20b807679961dffb6f70e82f03411ff30d48d13190889e8a06a003f7e7c7e4
- evidence_id: septin-adapter-b_subtilis-modulome-BSU_15290
  kind: database
  reference: https://imodulondb.org/api/genes/b_subtilis/modulome/BSU_15290
  locator: 'Exact gene entry: gene_id/name/product, organism-dataset context and imported
    UniProt annotation.'
  accessed_at: '2026-11-03T06:50:17.531862Z'
  support: context_only
  summary: FtsZ identity verified within matched dataset. E. coli b0095 corresponds
    to imported P0A9A6; B. subtilis BSU_15290 to P17865. Imported annotations are
    not direct experimental evidence or whole-species coverage.
  snapshot_sha256: 53b0851ed48206ae84bf0b2ed009518903535078e9414329b85978191ea5c216
- evidence_id: septin-adapter-b_subtilis-modulome-BSU_15290-imodulons
  kind: database
  reference: https://imodulondb.org/api/genes/b_subtilis/modulome/BSU_15290/imodulons
  locator: Entire returned gene-module membership list, including thresholds and is_in_imodulon
    flags.
  accessed_at: '2026-11-03T06:50:17.531911Z'
  support: context_only
  summary: All 72 returned component rows have is_in_imodulon=false. This thresholded
    membership output is not absence of gene expression, septal participation or biological
    function. No positive module hit informs this verdict.
  snapshot_sha256: 845b39befd56ab0bf9671e30c7d380a59c0ad427c55a777b7eb1270c720679ae
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:52:30.345469Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: a8b3e16d22cf8f428f548c963d3557aba2fe4f9b0f7c6dc6df0c160d1997f824
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:47:12.449719Z'
  support: supports
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:46:48.618411Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:46:46.032622Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:47:12.538057Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T06:56:10Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 674174cd37e60ff8b5c4db82032cc73de29b40990f9e0ff19423de5773246fea
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2354/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T06:48:33.543105Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 8be0fc88e1c3275f1e884a72abb0fc6aa11e9196b437404eb6317a8d8b7ffe94
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2354 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-current-0-identity
  area: identity
  topic: Generic FDH complex and respiratory example
  outcome: supported
  target_ids:
  - GO:0009326
  summary: GO0009326 is the exact generic complex and GO1990204 is its native is-a
    parent. The record explicitly frames FdnGHI/FdoGHI as respiratory examples; the
    generic identity must remain distinct from their particular composition and quinone
    coupling.
  evidence_ids:
  - plaque-formate-agent-go
  - plaque-formate-agent-pmid-11884747
  - plaque-formate-agent-CPX-1975
  - plaque-formate-agent-pmid-1504073
  - plaque-formate-agent-pmid-8566699
  - plaque-current-0
- assessment_id: plaque-current-0-composition
  area: evidence
  topic: FdnGHI membership and canonical stoichiometry
  outcome: supported
  target_ids:
  - GO:0009326
  summary: Fresh CPX1975 and UniProt support three copies each of FdnG/H/I and scoped
    cofactors. Independently inspected author-uploaded Jormakka main text supports
    periplasmic alpha-site oxidation, beta Fe-S relay and membrane gamma hemes/quinone
    site. The text is browser-rendered author content, not a native curl article body;
    no universal soluble or archaeal FDH architecture is inferred.
  evidence_ids:
  - plaque-formate-agent-CPX-1975
  - plaque-jormakka-browser-main
  - plaque-jormakka-browser-beta
  - plaque-jormakka-browser-later
  - plaque-formate-agent-chebi-60539
  - plaque-formate-agent-chebi-16374
  - plaque-formate-agent-chebi-30413
  - plaque-formate-agent-chebi-33725
  - plaque-formate-agent-P24183
  - plaque-formate-agent-P0AAJ3
  - plaque-formate-agent-P0AEK7
  - plaque-current-0
- assessment_id: plaque-current-0-necessity
  area: evidence
  topic: Assembly necessity of the conditional constituents
  outcome: unknown
  target_ids:
  - GO:0009326
  summary: The record labels all three proteins CONDITIONAL. The inspected intact
    structures and electron-transfer functions establish membership and roles, but
    do not isolate removal of each protein or define assembly requirements across
    alternative FDH classes. Assembly necessity remains unverified; catalytic necessity
    is not substituted for it.
  evidence_ids:
  - plaque-formate-agent-CPX-1975
  - plaque-jormakka-browser-main
  - plaque-jormakka-browser-beta
  - plaque-jormakka-browser-later
  - plaque-current-0
  - plaque-policy
- assessment_id: plaque-current-0-grounding
  area: grounding
  topic: Exact examples and bounded family withholding
  outcome: supported
  target_ids:
  - GO:0009326
  summary: All three reviewed accession/name/gene/taxon pairs and bounded uniqueness
    queries agree. Checked Fdn and Fdo entries share candidate family mappings; IPR006471
    also describes related hydrogenase/thiosulfate-reductase gamma subunits. Label-only
    status is defensible for these nitrate-inducible component labels, without claiming
    an exhaustive search or requiring optional additional examples.
  evidence_ids:
  - plaque-formate-agent-P24183
  - plaque-formate-agent-P0AAJ3
  - plaque-formate-agent-P0AEK7
  - plaque-formate-agent-query-fdnG
  - plaque-formate-agent-query-fdnH
  - plaque-formate-agent-query-fdnI
  - plaque-formate-agent-IPR006443
  - plaque-formate-agent-IPR006470
  - plaque-formate-agent-IPR006471
  - plaque-formate-agent-IPR014603
  - plaque-formate-agent-IPR051555
  - plaque-formate-agent-IPR051817
  - plaque-formate-agent-query-fdoG
  - plaque-formate-agent-query-fdoH
  - plaque-formate-agent-query-fdoI
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-current-0
- assessment_id: plaque-current-0-taxonomic-evidence
  area: scope
  topic: Bacterial and archaeal distribution references
  outcome: concern
  target_ids:
  - GO:0009326
  summary: Both broad taxonomic-distribution rows cite an unrelated viral/transcription
    study. E.coli FDH-N and the additional bacterial abstracts support bounded bacterial
    examples, but they cannot repair the declared broad bacterial frequency, methanogenic
    conservation or NAD+/F420-linked generalizations without appropriate sources.
  evidence_ids:
  - plaque-formate-agent-pmid-11884601
  - plaque-formate-agent-pmid-11884747
  - plaque-jormakka-browser-main
  - plaque-formate-agent-pmid-1504073
  - plaque-formate-agent-pmid-8566699
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-current-0
- assessment_id: plaque-current-0-function
  area: evidence
  topic: Respiratory reaction and PMF boundary
  outcome: supported
  target_ids:
  - GO:0009326
  summary: GO0036397 and the native/primary evidence support formate oxidation with
    quinone reduction for the respiratory example. The definition explicitly invokes
    a redox loop, which is consistent with the primary discussion when read as the
    coupled FDH-N/Nar system; no standalone proton-pump claim is inferred. Broader
    soluble/NAD+/F420-dependent examples are outside the recovered experiment.
  evidence_ids:
  - plaque-formate-agent-go
  - plaque-formate-agent-CPX-1975
  - plaque-jormakka-browser-main
  - plaque-jormakka-browser-beta
  - plaque-jormakka-browser-later
  - plaque-formate-agent-pmid-11884747
  - plaque-current-0
- assessment_id: plaque-current-0-completeness
  area: completeness
  topic: Optional inventories and images
  outcome: supported
  target_ids:
  - GO:0009326
  summary: The review identifies concrete existing evidence and graph defects. It
    does not require an image, measurement, exhaustive species inventory, or compulsory
    protein-family replacement merely because an optional slot is absent.
  evidence_ids:
  - plaque-formate-agent-CPX-1975
  - plaque-formate-agent-go
  - plaque-current-0
  - plaque-policy
- assessment_id: plaque-current-0-graph
  area: graph
  topic: Membership/activity summary versus mechanism
  outcome: concern
  target_ids:
  - GO:0009326
  summary: All five nodes and four edges were inspected. The component roles describe
    an electron-transfer sequence, but the graph connects each protein only by part-of
    and the complete structure to its activity. It does not represent transfer through
    the subunits or cofactor/quinone steps.
  evidence_ids:
  - plaque-formate-agent-go
  - plaque-formate-agent-CPX-1975
  - plaque-jormakka-browser-main
  - plaque-jormakka-browser-beta
  - plaque-jormakka-browser-later
  - plaque-current-0
  - plaque-graph-policy
- assessment_id: plaque-current-1-identity
  area: identity
  topic: Generic nitrate reductase versus NarGHI example
  outcome: supported
  target_ids:
  - GO:0009325
  summary: GO0009325 denotes the requested generic complex, GO1990204 is its parent,
    and GO0044799 is a narrower native NarGHI child. The identity and explicitly example-scoped
    NarGHI components are sound even though the copied broad definition reverses the
    reaction.
  evidence_ids:
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-current-1
- assessment_id: plaque-current-1-direction
  area: evidence
  topic: Native ontology conflict and internal inconsistency
  outcome: concern
  target_ids:
  - GO:0009325
  summary: The first definition sentence and structure-node description say nitrate
    is formed from nitrite. This wording is genuinely present in the inspected GO0009325
    snapshot; it was not invented by the record. It conflicts with the record function,
    GO0160182, CPX1974 and Bertero primary abstract, which describe nitrate-to-nitrite
    reduction coupled to quinol oxidation. Preserve this source conflict while correcting
    the scientific wording.
  evidence_ids:
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-current-1
- assessment_id: plaque-current-1-composition
  area: evidence
  topic: NarGHI membership and canonical stoichiometry
  outcome: supported
  target_ids:
  - GO:0009325
  summary: The three named proteins, their catalytic/relay/anchor roles, two copies
    each in the CPX1974 canonical complex, and listed cofactors match native curation
    and protein annotations. The heterotrimeric functional unit is distinguished from
    the dimer-of-heterotrimers assembly. No NarGHI inventory is imposed on NapAB,
    Nas/Nia or all nitrate reductase complexes. The IPR006547 tetramer prose conflicts
    with the separately inspected CPX1974 and UniProt dimer-of-heterotrimers annotations;
    the canonical example follows the latter, preserving the source conflict.
  evidence_ids:
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-pmid-12910261
  - plaque-nitrate-agent-bertero-rcsb
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-nitrate-agent-chebi-21137
  - plaque-nitrate-agent-chebi-49883
  - plaque-formate-agent-chebi-60539
  - plaque-formate-agent-chebi-30413
  - plaque-current-1
  - plaque-nitrate-agent-IPR006547
- assessment_id: plaque-current-1-necessity
  area: evidence
  topic: Assembly necessity of conditional subunits
  outcome: unknown
  target_ids:
  - GO:0009325
  summary: CONDITIONAL is an assembly-necessity claim under the schema. The intact-complex/functional
    sources do not isolate the assembly requirements of each row across the generic
    alternatives. This remains unverified; the review does not reinterpret conditional
    as merely catalytic or taxon-specific membership.
  evidence_ids:
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-current-1
  - plaque-policy
- assessment_id: plaque-current-1-grounding
  area: grounding
  topic: Exact protein and family identities
  outcome: supported
  target_ids:
  - GO:0009325
  summary: All three reviewed accession/name/gene/taxon pairs and bounded exact-gene
    queries agree. NarG/NarH mappings match native family classes and named NCBIfam
    members; homolog examples do not narrow the full family to one K-12 sequence.
    No optional NarI family or additional inventory is forced.
  evidence_ids:
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-nitrate-agent-query-narG
  - plaque-nitrate-agent-query-narH
  - plaque-nitrate-agent-query-narI
  - plaque-nitrate-agent-IPR006468
  - plaque-nitrate-agent-IPR006547
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-current-1
- assessment_id: plaque-current-1-distribution
  area: scope
  topic: Unrelated domain-distribution citation
  outcome: concern
  target_ids:
  - GO:0009325
  summary: Both distribution rows cite health economics rather than nitrate reductases.
    The Richardson review abstract independently supports broad prokaryotic diversity
    at a secondary tier but is not the rows cited source and does not verify every
    haloarchaeal/hyperthermophile or frequency claim. The added generic eukaryotic/assimilatory
    cofactor scope is not established by the NarGHI structure.
  evidence_ids:
  - plaque-nitrate-agent-pmid-12950096
  - plaque-nitrate-agent-pmid-11289299
  - plaque-nitrate-agent-pmid-17964535
  - plaque-nitrate-agent-pmid-12910261
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-current-1
- assessment_id: plaque-current-1-function
  area: evidence
  topic: Reduction and redox-loop coupling
  outcome: supported
  target_ids:
  - GO:0009325
  summary: Quinol oxidation and nitrate reduction are directly defined in GO0160182
    and described in native CPX/UniProt and Bertero primary abstract. The study-specific
    electron-transfer route is supported at those tiers, while a detailed full-body
    assay or proton-pathway audit is unavailable.
  evidence_ids:
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-nitrate-agent-bertero-rcsb
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-current-1
- assessment_id: plaque-current-1-completeness
  area: completeness
  topic: Known composition versus optional additions
  outcome: supported
  target_ids:
  - GO:0009325
  summary: The existing NarGHI exemplar has complete stated subunit examples. No missing
    image, additional taxon, nonprotein component row, or generic inventory is itself
    a finding; the concrete corrections concern present claims.
  evidence_ids:
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-go
  - plaque-current-1
  - plaque-policy
- assessment_id: plaque-current-1-graph
  area: graph
  topic: Membership/activity summary versus mechanism
  outcome: concern
  target_ids:
  - GO:0009325
  summary: All five nodes and four edges were inspected. The component roles describe
    an electron-transfer sequence, but the graph connects each protein only by part-of
    and the complete structure to its activity. It does not represent transfer through
    the subunits or cofactor/quinone steps.
  evidence_ids:
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-current-1
  - plaque-graph-policy
- assessment_id: plaque-current-2-identity
  area: identity
  topic: Generic photosystem and exact hierarchy
  outcome: supported
  target_ids:
  - GO:0009521
  summary: GO0009521 is an exact generic structure class with correct is-a, parthood
    and narrow synonym scopes. The appended oxygenic/anoxygenic language should remain
    broader than the two cyanobacterial exemplars. No single PSI/PSII structure is
    substituted for the generic identity.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-current-2
- assessment_id: plaque-current-2-composition
  area: evidence
  topic: Cofactor allocation within oxygenic PSI
  outcome: concern
  target_ids:
  - GO:0009521
  summary: PsaA/PsaB are valid oxygenic type-I constituents, but their stated binding
    of FX,FA,FB is wrong at the declared heterodimer scope. Jordan directly places
    only FX between PsaA/PsaB and assigns FA/FB to PsaC. Whole-PSI electron flow through
    all three centers does not make all three PsaA/PsaB-bound cofactors.
  evidence_ids:
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-P0A406
  - plaque-photosystem-agent-P0A408
  - plaque-photosystem-agent-pdb-1jb0-3
  - plaque-current-2
- assessment_id: plaque-current-2-psii
  area: evidence
  topic: Oxygenic type-II exemplar
  outcome: supported
  target_ids:
  - GO:0009521
  summary: Umena supports the named D1/D2 reaction-center class and its P680-associated
    chlorophylls, pheophytins and quinones; D1 contributes most Mn4CaO5 ligands, with
    a direct CP43 ligand too. These named oxygenic components are examples, not a
    universal L/M description of all anoxygenic type-II centers. The broad generic
    class remains valid.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-photosystem-agent-P51765
  - plaque-photosystem-agent-D0VWR8
  - plaque-current-2
- assessment_id: plaque-current-2-pigments
  area: evidence
  topic: Antenna inventory and mechanistic inference
  outcome: supported
  target_ids:
  - GO:0009521
  summary: The primary PSI structure directly resolves chlorophyll and carotenoid
    architecture. Its excitation-transfer and triplet-quenching discussion combines
    structural distances with cited functional work and qualified inference. Bacteriochlorophyll
    is a generic anoxygenic class possibility, not a chemical observed in Jordan's
    chlorophyll-a preparation.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-current-2
- assessment_id: plaque-current-2-necessity
  area: evidence
  topic: Assembly necessity remains independent
  outcome: unknown
  target_ids:
  - GO:0009521
  summary: Alternative photosystem types explain membership scope, but do not establish
    CONDITIONAL assembly necessity. Exact component-removal assembly endpoints were
    not established by these intact crystal structures. Likewise, ESSENTIAL for the
    grouped antenna-pigment class remains unverified as a class-wide formation requirement.
    Catalytic necessity, photoprotection, resolved membership and stable assembly
    are not interchangeable; no finding is made solely for an untested removal assay.
  evidence_ids:
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-policy
  - plaque-current-2
- assessment_id: plaque-current-2-examples
  area: grounding
  topic: Four reviewed accessions and bounded uniqueness
  outcome: supported
  target_ids:
  - GO:0009521
  summary: 'All four declared accession/gene/status/taxon pairs and exact-node reviewed
    queries agree. These identity-only examples are distinct from crystallographic
    chain identity: RCSB1JB0 maps its PsaA/PsaB chains to P0A405/P0A407 at BP-1 tax197221,
    although its original source-organism field retains tax32046. That conflict affects
    the canonical example and is separately flagged; it does not make record P0A406/P0A408
    identity annotations false.'
  evidence_ids:
  - plaque-photosystem-agent-P0A406
  - plaque-photosystem-agent-P0A408
  - plaque-photosystem-agent-P51765
  - plaque-photosystem-agent-D0VWR8
  - plaque-photosystem-agent-tax-1117
  - plaque-photosystem-agent-tax-32046
  - plaque-photosystem-agent-tax-32053
  - plaque-photosystem-agent-psi-unique
  - plaque-photosystem-agent-uniprot-unique
  - plaque-photosystem-agent-pdb-1jb0
  - plaque-photosystem-agent-pdb-1jb0-1
  - plaque-photosystem-agent-pdb-1jb0-2
  - plaque-photosystem-agent-pdb-1jb0-3
  - plaque-current-2
  - plaque-taxonomy-PSI-P0A405
  - plaque-taxonomy-PSI-P0A407
  - plaque-taxonomy-bp1
- assessment_id: plaque-current-2-literature
  area: evidence
  topic: Primary versus annotation and abstract tiers
  outcome: supported
  target_ids:
  - GO:0009521
  summary: Jordan was read from a genuine public HTTP PDF mirror after an HTTPS certificate
    failure; Umena from a genuine HTTPS PDF. Main-body/caption scopes are recorded.
    Kamiya2003/Kawakami2009 remain citation/abstract plus verified UniProt location-attribution
    tier because attempted JATS routes failed. No unread-body detail is credited.
  evidence_ids:
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-photosystem-agent-epmc
  - plaque-photosystem-agent-P51765
  - plaque-photosystem-agent-D0VWR8
  - plaque-photosystem-agent-jordan2001-publisher
  - plaque-current-2
- assessment_id: plaque-current-2-taxa
  area: scope
  topic: Cyanobacterial distribution and canonical preparations
  outcome: supported
  target_ids:
  - GO:0009521
  summary: The named taxa and historical vulcanus synonyms agree with native taxonomy.
    COMMON Cyanobacteriota is compatible with the native PSI definition and the oxygenic
    sources, without claiming universality or a measured prevalence. Jordan's source
    and PDB metadata use S.elongatus; Umena uses the native synonym T.vulcanus. Exact
    cultured stock equivalence is not independently reconstructed.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-photosystem-agent-pdb-1jb0
  - plaque-photosystem-agent-tax-1117
  - plaque-photosystem-agent-tax-32046
  - plaque-photosystem-agent-tax-32053
  - plaque-current-2
- assessment_id: plaque-current-2-function
  area: scope
  topic: Scoped electron transport
  outcome: supported
  target_ids:
  - GO:0009521
  summary: The function already restricts the P700/ferredoxin path to oxygenic/cyanobacterial
    PSI and explicitly excludes a universal bacterial type-I interpretation. This
    is supported. Coupling to ATP/reductant production belongs to the photosynthetic
    electron-transport system; neither PSI alone nor PSII alone is claimed as a complete
    ATP-synthesis enzyme.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-current-2
- assessment_id: plaque-current-2-graph
  area: graph
  topic: Membership and output versus causal path
  outcome: concern
  target_ids:
  - GO:0009521
  summary: All six nodes and five edges were inspected; two gene/protein nodes correctly
    inherit all four accessions. The graph contains three constituent edges, a membrane
    parthood edge and a whole-structure output. Correcting the PsaC cofactor allocation
    does not turn these relationships into a represented charge-separation/transfer
    causal path. MECHANISTIC therefore overstates its current explanatory detail.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-current-2
  - plaque-graph-policy
- assessment_id: plaque-current-2-completeness
  area: completeness
  topic: Bounded corrections
  outcome: supported
  target_ids:
  - GO:0009521
  summary: The PsaC issue is an affirmative wrong binding allocation, not an automatic
    demand for an optional missing component row. No full accessory inventory, extra
    family identifier, image or measured-property field is required merely because
    it is absent. The whole maintained target and all declared stable identifiers/source
    identities were checked.
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-photosystem-agent-epmc
  - plaque-current-2
  - plaque-policy
- assessment_id: plaque-current-0-provenance
  area: provenance
  topic: Historical frozen input and current observation
  outcome: supported
  summary: Original record hash is unchanged.
  target_ids:
  - GO:0009326
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-original-validation
- assessment_id: plaque-current-0-native
  area: schema
  topic: Native identity and graph example gates
  outcome: supported
  summary: Actual native verify and causal-graphs commands passed at source head;
    declared component examples cover all named graph symbols. These checks do not
    establish mechanism or resolve the scientific findings.
  target_ids:
  - GO:0009326
  evidence_ids:
  - plaque-native-formate_dehydrogenase_complex-verify
  - plaque-native-formate_dehydrogenase_complex-causal
- assessment_id: plaque-current-1-provenance
  area: provenance
  topic: Historical frozen input and current observation
  outcome: supported
  summary: Original record hash is unchanged.
  target_ids:
  - GO:0009325
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-original-validation
- assessment_id: plaque-current-1-native
  area: schema
  topic: Native identity and graph example gates
  outcome: supported
  summary: Actual native verify and causal-graphs commands passed at source head;
    declared component examples cover all named graph symbols. These checks do not
    establish mechanism or resolve the scientific findings.
  target_ids:
  - GO:0009325
  evidence_ids:
  - plaque-native-nitrate_reductase_complex-verify
  - plaque-native-nitrate_reductase_complex-causal
- assessment_id: plaque-current-2-provenance
  area: provenance
  topic: Historical frozen input and current observation
  outcome: supported
  summary: 'The only changed scientific fields are both reaction-center core types
    from PROTEIN to PROTEIN_COMPLEX, plus the dated #2420 history entry. Fresh primary/authority
    sources support both heterodimer groupings. Old cofactor and graph findings remain;
    this refresh does not edit records.'
  target_ids:
  - GO:0009521
  evidence_ids:
  - plaque-current-2
  - plaque-original-2
  - plaque-original-validation
  - plaque-energy-category-prior
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-historical-issue2420
- assessment_id: plaque-current-2-native
  area: schema
  topic: Native identity and graph example gates
  outcome: supported
  summary: Actual native verify and causal-graphs commands passed at source head;
    declared component examples cover all named graph symbols. These checks do not
    establish mechanism or resolve the scientific findings.
  target_ids:
  - GO:0009521
  evidence_ids:
  - plaque-native-photosystem-verify
  - plaque-native-photosystem-causal
- assessment_id: plaque-current-0-adapter
  area: evidence
  topic: Bounded matching MG1655 expression context
  outcome: supported
  summary: MG1655 gene searches resolve FdnG/H/I and FdoG/H/I; FdnG/H are thresholded
    in67, FdnG additionally69, while FdnI/Fdo genes have no above-threshold memberships
    in this dataset. Native module/member annotations were inspected and structural
    source claims separately checked. This corrects unsupported original no-expression
    N/A rationale. MG1655 is one K-12 context, not every strain/class; thresholds
    are not biological absence, and generated module prose/activity inference is excluded.
    The historical unavailable adapter runner was not rerun by this subreview.
  target_ids:
  - GO:0009326
  evidence_ids:
  - plaque-adapter-policy
  - plaque-adapter-datasets
  - plaque-adapter-meta
  - plaque-adapter-search-fdnG
  - plaque-adapter-search-fdnH
  - plaque-adapter-search-fdnI
  - plaque-adapter-search-fdoG
  - plaque-adapter-search-fdoH
  - plaque-adapter-search-fdoI
  - plaque-adapter-gene-modules-fdnG
  - plaque-adapter-gene-modules-fdnH
  - plaque-adapter-gene-modules-fdnI
  - plaque-adapter-gene-modules-fdoG
  - plaque-adapter-gene-modules-fdoH
  - plaque-adapter-gene-modules-fdoI
  - plaque-adapter-summary-67
  - plaque-adapter-members-67
  - plaque-adapter-summary-69
  - plaque-adapter-members-69
  - plaque-current-0
- assessment_id: plaque-current-1-adapter
  area: evidence
  topic: Bounded matching MG1655 expression context
  outcome: supported
  summary: MG1655 NarG/H/I all occur in module67; NarG additionally69 and NarH/I additionally21.
    Native module/member annotations were inspected and structural source claims separately
    checked. This corrects unsupported original no-expression N/A rationale. MG1655
    is one K-12 context, not every strain/class; thresholds are not biological absence,
    and generated module prose/activity inference is excluded. The historical unavailable
    adapter runner was not rerun by this subreview.
  target_ids:
  - GO:0009325
  evidence_ids:
  - plaque-adapter-policy
  - plaque-adapter-datasets
  - plaque-adapter-meta
  - plaque-adapter-search-narG
  - plaque-adapter-search-narH
  - plaque-adapter-search-narI
  - plaque-adapter-gene-modules-narG
  - plaque-adapter-gene-modules-narH
  - plaque-adapter-gene-modules-narI
  - plaque-adapter-summary-21
  - plaque-adapter-members-21
  - plaque-adapter-summary-67
  - plaque-adapter-members-67
  - plaque-adapter-summary-69
  - plaque-adapter-members-69
  - plaque-current-1
- assessment_id: plaque-current-2-adapter
  area: evidence
  topic: PCC7942 computational context and thermophile exclusion
  outcome: supported
  summary: Catalogue S.elongatus coverage resolves specifically to PCC7942. Bounded
    psaA/psaB searches give Synpcc7942_2049/2048 and module38 Photosystems; all44
    returned members and the actual publication body support a computational expression
    context. The record gene names can be cross-checked there, but this is not Jordan
    BP-1 or Umena vulcanus evidence. No matching thermophilic dataset is listed in
    the retrieved catalogue; psbA/psbD paralog search hits from PCC7942 are excluded
    as substitutes for record tax32053. No new runner execution is claimed.
  target_ids:
  - GO:0009521
  evidence_ids:
  - plaque-adapter-policy
  - plaque-adapter-datasets
  - plaque-adapter-syn-meta
  - plaque-adapter-syn-search-psaA
  - plaque-adapter-syn-search-psaB
  - plaque-adapter-syn-search-psbA
  - plaque-adapter-syn-search-psbD
  - plaque-adapter-syn-modules-psaA
  - plaque-adapter-syn-modules-psaB
  - plaque-adapter-syn-summary-38
  - plaque-adapter-syn-members-38
  - plaque-adapter-syn-publication
  - plaque-adapter-syn-primary
  - plaque-taxonomy-pcc7942
  - plaque-taxonomy-bp1
- assessment_id: plaque-current-2-source-taxon
  area: scope
  topic: Jordan thermophilic canonical example versus modern taxon
  outcome: concern
  summary: Jordan uses historical thermophilic S.elongatus naming. Later primary structural
    literature identifies its1JB0 preparation as Thermosynechococcus elongatus BP-1;
    current tax authority and SIFTS-linked P0A405/P0A407 resolve BP-1 to Thermosynechococcus
    vestitus tax197221. Canonical example tax32046 belongs to the separate Synechococcus
    lineage. Preserve the conflicting original RCSB source field rather than silently
    trusting or averaging it; correct the source-specific canonical mapping through
    curation.
  target_ids:
  - GO:0009521
  evidence_ids:
  - plaque-current-2
  - plaque-photosystem-jordan-http
  - plaque-semchonok2021-pdf
  - plaque-taxonomy-bp1
  - plaque-photosystem-agent-tax-32046
  - plaque-photosystem-agent-pdb-1jb0-1
  - plaque-photosystem-agent-pdb-1jb0-2
  - plaque-taxonomy-PSI-P0A405
  - plaque-taxonomy-PSI-P0A407
- assessment_id: plaque-historical-core-types
  area: representation
  topic: Scoped historical component-type resolution
  outcome: supported
  summary: 'Current record already types both named heterodimeric cores PROTEIN_COMPLEX;
    fresh primary structure evidence supports this grouping. Its existing2026-10-24
    history and closed#2420 document a prior record correction. This resolves only
    this single-target category F1, not the seven other #2420 records or all37 category
    assessments; no record correction made by PR2354.'
  target_ids:
  - GO:0009521
  evidence_ids:
  - plaque-current-2
  - plaque-energy-category-prior
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-schema
  - plaque-historical-issue2420
- assessment_id: micro-proton_transporting_v_type_atpase_complex-identity
  area: identity
  topic: Exact generic complex/sector identity, hierarchy and nomenclature
  outcome: supported
  summary: The generic GO identity and labelled parent/part relations resolve; generic
    versus vacuolar subtype distinctions are real. Correct identity is retained while
    the source/graph concerns below remain. No single protein is substituted for the
    structure.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-go
- assessment_id: micro-proton_transporting_v_type_atpase_complex-schema
  area: schema
  topic: Original schema/render and unchanged frozen scientific input
  outcome: supported
  summary: Original native validate and render --content passed. The current target
    is byte-identical to the original frozen input and current main. Existing PROPOSED
    history is not promoted. This slice requires current reassessment but no stale-input
    refresh.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-go
  - micro-original-roundtrip
  - micro-prior-proton_transporting_v_type_atpase_complex
- assessment_id: micro-proton_transporting_v_type_atpase_complex-protein
  area: grounding
  topic: Prose yeast gene identity and bounded native protein diagnostics
  outcome: supported
  summary: 'All named yeast Vma/Vph1/Stv1 mappings inspected in the bounded reviewed
    UniProt result agree with the corresponding yeast subunit identities. Records
    maintain no protein_examples or GENE_OR_PROTEIN graph nodes: both native checks
    passed with empty scope. Neither these zero counts nor the prose-name query establish
    necessity, universal family coverage or protist nomenclature.'
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-named-yeast-genes
  - micro-native-proton_transporting_v_type_atpase_complex-verify
  - micro-native-proton_transporting_v_type_atpase_complex-causal
- assessment_id: micro-proton_transporting_v_type_atpase_complex-taxon
  area: evidence
  topic: Taxon, localization and reference tiers
  outcome: supported
  summary: Taxon 4932 is S. cerevisiae. Kane 2006 is a secondary yeast-focused review
    and supports this canonical-organism context; Li/Kane and Forgac are secondary
    context at the sections actually read. Vph1 vacuolar and Stv1 Golgi/endosomal
    distinctions are retained. No independent population-frequency or universal protist
    composition claim follows from these sources.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-tax-4932
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-literature-metadata
- assessment_id: micro-proton_transporting_v_type_atpase_complex-adapter
  area: scope
  topic: Structured-source applicability for named yeast examples
  outcome: not_applicable
  summary: Current iModulonDB catalogue inspection finds no organism/dataset match
    for named S. cerevisiae or other eukaryotic examples. No matched-gene/module summarization
    follows for those examples. The original no-expression-inference rationale is
    corrected by actual organism coverage. Historical runner unavailable; fresh direct
    catalogue fallback is distinct. The generic bacterial V/A extension is underdetermined
    because no species/strain/gene pair is named; this does not assert absence of
    bacterial ATPase datasets.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-prior-proton_transporting_v_type_atpase_complex
- assessment_id: micro-proton_transporting_v_type_atpase_complex-access
  area: provenance
  topic: Current primary access and historical source reuse
  outcome: supported
  summary: Current Zhao2015 publisher access is abstract-only; its explicit yeast
    ten-proteolipid result, three eukaryotic stalks and rotor/stator distinction are
    sufficient for the retained bounded findings. Earlier full-body/Methods assertions
    belong only to the immutable original observation. No fresh JTY002, DDM, nucleotide-condition
    or subunit-e-loss audit is claimed. Secondary material and authority identities
    are labelled separately.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-prior-proton_transporting_v_type_atpase_complex
- assessment_id: micro-proton_transporting_v_type_atpase_complex-necessity
  area: scope
  topic: Assembly, physiological activity and purification limits
  outcome: unknown
  summary: Evidence for proton pumping, vacuolar pH or localization is not automatically
    evidence of structural assembly necessity. Secondary assembly discussions distinguish
    incomplete/inactive complexes and preserve route uncertainty. No current inspection
    proves universal ESSENTIAL membership or exact assembly context across all fungi/protists;
    preparation-level facts outside the fresh primary abstract remain historical-only.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-zhao2015-abstract
- assessment_id: micro-proton_transporting_v_type_atpase_complex-optional
  area: completeness
  topic: Optional fields and representation coverage
  outcome: not_applicable
  summary: No image, quantitative property, verbatim snippet, associated-trait assertion
    or maintained UniProt/family inventory occurs in these targets. Their absence
    is not converted into a quota-based finding. Native protein-check emptiness and
    the named-gene source audit are both disclosed.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-native-proton_transporting_v_type_atpase_complex-verify
  - micro-native-proton_transporting_v_type_atpase_complex-causal
- assessment_id: micro-proton_transporting_v_type_atpase_complex-broad-localization
  area: scope
  topic: Broad acidocalcisome and unspecified bacterial extension
  outcome: unknown
  summary: 'The exact acidocalcisome extension is not established by the inspected
    primary abstract or the stated secondary sections; no contradictory biological
    claim is made. The broad bacterial V/A remark is not itself treated as a family
    error: Kane distinguishes related archaeal/bacterial enzymes and their functional
    diversity. Neither phrase supplies a particular bacterial adapter match.'
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-kane2006-secondary
  - micro-zhao2015-abstract
  - micro-adapter-catalogue
- assessment_id: micro-proton_transporting_v_type_atpase_complex-finding-f1
  area: scope
  topic: Qualify compartment-specific sector examples within the generic complex
  outcome: concern
  summary: The only component rows use vacuolar GO0000220/0000221 and are marked ESSENTIAL
    without an example scope, while the record identity includes organelle and plasma-membrane
    V-ATPases. Their labels and mappings are correct for vacuolar instances; the issue
    is their unqualified use as the broad class inventory.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-li2009-secondary
- assessment_id: micro-proton_transporting_v_type_atpase_complex-finding-f2
  area: graph
  topic: Match graph scope to the represented coupling
  outcome: concern
  summary: Parthood and whole-complex activity edges do not encode the ATP-hydrolysis,
    rotor and translocation transitions described in prose. MECHANISTIC promises more
    than this graph represents.
  target_ids:
  - GO:0033176
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-graph-policy
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-identity
  area: identity
  topic: Exact generic complex/sector identity, hierarchy and nomenclature
  outcome: supported
  summary: The generic GO identity and labelled parent/part relations resolve; generic
    versus vacuolar subtype distinctions are real. Correct identity is retained while
    the source/graph concerns below remain. No single protein is substituted for the
    structure.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-go
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-schema
  area: schema
  topic: Original schema/render and unchanged frozen scientific input
  outcome: supported
  summary: Original native validate and render --content passed. The current target
    is byte-identical to the original frozen input and current main. Existing PROPOSED
    history is not promoted. This slice requires current reassessment but no stale-input
    refresh.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-go
  - micro-original-roundtrip
  - micro-prior-proton_transporting_v_type_atpase_v0_domain
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-protein
  area: grounding
  topic: Prose yeast gene identity and bounded native protein diagnostics
  outcome: supported
  summary: 'All named yeast Vma/Vph1/Stv1 mappings inspected in the bounded reviewed
    UniProt result agree with the corresponding yeast subunit identities. Records
    maintain no protein_examples or GENE_OR_PROTEIN graph nodes: both native checks
    passed with empty scope. Neither these zero counts nor the prose-name query establish
    necessity, universal family coverage or protist nomenclature.'
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-named-yeast-genes
  - micro-native-proton_transporting_v_type_atpase_v0_domain-verify
  - micro-native-proton_transporting_v_type_atpase_v0_domain-causal
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-taxon
  area: evidence
  topic: Taxon, localization and reference tiers
  outcome: supported
  summary: Taxon 4932 is S. cerevisiae. Kane 2006 is a secondary yeast-focused review
    and supports this canonical-organism context; Li/Kane and Forgac are secondary
    context at the sections actually read. Vph1 vacuolar and Stv1 Golgi/endosomal
    distinctions are retained. No independent population-frequency or universal protist
    composition claim follows from these sources.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-tax-4932
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-literature-metadata
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-adapter
  area: scope
  topic: Structured-source applicability for named yeast examples
  outcome: not_applicable
  summary: Current iModulonDB catalogue inspection finds no organism/dataset match
    for named S. cerevisiae or other eukaryotic examples. No matched-gene/module summarization
    follows for those examples. The original no-expression-inference rationale is
    corrected by actual organism coverage. Historical runner unavailable; fresh direct
    catalogue fallback is distinct. No bacterial matched organism is asserted by this
    target.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-prior-proton_transporting_v_type_atpase_v0_domain
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-access
  area: provenance
  topic: Current primary access and historical source reuse
  outcome: supported
  summary: Current Zhao2015 publisher access is abstract-only; its explicit yeast
    ten-proteolipid result, three eukaryotic stalks and rotor/stator distinction are
    sufficient for the retained bounded findings. Earlier full-body/Methods assertions
    belong only to the immutable original observation. No fresh JTY002, DDM, nucleotide-condition
    or subunit-e-loss audit is claimed. Secondary material and authority identities
    are labelled separately.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-prior-proton_transporting_v_type_atpase_v0_domain
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-necessity
  area: scope
  topic: Assembly, physiological activity and purification limits
  outcome: unknown
  summary: Evidence for proton pumping, vacuolar pH or localization is not automatically
    evidence of structural assembly necessity. Secondary assembly discussions distinguish
    incomplete/inactive complexes and preserve route uncertainty. No current inspection
    proves universal ESSENTIAL membership or exact assembly context across all fungi/protists;
    preparation-level facts outside the fresh primary abstract remain historical-only.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-zhao2015-abstract
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-optional
  area: completeness
  topic: Optional fields and representation coverage
  outcome: not_applicable
  summary: No image, quantitative property, verbatim snippet, associated-trait assertion
    or maintained UniProt/family inventory occurs in these targets. Their absence
    is not converted into a quota-based finding. Native protein-check emptiness and
    the named-gene source audit are both disclosed.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-native-proton_transporting_v_type_atpase_v0_domain-verify
  - micro-native-proton_transporting_v_type_atpase_v0_domain-causal
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-finding-f1
  area: scope
  topic: Bind the decamer and assembly model to the source organism
  outcome: concern
  summary: The added definition exports a decameric proteolipid ring, yeast gene names
    and ER assembly account to yeasts, fungi and protists while naming only generic
    GO0033179 as its source. GO supplies a six-or-more description; inspected primary
    evidence establishes ten subunits in the particular yeast enzyme. The precise
    composition and assembly context need explicit source/taxon limits, without declaring
    the underlying yeast model false.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
- assessment_id: micro-proton_transporting_v_type_atpase_v0_domain-finding-f2
  area: graph
  topic: Make the rotation endpoint agree with its c-ring description
  outcome: concern
  summary: The drives-rotation-of edge correctly describes the proteolipid c-ring
    moving relative to subunit a but points to the entire V0 domain. V0 includes stationary
    elements, so the typed endpoint should identify the rotor or use a relationship
    that preserves the explicitly correct substructure scope.
  target_ids:
  - GO:0033179
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-graph-policy
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-identity
  area: identity
  topic: Exact generic complex/sector identity, hierarchy and nomenclature
  outcome: supported
  summary: The generic GO identity and labelled parent/part relations resolve; generic
    versus vacuolar subtype distinctions are real. Correct identity is retained while
    the source/graph concerns below remain. No single protein is substituted for the
    structure.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-go
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-schema
  area: schema
  topic: Original schema/render and unchanged frozen scientific input
  outcome: supported
  summary: Original native validate and render --content passed. The current target
    is byte-identical to the original frozen input and current main. Existing PROPOSED
    history is not promoted. This slice requires current reassessment but no stale-input
    refresh.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-go
  - micro-original-roundtrip
  - micro-prior-proton_transporting_v_type_atpase_v1_domain
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-protein
  area: grounding
  topic: Prose yeast gene identity and bounded native protein diagnostics
  outcome: supported
  summary: 'All named yeast Vma/Vph1/Stv1 mappings inspected in the bounded reviewed
    UniProt result agree with the corresponding yeast subunit identities. Records
    maintain no protein_examples or GENE_OR_PROTEIN graph nodes: both native checks
    passed with empty scope. Neither these zero counts nor the prose-name query establish
    necessity, universal family coverage or protist nomenclature.'
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-named-yeast-genes
  - micro-native-proton_transporting_v_type_atpase_v1_domain-verify
  - micro-native-proton_transporting_v_type_atpase_v1_domain-causal
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-taxon
  area: evidence
  topic: Taxon, localization and reference tiers
  outcome: supported
  summary: Taxon 4932 is S. cerevisiae. Kane 2006 is a secondary yeast-focused review
    and supports this canonical-organism context; Li/Kane and Forgac are secondary
    context at the sections actually read. Vph1 vacuolar and Stv1 Golgi/endosomal
    distinctions are retained. No independent population-frequency or universal protist
    composition claim follows from these sources.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-tax-4932
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-literature-metadata
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-adapter
  area: scope
  topic: Structured-source applicability for named yeast examples
  outcome: not_applicable
  summary: Current iModulonDB catalogue inspection finds no organism/dataset match
    for named S. cerevisiae or other eukaryotic examples. No matched-gene/module summarization
    follows for those examples. The original no-expression-inference rationale is
    corrected by actual organism coverage. Historical runner unavailable; fresh direct
    catalogue fallback is distinct. No bacterial matched organism is asserted by this
    target.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-prior-proton_transporting_v_type_atpase_v1_domain
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-access
  area: provenance
  topic: Current primary access and historical source reuse
  outcome: supported
  summary: Current Zhao2015 publisher access is abstract-only; its explicit yeast
    ten-proteolipid result, three eukaryotic stalks and rotor/stator distinction are
    sufficient for the retained bounded findings. Earlier full-body/Methods assertions
    belong only to the immutable original observation. No fresh JTY002, DDM, nucleotide-condition
    or subunit-e-loss audit is claimed. Secondary material and authority identities
    are labelled separately.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-forgac2007-summary
  - micro-prior-proton_transporting_v_type_atpase_v1_domain
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-necessity
  area: scope
  topic: Assembly, physiological activity and purification limits
  outcome: unknown
  summary: Evidence for proton pumping, vacuolar pH or localization is not automatically
    evidence of structural assembly necessity. Secondary assembly discussions distinguish
    incomplete/inactive complexes and preserve route uncertainty. No current inspection
    proves universal ESSENTIAL membership or exact assembly context across all fungi/protists;
    preparation-level facts outside the fresh primary abstract remain historical-only.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-kane2006-secondary
  - micro-li2009-secondary
  - micro-zhao2015-abstract
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-optional
  area: completeness
  topic: Optional fields and representation coverage
  outcome: not_applicable
  summary: No image, quantitative property, verbatim snippet, associated-trait assertion
    or maintained UniProt/family inventory occurs in these targets. Their absence
    is not converted into a quota-based finding. Native protein-check emptiness and
    the named-gene source audit are both disclosed.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-native-proton_transporting_v_type_atpase_v1_domain-verify
  - micro-native-proton_transporting_v_type_atpase_v1_domain-causal
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-finding-f1
  area: provenance
  topic: Attach the expanded stalk description to the supporting literature
  outcome: concern
  summary: The definition names only GO:0033180 as source while adding three peripheral
    stalks and yeast Vma protein names. The freshly accessible Zhao2015 primary abstract
    explicitly supports three stalks at its eukaryotic/yeast scopes, whereas the inspected
    older Kane2006 review retains less settled stalk models. Correct evidence placement
    and qualify yeast nomenclature instead of treating GO as the source of every detail.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-named-yeast-genes
- assessment_id: micro-proton_transporting_v_type_atpase_v1_domain-finding-f2
  area: graph
  topic: Match graph scope to its parthood and activity summary
  outcome: concern
  summary: The graph contains no represented hydrolysis-to-rotation or V0-coupling
    transition; its two edges give containment and whole-sector function. MECHANISTIC
    is stronger than the actual directed explanation.
  target_ids:
  - GO:0033180
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-graph-policy
- assessment_id: septin-S2354-A1
  area: identity
  topic: Generic septum versus completed division septum
  outcome: supported
  target_ids:
  - GO:0030428
  summary: The structure identity, broad parent and synonym types match native GO.
    The opening definition reproduces GO wording, including its unusual material phrasing;
    that inherited wording is not treated as an independently invented record error.
    The completed-division-septum function explicitly narrows its context. Division-site
    parthood is supported in the bacterial division context, without asserting a newly
    verified universal relation for every fungal cross-wall.
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-record-cell_septum
- assessment_id: septin-S2354-A2
  area: scope
  topic: Appended cross-domain claims lack matching cited support
  outcome: concern
  target_ids:
  - GO:0030428
  summary: The added definition assigns pseudomurein/S-layer septa to archaea, chitin/beta-glucan
    septa and actomyosin/septin control to fungi, and FtsZ-directed synthesis to prokaryotes.
    The sole definition_source is GO0030428, which supplies none of these extensions.
    The two literature sources are bacterial reviews. These source scopes do not establish
    the broad materials/mechanism formulation.
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-septum-agent-doi-10.1111_j.1749-6632.2012.06818.x
  - septin-septum-agent-doi-10.1146_annurev-biophys-121219-081703
  - septin-record-cell_septum
- assessment_id: septin-S2354-A3
  area: grounding
  topic: Material identity and deposition context
  outcome: concern
  target_ids:
  - GO:0030428
  summary: 'Septal peptidoglycan is a supported bacterial constituent. Its label-only
    rationale unnecessarily requires a septum-specific chemical identifier: native
    CHEBI8005 grounds the material class while role and evidence can preserve its
    bacterial septal location. CONDITIONAL is bounded by walled bacterial context;
    this audit does not infer an assembly knockout result or a particular cross-link
    composition.'
  evidence_ids:
  - septin-septum-agent-chebi-8005
  - septin-septum-agent-jats-PMC8610174
  - septin-septum-agent-doi-10.1111_j.1749-6632.2012.06818.x
  - septin-septum-agent-doi-10.1146_annurev-biophys-121219-081703
  - septin-record-cell_septum
  - septin-policy
- assessment_id: septin-S2354-A4
  area: scope
  topic: Qualified bacterial occurrence and model examples
  outcome: supported
  target_ids:
  - GO:0030428
  summary: The Bacteria row explicitly limits itself to walled FtsZ-dividing bacteria.
    The review supports septal synthesis in E.coli and B.subtilis; taxonomy receipts
    distinguish K-12 strain from B.subtilis species. COMMON is qualitative occurrence,
    not a surveyed proportion. Exact experimental stock identity is not inferred from
    the broad review.
  evidence_ids:
  - septin-septum-agent-jats-PMC8610174
  - septin-septum-agent-tax-2
  - septin-septum-agent-tax-83333
  - septin-septum-agent-tax-1423
  - septin-record-cell_septum
- assessment_id: septin-S2354-A5
  area: evidence
  topic: Completed septum compartmentalization
  outcome: supported
  target_ids:
  - GO:0030428
  summary: The daughter-cell function cites the exact narrower GO0000935 definition
    and explicitly says completed division septum. It does not require every developmental
    septum or porous hyphal cross-wall to block all exchange. Bacterial septal material
    and its division-plane context remain supported independently of the definition-scope
    problem.
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-record-cell_septum
- assessment_id: septin-S2354-A6
  area: graph
  topic: Descriptive topology is overstated as mechanism
  outcome: concern
  target_ids:
  - GO:0030428
  summary: The graph contains two parthood edges and one whole-septum mediates compartmentalization
    edge. Those descriptions preserve useful bounded structural context but do not
    encode a causal transition from material deposition or closure to the function.
    MECHANISTIC overstates the represented explanation.
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-record-cell_septum
  - septin-policy
- assessment_id: septin-S2354-A7
  area: completeness
  topic: Optional inventories and state
  outcome: supported
  target_ids:
  - GO:0030428
  summary: No universal protein inventory, stoichiometry, dimensions, image or trait
    link is required. Further fungal/archaeal components need their own scoped evidence.
    No verbatim snippet is present to verify. PROPOSED status and historical events
    are preserved; this review does not certify historical authorship.
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-record-cell_septum
  - septin-policy
- assessment_id: septin-S2354-A8
  area: evidence
  topic: Bounded structured-source applicability
  outcome: supported
  summary: FtsZ wording triggers applicability. Fresh catalogue matches E. coli precise1k
    and B. subtilis modulome. Exact ftsZ searches and gene records identify b0095
    and BSU_15290. Returned memberships are all below stored module thresholds (201/72
    rows), so no positive module requires summary. This contextual result neither
    proves nor refutes septal function and does not repair cross-domain definition
    sourcing.
  target_ids:
  - GO:0030428
  evidence_ids:
  - septin-record-cell_septum
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
  - septin-adapter-policy
  - septin-adapter-e_coli-precise1k-ftsZ-search
  - septin-adapter-b_subtilis-modulome-ftsZ-search
  - septin-adapter-e_coli-precise1k-b0095
  - septin-adapter-e_coli-precise1k-b0095-imodulons
  - septin-adapter-b_subtilis-modulome-BSU_15290
  - septin-adapter-b_subtilis-modulome-BSU_15290-imodulons
- assessment_id: septin-S2354-A9
  area: schema
  topic: Current native checks and frozen original provenance
  outcome: supported
  summary: Original native schema/render and target hashes pass. Root current protein
    verification/causal commands exit0 with empty inventory and zero gene-protein
    nodes; these checks do not independently validate narrative molecules or assembly
    necessity.
  target_ids:
  - GO:0030428
  evidence_ids:
  - septin-original-native-checks
  - septin-native-cell_septum-verify
  - septin-native-cell_septum-causal
- assessment_id: septin-S2354-A10
  area: identity
  topic: Specialized region of the plasma membrane
  outcome: supported
  target_ids:
  - GO:0033101
  summary: The GO identity, membrane parent, cellular-bud/plasma-membrane parthood
    and UniProt location xref agree. The exact bud membrane synonym is supported.
    A membrane region is distinguished from the bud as a whole and the growth machinery.
  evidence_ids:
  - septin-bud-membrane-agent-go
  - septin-bud-membrane-agent-SL-0028
  - septin-bud-membrane-agent-SL-0027
  - septin-record-cellular_bud_membrane
- assessment_id: septin-S2354-A11
  area: grounding
  topic: Collective lipid boundary and protein boundary
  outcome: supported
  target_ids:
  - GO:0033101
  summary: The component denotes the collective lipid bilayer surrounding the bud,
    not one identified lipid molecule. Leaving this assemblage label-only is justified;
    a generic individual lipid CURIE would not name its composition. ESSENTIAL is
    interpretable here as the defining lipid boundary required for a membrane to exist,
    not as evidence that any particular lipid species or recruited factor is individually
    necessary. The resolved exocyst/Pea2/Spa2 discussion is a representation boundary,
    not a claim of no protein association.
  evidence_ids:
  - septin-bud-membrane-agent-go
  - septin-bud-membrane-agent-SL-0028
  - septin-bud-membrane-agent-SL-0027
  - septin-bud-membrane-agent-valtz1996-pdf
  - septin-bud-membrane-agent-finger-body
  - septin-bud-membrane-agent-finger-methods
  - septin-record-cellular_bud_membrane
  - septin-policy
- assessment_id: septin-S2354-A12
  area: evidence
  topic: Budding yeast and polarized membrane growth
  outcome: supported
  target_ids:
  - GO:0033101
  summary: Valtz supports S.cerevisiae budding/polarity context; Finger supports polarized
    secretion sites at bud cortex. The growth function combines this directly observed
    site organization with the study introduction/discussion account of membrane delivery.
    It does not claim a measured membrane-growth rate, complete exocyst mechanism
    or a prevalence census.
  evidence_ids:
  - septin-bud-membrane-agent-go
  - septin-bud-membrane-agent-tax-4932
  - septin-bud-membrane-agent-doi-10.1083_jcb.135.3.725
  - septin-bud-membrane-agent-doi-10.1016_S0092-8674_00_80948-4
  - septin-bud-membrane-agent-valtz1996-pdf
  - septin-bud-membrane-agent-finger-body
  - septin-bud-membrane-agent-finger-methods
  - septin-record-cellular_bud_membrane
- assessment_id: septin-S2354-A13
  area: graph
  topic: Explicitly nonmechanistic membrane topology
  outcome: supported
  target_ids:
  - GO:0033101
  summary: The surrounds and plasma-membrane parthood edges match GO/UniProt. NONMECHANISTIC
    and its scope note accurately limit the graph to topology, while leaving secretion
    and polarity machinery in cited discussion.
  evidence_ids:
  - septin-bud-membrane-agent-go
  - septin-bud-membrane-agent-SL-0028
  - septin-bud-membrane-agent-SL-0027
  - septin-record-cellular_bud_membrane
- assessment_id: septin-S2354-A14
  area: completeness
  topic: Bounded clean review
  outcome: supported
  target_ids:
  - GO:0033101
  summary: No concrete scientific-record corrective issue was observed. Exact lipid
    species, quantities, protein examples, image, trait link and full mechanism are
    not mandatory optional inventories. Evidence uses notes, not unverifiable quotations.
    PROPOSED state and history are preserved.
  evidence_ids:
  - septin-bud-membrane-agent-go
  - septin-bud-membrane-agent-valtz1996-pdf
  - septin-bud-membrane-agent-finger-body
  - septin-bud-membrane-agent-finger-methods
  - septin-record-cellular_bud_membrane
  - septin-policy
- assessment_id: septin-S2354-A15
  area: evidence
  topic: Bounded structured-source applicability
  outcome: not_applicable
  summary: Specific Sec3/Pea2/Spa2 localization and polarity claims trigger molecular
    applicability despite exclusion from the lipid-boundary inventory. Fresh catalogue
    contains no S. cerevisiae dataset; downstream organism-matched gene/module requests
    are not applicable. No expression-claim exemption or bacterial taxon substitution
    is used.
  target_ids:
  - GO:0033101
  evidence_ids:
  - septin-record-cellular_bud_membrane
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
  - septin-adapter-policy
- assessment_id: septin-S2354-A16
  area: schema
  topic: Current native checks and frozen original provenance
  outcome: supported
  summary: Original native schema/render and target hashes pass. Root current protein
    verification/causal commands exit0 with empty inventory and zero gene-protein
    nodes; these checks do not independently validate narrative molecules or assembly
    necessity.
  target_ids:
  - GO:0033101
  evidence_ids:
  - septin-original-native-checks
  - septin-native-cellular_bud_membrane-verify
  - septin-native-cellular_bud_membrane-causal
- assessment_id: septin-S2354-A17
  area: identity
  topic: Individual mineral scale, distinct from covering and vesicle
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: The local identifier uniquely resolves to the maintained scale record.
    OTHER kind avoids calling one scale a continuous layer. The broad GO parent is
    appropriate, while vesicle, entire coccosphere and narrower holo-/heterococcolith
    types retain separate identities. No unconditional vesicle parthood or exclusively
    extracellular development is asserted.
  evidence_ids:
  - septin-current-local-ids
  - septin-coccolith-agent-go
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-jats-PMC13089448
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccolith
- assessment_id: septin-S2354-A18
  area: grounding
  topic: Mineral grounding and unresolved organic chemistry
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: The calcite grounding is exact at mineral-material level. Associated organic
    material is experimentally supported, but oxidation and morphology do not identify
    one polymer or protein family. REVIEWED_LABEL_ONLY and UNKNOWN necessity correctly
    preserve that limit. Post-assembly persistence after oxidation does not establish
    dispensability for formation.
  evidence_ids:
  - septin-coccolith-agent-chebi-46719
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-jats-PMC13089448
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccolith
  - septin-policy
- assessment_id: septin-S2354-A19
  area: scope
  topic: Two species examples retain their experimental preparation
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: Native taxa match the named species. RCC1130 is established by the supplement;
    CCMP374 calcified donor identity is established separately from naked recipient
    cultures in Johns. No generic crystal count, size, shape, broad prevalence or
    single-morphotype adsorption rule is promoted.
  evidence_ids:
  - septin-coccolith-agent-tax-127549
  - septin-coccolith-agent-tax-2903
  - septin-coccolith-agent-doi-10.1021_jacs.6c02151
  - septin-coccolith-agent-doi-10.1093_pnasnexus_pgag104
  - septin-coccolith-agent-doi-10.1126_sciadv.adc8728
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-avrahami2026-supp
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccolith
- assessment_id: septin-S2354-A20
  area: evidence
  topic: Covering element and scoped adsorption
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: Individual scales demonstrably contribute to an external covering. The
    adsorption function is limited to the tested E.huxleyi system and organic-removal
    comparison. The record does not infer universal adaptive protection, exact adhesion
    chemistry or nucleation-template mechanism.
  evidence_ids:
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-jats-PMC13089448
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccolith
- assessment_id: septin-S2354-A21
  area: provenance
  topic: Exact image, license and preparation
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: The local unmodified Figure1 byte hashes, PMC accession and media locator
    agree. JATS licenses the article under CC BY4.0, and attribution agrees with author
    metadata. Mixed SEM/diagram/AFM content is explicitly described; species and sample
    preparation remain scoped.
  evidence_ids:
  - septin-coccolith-agent-image
  - septin-coccolith-agent-package-PMC13067266
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-avrahami2026-supp
  - septin-coccolith-agent-doi-10.1021_jacs.6c02151
  - septin-coccolith-agent-doi-10.1093_pnasnexus_pgag104
  - septin-coccolith-agent-doi-10.1126_sciadv.adc8728
  - septin-record-coccolith
- assessment_id: septin-S2354-A22
  area: completeness
  topic: Boundaries and optional omissions are justified
  outcome: supported
  target_ids:
  - cellstructuremech:coccolith
  summary: No concrete scientific-record corrective issue was observed. Unidentified
    vesicle particles are not imported as scale constituents; unresolved organic inventory
    and crystal-ordering mechanisms remain explicit. No causal graph, trait link or
    numeric property is required solely because the source contains one. No verbatim
    snippet or status promotion is present.
  evidence_ids:
  - septin-coccolith-agent-jats-PMC13067266
  - septin-coccolith-agent-jats-PMC13089448
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccolith
  - septin-policy
- assessment_id: septin-S2354-A23
  area: evidence
  topic: Bounded structured-source applicability
  outcome: not_applicable
  summary: The target contains calcite and unresolved mixed organic material, without
    an identified gene/locus/protein constituent or named molecular pathway assertion.
    Generic unidentified vesicle densities/full-ATPase comparison is explicitly excluded
    from the target composition. The sparse material/morphology scope does not require
    gene/module searches. Fresh catalogue additionally has no matching named haptophyte
    dataset; no expression or biological absence inferred.
  target_ids:
  - cellstructuremech:coccolith
  evidence_ids:
  - septin-record-coccolith
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
  - septin-adapter-policy
- assessment_id: septin-S2354-A24
  area: schema
  topic: Current native checks and frozen original provenance
  outcome: supported
  summary: Original native schema/render and target hashes pass. Root current protein
    verification/causal commands exit0 with empty inventory and zero gene-protein
    nodes; these checks do not independently validate narrative molecules or assembly
    necessity.
  target_ids:
  - cellstructuremech:coccolith
  evidence_ids:
  - septin-original-native-checks
  - septin-native-coccolith-verify
  - septin-native-coccolith-causal
- assessment_id: septin-S2354-A25
  area: identity
  topic: Whole covering and structural parthood
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: The local coccosphere identity uniquely resolves. External encapsulating
    structure is a broader parent; has_part points to the separately frozen individual-scale
    record. Scale, whole covering, vesicle and organic matrix are kept distinct. ENVELOPE_LAYER
    does not assert exactly one geometric layer.
  evidence_ids:
  - septin-current-local-ids
  - septin-record-coccolith
  - septin-coccosphere-agent-go
  - septin-coccosphere-agent-jats-PMC5896503
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccosphere
- assessment_id: septin-S2354-A26
  area: grounding
  topic: Calcite and mixed extracellular material
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Calcite is correctly grounded. The matrix is supported by lectin staining
    and retained pattern after decalcification but is not a chemically identified
    polymer or protein family. Label-only identity and UNKNOWN formation necessity
    are appropriate. Intracellular tubulin imaged during division is not thereby a
    constituent of the external covering.
  evidence_ids:
  - septin-coccolith-agent-chebi-46719
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-record-coccosphere
  - septin-policy
- assessment_id: septin-S2354-A27
  area: scope
  topic: CS-369 and PLY182g contexts
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Taxon authorities match each species and the older C.pelagicus-subspecies
    name. Xu documents CS-369 and pooled light/CO2 conditions; Walker documents PLY182g.
    Counting assumptions, preparation, species differences and treatment context are
    accurately retained instead of promoting universal plate numbers or layer counts.
  evidence_ids:
  - septin-coccolith-agent-tax-2903
  - septin-coccosphere-agent-tax-221442
  - septin-coccosphere-agent-doi-10.7717_peerj.4608
  - septin-coccosphere-agent-doi-10.1111_nph.15272
  - septin-coccolith-agent-doi-10.1126_sciadv.adc8728
  - septin-coccosphere-agent-jats-PMC5896503
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-record-coccosphere
- assessment_id: septin-S2354-A28
  area: evidence
  topic: Covering organization and daughter-cell separation
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: SEM supports the collective-covering function. Walker supports rearrangement
    during division and an association between disrupted covering and failure of daughter-cell
    separation in Ge/HEDP-treated C.braarudii. The record explicitly distinguishes
    this from failure of initial cytokinesis, low-Ca effects and universal calcification
    requirements; it retains confounding-treatment and adhesion-mechanism uncertainty.
  evidence_ids:
  - septin-coccosphere-agent-jats-PMC5896503
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-record-coccosphere
- assessment_id: septin-S2354-A29
  area: scope
  topic: Scale origin and ecological boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Johns establishes adsorption from external donor scales, including mixed
    morphotypes/species. Structural has_part does not imply same-host biosynthesis.
    The record avoids treating every attached scale as a reconstructed covering or
    assigning a universal antiviral, grazing-protection or photosynthetic benefit.
  evidence_ids:
  - septin-coccolith-agent-jats-PMC9858585
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-record-coccosphere
- assessment_id: septin-S2354-A30
  area: provenance
  topic: Exact SEM figure and source-specific license
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: Local Figure2 SHA-256 and media MD5 match the record and native PMC package.
    The source caption identifies white1micrometre bars and red neighboring counts.
    Culture/SEM preparation and estimated whole-sphere counts are correctly qualified.
    Full source-specific attribution satisfies the inspected CC BY4.0 statement.
  evidence_ids:
  - septin-coccosphere-agent-image
  - septin-coccosphere-agent-package-PMC5896503
  - septin-coccosphere-agent-jats-PMC5896503
  - septin-coccosphere-agent-doi-10.7717_peerj.4608
  - septin-coccosphere-agent-doi-10.1111_nph.15272
  - septin-coccolith-agent-doi-10.1126_sciadv.adc8728
  - septin-record-coccosphere
- assessment_id: septin-S2354-A31
  area: completeness
  topic: Supported boundaries with acknowledged unknowns
  outcome: supported
  target_ids:
  - cellstructuremech:coccosphere
  summary: No concrete scientific-record corrective issue was observed. Exact matrix
    chemistry, assembly mechanism, counts, causal graph and traits are not mandatory
    inventories. Omitted intracellular cytoskeleton is an explicit boundary decision,
    not a claim that it cannot affect division or trafficking. PROPOSED status and
    historical events remain unchanged.
  evidence_ids:
  - septin-coccosphere-agent-jats-PMC5896503
  - septin-coccosphere-agent-jats-PMC6175242
  - septin-coccolith-agent-jats-PMC9858585
  - septin-record-coccosphere
  - septin-policy
- assessment_id: septin-S2354-A32
  area: evidence
  topic: Bounded structured-source applicability
  outcome: not_applicable
  summary: The target contains calcite and unresolved mixed organic material, without
    an identified gene/locus/protein constituent or named molecular pathway assertion.
    Generic intracellular tubulin imaging is explicitly excluded from the target composition.
    The sparse material/morphology scope does not require gene/module searches. Fresh
    catalogue additionally has no matching named haptophyte dataset; no expression
    or biological absence inferred.
  target_ids:
  - cellstructuremech:coccosphere
  evidence_ids:
  - septin-record-coccosphere
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
  - septin-adapter-policy
- assessment_id: septin-S2354-A33
  area: schema
  topic: Current native checks and frozen original provenance
  outcome: supported
  summary: Original native schema/render and target hashes pass. Root current protein
    verification/causal commands exit0 with empty inventory and zero gene-protein
    nodes; these checks do not independently validate narrative molecules or assembly
    necessity.
  target_ids:
  - cellstructuremech:coccosphere
  evidence_ids:
  - septin-original-native-checks
  - septin-native-coccosphere-verify
  - septin-native-coccosphere-causal
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0009326
  - GO:0009325
  - GO:0009521
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - GO:0030428
  - GO:0033101
  - cellstructuremech:coccolith
  - cellstructuremech:coccosphere
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
  issue_key: formate-dehydrogenase-complex-unrelated-distribution-reference
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Replace the unrelated taxonomic-distribution citation
  description: Both bacterial and archaeal distribution claims cite PMID11884601,
    which resolves to a study of HA95/PKA and EBV-mediated transcription. It provides
    no support for formate-dehydrogenase occurrence, frequency, or conservation in
    either domain. The E.coli FDH-N structure supports a specific bacterial example,
    not the uncited archaeal/general-frequency claims.
  target_ids:
  - GO:0009326
  field_paths:
  - taxonomic_distribution[0].reference
  - taxonomic_distribution[1].reference
  - taxonomic_distribution[0].note
  - taxonomic_distribution[1].note
  evidence_ids:
  - plaque-formate-agent-pmid-11884601
  - plaque-formate-agent-pmid-11884747
  - plaque-jormakka-browser-main
  - plaque-formate-agent-go
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-current-0
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: A material asserted biological claim has an unrelated supporting
    citation or contradicts the demonstrated reaction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100134Z-formate-dehydrogenase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2613
- finding_id: plaque-t0-F2
  issue_key: formate-dehydrogenase-complex-graph-explanatory-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the supported electron-transfer steps or narrow graph scope
  description: The FUNCTION graph is marked MECHANISTIC but contains only three constituent
    part-of edges and one whole-complex activity edge. These relationships are sound
    for the named example, yet they do not express the causal transfer route described
    in the prose. Preserve them as NONMECHANISTIC or add experimentally scoped electron-transfer
    transitions. Do not infer that a generic class always has this species-specific
    subunit set.
  target_ids:
  - GO:0009326
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].edges
  evidence_ids:
  - plaque-formate-agent-go
  - plaque-formate-agent-CPX-1975
  - plaque-jormakka-browser-main
  - plaque-jormakka-browser-beta
  - plaque-jormakka-browser-later
  - plaque-current-0
  - plaque-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported constituent membership and activity remain valid;
    the defect is bounded to explanatory graph scope.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100134Z-formate-dehydrogenase-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2614
- finding_id: plaque-t1-F1
  issue_key: nitrate-reductase-complex-reversed-definition-reaction
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the reversed nitrate/nitrite reaction while preserving the upstream
    conflict
  description: The definition opening and structure-node description assert formation
    of nitrate from nitrite. Native GO0009325 currently contains that same wording,
    but the record itself and independent GO0160182/CPX1974/Bertero abstract evidence
    describe the nitrate-to-nitrite reaction. This is a material direction contradiction,
    not an identity mismatch or proof that every nitrite-oxidizing enzyme is the target.
  target_ids:
  - GO:0009325
  field_paths:
  - definition
  - causal_graphs[0].nodes[node_id=nitrate_reductase_complex].description
  evidence_ids:
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-nitrate-agent-P09152
  - plaque-nitrate-agent-P11349
  - plaque-nitrate-agent-P11350
  - plaque-current-1
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: A material asserted biological claim has an unrelated supporting
    citation or contradicts the demonstrated reaction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100137Z-nitrate-reductase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2615
- finding_id: plaque-t1-F2
  issue_key: nitrate-reductase-complex-unrelated-distribution-reference
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Replace the unrelated taxonomic-distribution citation
  description: Both bacterial and archaeal rows cite PMID12950096, a health-economics
    study of willingness to pay. It cannot support nitrate-reductase occurrence or
    frequency. Other readable secondary/native sources provide bounded context, but
    do not validate that attached citation or all detailed taxon claims.
  target_ids:
  - GO:0009325
  field_paths:
  - taxonomic_distribution[0].reference
  - taxonomic_distribution[1].reference
  - taxonomic_distribution[0].note
  - taxonomic_distribution[1].note
  evidence_ids:
  - plaque-nitrate-agent-pmid-12950096
  - plaque-nitrate-agent-pmid-11289299
  - plaque-nitrate-agent-pmid-17964535
  - plaque-nitrate-agent-pmid-12910261
  - plaque-formate-agent-tax-83333
  - plaque-formate-agent-tax-2
  - plaque-formate-agent-tax-2157
  - plaque-current-1
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: A material asserted biological claim has an unrelated supporting
    citation or contradicts the demonstrated reaction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100137Z-nitrate-reductase-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2616
- finding_id: plaque-t1-F3
  issue_key: nitrate-reductase-complex-graph-explanatory-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the supported electron-transfer steps or narrow graph scope
  description: The FUNCTION graph is marked MECHANISTIC but contains only three constituent
    part-of edges and one whole-complex activity edge. These relationships are sound
    for the named example, yet they do not express the causal transfer route described
    in the prose. Preserve them as NONMECHANISTIC or add experimentally scoped electron-transfer
    transitions. Do not infer that a generic class always has this species-specific
    subunit set.
  target_ids:
  - GO:0009325
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].edges
  evidence_ids:
  - plaque-nitrate-agent-go
  - plaque-nitrate-agent-CPX-1974
  - plaque-nitrate-agent-pmid-12910261
  - plaque-current-1
  - plaque-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported constituent membership and activity remain valid;
    the defect is bounded to explanatory graph scope.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100137Z-nitrate-reductase-complex-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2617
- finding_id: plaque-t2-F1
  issue_key: photosystem-psaa-psab-terminal-cluster-allocation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Assign FA and FB to PsaC rather than the PsaA/PsaB heterodimer
  description: The type-I core role and duplicated graph descriptions say the PsaA/PsaB
    heterodimer binds FX,FA,FB. Jordan2001 pp911 and913 explicitly place FA/FB in
    the separate stromal PsaC subunit, while FX is jointly ligated by PsaA/PsaB. The
    full PSI electron-transfer sequence is correct but has been conflated with the
    binding inventory of one component.
  target_ids:
  - GO:0009521
  field_paths:
  - components[component_id=type_i_reaction_center_core].role
  - causal_graphs[graph_id=photosystem_mechanism].nodes[node_id=type_i_reaction_center_core].description
  - causal_graphs[graph_id=photosystem_mechanism].edges[subject=type_i_reaction_center_core].description
  evidence_ids:
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-P0A406
  - plaque-photosystem-agent-P0A408
  - plaque-photosystem-agent-pdb-1jb0-3
  - plaque-current-2
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
  rule_id: 'review-checklist: component roles, exact source support and causal graph
    scope'
  native_severity: major
  normalization_reason: The declared molecular actor is assigned cofactors that the
    cited primary structure allocates to a separate subunit.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100138Z-photosystem-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2618
- finding_id: plaque-t2-F2
  issue_key: photosystem-membership-output-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Align graph scope with the represented relationships
  description: The FUNCTION graph is marked MECHANISTIC but consists of constituent/compartment
    parthood and photosystem-to-electron-transport output. The process description
    names P700 excitation and electron transfer, but the graph does not represent
    a directed causal transition among those events. Preserve the supported summary
    as NONMECHANISTIC or encode a bounded source-supported transfer path.
  target_ids:
  - GO:0009521
  field_paths:
  - causal_graphs[graph_id=photosystem_mechanism].scope_status
  - causal_graphs[graph_id=photosystem_mechanism].nodes
  - causal_graphs[graph_id=photosystem_mechanism].edges
  evidence_ids:
  - plaque-photosystem-agent-go
  - plaque-photosystem-jordan-http
  - plaque-current-2
  - plaque-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
  rule_id: 'review-checklist: component roles, exact source support and causal graph
    scope'
  native_severity: minor
  normalization_reason: The supported physical membership/output relationships remain
    valid; the represented graph scope needs a bounded correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100138Z-photosystem-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2619
- finding_id: plaque-t2-F3
  issue_key: photosystem-jordan-canonical-example-taxon-conflation
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile the thermophilic Jordan PSI example with current BP-1 taxonomy
  description: The canonical example attaches Jordan2001 to modern Synechococcus elongatus
    tax32046. The original paper uses historical thermophilic S.elongatus naming,
    but later primary structural literature explicitly identifies its1JB0 preparation
    as Thermosynechococcus elongatus BP-1. Current ENA and the deposition SIFTS-linked
    P0A405/P0A407 identify that strain as Thermosynechococcus vestitus BP-1 tax197221,
    a separate lineage. The original RCSB source-organism field still says32046, so
    the conflict must remain explicit. Identity-only record examples P0A406/P0A408
    correctly resolve to32046 and must not be mislabeled as the exact crystal chains.
    PCC7942 coexpression data cannot support the thermophilic preparation.
  target_ids:
  - GO:0009521
  field_paths:
  - canonical_examples[0].taxon_id
  - canonical_examples[0].taxon_label
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - plaque-current-2
  - plaque-photosystem-jordan-http
  - plaque-semchonok2021-pdf
  - plaque-taxonomy-bp1
  - plaque-photosystem-agent-tax-32046
  - plaque-photosystem-agent-pdb-1jb0-1
  - plaque-photosystem-agent-pdb-1jb0-2
  - plaque-taxonomy-PSI-P0A405
  - plaque-taxonomy-PSI-P0A407
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope
  native_severity: major
  normalization_reason: A source-specific canonical organism is grounded to a different
    modern lineage; generic photosystem identity is unchanged.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2620
- finding_id: plaque-historical-core-types
  issue_key: photosystem-reaction-center-core-component-types
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  title: Heterodimeric reaction-center core components in photosystem.yaml (GO:0009521)
    are typed PROTEIN instead of PROTEIN_COMPLEX
  description: 'In data/structures/energy_complex/photosystem.yaml (GO:0009521), components#type_i_reaction_center_core
    (label: ''Type I (Fe-S type) photosystem reaction center core (PsaA/PsaB)'', gene_symbols:
    [psaA, psaB]) and components#type_ii_reaction_center_core (label: ''Type II (pheophytin-quinone
    type) photosystem reaction center core (D1/PsbA and D2/PsbD)'', gene_symbols:
    [psbA, psbD]) represent heterodimeric reaction-center core subcomplexes rather
    than a single protein family, and should be typed component_type: PROTEIN_COMPLEX.'
  target_ids:
  - GO:0009521
  field_paths:
  - components[0].component_type
  - components[1].component_type
  evidence_ids:
  - plaque-current-2
  - plaque-energy-category-prior
  - plaque-photosystem-jordan-http
  - plaque-photosystem-agent-umena2011-pdf
  - plaque-schema
  - plaque-historical-issue2420
  rule_id: docs/SCHEMA.md:ComponentTypeEnum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained_record
  tags:
  - components
  - component-type
  - stage4-record-review
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261023T230504Z-energy-complex-category-review
    finding_id: F1
  disposition_reason: 'Current record already types both named heterodimeric cores
    PROTEIN_COMPLEX; fresh primary structure evidence supports this grouping. Its
    existing2026-10-24 history and closed#2420 document a prior record correction.
    This resolves only this single-target category F1, not the seven other #2420 records
    or all37 category assessments; no record correction made by PR2354.'
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2420
- finding_id: micro-F1
  issue_key: generic-v-atpase-vacuolar-component-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify compartment-specific sector examples within the generic complex
  description: The only component rows use vacuolar GO0000220/0000221 and are marked
    ESSENTIAL without an example scope, while the record identity includes organelle
    and plasma-membrane V-ATPases. Their labels and mappings are correct for vacuolar
    instances; the issue is their unqualified use as the broad class inventory.
  target_ids:
  - GO:0033176
  field_paths:
  - components[component_id=v0_domain]
  - components[component_id=v1_domain]
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-li2009-secondary
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100139Z-proton-transporting-v-type-atpase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2604
- finding_id: micro-F2
  issue_key: generic-v-atpase-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented coupling
  description: Parthood and whole-complex activity edges do not encode the ATP-hydrolysis,
    rotor and translocation transitions described in prose. MECHANISTIC promises more
    than this graph represents.
  target_ids:
  - GO:0033176
  field_paths:
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_complex_mechanism].scope_status
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_complex_mechanism].edges
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_complex
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100139Z-proton-transporting-v-type-atpase-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2605
- finding_id: micro-F3
  issue_key: generic-v0-yeast-decamer-assembly-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bind the decamer and assembly model to the source organism
  description: The added definition exports a decameric proteolipid ring, yeast gene
    names and ER assembly account to yeasts, fungi and protists while naming only
    generic GO0033179 as its source. GO supplies a six-or-more description; inspected
    primary evidence establishes ten subunits in the particular yeast enzyme. The
    precise composition and assembly context need explicit source/taxon limits, without
    declaring the underlying yeast model false.
  target_ids:
  - GO:0033179
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: An exact numerical composition and assembly context are generalized
    beyond the inspected evidence; the target identity itself remains correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2606
- finding_id: micro-F4
  issue_key: generic-v0-rotating-substructure-endpoint
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Make the rotation endpoint agree with its c-ring description
  description: The drives-rotation-of edge correctly describes the proteolipid c-ring
    moving relative to subunit a but points to the entire V0 domain. V0 includes stationary
    elements, so the typed endpoint should identify the rotor or use a relationship
    that preserves the explicitly correct substructure scope.
  target_ids:
  - GO:0033179
  field_paths:
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_v0_domain_mechanism].edges[subject=v1_catalytic_domain,predicate=drives
    rotation of,object=proton_transporting_v_type_atpase_v0_domain]
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v0_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2607
- finding_id: micro-F5
  issue_key: generic-v1-expanded-architecture-source
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Attach the expanded stalk description to the supporting literature
  description: The definition names only GO:0033180 as source while adding three peripheral
    stalks and yeast Vma protein names. The freshly accessible Zhao2015 primary abstract
    explicitly supports three stalks at its eukaryotic/yeast scopes, whereas the inspected
    older Kane2006 review retains less settled stalk models. Correct evidence placement
    and qualify yeast nomenclature instead of treating GO as the source of every detail.
  target_ids:
  - GO:0033180
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-named-yeast-genes
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2608
- finding_id: micro-F6
  issue_key: generic-v1-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to its parthood and activity summary
  description: The graph contains no represented hydrolysis-to-rotation or V0-coupling
    transition; its two edges give containment and whole-sector function. MECHANISTIC
    is stronger than the actual directed explanation.
  target_ids:
  - GO:0033180
  field_paths:
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_v1_domain_mechanism].scope_status
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_v1_domain_mechanism].edges
  evidence_ids:
  - micro-record-proton_transporting_v_type_atpase_v1_domain
  - micro-go
  - micro-zhao2015-abstract
  - micro-kane2006-secondary
  - micro-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2609
- finding_id: septin-S2354-F1
  issue_key: cell-septum-definition-domain-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Source the expanded definition at its actual domain scope
  description: The appended definition moves beyond native GO into cross-domain material
    assignments and a prokaryote-versus-fungus cytokinetic mechanism. GO0030428 does
    not contain those claims, and the cited reviews concern bacterial division. This
    is a material evidence-scope gap, not a claim that all fungal septation statements
    are false.
  target_ids:
  - GO:0030428
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-septum-agent-doi-10.1111_j.1749-6632.2012.06818.x
  - septin-septum-agent-doi-10.1146_annurev-biophys-121219-081703
  - septin-record-cell_septum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: The extension changes biological and mechanistic scope across
    domains; the correct generic GO identity remains intact.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100142Z-cell-septum-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2610
- finding_id: septin-S2354-F2
  issue_key: cell-septum-peptidoglycan-material-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Separate peptidoglycan identity from its septal location
  description: The component is explicitly bacterial peptidoglycan, but its grounding
    note requires a term that also encodes deposition at division septa. CHEBI8005
    supplies the verified material-class identity. Septal placement and exclusion
    of fungal chitin/glucan can remain in the role and evidence.
  target_ids:
  - GO:0030428
  field_paths:
  - components[component_id=bacterial_septal_peptidoglycan].grounding
  - components[component_id=bacterial_septal_peptidoglycan].grounding_status
  - components[component_id=bacterial_septal_peptidoglycan].grounding_notes
  evidence_ids:
  - septin-septum-agent-chebi-8005
  - septin-septum-agent-jats-PMC8610174
  - septin-record-cell_septum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: A bounded machine-readable material link is withheld; biological
    identity and the bacterial boundary are already correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100142Z-cell-septum-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2611
- finding_id: septin-S2354-F3
  issue_key: cell-septum-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to its topology
  description: The MECHANISTIC graph consists of constituent and context parthood
    plus a whole-structure-to-function mediates edge. It does not represent the material-deposition,
    closure or other causal transition that explains compartmentalization. This concerns
    scope classification, not a demand for atomic detail.
  target_ids:
  - GO:0030428
  field_paths:
  - causal_graphs[graph_id=cell_septum_mechanism].scope_status
  - causal_graphs[graph_id=cell_septum_mechanism].scope_notes
  evidence_ids:
  - septin-septum-agent-go
  - septin-septum-agent-jats-PMC8610174
  - septin-record-cell_septum
  - septin-policy
  - septin-graph-policy
  - septin-graph-contract
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The useful topology can remain after a bounded scope correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T100142Z-cell-septum-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2612
actions:
- action_id: plaque-t0-A1
  finding_ids:
  - plaque-t0-F1
  target_ids:
  - GO:0009326
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  description: Attach relevant, directly inspected distribution sources or narrow/defer
    the unsupported rows.
  acceptance_checks:
  - Preserve the verified broad complex identity and E.coli example.
  - Each bacterial/archaeal occurrence and frequency claim must match its own source;
    do not use one bacterial structure paper to prove archaeal conservation.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
- action_id: plaque-t0-A2
  finding_ids:
  - plaque-t0-F2
  target_ids:
  - GO:0009326
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained scientific record
  description: Match graph scope to its actual explanatory content.
  acceptance_checks:
  - Retain valid membership and activity statements.
  - A mechanistic version must resolve the supported subunit/cofactor electron route
    and distinguish the specific E.coli holoenzyme from the generic class.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
- action_id: plaque-t1-A1
  finding_ids:
  - plaque-t1-F1
  target_ids:
  - GO:0009325
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
  description: Use biologically correct reduction wording and document the source
    discrepancy rather than silently pretending GO already says it.
  acceptance_checks:
  - Nitrate is the reduced substrate and nitrite the product for the stated NarGHI
    reaction.
  - The source-specific GO quotation may remain as an attributed historical/current-source
    observation, but must not serve as an unqualified biological definition.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
- action_id: plaque-t1-A2
  finding_ids:
  - plaque-t1-F2
  target_ids:
  - GO:0009325
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
  description: Source each actual distribution statement appropriately or narrow/defer
    it.
  acceptance_checks:
  - Keep generic class, respiratory NarGHI, periplasmic Nap and assimilatory alternatives
    distinct.
  - Use inspected taxon-specific or explicitly broad sources; retain the secondary
    tier of review-based generalizations.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
- action_id: plaque-t1-A3
  finding_ids:
  - plaque-t1-F3
  target_ids:
  - GO:0009325
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained scientific record
  description: Match graph scope to its actual explanatory content.
  acceptance_checks:
  - Retain valid membership and activity statements.
  - A mechanistic version must resolve the supported subunit/cofactor electron route
    and distinguish the specific E.coli holoenzyme from the generic class.
  - Any scientific correction requires separately authorized guarded curation, append-only
    history, rendering and native validation.
- action_id: plaque-t2-A1
  finding_ids:
  - plaque-t2-F1
  target_ids:
  - GO:0009521
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
  description: Narrow the PsaA/PsaB binding description to P700 and its actual acceptors,
    including shared FX; identify FA/FB as PsaC-bound when describing the complete
    PSI electron path. A new component row is optional, but the existing assignment
    must be corrected.
  acceptance_checks:
  - Check the correction against Jordan Polypeptide subunits p911 and Electron transfer
    chain p913.
  - Keep full-complex electron-transfer order separate from protein-specific coordination
    and reconcile all duplicated role text.
  - Apply only through separately authorized curation with guarded writing/history
    and native focused validation.
- action_id: plaque-t2-A2
  finding_ids:
  - plaque-t2-F2
  target_ids:
  - GO:0009521
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
  description: Retain supported membership and the existing oxygenic-PSI function
    restriction, and either narrow the scope label or represent the relevant charge-separation/transfer
    steps with correct subunit/cofactor actors.
  acceptance_checks:
  - Do not turn every generic photosystem into the same oxygenic PSI mechanism.
  - A source-supported causal transition is sufficient; no atomistic simulation is
    required.
  - Apply only through separately authorized curation with guarded writing/history
    and native focused validation.
- action_id: plaque-t2-A3
  finding_ids:
  - plaque-t2-F3
  target_ids:
  - GO:0009521
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained scientific record
  description: Use the verified BP-1 canonical taxon and retain historical names plus
    the conflicting deposition metadata in source notes. Reassess whether identity-only
    protein examples should remain separate examples; do not silently relabel their
    existing accessions.
  acceptance_checks:
  - Cited Jordan1JB0 preparation maps to the verified thermophilic BP-1 lineage, with
    historical naming explicitly explained.
  - Distinguish record P0A406/P0A408 identity examples from deposition P0A405/P0A407;
    no PCC7942 transcriptome substitution.
  - Separate guarded record curation, history and native validation; no record edit
    in this review PR.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0033176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  description: Use the generic sector identities for a generic inventory or explicitly
    retain the vacuolar rows as scoped examples; reconcile duplicate generic/vacuolar
    graph nodes.
  acceptance_checks:
  - Native GO must preserve generic-versus-vacuolar subtype relations.
  - Yeast vacuolar evidence must not imply universal compartment-specific constituents.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0033176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  description: Classify the current graph as descriptive or add a bounded source-supported
    hydrolysis-to-rotation-to-proton-transport path.
  acceptance_checks:
  - Retain correct distinction between rotor and stationary V0 elements.
  - No invented molecular-detail quota or universal taxon mechanism.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0033179
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
  description: Separate the generic V0 definition from a cited S.cerevisiae structural/assembly
    example; retain historical source uncertainty and obtain matched evidence before
    widening the exact count.
  acceptance_checks:
  - Cite the source actually supporting ten proteolipids and its experimental preparation.
  - Do not infer native subunit dispensability from purification losses; any particular
    preparation-level assertion requires inspection of matched primary Methods, which
    current abstract access does not provide.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0033179
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained scientific record
  description: Introduce a source-supported c-ring/rotor node or change the relation
    to coupling with V0 while retaining the substructure explanation.
  acceptance_checks:
  - The directed relation must not entail rigid-body rotation of all V0.
  - Retain the existing correct functional qualification and real coupling path.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: micro-A5
  finding_ids:
  - micro-F5
  target_ids:
  - GO:0033180
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  description: Add narrow source attribution for the expanded architecture and mark
    the yeast protein names as a scoped example; preserve distinctions between EG
    stalks and other collar/stator elements.
  acceptance_checks:
  - GO-supplied text and later structural evidence must be distinguishable.
  - Do not export yeast gene tokens as independently established protist names.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: micro-A6
  finding_ids:
  - micro-F6
  target_ids:
  - GO:0033180
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  description: Narrow scope for the existing summary or add a source-supported catalytic/rotor
    coupling path.
  acceptance_checks:
  - Preserve the intact-enzyme context and distinguish rotor from stator.
  - No optional complete subunit inventory is required to repair scope.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: septin-S2354-C1
  finding_ids:
  - septin-S2354-F1
  target_ids:
  - GO:0030428
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
  description: Retain the sourced generic definition or add directly inspected, explicitly
    taxon-bounded support for each added material/mechanism claim; avoid treating
    all prokaryotes as sharing one septation apparatus.
  acceptance_checks:
  - Retained statements must be supported at their actual taxon scope.
  - Preserve the narrower completed-division-septum function.
  - Run focused schema and strict-reference checks.
- action_id: septin-S2354-C2
  finding_ids:
  - septin-S2354-F2
  target_ids:
  - GO:0030428
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
  description: Ground the material class to verified CHEBI8005, using a class-level
    label if needed for label correspondence, and retain the septal/bacterial qualifier
    in role and evidence.
  acceptance_checks:
  - Do not equate peptidoglycan with chitin or archaeal pseudomurein.
  - Do not invent exact polymer chemistry or assembly necessity.
  - Run identifier-label, schema and strict-reference checks.
- action_id: septin-S2354-C3
  finding_ids:
  - septin-S2354-F3
  target_ids:
  - GO:0030428
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_septum.yaml
    role: maintained scientific record
  description: Mark the current graph NONMECHANISTIC with an explicit scope note,
    or represent a source-supported causal transition at its taxon and developmental
    scope.
  acceptance_checks:
  - Preserve valid structural edges.
  - Do not generalize bacterial FtsZ dynamics across domains.
  - Run native graph coverage and focused validation.
limitations:
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Jormakka2002 is inspected at preserved browser-rendered author-uploaded main-text/caption
  tier. Native curl returned403; no supplementary Methods, raw diffraction, figure-pixel
  or proton-flux audit. Structure/HQNO-based proton-pathway proposals remain qualified.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Jordan2001 main text/captions were read from a genuine HTTP PDF after an HTTPS certificate
  failure; browser opens also partially failed and remain access receipts. Umena2011
  was read as genuine HTTPS PDF main text/captions/Methods. No raw coordinates, supplementary
  data or image pixels were reanalyzed.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Bertero2003 remains primary abstract plus author-deposition/native-curation tier;
  both publisher and nominal PDF URLs returned subscription HTML. Richardson2001/Rothery2008
  are secondary-review abstracts; Rothery HTTP200 XML was entitlement/metadata, not
  full body.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Kamiya2003/Kawakami2009 were verified at exact metadata/abstract and UniProt location-citation
  attribution tiers; attempted JATS responses500 do not prove global unreadability
  or biological error.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  No full domain-frequency census or component-removal assembly experiment was audited.
  Conditional/essential assembly-necessity values remain unverified where the cited
  intact structures do not establish them; no issue is manufactured from an optional
  empty field.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Bounded family comparisons and exact-node queries are not exhaustive. Generated
  InterPro descriptions marked llm:true and generated iModulon summaries are excluded
  from biological evidence.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Fresh iModulonDB source fallback covers MG1655 and bounded PCC7942 context only.
  The historical unavailable runner was not rerun. Thresholded nonmembership does
  not establish biological absence; module membership does not establish assembly,
  location or mechanism. The catalogue does not list a matching BP-1/vulcanus dataset.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  RCSB1JB0 retains legacy source tax32046 while current SIFTS proteins and primary
  comparative literature identify BP-1. This conflict is preserved as a canonical-example
  finding. PCC7942 context and identity-only P0A406/P0A408 annotations do not resolve
  the historical preparation identity.'
- 'Formate dehydrogenase, nitrate reductase and photosystem independent subreview:
  Only the photosystem target of Oct23 category F1 is dispositioned; no whole-category
  or all-target#2420 resolution is claimed. Record correction was already present
  on main. Root owns current global QC/CI and scientific issue filing.'
- 'Three generic V-type ATPase records independent subreview: Zhao2015 current publisher
  HTML is abstract/deposition-list only and subscription-gates main text. A browser
  attempt encountered Nature identity redirect failure. No current primary Methods,
  figure pixels, raw maps/coordinates, JTY002, detergent/nucleotide conditions or
  subunit-e-loss verification is claimed. Earlier original source access remains explicitly
  historical.'
- 'Three generic V-type ATPase records independent subreview: Kane2006 is secondary:
  inspected Introduction/Structure and stated assembly/targeting sections; Figure1/2
  captions were read without image-pixel review. Li/Kane2009 inspection covers JATS
  S15-S18/P27-P34. Forgac2007 is secondary Key Points/abstract only. Bibliographic
  metadata does not replace unseen full text.'
- 'Three generic V-type ATPase records independent subreview: Native six UniProt commands
  passed on empty maintained protein_examples and zero GENE_OR_PROTEIN nodes. The
  separate bounded fifteen-name yeast UniProt query verifies those mappings only,
  not full family coverage, assembly necessity or protist gene names.'
- 'Three generic V-type ATPase records independent subreview: Historical adapter runner
  unavailable receipt is reused with its actual 00:49Z time and exit1. Fresh direct
  catalogue has no yeast/eukaryotic match; unspecified bacterial V/A prose does not
  identify a matched species/gene. No unrelated bacterial F-type module evidence or
  universal absence inference is substituted.'
- 'Three generic V-type ATPase records independent subreview: No independent frequency
  study, universal composition/assembly model, acidocalcisome-specific source, or
  population-level occurrence estimate was added. These limitations are distinguished
  from the six confirmed original findings.'
- 'Three generic V-type ATPase records independent subreview: All three targets are
  unchanged and original frozen hashes/renderings validate. Original six findings
  retain exact predecessor occurrences; no category-wide or earlier vacuolar-record
  finding is resolved by this generic-record slice.'
- 'Three generic V-type ATPase records independent subreview: Common policy/config/schema/verifier
  context was retained from prior reads, checked byte-identical to this frozen source,
  with applicable adapter/graph sections reread. The three current targets, six original
  YAML/Markdown files and source responses were inspected independently. No tracked
  image or energy-category review was used by this slice.'
- 'Three generic V-type ATPase records independent subreview: Root owns full QC, final
  CI, issue deduplication/publication and immutable successor synthesis. This report
  does not claim their pending or external results.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Independent read-only reassessment of four unchanged targets. Historical bundles
  and receipts remain immutable; current checks and source accesses are separately
  dated. No record or GitHub mutation by reviewer.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Egan full text remains unavailable after an actual fresh Wiley pdfdirect HTTP403;
  exact Europe PMC metadata/abstract only. 2012 electronic publication versus 2013
  issue year is not a separate identity defect. McQuillen is secondary review evidence
  at named body sections; underlying primary experiments were not independently audited.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  No exhaustive archaeal/fungal septation literature survey or direct assembly-removal
  experiment was performed. The definition finding concerns unsupported maintained
  scope, not proof that every appended statement is false.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Valtz genuine PDF was read at specified methods, localization and complex-interpretation
  passages, not every mating assay, strain-table row or image. Finger primary author-uploaded
  indexed body/methods were freshly accessed through browser with declared three-week
  crawl age while direct HTTP returned403. No direct full-text success or entire-paper
  audit claimed.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  The bud lipid bilayer is a collective defining material, not one measured lipid
  species; ESSENTIAL here does not assert an individual lipid knockout endpoint. Localization
  of associated machinery is not proof of complete membrane composition.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Both frozen local images were actually viewed and match fresh native PMC media bytes,
  metadata MD5, record SHA256, figure captions and exact CC BY4.0 permissions. Only
  these two images received pixel inspection. Other source figures are text/caption
  scopes.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Avrahami main text and culture/isolation/SEM/AFM supplement sections were read;
  downstream tomography processing and raw volumes were not reanalysed. Ben-Joseph
  holococcolith supplementary Methods were not audited. Johns detailed virus-encounter
  modelling and supplementary videos were not independently audited.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Walker claim-bearing Methods/Results/Discussion and Figure6/8/9 captions were read;
  movies, source image pixels and raw datasets were not reanalysed. Xu mathematical
  simulations and workbook were not recalculated. Morphology/counting assumptions
  and treatment-specific cell-separation endpoints are retained.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Historical ontology searches and exact current GO-wide absence were not reconstructed.
  Current repository-local exact identifiers were searched with ignored and hidden
  files included; broad GO parents are not asserted to be exact matches.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Mixed organic chemistry and formation necessity remain UNKNOWN. No issue is manufactured
  for optional missing molecule inventories, dimensions, protein examples, causal
  graph or trait links.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Fresh official dataset catalogue and exact organism-matched FtsZ queries are scoped
  to E. coli precise1k and B. subtilis modulome. All-false thresholded membership
  is not biological absence. No positive module hit informs the verdict; no unrelated
  taxon substitution. Runner failure is explicitly historical, not a fresh invocation.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  All eight current native protein commands pass with empty declared exact-protein
  inventories and zero gene-protein graph nodes; they establish neither scientific
  completeness nor narrative protein identity.'
- 'Cell septum, cellular bud membrane, coccolith and coccosphere independent subreview:
  Root owns global QC, issue deduplication/publication and final CI. Three cell-septum
  findings retain exact original lineage; the other targets remain scientifically
  supported with limitations.'
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
  Every inherited finding is reassessed and retains exact predecessor identity.
- 'Bundle issues #2601 (one stale review), #2602 (eight structured-source applicability
  defects) and #2603 (missed photosystem canonical-example source/taxon conflict)
  are addressed here. Separate scientific record-curation findings remain open. Existing
  validator #2514 remains open.'
- 'The frozen October23 energy-category finding photosystem-reaction-center-core-component-types
  targets only GO:0009521. Its corrected current component types are substantively
  reassessed and this exact historical finding is resolved. Already-closed #2420 is
  reused for that scoped lineage; this does not resolve its other historical targets
  anew.'
- Source commit d7ee610a5d142b5961a6057e22437aabb68f191f is retained by tag review-base/pr2354-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration,
  graph/protein policies, verifier source, two target images and the October23 energy-category
  review pair.
- Six energy-complex reviews used unsupported lack-expression exemptions. Cell septum
  and cellular bud membrane omitted applicable molecular-source checks. Coccolith
  and coccosphere morphology/material claims do not require invented gene/module evidence.
- Fresh source inspection retains actual access dates. Primary bodies, abstracts,
  secondary reviews, authority responses, captions and inspected image pixels have
  distinct evidence scopes.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not
  validate molecular mechanisms or names appearing only in prose.
- PCC7942 computational module context is not evidence for the thermophilic preparation
  in Jordan2001. The historical 1JB0 metadata/current taxon and protein mapping conflict
  remains explicit.
- 'Seventeen open scientific findings are linked to #2604–#2620; sixteen preserve
  exact original batch occurrences and one newly identifies the photosystem canonical-example
  taxon/source conflict. The separately resolved category finding retains its exact
  single-target predecessor and already-closed #2420.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100134Z-formate-dehydrogenase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100137Z-nitrate-reductase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100138Z-photosystem-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100139Z-proton-transporting-v-type-atpase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100140Z-proton-transporting-v-type-atpase-v0-domain-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100141Z-proton-transporting-v-type-atpase-v1-domain-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100142Z-cell-septum-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100144Z-cellular-bud-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100145Z-coccolith-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T100146Z-coccosphere-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2354
- https://github.com/CultureBotAI/CellStructureMech/issues/2420
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2601
- https://github.com/CultureBotAI/CellStructureMech/issues/2602
- https://github.com/CultureBotAI/CellStructureMech/issues/2603
- https://github.com/CultureBotAI/CellStructureMech/issues/2604
- https://github.com/CultureBotAI/CellStructureMech/issues/2605
- https://github.com/CultureBotAI/CellStructureMech/issues/2606
- https://github.com/CultureBotAI/CellStructureMech/issues/2607
- https://github.com/CultureBotAI/CellStructureMech/issues/2608
- https://github.com/CultureBotAI/CellStructureMech/issues/2609
- https://github.com/CultureBotAI/CellStructureMech/issues/2610
- https://github.com/CultureBotAI/CellStructureMech/issues/2611
- https://github.com/CultureBotAI/CellStructureMech/issues/2612
- https://github.com/CultureBotAI/CellStructureMech/issues/2613
- https://github.com/CultureBotAI/CellStructureMech/issues/2614
- https://github.com/CultureBotAI/CellStructureMech/issues/2615
- https://github.com/CultureBotAI/CellStructureMech/issues/2616
- https://github.com/CultureBotAI/CellStructureMech/issues/2617
- https://github.com/CultureBotAI/CellStructureMech/issues/2618
- https://github.com/CultureBotAI/CellStructureMech/issues/2619
- https://github.com/CultureBotAI/CellStructureMech/issues/2620
```
