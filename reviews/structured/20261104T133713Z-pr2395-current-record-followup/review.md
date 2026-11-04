# PR 2395: current-input review of ten records and adversarial follow-up

- Review: 20261104T133713Z-pr2395-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T13:16:07.533152Z
- Finished UTC: 2026-11-04T13:37:13Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Independent whole-record reassessment of ten current records retains ten inherited scientific findings and establishes one new minor m-AAA source-count finding: eleven minor findings across seven records needing curation. The inherited Isw1 major finding is explicitly narrowed to a minor class/variant scope inconsistency with bounded action. Isw1a, Isw1b and LYSP100-associated nuclear domain pass with limitations. Three stale reviews are substantively refreshed; seven current targets match their original frozen bytes. The immutable successor corrects ten applicability assessments, 23 historical access-only evidence occurrences and six native receipt/hash bindings, preserving all original artifacts and access boundaries. Every scientific action is linked to a separate open record-curation issue; no records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main b508909649f4f7b0b2f11ea4d3ee5a45f09081fd. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 95ad1b68018d096f0e86328b39d87b6c288e5790.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base f9ac707415c382929b15517997efaa11ec96230d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0016587 | data/structures/other/isw1_complex.yaml | maintained | Isw1 complex |
| GO:0036436 | data/structures/other/isw1a_complex.yaml | maintained | Isw1a complex |
| GO:0036437 | data/structures/other/isw1b_complex.yaml | maintained | Isw1b complex |
| GO:0000776 | data/structures/other/kinetochore.yaml | maintained | kinetochore |
| GO:0043564 | data/structures/other/ku70_ku80_complex.yaml | maintained | Ku70:Ku80 complex |
| GO:0062051 | data/structures/other/lipopolysaccharide_transport_system.yaml | maintained | lipopolysaccharide transport system |
| cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml | maintained | LolCDE lipoprotein ABC transporter complex |
| GO:0016606 | data/structures/other/lysp100_associated_nuclear_domain.yaml | maintained | LYSP100-associated nuclear domain |
| GO:0005745 | data/structures/other/m_aaa_complex.yaml | maintained | m-AAA complex |
| GO:1990196 | data/structures/other/macab_tolc_complex.yaml | maintained | MacAB-TolC complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | Native TraitMech check passed: all 10 links resolve with matching labels against the 1130-trait source index. |
| Pinned governed files | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | All 22 governed artifacts match the pinned CLAW revision. |
| Native identifier resolver | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified all 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0016587 | passed | True | GO:0016587 | Documented focused command passed. |
| validate-strict GO:0016587 | passed | True | GO:0016587 | Documented focused command passed. |
| validate GO:0036436 | passed | True | GO:0036436 | Documented focused command passed. |
| validate-strict GO:0036436 | passed | True | GO:0036436 | Documented focused command passed. |
| validate GO:0036437 | passed | True | GO:0036437 | Documented focused command passed. |
| validate-strict GO:0036437 | passed | True | GO:0036437 | Documented focused command passed. |
| validate GO:0000776 | passed | True | GO:0000776 | Documented focused command passed. |
| validate-strict GO:0000776 | passed | True | GO:0000776 | Documented focused command passed. |
| validate GO:0043564 | passed | True | GO:0043564 | Documented focused command passed. |
| validate-strict GO:0043564 | passed | True | GO:0043564 | Documented focused command passed. |
| validate GO:0062051 | passed | True | GO:0062051 | Documented focused command passed. |
| validate-strict GO:0062051 | passed | True | GO:0062051 | Documented focused command passed. |
| validate cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | passed | True | cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | Documented focused command passed. |
| validate-strict cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | passed | True | cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | Documented focused command passed. |
| validate GO:0016606 | passed | True | GO:0016606 | Documented focused command passed. |
| validate-strict GO:0016606 | passed | True | GO:0016606 | Documented focused command passed. |
| validate GO:0005745 | passed | True | GO:0005745 | Documented focused command passed. |
| validate-strict GO:0005745 | passed | True | GO:0005745 | Documented focused command passed. |
| validate GO:1990196 | passed | True | GO:1990196 | Documented focused command passed. |
| validate-strict GO:1990196 | passed | True | GO:1990196 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | All ten positive molecular narratives trigger structured-source applicability. The complete fresh official catalogue has 20 organism rows and 28 organism/dataset pairs, without the relevant yeast, human or mouse biological hosts; recombinant hosts are not proxies. For the three E. coli transport records, exact e_coli/precise1k joins cover 15 loci and their complete 201-module membership tables. lptA/lptB/lptC/tolC join module22 (SoxS), lpp module45 (Resistance), and lptF module167 (UC-2); the other nine loci have zero thresholded flags. Full module member tables contain 117, 58 and 96 genes. The five-strain expression dataset is not an exact experimental-strain match, physical-assembly evidence or evidence of biological absence. Generated summaries are excluded. Historical runner PermissionError retains its actual November3 timestamp; fresh native packets have their own access times. |
| Independent claim-level source review | passed | True | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native Isw1 complex UniProt verify check | passed | True | GO:0016587 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Isw1 complex UniProt causal check | passed | True | GO:0016587 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Isw1a complex UniProt verify check | passed | True | GO:0036436 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Isw1a complex UniProt causal check | passed | True | GO:0036436 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Isw1b complex UniProt verify check | passed | True | GO:0036437 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Isw1b complex UniProt causal check | passed | True | GO:0036437 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native kinetochore UniProt verify check | passed | True | GO:0000776 | 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native kinetochore UniProt causal check | passed | True | GO:0000776 | 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Ku70:Ku80 complex UniProt verify check | passed | True | GO:0043564 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Ku70:Ku80 complex UniProt causal check | passed | True | GO:0043564 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native lipopolysaccharide transport system UniProt verify check | passed | True | GO:0062051 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native lipopolysaccharide transport system UniProt causal check | passed | True | GO:0062051 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native LolCDE lipoprotein ABC transporter complex UniProt verify check | passed | True | cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native LolCDE lipoprotein ABC transporter complex UniProt causal check | passed | True | cellstructuremech:lolcde_lipoprotein_abc_transporter_complex | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native LYSP100-associated nuclear domain UniProt verify check | passed | True | GO:0016606 | 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native LYSP100-associated nuclear domain UniProt causal check | passed | True | GO:0016606 | 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native m-AAA complex UniProt verify check | passed | True | GO:0005745 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native m-AAA complex UniProt causal check | passed | True | GO:0005745 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MacAB-TolC complex UniProt verify check | passed | True | GO:1990196 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native MacAB-TolC complex UniProt causal check | passed | True | GO:1990196 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Frozen original/current artifacts

schema: supported. Targets: GO:0016587.

Complete assigned target is nonstale. Eight original validate/render commands pass; 61 historical input occurrences match original source revisions. Original artifacts are immutable and current targets equal reviewed main.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0016587.

Original formal no-iModulon-specific-claim exclusion is unsupported by the positive constituent/chromatin-remodeling narrative. Positive molecular claims require assessment. The actual complete current catalogue has no Saccharomyces host, so no unmatched downstream proxy is used. Historical runner failure is not fresh.

### Actual native protein inventory

schema: supported. Targets: GO:0016587.

2 maintained reviewed examples and the same number of COVERED typed nodes; eight total current commands across these targets exit zero. Correct accession joins do not independently certify generic component scope or scientific evidence.

### Historical tasks and current grounding claims

provenance: supported. Targets: GO:0016587.

Dated history/rationale remains append-only. Current source-neutral grounding tasks are separate from species-protein examples; no old rationale must be rewritten to mimic a present inventory. No whole-category closure or record edits.

### Historical and current source kinds

evidence: concern. Targets: GO:0016587.

Seven historical diagnostic access rows require kind-only correction; their original limits were already honest. Genuine original Vary/Koike reads are not denied. Fresh body/abstract/authority reads have distinct dates; metadata and access failures are not upgraded.

### Frozen original/current artifacts

schema: supported. Targets: GO:0036436.

Complete assigned target is nonstale. Eight original validate/render commands pass; 61 historical input occurrences match original source revisions. Original artifacts are immutable and current targets equal reviewed main.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0036436.

Original formal no-iModulon-specific-claim exclusion is unsupported by the positive constituent/chromatin-remodeling narrative. Positive molecular claims require assessment. The actual complete current catalogue has no Saccharomyces host, so no unmatched downstream proxy is used. Historical runner failure is not fresh.

### Actual native protein inventory

schema: supported. Targets: GO:0036436.

2 maintained reviewed examples and the same number of COVERED typed nodes; eight total current commands across these targets exit zero. Correct accession joins do not independently certify generic component scope or scientific evidence.

### Historical tasks and current grounding claims

provenance: supported. Targets: GO:0036436.

Dated history/rationale remains append-only. Current source-neutral grounding tasks are separate from species-protein examples; no old rationale must be rewritten to mimic a present inventory. No whole-category closure or record edits.

### Historical and current source kinds

evidence: concern. Targets: GO:0036436.

Seven historical diagnostic access rows require kind-only correction; their original limits were already honest. Genuine original Vary/Koike reads are not denied. Fresh body/abstract/authority reads have distinct dates; metadata and access failures are not upgraded.

### Frozen original/current artifacts

schema: supported. Targets: GO:0036437.

Complete assigned target is nonstale. Eight original validate/render commands pass; 61 historical input occurrences match original source revisions. Original artifacts are immutable and current targets equal reviewed main.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0036437.

Original formal no-iModulon-specific-claim exclusion is unsupported by the positive constituent/chromatin-remodeling narrative. Positive molecular claims require assessment. The actual complete current catalogue has no Saccharomyces host, so no unmatched downstream proxy is used. Historical runner failure is not fresh.

### Actual native protein inventory

schema: supported. Targets: GO:0036437.

3 maintained reviewed examples and the same number of COVERED typed nodes; eight total current commands across these targets exit zero. Correct accession joins do not independently certify generic component scope or scientific evidence.

### Historical tasks and current grounding claims

provenance: supported. Targets: GO:0036437.

Dated history/rationale remains append-only. Current source-neutral grounding tasks are separate from species-protein examples; no old rationale must be rewritten to mimic a present inventory. No whole-category closure or record edits.

### Historical and current source kinds

evidence: concern. Targets: GO:0036437.

Seven historical diagnostic access rows require kind-only correction; their original limits were already honest. Genuine original Vary/Koike reads are not denied. Fresh body/abstract/authority reads have distinct dates; metadata and access failures are not upgraded.

### Frozen original/current artifacts

schema: supported. Targets: GO:0043564.

Complete assigned target is nonstale. Eight original validate/render commands pass; 61 historical input occurrences match original source revisions. Original artifacts are immutable and current targets equal reviewed main.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0043564.

Original YAML and derived Markdown contain no formal or prose iModulon/transcriptomic applicability assessment; this is an omission, not an expression-only exclusion. Positive molecular claims require assessment. The actual complete current catalogue has no Saccharomyces host, so no unmatched downstream proxy is used. Historical runner failure is not fresh.

### Actual native protein inventory

schema: supported. Targets: GO:0043564.

2 maintained reviewed examples and the same number of COVERED typed nodes; eight total current commands across these targets exit zero. Correct accession joins do not independently certify generic component scope or scientific evidence.

### Historical tasks and current grounding claims

provenance: supported. Targets: GO:0043564.

Dated history/rationale remains append-only. Current source-neutral grounding tasks are separate from species-protein examples; no old rationale must be rewritten to mimic a present inventory. No whole-category closure or record edits.

### Historical and current source kinds

evidence: concern. Targets: GO:0043564.

Two historical diagnostic access rows require kind-only correction; their original limits were already honest. Genuine original Vary/Koike reads are not denied. Fresh body/abstract/authority reads have distinct dates; metadata and access failures are not upgraded.

### Generic and subtype ontology boundaries

identity: supported. Targets: GO:0016587.

Current active GO0016587 remains the generic Isw1 class with two exact is_a children GO0036436/37 under ISWI-type complex. Generic and subtype records may coexist; one canonical Isw1a example is not itself a faulty universal definition.

### Broad accessory class versus specific constituent description

identity: concern. Targets: GO:0016587.

The generic accessory row labels Ioc3 in Isw1a and Ioc2/Ioc4 in Isw1b, but its role and graph-node description call the same row specific to Isw1a. Vary resolves distinct assemblies. Generic functional classes and a single representative example are allowed; a correction must target actual inconsistent scope or family attribution, not merely heterogeneous proteins or missing optional examples.

### Expanded definition source

provenance: concern. Targets: GO:0016587.

GO0016587 directly supports only the opening generic definition. The extra promoter-proximal/coding-region and cryptic-transcription clauses are not contained in that GO definition; Vary addresses separate complexes and biochemical/genetic outcomes. Native protein annotations support some later specialization but do not make the declared GO source support every added clause. This is a claim-specific provenance gap, not proof those biological clauses are false.

### Membership/function graph status

graph: concern. Targets: GO:0016587.

Every represented edge is either a constituent is-part-of relation or whole-complex chromatin remodeling. MECHANISTIC status and assembly/mechanism title overstate the encoded detail; NONMECHANISTIC with precise scope is sufficient without forcing new steps or experiments.

### Species example and reference/assay strain

scope: supported. Targets: GO:0016587.

S. cerevisiae is the actual organism. Vary uses W303-derived RAD5-repaired strains, not S288C; current protein examples explicitly represent S288C annotations. COMMON is a qualitative occurrence assertion, not a newly measured clade-wide frequency or an exhaustive isolate census.

### Physical association and activity limits

evidence: supported. Targets: GO:0016587.

Reciprocal co-IP/TAP purification supports distinct complexes. Ioc2/Ioc4 mutual stable association under tested extraction conditions is separate from global assembly necessity; activity, spacing/sliding and growth/transcription phenotypes are distinct assays. Current UNKNOWN classifications need not be changed. The Isw1b record already includes the conditional association evidence.

### Exact family versus verified domain candidates

grounding: unknown. Targets: GO:0016587.

Current inspected Isw1/2 N-terminal, SNF2-like, WHIM1, PWWP and IOC2-region candidates are domains or broad domain superfamilies where successfully resolved. They do not establish exact whole Isw1/Ioc classes. REVIEWED_LABEL_ONLY remains boundedly justified; no exhaustive absence, forced broad-family mapping or independent sequence alignment is claimed. Initial three rate-limit responses are retained separately.

### Source-dependent remodeling results

evidence: supported. Targets: GO:0016587.

Both purified assemblies have nucleosome-stimulated ATPase activity. Spacing/sliding and binding differ under recombinant nucleosome/DNA substrates, competitor, concentration and extraction conditions; those results do not prescribe universal in-vivo rates or genomic occupancy. Transcript measurements establish condition-specific expression effects, not a complete mechanistic pathway.

### Species example and reference/assay strain

scope: supported. Targets: GO:0036436.

S. cerevisiae is the actual organism. Vary uses W303-derived RAD5-repaired strains, not S288C; current protein examples explicitly represent S288C annotations. COMMON is a qualitative occurrence assertion, not a newly measured clade-wide frequency or an exhaustive isolate census.

### Physical association and activity limits

evidence: supported. Targets: GO:0036436.

Reciprocal co-IP/TAP purification supports distinct complexes. Ioc2/Ioc4 mutual stable association under tested extraction conditions is separate from global assembly necessity; activity, spacing/sliding and growth/transcription phenotypes are distinct assays. Current UNKNOWN classifications need not be changed. The Isw1b record already includes the conditional association evidence.

### Exact family versus verified domain candidates

grounding: unknown. Targets: GO:0036436.

Current inspected Isw1/2 N-terminal, SNF2-like, WHIM1, PWWP and IOC2-region candidates are domains or broad domain superfamilies where successfully resolved. They do not establish exact whole Isw1/Ioc classes. REVIEWED_LABEL_ONLY remains boundedly justified; no exhaustive absence, forced broad-family mapping or independent sequence alignment is claimed. Initial three rate-limit responses are retained separately.

### Source-dependent remodeling results

evidence: supported. Targets: GO:0036436.

Both purified assemblies have nucleosome-stimulated ATPase activity. Spacing/sliding and binding differ under recombinant nucleosome/DNA substrates, competitor, concentration and extraction conditions; those results do not prescribe universal in-vivo rates or genomic occupancy. Transcript measurements establish condition-specific expression effects, not a complete mechanistic pathway.

### Species example and reference/assay strain

scope: supported. Targets: GO:0036437.

S. cerevisiae is the actual organism. Vary uses W303-derived RAD5-repaired strains, not S288C; current protein examples explicitly represent S288C annotations. COMMON is a qualitative occurrence assertion, not a newly measured clade-wide frequency or an exhaustive isolate census.

### Physical association and activity limits

evidence: supported. Targets: GO:0036437.

Reciprocal co-IP/TAP purification supports distinct complexes. Ioc2/Ioc4 mutual stable association under tested extraction conditions is separate from global assembly necessity; activity, spacing/sliding and growth/transcription phenotypes are distinct assays. Current UNKNOWN classifications need not be changed. The Isw1b record already includes the conditional association evidence.

### Exact family versus verified domain candidates

grounding: unknown. Targets: GO:0036437.

Current inspected Isw1/2 N-terminal, SNF2-like, WHIM1, PWWP and IOC2-region candidates are domains or broad domain superfamilies where successfully resolved. They do not establish exact whole Isw1/Ioc classes. REVIEWED_LABEL_ONLY remains boundedly justified; no exhaustive absence, forced broad-family mapping or independent sequence alignment is claimed. Initial three rate-limit responses are retained separately.

### Source-dependent remodeling results

evidence: supported. Targets: GO:0036437.

Both purified assemblies have nucleosome-stimulated ATPase activity. Spacing/sliding and binding differ under recombinant nucleosome/DNA substrates, competitor, concentration and extraction conditions; those results do not prescribe universal in-vivo rates or genomic occupancy. Transcript measurements establish condition-specific expression effects, not a complete mechanistic pathway.

### Exact stable subtype and constituent identities

identity: supported. Targets: GO:0036436.

Isw1a is the supported Isw1-Ioc3 assembly. Active exact GO and primary purification agree. The broader Isw1 parent is is_a; neither subtype is silently replaced by a four-protein superassembly.

### Complete bounded composition/function graph

graph: supported. Targets: GO:0036436.

All constituent membership and broad remodeling edges agree with actual source. NONMECHANISTIC status and explicit limits correctly avoid claiming ATP hydrolysis, nucleosome-recognition or a temporal sliding/assembly mechanism not represented by the graph.

### Exact stable subtype and constituent identities

identity: supported. Targets: GO:0036437.

Isw1b is the supported Isw1-Ioc2-Ioc4 assembly. Active exact GO and primary purification agree. The broader Isw1 parent is is_a; neither subtype is silently replaced by a four-protein superassembly.

### Complete bounded composition/function graph

graph: supported. Targets: GO:0036437.

All constituent membership and broad remodeling edges agree with actual source. NONMECHANISTIC status and explicit limits correctly avoid claiming ATP hydrolysis, nucleosome-recognition or a temporal sliding/assembly mechanism not represented by the graph.

### Ku heterodimer and parent boundary

identity: supported. Targets: GO:0043564.

Active GO0043564 denotes the two-class Ku70:Ku80 heterodimer, with exact nuclear-complex parent. It is not identity-equivalent to DNA-PK or prokaryotic Ku homodimers. Generic GO/review V(D)J and DNA-PK wording is not asserted as a yeast graph function.

### Two resolvable whole-subunit classes

grounding: concern. Targets: GO:0043564.

Current exact IPR006165 Ku70 and IPR024193 Ku80 family identities and native P32807/Q04437 cross-references resolve the existing deferred task. Shared IPR006164 is only a DNA-binding domain. This is positive class evidence, not an optional accession or a requirement that families be complex-exclusive.

### Yeast binding/repair and mammalian context

evidence: supported. Targets: GO:0043564.

Complete primary abstracts for Feldmann and Boulton support the bounded yeast heterodimer/end-binding, repair and telomere observations. Koike is explicitly secondary and separates mammalian DNA-PK/V(D)J context; Downs remains metadata only. No unread primary body or cross-species formation experiment is asserted.

### Global UNKNOWN and experimental limits

scope: supported. Targets: GO:0043564.

Binding loss, repair defects and mammalian subunit stabilization are not automatically yeast assembly necessity. Preserve permissive UNKNOWN values and the two-subunit defining boundary; no isolated-formation experiment is mandated.

### Complete NONMECHANISTIC membership/output graph

graph: supported. Targets: GO:0043564.

The two constituent membership relations and broad DNA-end-binding/NHEJ outputs are scoped to composition and function. No detailed synapsis, DNA-PK recruitment or ligation sequence is invented; GO exact process labels and primary abstract scopes support the coarse representation.

### Yeast occurrence and reference localization

scope: supported. Targets: GO:0043564.

Species4932 canonical context and two reviewed S288C reference examples are distinct. Current UniProt cites Laroche1998 for nuclear/telomere location; exact complete abstract is read, not the primary microscopy body. COMMON is not an experimentally measured prevalence statistic across isolates.

### Verified citation identities and annotation scopes

evidence: supported. Targets: GO:0016587, GO:0036436, GO:0036437, GO:0043564.

Huh and Laroche exact author/title/PMID identities and complete indexed abstracts match native citation provenance. Current proteins independently provide nuclear annotations. No Huh or Laroche body/pixel assay is certified, and location alone is not used as proof of physical membership.

### Narrow inherited severity and action scope

provenance: concern. Targets: GO:0016587.

Original F1 major severity and separate-classes framing overstate the independently confirmed residual. The generic definition already distinguishes two assemblies; generic functional classes and representative examples are allowed. Retain exact predecessor/key as a minor internal wording/scope finding, with a bounded correction that permits the generic class and requires no row/type/example expansion.

### Current native contract and immutable historical proof

schema: supported. Targets: GO:0062051.

Current complete record and original review schema/history were checked. Native original validate/render pass and original frozen hashes match. Current source bytes are unchanged for LPS/MacAB; LolCDE is substantively refreshed separately.

### Current native example identity and diagnostic limits

grounding: supported. Targets: GO:0062051.

Seven reviewed K-12 examples and seven covered typed nodes; actual gene names and current accessions agree. This does not settle exact class grounding or paper-level membership.

### Required whole-record structured-source cross-check

completeness: concern. Targets: GO:0062051.

Original YAML has no formal or prose iModulon applicability assessment. Positive seven-protein transport and gene/pathway assertions trigger assessment. Exact full YAML was searched recursively, including notes/checks/evidence; this is an omission, not an explicit N/A.

### Exact matched dataset and downstream computational context

scope: supported. Targets: GO:0062051.

Full fresh catalogue and precise1k metadata distinguish five strains from reference locus511145 and from actual assay constructs. Exact15-gene join and complete201-module memberships were followed by module22/45/167 metadata/member tables. lptA/B/C,tolC→22; lpp→45; lptF→167; other9 zero true flags. No expression correlation or threshold absence is treated as physical assembly, transport, necessity or biological absence.

### Original source access and evidence-kind audit

provenance: supported. Targets: GO:0062051.

Own original evidence kinds and access locators were inspected; no access-only or secondary-as-primary defect was established for these three bundles. Fresh failed routes are validation/context_only; metadata is database/context_only; primary abstracts/captions retain limited tiers. Original source timestamps remain historical. No new successful runner invocation is claimed.

### Image and source-access limits

evidence: not_applicable. Targets: GO:0062051.

No maintained local image is present in the inspected cohort. Source text captions may inform bounded experiments, but no figure pixels, raw maps or supplementary data were inspected and no image audit is certified.

### Historical rationale and record-curation boundary

provenance: supported. Targets: GO:0062051.

Original reviews and historical rationale remain immutable. Findings/actions address current fields with dated append-only discussion updates if needed. No neighbor, category or previous closed issue is resolved by inference. Root owns issues and all repository mutations.

### Current native contract and immutable historical proof

schema: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Current complete record and original review schema/history were checked. Native original validate/render pass and original frozen hashes match. Current source bytes are unchanged for LPS/MacAB; LolCDE is substantively refreshed separately.

### Current native example identity and diagnostic limits

grounding: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Three reviewed K-12 examples and three covered constituent nodes; the fourth typed node is the nonconstituent Lpp/Pal substrate and is accurately UNANCHORED_WITH_UNIPROT. It need not become a transporter component.

### Required whole-record structured-source cross-check

completeness: concern. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Original checks[4] explicitly says no expression-module inference is used. That does not exempt the named LolC/D/E proteins, transport pathway and Lpp/Pal substrate assertions. All are checked in matched E. coli context.

### Exact matched dataset and downstream computational context

scope: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Full fresh catalogue and precise1k metadata distinguish five strains from reference locus511145 and from actual assay constructs. Exact15-gene join and complete201-module memberships were followed by module22/45/167 metadata/member tables. lptA/B/C,tolC→22; lpp→45; lptF→167; other9 zero true flags. No expression correlation or threshold absence is treated as physical assembly, transport, necessity or biological absence.

### Original source access and evidence-kind audit

provenance: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Own original evidence kinds and access locators were inspected; no access-only or secondary-as-primary defect was established for these three bundles. Fresh failed routes are validation/context_only; metadata is database/context_only; primary abstracts/captions retain limited tiers. Original source timestamps remain historical. No new successful runner invocation is claimed.

### Image and source-access limits

evidence: not_applicable. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

No maintained local image is present in the inspected cohort. Source text captions may inform bounded experiments, but no figure pixels, raw maps or supplementary data were inspected and no image audit is certified.

### Historical rationale and record-curation boundary

provenance: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Original reviews and historical rationale remain immutable. Findings/actions address current fields with dated append-only discussion updates if needed. No neighbor, category or previous closed issue is resolved by inference. Root owns issues and all repository mutations.

### Current native contract and immutable historical proof

schema: supported. Targets: GO:1990196.

Current complete record and original review schema/history were checked. Native original validate/render pass and original frozen hashes match. Current source bytes are unchanged for LPS/MacAB; LolCDE is substantively refreshed separately.

### Current native example identity and diagnostic limits

grounding: supported. Targets: GO:1990196.

Three reviewed K-12 examples and three covered typed nodes. Current exact MacA, MacB and TolC family names and example mappings agree; generated MacB family prose is excluded.

### Required whole-record structured-source cross-check

completeness: concern. Targets: GO:1990196.

Original checks[4] explicitly says no expression-module inference is used. Positive MacA/MacB/TolC efflux and pathway assertions require actual matched source coverage assessment.

### Exact matched dataset and downstream computational context

scope: supported. Targets: GO:1990196.

Full fresh catalogue and precise1k metadata distinguish five strains from reference locus511145 and from actual assay constructs. Exact15-gene join and complete201-module memberships were followed by module22/45/167 metadata/member tables. lptA/B/C,tolC→22; lpp→45; lptF→167; other9 zero true flags. No expression correlation or threshold absence is treated as physical assembly, transport, necessity or biological absence.

### Original source access and evidence-kind audit

provenance: supported. Targets: GO:1990196.

Own original evidence kinds and access locators were inspected; no access-only or secondary-as-primary defect was established for these three bundles. Fresh failed routes are validation/context_only; metadata is database/context_only; primary abstracts/captions retain limited tiers. Original source timestamps remain historical. No new successful runner invocation is claimed.

### Image and source-access limits

evidence: not_applicable. Targets: GO:1990196.

No maintained local image is present in the inspected cohort. Source text captions may inform bounded experiments, but no figure pixels, raw maps or supplementary data were inspected and no image audit is certified.

### Historical rationale and record-curation boundary

provenance: supported. Targets: GO:1990196.

Original reviews and historical rationale remain immutable. Findings/actions address current fields with dated append-only discussion updates if needed. No neighbor, category or previous closed issue is resolved by inference. Root owns issues and all repository mutations.

### Seven-member transenvelope Lpt identity

identity: supported. Targets: GO:0062051.

GO0062051 and direct GO1990351 parent retain the seven Lpt classes. MsbA flips LPS upstream and is not an eighth constituent. Biological scope is E. coli and source-qualified diderm transport, not uniform essentiality across all bacteria.

### Seven exact families versus current label-only notes

grounding: concern. Targets: GO:0062051.

Current exact family types/signatures and independently mapped reviewed examples support LptA IPR014340, LptB IPR030921, LptC IPR026265, LptD IPR020889, LptE IPR007485, LptF IPR030922, LptG IPR030923. Retain species exceptions and distinguish F/G. Older five-member background is not current composition evidence.

### ATP-driven extraction and bridge source scope

graph: supported. Targets: GO:0062051.

Sherman reconstitution supports all-seven transport and association; Okuda distinguishes ATP-dependent LPS extraction/transfer from ATP-independent LptA/C contact; Chng2010 copurification supports transenvelope association. The coarse graph does not resolve physiological LptA count or imply every function-loss phenotype is failure to assemble.

### 2010 proposal versus 2011 contact-mapping support

provenance: concern. Targets: GO:0062051.

The retained edge6 evidence1 says Chng2010 demonstrated plug/barrel architecture. Its Discussion is conditional; Freinkman2011 supplies later contact mapping supporting buried plug topology. Correct the evidential-stage attribution while retaining valid LptD/E partnership, and do not describe 2011 as an atomic structure.

### Localization, function and necessity distinctions

scope: supported. Targets: GO:0062051.

Native abstracts support LptA periplasm, LptC periplasmic domain/LPS binding and ordered transfer, LptF/G inner membrane and LptD/E outer membrane. Depletion/viability and altered membrane fractions are not automatically direct formation tests; no universal necessity or optional formation experiment is imposed.

### Specific LolCDE release complex

identity: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Local identity is narrower than GO0043190 ABC-transporter parent. CPX4262/7MDY give LolC1:LolD2:LolE1; GO0140306 release contributes to GO0044874 outer-membrane localization. LolA/B handoff is pathway context, not extra LolCDE constituents.

### Exact LolC/D/E family mappings

grounding: concern. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Current exact native families and independent example xrefs support LolC NCBIfamNF008076, LolD InterProIPR011924 and LolE NCBIfamNF008357. Broad LolC/E IPR011925 and LolD-like IPR015854 are near misses, not substitutes. Historical search rationale remains historical.

### Substantive refresh of added Lpp/Pal substrate scope

scope: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Fresh Yakushi abstract and public captions1,3,4,7 support ATP/LolA-dependent Pal proteoliposome release, Lpp release in DLP79-22 spheroplast assays and Asp+2 sorting. Current K-12 reference xrefs identify Lpp/Pal but are distinct from exact assay strains. No inaccessible full-body or figure-pixel inspection is claimed.

### Added membership and release-localization edges

graph: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

New descriptions call LolC/D/E essential stoichiometric constituents, while evidence notes accurately state CPX explicit1:2:1 counts and PDB assembled heterotetramer. CPX physical-interaction evidence has LolD enzyme and LolC/E unspecified bioRole; it is not a deletion-essentiality annotation. Unlike explicit false CPX essentiality attributions, these notes support defining membership. Retain contributes-to and bounded release-localization; do not infer universal assembly indispensability or demand a depletion assay.

### Structural state and assay limits

scope: supported. Targets: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex.

Sharma2021 K-12 genes expressed in BL21(DE3), His-LolD purification and nucleotide cryo-EM support the heterotetramer/state model. Basal ATPase, Lpp K58-deletion copurification and density interpreted as lipoprotein do not independently prove every substrate sequence or direct transport kinetics. Coarse NONMECHANISTIC graph preserves this limit.

### MacAB-TolC ordered core and current families

identity: supported. Targets: GO:1990196.

GO1990196/GO1990195 identity and ordered PDB5NIK model support MacB2:MacA6:TolC3. Exact MacA IPR058623, MacB IPR050250 and TolC IPR058622 match the separate current reviewed examples. The engineered fusion/disulfide stabilization and expression host are retained limits.

### Macrolide-subclass preference versus broader cargo

scope: concern. Targets: GO:1990196.

Current definition faithfully quotes current GO, yet its unqualified specific-to14/15-membered-macrolides sentence overrestricts total cargo. Kobayashi2001 abstract gives the tested resistance profile; independent Yamanaka2008 primary abstract documents BL21(DE3) STII secretion/rescue and Turlin2014 abstract documents E. coli PPIX efflux under stated perturbations. Fitzpatrick2017 introduction cites broader reports rather than assaying every listed cargo. Preserve that distinction.

### Correct Lin2009 bibliographic attribution

provenance: concern. Targets: GO:1990196.

The exact PMID18955484 title/authors/DOI and genuine primary body identify Lin et al. 2009. Two current notes name Tikhonova et al. 2009 despite correct PMID and supported assays; correct those names without changing biological conclusions.

### Assembly, ATPase and translocation evidence

graph: supported. Targets: GO:1990196.

Lin2009 detergent pulldowns, MacB dimer biophysics and ATPase/erythromycin assays support interactions and functional coupling in stated conditions; 2017 structure supports periplasmic portal/gating interpretation. These do not certify universal subunit-deletion formation necessity or all ATP-cycle steps; UNKNOWN remains acceptable.

### Native reference versus assay hosts

scope: supported. Targets: GO:1990196.

Reviewed examples and native assembly entities map to K-12 references. W3110 source genes/C43(DE3) ΔacrAB expression, KAM3(DE3) transport assays and BL21(DE3) STII experiments remain distinct; the multi-strain precise1k data are only bounded computational context.

### Original native schema/render and historical inputs

schema: supported. Targets: GO:0000776.

Three originals validate/render exactly and39 historical input occurrences match. Current target changed; exact old/current delta is scientifically reassessed, not accepted by hash alone. Schema/provenance checks are not scientific proof.

### Actual protein inventories and coverage

consistency: supported. Targets: GO:0000776.

Thirteen reviewed S288C examples; one typed Cse4 node COVERED. Native coverage validates representative identity but does not resolve whole-nucleosome grounding/actor type or prove full kinetochore formation.

### Dated reasoning and current clarifications

provenance: supported. Targets: GO:0000776.

Dated history and search/access rationale remain provenance. Current source availability does not retroactively invalidate earlier failures; any curation updates current fields or appends clarification without rewriting dated history. No other-record/group disposition is inferred.

### Positive molecular claims and actual host coverage

evidence: supported. Targets: GO:0000776.

Whole record asserts CSE4/COMA/MIND/Ndc80 chromosome-attachment pathways. Actual coverage assessment is required. Fresh complete official catalogue has no matching biological host, so downstream dataset queries are not applicable and primary/authority fallback is retained. Absence of expression inference alone is not the reason.

### Historical source kinds and access boundaries

provenance: supported. Targets: GO:0000776.

No separate access-only evidence row mislabeled as a scientific source was identified in this assigned original. Failed routes are explicitly scoped limitations next to genuine alternative bodies/abstracts; genuine Lee Methods access is not reclassified as failed merely because another route failed.

### Original native schema/render and historical inputs

schema: supported. Targets: GO:0016606.

Three originals validate/render exactly and39 historical input occurrences match. Current target equals its historical frozen input. Schema/provenance checks are not scientific proof.

### Actual protein inventories and coverage

consistency: supported. Targets: GO:0016606.

One reviewed human SP140 example; one COVERED SP140 node and one UNANCHORED_WITH_UNIPROT external Bright/ARID3A Q99856. The external regulator is intentionally not a stable constituent; no missing optional inventory defect.

### Dated reasoning and current clarifications

provenance: supported. Targets: GO:0016606.

Dated history and search/access rationale remain provenance. Current source availability does not retroactively invalidate earlier failures; any curation updates current fields or appends clarification without rewriting dated history. No other-record/group disposition is inferred.

### Positive molecular claims and actual host coverage

evidence: supported. Targets: GO:0016606.

Whole record asserts SP140/Bright regulation and enhancer transcription. Actual coverage assessment is required. Fresh complete official catalogue has no matching biological host, so downstream dataset queries are not applicable and primary/authority fallback is retained. Absence of expression inference alone is not the reason.

### Historical source kinds and access boundaries

provenance: supported. Targets: GO:0016606.

No separate access-only evidence row mislabeled as a scientific source was identified in this assigned original. Failed routes are explicitly scoped limitations next to genuine alternative bodies/abstracts; genuine Lee Methods access is not reclassified as failed merely because another route failed.

### Original native schema/render and historical inputs

schema: supported. Targets: GO:0005745.

Three originals validate/render exactly and39 historical input occurrences match. Current target changed; exact old/current delta is scientifically reassessed, not accepted by hash alone. Schema/provenance checks are not scientific proof.

### Actual protein inventories and coverage

consistency: supported. Targets: GO:0005745.

Two reviewed S288C examples and two COVERED typed protein nodes. Native validation does not certify newly asserted source counts, experimental W303 identity or formation necessity.

### Dated reasoning and current clarifications

provenance: supported. Targets: GO:0005745.

Dated history and search/access rationale remain provenance. Current source availability does not retroactively invalidate earlier failures; any curation updates current fields or appends clarification without rewriting dated history. No other-record/group disposition is inferred.

### Positive molecular claims and actual host coverage

evidence: supported. Targets: GO:0005745.

Whole record asserts Yta10/Yta12/PHB protein processing and ATP-dependent proteolysis. Actual coverage assessment is required. Fresh complete official catalogue has no matching biological host, so downstream dataset queries are not applicable and primary/authority fallback is retained. Absence of expression inference alone is not the reason.

### Historical source kinds and access boundaries

provenance: supported. Targets: GO:0005745.

No separate access-only evidence row mislabeled as a scientific source was identified in this assigned original. Failed routes are explicitly scoped limitations next to genuine alternative bodies/abstracts; genuine Lee Methods access is not reclassified as failed merely because another route failed.

### Whole kinetochore and constituent boundaries

identity: supported. Targets: GO:0000776.

GO0000776 is exact; COMA GO0000817, MIND GO0000444 and Ndc80 GO0031262 are specific subcomplexes. Selective early inventory is explicit; no unsupported complete yeast inventory or centromeric DNA-as-component inference.

### New CSE4 representative and retained platform identity

identity: concern. Targets: GO:0000776.

New reviewed P36012/CSE4/CSL2/YKL049C S288C example matches native authority and a current exact one-result query. Its PMID14581449 nuclear-centromere annotation is independently supported by Cse4-containing material in Westermann. This correct representative does not resolve F1: the maintained component/graph actor still denotes the whole CENP-A nucleosome, whose exact current class is GO0043505.

### Twelve preexisting complex references

identity: supported. Targets: GO:0000776.

The twelve COMA/MIND/Ndc80 examples retain reviewed S288C identities, exact primary genes and current one-result queries. Native protein examples are source-strain references, not proof every cited experiment used S288C.

### Purification, localization and source-specific strains

evidence: supported. Targets: GO:0000776.

De Wulf W303-congenic hydrodynamic/co-purification and Westermann tagged300mMKCl material support the selected yeast core. Schmitzberger2017 abstract specifically studies recombinant Kluyveromyces lactis COMA; it is not S288C primary experimental evidence. Ancillary native localization citations remain abstract-tier and do not replace direct body evidence.

### Conditional dependencies versus complete formation

completeness: unknown. Targets: GO:0000776.

Conditional mutations change protein abundance, stability, CEN occupancy and segregation; those endpoints do not uniformly abolish the entire kinetochore. De Wulf retains residual COMA subcomplexes; Biggins explicitly treats minimal assembly requirements and Cse4 stoichiometry as unresolved. UNKNOWN is reasonable; no universal necessity mandate.

### Coarse assembly hierarchy and class grounding

graph: concern. Targets: GO:0000776.

NONMECHANISTIC assembly scope honestly describes a coarse inner/outer map. COMA bridge/MIND recruitment/Ndc80 outer role are supported, without importing every omitted subcomplex. F1 aligns the complete Cse4 nucleosome actor to its exact structural class; it is not a generic objection to all protein-complex actor types.

### Taxon and prevalence limits

scope: supported. Targets: GO:0000776.

Saccharomyces is a supported canonical model; COMMON is qualitative scope, not a measured prevalence census. Human homology and Kluyveromyces structural comparisons do not change the maintained yeast assembly scope.

### No claimed target image inspection

scope: supported. Targets: GO:0000776.

No maintained image is present. Genuine bodies and embedded captions were read; no Westermann/De Wulf/Biggins figure pixels, supplements or raw biochemical measurements were analyzed.

### Exact nuclear domain and physical boundary

identity: supported. Targets: GO:0016606.

GO0016606/its LANDs synonym and nuclear-body parent are exact. Morphological globular/electron-dense distinction from annular PML bodies is supported at GO and Dent complete-abstract scope. Nuclear-lumen parthood is biological localization, not falsely claimed as direct current ontology edge.

### SP140 isoform and external Bright reference

identity: supported. Targets: GO:0016606.

Q13342 is reviewed human SP140 with LYSP100 alias; displayed isoform LYSp100-B and alternative forms are distinguished. Q99856 is reviewed human ARID3A/Bright, an external cross-reference. It does not identify the species of every construct in the J558/HeLa study; the record does not make it a stable constituent.

### Broad family/domain candidates remain nonexact

grounding: supported. Targets: GO:0016606.

IPR043563/PTHR46386 span SP110/SP140/SP140L and other reviewed members; IPR030411 is a bromodomain, not whole LYSp100B. These current native classifications do not justify forcing the exact retained component into a broader family/domain. No exhaustive absence claim or optional-example mandate.

### Human identity and variable localization

scope: supported. Targets: GO:0016606.

Dent complete abstract supports human lymphoid protein and HeLa expression/localization. Zong directly studies ectopic nuclear dots, partial overlap and Bright-driven redistribution in HeLa and J558; this does not establish all endogenous isoforms or all human lineages. VARIABLE does not purport to be a population census.

### Reporter coactivation and interaction limits

evidence: supported. Targets: GO:0016606.

Zong shows stronger Bright-dependent E-mu CAT output in J558 reporter cells; HeLa/Jurkat do not share that coactivation. In-vitro LYSp100B–Bright interaction is supported, whereas in-vivo co-IP was not detected. Existing broad modulation and redistribution descriptions remain bounded; no direct endogenous chromatin-remodeling mechanism is asserted.

### Unknown formation-specific requirement

completeness: unknown. Targets: GO:0016606.

Defining enrichment, transfection redistribution and reporter activity do not establish that SP140 or Bright is universally required to form all LANDs. Existing UNKNOWN and discussion boundaries are appropriate; no required new experiment.

### Nonmechanistic regulatory observations

graph: supported. Targets: GO:0016606.

NONMECHANISTIC regulation graph distinguishes SP140-enriched LANDs, PML bodies and external Bright; redistribution and reporter modulation are observed endpoints, not a resolved direct causal chain from nuclear-body disruption to enhancer activity. PML/SP100/Bright are not silently promoted to stable constituents.

### Main text versus abstract and visual limits

scope: supported. Targets: GO:0016606.

Zong genuine full-body sections/captions were read after failed/challenged routes. Dent/Bloch/Gong are complete-abstract only; Gong supplies native nuclear-annotation context, not LAND membership evidence. No target image, source figure pixels or supplements inspected.

### Exact complex, ancestry and matrix-facing protease

identity: supported. Targets: GO:0005745.

GO0005745 and parents GO0098800/GO1905368 remain exact; membrane parthood is correctly inherited through the inner-membrane complex class. CPX retains real Yta10/Yta12 and zinc membership; no universal PHB- or substrate-containing assembly is inferred.

### Native aliases, reference strain and exact families

identity: supported. Targets: GO:0005745.

P39925 primaryAFG3 aliasYTA10 and P40341 primaryYTA12 aliasRCA1 are reviewed S288C references with current one-result queries. IPR050928/005936 are broader shared families and IPR011546 is a domain. Unchecked machine-generated IPR050928 prose is excluded; no narrow paralog family is invented.

### Reference, preparation and assay organisms

scope: supported. Targets: GO:0005745.

CPX numeric559292 is S288C despite generic species label; released EMD1712 uses species4932 preparation metadata; Lee uses YKO200-derived variants; Luo uses W303-1B endogenous replacements. These contexts remain distinct; human/Ct PHB experiments do not become yeast atomistic evidence.

### New constituent edges and source-count attribution

evidence: concern. Targets: GO:0005745.

All three added actors/relation types have real membership/cofactor support. However CPX participant counts are null, not3:3 or6zinc as the new edge notes state. EMD1712/Lee support a scoped3:3 preparation/model, not an unqualified universal structure; six zinc is not supplied by either inspected count source. One new minor finding corrects attribution/scope without rejecting heteromer or cofactor biology.

### EMDB preparation and map resolution

scope: supported. Targets: GO:0005745.

EMD1712 supersedes1543; cross-linked detergent/ATP/C6 preparation and12angstrom header match. Lee specifically reports ATPase Trap mutants and inability to distinguish homologous subunits at this resolution; alternation is assigned using prior biochemistry. Sample0.5MDa versusCPX1000kDa is not forced into one physiological mass.

### Reporter maturation versus flux

evidence: supported. Targets: GO:0005745.

Luo Fig4 distinguishes precursor/total C-terminal Strep MrpL32 after14hYPG30C in four biological replicates. PHB1/SIM perturbations lower precursor fraction and IMSD replacement raises it. These data do not measure endogenous untagged flux or ribosome incorporation; current descriptions expressly retain those limits.

### Respiratory peroxide response

evidence: supported. Targets: GO:0005745.

Figure4c/d serial dilution assays at30C distinguish48hYPD and72hYPG with/without2mMH2O2. PHB1 re-expression partially rescues; SIM/IMSD states differ from whole-protein deletion. Separate growth endpoint does not establish processing causes stress sensitivity.

### Co-assembly versus perturbation phenotype

completeness: unknown. Targets: GO:0005745.

Membership and preparation architecture support real assembly; current domain-replacement processing phenotypes do not directly establish abolished oligomer formation. Lee engineered homo-oligomer rescue and wild-type heteromer behavior are source-specific. No universal essentiality or new depletion experiment is requested.

### Bounded intervention-response graph

graph: supported. Targets: GO:0005745.

MECHANISTIC REGULATION is appropriate for the existing experiment-bounded interventions and assayed responses. It neither draws a processing-to-stress edge nor claims a resolved atomic yeast PHB interface. Newly inserted count/source statements are separately flagged, while contribution/cofactor relations remain.

### Actual Fig4 pixels and link-only attribution

scope: supported. Targets: GO:0005745.

External native Fig4 panelsA–D were visually inspected and match the biochemical/growth caption. MD5 and CC BY-NC-ND4.0 authors/license match current record; OTHER correctly retains exact license URL. No maintained local image file or hosted derivative is introduced.

### Independent current disposition

consistency: concern. Targets: GO:0000776.

Needs curation: 1 minor finding; inherited exact grounding gap remains after valid CSE4 refresh. Review-bundle applicability/staleness corrections are separate from record curation.

### Independent current disposition

consistency: supported. Targets: GO:0016606.

Pass with limitations: no supported new record finding; source conditions, reference identity and unknown formation limits are retained. Review-bundle applicability/staleness corrections are separate from record curation.

### Independent current disposition

consistency: concern. Targets: GO:0005745.

Needs curation: 1 minor finding; new source-count mismatch in stale-edge refresh, without invented predecessor. Review-bundle applicability/staleness corrections are separate from record curation.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0016587, GO:0036436, GO:0036437, GO:0000776, GO:0043564, GO:0062051, cellstructuremech:lolcde_lipoprotein_abc_transporter_complex, GO:0016606, GO:0005745, GO:1990196.

3 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Align the Isw1 accessory class and variant wording

minor / open / confirmed; issue key: isw1-generic-subtype-component-conflation.

The generic definition already distinguishes Isw1a and Isw1b, and a broad functional accessory class is permitted. However, components[1] and its graph node label include Ioc3 in Isw1a and Ioc2/Ioc4 in Isw1b while the same row role/grounding notes and node description categorically call it Isw1a-specific. Clarify this internal class/variant scope. Nonhomology, PROTEIN type or a single Ioc3 example alone do not establish an identity error or require additional examples.

### micro-F2: Source the added definition claims

minor / open / confirmed; issue key: isw1-expanded-definition-source.

The expanded definition attributes promoter-proximal Isw1a, coding-region Isw1b and cryptic-transcription suppression to definition_source GO0016587, whose actual definition states only an Isw1-containing chromatin-modifying complex. The record does not provide claim-specific support for all added scope and functions.

### micro-F3: Align the graph status with its represented evidence

minor / open / confirmed; issue key: isw1-membership-graph-scope.

The MECHANISTIC status and mechanism title describe a graph consisting of constituent membership and one broad chromatin-remodeling edge. These claims establish composition and function but do not themselves encode a mechanism.

### micro-F4: Ground the two Ku subunit classes

minor / open / confirmed; issue key: ku70-ku80-exact-subunit-families.

Ku70/Yku70 and Ku80/Yku80 remain REVIEWED_LABEL_ONLY despite exact whole-family identities IPR006165 and IPR024193. Native family types/signatures and separately verified yeast protein cross-references corroborate both mappings.

### plaque-t5-F1: Ground the seven named Lpt protein classes

minor / open / confirmed; issue key: lpt-seven-exact-subunit-families.

All seven named subunits remain REVIEWED_LABEL_ONLY despite exact current families: LptA IPR014340, LptB IPR030921, LptC IPR026265, LptD IPR020889, LptE IPR007485, LptF IPR030922 and LptG IPR030923. Family types/signatures and separate native protein cross-references support these class mappings.

Disposition: Independently reconfirmed against current record and freshly inspected native/primary sources; remains open for separately authorized record curation.

### plaque-t5-F2: Separate the 2010 plug model from later demonstration

minor / open / confirmed; issue key: lpt-chng2010-plug-barrel-attribution.

The evidence note on the LptE-to-LptD edge says Chng2010 DOI10.1073/pnas.0912872107 demonstrated the plug-and-barrel architecture. That paper characterizes LptD/E and explicitly discusses alternative arrangements conditionally. Freinkman2011 PMID21257904 supplies the later contact-mapping support.

Disposition: Independently reconfirmed against current record and freshly inspected native/primary sources; remains open for separately authorized record curation.

### plaque-t6-F1: Ground the three exact LolCDE subunit families

minor / open / confirmed; issue key: lolcde-exact-subunit-families.

All three protein rows remain REVIEWED_LABEL_ONLY while native full-family identities and independent example membership now resolve their retained classes. Exact mappings are LolC NCBIfam:NF008076, LolD InterPro:IPR011924 and LolE NCBIfam:NF008357; the new supported graph edges do not repair this current grounding gap. Preserve dated discussion rationale.

Disposition: Independently reconfirmed against current record and freshly inspected native/primary sources; remains open for separately authorized record curation.

### plaque-t9-F1: Qualify the macrolide-specificity sentence

minor / open / confirmed; issue key: macab-substrate-specificity-qualification.

The definition says transport activity is specific to14/15-membered macrolides, while its cited structural source and retained broader function cover other cargo. The sentence is faithfully inherited from current GO, but that provenance does not remove its overexclusive reading. Fresh independent primary abstracts for E. coli STII secretion and PPIX efflux corroborate broader cargo, with assay/strain limits; the structural paper introduction is not itself a direct assay of every cargo.

Disposition: Independently reconfirmed against current record and freshly inspected native/primary sources; remains open for separately authorized record curation.

### plaque-t9-F2: Correct the2009paper author attribution

minor / open / confirmed; issue key: macab-lin2009-author-attribution.

Two evidence notes call PMID18955484 Tikhonova etal2009. The exact native identity and full primary body identify LinHT etal2009; the DOI and biological conclusions remain correct.

Disposition: Independently reconfirmed against current record and freshly inspected native/primary sources; remains open for separately authorized record curation.

### septin-kinetochore-F1: Ground the named CENP-A nucleosome class

minor / open / confirmed; issue key: kinetochore-cenpa-nucleosome-grounding.

The centromeric Cse4/CENP-A nucleosome platform remains REVIEWED_LABEL_ONLY despite active exact GO0043505, CENP-A containing nucleosome. Its native definition and primary Cse4/H3 replacement context match the named class. The linked graph node labels and references this complete nucleosome platform, so its current GENE_OR_PROTEIN typing should be aligned to the structural class in the same correction. The newly added correct CSE4 representative does not change the complete nucleosome actor/class. Preserve dated rationale; update current class grounding with no inferred fixed nucleosome stoichiometry.

### septin-m_aaa_complex-F1: Correct m-AAA graph count attribution and preparation scope

minor / open / confirmed; issue key: m-aaa-stoichiometry-source-scope.

The three new constituent edges attribute3xYta10,3xYta12 and6xZn to CPX-1654. The complete current CPX response leaves all participant stochiometry fields null. EMD1712 explicitly records3+3 proteins for its cross-linked detergent preparation; Lee describes roughly equimolar Trap-mutant material and a C6 model unable to distinguish paralogs. Neither inspected CPX response nor EMDB header supplies six zinc ions. Thus the edge source notes and unqualified count wording overstate these sources and conflict with retained scoped component/dataset notes. This does not refute heteromer formation, zinc membership, or a possible independently supported six-ion model.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, align the accessory component and graph-node label with their stated variant scope. An explicitly generic functional accessory class with qualified Isw1a/Isw1b roles and evidence is valid; alternatively narrow the row to its represented variant while preserving the generic structure identity.

- The same component and graph node do not simultaneously include Isw1b constituents in their label and categorically describe their whole scope as Isw1a-specific.
- Keep the already stated Isw1a/Isw1b distinction and valid representative examples. No mandatory row split, component-type change, extra example inventory or all-Ioc single-complex assertion is required.
- Do not treat a generic functional class as an assertion that all Ioc proteins form a homologous family.
- Preserve dated history and rationale; use current clarification or appended scope.
- Retain permissible UNKNOWN formation values and avoid new experimental demands.
- Run applicable native checks after separately authorized curation; no record edit occurs in this review PR.

### micro-A2

In separately authorized record curation, keep the GO-backed definition bounded, or support the added scientific clauses with directly checked sources and explicit scope.

- Distinguish support for subtype composition from promoter/coding-region localization and cryptic-transcription suppression.
- Do not label those biological claims false merely because the declared GO definition does not establish them.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated history and discussions.rationale; put current clarifications in current notes or appended scope.
- Retain valid existing examples and permissible UNKNOWN values; do not mandate optional examples or new experiments.
- No maintained record is edited in this review PR.

### micro-A3

In separately authorized record curation, declare the present graph nonmechanistic with precise scope notes, or separately curate source-supported causal steps.

- Do not turn a membership relation into an assembly or activity dependency without assay evidence.
- Preserve the source-supported broad chromatin-remodeling function.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve dated history and discussions.rationale; put current clarifications in current notes or appended scope.
- Retain valid existing examples and permissible UNKNOWN values; do not mandate optional examples or new experiments.
- No maintained record is edited in this review PR.

### micro-A4

In separately authorized record curation, ground Ku70 to IPR006165 and Ku80 to IPR024193, retaining yeast roles, examples and UNKNOWN assembly necessity.

- Each mapping identifies the correct whole subunit family.
- Shared Ku domain IPR006164 is not used as an exact whole-subunit identity.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated history and discussions.rationale; put current clarifications in current notes or appended scope.
- Retain valid existing examples and permissible UNKNOWN values; do not mandate optional examples or new experiments.
- No maintained record is edited in this review PR.

### plaque-t5-A1

Ground the seven named subunit classes to the exact verified families, retaining role evidence and species exceptions. Keep LptF and LptG distinct.

- Each family matches the named whole protein class and its reviewed example.
- No broad ABC, shared LptF/G or isolated domain is substituted; historical search claims remain historical.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve append-only historical rationale; any current clarification is dated and source-scoped. No universal formation necessity or new experiment is required by this action.

### plaque-t5-A2

Change the2010 note to its demonstrated biochemical characterization/proposed arrangement, and cite the later directly relevant2011 study for the architecture claim.

- Each citation is attached to the claim and epistemic stage actually supported.
- The valid LptD/E insertion relationship is retained without claiming the2010 paper solved the later architecture.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve append-only historical rationale; any current clarification is dated and source-scoped. No universal formation necessity or new experiment is required by this action.

### plaque-t6-A1

Map LolC to NCBIfam:NF008076, LolD to InterPro:IPR011924 and LolE to NCBIfam:NF008357; retain correct examples,1:2:1 architecture and source-specific scope.

- Do not substitute the broader LolC/E or LolD-like classes for these exact subunit families.
- Preserve supported source-specific claims and pass applicable native gates.
- Preserve append-only historical rationale; any current clarification is dated and source-scoped. No universal formation necessity or new experiment is required by this action.

### plaque-t9-A1

State the14/15-membered preference as the reported macrolide-subclass profile, and preserve the broader source-supported transport scope with an appropriate source.

- Do not change the supported2:6:3 identity or claim every cargo listed in introductory context was assayed by the structural study.
- Preserve supported source-specific claims and pass applicable native gates.
- Preserve append-only historical rationale; any current clarification is dated and source-scoped. No universal formation necessity or new experiment is required by this action.

### plaque-t9-A2

Replace the two author-name attributions with Lin etal2009 while retaining the exact PMID and supported assay descriptions.

- Check both the function evidence and the first causal-edge evidence note.
- Preserve supported source-specific claims and pass applicable native gates.
- Preserve append-only historical rationale; any current clarification is dated and source-scoped. No universal formation necessity or new experiment is required by this action.

### septin-kinetochore-A1

Ground the existing component to GO0043505 with a current scope note. Preserve its Cse4 yeast role, OTHER constituent representation and unknown stoichiometry/formation limits. Align the corresponding whole-nucleosome graph node to STRUCTURE with the same exact GO grounding, retaining the component_ref.

- The adopted term denotes the nucleosome class rather than Cse4 alone or generic chromatin.
- The graph actor denotes the whole nucleosome platform, not Cse4 alone, and its node type/grounding agree with that identity.
- No fixed octameric arrangement or universal formation necessity is inferred from the class mapping.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated rationale/history and append current clarification; representative P36012 identity remains correct.

### septin-m_aaa_complex-A1

In separately authorized record curation, remove false CPX count attribution, scope3:3 protein counts explicitly to the released EMD1712/Lee preparation/model, and omit or independently support the six-zinc assertion. Retain Yta10/Yta12 co-assembly and zinc cofactor relations, experimental graph limits and correctly scoped composition/dataset fields.

- CPX notes reflect unspecified participant counts; no3:3 or6Zn is attributed to CPX-1654.
- Any3:3 statement identifies the actual preparation/model source and its engineered/detergent/C6 limits.
- Six zinc is either omitted as an unsupported quantity or supported by an exact independently verified source; do not infer it is biologically false.
- Preserve dated discussion/history; current clarification may be appended without rewriting historical source-access observations.
- Do not demand new experiments, universal alternative stoichiometry, dispensability claims or mandatory essentiality changes.
- Run native schema/strict/identifier gates after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/isw1_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912; current SHA256 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/isw1a_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865; current SHA256 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/isw1b_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137; current SHA256 da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/kinetochore.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 aefa8aee06e9c0d6c20b86cf110f44bd6ead107d28e5ae579027cf07a957bf9e; current SHA256 ea8645dec5b13874441be4fa7a2db0b477265d3c23ecd399aa9559824428640d. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261022T080129Z-kinetochore-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/ku70_ku80_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44; current SHA256 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/lipopolysaccharide_transport_system.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e; current SHA256 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T080130Z-lipopolysaccharide-transport-system-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 9bc1e320681a91bb883829715c5e4db10330c4f5505b7155f8485e6e662d0f80; current SHA256 96bf1ce75ce606af29c2d8a549c345e9487f0e426ac1f86823f14db22c651866. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/lysp100_associated_nuclear_domain.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493; current SHA256 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T080132Z-lysp100-associated-nuclear-domain-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/m_aaa_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 799f2eef086fc6c2f621ee63a5b1293feaf04cb48bcf31743bff7988497991a6; current SHA256 9686eb96f5b95da3c8b9dbb002841e31ac5c884c66e4af52f05706b375ea87a7. Changed record reassessed against current sources. |
| original-review-8 | reviews/structured/20261022T080133Z-m-aaa-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/macab_tolc_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636; current SHA256 b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T080133Z-macab-tolc-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/isw1_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-0 | reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; Complete immutable original native review and deterministic Markdown | context_only | Original findings/actions, evidence kinds and stated source tiers, checks, verdict and limitations audited. Historical access is not retrospectively upgraded by fresh retrieval. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/0-stale.diff; Actual diff original source revision to reviewed main | context_only | Empty record delta; original frozen target and current main byte-identical. |
| micro-record-1 | data/structures/other/isw1a_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-1 | reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; Complete immutable original native review and deterministic Markdown | context_only | Original findings/actions, evidence kinds and stated source tiers, checks, verdict and limitations audited. Historical access is not retrospectively upgraded by fresh retrieval. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/1-stale.diff; Actual diff original source revision to reviewed main | context_only | Empty record delta; original frozen target and current main byte-identical. |
| micro-record-2 | data/structures/other/isw1b_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-2 | reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; Complete immutable original native review and deterministic Markdown | context_only | Original findings/actions, evidence kinds and stated source tiers, checks, verdict and limitations audited. Historical access is not retrospectively upgraded by fresh retrieval. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/2-stale.diff; Actual diff original source revision to reviewed main | context_only | Empty record delta; original frozen target and current main byte-identical. |
| micro-record-3 | data/structures/other/ku70_ku80_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-3 | reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml; Complete immutable original native review and deterministic Markdown | context_only | Original findings/actions, evidence kinds and stated source tiers, checks, verdict and limitations audited. Historical access is not retrospectively upgraded by fresh retrieval. |
| micro-delta-3 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/4-stale.diff; Actual diff original source revision to reviewed main | context_only | Empty record delta; original frozen target and current main byte-identical. |
| micro-policy | docs/CURATION.md; Components, Evidence and Discussions sections | context_only | Components may denote taxon-agnostic families or classes. Specific class identities, roles, claims and evidence must agree; optional examples are not an exhaustive inventory. Formation necessity differs from activity/viability. Dated rationale is append-only. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum and graph scope fields | context_only | Reviewed-label-only needs a reason; UNKNOWN is valid and neither generic classes nor sparse examples alone establish defects. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Whole graph-kind/scope, actor and edge-evidence contract | context_only | Membership and broad function can be represented as NONMECHANISTIC. No mandatory detailed assembly pathway or universal necessity inference follows from a coarse graph. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Full review workflow and structured-source applicability | context_only | Positive molecular/function/pathway assertions trigger actual source applicability, independently of expression-specific claims. |
| micro-native-config | conf/record_review.yaml; Full configured checks/rubrics | context_only | Read native configured workflow; root owns corpus gates and successor publication. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/original-audit.json; Eight actual original native validate/render commands; 61 historical input occurrences; eight original artifacts | supports | All eight commands exit zero, original Markdown equals renderer output byte-for-byte, all declared historical inputs match their revision/hash and original PR artifacts are immutable. |
| micro-protein-P38144 | https://rest.uniprot.org/uniprotkb/P38144.json; Current status/name, full gene primary/alias/locus fields, organism; complete FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-P38144.raw | supports | P38144: UniProtKB reviewed (Swiss-Prot); ISWI chromatin-remodeling complex ATPase ISW1; taxon 559292; genes [{'geneName': {'value': 'ISW1'}, 'orderedLocusNames': [{'value': 'YBR245C'}], 'orfNames': [{'value': 'YBR1633'}]}]; InterPro ['IPR014001', 'IPR001650', 'IPR009057', 'IPR044754', 'IPR015194', 'IPR036306', 'IPR027417', 'IPR001005', 'IPR017884', 'IPR015195', 'IPR038718', 'IPR049730', 'IPR000330']. Reference annotation, native citation provenance and actual experimental preparations are distinguished. |
| micro-protein-P43596 | https://rest.uniprot.org/uniprotkb/P43596.json; Current status/name, full gene primary/alias/locus fields, organism; complete FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-P43596.raw | supports | P43596: UniProtKB reviewed (Swiss-Prot); ISWI one complex protein 3; taxon 559292; genes [{'geneName': {'value': 'IOC3'}, 'orderedLocusNames': [{'value': 'YFR013W'}]}]; InterPro ['IPR028942']. Reference annotation, native citation provenance and actual experimental preparations are distinguished. |
| micro-protein-Q12072 | https://rest.uniprot.org/uniprotkb/Q12072.json; Current status/name, full gene primary/alias/locus fields, organism; complete FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-Q12072.raw | supports | Q12072: UniProtKB reviewed (Swiss-Prot); ISWI one complex protein 2; taxon 559292; genes [{'geneName': {'value': 'IOC2'}, 'orderedLocusNames': [{'value': 'YLR095C'}]}]; InterPro ['IPR063422', 'IPR062587', 'IPR062429', 'IPR011011']. Reference annotation, native citation provenance and actual experimental preparations are distinguished. |
| micro-protein-Q04213 | https://rest.uniprot.org/uniprotkb/Q04213.json; Current status/name, full gene primary/alias/locus fields, organism; complete FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-Q04213.raw | supports | Q04213: UniProtKB reviewed (Swiss-Prot); ISWI one complex protein 4; taxon 559292; genes [{'geneName': {'value': 'IOC4'}, 'orderedLocusNames': [{'value': 'YMR044W'}], 'orfNames': [{'value': 'YM9532.09'}]}]; InterPro ['IPR035503', 'IPR000313']. Reference annotation, native citation provenance and actual experimental preparations are distinguished. |
| micro-protein-P32807 | https://rest.uniprot.org/uniprotkb/P32807.json; Current status/name, full gene primary/alias/locus fields, organism; complete FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-P32807.raw | supports | P32807: UniProtKB reviewed (Swiss-Prot); ATP-dependent DNA helicase II subunit 1; taxon 559292; genes [{'geneName': {'value': 'YKU70'}, 'synonyms': [{'value': 'HDF1'}, {'value': 'NES24'}], 'orderedLocusNames': [{'value': 'YMR284W'}], 'orfNames': [{'value': 'YM8021.10'}]}]; InterPro ['IPR006164', 'IPR006165', 'IPR047087', 'IPR005160', 'IPR005161', 'IPR016194', 'IPR036465']. Reference annotation, native citation provenance and actual experimental preparations are distinguished. |
| micro-protein-Q04437 | https://rest.uniprot.org/uniprotkb/Q04437.json; Current status/name, full gene primary/alias/locus fields, organism; complete FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-Q04437.raw | supports | Q04437: UniProtKB reviewed (Swiss-Prot); ATP-dependent DNA helicase II subunit 2; taxon 559292; genes [{'geneName': {'value': 'YKU80'}, 'synonyms': [{'value': 'HDF2'}], 'orderedLocusNames': [{'value': 'YMR106C'}], 'orfNames': [{'value': 'YM9718.05C'}]}]; InterPro ['IPR006164', 'IPR024193', 'IPR005161', 'IPR016194', 'IPR036465']. Reference annotation, native citation provenance and actual experimental preparations are distinguished. |
| micro-query-IOC2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full exact reviewed gene/taxon result page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-IOC2.raw | supports | One current reviewed result ['Q12072'], matching primary gene and S288C taxon; all alias/locus fields inspected. This does not reconstruct the dated historical query execution. |
| micro-query-IOC3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full exact reviewed gene/taxon result page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-IOC3.raw | supports | One current reviewed result ['P43596'], matching primary gene and S288C taxon; all alias/locus fields inspected. This does not reconstruct the dated historical query execution. |
| micro-query-IOC4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full exact reviewed gene/taxon result page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-IOC4.raw | supports | One current reviewed result ['Q04213'], matching primary gene and S288C taxon; all alias/locus fields inspected. This does not reconstruct the dated historical query execution. |
| micro-query-ISW1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full exact reviewed gene/taxon result page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-ISW1.raw | supports | One current reviewed result ['P38144'], matching primary gene and S288C taxon; all alias/locus fields inspected. This does not reconstruct the dated historical query execution. |
| micro-query-YKU70 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU70%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full exact reviewed gene/taxon result page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-YKU70.raw | supports | One current reviewed result ['P32807'], matching primary gene and S288C taxon; all alias/locus fields inspected. This does not reconstruct the dated historical query execution. |
| micro-query-YKU80 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full exact reviewed gene/taxon result page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-YKU80.raw | supports | One current reviewed result ['Q04437'], matching primary gene and S288C taxon; all alias/locus fields inspected. This does not reconstruct the dated historical query execution. |
| micro-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; Exact native name, active state, rank, parent and reference-strain lineage; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/tax-4932.raw | supports | Taxon 4932: Saccharomyces cerevisiae, active True, rank species. S. cerevisiae species and S288C protein-reference strain are not interchangeable experimental claims. |
| micro-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; Exact native name, active state, rank, parent and reference-strain lineage; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/tax-559292.raw | supports | Taxon 559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c), active True, rank strain. S. cerevisiae species and S288C protein-reference strain are not interchangeable experimental claims. |
| micro-go-0006303 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006303; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0006303.raw | supports | GO:0006303: double-strand break repair via nonhomologous end joining; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0006338 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006338; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0006338.raw | supports | GO:0006338: chromatin remodeling; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0016587 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0016587; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0016587.raw | supports | GO:0016587: Isw1 complex; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0031010 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0031010; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0031010.raw | supports | GO:0031010: ISWI-type complex; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0036436 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036436; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0036436.raw | supports | GO:0036436: Isw1a complex; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0036437 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036437; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0036437.raw | supports | GO:0036437: Isw1b complex; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0043564 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043564; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0043564.raw | supports | GO:0043564: Ku70:Ku80 complex; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0045027 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0045027; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0045027.raw | supports | GO:0045027: DNA end binding; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-go-0140513 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0140513; Exact active term, full definition/synonyms and typed relationships; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0140513.raw | supports | GO:0140513: nuclear protein-containing complex; isObsolete=False. Definition and structure/function scope inspected; authority text is not a new experimental assay. |
| micro-ancestors-0016587 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0016587/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0016587.raw | supports | GO:0016587 ancestors ['GO:1902494', 'GO:1904949', 'GO:0140513', 'GO:0031010', 'GO:0032991', 'GO:0070603', 'GO:0016587', 'GO:0005575']; declared parent corroborated, distinct from parthood or prevalence. |
| micro-ancestors-0036436 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036436/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0036436.raw | supports | GO:0036436 ancestors ['GO:1902494', 'GO:1904949', 'GO:0140513', 'GO:0031010', 'GO:0032991', 'GO:0070603', 'GO:0016587', 'GO:0005575', 'GO:0036436']; declared parent corroborated, distinct from parthood or prevalence. |
| micro-ancestors-0036437 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036437/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0036437.raw | supports | GO:0036437 ancestors ['GO:1902494', 'GO:1904949', 'GO:0140513', 'GO:0031010', 'GO:0032991', 'GO:0070603', 'GO:0016587', 'GO:0005575', 'GO:0036437']; declared parent corroborated, distinct from parthood or prevalence. |
| micro-ancestors-0043564 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043564/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0043564.raw | supports | GO:0043564 ancestors ['GO:0140513', 'GO:0032991', 'GO:0043564', 'GO:0005575']; declared parent corroborated, distinct from parthood or prevalence. |
| micro-family-IPR006165 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006165/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR006165.raw | supports | IPR006165: Ku70; type family. Exact Ku70 whole-protein family, positively linked from reviewed yeast P32807; PIRSF003033/TIGR00578 signatures. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR024193 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024193/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR024193.raw | supports | IPR024193: Ku80; type family. Exact Ku80 family, positively linked from reviewed yeast Q04437; PIRSF016570/cd00873 signatures. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR006164 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006164/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR006164.raw | supports | IPR006164: Ku70/Ku80, DNA-binding domain; type domain. Shared Ku70/Ku80 DNA-binding domain; not a whole-subunit class substitute. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR044754 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR044754.raw | supports | IPR044754: Isw1/2, N-terminal; type domain. Isw1/Isw2 N-terminal domain, spanning both ATPase paralogs; not exact whole Isw1. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR038718 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038718/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR038718.raw | supports | IPR038718: SNF2-like, N-terminal domain superfamily; type homologous_superfamily. Broad SNF2-like N-terminal domain superfamily, not exact whole Isw1. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR035503 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035503/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR035503.raw | supports | IPR035503: IOC4-like, PWWP domain; type domain. IOC4-like PWWP domain, not whole Ioc4. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR062587 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062587/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR062587.raw | supports | IPR062587: IOC2, middle domain; type domain. IOC2 middle domain, not whole Ioc2. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR028942-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028942/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR028942-retry.raw | supports | IPR028942: WHIM1 domain; type domain. WHIM1 domain, not whole Ioc3. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR062429-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062429/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR062429-retry.raw | supports | IPR062429: ISWI one complex protein 2, N-terminal domain; type domain. IOC2 N-terminal domain, not whole Ioc2. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-family-IPR063422-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063422/; Complete native name/type, description with quality flags, integrated signatures and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR063422-retry.raw | supports | IPR063422: IOC2, C-terminal domain; type domain. IOC2 C-terminal domain, not whole Ioc2. These exact candidate entries do not constitute an exhaustive family absence search or independent sequence alignment. |
| micro-pmid-12482963 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12482963+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-12482963.raw | context_only | Yeast Isw1p forms two separable complexes in vivo.; Vary JC, Gangaraju VK, Qin J, Landel CC, Kooperberg C, Bartholomew B, Tsukiyama T.; PMID12482963, DOI10.1128/mcb.23.1.80-91.2003. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-12518983 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12518983+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-12518983.raw | context_only | Dimerization, translocation and localization of Ku70 and Ku80 proteins.; Koike M.; PMID12518983, DOI10.1269/jrr.43.223. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-14562095.raw | context_only | Global analysis of protein localization in budding yeast.; Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; PMID14562095, DOI10.1038/nature02026. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-15122350 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15122350+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-15122350.raw | context_only | A means to a DNA end: the many roles of Ku.; Downs JA, Jackson SP.; PMID15122350, DOI10.1038/nrm1367. No abstractText in exact returned result; bibliographic metadata only. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-8890183 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8890183+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-8890183.raw | context_only | Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand break repair and serves as a barrier to error-prone DNA repair pathways.; Boulton SJ, Jackson SP.; PMID8890183, DOI10.1002/j.1460-2075.1996.tb00890.x. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-8910371 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910371+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-8910371.raw | context_only | HDF2, the second subunit of the Ku homologue from Saccharomyces cerevisiae.; Feldmann H, Driller L, Meier B, Mages G, Kellermann J, Winnacker EL.; PMID8910371, DOI10.1074/jbc.271.44.27765. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-8972848 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8972848+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-8972848.raw | context_only | Identification of a Saccharomyces cerevisiae Ku80 homologue: roles in DNA double strand break rejoining and in telomeric maintenance.; Boulton SJ, Jackson SP.; PMID8972848, DOI10.1093/nar/24.23.4639. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-pmid-9635192 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9635192+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Unique exact MED PMID metadata, authors/year/DOI/article type and full abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-9635192.raw | context_only | Mutation of yeast Ku genes disrupts the subnuclear organization of telomeres.; Laroche T, Martin SG, Gotta M, Gorham HC, Pryde FE, Louis EJ, Gasser SM.; PMID9635192, DOI10.1016/s0960-9822(98)70252-0. Complete indexed abstract read. Primary versus review publication type checked; no unlisted body access inferred. |
| micro-vary2003-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/; Genuine PMC HTML; complete Methods sec2–11 including strain Table1, Results sec13–20, Discussion sec21 and all embedded Figures1–5 text captions; not Introduction, Table2 appendix, pixels or external/raw data; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/vary2003-html.raw | supports | Vary and colleagues directly separate Isw1-Ioc3 and Isw1-Ioc2-Ioc4 assemblies by reciprocal immunoprecipitation and tagged purification. Ioc2/Ioc4 are mutually required for stable recovery under tested conditions. Both complexes show nucleosome-stimulated ATPase activity; spacing/sliding/binding and genetic-expression results depend on assay/substrate. Unstable interactions/other conditions remain possible. W303 derivatives had RAD5 repaired; S288C references are not the experimental strain. |
| micro-koike2002-pdf | https://www.jstage.jst.go.jp/article/jrr/43/3/43_3_223/_pdf; Fresh genuine secondary-review PDF; printed pp223–227 and dimerization conclusion at the start of p228: complete Abstract/Introduction, chromosome-location and dimerization sections, Table1 and Figure1 caption; remaining p228 localization excerpt not used, no pixels or later pages; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/koike2002-pdf.raw | supports | Koike 2002 distinguishes the Ku heterodimer and DNA-PKcs, two-subunit DNA channel, mammalian heterodimer-stability observations and organism-specific NHEJ. The review explicitly notes no obvious yeast DNA-PKcs homolog; mammalian V(D)J/DNA-PK functions do not become yeast claims. Secondary synthesis is not fresh primary assay evidence. |
| micro-boulton70-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC452249/; Genuine PMC abstract and article metadata only; full-text route is a scanned/PDF landing, not a readable main body; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/boulton70-html.raw | supports | Complete primary abstract supports the bounded yeast repair/telomere observations stated there. Main methods, strain construction, figures and experimental detail were not read; genuine landing-page access does not certify full-body access. |
| micro-boulton80-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC146307/; Genuine PMC abstract and article metadata only; full-text route is a scanned/PDF landing, not a readable main body; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/boulton80-html.raw | supports | Complete primary abstract supports the bounded yeast repair/telomere observations stated there. Main methods, strain construction, figures and experimental detail were not read; genuine landing-page access does not certify full-body access. |
| micro-downs2004-doi | https://doi.org/10.1038/nrm1367; DOI content-negotiated Crossref JSON metadata, title/authors/DOI and publisher pointers only; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/downs2004-doi.raw | context_only | DOI resolves to Downs and Jackson 2004 secondary review metadata, not its body. The exact MED record has no abstract; no review-body scientific support is claimed from this route. |
| micro-access-vary2003-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC140669.1/PMC140669.1.xml; Actual HTTP status/content-type and retained diagnostic body | context_only | HTTP 404; failed route or rate-limit response only, not article/family evidence. Later successful access remains separately timestamped. |
| micro-access-boulton80-pdf | https://academic.oup.com/nar/article-pdf/24/23/4639/3997483/24-23-4639.pdf; Actual HTTP status/content-type and retained diagnostic body | context_only | HTTP 403; failed route or rate-limit response only, not article/family evidence. Later successful access remains separately timestamped. |
| micro-access-feldmann1996-pdf | https://www.jbc.org/article/S0021925818352992/pdf; Actual HTTP status/content-type and retained diagnostic body | context_only | HTTP 403; failed route or rate-limit response only, not article/family evidence. Later successful access remains separately timestamped. |
| micro-access-family-IPR028942 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028942/; Actual HTTP status/content-type and retained diagnostic body | context_only | HTTP 429; failed route or rate-limit response only, not article/family evidence. Later successful access remains separately timestamped. |
| micro-access-family-IPR062429 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062429/; Actual HTTP status/content-type and retained diagnostic body | context_only | HTTP 429; failed route or rate-limit response only, not article/family evidence. Later successful access remains separately timestamped. |
| micro-access-family-IPR063422 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063422/; Actual HTTP status/content-type and retained diagnostic body | context_only | HTTP 429; failed route or rate-limit response only, not article/family evidence. Later successful access remains separately timestamped. |
| micro-historical-0-access-PMC140669-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/; Immutable original evidence access-PMC140669-html in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 was a browser challenge, not article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-0-access-PMC140669-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Immutable original evidence access-PMC140669-xml in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | The first request failed at local DNS before retrieval; no article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-0-access-PMC140669-xml-network | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Immutable original evidence access-PMC140669-xml-network in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | The network XML route returned HTTP500 and an error body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-0-access-PMC140669-europepmc | https://europepmc.org/articles/PMC140669; Immutable original evidence access-PMC140669-europepmc in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 provided a JavaScript page shell rather than the article body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-0-access-vary2003-doi | https://doi.org/10.1128/MCB.23.1.80-91.2003; Immutable original evidence access-vary2003-doi in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | The publisher DOI route returned HTTP403. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-0-access-PMC140669-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode; Immutable original evidence access-PMC140669-bioc in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 contained an explicit no-result response rather than article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-0-access-panther-PTHR45623-SF49 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/; Immutable original evidence access-panther-PTHR45623-SF49 in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml; diagnostic access scope only | context_only | The protein-linked candidate subfamily route returned HTTP204 and no body; it did not establish an exact Isw1-only family. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-PMC140669-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/; Immutable original evidence access-PMC140669-html in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 was a browser challenge, not article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-PMC140669-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Immutable original evidence access-PMC140669-xml in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | The first request failed at local DNS before retrieval; no article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-PMC140669-xml-network | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Immutable original evidence access-PMC140669-xml-network in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | The network XML route returned HTTP500 and an error body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-PMC140669-europepmc | https://europepmc.org/articles/PMC140669; Immutable original evidence access-PMC140669-europepmc in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 provided a JavaScript page shell rather than the article body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-vary2003-doi | https://doi.org/10.1128/MCB.23.1.80-91.2003; Immutable original evidence access-vary2003-doi in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | The publisher DOI route returned HTTP403. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-PMC140669-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode; Immutable original evidence access-PMC140669-bioc in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 contained an explicit no-result response rather than article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-1-access-panther-PTHR45623-SF49 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/; Immutable original evidence access-panther-PTHR45623-SF49 in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml; diagnostic access scope only | context_only | The protein-linked candidate subfamily route returned HTTP204 and no body; it did not establish an exact Isw1-only family. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-PMC140669-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/; Immutable original evidence access-PMC140669-html in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 was a browser challenge, not article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-PMC140669-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Immutable original evidence access-PMC140669-xml in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | The first request failed at local DNS before retrieval; no article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-PMC140669-xml-network | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML; Immutable original evidence access-PMC140669-xml-network in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | The network XML route returned HTTP500 and an error body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-PMC140669-europepmc | https://europepmc.org/articles/PMC140669; Immutable original evidence access-PMC140669-europepmc in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 provided a JavaScript page shell rather than the article body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-vary2003-doi | https://doi.org/10.1128/MCB.23.1.80-91.2003; Immutable original evidence access-vary2003-doi in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | The publisher DOI route returned HTTP403. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-PMC140669-bioc | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode; Immutable original evidence access-PMC140669-bioc in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | HTTP200 contained an explicit no-result response rather than article text. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-2-access-panther-PTHR45623-SF49 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/; Immutable original evidence access-panther-PTHR45623-SF49 in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml; diagnostic access scope only | context_only | The protein-linked candidate subfamily route returned HTTP204 and no body; it did not establish an exact Isw1-only family. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-3-micro58-PMC146307-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC146307/; Immutable original evidence micro58-PMC146307-legacy in reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml; diagnostic access scope only | context_only | The retained HTTP200 legacy response is a browser-check challenge, not the Boulton Ku80 main body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-historical-3-micro58-feldmann1996-publisher-html | https://www.sciencedirect.com/science/article/pii/S0021925818352992; Immutable original evidence micro58-feldmann1996-publisher-html in reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml; diagnostic access scope only | context_only | The ScienceDirect route returned403 and an error page, not the Feldmann main body. Original access timestamp/hash and honest limitations retained; kind corrected to validation/context_only in this successor evidence. No fresh invocation or retroactive body upgrade. |
| micro-adapter-catalogue | https://imodulondb.org/api/organisms; Complete official organism/dataset catalogue, all organism names and dataset pairs; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-catalogue.raw | context_only | All 20 organism rows and 28 organism/dataset pairs inspected. No Saccharomyces host is present in this exact current response. No matched dataset exists for these four yeast-scoped records; no foreign-host gene/module proxy or expression-to-assembly inference is used. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner attempt 2026-11-03T00:49:00.848907–00:49:00.863225Z | context_only | Historical PermissionError pyvenv.cfg retained; no fresh runner invocation. The current official catalogue fallback has its own actual fetch timestamp. |
| micro-native-isw1_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1_complex.yaml --verify; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-verify-receipt.json SHA256 090e422f1915f7aa1701113ac30d4e0a9a86fc65acd3a4bbb40ca03770a9d158 | supports | 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-isw1_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1_complex.yaml --causal-graphs; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-causal-receipt.json SHA256 1e96f1270cf6736c2b11449cc86a454a5da8649e95c4bdf0f994fa8a6d96f071 | supports | 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-isw1a_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1a_complex.yaml --verify; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-verify-receipt.json SHA256 48d5c2b3bb4d835e89c61f1e43c2e0f0d928880c2f3935e5c190a567ab163d3a | supports | 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-isw1a_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1a_complex.yaml --causal-graphs; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-causal-receipt.json SHA256 f8d8b49e7bbab7fd05ec1b9c241289fa03481b44e07193c6137a215327132d81 | supports | 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-isw1b_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml --verify; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-verify-receipt.json SHA256 2e2b643db38b2260389b58403aff5c1be583d18b1bb19a17985674d1b579efac | supports | 3 maintained reviewed S288C examples and 3 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-isw1b_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml --causal-graphs; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-causal-receipt.json SHA256 af9e274c4664fb41a7304a5cc3fdc5033fff0c5c1d0392414b2d414ea7031016 | supports | 3 maintained reviewed S288C examples and 3 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-ku70_ku80_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml --verify; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-verify-receipt.json SHA256 aeada98cb98d38f397b5161e7291ccd33a11abaa4ec7f6eb7374bcea59af1cd3 | supports | 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-native-ku70_ku80_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml --causal-graphs; Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-causal-receipt.json SHA256 1a29d8b6760874bb054c344bf59399dcc9b96b16de0c25472a2d9939fc362844 | supports | 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes. Complete actual log inspected; identity/coverage is not biological membership or mechanism proof. |
| micro-isw1-peer-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/isw1-class-scope-challenge.json; Independent bounded current class/variant challenge with exact frozen inputs and Vary read scope | context_only | Corroborates a minor internal scope mismatch while rejecting nonhomology, generic class or optional example absence as sufficient major-defect grounds. No mandatory row split, component type change or extra examples. |
| plaque-native-policy | docs/CURATION.md; docs/record-review-profile.md; .claude/skills/review-yaml-record/SKILL.md; Frozen whole-record source applicability, class grounding, formation versus function, append-only historical rationale and native review contract; exact used inputs separately manifested. | context_only | Applied native rules without imposing optional inventory or universal depletion experiments. Gene/pathway assertions trigger structured-source assessment regardless of expression-inference wording. |
| plaque-native-schema | schema/record_review.yaml; src/cellstructuremech/schema/cellstructuremech.yaml; Frozen native evidence/assessment/finding enums and graph/record contract. | context_only | GENE_OR_PROTEIN may represent a protein family/class or complex; source-aware NONMECHANISTIC graphs and UNKNOWN formation status are permitted. |
| plaque-original-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/original-proof.json; Actual independent native validate/render of all three originals; historical source hashes checked at their declared original revision; YAML/Markdown SHA256 and byte equality. SHA256 ec87bce8c2a1da2757dc6510d1a633f84e7f28344f42f24efaaa8488ae7b01d4 | supports | All three immutable originals validate and render exactly, and all their historical source-input hashes match. LPS and MacAB current target bytes match the originals; LolCDE stale delta is separately assessed. |
| plaque-t5-record | data/structures/other/lipopolysaccharide_transport_system.yaml; Complete current record including definition, components/examples, distribution, properties, functions, graph, canonical examples, discussions and history; SHA256 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e | context_only | Whole assigned index 5 independently read at exact source f9ac707415c382929b15517997efaa11ec96230d. |
| plaque-t5-original | reviews/structured/20261022T080130Z-lipopolysaccharide-transport-system-audit/review.yaml; Complete original YAML and canonically identical Markdown; exact original proof above. | context_only | Original review 20261022T080130Z-lipopolysaccharide-transport-system-audit; original findings independently reassessed, with historical source and access assertions kept historical. |
| plaque-native-lipopolysaccharide_transport_system-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-verify-receipt.json; Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lipopolysaccharide_transport_system.yaml', '--verify']; receipt SHA256 d8dd31312e9a9d8c1ce5cf08e3f96dbe9a92e1e7eee2fa03a85939f12b7d13ee; actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently inventoried 7 reviewed examples; 7 typed nodes COVERED. Verification covers identity/xrefs, not scientific participation, family exactness or universal assembly necessity. |
| plaque-native-lipopolysaccharide_transport_system-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-causal-receipt.json; Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lipopolysaccharide_transport_system.yaml', '--causal-graphs']; receipt SHA256 68e17a0aca56ab7ba11f455e314749b5a61e63ce43520e1f9f2526ae5c36b6ca; actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-causal.log SHA256 22dc6e5a43f3ee651b4ba14ac6c41138867d16abc99858e2a217188e2a4a2c83 | supports | Exit0 at source head. Independently inventoried 7 reviewed examples; 7 typed nodes COVERED. Verification covers identity/xrefs, not scientific participation, family exactness or universal assembly necessity. |
| plaque-t6-record | data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml; Complete current record including definition, components/examples, distribution, properties, functions, graph, canonical examples, discussions and history; SHA256 96bf1ce75ce606af29c2d8a549c345e9487f0e426ac1f86823f14db22c651866 | context_only | Whole assigned index 6 independently read at exact source f9ac707415c382929b15517997efaa11ec96230d. |
| plaque-t6-original | reviews/structured/20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit/review.yaml; Complete original YAML and canonically identical Markdown; exact original proof above. | context_only | Original review 20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit; original findings independently reassessed, with historical source and access assertions kept historical. |
| plaque-native-lolcde_lipoprotein_abc_transporter_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-verify-receipt.json; Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml', '--verify']; receipt SHA256 bf3e150b5ad894bc9f1fab13d0abaebd5d5dc5e4b581405c5666645c3f6270ec; actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently inventoried 3 reviewed examples; 3 COVERED typed constituents plus 1 substrate UNANCHORED_WITH_UNIPROT carrying Lpp/Pal. Verification covers identity/xrefs, not scientific participation, family exactness or universal assembly necessity. |
| plaque-native-lolcde_lipoprotein_abc_transporter_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-causal-receipt.json; Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml', '--causal-graphs']; receipt SHA256 5501faf803afe3f763eb166c3754e496912e4e4734426f67782d58ab04c5a323; actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-causal.log SHA256 ec1f04f331b7a6dece930cf0d7b4799eb610cbbca2f0af475f09083aa4c4a241 | supports | Exit0 at source head. Independently inventoried 3 reviewed examples; 3 COVERED typed constituents plus 1 substrate UNANCHORED_WITH_UNIPROT carrying Lpp/Pal. Verification covers identity/xrefs, not scientific participation, family exactness or universal assembly necessity. |
| plaque-t9-record | data/structures/other/macab_tolc_complex.yaml; Complete current record including definition, components/examples, distribution, properties, functions, graph, canonical examples, discussions and history; SHA256 b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636 | context_only | Whole assigned index 9 independently read at exact source f9ac707415c382929b15517997efaa11ec96230d. |
| plaque-t9-original | reviews/structured/20261022T080133Z-macab-tolc-complex-audit/review.yaml; Complete original YAML and canonically identical Markdown; exact original proof above. | context_only | Original review 20261022T080133Z-macab-tolc-complex-audit; original findings independently reassessed, with historical source and access assertions kept historical. |
| plaque-native-macab_tolc_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-verify-receipt.json; Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/macab_tolc_complex.yaml', '--verify']; receipt SHA256 aedfa789d115b849c5373dd04a79b2955c9952c28c560f6917421961c53a53a6; actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0 at source head. Independently inventoried 3 reviewed examples; 3 typed nodes COVERED. Verification covers identity/xrefs, not scientific participation, family exactness or universal assembly necessity. |
| plaque-native-macab_tolc_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-causal-receipt.json; Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/macab_tolc_complex.yaml', '--causal-graphs']; receipt SHA256 6916caf9407ca7f05c2309ce1354ef05594e54e375db4583d1e8a52cceb5b564; actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-causal.log SHA256 404a309417e082e13a78e994b12da77302a38ee7f6546a78f8f98b0a9743e762 | supports | Exit0 at source head. Independently inventoried 3 reviewed examples; 3 typed nodes COVERED. Verification covers identity/xrefs, not scientific participation, family exactness or universal assembly necessity. |
| plaque-PMC2851745-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2851745/; Genuine primary body sections2,3,4,7,10: LptD/E purification and biochemical characterization, conditional plug/barrel alternatives in Discussion; source does not present the later demonstrated architecture. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-legacy.raw SHA256 53a39228d92aff6d6d776343950fa2b80ced9fcc0aafbfe22fa607503ea4deb8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-legacy.receipt.json SHA256 5412a9060ee677015ca48fb7b5a2e6cf4367cedcd6e400f8aca469be361fa338 | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-PMC3038725-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3038725/; Genuine primary body sections2,4,5,Discussion SEC2 and section10: LptE-LptD contact mapping/photocrosslinking and mutant analysis; supports later buried plug model, not an atomic structure. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-legacy.raw SHA256 4bf892fc7b163ae5662df02d3e18ea32eee2515cfdf4f7e2ed4de14eb5887895; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-legacy.receipt.json SHA256 c75a613cf33e050e121a4f55d225a1fe2fca3b02ce02f8afc7f36a68984154cb | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-yakushi2000-pdf | https://www.nature.com/articles/35008635.pdf; Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-pdf.raw SHA256 8ed2bbedd7f13cb850b9ec216fc9bd2ad87e8059170b70d2454bdf5a5ff12121; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-pdf.receipt.json SHA256 af5aa27c907d2f87e16c44b93c209eae92be65b36466ac80f519f9569b8662c9 | context_only | Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather than PDF. Successful alternative routes are independently tiered. |
| plaque-yakushi2000-publisher | https://www.nature.com/articles/35008635; Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-publisher.raw SHA256 8ed2bbedd7f13cb850b9ec216fc9bd2ad87e8059170b70d2454bdf5a5ff12121; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-publisher.receipt.json SHA256 e0e72df4ad10821e89e9ff536c7fccf76f873f098f7aced6d506e6eeaafd214f | context_only | Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather than PDF. Successful alternative routes are independently tiered. |
| plaque-query-lptA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptA.raw SHA256 e97a531c6792ce399e4ff13718c26ef6b8492357f54d130230c72afcb8fb0b19; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptA.receipt.json SHA256 4e8f709af44eb71540969978e98f784adcf951185146cff98c76d1cb81aceb13 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lptB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptB.raw SHA256 50c80c40179588c0cbda5e9914674e3561dd3f52fd1de12dec341b827da48bcc; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptB.receipt.json SHA256 978f950d1657751b9aba636336256262fb1c4211381c32b7144f965287bcb003 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lptC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptC.raw SHA256 9275ea8f055bff383cda815a15b30587451b4228aa8a12dcbb6441316600d41c; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptC.receipt.json SHA256 6794dddeb11983b0d2314309f8bc77c7165efb6b8334870fdba1915c359d693f | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lptD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptD.raw SHA256 1cefffb7d372496094e05d2fcba958a834d1b35316006f0c3e13d60d143c15e5; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptD.receipt.json SHA256 36dca3ba88de8b15661390c0bd951c8e331290e33757dd7816e5d92d0ef59ec7 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lptE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptE.raw SHA256 c335b8cad051a875c24d87fa500eab861f2656e511ac7164d0a6664830daeef4; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptE.receipt.json SHA256 c05068f6f4bf194e3dec6113930fad1f10d869bcf645a0d19cbdafdc780321de | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lptF | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptF%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptF.raw SHA256 d5933058a3cccc7ee4679d7043e63990578d827ba058fe21f9f8d01b3de57f23; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptF.receipt.json SHA256 cb413910d13cee29f97cc97db272eeb076ca7bcd5e4690662466eb5d76a801b6 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lptG | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptG.raw SHA256 664f7d12805970dcb311daba5feb97624ef8d394464edc55edfc90b0f4f6f177; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptG.receipt.json SHA256 a27d4a0e78753881e34ebb6ee5ee1ea42a326c568a66ad8b70017db9d95882df | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lolC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolC.raw SHA256 24e5e117fdd695734205da1b44dfbece3dfb1c69250abab110a2b53502aa67ad; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolC.receipt.json SHA256 71218d8fc34369f969499f42d7e538c5075f5cf3bf8ad9cd8ad883016cbba27a | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lolD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlolD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolD.raw SHA256 6301389cebcd2127dda9ededfdb40589c9f7ea17c64bc3d413420d858ca726f2; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolD.receipt.json SHA256 f667a9eccbd1672b2f15242d88a189229fca37085580cecc9bcee6f748e24346 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lolE | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlolE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolE.raw SHA256 7116f3a87e7c09a2364fe937867b284c48682d6c1262adaec07f9c8c14df4ae2; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolE.receipt.json SHA256 ef5bb049a835c0b06249bb81d5504b4b0687b10a7cb83739d0e8b908519f1dae | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-lpp | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Alpp%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lpp.raw SHA256 7b371f7303c4e13f128bbc6283474ddfbd5ad36128fccf593aad138328796920; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lpp.receipt.json SHA256 032e3279ff4256b7565d2b6c5b2283f0e14e4f2ce7b7bbb8ccadff6c033962cf | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-pal | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Apal%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-pal.raw SHA256 4a942cc3f3a596e061c83696017ce27acbe5fd0a32c90e69a5988ab4a8a72ec1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-pal.receipt.json SHA256 5ec22da045ba3137940ce0a0a21c5ab897197277122c924f585d4bc5db7c351b | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-macA | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmacA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macA.raw SHA256 27c0caf5770fe21cab614b751a0d12c0e15448ed3ce1ab11bfe27f8415b4aa90; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macA.receipt.json SHA256 ca1a931f4da10e6286aa936fd19a61ceb8cf8af35d68c36d200982a9935f3a71 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-macB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmacB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macB.raw SHA256 b499c3c03b744afbc926cfa35dd5af14d32141a991b2631a270aeb4e941f7259; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macB.receipt.json SHA256 b36277796d44eb8f5a76ba5d2e0c84598f41c56cbe372118b2a0066000dd91b2 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-query-tolC | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Full returned current UniProt reviewed exact-gene taxon83333 query, size500, one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-tolC.raw SHA256 3e284eede466d8aa6d6eac091b434ce033083e18848c220476a3bdb06463365a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-tolC.receipt.json SHA256 90041b167ae727a647725a57456702a0b4c45a44e6e2632e8e3f502f65371537 | partial | Exact native K-12 accession selection corroborates the record reference, without proving complex participation. |
| plaque-adapter-module-22 | https://imodulondb.org/api/imodulons/e_coli/precise1k/22; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22.raw SHA256 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22.receipt.json SHA256 5627aef36d82d0c9fb57cfbeafe2a2e0dc2ca53bd6472ef198a52be9b399a961 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-module-22-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22-genes.raw SHA256 6e779e25e705f68403277aa34683af16a8dddfd4dc5fbe96fb6bdfc7117e20f0; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22-genes.receipt.json SHA256 7adacf5ec076e6a64fcfd443db3494aa542071535554c94ad9d41b456badfabc | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-module-45 | https://imodulondb.org/api/imodulons/e_coli/precise1k/45; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45.raw SHA256 12f2886fe517f3015a3855554588553d6f3bf4e12a11cc4877ecadb00133064b; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45.receipt.json SHA256 3b5b14ecee432f8eaadf907e41d9a801aa199567f1293fd8dea8a7beeb34e685 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-module-45-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/45/genes; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45-genes.raw SHA256 d32d1ee58b1768cada05d6a326fb8012e5a7a8d5e4ae5f3e9cd373375046a920; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45-genes.receipt.json SHA256 85312eb725b480d1c9ea4fda02364e9345f846b5c5345a406022e150d3e867f8 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-module-167 | https://imodulondb.org/api/imodulons/e_coli/precise1k/167; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167.raw SHA256 49c7e478867c20e407e8929c8a92872f8eeb679c4a835f5344b90ba5bad34292; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167.receipt.json SHA256 553da6411cc1fdb119be9f92d835d29b7e7b7ef789fd804cec2bf35a5a5cd5d1 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-module-167-genes | https://imodulondb.org/api/imodulons/e_coli/precise1k/167/genes; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167-genes.raw SHA256 cd9b96081fad9fd906870f03c736d6a152bb04c3927ad7c4c910a5b5884c69fb; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167-genes.receipt.json SHA256 05f99ced53e58fce50b9bc6751c378e2c91450afc1e46419c4062af24c6752f8 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-yakushi2000-canonical-pdf | https://www.nature.com/articles/ncb0400_212.pdf; Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical-pdf.raw SHA256 fe5a7dc76ae9624ea65eb8f73983d456b2f31ec535aebdfb0500b4b6803eddaa; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical-pdf.receipt.json SHA256 08dabf55516660dbc1ba83714312145e412a258f73fbea6a5595f389d774341e | context_only | Failed or non-body route: HTTP 200; canonical PDF route returns HTML rather than PDF. Successful alternative routes are independently tiered. |
| plaque-yakushi2000-canonical | https://www.nature.com/articles/ncb0400_212; Publisher title/authors/DOI and displayed abstract/figure navigation only; body paywalled. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical.raw SHA256 afab2528b5e4dce9ddba497f7d3d1b586aee55a62f97517953cc81dbba99d84d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical.receipt.json SHA256 bf72a3fa007450e3bfd420fca29897f060f7e3dd133cf820df3d47f0b3a27678 | context_only | Correct canonical article route; abstract is separately captured by PMID10783239. No full-body inspection claimed. |
| plaque-go-0062051-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0062051/ancestors?relations=is_a; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051-ancestors.raw SHA256 d1a97376dc80e450241fd90f2c148c4b6f9ba36e4fce3d1b452dd9cae3d92e52; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051-ancestors.receipt.json SHA256 159808725427186c59600b1a8a920fceb067b1c3bde17339895ffa8244fe576b | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-1990196-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990196/ancestors?relations=is_a; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196-ancestors.raw SHA256 8120216524da941cc23167cd8a5283877080de1a2b8bf55aefb4402972dd977b; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196-ancestors.receipt.json SHA256 f06079e516998f3abe93d623292508af4ae8572ab3e0148b932b4688ebe0a875 | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-protein-P0ADV1 | https://rest.uniprot.org/uniprotkb/P0ADV1.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV1.raw SHA256 a49f57f247687a374446fcfe0d6b33e53ea8060af935201b1d8e588c245901e7; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV1.receipt.json SHA256 735cca2df2ca115818516622615c8978cb9d111e34eee9447b46ea1272c12b54 | partial | P0ADV1; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0A9V1 | https://rest.uniprot.org/uniprotkb/P0A9V1.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A9V1.raw SHA256 a539dccc2f9371777cda184328fdbdf0ea913901bb0a4f8be9973ccb28e38a07; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A9V1.receipt.json SHA256 350d59ce0dce916c67063d79eef5a65be854960f39121eb90731f0c774f070aa | partial | P0A9V1; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0ADV9 | https://rest.uniprot.org/uniprotkb/P0ADV9.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV9.raw SHA256 53d4861aae4b0c63f0442dabafde093c6df6d2ed831df1b48bff73b6717d2e4f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV9.receipt.json SHA256 3ee2a8d4569fd9e17b0036d8f8b19d9f9468397e8367704bb2f01598cbd437fa | partial | P0ADV9; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P31554 | https://rest.uniprot.org/uniprotkb/P31554.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P31554.raw SHA256 dbab992a253dc68cd2b7543da5236b46111557f1f37b9fdd619b4b81794bf178; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P31554.receipt.json SHA256 381b55600d11346282e2f6b6b6a327594e78bd8e781dedb1d34603ae31fc1fd7 | partial | P31554; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0ADC1 | https://rest.uniprot.org/uniprotkb/P0ADC1.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC1.raw SHA256 70872174ddd7695d30b349af2863fe0f5d9c5f83f387200cbf6f8da40d459a90; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC1.receipt.json SHA256 54971d0fee5d1123acba92b87bf3e99587f260f9c47962eb86c26911d50c84d8 | partial | P0ADC1; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0AF98 | https://rest.uniprot.org/uniprotkb/P0AF98.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0AF98.raw SHA256 a4fd62e77373d82751c493c32e954a4a935cecb2c8d43d2a357743077dd5c3c4; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0AF98.receipt.json SHA256 54342bdd6ca1f3d74066c457a491fdae0a738c34c55c47d11bb838b10f7ed096 | partial | P0AF98; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0ADC6 | https://rest.uniprot.org/uniprotkb/P0ADC6.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC6.raw SHA256 20aa3222eec43cbb1782775b815c3b69549e897e0cfcc81d7556732e6cb2f5bc; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC6.receipt.json SHA256 1190b248eaa9e9253d66aafc8d48386e27d0de2e7b84bfb614dabf3388660b92 | partial | P0ADC6; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0ADC3 | https://rest.uniprot.org/uniprotkb/P0ADC3.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC3.raw SHA256 a9b53bf112c3ddac173aa28de70bab78e43ff7104a2b4e33f32ffcc337527470; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC3.receipt.json SHA256 d5227f3103d78ed248cf41d5fdd7d7d2ba5f33d081726d1b869a6528334c48eb | partial | P0ADC3; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P75957 | https://rest.uniprot.org/uniprotkb/P75957.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75957.raw SHA256 4a90a4d028ffd3b16115b94edd516cb4b88e9a9ba1e1d667e5cb3851fb333e4d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75957.receipt.json SHA256 c11e571ef1040ee01e4d328234c1fa72aa5bd70b227253c51de4bbd823fa3300 | partial | P75957; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P75958 | https://rest.uniprot.org/uniprotkb/P75958.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75958.raw SHA256 d90ee551682661d6bd97c04e3a399814bacec9688257988b268467314b152459; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75958.receipt.json SHA256 26913d6564d2410e01f75e6204ba96a98748d1a7910698cd4b96d4cec2a84f93 | partial | P75958; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P69776 | https://rest.uniprot.org/uniprotkb/P69776.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P69776.raw SHA256 ad352c7a4cde4709f826a28fe7021076ca97a53582236f32ec60d3dd4846e6bd; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P69776.receipt.json SHA256 72557ad3d133bee226f2e6513505dce6b0f06f7069a82d3ea19b950f2cbe28ba | partial | P69776; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P0A912 | https://rest.uniprot.org/uniprotkb/P0A912.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A912.raw SHA256 93a07fedc75dfc2a7729de1128fd5d4eb22bfb376d5251a6419446c2cffc42fa; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A912.receipt.json SHA256 034efcfcd0a08ccb74542350f8753521fd3fb1a2b9dea20b24c8031db9eb9091 | partial | P0A912; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P75830 | https://rest.uniprot.org/uniprotkb/P75830.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75830.raw SHA256 0465a58120398458818561f76d7fc68cdaa56d02690ab95f7ca5f730656067a4; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75830.receipt.json SHA256 d4486d0efe6282eb2f297a2fdc694ee3a2bdf08f1f6d46d227fe871a030d50bf | partial | P75830; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P75831 | https://rest.uniprot.org/uniprotkb/P75831.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75831.raw SHA256 544d28caf979f42b50802e05fe332a5350cb8ba79df24df0002874c3ef36ce42; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75831.receipt.json SHA256 443bea708a97d7d0f04e5a623351160d8f90156186d417dcb36cdbf290402bb5 | partial | P75831; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-protein-P02930 | https://rest.uniprot.org/uniprotkb/P02930.json; Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization comments and exact family cross-references read; bibliographic annotations are not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P02930.raw SHA256 cef14f6af1999fe0b5218d959cca8788ec00afc1b145201ba48344a4b15bbb04; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P02930.receipt.json SHA256 a1299f0ab8dce3aade2529833872b903adb9ae28448c83578a0761559603499a | partial | P02930; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct from direct participation/localization/necessity evidence. |
| plaque-family-IPR014340 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014340/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR014340.raw SHA256 0771d28efa0d43eb3d035c9a2bfe493df3bb92162384988fe8dc6eb3cab22526; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR014340.receipt.json SHA256 315517166ba024faff5052a20f8d5d4d4542788b372967923e2f8e61ace262eb | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR030921 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030921/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030921.raw SHA256 3c2d08b1686549651ee7093273649dded7908b349a60b40e45567fdf432e2924; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030921.receipt.json SHA256 ef9cebd32377c7ffee7993684f97da3bbc22abc45e66590dbd338140424a29e8 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR026265 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026265/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR026265.raw SHA256 e13a5fb3ce284814ce35a6385238428b8b3a64eefe2b790a2550f446dff31c41; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR026265.receipt.json SHA256 ccf1de0c93a0588b67955ef7a0acc95901571049ae13e51aacc42ade3372787f | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR020889 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020889/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR020889.raw SHA256 012318b2911e0a9d11b42b5289e9b0051b4a9cfd6c59fc6c2a091b35642a2bf5; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR020889.receipt.json SHA256 82fc410eaf2a997d38e06768bc534354f713117274348c1216be05a454c13b62 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR007485 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007485/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR007485.raw SHA256 6ae7a373d99ee781c3000e39974e66fd76e6a9c81d478e98c9bd4cb08d3d0669; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR007485.receipt.json SHA256 ac4a5a293112df221a1da3a6d0e921c23ac958d5a9ab88d8dd2a1ad6c70cc9c9 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR030922 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030922/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030922.raw SHA256 64c715c496a528e693830567cc118b2b2fad20562374f2e3cb033d21a8d37863; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030922.receipt.json SHA256 c03626b81806664cda8399c81918c7c8c89e00e8a754e0da9361a133c70be917 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR030923 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030923/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030923.raw SHA256 3a6f425a6e6e4697c474a88abab19320ffe52dafbfdfcbb3d2b6d9402693f8e8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030923.receipt.json SHA256 898726ae0ef2f5627e85fea3e4d47fac4bff428ec508a542befb41d8befe45db | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR011924 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011924/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011924.raw SHA256 43f64974d9b0c477d5e3e6fb416e9a35d79e2322428fe780481bdf2937eb6bef; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011924.receipt.json SHA256 b91f79e22df14a0818f91574be3df9078912f199dac2228b7c5ec0b1b0c024c6 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR011925 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011925/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011925.raw SHA256 efb3b57d6da640ce7de3071f41d7a161baad0daabd7b09521086ce41a6467216; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011925.receipt.json SHA256 3d6da573ee25c05ba68f1362035ab65a17cc044436a354e29ee0910d9f3a8b7b | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR015854 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015854/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR015854.raw SHA256 272d9a8c0574e7444f45a89946d06ba7730f9113cf8f157862f10bd4440c6640; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR015854.receipt.json SHA256 4004999076bd937be6d235b9a4ce4a92c56c10ecf0de54978aa7a1ed11970f09 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR058623 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058623/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058623.raw SHA256 d3ed15d36e942a9a5ab5ef5d0f6538ae597d289bf7747c7ac54c91f400418ce8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058623.receipt.json SHA256 ac490605aeb2024b516f7789c33dfaf4c92c2357b8f07e28dce94dfb39be3e5b | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR050250 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050250/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR050250.raw SHA256 0446bff126f9f98bdb8ce3b393de25b559ab55bd88ea2a207353dcb3bad360fc; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR050250.receipt.json SHA256 cc80e476b515d66197e8d5266bdcdcdce90d3b52b959f25b8d28faf74925b9be | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-IPR058622 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058622.raw SHA256 d3c58cbb9737d5f395f703b634f84df048f355555af2b817f321a5e474b8e310; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058622.receipt.json SHA256 cc35af549b0dd15fa314a3850a322c5a2bb67223c7246601acc42c7c1ba1ad31 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-NF008076 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008076/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008076.raw SHA256 25245b083fe05c65934c02caa3000a91071ccc8d9ce8f9a86e51bf8578f0e467; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008076.receipt.json SHA256 730b223b54da0adb3e11118e021a87b1c0dd85392ab1f125c5ff57a072ae7c7b | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-family-NF008357 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008357/; Exact native family identity/type/signatures and description compared with independently retrieved example membership; broader near misses retained as comparison. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008357.raw SHA256 a190a0b893efd7e75bb191ecf35d6ba381aaa3a04aecc1e6045abfcf13ac79c6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008357.receipt.json SHA256 bbfa1eb28eb46c501022c629876049b2752adb2f7663e22c8422376ec8801159 | partial | Exact named-family grounding support; no family accession guessed. IPR050250 generated descriptive prose is excluded from biological support. |
| plaque-go-0062051 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0062051; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051.raw SHA256 52502a08c75622abe3dc387b50b0b7e01323f6bbc655256799048936462640e3; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051.receipt.json SHA256 d592ed8132b85a2d5ebd8fdb5999c90393adc996e020f666db12637f826cbbfa | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-1990351 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990351; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990351.raw SHA256 f612331f15ccd63723f76f6a394d4cd84d5833db64d78e82319774733c56cd36; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990351.receipt.json SHA256 b0327ae25666d694c2a3cc6d386e2e8670e0c4cb6d2076550164dffaaf02d45d | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-0043190 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043190; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0043190.raw SHA256 ca3b015a4fa8bef4ab9830aa639f3f99f7484b37f26120ed6070d2c25c4c631f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0043190.receipt.json SHA256 19decd325f75e69e8f1d6a938533e04d343ed0dc50c624dcdbc3037e89c6d857 | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-0140306 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0140306; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0140306.raw SHA256 9c6e222a03f9e8290b4c3e88611f726a08a958bfd5e0c96105206f9d6c8b2c0d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0140306.receipt.json SHA256 527e14e7c2bb515812979321d93694103687709fe2d598551889cae352cc2b1c | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-0044874 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044874; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0044874.raw SHA256 abf1bc52e1fd40de4725ecce9516ceef0f3aa3193f017f0ea7ef6b093a1275d5; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0044874.receipt.json SHA256 e161f8dbd24d6c96544055d22f296f0a1569b3c4db3fa3df1b3ed9271c03bff1 | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-1990196 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990196; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196.raw SHA256 4bdbc0587807f14fd6b3786bdff2da82d5aa346bd4d9efffed645b06fe2b4bc6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196.receipt.json SHA256 8bef84fc08ea04fd34d937fb257711720fc18a169ebfed49b7fd6741502a7bc4 | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-1990195 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990195; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990195.raw SHA256 5bd952f4607139605c8ff33e27d0d9470cc7d178d0e6ec365e72672d36738247; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990195.receipt.json SHA256 04dc4c52bc30c26f3823ed10ae0ab10de3ef983d567c1ba4cb7a21f620da398a | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-go-0008559 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0008559; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0008559.raw SHA256 55c2744a45c0c938e020c79e6acd9dd866d8bf3fa789c12821b21e33a4a5658f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0008559.receipt.json SHA256 6e645c702960b7887ef99b75bf81964e5188fcf954020ac1d1ddd970328e29d2 | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-2.raw SHA256 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-2.receipt.json SHA256 11b633598c38185d9b39f6d8fa2057a96e640417b8c093b7f013af382fc6c03a | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-562.raw SHA256 ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-562.receipt.json SHA256 3429206222ca129427834f9bb61bd372a012f08a57d99a283b8b99a2fc9338d6 | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Native source response identity and relevant annotations inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-83333.raw SHA256 f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-83333.receipt.json SHA256 5ac7317f3954e4c4989d12700d6afeb9d097f77ecb494ae3169c80bb31a76ada | partial | Bounded authority evidence; scope limited to the exact accession/term/record response. |
| plaque-cpx-4262 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4262; Complete native CPX-4262 response: participants, counts, bioRoles, taxon, functions/properties and physical-interaction evidence type. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/cpx-4262.raw SHA256 74344dc561706cb864458e9d5e36b05c487d1a6633b2cc379f9761f79819b48c; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/cpx-4262.receipt.json SHA256 848b87bb0b4ab7a99007f5080926ff1f48b089615f54382e67bad5428ad2008e | partial | Explicit LolC1:LolD2:LolE1 and heterotetramer. LolD enzyme; LolC/E unspecified bioRole. No deletion-essentiality annotation inferred. |
| plaque-pdb-7MDY | https://data.rcsb.org/rest/v1/core/entry/7MDY; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY.raw SHA256 dfe61154e5964c515f6da17c9f088704793731a4a5ca927366456049a5484392; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY.receipt.json SHA256 8ef49cf9abe15ba5f9eff3e548aeb54e3da154e1155e1c13107ccf7230a2bd4c | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-7MDY-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/7MDY/1; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-assembly1.raw SHA256 f36d97824690e5893d5685e056bf423569429b20139a3f4b4b7092af70ec4d35; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-assembly1.receipt.json SHA256 002468867a1f46a946d0946c20e77d91468cd6c405169414e3b13e54fdd1473f | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-7MDY-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/7MDY/1; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity1.raw SHA256 6f085339a88c34e05cd541bdd24dfca4f770270c7a0471249232c76ffdcabd52; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity1.receipt.json SHA256 789b35146752259fff0a6637c61d4278f36114d8031a3f29c8181fd1d622592c | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-7MDY-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/7MDY/2; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity2.raw SHA256 6acbe7ff63acbbbcaef6133c374e3ff7a70029cd06b83b1c25d46ab7322cffc8; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity2.receipt.json SHA256 99bfc1841f8b47937835fed6c2c741b5054cc5570ea07ebbd5892e7b8387632d | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-7MDY-entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/7MDY/3; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity3.raw SHA256 8da9d569fe05bd755b5539fad5739e59820ab975cefe4f5fe3b140c67005b0b9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity3.receipt.json SHA256 8fd259da240f5e79b9758ec0eed3ae815d56ec1731c1cbc3f6ab8d648fa8e285 | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-5NIK | https://data.rcsb.org/rest/v1/core/entry/5NIK; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK.raw SHA256 d2799b6484764d471a1ce9763e705aede07783c33badce15004e594d5d443be9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK.receipt.json SHA256 7968fba2a2be6b3d124d2cddeb252f3bef80537e210368ded53020428da048a6 | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-5NIK-assembly1 | https://data.rcsb.org/rest/v1/core/assembly/5NIK/1; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-assembly1.raw SHA256 07d19775fead4956f862ae07ba21095603eb223cd94d349391187ab37af99776; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-assembly1.receipt.json SHA256 c1a183a342a5c6f61df0f4b58621a91b34da09c6a581f69d131d021c1bb0f469 | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-5NIK-entity1 | https://data.rcsb.org/rest/v1/core/polymer_entity/5NIK/1; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity1.raw SHA256 fa2589b36968f01f3d04b0c2b02188f0b9b566629d8c8d6cdd9957a15ba8ea30; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity1.receipt.json SHA256 cbc3d658845d67a2302dbb6524371ed716c5a95cfce9679af430d2ec21893b11 | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-5NIK-entity2 | https://data.rcsb.org/rest/v1/core/polymer_entity/5NIK/2; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity2.raw SHA256 d04c66f5b3c776028830ee4155d3249a4a12efbf9832eb1069cd496764c82783; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity2.receipt.json SHA256 9c9a3a52d77b84cad0bd00b74572bcca637aa4e157b109cdde0131b7ea62b1fb | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-pdb-5NIK-entity3 | https://data.rcsb.org/rest/v1/core/polymer_entity/5NIK/3; RCSB exact entry/assembly1/entity response: deposited identity, author assembly counts, chain/UniProt mappings, source organism versus expression host. Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity3.raw SHA256 d2016d8529eeacec931f3b94ef6c12be4725a1d98934e2dacbc96579ab5e8a7f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity3.receipt.json SHA256 dcb3cd53ae30029c7f8a60331f330963f8aed6e97f4fe76589052eb351125f1c | partial | 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3. Experimental construct limitations come from primary Methods. |
| plaque-PMC2851745-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2851745.1/PMC2851745.1.xml; Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-jats.raw SHA256 23f82e897b6a1873a6d35fe182d39949af7092a21c756c9114b18f67064b9d2b; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-jats.receipt.json SHA256 f04821a1cd605429aba2310202ed92b9296425d3bd4b466cacb3779ff5086baa | context_only | Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather than PDF. Successful alternative routes are independently tiered. |
| plaque-PMC3038725-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3038725.1/PMC3038725.1.xml; Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-jats.raw SHA256 afef1ec318870082585cbf50af335568e02121756a6da96a8255ee28960da0f0; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-jats.receipt.json SHA256 bd700220ea09b31132be086b19838c4b229b1524c1fa6796ca7b6e49e4ac8319 | context_only | Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather than PDF. Successful alternative routes are independently tiered. |
| plaque-PMC5858563-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5858563.1/PMC5858563.1.xml; Complete direct main-body paragraphs0–12: seven-protein proteoliposome LPS transport and LptA-mediated membrane association; no physiological LptA copy-number resolution, no supplemental experiments or pixels inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5858563-jats.raw SHA256 2ba2a990adb12cbeb5829b5fd3d4eb716c9a4807e038ec1cafffa2308a96ee97; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5858563-jats.receipt.json SHA256 ab98d22df9d572e9791478cff72d6ef1d6f685b2e6141b7b70ece02744d5c7f1 | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-PMC3552488-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3552488.1/PMC3552488.1.xml; Complete direct main-body paragraphs0–7: ATP-dependent LPS extraction and transfer, contrasted with ATP-independent LptA/LptC association; no supplement or pixels. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3552488-jats.raw SHA256 524716c6851340007bc32191eaef5626eda010fe739c194a4a943fbb76f1e98d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3552488-jats.receipt.json SHA256 853008adead8616071b6cb7d1276bdef046143fc917ca2bc6432942bdaadcc33 | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-PMC2880507-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2880507.1/PMC2880507.1.xml; Complete direct main-body paragraphs0–9: seven-protein copurification/fractionation and bridge proposal. These association data are not atomic continuous-pathway or universal necessity proof. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2880507-jats.raw SHA256 620e0b9037dba893469d09f9dd830b83c872dccf392da6d1fa3a1c8ae25cf3ff; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2880507-jats.receipt.json SHA256 cff7cb61202411c7eea6ad7568b4621ab70430e404b8204e97a3d36c6b0df797 | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-PMC5672026-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5672026.1/PMC5672026.1.xml; Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5672026-jats.raw SHA256 22dfee541aa6f8eeaa6055886c05ba7d864831564d1be1eb6c04ffda5a948d8b; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5672026-jats.receipt.json SHA256 c7729d08b0e4d58f50eb83efe7a7ed7852ee0aab7be3f60e830106307095b325 | context_only | Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather than PDF. Successful alternative routes are independently tiered. |
| plaque-PMC8333309-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC8333309.1/PMC8333309.1.xml; Primary Results sections3–8 and Methods11,13,15 read: K-12 genes expressed in BL21(DE3), His-LolD complex, Lpp K58-deletion copurification, nucleotide-state cryo-EM and basal ATPase. Bound lipoprotein density is not exact sequence proof; extrusion/reset model distinct from direct transport flux. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC8333309-jats.raw SHA256 f06cbeb2b0cfef54e1b2abb272d1f2a9fbbc657418b548b017ef359fd0e2bb48; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC8333309-jats.receipt.json SHA256 56e4a99448bdf42e3ab1e14bb5948a0430086eda0a1849e2839c4885e26ea1aa | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-PMC5447821-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5447821.1/PMC5447821.1.xml; Primary direct introductory paragraphs, Results S2–S8 and Methods S10,S12,S13 read: W3110 genes, C43(DE3) ΔacrAB expression, MacB-MacA fusion/disulfide-stabilized purification, ordered 2:6:3 core, proposed periplasmic entry/gate. Introductory broader cargo references are not all experimentally assayed here; no pixels/supplemental data read. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5447821-jats.raw SHA256 9a25d568fd93109b8bd837e7bf71e0b1476fcd25182f0247d1d3c013d9fa4611; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5447821-jats.receipt.json SHA256 3ace879c5617227d8246c9cbeae2d703bf3268de89fa3084f4f416104d72f949 | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-PMC2613632-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2613632.1/PMC2613632.1.xml; Primary Experimental Procedures, Results and Discussion text read (including text captions): KAM3(DE3) assays, tagged-protein pulldown, detergent-state dimer biophysics, ATPase kinetics, erythromycin binding and resistance. Two author attributions in the record should name Lin et al. 2009. Detailed coupling models remain interpretations; no supplemental data or pixels. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2613632-jats.raw SHA256 cc4ef19105973cda7330b93388ed3f39471975ca9f51398676ab0b9bae9acb00; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2613632-jats.receipt.json SHA256 949c6bb442d28598cb1d70e82221136a0d00294ee1224789cc8a817547edb781 | partial | Fresh genuine primary source read at the declared bounded extent; assay, construct and evidential-stage limits retained. |
| plaque-pmid-10783239 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10783239+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-10783239.raw SHA256 4e90c52b481aae1c19b7104c6397061c21fe70bfa53e10f14bd61acb275e46a9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-10783239.receipt.json SHA256 87054b473ed0129b97bb0232ba4ac2bfd17691607e6df154023330b18743fbd9 | partial | A new ABC transporter mediating the detachment of lipid-modified proteins from membranes. Primary abstract scope retained. |
| plaque-pmid-18634750 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18634750+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete secondary-review abstract and bibliographic identity only; no body claim. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18634750.raw SHA256 486bed2be46da4e93c72158a1b835a71b731ba22b288d7f2db620544d1aaff0f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18634750.receipt.json SHA256 16def06c5b0a6da2d8a9eccbb4b3d82c7f3da2690a36d62fc3b42bb4bd8ced41 | partial | ATP-binding cassette transporters in Escherichia coli. Secondary synthesis, not primary experiment. |
| plaque-pmid-34344901 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A34344901+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Bibliographic identity/title/authors/DOI and primary body linkage; separate genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-34344901.raw SHA256 e4e20cff1e8c0f66a9e37d9097cbc88e68c7d26905555a0d618a7b2b80768de2; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-34344901.receipt.json SHA256 dcad8534c5c5e313b22df99443158d12cd5d0561afc8d0d7dbaaa623b054e82d | context_only | Mechanism of LolCDE as a molecular extruder of bacterial triacylated lipoproteins. Identity only in this evidence row. |
| plaque-pmid-18955484 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18955484+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Bibliographic identity/title/authors/DOI and primary body linkage; separate genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18955484.raw SHA256 3bd3f3d4f8fc8d32518d6dcd5a638a3f094dac18efe8a85577c3546398ed6ade; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18955484.receipt.json SHA256 f9d32ff0eceeca17fa305fa6dfb0d2d140798670032f9ab0d4d752182fd3c8f0 | context_only | MacB ABC transporter is a dimer whose ATPase activity and macrolide-binding capacity are regulated by the membrane fusion protein MacA. Identity only in this evidence row. |
| plaque-pmid-28504659 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28504659+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Bibliographic identity/title/authors/DOI and primary body linkage; separate genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28504659.raw SHA256 b2f2df1b4d9cd9326012b45b5655a9e2aebc95099d04dc46094322a69ec983ee; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28504659.receipt.json SHA256 362e755a776bfaff122e7dfa5f6e8cececc2a51e5aeb82cac803157b0c48ac02 | context_only | Structure of the MacAB-TolC ABC-type tripartite multidrug efflux pump. Identity only in this evidence row. |
| plaque-pmid-12207697 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12207697+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12207697.raw SHA256 4acb7231e965168dc6e8d81706bf1fc157a3d7e1914a761f2a4c4740594d970a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12207697.receipt.json SHA256 806e8b81e5b7c7946d3167ce038e29924e68c042851123c980e17aafc8fb76f2 | partial | Imp/OstA is required for cell envelope biogenesis in Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-12724388 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12724388+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12724388.raw SHA256 87bbb11612b9d208012d1a5f0f51b4c03b427a081453eb5718828aa491b01f84; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12724388.receipt.json SHA256 6d56a860faf5893dba730f523d9b4566814baec90ba45c21aa0fb62b5c3d38f0 | partial | n-Hexane sensitivity of Escherichia coli due to low expression of imp/ostA encoding an 87 kDa minor protein associated with the outer membrane. Primary abstract scope retained. |
| plaque-pmid-16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16079137+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16079137.raw SHA256 64452b120f275a02c3b16d6dc23744b0a37865ec6c957a437bb12644d987241d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16079137.receipt.json SHA256 a53415ba92da4d08e75780557ddd89b3b3601d586201429a1ea9b5e9afb75820 | partial | Protein complexes of the Escherichia coli cell envelope. Primary abstract scope retained. |
| plaque-pmid-17056748 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17056748+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-17056748.raw SHA256 98e7fdce444d2bc6646d3a6d5b99b117aba709ddcca3a9031f58cb1ad457f6e6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-17056748.receipt.json SHA256 25a4e95e4ef31d1f5327ebd4fba5f73f2713617cef98d337decfe2576f3d9d37 | partial | Characterization of lptA and lptB, two essential genes implicated in lipopolysaccharide transport to the outer membrane of Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-18424520 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18424520+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18424520.raw SHA256 a85cd496ad6bbf9e69b1b03b57dff5cecf8257321f98e3d9a8a9d4a07738e26a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18424520.receipt.json SHA256 b5a48b8a95de861327b5fd7cc465a98ee24ade5e792b6bf3dd674bacd1843b4c | partial | Functional analysis of the protein machinery required for transport of lipopolysaccharide to the outer membrane of Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-18480051 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18480051+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18480051.raw SHA256 64df91f2e64e1517f5069e770d70f359e090b819ef1fffa8834ffbf2d1662e39; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18480051.receipt.json SHA256 fa87978b1caeb5d7e7a5277a90542a9a978cb7107ec44ce9d0602032fb7d923d | partial | The LptA protein of Escherichia coli is a periplasmic lipid A-binding protein involved in the lipopolysaccharide export pathway. Primary abstract scope retained. |
| plaque-pmid-20720015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20720015+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-20720015.raw SHA256 77562c9ea8468a9080f5cb0cead52b9930ce04e70520ced9e58eca0dd14d0461; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-20720015.receipt.json SHA256 79dba0cdf3f8e47ec4b8ca79f8dc2b282db398cd4db0231d2d7342612f8bf78f | partial | Structure and functional analysis of LptC, a conserved membrane protein involved in the lipopolysaccharide export pathway in Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-21257904 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21257904+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Bibliographic identity/title/authors/DOI and primary body linkage; separate genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-21257904.raw SHA256 68b273cb5914a605dae4e98370d516366d649fa8b0e9a987f52af814951df25f; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-21257904.receipt.json SHA256 94799b2120ecd9a12e00d0cc87147bc287ccd3c70c614d2364530bb9ce20598c | context_only | The complex that inserts lipopolysaccharide into the bacterial outer membrane forms a two-protein plug-and-barrel. Identity only in this evidence row. |
| plaque-pmid-3316191 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3316191+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-3316191.raw SHA256 ce9e18cf910238adfced888d5cbc73e15ad84f7807cd5b34870d9acaf935801d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-3316191.receipt.json SHA256 ce69048c214aee59e112fa77980fccb8279124af80fdef920837026efef53311 | partial | Genes encoding two lipoproteins in the leuS-dacA region of the Escherichia coli chromosome. Primary abstract scope retained. |
| plaque-pmid-19500581 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19500581+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-19500581.raw SHA256 5bc71d31def1d0531d0de39ca5e05871759e372e796d90ec33b2b6ffd44953c7; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-19500581.receipt.json SHA256 44291e8fafca957b27e942aa68d00ca385bc5008552bca1fe47b21fa31c646e5 | partial | Biochemical characterization of an ABC transporter LptBFGC complex required for the outer membrane sorting of lipopolysaccharides. Primary abstract scope retained. |
| plaque-pmid-22668317 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22668317+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-22668317.raw SHA256 4d90d55f5badfca47afe7d0553fd20bdad5110d6bfded6cd87e3704648a882ab; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-22668317.receipt.json SHA256 395dad9a98dfa7c5cc20e88bc78014b51ab08d524a70da806e0374a2faf206b6 | partial | Regulated assembly of the transenvelope protein complex required for lipopolysaccharide export. Primary abstract scope retained. |
| plaque-pmid-16861298 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16861298+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16861298.raw SHA256 363ed994ed36a0c2b37a0150170d2036e64e2d60963dfc12efb454892951f106; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16861298.receipt.json SHA256 8cfb557618cba2ecbbdadd3dc3a039f62c515c584d65c5d8e0c04b743f503b66 | partial | Identification of a protein complex that assembles lipopolysaccharide in the outer membrane of Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-18375759 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18375759+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18375759.raw SHA256 6c0c3c22a22f322693f0859ecb37080211a24cf86d67cd3ae5d2b7c4e38ef120; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18375759.receipt.json SHA256 da9906f86f3121871c1d137f8bc91861db6fccba0a9714009a105e1c2b56f09d | partial | Identification of two inner-membrane proteins required for the transport of lipopolysaccharide to the outer membrane of Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-28878019 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28878019+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete secondary-review abstract and bibliographic identity only; no body claim. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28878019.raw SHA256 409f1cc537de7ff02f3b07e2da4dab45d45deb85bfe2153bfec48698145aa03d; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28878019.receipt.json SHA256 18a4084459fb06b125567c539fb5b9d8b782de4f29d7607aae3322cbdb91dcff | partial | The lipopolysaccharide transport (Lpt) machinery: A nonconventional transporter for lipopolysaccharide assembly at the outer membrane of Gram-negative bacteria. Secondary synthesis, not primary experiment. |
| plaque-pmid-25257218 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25257218%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-25257218.raw SHA256 dbd292cf452bbcf52df029258270193b2c7abc3af8f4a0098f101427d90bb531; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-25257218.receipt.json SHA256 1a7f6bf5954d84dcca0a4865397e6d26ee07dfa80685ab954bb99de2e68a9534 | partial | Protoporphyrin (PPIX) efflux by the MacAB-TolC pump in Escherichia coli. Primary abstract scope retained. |
| plaque-pmid-18805970 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18805970%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18805970.raw SHA256 5711bde7f4fe1e8e432cac5bb33e2dcad34a75e5745aae82d8aca1ed624749ce; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18805970.receipt.json SHA256 bb472fd0e4432ba1740dd3fca022d9398ad528214aded84bf89631557ca556b8 | partial | MacAB is involved in the secretion of Escherichia coli heat-stable enterotoxin II. Primary abstract scope retained. |
| plaque-pmid-11544226 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11544226%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Complete native primary abstract and bibliographic identity only, no body, figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-11544226.raw SHA256 34b04bb07df1e84f4678fdba6d89280f9399d50cf1cedd1e372c4a68e7e7c5f9; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-11544226.receipt.json SHA256 ba4966e19bf23c194859e6ba1b852adc3c6a14afa485aa9091c3b186ca6d7f5d | partial | Novel macrolide-specific ABC-type efflux transporter in Escherichia coli. Primary abstract scope retained. |
| plaque-yakushi2000-figure1 | https://www.nature.com/articles/ncb0400_212/figures/1; Public publisher figure 1 title and complete text caption, decoded as UTF-8; no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure1.raw SHA256 fcba753f666a7a6d17748264ab4e29865a32490cf448d8351af4daafcd648b69; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure1.receipt.json SHA256 38aab5322172bfd6431aa5731640f6c747dc610b032c23e74abec28dd526c280 | partial | Pal proteoliposome ATP/LolA-dependent release and LolB transfer assay. |
| plaque-yakushi2000-figure3 | https://www.nature.com/articles/ncb0400_212/figures/3; Public publisher figure 3 title and complete text caption, decoded as UTF-8; no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure3.raw SHA256 41c80de15b510c802441e0a290804dd55153d5a74dd67a698c5d0fd93904e3ac; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure3.receipt.json SHA256 0d0c70d32e4b5e9dc164cb4d70382baf973e8dbe4c17154b288522ea4cf20c4e | partial | LolD mutants, JE5505/JE5506 Lpp growth comparisons and DLP79-22 spheroplast Lpp release assay. |
| plaque-yakushi2000-figure4 | https://www.nature.com/articles/ncb0400_212/figures/4; Public publisher figure 4 title and complete text caption, decoded as UTF-8; no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure4.raw SHA256 8ec2e9e8ba871fd2303dda5df615e76aa972b22c3c471d920d5400135c418c75; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure4.receipt.json SHA256 1492e243a91e68b44bd20ccc8647281913bbde28a440f311a2c32134f28d14a0 | partial | Pal outer-leaflet proteoliposome release and protease-protection experiments. |
| plaque-yakushi2000-figure7 | https://www.nature.com/articles/ncb0400_212/figures/7; Public publisher figure 7 title and complete text caption, decoded as UTF-8; no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure7.raw SHA256 0447128fc41d705d757b0694611fc9a8e97fd9fc394505d74f275502da33ef55; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure7.receipt.json SHA256 15d74c23ca1ea251fb589024ac8d199fa69d6617f020ce43d6bf08274205b52e | partial | Model caption distinguishes Asp+2 inner-membrane lipoproteins from non-Asp+2 outer-membrane lipoproteins. |
| plaque-adapter-b0054 | https://imodulondb.org/api/genes/e_coli/precise1k/b0054; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054.raw SHA256 afbb01c7d50a3e0554edc74d97d72c73233e9bb57ebdc0f3084414473b766bd6; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054.receipt.json SHA256 ff47ce46e5bf405898b387688e043b58a5ff3b92a5fe969b32ef54354294119b | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0054-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0054/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054-modules.raw SHA256 b7cb5257aaf8002c3e66ba15137cf03baa4e2ad2808259ece68763901d61df4e; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054-modules.receipt.json SHA256 b8fa566f459a23b2824ff23e03810c175b2fb0efe9bd05c8789ea85a7bea7074 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0641 | https://imodulondb.org/api/genes/e_coli/precise1k/b0641; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641.raw SHA256 008d4160cff20dc5836c8a35376b65bce93dac1cc4ce9f290642c4b5b6ea56f2; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641.receipt.json SHA256 e9e678046e146669b08580bbd4d00d70cf3f3d362db195c8cbd7566565c1547d | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0641-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0641/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641-modules.raw SHA256 6b71b8b00939a5dd834219a04a43fda62b1e9b7e0360e589de968d38f4532442; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641-modules.receipt.json SHA256 ba03de166d3609460d279e275e64ff5a45bad6eff43a43747e7e39da894d32c4 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0741 | https://imodulondb.org/api/genes/e_coli/precise1k/b0741; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741.raw SHA256 f706efff4ca56892ccf7c4b3ea5163aaf0a2fba02ead0c88389f60d583147fb2; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741.receipt.json SHA256 8ff90841c159ce395292db07b3d4888e5316e27f858fe0532f485f77916fd7dc | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0741-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0741/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741-modules.raw SHA256 f9c546a89ead820156e0a18bb74bc9afcab24447fdf492bbf608a183bf6c8419; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741-modules.receipt.json SHA256 01f96c632bdf8b48a579fb647ed4ce9a0249f24a7bf90e151421d55f3f119234 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0878 | https://imodulondb.org/api/genes/e_coli/precise1k/b0878; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878.raw SHA256 993339965dcb1dbeab0e209ab7ec8f776099bcccb1d82d8baf328969e00bf8da; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878.receipt.json SHA256 d7e8a8a704d575f713f07a13069cec5c2159a5ca06ea533c14d83d867c234b0c | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0878-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0878/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878-modules.raw SHA256 dc1f3d2335e3f8a0f27e6374d3a8be853eff8a71b10972d7408ff8ed704b9ca5; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878-modules.receipt.json SHA256 63436a1e61291d1f143e20d3246140f303c73b7e6e54e36dd5609a699a7f722e | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0879 | https://imodulondb.org/api/genes/e_coli/precise1k/b0879; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879.raw SHA256 182e707ecf9aaa44267b54e298131624182ae19c60b076bb6559dc4657f0925a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879.receipt.json SHA256 1411fe7160d1fc1cd259c9cf1d4472b26118519710e3526f215deac51d989f56 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b0879-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b0879/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879-modules.raw SHA256 e378238a159a7b1c2fc2b249b6a6305cacdb4a741894230e91f5004412adb2e1; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879-modules.receipt.json SHA256 46a0c4dcb439425c94abeb963dcea10e022356f19ea4b54a6f9437111a2073cc | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1116 | https://imodulondb.org/api/genes/e_coli/precise1k/b1116; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116.raw SHA256 3edee3ba975893ce7af0e2e47dcf77622948c363e0451cb425cb75d91cdd77ef; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116.receipt.json SHA256 dea84940e916ee8a30929385c47a008841bb91f51cbd4cbe912565226a4ceb05 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1116-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b1116/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116-modules.raw SHA256 7f6719d2867e699d7c92304895375c30227897a28cefcb5b015b00a9c2e34445; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116-modules.receipt.json SHA256 f0e151edb52ec58d60c11988121cac9d734b4f46df646fcdfd08fbc91207d9bc | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1117 | https://imodulondb.org/api/genes/e_coli/precise1k/b1117; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117.raw SHA256 6dc84fb1f0ff5e43a52d728111a992d3d5772c1c11bce03e414c4a16a027aeb0; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117.receipt.json SHA256 409bba946cfe17ca0d594eba24bd7a1fa569f6430453b30d8a7e103a5c6e3ab8 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1117-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b1117/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117-modules.raw SHA256 86b3250cb1381a9e64880d4897979c83f9f020f49a92f7d792a47c286a22b16a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117-modules.receipt.json SHA256 3227ca056cf1543687ddc127dd0924a1b575d32025f084b1c41ff292a602aa65 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1118 | https://imodulondb.org/api/genes/e_coli/precise1k/b1118; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118.raw SHA256 e2c26351aed611404ee9d87678250a78e553f86289c38e1c3a3dc158adc87fed; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118.receipt.json SHA256 56cd11f044e819f912c1256339473430e215340ef9d71f0d4d0cf2eefc10f934 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1118-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b1118/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118-modules.raw SHA256 f80b2a99f8b4cce1ec72818ac91a8a11b5e31c0b0402f91b44ea5b7a5d80bdc3; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118-modules.receipt.json SHA256 69285f340a4c61c1e2881cf2a7873a05609b80bd963b803530f0d7d50d3a5545 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1677 | https://imodulondb.org/api/genes/e_coli/precise1k/b1677; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677.raw SHA256 d2c646ac4c203b1ca72c75955f47a99a92b58dae718a0643ea3e4a7066a22513; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677.receipt.json SHA256 e10672b9c898ea7373f73d3beb53bf2afd75f10e0b80b253607e6d53890c5128 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b1677-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b1677/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677-modules.raw SHA256 1e48c9eeba3cd8fe5bd62ece576b84f7c86c6aa45c5f875f6bcd6e80fe3bf8a5; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677-modules.receipt.json SHA256 210573623e7fea185be0c756b3bc4c66a663d0a9f6cb1271bcb4deca9724fa75 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3035 | https://imodulondb.org/api/genes/e_coli/precise1k/b3035; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035.raw SHA256 3c1072490b201aff8b31f919b89d538017fabee3272bdf9115b4949ad8844a7a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035.receipt.json SHA256 bf169f1b324b8ce0c8b0f94ebe71b6c1e23dd278f82e35a95850e1b85822effe | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3035-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b3035/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035-modules.raw SHA256 c65a4d314d71a084b2bf80376d7a091196d354d2d4cbc86c6b07b60952e15988; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035-modules.receipt.json SHA256 db6f5f7cf7518b2a18e8c291bb875efd53097fb05dde7b5ecfb2f43ebb116c9c | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3199 | https://imodulondb.org/api/genes/e_coli/precise1k/b3199; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199.raw SHA256 73f015ea9b9806201ae77c61660fcb0c9885d5b955db0f8a7a9e67d7acaca868; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199.receipt.json SHA256 1b5a3417c02f626f489f6231f3096f20ce0616a43fec1e6762690eeb41312605 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3199-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b3199/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199-modules.raw SHA256 46ed8c54560a4ede0a9019a7d65bd5d609e1ab95170045a2907f3bf46ffcd87a; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199-modules.receipt.json SHA256 1920f586305d94f4b259529ae13e57ac5bb91d6ed61189c081b01dbc60608e7f | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3200 | https://imodulondb.org/api/genes/e_coli/precise1k/b3200; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200.raw SHA256 a6ec3cce59ce2d2c618ea96eda3a0c4246b1eb8c20ef20a38ba70fafd7aa338e; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200.receipt.json SHA256 16f193de54f1faa9ff85f2550412d144d4568af2734f167c572944d326068880 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3200-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b3200/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200-modules.raw SHA256 bb054259370bf3f2aa6d748bab64f3fdb222bbf72b7021f4568f863bd8372c55; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200-modules.receipt.json SHA256 143d838bcf082e68b1985178b3d9f03812985e698d4d4921a8b0e213889bb973 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3201 | https://imodulondb.org/api/genes/e_coli/precise1k/b3201; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201.raw SHA256 9184bf4470a080a9537eb62ffb5a3f8a482e1bc45ff8c0f86a49727badadcbdb; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201.receipt.json SHA256 5d2276aad18920fe0cacf5e4e370fb6a04c809eb341fb7bc91adc41152dc9313 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b3201-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b3201/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201-modules.raw SHA256 ef299a66694efa19451c0a8bda4d69b54bf9e350cd9fe2cfd36821a96e04abae; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201-modules.receipt.json SHA256 fba48c9898f1432e612e18964af96c8f43cc637a281e061f0f5e69c1e608cbaf | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b4261 | https://imodulondb.org/api/genes/e_coli/precise1k/b4261; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261.raw SHA256 2bdb1fa5be7099671156704e18a31ea719cbcac6ae5327fe791986d55ae40b1c; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261.receipt.json SHA256 b0ea87b9f901d2d79a0028bbb259743832328d0c44a6bf9d7e351c3ab0670aa1 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b4261-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b4261/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261-modules.raw SHA256 bd9da7a4cddcdab9cc3b647fcccf4bfd9bcdf878f4df460d89d0dd5f85fb6f92; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261-modules.receipt.json SHA256 70b9fd56aae2816d902a94aa54ad9f5c2d723a4475ce87097fe950035d9fd167 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b4262 | https://imodulondb.org/api/genes/e_coli/precise1k/b4262; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262.raw SHA256 88ccf9370c561f2014c8acbe3f364f5a6de7a14c8372325080756c14f4625f50; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262.receipt.json SHA256 79000bcef0f102831b5554ff9576e90ff87ae2ead3bdba5f2e272c932e8b83a2 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-b4262-modules | https://imodulondb.org/api/genes/e_coli/precise1k/b4262/imodulons; Official E. coli precise1k exact-locus or exact-module response; full returned computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262-modules.raw SHA256 f88707c86222d991c2459899bbdaab7367091571fa718847a74b0dda44ccf763; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262-modules.receipt.json SHA256 ffbab103607d1cd81e6e61d94cd97be1c16eb298823ab091b9e25a2579fb0b36 | partial | Expression-module evidence only, not localization, physical assembly, transport or absence proof. |
| plaque-adapter-catalogue | https://imodulondb.org/api/organisms; Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-catalogue.raw SHA256 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693; receipt SHA256 d83e600c4e77f3eecbfc797c94114aa865f20bf3c57049a31ac0f0ba0eb17c03. Full catalogue/metadata/index; for gene table exact full-table scan for 15 named loci. Generated prose excluded. | partial | 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This is not exact equivalence to all experimental strains or recombinant constructs. |
| plaque-adapter-precise1k-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-precise1k-meta.raw SHA256 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865; receipt SHA256 bc0785967572c75209e0274775d75d945dffe53f2ec5c37bfb228b0f48d16c7e. Full catalogue/metadata/index; for gene table exact full-table scan for 15 named loci. Generated prose excluded. | partial | 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This is not exact equivalence to all experimental strains or recombinant constructs. |
| plaque-adapter-precise1k-genes | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;limit=5000; Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-precise1k-genes.raw SHA256 db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27; receipt SHA256 8c5b751e9c0f107a1d1bdd84d136c9ab7ec49497b4c02dc4e94f9e908e889969. Full catalogue/metadata/index; for gene table exact full-table scan for 15 named loci. Generated prose excluded. | partial | 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This is not exact equivalence to all experimental strains or recombinant constructs. |
| plaque-adapter-precise1k-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-precise1k-modules.raw SHA256 c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d; receipt SHA256 886c69335fab65b02c9c3d2c197a242a2da2e16a92e8a17aee602ed59fa74dd0. Full catalogue/metadata/index; for gene table exact full-table scan for 15 named loci. Generated prose excluded. | partial | 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This is not exact equivalence to all experimental strains or recombinant constructs. |
| plaque-adapter-joined-scope | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-membership-summary.json; Computed full 201-row per-gene memberships, exact selected module metadata and full module member tables; summary SHA256 42a00f0dc04109162b6a88252b8481bf7936b661effce1622fb799987205fbb6 | supports | Positive memberships: lptA/B/C and tolC in22/SoxS, lpp in45/Resistance, lptF in167/UC-2; full member counts117/58/96 confirm these joins. Other9 loci have no true membership among201. These are thresholded computational contexts, never biological absence or assembly evidence. |
| plaque-lolcde-stale-delta | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/lolcde-stale.diff; Exact old frozen record versus current source; SHA256 1dc27510e1617705b107334a77e63b34239838d96dc8fbf34fba266d0ae21b21 | context_only | Delta adds Lpp/Pal substrate xrefs, three LolC/D/E contributes-to membership edges and one lipoprotein-release-to-localization edge, with history. Family-grounding finding remains unaffected. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record structured-source and scientific review | supports | Positive named molecular/pathway claims trigger actual host coverage assessment; no-expression wording alone does not establish exemption. |
| septin-curation-policy | docs/CURATION.md; Exact component identities and dated discussion contract | supports | Resolve demonstrated exact class groundings, while retaining valid broader classes and preserving dated rationale. Current clarification does not rewrite historical searches. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component and graph identity; experimental necessity | supports | A verified accession and covered typed node do not establish structural class identity, universal formation necessity, copy count or source-specific experiment. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native reference identity and query scope | supports | Native names/status/taxa and exact current searches establish reference identity, not historical release results, experimental strain or causal membership. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, intervention and source attribution | supports | Component membership, source-specific counts, activity and whole-assembly formation differ. External regulators need not be constituents. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Exact source access tiers | supports | Primary abstracts, genuine main text, secondary synthesis, metadata and actual pixels have distinct scopes. Failed access is validation context only. |
| septin-review-schema | schema/record_review.yaml; Native review envelope and lineage | supports | Use unique evidence references, exact predecessor repository/review/finding and bounded searches. |
| septin-up-P38313 | https://rest.uniprot.org/uniprotkb/P38313.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P38313: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "AME1"}, "synonyms": [{"value": "ARP100"}], "orderedLocusNames": [{"value": "YBR211C"}], "orfNames": [{"value": "YBR1458"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P47149 | https://rest.uniprot.org/uniprotkb/P47149.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P47149: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "NNF1"}, "orderedLocusNames": [{"value": "YJR112W"}], "orfNames": [{"value": "J2011"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-Q02732 | https://rest.uniprot.org/uniprotkb/Q02732.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | Q02732: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "CTF19"}, "synonyms": [{"value": "MCM18"}], "orderedLocusNames": [{"value": "YPL018W"}], "orfNames": [{"value": "LPB13W"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-Q04477 | https://rest.uniprot.org/uniprotkb/Q04477.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | Q04477: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "SPC24"}, "orderedLocusNames": [{"value": "YMR117C"}], "orfNames": [{"value": "YM9718.16C"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P40568 | https://rest.uniprot.org/uniprotkb/P40568.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P40568: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "DSN1"}, "orderedLocusNames": [{"value": "YIR010W"}], "orfNames": [{"value": "YIB10W"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-Q12143 | https://rest.uniprot.org/uniprotkb/Q12143.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | Q12143: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "NSL1"}, "orderedLocusNames": [{"value": "YPL233W"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-Q06675 | https://rest.uniprot.org/uniprotkb/Q06675.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | Q06675: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "MCM21"}, "synonyms": [{"value": "CTF5"}], "orderedLocusNames": [{"value": "YDR318W"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P36012 | https://rest.uniprot.org/uniprotkb/P36012.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P36012: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "CSE4"}, "synonyms": [{"value": "CSL2"}], "orderedLocusNames": [{"value": "YKL049C"}], "orfNames": [{"value": "YKL262"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P33895 | https://rest.uniprot.org/uniprotkb/P33895.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P33895: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "NUF2"}, "orderedLocusNames": [{"value": "YOL069W"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P39731 | https://rest.uniprot.org/uniprotkb/P39731.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P39731: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "MTW1"}, "synonyms": [{"value": "DSN3"}, {"value": "NSL2"}], "orderedLocusNames": [{"value": "YAL034W-A"}], "orfNames": [{"value": "YAL034AW"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P40460 | https://rest.uniprot.org/uniprotkb/P40460.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P40460: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "9585415"}], "value": "NDC80"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "10409732"}], "value": "HEC1"}, {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "9335591"}], "value": "TID3"}], "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000001406"}], "value": "YIL144W"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P53298 | https://rest.uniprot.org/uniprotkb/P53298.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P53298: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "10323865"}], "value": "OKP1"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000003411"}], "value": "YGR179C"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P40014 | https://rest.uniprot.org/uniprotkb/P40014.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P40014: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"value": "SPC25"}, "orderedLocusNames": [{"value": "YER018C"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxon name, identifiers and lineage | supports | Saccharomyces cerevisiae identity verified; S288C annotation identity is not W303/YKO200 experimental identity. |
| septin-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native taxon name, identifiers and lineage | supports | Saccharomyces cerevisiae S288C identity verified; S288C annotation identity is not W303/YKO200 experimental identity. |
| septin-pmid-14581449 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14581449+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Architecture of the budding yeast kinetochore reveals a conserved molecular core.; Westermann S, Cheeseman IM, Anderson S, Yates JR, Drubin DG, Barnes G.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-14581449-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14581449+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-11179222 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11179222+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | The budding yeast proteins Spc24p and Spc25p interact with Ndc80p and Nuf2p at the kinetochore and are important for kinetochore clustering and checkpoint control.; Janke C, Ortiz J, Lechner J, Shevchenko A, Shevchenko A, Magiera MM, Schramm C, Schiebel E.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-11179222-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11179222+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-10323865 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | A putative protein complex consisting of Ctf19, Mcm21, and Okp1 represents a missing link in the budding yeast kinetochore.; Ortiz J, Stemmann O, Rank S, Lechner J.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-10323865-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-12455957 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12455957+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Nnf1p, Dsn1p, Mtw1p, and Nsl1p: a new group of proteins important for chromosome segregation in Saccharomyces cerevisiae.; Euskirchen GM.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-12455957-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12455957+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-14602074 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14602074+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | An Mtw1 complex promotes kinetochore biorientation that is monitored by the Ipl1/Aurora protein kinase.; Pinsky BA, Tatsutani SY, Collins KA, Biggins S.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-14602074-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14602074+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-11266451 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11266451+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | The Ndc80p complex from Saccharomyces cerevisiae contains conserved centromere components and has a function in chromosome segregation.; Wigge PA, Kilmartin JV.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-11266451-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11266451+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-29046335 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Molecular basis for inner kinetochore configuration through RWD domain-peptide interactions.; Schmitzberger F, Richter MM, Gordiyenko Y, Robinson CV, Dadlez M, Westermann S.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-29046335-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-14657030 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14657030+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Nsl1p is essential for the establishment of bipolarity and the localization of the Dam-Duo complex.; Scharfenberger M, Ortiz J, Grau N, Janke C, Schiebel E, Lechner J.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-14657030-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14657030+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Global analysis of protein localization in budding yeast.; Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-14562095-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-11952896 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11952896+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Spc24 interacts with Mps2 and is required for chromosome segregation, but is not implicated in spindle pole body duplication.; Le Masson I, Saveanu C, Chevalier A, Namane A, Gobin R, Fromont-Racine M, Jacquier A, Mann C.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-11952896-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11952896+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-query-CSE4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACSE4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P36012. Does not reconstruct historical searches or establish biological absence. |
| septin-query-CTF19-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACTF19%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: Q02732. Does not reconstruct historical searches or establish biological absence. |
| septin-query-OKP1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AOKP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P53298. Does not reconstruct historical searches or establish biological absence. |
| septin-query-MCM21-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMCM21%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: Q06675. Does not reconstruct historical searches or establish biological absence. |
| septin-query-AME1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAME1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P38313. Does not reconstruct historical searches or establish biological absence. |
| septin-query-MTW1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMTW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P39731. Does not reconstruct historical searches or establish biological absence. |
| septin-query-DSN1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSN1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P40568. Does not reconstruct historical searches or establish biological absence. |
| septin-query-NSL1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: Q12143. Does not reconstruct historical searches or establish biological absence. |
| septin-query-NNF1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANNF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P47149. Does not reconstruct historical searches or establish biological absence. |
| septin-query-NDC80-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDC80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P40460. Does not reconstruct historical searches or establish biological absence. |
| septin-query-NUF2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANUF2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P33895. Does not reconstruct historical searches or establish biological absence. |
| septin-query-SPC24-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPC24%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: Q04477. Does not reconstruct historical searches or establish biological absence. |
| septin-query-SPC25-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPC25%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P40014. Does not reconstruct historical searches or establish biological absence. |
| septin-up-Q13342 | https://rest.uniprot.org/uniprotkb/Q13342.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | Q13342: UniProtKB reviewed (Swiss-Prot); taxon 9606; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000312", "source": "HGNC", "id": "HGNC:17133"}], "value": "SP140"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "8695863"}], "value": "LYSP100"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-Q99856 | https://rest.uniprot.org/uniprotkb/Q99856.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | Q99856: UniProtKB reviewed (Swiss-Prot); taxon 9606; genes [{"geneName": {"value": "ARID3A"}, "synonyms": [{"value": "DRIL1"}, {"value": "DRIL3"}, {"value": "DRX"}, {"value": "E2FBP1"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-tax-9606 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606; Native taxon name, identifiers and lineage | supports | Homo sapiens identity verified; S288C annotation identity is not W303/YKO200 experimental identity. |
| septin-pmid-8910577 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910577+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Identification and characterization of a leukocyte-specific component of the nuclear body.; Bloch DB, de la Monte SM, Guigaouri P, Filippov A, Bloch KD.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-8910577-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910577+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-8695863 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8695863+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | LYSP100-associated nuclear domains (LANDs): description of a new class of subnuclear structures and their relationship to PML nuclear bodies.; Dent AL, Yewdell J, Puvion-Dutilleul F, Koken MH, de The H, Staudt LM.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-8695863-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8695863+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-25593309 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25593309+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Screen identifies bromodomain protein ZMYND8 in chromatin recognition of transcription-associated DNA damage that promotes homologous recombination.; Gong F, Chiu LY, Cox B, Aymard F, Clouaire T, Leung JW, Cammarata M, Perez M, Agarwal P, Brodbelt JS, Legube G, Miller KM.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-25593309-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25593309+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-query-SP140-9606 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASP140%29+AND+%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: Q13342. Does not reconstruct historical searches or establish biological absence. |
| septin-up-P39925 | https://rest.uniprot.org/uniprotkb/P39925.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P39925: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "7900428"}, {"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000000819"}], "value": "AFG3"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "7754704"}], "value": "YTA10"}], "orderedLocusNames": [{"value": "YER017C"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-up-P40341 | https://rest.uniprot.org/uniprotkb/P40341.json; Complete native identity; gene primary/alias/locus fields, status/taxon; FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references | supports | P40341: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "7754704"}, {"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000004695"}], "value": "YTA12"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "7929327"}], "value": "RCA1"}], "orderedLocusNames": [{"value": "YMR089C"}], "orfNames": [{"value": "YM9582.14C"}]}]. Native annotation is not a substitute for the independently scoped experimental source. |
| septin-pmid-7929327 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7929327+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | A new member of a family of ATPases is essential for assembly of mitochondrial respiratory chain and ATP synthetase complexes in Saccharomyces cerevisiae.; Tzagoloff A, Yue J, Jang J, Paul MF.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-7929327-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7929327+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-21147776 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21147776+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Electron cryomicroscopy structure of a membrane-anchored mitochondrial AAA protease.; Lee S, Augustin S, Tatsuta T, Gerdes F, Langer T, Tsai FT.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-21147776-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21147776+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-pmid-8681382 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8681382+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | The YTA10-12 complex, an AAA protease with chaperone-like activity in the inner membrane of mitochondria.; Arlt H, Tauer R, Feldmann H, Neupert W, Langer T.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-pmid-8681382-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8681382+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-query-AFG3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAFG3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P39925. Does not reconstruct historical searches or establish biological absence. |
| septin-query-YTA12-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYTA12%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete current returned identities, primary names and aliases | supports | Current query returns 1 entry: P40341. Does not reconstruct historical searches or establish biological absence. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444,GO:0000776,GO:0000817,GO:0004176,GO:0005743,GO:0005745,GO:0007059,GO:0016604,GO:0016605,GO:0016606,GO:0031262,GO:0031981,GO:0034982,GO:0098800,GO:1905368; Complete native term response: identifier/name/status/definition/synonyms/typed relationships or requested is_a ancestors | supports | Current exact GO identities verified. GO0043505 denotes the whole CENP-A nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and from a direct versus inherited ontology relation. |
| septin-go-0000776-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776/ancestors?relations=is_a; Complete native term response: identifier/name/status/definition/synonyms/typed relationships or requested is_a ancestors | supports | Current exact GO identities verified. GO0043505 denotes the whole CENP-A nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and from a direct versus inherited ontology relation. |
| septin-go-0016606-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016606/ancestors?relations=is_a; Complete native term response: identifier/name/status/definition/synonyms/typed relationships or requested is_a ancestors | supports | Current exact GO identities verified. GO0043505 denotes the whole CENP-A nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and from a direct versus inherited ontology relation. |
| septin-go-0005745-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005745/ancestors?relations=is_a; Complete native term response: identifier/name/status/definition/synonyms/typed relationships or requested is_a ancestors | supports | Current exact GO identities verified. GO0043505 denotes the whole CENP-A nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and from a direct versus inherited ontology relation. |
| septin-go-cenpa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043505; Complete native term response: identifier/name/status/definition/synonyms/typed relationships or requested is_a ancestors | supports | Current exact GO identities verified. GO0043505 denotes the whole CENP-A nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and from a direct versus inherited ontology relation. |
| septin-westermann-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200305100%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Architecture of the budding yeast kinetochore reveals a conserved molecular core.; Westermann S, Cheeseman IM, Anderson S, Yates JR, Drubin DG, Barnes G.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-westermann-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200305100%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-dewulf-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144403%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Hierarchical assembly of the budding yeast kinetochore from multiple subcomplexes.; De Wulf P, McAinsh AD, Sorger PK.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-dewulf-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144403%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-biggins-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fgenetics.112.145276%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | The composition, functions, and regulation of the budding yeast kinetochore.; Biggins S.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-biggins-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fgenetics.112.145276%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Secondary Biggins synthesis, not an independent primary experiment. |
| septin-zong-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1093%2Femboj%2F19.15.4123%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Regulation of matrix attachment region-dependent, lymphocyte-restricted transcription through differential localization within promyelocytic leukemia nuclear bodies.; Zong RT, Das C, Tucker PW.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-zong-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1093%2Femboj%2F19.15.4123%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-luo-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-026-73040-0%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Structural basis for prohibitin-mediated regulation of mitochondrial m-AAA protease.; Luo D, Zheng L, Lu MA, Chen Z, Wang P, Guo Q, Gao N.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-luo-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-026-73040-0%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-lee-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.158741%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact MED metadata: title, authors, date, DOI/PMID and abstract availability | context_only | Electron cryomicroscopy structure of a membrane-anchored mitochondrial AAA protease.; Lee S, Augustin S, Tatsuta T, Gerdes F, Langer T, Tsai FT.. Bibliography only; separately classified abstract/body carries scientific support. |
| septin-lee-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.158741%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no unlisted Methods, figure or supplement access implied | supports | Complete primary abstract independently read. Its stated experiment, species and uncertainty are retained; no hidden body/strain detail is inferred. |
| septin-ipr-IPR043563 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR043563/; Native accession/name/type/member signatures and curation flags; native UniProt cross-references compared | supports | IPR043563 {'name': 'Nuclear body protein Sp110/Sp140/Sp140L-like', 'short': 'Sp110/Sp140/Sp140L-like'}; type family. Family versus domain and paralogue coverage distinguished; descriptive prose does not establish necessity. |
| septin-ipr-IPR030411 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030411/; Native accession/name/type/member signatures and curation flags; native UniProt cross-references compared | supports | IPR030411 {'name': 'Nuclear body protein Sp140, bromodomain', 'short': 'Sp140_Bromo'}; type domain. Family versus domain and paralogue coverage distinguished; descriptive prose does not establish necessity. |
| septin-ipr-IPR050928 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050928/; Native accession/name/type/member signatures and curation flags; native UniProt cross-references compared | supports | IPR050928 {'name': 'ATP-dependent Zinc Metalloprotease', 'short': 'ATP-dep_Zn_Metalloprotease'}; type family. Unchecked machine-generated biological prose excluded; only native identity/classification used. |
| septin-ipr-IPR005936 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005936/; Native accession/name/type/member signatures and curation flags; native UniProt cross-references compared | supports | IPR005936 {'name': 'ATP-dependent zinc metalloprotease, FtsH', 'short': 'FtsH'}; type family. Family versus domain and paralogue coverage distinguished; descriptive prose does not establish necessity. |
| septin-ipr-IPR011546 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011546/; Actual failed HTTP response | context_only | HTTP 429 does not supply usable family evidence; separate successful retry retains its own time/hash. |
| septin-ipr-retry-IPR011546 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011546/; Native accession/name/type/member signatures and curation flags; native UniProt cross-references compared | supports | IPR011546 {'name': 'Peptidase M41, FtsH extracellular', 'short': 'Pept_M41_FtsH_extracell'}; type domain. Family versus domain and paralogue coverage distinguished; descriptive prose does not establish necessity. |
| septin-panther-retry-SP140 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR46386/; Native accession/name/type/member signatures and curation flags; native UniProt cross-references compared | supports | PTHR46386 {'name': 'NUCLEAR BODY PROTEIN SP140', 'short': None}; type family. Family versus domain and paralogue coverage distinguished; descriptive prose does not establish necessity. |
| septin-westermann-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2173538/fullTextXML; Genuine JATS sections3–7 and Methods9/10/12/13; full relevant text and embedded captions, not supplement or pixels | supports | Purified Cse4 material includes H2A/H2B/H4 without detectable H3; MIND identities and conditional CEN occupancy support a coarse yeast core. Tagged preparations used300mM KCl; conditional occupancy/stability is not complete-kinetochore formation or universal stoichiometry. Exact strain table was not opened. |
| septin-dewulf-ncbi | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC289150/; Genuine NCBI main article: abstract; Results hydrodynamic/COMA/MIND composition and conditional dependency sections through Fig6; Methods strains/biochemistry/microscopy; embedded relevant captions | supports | W303-congenic preparations distinguish stable COMA/MIND/Ndc80 complexes from variable co-purifications. Conditional24/37C perturbations, CEN occupancy and protein stability are separate from universal assembly necessity. COMA nonessential Ctf19/Mcm21 and residual subcomplexes are explicit. No supplementary tables or pixels inspected. |
| septin-biggins-ncbi | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730914/; Genuine secondary review: complete abstract; Centromeric chromatin paragraphs, composition/CBF3/CCAN and architecture sections actually read; no figure pixels | supports | Secondary synthesis supports coarse centromeric platform and inner/outer hierarchy while explicitly discussing disputed Cse4 nucleosome arrangements and unresolved minimal assembly requirements. No fixed octameric stoichiometry or all-or-none formation rule is imported. |
| septin-zong-ncbi | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC306587/; Genuine NCBI main body: Introduction, Results interaction/reporter/redistribution/matrix sections; Discussion; Methods and embedded relevant figure captions | supports | Human lymphocyte cDNA/LYSp100B, J558L mouse plasmacytoma reporter and HeLa/Jurkat comparisons are distinct. LYSp100B interacts in vitro; in-vivo co-IP was not detected. Overexpressed Bright redistributes LYSp100B, and reporter coactivation occurs in J558 but not HeLa/Jurkat. The proposed endogenous/coactivation mechanism and nuclear-domain formation necessity are not directly established. Human ARID3A reference xref does not make every source construct human. |
| septin-lee-ncbi | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3039362/; Genuine NCBI primary main article: abstract/Introduction, Experimental Procedures, Results and Discussion, embedded captions; no supplement, pixels or raw map analysis | supports | YKO200 genetic rescue and purified ATP-hydrolysis-deficient Trap Yta10E388Q/His6-Yta12E448Q preparations are explicit. Roughly equimolar purified proteins and a cross-linked detergent/C6 12-angstrom model support a preparation-specific hexamer. The map cannot distinguish paralogs; alternating assignment is inferred from prior biochemistry. No count of zinc ions is established by the inspected preparation source. |
| septin-luo-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13376388/fullTextXML; Genuine JATS Introduction; Results conserved PHB-protease interaction and yeast Fig4 perturbation; Discussion; yeast engineering, MrpL32 processing and stress Methods; exact embedded Fig4 caption and license | supports | W303-1B endogenous Yta12 residues236–251 or199–290 replaced withGGGGGS; TEF-driven C-terminal Strep MrpL32 reporter precursor/total endpoint after14hYPG30C, four biological replicates. PHB1 loss/SIM replacement lower precursor fraction, IMSD replacement raises it; separate YPG2mMH2O2 growth assays do not prove a reporter-to-stress causal link. Ct/human co-purification/predicted interfaces are not atomic yeast contacts or compulsory protease constituents. |
| septin-luo-fig4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC13376388.1/41467_2026_73040_Fig4_HTML.jpg; Actual external figure pixels viewed: panelsA–D and matching JATS caption; raw JPG/MD5 checked | supports | Immunoblots, precursor quantification and plate dilution panels match the retained source-scoped interpretation. MD5 8437fa5c981491200b4243f15c6cef68 matches the link-only record. CC BY-NC-ND4.0 and attribution verified in genuine JATS; no figure file is copied into the repository. |
| septin-cpx-1654 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1654; Complete native composition, participants/roles, annotations/properties/evidence and null stochiometry fields | supports | CPX-1654 identifies P40341/YTA12, P39925/AFG3 and CHEBI29105 zinc with enzyme/cofactor roles. All three participant stochiometry fields are null; full inspected response does not supply3:3 or6zinc. Source reference taxon559292, labelSaccharomyces cerevisiae, MW1000kDa and physical-interaction evidence remain scoped annotations. |
| septin-emdb-1712-wwpdb | https://files.wwpdb.org/pub/emdb/structures/EMD-1712/header/emd-1712.xml; Complete released EMD-1712 XML header: citation, specimen, composition, method/reconstruction | supports | Header records3Yta10+3Yta12 in a recombinant glutaraldehyde-cross-linked detergent preparation,5mMATP/10mMMgCl2,C6,12angstrom,0.5MDa. SupersedesEMD1543. No zinc count in this inspected header; source preparation is not universal physiology or resolved alternating identity. |
| septin-chebi-29105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29105; Complete exact native ChEBI identity, charge/formula/name and synonyms | supports | CHEBI29105 is active zinc(2+), formulaZn, charge+2. This verifies cofactor identity, not molecular copy count. |
| septin-panther-retry-SP140-members | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100; Complete returned twelve reviewed member identities and pagination | supports | PTHR46386 includes SP140 but also SP100,SP110,SP140L and AIRE proteins. Its display name does not make it exact to LYSp100B; no exhaustive claim about all possible family databases. |
| septin-dewulf-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC275422/fullTextXML; Actual HTTP/content diagnostic only | context_only | Initial guessed wrong-PMC route, not the De Wulf target identity; diagnostic only and excluded from target-paper access conclusions. |
| septin-biggins-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3730914/fullTextXML; Actual HTTP/content diagnostic only | context_only | Actual route status 500; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-zong-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC306587/fullTextXML; Actual HTTP/content diagnostic only | context_only | Actual route status 500; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-lee-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3039362/fullTextXML; Actual HTTP/content diagnostic only | context_only | Actual route status 500; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-emdb-1712 | https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-1712/header/emd-1712.xml; Actual HTTP/content diagnostic only | context_only | Transport connection refused before an HTTP response; no source header read through this route. The separate released wwPDB XML succeeded and is the inspected authority. |
| septin-panther-SP140 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR46386/; Actual HTTP/content diagnostic only | context_only | Actual route status 429; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-panther-SP140-members | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100; Actual HTTP/content diagnostic only | context_only | Actual route status 429; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-dewulf-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/; Actual HTTP/content diagnostic only | context_only | HTTP200 browser-check/proof-of-work page; not genuine paper text. A later genuine NCBI article is independently classified. |
| septin-dewulf-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC289150.1/PMC289150.1.xml; Actual HTTP/content diagnostic only | context_only | Actual route status 404; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-biggins-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC3730914/; Actual HTTP/content diagnostic only | context_only | HTTP200 browser-check/proof-of-work page; not genuine paper text. A later genuine NCBI article is independently classified. |
| septin-biggins-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC3730914.1/PMC3730914.1.xml; Actual HTTP/content diagnostic only | context_only | Actual route status 404; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-zong-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC306587/; Actual HTTP/content diagnostic only | context_only | HTTP200 browser-check/proof-of-work page; not genuine paper text. A later genuine NCBI article is independently classified. |
| septin-zong-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC306587.1/PMC306587.1.xml; Actual HTTP/content diagnostic only | context_only | Actual route status 404; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-lee-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC3039362/; Actual HTTP/content diagnostic only | context_only | HTTP200 browser-check/proof-of-work page; not genuine paper text. A later genuine NCBI article is independently classified. |
| septin-lee-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC3039362.1/PMC3039362.1.xml; Actual HTTP/content diagnostic only | context_only | Actual route status 404; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-emdb-1712-api | https://www.ebi.ac.uk/emdb/api/entry/EMD-1712; Actual HTTP/content diagnostic only | context_only | Successful duplicate native EMDB response retained for access provenance; biological conclusions use the fully read released XML header. |
| septin-dent-publisher | https://doi.org/10.1182/blood.V88.4.1423.bloodjournal8841423; Actual HTTP/content diagnostic only | context_only | Actual route status 403; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-dewulf-s3list | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC289150; Actual HTTP/content diagnostic only | context_only | Bounded exact S3 package-prefix listing, directory metadata only; no scientific body or absence of the paper is inferred. |
| septin-biggins-s3list | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC3730914; Actual HTTP/content diagnostic only | context_only | Bounded exact S3 package-prefix listing, directory metadata only; no scientific body or absence of the paper is inferred. |
| septin-zong-s3list | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC306587; Actual HTTP/content diagnostic only | context_only | Bounded exact S3 package-prefix listing, directory metadata only; no scientific body or absence of the paper is inferred. |
| septin-lee-s3list | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC3039362; Actual HTTP/content diagnostic only | context_only | Bounded exact S3 package-prefix listing, directory metadata only; no scientific body or absence of the paper is inferred. |
| septin-dewulf-corrected-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC289150/fullTextXML; Actual HTTP/content diagnostic only | context_only | Actual route status 500; failed/unusable body or family request retained as access context only. Successful alternative is separately evidenced. |
| septin-adapter-catalogue | https://imodulondb.org/api/organisms; Complete twenty organism rows and dataset keys; exact biological target/comparison-host scope | supports | No Saccharomyces/S288C/W303/YKO200, Homo, Mus/J558, Kluyveromyces or Chaetomium biological host appears. E. coli expression and bacterial structural-template context are not proxies. Host-matched downstream genes/modules are not applicable; catalogue noncoverage does not imply biological absence. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical runner attempt Nov3 00:49:00.848907Z–00:49:00.863225Z | context_only | PermissionError reading pyvenv.cfg, exit1. No fresh runner invocation. Current official-source fallback is separate. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-septin/original-checks.json; Actual three validate/render pairs and all39 original input occurrences | supports | All three original native validations/renderings exit0 and exact Markdown matches. All39 historical input occurrences match exact Git objects; current kinetochore and mAAA targets changed and are substantively reassessed here. |
| septin-maaa-independent-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/maaa-count-source-challenge.json; Separate independent narrow frozen-record/CPX/EMDB source-count challenge | context_only | Corroborates only the bounded minor attribution/scope correction: CPX unspecified; EMDB preparation3:3; no six-zinc count in either inspected source. No Luo/pixel assessment claimed by challenger. |
| septin-record-kinetochore | data/structures/other/kinetochore.yaml; Complete current record: all fields, examples, graph, source annotations, discussion and history | supports | Independently read at sourcef9ac707415c382929b15517997efaa11ec96230d. Stale versus original frozen record: True; new content reassessed without editing record. |
| septin-original-kinetochore | reviews/structured/20261022T080129Z-kinetochore-audit/review.yaml; Entire immutable original YAML and derived Markdown: evidence scopes, checks, findings/actions, notes/limitations | supports | Original20261022T080129Z-kinetochore-audit: 1 inherited findings. Historical batch26 executions remain accurately scoped historical provenance, not current PR2395 checks. |
| septin-native-kinetochore-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-verify-receipt.json; Actual command receipt JSON (snapshot_sha256 binds this referenced receipt); full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-verify.log. Receipt stdout_sha256 and summary bind the separate log bytes. | supports | Thirteen reviewed S288C examples; one typed Cse4 node COVERED. Native coverage validates representative identity but does not resolve whole-nucleosome grounding/actor type or prove full kinetochore formation. Exit0. ReceiptSHA 57360d96f2b6d5364827d01aceafda21a528ad28834560a54f5a91091024e9cc; logSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-kinetochore-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-causal-receipt.json; Actual command receipt JSON (snapshot_sha256 binds this referenced receipt); full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-causal.log. Receipt stdout_sha256 and summary bind the separate log bytes. | supports | Thirteen reviewed S288C examples; one typed Cse4 node COVERED. Native coverage validates representative identity but does not resolve whole-nucleosome grounding/actor type or prove full kinetochore formation. Exit0. ReceiptSHA 0d49b799c6b96ed0356d80ef3d79fac875fd7eb80f4adff44d00c0484222b0c1; logSHA e93a54ceaf84c96a94b14c1179fd71a25c8c1b23785781886fab6aa93aa540b3. |
| septin-record-lysp100_associated_nuclear_domain | data/structures/other/lysp100_associated_nuclear_domain.yaml; Complete current record: all fields, examples, graph, source annotations, discussion and history | supports | Independently read at sourcef9ac707415c382929b15517997efaa11ec96230d. Stale versus original frozen record: False; new content reassessed without editing record. |
| septin-original-lysp100_associated_nuclear_domain | reviews/structured/20261022T080132Z-lysp100-associated-nuclear-domain-audit/review.yaml; Entire immutable original YAML and derived Markdown: evidence scopes, checks, findings/actions, notes/limitations | supports | Original20261022T080132Z-lysp100-associated-nuclear-domain-audit: 0 inherited findings. Historical batch26 executions remain accurately scoped historical provenance, not current PR2395 checks. |
| septin-native-lysp100_associated_nuclear_domain-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-verify-receipt.json; Actual command receipt JSON (snapshot_sha256 binds this referenced receipt); full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-verify.log. Receipt stdout_sha256 and summary bind the separate log bytes. | supports | One reviewed human SP140 example; one COVERED SP140 node and one UNANCHORED_WITH_UNIPROT external Bright/ARID3A Q99856. The external regulator is intentionally not a stable constituent; no missing optional inventory defect. Exit0. ReceiptSHA edc46e06cd5b7bd9743f9d544797bb7edf8b648707eb5b221047c39fb0802776; logSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-lysp100_associated_nuclear_domain-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-causal-receipt.json; Actual command receipt JSON (snapshot_sha256 binds this referenced receipt); full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-causal.log. Receipt stdout_sha256 and summary bind the separate log bytes. | supports | One reviewed human SP140 example; one COVERED SP140 node and one UNANCHORED_WITH_UNIPROT external Bright/ARID3A Q99856. The external regulator is intentionally not a stable constituent; no missing optional inventory defect. Exit0. ReceiptSHA 874926f4a10dad6cbe7511ce3604fa5471a1d1208bd303463da78d45eb2e7b50; logSHA 03c648141dc26b94acdd7b083c185da463446f71a47c54aa27026991ce67e399. |
| septin-record-m_aaa_complex | data/structures/other/m_aaa_complex.yaml; Complete current record: all fields, examples, graph, source annotations, discussion and history | supports | Independently read at sourcef9ac707415c382929b15517997efaa11ec96230d. Stale versus original frozen record: True; new content reassessed without editing record. |
| septin-original-m_aaa_complex | reviews/structured/20261022T080133Z-m-aaa-complex-audit/review.yaml; Entire immutable original YAML and derived Markdown: evidence scopes, checks, findings/actions, notes/limitations | supports | Original20261022T080133Z-m-aaa-complex-audit: 0 inherited findings. Historical batch26 executions remain accurately scoped historical provenance, not current PR2395 checks. |
| septin-native-m_aaa_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-verify-receipt.json; Actual command receipt JSON (snapshot_sha256 binds this referenced receipt); full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-verify.log. Receipt stdout_sha256 and summary bind the separate log bytes. | supports | Two reviewed S288C examples and two COVERED typed protein nodes. Native validation does not certify newly asserted source counts, experimental W303 identity or formation necessity. Exit0. ReceiptSHA 03270ace4152075782b38ee838b82f2afb83eec6431225cd9123c0e75db78172; logSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-m_aaa_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-causal-receipt.json; Actual command receipt JSON (snapshot_sha256 binds this referenced receipt); full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-causal.log. Receipt stdout_sha256 and summary bind the separate log bytes. | supports | Two reviewed S288C examples and two COVERED typed protein nodes. Native validation does not certify newly asserted source counts, experimental W303 identity or formation necessity. Exit0. ReceiptSHA d2bccb1480f46709ab93317cc58519183a51ed6e5781ae1d995c598818081e17; logSHA 03c66b2285794a12d4db1589391c5232e529f502abc044e157faada8cf19e46a. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech check passed: all 10 links resolve with matching labels against the 1130-trait source index. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | All 22 governed artifacts match the pinned CLAW revision. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified all 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2395 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-isw1_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-isw1_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-isw1a_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-isw1a_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-isw1b_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-isw1b_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-kinetochore-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-kinetochore-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ku70_ku80_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ku70_ku80_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-lipopolysaccharide_transport_system-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-lipopolysaccharide_transport_system-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-lolcde_lipoprotein_abc_transporter_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-lolcde_lipoprotein_abc_transporter_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-lysp100_associated_nuclear_domain-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-lysp100_associated_nuclear_domain-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-m_aaa_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-m_aaa_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-macab_tolc_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-macab_tolc_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Assigned science scope is four complete unchanged records at cohort indices0,1,2,4. Thirty maintained inputs are17 common frozen rules/config/schema/scripts, four targets, eight original artifacts and the frozen m-AAA record used solely in a separate auxiliary source-count challenge. All47 frozen inputs and20 originals are hash-audited in finalization.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Fresh genuine Vary2003 main Methods sec2–11, Results sec13–20, Discussion sec21, Table1 and Figures1–5 text captions were read. Introduction, Table2 sequence appendix, figure pixels, raw microarrays and external data were not read. Reciprocal recovery supports stable assemblies under tested conditions, not universal exclusivity or universal formation essentiality.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Vary uses W303-derived RAD5-repaired strains and assay-specific recombinant nucleosome/DNA substrates. S288C UniProt examples are references, not experimentally substituted strains. Quantitative sliding/spacing differences are not universal in-vivo rates.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Koike2002 is a secondary review; fresh PDF pp223–227 plus the dimerization conclusion at the start of p228, Table1 and Figure1 caption read; partial later p228 localization text is not used, no pixels or later pages. Boulton primary abstracts were read both through MED and genuine PMC abstract/PDF landings, not main bodies. Feldmann and Laroche are complete indexed abstracts only. Downs2004 is bibliographic metadata without indexed abstract, plus DOI Crossref metadata, not a read review body.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Current exact six reviewed gene/taxon queries each return one expected S288C accession with no next page. This verifies bounded present joins, not historical query execution. Native annotation citations and real primary experiments remain different tiers.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Exact family candidates were checked for type, scope, native descriptions/signatures and positive protein xrefs. Successful Isw1/Ioc candidates are domain-level or broad; no exhaustive family absence or independent sequence alignment is claimed. Three initial InterPro429 responses and failed primary routes are retained as validation only; successful retries are separately timestamped.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: The complete official catalogue has20 organism rows/28 organism-dataset pairs and no Saccharomyces. No unmatched yeast proxy or gene/module query is used. E.coli packets were fetched for sibling reviewers but are not scientific evidence for these yeast targets. Historical runner unavailability remains the actual Nov3 00:49Z receipt, never a fresh execution.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Eight actual current native protein commands pass for nine maintained example occurrences and nine COVERED typed nodes:2/2/3/2. Coverage is not independent biological evidence. Eight original validate/render commands and61 historical input occurrences pass. Root corpus/publication/successor/final-head/CI/queue gates remain separate, not precertified.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Own original applicability defects are three formal unsupported exclusions plus one complete Ku applicability omission. Twenty-three historical access-only kind occurrences are corrected without rewriting original observations or claiming that the original authors falsely read bodies. No own stale targets or record edits.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Four inherited findings remain open at minor severity; original Isw1 F1 major is explicitly narrowed with a normalization reason and tracked bundle correction. Exact inherited lineages are preserved; no family/domain/type-only or missing-optional-example finding is introduced. Generic class allowance and actual within-row scope are evaluated separately. Source-neutral class grounding does not follow merely from species examples.
- Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Separate immutable m-AAA auxiliary reads the full frozen record, CPX response and EMD1712 XML only. It is a narrow source-count attribution challenge, not an additional assigned finding, complete m-AAA science review, Luo body read or image/map inspection.
- LPS transport, LolCDE and MacAB-TolC independent review: Only assigned indices5,6,9 receive a complete scientific review here; separate Isw1 auxiliary receipt is not merged into these findings. All maintained inputs used are frozen and listed.
- LPS transport, LolCDE and MacAB-TolC independent review: Fresh public snapshots retain their actual UTC timestamps and SHA256. Yakushi2000 full body was inaccessible, but complete native abstract and public captions1,3,4,7 were read. No figure pixels, raw coordinates/maps, supplemental data or uninspected paper bodies are certified.
- LPS transport, LolCDE and MacAB-TolC independent review: Older family prose, source metadata and computational annotations are not elevated into direct experimental proof. Secondary abstracts are authority/partial, metadata-only rows database/context_only and failed routes validation/context_only.
- LPS transport, LolCDE and MacAB-TolC independent review: Native protein success validates reference identity/xrefs and diagnostic coverage, not scientific participation, exact family scope or formation necessity. LolCDE substrate UNANCHORED_WITH_UNIPROT is not automatically a missing constituent.
- LPS transport, LolCDE and MacAB-TolC independent review: The historical structured-adapter runner failure at 2026-11-03 around00:49Z remains historical; no fresh runner invocation or success is claimed. Current official API fallback, exact genes and full membership joins were independently inspected.
- LPS transport, LolCDE and MacAB-TolC independent review: precise1k is a five-strain computational expression dataset, not an exact substitute for every strain/construct in the experiments. Generated ai_summary text is excluded. Zero threshold flags do not show biological absence and module membership does not establish assembly/localization/transport.
- LPS transport, LolCDE and MacAB-TolC independent review: Repository/Git/GitHub and original bundles were not mutated. Root owns deduplication, issue publication, global gates and later save/CI/queue; this source report does not certify pending stages.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Only the three assigned records are scientifically re-reviewed. All39 original historical input occurrences match and all three native original pairs validate/render exactly. Kinetochore and mAAA are stale, LYSP is unchanged; two substantive refreshes are explicit.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Current De Wulf/Westermann main-text sections and relevant embedded captions support kinetochore assembly scope; no supplements or figure pixels were inspected. Biggins is explicitly secondary synthesis, not new primary evidence. The CSE4 representative is valid but does not ground the whole nucleosome class.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Ancillary reference papers, including Schmitzberger2017 Kluyveromyces COMA, are limited to complete native abstracts. S288C reference accessions do not establish experimental strain; De Wulf is W303-congenic and Westermann strain supplement was not opened.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Zong genuine main text and listed captions were read. Dent publisher403 means Dent remains complete-primary-abstract scope; Bloch/Gong are likewise abstract-tier. No source figure pixels or raw experiments were assessed for LANDs; ectopic J558/HeLa results do not establish all endogenous isoforms, human prevalence or universal body formation.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Lee genuine main body became available through the alternate NCBI route; this does not retroactively invalidate the historical failed-access rationale. No Lee supplement, raw density map, atomistic reanalysis or image pixels were inspected. Header3:3 preparation and current CPX null counts remain distinct.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Luo genuine source sections and actual external Fig4 panelsA–D were inspected; no other pixels, supplementary/source-data files, coordinates or raw experimental images were analyzed. Reporter endpoint, separate growth response, engineered domains and species/preparation limits are retained. Link-only CC BY-NC-ND4.0 attribution is preserved.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: InterPro/PANTHER candidate checks are bounded to named entries and their reviewed members; no exhaustive family absence claim. Unchecked machine-generated IPR050928 prose is excluded. Shared families/domains are not forced onto narrower paralog/isoform classes.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Complete fresh official catalogue lacks all relevant yeast/human/mouse/fungal biological hosts; recombinant expression/template organisms are not proxies. Downstream unmatched-dataset queries are not applicable. Historical runner PermissionError retains Nov3 00:49 time; no fresh invocation or biology-absence inference.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: Six actual native protein commands pass:16 reviewed constituent examples and5typed nodes,4COVERED plus external Bright1UNANCHORED_WITH_UNIPROT. Coverage is reference validation, not class-grounding, source-count, assembly or necessity certification.
- Kinetochore, LYSP100-associated domain and m-AAA independent review: All failed/challenged or wrong-initial-route responses remain diagnostics; HTTP200 alone does not establish paper text. Successful alternates have independent actual times and hashes. No records, original bundles, Git refs or GitHub content were mutated; root-owned fullQC, later saved-head checks/CI/queue/merge are not certified here.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun. Its retained November3 PermissionError receipt is historical; current catalogue coverage is assessed directly, and fresh or reused responses retain their actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- Three changed targets require substantive current-input reassessment; seven other current target hashes match original frozen inputs. All used maintained context is frozen before synthesis.
- Twenty current native protein commands passed across 38 represented protein examples and 28 typed GENE_OR_PROTEIN nodes: 26 COVERED and two UNANCHORED_WITH_UNIPROT (LolCDE substrate and LYSP100 Bright/ARID3A). External machinery and substrates are not forced into constituent rows. Identity and coverage are not experimental membership or necessity evidence.
- Original observations and dated rationale remain immutable. Source bodies, abstracts, database entries and failed-access diagnostics retain exact scopes and dates.
- Root synthesis explicitly corrects six native evidence snapshot/reference bindings identified during integration: the snapshot hashes now identify the referenced receipt JSON; each locator and summary preserve the separately verified stdout path/hash. Immutable independent source reports, executed checks and scientific results are unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T133713Z-pr2395-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2395: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T13:16:07.533152Z'
finished_at: '2026-11-04T13:37:13Z'
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
summary: 'Independent whole-record reassessment of ten current records retains ten
  inherited scientific findings and establishes one new minor m-AAA source-count finding:
  eleven minor findings across seven records needing curation. The inherited Isw1
  major finding is explicitly narrowed to a minor class/variant scope inconsistency
  with bounded action. Isw1a, Isw1b and LYSP100-associated nuclear domain pass with
  limitations. Three stale reviews are substantively refreshed; seven current targets
  match their original frozen bytes. The immutable successor corrects ten applicability
  assessments, 23 historical access-only evidence occurrences and six native receipt/hash
  bindings, preserving all original artifacts and access boundaries. Every scientific
  action is linked to a separate open record-curation issue; no records are edited.'
source:
  git_revision: f9ac707415c382929b15517997efaa11ec96230d
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
  - path: data/structures/other/isw1_complex.yaml
    sha256: 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912
    role: target
  - path: data/structures/other/isw1a_complex.yaml
    sha256: 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865
    role: target
  - path: data/structures/other/isw1b_complex.yaml
    sha256: da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137
    role: target
  - path: data/structures/other/kinetochore.yaml
    sha256: ea8645dec5b13874441be4fa7a2db0b477265d3c23ecd399aa9559824428640d
    role: target
  - path: data/structures/other/ku70_ku80_complex.yaml
    sha256: 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44
    role: target
  - path: data/structures/other/lipopolysaccharide_transport_system.yaml
    sha256: 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e
    role: target
  - path: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
    sha256: 96bf1ce75ce606af29c2d8a549c345e9487f0e426ac1f86823f14db22c651866
    role: target
  - path: data/structures/other/lysp100_associated_nuclear_domain.yaml
    sha256: 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493
    role: target
  - path: data/structures/other/m_aaa_complex.yaml
    sha256: 9686eb96f5b95da3c8b9dbb002841e31ac5c884c66e4af52f05706b375ea87a7
    role: target
  - path: data/structures/other/macab_tolc_complex.yaml
    sha256: b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636
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
  - path: reviews/structured/20261022T080127Z-isw1-complex-audit/review.md
    sha256: e109ba65099f29805f79f5e73999a09972d351156ae4dbf4447abc2d3c16c3c2
    role: context
  - path: reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml
    sha256: 9acdb77d73b67e676b09e489f69d11accd7e5097d79aeee7df506b1e38097d7c
    role: context
  - path: reviews/structured/20261022T080128Z-isw1a-complex-audit/review.md
    sha256: 958e9df6b5c198e195fd713517a4b3d473e9340c9e6bbbf33f7c7dc5ce332f6c
    role: context
  - path: reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml
    sha256: 11a7087b4b9ceddaabf4cfb426f1380a5a8012cb155d54ca310258132fb17c4f
    role: context
  - path: reviews/structured/20261022T080128Z-isw1b-complex-audit/review.md
    sha256: c0aa8b7c0f1bf6b1cda56c8a805036269793ef8acf58e008437b26150cfa56b4
    role: context
  - path: reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml
    sha256: 4183282a7718a6f641674d7a9c91ecfc223b99c73bdff509c9978a6253e84b5d
    role: context
  - path: reviews/structured/20261022T080129Z-kinetochore-audit/review.md
    sha256: e76ccc32d0a9552eb3957d4d6a5d194ea98a5bf18c3d14b35a648edebfe87874
    role: context
  - path: reviews/structured/20261022T080129Z-kinetochore-audit/review.yaml
    sha256: 54c19f806698dec91e445973dc9037e2fd23c8f44685683db50a6539c5eac083
    role: context
  - path: reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.md
    sha256: 3e2398b97a626a2e54d9579abd02c06dbc838d110e679fa44d37d0ff61b19c59
    role: context
  - path: reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml
    sha256: 599877808fbf65125c153255d03500c2ea571d6412e90423e84110b2bf214fcc
    role: context
  - path: reviews/structured/20261022T080130Z-lipopolysaccharide-transport-system-audit/review.md
    sha256: cf36b160425fba346a23318911db6820eb4a0cb54e7c3b56f4488a3f8f9544b2
    role: context
  - path: reviews/structured/20261022T080130Z-lipopolysaccharide-transport-system-audit/review.yaml
    sha256: a9cd71fe7c4f253a769cf31d55cc615adcdbc1c1fb0547b2ea481d58009b2ef3
    role: context
  - path: reviews/structured/20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit/review.md
    sha256: 4cb08f9f2c4ba451f6150f7f969935856e39f8c3b1d5534f415ae910b6bf4de6
    role: context
  - path: reviews/structured/20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit/review.yaml
    sha256: 69c90d2c80fcf3825f88c8f33616374e1abb58414ba0ba2ba3ce9edfd04cba0c
    role: context
  - path: reviews/structured/20261022T080132Z-lysp100-associated-nuclear-domain-audit/review.md
    sha256: 70b9f914589c90c5040d9dca6daae86c92dcf79f1473c715682a3709ef1d2d44
    role: context
  - path: reviews/structured/20261022T080132Z-lysp100-associated-nuclear-domain-audit/review.yaml
    sha256: 07a59eacac81ab2cefb303de28cdc2617de403a1c9ec1b35ed9136b44971dc5b
    role: context
  - path: reviews/structured/20261022T080133Z-m-aaa-complex-audit/review.md
    sha256: 8637944959c74f867707b6dc4316ccb67ea0ba47be6dcbd42621bc5a0db8b034
    role: context
  - path: reviews/structured/20261022T080133Z-m-aaa-complex-audit/review.yaml
    sha256: 22517eca0c698f0befc2c2d854f086f6873d11853fcb4b62bb783b8c036adcc8
    role: context
  - path: reviews/structured/20261022T080133Z-macab-tolc-complex-audit/review.md
    sha256: 7f5d5bee568eef5feb40aae5cdc0e459d0089a9aceaf0c8add530e389b0d2cb6
    role: context
  - path: reviews/structured/20261022T080133Z-macab-tolc-complex-audit/review.yaml
    sha256: c50a5725d852f71a2553749170a3cbef86efa47120cb9a3d27a43b9eb3c6ac88
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
- target_id: GO:0016587
  path: data/structures/other/isw1_complex.yaml
  label: Isw1 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
- target_id: GO:0036436
  path: data/structures/other/isw1a_complex.yaml
  label: Isw1a complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1a_complex.yaml
    role: maintained scientific record
- target_id: GO:0036437
  path: data/structures/other/isw1b_complex.yaml
  label: Isw1b complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1b_complex.yaml
    role: maintained scientific record
- target_id: GO:0000776
  path: data/structures/other/kinetochore.yaml
  label: kinetochore
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/kinetochore.yaml
    role: maintained scientific record
- target_id: GO:0043564
  path: data/structures/other/ku70_ku80_complex.yaml
  label: Ku70:Ku80 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ku70_ku80_complex.yaml
    role: maintained scientific record
- target_id: GO:0062051
  path: data/structures/other/lipopolysaccharide_transport_system.yaml
  label: lipopolysaccharide transport system
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lipopolysaccharide_transport_system.yaml
    role: maintained scientific record
- target_id: cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  path: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
  label: LolCDE lipoprotein ABC transporter complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
    role: maintained scientific record
- target_id: GO:0016606
  path: data/structures/other/lysp100_associated_nuclear_domain.yaml
  label: LYSP100-associated nuclear domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lysp100_associated_nuclear_domain.yaml
    role: maintained scientific record
- target_id: GO:0005745
  path: data/structures/other/m_aaa_complex.yaml
  label: m-AAA complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/m_aaa_complex.yaml
    role: maintained scientific record
- target_id: GO:1990196
  path: data/structures/other/macab_tolc_complex.yaml
  label: MacAB-TolC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/macab_tolc_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main b508909649f4f7b0b2f11ea4d3ee5a45f09081fd.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    95ad1b68018d096f0e86328b39d87b6c288e5790.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head f9ac707415c382929b15517997efaa11ec96230d.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head f9ac707415c382929b15517997efaa11ec96230d.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Native TraitMech check passed: all 10 links resolve with matching labels
    against the 1130-trait source index.'
  scope_note: Actual local execution at main-merge head f9ac707415c382929b15517997efaa11ec96230d.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  command: just vendored-check
  exit_code: 0
  summary: All 22 governed artifacts match the pinned CLAW revision.
  scope_note: Actual local execution at main-merge head f9ac707415c382929b15517997efaa11ec96230d.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    all 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head f9ac707415c382929b15517997efaa11ec96230d.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0016587
  status: passed
  required: true
  target_ids:
  - GO:0016587
  command: just validate data/structures/other/isw1_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0016587
  status: passed
  required: true
  target_ids:
  - GO:0016587
  command: just validate-strict data/structures/other/isw1_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0036436
  status: passed
  required: true
  target_ids:
  - GO:0036436
  command: just validate data/structures/other/isw1a_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0036436
  status: passed
  required: true
  target_ids:
  - GO:0036436
  command: just validate-strict data/structures/other/isw1a_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0036437
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just validate data/structures/other/isw1b_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0036437
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: just validate-strict data/structures/other/isw1b_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0000776
  status: passed
  required: true
  target_ids:
  - GO:0000776
  command: just validate data/structures/other/kinetochore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0000776
  status: passed
  required: true
  target_ids:
  - GO:0000776
  command: just validate-strict data/structures/other/kinetochore.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0043564
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just validate data/structures/other/ku70_ku80_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0043564
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just validate-strict data/structures/other/ku70_ku80_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0062051
  status: passed
  required: true
  target_ids:
  - GO:0062051
  command: just validate data/structures/other/lipopolysaccharide_transport_system.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0062051
  status: passed
  required: true
  target_ids:
  - GO:0062051
  command: just validate-strict data/structures/other/lipopolysaccharide_transport_system.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  command: just validate data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  command: just validate-strict data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0016606
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: just validate data/structures/other/lysp100_associated_nuclear_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0016606
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: just validate-strict data/structures/other/lysp100_associated_nuclear_domain.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0005745
  status: passed
  required: true
  target_ids:
  - GO:0005745
  command: just validate data/structures/other/m_aaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0005745
  status: passed
  required: true
  target_ids:
  - GO:0005745
  command: just validate-strict data/structures/other/m_aaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:1990196
  status: passed
  required: true
  target_ids:
  - GO:1990196
  command: just validate data/structures/other/macab_tolc_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:1990196
  status: passed
  required: true
  target_ids:
  - GO:1990196
  command: just validate-strict data/structures/other/macab_tolc_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395
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
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  summary: All ten positive molecular narratives trigger structured-source applicability.
    The complete fresh official catalogue has 20 organism rows and 28 organism/dataset
    pairs, without the relevant yeast, human or mouse biological hosts; recombinant
    hosts are not proxies. For the three E. coli transport records, exact e_coli/precise1k
    joins cover 15 loci and their complete 201-module membership tables. lptA/lptB/lptC/tolC
    join module22 (SoxS), lpp module45 (Resistance), and lptF module167 (UC-2); the
    other nine loci have zero thresholded flags. Full module member tables contain
    117, 58 and 96 genes. The five-strain expression dataset is not an exact experimental-strain
    match, physical-assembly evidence or evidence of biological absence. Generated
    summaries are excluded. Historical runner PermissionError retains its actual November3
    timestamp; fresh native packets have their own access times.
  evidence_ids:
  - micro-adapter-catalogue
  - plaque-adapter-module-22
  - plaque-adapter-module-22-genes
  - plaque-adapter-module-45
  - plaque-adapter-module-45-genes
  - plaque-adapter-module-167
  - plaque-adapter-module-167-genes
  - plaque-adapter-b0054
  - plaque-adapter-b0054-modules
  - plaque-adapter-b0641
  - plaque-adapter-b0641-modules
  - plaque-adapter-b0741
  - plaque-adapter-b0741-modules
  - plaque-adapter-b0878
  - plaque-adapter-b0878-modules
  - plaque-adapter-b0879
  - plaque-adapter-b0879-modules
  - plaque-adapter-b1116
  - plaque-adapter-b1116-modules
  - plaque-adapter-b1117
  - plaque-adapter-b1117-modules
  - plaque-adapter-b1118
  - plaque-adapter-b1118-modules
  - plaque-adapter-b1677
  - plaque-adapter-b1677-modules
  - plaque-adapter-b3035
  - plaque-adapter-b3035-modules
  - plaque-adapter-b3199
  - plaque-adapter-b3199-modules
  - plaque-adapter-b3200
  - plaque-adapter-b3200-modules
  - plaque-adapter-b3201
  - plaque-adapter-b3201-modules
  - plaque-adapter-b4261
  - plaque-adapter-b4261-modules
  - plaque-adapter-b4262
  - plaque-adapter-b4262-modules
  - plaque-adapter-catalogue
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
  - plaque-adapter-precise1k-modules
  - septin-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-graph-policy
  - micro-native-policy
  - micro-native-config
  - micro-protein-P38144
  - micro-protein-P43596
  - micro-protein-Q12072
  - micro-protein-Q04213
  - micro-protein-P32807
  - micro-protein-Q04437
  - micro-tax-4932
  - micro-tax-559292
  - micro-go-0006303
  - micro-go-0006338
  - micro-go-0016587
  - micro-go-0031010
  - micro-go-0036436
  - micro-go-0036437
  - micro-go-0043564
  - micro-go-0045027
  - micro-go-0140513
  - micro-ancestors-0016587
  - micro-ancestors-0036436
  - micro-ancestors-0036437
  - micro-ancestors-0043564
  - micro-family-IPR006165
  - micro-family-IPR024193
  - micro-family-IPR006164
  - micro-family-IPR044754
  - micro-family-IPR038718
  - micro-family-IPR035503
  - micro-family-IPR062587
  - micro-family-IPR028942-retry
  - micro-family-IPR062429-retry
  - micro-family-IPR063422-retry
  - micro-pmid-12482963
  - micro-pmid-12518983
  - micro-pmid-14562095
  - micro-pmid-15122350
  - micro-pmid-8890183
  - micro-pmid-8910371
  - micro-pmid-8972848
  - micro-pmid-9635192
  - micro-vary2003-html
  - micro-koike2002-pdf
  - micro-boulton70-html
  - micro-boulton80-html
  - micro-downs2004-doi
  - plaque-native-policy
  - plaque-native-schema
  - plaque-PMC2851745-legacy
  - plaque-PMC3038725-legacy
  - plaque-adapter-module-22
  - plaque-adapter-module-22-genes
  - plaque-adapter-module-45
  - plaque-adapter-module-45-genes
  - plaque-adapter-module-167
  - plaque-adapter-module-167-genes
  - plaque-yakushi2000-canonical
  - plaque-go-0062051-ancestors
  - plaque-go-1990196-ancestors
  - plaque-protein-P0ADV1
  - plaque-protein-P0A9V1
  - plaque-protein-P0ADV9
  - plaque-protein-P31554
  - plaque-protein-P0ADC1
  - plaque-protein-P0AF98
  - plaque-protein-P0ADC6
  - plaque-protein-P0ADC3
  - plaque-protein-P75957
  - plaque-protein-P75958
  - plaque-protein-P69776
  - plaque-protein-P0A912
  - plaque-protein-P75830
  - plaque-protein-P75831
  - plaque-protein-P02930
  - plaque-family-IPR014340
  - plaque-family-IPR030921
  - plaque-family-IPR026265
  - plaque-family-IPR020889
  - plaque-family-IPR007485
  - plaque-family-IPR030922
  - plaque-family-IPR030923
  - plaque-family-IPR011924
  - plaque-family-IPR011925
  - plaque-family-IPR015854
  - plaque-family-IPR058623
  - plaque-family-IPR050250
  - plaque-family-IPR058622
  - plaque-family-NF008076
  - plaque-family-NF008357
  - plaque-go-0062051
  - plaque-go-1990351
  - plaque-go-0043190
  - plaque-go-0140306
  - plaque-go-0044874
  - plaque-go-1990196
  - plaque-go-1990195
  - plaque-go-0008559
  - plaque-tax-2
  - plaque-tax-562
  - plaque-tax-83333
  - plaque-cpx-4262
  - plaque-pdb-7MDY
  - plaque-pdb-7MDY-assembly1
  - plaque-pdb-7MDY-entity1
  - plaque-pdb-7MDY-entity2
  - plaque-pdb-7MDY-entity3
  - plaque-pdb-5NIK
  - plaque-pdb-5NIK-assembly1
  - plaque-pdb-5NIK-entity1
  - plaque-pdb-5NIK-entity2
  - plaque-pdb-5NIK-entity3
  - plaque-PMC5858563-jats
  - plaque-PMC3552488-jats
  - plaque-PMC2880507-jats
  - plaque-PMC8333309-jats
  - plaque-PMC5447821-jats
  - plaque-PMC2613632-jats
  - plaque-pmid-10783239
  - plaque-pmid-18634750
  - plaque-pmid-34344901
  - plaque-pmid-18955484
  - plaque-pmid-28504659
  - plaque-pmid-12207697
  - plaque-pmid-12724388
  - plaque-pmid-16079137
  - plaque-pmid-17056748
  - plaque-pmid-18424520
  - plaque-pmid-18480051
  - plaque-pmid-20720015
  - plaque-pmid-21257904
  - plaque-pmid-3316191
  - plaque-pmid-19500581
  - plaque-pmid-22668317
  - plaque-pmid-16861298
  - plaque-pmid-18375759
  - plaque-pmid-28878019
  - plaque-pmid-25257218
  - plaque-pmid-18805970
  - plaque-pmid-11544226
  - plaque-yakushi2000-figure1
  - plaque-yakushi2000-figure3
  - plaque-yakushi2000-figure4
  - plaque-yakushi2000-figure7
  - plaque-adapter-catalogue
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-modules
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-up-P38313
  - septin-up-P47149
  - septin-up-Q02732
  - septin-up-Q04477
  - septin-up-P40568
  - septin-up-Q12143
  - septin-up-Q06675
  - septin-up-P36012
  - septin-up-P33895
  - septin-up-P39731
  - septin-up-P40460
  - septin-up-P53298
  - septin-up-P40014
  - septin-tax-4932
  - septin-tax-559292
  - septin-pmid-14581449
  - septin-pmid-14581449-abstract
  - septin-pmid-11179222
  - septin-pmid-11179222-abstract
  - septin-pmid-10323865
  - septin-pmid-10323865-abstract
  - septin-pmid-12455957
  - septin-pmid-12455957-abstract
  - septin-pmid-14602074
  - septin-pmid-14602074-abstract
  - septin-pmid-11266451
  - septin-pmid-11266451-abstract
  - septin-pmid-29046335
  - septin-pmid-29046335-abstract
  - septin-pmid-14657030
  - septin-pmid-14657030-abstract
  - septin-pmid-14562095
  - septin-pmid-14562095-abstract
  - septin-pmid-11952896
  - septin-pmid-11952896-abstract
  - septin-up-Q13342
  - septin-up-Q99856
  - septin-tax-9606
  - septin-pmid-8910577
  - septin-pmid-8910577-abstract
  - septin-pmid-8695863
  - septin-pmid-8695863-abstract
  - septin-pmid-25593309
  - septin-pmid-25593309-abstract
  - septin-up-P39925
  - septin-up-P40341
  - septin-pmid-7929327
  - septin-pmid-7929327-abstract
  - septin-pmid-21147776
  - septin-pmid-21147776-abstract
  - septin-pmid-8681382
  - septin-pmid-8681382-abstract
  - septin-go
  - septin-go-0000776-ancestors
  - septin-go-0016606-ancestors
  - septin-go-0005745-ancestors
  - septin-go-cenpa
  - septin-westermann-metadata
  - septin-westermann-metadata-abstract
  - septin-dewulf-metadata
  - septin-dewulf-metadata-abstract
  - septin-biggins-metadata
  - septin-biggins-metadata-abstract
  - septin-zong-metadata
  - septin-zong-metadata-abstract
  - septin-luo-metadata
  - septin-luo-metadata-abstract
  - septin-lee-metadata
  - septin-lee-metadata-abstract
  - septin-ipr-IPR043563
  - septin-ipr-IPR030411
  - septin-ipr-IPR050928
  - septin-ipr-IPR005936
  - septin-ipr-retry-IPR011546
  - septin-panther-retry-SP140
  - septin-westermann-xml
  - septin-dewulf-ncbi
  - septin-biggins-ncbi
  - septin-zong-ncbi
  - septin-lee-ncbi
  - septin-luo-xml
  - septin-luo-fig4
  - septin-cpx-1654
  - septin-emdb-1712-wwpdb
  - septin-chebi-29105
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
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
- check_id: isw1_complex-uniprot-verify
  name: Native Isw1 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0016587
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-isw1_complex-uniprot-verify
- check_id: isw1_complex-uniprot-causal
  name: Native Isw1 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0016587
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-isw1_complex-uniprot-causal
- check_id: isw1a_complex-uniprot-verify
  name: Native Isw1a complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036436
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1a_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-isw1a_complex-uniprot-verify
- check_id: isw1a_complex-uniprot-causal
  name: Native Isw1a complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036436
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1a_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-isw1a_complex-uniprot-causal
- check_id: isw1b_complex-uniprot-verify
  name: Native Isw1b complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-isw1b_complex-uniprot-verify
- check_id: isw1b_complex-uniprot-causal
  name: Native Isw1b complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0036437
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-isw1b_complex-uniprot-causal
- check_id: kinetochore-uniprot-verify
  name: Native kinetochore UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000776
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/kinetochore.yaml
    --verify
  exit_code: 0
  summary: 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-kinetochore-uniprot-verify
- check_id: kinetochore-uniprot-causal
  name: Native kinetochore UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000776
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/kinetochore.yaml
    --causal-graphs
  exit_code: 0
  summary: 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-kinetochore-uniprot-causal
- check_id: ku70_ku80_complex-uniprot-verify
  name: Native Ku70:Ku80 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ku70_ku80_complex-uniprot-verify
- check_id: ku70_ku80_complex-uniprot-causal
  name: Native Ku70:Ku80 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ku70_ku80_complex-uniprot-causal
- check_id: lipopolysaccharide_transport_system-uniprot-verify
  name: Native lipopolysaccharide transport system UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0062051
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/lipopolysaccharide_transport_system.yaml
    --verify
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-lipopolysaccharide_transport_system-uniprot-verify
- check_id: lipopolysaccharide_transport_system-uniprot-causal
  name: Native lipopolysaccharide transport system UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0062051
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/lipopolysaccharide_transport_system.yaml
    --causal-graphs
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-lipopolysaccharide_transport_system-uniprot-causal
- check_id: lolcde_lipoprotein_abc_transporter_complex-uniprot-verify
  name: Native LolCDE lipoprotein ABC transporter complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-lolcde_lipoprotein_abc_transporter_complex-uniprot-verify
- check_id: lolcde_lipoprotein_abc_transporter_complex-uniprot-causal
  name: Native LolCDE lipoprotein ABC transporter complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-lolcde_lipoprotein_abc_transporter_complex-uniprot-causal
- check_id: lysp100_associated_nuclear_domain-uniprot-verify
  name: Native LYSP100-associated nuclear domain UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-lysp100_associated_nuclear_domain-uniprot-verify
- check_id: lysp100_associated_nuclear_domain-uniprot-causal
  name: Native LYSP100-associated nuclear domain UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0016606
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/lysp100_associated_nuclear_domain.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-lysp100_associated_nuclear_domain-uniprot-causal
- check_id: m_aaa_complex-uniprot-verify
  name: Native m-AAA complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005745
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/m_aaa_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-m_aaa_complex-uniprot-verify
- check_id: m_aaa_complex-uniprot-causal
  name: Native m-AAA complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005745
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/m_aaa_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-m_aaa_complex-uniprot-causal
- check_id: macab_tolc_complex-uniprot-verify
  name: Native MacAB-TolC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990196
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/macab_tolc_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-macab_tolc_complex-uniprot-verify
- check_id: macab_tolc_complex-uniprot-causal
  name: Native MacAB-TolC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990196
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/macab_tolc_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-macab_tolc_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/isw1_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912;
    current SHA256 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912.
    Record bytes unchanged since the original review.
  snapshot_sha256: 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9acdb77d73b67e676b09e489f69d11accd7e5097d79aeee7df506b1e38097d7c
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/isw1a_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865;
    current SHA256 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 11a7087b4b9ceddaabf4cfb426f1380a5a8012cb155d54ca310258132fb17c4f
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/isw1b_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137;
    current SHA256 da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137.
    Record bytes unchanged since the original review.
  snapshot_sha256: da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 4183282a7718a6f641674d7a9c91ecfc223b99c73bdff509c9978a6253e84b5d
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/kinetochore.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 aefa8aee06e9c0d6c20b86cf110f44bd6ead107d28e5ae579027cf07a957bf9e;
    current SHA256 ea8645dec5b13874441be4fa7a2db0b477265d3c23ecd399aa9559824428640d.
    Changed record reassessed against current sources.
  snapshot_sha256: ea8645dec5b13874441be4fa7a2db0b477265d3c23ecd399aa9559824428640d
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T080129Z-kinetochore-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 54c19f806698dec91e445973dc9037e2fd23c8f44685683db50a6539c5eac083
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/ku70_ku80_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44;
    current SHA256 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 599877808fbf65125c153255d03500c2ea571d6412e90423e84110b2bf214fcc
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/lipopolysaccharide_transport_system.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e;
    current SHA256 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T080130Z-lipopolysaccharide-transport-system-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a9cd71fe7c4f253a769cf31d55cc615adcdbc1c1fb0547b2ea481d58009b2ef3
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 9bc1e320681a91bb883829715c5e4db10330c4f5505b7155f8485e6e662d0f80;
    current SHA256 96bf1ce75ce606af29c2d8a549c345e9487f0e426ac1f86823f14db22c651866.
    Changed record reassessed against current sources.
  snapshot_sha256: 96bf1ce75ce606af29c2d8a549c345e9487f0e426ac1f86823f14db22c651866
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 69c90d2c80fcf3825f88c8f33616374e1abb58414ba0ba2ba3ce9edfd04cba0c
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/lysp100_associated_nuclear_domain.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493;
    current SHA256 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T080132Z-lysp100-associated-nuclear-domain-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 07a59eacac81ab2cefb303de28cdc2617de403a1c9ec1b35ed9136b44971dc5b
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/m_aaa_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 799f2eef086fc6c2f621ee63a5b1293feaf04cb48bcf31743bff7988497991a6;
    current SHA256 9686eb96f5b95da3c8b9dbb002841e31ac5c884c66e4af52f05706b375ea87a7.
    Changed record reassessed against current sources.
  snapshot_sha256: 9686eb96f5b95da3c8b9dbb002841e31ac5c884c66e4af52f05706b375ea87a7
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T080133Z-m-aaa-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 22517eca0c698f0befc2c2d854f086f6873d11853fcb4b62bb783b8c036adcc8
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/macab_tolc_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Original frozen SHA256 b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636;
    current SHA256 b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636.
    Record bytes unchanged since the original review.
  snapshot_sha256: b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T080133Z-macab-tolc-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T13:37:13Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c50a5725d852f71a2553749170a3cbef86efa47120cb9a3d27a43b9eb3c6ac88
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/isw1_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T13:31:16.686588Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: 5662405c6e9c5ce9d246c4ea52175ca1cce9eee337ac704e5cb405e66f0ce912
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml
  locator: Complete immutable original native review and deterministic Markdown
  accessed_at: '2026-11-04T13:31:16.686666Z'
  support: context_only
  summary: Original findings/actions, evidence kinds and stated source tiers, checks,
    verdict and limitations audited. Historical access is not retrospectively upgraded
    by fresh retrieval.
  snapshot_sha256: 9acdb77d73b67e676b09e489f69d11accd7e5097d79aeee7df506b1e38097d7c
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/0-stale.diff
  locator: Actual diff original source revision to reviewed main
  accessed_at: '2026-11-04T13:31:16.686703Z'
  support: context_only
  summary: Empty record delta; original frozen target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/isw1a_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T13:31:16.686730Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: 1f8db379fbf44a20126d11fe7418076ec4361066f6564871614361ad31273865
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml
  locator: Complete immutable original native review and deterministic Markdown
  accessed_at: '2026-11-04T13:31:16.686748Z'
  support: context_only
  summary: Original findings/actions, evidence kinds and stated source tiers, checks,
    verdict and limitations audited. Historical access is not retrospectively upgraded
    by fresh retrieval.
  snapshot_sha256: 11a7087b4b9ceddaabf4cfb426f1380a5a8012cb155d54ca310258132fb17c4f
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/1-stale.diff
  locator: Actual diff original source revision to reviewed main
  accessed_at: '2026-11-04T13:31:16.686779Z'
  support: context_only
  summary: Empty record delta; original frozen target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/isw1b_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T13:31:16.686803Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: da27a6000afe1a8e535d8586b2841416d6f10e07058b226e446d785541c37137
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml
  locator: Complete immutable original native review and deterministic Markdown
  accessed_at: '2026-11-04T13:31:16.686821Z'
  support: context_only
  summary: Original findings/actions, evidence kinds and stated source tiers, checks,
    verdict and limitations audited. Historical access is not retrospectively upgraded
    by fresh retrieval.
  snapshot_sha256: 4183282a7718a6f641674d7a9c91ecfc223b99c73bdff509c9978a6253e84b5d
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/2-stale.diff
  locator: Actual diff original source revision to reviewed main
  accessed_at: '2026-11-04T13:31:16.686852Z'
  support: context_only
  summary: Empty record delta; original frozen target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-3
  kind: record_content
  reference: data/structures/other/ku70_ku80_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T13:31:16.686875Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44
- evidence_id: micro-prior-3
  kind: prior_review
  reference: reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml
  locator: Complete immutable original native review and deterministic Markdown
  accessed_at: '2026-11-04T13:31:16.686894Z'
  support: context_only
  summary: Original findings/actions, evidence kinds and stated source tiers, checks,
    verdict and limitations audited. Historical access is not retrospectively upgraded
    by fresh retrieval.
  snapshot_sha256: 599877808fbf65125c153255d03500c2ea571d6412e90423e84110b2bf214fcc
- evidence_id: micro-delta-3
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/4-stale.diff
  locator: Actual diff original source revision to reviewed main
  accessed_at: '2026-11-04T13:31:16.686925Z'
  support: context_only
  summary: Empty record delta; original frozen target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components, Evidence and Discussions sections
  accessed_at: '2026-11-04T13:31:16.686948Z'
  support: context_only
  summary: Components may denote taxon-agnostic families or classes. Specific class
    identities, roles, claims and evidence must agree; optional examples are not an
    exhaustive inventory. Formation necessity differs from activity/viability. Dated
    rationale is append-only.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum and graph scope fields
  accessed_at: '2026-11-04T13:31:16.686971Z'
  support: context_only
  summary: Reviewed-label-only needs a reason; UNKNOWN is valid and neither generic
    classes nor sparse examples alone establish defects.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Whole graph-kind/scope, actor and edge-evidence contract
  accessed_at: '2026-11-04T13:31:16.687000Z'
  support: context_only
  summary: Membership and broad function can be represented as NONMECHANISTIC. No
    mandatory detailed assembly pathway or universal necessity inference follows from
    a coarse graph.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Full review workflow and structured-source applicability
  accessed_at: '2026-11-04T13:31:16.687016Z'
  support: context_only
  summary: Positive molecular/function/pathway assertions trigger actual source applicability,
    independently of expression-specific claims.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-native-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Full configured checks/rubrics
  accessed_at: '2026-11-04T13:31:16.687036Z'
  support: context_only
  summary: Read native configured workflow; root owns corpus gates and successor publication.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/original-audit.json
  locator: Eight actual original native validate/render commands; 61 historical input
    occurrences; eight original artifacts
  accessed_at: '2026-11-04T13:23:43.403293Z'
  support: supports
  summary: All eight commands exit zero, original Markdown equals renderer output
    byte-for-byte, all declared historical inputs match their revision/hash and original
    PR artifacts are immutable.
  snapshot_sha256: 8d30c9d5e41a859b3c876c32771d46d1b92bb0d1b4fb1c84d8de51446b643b1b
- evidence_id: micro-protein-P38144
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38144.json
  locator: Current status/name, full gene primary/alias/locus fields, organism; complete
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-P38144.raw
  accessed_at: '2026-11-04T13:18:10.979792Z'
  support: supports
  summary: 'P38144: UniProtKB reviewed (Swiss-Prot); ISWI chromatin-remodeling complex
    ATPase ISW1; taxon 559292; genes [{''geneName'': {''value'': ''ISW1''}, ''orderedLocusNames'':
    [{''value'': ''YBR245C''}], ''orfNames'': [{''value'': ''YBR1633''}]}]; InterPro
    [''IPR014001'', ''IPR001650'', ''IPR009057'', ''IPR044754'', ''IPR015194'', ''IPR036306'',
    ''IPR027417'', ''IPR001005'', ''IPR017884'', ''IPR015195'', ''IPR038718'', ''IPR049730'',
    ''IPR000330'']. Reference annotation, native citation provenance and actual experimental
    preparations are distinguished.'
  snapshot_sha256: bbf8ea6564b1a0aeb6b66ba4f0449ebf54b36b780e36dc504e4c88293889256e
- evidence_id: micro-protein-P43596
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P43596.json
  locator: Current status/name, full gene primary/alias/locus fields, organism; complete
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-P43596.raw
  accessed_at: '2026-11-04T13:18:11.812648Z'
  support: supports
  summary: 'P43596: UniProtKB reviewed (Swiss-Prot); ISWI one complex protein 3; taxon
    559292; genes [{''geneName'': {''value'': ''IOC3''}, ''orderedLocusNames'': [{''value'':
    ''YFR013W''}]}]; InterPro [''IPR028942'']. Reference annotation, native citation
    provenance and actual experimental preparations are distinguished.'
  snapshot_sha256: 5983cfa5c731bff1eba1b98ebfb1e56bb7726272e1e2128ec405e109ccbaa512
- evidence_id: micro-protein-Q12072
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12072.json
  locator: Current status/name, full gene primary/alias/locus fields, organism; complete
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-Q12072.raw
  accessed_at: '2026-11-04T13:18:12.831559Z'
  support: supports
  summary: 'Q12072: UniProtKB reviewed (Swiss-Prot); ISWI one complex protein 2; taxon
    559292; genes [{''geneName'': {''value'': ''IOC2''}, ''orderedLocusNames'': [{''value'':
    ''YLR095C''}]}]; InterPro [''IPR063422'', ''IPR062587'', ''IPR062429'', ''IPR011011''].
    Reference annotation, native citation provenance and actual experimental preparations
    are distinguished.'
  snapshot_sha256: 4035abf4ee6da474aae5a55ddcd7f7f0ed4d671a7f51aa4e597c8d74ac33f885
- evidence_id: micro-protein-Q04213
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04213.json
  locator: Current status/name, full gene primary/alias/locus fields, organism; complete
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-Q04213.raw
  accessed_at: '2026-11-04T13:18:13.873781Z'
  support: supports
  summary: 'Q04213: UniProtKB reviewed (Swiss-Prot); ISWI one complex protein 4; taxon
    559292; genes [{''geneName'': {''value'': ''IOC4''}, ''orderedLocusNames'': [{''value'':
    ''YMR044W''}], ''orfNames'': [{''value'': ''YM9532.09''}]}]; InterPro [''IPR035503'',
    ''IPR000313'']. Reference annotation, native citation provenance and actual experimental
    preparations are distinguished.'
  snapshot_sha256: 05f67a4b4a1047320b071cf91045b4b153e9b88c4ae7e95a845ca6fed97441c4
- evidence_id: micro-protein-P32807
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32807.json
  locator: Current status/name, full gene primary/alias/locus fields, organism; complete
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-P32807.raw
  accessed_at: '2026-11-04T13:18:15.974466Z'
  support: supports
  summary: 'P32807: UniProtKB reviewed (Swiss-Prot); ATP-dependent DNA helicase II
    subunit 1; taxon 559292; genes [{''geneName'': {''value'': ''YKU70''}, ''synonyms'':
    [{''value'': ''HDF1''}, {''value'': ''NES24''}], ''orderedLocusNames'': [{''value'':
    ''YMR284W''}], ''orfNames'': [{''value'': ''YM8021.10''}]}]; InterPro [''IPR006164'',
    ''IPR006165'', ''IPR047087'', ''IPR005160'', ''IPR005161'', ''IPR016194'', ''IPR036465''].
    Reference annotation, native citation provenance and actual experimental preparations
    are distinguished.'
  snapshot_sha256: 97b4ff0a59bb5294156d7eeb57199c772db366277ef994a179e5e733c0fe0a2c
- evidence_id: micro-protein-Q04437
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04437.json
  locator: Current status/name, full gene primary/alias/locus fields, organism; complete
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/protein-Q04437.raw
  accessed_at: '2026-11-04T13:18:10.855182Z'
  support: supports
  summary: 'Q04437: UniProtKB reviewed (Swiss-Prot); ATP-dependent DNA helicase II
    subunit 2; taxon 559292; genes [{''geneName'': {''value'': ''YKU80''}, ''synonyms'':
    [{''value'': ''HDF2''}], ''orderedLocusNames'': [{''value'': ''YMR106C''}], ''orfNames'':
    [{''value'': ''YM9718.05C''}]}]; InterPro [''IPR006164'', ''IPR024193'', ''IPR005161'',
    ''IPR016194'', ''IPR036465'']. Reference annotation, native citation provenance
    and actual experimental preparations are distinguished.'
  snapshot_sha256: 6b53c3dac8841bccdd6fd94d179ad85217e17dd85f06a419c0cfb5ec5ebadcd3
- evidence_id: micro-query-IOC2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full exact reviewed gene/taxon result page, total-result and next-link
    headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-IOC2.raw
  accessed_at: '2026-11-04T13:18:13.950783Z'
  support: supports
  summary: One current reviewed result ['Q12072'], matching primary gene and S288C
    taxon; all alias/locus fields inspected. This does not reconstruct the dated historical
    query execution.
  snapshot_sha256: 608a84c396b8605bceb1199ad71f40482f9f036bf6b9ac8056febf4dfca0f2c8
  search_scope: UniProtKB; query (gene_exact:IOC2) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T13:18:13.950783Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-IOC3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full exact reviewed gene/taxon result page, total-result and next-link
    headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-IOC3.raw
  accessed_at: '2026-11-04T13:18:14.944689Z'
  support: supports
  summary: One current reviewed result ['P43596'], matching primary gene and S288C
    taxon; all alias/locus fields inspected. This does not reconstruct the dated historical
    query execution.
  snapshot_sha256: 65be11719af8c81aa807ff17341fc61c102ad9d4fed34b809a2b4b1c81a9d464
  search_scope: UniProtKB; query (gene_exact:IOC3) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T13:18:14.944689Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-IOC4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIOC4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full exact reviewed gene/taxon result page, total-result and next-link
    headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-IOC4.raw
  accessed_at: '2026-11-04T13:18:12.951915Z'
  support: supports
  summary: One current reviewed result ['Q04213'], matching primary gene and S288C
    taxon; all alias/locus fields inspected. This does not reconstruct the dated historical
    query execution.
  snapshot_sha256: 4656f8fb3cc23c0748c260dd404667148c4bbb98c891e8d265cb09dcfbaab074
  search_scope: UniProtKB; query (gene_exact:IOC4) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T13:18:12.951915Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-ISW1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full exact reviewed gene/taxon result page, total-result and next-link
    headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-ISW1.raw
  accessed_at: '2026-11-04T13:18:12.017061Z'
  support: supports
  summary: One current reviewed result ['P38144'], matching primary gene and S288C
    taxon; all alias/locus fields inspected. This does not reconstruct the dated historical
    query execution.
  snapshot_sha256: 775233aac5f6c5e13fc0a73ff73d13b9055f2c9fc8c8ccf000d4373501cb662f
  search_scope: UniProtKB; query (gene_exact:ISW1) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T13:18:12.017061Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-YKU70
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU70%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full exact reviewed gene/taxon result page, total-result and next-link
    headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-YKU70.raw
  accessed_at: '2026-11-04T13:18:14.989877Z'
  support: supports
  summary: One current reviewed result ['P32807'], matching primary gene and S288C
    taxon; all alias/locus fields inspected. This does not reconstruct the dated historical
    query execution.
  snapshot_sha256: 56193c1470cfac0d0b5ffd1aad8cad276cbce4e55ffef0eb1b8f1e0c32c7b2e1
  search_scope: UniProtKB; query (gene_exact:YKU70) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T13:18:14.989877Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-YKU80
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full exact reviewed gene/taxon result page, total-result and next-link
    headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/query-YKU80.raw
  accessed_at: '2026-11-04T13:18:16.193680Z'
  support: supports
  summary: One current reviewed result ['Q04437'], matching primary gene and S288C
    taxon; all alias/locus fields inspected. This does not reconstruct the dated historical
    query execution.
  snapshot_sha256: cedf3624a19a6ba4a5bf2f8252edf337727515ab84978260ce94b60948ef9d31
  search_scope: UniProtKB; query (gene_exact:YKU80) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T13:18:16.193680Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Exact native name, active state, rank, parent and reference-strain lineage;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/tax-4932.raw
  accessed_at: '2026-11-04T13:18:09.799197Z'
  support: supports
  summary: 'Taxon 4932: Saccharomyces cerevisiae, active True, rank species. S. cerevisiae
    species and S288C protein-reference strain are not interchangeable experimental
    claims.'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
- evidence_id: micro-tax-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Exact native name, active state, rank, parent and reference-strain lineage;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/tax-559292.raw
  accessed_at: '2026-11-04T13:18:09.931493Z'
  support: supports
  summary: 'Taxon 559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c), active
    True, rank strain. S. cerevisiae species and S288C protein-reference strain are
    not interchangeable experimental claims.'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: micro-go-0006303
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006303
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0006303.raw
  accessed_at: '2026-11-04T13:18:09.452460Z'
  support: supports
  summary: 'GO:0006303: double-strand break repair via nonhomologous end joining;
    isObsolete=False. Definition and structure/function scope inspected; authority
    text is not a new experimental assay.'
  snapshot_sha256: e1b0d7187fceb1950f31b4c99b44b3bdffe2cb49ab4216b96dc435f2a205dd0a
- evidence_id: micro-go-0006338
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006338
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0006338.raw
  accessed_at: '2026-11-04T13:18:09.218899Z'
  support: supports
  summary: 'GO:0006338: chromatin remodeling; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: 1d1be8a7b9b76d3fb84d9ad059c890b5b57f8ce43b54d4530fbf09173c4ac82b
- evidence_id: micro-go-0016587
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0016587
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0016587.raw
  accessed_at: '2026-11-04T13:18:09.546487Z'
  support: supports
  summary: 'GO:0016587: Isw1 complex; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: 959e759c4f870068b5f175dc486dd065803bd220a5e54cd9e726381b8de975aa
- evidence_id: micro-go-0031010
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0031010
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0031010.raw
  accessed_at: '2026-11-04T13:18:09.166252Z'
  support: supports
  summary: 'GO:0031010: ISWI-type complex; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: ab478e694e3e60d5d5f750c82c919d547d818d8a612ea5870d3bcf4b8ff67539
- evidence_id: micro-go-0036436
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036436
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0036436.raw
  accessed_at: '2026-11-04T13:18:09.203673Z'
  support: supports
  summary: 'GO:0036436: Isw1a complex; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: 729f79cdd66eb5f4302b4bfb4d5d1fa856b60a9dcdd0479845eaca8d5ec35342
- evidence_id: micro-go-0036437
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036437
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0036437.raw
  accessed_at: '2026-11-04T13:18:09.218936Z'
  support: supports
  summary: 'GO:0036437: Isw1b complex; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: c37f52ca44c719843c24bfe70e0184cd4dc43f9b319a364b8dfc8027608ac327
- evidence_id: micro-go-0043564
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043564
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0043564.raw
  accessed_at: '2026-11-04T13:18:09.211147Z'
  support: supports
  summary: 'GO:0043564: Ku70:Ku80 complex; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: 4ecec1b8bbc4014c64611d4c91cc06343f9835b99bd444becc4aaaa57b19a6c2
- evidence_id: micro-go-0045027
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0045027
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0045027.raw
  accessed_at: '2026-11-04T13:18:09.385947Z'
  support: supports
  summary: 'GO:0045027: DNA end binding; isObsolete=False. Definition and structure/function
    scope inspected; authority text is not a new experimental assay.'
  snapshot_sha256: d131971d14f16a80916fd0d4249157dc8a740326ec2c66b783923860aedf8921
- evidence_id: micro-go-0140513
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0140513
  locator: Exact active term, full definition/synonyms and typed relationships; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/go-0140513.raw
  accessed_at: '2026-11-04T13:18:09.313493Z'
  support: supports
  summary: 'GO:0140513: nuclear protein-containing complex; isObsolete=False. Definition
    and structure/function scope inspected; authority text is not a new experimental
    assay.'
  snapshot_sha256: 61c31928c6fb33a97da0bafa0beafb5392a27dac53b617f92ba08fb5cf0511b7
- evidence_id: micro-ancestors-0016587
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0016587/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0016587.raw
  accessed_at: '2026-11-04T13:18:09.753388Z'
  support: supports
  summary: GO:0016587 ancestors ['GO:1902494', 'GO:1904949', 'GO:0140513', 'GO:0031010',
    'GO:0032991', 'GO:0070603', 'GO:0016587', 'GO:0005575']; declared parent corroborated,
    distinct from parthood or prevalence.
  snapshot_sha256: 4a6b452cbefdc3ce54b0624458fdb5e4f3e364115f04dac492a1fcc2b36a3c81
- evidence_id: micro-ancestors-0036436
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036436/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0036436.raw
  accessed_at: '2026-11-04T13:18:09.882635Z'
  support: supports
  summary: GO:0036436 ancestors ['GO:1902494', 'GO:1904949', 'GO:0140513', 'GO:0031010',
    'GO:0032991', 'GO:0070603', 'GO:0016587', 'GO:0005575', 'GO:0036436']; declared
    parent corroborated, distinct from parthood or prevalence.
  snapshot_sha256: b0738aec16a8ba61a410853263c7c1ff04a4a20148134d7e02cc443ad1b55486
- evidence_id: micro-ancestors-0036437
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0036437/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0036437.raw
  accessed_at: '2026-11-04T13:18:09.807109Z'
  support: supports
  summary: GO:0036437 ancestors ['GO:1902494', 'GO:1904949', 'GO:0140513', 'GO:0031010',
    'GO:0032991', 'GO:0070603', 'GO:0016587', 'GO:0005575', 'GO:0036437']; declared
    parent corroborated, distinct from parthood or prevalence.
  snapshot_sha256: e4da0c42c3c80f09c12136df991e0b4f73e6e91e5e07d2f9de9f8a9c1aad7c42
- evidence_id: micro-ancestors-0043564
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043564/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/ancestors-0043564.raw
  accessed_at: '2026-11-04T13:18:09.858628Z'
  support: supports
  summary: GO:0043564 ancestors ['GO:0140513', 'GO:0032991', 'GO:0043564', 'GO:0005575'];
    declared parent corroborated, distinct from parthood or prevalence.
  snapshot_sha256: e1e7c030bfc18631a6490f9871801204f800d42102f2268664e61baa47f5bd2c
- evidence_id: micro-family-IPR006165
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006165/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR006165.raw
  accessed_at: '2026-11-04T13:18:10.448782Z'
  support: supports
  summary: 'IPR006165: Ku70; type family. Exact Ku70 whole-protein family, positively
    linked from reviewed yeast P32807; PIRSF003033/TIGR00578 signatures. These exact
    candidate entries do not constitute an exhaustive family absence search or independent
    sequence alignment.'
  snapshot_sha256: 468a80293945de05f280632f853a4bc5c60988ebb0cf696fc8be32e28efd2248
- evidence_id: micro-family-IPR024193
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024193/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR024193.raw
  accessed_at: '2026-11-04T13:18:10.471197Z'
  support: supports
  summary: 'IPR024193: Ku80; type family. Exact Ku80 family, positively linked from
    reviewed yeast Q04437; PIRSF016570/cd00873 signatures. These exact candidate entries
    do not constitute an exhaustive family absence search or independent sequence
    alignment.'
  snapshot_sha256: 19728344223f897e6e0aa282f7a6e65bd36d9ad49e90fdbc9e72ee4590a3c6ac
- evidence_id: micro-family-IPR006164
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006164/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR006164.raw
  accessed_at: '2026-11-04T13:18:10.480774Z'
  support: supports
  summary: 'IPR006164: Ku70/Ku80, DNA-binding domain; type domain. Shared Ku70/Ku80
    DNA-binding domain; not a whole-subunit class substitute. These exact candidate
    entries do not constitute an exhaustive family absence search or independent sequence
    alignment.'
  snapshot_sha256: 37767860040074bdb317cccb96a77d53a34eb4bec030215c8da1fd34e9d889d0
- evidence_id: micro-family-IPR044754
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR044754.raw
  accessed_at: '2026-11-04T13:19:38.928437Z'
  support: supports
  summary: 'IPR044754: Isw1/2, N-terminal; type domain. Isw1/Isw2 N-terminal domain,
    spanning both ATPase paralogs; not exact whole Isw1. These exact candidate entries
    do not constitute an exhaustive family absence search or independent sequence
    alignment.'
  snapshot_sha256: 061068d91ce4e280dc97c8d9a97b780be29b8b80f8c5df5475c0f0511e87bf06
- evidence_id: micro-family-IPR038718
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038718/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR038718.raw
  accessed_at: '2026-11-04T13:19:38.921128Z'
  support: supports
  summary: 'IPR038718: SNF2-like, N-terminal domain superfamily; type homologous_superfamily.
    Broad SNF2-like N-terminal domain superfamily, not exact whole Isw1. These exact
    candidate entries do not constitute an exhaustive family absence search or independent
    sequence alignment.'
  snapshot_sha256: 4ea00d2c09f5089e771ef955d3066039ffbdca88d870d85de0109600aa99e155
- evidence_id: micro-family-IPR035503
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035503/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR035503.raw
  accessed_at: '2026-11-04T13:19:38.928464Z'
  support: supports
  summary: 'IPR035503: IOC4-like, PWWP domain; type domain. IOC4-like PWWP domain,
    not whole Ioc4. These exact candidate entries do not constitute an exhaustive
    family absence search or independent sequence alignment.'
  snapshot_sha256: 2be8ebb80d6bf3d9e6dfe5093f4324782c533a9bec6c5abe0e44cf0a8a9d7d45
- evidence_id: micro-family-IPR062587
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062587/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR062587.raw
  accessed_at: '2026-11-04T13:19:38.938474Z'
  support: supports
  summary: 'IPR062587: IOC2, middle domain; type domain. IOC2 middle domain, not whole
    Ioc2. These exact candidate entries do not constitute an exhaustive family absence
    search or independent sequence alignment.'
  snapshot_sha256: 41efdf3fd1268876253e8db2213e55abd8dc6495513a3be0d695760d7b9da214
- evidence_id: micro-family-IPR028942-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028942/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR028942-retry.raw
  accessed_at: '2026-11-04T13:26:32.402930Z'
  support: supports
  summary: 'IPR028942: WHIM1 domain; type domain. WHIM1 domain, not whole Ioc3. These
    exact candidate entries do not constitute an exhaustive family absence search
    or independent sequence alignment.'
  snapshot_sha256: 91d266cd2f819b65c0636857bebd436de01d5f733d51a68a873c3c8b8bb07776
- evidence_id: micro-family-IPR062429-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062429/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR062429-retry.raw
  accessed_at: '2026-11-04T13:26:34.224087Z'
  support: supports
  summary: 'IPR062429: ISWI one complex protein 2, N-terminal domain; type domain.
    IOC2 N-terminal domain, not whole Ioc2. These exact candidate entries do not constitute
    an exhaustive family absence search or independent sequence alignment.'
  snapshot_sha256: 131a1fdb8dfebcd5880e3ed5368994aa658dd9b68d55d27fd89c9f2356c1ca22
- evidence_id: micro-family-IPR063422-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063422/
  locator: Complete native name/type, description with quality flags, integrated signatures
    and hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/family-IPR063422-retry.raw
  accessed_at: '2026-11-04T13:26:35.858903Z'
  support: supports
  summary: 'IPR063422: IOC2, C-terminal domain; type domain. IOC2 C-terminal domain,
    not whole Ioc2. These exact candidate entries do not constitute an exhaustive
    family absence search or independent sequence alignment.'
  snapshot_sha256: f653a487609cb242e843fd92c5219bf5ffedd7820a8504913421f7e5f1393787
- evidence_id: micro-pmid-12482963
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12482963+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-12482963.raw
  accessed_at: '2026-11-04T13:18:12.523681Z'
  support: context_only
  summary: Yeast Isw1p forms two separable complexes in vivo.; Vary JC, Gangaraju
    VK, Qin J, Landel CC, Kooperberg C, Bartholomew B, Tsukiyama T.; PMID12482963,
    DOI10.1128/mcb.23.1.80-91.2003. Complete indexed abstract read. Primary versus
    review publication type checked; no unlisted body access inferred.
  snapshot_sha256: 00c6ca1ad49fba2824a8f7145b98b5f891071836ab92930b680a4dd90f96d06d
  search_scope: Europe PMC; query EXT_ID:12482963 AND SRC:MED; actual accessed_at
    2026-11-04T13:18:12.523681Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-12518983
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12518983+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-12518983.raw
  accessed_at: '2026-11-04T13:18:15.130146Z'
  support: context_only
  summary: Dimerization, translocation and localization of Ku70 and Ku80 proteins.;
    Koike M.; PMID12518983, DOI10.1269/jrr.43.223. Complete indexed abstract read.
    Primary versus review publication type checked; no unlisted body access inferred.
  snapshot_sha256: bfc351a6487a52790268143567e1aa513342033188590f5faf30b189f7154f91
  search_scope: Europe PMC; query EXT_ID:12518983 AND SRC:MED; actual accessed_at
    2026-11-04T13:18:15.130146Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-14562095.raw
  accessed_at: '2026-11-04T13:18:12.657404Z'
  support: context_only
  summary: Global analysis of protein localization in budding yeast.; Huh WK, Falvo
    JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; PMID14562095, DOI10.1038/nature02026.
    Complete indexed abstract read. Primary versus review publication type checked;
    no unlisted body access inferred.
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
  search_scope: Europe PMC; query EXT_ID:14562095 AND SRC:MED; actual accessed_at
    2026-11-04T13:18:12.657404Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-15122350
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15122350+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-15122350.raw
  accessed_at: '2026-11-04T13:18:15.222801Z'
  support: context_only
  summary: 'A means to a DNA end: the many roles of Ku.; Downs JA, Jackson SP.; PMID15122350,
    DOI10.1038/nrm1367. No abstractText in exact returned result; bibliographic metadata
    only. Primary versus review publication type checked; no unlisted body access
    inferred.'
  snapshot_sha256: e68ea167c83d26c3c2b94519238b9311925af13bd31c2cbd1f6c15012058df57
  search_scope: Europe PMC; query EXT_ID:15122350 AND SRC:MED; actual accessed_at
    2026-11-04T13:18:15.222801Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-8890183
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8890183+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-8890183.raw
  accessed_at: '2026-11-04T13:18:15.249342Z'
  support: context_only
  summary: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand
    break repair and serves as a barrier to error-prone DNA repair pathways.; Boulton
    SJ, Jackson SP.; PMID8890183, DOI10.1002/j.1460-2075.1996.tb00890.x. Complete
    indexed abstract read. Primary versus review publication type checked; no unlisted
    body access inferred.
  snapshot_sha256: 184c9023983ff3e0c30cc772ebf8e940cd9dbd5a804397be14fc89d21ad30c09
  search_scope: Europe PMC; query EXT_ID:8890183 AND SRC:MED; actual accessed_at 2026-11-04T13:18:15.249342Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-pmid-8910371
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910371+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-8910371.raw
  accessed_at: '2026-11-04T13:18:14.977959Z'
  support: context_only
  summary: HDF2, the second subunit of the Ku homologue from Saccharomyces cerevisiae.;
    Feldmann H, Driller L, Meier B, Mages G, Kellermann J, Winnacker EL.; PMID8910371,
    DOI10.1074/jbc.271.44.27765. Complete indexed abstract read. Primary versus review
    publication type checked; no unlisted body access inferred.
  snapshot_sha256: a1bd1576de76d17dcccff025b5ab46127a8b7cd85e4585e00b191d9536919e31
  search_scope: Europe PMC; query EXT_ID:8910371 AND SRC:MED; actual accessed_at 2026-11-04T13:18:14.977959Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-pmid-8972848
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8972848+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-8972848.raw
  accessed_at: '2026-11-04T13:18:14.497257Z'
  support: context_only
  summary: 'Identification of a Saccharomyces cerevisiae Ku80 homologue: roles in
    DNA double strand break rejoining and in telomeric maintenance.; Boulton SJ, Jackson
    SP.; PMID8972848, DOI10.1093/nar/24.23.4639. Complete indexed abstract read. Primary
    versus review publication type checked; no unlisted body access inferred.'
  snapshot_sha256: 2863f379f06ab17a1956681eafb5b8312e948e4d6905c118eb4cb109de92dc12
  search_scope: Europe PMC; query EXT_ID:8972848 AND SRC:MED; actual accessed_at 2026-11-04T13:18:14.497257Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-pmid-9635192
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9635192+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Unique exact MED PMID metadata, authors/year/DOI/article type and full
    abstract when present; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/pmid-9635192.raw
  accessed_at: '2026-11-04T13:18:14.793265Z'
  support: context_only
  summary: Mutation of yeast Ku genes disrupts the subnuclear organization of telomeres.;
    Laroche T, Martin SG, Gotta M, Gorham HC, Pryde FE, Louis EJ, Gasser SM.; PMID9635192,
    DOI10.1016/s0960-9822(98)70252-0. Complete indexed abstract read. Primary versus
    review publication type checked; no unlisted body access inferred.
  snapshot_sha256: f9028d08fcaec95986c5cb172700321df3bef5d4a428e0cee68a07e9522d3eed
  search_scope: Europe PMC; query EXT_ID:9635192 AND SRC:MED; actual accessed_at 2026-11-04T13:18:14.793265Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-vary2003-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/
  locator: Genuine PMC HTML; complete Methods sec2–11 including strain Table1, Results
    sec13–20, Discussion sec21 and all embedded Figures1–5 text captions; not Introduction,
    Table2 appendix, pixels or external/raw data; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/vary2003-html.raw
  accessed_at: '2026-11-04T13:18:14.754228Z'
  support: supports
  summary: Vary and colleagues directly separate Isw1-Ioc3 and Isw1-Ioc2-Ioc4 assemblies
    by reciprocal immunoprecipitation and tagged purification. Ioc2/Ioc4 are mutually
    required for stable recovery under tested conditions. Both complexes show nucleosome-stimulated
    ATPase activity; spacing/sliding/binding and genetic-expression results depend
    on assay/substrate. Unstable interactions/other conditions remain possible. W303
    derivatives had RAD5 repaired; S288C references are not the experimental strain.
  snapshot_sha256: a3ee9d2a910b30dcfc59a2e82f6f93e686fc6bae63d57bb90e93ac7cb205b7cc
- evidence_id: micro-koike2002-pdf
  kind: authority
  reference: https://www.jstage.jst.go.jp/article/jrr/43/3/43_3_223/_pdf
  locator: 'Fresh genuine secondary-review PDF; printed pp223–227 and dimerization
    conclusion at the start of p228: complete Abstract/Introduction, chromosome-location
    and dimerization sections, Table1 and Figure1 caption; remaining p228 localization
    excerpt not used, no pixels or later pages; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/koike2002-pdf.raw'
  accessed_at: '2026-11-04T13:19:41.301979Z'
  support: supports
  summary: Koike 2002 distinguishes the Ku heterodimer and DNA-PKcs, two-subunit DNA
    channel, mammalian heterodimer-stability observations and organism-specific NHEJ.
    The review explicitly notes no obvious yeast DNA-PKcs homolog; mammalian V(D)J/DNA-PK
    functions do not become yeast claims. Secondary synthesis is not fresh primary
    assay evidence.
  snapshot_sha256: 4ac70fb22c4df72963efa4f74a797e65fcc2bcc3626ca36c9faee7d44177ac54
- evidence_id: micro-boulton70-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC452249/
  locator: Genuine PMC abstract and article metadata only; full-text route is a scanned/PDF
    landing, not a readable main body; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/boulton70-html.raw
  accessed_at: '2026-11-04T13:19:38.523800Z'
  support: supports
  summary: Complete primary abstract supports the bounded yeast repair/telomere observations
    stated there. Main methods, strain construction, figures and experimental detail
    were not read; genuine landing-page access does not certify full-body access.
  snapshot_sha256: a82282bbb35dd88eee02601cb79658bb905b49b6ee48266a43a9d86ee9c08aab
- evidence_id: micro-boulton80-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC146307/
  locator: Genuine PMC abstract and article metadata only; full-text route is a scanned/PDF
    landing, not a readable main body; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/boulton80-html.raw
  accessed_at: '2026-11-04T13:19:38.565614Z'
  support: supports
  summary: Complete primary abstract supports the bounded yeast repair/telomere observations
    stated there. Main methods, strain construction, figures and experimental detail
    were not read; genuine landing-page access does not certify full-body access.
  snapshot_sha256: 3df791cef0777982cc24f280d25a4c41ee42c39ddb0edfebe73fe740e21c0231
- evidence_id: micro-downs2004-doi
  kind: database
  reference: https://doi.org/10.1038/nrm1367
  locator: DOI content-negotiated Crossref JSON metadata, title/authors/DOI and publisher
    pointers only; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/downs2004-doi.raw
  accessed_at: '2026-11-04T13:19:39.015584Z'
  support: context_only
  summary: DOI resolves to Downs and Jackson 2004 secondary review metadata, not its
    body. The exact MED record has no abstract; no review-body scientific support
    is claimed from this route.
  snapshot_sha256: 2978ef95ad49e713968637bd7c25a2cf1a24695dbeac4c45a175d648d7282be8
- evidence_id: micro-access-vary2003-s3
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC140669.1/PMC140669.1.xml
  locator: Actual HTTP status/content-type and retained diagnostic body
  accessed_at: '2026-11-04T13:18:15.042804Z'
  support: context_only
  summary: HTTP 404; failed route or rate-limit response only, not article/family
    evidence. Later successful access remains separately timestamped.
  snapshot_sha256: 42a8a9821051c12423dfc2eac3aff04e7813e146d308c220491d60c5a6812caf
- evidence_id: micro-access-boulton80-pdf
  kind: validation
  reference: https://academic.oup.com/nar/article-pdf/24/23/4639/3997483/24-23-4639.pdf
  locator: Actual HTTP status/content-type and retained diagnostic body
  accessed_at: '2026-11-04T13:19:38.372869Z'
  support: context_only
  summary: HTTP 403; failed route or rate-limit response only, not article/family
    evidence. Later successful access remains separately timestamped.
  snapshot_sha256: 4260cccf50d1c6bf1e6148f7cdb6ed81fa272a6648ce0c0ec954b936064548ee
- evidence_id: micro-access-feldmann1996-pdf
  kind: validation
  reference: https://www.jbc.org/article/S0021925818352992/pdf
  locator: Actual HTTP status/content-type and retained diagnostic body
  accessed_at: '2026-11-04T13:19:38.504398Z'
  support: context_only
  summary: HTTP 403; failed route or rate-limit response only, not article/family
    evidence. Later successful access remains separately timestamped.
  snapshot_sha256: ced9533fed2c0aca9c096d1ffecda78ea664c4ab5b1bcde71b53d2a3e8853b3f
- evidence_id: micro-access-family-IPR028942
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028942/
  locator: Actual HTTP status/content-type and retained diagnostic body
  accessed_at: '2026-11-04T13:19:38.936533Z'
  support: context_only
  summary: HTTP 429; failed route or rate-limit response only, not article/family
    evidence. Later successful access remains separately timestamped.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-access-family-IPR062429
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062429/
  locator: Actual HTTP status/content-type and retained diagnostic body
  accessed_at: '2026-11-04T13:19:38.928398Z'
  support: context_only
  summary: HTTP 429; failed route or rate-limit response only, not article/family
    evidence. Later successful access remains separately timestamped.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-access-family-IPR063422
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063422/
  locator: Actual HTTP status/content-type and retained diagnostic body
  accessed_at: '2026-11-04T13:19:38.921165Z'
  support: context_only
  summary: HTTP 429; failed route or rate-limit response only, not article/family
    evidence. Later successful access remains separately timestamped.
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: micro-historical-0-access-PMC140669-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/
  locator: Immutable original evidence access-PMC140669-html in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:25:29.713982Z'
  support: context_only
  summary: HTTP200 was a browser challenge, not article text. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 3e1c2bfa98a2b59ecb5d8523bf933eea4f98364160ef0f5a7692e75aa9b91e9b
- evidence_id: micro-historical-0-access-PMC140669-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Immutable original evidence access-PMC140669-xml in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:29:49.530643Z'
  support: context_only
  summary: The first request failed at local DNS before retrieval; no article text.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: micro-historical-0-access-PMC140669-xml-network
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Immutable original evidence access-PMC140669-xml-network in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:16.724232Z'
  support: context_only
  summary: The network XML route returned HTTP500 and an error body. Original access
    timestamp/hash and honest limitations retained; kind corrected to validation/context_only
    in this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: cd338236e7d267bf72bd57f3bd5bb62c39adda0451ca46dea4890f637dcf7e96
- evidence_id: micro-historical-0-access-PMC140669-europepmc
  kind: validation
  reference: https://europepmc.org/articles/PMC140669
  locator: Immutable original evidence access-PMC140669-europepmc in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:32.454249Z'
  support: context_only
  summary: HTTP200 provided a JavaScript page shell rather than the article body.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: db7e4f3351ac6a45e2475e25054e247d557083db08daaa07104d0375e3744b6d
- evidence_id: micro-historical-0-access-vary2003-doi
  kind: validation
  reference: https://doi.org/10.1128/MCB.23.1.80-91.2003
  locator: Immutable original evidence access-vary2003-doi in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:32.454024Z'
  support: context_only
  summary: The publisher DOI route returned HTTP403. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 75b4ca6429c083e85d882dbf8074a4bc357d2b57e479643e830499e16da8ef8d
- evidence_id: micro-historical-0-access-PMC140669-bioc
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode
  locator: Immutable original evidence access-PMC140669-bioc in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:31:06.007594Z'
  support: context_only
  summary: HTTP200 contained an explicit no-result response rather than article text.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-historical-0-access-panther-PTHR45623-SF49
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/
  locator: Immutable original evidence access-panther-PTHR45623-SF49 in reviews/structured/20261022T080127Z-isw1-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:25:29.884732Z'
  support: context_only
  summary: The protein-linked candidate subfamily route returned HTTP204 and no body;
    it did not establish an exact Isw1-only family. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-historical-1-access-PMC140669-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/
  locator: Immutable original evidence access-PMC140669-html in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:25:29.713982Z'
  support: context_only
  summary: HTTP200 was a browser challenge, not article text. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 3e1c2bfa98a2b59ecb5d8523bf933eea4f98364160ef0f5a7692e75aa9b91e9b
- evidence_id: micro-historical-1-access-PMC140669-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Immutable original evidence access-PMC140669-xml in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:29:49.530643Z'
  support: context_only
  summary: The first request failed at local DNS before retrieval; no article text.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: micro-historical-1-access-PMC140669-xml-network
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Immutable original evidence access-PMC140669-xml-network in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:16.724232Z'
  support: context_only
  summary: The network XML route returned HTTP500 and an error body. Original access
    timestamp/hash and honest limitations retained; kind corrected to validation/context_only
    in this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: cd338236e7d267bf72bd57f3bd5bb62c39adda0451ca46dea4890f637dcf7e96
- evidence_id: micro-historical-1-access-PMC140669-europepmc
  kind: validation
  reference: https://europepmc.org/articles/PMC140669
  locator: Immutable original evidence access-PMC140669-europepmc in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:32.454249Z'
  support: context_only
  summary: HTTP200 provided a JavaScript page shell rather than the article body.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: db7e4f3351ac6a45e2475e25054e247d557083db08daaa07104d0375e3744b6d
- evidence_id: micro-historical-1-access-vary2003-doi
  kind: validation
  reference: https://doi.org/10.1128/MCB.23.1.80-91.2003
  locator: Immutable original evidence access-vary2003-doi in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:32.454024Z'
  support: context_only
  summary: The publisher DOI route returned HTTP403. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 75b4ca6429c083e85d882dbf8074a4bc357d2b57e479643e830499e16da8ef8d
- evidence_id: micro-historical-1-access-PMC140669-bioc
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode
  locator: Immutable original evidence access-PMC140669-bioc in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:31:06.007594Z'
  support: context_only
  summary: HTTP200 contained an explicit no-result response rather than article text.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-historical-1-access-panther-PTHR45623-SF49
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/
  locator: Immutable original evidence access-panther-PTHR45623-SF49 in reviews/structured/20261022T080128Z-isw1a-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:25:29.884732Z'
  support: context_only
  summary: The protein-linked candidate subfamily route returned HTTP204 and no body;
    it did not establish an exact Isw1-only family. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-historical-2-access-PMC140669-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC140669/
  locator: Immutable original evidence access-PMC140669-html in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:25:29.713982Z'
  support: context_only
  summary: HTTP200 was a browser challenge, not article text. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 3e1c2bfa98a2b59ecb5d8523bf933eea4f98364160ef0f5a7692e75aa9b91e9b
- evidence_id: micro-historical-2-access-PMC140669-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Immutable original evidence access-PMC140669-xml in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:29:49.530643Z'
  support: context_only
  summary: The first request failed at local DNS before retrieval; no article text.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: 35281279d8e2164cee8666d6f8aad891326911e887ab1b2ab778c8ac6d09dc6c
- evidence_id: micro-historical-2-access-PMC140669-xml-network
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC140669/fullTextXML
  locator: Immutable original evidence access-PMC140669-xml-network in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:16.724232Z'
  support: context_only
  summary: The network XML route returned HTTP500 and an error body. Original access
    timestamp/hash and honest limitations retained; kind corrected to validation/context_only
    in this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: cd338236e7d267bf72bd57f3bd5bb62c39adda0451ca46dea4890f637dcf7e96
- evidence_id: micro-historical-2-access-PMC140669-europepmc
  kind: validation
  reference: https://europepmc.org/articles/PMC140669
  locator: Immutable original evidence access-PMC140669-europepmc in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:32.454249Z'
  support: context_only
  summary: HTTP200 provided a JavaScript page shell rather than the article body.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: db7e4f3351ac6a45e2475e25054e247d557083db08daaa07104d0375e3744b6d
- evidence_id: micro-historical-2-access-vary2003-doi
  kind: validation
  reference: https://doi.org/10.1128/MCB.23.1.80-91.2003
  locator: Immutable original evidence access-vary2003-doi in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:30:32.454024Z'
  support: context_only
  summary: The publisher DOI route returned HTTP403. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 75b4ca6429c083e85d882dbf8074a4bc357d2b57e479643e830499e16da8ef8d
- evidence_id: micro-historical-2-access-PMC140669-bioc
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC140669/unicode
  locator: Immutable original evidence access-PMC140669-bioc in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:31:06.007594Z'
  support: context_only
  summary: HTTP200 contained an explicit no-result response rather than article text.
    Original access timestamp/hash and honest limitations retained; kind corrected
    to validation/context_only in this successor evidence. No fresh invocation or
    retroactive body upgrade.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-historical-2-access-panther-PTHR45623-SF49
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45623:SF49/
  locator: Immutable original evidence access-panther-PTHR45623-SF49 in reviews/structured/20261022T080128Z-isw1b-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:25:29.884732Z'
  support: context_only
  summary: The protein-linked candidate subfamily route returned HTTP204 and no body;
    it did not establish an exact Isw1-only family. Original access timestamp/hash
    and honest limitations retained; kind corrected to validation/context_only in
    this successor evidence. No fresh invocation or retroactive body upgrade.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-historical-3-micro58-PMC146307-legacy
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC146307/
  locator: Immutable original evidence micro58-PMC146307-legacy in reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:40:11.789749Z'
  support: context_only
  summary: The retained HTTP200 legacy response is a browser-check challenge, not
    the Boulton Ku80 main body. Original access timestamp/hash and honest limitations
    retained; kind corrected to validation/context_only in this successor evidence.
    No fresh invocation or retroactive body upgrade.
  snapshot_sha256: 23a88ed17b8924b06b1aa09297a6bc80ec9860287a84c67b9c1fd5c285367901
- evidence_id: micro-historical-3-micro58-feldmann1996-publisher-html
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/S0021925818352992
  locator: Immutable original evidence micro58-feldmann1996-publisher-html in reviews/structured/20261022T080129Z-ku70-ku80-complex-audit/review.yaml;
    diagnostic access scope only
  accessed_at: '2026-10-22T07:41:28.162364Z'
  support: context_only
  summary: The ScienceDirect route returned403 and an error page, not the Feldmann
    main body. Original access timestamp/hash and honest limitations retained; kind
    corrected to validation/context_only in this successor evidence. No fresh invocation
    or retroactive body upgrade.
  snapshot_sha256: e11a834745d1c85b7a586974bbf9a45fe612ce8118422eb2ada5d26736ddc865
- evidence_id: micro-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete official organism/dataset catalogue, all organism names and dataset
    pairs; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-catalogue.raw
  accessed_at: '2026-11-04T13:18:08.811643Z'
  support: context_only
  summary: All 20 organism rows and 28 organism/dataset pairs inspected. No Saccharomyces
    host is present in this exact current response. No matched dataset exists for
    these four yeast-scoped records; no foreign-host gene/module proxy or expression-to-assembly
    inference is used.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB catalogue; query GET /api/organisms; complete
    returned organism/dataset catalogue; actual accessed_at 2026-11-04T13:18:08.811643Z;
    limit One complete current JSON response; downstream only actual matching biological
    hosts; exact complete returned response only, no broader absence inference.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner attempt 2026-11-03T00:49:00.848907–00:49:00.863225Z
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical PermissionError pyvenv.cfg retained; no fresh runner invocation.
    The current official catalogue fallback has its own actual fetch timestamp.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-isw1_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1_complex.yaml
    --verify
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-verify-receipt.json
    SHA256 090e422f1915f7aa1701113ac30d4e0a9a86fc65acd3a4bbb40ca03770a9d158
  accessed_at: '2026-11-04T13:17:42.974820Z'
  support: supports
  summary: 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-isw1_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1_complex.yaml
    --causal-graphs
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-causal-receipt.json
    SHA256 1e96f1270cf6736c2b11449cc86a454a5da8649e95c4bdf0f994fa8a6d96f071
  accessed_at: '2026-11-04T13:17:43.390518Z'
  support: supports
  summary: 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: e3606d9492412eba7584d15f0b359a7e5845a9b93f368c2bdb8a4f074332af06
- evidence_id: micro-native-isw1a_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1a_complex.yaml
    --verify
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-verify-receipt.json
    SHA256 48d5c2b3bb4d835e89c61f1e43c2e0f0d928880c2f3935e5c190a567ab163d3a
  accessed_at: '2026-11-04T13:17:44.402326Z'
  support: supports
  summary: 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-isw1a_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1a_complex.yaml
    --causal-graphs
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-causal-receipt.json
    SHA256 f8d8b49e7bbab7fd05ec1b9c241289fa03481b44e07193c6137a215327132d81
  accessed_at: '2026-11-04T13:17:44.811804Z'
  support: supports
  summary: 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 850617ab05abf9be586d72f4a3ed65451ddf808e1e501e9b1ba0eb3c7ad2bbec
- evidence_id: micro-native-isw1b_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --verify
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-verify-receipt.json
    SHA256 2e2b643db38b2260389b58403aff5c1be583d18b1bb19a17985674d1b579efac
  accessed_at: '2026-11-04T13:17:45.955516Z'
  support: supports
  summary: 3 maintained reviewed S288C examples and 3 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-isw1b_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/isw1b_complex.yaml
    --causal-graphs
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-causal-receipt.json
    SHA256 af9e274c4664fb41a7304a5cc3fdc5033fff0c5c1d0392414b2d414ea7031016
  accessed_at: '2026-11-04T13:17:46.363151Z'
  support: supports
  summary: 3 maintained reviewed S288C examples and 3 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 0c0bce6fe667636f6e9cc1ecdfdf7e8f0a431f04d7dfc7da15f0cda90ac6517d
- evidence_id: micro-native-ku70_ku80_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --verify
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-verify-receipt.json
    SHA256 aeada98cb98d38f397b5161e7291ccd33a11abaa4ec7f6eb7374bcea59af1cd3
  accessed_at: '2026-11-04T13:17:49.087674Z'
  support: supports
  summary: 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-ku70_ku80_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --causal-graphs
  locator: Actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-causal-receipt.json
    SHA256 1a29d8b6760874bb054c344bf59399dcc9b96b16de0c25472a2d9939fc362844
  accessed_at: '2026-11-04T13:17:49.495826Z'
  support: supports
  summary: 2 maintained reviewed S288C examples and 2 COVERED typed protein nodes.
    Complete actual log inspected; identity/coverage is not biological membership
    or mechanism proof.
  snapshot_sha256: 8298d3326981375e22726968929f402596c518105adec5b93042793f0569ec3f
- evidence_id: micro-isw1-peer-challenge
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/isw1-class-scope-challenge.json
  locator: Independent bounded current class/variant challenge with exact frozen inputs
    and Vary read scope
  accessed_at: '2026-11-04T13:28:34.953651Z'
  support: context_only
  summary: Corroborates a minor internal scope mismatch while rejecting nonhomology,
    generic class or optional example absence as sufficient major-defect grounds.
    No mandatory row split, component type change or extra examples.
  snapshot_sha256: 669238f9f248a697982490ed7c96827a5b055e84a7c21c3e24893697831cb094
- evidence_id: plaque-native-policy
  kind: authority
  reference: docs/CURATION.md; docs/record-review-profile.md; .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen whole-record source applicability, class grounding, formation versus
    function, append-only historical rationale and native review contract; exact used
    inputs separately manifested.
  accessed_at: '2026-11-04T13:33:20.749160Z'
  support: context_only
  summary: Applied native rules without imposing optional inventory or universal depletion
    experiments. Gene/pathway assertions trigger structured-source assessment regardless
    of expression-inference wording.
- evidence_id: plaque-native-schema
  kind: authority
  reference: schema/record_review.yaml; src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen native evidence/assessment/finding enums and graph/record contract.
  accessed_at: '2026-11-04T13:33:20.749240Z'
  support: context_only
  summary: GENE_OR_PROTEIN may represent a protein family/class or complex; source-aware
    NONMECHANISTIC graphs and UNKNOWN formation status are permitted.
- evidence_id: plaque-original-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/original-proof.json
  locator: Actual independent native validate/render of all three originals; historical
    source hashes checked at their declared original revision; YAML/Markdown SHA256
    and byte equality. SHA256 ec87bce8c2a1da2757dc6510d1a633f84e7f28344f42f24efaaa8488ae7b01d4
  accessed_at: '2026-11-04T13:33:20.749319Z'
  support: supports
  summary: All three immutable originals validate and render exactly, and all their
    historical source-input hashes match. LPS and MacAB current target bytes match
    the originals; LolCDE stale delta is separately assessed.
- evidence_id: plaque-t5-record
  kind: record_content
  reference: data/structures/other/lipopolysaccharide_transport_system.yaml
  locator: Complete current record including definition, components/examples, distribution,
    properties, functions, graph, canonical examples, discussions and history; SHA256
    7ce50d437cce77aa049b4340bd3c95899875c156a208e23cb92b38fd4ba0e32e
  accessed_at: '2026-11-04T13:33:20.749328Z'
  support: context_only
  summary: Whole assigned index 5 independently read at exact source f9ac707415c382929b15517997efaa11ec96230d.
- evidence_id: plaque-t5-original
  kind: prior_review
  reference: reviews/structured/20261022T080130Z-lipopolysaccharide-transport-system-audit/review.yaml
  locator: Complete original YAML and canonically identical Markdown; exact original
    proof above.
  accessed_at: '2026-11-04T13:33:20.749331Z'
  support: context_only
  summary: Original review 20261022T080130Z-lipopolysaccharide-transport-system-audit;
    original findings independently reassessed, with historical source and access
    assertions kept historical.
- evidence_id: plaque-native-lipopolysaccharide_transport_system-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-verify-receipt.json
  locator: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lipopolysaccharide_transport_system.yaml',
    '--verify']; receipt SHA256 d8dd31312e9a9d8c1ce5cf08e3f96dbe9a92e1e7eee2fa03a85939f12b7d13ee;
    actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T13:17:50.665378Z'
  support: supports
  summary: Exit0 at source head. Independently inventoried 7 reviewed examples; 7
    typed nodes COVERED. Verification covers identity/xrefs, not scientific participation,
    family exactness or universal assembly necessity.
- evidence_id: plaque-native-lipopolysaccharide_transport_system-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-causal-receipt.json
  locator: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lipopolysaccharide_transport_system.yaml',
    '--causal-graphs']; receipt SHA256 68e17a0aca56ab7ba11f455e314749b5a61e63ce43520e1f9f2526ae5c36b6ca;
    actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-causal.log
    SHA256 22dc6e5a43f3ee651b4ba14ac6c41138867d16abc99858e2a217188e2a4a2c83
  accessed_at: '2026-11-04T13:17:51.081915Z'
  support: supports
  summary: Exit0 at source head. Independently inventoried 7 reviewed examples; 7
    typed nodes COVERED. Verification covers identity/xrefs, not scientific participation,
    family exactness or universal assembly necessity.
- evidence_id: plaque-t6-record
  kind: record_content
  reference: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
  locator: Complete current record including definition, components/examples, distribution,
    properties, functions, graph, canonical examples, discussions and history; SHA256
    96bf1ce75ce606af29c2d8a549c345e9487f0e426ac1f86823f14db22c651866
  accessed_at: '2026-11-04T13:33:20.749552Z'
  support: context_only
  summary: Whole assigned index 6 independently read at exact source f9ac707415c382929b15517997efaa11ec96230d.
- evidence_id: plaque-t6-original
  kind: prior_review
  reference: reviews/structured/20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit/review.yaml
  locator: Complete original YAML and canonically identical Markdown; exact original
    proof above.
  accessed_at: '2026-11-04T13:33:20.749554Z'
  support: context_only
  summary: Original review 20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit;
    original findings independently reassessed, with historical source and access
    assertions kept historical.
- evidence_id: plaque-native-lolcde_lipoprotein_abc_transporter_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-verify-receipt.json
  locator: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml',
    '--verify']; receipt SHA256 bf3e150b5ad894bc9f1fab13d0abaebd5d5dc5e4b581405c5666645c3f6270ec;
    actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T13:17:52.213869Z'
  support: supports
  summary: Exit0 at source head. Independently inventoried 3 reviewed examples; 3
    COVERED typed constituents plus 1 substrate UNANCHORED_WITH_UNIPROT carrying Lpp/Pal.
    Verification covers identity/xrefs, not scientific participation, family exactness
    or universal assembly necessity.
- evidence_id: plaque-native-lolcde_lipoprotein_abc_transporter_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-causal-receipt.json
  locator: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml',
    '--causal-graphs']; receipt SHA256 5501faf803afe3f763eb166c3754e496912e4e4734426f67782d58ab04c5a323;
    actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-causal.log
    SHA256 ec1f04f331b7a6dece930cf0d7b4799eb610cbbca2f0af475f09083aa4c4a241
  accessed_at: '2026-11-04T13:17:52.620167Z'
  support: supports
  summary: Exit0 at source head. Independently inventoried 3 reviewed examples; 3
    COVERED typed constituents plus 1 substrate UNANCHORED_WITH_UNIPROT carrying Lpp/Pal.
    Verification covers identity/xrefs, not scientific participation, family exactness
    or universal assembly necessity.
- evidence_id: plaque-t9-record
  kind: record_content
  reference: data/structures/other/macab_tolc_complex.yaml
  locator: Complete current record including definition, components/examples, distribution,
    properties, functions, graph, canonical examples, discussions and history; SHA256
    b2f794251b4bbc18fa1e7c1bdc93d9fc0098d20d1160e8230ee4b0a9b247e636
  accessed_at: '2026-11-04T13:33:20.749722Z'
  support: context_only
  summary: Whole assigned index 9 independently read at exact source f9ac707415c382929b15517997efaa11ec96230d.
- evidence_id: plaque-t9-original
  kind: prior_review
  reference: reviews/structured/20261022T080133Z-macab-tolc-complex-audit/review.yaml
  locator: Complete original YAML and canonically identical Markdown; exact original
    proof above.
  accessed_at: '2026-11-04T13:33:20.749723Z'
  support: context_only
  summary: Original review 20261022T080133Z-macab-tolc-complex-audit; original findings
    independently reassessed, with historical source and access assertions kept historical.
- evidence_id: plaque-native-macab_tolc_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-verify-receipt.json
  locator: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/macab_tolc_complex.yaml',
    '--verify']; receipt SHA256 aedfa789d115b849c5373dd04a79b2955c9952c28c560f6917421961c53a53a6;
    actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T13:17:56.780972Z'
  support: supports
  summary: Exit0 at source head. Independently inventoried 3 reviewed examples; 3
    typed nodes COVERED. Verification covers identity/xrefs, not scientific participation,
    family exactness or universal assembly necessity.
- evidence_id: plaque-native-macab_tolc_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-causal-receipt.json
  locator: Command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/macab_tolc_complex.yaml',
    '--causal-graphs']; receipt SHA256 6916caf9407ca7f05c2309ce1354ef05594e54e375db4583d1e8a52cceb5b564;
    actual log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-causal.log
    SHA256 404a309417e082e13a78e994b12da77302a38ee7f6546a78f8f98b0a9743e762
  accessed_at: '2026-11-04T13:17:57.195842Z'
  support: supports
  summary: Exit0 at source head. Independently inventoried 3 reviewed examples; 3
    typed nodes COVERED. Verification covers identity/xrefs, not scientific participation,
    family exactness or universal assembly necessity.
- evidence_id: plaque-PMC2851745-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2851745/
  locator: 'Genuine primary body sections2,3,4,7,10: LptD/E purification and biochemical
    characterization, conditional plug/barrel alternatives in Discussion; source does
    not present the later demonstrated architecture. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-legacy.raw
    SHA256 53a39228d92aff6d6d776343950fa2b80ced9fcc0aafbfe22fa607503ea4deb8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-legacy.receipt.json
    SHA256 5412a9060ee677015ca48fb7b5a2e6cf4367cedcd6e400f8aca469be361fa338'
  accessed_at: '2026-11-04T13:21:43.404184Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-PMC3038725-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3038725/
  locator: 'Genuine primary body sections2,4,5,Discussion SEC2 and section10: LptE-LptD
    contact mapping/photocrosslinking and mutant analysis; supports later buried plug
    model, not an atomic structure. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-legacy.raw
    SHA256 4bf892fc7b163ae5662df02d3e18ea32eee2515cfdf4f7e2ed4de14eb5887895; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-legacy.receipt.json
    SHA256 c75a613cf33e050e121a4f55d225a1fe2fca3b02ce02f8afc7f36a68984154cb'
  accessed_at: '2026-11-04T13:21:43.405206Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-yakushi2000-pdf
  kind: validation
  reference: https://www.nature.com/articles/35008635.pdf
  locator: Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-pdf.raw
    SHA256 8ed2bbedd7f13cb850b9ec216fc9bd2ad87e8059170b70d2454bdf5a5ff12121; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-pdf.receipt.json
    SHA256 af5aa27c907d2f87e16c44b93c209eae92be65b36466ac80f519f9569b8662c9
  accessed_at: '2026-11-04T13:21:43.407547Z'
  support: context_only
  summary: 'Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather
    than PDF. Successful alternative routes are independently tiered.'
- evidence_id: plaque-yakushi2000-publisher
  kind: validation
  reference: https://www.nature.com/articles/35008635
  locator: Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-publisher.raw
    SHA256 8ed2bbedd7f13cb850b9ec216fc9bd2ad87e8059170b70d2454bdf5a5ff12121; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-publisher.receipt.json
    SHA256 e0e72df4ad10821e89e9ff536c7fccf76f873f098f7aced6d506e6eeaafd214f
  accessed_at: '2026-11-04T13:21:43.408592Z'
  support: context_only
  summary: 'Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather
    than PDF. Successful alternative routes are independently tiered.'
- evidence_id: plaque-query-lptA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptA.raw
    SHA256 e97a531c6792ce399e4ff13718c26ef6b8492357f54d130230c72afcb8fb0b19; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptA.receipt.json
    SHA256 4e8f709af44eb71540969978e98f784adcf951185146cff98c76d1cb81aceb13
  accessed_at: '2026-11-04T13:21:43.409123Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptA AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lptB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptB.raw
    SHA256 50c80c40179588c0cbda5e9914674e3561dd3f52fd1de12dec341b827da48bcc; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptB.receipt.json
    SHA256 978f950d1657751b9aba636336256262fb1c4211381c32b7144f965287bcb003
  accessed_at: '2026-11-04T13:21:43.410558Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptB AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lptC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptC.raw
    SHA256 9275ea8f055bff383cda815a15b30587451b4228aa8a12dcbb6441316600d41c; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptC.receipt.json
    SHA256 6794dddeb11983b0d2314309f8bc77c7165efb6b8334870fdba1915c359d693f
  accessed_at: '2026-11-04T13:21:43.412681Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptC AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lptD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptD.raw
    SHA256 1cefffb7d372496094e05d2fcba958a834d1b35316006f0c3e13d60d143c15e5; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptD.receipt.json
    SHA256 36dca3ba88de8b15661390c0bd951c8e331290e33757dd7816e5d92d0ef59ec7
  accessed_at: '2026-11-04T13:21:43.827841Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptD AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lptE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptE.raw
    SHA256 c335b8cad051a875c24d87fa500eab861f2656e511ac7164d0a6664830daeef4; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptE.receipt.json
    SHA256 c05068f6f4bf194e3dec6113930fad1f10d869bcf645a0d19cbdafdc780321de
  accessed_at: '2026-11-04T13:21:43.854428Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptE AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lptF
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptF%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptF.raw
    SHA256 d5933058a3cccc7ee4679d7043e63990578d827ba058fe21f9f8d01b3de57f23; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptF.receipt.json
    SHA256 cb413910d13cee29f97cc97db272eeb076ca7bcd5e4690662466eb5d76a801b6
  accessed_at: '2026-11-04T13:21:43.884751Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptF AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lptG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlptG%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptG.raw
    SHA256 664f7d12805970dcb311daba5feb97624ef8d394464edc55edfc90b0f4f6f177; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lptG.receipt.json
    SHA256 a27d4a0e78753881e34ebb6ee5ee1ea42a326c568a66ad8b70017db9d95882df
  accessed_at: '2026-11-04T13:21:44.249823Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lptG AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lolC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolC.raw
    SHA256 24e5e117fdd695734205da1b44dfbece3dfb1c69250abab110a2b53502aa67ad; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolC.receipt.json
    SHA256 71218d8fc34369f969499f42d7e538c5075f5cf3bf8ad9cd8ad883016cbba27a
  accessed_at: '2026-11-04T13:21:44.258750Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lolC AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lolD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlolD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolD.raw
    SHA256 6301389cebcd2127dda9ededfdb40589c9f7ea17c64bc3d413420d858ca726f2; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolD.receipt.json
    SHA256 f667a9eccbd1672b2f15242d88a189229fca37085580cecc9bcee6f748e24346
  accessed_at: '2026-11-04T13:21:44.593995Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lolD AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lolE
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AlolE%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolE.raw
    SHA256 7116f3a87e7c09a2364fe937867b284c48682d6c1262adaec07f9c8c14df4ae2; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lolE.receipt.json
    SHA256 ef5bb049a835c0b06249bb81d5504b4b0687b10a7cb83739d0e8b908519f1dae
  accessed_at: '2026-11-04T13:21:44.616430Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lolE AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-lpp
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Alpp%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lpp.raw
    SHA256 7b371f7303c4e13f128bbc6283474ddfbd5ad36128fccf593aad138328796920; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-lpp.receipt.json
    SHA256 032e3279ff4256b7565d2b6c5b2283f0e14e4f2ce7b7bbb8ccadff6c033962cf
  accessed_at: '2026-11-04T13:21:45.033761Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:lpp AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-pal
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Apal%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-pal.raw
    SHA256 4a942cc3f3a596e061c83696017ce27acbe5fd0a32c90e69a5988ab4a8a72ec1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-pal.receipt.json
    SHA256 5ec22da045ba3137940ce0a0a21c5ab897197277122c924f585d4bc5db7c351b
  accessed_at: '2026-11-04T13:21:45.134402Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:pal AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-macA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmacA%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macA.raw
    SHA256 27c0caf5770fe21cab614b751a0d12c0e15448ed3ce1ab11bfe27f8415b4aa90; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macA.receipt.json
    SHA256 ca1a931f4da10e6286aa936fd19a61ceb8cf8af35d68c36d200982a9935f3a71
  accessed_at: '2026-11-04T13:21:46.037017Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:macA AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-macB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AmacB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macB.raw
    SHA256 b499c3c03b744afbc926cfa35dd5af14d32141a991b2631a270aeb4e941f7259; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-macB.receipt.json
    SHA256 b36277796d44eb8f5a76ba5d2e0c84598f41c56cbe372118b2a0066000dd91b2
  accessed_at: '2026-11-04T13:21:46.160363Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:macB AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-query-tolC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AtolC%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Full returned current UniProt reviewed exact-gene taxon83333 query, size500,
    one result; exact URL retained. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-tolC.raw
    SHA256 3e284eede466d8aa6d6eac091b434ce033083e18848c220476a3bdb06463365a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/query-tolC.receipt.json
    SHA256 90041b167ae727a647725a57456702a0b4c45a44e6e2632e8e3f502f65371537
  accessed_at: '2026-11-04T13:21:47.125733Z'
  support: partial
  summary: Exact native K-12 accession selection corroborates the record reference,
    without proving complex participation.
  search_scope: UniProt REST, query gene_exact:tolC AND organism_id:83333 AND reviewed:true,
    size500; full returned result list inspected, one entry. Not exhaustive over other
    taxa or unreviewed proteins.
- evidence_id: plaque-adapter-module-22
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22.raw
    SHA256 75c93e893c864c0c0a515a7fb566fa97ed84141f008da563c9174b27e41e2703; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22.receipt.json
    SHA256 5627aef36d82d0c9fb57cfbeafe2a2e0dc2ca53bd6472ef198a52be9b399a961
  accessed_at: '2026-11-04T13:22:47.689851Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/imodulons/e_coli/precise1k/22;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-module-22-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22-genes.raw
    SHA256 6e779e25e705f68403277aa34683af16a8dddfd4dc5fbe96fb6bdfc7117e20f0; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-22-genes.receipt.json
    SHA256 7adacf5ec076e6a64fcfd443db3494aa542071535554c94ad9d41b456badfabc
  accessed_at: '2026-11-04T13:22:47.690870Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/imodulons/e_coli/precise1k/22/genes;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-module-45
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/45
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45.raw
    SHA256 12f2886fe517f3015a3855554588553d6f3bf4e12a11cc4877ecadb00133064b; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45.receipt.json
    SHA256 3b5b14ecee432f8eaadf907e41d9a801aa199567f1293fd8dea8a7beeb34e685
  accessed_at: '2026-11-04T13:22:47.691101Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/imodulons/e_coli/precise1k/45;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-module-45-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/45/genes
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45-genes.raw
    SHA256 d32d1ee58b1768cada05d6a326fb8012e5a7a8d5e4ae5f3e9cd373375046a920; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-45-genes.receipt.json
    SHA256 85312eb725b480d1c9ea4fda02364e9345f846b5c5345a406022e150d3e867f8
  accessed_at: '2026-11-04T13:22:47.692255Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/imodulons/e_coli/precise1k/45/genes;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-module-167
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/167
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167.raw
    SHA256 49c7e478867c20e407e8929c8a92872f8eeb679c4a835f5344b90ba5bad34292; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167.receipt.json
    SHA256 553da6411cc1fdb119be9f92d835d29b7e7b7ef789fd804cec2bf35a5a5cd5d1
  accessed_at: '2026-11-04T13:22:47.693562Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/imodulons/e_coli/precise1k/167;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-module-167-genes
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/167/genes
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167-genes.raw
    SHA256 cd9b96081fad9fd906870f03c736d6a152bb04c3927ad7c4c910a5b5884c69fb; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-module-167-genes.receipt.json
    SHA256 05f99ced53e58fce50b9bc6751c378e2c91450afc1e46419c4062af24c6752f8
  accessed_at: '2026-11-04T13:22:47.694750Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/imodulons/e_coli/precise1k/167/genes;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-yakushi2000-canonical-pdf
  kind: validation
  reference: https://www.nature.com/articles/ncb0400_212.pdf
  locator: Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical-pdf.raw
    SHA256 fe5a7dc76ae9624ea65eb8f73983d456b2f31ec535aebdfb0500b4b6803eddaa; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical-pdf.receipt.json
    SHA256 08dabf55516660dbc1ba83714312145e412a258f73fbea6a5595f389d774341e
  accessed_at: '2026-11-04T13:23:04.661664Z'
  support: context_only
  summary: 'Failed or non-body route: HTTP 200; canonical PDF route returns HTML rather
    than PDF. Successful alternative routes are independently tiered.'
- evidence_id: plaque-yakushi2000-canonical
  kind: database
  reference: https://www.nature.com/articles/ncb0400_212
  locator: Publisher title/authors/DOI and displayed abstract/figure navigation only;
    body paywalled. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical.raw
    SHA256 afab2528b5e4dce9ddba497f7d3d1b586aee55a62f97517953cc81dbba99d84d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-canonical.receipt.json
    SHA256 bf72a3fa007450e3bfd420fca29897f060f7e3dd133cf820df3d47f0b3a27678
  accessed_at: '2026-11-04T13:23:04.662673Z'
  support: context_only
  summary: Correct canonical article route; abstract is separately captured by PMID10783239.
    No full-body inspection claimed.
- evidence_id: plaque-go-0062051-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0062051/ancestors?relations=is_a
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051-ancestors.raw
    SHA256 d1a97376dc80e450241fd90f2c148c4b6f9ba36e4fce3d1b452dd9cae3d92e52; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051-ancestors.receipt.json
    SHA256 159808725427186c59600b1a8a920fceb067b1c3bde17339895ffa8244fe576b
  accessed_at: '2026-11-04T13:23:04.664283Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-1990196-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990196/ancestors?relations=is_a
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196-ancestors.raw
    SHA256 8120216524da941cc23167cd8a5283877080de1a2b8bf55aefb4402972dd977b; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196-ancestors.receipt.json
    SHA256 f06079e516998f3abe93d623292508af4ae8572ab3e0148b932b4688ebe0a875
  accessed_at: '2026-11-04T13:23:04.664459Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-protein-P0ADV1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ADV1.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV1.raw
    SHA256 a49f57f247687a374446fcfe0d6b33e53ea8060af935201b1d8e588c245901e7; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV1.receipt.json
    SHA256 735cca2df2ca115818516622615c8978cb9d111e34eee9447b46ea1272c12b54
  accessed_at: '2026-11-04T13:20:57.358154Z'
  support: partial
  summary: P0ADV1; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0A9V1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A9V1.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A9V1.raw
    SHA256 a539dccc2f9371777cda184328fdbdf0ea913901bb0a4f8be9973ccb28e38a07; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A9V1.receipt.json
    SHA256 350d59ce0dce916c67063d79eef5a65be854960f39121eb90731f0c774f070aa
  accessed_at: '2026-11-04T13:20:57.359260Z'
  support: partial
  summary: P0A9V1; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0ADV9
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ADV9.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV9.raw
    SHA256 53d4861aae4b0c63f0442dabafde093c6df6d2ed831df1b48bff73b6717d2e4f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADV9.receipt.json
    SHA256 3ee2a8d4569fd9e17b0036d8f8b19d9f9468397e8367704bb2f01598cbd437fa
  accessed_at: '2026-11-04T13:20:57.360197Z'
  support: partial
  summary: P0ADV9; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P31554
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P31554.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P31554.raw
    SHA256 dbab992a253dc68cd2b7543da5236b46111557f1f37b9fdd619b4b81794bf178; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P31554.receipt.json
    SHA256 381b55600d11346282e2f6b6b6a327594e78bd8e781dedb1d34603ae31fc1fd7
  accessed_at: '2026-11-04T13:20:57.361422Z'
  support: partial
  summary: P31554; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0ADC1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ADC1.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC1.raw
    SHA256 70872174ddd7695d30b349af2863fe0f5d9c5f83f387200cbf6f8da40d459a90; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC1.receipt.json
    SHA256 54971d0fee5d1123acba92b87bf3e99587f260f9c47962eb86c26911d50c84d8
  accessed_at: '2026-11-04T13:20:57.362297Z'
  support: partial
  summary: P0ADC1; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0AF98
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0AF98.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0AF98.raw
    SHA256 a4fd62e77373d82751c493c32e954a4a935cecb2c8d43d2a357743077dd5c3c4; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0AF98.receipt.json
    SHA256 54342bdd6ca1f3d74066c457a491fdae0a738c34c55c47d11bb838b10f7ed096
  accessed_at: '2026-11-04T13:20:57.363502Z'
  support: partial
  summary: P0AF98; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0ADC6
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ADC6.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC6.raw
    SHA256 20aa3222eec43cbb1782775b815c3b69549e897e0cfcc81d7556732e6cb2f5bc; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC6.receipt.json
    SHA256 1190b248eaa9e9253d66aafc8d48386e27d0de2e7b84bfb614dabf3388660b92
  accessed_at: '2026-11-04T13:20:57.365115Z'
  support: partial
  summary: P0ADC6; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0ADC3
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ADC3.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC3.raw
    SHA256 a9b53bf112c3ddac173aa28de70bab78e43ff7104a2b4e33f32ffcc337527470; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0ADC3.receipt.json
    SHA256 d5227f3103d78ed248cf41d5fdd7d7d2ba5f33d081726d1b869a6528334c48eb
  accessed_at: '2026-11-04T13:20:57.365312Z'
  support: partial
  summary: P0ADC3; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P75957
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P75957.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75957.raw
    SHA256 4a90a4d028ffd3b16115b94edd516cb4b88e9a9ba1e1d667e5cb3851fb333e4d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75957.receipt.json
    SHA256 c11e571ef1040ee01e4d328234c1fa72aa5bd70b227253c51de4bbd823fa3300
  accessed_at: '2026-11-04T13:20:58.006992Z'
  support: partial
  summary: P75957; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P75958
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P75958.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75958.raw
    SHA256 d90ee551682661d6bd97c04e3a399814bacec9688257988b268467314b152459; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75958.receipt.json
    SHA256 26913d6564d2410e01f75e6204ba96a98748d1a7910698cd4b96d4cec2a84f93
  accessed_at: '2026-11-04T13:20:58.110489Z'
  support: partial
  summary: P75958; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P69776
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P69776.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P69776.raw
    SHA256 ad352c7a4cde4709f826a28fe7021076ca97a53582236f32ec60d3dd4846e6bd; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P69776.receipt.json
    SHA256 72557ad3d133bee226f2e6513505dce6b0f06f7069a82d3ea19b950f2cbe28ba
  accessed_at: '2026-11-04T13:20:59.066109Z'
  support: partial
  summary: P69776; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P0A912
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A912.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A912.raw
    SHA256 93a07fedc75dfc2a7729de1128fd5d4eb22bfb376d5251a6419446c2cffc42fa; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P0A912.receipt.json
    SHA256 034efcfcd0a08ccb74542350f8753521fd3fb1a2b9dea20b24c8031db9eb9091
  accessed_at: '2026-11-04T13:20:59.268805Z'
  support: partial
  summary: P0A912; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P75830
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P75830.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75830.raw
    SHA256 0465a58120398458818561f76d7fc68cdaa56d02690ab95f7ca5f730656067a4; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75830.receipt.json
    SHA256 d4486d0efe6282eb2f297a2fdc694ee3a2bdf08f1f6d46d227fe871a030d50bf
  accessed_at: '2026-11-04T13:20:59.981279Z'
  support: partial
  summary: P75830; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P75831
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P75831.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75831.raw
    SHA256 544d28caf979f42b50802e05fe332a5350cb8ba79df24df0002874c3ef36ce42; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P75831.receipt.json
    SHA256 443bea708a97d7d0f04e5a623351160d8f90156186d417dcb36cdbf290402bb5
  accessed_at: '2026-11-04T13:21:00.192594Z'
  support: partial
  summary: P75831; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-protein-P02930
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P02930.json
  locator: Current accession/status, protein and gene names, taxon, SUBUNIT/FUNCTION/localization
    comments and exact family cross-references read; bibliographic annotations are
    not fresh paper-body reads. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P02930.raw
    SHA256 cef14f6af1999fe0b5218d959cca8788ec00afc1b145201ba48344a4b15bbb04; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/protein-P02930.receipt.json
    SHA256 a1299f0ab8dce3aade2529833872b903adb9ae28448c83578a0761559603499a
  accessed_at: '2026-11-04T13:21:01.103726Z'
  support: partial
  summary: P02930; UniProtKB reviewed (Swiss-Prot); taxon 83333. Identity is distinct
    from direct participation/localization/necessity evidence.
- evidence_id: plaque-family-IPR014340
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014340/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR014340.raw
    SHA256 0771d28efa0d43eb3d035c9a2bfe493df3bb92162384988fe8dc6eb3cab22526; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR014340.receipt.json
    SHA256 315517166ba024faff5052a20f8d5d4d4542788b372967923e2f8e61ace262eb
  accessed_at: '2026-11-04T13:21:01.216539Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR030921
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030921/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030921.raw
    SHA256 3c2d08b1686549651ee7093273649dded7908b349a60b40e45567fdf432e2924; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030921.receipt.json
    SHA256 ef9cebd32377c7ffee7993684f97da3bbc22abc45e66590dbd338140424a29e8
  accessed_at: '2026-11-04T13:21:02.098989Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR026265
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026265/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR026265.raw
    SHA256 e13a5fb3ce284814ce35a6385238428b8b3a64eefe2b790a2550f446dff31c41; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR026265.receipt.json
    SHA256 ccf1de0c93a0588b67955ef7a0acc95901571049ae13e51aacc42ade3372787f
  accessed_at: '2026-11-04T13:21:02.099070Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR020889
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020889/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR020889.raw
    SHA256 012318b2911e0a9d11b42b5289e9b0051b4a9cfd6c59fc6c2a091b35642a2bf5; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR020889.receipt.json
    SHA256 82fc410eaf2a997d38e06768bc534354f713117274348c1216be05a454c13b62
  accessed_at: '2026-11-04T13:21:02.446418Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR007485
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007485/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR007485.raw
    SHA256 6ae7a373d99ee781c3000e39974e66fd76e6a9c81d478e98c9bd4cb08d3d0669; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR007485.receipt.json
    SHA256 ac4a5a293112df221a1da3a6d0e921c23ac958d5a9ab88d8dd2a1ad6c70cc9c9
  accessed_at: '2026-11-04T13:21:03.162204Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR030922
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030922/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030922.raw
    SHA256 64c715c496a528e693830567cc118b2b2fad20562374f2e3cb033d21a8d37863; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030922.receipt.json
    SHA256 c03626b81806664cda8399c81918c7c8c89e00e8a754e0da9361a133c70be917
  accessed_at: '2026-11-04T13:21:03.162261Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR030923
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030923/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030923.raw
    SHA256 3a6f425a6e6e4697c474a88abab19320ffe52dafbfdfcbb3d2b6d9402693f8e8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR030923.receipt.json
    SHA256 898726ae0ef2f5627e85fea3e4d47fac4bff428ec508a542befb41d8befe45db
  accessed_at: '2026-11-04T13:21:03.226368Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR011924
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011924/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011924.raw
    SHA256 43f64974d9b0c477d5e3e6fb416e9a35d79e2322428fe780481bdf2937eb6bef; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011924.receipt.json
    SHA256 b91f79e22df14a0818f91574be3df9078912f199dac2228b7c5ec0b1b0c024c6
  accessed_at: '2026-11-04T13:21:03.481378Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR011925
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011925/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011925.raw
    SHA256 efb3b57d6da640ce7de3071f41d7a161baad0daabd7b09521086ce41a6467216; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR011925.receipt.json
    SHA256 3d6da573ee25c05ba68f1362035ab65a17cc044436a354e29ee0910d9f3a8b7b
  accessed_at: '2026-11-04T13:21:03.655290Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR015854
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015854/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR015854.raw
    SHA256 272d9a8c0574e7444f45a89946d06ba7730f9113cf8f157862f10bd4440c6640; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR015854.receipt.json
    SHA256 4004999076bd937be6d235b9a4ce4a92c56c10ecf0de54978aa7a1ed11970f09
  accessed_at: '2026-11-04T13:21:03.955031Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR058623
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058623/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058623.raw
    SHA256 d3ed15d36e942a9a5ab5ef5d0f6538ae597d289bf7747c7ac54c91f400418ce8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058623.receipt.json
    SHA256 ac490605aeb2024b516f7789c33dfaf4c92c2357b8f07e28dce94dfb39be3e5b
  accessed_at: '2026-11-04T13:21:04.033045Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR050250
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050250/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR050250.raw
    SHA256 0446bff126f9f98bdb8ce3b393de25b559ab55bd88ea2a207353dcb3bad360fc; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR050250.receipt.json
    SHA256 cc80e476b515d66197e8d5266bdcdcdce90d3b52b959f25b8d28faf74925b9be
  accessed_at: '2026-11-04T13:21:04.081956Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-IPR058622
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR058622/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058622.raw
    SHA256 d3c58cbb9737d5f395f703b634f84df048f355555af2b817f321a5e474b8e310; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-IPR058622.receipt.json
    SHA256 cc35af549b0dd15fa314a3850a322c5a2bb67223c7246601acc42c7c1ba1ad31
  accessed_at: '2026-11-04T13:21:04.086902Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-NF008076
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008076/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008076.raw
    SHA256 25245b083fe05c65934c02caa3000a91071ccc8d9ce8f9a86e51bf8578f0e467; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008076.receipt.json
    SHA256 730b223b54da0adb3e11118e021a87b1c0dd85392ab1f125c5ff57a072ae7c7b
  accessed_at: '2026-11-04T13:21:04.276092Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-family-NF008357
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008357/
  locator: Exact native family identity/type/signatures and description compared with
    independently retrieved example membership; broader near misses retained as comparison.
    Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008357.raw
    SHA256 a190a0b893efd7e75bb191ecf35d6ba381aaa3a04aecc1e6045abfcf13ac79c6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/family-NF008357.receipt.json
    SHA256 bbfa1eb28eb46c501022c629876049b2752adb2f7663e22c8422376ec8801159
  accessed_at: '2026-11-04T13:21:04.800811Z'
  support: partial
  summary: Exact named-family grounding support; no family accession guessed. IPR050250
    generated descriptive prose is excluded from biological support.
- evidence_id: plaque-go-0062051
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0062051
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051.raw
    SHA256 52502a08c75622abe3dc387b50b0b7e01323f6bbc655256799048936462640e3; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0062051.receipt.json
    SHA256 d592ed8132b85a2d5ebd8fdb5999c90393adc996e020f666db12637f826cbbfa
  accessed_at: '2026-11-04T13:21:05.004266Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-1990351
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990351
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990351.raw
    SHA256 f612331f15ccd63723f76f6a394d4cd84d5833db64d78e82319774733c56cd36; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990351.receipt.json
    SHA256 b0327ae25666d694c2a3cc6d386e2e8670e0c4cb6d2076550164dffaaf02d45d
  accessed_at: '2026-11-04T13:21:05.107718Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-0043190
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043190
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0043190.raw
    SHA256 ca3b015a4fa8bef4ab9830aa639f3f99f7484b37f26120ed6070d2c25c4c631f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0043190.receipt.json
    SHA256 19decd325f75e69e8f1d6a938533e04d343ed0dc50c624dcdbc3037e89c6d857
  accessed_at: '2026-11-04T13:21:05.312580Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-0140306
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0140306
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0140306.raw
    SHA256 9c6e222a03f9e8290b4c3e88611f726a08a958bfd5e0c96105206f9d6c8b2c0d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0140306.receipt.json
    SHA256 527e14e7c2bb515812979321d93694103687709fe2d598551889cae352cc2b1c
  accessed_at: '2026-11-04T13:21:05.312636Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-0044874
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044874
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0044874.raw
    SHA256 abf1bc52e1fd40de4725ecce9516ceef0f3aa3193f017f0ea7ef6b093a1275d5; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0044874.receipt.json
    SHA256 e161f8dbd24d6c96544055d22f296f0a1569b3c4db3fa3df1b3ed9271c03bff1
  accessed_at: '2026-11-04T13:21:05.517949Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-1990196
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990196
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196.raw
    SHA256 4bdbc0587807f14fd6b3786bdff2da82d5aa346bd4d9efffed645b06fe2b4bc6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990196.receipt.json
    SHA256 8bef84fc08ea04fd34d937fb257711720fc18a169ebfed49b7fd6741502a7bc4
  accessed_at: '2026-11-04T13:21:05.608078Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-1990195
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990195
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990195.raw
    SHA256 5bd952f4607139605c8ff33e27d0d9470cc7d178d0e6ec365e72672d36738247; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-1990195.receipt.json
    SHA256 04dc4c52bc30c26f3823ed10ae0ab10de3ef983d567c1ba4cb7a21f620da398a
  accessed_at: '2026-11-04T13:21:05.770752Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-go-0008559
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0008559
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0008559.raw
    SHA256 55c2744a45c0c938e020c79e6acd9dd866d8bf3fa789c12821b21e33a4a5658f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/go-0008559.receipt.json
    SHA256 6e645c702960b7887ef99b75bf81964e5188fcf954020ac1d1ddd970328e29d2
  accessed_at: '2026-11-04T13:21:05.905514Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-2.raw
    SHA256 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-2.receipt.json
    SHA256 11b633598c38185d9b39f6d8fa2057a96e640417b8c093b7f013af382fc6c03a
  accessed_at: '2026-11-04T13:21:05.908628Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-562.raw
    SHA256 ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-562.receipt.json
    SHA256 3429206222ca129427834f9bb61bd372a012f08a57d99a283b8b99a2fc9338d6
  accessed_at: '2026-11-04T13:21:06.039798Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Native source response identity and relevant annotations inspected. Snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-83333.raw
    SHA256 f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/tax-83333.receipt.json
    SHA256 5ac7317f3954e4c4989d12700d6afeb9d097f77ecb494ae3169c80bb31a76ada
  accessed_at: '2026-11-04T13:21:06.048254Z'
  support: partial
  summary: Bounded authority evidence; scope limited to the exact accession/term/record
    response.
- evidence_id: plaque-cpx-4262
  kind: authority
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-4262
  locator: 'Complete native CPX-4262 response: participants, counts, bioRoles, taxon,
    functions/properties and physical-interaction evidence type. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/cpx-4262.raw
    SHA256 74344dc561706cb864458e9d5e36b05c487d1a6633b2cc379f9761f79819b48c; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/cpx-4262.receipt.json
    SHA256 848b87bb0b4ab7a99007f5080926ff1f48b089615f54382e67bad5428ad2008e'
  accessed_at: '2026-11-04T13:21:06.210001Z'
  support: partial
  summary: Explicit LolC1:LolD2:LolE1 and heterotetramer. LolD enzyme; LolC/E unspecified
    bioRole. No deletion-essentiality annotation inferred.
- evidence_id: plaque-pdb-7MDY
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/7MDY
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY.raw
    SHA256 dfe61154e5964c515f6da17c9f088704793731a4a5ca927366456049a5484392; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY.receipt.json
    SHA256 8ef49cf9abe15ba5f9eff3e548aeb54e3da154e1155e1c13107ccf7230a2bd4c'
  accessed_at: '2026-11-04T13:21:06.317498Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-7MDY-assembly1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/assembly/7MDY/1
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-assembly1.raw
    SHA256 f36d97824690e5893d5685e056bf423569429b20139a3f4b4b7092af70ec4d35; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-assembly1.receipt.json
    SHA256 002468867a1f46a946d0946c20e77d91468cd6c405169414e3b13e54fdd1473f'
  accessed_at: '2026-11-04T13:21:06.319760Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-7MDY-entity1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7MDY/1
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity1.raw
    SHA256 6f085339a88c34e05cd541bdd24dfca4f770270c7a0471249232c76ffdcabd52; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity1.receipt.json
    SHA256 789b35146752259fff0a6637c61d4278f36114d8031a3f29c8181fd1d622592c'
  accessed_at: '2026-11-04T13:21:06.385748Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-7MDY-entity2
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7MDY/2
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity2.raw
    SHA256 6acbe7ff63acbbbcaef6133c374e3ff7a70029cd06b83b1c25d46ab7322cffc8; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity2.receipt.json
    SHA256 99bfc1841f8b47937835fed6c2c741b5054cc5570ea07ebbd5892e7b8387632d'
  accessed_at: '2026-11-04T13:21:06.404177Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-7MDY-entity3
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/7MDY/3
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity3.raw
    SHA256 8da9d569fe05bd755b5539fad5739e59820ab975cefe4f5fe3b140c67005b0b9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-7MDY-entity3.receipt.json
    SHA256 8fd259da240f5e79b9758ec0eed3ae815d56ec1731c1cbc3f6ab8d648fa8e285'
  accessed_at: '2026-11-04T13:21:06.404234Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-5NIK
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/5NIK
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK.raw
    SHA256 d2799b6484764d471a1ce9763e705aede07783c33badce15004e594d5d443be9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK.receipt.json
    SHA256 7968fba2a2be6b3d124d2cddeb252f3bef80537e210368ded53020428da048a6'
  accessed_at: '2026-11-04T13:21:06.476812Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-5NIK-assembly1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/assembly/5NIK/1
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-assembly1.raw
    SHA256 07d19775fead4956f862ae07ba21095603eb223cd94d349391187ab37af99776; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-assembly1.receipt.json
    SHA256 c1a183a342a5c6f61df0f4b58621a91b34da09c6a581f69d131d021c1bb0f469'
  accessed_at: '2026-11-04T13:21:06.495900Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-5NIK-entity1
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5NIK/1
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity1.raw
    SHA256 fa2589b36968f01f3d04b0c2b02188f0b9b566629d8c8d6cdd9957a15ba8ea30; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity1.receipt.json
    SHA256 cbc3d658845d67a2302dbb6524371ed716c5a95cfce9679af430d2ec21893b11'
  accessed_at: '2026-11-04T13:21:06.503504Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-5NIK-entity2
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5NIK/2
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity2.raw
    SHA256 d04c66f5b3c776028830ee4155d3249a4a12efbf9832eb1069cd496764c82783; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity2.receipt.json
    SHA256 9c9a3a52d77b84cad0bd00b74572bcca637aa4e157b109cdde0131b7ea62b1fb'
  accessed_at: '2026-11-04T13:21:06.504276Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-pdb-5NIK-entity3
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/5NIK/3
  locator: 'RCSB exact entry/assembly1/entity response: deposited identity, author
    assembly counts, chain/UniProt mappings, source organism versus expression host.
    Coordinate pixels/raw maps not inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity3.raw
    SHA256 d2016d8529eeacec931f3b94ef6c12be4725a1d98934e2dacbc96579ab5e8a7f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pdb-5NIK-entity3.receipt.json
    SHA256 dcb3cd53ae30029c7f8a60331f330963f8aed6e97f4fe76589052eb351125f1c'
  accessed_at: '2026-11-04T13:21:06.511381Z'
  support: partial
  summary: 7MDY supports LolC1:LolD2:LolE1; 5NIK ordered model supports MacB2:MacA6:TolC3.
    Experimental construct limitations come from primary Methods.
- evidence_id: plaque-PMC2851745-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2851745.1/PMC2851745.1.xml
  locator: Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-jats.raw
    SHA256 23f82e897b6a1873a6d35fe182d39949af7092a21c756c9114b18f67064b9d2b; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2851745-jats.receipt.json
    SHA256 f04821a1cd605429aba2310202ed92b9296425d3bd4b466cacb3779ff5086baa
  accessed_at: '2026-11-04T13:21:06.564180Z'
  support: context_only
  summary: 'Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather
    than PDF. Successful alternative routes are independently tiered.'
- evidence_id: plaque-PMC3038725-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3038725.1/PMC3038725.1.xml
  locator: Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-jats.raw
    SHA256 afef1ec318870082585cbf50af335568e02121756a6da96a8255ee28960da0f0; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3038725-jats.receipt.json
    SHA256 bd700220ea09b31132be086b19838c4b229b1524c1fa6796ca7b6e49e4ac8319
  accessed_at: '2026-11-04T13:21:06.564226Z'
  support: context_only
  summary: 'Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather
    than PDF. Successful alternative routes are independently tiered.'
- evidence_id: plaque-PMC5858563-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5858563.1/PMC5858563.1.xml
  locator: 'Complete direct main-body paragraphs0–12: seven-protein proteoliposome
    LPS transport and LptA-mediated membrane association; no physiological LptA copy-number
    resolution, no supplemental experiments or pixels inspected. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5858563-jats.raw
    SHA256 2ba2a990adb12cbeb5829b5fd3d4eb716c9a4807e038ec1cafffa2308a96ee97; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5858563-jats.receipt.json
    SHA256 ab98d22df9d572e9791478cff72d6ef1d6f685b2e6141b7b70ece02744d5c7f1'
  accessed_at: '2026-11-04T13:21:06.587306Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-PMC3552488-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3552488.1/PMC3552488.1.xml
  locator: 'Complete direct main-body paragraphs0–7: ATP-dependent LPS extraction
    and transfer, contrasted with ATP-independent LptA/LptC association; no supplement
    or pixels. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3552488-jats.raw
    SHA256 524716c6851340007bc32191eaef5626eda010fe739c194a4a943fbb76f1e98d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC3552488-jats.receipt.json
    SHA256 853008adead8616071b6cb7d1276bdef046143fc917ca2bc6432942bdaadcc33'
  accessed_at: '2026-11-04T13:21:06.588492Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-PMC2880507-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2880507.1/PMC2880507.1.xml
  locator: 'Complete direct main-body paragraphs0–9: seven-protein copurification/fractionation
    and bridge proposal. These association data are not atomic continuous-pathway
    or universal necessity proof. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2880507-jats.raw
    SHA256 620e0b9037dba893469d09f9dd830b83c872dccf392da6d1fa3a1c8ae25cf3ff; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2880507-jats.receipt.json
    SHA256 cff7cb61202411c7eea6ad7568b4621ab70430e404b8204e97a3d36c6b0df797'
  accessed_at: '2026-11-04T13:21:06.643551Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-PMC5672026-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5672026.1/PMC5672026.1.xml
  locator: Actual HTTP/access response only; no scientific body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5672026-jats.raw
    SHA256 22dfee541aa6f8eeaa6055886c05ba7d864831564d1be1eb6c04ffda5a948d8b; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5672026-jats.receipt.json
    SHA256 c7729d08b0e4d58f50eb83efe7a7ed7852ee0aab7be3f60e830106307095b325
  accessed_at: '2026-11-04T13:21:06.643620Z'
  support: context_only
  summary: 'Failed or non-body route: HTTP 404; canonical PDF route returns HTML rather
    than PDF. Successful alternative routes are independently tiered.'
- evidence_id: plaque-PMC8333309-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8333309.1/PMC8333309.1.xml
  locator: 'Primary Results sections3–8 and Methods11,13,15 read: K-12 genes expressed
    in BL21(DE3), His-LolD complex, Lpp K58-deletion copurification, nucleotide-state
    cryo-EM and basal ATPase. Bound lipoprotein density is not exact sequence proof;
    extrusion/reset model distinct from direct transport flux. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC8333309-jats.raw
    SHA256 f06cbeb2b0cfef54e1b2abb272d1f2a9fbbc657418b548b017ef359fd0e2bb48; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC8333309-jats.receipt.json
    SHA256 56e4a99448bdf42e3ab1e14bb5948a0430086eda0a1849e2839c4885e26ea1aa'
  accessed_at: '2026-11-04T13:21:06.645188Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-PMC5447821-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5447821.1/PMC5447821.1.xml
  locator: 'Primary direct introductory paragraphs, Results S2–S8 and Methods S10,S12,S13
    read: W3110 genes, C43(DE3) ΔacrAB expression, MacB-MacA fusion/disulfide-stabilized
    purification, ordered 2:6:3 core, proposed periplasmic entry/gate. Introductory
    broader cargo references are not all experimentally assayed here; no pixels/supplemental
    data read. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5447821-jats.raw
    SHA256 9a25d568fd93109b8bd837e7bf71e0b1476fcd25182f0247d1d3c013d9fa4611; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC5447821-jats.receipt.json
    SHA256 3ace879c5617227d8246c9cbeae2d703bf3268de89fa3084f4f416104d72f949'
  accessed_at: '2026-11-04T13:21:06.950857Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-PMC2613632-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2613632.1/PMC2613632.1.xml
  locator: 'Primary Experimental Procedures, Results and Discussion text read (including
    text captions): KAM3(DE3) assays, tagged-protein pulldown, detergent-state dimer
    biophysics, ATPase kinetics, erythromycin binding and resistance. Two author attributions
    in the record should name Lin et al. 2009. Detailed coupling models remain interpretations;
    no supplemental data or pixels. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2613632-jats.raw
    SHA256 cc4ef19105973cda7330b93388ed3f39471975ca9f51398676ab0b9bae9acb00; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/PMC2613632-jats.receipt.json
    SHA256 949c6bb442d28598cb1d70e82221136a0d00294ee1224789cc8a817547edb781'
  accessed_at: '2026-11-04T13:21:06.951652Z'
  support: partial
  summary: Fresh genuine primary source read at the declared bounded extent; assay,
    construct and evidential-stage limits retained.
- evidence_id: plaque-pmid-10783239
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10783239+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-10783239.raw
    SHA256 4e90c52b481aae1c19b7104c6397061c21fe70bfa53e10f14bd61acb275e46a9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-10783239.receipt.json
    SHA256 87054b473ed0129b97bb0232ba4ac2bfd17691607e6df154023330b18743fbd9
  accessed_at: '2026-11-04T13:21:07.063688Z'
  support: partial
  summary: A new ABC transporter mediating the detachment of lipid-modified proteins
    from membranes. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:10783239 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-18634750
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18634750+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete secondary-review abstract and bibliographic identity only; no
    body claim. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18634750.raw
    SHA256 486bed2be46da4e93c72158a1b835a71b731ba22b288d7f2db620544d1aaff0f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18634750.receipt.json
    SHA256 16def06c5b0a6da2d8a9eccbb4b3d82c7f3da2690a36d62fc3b42bb4bd8ced41
  accessed_at: '2026-11-04T13:21:07.074931Z'
  support: partial
  summary: ATP-binding cassette transporters in Escherichia coli. Secondary synthesis,
    not primary experiment.
  search_scope: Europe PMC exact EXT_ID:18634750 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-34344901
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A34344901+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Bibliographic identity/title/authors/DOI and primary body linkage; separate
    genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-34344901.raw
    SHA256 e4e20cff1e8c0f66a9e37d9097cbc88e68c7d26905555a0d618a7b2b80768de2; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-34344901.receipt.json
    SHA256 dcad8534c5c5e313b22df99443158d12cd5d0561afc8d0d7dbaaa623b054e82d
  accessed_at: '2026-11-04T13:21:07.103241Z'
  support: context_only
  summary: Mechanism of LolCDE as a molecular extruder of bacterial triacylated lipoproteins.
    Identity only in this evidence row.
  search_scope: Europe PMC exact EXT_ID:34344901 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-18955484
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18955484+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Bibliographic identity/title/authors/DOI and primary body linkage; separate
    genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18955484.raw
    SHA256 3bd3f3d4f8fc8d32518d6dcd5a638a3f094dac18efe8a85577c3546398ed6ade; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18955484.receipt.json
    SHA256 f9d32ff0eceeca17fa305fa6dfb0d2d140798670032f9ab0d4d752182fd3c8f0
  accessed_at: '2026-11-04T13:21:07.221397Z'
  support: context_only
  summary: MacB ABC transporter is a dimer whose ATPase activity and macrolide-binding
    capacity are regulated by the membrane fusion protein MacA. Identity only in this
    evidence row.
  search_scope: Europe PMC exact EXT_ID:18955484 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-28504659
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28504659+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Bibliographic identity/title/authors/DOI and primary body linkage; separate
    genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28504659.raw
    SHA256 b2f2df1b4d9cd9326012b45b5655a9e2aebc95099d04dc46094322a69ec983ee; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28504659.receipt.json
    SHA256 362e755a776bfaff122e7dfa5f6e8cececc2a51e5aeb82cac803157b0c48ac02
  accessed_at: '2026-11-04T13:21:07.358887Z'
  support: context_only
  summary: Structure of the MacAB-TolC ABC-type tripartite multidrug efflux pump.
    Identity only in this evidence row.
  search_scope: Europe PMC exact EXT_ID:28504659 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-12207697
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12207697+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12207697.raw
    SHA256 4acb7231e965168dc6e8d81706bf1fc157a3d7e1914a761f2a4c4740594d970a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12207697.receipt.json
    SHA256 806e8b81e5b7c7946d3167ce038e29924e68c042851123c980e17aafc8fb76f2
  accessed_at: '2026-11-04T13:21:07.565156Z'
  support: partial
  summary: Imp/OstA is required for cell envelope biogenesis in Escherichia coli.
    Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:12207697 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-12724388
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12724388+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12724388.raw
    SHA256 87bbb11612b9d208012d1a5f0f51b4c03b427a081453eb5718828aa491b01f84; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-12724388.receipt.json
    SHA256 6d56a860faf5893dba730f523d9b4566814baec90ba45c21aa0fb62b5c3d38f0
  accessed_at: '2026-11-04T13:21:07.565230Z'
  support: partial
  summary: n-Hexane sensitivity of Escherichia coli due to low expression of imp/ostA
    encoding an 87 kDa minor protein associated with the outer membrane. Primary abstract
    scope retained.
  search_scope: Europe PMC exact EXT_ID:12724388 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-16079137
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16079137+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16079137.raw
    SHA256 64452b120f275a02c3b16d6dc23744b0a37865ec6c957a437bb12644d987241d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16079137.receipt.json
    SHA256 a53415ba92da4d08e75780557ddd89b3b3601d586201429a1ea9b5e9afb75820
  accessed_at: '2026-11-04T13:21:07.642226Z'
  support: partial
  summary: Protein complexes of the Escherichia coli cell envelope. Primary abstract
    scope retained.
  search_scope: Europe PMC exact EXT_ID:16079137 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-17056748
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17056748+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-17056748.raw
    SHA256 98e7fdce444d2bc6646d3a6d5b99b117aba709ddcca3a9031f58cb1ad457f6e6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-17056748.receipt.json
    SHA256 25a4e95e4ef31d1f5327ebd4fba5f73f2713617cef98d337decfe2576f3d9d37
  accessed_at: '2026-11-04T13:21:07.765853Z'
  support: partial
  summary: Characterization of lptA and lptB, two essential genes implicated in lipopolysaccharide
    transport to the outer membrane of Escherichia coli. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:17056748 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-18424520
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18424520+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18424520.raw
    SHA256 a85cd496ad6bbf9e69b1b03b57dff5cecf8257321f98e3d9a8a9d4a07738e26a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18424520.receipt.json
    SHA256 b5a48b8a95de861327b5fd7cc465a98ee24ade5e792b6bf3dd674bacd1843b4c
  accessed_at: '2026-11-04T13:21:07.900320Z'
  support: partial
  summary: Functional analysis of the protein machinery required for transport of
    lipopolysaccharide to the outer membrane of Escherichia coli. Primary abstract
    scope retained.
  search_scope: Europe PMC exact EXT_ID:18424520 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-18480051
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18480051+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18480051.raw
    SHA256 64df91f2e64e1517f5069e770d70f359e090b819ef1fffa8834ffbf2d1662e39; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18480051.receipt.json
    SHA256 fa87978b1caeb5d7e7a5277a90542a9a978cb7107ec44ce9d0602032fb7d923d
  accessed_at: '2026-11-04T13:21:07.901212Z'
  support: partial
  summary: The LptA protein of Escherichia coli is a periplasmic lipid A-binding protein
    involved in the lipopolysaccharide export pathway. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:18480051 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-20720015
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20720015+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-20720015.raw
    SHA256 77562c9ea8468a9080f5cb0cead52b9930ce04e70520ced9e58eca0dd14d0461; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-20720015.receipt.json
    SHA256 79dba0cdf3f8e47ec4b8ca79f8dc2b282db398cd4db0231d2d7342612f8bf78f
  accessed_at: '2026-11-04T13:21:08.361851Z'
  support: partial
  summary: Structure and functional analysis of LptC, a conserved membrane protein
    involved in the lipopolysaccharide export pathway in Escherichia coli. Primary
    abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:20720015 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-21257904
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21257904+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Bibliographic identity/title/authors/DOI and primary body linkage; separate
    genuine body is the scientific evidence. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-21257904.raw
    SHA256 68b273cb5914a605dae4e98370d516366d649fa8b0e9a987f52af814951df25f; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-21257904.receipt.json
    SHA256 94799b2120ecd9a12e00d0cc87147bc287ccd3c70c614d2364530bb9ce20598c
  accessed_at: '2026-11-04T13:21:08.403315Z'
  support: context_only
  summary: The complex that inserts lipopolysaccharide into the bacterial outer membrane
    forms a two-protein plug-and-barrel. Identity only in this evidence row.
  search_scope: Europe PMC exact EXT_ID:21257904 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-3316191
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3316191+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-3316191.raw
    SHA256 ce9e18cf910238adfced888d5cbc73e15ad84f7807cd5b34870d9acaf935801d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-3316191.receipt.json
    SHA256 ce69048c214aee59e112fa77980fccb8279124af80fdef920837026efef53311
  accessed_at: '2026-11-04T13:21:08.483901Z'
  support: partial
  summary: Genes encoding two lipoproteins in the leuS-dacA region of the Escherichia
    coli chromosome. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:3316191 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-19500581
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19500581+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-19500581.raw
    SHA256 5bc71d31def1d0531d0de39ca5e05871759e372e796d90ec33b2b6ffd44953c7; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-19500581.receipt.json
    SHA256 44291e8fafca957b27e942aa68d00ca385bc5008552bca1fe47b21fa31c646e5
  accessed_at: '2026-11-04T13:21:08.541676Z'
  support: partial
  summary: Biochemical characterization of an ABC transporter LptBFGC complex required
    for the outer membrane sorting of lipopolysaccharides. Primary abstract scope
    retained.
  search_scope: Europe PMC exact EXT_ID:19500581 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-22668317
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22668317+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-22668317.raw
    SHA256 4d90d55f5badfca47afe7d0553fd20bdad5110d6bfded6cd87e3704648a882ab; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-22668317.receipt.json
    SHA256 395dad9a98dfa7c5cc20e88bc78014b51ab08d524a70da806e0374a2faf206b6
  accessed_at: '2026-11-04T13:21:08.557081Z'
  support: partial
  summary: Regulated assembly of the transenvelope protein complex required for lipopolysaccharide
    export. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:22668317 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-16861298
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16861298+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16861298.raw
    SHA256 363ed994ed36a0c2b37a0150170d2036e64e2d60963dfc12efb454892951f106; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-16861298.receipt.json
    SHA256 8cfb557618cba2ecbbdadd3dc3a039f62c515c584d65c5d8e0c04b743f503b66
  accessed_at: '2026-11-04T13:21:08.586492Z'
  support: partial
  summary: Identification of a protein complex that assembles lipopolysaccharide in
    the outer membrane of Escherichia coli. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:16861298 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-18375759
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A18375759+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18375759.raw
    SHA256 6c0c3c22a22f322693f0859ecb37080211a24cf86d67cd3ae5d2b7c4e38ef120; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18375759.receipt.json
    SHA256 da9906f86f3121871c1d137f8bc91861db6fccba0a9714009a105e1c2b56f09d
  accessed_at: '2026-11-04T13:21:09.100714Z'
  support: partial
  summary: Identification of two inner-membrane proteins required for the transport
    of lipopolysaccharide to the outer membrane of Escherichia coli. Primary abstract
    scope retained.
  search_scope: Europe PMC exact EXT_ID:18375759 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-28878019
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A28878019+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete secondary-review abstract and bibliographic identity only; no
    body claim. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28878019.raw
    SHA256 409f1cc537de7ff02f3b07e2da4dab45d45deb85bfe2153bfec48698145aa03d; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-28878019.receipt.json
    SHA256 18a4084459fb06b125567c539fb5b9d8b782de4f29d7607aae3322cbdb91dcff
  accessed_at: '2026-11-04T13:21:09.203055Z'
  support: partial
  summary: 'The lipopolysaccharide transport (Lpt) machinery: A nonconventional transporter
    for lipopolysaccharide assembly at the outer membrane of Gram-negative bacteria.
    Secondary synthesis, not primary experiment.'
  search_scope: Europe PMC exact EXT_ID:28878019 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-25257218
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25257218%20AND%20SRC:MED&format=json&resultType=core
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-25257218.raw
    SHA256 dbd292cf452bbcf52df029258270193b2c7abc3af8f4a0098f101427d90bb531; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-25257218.receipt.json
    SHA256 1a7f6bf5954d84dcca0a4865397e6d26ee07dfa80685ab954bb99de2e68a9534
  accessed_at: '2026-11-04T13:29:41.938881Z'
  support: partial
  summary: Protoporphyrin (PPIX) efflux by the MacAB-TolC pump in Escherichia coli.
    Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:25257218 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-18805970
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:18805970%20AND%20SRC:MED&format=json&resultType=core
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18805970.raw
    SHA256 5711bde7f4fe1e8e432cac5bb33e2dcad34a75e5745aae82d8aca1ed624749ce; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-18805970.receipt.json
    SHA256 bb472fd0e4432ba1740dd3fca022d9398ad528214aded84bf89631557ca556b8
  accessed_at: '2026-11-04T13:29:41.939885Z'
  support: partial
  summary: MacAB is involved in the secretion of Escherichia coli heat-stable enterotoxin
    II. Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:18805970 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-pmid-11544226
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:11544226%20AND%20SRC:MED&format=json&resultType=core
  locator: Complete native primary abstract and bibliographic identity only, no body,
    figures or supplements. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-11544226.raw
    SHA256 34b04bb07df1e84f4678fdba6d89280f9399d50cf1cedd1e372c4a68e7e7c5f9; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/pmid-11544226.receipt.json
    SHA256 ba4966e19bf23c194859e6ba1b852adc3c6a14afa485aa9091c3b186ca6d7f5d
  accessed_at: '2026-11-04T13:29:41.941091Z'
  support: partial
  summary: Novel macrolide-specific ABC-type efflux transporter in Escherichia coli.
    Primary abstract scope retained.
  search_scope: Europe PMC exact EXT_ID:11544226 AND SRC:MED, resultType=core; single
    matching record inspected; abstract/body tiers distinguished.
- evidence_id: plaque-yakushi2000-figure1
  kind: primary_source
  reference: https://www.nature.com/articles/ncb0400_212/figures/1
  locator: Public publisher figure 1 title and complete text caption, decoded as UTF-8;
    no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure1.raw
    SHA256 fcba753f666a7a6d17748264ab4e29865a32490cf448d8351af4daafcd648b69; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure1.receipt.json
    SHA256 38aab5322172bfd6431aa5731640f6c747dc610b032c23e74abec28dd526c280
  accessed_at: '2026-11-04T13:23:33.073595Z'
  support: partial
  summary: Pal proteoliposome ATP/LolA-dependent release and LolB transfer assay.
- evidence_id: plaque-yakushi2000-figure3
  kind: primary_source
  reference: https://www.nature.com/articles/ncb0400_212/figures/3
  locator: Public publisher figure 3 title and complete text caption, decoded as UTF-8;
    no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure3.raw
    SHA256 41c80de15b510c802441e0a290804dd55153d5a74dd67a698c5d0fd93904e3ac; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure3.receipt.json
    SHA256 0d0c70d32e4b5e9dc164cb4d70382baf973e8dbe4c17154b288522ea4cf20c4e
  accessed_at: '2026-11-04T13:23:33.075791Z'
  support: partial
  summary: LolD mutants, JE5505/JE5506 Lpp growth comparisons and DLP79-22 spheroplast
    Lpp release assay.
- evidence_id: plaque-yakushi2000-figure4
  kind: primary_source
  reference: https://www.nature.com/articles/ncb0400_212/figures/4
  locator: Public publisher figure 4 title and complete text caption, decoded as UTF-8;
    no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure4.raw
    SHA256 8ec2e9e8ba871fd2303dda5df615e76aa972b22c3c471d920d5400135c418c75; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure4.receipt.json
    SHA256 1492e243a91e68b44bd20ccc8647281913bbde28a440f311a2c32134f28d14a0
  accessed_at: '2026-11-04T13:23:33.077100Z'
  support: partial
  summary: Pal outer-leaflet proteoliposome release and protease-protection experiments.
- evidence_id: plaque-yakushi2000-figure7
  kind: primary_source
  reference: https://www.nature.com/articles/ncb0400_212/figures/7
  locator: Public publisher figure 7 title and complete text caption, decoded as UTF-8;
    no image pixels and no inaccessible full main body. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure7.raw
    SHA256 0447128fc41d705d757b0694611fc9a8e97fd9fc394505d74f275502da33ef55; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/yakushi2000-figure7.receipt.json
    SHA256 15d74c23ca1ea251fb589024ac8d199fa69d6617f020ce43d6bf08274205b52e
  accessed_at: '2026-11-04T13:23:33.079758Z'
  support: partial
  summary: Model caption distinguishes Asp+2 inner-membrane lipoproteins from non-Asp+2
    outer-membrane lipoproteins.
- evidence_id: plaque-adapter-b0054
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0054
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054.raw
    SHA256 afbb01c7d50a3e0554edc74d97d72c73233e9bb57ebdc0f3084414473b766bd6; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054.receipt.json
    SHA256 ff47ce46e5bf405898b387688e043b58a5ff3b92a5fe969b32ef54354294119b
  accessed_at: '2026-11-04T13:22:07.939602Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0054;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0054-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0054/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054-modules.raw
    SHA256 b7cb5257aaf8002c3e66ba15137cf03baa4e2ad2808259ece68763901d61df4e; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0054-modules.receipt.json
    SHA256 b8fa566f459a23b2824ff23e03810c175b2fb0efe9bd05c8789ea85a7bea7074
  accessed_at: '2026-11-04T13:22:07.940725Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0054/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0641
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0641
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641.raw
    SHA256 008d4160cff20dc5836c8a35376b65bce93dac1cc4ce9f290642c4b5b6ea56f2; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641.receipt.json
    SHA256 e9e678046e146669b08580bbd4d00d70cf3f3d362db195c8cbd7566565c1547d
  accessed_at: '2026-11-04T13:22:07.942169Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0641;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0641-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0641/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641-modules.raw
    SHA256 6b71b8b00939a5dd834219a04a43fda62b1e9b7e0360e589de968d38f4532442; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0641-modules.receipt.json
    SHA256 ba03de166d3609460d279e275e64ff5a45bad6eff43a43747e7e39da894d32c4
  accessed_at: '2026-11-04T13:22:07.943276Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0641/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0741
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0741
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741.raw
    SHA256 f706efff4ca56892ccf7c4b3ea5163aaf0a2fba02ead0c88389f60d583147fb2; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741.receipt.json
    SHA256 8ff90841c159ce395292db07b3d4888e5316e27f858fe0532f485f77916fd7dc
  accessed_at: '2026-11-04T13:22:07.944257Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0741;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0741-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0741/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741-modules.raw
    SHA256 f9c546a89ead820156e0a18bb74bc9afcab24447fdf492bbf608a183bf6c8419; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0741-modules.receipt.json
    SHA256 01f96c632bdf8b48a579fb647ed4ce9a0249f24a7bf90e151421d55f3f119234
  accessed_at: '2026-11-04T13:22:07.945735Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0741/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0878
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0878
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878.raw
    SHA256 993339965dcb1dbeab0e209ab7ec8f776099bcccb1d82d8baf328969e00bf8da; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878.receipt.json
    SHA256 d7e8a8a704d575f713f07a13069cec5c2159a5ca06ea533c14d83d867c234b0c
  accessed_at: '2026-11-04T13:22:07.947092Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0878;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0878-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0878/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878-modules.raw
    SHA256 dc1f3d2335e3f8a0f27e6374d3a8be853eff8a71b10972d7408ff8ed704b9ca5; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0878-modules.receipt.json
    SHA256 63436a1e61291d1f143e20d3246140f303c73b7e6e54e36dd5609a699a7f722e
  accessed_at: '2026-11-04T13:22:07.948303Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0878/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0879
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0879
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879.raw
    SHA256 182e707ecf9aaa44267b54e298131624182ae19c60b076bb6559dc4657f0925a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879.receipt.json
    SHA256 1411fe7160d1fc1cd259c9cf1d4472b26118519710e3526f215deac51d989f56
  accessed_at: '2026-11-04T13:22:07.989078Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0879;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b0879-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b0879/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879-modules.raw
    SHA256 e378238a159a7b1c2fc2b249b6a6305cacdb4a741894230e91f5004412adb2e1; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b0879-modules.receipt.json
    SHA256 46a0c4dcb439425c94abeb963dcea10e022356f19ea4b54a6f9437111a2073cc
  accessed_at: '2026-11-04T13:22:07.991138Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b0879/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1116
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1116
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116.raw
    SHA256 3edee3ba975893ce7af0e2e47dcf77622948c363e0451cb425cb75d91cdd77ef; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116.receipt.json
    SHA256 dea84940e916ee8a30929385c47a008841bb91f51cbd4cbe912565226a4ceb05
  accessed_at: '2026-11-04T13:22:07.991766Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1116;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1116-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1116/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116-modules.raw
    SHA256 7f6719d2867e699d7c92304895375c30227897a28cefcb5b015b00a9c2e34445; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1116-modules.receipt.json
    SHA256 f0e151edb52ec58d60c11988121cac9d734b4f46df646fcdfd08fbc91207d9bc
  accessed_at: '2026-11-04T13:22:08.001558Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1116/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1117
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1117
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117.raw
    SHA256 6dc84fb1f0ff5e43a52d728111a992d3d5772c1c11bce03e414c4a16a027aeb0; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117.receipt.json
    SHA256 409bba946cfe17ca0d594eba24bd7a1fa569f6430453b30d8a7e103a5c6e3ab8
  accessed_at: '2026-11-04T13:22:08.003772Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1117;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1117-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1117/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117-modules.raw
    SHA256 86b3250cb1381a9e64880d4897979c83f9f020f49a92f7d792a47c286a22b16a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1117-modules.receipt.json
    SHA256 3227ca056cf1543687ddc127dd0924a1b575d32025f084b1c41ff292a602aa65
  accessed_at: '2026-11-04T13:22:08.004479Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1117/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1118
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1118
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118.raw
    SHA256 e2c26351aed611404ee9d87678250a78e553f86289c38e1c3a3dc158adc87fed; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118.receipt.json
    SHA256 56cd11f044e819f912c1256339473430e215340ef9d71f0d4d0cf2eefc10f934
  accessed_at: '2026-11-04T13:22:08.017356Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1118;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1118-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1118/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118-modules.raw
    SHA256 f80b2a99f8b4cce1ec72818ac91a8a11b5e31c0b0402f91b44ea5b7a5d80bdc3; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1118-modules.receipt.json
    SHA256 69285f340a4c61c1e2881cf2a7873a05609b80bd963b803530f0d7d50d3a5545
  accessed_at: '2026-11-04T13:22:08.027484Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1118/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1677
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1677
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677.raw
    SHA256 d2c646ac4c203b1ca72c75955f47a99a92b58dae718a0643ea3e4a7066a22513; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677.receipt.json
    SHA256 e10672b9c898ea7373f73d3beb53bf2afd75f10e0b80b253607e6d53890c5128
  accessed_at: '2026-11-04T13:22:08.031934Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1677;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b1677-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b1677/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677-modules.raw
    SHA256 1e48c9eeba3cd8fe5bd62ece576b84f7c86c6aa45c5f875f6bcd6e80fe3bf8a5; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b1677-modules.receipt.json
    SHA256 210573623e7fea185be0c756b3bc4c66a663d0a9f6cb1271bcb4deca9724fa75
  accessed_at: '2026-11-04T13:22:08.034175Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b1677/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3035
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3035
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035.raw
    SHA256 3c1072490b201aff8b31f919b89d538017fabee3272bdf9115b4949ad8844a7a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035.receipt.json
    SHA256 bf169f1b324b8ce0c8b0f94ebe71b6c1e23dd278f82e35a95850e1b85822effe
  accessed_at: '2026-11-04T13:22:08.049823Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3035;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3035-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3035/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035-modules.raw
    SHA256 c65a4d314d71a084b2bf80376d7a091196d354d2d4cbc86c6b07b60952e15988; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3035-modules.receipt.json
    SHA256 db6f5f7cf7518b2a18e8c291bb875efd53097fb05dde7b5ecfb2f43ebb116c9c
  accessed_at: '2026-11-04T13:22:08.050569Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3035/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3199
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3199
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199.raw
    SHA256 73f015ea9b9806201ae77c61660fcb0c9885d5b955db0f8a7a9e67d7acaca868; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199.receipt.json
    SHA256 1b5a3417c02f626f489f6231f3096f20ce0616a43fec1e6762690eeb41312605
  accessed_at: '2026-11-04T13:22:08.058514Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3199;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3199-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3199/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199-modules.raw
    SHA256 46ed8c54560a4ede0a9019a7d65bd5d609e1ab95170045a2907f3bf46ffcd87a; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3199-modules.receipt.json
    SHA256 1920f586305d94f4b259529ae13e57ac5bb91d6ed61189c081b01dbc60608e7f
  accessed_at: '2026-11-04T13:22:08.059254Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3199/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3200
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3200
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200.raw
    SHA256 a6ec3cce59ce2d2c618ea96eda3a0c4246b1eb8c20ef20a38ba70fafd7aa338e; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200.receipt.json
    SHA256 16f193de54f1faa9ff85f2550412d144d4568af2734f167c572944d326068880
  accessed_at: '2026-11-04T13:22:08.069579Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3200;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3200-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3200/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200-modules.raw
    SHA256 bb054259370bf3f2aa6d748bab64f3fdb222bbf72b7021f4568f863bd8372c55; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3200-modules.receipt.json
    SHA256 143d838bcf082e68b1985178b3d9f03812985e698d4d4921a8b0e213889bb973
  accessed_at: '2026-11-04T13:22:08.079315Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3200/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3201
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3201
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201.raw
    SHA256 9184bf4470a080a9537eb62ffb5a3f8a482e1bc45ff8c0f86a49727badadcbdb; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201.receipt.json
    SHA256 5d2276aad18920fe0cacf5e4e370fb6a04c809eb341fb7bc91adc41152dc9313
  accessed_at: '2026-11-04T13:22:08.085552Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3201;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b3201-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b3201/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201-modules.raw
    SHA256 ef299a66694efa19451c0a8bda4d69b54bf9e350cd9fe2cfd36821a96e04abae; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b3201-modules.receipt.json
    SHA256 fba48c9898f1432e612e18964af96c8f43cc637a281e061f0f5e69c1e608cbaf
  accessed_at: '2026-11-04T13:22:08.091962Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b3201/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b4261
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4261
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261.raw
    SHA256 2bdb1fa5be7099671156704e18a31ea719cbcac6ae5327fe791986d55ae40b1c; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261.receipt.json
    SHA256 b0ea87b9f901d2d79a0028bbb259743832328d0c44a6bf9d7e351c3ab0670aa1
  accessed_at: '2026-11-04T13:22:08.098496Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b4261;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b4261-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4261/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261-modules.raw
    SHA256 bd9da7a4cddcdab9cc3b647fcccf4bfd9bcdf878f4df460d89d0dd5f85fb6f92; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4261-modules.receipt.json
    SHA256 70b9fd56aae2816d902a94aa54ad9f5c2d723a4475ce87097fe950035d9fd167
  accessed_at: '2026-11-04T13:22:08.100630Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b4261/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b4262
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4262
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262.raw
    SHA256 88ccf9370c561f2014c8acbe3f364f5a6de7a14c8372325080756c14f4625f50; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262.receipt.json
    SHA256 79000bcef0f102831b5554ff9576e90ff87ae2ead3bdba5f2e272c932e8b83a2
  accessed_at: '2026-11-04T13:22:08.112359Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b4262;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-b4262-modules
  kind: search
  reference: https://imodulondb.org/api/genes/e_coli/precise1k/b4262/imodulons
  locator: Official E. coli precise1k exact-locus or exact-module response; full returned
    computational membership table read; generated ai_summary excluded. Snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262-modules.raw
    SHA256 f88707c86222d991c2459899bbdaab7367091571fa718847a74b0dda44ccf763; receipt
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-b4262-modules.receipt.json
    SHA256 ffbab103607d1cd81e6e61d94cd97be1c16eb298823ab091b9e25a2579fb0b36
  accessed_at: '2026-11-04T13:22:08.120080Z'
  support: partial
  summary: Expression-module evidence only, not localization, physical assembly, transport
    or absence proof.
  search_scope: Official iModulonDB e_coli/precise1k exact endpoint https://imodulondb.org/api/genes/e_coli/precise1k/b4262/imodulons;
    one locus/one module selected from the complete catalogue and 4257-gene table;
    complete 201-row locus memberships or full module table, no pagination omitted.
- evidence_id: plaque-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/organisms
  locator: Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-catalogue.raw
    SHA256 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693; receipt
    SHA256 d83e600c4e77f3eecbfc797c94114aa865f20bf3c57049a31ac0f0ba0eb17c03. Full
    catalogue/metadata/index; for gene table exact full-table scan for 15 named loci.
    Generated prose excluded.
  accessed_at: '2026-11-04T13:18:08.811643Z'
  support: partial
  summary: 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related
    strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This
    is not exact equivalence to all experimental strains or recombinant constructs.
- evidence_id: plaque-adapter-precise1k-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-precise1k-meta.raw
    SHA256 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865; receipt
    SHA256 bc0785967572c75209e0274775d75d945dffe53f2ec5c37bfb228b0f48d16c7e. Full
    catalogue/metadata/index; for gene table exact full-table scan for 15 named loci.
    Generated prose excluded.
  accessed_at: '2026-11-04T13:18:09.355654Z'
  support: partial
  summary: 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related
    strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This
    is not exact equivalence to all experimental strains or recombinant constructs.
- evidence_id: plaque-adapter-precise1k-genes
  kind: search
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=5000
  locator: Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-precise1k-genes.raw
    SHA256 db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27; receipt
    SHA256 8c5b751e9c0f107a1d1bdd84d136c9ab7ec49497b4c02dc4e94f9e908e889969. Full
    catalogue/metadata/index; for gene table exact full-table scan for 15 named loci.
    Generated prose excluded.
  accessed_at: '2026-11-04T13:18:08.860491Z'
  support: partial
  summary: 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related
    strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This
    is not exact equivalence to all experimental strains or recombinant constructs.
  search_scope: Complete 4257-row official e_coli/precise1k gene table, exact gene_name
    in lptA,lptB,lptC,lptD,lptE,lptF,lptG,lolC,lolD,lolE,lpp,pal,macA,macB,tolC; all15
    found and joined by locus/UniProt; no other hosts searched.
- evidence_id: plaque-adapter-precise1k-modules
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Independently read actual shared same-PR snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/adapter-precise1k-modules.raw
    SHA256 c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d; receipt
    SHA256 886c69335fab65b02c9c3d2c197a242a2da2e16a92e8a17aee602ed59fa74dd0. Full
    catalogue/metadata/index; for gene table exact full-table scan for 15 named loci.
    Generated prose excluded.
  accessed_at: '2026-11-04T13:18:08.701527Z'
  support: partial
  summary: 20 organism rows/28 organism-dataset pairs; precise1k covers five K-12-related
    strains (BW25113,DGF-298,GMOS,MG1655,W3110), 4257 genes and 201 modules. This
    is not exact equivalence to all experimental strains or recombinant constructs.
- evidence_id: plaque-adapter-joined-scope
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/adapter-membership-summary.json
  locator: Computed full 201-row per-gene memberships, exact selected module metadata
    and full module member tables; summary SHA256 42a00f0dc04109162b6a88252b8481bf7936b661effce1622fb799987205fbb6
  accessed_at: '2026-11-04T13:33:20.766391Z'
  support: supports
  summary: 'Positive memberships: lptA/B/C and tolC in22/SoxS, lpp in45/Resistance,
    lptF in167/UC-2; full member counts117/58/96 confirm these joins. Other9 loci
    have no true membership among201. These are thresholded computational contexts,
    never biological absence or assembly evidence.'
- evidence_id: plaque-lolcde-stale-delta
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-plaque/lolcde-stale.diff
  locator: Exact old frozen record versus current source; SHA256 1dc27510e1617705b107334a77e63b34239838d96dc8fbf34fba266d0ae21b21
  accessed_at: '2026-11-04T13:33:20.766421Z'
  support: context_only
  summary: Delta adds Lpp/Pal substrate xrefs, three LolC/D/E contributes-to membership
    edges and one lipoprotein-release-to-localization edge, with history. Family-grounding
    finding remains unaffected.
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record structured-source and scientific review
  summary: Positive named molecular/pathway claims trigger actual host coverage assessment;
    no-expression wording alone does not establish exemption.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Exact component identities and dated discussion contract
  summary: Resolve demonstrated exact class groundings, while retaining valid broader
    classes and preserving dated rationale. Current clarification does not rewrite
    historical searches.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component and graph identity; experimental necessity
  summary: A verified accession and covered typed node do not establish structural
    class identity, universal formation necessity, copy count or source-specific experiment.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native reference identity and query scope
  summary: Native names/status/taxa and exact current searches establish reference
    identity, not historical release results, experimental strain or causal membership.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, intervention and source attribution
  summary: Component membership, source-specific counts, activity and whole-assembly
    formation differ. External regulators need not be constituents.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Exact source access tiers
  summary: Primary abstracts, genuine main text, secondary synthesis, metadata and
    actual pixels have distinct scopes. Failed access is validation context only.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Native review envelope and lineage
  summary: Use unique evidence references, exact predecessor repository/review/finding
    and bounded searches.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-up-P38313
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38313.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P38313: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "AME1"}, "synonyms": [{"value": "ARP100"}], "orderedLocusNames": [{"value":
    "YBR211C"}], "orfNames": [{"value": "YBR1458"}]}]. Native annotation is not a
    substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:10.924869Z'
  support: supports
  snapshot_sha256: 053d6d5cadc71a57b6b685c5ac036757f82d889c4efce071a4a694908c5e0d07
- evidence_id: septin-up-P47149
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47149.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P47149: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "NNF1"}, "orderedLocusNames": [{"value": "YJR112W"}], "orfNames": [{"value":
    "J2011"}]}]. Native annotation is not a substitute for the independently scoped
    experimental source.'
  accessed_at: '2026-11-04T13:21:12.889708Z'
  support: supports
  snapshot_sha256: 44813039d8c829e0a812002be1831fd38c887accf5ef3c34740df83eb00283a8
- evidence_id: septin-up-Q02732
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q02732.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'Q02732: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "CTF19"}, "synonyms": [{"value": "MCM18"}], "orderedLocusNames": [{"value":
    "YPL018W"}], "orfNames": [{"value": "LPB13W"}]}]. Native annotation is not a substitute
    for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:10.120170Z'
  support: supports
  snapshot_sha256: 4300f75049f2449011c3e78557ed639585c8206f4ea707ce6abda1aaa5b6b62d
- evidence_id: septin-up-Q04477
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04477.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'Q04477: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "SPC24"}, "orderedLocusNames": [{"value": "YMR117C"}], "orfNames": [{"value":
    "YM9718.16C"}]}]. Native annotation is not a substitute for the independently
    scoped experimental source.'
  accessed_at: '2026-11-04T13:21:10.250954Z'
  support: supports
  snapshot_sha256: 7c4ad50bf5ae4e1eb7738038fdb2a60c4f3ba91ee1b8fd9f7484489ef732d559
- evidence_id: septin-up-P40568
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40568.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P40568: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "DSN1"}, "orderedLocusNames": [{"value": "YIR010W"}], "orfNames": [{"value":
    "YIB10W"}]}]. Native annotation is not a substitute for the independently scoped
    experimental source.'
  accessed_at: '2026-11-04T13:21:13.914035Z'
  support: supports
  snapshot_sha256: 96137f8354085cb9072053d5c31c4cddc8b6c2c8623b3799b94e7aacad26b4c2
- evidence_id: septin-up-Q12143
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12143.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'Q12143: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "NSL1"}, "orderedLocusNames": [{"value": "YPL233W"}]}]. Native annotation
    is not a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:10.841397Z'
  support: supports
  snapshot_sha256: 95ff5d2d38d1e8a898ac78e592ce030278a36553b4b9da0848c23c911cd96d47
- evidence_id: septin-up-Q06675
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06675.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'Q06675: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "MCM21"}, "synonyms": [{"value": "CTF5"}], "orderedLocusNames": [{"value":
    "YDR318W"}]}]. Native annotation is not a substitute for the independently scoped
    experimental source.'
  accessed_at: '2026-11-04T13:21:12.889634Z'
  support: supports
  snapshot_sha256: a284987a228269755202e144975329d40045d32097395fa0a3b5efbc26dcd801
- evidence_id: septin-up-P36012
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36012.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P36012: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "CSE4"}, "synonyms": [{"value": "CSL2"}], "orderedLocusNames": [{"value":
    "YKL049C"}], "orfNames": [{"value": "YKL262"}]}]. Native annotation is not a substitute
    for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:11.965429Z'
  support: supports
  snapshot_sha256: bca7e7c2253768cc51d28557ea8967dd642ffbff3dff58274cecc9e8fae973f5
- evidence_id: septin-up-P33895
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33895.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P33895: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "NUF2"}, "orderedLocusNames": [{"value": "YOL069W"}]}]. Native annotation
    is not a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:14.934342Z'
  support: supports
  snapshot_sha256: 571967574ce29a5f5b3a43ad0c65267df722a3e258d80aeb78fea83a2b7323fe
- evidence_id: septin-up-P39731
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39731.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P39731: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "MTW1"}, "synonyms": [{"value": "DSN3"}, {"value": "NSL2"}], "orderedLocusNames":
    [{"value": "YAL034W-A"}], "orfNames": [{"value": "YAL034AW"}]}]. Native annotation
    is not a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:11.864693Z'
  support: supports
  snapshot_sha256: b37940b084e0c71e437af46a461aefb2da2688e1d94fe6985d2cba3a837d0822
- evidence_id: septin-up-P40460
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40460.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P40460: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "9585415"}],
    "value": "NDC80"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303",
    "source": "PubMed", "id": "10409732"}], "value": "HEC1"}, {"evidences": [{"evidenceCode":
    "ECO:0000303", "source": "PubMed", "id": "9335591"}], "value": "TID3"}], "orderedLocusNames":
    [{"evidences": [{"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000001406"}],
    "value": "YIL144W"}]}]. Native annotation is not a substitute for the independently
    scoped experimental source.'
  accessed_at: '2026-11-04T13:21:14.015771Z'
  support: supports
  snapshot_sha256: e9118ff7804c75195f78434aabd4f7b07fe4678b12faf54aa90a012fede3f5a6
- evidence_id: septin-up-P53298
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53298.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P53298: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "10323865"}],
    "value": "OKP1"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000312",
    "source": "SGD", "id": "S000003411"}], "value": "YGR179C"}]}]. Native annotation
    is not a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:14.934409Z'
  support: supports
  snapshot_sha256: e286b14d37ffacdfdacead4d28a714fb2cd7647ebcccc49df73d642fe0756906
- evidence_id: septin-up-P40014
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40014.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P40014: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"value": "SPC25"}, "orderedLocusNames": [{"value": "YER018C"}]}]. Native annotation
    is not a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:15.961267Z'
  support: supports
  snapshot_sha256: a89a4a422be89dd670679ec99deba6afbbca7b2af4b4c447c31ab4bdf254eabe
- evidence_id: septin-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxon name, identifiers and lineage
  summary: Saccharomyces cerevisiae identity verified; S288C annotation identity is
    not W303/YKO200 experimental identity.
  accessed_at: '2026-11-04T13:21:13.048356Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native taxon name, identifiers and lineage
  summary: Saccharomyces cerevisiae S288C identity verified; S288C annotation identity
    is not W303/YKO200 experimental identity.
  accessed_at: '2026-11-04T13:21:13.913306Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-pmid-14581449
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14581449+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Architecture of the budding yeast kinetochore reveals a conserved molecular
    core.; Westermann S, Cheeseman IM, Anderson S, Yates JR, Drubin DG, Barnes G..
    Bibliography only; separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:13.913664Z'
  support: context_only
  snapshot_sha256: 7026f730ac7c9df2a948c4d0eef41693aa077d6a52cc991324fbb8aa260443de
- evidence_id: septin-pmid-14581449-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14581449+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:13.913664Z'
  support: supports
  snapshot_sha256: 7026f730ac7c9df2a948c4d0eef41693aa077d6a52cc991324fbb8aa260443de
- evidence_id: septin-pmid-11179222
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11179222+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: The budding yeast proteins Spc24p and Spc25p interact with Ndc80p and Nuf2p
    at the kinetochore and are important for kinetochore clustering and checkpoint
    control.; Janke C, Ortiz J, Lechner J, Shevchenko A, Shevchenko A, Magiera MM,
    Schramm C, Schiebel E.. Bibliography only; separately classified abstract/body
    carries scientific support.
  accessed_at: '2026-11-04T13:21:22.198717Z'
  support: context_only
  snapshot_sha256: b2628bb1e2e12161e07aaa9c50dae7afba2fe664bc5bd7eecffdc6014262aa32
- evidence_id: septin-pmid-11179222-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11179222+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.198717Z'
  support: supports
  snapshot_sha256: b2628bb1e2e12161e07aaa9c50dae7afba2fe664bc5bd7eecffdc6014262aa32
- evidence_id: septin-pmid-10323865
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: A putative protein complex consisting of Ctf19, Mcm21, and Okp1 represents
    a missing link in the budding yeast kinetochore.; Ortiz J, Stemmann O, Rank S,
    Lechner J.. Bibliography only; separately classified abstract/body carries scientific
    support.
  accessed_at: '2026-11-04T13:21:15.142115Z'
  support: context_only
  snapshot_sha256: 3e58cf78ac0eb0ad781fd91bdc3f5929a943057a17195c0a69eaef9350619467
- evidence_id: septin-pmid-10323865-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:15.142115Z'
  support: supports
  snapshot_sha256: 3e58cf78ac0eb0ad781fd91bdc3f5929a943057a17195c0a69eaef9350619467
- evidence_id: septin-pmid-12455957
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12455957+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: 'Nnf1p, Dsn1p, Mtw1p, and Nsl1p: a new group of proteins important for
    chromosome segregation in Saccharomyces cerevisiae.; Euskirchen GM.. Bibliography
    only; separately classified abstract/body carries scientific support.'
  accessed_at: '2026-11-04T13:21:15.142048Z'
  support: context_only
  snapshot_sha256: e3d4ca7d4f6a49a920046912e7220836edae2279314f86b2c16bb976835e6b57
- evidence_id: septin-pmid-12455957-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12455957+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:15.142048Z'
  support: supports
  snapshot_sha256: e3d4ca7d4f6a49a920046912e7220836edae2279314f86b2c16bb976835e6b57
- evidence_id: septin-pmid-14602074
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14602074+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: An Mtw1 complex promotes kinetochore biorientation that is monitored by
    the Ipl1/Aurora protein kinase.; Pinsky BA, Tatsutani SY, Collins KA, Biggins
    S.. Bibliography only; separately classified abstract/body carries scientific
    support.
  accessed_at: '2026-11-04T13:21:15.141963Z'
  support: context_only
  snapshot_sha256: a33f1fcca8e34a2e5fb6bae246236f4c455eb45311883bdc4ee931bf06ef6c54
- evidence_id: septin-pmid-14602074-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14602074+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:15.141963Z'
  support: supports
  snapshot_sha256: a33f1fcca8e34a2e5fb6bae246236f4c455eb45311883bdc4ee931bf06ef6c54
- evidence_id: septin-pmid-11266451
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11266451+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: The Ndc80p complex from Saccharomyces cerevisiae contains conserved centromere
    components and has a function in chromosome segregation.; Wigge PA, Kilmartin
    JV.. Bibliography only; separately classified abstract/body carries scientific
    support.
  accessed_at: '2026-11-04T13:21:22.245788Z'
  support: context_only
  snapshot_sha256: 7b0836c615ec3b273b5236fcf2aa121afc608eab2489af5253a00da562907d37
- evidence_id: septin-pmid-11266451-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11266451+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.245788Z'
  support: supports
  snapshot_sha256: 7b0836c615ec3b273b5236fcf2aa121afc608eab2489af5253a00da562907d37
- evidence_id: septin-pmid-29046335
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Molecular basis for inner kinetochore configuration through RWD domain-peptide
    interactions.; Schmitzberger F, Richter MM, Gordiyenko Y, Robinson CV, Dadlez
    M, Westermann S.. Bibliography only; separately classified abstract/body carries
    scientific support.
  accessed_at: '2026-11-04T13:21:15.852739Z'
  support: context_only
  snapshot_sha256: 3766e86ee9940c55356a077622cef5b1c1d3707f1dbf2eef090e2456106fe1a5
- evidence_id: septin-pmid-29046335-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:15.852739Z'
  support: supports
  snapshot_sha256: 3766e86ee9940c55356a077622cef5b1c1d3707f1dbf2eef090e2456106fe1a5
- evidence_id: septin-pmid-14657030
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14657030+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Nsl1p is essential for the establishment of bipolarity and the localization
    of the Dam-Duo complex.; Scharfenberger M, Ortiz J, Grau N, Janke C, Schiebel
    E, Lechner J.. Bibliography only; separately classified abstract/body carries
    scientific support.
  accessed_at: '2026-11-04T13:21:22.288294Z'
  support: context_only
  snapshot_sha256: 0e471f97148f0d89ff433402030ea5c91fc09cf6c32458a8c98632895a2011d1
- evidence_id: septin-pmid-14657030-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14657030+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.288294Z'
  support: supports
  snapshot_sha256: 0e471f97148f0d89ff433402030ea5c91fc09cf6c32458a8c98632895a2011d1
- evidence_id: septin-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Global analysis of protein localization in budding yeast.; Huh WK, Falvo
    JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.. Bibliography only;
    separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:16.021025Z'
  support: context_only
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
- evidence_id: septin-pmid-14562095-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:16.021025Z'
  support: supports
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
- evidence_id: septin-pmid-11952896
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11952896+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Spc24 interacts with Mps2 and is required for chromosome segregation, but
    is not implicated in spindle pole body duplication.; Le Masson I, Saveanu C, Chevalier
    A, Namane A, Gobin R, Fromont-Racine M, Jacquier A, Mann C.. Bibliography only;
    separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:22.293206Z'
  support: context_only
  snapshot_sha256: 3a569ebfbd9153bce8ca568b499115101e287ffbb0f4660a0b5e386307409a97
- evidence_id: septin-pmid-11952896-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11952896+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.293206Z'
  support: supports
  snapshot_sha256: 3a569ebfbd9153bce8ca568b499115101e287ffbb0f4660a0b5e386307409a97
- evidence_id: septin-query-CSE4-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACSE4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P36012. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:17.120849Z'
  support: supports
  snapshot_sha256: b3d552919a546bf02e7e024ef2ce711793c53ee54b826e9faddd36e1c711e4c9
  search_scope: 'database: UniProtKB; query: (gene_exact:CSE4) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:17.120849Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-CTF19-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACTF19%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: Q02732. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:16.944618Z'
  support: supports
  snapshot_sha256: a9a47e880c6ddf126c5a8cfc5e899ce09ebe7ebc7a00b39ff7594e40f4a32309
  search_scope: 'database: UniProtKB; query: (gene_exact:CTF19) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:16.944618Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-OKP1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AOKP1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P53298. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:17.117173Z'
  support: supports
  snapshot_sha256: cbe45d27fdfe19adae898e1527e55b3a9c8b4ecc618ec106ea301c3e7c94c4a3
  search_scope: 'database: UniProtKB; query: (gene_exact:OKP1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:17.117173Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-MCM21-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMCM21%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: Q06675. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:18.110026Z'
  support: supports
  snapshot_sha256: a3cc24e2df5723fb6cec03e1893aaf4548a563624f8dc245d6c6e518e7334abd
  search_scope: 'database: UniProtKB; query: (gene_exact:MCM21) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:18.110026Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-AME1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAME1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P38313. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:18.109894Z'
  support: supports
  snapshot_sha256: 0d24b7575005296c4ba534d40d5e66dd54a2d6aebf6625ad1180ceb8ff885018
  search_scope: 'database: UniProtKB; query: (gene_exact:AME1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:18.109894Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-MTW1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMTW1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P39731. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:21.082739Z'
  support: supports
  snapshot_sha256: 4e1c13f94acaeac92e3bd48e22247f98dd74e7ad41dc26a37b6d69c904646d51
  search_scope: 'database: UniProtKB; query: (gene_exact:MTW1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:21.082739Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-DSN1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSN1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P40568. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:24.980054Z'
  support: supports
  snapshot_sha256: 33d7623f58dbfaaa46ba87f4147bb0903002d81d5cab87589771b415136dffb6
  search_scope: 'database: UniProtKB; query: (gene_exact:DSN1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:24.980054Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-NSL1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: Q12143. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:18.996403Z'
  support: supports
  snapshot_sha256: 7e452ae2cb97c8e5816fec9b342591a9b9c637a8e0a5f9cb4426019af035dc19
  search_scope: 'database: UniProtKB; query: (gene_exact:NSL1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:18.996403Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-NNF1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANNF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P47149. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:19.011759Z'
  support: supports
  snapshot_sha256: c3360e0ca5a435d02211fbfbe88566357a5f1e4a1b3658ef3a9ee3e7eadda293
  search_scope: 'database: UniProtKB; query: (gene_exact:NNF1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:19.011759Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-NDC80-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANDC80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P40460. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:20.026830Z'
  support: supports
  snapshot_sha256: cb9e2605da1af744ac1cc58f6ff8bc03bd477da0d59ba0361168eca14361e1dc
  search_scope: 'database: UniProtKB; query: (gene_exact:NDC80) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:20.026830Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-NUF2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANUF2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P33895. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:19.942510Z'
  support: supports
  snapshot_sha256: bf43297dd64c38303056413208f9510db1c067a22e6649517a171a0292db1d07
  search_scope: 'database: UniProtKB; query: (gene_exact:NUF2) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:19.942510Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-SPC24-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPC24%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: Q04477. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:21.096235Z'
  support: supports
  snapshot_sha256: bd05a8bed40ca05510ff106131c3f13e1b21aab5c8d4e54f4e340e8f45786292
  search_scope: 'database: UniProtKB; query: (gene_exact:SPC24) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:21.096235Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-SPC25-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPC25%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P40014. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:21.933134Z'
  support: supports
  snapshot_sha256: d4a85f3c865f28fd598736cb170c803b1e3cb8d91105103746f3c78450d9f785
  search_scope: 'database: UniProtKB; query: (gene_exact:SPC25) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:21.933134Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-up-Q13342
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q13342.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'Q13342: UniProtKB reviewed (Swiss-Prot); taxon 9606; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000312", "source": "HGNC", "id": "HGNC:17133"}],
    "value": "SP140"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303",
    "source": "PubMed", "id": "8695863"}], "value": "LYSP100"}]}]. Native annotation
    is not a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:21.906320Z'
  support: supports
  snapshot_sha256: 1ca48edbb0de5521968ad68e86b4df106c225d9d44713e7a6e8822fb9b48b11d
- evidence_id: septin-up-Q99856
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q99856.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'Q99856: UniProtKB reviewed (Swiss-Prot); taxon 9606; genes [{"geneName":
    {"value": "ARID3A"}, "synonyms": [{"value": "DRIL1"}, {"value": "DRIL3"}, {"value":
    "DRX"}, {"value": "E2FBP1"}]}]. Native annotation is not a substitute for the
    independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:23.146694Z'
  support: supports
  snapshot_sha256: fb86b98d83c2577e4851fe5033d8fc521fbf9d332623f823507e25bce306c332
- evidence_id: septin-tax-9606
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/9606
  locator: Native taxon name, identifiers and lineage
  summary: Homo sapiens identity verified; S288C annotation identity is not W303/YKO200
    experimental identity.
  accessed_at: '2026-11-04T13:21:22.501476Z'
  support: supports
  snapshot_sha256: 43da11bd5ae67c7de16256e9a9f3d3f90f4d70315de700d16c290352aa7b94ba
- evidence_id: septin-pmid-8910577
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910577+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Identification and characterization of a leukocyte-specific component of
    the nuclear body.; Bloch DB, de la Monte SM, Guigaouri P, Filippov A, Bloch KD..
    Bibliography only; separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:22.593694Z'
  support: context_only
  snapshot_sha256: 7d3ba4a8e7dc777b667d98ff34f114c653dc824a6cc8b4971293c0c78c9672c9
- evidence_id: septin-pmid-8910577-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910577+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.593694Z'
  support: supports
  snapshot_sha256: 7d3ba4a8e7dc777b667d98ff34f114c653dc824a6cc8b4971293c0c78c9672c9
- evidence_id: septin-pmid-8695863
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8695863+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: 'LYSP100-associated nuclear domains (LANDs): description of a new class
    of subnuclear structures and their relationship to PML nuclear bodies.; Dent AL,
    Yewdell J, Puvion-Dutilleul F, Koken MH, de The H, Staudt LM.. Bibliography only;
    separately classified abstract/body carries scientific support.'
  accessed_at: '2026-11-04T13:21:22.793236Z'
  support: context_only
  snapshot_sha256: e39d1441f1eb727b03a4a4b4f57bdc66f395b529f56a0957f143168edc55be87
- evidence_id: septin-pmid-8695863-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8695863+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.793236Z'
  support: supports
  snapshot_sha256: e39d1441f1eb727b03a4a4b4f57bdc66f395b529f56a0957f143168edc55be87
- evidence_id: septin-pmid-25593309
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25593309+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Screen identifies bromodomain protein ZMYND8 in chromatin recognition of
    transcription-associated DNA damage that promotes homologous recombination.; Gong
    F, Chiu LY, Cox B, Aymard F, Clouaire T, Leung JW, Cammarata M, Perez M, Agarwal
    P, Brodbelt JS, Legube G, Miller KM.. Bibliography only; separately classified
    abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:22.861014Z'
  support: context_only
  snapshot_sha256: e374cab9b51f676a72bd9685d180ea7e641604a8ec6e4e5cb17a52a691c48f8a
- evidence_id: septin-pmid-25593309-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25593309+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:22.861014Z'
  support: supports
  snapshot_sha256: e374cab9b51f676a72bd9685d180ea7e641604a8ec6e4e5cb17a52a691c48f8a
- evidence_id: septin-query-SP140-9606
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASP140%29+AND+%28organism_id%3A9606%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: Q13342. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:25.087677Z'
  support: supports
  snapshot_sha256: 9a7e8c825872a5904efa07a2ba86f90816167d8403ae5eb68b0423259f58744d
  search_scope: 'database: UniProtKB; query: (gene_exact:SP140) AND (organism_id:9606)
    AND (reviewed:true); date: 2026-11-04T13:21:25.087677Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-up-P39925
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39925.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P39925: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "7900428"},
    {"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000000819"}], "value":
    "AFG3"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303", "source":
    "PubMed", "id": "7754704"}], "value": "YTA10"}], "orderedLocusNames": [{"value":
    "YER017C"}]}]. Native annotation is not a substitute for the independently scoped
    experimental source.'
  accessed_at: '2026-11-04T13:21:22.949962Z'
  support: supports
  snapshot_sha256: ba6d52d637428ee249abe1a64cefcf20fa7f4b93eb6690d058996632a75404cb
- evidence_id: septin-up-P40341
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40341.json
  locator: Complete native identity; gene primary/alias/locus fields, status/taxon;
    FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments, isoforms and family cross-references
  summary: 'P40341: UniProtKB reviewed (Swiss-Prot); taxon 559292; genes [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000303", "source": "PubMed", "id": "7754704"},
    {"evidenceCode": "ECO:0000312", "source": "SGD", "id": "S000004695"}], "value":
    "YTA12"}, "synonyms": [{"evidences": [{"evidenceCode": "ECO:0000303", "source":
    "PubMed", "id": "7929327"}], "value": "RCA1"}], "orderedLocusNames": [{"value":
    "YMR089C"}], "orfNames": [{"value": "YM9582.14C"}]}]. Native annotation is not
    a substitute for the independently scoped experimental source.'
  accessed_at: '2026-11-04T13:21:23.836902Z'
  support: supports
  snapshot_sha256: b90dc68c81d617ff17b4f56722ce0707fca1e8b3a6ade35fd5cbe15834dbcc88
- evidence_id: septin-pmid-7929327
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7929327+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: A new member of a family of ATPases is essential for assembly of mitochondrial
    respiratory chain and ATP synthetase complexes in Saccharomyces cerevisiae.; Tzagoloff
    A, Yue J, Jang J, Paul MF.. Bibliography only; separately classified abstract/body
    carries scientific support.
  accessed_at: '2026-11-04T13:21:24.648186Z'
  support: context_only
  snapshot_sha256: e351c659609e8da0a49504268450230035023def2e86a100c8a1b566c0dab648
- evidence_id: septin-pmid-7929327-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A7929327+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:24.648186Z'
  support: supports
  snapshot_sha256: e351c659609e8da0a49504268450230035023def2e86a100c8a1b566c0dab648
- evidence_id: septin-pmid-21147776
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21147776+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Electron cryomicroscopy structure of a membrane-anchored mitochondrial
    AAA protease.; Lee S, Augustin S, Tatsuta T, Gerdes F, Langer T, Tsai FT.. Bibliography
    only; separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:23.441487Z'
  support: context_only
  snapshot_sha256: 312d361f1bc96b38b67df6af6bae4b6705d0c617eed3aff3c13155f4374ffd80
- evidence_id: septin-pmid-21147776-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21147776+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:23.441487Z'
  support: supports
  snapshot_sha256: 312d361f1bc96b38b67df6af6bae4b6705d0c617eed3aff3c13155f4374ffd80
- evidence_id: septin-pmid-8681382
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8681382+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: The YTA10-12 complex, an AAA protease with chaperone-like activity in the
    inner membrane of mitochondria.; Arlt H, Tauer R, Feldmann H, Neupert W, Langer
    T.. Bibliography only; separately classified abstract/body carries scientific
    support.
  accessed_at: '2026-11-04T13:21:23.847794Z'
  support: context_only
  snapshot_sha256: 049a4c12e1e57eaee305a820dc31f82637497fa9856bd9c21b1d1e7cc9466105
- evidence_id: septin-pmid-8681382-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8681382+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:23.847794Z'
  support: supports
  snapshot_sha256: 049a4c12e1e57eaee305a820dc31f82637497fa9856bd9c21b1d1e7cc9466105
- evidence_id: septin-query-AFG3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAFG3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P39925. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:26.018892Z'
  support: supports
  snapshot_sha256: 3c72a44e12666da642d1b2b6926d6434f4cf59b27d53795e854f99972d68e9d7
  search_scope: 'database: UniProtKB; query: (gene_exact:AFG3) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:26.018892Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-query-YTA12-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYTA12%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete current returned identities, primary names and aliases
  summary: 'Current query returns 1 entry: P40341. Does not reconstruct historical
    searches or establish biological absence.'
  accessed_at: '2026-11-04T13:21:24.020617Z'
  support: supports
  snapshot_sha256: d229aa45ae04433f17193b47828d47561f02553fe6d47e635265c76dd0cfc173
  search_scope: 'database: UniProtKB; query: (gene_exact:YTA12) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T13:21:24.020617Z; limit: size=100; complete
    returned one-page result; primary/alias distinction retained'
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444,GO:0000776,GO:0000817,GO:0004176,GO:0005743,GO:0005745,GO:0007059,GO:0016604,GO:0016605,GO:0016606,GO:0031262,GO:0031981,GO:0034982,GO:0098800,GO:1905368
  locator: 'Complete native term response: identifier/name/status/definition/synonyms/typed
    relationships or requested is_a ancestors'
  summary: Current exact GO identities verified. GO0043505 denotes the whole CENP-A
    nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and
    from a direct versus inherited ontology relation.
  accessed_at: '2026-11-04T13:21:24.042389Z'
  support: supports
  snapshot_sha256: 4579b2e5040b980ef3c76e0b8e2838c5b3522c60dc288ae1f42ddd374d9a42c3
- evidence_id: septin-go-0000776-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776/ancestors?relations=is_a
  locator: 'Complete native term response: identifier/name/status/definition/synonyms/typed
    relationships or requested is_a ancestors'
  summary: Current exact GO identities verified. GO0043505 denotes the whole CENP-A
    nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and
    from a direct versus inherited ontology relation.
  accessed_at: '2026-11-04T13:21:24.430967Z'
  support: supports
  snapshot_sha256: abafadbe6273a784ab51f1ebaa39abfccb54b8022354c9b1f21faf99f99cdf49
- evidence_id: septin-go-0016606-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016606/ancestors?relations=is_a
  locator: 'Complete native term response: identifier/name/status/definition/synonyms/typed
    relationships or requested is_a ancestors'
  summary: Current exact GO identities verified. GO0043505 denotes the whole CENP-A
    nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and
    from a direct versus inherited ontology relation.
  accessed_at: '2026-11-04T13:21:24.445499Z'
  support: supports
  snapshot_sha256: 80795cf10b2383ea69c6793d595d053bf98643aa18b6acd1123bdc276bc84203
- evidence_id: septin-go-0005745-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005745/ancestors?relations=is_a
  locator: 'Complete native term response: identifier/name/status/definition/synonyms/typed
    relationships or requested is_a ancestors'
  summary: Current exact GO identities verified. GO0043505 denotes the whole CENP-A
    nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and
    from a direct versus inherited ontology relation.
  accessed_at: '2026-11-04T13:21:24.600272Z'
  support: supports
  snapshot_sha256: d606613872c55d9e51198cf32d6d4f403bde15f01f07179a60fa6c62bf7e87f5
- evidence_id: septin-go-cenpa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043505
  locator: 'Complete native term response: identifier/name/status/definition/synonyms/typed
    relationships or requested is_a ancestors'
  summary: Current exact GO identities verified. GO0043505 denotes the whole CENP-A
    nucleosome, not Cse4 alone. Biological parthood is distinguished from is-a and
    from a direct versus inherited ontology relation.
  accessed_at: '2026-11-04T13:21:24.666539Z'
  support: supports
  snapshot_sha256: ef6a95bddfb44836946f94f6cebc2e43458d66369ee0400ab2b2a9ca13148139
- evidence_id: septin-westermann-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200305100%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Architecture of the budding yeast kinetochore reveals a conserved molecular
    core.; Westermann S, Cheeseman IM, Anderson S, Yates JR, Drubin DG, Barnes G..
    Bibliography only; separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:25.167124Z'
  support: context_only
  snapshot_sha256: 861ab62ed7fdbe40ff4469681a4e79d1200d50a9c901b0d1d6f8171934caf55e
- evidence_id: septin-westermann-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200305100%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:25.167124Z'
  support: supports
  snapshot_sha256: 861ab62ed7fdbe40ff4469681a4e79d1200d50a9c901b0d1d6f8171934caf55e
- evidence_id: septin-dewulf-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144403%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Hierarchical assembly of the budding yeast kinetochore from multiple subcomplexes.;
    De Wulf P, McAinsh AD, Sorger PK.. Bibliography only; separately classified abstract/body
    carries scientific support.
  accessed_at: '2026-11-04T13:21:25.250828Z'
  support: context_only
  snapshot_sha256: 6102ca718aa71bb04ef1470b2846ec952ee00a5326b5fdcda1da526f47565e4b
- evidence_id: septin-dewulf-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144403%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:25.250828Z'
  support: supports
  snapshot_sha256: 6102ca718aa71bb04ef1470b2846ec952ee00a5326b5fdcda1da526f47565e4b
- evidence_id: septin-biggins-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fgenetics.112.145276%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: The composition, functions, and regulation of the budding yeast kinetochore.;
    Biggins S.. Bibliography only; separately classified abstract/body carries scientific
    support.
  accessed_at: '2026-11-04T13:21:25.292180Z'
  support: context_only
  snapshot_sha256: bdeb619152afa1ec229da5e54b0575b616441d5b5eb1827c5932135ee701e6fb
- evidence_id: septin-biggins-metadata-abstract
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fgenetics.112.145276%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Secondary Biggins synthesis, not an independent primary experiment.
  accessed_at: '2026-11-04T13:21:25.292180Z'
  support: supports
  snapshot_sha256: bdeb619152afa1ec229da5e54b0575b616441d5b5eb1827c5932135ee701e6fb
- evidence_id: septin-zong-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1093%2Femboj%2F19.15.4123%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Regulation of matrix attachment region-dependent, lymphocyte-restricted
    transcription through differential localization within promyelocytic leukemia
    nuclear bodies.; Zong RT, Das C, Tucker PW.. Bibliography only; separately classified
    abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:34.204978Z'
  support: context_only
  snapshot_sha256: b1c576b28ad5448c6fa4da212a08295fab1089a635edc056b7866d7172efa3f5
- evidence_id: septin-zong-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1093%2Femboj%2F19.15.4123%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:34.204978Z'
  support: supports
  snapshot_sha256: b1c576b28ad5448c6fa4da212a08295fab1089a635edc056b7866d7172efa3f5
- evidence_id: septin-luo-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-026-73040-0%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Structural basis for prohibitin-mediated regulation of mitochondrial m-AAA
    protease.; Luo D, Zheng L, Lu MA, Chen Z, Wang P, Guo Q, Gao N.. Bibliography
    only; separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:25.960035Z'
  support: context_only
  snapshot_sha256: adcc7d956654c186686db84715666010d04b8a1ddace679d9f2056fe0bc0aeb8
- evidence_id: septin-luo-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41467-026-73040-0%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:25.960035Z'
  support: supports
  snapshot_sha256: adcc7d956654c186686db84715666010d04b8a1ddace679d9f2056fe0bc0aeb8
- evidence_id: septin-lee-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.158741%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Exact MED metadata: title, authors, date, DOI/PMID and abstract availability'
  summary: Electron cryomicroscopy structure of a membrane-anchored mitochondrial
    AAA protease.; Lee S, Augustin S, Tatsuta T, Gerdes F, Langer T, Tsai FT.. Bibliography
    only; separately classified abstract/body carries scientific support.
  accessed_at: '2026-11-04T13:21:26.795279Z'
  support: context_only
  snapshot_sha256: fc68d74515713f40bcff1a0338b9c50895d37809f88547df8cb0e8de75f2649f
- evidence_id: septin-lee-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.158741%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no unlisted Methods, figure or supplement
    access implied
  summary: Complete primary abstract independently read. Its stated experiment, species
    and uncertainty are retained; no hidden body/strain detail is inferred.
  accessed_at: '2026-11-04T13:21:26.795279Z'
  support: supports
  snapshot_sha256: fc68d74515713f40bcff1a0338b9c50895d37809f88547df8cb0e8de75f2649f
- evidence_id: septin-ipr-IPR043563
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR043563/
  locator: Native accession/name/type/member signatures and curation flags; native
    UniProt cross-references compared
  summary: 'IPR043563 {''name'': ''Nuclear body protein Sp110/Sp140/Sp140L-like'',
    ''short'': ''Sp110/Sp140/Sp140L-like''}; type family. Family versus domain and
    paralogue coverage distinguished; descriptive prose does not establish necessity.'
  accessed_at: '2026-11-04T13:21:27.487931Z'
  support: supports
  snapshot_sha256: e2ba723108e50754180ad0e7cc9b915e06a30f2de13241eb7a84c978eee961ed
- evidence_id: septin-ipr-IPR030411
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030411/
  locator: Native accession/name/type/member signatures and curation flags; native
    UniProt cross-references compared
  summary: 'IPR030411 {''name'': ''Nuclear body protein Sp140, bromodomain'', ''short'':
    ''Sp140_Bromo''}; type domain. Family versus domain and paralogue coverage distinguished;
    descriptive prose does not establish necessity.'
  accessed_at: '2026-11-04T13:21:27.597693Z'
  support: supports
  snapshot_sha256: 5b4f5ae80ac063073f2f63fee038bd5c751914cd2d5f04ad91faa8c72cf95009
- evidence_id: septin-ipr-IPR050928
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050928/
  locator: Native accession/name/type/member signatures and curation flags; native
    UniProt cross-references compared
  summary: 'IPR050928 {''name'': ''ATP-dependent Zinc Metalloprotease'', ''short'':
    ''ATP-dep_Zn_Metalloprotease''}; type family. Unchecked machine-generated biological
    prose excluded; only native identity/classification used.'
  accessed_at: '2026-11-04T13:21:27.568568Z'
  support: supports
  snapshot_sha256: 7f31eb4bb71dde8d23574aad78c92ae317657e84b8961945ae8fc79d41a1b315
- evidence_id: septin-ipr-IPR005936
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005936/
  locator: Native accession/name/type/member signatures and curation flags; native
    UniProt cross-references compared
  summary: 'IPR005936 {''name'': ''ATP-dependent zinc metalloprotease, FtsH'', ''short'':
    ''FtsH''}; type family. Family versus domain and paralogue coverage distinguished;
    descriptive prose does not establish necessity.'
  accessed_at: '2026-11-04T13:21:27.697476Z'
  support: supports
  snapshot_sha256: 6d706dbe689ac3fbe1f2fa131c38f2c451b7e8e8d105e431cac431c1d1fe413c
- evidence_id: septin-ipr-IPR011546
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011546/
  locator: Actual failed HTTP response
  summary: HTTP 429 does not supply usable family evidence; separate successful retry
    retains its own time/hash.
  accessed_at: '2026-11-04T13:21:28.075074Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-retry-IPR011546
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011546/
  locator: Native accession/name/type/member signatures and curation flags; native
    UniProt cross-references compared
  summary: 'IPR011546 {''name'': ''Peptidase M41, FtsH extracellular'', ''short'':
    ''Pept_M41_FtsH_extracell''}; type domain. Family versus domain and paralogue
    coverage distinguished; descriptive prose does not establish necessity.'
  accessed_at: '2026-11-04T13:22:10.813185Z'
  support: supports
  snapshot_sha256: 938434518b50d2086d8d2165221a28c333026017d4126647103409a065ffe7c9
- evidence_id: septin-panther-retry-SP140
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR46386/
  locator: Native accession/name/type/member signatures and curation flags; native
    UniProt cross-references compared
  summary: 'PTHR46386 {''name'': ''NUCLEAR BODY PROTEIN SP140'', ''short'': None};
    type family. Family versus domain and paralogue coverage distinguished; descriptive
    prose does not establish necessity.'
  accessed_at: '2026-11-04T13:22:10.862065Z'
  support: supports
  snapshot_sha256: b912bcf6a56f167b7309dbd31586c9a0a3c777ae24a869216f3a4d494254b860
- evidence_id: septin-westermann-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2173538/fullTextXML
  locator: Genuine JATS sections3–7 and Methods9/10/12/13; full relevant text and
    embedded captions, not supplement or pixels
  summary: Purified Cse4 material includes H2A/H2B/H4 without detectable H3; MIND
    identities and conditional CEN occupancy support a coarse yeast core. Tagged preparations
    used300mM KCl; conditional occupancy/stability is not complete-kinetochore formation
    or universal stoichiometry. Exact strain table was not opened.
  accessed_at: '2026-11-04T13:21:26.686461Z'
  support: supports
  snapshot_sha256: 3b73205f56276092dc53bee8db153b161db527f40d9c9b7ed88b11556df53bcd
- evidence_id: septin-dewulf-ncbi
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC289150/
  locator: 'Genuine NCBI main article: abstract; Results hydrodynamic/COMA/MIND composition
    and conditional dependency sections through Fig6; Methods strains/biochemistry/microscopy;
    embedded relevant captions'
  summary: W303-congenic preparations distinguish stable COMA/MIND/Ndc80 complexes
    from variable co-purifications. Conditional24/37C perturbations, CEN occupancy
    and protein stability are separate from universal assembly necessity. COMA nonessential
    Ctf19/Mcm21 and residual subcomplexes are explicit. No supplementary tables or
    pixels inspected.
  accessed_at: '2026-11-04T13:23:06.664328Z'
  support: supports
  snapshot_sha256: 06330b966c1e3b1491c365bbb913e644ff9d524a89a722acfee55225ffce79bf
- evidence_id: septin-biggins-ncbi
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730914/
  locator: 'Genuine secondary review: complete abstract; Centromeric chromatin paragraphs,
    composition/CBF3/CCAN and architecture sections actually read; no figure pixels'
  summary: Secondary synthesis supports coarse centromeric platform and inner/outer
    hierarchy while explicitly discussing disputed Cse4 nucleosome arrangements and
    unresolved minimal assembly requirements. No fixed octameric stoichiometry or
    all-or-none formation rule is imported.
  accessed_at: '2026-11-04T13:23:06.841662Z'
  support: supports
  snapshot_sha256: f5df14e67b01f7e5ff5cc32aafb914c1b5c68664da21b7b7974b1b35fce92024
- evidence_id: septin-zong-ncbi
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC306587/
  locator: 'Genuine NCBI main body: Introduction, Results interaction/reporter/redistribution/matrix
    sections; Discussion; Methods and embedded relevant figure captions'
  summary: Human lymphocyte cDNA/LYSp100B, J558L mouse plasmacytoma reporter and HeLa/Jurkat
    comparisons are distinct. LYSp100B interacts in vitro; in-vivo co-IP was not detected.
    Overexpressed Bright redistributes LYSp100B, and reporter coactivation occurs
    in J558 but not HeLa/Jurkat. The proposed endogenous/coactivation mechanism and
    nuclear-domain formation necessity are not directly established. Human ARID3A
    reference xref does not make every source construct human.
  accessed_at: '2026-11-04T13:23:06.651877Z'
  support: supports
  snapshot_sha256: 49186001875791fe0c52b2e6e8b378c7808664f937bbe7c96b0b68fa3480c7a9
- evidence_id: septin-lee-ncbi
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3039362/
  locator: 'Genuine NCBI primary main article: abstract/Introduction, Experimental
    Procedures, Results and Discussion, embedded captions; no supplement, pixels or
    raw map analysis'
  summary: YKO200 genetic rescue and purified ATP-hydrolysis-deficient Trap Yta10E388Q/His6-Yta12E448Q
    preparations are explicit. Roughly equimolar purified proteins and a cross-linked
    detergent/C6 12-angstrom model support a preparation-specific hexamer. The map
    cannot distinguish paralogs; alternating assignment is inferred from prior biochemistry.
    No count of zinc ions is established by the inspected preparation source.
  accessed_at: '2026-11-04T13:23:06.619539Z'
  support: supports
  snapshot_sha256: 2b75dbbe8b2dc504b6bcb6d706c344d9e4bdb96641bdb510bff07301270d6e0f
- evidence_id: septin-luo-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13376388/fullTextXML
  locator: Genuine JATS Introduction; Results conserved PHB-protease interaction and
    yeast Fig4 perturbation; Discussion; yeast engineering, MrpL32 processing and
    stress Methods; exact embedded Fig4 caption and license
  summary: W303-1B endogenous Yta12 residues236–251 or199–290 replaced withGGGGGS;
    TEF-driven C-terminal Strep MrpL32 reporter precursor/total endpoint after14hYPG30C,
    four biological replicates. PHB1 loss/SIM replacement lower precursor fraction,
    IMSD replacement raises it; separate YPG2mMH2O2 growth assays do not prove a reporter-to-stress
    causal link. Ct/human co-purification/predicted interfaces are not atomic yeast
    contacts or compulsory protease constituents.
  accessed_at: '2026-11-04T13:21:27.091588Z'
  support: supports
  snapshot_sha256: a60bd87a9adc48722fb9a683bbc7646922857b2e838ebd3566215fe0d7fffa59
- evidence_id: septin-luo-fig4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC13376388.1/41467_2026_73040_Fig4_HTML.jpg
  locator: 'Actual external figure pixels viewed: panelsA–D and matching JATS caption;
    raw JPG/MD5 checked'
  summary: Immunoblots, precursor quantification and plate dilution panels match the
    retained source-scoped interpretation. MD5 8437fa5c981491200b4243f15c6cef68 matches
    the link-only record. CC BY-NC-ND4.0 and attribution verified in genuine JATS;
    no figure file is copied into the repository.
  accessed_at: '2026-11-04T13:21:26.871747Z'
  support: supports
  snapshot_sha256: 947ef911cb232b3154b441fc7f8ed08c1d66c1af316a45627b9f563c16e8f28d
- evidence_id: septin-cpx-1654
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1654
  locator: Complete native composition, participants/roles, annotations/properties/evidence
    and null stochiometry fields
  summary: CPX-1654 identifies P40341/YTA12, P39925/AFG3 and CHEBI29105 zinc with
    enzyme/cofactor roles. All three participant stochiometry fields are null; full
    inspected response does not supply3:3 or6zinc. Source reference taxon559292, labelSaccharomyces
    cerevisiae, MW1000kDa and physical-interaction evidence remain scoped annotations.
  accessed_at: '2026-11-04T13:21:27.520255Z'
  support: supports
  snapshot_sha256: ca916f3df6180e8b0a30d57683bef1fc23c6e7f39b708e6320cfbb85ef4c654e
- evidence_id: septin-emdb-1712-wwpdb
  kind: database
  reference: https://files.wwpdb.org/pub/emdb/structures/EMD-1712/header/emd-1712.xml
  locator: 'Complete released EMD-1712 XML header: citation, specimen, composition,
    method/reconstruction'
  summary: Header records3Yta10+3Yta12 in a recombinant glutaraldehyde-cross-linked
    detergent preparation,5mMATP/10mMMgCl2,C6,12angstrom,0.5MDa. SupersedesEMD1543.
    No zinc count in this inspected header; source preparation is not universal physiology
    or resolved alternating identity.
  accessed_at: '2026-11-04T13:22:11.295584Z'
  support: supports
  snapshot_sha256: 723a9513e5b5082264156a59e0bfd49f7e168af9596506a9a0d286446fca0ad4
- evidence_id: septin-chebi-29105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29105
  locator: Complete exact native ChEBI identity, charge/formula/name and synonyms
  summary: CHEBI29105 is active zinc(2+), formulaZn, charge+2. This verifies cofactor
    identity, not molecular copy count.
  accessed_at: '2026-11-04T13:21:27.555199Z'
  support: supports
  snapshot_sha256: 1710e73dbe5e68523715fe5378901b0c97d35f0260bbf9aeb00b0c390e464e0f
- evidence_id: septin-panther-retry-SP140-members
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100
  locator: Complete returned twelve reviewed member identities and pagination
  summary: PTHR46386 includes SP140 but also SP100,SP110,SP140L and AIRE proteins.
    Its display name does not make it exact to LYSp100B; no exhaustive claim about
    all possible family databases.
  accessed_at: '2026-11-04T13:22:12.084455Z'
  support: supports
  snapshot_sha256: 0ebef401307b7308b52d811757435cc52ac8b3b8ee96f4af5158dacbbc83f499
  search_scope: 'database: InterPro API reviewed UniProt members for PANTHER PTHR46386;
    query: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100;
    date: 2026-11-04T13:22:12.084455Z; limit: page_size=100; count12,nextnull, all
    twelve identities inspected'
- evidence_id: septin-dewulf-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC275422/fullTextXML
  locator: Actual HTTP/content diagnostic only
  summary: Initial guessed wrong-PMC route, not the De Wulf target identity; diagnostic
    only and excluded from target-paper access conclusions.
  accessed_at: '2026-11-04T13:21:26.386060Z'
  support: context_only
  snapshot_sha256: 34e33b2d97fd8d5d2462dcba23f5d2b0bc4e5dfc6fe62744bfe1bf6862c74941
- evidence_id: septin-biggins-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3730914/fullTextXML
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 500; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:21:26.960982Z'
  support: context_only
  snapshot_sha256: 34e33b2d97fd8d5d2462dcba23f5d2b0bc4e5dfc6fe62744bfe1bf6862c74941
- evidence_id: septin-zong-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC306587/fullTextXML
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 500; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:21:26.820603Z'
  support: context_only
  snapshot_sha256: 34e33b2d97fd8d5d2462dcba23f5d2b0bc4e5dfc6fe62744bfe1bf6862c74941
- evidence_id: septin-lee-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3039362/fullTextXML
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 500; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:21:27.668225Z'
  support: context_only
  snapshot_sha256: 32d0ab51d33009b3d083977eb290c0d8be3a0c751cd320854d0abcaa64a6090c
- evidence_id: septin-emdb-1712
  kind: validation
  reference: https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-1712/header/emd-1712.xml
  locator: Actual HTTP/content diagnostic only
  summary: Transport connection refused before an HTTP response; no source header
    read through this route. The separate released wwPDB XML succeeded and is the
    inspected authority.
  accessed_at: '2026-11-04T13:21:26.943553Z'
  support: context_only
  snapshot_sha256: fb8850cdde0e901a5a9db57f944ed3afcc0057b494e692f6c3b5f9085867f2e4
- evidence_id: septin-panther-SP140
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR46386/
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 429; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:21:28.121515Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-panther-SP140-members
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/panther/PTHR46386/?page_size=100
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 429; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:21:28.137630Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-dewulf-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/
  locator: Actual HTTP/content diagnostic only
  summary: HTTP200 browser-check/proof-of-work page; not genuine paper text. A later
    genuine NCBI article is independently classified.
  accessed_at: '2026-11-04T13:22:10.161035Z'
  support: context_only
  snapshot_sha256: c0ae120fe75f63a82e8321ada940e42d9127649c1c0f7b44fb5c4ba158e6f0ee
- evidence_id: septin-dewulf-s3xml
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC289150.1/PMC289150.1.xml
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 404; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:22:10.272685Z'
  support: context_only
  snapshot_sha256: 6c60bb88a171737b7755a33dd5c7954bfa6dc7f077d8973319f628741acdeaae
- evidence_id: septin-biggins-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3730914/
  locator: Actual HTTP/content diagnostic only
  summary: HTTP200 browser-check/proof-of-work page; not genuine paper text. A later
    genuine NCBI article is independently classified.
  accessed_at: '2026-11-04T13:22:10.163408Z'
  support: context_only
  snapshot_sha256: ea9cc5ed6e5052693a78d8ab85ddf7222a260662a454dadbc9690b38a1b7b047
- evidence_id: septin-biggins-s3xml
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3730914.1/PMC3730914.1.xml
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 404; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:22:10.259093Z'
  support: context_only
  snapshot_sha256: bb1059989c664e16bec13b46b4b4593953b3e6572b7e809eaa5ee1c7e781259f
- evidence_id: septin-zong-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC306587/
  locator: Actual HTTP/content diagnostic only
  summary: HTTP200 browser-check/proof-of-work page; not genuine paper text. A later
    genuine NCBI article is independently classified.
  accessed_at: '2026-11-04T13:22:10.185096Z'
  support: context_only
  snapshot_sha256: 70d17b80b263b090fa8fc5fb415bf31c17367b3445b5a001e26fcb420648dcf7
- evidence_id: septin-zong-s3xml
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC306587.1/PMC306587.1.xml
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 404; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:22:10.266598Z'
  support: context_only
  snapshot_sha256: 8902790f6d7a6a6673a8e29bf9aa22bf3ee10ba666f92825c660dba5a1a63e67
- evidence_id: septin-lee-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3039362/
  locator: Actual HTTP/content diagnostic only
  summary: HTTP200 browser-check/proof-of-work page; not genuine paper text. A later
    genuine NCBI article is independently classified.
  accessed_at: '2026-11-04T13:22:10.169921Z'
  support: context_only
  snapshot_sha256: 16671060abd88ffbb3770164b7cc2524cdd799975a5c7b7bad5f7083e0998cdd
- evidence_id: septin-lee-s3xml
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3039362.1/PMC3039362.1.xml
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 404; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:22:10.278770Z'
  support: context_only
  snapshot_sha256: 376f8e0b68dcfecbede5d8de29c69f06c18d1b40daea73ee6e0a6183ecf2976c
- evidence_id: septin-emdb-1712-api
  kind: validation
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-1712
  locator: Actual HTTP/content diagnostic only
  summary: Successful duplicate native EMDB response retained for access provenance;
    biological conclusions use the fully read released XML header.
  accessed_at: '2026-11-04T13:22:10.834213Z'
  support: context_only
  snapshot_sha256: bb2619268c284b966f7ad24d1f437356c0faa0340078fbb880ba3bb2e777c64d
- evidence_id: septin-dent-publisher
  kind: validation
  reference: https://doi.org/10.1182/blood.V88.4.1423.bloodjournal8841423
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 403; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:22:10.401517Z'
  support: context_only
  snapshot_sha256: 4c1c5d9a91251c1c493c08b0b6d8603bfbd5e426bc62b0b3c54f6f7d5a9e2b87
- evidence_id: septin-dewulf-s3list
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC289150
  locator: Actual HTTP/content diagnostic only
  summary: Bounded exact S3 package-prefix listing, directory metadata only; no scientific
    body or absence of the paper is inferred.
  accessed_at: '2026-11-04T13:23:06.505897Z'
  support: context_only
  snapshot_sha256: 4fca1d56501cb4ac961fd76edcc48ac2a149a3824baa7b8cee48b0d65d26ab20
- evidence_id: septin-biggins-s3list
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC3730914
  locator: Actual HTTP/content diagnostic only
  summary: Bounded exact S3 package-prefix listing, directory metadata only; no scientific
    body or absence of the paper is inferred.
  accessed_at: '2026-11-04T13:23:06.515375Z'
  support: context_only
  snapshot_sha256: 8d51246bf7bdb7c28fc812d6b1ece54440164e16662fb6fa28e05953c2657b3c
- evidence_id: septin-zong-s3list
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC306587
  locator: Actual HTTP/content diagnostic only
  summary: Bounded exact S3 package-prefix listing, directory metadata only; no scientific
    body or absence of the paper is inferred.
  accessed_at: '2026-11-04T13:23:06.494428Z'
  support: context_only
  snapshot_sha256: 93d5171ef9881be0ef8bb2958189dad412bb1e975d7b5856f71b33580e034463
- evidence_id: septin-lee-s3list
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC3039362
  locator: Actual HTTP/content diagnostic only
  summary: Bounded exact S3 package-prefix listing, directory metadata only; no scientific
    body or absence of the paper is inferred.
  accessed_at: '2026-11-04T13:23:06.500498Z'
  support: context_only
  snapshot_sha256: 003e7831607efddc7cb4b28fd89820e1146a15004acd538a6bba1f51dadc5f9a
- evidence_id: septin-dewulf-corrected-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC289150/fullTextXML
  locator: Actual HTTP/content diagnostic only
  summary: Actual route status 500; failed/unusable body or family request retained
    as access context only. Successful alternative is separately evidenced.
  accessed_at: '2026-11-04T13:23:21.977449Z'
  support: context_only
  snapshot_sha256: ac9c02cf7d4ba94971881115aa7ce9be206d96b1f45593309d26272d22c0d647
- evidence_id: septin-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete twenty organism rows and dataset keys; exact biological target/comparison-host
    scope
  summary: No Saccharomyces/S288C/W303/YKO200, Homo, Mus/J558, Kluyveromyces or Chaetomium
    biological host appears. E. coli expression and bacterial structural-template
    context are not proxies. Host-matched downstream genes/modules are not applicable;
    catalogue noncoverage does not imply biological absence.
  accessed_at: '2026-11-04T13:18:08.811643Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: 'database: Official iModulonDB; query: GET /api/organisms; complete
    returned catalogue matched to all named biological target/source hosts; date:
    2026-11-04T13:18:08.811643Z; limit: All20rows; no cross-species substitute, no
    unmatched downstream query'
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical runner attempt Nov3 00:49:00.848907Z–00:49:00.863225Z
  summary: PermissionError reading pyvenv.cfg, exit1. No fresh runner invocation.
    Current official-source fallback is separate.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-septin/original-checks.json
  locator: Actual three validate/render pairs and all39 original input occurrences
  summary: All three original native validations/renderings exit0 and exact Markdown
    matches. All39 historical input occurrences match exact Git objects; current kinetochore
    and mAAA targets changed and are substantively reassessed here.
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 8dc557338e42aa21c2e6de2208d4878176e56d156987f38018e69c1ee9d05ef3
- evidence_id: septin-maaa-independent-challenge
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/adversary-microtubule/maaa-count-source-challenge.json
  locator: Separate independent narrow frozen-record/CPX/EMDB source-count challenge
  summary: 'Corroborates only the bounded minor attribution/scope correction: CPX
    unspecified; EMDB preparation3:3; no six-zinc count in either inspected source.
    No Luo/pixel assessment claimed by challenger.'
  accessed_at: '2026-11-04T13:24:38.629906Z'
  support: context_only
  snapshot_sha256: fb724bc32a9104d2a8660ed6817ce8ce4ec36ccc650a617f907903e2084d777f
- evidence_id: septin-record-kinetochore
  kind: record_content
  reference: data/structures/other/kinetochore.yaml
  locator: 'Complete current record: all fields, examples, graph, source annotations,
    discussion and history'
  summary: 'Independently read at sourcef9ac707415c382929b15517997efaa11ec96230d.
    Stale versus original frozen record: True; new content reassessed without editing
    record.'
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: ea8645dec5b13874441be4fa7a2db0b477265d3c23ecd399aa9559824428640d
- evidence_id: septin-original-kinetochore
  kind: record_content
  reference: reviews/structured/20261022T080129Z-kinetochore-audit/review.yaml
  locator: 'Entire immutable original YAML and derived Markdown: evidence scopes,
    checks, findings/actions, notes/limitations'
  summary: 'Original20261022T080129Z-kinetochore-audit: 1 inherited findings. Historical
    batch26 executions remain accurately scoped historical provenance, not current
    PR2395 checks.'
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 54c19f806698dec91e445973dc9037e2fd23c8f44685683db50a6539c5eac083
- evidence_id: septin-native-kinetochore-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-verify-receipt.json
  locator: Actual command receipt JSON (snapshot_sha256 binds this referenced receipt);
    full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-verify.log.
    Receipt stdout_sha256 and summary bind the separate log bytes.
  summary: Thirteen reviewed S288C examples; one typed Cse4 node COVERED. Native coverage
    validates representative identity but does not resolve whole-nucleosome grounding/actor
    type or prove full kinetochore formation. Exit0. ReceiptSHA 57360d96f2b6d5364827d01aceafda21a528ad28834560a54f5a91091024e9cc;
    logSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T13:17:47.579779Z'
  support: supports
  snapshot_sha256: 57360d96f2b6d5364827d01aceafda21a528ad28834560a54f5a91091024e9cc
- evidence_id: septin-native-kinetochore-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-causal-receipt.json
  locator: Actual command receipt JSON (snapshot_sha256 binds this referenced receipt);
    full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-causal.log.
    Receipt stdout_sha256 and summary bind the separate log bytes.
  summary: Thirteen reviewed S288C examples; one typed Cse4 node COVERED. Native coverage
    validates representative identity but does not resolve whole-nucleosome grounding/actor
    type or prove full kinetochore formation. Exit0. ReceiptSHA 0d49b799c6b96ed0356d80ef3d79fac875fd7eb80f4adff44d00c0484222b0c1;
    logSHA e93a54ceaf84c96a94b14c1179fd71a25c8c1b23785781886fab6aa93aa540b3.
  accessed_at: '2026-11-04T13:17:47.996155Z'
  support: supports
  snapshot_sha256: 0d49b799c6b96ed0356d80ef3d79fac875fd7eb80f4adff44d00c0484222b0c1
- evidence_id: septin-record-lysp100_associated_nuclear_domain
  kind: record_content
  reference: data/structures/other/lysp100_associated_nuclear_domain.yaml
  locator: 'Complete current record: all fields, examples, graph, source annotations,
    discussion and history'
  summary: 'Independently read at sourcef9ac707415c382929b15517997efaa11ec96230d.
    Stale versus original frozen record: False; new content reassessed without editing
    record.'
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 1ab946fc5be33e183cca56f752088cfc96ff3c898c908039b43ed4007e3b1493
- evidence_id: septin-original-lysp100_associated_nuclear_domain
  kind: record_content
  reference: reviews/structured/20261022T080132Z-lysp100-associated-nuclear-domain-audit/review.yaml
  locator: 'Entire immutable original YAML and derived Markdown: evidence scopes,
    checks, findings/actions, notes/limitations'
  summary: 'Original20261022T080132Z-lysp100-associated-nuclear-domain-audit: 0 inherited
    findings. Historical batch26 executions remain accurately scoped historical provenance,
    not current PR2395 checks.'
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 07a59eacac81ab2cefb303de28cdc2617de403a1c9ec1b35ed9136b44971dc5b
- evidence_id: septin-native-lysp100_associated_nuclear_domain-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-verify-receipt.json
  locator: Actual command receipt JSON (snapshot_sha256 binds this referenced receipt);
    full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-verify.log.
    Receipt stdout_sha256 and summary bind the separate log bytes.
  summary: One reviewed human SP140 example; one COVERED SP140 node and one UNANCHORED_WITH_UNIPROT
    external Bright/ARID3A Q99856. The external regulator is intentionally not a stable
    constituent; no missing optional inventory defect. Exit0. ReceiptSHA edc46e06cd5b7bd9743f9d544797bb7edf8b648707eb5b221047c39fb0802776;
    logSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T13:17:53.727369Z'
  support: supports
  snapshot_sha256: edc46e06cd5b7bd9743f9d544797bb7edf8b648707eb5b221047c39fb0802776
- evidence_id: septin-native-lysp100_associated_nuclear_domain-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-causal-receipt.json
  locator: Actual command receipt JSON (snapshot_sha256 binds this referenced receipt);
    full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-causal.log.
    Receipt stdout_sha256 and summary bind the separate log bytes.
  summary: One reviewed human SP140 example; one COVERED SP140 node and one UNANCHORED_WITH_UNIPROT
    external Bright/ARID3A Q99856. The external regulator is intentionally not a stable
    constituent; no missing optional inventory defect. Exit0. ReceiptSHA 874926f4a10dad6cbe7511ce3604fa5471a1d1208bd303463da78d45eb2e7b50;
    logSHA 03c648141dc26b94acdd7b083c185da463446f71a47c54aa27026991ce67e399.
  accessed_at: '2026-11-04T13:17:54.137200Z'
  support: supports
  snapshot_sha256: 874926f4a10dad6cbe7511ce3604fa5471a1d1208bd303463da78d45eb2e7b50
- evidence_id: septin-record-m_aaa_complex
  kind: record_content
  reference: data/structures/other/m_aaa_complex.yaml
  locator: 'Complete current record: all fields, examples, graph, source annotations,
    discussion and history'
  summary: 'Independently read at sourcef9ac707415c382929b15517997efaa11ec96230d.
    Stale versus original frozen record: True; new content reassessed without editing
    record.'
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 9686eb96f5b95da3c8b9dbb002841e31ac5c884c66e4af52f05706b375ea87a7
- evidence_id: septin-original-m_aaa_complex
  kind: record_content
  reference: reviews/structured/20261022T080133Z-m-aaa-complex-audit/review.yaml
  locator: 'Entire immutable original YAML and derived Markdown: evidence scopes,
    checks, findings/actions, notes/limitations'
  summary: 'Original20261022T080133Z-m-aaa-complex-audit: 0 inherited findings. Historical
    batch26 executions remain accurately scoped historical provenance, not current
    PR2395 checks.'
  accessed_at: '2026-11-04T13:32:27.919464Z'
  support: supports
  snapshot_sha256: 22517eca0c698f0befc2c2d854f086f6873d11853fcb4b62bb783b8c036adcc8
- evidence_id: septin-native-m_aaa_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-verify-receipt.json
  locator: Actual command receipt JSON (snapshot_sha256 binds this referenced receipt);
    full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-verify.log.
    Receipt stdout_sha256 and summary bind the separate log bytes.
  summary: Two reviewed S288C examples and two COVERED typed protein nodes. Native
    validation does not certify newly asserted source counts, experimental W303 identity
    or formation necessity. Exit0. ReceiptSHA 03270ace4152075782b38ee838b82f2afb83eec6431225cd9123c0e75db78172;
    logSHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T13:17:55.257387Z'
  support: supports
  snapshot_sha256: 03270ace4152075782b38ee838b82f2afb83eec6431225cd9123c0e75db78172
- evidence_id: septin-native-m_aaa_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-causal-receipt.json
  locator: Actual command receipt JSON (snapshot_sha256 binds this referenced receipt);
    full stdout independently read at /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-causal.log.
    Receipt stdout_sha256 and summary bind the separate log bytes.
  summary: Two reviewed S288C examples and two COVERED typed protein nodes. Native
    validation does not certify newly asserted source counts, experimental W303 identity
    or formation necessity. Exit0. ReceiptSHA d2bccb1480f46709ab93317cc58519183a51ed6e5781ae1d995c598818081e17;
    logSHA 03c66b2285794a12d4db1589391c5232e529f502abc044e157faada8cf19e46a.
  accessed_at: '2026-11-04T13:17:55.688387Z'
  support: supports
  snapshot_sha256: d2bccb1480f46709ab93317cc58519183a51ed6e5781ae1d995c598818081e17
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T13:23:20.438947Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 31a8fd07e26196af97f84366ec0a20b19a9b721c4a6228715823bbf401ee364d
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T13:18:05.138018Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T13:17:43.682234Z'
  support: supports
  summary: 'Native TraitMech check passed: all 10 links resolve with matching labels
    against the 1130-trait source index.'
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T13:17:39.570406Z'
  support: supports
  summary: All 22 governed artifacts match the pinned CLAW revision.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T13:18:10.191917Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    all 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T13:37:13Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 80c2d14e8451e1ef40e642efe703caed73a46e4d97198f44a663bb467b3e974c
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T13:20:35.002958Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 23c39f1de41eecdd100fe6ce2ab5ff0c839ce5883161d6535da527cd03cca1de
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2395 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-isw1_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:42.974820Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-isw1_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:43.390518Z'
  support: context_only
  snapshot_sha256: e3606d9492412eba7584d15f0b359a7e5845a9b93f368c2bdb8a4f074332af06
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-isw1a_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:44.402326Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-isw1a_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1a_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:44.811804Z'
  support: context_only
  snapshot_sha256: 850617ab05abf9be586d72f4a3ed65451ddf808e1e501e9b1ba0eb3c7ad2bbec
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-isw1b_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:45.955516Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-isw1b_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/isw1b_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:46.363151Z'
  support: context_only
  snapshot_sha256: 0c0bce6fe667636f6e9cc1ecdfdf7e8f0a431f04d7dfc7da15f0cda90ac6517d
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-kinetochore-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:47.579779Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-kinetochore-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/kinetochore-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:47.996155Z'
  support: context_only
  snapshot_sha256: e93a54ceaf84c96a94b14c1179fd71a25c8c1b23785781886fab6aa93aa540b3
  summary: 13 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ku70_ku80_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:49.087674Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ku70_ku80_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/ku70_ku80_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:49.495826Z'
  support: context_only
  snapshot_sha256: 8298d3326981375e22726968929f402596c518105adec5b93042793f0569ec3f
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-lipopolysaccharide_transport_system-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:50.665378Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-lipopolysaccharide_transport_system-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lipopolysaccharide_transport_system-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:51.081915Z'
  support: context_only
  snapshot_sha256: 22dc6e5a43f3ee651b4ba14ac6c41138867d16abc99858e2a217188e2a4a2c83
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-lolcde_lipoprotein_abc_transporter_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:52.213869Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-lolcde_lipoprotein_abc_transporter_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lolcde_lipoprotein_abc_transporter_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:52.620167Z'
  support: context_only
  snapshot_sha256: ec1f04f331b7a6dece930cf0d7b4799eb610cbbca2f0af475f09083aa4c4a241
  summary: 3 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-lysp100_associated_nuclear_domain-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:53.727369Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-lysp100_associated_nuclear_domain-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/lysp100_associated_nuclear_domain-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:54.137200Z'
  support: context_only
  snapshot_sha256: 03c648141dc26b94acdd7b083c185da463446f71a47c54aa27026991ce67e399
  summary: 1 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-m_aaa_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:55.257387Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-m_aaa_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/m_aaa_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:55.688387Z'
  support: context_only
  snapshot_sha256: 03c66b2285794a12d4db1589391c5232e529f502abc044e157faada8cf19e46a
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-macab_tolc_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:56.780972Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-macab_tolc_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2395/macab_tolc_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T13:17:57.195842Z'
  support: context_only
  snapshot_sha256: 404a309417e082e13a78e994b12da77302a38ee7f6546a78f8f98b0a9743e762
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-provenance-0
  area: schema
  topic: Frozen original/current artifacts
  outcome: supported
  summary: Complete assigned target is nonstale. Eight original validate/render commands
    pass; 61 historical input occurrences match original source revisions. Original
    artifacts are immutable and current targets equal reviewed main.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-original-audit
- assessment_id: micro-applicability-0
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal no-iModulon-specific-claim exclusion is unsupported by
    the positive constituent/chromatin-remodeling narrative. Positive molecular claims
    require assessment. The actual complete current catalogue has no Saccharomyces
    host, so no unmatched downstream proxy is used. Historical runner failure is not
    fresh.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-adapter-catalogue
  - micro-historical-runner
- assessment_id: micro-native-0
  area: schema
  topic: Actual native protein inventory
  outcome: supported
  summary: 2 maintained reviewed examples and the same number of COVERED typed nodes;
    eight total current commands across these targets exit zero. Correct accession
    joins do not independently certify generic component scope or scientific evidence.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-native-isw1_complex-verify
  - micro-native-isw1_complex-causal
  - micro-record-0
- assessment_id: micro-history-0
  area: provenance
  topic: Historical tasks and current grounding claims
  outcome: supported
  summary: Dated history/rationale remains append-only. Current source-neutral grounding
    tasks are separate from species-protein examples; no old rationale must be rewritten
    to mimic a present inventory. No whole-category closure or record edits.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-access-0
  area: evidence
  topic: Historical and current source kinds
  outcome: concern
  summary: Seven historical diagnostic access rows require kind-only correction; their
    original limits were already honest. Genuine original Vary/Koike reads are not
    denied. Fresh body/abstract/authority reads have distinct dates; metadata and
    access failures are not upgraded.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-prior-0
  - micro-historical-0-access-PMC140669-html
  - micro-historical-0-access-PMC140669-xml
  - micro-historical-0-access-PMC140669-xml-network
  - micro-historical-0-access-PMC140669-europepmc
  - micro-historical-0-access-vary2003-doi
  - micro-historical-0-access-PMC140669-bioc
  - micro-historical-0-access-panther-PTHR45623-SF49
- assessment_id: micro-provenance-1
  area: schema
  topic: Frozen original/current artifacts
  outcome: supported
  summary: Complete assigned target is nonstale. Eight original validate/render commands
    pass; 61 historical input occurrences match original source revisions. Original
    artifacts are immutable and current targets equal reviewed main.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-delta-1
  - micro-original-audit
- assessment_id: micro-applicability-1
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal no-iModulon-specific-claim exclusion is unsupported by
    the positive constituent/chromatin-remodeling narrative. Positive molecular claims
    require assessment. The actual complete current catalogue has no Saccharomyces
    host, so no unmatched downstream proxy is used. Historical runner failure is not
    fresh.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-adapter-catalogue
  - micro-historical-runner
- assessment_id: micro-native-1
  area: schema
  topic: Actual native protein inventory
  outcome: supported
  summary: 2 maintained reviewed examples and the same number of COVERED typed nodes;
    eight total current commands across these targets exit zero. Correct accession
    joins do not independently certify generic component scope or scientific evidence.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-native-isw1a_complex-verify
  - micro-native-isw1a_complex-causal
  - micro-record-1
- assessment_id: micro-history-1
  area: provenance
  topic: Historical tasks and current grounding claims
  outcome: supported
  summary: Dated history/rationale remains append-only. Current source-neutral grounding
    tasks are separate from species-protein examples; no old rationale must be rewritten
    to mimic a present inventory. No whole-category closure or record edits.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-access-1
  area: evidence
  topic: Historical and current source kinds
  outcome: concern
  summary: Seven historical diagnostic access rows require kind-only correction; their
    original limits were already honest. Genuine original Vary/Koike reads are not
    denied. Fresh body/abstract/authority reads have distinct dates; metadata and
    access failures are not upgraded.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-prior-1
  - micro-historical-1-access-PMC140669-html
  - micro-historical-1-access-PMC140669-xml
  - micro-historical-1-access-PMC140669-xml-network
  - micro-historical-1-access-PMC140669-europepmc
  - micro-historical-1-access-vary2003-doi
  - micro-historical-1-access-PMC140669-bioc
  - micro-historical-1-access-panther-PTHR45623-SF49
- assessment_id: micro-provenance-2
  area: schema
  topic: Frozen original/current artifacts
  outcome: supported
  summary: Complete assigned target is nonstale. Eight original validate/render commands
    pass; 61 historical input occurrences match original source revisions. Original
    artifacts are immutable and current targets equal reviewed main.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-delta-2
  - micro-original-audit
- assessment_id: micro-applicability-2
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal no-iModulon-specific-claim exclusion is unsupported by
    the positive constituent/chromatin-remodeling narrative. Positive molecular claims
    require assessment. The actual complete current catalogue has no Saccharomyces
    host, so no unmatched downstream proxy is used. Historical runner failure is not
    fresh.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-adapter-catalogue
  - micro-historical-runner
- assessment_id: micro-native-2
  area: schema
  topic: Actual native protein inventory
  outcome: supported
  summary: 3 maintained reviewed examples and the same number of COVERED typed nodes;
    eight total current commands across these targets exit zero. Correct accession
    joins do not independently certify generic component scope or scientific evidence.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-native-isw1b_complex-verify
  - micro-native-isw1b_complex-causal
  - micro-record-2
- assessment_id: micro-history-2
  area: provenance
  topic: Historical tasks and current grounding claims
  outcome: supported
  summary: Dated history/rationale remains append-only. Current source-neutral grounding
    tasks are separate from species-protein examples; no old rationale must be rewritten
    to mimic a present inventory. No whole-category closure or record edits.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-access-2
  area: evidence
  topic: Historical and current source kinds
  outcome: concern
  summary: Seven historical diagnostic access rows require kind-only correction; their
    original limits were already honest. Genuine original Vary/Koike reads are not
    denied. Fresh body/abstract/authority reads have distinct dates; metadata and
    access failures are not upgraded.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-prior-2
  - micro-historical-2-access-PMC140669-html
  - micro-historical-2-access-PMC140669-xml
  - micro-historical-2-access-PMC140669-xml-network
  - micro-historical-2-access-PMC140669-europepmc
  - micro-historical-2-access-vary2003-doi
  - micro-historical-2-access-PMC140669-bioc
  - micro-historical-2-access-panther-PTHR45623-SF49
- assessment_id: micro-provenance-3
  area: schema
  topic: Frozen original/current artifacts
  outcome: supported
  summary: Complete assigned target is nonstale. Eight original validate/render commands
    pass; 61 historical input occurrences match original source revisions. Original
    artifacts are immutable and current targets equal reviewed main.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-delta-3
  - micro-original-audit
- assessment_id: micro-applicability-3
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original YAML and derived Markdown contain no formal or prose iModulon/transcriptomic
    applicability assessment; this is an omission, not an expression-only exclusion.
    Positive molecular claims require assessment. The actual complete current catalogue
    has no Saccharomyces host, so no unmatched downstream proxy is used. Historical
    runner failure is not fresh.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-native-policy
  - micro-adapter-catalogue
  - micro-historical-runner
- assessment_id: micro-native-3
  area: schema
  topic: Actual native protein inventory
  outcome: supported
  summary: 2 maintained reviewed examples and the same number of COVERED typed nodes;
    eight total current commands across these targets exit zero. Correct accession
    joins do not independently certify generic component scope or scientific evidence.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-native-ku70_ku80_complex-verify
  - micro-native-ku70_ku80_complex-causal
  - micro-record-3
- assessment_id: micro-history-3
  area: provenance
  topic: Historical tasks and current grounding claims
  outcome: supported
  summary: Dated history/rationale remains append-only. Current source-neutral grounding
    tasks are separate from species-protein examples; no old rationale must be rewritten
    to mimic a present inventory. No whole-category closure or record edits.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-policy
- assessment_id: micro-access-3
  area: evidence
  topic: Historical and current source kinds
  outcome: concern
  summary: Two historical diagnostic access rows require kind-only correction; their
    original limits were already honest. Genuine original Vary/Koike reads are not
    denied. Fresh body/abstract/authority reads have distinct dates; metadata and
    access failures are not upgraded.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-prior-3
  - micro-historical-3-micro58-PMC146307-legacy
  - micro-historical-3-micro58-feldmann1996-publisher-html
- assessment_id: micro-isw1-identity
  area: identity
  topic: Generic and subtype ontology boundaries
  outcome: supported
  summary: Current active GO0016587 remains the generic Isw1 class with two exact
    is_a children GO0036436/37 under ISWI-type complex. Generic and subtype records
    may coexist; one canonical Isw1a example is not itself a faulty universal definition.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-record-1
  - micro-record-2
  - micro-go-0016587
  - micro-go-0036436
  - micro-go-0036437
  - micro-ancestors-0016587
  - micro-vary2003-html
- assessment_id: micro-isw1-component-scope
  area: identity
  topic: Broad accessory class versus specific constituent description
  outcome: concern
  summary: The generic accessory row labels Ioc3 in Isw1a and Ioc2/Ioc4 in Isw1b,
    but its role and graph-node description call the same row specific to Isw1a. Vary
    resolves distinct assemblies. Generic functional classes and a single representative
    example are allowed; a correction must target actual inconsistent scope or family
    attribution, not merely heterogeneous proteins or missing optional examples.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-record-1
  - micro-record-2
  - micro-policy
  - micro-schema
  - micro-vary2003-html
  - micro-protein-P43596
  - micro-protein-Q12072
  - micro-protein-Q04213
- assessment_id: micro-isw1-definition
  area: provenance
  topic: Expanded definition source
  outcome: concern
  summary: GO0016587 directly supports only the opening generic definition. The extra
    promoter-proximal/coding-region and cryptic-transcription clauses are not contained
    in that GO definition; Vary addresses separate complexes and biochemical/genetic
    outcomes. Native protein annotations support some later specialization but do
    not make the declared GO source support every added clause. This is a claim-specific
    provenance gap, not proof those biological clauses are false.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-go-0016587
  - micro-vary2003-html
  - micro-protein-P38144
  - micro-protein-P43596
  - micro-protein-Q12072
  - micro-protein-Q04213
- assessment_id: micro-isw1-graph
  area: graph
  topic: Membership/function graph status
  outcome: concern
  summary: Every represented edge is either a constituent is-part-of relation or whole-complex
    chromatin remodeling. MECHANISTIC status and assembly/mechanism title overstate
    the encoded detail; NONMECHANISTIC with precise scope is sufficient without forcing
    new steps or experiments.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-vary2003-html
  - micro-go-0006338
- assessment_id: micro-isw-strain-0
  area: scope
  topic: Species example and reference/assay strain
  outcome: supported
  summary: S. cerevisiae is the actual organism. Vary uses W303-derived RAD5-repaired
    strains, not S288C; current protein examples explicitly represent S288C annotations.
    COMMON is a qualitative occurrence assertion, not a newly measured clade-wide
    frequency or an exhaustive isolate census.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-vary2003-html
  - micro-tax-4932
  - micro-tax-559292
- assessment_id: micro-isw-necessity-0
  area: evidence
  topic: Physical association and activity limits
  outcome: supported
  summary: Reciprocal co-IP/TAP purification supports distinct complexes. Ioc2/Ioc4
    mutual stable association under tested extraction conditions is separate from
    global assembly necessity; activity, spacing/sliding and growth/transcription
    phenotypes are distinct assays. Current UNKNOWN classifications need not be changed.
    The Isw1b record already includes the conditional association evidence.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-vary2003-html
  - micro-tax-4932
  - micro-tax-559292
  - micro-schema
  - micro-record-2
- assessment_id: micro-isw-family-0
  area: grounding
  topic: Exact family versus verified domain candidates
  outcome: unknown
  summary: Current inspected Isw1/2 N-terminal, SNF2-like, WHIM1, PWWP and IOC2-region
    candidates are domains or broad domain superfamilies where successfully resolved.
    They do not establish exact whole Isw1/Ioc classes. REVIEWED_LABEL_ONLY remains
    boundedly justified; no exhaustive absence, forced broad-family mapping or independent
    sequence alignment is claimed. Initial three rate-limit responses are retained
    separately.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-family-IPR044754
  - micro-family-IPR038718
  - micro-family-IPR035503
  - micro-family-IPR062587
  - micro-family-IPR028942-retry
  - micro-family-IPR062429-retry
  - micro-family-IPR063422-retry
- assessment_id: micro-isw-assays-0
  area: evidence
  topic: Source-dependent remodeling results
  outcome: supported
  summary: Both purified assemblies have nucleosome-stimulated ATPase activity. Spacing/sliding
    and binding differ under recombinant nucleosome/DNA substrates, competitor, concentration
    and extraction conditions; those results do not prescribe universal in-vivo rates
    or genomic occupancy. Transcript measurements establish condition-specific expression
    effects, not a complete mechanistic pathway.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-record-0
  - micro-vary2003-html
  - micro-go-0006338
- assessment_id: micro-isw-strain-1
  area: scope
  topic: Species example and reference/assay strain
  outcome: supported
  summary: S. cerevisiae is the actual organism. Vary uses W303-derived RAD5-repaired
    strains, not S288C; current protein examples explicitly represent S288C annotations.
    COMMON is a qualitative occurrence assertion, not a newly measured clade-wide
    frequency or an exhaustive isolate census.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-vary2003-html
  - micro-tax-4932
  - micro-tax-559292
- assessment_id: micro-isw-necessity-1
  area: evidence
  topic: Physical association and activity limits
  outcome: supported
  summary: Reciprocal co-IP/TAP purification supports distinct complexes. Ioc2/Ioc4
    mutual stable association under tested extraction conditions is separate from
    global assembly necessity; activity, spacing/sliding and growth/transcription
    phenotypes are distinct assays. Current UNKNOWN classifications need not be changed.
    The Isw1b record already includes the conditional association evidence.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-vary2003-html
  - micro-tax-4932
  - micro-tax-559292
  - micro-schema
  - micro-record-2
- assessment_id: micro-isw-family-1
  area: grounding
  topic: Exact family versus verified domain candidates
  outcome: unknown
  summary: Current inspected Isw1/2 N-terminal, SNF2-like, WHIM1, PWWP and IOC2-region
    candidates are domains or broad domain superfamilies where successfully resolved.
    They do not establish exact whole Isw1/Ioc classes. REVIEWED_LABEL_ONLY remains
    boundedly justified; no exhaustive absence, forced broad-family mapping or independent
    sequence alignment is claimed. Initial three rate-limit responses are retained
    separately.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-family-IPR044754
  - micro-family-IPR038718
  - micro-family-IPR035503
  - micro-family-IPR062587
  - micro-family-IPR028942-retry
  - micro-family-IPR062429-retry
  - micro-family-IPR063422-retry
- assessment_id: micro-isw-assays-1
  area: evidence
  topic: Source-dependent remodeling results
  outcome: supported
  summary: Both purified assemblies have nucleosome-stimulated ATPase activity. Spacing/sliding
    and binding differ under recombinant nucleosome/DNA substrates, competitor, concentration
    and extraction conditions; those results do not prescribe universal in-vivo rates
    or genomic occupancy. Transcript measurements establish condition-specific expression
    effects, not a complete mechanistic pathway.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-vary2003-html
  - micro-go-0006338
- assessment_id: micro-isw-strain-2
  area: scope
  topic: Species example and reference/assay strain
  outcome: supported
  summary: S. cerevisiae is the actual organism. Vary uses W303-derived RAD5-repaired
    strains, not S288C; current protein examples explicitly represent S288C annotations.
    COMMON is a qualitative occurrence assertion, not a newly measured clade-wide
    frequency or an exhaustive isolate census.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-vary2003-html
  - micro-tax-4932
  - micro-tax-559292
- assessment_id: micro-isw-necessity-2
  area: evidence
  topic: Physical association and activity limits
  outcome: supported
  summary: Reciprocal co-IP/TAP purification supports distinct complexes. Ioc2/Ioc4
    mutual stable association under tested extraction conditions is separate from
    global assembly necessity; activity, spacing/sliding and growth/transcription
    phenotypes are distinct assays. Current UNKNOWN classifications need not be changed.
    The Isw1b record already includes the conditional association evidence.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-vary2003-html
  - micro-tax-4932
  - micro-tax-559292
  - micro-schema
- assessment_id: micro-isw-family-2
  area: grounding
  topic: Exact family versus verified domain candidates
  outcome: unknown
  summary: Current inspected Isw1/2 N-terminal, SNF2-like, WHIM1, PWWP and IOC2-region
    candidates are domains or broad domain superfamilies where successfully resolved.
    They do not establish exact whole Isw1/Ioc classes. REVIEWED_LABEL_ONLY remains
    boundedly justified; no exhaustive absence, forced broad-family mapping or independent
    sequence alignment is claimed. Initial three rate-limit responses are retained
    separately.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-family-IPR044754
  - micro-family-IPR038718
  - micro-family-IPR035503
  - micro-family-IPR062587
  - micro-family-IPR028942-retry
  - micro-family-IPR062429-retry
  - micro-family-IPR063422-retry
- assessment_id: micro-isw-assays-2
  area: evidence
  topic: Source-dependent remodeling results
  outcome: supported
  summary: Both purified assemblies have nucleosome-stimulated ATPase activity. Spacing/sliding
    and binding differ under recombinant nucleosome/DNA substrates, competitor, concentration
    and extraction conditions; those results do not prescribe universal in-vivo rates
    or genomic occupancy. Transcript measurements establish condition-specific expression
    effects, not a complete mechanistic pathway.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-vary2003-html
  - micro-go-0006338
- assessment_id: micro-subtype-identity-1
  area: identity
  topic: Exact stable subtype and constituent identities
  outcome: supported
  summary: Isw1a is the supported Isw1-Ioc3 assembly. Active exact GO and primary
    purification agree. The broader Isw1 parent is is_a; neither subtype is silently
    replaced by a four-protein superassembly.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-go-0036436
  - micro-ancestors-0036436
  - micro-vary2003-html
- assessment_id: micro-subtype-graph-1
  area: graph
  topic: Complete bounded composition/function graph
  outcome: supported
  summary: All constituent membership and broad remodeling edges agree with actual
    source. NONMECHANISTIC status and explicit limits correctly avoid claiming ATP
    hydrolysis, nucleosome-recognition or a temporal sliding/assembly mechanism not
    represented by the graph.
  target_ids:
  - GO:0036436
  evidence_ids:
  - micro-record-1
  - micro-vary2003-html
  - micro-graph-policy
  - micro-go-0006338
- assessment_id: micro-subtype-identity-2
  area: identity
  topic: Exact stable subtype and constituent identities
  outcome: supported
  summary: Isw1b is the supported Isw1-Ioc2-Ioc4 assembly. Active exact GO and primary
    purification agree. The broader Isw1 parent is is_a; neither subtype is silently
    replaced by a four-protein superassembly.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-go-0036437
  - micro-ancestors-0036437
  - micro-vary2003-html
- assessment_id: micro-subtype-graph-2
  area: graph
  topic: Complete bounded composition/function graph
  outcome: supported
  summary: All constituent membership and broad remodeling edges agree with actual
    source. NONMECHANISTIC status and explicit limits correctly avoid claiming ATP
    hydrolysis, nucleosome-recognition or a temporal sliding/assembly mechanism not
    represented by the graph.
  target_ids:
  - GO:0036437
  evidence_ids:
  - micro-record-2
  - micro-vary2003-html
  - micro-graph-policy
  - micro-go-0006338
- assessment_id: micro-ku-identity
  area: identity
  topic: Ku heterodimer and parent boundary
  outcome: supported
  summary: Active GO0043564 denotes the two-class Ku70:Ku80 heterodimer, with exact
    nuclear-complex parent. It is not identity-equivalent to DNA-PK or prokaryotic
    Ku homodimers. Generic GO/review V(D)J and DNA-PK wording is not asserted as a
    yeast graph function.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-go-0043564
  - micro-ancestors-0043564
  - micro-go-0140513
  - micro-koike2002-pdf
- assessment_id: micro-ku-families
  area: grounding
  topic: Two resolvable whole-subunit classes
  outcome: concern
  summary: Current exact IPR006165 Ku70 and IPR024193 Ku80 family identities and native
    P32807/Q04437 cross-references resolve the existing deferred task. Shared IPR006164
    is only a DNA-binding domain. This is positive class evidence, not an optional
    accession or a requirement that families be complex-exclusive.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-policy
  - micro-family-IPR006165
  - micro-family-IPR024193
  - micro-family-IPR006164
  - micro-protein-P32807
  - micro-protein-Q04437
- assessment_id: micro-ku-functions
  area: evidence
  topic: Yeast binding/repair and mammalian context
  outcome: supported
  summary: Complete primary abstracts for Feldmann and Boulton support the bounded
    yeast heterodimer/end-binding, repair and telomere observations. Koike is explicitly
    secondary and separates mammalian DNA-PK/V(D)J context; Downs remains metadata
    only. No unread primary body or cross-species formation experiment is asserted.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-pmid-8910371
  - micro-pmid-8890183
  - micro-pmid-8972848
  - micro-boulton70-html
  - micro-boulton80-html
  - micro-koike2002-pdf
  - micro-pmid-15122350
  - micro-downs2004-doi
- assessment_id: micro-ku-necessity
  area: scope
  topic: Global UNKNOWN and experimental limits
  outcome: supported
  summary: Binding loss, repair defects and mammalian subunit stabilization are not
    automatically yeast assembly necessity. Preserve permissive UNKNOWN values and
    the two-subunit defining boundary; no isolated-formation experiment is mandated.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-schema
  - micro-koike2002-pdf
  - micro-pmid-8910371
  - micro-pmid-8890183
  - micro-pmid-8972848
- assessment_id: micro-ku-graph
  area: graph
  topic: Complete NONMECHANISTIC membership/output graph
  outcome: supported
  summary: The two constituent membership relations and broad DNA-end-binding/NHEJ
    outputs are scoped to composition and function. No detailed synapsis, DNA-PK recruitment
    or ligation sequence is invented; GO exact process labels and primary abstract
    scopes support the coarse representation.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-graph-policy
  - micro-go-0045027
  - micro-go-0006303
  - micro-pmid-8910371
  - micro-pmid-8890183
  - micro-pmid-8972848
- assessment_id: micro-ku-taxa
  area: scope
  topic: Yeast occurrence and reference localization
  outcome: supported
  summary: Species4932 canonical context and two reviewed S288C reference examples
    are distinct. Current UniProt cites Laroche1998 for nuclear/telomere location;
    exact complete abstract is read, not the primary microscopy body. COMMON is not
    an experimentally measured prevalence statistic across isolates.
  target_ids:
  - GO:0043564
  evidence_ids:
  - micro-record-3
  - micro-tax-4932
  - micro-tax-559292
  - micro-protein-P32807
  - micro-protein-Q04437
  - micro-pmid-9635192
- assessment_id: micro-reference-localization
  area: evidence
  topic: Verified citation identities and annotation scopes
  outcome: supported
  summary: Huh and Laroche exact author/title/PMID identities and complete indexed
    abstracts match native citation provenance. Current proteins independently provide
    nuclear annotations. No Huh or Laroche body/pixel assay is certified, and location
    alone is not used as proof of physical membership.
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0043564
  evidence_ids:
  - micro-protein-P38144
  - micro-protein-P43596
  - micro-protein-Q12072
  - micro-protein-Q04213
  - micro-protein-P32807
  - micro-protein-Q04437
  - micro-pmid-14562095
  - micro-pmid-9635192
- assessment_id: micro-isw1-old-verdict
  area: provenance
  topic: Narrow inherited severity and action scope
  outcome: concern
  summary: Original F1 major severity and separate-classes framing overstate the independently
    confirmed residual. The generic definition already distinguishes two assemblies;
    generic functional classes and representative examples are allowed. Retain exact
    predecessor/key as a minor internal wording/scope finding, with a bounded correction
    that permits the generic class and requires no row/type/example expansion.
  target_ids:
  - GO:0016587
  evidence_ids:
  - micro-prior-0
  - micro-record-0
  - micro-policy
  - micro-vary2003-html
  - micro-isw1-peer-challenge
- assessment_id: plaque-t5-schema
  area: schema
  topic: Current native contract and immutable historical proof
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Current complete record and original review schema/history were checked.
    Native original validate/render pass and original frozen hashes match. Current
    source bytes are unchanged for LPS/MacAB; LolCDE is substantively refreshed separately.
  evidence_ids:
  - plaque-t5-record
  - plaque-native-schema
  - plaque-original-proof
  - plaque-t5-original
- assessment_id: plaque-t5-identity-protein
  area: grounding
  topic: Current native example identity and diagnostic limits
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Seven reviewed K-12 examples and seven covered typed nodes; actual gene
    names and current accessions agree. This does not settle exact class grounding
    or paper-level membership.
  evidence_ids:
  - plaque-t5-record
  - plaque-native-lipopolysaccharide_transport_system-verify
  - plaque-native-lipopolysaccharide_transport_system-causal
  - plaque-protein-P0ADV1
  - plaque-protein-P0A9V1
  - plaque-protein-P0ADV9
  - plaque-protein-P31554
  - plaque-protein-P0ADC1
  - plaque-protein-P0AF98
  - plaque-protein-P0ADC6
- assessment_id: plaque-t5-applicability
  area: completeness
  topic: Required whole-record structured-source cross-check
  outcome: concern
  target_ids:
  - GO:0062051
  summary: Original YAML has no formal or prose iModulon applicability assessment.
    Positive seven-protein transport and gene/pathway assertions trigger assessment.
    Exact full YAML was searched recursively, including notes/checks/evidence; this
    is an omission, not an explicit N/A.
  evidence_ids:
  - plaque-t5-record
  - plaque-t5-original
  - plaque-native-policy
  - plaque-adapter-catalogue
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
- assessment_id: plaque-t5-adapter-scope
  area: scope
  topic: Exact matched dataset and downstream computational context
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Full fresh catalogue and precise1k metadata distinguish five strains from
    reference locus511145 and from actual assay constructs. Exact15-gene join and
    complete201-module memberships were followed by module22/45/167 metadata/member
    tables. lptA/B/C,tolC→22; lpp→45; lptF→167; other9 zero true flags. No expression
    correlation or threshold absence is treated as physical assembly, transport, necessity
    or biological absence.
  evidence_ids:
  - plaque-t5-record
  - plaque-adapter-joined-scope
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
  - plaque-adapter-module-22
  - plaque-adapter-module-22-genes
  - plaque-adapter-module-45
  - plaque-adapter-module-45-genes
  - plaque-adapter-module-167
  - plaque-adapter-module-167-genes
- assessment_id: plaque-t5-historical-kind
  area: provenance
  topic: Original source access and evidence-kind audit
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Own original evidence kinds and access locators were inspected; no access-only
    or secondary-as-primary defect was established for these three bundles. Fresh
    failed routes are validation/context_only; metadata is database/context_only;
    primary abstracts/captions retain limited tiers. Original source timestamps remain
    historical. No new successful runner invocation is claimed.
  evidence_ids:
  - plaque-t5-record
  - plaque-original-proof
  - plaque-t5-original
  - plaque-native-policy
- assessment_id: plaque-t5-images
  area: evidence
  topic: Image and source-access limits
  outcome: not_applicable
  target_ids:
  - GO:0062051
  summary: No maintained local image is present in the inspected cohort. Source text
    captions may inform bounded experiments, but no figure pixels, raw maps or supplementary
    data were inspected and no image audit is certified.
  evidence_ids:
  - plaque-t5-record
  - plaque-native-schema
- assessment_id: plaque-t5-history
  area: provenance
  topic: Historical rationale and record-curation boundary
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Original reviews and historical rationale remain immutable. Findings/actions
    address current fields with dated append-only discussion updates if needed. No
    neighbor, category or previous closed issue is resolved by inference. Root owns
    issues and all repository mutations.
  evidence_ids:
  - plaque-t5-record
  - plaque-native-policy
  - plaque-t5-original
- assessment_id: plaque-t6-schema
  area: schema
  topic: Current native contract and immutable historical proof
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Current complete record and original review schema/history were checked.
    Native original validate/render pass and original frozen hashes match. Current
    source bytes are unchanged for LPS/MacAB; LolCDE is substantively refreshed separately.
  evidence_ids:
  - plaque-t6-record
  - plaque-native-schema
  - plaque-original-proof
  - plaque-t6-original
- assessment_id: plaque-t6-identity-protein
  area: grounding
  topic: Current native example identity and diagnostic limits
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Three reviewed K-12 examples and three covered constituent nodes; the fourth
    typed node is the nonconstituent Lpp/Pal substrate and is accurately UNANCHORED_WITH_UNIPROT.
    It need not become a transporter component.
  evidence_ids:
  - plaque-t6-record
  - plaque-native-lolcde_lipoprotein_abc_transporter_complex-verify
  - plaque-native-lolcde_lipoprotein_abc_transporter_complex-causal
  - plaque-protein-P0ADC3
  - plaque-protein-P75957
  - plaque-protein-P75958
  - plaque-protein-P69776
  - plaque-protein-P0A912
- assessment_id: plaque-t6-applicability
  area: completeness
  topic: Required whole-record structured-source cross-check
  outcome: concern
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Original checks[4] explicitly says no expression-module inference is used.
    That does not exempt the named LolC/D/E proteins, transport pathway and Lpp/Pal
    substrate assertions. All are checked in matched E. coli context.
  evidence_ids:
  - plaque-t6-record
  - plaque-t6-original
  - plaque-native-policy
  - plaque-adapter-catalogue
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
- assessment_id: plaque-t6-adapter-scope
  area: scope
  topic: Exact matched dataset and downstream computational context
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Full fresh catalogue and precise1k metadata distinguish five strains from
    reference locus511145 and from actual assay constructs. Exact15-gene join and
    complete201-module memberships were followed by module22/45/167 metadata/member
    tables. lptA/B/C,tolC→22; lpp→45; lptF→167; other9 zero true flags. No expression
    correlation or threshold absence is treated as physical assembly, transport, necessity
    or biological absence.
  evidence_ids:
  - plaque-t6-record
  - plaque-adapter-joined-scope
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
  - plaque-adapter-module-22
  - plaque-adapter-module-22-genes
  - plaque-adapter-module-45
  - plaque-adapter-module-45-genes
  - plaque-adapter-module-167
  - plaque-adapter-module-167-genes
- assessment_id: plaque-t6-historical-kind
  area: provenance
  topic: Original source access and evidence-kind audit
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Own original evidence kinds and access locators were inspected; no access-only
    or secondary-as-primary defect was established for these three bundles. Fresh
    failed routes are validation/context_only; metadata is database/context_only;
    primary abstracts/captions retain limited tiers. Original source timestamps remain
    historical. No new successful runner invocation is claimed.
  evidence_ids:
  - plaque-t6-record
  - plaque-original-proof
  - plaque-t6-original
  - plaque-native-policy
- assessment_id: plaque-t6-images
  area: evidence
  topic: Image and source-access limits
  outcome: not_applicable
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: No maintained local image is present in the inspected cohort. Source text
    captions may inform bounded experiments, but no figure pixels, raw maps or supplementary
    data were inspected and no image audit is certified.
  evidence_ids:
  - plaque-t6-record
  - plaque-native-schema
- assessment_id: plaque-t6-history
  area: provenance
  topic: Historical rationale and record-curation boundary
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Original reviews and historical rationale remain immutable. Findings/actions
    address current fields with dated append-only discussion updates if needed. No
    neighbor, category or previous closed issue is resolved by inference. Root owns
    issues and all repository mutations.
  evidence_ids:
  - plaque-t6-record
  - plaque-native-policy
  - plaque-t6-original
- assessment_id: plaque-t9-schema
  area: schema
  topic: Current native contract and immutable historical proof
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Current complete record and original review schema/history were checked.
    Native original validate/render pass and original frozen hashes match. Current
    source bytes are unchanged for LPS/MacAB; LolCDE is substantively refreshed separately.
  evidence_ids:
  - plaque-t9-record
  - plaque-native-schema
  - plaque-original-proof
  - plaque-t9-original
- assessment_id: plaque-t9-identity-protein
  area: grounding
  topic: Current native example identity and diagnostic limits
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Three reviewed K-12 examples and three covered typed nodes. Current exact
    MacA, MacB and TolC family names and example mappings agree; generated MacB family
    prose is excluded.
  evidence_ids:
  - plaque-t9-record
  - plaque-native-macab_tolc_complex-verify
  - plaque-native-macab_tolc_complex-causal
  - plaque-protein-P75830
  - plaque-protein-P75831
  - plaque-protein-P02930
- assessment_id: plaque-t9-applicability
  area: completeness
  topic: Required whole-record structured-source cross-check
  outcome: concern
  target_ids:
  - GO:1990196
  summary: Original checks[4] explicitly says no expression-module inference is used.
    Positive MacA/MacB/TolC efflux and pathway assertions require actual matched source
    coverage assessment.
  evidence_ids:
  - plaque-t9-record
  - plaque-t9-original
  - plaque-native-policy
  - plaque-adapter-catalogue
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
- assessment_id: plaque-t9-adapter-scope
  area: scope
  topic: Exact matched dataset and downstream computational context
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Full fresh catalogue and precise1k metadata distinguish five strains from
    reference locus511145 and from actual assay constructs. Exact15-gene join and
    complete201-module memberships were followed by module22/45/167 metadata/member
    tables. lptA/B/C,tolC→22; lpp→45; lptF→167; other9 zero true flags. No expression
    correlation or threshold absence is treated as physical assembly, transport, necessity
    or biological absence.
  evidence_ids:
  - plaque-t9-record
  - plaque-adapter-joined-scope
  - plaque-adapter-precise1k-meta
  - plaque-adapter-precise1k-genes
  - plaque-adapter-module-22
  - plaque-adapter-module-22-genes
  - plaque-adapter-module-45
  - plaque-adapter-module-45-genes
  - plaque-adapter-module-167
  - plaque-adapter-module-167-genes
- assessment_id: plaque-t9-historical-kind
  area: provenance
  topic: Original source access and evidence-kind audit
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Own original evidence kinds and access locators were inspected; no access-only
    or secondary-as-primary defect was established for these three bundles. Fresh
    failed routes are validation/context_only; metadata is database/context_only;
    primary abstracts/captions retain limited tiers. Original source timestamps remain
    historical. No new successful runner invocation is claimed.
  evidence_ids:
  - plaque-t9-record
  - plaque-original-proof
  - plaque-t9-original
  - plaque-native-policy
- assessment_id: plaque-t9-images
  area: evidence
  topic: Image and source-access limits
  outcome: not_applicable
  target_ids:
  - GO:1990196
  summary: No maintained local image is present in the inspected cohort. Source text
    captions may inform bounded experiments, but no figure pixels, raw maps or supplementary
    data were inspected and no image audit is certified.
  evidence_ids:
  - plaque-t9-record
  - plaque-native-schema
- assessment_id: plaque-t9-history
  area: provenance
  topic: Historical rationale and record-curation boundary
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Original reviews and historical rationale remain immutable. Findings/actions
    address current fields with dated append-only discussion updates if needed. No
    neighbor, category or previous closed issue is resolved by inference. Root owns
    issues and all repository mutations.
  evidence_ids:
  - plaque-t9-record
  - plaque-native-policy
  - plaque-t9-original
- assessment_id: plaque-t5-identity
  area: identity
  topic: Seven-member transenvelope Lpt identity
  outcome: supported
  target_ids:
  - GO:0062051
  summary: GO0062051 and direct GO1990351 parent retain the seven Lpt classes. MsbA
    flips LPS upstream and is not an eighth constituent. Biological scope is E. coli
    and source-qualified diderm transport, not uniform essentiality across all bacteria.
  evidence_ids:
  - plaque-t5-record
  - plaque-go-0062051
  - plaque-go-1990351
  - plaque-tax-2
  - plaque-tax-562
  - plaque-PMC5858563-jats
  - plaque-PMC2880507-jats
- assessment_id: plaque-t5-families
  area: grounding
  topic: Seven exact families versus current label-only notes
  outcome: concern
  target_ids:
  - GO:0062051
  summary: Current exact family types/signatures and independently mapped reviewed
    examples support LptA IPR014340, LptB IPR030921, LptC IPR026265, LptD IPR020889,
    LptE IPR007485, LptF IPR030922, LptG IPR030923. Retain species exceptions and
    distinguish F/G. Older five-member background is not current composition evidence.
  evidence_ids:
  - plaque-t5-record
  - plaque-native-policy
  - plaque-family-IPR014340
  - plaque-family-IPR030921
  - plaque-family-IPR026265
  - plaque-family-IPR020889
  - plaque-family-IPR007485
  - plaque-family-IPR030922
  - plaque-family-IPR030923
- assessment_id: plaque-t5-graph
  area: graph
  topic: ATP-driven extraction and bridge source scope
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Sherman reconstitution supports all-seven transport and association; Okuda
    distinguishes ATP-dependent LPS extraction/transfer from ATP-independent LptA/C
    contact; Chng2010 copurification supports transenvelope association. The coarse
    graph does not resolve physiological LptA count or imply every function-loss phenotype
    is failure to assemble.
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC5858563-jats
  - plaque-PMC3552488-jats
  - plaque-PMC2880507-jats
  - plaque-pmid-19500581
  - plaque-pmid-22668317
- assessment_id: plaque-t5-plug
  area: provenance
  topic: 2010 proposal versus 2011 contact-mapping support
  outcome: concern
  target_ids:
  - GO:0062051
  summary: The retained edge6 evidence1 says Chng2010 demonstrated plug/barrel architecture.
    Its Discussion is conditional; Freinkman2011 supplies later contact mapping supporting
    buried plug topology. Correct the evidential-stage attribution while retaining
    valid LptD/E partnership, and do not describe 2011 as an atomic structure.
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC2851745-legacy
  - plaque-PMC3038725-legacy
- assessment_id: plaque-t5-experiments
  area: scope
  topic: Localization, function and necessity distinctions
  outcome: supported
  target_ids:
  - GO:0062051
  summary: Native abstracts support LptA periplasm, LptC periplasmic domain/LPS binding
    and ordered transfer, LptF/G inner membrane and LptD/E outer membrane. Depletion/viability
    and altered membrane fractions are not automatically direct formation tests; no
    universal necessity or optional formation experiment is imposed.
  evidence_ids:
  - plaque-t5-record
  - plaque-pmid-17056748
  - plaque-pmid-18424520
  - plaque-pmid-20720015
  - plaque-pmid-18375759
  - plaque-pmid-16861298
  - plaque-pmid-18480051
- assessment_id: plaque-t6-identity
  area: identity
  topic: Specific LolCDE release complex
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Local identity is narrower than GO0043190 ABC-transporter parent. CPX4262/7MDY
    give LolC1:LolD2:LolE1; GO0140306 release contributes to GO0044874 outer-membrane
    localization. LolA/B handoff is pathway context, not extra LolCDE constituents.
  evidence_ids:
  - plaque-t6-record
  - plaque-go-0043190
  - plaque-go-0140306
  - plaque-go-0044874
  - plaque-cpx-4262
  - plaque-pdb-7MDY-assembly1
  - plaque-PMC8333309-jats
- assessment_id: plaque-t6-families
  area: grounding
  topic: Exact LolC/D/E family mappings
  outcome: concern
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Current exact native families and independent example xrefs support LolC
    NCBIfamNF008076, LolD InterProIPR011924 and LolE NCBIfamNF008357. Broad LolC/E
    IPR011925 and LolD-like IPR015854 are near misses, not substitutes. Historical
    search rationale remains historical.
  evidence_ids:
  - plaque-t6-record
  - plaque-family-NF008076
  - plaque-family-IPR011924
  - plaque-family-NF008357
  - plaque-family-IPR011925
  - plaque-family-IPR015854
  - plaque-protein-P0ADC3
  - plaque-protein-P75957
  - plaque-protein-P75958
- assessment_id: plaque-t6-stale-substrate
  area: scope
  topic: Substantive refresh of added Lpp/Pal substrate scope
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Fresh Yakushi abstract and public captions1,3,4,7 support ATP/LolA-dependent
    Pal proteoliposome release, Lpp release in DLP79-22 spheroplast assays and Asp+2
    sorting. Current K-12 reference xrefs identify Lpp/Pal but are distinct from exact
    assay strains. No inaccessible full-body or figure-pixel inspection is claimed.
  evidence_ids:
  - plaque-t6-record
  - plaque-lolcde-stale-delta
  - plaque-pmid-10783239
  - plaque-yakushi2000-figure1
  - plaque-yakushi2000-figure3
  - plaque-yakushi2000-figure4
  - plaque-yakushi2000-figure7
  - plaque-protein-P69776
  - plaque-protein-P0A912
- assessment_id: plaque-t6-stale-membership
  area: graph
  topic: Added membership and release-localization edges
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: New descriptions call LolC/D/E essential stoichiometric constituents, while
    evidence notes accurately state CPX explicit1:2:1 counts and PDB assembled heterotetramer.
    CPX physical-interaction evidence has LolD enzyme and LolC/E unspecified bioRole;
    it is not a deletion-essentiality annotation. Unlike explicit false CPX essentiality
    attributions, these notes support defining membership. Retain contributes-to and
    bounded release-localization; do not infer universal assembly indispensability
    or demand a depletion assay.
  evidence_ids:
  - plaque-t6-record
  - plaque-lolcde-stale-delta
  - plaque-cpx-4262
  - plaque-pdb-7MDY-assembly1
  - plaque-PMC8333309-jats
  - plaque-native-policy
- assessment_id: plaque-t6-mechanism
  area: scope
  topic: Structural state and assay limits
  outcome: supported
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  summary: Sharma2021 K-12 genes expressed in BL21(DE3), His-LolD purification and
    nucleotide cryo-EM support the heterotetramer/state model. Basal ATPase, Lpp K58-deletion
    copurification and density interpreted as lipoprotein do not independently prove
    every substrate sequence or direct transport kinetics. Coarse NONMECHANISTIC graph
    preserves this limit.
  evidence_ids:
  - plaque-t6-record
  - plaque-PMC8333309-jats
  - plaque-pdb-7MDY
  - plaque-pmid-10783239
- assessment_id: plaque-t9-identity
  area: identity
  topic: MacAB-TolC ordered core and current families
  outcome: supported
  target_ids:
  - GO:1990196
  summary: GO1990196/GO1990195 identity and ordered PDB5NIK model support MacB2:MacA6:TolC3.
    Exact MacA IPR058623, MacB IPR050250 and TolC IPR058622 match the separate current
    reviewed examples. The engineered fusion/disulfide stabilization and expression
    host are retained limits.
  evidence_ids:
  - plaque-t9-record
  - plaque-go-1990196
  - plaque-go-1990195
  - plaque-pdb-5NIK-assembly1
  - plaque-family-IPR058623
  - plaque-family-IPR050250
  - plaque-family-IPR058622
  - plaque-PMC5447821-jats
- assessment_id: plaque-t9-substrate
  area: scope
  topic: Macrolide-subclass preference versus broader cargo
  outcome: concern
  target_ids:
  - GO:1990196
  summary: Current definition faithfully quotes current GO, yet its unqualified specific-to14/15-membered-macrolides
    sentence overrestricts total cargo. Kobayashi2001 abstract gives the tested resistance
    profile; independent Yamanaka2008 primary abstract documents BL21(DE3) STII secretion/rescue
    and Turlin2014 abstract documents E. coli PPIX efflux under stated perturbations.
    Fitzpatrick2017 introduction cites broader reports rather than assaying every
    listed cargo. Preserve that distinction.
  evidence_ids:
  - plaque-t9-record
  - plaque-go-1990196
  - plaque-pmid-11544226
  - plaque-pmid-18805970
  - plaque-pmid-25257218
  - plaque-PMC5447821-jats
- assessment_id: plaque-t9-attribution
  area: provenance
  topic: Correct Lin2009 bibliographic attribution
  outcome: concern
  target_ids:
  - GO:1990196
  summary: The exact PMID18955484 title/authors/DOI and genuine primary body identify
    Lin et al. 2009. Two current notes name Tikhonova et al. 2009 despite correct
    PMID and supported assays; correct those names without changing biological conclusions.
  evidence_ids:
  - plaque-t9-record
  - plaque-pmid-18955484
  - plaque-PMC2613632-jats
- assessment_id: plaque-t9-function
  area: graph
  topic: Assembly, ATPase and translocation evidence
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Lin2009 detergent pulldowns, MacB dimer biophysics and ATPase/erythromycin
    assays support interactions and functional coupling in stated conditions; 2017
    structure supports periplasmic portal/gating interpretation. These do not certify
    universal subunit-deletion formation necessity or all ATP-cycle steps; UNKNOWN
    remains acceptable.
  evidence_ids:
  - plaque-t9-record
  - plaque-PMC2613632-jats
  - plaque-PMC5447821-jats
  - plaque-native-policy
  - plaque-go-0008559
- assessment_id: plaque-t9-taxon
  area: scope
  topic: Native reference versus assay hosts
  outcome: supported
  target_ids:
  - GO:1990196
  summary: Reviewed examples and native assembly entities map to K-12 references.
    W3110 source genes/C43(DE3) ΔacrAB expression, KAM3(DE3) transport assays and
    BL21(DE3) STII experiments remain distinct; the multi-strain precise1k data are
    only bounded computational context.
  evidence_ids:
  - plaque-t9-record
  - plaque-tax-83333
  - plaque-tax-562
  - plaque-PMC2613632-jats
  - plaque-PMC5447821-jats
  - plaque-pmid-18805970
  - plaque-adapter-precise1k-meta
- assessment_id: septin-kinetochore-schema-inputs
  area: schema
  topic: Original native schema/render and historical inputs
  outcome: supported
  summary: Three originals validate/render exactly and39 historical input occurrences
    match. Current target changed; exact old/current delta is scientifically reassessed,
    not accepted by hash alone. Schema/provenance checks are not scientific proof.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-original-kinetochore
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-kinetochore-native-coverage
  area: consistency
  topic: Actual protein inventories and coverage
  outcome: supported
  summary: Thirteen reviewed S288C examples; one typed Cse4 node COVERED. Native coverage
    validates representative identity but does not resolve whole-nucleosome grounding/actor
    type or prove full kinetochore formation.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-native-kinetochore-verify
  - septin-native-kinetochore-causal
  - septin-protein-policy
- assessment_id: septin-kinetochore-history
  area: provenance
  topic: Dated reasoning and current clarifications
  outcome: supported
  summary: Dated history and search/access rationale remain provenance. Current source
    availability does not retroactively invalidate earlier failures; any curation
    updates current fields or appends clarification without rewriting dated history.
    No other-record/group disposition is inferred.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-original-kinetochore
  - septin-curation-policy
- assessment_id: septin-kinetochore-structured-sources
  area: evidence
  topic: Positive molecular claims and actual host coverage
  outcome: supported
  summary: Whole record asserts CSE4/COMA/MIND/Ndc80 chromosome-attachment pathways.
    Actual coverage assessment is required. Fresh complete official catalogue has
    no matching biological host, so downstream dataset queries are not applicable
    and primary/authority fallback is retained. Absence of expression inference alone
    is not the reason.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-original-kinetochore
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-kinetochore-old-source-kinds
  area: provenance
  topic: Historical source kinds and access boundaries
  outcome: supported
  summary: No separate access-only evidence row mislabeled as a scientific source
    was identified in this assigned original. Failed routes are explicitly scoped
    limitations next to genuine alternative bodies/abstracts; genuine Lee Methods
    access is not reclassified as failed merely because another route failed.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-original-kinetochore
  - septin-literature-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-schema-inputs
  area: schema
  topic: Original native schema/render and historical inputs
  outcome: supported
  summary: Three originals validate/render exactly and39 historical input occurrences
    match. Current target equals its historical frozen input. Schema/provenance checks
    are not scientific proof.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-original-lysp100_associated_nuclear_domain
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-lysp100_associated_nuclear_domain-native-coverage
  area: consistency
  topic: Actual protein inventories and coverage
  outcome: supported
  summary: One reviewed human SP140 example; one COVERED SP140 node and one UNANCHORED_WITH_UNIPROT
    external Bright/ARID3A Q99856. The external regulator is intentionally not a stable
    constituent; no missing optional inventory defect.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-native-lysp100_associated_nuclear_domain-verify
  - septin-native-lysp100_associated_nuclear_domain-causal
  - septin-protein-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-history
  area: provenance
  topic: Dated reasoning and current clarifications
  outcome: supported
  summary: Dated history and search/access rationale remain provenance. Current source
    availability does not retroactively invalidate earlier failures; any curation
    updates current fields or appends clarification without rewriting dated history.
    No other-record/group disposition is inferred.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-original-lysp100_associated_nuclear_domain
  - septin-curation-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-structured-sources
  area: evidence
  topic: Positive molecular claims and actual host coverage
  outcome: supported
  summary: Whole record asserts SP140/Bright regulation and enhancer transcription.
    Actual coverage assessment is required. Fresh complete official catalogue has
    no matching biological host, so downstream dataset queries are not applicable
    and primary/authority fallback is retained. Absence of expression inference alone
    is not the reason.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-original-lysp100_associated_nuclear_domain
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-lysp100_associated_nuclear_domain-old-source-kinds
  area: provenance
  topic: Historical source kinds and access boundaries
  outcome: supported
  summary: No separate access-only evidence row mislabeled as a scientific source
    was identified in this assigned original. Failed routes are explicitly scoped
    limitations next to genuine alternative bodies/abstracts; genuine Lee Methods
    access is not reclassified as failed merely because another route failed.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-original-lysp100_associated_nuclear_domain
  - septin-literature-policy
- assessment_id: septin-m_aaa_complex-schema-inputs
  area: schema
  topic: Original native schema/render and historical inputs
  outcome: supported
  summary: Three originals validate/render exactly and39 historical input occurrences
    match. Current target changed; exact old/current delta is scientifically reassessed,
    not accepted by hash alone. Schema/provenance checks are not scientific proof.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-original-m_aaa_complex
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-m_aaa_complex-native-coverage
  area: consistency
  topic: Actual protein inventories and coverage
  outcome: supported
  summary: Two reviewed S288C examples and two COVERED typed protein nodes. Native
    validation does not certify newly asserted source counts, experimental W303 identity
    or formation necessity.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-native-m_aaa_complex-verify
  - septin-native-m_aaa_complex-causal
  - septin-protein-policy
- assessment_id: septin-m_aaa_complex-history
  area: provenance
  topic: Dated reasoning and current clarifications
  outcome: supported
  summary: Dated history and search/access rationale remain provenance. Current source
    availability does not retroactively invalidate earlier failures; any curation
    updates current fields or appends clarification without rewriting dated history.
    No other-record/group disposition is inferred.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-original-m_aaa_complex
  - septin-curation-policy
- assessment_id: septin-m_aaa_complex-structured-sources
  area: evidence
  topic: Positive molecular claims and actual host coverage
  outcome: supported
  summary: Whole record asserts Yta10/Yta12/PHB protein processing and ATP-dependent
    proteolysis. Actual coverage assessment is required. Fresh complete official catalogue
    has no matching biological host, so downstream dataset queries are not applicable
    and primary/authority fallback is retained. Absence of expression inference alone
    is not the reason.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-original-m_aaa_complex
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-m_aaa_complex-old-source-kinds
  area: provenance
  topic: Historical source kinds and access boundaries
  outcome: supported
  summary: No separate access-only evidence row mislabeled as a scientific source
    was identified in this assigned original. Failed routes are explicitly scoped
    limitations next to genuine alternative bodies/abstracts; genuine Lee Methods
    access is not reclassified as failed merely because another route failed.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-original-m_aaa_complex
  - septin-literature-policy
- assessment_id: septin-kinetochore-identity
  area: identity
  topic: Whole kinetochore and constituent boundaries
  outcome: supported
  summary: GO0000776 is exact; COMA GO0000817, MIND GO0000444 and Ndc80 GO0031262
    are specific subcomplexes. Selective early inventory is explicit; no unsupported
    complete yeast inventory or centromeric DNA-as-component inference.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-go
  - septin-dewulf-ncbi
  - septin-westermann-xml
- assessment_id: septin-kinetochore-stale-refresh
  area: identity
  topic: New CSE4 representative and retained platform identity
  outcome: concern
  summary: 'New reviewed P36012/CSE4/CSL2/YKL049C S288C example matches native authority
    and a current exact one-result query. Its PMID14581449 nuclear-centromere annotation
    is independently supported by Cse4-containing material in Westermann. This correct
    representative does not resolve F1: the maintained component/graph actor still
    denotes the whole CENP-A nucleosome, whose exact current class is GO0043505.'
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-up-P36012
  - septin-query-CSE4-559292
  - septin-go-cenpa
  - septin-westermann-xml
  - septin-protein-policy
- assessment_id: septin-kinetochore-subunit-identities
  area: identity
  topic: Twelve preexisting complex references
  outcome: supported
  summary: The twelve COMA/MIND/Ndc80 examples retain reviewed S288C identities, exact
    primary genes and current one-result queries. Native protein examples are source-strain
    references, not proof every cited experiment used S288C.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-tax-559292
  - septin-up-Q02732
  - septin-up-P53298
  - septin-up-Q06675
  - septin-up-P38313
  - septin-up-P39731
  - septin-up-P40568
  - septin-up-Q12143
  - septin-up-P47149
  - septin-up-P40460
  - septin-up-P33895
  - septin-up-Q04477
  - septin-up-P40014
- assessment_id: septin-kinetochore-primary-membership
  area: evidence
  topic: Purification, localization and source-specific strains
  outcome: supported
  summary: De Wulf W303-congenic hydrodynamic/co-purification and Westermann tagged300mMKCl
    material support the selected yeast core. Schmitzberger2017 abstract specifically
    studies recombinant Kluyveromyces lactis COMA; it is not S288C primary experimental
    evidence. Ancillary native localization citations remain abstract-tier and do
    not replace direct body evidence.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-dewulf-ncbi
  - septin-westermann-xml
  - septin-pmid-29046335-abstract
  - septin-pmid-11179222-abstract
  - septin-pmid-14657030-abstract
- assessment_id: septin-kinetochore-formation
  area: completeness
  topic: Conditional dependencies versus complete formation
  outcome: unknown
  summary: Conditional mutations change protein abundance, stability, CEN occupancy
    and segregation; those endpoints do not uniformly abolish the entire kinetochore.
    De Wulf retains residual COMA subcomplexes; Biggins explicitly treats minimal
    assembly requirements and Cse4 stoichiometry as unresolved. UNKNOWN is reasonable;
    no universal necessity mandate.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-dewulf-ncbi
  - septin-westermann-xml
  - septin-biggins-ncbi
  - septin-schema-policy
- assessment_id: septin-kinetochore-graph
  area: graph
  topic: Coarse assembly hierarchy and class grounding
  outcome: concern
  summary: NONMECHANISTIC assembly scope honestly describes a coarse inner/outer map.
    COMA bridge/MIND recruitment/Ndc80 outer role are supported, without importing
    every omitted subcomplex. F1 aligns the complete Cse4 nucleosome actor to its
    exact structural class; it is not a generic objection to all protein-complex actor
    types.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-go
  - septin-go-cenpa
  - septin-westermann-xml
  - septin-biggins-ncbi
  - septin-graph-policy
- assessment_id: septin-kinetochore-distribution
  area: scope
  topic: Taxon and prevalence limits
  outcome: supported
  summary: Saccharomyces is a supported canonical model; COMMON is qualitative scope,
    not a measured prevalence census. Human homology and Kluyveromyces structural
    comparisons do not change the maintained yeast assembly scope.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-tax-4932
  - septin-tax-559292
  - septin-dewulf-ncbi
  - septin-pmid-29046335-abstract
- assessment_id: septin-kinetochore-images
  area: scope
  topic: No claimed target image inspection
  outcome: supported
  summary: No maintained image is present. Genuine bodies and embedded captions were
    read; no Westermann/De Wulf/Biggins figure pixels, supplements or raw biochemical
    measurements were analyzed.
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-literature-policy
  - septin-westermann-xml
  - septin-dewulf-ncbi
  - septin-biggins-ncbi
- assessment_id: septin-lysp100_associated_nuclear_domain-identity
  area: identity
  topic: Exact nuclear domain and physical boundary
  outcome: supported
  summary: GO0016606/its LANDs synonym and nuclear-body parent are exact. Morphological
    globular/electron-dense distinction from annular PML bodies is supported at GO
    and Dent complete-abstract scope. Nuclear-lumen parthood is biological localization,
    not falsely claimed as direct current ontology edge.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-go
  - septin-go-0016606-ancestors
  - septin-pmid-8695863-abstract
- assessment_id: septin-lysp100_associated_nuclear_domain-representatives
  area: identity
  topic: SP140 isoform and external Bright reference
  outcome: supported
  summary: Q13342 is reviewed human SP140 with LYSP100 alias; displayed isoform LYSp100-B
    and alternative forms are distinguished. Q99856 is reviewed human ARID3A/Bright,
    an external cross-reference. It does not identify the species of every construct
    in the J558/HeLa study; the record does not make it a stable constituent.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-up-Q13342
  - septin-up-Q99856
  - septin-query-SP140-9606
  - septin-zong-ncbi
  - septin-protein-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-family-boundary
  area: grounding
  topic: Broad family/domain candidates remain nonexact
  outcome: supported
  summary: IPR043563/PTHR46386 span SP110/SP140/SP140L and other reviewed members;
    IPR030411 is a bromodomain, not whole LYSp100B. These current native classifications
    do not justify forcing the exact retained component into a broader family/domain.
    No exhaustive absence claim or optional-example mandate.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-ipr-IPR043563
  - septin-ipr-IPR030411
  - septin-panther-retry-SP140
  - septin-panther-retry-SP140-members
- assessment_id: septin-lysp100_associated_nuclear_domain-localization
  area: scope
  topic: Human identity and variable localization
  outcome: supported
  summary: Dent complete abstract supports human lymphoid protein and HeLa expression/localization.
    Zong directly studies ectopic nuclear dots, partial overlap and Bright-driven
    redistribution in HeLa and J558; this does not establish all endogenous isoforms
    or all human lineages. VARIABLE does not purport to be a population census.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-pmid-8695863-abstract
  - septin-zong-ncbi
  - septin-tax-9606
- assessment_id: septin-lysp100_associated_nuclear_domain-function
  area: evidence
  topic: Reporter coactivation and interaction limits
  outcome: supported
  summary: Zong shows stronger Bright-dependent E-mu CAT output in J558 reporter cells;
    HeLa/Jurkat do not share that coactivation. In-vitro LYSp100B–Bright interaction
    is supported, whereas in-vivo co-IP was not detected. Existing broad modulation
    and redistribution descriptions remain bounded; no direct endogenous chromatin-remodeling
    mechanism is asserted.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-zong-ncbi
- assessment_id: septin-lysp100_associated_nuclear_domain-formation
  area: completeness
  topic: Unknown formation-specific requirement
  outcome: unknown
  summary: Defining enrichment, transfection redistribution and reporter activity
    do not establish that SP140 or Bright is universally required to form all LANDs.
    Existing UNKNOWN and discussion boundaries are appropriate; no required new experiment.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-zong-ncbi
  - septin-pmid-8695863-abstract
  - septin-schema-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-graph
  area: graph
  topic: Nonmechanistic regulatory observations
  outcome: supported
  summary: NONMECHANISTIC regulation graph distinguishes SP140-enriched LANDs, PML
    bodies and external Bright; redistribution and reporter modulation are observed
    endpoints, not a resolved direct causal chain from nuclear-body disruption to
    enhancer activity. PML/SP100/Bright are not silently promoted to stable constituents.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-zong-ncbi
  - septin-go
  - septin-graph-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-access
  area: scope
  topic: Main text versus abstract and visual limits
  outcome: supported
  summary: Zong genuine full-body sections/captions were read after failed/challenged
    routes. Dent/Bloch/Gong are complete-abstract only; Gong supplies native nuclear-annotation
    context, not LAND membership evidence. No target image, source figure pixels or
    supplements inspected.
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-zong-ncbi
  - septin-pmid-8695863-abstract
  - septin-pmid-8910577-abstract
  - septin-pmid-25593309-abstract
  - septin-dent-publisher
- assessment_id: septin-m_aaa_complex-identity
  area: identity
  topic: Exact complex, ancestry and matrix-facing protease
  outcome: supported
  summary: GO0005745 and parents GO0098800/GO1905368 remain exact; membrane parthood
    is correctly inherited through the inner-membrane complex class. CPX retains real
    Yta10/Yta12 and zinc membership; no universal PHB- or substrate-containing assembly
    is inferred.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-go
  - septin-go-0005745-ancestors
  - septin-cpx-1654
  - septin-lee-ncbi
- assessment_id: septin-m_aaa_complex-representatives
  area: identity
  topic: Native aliases, reference strain and exact families
  outcome: supported
  summary: P39925 primaryAFG3 aliasYTA10 and P40341 primaryYTA12 aliasRCA1 are reviewed
    S288C references with current one-result queries. IPR050928/005936 are broader
    shared families and IPR011546 is a domain. Unchecked machine-generated IPR050928
    prose is excluded; no narrow paralog family is invented.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-up-P39925
  - septin-up-P40341
  - septin-query-AFG3-559292
  - septin-query-YTA12-559292
  - septin-ipr-IPR050928
  - septin-ipr-IPR005936
  - septin-ipr-retry-IPR011546
  - septin-tax-559292
- assessment_id: septin-m_aaa_complex-source-strains
  area: scope
  topic: Reference, preparation and assay organisms
  outcome: supported
  summary: CPX numeric559292 is S288C despite generic species label; released EMD1712
    uses species4932 preparation metadata; Lee uses YKO200-derived variants; Luo uses
    W303-1B endogenous replacements. These contexts remain distinct; human/Ct PHB
    experiments do not become yeast atomistic evidence.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-cpx-1654
  - septin-emdb-1712-wwpdb
  - septin-lee-ncbi
  - septin-luo-xml
  - septin-tax-4932
  - septin-tax-559292
- assessment_id: septin-m_aaa_complex-stale-count-refresh
  area: evidence
  topic: New constituent edges and source-count attribution
  outcome: concern
  summary: All three added actors/relation types have real membership/cofactor support.
    However CPX participant counts are null, not3:3 or6zinc as the new edge notes
    state. EMD1712/Lee support a scoped3:3 preparation/model, not an unqualified universal
    structure; six zinc is not supplied by either inspected count source. One new
    minor finding corrects attribution/scope without rejecting heteromer or cofactor
    biology.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-cpx-1654
  - septin-emdb-1712-wwpdb
  - septin-lee-ncbi
  - septin-chebi-29105
  - septin-maaa-independent-challenge
- assessment_id: septin-m_aaa_complex-structural-dataset
  area: scope
  topic: EMDB preparation and map resolution
  outcome: supported
  summary: EMD1712 supersedes1543; cross-linked detergent/ATP/C6 preparation and12angstrom
    header match. Lee specifically reports ATPase Trap mutants and inability to distinguish
    homologous subunits at this resolution; alternation is assigned using prior biochemistry.
    Sample0.5MDa versusCPX1000kDa is not forced into one physiological mass.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-emdb-1712-wwpdb
  - septin-lee-ncbi
  - septin-cpx-1654
- assessment_id: septin-m_aaa_complex-reporter-function
  area: evidence
  topic: Reporter maturation versus flux
  outcome: supported
  summary: Luo Fig4 distinguishes precursor/total C-terminal Strep MrpL32 after14hYPG30C
    in four biological replicates. PHB1/SIM perturbations lower precursor fraction
    and IMSD replacement raises it. These data do not measure endogenous untagged
    flux or ribosome incorporation; current descriptions expressly retain those limits.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-luo-xml
  - septin-luo-fig4
- assessment_id: septin-m_aaa_complex-growth
  area: evidence
  topic: Respiratory peroxide response
  outcome: supported
  summary: Figure4c/d serial dilution assays at30C distinguish48hYPD and72hYPG with/without2mMH2O2.
    PHB1 re-expression partially rescues; SIM/IMSD states differ from whole-protein
    deletion. Separate growth endpoint does not establish processing causes stress
    sensitivity.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-luo-xml
  - septin-luo-fig4
- assessment_id: septin-m_aaa_complex-formation
  area: completeness
  topic: Co-assembly versus perturbation phenotype
  outcome: unknown
  summary: Membership and preparation architecture support real assembly; current
    domain-replacement processing phenotypes do not directly establish abolished oligomer
    formation. Lee engineered homo-oligomer rescue and wild-type heteromer behavior
    are source-specific. No universal essentiality or new depletion experiment is
    requested.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-lee-ncbi
  - septin-luo-xml
  - septin-schema-policy
- assessment_id: septin-m_aaa_complex-graph
  area: graph
  topic: Bounded intervention-response graph
  outcome: supported
  summary: MECHANISTIC REGULATION is appropriate for the existing experiment-bounded
    interventions and assayed responses. It neither draws a processing-to-stress edge
    nor claims a resolved atomic yeast PHB interface. Newly inserted count/source
    statements are separately flagged, while contribution/cofactor relations remain.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-luo-xml
  - septin-luo-fig4
  - septin-graph-policy
  - septin-cpx-1654
- assessment_id: septin-m_aaa_complex-image-rights
  area: scope
  topic: Actual Fig4 pixels and link-only attribution
  outcome: supported
  summary: External native Fig4 panelsA–D were visually inspected and match the biochemical/growth
    caption. MD5 and CC BY-NC-ND4.0 authors/license match current record; OTHER correctly
    retains exact license URL. No maintained local image file or hosted derivative
    is introduced.
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-luo-fig4
  - septin-luo-xml
  - septin-literature-policy
- assessment_id: septin-kinetochore-verdict
  area: consistency
  topic: Independent current disposition
  outcome: concern
  summary: 'Needs curation: 1 minor finding; inherited exact grounding gap remains
    after valid CSE4 refresh. Review-bundle applicability/staleness corrections are
    separate from record curation.'
  target_ids:
  - GO:0000776
  evidence_ids:
  - septin-record-kinetochore
  - septin-original-kinetochore
  - septin-review-policy
  - septin-go-cenpa
  - septin-westermann-xml
  - septin-biggins-ncbi
  - septin-up-P36012
  - septin-curation-policy
  - septin-graph-policy
- assessment_id: septin-lysp100_associated_nuclear_domain-verdict
  area: consistency
  topic: Independent current disposition
  outcome: supported
  summary: 'Pass with limitations: no supported new record finding; source conditions,
    reference identity and unknown formation limits are retained. Review-bundle applicability/staleness
    corrections are separate from record curation.'
  target_ids:
  - GO:0016606
  evidence_ids:
  - septin-record-lysp100_associated_nuclear_domain
  - septin-original-lysp100_associated_nuclear_domain
  - septin-review-policy
- assessment_id: septin-m_aaa_complex-verdict
  area: consistency
  topic: Independent current disposition
  outcome: concern
  summary: 'Needs curation: 1 minor finding; new source-count mismatch in stale-edge
    refresh, without invented predecessor. Review-bundle applicability/staleness corrections
    are separate from record curation.'
  target_ids:
  - GO:0005745
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-original-m_aaa_complex
  - septin-review-policy
  - septin-cpx-1654
  - septin-emdb-1712-wwpdb
  - septin-lee-ncbi
  - septin-maaa-independent-challenge
  - septin-curation-policy
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 3 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0016587
  - GO:0036436
  - GO:0036437
  - GO:0000776
  - GO:0043564
  - GO:0062051
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  - GO:0016606
  - GO:0005745
  - GO:1990196
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
  issue_key: isw1-generic-subtype-component-conflation
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Align the Isw1 accessory class and variant wording
  description: The generic definition already distinguishes Isw1a and Isw1b, and a
    broad functional accessory class is permitted. However, components[1] and its
    graph node label include Ioc3 in Isw1a and Ioc2/Ioc4 in Isw1b while the same row
    role/grounding notes and node description categorically call it Isw1a-specific.
    Clarify this internal class/variant scope. Nonhomology, PROTEIN type or a single
    Ioc3 example alone do not establish an identity error or require additional examples.
  target_ids:
  - GO:0016587
  field_paths:
  - components[1].label
  - components[1].role
  - components[1].grounding_notes
  - causal_graphs[0].nodes[2].label
  - causal_graphs[0].nodes[2].description
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-schema
  - micro-vary2003-html
  - micro-protein-P43596
  - micro-protein-Q12072
  - micro-protein-Q04213
  - micro-isw1-peer-challenge
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
  rule_id: Exact class boundary, source attribution and graph scope
  native_severity: major
  normalization_reason: 'The original major is narrowed to a minor wording/scope inconsistency:
    generic identity and both variant boundaries are already stated. Native family-or-class
    guidance permits a generic accessory class; the required correction need not split
    rows, change component type or expand optional examples.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080127Z-isw1-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3030
- finding_id: micro-F2
  issue_key: isw1-expanded-definition-source
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source the added definition claims
  description: The expanded definition attributes promoter-proximal Isw1a, coding-region
    Isw1b and cryptic-transcription suppression to definition_source GO0016587, whose
    actual definition states only an Isw1-containing chromatin-modifying complex.
    The record does not provide claim-specific support for all added scope and functions.
  target_ids:
  - GO:0016587
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-go-0016587
  - micro-vary2003-html
  - micro-protein-P38144
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
  rule_id: Exact class boundary, source attribution and graph scope
  native_severity: minor
  normalization_reason: Concrete maintained claim or identity mismatch within the
    stated scope, not an empty optional field.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080127Z-isw1-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3031
- finding_id: micro-F3
  issue_key: isw1-membership-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Align the graph status with its represented evidence
  description: The MECHANISTIC status and mechanism title describe a graph consisting
    of constituent membership and one broad chromatin-remodeling edge. These claims
    establish composition and function but do not themselves encode a mechanism.
  target_ids:
  - GO:0016587
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].title
  - causal_graphs[0].description
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-graph-policy
  - micro-vary2003-html
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
  rule_id: Exact class boundary, source attribution and graph scope
  native_severity: minor
  normalization_reason: Concrete maintained claim or identity mismatch within the
    stated scope, not an empty optional field.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080127Z-isw1-complex-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3032
- finding_id: micro-F4
  issue_key: ku70-ku80-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the two Ku subunit classes
  description: Ku70/Yku70 and Ku80/Yku80 remain REVIEWED_LABEL_ONLY despite exact
    whole-family identities IPR006165 and IPR024193. Native family types/signatures
    and separately verified yeast protein cross-references corroborate both mappings.
  target_ids:
  - GO:0043564
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding_status
  - components[1].grounding_notes
  evidence_ids:
  - micro-record-3
  - micro-prior-3
  - micro-policy
  - micro-family-IPR006165
  - micro-family-IPR024193
  - micro-family-IPR006164
  - micro-protein-P32807
  - micro-protein-Q04437
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ku70_ku80_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: One grouped minor grounding gap with correct membership, accessions
    and biological roles already present. Neither a generic domain nor an organism-specific
    gene identifier is substituted for the class.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080129Z-ku70-ku80-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3033
- finding_id: plaque-t5-F1
  issue_key: lpt-seven-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the seven named Lpt protein classes
  description: 'All seven named subunits remain REVIEWED_LABEL_ONLY despite exact
    current families: LptA IPR014340, LptB IPR030921, LptC IPR026265, LptD IPR020889,
    LptE IPR007485, LptF IPR030922 and LptG IPR030923. Family types/signatures and
    separate native protein cross-references support these class mappings.'
  target_ids:
  - GO:0062051
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - components[4].grounding_status
  - components[5].grounding_status
  - components[6].grounding_status
  - components[0].grounding_notes
  - components[1].grounding_notes
  - components[2].grounding_notes
  - components[3].grounding_notes
  - components[4].grounding_notes
  - components[5].grounding_notes
  - components[6].grounding_notes
  evidence_ids:
  - plaque-t5-record
  - plaque-native-policy
  - plaque-family-IPR014340
  - plaque-family-IPR030921
  - plaque-family-IPR026265
  - plaque-family-IPR020889
  - plaque-family-IPR007485
  - plaque-family-IPR030922
  - plaque-family-IPR030923
  - plaque-protein-P0ADV1
  - plaque-protein-P0A9V1
  - plaque-protein-P0ADV9
  - plaque-protein-P31554
  - plaque-protein-P0ADC1
  - plaque-protein-P0AF98
  - plaque-protein-P0ADC6
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lipopolysaccharide_transport_system.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: Grouped minor class-grounding gap; the correct seven-member
    inventory and reference accessions already exist. Older background prose or generated
    alternative entries are not used to infer current mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080130Z-lipopolysaccharide-transport-system-audit
    finding_id: F1
  disposition_reason: Independently reconfirmed against current record and freshly
    inspected native/primary sources; remains open for separately authorized record
    curation.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3037
- finding_id: plaque-t5-F2
  issue_key: lpt-chng2010-plug-barrel-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Separate the 2010 plug model from later demonstration
  description: The evidence note on the LptE-to-LptD edge says Chng2010 DOI10.1073/pnas.0912872107
    demonstrated the plug-and-barrel architecture. That paper characterizes LptD/E
    and explicitly discusses alternative arrangements conditionally. Freinkman2011
    PMID21257904 supplies the later contact-mapping support.
  target_ids:
  - GO:0062051
  field_paths:
  - causal_graphs[0].edges[6].evidence[1].notes
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC2851745-legacy
  - plaque-PMC3038725-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lipopolysaccharide_transport_system.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: Localized source-stage overstatement; the LptD/E partnership
    and plug-and-barrel biology are independently supported, so the mechanism itself
    is not rejected.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080130Z-lipopolysaccharide-transport-system-audit
    finding_id: F2
  disposition_reason: Independently reconfirmed against current record and freshly
    inspected native/primary sources; remains open for separately authorized record
    curation.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3038
- finding_id: plaque-t6-F1
  issue_key: lolcde-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the three exact LolCDE subunit families
  description: All three protein rows remain REVIEWED_LABEL_ONLY while native full-family
    identities and independent example membership now resolve their retained classes.
    Exact mappings are LolC NCBIfam:NF008076, LolD InterPro:IPR011924 and LolE NCBIfam:NF008357;
    the new supported graph edges do not repair this current grounding gap. Preserve
    dated discussion rationale.
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  field_paths:
  - components[0].grounding_status
  - components[1].grounding_status
  - components[2].grounding_status
  - components[0].grounding_notes
  - components[1].grounding_notes
  - components[2].grounding_notes
  evidence_ids:
  - plaque-t6-record
  - plaque-native-policy
  - plaque-family-NF008076
  - plaque-family-IPR011924
  - plaque-family-NF008357
  - plaque-protein-P0ADC3
  - plaque-protein-P75957
  - plaque-protein-P75958
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit
    finding_id: F1
  disposition_reason: Independently reconfirmed against current record and freshly
    inspected native/primary sources; remains open for separately authorized record
    curation.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3039
- finding_id: plaque-t9-F1
  issue_key: macab-substrate-specificity-qualification
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the macrolide-specificity sentence
  description: The definition says transport activity is specific to14/15-membered
    macrolides, while its cited structural source and retained broader function cover
    other cargo. The sentence is faithfully inherited from current GO, but that provenance
    does not remove its overexclusive reading. Fresh independent primary abstracts
    for E. coli STII secretion and PPIX efflux corroborate broader cargo, with assay/strain
    limits; the structural paper introduction is not itself a direct assay of every
    cargo.
  target_ids:
  - GO:1990196
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - plaque-t9-record
  - plaque-go-1990196
  - plaque-PMC5447821-jats
  - plaque-pmid-11544226
  - plaque-pmid-18805970
  - plaque-pmid-25257218
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/macab_tolc_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080133Z-macab-tolc-complex-audit
    finding_id: F1
  disposition_reason: Independently reconfirmed against current record and freshly
    inspected native/primary sources; remains open for separately authorized record
    curation.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3040
- finding_id: plaque-t9-F2
  issue_key: macab-lin2009-author-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the2009paper author attribution
  description: Two evidence notes call PMID18955484 Tikhonova etal2009. The exact
    native identity and full primary body identify LinHT etal2009; the DOI and biological
    conclusions remain correct.
  target_ids:
  - GO:1990196
  field_paths:
  - functions
  - causal_graphs#macab_tolc_efflux_function.edges
  evidence_ids:
  - plaque-t9-record
  - plaque-pmid-18955484
  - plaque-PMC2613632-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/macab_tolc_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported complex identity
    and principal biological function.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080133Z-macab-tolc-complex-audit
    finding_id: F2
  disposition_reason: Independently reconfirmed against current record and freshly
    inspected native/primary sources; remains open for separately authorized record
    curation.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3041
- finding_id: septin-kinetochore-F1
  issue_key: kinetochore-cenpa-nucleosome-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the named CENP-A nucleosome class
  description: The centromeric Cse4/CENP-A nucleosome platform remains REVIEWED_LABEL_ONLY
    despite active exact GO0043505, CENP-A containing nucleosome. Its native definition
    and primary Cse4/H3 replacement context match the named class. The linked graph
    node labels and references this complete nucleosome platform, so its current GENE_OR_PROTEIN
    typing should be aligned to the structural class in the same correction. The newly
    added correct CSE4 representative does not change the complete nucleosome actor/class.
    Preserve dated rationale; update current class grounding with no inferred fixed
    nucleosome stoichiometry.
  target_ids:
  - GO:0000776
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - causal_graphs[0].nodes[0].node_type
  - causal_graphs[0].nodes[0].grounding
  evidence_ids:
  - septin-record-kinetochore
  - septin-original-kinetochore
  - septin-go-cenpa
  - septin-westermann-xml
  - septin-biggins-ncbi
  - septin-up-P36012
  - septin-curation-policy
  - septin-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/kinetochore.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: Localized current class-grounding gap; correct platform biology,
    OTHER typing and source-supported roles remain intact. This does not claim that
    the earlier curation search was false.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T080129Z-kinetochore-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3034
- finding_id: septin-m_aaa_complex-F1
  issue_key: m-aaa-stoichiometry-source-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct m-AAA graph count attribution and preparation scope
  description: The three new constituent edges attribute3xYta10,3xYta12 and6xZn to
    CPX-1654. The complete current CPX response leaves all participant stochiometry
    fields null. EMD1712 explicitly records3+3 proteins for its cross-linked detergent
    preparation; Lee describes roughly equimolar Trap-mutant material and a C6 model
    unable to distinguish paralogs. Neither inspected CPX response nor EMDB header
    supplies six zinc ions. Thus the edge source notes and unqualified count wording
    overstate these sources and conflict with retained scoped component/dataset notes.
    This does not refute heteromer formation, zinc membership, or a possible independently
    supported six-ion model.
  target_ids:
  - GO:0005745
  field_paths:
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0].notes
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].notes
  - causal_graphs[0].edges[2].description
  - causal_graphs[0].edges[2].evidence[0].notes
  evidence_ids:
  - septin-record-m_aaa_complex
  - septin-original-m_aaa_complex
  - septin-cpx-1654
  - septin-emdb-1712-wwpdb
  - septin-lee-ncbi
  - septin-maaa-independent-challenge
  - septin-curation-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/m_aaa_complex.yaml
    role: maintained scientific record
  rule_id: Source-specific quantitative attribution and preparation scope
  native_severity: minor
  normalization_reason: Localized source-count correction. Supported biological membership/cofactor
    and preparation-specific3:3 remain intact; no claim of biological impossibility
    or universal alternative stoichiometry.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3035
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0016587
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, align the accessory component
    and graph-node label with their stated variant scope. An explicitly generic functional
    accessory class with qualified Isw1a/Isw1b roles and evidence is valid; alternatively
    narrow the row to its represented variant while preserving the generic structure
    identity.
  acceptance_checks:
  - The same component and graph node do not simultaneously include Isw1b constituents
    in their label and categorically describe their whole scope as Isw1a-specific.
  - Keep the already stated Isw1a/Isw1b distinction and valid representative examples.
    No mandatory row split, component-type change, extra example inventory or all-Ioc
    single-complex assertion is required.
  - Do not treat a generic functional class as an assertion that all Ioc proteins
    form a homologous family.
  - Preserve dated history and rationale; use current clarification or appended scope.
  - Retain permissible UNKNOWN formation values and avoid new experimental demands.
  - Run applicable native checks after separately authorized curation; no record edit
    occurs in this review PR.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0016587
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, keep the GO-backed definition
    bounded, or support the added scientific clauses with directly checked sources
    and explicit scope.
  acceptance_checks:
  - Distinguish support for subtype composition from promoter/coding-region localization
    and cryptic-transcription suppression.
  - Do not label those biological claims false merely because the declared GO definition
    does not establish them.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated history and discussions.rationale; put current clarifications in
    current notes or appended scope.
  - Retain valid existing examples and permissible UNKNOWN values; do not mandate
    optional examples or new experiments.
  - No maintained record is edited in this review PR.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0016587
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/isw1_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, declare the present graph
    nonmechanistic with precise scope notes, or separately curate source-supported
    causal steps.
  acceptance_checks:
  - Do not turn a membership relation into an assembly or activity dependency without
    assay evidence.
  - Preserve the source-supported broad chromatin-remodeling function.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve dated history and discussions.rationale; put current clarifications in
    current notes or appended scope.
  - Retain valid existing examples and permissible UNKNOWN values; do not mandate
    optional examples or new experiments.
  - No maintained record is edited in this review PR.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0043564
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ku70_ku80_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground Ku70 to IPR006165
    and Ku80 to IPR024193, retaining yeast roles, examples and UNKNOWN assembly necessity.
  acceptance_checks:
  - Each mapping identifies the correct whole subunit family.
  - Shared Ku domain IPR006164 is not used as an exact whole-subunit identity.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated history and discussions.rationale; put current clarifications in
    current notes or appended scope.
  - Retain valid existing examples and permissible UNKNOWN values; do not mandate
    optional examples or new experiments.
  - No maintained record is edited in this review PR.
- action_id: plaque-t5-A1
  finding_ids:
  - plaque-t5-F1
  target_ids:
  - GO:0062051
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lipopolysaccharide_transport_system.yaml
    role: maintained scientific record
  description: Ground the seven named subunit classes to the exact verified families,
    retaining role evidence and species exceptions. Keep LptF and LptG distinct.
  acceptance_checks:
  - Each family matches the named whole protein class and its reviewed example.
  - No broad ABC, shared LptF/G or isolated domain is substituted; historical search
    claims remain historical.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve append-only historical rationale; any current clarification is dated
    and source-scoped. No universal formation necessity or new experiment is required
    by this action.
- action_id: plaque-t5-A2
  finding_ids:
  - plaque-t5-F2
  target_ids:
  - GO:0062051
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lipopolysaccharide_transport_system.yaml
    role: maintained scientific record
  description: Change the2010 note to its demonstrated biochemical characterization/proposed
    arrangement, and cite the later directly relevant2011 study for the architecture
    claim.
  acceptance_checks:
  - Each citation is attached to the claim and epistemic stage actually supported.
  - The valid LptD/E insertion relationship is retained without claiming the2010 paper
    solved the later architecture.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve append-only historical rationale; any current clarification is dated
    and source-scoped. No universal formation necessity or new experiment is required
    by this action.
- action_id: plaque-t6-A1
  finding_ids:
  - plaque-t6-F1
  target_ids:
  - cellstructuremech:lolcde_lipoprotein_abc_transporter_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/lolcde_lipoprotein_abc_transporter_complex.yaml
    role: maintained scientific record
  description: Map LolC to NCBIfam:NF008076, LolD to InterPro:IPR011924 and LolE to
    NCBIfam:NF008357; retain correct examples,1:2:1 architecture and source-specific
    scope.
  acceptance_checks:
  - Do not substitute the broader LolC/E or LolD-like classes for these exact subunit
    families.
  - Preserve supported source-specific claims and pass applicable native gates.
  - Preserve append-only historical rationale; any current clarification is dated
    and source-scoped. No universal formation necessity or new experiment is required
    by this action.
- action_id: plaque-t9-A1
  finding_ids:
  - plaque-t9-F1
  target_ids:
  - GO:1990196
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/macab_tolc_complex.yaml
    role: maintained scientific record
  description: State the14/15-membered preference as the reported macrolide-subclass
    profile, and preserve the broader source-supported transport scope with an appropriate
    source.
  acceptance_checks:
  - Do not change the supported2:6:3 identity or claim every cargo listed in introductory
    context was assayed by the structural study.
  - Preserve supported source-specific claims and pass applicable native gates.
  - Preserve append-only historical rationale; any current clarification is dated
    and source-scoped. No universal formation necessity or new experiment is required
    by this action.
- action_id: plaque-t9-A2
  finding_ids:
  - plaque-t9-F2
  target_ids:
  - GO:1990196
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/macab_tolc_complex.yaml
    role: maintained scientific record
  description: Replace the two author-name attributions with Lin etal2009 while retaining
    the exact PMID and supported assay descriptions.
  acceptance_checks:
  - Check both the function evidence and the first causal-edge evidence note.
  - Preserve supported source-specific claims and pass applicable native gates.
  - Preserve append-only historical rationale; any current clarification is dated
    and source-scoped. No universal formation necessity or new experiment is required
    by this action.
- action_id: septin-kinetochore-A1
  finding_ids:
  - septin-kinetochore-F1
  target_ids:
  - GO:0000776
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/kinetochore.yaml
    role: maintained scientific record
  description: Ground the existing component to GO0043505 with a current scope note.
    Preserve its Cse4 yeast role, OTHER constituent representation and unknown stoichiometry/formation
    limits. Align the corresponding whole-nucleosome graph node to STRUCTURE with
    the same exact GO grounding, retaining the component_ref.
  acceptance_checks:
  - The adopted term denotes the nucleosome class rather than Cse4 alone or generic
    chromatin.
  - The graph actor denotes the whole nucleosome platform, not Cse4 alone, and its
    node type/grounding agree with that identity.
  - No fixed octameric arrangement or universal formation necessity is inferred from
    the class mapping.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated rationale/history and append current clarification; representative
    P36012 identity remains correct.
- action_id: septin-m_aaa_complex-A1
  finding_ids:
  - septin-m_aaa_complex-F1
  target_ids:
  - GO:0005745
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/m_aaa_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, remove false CPX count attribution,
    scope3:3 protein counts explicitly to the released EMD1712/Lee preparation/model,
    and omit or independently support the six-zinc assertion. Retain Yta10/Yta12 co-assembly
    and zinc cofactor relations, experimental graph limits and correctly scoped composition/dataset
    fields.
  acceptance_checks:
  - CPX notes reflect unspecified participant counts; no3:3 or6Zn is attributed to
    CPX-1654.
  - Any3:3 statement identifies the actual preparation/model source and its engineered/detergent/C6
    limits.
  - Six zinc is either omitted as an unsupported quantity or supported by an exact
    independently verified source; do not infer it is biologically false.
  - Preserve dated discussion/history; current clarification may be appended without
    rewriting historical source-access observations.
  - Do not demand new experiments, universal alternative stoichiometry, dispensability
    claims or mandatory essentiality changes.
  - Run native schema/strict/identifier gates after separately authorized curation.
limitations:
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Assigned science scope is
  four complete unchanged records at cohort indices0,1,2,4. Thirty maintained inputs
  are17 common frozen rules/config/schema/scripts, four targets, eight original artifacts
  and the frozen m-AAA record used solely in a separate auxiliary source-count challenge.
  All47 frozen inputs and20 originals are hash-audited in finalization.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Fresh genuine Vary2003 main
  Methods sec2–11, Results sec13–20, Discussion sec21, Table1 and Figures1–5 text
  captions were read. Introduction, Table2 sequence appendix, figure pixels, raw microarrays
  and external data were not read. Reciprocal recovery supports stable assemblies
  under tested conditions, not universal exclusivity or universal formation essentiality.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Vary uses W303-derived RAD5-repaired
  strains and assay-specific recombinant nucleosome/DNA substrates. S288C UniProt
  examples are references, not experimentally substituted strains. Quantitative sliding/spacing
  differences are not universal in-vivo rates.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Koike2002 is a secondary review;
  fresh PDF pp223–227 plus the dimerization conclusion at the start of p228, Table1
  and Figure1 caption read; partial later p228 localization text is not used, no pixels
  or later pages. Boulton primary abstracts were read both through MED and genuine
  PMC abstract/PDF landings, not main bodies. Feldmann and Laroche are complete indexed
  abstracts only. Downs2004 is bibliographic metadata without indexed abstract, plus
  DOI Crossref metadata, not a read review body.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Current exact six reviewed
  gene/taxon queries each return one expected S288C accession with no next page. This
  verifies bounded present joins, not historical query execution. Native annotation
  citations and real primary experiments remain different tiers.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Exact family candidates were
  checked for type, scope, native descriptions/signatures and positive protein xrefs.
  Successful Isw1/Ioc candidates are domain-level or broad; no exhaustive family absence
  or independent sequence alignment is claimed. Three initial InterPro429 responses
  and failed primary routes are retained as validation only; successful retries are
  separately timestamped.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: The complete official catalogue
  has20 organism rows/28 organism-dataset pairs and no Saccharomyces. No unmatched
  yeast proxy or gene/module query is used. E.coli packets were fetched for sibling
  reviewers but are not scientific evidence for these yeast targets. Historical runner
  unavailability remains the actual Nov3 00:49Z receipt, never a fresh execution.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Eight actual current native
  protein commands pass for nine maintained example occurrences and nine COVERED typed
  nodes:2/2/3/2. Coverage is not independent biological evidence. Eight original validate/render
  commands and61 historical input occurrences pass. Root corpus/publication/successor/final-head/CI/queue
  gates remain separate, not precertified.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Own original applicability
  defects are three formal unsupported exclusions plus one complete Ku applicability
  omission. Twenty-three historical access-only kind occurrences are corrected without
  rewriting original observations or claiming that the original authors falsely read
  bodies. No own stale targets or record edits.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Four inherited findings remain
  open at minor severity; original Isw1 F1 major is explicitly narrowed with a normalization
  reason and tracked bundle correction. Exact inherited lineages are preserved; no
  family/domain/type-only or missing-optional-example finding is introduced. Generic
  class allowance and actual within-row scope are evaluated separately. Source-neutral
  class grounding does not follow merely from species examples.'
- 'Isw1, Isw1a, Isw1b and Ku70:Ku80 independent review: Separate immutable m-AAA auxiliary
  reads the full frozen record, CPX response and EMD1712 XML only. It is a narrow
  source-count attribution challenge, not an additional assigned finding, complete
  m-AAA science review, Luo body read or image/map inspection.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: Only assigned indices5,6,9
  receive a complete scientific review here; separate Isw1 auxiliary receipt is not
  merged into these findings. All maintained inputs used are frozen and listed.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: Fresh public snapshots
  retain their actual UTC timestamps and SHA256. Yakushi2000 full body was inaccessible,
  but complete native abstract and public captions1,3,4,7 were read. No figure pixels,
  raw coordinates/maps, supplemental data or uninspected paper bodies are certified.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: Older family prose, source
  metadata and computational annotations are not elevated into direct experimental
  proof. Secondary abstracts are authority/partial, metadata-only rows database/context_only
  and failed routes validation/context_only.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: Native protein success
  validates reference identity/xrefs and diagnostic coverage, not scientific participation,
  exact family scope or formation necessity. LolCDE substrate UNANCHORED_WITH_UNIPROT
  is not automatically a missing constituent.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: The historical structured-adapter
  runner failure at 2026-11-03 around00:49Z remains historical; no fresh runner invocation
  or success is claimed. Current official API fallback, exact genes and full membership
  joins were independently inspected.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: precise1k is a five-strain
  computational expression dataset, not an exact substitute for every strain/construct
  in the experiments. Generated ai_summary text is excluded. Zero threshold flags
  do not show biological absence and module membership does not establish assembly/localization/transport.'
- 'LPS transport, LolCDE and MacAB-TolC independent review: Repository/Git/GitHub
  and original bundles were not mutated. Root owns deduplication, issue publication,
  global gates and later save/CI/queue; this source report does not certify pending
  stages.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Only the three
  assigned records are scientifically re-reviewed. All39 original historical input
  occurrences match and all three native original pairs validate/render exactly. Kinetochore
  and mAAA are stale, LYSP is unchanged; two substantive refreshes are explicit.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Current De
  Wulf/Westermann main-text sections and relevant embedded captions support kinetochore
  assembly scope; no supplements or figure pixels were inspected. Biggins is explicitly
  secondary synthesis, not new primary evidence. The CSE4 representative is valid
  but does not ground the whole nucleosome class.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Ancillary
  reference papers, including Schmitzberger2017 Kluyveromyces COMA, are limited to
  complete native abstracts. S288C reference accessions do not establish experimental
  strain; De Wulf is W303-congenic and Westermann strain supplement was not opened.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Zong genuine
  main text and listed captions were read. Dent publisher403 means Dent remains complete-primary-abstract
  scope; Bloch/Gong are likewise abstract-tier. No source figure pixels or raw experiments
  were assessed for LANDs; ectopic J558/HeLa results do not establish all endogenous
  isoforms, human prevalence or universal body formation.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Lee genuine
  main body became available through the alternate NCBI route; this does not retroactively
  invalidate the historical failed-access rationale. No Lee supplement, raw density
  map, atomistic reanalysis or image pixels were inspected. Header3:3 preparation
  and current CPX null counts remain distinct.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Luo genuine
  source sections and actual external Fig4 panelsA–D were inspected; no other pixels,
  supplementary/source-data files, coordinates or raw experimental images were analyzed.
  Reporter endpoint, separate growth response, engineered domains and species/preparation
  limits are retained. Link-only CC BY-NC-ND4.0 attribution is preserved.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: InterPro/PANTHER
  candidate checks are bounded to named entries and their reviewed members; no exhaustive
  family absence claim. Unchecked machine-generated IPR050928 prose is excluded. Shared
  families/domains are not forced onto narrower paralog/isoform classes.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Complete fresh
  official catalogue lacks all relevant yeast/human/mouse/fungal biological hosts;
  recombinant expression/template organisms are not proxies. Downstream unmatched-dataset
  queries are not applicable. Historical runner PermissionError retains Nov3 00:49
  time; no fresh invocation or biology-absence inference.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: Six actual
  native protein commands pass:16 reviewed constituent examples and5typed nodes,4COVERED
  plus external Bright1UNANCHORED_WITH_UNIPROT. Coverage is reference validation,
  not class-grounding, source-count, assembly or necessity certification.'
- 'Kinetochore, LYSP100-associated domain and m-AAA independent review: All failed/challenged
  or wrong-initial-route responses remain diagnostics; HTTP200 alone does not establish
  paper text. Successful alternates have independent actual times and hashes. No records,
  original bundles, Git refs or GitHub content were mutated; root-owned fullQC, later
  saved-head checks/CI/queue/merge are not certified here.'
- Historical observations remain immutable; their old checks are not represented as
  current-head execution.
- The adapter runner was not rerun. Its retained November3 PermissionError receipt
  is historical; current catalogue coverage is assessed directly, and fresh or reused
  responses retain their actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include
  909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks
  independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited
  by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head
  CI and merge-group CI occur after saving this immutable observation and are not
  represented here as already completed.
notes:
- Three changed targets require substantive current-input reassessment; seven other
  current target hashes match original frozen inputs. All used maintained context
  is frozen before synthesis.
- 'Twenty current native protein commands passed across 38 represented protein examples
  and 28 typed GENE_OR_PROTEIN nodes: 26 COVERED and two UNANCHORED_WITH_UNIPROT (LolCDE
  substrate and LYSP100 Bright/ARID3A). External machinery and substrates are not
  forced into constituent rows. Identity and coverage are not experimental membership
  or necessity evidence.'
- Original observations and dated rationale remain immutable. Source bodies, abstracts,
  database entries and failed-access diagnostics retain exact scopes and dates.
- 'Root synthesis explicitly corrects six native evidence snapshot/reference bindings
  identified during integration: the snapshot hashes now identify the referenced receipt
  JSON; each locator and summary preserve the separately verified stdout path/hash.
  Immutable independent source reports, executed checks and scientific results are
  unchanged.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080127Z-isw1-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080128Z-isw1a-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080128Z-isw1b-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080129Z-kinetochore-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080129Z-ku70-ku80-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080130Z-lipopolysaccharide-transport-system-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080132Z-lolcde-lipoprotein-abc-transporter-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080132Z-lysp100-associated-nuclear-domain-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080133Z-m-aaa-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T080133Z-macab-tolc-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2395
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/3026
- https://github.com/CultureBotAI/CellStructureMech/issues/3027
- https://github.com/CultureBotAI/CellStructureMech/issues/3028
- https://github.com/CultureBotAI/CellStructureMech/issues/3029
- https://github.com/CultureBotAI/CellStructureMech/issues/3030
- https://github.com/CultureBotAI/CellStructureMech/issues/3031
- https://github.com/CultureBotAI/CellStructureMech/issues/3032
- https://github.com/CultureBotAI/CellStructureMech/issues/3033
- https://github.com/CultureBotAI/CellStructureMech/issues/3034
- https://github.com/CultureBotAI/CellStructureMech/issues/3035
- https://github.com/CultureBotAI/CellStructureMech/issues/3036
- https://github.com/CultureBotAI/CellStructureMech/issues/3037
- https://github.com/CultureBotAI/CellStructureMech/issues/3038
- https://github.com/CultureBotAI/CellStructureMech/issues/3039
- https://github.com/CultureBotAI/CellStructureMech/issues/3040
- https://github.com/CultureBotAI/CellStructureMech/issues/3041
```
