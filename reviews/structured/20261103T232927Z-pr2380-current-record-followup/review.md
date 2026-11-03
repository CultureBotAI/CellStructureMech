# PR 2380: current-input review of ten records and adversarial follow-up

- Review: 20261103T232927Z-pr2380-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T23:15:45.781598Z
- Finished UTC: 2026-11-03T23:29:27Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment refreshes the two stale Pdu and AcrAB-TolC reviews and corrects ten unsupported structured-source applicability exclusions. Six scientific findings remain open across three records (three major and three minor), including one newly observed, narrowly scoped CPX essentiality-attribution issue; seven records have qualified positive assessments. Original observations and scientific records remain unchanged.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 3a10e7b468ffc187a10f8d6b123120f8cdbbcf14. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 71e8b8755cdeab5619000ba0b749999107ecd8c4.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 7b6cd533340948100b7b23d8ab4e659702d9feba.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031472 | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml | maintained | propanediol degradation polyhedral organelle |
| GO:0042644 | data/structures/nucleoid/chloroplast_nucleoid.yaml | maintained | chloroplast nucleoid |
| GO:0020023 | data/structures/nucleoid/kinetoplast.yaml | maintained | kinetoplast |
| GO:0042645 | data/structures/nucleoid/mitochondrial_nucleoid.yaml | maintained | mitochondrial nucleoid |
| GO:0009295 | data/structures/nucleoid/nucleoid.yaml | maintained | nucleoid |
| GO:0042646 | data/structures/nucleoid/plastid_nucleoid.yaml | maintained | plastid nucleoid |
| GO:0000148 | data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml | maintained | 1,3-beta-D-glucan synthase complex |
| GO:0009334 | data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml | maintained | 3-phenylpropionate dioxygenase complex |
| GO:0016590 | data/structures/other/acf_complex.yaml | maintained | ACF complex |
| cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml | maintained | AcrAB-TolC multidrug efflux transport complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0031472 | passed | True | GO:0031472 | Documented focused command passed. |
| validate-strict GO:0031472 | passed | True | GO:0031472 | Documented focused command passed. |
| validate GO:0042644 | passed | True | GO:0042644 | Documented focused command passed. |
| validate-strict GO:0042644 | passed | True | GO:0042644 | Documented focused command passed. |
| validate GO:0020023 | passed | True | GO:0020023 | Documented focused command passed. |
| validate-strict GO:0020023 | passed | True | GO:0020023 | Documented focused command passed. |
| validate GO:0042645 | passed | True | GO:0042645 | Documented focused command passed. |
| validate-strict GO:0042645 | passed | True | GO:0042645 | Documented focused command passed. |
| validate GO:0009295 | passed | True | GO:0009295 | Documented focused command passed. |
| validate-strict GO:0009295 | passed | True | GO:0009295 | Documented focused command passed. |
| validate GO:0042646 | passed | True | GO:0042646 | Documented focused command passed. |
| validate-strict GO:0042646 | passed | True | GO:0042646 | Documented focused command passed. |
| validate GO:0000148 | passed | True | GO:0000148 | Documented focused command passed. |
| validate-strict GO:0000148 | passed | True | GO:0000148 | Documented focused command passed. |
| validate GO:0009334 | passed | True | GO:0009334 | Documented focused command passed. |
| validate-strict GO:0009334 | passed | True | GO:0009334 | Documented focused command passed. |
| validate GO:0016590 | passed | True | GO:0016590 | Documented focused command passed. |
| validate-strict GO:0016590 | passed | True | GO:0016590 | Documented focused command passed. |
| validate cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Documented focused command passed. |
| validate-strict cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | All ten targets contain positive molecular or pathway claims and require applicability assessment. Fresh official catalogue supports matched Salmonella core and E.coli precise1k checks; these are mixed six-strain and five-strain datasets, respectively, not strain-specific physical-assembly evidence. Actual gene/module checks retain thresholds and absent-gene endpoint limits. The catalogue has no matching eukaryotic host for the assigned algal/plant, kinetoplastid and yeast contexts; no unrelated bacterial proxy or biological absence inference is substituted. Historical runner unavailability is retained separately; public-source fallback is current. |
| Independent claim-level source review | passed | True | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native propanediol degradation polyhedral organelle UniProt verify check | passed | True | GO:0031472 | 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native propanediol degradation polyhedral organelle UniProt causal check | passed | True | GO:0031472 | 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native chloroplast nucleoid UniProt verify check | passed | True | GO:0042644 | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native chloroplast nucleoid UniProt causal check | passed | True | GO:0042644 | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native kinetoplast UniProt verify check | passed | True | GO:0020023 | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native kinetoplast UniProt causal check | passed | True | GO:0020023 | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial nucleoid UniProt verify check | passed | True | GO:0042645 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native mitochondrial nucleoid UniProt causal check | passed | True | GO:0042645 | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native nucleoid UniProt verify check | passed | True | GO:0009295 | 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native nucleoid UniProt causal check | passed | True | GO:0009295 | 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid nucleoid UniProt verify check | passed | True | GO:0042646 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native plastid nucleoid UniProt causal check | passed | True | GO:0042646 | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native 1,3-beta-D-glucan synthase complex UniProt verify check | passed | True | GO:0000148 | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native 1,3-beta-D-glucan synthase complex UniProt causal check | passed | True | GO:0000148 | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native 3-phenylpropionate dioxygenase complex UniProt verify check | passed | True | GO:0009334 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native 3-phenylpropionate dioxygenase complex UniProt causal check | passed | True | GO:0009334 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ACF complex UniProt verify check | passed | True | GO:0016590 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native ACF complex UniProt causal check | passed | True | GO:0016590 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native AcrAB-TolC multidrug efflux transport complex UniProt verify check | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native AcrAB-TolC multidrug efflux transport complex UniProt causal check | passed | True | cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact structure versus protein/DNA material identity

identity: supported. Targets: GO:0042644.

GO0042644 is exact; is_a plastid nucleoid and part_of chloroplast stroma are supported by distinct typed native relations.

### Constituent boundaries and exact family/material scope

grounding: supported. Targets: GO:0042644.

Chloroplast DNA and the Chlamydomonas-HLP-represented HU-like class are supported. IPR000119 is broader HU/IHF family context, not an exact chloroplast-localized class; CreCNS is a documented additional factor but absence from a deliberately bounded optional inventory is not itself a defect.

### Native names, reference taxa and inventory

grounding: supported. Targets: GO:0042644.

Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported HLP token is not refuted by a bounded zero UniProt exact-name result. The exact HLP query returns zero across statuses in tax3055; this is a bounded index result, not evidence against the literature gene or absence under other loci.

### Organism, source strain and qualitative presence

scope: supported. Targets: GO:0042644.

Chlamydomonas3055 is exact and source-supported; complete Karcher primary abstract supports RNAi/localization, but full Methods and exact RNAi strain were not accessed. COMMON remains a qualitative synthesis consistent with native presence semantics, not a newly measured prevalence estimate.

### Actor, edge and mechanistic scope

graph: supported. Targets: GO:0042644.

All three FUNCTION/NONMECHANISTIC edges have bounded support: HLP association, cpDNA packaging and HLP knockdown effects. Protein organization/maintenance is not an HLP-only complete formation mechanism.

### Formation necessity versus organization/function

evidence: unknown. Targets: GO:0042644.

DNA is constituting material of this DNA-defined region. Its collective ESSENTIAL designation does not establish necessity of a particular sequence, nor universal requirement for an individual HLP/CNS factor.

### Source identity, experiment and actual access

provenance: supported. Targets: GO:0042644.

Karcher is complete primary abstract only; Kobayashi is genuine primary comparative research with explicitly selected body/Methods/caption scopes. The record verb review is not treated as an assertion that this article is a secondary review.

### Full-assertion structured-source applicability

provenance: supported. Targets: GO:0042644.

HLP organization/maintenance and RNAi narrative positively trigger the native policy. Original expression-only exclusion is unsupported. Fresh full official catalogue has no actual host match; no unrelated prokaryotic proxy or unmatched downstream query. Historical runner failure and current fallback are explicit.

### Actual native validation and protein scope

schema: supported. Targets: GO:0042644.

Original validates and renders exactly; all historical inputs and current target hash match. Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported HLP token is not refuted by a bounded zero UniProt exact-name result. Both fresh root protein commands exit0; this bounded inventory result does not certify every scientific claim.

### History and unresolved discussions

provenance: supported. Targets: GO:0042644.

Current gene/class fields are assessed on their actual source support; dated history/rationale remains historical and is not rewritten. Existing label-only/family discussions remain scoped follow-up, not automatically resolved or converted into mandatory inventory findings. No new record event or status promotion is performed.

### Unasserted images, measurements and trait links

scope: not_applicable. Targets: GO:0042644.

No maintained image/license claim, record measurement, verbatim snippet or associated-trait mapping requires certification. Source captions were read where declared, but no figure pixels, supplements, raw experiments or sequence realignment were independently analyzed.

### Remaining scientific knowledge and coverage

completeness: unknown. Targets: GO:0042644.

No complete constituent census, universal taxon prevalence, exact localized protein-family equivalence or detailed molecular assembly/replication mechanism is certified. Source-specific access and assay limits above remain; optional gaps and uncertain formation requirements are not fabricated findings.

### Current record verdict and finding lineage

completeness: supported. Targets: GO:0042644.

pass_with_limitations: current structure identity, bounded source-supported constituents/functions/taxa and explicitly nonmechanistic graph are positively assessed. No scientific curation finding is established in this assigned target; the original likewise has no findings/actions, so no predecessor or terminal disposition is invented. Bundle applicability correction remains separate.

### Exact structure versus protein/DNA material identity

identity: supported. Targets: GO:0020023.

GO0020023/SL0150 identify the mitochondrial kinetoplast region. Contextual kDNA-network synonyms do not equate an isolated DNA molecule with the entire mitochondrion.

### Constituent boundaries and exact family/material scope

grounding: supported. Targets: GO:0020023.

Mini/maxicircle DNA and compacting DNA-bound KAP cohort are supported. The multi-family class is not every KAP-labelled protein; aKAP23 non-DNA localization and lineage-specific KAP1/2 prevent universal-name or complete T.brucei inventory inference. No forced one-family CURIE is justified.

### Native names, reference taxa and inventory

grounding: supported. Targets: GO:0020023.

Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative literature names, not a verified set of four universal T.brucei accession identities.

### Organism, source strain and qualitative presence

scope: supported. Targets: GO:0020023.

Kinetoplastea5653 and T.brucei5691 are correct. The record explicitly acknowledges architectural diversity; interlocked disk/copy estimates are T.brucei/trypanosomatid context, not every kinetoplastid. Cooper uses EATRO1125-derived cells; Gluenz uses procyclic LISTER427/TREU927/29-13 assays. COMMON remains a qualitative synthesis consistent with native presence semantics, not a newly measured prevalence estimate.

### Actor, edge and mechanistic scope

graph: supported. Targets: GO:0020023.

Four ASSEMBLY/NONMECHANISTIC catenation/condensation edges summarize trypanosomatid network organization. Scope expressly withholds replication enzymology; TAC is relevant segregation context rather than a compulsory DNA-bound component. deSouza localization and secondary compaction synthesis do not establish a completed molecular compaction mechanism.

### Formation necessity versus organization/function

evidence: unknown. Targets: GO:0020023.

All three component essentialities remain UNKNOWN. Different KAP mutations, lineage repertoires and DNA-copy contexts do not establish universal formation necessity.

### Source identity, experiment and actual access

provenance: supported. Targets: GO:0020023.

Amodeo/Jensen are secondary; Cooper/deSouza/Gluenz are primary with specified body scopes. Ogbadoyi is complete-primary-abstract scope despite a fetched unread body. Source counts and secondary proposals are not upgraded into universal experimental proof.

### Full-assertion structured-source applicability

provenance: supported. Targets: GO:0020023.

KAP DNA compaction, guide-RNA editing and genome organization positively trigger the native policy. Original expression-only exclusion is unsupported. Fresh full official catalogue has no actual host match; no unrelated prokaryotic proxy or unmatched downstream query. Historical runner failure and current fallback are explicit.

### Actual native validation and protein scope

schema: supported. Targets: GO:0020023.

Original validates and renders exactly; all historical inputs and current target hash match. Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative literature names, not a verified set of four universal T.brucei accession identities. Both fresh root protein commands exit0; this bounded inventory result does not certify every scientific claim.

### History and unresolved discussions

provenance: supported. Targets: GO:0020023.

Current gene/class fields are assessed on their actual source support; dated history/rationale remains historical and is not rewritten. Existing label-only/family discussions remain scoped follow-up, not automatically resolved or converted into mandatory inventory findings. No new record event or status promotion is performed.

### Unasserted images, measurements and trait links

scope: not_applicable. Targets: GO:0020023.

No maintained image/license claim, record measurement, verbatim snippet or associated-trait mapping requires certification. Source captions were read where declared, but no figure pixels, supplements, raw experiments or sequence realignment were independently analyzed.

### Remaining scientific knowledge and coverage

completeness: unknown. Targets: GO:0020023.

No complete constituent census, universal taxon prevalence, exact localized protein-family equivalence or detailed molecular assembly/replication mechanism is certified. Source-specific access and assay limits above remain; optional gaps and uncertain formation requirements are not fabricated findings.

### Current record verdict and finding lineage

completeness: supported. Targets: GO:0020023.

pass_with_limitations: current structure identity, bounded source-supported constituents/functions/taxa and explicitly nonmechanistic graph are positively assessed. No scientific curation finding is established in this assigned target; the original likewise has no findings/actions, so no predecessor or terminal disposition is invented. Bundle applicability correction remains separate.

### Historical execution cohort versus target review cohort

provenance: supported. Targets: GO:0020023.

Original limitations[0] correctly refers to the actual batch26 execution. All five check scope notes and evidence locators identify f97b1abe and same-base guards for batch26/batch43. This is supported historical provenance, not a cohort-label defect or a current-head execution claim. The tentative label-only concern was withdrawn after reading complete scope notes.

### Exact structure versus protein/DNA material identity

identity: supported. Targets: GO:0042645.

GO0042645/SL0269 identify the nucleoid region; generic-nucleoid is_a, matrix parthood and mitochromosome/location synonyms are correct.

### Constituent boundaries and exact family/material scope

grounding: supported. Targets: GO:0042645.

mtDNA and an Abf2-represented mitochondrial HMG class are supported. IPR009071 is a domain; broad IPR051965 with unchecked LLM prose does not supply exact class equivalence. No complete nucleoid proteome or exact DNA sequence-feature identity is certified.

### Native names, reference taxa and inventory

grounding: supported. Targets: GO:0042645.

One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node. Identity and coverage do not turn every source assay into S288C or prove formation necessity. Exact reviewed ABF2 query returns one Q02486; primary ABF2, synonym HIM1, locusYMR072W/ORFYM9916.11 and S288C identity match.

### Organism, source strain and qualitative presence

scope: supported. Targets: GO:0042645.

S.cerevisiae4932 and S288C559292 reference identity are correct. MCC109/BY4741/W303 assay contexts remain separate from Q02486 reference strain. COMMON remains a qualitative synthesis consistent with native presence semantics, not a newly measured prevalence estimate.

### Actor, edge and mechanistic scope

graph: supported. Targets: GO:0042645.

Yeast FUNCTION/NONMECHANISTIC binding, passive packaging and repeat-stability edges are supported. Kucej uses in organello crosslinking and itself interprets in vivo association; no intact-live-cell ChIP is claimed here. Sia distinguishes frameshifts/deletions from unchanged point-mutation rate.

### Formation necessity versus organization/function

evidence: unknown. Targets: GO:0042645.

UNKNOWN essentiality is retained. Abf2 deletion permits mtDNA retention under respiratory selection; instability or altered compaction is not universal loss of nucleoid formation.

### Source identity, experiment and actual access

provenance: supported. Targets: GO:0042645.

Kucej2008 and Sia2009 genuine scientific main text/Methods or assay footnotes were read; Kucej/Butow2007 remains secondary complete-abstract scope. Fresh access failures and separate recovered successes remain distinct.

### Full-assertion structured-source applicability

provenance: supported. Targets: GO:0042645.

Abf2 packaging and metabolic remodeling positively trigger the native policy. Original expression-only exclusion is unsupported. Fresh full official catalogue has no actual host match; no unrelated prokaryotic proxy or unmatched downstream query. Historical runner failure and current fallback are explicit.

### Actual native validation and protein scope

schema: supported. Targets: GO:0042645.

Original validates and renders exactly; all historical inputs and current target hash match. One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node. Identity and coverage do not turn every source assay into S288C or prove formation necessity. Both fresh root protein commands exit0; this bounded inventory result does not certify every scientific claim.

### History and unresolved discussions

provenance: supported. Targets: GO:0042645.

Current gene/class fields are assessed on their actual source support; dated history/rationale remains historical and is not rewritten. Existing label-only/family discussions remain scoped follow-up, not automatically resolved or converted into mandatory inventory findings. No new record event or status promotion is performed.

### Unasserted images, measurements and trait links

scope: not_applicable. Targets: GO:0042645.

No maintained image/license claim, record measurement, verbatim snippet or associated-trait mapping requires certification. Source captions were read where declared, but no figure pixels, supplements, raw experiments or sequence realignment were independently analyzed.

### Remaining scientific knowledge and coverage

completeness: unknown. Targets: GO:0042645.

No complete constituent census, universal taxon prevalence, exact localized protein-family equivalence or detailed molecular assembly/replication mechanism is certified. Source-specific access and assay limits above remain; optional gaps and uncertain formation requirements are not fabricated findings.

### Current record verdict and finding lineage

completeness: supported. Targets: GO:0042645.

pass_with_limitations: current structure identity, bounded source-supported constituents/functions/taxa and explicitly nonmechanistic graph are positively assessed. No scientific curation finding is established in this assigned target; the original likewise has no findings/actions, so no predecessor or terminal disposition is invented. Bundle applicability correction remains separate.

### Exact structure versus protein/DNA material identity

identity: supported. Targets: GO:0042646.

GO0042646/SL0140 identify the generic plastid nucleoid; generic-nucleoid parent and plastid-stroma parthood are correct, with chloroplast as an exact child subtype.

### Constituent boundaries and exact family/material scope

grounding: supported. Targets: GO:0042646.

Constituting plastid DNA material and variable associated protein complements are supported. The generic graph deliberately excludes lineage-specific protein identities; narrative Chlamydomonas HLP is an example, not a universal plastid requirement. The existing exact-family TODO does not mandate invented groundings.

### Native names, reference taxa and inventory

grounding: supported. Targets: GO:0042646.

Zero examples and zero typed protein nodes; native success is empty inventory scope. HLP-containing narrative elsewhere still triggers applicability.

### Organism, source strain and qualitative presence

scope: supported. Targets: GO:0042646.

Viridiplantae33090 and Chlamydomonas3055 identities are correct. Kobayashi primary comparative and Introduction scope support ordinary green-plant occurrence, not a census of every plastid lineage; HLP evidence remains Chlamydomonas-specific. COMMON remains a qualitative synthesis consistent with native presence semantics, not a newly measured prevalence estimate.

### Actor, edge and mechanistic scope

graph: supported. Targets: GO:0042646.

The two FUNCTION/NONMECHANISTIC edges state stromal containment and DNA packaging; exact GO/SL anatomy supports them. They do not assert an HLP-dependent universal molecular pathway.

### Formation necessity versus organization/function

evidence: unknown. Targets: GO:0042646.

DNA is constituting material of this DNA-defined region. Its collective ESSENTIAL designation does not establish necessity of a particular sequence, nor universal requirement for an individual HLP/CNS factor.

### Source identity, experiment and actual access

provenance: supported. Targets: GO:0042646.

Karcher is complete primary abstract only; Kobayashi is genuine primary comparative research with explicitly selected body/Methods/caption scopes. The record verb review is not treated as an assertion that this article is a secondary review.

### Full-assertion structured-source applicability

provenance: supported. Targets: GO:0042646.

HLP organization/maintenance and RNAi narrative positively trigger the native policy. Original expression-only exclusion is unsupported. Fresh full official catalogue has no actual host match; no unrelated prokaryotic proxy or unmatched downstream query. Historical runner failure and current fallback are explicit.

### Actual native validation and protein scope

schema: supported. Targets: GO:0042646.

Original validates and renders exactly; all historical inputs and current target hash match. Zero examples and zero typed protein nodes; native success is empty inventory scope. HLP-containing narrative elsewhere still triggers applicability. Both fresh root protein commands exit0; this bounded inventory result does not certify every scientific claim.

### History and unresolved discussions

provenance: supported. Targets: GO:0042646.

Current gene/class fields are assessed on their actual source support; dated history/rationale remains historical and is not rewritten. Existing label-only/family discussions remain scoped follow-up, not automatically resolved or converted into mandatory inventory findings. No new record event or status promotion is performed.

### Unasserted images, measurements and trait links

scope: not_applicable. Targets: GO:0042646.

No maintained image/license claim, record measurement, verbatim snippet or associated-trait mapping requires certification. Source captions were read where declared, but no figure pixels, supplements, raw experiments or sequence realignment were independently analyzed.

### Remaining scientific knowledge and coverage

completeness: unknown. Targets: GO:0042646.

No complete constituent census, universal taxon prevalence, exact localized protein-family equivalence or detailed molecular assembly/replication mechanism is certified. Source-specific access and assay limits above remain; optional gaps and uncertain formation requirements are not fabricated findings.

### Current record verdict and finding lineage

completeness: supported. Targets: GO:0042646.

pass_with_limitations: current structure identity, bounded source-supported constituents/functions/taxa and explicitly nonmechanistic graph are positively assessed. No scientific curation finding is established in this assigned target; the original likewise has no findings/actions, so no predecessor or terminal disposition is invented. Bundle applicability correction remains separate.

### Exact original provenance and current native coverage

schema: supported. Targets: GO:0009295.

Own three original YAML/MD pairs validate/render exactly;44 historical input rows match. Current unchanged target inventory: seven reviewed K-12 examples, one COVERED pooled NAP node. Root owns wider current gates.

### Historical rationale and conservative optional grounding

provenance: supported. Targets: GO:0009295.

Dated history and rationale preserved; current source-neutral class TODOs are not contradicted merely by individual protein examples. No neighbor/category finding or prior issue is resolved by inference.

### Actual access and source-tier separation

evidence: supported. Targets: GO:0009295.

Every citation identity and current claim inspected within declared source extent. Secondary synthesis is authority; current challenge/404 responses are access context only. Abstract-only claims retain protocol/strain limits; no pixels, supplements or rawdata reanalysis.

### Scientific outcome separate from bundle repairs

consistency: concern. Targets: GO:0009295.

One inherited major generic-nucleoid identity finding remains open. Applicability repair stays in review bundles; no record edits or future CI/merge certification.

### Exact original provenance and current native coverage

schema: supported. Targets: GO:0000148.

Own three original YAML/MD pairs validate/render exactly;44 historical input rows match. Current unchanged target inventory: three reviewed S288C examples, two COVERED Fks/Rho1 nodes. Root owns wider current gates.

### Historical rationale and conservative optional grounding

provenance: supported. Targets: GO:0000148.

Dated history and rationale preserved; current source-neutral class TODOs are not contradicted merely by individual protein examples. No neighbor/category finding or prior issue is resolved by inference.

### Actual access and source-tier separation

evidence: supported. Targets: GO:0000148.

Every citation identity and current claim inspected within declared source extent. Secondary synthesis is authority; current challenge/404 responses are access context only. Abstract-only claims retain protocol/strain limits; no pixels, supplements or rawdata reanalysis.

### Scientific outcome separate from bundle repairs

consistency: supported. Targets: GO:0000148.

Qualified pass retained; no inherited or new scientific finding confirmed. Applicability repair stays in review bundles; no record edits or future CI/merge certification.

### Exact original provenance and current native coverage

schema: supported. Targets: GO:0016590.

Own three original YAML/MD pairs validate/render exactly;44 historical input rows match. Current unchanged target inventory: two reviewed S288C examples, two COVERED Isw2/Itc1 nodes. Root owns wider current gates.

### Historical rationale and conservative optional grounding

provenance: supported. Targets: GO:0016590.

Dated history and rationale preserved; current source-neutral class TODOs are not contradicted merely by individual protein examples. No neighbor/category finding or prior issue is resolved by inference.

### Actual access and source-tier separation

evidence: supported. Targets: GO:0016590.

Every citation identity and current claim inspected within declared source extent. Secondary synthesis is authority; current challenge/404 responses are access context only. Abstract-only claims retain protocol/strain limits; no pixels, supplements or rawdata reanalysis.

### Scientific outcome separate from bundle repairs

consistency: supported. Targets: GO:0016590.

Qualified pass retained; no inherited or new scientific finding confirmed. Applicability repair stays in review bundles; no record edits or future CI/merge certification.

### Generic identifier with bacterial-only definition

identity: concern. Targets: GO:0009295.

GO0009295 definition and direct children include organellar nucleoids; current definition requires bacterial chromosome. GO0043590 is exact narrower bacterial class. Maintained mitochondrial/plastid records parent generic GO0009295; chloroplast parents plastid. Preserve generic identity and scope bacterial example, or undertake a separately authorized identity decision; no silent rename.

### Heterogeneous bacterial chromosome and NAP components

grounding: supported. Targets: GO:0009295.

Chromosomal DNA defines the bacterial example. HU/IHF/Fis/H-NS/Dps roles are supported at primary or secondary scopes; IPR000119 covers HU/IHF, not all NAPs. Heterogeneous pool does not assert all proteins perform every graph action or every member is necessary.

### Seven accession and source-annotation identities

grounding: supported. Targets: GO:0009295.

Seven exact reviewed K-12 accessions/gene/locus pairs and one-hit queries agree. Four PMID21903814 nucleoid annotations and H-NS333393 join verified. HU-beta/IHF-beta/Dps examples correctly remain identity-only where not attaching direct experimental location; modern H-NS mapping of1977 source is annotation-level.

### Bacterial example distinct from complete generic class

scope: supported. Targets: GO:0009295.

Bacteria/E.coli/K-12 identities agree. UNIVERSAL is qualitative bacterial chromosome-region scope, not every physiological state or universal NAP complement. Wang uses cultured E.coli early-log endogenous fusions, glucose/glycerol minimal media; reference accession taxon does not establish every experimental substrain.

### Scoped multiscale bacterial mechanism

graph: supported. Targets: GO:0009295.

NAP binding/geometry, supercoil constraints and compaction are supported as coarse review-level synthesis. Verma explicitly limits in-vivo barriers and concentration/magnesium-dependent NAP behavior; Wang supports observed H-NS organization separately from proposed loops. Pool does not claim each member executes all actions.

### Defining material versus individual formation requirements

evidence: unknown. Targets: GO:0009295.

DNA is defining material of the bacterial example; CONDITIONAL NAP cohort does not establish every listed protein necessary for assembly. Gene-specific phenotype/function and organization evidence do not constitute universal formation requirements.

### Covered bacterial NAP expression contexts

scope: concern. Targets: GO:0009295.

Original formal no-expression exclusion ignores genes and regulator/pathway claims. Fresh e_coli/precise1k includes five strains and MG1655 reference-locus mapping; all seven genes found. dps has OxyR3/RpoS51 true flags, fis ppGpp145; other five no true flags among201modules. This is bounded transcriptional context, no biological absence or formation proof, AI prose excluded.

### Exact complex and bounded yeast example

identity: supported. Targets: GO:0000148.

Native GO exact identity agrees. Fks1/Fks2 alternative catalytic subunits and Rho1 regulator define the selected yeast model, not a simultaneous obligatory Fks1/Fks2 heteromer.

### Species example versus experimental/reference strains

scope: supported. Targets: GO:0000148.

S.cerevisiae4932 and S288C559292 verified. COMMON remains qualitative native prevalence wording, not independently measured strain census. Primary abstract-level experiments support yeast model without resolving every experimental strain.

### Activity requirement is not assembly necessity

grounding: unknown. Targets: GO:0000148.

Both components retain UNKNOWN essentiality. Rho1 catalytic dependence, mutant activity and copurification support biochemical roles, not a demonstrated failure of complex formation.

### Positive molecular narrative assessed against actual host catalogue

scope: concern. Targets: GO:0000148.

Original prose-only exclusion invokes absent expression assertions despite named genes/complex functions. Fresh complete catalogue has no Saccharomyces match; current primary/authority fallback applies, no bacterial module proxy or biological absence claim.

### Exact complex and bounded yeast example

identity: supported. Targets: GO:0016590.

Native GO exact identity agrees. GO explicitly includes Isw2; chosen purified Isw2/Itc1 ACF-like example is distinguished from four-subunit CHRAC-like Isw2.

### Species example versus experimental/reference strains

scope: supported. Targets: GO:0016590.

S.cerevisiae4932 and S288C559292 verified. COMMON remains qualitative native prevalence wording, not independently measured strain census. Gelbart Methods specify W1588-4C congenic to W303, not S288C; current example is species-level purified complex and does not force strain equivalence. Native two-subunit in-vivo prevalence remains uncertain.

### Activity requirement is not assembly necessity

grounding: unknown. Targets: GO:0016590.

Both components retain UNKNOWN essentiality. Cooperative Isw2/Itc1 biochemical activity and possible two-subunit populations do not establish formation necessity; purification caveat retained.

### Positive molecular narrative assessed against actual host catalogue

scope: concern. Targets: GO:0016590.

Original formal exclusion invokes absent expression assertions despite named genes/complex functions. Fresh complete catalogue has no Saccharomyces match; current primary/authority fallback applies, no bacterial module proxy or biological absence claim.

### Exact selected subunit classes and conservative grounding

grounding: supported. Targets: GO:0000148.

Douglas/Mazur/Qadota complete primary abstracts and current annotations support alternative Fks1/Fks2 and Rho1 association/regulation. GT48 domain and broad Rho family are not exact selected pair/regulator identity; label-only TODO remains justified without exhaustive-family absence claim.

### Verified yeast protein aliases and annotation joins

grounding: supported. Targets: GO:0000148.

P38631 FKS1, P40989 GSC2 aliasFKS2 and P06780 RHO1 are reviewed S288C. P38631 current Mitochondrion location explicitly carries11856368/12185837/14576278; the record accurately says UniProt annotates these joins. Utsugi surface movement, Dijkgraaf wall phenotype and Sickmann proteome abstracts differ in scope; mitochondrial localization is not independently certified or used as synthase mechanism location. No new attribution finding established.

### Bounded synthase regulatory function

graph: supported. Targets: GO:0000148.

UDP-glucose polymerization, Rho1 stimulation and glucan contribution to fungal wall are supported at complete primary abstract and GO tiers. NONMECHANISTIC correctly withholds assembly order and upstream cell-integrity/GEF membership. Abstract scope does not certify complete protocols, direct binding affinity or exact stoichiometry.

### ACF-like two-subunit biochemistry with CHRAC caveat

grounding: supported. Targets: GO:0016590.

Gelbart identifies Itc1/WAC and reconstitutes cooperative activity; McConnell detects Dpb4/Dls1 and two-/four-subunit populations but explicitly cannot exclude procedural destabilization. Record recognizes both; no exclusive native two-subunit claim or additional mandatory component inferred. WAC and Isw1/2 N-terminal candidates are domains, not exact full-length ACF constituents.

### Reviewed Isw2/Itc1 and nuclear annotation provenance

grounding: supported. Targets: GO:0016590.

Q08773 ISW2/YOR304W and P53125 ITC1/YGL133W are reviewed S288C; one-hit gene queries and nuclear annotations agree. Huh2003 PMID14562095 is abstract plus native annotation only; Gelbart11238944 source agrees. Nuclear location does not establish complex membership by itself.

### Supported nonmechanistic remodeling summary

graph: supported. Targets: GO:0016590.

Subunit association with ACF-like complex and ATP-dependent chromatin remodeling match the primary experiments. NONMECHANISTIC correctly avoids substrate-recognition/sliding order, universal native stoichiometry or exact assembly necessity.

### Original validity and current provenance

schema: supported. Targets: GO:0031472.

Original validate/render and frozen-input comparisons passed; current source bytes match native inspect. Validation is not scientific certification. Root owns current full QC/focused/CI gates.

### Complete target, source tiers and preserved history

scope: supported. Targets: GO:0031472.

Complete current record and immutable original were read; no maintained image or verbatim snippet. Exact source tiers and experimental host/condition limits are retained. Other cohort records are outside this scientific disposition; no group/category issue is resolved by inference.

### Original validity and current provenance

schema: supported. Targets: GO:0009334.

Original validate/render and frozen-input comparisons passed; current source bytes match native inspect. Validation is not scientific certification. Root owns current full QC/focused/CI gates.

### Complete target, source tiers and preserved history

scope: supported. Targets: GO:0009334.

Complete current record and immutable original were read; no maintained image or verbatim snippet. Exact source tiers and experimental host/condition limits are retained. Other cohort records are outside this scientific disposition; no group/category issue is resolved by inference.

### Original validity and current provenance

schema: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Original validate/render and frozen-input comparisons passed; current source bytes match native inspect. Validation is not scientific certification. Root owns current full QC/focused/CI gates.

### Complete target, source tiers and preserved history

scope: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Complete current record and immutable original were read; no maintained image or verbatim snippet. Exact source tiers and experimental host/condition limits are retained. Other cohort records are outside this scientific disposition; no group/category issue is resolved by inference.

### Exact Pdu organelle and taxon

identity: supported. Targets: GO:0031472.

GO0031472 and broader GO0031469 fit a protein-coated metabolic organelle. Native LT2 occurrence and variable Bacteria scope are distinct from broad genomic potential and recombinant expression. GO0050215 is an activity, correctly not substituted as the PduCDE-complex identity.

### PduU subclass and current PduM family

grounding: concern. Targets: GO:0031472.

Current PduU remains grouped as tandem BMC-T although native protein, IPR044870 architecture and Yang2020 table distinguish a circularly permuted single-domain hexamer. New tiles-edge description names PduB/PduT, but the shared actor retains erroneous PduU membership. IPR030992 exactly resolves current PduM label-only grounding. F1/F3 persist.

### Eleven native LT2 examples and bounded query checks

grounding: supported. Targets: GO:0031472.

All11 examples remain reviewed, exact native primary symbols/loci/taxon and current query-selected identities agree. Native localization-source joins are annotation provenance; Held2016 recombinant Eut abstract is not independently direct proof of each native Pdu localization. Membership has separate Pdu primary support.

### Formation is distinct from catalysis and cohort membership

grounding: unknown. Targets: GO:0031472.

Recovered MCPs from delta-pduCDE support catalytic complex dispensability for shell assembly. PduM/PduN UNKNOWN avoids automatic formation-necessity inference. Shell-cohort CONDITIONAL is not a complete condition-by-member matrix; old/new pduA experiments differ in phenotype and conditions. No universal claim for every cohort member is inferred.

### Sequestered B12 chemistry and toxicity protection

evidence: supported. Targets: GO:0031472.

LT2 source experiments and exact GO activity/process support 1,2-PD chemistry, enzyme compartmentalization and reduced propionaldehyde-associated damage. Fresh Sampson body now supplies bounded growth/HPLC/mutagenesis detail beyond the historical abstract-only scope; no universal volatility claim is made.

### Cargo-targeting receptor specificity

graph: concern. Targets: GO:0031472.

Fan2010/2011 establish PduP/PduD targeting sequences, not the general enzyme-core-to-BMC-T binding edge. Fresh Fan2012 body directly tests PduP binding to PduA/J, with separate recombinant pull-down and native encapsulation contexts. PduD/core cannot be reassigned to those partners by analogy; F2 persists.

### Changed PduCDE type and two convergence edges

graph: supported. Targets: GO:0031472.

PduCDE STRUCTURE is appropriate for the named multisubunit complex; the prior allowed GENE_OR_PROTEIN representation is not condemned merely by enum. New tiles/assembles-into edges fit the coarse source-based convergence model, subject to F1 actor classification. PduB1–37 linkage is experimentally supported; EP-driven condensation/PduM contact geometry are proposed explanatory models, not new direct contact/kinetic measurements. No fabricated new issue is inferred from that distinction.

### Pentamer/vertex evidence scope

evidence: supported. Targets: GO:0031472.

Wheatley2013 abstract reports GrpN crystal and EutN solution pentamers, supplying homologous-family support rather than a measured PduN structure. Current native PduN and Pdu experiments provide separate context; no paper-specific PduN atomic measurement is claimed.

### Exact complex versus broader oxidoreductase and downstream dehydrogenase

identity: supported. Targets: GO:0009334.

GO0009334 exact four-protein complex, GO1990204 parent and GO0008695 activity agree. Historical HcaA1/A2 correspond to HcaE/F; downstream HcaB dehydrogenase is distinct from a legacy hcaF alias. Current K-12 identities and four exact families agree.

### Whole-cell activity and experimental strains

evidence: supported. Targets: GO:0009334.

Díaz1998 uses K-12 MC1061/ED1061 with MG1655/DH5alpha context and recombinant Salmonella controls. Whole-cell PP-to-DHPP assay includes downstream HcaB; it is not purified Hca-only product kinetics. The record canonical K-12 context and known enzyme roles are compatible with this bounded source.

### Coarse classIIB electron-transfer architecture

graph: supported. Targets: GO:0009334.

HcaD-to-HcaC-to-HcaE electron transfer, HcaF/alpha oxygenase association and catalysis form a mechanistic biochemical model. Native family assignments/sequence comparisons support this architecture; the primary paper did not individually measure every electron-transfer step. The record does not claim isolated reconstitution or measured transfer kinetics.

### UNKNOWN component essentiality

grounding: supported. Targets: GO:0009334.

All four UNKNOWN values avoid equating pathway loss with inability of the physical complex to form. No optional example or additional enzyme is demanded.

### Exact CPX pump and source-specific composition

identity: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Minted record identity denotes exact CPX4263, not broader GO1990281 as identity. All interactor IDs,6AcrA:3AcrB:3TolC counts and PDB entity mappings agree. K-12 source composition remains separate from the engineered C43(DE3) expression experiment and generic PDB source taxon562.

### AcrA exact family versus unresolved AcrB

grounding: concern. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Current IPR058628 is the exact AcrA family and P0AE06 native link. This resolves a current label-only task without rewriting old verification history. TolC IPR058622 is correct; no broader RND family is forced onto AcrB. F4 preserves original Acr F1 lineage.

### Native accession identity is not an ambiguous alias query

grounding: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

All3 exact reviewed K-12 entries, primary names/loci and CPX joins agree. Current gene_exact:acrB also returns gyrB through an old alias; the record identifies exact P31224/ACRB_ECOLI rather than asserting that the symbol query has one hit. No new query-uniqueness finding is warranted.

### Bounded tripartite pump export and stale membership links

graph: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Existing NONMECHANISTIC function graph and the3new contributes-to edges are supported as coarse physical membership/coupling and xenobiotic export. Apo5V5S is disulfide-stabilized AcrAB-TolC; separate ligand-state AcrABZ preparations do not require adding AcrZ to this target. No assembly order or kinetics is inferred.

### Formation necessity and narrow source provenance

grounding: unknown. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Intact tripartite composition is established, but the three ESSENTIAL flags are not independently tested formation-depletion claims in the inspected CPX/PDB/Wang evidence. Missing depletion evidence alone is not refutation. The added notes specifically attributing essentiality to CPX require separate narrow provenance scrutiny.

### Whole-record structured-source applicability and matched context

scope: supported. Targets: GO:0031472.

Named proteins, loci and metabolic/transport pathways trigger inspection. Salmonella core includes LT2 among6strains; ten of11checked native loci are module33 members. STM2045/PduJ is absent from its gene table and its endpoint all-zero output is not meaningful negative evidence. Fresh official metadata/gene/module fallback completed; the historical00:49Z unavailable runner was not rerun or called successful.

### Original review applicability defect

provenance: concern. Targets: GO:0031472.

Original notes exclude iModulonDB for complex identity, protein family, assembly and enzyme/transport claims without a formal adapter check. This does not implement the actual gene/protein/pathway trigger. Successor supplies bounded applicability and selected matched-source evidence; original remains immutable.

### Whole-record structured-source applicability and matched context

scope: supported. Targets: GO:0009334.

Named proteins, loci and metabolic/transport pathways trigger inspection. E. coli precise1k includes5strains; all four Hca loci are present but below all201 module thresholds. This is not biological absence or an incorrect Hca record. Fresh official metadata/gene/module fallback completed; the historical00:49Z unavailable runner was not rerun or called successful.

### Original review applicability defect

provenance: concern. Targets: GO:0009334.

Original Hca check imodulondb explicitly says no expression-module claim is maintained. This does not implement the actual gene/protein/pathway trigger. Successor supplies bounded applicability and selected matched-source evidence; original remains immutable.

### Whole-record structured-source applicability and matched context

scope: supported. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Named proteins, loci and metabolic/transport pathways trigger inspection. E. coli precise1k includes5strains; b0462/b0463/b3035 belong to SoxS module22. This does not demonstrate physical pump assembly or necessity. Fresh official metadata/gene/module fallback completed; the historical00:49Z unavailable runner was not rerun or called successful.

### Original review applicability defect

provenance: concern. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

Original notes exclude iModulonDB for complex identity, protein family, assembly and enzyme/transport claims without a formal adapter check. This does not implement the actual gene/protein/pathway trigger. Successor supplies bounded applicability and selected matched-source evidence; original remains immutable.

### Added CPX notes overstate the source annotation

provenance: concern. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

New F5 is limited to source attribution: native CPX lists stoichiometric participants and physical interaction, not an explicit essentiality annotation. The three formal membership edges remain supported; inherited component formation-necessity uncertainty is not promoted to a biological contradiction.

### Current scoped verdict

other: concern. Targets: GO:0031472.

needs_curation: 3 current findings; sources and positive assessments remain bounded.

### Current scoped verdict

other: supported. Targets: GO:0009334.

pass_with_limitations: exact Hca identity, four components and source-based classIIB model supported; no demonstrated current record defect. Native adapter review defect is repaired by the successor observation.

### Current scoped verdict

other: concern. Targets: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

needs_curation: 2 current findings; sources and positive assessments remain bounded.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0031472, GO:0042644, GO:0020023, GO:0042645, GO:0009295, GO:0042646, GO:0000148, GO:0009334, GO:0016590, cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex.

2 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t4-F1: Align the bacterial-only definition with the generic nucleoid identity

major / open / confirmed; issue key: nucleoid-generic-identifier-bacterial-definition-scope.

The maintained identifier GO0009295 denotes bacterial, mitochondrial, plastid and viral nucleic-acid regions, and the frozen organellar records use it as their parent. The target definition instead requires a bacterial chromosome. Native GO0043590 is the exact narrower bacterial-nucleoid class. This is more than incomplete taxonomic examples: it changes the defining scope of the generic record. The bacterial NAP evidence, verified E. coli proteins and example-specific mechanism remain valid.

### micro-F1: Separate PduU from the tandem-domain BMC-T cohort

major / open / confirmed; issue key: pdu-pduu-shell-class.

The component explicitly declares PduB, PduT and PduU to be BMC-T proteins and treats circular permutation as sufficient for that class. The cited quantitative study distinguishes trimeric PduT from hexameric PduU; native PduU and domain metadata identify the single-domain BMC-H architecture. Correct organelle membership does not repair the wrong molecular subclass.

### micro-F2: Do not infer a general BMC-T receptor from cargo-targeting experiments

major / open / confirmed; issue key: pdu-targeting-bmc-t-partner.

The MECHANISTIC edge directly binds the lumen enzyme core to the BMC-T cohort. Fan2010/2011 establish terminal-sequence targeting, not that specific receptor class. The freshly inspected Fan2012 body reports PduP binding to PduA/PduJ, and the Yang2022 PduM/PduB model is a different, explicitly qualified coupling mechanism. The existing edge conflates these cargo and interaction contexts.

### micro-F3: Ground PduM to its verified protein family

minor / open / confirmed; issue key: pdu-pdum-family-grounding.

The label-only PduM component now has an exact source-neutral family, IPR030992, whose native description and citation match the curated structural protein. This is a current resolvable gap, not a claim that a historical search was dishonest.

### micro-F4: Resolve the available exact AcrA family grounding

minor / open / confirmed; issue key: acrab-acra-family-grounding.

The component and open discussion retain AcrA as reviewed-label-only pending an exact family. IPR058628 now supplies the named AcrA family matching P0AE06 and the curated adaptor role. This finding concerns the current resolvable task, not the accuracy of its historical verification statement.

### micro-F5: Keep CPX participant provenance distinct from an essentiality annotation

minor / open / confirmed; issue key: acrab-cpx-essentiality-attribution.

The three newly added contributes-to edges correctly connect AcrA,AcrB and TolC to the intact pump, but their CPX evidence notes say the source curates each as an essential stoichiometric subunit. The current native source supplies exact multiplicities and physical-interaction membership, with each participant role unspecified; it does not explicitly annotate formation essentiality. Narrow the source claim without asserting that any subunit is biologically dispensable or demanding an optional depletion experiment.

## Recommended Actions And Acceptance Checks

### plaque-t4-A1

In separately authorized curation, align the generic GO0009295 definition with its actual scope and clearly qualify bacterial DNA/NAP/examples and graph as bacterial exemplars. Preserve the correct generic identifier and valid organellar child relations. If the intended record is instead specifically bacterial nucleoid, make that a deliberate separate identity/hierarchy decision using verified GO0043590, with all affected references reviewed; do not silently relabel the generic parent.

- The defining text and identifier denote the same class and do not exclude the maintained mitochondrial/plastid subclasses of generic nucleoid.
- The original bacterial evidence and seven verified protein examples remain explicitly scoped; no unsupported universal protein inventory is introduced.
- Any separately authorized identity change checks all ignored-inclusive inbound references and follows native guarded-writer/history rules.
- Focused schema/strict, native protein/graph and identifier-label gates pass after authorized curation.
- Preserve valid bacterial NAP examples and scoped graph, append-only history/rationale and independent organellar records; no automatic broader issue resolution.

### micro-A1

In authorized curation, move or separately represent PduU in its supported single-domain circularly permuted BMC-H class. Retain PduB/PduT in the properly scoped BMC-T cohort and update dependent node membership without losing supported PduU occurrence.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated discussion rationale and posed_date; append historical context and update current prompt/notes only where needed. No record edits are made in this review PR.

### micro-A2

Replace the edge with the directly supported targeting relation or a specifically identified, source-qualified cargo/receptor interaction. If representing PduP–PduA/PduJ, preserve that distinct cargo identity and cite its actual interaction study; do not reassign PduD/CDE binding merely by analogy.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated discussion rationale and posed_date; append historical context and update current prompt/notes only where needed. No record edits are made in this review PR.

### micro-A3

Use the verified PduM family grounding and reconcile the label-only note, preserving organism-specific examples and the model-qualified assembly role.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated discussion rationale and posed_date; append historical context and update current prompt/notes only where needed. No record edits are made in this review PR.

### micro-A4

Ground AcrA to its verified family and narrow the remaining open grounding task to AcrB. Preserve exact protein references, source stoichiometry and the distinction between a protein family and the complete pump.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated discussion rationale and posed_date; append historical context and update current prompt/notes only where needed. No record edits are made in this review PR.

### micro-A5

In authorized curation, narrow all3CPX notes to the actually curated stoichiometric participants/physical interaction evidence, or attach an explicit source supporting any retained formation-necessity claim. Keep the valid contributes-to edges, exact6:3:3counts and protein identities.

- Do not infer biological dispensability from unspecified source role or missing depletion experiments.
- Preserve dated history/rationale; append current correction provenance through native guarded curation.
- Native schema/graph/identifier checks pass; no records edited in this review-only PR.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6be0e75f5fb1ffa1081869af24522c1c2864d31090832eacb2f920b3dec3d443; current SHA256 2b55cd8964b49c798747f87a1027fd9817864853f125fcdc10569ed285f784cc. Changed record reassessed against current sources. |
| original-review-0 | reviews/structured/20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/nucleoid/chloroplast_nucleoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25; current SHA256 ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T042548Z-chloroplast-nucleoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/nucleoid/kinetoplast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a; current SHA256 e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T042549Z-kinetoplast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/nucleoid/mitochondrial_nucleoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d; current SHA256 c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T042550Z-mitochondrial-nucleoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/nucleoid/nucleoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08; current SHA256 e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T042551Z-nucleoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/nucleoid/plastid_nucleoid.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842; current SHA256 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T042551Z-plastid-nucleoid-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc; current SHA256 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e; current SHA256 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/acf_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d; current SHA256 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T042554Z-acf-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 f6cb94dea736f627892fc1cdc8a1f44668752e605644876e937a6f11ecc0f62d; current SHA256 781dd7e152917915b204ac297248d0caa8f290a2f815b9bf9ed41f43b8819c25. Changed record reassessed against current sources. |
| original-review-9 | reviews/structured/20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Complete source/scope/frozen-input review and structured-source cross-check contract | supports | Positive named molecular/pathway assertions anywhere in a record trigger applicability assessment. Lack of computational expression-module claims is not an exemption. |
| septin-curation-policy | docs/CURATION.md; Taxon-agnostic family or class components; formation necessity; dated rationale | supports | Generic protein classes and collective constitutional material are allowed; absent optional examples or exact family groundings are not automatic defects. Dated rationale and history remain append-only. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Structure identity, examples, taxonomic presence and graph/essentiality enums | supports | Identity, reference-strain protein example, source experiment, localization, organization and formation necessity are distinct. COMMON is qualitative presence with losses as exceptions, not a measured census. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Coarse FUNCTION or ASSEMBLY/NONMECHANISTIC scope | supports | A coarse packaging/organization graph need not supply replication enzymology or a full assembly pathway. Edge-level experiments retain actual taxon and assay context. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Actual identity versus represented-symbol coverage | supports | COVERED and HAS_SYMBOLS_NO_EXAMPLES describe native inventory coverage; neither establishes universal localization/formation necessity. Generic classes do not require invented accession representatives. |
| septin-review-contract | docs/record-reviews.md; Immutable source inputs, verdicts and exact prior finding identities | supports | Original reviews are preserved. No scientific finding or prior occurrence is invented for an original clean review. Native validation does not certify biology. |
| septin-nucleoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009295,GO:0042644,GO:0042645,GO:0042646,GO:0009570,GO:0009532,GO:0005759,GO:0051276; Fresh response independently read for this successor. Complete eight-term native names, definitions, active states and typed child relations | supports | GO0009295 denotes a nucleic-acid region in a virus, bacterial cell, mitochondrion or chloroplast. GO0042644/0042645/0042646 exactly identify the three organellar nucleoid classes. The returned stroma/matrix terms show their corresponding nucleoid part_of children; GO0051276 is chromosome organization. Each exact term was read; no omitted edge is treated as biological disproof. |
| septin-nucleoid-agent-go-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042644,GO:0042645,GO:0042646/ancestors?relations=is_a; Fresh response independently read for this successor. Complete is_a-only ancestor arrays for GO0042644, GO0042645 and GO0042646 | supports | The is_a-only response places chloroplast nucleoid under plastid nucleoid and places both plastid and mitochondrial nucleoids under generic nucleoid. The direct typed child relations are independently visible in the term response. This request does not establish parthood. |
| septin-nucleoid-agent-karcher2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093/mp/ssp083%22; Fresh response independently read for this successor. Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Karcher D, Köster D, Schadach A, Klevesath A and Bock R2009, DOI10.1093/mp/ssp083, PMID19995727. The complete primary abstract reports C. reinhardtii HLP chloroplast targeting/nucleoid association, RNAi-altered nucleoid structure, apparently reduced compaction and reduced plastome copy number. This is abstract-level evidence, not a full Methods or strain audit. |
| septin-nucleoid-agent-kobayashi2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093/gbe/evv233%22; Fresh response independently read for this successor. Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Kobayashi et al.2015, DOI10.1093/gbe/evv233, PMC4758235, is primary research on evolutionary differences in chloroplast nucleoid proteins, not a review article. The abstract identifies comparative proteomic, cell-biological and biochemical work in green plants. |
| septin-nucleoid-agent-kobayashi2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4758235.1/PMC4758235.1.xml; Genuine fresh JATS: complete Introduction; Methods Plant Culture Conditions, Nuclear Transformation of C. reinhardtii and Isolation of cp Nucleoids; complete first Results subsection with Table1/Fig1–2 captions; Discussion HLP as a Prokaryotic Component and Evolutionary Scenario of Cp Nucleoid Proteins. No figure pixels, other Results/Methods or supplements. | supports | Primary comparative research, not a review article. Direct CreHLP localization and purified-nucleoid recovery support Chlamydomonas membership; CreCNS candidates are separated from verified localizations. Purified-protein binding and heterologous E.coli compaction do not establish universal plastid formation necessity. Protein complements vary across green-plant lineages; evolutionary replacement is an interpreted model, not an exhaustive census. |
| septin-nucleoid-agent-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage and names | supports | ENA 3055 identifies Chlamydomonas reinhardtii, rank species. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| septin-nucleoid-agent-family-IPR000119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000119/; Fresh response independently read for this successor. Native accession/type/name, complete description, child families and integrated signatures | supports | IPR000119 is the Histone-like DNA-binding protein family. It includes bacterial HU, IHF and other members and notes algal chloroplast-encoded representatives. It is a relevant broader family candidate, not an exact identification of the localized chloroplast-nucleoid HU-like cohort; no new family grounding is forced. |
| septin-nucleoid-agent-gene-HLP | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AHLP%29%20AND%20%28organism_id%3A3055%29; Fresh response independently read for this successor. Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The exact HLP gene query in taxon3055 returns zero entries across the queried statuses. This bounded index result does not negate the directly supported literature HLP name or establish that no protein accession exists under another locus/alias. |
| septin-root43-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204; Fresh response; exact GO0020023/0005739 identity, active status, definitions and relevant part_of child only. Six unrelated terms are not assigned verdicts. | supports | GO0020023 denotes the kinetoplast region in the single mitochondrion of kinetoplastid parasites. GO0005739 lists the kinetoplast part_of child; this verifies anatomy, not a complete kinetoplast replication mechanism. |
| septin-root43-sources-tax5653 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653; Fresh response independently read for this successor. Complete native taxonomy response | supports | ENA verifies Kinetoplastea identity, rank and lineage. |
| septin-root43-sources-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Fresh response independently read for this successor. Complete native taxonomy response | supports | ENA verifies Trypanosoma brucei identity, rank and lineage. |
| septin-root43-sources-SL0150 | https://rest.uniprot.org/locations/SL-0150.json; Fresh response independently read for this successor. Complete native response, including matrix/mitochondrion parthood | supports | Native SL0150 maps to GO0020023 and describes mitochondrial maxicircle/minicircle network organization. |
| septin-root43-sources-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.E02-08-0525&amp;format=json&amp;resultType=core; Fresh response independently read for this successor. Complete native MED bibliographic identity and complete returned abstract | supports | Ogbadoyi2003 MED12802053 DOI10.1091/mbc.E02-08-0525 identifies a TAC linkage across mitochondrial membranes to basal bodies; this is contextual machinery, not the DNA region itself. |
| septin-root43-sources-doi-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Ffemsre%2Ffuac047&amp;format=json&amp;resultType=core; Fresh response independently read for this successor. Complete native MED bibliographic identity and complete returned abstract | supports | Amodeo2023 MED36449697 DOI10.1093/femsre/fuac047 is a secondary review centered on T.brucei and explicitly proposes an updated replication model. |
| septin-root43-sources-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Fnar%2Fgkz928&amp;format=json&amp;resultType=core; Fresh response independently read for this successor. Complete native MED bibliographic identity and complete returned abstract | supports | Cooper2019 MED31665448 DOI10.1093/nar/gkz928 reports391 assembled minicircle classes and predicted/expressed guide RNAs in a defined T.brucei strain, not391 total circles per organelle. |
| septin-root43-sources-doi-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMCB.01176-10&amp;format=json&amp;resultType=core; Fresh response independently read for this successor. Complete native MED bibliographic identity and complete returned abstract | supports | Gluenz2011 MED21173163 DOI10.1128/MCB.01176-10 reports serial-section microscopy and maxicircle/minicircle probes across the duplication cycle. Native MED omitted its PMC field; genuine PMC3067821 was recovered separately. |
| septin-root43-sources-doi-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-micro-092611-150057&amp;format=json&amp;resultType=core; Fresh response independently read for this successor. Complete native MED bibliographic identity and complete returned abstract | supports | Jensen2012 MED22994497 DOI10.1146/annurev-micro-092611-150057 is a review of network structure, replication and segregation. |
| septin-root43-sources-doi-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371%2Fjournal.pone.0187516&amp;format=json&amp;resultType=core; Fresh response independently read for this successor. Complete native MED bibliographic identity and complete returned abstract | supports | deSouza2017 MED29131838 DOI10.1371/journal.pone.0187516 studies comparative KAP repertoires and distinct localization patterns in symbiont-bearing trypanosomatids. |
| septin-nucleoid-agent-SL-0269 | https://rest.uniprot.org/locations/SL-0269.json; Fresh response independently read for this successor. Complete native name/definition/synonyms/GO and part-of hierarchy | supports | SL0269 identifies Mitochondrion nucleoid, maps GO0042645, supplies mitochondrial nucleoid and mitochromosome synonyms and places the location under mitochondrial matrix SL0170/GO0005759. |
| septin-nucleoid-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage and names | supports | ENA 4932 identifies Saccharomyces cerevisiae, rank species. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| septin-nucleoid-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage and names | supports | ENA 559292 identifies Saccharomyces cerevisiae S288C, rank strain. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| septin-nucleoid-agent-kucej2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1242/jcs.028605%22; Fresh response independently read for this successor. Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Kucej M, Kucejova B, Subramanian R, Chen XJ and Butow RA2008, DOI10.1242/jcs.028605/PMC5728373. The complete abstract reports in organello ChIP-chip, genome-wide Abf2 association and metabolic remodeling. |
| septin-nucleoid-agent-kucej2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.tcb.2007.08.007%22; Fresh response independently read for this successor. Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Kucej M and Butow RA2007, DOI10.1016/j.tcb.2007.08.007, PMID17981466, is a review. The complete abstract describes mitochondrial DNA-protein particles, species-specific protein combinations and HMG packaging proteins. No full review body is claimed. |
| septin-nucleoid-agent-sia2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1534/genetics.108.095786%22; Fresh response independently read for this successor. Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Sia RA, Carrol S, Kalifa L, Hochmuth C and Sia EA2009, DOI10.1534/genetics.108.095786/PMC2621183. The abstract distinguishes increased frameshifts/direct-repeat deletions from no point-mutation-rate effect. |
| septin-nucleoid-agent-protein-Q02486 | https://rest.uniprot.org/uniprotkb/Q02486.json; Fresh response independently read for this successor. Exact accession/status/name/genes/taxon and subcellular-location comments; native family crossrefs inspected separately | supports | Q02486 is reviewed ARS-binding factor2, mitochondrial, primary gene ABF2 with HIM1/YMR072W/YM9916.11 tokens, organism559292. It verifies the reference-strain example identity; the current location comments alone do not cite the Kucej/Sia nucleoid experiments. |
| septin-nucleoid-agent-gene-ABF2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AABF2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Fresh response independently read for this successor. Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The exact reviewed ABF2 query at taxon559292 returns one entry Q02486 with matching primary ABF2 gene. This is the current bounded query, not reconstruction of the historical retrieval. |
| septin-nucleoid-agent-family-IPR009071 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009071/; Fresh response independently read for this successor. Native type/name, complete description and integrated signatures | supports | IPR009071 is a High mobility group box domain, present in diverse nuclear and other proteins as well as Abf2. It is not an exact localized mitochondrial HMG-box protein family. |
| septin-nucleoid-agent-family-IPR051965 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051965/; Fresh response independently read for this successor. Native type/name/description, LLM flags and Q02486 cross-reference context | context_only | Native metadata identifies a broad family named Chromatin Regulation and Neuronal Gene Expression, linked by Q02486. Its narrative is explicitly unchecked LLM-generated; that prose is not accepted as biological evidence or an exact localized mitochondrial HMG-class mapping. |
| septin-nucleoid-agent-SL-0140 | https://rest.uniprot.org/locations/SL-0140.json; Fresh response independently read for this successor. Complete native location name/definition/synonyms/GO and part-of hierarchy | supports | UniProt SL0140 identifies Plastid nucleoid, maps GO0042646, supplies Plastidic nucleoid as a synonym and places it under Plastid stroma SL0215/GO0009532. Its definition describes a non-membrane-bounded chromatin-dense plastid pseudocompartment. |
| septin-nucleoid-agent-tax33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage and names | supports | ENA 33090 identifies Viridiplantae, rank kingdom. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| septin-PMC10719067-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC10719067.1/PMC10719067.1.xml; Fresh genuine SECONDARY review JATS; complete sec1 with Fig1/2 captions and Table1, sec8 including both subsections, sec10. Other sections, pixels and supplements not read. | supports | Amodeo2023 explicitly centers T.brucei. It supports interlocked mini/maxicircle organization, conditional KAP contributions and TAC/basal-body segregation context. Models and unknown exact basic-protein localization/compaction are distinguished from direct experiments; no universal KAP repertoire or new measured prevalence is inferred. |
| septin-PMC6868439-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6868439.1/PMC6868439.1.xml; Fresh genuine primary JATS; complete Methods SEC2-1 with Table1, Results SEC3-1 and SEC3-2 including Fig1 caption. Other Results/Methods, pixels and supplements not read. | supports | Cooper2019 uses EATRO1125 AnTat1.1 90:13-derived cell lines and distinguishes391 sequence classes from thousands of minicircle copies. Read-depth estimates yield about30 maxicircles and about6000 minicircles for an unreplicated network; neither391 classes nor population averages are universal per-organelle stoichiometry. |
| septin-PMC5683618-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5683618.1/PMC5683618.1.xml; Fresh genuine primary JATS; complete Introduction sec001, cell culture sec004, Results sec013 and sec016 with Fig1/3 captions. Other sections/pixels/supplements not read. | supports | deSouza2017 surveys lineage-variable KAP repertoires and tests Angomonas/Strigomonas wild-type/aposymbiotic strains. KAP1/2 are not universal; KAP2/3 cluster together. KAP4 overlaps kDNA, whereas aKAP23 does not coincide with DAPI and may occupy the kinetoflagellar zone. The curated DNA-bound compacting cohort is not every protein ever called KAP, nor a complete T.brucei KAP1–4 inventory. |
| septin-kucej2008-xmlhtml | https://pmc.ncbi.nlm.nih.gov/articles/PMC5728373/?report=xml; Genuine recovered PMC HTML; complete Introduction S1, all Results S3–S6, Discussion S7, Methods S9–S13 and Fig1–6 captions. No pixels, supplementary tables/data or independent assay reanalysis. | supports | Kucej2008 crosslinks isolated mitochondria in organello and samples about70% of an intronless genome; its own in vivo interpretation is not intact-live-cell ChIP. Abf2 binds most mtDNA with GC-rich preference; glucose/glycerol differences alter DNA:Abf2 ratio and nuclease sensitivity, while Hsp60/Ilv5 recruitment is condition-dependent. MCC109, BY4741 and W303-1B contexts are not silently relabeled as the S288C protein-reference example. |
| septin-sia2009-xmlhtml | https://pmc.ncbi.nlm.nih.gov/articles/PMC2621183/?report=xml; Genuine recovered PMC HTML; complete short scientific main body through conclusion, Table1/footnote, Fig1/2 captions. No figure pixels or unlinked supplementary strain ancestry. | supports | Sia2009 shows increased frameshift/microsatellite instability and direct-repeat deletion after ABF2 loss, not an increased point-mutation rate. Respiratory selection permits retained mtDNA while fermentative growth favors loss. These genome-stability effects do not establish unconditional nucleoid formation necessity. |
| septin-gluenz2011-canonical | https://pmc.ncbi.nlm.nih.gov/articles/PMC3067821/; Genuine recovered canonical PMC HTML; complete Methods sec2/4 and Results sec7/8 with Fig1/2 captions. No figure pixels, other sections or supplements. | supports | Gluenz2011 uses procyclic T.brucei LISTER427/TREU927/29-13 assay strains, serial thin-section EM and3D reconstructions. Five duplication stages link kDNA morphology to basal-body/flagellar-pocket organization. The declared canonical species example is supported without extending these measurements to every kinetoplastid architecture. |
| septin-access-initial-sandbox-failure-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/initial-sandbox-failure-receipts.json; Actual retrieval receipt packet and response hashes; access context only | context_only | Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404 and four EuropePMC XML500 responses do not support or refute scientific claims. Separate successful genuine bodies above were inspected. Ogbadoyi genuine body was fetched but only its complete primary abstract was assessed; no body-read claim. |
| septin-access-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/source-receipts.json; Actual retrieval receipt packet and response hashes; access context only | context_only | Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404 and four EuropePMC XML500 responses do not support or refute scientific claims. Separate successful genuine bodies above were inspected. Ogbadoyi genuine body was fetched but only its complete primary abstract was assessed; no body-read claim. |
| septin-access-body-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/body-receipts.json; Actual retrieval receipt packet and response hashes; access context only | context_only | Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404 and four EuropePMC XML500 responses do not support or refute scientific claims. Separate successful genuine bodies above were inspected. Ogbadoyi genuine body was fetched but only its complete primary abstract was assessed; no body-read claim. |
| septin-access-more-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/more-receipts.json; Actual retrieval receipt packet and response hashes; access context only | context_only | Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404 and four EuropePMC XML500 responses do not support or refute scientific claims. Separate successful genuine bodies above were inspected. Ogbadoyi genuine body was fetched but only its complete primary abstract was assessed; no body-read claim. |
| septin-access-canonical-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/canonical-receipts.json; Actual retrieval receipt packet and response hashes; access context only | context_only | Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404 and four EuropePMC XML500 responses do not support or refute scientific claims. Separate successful genuine bodies above were inspected. Ogbadoyi genuine body was fetched but only its complete primary abstract was assessed; no body-read claim. |
| septin-catalogue | https://imodulondb.org/api/datasets; Entire fresh official organism/dataset response; all rows and arrays | supports | The current catalogue has no matching Chlamydomonas/green-plant, Saccharomyces or kinetoplastid host. All four records positively assert molecular/pathway biology, so applicability is checked; no unrelated bacterial proxy or downstream unmatched gene/module query is justified. Noncoverage is not biological absence. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual retained historical runner attempt; no new invocation | context_only | 2026-11-03T00:49:00.848907Z–00:49:00.863225Z exit1 PermissionError reading pyvenv.cfg. Current direct official catalogue fallback is separate, not a new successful adapter run. |
| septin-generic-nucleoid-context | data/structures/nucleoid/nucleoid.yaml; Complete already-frozen cohort neighbor, used only for identity boundary | supports | The generic maintained neighbor has broader GO0009295 identity with bacterial wording; that separate target is reviewed by another agent. Correct organellar child ontology links are assessed directly against GO. No neighbor finding, verdict or terminal disposition is inferred. |
| septin-record-chloroplast_nucleoid | data/structures/nucleoid/chloroplast_nucleoid.yaml; Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | All scientific fields, sources, discussions, history and graph edges read. Record remains byte-identical to the original frozen target; independent current source checks performed, not merely a hash refresh. 0 protein examples/1 typed protein nodes; no maintained images. |
| septin-original-chloroplast_nucleoid | reviews/structured/20261022T042548Z-chloroplast-nucleoid-audit/review.yaml; Complete original YAML/Markdown, science/checks/verdict/actions/limitations and frozen input manifest | supports | Original qualified pass has no scientific findings or request-curation actions. Its current-input identity is unchanged; original dated checks remain historical, not newly executed. Unsupported formal adapter exclusion is separately corrected in successor only. |
| septin-original-validation-chloroplast_nucleoid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json; Actual native validate/render and complete frozen historical-input check | supports | Both commands exit0, original Markdown byte-exact, all16 original input hashes match the frozen source; current target matches original target. Native validity is not a scientific verdict. |
| septin-native-chloroplast_nucleoid-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-verify-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported HLP token is not refuted by a bounded zero UniProt exact-name result. |
| septin-native-chloroplast_nucleoid-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-causal-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-causal.log SHA256 1ad288cda6d8baaea929dfe9142bcf9ba8b7e4f320f7678340a454924e46c0b8 | supports | Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported HLP token is not refuted by a bounded zero UniProt exact-name result. |
| septin-record-kinetoplast | data/structures/nucleoid/kinetoplast.yaml; Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | All scientific fields, sources, discussions, history and graph edges read. Record remains byte-identical to the original frozen target; independent current source checks performed, not merely a hash refresh. 0 protein examples/1 typed protein nodes; no maintained images. |
| septin-original-kinetoplast | reviews/structured/20261022T042549Z-kinetoplast-audit/review.yaml; Complete original YAML/Markdown, science/checks/verdict/actions/limitations and frozen input manifest | supports | Original qualified pass has no scientific findings or request-curation actions. Its current-input identity is unchanged; original dated checks remain historical, not newly executed. Unsupported formal adapter exclusion is separately corrected in successor only. |
| septin-original-validation-kinetoplast | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json; Actual native validate/render and complete frozen historical-input check | supports | Both commands exit0, original Markdown byte-exact, all14 original input hashes match the frozen source; current target matches original target. Native validity is not a scientific verdict. |
| septin-native-kinetoplast-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-verify-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative literature names, not a verified set of four universal T.brucei accession identities. |
| septin-native-kinetoplast-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-causal-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-causal.log SHA256 8676810ab064da164f9b59c268811a6c76f4dbc7dc0297ac3e4089301cd09f4d | supports | Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative literature names, not a verified set of four universal T.brucei accession identities. |
| septin-record-mitochondrial_nucleoid | data/structures/nucleoid/mitochondrial_nucleoid.yaml; Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | All scientific fields, sources, discussions, history and graph edges read. Record remains byte-identical to the original frozen target; independent current source checks performed, not merely a hash refresh. 1 protein examples/1 typed protein nodes; no maintained images. |
| septin-original-mitochondrial_nucleoid | reviews/structured/20261022T042550Z-mitochondrial-nucleoid-audit/review.yaml; Complete original YAML/Markdown, science/checks/verdict/actions/limitations and frozen input manifest | supports | Original qualified pass has no scientific findings or request-curation actions. Its current-input identity is unchanged; original dated checks remain historical, not newly executed. Unsupported formal adapter exclusion is separately corrected in successor only. |
| septin-original-validation-mitochondrial_nucleoid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json; Actual native validate/render and complete frozen historical-input check | supports | Both commands exit0, original Markdown byte-exact, all16 original input hashes match the frozen source; current target matches original target. Native validity is not a scientific verdict. |
| septin-native-mitochondrial_nucleoid-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-verify-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node. Identity and coverage do not turn every source assay into S288C or prove formation necessity. |
| septin-native-mitochondrial_nucleoid-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-causal-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-causal.log SHA256 f99e2411914f5015315ed9c67ad81727e914466b91175451cb0ca9ca924f37f8 | supports | One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node. Identity and coverage do not turn every source assay into S288C or prove formation necessity. |
| septin-record-plastid_nucleoid | data/structures/nucleoid/plastid_nucleoid.yaml; Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | All scientific fields, sources, discussions, history and graph edges read. Record remains byte-identical to the original frozen target; independent current source checks performed, not merely a hash refresh. 0 protein examples/0 typed protein nodes; no maintained images. |
| septin-original-plastid_nucleoid | reviews/structured/20261022T042551Z-plastid-nucleoid-audit/review.yaml; Complete original YAML/Markdown, science/checks/verdict/actions/limitations and frozen input manifest | supports | Original qualified pass has no scientific findings or request-curation actions. Its current-input identity is unchanged; original dated checks remain historical, not newly executed. Unsupported formal adapter exclusion is separately corrected in successor only. |
| septin-original-validation-plastid_nucleoid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json; Actual native validate/render and complete frozen historical-input check | supports | Both commands exit0, original Markdown byte-exact, all15 original input hashes match the frozen source; current target matches original target. Native validity is not a scientific verdict. |
| septin-native-plastid_nucleoid-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-verify-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Zero examples and zero typed protein nodes; native success is empty inventory scope. HLP-containing narrative elsewhere still triggers applicability. |
| septin-native-plastid_nucleoid-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-causal-receipt.json; Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Zero examples and zero typed protein nodes; native success is empty inventory scope. HLP-containing narrative elsewhere still triggers applicability. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks and full review skill reread; previously read remaining rules byte-identical | context_only | Genes, proteins, regulators and pathways trigger applicability; no expression-module assertion alone does not establish N/A. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Previously read unchanged native scientific checklist | context_only | Identity, source scope, component necessity and optional inventory are separate questions. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Previously read unchanged component, CausalNode and necessity contracts | context_only | Protein families and complexes may be GENE_OR_PROTEIN. Functional requirement differs from formation necessity; optional examples are not mandatory. |
| plaque-history-policy | docs/CURATION.md; Previously read unchanged append-only discussion/history rules | context_only | Preserve dated historical rationale and current scientific uncertainty; individual examples do not require broad family grounding or retroactive history rewriting. |
| plaque-current-4 | data/structures/nucleoid/nucleoid.yaml; Entire maintained record at 7b6cd533340948100b7b23d8ab4e659702d9feba including all sources, components, examples, graph, discussion and history | supports | Full unchanged target independently reassessed; no record mutation. |
| plaque-original-4 | reviews/structured/20261022T042551Z-nucleoid-audit/review.yaml; Complete exact original YAML and derived Markdown, checks, evidence, findings, actions and limitations | supports | Nucleoid has one inherited major identity finding; glucan synthase and ACF have no findings. Nucleoid/ACF formal and glucan prose-only exclusions are reassessed. Historical source bytes and native rendering checked. |
| plaque-current-6 | data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml; Entire maintained record at 7b6cd533340948100b7b23d8ab4e659702d9feba including all sources, components, examples, graph, discussion and history | supports | Full unchanged target independently reassessed; no record mutation. |
| plaque-original-6 | reviews/structured/20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit/review.yaml; Complete exact original YAML and derived Markdown, checks, evidence, findings, actions and limitations | supports | Nucleoid has one inherited major identity finding; glucan synthase and ACF have no findings. Nucleoid/ACF formal and glucan prose-only exclusions are reassessed. Historical source bytes and native rendering checked. |
| plaque-current-8 | data/structures/other/acf_complex.yaml; Entire maintained record at 7b6cd533340948100b7b23d8ab4e659702d9feba including all sources, components, examples, graph, discussion and history | supports | Full unchanged target independently reassessed; no record mutation. |
| plaque-original-8 | reviews/structured/20261022T042554Z-acf-complex-audit/review.yaml; Complete exact original YAML and derived Markdown, checks, evidence, findings, actions and limitations | supports | Nucleoid has one inherited major identity finding; glucan synthase and ACF have no findings. Nucleoid/ACF formal and glucan prose-only exclusions are reassessed. Historical source bytes and native rendering checked. |
| plaque-context-chloroplast_nucleoid | data/structures/nucleoid/chloroplast_nucleoid.yaml; Identity, definition, parent_structures and part_of only | context_only | Maintained organellar identities provide bounded local context: mitochondrial and plastid nucleoids use generic GO0009295 parent; chloroplast uses plastid nucleoid parent. |
| plaque-context-mitochondrial_nucleoid | data/structures/nucleoid/mitochondrial_nucleoid.yaml; Identity, definition, parent_structures and part_of only | context_only | Maintained organellar identities provide bounded local context: mitochondrial and plastid nucleoids use generic GO0009295 parent; chloroplast uses plastid nucleoid parent. |
| plaque-context-plastid_nucleoid | data/structures/nucleoid/plastid_nucleoid.yaml; Identity, definition, parent_structures and part_of only | context_only | Maintained organellar identities provide bounded local context: mitochondrial and plastid nucleoids use generic GO0009295 parent; chloroplast uses plastid nucleoid parent. |
| plaque-go-terms | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009295,GO:0043590,GO:0042644,GO:0042645,GO:0042646,GO:0051276,GO:0000148,GO:0003843,GO:0009277,GO:0071970,GO:0016590,GO:0031010,GO:0006338; Fresh complete thirteen native GO identities, definitions, synonyms, active status and typed child entries | supports | Generic GO0009295 explicitly spans virus, bacterial cell, mitochondrion and chloroplast; GO0043590 is bacterial nucleoid. GO0009295 directly lists mitochondrial/plastid/bacterial is_a children. Exact glucan synthase and ACF definitions and ACF ISWI-type parent agree; retained process/activity/wall identities agree. |
| plaque-sl-0187 | https://rest.uniprot.org/locations/SL-0187.json; Fresh complete native localization identity/definition | supports | SL0187 is nucleoid, supporting localization cross-reference rather than narrowing generic GO identity to the chosen bacterial example. |
| plaque-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete fresh ENA identity/rank/lineage | supports | Domain, species and reference-strain identities verified separately. K-12 examples do not mean all experiments use MG1655; S288C accessions do not make W303-derived experiments S288C. |
| plaque-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete fresh ENA identity/rank/lineage | supports | Domain, species and reference-strain identities verified separately. K-12 examples do not mean all experiments use MG1655; S288C accessions do not make W303-derived experiments S288C. |
| plaque-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete fresh ENA identity/rank/lineage | supports | Domain, species and reference-strain identities verified separately. K-12 examples do not mean all experiments use MG1655; S288C accessions do not make W303-derived experiments S288C. |
| plaque-tax-511145 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/511145; Complete fresh ENA identity/rank/lineage | supports | Domain, species and reference-strain identities verified separately. K-12 examples do not mean all experiments use MG1655; S288C accessions do not make W303-derived experiments S288C. |
| plaque-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete fresh ENA identity/rank/lineage | supports | Domain, species and reference-strain identities verified separately. K-12 examples do not mean all experiments use MG1655; S288C accessions do not make W303-derived experiments S288C. |
| plaque-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete fresh ENA identity/rank/lineage | supports | Domain, species and reference-strain identities verified separately. K-12 examples do not mean all experiments use MG1655; S288C accessions do not make W303-derived experiments S288C. |
| plaque-dillon2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrmicro2261&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; secondary review | supports | Dillon SC, Dorman CJ. (2010), Bacterial nucleoid-associated proteins, nucleoid structure and gene expression. Native MED20140026 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-verma2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371/journal.pgen.1008456&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; secondary review | supports | Verma SC, Qian Z, Adhya SL. (2019), Architecture of the Escherichia coli nucleoid. Native MED31830036 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-douglas1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.91.26.12907&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Douglas CM, Foor F, Marrinan JA, Morin N, Nielsen JB, Dahl AM, Mazur P, Baginsky W, Li W, el-Sherbeini M. (1994), The Saccharomyces cerevisiae FKS1 (ETG1) gene encodes an integral membrane protein which is a subunit of 1,3-beta-D-glucan synthase. Native MED7528927 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-mazur1995-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/MCB.15.10.5671&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Mazur P, Morin N, Baginsky W, el-Sherbeini M, Clemas JA, Nielsen JB, Foor F. (1995), Differential expression and function of two homologous subunits of yeast 1,3-beta-D-glucan synthase. Native MED7565718 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-qadota1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1126/science.272.5259.279&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Qadota H, Python CP, Inoue SB, Arisawa M, Anraku Y, Zheng Y, Watanabe T, Levin DE, Ohya Y. (1996), Identification of yeast Rho1p GTPase as a regulatory subunit of 1,3-beta-glucan synthase. Native MED8602515 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-mazur1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074/jbc.271.24.14604&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Mazur P, Baginsky W. (1996), In vitro activity of 1,3-beta-D-glucan synthase requires the GTP-binding protein Rho1. Native MED8662910 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-gelbart2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/MCB.21.6.2098-2106.2001&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Gelbart ME, Rechsteiner T, Richmond TJ, Tsukiyama T. (2001), Interactions of Isw2 chromatin remodeling complex with nucleosomal arrays: analyses using recombinant yeast histones and immobilized templates. Native MED11238944 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-mcconnell2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/MCB.24.7.2605-2613.2004&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | McConnell AD, Gelbart ME, Tsukiyama T. (2004), Histone fold protein Dls1p is required for Isw2-dependent chromatin remodeling in vivo. Native MED15024052 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-21903814 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21903814%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Wang W, Li GW, Chen C, Xie XS, Zhuang X. (2011), Chromosome organization by a nucleoid-associated protein in live bacteria. Native MED21903814 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-333393 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:333393%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Varshavsky AJ, Nedospasov SA, Bakayev VV, Bakayeva TG, Georgiev GP. (1977), Histone-like proteins in the purified Escherichia coli deoxyribonucleoprotein. Native MED333393 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-11856368 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11856368%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Utsugi T, Minemura M, Hirata A, Abe M, Watanabe D, Ohya Y. (2002), Movement of yeast 1,3-beta-glucan synthase is essential for uniform cell wall synthesis. Native MED11856368 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-12185837 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12185837%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Dijkgraaf GJ, Abe M, Ohya Y, Bussey H. (2002), Mutations in Fks1p affect the cell wall content of beta-1,3- and beta-1,6-glucan in Saccharomyces cerevisiae. Native MED12185837 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-14576278 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14576278%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Sickmann A, Reinders J, Wagner Y, Joppich C, Zahedi R, Meyer HE, Schönfisch B, Perschil I, Chacinska A, Guiard B, Rehling P, Pfanner N, Meisinger C. (2003), The proteome of Saccharomyces cerevisiae mitochondria. Native MED14576278 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-7565718 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7565718%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Mazur P, Morin N, Baginsky W, el-Sherbeini M, Clemas JA, Nielsen JB, Foor F. (1995), Differential expression and function of two homologous subunits of yeast 1,3-beta-D-glucan synthase. Native MED7565718 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14562095%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003), Global analysis of protein localization in budding yeast. Native MED14562095 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-11238944 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11238944%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Gelbart ME, Rechsteiner T, Richmond TJ, Tsukiyama T. (2001), Interactions of Isw2 chromatin remodeling complex with nucleosomal arrays: analyses using recombinant yeast histones and immobilized templates. Native MED11238944 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-15024052 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15024052%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | McConnell AD, Gelbart ME, Tsukiyama T. (2004), Histone fold protein Dls1p is required for Isw2-dependent chromatin remodeling in vivo. Native MED15024052 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-pmid-7983071 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7983071%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=1; Complete returned exact bibliographic identity and deposited abstract; primary abstract tier | supports | Mol PC, Park HM, Mullins JT, Cabib E. (1994), A GTP-binding protein regulates the activity of (1--&gt;3)-beta-glucan synthase, an enzyme directly involved in yeast cell wall morphogenesis. Native MED7983071 and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement certified. |
| plaque-verma2019-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6907758.1/PMC6907758.1.xml; Fresh genuine secondary JATS sec002 including HU/IHF/H-NS/Fis subsections/tables and text captions; sec010,014,015 | supports | Secondary multiscale E.coli synthesis supports heterogeneous NAP DNA-binding/bending/bridging and supercoiling compaction. Concentration, magnesium, growth phase and unproven in-vivo topological barriers remain explicit. No individual primary study behind every review claim independently recovered; no pixels. |
| plaque-wang2011-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3329943.1/PMC3329943.1.xml; Fresh genuine JATS complete main scientific text and in-text experimental details; no supplementary methods/TableS1 or figure pixels | supports | Live E.coli fluorescent endogenous NAP fusions, early-log minimal-medium imaging, H-NS mutation/deletion and chromosome-conformation capture support heterogeneous NAP localization and H-NS-dependent chromosome organization. Main text distinguishes observed clusters from proposed organizing loops; no universal NAP-necessity or exact reference-strain equivalence. |
| plaque-gelbart2001-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC86823/; Fresh genuine PMC body sec2,sec6,sec14,sec15 including Fig4/5 text captions; no pixels/supplements | supports | W1588-4C congenic W303-derived yeast, FLAG purification and separated/reconstituted Isw2/Itc1 support two-subunit biochemical association and efficient DNA/nucleosome binding, ATPase/remodeling. Monomer folding/purification and incomplete activity restoration remain caveats; activity necessity is not formation necessity. |
| plaque-mcconnell2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC371119/; Fresh genuine PMC body sec3 and sec9 including Fig1/2 text captions; no pixels/supplements | supports | Independent purifications and immunodepletion identify Dpb4/Dls1 in four-subunit Isw2 and populations consistent with two-subunit Isw2/Itc1. Authors explicitly cannot rule out two-subunit material generated by tags/purification; native prevalence/exclusive stoichiometry not certified. |
| plaque-verma2019-pmc-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC6907758/; Actual retained response/readability only | context_only | HTTP200 challenge/frontend HTML, not scientific body or genes dataset; successful JATS/other direct endpoints are separately cited. No biological evidence inferred. |
| plaque-wang2011-pmc-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC3329943/; Actual retained response/readability only | context_only | HTTP200 challenge/frontend HTML, not scientific body or genes dataset; successful JATS/other direct endpoints are separately cited. No biological evidence inferred. |
| plaque-douglas1994-pmc-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC45549/; Actual retained response/readability only | context_only | HTTP200 challenge/frontend HTML, not scientific body or genes dataset; successful JATS/other direct endpoints are separately cited. No biological evidence inferred. |
| plaque-mazur1995-pmc-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC230817/; Actual retained response/readability only | context_only | HTTP200 challenge/frontend HTML, not scientific body or genes dataset; successful JATS/other direct endpoints are separately cited. No biological evidence inferred. |
| plaque-adapter-genes-access | https://imodulondb.org/api/datasets/e_coli/precise1k/genes; Actual retained response/readability only | context_only | HTTP200 challenge/frontend HTML, not scientific body or genes dataset; successful JATS/other direct endpoints are separately cited. No biological evidence inferred. |
| plaque-douglas1994-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC45549.1/PMC45549.1.xml; Actual retained HTTP404 only | context_only | Guessed public JATS route unavailable; no body read from this response. Successful PMC or primary abstract evidence is separately bounded. |
| plaque-mazur1995-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC230817.1/PMC230817.1.xml; Actual retained HTTP404 only | context_only | Guessed public JATS route unavailable; no body read from this response. Successful PMC or primary abstract evidence is separately bounded. |
| plaque-gelbart2001-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC86823.1/PMC86823.1.xml; Actual retained HTTP404 only | context_only | Guessed public JATS route unavailable; no body read from this response. Successful PMC or primary abstract evidence is separately bounded. |
| plaque-mcconnell2004-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC371119.1/PMC371119.1.xml; Actual retained HTTP404 only | context_only | Guessed public JATS route unavailable; no body read from this response. Successful PMC or primary abstract evidence is separately bounded. |
| plaque-up-P0ACF0 | https://rest.uniprot.org/uniprotkb/P0ACF0.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0ACF0 is reviewed taxon83333 DNA-binding protein HU-alpha. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P0ACF4 | https://rest.uniprot.org/uniprotkb/P0ACF4.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0ACF4 is reviewed taxon83333 DNA-binding protein HU-beta. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P0A6X7 | https://rest.uniprot.org/uniprotkb/P0A6X7.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0A6X7 is reviewed taxon83333 Integration host factor subunit alpha. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P0A6Y1 | https://rest.uniprot.org/uniprotkb/P0A6Y1.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0A6Y1 is reviewed taxon83333 Integration host factor subunit beta. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P0A6R3 | https://rest.uniprot.org/uniprotkb/P0A6R3.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0A6R3 is reviewed taxon83333 DNA-binding protein Fis. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P0ACF8 | https://rest.uniprot.org/uniprotkb/P0ACF8.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0ACF8 is reviewed taxon83333 DNA-binding protein H-NS. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P0ABT2 | https://rest.uniprot.org/uniprotkb/P0ABT2.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P0ABT2 is reviewed taxon83333 DNA protection during starvation protein. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P38631 | https://rest.uniprot.org/uniprotkb/P38631.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P38631 is reviewed taxon559292 1,3-beta-glucan synthase component FKS1. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P40989 | https://rest.uniprot.org/uniprotkb/P40989.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P40989 is reviewed taxon559292 1,3-beta-glucan synthase component GSC2. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P06780 | https://rest.uniprot.org/uniprotkb/P06780.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P06780 is reviewed taxon559292 GTP-binding protein RHO1. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-Q08773 | https://rest.uniprot.org/uniprotkb/Q08773.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | Q08773 is reviewed taxon559292 ISWI chromatin-remodeling complex ATPase ISW2. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-up-P53125 | https://rest.uniprot.org/uniprotkb/P53125.json; Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis | supports | P53125 is reviewed taxon559292 Imitation switch two complex protein 1. Exact aliases and source annotations checked; annotation joins are not independently reproduced localization or assembly experiments. |
| plaque-gene-hupA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-hupB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-ihfA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AihfA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-ihfB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AihfB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-fis | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Afis%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-hns | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahns%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-dps | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-FKS1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AFKS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-FKS2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AFKS2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-RHO1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARHO1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-ISW2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-gene-ITC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AITC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned exact gene/taxon/reviewed first page | supports | Single reviewed hit matches direct accession; FKS2 returns primary gene GSC2/P40989 via alias. No exhaustive homolog inventory claimed. |
| plaque-ipr-IPR000119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000119/; Complete native identity/type/curated description and hierarchy; unrelated cross-reference literature not independently read | supports | IPR000119 Histone-like DNA-binding protein is family. HU/IHF family is not the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain are broader than the curated specific subunit boundaries. Bounded candidates do not prove no exact family exists anywhere. |
| plaque-ipr-IPR003440 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003440/; Complete native identity/type/curated description and hierarchy; unrelated cross-reference literature not independently read | supports | IPR003440 Glycosyl transferase 48 domain is domain. HU/IHF family is not the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain are broader than the curated specific subunit boundaries. Bounded candidates do not prove no exact family exists anywhere. |
| plaque-ipr-IPR003578 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003578/; Complete native identity/type/curated description and hierarchy; unrelated cross-reference literature not independently read | supports | IPR003578 Small GTPase Rho is family. HU/IHF family is not the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain are broader than the curated specific subunit boundaries. Bounded candidates do not prove no exact family exists anywhere. |
| plaque-ipr-IPR013136 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013136/; Complete native identity/type/curated description and hierarchy; unrelated cross-reference literature not independently read | supports | IPR013136 WSTF/Acf1/Cbp146 is domain. HU/IHF family is not the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain are broader than the curated specific subunit boundaries. Bounded candidates do not prove no exact family exists anywhere. |
| plaque-ipr-IPR044754 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/; Complete native identity/type/curated description and hierarchy; unrelated cross-reference literature not independently read | supports | IPR044754 Isw1/2, N-terminal is domain. HU/IHF family is not the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain are broader than the curated specific subunit boundaries. Bounded candidates do not prove no exact family exists anywhere. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Fresh complete official /api/datasets response | supports | All twenty organism rows and28 organism-dataset pairs inspected. E.coli is covered; no Saccharomyces entry. Yeast source fallback uses current primary/authority evidence, not bacterial proxies. |
| plaque-adapter-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete precise1k metadata | supports | e_coli/precise1k has201 modules,4257 genes and five named strains BW25113,DGF-298,GMOS,MG1655,W3110. Selected MG1655 reference-locus mapping does not make this a single-strain dataset. |
| plaque-adapter-imodulons | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete201-row module metadata list; selected3,51,145 considered | supports | Module labels/regulators/thresholds are computational context, not direct nucleoid assembly/necessity evidence. No generated summary or activity interpretation used. |
| plaque-adapter-search-hupA | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=hupA&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 0 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-search-hupB | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=hupB&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 0 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-search-ihfA | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=ihfA&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 0 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-search-ihfB | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=ihfB&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 0 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-search-fis | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=fis&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 3 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-search-hns | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=hns&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 0 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-search-dps | https://imodulondb.org/api/search?organism=e_coli&amp;dataset=precise1k&amp;query=dps&amp;limit=50; Complete official bounded returned gene/module hits | supports | 1 gene hits and 0 module text hits; exact locus identities used for follow-up. Regulator text hit is not membership or binding evidence. |
| plaque-adapter-gene-b4000 | https://imodulondb.org/api/genes/e_coli/precise1k/b4000; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b4000 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b4000-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b4000/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: none. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-gene-b0440 | https://imodulondb.org/api/genes/e_coli/precise1k/b0440; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b0440 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b0440-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0440/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: none. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-gene-b1712 | https://imodulondb.org/api/genes/e_coli/precise1k/b1712; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b1712 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b1712-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b1712/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: none. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-gene-b0912 | https://imodulondb.org/api/genes/e_coli/precise1k/b0912; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b0912 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b0912-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0912/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: none. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-gene-b3261 | https://imodulondb.org/api/genes/e_coli/precise1k/b3261; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b3261 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b3261-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b3261/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: 145 ppGpp. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-gene-b1237 | https://imodulondb.org/api/genes/e_coli/precise1k/b1237; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b1237 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b1237-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b1237/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: none. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-gene-b0812 | https://imodulondb.org/api/genes/e_coli/precise1k/b0812; Exact selected gene metadata, accession and String taxon-locus fields | supports | Reference locus b0812 maps to the corresponding maintained reviewed NAP accession and String511145. Mixed experimental strains remain governed by dataset metadata. |
| plaque-adapter-gene-b0812-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0812/imodulons; All201 is_in_imodulon flags; selected true rows and thresholds | supports | True membership rows: 3 OxyR, 51 RpoS. Below-threshold values do not imply biological absence, no localization or assembly inference. |
| plaque-adapter-module-3 | https://imodulondb.org/api/imodulons/e_coli/precise1k/3; Exact selected module metadata and gene memberships/threshold; AI summary and activities excluded | supports | Selected OxyR3/RpoS51 carry dps b0812; ppGpp145 carries fis b3261, matching gene-side true flags. Computational transcriptional context only; no proof of all-NAP coregulation or nucleoid formation. |
| plaque-adapter-module-51 | https://imodulondb.org/api/imodulons/e_coli/precise1k/51; Exact selected module metadata and gene memberships/threshold; AI summary and activities excluded | supports | Selected OxyR3/RpoS51 carry dps b0812; ppGpp145 carries fis b3261, matching gene-side true flags. Computational transcriptional context only; no proof of all-NAP coregulation or nucleoid formation. |
| plaque-adapter-module-145 | https://imodulondb.org/api/imodulons/e_coli/precise1k/145; Exact selected module metadata and gene memberships/threshold; AI summary and activities excluded | supports | Selected OxyR3/RpoS51 carry dps b0812; ppGpp145 carries fis b3261, matching gene-side true flags. Computational transcriptional context only; no proof of all-NAP coregulation or nucleoid formation. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical actual00:49Z runner receipt only, never fresh invocation | context_only | Prior kg-microbe-sources datasets runner exited1 with pyvenv.cfg permission error. Current review uses direct inspected official public-source fallback; no current runner success claimed. |
| plaque-original-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-plaque/original-checks.json; Actual three native validate/render commands and44 historical frozen rows checked by git show | supports | All three originals validate, Markdown is deterministic and all historical hashes match; all own current targets unchanged. |
| plaque-native-nucleoid-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/nucleoid.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-verify-receipt.json; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | seven reviewed K-12 examples, one COVERED pooled NAP node. Actual native success concerns represented identity/coverage, not scientific mechanism, necessity or universal class completeness. |
| plaque-native-nucleoid-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/nucleoid.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-causal-receipt.json; logSHA256 060c0334ea540c0999476872bdce276671f1ffa111deee448f7ebcb5fe1291a1 | supports | seven reviewed K-12 examples, one COVERED pooled NAP node. Actual native success concerns represented identity/coverage, not scientific mechanism, necessity or universal class completeness. |
| plaque-native-1_3_beta_d_glucan_synthase_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-verify-receipt.json; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | three reviewed S288C examples, two COVERED Fks/Rho1 nodes. Actual native success concerns represented identity/coverage, not scientific mechanism, necessity or universal class completeness. |
| plaque-native-1_3_beta_d_glucan_synthase_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-causal-receipt.json; logSHA256 e5e246afc40662210eb530ad32b4b670cccbcf512c0f14cb2d7c4689b7445665 | supports | three reviewed S288C examples, two COVERED Fks/Rho1 nodes. Actual native success concerns represented identity/coverage, not scientific mechanism, necessity or universal class completeness. |
| plaque-native-acf_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acf_complex.yaml --verify; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-verify-receipt.json; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | two reviewed S288C examples, two COVERED Isw2/Itc1 nodes. Actual native success concerns represented identity/coverage, not scientific mechanism, necessity or universal class completeness. |
| plaque-native-acf_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acf_complex.yaml --causal-graphs; Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-causal-receipt.json; logSHA256 e34e9c8cebb57c5f572bee3aa6dcdb3271c14c814833d2bbe620d8bddfa7862f | supports | two reviewed S288C examples, two COVERED Isw2/Itc1 nodes. Actual native success concerns represented identity/coverage, not scientific mechanism, necessity or universal class completeness. |
| micro-record-0 | data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml; Complete current YAML, all fields; source 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | Whole record read, including all components, examples, evidence placements, graph, discussion and append-only history. |
| micro-prior-0 | reviews/structured/20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit/review.yaml; Complete immutable original YAML and paired Markdown; original source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc | supports | Original scientific verdict, checks, findings/actions and access limitations inspected; historical reads/checks are not relabeled as current. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/propanediol_degradation_polyhedral_organelle-actual-stale.diff; Exact git diff of original frozen target to current source | supports | Substantive delta reassessed against current sources; history and graph changes; see evidence-linked stale assessment. |
| micro-record-1 | data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; Complete current YAML, all fields; source 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | Whole record read, including all components, examples, evidence placements, graph, discussion and append-only history. |
| micro-prior-1 | reviews/structured/20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit/review.yaml; Complete immutable original YAML and paired Markdown; original source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc | supports | Original scientific verdict, checks, findings/actions and access limitations inspected; historical reads/checks are not relabeled as current. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/3_phenylpropionate_dioxygenase_complex-actual-stale.diff; Exact git diff of original frozen target to current source | supports | Substantive delta reassessed against current sources; target unchanged. |
| micro-record-2 | data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml; Complete current YAML, all fields; source 7b6cd533340948100b7b23d8ab4e659702d9feba | supports | Whole record read, including all components, examples, evidence placements, graph, discussion and append-only history. |
| micro-prior-2 | reviews/structured/20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml; Complete immutable original YAML and paired Markdown; original source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc | supports | Original scientific verdict, checks, findings/actions and access limitations inspected; historical reads/checks are not relabeled as current. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/acrab_tolc_multidrug_efflux_transport_complex-actual-stale.diff; Exact git diff of original frozen target to current source | supports | Substantive delta reassessed against current sources; history and graph changes; see evidence-linked stale assessment. |
| micro-policy | docs/CURATION.md; Components, family grounding, source-specific complex_compositions, formation essentiality, Discussions lines305–324 | supports | Exact-family grounding is required when available; source composition does not redefine a protein family or independently establish formation necessity. Historical rationale is append-only; prompts/notes can reflect present unresolved work. |
| micro-native-review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules and Structured Source Cross-Checks; current profile/config and rubric reread | supports | Whole-record gene/protein/pathway assertions trigger source-adapter applicability. Reviewed assertions are distinguished from old provenance and bounded source access. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/original-pair-and-hash-audit.json; All three original validate/render commands; all original manifested source inputs at each original git_revision | supports | All three original YAMLs validate; Markdown rendering is byte-identical. Every original input SHA matches its historical revision; Pdu and Acr current inputs differ, Hca matches. |
| micro-up-H9L478 | https://rest.uniprot.org/uniprotkb/H9L478.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-H9L478.raw | supports | H9L478: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduJ; Bacterial microcompartment shell protein PduJ. Native InterPro links IPR020808, IPR000249, IPR050575, IPR037233, IPR044872. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-O31041 | https://rest.uniprot.org/uniprotkb/O31041.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-O31041.raw | supports | O31041: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduD; Propanediol dehydratase medium subunit. Native InterPro links IPR010254, IPR003208, IPR025541. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-O31042 | https://rest.uniprot.org/uniprotkb/O31042.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-O31042.raw | supports | O31042: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduE; Propanediol dehydratase small subunit. Native InterPro links IPR003207, IPR036091. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P02930 | https://rest.uniprot.org/uniprotkb/P02930.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P02930.raw | supports | P02930: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene tolC; Outer membrane protein TolC. Native InterPro links IPR003423, IPR010130, IPR058622, IPR051906. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P0A1C7 | https://rest.uniprot.org/uniprotkb/P0A1C7.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0A1C7.raw | supports | P0A1C7: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduA; Bacterial microcompartment shell protein PduA. Native InterPro links IPR020808, IPR000249, IPR050575, IPR037233, IPR044872. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P0A1D1 | https://rest.uniprot.org/uniprotkb/P0A1D1.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0A1D1.raw | supports | P0A1D1: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduU; Bacterial microcompartment shell protein PduU. Native InterPro links IPR044870, IPR000249, IPR037233, IPR009307. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P0ABR5 | https://rest.uniprot.org/uniprotkb/P0ABR5.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0ABR5.raw | supports | P0ABR5: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaE; 3-phenylpropionate/cinnamic acid dioxygenase subunit alpha. Native InterPro links IPR054883, IPR015881, IPR020875, IPR043266, IPR017941, IPR036922, IPR015879, IPR001663. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P0ABW0 | https://rest.uniprot.org/uniprotkb/P0ABW0.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0ABW0.raw | supports | P0ABW0: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaC; 3-phenylpropionate/cinnamic acid dioxygenase ferredoxin subunit. Native InterPro links IPR023739, IPR017941, IPR036922, IPR053387. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P0AE06 | https://rest.uniprot.org/uniprotkb/P0AE06.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0AE06.raw | supports | P0AE06: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene acrA; Multidrug efflux pump subunit AcrA. Native InterPro links IPR058628, IPR058626, IPR058625, IPR058627, IPR058624, IPR006143. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P31224 | https://rest.uniprot.org/uniprotkb/P31224.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P31224.raw | supports | P31224: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene acrB; Multidrug efflux pump subunit AcrB. Native InterPro links IPR027463, IPR001036, IPR004764. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P37449 | https://rest.uniprot.org/uniprotkb/P37449.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P37449.raw | supports | P37449: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduB; Bacterial microcompartment shell protein PduB. Native InterPro links IPR044870, IPR000249, IPR037233, IPR009193, IPR030984. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P37450 | https://rest.uniprot.org/uniprotkb/P37450.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P37450.raw | supports | P37450: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduC; Propanediol dehydratase large subunit. Native InterPro links IPR016176, IPR036999, IPR003206. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-P77650 | https://rest.uniprot.org/uniprotkb/P77650.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P77650.raw | supports | P77650: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaD; 3-phenylpropionate/cinnamic acid dioxygenase ferredoxin--NAD(+) reductase component. Native InterPro links IPR050446, IPR036188, IPR023753, IPR016156, IPR023744, IPR028202, IPR053382. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-Q47140 | https://rest.uniprot.org/uniprotkb/Q47140.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q47140.raw | supports | Q47140: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaF; 3-phenylpropionate/cinnamic acid dioxygenase subunit beta. Native InterPro links IPR054881, IPR023712, IPR032710, IPR000391. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-Q9XDM8 | https://rest.uniprot.org/uniprotkb/Q9XDM8.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDM8.raw | supports | Q9XDM8: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduT; Bacterial microcompartment shell protein PduT. Native InterPro links IPR000249, IPR050575, IPR037233, IPR044872, IPR011238. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-Q9XDN3 | https://rest.uniprot.org/uniprotkb/Q9XDN3.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDN3.raw | supports | Q9XDN3: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduN; Bacterial microcompartment shell vertex protein PduN. Native InterPro links IPR004992, IPR036677. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-Q9XDN4 | https://rest.uniprot.org/uniprotkb/Q9XDN4.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDN4.raw | supports | Q9XDN4: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduM; Bacterial microcompartment assembly protein PduM. Native InterPro links IPR030992. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-up-Q9XDN6 | https://rest.uniprot.org/uniprotkb/Q9XDN6.json; Native accession, reviewed status, organism, primary gene/aliases/loci, recommended protein name, InterPro and source-comment joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDN6.raw | supports | Q9XDN6: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduK; Bacterial microcompartment shell protein PduK. Native InterPro links IPR000249, IPR050575, IPR037233, IPR044872. Identity and native annotation are distinct from primary experimental membership evidence. |
| micro-gene-acrA | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AacrA+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-acrA.raw | supports | Current bounded query returns 1 reviewed accession(s): P0AE06. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-acrB | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AacrB+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-acrB.raw | supports | Current bounded query returns 2 reviewed accession(s): P0AES6, P31224. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-hcaC | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaC+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaC.raw | supports | Current bounded query returns 1 reviewed accession(s): P0ABW0. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-hcaD | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaD+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaD.raw | supports | Current bounded query returns 1 reviewed accession(s): P77650. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-hcaE | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaE+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaE.raw | supports | Current bounded query returns 1 reviewed accession(s): P0ABR5. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-hcaF | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaF+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaF.raw | supports | Current bounded query returns 1 reviewed accession(s): Q47140. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduA | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduA+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduA.raw | supports | Current bounded query returns 1 reviewed accession(s): P0A1C7. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduB | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduB+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduB.raw | supports | Current bounded query returns 1 reviewed accession(s): P37449. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduC | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduC+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduC.raw | supports | Current bounded query returns 1 reviewed accession(s): P37450. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduD | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduD+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduD.raw | supports | Current bounded query returns 1 reviewed accession(s): O31041. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduE | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduE+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduE.raw | supports | Current bounded query returns 1 reviewed accession(s): O31042. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduJ | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduJ+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduJ.raw | supports | Current bounded query returns 1 reviewed accession(s): H9L478. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduK | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduK+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduK.raw | supports | Current bounded query returns 1 reviewed accession(s): Q9XDN6. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduM | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduM+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduM.raw | supports | Current bounded query returns 1 reviewed accession(s): Q9XDN4. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduN | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduN+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduN.raw | supports | Current bounded query returns 1 reviewed accession(s): Q9XDN3. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduT | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduT+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduT.raw | supports | Current bounded query returns 1 reviewed accession(s): Q9XDM8. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-pduU | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduU+AND+organism_id%3A99287+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduU.raw | supports | Current bounded query returns 1 reviewed accession(s): P0A1D1. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-gene-tolC | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AtolC+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed; Complete returned current exact-symbol search result; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-tolC.raw | supports | Current bounded query returns 1 reviewed accession(s): P02930. The acrB search also returns gyrB via a historical alias; exact P31224 identity is disambiguated by primary name, locus and CPX, and the record does not assert query uniqueness. |
| micro-ipr-IPR020875 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020875/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR020875.raw | supports | IPR020875 is type family: 3-phenylpropionate/cinnamic acid dioxygenase, alpha subunit. Exact family scope agrees with the named constituent; family identity does not prove formation necessity. |
| micro-ipr-IPR023712 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023712/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR023712.raw | supports | IPR023712 is type family: 3-phenylpropionate/cinnamic acid dioxygenase, beta subunit. Exact family scope agrees with the named constituent; family identity does not prove formation necessity. |
| micro-ipr-IPR023739 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023739/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR023739.raw | supports | IPR023739 is type family: 3-phenylpropionate/cinnamic acid dioxygenase, ferredoxin subunit. Exact family scope agrees with the named constituent; family identity does not prove formation necessity. |
| micro-ipr-IPR023744 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023744/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR023744.raw | supports | IPR023744 is type family: 3-phenylpropionate/cinnamic acid dioxygenase, ferredoxin--NAD(+) reductase subunit. Exact family scope agrees with the named constituent; family identity does not prove formation necessity. |
| micro-ipr-IPR030992 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030992/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR030992.raw | supports | IPR030992 is type family: Bacterial microcompartment assembly protein PduM. Exact PduM family cites Sinha2012 and matches current Q9XDN4. |
| micro-ipr-IPR058622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR058622.raw | supports | IPR058622 is type family: Outer membrane channel protein TolC. Exact family scope agrees with the named constituent; family identity does not prove formation necessity. |
| micro-ipr-IPR058628 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058628/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR058628.raw | supports | IPR058628 is type family: Multidrug efflux pump subunit AcrA. Exact AcrA family includes E. coli AcrA and matches current P0AE06. |
| micro-ipr-IPR044870 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044870/; Native metadata name/type, complete description, hierarchy and supporting citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR044870.raw | supports | IPR044870 is type domain: Bacterial microcompartment (BMC) circularly permuted domain. Circular permutation is domain architecture, not tandem duplication; BMC-H single-domain hexamers and BMC-T tandem-domain trimers are distinguished. |
| micro-go-0008695 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0008695; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0008695.raw | supports | GO:0008695 active=True; 3-phenylpropionate dioxygenase activity. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-0009334 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0009334; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0009334.raw | supports | GO:0009334 active=True; 3-phenylpropionate dioxygenase complex. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-0031469 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0031469; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0031469.raw | supports | GO:0031469 active=True; bacterial microcompartment. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-0031472 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0031472; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0031472.raw | supports | GO:0031472 active=True; propanediol degradation polyhedral organelle. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-0042910 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0042910; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0042910.raw | supports | GO:0042910 active=True; xenobiotic transmembrane transporter activity. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-0050215 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0050215; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0050215.raw | supports | GO:0050215 active=True; propanediol dehydratase activity. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-0051144 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0051144; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0051144.raw | supports | GO:0051144 active=True; 1,2-propanediol catabolic process. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-1990204 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:1990204; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-1990204.raw | supports | GO:1990204 active=True; oxidoreductase complex. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-go-1990281 | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:1990281; Native exact OBO identifier, active status, label and complete definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-1990281.raw | supports | GO:1990281 active=True; efflux pump complex. Definition read and compared with exact identity, parent class or activity use; not an exhaustive ontology absence search. |
| micro-tax-2 | https://rest.uniprot.org/taxonomy/2.json; Native taxonomy identifier and name/lineage; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/tax-2.raw | supports | Exact native taxon identity checked; Bacteria, E. coli K-12 and Salmonella Typhimurium LT2 are not conflated with expression hosts or individual dataset strains. |
| micro-tax-83333 | https://rest.uniprot.org/taxonomy/83333.json; Native taxonomy identifier and name/lineage; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/tax-83333.raw | supports | Exact native taxon identity checked; Bacteria, E. coli K-12 and Salmonella Typhimurium LT2 are not conflated with expression hosts or individual dataset strains. |
| micro-tax-99287 | https://rest.uniprot.org/taxonomy/99287.json; Native taxonomy identifier and name/lineage; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/tax-99287.raw | supports | Exact native taxon identity checked; Bacteria, E. coli K-12 and Salmonella Typhimurium LT2 are not conflated with expression hosts or individual dataset strains. |
| micro-eco-0353 | https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0000353; Exact active ECO:0000353 label and definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/extra/eco0000353.raw | supports | Physical interaction evidence used in manual assertion; this is not a formation-necessity assay code. |
| micro-cpx | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4263; Complete CPX-4263 native response; species, systematicName, functions, properties, participants/interactorAC/stoichiometry/bioRole, cross-references and evidenceType; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/cpx4263.raw | supports | Exact K-12 AcrAB-TolC heterododecamer: P0AE06/AcrA6, P31224/AcrB3, P02930/TolC3; exact EBI participant identifiers agree. Each bioRole is unspecified role, and ECO0000353 denotes physical interaction evidence. The response supports composition/function; it does not explicitly annotate essentiality. |
| micro-pdb | https://data.rcsb.org/rest/v1/core/entry/5V5S; Entry identity, primary citation, EM resolution and entity identifiers; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S.raw | supports | 5V5S is the 6.5 Angstrom apo AcrAB-TolC assembly linked to Wang2017. Metadata is not a new raw-map/coordinate reanalysis. |
| micro-pdb-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/1; Entity identity/name, number_of_molecules, UniProt/SIFTS mappings and source/expression taxonomy; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S-entity1.raw | supports | Entity1: Outer membrane protein TolC; 3 copies; ['P02930']. Source taxon562 and construct metadata are not silently equated with native K-12 assembly. |
| micro-pdb-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/2; Entity identity/name, number_of_molecules, UniProt/SIFTS mappings and source/expression taxonomy; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S-entity2.raw | supports | Entity2: Multidrug efflux pump subunit AcrA; 6 copies; ['P0AE06']. Source taxon562 and construct metadata are not silently equated with native K-12 assembly. |
| micro-pdb-entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/3; Entity identity/name, number_of_molecules, UniProt/SIFTS mappings and source/expression taxonomy; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S-entity3.raw | supports | Entity3: Multidrug efflux pump subunit AcrB; 3 copies; ['P31224']. Source taxon562 and construct metadata are not silently equated with native K-12 assembly. |
| micro-meta-doi-0 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1002/pro.2246%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-0.raw | partial | Bacterial microcompartment shells of diverse functional types possess pentameric vertex proteins.; PMID 23456886; DOI 10.1002/pro.2246. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1038/s41467-020-15888-4%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-1.raw | partial | Decoding the stoichiometric composition and organisation of bacterial metabolosomes.; PMID 32332738; DOI 10.1038/s41467-020-15888-4. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-10 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.184.5.1253-1261.2002%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-10.raw | partial | PduA is a shell protein of polyhedral organelles involved in coenzyme B(12)-dependent degradation of 1,2-propanediol in Salmonella enterica serovar typhimurium LT2.; PMID 11844753; DOI 10.1128/jb.184.5.1253-1261.2002. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-11 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.185.17.5086-5095.2003%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-11.raw | partial | Protein content of polyhedral organelles involved in coenzyme B12-dependent degradation of 1,2-propanediol in Salmonella enterica serovar Typhimurium LT2.; PMID 12923081; DOI 10.1128/jb.185.17.5086-5095.2003. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-12 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.7554/eLife.24905%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-12.raw | partial | An allosteric transport mechanism for the AcrAB-TolC multidrug efflux pump.; PMID 28355133; DOI 10.7554/elife.24905. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1038/s41467-021-24126-4%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-2.raw | partial | A catalog of the diversity and ubiquity of bacterial microcompartments.; PMID 34155212; DOI 10.1038/s41467-021-24126-4. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1038/s41467-022-30608-w%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-3.raw | partial | Biogenesis of a bacterial metabolosome for propanediol utilization.; PMID 35614058; DOI 10.1038/s41467-022-30608-w. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1073/pnas.0913199107%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-4.raw | partial | Short N-terminal sequences package proteins into bacterial microcompartments.; PMID 20308536; DOI 10.1073/pnas.0913199107. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.01925-07%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-5.raw | partial | Microcompartments for B12-dependent 1,2-propanediol degradation provide protection from DNA and cellular damage by a reactive metabolic intermediate.; PMID 18296526; DOI 10.1128/jb.01925-07. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.05661-11%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-6.raw | partial | The N-terminal region of the medium subunit (PduD) packages adenosylcobalamin-dependent diol dehydratase (PduCDE) into the Pdu microcompartment.; PMID 21821773; DOI 10.1128/jb.05661-11. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.06529-11%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-7.raw | partial | The PduM protein is a structural component of the microcompartments involved in coenzyme B(12)-dependent 1,2-propanediol degradation by Salmonella enterica.; PMID 22343294; DOI 10.1128/jb.06529-11. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.179.21.6633-6639.1997%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-8.raw | partial | Propanediol utilization genes (pdu) of Salmonella typhimurium: three genes for the propanediol dehydratase.; PMID 9352910; DOI 10.1128/jb.179.21.6633-6639.1997. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-doi-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=DOI%3A%2210.1128/JB.180.11.2915-2923.1998%22; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-9.raw | partial | Characterization of the hca cluster encoding the dioxygenolytic pathway for initial catabolism of 3-phenylpropionic acid in Escherichia coli K-12.; PMID 9603882; DOI 10.1128/jb.180.11.2915-2923.1998. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-10498708 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A10498708%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-10498708.raw | partial | The propanediol utilization (pdu) operon of Salmonella enterica serovar Typhimurium LT2 includes genes necessary for formation of polyhedral organelles involved in coenzyme B(12)-dependent 1, 2-propanediol degradation.; PMID 10498708; DOI 10.1128/jb.181.19.5967-5975.1999. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-11844753 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A11844753%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-11844753.raw | partial | PduA is a shell protein of polyhedral organelles involved in coenzyme B(12)-dependent degradation of 1,2-propanediol in Salmonella enterica serovar typhimurium LT2.; PMID 11844753; DOI 10.1128/jb.184.5.1253-1261.2002. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-12923081 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A12923081%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-12923081.raw | partial | Protein content of polyhedral organelles involved in coenzyme B12-dependent degradation of 1,2-propanediol in Salmonella enterica serovar Typhimurium LT2.; PMID 12923081; DOI 10.1128/jb.185.17.5086-5095.2003. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-21239588 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A21239588%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-21239588.raw | partial | Genetic analysis of the protein shell of the microcompartments involved in coenzyme B12-dependent 1,2-propanediol degradation by Salmonella.; PMID 21239588; DOI 10.1128/jb.01473-10. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-22343294 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A22343294%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-22343294.raw | partial | The PduM protein is a structural component of the microcompartments involved in coenzyme B(12)-dependent 1,2-propanediol degradation by Salmonella enterica.; PMID 22343294; DOI 10.1128/jb.06529-11. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-24747050 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A24747050%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-24747050.raw | partial | Alanine scanning mutagenesis identifies an asparagine-arginine-lysine triad essential to assembly of the shell of the Pdu microcompartment.; PMID 24747050; DOI 10.1016/j.jmb.2014.04.012. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-27063436 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A27063436%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-27063436.raw | partial | Engineering formation of multiple recombinant Eut protein nanocompartments in E. coli.; PMID 27063436; DOI 10.1038/srep24359. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-28355133 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A28355133%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-28355133.raw | partial | An allosteric transport mechanism for the AcrAB-TolC multidrug efflux pump.; PMID 28355133; DOI 10.7554/elife.24905. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pmid-9603882 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=10&amp;query=EXT_ID%3A9603882%20AND%20SRC%3AMED; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-9603882.raw | partial | Characterization of the hca cluster encoding the dioxygenolytic pathway for initial catabolism of 3-phenylpropionic acid in Escherichia coli K-12.; PMID 9603882; DOI 10.1128/jb.180.11.2915-2923.1998. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-fan2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.1207516109&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/fan2012-meta.raw | partial | Interactions between the termini of lumen enzymes and shell proteins mediate enzyme encapsulation into bacterial microcompartments.; PMID 22927404; DOI 10.1073/pnas.1207516109. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-meta-pduu2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18786396%20AND%20SRC:MED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact Europe PMC native article metadata and complete abstract only; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/pduu2008-meta.raw | partial | Structure of the PduU shell protein from the Pdu microcompartment of Salmonella.; PMID 18786396; DOI 10.1016/j.str.2008.05.013. Abstract/metadata tier only; this row does not certify uninspected body, figures or supplements. |
| micro-yang2020 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7181861.1/PMC7181861.1.xml; Sec4 complete direct paragraphs and Tables1–2/captions; Sec9 strains/growth and Sec12 purification; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/PMC7181861.raw | supports | LT2 induced purified Pdu particles, QconCAT-based composition and condition-dependent deletion observations. Table1 distinguishes trimeric PduB/PduT from hexameric PduU. Absolute counts use calibration assumptions including60PduN; no independent vertex-count or raw-spectrum reanalysis. |
| micro-yang2022 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9132943.1/PMC9132943.1.xml; Sec5,6,8,9,12,16 complete direct paragraphs and embedded captions; formerly clipped Sec5 spatial-separation paragraph independently reread; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/PMC9132943.raw | supports | LT2 genetics/tagged imaging support independent shell/cargo assemblies, PduB1–37 linkage, PduM-associated proposed bridge and alternative assembly pathways. PduCDE is major cargo; EP-driven condensation and precise molecular contacts remain model-qualified. No images/movies/supplements inspected. |
| micro-havemann2002 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC134856/; Sec3/Table1 and Sec19–22 complete text/embedded captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC134856.raw | supports | LT2 induction/immunogold and pduA mutant/complementation experiments support shell localization and condition-specific assembly phenotype. E. coli expression strains remain distinct; no raw image pixels inspected. |
| micro-havemann2003 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC180998/; Sec3,15,18,21,22,24,25 complete text/tables/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC180998.raw | supports | Purified induced LT2 particles,100–150nm/3–4nm shell, protein identity analyses and co-purification support shell/cargo membership. Protein presence is not direct binding or a full causal assembly trajectory; absent proteins in this preparation are not universal absence. |
| micro-fan2010 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2867708/; Sec2–5,7, Discussion s2 and strains sec11 complete text/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC2867708.raw | supports | PduP N-terminal truncations and reporter targeting establish encapsulation sequence function in LT2 derivatives; Discussion explicitly leaves the specific shell receptor mechanism uncertain. |
| micro-fan2011 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187188/; Sec11–15 complete Results/Discussion text, Tables2 and embedded captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC3187188.raw | supports | PduD terminal sequence targets PduCDE and heterologous proteins; recovered particles from delta-pduCDE distinguish catalytic cargo from shell formation. No general BMC-T receptor was measured. |
| micro-fan2012 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3443165/; Sec2–4, Discussion s2 and purification/pull-down Methods sec11 complete text/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/fan2012-body.raw | supports | Recombinant E. coli BL21(DE3) Rosetta2 pull-downs tested PduP against nine shell proteins and identified PduA/PduJ interactions; terminal specificity and native targeting context support a specific PduP mechanism, not reassignment of PduD or the entire enzyme core by analogy. |
| micro-sinha2012 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3318458/; Sec16–21 complete sequence/distribution, deletion/complementation, biochemical localization and Discussion text/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC3318458.raw | supports | PduM is a low-abundance structural component of LT2 Pdu particles. Deletion impairs normal assembly and overexpression perturbs it; specific vertex/bridge geometry is proposed, not measured atomic structure. Native exact family now resolves the current label-only gap. |
| micro-sampson2008 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2293232/; Sec3/Table1,Sec12,Sec17/Table3 and Discussion sec18 complete text/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC2293232.raw | supports | LT2-derived MCP-minus mutants accumulate propionaldehyde with growth arrest and increased mutagenesis under stated culture conditions. Supports toxicity-protection function; volatility and mechanism are condition-dependent. |
| micro-diaz1998 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC107259/; Sec2,7,10/Table1,12 complete Methods and Results text; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC107259.raw | supports | K-12 MC1061/ED1061 and recombinant Salmonella experiments support hca-cluster pathway function; HcaA1/A2/CD subunit roles were primarily sequence-based classIIB assignments. Whole-cell DHPP production includes downstream HcaB and is not a purified individual electron-transfer assay. |
| micro-wang2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5404916.1/PMC5404916.1.xml; s2-1,s2-2,s2-3,s3,s4-1,s4-2,s4-9 complete text including embedded captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/extra/PMC5404916.raw | supports | Engineered disulfide-stabilized AcrAB-TolC apo5V5S differs from ligand-state AcrABZ fusion preparations. SixAcrA/threeAcrB/threeTolC architecture, C43(DE3) expression and coarse transport model supported; no independent formation-essentiality depletion experiment or new raw-map/pixel analysis. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue JSON; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/catalogue.raw | supports | All returned organism/dataset entries inspected. E. coli and Salmonella hosts have represented datasets; this is a positive applicability match, not a claim that module results prove organelle biology. |
| micro-e_coli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete selected dataset metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/e_coli-meta.raw | supports | e_coli/precise1k: 4257genes,201modules,1035samples; strains BW25113, DGF-298, GMOS, MG1655, W3110. This is multi-strain transcriptomic context, not an exact experimental-strain substitute. |
| micro-e_coli-genes | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;limit=10000; Complete selected gene table; exact native loci/names/accession joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter/e_coli-genes.raw | supports | 4257 returned genes inspected by exact requested names/loci. PduB STM2039 is present even when native display name differs; STM2045/PduJ is not in this returned gene table, so its gene-module all-zero response is not certified negative membership evidence. |
| micro-e_coli-module-list | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete returned selected module list, names/regulator/function/count fields; no generated narrative used; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/e_coli-imodulons.raw | supports | Selected e_coli/precise1k module list inspected to resolve exact module keys and native summaries. Only computational expression context. |
| micro-s_enterica-meta | https://imodulondb.org/api/datasets/s_enterica/core/meta; Complete selected dataset metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/s_enterica-meta.raw | supports | s_enterica/core: 3886genes,115modules,533samples; strains 14028S, D23580, LT2, SL1344, ST4/74, UK-1. This is multi-strain transcriptomic context, not an exact experimental-strain substitute. |
| micro-s_enterica-genes | https://imodulondb.org/api/genes?organism=s_enterica&amp;dataset=core&amp;limit=10000; Complete selected gene table; exact native loci/names/accession joins; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter/s_enterica-genes.raw | supports | 3886 returned genes inspected by exact requested names/loci. PduB STM2039 is present even when native display name differs; STM2045/PduJ is not in this returned gene table, so its gene-module all-zero response is not certified negative membership evidence. |
| micro-s_enterica-module-list | https://imodulondb.org/api/datasets/s_enterica/core/imodulons; Complete returned selected module list, names/regulator/function/count fields; no generated narrative used; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/s_enterica-imodulons.raw | supports | Selected s_enterica/core module list inspected to resolve exact module keys and native summaries. Only computational expression context. |
| micro-modules-e_coli-b0462 | https://imodulondb.org/api/genes/b0462/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b0462.raw | context_only | e_coli/precise1k/b0462: 201module rows; threshold memberships [(22, 'SoxS')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-e_coli-b0463 | https://imodulondb.org/api/genes/b0463/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b0463.raw | context_only | e_coli/precise1k/b0463: 201module rows; threshold memberships [(22, 'SoxS')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-e_coli-b2538 | https://imodulondb.org/api/genes/b2538/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2538.raw | context_only | e_coli/precise1k/b2538: 201module rows; threshold memberships []. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-e_coli-b2539 | https://imodulondb.org/api/genes/b2539/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2539.raw | context_only | e_coli/precise1k/b2539: 201module rows; threshold memberships []. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-e_coli-b2540 | https://imodulondb.org/api/genes/b2540/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2540.raw | context_only | e_coli/precise1k/b2540: 201module rows; threshold memberships []. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-e_coli-b2542 | https://imodulondb.org/api/genes/b2542/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2542.raw | context_only | e_coli/precise1k/b2542: 201module rows; threshold memberships []. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-e_coli-b3035 | https://imodulondb.org/api/genes/b3035/imodulons?organism=e_coli&amp;dataset=precise1k; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b3035.raw | context_only | e_coli/precise1k/b3035: 201module rows; threshold memberships [(22, 'SoxS')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2038 | https://imodulondb.org/api/genes/STM2038/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2038.raw | context_only | s_enterica/core/STM2038: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2039 | https://imodulondb.org/api/genes/STM2039/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2039.raw | context_only | s_enterica/core/STM2039: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2040 | https://imodulondb.org/api/genes/STM2040/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2040.raw | context_only | s_enterica/core/STM2040: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2041 | https://imodulondb.org/api/genes/STM2041/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2041.raw | context_only | s_enterica/core/STM2041: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2042 | https://imodulondb.org/api/genes/STM2042/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2042.raw | context_only | s_enterica/core/STM2042: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2045 | https://imodulondb.org/api/genes/STM2045/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2045.raw | context_only | s_enterica/core/STM2045: 115module rows; threshold memberships []. STM2045 is absent from selected gene table; all-zero fallback is not negative biological evidence. |
| micro-modules-s_enterica-STM2046 | https://imodulondb.org/api/genes/STM2046/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2046.raw | context_only | s_enterica/core/STM2046: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2048 | https://imodulondb.org/api/genes/STM2048/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2048.raw | context_only | s_enterica/core/STM2048: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2049 | https://imodulondb.org/api/genes/STM2049/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2049.raw | context_only | s_enterica/core/STM2049: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2054 | https://imodulondb.org/api/genes/STM2054/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2054.raw | context_only | s_enterica/core/STM2054: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-modules-s_enterica-STM2055 | https://imodulondb.org/api/genes/STM2055/imodulons?organism=s_enterica&amp;dataset=core; Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2055.raw | context_only | s_enterica/core/STM2055: 115module rows; threshold memberships [(33, 'pdu')]. No membership or nonmembership establishes physical localization, stoichiometry or necessity. |
| micro-e_coli-module22 | https://imodulondb.org/api/imodulons/e_coli/precise1k/22; Native module name/regulator/function, threshold, full gene membership list; generated ai_summary explicitly excluded and activities not interpreted; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/e_coli-module22.raw | context_only | e_coli/precise1k/22: SoxS, 117genes. AcrA b0463,AcrB b0462,TolC b3035 have SoxS-module membership. Computational expression association only. |
| micro-s_enterica-module33 | https://imodulondb.org/api/imodulons/s_enterica/core/33; Native module name/regulator/function, threshold, full gene membership list; generated ai_summary explicitly excluded and activities not interpreted; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/s_enterica-module33.raw | context_only | s_enterica/core/33: pdu, 19genes. Ten selected Pdu loci meet module33 threshold; PduJ missing gene-table coverage is not a contradictory result. Computational expression association only. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical command receipt only; no fresh runner execution | context_only | Actual00:49Z run exited1 with PermissionError on pyvenv.cfg. Current review uses fresh inspected official catalogue/metadata/gene/module fallback. Historical unavailability is not represented as a current successful adapter execution. |
| micro-native-propanediol_degradation_polyhedral_organelle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 11 reviewed examples; five GENE_OR_PROTEIN nodes:4COVERED+1UNANCHORED_WITH_UNIPROT. STRUCTURE-typed PduCDE omitted from this typed-node summary; its three examples separately verified. Native pass verifies its implemented identity/coverage contract, not physical membership, correct molecular class, direct binding or essentiality. |
| micro-native-propanediol_degradation_polyhedral_organelle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-causal.log SHA256 21b89ef20c41b68d80b3fb47dad935957101d412e816fd03c3b57f24706d4b84 | supports | 11 reviewed examples; five GENE_OR_PROTEIN nodes:4COVERED+1UNANCHORED_WITH_UNIPROT. STRUCTURE-typed PduCDE omitted from this typed-node summary; its three examples separately verified. Native pass verifies its implemented identity/coverage contract, not physical membership, correct molecular class, direct binding or essentiality. |
| micro-native-3_phenylpropionate_dioxygenase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 4reviewed examples and4COVERED typed nodes. Native pass verifies its implemented identity/coverage contract, not physical membership, correct molecular class, direct binding or essentiality. |
| micro-native-3_phenylpropionate_dioxygenase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-causal.log SHA256 643c232d1c030efc53020a6851cb8fbf86dc4243c87cbb2a971fc41c067a79d0 | supports | 4reviewed examples and4COVERED typed nodes. Native pass verifies its implemented identity/coverage contract, not physical membership, correct molecular class, direct binding or essentiality. |
| micro-native-acrab_tolc_multidrug_efflux_transport_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | 3reviewed examples and3COVERED typed nodes. Native pass verifies its implemented identity/coverage contract, not physical membership, correct molecular class, direct binding or essentiality. |
| micro-native-acrab_tolc_multidrug_efflux_transport_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal-receipt.json; Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal.log SHA256 d006bc9e9c113add93b358d1af24eb05ca200ab4c477df0f514cbcca129b7518 | supports | 3reviewed examples and3COVERED typed nodes. Native pass verifies its implemented identity/coverage contract, not physical membership, correct molecular class, direct binding or essentiality. |
| micro-acr-independent-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-plaque/acrab-source-attribution-challenge.json; Complete independent bounded source-attribution challenge receipt | supports | Independent second reviewer confirms only the new CPX source-attribution defect. The defining intact-complex inference and existing ESSENTIAL flags are not rejected; no depletion assay is demanded and contributes-to edges remain valid. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, exact SHA256 reverified during PR2380 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-propanediol_degradation_polyhedral_organelle-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-propanediol_degradation_polyhedral_organelle-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-chloroplast_nucleoid-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-chloroplast_nucleoid-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-kinetoplast-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-kinetoplast-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_nucleoid-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-mitochondrial_nucleoid-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-nucleoid-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-nucleoid-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_nucleoid-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-plastid_nucleoid-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-1_3_beta_d_glucan_synthase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-1_3_beta_d_glucan_synthase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-3_phenylpropionate_dioxygenase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-3_phenylpropionate_dioxygenase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-acf_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-acf_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Four assigned records are independently reassessed and nonstale. No scientific findings/actions, no invented predecessor or terminal resolution; all four retain positive qualified passes. Only four formal applicability exclusions are confirmed review-bundle defects. The tentative cohort-label concern was withdrawn: complete scope notes correctly identify the original batch26 execution reused with same-base guards.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: All current source responses are freshly retrieved with actual timestamps and SHA256. Earlier HTTP200 challenge pages, DNS failures, XML404/500 are validation context only. Genuine recovered bodies have separate receipts. Karcher2009, Jensen2012, Kucej/Butow2007 and Ogbadoyi2003 remain complete-abstract scopes; the fetched Ogbadoyi body is not claimed read.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Kobayashi2015 is primary comparative research. Only specified Introduction, Methods, first Results/Table1/Fig1–2 captions and two Discussion subsections were read. No image pixels, remaining Results/Methods, supplements or experimental reanalysis; purified proteins/heterologous E.coli compaction are not universal in vivo plastid formation tests.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Amodeo2023 is secondary review at sec1/8/10 scope. Cooper2019 body scopes distinguish391 minicircle sequence classes from copy-number estimates in EATRO1125-derived cultured populations. deSouza2017 KAP1/2 restrictions and aKAP23 non-DNA localization constrain class interpretation. Gluenz2011 microscopy scope is procyclic T.brucei, not all kinetoplastid architectures.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Kucej2008 whole scientific main text and specified Methods/captions were read: isolated-mitochondrion in organello ChIP and about70% sampled intronless genome are explicit despite the authors own in vivo interpretation. Sia2009 full short main text/Table1/captions distinguish repeated-sequence instability from point mutation and respiratory selection from fermentative mtDNA loss. No pixels, supplements or new data analysis.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Q02486/ABF2 reviewed S288C identity and unique exact query are current. HLP zero exact-query result is bounded index noncoverage, not absence of a literature-supported protein. Native HLP/KAP nodes are HAS_SYMBOLS_NO_EXAMPLES, Abf2 is COVERED and plastid inventory is empty. Optional examples are not invented.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: IPR000119 is broader HU/IHF context; IPR009071 is a domain, and IPR051965 has unchecked LLM-generated prose that is not accepted as biological proof. No exact source-neutral family equivalence or exhaustive composition is certified.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Actual whole-record positive molecular claims trigger all four applicability checks. Current full catalogue has no matching eukaryotic host; no unrelated bacterial proxy/downstream query, no biological absence inference. Historical runner failure at00:49Z is not a fresh invocation.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Thirty frozen inputs actually informed this subreview:17 common policies/config/helper inputs,4 targets,8 original artifacts and one already-frozen generic-nucleoid boundary context. Original pairs validate/render exactly and all61 historical inputs match. Generic-neighbor science/disposition belongs to its assigned reviewer; no cross-target resolution inferred.
- Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview: Root owns current global gates, native final save, committed-head checks, CI and queue. This source-stage report does not certify future execution or perform record/Git/GitHub writes. Append-only history and unresolved scientific unknowns remain preserved.
- Generic nucleoid, glucan synthase and ACF independent subreview: Three unchanged targets independently reassessed. Three original pairs validate/render exactly; all44historical input rows match. One inherited major nucleoid identity finding retained; glucan synthase and ACF qualified passes. No new scientific finding established and no records/repository/GitHub mutated.
- Generic nucleoid, glucan synthase and ACF independent subreview: Primary body scope: Wang2011 complete scientific main text/in-text experimental details, without supplementary Methods/TableS1 or pixels; Gelbart2001 sec2,6,14,15 andFig4/5 text captions; McConnell2004 sec3,9 andFig1/2 text captions. No supplements, raw data, individual images or complete separately cited-reference audit. Verma2019 is secondary synthesis, sec002 including subsections/tables/text captions andsec010,014,015; Dillon2010 secondary abstract only.
- Generic nucleoid, glucan synthase and ACF independent subreview: Glucan Douglas1994, Mazur1995, Qadota1996, Mazur/Baginsky1996, Mol1994 and Utsugi/Dijkgraaf/Sickmann annotation sources were read at complete deposited abstract/metadata scope only. PMCchallenge/guessedS3 404 responses do not count as bodies. FKS1 mitochondrial native evidence joins are verified annotation provenance, not independent mitochondrial-localization confirmation. No detailed experimental protocols or formation assay claimed.
- Generic nucleoid, glucan synthase and ACF independent subreview: Seven K-12 NAP examples and three/two S288C glucan/ACF examples are all reviewed. Native identities/coverage do not certify every mechanistic edge or experimental strain. Gelbart uses W303-derivedW1588-4C; native S288C accession mapping remains distinct. UNKNOWN formation necessity retained; activity/deletion phenotypes are not universal assembly requirements.
- Generic nucleoid, glucan synthase and ACF independent subreview: Nucleoid graph is bacterial coarse secondary synthesis with protein/concentration/magnesium/growth-phase limits and unresolved in-vivo domain barriers. Heterogeneous NAP cohort does not mean every protein performs every action. Generic nucleoid identity includes organellar children; current bacterial-only definition remains material scope defect.
- Generic nucleoid, glucan synthase and ACF independent subreview: Exact five InterPro candidates are bounded checks, not an exhaustive family-catalogue search. HU/IHF family is not whole NAP pool; GT48/WAC/Isw domains and Rho family are broader than the selected components. Existing open grounding discussions remain scientifically legitimate; no optional empty-slot or enum-only finding.
- Generic nucleoid, glucan synthase and ACF independent subreview: Fresh official catalogue has E.coli coverage and no Saccharomyces entry. e_coli/precise1k is a mixed five-strain dataset with201modules and4257genes; selected String511145 loci map to maintained K-12 examples, not all experimental conditions. Seven exact gene searches followed by all201membership flags and selected OxyR3/RpoS51/ppGpp145 metadata show dps andfis contexts; five other NAPs have no trueflags, not biological absence. AI summaries and activities excluded; no direct localization/necessity/causal inference.
- Generic nucleoid, glucan synthase and ACF independent subreview: Historical adapter runner failure is actual00:49Z evidence only, no new invocation or fresh success. Current direct public-source fallback is separate. Unused dermatology PMID15611425 request was an irrelevant scratch fetch and is excluded from evidence/assessments. Frontend-only genes endpoint is access context only. Root owns wider gates/issues/publication; pending CI/queue/merge not certified.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Only the three assigned full records receive scientific dispositions. Other batch records and neighbor/category issue states are not inferred.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Every primary-source body row states exact read sections. Metadata/abstract rows do not certify unseen body, figures, supplements or raw experiments. No source images, cryo-EM maps, protein coordinates, spectra or supplementary movies were reanalyzed; there are no maintained images in these targets.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Wheatley2013,Sutter2021,Bobik1997/Bobik1999,Cheng2011, Sinha2014 and Held2016 are bounded to the complete native abstract/metadata or explicitly cited native annotation checks. Held2016 recombinant Eut scope is not independent proof of every native Pdu localization.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Yang2020 abundance depends on QconCAT assumptions. Yang2022 EP condensation and specific PduM/PduB molecular contacts remain proposed models; shell/cargo convergence is supported without claiming new atomic contacts or one exclusive trajectory.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Pdu cohort CONDITIONAL labels are not a complete condition-by-member necessity matrix. Hca biochemical architecture includes sequence/family inference; whole-cell Hca assays also include downstream HcaB. Acr5V5S is engineered and does not independently test formation necessity.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Native protein verification checks implemented identities/xrefs/coverage, not biological membership or subclass correctness. PduCDE STRUCTURE is outside the GENE_OR_PROTEIN diagnostic summary; its exact examples were separately inspected.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Structured runner availability evidence is historical00:49Z, not a new attempt. Fresh official source fallback inspected selected multi-strain e_coli/precise1k and s_enterica/core only. Module membership, nonmembership or missing locus coverage is not assembly/phenotype/localization evidence. Generated ai_summary and raw condition activities were not used.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Initial guessed module/metadata query-form endpoints returned frontend HTML; those responses were rejected as scientific data. Failed S3 routes and one unrelated guessed PMC candidate were not read as supporting sources; genuine successfully retrieved identities were checked separately.
- Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Root owns corpus QC, final CI, queue and publication. This source report does not certify later committed-head CI or merge outcomes. No records, original bundles, repository refs or GitHub objects were changed by this reviewer.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- This immutable successor corrects review-bundle issues #2832 and #2833: two stale target inputs are substantively reassessed; ten unsupported source-applicability exclusions (seven formal, three prose) are replaced by actual whole-record applicability, official catalogue checks and covered-source queries.
- Pdu new PduCDE STRUCTURE typing and two added convergent-biogenesis edges are assessed alongside the original PduU class and BMC-T cargo-receptor findings. AcrAB-TolC new membership edges are supported, while three added CPX notes misattribute essentiality and are separately scoped for later record curation.
- Acr source-attribution correction does not reject defining-material ESSENTIAL values, assert dispensability or require new formation assays. Five inherited findings retain exact predecessor identities; the new CPX finding has no invented predecessor.
- All 47 used local inputs are frozen; the source commit is retained by review-base/pr2380-current-record-followup-20261103. All20 original review files remain byte-identical. No scientific record, history, generated page or other branch is edited.
- The batch26 historical execution wording was challenged and retained because full scope notes explicitly document its original execution and batch43 same-base reuse. No defect or issue is asserted for that accurate provenance.
- Native inventory is31 represented protein examples and20 GENE_OR_PROTEIN nodes; documented verification and causal-node commands all passed. Empty optional examples and legitimate group actors are not manufactured findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T232927Z-pr2380-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2380: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T23:15:45.781598Z'
finished_at: '2026-11-03T23:29:27Z'
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
summary: Current-input reassessment refreshes the two stale Pdu and AcrAB-TolC reviews
  and corrects ten unsupported structured-source applicability exclusions. Six scientific
  findings remain open across three records (three major and three minor), including
  one newly observed, narrowly scoped CPX essentiality-attribution issue; seven records
  have qualified positive assessments. Original observations and scientific records
  remain unchanged.
source:
  git_revision: 7b6cd533340948100b7b23d8ab4e659702d9feba
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
  - path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    sha256: 2b55cd8964b49c798747f87a1027fd9817864853f125fcdc10569ed285f784cc
    role: target
  - path: data/structures/nucleoid/chloroplast_nucleoid.yaml
    sha256: ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25
    role: target
  - path: data/structures/nucleoid/kinetoplast.yaml
    sha256: e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a
    role: target
  - path: data/structures/nucleoid/mitochondrial_nucleoid.yaml
    sha256: c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d
    role: target
  - path: data/structures/nucleoid/nucleoid.yaml
    sha256: e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08
    role: target
  - path: data/structures/nucleoid/plastid_nucleoid.yaml
    sha256: 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842
    role: target
  - path: data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
    sha256: 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc
    role: target
  - path: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    sha256: 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e
    role: target
  - path: data/structures/other/acf_complex.yaml
    sha256: 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d
    role: target
  - path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    sha256: 781dd7e152917915b204ac297248d0caa8f290a2f815b9bf9ed41f43b8819c25
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
  - path: reviews/structured/20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit/review.md
    sha256: 196decdc9df0ed89a55ab1f6c37a559337e66b651c8ad4a322d094e7177617db
    role: context
  - path: reviews/structured/20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit/review.yaml
    sha256: 53166c85e2439f7129d436ff0996c75dafde87a526cfcba46e7a63f1f57f0aea
    role: context
  - path: reviews/structured/20261022T042548Z-chloroplast-nucleoid-audit/review.md
    sha256: de7d120dd6ca98d9a03f011b8e11f2a0b6c202155198f0cb0c5bd8fbcd6974d0
    role: context
  - path: reviews/structured/20261022T042548Z-chloroplast-nucleoid-audit/review.yaml
    sha256: 70eab0f88e1ab71c70c4d72b432d3790a42319711f15169d9c2840d9e835006b
    role: context
  - path: reviews/structured/20261022T042549Z-kinetoplast-audit/review.md
    sha256: 367f1441ca6b06546314cb2f7aa1a22d4f610fefbbe75afac8953c5570bded7e
    role: context
  - path: reviews/structured/20261022T042549Z-kinetoplast-audit/review.yaml
    sha256: f16cbd9d79a441e32dc7db63392a69298f0a3a4888a2d0c70435a9ff05e6a169
    role: context
  - path: reviews/structured/20261022T042550Z-mitochondrial-nucleoid-audit/review.md
    sha256: c8e2a7ad07763d4689aa35bdc06c71b22de4c2b413294a318e10eb8b0dc5b79b
    role: context
  - path: reviews/structured/20261022T042550Z-mitochondrial-nucleoid-audit/review.yaml
    sha256: cf1f08188e6e2f40c0ce44d7683a27f887bef23ef85f6e141eda37c630d9a82b
    role: context
  - path: reviews/structured/20261022T042551Z-nucleoid-audit/review.md
    sha256: 0977aa8f5683b28a94ee9cf9ec938ef603b137233a9dc1fe02ae95bb298e911f
    role: context
  - path: reviews/structured/20261022T042551Z-nucleoid-audit/review.yaml
    sha256: 41cb6682369ea9da295f9f13500d8dd7f60c75971bbde3a7160f2562ca90b600
    role: context
  - path: reviews/structured/20261022T042551Z-plastid-nucleoid-audit/review.md
    sha256: 20fd3bb4cfc895d44d515e02bc870d182a22690bc28c13668ae6050fc9304a30
    role: context
  - path: reviews/structured/20261022T042551Z-plastid-nucleoid-audit/review.yaml
    sha256: bd68c472e18d9009c35dd640700ab9422f857eb37b29a79cc6b41d8e7a9146f8
    role: context
  - path: reviews/structured/20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit/review.md
    sha256: 311334e2fad96d010d7c57674f4dde0ad59ccd5fd75db967a89fa2fe5c8e8b62
    role: context
  - path: reviews/structured/20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit/review.yaml
    sha256: e881a8058d08a36997b16b19b298152d5c347df67d579851347daa78433a74f7
    role: context
  - path: reviews/structured/20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit/review.md
    sha256: a1b233bbf495596eda637afb93fc3aefd96f8070ad47d02daae4e4d526279d76
    role: context
  - path: reviews/structured/20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit/review.yaml
    sha256: e2920ac68a117c70a04bc1446d841e4f3ba0d1d8b828b8c839d8bf08fb656e5f
    role: context
  - path: reviews/structured/20261022T042554Z-acf-complex-audit/review.md
    sha256: 2e1f5a3c3f599f795aa6a0c1eba1c4898f22e938e17ac98101f5e3bb64d5442e
    role: context
  - path: reviews/structured/20261022T042554Z-acf-complex-audit/review.yaml
    sha256: a45c3dabfbef02e1ffe4558429ff9b775b6564ada70e2a30617ab81ee81388fc
    role: context
  - path: reviews/structured/20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit/review.md
    sha256: 01315cc641aabdd2e9dcd5e015f31abb7ccbec5cfab0ed632331278b2cf072f7
    role: context
  - path: reviews/structured/20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml
    sha256: 17ce9ceedb6bbe85b4c7343c55e968970c093e3fa088a8d11c5e0b1d1270d42c
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
- target_id: GO:0031472
  path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  label: propanediol degradation polyhedral organelle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
- target_id: GO:0042644
  path: data/structures/nucleoid/chloroplast_nucleoid.yaml
  label: chloroplast nucleoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/chloroplast_nucleoid.yaml
    role: maintained scientific record
- target_id: GO:0020023
  path: data/structures/nucleoid/kinetoplast.yaml
  label: kinetoplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/kinetoplast.yaml
    role: maintained scientific record
- target_id: GO:0042645
  path: data/structures/nucleoid/mitochondrial_nucleoid.yaml
  label: mitochondrial nucleoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/mitochondrial_nucleoid.yaml
    role: maintained scientific record
- target_id: GO:0009295
  path: data/structures/nucleoid/nucleoid.yaml
  label: nucleoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/nucleoid.yaml
    role: maintained scientific record
- target_id: GO:0042646
  path: data/structures/nucleoid/plastid_nucleoid.yaml
  label: plastid nucleoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/plastid_nucleoid.yaml
    role: maintained scientific record
- target_id: GO:0000148
  path: data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
  label: 1,3-beta-D-glucan synthase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
    role: maintained scientific record
- target_id: GO:0009334
  path: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  label: 3-phenylpropionate dioxygenase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    role: maintained scientific record
- target_id: GO:0016590
  path: data/structures/other/acf_complex.yaml
  label: ACF complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acf_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  label: AcrAB-TolC multidrug efflux transport complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 3a10e7b468ffc187a10f8d6b123120f8cdbbcf14.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    71e8b8755cdeab5619000ba0b749999107ecd8c4.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 7b6cd533340948100b7b23d8ab4e659702d9feba.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 7b6cd533340948100b7b23d8ab4e659702d9feba.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 7b6cd533340948100b7b23d8ab4e659702d9feba.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 7b6cd533340948100b7b23d8ab4e659702d9feba.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just check-curies
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 7b6cd533340948100b7b23d8ab4e659702d9feba.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0031472
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just validate data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0031472
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: just validate-strict data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0042644
  status: passed
  required: true
  target_ids:
  - GO:0042644
  command: just validate data/structures/nucleoid/chloroplast_nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0042644
  status: passed
  required: true
  target_ids:
  - GO:0042644
  command: just validate-strict data/structures/nucleoid/chloroplast_nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0020023
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just validate data/structures/nucleoid/kinetoplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0020023
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: just validate-strict data/structures/nucleoid/kinetoplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0042645
  status: passed
  required: true
  target_ids:
  - GO:0042645
  command: just validate data/structures/nucleoid/mitochondrial_nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0042645
  status: passed
  required: true
  target_ids:
  - GO:0042645
  command: just validate-strict data/structures/nucleoid/mitochondrial_nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0009295
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just validate data/structures/nucleoid/nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0009295
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just validate-strict data/structures/nucleoid/nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0042646
  status: passed
  required: true
  target_ids:
  - GO:0042646
  command: just validate data/structures/nucleoid/plastid_nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0042646
  status: passed
  required: true
  target_ids:
  - GO:0042646
  command: just validate-strict data/structures/nucleoid/plastid_nucleoid.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0000148
  status: passed
  required: true
  target_ids:
  - GO:0000148
  command: just validate data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0000148
  status: passed
  required: true
  target_ids:
  - GO:0000148
  command: just validate-strict data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0009334
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: just validate data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0009334
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: just validate-strict data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0016590
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just validate data/structures/other/acf_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0016590
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just validate-strict data/structures/other/acf_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: just validate-strict data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380
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
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: All ten targets contain positive molecular or pathway claims and require
    applicability assessment. Fresh official catalogue supports matched Salmonella
    core and E.coli precise1k checks; these are mixed six-strain and five-strain datasets,
    respectively, not strain-specific physical-assembly evidence. Actual gene/module
    checks retain thresholds and absent-gene endpoint limits. The catalogue has no
    matching eukaryotic host for the assigned algal/plant, kinetoplastid and yeast
    contexts; no unrelated bacterial proxy or biological absence inference is substituted.
    Historical runner unavailability is retained separately; public-source fallback
    is current.
  evidence_ids:
  - septin-catalogue
  - plaque-adapter-genes-access
  - plaque-catalogue
  - plaque-adapter-meta
  - plaque-adapter-imodulons
  - plaque-adapter-search-hupA
  - plaque-adapter-search-hupB
  - plaque-adapter-search-ihfA
  - plaque-adapter-search-ihfB
  - plaque-adapter-search-fis
  - plaque-adapter-search-hns
  - plaque-adapter-search-dps
  - plaque-adapter-gene-b4000
  - plaque-adapter-gene-b4000-modules
  - plaque-adapter-gene-b0440
  - plaque-adapter-gene-b0440-modules
  - plaque-adapter-gene-b1712
  - plaque-adapter-gene-b1712-modules
  - plaque-adapter-gene-b0912
  - plaque-adapter-gene-b0912-modules
  - plaque-adapter-gene-b3261
  - plaque-adapter-gene-b3261-modules
  - plaque-adapter-gene-b1237
  - plaque-adapter-gene-b1237-modules
  - plaque-adapter-gene-b0812
  - plaque-adapter-gene-b0812-modules
  - plaque-adapter-module-3
  - plaque-adapter-module-51
  - plaque-adapter-module-145
  - micro-catalogue
  - micro-e_coli-meta
  - micro-e_coli-genes
  - micro-e_coli-module-list
  - micro-s_enterica-meta
  - micro-s_enterica-genes
  - micro-s_enterica-module-list
  - micro-modules-e_coli-b0462
  - micro-modules-e_coli-b0463
  - micro-modules-e_coli-b2538
  - micro-modules-e_coli-b2539
  - micro-modules-e_coli-b2540
  - micro-modules-e_coli-b2542
  - micro-modules-e_coli-b3035
  - micro-modules-s_enterica-STM2038
  - micro-modules-s_enterica-STM2039
  - micro-modules-s_enterica-STM2040
  - micro-modules-s_enterica-STM2041
  - micro-modules-s_enterica-STM2042
  - micro-modules-s_enterica-STM2045
  - micro-modules-s_enterica-STM2046
  - micro-modules-s_enterica-STM2048
  - micro-modules-s_enterica-STM2049
  - micro-modules-s_enterica-STM2054
  - micro-modules-s_enterica-STM2055
  - micro-e_coli-module22
  - micro-s_enterica-module33
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-graph-policy
  - septin-protein-policy
  - septin-review-contract
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-root43-sources-go
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-SL0150
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-family-IPR009071
  - septin-nucleoid-agent-family-IPR051965
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-gluenz2011-canonical
  - plaque-policy
  - plaque-rubric
  - plaque-schema-policy
  - plaque-history-policy
  - plaque-go-terms
  - plaque-sl-0187
  - plaque-tax-2
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-tax-511145
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-dillon2010-meta
  - plaque-verma2019-meta
  - plaque-douglas1994-meta
  - plaque-mazur1995-meta
  - plaque-qadota1996-meta
  - plaque-mazur1996-meta
  - plaque-gelbart2001-meta
  - plaque-mcconnell2004-meta
  - plaque-pmid-21903814
  - plaque-pmid-333393
  - plaque-pmid-11856368
  - plaque-pmid-12185837
  - plaque-pmid-14576278
  - plaque-pmid-7565718
  - plaque-pmid-14562095
  - plaque-pmid-11238944
  - plaque-pmid-15024052
  - plaque-pmid-7983071
  - plaque-verma2019-jats
  - plaque-wang2011-jats
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
  - plaque-verma2019-pmc-access
  - plaque-wang2011-pmc-access
  - plaque-douglas1994-pmc-access
  - plaque-mazur1995-pmc-access
  - plaque-adapter-genes-access
  - plaque-douglas1994-jats-access
  - plaque-mazur1995-jats-access
  - plaque-gelbart2001-jats-access
  - plaque-mcconnell2004-jats-access
  - plaque-up-P0ACF0
  - plaque-up-P0ACF4
  - plaque-up-P0A6X7
  - plaque-up-P0A6Y1
  - plaque-up-P0A6R3
  - plaque-up-P0ACF8
  - plaque-up-P0ABT2
  - plaque-up-P38631
  - plaque-up-P40989
  - plaque-up-P06780
  - plaque-up-Q08773
  - plaque-up-P53125
  - plaque-ipr-IPR000119
  - plaque-ipr-IPR003440
  - plaque-ipr-IPR003578
  - plaque-ipr-IPR013136
  - plaque-ipr-IPR044754
  - plaque-catalogue
  - plaque-adapter-meta
  - plaque-adapter-imodulons
  - plaque-adapter-gene-b4000
  - plaque-adapter-gene-b4000-modules
  - plaque-adapter-gene-b0440
  - plaque-adapter-gene-b0440-modules
  - plaque-adapter-gene-b1712
  - plaque-adapter-gene-b1712-modules
  - plaque-adapter-gene-b0912
  - plaque-adapter-gene-b0912-modules
  - plaque-adapter-gene-b3261
  - plaque-adapter-gene-b3261-modules
  - plaque-adapter-gene-b1237
  - plaque-adapter-gene-b1237-modules
  - plaque-adapter-gene-b0812
  - plaque-adapter-gene-b0812-modules
  - plaque-adapter-module-3
  - plaque-adapter-module-51
  - plaque-adapter-module-145
  - micro-policy
  - micro-native-review-policy
  - micro-up-H9L478
  - micro-up-O31041
  - micro-up-O31042
  - micro-up-P02930
  - micro-up-P0A1C7
  - micro-up-P0A1D1
  - micro-up-P0ABR5
  - micro-up-P0ABW0
  - micro-up-P0AE06
  - micro-up-P31224
  - micro-up-P37449
  - micro-up-P37450
  - micro-up-P77650
  - micro-up-Q47140
  - micro-up-Q9XDM8
  - micro-up-Q9XDN3
  - micro-up-Q9XDN4
  - micro-up-Q9XDN6
  - micro-ipr-IPR020875
  - micro-ipr-IPR023712
  - micro-ipr-IPR023739
  - micro-ipr-IPR023744
  - micro-ipr-IPR030992
  - micro-ipr-IPR058622
  - micro-ipr-IPR058628
  - micro-ipr-IPR044870
  - micro-go-0008695
  - micro-go-0009334
  - micro-go-0031469
  - micro-go-0031472
  - micro-go-0042910
  - micro-go-0050215
  - micro-go-0051144
  - micro-go-1990204
  - micro-go-1990281
  - micro-tax-2
  - micro-tax-83333
  - micro-tax-99287
  - micro-eco-0353
  - micro-cpx
  - micro-pdb
  - micro-pdb-entity1
  - micro-pdb-entity2
  - micro-pdb-entity3
  - micro-meta-doi-0
  - micro-meta-doi-1
  - micro-meta-doi-10
  - micro-meta-doi-11
  - micro-meta-doi-12
  - micro-meta-doi-2
  - micro-meta-doi-3
  - micro-meta-doi-4
  - micro-meta-doi-5
  - micro-meta-doi-6
  - micro-meta-doi-7
  - micro-meta-doi-8
  - micro-meta-doi-9
  - micro-meta-pmid-10498708
  - micro-meta-pmid-11844753
  - micro-meta-pmid-12923081
  - micro-meta-pmid-21239588
  - micro-meta-pmid-22343294
  - micro-meta-pmid-24747050
  - micro-meta-pmid-27063436
  - micro-meta-pmid-28355133
  - micro-meta-pmid-9603882
  - micro-meta-fan2012-meta
  - micro-meta-pduu2008-meta
  - micro-yang2020
  - micro-yang2022
  - micro-havemann2002
  - micro-havemann2003
  - micro-fan2010
  - micro-fan2011
  - micro-fan2012
  - micro-sinha2012
  - micro-sampson2008
  - micro-diaz1998
  - micro-wang2017
  - micro-e_coli-meta
  - micro-e_coli-module-list
  - micro-s_enterica-meta
  - micro-s_enterica-module-list
  - micro-e_coli-module22
  - micro-s_enterica-module33
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
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
- check_id: propanediol_degradation_polyhedral_organelle-uniprot-verify
  name: Native propanediol degradation polyhedral organelle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    --verify
  exit_code: 0
  summary: 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-propanediol_degradation_polyhedral_organelle-uniprot-verify
- check_id: propanediol_degradation_polyhedral_organelle-uniprot-causal
  name: Native propanediol degradation polyhedral organelle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031472
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    --causal-graphs
  exit_code: 0
  summary: 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-propanediol_degradation_polyhedral_organelle-uniprot-causal
- check_id: chloroplast_nucleoid-uniprot-verify
  name: Native chloroplast nucleoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042644
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/chloroplast_nucleoid.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-chloroplast_nucleoid-uniprot-verify
- check_id: chloroplast_nucleoid-uniprot-causal
  name: Native chloroplast nucleoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042644
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/chloroplast_nucleoid.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-chloroplast_nucleoid-uniprot-causal
- check_id: kinetoplast-uniprot-verify
  name: Native kinetoplast UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/kinetoplast.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-kinetoplast-uniprot-verify
- check_id: kinetoplast-uniprot-causal
  name: Native kinetoplast UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020023
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/kinetoplast.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-kinetoplast-uniprot-causal
- check_id: mitochondrial_nucleoid-uniprot-verify
  name: Native mitochondrial nucleoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042645
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/mitochondrial_nucleoid.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_nucleoid-uniprot-verify
- check_id: mitochondrial_nucleoid-uniprot-causal
  name: Native mitochondrial nucleoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042645
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/mitochondrial_nucleoid.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-mitochondrial_nucleoid-uniprot-causal
- check_id: nucleoid-uniprot-verify
  name: Native nucleoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/nucleoid.yaml
    --verify
  exit_code: 0
  summary: 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-nucleoid-uniprot-verify
- check_id: nucleoid-uniprot-causal
  name: Native nucleoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/nucleoid.yaml
    --causal-graphs
  exit_code: 0
  summary: 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-nucleoid-uniprot-causal
- check_id: plastid_nucleoid-uniprot-verify
  name: Native plastid nucleoid UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0042646
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/plastid_nucleoid.yaml
    --verify
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_nucleoid-uniprot-verify
- check_id: plastid_nucleoid-uniprot-causal
  name: Native plastid nucleoid UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0042646
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/plastid_nucleoid.yaml
    --causal-graphs
  exit_code: 0
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-plastid_nucleoid-uniprot-causal
- check_id: 1_3_beta_d_glucan_synthase_complex-uniprot-verify
  name: Native 1,3-beta-D-glucan synthase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000148
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-1_3_beta_d_glucan_synthase_complex-uniprot-verify
- check_id: 1_3_beta_d_glucan_synthase_complex-uniprot-causal
  name: Native 1,3-beta-D-glucan synthase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000148
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-1_3_beta_d_glucan_synthase_complex-uniprot-causal
- check_id: 3_phenylpropionate_dioxygenase_complex-uniprot-verify
  name: Native 3-phenylpropionate dioxygenase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-3_phenylpropionate_dioxygenase_complex-uniprot-verify
- check_id: 3_phenylpropionate_dioxygenase_complex-uniprot-causal
  name: Native 3-phenylpropionate dioxygenase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-3_phenylpropionate_dioxygenase_complex-uniprot-causal
- check_id: acf_complex-uniprot-verify
  name: Native ACF complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acf_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-acf_complex-uniprot-verify
- check_id: acf_complex-uniprot-causal
  name: Native ACF complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acf_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-acf_complex-uniprot-causal
- check_id: acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify
  name: Native AcrAB-TolC multidrug efflux transport complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify
- check_id: acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal
  name: Native AcrAB-TolC multidrug efflux transport complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 6be0e75f5fb1ffa1081869af24522c1c2864d31090832eacb2f920b3dec3d443;
    current SHA256 2b55cd8964b49c798747f87a1027fd9817864853f125fcdc10569ed285f784cc.
    Changed record reassessed against current sources.
  snapshot_sha256: 2b55cd8964b49c798747f87a1027fd9817864853f125fcdc10569ed285f784cc
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 53166c85e2439f7129d436ff0996c75dafde87a526cfcba46e7a63f1f57f0aea
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/nucleoid/chloroplast_nucleoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25;
    current SHA256 ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25.
    Record bytes unchanged since the original review.
  snapshot_sha256: ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T042548Z-chloroplast-nucleoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 70eab0f88e1ab71c70c4d72b432d3790a42319711f15169d9c2840d9e835006b
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/nucleoid/kinetoplast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a;
    current SHA256 e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a.
    Record bytes unchanged since the original review.
  snapshot_sha256: e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T042549Z-kinetoplast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f16cbd9d79a441e32dc7db63392a69298f0a3a4888a2d0c70435a9ff05e6a169
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/nucleoid/mitochondrial_nucleoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d;
    current SHA256 c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d.
    Record bytes unchanged since the original review.
  snapshot_sha256: c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T042550Z-mitochondrial-nucleoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: cf1f08188e6e2f40c0ce44d7683a27f887bef23ef85f6e141eda37c630d9a82b
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/nucleoid/nucleoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08;
    current SHA256 e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08.
    Record bytes unchanged since the original review.
  snapshot_sha256: e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T042551Z-nucleoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 41cb6682369ea9da295f9f13500d8dd7f60c75971bbde3a7160f2562ca90b600
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/nucleoid/plastid_nucleoid.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842;
    current SHA256 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842.
    Record bytes unchanged since the original review.
  snapshot_sha256: 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T042551Z-plastid-nucleoid-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: bd68c472e18d9009c35dd640700ab9422f857eb37b29a79cc6b41d8e7a9146f8
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc;
    current SHA256 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e881a8058d08a36997b16b19b298152d5c347df67d579851347daa78433a74f7
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e;
    current SHA256 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e2920ac68a117c70a04bc1446d841e4f3ba0d1d8b828b8c839d8bf08fb656e5f
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/acf_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d;
    current SHA256 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d.
    Record bytes unchanged since the original review.
  snapshot_sha256: 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T042554Z-acf-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a45c3dabfbef02e1ffe4558429ff9b775b6564ada70e2a30617ab81ee81388fc
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Original frozen SHA256 f6cb94dea736f627892fc1cdc8a1f44668752e605644876e937a6f11ecc0f62d;
    current SHA256 781dd7e152917915b204ac297248d0caa8f290a2f815b9bf9ed41f43b8819c25.
    Changed record reassessed against current sources.
  snapshot_sha256: 781dd7e152917915b204ac297248d0caa8f290a2f815b9bf9ed41f43b8819c25
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T23:29:27Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 17ce9ceedb6bbe85b4c7343c55e968970c093e3fa088a8d11c5e0b1d1270d42c
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Complete source/scope/frozen-input review and structured-source cross-check
    contract
  summary: Positive named molecular/pathway assertions anywhere in a record trigger
    applicability assessment. Lack of computational expression-module claims is not
    an exemption.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Taxon-agnostic family or class components; formation necessity; dated rationale
  summary: Generic protein classes and collective constitutional material are allowed;
    absent optional examples or exact family groundings are not automatic defects.
    Dated rationale and history remain append-only.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Structure identity, examples, taxonomic presence and graph/essentiality
    enums
  summary: Identity, reference-strain protein example, source experiment, localization,
    organization and formation necessity are distinct. COMMON is qualitative presence
    with losses as exceptions, not a measured census.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Coarse FUNCTION or ASSEMBLY/NONMECHANISTIC scope
  summary: A coarse packaging/organization graph need not supply replication enzymology
    or a full assembly pathway. Edge-level experiments retain actual taxon and assay
    context.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Actual identity versus represented-symbol coverage
  summary: COVERED and HAS_SYMBOLS_NO_EXAMPLES describe native inventory coverage;
    neither establishes universal localization/formation necessity. Generic classes
    do not require invented accession representatives.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-review-contract
  kind: authority
  reference: docs/record-reviews.md
  locator: Immutable source inputs, verdicts and exact prior finding identities
  summary: Original reviews are preserved. No scientific finding or prior occurrence
    is invented for an original clean review. Native validation does not certify biology.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
- evidence_id: septin-nucleoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009295,GO:0042644,GO:0042645,GO:0042646,GO:0009570,GO:0009532,GO:0005759,GO:0051276
  locator: Fresh response independently read for this successor. Complete eight-term
    native names, definitions, active states and typed child relations
  accessed_at: '2026-11-03T23:18:44.662043Z'
  support: supports
  summary: GO0009295 denotes a nucleic-acid region in a virus, bacterial cell, mitochondrion
    or chloroplast. GO0042644/0042645/0042646 exactly identify the three organellar
    nucleoid classes. The returned stroma/matrix terms show their corresponding nucleoid
    part_of children; GO0051276 is chromosome organization. Each exact term was read;
    no omitted edge is treated as biological disproof.
  snapshot_sha256: 157b49ca60fedbfa204de107ed8accec843e846c341d6803ca0c7b3b2b8b2b14
- evidence_id: septin-nucleoid-agent-go-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042644,GO:0042645,GO:0042646/ancestors?relations=is_a
  locator: Fresh response independently read for this successor. Complete is_a-only
    ancestor arrays for GO0042644, GO0042645 and GO0042646
  accessed_at: '2026-11-03T23:18:44.648996Z'
  support: supports
  summary: The is_a-only response places chloroplast nucleoid under plastid nucleoid
    and places both plastid and mitochondrial nucleoids under generic nucleoid. The
    direct typed child relations are independently visible in the term response. This
    request does not establish parthood.
  snapshot_sha256: ca89714e653442f4f3d54532fb4a24f02f4bb7443db4be2ec7d2462c9b738df3
- evidence_id: septin-nucleoid-agent-karcher2009-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/mp/ssp083%22
  locator: Fresh response independently read for this successor. Unique native Europe
    PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract
  accessed_at: '2026-11-03T23:18:44.682930Z'
  support: supports
  summary: Karcher D, Köster D, Schadach A, Klevesath A and Bock R2009, DOI10.1093/mp/ssp083,
    PMID19995727. The complete primary abstract reports C. reinhardtii HLP chloroplast
    targeting/nucleoid association, RNAi-altered nucleoid structure, apparently reduced
    compaction and reduced plastome copy number. This is abstract-level evidence,
    not a full Methods or strain audit.
  snapshot_sha256: 565c165b0882c6d382ef3539d17417fad3dc69de235107bbd608f2d1ab89deac
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:44.682930Z.
- evidence_id: septin-nucleoid-agent-kobayashi2015-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/gbe/evv233%22
  locator: Fresh response independently read for this successor. Unique native Europe
    PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract
  accessed_at: '2026-11-03T23:18:44.762751Z'
  support: supports
  summary: Kobayashi et al.2015, DOI10.1093/gbe/evv233, PMC4758235, is primary research
    on evolutionary differences in chloroplast nucleoid proteins, not a review article.
    The abstract identifies comparative proteomic, cell-biological and biochemical
    work in green plants.
  snapshot_sha256: 4258f55cc96e99bdabbcbbf2ec1e28f28f69cd066dca146d22128f4444851647
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:44.762751Z.
- evidence_id: septin-nucleoid-agent-kobayashi2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4758235.1/PMC4758235.1.xml
  locator: 'Genuine fresh JATS: complete Introduction; Methods Plant Culture Conditions,
    Nuclear Transformation of C. reinhardtii and Isolation of cp Nucleoids; complete
    first Results subsection with Table1/Fig1–2 captions; Discussion HLP as a Prokaryotic
    Component and Evolutionary Scenario of Cp Nucleoid Proteins. No figure pixels,
    other Results/Methods or supplements.'
  accessed_at: '2026-11-03T23:18:44.149899Z'
  support: supports
  summary: Primary comparative research, not a review article. Direct CreHLP localization
    and purified-nucleoid recovery support Chlamydomonas membership; CreCNS candidates
    are separated from verified localizations. Purified-protein binding and heterologous
    E.coli compaction do not establish universal plastid formation necessity. Protein
    complements vary across green-plant lineages; evolutionary replacement is an interpreted
    model, not an exhaustive census.
  snapshot_sha256: 24f41afe4710e910e26741b3460c4c45982cc34d04c74fef351d6505023bc8e4
- evidence_id: septin-nucleoid-agent-tax3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage
    and names
  accessed_at: '2026-11-03T23:18:44.653673Z'
  support: supports
  summary: ENA 3055 identifies Chlamydomonas reinhardtii, rank species. This verifies
    this named taxon only; it does not measure prevalence or identify a different
    experimental strain.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: septin-nucleoid-agent-family-IPR000119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000119/
  locator: Fresh response independently read for this successor. Native accession/type/name,
    complete description, child families and integrated signatures
  accessed_at: '2026-11-03T23:18:44.673580Z'
  support: supports
  summary: IPR000119 is the Histone-like DNA-binding protein family. It includes bacterial
    HU, IHF and other members and notes algal chloroplast-encoded representatives.
    It is a relevant broader family candidate, not an exact identification of the
    localized chloroplast-nucleoid HU-like cohort; no new family grounding is forced.
  snapshot_sha256: 2d778c0a6dc148b8ae5dd8242ed2ee98cede39e09253798ac3e85ec4a2de2e88
- evidence_id: septin-nucleoid-agent-gene-HLP
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AHLP%29%20AND%20%28organism_id%3A3055%29
  locator: Fresh response independently read for this successor. Complete current
    UniProt JSON result array and returned entry genes; query conditions in exact
    source URL
  accessed_at: '2026-11-03T23:18:44.561193Z'
  support: context_only
  summary: The exact HLP gene query in taxon3055 returns zero entries across the queried
    statuses. This bounded index result does not negate the directly supported literature
    HLP name or establish that no protein accession exists under another locus/alias.
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProt REST exact query as encoded in the reference, size500, all
    statuses for HLP; reviewed only for ABF2; no date filter; complete returned result
    array and suggestions distinguished from results. Access 2026-11-03T23:18:44.561193Z.
- evidence_id: septin-root43-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204
  locator: Fresh response; exact GO0020023/0005739 identity, active status, definitions
    and relevant part_of child only. Six unrelated terms are not assigned verdicts.
  accessed_at: '2026-11-03T23:18:44.673721Z'
  support: supports
  summary: GO0020023 denotes the kinetoplast region in the single mitochondrion of
    kinetoplastid parasites. GO0005739 lists the kinetoplast part_of child; this verifies
    anatomy, not a complete kinetoplast replication mechanism.
  snapshot_sha256: 758170e2adf2bdecccd550d870e811d4aa0171ee8322ea75ccf5c4e3fd84ca83
- evidence_id: septin-root43-sources-tax5653
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5653
  locator: Fresh response independently read for this successor. Complete native taxonomy
    response
  accessed_at: '2026-11-03T23:18:44.685336Z'
  support: supports
  summary: ENA verifies Kinetoplastea identity, rank and lineage.
  snapshot_sha256: 6e467f5ff25d9bd8189b9c916942db46996eee6ad67fa41afd146096c2fb0556
- evidence_id: septin-root43-sources-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Fresh response independently read for this successor. Complete native taxonomy
    response
  accessed_at: '2026-11-03T23:18:44.767625Z'
  support: supports
  summary: ENA verifies Trypanosoma brucei identity, rank and lineage.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: septin-root43-sources-SL0150
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0150.json
  locator: Fresh response independently read for this successor. Complete native response,
    including matrix/mitochondrion parthood
  accessed_at: '2026-11-03T23:18:45.141148Z'
  support: supports
  summary: Native SL0150 maps to GO0020023 and describes mitochondrial maxicircle/minicircle
    network organization.
  snapshot_sha256: a2ff48cddc11468ae130307891a3b1b0593051d67fe6ae0f108861f392d75148
- evidence_id: septin-root43-sources-doi-1
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.E02-08-0525&format=json&resultType=core
  locator: Fresh response independently read for this successor. Complete native MED
    bibliographic identity and complete returned abstract
  accessed_at: '2026-11-03T23:18:45.254024Z'
  support: supports
  summary: Ogbadoyi2003 MED12802053 DOI10.1091/mbc.E02-08-0525 identifies a TAC linkage
    across mitochondrial membranes to basal bodies; this is contextual machinery,
    not the DNA region itself.
  snapshot_sha256: 3d4dee6329fe68410ff7e0c47f868798c992db1a43b507fc9d4d3be72fe49af5
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.254024Z.
- evidence_id: septin-root43-sources-doi-2
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Ffemsre%2Ffuac047&format=json&resultType=core
  locator: Fresh response independently read for this successor. Complete native MED
    bibliographic identity and complete returned abstract
  accessed_at: '2026-11-03T23:18:45.319615Z'
  support: supports
  summary: Amodeo2023 MED36449697 DOI10.1093/femsre/fuac047 is a secondary review
    centered on T.brucei and explicitly proposes an updated replication model.
  snapshot_sha256: 4dd435c8a25c9a2e8119cc39381a74901437024ab15966565625236dd2e40ca1
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.319615Z.
- evidence_id: septin-root43-sources-doi-3
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Fnar%2Fgkz928&format=json&resultType=core
  locator: Fresh response independently read for this successor. Complete native MED
    bibliographic identity and complete returned abstract
  accessed_at: '2026-11-03T23:18:45.280143Z'
  support: supports
  summary: Cooper2019 MED31665448 DOI10.1093/nar/gkz928 reports391 assembled minicircle
    classes and predicted/expressed guide RNAs in a defined T.brucei strain, not391
    total circles per organelle.
  snapshot_sha256: a879dc889caaafe2755cfe60fb6f4996a4aec491a5592f3f516bc3de88f15b50
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.280143Z.
- evidence_id: septin-root43-sources-doi-5
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMCB.01176-10&format=json&resultType=core
  locator: Fresh response independently read for this successor. Complete native MED
    bibliographic identity and complete returned abstract
  accessed_at: '2026-11-03T23:18:45.286393Z'
  support: supports
  summary: Gluenz2011 MED21173163 DOI10.1128/MCB.01176-10 reports serial-section microscopy
    and maxicircle/minicircle probes across the duplication cycle. Native MED omitted
    its PMC field; genuine PMC3067821 was recovered separately.
  snapshot_sha256: 029661b36faa9b48cad2d1105ceb324a892abe0bdef8a0ede098d8c9466811ab
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.286393Z.
- evidence_id: septin-root43-sources-doi-8
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-micro-092611-150057&format=json&resultType=core
  locator: Fresh response independently read for this successor. Complete native MED
    bibliographic identity and complete returned abstract
  accessed_at: '2026-11-03T23:18:45.323210Z'
  support: supports
  summary: Jensen2012 MED22994497 DOI10.1146/annurev-micro-092611-150057 is a review
    of network structure, replication and segregation.
  snapshot_sha256: 340bb78f4a61993112a200d3770f34bea810b89b804ee4bcc5a24363e53c75e6
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.323210Z.
- evidence_id: septin-root43-sources-doi-9
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371%2Fjournal.pone.0187516&format=json&resultType=core
  locator: Fresh response independently read for this successor. Complete native MED
    bibliographic identity and complete returned abstract
  accessed_at: '2026-11-03T23:18:45.313320Z'
  support: supports
  summary: deSouza2017 MED29131838 DOI10.1371/journal.pone.0187516 studies comparative
    KAP repertoires and distinct localization patterns in symbiont-bearing trypanosomatids.
  snapshot_sha256: d3a6f36c2994f793c42f0dba3718c5610c2b85b25fdeec0eb7dcdc3f32fe87e6
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.313320Z.
- evidence_id: septin-nucleoid-agent-SL-0269
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0269.json
  locator: Fresh response independently read for this successor. Complete native name/definition/synonyms/GO
    and part-of hierarchy
  accessed_at: '2026-11-03T23:18:45.769681Z'
  support: supports
  summary: SL0269 identifies Mitochondrion nucleoid, maps GO0042645, supplies mitochondrial
    nucleoid and mitochromosome synonyms and places the location under mitochondrial
    matrix SL0170/GO0005759.
  snapshot_sha256: a8d00d2f20b2ea058e41b4768154df594b1902d742af3a2a6834dad64a5c2c98
- evidence_id: septin-nucleoid-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage
    and names
  accessed_at: '2026-11-03T23:18:45.549554Z'
  support: supports
  summary: ENA 4932 identifies Saccharomyces cerevisiae, rank species. This verifies
    this named taxon only; it does not measure prevalence or identify a different
    experimental strain.
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
- evidence_id: septin-nucleoid-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage
    and names
  accessed_at: '2026-11-03T23:18:45.615986Z'
  support: supports
  summary: ENA 559292 identifies Saccharomyces cerevisiae S288C, rank strain. This
    verifies this named taxon only; it does not measure prevalence or identify a different
    experimental strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-nucleoid-agent-kucej2008-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1242/jcs.028605%22
  locator: Fresh response independently read for this successor. Unique native Europe
    PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract
  accessed_at: '2026-11-03T23:18:45.804806Z'
  support: supports
  summary: Kucej M, Kucejova B, Subramanian R, Chen XJ and Butow RA2008, DOI10.1242/jcs.028605/PMC5728373.
    The complete abstract reports in organello ChIP-chip, genome-wide Abf2 association
    and metabolic remodeling.
  snapshot_sha256: 06b7c93ff57196cc6ba560c9b9aaf72931e2ad8f9b420177cfdc85fa340a234d
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.804806Z.
- evidence_id: septin-nucleoid-agent-kucej2007-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.tcb.2007.08.007%22
  locator: Fresh response independently read for this successor. Unique native Europe
    PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract
  accessed_at: '2026-11-03T23:18:45.860357Z'
  support: supports
  summary: Kucej M and Butow RA2007, DOI10.1016/j.tcb.2007.08.007, PMID17981466, is
    a review. The complete abstract describes mitochondrial DNA-protein particles,
    species-specific protein combinations and HMG packaging proteins. No full review
    body is claimed.
  snapshot_sha256: 60671b7660305ead8ea0fd8f4989fd30095e4bb135ae015762c491c05d3e349a
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.860357Z.
- evidence_id: septin-nucleoid-agent-sia2009-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1534/genetics.108.095786%22
  locator: Fresh response independently read for this successor. Unique native Europe
    PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract
  accessed_at: '2026-11-03T23:18:45.930140Z'
  support: supports
  summary: Sia RA, Carrol S, Kalifa L, Hochmuth C and Sia EA2009, DOI10.1534/genetics.108.095786/PMC2621183.
    The abstract distinguishes increased frameshifts/direct-repeat deletions from
    no point-mutation-rate effect.
  snapshot_sha256: e9bb0139bb23cbeb110727128f3caefbe77c98c56f3ba0a6b61f5aba4f3f09ae
  search_scope: Europe PMC REST exact DOI query as encoded in reference, resultType=core,
    default page size25, no date filter; exactly one returned MED hit and complete
    abstract read, not an exhaustive literature search. Access 2026-11-03T23:18:45.930140Z.
- evidence_id: septin-nucleoid-agent-protein-Q02486
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q02486.json
  locator: Fresh response independently read for this successor. Exact accession/status/name/genes/taxon
    and subcellular-location comments; native family crossrefs inspected separately
  accessed_at: '2026-11-03T23:18:46.682278Z'
  support: supports
  summary: Q02486 is reviewed ARS-binding factor2, mitochondrial, primary gene ABF2
    with HIM1/YMR072W/YM9916.11 tokens, organism559292. It verifies the reference-strain
    example identity; the current location comments alone do not cite the Kucej/Sia
    nucleoid experiments.
  snapshot_sha256: 598307b8c9dbce8b7e341554122e14bcd4b360a371e82452ba9379a2d8a8df32
- evidence_id: septin-nucleoid-agent-gene-ABF2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AABF2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Fresh response independently read for this successor. Complete current
    UniProt JSON result array and returned entry genes; query conditions in exact
    source URL
  accessed_at: '2026-11-03T23:18:46.044837Z'
  support: context_only
  summary: The exact reviewed ABF2 query at taxon559292 returns one entry Q02486 with
    matching primary ABF2 gene. This is the current bounded query, not reconstruction
    of the historical retrieval.
  snapshot_sha256: 2f1a4b7da1f69f1aa503aab21b8943f00b277576ba864fdae142ec1699d7402b
  search_scope: UniProt REST exact query as encoded in the reference, size500, all
    statuses for HLP; reviewed only for ABF2; no date filter; complete returned result
    array and suggestions distinguished from results. Access 2026-11-03T23:18:46.044837Z.
- evidence_id: septin-nucleoid-agent-family-IPR009071
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009071/
  locator: Fresh response independently read for this successor. Native type/name,
    complete description and integrated signatures
  accessed_at: '2026-11-03T23:18:46.084720Z'
  support: supports
  summary: IPR009071 is a High mobility group box domain, present in diverse nuclear
    and other proteins as well as Abf2. It is not an exact localized mitochondrial
    HMG-box protein family.
  snapshot_sha256: 624ec9d277aca01da75e1ab484d4c58cac553a9e08e3f045a2297c3554e16eaa
- evidence_id: septin-nucleoid-agent-family-IPR051965
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051965/
  locator: Fresh response independently read for this successor. Native type/name/description,
    LLM flags and Q02486 cross-reference context
  accessed_at: '2026-11-03T23:18:46.087596Z'
  support: context_only
  summary: Native metadata identifies a broad family named Chromatin Regulation and
    Neuronal Gene Expression, linked by Q02486. Its narrative is explicitly unchecked
    LLM-generated; that prose is not accepted as biological evidence or an exact localized
    mitochondrial HMG-class mapping.
  snapshot_sha256: e382a831709c9be2575382b010ab2aa7e3bf6c1764a7b0953adb68c04f01d119
- evidence_id: septin-nucleoid-agent-SL-0140
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0140.json
  locator: Fresh response independently read for this successor. Complete native location
    name/definition/synonyms/GO and part-of hierarchy
  accessed_at: '2026-11-03T23:18:46.634771Z'
  support: supports
  summary: UniProt SL0140 identifies Plastid nucleoid, maps GO0042646, supplies Plastidic
    nucleoid as a synonym and places it under Plastid stroma SL0215/GO0009532. Its
    definition describes a non-membrane-bounded chromatin-dense plastid pseudocompartment.
  snapshot_sha256: 2eb64592c08fa0a3e2307f71f82548129b34380ec0cfbe398e61269e09dc42e6
- evidence_id: septin-nucleoid-agent-tax33090
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Fresh response independently read for this successor. Complete native taxId/scientificName/rank/lineage
    and names
  accessed_at: '2026-11-03T23:18:46.206127Z'
  support: supports
  summary: ENA 33090 identifies Viridiplantae, rank kingdom. This verifies this named
    taxon only; it does not measure prevalence or identify a different experimental
    strain.
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
- evidence_id: septin-PMC10719067-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10719067.1/PMC10719067.1.xml
  locator: Fresh genuine SECONDARY review JATS; complete sec1 with Fig1/2 captions
    and Table1, sec8 including both subsections, sec10. Other sections, pixels and
    supplements not read.
  summary: Amodeo2023 explicitly centers T.brucei. It supports interlocked mini/maxicircle
    organization, conditional KAP contributions and TAC/basal-body segregation context.
    Models and unknown exact basic-protein localization/compaction are distinguished
    from direct experiments; no universal KAP repertoire or new measured prevalence
    is inferred.
  accessed_at: '2026-11-03T23:19:29.524369Z'
  support: supports
  snapshot_sha256: d7fb06d4ac80d46798f19cce168079a41178926b04d7fb5a0e7816082386f26c
- evidence_id: septin-PMC6868439-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6868439.1/PMC6868439.1.xml
  locator: Fresh genuine primary JATS; complete Methods SEC2-1 with Table1, Results
    SEC3-1 and SEC3-2 including Fig1 caption. Other Results/Methods, pixels and supplements
    not read.
  summary: Cooper2019 uses EATRO1125 AnTat1.1 90:13-derived cell lines and distinguishes391
    sequence classes from thousands of minicircle copies. Read-depth estimates yield
    about30 maxicircles and about6000 minicircles for an unreplicated network; neither391
    classes nor population averages are universal per-organelle stoichiometry.
  accessed_at: '2026-11-03T23:19:29.613621Z'
  support: supports
  snapshot_sha256: 06fc52d8fec60a36aa06e01a754d93ea719c0b39341e994a634b85bfebab2cdd
- evidence_id: septin-PMC5683618-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5683618.1/PMC5683618.1.xml
  locator: Fresh genuine primary JATS; complete Introduction sec001, cell culture
    sec004, Results sec013 and sec016 with Fig1/3 captions. Other sections/pixels/supplements
    not read.
  summary: deSouza2017 surveys lineage-variable KAP repertoires and tests Angomonas/Strigomonas
    wild-type/aposymbiotic strains. KAP1/2 are not universal; KAP2/3 cluster together.
    KAP4 overlaps kDNA, whereas aKAP23 does not coincide with DAPI and may occupy
    the kinetoflagellar zone. The curated DNA-bound compacting cohort is not every
    protein ever called KAP, nor a complete T.brucei KAP1–4 inventory.
  accessed_at: '2026-11-03T23:19:29.521129Z'
  support: supports
  snapshot_sha256: 8c9871c8a8a2fd63de9065b41954300c28168e304da4bb714e9d74f9692cd9ac
- evidence_id: septin-kucej2008-xmlhtml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5728373/?report=xml
  locator: Genuine recovered PMC HTML; complete Introduction S1, all Results S3–S6,
    Discussion S7, Methods S9–S13 and Fig1–6 captions. No pixels, supplementary tables/data
    or independent assay reanalysis.
  summary: Kucej2008 crosslinks isolated mitochondria in organello and samples about70%
    of an intronless genome; its own in vivo interpretation is not intact-live-cell
    ChIP. Abf2 binds most mtDNA with GC-rich preference; glucose/glycerol differences
    alter DNA:Abf2 ratio and nuclease sensitivity, while Hsp60/Ilv5 recruitment is
    condition-dependent. MCC109, BY4741 and W303-1B contexts are not silently relabeled
    as the S288C protein-reference example.
  accessed_at: '2026-11-03T23:20:21.357340Z'
  support: supports
  snapshot_sha256: 26cec5be6716c8a1dd47e217da05930ea1099975706251660d330e7a05fe43e9
- evidence_id: septin-sia2009-xmlhtml
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2621183/?report=xml
  locator: Genuine recovered PMC HTML; complete short scientific main body through
    conclusion, Table1/footnote, Fig1/2 captions. No figure pixels or unlinked supplementary
    strain ancestry.
  summary: Sia2009 shows increased frameshift/microsatellite instability and direct-repeat
    deletion after ABF2 loss, not an increased point-mutation rate. Respiratory selection
    permits retained mtDNA while fermentative growth favors loss. These genome-stability
    effects do not establish unconditional nucleoid formation necessity.
  accessed_at: '2026-11-03T23:20:21.286496Z'
  support: supports
  snapshot_sha256: 0573097c6e11e031b15238fa0b595e8725dd92252db5c89b289b061387cb12e8
- evidence_id: septin-gluenz2011-canonical
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3067821/
  locator: Genuine recovered canonical PMC HTML; complete Methods sec2/4 and Results
    sec7/8 with Fig1/2 captions. No figure pixels, other sections or supplements.
  summary: Gluenz2011 uses procyclic T.brucei LISTER427/TREU927/29-13 assay strains,
    serial thin-section EM and3D reconstructions. Five duplication stages link kDNA
    morphology to basal-body/flagellar-pocket organization. The declared canonical
    species example is supported without extending these measurements to every kinetoplastid
    architecture.
  accessed_at: '2026-11-03T23:20:21.326846Z'
  support: supports
  snapshot_sha256: 5cdd66656955825e47afb7cf6258f1fda1cdb0661e5228b542e5e93fc14464ac
- evidence_id: septin-access-initial-sandbox-failure-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/initial-sandbox-failure-receipts.json
  locator: Actual retrieval receipt packet and response hashes; access context only
  summary: Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404
    and four EuropePMC XML500 responses do not support or refute scientific claims.
    Separate successful genuine bodies above were inspected. Ogbadoyi genuine body
    was fetched but only its complete primary abstract was assessed; no body-read
    claim.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: context_only
  snapshot_sha256: 157f1e5b36105894127e82a319435afe48b0262b7b8cdb195b2034ac830dcf31
- evidence_id: septin-access-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/source-receipts.json
  locator: Actual retrieval receipt packet and response hashes; access context only
  summary: Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404
    and four EuropePMC XML500 responses do not support or refute scientific claims.
    Separate successful genuine bodies above were inspected. Ogbadoyi genuine body
    was fetched but only its complete primary abstract was assessed; no body-read
    claim.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: context_only
  snapshot_sha256: 5b2c1eb26fd265d982bb555a57086250e2b13e3c528a5af6beaa43a92ce2627f
- evidence_id: septin-access-body-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/body-receipts.json
  locator: Actual retrieval receipt packet and response hashes; access context only
  summary: Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404
    and four EuropePMC XML500 responses do not support or refute scientific claims.
    Separate successful genuine bodies above were inspected. Ogbadoyi genuine body
    was fetched but only its complete primary abstract was assessed; no body-read
    claim.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: context_only
  snapshot_sha256: 740d0d0f54869bde294bd1a7dceebb6c52d1c8e17ed66c234f0cf1898aba2835
- evidence_id: septin-access-more-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/more-receipts.json
  locator: Actual retrieval receipt packet and response hashes; access context only
  summary: Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404
    and four EuropePMC XML500 responses do not support or refute scientific claims.
    Separate successful genuine bodies above were inspected. Ogbadoyi genuine body
    was fetched but only its complete primary abstract was assessed; no body-read
    claim.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: context_only
  snapshot_sha256: 26e9a02f157265d62038c7d7a59379b595fd5019d60354b07e7081b5e8388f2f
- evidence_id: septin-access-canonical-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/canonical-receipts.json
  locator: Actual retrieval receipt packet and response hashes; access context only
  summary: Initial sandbox DNS failures, six HTTP200 anti-bot pages, four S3 XML404
    and four EuropePMC XML500 responses do not support or refute scientific claims.
    Separate successful genuine bodies above were inspected. Ogbadoyi genuine body
    was fetched but only its complete primary abstract was assessed; no body-read
    claim.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: context_only
  snapshot_sha256: 264493c000c560714d2a3d06a2f3f2293afd2a4c728bdf34361dc6b44b321fbd
- evidence_id: septin-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Entire fresh official organism/dataset response; all rows and arrays
  summary: The current catalogue has no matching Chlamydomonas/green-plant, Saccharomyces
    or kinetoplastid host. All four records positively assert molecular/pathway biology,
    so applicability is checked; no unrelated bacterial proxy or downstream unmatched
    gene/module query is justified. Noncoverage is not biological absence.
  accessed_at: '2026-11-03T23:18:45.835099Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: GET official https://imodulondb.org/api/datasets; all20 organism rows,28
    organism-dataset pairs and22 unique dataset keys, no query filters/truncation;
    accessed 2026-11-03T23:18:45.835099Z.
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual retained historical runner attempt; no new invocation
  summary: 2026-11-03T00:49:00.848907Z–00:49:00.863225Z exit1 PermissionError reading
    pyvenv.cfg. Current direct official catalogue fallback is separate, not a new
    successful adapter run.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-generic-nucleoid-context
  kind: record_content
  reference: data/structures/nucleoid/nucleoid.yaml
  locator: Complete already-frozen cohort neighbor, used only for identity boundary
  summary: The generic maintained neighbor has broader GO0009295 identity with bacterial
    wording; that separate target is reviewed by another agent. Correct organellar
    child ontology links are assessed directly against GO. No neighbor finding, verdict
    or terminal disposition is inferred.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08
- evidence_id: septin-record-chloroplast_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/chloroplast_nucleoid.yaml
  locator: Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba
  summary: All scientific fields, sources, discussions, history and graph edges read.
    Record remains byte-identical to the original frozen target; independent current
    source checks performed, not merely a hash refresh. 0 protein examples/1 typed
    protein nodes; no maintained images.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25
- evidence_id: septin-original-chloroplast_nucleoid
  kind: prior_review
  reference: reviews/structured/20261022T042548Z-chloroplast-nucleoid-audit/review.yaml
  locator: Complete original YAML/Markdown, science/checks/verdict/actions/limitations
    and frozen input manifest
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its current-input identity is unchanged; original dated checks remain
    historical, not newly executed. Unsupported formal adapter exclusion is separately
    corrected in successor only.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: 70eab0f88e1ab71c70c4d72b432d3790a42319711f15169d9c2840d9e835006b
- evidence_id: septin-original-validation-chloroplast_nucleoid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json
  locator: Actual native validate/render and complete frozen historical-input check
  summary: Both commands exit0, original Markdown byte-exact, all16 original input
    hashes match the frozen source; current target matches original target. Native
    validity is not a scientific verdict.
  accessed_at: '2026-11-03T23:18:59.803014Z'
  support: supports
  snapshot_sha256: 2b4a7c5651a5c7806bc98822342b2bb9b721ff246fb21a7fcc8687099b1ab7b2
- evidence_id: septin-native-chloroplast_nucleoid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-verify-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported
    HLP token is not refuted by a bounded zero UniProt exact-name result.
  accessed_at: '2026-11-03T23:17:25.808825Z'
  support: supports
  snapshot_sha256: 00f948e6f4467cc325f964b045ba1316a725056d2ff17d27f20ae6b7b5e71422
- evidence_id: septin-native-chloroplast_nucleoid-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-causal-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-causal.log
    SHA256 1ad288cda6d8baaea929dfe9142bcf9ba8b7e4f320f7678340a454924e46c0b8
  summary: Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported
    HLP token is not refuted by a bounded zero UniProt exact-name result.
  accessed_at: '2026-11-03T23:17:26.211023Z'
  support: supports
  snapshot_sha256: 60f3e937d4198b0f2542f12bf03c1980871ad8ee09a81e382cbd21738bb61a41
- evidence_id: septin-record-kinetoplast
  kind: record_content
  reference: data/structures/nucleoid/kinetoplast.yaml
  locator: Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba
  summary: All scientific fields, sources, discussions, history and graph edges read.
    Record remains byte-identical to the original frozen target; independent current
    source checks performed, not merely a hash refresh. 0 protein examples/1 typed
    protein nodes; no maintained images.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: e40505c18375c267ebabc32d2b4bd7101c7da9b7bdf1b1549469b8b4a7292f7a
- evidence_id: septin-original-kinetoplast
  kind: prior_review
  reference: reviews/structured/20261022T042549Z-kinetoplast-audit/review.yaml
  locator: Complete original YAML/Markdown, science/checks/verdict/actions/limitations
    and frozen input manifest
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its current-input identity is unchanged; original dated checks remain
    historical, not newly executed. Unsupported formal adapter exclusion is separately
    corrected in successor only.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: f16cbd9d79a441e32dc7db63392a69298f0a3a4888a2d0c70435a9ff05e6a169
- evidence_id: septin-original-validation-kinetoplast
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json
  locator: Actual native validate/render and complete frozen historical-input check
  summary: Both commands exit0, original Markdown byte-exact, all14 original input
    hashes match the frozen source; current target matches original target. Native
    validity is not a scientific verdict.
  accessed_at: '2026-11-03T23:19:01.110912Z'
  support: supports
  snapshot_sha256: 2b4a7c5651a5c7806bc98822342b2bb9b721ff246fb21a7fcc8687099b1ab7b2
- evidence_id: septin-native-kinetoplast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-verify-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative
    literature names, not a verified set of four universal T.brucei accession identities.
  accessed_at: '2026-11-03T23:17:26.616907Z'
  support: supports
  snapshot_sha256: f0c837aafe0c081160fdf7af17e0a7e72fc81539479abf6afecf5a1ee5cae5b2
- evidence_id: septin-native-kinetoplast-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-causal-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-causal.log
    SHA256 8676810ab064da164f9b59c268811a6c76f4dbc7dc0297ac3e4089301cd09f4d
  summary: Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative
    literature names, not a verified set of four universal T.brucei accession identities.
  accessed_at: '2026-11-03T23:17:27.018292Z'
  support: supports
  snapshot_sha256: bcbf35a33e379f58bfa66d3a3f8ea68db6e6a2ce4afeed4c06978e5e63948dd6
- evidence_id: septin-record-mitochondrial_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/mitochondrial_nucleoid.yaml
  locator: Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba
  summary: All scientific fields, sources, discussions, history and graph edges read.
    Record remains byte-identical to the original frozen target; independent current
    source checks performed, not merely a hash refresh. 1 protein examples/1 typed
    protein nodes; no maintained images.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d
- evidence_id: septin-original-mitochondrial_nucleoid
  kind: prior_review
  reference: reviews/structured/20261022T042550Z-mitochondrial-nucleoid-audit/review.yaml
  locator: Complete original YAML/Markdown, science/checks/verdict/actions/limitations
    and frozen input manifest
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its current-input identity is unchanged; original dated checks remain
    historical, not newly executed. Unsupported formal adapter exclusion is separately
    corrected in successor only.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: cf1f08188e6e2f40c0ce44d7683a27f887bef23ef85f6e141eda37c630d9a82b
- evidence_id: septin-original-validation-mitochondrial_nucleoid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json
  locator: Actual native validate/render and complete frozen historical-input check
  summary: Both commands exit0, original Markdown byte-exact, all16 original input
    hashes match the frozen source; current target matches original target. Native
    validity is not a scientific verdict.
  accessed_at: '2026-11-03T23:19:02.435392Z'
  support: supports
  snapshot_sha256: 2b4a7c5651a5c7806bc98822342b2bb9b721ff246fb21a7fcc8687099b1ab7b2
- evidence_id: septin-native-mitochondrial_nucleoid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-verify-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node.
    Identity and coverage do not turn every source assay into S288C or prove formation
    necessity.
  accessed_at: '2026-11-03T23:17:28.096580Z'
  support: supports
  snapshot_sha256: 88d91cee49a5cdf8061937002323b78f8d9e3cc49d7031d43aea97d040c0682f
- evidence_id: septin-native-mitochondrial_nucleoid-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-causal-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-causal.log
    SHA256 f99e2411914f5015315ed9c67ad81727e914466b91175451cb0ca9ca924f37f8
  summary: One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node.
    Identity and coverage do not turn every source assay into S288C or prove formation
    necessity.
  accessed_at: '2026-11-03T23:17:28.501894Z'
  support: supports
  snapshot_sha256: 9fcc12f1523f884d6307673fd3838ea76b7d02c47d402f6b2a26392d432e3491
- evidence_id: septin-record-plastid_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/plastid_nucleoid.yaml
  locator: Complete current record at 7b6cd533340948100b7b23d8ab4e659702d9feba
  summary: All scientific fields, sources, discussions, history and graph edges read.
    Record remains byte-identical to the original frozen target; independent current
    source checks performed, not merely a hash refresh. 0 protein examples/0 typed
    protein nodes; no maintained images.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842
- evidence_id: septin-original-plastid_nucleoid
  kind: prior_review
  reference: reviews/structured/20261022T042551Z-plastid-nucleoid-audit/review.yaml
  locator: Complete original YAML/Markdown, science/checks/verdict/actions/limitations
    and frozen input manifest
  summary: Original qualified pass has no scientific findings or request-curation
    actions. Its current-input identity is unchanged; original dated checks remain
    historical, not newly executed. Unsupported formal adapter exclusion is separately
    corrected in successor only.
  accessed_at: '2026-11-03T23:23:45.229788Z'
  support: supports
  snapshot_sha256: bd68c472e18d9009c35dd640700ab9422f857eb37b29a79cc6b41d8e7a9146f8
- evidence_id: septin-original-validation-plastid_nucleoid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-septin/original-checks.json
  locator: Actual native validate/render and complete frozen historical-input check
  summary: Both commands exit0, original Markdown byte-exact, all15 original input
    hashes match the frozen source; current target matches original target. Native
    validity is not a scientific verdict.
  accessed_at: '2026-11-03T23:19:03.751393Z'
  support: supports
  snapshot_sha256: 2b4a7c5651a5c7806bc98822342b2bb9b721ff246fb21a7fcc8687099b1ab7b2
- evidence_id: septin-native-plastid_nucleoid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-verify-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Zero examples and zero typed protein nodes; native success is empty inventory
    scope. HLP-containing narrative elsewhere still triggers applicability.
  accessed_at: '2026-11-03T23:17:30.679026Z'
  support: supports
  snapshot_sha256: ce5782517b4b049acacdf3d3ad9cb5b863feabb0db906e403905676bc820f6b0
- evidence_id: septin-native-plastid_nucleoid-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-causal-receipt.json
  locator: Actual command/exit/timestamp/head and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Zero examples and zero typed protein nodes; native success is empty inventory
    scope. HLP-containing narrative elsewhere still triggers applicability.
  accessed_at: '2026-11-03T23:17:31.082068Z'
  support: supports
  snapshot_sha256: 17629eb9cfd504a555d32438db125f364427b41c33f7752e7446b03889a3332f
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks and full review skill reread; previously
    read remaining rules byte-identical
  summary: Genes, proteins, regulators and pathways trigger applicability; no expression-module
    assertion alone does not establish N/A.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Previously read unchanged native scientific checklist
  summary: Identity, source scope, component necessity and optional inventory are
    separate questions.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Previously read unchanged component, CausalNode and necessity contracts
  summary: Protein families and complexes may be GENE_OR_PROTEIN. Functional requirement
    differs from formation necessity; optional examples are not mandatory.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-history-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Previously read unchanged append-only discussion/history rules
  summary: Preserve dated historical rationale and current scientific uncertainty;
    individual examples do not require broad family grounding or retroactive history
    rewriting.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/nucleoid/nucleoid.yaml
  locator: Entire maintained record at 7b6cd533340948100b7b23d8ab4e659702d9feba including
    all sources, components, examples, graph, discussion and history
  summary: Full unchanged target independently reassessed; no record mutation.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08
- evidence_id: plaque-original-4
  kind: prior_review
  reference: reviews/structured/20261022T042551Z-nucleoid-audit/review.yaml
  locator: Complete exact original YAML and derived Markdown, checks, evidence, findings,
    actions and limitations
  summary: Nucleoid has one inherited major identity finding; glucan synthase and
    ACF have no findings. Nucleoid/ACF formal and glucan prose-only exclusions are
    reassessed. Historical source bytes and native rendering checked.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: 41cb6682369ea9da295f9f13500d8dd7f60c75971bbde3a7160f2562ca90b600
- evidence_id: plaque-current-6
  kind: record_content
  reference: data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
  locator: Entire maintained record at 7b6cd533340948100b7b23d8ab4e659702d9feba including
    all sources, components, examples, graph, discussion and history
  summary: Full unchanged target independently reassessed; no record mutation.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: 3dedbfa89047d1949a9d4691dcb873546c76dcd836c17494c43160462b9626bc
- evidence_id: plaque-original-6
  kind: prior_review
  reference: reviews/structured/20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit/review.yaml
  locator: Complete exact original YAML and derived Markdown, checks, evidence, findings,
    actions and limitations
  summary: Nucleoid has one inherited major identity finding; glucan synthase and
    ACF have no findings. Nucleoid/ACF formal and glucan prose-only exclusions are
    reassessed. Historical source bytes and native rendering checked.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: e881a8058d08a36997b16b19b298152d5c347df67d579851347daa78433a74f7
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/other/acf_complex.yaml
  locator: Entire maintained record at 7b6cd533340948100b7b23d8ab4e659702d9feba including
    all sources, components, examples, graph, discussion and history
  summary: Full unchanged target independently reassessed; no record mutation.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261022T042554Z-acf-complex-audit/review.yaml
  locator: Complete exact original YAML and derived Markdown, checks, evidence, findings,
    actions and limitations
  summary: Nucleoid has one inherited major identity finding; glucan synthase and
    ACF have no findings. Nucleoid/ACF formal and glucan prose-only exclusions are
    reassessed. Historical source bytes and native rendering checked.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: a45c3dabfbef02e1ffe4558429ff9b775b6564ada70e2a30617ab81ee81388fc
- evidence_id: plaque-context-chloroplast_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/chloroplast_nucleoid.yaml
  locator: Identity, definition, parent_structures and part_of only
  summary: 'Maintained organellar identities provide bounded local context: mitochondrial
    and plastid nucleoids use generic GO0009295 parent; chloroplast uses plastid nucleoid
    parent.'
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25
- evidence_id: plaque-context-mitochondrial_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/mitochondrial_nucleoid.yaml
  locator: Identity, definition, parent_structures and part_of only
  summary: 'Maintained organellar identities provide bounded local context: mitochondrial
    and plastid nucleoids use generic GO0009295 parent; chloroplast uses plastid nucleoid
    parent.'
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d
- evidence_id: plaque-context-plastid_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/plastid_nucleoid.yaml
  locator: Identity, definition, parent_structures and part_of only
  summary: 'Maintained organellar identities provide bounded local context: mitochondrial
    and plastid nucleoids use generic GO0009295 parent; chloroplast uses plastid nucleoid
    parent.'
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: context_only
  snapshot_sha256: 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842
- evidence_id: plaque-go-terms
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009295,GO:0043590,GO:0042644,GO:0042645,GO:0042646,GO:0051276,GO:0000148,GO:0003843,GO:0009277,GO:0071970,GO:0016590,GO:0031010,GO:0006338
  locator: Fresh complete thirteen native GO identities, definitions, synonyms, active
    status and typed child entries
  summary: Generic GO0009295 explicitly spans virus, bacterial cell, mitochondrion
    and chloroplast; GO0043590 is bacterial nucleoid. GO0009295 directly lists mitochondrial/plastid/bacterial
    is_a children. Exact glucan synthase and ACF definitions and ACF ISWI-type parent
    agree; retained process/activity/wall identities agree.
  accessed_at: '2026-11-03T23:18:47.797847Z'
  support: supports
  snapshot_sha256: fbad1b1f2d76428bb604c3698454fc1db717f4f94e9adec2c6e719f3ca63cdf1
- evidence_id: plaque-sl-0187
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0187.json
  locator: Fresh complete native localization identity/definition
  summary: SL0187 is nucleoid, supporting localization cross-reference rather than
    narrowing generic GO identity to the chosen bacterial example.
  accessed_at: '2026-11-03T23:18:47.798836Z'
  support: supports
  snapshot_sha256: f012b1f206fcd611ddbc672bf2ffd28df17e2ca416d836d1bd8516a41eb0a999
- evidence_id: plaque-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete fresh ENA identity/rank/lineage
  summary: Domain, species and reference-strain identities verified separately. K-12
    examples do not mean all experiments use MG1655; S288C accessions do not make
    W303-derived experiments S288C.
  accessed_at: '2026-11-03T23:18:47.799769Z'
  support: supports
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: plaque-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete fresh ENA identity/rank/lineage
  summary: Domain, species and reference-strain identities verified separately. K-12
    examples do not mean all experiments use MG1655; S288C accessions do not make
    W303-derived experiments S288C.
  accessed_at: '2026-11-03T23:18:47.800919Z'
  support: supports
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: plaque-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete fresh ENA identity/rank/lineage
  summary: Domain, species and reference-strain identities verified separately. K-12
    examples do not mean all experiments use MG1655; S288C accessions do not make
    W303-derived experiments S288C.
  accessed_at: '2026-11-03T23:18:47.801897Z'
  support: supports
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: plaque-tax-511145
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/511145
  locator: Complete fresh ENA identity/rank/lineage
  summary: Domain, species and reference-strain identities verified separately. K-12
    examples do not mean all experiments use MG1655; S288C accessions do not make
    W303-derived experiments S288C.
  accessed_at: '2026-11-03T23:18:47.802767Z'
  support: supports
  snapshot_sha256: e3a402d3d5b5d1b11deda22f50922b38962f0bb955b7fa8edfea0a937277199e
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete fresh ENA identity/rank/lineage
  summary: Domain, species and reference-strain identities verified separately. K-12
    examples do not mean all experiments use MG1655; S288C accessions do not make
    W303-derived experiments S288C.
  accessed_at: '2026-11-03T23:18:47.803729Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete fresh ENA identity/rank/lineage
  summary: Domain, species and reference-strain identities verified separately. K-12
    examples do not mean all experiments use MG1655; S288C accessions do not make
    W303-derived experiments S288C.
  accessed_at: '2026-11-03T23:18:47.804793Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-dillon2010-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nrmicro2261&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    secondary review
  summary: Dillon SC, Dorman CJ. (2010), Bacterial nucleoid-associated proteins, nucleoid
    structure and gene expression. Native MED20140026 and DOI agree. Entire deposited
    abstract read; no unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.688888Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.688888Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: dd4338efc3a097fd20fc79a4dc161858783d7b0a5d985e6c2e39faeee69f7562
- evidence_id: plaque-verma2019-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1371/journal.pgen.1008456&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    secondary review
  summary: Verma SC, Qian Z, Adhya SL. (2019), Architecture of the Escherichia coli
    nucleoid. Native MED31830036 and DOI agree. Entire deposited abstract read; no
    unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.692509Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.692509Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 7ce0e45115a010b18383a855c6dccf46cd8de08102fb3c681128abcf2caec14c
- evidence_id: plaque-douglas1994-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.91.26.12907&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Douglas CM, Foor F, Marrinan JA, Morin N, Nielsen JB, Dahl AM, Mazur P,
    Baginsky W, Li W, el-Sherbeini M. (1994), The Saccharomyces cerevisiae FKS1 (ETG1)
    gene encodes an integral membrane protein which is a subunit of 1,3-beta-D-glucan
    synthase. Native MED7528927 and DOI agree. Entire deposited abstract read; no
    unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.815316Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.815316Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: edc9ae786bad4ae247b237893e8481c7a8586f169ca615b5f7c3febd294b3bf6
- evidence_id: plaque-mazur1995-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/MCB.15.10.5671&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Mazur P, Morin N, Baginsky W, el-Sherbeini M, Clemas JA, Nielsen JB, Foor
    F. (1995), Differential expression and function of two homologous subunits of
    yeast 1,3-beta-D-glucan synthase. Native MED7565718 and DOI agree. Entire deposited
    abstract read; no unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.923562Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.923562Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 34527c4a0e0f9a8f34e54ce7ac8e2fa61562e551ce259b43aff88789ce56b778
- evidence_id: plaque-qadota1996-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1126/science.272.5259.279&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Qadota H, Python CP, Inoue SB, Arisawa M, Anraku Y, Zheng Y, Watanabe T,
    Levin DE, Ohya Y. (1996), Identification of yeast Rho1p GTPase as a regulatory
    subunit of 1,3-beta-glucan synthase. Native MED8602515 and DOI agree. Entire deposited
    abstract read; no unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.934317Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.934317Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: c46450edb5269c07c8b49b28322c5fcc72dd8a3a8e07bb16ac563291521a43bb
- evidence_id: plaque-mazur1996-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074/jbc.271.24.14604&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Mazur P, Baginsky W. (1996), In vitro activity of 1,3-beta-D-glucan synthase
    requires the GTP-binding protein Rho1. Native MED8662910 and DOI agree. Entire
    deposited abstract read; no unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:54.049245Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:54.049245Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 8f43f54f0b31f3d39f5c0770ef1065a253a8424a3b1aaaf0e40eb6361a3e3fee
- evidence_id: plaque-gelbart2001-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/MCB.21.6.2098-2106.2001&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: 'Gelbart ME, Rechsteiner T, Richmond TJ, Tsukiyama T. (2001), Interactions
    of Isw2 chromatin remodeling complex with nucleosomal arrays: analyses using recombinant
    yeast histones and immobilized templates. Native MED11238944 and DOI agree. Entire
    deposited abstract read; no unread protocol, figure or supplement certified.'
  accessed_at: '2026-11-03T23:18:54.317689Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:54.317689Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 34e05a64d252a84ab227e12a5f03b5fc24ea5ee25f2dbc58fec05353878545df
- evidence_id: plaque-mcconnell2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128/MCB.24.7.2605-2613.2004&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: McConnell AD, Gelbart ME, Tsukiyama T. (2004), Histone fold protein Dls1p
    is required for Isw2-dependent chromatin remodeling in vivo. Native MED15024052
    and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement
    certified.
  accessed_at: '2026-11-03T23:18:54.371676Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:54.371676Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: a163db090f8737da15b4595976a2f69c4aa7e16d64755329ed88c1550d3e15e2
- evidence_id: plaque-pmid-21903814
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21903814%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Wang W, Li GW, Chen C, Xie XS, Zhuang X. (2011), Chromosome organization
    by a nucleoid-associated protein in live bacteria. Native MED21903814 and DOI
    agree. Entire deposited abstract read; no unread protocol, figure or supplement
    certified.
  accessed_at: '2026-11-03T23:18:52.415230Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:52.415230Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 918c985b4e70dac21c4cdd9dbd68d90fe4c33f40a04a65f7b70aa9cfdd3dc73f
- evidence_id: plaque-pmid-333393
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:333393%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Varshavsky AJ, Nedospasov SA, Bakayev VV, Bakayeva TG, Georgiev GP. (1977),
    Histone-like proteins in the purified Escherichia coli deoxyribonucleoprotein.
    Native MED333393 and DOI agree. Entire deposited abstract read; no unread protocol,
    figure or supplement certified.
  accessed_at: '2026-11-03T23:18:52.519026Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:52.519026Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: d6feac7ea49acf534a38609974b25ac5797e985af620c0ab79465a399fb0ba1c
- evidence_id: plaque-pmid-11856368
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11856368%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Utsugi T, Minemura M, Hirata A, Abe M, Watanabe D, Ohya Y. (2002), Movement
    of yeast 1,3-beta-glucan synthase is essential for uniform cell wall synthesis.
    Native MED11856368 and DOI agree. Entire deposited abstract read; no unread protocol,
    figure or supplement certified.
  accessed_at: '2026-11-03T23:18:52.668040Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:52.668040Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: e324952f934166e3df6894be989145e34dea614fa811316c50abe45786ebfe02
- evidence_id: plaque-pmid-12185837
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12185837%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Dijkgraaf GJ, Abe M, Ohya Y, Bussey H. (2002), Mutations in Fks1p affect
    the cell wall content of beta-1,3- and beta-1,6-glucan in Saccharomyces cerevisiae.
    Native MED12185837 and DOI agree. Entire deposited abstract read; no unread protocol,
    figure or supplement certified.
  accessed_at: '2026-11-03T23:18:52.687546Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:52.687546Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 5430b8ac80f75302bbf3f7ee1df8bce0920f9ed42bac940eff0e0e9600cb26d5
- evidence_id: plaque-pmid-14576278
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14576278%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Sickmann A, Reinders J, Wagner Y, Joppich C, Zahedi R, Meyer HE, Schönfisch
    B, Perschil I, Chacinska A, Guiard B, Rehling P, Pfanner N, Meisinger C. (2003),
    The proteome of Saccharomyces cerevisiae mitochondria. Native MED14576278 and
    DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement
    certified.
  accessed_at: '2026-11-03T23:18:52.808648Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:52.808648Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 9f13b62fcf0bcf1db88bdaf447cd091306f40f6fe24b540b5beb745b4cb62c1a
- evidence_id: plaque-pmid-7565718
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7565718%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Mazur P, Morin N, Baginsky W, el-Sherbeini M, Clemas JA, Nielsen JB, Foor
    F. (1995), Differential expression and function of two homologous subunits of
    yeast 1,3-beta-D-glucan synthase. Native MED7565718 and DOI agree. Entire deposited
    abstract read; no unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.050765Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.050765Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: d9310433cb35ec6db916dfc1f10dff1bb38514afd5e2f7ab2b75f92b0ab0c5f0
- evidence_id: plaque-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14562095%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea
    EK. (2003), Global analysis of protein localization in budding yeast. Native MED14562095
    and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement
    certified.
  accessed_at: '2026-11-03T23:18:53.165501Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.165501Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 0ace0edb94d472ba05450e01ed40fea07bff460eb49ed7f7a3dac5817fdb7ae5
- evidence_id: plaque-pmid-11238944
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11238944%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: 'Gelbart ME, Rechsteiner T, Richmond TJ, Tsukiyama T. (2001), Interactions
    of Isw2 chromatin remodeling complex with nucleosomal arrays: analyses using recombinant
    yeast histones and immobilized templates. Native MED11238944 and DOI agree. Entire
    deposited abstract read; no unread protocol, figure or supplement certified.'
  accessed_at: '2026-11-03T23:18:53.308481Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.308481Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 7c0591f7c7cb93f8b32c55f0c220b0732045d7d5e8794e2f9487faa22057d86a
- evidence_id: plaque-pmid-15024052
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15024052%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: McConnell AD, Gelbart ME, Tsukiyama T. (2004), Histone fold protein Dls1p
    is required for Isw2-dependent chromatin remodeling in vivo. Native MED15024052
    and DOI agree. Entire deposited abstract read; no unread protocol, figure or supplement
    certified.
  accessed_at: '2026-11-03T23:18:53.320310Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.320310Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 6c3e6c094ba6e900295670a633fc13b481c8fe443fbf3e9880f25ec92c8c16ce
- evidence_id: plaque-pmid-7983071
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:7983071%20AND%20SRC:MED&format=json&resultType=core&pageSize=1
  locator: Complete returned exact bibliographic identity and deposited abstract;
    primary abstract tier
  summary: Mol PC, Park HM, Mullins JT, Cabib E. (1994), A GTP-binding protein regulates
    the activity of (1-->3)-beta-glucan synthase, an enzyme directly involved in yeast
    cell wall morphogenesis. Native MED7983071 and DOI agree. Entire deposited abstract
    read; no unread protocol, figure or supplement certified.
  accessed_at: '2026-11-03T23:18:53.433602Z'
  support: supports
  search_scope: EuropePMC exact DOI or MED identifier query encoded in URL at 2026-11-03T23:18:53.433602Z;
    pageSize1, first returned page, 1 total hits; complete returned identity/abstract
    inspected, body separately cited.
  snapshot_sha256: 3b68c00b2225b59186a2b7504bd0ec47f7b65e391e7869a07c9425d4a1270027
- evidence_id: plaque-verma2019-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6907758.1/PMC6907758.1.xml
  locator: Fresh genuine secondary JATS sec002 including HU/IHF/H-NS/Fis subsections/tables
    and text captions; sec010,014,015
  summary: Secondary multiscale E.coli synthesis supports heterogeneous NAP DNA-binding/bending/bridging
    and supercoiling compaction. Concentration, magnesium, growth phase and unproven
    in-vivo topological barriers remain explicit. No individual primary study behind
    every review claim independently recovered; no pixels.
  accessed_at: '2026-11-03T23:18:54.464208Z'
  support: supports
  snapshot_sha256: f0ac2a95634cffece5970d32302e4a843c46f9627f0478b63bc6d2233662b387
- evidence_id: plaque-wang2011-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3329943.1/PMC3329943.1.xml
  locator: Fresh genuine JATS complete main scientific text and in-text experimental
    details; no supplementary methods/TableS1 or figure pixels
  summary: Live E.coli fluorescent endogenous NAP fusions, early-log minimal-medium
    imaging, H-NS mutation/deletion and chromosome-conformation capture support heterogeneous
    NAP localization and H-NS-dependent chromosome organization. Main text distinguishes
    observed clusters from proposed organizing loops; no universal NAP-necessity or
    exact reference-strain equivalence.
  accessed_at: '2026-11-03T23:18:54.598284Z'
  support: supports
  snapshot_sha256: a32d98bd8b93eb622fcca97af2c2360333f01cdc78c022e2ca34d3544db24256
- evidence_id: plaque-gelbart2001-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC86823/
  locator: Fresh genuine PMC body sec2,sec6,sec14,sec15 including Fig4/5 text captions;
    no pixels/supplements
  summary: W1588-4C congenic W303-derived yeast, FLAG purification and separated/reconstituted
    Isw2/Itc1 support two-subunit biochemical association and efficient DNA/nucleosome
    binding, ATPase/remodeling. Monomer folding/purification and incomplete activity
    restoration remain caveats; activity necessity is not formation necessity.
  accessed_at: '2026-11-03T23:18:54.995842Z'
  support: supports
  snapshot_sha256: e93e2e0a2a308fcc998e489fa51cafa2e7cf3460e58cd6f5b5980d2dac475703
- evidence_id: plaque-mcconnell2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC371119/
  locator: Fresh genuine PMC body sec3 and sec9 including Fig1/2 text captions; no
    pixels/supplements
  summary: Independent purifications and immunodepletion identify Dpb4/Dls1 in four-subunit
    Isw2 and populations consistent with two-subunit Isw2/Itc1. Authors explicitly
    cannot rule out two-subunit material generated by tags/purification; native prevalence/exclusive
    stoichiometry not certified.
  accessed_at: '2026-11-03T23:18:55.001159Z'
  support: supports
  snapshot_sha256: fe11394ad2653941135898f59df3c9a3c07de73148fd9cac500176ebc659da6d
- evidence_id: plaque-verma2019-pmc-access
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6907758/
  locator: Actual retained response/readability only
  summary: HTTP200 challenge/frontend HTML, not scientific body or genes dataset;
    successful JATS/other direct endpoints are separately cited. No biological evidence
    inferred.
  accessed_at: '2026-11-03T23:18:54.427602Z'
  support: context_only
  snapshot_sha256: 43738b6fc3d19b59ef2772f5111efc47c5647d089bd0d1a8b0d63c0a016b181d
- evidence_id: plaque-wang2011-pmc-access
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3329943/
  locator: Actual retained response/readability only
  summary: HTTP200 challenge/frontend HTML, not scientific body or genes dataset;
    successful JATS/other direct endpoints are separately cited. No biological evidence
    inferred.
  accessed_at: '2026-11-03T23:18:54.544120Z'
  support: context_only
  snapshot_sha256: def39ba5306f9a409ab217b06024d453e054da2689b740e795829320b6fac95f
- evidence_id: plaque-douglas1994-pmc-access
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC45549/
  locator: Actual retained response/readability only
  summary: HTTP200 challenge/frontend HTML, not scientific body or genes dataset;
    successful JATS/other direct endpoints are separately cited. No biological evidence
    inferred.
  accessed_at: '2026-11-03T23:18:54.708820Z'
  support: context_only
  snapshot_sha256: f4dd83cd34c085f6cc1a1883f924853bc9b39cdd95bd669a668ed4400d4ee347
- evidence_id: plaque-mazur1995-pmc-access
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC230817/
  locator: Actual retained response/readability only
  summary: HTTP200 challenge/frontend HTML, not scientific body or genes dataset;
    successful JATS/other direct endpoints are separately cited. No biological evidence
    inferred.
  accessed_at: '2026-11-03T23:18:54.799731Z'
  support: context_only
  snapshot_sha256: a9ce9fcb2f5c1bb1ff07e404af5a4e53c7b5b7bb83d7aaad7a47bd179e47e2f8
- evidence_id: plaque-adapter-genes-access
  kind: authority
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/genes
  locator: Actual retained response/readability only
  summary: HTTP200 challenge/frontend HTML, not scientific body or genes dataset;
    successful JATS/other direct endpoints are separately cited. No biological evidence
    inferred.
  accessed_at: '2026-11-03T23:20:32.729581Z'
  support: context_only
  snapshot_sha256: 372db3e7392f2779f2d46aef5c4f7786399705355520de485f6c37ee92bf0478
- evidence_id: plaque-douglas1994-jats-access
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC45549.1/PMC45549.1.xml
  locator: Actual retained HTTP404 only
  summary: Guessed public JATS route unavailable; no body read from this response.
    Successful PMC or primary abstract evidence is separately bounded.
  accessed_at: '2026-11-03T23:18:54.735656Z'
  support: context_only
  snapshot_sha256: bc902507ccb375dd9cc251acae1ff1d9c944f57c29ebb3f94b589cbc27bc976c
- evidence_id: plaque-mazur1995-jats-access
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC230817.1/PMC230817.1.xml
  locator: Actual retained HTTP404 only
  summary: Guessed public JATS route unavailable; no body read from this response.
    Successful PMC or primary abstract evidence is separately bounded.
  accessed_at: '2026-11-03T23:18:54.897416Z'
  support: context_only
  snapshot_sha256: a40480345dae3a13c165218f93caa560800f3b5c0ccf1ae9e494cffc3ca2aa87
- evidence_id: plaque-gelbart2001-jats-access
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC86823.1/PMC86823.1.xml
  locator: Actual retained HTTP404 only
  summary: Guessed public JATS route unavailable; no body read from this response.
    Successful PMC or primary abstract evidence is separately bounded.
  accessed_at: '2026-11-03T23:18:55.000014Z'
  support: context_only
  snapshot_sha256: 984e98f95bd6fe3517564f3e2e3ffc49506ef61c9fd2ca72f166a2a6c4515808
- evidence_id: plaque-mcconnell2004-jats-access
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC371119.1/PMC371119.1.xml
  locator: Actual retained HTTP404 only
  summary: Guessed public JATS route unavailable; no body read from this response.
    Successful PMC or primary abstract evidence is separately bounded.
  accessed_at: '2026-11-03T23:18:55.028114Z'
  support: context_only
  snapshot_sha256: 169393760c5129e99b9b1ea4ab7bba7bb3cba19c8ea3eab93ee156aac10bff58
- evidence_id: plaque-up-P0ACF0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACF0.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0ACF0 is reviewed taxon83333 DNA-binding protein HU-alpha. Exact aliases
    and source annotations checked; annotation joins are not independently reproduced
    localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.408076Z'
  support: supports
  snapshot_sha256: 2c196a6263284294e56ac728414727fcb7f484114bea5a93676fc69cd18378e6
- evidence_id: plaque-up-P0ACF4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACF4.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0ACF4 is reviewed taxon83333 DNA-binding protein HU-beta. Exact aliases
    and source annotations checked; annotation joins are not independently reproduced
    localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.412768Z'
  support: supports
  snapshot_sha256: 0c491ed797820b6ef9cb677d80467eec7879f829b47f44076c40ce27d0b35f09
- evidence_id: plaque-up-P0A6X7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6X7.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0A6X7 is reviewed taxon83333 Integration host factor subunit alpha. Exact
    aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.417929Z'
  support: supports
  snapshot_sha256: 443ba5d81e02adf48c4e893a050fe589e232d4f74bf55891a91811f34d70dc09
- evidence_id: plaque-up-P0A6Y1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6Y1.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0A6Y1 is reviewed taxon83333 Integration host factor subunit beta. Exact
    aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.422814Z'
  support: supports
  snapshot_sha256: 00e7d54c17acfe2db9536cac8f82c66606733b43bb3d6b6a337b744198d6d2e1
- evidence_id: plaque-up-P0A6R3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6R3.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0A6R3 is reviewed taxon83333 DNA-binding protein Fis. Exact aliases and
    source annotations checked; annotation joins are not independently reproduced
    localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.425362Z'
  support: supports
  snapshot_sha256: 91fe66ce876b12a17652e63ad345bc4c7badeb7fbdd81ab24b7ff996069f21d9
- evidence_id: plaque-up-P0ACF8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACF8.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0ACF8 is reviewed taxon83333 DNA-binding protein H-NS. Exact aliases and
    source annotations checked; annotation joins are not independently reproduced
    localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.435932Z'
  support: supports
  snapshot_sha256: 69765685e6a74d1b208bbeb2ddd51204aa1be75b3b8b411efbe83252cd9523c8
- evidence_id: plaque-up-P0ABT2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABT2.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P0ABT2 is reviewed taxon83333 DNA protection during starvation protein.
    Exact aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.436747Z'
  support: supports
  snapshot_sha256: 5bc26c2d3491d422d27034cfa9f4afb128bbe8403d8b097b9e36bf810df038dc
- evidence_id: plaque-up-P38631
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38631.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P38631 is reviewed taxon559292 1,3-beta-glucan synthase component FKS1.
    Exact aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:48.467083Z'
  support: supports
  snapshot_sha256: 7c39236f9feb71057ef9def7792aa07b86eca0508e9d1a85422f54537e73473c
- evidence_id: plaque-up-P40989
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40989.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P40989 is reviewed taxon559292 1,3-beta-glucan synthase component GSC2.
    Exact aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:49.174377Z'
  support: supports
  snapshot_sha256: 7028d3b8a2e4910e99772ff19805e062c077a08c8cae0f602c6ef1de9729c06b
- evidence_id: plaque-up-P06780
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P06780.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P06780 is reviewed taxon559292 GTP-binding protein RHO1. Exact aliases
    and source annotations checked; annotation joins are not independently reproduced
    localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:49.175763Z'
  support: supports
  snapshot_sha256: 38a9436c03b9abbb11b6ff40c5fa3a5fa7b0204d630adb3e437da6211d009047
- evidence_id: plaque-up-Q08773
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08773.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: Q08773 is reviewed taxon559292 ISWI chromatin-remodeling complex ATPase
    ISW2. Exact aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:49.733870Z'
  support: supports
  snapshot_sha256: 2637bfb5d984e050fbf830b95bf000a10c6cf69fd9895b6921cdfe853f59ee2c
- evidence_id: plaque-up-P53125
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53125.json
  locator: Native accession/status/name/gene aliases/loci/taxon; FUNCTION/SUBUNIT/location
    evidence joins and SIMILARITY; no complete sequence/bibliography reanalysis
  summary: P53125 is reviewed taxon559292 Imitation switch two complex protein 1.
    Exact aliases and source annotations checked; annotation joins are not independently
    reproduced localization or assembly experiments.
  accessed_at: '2026-11-03T23:18:49.847624Z'
  support: supports
  snapshot_sha256: 15a6f5624bd3147df7e928db6e548bf9a5d8e7c586453675ef5661d7d4221fd5
- evidence_id: plaque-gene-hupA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.563051Z'
  support: supports
  search_scope: UniProt exact gene hupA plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.563051Z; size100, complete one-entry first page.
  snapshot_sha256: f5131b360ffafed8326ba4a6f8e49aa8075273ef04bdd0fe77f4fd2f9a8a6244
- evidence_id: plaque-gene-hupB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.563931Z'
  support: supports
  search_scope: UniProt exact gene hupB plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.563931Z; size100, complete one-entry first page.
  snapshot_sha256: f6f7f2b99d298b9b720156fbf955840feedd854accfe6be153ab49ce49b73b18
- evidence_id: plaque-gene-ihfA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AihfA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.564876Z'
  support: supports
  search_scope: UniProt exact gene ihfA plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.564876Z; size100, complete one-entry first page.
  snapshot_sha256: 5a6c232662fddade215e3ec7ee975bac8eb0c554b1ac007be5ecd2d584946197
- evidence_id: plaque-gene-ihfB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AihfB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.566011Z'
  support: supports
  search_scope: UniProt exact gene ihfB plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.566011Z; size100, complete one-entry first page.
  snapshot_sha256: 00dca6f69237cb0cf2fa1bd1489807bdf6c63c8ff390ed3a9dc08ef76e868033
- evidence_id: plaque-gene-fis
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Afis%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.566184Z'
  support: supports
  search_scope: UniProt exact gene fis plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.566184Z; size100, complete one-entry first page.
  snapshot_sha256: 359db2d48e14e3708cd83734b39dc68565c7dd321b7aa1381b95f17ce3cdbb42
- evidence_id: plaque-gene-hns
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahns%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.568506Z'
  support: supports
  search_scope: UniProt exact gene hns plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.568506Z; size100, complete one-entry first page.
  snapshot_sha256: c2d0e5f91fafe9a823753036538ef81645c7a74225054fb9d4b8b443df015ec0
- evidence_id: plaque-gene-dps
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.569038Z'
  support: supports
  search_scope: UniProt exact gene dps plus organism_id 83333 and reviewed:true at
    2026-11-03T23:20:29.569038Z; size100, complete one-entry first page.
  snapshot_sha256: 55916ff15491526e1713c2c33dd025ca4d012ffc4a8ed2f8a596f6dcad3c0619
- evidence_id: plaque-gene-FKS1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AFKS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:29.570472Z'
  support: supports
  search_scope: UniProt exact gene FKS1 plus organism_id 559292 and reviewed:true
    at 2026-11-03T23:20:29.570472Z; size100, complete one-entry first page.
  snapshot_sha256: aadedac84d93bd1dbcc09104db77e8b8e54caf7a1db2c76aba03a63c030720d0
- evidence_id: plaque-gene-FKS2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AFKS2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:30.641009Z'
  support: supports
  search_scope: UniProt exact gene FKS2 plus organism_id 559292 and reviewed:true
    at 2026-11-03T23:20:30.641009Z; size100, complete one-entry first page.
  snapshot_sha256: 67c33b0942299de098a994c951ac37451b48f69604b1b40681ea77750a4f4b98
- evidence_id: plaque-gene-RHO1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARHO1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:30.820648Z'
  support: supports
  search_scope: UniProt exact gene RHO1 plus organism_id 559292 and reviewed:true
    at 2026-11-03T23:20:30.820648Z; size100, complete one-entry first page.
  snapshot_sha256: 90d4a88deadb08d4a446a7a6399b97b140ef41e297821cb315221711374ba7e9
- evidence_id: plaque-gene-ISW2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:31.000725Z'
  support: supports
  search_scope: UniProt exact gene ISW2 plus organism_id 559292 and reviewed:true
    at 2026-11-03T23:20:31.000725Z; size100, complete one-entry first page.
  snapshot_sha256: 4a0b2c299a8108e3d0211b807a656d0b2a8cc4309334e35a687d00689cca310d
- evidence_id: plaque-gene-ITC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AITC1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned exact gene/taxon/reviewed first page
  summary: Single reviewed hit matches direct accession; FKS2 returns primary gene
    GSC2/P40989 via alias. No exhaustive homolog inventory claimed.
  accessed_at: '2026-11-03T23:20:31.778151Z'
  support: supports
  search_scope: UniProt exact gene ITC1 plus organism_id 559292 and reviewed:true
    at 2026-11-03T23:20:31.778151Z; size100, complete one-entry first page.
  snapshot_sha256: 9555d012d20ee604810ec610e8d7bb48fa09ada92bbfafe02f82a3ac4e6f7c2f
- evidence_id: plaque-ipr-IPR000119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000119/
  locator: Complete native identity/type/curated description and hierarchy; unrelated
    cross-reference literature not independently read
  summary: IPR000119 Histone-like DNA-binding protein is family. HU/IHF family is
    not the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and
    Isw1/2 N-terminal domain are broader than the curated specific subunit boundaries.
    Bounded candidates do not prove no exact family exists anywhere.
  accessed_at: '2026-11-03T23:18:50.674807Z'
  support: supports
  snapshot_sha256: 2d778c0a6dc148b8ae5dd8242ed2ee98cede39e09253798ac3e85ec4a2de2e88
- evidence_id: plaque-ipr-IPR003440
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003440/
  locator: Complete native identity/type/curated description and hierarchy; unrelated
    cross-reference literature not independently read
  summary: IPR003440 Glycosyl transferase 48 domain is domain. HU/IHF family is not
    the heterogeneous full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2
    N-terminal domain are broader than the curated specific subunit boundaries. Bounded
    candidates do not prove no exact family exists anywhere.
  accessed_at: '2026-11-03T23:18:51.319416Z'
  support: supports
  snapshot_sha256: 2ec93b9fecde227aa097f079b5d15e70e572435283f09de7c6c33e6e9f4a4ff9
- evidence_id: plaque-ipr-IPR003578
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003578/
  locator: Complete native identity/type/curated description and hierarchy; unrelated
    cross-reference literature not independently read
  summary: IPR003578 Small GTPase Rho is family. HU/IHF family is not the heterogeneous
    full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain
    are broader than the curated specific subunit boundaries. Bounded candidates do
    not prove no exact family exists anywhere.
  accessed_at: '2026-11-03T23:18:51.746477Z'
  support: supports
  snapshot_sha256: 446700f6da68021d90d57bbab566c1a135016325e960f2c8a1ec8d39ebca8902
- evidence_id: plaque-ipr-IPR013136
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013136/
  locator: Complete native identity/type/curated description and hierarchy; unrelated
    cross-reference literature not independently read
  summary: IPR013136 WSTF/Acf1/Cbp146 is domain. HU/IHF family is not the heterogeneous
    full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain
    are broader than the curated specific subunit boundaries. Bounded candidates do
    not prove no exact family exists anywhere.
  accessed_at: '2026-11-03T23:18:51.897854Z'
  support: supports
  snapshot_sha256: 488a03063928728b3bf2a6a15a1a53cfd9746338990d7028aa065f067d117d1e
- evidence_id: plaque-ipr-IPR044754
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/
  locator: Complete native identity/type/curated description and hierarchy; unrelated
    cross-reference literature not independently read
  summary: IPR044754 Isw1/2, N-terminal is domain. HU/IHF family is not the heterogeneous
    full NAP cohort; GT48 domain, Rho family, WAC domain and Isw1/2 N-terminal domain
    are broader than the curated specific subunit boundaries. Bounded candidates do
    not prove no exact family exists anywhere.
  accessed_at: '2026-11-03T23:18:52.014229Z'
  support: supports
  snapshot_sha256: 061068d91ce4e280dc97c8d9a97b780be29b8b80f8c5df5475c0f0511e87bf06
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Fresh complete official /api/datasets response
  summary: All twenty organism rows and28 organism-dataset pairs inspected. E.coli
    is covered; no Saccharomyces entry. Yeast source fallback uses current primary/authority
    evidence, not bacterial proxies.
  accessed_at: '2026-11-03T23:18:55.079088Z'
  support: supports
  search_scope: Official full catalogue at 2026-11-03T23:18:55.079088Z; all returned
    rows inspected for E.coli and Saccharomyces, no broader database absence claim.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-adapter-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete precise1k metadata
  summary: e_coli/precise1k has201 modules,4257 genes and five named strains BW25113,DGF-298,GMOS,MG1655,W3110.
    Selected MG1655 reference-locus mapping does not make this a single-strain dataset.
  accessed_at: '2026-11-03T23:20:32.230387Z'
  support: supports
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: plaque-adapter-imodulons
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete201-row module metadata list; selected3,51,145 considered
  summary: Module labels/regulators/thresholds are computational context, not direct
    nucleoid assembly/necessity evidence. No generated summary or activity interpretation
    used.
  accessed_at: '2026-11-03T23:20:32.773465Z'
  support: supports
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: plaque-adapter-search-hupA
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=hupA&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 0 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:31.899488Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:31.899488Z; organism=e_coli,dataset=precise1k,query=hupA,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: 322a156c0df3ccc70ccc3865d5cee4c384d696dd5b33c0536a4c52c5e4c2c247
- evidence_id: plaque-adapter-search-hupB
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=hupB&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 0 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:31.946815Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:31.946815Z; organism=e_coli,dataset=precise1k,query=hupB,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: 120ed8dec1f3e1443a624617e1b427bf0a099fcdceefdacfdb24178dcba7a4f2
- evidence_id: plaque-adapter-search-ihfA
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ihfA&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 0 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:31.993196Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:31.993196Z; organism=e_coli,dataset=precise1k,query=ihfA,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: b6763599e63ed575be70edb5adc7eff50ee2b4f1f05fc5c49049f8ed742910d8
- evidence_id: plaque-adapter-search-ihfB
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=ihfB&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 0 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:32.041269Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:32.041269Z; organism=e_coli,dataset=precise1k,query=ihfB,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: 5d7169cee024f0d3b2128c3140078841797fd4bfe3ad8b707a817dc2f86a2dd4
- evidence_id: plaque-adapter-search-fis
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=fis&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 3 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:32.090317Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:32.090317Z; organism=e_coli,dataset=precise1k,query=fis,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: 833de800d7ad67cfdb0e8995b903a65b645fb476bbafaf54fa46611203b1c31f
- evidence_id: plaque-adapter-search-hns
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=hns&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 0 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:32.136470Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:32.136470Z; organism=e_coli,dataset=precise1k,query=hns,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: 2fb4484bbab56305d36d86889492f20878d3b7795e9e71c44127049170bff432
- evidence_id: plaque-adapter-search-dps
  kind: search
  reference: https://imodulondb.org/api/search?organism=e_coli&dataset=precise1k&query=dps&limit=50
  locator: Complete official bounded returned gene/module hits
  summary: 1 gene hits and 0 module text hits; exact locus identities used for follow-up.
    Regulator text hit is not membership or binding evidence.
  accessed_at: '2026-11-03T23:20:32.183745Z'
  support: supports
  search_scope: Official search at 2026-11-03T23:20:32.183745Z; organism=e_coli,dataset=precise1k,query=dps,limit50;
    complete returned result lists, no unrelated strain proxy.
  snapshot_sha256: a763ae83767d2194c038ef0fc8396914ce620ddbf94be8d53bf655403f14d50b
- evidence_id: plaque-adapter-gene-b4000
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4000
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b4000 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.243803Z'
  support: supports
  snapshot_sha256: b45f61696b0ee2cc6fd611a1269a2a8576642efa1aabffddfc0e3a129d6379f0
- evidence_id: plaque-adapter-gene-b4000-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4000/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: none. Below-threshold values do not imply biological
    absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.244905Z'
  support: supports
  snapshot_sha256: a13c830fbd7d2e7169fbbd345eadb7600d67ab46d7d389ec0f282d2d6cc28bcb
- evidence_id: plaque-adapter-gene-b0440
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0440
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b0440 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.246013Z'
  support: supports
  snapshot_sha256: c68696276d2626879193398a43271c816eaa3f74946c144090c66f4847a4896e
- evidence_id: plaque-adapter-gene-b0440-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0440/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: none. Below-threshold values do not imply biological
    absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.247202Z'
  support: supports
  snapshot_sha256: 87f05cf2bd19cc1c4fcc48ab37ff284bfa70a60c7fdf8a6547c3a965e8df15fb
- evidence_id: plaque-adapter-gene-b1712
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1712
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b1712 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.248397Z'
  support: supports
  snapshot_sha256: efb84ea173003be3f87870e61c17bddf5d205b4ad20f7397eb420a64e531bab3
- evidence_id: plaque-adapter-gene-b1712-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1712/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: none. Below-threshold values do not imply biological
    absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.249654Z'
  support: supports
  snapshot_sha256: 3ba0762a3e0dd804fd0c8da9e656e29eb654143be71394441e07ee8bdbb65cb9
- evidence_id: plaque-adapter-gene-b0912
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0912
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b0912 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.250986Z'
  support: supports
  snapshot_sha256: 49f94080eb811fee3e6d0d84ecf3678cd083f63d9c62e4d22693c9eac163a91f
- evidence_id: plaque-adapter-gene-b0912-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0912/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: none. Below-threshold values do not imply biological
    absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.252231Z'
  support: supports
  snapshot_sha256: 89c2530e4a5fe7a5c5ca7932605578321f83d33af859fbf5a78c2ce79c37537d
- evidence_id: plaque-adapter-gene-b3261
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3261
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b3261 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.604945Z'
  support: supports
  snapshot_sha256: b1f3305916b9fe3da78613bdd12b8a8a98713af0ed37aedacffadba4b3e69155
- evidence_id: plaque-adapter-gene-b3261-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3261/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: 145 ppGpp. Below-threshold values do not imply biological
    absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.605821Z'
  support: supports
  snapshot_sha256: 82d71bff635e99da2af04cc93a2c654b2459ca46919214b47f8d8f3163697d82
- evidence_id: plaque-adapter-gene-b1237
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1237
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b1237 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.606833Z'
  support: supports
  snapshot_sha256: 23ec8c95373585b4a8a1d91b110cf2d5e4a228582f8b6bd4cd6575b94719cd15
- evidence_id: plaque-adapter-gene-b1237-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1237/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: none. Below-threshold values do not imply biological
    absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.608116Z'
  support: supports
  snapshot_sha256: 418140dc466cb21d2f8fe4a4ce96621cfa961cc9cba93803f1b1ca9f7bf45ffa
- evidence_id: plaque-adapter-gene-b0812
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0812
  locator: Exact selected gene metadata, accession and String taxon-locus fields
  summary: Reference locus b0812 maps to the corresponding maintained reviewed NAP
    accession and String511145. Mixed experimental strains remain governed by dataset
    metadata.
  accessed_at: '2026-11-03T23:20:55.907520Z'
  support: supports
  snapshot_sha256: 884791963f2d48da38c11a21c767a55201f6997f978c02976e0ed5ac7db50871
- evidence_id: plaque-adapter-gene-b0812-modules
  kind: database
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0812/imodulons
  locator: All201 is_in_imodulon flags; selected true rows and thresholds
  summary: 'True membership rows: 3 OxyR, 51 RpoS. Below-threshold values do not imply
    biological absence, no localization or assembly inference.'
  accessed_at: '2026-11-03T23:20:55.908656Z'
  support: supports
  snapshot_sha256: 6e22deeb24f50dcae23f9476907de7878c8c159961d1f1753f18f02b39712ad5
- evidence_id: plaque-adapter-module-3
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/3
  locator: Exact selected module metadata and gene memberships/threshold; AI summary
    and activities excluded
  summary: Selected OxyR3/RpoS51 carry dps b0812; ppGpp145 carries fis b3261, matching
    gene-side true flags. Computational transcriptional context only; no proof of
    all-NAP coregulation or nucleoid formation.
  accessed_at: '2026-11-03T23:21:19.637429Z'
  support: supports
  snapshot_sha256: 8f13d013b44e8d7cc9c4f7a17131b26bacd92039947bd13be57aadffea91f49e
- evidence_id: plaque-adapter-module-51
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/51
  locator: Exact selected module metadata and gene memberships/threshold; AI summary
    and activities excluded
  summary: Selected OxyR3/RpoS51 carry dps b0812; ppGpp145 carries fis b3261, matching
    gene-side true flags. Computational transcriptional context only; no proof of
    all-NAP coregulation or nucleoid formation.
  accessed_at: '2026-11-03T23:21:19.638495Z'
  support: supports
  snapshot_sha256: 0178f2450c16c9f77f3c57a250537106ec85c4ddf6d1771458a534245b109fee
- evidence_id: plaque-adapter-module-145
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/145
  locator: Exact selected module metadata and gene memberships/threshold; AI summary
    and activities excluded
  summary: Selected OxyR3/RpoS51 carry dps b0812; ppGpp145 carries fis b3261, matching
    gene-side true flags. Computational transcriptional context only; no proof of
    all-NAP coregulation or nucleoid formation.
  accessed_at: '2026-11-03T23:21:19.638700Z'
  support: supports
  snapshot_sha256: 830f9a931fa5b6577f9ad87c99a4cbc198961cbd72c61ad8ff4d42812846f2dd
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical actual00:49Z runner receipt only, never fresh invocation
  summary: Prior kg-microbe-sources datasets runner exited1 with pyvenv.cfg permission
    error. Current review uses direct inspected official public-source fallback; no
    current runner success claimed.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-plaque/original-checks.json
  locator: Actual three native validate/render commands and44 historical frozen rows
    checked by git show
  summary: All three originals validate, Markdown is deterministic and all historical
    hashes match; all own current targets unchanged.
  accessed_at: '2026-11-03T23:23:47.077755Z'
  support: supports
  snapshot_sha256: c46bc6b5e9ba1436ba6453b590b1452ad71938a565650a119aa0f0e8d1e342eb
- evidence_id: plaque-native-nucleoid-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/nucleoid.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-verify-receipt.json;
    logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: seven reviewed K-12 examples, one COVERED pooled NAP node. Actual native
    success concerns represented identity/coverage, not scientific mechanism, necessity
    or universal class completeness.
  accessed_at: '2026-11-03T23:17:29.874176Z'
  support: supports
  snapshot_sha256: e8777daf2b621cc00018c063affe15f73d8b3cc8c75d1e4cc421d83d74ca7aff
- evidence_id: plaque-native-nucleoid-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/nucleoid/nucleoid.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-causal-receipt.json;
    logSHA256 060c0334ea540c0999476872bdce276671f1ffa111deee448f7ebcb5fe1291a1
  summary: seven reviewed K-12 examples, one COVERED pooled NAP node. Actual native
    success concerns represented identity/coverage, not scientific mechanism, necessity
    or universal class completeness.
  accessed_at: '2026-11-03T23:17:30.280335Z'
  support: supports
  snapshot_sha256: b501d0dcaa40e5b235bec7fb7a0accc5028a8d538b900192fe0e67116eeb7bbc
- evidence_id: plaque-native-1_3_beta_d_glucan_synthase_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-verify-receipt.json;
    logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: three reviewed S288C examples, two COVERED Fks/Rho1 nodes. Actual native
    success concerns represented identity/coverage, not scientific mechanism, necessity
    or universal class completeness.
  accessed_at: '2026-11-03T23:17:32.249837Z'
  support: supports
  snapshot_sha256: 587c38b3b5c933f218e1dc2ebfb2036a95a1f7bc5ab76868f0c0291e5dd645e1
- evidence_id: plaque-native-1_3_beta_d_glucan_synthase_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/1_3_beta_d_glucan_synthase_complex.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-causal-receipt.json;
    logSHA256 e5e246afc40662210eb530ad32b4b670cccbcf512c0f14cb2d7c4689b7445665
  summary: three reviewed S288C examples, two COVERED Fks/Rho1 nodes. Actual native
    success concerns represented identity/coverage, not scientific mechanism, necessity
    or universal class completeness.
  accessed_at: '2026-11-03T23:17:32.659871Z'
  support: supports
  snapshot_sha256: 0a48893bce3ddfb04c7b2de7a6c045e2186344c46ab593cf44307b03e90232b5
- evidence_id: plaque-native-acf_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acf_complex.yaml
    --verify
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-verify-receipt.json;
    logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: two reviewed S288C examples, two COVERED Isw2/Itc1 nodes. Actual native
    success concerns represented identity/coverage, not scientific mechanism, necessity
    or universal class completeness.
  accessed_at: '2026-11-03T23:17:35.308337Z'
  support: supports
  snapshot_sha256: 5981739952ebf7bfea452da0ccd96add135fb94a01ad83ad5876aa48ad97d567
- evidence_id: plaque-native-acf_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/acf_complex.yaml
    --causal-graphs
  locator: Actual receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-causal-receipt.json;
    logSHA256 e34e9c8cebb57c5f572bee3aa6dcdb3271c14c814833d2bbe620d8bddfa7862f
  summary: two reviewed S288C examples, two COVERED Isw2/Itc1 nodes. Actual native
    success concerns represented identity/coverage, not scientific mechanism, necessity
    or universal class completeness.
  accessed_at: '2026-11-03T23:17:35.713055Z'
  support: supports
  snapshot_sha256: c5d729f64d58145410c7241fe4f40743de694f72251c60c43ae0c267e985e39f
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
  locator: Complete current YAML, all fields; source 7b6cd533340948100b7b23d8ab4e659702d9feba
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Whole record read, including all components, examples, evidence placements,
    graph, discussion and append-only history.
  snapshot_sha256: 2b55cd8964b49c798747f87a1027fd9817864853f125fcdc10569ed285f784cc
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit/review.yaml
  locator: Complete immutable original YAML and paired Markdown; original source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Original scientific verdict, checks, findings/actions and access limitations
    inspected; historical reads/checks are not relabeled as current.
  snapshot_sha256: 53166c85e2439f7129d436ff0996c75dafde87a526cfcba46e7a63f1f57f0aea
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/propanediol_degradation_polyhedral_organelle-actual-stale.diff
  locator: Exact git diff of original frozen target to current source
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Substantive delta reassessed against current sources; history and graph
    changes; see evidence-linked stale assessment.
  snapshot_sha256: d425356b9210e8ce9352bd375da9ea59c74b58e7067c6c56f8ab2a63f56d8040
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  locator: Complete current YAML, all fields; source 7b6cd533340948100b7b23d8ab4e659702d9feba
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Whole record read, including all components, examples, evidence placements,
    graph, discussion and append-only history.
  snapshot_sha256: 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit/review.yaml
  locator: Complete immutable original YAML and paired Markdown; original source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Original scientific verdict, checks, findings/actions and access limitations
    inspected; historical reads/checks are not relabeled as current.
  snapshot_sha256: e2920ac68a117c70a04bc1446d841e4f3ba0d1d8b828b8c839d8bf08fb656e5f
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/3_phenylpropionate_dioxygenase_complex-actual-stale.diff
  locator: Exact git diff of original frozen target to current source
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Substantive delta reassessed against current sources; target unchanged.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
  locator: Complete current YAML, all fields; source 7b6cd533340948100b7b23d8ab4e659702d9feba
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Whole record read, including all components, examples, evidence placements,
    graph, discussion and append-only history.
  snapshot_sha256: 781dd7e152917915b204ac297248d0caa8f290a2f815b9bf9ed41f43b8819c25
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit/review.yaml
  locator: Complete immutable original YAML and paired Markdown; original source f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Original scientific verdict, checks, findings/actions and access limitations
    inspected; historical reads/checks are not relabeled as current.
  snapshot_sha256: 17ce9ceedb6bbe85b4c7343c55e968970c093e3fa088a8d11c5e0b1d1270d42c
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/acrab_tolc_multidrug_efflux_transport_complex-actual-stale.diff
  locator: Exact git diff of original frozen target to current source
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Substantive delta reassessed against current sources; history and graph
    changes; see evidence-linked stale assessment.
  snapshot_sha256: 8ee7493ca1932906d2982d0b838431093ddbf98a499904909c1c758dc8f89767
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components, family grounding, source-specific complex_compositions, formation
    essentiality, Discussions lines305–324
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Exact-family grounding is required when available; source composition does
    not redefine a protein family or independently establish formation necessity.
    Historical rationale is append-only; prompts/notes can reflect present unresolved
    work.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-native-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules and Structured Source Cross-Checks; current profile/config
    and rubric reread
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Whole-record gene/protein/pathway assertions trigger source-adapter applicability.
    Reviewed assertions are distinguished from old provenance and bounded source access.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/original-pair-and-hash-audit.json
  locator: All three original validate/render commands; all original manifested source
    inputs at each original git_revision
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: All three original YAMLs validate; Markdown rendering is byte-identical.
    Every original input SHA matches its historical revision; Pdu and Acr current
    inputs differ, Hca matches.
  snapshot_sha256: 9d2510f40fff6a700f22318a2ecfddc1b6136171e2516cac5d1c4f637774f766
- evidence_id: micro-up-H9L478
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/H9L478.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-H9L478.raw
  accessed_at: '2026-11-03T23:16:50.741739Z'
  support: supports
  summary: 'H9L478: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduJ;
    Bacterial microcompartment shell protein PduJ. Native InterPro links IPR020808,
    IPR000249, IPR050575, IPR037233, IPR044872. Identity and native annotation are
    distinct from primary experimental membership evidence.'
  snapshot_sha256: 36333b80883cffc9e16691c1a00cb20786510cc6827b59b953e701172ea78c53
- evidence_id: micro-up-O31041
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O31041.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-O31041.raw
  accessed_at: '2026-11-03T23:16:50.742010Z'
  support: supports
  summary: 'O31041: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduD;
    Propanediol dehydratase medium subunit. Native InterPro links IPR010254, IPR003208,
    IPR025541. Identity and native annotation are distinct from primary experimental
    membership evidence.'
  snapshot_sha256: 269ad4332be19430e7c7584d14764c257523f85397d87cf421cf45e7e63bef6d
- evidence_id: micro-up-O31042
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/O31042.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-O31042.raw
  accessed_at: '2026-11-03T23:16:50.742088Z'
  support: supports
  summary: 'O31042: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduE;
    Propanediol dehydratase small subunit. Native InterPro links IPR003207, IPR036091.
    Identity and native annotation are distinct from primary experimental membership
    evidence.'
  snapshot_sha256: 069d7e39a2dc26608992b9ae88e8ec89578fc94c513543471f83ce31becb1f5d
- evidence_id: micro-up-P02930
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P02930.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P02930.raw
  accessed_at: '2026-11-03T23:16:50.742139Z'
  support: supports
  summary: 'P02930: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene tolC;
    Outer membrane protein TolC. Native InterPro links IPR003423, IPR010130, IPR058622,
    IPR051906. Identity and native annotation are distinct from primary experimental
    membership evidence.'
  snapshot_sha256: cef14f6af1999fe0b5218d959cca8788ec00afc1b145201ba48344a4b15bbb04
- evidence_id: micro-up-P0A1C7
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1C7.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0A1C7.raw
  accessed_at: '2026-11-03T23:16:50.742179Z'
  support: supports
  summary: 'P0A1C7: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduA;
    Bacterial microcompartment shell protein PduA. Native InterPro links IPR020808,
    IPR000249, IPR050575, IPR037233, IPR044872. Identity and native annotation are
    distinct from primary experimental membership evidence.'
  snapshot_sha256: 389718a823a5a31aeff4e117b5c2a3af6c95e95647de047e52a9c0745dd5f064
- evidence_id: micro-up-P0A1D1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A1D1.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0A1D1.raw
  accessed_at: '2026-11-03T23:16:50.742211Z'
  support: supports
  summary: 'P0A1D1: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduU;
    Bacterial microcompartment shell protein PduU. Native InterPro links IPR044870,
    IPR000249, IPR037233, IPR009307. Identity and native annotation are distinct from
    primary experimental membership evidence.'
  snapshot_sha256: 77369d0ed03be3e2c5b5d655dc9451a709e79dea816a98fa564f6d026e7d3796
- evidence_id: micro-up-P0ABR5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ABR5.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0ABR5.raw
  accessed_at: '2026-11-03T23:16:51.695937Z'
  support: supports
  summary: 'P0ABR5: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaE;
    3-phenylpropionate/cinnamic acid dioxygenase subunit alpha. Native InterPro links
    IPR054883, IPR015881, IPR020875, IPR043266, IPR017941, IPR036922, IPR015879, IPR001663.
    Identity and native annotation are distinct from primary experimental membership
    evidence.'
  snapshot_sha256: 08176c230f3b4a248de3364416a47222d604fa3ee17abcd31de7a61b8bb06b62
- evidence_id: micro-up-P0ABW0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ABW0.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0ABW0.raw
  accessed_at: '2026-11-03T23:16:52.007894Z'
  support: supports
  summary: 'P0ABW0: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaC;
    3-phenylpropionate/cinnamic acid dioxygenase ferredoxin subunit. Native InterPro
    links IPR023739, IPR017941, IPR036922, IPR053387. Identity and native annotation
    are distinct from primary experimental membership evidence.'
  snapshot_sha256: 5a0c63f8f56d5fbc19917b7b96d82f83736563385e701c0a391f55e21e1bb875
- evidence_id: micro-up-P0AE06
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AE06.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P0AE06.raw
  accessed_at: '2026-11-03T23:16:52.662992Z'
  support: supports
  summary: 'P0AE06: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene acrA;
    Multidrug efflux pump subunit AcrA. Native InterPro links IPR058628, IPR058626,
    IPR058625, IPR058627, IPR058624, IPR006143. Identity and native annotation are
    distinct from primary experimental membership evidence.'
  snapshot_sha256: 3353ebe0339b2686335d36fa720ceee4c8808ae38f2a2c975d3ef3cdba6cdb9d
- evidence_id: micro-up-P31224
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P31224.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P31224.raw
  accessed_at: '2026-11-03T23:16:53.009378Z'
  support: supports
  summary: 'P31224: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene acrB;
    Multidrug efflux pump subunit AcrB. Native InterPro links IPR027463, IPR001036,
    IPR004764. Identity and native annotation are distinct from primary experimental
    membership evidence.'
  snapshot_sha256: cd8e89b948d93accd44fa9e734affcae68c35ac537710cbca4aedd1ea46d47ae
- evidence_id: micro-up-P37449
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P37449.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P37449.raw
  accessed_at: '2026-11-03T23:16:53.902796Z'
  support: supports
  summary: 'P37449: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduB;
    Bacterial microcompartment shell protein PduB. Native InterPro links IPR044870,
    IPR000249, IPR037233, IPR009193, IPR030984. Identity and native annotation are
    distinct from primary experimental membership evidence.'
  snapshot_sha256: 4c43b72065c16c776a492d6ffafacc3bf9348b1bd54bd5164b67a16a09980ed0
- evidence_id: micro-up-P37450
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P37450.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P37450.raw
  accessed_at: '2026-11-03T23:16:54.607251Z'
  support: supports
  summary: 'P37450: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduC;
    Propanediol dehydratase large subunit. Native InterPro links IPR016176, IPR036999,
    IPR003206. Identity and native annotation are distinct from primary experimental
    membership evidence.'
  snapshot_sha256: c53413b5403dc092d117c68da0b59e6dfaaebfae9e3e1c50c7fb0d9fe2a58ade
- evidence_id: micro-up-P77650
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P77650.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-P77650.raw
  accessed_at: '2026-11-03T23:16:55.548851Z'
  support: supports
  summary: 'P77650: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaD;
    3-phenylpropionate/cinnamic acid dioxygenase ferredoxin--NAD(+) reductase component.
    Native InterPro links IPR050446, IPR036188, IPR023753, IPR016156, IPR023744, IPR028202,
    IPR053382. Identity and native annotation are distinct from primary experimental
    membership evidence.'
  snapshot_sha256: 7781933570445ba5da2b33cdf9f8c58a66120b43916bf9d5d5504b236a2d40e4
- evidence_id: micro-up-Q47140
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q47140.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q47140.raw
  accessed_at: '2026-11-03T23:16:55.575824Z'
  support: supports
  summary: 'Q47140: UniProtKB reviewed (Swiss-Prot); taxon 83333; primary gene hcaF;
    3-phenylpropionate/cinnamic acid dioxygenase subunit beta. Native InterPro links
    IPR054881, IPR023712, IPR032710, IPR000391. Identity and native annotation are
    distinct from primary experimental membership evidence.'
  snapshot_sha256: 08f095db894d9c06832d7216602d49ec9751f8479467f4a93b9ce5aee42bf51a
- evidence_id: micro-up-Q9XDM8
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9XDM8.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDM8.raw
  accessed_at: '2026-11-03T23:16:55.752280Z'
  support: supports
  summary: 'Q9XDM8: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduT;
    Bacterial microcompartment shell protein PduT. Native InterPro links IPR000249,
    IPR050575, IPR037233, IPR044872, IPR011238. Identity and native annotation are
    distinct from primary experimental membership evidence.'
  snapshot_sha256: 805112b48c5200721328c2a87ee11a81aa36e9c9864afc22e0262ef5f677cf1c
- evidence_id: micro-up-Q9XDN3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9XDN3.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDN3.raw
  accessed_at: '2026-11-03T23:16:56.643142Z'
  support: supports
  summary: 'Q9XDN3: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduN;
    Bacterial microcompartment shell vertex protein PduN. Native InterPro links IPR004992,
    IPR036677. Identity and native annotation are distinct from primary experimental
    membership evidence.'
  snapshot_sha256: 0b1f46044a456550bd908272a2b76536d36d59146da0295d7113948452fe2907
- evidence_id: micro-up-Q9XDN4
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9XDN4.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDN4.raw
  accessed_at: '2026-11-03T23:16:56.765720Z'
  support: supports
  summary: 'Q9XDN4: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduM;
    Bacterial microcompartment assembly protein PduM. Native InterPro links IPR030992.
    Identity and native annotation are distinct from primary experimental membership
    evidence.'
  snapshot_sha256: 4fe5c228010e17183e28a56db12e6eedaaf515089cfe4e7458ab754c6a5a56d6
- evidence_id: micro-up-Q9XDN6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q9XDN6.json
  locator: Native accession, reviewed status, organism, primary gene/aliases/loci,
    recommended protein name, InterPro and source-comment joins; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/up-Q9XDN6.raw
  accessed_at: '2026-11-03T23:16:57.573142Z'
  support: supports
  summary: 'Q9XDN6: UniProtKB reviewed (Swiss-Prot); taxon 99287; primary gene pduK;
    Bacterial microcompartment shell protein PduK. Native InterPro links IPR000249,
    IPR050575, IPR037233, IPR044872. Identity and native annotation are distinct from
    primary experimental membership evidence.'
  snapshot_sha256: 7078fab3c550ef1d2bef2004939cec6072992dacb1c6d7e9f82907f499577eb5
- evidence_id: micro-gene-acrA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AacrA+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-acrA.raw
  accessed_at: '2026-11-03T23:22:36.670283Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P0AE06. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: db2b7a433db8b30d1e3c4eeda0b263513bffa43484c8e1403d8cd41029abd2c3
  search_scope: UniProtKB official REST, 2026-11-03T23:22:36.670283Z; query gene_exact:acrA
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-acrB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AacrB+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-acrB.raw
  accessed_at: '2026-11-03T23:22:36.702799Z'
  support: supports
  summary: 'Current bounded query returns 2 reviewed accession(s): P0AES6, P31224.
    The acrB search also returns gyrB via a historical alias; exact P31224 identity
    is disambiguated by primary name, locus and CPX, and the record does not assert
    query uniqueness.'
  snapshot_sha256: c53b7a06c823e1c287f6dea99c2e96cde8f91bf47419b4a6f12fd1733ce27731
  search_scope: UniProtKB official REST, 2026-11-03T23:22:36.702799Z; query gene_exact:acrB
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 2, X-Total-Results=2,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-hcaC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaC+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaC.raw
  accessed_at: '2026-11-03T23:22:35.887280Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P0ABW0. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: d700e37536aa89a1082b77640f8ed0d161f1c5f400f831e6accc1fba6abbd7e9
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.887280Z; query gene_exact:hcaC
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-hcaD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaD+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaD.raw
  accessed_at: '2026-11-03T23:22:38.688365Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P77650. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 01a5f217b35169902c6ee831a1566a639fc8558b899cf7b08afd3276352e53c0
  search_scope: UniProtKB official REST, 2026-11-03T23:22:38.688365Z; query gene_exact:hcaD
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-hcaE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaE+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaE.raw
  accessed_at: '2026-11-03T23:22:35.764355Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P0ABR5. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 1545daa1f007b87b3c700efea3e1f2913f9f4a6d62e5fd491a9f72ed066fe62b
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.764355Z; query gene_exact:hcaE
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-hcaF
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AhcaF+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-hcaF.raw
  accessed_at: '2026-11-03T23:22:38.727095Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): Q47140. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: e58a3f6471b9b0bd2d3a34865576f4d6df12b0c6b915cc74273ab9034fe66fe0
  search_scope: UniProtKB official REST, 2026-11-03T23:22:38.727095Z; query gene_exact:hcaF
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduA+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduA.raw
  accessed_at: '2026-11-03T23:22:35.096214Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P0A1C7. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 9230083ff15b60a536605ae6b3aa9029d00107e06101f547847aef014b974312
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.096214Z; query gene_exact:pduA
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduB+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduB.raw
  accessed_at: '2026-11-03T23:22:37.600728Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P37449. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 70180ba802ea7f9ac8624cfdc12e8c7b7d6779abfd09629a30c0cb4e81db5617
  search_scope: UniProtKB official REST, 2026-11-03T23:22:37.600728Z; query gene_exact:pduB
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduC+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduC.raw
  accessed_at: '2026-11-03T23:22:37.747059Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P37450. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: f867b5bacef9b8605be6d5e184e68681651cb08e1cbbd843ab8fe19c8c3d1625
  search_scope: UniProtKB official REST, 2026-11-03T23:22:37.747059Z; query gene_exact:pduC
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduD+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduD.raw
  accessed_at: '2026-11-03T23:22:35.096001Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): O31041. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 133e5c9eb4fb3cd6affcf558bf16e17a84c1dc7ef4416204745dd9524bc79953
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.096001Z; query gene_exact:pduD
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduE+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduE.raw
  accessed_at: '2026-11-03T23:22:35.096097Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): O31042. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 5f93191405fcea4be04a84d8021cac700ad38266717425bedcc074e3a7cba6fd
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.096097Z; query gene_exact:pduE
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduJ
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduJ+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduJ.raw
  accessed_at: '2026-11-03T23:22:35.095733Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): H9L478. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 40795971e9074201a420a6a358abf7be3078afe2243853b7a76233cb5363b8aa
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.095733Z; query gene_exact:pduJ
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduK
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduK+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduK.raw
  accessed_at: '2026-11-03T23:22:40.664576Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): Q9XDN6. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 0ec1a602c883c9237a1faf123481193ee06d3c1516a44e9cbeacb16bce014a74
  search_scope: UniProtKB official REST, 2026-11-03T23:22:40.664576Z; query gene_exact:pduK
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduM
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduM+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduM.raw
  accessed_at: '2026-11-03T23:22:40.583631Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): Q9XDN4. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 107f1c90997cb5b80fd43d3b3b466d0be13d784a9f68a5d78b2565106dc6519a
  search_scope: UniProtKB official REST, 2026-11-03T23:22:40.583631Z; query gene_exact:pduM
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduN
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduN+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduN.raw
  accessed_at: '2026-11-03T23:22:39.766007Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): Q9XDN3. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 1bfe9f7f4b2522efc8aec199d6768f851069dd32dbd6f9b30218e91ff6dcda74
  search_scope: UniProtKB official REST, 2026-11-03T23:22:39.766007Z; query gene_exact:pduN
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduT
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduT+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduT.raw
  accessed_at: '2026-11-03T23:22:39.738629Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): Q9XDM8. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: e8a827040606f8b4a9d3bf9e1932f13ae9ee13bb8a759541084aa5cf57bd7086
  search_scope: UniProtKB official REST, 2026-11-03T23:22:39.738629Z; query gene_exact:pduT
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-pduU
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ApduU+AND+organism_id%3A99287+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-pduU.raw
  accessed_at: '2026-11-03T23:22:35.096253Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P0A1D1. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 186d353f99d5d950ee20c48842b55c68dcaec056059065944adc2ce6e6c918da
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.096253Z; query gene_exact:pduU
    AND organism_id:99287 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-gene-tolC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AtolC+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=500&fields=accession%2Cid%2Cgene_names%2Corganism_id%2Creviewed
  locator: Complete returned current exact-symbol search result; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/gene-tolC.raw
  accessed_at: '2026-11-03T23:22:35.096164Z'
  support: supports
  summary: 'Current bounded query returns 1 reviewed accession(s): P02930. The acrB
    search also returns gyrB via a historical alias; exact P31224 identity is disambiguated
    by primary name, locus and CPX, and the record does not assert query uniqueness.'
  snapshot_sha256: 0d164b979e58fe34b446ff9c3f0bec688eaa226faf5f9278cf253febbe079626
  search_scope: UniProtKB official REST, 2026-11-03T23:22:35.096164Z; query gene_exact:tolC
    AND organism_id:83333 AND reviewed:true; format=json, size500, returned 1, X-Total-Results=1,
    Link=None. Only this literal current gene/taxon/reviewed query, not all synonyms/taxa
    or historical query state.
- evidence_id: micro-ipr-IPR020875
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020875/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR020875.raw
  accessed_at: '2026-11-03T23:17:00.169874Z'
  support: supports
  summary: 'IPR020875 is type family: 3-phenylpropionate/cinnamic acid dioxygenase,
    alpha subunit. Exact family scope agrees with the named constituent; family identity
    does not prove formation necessity.'
  snapshot_sha256: ffb91c473635ef374c44f21d8c166d81d58bbddb0518617e4b368eb5c91ff63e
- evidence_id: micro-ipr-IPR023712
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023712/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR023712.raw
  accessed_at: '2026-11-03T23:17:00.925492Z'
  support: supports
  summary: 'IPR023712 is type family: 3-phenylpropionate/cinnamic acid dioxygenase,
    beta subunit. Exact family scope agrees with the named constituent; family identity
    does not prove formation necessity.'
  snapshot_sha256: 553f0f946383db786d264b7bc8ce421c703f6c1909eac54310b54a09f9d3ea0a
- evidence_id: micro-ipr-IPR023739
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023739/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR023739.raw
  accessed_at: '2026-11-03T23:17:01.072502Z'
  support: supports
  summary: 'IPR023739 is type family: 3-phenylpropionate/cinnamic acid dioxygenase,
    ferredoxin subunit. Exact family scope agrees with the named constituent; family
    identity does not prove formation necessity.'
  snapshot_sha256: 578080bcd60af9d87d08da429fadd44fe6ca3e3f4eb5c03e36d33c6da59d2787
- evidence_id: micro-ipr-IPR023744
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023744/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR023744.raw
  accessed_at: '2026-11-03T23:17:01.527438Z'
  support: supports
  summary: 'IPR023744 is type family: 3-phenylpropionate/cinnamic acid dioxygenase,
    ferredoxin--NAD(+) reductase subunit. Exact family scope agrees with the named
    constituent; family identity does not prove formation necessity.'
  snapshot_sha256: a5ceb7231afbca265e4ce4b6c27e424c86fb1e5cfd98a18972110295f269c272
- evidence_id: micro-ipr-IPR030992
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030992/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR030992.raw
  accessed_at: '2026-11-03T23:17:02.880321Z'
  support: supports
  summary: 'IPR030992 is type family: Bacterial microcompartment assembly protein
    PduM. Exact PduM family cites Sinha2012 and matches current Q9XDN4.'
  snapshot_sha256: 721b07d44b115a0cb2e00f4dd63ad061d2c2d0d0ab0d5957fd125752419020c9
- evidence_id: micro-ipr-IPR058622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR058622.raw
  accessed_at: '2026-11-03T23:17:01.544131Z'
  support: supports
  summary: 'IPR058622 is type family: Outer membrane channel protein TolC. Exact family
    scope agrees with the named constituent; family identity does not prove formation
    necessity.'
  snapshot_sha256: d3c58cbb9737d5f395f703b634f84df048f355555af2b817f321a5e474b8e310
- evidence_id: micro-ipr-IPR058628
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058628/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR058628.raw
  accessed_at: '2026-11-03T23:17:03.102317Z'
  support: supports
  summary: 'IPR058628 is type family: Multidrug efflux pump subunit AcrA. Exact AcrA
    family includes E. coli AcrA and matches current P0AE06.'
  snapshot_sha256: 122db3dd9fef2511493cb2808549931269cfb075d3fdb63230bf5d05f01c1b9b
- evidence_id: micro-ipr-IPR044870
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044870/
  locator: Native metadata name/type, complete description, hierarchy and supporting
    citation identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/ipr-IPR044870.raw
  accessed_at: '2026-11-03T23:17:03.303647Z'
  support: supports
  summary: 'IPR044870 is type domain: Bacterial microcompartment (BMC) circularly
    permuted domain. Circular permutation is domain architecture, not tandem duplication;
    BMC-H single-domain hexamers and BMC-T tandem-domain trimers are distinguished.'
  snapshot_sha256: ea9d3be2d8b421f5fe80535a4a43a5e82b164a6761578d282c3bc7d962f4b62e
- evidence_id: micro-go-0008695
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0008695
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0008695.raw
  accessed_at: '2026-11-03T23:17:01.663308Z'
  support: supports
  summary: GO:0008695 active=True; 3-phenylpropionate dioxygenase activity. Definition
    read and compared with exact identity, parent class or activity use; not an exhaustive
    ontology absence search.
  snapshot_sha256: 3033e57956b11d5a16016a49052d9218dc498cb839591f2911f76d209eedb843
- evidence_id: micro-go-0009334
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0009334
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0009334.raw
  accessed_at: '2026-11-03T23:17:02.117440Z'
  support: supports
  summary: GO:0009334 active=True; 3-phenylpropionate dioxygenase complex. Definition
    read and compared with exact identity, parent class or activity use; not an exhaustive
    ontology absence search.
  snapshot_sha256: 068cf14fc641de592d99fde1f82a9f09371904a8eaa408f9d66e1e9e43af4ed5
- evidence_id: micro-go-0031469
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0031469
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0031469.raw
  accessed_at: '2026-11-03T23:17:02.177545Z'
  support: supports
  summary: GO:0031469 active=True; bacterial microcompartment. Definition read and
    compared with exact identity, parent class or activity use; not an exhaustive
    ontology absence search.
  snapshot_sha256: 7bc8691f170f3826c82d090eb3b6e2e1891af968afefc2165005eb5f9b369664
- evidence_id: micro-go-0031472
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0031472
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0031472.raw
  accessed_at: '2026-11-03T23:17:02.177671Z'
  support: supports
  summary: GO:0031472 active=True; propanediol degradation polyhedral organelle. Definition
    read and compared with exact identity, parent class or activity use; not an exhaustive
    ontology absence search.
  snapshot_sha256: 7c601655cea95e1b27168a3fdc60cc7c95563063658707eae109f42d8c95f13e
- evidence_id: micro-go-0042910
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0042910
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0042910.raw
  accessed_at: '2026-11-03T23:17:02.255390Z'
  support: supports
  summary: GO:0042910 active=True; xenobiotic transmembrane transporter activity.
    Definition read and compared with exact identity, parent class or activity use;
    not an exhaustive ontology absence search.
  snapshot_sha256: 792fcd0cedd46aff4f9dd993a5455205040d8d9e943afd94fedfa113fe104c6b
- evidence_id: micro-go-0050215
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0050215
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0050215.raw
  accessed_at: '2026-11-03T23:17:02.477635Z'
  support: supports
  summary: GO:0050215 active=True; propanediol dehydratase activity. Definition read
    and compared with exact identity, parent class or activity use; not an exhaustive
    ontology absence search.
  snapshot_sha256: 7cfb96d359b6eccb6ffea425d29b38c203722bf7061eb284849bc6070f6e715c
- evidence_id: micro-go-0051144
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:0051144
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-0051144.raw
  accessed_at: '2026-11-03T23:17:02.719065Z'
  support: supports
  summary: GO:0051144 active=True; 1,2-propanediol catabolic process. Definition read
    and compared with exact identity, parent class or activity use; not an exhaustive
    ontology absence search.
  snapshot_sha256: 18ed6d4a95d91cb106e3cced6f151f975ef71156169186a7dc817852418367bf
- evidence_id: micro-go-1990204
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:1990204
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-1990204.raw
  accessed_at: '2026-11-03T23:17:02.773477Z'
  support: supports
  summary: GO:1990204 active=True; oxidoreductase complex. Definition read and compared
    with exact identity, parent class or activity use; not an exhaustive ontology
    absence search.
  snapshot_sha256: 65455700a96f92b5a0e970a241281d8877bd3aae89a237dc6e946c5ad1309527
- evidence_id: micro-go-1990281
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:1990281
  locator: Native exact OBO identifier, active status, label and complete definition;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/go-1990281.raw
  accessed_at: '2026-11-03T23:17:02.773555Z'
  support: supports
  summary: GO:1990281 active=True; efflux pump complex. Definition read and compared
    with exact identity, parent class or activity use; not an exhaustive ontology
    absence search.
  snapshot_sha256: 71705a0d0e916844f1131460c1bd3d656e06ee14b9dd49f2d37198e1334619c7
- evidence_id: micro-tax-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Native taxonomy identifier and name/lineage; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/tax-2.raw
  accessed_at: '2026-11-03T23:16:57.609038Z'
  support: supports
  summary: Exact native taxon identity checked; Bacteria, E. coli K-12 and Salmonella
    Typhimurium LT2 are not conflated with expression hosts or individual dataset
    strains.
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Native taxonomy identifier and name/lineage; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-03T23:16:58.662130Z'
  support: supports
  summary: Exact native taxon identity checked; Bacteria, E. coli K-12 and Salmonella
    Typhimurium LT2 are not conflated with expression hosts or individual dataset
    strains.
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-tax-99287
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/99287.json
  locator: Native taxonomy identifier and name/lineage; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/tax-99287.raw
  accessed_at: '2026-11-03T23:16:59.516219Z'
  support: supports
  summary: Exact native taxon identity checked; Bacteria, E. coli K-12 and Salmonella
    Typhimurium LT2 are not conflated with expression hosts or individual dataset
    strains.
  snapshot_sha256: 107ebfece75c5a7147abe7547dec9166f87ff267e6cbc3f67bea9ab9df694a59
- evidence_id: micro-eco-0353
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0000353
  locator: Exact active ECO:0000353 label and definition; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/extra/eco0000353.raw
  accessed_at: '2026-11-03T23:17:16.971000Z'
  support: supports
  summary: Physical interaction evidence used in manual assertion; this is not a formation-necessity
    assay code.
  snapshot_sha256: a85f179a3fca3a554fa914be25c4972efe9e487088eb9d16fdaf28961e63a057
- evidence_id: micro-cpx
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4263
  locator: Complete CPX-4263 native response; species, systematicName, functions,
    properties, participants/interactorAC/stoichiometry/bioRole, cross-references
    and evidenceType; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/cpx4263.raw
  accessed_at: '2026-11-03T23:17:06.536652Z'
  support: supports
  summary: 'Exact K-12 AcrAB-TolC heterododecamer: P0AE06/AcrA6, P31224/AcrB3, P02930/TolC3;
    exact EBI participant identifiers agree. Each bioRole is unspecified role, and
    ECO0000353 denotes physical interaction evidence. The response supports composition/function;
    it does not explicitly annotate essentiality.'
  snapshot_sha256: 71f09098a426c7a68e74d9e10882617e7eccc2ecb6e4eec05d92a6653992c31e
- evidence_id: micro-pdb
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/5V5S
  locator: Entry identity, primary citation, EM resolution and entity identifiers;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S.raw
  accessed_at: '2026-11-03T23:17:06.551276Z'
  support: supports
  summary: 5V5S is the 6.5 Angstrom apo AcrAB-TolC assembly linked to Wang2017. Metadata
    is not a new raw-map/coordinate reanalysis.
  snapshot_sha256: 033ab55d54cac2f6c3941468b74921b8cf4fafe5bc1460fa5ca869011002f3fb
- evidence_id: micro-pdb-entity1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/1
  locator: Entity identity/name, number_of_molecules, UniProt/SIFTS mappings and source/expression
    taxonomy; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S-entity1.raw
  accessed_at: '2026-11-03T23:17:06.624666Z'
  support: supports
  summary: 'Entity1: Outer membrane protein TolC; 3 copies; [''P02930'']. Source taxon562
    and construct metadata are not silently equated with native K-12 assembly.'
  snapshot_sha256: 597a64be51e1fdfb969a3dd78da161a7a7acaabacc8f1d316bc1372f885c9b07
- evidence_id: micro-pdb-entity2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/2
  locator: Entity identity/name, number_of_molecules, UniProt/SIFTS mappings and source/expression
    taxonomy; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S-entity2.raw
  accessed_at: '2026-11-03T23:17:06.644445Z'
  support: supports
  summary: 'Entity2: Multidrug efflux pump subunit AcrA; 6 copies; [''P0AE06'']. Source
    taxon562 and construct metadata are not silently equated with native K-12 assembly.'
  snapshot_sha256: e071580c679ea7dadfd1374d0c9bca8b54b280b3b6b278bf3b05ec9bf200a8c9
- evidence_id: micro-pdb-entity3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5V5S/3
  locator: Entity identity/name, number_of_molecules, UniProt/SIFTS mappings and source/expression
    taxonomy; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pdb5V5S-entity3.raw
  accessed_at: '2026-11-03T23:17:06.661234Z'
  support: supports
  summary: 'Entity3: Multidrug efflux pump subunit AcrB; 3 copies; [''P31224'']. Source
    taxon562 and construct metadata are not silently equated with native K-12 assembly.'
  snapshot_sha256: 441fca0757a9a81a7b93f3d70b067b712d48adcc3d0d4a891d7123c561381894
- evidence_id: micro-meta-doi-0
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1002/pro.2246%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-0.raw
  accessed_at: '2026-11-03T23:17:04.513710Z'
  support: partial
  summary: Bacterial microcompartment shells of diverse functional types possess pentameric
    vertex proteins.; PMID 23456886; DOI 10.1002/pro.2246. Abstract/metadata tier
    only; this row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 64ed4afafd558f38b74959e17f2b803c2316bf5edfc469559e0780842cce588e
- evidence_id: micro-meta-doi-1
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1038/s41467-020-15888-4%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-1.raw
  accessed_at: '2026-11-03T23:17:04.592729Z'
  support: partial
  summary: Decoding the stoichiometric composition and organisation of bacterial metabolosomes.;
    PMID 32332738; DOI 10.1038/s41467-020-15888-4. Abstract/metadata tier only; this
    row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 73a7e00444ef768d88772feae307319cc2ae625b49bffadf77658b9a4040610e
- evidence_id: micro-meta-doi-10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.184.5.1253-1261.2002%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-10.raw
  accessed_at: '2026-11-03T23:17:05.762772Z'
  support: partial
  summary: PduA is a shell protein of polyhedral organelles involved in coenzyme B(12)-dependent
    degradation of 1,2-propanediol in Salmonella enterica serovar typhimurium LT2.;
    PMID 11844753; DOI 10.1128/jb.184.5.1253-1261.2002. Abstract/metadata tier only;
    this row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 1ca7d932b98912d170c9aea3edf550cbb54401139341d1e446db5fd614c2de72
- evidence_id: micro-meta-doi-11
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.185.17.5086-5095.2003%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-11.raw
  accessed_at: '2026-11-03T23:17:05.876007Z'
  support: partial
  summary: Protein content of polyhedral organelles involved in coenzyme B12-dependent
    degradation of 1,2-propanediol in Salmonella enterica serovar Typhimurium LT2.;
    PMID 12923081; DOI 10.1128/jb.185.17.5086-5095.2003. Abstract/metadata tier only;
    this row does not certify uninspected body, figures or supplements.
  snapshot_sha256: cc14a22b7d0ad4814c6500452ec28b70b0aa471a79df9a6cdc4a7d4578293e8e
- evidence_id: micro-meta-doi-12
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.7554/eLife.24905%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-12.raw
  accessed_at: '2026-11-03T23:17:05.916391Z'
  support: partial
  summary: An allosteric transport mechanism for the AcrAB-TolC multidrug efflux pump.;
    PMID 28355133; DOI 10.7554/elife.24905. Abstract/metadata tier only; this row
    does not certify uninspected body, figures or supplements.
  snapshot_sha256: 90c3bf5085ffc2417e2973b05237256d19ef582289e3e2f129bcce3b18761f7f
- evidence_id: micro-meta-doi-2
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1038/s41467-021-24126-4%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-2.raw
  accessed_at: '2026-11-03T23:17:04.698370Z'
  support: partial
  summary: A catalog of the diversity and ubiquity of bacterial microcompartments.;
    PMID 34155212; DOI 10.1038/s41467-021-24126-4. Abstract/metadata tier only; this
    row does not certify uninspected body, figures or supplements.
  snapshot_sha256: d49833058cad922f93b12f0dde6458dc7071ef450c1ff0514a9fbb82f564950e
- evidence_id: micro-meta-doi-3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1038/s41467-022-30608-w%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-3.raw
  accessed_at: '2026-11-03T23:17:04.817799Z'
  support: partial
  summary: Biogenesis of a bacterial metabolosome for propanediol utilization.; PMID
    35614058; DOI 10.1038/s41467-022-30608-w. Abstract/metadata tier only; this row
    does not certify uninspected body, figures or supplements.
  snapshot_sha256: dca8a59738c8ac466005703c424fe46d1f2f99080ec2db30ee4411f560485879
- evidence_id: micro-meta-doi-4
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1073/pnas.0913199107%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-4.raw
  accessed_at: '2026-11-03T23:17:04.936249Z'
  support: partial
  summary: Short N-terminal sequences package proteins into bacterial microcompartments.;
    PMID 20308536; DOI 10.1073/pnas.0913199107. Abstract/metadata tier only; this
    row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 1096ff43a0c19f67bc5947c26474f7586cf519ffec0ff955d861c8b518f79963
- evidence_id: micro-meta-doi-5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.01925-07%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-5.raw
  accessed_at: '2026-11-03T23:17:05.126354Z'
  support: partial
  summary: Microcompartments for B12-dependent 1,2-propanediol degradation provide
    protection from DNA and cellular damage by a reactive metabolic intermediate.;
    PMID 18296526; DOI 10.1128/jb.01925-07. Abstract/metadata tier only; this row
    does not certify uninspected body, figures or supplements.
  snapshot_sha256: 9d54a51786dcd48fc694d5d0d10e9bde75aeb36c2b1430b3b2a041419ca17f98
- evidence_id: micro-meta-doi-6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.05661-11%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-6.raw
  accessed_at: '2026-11-03T23:17:05.239398Z'
  support: partial
  summary: The N-terminal region of the medium subunit (PduD) packages adenosylcobalamin-dependent
    diol dehydratase (PduCDE) into the Pdu microcompartment.; PMID 21821773; DOI 10.1128/jb.05661-11.
    Abstract/metadata tier only; this row does not certify uninspected body, figures
    or supplements.
  snapshot_sha256: f5bc6464e38dcdc5a2662a3f0bb88fd698a67f75bd2de875fa3ad7bf72c8845a
- evidence_id: micro-meta-doi-7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.06529-11%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-7.raw
  accessed_at: '2026-11-03T23:17:05.322143Z'
  support: partial
  summary: The PduM protein is a structural component of the microcompartments involved
    in coenzyme B(12)-dependent 1,2-propanediol degradation by Salmonella enterica.;
    PMID 22343294; DOI 10.1128/jb.06529-11. Abstract/metadata tier only; this row
    does not certify uninspected body, figures or supplements.
  snapshot_sha256: 7025f28611a9473eb7260da7e1282e1ee3e56c98d101cc67fda6110a35cbaab9
- evidence_id: micro-meta-doi-8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.179.21.6633-6639.1997%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-8.raw
  accessed_at: '2026-11-03T23:17:05.430846Z'
  support: partial
  summary: 'Propanediol utilization genes (pdu) of Salmonella typhimurium: three genes
    for the propanediol dehydratase.; PMID 9352910; DOI 10.1128/jb.179.21.6633-6639.1997.
    Abstract/metadata tier only; this row does not certify uninspected body, figures
    or supplements.'
  snapshot_sha256: d582ebb5a71bd693642dc032876e92b6ee21c71887546b16db945611588d3505
- evidence_id: micro-meta-doi-9
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=DOI%3A%2210.1128/JB.180.11.2915-2923.1998%22
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/doi-9.raw
  accessed_at: '2026-11-03T23:17:05.538531Z'
  support: partial
  summary: Characterization of the hca cluster encoding the dioxygenolytic pathway
    for initial catabolism of 3-phenylpropionic acid in Escherichia coli K-12.; PMID
    9603882; DOI 10.1128/jb.180.11.2915-2923.1998. Abstract/metadata tier only; this
    row does not certify uninspected body, figures or supplements.
  snapshot_sha256: ed275e8c7e2bc729a67714f7d0f23a91f7d5373f1b9070ea71fc0bc6d29f8a65
- evidence_id: micro-meta-pmid-10498708
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A10498708%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-10498708.raw
  accessed_at: '2026-11-03T23:17:03.366606Z'
  support: partial
  summary: The propanediol utilization (pdu) operon of Salmonella enterica serovar
    Typhimurium LT2 includes genes necessary for formation of polyhedral organelles
    involved in coenzyme B(12)-dependent 1, 2-propanediol degradation.; PMID 10498708;
    DOI 10.1128/jb.181.19.5967-5975.1999. Abstract/metadata tier only; this row does
    not certify uninspected body, figures or supplements.
  snapshot_sha256: c438fb4c26bf0457a751126866aa1483001c07903c0127ccb90a29a0e62de69d
- evidence_id: micro-meta-pmid-11844753
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A11844753%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-11844753.raw
  accessed_at: '2026-11-03T23:17:03.368744Z'
  support: partial
  summary: PduA is a shell protein of polyhedral organelles involved in coenzyme B(12)-dependent
    degradation of 1,2-propanediol in Salmonella enterica serovar typhimurium LT2.;
    PMID 11844753; DOI 10.1128/jb.184.5.1253-1261.2002. Abstract/metadata tier only;
    this row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 2c05f58a005597aff79f331f95fd2f1c30335f12d1c99c4ded17414deb9d5759
- evidence_id: micro-meta-pmid-12923081
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A12923081%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-12923081.raw
  accessed_at: '2026-11-03T23:17:03.503274Z'
  support: partial
  summary: Protein content of polyhedral organelles involved in coenzyme B12-dependent
    degradation of 1,2-propanediol in Salmonella enterica serovar Typhimurium LT2.;
    PMID 12923081; DOI 10.1128/jb.185.17.5086-5095.2003. Abstract/metadata tier only;
    this row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 6ae01885ea4a493de328b134491039ee59d3fc8c1eb26e7b70e68da278695174
- evidence_id: micro-meta-pmid-21239588
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A21239588%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-21239588.raw
  accessed_at: '2026-11-03T23:17:03.702805Z'
  support: partial
  summary: Genetic analysis of the protein shell of the microcompartments involved
    in coenzyme B12-dependent 1,2-propanediol degradation by Salmonella.; PMID 21239588;
    DOI 10.1128/jb.01473-10. Abstract/metadata tier only; this row does not certify
    uninspected body, figures or supplements.
  snapshot_sha256: f559c7d943c0d8fbed91269c25188e696cf46c3d7557b0db7a8f337386d1d6db
- evidence_id: micro-meta-pmid-22343294
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A22343294%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-22343294.raw
  accessed_at: '2026-11-03T23:17:03.920509Z'
  support: partial
  summary: The PduM protein is a structural component of the microcompartments involved
    in coenzyme B(12)-dependent 1,2-propanediol degradation by Salmonella enterica.;
    PMID 22343294; DOI 10.1128/jb.06529-11. Abstract/metadata tier only; this row
    does not certify uninspected body, figures or supplements.
  snapshot_sha256: e0243fa30530b2609cafd77fb1d4c8d9adba03b53b334918203b76a780236e34
- evidence_id: micro-meta-pmid-24747050
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A24747050%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-24747050.raw
  accessed_at: '2026-11-03T23:17:03.968626Z'
  support: partial
  summary: Alanine scanning mutagenesis identifies an asparagine-arginine-lysine triad
    essential to assembly of the shell of the Pdu microcompartment.; PMID 24747050;
    DOI 10.1016/j.jmb.2014.04.012. Abstract/metadata tier only; this row does not
    certify uninspected body, figures or supplements.
  snapshot_sha256: 5de3f912eb66ffbd298cdec3ea7bee06f709a5d9cbe2633cb7ae124cb5f94f40
- evidence_id: micro-meta-pmid-27063436
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A27063436%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-27063436.raw
  accessed_at: '2026-11-03T23:17:04.014594Z'
  support: partial
  summary: Engineering formation of multiple recombinant Eut protein nanocompartments
    in E. coli.; PMID 27063436; DOI 10.1038/srep24359. Abstract/metadata tier only;
    this row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 95e1bcbbc1e12bfaf4da2216de746cdb8e68eaee83501a4cf38cf4d0f3fff50f
- evidence_id: micro-meta-pmid-28355133
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A28355133%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-28355133.raw
  accessed_at: '2026-11-03T23:17:04.165726Z'
  support: partial
  summary: An allosteric transport mechanism for the AcrAB-TolC multidrug efflux pump.;
    PMID 28355133; DOI 10.7554/elife.24905. Abstract/metadata tier only; this row
    does not certify uninspected body, figures or supplements.
  snapshot_sha256: c07cb80659dda6230b0012de385720cccca91761ce6f39e8159e0cd8451d2525
- evidence_id: micro-meta-pmid-9603882
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=10&query=EXT_ID%3A9603882%20AND%20SRC%3AMED
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/pmid-9603882.raw
  accessed_at: '2026-11-03T23:17:04.309228Z'
  support: partial
  summary: Characterization of the hca cluster encoding the dioxygenolytic pathway
    for initial catabolism of 3-phenylpropionic acid in Escherichia coli K-12.; PMID
    9603882; DOI 10.1128/jb.180.11.2915-2923.1998. Abstract/metadata tier only; this
    row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 025edb072840a073d0ca912feafd045eed4a394d671a6ef1781861f88ba00fa4
- evidence_id: micro-meta-fan2012-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1073/pnas.1207516109&format=json&resultType=core&pageSize=10
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/fan2012-meta.raw
  accessed_at: '2026-11-03T23:20:20.491575Z'
  support: partial
  summary: Interactions between the termini of lumen enzymes and shell proteins mediate
    enzyme encapsulation into bacterial microcompartments.; PMID 22927404; DOI 10.1073/pnas.1207516109.
    Abstract/metadata tier only; this row does not certify uninspected body, figures
    or supplements.
  snapshot_sha256: 635409bc4d1be70261e8015573264ea5247a3902be9e4dae9b8fa13e16c3b140
- evidence_id: micro-meta-pduu2008-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18786396%20AND%20SRC:MED&format=json&resultType=core&pageSize=10
  locator: Exact Europe PMC native article metadata and complete abstract only; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/pduu2008-meta.raw
  accessed_at: '2026-11-03T23:21:47.661731Z'
  support: partial
  summary: Structure of the PduU shell protein from the Pdu microcompartment of Salmonella.;
    PMID 18786396; DOI 10.1016/j.str.2008.05.013. Abstract/metadata tier only; this
    row does not certify uninspected body, figures or supplements.
  snapshot_sha256: 48fcb5660973d1e86563fa93e9fa995fe15d78054e7963e5916c76ed64896293
- evidence_id: micro-yang2020
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7181861.1/PMC7181861.1.xml
  locator: Sec4 complete direct paragraphs and Tables1–2/captions; Sec9 strains/growth
    and Sec12 purification; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/PMC7181861.raw
  accessed_at: '2026-11-03T23:17:06.061000Z'
  support: supports
  summary: LT2 induced purified Pdu particles, QconCAT-based composition and condition-dependent
    deletion observations. Table1 distinguishes trimeric PduB/PduT from hexameric
    PduU. Absolute counts use calibration assumptions including60PduN; no independent
    vertex-count or raw-spectrum reanalysis.
  snapshot_sha256: 027a9e17978be0a430b7e343c210d8f02696487391172f33a97fa1367d83cc63
- evidence_id: micro-yang2022
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9132943.1/PMC9132943.1.xml
  locator: Sec5,6,8,9,12,16 complete direct paragraphs and embedded captions; formerly
    clipped Sec5 spatial-separation paragraph independently reread; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/PMC9132943.raw
  accessed_at: '2026-11-03T23:17:06.201345Z'
  support: supports
  summary: LT2 genetics/tagged imaging support independent shell/cargo assemblies,
    PduB1–37 linkage, PduM-associated proposed bridge and alternative assembly pathways.
    PduCDE is major cargo; EP-driven condensation and precise molecular contacts remain
    model-qualified. No images/movies/supplements inspected.
  snapshot_sha256: bb36c6d2fefbed94231fcba0ce4e2517c3b23e25cb5fe4c580db9e21f4f5888e
- evidence_id: micro-havemann2002
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC134856/
  locator: Sec3/Table1 and Sec19–22 complete text/embedded captions; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC134856.raw
  accessed_at: '2026-11-03T23:17:37.688961Z'
  support: supports
  summary: LT2 induction/immunogold and pduA mutant/complementation experiments support
    shell localization and condition-specific assembly phenotype. E. coli expression
    strains remain distinct; no raw image pixels inspected.
  snapshot_sha256: 5994dd3f15bfda20e2d1cc5925e7c3a26f0fe7704861249d1a4dd6b4aa3acfee
- evidence_id: micro-havemann2003
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC180998/
  locator: Sec3,15,18,21,22,24,25 complete text/tables/captions; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC180998.raw
  accessed_at: '2026-11-03T23:17:37.689333Z'
  support: supports
  summary: Purified induced LT2 particles,100–150nm/3–4nm shell, protein identity
    analyses and co-purification support shell/cargo membership. Protein presence
    is not direct binding or a full causal assembly trajectory; absent proteins in
    this preparation are not universal absence.
  snapshot_sha256: 53f23c405b8ee5324cc2bbfd0fab2d25b86e5239a9987ab566600f284052089e
- evidence_id: micro-fan2010
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2867708/
  locator: Sec2–5,7, Discussion s2 and strains sec11 complete text/captions; retained
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC2867708.raw
  accessed_at: '2026-11-03T23:17:37.689484Z'
  support: supports
  summary: PduP N-terminal truncations and reporter targeting establish encapsulation
    sequence function in LT2 derivatives; Discussion explicitly leaves the specific
    shell receptor mechanism uncertain.
  snapshot_sha256: 4c179dd714dd6c90c93604904e381ac869f474314d1313dc1eb54ba2dcf477bd
- evidence_id: micro-fan2011
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3187188/
  locator: Sec11–15 complete Results/Discussion text, Tables2 and embedded captions;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC3187188.raw
  accessed_at: '2026-11-03T23:17:37.689446Z'
  support: supports
  summary: PduD terminal sequence targets PduCDE and heterologous proteins; recovered
    particles from delta-pduCDE distinguish catalytic cargo from shell formation.
    No general BMC-T receptor was measured.
  snapshot_sha256: dd89d458cc9fa992e8411ca4a1c03257b93d31df42f1adc2bf6a73ec092bbf87
- evidence_id: micro-fan2012
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3443165/
  locator: Sec2–4, Discussion s2 and purification/pull-down Methods sec11 complete
    text/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/fan2012-body.raw
  accessed_at: '2026-11-03T23:21:47.659524Z'
  support: supports
  summary: Recombinant E. coli BL21(DE3) Rosetta2 pull-downs tested PduP against nine
    shell proteins and identified PduA/PduJ interactions; terminal specificity and
    native targeting context support a specific PduP mechanism, not reassignment of
    PduD or the entire enzyme core by analogy.
  snapshot_sha256: 42a973ed612e9679e03acbec4c90a3f3867fb0f4139b9e7992925f102dc53259
- evidence_id: micro-sinha2012
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3318458/
  locator: Sec16–21 complete sequence/distribution, deletion/complementation, biochemical
    localization and Discussion text/captions; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC3318458.raw
  accessed_at: '2026-11-03T23:17:37.689397Z'
  support: supports
  summary: PduM is a low-abundance structural component of LT2 Pdu particles. Deletion
    impairs normal assembly and overexpression perturbs it; specific vertex/bridge
    geometry is proposed, not measured atomic structure. Native exact family now resolves
    the current label-only gap.
  snapshot_sha256: e0a046f88c962271fde462816c491272bf51cfae443960c0b6209fd83d31fe9e
- evidence_id: micro-sampson2008
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2293232/
  locator: Sec3/Table1,Sec12,Sec17/Table3 and Discussion sec18 complete text/captions;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC2293232.raw
  accessed_at: '2026-11-03T23:17:38.222127Z'
  support: supports
  summary: LT2-derived MCP-minus mutants accumulate propionaldehyde with growth arrest
    and increased mutagenesis under stated culture conditions. Supports toxicity-protection
    function; volatility and mechanism are condition-dependent.
  snapshot_sha256: 776bf1154da22a50703541cfde93f89bf95786f753e4f3aafc5f76f05ab340c7
- evidence_id: micro-diaz1998
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC107259/
  locator: Sec2,7,10/Table1,12 complete Methods and Results text; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/fallback/PMC107259.raw
  accessed_at: '2026-11-03T23:17:37.688706Z'
  support: supports
  summary: K-12 MC1061/ED1061 and recombinant Salmonella experiments support hca-cluster
    pathway function; HcaA1/A2/CD subunit roles were primarily sequence-based classIIB
    assignments. Whole-cell DHPP production includes downstream HcaB and is not a
    purified individual electron-transfer assay.
  snapshot_sha256: 3a4a627538bcee0afc310c792e10bd1e6e7cbcbd311ea966eb7b3a78a7d1f886
- evidence_id: micro-wang2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5404916.1/PMC5404916.1.xml
  locator: s2-1,s2-2,s2-3,s3,s4-1,s4-2,s4-9 complete text including embedded captions;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/extra/PMC5404916.raw
  accessed_at: '2026-11-03T23:17:16.543450Z'
  support: supports
  summary: Engineered disulfide-stabilized AcrAB-TolC apo5V5S differs from ligand-state
    AcrABZ fusion preparations. SixAcrA/threeAcrB/threeTolC architecture, C43(DE3)
    expression and coarse transport model supported; no independent formation-essentiality
    depletion experiment or new raw-map/pixel analysis.
  snapshot_sha256: 6b1cde98d3290310f97ca256ec6793f25f31f5a33976cd10bc88612c24db634c
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue JSON; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-03T23:17:06.503752Z'
  support: supports
  summary: All returned organism/dataset entries inspected. E. coli and Salmonella
    hosts have represented datasets; this is a positive applicability match, not a
    claim that module results prove organelle biology.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB /api/datasets complete response on 2026-11-03T23:17:06.503752Z;
    inspected all20 organism rows/28 organism-dataset pairs, selecting e_coli/precise1k
    and s_enterica/core. No all-dataset downstream census or universal absence inference.
- evidence_id: micro-e_coli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete selected dataset metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/e_coli-meta.raw
  accessed_at: '2026-11-03T23:20:20.491118Z'
  support: supports
  summary: 'e_coli/precise1k: 4257genes,201modules,1035samples; strains BW25113, DGF-298,
    GMOS, MG1655, W3110. This is multi-strain transcriptomic context, not an exact
    experimental-strain substitute.'
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-e_coli-genes
  kind: search
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=10000
  locator: Complete selected gene table; exact native loci/names/accession joins;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter/e_coli-genes.raw
  accessed_at: '2026-11-03T23:18:00.340139Z'
  support: supports
  summary: 4257 returned genes inspected by exact requested names/loci. PduB STM2039
    is present even when native display name differs; STM2045/PduJ is not in this
    returned gene table, so its gene-module all-zero response is not certified negative
    membership evidence.
  snapshot_sha256: db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27
  search_scope: iModulonDB official genes endpoint for e_coli/precise1k, 2026-11-03T23:18:00.340139Z;
    limit10000, complete returned 4257 rows; exact local filtering for PduA/B/C/D/E/J/K/M/N/T/U
    or HcaE/F/C/D,AcrA/B,TolC and their native loci/accessions. Only these two selected
    datasets, not all organism datasets.
- evidence_id: micro-e_coli-module-list
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete returned selected module list, names/regulator/function/count
    fields; no generated narrative used; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/e_coli-imodulons.raw
  accessed_at: '2026-11-03T23:20:20.491387Z'
  support: supports
  summary: Selected e_coli/precise1k module list inspected to resolve exact module
    keys and native summaries. Only computational expression context.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: micro-s_enterica-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/s_enterica/core/meta
  locator: Complete selected dataset metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/s_enterica-meta.raw
  accessed_at: '2026-11-03T23:20:20.491476Z'
  support: supports
  summary: 's_enterica/core: 3886genes,115modules,533samples; strains 14028S, D23580,
    LT2, SL1344, ST4/74, UK-1. This is multi-strain transcriptomic context, not an
    exact experimental-strain substitute.'
  snapshot_sha256: bb71cfd723e9b6b60a3ee5ad0db8278c92907336ac28794d83a3822955bbc054
- evidence_id: micro-s_enterica-genes
  kind: search
  reference: https://imodulondb.org/api/genes?organism=s_enterica&dataset=core&limit=10000
  locator: Complete selected gene table; exact native loci/names/accession joins;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter/s_enterica-genes.raw
  accessed_at: '2026-11-03T23:18:00.340324Z'
  support: supports
  summary: 3886 returned genes inspected by exact requested names/loci. PduB STM2039
    is present even when native display name differs; STM2045/PduJ is not in this
    returned gene table, so its gene-module all-zero response is not certified negative
    membership evidence.
  snapshot_sha256: 7bdbfb15bedb14be78f8df9657f55d8f9dfcb76382648087b777f5086ff91eaf
  search_scope: iModulonDB official genes endpoint for s_enterica/core, 2026-11-03T23:18:00.340324Z;
    limit10000, complete returned 3886 rows; exact local filtering for PduA/B/C/D/E/J/K/M/N/T/U
    or HcaE/F/C/D,AcrA/B,TolC and their native loci/accessions. Only these two selected
    datasets, not all organism datasets.
- evidence_id: micro-s_enterica-module-list
  kind: database
  reference: https://imodulondb.org/api/datasets/s_enterica/core/imodulons
  locator: Complete returned selected module list, names/regulator/function/count
    fields; no generated narrative used; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/adapter2/s_enterica-imodulons.raw
  accessed_at: '2026-11-03T23:20:20.491532Z'
  support: supports
  summary: Selected s_enterica/core module list inspected to resolve exact module
    keys and native summaries. Only computational expression context.
  snapshot_sha256: a077947057c7bdd41de80172fd0268f9eddaee6c41e43717ecaa96b2070f6dcd
- evidence_id: micro-modules-e_coli-b0462
  kind: search
  reference: https://imodulondb.org/api/genes/b0462/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b0462.raw
  accessed_at: '2026-11-03T23:21:47.476773Z'
  support: context_only
  summary: 'e_coli/precise1k/b0462: 201module rows; threshold memberships [(22, ''SoxS'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: 1a7b6998e851bf55e334f591b578902dba107e7e6f4a9807da3c0116c19cb7c2
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b0462/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.476773Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-e_coli-b0463
  kind: search
  reference: https://imodulondb.org/api/genes/b0463/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b0463.raw
  accessed_at: '2026-11-03T23:21:47.477071Z'
  support: context_only
  summary: 'e_coli/precise1k/b0463: 201module rows; threshold memberships [(22, ''SoxS'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: 7b4258beeebd7c86c64160029c2c94c500b68f1222187ea3bd5ba57cdd125506
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b0463/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.477071Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-e_coli-b2538
  kind: search
  reference: https://imodulondb.org/api/genes/b2538/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2538.raw
  accessed_at: '2026-11-03T23:21:47.477212Z'
  support: context_only
  summary: 'e_coli/precise1k/b2538: 201module rows; threshold memberships []. No membership
    or nonmembership establishes physical localization, stoichiometry or necessity.'
  snapshot_sha256: 2b59990d1a9dd9b50f2839b67696006607af0c86ae02e05547266537e2f5410a
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b2538/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.477212Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-e_coli-b2539
  kind: search
  reference: https://imodulondb.org/api/genes/b2539/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2539.raw
  accessed_at: '2026-11-03T23:21:47.477257Z'
  support: context_only
  summary: 'e_coli/precise1k/b2539: 201module rows; threshold memberships []. No membership
    or nonmembership establishes physical localization, stoichiometry or necessity.'
  snapshot_sha256: c54d677b27ed5cb6f7f536dfacb97cb1678cad3eaacabb94a8229874b05d177a
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b2539/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.477257Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-e_coli-b2540
  kind: search
  reference: https://imodulondb.org/api/genes/b2540/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2540.raw
  accessed_at: '2026-11-03T23:21:47.477295Z'
  support: context_only
  summary: 'e_coli/precise1k/b2540: 201module rows; threshold memberships []. No membership
    or nonmembership establishes physical localization, stoichiometry or necessity.'
  snapshot_sha256: 3d8ebaef1bac26aaa59a6b3cd78bb84867e2384dff4c320c79cde7abc9893d23
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b2540/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.477295Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-e_coli-b2542
  kind: search
  reference: https://imodulondb.org/api/genes/b2542/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b2542.raw
  accessed_at: '2026-11-03T23:21:47.541794Z'
  support: context_only
  summary: 'e_coli/precise1k/b2542: 201module rows; threshold memberships []. No membership
    or nonmembership establishes physical localization, stoichiometry or necessity.'
  snapshot_sha256: b304409594705c2c252d41a710e8e62da7bd5b018e82dfa009d6e0b15a272fe5
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b2542/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.541794Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-e_coli-b3035
  kind: search
  reference: https://imodulondb.org/api/genes/b3035/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/e_coli-b3035.raw
  accessed_at: '2026-11-03T23:21:47.477155Z'
  support: context_only
  summary: 'e_coli/precise1k/b3035: 201module rows; threshold memberships [(22, ''SoxS'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: 5db135045efa59ff66876f57b3e6ebe3c25375196fac7f1a410c36cb4befced3
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/b3035/imodulons?organism=e_coli&dataset=precise1k
    accessed2026-11-03T23:21:47.477155Z; read all201 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2038
  kind: search
  reference: https://imodulondb.org/api/genes/STM2038/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2038.raw
  accessed_at: '2026-11-03T23:21:47.541882Z'
  support: context_only
  summary: 's_enterica/core/STM2038: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: b83eaa7b93337b11213736b7f9529bd00a9082453ebbb6b2358cf1b73f4f8683
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2038/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.541882Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2039
  kind: search
  reference: https://imodulondb.org/api/genes/STM2039/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2039.raw
  accessed_at: '2026-11-03T23:21:47.544344Z'
  support: context_only
  summary: 's_enterica/core/STM2039: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: a7f30106bb9c40bcd1831a850a24a4e660656e288d251b736d7e07889a128955
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2039/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.544344Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2040
  kind: search
  reference: https://imodulondb.org/api/genes/STM2040/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2040.raw
  accessed_at: '2026-11-03T23:21:47.546526Z'
  support: context_only
  summary: 's_enterica/core/STM2040: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: 37951c1c0aae6835bb04f82ca4fab060feaaebb296f7b0afe7a7712058552640
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2040/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.546526Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2041
  kind: search
  reference: https://imodulondb.org/api/genes/STM2041/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2041.raw
  accessed_at: '2026-11-03T23:21:47.546644Z'
  support: context_only
  summary: 's_enterica/core/STM2041: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: ba6b2494fa53c43dfb4a3b58d4bf563c39977143b2ee514157030ad5ccba9a8b
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2041/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.546644Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2042
  kind: search
  reference: https://imodulondb.org/api/genes/STM2042/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2042.raw
  accessed_at: '2026-11-03T23:21:47.550841Z'
  support: context_only
  summary: 's_enterica/core/STM2042: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: 91b5d3dd0f09e2ac5cde5bfc91dbccf9b72cf0ca52b87fb82ca10f38e2802013
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2042/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.550841Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2045
  kind: search
  reference: https://imodulondb.org/api/genes/STM2045/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2045.raw
  accessed_at: '2026-11-03T23:21:47.605183Z'
  support: context_only
  summary: 's_enterica/core/STM2045: 115module rows; threshold memberships []. STM2045
    is absent from selected gene table; all-zero fallback is not negative biological
    evidence.'
  snapshot_sha256: c4f9cb929d8934ff162109dc653a56a63f6b62175ca56998529f55e9a420b77a
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2045/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.605183Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2046
  kind: search
  reference: https://imodulondb.org/api/genes/STM2046/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2046.raw
  accessed_at: '2026-11-03T23:21:47.605265Z'
  support: context_only
  summary: 's_enterica/core/STM2046: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: 380321efabdb6b121d697b47919f82ed7360ea8fb8af5791c2c14a90a4e9a44c
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2046/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.605265Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2048
  kind: search
  reference: https://imodulondb.org/api/genes/STM2048/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2048.raw
  accessed_at: '2026-11-03T23:21:47.605328Z'
  support: context_only
  summary: 's_enterica/core/STM2048: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: d93048d2c2b1d9240d5e52511faa0dcc283329bc69c12f0021a9b82799f9b23b
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2048/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.605328Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2049
  kind: search
  reference: https://imodulondb.org/api/genes/STM2049/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2049.raw
  accessed_at: '2026-11-03T23:21:47.605395Z'
  support: context_only
  summary: 's_enterica/core/STM2049: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: f2b115bf658d8b32acdb2434984a9664c6b31a7a5c9d3858533cdb9e3a50ec07
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2049/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.605395Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2054
  kind: search
  reference: https://imodulondb.org/api/genes/STM2054/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2054.raw
  accessed_at: '2026-11-03T23:21:47.605891Z'
  support: context_only
  summary: 's_enterica/core/STM2054: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: eb491dddc8538e3cc78c4c1c6c89ef77b0da7db94f367d606909d01a357ae22d
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2054/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.605891Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-modules-s_enterica-STM2055
  kind: search
  reference: https://imodulondb.org/api/genes/STM2055/imodulons?organism=s_enterica&dataset=core
  locator: Complete per-gene module weights/threshold flags; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/downstream/s_enterica-STM2055.raw
  accessed_at: '2026-11-03T23:21:47.605978Z'
  support: context_only
  summary: 's_enterica/core/STM2055: 115module rows; threshold memberships [(33, ''pdu'')].
    No membership or nonmembership establishes physical localization, stoichiometry
    or necessity.'
  snapshot_sha256: cbb1e2e07ce52ceeea220386a4fd929dce83905bfca19652cca6c4ddba69ff20
  search_scope: Official iModulonDB exact locus endpoint https://imodulondb.org/api/genes/STM2055/imodulons?organism=s_enterica&dataset=core
    accessed2026-11-03T23:21:47.605978Z; read all115 returned module rows, native
    in_imodulon threshold flags. No activity reanalysis or wider dataset search.
- evidence_id: micro-e_coli-module22
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22
  locator: Native module name/regulator/function, threshold, full gene membership
    list; generated ai_summary explicitly excluded and activities not interpreted;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/e_coli-module22.raw
  accessed_at: '2026-11-03T23:22:41.709873Z'
  support: context_only
  summary: 'e_coli/precise1k/22: SoxS, 117genes. AcrA b0463,AcrB b0462,TolC b3035
    have SoxS-module membership. Computational expression association only.'
  snapshot_sha256: 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703
- evidence_id: micro-s_enterica-module33
  kind: database
  reference: https://imodulondb.org/api/imodulons/s_enterica/core/33
  locator: Native module name/regulator/function, threshold, full gene membership
    list; generated ai_summary explicitly excluded and activities not interpreted;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-microtubule/queries/s_enterica-module33.raw
  accessed_at: '2026-11-03T23:22:41.783168Z'
  support: context_only
  summary: 's_enterica/core/33: pdu, 19genes. Ten selected Pdu loci meet module33
    threshold; PduJ missing gene-table coverage is not a contradictory result. Computational
    expression association only.'
  snapshot_sha256: e390f7dd30002a785cad9f610e956ccca4bd48fda7b79a6062207f3d150fda84
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical command receipt only; no fresh runner execution
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Actual00:49Z run exited1 with PermissionError on pyvenv.cfg. Current review
    uses fresh inspected official catalogue/metadata/gene/module fallback. Historical
    unavailability is not represented as a current successful adapter execution.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-propanediol_degradation_polyhedral_organelle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T23:17:24.994577Z'
  support: supports
  summary: 11 reviewed examples; five GENE_OR_PROTEIN nodes:4COVERED+1UNANCHORED_WITH_UNIPROT.
    STRUCTURE-typed PduCDE omitted from this typed-node summary; its three examples
    separately verified. Native pass verifies its implemented identity/coverage contract,
    not physical membership, correct molecular class, direct binding or essentiality.
  snapshot_sha256: 12292e392b64fafbf1ccf42b60292fdb05042c57e75500cd1382dead3172691b
- evidence_id: micro-native-propanediol_degradation_polyhedral_organelle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-causal.log
    SHA256 21b89ef20c41b68d80b3fb47dad935957101d412e816fd03c3b57f24706d4b84
  accessed_at: '2026-11-03T23:17:25.408127Z'
  support: supports
  summary: 11 reviewed examples; five GENE_OR_PROTEIN nodes:4COVERED+1UNANCHORED_WITH_UNIPROT.
    STRUCTURE-typed PduCDE omitted from this typed-node summary; its three examples
    separately verified. Native pass verifies its implemented identity/coverage contract,
    not physical membership, correct molecular class, direct binding or essentiality.
  snapshot_sha256: 17601c5b4f708c1ece8950d4354fb7f617e11942d8c707fdfe3fc95fcee0fa78
- evidence_id: micro-native-3_phenylpropionate_dioxygenase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T23:17:33.792850Z'
  support: supports
  summary: 4reviewed examples and4COVERED typed nodes. Native pass verifies its implemented
    identity/coverage contract, not physical membership, correct molecular class,
    direct binding or essentiality.
  snapshot_sha256: b3e97fae861e7901b6201302a48d26dac25385d3e31efa197a1e70aceb9ee970
- evidence_id: micro-native-3_phenylpropionate_dioxygenase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-causal.log
    SHA256 643c232d1c030efc53020a6851cb8fbf86dc4243c87cbb2a971fc41c067a79d0
  accessed_at: '2026-11-03T23:17:34.203105Z'
  support: supports
  summary: 4reviewed examples and4COVERED typed nodes. Native pass verifies its implemented
    identity/coverage contract, not physical membership, correct molecular class,
    direct binding or essentiality.
  snapshot_sha256: 1ba8de8a956350a38e582954057776d2d660873b1c7f1e87c3d1068304726f55
- evidence_id: micro-native-acrab_tolc_multidrug_efflux_transport_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T23:17:36.926779Z'
  support: supports
  summary: 3reviewed examples and3COVERED typed nodes. Native pass verifies its implemented
    identity/coverage contract, not physical membership, correct molecular class,
    direct binding or essentiality.
  snapshot_sha256: 25fdc441697eb030b354a824dc38faa7c63dbc84abf3843fde0af7264b58a3fc
- evidence_id: micro-native-acrab_tolc_multidrug_efflux_transport_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal-receipt.json
  locator: Actual receipt and stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal.log
    SHA256 d006bc9e9c113add93b358d1af24eb05ca200ab4c477df0f514cbcca129b7518
  accessed_at: '2026-11-03T23:17:37.335133Z'
  support: supports
  summary: 3reviewed examples and3COVERED typed nodes. Native pass verifies its implemented
    identity/coverage contract, not physical membership, correct molecular class,
    direct binding or essentiality.
  snapshot_sha256: 890e74e16fcf90f6caf48784c953d9669377784e941390e3fded0de1b583cd66
- evidence_id: micro-acr-independent-challenge
  kind: prior_review
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/adversary-plaque/acrab-source-attribution-challenge.json
  locator: Complete independent bounded source-attribution challenge receipt
  accessed_at: '2026-11-03T23:28:45.187645Z'
  support: supports
  summary: Independent second reviewer confirms only the new CPX source-attribution
    defect. The defining intact-complex inference and existing ESSENTIAL flags are
    not rejected; no depletion assay is demanded and contributes-to edges remain valid.
  snapshot_sha256: 4dc592793986a65aceaee73ea0983effeb6a8bbe94771fbff3b2d58d765a95d6
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T23:21:35.742724Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 5199a3c40e8439735b2ee8d96a0446665974e5a0ea409cf9d342e3336db64780
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T23:17:04.545980Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T23:16:41.990305Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T23:16:37.894505Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T23:16:42.140268Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: bc12b1285f5747707643f7a98e03dbb3a6c88fb062ad49f99db9cb42ececf3d2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T23:29:27Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 3f4ca9498b0f3bbdcd92e86f318f5f0a5929835f1c02514dc3512b53bea9e862
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T23:17:59.641947Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 086a3227070c68e1f1c2d4f797e4c89a80b2e9b08f17f93f169331d13d2a3e83
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, exact SHA256 reverified during PR2380
    synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-propanediol_degradation_polyhedral_organelle-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:24.994577Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-propanediol_degradation_polyhedral_organelle-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/propanediol_degradation_polyhedral_organelle-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:25.408127Z'
  support: context_only
  snapshot_sha256: 21b89ef20c41b68d80b3fb47dad935957101d412e816fd03c3b57f24706d4b84
  summary: 11 represented protein examples; 5 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-chloroplast_nucleoid-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:25.808825Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-chloroplast_nucleoid-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/chloroplast_nucleoid-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:26.211023Z'
  support: context_only
  snapshot_sha256: 1ad288cda6d8baaea929dfe9142bcf9ba8b7e4f320f7678340a454924e46c0b8
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-kinetoplast-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:26.616907Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-kinetoplast-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/kinetoplast-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:27.018292Z'
  support: context_only
  snapshot_sha256: 8676810ab064da164f9b59c268811a6c76f4dbc7dc0297ac3e4089301cd09f4d
  summary: 0 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_nucleoid-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:28.096580Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-mitochondrial_nucleoid-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/mitochondrial_nucleoid-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:28.501894Z'
  support: context_only
  snapshot_sha256: f99e2411914f5015315ed9c67ad81727e914466b91175451cb0ca9ca924f37f8
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-nucleoid-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:29.874176Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-nucleoid-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/nucleoid-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:30.280335Z'
  support: context_only
  snapshot_sha256: 060c0334ea540c0999476872bdce276671f1ffa111deee448f7ebcb5fe1291a1
  summary: 7 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_nucleoid-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:30.679026Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-plastid_nucleoid-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/plastid_nucleoid-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:31.082068Z'
  support: context_only
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: 0 represented protein examples; 0 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-1_3_beta_d_glucan_synthase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:32.249837Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-1_3_beta_d_glucan_synthase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/1_3_beta_d_glucan_synthase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:32.659871Z'
  support: context_only
  snapshot_sha256: e5e246afc40662210eb530ad32b4b670cccbcf512c0f14cb2d7c4689b7445665
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-3_phenylpropionate_dioxygenase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:33.792850Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-3_phenylpropionate_dioxygenase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/3_phenylpropionate_dioxygenase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:34.203105Z'
  support: context_only
  snapshot_sha256: 643c232d1c030efc53020a6851cb8fbf86dc4243c87cbb2a971fc41c067a79d0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-acf_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:35.308337Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-acf_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acf_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:35.713055Z'
  support: context_only
  snapshot_sha256: e34e9c8cebb57c5f572bee3aa6dcdb3271c14c814833d2bbe620d8bddfa7862f
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:36.926779Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2380/acrab_tolc_multidrug_efflux_transport_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-03T23:17:37.335133Z'
  support: context_only
  snapshot_sha256: d006bc9e9c113add93b358d1af24eb05ca200ab4c477df0f514cbcca129b7518
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: septin-chloroplast_nucleoid-identity
  area: identity
  topic: Exact structure versus protein/DNA material identity
  outcome: supported
  summary: GO0042644 is exact; is_a plastid nucleoid and part_of chloroplast stroma
    are supported by distinct typed native relations.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-generic-nucleoid-context
- assessment_id: septin-chloroplast_nucleoid-components
  area: grounding
  topic: Constituent boundaries and exact family/material scope
  outcome: supported
  summary: Chloroplast DNA and the Chlamydomonas-HLP-represented HU-like class are
    supported. IPR000119 is broader HU/IHF family context, not an exact chloroplast-localized
    class; CreCNS is a documented additional factor but absence from a deliberately
    bounded optional inventory is not itself a defect.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-curation-policy
- assessment_id: septin-chloroplast_nucleoid-protein
  area: grounding
  topic: Native names, reference taxa and inventory
  outcome: supported
  summary: Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node. Literature-supported
    HLP token is not refuted by a bounded zero UniProt exact-name result. The exact
    HLP query returns zero across statuses in tax3055; this is a bounded index result,
    not evidence against the literature gene or absence under other loci.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-protein-policy
  - septin-native-chloroplast_nucleoid-verify
  - septin-native-chloroplast_nucleoid-causal
- assessment_id: septin-chloroplast_nucleoid-taxa
  area: scope
  topic: Organism, source strain and qualitative presence
  outcome: supported
  summary: Chlamydomonas3055 is exact and source-supported; complete Karcher primary
    abstract supports RNAi/localization, but full Methods and exact RNAi strain were
    not accessed. COMMON remains a qualitative synthesis consistent with native presence
    semantics, not a newly measured prevalence estimate.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-schema-policy
- assessment_id: septin-chloroplast_nucleoid-graph
  area: graph
  topic: Actor, edge and mechanistic scope
  outcome: supported
  summary: 'All three FUNCTION/NONMECHANISTIC edges have bounded support: HLP association,
    cpDNA packaging and HLP knockdown effects. Protein organization/maintenance is
    not an HLP-only complete formation mechanism.'
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-graph-policy
- assessment_id: septin-chloroplast_nucleoid-necessity
  area: evidence
  topic: Formation necessity versus organization/function
  outcome: unknown
  summary: DNA is constituting material of this DNA-defined region. Its collective
    ESSENTIAL designation does not establish necessity of a particular sequence, nor
    universal requirement for an individual HLP/CNS factor.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-curation-policy
- assessment_id: septin-chloroplast_nucleoid-source-tier
  area: provenance
  topic: Source identity, experiment and actual access
  outcome: supported
  summary: Karcher is complete primary abstract only; Kobayashi is genuine primary
    comparative research with explicitly selected body/Methods/caption scopes. The
    record verb review is not treated as an assertion that this article is a secondary
    review.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-access-source-receipts
  - septin-access-body-receipts
  - septin-access-more-receipts
  - septin-access-canonical-receipts
- assessment_id: septin-chloroplast_nucleoid-adapter
  area: provenance
  topic: Full-assertion structured-source applicability
  outcome: supported
  summary: HLP organization/maintenance and RNAi narrative positively trigger the
    native policy. Original expression-only exclusion is unsupported. Fresh full official
    catalogue has no actual host match; no unrelated prokaryotic proxy or unmatched
    downstream query. Historical runner failure and current fallback are explicit.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-chloroplast_nucleoid-native
  area: schema
  topic: Actual native validation and protein scope
  outcome: supported
  summary: Original validates and renders exactly; all historical inputs and current
    target hash match. Zero examples; one HAS_SYMBOLS_NO_EXAMPLES HLP class node.
    Literature-supported HLP token is not refuted by a bounded zero UniProt exact-name
    result. Both fresh root protein commands exit0; this bounded inventory result
    does not certify every scientific claim.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-original-validation-chloroplast_nucleoid
  - septin-native-chloroplast_nucleoid-verify
  - septin-native-chloroplast_nucleoid-causal
- assessment_id: septin-chloroplast_nucleoid-history
  area: provenance
  topic: History and unresolved discussions
  outcome: supported
  summary: Current gene/class fields are assessed on their actual source support;
    dated history/rationale remains historical and is not rewritten. Existing label-only/family
    discussions remain scoped follow-up, not automatically resolved or converted into
    mandatory inventory findings. No new record event or status promotion is performed.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-curation-policy
  - septin-review-contract
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
- assessment_id: septin-chloroplast_nucleoid-optional
  area: scope
  topic: Unasserted images, measurements and trait links
  outcome: not_applicable
  summary: No maintained image/license claim, record measurement, verbatim snippet
    or associated-trait mapping requires certification. Source captions were read
    where declared, but no figure pixels, supplements, raw experiments or sequence
    realignment were independently analyzed.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
- assessment_id: septin-chloroplast_nucleoid-limits
  area: completeness
  topic: Remaining scientific knowledge and coverage
  outcome: unknown
  summary: No complete constituent census, universal taxon prevalence, exact localized
    protein-family equivalence or detailed molecular assembly/replication mechanism
    is certified. Source-specific access and assay limits above remain; optional gaps
    and uncertain formation requirements are not fabricated findings.
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
- assessment_id: septin-chloroplast_nucleoid-verdict
  area: completeness
  topic: Current record verdict and finding lineage
  outcome: supported
  summary: 'pass_with_limitations: current structure identity, bounded source-supported
    constituents/functions/taxa and explicitly nonmechanistic graph are positively
    assessed. No scientific curation finding is established in this assigned target;
    the original likewise has no findings/actions, so no predecessor or terminal disposition
    is invented. Bundle applicability correction remains separate.'
  target_ids:
  - GO:0042644
  evidence_ids:
  - septin-record-chloroplast_nucleoid
  - septin-original-chloroplast_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-family-IPR000119
  - septin-nucleoid-agent-gene-HLP
  - septin-review-contract
- assessment_id: septin-kinetoplast-identity
  area: identity
  topic: Exact structure versus protein/DNA material identity
  outcome: supported
  summary: GO0020023/SL0150 identify the mitochondrial kinetoplast region. Contextual
    kDNA-network synonyms do not equate an isolated DNA molecule with the entire mitochondrion.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-generic-nucleoid-context
- assessment_id: septin-kinetoplast-components
  area: grounding
  topic: Constituent boundaries and exact family/material scope
  outcome: supported
  summary: Mini/maxicircle DNA and compacting DNA-bound KAP cohort are supported.
    The multi-family class is not every KAP-labelled protein; aKAP23 non-DNA localization
    and lineage-specific KAP1/2 prevent universal-name or complete T.brucei inventory
    inference. No forced one-family CURIE is justified.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-curation-policy
- assessment_id: septin-kinetoplast-protein
  area: grounding
  topic: Native names, reference taxa and inventory
  outcome: supported
  summary: Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node. KAP1–4 are comparative
    literature names, not a verified set of four universal T.brucei accession identities.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-protein-policy
  - septin-native-kinetoplast-verify
  - septin-native-kinetoplast-causal
- assessment_id: septin-kinetoplast-taxa
  area: scope
  topic: Organism, source strain and qualitative presence
  outcome: supported
  summary: Kinetoplastea5653 and T.brucei5691 are correct. The record explicitly acknowledges
    architectural diversity; interlocked disk/copy estimates are T.brucei/trypanosomatid
    context, not every kinetoplastid. Cooper uses EATRO1125-derived cells; Gluenz
    uses procyclic LISTER427/TREU927/29-13 assays. COMMON remains a qualitative synthesis
    consistent with native presence semantics, not a newly measured prevalence estimate.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-schema-policy
- assessment_id: septin-kinetoplast-graph
  area: graph
  topic: Actor, edge and mechanistic scope
  outcome: supported
  summary: Four ASSEMBLY/NONMECHANISTIC catenation/condensation edges summarize trypanosomatid
    network organization. Scope expressly withholds replication enzymology; TAC is
    relevant segregation context rather than a compulsory DNA-bound component. deSouza
    localization and secondary compaction synthesis do not establish a completed molecular
    compaction mechanism.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-graph-policy
- assessment_id: septin-kinetoplast-necessity
  area: evidence
  topic: Formation necessity versus organization/function
  outcome: unknown
  summary: All three component essentialities remain UNKNOWN. Different KAP mutations,
    lineage repertoires and DNA-copy contexts do not establish universal formation
    necessity.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-curation-policy
- assessment_id: septin-kinetoplast-source-tier
  area: provenance
  topic: Source identity, experiment and actual access
  outcome: supported
  summary: Amodeo/Jensen are secondary; Cooper/deSouza/Gluenz are primary with specified
    body scopes. Ogbadoyi is complete-primary-abstract scope despite a fetched unread
    body. Source counts and secondary proposals are not upgraded into universal experimental
    proof.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-access-source-receipts
  - septin-access-body-receipts
  - septin-access-more-receipts
  - septin-access-canonical-receipts
- assessment_id: septin-kinetoplast-adapter
  area: provenance
  topic: Full-assertion structured-source applicability
  outcome: supported
  summary: KAP DNA compaction, guide-RNA editing and genome organization positively
    trigger the native policy. Original expression-only exclusion is unsupported.
    Fresh full official catalogue has no actual host match; no unrelated prokaryotic
    proxy or unmatched downstream query. Historical runner failure and current fallback
    are explicit.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-kinetoplast-native
  area: schema
  topic: Actual native validation and protein scope
  outcome: supported
  summary: Original validates and renders exactly; all historical inputs and current
    target hash match. Zero examples; one HAS_SYMBOLS_NO_EXAMPLES KAP class node.
    KAP1–4 are comparative literature names, not a verified set of four universal
    T.brucei accession identities. Both fresh root protein commands exit0; this bounded
    inventory result does not certify every scientific claim.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-original-validation-kinetoplast
  - septin-native-kinetoplast-verify
  - septin-native-kinetoplast-causal
- assessment_id: septin-kinetoplast-history
  area: provenance
  topic: History and unresolved discussions
  outcome: supported
  summary: Current gene/class fields are assessed on their actual source support;
    dated history/rationale remains historical and is not rewritten. Existing label-only/family
    discussions remain scoped follow-up, not automatically resolved or converted into
    mandatory inventory findings. No new record event or status promotion is performed.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-curation-policy
  - septin-review-contract
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
- assessment_id: septin-kinetoplast-optional
  area: scope
  topic: Unasserted images, measurements and trait links
  outcome: not_applicable
  summary: No maintained image/license claim, record measurement, verbatim snippet
    or associated-trait mapping requires certification. Source captions were read
    where declared, but no figure pixels, supplements, raw experiments or sequence
    realignment were independently analyzed.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
- assessment_id: septin-kinetoplast-limits
  area: completeness
  topic: Remaining scientific knowledge and coverage
  outcome: unknown
  summary: No complete constituent census, universal taxon prevalence, exact localized
    protein-family equivalence or detailed molecular assembly/replication mechanism
    is certified. Source-specific access and assay limits above remain; optional gaps
    and uncertain formation requirements are not fabricated findings.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
- assessment_id: septin-kinetoplast-verdict
  area: completeness
  topic: Current record verdict and finding lineage
  outcome: supported
  summary: 'pass_with_limitations: current structure identity, bounded source-supported
    constituents/functions/taxa and explicitly nonmechanistic graph are positively
    assessed. No scientific curation finding is established in this assigned target;
    the original likewise has no findings/actions, so no predecessor or terminal disposition
    is invented. Bundle applicability correction remains separate.'
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-root43-sources-go
  - septin-root43-sources-SL0150
  - septin-root43-sources-tax5653
  - septin-root43-sources-tax5691
  - septin-root43-sources-doi-1
  - septin-root43-sources-doi-2
  - septin-root43-sources-doi-3
  - septin-root43-sources-doi-5
  - septin-root43-sources-doi-8
  - septin-root43-sources-doi-9
  - septin-PMC10719067-jats
  - septin-PMC6868439-jats
  - septin-PMC5683618-jats
  - septin-gluenz2011-canonical
  - septin-review-contract
- assessment_id: septin-kinetoplast-cohort-provenance
  area: provenance
  topic: Historical execution cohort versus target review cohort
  outcome: supported
  summary: Original limitations[0] correctly refers to the actual batch26 execution.
    All five check scope notes and evidence locators identify f97b1abe and same-base
    guards for batch26/batch43. This is supported historical provenance, not a cohort-label
    defect or a current-head execution claim. The tentative label-only concern was
    withdrawn after reading complete scope notes.
  target_ids:
  - GO:0020023
  evidence_ids:
  - septin-record-kinetoplast
  - septin-original-kinetoplast
  - septin-original-validation-kinetoplast
- assessment_id: septin-mitochondrial_nucleoid-identity
  area: identity
  topic: Exact structure versus protein/DNA material identity
  outcome: supported
  summary: GO0042645/SL0269 identify the nucleoid region; generic-nucleoid is_a, matrix
    parthood and mitochromosome/location synonyms are correct.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-generic-nucleoid-context
- assessment_id: septin-mitochondrial_nucleoid-components
  area: grounding
  topic: Constituent boundaries and exact family/material scope
  outcome: supported
  summary: mtDNA and an Abf2-represented mitochondrial HMG class are supported. IPR009071
    is a domain; broad IPR051965 with unchecked LLM prose does not supply exact class
    equivalence. No complete nucleoid proteome or exact DNA sequence-feature identity
    is certified.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-curation-policy
  - septin-nucleoid-agent-family-IPR009071
  - septin-nucleoid-agent-family-IPR051965
- assessment_id: septin-mitochondrial_nucleoid-protein
  area: grounding
  topic: Native names, reference taxa and inventory
  outcome: supported
  summary: One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class node.
    Identity and coverage do not turn every source assay into S288C or prove formation
    necessity. Exact reviewed ABF2 query returns one Q02486; primary ABF2, synonym
    HIM1, locusYMR072W/ORFYM9916.11 and S288C identity match.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-protein-policy
  - septin-native-mitochondrial_nucleoid-verify
  - septin-native-mitochondrial_nucleoid-causal
- assessment_id: septin-mitochondrial_nucleoid-taxa
  area: scope
  topic: Organism, source strain and qualitative presence
  outcome: supported
  summary: S.cerevisiae4932 and S288C559292 reference identity are correct. MCC109/BY4741/W303
    assay contexts remain separate from Q02486 reference strain. COMMON remains a
    qualitative synthesis consistent with native presence semantics, not a newly measured
    prevalence estimate.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-schema-policy
- assessment_id: septin-mitochondrial_nucleoid-graph
  area: graph
  topic: Actor, edge and mechanistic scope
  outcome: supported
  summary: Yeast FUNCTION/NONMECHANISTIC binding, passive packaging and repeat-stability
    edges are supported. Kucej uses in organello crosslinking and itself interprets
    in vivo association; no intact-live-cell ChIP is claimed here. Sia distinguishes
    frameshifts/deletions from unchanged point-mutation rate.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-graph-policy
- assessment_id: septin-mitochondrial_nucleoid-necessity
  area: evidence
  topic: Formation necessity versus organization/function
  outcome: unknown
  summary: UNKNOWN essentiality is retained. Abf2 deletion permits mtDNA retention
    under respiratory selection; instability or altered compaction is not universal
    loss of nucleoid formation.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-curation-policy
- assessment_id: septin-mitochondrial_nucleoid-source-tier
  area: provenance
  topic: Source identity, experiment and actual access
  outcome: supported
  summary: Kucej2008 and Sia2009 genuine scientific main text/Methods or assay footnotes
    were read; Kucej/Butow2007 remains secondary complete-abstract scope. Fresh access
    failures and separate recovered successes remain distinct.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-access-source-receipts
  - septin-access-body-receipts
  - septin-access-more-receipts
  - septin-access-canonical-receipts
- assessment_id: septin-mitochondrial_nucleoid-adapter
  area: provenance
  topic: Full-assertion structured-source applicability
  outcome: supported
  summary: Abf2 packaging and metabolic remodeling positively trigger the native policy.
    Original expression-only exclusion is unsupported. Fresh full official catalogue
    has no actual host match; no unrelated prokaryotic proxy or unmatched downstream
    query. Historical runner failure and current fallback are explicit.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-mitochondrial_nucleoid-native
  area: schema
  topic: Actual native validation and protein scope
  outcome: supported
  summary: Original validates and renders exactly; all historical inputs and current
    target hash match. One reviewed Q02486/ABF2/tax559292 example; one COVERED HMG-class
    node. Identity and coverage do not turn every source assay into S288C or prove
    formation necessity. Both fresh root protein commands exit0; this bounded inventory
    result does not certify every scientific claim.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-original-validation-mitochondrial_nucleoid
  - septin-native-mitochondrial_nucleoid-verify
  - septin-native-mitochondrial_nucleoid-causal
- assessment_id: septin-mitochondrial_nucleoid-history
  area: provenance
  topic: History and unresolved discussions
  outcome: supported
  summary: Current gene/class fields are assessed on their actual source support;
    dated history/rationale remains historical and is not rewritten. Existing label-only/family
    discussions remain scoped follow-up, not automatically resolved or converted into
    mandatory inventory findings. No new record event or status promotion is performed.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-curation-policy
  - septin-review-contract
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
- assessment_id: septin-mitochondrial_nucleoid-optional
  area: scope
  topic: Unasserted images, measurements and trait links
  outcome: not_applicable
  summary: No maintained image/license claim, record measurement, verbatim snippet
    or associated-trait mapping requires certification. Source captions were read
    where declared, but no figure pixels, supplements, raw experiments or sequence
    realignment were independently analyzed.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
- assessment_id: septin-mitochondrial_nucleoid-limits
  area: completeness
  topic: Remaining scientific knowledge and coverage
  outcome: unknown
  summary: No complete constituent census, universal taxon prevalence, exact localized
    protein-family equivalence or detailed molecular assembly/replication mechanism
    is certified. Source-specific access and assay limits above remain; optional gaps
    and uncertain formation requirements are not fabricated findings.
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
- assessment_id: septin-mitochondrial_nucleoid-verdict
  area: completeness
  topic: Current record verdict and finding lineage
  outcome: supported
  summary: 'pass_with_limitations: current structure identity, bounded source-supported
    constituents/functions/taxa and explicitly nonmechanistic graph are positively
    assessed. No scientific curation finding is established in this assigned target;
    the original likewise has no findings/actions, so no predecessor or terminal disposition
    is invented. Bundle applicability correction remains separate.'
  target_ids:
  - GO:0042645
  evidence_ids:
  - septin-record-mitochondrial_nucleoid
  - septin-original-mitochondrial_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-SL-0269
  - septin-nucleoid-agent-kucej2008-meta
  - septin-nucleoid-agent-kucej2007-meta
  - septin-nucleoid-agent-sia2009-meta
  - septin-kucej2008-xmlhtml
  - septin-sia2009-xmlhtml
  - septin-nucleoid-agent-tax4932
  - septin-nucleoid-agent-tax559292
  - septin-nucleoid-agent-protein-Q02486
  - septin-nucleoid-agent-gene-ABF2
  - septin-review-contract
- assessment_id: septin-plastid_nucleoid-identity
  area: identity
  topic: Exact structure versus protein/DNA material identity
  outcome: supported
  summary: GO0042646/SL0140 identify the generic plastid nucleoid; generic-nucleoid
    parent and plastid-stroma parthood are correct, with chloroplast as an exact child
    subtype.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-generic-nucleoid-context
- assessment_id: septin-plastid_nucleoid-components
  area: grounding
  topic: Constituent boundaries and exact family/material scope
  outcome: supported
  summary: Constituting plastid DNA material and variable associated protein complements
    are supported. The generic graph deliberately excludes lineage-specific protein
    identities; narrative Chlamydomonas HLP is an example, not a universal plastid
    requirement. The existing exact-family TODO does not mandate invented groundings.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-curation-policy
- assessment_id: septin-plastid_nucleoid-protein
  area: grounding
  topic: Native names, reference taxa and inventory
  outcome: supported
  summary: Zero examples and zero typed protein nodes; native success is empty inventory
    scope. HLP-containing narrative elsewhere still triggers applicability.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-protein-policy
  - septin-native-plastid_nucleoid-verify
  - septin-native-plastid_nucleoid-causal
- assessment_id: septin-plastid_nucleoid-taxa
  area: scope
  topic: Organism, source strain and qualitative presence
  outcome: supported
  summary: Viridiplantae33090 and Chlamydomonas3055 identities are correct. Kobayashi
    primary comparative and Introduction scope support ordinary green-plant occurrence,
    not a census of every plastid lineage; HLP evidence remains Chlamydomonas-specific.
    COMMON remains a qualitative synthesis consistent with native presence semantics,
    not a newly measured prevalence estimate.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-schema-policy
- assessment_id: septin-plastid_nucleoid-graph
  area: graph
  topic: Actor, edge and mechanistic scope
  outcome: supported
  summary: The two FUNCTION/NONMECHANISTIC edges state stromal containment and DNA
    packaging; exact GO/SL anatomy supports them. They do not assert an HLP-dependent
    universal molecular pathway.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-graph-policy
- assessment_id: septin-plastid_nucleoid-necessity
  area: evidence
  topic: Formation necessity versus organization/function
  outcome: unknown
  summary: DNA is constituting material of this DNA-defined region. Its collective
    ESSENTIAL designation does not establish necessity of a particular sequence, nor
    universal requirement for an individual HLP/CNS factor.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-curation-policy
- assessment_id: septin-plastid_nucleoid-source-tier
  area: provenance
  topic: Source identity, experiment and actual access
  outcome: supported
  summary: Karcher is complete primary abstract only; Kobayashi is genuine primary
    comparative research with explicitly selected body/Methods/caption scopes. The
    record verb review is not treated as an assertion that this article is a secondary
    review.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-access-source-receipts
  - septin-access-body-receipts
  - septin-access-more-receipts
  - septin-access-canonical-receipts
- assessment_id: septin-plastid_nucleoid-adapter
  area: provenance
  topic: Full-assertion structured-source applicability
  outcome: supported
  summary: HLP organization/maintenance and RNAi narrative positively trigger the
    native policy. Original expression-only exclusion is unsupported. Fresh full official
    catalogue has no actual host match; no unrelated prokaryotic proxy or unmatched
    downstream query. Historical runner failure and current fallback are explicit.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-plastid_nucleoid-native
  area: schema
  topic: Actual native validation and protein scope
  outcome: supported
  summary: Original validates and renders exactly; all historical inputs and current
    target hash match. Zero examples and zero typed protein nodes; native success
    is empty inventory scope. HLP-containing narrative elsewhere still triggers applicability.
    Both fresh root protein commands exit0; this bounded inventory result does not
    certify every scientific claim.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-original-validation-plastid_nucleoid
  - septin-native-plastid_nucleoid-verify
  - septin-native-plastid_nucleoid-causal
- assessment_id: septin-plastid_nucleoid-history
  area: provenance
  topic: History and unresolved discussions
  outcome: supported
  summary: Current gene/class fields are assessed on their actual source support;
    dated history/rationale remains historical and is not rewritten. Existing label-only/family
    discussions remain scoped follow-up, not automatically resolved or converted into
    mandatory inventory findings. No new record event or status promotion is performed.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-curation-policy
  - septin-review-contract
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
- assessment_id: septin-plastid_nucleoid-optional
  area: scope
  topic: Unasserted images, measurements and trait links
  outcome: not_applicable
  summary: No maintained image/license claim, record measurement, verbatim snippet
    or associated-trait mapping requires certification. Source captions were read
    where declared, but no figure pixels, supplements, raw experiments or sequence
    realignment were independently analyzed.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
- assessment_id: septin-plastid_nucleoid-limits
  area: completeness
  topic: Remaining scientific knowledge and coverage
  outcome: unknown
  summary: No complete constituent census, universal taxon prevalence, exact localized
    protein-family equivalence or detailed molecular assembly/replication mechanism
    is certified. Source-specific access and assay limits above remain; optional gaps
    and uncertain formation requirements are not fabricated findings.
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
- assessment_id: septin-plastid_nucleoid-verdict
  area: completeness
  topic: Current record verdict and finding lineage
  outcome: supported
  summary: 'pass_with_limitations: current structure identity, bounded source-supported
    constituents/functions/taxa and explicitly nonmechanistic graph are positively
    assessed. No scientific curation finding is established in this assigned target;
    the original likewise has no findings/actions, so no predecessor or terminal disposition
    is invented. Bundle applicability correction remains separate.'
  target_ids:
  - GO:0042646
  evidence_ids:
  - septin-record-plastid_nucleoid
  - septin-original-plastid_nucleoid
  - septin-nucleoid-agent-go
  - septin-nucleoid-agent-go-ancestors
  - septin-nucleoid-agent-karcher2009-meta
  - septin-nucleoid-agent-kobayashi2015-meta
  - septin-nucleoid-agent-kobayashi2015-jats
  - septin-nucleoid-agent-tax3055
  - septin-nucleoid-agent-SL-0140
  - septin-nucleoid-agent-tax33090
  - septin-review-contract
- assessment_id: plaque-t4-schema
  area: schema
  topic: Exact original provenance and current native coverage
  outcome: supported
  summary: 'Own three original YAML/MD pairs validate/render exactly;44 historical
    input rows match. Current unchanged target inventory: seven reviewed K-12 examples,
    one COVERED pooled NAP node. Root owns wider current gates.'
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-original-checks
  - plaque-native-nucleoid-verify
  - plaque-native-nucleoid-causal
- assessment_id: plaque-t4-history
  area: provenance
  topic: Historical rationale and conservative optional grounding
  outcome: supported
  summary: Dated history and rationale preserved; current source-neutral class TODOs
    are not contradicted merely by individual protein examples. No neighbor/category
    finding or prior issue is resolved by inference.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-history-policy
  - plaque-schema-policy
- assessment_id: plaque-t4-source
  area: evidence
  topic: Actual access and source-tier separation
  outcome: supported
  summary: Every citation identity and current claim inspected within declared source
    extent. Secondary synthesis is authority; current challenge/404 responses are
    access context only. Abstract-only claims retain protocol/strain limits; no pixels,
    supplements or rawdata reanalysis.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-go-terms
  - plaque-verma2019-jats
  - plaque-wang2011-jats
- assessment_id: plaque-t4-verdict
  area: consistency
  topic: Scientific outcome separate from bundle repairs
  outcome: concern
  summary: One inherited major generic-nucleoid identity finding remains open. Applicability
    repair stays in review bundles; no record edits or future CI/merge certification.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-go-terms
  - plaque-original-checks
- assessment_id: plaque-t6-schema
  area: schema
  topic: Exact original provenance and current native coverage
  outcome: supported
  summary: 'Own three original YAML/MD pairs validate/render exactly;44 historical
    input rows match. Current unchanged target inventory: three reviewed S288C examples,
    two COVERED Fks/Rho1 nodes. Root owns wider current gates.'
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-original-checks
  - plaque-native-1_3_beta_d_glucan_synthase_complex-verify
  - plaque-native-1_3_beta_d_glucan_synthase_complex-causal
- assessment_id: plaque-t6-history
  area: provenance
  topic: Historical rationale and conservative optional grounding
  outcome: supported
  summary: Dated history and rationale preserved; current source-neutral class TODOs
    are not contradicted merely by individual protein examples. No neighbor/category
    finding or prior issue is resolved by inference.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-history-policy
  - plaque-schema-policy
- assessment_id: plaque-t6-source
  area: evidence
  topic: Actual access and source-tier separation
  outcome: supported
  summary: Every citation identity and current claim inspected within declared source
    extent. Secondary synthesis is authority; current challenge/404 responses are
    access context only. Abstract-only claims retain protocol/strain limits; no pixels,
    supplements or rawdata reanalysis.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-go-terms
  - plaque-douglas1994-meta
  - plaque-qadota1996-meta
- assessment_id: plaque-t6-verdict
  area: consistency
  topic: Scientific outcome separate from bundle repairs
  outcome: supported
  summary: Qualified pass retained; no inherited or new scientific finding confirmed.
    Applicability repair stays in review bundles; no record edits or future CI/merge
    certification.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-go-terms
  - plaque-original-checks
- assessment_id: plaque-t8-schema
  area: schema
  topic: Exact original provenance and current native coverage
  outcome: supported
  summary: 'Own three original YAML/MD pairs validate/render exactly;44 historical
    input rows match. Current unchanged target inventory: two reviewed S288C examples,
    two COVERED Isw2/Itc1 nodes. Root owns wider current gates.'
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-original-checks
  - plaque-native-acf_complex-verify
  - plaque-native-acf_complex-causal
- assessment_id: plaque-t8-history
  area: provenance
  topic: Historical rationale and conservative optional grounding
  outcome: supported
  summary: Dated history and rationale preserved; current source-neutral class TODOs
    are not contradicted merely by individual protein examples. No neighbor/category
    finding or prior issue is resolved by inference.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-history-policy
  - plaque-schema-policy
- assessment_id: plaque-t8-source
  area: evidence
  topic: Actual access and source-tier separation
  outcome: supported
  summary: Every citation identity and current claim inspected within declared source
    extent. Secondary synthesis is authority; current challenge/404 responses are
    access context only. Abstract-only claims retain protocol/strain limits; no pixels,
    supplements or rawdata reanalysis.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-go-terms
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
- assessment_id: plaque-t8-verdict
  area: consistency
  topic: Scientific outcome separate from bundle repairs
  outcome: supported
  summary: Qualified pass retained; no inherited or new scientific finding confirmed.
    Applicability repair stays in review bundles; no record edits or future CI/merge
    certification.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-go-terms
  - plaque-original-checks
- assessment_id: plaque-t4-identity
  area: identity
  topic: Generic identifier with bacterial-only definition
  outcome: concern
  summary: GO0009295 definition and direct children include organellar nucleoids;
    current definition requires bacterial chromosome. GO0043590 is exact narrower
    bacterial class. Maintained mitochondrial/plastid records parent generic GO0009295;
    chloroplast parents plastid. Preserve generic identity and scope bacterial example,
    or undertake a separately authorized identity decision; no silent rename.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-go-terms
  - plaque-sl-0187
  - plaque-context-chloroplast_nucleoid
  - plaque-context-mitochondrial_nucleoid
  - plaque-context-plastid_nucleoid
- assessment_id: plaque-t4-material
  area: grounding
  topic: Heterogeneous bacterial chromosome and NAP components
  outcome: supported
  summary: Chromosomal DNA defines the bacterial example. HU/IHF/Fis/H-NS/Dps roles
    are supported at primary or secondary scopes; IPR000119 covers HU/IHF, not all
    NAPs. Heterogeneous pool does not assert all proteins perform every graph action
    or every member is necessary.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-verma2019-jats
  - plaque-wang2011-jats
  - plaque-ipr-IPR000119
- assessment_id: plaque-t4-proteins
  area: grounding
  topic: Seven accession and source-annotation identities
  outcome: supported
  summary: Seven exact reviewed K-12 accessions/gene/locus pairs and one-hit queries
    agree. Four PMID21903814 nucleoid annotations and H-NS333393 join verified. HU-beta/IHF-beta/Dps
    examples correctly remain identity-only where not attaching direct experimental
    location; modern H-NS mapping of1977 source is annotation-level.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-pmid-21903814
  - plaque-pmid-333393
  - plaque-wang2011-jats
  - plaque-up-P0ACF0
  - plaque-up-P0ACF4
  - plaque-up-P0A6X7
  - plaque-up-P0A6Y1
  - plaque-up-P0A6R3
  - plaque-up-P0ACF8
  - plaque-up-P0ABT2
  - plaque-gene-hupA
  - plaque-gene-hupB
  - plaque-gene-ihfA
  - plaque-gene-ihfB
  - plaque-gene-fis
  - plaque-gene-hns
  - plaque-gene-dps
- assessment_id: plaque-t4-scope
  area: scope
  topic: Bacterial example distinct from complete generic class
  outcome: supported
  summary: Bacteria/E.coli/K-12 identities agree. UNIVERSAL is qualitative bacterial
    chromosome-region scope, not every physiological state or universal NAP complement.
    Wang uses cultured E.coli early-log endogenous fusions, glucose/glycerol minimal
    media; reference accession taxon does not establish every experimental substrain.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-tax-2
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-wang2011-jats
  - plaque-verma2019-jats
- assessment_id: plaque-t4-graph
  area: graph
  topic: Scoped multiscale bacterial mechanism
  outcome: supported
  summary: NAP binding/geometry, supercoil constraints and compaction are supported
    as coarse review-level synthesis. Verma explicitly limits in-vivo barriers and
    concentration/magnesium-dependent NAP behavior; Wang supports observed H-NS organization
    separately from proposed loops. Pool does not claim each member executes all actions.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-verma2019-jats
  - plaque-wang2011-jats
  - plaque-dillon2010-meta
- assessment_id: plaque-t4-necessity
  area: evidence
  topic: Defining material versus individual formation requirements
  outcome: unknown
  summary: DNA is defining material of the bacterial example; CONDITIONAL NAP cohort
    does not establish every listed protein necessary for assembly. Gene-specific
    phenotype/function and organization evidence do not constitute universal formation
    requirements.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-schema-policy
  - plaque-verma2019-jats
  - plaque-wang2011-jats
- assessment_id: plaque-t4-adapter
  area: scope
  topic: Covered bacterial NAP expression contexts
  outcome: concern
  summary: Original formal no-expression exclusion ignores genes and regulator/pathway
    claims. Fresh e_coli/precise1k includes five strains and MG1655 reference-locus
    mapping; all seven genes found. dps has OxyR3/RpoS51 true flags, fis ppGpp145;
    other five no true flags among201modules. This is bounded transcriptional context,
    no biological absence or formation proof, AI prose excluded.
  target_ids:
  - GO:0009295
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
  - plaque-adapter-meta
  - plaque-adapter-gene-b4000-modules
  - plaque-adapter-gene-b0440-modules
  - plaque-adapter-gene-b1712-modules
  - plaque-adapter-gene-b0912-modules
  - plaque-adapter-gene-b3261-modules
  - plaque-adapter-gene-b1237-modules
  - plaque-adapter-gene-b0812-modules
  - plaque-adapter-module-3
  - plaque-adapter-module-51
  - plaque-adapter-module-145
- assessment_id: plaque-t6-identity
  area: identity
  topic: Exact complex and bounded yeast example
  outcome: supported
  summary: Native GO exact identity agrees. Fks1/Fks2 alternative catalytic subunits
    and Rho1 regulator define the selected yeast model, not a simultaneous obligatory
    Fks1/Fks2 heteromer.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-go-terms
  - plaque-mazur1995-meta
  - plaque-qadota1996-meta
- assessment_id: plaque-t6-taxon
  area: scope
  topic: Species example versus experimental/reference strains
  outcome: supported
  summary: S.cerevisiae4932 and S288C559292 verified. COMMON remains qualitative native
    prevalence wording, not independently measured strain census. Primary abstract-level
    experiments support yeast model without resolving every experimental strain.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-qadota1996-meta
  - plaque-mazur1995-meta
- assessment_id: plaque-t6-necessity
  area: grounding
  topic: Activity requirement is not assembly necessity
  outcome: unknown
  summary: Both components retain UNKNOWN essentiality. Rho1 catalytic dependence,
    mutant activity and copurification support biochemical roles, not a demonstrated
    failure of complex formation.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-schema-policy
  - plaque-qadota1996-meta
  - plaque-mazur1996-meta
- assessment_id: plaque-t6-adapter
  area: scope
  topic: Positive molecular narrative assessed against actual host catalogue
  outcome: concern
  summary: Original prose-only exclusion invokes absent expression assertions despite
    named genes/complex functions. Fresh complete catalogue has no Saccharomyces match;
    current primary/authority fallback applies, no bacterial module proxy or biological
    absence claim.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-original-6
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t8-identity
  area: identity
  topic: Exact complex and bounded yeast example
  outcome: supported
  summary: Native GO exact identity agrees. GO explicitly includes Isw2; chosen purified
    Isw2/Itc1 ACF-like example is distinguished from four-subunit CHRAC-like Isw2.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-go-terms
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
- assessment_id: plaque-t8-taxon
  area: scope
  topic: Species example versus experimental/reference strains
  outcome: supported
  summary: S.cerevisiae4932 and S288C559292 verified. COMMON remains qualitative native
    prevalence wording, not independently measured strain census. Gelbart Methods
    specify W1588-4C congenic to W303, not S288C; current example is species-level
    purified complex and does not force strain equivalence. Native two-subunit in-vivo
    prevalence remains uncertain.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
- assessment_id: plaque-t8-necessity
  area: grounding
  topic: Activity requirement is not assembly necessity
  outcome: unknown
  summary: Both components retain UNKNOWN essentiality. Cooperative Isw2/Itc1 biochemical
    activity and possible two-subunit populations do not establish formation necessity;
    purification caveat retained.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-schema-policy
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
- assessment_id: plaque-t8-adapter
  area: scope
  topic: Positive molecular narrative assessed against actual host catalogue
  outcome: concern
  summary: Original formal exclusion invokes absent expression assertions despite
    named genes/complex functions. Fresh complete catalogue has no Saccharomyces match;
    current primary/authority fallback applies, no bacterial module proxy or biological
    absence claim.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-original-8
  - plaque-policy
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t6-composition
  area: grounding
  topic: Exact selected subunit classes and conservative grounding
  outcome: supported
  summary: Douglas/Mazur/Qadota complete primary abstracts and current annotations
    support alternative Fks1/Fks2 and Rho1 association/regulation. GT48 domain and
    broad Rho family are not exact selected pair/regulator identity; label-only TODO
    remains justified without exhaustive-family absence claim.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-douglas1994-meta
  - plaque-mazur1995-meta
  - plaque-qadota1996-meta
  - plaque-mazur1996-meta
  - plaque-ipr-IPR003440
  - plaque-ipr-IPR003578
- assessment_id: plaque-t6-proteins
  area: grounding
  topic: Verified yeast protein aliases and annotation joins
  outcome: supported
  summary: P38631 FKS1, P40989 GSC2 aliasFKS2 and P06780 RHO1 are reviewed S288C.
    P38631 current Mitochondrion location explicitly carries11856368/12185837/14576278;
    the record accurately says UniProt annotates these joins. Utsugi surface movement,
    Dijkgraaf wall phenotype and Sickmann proteome abstracts differ in scope; mitochondrial
    localization is not independently certified or used as synthase mechanism location.
    No new attribution finding established.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-up-P38631
  - plaque-up-P40989
  - plaque-up-P06780
  - plaque-gene-FKS1
  - plaque-gene-FKS2
  - plaque-gene-RHO1
  - plaque-pmid-11856368
  - plaque-pmid-12185837
  - plaque-pmid-14576278
- assessment_id: plaque-t6-graph
  area: graph
  topic: Bounded synthase regulatory function
  outcome: supported
  summary: UDP-glucose polymerization, Rho1 stimulation and glucan contribution to
    fungal wall are supported at complete primary abstract and GO tiers. NONMECHANISTIC
    correctly withholds assembly order and upstream cell-integrity/GEF membership.
    Abstract scope does not certify complete protocols, direct binding affinity or
    exact stoichiometry.
  target_ids:
  - GO:0000148
  evidence_ids:
  - plaque-current-6
  - plaque-go-terms
  - plaque-qadota1996-meta
  - plaque-mazur1996-meta
  - plaque-pmid-7983071
- assessment_id: plaque-t8-composition
  area: grounding
  topic: ACF-like two-subunit biochemistry with CHRAC caveat
  outcome: supported
  summary: Gelbart identifies Itc1/WAC and reconstitutes cooperative activity; McConnell
    detects Dpb4/Dls1 and two-/four-subunit populations but explicitly cannot exclude
    procedural destabilization. Record recognizes both; no exclusive native two-subunit
    claim or additional mandatory component inferred. WAC and Isw1/2 N-terminal candidates
    are domains, not exact full-length ACF constituents.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
  - plaque-ipr-IPR013136
  - plaque-ipr-IPR044754
- assessment_id: plaque-t8-proteins
  area: grounding
  topic: Reviewed Isw2/Itc1 and nuclear annotation provenance
  outcome: supported
  summary: Q08773 ISW2/YOR304W and P53125 ITC1/YGL133W are reviewed S288C; one-hit
    gene queries and nuclear annotations agree. Huh2003 PMID14562095 is abstract plus
    native annotation only; Gelbart11238944 source agrees. Nuclear location does not
    establish complex membership by itself.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-up-Q08773
  - plaque-up-P53125
  - plaque-gene-ISW2
  - plaque-gene-ITC1
  - plaque-pmid-14562095
  - plaque-gelbart2001-pmc
- assessment_id: plaque-t8-graph
  area: graph
  topic: Supported nonmechanistic remodeling summary
  outcome: supported
  summary: Subunit association with ACF-like complex and ATP-dependent chromatin remodeling
    match the primary experiments. NONMECHANISTIC correctly avoids substrate-recognition/sliding
    order, universal native stoichiometry or exact assembly necessity.
  target_ids:
  - GO:0016590
  evidence_ids:
  - plaque-current-8
  - plaque-go-terms
  - plaque-gelbart2001-pmc
  - plaque-mcconnell2004-pmc
- assessment_id: micro-schema-0
  area: schema
  topic: Original validity and current provenance
  outcome: supported
  summary: Original validate/render and frozen-input comparisons passed; current source
    bytes match native inspect. Validation is not scientific certification. Root owns
    current full QC/focused/CI gates.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-original-audit
  - micro-native-propanediol_degradation_polyhedral_organelle-verify
  - micro-native-propanediol_degradation_polyhedral_organelle-causal
- assessment_id: micro-scope-0
  area: scope
  topic: Complete target, source tiers and preserved history
  outcome: supported
  summary: Complete current record and immutable original were read; no maintained
    image or verbatim snippet. Exact source tiers and experimental host/condition
    limits are retained. Other cohort records are outside this scientific disposition;
    no group/category issue is resolved by inference.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-schema-1
  area: schema
  topic: Original validity and current provenance
  outcome: supported
  summary: Original validate/render and frozen-input comparisons passed; current source
    bytes match native inspect. Validation is not scientific certification. Root owns
    current full QC/focused/CI gates.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-original-audit
  - micro-native-3_phenylpropionate_dioxygenase_complex-verify
  - micro-native-3_phenylpropionate_dioxygenase_complex-causal
- assessment_id: micro-scope-1
  area: scope
  topic: Complete target, source tiers and preserved history
  outcome: supported
  summary: Complete current record and immutable original were read; no maintained
    image or verbatim snippet. Exact source tiers and experimental host/condition
    limits are retained. Other cohort records are outside this scientific disposition;
    no group/category issue is resolved by inference.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-schema-2
  area: schema
  topic: Original validity and current provenance
  outcome: supported
  summary: Original validate/render and frozen-input comparisons passed; current source
    bytes match native inspect. Validation is not scientific certification. Root owns
    current full QC/focused/CI gates.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-original-audit
  - micro-native-acrab_tolc_multidrug_efflux_transport_complex-verify
  - micro-native-acrab_tolc_multidrug_efflux_transport_complex-causal
- assessment_id: micro-scope-2
  area: scope
  topic: Complete target, source tiers and preserved history
  outcome: supported
  summary: Complete current record and immutable original were read; no maintained
    image or verbatim snippet. Exact source tiers and experimental host/condition
    limits are retained. Other cohort records are outside this scientific disposition;
    no group/category issue is resolved by inference.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-pdu-identity
  area: identity
  topic: Exact Pdu organelle and taxon
  outcome: supported
  summary: GO0031472 and broader GO0031469 fit a protein-coated metabolic organelle.
    Native LT2 occurrence and variable Bacteria scope are distinct from broad genomic
    potential and recombinant expression. GO0050215 is an activity, correctly not
    substituted as the PduCDE-complex identity.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-go-0031472
  - micro-go-0031469
  - micro-go-0050215
  - micro-tax-2
  - micro-tax-99287
  - micro-havemann2002
  - micro-havemann2003
  - micro-meta-pmid-10498708
- assessment_id: micro-pdu-class
  area: grounding
  topic: PduU subclass and current PduM family
  outcome: concern
  summary: Current PduU remains grouped as tandem BMC-T although native protein, IPR044870
    architecture and Yang2020 table distinguish a circularly permuted single-domain
    hexamer. New tiles-edge description names PduB/PduT, but the shared actor retains
    erroneous PduU membership. IPR030992 exactly resolves current PduM label-only
    grounding. F1/F3 persist.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-yang2020
  - micro-ipr-IPR044870
  - micro-up-P0A1D1
  - micro-meta-pduu2008-meta
  - micro-ipr-IPR030992
  - micro-up-Q9XDN4
  - micro-sinha2012
- assessment_id: micro-pdu-native-identities
  area: grounding
  topic: Eleven native LT2 examples and bounded query checks
  outcome: supported
  summary: All11 examples remain reviewed, exact native primary symbols/loci/taxon
    and current query-selected identities agree. Native localization-source joins
    are annotation provenance; Held2016 recombinant Eut abstract is not independently
    direct proof of each native Pdu localization. Membership has separate Pdu primary
    support.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-tax-99287
  - micro-havemann2003
  - micro-sinha2012
  - micro-yang2020
  - micro-meta-pmid-27063436
  - micro-up-P0A1C7
  - micro-up-H9L478
  - micro-up-Q9XDN6
  - micro-up-P37449
  - micro-up-Q9XDM8
  - micro-up-P0A1D1
  - micro-up-Q9XDN3
  - micro-up-Q9XDN4
  - micro-up-P37450
  - micro-up-O31041
  - micro-up-O31042
- assessment_id: micro-pdu-necessity
  area: grounding
  topic: Formation is distinct from catalysis and cohort membership
  outcome: unknown
  summary: Recovered MCPs from delta-pduCDE support catalytic complex dispensability
    for shell assembly. PduM/PduN UNKNOWN avoids automatic formation-necessity inference.
    Shell-cohort CONDITIONAL is not a complete condition-by-member matrix; old/new
    pduA experiments differ in phenotype and conditions. No universal claim for every
    cohort member is inferred.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-fan2011
  - micro-havemann2002
  - micro-yang2020
  - micro-yang2022
  - micro-meta-pmid-21239588
  - micro-sinha2012
- assessment_id: micro-pdu-functions
  area: evidence
  topic: Sequestered B12 chemistry and toxicity protection
  outcome: supported
  summary: LT2 source experiments and exact GO activity/process support 1,2-PD chemistry,
    enzyme compartmentalization and reduced propionaldehyde-associated damage. Fresh
    Sampson body now supplies bounded growth/HPLC/mutagenesis detail beyond the historical
    abstract-only scope; no universal volatility claim is made.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-go-0050215
  - micro-go-0051144
  - micro-havemann2003
  - micro-sampson2008
  - micro-meta-doi-8
  - micro-fan2010
- assessment_id: micro-pdu-receptor
  area: graph
  topic: Cargo-targeting receptor specificity
  outcome: concern
  summary: Fan2010/2011 establish PduP/PduD targeting sequences, not the general enzyme-core-to-BMC-T
    binding edge. Fresh Fan2012 body directly tests PduP binding to PduA/J, with separate
    recombinant pull-down and native encapsulation contexts. PduD/core cannot be reassigned
    to those partners by analogy; F2 persists.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-fan2010
  - micro-fan2011
  - micro-fan2012
  - micro-yang2022
- assessment_id: micro-pdu-stale-refresh
  area: graph
  topic: Changed PduCDE type and two convergence edges
  outcome: supported
  summary: PduCDE STRUCTURE is appropriate for the named multisubunit complex; the
    prior allowed GENE_OR_PROTEIN representation is not condemned merely by enum.
    New tiles/assembles-into edges fit the coarse source-based convergence model,
    subject to F1 actor classification. PduB1–37 linkage is experimentally supported;
    EP-driven condensation/PduM contact geometry are proposed explanatory models,
    not new direct contact/kinetic measurements. No fabricated new issue is inferred
    from that distinction.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-delta-0
  - micro-record-0
  - micro-meta-doi-8
  - micro-fan2011
  - micro-yang2022
  - micro-havemann2003
  - micro-yang2020
- assessment_id: micro-pdu-vertex
  area: evidence
  topic: Pentamer/vertex evidence scope
  outcome: supported
  summary: Wheatley2013 abstract reports GrpN crystal and EutN solution pentamers,
    supplying homologous-family support rather than a measured PduN structure. Current
    native PduN and Pdu experiments provide separate context; no paper-specific PduN
    atomic measurement is claimed.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-meta-doi-0
  - micro-up-Q9XDN3
  - micro-yang2020
  - micro-meta-pmid-21239588
- assessment_id: micro-hca-identity
  area: identity
  topic: Exact complex versus broader oxidoreductase and downstream dehydrogenase
  outcome: supported
  summary: GO0009334 exact four-protein complex, GO1990204 parent and GO0008695 activity
    agree. Historical HcaA1/A2 correspond to HcaE/F; downstream HcaB dehydrogenase
    is distinct from a legacy hcaF alias. Current K-12 identities and four exact families
    agree.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-go-0009334
  - micro-go-1990204
  - micro-go-0008695
  - micro-diaz1998
  - micro-ipr-IPR020875
  - micro-ipr-IPR023712
  - micro-ipr-IPR023739
  - micro-ipr-IPR023744
  - micro-up-P0ABR5
  - micro-up-Q47140
  - micro-up-P0ABW0
  - micro-up-P77650
- assessment_id: micro-hca-source
  area: evidence
  topic: Whole-cell activity and experimental strains
  outcome: supported
  summary: Díaz1998 uses K-12 MC1061/ED1061 with MG1655/DH5alpha context and recombinant
    Salmonella controls. Whole-cell PP-to-DHPP assay includes downstream HcaB; it
    is not purified Hca-only product kinetics. The record canonical K-12 context and
    known enzyme roles are compatible with this bounded source.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-diaz1998
  - micro-tax-83333
  - micro-go-0008695
- assessment_id: micro-hca-mechanism
  area: graph
  topic: Coarse classIIB electron-transfer architecture
  outcome: supported
  summary: HcaD-to-HcaC-to-HcaE electron transfer, HcaF/alpha oxygenase association
    and catalysis form a mechanistic biochemical model. Native family assignments/sequence
    comparisons support this architecture; the primary paper did not individually
    measure every electron-transfer step. The record does not claim isolated reconstitution
    or measured transfer kinetics.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-diaz1998
  - micro-ipr-IPR023739
  - micro-ipr-IPR023744
  - micro-ipr-IPR020875
  - micro-go-0009334
- assessment_id: micro-hca-necessity
  area: grounding
  topic: UNKNOWN component essentiality
  outcome: supported
  summary: All four UNKNOWN values avoid equating pathway loss with inability of the
    physical complex to form. No optional example or additional enzyme is demanded.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-diaz1998
  - micro-policy
- assessment_id: micro-acr-identity
  area: identity
  topic: Exact CPX pump and source-specific composition
  outcome: supported
  summary: Minted record identity denotes exact CPX4263, not broader GO1990281 as
    identity. All interactor IDs,6AcrA:3AcrB:3TolC counts and PDB entity mappings
    agree. K-12 source composition remains separate from the engineered C43(DE3) expression
    experiment and generic PDB source taxon562.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-cpx
  - micro-pdb
  - micro-pdb-entity1
  - micro-pdb-entity2
  - micro-pdb-entity3
  - micro-wang2017
  - micro-tax-83333
  - micro-go-1990281
- assessment_id: micro-acr-family
  area: grounding
  topic: AcrA exact family versus unresolved AcrB
  outcome: concern
  summary: Current IPR058628 is the exact AcrA family and P0AE06 native link. This
    resolves a current label-only task without rewriting old verification history.
    TolC IPR058622 is correct; no broader RND family is forced onto AcrB. F4 preserves
    original Acr F1 lineage.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-ipr-IPR058628
  - micro-up-P0AE06
  - micro-ipr-IPR058622
  - micro-policy
- assessment_id: micro-acr-proteins
  area: grounding
  topic: Native accession identity is not an ambiguous alias query
  outcome: supported
  summary: All3 exact reviewed K-12 entries, primary names/loci and CPX joins agree.
    Current gene_exact:acrB also returns gyrB through an old alias; the record identifies
    exact P31224/ACRB_ECOLI rather than asserting that the symbol query has one hit.
    No new query-uniqueness finding is warranted.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-up-P0AE06
  - micro-up-P31224
  - micro-up-P02930
  - micro-gene-acrB
  - micro-cpx
- assessment_id: micro-acr-function
  area: graph
  topic: Bounded tripartite pump export and stale membership links
  outcome: supported
  summary: Existing NONMECHANISTIC function graph and the3new contributes-to edges
    are supported as coarse physical membership/coupling and xenobiotic export. Apo5V5S
    is disulfide-stabilized AcrAB-TolC; separate ligand-state AcrABZ preparations
    do not require adding AcrZ to this target. No assembly order or kinetics is inferred.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-delta-2
  - micro-cpx
  - micro-pdb
  - micro-wang2017
  - micro-go-0042910
- assessment_id: micro-acr-necessity
  area: grounding
  topic: Formation necessity and narrow source provenance
  outcome: unknown
  summary: Intact tripartite composition is established, but the three ESSENTIAL flags
    are not independently tested formation-depletion claims in the inspected CPX/PDB/Wang
    evidence. Missing depletion evidence alone is not refutation. The added notes
    specifically attributing essentiality to CPX require separate narrow provenance
    scrutiny.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-cpx
  - micro-eco-0353
  - micro-wang2017
  - micro-policy
- assessment_id: micro-adapter-0
  area: scope
  topic: Whole-record structured-source applicability and matched context
  outcome: supported
  summary: Named proteins, loci and metabolic/transport pathways trigger inspection.
    Salmonella core includes LT2 among6strains; ten of11checked native loci are module33
    members. STM2045/PduJ is absent from its gene table and its endpoint all-zero
    output is not meaningful negative evidence. Fresh official metadata/gene/module
    fallback completed; the historical00:49Z unavailable runner was not rerun or called
    successful.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-native-review-policy
  - micro-catalogue
  - micro-s_enterica-meta
  - micro-s_enterica-genes
  - micro-s_enterica-module-list
  - micro-historical-runner
  - micro-s_enterica-module33
- assessment_id: micro-adapter-defect-0
  area: provenance
  topic: Original review applicability defect
  outcome: concern
  summary: Original notes exclude iModulonDB for complex identity, protein family,
    assembly and enzyme/transport claims without a formal adapter check. This does
    not implement the actual gene/protein/pathway trigger. Successor supplies bounded
    applicability and selected matched-source evidence; original remains immutable.
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-prior-0
  - micro-native-review-policy
  - micro-catalogue
  - micro-s_enterica-meta
- assessment_id: micro-adapter-1
  area: scope
  topic: Whole-record structured-source applicability and matched context
  outcome: supported
  summary: Named proteins, loci and metabolic/transport pathways trigger inspection.
    E. coli precise1k includes5strains; all four Hca loci are present but below all201
    module thresholds. This is not biological absence or an incorrect Hca record.
    Fresh official metadata/gene/module fallback completed; the historical00:49Z unavailable
    runner was not rerun or called successful.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-native-review-policy
  - micro-catalogue
  - micro-e_coli-meta
  - micro-e_coli-genes
  - micro-e_coli-module-list
  - micro-historical-runner
  - micro-modules-e_coli-b2538
  - micro-modules-e_coli-b2539
  - micro-modules-e_coli-b2540
  - micro-modules-e_coli-b2542
- assessment_id: micro-adapter-defect-1
  area: provenance
  topic: Original review applicability defect
  outcome: concern
  summary: Original Hca check imodulondb explicitly says no expression-module claim
    is maintained. This does not implement the actual gene/protein/pathway trigger.
    Successor supplies bounded applicability and selected matched-source evidence;
    original remains immutable.
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-prior-1
  - micro-native-review-policy
  - micro-catalogue
  - micro-e_coli-meta
- assessment_id: micro-adapter-2
  area: scope
  topic: Whole-record structured-source applicability and matched context
  outcome: supported
  summary: Named proteins, loci and metabolic/transport pathways trigger inspection.
    E. coli precise1k includes5strains; b0462/b0463/b3035 belong to SoxS module22.
    This does not demonstrate physical pump assembly or necessity. Fresh official
    metadata/gene/module fallback completed; the historical00:49Z unavailable runner
    was not rerun or called successful.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-native-review-policy
  - micro-catalogue
  - micro-e_coli-meta
  - micro-e_coli-genes
  - micro-e_coli-module-list
  - micro-historical-runner
  - micro-e_coli-module22
- assessment_id: micro-adapter-defect-2
  area: provenance
  topic: Original review applicability defect
  outcome: concern
  summary: Original notes exclude iModulonDB for complex identity, protein family,
    assembly and enzyme/transport claims without a formal adapter check. This does
    not implement the actual gene/protein/pathway trigger. Successor supplies bounded
    applicability and selected matched-source evidence; original remains immutable.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-prior-2
  - micro-native-review-policy
  - micro-catalogue
  - micro-e_coli-meta
- assessment_id: micro-acr-new-provenance
  area: provenance
  topic: Added CPX notes overstate the source annotation
  outcome: concern
  summary: 'New F5 is limited to source attribution: native CPX lists stoichiometric
    participants and physical interaction, not an explicit essentiality annotation.
    The three formal membership edges remain supported; inherited component formation-necessity
    uncertainty is not promoted to a biological contradiction.'
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-delta-2
  - micro-cpx
  - micro-eco-0353
  - micro-wang2017
  - micro-policy
- assessment_id: micro-verdict-0
  area: other
  topic: Current scoped verdict
  outcome: concern
  summary: 'needs_curation: 3 current findings; sources and positive assessments remain
    bounded.'
  target_ids:
  - GO:0031472
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-yang2020
  - micro-ipr-IPR044870
  - micro-up-P0A1D1
  - micro-meta-pduu2008-meta
  - micro-fan2010
  - micro-fan2011
  - micro-fan2012
  - micro-yang2022
  - micro-policy
  - micro-ipr-IPR030992
  - micro-up-Q9XDN4
  - micro-sinha2012
- assessment_id: micro-verdict-1
  area: other
  topic: Current scoped verdict
  outcome: supported
  summary: 'pass_with_limitations: exact Hca identity, four components and source-based
    classIIB model supported; no demonstrated current record defect. Native adapter
    review defect is repaired by the successor observation.'
  target_ids:
  - GO:0009334
  evidence_ids:
  - micro-record-1
  - micro-prior-1
- assessment_id: micro-verdict-2
  area: other
  topic: Current scoped verdict
  outcome: concern
  summary: 'needs_curation: 2 current findings; sources and positive assessments remain
    bounded.'
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
  - micro-ipr-IPR058628
  - micro-up-P0AE06
  - micro-cpx
  - micro-delta-2
  - micro-eco-0353
  - micro-wang2017
  - micro-acr-independent-challenge
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 2 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0031472
  - GO:0042644
  - GO:0020023
  - GO:0042645
  - GO:0009295
  - GO:0042646
  - GO:0000148
  - GO:0009334
  - GO:0016590
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
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
  issue_key: nucleoid-generic-identifier-bacterial-definition-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Align the bacterial-only definition with the generic nucleoid identity
  description: 'The maintained identifier GO0009295 denotes bacterial, mitochondrial,
    plastid and viral nucleic-acid regions, and the frozen organellar records use
    it as their parent. The target definition instead requires a bacterial chromosome.
    Native GO0043590 is the exact narrower bacterial-nucleoid class. This is more
    than incomplete taxonomic examples: it changes the defining scope of the generic
    record. The bacterial NAP evidence, verified E. coli proteins and example-specific
    mechanism remain valid.'
  target_ids:
  - GO:0009295
  field_paths:
  - definition
  - definition_source
  - identifier
  evidence_ids:
  - plaque-current-4
  - plaque-original-4
  - plaque-go-terms
  - plaque-sl-0187
  - plaque-context-chloroplast_nucleoid
  - plaque-context-mitochondrial_nucleoid
  - plaque-context-plastid_nucleoid
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/nucleoid.yaml
    role: maintained scientific record
  rule_id: Exact GO identity and source scope
  native_severity: major
  normalization_reason: An affirmative bacterial-only definition materially narrows
    an explicitly generic ontology identity and excludes its maintained organellar
    children. Major scope/identity normalization is warranted; blocker is unnecessary
    because the generic identifier remains valid and the biological example material
    is usable.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T042551Z-nucleoid-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2834
- finding_id: micro-F1
  issue_key: pdu-pduu-shell-class
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate PduU from the tandem-domain BMC-T cohort
  description: The component explicitly declares PduB, PduT and PduU to be BMC-T proteins
    and treats circular permutation as sufficient for that class. The cited quantitative
    study distinguishes trimeric PduT from hexameric PduU; native PduU and domain
    metadata identify the single-domain BMC-H architecture. Correct organelle membership
    does not repair the wrong molecular subclass.
  target_ids:
  - GO:0031472
  field_paths:
  - components[1].label
  - components[1].gene_symbols
  - components[1].role
  - components[1].grounding_notes
  - causal_graphs[0].nodes[1]
  evidence_ids:
  - micro-record-0
  - micro-yang2020
  - micro-ipr-IPR044870
  - micro-up-P0A1D1
  - micro-meta-pduu2008-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: major
  normalization_reason: This is a material protein-class assignment error propagated
    into a mechanistic actor, not an optional annotation or terminology preference.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2835
- finding_id: micro-F2
  issue_key: pdu-targeting-bmc-t-partner
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Do not infer a general BMC-T receptor from cargo-targeting experiments
  description: The MECHANISTIC edge directly binds the lumen enzyme core to the BMC-T
    cohort. Fan2010/2011 establish terminal-sequence targeting, not that specific
    receptor class. The freshly inspected Fan2012 body reports PduP binding to PduA/PduJ,
    and the Yang2022 PduM/PduB model is a different, explicitly qualified coupling
    mechanism. The existing edge conflates these cargo and interaction contexts.
  target_ids:
  - GO:0031472
  field_paths:
  - causal_graphs[0].edges[2]
  evidence_ids:
  - micro-record-0
  - micro-fan2010
  - micro-fan2011
  - micro-fan2012
  - micro-yang2022
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: major
  normalization_reason: The endpoint and binding predicate assert a specific causal
    molecular relation unsupported by their cited experiments; generic encapsulation
    remains correct. This is independent of the PduU classification correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2836
- finding_id: micro-F3
  issue_key: pdu-pdum-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground PduM to its verified protein family
  description: The label-only PduM component now has an exact source-neutral family,
    IPR030992, whose native description and citation match the curated structural
    protein. This is a current resolvable gap, not a claim that a historical search
    was dishonest.
  target_ids:
  - GO:0031472
  field_paths:
  - components[3].grounding
  - components[3].grounding_status
  - components[3].grounding_notes
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR030992
  - micro-up-Q9XDN4
  - micro-sinha2012
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: Identity and biological role are correct; only the exact available
    family grounding remains unresolved.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2837
- finding_id: micro-F4
  issue_key: acrab-acra-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the available exact AcrA family grounding
  description: The component and open discussion retain AcrA as reviewed-label-only
    pending an exact family. IPR058628 now supplies the named AcrA family matching
    P0AE06 and the curated adaptor role. This finding concerns the current resolvable
    task, not the accuracy of its historical verification statement.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  - discussions[0]
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR058628
  - micro-up-P0AE06
  - micro-cpx
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: The protein and pump identities are correct; this is a bounded
    source-neutral family-grounding correction. AcrB is left unresolved rather than
    forced into a broader RND family.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2838
- finding_id: micro-F5
  issue_key: acrab-cpx-essentiality-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Keep CPX participant provenance distinct from an essentiality annotation
  description: The three newly added contributes-to edges correctly connect AcrA,AcrB
    and TolC to the intact pump, but their CPX evidence notes say the source curates
    each as an essential stoichiometric subunit. The current native source supplies
    exact multiplicities and physical-interaction membership, with each participant
    role unspecified; it does not explicitly annotate formation essentiality. Narrow
    the source claim without asserting that any subunit is biologically dispensable
    or demanding an optional depletion experiment.
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  field_paths:
  - causal_graphs[0].edges[5].evidence[0].notes
  - causal_graphs[0].edges[6].evidence[0].notes
  - causal_graphs[0].edges[7].evidence[0].notes
  evidence_ids:
  - micro-record-2
  - micro-delta-2
  - micro-cpx
  - micro-eco-0353
  - micro-wang2017
  - micro-policy
  - micro-acr-independent-challenge
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  rule_id: Evidence must support the precise attributed claim; source-specific composition
    is distinct from formation necessity
  native_severity: minor
  normalization_reason: The physical relation and protein identities are correct;
    this is a bounded new source-provenance overstatement, not a demonstrated biological
    essentiality error.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2839
actions:
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0009295
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/nucleoid.yaml
    role: maintained scientific record
  description: In separately authorized curation, align the generic GO0009295 definition
    with its actual scope and clearly qualify bacterial DNA/NAP/examples and graph
    as bacterial exemplars. Preserve the correct generic identifier and valid organellar
    child relations. If the intended record is instead specifically bacterial nucleoid,
    make that a deliberate separate identity/hierarchy decision using verified GO0043590,
    with all affected references reviewed; do not silently relabel the generic parent.
  acceptance_checks:
  - The defining text and identifier denote the same class and do not exclude the
    maintained mitochondrial/plastid subclasses of generic nucleoid.
  - The original bacterial evidence and seven verified protein examples remain explicitly
    scoped; no unsupported universal protein inventory is introduced.
  - Any separately authorized identity change checks all ignored-inclusive inbound
    references and follows native guarded-writer/history rules.
  - Focused schema/strict, native protein/graph and identifier-label gates pass after
    authorized curation.
  - Preserve valid bacterial NAP examples and scoped graph, append-only history/rationale
    and independent organellar records; no automatic broader issue resolution.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0031472
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: In authorized curation, move or separately represent PduU in its supported
    single-domain circularly permuted BMC-H class. Retain PduB/PduT in the properly
    scoped BMC-T cohort and update dependent node membership without losing supported
    PduU occurrence.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated discussion rationale and posed_date; append historical context
    and update current prompt/notes only where needed. No record edits are made in
    this review PR.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0031472
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: Replace the edge with the directly supported targeting relation or
    a specifically identified, source-qualified cargo/receptor interaction. If representing
    PduP–PduA/PduJ, preserve that distinct cargo identity and cite its actual interaction
    study; do not reassign PduD/CDE binding merely by analogy.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated discussion rationale and posed_date; append historical context
    and update current prompt/notes only where needed. No record edits are made in
    this review PR.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0031472
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/microcompartment/propanediol_degradation_polyhedral_organelle.yaml
    role: maintained scientific record
  description: Use the verified PduM family grounding and reconcile the label-only
    note, preserving organism-specific examples and the model-qualified assembly role.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated discussion rationale and posed_date; append historical context
    and update current prompt/notes only where needed. No record edits are made in
    this review PR.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  description: Ground AcrA to its verified family and narrow the remaining open grounding
    task to AcrB. Preserve exact protein references, source stoichiometry and the
    distinction between a protein family and the complete pump.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated discussion rationale and posed_date; append historical context
    and update current prompt/notes only where needed. No record edits are made in
    this review PR.
- action_id: micro-A5
  finding_ids:
  - micro-F5
  target_ids:
  - cellstructuremech:acrab_tolc_multidrug_efflux_transport_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acrab_tolc_multidrug_efflux_transport_complex.yaml
    role: maintained scientific record
  description: In authorized curation, narrow all3CPX notes to the actually curated
    stoichiometric participants/physical interaction evidence, or attach an explicit
    source supporting any retained formation-necessity claim. Keep the valid contributes-to
    edges, exact6:3:3counts and protein identities.
  acceptance_checks:
  - Do not infer biological dispensability from unspecified source role or missing
    depletion experiments.
  - Preserve dated history/rationale; append current correction provenance through
    native guarded curation.
  - Native schema/graph/identifier checks pass; no records edited in this review-only
    PR.
limitations:
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Four assigned records are independently reassessed and nonstale. No scientific findings/actions,
  no invented predecessor or terminal resolution; all four retain positive qualified
  passes. Only four formal applicability exclusions are confirmed review-bundle defects.
  The tentative cohort-label concern was withdrawn: complete scope notes correctly
  identify the original batch26 execution reused with same-base guards.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  All current source responses are freshly retrieved with actual timestamps and SHA256.
  Earlier HTTP200 challenge pages, DNS failures, XML404/500 are validation context
  only. Genuine recovered bodies have separate receipts. Karcher2009, Jensen2012,
  Kucej/Butow2007 and Ogbadoyi2003 remain complete-abstract scopes; the fetched Ogbadoyi
  body is not claimed read.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Kobayashi2015 is primary comparative research. Only specified Introduction, Methods,
  first Results/Table1/Fig1–2 captions and two Discussion subsections were read. No
  image pixels, remaining Results/Methods, supplements or experimental reanalysis;
  purified proteins/heterologous E.coli compaction are not universal in vivo plastid
  formation tests.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Amodeo2023 is secondary review at sec1/8/10 scope. Cooper2019 body scopes distinguish391
  minicircle sequence classes from copy-number estimates in EATRO1125-derived cultured
  populations. deSouza2017 KAP1/2 restrictions and aKAP23 non-DNA localization constrain
  class interpretation. Gluenz2011 microscopy scope is procyclic T.brucei, not all
  kinetoplastid architectures.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Kucej2008 whole scientific main text and specified Methods/captions were read: isolated-mitochondrion
  in organello ChIP and about70% sampled intronless genome are explicit despite the
  authors own in vivo interpretation. Sia2009 full short main text/Table1/captions
  distinguish repeated-sequence instability from point mutation and respiratory selection
  from fermentative mtDNA loss. No pixels, supplements or new data analysis.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Q02486/ABF2 reviewed S288C identity and unique exact query are current. HLP zero
  exact-query result is bounded index noncoverage, not absence of a literature-supported
  protein. Native HLP/KAP nodes are HAS_SYMBOLS_NO_EXAMPLES, Abf2 is COVERED and plastid
  inventory is empty. Optional examples are not invented.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  IPR000119 is broader HU/IHF context; IPR009071 is a domain, and IPR051965 has unchecked
  LLM-generated prose that is not accepted as biological proof. No exact source-neutral
  family equivalence or exhaustive composition is certified.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Actual whole-record positive molecular claims trigger all four applicability checks.
  Current full catalogue has no matching eukaryotic host; no unrelated bacterial proxy/downstream
  query, no biological absence inference. Historical runner failure at00:49Z is not
  a fresh invocation.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Thirty frozen inputs actually informed this subreview:17 common policies/config/helper
  inputs,4 targets,8 original artifacts and one already-frozen generic-nucleoid boundary
  context. Original pairs validate/render exactly and all61 historical inputs match.
  Generic-neighbor science/disposition belongs to its assigned reviewer; no cross-target
  resolution inferred.'
- 'Chloroplast, kinetoplast, mitochondrial and plastid nucleoid independent subreview:
  Root owns current global gates, native final save, committed-head checks, CI and
  queue. This source-stage report does not certify future execution or perform record/Git/GitHub
  writes. Append-only history and unresolved scientific unknowns remain preserved.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Three unchanged
  targets independently reassessed. Three original pairs validate/render exactly;
  all44historical input rows match. One inherited major nucleoid identity finding
  retained; glucan synthase and ACF qualified passes. No new scientific finding established
  and no records/repository/GitHub mutated.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Primary body scope:
  Wang2011 complete scientific main text/in-text experimental details, without supplementary
  Methods/TableS1 or pixels; Gelbart2001 sec2,6,14,15 andFig4/5 text captions; McConnell2004
  sec3,9 andFig1/2 text captions. No supplements, raw data, individual images or complete
  separately cited-reference audit. Verma2019 is secondary synthesis, sec002 including
  subsections/tables/text captions andsec010,014,015; Dillon2010 secondary abstract
  only.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Glucan Douglas1994,
  Mazur1995, Qadota1996, Mazur/Baginsky1996, Mol1994 and Utsugi/Dijkgraaf/Sickmann
  annotation sources were read at complete deposited abstract/metadata scope only.
  PMCchallenge/guessedS3 404 responses do not count as bodies. FKS1 mitochondrial
  native evidence joins are verified annotation provenance, not independent mitochondrial-localization
  confirmation. No detailed experimental protocols or formation assay claimed.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Seven K-12 NAP
  examples and three/two S288C glucan/ACF examples are all reviewed. Native identities/coverage
  do not certify every mechanistic edge or experimental strain. Gelbart uses W303-derivedW1588-4C;
  native S288C accession mapping remains distinct. UNKNOWN formation necessity retained;
  activity/deletion phenotypes are not universal assembly requirements.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Nucleoid graph
  is bacterial coarse secondary synthesis with protein/concentration/magnesium/growth-phase
  limits and unresolved in-vivo domain barriers. Heterogeneous NAP cohort does not
  mean every protein performs every action. Generic nucleoid identity includes organellar
  children; current bacterial-only definition remains material scope defect.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Exact five InterPro
  candidates are bounded checks, not an exhaustive family-catalogue search. HU/IHF
  family is not whole NAP pool; GT48/WAC/Isw domains and Rho family are broader than
  the selected components. Existing open grounding discussions remain scientifically
  legitimate; no optional empty-slot or enum-only finding.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Fresh official
  catalogue has E.coli coverage and no Saccharomyces entry. e_coli/precise1k is a
  mixed five-strain dataset with201modules and4257genes; selected String511145 loci
  map to maintained K-12 examples, not all experimental conditions. Seven exact gene
  searches followed by all201membership flags and selected OxyR3/RpoS51/ppGpp145 metadata
  show dps andfis contexts; five other NAPs have no trueflags, not biological absence.
  AI summaries and activities excluded; no direct localization/necessity/causal inference.'
- 'Generic nucleoid, glucan synthase and ACF independent subreview: Historical adapter
  runner failure is actual00:49Z evidence only, no new invocation or fresh success.
  Current direct public-source fallback is separate. Unused dermatology PMID15611425
  request was an irrelevant scratch fetch and is excluded from evidence/assessments.
  Frontend-only genes endpoint is access context only. Root owns wider gates/issues/publication;
  pending CI/queue/merge not certified.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Only the three
  assigned full records receive scientific dispositions. Other batch records and neighbor/category
  issue states are not inferred.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Every primary-source
  body row states exact read sections. Metadata/abstract rows do not certify unseen
  body, figures, supplements or raw experiments. No source images, cryo-EM maps, protein
  coordinates, spectra or supplementary movies were reanalyzed; there are no maintained
  images in these targets.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Wheatley2013,Sutter2021,Bobik1997/Bobik1999,Cheng2011,
  Sinha2014 and Held2016 are bounded to the complete native abstract/metadata or explicitly
  cited native annotation checks. Held2016 recombinant Eut scope is not independent
  proof of every native Pdu localization.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Yang2020 abundance
  depends on QconCAT assumptions. Yang2022 EP condensation and specific PduM/PduB
  molecular contacts remain proposed models; shell/cargo convergence is supported
  without claiming new atomic contacts or one exclusive trajectory.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Pdu cohort
  CONDITIONAL labels are not a complete condition-by-member necessity matrix. Hca
  biochemical architecture includes sequence/family inference; whole-cell Hca assays
  also include downstream HcaB. Acr5V5S is engineered and does not independently test
  formation necessity.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Native protein
  verification checks implemented identities/xrefs/coverage, not biological membership
  or subclass correctness. PduCDE STRUCTURE is outside the GENE_OR_PROTEIN diagnostic
  summary; its exact examples were separately inspected.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Structured
  runner availability evidence is historical00:49Z, not a new attempt. Fresh official
  source fallback inspected selected multi-strain e_coli/precise1k and s_enterica/core
  only. Module membership, nonmembership or missing locus coverage is not assembly/phenotype/localization
  evidence. Generated ai_summary and raw condition activities were not used.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Initial guessed
  module/metadata query-form endpoints returned frontend HTML; those responses were
  rejected as scientific data. Failed S3 routes and one unrelated guessed PMC candidate
  were not read as supporting sources; genuine successfully retrieved identities were
  checked separately.'
- 'Pdu organelle, Hca dioxygenase and AcrAB-TolC independent subreview: Root owns
  corpus QC, final CI, queue and publication. This source report does not certify
  later committed-head CI or merge outcomes. No records, original bundles, repository
  refs or GitHub objects were changed by this reviewer.'
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
- 'This immutable successor corrects review-bundle issues #2832 and #2833: two stale
  target inputs are substantively reassessed; ten unsupported source-applicability
  exclusions (seven formal, three prose) are replaced by actual whole-record applicability,
  official catalogue checks and covered-source queries.'
- Pdu new PduCDE STRUCTURE typing and two added convergent-biogenesis edges are assessed
  alongside the original PduU class and BMC-T cargo-receptor findings. AcrAB-TolC
  new membership edges are supported, while three added CPX notes misattribute essentiality
  and are separately scoped for later record curation.
- Acr source-attribution correction does not reject defining-material ESSENTIAL values,
  assert dispensability or require new formation assays. Five inherited findings retain
  exact predecessor identities; the new CPX finding has no invented predecessor.
- All 47 used local inputs are frozen; the source commit is retained by review-base/pr2380-current-record-followup-20261103.
  All20 original review files remain byte-identical. No scientific record, history,
  generated page or other branch is edited.
- The batch26 historical execution wording was challenged and retained because full
  scope notes explicitly document its original execution and batch43 same-base reuse.
  No defect or issue is asserted for that accurate provenance.
- Native inventory is31 represented protein examples and20 GENE_OR_PROTEIN nodes;
  documented verification and causal-node commands all passed. Empty optional examples
  and legitimate group actors are not manufactured findings.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042547Z-propanediol-degradation-polyhedral-organelle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042548Z-chloroplast-nucleoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042549Z-kinetoplast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042550Z-mitochondrial-nucleoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042551Z-nucleoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042551Z-plastid-nucleoid-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042552Z-1-3-beta-d-glucan-synthase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042554Z-acf-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T042555Z-acrab-tolc-multidrug-efflux-transport-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2380
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2832
- https://github.com/CultureBotAI/CellStructureMech/issues/2833
- https://github.com/CultureBotAI/CellStructureMech/issues/2834
- https://github.com/CultureBotAI/CellStructureMech/issues/2835
- https://github.com/CultureBotAI/CellStructureMech/issues/2836
- https://github.com/CultureBotAI/CellStructureMech/issues/2837
- https://github.com/CultureBotAI/CellStructureMech/issues/2838
- https://github.com/CultureBotAI/CellStructureMech/issues/2839
```
