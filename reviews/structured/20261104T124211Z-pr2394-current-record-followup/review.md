# PR 2394: current-input review of ten records and adversarial follow-up

- Review: 20261104T124211Z-pr2394-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T12:22:27.268858Z
- Finished UTC: 2026-11-04T12:42:11Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Independent whole-record reassessment of ten current records retains nine inherited scientific findings and establishes one new major source-attribution finding in the stale i-AAA record: three major and seven minor findings across eight records needing curation. Hsp78 and hyphal-tip polarisome pass with explicit limitations. One stale record review is substantively refreshed against current inputs; the other nine records are byte-identical to their original frozen targets. The immutable successor corrects ten applicability assessments and six historical access-only evidence kinds, preserves all original artifacts and source-access boundaries, and links every scientific action to a separate open record-curation issue. No records are edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main d4d24c6c38d06ef27a6bac2c25ed381d50e96431. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head a1efd4e9ec612b402ce4ffdf9a65ffafc137cddb.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base f5668d26c554ec2f62610183aed5c5bc3aa76826.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070823 | data/structures/other/hda1_complex.yaml | maintained | HDA1 complex |
| GO:1990085 | data/structures/other/hda_beta_clamp_complex.yaml | maintained | Hda-beta clamp complex |
| GO:0000417 | data/structures/other/hir_complex.yaml | maintained | HIR complex |
| cellstructuremech:holdfast | data/structures/other/holdfast.yaml | maintained | holdfast |
| GO:0030897 | data/structures/other/hops_complex.yaml | maintained | HOPS complex |
| cellstructuremech:hsp78_chaperone_complex | data/structures/other/hsp78_chaperone_complex.yaml | maintained | Hsp78 chaperone complex |
| GO:0001411 | data/structures/other/hyphal_tip.yaml | maintained | hyphal tip |
| GO:0031562 | data/structures/other/hyphal_tip_polarisome.yaml | maintained | hyphal tip polarisome |
| GO:0031942 | data/structures/other/i_aaa_complex.yaml | maintained | i-AAA complex |
| GO:0031011 | data/structures/other/ino80_complex.yaml | maintained | Ino80 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | Native TraitMech check passed: all 10 links resolve with matching labels against the 1130-trait source index. |
| Pinned governed files | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | All 22 governed artifacts match the pinned CLAW revision. |
| Native identifier resolver | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified all 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0070823 | passed | True | GO:0070823 | Documented focused command passed. |
| validate-strict GO:0070823 | passed | True | GO:0070823 | Documented focused command passed. |
| validate GO:1990085 | passed | True | GO:1990085 | Documented focused command passed. |
| validate-strict GO:1990085 | passed | True | GO:1990085 | Documented focused command passed. |
| validate GO:0000417 | passed | True | GO:0000417 | Documented focused command passed. |
| validate-strict GO:0000417 | passed | True | GO:0000417 | Documented focused command passed. |
| validate cellstructuremech:holdfast | passed | True | cellstructuremech:holdfast | Documented focused command passed. |
| validate-strict cellstructuremech:holdfast | passed | True | cellstructuremech:holdfast | Documented focused command passed. |
| validate GO:0030897 | passed | True | GO:0030897 | Documented focused command passed. |
| validate-strict GO:0030897 | passed | True | GO:0030897 | Documented focused command passed. |
| validate cellstructuremech:hsp78_chaperone_complex | passed | True | cellstructuremech:hsp78_chaperone_complex | Documented focused command passed. |
| validate-strict cellstructuremech:hsp78_chaperone_complex | passed | True | cellstructuremech:hsp78_chaperone_complex | Documented focused command passed. |
| validate GO:0001411 | passed | True | GO:0001411 | Documented focused command passed. |
| validate-strict GO:0001411 | passed | True | GO:0001411 | Documented focused command passed. |
| validate GO:0031562 | passed | True | GO:0031562 | Documented focused command passed. |
| validate-strict GO:0031562 | passed | True | GO:0031562 | Documented focused command passed. |
| validate GO:0031942 | passed | True | GO:0031942 | Documented focused command passed. |
| validate-strict GO:0031942 | passed | True | GO:0031942 | Documented focused command passed. |
| validate GO:0031011 | passed | True | GO:0031011 | Documented focused command passed. |
| validate-strict GO:0031011 | passed | True | GO:0031011 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | All ten positive molecular narratives trigger structured-source applicability. The complete fresh official iModulonDB catalogue contains 20 organism rows and 28 organism/dataset pairs. It lacks the named yeast, Neurospora and Caulobacter biological hosts; recombinant E. coli expression hosts are not proxies. For the Hda-beta clamp record, e_coli/precise1k contains exact hda/b2496/P69931 and dnaN/b3701/P0A988 matches; both have zero thresholded memberships among 201 modules. The 4257-gene, 1035-sample, 518-condition, five-strain dataset is expression context, not the Kurz assay preparation or evidence of physical assembly or biological absence. Historical runner PermissionError retains its actual November3 timestamp; fresh native packets have their own access times. |
| Independent claim-level source review | passed | True | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native HDA1 complex UniProt verify check | passed | True | GO:0070823 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native HDA1 complex UniProt causal check | passed | True | GO:0070823 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Hda-beta clamp complex UniProt verify check | passed | True | GO:1990085 | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Hda-beta clamp complex UniProt causal check | passed | True | GO:1990085 | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native HIR complex UniProt verify check | passed | True | GO:0000417 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native HIR complex UniProt causal check | passed | True | GO:0000417 | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native holdfast UniProt verify check | passed | True | cellstructuremech:holdfast | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native holdfast UniProt causal check | passed | True | cellstructuremech:holdfast | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native HOPS complex UniProt verify check | passed | True | GO:0030897 | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native HOPS complex UniProt causal check | passed | True | GO:0030897 | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Hsp78 chaperone complex UniProt verify check | passed | True | cellstructuremech:hsp78_chaperone_complex | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Hsp78 chaperone complex UniProt causal check | passed | True | cellstructuremech:hsp78_chaperone_complex | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native hyphal tip UniProt verify check | passed | True | GO:0001411 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native hyphal tip UniProt causal check | passed | True | GO:0001411 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native hyphal tip polarisome UniProt verify check | passed | True | GO:0031562 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native hyphal tip polarisome UniProt causal check | passed | True | GO:0031562 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native i-AAA complex UniProt verify check | passed | True | GO:0031942 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native i-AAA complex UniProt causal check | passed | True | GO:0031942 | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Ino80 complex UniProt verify check | passed | True | GO:0031011 | 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Ino80 complex UniProt causal check | passed | True | GO:0031011 | 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Original/current native inputs and artifacts

schema: supported. Targets: GO:0070823.

Current target equals original frozen source and reviewed main. Six original native validate/render commands pass; own42 historical input occurrences match declared revisions/hashes and six original artifact bytes are unchanged.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0070823.

Original formal no-iModulon-specific-claim rationale excludes a record with explicit molecular/function/pathway assertions. Fresh complete catalogue has no matched yeast host; no foreign-host proxy is used. Historical runner failure is not fresh.

### Actual native protein scope

schema: supported. Targets: GO:0070823.

Three maintained reviewed examples and three covered protein nodes. Both actual commands exit0; coverage is not biological confirmation.

### Existing tasks and append-only rationale

provenance: supported. Targets: GO:0070823.

The active source-neutral grounding task can be progressed with verified class identities; historical rationale need not be rewritten to mimic a present inventory. Preserve dates/events and update current notes or narrow prompts. No record edits or grouped-issue closure.

### Original and current access tiers

evidence: concern. Targets: GO:0070823.

Original contains 3 access-only rows misclassified primary_source; original summaries already admit their limits. Correct successor kinds only, retaining old times/hashes. Current metadata/abstract and genuine primary-body reads are separately scoped.

### Physical necessity versus function and recovery

grounding: unknown. Targets: GO:0070823.

Current UNKNOWN formation values remain permitted. Activity loss, viability, localization, conditional recovery and universal formation necessity are distinct; no automatic ESSENTIAL conversion or new experiment is required.

### Image/quantitative-property coverage

scope: not_applicable. Targets: GO:0070823.

No maintained images or physical-property fields require pixel inspection for this target. Text captions read only within explicit source scopes; no pixels, raw-gel quantification or structural coordinate analysis claimed.

### Original/current native inputs and artifacts

schema: supported. Targets: GO:1990085.

Current target equals original frozen source and reviewed main. Six original native validate/render commands pass; own42 historical input occurrences match declared revisions/hashes and six original artifact bytes are unchanged.

### Whole-record structured-source applicability

scope: concern. Targets: GO:1990085.

Original formal no-iModulon-specific-claim rationale excludes a record with explicit molecular/function/pathway assertions. Actual E.coli precise1k dataset is matched at reference locus level; hda and dnaN each have zero thresholded memberships in201 rows, with five-strain/assay-context limits. Historical runner failure is not fresh.

### Actual native protein scope

schema: supported. Targets: GO:1990085.

Two maintained reviewed examples; only Hda is a typed protein node and is COVERED. DnaN ring is a structure. Both actual commands exit0; coverage is not biological confirmation.

### Existing tasks and append-only rationale

provenance: supported. Targets: GO:1990085.

The active source-neutral grounding task can be progressed with verified class identities; historical rationale need not be rewritten to mimic a present inventory. Preserve dates/events and update current notes or narrow prompts. No record edits or grouped-issue closure.

### Original and current access tiers

evidence: supported. Targets: GO:1990085.

No failed-access kind defect found in this original after full evidence inventory inspection. Current metadata/abstract and genuine primary-body reads are separately scoped.

### Physical necessity versus function and recovery

grounding: unknown. Targets: GO:1990085.

Current UNKNOWN formation values remain permitted. Activity loss, viability, localization, conditional recovery and universal formation necessity are distinct; no automatic ESSENTIAL conversion or new experiment is required.

### Image/quantitative-property coverage

scope: not_applicable. Targets: GO:1990085.

No maintained images or physical-property fields require pixel inspection for this target. Text captions read only within explicit source scopes; no pixels, raw-gel quantification or structural coordinate analysis claimed.

### Original/current native inputs and artifacts

schema: supported. Targets: GO:0000417.

Current target equals original frozen source and reviewed main. Six original native validate/render commands pass; own42 historical input occurrences match declared revisions/hashes and six original artifact bytes are unchanged.

### Whole-record structured-source applicability

scope: concern. Targets: GO:0000417.

Original formal no-iModulon-specific-claim rationale excludes a record with explicit molecular/function/pathway assertions. Fresh complete catalogue has no matched yeast host; no foreign-host proxy is used. Historical runner failure is not fresh.

### Actual native protein scope

schema: supported. Targets: GO:0000417.

Four maintained reviewed examples and four covered protein nodes. Both actual commands exit0; coverage is not biological confirmation.

### Existing tasks and append-only rationale

provenance: supported. Targets: GO:0000417.

The active source-neutral grounding task can be progressed with verified class identities; historical rationale need not be rewritten to mimic a present inventory. Preserve dates/events and update current notes or narrow prompts. No record edits or grouped-issue closure.

### Original and current access tiers

evidence: concern. Targets: GO:0000417.

Original contains 2 access-only rows misclassified primary_source; original summaries already admit their limits. Correct successor kinds only, retaining old times/hashes. Current metadata/abstract and genuine primary-body reads are separately scoped.

### Physical necessity versus function and recovery

grounding: unknown. Targets: GO:0000417.

Current UNKNOWN formation values remain permitted. Activity loss, viability, localization, conditional recovery and universal formation necessity are distinct; no automatic ESSENTIAL conversion or new experiment is required.

### Image/quantitative-property coverage

scope: not_applicable. Targets: GO:0000417.

No maintained images or physical-property fields require pixel inspection for this target. Text captions read only within explicit source scopes; no pixels, raw-gel quantification or structural coordinate analysis claimed.

### Exact HDA1 identity and parent/parthood

identity: supported. Targets: GO:0070823.

Active GO0070823 describes two Hda1 with Hda2/Hda3 and is_a GO0000118; chromatin GO0000785 is parthood. Wu hydrodynamic analysis suggests the tetramer rather than supplying an atomic-count determination. The record does not conflate this class-II assembly with Rpd3/class-I complex.

### Exact Hda1 and Hda3 family task

grounding: concern. Targets: GO:0070823.

The explicit deferred task can be narrowed: IPR017321 is the yeast class-II Hda1 family and IPR026216 is the specific Hda3 family, with positive native P53973/Q06623 xrefs. Shared Hda2/3 IPR021006 and broad deacetylase IPR000286 do not uniquely denote the respective narrower named class. Hda2 remains unresolved within this bounded candidate set, not globally ungroundable.

### Assembly and activity observations remain distinct

evidence: supported. Targets: GO:0070823.

Wu native co-IP/direct GST tests support Hda1 self-association and Hda2/Hda3 subassembly. hda2-deletion reduces recovered Hda3 partly with instability; hda3-deletion loses Hda2 co-IP despite reported comparable Hda2. Activity assays fall to background in deletions. Current constituent roles are compatible; these conditional observations do not force new universal necessity findings.

### All membership and deacetylase-function edges

graph: supported. Targets: GO:0070823.

Three contributes-to and the histone-deacetylase function edge fit direct complex/activity evidence and GO0004407. Wu ENA1 ChIP H3/H2B effects are locus/assay-specific; Carmen abstract includes broad core-histone deacetylation. No universal in-vivo preference across all genes/histones is asserted by this coarse graph.

### Species/reference identity and historic mass

scope: supported. Targets: GO:0070823.

Yeast species example is compatible with Wu YDS/WJY experimental backgrounds. S288C examples are separate current reference annotations. Carmen1996 is complete abstract only: approximate350kDa HDA and different HDB are historical biochemical context, not an independently read body or precise structural mass.

### Hda-beta state and DnaA boundary

identity: supported. Targets: GO:1990085.

Active GO1990085 exact synonyms and parent1990078 support the Hda/DnaN complex. GO0044775 beta ring is a complex constituent/has_part; GO1990083 DnaA-Hda is distinct. DnaA is functionally relevant but not automatically a constituent of this two-class record.

### Resolvable Hda branch

grounding: concern. Targets: GO:1990085.

Current Hda label-only class and active explicit task defer a verified family: IPR017788 is the Hda branch distinct from initiator DnaA, carried by P69931. IPR022864 is the narrower Enterobacteriaceae child; no broader DnaA-like identity or species accession substitutes for the whole Hda class.

### Direct binding versus RIDA reaction

evidence: supported. Targets: GO:1990085.

Kurz directly tests purified Hda-beta binding, motif mutants and peptide competition. The source connects binding to proposed RIDA relevance and prior DnaA-ATP hydrolysis work; record graph explicitly does not resolve loading or ATP-hydrolysis chemistry. Motif-mutant solubility controls do not eliminate misfolding, and no whole-RIDA reconstitution is claimed.

### Three bounded composition/function edges

graph: supported. Targets: GO:1990085.

Two membership contributions and the broad support of negative initiation regulation fit GO1990085/GO0032297 and direct binding plus scoped RIDA interpretation. DNA-loaded clamp requirements and DnaA contacts remain outside declared NONMECHANISTIC graph; existing DnaN structure typing is valid.

### Biological and dataset preparations

scope: supported. Targets: GO:1990085.

Kurz uses genes amplified from XL1Blue and BL21(DE3)pLyS/TB1 expression contexts. Current P69931/P0A988 are reviewed K-12 references. precise1k contains BW25113,DGF-298,GMOS,MG1655,W3110, not exact Kurz assay strains; reference locus joins are valid but expression measurements cannot establish binding/formation.

### Four-class HIR and Asf1 partner boundary

identity: supported. Targets: GO:0000417.

Active GO0000417 and Green tagged purification identify Hir1/Hir2/Hir3/Hpc2. Asf1 is an interacting cooperating histone chaperone; different purification salt/conditions and promoter/assembly assays do not make it an obligatory fifth HIR constituent. HIRA exact synonym does not impose yeast composition on every lineage.

### Specific Hir3 family and unresolved alternatives

grounding: concern. Targets: GO:0000417.

IPR033053 is a verified whole Hir3/CABIN1 homolog family and P47171 carries it; fungal/animal breadth is explicit. It resolves the existing Hir3 task without forcing named Hir1/Hir2 to the mixed IPR031120 family or Hpc2 to domain IPR014840. Remaining classes are unresolved by inspected candidates, not globally nonexistent.

### Purification/deletion and nucleosome assembly scope

evidence: supported. Targets: GO:0000417.

Green distinguishes Asf1 association losses from HIR subunit recovery: remaining partners persist in hir1/hir3 deletions, while Hir3 is not recovered in hpc2 deletion with association versus instability unresolved. HIR binds DNA and supports deposition in vitro, enhanced with Asf1 under tested conditions; no global four-subunit formation necessity or absolute Asf1 dependence follows.

### Five supported coarse membership/function edges

graph: supported. Targets: GO:0000417.

Four constituent contributions and support for GO0006334 nucleosome assembly fit primary purification and assembly assays; replication independence is the class context. The NONMECHANISTIC graph does not claim a temporal deposition sequence or conflate histone transcription regulation with physical membership.

### Yeast scope and secondary review limits

scope: supported. Targets: GO:0000417.

S.cerevisiae is the primary biological context; four S288C examples are authority identities, not a claim all Green experiments use that reference strain. Main captions name PKY backgrounds; supplementary detailed methods/strain tables are unread. Mousson2007 is a secondary review accessed as indexed abstract only, not primary mechanism proof.

### Identity-only localization citations

evidence: supported. Targets: GO:0070823, GO:1990085, GO:0000417.

Current reviewed entries and exact indexed article identities reproduce declared native citation provenance. Complete abstracts for Huh2003,Kim et al. 2003 (Dp/Hda),Ozaki2013,Sharp2002,Fillingham2009,Sherwood1993,Qian1998 were read; not all abstracts contain each protein-localization experiment. No unread body localization assay or localization-to-membership inference is claimed.

### HOPS identity, class and membrane location

identity: supported. Targets: GO:0030897.

GO0030897, membrane-protein-complex parent, vacuolar membrane location and fusion function denote distinct entities; six-member HOPS is not the larger SNARE-bound assembly.

### Six core constituents and external Ypt7

scope: supported. Targets: GO:0030897.

Seals primary recovery supports six HOPS members; Ypt7 is a GTP-state-selective interacting Rab, not a seventh constituent. No mandatory complete-family finding is inferred for every deferred class.

### Exact verified Vps11/Vps16/Vps41 families

grounding: concern. Targets: GO:0030897.

Original F1 remains: native family entries IPR016528/IPR016534/IPR016902 and matched protein xrefs support these exact source-neutral classes. Active REVIEWED_LABEL_ONLY/no exact grounding still requires correction; historical discussion rationale remains unchanged.

### Reference proteins, aliases and strain

nomenclature: supported. Targets: GO:0030897.

Six reviewed S288C examples and native gene aliases/loci match; PEP5/Vps11, PEP3/Vps18 and VAM6/Vps39 differences are legitimate synonyms. Native exact reviewed queries each return one matching accession. Reference S288C is distinct from primary BJ3505/DKY6281 and SEY strains.

### Assembly evidence versus function

completeness: supported. Targets: GO:0030897.

Rieder Vps16-dependent Vps33 core recovery is a condition-specific association result; six global UNKNOWN values do not become a defect merely because fusion is antibody-sensitive or proteins co-purify. No universal formation or viability claim is inferred.

### Bounded association, priming and fusion edges

graph: supported. Targets: GO:0030897.

NON_MECHANISTIC association/membership graph and Ypt7/fusion relationships match actual yeast assays; GTP association, ATP/Sec18 priming and antibody effects remain separate observations.

### Primary evidence and source access

evidence: supported. Targets: GO:0030897.

Seals Methods/Results/Discussion and bounded Rieder sections read in genuine HTML; older abstracts independently resolve bibliography. No Rieder whole-body, primary figure pixels or newly inspected papers behind UniProt comments claimed.

### Structured-source assessment omitted originally

scope: concern. Targets: GO:0030897.

Full original YAML/MD has no formal or prose structured-source applicability assessment. Named HOPS/Ypt7 fusion narrative triggers policy. Current complete catalogue has no yeast match; downstream molecular-module queries therefore not applicable within its actual coverage.

### Historical and current native gates

schema: supported. Targets: GO:0030897.

Original validates and renders identically with historical hashes verified. Current verify/causal exit0; Ypt7 external-xref classification is appropriate and is not a curation defect.

### Exact inherited finding retained

provenance: concern. Targets: GO:0030897.

Retain original F1 minor and action under exact predecessor identity; no other original or category finding resolved by inference. Current record unchanged and still needs scoped grounding curation.

### Local Hsp78 oligomer identity

identity: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

Local identifier appropriately denotes Hsp78 chaperone assembly; broader GO0101031 parent and matrix part_of are distinct. One exact bounded zero-hit GO query cannot establish exhaustive ontology absence.

### Reviewed Hsp78 example and broad families

nomenclature: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

P33416/HSP78/YDR258C reviewed S288C identity and gene query agree. Complete nine-match InterPro inventory supplies broad ClpA/B families/domains, not exact Hsp78-only class; generated unchecked IPR050130 description is excluded from biological evidence.

### Preparation-dependent oligomer observations

quantity: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

Native mitochondrial bands interpreted as trimers/hexamers and purified SEC conditions do not define one invariant count. WT/trap constructs, ATP/Mg and salt contexts remain separate; no six-count generalization imposed.

### ATPase, reporter recovery and heat-growth scope

graph: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

Approximately 70% reduced trap ATPase is not null; reporter resolubilization is not measured refolding and global ATP depletion is not Hsp78-specific. Glycerol growth and proteome association are not respiratory flux or fixed constituent identity.

### Source conflicts disclosed by record

consistency: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

Results/figure E614Q versus Methods E612Q, salt NaCl/KCl wording and Fig2D versus Methods temperature/centrifugation discrepancies are already explicitly disclosed. No external reconciliation invented; they do not create a new record defect.

### Experimental strains and assays

scope: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

Y03617-ES/Y13617-ES hsp78 deletion/complementation backgrounds and isolated mitochondrial assays are separate from reference S288C and E. coli recombinant expression. No bacterial transcriptome proxy.

### Actual figure and dataset provenance

provenance: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

All Figure1/2 pixels inspected and maintained MD5s match. Main article CC BY-NC-ND4.0 and project-metadata CC0 are distinct; link-only image metadata preserved. PRIDE PXD030405/030436 identity/DOI/organism confirmed without raw-MS reanalysis.

### Structured-source assessment omitted originally

scope: concern. Targets: cellstructuremech:hsp78_chaperone_complex.

Full original YAML/MD lacks an applicability row or prose decision despite positive HSP78 heat-stress/protein narrative. Current official catalogue has no yeast host; no matching dataset means no downstream query warranted, not an expression-only exemption.

### Historical failed XML classified correctly

provenance: concern. Targets: cellstructuremech:hsp78_chaperone_complex.

Original evidence[19] micro57-jaworek2022-xml is HTTP406 access-only evidence, already context_only but kind authority. Successor must classify validation while preserving October22 timestamp/raw SHA and not alleging unread primary biology; genuine separately read primary source remains valid.

### Qualified pass with native coverage limits

schema: supported. Targets: cellstructuremech:hsp78_chaperone_complex.

No scientific finding established. One current example/typed node is verified/COVERED; all original historical hashes and native render match. UNKNOWN formation and broad class boundaries remain honest limits.

### i-AAA assembly, orientation and function

identity: supported. Targets: GO:0031942.

GO0031942 and GO0098800 distinguish i-AAA assembly from inner membrane; current GO/Wu IMS context is maintained. Older Weber abstract and UniProt topology phrasing conflict with that orientation, disclosed as source conflict without silently rewriting the well-supported current record.

### Three protein classes and zinc cofactor

grounding: supported. Targets: GO:0031942.

Exact Mgr1/Mgr3 families match examples; broad FtsH and Yme1 N-terminal domain do not substitute for an exact Yme1 family. CPX1655 preserves three protein participants and zinc with null copy numbers; its source-composition layer is separate from taxon-agnostic components.

### Yme1/Mgr1/Mgr3 reference identities

nomenclature: supported. Targets: GO:0031942.

All three current protein examples reviewed S288C with correct primary genes/loci and YME1 OSD1/YTA11, MGR3 FMP24 aliases; exact queries uniquely match. CPX species-style label does not change taxon559292.

### Bounded adaptor recruitment and turnover

graph: supported. Targets: GO:0031942.

Wu supports Mgr1 bridging Yme1-Mgr3, Mgr3 stabilization of Mgr1, cooperative substrate recruitment and tested turnover. Tagged substrate effects, endogenous temperature regimes and adaptor-independent observed Yme1 size stay separate; crosslink contact is not atomically proven handoff.

### New architecture edges lack cited support

evidence: concern. Targets: GO:0031942.

Stale refresh exposes a new grouped major source defect: two appended edges assert six Yme1 copies/six zinc cofactors from CPX1655, whose native stochiometry fields are all null, and introduce a purported Wu quotation absent from the complete genuine article. Valid Yme1-core/zinc roles remain supported; an isolated-core hexamer may have a different supporting primary source.

### Association and activity do not force necessity labels

completeness: supported. Targets: GO:0031942.

Mgr1-mediated association, Mgr3-dependent stability and substrate turnover support bounded mechanism; no universal assembly-essentiality or new assay mandate follows from UNKNOWN values or CPX curator inference.

### Actual strain, figure, license and bibliography

provenance: supported. Targets: GO:0031942.

TableS1 specified ranges distinguish BY4741/CEN.PK/W303 constructs from S288C reference proteins. Figure3 pixels/MD5 and main caption/license agree; post-six-month CC BY-NC-SA4.0 link-only metadata is preserved. Other five PMID records read at full-abstract/database tier only.

### Replace expression-only exclusion with actual scope

scope: concern. Targets: GO:0031942.

Original checks[4] imodulondb says no expression-module inference is used, insufficient for its positive molecular/proteolysis narrative. Current complete catalogue lacks yeast coverage; downstream queries are not applicable within that actual catalogue after explicit assessment.

### Current three-node native coverage

schema: supported. Targets: GO:0031942.

Current verify/causal commands exit0 for three reviewed examples and three COVERED typed nodes, versus two old typed nodes. Native success does not validate the new quoted-source/count claims; zinc is chemical. Original validates/renders and historical hashes still match.

### Substantive stale refresh changes disposition

provenance: concern. Targets: GO:0031942.

Original qualified pass is a valid historical observation of bytes without the new edges. Current record needs curation for the newly added source-support defect; no invented original predecessor and no historical record-fix credit assigned to this review.

### Native original schema/render and frozen inputs

schema: supported. Targets: cellstructuremech:holdfast.

Original validation and exact rendering pass; all original historical inputs were compared to exact Git objects. Current record hash is unchanged. These checks establish provenance/schema, not scientific truth.

### Actual protein inventory and typed coverage

consistency: supported. Targets: cellstructuremech:holdfast.

Three reviewed CB15 Hfa examples; one COVERED Hfa complex node and one UNANCHORED_WITH_UNIPROT external HfsK node A0A0H3CE47 (unreviewed NA1000 reference). No missing optional component is inferred; reference identity does not prove experimental NA1000 adhesiveness.

### Dated history and discussion boundaries

provenance: supported. Targets: cellstructuremech:holdfast.

Historical reasoning remains provenance. Proposed changes address current fields or append dated clarification; no historical rationale is rewritten, no unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity alone are not findings.

### Images and exact visual-read limits

scope: supported. Targets: cellstructuremech:holdfast.

No maintained image exists in this target. Genuine textual sections/captions and, for Ino80, extracted supplementary tables are distinguished from pixel, video, coordinate and raw-data analysis; none of those unperformed analyses is claimed.

### Whole-record structured-source applicability

evidence: supported. Targets: cellstructuremech:holdfast.

Named Hfa/HfsK/c-di-GMP/holdfast biosynthesis claims require actual coverage assessment. Complete fresh official catalogue lacks the exact biological hosts, so no host-matched downstream module query applies. Primary/authority fallback is explicit; E. coli cloning/expression context is not a proxy and noncoverage is not biological absence.

### Native original schema/render and frozen inputs

schema: supported. Targets: GO:0001411.

Original validation and exact rendering pass; all original historical inputs were compared to exact Git objects. Current record hash is unchanged. These checks establish provenance/schema, not scientific truth.

### Actual protein inventory and typed coverage

consistency: supported. Targets: GO:0001411.

Three unreviewed Neurospora OR74A examples V5IQM7/Q7RVZ1/Q7RWH7; all three typed nodes COVERED. Identity coverage does not validate the expanded definition or MECHANISTIC graph label.

### Dated history and discussion boundaries

provenance: supported. Targets: GO:0001411.

Historical reasoning remains provenance. Proposed changes address current fields or append dated clarification; no historical rationale is rewritten, no unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity alone are not findings.

### Images and exact visual-read limits

scope: supported. Targets: GO:0001411.

No maintained image exists in this target. Genuine textual sections/captions and, for Ino80, extracted supplementary tables are distinguished from pixel, video, coordinate and raw-data analysis; none of those unperformed analyses is claimed.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:0001411.

Named SPA2/BUD6/BNI1 polarity, cytoskeleton and secretion claims require actual coverage assessment. Complete fresh official catalogue lacks the exact biological hosts, so no host-matched downstream module query applies. Primary/authority fallback is explicit; E. coli cloning/expression context is not a proxy and noncoverage is not biological absence.

### Native original schema/render and frozen inputs

schema: supported. Targets: GO:0031562.

Original validation and exact rendering pass; all original historical inputs were compared to exact Git objects. Current record hash is unchanged. These checks establish provenance/schema, not scientific truth.

### Actual protein inventory and typed coverage

consistency: supported. Targets: GO:0031562.

Three unreviewed Neurospora OR74A examples and all three nodes COVERED. Distinct mature-tip localizations are source-supported; no direct physical-contact or universal assembly claim follows from coverage.

### Dated history and discussion boundaries

provenance: supported. Targets: GO:0031562.

Historical reasoning remains provenance. Proposed changes address current fields or append dated clarification; no historical rationale is rewritten, no unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity alone are not findings.

### Images and exact visual-read limits

scope: supported. Targets: GO:0031562.

No maintained image exists in this target. Genuine textual sections/captions and, for Ino80, extracted supplementary tables are distinguished from pixel, video, coordinate and raw-data analysis; none of those unperformed analyses is claimed.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:0031562.

Named SPA2/BUD6/BNI1 polarity, cytoskeleton and secretion claims require actual coverage assessment. Complete fresh official catalogue lacks the exact biological hosts, so no host-matched downstream module query applies. Primary/authority fallback is explicit; E. coli cloning/expression context is not a proxy and noncoverage is not biological absence.

### Native original schema/render and frozen inputs

schema: supported. Targets: GO:0031011.

Original validation and exact rendering pass; all original historical inputs were compared to exact Git objects. Current record hash is unchanged. These checks establish provenance/schema, not scientific truth.

### Actual protein inventory and typed coverage

consistency: supported. Targets: GO:0031011.

Fifteen reviewed S288C reference examples and all fifteen nodes COVERED. These are fifteen constituent classes, not a fixed fifteen-protein stoichiometry; exact family and activity/necessity scopes are independently assessed.

### Dated history and discussion boundaries

provenance: supported. Targets: GO:0031011.

Historical reasoning remains provenance. Proposed changes address current fields or append dated clarification; no historical rationale is rewritten, no unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity alone are not findings.

### Images and exact visual-read limits

scope: supported. Targets: GO:0031011.

No maintained image exists in this target. Genuine textual sections/captions and, for Ino80, extracted supplementary tables are distinguished from pixel, video, coordinate and raw-data analysis; none of those unperformed analyses is claimed.

### Whole-record structured-source applicability

evidence: supported. Targets: GO:0031011.

Named Ino80 ATP-dependent chromatin remodeling claims require actual coverage assessment. Complete fresh official catalogue lacks the exact biological hosts, so no host-matched downstream module query applies. Primary/authority fallback is explicit; E. coli cloning/expression context is not a proxy and noncoverage is not biological absence.

### Local holdfast identity and extracellular boundary

identity: supported. Targets: cellstructuremech:holdfast.

The polar extracellular polysaccharide adhesin is a structure, distinct from the associated Hfa anchor machinery and upstream biosynthesis. GO0031012 is a broader matrix parent; bounded native holdfast search does not justify adopting a guessed exact GO identifier.

### Polymer composition and grouped anchor boundary

grounding: supported. Targets: cellstructuremech:holdfast.

Hershey primary abstract explicitly reports glucose, 3-O-methylglucose, mannose, GlcNAc and xylose in extracts. It supports the stated composition without asserting a unique whole-polymer chemical accession. HfaABD is an associated multiprotein anchor, not the holdfast matrix itself; no arbitrary single-protein family or lipid identifier is forced.

### Hfa and HfsK reference identities

identity: supported. Targets: cellstructuremech:holdfast.

P27342/hfaA, P27343/hfaB and Q45977/hfaD are reviewed CB15 references. HfaB native recommended name remains putative transcription activator, while independent primary evidence supplies its anchoring role. External HfsK A0A0H3CE47 is an unreviewed NA1000 reference; identity does not establish NA1000 as the adhesive experimental strain.

### Canonical experimental model versus reference genome

scope: concern. Targets: cellstructuremech:holdfast.

The current canonical NA1000 note attributes anchoring/composition/c-di-GMP work to Sulkowski. Sulkowski specifies CB15 and derivatives, and Sprecher uses NA1000 as a nonadherent comparison. F1 retains the precise strain/source correction without invalidating the reference HfsK accession or asserting every engineered NA1000 derivative is nonadherent.

### Species presence and developmental state

scope: supported. Targets: cellstructuremech:holdfast.

C. vibrioides/crescentus synonymy and CB15/NA1000 identities are explicit. Species-level developmental presence is distinguished from condition, cell-cycle state and strain-specific loss/nonadherence. These studies are not an exhaustive species prevalence census; the actionable canonical-strain mismatch is separately recorded.

### Matrix formation versus anchoring and cohesion

completeness: supported. Targets: cellstructuremech:holdfast.

Hfa mutants can synthesize and shed holdfast, supporting DISPENSABLE for formation of matrix while anchoring/adhesion fails. HfsK deletion alters cohesion and shear resistance; direct chemical substrate/acylation mechanism remains unresolved. These measured endpoints are not collapsed into one universal necessity.

### Coarse cohesion, anchoring and adhesion mechanism

graph: supported. Targets: cellstructuremech:holdfast.

The graph correctly keeps external HfsK separate from polysaccharide and Hfa machinery. HfsK tunes cohesion; Hfa retains matrix at pole/stalk; matrix adheres cells to surfaces. It does not assert the removed under-evidenced synthesis/export edge, direct acetylation chemistry or a universal assembly ordering.

### Sulkowski title and real source access

provenance: concern. Targets: cellstructuremech:holdfast.

The current bibliography substitutes Old Cell Pole for the published title phrase Outer Membrane. F2 is a local title correction. Sulkowski/Sprecher genuine bodies are distinguished from Hershey complete abstract; no failed Hershey route is promoted to a body read.

### Fungal tip and region/complex distinction

identity: supported. Targets: GO:0001411.

GO0001411 identifies the fungal hyphal tip; GO0030427 site of polarized growth and GO0051286 cell tip are correct parents. Spitzenkorper/polarisome are parts of the region, not synonyms for the whole tip or an arbitrary protein class.

### Expanded definition and cross-lineage source attribution

scope: concern. Targets: GO:0001411.

The maintained definition adds oomycetes and generalized apparatus mechanisms while citing only GO0001411. Exact GO wording is fungal, and Lichius directly studies Neurospora with prior fungal comparisons; it does not establish the added oomycete defining scope. F1 requests relevant evidence/qualification, not an assertion that oomycetes lack tips.

### Three native reference proteins and source strains

identity: supported. Targets: GO:0001411.

V5IQM7/spa2/NCU03115, Q7RVZ1/bud6/NCU08468 and Q7RWH7/bni1/NCU01431 are unreviewed OR74A examples. Native taxonomy includes N150/FGSC9013 equivalent names, while Lichius specifies additional transformed/deletion backgrounds; accession identity is not a substitute for each experiment.

### Broader family candidates and optional grounding

grounding: supported. Targets: GO:0001411.

Spa2/Sph1 includes paralogues, and the inspected SRCIN1/actin-regulator families do not by themselves resolve the exact local classes. Unchecked machine-generated descriptive prose is excluded. Existing label-only rows are not automatically defective because a broader family or optional example exists.

### Neurospora mature-tip observations

scope: supported. Targets: GO:0001411.

Lichius supports the Neurospora model and distinct mature apical-dome localizations, including subapical BUD6 outside Spk and SPA2/BNI1 partial Spk/apical localization. COMMON is qualitative model-level context, not a measured prevalence fraction or an assertion that every developmental stage has identical geometry.

### Architecture defects versus universal tip formation

completeness: unknown. Targets: GO:0001411.

Deletion analyses alter Spk integrity, growth and morphology, but polarized extension can persist without a detectable Spk. CONDITIONAL retains this architecture/growth evidence without certifying that the whole tip or every partial polarisome cannot form. No forced all-or-none essentiality or new experiment is requested.

### Spatial parthood/function graph mislabeled mechanistic

graph: concern. Targets: GO:0001411.

Five part_of edges plus whole-structure function describe topology and function. The MECHANISTIC label and assembly/functional-mechanism title overstate what is encoded. F2 can be addressed by accurately labeling this map NONMECHANISTIC and narrowing its title; no additional molecular steps are mandatory.

### Localized complex boundary and exact ontology

identity: supported. Targets: GO:0031562.

GO0031562 identifies the protein complex at the tip of a growing fungal hypha, with GO0000133 polarisome parent and GO0001411 parthood. It is distinct from the whole apical region and from the Spitzenkorper alone.

### Three native proteins and independent localization

identity: supported. Targets: GO:0031562.

All three unreviewed OR74A accessions, primary genes and loci match the maintained examples. Native authority supports identity; Lichius supports the relevant localizations. Reference equivalence to N150/FGSC9013 does not erase the reported mutant/transformant backgrounds.

### Label-only exact classes and broader candidates

grounding: supported. Targets: GO:0031562.

Inspected Spa2/Sph1 and broader SRCIN1/actin-regulator classifications do not independently justify forcing exact retained local classes onto broad family or domain IDs. Machine-generated descriptive prose is excluded; open grounding discussion remains explicitly bounded rather than silently resolved.

### Mature hyphal-tip architecture and other developmental contexts

scope: supported. Targets: GO:0031562.

SPA2 partially overlaps Spk/apical dome; BUD6 forms an excluded subapical cloud; BNI1 occupies Spk core plus apical cap. Source also reports germling, cell-fusion, septal-plug and cytokinetic contexts, which are kept outside this first mature-tip assembly boundary rather than denied biologically.

### Conditional architecture and unresolved formation necessity

completeness: unknown. Targets: GO:0031562.

Deletion phenotypes show conditional architecture/growth contributions, not universal abolition of every encompassing tip or residual complex. UNKNOWN formation-specific scope is retained and CONDITIONAL is not treated as universal catalytic/growth essentiality.

### Accurately labeled nonmechanistic architecture

graph: supported. Targets: GO:0031562.

NONMECHANISTIC FUNCTION scope is appropriate for the mature-tip constituent distributions and polarity function. It neither asserts direct physical interactions from colocalization nor imports septal-plug/cytokinetic assemblies into this record.

### Exact complex, ancestry and fifteen constituent classes

identity: supported. Targets: GO:0031011.

GO0031011, parent GO0097346 and nuclear-chromosome parthood are current and exact. Actual Supplementary Table2 supports all fifteen named INO80 classes. This list is not a fixed fifteen-molecule stoichiometry; Rvb multiplicity and shared components remain distinct.

### Reviewed yeast reference genes and status

identity: supported. Targets: GO:0031011.

All fifteen examples are reviewed S288C references with matching native names/aliases and current one-result bounded queries. Native status/identity does not assign every cited culture to S288C. Watanabe TAP preparations and recombinant E. coli histone expression are separate biological/sample contexts.

### Five verified Ies families and broader retained boundaries

grounding: concern. Targets: GO:0031011.

Ies1/IPR038014, Ies2/IPR029523, Ies4/IPR062650, Ies5/IPR020366 and Ies6/IPR029525 are full-family entries with independent native reference-protein membership. The current five deferrals remain actionable F1. Shared INO80/SWR1, Rvb1/2, actin/Arp, Sas5/TAF14 and HMGB candidates are not forced onto narrower classes; no exhaustive absence claim for Ies3.

### Three TAP preparations and physical module associations

evidence: supported. Targets: GO:0031011.

Supplementary Table2 reports spectral counts and coverage for all fifteen INO80 classes in three independent preparations. Arp8 deletion removes the Arp8/Arp4/Act1 module; Ies6 deletion removes Arp5 from residual complex. These measured associations are bounded positive context, not evidence that the entire complex ceases to form.

### Activity, residual complexes and necessity

completeness: unknown. Targets: GO:0031011.

Watanabe distinguishes reduced Arp8-module remodeling from inactive Ies6/Arp5 module-loss preparations, while residual complexes are purified. Functional loss and physical module dependence do not establish universal all-or-none formation requirements for every constituent. UNKNOWN remains valid and does not deny measured module dependencies.

### Explicit nonmechanistic inventory and remodeling activity

graph: supported. Targets: GO:0031011.

The graph declares NONMECHANISTIC FUNCTION scope for fifteen members and chromatin remodeling. It does not require invented ordered assembly steps. Earlier Shen helicase claim and later Watanabe inability to detect helicase, and Tosi versus Watanabe Rvb ring interpretations, remain source-specific; the record does not assert either contested mechanism/count.

### Primary bodies, abstract-only papers and secondary context

evidence: supported. Targets: GO:0031011.

Watanabe genuine body and supplementary tables provide current direct composition/module evidence. Shen2000/2003, Jonsson2004, Tosi2013 and ancillary localization/Rvb studies were read at complete native abstract scope only. Clapier/Cairns2009 is secondary abstract context, not primary mechanism evidence. No unseen images, coordinates, raw spectra or full bodies are certified.

### Independent current scientific disposition

consistency: concern. Targets: cellstructuremech:holdfast.

Needs curation: 2 inherited findings independently retained, no invented new predecessor or optional-field defect. Scientific curation remains outside this review PR; the applicability bundle defect is corrected by current review evidence. Source access, reference strains, formation and visual-read limits remain explicit.

### Independent current scientific disposition

consistency: concern. Targets: GO:0001411.

Needs curation: 2 inherited findings independently retained, no invented new predecessor or optional-field defect. Scientific curation remains outside this review PR; the applicability bundle defect is corrected by current review evidence. Source access, reference strains, formation and visual-read limits remain explicit.

### Independent current scientific disposition

consistency: supported. Targets: GO:0031562.

Pass with limitations: 0 inherited findings independently retained, no invented new predecessor or optional-field defect. Scientific curation remains outside this review PR; the applicability bundle defect is corrected by current review evidence. Source access, reference strains, formation and visual-read limits remain explicit.

### Independent current scientific disposition

consistency: concern. Targets: GO:0031011.

Needs curation: 1 inherited findings independently retained, no invented new predecessor or optional-field defect. Scientific curation remains outside this review PR; the applicability bundle defect is corrected by current review evidence. Source access, reference strains, formation and visual-read limits remain explicit.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0070823, GO:1990085, GO:0000417, cellstructuremech:holdfast, GO:0030897, cellstructuremech:hsp78_chaperone_complex, GO:0001411, GO:0031562, GO:0031942, GO:0031011.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Resolve Hda1 and Hda3 family mappings

minor / open / confirmed; issue key: hda1-resolve-hda1-hda3-families.

The open task and label-only rows still defer all three families. Native IPR017321 and IPR026216 now resolve the Hda1 and Hda3 classes, while the inspected Hda2 candidate remains broader.

### micro-F2: Resolve the Hda family mapping

minor / open / confirmed; issue key: hda-beta-resolve-hda-family.

The Hda component and existing open task defer the exact family although native IPR017788 is the verified Hda branch, distinct from DnaA, and matches the reviewed reference protein.

### micro-F3: Resolve the Hir3 whole-family mapping

minor / open / confirmed; issue key: hir-resolve-hir3-family.

The open family task and Hir3 label-only row still defer a mapping despite verified IPR033053 Hir3/CABIN1 whole-family identity and the matching P47171 reference. Other HIR component boundaries remain unresolved by the inspected candidates.

### plaque-t4-F1: Ground three named HOPS subunit classes

minor / open / confirmed; issue key: hops-exact-vps11-vps16-vps41-families.

Current native whole-family identities IPR016528 (Vps11), IPR016534 (Vps16) and IPR016902 (Vps41), corroborated by matched reviewed protein memberships, reconfirm original F1. The active reviewed-label-only deferral and open task should record these exact mappings. This is not a requirement to ground every remaining class or rewrite dated discussion rationale.

### plaque-t8-F1: Repair source support for the newly added i-AAA core and cofactor edges

major / open / confirmed; issue key: i-aaa-added-core-stoichiometry-source-support.

The current October24 addition asserts six Yme1 copies and six zinc cofactors from CPX-1655, but its full native response has present null stochiometry fields for every participant. The Yme1 edge also presents a purported verbatim rocky-road/spiral-staircase quotation attributed to DOI10.1083/jcb.201702125 which is absent from the complete genuine JATS (including captions). The cited Wu study supports recruitment/turnover, not this quoted structural claim. This materially misattributes central architecture evidence and conflicts with the record’s retained unspecified source counts. It does not establish that a separately studied isolated Yme1 core cannot be hexameric.

### septin-holdfast-F1: Correct the canonical holdfast model strain

major / open / confirmed; issue key: holdfast-canonical-strain-source.

The canonical example names NA1000 tax565050 and attributes its anchoring/composition/c-di-GMP model role to Sulkowski2019. That study specifies CB15 and CB15-derived strains; the separately cited Sprecher study explicitly uses NA1000 as a nonadherent comparison. The current unqualified canonical strain/source pairing is materially misleading. Independently reconfirmed against the freshly inspected source/authority scopes recorded here. Correct current fields or append dated clarification in separately authorized curation; preserve historical rationale.

### septin-holdfast-F2: Correct the Sulkowski paper title

minor / open / confirmed; issue key: holdfast-sulkowski-title.

The DOI bibliography substitutes Old Cell Pole for Outer Membrane in the title. Native MED and the genuine primary title agree on A Multiprotein Complex Anchors Adhesive Holdfast at the Outer Membrane of Caulobacter crescentus. Independently reconfirmed against the freshly inspected source/authority scopes recorded here. Correct current fields or append dated clarification in separately authorized curation; preserve historical rationale.

### septin-hyphal_tip-F1: Source and qualify the expanded hyphal-tip definition

major / open / confirmed; issue key: hyphal-tip-definition-scope.

The fungal GO identity is extended in the maintained defining text to oomycetes and generalized apparatus mechanisms while definition_source remains GO0001411. The exact GO definition and the cited Neurospora primary study do not establish that cross-lineage defining scope. Independently reconfirmed against the freshly inspected source/authority scopes recorded here. Correct current fields or append dated clarification in separately authorized curation; preserve historical rationale.

### septin-hyphal_tip-F2: Label the spatial graph as nonmechanistic

minor / open / confirmed; issue key: hyphal-tip-graph-scope.

All five constituent edges are parthood statements and the final edge attaches a whole-structure function. The MECHANISTIC label and mechanism title imply a causal explanation that the graph does not encode. Independently reconfirmed against the freshly inspected source/authority scopes recorded here. Correct current fields or append dated clarification in separately authorized curation; preserve historical rationale.

### septin-ino80_complex-F1: Ground five exact Ies subunit families

minor / open / confirmed; issue key: ino80-exact-ies-families.

Ies1, Ies2, Ies4, Ies5 and Ies6 remain REVIEWED_LABEL_ONLY because exact families were not curated in this pass. Current native full-family entries and independently verified protein membership resolve those specific classes. Independently reconfirmed against the freshly inspected source/authority scopes recorded here. Correct current fields or append dated clarification in separately authorized curation; preserve historical rationale.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, ground Hda1 and Hda3 at their verified whole-family identities and narrow the remaining task to Hda2.

- Use IPR017321 for the yeast class-II Hda1 class and IPR026216 for Hda3.
- Do not use shared IPR021006 as an exact Hda2-only mapping.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve all dated discussions.rationale, posed dates and curation events; record progress in current notes, narrow prompts or appended explanation rather than rewriting historical observations.
- Retain supported protein examples, complex boundaries and permissible global UNKNOWN formation values; no new experiments or optional exhaustive inventory is required.
- No maintained record edit occurs in this review PR.

### micro-A2

In separately authorized record curation, ground Hda at the verified whole-family identity and resolve the existing task.

- Use IPR017788 for the Hda class, retaining IPR022864 as narrower Enterobacteriaceae context.
- Keep the DnaN beta ring as the already grounded GO complex and preserve the DnaA boundary.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve all dated discussions.rationale, posed dates and curation events; record progress in current notes, narrow prompts or appended explanation rather than rewriting historical observations.
- Retain supported protein examples, complex boundaries and permissible global UNKNOWN formation values; no new experiments or optional exhaustive inventory is required.
- No maintained record edit occurs in this review PR.

### micro-A3

In separately authorized record curation, ground Hir3 in the verified homolog family and narrow the existing task to the unresolved component classes.

- Use IPR033053 with the fungal Hir3 reference example and the native homolog breadth stated.
- Do not use mixed HIR1/HIR2 IPR031120 or HRD domain IPR014840 as exact replacements for their named complete classes.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.
- Preserve all dated discussions.rationale, posed dates and curation events; record progress in current notes, narrow prompts or appended explanation rather than rewriting historical observations.
- Retain supported protein examples, complex boundaries and permissible global UNKNOWN formation values; no new experiments or optional exhaustive inventory is required.
- No maintained record edit occurs in this review PR.

### plaque-t4-A1

Curate the verified Vps11/IPR016528, Vps16/IPR016534 and Vps41/IPR016902 class mappings with exact scope and evidence; update current grounding notes/task disposition while preserving dated historical rationale. Do not substitute broader families or domains for other unresolved classes.

- Each adopted family is the named whole protein class, with original role evidence retained.
- Broader Vps39/Vps3, Vps41/Vps8, Sec1-like families and isolated domains are not substituted indiscriminately.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Historical discussion rationale and curation history remain append-only; no unsupported mechanism or necessity change.

### plaque-t8-A1

Repair the new core/cofactor edge evidence: remove the absent quotation and incorrect CPX six-copy attribution. Preserve supported Yme1 proteolytic-core and zinc-cofactor participation. If precise hexameric/asymmetric architecture is retained, inspect and cite a genuinely supporting primary structural study and explicitly distinguish its preparation/isolated core from the adaptor-bearing yeast assembly; otherwise qualify or remove unsupported count/architecture clauses. Append the correction history without rewriting dated rationale.

- Each retained snippet is verifiably verbatim in its cited inspected source; paraphrases stay in notes.
- CPX1655 participant copy numbers remain unspecified unless an actual source version supplies them; no fabricated six-copy annotation.
- Any retained fixed architecture/count has claim-level primary support and explicit preparation/taxon/assembly scope.
- Existing valid adaptor recruitment/turnover evidence and supported core/cofactor roles are preserved; no biological impossibility, universal necessity or new experiment demand inferred.
- Separately authorized record curation uses the native writer and required focused validation/history checks.

### septin-holdfast-A1

Use the source-supported CB15 tax190650 canonical example, or provide directly read evidence for a specified restored/modified NA1000 genotype and restrict its claim accordingly. Keep CB15 experiments separate from the NA1000 HfsK reference sequence. This review PR does not edit the maintained record.

- Canonical taxon, genotype, note and cited experiment agree.
- Do not imply unmodified NA1000 supplies the reported adhesive model merely because its reference genome contains hfsK.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated discussion and curation history; use current-note edits or an appended dated clarification rather than rewriting provenance.
- Do not infer universal formation necessity or require additional experiments from the source-specific observations.

### septin-holdfast-A2

Replace the title with the verified native title while retaining the correct DOI and scientific claims. This review PR does not edit the maintained record.

- Title text matches the native bibliographic record and article header.
- Native schema, strict and CURIE checks pass after separately authorized curation.
- Preserve dated discussion and curation history; use current-note edits or an appended dated clarification rather than rewriting provenance.
- Do not infer universal formation necessity or require additional experiments from the source-specific observations.

### septin-hyphal_tip-A1

Retain the exact supported fungal-tip definition, or add directly relevant evidence and explicit taxon/architecture qualifications for the expanded scope. Preserve the supported Neurospora observations and distinguish prior fungal comparisons. This review PR does not edit the maintained record.

- Do not claim that the lack of an oomycete mention proves biological absence.
- Ensure every retained defining taxon/mechanistic extension is supported by an actually inspected source.
- Preserve supported source-specific claims and pass applicable native gates.
- Preserve dated discussion and curation history; use current-note edits or an appended dated clarification rather than rewriting provenance.
- Do not infer universal formation necessity or require additional experiments from the source-specific observations.

### septin-hyphal_tip-A2

Mark the current graph NONMECHANISTIC and describe its spatial/function scope, or add only directly sourced causal steps if a separate authorized curation establishes them. This review PR does not edit the maintained record.

- Preserve the valid component identities, regional parthood and polarity function.
- Preserve supported source-specific claims and pass applicable native gates.
- Preserve dated discussion and curation history; use current-note edits or an appended dated clarification rather than rewriting provenance.
- Do not infer universal formation necessity or require additional experiments from the source-specific observations.

### septin-ino80_complex-A1

Map Ies1/IPR038014, Ies2/IPR029523, Ies4/IPR062650, Ies5/IPR020366 and Ies6/IPR029525, preserving their correct yeast examples and existing complex/module boundaries. This review PR does not edit the maintained record.

- Retain broader or unresolved other classes as label-only rather than substituting domains or shared paralog families.
- Preserve supported source-specific claims and pass applicable native gates.
- Preserve dated discussion and curation history; use current-note edits or an appended dated clarification rather than rewriting provenance.
- Do not infer universal formation necessity or require additional experiments from the source-specific observations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/hda1_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90; current SHA256 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/hda_beta_clamp_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb; current SHA256 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261022T074157Z-hda-beta-clamp-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/hir_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52; current SHA256 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/holdfast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862; current SHA256 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T074158Z-holdfast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/hops_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f; current SHA256 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T074159Z-hops-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/hsp78_chaperone_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262; current SHA256 ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T074159Z-hsp78-chaperone-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/hyphal_tip.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4; current SHA256 d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T074200Z-hyphal-tip-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/hyphal_tip_polarisome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667; current SHA256 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T074201Z-hyphal-tip-polarisome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/i_aaa_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4d6022b40a8f3933519d560a757641a771e17679d410cca43f010bebe3093a53; current SHA256 f6877406ef9d82f3c18666e77b2ae3bb8c0a8c8c582c35bfba92d7cffafacda9. Changed record reassessed against current sources. |
| original-review-8 | reviews/structured/20261022T074201Z-i-aaa-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/ino80_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4; current SHA256 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T074202Z-ino80-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/hda1_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-0 | reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml; Complete immutable original YAML plus native deterministic Markdown | context_only | Original findings/actions/evidence/verdict and historical source claims independently audited; original access tiers are not retrospectively upgraded. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/0-stale.diff; Exact git diff from original frozen revision to reviewed main | context_only | No record delta; historical target and current main byte-identical. |
| micro-record-1 | data/structures/other/hda_beta_clamp_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-1 | reviews/structured/20261022T074157Z-hda-beta-clamp-complex-audit/review.yaml; Complete immutable original YAML plus native deterministic Markdown | context_only | Original findings/actions/evidence/verdict and historical source claims independently audited; original access tiers are not retrospectively upgraded. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/1-stale.diff; Exact git diff from original frozen revision to reviewed main | context_only | No record delta; historical target and current main byte-identical. |
| micro-record-2 | data/structures/other/hir_complex.yaml; Entire current maintained record at source HEAD | context_only | Every identity, component/example, evidence, function, taxon, graph edge, discussion and history field read. Current bytes equal original frozen target; no stale refresh required. |
| micro-prior-2 | reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml; Complete immutable original YAML plus native deterministic Markdown | context_only | Original findings/actions/evidence/verdict and historical source claims independently audited; original access tiers are not retrospectively upgraded. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/2-stale.diff; Exact git diff from original frozen revision to reviewed main | context_only | No record delta; historical target and current main byte-identical. |
| micro-policy | docs/CURATION.md; Components, evidence and Discussions sections | context_only | Specific class grounding is separate from organism examples; named paralogs are not automatically interchangeable; dated rationale is append-only and current notes can record progress. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum and causal graph slots | context_only | UNKNOWN remains valid when universal formation necessity is not established; a complex can be a structural constituent. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph scopes and evidence contract | context_only | Scoped NONMECHANISTIC graphs need not be full assembly pathways. Function, physical association, localization and universal necessity differ. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Full review and source-native structured applicability workflow | context_only | Positive protein/pathway assertions trigger applicability assessment even without an expression-specific claim. |
| micro-native-config | conf/record_review.yaml; Full configured checks/rubrics | context_only | Current native configuration inspected; this scratch preflight does not certify later root gates. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/original-audit.json; Six actual original native validate/render commands,42 historical input occurrences,six original artifacts | supports | All passed; original pairs render byte-identically and original PR artifacts are immutable. Historical declared inputs match source revisions/hashes. |
| micro-protein-P53973-fresh | https://rest.uniprot.org/uniprotkb/P53973.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P53973-fresh.raw | supports | P53973: UniProtKB reviewed (Swiss-Prot); Histone deacetylase HDA1; taxon 559292; gene fields [{'geneName': {'value': 'HDA1'}, 'orderedLocusNames': [{'value': 'YNL021W'}], 'orfNames': [{'value': 'N2819'}]}]; InterPro references ['IPR019154', 'IPR000286', 'IPR023801', 'IPR037138', 'IPR017321', 'IPR023696']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-Q06629-fresh | https://rest.uniprot.org/uniprotkb/Q06629.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-Q06629-fresh.raw | supports | Q06629: UniProtKB reviewed (Swiss-Prot); HDA1 complex subunit 2; taxon 559292; gene fields [{'geneName': {'value': 'HDA2'}, 'synonyms': [{'value': 'PLO2'}], 'orderedLocusNames': [{'value': 'YDR295C'}]}]; InterPro references ['IPR038609', 'IPR021006']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-Q06623-fresh | https://rest.uniprot.org/uniprotkb/Q06623.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-Q06623-fresh.raw | supports | Q06623: UniProtKB reviewed (Swiss-Prot); HDA1 complex subunit 3; taxon 559292; gene fields [{'geneName': {'value': 'HDA3'}, 'synonyms': [{'value': 'PLO1'}], 'orderedLocusNames': [{'value': 'YPR179C'}]}]; InterPro references ['IPR038609', 'IPR021006', 'IPR026216']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-P69931-fresh | https://rest.uniprot.org/uniprotkb/P69931.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P69931-fresh.raw | supports | P69931: UniProtKB reviewed (Swiss-Prot); DnaA regulatory inactivator Hda; taxon 83333; gene fields [{'geneName': {'value': 'hda'}, 'synonyms': [{'value': 'idaB'}, {'value': 'yfgE'}], 'orderedLocusNames': [{'value': 'b2496'}, {'value': 'JW5397'}], 'orfNames': [{'value': 'f248c'}]}]; InterPro references ['IPR020591', 'IPR013317', 'IPR017788', 'IPR022864', 'IPR055199', 'IPR027417']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-P0A988-fresh | https://rest.uniprot.org/uniprotkb/P0A988.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P0A988-fresh.raw | supports | P0A988: UniProtKB reviewed (Swiss-Prot); Beta sliding clamp; taxon 83333; gene fields [{'geneName': {'value': 'dnaN'}, 'orderedLocusNames': [{'value': 'b3701'}, {'value': 'JW3678'}]}]; InterPro references ['IPR046938', 'IPR001001', 'IPR022635', 'IPR022637', 'IPR022634']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-P32479-fresh | https://rest.uniprot.org/uniprotkb/P32479.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P32479-fresh.raw | supports | P32479: UniProtKB reviewed (Swiss-Prot); Protein HIR1; taxon 559292; gene fields [{'geneName': {'value': 'HIR1'}, 'orderedLocusNames': [{'value': 'YBL008W'}], 'orfNames': [{'value': 'YBL0318'}]}]; InterPro references ['IPR055410', 'IPR031120', 'IPR011494', 'IPR019015', 'IPR015943', 'IPR036322', 'IPR001680']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-P32480-fresh | https://rest.uniprot.org/uniprotkb/P32480.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P32480-fresh.raw | supports | P32480: UniProtKB reviewed (Swiss-Prot); Protein HIR2; taxon 559292; gene fields [{'geneName': {'value': 'HIR2'}, 'orderedLocusNames': [{'value': 'YOR038C'}], 'orfNames': [{'value': 'OR26.31'}]}]; InterPro references ['IPR031120', 'IPR011494', 'IPR015943', 'IPR036322']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-P47171-fresh | https://rest.uniprot.org/uniprotkb/P47171.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P47171-fresh.raw | supports | P47171: UniProtKB reviewed (Swiss-Prot); Histone transcription regulator 3; taxon 559292; gene fields [{'geneName': {'value': 'HIR3'}, 'synonyms': [{'value': 'HPC1'}], 'orderedLocusNames': [{'value': 'YJR140C'}], 'orfNames': [{'value': 'J2161'}]}]; InterPro references ['IPR060091', 'IPR033053', 'IPR060094', 'IPR060090', 'IPR060092', 'IPR063734']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-protein-Q01448-fresh | https://rest.uniprot.org/uniprotkb/Q01448.json; Current status/name, entire primary/synonym/ordered-locus gene fields, organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-Q01448-fresh.raw | supports | Q01448: UniProtKB reviewed (Swiss-Prot); Histone promoter control protein 2; taxon 559292; gene fields [{'geneName': {'value': 'HPC2'}, 'orderedLocusNames': [{'value': 'YBR215W'}], 'orfNames': [{'value': 'YBR1503'}]}]; InterPro references ['IPR014840']. Native localization/citation annotations are distinguished from independently read primary body evidence and actual experimental strains. |
| micro-query-HDA1-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HDA1-fresh.raw | supports | One current reviewed result ['P53973']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-HDA2-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HDA2-fresh.raw | supports | One current reviewed result ['Q06629']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-HDA3-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HDA3-fresh.raw | supports | One current reviewed result ['Q06623']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-HIR1-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HIR1-fresh.raw | supports | One current reviewed result ['P32479']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-HIR2-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HIR2-fresh.raw | supports | One current reviewed result ['P32480']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-HIR3-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HIR3-fresh.raw | supports | One current reviewed result ['P47171']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-HPC2-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHPC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HPC2-fresh.raw | supports | One current reviewed result ['Q01448']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-dnaN-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-dnaN-fresh.raw | supports | One current reviewed result ['P0A988']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-query-hda-fresh | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete exact reviewed gene/taxon query, single returned page, total-result and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-hda-fresh.raw | supports | One current reviewed result ['P69931']; all native gene/alias/locus fields inspected and no next page. This reproduces a bounded current query, not the historic selection execution. |
| micro-tax-4932-fresh | https://rest.uniprot.org/taxonomy/4932.json; Native active taxon name/rank/parent and reference-strain scope; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-4932-fresh.raw | supports | 4932: Saccharomyces cerevisiae; active True; rank species. Yeast species versus S288C and E.coli species versus K-12 remain distinct from experiment preparations. |
| micro-tax-559292-fresh | https://rest.uniprot.org/taxonomy/559292.json; Native active taxon name/rank/parent and reference-strain scope; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-559292-fresh.raw | supports | 559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c); active True; rank strain. Yeast species versus S288C and E.coli species versus K-12 remain distinct from experiment preparations. |
| micro-tax-562-fresh | https://rest.uniprot.org/taxonomy/562.json; Native active taxon name/rank/parent and reference-strain scope; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-562-fresh.raw | supports | 562: Escherichia coli; active True; rank species. Yeast species versus S288C and E.coli species versus K-12 remain distinct from experiment preparations. |
| micro-tax-83333-fresh | https://rest.uniprot.org/taxonomy/83333.json; Native active taxon name/rank/parent and reference-strain scope; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-83333-fresh.raw | supports | 83333: Escherichia coli (strain K12); active True; rank strain. Yeast species versus S288C and E.coli species versus K-12 remain distinct from experiment preparations. |
| micro-ena-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-4932.raw | supports | Independent issuing taxonomy response corroborates exact named species/reference taxon. No experimental-strain identity follows from this authority alone. |
| micro-ena-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-559292.raw | supports | Independent issuing taxonomy response corroborates exact named species/reference taxon. No experimental-strain identity follows from this authority alone. |
| micro-ena-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-562.raw | supports | Independent issuing taxonomy response corroborates exact named species/reference taxon. No experimental-strain identity follows from this authority alone. |
| micro-ena-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-83333.raw | supports | Independent issuing taxonomy response corroborates exact named species/reference taxon. No experimental-strain identity follows from this authority alone. |
| micro-go-0000118-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000118; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0000118-fresh.raw | supports | GO:0000118: histone deacetylase complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0000417-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000417; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0000417-fresh.raw | supports | GO:0000417: HIR complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0000785-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000785; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0000785-fresh.raw | supports | GO:0000785: chromatin; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0004407-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0004407; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0004407-fresh.raw | supports | GO:0004407: histone deacetylase activity; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0006334-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006334; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0006334-fresh.raw | supports | GO:0006334: nucleosome assembly; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0032297 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032297; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0032297.raw | supports | GO:0032297: negative regulation of DNA-templated DNA replication initiation; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0032991-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032991; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0032991-fresh.raw | supports | GO:0032991: protein-containing complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0044775-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044775; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0044775-fresh.raw | supports | GO:0044775: DNA polymerase III, beta sliding clamp processivity factor complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-0070823-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0070823; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0070823-fresh.raw | supports | GO:0070823: HDA1 complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-1990078-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990078; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-1990078-fresh.raw | supports | GO:1990078: replication inhibiting complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-1990083-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-1990083-fresh.raw | supports | GO:1990083: DnaA-Hda complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-go-1990085-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990085; Exact term ID/name/active state, definition, relationships and synonyms; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-1990085-fresh.raw | supports | GO:1990085: Hda-beta clamp complex; isObsolete=False. Current identity and stated scope checked; GO definition is authority synthesis, not a new experiment. |
| micro-ancestors-0000417-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000417/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ancestors-0000417-fresh.raw | supports | GO:0000417: ['GO:0000417', 'GO:0032991', 'GO:0005575']. Declared parent verified; parthood is assessed separately. |
| micro-ancestors-0070823-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0070823/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ancestors-0070823-fresh.raw | supports | GO:0070823: ['GO:1902494', 'GO:0140513', 'GO:0000118', 'GO:0032991', 'GO:0070823', 'GO:0005575']. Declared parent verified; parthood is assessed separately. |
| micro-ancestors-1990085-fresh | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990085/ancestors?relations=is_a; Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ancestors-1990085-fresh.raw | supports | GO:1990085: ['GO:1990078', 'GO:0032991', 'GO:1990085', 'GO:0005575']. Declared parent verified; parthood is assessed separately. |
| micro-family-IPR017321-fresh | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017321/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR017321-fresh.raw | supports | IPR017321: Histone deacetylase class II, yeast; native type family. Exact constituent family corroborated by current reference-protein native xrefs. Domain prose is not used as primary experiment evidence. |
| micro-family-IPR026216-fresh | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026216/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR026216-fresh.raw | supports | IPR026216: HDA1 complex subunit 3; native type family. Exact constituent family corroborated by current reference-protein native xrefs. Domain prose is not used as primary experiment evidence. |
| micro-family-IPR017788-fresh | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR017788-fresh.raw | supports | IPR017788: DnaA regulatory inactivator Hda; native type family. Exact Hda branch, distinct from DnaA sibling under the broader DnaA-like family. |
| micro-family-IPR022864-fresh | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR022864-fresh.raw | supports | IPR022864: DnaA regulatory inactivator Hda, Enterobacteriaceae; native type family. Enterobacteriaceae child of Hda; useful narrower reference context, not mandatory scope for the whole Hda class. |
| micro-family-IPR033053-fresh | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033053/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR033053-fresh.raw | supports | IPR033053: Histone transcription regulator 3/CABIN1; native type family. Whole Hir3/CABIN1 homolog family spans fungal Hir3 and animal CABIN1; breadth is explicit, not a claim of identical HIR composition in all taxa. |
| micro-family-IPR021006 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021006/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR021006.raw | supports | IPR021006: HDA1 complex subunit 2/3; native type family. Shared Hda2/3 family, with specific Hda3 child IPR026216; not an exact Hda2-only mapping. |
| micro-family-IPR000286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000286/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR000286.raw | supports | IPR000286: Histone deacetylase HDAC; native type family. Broad deacetylase entry; not substituted for the yeast Hda1-specific class. Broad descriptive substrate claims do not replace direct Wu/Carmen assay scope. |
| micro-family-IPR031120 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031120/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR031120.raw | supports | IPR031120: WD repeat HIR1-like; native type family. Includes yeast Hir1/Hir2 and animal HIRA; not treated as a uniquely Hir1-only or Hir2-only class. |
| micro-family-IPR014840 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014840/; Complete metadata/type/name, native description, integrated signatures and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR014840.raw | supports | IPR014840: Hpc2-related domain; native type domain. Hpc2-related domain, not a verified whole Hpc2 protein family. |
| micro-doi-0-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.081560698%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-0-fresh.raw | context_only | HDA2 and HDA3 are related proteins that interact with and are essential for the activity of the yeast histone deacetylase HDA1.; PMID11287668, DOI10.1073/pnas.081560698; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-doi-1-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.271.26.15837%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-1-fresh.raw | context_only | HDA1 and HDA3 are components of a yeast histone deacetylase (HDA) complex.; PMID8663039, DOI10.1074/jbc.271.26.15837; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-doi-3-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2005.10.053%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-3-fresh.raw | context_only | Replication-independent histone deposition by the HIR complex and Asf1.; PMID16303565, DOI10.1016/j.cub.2005.10.053; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-doi-4-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00412-006-0087-z%22&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-4-fresh.raw | context_only | The histone chaperone Asf1 at the crossroads of chromatin and DNA checkpoint pathways.; PMID17180700, DOI10.1007/s00412-006-0087-z; underlying secondary review. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-11287668-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11287668+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-11287668-fresh.raw | context_only | HDA2 and HDA3 are related proteins that interact with and are essential for the activity of the yeast histone deacetylase HDA1.; PMID11287668, DOI10.1073/pnas.081560698; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-11782447 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11782447+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-11782447.raw | context_only | Chromatin assembly factor I and Hir proteins contribute to building functional kinetochores in S. cerevisiae.; PMID11782447, DOI10.1101/gad.925302; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-12618445 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12618445+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-12618445.raw | context_only | Identification of a novel membrane-associated gene product that suppresses toxicity of a TrfA peptide from plasmid RK2 and its relationship to the DnaA host initiation protein.; PMID12618445, DOI10.1128/jb.185.6.1817-1824.2003; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-14562095.raw | context_only | Global analysis of protein localization in budding yeast.; PMID14562095, DOI10.1038/nature02026; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-15150238-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15150238+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-15150238-fresh.raw | context_only | Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related protein.; PMID15150238, DOI10.1128/jb.186.11.3508-3515.2004; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-16303565-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16303565+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-16303565-fresh.raw | context_only | Replication-independent histone deposition by the HIR complex and Asf1.; PMID16303565, DOI10.1016/j.cub.2005.10.053; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-17180700-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17180700+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-17180700-fresh.raw | context_only | The histone chaperone Asf1 at the crossroads of chromatin and DNA checkpoint pathways.; PMID17180700, DOI10.1007/s00412-006-0087-z; underlying secondary review. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-19683497 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19683497+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-19683497.raw | context_only | Two-color cell array screen reveals interdependent roles for histone chaperones and a chromatin boundary regulator in histone gene repression.; PMID19683497, DOI10.1016/j.molcel.2009.06.023; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-23994470 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23994470+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-23994470.raw | context_only | A replicase clamp-binding dynamin-like protein promotes colocalization of nascent DNA strands and equipartitioning of chromosomes in E. coli.; PMID23994470, DOI10.1016/j.celrep.2013.07.040; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-8417331 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8417331+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-8417331.raw | context_only | Characterization of HIR1 and HIR2, two genes required for regulation of histone gene transcription in Saccharomyces cerevisiae.; PMID8417331, DOI10.1128/mcb.13.1.28-38.1993; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-8663039-fresh | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663039+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-8663039-fresh.raw | context_only | HDA1 and HDA3 are components of a yeast histone deacetylase (HDA) complex.; PMID8663039, DOI10.1074/jbc.271.26.15837; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-pmid-9671488 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9671488+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Exact PMID/DOI metadata, authors/year/article type and complete indexed abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-9671488.raw | context_only | Yeast Ty1 retrotransposition is stimulated by a synergistic interaction between mutations in chromatin assembly factor I and histone regulatory proteins.; PMID9671488, DOI10.1128/mcb.18.8.4783; underlying primary article. Only indexed metadata/abstract read here; primary body access is separately specified. Localization provenance references do not independently establish membership. |
| micro-carmen-doi | https://doi.org/10.1074/jbc.271.26.15837; Current DOI content-negotiated Crossref metadata, title/PII and publisher resource links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/carmen-doi.raw | context_only | Genuine bibliographic metadata only; not Carmen1996 body. Historical DOI redirect and publisher403 remain distinct old observations. |
| micro-PMC31845-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC31845/?pdf=0; Genuine PMC HTML; complete Methods sec1–8 including Table1; Results/Discussion sec9–17, all Figures1–6 text captions; no pixels/supplements; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/PMC31845-legacy.raw | supports | Wu2001 directly supports Hda1 self-association, Hda2/Hda3 association and native Hda1-containing complex in YDS/WJY yeast preparations. Hydrodynamic299.2kDa estimate supports likely2:1:1 tetramer, not resolved atomic stoichiometry. Co-IP partner losses, activity loss, and ENA1-specific H3/H2B ChIP effects are separate observations; no universal histone/locus preference or formation-essentiality inferred. |
| micro-PMC415757-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC415757/?pdf=0; Genuine PMC HTML; complete Methods sec1–10 including Table2; Results sec11–16 with all Figures1–3/Table1; Discussion sec17; no pixels; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/PMC415757-legacy.raw | supports | Kurz2004 demonstrates purified Hda-beta binding by plate and pull-down assays, motif-dependent binding and peptide competition. XL1Blue-derived amplified genes and BL21(DE3)pLyS/TB1 expression/preparations are distinguished from reference K-12 annotation. The paper proposes RIDA relevance and cites prior ATP-hydrolysis studies; it does not newly measure the whole RIDA reaction. Mutant misfolding remains an explicit alternative. |
| micro-PMC2819815-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC2819815/?pdf=0; Genuine PMC HTML; complete Results/Discussion S2–S6, Figures1–4 captions and main Experimental Procedures S7 pointer; no supplemental protocols/strain tables/pixels; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/PMC2819815-legacy.raw | supports | Green2005 purified Hir2-STAP complex identifies Hir1/Hir2/Hir3/Hpc2; Asf1 is a cooperating partner. Conditional deletion/purification observations, promoter binding and in-vitro nucleosome assembly are distinguished. HIR alone can support histone deposition under tested conditions; efficient cooperation is not obligatory Asf1 membership. Hir3 loss from hpc2-deletion preparation does not distinguish failed association from protein instability. |
| micro-historical-0-access-panther-PTHR31882-SF11 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR31882:SF11/; Retained immutable original evidence access-panther-PTHR31882-SF11 at reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml; historical status/diagnostic scope only | context_only | The candidate subfamily identified by Q06629 returned HTTP204 with an empty body; this route did not independently resolve its class boundary. Historical observation retained without fresh invocation or body-access upgrade; original primary_source kind is corrected to validation/context_only. |
| micro-historical-0-access-carmen1996-doi | https://doi.org/10.1074/jbc.271.26.15837; Retained immutable original evidence access-carmen1996-doi at reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml; historical status/diagnostic scope only | context_only | The DOI resolved to an Elsevier redirect page naming the correct title and PII, without article body text. Historical observation retained without fresh invocation or body-access upgrade; original primary_source kind is corrected to validation/context_only. |
| micro-historical-0-access-carmen1996-jbc | https://www.jbc.org/article/S0021-9258(18)36134-9/fulltext; Retained immutable original evidence access-carmen1996-jbc at reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml; historical status/diagnostic scope only | context_only | The publisher article route derived from the DOI PII returned HTTP403. Carmen1996 remains verified at native complete-abstract tier. Historical observation retained without fresh invocation or body-access upgrade; original primary_source kind is corrected to validation/context_only. |
| micro-historical-2-access-panther-PTHR13831-SF0 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF0/; Retained immutable original evidence access-panther-PTHR13831-SF0 at reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml; historical status/diagnostic scope only | context_only | The reference-protein-linked candidate subfamily route returned HTTP204 and no response body; this route does not independently resolve an exact Hir1/Hir2 class boundary. Historical observation retained without fresh invocation or body-access upgrade; original primary_source kind is corrected to validation/context_only. |
| micro-historical-2-access-panther-PTHR13831-SF1 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF1/; Retained immutable original evidence access-panther-PTHR13831-SF1 at reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml; historical status/diagnostic scope only | context_only | The reference-protein-linked candidate subfamily route returned HTTP204 and no response body; this route does not independently resolve an exact Hir1/Hir2 class boundary. Historical observation retained without fresh invocation or body-access upgrade; original primary_source kind is corrected to validation/context_only. |
| micro-access-PMC31845-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC31845.1/PMC31845.1.xml; Actual failed candidate S3 route and diagnostic body | context_only | HTTP404; no primary body at this route. Genuine later PMC HTML is separately read and does not retroactively upgrade this failure. |
| micro-access-PMC415757-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC415757.1/PMC415757.1.xml; Actual failed candidate S3 route and diagnostic body | context_only | HTTP404; no primary body at this route. Genuine later PMC HTML is separately read and does not retroactively upgrade this failure. |
| micro-access-PMC2819815-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2819815.1/PMC2819815.1.xml; Actual failed candidate S3 route and diagnostic body | context_only | HTTP404; no primary body at this route. Genuine later PMC HTML is separately read and does not retroactively upgrade this failure. |
| micro-adapter-catalogue-fresh | https://imodulondb.org/api/organisms; Complete official organism/dataset catalogue; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-catalogue-fresh.raw | context_only | Complete20 organism rows and28 organism/dataset pairs inspected. No Saccharomyces host; no yeast proxy query. E.coli is represented and the actual precise1k packet is assessed for the Hda-beta narrative. |
| micro-adapter-precise1k-meta-fresh | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Full selected e_coli/precise1k metadata; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-precise1k-meta-fresh.raw | context_only | Dataset has201 modules,4257 genes,1035 samples/518 conditions and five strains BW25113,DGF-298,GMOS,MG1655,W3110. This is a multistrain expression dataset, not the Kurz assay preparations or all E.coli. |
| micro-adapter-precise1k-genes-fresh | https://imodulondb.org/api/genes?organism=e_coli&amp;dataset=precise1k&amp;limit=5000; Full4257-row table; exact hda/b2496 and dnaN/b3701 symbols/loci/UniProt joins; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-precise1k-genes-fresh.raw | context_only | Exact two rows map hda/b2496 to P69931 and dnaN/b3701 to P0A988; reference mapping is distinguished from primary experiment background. No substring/foreign-host substitution. |
| micro-adapter-precise1k-modules-fresh | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete201-module listing and metadata; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-precise1k-modules-fresh.raw | context_only | Used to bound the returned memberships and module population; AI-generated narrative summaries and activity vectors are not biological evidence here. |
| micro-adapter-membership-b2496 | https://imodulondb.org/api/genes/b2496/imodulons?organism=e_coli&amp;dataset=precise1k; Complete201 returned gene-module membership rows, in_imodulon flags and weight/threshold fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-membership-b2496.raw | context_only | b2496: zero thresholded memberships among201 returned modules. No above-threshold module warrants member-level source interpretation. Zero membership is neither gene/protein absence nor physical-complex/causal evidence. |
| micro-adapter-membership-b3701 | https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&amp;dataset=precise1k; Complete201 returned gene-module membership rows, in_imodulon flags and weight/threshold fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-membership-b3701.raw | context_only | b3701: zero thresholded memberships among201 returned modules. No above-threshold module warrants member-level source interpretation. Zero membership is neither gene/protein absence nor physical-complex/causal evidence. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner attempt2026-11-03T00:49:00.848907–00:49:00.863225Z only | context_only | Retained PermissionError pyvenv.cfg is historical; no fresh runner invocation. Current official catalogue/dataset fallbacks have their own actual timestamps and scope. |
| micro-native-hda1_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --verify; Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-verify.log; exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-verify-receipt.json SHA256 fe27fd8c8d07e679836b04a20666d343d3f443b0da58761fe55df74f3916c191 | supports | Three reviewed S288C examples and three COVERED typed nodes. Native exit0 is identity/coverage validation, not experimental membership or assembly proof. |
| micro-native-hda1_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml --causal-graphs; Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-causal.log; exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-causal-receipt.json SHA256 c4f1ba724243bd76fa8dc96c2be79afcdb6f88d38fc70c5ce9de315592652f8b | supports | Three reviewed S288C examples and three COVERED typed nodes. Native exit0 is identity/coverage validation, not experimental membership or assembly proof. |
| micro-native-hda_beta_clamp_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml --verify; Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-verify.log; exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-verify-receipt.json SHA256 134ff93b95ddefb6bd6346016152d6e15e15c47611c7fd84be1f87696d04ded7 | supports | Two reviewed K-12 examples and one COVERED typed Hda node; DnaN is a STRUCTURE node, not a second typed protein node. Native exit0 is identity/coverage validation, not experimental membership or assembly proof. |
| micro-native-hda_beta_clamp_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml --causal-graphs; Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-causal.log; exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-causal-receipt.json SHA256 2a65f2d110a0e87a8a2085b5ec96c14a5a5f8f81624590e8e995691aa1016308 | supports | Two reviewed K-12 examples and one COVERED typed Hda node; DnaN is a STRUCTURE node, not a second typed protein node. Native exit0 is identity/coverage validation, not experimental membership or assembly proof. |
| micro-native-hir_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --verify; Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-verify.log; exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-verify-receipt.json SHA256 9259920f9533e69b943ec86ac5add0315b305f6b261fb0bbf48ae6587a119518 | supports | Four reviewed S288C examples and four COVERED typed nodes. Native exit0 is identity/coverage validation, not experimental membership or assembly proof. |
| micro-native-hir_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --causal-graphs; Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-causal.log; exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-causal-receipt.json SHA256 e6281fe449aa49aedef70e8386aaf925c15ca23d7d4f2bdaeaa8515f3f5ba45f | supports | Four reviewed S288C examples and four COVERED typed nodes. Native exit0 is identity/coverage validation, not experimental membership or assembly proof. |
| plaque-t4-record | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/other/hops_complex.yaml; Entire current record, all assertions, components, examples, graphs, datasets/images, discussions and curation history. | context_only | Complete current HOPS complex record at source f5668d26c554ec2f62610183aed5c5bc3aa76826; no record mutation. |
| plaque-t4-original | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261022T074159Z-hops-complex-audit/review.yaml; Entire original native YAML and canonical derived Markdown; exact historical input verification in original-proof.json. | context_only | Original review 20261022T074159Z-hops-complex-audit: findings, actions, evidence tiers, checks and verdict independently reassessed; immutable historical observation. |
| plaque-t5-record | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/other/hsp78_chaperone_complex.yaml; Entire current record, all assertions, components, examples, graphs, datasets/images, discussions and curation history. | context_only | Complete current Hsp78 chaperone complex record at source f5668d26c554ec2f62610183aed5c5bc3aa76826; no record mutation. |
| plaque-t5-original | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261022T074159Z-hsp78-chaperone-complex-audit/review.yaml; Entire original native YAML and canonical derived Markdown; exact historical input verification in original-proof.json. | context_only | Original review 20261022T074159Z-hsp78-chaperone-complex-audit: findings, actions, evidence tiers, checks and verdict independently reassessed; immutable historical observation. |
| plaque-t8-record | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/other/i_aaa_complex.yaml; Entire current record, all assertions, components, examples, graphs, datasets/images, discussions and curation history. | context_only | Complete current i-AAA complex record at source f5668d26c554ec2f62610183aed5c5bc3aa76826; no record mutation. |
| plaque-t8-original | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261022T074201Z-i-aaa-complex-audit/review.yaml; Entire original native YAML and canonical derived Markdown; exact historical input verification in original-proof.json. | context_only | Original review 20261022T074201Z-i-aaa-complex-audit: findings, actions, evidence tiers, checks and verdict independently reassessed; immutable historical observation. |
| plaque-curation | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/docs/CURATION.md; Identity, source-neutral classes, reviewed-label-only semantics, verbatim snippet, separate taxon-specific complex compositions and append-only history/discussion policy. | context_only | Frozen repository guidance used only as review authority, not independent biological evidence. |
| plaque-schema | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/src/cellstructuremech/schema/cellstructuremech.yaml; Components, protein examples, graph nodes/edges, chemical identity, essentiality and image/dataset fields. | context_only | Frozen repository guidance used only as review authority, not independent biological evidence. |
| plaque-profile | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/docs/record-review-profile.md; Scientific claim-level review and structured-source applicability from positive protein/pathway/stress assertions. | context_only | Frozen repository guidance used only as review authority, not independent biological evidence. |
| plaque-review-skill | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/review-yaml-record/SKILL.md; Read-only scientific review, source/input freezing, bounded searches, native artifact lifecycle. | context_only | Frozen repository guidance used only as review authority, not independent biological evidence. |
| plaque-protein-skill | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/uniprot-protein-examples/SKILL.md; Exact gene identities, native accession status/taxa, external actor xrefs and limits of deterministic coverage. | context_only | Frozen repository guidance used only as review authority, not independent biological evidence. |
| plaque-graph-skill | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/curate-causal-graphs/SKILL.md; Identity and evidence for directed relationships; association/function distinct from physical formation. | context_only | Frozen repository guidance used only as review authority, not independent biological evidence. |
| plaque-go-0030897 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030897; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0030897.receipt.json SHA256 1645a83548eac7b39ea99f105e3bf6ed1d13e5f91283f665ff9e7d033fe180ff. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0098796 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098796; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0098796.receipt.json SHA256 147fb20f001434e9c07e7cc5dc925f07ffa3fbf2e6d971398299225b917a0950. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0042144 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042144; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0042144.receipt.json SHA256 1faa5abb8a913fbf35cd0dd399649e4837eb5af41cfdb79352206a2714cbd2d9. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0000329 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0000329.receipt.json SHA256 46b8a59671c07780b2394b2c0b1c15191cb2f71dec889a4f19d91c8610d2420f. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0101031 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0101031; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0101031.receipt.json SHA256 e3e5d48f7ca4b68ceac2145e24dd7d86c9f3fffabcc3b16bb5e364e1bb01b0d9. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0005759 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005759; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0005759.receipt.json SHA256 805729c31900a37e58cbe09f242bda867c5afb3ddcd529ce94b576ff7665e24d. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0140545 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140545; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0140545.receipt.json SHA256 cb485d00600adbe55ec5792809cb8fe77cd7e8d31d9a4eb3d06dbf8fe8d4917d. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0016887 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016887; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0016887.receipt.json SHA256 1614d68be27c0f260f4d45b445ed5367d37581f52aa4016931757f227a12bc86. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0031942 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031942; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0031942.receipt.json SHA256 d2b37cd7e0d99a540791eddcdc3b31c1e34ce519392fe3cd9e09933bfea3a266. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0098800 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098800; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0098800.receipt.json SHA256 5a0c862d6deb061da397bf02685f7f253bb52792e5fffc86d897e3ba9b22bdb4. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0005743 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005743; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0005743.receipt.json SHA256 a4f5e16599c10f22b3c55b14c58ea5409cdcf4b66a265b5313921203aee0131e. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-go-0004176 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176; Exact term identity, definition, synonyms and typed child relationships in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0004176.receipt.json SHA256 a631ea1528f29e270e1caee01768156818eef6e6df71a5a07b2f34e9dd101aa3. | supports | Current native GO term supports the specifically associated structure, broader class, location or function; typed relations are not interchanged and do not prove taxonomic prevalence. |
| plaque-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete exact ENA taxon identity, rank, names and lineage. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/tax-4932.receipt.json SHA256 de6128306d9f7caa1ca6c1639b8316bbf35c43632fb41ae6796ebf046634c9b3. | supports | Saccharomyces cerevisiae species 4932 and S288C reference strain 559292 are distinct; reference sequence taxon is not substituted for experimental strain backgrounds. |
| plaque-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete exact ENA taxon identity, rank, names and lineage. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/tax-559292.receipt.json SHA256 0e4c5f5f547a3737019c79b36dd9d2a773f8fb385b2525bbb688f85baf7f6466. | supports | Saccharomyces cerevisiae species 4932 and S288C reference strain 559292 are distinct; reference sequence taxon is not substituted for experimental strain backgrounds. |
| plaque-up-P12868 | https://rest.uniprot.org/uniprotkb/P12868.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P12868.receipt.json SHA256 7a07a74bd818e2d5a795be3217d78e0bac90c2c7ccf456a65d529213fee33839. | supports | Reviewed S288C P12868 independently matches Vps11/PEP5/YMR231W. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-Q03308 | https://rest.uniprot.org/uniprotkb/Q03308.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-Q03308.receipt.json SHA256 acfa27195b39d9d702f063d56be347a9b17148e6ac36da488a089a223a0d8ac5. | supports | Reviewed S288C Q03308 independently matches VPS16/YPL045W. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P27801 | https://rest.uniprot.org/uniprotkb/P27801.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P27801.receipt.json SHA256 2e05ba8b5ef74f99927896cfea1c68d83c508ddc008c3dbd8b4c016e117ad741. | supports | Reviewed S288C P27801 independently matches Vps18/PEP3/YLR148W. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P20795 | https://rest.uniprot.org/uniprotkb/P20795.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P20795.receipt.json SHA256 d3d5f319f2ae19dd5f5e8ce5dc762d68c751733079723d7879d12b3c1f3cb5e9. | supports | Reviewed S288C P20795 independently matches VPS33/YLR396C. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-Q07468 | https://rest.uniprot.org/uniprotkb/Q07468.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-Q07468.receipt.json SHA256 2cdac555850f4d1c94ad74d8f1e20c3af6cb557c2a40675e239bbfdda279eed3. | supports | Reviewed S288C Q07468 independently matches Vps39/VAM6/YDL077C. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P38959 | https://rest.uniprot.org/uniprotkb/P38959.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P38959.receipt.json SHA256 fcb7202d1984a7e5150be2db7a7e7f0466e24df2ae69d80f78752dd08e9e8f7f. | supports | Reviewed S288C P38959 independently matches VPS41/YDR080W. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P32939 | https://rest.uniprot.org/uniprotkb/P32939.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P32939.receipt.json SHA256 e21af0a6f0c6d293747a996586e892dc10e82098f9582bc84910d8f5440b7237. | supports | Reviewed S288C P32939 independently matches YPT7/YML001W. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P33416 | https://rest.uniprot.org/uniprotkb/P33416.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P33416.receipt.json SHA256 93f32df3a5a58c3f0ed6a562663125de0cf00122702f5d9a606f144fdb480c71. | supports | Reviewed S288C P33416 independently matches HSP78/YDR258C/YD9320A.08C. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P32795 | https://rest.uniprot.org/uniprotkb/P32795.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P32795.receipt.json SHA256 cd9f926d16309df7e4714f9f59f97638bc34dd12592c2c09e25abf1339568855. | supports | Reviewed S288C P32795 independently matches YME1/YPR024W; OSD1/YTA11 aliases. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-P25573 | https://rest.uniprot.org/uniprotkb/P25573.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P25573.receipt.json SHA256 94ede4c273a34120998091b1b3d44452f3c53ccf736c9c5ddbe2ff62d3d90c81. | supports | Reviewed S288C P25573 independently matches MGR1/YCL044C. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-up-Q04472 | https://rest.uniprot.org/uniprotkb/Q04472.json; Primary accession, entryType, full gene/locus tokens, organism/taxon and FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-Q04472.receipt.json SHA256 ce6c4a37a09a1dd2960ec2ac44669d5db0932c964319e7aaec9174588036de87. | supports | Reviewed S288C Q04472 independently matches MGR3/YMR115W; FMP24 alias. Native comments are annotation context, not a claim that every cited experiment was read. Ypt7 remains an external Rab actor; reference identity does not independently prove assembly membership. |
| plaque-query-FMP24 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AFMP24%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-FMP24.receipt.json SHA256 ee0ec2b114c26d06391350fd35d394a8ba2f999297db949f852b1138a591fe09. | supports | Exact reviewed S288C gene query for FMP24 returns one entry, Q04472; actual tokens match the named primary gene or synonym. |
| plaque-query-HSP78 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHSP78%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-HSP78.receipt.json SHA256 b78434337ada49df83e28ecbf411c612034f63a51dc88ad95979813fce263234. | supports | Exact reviewed S288C gene query for HSP78 returns one entry, P33416; actual tokens match the named primary gene or synonym. |
| plaque-query-MGR1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMGR1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-MGR1.receipt.json SHA256 67acee776f8212e1adb668138c8dc94ac3f5d42b8d1868bc46ad3ce019d0c0ca. | supports | Exact reviewed S288C gene query for MGR1 returns one entry, P25573; actual tokens match the named primary gene or synonym. |
| plaque-query-MGR3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMGR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-MGR3.receipt.json SHA256 e306dc8d0d89557b683bac4a596693adc39227abdf33460dbe8ce2bbbbe1075d. | supports | Exact reviewed S288C gene query for MGR3 returns one entry, Q04472; actual tokens match the named primary gene or synonym. |
| plaque-query-OSD1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AOSD1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-OSD1.receipt.json SHA256 ec91d2fe36fdf02b61c9bd4422f33226faac4883404aa9fa9038c4aa588f4222. | supports | Exact reviewed S288C gene query for OSD1 returns one entry, P32795; actual tokens match the named primary gene or synonym. |
| plaque-query-PEP3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-PEP3.receipt.json SHA256 d5be816ef2bc1c2592eb4c5c5c4fa4d5f091999d1c257d3cc86c04aa93277046. | supports | Exact reviewed S288C gene query for PEP3 returns one entry, P27801; actual tokens match the named primary gene or synonym. |
| plaque-query-PEP5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEP5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-PEP5.receipt.json SHA256 4ae36637e5b6db1c577e49532f9130177e04e1c2bb0f96644c5d36ec09eabc9c. | supports | Exact reviewed S288C gene query for PEP5 returns one entry, P12868; actual tokens match the named primary gene or synonym. |
| plaque-query-VAM2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVAM2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VAM2.receipt.json SHA256 321629c5bcd4a5d4d3f65a5c6a0e603387311ce53cbef6f7bd4fc40f491123a2. | supports | Exact reviewed S288C gene query for VAM2 returns one entry, P38959; actual tokens match the named primary gene or synonym. |
| plaque-query-VAM6 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVAM6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VAM6.receipt.json SHA256 2b50c30a9fb8d194c79edab6c7a25a6871212837ef6a3e80a977fd01bfd1a1e3. | supports | Exact reviewed S288C gene query for VAM6 returns one entry, Q07468; actual tokens match the named primary gene or synonym. |
| plaque-query-VPS11 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS11.receipt.json SHA256 6961403e6b70149c83b81407cd2caa1d9aff48662d765aa52705aa1ba8f7d4f3. | supports | Exact reviewed S288C gene query for VPS11 returns one entry, P12868; actual tokens match the named primary gene or synonym. |
| plaque-query-VPS16 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS16%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS16.receipt.json SHA256 ce36f2fe3e79d5060cc030b1e602c6dc588400adb3ec5831e5ad17c459b10d9b. | supports | Exact reviewed S288C gene query for VPS16 returns one entry, Q03308; actual tokens match the named primary gene or synonym. |
| plaque-query-VPS18 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS18%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS18.receipt.json SHA256 c26ce0cac9b5238d2a257327bc5422e554144767866fc7621fa3de4e5252a5b4. | supports | Exact reviewed S288C gene query for VPS18 returns one entry, P27801; actual tokens match the named primary gene or synonym. |
| plaque-query-VPS33 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS33%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS33.receipt.json SHA256 f961b8f5ff93f984358ac733f0a84dcbda4cd1a92af2a4272e7ce4ad6b1303e0. | supports | Exact reviewed S288C gene query for VPS33 returns one entry, P20795; actual tokens match the named primary gene or synonym. |
| plaque-query-VPS39 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS39.receipt.json SHA256 0230f3421830e8b7d3fb69cf7505aef82a14e90f5c60809d5f7a987de975604f. | supports | Exact reviewed S288C gene query for VPS39 returns one entry, Q07468; actual tokens match the named primary gene or synonym. |
| plaque-query-VPS41 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS41%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS41.receipt.json SHA256 3957a1fb9119ec909e76b25e6dd0bef628681d80449198a1f06a85176962691a. | supports | Exact reviewed S288C gene query for VPS41 returns one entry, P38959; actual tokens match the named primary gene or synonym. |
| plaque-query-YME1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYME1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-YME1.receipt.json SHA256 dedcb7dafa7b92fb7e6ce4b447f277f2c21928a96d0839f149d1bfaca025fd99. | supports | Exact reviewed S288C gene query for YME1 returns one entry, P32795; actual tokens match the named primary gene or synonym. |
| plaque-query-YPT7 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYPT7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-YPT7.receipt.json SHA256 021883601e23ec29157ee702a07a22d9b4a04927b705013acb14dc07be47887b. | supports | Exact reviewed S288C gene query for YPT7 returns one entry, P32939; actual tokens match the named primary gene or synonym. |
| plaque-query-YTA11 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYTA11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete one-page accession/gene/organism identity set, including primary and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-YTA11.receipt.json SHA256 b1105c83004ea6c11beb1bc61b34aef1397c5b85ef65201d5562a536e8df24c4. | supports | Exact reviewed S288C gene query for YTA11 returns one entry, P32795; actual tokens match the named primary gene or synonym. |
| plaque-ipr-IPR016528 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016528/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR016528.receipt.json SHA256 576cc73a6a687e3361e0a318874e77e01586e56c8b98f6606e198fd49f9554d3. | supports | Whole Vps11/Pep5 family, supported by native P12868 membership. |
| plaque-ipr-IPR016534 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016534/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR016534.receipt.json SHA256 3714b28ff4bdc3fbec40236d26e97523b087b91a8e802ddf10f8a4781996ff52. | supports | Whole Vps16 family, supported by native Q03308 membership. |
| plaque-ipr-IPR016902 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016902/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR016902.receipt.json SHA256 aeb2674acbf0255ab7ae5ea21e8d9c2fe55910a3820d4f25e3fa98c2956c83b4. | supports | Whole Vps41 family, supported by native P38959 membership; ambiguous descriptive prose is not imported as mechanism. |
| plaque-ipr-IPR013911 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013911/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR013911.receipt.json SHA256 8d7033578fb20aa2b9c631a23db6ff33a09810574daa9ffeeffa153acdd0b795. | supports | Whole Mgr1 family, with P25573 membership. |
| plaque-ipr-IPR040201 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040201/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR040201.receipt.json SHA256 3a37a9ead04422de8306a06112ca9feca549797e30cfda916618bd116201486e. | supports | Mrg3-like/Mgr3 family, with Q04472 membership; native authority spelling distinguished from yeast gene. |
| plaque-ipr-IPR005936 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005936/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR005936.receipt.json SHA256 c2dac901042671d5bf1fd334aacadd20c63a2d1ccceffcb9dac1d17afb2ca4fa. | supports | Broad FtsH family, not an exact Yme1-only class. |
| plaque-ipr-IPR048438 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048438/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR048438.receipt.json SHA256 51322fcb27fc6a273f6a9e0caff1fc45065762b0fec7fb092f5e1843e1f6860e. | supports | Yme1 amino-terminal domain, not a whole-protein Yme1 family. |
| plaque-ipr-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR001270.receipt.json SHA256 b884ed64172fa702706686afcbb2acdfd0320f998f6b3a3d1e15378dc60a998c. | supports | Broad ClpA/B-family grouping, not an exact Hsp78 class. |
| plaque-ipr-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; Native entry name/type, descriptions and quality flags, signatures; matched protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR050130.receipt.json SHA256 a63802c1204d64d87277f46f071c25ab816513ae28b5cc6bb3fec60097843df0. | supports | Broad ClpA/B-family grouping; generated description llm:true/checked:false is excluded from biological inference. |
| plaque-ipr-protein-P33416 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P33416/?page_size=200; Complete integrated InterPro response, entry types/names/accessions and next:null pagination. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-protein-P33416.receipt.json SHA256 15ea42c0fb5e1fae266ce179a15ad9c3ccb21266cc24831779cfc941418f1a09. | supports | Bounded exact protein P33416 family/domain inventory. Broader families or isolated domains do not establish an exact whole class; no all-authority absence claim. |
| plaque-ipr-protein-P32795 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P32795/?page_size=200; Complete integrated InterPro response, entry types/names/accessions and next:null pagination. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-protein-P32795.receipt.json SHA256 3a28a1a3c47f18bb4fa9bfc3a5f026a73c57388a8323d3cb2a427155c734ba37. | supports | Bounded exact protein P32795 family/domain inventory. Broader families or isolated domains do not establish an exact whole class; no all-authority absence claim. |
| plaque-go-search-hsp78 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Hsp78&amp;limit=25&amp;page=1; Complete response, zero results. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-search-hsp78.receipt.json SHA256 ca11786ab03deee4c19c1088fff9d03b904267fbf2db35d7f41b848b7fdf3a75. | supports | No term returned in this one bounded query; the local complex identity is not replaced by the broader chaperone class. |
| plaque-pmid-10944212 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10944212+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-10944212.receipt.json SHA256 c207cdee4458a12265c94e84772d4fb4e6e8239ab97766fbd4d2d674710c25ef. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-9362071 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9362071+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-9362071.receipt.json SHA256 7cfa2bcdfa94ba94985ce96b78e5a5ffd62fb34d9b5d2a7d489f5275c772e499. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-36115461 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36115461+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-36115461.receipt.json SHA256 ad9f6b32ff7d517f5f01984deff005d6a9976094fbab43b688720c4e866a7a64. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-29138251 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29138251+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-29138251.receipt.json SHA256 4bd5bbd53c697be2e3a67cc3dfeb0a6e3f8a92efbac099ef873396907f8cec27. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-14562095.receipt.json SHA256 8e776dc85ad692e78c8d2b361456877c6d12e510b6b91b733d137580d56158ef. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-14576278 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14576278+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-14576278.receipt.json SHA256 b3fd46a935085c9b07ba823be1c2abeecf4b52f116ad1460fddcc2d0f9e91659. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-16267274 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16267274+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-16267274.receipt.json SHA256 315af125552a90fc4ebd61392bbfef9ecdde5cce4efcf1763a4ed465c98aa08b. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-8355690 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8355690+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-8355690.receipt.json SHA256 2f8e6d944eef520a86399ec2cde6526ffa8dfd2b52446028c4f57b89b5c11fae. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-pmid-8688560 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8688560+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=2; Unique exact MED bibliographic identity, title/authors/year/DOI and complete available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-8688560.receipt.json SHA256 bcfb1fabe04a965681560e3feff8924197f1042a96b1ff2bad0df237bfbc44ec. | supports | Native bibliographic and abstract scope only; paper-body claims require separately inspected primary text. Historical Yme1 topology terminology is not silently reconciled with modern authority and Wu evidence. |
| plaque-PMC16876-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC16876/; Genuine full HTML: abstract; Methods sec1 including sec2–4, Results sec5 including sec6–9 and Figure1–4 text captions, Discussion sec10. No figure pixels. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC16876-body.receipt.json SHA256 f4cc75cd8c282d36ebe7b95cd4b7b41e79c43ce4d4ac189dd91fdb005f507d70. | supports | Seals2000 native yeast vacuole experiments support six-subunit HOPS association, priming-dependent rearrangement, GTP-Ypt7 binding and antibody-sensitive fusion. Vam2 identified by immunoblot, unlike the five MS assignments. BJ3505/DKY6281 vacuoles and recombinant bacterial antigens are distinct contexts. |
| plaque-PMC25710-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC25710/; Genuine full HTML, bounded reading: Methods sec3/Table1 and sec12 crosslinking, Results sec21 and Figure7 caption, Discussion sec25; no whole-body or pixel claim. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC25710-body.receipt.json SHA256 582483a8a91ae4aef4440effb765a4f2fee3685042bc8d6dfd47dde58dc7aa4e. | partial | Rieder1997 supports class-C core association and conditional Vps16-dependent recovery of Vps33, not universal formation necessity for each whole-HOPS member. SEY6210/6211 native yeast backgrounds and recombinant bacterial host are distinguished. |
| plaque-PMC9574514-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9574514.1/PMC9574514.1.xml; Genuine JATS: Results sec1.1–1.4 and main Fig1–7 captions; Discussion sec2; Methods sec3.1–3.14; Data availability sec4 and copyright. Introduction and supplementary data not certified. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-s3.receipt.json SHA256 6c9722b3f065b9f9088882436e52725982a8e1600b7c42dfff3f480ea1444cce. | supports | Jaworek2022 supports preparation-dependent oligomer observations, approximately 70% reduced (not absent) trap ATPase activity, reporter resolubilization and growth complementation. Solubility is not refolding, glycerol growth is not measured respiratory flux, and proteomic interaction candidates are not fixed oligomer constituents. Source mutation-numbering, salt and protocol inconsistencies are retained, as already disclosed by the record. |
| plaque-PMC5748973-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5748973.1/PMC5748973.1.xml; Genuine complete JATS: Introduction s01, Results/Discussion s03–s09 and embedded Fig1–5 captions, Methods s11/s16/s17. Whole article text additionally searched only for the asserted quote and specified words. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-s3.receipt.json SHA256 e038a3b2cce2b09cea6075e03625b51f353256b0da7227cd82f48592654a6fd6. | partial | Wu2017/2018 supports tagged/endogenous substrate turnover, Mgr1/Mgr3 recruitment/association, Mgr1 bridging and Mgr3-dependent Mgr1 stability. Adaptor deletions do not alter the observed Yme1 complex size. Neither a six-copy CPX annotation nor the asserted rocky-road/spiral quotation is supplied. These are source-support limits, not a refutation of independently studied isolated hexameric cores. |
| plaque-PMC5748973-JCB_201702125_TableS1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5748973.1/JCB_201702125_TableS1.xlsx; XLSX ZIP/XML worksheet1 A4:B25 and A123:C138 only, all returned cells in those ranges. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-JCB_201702125_TableS1.receipt.json SHA256 ef3c538d464d1b8966f577dc07604a10330a1e21c80eea180a5398ede036171c. | supports | TableS1 distinguishes BY4741 derivatives from CEN.PK and W303-1A constructs. Other strain/primer rows are not claimed read. |
| plaque-PMC9574514-gr1 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9574514.1/gr1.jpg; Actual downloaded native figure pixels, labels and separately read main-source caption/license. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr1.raw Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr1.receipt.json SHA256 3b74d97bf1fecc2bc2a8631eff476677a80668cf051b2456791dd8b70200d9f9. | supports | All Figure1 pixels inspected: ATPase curves, growth, native oligomer bands and purified SEC contexts; maintained MD5 d9e29f8d857266d914484f772d55ecac matches. No quantitative image reanalysis. |
| plaque-PMC9574514-gr2 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9574514.1/gr2.jpg; Actual downloaded native figure pixels, labels and separately read main-source caption/license. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr2.raw Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr2.receipt.json SHA256 8833b7925a298cc46bc4a237fcb5c638dbd973f558a11a3ac3e5e2f46c027e63. | supports | All Figure2 pixels inspected: reporter soluble/pellet fractions and separate binding assay. Caption/Methods protocol discrepancy remains disclosed; maintained MD5 9c7316c59aa052f86222a1cc34b03cc8 matches. |
| plaque-PMC5748973-JCB_201702125_Fig3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5748973.1/JCB_201702125_Fig3.jpg; Actual downloaded native figure pixels, labels and separately read main-source caption/license. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-JCB_201702125_Fig3.raw Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-JCB_201702125_Fig3.receipt.json SHA256 ccb75ac760bee0fec94be00e438ffd1995892f9a57cbbbe71b6db9f57c14ad80. | supports | All Figure3 A–H pixels inspected: co-IP recruitment blots and native-complex assays, not atomic reconstruction or counted stoichiometry; maintained MD5 ef80f8c8369e0bfd73138fdfd51c77be matches. |
| plaque-pride-PXD030405 | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD030405; Project accession/title, species, publication DOI, license, instrument and experiment metadata; underlying raw MS files not downloaded or reanalyzed. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pride-PXD030405.receipt.json SHA256 a7d41edf209239d116bdcfa17483dfa3930bf6b1f8439de1ad4809c6574d122e. | supports | Correct Hsp78 interaction/aggregation project identity, yeast organism and linked Jaworek paper. Project metadata CC0 is separate from article/figure CC BY-NC-ND4.0; proteomic associations are condition-specific. |
| plaque-pride-PXD030436 | https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD030436; Project accession/title, species, publication DOI, license, instrument and experiment metadata; underlying raw MS files not downloaded or reanalyzed. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pride-PXD030436.receipt.json SHA256 836e3872ca3951fcaaa358db06784ef1a0ba6cf5b3742dfde3c269d2a3eb0337. | supports | Correct Hsp78 interaction/aggregation project identity, yeast organism and linked Jaworek paper. Project metadata CC0 is separate from article/figure CC BY-NC-ND4.0; proteomic associations are condition-specific. |
| plaque-cpx-1655 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1655; Complete native complex identity, taxon, participants including native stochiometry keys, bioRole, linkedFeatures and evidenceType. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/cpx-1655.receipt.json SHA256 4339d42e9139fc830222d28770a3d344506334528e42e75c7adb1bbebb7ccab9. | supports | YME1/P32795 enzyme, MGR1/P25573, MGR3/Q04472 and CHEBI:29105 cofactor are participants. Every native stochiometry field exists and is null; no 6x annotation for Yme1 or zinc. ECO0005547 is curator inference, not a depletion/assembly assay. Taxon559292 retained despite species-style source label. |
| plaque-chebi-29105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29105; Exact native ChEBI identity and chemical definition. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/chebi-29105.receipt.json SHA256 57e98d8334b715288745c1f35bbf4089745afbd2192fc6f2520b509009c70e7c. | supports | CHEBI:29105 denotes zinc(2+), matching the maintained cofactor identity. |
| plaque-eco-0005547 | https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0005547; Exact native ECO definition. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/eco-0005547.receipt.json SHA256 797b1d2a03aaaff5524d574ea9691ea7d97afd33a5da1c13daa03da5ba7f7266. | supports | Curator inference based on background knowledge is distinct from physical-interaction experimental evidence. |
| plaque-PMC9574514-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9574514/fullTextXML; Exact failed retrieval receipt and raw response; no scientific content used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-jats.receipt.json SHA256 5b04a12c5a2fcd84a564db346bc2d0ca200e5dbf514d4103b31c2831a5bd6fcc. | context_only | This route returned HTTP 406; genuine separately read HTML/JATS supplies positive evidence. Failure is not biological absence. |
| plaque-PMC5748973-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5748973/fullTextXML; Exact failed retrieval receipt and raw response; no scientific content used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-jats.receipt.json SHA256 5b82909d8f98de2975c9a8e77ec0994501cf6fbee7a579a6c25165007b968c7c. | context_only | This route returned HTTP 406; genuine separately read HTML/JATS supplies positive evidence. Failure is not biological absence. |
| plaque-PMC16876-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC16876/fullTextXML; Exact failed retrieval receipt and raw response; no scientific content used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC16876-xml.receipt.json SHA256 76d643ea7e5889e91f39eed6a6ba6b499d2c540728f12440b14261a166915742. | context_only | This route returned HTTP 500; genuine separately read HTML/JATS supplies positive evidence. Failure is not biological absence. |
| plaque-PMC25710-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC25710/fullTextXML; Exact failed retrieval receipt and raw response; no scientific content used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC25710-xml.receipt.json SHA256 8cce8fdd2604dda52b477b534b19faa3b28cc37d6505a0959dfca9d3a3f8a079. | context_only | This route returned HTTP 500; genuine separately read HTML/JATS supplies positive evidence. Failure is not biological absence. |
| plaque-PMC16876-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC16876.1/PMC16876.1.xml; Exact failed retrieval receipt and raw response; no scientific content used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC16876-s3.receipt.json SHA256 24c7e402979be4ed9673b8c76796a56eca90da3fd720214fe80d0efa2b6059c7. | context_only | This route returned HTTP 404; genuine separately read HTML/JATS supplies positive evidence. Failure is not biological absence. |
| plaque-PMC25710-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC25710.1/PMC25710.1.xml; Exact failed retrieval receipt and raw response; no scientific content used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC25710-s3.receipt.json SHA256 3f80bc85699acb61173bf0dd0e726c45825f4beffb5932840f222e2987ad3947. | context_only | This route returned HTTP 404; genuine separately read HTML/JATS supplies positive evidence. Failure is not biological absence. |
| plaque-catalogue | https://imodulondb.org/api/organisms; Complete genuine 20-row organism catalogue, 28 organism/dataset entries; independent reread of shared current packet. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-catalogue-fresh.receipt.json SHA256 d426447e30a6a70975c1b3878c4952ed2ab69ee6756aa4a5bdf2e73b5a2d4ee2 | supports | No Saccharomyces cerevisiae or yeast experimental/reference strain represented. All three molecular narratives trigger assessment; no matched dataset exists within this inspected catalogue. Recombinant E. coli expression hosts are not proxies for yeast complexes. |
| plaque-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical command receipt only; no fresh invocation on this review. | context_only | 2026-11-03T00:49Z runner failed with PermissionError on pyvenv.cfg. Current assessment uses separately successful official HTTPS catalogue; historical failure is not current biological noncoverage. |
| plaque-original-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/original-proof.json; Three original native validate/render commands and 41 historical source-input hashes at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc. | supports | All three validations/render commands exit0; rendered Markdown equals original bytes; all original frozen input hashes match historical Git bytes. Historical success does not certify current changed i-AAA edges. |
| plaque-stale-diff | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/i-aaa-stale.diff; Exact original frozen i-AAA record to current source record diff. | supports | Current i-AAA adds Yme1 and zinc nodes, two architecture/cofactor edges and an October24 history entry. The new source-support defect is absent from the original reviewed record; HOPS/Hsp78 unchanged. |
| plaque-iaaa-attribution-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/iaaa-attribution-proof.json; Complete normalized genuine JATS phrase/word search and all four exact native CPX stochiometry fields. | supports | Exact purported quote absent; staircase/rocky/hexamer/spiral each zero in that article. All CPX fields present and null. Search bounded to this source, not literature-wide biology. |
| plaque-iaaa-peer-challenge | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/iaaa-core-source-challenge.json; Separate independent reading and whole-source quote search; exact source hashes retained. | supports | Independent challenge corroborates source-attribution finding while preserving valid roles, possible separately evidenced isolated hexamer and assay scope. |
| plaque-historical-jaworek-xml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9574514/fullTextXML; Original 20261022T074159Z-hsp78-chaperone-complex-audit evidence[19] micro57-jaworek2022-xml. Historical HTTP406 access-only evidence, kind corrected here; original artifact untouched. Original native406 receipt and raw bytes. | context_only | The EuropePMC XML request returned406 with a short error body, not a scientific source. Positive reading rests on the separately retained genuine PMC HTML and actual figure files. |
| plaque-native-hops_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-verify-receipt.json; Actual command receipt SHA256 1219be18d4fc421d3f2f4ad45265c96eb3a3085384bdc8004b4dba2b7722775e; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-verify.log with snapshot hash below; full log read. | supports | Six reviewed examples; six COVERED subunit nodes and external Ypt7 UNANCHORED_WITH_UNIPROT, correctly retained as external actor. Exit0 is identity/coverage validation, not mechanism or stoichiometry proof. |
| plaque-native-hops_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-causal-receipt.json; Actual command receipt SHA256 513d9eb6f9004d356cdd6256f2c8b4dcbad74c5d493139c93152da8ab04780cd; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-causal.log with snapshot hash below; full log read. | supports | Six reviewed examples; six COVERED subunit nodes and external Ypt7 UNANCHORED_WITH_UNIPROT, correctly retained as external actor. Exit0 is identity/coverage validation, not mechanism or stoichiometry proof. |
| plaque-native-hsp78_chaperone_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-verify-receipt.json; Actual command receipt SHA256 e34f7c886c2ac0da846eb4f79ddb8de94c5c87c8885e6ae0ae7f143a3a228e6d; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-verify.log with snapshot hash below; full log read. | supports | One reviewed Hsp78 example and one COVERED typed node. Exit0 is identity/coverage validation, not mechanism or stoichiometry proof. |
| plaque-native-hsp78_chaperone_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-causal-receipt.json; Actual command receipt SHA256 17f9e0759cfa889602f4cb4af4f2c7af021636803e4fb0868c9d7ca1897b7d26; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-causal.log with snapshot hash below; full log read. | supports | One reviewed Hsp78 example and one COVERED typed node. Exit0 is identity/coverage validation, not mechanism or stoichiometry proof. |
| plaque-native-i_aaa_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-verify-receipt.json; Actual command receipt SHA256 5bff57b1b18c281d7c74acf11216f97e989f315053767a9a0217cd259737438a; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-verify.log with snapshot hash below; full log read. | supports | Three reviewed examples and three COVERED typed protein nodes in current record; zinc is chemical. Original graph had only two typed protein nodes. Exit0 is identity/coverage validation, not mechanism or stoichiometry proof. |
| plaque-native-i_aaa_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-causal-receipt.json; Actual command receipt SHA256 6479d48213774e5852c8f91166f40bf9d116d8c52fbc912704869f8fcf83a992; stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-causal.log with snapshot hash below; full log read. | supports | Three reviewed examples and three COVERED typed protein nodes in current record; zinc is chemical. Original graph had only two typed protein nodes. Exit0 is identity/coverage validation, not mechanism or stoichiometry proof. |
| plaque-used-input-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/used-input-proof.json; Exact actually used maintained context and target/original paths; Git source and worktree hashes compared with native inspect. | supports | All actually used maintained input bytes match frozen source and current worktree. No unlisted maintained neighbor used. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Whole-record review and structured-source policy | supports | Positive named molecular/pathway assertions trigger actual host-specific applicability checks; absence of expression inference is not an exemption. |
| septin-curation-policy | docs/CURATION.md; Component grounding and dated discussion/history contract | supports | Verified exact families can resolve a current deferral. Preserve dated rationale and append current clarification rather than rewriting history. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Components, presence, essentiality and graph contracts | supports | Valid protein classes and associated machinery need not be one family or obligatorily represented in every optional field. Localization, membership, activity, viability and formation necessity differ. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Reference accession/name/status/taxon checks | supports | Reference identity and current singleton query evidence do not reconstruct historical releases or prove experimental membership/strain/causality. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope and actor/edge evidence | supports | Spatial parthood/function maps are nonmechanistic; a real coarse mechanistic edge need not assert unmeasured chemistry or universal necessity. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Source access and exact inspected extent | supports | Metadata, primary abstracts, genuine main bodies, supplements and viewed pixels have different scopes; failed access is validation context only. |
| septin-review-schema | schema/record_review.yaml; Native review schema and exact predecessor identities | supports | Use unique evidence references, bounded searches and exact inherited repository/review/finding references. |
| septin-up-P27343 | https://rest.uniprot.org/uniprotkb/P27343.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P27343: UniProtKB reviewed (Swiss-Prot); taxon 190650; gene tokens [{"geneName": {"value": "hfaB"}, "orderedLocusNames": [{"value": "CC_2629"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-A0A0H3CE47 | https://rest.uniprot.org/uniprotkb/A0A0H3CE47.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | A0A0H3CE47: UniProtKB unreviewed (TrEMBL); taxon 565050; gene tokens [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ACL97268.1"}], "value": "hfsK"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ACL97268.1"}], "value": "CCNA_03803"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q45977 | https://rest.uniprot.org/uniprotkb/Q45977.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q45977: UniProtKB reviewed (Swiss-Prot); taxon 190650; gene tokens [{"geneName": {"value": "hfaD"}, "orderedLocusNames": [{"value": "CC_2630"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P27342 | https://rest.uniprot.org/uniprotkb/P27342.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P27342: UniProtKB reviewed (Swiss-Prot); taxon 190650; gene tokens [{"geneName": {"value": "hfaA"}, "orderedLocusNames": [{"value": "CC_2628"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-tax-565050 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/565050; Entire native taxon identity/names/lineage | supports | Native scientific name Caulobacter vibrioides NA1000; relevant equivalent/synonym names ["Caulobacter crescentus NA1000:synonym"]. Taxon identity is not an experimental-strain substitution. |
| septin-tax-190650 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/190650; Entire native taxon identity/names/lineage | supports | Native scientific name Caulobacter vibrioides CB15; relevant equivalent/synonym names ["Caulobacter crescentus CB15:synonym", "Caulobacter vibrioides ATCC 19089:synonym"]. Taxon identity is not an experimental-strain substitution. |
| septin-tax-155892 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892; Entire native taxon identity/names/lineage | supports | Native scientific name Caulobacter vibrioides; relevant equivalent/synonym names ["Caulobacter vibrioides Henrici and Johnson 1935 (Approved Lists 1980):authority", "Caulobacter crescentus:synonym"]. Taxon identity is not an experimental-strain substitution. |
| septin-query-hfaA-190650 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhfaA%29+AND+%28organism_id%3A190650%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P27342. No historical query result or biological absence is inferred. |
| septin-query-hfaB-190650 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhfaB%29+AND+%28organism_id%3A190650%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P27343. No historical query result or biological absence is inferred. |
| septin-query-hfaD-190650 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhfaD%29+AND+%28organism_id%3A190650%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q45977. No historical query result or biological absence is inferred. |
| septin-up-V5IQM7 | https://rest.uniprot.org/uniprotkb/V5IQM7.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | V5IQM7: UniProtKB unreviewed (TrEMBL); taxon 367110; gene tokens [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ESA44030.1"}], "value": "spa2"}, "orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ESA44030.1"}], "value": "NCU03115"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q7RVZ1 | https://rest.uniprot.org/uniprotkb/Q7RVZ1.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q7RVZ1: UniProtKB unreviewed (TrEMBL); taxon 367110; gene tokens [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EAA34074.3"}], "value": "bud6"}, "orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EAA34074.3"}], "value": "NCU08468"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q7RWH7 | https://rest.uniprot.org/uniprotkb/Q7RWH7.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q7RWH7: UniProtKB unreviewed (TrEMBL); taxon 367110; gene tokens [{"geneName": {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EAA26755.1"}], "value": "bni1"}, "orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EAA26755.1"}], "value": "NCU01431"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-tax-5141 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141; Entire native taxon identity/names/lineage | supports | Native scientific name Neurospora crassa; relevant equivalent/synonym names ["Neurospora crassa Shear &amp; B.O. Dodge, 1927:authority", "Neurospora crassa Shear &amp; B. O. Dodge 1927:authority", "Chrysonilia crassa:synonym"]. Taxon identity is not an experimental-strain substitution. |
| septin-tax-367110 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/367110; Entire native taxon identity/names/lineage | supports | Native scientific name Neurospora crassa OR74A; relevant equivalent/synonym names ["Neurospora crassa FGSC 2489:equivalent name", "Neurospora crassa FGSC 9013:equivalent name", "Neurospora crassa 74-OR23-1VA:equivalent name", "Neurospora crassa N150:equivalent name", "Neurospora crassa 74-OR23-1V A:equivalent name"]. Taxon identity is not an experimental-strain substitution. |
| septin-query-spa2-367110 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Aspa2%29+AND+%28organism_id%3A367110%29+AND+%28reviewed%3Afalse%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: V5IQM7. No historical query result or biological absence is inferred. |
| septin-query-bud6-367110 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abud6%29+AND+%28organism_id%3A367110%29+AND+%28reviewed%3Afalse%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q7RVZ1. No historical query result or biological absence is inferred. |
| septin-query-bni1-367110 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abni1%29+AND+%28organism_id%3A367110%29+AND+%28reviewed%3Afalse%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q7RWH7. No historical query result or biological absence is inferred. |
| septin-up-P43579 | https://rest.uniprot.org/uniprotkb/P43579.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P43579: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "IES1"}, "orderedLocusNames": [{"value": "YFL013C"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P53946 | https://rest.uniprot.org/uniprotkb/P53946.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P53946: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "ARP5"}, "orderedLocusNames": [{"value": "YNL059C"}], "orfNames": [{"value": "N2430"}, {"value": "YNL2430C"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q03940 | https://rest.uniprot.org/uniprotkb/Q03940.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q03940: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "RVB1"}, "synonyms": [{"value": "TIH1"}, {"value": "TIP49A"}], "orderedLocusNames": [{"value": "YDR190C"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q03435 | https://rest.uniprot.org/uniprotkb/Q03435.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q03435: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "NHP10"}, "synonyms": [{"value": "HMO2"}], "orderedLocusNames": [{"value": "YDL002C"}], "orfNames": [{"value": "YD8119.05C"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q12345 | https://rest.uniprot.org/uniprotkb/Q12345.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q12345: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "IES3"}, "orderedLocusNames": [{"value": "YLR052W"}], "orfNames": [{"value": "L2131"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P35189 | https://rest.uniprot.org/uniprotkb/P35189.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P35189: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "TAF14"}, "synonyms": [{"value": "ANC1"}, {"value": "CST10"}, {"value": "SWP29"}, {"value": "TAF30"}, {"value": "TFG3"}], "orderedLocusNames": [{"value": "YPL129W"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P60010 | https://rest.uniprot.org/uniprotkb/P60010.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P60010: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "ACT1"}, "synonyms": [{"value": "ABY1"}, {"value": "END7"}], "orderedLocusNames": [{"value": "YFL039C"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P40154 | https://rest.uniprot.org/uniprotkb/P40154.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P40154: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "IES2"}, "orderedLocusNames": [{"value": "YNL215W"}], "orfNames": [{"value": "N1315"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q12386 | https://rest.uniprot.org/uniprotkb/Q12386.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q12386: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "ARP8"}, "orderedLocusNames": [{"value": "YOR141C"}], "orfNames": [{"value": "YOR3348C"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P32617 | https://rest.uniprot.org/uniprotkb/P32617.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P32617: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "IES6"}, "orderedLocusNames": [{"value": "YEL044W"}], "orfNames": [{"value": "SYGP-ORF13"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P80428 | https://rest.uniprot.org/uniprotkb/P80428.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P80428: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "ARP4"}, "synonyms": [{"value": "ACT3"}], "orderedLocusNames": [{"value": "YJL081C"}], "orfNames": [{"value": "J1012"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P40060 | https://rest.uniprot.org/uniprotkb/P40060.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P40060: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "IES5"}, "orderedLocusNames": [{"value": "YER092W"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-P53115 | https://rest.uniprot.org/uniprotkb/P53115.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | P53115: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "INO80"}, "orderedLocusNames": [{"value": "YGL150C"}], "orfNames": [{"value": "G1880"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q12464 | https://rest.uniprot.org/uniprotkb/Q12464.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q12464: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "RVB2"}, "synonyms": [{"value": "TIH2"}, {"value": "TIP49B"}], "orderedLocusNames": [{"value": "YPL235W"}], "orfNames": [{"value": "P1060"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-up-Q08561 | https://rest.uniprot.org/uniprotkb/Q08561.json; Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references | supports | Q08561: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName": {"value": "IES4"}, "orderedLocusNames": [{"value": "YOR189W"}]}]. Reference identity is separated from source experimental membership and necessity. |
| septin-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Entire native taxon identity/names/lineage | supports | Native scientific name Saccharomyces cerevisiae; relevant equivalent/synonym names ["Saccharomyces cerevisiae 'var. diastaticus':equivalent name", "Saccharomyces boulardii:equivalent name", "Saccharomyces boulardii Seguela, Bastide &amp; Massot, 1984:authority", "Saccharomyces diastaticus J. Andrews &amp; R.B. Gilliland ex Van der Walt, 1965:authority", "Mycoderma cerevisiae Desm., 1827:authority", "Saccharomyces sp. Af145-1-1:includes", "Saccharomyces uvarum var. melibiosus:synonym", "Saccharomyces oviformis:synonym", "Mycoderma cerevisiae:synonym", "Candida robusta:synonym", "Saccharomyces cerevisiae (Desm.) Meyen ex E.C. Hansen, 1883:synonym", "Saccharomyces boulardii (nom. inval.):synonym", "Saccharomyces italicus:synonym", "Saccharomyces capensis:synonym", "Saccharomyces diastaticus:synonym", "brewer's yeast:genbank common name"]. Taxon identity is not an experimental-strain substitution. |
| septin-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Entire native taxon identity/names/lineage | supports | Native scientific name Saccharomyces cerevisiae S288C; relevant equivalent/synonym names []. Taxon identity is not an experimental-strain substitution. |
| septin-pmid-19355820 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19355820+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: The biology of chromatin remodeling complexes.; Clapier CR, Cairns BR.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-19355820-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19355820+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | context_only | Clapier and Cairns 2009 is a secondary review; its abstract supplies general remodeling context, not a new assembly assay. |
| septin-pmid-12887900 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12887900+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Involvement of actin-related proteins in ATP-dependent chromatin remodeling.; Shen X, Ranallo R, Choi E, Wu C.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-12887900-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12887900+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-10787406 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10787406+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: The Saccharomyces cerevisiae RuvB-like protein, Tih2p, is required for cell cycle progression and RNA polymerase II-directed transcription.; Lim CR, Kimata Y, Ohdate H, Kokubo T, Kikuchi N, Horigome T, Kohno K.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-10787406-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10787406+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-8573785 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8573785+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: The actin-related protein Act3p of Saccharomyces cerevisiae is located in the nucleus.; Weber V, Harata M, Hauser H, Wintersberger U.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-8573785-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8573785+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-15525518 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15525518+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Rvb1p/Rvb2p recruit Arp5p and assemble a functional Ino80 chromatin remodeling complex.; Jónsson ZO, Jha S, Wohlschlegel JA, Dutta A.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-15525518-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15525518+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-11604509 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11604509+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: A well-connected and conserved nucleoplasmic helicase is required for production of box C/D and H/ACA snoRNAs and localization of snoRNP proteins.; King TH, Decatur WA, Bertrand E, Maxwell ES, Fournier MJ.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-11604509-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11604509+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-10952318 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10952318+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: A chromatin remodelling complex involved in transcription and DNA processing.; Shen X, Mizuguchi G, Hamiche A, Wu C.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-10952318-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10952318+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Global analysis of protein localization in budding yeast.; Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-14562095-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-24034245 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24034245+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Structure and subunit topology of the INO80 chromatin remodeler and its nucleosome complex.; Tosi A, Haas C, Herzog F, Gilmozzi A, Berninghausen O, Ungewickell C, Gerhold CB, Lakomek K, Aebersold R, Beckmann R, Hopfner KP.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-24034245-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24034245+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-pmid-25964121 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25964121+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Structural analyses of the chromatin remodelling enzymes INO80-C and SWR-C.; Watanabe S, Tan D, Lakshminarasimhan M, Washburn MP, Hong EJ, Walz T, Peterson CL.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-pmid-25964121-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25964121+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-query-INO80-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AINO80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P53115. No historical query result or biological absence is inferred. |
| septin-query-RVB1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARVB1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q03940. No historical query result or biological absence is inferred. |
| septin-query-RVB2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARVB2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q12464. No historical query result or biological absence is inferred. |
| septin-query-IES5-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P40060. No historical query result or biological absence is inferred. |
| septin-query-IES3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q12345. No historical query result or biological absence is inferred. |
| septin-query-NHP10-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANHP10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q03435. No historical query result or biological absence is inferred. |
| septin-query-IES6-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P32617. No historical query result or biological absence is inferred. |
| septin-query-IES1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P43579. No historical query result or biological absence is inferred. |
| septin-query-ARP8-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q12386. No historical query result or biological absence is inferred. |
| septin-query-ARP4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARP4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P80428. No historical query result or biological absence is inferred. |
| septin-query-ACT1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AACT1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P60010. No historical query result or biological absence is inferred. |
| septin-query-TAF14-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATAF14%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P35189. No historical query result or biological absence is inferred. |
| septin-query-IES2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P40154. No historical query result or biological absence is inferred. |
| septin-query-IES4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: Q08561. No historical query result or biological absence is inferred. |
| septin-query-ARP5-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARP5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned accession/name/gene/organism/status results; current exact query only | supports | Current response contains 1 entries: P53946. No historical query result or biological absence is inferred. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0000228,GO:0001411,GO:0006338,GO:0030427,GO:0031011,GO:0031012,GO:0031521,GO:0031562,GO:0051286,GO:0097346; Complete eleven-term response: names, definitions, synonyms and typed relationships | supports | Exact hyphal tip is fungal; GO0030427 is site of polarized growth. Polarisome/Spitzenkorper and Ino80 complex links retain correct parthood/is-a semantics. Extracellular matrix is broader than the local holdfast identity. |
| septin-go-0001411-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001411/ancestors?relations=is_a; Complete requested is_a-only ancestor response | supports | Typed is-a ancestry is assessed independently from parthood; no transitive relation is falsely reported as a direct edge. |
| septin-go-0031562-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031562/ancestors?relations=is_a; Complete requested is_a-only ancestor response | supports | Typed is-a ancestry is assessed independently from parthood; no transitive relation is falsely reported as a direct edge. |
| septin-go-0031011-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031011/ancestors?relations=is_a; Complete requested is_a-only ancestor response | supports | Typed is-a ancestry is assessed independently from parthood; no transitive relation is falsely reported as a direct edge. |
| septin-go-search-holdfast | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=holdfast&amp;limit=100; Complete zero-hit exact-text search response | supports | No exact holdfast term returned in this bounded current GO search. This supports retaining the local identifier with broader matrix parent; it is not an exhaustive assertion about all ontologies. |
| septin-sulkowski-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00112-19%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: A Multiprotein Complex Anchors Adhesive Holdfast at the Outer Membrane of Caulobacter crescentus.; Sulkowski NI, Hardy GG, Brun YV, Bharat TAM.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-sulkowski-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00112-19%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-hershey-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00276-19%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Composition of the Holdfast Polysaccharide from &lt;i&gt;Caulobacter crescentus&lt;/i&gt;.; Hershey DM, Porfírio S, Black I, Jaehrig B, Heiss C, Azadi P, Fiebig A, Crosson S.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-hershey-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00276-19%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-sprecher-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FmBio.00294-17%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Cohesive Properties of the &lt;i&gt;Caulobacter crescentus&lt;/i&gt; Holdfast Adhesin Are Regulated by a Novel c-di-GMP Effector Protein.; Sprecher KS, Hug I, Nesper J, Potthoff E, Mahi MA, Sangermani M, Kaever V, Schwede T, Vorholt J, Jenal U.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-sprecher-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FmBio.00294-17%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-lichius-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pone.0030372%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Comparative live-cell imaging analyses of SPA-2, BUD-6 and BNI-1 in Neurospora crassa reveal novel features of the filamentous fungal polarisome.; Lichius A, Yáñez-Gutiérrez ME, Read ND, Castro-Longoria E.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-lichius-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pone.0030372%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-watanabe-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms8108%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete exact MED bibliographic record: authors/title/year/DOI/PMID and abstract availability | context_only | Native bibliography: Structural analyses of the chromatin remodelling enzymes INO80-C and SWR-C.; Watanabe S, Tan D, Lakshminarasimhan M, Washburn MP, Hong EJ, Walz T, Peterson CL.. Metadata supports source identity only; the separately classified abstract has its own scientific scope. |
| septin-watanabe-metadata-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms8108%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; Complete available abstractText only; no main-body, figure-pixel, supplement or raw-data access implied | supports | Independently read complete native primary abstract. Its stated species, assays and limitations remain bounded; no unreported Methods details inferred. |
| septin-ipr-IPR038014 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038014/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR038014 name {'name': 'Ino80 subunit 1', 'short': 'Ies1'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR029523 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029523/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR029523 name {'name': 'INO80 complex, subunit Ies2', 'short': 'INO80B/Ies2'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR062650 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062650/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR062650 name {'name': 'INO80 complex subunit 4', 'short': 'IES4'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR020366 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020366/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR020366 name {'name': 'INO80 complex subunit Ies5', 'short': 'Ies5'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR029525 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029525/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR029525 name {'name': 'INO80 complex, subunit Ies6', 'short': 'INO80C/Ies6'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR050520 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050520/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR050520 name {'name': 'INO80/SWR1 chromatin remodeling helicase', 'short': 'INO80/SWR1_helicase'}, type family. Machine-generated unchecked descriptive prose is excluded from biological support; only native classification identity and independently verified membership used. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR027238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027238/; Actual failed HTTP retrieval | context_only | HTTP 429 did not supply a usable authority entry; successful bounded retry is separately recorded. |
| septin-ipr-IPR004000 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/; Actual failed HTTP retrieval | context_only | HTTP 429 did not supply a usable authority entry; successful bounded retry is separately recorded. |
| septin-ipr-IPR016665 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016665/; Actual failed HTTP retrieval | context_only | HTTP 429 did not supply a usable authority entry; successful bounded retry is separately recorded. |
| septin-ipr-IPR050342 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050342/; Actual failed HTTP retrieval | context_only | HTTP 429 did not supply a usable authority entry; successful bounded retry is separately recorded. |
| septin-ipr-IPR039892 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR039892 name {'name': 'Protein Spa2/Sph1', 'short': 'Spa2/Sph1'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR051825 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR051825 name {'name': 'SRC Kinase Signaling Inhibitor', 'short': 'SRCIN1'}, type family. Machine-generated unchecked descriptive prose is excluded from biological support; only native classification identity and independently verified membership used. This entry alone does not prove assembly necessity. |
| septin-ipr-IPR051661 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051661/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR051661 name {'name': 'Actin filament dynamics regulator', 'short': 'Actin_filament_regulator'}, type family. Machine-generated unchecked descriptive prose is excluded from biological support; only native classification identity and independently verified membership used. This entry alone does not prove assembly necessity. |
| septin-retry-IPR027238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027238/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR027238 name {'name': 'RuvB-like', 'short': 'RuvB-like'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-retry-IPR004000 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR004000 name {'name': 'Actin family', 'short': 'Actin'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-retry-IPR016665 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016665/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR016665 name {'name': 'SAS complex subunit SAS5/transcription initiation factor TFIID subunit 14', 'short': 'Sas5/TAF14'}, type family. Curated family boundary is distinguished from shared domains/paralogue classes. This entry alone does not prove assembly necessity. |
| septin-retry-IPR050342 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050342/; Native entry accession/name/type, member signatures, annotation curation flags; exact UniProt family joins checked independently | supports | Native IPR050342 name {'name': 'High Mobility Group Box (HMGB)', 'short': 'HMGB'}, type family. Machine-generated unchecked descriptive prose is excluded from biological support; only native classification identity and independently verified membership used. This entry alone does not prove assembly necessity. |
| septin-sulkowski-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6707917/fullTextXML; Genuine JATS title; full Introduction, Results s2.1–s2.3, Table1 and embedded figure captions; Discussion and Methods s4.1–s4.7 | supports | CB15 and CB15-derived strains support HfaABD anchor structure/retention, with HfaB density loss and A/D surface assignment. Hfa mutants can still synthesize and shed matrix. Actual title says Outer Membrane, not Old Cell Pole. No figure pixels, tomogram reanalysis or supplementary asset inspection. |
| septin-sprecher-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5362036/fullTextXML; Genuine JATS complete abstract; Results s1.2/s1.3/s1.5/s1.7, Discussion s2 and growth Methods s3.1; embedded relevant figure/supplement captions only | supports | CB15 experiments establish HfsK-dependent cohesion/shear resistance, c-di-GMP binding and localization. NA1000 is an explicitly nonadherent comparator. Catalytic acylation/substrate chemistry remains proposed; altered cohesion and/or anchoring are distinguished. Actual supplementary videos/pixels were not inspected. |
| septin-lichius-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3265482/fullTextXML; Genuine JATS complete abstract; Results s2b/s2e/s2f/s2i–s2l/s2n/s2o, Table2 and relevant embedded captions; Discussion s3a–s3e/s3g; Methods s4a | supports | Neurospora source distinguishes mature-tip SPA2/BUD6/BNI1 topology, early polarity, septal plugging and polarisome-independent septation/cytokinesis. N150/FGSC9013 and named derived strains are explicit; OR74A authority includes N150/FGSC9013 synonyms, without making every deletion strain identical. Delta bud6/bni1 disrupt Spk/tip organization but permit altered polarized growth, so no universal growth/assembly necessity is inferred. No pixels/videos or unlisted supplements read. |
| septin-watanabe-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC4431590.1/PMC4431590.1.xml; Genuine S3 JATS Results S3–S7, Discussion S8, Methods S10/S17; exact paper bibliography/abstract and relevant embedded text | supports | Fifteen named INO80 classes are recovered by TAP purifications; Ies6/Arp5 loss cripples remodeling activity while residual complexes remain. Arp8 module loss reduces rather than abolishes several activities. Rvb ring-count disagreement with Tosi is explicit; the record does not impose a contested fixed molecular count or claim helicase activity. No pixels/coordinates/raw MS data inspected. |
| septin-watanabe-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC4431590.1/NIHMS677628-supplement-1.pdf; Published supplementary PDF, extracted complete Supplementary Tables1 and2 and their captions on the final two pages; no image-pixel inspection | supports | Table2 names all fifteen INO80 classes and reports spectral counts/sequence coverage across three independent preparations. Table1 is SWR-C; inverted main-text table references are not propagated. Fifteen subunit identities are not fifteen total molecular copies. Supplementary figure pixels and raw spectra were not analyzed. |
| septin-hershey-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6689307/fullTextXML; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Actual route status 500 did not supply a usable article body. Successful alternative or primary-abstract support is separately scoped. |
| septin-watanabe-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4431590/fullTextXML; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Actual route status 500 did not supply a usable article body. Successful alternative or primary-abstract support is separately scoped. |
| septin-hershey-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC6689307/; Actual HTTP/status/body or exact package-list diagnostic only | context_only | HTTP200 browser-check/challenge content; no genuine main body obtained. |
| septin-watanabe-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC4431590/; Actual HTTP/status/body or exact package-list diagnostic only | context_only | HTTP200 browser-check/challenge content; no genuine main body obtained. |
| septin-hershey-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC6689307.1/PMC6689307.xml; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Actual route status 404 did not supply a usable article body. Successful alternative or primary-abstract support is separately scoped. |
| septin-watanabe-s3xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC4431590.1/PMC4431590.xml; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Actual route status 404 did not supply a usable article body. Successful alternative or primary-abstract support is separately scoped. |
| septin-hershey-s3listing | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC6689307.1/; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Exact specified public S3 package-prefix listing returned no entries (not truncated). This is only a bounded access-route result, not absence of the article or scientific refutation. |
| septin-watanabe-s3listing | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC4431590.1/; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Exact S3 package listing located the genuine versioned XML and supplementary PDF; directory metadata is not scientific evidence. |
| septin-hershey-package-list | https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&amp;prefix=PMC6689307; Actual HTTP/status/body or exact package-list diagnostic only | context_only | Exact specified public S3 package-prefix listing returned no entries (not truncated). This is only a bounded access-route result, not absence of the article or scientific refutation. |
| septin-adapter-catalogue | https://imodulondb.org/api/organisms; All twenty returned organism rows and their dataset names; exact target-host and synonym checks | supports | No Caulobacter vibrioides/crescentus, CB15/NA1000, Neurospora, Saccharomyces, Candida or Ashbya host dataset is represented. E. coli expression/cloning hosts are not substituted for biological targets. Downstream matched gene/module queries are therefore not applicable; absence is catalogue coverage only, not biology. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z | context_only | Historical runner failed exit1 with PermissionError reading pyvenv.cfg. No fresh runner invocation is claimed. Current independently inspected official catalogue and native primary/authority checks provide the declared fallback. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-septin/original-checks.json; Actual four native validate/render pairs plus exact historical Git-object input hashes | supports | All four original pairs validate/render0 and Markdown is exact. All 55 frozen historical input occurrences match. All four current records are nonstale. |
| septin-record-holdfast | data/structures/other/holdfast.yaml; Complete current maintained record: identity, boundaries, components/examples, functions, graph, evidence, discussions and history | supports | Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826; exact target SHA equals the original frozen input. No stale content or record edit. |
| septin-original-holdfast | reviews/structured/20261022T074158Z-holdfast-audit/review.yaml; Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations and source read scopes | supports | Original 20261022T074158Z-holdfast-audit contains 2 inherited findings; exact original hash/render retained. Historical batch26 execution provenance is distinguished from the target review cohort and not relabeled as a defect. |
| septin-native-holdfast-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-verify-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Three reviewed CB15 Hfa examples; one COVERED Hfa complex node and one UNANCHORED_WITH_UNIPROT external HfsK node A0A0H3CE47 (unreviewed NA1000 reference). No missing optional component is inferred; reference identity does not prove experimental NA1000 adhesiveness. Exit0. Receipt SHA 358e0da1c2bd67a0387813aaca067e76388fbe12ccee7ba0a04604d6d8a7aaeb; log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-holdfast-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-causal-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Three reviewed CB15 Hfa examples; one COVERED Hfa complex node and one UNANCHORED_WITH_UNIPROT external HfsK node A0A0H3CE47 (unreviewed NA1000 reference). No missing optional component is inferred; reference identity does not prove experimental NA1000 adhesiveness. Exit0. Receipt SHA 59333e0f6aeb71468c577539893b683019739efadc0875db683da5084f6c8259; log SHA 8cc632f432bb3112dab58b3fe1f3ab70db859089a87909be8af240e24661819c. |
| septin-record-hyphal_tip | data/structures/other/hyphal_tip.yaml; Complete current maintained record: identity, boundaries, components/examples, functions, graph, evidence, discussions and history | supports | Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826; exact target SHA equals the original frozen input. No stale content or record edit. |
| septin-original-hyphal_tip | reviews/structured/20261022T074200Z-hyphal-tip-audit/review.yaml; Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations and source read scopes | supports | Original 20261022T074200Z-hyphal-tip-audit contains 2 inherited findings; exact original hash/render retained. Historical batch26 execution provenance is distinguished from the target review cohort and not relabeled as a defect. |
| septin-native-hyphal_tip-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-verify-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Three unreviewed Neurospora OR74A examples V5IQM7/Q7RVZ1/Q7RWH7; all three typed nodes COVERED. Identity coverage does not validate the expanded definition or MECHANISTIC graph label. Exit0. Receipt SHA 1375c483e9ca46986d43e482bdfdddb753d544a88caa4814db7a2b245a551572; log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-hyphal_tip-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-causal-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Three unreviewed Neurospora OR74A examples V5IQM7/Q7RVZ1/Q7RWH7; all three typed nodes COVERED. Identity coverage does not validate the expanded definition or MECHANISTIC graph label. Exit0. Receipt SHA 0c4af3efaa47abbade941408b0458d6d2c79f7145b6e0e8daadc76f1c63d7c1b; log SHA 91cc237750b3f3b8f5dfa2f9942ef9989f97cd12bb602529c105cf1290bc4896. |
| septin-record-hyphal_tip_polarisome | data/structures/other/hyphal_tip_polarisome.yaml; Complete current maintained record: identity, boundaries, components/examples, functions, graph, evidence, discussions and history | supports | Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826; exact target SHA equals the original frozen input. No stale content or record edit. |
| septin-original-hyphal_tip_polarisome | reviews/structured/20261022T074201Z-hyphal-tip-polarisome-audit/review.yaml; Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations and source read scopes | supports | Original 20261022T074201Z-hyphal-tip-polarisome-audit contains 0 inherited findings; exact original hash/render retained. Historical batch26 execution provenance is distinguished from the target review cohort and not relabeled as a defect. |
| septin-native-hyphal_tip_polarisome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-verify-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Three unreviewed Neurospora OR74A examples and all three nodes COVERED. Distinct mature-tip localizations are source-supported; no direct physical-contact or universal assembly claim follows from coverage. Exit0. Receipt SHA 16a97967682d8b16138573d37fa961f37b9258c45ddb9bd9f7110e1c841bfdcf; log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-hyphal_tip_polarisome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-causal-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Three unreviewed Neurospora OR74A examples and all three nodes COVERED. Distinct mature-tip localizations are source-supported; no direct physical-contact or universal assembly claim follows from coverage. Exit0. Receipt SHA 1f5d749e79121d8477b4ca0df2e1dc6f07bf2fd36ad4325584ac898a8c9977b8; log SHA e888a6c3fd631ea34eb095cd4b5ab67fa6ad7b2e551ab37fe3c578aab82f92a3. |
| septin-record-ino80_complex | data/structures/other/ino80_complex.yaml; Complete current maintained record: identity, boundaries, components/examples, functions, graph, evidence, discussions and history | supports | Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826; exact target SHA equals the original frozen input. No stale content or record edit. |
| septin-original-ino80_complex | reviews/structured/20261022T074202Z-ino80-complex-audit/review.yaml; Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations and source read scopes | supports | Original 20261022T074202Z-ino80-complex-audit contains 1 inherited findings; exact original hash/render retained. Historical batch26 execution provenance is distinguished from the target review cohort and not relabeled as a defect. |
| septin-native-ino80_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-verify-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Fifteen reviewed S288C reference examples and all fifteen nodes COVERED. These are fifteen constituent classes, not a fixed fifteen-protein stoichiometry; exact family and activity/necessity scopes are independently assessed. Exit0. Receipt SHA d4fae12a56361c3343b94b3a9d50310e6fe73efe45827be6c78e57ddc34f6395; log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289. |
| septin-native-ino80_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-causal-receipt.json; Actual parent-run native command; independently read full stdout, receipt and target inventory | supports | Fifteen reviewed S288C reference examples and all fifteen nodes COVERED. These are fifteen constituent classes, not a fixed fifteen-protein stoichiometry; exact family and activity/necessity scopes are independently assessed. Exit0. Receipt SHA 66464ad8b169db3b2cdc639b76d68667f00d9f5c5049cdc4cfa13b58cc3ae130; log SHA aa96cf2f4b6921e477f5ffa6700a09bdedf93e8d1eaf4c39893c3fd5d6242a70. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech check passed: all 10 links resolve with matching labels against the 1130-trait source index. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | All 22 governed artifacts match the pinned CLAW revision. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified all 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2394 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-hda1_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hda1_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hda_beta_clamp_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hda_beta_clamp_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hir_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hir_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-holdfast-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-holdfast-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hops_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hops_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hsp78_chaperone_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hsp78_chaperone_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hyphal_tip-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hyphal_tip-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hyphal_tip_polarisome-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-hyphal_tip_polarisome-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-i_aaa_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-i_aaa_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ino80_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ino80_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- HDA1, Hda-beta clamp and HIR independent review: Assigned scientific scope is three complete nonstale records: HDA1,Hda-beta clamp,HIR.27 actually used maintained inputs are17 common rules/config/schema/scripts,three targets,six original artifacts and one frozen i-AAA target used only in a separate peer challenge. All47 frozen inputs and20 immutable originals are independently hash-audited in finalization.
- HDA1, Hda-beta clamp and HIR independent review: Wu2001 genuine PMC main Methods/Results/Discussion,Tables and Figures1–6 text captions were read; no pixels/raw densitometry or supplements. Hydrodynamic mass supports a likely2:1:1 model, not atomic stoichiometry; conditional recovery,activity and locus-specific ChIP are separate.
- HDA1, Hda-beta clamp and HIR independent review: Carmen1996 remains complete indexed abstract plus metadata only in this review; current DOI content negotiation yielded bibliographic metadata, not body. Earlier redirect/403 and Panther204 rows retain original dates/hashes and honest limits with corrected evidence kinds. No fresh Panther access or comprehensive alternative-family absence is claimed.
- HDA1, Hda-beta clamp and HIR independent review: Kurz2004 genuine main body,Methods,Tables1/2 and Figures1–3 captions read. Purified-binding assays and prior RIDA reaction evidence are distinguished; XL1Blue-derived genes and BL21(DE3)pLyS/TB1 preparations are not silently assigned reference K-12 or precise1k strain identities. Misfolding alternative remains.
- HDA1, Hda-beta clamp and HIR independent review: Green2005 genuine main Results/Discussion,Figures1–4 captions and Experimental Procedures pointer read. Supplementary detailed protocols/strain tables and pixels remain unread. HIR-Asf1 association, remaining-subunit recovery,DNA binding and deposition are different assays; global UNKNOWN is not a defect by itself.
- HDA1, Hda-beta clamp and HIR independent review: Mousson2007 is secondary review/abstract only; localization articles are exact current indexed metadata/abstracts with UniProt annotation provenance, not freshly certified complete bodies. Where individual assays are not in an abstract, native annotation scope remains explicit.
- HDA1, Hda-beta clamp and HIR independent review: Current family decisions use native type/name/hierarchy/signatures and positive reference xrefs. Generic shared classes are valid in principle; the bounded actions target explicitly named classes and existing tasks. No whole-protein identity is forced from a domain, no exhaustive family search or sequence alignment claimed.
- HDA1, Hda-beta clamp and HIR independent review: Nine current exact reviewed gene/taxon queries each have one expected result and no next page; actual native primary/synonym/locus fields checked. This is not a reconstruction or disproof of historical selection execution.
- HDA1, Hda-beta clamp and HIR independent review: Official catalogue has20 organism rows/28 pairs with no Saccharomyces. E.coli precise1k has201 modules,4257 genes,1035 samples/518 conditions across BW25113,DGF-298,GMOS,MG1655,W3110. hda/b2496 and dnaN/b3701 match reference accessions and each has0 thresholded memberships across201 rows. No gene absence, physical-complex evidence, foreign yeast proxy,AI narrative or activity-vector causality is inferred.
- HDA1, Hda-beta clamp and HIR independent review: Historical local runner PermissionError remains the actual Nov3 00:49Z observation. Fresh official fallback responses have separate dates. Three failed S3 body routes are validation only. Initial sandbox DNS failures and exploratory wrong DOI/irrelevant GO probes are retained in scratch but not used as biological evidence.
- HDA1, Hda-beta clamp and HIR independent review: Six current root native commands exit0: HDA1 three examples/three COVERED nodes;Hda-beta two examples/one COVERED Hda node,DnaN STRUCTURE;HIR four examples/four COVERED nodes. Native coverage does not establish biology. Original six validate/render commands and42 historical input occurrences pass. Root corpus gates/publication/successor/final-head/CI/queue remain separately owned, not precertified.
- HDA1, Hda-beta clamp and HIR independent review: Three inherited minor grounding findings persist with exact repository/review/finding lineage and three bounded future actions. No new own science or stale target; three formal applicability corrections plus five historical kind-only occurrences are bundle defects. No record edits, broad grouped-issue resolution, universal necessity demand or optional-example defect.
- HDA1, Hda-beta clamp and HIR independent review: Separate immutable i-AAA challenge validates source-attribution/quote limits for plaque; it is not an additional own scientific finding or complete i-AAA/image review. Exact genuine sources and frozen policy/record hashes are bound in that auxiliary receipt.
- HOPS, Hsp78 and i-AAA independent review: Only assigned HOPS, Hsp78 and i-AAA whole records and their exact originals were scientifically reviewed. No neighboring record, category resolution or unrelated issue disposition inferred.
- HOPS, Hsp78 and i-AAA independent review: Fresh exact native authorities and primary scopes are individually declared. Seals Methods/Results/Discussion, bounded Rieder core-association sections, Jaworek Results/Discussion/Methods/Data availability and Wu Introduction/Results/Discussion plus selected Methods were read; unlisted text and cited papers were not certified.
- HOPS, Hsp78 and i-AAA independent review: Actual external Hsp78 Figures1/2 and Wu Figure3 pixels inspected; no other primary figure pixels, quantitative image reanalysis, complete supplementary workbook or raw proteomic reanalysis claimed. TableS1 read only specified ranges.
- HOPS, Hsp78 and i-AAA independent review: Jaworek mutation, salt and protocol conflicts remain unresolved but explicitly disclosed by the record. Hsp78 native oligomers, purified SEC and activity/solubility/growth assays are not conflated.
- HOPS, Hsp78 and i-AAA independent review: Older Yme1 topology language in Weber abstract/UniProt conflicts with modern GO/Wu IMS context. No silent harmonization or full-body review of the five older PMID sources claimed.
- HOPS, Hsp78 and i-AAA independent review: i-AAA finding concerns the exact cited quotation and CPX count attribution. Complete source-text search is bounded to that article; it does not rule out an isolated hexamer established in other primary literature.
- HOPS, Hsp78 and i-AAA independent review: The original runner failure is historical November3 00:49Z, not a new execution. The fresh complete official catalogue has no yeast dataset; no bacterial expression-host proxy, generated module summary or inferred biological absence used.
- HOPS, Hsp78 and i-AAA independent review: Native verify/causal success checks identity and declared coverage. It does not establish mechanism, stoichiometry or necessity. HOPS Ypt7 external UNANCHORED_WITH_UNIPROT is appropriate, not a missing constituent.
- HOPS, Hsp78 and i-AAA independent review: Original bundles and records are immutable; bundle corrections belong in the successor. Scientific actions remain proposed separate curation. Global QC, issue publication, final save/CI/queue are parent-owned and not independently certified by this source report.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: All four assigned current records are byte-identical to their historical frozen record inputs; this review refreshes source scrutiny and applicability without any record edit. The other six records are not scientifically re-reviewed in this subreport.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: All 55 original input occurrences match their exact historical Git objects and four old pairs validate/render exactly. Historical batch26 global executions are preserved as scoped provenance, not reclassified as current PR2394 runs.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Hershey complete primary abstract directly enumerates all five claimed sugars. EPMC XML returned500, canonical PMC returned200 browser challenge, and two exact public S3 prefixes returned no package; no genuine Hershey main body, Methods, table or pixel inspection is claimed.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Watanabe genuine versioned S3 XML and supplement PDF succeeded after failed EPMC/guessed paths. Only listed main-text sections and extracted Supplementary Tables1/2 were read; no raw MS files, atomic coordinates or figure pixels. Main-text table-number inversion is not turned into a record defect.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Shen2000/2003, Jonsson2004, Tosi2013 and ancillary localization/Rvb source papers are limited to their complete native abstracts; Clapier/Cairns2009 is explicitly secondary abstract context. No abstract is promoted to full Methods or an experimental-strain identity.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Lichius and Sprecher scope is the enumerated genuine source text and embedded relevant captions, not supplementary videos or pixels. Deletion/activity/localization observations do not establish universal formation necessity; no direct physical contact is inferred solely from colocalization.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: InterPro unchecked machine-generated prose is excluded. Native entry name/type plus independent UniProt cross-references are used for family identity. Shared full families/domains are not forced onto narrower classes; no exhaustive absence of optional identifiers is asserted.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Complete fresh official iModulonDB catalogue lacks the exact biological hosts and relevant named fungal comparison hosts. E. coli recombinant expression/cloning context is not a surrogate. Historical runner PermissionError retains its actual Nov3 00:49 timestamp; no fresh runner invocation or biological absence inferred.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Native source verification covers three reviewed holdfast examples, six unreviewed Neurospora example occurrences across two records and fifteen reviewed Ino80 examples:24 occurrences,21 distinct constituent accessions plus external unreviewed HfsK. Twenty-three typed nodes comprise22 COVERED andone UNANCHORED_WITH_UNIPROT; this is reference coverage, not proof of membership or causality.
- Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: No maintained local image is present in these four targets. Repository/Git/GitHub remain read-only. Parent-owned full QC, later successor validation, final-head CI and queue/merge are not certified by this source report.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun. Its retained November3 PermissionError receipt is historical; current catalogue coverage is assessed directly, and fresh or reused responses retain their actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- One changed target, i-AAA complex, requires substantive current-input reassessment; nine other current target hashes match original frozen inputs. All used maintained context is frozen before synthesis.
- Twenty current native protein commands passed across 43 represented protein examples and 42 typed GENE_OR_PROTEIN nodes: 40 COVERED and two UNANCHORED_WITH_UNIPROT (holdfast HfsK and HOPS Ypt7). External machinery is not forced into constituent rows. Identity and coverage are not experimental membership or necessity evidence.
- Original observations and dated rationale remain immutable. Source bodies, primary abstracts, database entries and failed-access diagnostics retain exact scopes and dates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T124211Z-pr2394-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2394: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T12:22:27.268858Z'
finished_at: '2026-11-04T12:42:11Z'
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
summary: 'Independent whole-record reassessment of ten current records retains nine
  inherited scientific findings and establishes one new major source-attribution finding
  in the stale i-AAA record: three major and seven minor findings across eight records
  needing curation. Hsp78 and hyphal-tip polarisome pass with explicit limitations.
  One stale record review is substantively refreshed against current inputs; the other
  nine records are byte-identical to their original frozen targets. The immutable
  successor corrects ten applicability assessments and six historical access-only
  evidence kinds, preserves all original artifacts and source-access boundaries, and
  links every scientific action to a separate open record-curation issue. No records
  are edited.'
source:
  git_revision: f5668d26c554ec2f62610183aed5c5bc3aa76826
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
  - path: data/structures/other/hda1_complex.yaml
    sha256: 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90
    role: target
  - path: data/structures/other/hda_beta_clamp_complex.yaml
    sha256: 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb
    role: target
  - path: data/structures/other/hir_complex.yaml
    sha256: 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52
    role: target
  - path: data/structures/other/holdfast.yaml
    sha256: 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862
    role: target
  - path: data/structures/other/hops_complex.yaml
    sha256: 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f
    role: target
  - path: data/structures/other/hsp78_chaperone_complex.yaml
    sha256: ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262
    role: target
  - path: data/structures/other/hyphal_tip.yaml
    sha256: d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4
    role: target
  - path: data/structures/other/hyphal_tip_polarisome.yaml
    sha256: 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667
    role: target
  - path: data/structures/other/i_aaa_complex.yaml
    sha256: f6877406ef9d82f3c18666e77b2ae3bb8c0a8c8c582c35bfba92d7cffafacda9
    role: target
  - path: data/structures/other/ino80_complex.yaml
    sha256: 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4
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
  - path: reviews/structured/20261022T074156Z-hda1-complex-audit/review.md
    sha256: 6ef0d6eb89b5f0e0d68b4fd6a177477ecec3cdc50a0281785070cea626e192e9
    role: context
  - path: reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml
    sha256: 6802461abd98d8f664006cf9565d3d54b0ccb8571a1f4d7d7fbbb0e73bfb6801
    role: context
  - path: reviews/structured/20261022T074157Z-hda-beta-clamp-complex-audit/review.md
    sha256: aac9688ad23e584f648cdca438d9c8ecf15ea3dfc23b1a334621db57ce945b63
    role: context
  - path: reviews/structured/20261022T074157Z-hda-beta-clamp-complex-audit/review.yaml
    sha256: d1c8b27d6d3791d717a71e3f133f2ac4cae17e105393786bd68909e34d781794
    role: context
  - path: reviews/structured/20261022T074158Z-hir-complex-audit/review.md
    sha256: 868e428790c38ce983a7b5dfebb70f7f192e345ee7e7de311bf9585be4e29b87
    role: context
  - path: reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml
    sha256: 25f3189b1167801e98e7100f04581c3046aa690607b5fed3a516a735f803807f
    role: context
  - path: reviews/structured/20261022T074158Z-holdfast-audit/review.md
    sha256: 321c86d23bb16553c5a4b1bdff3dbaa2fda99a3cc1a02afd8dfc67ba3cc70424
    role: context
  - path: reviews/structured/20261022T074158Z-holdfast-audit/review.yaml
    sha256: b16e3690ce05de283b917f4beaaf377ec0f7b6666ab3b282801b7815fbb317b2
    role: context
  - path: reviews/structured/20261022T074159Z-hops-complex-audit/review.md
    sha256: 6fcc43a8c269900a23e1f801b115291ad5476f9a68faad9469f6fdc59777162e
    role: context
  - path: reviews/structured/20261022T074159Z-hops-complex-audit/review.yaml
    sha256: 18bb2f6e2b46e471e510a12d97a8bc34a3a7c8e725f12c6ffb4fb1740ce87627
    role: context
  - path: reviews/structured/20261022T074159Z-hsp78-chaperone-complex-audit/review.md
    sha256: 941ccaf4fb3b824746527456e8303e352fa54248c89443e4ed90b6ccbd0672ed
    role: context
  - path: reviews/structured/20261022T074159Z-hsp78-chaperone-complex-audit/review.yaml
    sha256: f068e79c710ace752becfe6eac9e0a040f51ede92bc849c874552663101e5280
    role: context
  - path: reviews/structured/20261022T074200Z-hyphal-tip-audit/review.md
    sha256: 1341dee055e15e46b34178e0f2ac5fc603f885410cb8066667052d2cb9417ba5
    role: context
  - path: reviews/structured/20261022T074200Z-hyphal-tip-audit/review.yaml
    sha256: deddbb7e7a0b47169c07440a8cd69f5d306c99bdb5528f852f067f4eb9b352dc
    role: context
  - path: reviews/structured/20261022T074201Z-hyphal-tip-polarisome-audit/review.md
    sha256: e1d34804c31506a04a8b4c090e64e3b83cdce576f9b36e762fe375cda7ef9236
    role: context
  - path: reviews/structured/20261022T074201Z-hyphal-tip-polarisome-audit/review.yaml
    sha256: b293319350cfdbf9c3edb6cafd0223e7933045f83564ff8e61a976fe7ebd3160
    role: context
  - path: reviews/structured/20261022T074201Z-i-aaa-complex-audit/review.md
    sha256: c82d78187baba3a9b35cceb53cb9a47adcb80f7a2df841cdb396743ffc3ebea6
    role: context
  - path: reviews/structured/20261022T074201Z-i-aaa-complex-audit/review.yaml
    sha256: d8137bbaecb76afcdb935654cb4ab466e8e63666a92dfbc82730a785a8568aeb
    role: context
  - path: reviews/structured/20261022T074202Z-ino80-complex-audit/review.md
    sha256: b686ac53af7b90c80839456c1c0668adf9f70182cd3df9b53cc47920d5e379ea
    role: context
  - path: reviews/structured/20261022T074202Z-ino80-complex-audit/review.yaml
    sha256: 90eddd1c07af6b359bede56e055de61f474e0840b1fe19abac5df75072b45035
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
- target_id: GO:0070823
  path: data/structures/other/hda1_complex.yaml
  label: HDA1 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda1_complex.yaml
    role: maintained scientific record
- target_id: GO:1990085
  path: data/structures/other/hda_beta_clamp_complex.yaml
  label: Hda-beta clamp complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda_beta_clamp_complex.yaml
    role: maintained scientific record
- target_id: GO:0000417
  path: data/structures/other/hir_complex.yaml
  label: HIR complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hir_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:holdfast
  path: data/structures/other/holdfast.yaml
  label: holdfast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/holdfast.yaml
    role: maintained scientific record
- target_id: GO:0030897
  path: data/structures/other/hops_complex.yaml
  label: HOPS complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hops_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:hsp78_chaperone_complex
  path: data/structures/other/hsp78_chaperone_complex.yaml
  label: Hsp78 chaperone complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hsp78_chaperone_complex.yaml
    role: maintained scientific record
- target_id: GO:0001411
  path: data/structures/other/hyphal_tip.yaml
  label: hyphal tip
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
- target_id: GO:0031562
  path: data/structures/other/hyphal_tip_polarisome.yaml
  label: hyphal tip polarisome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip_polarisome.yaml
    role: maintained scientific record
- target_id: GO:0031942
  path: data/structures/other/i_aaa_complex.yaml
  label: i-AAA complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/i_aaa_complex.yaml
    role: maintained scientific record
- target_id: GO:0031011
  path: data/structures/other/ino80_complex.yaml
  label: Ino80 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ino80_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main d4d24c6c38d06ef27a6bac2c25ed381d50e96431.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    a1efd4e9ec612b402ce4ffdf9a65ffafc137cddb.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head f5668d26c554ec2f62610183aed5c5bc3aa76826.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head f5668d26c554ec2f62610183aed5c5bc3aa76826.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Native TraitMech check passed: all 10 links resolve with matching labels
    against the 1130-trait source index.'
  scope_note: Actual local execution at main-merge head f5668d26c554ec2f62610183aed5c5bc3aa76826.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  command: just vendored-check
  exit_code: 0
  summary: All 22 governed artifacts match the pinned CLAW revision.
  scope_note: Actual local execution at main-merge head f5668d26c554ec2f62610183aed5c5bc3aa76826.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    all 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head f5668d26c554ec2f62610183aed5c5bc3aa76826.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0070823
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just validate data/structures/other/hda1_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0070823
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: just validate-strict data/structures/other/hda1_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:1990085
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just validate data/structures/other/hda_beta_clamp_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:1990085
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: just validate-strict data/structures/other/hda_beta_clamp_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0000417
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just validate data/structures/other/hir_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0000417
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just validate-strict data/structures/other/hir_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate cellstructuremech:holdfast
  status: passed
  required: true
  target_ids:
  - cellstructuremech:holdfast
  command: just validate data/structures/other/holdfast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict cellstructuremech:holdfast
  status: passed
  required: true
  target_ids:
  - cellstructuremech:holdfast
  command: just validate-strict data/structures/other/holdfast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0030897
  status: passed
  required: true
  target_ids:
  - GO:0030897
  command: just validate data/structures/other/hops_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0030897
  status: passed
  required: true
  target_ids:
  - GO:0030897
  command: just validate-strict data/structures/other/hops_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate cellstructuremech:hsp78_chaperone_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  command: just validate data/structures/other/hsp78_chaperone_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict cellstructuremech:hsp78_chaperone_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  command: just validate-strict data/structures/other/hsp78_chaperone_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0001411
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just validate data/structures/other/hyphal_tip.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0001411
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: just validate-strict data/structures/other/hyphal_tip.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0031562
  status: passed
  required: true
  target_ids:
  - GO:0031562
  command: just validate data/structures/other/hyphal_tip_polarisome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0031562
  status: passed
  required: true
  target_ids:
  - GO:0031562
  command: just validate-strict data/structures/other/hyphal_tip_polarisome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0031942
  status: passed
  required: true
  target_ids:
  - GO:0031942
  command: just validate data/structures/other/i_aaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0031942
  status: passed
  required: true
  target_ids:
  - GO:0031942
  command: just validate-strict data/structures/other/i_aaa_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0031011
  status: passed
  required: true
  target_ids:
  - GO:0031011
  command: just validate data/structures/other/ino80_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0031011
  status: passed
  required: true
  target_ids:
  - GO:0031011
  command: just validate-strict data/structures/other/ino80_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394
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
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  summary: All ten positive molecular narratives trigger structured-source applicability.
    The complete fresh official iModulonDB catalogue contains 20 organism rows and
    28 organism/dataset pairs. It lacks the named yeast, Neurospora and Caulobacter
    biological hosts; recombinant E. coli expression hosts are not proxies. For the
    Hda-beta clamp record, e_coli/precise1k contains exact hda/b2496/P69931 and dnaN/b3701/P0A988
    matches; both have zero thresholded memberships among 201 modules. The 4257-gene,
    1035-sample, 518-condition, five-strain dataset is expression context, not the
    Kurz assay preparation or evidence of physical assembly or biological absence.
    Historical runner PermissionError retains its actual November3 timestamp; fresh
    native packets have their own access times.
  evidence_ids:
  - micro-adapter-catalogue-fresh
  - micro-adapter-precise1k-meta-fresh
  - micro-adapter-precise1k-genes-fresh
  - micro-adapter-precise1k-modules-fresh
  - micro-adapter-membership-b2496
  - micro-adapter-membership-b3701
  - plaque-catalogue
  - septin-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-graph-policy
  - micro-native-policy
  - micro-native-config
  - micro-protein-P53973-fresh
  - micro-protein-Q06629-fresh
  - micro-protein-Q06623-fresh
  - micro-protein-P69931-fresh
  - micro-protein-P0A988-fresh
  - micro-protein-P32479-fresh
  - micro-protein-P32480-fresh
  - micro-protein-P47171-fresh
  - micro-protein-Q01448-fresh
  - micro-tax-4932-fresh
  - micro-tax-559292-fresh
  - micro-tax-562-fresh
  - micro-tax-83333-fresh
  - micro-ena-tax-4932
  - micro-ena-tax-559292
  - micro-ena-tax-562
  - micro-ena-tax-83333
  - micro-go-0000118-fresh
  - micro-go-0000417-fresh
  - micro-go-0000785-fresh
  - micro-go-0004407-fresh
  - micro-go-0006334-fresh
  - micro-go-0032297
  - micro-go-0032991-fresh
  - micro-go-0044775-fresh
  - micro-go-0070823-fresh
  - micro-go-1990078-fresh
  - micro-go-1990083-fresh
  - micro-go-1990085-fresh
  - micro-ancestors-0000417-fresh
  - micro-ancestors-0070823-fresh
  - micro-ancestors-1990085-fresh
  - micro-family-IPR017321-fresh
  - micro-family-IPR026216-fresh
  - micro-family-IPR017788-fresh
  - micro-family-IPR022864-fresh
  - micro-family-IPR033053-fresh
  - micro-family-IPR021006
  - micro-family-IPR000286
  - micro-family-IPR031120
  - micro-family-IPR014840
  - micro-doi-0-fresh
  - micro-doi-1-fresh
  - micro-doi-3-fresh
  - micro-doi-4-fresh
  - micro-pmid-11287668-fresh
  - micro-pmid-11782447
  - micro-pmid-12618445
  - micro-pmid-14562095
  - micro-pmid-15150238-fresh
  - micro-pmid-16303565-fresh
  - micro-pmid-17180700-fresh
  - micro-pmid-19683497
  - micro-pmid-23994470
  - micro-pmid-8417331
  - micro-pmid-8663039-fresh
  - micro-pmid-9671488
  - micro-carmen-doi
  - micro-PMC31845-legacy
  - micro-PMC415757-legacy
  - micro-PMC2819815-legacy
  - micro-adapter-precise1k-meta-fresh
  - micro-adapter-precise1k-modules-fresh
  - plaque-curation
  - plaque-schema
  - plaque-profile
  - plaque-review-skill
  - plaque-protein-skill
  - plaque-graph-skill
  - plaque-go-0030897
  - plaque-go-0098796
  - plaque-go-0042144
  - plaque-go-0000329
  - plaque-go-0101031
  - plaque-go-0005759
  - plaque-go-0140545
  - plaque-go-0016887
  - plaque-go-0031942
  - plaque-go-0098800
  - plaque-go-0005743
  - plaque-go-0004176
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-up-P12868
  - plaque-up-Q03308
  - plaque-up-P27801
  - plaque-up-P20795
  - plaque-up-Q07468
  - plaque-up-P38959
  - plaque-up-P32939
  - plaque-up-P33416
  - plaque-up-P32795
  - plaque-up-P25573
  - plaque-up-Q04472
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR016902
  - plaque-ipr-IPR013911
  - plaque-ipr-IPR040201
  - plaque-ipr-IPR005936
  - plaque-ipr-IPR048438
  - plaque-ipr-IPR001270
  - plaque-ipr-IPR050130
  - plaque-ipr-protein-P33416
  - plaque-ipr-protein-P32795
  - plaque-pmid-10944212
  - plaque-pmid-9362071
  - plaque-pmid-36115461
  - plaque-pmid-29138251
  - plaque-pmid-14562095
  - plaque-pmid-14576278
  - plaque-pmid-16267274
  - plaque-pmid-8355690
  - plaque-pmid-8688560
  - plaque-PMC16876-body
  - plaque-PMC25710-body
  - plaque-PMC9574514-s3
  - plaque-PMC5748973-s3
  - plaque-PMC5748973-JCB_201702125_TableS1
  - plaque-PMC9574514-gr1
  - plaque-PMC9574514-gr2
  - plaque-PMC5748973-JCB_201702125_Fig3
  - plaque-pride-PXD030405
  - plaque-pride-PXD030436
  - plaque-cpx-1655
  - plaque-chebi-29105
  - plaque-eco-0005547
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-review-schema
  - septin-up-P27343
  - septin-up-A0A0H3CE47
  - septin-up-Q45977
  - septin-up-P27342
  - septin-tax-565050
  - septin-tax-190650
  - septin-tax-155892
  - septin-up-V5IQM7
  - septin-up-Q7RVZ1
  - septin-up-Q7RWH7
  - septin-tax-5141
  - septin-tax-367110
  - septin-up-P43579
  - septin-up-P53946
  - septin-up-Q03940
  - septin-up-Q03435
  - septin-up-Q12345
  - septin-up-P35189
  - septin-up-P60010
  - septin-up-P40154
  - septin-up-Q12386
  - septin-up-P32617
  - septin-up-P80428
  - septin-up-P40060
  - septin-up-P53115
  - septin-up-Q12464
  - septin-up-Q08561
  - septin-tax-4932
  - septin-tax-559292
  - septin-pmid-19355820
  - septin-pmid-19355820-abstract
  - septin-pmid-12887900
  - septin-pmid-12887900-abstract
  - septin-pmid-10787406
  - septin-pmid-10787406-abstract
  - septin-pmid-8573785
  - septin-pmid-8573785-abstract
  - septin-pmid-15525518
  - septin-pmid-15525518-abstract
  - septin-pmid-11604509
  - septin-pmid-11604509-abstract
  - septin-pmid-10952318
  - septin-pmid-10952318-abstract
  - septin-pmid-14562095
  - septin-pmid-14562095-abstract
  - septin-pmid-24034245
  - septin-pmid-24034245-abstract
  - septin-pmid-25964121
  - septin-pmid-25964121-abstract
  - septin-go
  - septin-go-0001411-ancestors
  - septin-go-0031562-ancestors
  - septin-go-0031011-ancestors
  - septin-sulkowski-metadata
  - septin-sulkowski-metadata-abstract
  - septin-hershey-metadata
  - septin-hershey-metadata-abstract
  - septin-sprecher-metadata
  - septin-sprecher-metadata-abstract
  - septin-lichius-metadata
  - septin-lichius-metadata-abstract
  - septin-watanabe-metadata
  - septin-watanabe-metadata-abstract
  - septin-ipr-IPR038014
  - septin-ipr-IPR029523
  - septin-ipr-IPR062650
  - septin-ipr-IPR020366
  - septin-ipr-IPR029525
  - septin-ipr-IPR050520
  - septin-ipr-IPR039892
  - septin-ipr-IPR051825
  - septin-ipr-IPR051661
  - septin-retry-IPR027238
  - septin-retry-IPR004000
  - septin-retry-IPR016665
  - septin-retry-IPR050342
  - septin-sulkowski-xml
  - septin-sprecher-xml
  - septin-lichius-xml
  - septin-watanabe-body
  - septin-watanabe-supplement
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
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
- check_id: hda1_complex-uniprot-verify
  name: Native HDA1 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hda1_complex-uniprot-verify
- check_id: hda1_complex-uniprot-causal
  name: Native HDA1 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0070823
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hda1_complex-uniprot-causal
- check_id: hda_beta_clamp_complex-uniprot-verify
  name: Native Hda-beta clamp complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hda_beta_clamp_complex-uniprot-verify
- check_id: hda_beta_clamp_complex-uniprot-causal
  name: Native Hda-beta clamp complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990085
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hda_beta_clamp_complex-uniprot-causal
- check_id: hir_complex-uniprot-verify
  name: Native HIR complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hir_complex-uniprot-verify
- check_id: hir_complex-uniprot-causal
  name: Native HIR complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hir_complex-uniprot-causal
- check_id: holdfast-uniprot-verify
  name: Native holdfast UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:holdfast
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/holdfast.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-holdfast-uniprot-verify
- check_id: holdfast-uniprot-causal
  name: Native holdfast UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:holdfast
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/holdfast.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-holdfast-uniprot-causal
- check_id: hops_complex-uniprot-verify
  name: Native HOPS complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030897
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hops_complex.yaml
    --verify
  exit_code: 0
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hops_complex-uniprot-verify
- check_id: hops_complex-uniprot-causal
  name: Native HOPS complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030897
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hops_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hops_complex-uniprot-causal
- check_id: hsp78_chaperone_complex-uniprot-verify
  name: Native Hsp78 chaperone complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hsp78_chaperone_complex.yaml
    --verify
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hsp78_chaperone_complex-uniprot-verify
- check_id: hsp78_chaperone_complex-uniprot-causal
  name: Native Hsp78 chaperone complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hsp78_chaperone_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hsp78_chaperone_complex-uniprot-causal
- check_id: hyphal_tip-uniprot-verify
  name: Native hyphal tip UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hyphal_tip-uniprot-verify
- check_id: hyphal_tip-uniprot-causal
  name: Native hyphal tip UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0001411
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hyphal_tip.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hyphal_tip-uniprot-causal
- check_id: hyphal_tip_polarisome-uniprot-verify
  name: Native hyphal tip polarisome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031562
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hyphal_tip_polarisome.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hyphal_tip_polarisome-uniprot-verify
- check_id: hyphal_tip_polarisome-uniprot-causal
  name: Native hyphal tip polarisome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031562
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hyphal_tip_polarisome.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-hyphal_tip_polarisome-uniprot-causal
- check_id: i_aaa_complex-uniprot-verify
  name: Native i-AAA complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031942
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/i_aaa_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-i_aaa_complex-uniprot-verify
- check_id: i_aaa_complex-uniprot-causal
  name: Native i-AAA complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031942
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/i_aaa_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-i_aaa_complex-uniprot-causal
- check_id: ino80_complex-uniprot-verify
  name: Native Ino80 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031011
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ino80_complex.yaml
    --verify
  exit_code: 0
  summary: 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ino80_complex-uniprot-verify
- check_id: ino80_complex-uniprot-causal
  name: Native Ino80 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031011
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ino80_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ino80_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/hda1_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90;
    current SHA256 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90.
    Record bytes unchanged since the original review.
  snapshot_sha256: 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 6802461abd98d8f664006cf9565d3d54b0ccb8571a1f4d7d7fbbb0e73bfb6801
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/hda_beta_clamp_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb;
    current SHA256 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb.
    Record bytes unchanged since the original review.
  snapshot_sha256: 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T074157Z-hda-beta-clamp-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d1c8b27d6d3791d717a71e3f133f2ac4cae17e105393786bd68909e34d781794
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/hir_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52;
    current SHA256 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52.
    Record bytes unchanged since the original review.
  snapshot_sha256: 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 25f3189b1167801e98e7100f04581c3046aa690607b5fed3a516a735f803807f
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/holdfast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862;
    current SHA256 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T074158Z-holdfast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b16e3690ce05de283b917f4beaaf377ec0f7b6666ab3b282801b7815fbb317b2
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/hops_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f;
    current SHA256 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f.
    Record bytes unchanged since the original review.
  snapshot_sha256: 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T074159Z-hops-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 18bb2f6e2b46e471e510a12d97a8bc34a3a7c8e725f12c6ffb4fb1740ce87627
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/hsp78_chaperone_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262;
    current SHA256 ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262.
    Record bytes unchanged since the original review.
  snapshot_sha256: ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T074159Z-hsp78-chaperone-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f068e79c710ace752becfe6eac9e0a040f51ede92bc849c874552663101e5280
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/hyphal_tip.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4;
    current SHA256 d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4.
    Record bytes unchanged since the original review.
  snapshot_sha256: d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T074200Z-hyphal-tip-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: deddbb7e7a0b47169c07440a8cd69f5d306c99bdb5528f852f067f4eb9b352dc
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/hyphal_tip_polarisome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667;
    current SHA256 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667.
    Record bytes unchanged since the original review.
  snapshot_sha256: 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T074201Z-hyphal-tip-polarisome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b293319350cfdbf9c3edb6cafd0223e7933045f83564ff8e61a976fe7ebd3160
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/i_aaa_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 4d6022b40a8f3933519d560a757641a771e17679d410cca43f010bebe3093a53;
    current SHA256 f6877406ef9d82f3c18666e77b2ae3bb8c0a8c8c582c35bfba92d7cffafacda9.
    Changed record reassessed against current sources.
  snapshot_sha256: f6877406ef9d82f3c18666e77b2ae3bb8c0a8c8c582c35bfba92d7cffafacda9
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T074201Z-i-aaa-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d8137bbaecb76afcdb935654cb4ab466e8e63666a92dfbc82730a785a8568aeb
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/ino80_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Original frozen SHA256 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4;
    current SHA256 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T074202Z-ino80-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T12:42:11Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 90eddd1c07af6b359bede56e055de61f474e0840b1fe19abac5df75072b45035
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/hda1_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T12:34:53.933091Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: 6b19f4b66623b018af2496a92442c707fecaf0e551591afaff220957c2bb7b90
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml
  locator: Complete immutable original YAML plus native deterministic Markdown
  accessed_at: '2026-11-04T12:34:53.933173Z'
  support: context_only
  summary: Original findings/actions/evidence/verdict and historical source claims
    independently audited; original access tiers are not retrospectively upgraded.
  snapshot_sha256: 6802461abd98d8f664006cf9565d3d54b0ccb8571a1f4d7d7fbbb0e73bfb6801
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/0-stale.diff
  locator: Exact git diff from original frozen revision to reviewed main
  accessed_at: '2026-11-04T12:34:53.933208Z'
  support: context_only
  summary: No record delta; historical target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/hda_beta_clamp_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T12:34:53.933231Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: 17d71a8e1991caf8baa03ec95079930ae623433d2f04a1c063211c4b127f4bfb
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T074157Z-hda-beta-clamp-complex-audit/review.yaml
  locator: Complete immutable original YAML plus native deterministic Markdown
  accessed_at: '2026-11-04T12:34:53.933252Z'
  support: context_only
  summary: Original findings/actions/evidence/verdict and historical source claims
    independently audited; original access tiers are not retrospectively upgraded.
  snapshot_sha256: d1c8b27d6d3791d717a71e3f133f2ac4cae17e105393786bd68909e34d781794
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/1-stale.diff
  locator: Exact git diff from original frozen revision to reviewed main
  accessed_at: '2026-11-04T12:34:53.933283Z'
  support: context_only
  summary: No record delta; historical target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/hir_complex.yaml
  locator: Entire current maintained record at source HEAD
  accessed_at: '2026-11-04T12:34:53.933303Z'
  support: context_only
  summary: Every identity, component/example, evidence, function, taxon, graph edge,
    discussion and history field read. Current bytes equal original frozen target;
    no stale refresh required.
  snapshot_sha256: 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml
  locator: Complete immutable original YAML plus native deterministic Markdown
  accessed_at: '2026-11-04T12:34:53.933326Z'
  support: context_only
  summary: Original findings/actions/evidence/verdict and historical source claims
    independently audited; original access tiers are not retrospectively upgraded.
  snapshot_sha256: 25f3189b1167801e98e7100f04581c3046aa690607b5fed3a516a735f803807f
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/2-stale.diff
  locator: Exact git diff from original frozen revision to reviewed main
  accessed_at: '2026-11-04T12:34:53.933361Z'
  support: context_only
  summary: No record delta; historical target and current main byte-identical.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components, evidence and Discussions sections
  accessed_at: '2026-11-04T12:34:53.933387Z'
  support: context_only
  summary: Specific class grounding is separate from organism examples; named paralogs
    are not automatically interchangeable; dated rationale is append-only and current
    notes can record progress.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum and causal graph slots
  accessed_at: '2026-11-04T12:34:53.933415Z'
  support: context_only
  summary: UNKNOWN remains valid when universal formation necessity is not established;
    a complex can be a structural constituent.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scopes and evidence contract
  accessed_at: '2026-11-04T12:34:53.933450Z'
  support: context_only
  summary: Scoped NONMECHANISTIC graphs need not be full assembly pathways. Function,
    physical association, localization and universal necessity differ.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Full review and source-native structured applicability workflow
  accessed_at: '2026-11-04T12:34:53.933470Z'
  support: context_only
  summary: Positive protein/pathway assertions trigger applicability assessment even
    without an expression-specific claim.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-native-config
  kind: authority
  reference: conf/record_review.yaml
  locator: Full configured checks/rubrics
  accessed_at: '2026-11-04T12:34:53.933490Z'
  support: context_only
  summary: Current native configuration inspected; this scratch preflight does not
    certify later root gates.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/original-audit.json
  locator: Six actual original native validate/render commands,42 historical input
    occurrences,six original artifacts
  accessed_at: '2026-11-04T12:26:13.490553Z'
  support: supports
  summary: All passed; original pairs render byte-identically and original PR artifacts
    are immutable. Historical declared inputs match source revisions/hashes.
  snapshot_sha256: 08f38b20a22fa5103e87f23b6bd69e434c6b2799bd6e5ec8c51f1e8b606fd996
- evidence_id: micro-protein-P53973-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53973.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P53973-fresh.raw
  accessed_at: '2026-11-04T12:24:23.487442Z'
  support: supports
  summary: 'P53973: UniProtKB reviewed (Swiss-Prot); Histone deacetylase HDA1; taxon
    559292; gene fields [{''geneName'': {''value'': ''HDA1''}, ''orderedLocusNames'':
    [{''value'': ''YNL021W''}], ''orfNames'': [{''value'': ''N2819''}]}]; InterPro
    references [''IPR019154'', ''IPR000286'', ''IPR023801'', ''IPR037138'', ''IPR017321'',
    ''IPR023696'']. Native localization/citation annotations are distinguished from
    independently read primary body evidence and actual experimental strains.'
  snapshot_sha256: e50191724ca3e786967c7b5ce8763d21fac7d51e9223d3f56c17a31de328b92c
- evidence_id: micro-protein-Q06629-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q06629.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-Q06629-fresh.raw
  accessed_at: '2026-11-04T12:24:27.569098Z'
  support: supports
  summary: 'Q06629: UniProtKB reviewed (Swiss-Prot); HDA1 complex subunit 2; taxon
    559292; gene fields [{''geneName'': {''value'': ''HDA2''}, ''synonyms'': [{''value'':
    ''PLO2''}], ''orderedLocusNames'': [{''value'': ''YDR295C''}]}]; InterPro references
    [''IPR038609'', ''IPR021006'']. Native localization/citation annotations are distinguished
    from independently read primary body evidence and actual experimental strains.'
  snapshot_sha256: c95cc08c295d630c447171a145ae4619f8ead6254b1e4cf7810d65d507b76479
- evidence_id: micro-protein-Q06623-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q06623.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-Q06623-fresh.raw
  accessed_at: '2026-11-04T12:24:25.479386Z'
  support: supports
  summary: 'Q06623: UniProtKB reviewed (Swiss-Prot); HDA1 complex subunit 3; taxon
    559292; gene fields [{''geneName'': {''value'': ''HDA3''}, ''synonyms'': [{''value'':
    ''PLO1''}], ''orderedLocusNames'': [{''value'': ''YPR179C''}]}]; InterPro references
    [''IPR038609'', ''IPR021006'', ''IPR026216'']. Native localization/citation annotations
    are distinguished from independently read primary body evidence and actual experimental
    strains.'
  snapshot_sha256: 5a71ecc7341f2b1495a8c62bce3fcbea0022bdb71b629f8db1bd9f4fd1a24420
- evidence_id: micro-protein-P69931-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P69931.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P69931-fresh.raw
  accessed_at: '2026-11-04T12:24:22.539976Z'
  support: supports
  summary: 'P69931: UniProtKB reviewed (Swiss-Prot); DnaA regulatory inactivator Hda;
    taxon 83333; gene fields [{''geneName'': {''value'': ''hda''}, ''synonyms'': [{''value'':
    ''idaB''}, {''value'': ''yfgE''}], ''orderedLocusNames'': [{''value'': ''b2496''},
    {''value'': ''JW5397''}], ''orfNames'': [{''value'': ''f248c''}]}]; InterPro references
    [''IPR020591'', ''IPR013317'', ''IPR017788'', ''IPR022864'', ''IPR055199'', ''IPR027417''].
    Native localization/citation annotations are distinguished from independently
    read primary body evidence and actual experimental strains.'
  snapshot_sha256: 426a92b935654ddf255d7bb462d2bd0bce6ab02033aed38b8e324916751c0b1d
- evidence_id: micro-protein-P0A988-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0A988.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P0A988-fresh.raw
  accessed_at: '2026-11-04T12:24:26.500624Z'
  support: supports
  summary: 'P0A988: UniProtKB reviewed (Swiss-Prot); Beta sliding clamp; taxon 83333;
    gene fields [{''geneName'': {''value'': ''dnaN''}, ''orderedLocusNames'': [{''value'':
    ''b3701''}, {''value'': ''JW3678''}]}]; InterPro references [''IPR046938'', ''IPR001001'',
    ''IPR022635'', ''IPR022637'', ''IPR022634'']. Native localization/citation annotations
    are distinguished from independently read primary body evidence and actual experimental
    strains.'
  snapshot_sha256: 41e5cead43ae6b73cc4fedfee2b9e111259e12f217532aba8590e487ea82f65f
- evidence_id: micro-protein-P32479-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32479.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P32479-fresh.raw
  accessed_at: '2026-11-04T12:24:24.536680Z'
  support: supports
  summary: 'P32479: UniProtKB reviewed (Swiss-Prot); Protein HIR1; taxon 559292; gene
    fields [{''geneName'': {''value'': ''HIR1''}, ''orderedLocusNames'': [{''value'':
    ''YBL008W''}], ''orfNames'': [{''value'': ''YBL0318''}]}]; InterPro references
    [''IPR055410'', ''IPR031120'', ''IPR011494'', ''IPR019015'', ''IPR015943'', ''IPR036322'',
    ''IPR001680'']. Native localization/citation annotations are distinguished from
    independently read primary body evidence and actual experimental strains.'
  snapshot_sha256: 10d8bcab99dd0a21e475c5d92360d1c1c7c61c979e35853b574817bf6abd9133
- evidence_id: micro-protein-P32480-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32480.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P32480-fresh.raw
  accessed_at: '2026-11-04T12:24:25.493553Z'
  support: supports
  summary: 'P32480: UniProtKB reviewed (Swiss-Prot); Protein HIR2; taxon 559292; gene
    fields [{''geneName'': {''value'': ''HIR2''}, ''orderedLocusNames'': [{''value'':
    ''YOR038C''}], ''orfNames'': [{''value'': ''OR26.31''}]}]; InterPro references
    [''IPR031120'', ''IPR011494'', ''IPR015943'', ''IPR036322'']. Native localization/citation
    annotations are distinguished from independently read primary body evidence and
    actual experimental strains.'
  snapshot_sha256: de54c92c878715d9d470fd56aab5a40c071883afef647b5345aba49683ac0a97
- evidence_id: micro-protein-P47171-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P47171.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-P47171-fresh.raw
  accessed_at: '2026-11-04T12:24:22.462765Z'
  support: supports
  summary: 'P47171: UniProtKB reviewed (Swiss-Prot); Histone transcription regulator
    3; taxon 559292; gene fields [{''geneName'': {''value'': ''HIR3''}, ''synonyms'':
    [{''value'': ''HPC1''}], ''orderedLocusNames'': [{''value'': ''YJR140C''}], ''orfNames'':
    [{''value'': ''J2161''}]}]; InterPro references [''IPR060091'', ''IPR033053'',
    ''IPR060094'', ''IPR060090'', ''IPR060092'', ''IPR063734'']. Native localization/citation
    annotations are distinguished from independently read primary body evidence and
    actual experimental strains.'
  snapshot_sha256: 0f569604566cce006a0e23abbf49142baca7c2aee06f2ba2684a54faea42d5bc
- evidence_id: micro-protein-Q01448-fresh
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q01448.json
  locator: Current status/name, entire primary/synonym/ordered-locus gene fields,
    organism, family links, SUBUNIT/FUNCTION/LOCATION and native citation provenance;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/protein-Q01448-fresh.raw
  accessed_at: '2026-11-04T12:24:23.499737Z'
  support: supports
  summary: 'Q01448: UniProtKB reviewed (Swiss-Prot); Histone promoter control protein
    2; taxon 559292; gene fields [{''geneName'': {''value'': ''HPC2''}, ''orderedLocusNames'':
    [{''value'': ''YBR215W''}], ''orfNames'': [{''value'': ''YBR1503''}]}]; InterPro
    references [''IPR014840'']. Native localization/citation annotations are distinguished
    from independently read primary body evidence and actual experimental strains.'
  snapshot_sha256: 7900b37c1697ed20e978396642a8a655d15283360f44ffec2869ebaaaa3454c6
- evidence_id: micro-query-HDA1-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HDA1-fresh.raw
  accessed_at: '2026-11-04T12:24:28.534626Z'
  support: supports
  summary: One current reviewed result ['P53973']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: 7da88f294fab60508ac10e385aa01f893bdcd109ac205710f49cc52ef030e780
  search_scope: UniProtKB; query (gene_exact:HDA1) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:28.534626Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-HDA2-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HDA2-fresh.raw
  accessed_at: '2026-11-04T12:24:29.630708Z'
  support: supports
  summary: One current reviewed result ['Q06629']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: f70e68b0e42f34d170def711100c9d8d122b4c13e00b4a7fcb402e46c7ee2010
  search_scope: UniProtKB; query (gene_exact:HDA2) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:29.630708Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-HDA3-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHDA3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HDA3-fresh.raw
  accessed_at: '2026-11-04T12:24:26.583060Z'
  support: supports
  summary: One current reviewed result ['Q06623']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: 795e8fbb802b47e30bc08a7f98e76bde37deaf7b16dbeeaa82e8d46546629a05
  search_scope: UniProtKB; query (gene_exact:HDA3) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:26.583060Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-HIR1-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HIR1-fresh.raw
  accessed_at: '2026-11-04T12:24:30.687416Z'
  support: supports
  summary: One current reviewed result ['P32479']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: b8becf3976e1f00de83f4e6604230c41697be4249efab0531814d582154e365b
  search_scope: UniProtKB; query (gene_exact:HIR1) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:30.687416Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-HIR2-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HIR2-fresh.raw
  accessed_at: '2026-11-04T12:24:28.796585Z'
  support: supports
  summary: One current reviewed result ['P32480']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: fa8be3811c9b11dbf4f1be47c71d43cfeead5bbf1abe3b1c118f7b2aa1c72532
  search_scope: UniProtKB; query (gene_exact:HIR2) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:28.796585Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-HIR3-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HIR3-fresh.raw
  accessed_at: '2026-11-04T12:24:29.538952Z'
  support: supports
  summary: One current reviewed result ['P47171']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: dbe73ca7bf8c6a1501d5fe1ee520ea140e4a253a8c3d705ed9cac3ce57dbd78e
  search_scope: UniProtKB; query (gene_exact:HIR3) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:29.538952Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-HPC2-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHPC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-HPC2-fresh.raw
  accessed_at: '2026-11-04T12:24:30.545522Z'
  support: supports
  summary: One current reviewed result ['Q01448']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: a2c8295ce6a030c468706b34f9ea4c5e8d29fa57c2e624dc089f03583ac65586
  search_scope: UniProtKB; query (gene_exact:HPC2) AND (organism_id:559292) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:30.545522Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-dnaN-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AdnaN%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-dnaN-fresh.raw
  accessed_at: '2026-11-04T12:24:27.567135Z'
  support: supports
  summary: One current reviewed result ['P0A988']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: 1887ae15fef4c0ae00bfb78438785bb21e2ed00e22c11ddbe95db13d89030426
  search_scope: UniProtKB; query (gene_exact:dnaN) AND (organism_id:83333) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:27.567135Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-query-hda-fresh
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Ahda%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete exact reviewed gene/taxon query, single returned page, total-result
    and next-link headers; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/query-hda-fresh.raw
  accessed_at: '2026-11-04T12:24:24.630946Z'
  support: supports
  summary: One current reviewed result ['P69931']; all native gene/alias/locus fields
    inspected and no next page. This reproduces a bounded current query, not the historic
    selection execution.
  snapshot_sha256: eb8af1bf9d21c98c3becc40e269fbb9fd003455df2925d8b91c12c8d659df4c1
  search_scope: UniProtKB; query (gene_exact:hda) AND (organism_id:83333) AND (reviewed:true);
    actual accessed_at 2026-11-04T12:24:24.630946Z; limit 500 records on first response;
    next-link inspected; current query does not reconstruct historical selection;
    exact complete returned response only, no broader absence inference.
- evidence_id: micro-tax-4932-fresh
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Native active taxon name/rank/parent and reference-strain scope; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-4932-fresh.raw
  accessed_at: '2026-11-04T12:24:21.347843Z'
  support: supports
  summary: '4932: Saccharomyces cerevisiae; active True; rank species. Yeast species
    versus S288C and E.coli species versus K-12 remain distinct from experiment preparations.'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
- evidence_id: micro-tax-559292-fresh
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Native active taxon name/rank/parent and reference-strain scope; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-559292-fresh.raw
  accessed_at: '2026-11-04T12:24:21.411388Z'
  support: supports
  summary: '559292: Saccharomyces cerevisiae (strain ATCC 204508 / S288c); active
    True; rank strain. Yeast species versus S288C and E.coli species versus K-12 remain
    distinct from experiment preparations.'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: micro-tax-562-fresh
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/562.json
  locator: Native active taxon name/rank/parent and reference-strain scope; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-562-fresh.raw
  accessed_at: '2026-11-04T12:24:21.422874Z'
  support: supports
  summary: '562: Escherichia coli; active True; rank species. Yeast species versus
    S288C and E.coli species versus K-12 remain distinct from experiment preparations.'
  snapshot_sha256: 20aa358053d2fae1e2cd74636ed5aca1efbc372e5b8bcfdb10d3fa80be6789a1
- evidence_id: micro-tax-83333-fresh
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Native active taxon name/rank/parent and reference-strain scope; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/tax-83333-fresh.raw
  accessed_at: '2026-11-04T12:24:21.598950Z'
  support: supports
  summary: '83333: Escherichia coli (strain K12); active True; rank strain. Yeast
    species versus S288C and E.coli species versus K-12 remain distinct from experiment
    preparations.'
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-ena-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-4932.raw
  accessed_at: '2026-11-04T12:25:58.992277Z'
  support: supports
  summary: Independent issuing taxonomy response corroborates exact named species/reference
    taxon. No experimental-strain identity follows from this authority alone.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: micro-ena-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-559292.raw
  accessed_at: '2026-11-04T12:25:58.992249Z'
  support: supports
  summary: Independent issuing taxonomy response corroborates exact named species/reference
    taxon. No experimental-strain identity follows from this authority alone.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro-ena-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-562.raw
  accessed_at: '2026-11-04T12:25:59.479047Z'
  support: supports
  summary: Independent issuing taxonomy response corroborates exact named species/reference
    taxon. No experimental-strain identity follows from this authority alone.
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: micro-ena-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Exact ENA taxonomy ID record and scientific-name/lineage fields; snapshot
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ena-tax-83333.raw
  accessed_at: '2026-11-04T12:25:59.470741Z'
  support: supports
  summary: Independent issuing taxonomy response corroborates exact named species/reference
    taxon. No experimental-strain identity follows from this authority alone.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro-go-0000118-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000118
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0000118-fresh.raw
  accessed_at: '2026-11-04T12:24:20.675583Z'
  support: supports
  summary: 'GO:0000118: histone deacetylase complex; isObsolete=False. Current identity
    and stated scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: f8768242e30c82c83d2b316ffe5c861027d43085d905bfadba6319c20d5eb6c8
- evidence_id: micro-go-0000417-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000417
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0000417-fresh.raw
  accessed_at: '2026-11-04T12:24:21.210191Z'
  support: supports
  summary: 'GO:0000417: HIR complex; isObsolete=False. Current identity and stated
    scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: be286c7062131162db1dc3920d7aefe8c905eccbcb51161f6bbf69c1a783d0a5
- evidence_id: micro-go-0000785-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000785
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0000785-fresh.raw
  accessed_at: '2026-11-04T12:24:20.741043Z'
  support: supports
  summary: 'GO:0000785: chromatin; isObsolete=False. Current identity and stated scope
    checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: 59374dae8a28c3857c401a898aed54a1d9133f1c35e4b23f548f4eb27b5a8d48
- evidence_id: micro-go-0004407-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0004407
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0004407-fresh.raw
  accessed_at: '2026-11-04T12:24:20.736880Z'
  support: supports
  summary: 'GO:0004407: histone deacetylase activity; isObsolete=False. Current identity
    and stated scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: d34e52cdda07b2819666ef4d1d1d5f5ad2ceae76221dc365ae993e9806ed3f82
- evidence_id: micro-go-0006334-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0006334
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0006334-fresh.raw
  accessed_at: '2026-11-04T12:24:21.201784Z'
  support: supports
  summary: 'GO:0006334: nucleosome assembly; isObsolete=False. Current identity and
    stated scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: 837eab3720834266809db7ebb3f979e5943908854ef991d4b65b0783d6ff0203
- evidence_id: micro-go-0032297
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032297
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0032297.raw
  accessed_at: '2026-11-04T12:25:58.869933Z'
  support: supports
  summary: 'GO:0032297: negative regulation of DNA-templated DNA replication initiation;
    isObsolete=False. Current identity and stated scope checked; GO definition is
    authority synthesis, not a new experiment.'
  snapshot_sha256: c73376493ff3e2bc86db2af907d7e2ff2b05b7188137d4a20fdc6ef7376bf876
- evidence_id: micro-go-0032991-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032991
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0032991-fresh.raw
  accessed_at: '2026-11-04T12:24:21.254350Z'
  support: supports
  summary: 'GO:0032991: protein-containing complex; isObsolete=False. Current identity
    and stated scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
- evidence_id: micro-go-0044775-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0044775
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0044775-fresh.raw
  accessed_at: '2026-11-04T12:24:20.760570Z'
  support: supports
  summary: 'GO:0044775: DNA polymerase III, beta sliding clamp processivity factor
    complex; isObsolete=False. Current identity and stated scope checked; GO definition
    is authority synthesis, not a new experiment.'
  snapshot_sha256: aab63fe0f13574e5cdb4285ac6c21025c42bd555213b4bdd48c4fe1328c9dba8
- evidence_id: micro-go-0070823-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0070823
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-0070823-fresh.raw
  accessed_at: '2026-11-04T12:24:20.608142Z'
  support: supports
  summary: 'GO:0070823: HDA1 complex; isObsolete=False. Current identity and stated
    scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: 9d9c78f5a5c34c71e739868ad09165a1903342a89c8a3390174308b61828f97b
- evidence_id: micro-go-1990078-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990078
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-1990078-fresh.raw
  accessed_at: '2026-11-04T12:24:20.612209Z'
  support: supports
  summary: 'GO:1990078: replication inhibiting complex; isObsolete=False. Current
    identity and stated scope checked; GO definition is authority synthesis, not a
    new experiment.'
  snapshot_sha256: 08c3d556dd3deeb3ca44662a13f9a1ec91fe795e9c1f611da59b212e417f7be7
- evidence_id: micro-go-1990083-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990083
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-1990083-fresh.raw
  accessed_at: '2026-11-04T12:24:20.836205Z'
  support: supports
  summary: 'GO:1990083: DnaA-Hda complex; isObsolete=False. Current identity and stated
    scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: d2f85f0916eaaed8c29b3898467c57d9f17770b9f5e1017b8069735db70f4e6b
- evidence_id: micro-go-1990085-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990085
  locator: Exact term ID/name/active state, definition, relationships and synonyms;
    snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/go-1990085-fresh.raw
  accessed_at: '2026-11-04T12:24:20.618850Z'
  support: supports
  summary: 'GO:1990085: Hda-beta clamp complex; isObsolete=False. Current identity
    and stated scope checked; GO definition is authority synthesis, not a new experiment.'
  snapshot_sha256: e0af87ab4d38b582534f2aaf03bf33758e35d33e546d1607bd6b93477ed6570e
- evidence_id: micro-ancestors-0000417-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0000417/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ancestors-0000417-fresh.raw
  accessed_at: '2026-11-04T12:24:21.320616Z'
  support: supports
  summary: 'GO:0000417: [''GO:0000417'', ''GO:0032991'', ''GO:0005575'']. Declared
    parent verified; parthood is assessed separately.'
  snapshot_sha256: e03bcdf4ed65c98e31ecfec94bda2aed0113ee595c088d03657013e660b46594
- evidence_id: micro-ancestors-0070823-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0070823/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ancestors-0070823-fresh.raw
  accessed_at: '2026-11-04T12:24:21.257856Z'
  support: supports
  summary: 'GO:0070823: [''GO:1902494'', ''GO:0140513'', ''GO:0000118'', ''GO:0032991'',
    ''GO:0070823'', ''GO:0005575'']. Declared parent verified; parthood is assessed
    separately.'
  snapshot_sha256: 536e5048998a508ae3656808f9a6a22e1560fb1b49b0b22ebfec3fb5dab7af49
- evidence_id: micro-ancestors-1990085-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A1990085/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/ancestors-1990085-fresh.raw
  accessed_at: '2026-11-04T12:24:21.321742Z'
  support: supports
  summary: 'GO:1990085: [''GO:1990078'', ''GO:0032991'', ''GO:1990085'', ''GO:0005575''].
    Declared parent verified; parthood is assessed separately.'
  snapshot_sha256: 79a887d523798106a919ec5ea9ad2ff992d366801e9c263cdc093ba67c98d66a
- evidence_id: micro-family-IPR017321-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017321/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR017321-fresh.raw
  accessed_at: '2026-11-04T12:24:22.236690Z'
  support: supports
  summary: 'IPR017321: Histone deacetylase class II, yeast; native type family. Exact
    constituent family corroborated by current reference-protein native xrefs. Domain
    prose is not used as primary experiment evidence.'
  snapshot_sha256: 6aa1d1d924b6c91decebcc7cd09ae8835f9c6e3e79963b9c0aeccba041ef213b
- evidence_id: micro-family-IPR026216-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR026216/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR026216-fresh.raw
  accessed_at: '2026-11-04T12:24:22.847331Z'
  support: supports
  summary: 'IPR026216: HDA1 complex subunit 3; native type family. Exact constituent
    family corroborated by current reference-protein native xrefs. Domain prose is
    not used as primary experiment evidence.'
  snapshot_sha256: a4c9bf5c6c00b7f375ec628e7de68503f5e89852c21c3243f1089eb3c83f0f05
- evidence_id: micro-family-IPR017788-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017788/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR017788-fresh.raw
  accessed_at: '2026-11-04T12:24:23.134478Z'
  support: supports
  summary: 'IPR017788: DnaA regulatory inactivator Hda; native type family. Exact
    Hda branch, distinct from DnaA sibling under the broader DnaA-like family.'
  snapshot_sha256: 7e9d3b5937bd2091b11b482deda5c5328592a0121f84c369e97a6ba8390abb6c
- evidence_id: micro-family-IPR022864-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022864/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR022864-fresh.raw
  accessed_at: '2026-11-04T12:24:23.154797Z'
  support: supports
  summary: 'IPR022864: DnaA regulatory inactivator Hda, Enterobacteriaceae; native
    type family. Enterobacteriaceae child of Hda; useful narrower reference context,
    not mandatory scope for the whole Hda class.'
  snapshot_sha256: a3300bce98be51679d5018b6ad7ad5dc4ad5108f0c7c19c006f084c8f43425f0
- evidence_id: micro-family-IPR033053-fresh
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033053/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR033053-fresh.raw
  accessed_at: '2026-11-04T12:24:23.551120Z'
  support: supports
  summary: 'IPR033053: Histone transcription regulator 3/CABIN1; native type family.
    Whole Hir3/CABIN1 homolog family spans fungal Hir3 and animal CABIN1; breadth
    is explicit, not a claim of identical HIR composition in all taxa.'
  snapshot_sha256: e3476a156c99f54de4db23f4815334b3faa11da85cc74bcff357aac18b8030c4
- evidence_id: micro-family-IPR021006
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021006/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR021006.raw
  accessed_at: '2026-11-04T12:25:58.767584Z'
  support: supports
  summary: 'IPR021006: HDA1 complex subunit 2/3; native type family. Shared Hda2/3
    family, with specific Hda3 child IPR026216; not an exact Hda2-only mapping.'
  snapshot_sha256: cd3f7ac1eda2c12e0e34aef59d59a330014c6373981bab6405ef0ebee027ac22
- evidence_id: micro-family-IPR000286
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000286/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR000286.raw
  accessed_at: '2026-11-04T12:25:58.767621Z'
  support: supports
  summary: 'IPR000286: Histone deacetylase HDAC; native type family. Broad deacetylase
    entry; not substituted for the yeast Hda1-specific class. Broad descriptive substrate
    claims do not replace direct Wu/Carmen assay scope.'
  snapshot_sha256: 65691d9d3d7eeb24628309fb3d164063dd7c60bd545eb804683db71cee53a88e
- evidence_id: micro-family-IPR031120
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031120/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR031120.raw
  accessed_at: '2026-11-04T12:25:58.842443Z'
  support: supports
  summary: 'IPR031120: WD repeat HIR1-like; native type family. Includes yeast Hir1/Hir2
    and animal HIRA; not treated as a uniquely Hir1-only or Hir2-only class.'
  snapshot_sha256: 8c7b01a95abd1f366529f1da46ab474ec3f486dd764c76e68ff45cc18172e5cb
- evidence_id: micro-family-IPR014840
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014840/
  locator: Complete metadata/type/name, native description, integrated signatures
    and family hierarchy; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/family-IPR014840.raw
  accessed_at: '2026-11-04T12:25:58.992202Z'
  support: supports
  summary: 'IPR014840: Hpc2-related domain; native type domain. Hpc2-related domain,
    not a verified whole Hpc2 protein family.'
  snapshot_sha256: 55a74a6761e80bc88bcd10dd75e5c1cc15a68b11d71131aeb4d38e697839f626
- evidence_id: micro-doi-0-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1073%2Fpnas.081560698%22&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-0-fresh.raw
  accessed_at: '2026-11-04T12:24:27.135341Z'
  support: context_only
  summary: HDA2 and HDA3 are related proteins that interact with and are essential
    for the activity of the yeast histone deacetylase HDA1.; PMID11287668, DOI10.1073/pnas.081560698;
    underlying primary article. Only indexed metadata/abstract read here; primary
    body access is separately specified. Localization provenance references do not
    independently establish membership.
  snapshot_sha256: 03c22341f2193b7ea878950fd9177a7fbebe07793e9996979fb68230dcb2d113
  search_scope: Europe PMC; query DOI:"10.1073/pnas.081560698"; actual accessed_at
    2026-11-04T12:24:27.135341Z; limit 10 exact-DOI results; complete returned metadata/abstract,
    not presumed full body; exact complete returned response only, no broader absence
    inference.
- evidence_id: micro-doi-1-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.271.26.15837%22&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-1-fresh.raw
  accessed_at: '2026-11-04T12:24:27.254999Z'
  support: context_only
  summary: HDA1 and HDA3 are components of a yeast histone deacetylase (HDA) complex.;
    PMID8663039, DOI10.1074/jbc.271.26.15837; underlying primary article. Only indexed
    metadata/abstract read here; primary body access is separately specified. Localization
    provenance references do not independently establish membership.
  snapshot_sha256: bd4b672f0dbcf54a76e603c6301335452f53da3c3ede82f31430de7e98605e80
  search_scope: Europe PMC; query DOI:"10.1074/jbc.271.26.15837"; actual accessed_at
    2026-11-04T12:24:27.254999Z; limit 10 exact-DOI results; complete returned metadata/abstract,
    not presumed full body; exact complete returned response only, no broader absence
    inference.
- evidence_id: micro-doi-3-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2005.10.053%22&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-3-fresh.raw
  accessed_at: '2026-11-04T12:24:27.933916Z'
  support: context_only
  summary: Replication-independent histone deposition by the HIR complex and Asf1.;
    PMID16303565, DOI10.1016/j.cub.2005.10.053; underlying primary article. Only indexed
    metadata/abstract read here; primary body access is separately specified. Localization
    provenance references do not independently establish membership.
  snapshot_sha256: ac33d6f39b9ce63401d65e1af4067d0d393e7140d106d3ef9edfaf6cf54b45da
  search_scope: Europe PMC; query DOI:"10.1016/j.cub.2005.10.053"; actual accessed_at
    2026-11-04T12:24:27.933916Z; limit 10 exact-DOI results; complete returned metadata/abstract,
    not presumed full body; exact complete returned response only, no broader absence
    inference.
- evidence_id: micro-doi-4-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00412-006-0087-z%22&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/doi-4-fresh.raw
  accessed_at: '2026-11-04T12:24:28.264346Z'
  support: context_only
  summary: The histone chaperone Asf1 at the crossroads of chromatin and DNA checkpoint
    pathways.; PMID17180700, DOI10.1007/s00412-006-0087-z; underlying secondary review.
    Only indexed metadata/abstract read here; primary body access is separately specified.
    Localization provenance references do not independently establish membership.
  snapshot_sha256: c3e38ba1e52e967dfc81566a3bf0487911c43762ebf51f9bf8d6cec94d779d9c
  search_scope: Europe PMC; query DOI:"10.1007/s00412-006-0087-z"; actual accessed_at
    2026-11-04T12:24:28.264346Z; limit 10 exact-DOI results; complete returned metadata/abstract,
    not presumed full body; exact complete returned response only, no broader absence
    inference.
- evidence_id: micro-pmid-11287668-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11287668+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-11287668-fresh.raw
  accessed_at: '2026-11-04T12:24:28.209944Z'
  support: context_only
  summary: HDA2 and HDA3 are related proteins that interact with and are essential
    for the activity of the yeast histone deacetylase HDA1.; PMID11287668, DOI10.1073/pnas.081560698;
    underlying primary article. Only indexed metadata/abstract read here; primary
    body access is separately specified. Localization provenance references do not
    independently establish membership.
  snapshot_sha256: f64de9b6c8d5357047e9ab55c3942414602a572011d0a177fcf9d85ed5e549e4
  search_scope: Europe PMC; query EXT_ID:11287668 AND SRC:MED; actual accessed_at
    2026-11-04T12:24:28.209944Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-11782447
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11782447+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-11782447.raw
  accessed_at: '2026-11-04T12:25:59.633170Z'
  support: context_only
  summary: Chromatin assembly factor I and Hir proteins contribute to building functional
    kinetochores in S. cerevisiae.; PMID11782447, DOI10.1101/gad.925302; underlying
    primary article. Only indexed metadata/abstract read here; primary body access
    is separately specified. Localization provenance references do not independently
    establish membership.
  snapshot_sha256: 3e9dec15c35471dec8b028d5caf0e6a52d8e9e5df35899fcc7da42b677112d4c
  search_scope: Europe PMC; query EXT_ID:11782447 AND SRC:MED; actual accessed_at
    2026-11-04T12:25:59.633170Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-12618445
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12618445+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-12618445.raw
  accessed_at: '2026-11-04T12:26:00.732680Z'
  support: context_only
  summary: Identification of a novel membrane-associated gene product that suppresses
    toxicity of a TrfA peptide from plasmid RK2 and its relationship to the DnaA host
    initiation protein.; PMID12618445, DOI10.1128/jb.185.6.1817-1824.2003; underlying
    primary article. Only indexed metadata/abstract read here; primary body access
    is separately specified. Localization provenance references do not independently
    establish membership.
  snapshot_sha256: 3fb10a34d2c2e076298ac23addce2277f5d50180ee3c7a00c14153252375d395
  search_scope: Europe PMC; query EXT_ID:12618445 AND SRC:MED; actual accessed_at
    2026-11-04T12:26:00.732680Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-14562095.raw
  accessed_at: '2026-11-04T12:25:59.476453Z'
  support: context_only
  summary: Global analysis of protein localization in budding yeast.; PMID14562095,
    DOI10.1038/nature02026; underlying primary article. Only indexed metadata/abstract
    read here; primary body access is separately specified. Localization provenance
    references do not independently establish membership.
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
  search_scope: Europe PMC; query EXT_ID:14562095 AND SRC:MED; actual accessed_at
    2026-11-04T12:25:59.476453Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-15150238-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15150238+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-15150238-fresh.raw
  accessed_at: '2026-11-04T12:24:28.548516Z'
  support: context_only
  summary: Interaction of the sliding clamp beta-subunit and Hda, a DnaA-related protein.;
    PMID15150238, DOI10.1128/jb.186.11.3508-3515.2004; underlying primary article.
    Only indexed metadata/abstract read here; primary body access is separately specified.
    Localization provenance references do not independently establish membership.
  snapshot_sha256: 172a39c1decf7071850da52fd439c228fc3dc383641bb40599cbe102af0e9fd5
  search_scope: Europe PMC; query EXT_ID:15150238 AND SRC:MED; actual accessed_at
    2026-11-04T12:24:28.548516Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-16303565-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16303565+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-16303565-fresh.raw
  accessed_at: '2026-11-04T12:24:28.860892Z'
  support: context_only
  summary: Replication-independent histone deposition by the HIR complex and Asf1.;
    PMID16303565, DOI10.1016/j.cub.2005.10.053; underlying primary article. Only indexed
    metadata/abstract read here; primary body access is separately specified. Localization
    provenance references do not independently establish membership.
  snapshot_sha256: 79ef3c2bd559eb234ee835497ed0213f70b3b5638d0f92ef1d58e491d7a4ddb4
  search_scope: Europe PMC; query EXT_ID:16303565 AND SRC:MED; actual accessed_at
    2026-11-04T12:24:28.860892Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-17180700-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17180700+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-17180700-fresh.raw
  accessed_at: '2026-11-04T12:24:28.965154Z'
  support: context_only
  summary: The histone chaperone Asf1 at the crossroads of chromatin and DNA checkpoint
    pathways.; PMID17180700, DOI10.1007/s00412-006-0087-z; underlying secondary review.
    Only indexed metadata/abstract read here; primary body access is separately specified.
    Localization provenance references do not independently establish membership.
  snapshot_sha256: 9d591efaafc6e8f2fa12057e7204c60731d4e449dd9ec08c19f0e0ef1b612468
  search_scope: Europe PMC; query EXT_ID:17180700 AND SRC:MED; actual accessed_at
    2026-11-04T12:24:28.965154Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-19683497
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19683497+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-19683497.raw
  accessed_at: '2026-11-04T12:25:59.631390Z'
  support: context_only
  summary: Two-color cell array screen reveals interdependent roles for histone chaperones
    and a chromatin boundary regulator in histone gene repression.; PMID19683497,
    DOI10.1016/j.molcel.2009.06.023; underlying primary article. Only indexed metadata/abstract
    read here; primary body access is separately specified. Localization provenance
    references do not independently establish membership.
  snapshot_sha256: 5cdf7d7a3a035eb29f0f4561ddaca6f173168a0c23f3c605c55297388cb891da
  search_scope: Europe PMC; query EXT_ID:19683497 AND SRC:MED; actual accessed_at
    2026-11-04T12:25:59.631390Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-23994470
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23994470+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-23994470.raw
  accessed_at: '2026-11-04T12:25:59.631335Z'
  support: context_only
  summary: A replicase clamp-binding dynamin-like protein promotes colocalization
    of nascent DNA strands and equipartitioning of chromosomes in E. coli.; PMID23994470,
    DOI10.1016/j.celrep.2013.07.040; underlying primary article. Only indexed metadata/abstract
    read here; primary body access is separately specified. Localization provenance
    references do not independently establish membership.
  snapshot_sha256: a52e86b020830d87a2ea365d3e749d8c0ce7061a4adf6d42af4fd9cb2a849586
  search_scope: Europe PMC; query EXT_ID:23994470 AND SRC:MED; actual accessed_at
    2026-11-04T12:25:59.631335Z; limit 10 exact-PMID results; complete returned metadata/abstract
    only; exact complete returned response only, no broader absence inference.
- evidence_id: micro-pmid-8417331
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8417331+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-8417331.raw
  accessed_at: '2026-11-04T12:26:00.915997Z'
  support: context_only
  summary: Characterization of HIR1 and HIR2, two genes required for regulation of
    histone gene transcription in Saccharomyces cerevisiae.; PMID8417331, DOI10.1128/mcb.13.1.28-38.1993;
    underlying primary article. Only indexed metadata/abstract read here; primary
    body access is separately specified. Localization provenance references do not
    independently establish membership.
  snapshot_sha256: f16a432051babd65faac5b8185c29aefea797369d49fdb6d514606200ab45796
  search_scope: Europe PMC; query EXT_ID:8417331 AND SRC:MED; actual accessed_at 2026-11-04T12:26:00.915997Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-pmid-8663039-fresh
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8663039+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-8663039-fresh.raw
  accessed_at: '2026-11-04T12:24:28.553071Z'
  support: context_only
  summary: HDA1 and HDA3 are components of a yeast histone deacetylase (HDA) complex.;
    PMID8663039, DOI10.1074/jbc.271.26.15837; underlying primary article. Only indexed
    metadata/abstract read here; primary body access is separately specified. Localization
    provenance references do not independently establish membership.
  snapshot_sha256: 0cc63ec8647b722e09514eaaf4136d64b6df300fe44954156ee5f9b5f2db5bc7
  search_scope: Europe PMC; query EXT_ID:8663039 AND SRC:MED; actual accessed_at 2026-11-04T12:24:28.553071Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-pmid-9671488
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9671488+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Exact PMID/DOI metadata, authors/year/article type and complete indexed
    abstract; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/pmid-9671488.raw
  accessed_at: '2026-11-04T12:26:00.323463Z'
  support: context_only
  summary: Yeast Ty1 retrotransposition is stimulated by a synergistic interaction
    between mutations in chromatin assembly factor I and histone regulatory proteins.;
    PMID9671488, DOI10.1128/mcb.18.8.4783; underlying primary article. Only indexed
    metadata/abstract read here; primary body access is separately specified. Localization
    provenance references do not independently establish membership.
  snapshot_sha256: 8da63450a793fe7fdcb358c99d856ac1129e123a13080bc7d3e21403b0bc2ea1
  search_scope: Europe PMC; query EXT_ID:9671488 AND SRC:MED; actual accessed_at 2026-11-04T12:26:00.323463Z;
    limit 10 exact-PMID results; complete returned metadata/abstract only; exact complete
    returned response only, no broader absence inference.
- evidence_id: micro-carmen-doi
  kind: database
  reference: https://doi.org/10.1074/jbc.271.26.15837
  locator: Current DOI content-negotiated Crossref metadata, title/PII and publisher
    resource links; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/carmen-doi.raw
  accessed_at: '2026-11-04T12:25:59.093780Z'
  support: context_only
  summary: Genuine bibliographic metadata only; not Carmen1996 body. Historical DOI
    redirect and publisher403 remain distinct old observations.
  snapshot_sha256: ce45cda9159ea5fe80b50a2673a3a0746a40eed51f4e89308e79542f440d9758
- evidence_id: micro-PMC31845-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC31845/?pdf=0
  locator: Genuine PMC HTML; complete Methods sec1–8 including Table1; Results/Discussion
    sec9–17, all Figures1–6 text captions; no pixels/supplements; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/PMC31845-legacy.raw
  accessed_at: '2026-11-04T12:25:58.104946Z'
  support: supports
  summary: Wu2001 directly supports Hda1 self-association, Hda2/Hda3 association and
    native Hda1-containing complex in YDS/WJY yeast preparations. Hydrodynamic299.2kDa
    estimate supports likely2:1:1 tetramer, not resolved atomic stoichiometry. Co-IP
    partner losses, activity loss, and ENA1-specific H3/H2B ChIP effects are separate
    observations; no universal histone/locus preference or formation-essentiality
    inferred.
  snapshot_sha256: 0ee6a32dc12fff94f00b8f3663bd123366562945f208be7d114016dc8fe3fbb7
- evidence_id: micro-PMC415757-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC415757/?pdf=0
  locator: Genuine PMC HTML; complete Methods sec1–10 including Table2; Results sec11–16
    with all Figures1–3/Table1; Discussion sec17; no pixels; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/PMC415757-legacy.raw
  accessed_at: '2026-11-04T12:25:58.105635Z'
  support: supports
  summary: Kurz2004 demonstrates purified Hda-beta binding by plate and pull-down
    assays, motif-dependent binding and peptide competition. XL1Blue-derived amplified
    genes and BL21(DE3)pLyS/TB1 expression/preparations are distinguished from reference
    K-12 annotation. The paper proposes RIDA relevance and cites prior ATP-hydrolysis
    studies; it does not newly measure the whole RIDA reaction. Mutant misfolding
    remains an explicit alternative.
  snapshot_sha256: b2d282715d5fe454e0d04d40044f62180f266b389701a904423fe5da25d62397
- evidence_id: micro-PMC2819815-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2819815/?pdf=0
  locator: Genuine PMC HTML; complete Results/Discussion S2–S6, Figures1–4 captions
    and main Experimental Procedures S7 pointer; no supplemental protocols/strain
    tables/pixels; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/PMC2819815-legacy.raw
  accessed_at: '2026-11-04T12:25:58.104847Z'
  support: supports
  summary: Green2005 purified Hir2-STAP complex identifies Hir1/Hir2/Hir3/Hpc2; Asf1
    is a cooperating partner. Conditional deletion/purification observations, promoter
    binding and in-vitro nucleosome assembly are distinguished. HIR alone can support
    histone deposition under tested conditions; efficient cooperation is not obligatory
    Asf1 membership. Hir3 loss from hpc2-deletion preparation does not distinguish
    failed association from protein instability.
  snapshot_sha256: 1dd99c9d85989bcd02f673152445a94784d65ff15166a3243e09db9b8e0bdb5e
- evidence_id: micro-historical-0-access-panther-PTHR31882-SF11
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR31882:SF11/
  locator: Retained immutable original evidence access-panther-PTHR31882-SF11 at reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml;
    historical status/diagnostic scope only
  accessed_at: '2026-10-22T07:18:52.670333Z'
  support: context_only
  summary: The candidate subfamily identified by Q06629 returned HTTP204 with an empty
    body; this route did not independently resolve its class boundary. Historical
    observation retained without fresh invocation or body-access upgrade; original
    primary_source kind is corrected to validation/context_only.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-historical-0-access-carmen1996-doi
  kind: validation
  reference: https://doi.org/10.1074/jbc.271.26.15837
  locator: Retained immutable original evidence access-carmen1996-doi at reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml;
    historical status/diagnostic scope only
  accessed_at: '2026-10-22T07:12:56.724441Z'
  support: context_only
  summary: The DOI resolved to an Elsevier redirect page naming the correct title
    and PII, without article body text. Historical observation retained without fresh
    invocation or body-access upgrade; original primary_source kind is corrected to
    validation/context_only.
  snapshot_sha256: 904124333ad441cefb964fba199f91bb7cf9eb82d36db393ccb9cda9448695a9
- evidence_id: micro-historical-0-access-carmen1996-jbc
  kind: validation
  reference: https://www.jbc.org/article/S0021-9258(18)36134-9/fulltext
  locator: Retained immutable original evidence access-carmen1996-jbc at reviews/structured/20261022T074156Z-hda1-complex-audit/review.yaml;
    historical status/diagnostic scope only
  accessed_at: '2026-10-22T07:18:53.284553Z'
  support: context_only
  summary: The publisher article route derived from the DOI PII returned HTTP403.
    Carmen1996 remains verified at native complete-abstract tier. Historical observation
    retained without fresh invocation or body-access upgrade; original primary_source
    kind is corrected to validation/context_only.
  snapshot_sha256: 7b96b333029e36921285ba0dc0602765fe24e8d39390887c60bd1a193286eca6
- evidence_id: micro-historical-2-access-panther-PTHR13831-SF0
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF0/
  locator: Retained immutable original evidence access-panther-PTHR13831-SF0 at reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml;
    historical status/diagnostic scope only
  accessed_at: '2026-10-22T07:18:52.670592Z'
  support: context_only
  summary: The reference-protein-linked candidate subfamily route returned HTTP204
    and no response body; this route does not independently resolve an exact Hir1/Hir2
    class boundary. Historical observation retained without fresh invocation or body-access
    upgrade; original primary_source kind is corrected to validation/context_only.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-historical-2-access-panther-PTHR13831-SF1
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF1/
  locator: Retained immutable original evidence access-panther-PTHR13831-SF1 at reviews/structured/20261022T074158Z-hir-complex-audit/review.yaml;
    historical status/diagnostic scope only
  accessed_at: '2026-10-22T07:18:53.270390Z'
  support: context_only
  summary: The reference-protein-linked candidate subfamily route returned HTTP204
    and no response body; this route does not independently resolve an exact Hir1/Hir2
    class boundary. Historical observation retained without fresh invocation or body-access
    upgrade; original primary_source kind is corrected to validation/context_only.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-access-PMC31845-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC31845.1/PMC31845.1.xml
  locator: Actual failed candidate S3 route and diagnostic body
  accessed_at: '2026-11-04T12:25:57.969475Z'
  support: context_only
  summary: HTTP404; no primary body at this route. Genuine later PMC HTML is separately
    read and does not retroactively upgrade this failure.
  snapshot_sha256: e5e9003d34b62db73590374a5b17a4071946ad1ee1a4b317fabdff279c1ccdd3
- evidence_id: micro-access-PMC415757-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC415757.1/PMC415757.1.xml
  locator: Actual failed candidate S3 route and diagnostic body
  accessed_at: '2026-11-04T12:25:57.969590Z'
  support: context_only
  summary: HTTP404; no primary body at this route. Genuine later PMC HTML is separately
    read and does not retroactively upgrade this failure.
  snapshot_sha256: 171d2e9169dd9a928594aebbd2d22e61a50c78b670be7eca117a22a669ae49fd
- evidence_id: micro-access-PMC2819815-jats
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2819815.1/PMC2819815.1.xml
  locator: Actual failed candidate S3 route and diagnostic body
  accessed_at: '2026-11-04T12:25:57.965907Z'
  support: context_only
  summary: HTTP404; no primary body at this route. Genuine later PMC HTML is separately
    read and does not retroactively upgrade this failure.
  snapshot_sha256: e0f7be09dc72669554aa18b2d476551e3f51cddf4bc7d23c3b36609d516cb072
- evidence_id: micro-adapter-catalogue-fresh
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete official organism/dataset catalogue; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-catalogue-fresh.raw
  accessed_at: '2026-11-04T12:24:20.225750Z'
  support: context_only
  summary: Complete20 organism rows and28 organism/dataset pairs inspected. No Saccharomyces
    host; no yeast proxy query. E.coli is represented and the actual precise1k packet
    is assessed for the Hda-beta narrative.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB catalogue; query GET /api/organisms; complete
    returned organism/dataset catalogue; actual accessed_at 2026-11-04T12:24:20.225750Z;
    limit One complete current JSON response; downstream only actual matching biological
    hosts; exact complete returned response only, no broader absence inference.
- evidence_id: micro-adapter-precise1k-meta-fresh
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Full selected e_coli/precise1k metadata; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-precise1k-meta-fresh.raw
  accessed_at: '2026-11-04T12:24:20.817816Z'
  support: context_only
  summary: Dataset has201 modules,4257 genes,1035 samples/518 conditions and five
    strains BW25113,DGF-298,GMOS,MG1655,W3110. This is a multistrain expression dataset,
    not the Kurz assay preparations or all E.coli.
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-adapter-precise1k-genes-fresh
  kind: search
  reference: https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=5000
  locator: Full4257-row table; exact hda/b2496 and dnaN/b3701 symbols/loci/UniProt
    joins; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-precise1k-genes-fresh.raw
  accessed_at: '2026-11-04T12:24:20.251112Z'
  support: context_only
  summary: Exact two rows map hda/b2496 to P69931 and dnaN/b3701 to P0A988; reference
    mapping is distinguished from primary experiment background. No substring/foreign-host
    substitution.
  snapshot_sha256: db4db81a724c8bee753c68fa5fefdd34f3d89e2cd101ae52311088f7cb094d27
  search_scope: Official iModulonDB; exact GET https://imodulondb.org/api/genes?organism=e_coli&dataset=precise1k&limit=5000;
    actual date 2026-11-04T12:24:20.251112Z; complete returned 4257-row e_coli/precise1k
    table under requested limit5000, exact hda/b2496 and dnaN/b3701 joins only. No
    broader absence inference.
- evidence_id: micro-adapter-precise1k-modules-fresh
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete201-module listing and metadata; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-precise1k-modules-fresh.raw
  accessed_at: '2026-11-04T12:24:20.148396Z'
  support: context_only
  summary: Used to bound the returned memberships and module population; AI-generated
    narrative summaries and activity vectors are not biological evidence here.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
- evidence_id: micro-adapter-membership-b2496
  kind: search
  reference: https://imodulondb.org/api/genes/b2496/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete201 returned gene-module membership rows, in_imodulon flags and
    weight/threshold fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-membership-b2496.raw
  accessed_at: '2026-11-04T12:25:59.607400Z'
  support: context_only
  summary: 'b2496: zero thresholded memberships among201 returned modules. No above-threshold
    module warrants member-level source interpretation. Zero membership is neither
    gene/protein absence nor physical-complex/causal evidence.'
  snapshot_sha256: 6a09cbbfc4e76bfb73b1d264e6230d893455b9c1efb1ceae2104d29ff64eabec
  search_scope: Official iModulonDB; query Exact locus b2496 in e_coli/precise1k;
    all returned module membership rows; actual accessed_at 2026-11-04T12:25:59.607400Z;
    limit One complete response, thresholded membership only; no expression-to-assembly
    inference; exact complete returned response only, no broader absence inference.
- evidence_id: micro-adapter-membership-b3701
  kind: search
  reference: https://imodulondb.org/api/genes/b3701/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete201 returned gene-module membership rows, in_imodulon flags and
    weight/threshold fields; snapshot /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-membership-b3701.raw
  accessed_at: '2026-11-04T12:25:59.607380Z'
  support: context_only
  summary: 'b3701: zero thresholded memberships among201 returned modules. No above-threshold
    module warrants member-level source interpretation. Zero membership is neither
    gene/protein absence nor physical-complex/causal evidence.'
  snapshot_sha256: d5e604543410b34561ac751e5b38c067a221e6ff1983dc41a90a52a22cc6670a
  search_scope: Official iModulonDB; query Exact locus b3701 in e_coli/precise1k;
    all returned module membership rows; actual accessed_at 2026-11-04T12:25:59.607380Z;
    limit One complete response, thresholded membership only; no expression-to-assembly
    inference; exact complete returned response only, no broader absence inference.
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner attempt2026-11-03T00:49:00.848907–00:49:00.863225Z only
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Retained PermissionError pyvenv.cfg is historical; no fresh runner invocation.
    Current official catalogue/dataset fallbacks have their own actual timestamps
    and scope.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-hda1_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml
    --verify
  locator: Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-verify.log;
    exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-verify-receipt.json
    SHA256 fe27fd8c8d07e679836b04a20666d343d3f443b0da58761fe55df74f3916c191
  accessed_at: '2026-11-04T12:24:01.345039Z'
  support: supports
  summary: Three reviewed S288C examples and three COVERED typed nodes. Native exit0
    is identity/coverage validation, not experimental membership or assembly proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-hda1_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda1_complex.yaml
    --causal-graphs
  locator: Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-causal.log;
    exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-causal-receipt.json
    SHA256 c4f1ba724243bd76fa8dc96c2be79afcdb6f88d38fc70c5ce9de315592652f8b
  accessed_at: '2026-11-04T12:24:01.756550Z'
  support: supports
  summary: Three reviewed S288C examples and three COVERED typed nodes. Native exit0
    is identity/coverage validation, not experimental membership or assembly proof.
  snapshot_sha256: 0698baa112f4c65d51a87fc7cdc54fa4c097af5e3283457b5e188c37526b371c
- evidence_id: micro-native-hda_beta_clamp_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --verify
  locator: Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-verify.log;
    exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-verify-receipt.json
    SHA256 134ff93b95ddefb6bd6346016152d6e15e15c47611c7fd84be1f87696d04ded7
  accessed_at: '2026-11-04T12:24:02.881474Z'
  support: supports
  summary: Two reviewed K-12 examples and one COVERED typed Hda node; DnaN is a STRUCTURE
    node, not a second typed protein node. Native exit0 is identity/coverage validation,
    not experimental membership or assembly proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-hda_beta_clamp_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hda_beta_clamp_complex.yaml
    --causal-graphs
  locator: Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-causal.log;
    exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-causal-receipt.json
    SHA256 2a65f2d110a0e87a8a2085b5ec96c14a5a5f8f81624590e8e995691aa1016308
  accessed_at: '2026-11-04T12:24:03.305603Z'
  support: supports
  summary: Two reviewed K-12 examples and one COVERED typed Hda node; DnaN is a STRUCTURE
    node, not a second typed protein node. Native exit0 is identity/coverage validation,
    not experimental membership or assembly proof.
  snapshot_sha256: fdb72ccdbcb760c5581b5ce5a9ec2ee7fbba558b130b4cc5bf5b39f01c27460d
- evidence_id: micro-native-hir_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml
    --verify
  locator: Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-verify.log;
    exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-verify-receipt.json
    SHA256 9259920f9533e69b943ec86ac5add0315b305f6b261fb0bbf48ae6587a119518
  accessed_at: '2026-11-04T12:24:04.536460Z'
  support: supports
  summary: Four reviewed S288C examples and four COVERED typed nodes. Native exit0
    is identity/coverage validation, not experimental membership or assembly proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-hir_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml
    --causal-graphs
  locator: Complete log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-causal.log;
    exact receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-causal-receipt.json
    SHA256 e6281fe449aa49aedef70e8386aaf925c15ca23d7d4f2bdaeaa8515f3f5ba45f
  accessed_at: '2026-11-04T12:24:04.987032Z'
  support: supports
  summary: Four reviewed S288C examples and four COVERED typed nodes. Native exit0
    is identity/coverage validation, not experimental membership or assembly proof.
  snapshot_sha256: 96856c000b7ea9ca08297600191ff88679229c41cc7e4bad485dc9450ca1081d
- evidence_id: plaque-t4-record
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/other/hops_complex.yaml
  locator: Entire current record, all assertions, components, examples, graphs, datasets/images,
    discussions and curation history.
  accessed_at: '2026-11-04T12:36:30.906759Z'
  support: context_only
  summary: Complete current HOPS complex record at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    no record mutation.
  snapshot_sha256: 17afe9c90b6a51d94e588059cea7c0cb63c37a04e8b9c656b868c5ac1ec2a57f
- evidence_id: plaque-t4-original
  kind: prior_review
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261022T074159Z-hops-complex-audit/review.yaml
  locator: Entire original native YAML and canonical derived Markdown; exact historical
    input verification in original-proof.json.
  accessed_at: '2026-11-04T12:36:30.906877Z'
  support: context_only
  summary: 'Original review 20261022T074159Z-hops-complex-audit: findings, actions,
    evidence tiers, checks and verdict independently reassessed; immutable historical
    observation.'
  snapshot_sha256: 18bb2f6e2b46e471e510a12d97a8bc34a3a7c8e725f12c6ffb4fb1740ce87627
- evidence_id: plaque-t5-record
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/other/hsp78_chaperone_complex.yaml
  locator: Entire current record, all assertions, components, examples, graphs, datasets/images,
    discussions and curation history.
  accessed_at: '2026-11-04T12:36:30.906909Z'
  support: context_only
  summary: Complete current Hsp78 chaperone complex record at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    no record mutation.
  snapshot_sha256: ce4cf652d09ceed2af98370e674ca290bb9c878039fc2db47b2b982c3f0e7262
- evidence_id: plaque-t5-original
  kind: prior_review
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261022T074159Z-hsp78-chaperone-complex-audit/review.yaml
  locator: Entire original native YAML and canonical derived Markdown; exact historical
    input verification in original-proof.json.
  accessed_at: '2026-11-04T12:36:30.906946Z'
  support: context_only
  summary: 'Original review 20261022T074159Z-hsp78-chaperone-complex-audit: findings,
    actions, evidence tiers, checks and verdict independently reassessed; immutable
    historical observation.'
  snapshot_sha256: f068e79c710ace752becfe6eac9e0a040f51ede92bc849c874552663101e5280
- evidence_id: plaque-t8-record
  kind: record_content
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/data/structures/other/i_aaa_complex.yaml
  locator: Entire current record, all assertions, components, examples, graphs, datasets/images,
    discussions and curation history.
  accessed_at: '2026-11-04T12:36:30.906972Z'
  support: context_only
  summary: Complete current i-AAA complex record at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    no record mutation.
  snapshot_sha256: f6877406ef9d82f3c18666e77b2ae3bb8c0a8c8c582c35bfba92d7cffafacda9
- evidence_id: plaque-t8-original
  kind: prior_review
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/reviews/structured/20261022T074201Z-i-aaa-complex-audit/review.yaml
  locator: Entire original native YAML and canonical derived Markdown; exact historical
    input verification in original-proof.json.
  accessed_at: '2026-11-04T12:36:30.907006Z'
  support: context_only
  summary: 'Original review 20261022T074201Z-i-aaa-complex-audit: findings, actions,
    evidence tiers, checks and verdict independently reassessed; immutable historical
    observation.'
  snapshot_sha256: d8137bbaecb76afcdb935654cb4ab466e8e63666a92dfbc82730a785a8568aeb
- evidence_id: plaque-curation
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/docs/CURATION.md
  locator: Identity, source-neutral classes, reviewed-label-only semantics, verbatim
    snippet, separate taxon-specific complex compositions and append-only history/discussion
    policy.
  accessed_at: '2026-11-04T12:36:30.907048Z'
  support: context_only
  summary: Frozen repository guidance used only as review authority, not independent
    biological evidence.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: plaque-schema
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, protein examples, graph nodes/edges, chemical identity, essentiality
    and image/dataset fields.
  accessed_at: '2026-11-04T12:36:30.907092Z'
  support: context_only
  summary: Frozen repository guidance used only as review authority, not independent
    biological evidence.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-profile
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/docs/record-review-profile.md
  locator: Scientific claim-level review and structured-source applicability from
    positive protein/pathway/stress assertions.
  accessed_at: '2026-11-04T12:36:30.907122Z'
  support: context_only
  summary: Frozen repository guidance used only as review authority, not independent
    biological evidence.
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
- evidence_id: plaque-review-skill
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/review-yaml-record/SKILL.md
  locator: Read-only scientific review, source/input freezing, bounded searches, native
    artifact lifecycle.
  accessed_at: '2026-11-04T12:36:30.907158Z'
  support: context_only
  summary: Frozen repository guidance used only as review authority, not independent
    biological evidence.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-protein-skill
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/uniprot-protein-examples/SKILL.md
  locator: Exact gene identities, native accession status/taxa, external actor xrefs
    and limits of deterministic coverage.
  accessed_at: '2026-11-04T12:36:30.907192Z'
  support: context_only
  summary: Frozen repository guidance used only as review authority, not independent
    biological evidence.
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: plaque-graph-skill
  kind: authority
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/repo/.claude/skills/curate-causal-graphs/SKILL.md
  locator: Identity and evidence for directed relationships; association/function
    distinct from physical formation.
  accessed_at: '2026-11-04T12:36:30.907218Z'
  support: context_only
  summary: Frozen repository guidance used only as review authority, not independent
    biological evidence.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-go-0030897
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030897
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0030897.receipt.json
    SHA256 1645a83548eac7b39ea99f105e3bf6ed1d13e5f91283f665ff9e7d033fe180ff.
  accessed_at: '2026-11-04T12:26:04.011047Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: bc39bacfb918b995c5d2bee598e9cc7ecafa168a752f18ae3c075b9dcfe52ad9
- evidence_id: plaque-go-0098796
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098796
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0098796.receipt.json
    SHA256 147fb20f001434e9c07e7cc5dc925f07ffa3fbf2e6d971398299225b917a0950.
  accessed_at: '2026-11-04T12:26:04.012539Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: c0b9ee522071e5d1930dde6110f8ec3b3f939a2f12cdb77914e864b1fa04d5bb
- evidence_id: plaque-go-0042144
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042144
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0042144.receipt.json
    SHA256 1faa5abb8a913fbf35cd0dd399649e4837eb5af41cfdb79352206a2714cbd2d9.
  accessed_at: '2026-11-04T12:26:04.013884Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 6aa0643535cf320ffecd03257096a94b1ae087a3efe619dae3cd568ea3505da5
- evidence_id: plaque-go-0000329
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0000329.receipt.json
    SHA256 46b8a59671c07780b2394b2c0b1c15191cb2f71dec889a4f19d91c8610d2420f.
  accessed_at: '2026-11-04T12:26:04.015731Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 6f63981050a5fa2b09c7671501b2d0c0ecca28d39a8a97af212d6027b50544ac
- evidence_id: plaque-go-0101031
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0101031
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0101031.receipt.json
    SHA256 e3e5d48f7ca4b68ceac2145e24dd7d86c9f3fffabcc3b16bb5e364e1bb01b0d9.
  accessed_at: '2026-11-04T12:26:04.015857Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 0e2aeaf068347492dd9a58ff68392ac7962f6f7ddc918c191516bbcf0e0626e2
- evidence_id: plaque-go-0005759
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005759
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0005759.receipt.json
    SHA256 805729c31900a37e58cbe09f242bda867c5afb3ddcd529ce94b576ff7665e24d.
  accessed_at: '2026-11-04T12:26:04.015954Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 654a93f0a97153d85b382b931161c127ab29258fb0054afc1a713ef5575ffa65
- evidence_id: plaque-go-0140545
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140545
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0140545.receipt.json
    SHA256 cb485d00600adbe55ec5792809cb8fe77cd7e8d31d9a4eb3d06dbf8fe8d4917d.
  accessed_at: '2026-11-04T12:26:04.019278Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 89c2141643a17fd34809c7a8a74d5914b060a8c44926f3f8d4b899085a7ecb23
- evidence_id: plaque-go-0016887
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016887
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0016887.receipt.json
    SHA256 1614d68be27c0f260f4d45b445ed5367d37581f52aa4016931757f227a12bc86.
  accessed_at: '2026-11-04T12:26:04.020322Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 752c1d3b8346a4daf05deb904a1c6f8053ff6883f17ff738a2aecde95060b91b
- evidence_id: plaque-go-0031942
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031942
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0031942.receipt.json
    SHA256 d2b37cd7e0d99a540791eddcdc3b31c1e34ce519392fe3cd9e09933bfea3a266.
  accessed_at: '2026-11-04T12:26:04.020476Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 837afc5dac9cab57af7483b62a0dd67196a840ebba4b4938762099c7a8280a7b
- evidence_id: plaque-go-0098800
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0098800
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0098800.receipt.json
    SHA256 5a0c862d6deb061da397bf02685f7f253bb52792e5fffc86d897e3ba9b22bdb4.
  accessed_at: '2026-11-04T12:26:04.024853Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: b5d2eb220eb1a1a42ad99cfe91d358cb21597a3adea956e3d2c88cb2dae93ce6
- evidence_id: plaque-go-0005743
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005743
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0005743.receipt.json
    SHA256 a4f5e16599c10f22b3c55b14c58ea5409cdcf4b66a265b5313921203aee0131e.
  accessed_at: '2026-11-04T12:26:04.026501Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: ba28e8a48bcde74c14009e24937b39e33b51a79d50486259b47b8a3bfb4122e4
- evidence_id: plaque-go-0004176
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176
  locator: Exact term identity, definition, synonyms and typed child relationships
    in the returned native response. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-0004176.receipt.json
    SHA256 a631ea1528f29e270e1caee01768156818eef6e6df71a5a07b2f34e9dd101aa3.
  accessed_at: '2026-11-04T12:26:04.027818Z'
  support: supports
  summary: Current native GO term supports the specifically associated structure,
    broader class, location or function; typed relations are not interchanged and
    do not prove taxonomic prevalence.
  snapshot_sha256: 42a89b755405ee166b991f3c96628b95721d2f563428f5a0825bdad8a021d88d
- evidence_id: plaque-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete exact ENA taxon identity, rank, names and lineage. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/tax-4932.receipt.json
    SHA256 de6128306d9f7caa1ca6c1639b8316bbf35c43632fb41ae6796ebf046634c9b3.
  accessed_at: '2026-11-04T12:26:06.934353Z'
  support: supports
  summary: Saccharomyces cerevisiae species 4932 and S288C reference strain 559292
    are distinct; reference sequence taxon is not substituted for experimental strain
    backgrounds.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete exact ENA taxon identity, rank, names and lineage. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/tax-559292.receipt.json
    SHA256 0e4c5f5f547a3737019c79b36dd9d2a773f8fb385b2525bbb688f85baf7f6466.
  accessed_at: '2026-11-04T12:26:07.182064Z'
  support: supports
  summary: Saccharomyces cerevisiae species 4932 and S288C reference strain 559292
    are distinct; reference sequence taxon is not substituted for experimental strain
    backgrounds.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-up-P12868
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P12868.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P12868.receipt.json
    SHA256 7a07a74bd818e2d5a795be3217d78e0bac90c2c7ccf456a65d529213fee33839.
  accessed_at: '2026-11-04T12:26:04.924181Z'
  support: supports
  summary: Reviewed S288C P12868 independently matches Vps11/PEP5/YMR231W. Native
    comments are annotation context, not a claim that every cited experiment was read.
    Ypt7 remains an external Rab actor; reference identity does not independently
    prove assembly membership.
  snapshot_sha256: ff283afab18523326c61ef44b5c5ae24ea501a36b0b32d75e46d7b5834d4a2b0
- evidence_id: plaque-up-Q03308
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03308.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-Q03308.receipt.json
    SHA256 acfa27195b39d9d702f063d56be347a9b17148e6ac36da488a089a223a0d8ac5.
  accessed_at: '2026-11-04T12:26:04.925575Z'
  support: supports
  summary: Reviewed S288C Q03308 independently matches VPS16/YPL045W. Native comments
    are annotation context, not a claim that every cited experiment was read. Ypt7
    remains an external Rab actor; reference identity does not independently prove
    assembly membership.
  snapshot_sha256: 572e18358d76bb4a5bcaa5f12a16aa6c5e0d24f6e8c11a5ad3637907f79c35f1
- evidence_id: plaque-up-P27801
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27801.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P27801.receipt.json
    SHA256 2e05ba8b5ef74f99927896cfea1c68d83c508ddc008c3dbd8b4c016e117ad741.
  accessed_at: '2026-11-04T12:26:04.925634Z'
  support: supports
  summary: Reviewed S288C P27801 independently matches Vps18/PEP3/YLR148W. Native
    comments are annotation context, not a claim that every cited experiment was read.
    Ypt7 remains an external Rab actor; reference identity does not independently
    prove assembly membership.
  snapshot_sha256: 6b73997591488f3066e961f073293728183c0b1b17eefa4c162d1abf133dd37d
- evidence_id: plaque-up-P20795
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20795.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P20795.receipt.json
    SHA256 d3d5f319f2ae19dd5f5e8ce5dc762d68c751733079723d7879d12b3c1f3cb5e9.
  accessed_at: '2026-11-04T12:26:04.928215Z'
  support: supports
  summary: Reviewed S288C P20795 independently matches VPS33/YLR396C. Native comments
    are annotation context, not a claim that every cited experiment was read. Ypt7
    remains an external Rab actor; reference identity does not independently prove
    assembly membership.
  snapshot_sha256: 74c8787eb68381dc26a6e70ba85414e3a05c4cc15f45e0686a0b57a4882755d6
- evidence_id: plaque-up-Q07468
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q07468.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-Q07468.receipt.json
    SHA256 2cdac555850f4d1c94ad74d8f1e20c3af6cb557c2a40675e239bbfdda279eed3.
  accessed_at: '2026-11-04T12:26:04.929598Z'
  support: supports
  summary: Reviewed S288C Q07468 independently matches Vps39/VAM6/YDL077C. Native
    comments are annotation context, not a claim that every cited experiment was read.
    Ypt7 remains an external Rab actor; reference identity does not independently
    prove assembly membership.
  snapshot_sha256: ba8c57ae7fbf39f49c7891bbc839a740cfa77ef3d1bf2ac2d8a507fd20adf87d
- evidence_id: plaque-up-P38959
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38959.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P38959.receipt.json
    SHA256 fcb7202d1984a7e5150be2db7a7e7f0466e24df2ae69d80f78752dd08e9e8f7f.
  accessed_at: '2026-11-04T12:26:04.930844Z'
  support: supports
  summary: Reviewed S288C P38959 independently matches VPS41/YDR080W. Native comments
    are annotation context, not a claim that every cited experiment was read. Ypt7
    remains an external Rab actor; reference identity does not independently prove
    assembly membership.
  snapshot_sha256: f00f0e9596601755a992f645d763e1863206965b84892c7987d446315d22157b
- evidence_id: plaque-up-P32939
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32939.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P32939.receipt.json
    SHA256 e21af0a6f0c6d293747a996586e892dc10e82098f9582bc84910d8f5440b7237.
  accessed_at: '2026-11-04T12:26:04.932721Z'
  support: supports
  summary: Reviewed S288C P32939 independently matches YPT7/YML001W. Native comments
    are annotation context, not a claim that every cited experiment was read. Ypt7
    remains an external Rab actor; reference identity does not independently prove
    assembly membership.
  snapshot_sha256: ebc258b2b618f56b878b0360989fa01631b889f6d324dc3f6b011770d7dd00e5
- evidence_id: plaque-up-P33416
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33416.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P33416.receipt.json
    SHA256 93f32df3a5a58c3f0ed6a562663125de0cf00122702f5d9a606f144fdb480c71.
  accessed_at: '2026-11-04T12:26:05.079542Z'
  support: supports
  summary: Reviewed S288C P33416 independently matches HSP78/YDR258C/YD9320A.08C.
    Native comments are annotation context, not a claim that every cited experiment
    was read. Ypt7 remains an external Rab actor; reference identity does not independently
    prove assembly membership.
  snapshot_sha256: bf59e546b5cce1e31ae58140fdd5adcae71159693e3d628ddb5b5dbec385da19
- evidence_id: plaque-up-P32795
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32795.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P32795.receipt.json
    SHA256 cd9f926d16309df7e4714f9f59f97638bc34dd12592c2c09e25abf1339568855.
  accessed_at: '2026-11-04T12:26:05.080945Z'
  support: supports
  summary: Reviewed S288C P32795 independently matches YME1/YPR024W; OSD1/YTA11 aliases.
    Native comments are annotation context, not a claim that every cited experiment
    was read. Ypt7 remains an external Rab actor; reference identity does not independently
    prove assembly membership.
  snapshot_sha256: 12c66b361d745737245f2f446a163ed431186beded2bc9908f687f87550c4539
- evidence_id: plaque-up-P25573
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25573.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-P25573.receipt.json
    SHA256 94ede4c273a34120998091b1b3d44452f3c53ccf736c9c5ddbe2ff62d3d90c81.
  accessed_at: '2026-11-04T12:26:05.081057Z'
  support: supports
  summary: Reviewed S288C P25573 independently matches MGR1/YCL044C. Native comments
    are annotation context, not a claim that every cited experiment was read. Ypt7
    remains an external Rab actor; reference identity does not independently prove
    assembly membership.
  snapshot_sha256: 34e90b11c0ac8f3ca8de0bb483fcfe64e2c1917c68fe08aa932df9d4ec2a302e
- evidence_id: plaque-up-Q04472
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04472.json
  locator: Primary accession, entryType, full gene/locus tokens, organism/taxon and
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments with native evidence
    qualifiers; InterPro xrefs. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/up-Q04472.receipt.json
    SHA256 ce6c4a37a09a1dd2960ec2ac44669d5db0932c964319e7aaec9174588036de87.
  accessed_at: '2026-11-04T12:26:05.084011Z'
  support: supports
  summary: Reviewed S288C Q04472 independently matches MGR3/YMR115W; FMP24 alias.
    Native comments are annotation context, not a claim that every cited experiment
    was read. Ypt7 remains an external Rab actor; reference identity does not independently
    prove assembly membership.
  snapshot_sha256: a8b529176f8fdf242628a0a424c3ae18ffbc105b94a95e627672ba2d288de343
- evidence_id: plaque-query-FMP24
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AFMP24%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-FMP24.receipt.json
    SHA256 ee0ec2b114c26d06391350fd35d394a8ba2f999297db949f852b1138a591fe09.
  accessed_at: '2026-11-04T12:26:54.627062Z'
  support: supports
  summary: Exact reviewed S288C gene query for FMP24 returns one entry, Q04472; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: c986ba0acfca6ff1ba30f530195d4be7a76d94dd09745c7b12bf73f5dab51c9e
  search_scope: 'UniProtKB REST search: (gene_exact:FMP24) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-HSP78
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHSP78%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-HSP78.receipt.json
    SHA256 b78434337ada49df83e28ecbf411c612034f63a51dc88ad95979813fce263234.
  accessed_at: '2026-11-04T12:26:51.712871Z'
  support: supports
  summary: Exact reviewed S288C gene query for HSP78 returns one entry, P33416; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 5f600ea2da28eef7b5db8631eb6c73fdc3cd5326e7a522e3b5b936b72fe596ee
  search_scope: 'UniProtKB REST search: (gene_exact:HSP78) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-MGR1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMGR1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-MGR1.receipt.json
    SHA256 67acee776f8212e1adb668138c8dc94ac3f5d42b8d1868bc46ad3ce019d0c0ca.
  accessed_at: '2026-11-04T12:26:53.703584Z'
  support: supports
  summary: Exact reviewed S288C gene query for MGR1 returns one entry, P25573; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 6dad6c0a522347c7d73a83a7adbc149d9bf1991189152ee4ae6fef628ca6f680
  search_scope: 'UniProtKB REST search: (gene_exact:MGR1) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-MGR3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMGR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-MGR3.receipt.json
    SHA256 e306dc8d0d89557b683bac4a596693adc39227abdf33460dbe8ce2bbbbe1075d.
  accessed_at: '2026-11-04T12:26:53.779643Z'
  support: supports
  summary: Exact reviewed S288C gene query for MGR3 returns one entry, Q04472; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: c986ba0acfca6ff1ba30f530195d4be7a76d94dd09745c7b12bf73f5dab51c9e
  search_scope: 'UniProtKB REST search: (gene_exact:MGR3) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-OSD1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AOSD1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-OSD1.receipt.json
    SHA256 ec91d2fe36fdf02b61c9bd4422f33226faac4883404aa9fa9038c4aa588f4222.
  accessed_at: '2026-11-04T12:26:52.667138Z'
  support: supports
  summary: Exact reviewed S288C gene query for OSD1 returns one entry, P32795; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 3cdeaaf3ffaa678e184be0de96b4e41155393cf50660f8f16eac36fb032b1c9e
  search_scope: 'UniProtKB REST search: (gene_exact:OSD1) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-PEP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEP3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-PEP3.receipt.json
    SHA256 d5be816ef2bc1c2592eb4c5c5c4fa4d5f091999d1c257d3cc86c04aa93277046.
  accessed_at: '2026-11-04T12:26:48.988648Z'
  support: supports
  summary: Exact reviewed S288C gene query for PEP3 returns one entry, P27801; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: cdc80fa77df47d8e14c7b1aad16a2b8b33747ae02fcfffecc4e8a1397a172656
  search_scope: 'UniProtKB REST search: (gene_exact:PEP3) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-PEP5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEP5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-PEP5.receipt.json
    SHA256 4ae36637e5b6db1c577e49532f9130177e04e1c2bb0f96644c5d36ec09eabc9c.
  accessed_at: '2026-11-04T12:26:48.905417Z'
  support: supports
  summary: Exact reviewed S288C gene query for PEP5 returns one entry, P12868; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 2d7ec548d4f724f09d2f3c966ca4b44cd93914500f4413fef040aa9da6c29b2e
  search_scope: 'UniProtKB REST search: (gene_exact:PEP5) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VAM2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVAM2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VAM2.receipt.json
    SHA256 321629c5bcd4a5d4d3f65a5c6a0e603387311ce53cbef6f7bd4fc40f491123a2.
  accessed_at: '2026-11-04T12:26:50.610533Z'
  support: supports
  summary: Exact reviewed S288C gene query for VAM2 returns one entry, P38959; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 229de087a4a3ca30215759ff934c3ac89a9f90068fed97acd29537c874333127
  search_scope: 'UniProtKB REST search: (gene_exact:VAM2) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VAM6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVAM6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VAM6.receipt.json
    SHA256 2b50c30a9fb8d194c79edab6c7a25a6871212837ef6a3e80a977fd01bfd1a1e3.
  accessed_at: '2026-11-04T12:26:49.760696Z'
  support: supports
  summary: Exact reviewed S288C gene query for VAM6 returns one entry, Q07468; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: af496615b04336c15fffe8ce5354941cb4e4c75f4da3cd4a7aefa41d35bac141
  search_scope: 'UniProtKB REST search: (gene_exact:VAM6) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VPS11
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS11.receipt.json
    SHA256 6961403e6b70149c83b81407cd2caa1d9aff48662d765aa52705aa1ba8f7d4f3.
  accessed_at: '2026-11-04T12:26:48.733343Z'
  support: supports
  summary: Exact reviewed S288C gene query for VPS11 returns one entry, P12868; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 2d7ec548d4f724f09d2f3c966ca4b44cd93914500f4413fef040aa9da6c29b2e
  search_scope: 'UniProtKB REST search: (gene_exact:VPS11) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VPS16
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS16%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS16.receipt.json
    SHA256 ce36f2fe3e79d5060cc030b1e602c6dc588400adb3ec5831e5ad17c459b10d9b.
  accessed_at: '2026-11-04T12:26:48.916984Z'
  support: supports
  summary: Exact reviewed S288C gene query for VPS16 returns one entry, Q03308; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 4f1949a2b20f0131930173f14291d988c2119a19df78c13000dba74e842bc037
  search_scope: 'UniProtKB REST search: (gene_exact:VPS16) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VPS18
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS18%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS18.receipt.json
    SHA256 c26ce0cac9b5238d2a257327bc5422e554144767866fc7621fa3de4e5252a5b4.
  accessed_at: '2026-11-04T12:26:48.918510Z'
  support: supports
  summary: Exact reviewed S288C gene query for VPS18 returns one entry, P27801; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: cdc80fa77df47d8e14c7b1aad16a2b8b33747ae02fcfffecc4e8a1397a172656
  search_scope: 'UniProtKB REST search: (gene_exact:VPS18) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VPS33
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS33%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS33.receipt.json
    SHA256 f961b8f5ff93f984358ac733f0a84dcbda4cd1a92af2a4272e7ce4ad6b1303e0.
  accessed_at: '2026-11-04T12:26:49.003273Z'
  support: supports
  summary: Exact reviewed S288C gene query for VPS33 returns one entry, P20795; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 3c912aef86561cdacce29565228c60917e9a991c97d59e453244354cb9551705
  search_scope: 'UniProtKB REST search: (gene_exact:VPS33) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VPS39
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS39.receipt.json
    SHA256 0230f3421830e8b7d3fb69cf7505aef82a14e90f5c60809d5f7a987de975604f.
  accessed_at: '2026-11-04T12:26:49.667489Z'
  support: supports
  summary: Exact reviewed S288C gene query for VPS39 returns one entry, Q07468; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: af496615b04336c15fffe8ce5354941cb4e4c75f4da3cd4a7aefa41d35bac141
  search_scope: 'UniProtKB REST search: (gene_exact:VPS39) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-VPS41
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS41%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-VPS41.receipt.json
    SHA256 3957a1fb9119ec909e76b25e6dd0bef628681d80449198a1f06a85176962691a.
  accessed_at: '2026-11-04T12:26:49.783027Z'
  support: supports
  summary: Exact reviewed S288C gene query for VPS41 returns one entry, P38959; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 229de087a4a3ca30215759ff934c3ac89a9f90068fed97acd29537c874333127
  search_scope: 'UniProtKB REST search: (gene_exact:VPS41) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-YME1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYME1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-YME1.receipt.json
    SHA256 dedcb7dafa7b92fb7e6ce4b447f277f2c21928a96d0839f149d1bfaca025fd99.
  accessed_at: '2026-11-04T12:26:51.722825Z'
  support: supports
  summary: Exact reviewed S288C gene query for YME1 returns one entry, P32795; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 3cdeaaf3ffaa678e184be0de96b4e41155393cf50660f8f16eac36fb032b1c9e
  search_scope: 'UniProtKB REST search: (gene_exact:YME1) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-YPT7
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYPT7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-YPT7.receipt.json
    SHA256 021883601e23ec29157ee702a07a22d9b4a04927b705013acb14dc07be47887b.
  accessed_at: '2026-11-04T12:26:50.652937Z'
  support: supports
  summary: Exact reviewed S288C gene query for YPT7 returns one entry, P32939; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 5b1c0998a75d5768494778167a2d616919ebf571c7e2d10ecd8f44f8695bb75f
  search_scope: 'UniProtKB REST search: (gene_exact:YPT7) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-query-YTA11
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYTA11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete one-page accession/gene/organism identity set, including primary
    and alias tokens. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/query-YTA11.receipt.json
    SHA256 b1105c83004ea6c11beb1bc61b34aef1397c5b85ef65201d5562a536e8df24c4.
  accessed_at: '2026-11-04T12:26:52.843975Z'
  support: supports
  summary: Exact reviewed S288C gene query for YTA11 returns one entry, P32795; actual
    tokens match the named primary gene or synonym.
  snapshot_sha256: 3cdeaaf3ffaa678e184be0de96b4e41155393cf50660f8f16eac36fb032b1c9e
  search_scope: 'UniProtKB REST search: (gene_exact:YTA11) AND (organism_id:559292)
    AND (reviewed:true), format=json, size=500; all one returned result inspected,
    no broader taxon/paralog absence inferred.'
- evidence_id: plaque-ipr-IPR016528
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016528/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR016528.receipt.json
    SHA256 576cc73a6a687e3361e0a318874e77e01586e56c8b98f6606e198fd49f9554d3.
  accessed_at: '2026-11-04T12:26:05.388461Z'
  support: supports
  summary: Whole Vps11/Pep5 family, supported by native P12868 membership.
  snapshot_sha256: 73b2d50cac8002fc54c640905ed1b5cede4fcd263942ae55daa674e0ab172bf7
- evidence_id: plaque-ipr-IPR016534
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016534/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR016534.receipt.json
    SHA256 3714b28ff4bdc3fbec40236d26e97523b087b91a8e802ddf10f8a4781996ff52.
  accessed_at: '2026-11-04T12:26:05.696749Z'
  support: supports
  summary: Whole Vps16 family, supported by native Q03308 membership.
  snapshot_sha256: ddcd8dd9da4c7607ff524d7af0615638c065e447fa9bd7868b7597340f06610d
- evidence_id: plaque-ipr-IPR016902
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016902/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR016902.receipt.json
    SHA256 aeb2674acbf0255ab7ae5ea21e8d9c2fe55910a3820d4f25e3fa98c2956c83b4.
  accessed_at: '2026-11-04T12:26:05.854539Z'
  support: supports
  summary: Whole Vps41 family, supported by native P38959 membership; ambiguous descriptive
    prose is not imported as mechanism.
  snapshot_sha256: 9d0f8c9a0ea59cc3f93ec8a65860f10f2508123176137e46ae4430ec4ee93eba
- evidence_id: plaque-ipr-IPR013911
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013911/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR013911.receipt.json
    SHA256 8d7033578fb20aa2b9c631a23db6ff33a09810574daa9ffeeffa153acdd0b795.
  accessed_at: '2026-11-04T12:26:06.025968Z'
  support: supports
  summary: Whole Mgr1 family, with P25573 membership.
  snapshot_sha256: 3d7fa9fd9f0775fd3bb9c0906647932213a65978956cbdebbe82c9221e4dcc2a
- evidence_id: plaque-ipr-IPR040201
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040201/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR040201.receipt.json
    SHA256 3a37a9ead04422de8306a06112ca9feca549797e30cfda916618bd116201486e.
  accessed_at: '2026-11-04T12:26:06.328618Z'
  support: supports
  summary: Mrg3-like/Mgr3 family, with Q04472 membership; native authority spelling
    distinguished from yeast gene.
  snapshot_sha256: c67366070635cd6745c3891f5482e7878926428146141b612ff3c874668bf6a2
- evidence_id: plaque-ipr-IPR005936
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005936/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR005936.receipt.json
    SHA256 c2dac901042671d5bf1fd334aacadd20c63a2d1ccceffcb9dac1d17afb2ca4fa.
  accessed_at: '2026-11-04T12:26:06.476887Z'
  support: supports
  summary: Broad FtsH family, not an exact Yme1-only class.
  snapshot_sha256: 6d706dbe689ac3fbe1f2fa131c38f2c451b7e8e8d105e431cac431c1d1fe413c
- evidence_id: plaque-ipr-IPR048438
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048438/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR048438.receipt.json
    SHA256 51322fcb27fc6a273f6a9e0caff1fc45065762b0fec7fb092f5e1843e1f6860e.
  accessed_at: '2026-11-04T12:26:06.550953Z'
  support: supports
  summary: Yme1 amino-terminal domain, not a whole-protein Yme1 family.
  snapshot_sha256: e2cfa7e07fc4c3a7cc16f80cdfab1261d8f63abc21c5396899a40c90fb6f335e
- evidence_id: plaque-ipr-IPR001270
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR001270.receipt.json
    SHA256 b884ed64172fa702706686afcbb2acdfd0320f998f6b3a3d1e15378dc60a998c.
  accessed_at: '2026-11-04T12:26:06.585135Z'
  support: supports
  summary: Broad ClpA/B-family grouping, not an exact Hsp78 class.
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
- evidence_id: plaque-ipr-IPR050130
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: Native entry name/type, descriptions and quality flags, signatures; matched
    protein xrefs independently checked. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-IPR050130.receipt.json
    SHA256 a63802c1204d64d87277f46f071c25ab816513ae28b5cc6bb3fec60097843df0.
  accessed_at: '2026-11-04T12:26:06.693631Z'
  support: supports
  summary: Broad ClpA/B-family grouping; generated description llm:true/checked:false
    is excluded from biological inference.
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
- evidence_id: plaque-ipr-protein-P33416
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P33416/?page_size=200
  locator: Complete integrated InterPro response, entry types/names/accessions and
    next:null pagination. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-protein-P33416.receipt.json
    SHA256 15ea42c0fb5e1fae266ce179a15ad9c3ccb21266cc24831779cfc941418f1a09.
  accessed_at: '2026-11-04T12:26:08.826039Z'
  support: supports
  summary: Bounded exact protein P33416 family/domain inventory. Broader families
    or isolated domains do not establish an exact whole class; no all-authority absence
    claim.
  snapshot_sha256: 371cfdd22ff27bb840a73ea823bc75a849ff53f83a8637c7f386a923149e309f
- evidence_id: plaque-ipr-protein-P32795
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P32795/?page_size=200
  locator: Complete integrated InterPro response, entry types/names/accessions and
    next:null pagination. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/ipr-protein-P32795.receipt.json
    SHA256 3a28a1a3c47f18bb4fa9bfc3a5f026a73c57388a8323d3cb2a427155c734ba37.
  accessed_at: '2026-11-04T12:26:09.439346Z'
  support: supports
  summary: Bounded exact protein P32795 family/domain inventory. Broader families
    or isolated domains do not establish an exact whole class; no all-authority absence
    claim.
  snapshot_sha256: aca91d882e3796488d908ad2c035d72eeb436e7699a2f570deb057f92f98a527
- evidence_id: plaque-go-search-hsp78
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Hsp78&limit=25&page=1
  locator: Complete response, zero results. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/go-search-hsp78.receipt.json
    SHA256 ca11786ab03deee4c19c1088fff9d03b904267fbf2db35d7f41b848b7fdf3a75.
  accessed_at: '2026-11-04T12:26:54.762504Z'
  support: supports
  summary: No term returned in this one bounded query; the local complex identity
    is not replaced by the broader chaperone class.
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
  search_scope: QuickGO search query=Hsp78, limit=25, page=1; complete zero-hit response
    inspected. No other synonyms, databases or exhaustive term absence established.
- evidence_id: plaque-pmid-10944212
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10944212+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-10944212.receipt.json
    SHA256 c207cdee4458a12265c94e84772d4fb4e6e8239ab97766fbd4d2d674710c25ef.
  accessed_at: '2026-11-04T12:26:07.260909Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: b29169197ad65efddaaf242755fb68634a25a7191876795ec98b6eacdf107acf
- evidence_id: plaque-pmid-9362071
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9362071+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-9362071.receipt.json
    SHA256 7cfa2bcdfa94ba94985ce96b78e5a5ffd62fb34d9b5d2a7d489f5275c772e499.
  accessed_at: '2026-11-04T12:26:07.260943Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: 5814c267f7fd5134b27c897ee730d4308e1b48ccc5ed03f64171339ae5eca157
- evidence_id: plaque-pmid-36115461
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A36115461+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-36115461.receipt.json
    SHA256 ad9f6b32ff7d517f5f01984deff005d6a9976094fbab43b688720c4e866a7a64.
  accessed_at: '2026-11-04T12:26:07.541334Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: dbafc32a452634143c2629e78eb1a7a3907200a696dd4c54ad97a67f125b5fd1
- evidence_id: plaque-pmid-29138251
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29138251+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-29138251.receipt.json
    SHA256 4bd5bbd53c697be2e3a67cc3dfeb0a6e3f8a92efbac099ef873396907f8cec27.
  accessed_at: '2026-11-04T12:26:07.699567Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: 7d7fcff5a30efce7cc8ef7339f0cab53de28b8f3b4b1cfb260a583bf61ea15ba
- evidence_id: plaque-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-14562095.receipt.json
    SHA256 8e776dc85ad692e78c8d2b361456877c6d12e510b6b91b733d137580d56158ef.
  accessed_at: '2026-11-04T12:26:07.709012Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: 093086098e24ad18eaa308710684a446872e31bcd38be78214d7b4f9bbe71371
- evidence_id: plaque-pmid-14576278
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14576278+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-14576278.receipt.json
    SHA256 b3fd46a935085c9b07ba823be1c2abeecf4b52f116ad1460fddcc2d0f9e91659.
  accessed_at: '2026-11-04T12:26:07.883321Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: 2abbbd030dad78708d38cad3bb3798354ddfcf3150318cf3e09fa3a14bceb1f0
- evidence_id: plaque-pmid-16267274
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16267274+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-16267274.receipt.json
    SHA256 315af125552a90fc4ebd61392bbfef9ecdde5cce4efcf1763a4ed465c98aa08b.
  accessed_at: '2026-11-04T12:26:07.923755Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: 13a520e7b9b777b957431ae432aeabf866d3d26c53cdef328fbaa81f45ae6edb
- evidence_id: plaque-pmid-8355690
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8355690+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-8355690.receipt.json
    SHA256 2f8e6d944eef520a86399ec2cde6526ffa8dfd2b52446028c4f57b89b5c11fae.
  accessed_at: '2026-11-04T12:26:07.924819Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: fd4a8ae450dbe805dec4e6961742e1a756d444e84a9317e6513e203de4299b60
- evidence_id: plaque-pmid-8688560
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8688560+AND+SRC%3AMED&format=json&resultType=core&pageSize=2
  locator: Unique exact MED bibliographic identity, title/authors/year/DOI and complete
    available abstractText. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pmid-8688560.receipt.json
    SHA256 bcfb1fabe04a965681560e3feff8924197f1042a96b1ff2bad0df237bfbc44ec.
  accessed_at: '2026-11-04T12:26:08.414676Z'
  support: supports
  summary: Native bibliographic and abstract scope only; paper-body claims require
    separately inspected primary text. Historical Yme1 topology terminology is not
    silently reconciled with modern authority and Wu evidence.
  snapshot_sha256: fd9c0592ee13e3d6bd839314f6c861903fefe3611fa717cea16a6546a99411f3
- evidence_id: plaque-PMC16876-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC16876/
  locator: 'Genuine full HTML: abstract; Methods sec1 including sec2–4, Results sec5
    including sec6–9 and Figure1–4 text captions, Discussion sec10. No figure pixels.
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC16876-body.receipt.json
    SHA256 f4cc75cd8c282d36ebe7b95cd4b7b41e79c43ce4d4ac189dd91fdb005f507d70.'
  accessed_at: '2026-11-04T12:26:48.007838Z'
  support: supports
  summary: Seals2000 native yeast vacuole experiments support six-subunit HOPS association,
    priming-dependent rearrangement, GTP-Ypt7 binding and antibody-sensitive fusion.
    Vam2 identified by immunoblot, unlike the five MS assignments. BJ3505/DKY6281
    vacuoles and recombinant bacterial antigens are distinct contexts.
  snapshot_sha256: 2b58c6b3c08e5500719f6744eb42117d3ab9b276b9586ee468508b30375d44b7
- evidence_id: plaque-PMC25710-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25710/
  locator: 'Genuine full HTML, bounded reading: Methods sec3/Table1 and sec12 crosslinking,
    Results sec21 and Figure7 caption, Discussion sec25; no whole-body or pixel claim.
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC25710-body.receipt.json
    SHA256 582483a8a91ae4aef4440effb765a4f2fee3685042bc8d6dfd47dde58dc7aa4e.'
  accessed_at: '2026-11-04T12:26:48.011315Z'
  support: partial
  summary: Rieder1997 supports class-C core association and conditional Vps16-dependent
    recovery of Vps33, not universal formation necessity for each whole-HOPS member.
    SEY6210/6211 native yeast backgrounds and recombinant bacterial host are distinguished.
  snapshot_sha256: 0b79b9f34ad7329272b94e91c8235ea1386bec9331413cb03c4cbece0a0cfbf4
- evidence_id: plaque-PMC9574514-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9574514.1/PMC9574514.1.xml
  locator: 'Genuine JATS: Results sec1.1–1.4 and main Fig1–7 captions; Discussion
    sec2; Methods sec3.1–3.14; Data availability sec4 and copyright. Introduction
    and supplementary data not certified. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-s3.receipt.json
    SHA256 6c9722b3f065b9f9088882436e52725982a8e1600b7c42dfff3f480ea1444cce.'
  accessed_at: '2026-11-04T12:26:48.478691Z'
  support: supports
  summary: Jaworek2022 supports preparation-dependent oligomer observations, approximately
    70% reduced (not absent) trap ATPase activity, reporter resolubilization and growth
    complementation. Solubility is not refolding, glycerol growth is not measured
    respiratory flux, and proteomic interaction candidates are not fixed oligomer
    constituents. Source mutation-numbering, salt and protocol inconsistencies are
    retained, as already disclosed by the record.
  snapshot_sha256: 75b5f2c13addf3554fbd534e58fea2aa26605afe26987185a88cc7b3c9a5b2d8
- evidence_id: plaque-PMC5748973-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5748973.1/PMC5748973.1.xml
  locator: 'Genuine complete JATS: Introduction s01, Results/Discussion s03–s09 and
    embedded Fig1–5 captions, Methods s11/s16/s17. Whole article text additionally
    searched only for the asserted quote and specified words. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-s3.receipt.json
    SHA256 e038a3b2cce2b09cea6075e03625b51f353256b0da7227cd82f48592654a6fd6.'
  accessed_at: '2026-11-04T12:26:48.528969Z'
  support: partial
  summary: Wu2017/2018 supports tagged/endogenous substrate turnover, Mgr1/Mgr3 recruitment/association,
    Mgr1 bridging and Mgr3-dependent Mgr1 stability. Adaptor deletions do not alter
    the observed Yme1 complex size. Neither a six-copy CPX annotation nor the asserted
    rocky-road/spiral quotation is supplied. These are source-support limits, not
    a refutation of independently studied isolated hexameric cores.
  snapshot_sha256: bcb8b5c0f3f8f4c55bd48bce939280cfbf37bde04a9180f5ec2ff9079363a3f3
- evidence_id: plaque-PMC5748973-JCB_201702125_TableS1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5748973.1/JCB_201702125_TableS1.xlsx
  locator: XLSX ZIP/XML worksheet1 A4:B25 and A123:C138 only, all returned cells in
    those ranges. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-JCB_201702125_TableS1.receipt.json
    SHA256 ef3c538d464d1b8966f577dc07604a10330a1e21c80eea180a5398ede036171c.
  accessed_at: '2026-11-04T12:26:48.425291Z'
  support: supports
  summary: TableS1 distinguishes BY4741 derivatives from CEN.PK and W303-1A constructs.
    Other strain/primer rows are not claimed read.
  snapshot_sha256: e10af85a5a1244fca764881fc35c12765ee1610f03dd6064519378ce8742e877
- evidence_id: plaque-PMC9574514-gr1
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9574514.1/gr1.jpg
  locator: Actual downloaded native figure pixels, labels and separately read main-source
    caption/license. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr1.raw
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr1.receipt.json
    SHA256 3b74d97bf1fecc2bc2a8631eff476677a80668cf051b2456791dd8b70200d9f9.
  accessed_at: '2026-11-04T12:26:48.012616Z'
  support: supports
  summary: 'All Figure1 pixels inspected: ATPase curves, growth, native oligomer bands
    and purified SEC contexts; maintained MD5 d9e29f8d857266d914484f772d55ecac matches.
    No quantitative image reanalysis.'
  snapshot_sha256: 7590543842b8be3b938e1684bf8c79d23c01da0095c046ca63df6d6720b5dfc0
- evidence_id: plaque-PMC9574514-gr2
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9574514.1/gr2.jpg
  locator: Actual downloaded native figure pixels, labels and separately read main-source
    caption/license. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr2.raw
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-gr2.receipt.json
    SHA256 8833b7925a298cc46bc4a237fcb5c638dbd973f558a11a3ac3e5e2f46c027e63.
  accessed_at: '2026-11-04T12:26:48.013952Z'
  support: supports
  summary: 'All Figure2 pixels inspected: reporter soluble/pellet fractions and separate
    binding assay. Caption/Methods protocol discrepancy remains disclosed; maintained
    MD5 9c7316c59aa052f86222a1cc34b03cc8 matches.'
  snapshot_sha256: 848a047eeedaa2816d558bb791c0ebf0253a0496f4d79a2fe83709ad4b6e8c12
- evidence_id: plaque-PMC5748973-JCB_201702125_Fig3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5748973.1/JCB_201702125_Fig3.jpg
  locator: Actual downloaded native figure pixels, labels and separately read main-source
    caption/license. /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-JCB_201702125_Fig3.raw
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-JCB_201702125_Fig3.receipt.json
    SHA256 ccb75ac760bee0fec94be00e438ffd1995892f9a57cbbbe71b6db9f57c14ad80.
  accessed_at: '2026-11-04T12:26:48.402296Z'
  support: supports
  summary: 'All Figure3 A–H pixels inspected: co-IP recruitment blots and native-complex
    assays, not atomic reconstruction or counted stoichiometry; maintained MD5 ef80f8c8369e0bfd73138fdfd51c77be
    matches.'
  snapshot_sha256: 5a001ed02c0452886892e7fc52d753919451254ceb4dfab9de7ec31c08f83b6a
- evidence_id: plaque-pride-PXD030405
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD030405
  locator: Project accession/title, species, publication DOI, license, instrument
    and experiment metadata; underlying raw MS files not downloaded or reanalyzed.
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pride-PXD030405.receipt.json
    SHA256 a7d41edf209239d116bdcfa17483dfa3930bf6b1f8439de1ad4809c6574d122e.
  accessed_at: '2026-11-04T12:26:08.716056Z'
  support: supports
  summary: Correct Hsp78 interaction/aggregation project identity, yeast organism
    and linked Jaworek paper. Project metadata CC0 is separate from article/figure
    CC BY-NC-ND4.0; proteomic associations are condition-specific.
  snapshot_sha256: e18c73a22e41bc420aa0c82536a734074664aef93445518a0ba4e4cd79ade5ef
- evidence_id: plaque-pride-PXD030436
  kind: database
  reference: https://www.ebi.ac.uk/pride/ws/archive/v2/projects/PXD030436
  locator: Project accession/title, species, publication DOI, license, instrument
    and experiment metadata; underlying raw MS files not downloaded or reanalyzed.
    Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/pride-PXD030436.receipt.json
    SHA256 836e3872ca3951fcaaa358db06784ef1a0ba6cf5b3742dfde3c269d2a3eb0337.
  accessed_at: '2026-11-04T12:26:08.821853Z'
  support: supports
  summary: Correct Hsp78 interaction/aggregation project identity, yeast organism
    and linked Jaworek paper. Project metadata CC0 is separate from article/figure
    CC BY-NC-ND4.0; proteomic associations are condition-specific.
  snapshot_sha256: c0bffbac5be7d67695c6ab81b69d9a76b8ddce9ae22dcb78d3bc66e7f019b961
- evidence_id: plaque-cpx-1655
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1655
  locator: Complete native complex identity, taxon, participants including native
    stochiometry keys, bioRole, linkedFeatures and evidenceType. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/cpx-1655.receipt.json
    SHA256 4339d42e9139fc830222d28770a3d344506334528e42e75c7adb1bbebb7ccab9.
  accessed_at: '2026-11-04T12:26:08.594134Z'
  support: supports
  summary: YME1/P32795 enzyme, MGR1/P25573, MGR3/Q04472 and CHEBI:29105 cofactor are
    participants. Every native stochiometry field exists and is null; no 6x annotation
    for Yme1 or zinc. ECO0005547 is curator inference, not a depletion/assembly assay.
    Taxon559292 retained despite species-style source label.
  snapshot_sha256: a24056b131bffc231be292a4fecbf108bfeb571f28539d44157adb53796418dc
- evidence_id: plaque-chebi-29105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29105
  locator: Exact native ChEBI identity and chemical definition. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/chebi-29105.receipt.json
    SHA256 57e98d8334b715288745c1f35bbf4089745afbd2192fc6f2520b509009c70e7c.
  accessed_at: '2026-11-04T12:26:09.744846Z'
  support: supports
  summary: CHEBI:29105 denotes zinc(2+), matching the maintained cofactor identity.
  snapshot_sha256: 1710e73dbe5e68523715fe5378901b0c97d35f0260bbf9aeb00b0c390e464e0f
- evidence_id: plaque-eco-0005547
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0005547
  locator: Exact native ECO definition. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/eco-0005547.receipt.json
    SHA256 797b1d2a03aaaff5524d574ea9691ea7d97afd33a5da1c13daa03da5ba7f7266.
  accessed_at: '2026-11-04T12:26:09.746596Z'
  support: supports
  summary: Curator inference based on background knowledge is distinct from physical-interaction
    experimental evidence.
  snapshot_sha256: a6ea6ff7334e1e7cd3fee1ef14c09bc40944adcbf6571775cf5f2ef49352bb8a
- evidence_id: plaque-PMC9574514-jats
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9574514/fullTextXML
  locator: Exact failed retrieval receipt and raw response; no scientific content
    used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC9574514-jats.receipt.json
    SHA256 5b04a12c5a2fcd84a564db346bc2d0ca200e5dbf514d4103b31c2831a5bd6fcc.
  accessed_at: '2026-11-04T12:26:08.823564Z'
  support: context_only
  summary: This route returned HTTP 406; genuine separately read HTML/JATS supplies
    positive evidence. Failure is not biological absence.
  snapshot_sha256: 6cfc171686f7a59c4ff9facbc3b766846eca774c11dc1444f0b8b273819ae4f1
- evidence_id: plaque-PMC5748973-jats
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5748973/fullTextXML
  locator: Exact failed retrieval receipt and raw response; no scientific content
    used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC5748973-jats.receipt.json
    SHA256 5b82909d8f98de2975c9a8e77ec0994501cf6fbee7a579a6c25165007b968c7c.
  accessed_at: '2026-11-04T12:26:08.824838Z'
  support: context_only
  summary: This route returned HTTP 406; genuine separately read HTML/JATS supplies
    positive evidence. Failure is not biological absence.
  snapshot_sha256: 3277971d4de0814376e547cdb938e3b304e4a3f9b685e061898d1d1805e5c83a
- evidence_id: plaque-PMC16876-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC16876/fullTextXML
  locator: Exact failed retrieval receipt and raw response; no scientific content
    used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC16876-xml.receipt.json
    SHA256 76d643ea7e5889e91f39eed6a6ba6b499d2c540728f12440b14261a166915742.
  accessed_at: '2026-11-04T12:26:48.010051Z'
  support: context_only
  summary: This route returned HTTP 500; genuine separately read HTML/JATS supplies
    positive evidence. Failure is not biological absence.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-PMC25710-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC25710/fullTextXML
  locator: Exact failed retrieval receipt and raw response; no scientific content
    used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC25710-xml.receipt.json
    SHA256 8cce8fdd2604dda52b477b534b19faa3b28cc37d6505a0959dfca9d3a3f8a079.
  accessed_at: '2026-11-04T12:26:48.011494Z'
  support: context_only
  summary: This route returned HTTP 500; genuine separately read HTML/JATS supplies
    positive evidence. Failure is not biological absence.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: plaque-PMC16876-s3
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC16876.1/PMC16876.1.xml
  locator: Exact failed retrieval receipt and raw response; no scientific content
    used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC16876-s3.receipt.json
    SHA256 24c7e402979be4ed9673b8c76796a56eca90da3fd720214fe80d0efa2b6059c7.
  accessed_at: '2026-11-04T12:26:48.640965Z'
  support: context_only
  summary: This route returned HTTP 404; genuine separately read HTML/JATS supplies
    positive evidence. Failure is not biological absence.
  snapshot_sha256: a6b415982cb608449c130c204b4171b171989df3d4114653a2f8e966d2533c27
- evidence_id: plaque-PMC25710-s3
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC25710.1/PMC25710.1.xml
  locator: Exact failed retrieval receipt and raw response; no scientific content
    used. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/PMC25710-s3.receipt.json
    SHA256 3f80bc85699acb61173bf0dd0e726c45825f4beffb5932840f222e2987ad3947.
  accessed_at: '2026-11-04T12:26:48.644053Z'
  support: context_only
  summary: This route returned HTTP 404; genuine separately read HTML/JATS supplies
    positive evidence. Failure is not biological absence.
  snapshot_sha256: 95d4da8fe70154c2da25729cd37e2818b6284caceead3f609a554d906c0f5a6a
- evidence_id: plaque-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: Complete genuine 20-row organism catalogue, 28 organism/dataset entries;
    independent reread of shared current packet. Receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/adapter-catalogue-fresh.receipt.json
    SHA256 d426447e30a6a70975c1b3878c4952ed2ab69ee6756aa4a5bdf2e73b5a2d4ee2
  accessed_at: '2026-11-04T12:24:20.225750Z'
  support: supports
  summary: No Saccharomyces cerevisiae or yeast experimental/reference strain represented.
    All three molecular narratives trigger assessment; no matched dataset exists within
    this inspected catalogue. Recombinant E. coli expression hosts are not proxies
    for yeast complexes.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: Official iModulonDB GET /api/organisms; all 20 organism rows and their
    28 dataset entries inspected for Saccharomyces/S288C and the paper yeast backgrounds.
    No downstream unrelated-host queries or generated module prose used.
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical command receipt only; no fresh invocation on this review.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: 2026-11-03T00:49Z runner failed with PermissionError on pyvenv.cfg. Current
    assessment uses separately successful official HTTPS catalogue; historical failure
    is not current biological noncoverage.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-original-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/original-proof.json
  locator: Three original native validate/render commands and 41 historical source-input
    hashes at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  accessed_at: '2026-11-04T12:36:30.914915Z'
  support: supports
  summary: All three validations/render commands exit0; rendered Markdown equals original
    bytes; all original frozen input hashes match historical Git bytes. Historical
    success does not certify current changed i-AAA edges.
  snapshot_sha256: 94779c43762ebd3c4b1de1c91147f6beef0d3c79369bb843278782dfa5bbbcd7
- evidence_id: plaque-stale-diff
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/i-aaa-stale.diff
  locator: Exact original frozen i-AAA record to current source record diff.
  accessed_at: '2026-11-04T12:36:30.914942Z'
  support: supports
  summary: Current i-AAA adds Yme1 and zinc nodes, two architecture/cofactor edges
    and an October24 history entry. The new source-support defect is absent from the
    original reviewed record; HOPS/Hsp78 unchanged.
  snapshot_sha256: 6d6afe3057b6ab3dd5776082dca0c2057d3b4bd104b29cc10fa43e89fe606cb6
- evidence_id: plaque-iaaa-attribution-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/iaaa-attribution-proof.json
  locator: Complete normalized genuine JATS phrase/word search and all four exact
    native CPX stochiometry fields.
  accessed_at: '2026-11-04T12:36:30.914966Z'
  support: supports
  summary: Exact purported quote absent; staircase/rocky/hexamer/spiral each zero
    in that article. All CPX fields present and null. Search bounded to this source,
    not literature-wide biology.
  snapshot_sha256: 600693f0ef321ae733ea4a98d87d2acea0c06ac6c0e1fb1d2c5918e435667400
- evidence_id: plaque-iaaa-peer-challenge
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-microtubule/iaaa-core-source-challenge.json
  locator: Separate independent reading and whole-source quote search; exact source
    hashes retained.
  accessed_at: '2026-11-04T12:36:30.915007Z'
  support: supports
  summary: Independent challenge corroborates source-attribution finding while preserving
    valid roles, possible separately evidenced isolated hexamer and assay scope.
  snapshot_sha256: 84c9ed3ad816d799408ee9b75de5bd79b2fd65d538517cced2e36068ed6104ab
- evidence_id: plaque-historical-jaworek-xml-access
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9574514/fullTextXML
  locator: Original 20261022T074159Z-hsp78-chaperone-complex-audit evidence[19] micro57-jaworek2022-xml.
    Historical HTTP406 access-only evidence, kind corrected here; original artifact
    untouched. Original native406 receipt and raw bytes.
  accessed_at: '2026-10-22T07:22:41.782724Z'
  support: context_only
  summary: The EuropePMC XML request returned406 with a short error body, not a scientific
    source. Positive reading rests on the separately retained genuine PMC HTML and
    actual figure files.
  snapshot_sha256: 33c7a5f865d318ca682a953c2a50ac925ff838f077d1166040a1f5bea0f42369
- evidence_id: plaque-native-hops_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-verify-receipt.json
  locator: Actual command receipt SHA256 1219be18d4fc421d3f2f4ad45265c96eb3a3085384bdc8004b4dba2b7722775e;
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-verify.log
    with snapshot hash below; full log read.
  accessed_at: '2026-11-04T12:24:08.001048Z'
  support: supports
  summary: Six reviewed examples; six COVERED subunit nodes and external Ypt7 UNANCHORED_WITH_UNIPROT,
    correctly retained as external actor. Exit0 is identity/coverage validation, not
    mechanism or stoichiometry proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-hops_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-causal-receipt.json
  locator: Actual command receipt SHA256 513d9eb6f9004d356cdd6256f2c8b4dcbad74c5d493139c93152da8ab04780cd;
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-causal.log
    with snapshot hash below; full log read.
  accessed_at: '2026-11-04T12:24:08.424569Z'
  support: supports
  summary: Six reviewed examples; six COVERED subunit nodes and external Ypt7 UNANCHORED_WITH_UNIPROT,
    correctly retained as external actor. Exit0 is identity/coverage validation, not
    mechanism or stoichiometry proof.
  snapshot_sha256: 892cd259b2c321099f6cac2b190f08044881c771012d46f67414f536f65de7dd
- evidence_id: plaque-native-hsp78_chaperone_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-verify-receipt.json
  locator: Actual command receipt SHA256 e34f7c886c2ac0da846eb4f79ddb8de94c5c87c8885e6ae0ae7f143a3a228e6d;
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-verify.log
    with snapshot hash below; full log read.
  accessed_at: '2026-11-04T12:24:09.561798Z'
  support: supports
  summary: One reviewed Hsp78 example and one COVERED typed node. Exit0 is identity/coverage
    validation, not mechanism or stoichiometry proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-hsp78_chaperone_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-causal-receipt.json
  locator: Actual command receipt SHA256 17f9e0759cfa889602f4cb4af4f2c7af021636803e4fb0868c9d7ca1897b7d26;
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-causal.log
    with snapshot hash below; full log read.
  accessed_at: '2026-11-04T12:24:09.995717Z'
  support: supports
  summary: One reviewed Hsp78 example and one COVERED typed node. Exit0 is identity/coverage
    validation, not mechanism or stoichiometry proof.
  snapshot_sha256: 5867d4085f1c7acff7bbc6c93531493cbeea3c2e94aabd23878aab54d7ebe9d8
- evidence_id: plaque-native-i_aaa_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-verify-receipt.json
  locator: Actual command receipt SHA256 5bff57b1b18c281d7c74acf11216f97e989f315053767a9a0217cd259737438a;
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-verify.log
    with snapshot hash below; full log read.
  accessed_at: '2026-11-04T12:24:14.148014Z'
  support: supports
  summary: Three reviewed examples and three COVERED typed protein nodes in current
    record; zinc is chemical. Original graph had only two typed protein nodes. Exit0
    is identity/coverage validation, not mechanism or stoichiometry proof.
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-i_aaa_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-causal-receipt.json
  locator: Actual command receipt SHA256 6479d48213774e5852c8f91166f40bf9d116d8c52fbc912704869f8fcf83a992;
    stdout /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-causal.log
    with snapshot hash below; full log read.
  accessed_at: '2026-11-04T12:24:14.551577Z'
  support: supports
  summary: Three reviewed examples and three COVERED typed protein nodes in current
    record; zinc is chemical. Original graph had only two typed protein nodes. Exit0
    is identity/coverage validation, not mechanism or stoichiometry proof.
  snapshot_sha256: 56d25989f5311df05c2743135e4baac5d6b8a99d427c86d00a8b43432d83517c
- evidence_id: plaque-used-input-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-plaque/used-input-proof.json
  locator: Exact actually used maintained context and target/original paths; Git source
    and worktree hashes compared with native inspect.
  accessed_at: '2026-11-04T12:36:31.142052Z'
  support: supports
  summary: All actually used maintained input bytes match frozen source and current
    worktree. No unlisted maintained neighbor used.
  snapshot_sha256: 55a196820e1c118d5190a25ae76818da338df8a3ed2f1481d4147c5f89564fd2
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Whole-record review and structured-source policy
  summary: Positive named molecular/pathway assertions trigger actual host-specific
    applicability checks; absence of expression inference is not an exemption.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Component grounding and dated discussion/history contract
  summary: Verified exact families can resolve a current deferral. Preserve dated
    rationale and append current clarification rather than rewriting history.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, presence, essentiality and graph contracts
  summary: Valid protein classes and associated machinery need not be one family or
    obligatorily represented in every optional field. Localization, membership, activity,
    viability and formation necessity differ.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Reference accession/name/status/taxon checks
  summary: Reference identity and current singleton query evidence do not reconstruct
    historical releases or prove experimental membership/strain/causality.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope and actor/edge evidence
  summary: Spatial parthood/function maps are nonmechanistic; a real coarse mechanistic
    edge need not assert unmeasured chemistry or universal necessity.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Source access and exact inspected extent
  summary: Metadata, primary abstracts, genuine main bodies, supplements and viewed
    pixels have different scopes; failed access is validation context only.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Native review schema and exact predecessor identities
  summary: Use unique evidence references, bounded searches and exact inherited repository/review/finding
    references.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
- evidence_id: septin-up-P27343
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27343.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P27343: UniProtKB reviewed (Swiss-Prot); taxon 190650; gene tokens [{"geneName":
    {"value": "hfaB"}, "orderedLocusNames": [{"value": "CC_2629"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:13.557900Z'
  support: supports
  snapshot_sha256: c572745c1197f92991aa58abd291585e6fc2ab13110e5bb0955aab610c62ba16
- evidence_id: septin-up-A0A0H3CE47
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A0H3CE47.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'A0A0H3CE47: UniProtKB unreviewed (TrEMBL); taxon 565050; gene tokens [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ACL97268.1"}],
    "value": "hfsK"}, "orderedLocusNames": [{"evidences": [{"evidenceCode": "ECO:0000313",
    "source": "EMBL", "id": "ACL97268.1"}], "value": "CCNA_03803"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:13.422671Z'
  support: supports
  snapshot_sha256: 4de14fa035f2d0bd60b45960442c882075a4b8c3222f678ddabc40cda67a5aac
- evidence_id: septin-up-Q45977
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q45977.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q45977: UniProtKB reviewed (Swiss-Prot); taxon 190650; gene tokens [{"geneName":
    {"value": "hfaD"}, "orderedLocusNames": [{"value": "CC_2630"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:13.422607Z'
  support: supports
  snapshot_sha256: 43c1b75c2f33c69c722641de197e5a387a688e755db48719ef7aac2856abadaa
- evidence_id: septin-up-P27342
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27342.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P27342: UniProtKB reviewed (Swiss-Prot); taxon 190650; gene tokens [{"geneName":
    {"value": "hfaA"}, "orderedLocusNames": [{"value": "CC_2628"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:17.494330Z'
  support: supports
  snapshot_sha256: 3e869d55ef8bcb269dd2d3e6718b55ae13f61ef44aaf46fed9bf972bbd90ff63
- evidence_id: septin-tax-565050
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/565050
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Caulobacter vibrioides NA1000; relevant equivalent/synonym
    names ["Caulobacter crescentus NA1000:synonym"]. Taxon identity is not an experimental-strain
    substitution.
  accessed_at: '2026-11-04T12:27:13.457056Z'
  support: supports
  snapshot_sha256: d3c932efaddd17db870d54241a8c2441cc71fa808cad435ef9bfd60976641685
- evidence_id: septin-tax-190650
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/190650
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Caulobacter vibrioides CB15; relevant equivalent/synonym
    names ["Caulobacter crescentus CB15:synonym", "Caulobacter vibrioides ATCC 19089:synonym"].
    Taxon identity is not an experimental-strain substitution.
  accessed_at: '2026-11-04T12:27:13.443399Z'
  support: supports
  snapshot_sha256: 1ee188a0befe230048162264bc667bcaf7616a5b6be3199d21f340408d42f5ef
- evidence_id: septin-tax-155892
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/155892
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Caulobacter vibrioides; relevant equivalent/synonym
    names ["Caulobacter vibrioides Henrici and Johnson 1935 (Approved Lists 1980):authority",
    "Caulobacter crescentus:synonym"]. Taxon identity is not an experimental-strain
    substitution.
  accessed_at: '2026-11-04T12:27:13.414584Z'
  support: supports
  snapshot_sha256: 99691bdcc66af16241d0a4d0a9ef13c3e6e87ecf9c4d36331ea8e40757bffce7
- evidence_id: septin-query-hfaA-190650
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhfaA%29+AND+%28organism_id%3A190650%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P27342. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:13.697212Z'
  support: supports
  snapshot_sha256: 186416d4b0a4d2ec138e7b241435d944052ebf2cc90bc02c415b6097d0dc3919
  search_scope: 'database: UniProtKB; query: (gene_exact:hfaA) AND (organism_id:190650)
    AND (reviewed:true); date: 2026-11-04T12:27:13.697212Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-hfaB-190650
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhfaB%29+AND+%28organism_id%3A190650%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P27343. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:14.632671Z'
  support: supports
  snapshot_sha256: 0cfe4ee0669864e87fb24b2474d09d14b382965e6fac5f5da2c67c93a73b4578
  search_scope: 'database: UniProtKB; query: (gene_exact:hfaB) AND (organism_id:190650)
    AND (reviewed:true); date: 2026-11-04T12:27:14.632671Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-hfaD-190650
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhfaD%29+AND+%28organism_id%3A190650%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q45977. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:14.632625Z'
  support: supports
  snapshot_sha256: 309b260df306f6d68384d5000101be4a886756c541418486c33087626b7096e5
  search_scope: 'database: UniProtKB; query: (gene_exact:hfaD) AND (organism_id:190650)
    AND (reviewed:true); date: 2026-11-04T12:27:14.632625Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-up-V5IQM7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/V5IQM7.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'V5IQM7: UniProtKB unreviewed (TrEMBL); taxon 367110; gene tokens [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "ESA44030.1"}],
    "value": "spa2"}, "orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313",
    "source": "EMBL", "id": "ESA44030.1"}], "value": "NCU03115"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:18.521490Z'
  support: supports
  snapshot_sha256: ee0cede8d78b4605032c09e5eb113255b2af4426d1005ad625f61459fdb505d5
- evidence_id: septin-up-Q7RVZ1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q7RVZ1.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q7RVZ1: UniProtKB unreviewed (TrEMBL); taxon 367110; gene tokens [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EAA34074.3"}],
    "value": "bud6"}, "orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313",
    "source": "EMBL", "id": "EAA34074.3"}], "value": "NCU08468"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:15.511950Z'
  support: supports
  snapshot_sha256: 73f599a7a5301dd84f4cc2c6e34cdd427139009880223ef6442ba39b3c6adfa2
- evidence_id: septin-up-Q7RWH7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q7RWH7.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q7RWH7: UniProtKB unreviewed (TrEMBL); taxon 367110; gene tokens [{"geneName":
    {"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EAA26755.1"}],
    "value": "bni1"}, "orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313",
    "source": "EMBL", "id": "EAA26755.1"}], "value": "NCU01431"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:19.537222Z'
  support: supports
  snapshot_sha256: 368ebdd6ae660b7568fafba5f8c8dd2bf302041f2123b41d14697d8d58ecd9b5
- evidence_id: septin-tax-5141
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5141
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Neurospora crassa; relevant equivalent/synonym names
    ["Neurospora crassa Shear & B.O. Dodge, 1927:authority", "Neurospora crassa Shear
    & B. O. Dodge 1927:authority", "Chrysonilia crassa:synonym"]. Taxon identity is
    not an experimental-strain substitution.
  accessed_at: '2026-11-04T12:27:14.168323Z'
  support: supports
  snapshot_sha256: 1e5524d77d1448765023e8b9b704ec3cfd7f70016410f33bd7e84a4aaed53ab9
- evidence_id: septin-tax-367110
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/367110
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Neurospora crassa OR74A; relevant equivalent/synonym
    names ["Neurospora crassa FGSC 2489:equivalent name", "Neurospora crassa FGSC
    9013:equivalent name", "Neurospora crassa 74-OR23-1VA:equivalent name", "Neurospora
    crassa N150:equivalent name", "Neurospora crassa 74-OR23-1V A:equivalent name"].
    Taxon identity is not an experimental-strain substitution.
  accessed_at: '2026-11-04T12:27:14.298445Z'
  support: supports
  snapshot_sha256: 87430922c9ed0f8b00941ec27fa887fe61aac644c305423904373674cd3d4c99
- evidence_id: septin-query-spa2-367110
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Aspa2%29+AND+%28organism_id%3A367110%29+AND+%28reviewed%3Afalse%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: V5IQM7. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:16.612091Z'
  support: supports
  snapshot_sha256: 8f8e3f6237924fc0ba75fceb6db541db15f9d7e5bc8fe973609f2178fee50069
  search_scope: 'database: UniProtKB; query: (gene_exact:spa2) AND (organism_id:367110)
    AND (reviewed:false); date: 2026-11-04T12:27:16.612091Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-bud6-367110
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abud6%29+AND+%28organism_id%3A367110%29+AND+%28reviewed%3Afalse%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q7RVZ1. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:15.729597Z'
  support: supports
  snapshot_sha256: 45cf9ee2ef22ec84356240221bca6f867ebfa037ed1ebe833db4e04e8d1447b5
  search_scope: 'database: UniProtKB; query: (gene_exact:bud6) AND (organism_id:367110)
    AND (reviewed:false); date: 2026-11-04T12:27:15.729597Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-bni1-367110
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3Abni1%29+AND+%28organism_id%3A367110%29+AND+%28reviewed%3Afalse%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q7RWH7. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:17.603175Z'
  support: supports
  snapshot_sha256: 580954f955281f412a2f133f3c0ccc8d21eefd0806ed91bcd6c19e1d7f6dc14e
  search_scope: 'database: UniProtKB; query: (gene_exact:bni1) AND (organism_id:367110)
    AND (reviewed:false); date: 2026-11-04T12:27:17.603175Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-up-P43579
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P43579.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P43579: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "IES1"}, "orderedLocusNames": [{"value": "YFL013C"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:16.517666Z'
  support: supports
  snapshot_sha256: 3952c1984f975bb6a4071c099fc5284f2287465e0d564a10d48a6f090ac23118
- evidence_id: septin-up-P53946
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53946.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P53946: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "ARP5"}, "orderedLocusNames": [{"value": "YNL059C"}], "orfNames": [{"value":
    "N2430"}, {"value": "YNL2430C"}]}]. Reference identity is separated from source
    experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:20.615968Z'
  support: supports
  snapshot_sha256: c90a8ed90dacea5ce4ead0ea8d99ad81ecc79a6d017aba33a2da99f415d98dec
- evidence_id: septin-up-Q03940
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03940.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q03940: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "RVB1"}, "synonyms": [{"value": "TIH1"}, {"value": "TIP49A"}], "orderedLocusNames":
    [{"value": "YDR190C"}]}]. Reference identity is separated from source experimental
    membership and necessity.'
  accessed_at: '2026-11-04T12:27:20.653029Z'
  support: supports
  snapshot_sha256: 6ce9d57f84802eaee38756f8f81d75949cd51ac5748b2f2ab3ec1011605bb377
- evidence_id: septin-up-Q03435
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03435.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q03435: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "NHP10"}, "synonyms": [{"value": "HMO2"}], "orderedLocusNames": [{"value":
    "YDL002C"}], "orfNames": [{"value": "YD8119.05C"}]}]. Reference identity is separated
    from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:18.484586Z'
  support: supports
  snapshot_sha256: d190afcc8fc585b5f95ab67afd0e74fa4234ed6f60b6d7a8e2115c0dffab42cf
- evidence_id: septin-up-Q12345
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12345.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q12345: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "IES3"}, "orderedLocusNames": [{"value": "YLR052W"}], "orfNames": [{"value":
    "L2131"}]}]. Reference identity is separated from source experimental membership
    and necessity.'
  accessed_at: '2026-11-04T12:27:19.518399Z'
  support: supports
  snapshot_sha256: f185d4a26f81e4be727e10e91b763208ef5762c7599c5a761b3f5cb17c97bebd
- evidence_id: septin-up-P35189
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P35189.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P35189: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "TAF14"}, "synonyms": [{"value": "ANC1"}, {"value": "CST10"}, {"value":
    "SWP29"}, {"value": "TAF30"}, {"value": "TFG3"}], "orderedLocusNames": [{"value":
    "YPL129W"}]}]. Reference identity is separated from source experimental membership
    and necessity.'
  accessed_at: '2026-11-04T12:27:21.538935Z'
  support: supports
  snapshot_sha256: 0d45bd3db17d72fa09760e05ffdad5bc906237015697a155a6a18c124b201dd6
- evidence_id: septin-up-P60010
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P60010.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P60010: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "ACT1"}, "synonyms": [{"value": "ABY1"}, {"value": "END7"}], "orderedLocusNames":
    [{"value": "YFL039C"}]}]. Reference identity is separated from source experimental
    membership and necessity.'
  accessed_at: '2026-11-04T12:27:22.528984Z'
  support: supports
  snapshot_sha256: 85ccbfada9f62388f2b4f90b3b15fd6e7c5df202249d114e3f5ed8482a086034
- evidence_id: septin-up-P40154
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40154.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P40154: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "IES2"}, "orderedLocusNames": [{"value": "YNL215W"}], "orfNames": [{"value":
    "N1315"}]}]. Reference identity is separated from source experimental membership
    and necessity.'
  accessed_at: '2026-11-04T12:27:23.529546Z'
  support: supports
  snapshot_sha256: 910aeeada31840023e4b258a230c5eac7909885e6fe095ad0650106790604928
- evidence_id: septin-up-Q12386
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12386.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q12386: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "ARP8"}, "orderedLocusNames": [{"value": "YOR141C"}], "orfNames": [{"value":
    "YOR3348C"}]}]. Reference identity is separated from source experimental membership
    and necessity.'
  accessed_at: '2026-11-04T12:27:21.617307Z'
  support: supports
  snapshot_sha256: 43efde4f9e7bcf49d031426d4133cc774968545d5c492760303e953450344cea
- evidence_id: septin-up-P32617
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32617.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P32617: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "IES6"}, "orderedLocusNames": [{"value": "YEL044W"}], "orfNames": [{"value":
    "SYGP-ORF13"}]}]. Reference identity is separated from source experimental membership
    and necessity.'
  accessed_at: '2026-11-04T12:27:24.638686Z'
  support: supports
  snapshot_sha256: 0306da0fb2167dbb6762f9a50a2de40e3ad347864992b6255c262b5c3e6a7303
- evidence_id: septin-up-P80428
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P80428.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P80428: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "ARP4"}, "synonyms": [{"value": "ACT3"}], "orderedLocusNames": [{"value":
    "YJL081C"}], "orfNames": [{"value": "J1012"}]}]. Reference identity is separated
    from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:25.511341Z'
  support: supports
  snapshot_sha256: 4bebfe4b74cce9ed302af0fb7cb01087203cc891ce9e034dace0f5b209b9e1e0
- evidence_id: septin-up-P40060
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40060.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P40060: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "IES5"}, "orderedLocusNames": [{"value": "YER092W"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:23.620583Z'
  support: supports
  snapshot_sha256: b46a8e58f6e005e6c31df1c320206dfcd6437f76de3b6a89295fcf5534c83f2d
- evidence_id: septin-up-P53115
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53115.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'P53115: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "INO80"}, "orderedLocusNames": [{"value": "YGL150C"}], "orfNames": [{"value":
    "G1880"}]}]. Reference identity is separated from source experimental membership
    and necessity.'
  accessed_at: '2026-11-04T12:27:24.618246Z'
  support: supports
  snapshot_sha256: b9dc9eeb0ceb14d664cdc004c6ab5d73d5c9cebd3a5353aac28568e6b6fb59ed
- evidence_id: septin-up-Q12464
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12464.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q12464: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "RVB2"}, "synonyms": [{"value": "TIH2"}, {"value": "TIP49B"}], "orderedLocusNames":
    [{"value": "YPL235W"}], "orfNames": [{"value": "P1060"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:26.514826Z'
  support: supports
  snapshot_sha256: b8c85170bb959c90c301628c98841fdcf738dba14d8c5ca841b8ecfa7e2adad2
- evidence_id: septin-up-Q08561
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08561.json
  locator: Native accession/status/name/all gene tokens/taxon; FUNCTION, SUBUNIT,
    SUBCELLULAR LOCATION, SIMILARITY comments and InterPro cross-references
  summary: 'Q08561: UniProtKB reviewed (Swiss-Prot); taxon 559292; gene tokens [{"geneName":
    {"value": "IES4"}, "orderedLocusNames": [{"value": "YOR189W"}]}]. Reference identity
    is separated from source experimental membership and necessity.'
  accessed_at: '2026-11-04T12:27:22.516995Z'
  support: supports
  snapshot_sha256: e6bcc7f67a8687f05d9e3bdaefe2d6a7672ca19a508800ae921b6451a730c668
- evidence_id: septin-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Saccharomyces cerevisiae; relevant equivalent/synonym
    names ["Saccharomyces cerevisiae 'var. diastaticus':equivalent name", "Saccharomyces
    boulardii:equivalent name", "Saccharomyces boulardii Seguela, Bastide & Massot,
    1984:authority", "Saccharomyces diastaticus J. Andrews & R.B. Gilliland ex Van
    der Walt, 1965:authority", "Mycoderma cerevisiae Desm., 1827:authority", "Saccharomyces
    sp. Af145-1-1:includes", "Saccharomyces uvarum var. melibiosus:synonym", "Saccharomyces
    oviformis:synonym", "Mycoderma cerevisiae:synonym", "Candida robusta:synonym",
    "Saccharomyces cerevisiae (Desm.) Meyen ex E.C. Hansen, 1883:synonym", "Saccharomyces
    boulardii (nom. inval.):synonym", "Saccharomyces italicus:synonym", "Saccharomyces
    capensis:synonym", "Saccharomyces diastaticus:synonym", "brewer's yeast:genbank
    common name"]. Taxon identity is not an experimental-strain substitution.
  accessed_at: '2026-11-04T12:27:23.276775Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Entire native taxon identity/names/lineage
  summary: Native scientific name Saccharomyces cerevisiae S288C; relevant equivalent/synonym
    names []. Taxon identity is not an experimental-strain substitution.
  accessed_at: '2026-11-04T12:27:23.308608Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-pmid-19355820
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19355820+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: The biology of chromatin remodeling complexes.; Clapier
    CR, Cairns BR.. Metadata supports source identity only; the separately classified
    abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:23.887562Z'
  support: context_only
  snapshot_sha256: 1b4c8ee687144e09185d06ce8451ce95c97ae68efad453f638867c2bd353ba64
  search_scope: 'database: Europe PMC MED; query: EXT_ID:19355820 AND SRC:MED; date:
    2026-11-04T12:27:23.887562Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-19355820-abstract
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19355820+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Clapier and Cairns 2009 is a secondary review; its abstract supplies general
    remodeling context, not a new assembly assay.
  accessed_at: '2026-11-04T12:27:23.887562Z'
  support: context_only
  snapshot_sha256: 1b4c8ee687144e09185d06ce8451ce95c97ae68efad453f638867c2bd353ba64
- evidence_id: septin-pmid-12887900
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12887900+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Involvement of actin-related proteins in ATP-dependent
    chromatin remodeling.; Shen X, Ranallo R, Choi E, Wu C.. Metadata supports source
    identity only; the separately classified abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:23.942336Z'
  support: context_only
  snapshot_sha256: 433d59bd77b17f5639c2de86bf8f334ebb1bed7dc91259a6b30277bc022faa4b
  search_scope: 'database: Europe PMC MED; query: EXT_ID:12887900 AND SRC:MED; date:
    2026-11-04T12:27:23.942336Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-12887900-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12887900+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:23.942336Z'
  support: supports
  snapshot_sha256: 433d59bd77b17f5639c2de86bf8f334ebb1bed7dc91259a6b30277bc022faa4b
- evidence_id: septin-pmid-10787406
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10787406+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: The Saccharomyces cerevisiae RuvB-like protein, Tih2p,
    is required for cell cycle progression and RNA polymerase II-directed transcription.;
    Lim CR, Kimata Y, Ohdate H, Kokubo T, Kikuchi N, Horigome T, Kohno K.. Metadata
    supports source identity only; the separately classified abstract has its own
    scientific scope.'
  accessed_at: '2026-11-04T12:27:24.141196Z'
  support: context_only
  snapshot_sha256: f22f7d8936828d73c077e1be33ef4000492ffe1ab833c89904e4b7034abc986d
  search_scope: 'database: Europe PMC MED; query: EXT_ID:10787406 AND SRC:MED; date:
    2026-11-04T12:27:24.141196Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-10787406-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10787406+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:24.141196Z'
  support: supports
  snapshot_sha256: f22f7d8936828d73c077e1be33ef4000492ffe1ab833c89904e4b7034abc986d
- evidence_id: septin-pmid-8573785
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8573785+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: The actin-related protein Act3p of Saccharomyces
    cerevisiae is located in the nucleus.; Weber V, Harata M, Hauser H, Wintersberger
    U.. Metadata supports source identity only; the separately classified abstract
    has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:24.267497Z'
  support: context_only
  snapshot_sha256: 0eeae14e4a798c19dc9345bc20104ee722d3c9be237d652e6b219a15510ff227
  search_scope: 'database: Europe PMC MED; query: EXT_ID:8573785 AND SRC:MED; date:
    2026-11-04T12:27:24.267497Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-8573785-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8573785+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:24.267497Z'
  support: supports
  snapshot_sha256: 0eeae14e4a798c19dc9345bc20104ee722d3c9be237d652e6b219a15510ff227
- evidence_id: septin-pmid-15525518
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15525518+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Rvb1p/Rvb2p recruit Arp5p and assemble a functional
    Ino80 chromatin remodeling complex.; Jónsson ZO, Jha S, Wohlschlegel JA, Dutta
    A.. Metadata supports source identity only; the separately classified abstract
    has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:24.523009Z'
  support: context_only
  snapshot_sha256: 3e44948b63e5914d15efb52bb6c8b9dac14c9ea8ff31d6d70118ba688f166a4e
  search_scope: 'database: Europe PMC MED; query: EXT_ID:15525518 AND SRC:MED; date:
    2026-11-04T12:27:24.523009Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-15525518-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15525518+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:24.523009Z'
  support: supports
  snapshot_sha256: 3e44948b63e5914d15efb52bb6c8b9dac14c9ea8ff31d6d70118ba688f166a4e
- evidence_id: septin-pmid-11604509
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11604509+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: A well-connected and conserved nucleoplasmic helicase
    is required for production of box C/D and H/ACA snoRNAs and localization of snoRNP
    proteins.; King TH, Decatur WA, Bertrand E, Maxwell ES, Fournier MJ.. Metadata
    supports source identity only; the separately classified abstract has its own
    scientific scope.'
  accessed_at: '2026-11-04T12:27:24.539985Z'
  support: context_only
  snapshot_sha256: 9928d5d106809fc46ce0c7da4a6d5c91d9a30d189427ef50188b55e2ffa05757
  search_scope: 'database: Europe PMC MED; query: EXT_ID:11604509 AND SRC:MED; date:
    2026-11-04T12:27:24.539985Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-11604509-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11604509+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:24.539985Z'
  support: supports
  snapshot_sha256: 9928d5d106809fc46ce0c7da4a6d5c91d9a30d189427ef50188b55e2ffa05757
- evidence_id: septin-pmid-10952318
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10952318+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: A chromatin remodelling complex involved in transcription
    and DNA processing.; Shen X, Mizuguchi G, Hamiche A, Wu C.. Metadata supports
    source identity only; the separately classified abstract has its own scientific
    scope.'
  accessed_at: '2026-11-04T12:27:24.750558Z'
  support: context_only
  snapshot_sha256: 6ff28db0dfddd2215a5042e23520037f4b7b01f250a6d31c3b808e48dc538436
  search_scope: 'database: Europe PMC MED; query: EXT_ID:10952318 AND SRC:MED; date:
    2026-11-04T12:27:24.750558Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-10952318-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10952318+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:24.750558Z'
  support: supports
  snapshot_sha256: 6ff28db0dfddd2215a5042e23520037f4b7b01f250a6d31c3b808e48dc538436
- evidence_id: septin-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Global analysis of protein localization in budding
    yeast.; Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea
    EK.. Metadata supports source identity only; the separately classified abstract
    has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:24.895844Z'
  support: context_only
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
  search_scope: 'database: Europe PMC MED; query: EXT_ID:14562095 AND SRC:MED; date:
    2026-11-04T12:27:24.895844Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-14562095-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:24.895844Z'
  support: supports
  snapshot_sha256: 22cb10c77fae30f93c6690dedcb90031ab7d7b93d5fa08626a202a6ceb9d7ba1
- evidence_id: septin-pmid-24034245
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24034245+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Structure and subunit topology of the INO80 chromatin
    remodeler and its nucleosome complex.; Tosi A, Haas C, Herzog F, Gilmozzi A, Berninghausen
    O, Ungewickell C, Gerhold CB, Lakomek K, Aebersold R, Beckmann R, Hopfner KP..
    Metadata supports source identity only; the separately classified abstract has
    its own scientific scope.'
  accessed_at: '2026-11-04T12:27:25.112275Z'
  support: context_only
  snapshot_sha256: e425a1deb46b89eba9ccc795baedb8b06ba8306ac084e70349e21087a53e30b4
  search_scope: 'database: Europe PMC MED; query: EXT_ID:24034245 AND SRC:MED; date:
    2026-11-04T12:27:25.112275Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-24034245-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A24034245+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:25.112275Z'
  support: supports
  snapshot_sha256: e425a1deb46b89eba9ccc795baedb8b06ba8306ac084e70349e21087a53e30b4
- evidence_id: septin-pmid-25964121
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25964121+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Structural analyses of the chromatin remodelling
    enzymes INO80-C and SWR-C.; Watanabe S, Tan D, Lakshminarasimhan M, Washburn MP,
    Hong EJ, Walz T, Peterson CL.. Metadata supports source identity only; the separately
    classified abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:25.135240Z'
  support: context_only
  snapshot_sha256: dd38ab75624f728384bc107f83d416f170c6e166fa72b65a6a07e4110b4d2575
  search_scope: 'database: Europe PMC MED; query: EXT_ID:25964121 AND SRC:MED; date:
    2026-11-04T12:27:25.135240Z; limit: Exact DOI/PMID lookup; all returned MED identities
    inspected'
- evidence_id: septin-pmid-25964121-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25964121+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:25.135240Z'
  support: supports
  snapshot_sha256: dd38ab75624f728384bc107f83d416f170c6e166fa72b65a6a07e4110b4d2575
- evidence_id: septin-query-INO80-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AINO80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P53115. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:28.708668Z'
  support: supports
  snapshot_sha256: dfab6fcc3656cde7bff6cd000ac804e917e12fc74764bebc269c4ba434d47b29
  search_scope: 'database: UniProtKB; query: (gene_exact:INO80) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:28.708668Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-RVB1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARVB1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q03940. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:26.632495Z'
  support: supports
  snapshot_sha256: 19d983274f1d43c56a52213b12a4847a72bc9eeb895800873ff8efaa77412c0b
  search_scope: 'database: UniProtKB; query: (gene_exact:RVB1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:26.632495Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-RVB2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARVB2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q12464. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:25.588410Z'
  support: supports
  snapshot_sha256: cfa1a99d691fa90e857f06d9773f252b82563cba006643483f4b3690220999dd
  search_scope: 'database: UniProtKB; query: (gene_exact:RVB2) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:25.588410Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-IES5-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P40060. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:30.574216Z'
  support: supports
  snapshot_sha256: b2a1931fe4102218838e2479af3ccc3c9e3ed21e4b890ad5e88e93d059503d4e
  search_scope: 'database: UniProtKB; query: (gene_exact:IES5) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:30.574216Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-IES3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q12345. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:27.592266Z'
  support: supports
  snapshot_sha256: 2e6508e593849083e65973f6b0ecfc2778f0b016eee9f30d0a6ade0dd945dbfc
  search_scope: 'database: UniProtKB; query: (gene_exact:IES3) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:27.592266Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-NHP10-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANHP10%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q03435. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:29.597366Z'
  support: supports
  snapshot_sha256: 0e405a042c9fc43dcbbf84cca1e867cac0c6f666647346f6b17af10e77b770de
  search_scope: 'database: UniProtKB; query: (gene_exact:NHP10) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:29.597366Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-IES6-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P32617. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:29.561969Z'
  support: supports
  snapshot_sha256: be371a8ee6aaf54c5b8aa63124fd1c9c2e9126ea38010f84243f9c5027e0ac83
  search_scope: 'database: UniProtKB; query: (gene_exact:IES6) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:29.561969Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-IES1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P43579. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:32.685566Z'
  support: supports
  snapshot_sha256: 59b51421e92698c1a27620d2e7aaa9eed1dee13b1c9fac022ad605e996bcffb5
  search_scope: 'database: UniProtKB; query: (gene_exact:IES1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:32.685566Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-ARP8-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q12386. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:31.589723Z'
  support: supports
  snapshot_sha256: 537762f3265784d48900bc894debafaefdcada8036b1aed372aaacfcc5358abc
  search_scope: 'database: UniProtKB; query: (gene_exact:ARP8) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:31.589723Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-ARP4-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARP4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P80428. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:27.640477Z'
  support: supports
  snapshot_sha256: d2c9d987fa278db85dbf167406d062a9760137dfc8c724cbe48dc7bb07969ec4
  search_scope: 'database: UniProtKB; query: (gene_exact:ARP4) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:27.640477Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-ACT1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AACT1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P60010. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:28.604212Z'
  support: supports
  snapshot_sha256: 5f32bb1ef917c3425db2aaa4a4d4f98e2a08794a7994a79de7a51aabe7b8c75c
  search_scope: 'database: UniProtKB; query: (gene_exact:ACT1) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:28.604212Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-TAF14-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATAF14%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P35189. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:31.619977Z'
  support: supports
  snapshot_sha256: f745d1cb34d5e820ca3f8a5dacff6aa7347f97b2cb877177acee3e21d184436b
  search_scope: 'database: UniProtKB; query: (gene_exact:TAF14) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:31.619977Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-IES2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P40154. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:33.644664Z'
  support: supports
  snapshot_sha256: 37d2509986c803299074a49e50976ad8554a26d4cdca090625152a188c6d325e
  search_scope: 'database: UniProtKB; query: (gene_exact:IES2) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:33.644664Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-IES4-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIES4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: Q08561. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:30.576587Z'
  support: supports
  snapshot_sha256: ff983e70eb43afeee1f17db2377f0a29039ffb8fb3777e448e6d91474149c36b
  search_scope: 'database: UniProtKB; query: (gene_exact:IES4) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:30.576587Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-query-ARP5-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARP5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned accession/name/gene/organism/status results; current
    exact query only
  summary: 'Current response contains 1 entries: P53946. No historical query result
    or biological absence is inferred.'
  accessed_at: '2026-11-04T12:27:32.661250Z'
  support: supports
  snapshot_sha256: 0f63c75513a1c10572751c5e81801aea4dcf8926ae0f05d40ae80d32bac79264
  search_scope: 'database: UniProtKB; query: (gene_exact:ARP5) AND (organism_id:559292)
    AND (reviewed:true); date: 2026-11-04T12:27:32.661250Z; limit: size=100; complete
    one-page current returned result, primary names and aliases distinguished'
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0000228,GO:0001411,GO:0006338,GO:0030427,GO:0031011,GO:0031012,GO:0031521,GO:0031562,GO:0051286,GO:0097346
  locator: 'Complete eleven-term response: names, definitions, synonyms and typed
    relationships'
  summary: Exact hyphal tip is fungal; GO0030427 is site of polarized growth. Polarisome/Spitzenkorper
    and Ino80 complex links retain correct parthood/is-a semantics. Extracellular
    matrix is broader than the local holdfast identity.
  accessed_at: '2026-11-04T12:27:30.207977Z'
  support: supports
  snapshot_sha256: ffc35165893658e0a39a37bca98ecfdfe062d36153987686ecc71c0ac3df3a62
- evidence_id: septin-go-0001411-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001411/ancestors?relations=is_a
  locator: Complete requested is_a-only ancestor response
  summary: Typed is-a ancestry is assessed independently from parthood; no transitive
    relation is falsely reported as a direct edge.
  accessed_at: '2026-11-04T12:27:30.789829Z'
  support: supports
  snapshot_sha256: 33ac2cae2d1346a8490cee7c367c2cddcafe714f1e5291b63404b9ad3bfef268
- evidence_id: septin-go-0031562-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031562/ancestors?relations=is_a
  locator: Complete requested is_a-only ancestor response
  summary: Typed is-a ancestry is assessed independently from parthood; no transitive
    relation is falsely reported as a direct edge.
  accessed_at: '2026-11-04T12:27:31.166164Z'
  support: supports
  snapshot_sha256: 455ac47ad87eb3fffba55266395665e48d2f7923cec1f298ea7855408c3ed71e
- evidence_id: septin-go-0031011-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031011/ancestors?relations=is_a
  locator: Complete requested is_a-only ancestor response
  summary: Typed is-a ancestry is assessed independently from parthood; no transitive
    relation is falsely reported as a direct edge.
  accessed_at: '2026-11-04T12:27:31.191237Z'
  support: supports
  snapshot_sha256: b58b1405dc99c87a6e14a83a19fe01f279b3d2f4cfc27079eb1da897cd7500e7
- evidence_id: septin-go-search-holdfast
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=holdfast&limit=100
  locator: Complete zero-hit exact-text search response
  summary: No exact holdfast term returned in this bounded current GO search. This
    supports retaining the local identifier with broader matrix parent; it is not
    an exhaustive assertion about all ontologies.
  accessed_at: '2026-11-04T12:27:31.384510Z'
  support: supports
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  search_scope: 'database: QuickGO ontology search; query: holdfast; date: 2026-11-04T12:27:31.384510Z;
    limit: limit=100, complete zero-hit response'
- evidence_id: septin-sulkowski-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00112-19%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: A Multiprotein Complex Anchors Adhesive Holdfast
    at the Outer Membrane of Caulobacter crescentus.; Sulkowski NI, Hardy GG, Brun
    YV, Bharat TAM.. Metadata supports source identity only; the separately classified
    abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:31.777183Z'
  support: context_only
  snapshot_sha256: ed02084c8fa6cb0cac42e1061ba5054ba356aeb1fd97f5e5b0c4fb1a009f86dc
  search_scope: 'database: Europe PMC MED; query: DOI:"10.1128/JB.00112-19" AND SRC:MED;
    date: 2026-11-04T12:27:31.777183Z; limit: Exact DOI/PMID lookup; all returned
    MED identities inspected'
- evidence_id: septin-sulkowski-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00112-19%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:31.777183Z'
  support: supports
  snapshot_sha256: ed02084c8fa6cb0cac42e1061ba5054ba356aeb1fd97f5e5b0c4fb1a009f86dc
- evidence_id: septin-hershey-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00276-19%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Composition of the Holdfast Polysaccharide from <i>Caulobacter
    crescentus</i>.; Hershey DM, Porfírio S, Black I, Jaehrig B, Heiss C, Azadi P,
    Fiebig A, Crosson S.. Metadata supports source identity only; the separately classified
    abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:32.021603Z'
  support: context_only
  snapshot_sha256: dc689be5550cdefa44ce6e8ef1b2318ba026c4ad2edc8af35655c3aba469c531
  search_scope: 'database: Europe PMC MED; query: DOI:"10.1128/JB.00276-19" AND SRC:MED;
    date: 2026-11-04T12:27:32.021603Z; limit: Exact DOI/PMID lookup; all returned
    MED identities inspected'
- evidence_id: septin-hershey-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FJB.00276-19%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:32.021603Z'
  support: supports
  snapshot_sha256: dc689be5550cdefa44ce6e8ef1b2318ba026c4ad2edc8af35655c3aba469c531
- evidence_id: septin-sprecher-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FmBio.00294-17%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Cohesive Properties of the <i>Caulobacter crescentus</i>
    Holdfast Adhesin Are Regulated by a Novel c-di-GMP Effector Protein.; Sprecher
    KS, Hug I, Nesper J, Potthoff E, Mahi MA, Sangermani M, Kaever V, Schwede T, Vorholt
    J, Jenal U.. Metadata supports source identity only; the separately classified
    abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:32.220794Z'
  support: context_only
  snapshot_sha256: cb53c431495facc6e1a8a36b767c55ea8c7d06283970b86df15ec80fa41aff5c
  search_scope: 'database: Europe PMC MED; query: DOI:"10.1128/mBio.00294-17" AND
    SRC:MED; date: 2026-11-04T12:27:32.220794Z; limit: Exact DOI/PMID lookup; all
    returned MED identities inspected'
- evidence_id: septin-sprecher-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128%2FmBio.00294-17%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:32.220794Z'
  support: supports
  snapshot_sha256: cb53c431495facc6e1a8a36b767c55ea8c7d06283970b86df15ec80fa41aff5c
- evidence_id: septin-lichius-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pone.0030372%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Comparative live-cell imaging analyses of SPA-2,
    BUD-6 and BNI-1 in Neurospora crassa reveal novel features of the filamentous
    fungal polarisome.; Lichius A, Yáñez-Gutiérrez ME, Read ND, Castro-Longoria E..
    Metadata supports source identity only; the separately classified abstract has
    its own scientific scope.'
  accessed_at: '2026-11-04T12:27:35.024826Z'
  support: context_only
  snapshot_sha256: 658eb816a8130254f855ae8837ed80788fa385a13f17407b2392aa9d5b93de74
  search_scope: 'database: Europe PMC MED; query: DOI:"10.1371/journal.pone.0030372"
    AND SRC:MED; date: 2026-11-04T12:27:35.024826Z; limit: Exact DOI/PMID lookup;
    all returned MED identities inspected'
- evidence_id: septin-lichius-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.pone.0030372%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:35.024826Z'
  support: supports
  snapshot_sha256: 658eb816a8130254f855ae8837ed80788fa385a13f17407b2392aa9d5b93de74
- evidence_id: septin-watanabe-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms8108%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: 'Complete exact MED bibliographic record: authors/title/year/DOI/PMID and
    abstract availability'
  summary: 'Native bibliography: Structural analyses of the chromatin remodelling
    enzymes INO80-C and SWR-C.; Watanabe S, Tan D, Lakshminarasimhan M, Washburn MP,
    Hong EJ, Walz T, Peterson CL.. Metadata supports source identity only; the separately
    classified abstract has its own scientific scope.'
  accessed_at: '2026-11-04T12:27:32.940261Z'
  support: context_only
  snapshot_sha256: 7d23449adeeade0f767538eed3931ff74604c9abb251aa7ecabfa9362e0d479a
  search_scope: 'database: Europe PMC MED; query: DOI:"10.1038/ncomms8108" AND SRC:MED;
    date: 2026-11-04T12:27:32.940261Z; limit: Exact DOI/PMID lookup; all returned
    MED identities inspected'
- evidence_id: septin-watanabe-metadata-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fncomms8108%22+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: Complete available abstractText only; no main-body, figure-pixel, supplement
    or raw-data access implied
  summary: Independently read complete native primary abstract. Its stated species,
    assays and limitations remain bounded; no unreported Methods details inferred.
  accessed_at: '2026-11-04T12:27:32.940261Z'
  support: supports
  snapshot_sha256: 7d23449adeeade0f767538eed3931ff74604c9abb251aa7ecabfa9362e0d479a
- evidence_id: septin-ipr-IPR038014
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR038014/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR038014 name {''name'': ''Ino80 subunit 1'', ''short'': ''Ies1''},
    type family. Curated family boundary is distinguished from shared domains/paralogue
    classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:33.539013Z'
  support: supports
  snapshot_sha256: 411cab4340cf3f52db50591caf31e013c5ca43c990c9c5cdd6b1b1a1f10c1b67
- evidence_id: septin-ipr-IPR029523
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029523/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR029523 name {''name'': ''INO80 complex, subunit Ies2'', ''short'':
    ''INO80B/Ies2''}, type family. Curated family boundary is distinguished from shared
    domains/paralogue classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:33.808696Z'
  support: supports
  snapshot_sha256: 0c23206dd564ba1b40ed445882d0fd2a7eb8e1baa4c25aa887f40d87de613928
- evidence_id: septin-ipr-IPR062650
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062650/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR062650 name {''name'': ''INO80 complex subunit 4'', ''short'':
    ''IES4''}, type family. Curated family boundary is distinguished from shared domains/paralogue
    classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:33.966778Z'
  support: supports
  snapshot_sha256: 8bbb43f4200ee8ace175f0aaf9674470d749ef84d48d7934603a1a2f87aad507
- evidence_id: septin-ipr-IPR020366
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020366/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR020366 name {''name'': ''INO80 complex subunit Ies5'', ''short'':
    ''Ies5''}, type family. Curated family boundary is distinguished from shared domains/paralogue
    classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:34.173423Z'
  support: supports
  snapshot_sha256: 6d7a29f25d365a7c074ec341d6c2dac875dfb6891af00585963a9f397cf0e39f
- evidence_id: septin-ipr-IPR029525
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029525/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR029525 name {''name'': ''INO80 complex, subunit Ies6'', ''short'':
    ''INO80C/Ies6''}, type family. Curated family boundary is distinguished from shared
    domains/paralogue classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:34.254304Z'
  support: supports
  snapshot_sha256: 55f39022487454ed9f07df394057eac2c8ec18ff3a89765b7f32a3633611dd5d
- evidence_id: septin-ipr-IPR050520
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050520/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR050520 name {''name'': ''INO80/SWR1 chromatin remodeling helicase'',
    ''short'': ''INO80/SWR1_helicase''}, type family. Machine-generated unchecked
    descriptive prose is excluded from biological support; only native classification
    identity and independently verified membership used. This entry alone does not
    prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:34.402785Z'
  support: supports
  snapshot_sha256: 9d6834b933901b2a309b3f7ac4d9fef9d43a937289b8a503a1c62f07dd145c25
- evidence_id: septin-ipr-IPR027238
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027238/
  locator: Actual failed HTTP retrieval
  summary: HTTP 429 did not supply a usable authority entry; successful bounded retry
    is separately recorded.
  accessed_at: '2026-11-04T12:27:34.595893Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR004000
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/
  locator: Actual failed HTTP retrieval
  summary: HTTP 429 did not supply a usable authority entry; successful bounded retry
    is separately recorded.
  accessed_at: '2026-11-04T12:27:34.751173Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR016665
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016665/
  locator: Actual failed HTTP retrieval
  summary: HTTP 429 did not supply a usable authority entry; successful bounded retry
    is separately recorded.
  accessed_at: '2026-11-04T12:27:34.755443Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR050342
  kind: validation
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050342/
  locator: Actual failed HTTP retrieval
  summary: HTTP 429 did not supply a usable authority entry; successful bounded retry
    is separately recorded.
  accessed_at: '2026-11-04T12:27:34.841271Z'
  support: context_only
  snapshot_sha256: 9abf9cb941ee77b8e8a3348aa3517c7fbb81c7ae7cb580ff9d1b87961335b26f
- evidence_id: septin-ipr-IPR039892
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR039892 name {''name'': ''Protein Spa2/Sph1'', ''short'': ''Spa2/Sph1''},
    type family. Curated family boundary is distinguished from shared domains/paralogue
    classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:35.007002Z'
  support: supports
  snapshot_sha256: 6476f3f836012c74087ca05a1402415a40723e51e74135035b060d96fafabc01
- evidence_id: septin-ipr-IPR051825
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR051825 name {''name'': ''SRC Kinase Signaling Inhibitor'', ''short'':
    ''SRCIN1''}, type family. Machine-generated unchecked descriptive prose is excluded
    from biological support; only native classification identity and independently
    verified membership used. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:35.197810Z'
  support: supports
  snapshot_sha256: 34dc77dcf99b4747caa75d530205831b3d9edd66f5e4df7833319637fb3bb245
- evidence_id: septin-ipr-IPR051661
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051661/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR051661 name {''name'': ''Actin filament dynamics regulator'',
    ''short'': ''Actin_filament_regulator''}, type family. Machine-generated unchecked
    descriptive prose is excluded from biological support; only native classification
    identity and independently verified membership used. This entry alone does not
    prove assembly necessity.'
  accessed_at: '2026-11-04T12:27:35.445445Z'
  support: supports
  snapshot_sha256: babdb17855c5f01a4a0410ef193cff0c2e95c9eaafe0dfda2a58b7bad3b33e04
- evidence_id: septin-retry-IPR027238
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027238/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR027238 name {''name'': ''RuvB-like'', ''short'': ''RuvB-like''},
    type family. Curated family boundary is distinguished from shared domains/paralogue
    classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:28:13.351279Z'
  support: supports
  snapshot_sha256: 08a048c568949fbb29f30855b9421944a74e5d6f06de1dc6ffbeea6dd11ce7e2
- evidence_id: septin-retry-IPR004000
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR004000 name {''name'': ''Actin family'', ''short'': ''Actin''},
    type family. Curated family boundary is distinguished from shared domains/paralogue
    classes. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:28:13.454684Z'
  support: supports
  snapshot_sha256: 353427570f0d1c3842a14f7737374f68e9dd70a98b09cf9fc2a8e8c86062edca
- evidence_id: septin-retry-IPR016665
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016665/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR016665 name {''name'': ''SAS complex subunit SAS5/transcription
    initiation factor TFIID subunit 14'', ''short'': ''Sas5/TAF14''}, type family.
    Curated family boundary is distinguished from shared domains/paralogue classes.
    This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:28:13.645308Z'
  support: supports
  snapshot_sha256: ca6de0795e5014bc6d92ea86f320ac302e4f829fd285239c863862f2d2d365d5
- evidence_id: septin-retry-IPR050342
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050342/
  locator: Native entry accession/name/type, member signatures, annotation curation
    flags; exact UniProt family joins checked independently
  summary: 'Native IPR050342 name {''name'': ''High Mobility Group Box (HMGB)'', ''short'':
    ''HMGB''}, type family. Machine-generated unchecked descriptive prose is excluded
    from biological support; only native classification identity and independently
    verified membership used. This entry alone does not prove assembly necessity.'
  accessed_at: '2026-11-04T12:28:14.153619Z'
  support: supports
  snapshot_sha256: b1f3db4bfdcbc2e07497675d9db436601cc9bc73b9f86085eb8285826b0ccbea
- evidence_id: septin-sulkowski-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6707917/fullTextXML
  locator: Genuine JATS title; full Introduction, Results s2.1–s2.3, Table1 and embedded
    figure captions; Discussion and Methods s4.1–s4.7
  summary: CB15 and CB15-derived strains support HfaABD anchor structure/retention,
    with HfaB density loss and A/D surface assignment. Hfa mutants can still synthesize
    and shed matrix. Actual title says Outer Membrane, not Old Cell Pole. No figure
    pixels, tomogram reanalysis or supplementary asset inspection.
  accessed_at: '2026-11-04T12:27:32.269481Z'
  support: supports
  snapshot_sha256: b69005fc396b3239a040bbbf3d432fe9b5ba0e92c176ac0f35b13e1d2c39ca11
- evidence_id: septin-sprecher-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5362036/fullTextXML
  locator: Genuine JATS complete abstract; Results s1.2/s1.3/s1.5/s1.7, Discussion
    s2 and growth Methods s3.1; embedded relevant figure/supplement captions only
  summary: CB15 experiments establish HfsK-dependent cohesion/shear resistance, c-di-GMP
    binding and localization. NA1000 is an explicitly nonadherent comparator. Catalytic
    acylation/substrate chemistry remains proposed; altered cohesion and/or anchoring
    are distinguished. Actual supplementary videos/pixels were not inspected.
  accessed_at: '2026-11-04T12:27:33.189307Z'
  support: supports
  snapshot_sha256: 907704232d9b03c8d9056f774290db4099b7c477f1f08ea7374eaefbe0b3e84a
- evidence_id: septin-lichius-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3265482/fullTextXML
  locator: Genuine JATS complete abstract; Results s2b/s2e/s2f/s2i–s2l/s2n/s2o, Table2
    and relevant embedded captions; Discussion s3a–s3e/s3g; Methods s4a
  summary: Neurospora source distinguishes mature-tip SPA2/BUD6/BNI1 topology, early
    polarity, septal plugging and polarisome-independent septation/cytokinesis. N150/FGSC9013
    and named derived strains are explicit; OR74A authority includes N150/FGSC9013
    synonyms, without making every deletion strain identical. Delta bud6/bni1 disrupt
    Spk/tip organization but permit altered polarized growth, so no universal growth/assembly
    necessity is inferred. No pixels/videos or unlisted supplements read.
  accessed_at: '2026-11-04T12:27:42.245104Z'
  support: supports
  snapshot_sha256: 281f73a0f66fcac1d984a991311c6b3d8764e788c99972206f5faea072f3187d
- evidence_id: septin-watanabe-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4431590.1/PMC4431590.1.xml
  locator: Genuine S3 JATS Results S3–S7, Discussion S8, Methods S10/S17; exact paper
    bibliography/abstract and relevant embedded text
  summary: Fifteen named INO80 classes are recovered by TAP purifications; Ies6/Arp5
    loss cripples remodeling activity while residual complexes remain. Arp8 module
    loss reduces rather than abolishes several activities. Rvb ring-count disagreement
    with Tosi is explicit; the record does not impose a contested fixed molecular
    count or claim helicase activity. No pixels/coordinates/raw MS data inspected.
  accessed_at: '2026-11-04T12:29:14.322330Z'
  support: supports
  snapshot_sha256: 854977b35f6e2641c459e9da09e4f251b620ea32daea645449fbf3d8ff5acaee
- evidence_id: septin-watanabe-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4431590.1/NIHMS677628-supplement-1.pdf
  locator: Published supplementary PDF, extracted complete Supplementary Tables1 and2
    and their captions on the final two pages; no image-pixel inspection
  summary: Table2 names all fifteen INO80 classes and reports spectral counts/sequence
    coverage across three independent preparations. Table1 is SWR-C; inverted main-text
    table references are not propagated. Fifteen subunit identities are not fifteen
    total molecular copies. Supplementary figure pixels and raw spectra were not analyzed.
  accessed_at: '2026-11-04T12:27:34.154046Z'
  support: supports
  snapshot_sha256: e2617d57e5578b4cb1d9c3b3a4b75e2ff5ffba9a73bdfa90fe1b0da7426b127b
- evidence_id: septin-hershey-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6689307/fullTextXML
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Actual route status 500 did not supply a usable article body. Successful
    alternative or primary-abstract support is separately scoped.
  accessed_at: '2026-11-04T12:27:40.098202Z'
  support: context_only
  snapshot_sha256: 8c52b0bd3c3223929dc26670089707950d894a761445245d76027d5dd3c5c50c
- evidence_id: septin-watanabe-xml
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4431590/fullTextXML
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Actual route status 500 did not supply a usable article body. Successful
    alternative or primary-abstract support is separately scoped.
  accessed_at: '2026-11-04T12:27:33.361241Z'
  support: context_only
  snapshot_sha256: eff173f9e145cd7e7aa0af0c0f4a6ed6aab0071d6e5f23a94c2e201140582b15
- evidence_id: septin-hershey-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6689307/
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: HTTP200 browser-check/challenge content; no genuine main body obtained.
  accessed_at: '2026-11-04T12:28:12.745208Z'
  support: context_only
  snapshot_sha256: 4440607157d877ef07f18b89f3af60a2bb7ac93b3ef2672d8c94450065835e18
- evidence_id: septin-watanabe-html
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4431590/
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: HTTP200 browser-check/challenge content; no genuine main body obtained.
  accessed_at: '2026-11-04T12:28:12.753194Z'
  support: context_only
  snapshot_sha256: 5fabf8f08305358941002abeeaee9da6fc6228811c7adc1a4ef0cc36cb8656a0
- evidence_id: septin-hershey-s3xml
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6689307.1/PMC6689307.xml
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Actual route status 404 did not supply a usable article body. Successful
    alternative or primary-abstract support is separately scoped.
  accessed_at: '2026-11-04T12:28:12.840053Z'
  support: context_only
  snapshot_sha256: fbcfeac0b85748144a96473a2a13bfd07333cd4b2b02413db7b344b86a7e9c25
- evidence_id: septin-watanabe-s3xml
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4431590.1/PMC4431590.xml
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Actual route status 404 did not supply a usable article body. Successful
    alternative or primary-abstract support is separately scoped.
  accessed_at: '2026-11-04T12:28:13.011888Z'
  support: context_only
  snapshot_sha256: 4ba7f83e498739fc1531b9651f9f307ce9ca40755908a64bd0eefebf8a20e7fb
- evidence_id: septin-hershey-s3listing
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC6689307.1/
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Exact specified public S3 package-prefix listing returned no entries (not
    truncated). This is only a bounded access-route result, not absence of the article
    or scientific refutation.
  accessed_at: '2026-11-04T12:28:55.978391Z'
  support: context_only
  snapshot_sha256: 9f385d176c210798d62702631907fde89dbe51e2937bff92725bbee8e4c34ef2
- evidence_id: septin-watanabe-s3listing
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC4431590.1/
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Exact S3 package listing located the genuine versioned XML and supplementary
    PDF; directory metadata is not scientific evidence.
  accessed_at: '2026-11-04T12:28:56.250655Z'
  support: context_only
  snapshot_sha256: 695545ae4ec2af17808a1a43c0adf82e5323513ce352ea4e6774952200d9c379
- evidence_id: septin-hershey-package-list
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC6689307
  locator: Actual HTTP/status/body or exact package-list diagnostic only
  summary: Exact specified public S3 package-prefix listing returned no entries (not
    truncated). This is only a bounded access-route result, not absence of the article
    or scientific refutation.
  accessed_at: '2026-11-04T12:29:13.840160Z'
  support: context_only
  snapshot_sha256: 0832bc558492ef80daec2eb1eb87e980e1b92736126522a8d9edf80f2cf49b7d
- evidence_id: septin-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/organisms
  locator: All twenty returned organism rows and their dataset names; exact target-host
    and synonym checks
  summary: No Caulobacter vibrioides/crescentus, CB15/NA1000, Neurospora, Saccharomyces,
    Candida or Ashbya host dataset is represented. E. coli expression/cloning hosts
    are not substituted for biological targets. Downstream matched gene/module queries
    are therefore not applicable; absence is catalogue coverage only, not biology.
  accessed_at: '2026-11-04T12:24:20.225750Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: 'database: Official iModulonDB complete organisms endpoint; query:
    GET https://imodulondb.org/api/organisms; exact organism/synonym matching for
    all named record/source hosts; date: 2026-11-04T12:24:20.225750Z; limit: Complete
    twenty-organism response; no cross-species proxy or downstream unmatched dataset'
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z
  summary: Historical runner failed exit1 with PermissionError reading pyvenv.cfg.
    No fresh runner invocation is claimed. Current independently inspected official
    catalogue and native primary/authority checks provide the declared fallback.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/adversary-septin/original-checks.json
  locator: Actual four native validate/render pairs plus exact historical Git-object
    input hashes
  summary: All four original pairs validate/render0 and Markdown is exact. All 55
    frozen historical input occurrences match. All four current records are nonstale.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 000e78176de784e86a0af2d4f01ea83a660b58de98d43dea9a047b3f80e8dc2a
- evidence_id: septin-record-holdfast
  kind: record_content
  reference: data/structures/other/holdfast.yaml
  locator: 'Complete current maintained record: identity, boundaries, components/examples,
    functions, graph, evidence, discussions and history'
  summary: Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    exact target SHA equals the original frozen input. No stale content or record
    edit.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 3875b459c05e557e38d7b4ec9b227a1cc2ddcdbcbb55296f2926deaf9cacc862
- evidence_id: septin-original-holdfast
  kind: record_content
  reference: reviews/structured/20261022T074158Z-holdfast-audit/review.yaml
  locator: Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations
    and source read scopes
  summary: Original 20261022T074158Z-holdfast-audit contains 2 inherited findings;
    exact original hash/render retained. Historical batch26 execution provenance is
    distinguished from the target review cohort and not relabeled as a defect.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: b16e3690ce05de283b917f4beaaf377ec0f7b6666ab3b282801b7815fbb317b2
- evidence_id: septin-native-holdfast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-verify-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Three reviewed CB15 Hfa examples; one COVERED Hfa complex node and one
    UNANCHORED_WITH_UNIPROT external HfsK node A0A0H3CE47 (unreviewed NA1000 reference).
    No missing optional component is inferred; reference identity does not prove experimental
    NA1000 adhesiveness. Exit0. Receipt SHA 358e0da1c2bd67a0387813aaca067e76388fbe12ccee7ba0a04604d6d8a7aaeb;
    log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T12:24:06.362693Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-holdfast-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-causal-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Three reviewed CB15 Hfa examples; one COVERED Hfa complex node and one
    UNANCHORED_WITH_UNIPROT external HfsK node A0A0H3CE47 (unreviewed NA1000 reference).
    No missing optional component is inferred; reference identity does not prove experimental
    NA1000 adhesiveness. Exit0. Receipt SHA 59333e0f6aeb71468c577539893b683019739efadc0875db683da5084f6c8259;
    log SHA 8cc632f432bb3112dab58b3fe1f3ab70db859089a87909be8af240e24661819c.
  accessed_at: '2026-11-04T12:24:06.803898Z'
  support: supports
  snapshot_sha256: 8cc632f432bb3112dab58b3fe1f3ab70db859089a87909be8af240e24661819c
- evidence_id: septin-record-hyphal_tip
  kind: record_content
  reference: data/structures/other/hyphal_tip.yaml
  locator: 'Complete current maintained record: identity, boundaries, components/examples,
    functions, graph, evidence, discussions and history'
  summary: Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    exact target SHA equals the original frozen input. No stale content or record
    edit.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: d33af9efa38fa45e9d44a06739b952ee6c2b009b85d597f51b8e981084c3c7d4
- evidence_id: septin-original-hyphal_tip
  kind: record_content
  reference: reviews/structured/20261022T074200Z-hyphal-tip-audit/review.yaml
  locator: Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations
    and source read scopes
  summary: Original 20261022T074200Z-hyphal-tip-audit contains 2 inherited findings;
    exact original hash/render retained. Historical batch26 execution provenance is
    distinguished from the target review cohort and not relabeled as a defect.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: deddbb7e7a0b47169c07440a8cd69f5d306c99bdb5528f852f067f4eb9b352dc
- evidence_id: septin-native-hyphal_tip-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-verify-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Three unreviewed Neurospora OR74A examples V5IQM7/Q7RVZ1/Q7RWH7; all three
    typed nodes COVERED. Identity coverage does not validate the expanded definition
    or MECHANISTIC graph label. Exit0. Receipt SHA 1375c483e9ca46986d43e482bdfdddb753d544a88caa4814db7a2b245a551572;
    log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T12:24:11.121618Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-hyphal_tip-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-causal-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Three unreviewed Neurospora OR74A examples V5IQM7/Q7RVZ1/Q7RWH7; all three
    typed nodes COVERED. Identity coverage does not validate the expanded definition
    or MECHANISTIC graph label. Exit0. Receipt SHA 0c4af3efaa47abbade941408b0458d6d2c79f7145b6e0e8daadc76f1c63d7c1b;
    log SHA 91cc237750b3f3b8f5dfa2f9942ef9989f97cd12bb602529c105cf1290bc4896.
  accessed_at: '2026-11-04T12:24:11.562192Z'
  support: supports
  snapshot_sha256: 91cc237750b3f3b8f5dfa2f9942ef9989f97cd12bb602529c105cf1290bc4896
- evidence_id: septin-record-hyphal_tip_polarisome
  kind: record_content
  reference: data/structures/other/hyphal_tip_polarisome.yaml
  locator: 'Complete current maintained record: identity, boundaries, components/examples,
    functions, graph, evidence, discussions and history'
  summary: Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    exact target SHA equals the original frozen input. No stale content or record
    edit.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 69417314e33e5f9ef62038f48149ff6a8099a77ca45c1227b8bb6d52ac269667
- evidence_id: septin-original-hyphal_tip_polarisome
  kind: record_content
  reference: reviews/structured/20261022T074201Z-hyphal-tip-polarisome-audit/review.yaml
  locator: Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations
    and source read scopes
  summary: Original 20261022T074201Z-hyphal-tip-polarisome-audit contains 0 inherited
    findings; exact original hash/render retained. Historical batch26 execution provenance
    is distinguished from the target review cohort and not relabeled as a defect.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: b293319350cfdbf9c3edb6cafd0223e7933045f83564ff8e61a976fe7ebd3160
- evidence_id: septin-native-hyphal_tip_polarisome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-verify-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Three unreviewed Neurospora OR74A examples and all three nodes COVERED.
    Distinct mature-tip localizations are source-supported; no direct physical-contact
    or universal assembly claim follows from coverage. Exit0. Receipt SHA 16a97967682d8b16138573d37fa961f37b9258c45ddb9bd9f7110e1c841bfdcf;
    log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T12:24:12.584286Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-hyphal_tip_polarisome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-causal-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Three unreviewed Neurospora OR74A examples and all three nodes COVERED.
    Distinct mature-tip localizations are source-supported; no direct physical-contact
    or universal assembly claim follows from coverage. Exit0. Receipt SHA 1f5d749e79121d8477b4ca0df2e1dc6f07bf2fd36ad4325584ac898a8c9977b8;
    log SHA e888a6c3fd631ea34eb095cd4b5ab67fa6ad7b2e551ab37fe3c578aab82f92a3.
  accessed_at: '2026-11-04T12:24:13.012864Z'
  support: supports
  snapshot_sha256: e888a6c3fd631ea34eb095cd4b5ab67fa6ad7b2e551ab37fe3c578aab82f92a3
- evidence_id: septin-record-ino80_complex
  kind: record_content
  reference: data/structures/other/ino80_complex.yaml
  locator: 'Complete current maintained record: identity, boundaries, components/examples,
    functions, graph, evidence, discussions and history'
  summary: Whole target independently read at source f5668d26c554ec2f62610183aed5c5bc3aa76826;
    exact target SHA equals the original frozen input. No stale content or record
    edit.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 0903c3843e1e1d782fa1437c3ec324bc1c5aae25f19cb4cbe5452a3d36e865c4
- evidence_id: septin-original-ino80_complex
  kind: record_content
  reference: reviews/structured/20261022T074202Z-ino80-complex-audit/review.yaml
  locator: Entire immutable original YAML and derived Markdown, including checks/findings/actions/limitations
    and source read scopes
  summary: Original 20261022T074202Z-ino80-complex-audit contains 1 inherited findings;
    exact original hash/render retained. Historical batch26 execution provenance is
    distinguished from the target review cohort and not relabeled as a defect.
  accessed_at: '2026-11-04T12:36:12.159635Z'
  support: supports
  snapshot_sha256: 90eddd1c07af6b359bede56e055de61f474e0840b1fe19abac5df75072b45035
- evidence_id: septin-native-ino80_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-verify-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Fifteen reviewed S288C reference examples and all fifteen nodes COVERED.
    These are fifteen constituent classes, not a fixed fifteen-protein stoichiometry;
    exact family and activity/necessity scopes are independently assessed. Exit0.
    Receipt SHA d4fae12a56361c3343b94b3a9d50310e6fe73efe45827be6c78e57ddc34f6395;
    log SHA 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289.
  accessed_at: '2026-11-04T12:24:15.770976Z'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: septin-native-ino80_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-causal-receipt.json
  locator: Actual parent-run native command; independently read full stdout, receipt
    and target inventory
  summary: Fifteen reviewed S288C reference examples and all fifteen nodes COVERED.
    These are fifteen constituent classes, not a fixed fifteen-protein stoichiometry;
    exact family and activity/necessity scopes are independently assessed. Exit0.
    Receipt SHA 66464ad8b169db3b2cdc639b76d68667f00d9f5c5049cdc4cfa13b58cc3ae130;
    log SHA aa96cf2f4b6921e477f5ffa6700a09bdedf93e8d1eaf4c39893c3fd5d6242a70.
  accessed_at: '2026-11-04T12:24:16.174552Z'
  support: supports
  snapshot_sha256: aa96cf2f4b6921e477f5ffa6700a09bdedf93e8d1eaf4c39893c3fd5d6242a70
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T12:29:22.815032Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 54c2268bfc00ef5259376161a01d0d3622c0d27527454ad2804e07dfd552fdf2
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T12:24:13.264652Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T12:23:50.794212Z'
  support: supports
  summary: 'Native TraitMech check passed: all 10 links resolve with matching labels
    against the 1130-trait source index.'
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T12:23:48.859808Z'
  support: supports
  summary: All 22 governed artifacts match the pinned CLAW revision.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T12:24:14.954305Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    all 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T12:42:11Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 1b3c4291977376d6e4f68a8690ffe50018f5dd542b065cdf91763056fcaad01f
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T12:25:48.476810Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 0590ce7259636032c009705341045e556eea6ddfae65aae0a20073961850a0c0
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2394 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-hda1_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:01.345039Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hda1_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda1_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:01.756550Z'
  support: context_only
  snapshot_sha256: 0698baa112f4c65d51a87fc7cdc54fa4c097af5e3283457b5e188c37526b371c
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hda_beta_clamp_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:02.881474Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hda_beta_clamp_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hda_beta_clamp_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:03.305603Z'
  support: context_only
  snapshot_sha256: fdb72ccdbcb760c5581b5ce5a9ec2ee7fbba558b130b4cc5bf5b39f01c27460d
  summary: 2 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hir_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:04.536460Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hir_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hir_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:04.987032Z'
  support: context_only
  snapshot_sha256: 96856c000b7ea9ca08297600191ff88679229c41cc7e4bad485dc9450ca1081d
  summary: 4 represented protein examples; 4 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-holdfast-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:06.362693Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-holdfast-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/holdfast-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:06.803898Z'
  support: context_only
  snapshot_sha256: 8cc632f432bb3112dab58b3fe1f3ab70db859089a87909be8af240e24661819c
  summary: 3 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hops_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:08.001048Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hops_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hops_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:08.424569Z'
  support: context_only
  snapshot_sha256: 892cd259b2c321099f6cac2b190f08044881c771012d46f67414f536f65de7dd
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hsp78_chaperone_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:09.561798Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hsp78_chaperone_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hsp78_chaperone_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:09.995717Z'
  support: context_only
  snapshot_sha256: 5867d4085f1c7acff7bbc6c93531493cbeea3c2e94aabd23878aab54d7ebe9d8
  summary: 1 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hyphal_tip-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:11.121618Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hyphal_tip-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:11.562192Z'
  support: context_only
  snapshot_sha256: 91cc237750b3f3b8f5dfa2f9942ef9989f97cd12bb602529c105cf1290bc4896
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hyphal_tip_polarisome-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:12.584286Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-hyphal_tip_polarisome-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/hyphal_tip_polarisome-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:13.012864Z'
  support: context_only
  snapshot_sha256: e888a6c3fd631ea34eb095cd4b5ab67fa6ad7b2e551ab37fe3c578aab82f92a3
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-i_aaa_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:14.148014Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-i_aaa_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/i_aaa_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:14.551577Z'
  support: context_only
  snapshot_sha256: 56d25989f5311df05c2743135e4baac5d6b8a99d427c86d00a8b43432d83517c
  summary: 3 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ino80_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:15.770976Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ino80_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2394/ino80_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T12:24:16.174552Z'
  support: context_only
  snapshot_sha256: aa96cf2f4b6921e477f5ffa6700a09bdedf93e8d1eaf4c39893c3fd5d6242a70
  summary: 15 represented protein examples; 15 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-provenance-0
  area: schema
  topic: Original/current native inputs and artifacts
  outcome: supported
  summary: Current target equals original frozen source and reviewed main. Six original
    native validate/render commands pass; own42 historical input occurrences match
    declared revisions/hashes and six original artifact bytes are unchanged.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-original-audit
- assessment_id: micro-applicability-0
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal no-iModulon-specific-claim rationale excludes a record
    with explicit molecular/function/pathway assertions. Fresh complete catalogue
    has no matched yeast host; no foreign-host proxy is used. Historical runner failure
    is not fresh.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-adapter-catalogue-fresh
  - micro-historical-runner
- assessment_id: micro-native-0
  area: schema
  topic: Actual native protein scope
  outcome: supported
  summary: Three maintained reviewed examples and three covered protein nodes. Both
    actual commands exit0; coverage is not biological confirmation.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-native-hda1_complex-verify
  - micro-native-hda1_complex-causal
  - micro-record-0
- assessment_id: micro-history-0
  area: provenance
  topic: Existing tasks and append-only rationale
  outcome: supported
  summary: The active source-neutral grounding task can be progressed with verified
    class identities; historical rationale need not be rewritten to mimic a present
    inventory. Preserve dates/events and update current notes or narrow prompts. No
    record edits or grouped-issue closure.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
- assessment_id: micro-access-0
  area: evidence
  topic: Original and current access tiers
  outcome: concern
  summary: Original contains 3 access-only rows misclassified primary_source; original
    summaries already admit their limits. Correct successor kinds only, retaining
    old times/hashes. Current metadata/abstract and genuine primary-body reads are
    separately scoped.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-prior-0
  - micro-record-0
  - micro-original-audit
  - micro-historical-0-access-panther-PTHR31882-SF11
  - micro-historical-0-access-carmen1996-doi
  - micro-historical-0-access-carmen1996-jbc
- assessment_id: micro-formation-0
  area: grounding
  topic: Physical necessity versus function and recovery
  outcome: unknown
  summary: Current UNKNOWN formation values remain permitted. Activity loss, viability,
    localization, conditional recovery and universal formation necessity are distinct;
    no automatic ESSENTIAL conversion or new experiment is required.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-schema
  - micro-graph-policy
- assessment_id: micro-physical-0
  area: scope
  topic: Image/quantitative-property coverage
  outcome: not_applicable
  summary: No maintained images or physical-property fields require pixel inspection
    for this target. Text captions read only within explicit source scopes; no pixels,
    raw-gel quantification or structural coordinate analysis claimed.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
- assessment_id: micro-provenance-1
  area: schema
  topic: Original/current native inputs and artifacts
  outcome: supported
  summary: Current target equals original frozen source and reviewed main. Six original
    native validate/render commands pass; own42 historical input occurrences match
    declared revisions/hashes and six original artifact bytes are unchanged.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-delta-1
  - micro-original-audit
- assessment_id: micro-applicability-1
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal no-iModulon-specific-claim rationale excludes a record
    with explicit molecular/function/pathway assertions. Actual E.coli precise1k dataset
    is matched at reference locus level; hda and dnaN each have zero thresholded memberships
    in201 rows, with five-strain/assay-context limits. Historical runner failure is
    not fresh.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-adapter-catalogue-fresh
  - micro-historical-runner
  - micro-adapter-precise1k-meta-fresh
  - micro-adapter-precise1k-genes-fresh
  - micro-adapter-membership-b2496
  - micro-adapter-membership-b3701
- assessment_id: micro-native-1
  area: schema
  topic: Actual native protein scope
  outcome: supported
  summary: Two maintained reviewed examples; only Hda is a typed protein node and
    is COVERED. DnaN ring is a structure. Both actual commands exit0; coverage is
    not biological confirmation.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-native-hda_beta_clamp_complex-verify
  - micro-native-hda_beta_clamp_complex-causal
  - micro-record-1
- assessment_id: micro-history-1
  area: provenance
  topic: Existing tasks and append-only rationale
  outcome: supported
  summary: The active source-neutral grounding task can be progressed with verified
    class identities; historical rationale need not be rewritten to mimic a present
    inventory. Preserve dates/events and update current notes or narrow prompts. No
    record edits or grouped-issue closure.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
- assessment_id: micro-access-1
  area: evidence
  topic: Original and current access tiers
  outcome: supported
  summary: No failed-access kind defect found in this original after full evidence
    inventory inspection. Current metadata/abstract and genuine primary-body reads
    are separately scoped.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-prior-1
  - micro-record-1
  - micro-original-audit
- assessment_id: micro-formation-1
  area: grounding
  topic: Physical necessity versus function and recovery
  outcome: unknown
  summary: Current UNKNOWN formation values remain permitted. Activity loss, viability,
    localization, conditional recovery and universal formation necessity are distinct;
    no automatic ESSENTIAL conversion or new experiment is required.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-schema
  - micro-graph-policy
- assessment_id: micro-physical-1
  area: scope
  topic: Image/quantitative-property coverage
  outcome: not_applicable
  summary: No maintained images or physical-property fields require pixel inspection
    for this target. Text captions read only within explicit source scopes; no pixels,
    raw-gel quantification or structural coordinate analysis claimed.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
- assessment_id: micro-provenance-2
  area: schema
  topic: Original/current native inputs and artifacts
  outcome: supported
  summary: Current target equals original frozen source and reviewed main. Six original
    native validate/render commands pass; own42 historical input occurrences match
    declared revisions/hashes and six original artifact bytes are unchanged.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-delta-2
  - micro-original-audit
- assessment_id: micro-applicability-2
  area: scope
  topic: Whole-record structured-source applicability
  outcome: concern
  summary: Original formal no-iModulon-specific-claim rationale excludes a record
    with explicit molecular/function/pathway assertions. Fresh complete catalogue
    has no matched yeast host; no foreign-host proxy is used. Historical runner failure
    is not fresh.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-adapter-catalogue-fresh
  - micro-historical-runner
- assessment_id: micro-native-2
  area: schema
  topic: Actual native protein scope
  outcome: supported
  summary: Four maintained reviewed examples and four covered protein nodes. Both
    actual commands exit0; coverage is not biological confirmation.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-native-hir_complex-verify
  - micro-native-hir_complex-causal
  - micro-record-2
- assessment_id: micro-history-2
  area: provenance
  topic: Existing tasks and append-only rationale
  outcome: supported
  summary: The active source-neutral grounding task can be progressed with verified
    class identities; historical rationale need not be rewritten to mimic a present
    inventory. Preserve dates/events and update current notes or narrow prompts. No
    record edits or grouped-issue closure.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
- assessment_id: micro-access-2
  area: evidence
  topic: Original and current access tiers
  outcome: concern
  summary: Original contains 2 access-only rows misclassified primary_source; original
    summaries already admit their limits. Correct successor kinds only, retaining
    old times/hashes. Current metadata/abstract and genuine primary-body reads are
    separately scoped.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-prior-2
  - micro-record-2
  - micro-original-audit
  - micro-historical-2-access-panther-PTHR13831-SF0
  - micro-historical-2-access-panther-PTHR13831-SF1
- assessment_id: micro-formation-2
  area: grounding
  topic: Physical necessity versus function and recovery
  outcome: unknown
  summary: Current UNKNOWN formation values remain permitted. Activity loss, viability,
    localization, conditional recovery and universal formation necessity are distinct;
    no automatic ESSENTIAL conversion or new experiment is required.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-schema
  - micro-graph-policy
- assessment_id: micro-physical-2
  area: scope
  topic: Image/quantitative-property coverage
  outcome: not_applicable
  summary: No maintained images or physical-property fields require pixel inspection
    for this target. Text captions read only within explicit source scopes; no pixels,
    raw-gel quantification or structural coordinate analysis claimed.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
- assessment_id: micro-hda1-identity
  area: identity
  topic: Exact HDA1 identity and parent/parthood
  outcome: supported
  summary: Active GO0070823 describes two Hda1 with Hda2/Hda3 and is_a GO0000118;
    chromatin GO0000785 is parthood. Wu hydrodynamic analysis suggests the tetramer
    rather than supplying an atomic-count determination. The record does not conflate
    this class-II assembly with Rpd3/class-I complex.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-go-0070823-fresh
  - micro-go-0000118-fresh
  - micro-go-0000785-fresh
  - micro-ancestors-0070823-fresh
  - micro-PMC31845-legacy
- assessment_id: micro-hda1-families
  area: grounding
  topic: Exact Hda1 and Hda3 family task
  outcome: concern
  summary: 'The explicit deferred task can be narrowed: IPR017321 is the yeast class-II
    Hda1 family and IPR026216 is the specific Hda3 family, with positive native P53973/Q06623
    xrefs. Shared Hda2/3 IPR021006 and broad deacetylase IPR000286 do not uniquely
    denote the respective narrower named class. Hda2 remains unresolved within this
    bounded candidate set, not globally ungroundable.'
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-family-IPR017321-fresh
  - micro-family-IPR026216-fresh
  - micro-family-IPR021006
  - micro-family-IPR000286
  - micro-protein-P53973-fresh
  - micro-protein-Q06623-fresh
  - micro-protein-Q06629-fresh
- assessment_id: micro-hda1-association
  area: evidence
  topic: Assembly and activity observations remain distinct
  outcome: supported
  summary: Wu native co-IP/direct GST tests support Hda1 self-association and Hda2/Hda3
    subassembly. hda2-deletion reduces recovered Hda3 partly with instability; hda3-deletion
    loses Hda2 co-IP despite reported comparable Hda2. Activity assays fall to background
    in deletions. Current constituent roles are compatible; these conditional observations
    do not force new universal necessity findings.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-PMC31845-legacy
  - micro-schema
- assessment_id: micro-hda1-function-graph
  area: graph
  topic: All membership and deacetylase-function edges
  outcome: supported
  summary: Three contributes-to and the histone-deacetylase function edge fit direct
    complex/activity evidence and GO0004407. Wu ENA1 ChIP H3/H2B effects are locus/assay-specific;
    Carmen abstract includes broad core-histone deacetylation. No universal in-vivo
    preference across all genes/histones is asserted by this coarse graph.
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-PMC31845-legacy
  - micro-pmid-8663039-fresh
  - micro-go-0004407-fresh
  - micro-graph-policy
- assessment_id: micro-hda1-reference
  area: scope
  topic: Species/reference identity and historic mass
  outcome: supported
  summary: 'Yeast species example is compatible with Wu YDS/WJY experimental backgrounds.
    S288C examples are separate current reference annotations. Carmen1996 is complete
    abstract only: approximate350kDa HDA and different HDB are historical biochemical
    context, not an independently read body or precise structural mass.'
  target_ids:
  - GO:0070823
  evidence_ids:
  - micro-record-0
  - micro-PMC31845-legacy
  - micro-pmid-8663039-fresh
  - micro-carmen-doi
  - micro-tax-4932-fresh
  - micro-tax-559292-fresh
  - micro-protein-P53973-fresh
  - micro-protein-Q06629-fresh
  - micro-protein-Q06623-fresh
- assessment_id: micro-hda-beta-identity
  area: identity
  topic: Hda-beta state and DnaA boundary
  outcome: supported
  summary: Active GO1990085 exact synonyms and parent1990078 support the Hda/DnaN
    complex. GO0044775 beta ring is a complex constituent/has_part; GO1990083 DnaA-Hda
    is distinct. DnaA is functionally relevant but not automatically a constituent
    of this two-class record.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-go-1990085-fresh
  - micro-ancestors-1990085-fresh
  - micro-go-1990078-fresh
  - micro-go-0044775-fresh
  - micro-go-1990083-fresh
  - micro-PMC415757-legacy
- assessment_id: micro-hda-family
  area: grounding
  topic: Resolvable Hda branch
  outcome: concern
  summary: 'Current Hda label-only class and active explicit task defer a verified
    family: IPR017788 is the Hda branch distinct from initiator DnaA, carried by P69931.
    IPR022864 is the narrower Enterobacteriaceae child; no broader DnaA-like identity
    or species accession substitutes for the whole Hda class.'
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-family-IPR017788-fresh
  - micro-family-IPR022864-fresh
  - micro-protein-P69931-fresh
- assessment_id: micro-hda-beta-binding
  area: evidence
  topic: Direct binding versus RIDA reaction
  outcome: supported
  summary: Kurz directly tests purified Hda-beta binding, motif mutants and peptide
    competition. The source connects binding to proposed RIDA relevance and prior
    DnaA-ATP hydrolysis work; record graph explicitly does not resolve loading or
    ATP-hydrolysis chemistry. Motif-mutant solubility controls do not eliminate misfolding,
    and no whole-RIDA reconstitution is claimed.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-PMC415757-legacy
  - micro-pmid-15150238-fresh
- assessment_id: micro-hda-beta-graph
  area: graph
  topic: Three bounded composition/function edges
  outcome: supported
  summary: Two membership contributions and the broad support of negative initiation
    regulation fit GO1990085/GO0032297 and direct binding plus scoped RIDA interpretation.
    DNA-loaded clamp requirements and DnaA contacts remain outside declared NONMECHANISTIC
    graph; existing DnaN structure typing is valid.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-PMC415757-legacy
  - micro-go-0032297
  - micro-go-1990085-fresh
  - micro-graph-policy
- assessment_id: micro-hda-beta-strains
  area: scope
  topic: Biological and dataset preparations
  outcome: supported
  summary: Kurz uses genes amplified from XL1Blue and BL21(DE3)pLyS/TB1 expression
    contexts. Current P69931/P0A988 are reviewed K-12 references. precise1k contains
    BW25113,DGF-298,GMOS,MG1655,W3110, not exact Kurz assay strains; reference locus
    joins are valid but expression measurements cannot establish binding/formation.
  target_ids:
  - GO:1990085
  evidence_ids:
  - micro-record-1
  - micro-PMC415757-legacy
  - micro-tax-562-fresh
  - micro-tax-83333-fresh
  - micro-protein-P69931-fresh
  - micro-protein-P0A988-fresh
  - micro-adapter-precise1k-meta-fresh
  - micro-adapter-precise1k-genes-fresh
- assessment_id: micro-hir-identity
  area: identity
  topic: Four-class HIR and Asf1 partner boundary
  outcome: supported
  summary: Active GO0000417 and Green tagged purification identify Hir1/Hir2/Hir3/Hpc2.
    Asf1 is an interacting cooperating histone chaperone; different purification salt/conditions
    and promoter/assembly assays do not make it an obligatory fifth HIR constituent.
    HIRA exact synonym does not impose yeast composition on every lineage.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-go-0000417-fresh
  - micro-ancestors-0000417-fresh
  - micro-go-0032991-fresh
  - micro-PMC2819815-legacy
- assessment_id: micro-hir-family
  area: grounding
  topic: Specific Hir3 family and unresolved alternatives
  outcome: concern
  summary: IPR033053 is a verified whole Hir3/CABIN1 homolog family and P47171 carries
    it; fungal/animal breadth is explicit. It resolves the existing Hir3 task without
    forcing named Hir1/Hir2 to the mixed IPR031120 family or Hpc2 to domain IPR014840.
    Remaining classes are unresolved by inspected candidates, not globally nonexistent.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-family-IPR033053-fresh
  - micro-family-IPR031120
  - micro-family-IPR014840
  - micro-protein-P47171-fresh
  - micro-protein-P32479-fresh
  - micro-protein-P32480-fresh
  - micro-protein-Q01448-fresh
- assessment_id: micro-hir-assembly
  area: evidence
  topic: Purification/deletion and nucleosome assembly scope
  outcome: supported
  summary: 'Green distinguishes Asf1 association losses from HIR subunit recovery:
    remaining partners persist in hir1/hir3 deletions, while Hir3 is not recovered
    in hpc2 deletion with association versus instability unresolved. HIR binds DNA
    and supports deposition in vitro, enhanced with Asf1 under tested conditions;
    no global four-subunit formation necessity or absolute Asf1 dependence follows.'
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-PMC2819815-legacy
  - micro-schema
- assessment_id: micro-hir-graph
  area: graph
  topic: Five supported coarse membership/function edges
  outcome: supported
  summary: Four constituent contributions and support for GO0006334 nucleosome assembly
    fit primary purification and assembly assays; replication independence is the
    class context. The NONMECHANISTIC graph does not claim a temporal deposition sequence
    or conflate histone transcription regulation with physical membership.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-PMC2819815-legacy
  - micro-go-0006334-fresh
  - micro-graph-policy
- assessment_id: micro-hir-taxa-and-review
  area: scope
  topic: Yeast scope and secondary review limits
  outcome: supported
  summary: S.cerevisiae is the primary biological context; four S288C examples are
    authority identities, not a claim all Green experiments use that reference strain.
    Main captions name PKY backgrounds; supplementary detailed methods/strain tables
    are unread. Mousson2007 is a secondary review accessed as indexed abstract only,
    not primary mechanism proof.
  target_ids:
  - GO:0000417
  evidence_ids:
  - micro-record-2
  - micro-PMC2819815-legacy
  - micro-pmid-17180700-fresh
  - micro-tax-4932-fresh
  - micro-tax-559292-fresh
- assessment_id: micro-reference-localization
  area: evidence
  topic: Identity-only localization citations
  outcome: supported
  summary: Current reviewed entries and exact indexed article identities reproduce
    declared native citation provenance. Complete abstracts for Huh2003,Kim et al.
    2003 (Dp/Hda),Ozaki2013,Sharp2002,Fillingham2009,Sherwood1993,Qian1998 were read;
    not all abstracts contain each protein-localization experiment. No unread body
    localization assay or localization-to-membership inference is claimed.
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  evidence_ids:
  - micro-protein-P53973-fresh
  - micro-protein-Q06629-fresh
  - micro-protein-Q06623-fresh
  - micro-protein-P69931-fresh
  - micro-protein-P0A988-fresh
  - micro-protein-P32479-fresh
  - micro-protein-P32480-fresh
  - micro-protein-P47171-fresh
  - micro-protein-Q01448-fresh
  - micro-pmid-14562095
  - micro-pmid-12618445
  - micro-pmid-23994470
  - micro-pmid-11782447
  - micro-pmid-19683497
  - micro-pmid-8417331
  - micro-pmid-9671488
- assessment_id: plaque-t4-identity
  area: identity
  topic: HOPS identity, class and membrane location
  outcome: supported
  target_ids:
  - GO:0030897
  summary: GO0030897, membrane-protein-complex parent, vacuolar membrane location
    and fusion function denote distinct entities; six-member HOPS is not the larger
    SNARE-bound assembly.
  evidence_ids:
  - plaque-t4-record
  - plaque-go-0030897
  - plaque-go-0098796
  - plaque-go-0000329
  - plaque-go-0042144
  - plaque-PMC16876-body
- assessment_id: plaque-t4-composition
  area: scope
  topic: Six core constituents and external Ypt7
  outcome: supported
  target_ids:
  - GO:0030897
  summary: Seals primary recovery supports six HOPS members; Ypt7 is a GTP-state-selective
    interacting Rab, not a seventh constituent. No mandatory complete-family finding
    is inferred for every deferred class.
  evidence_ids:
  - plaque-t4-record
  - plaque-PMC16876-body
  - plaque-PMC25710-body
  - plaque-up-P32939
  - plaque-protein-skill
- assessment_id: plaque-t4-grounding
  area: grounding
  topic: Exact verified Vps11/Vps16/Vps41 families
  outcome: concern
  target_ids:
  - GO:0030897
  summary: 'Original F1 remains: native family entries IPR016528/IPR016534/IPR016902
    and matched protein xrefs support these exact source-neutral classes. Active REVIEWED_LABEL_ONLY/no
    exact grounding still requires correction; historical discussion rationale remains
    unchanged.'
  evidence_ids:
  - plaque-t4-record
  - plaque-curation
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR016902
  - plaque-up-P12868
  - plaque-up-Q03308
  - plaque-up-P38959
  - plaque-t4-original
- assessment_id: plaque-t4-identity-protein
  area: nomenclature
  topic: Reference proteins, aliases and strain
  outcome: supported
  target_ids:
  - GO:0030897
  summary: Six reviewed S288C examples and native gene aliases/loci match; PEP5/Vps11,
    PEP3/Vps18 and VAM6/Vps39 differences are legitimate synonyms. Native exact reviewed
    queries each return one matching accession. Reference S288C is distinct from primary
    BJ3505/DKY6281 and SEY strains.
  evidence_ids:
  - plaque-t4-record
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-up-P12868
  - plaque-up-Q03308
  - plaque-up-P27801
  - plaque-up-P20795
  - plaque-up-Q07468
  - plaque-up-P38959
  - plaque-query-VPS11
  - plaque-query-PEP5
  - plaque-query-VPS16
  - plaque-query-VPS18
  - plaque-query-PEP3
  - plaque-query-VPS33
  - plaque-query-VPS39
  - plaque-query-VAM6
  - plaque-query-VPS41
  - plaque-query-VAM2
- assessment_id: plaque-t4-formation
  area: completeness
  topic: Assembly evidence versus function
  outcome: supported
  target_ids:
  - GO:0030897
  summary: Rieder Vps16-dependent Vps33 core recovery is a condition-specific association
    result; six global UNKNOWN values do not become a defect merely because fusion
    is antibody-sensitive or proteins co-purify. No universal formation or viability
    claim is inferred.
  evidence_ids:
  - plaque-t4-record
  - plaque-curation
  - plaque-schema
  - plaque-PMC25710-body
  - plaque-PMC16876-body
- assessment_id: plaque-t4-graph
  area: graph
  topic: Bounded association, priming and fusion edges
  outcome: supported
  target_ids:
  - GO:0030897
  summary: NON_MECHANISTIC association/membership graph and Ypt7/fusion relationships
    match actual yeast assays; GTP association, ATP/Sec18 priming and antibody effects
    remain separate observations.
  evidence_ids:
  - plaque-t4-record
  - plaque-graph-skill
  - plaque-PMC16876-body
  - plaque-up-P32939
  - plaque-native-hops_complex-causal
- assessment_id: plaque-t4-sources
  area: evidence
  topic: Primary evidence and source access
  outcome: supported
  target_ids:
  - GO:0030897
  summary: Seals Methods/Results/Discussion and bounded Rieder sections read in genuine
    HTML; older abstracts independently resolve bibliography. No Rieder whole-body,
    primary figure pixels or newly inspected papers behind UniProt comments claimed.
  evidence_ids:
  - plaque-t4-record
  - plaque-PMC16876-body
  - plaque-PMC25710-body
  - plaque-pmid-10944212
  - plaque-pmid-9362071
- assessment_id: plaque-t4-applicability
  area: scope
  topic: Structured-source assessment omitted originally
  outcome: concern
  target_ids:
  - GO:0030897
  summary: Full original YAML/MD has no formal or prose structured-source applicability
    assessment. Named HOPS/Ypt7 fusion narrative triggers policy. Current complete
    catalogue has no yeast match; downstream molecular-module queries therefore not
    applicable within its actual coverage.
  evidence_ids:
  - plaque-t4-record
  - plaque-t4-original
  - plaque-profile
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t4-native
  area: schema
  topic: Historical and current native gates
  outcome: supported
  target_ids:
  - GO:0030897
  summary: Original validates and renders identically with historical hashes verified.
    Current verify/causal exit0; Ypt7 external-xref classification is appropriate
    and is not a curation defect.
  evidence_ids:
  - plaque-t4-record
  - plaque-original-proof
  - plaque-native-hops_complex-verify
  - plaque-native-hops_complex-causal
- assessment_id: plaque-t4-verdict
  area: provenance
  topic: Exact inherited finding retained
  outcome: concern
  target_ids:
  - GO:0030897
  summary: Retain original F1 minor and action under exact predecessor identity; no
    other original or category finding resolved by inference. Current record unchanged
    and still needs scoped grounding curation.
  evidence_ids:
  - plaque-t4-record
  - plaque-t4-original
  - plaque-original-proof
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR016902
- assessment_id: plaque-t5-identity
  area: identity
  topic: Local Hsp78 oligomer identity
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Local identifier appropriately denotes Hsp78 chaperone assembly; broader
    GO0101031 parent and matrix part_of are distinct. One exact bounded zero-hit GO
    query cannot establish exhaustive ontology absence.
  evidence_ids:
  - plaque-t5-record
  - plaque-go-0101031
  - plaque-go-0005759
  - plaque-go-search-hsp78
  - plaque-PMC9574514-s3
- assessment_id: plaque-t5-identity-protein
  area: nomenclature
  topic: Reviewed Hsp78 example and broad families
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: P33416/HSP78/YDR258C reviewed S288C identity and gene query agree. Complete
    nine-match InterPro inventory supplies broad ClpA/B families/domains, not exact
    Hsp78-only class; generated unchecked IPR050130 description is excluded from biological
    evidence.
  evidence_ids:
  - plaque-t5-record
  - plaque-up-P33416
  - plaque-query-HSP78
  - plaque-tax-559292
  - plaque-ipr-protein-P33416
  - plaque-ipr-IPR001270
  - plaque-ipr-IPR050130
- assessment_id: plaque-t5-oligomers
  area: quantity
  topic: Preparation-dependent oligomer observations
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Native mitochondrial bands interpreted as trimers/hexamers and purified
    SEC conditions do not define one invariant count. WT/trap constructs, ATP/Mg and
    salt contexts remain separate; no six-count generalization imposed.
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC9574514-s3
  - plaque-PMC9574514-gr1
  - plaque-up-P33416
- assessment_id: plaque-t5-function
  area: graph
  topic: ATPase, reporter recovery and heat-growth scope
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Approximately 70% reduced trap ATPase is not null; reporter resolubilization
    is not measured refolding and global ATP depletion is not Hsp78-specific. Glycerol
    growth and proteome association are not respiratory flux or fixed constituent
    identity.
  evidence_ids:
  - plaque-t5-record
  - plaque-go-0140545
  - plaque-go-0016887
  - plaque-PMC9574514-s3
  - plaque-PMC9574514-gr1
  - plaque-PMC9574514-gr2
- assessment_id: plaque-t5-inconsistencies
  area: consistency
  topic: Source conflicts disclosed by record
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Results/figure E614Q versus Methods E612Q, salt NaCl/KCl wording and Fig2D
    versus Methods temperature/centrifugation discrepancies are already explicitly
    disclosed. No external reconciliation invented; they do not create a new record
    defect.
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC9574514-s3
  - plaque-PMC9574514-gr1
  - plaque-PMC9574514-gr2
- assessment_id: plaque-t5-taxa
  area: scope
  topic: Experimental strains and assays
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Y03617-ES/Y13617-ES hsp78 deletion/complementation backgrounds and isolated
    mitochondrial assays are separate from reference S288C and E. coli recombinant
    expression. No bacterial transcriptome proxy.
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC9574514-s3
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t5-image-dataset
  area: provenance
  topic: Actual figure and dataset provenance
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: All Figure1/2 pixels inspected and maintained MD5s match. Main article
    CC BY-NC-ND4.0 and project-metadata CC0 are distinct; link-only image metadata
    preserved. PRIDE PXD030405/030436 identity/DOI/organism confirmed without raw-MS
    reanalysis.
  evidence_ids:
  - plaque-t5-record
  - plaque-PMC9574514-s3
  - plaque-PMC9574514-gr1
  - plaque-PMC9574514-gr2
  - plaque-pride-PXD030405
  - plaque-pride-PXD030436
- assessment_id: plaque-t5-applicability
  area: scope
  topic: Structured-source assessment omitted originally
  outcome: concern
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Full original YAML/MD lacks an applicability row or prose decision despite
    positive HSP78 heat-stress/protein narrative. Current official catalogue has no
    yeast host; no matching dataset means no downstream query warranted, not an expression-only
    exemption.
  evidence_ids:
  - plaque-t5-record
  - plaque-t5-original
  - plaque-profile
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t5-access-kind
  area: provenance
  topic: Historical failed XML classified correctly
  outcome: concern
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: Original evidence[19] micro57-jaworek2022-xml is HTTP406 access-only evidence,
    already context_only but kind authority. Successor must classify validation while
    preserving October22 timestamp/raw SHA and not alleging unread primary biology;
    genuine separately read primary source remains valid.
  evidence_ids:
  - plaque-t5-record
  - plaque-t5-original
  - plaque-historical-jaworek-xml-access
  - plaque-PMC9574514-s3
- assessment_id: plaque-t5-native-verdict
  area: schema
  topic: Qualified pass with native coverage limits
  outcome: supported
  target_ids:
  - cellstructuremech:hsp78_chaperone_complex
  summary: No scientific finding established. One current example/typed node is verified/COVERED;
    all original historical hashes and native render match. UNKNOWN formation and
    broad class boundaries remain honest limits.
  evidence_ids:
  - plaque-t5-record
  - plaque-original-proof
  - plaque-native-hsp78_chaperone_complex-verify
  - plaque-native-hsp78_chaperone_complex-causal
  - plaque-PMC9574514-s3
- assessment_id: plaque-t8-identity
  area: identity
  topic: i-AAA assembly, orientation and function
  outcome: supported
  target_ids:
  - GO:0031942
  summary: GO0031942 and GO0098800 distinguish i-AAA assembly from inner membrane;
    current GO/Wu IMS context is maintained. Older Weber abstract and UniProt topology
    phrasing conflict with that orientation, disclosed as source conflict without
    silently rewriting the well-supported current record.
  evidence_ids:
  - plaque-t8-record
  - plaque-go-0031942
  - plaque-go-0098800
  - plaque-go-0005743
  - plaque-go-0004176
  - plaque-up-P32795
  - plaque-pmid-8688560
  - plaque-PMC5748973-s3
- assessment_id: plaque-t8-composition
  area: grounding
  topic: Three protein classes and zinc cofactor
  outcome: supported
  target_ids:
  - GO:0031942
  summary: Exact Mgr1/Mgr3 families match examples; broad FtsH and Yme1 N-terminal
    domain do not substitute for an exact Yme1 family. CPX1655 preserves three protein
    participants and zinc with null copy numbers; its source-composition layer is
    separate from taxon-agnostic components.
  evidence_ids:
  - plaque-t8-record
  - plaque-curation
  - plaque-ipr-IPR013911
  - plaque-ipr-IPR040201
  - plaque-ipr-IPR005936
  - plaque-ipr-IPR048438
  - plaque-ipr-protein-P32795
  - plaque-cpx-1655
  - plaque-chebi-29105
  - plaque-eco-0005547
- assessment_id: plaque-t8-identity-protein
  area: nomenclature
  topic: Yme1/Mgr1/Mgr3 reference identities
  outcome: supported
  target_ids:
  - GO:0031942
  summary: All three current protein examples reviewed S288C with correct primary
    genes/loci and YME1 OSD1/YTA11, MGR3 FMP24 aliases; exact queries uniquely match.
    CPX species-style label does not change taxon559292.
  evidence_ids:
  - plaque-t8-record
  - plaque-up-P32795
  - plaque-up-P25573
  - plaque-up-Q04472
  - plaque-query-YME1
  - plaque-query-OSD1
  - plaque-query-YTA11
  - plaque-query-MGR1
  - plaque-query-MGR3
  - plaque-query-FMP24
  - plaque-tax-559292
  - plaque-cpx-1655
- assessment_id: plaque-t8-mechanism
  area: graph
  topic: Bounded adaptor recruitment and turnover
  outcome: supported
  target_ids:
  - GO:0031942
  summary: Wu supports Mgr1 bridging Yme1-Mgr3, Mgr3 stabilization of Mgr1, cooperative
    substrate recruitment and tested turnover. Tagged substrate effects, endogenous
    temperature regimes and adaptor-independent observed Yme1 size stay separate;
    crosslink contact is not atomically proven handoff.
  evidence_ids:
  - plaque-t8-record
  - plaque-PMC5748973-s3
  - plaque-PMC5748973-JCB_201702125_Fig3
  - plaque-pmid-29138251
- assessment_id: plaque-t8-new-edges
  area: evidence
  topic: New architecture edges lack cited support
  outcome: concern
  target_ids:
  - GO:0031942
  summary: 'Stale refresh exposes a new grouped major source defect: two appended
    edges assert six Yme1 copies/six zinc cofactors from CPX1655, whose native stochiometry
    fields are all null, and introduce a purported Wu quotation absent from the complete
    genuine article. Valid Yme1-core/zinc roles remain supported; an isolated-core
    hexamer may have a different supporting primary source.'
  evidence_ids:
  - plaque-t8-record
  - plaque-stale-diff
  - plaque-cpx-1655
  - plaque-PMC5748973-s3
  - plaque-iaaa-attribution-proof
  - plaque-iaaa-peer-challenge
  - plaque-curation
- assessment_id: plaque-t8-formation
  area: completeness
  topic: Association and activity do not force necessity labels
  outcome: supported
  target_ids:
  - GO:0031942
  summary: Mgr1-mediated association, Mgr3-dependent stability and substrate turnover
    support bounded mechanism; no universal assembly-essentiality or new assay mandate
    follows from UNKNOWN values or CPX curator inference.
  evidence_ids:
  - plaque-t8-record
  - plaque-PMC5748973-s3
  - plaque-cpx-1655
  - plaque-eco-0005547
  - plaque-schema
- assessment_id: plaque-t8-taxa-image
  area: provenance
  topic: Actual strain, figure, license and bibliography
  outcome: supported
  target_ids:
  - GO:0031942
  summary: TableS1 specified ranges distinguish BY4741/CEN.PK/W303 constructs from
    S288C reference proteins. Figure3 pixels/MD5 and main caption/license agree; post-six-month
    CC BY-NC-SA4.0 link-only metadata is preserved. Other five PMID records read at
    full-abstract/database tier only.
  evidence_ids:
  - plaque-t8-record
  - plaque-PMC5748973-JCB_201702125_TableS1
  - plaque-PMC5748973-JCB_201702125_Fig3
  - plaque-PMC5748973-s3
  - plaque-pmid-14562095
  - plaque-pmid-14576278
  - plaque-pmid-16267274
  - plaque-pmid-8355690
  - plaque-pmid-8688560
- assessment_id: plaque-t8-applicability
  area: scope
  topic: Replace expression-only exclusion with actual scope
  outcome: concern
  target_ids:
  - GO:0031942
  summary: Original checks[4] imodulondb says no expression-module inference is used,
    insufficient for its positive molecular/proteolysis narrative. Current complete
    catalogue lacks yeast coverage; downstream queries are not applicable within that
    actual catalogue after explicit assessment.
  evidence_ids:
  - plaque-t8-record
  - plaque-t8-original
  - plaque-profile
  - plaque-catalogue
  - plaque-historical-runner
- assessment_id: plaque-t8-native
  area: schema
  topic: Current three-node native coverage
  outcome: supported
  target_ids:
  - GO:0031942
  summary: Current verify/causal commands exit0 for three reviewed examples and three
    COVERED typed nodes, versus two old typed nodes. Native success does not validate
    the new quoted-source/count claims; zinc is chemical. Original validates/renders
    and historical hashes still match.
  evidence_ids:
  - plaque-t8-record
  - plaque-original-proof
  - plaque-native-i_aaa_complex-verify
  - plaque-native-i_aaa_complex-causal
  - plaque-stale-diff
- assessment_id: plaque-t8-verdict
  area: provenance
  topic: Substantive stale refresh changes disposition
  outcome: concern
  target_ids:
  - GO:0031942
  summary: Original qualified pass is a valid historical observation of bytes without
    the new edges. Current record needs curation for the newly added source-support
    defect; no invented original predecessor and no historical record-fix credit assigned
    to this review.
  evidence_ids:
  - plaque-t8-record
  - plaque-t8-original
  - plaque-stale-diff
  - plaque-iaaa-attribution-proof
  - plaque-cpx-1655
  - plaque-PMC5748973-s3
- assessment_id: septin-holdfast-schema-inputs
  area: schema
  topic: Native original schema/render and frozen inputs
  outcome: supported
  summary: Original validation and exact rendering pass; all original historical inputs
    were compared to exact Git objects. Current record hash is unchanged. These checks
    establish provenance/schema, not scientific truth.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-original-holdfast
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-holdfast-native-coverage
  area: consistency
  topic: Actual protein inventory and typed coverage
  outcome: supported
  summary: Three reviewed CB15 Hfa examples; one COVERED Hfa complex node and one
    UNANCHORED_WITH_UNIPROT external HfsK node A0A0H3CE47 (unreviewed NA1000 reference).
    No missing optional component is inferred; reference identity does not prove experimental
    NA1000 adhesiveness.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-native-holdfast-verify
  - septin-native-holdfast-causal
  - septin-protein-policy
- assessment_id: septin-holdfast-history
  area: provenance
  topic: Dated history and discussion boundaries
  outcome: supported
  summary: Historical reasoning remains provenance. Proposed changes address current
    fields or append dated clarification; no historical rationale is rewritten, no
    unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity
    alone are not findings.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-original-holdfast
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-holdfast-figures
  area: scope
  topic: Images and exact visual-read limits
  outcome: supported
  summary: No maintained image exists in this target. Genuine textual sections/captions
    and, for Ino80, extracted supplementary tables are distinguished from pixel, video,
    coordinate and raw-data analysis; none of those unperformed analyses is claimed.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-literature-policy
- assessment_id: septin-holdfast-structured-sources
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Named Hfa/HfsK/c-di-GMP/holdfast biosynthesis claims require actual coverage
    assessment. Complete fresh official catalogue lacks the exact biological hosts,
    so no host-matched downstream module query applies. Primary/authority fallback
    is explicit; E. coli cloning/expression context is not a proxy and noncoverage
    is not biological absence.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-original-holdfast
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-hyphal_tip-schema-inputs
  area: schema
  topic: Native original schema/render and frozen inputs
  outcome: supported
  summary: Original validation and exact rendering pass; all original historical inputs
    were compared to exact Git objects. Current record hash is unchanged. These checks
    establish provenance/schema, not scientific truth.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-original-hyphal_tip
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-hyphal_tip-native-coverage
  area: consistency
  topic: Actual protein inventory and typed coverage
  outcome: supported
  summary: Three unreviewed Neurospora OR74A examples V5IQM7/Q7RVZ1/Q7RWH7; all three
    typed nodes COVERED. Identity coverage does not validate the expanded definition
    or MECHANISTIC graph label.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-native-hyphal_tip-verify
  - septin-native-hyphal_tip-causal
  - septin-protein-policy
- assessment_id: septin-hyphal_tip-history
  area: provenance
  topic: Dated history and discussion boundaries
  outcome: supported
  summary: Historical reasoning remains provenance. Proposed changes address current
    fields or append dated clarification; no historical rationale is rewritten, no
    unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity
    alone are not findings.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-original-hyphal_tip
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-hyphal_tip-figures
  area: scope
  topic: Images and exact visual-read limits
  outcome: supported
  summary: No maintained image exists in this target. Genuine textual sections/captions
    and, for Ino80, extracted supplementary tables are distinguished from pixel, video,
    coordinate and raw-data analysis; none of those unperformed analyses is claimed.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-literature-policy
- assessment_id: septin-hyphal_tip-structured-sources
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Named SPA2/BUD6/BNI1 polarity, cytoskeleton and secretion claims require
    actual coverage assessment. Complete fresh official catalogue lacks the exact
    biological hosts, so no host-matched downstream module query applies. Primary/authority
    fallback is explicit; E. coli cloning/expression context is not a proxy and noncoverage
    is not biological absence.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-original-hyphal_tip
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-hyphal_tip_polarisome-schema-inputs
  area: schema
  topic: Native original schema/render and frozen inputs
  outcome: supported
  summary: Original validation and exact rendering pass; all original historical inputs
    were compared to exact Git objects. Current record hash is unchanged. These checks
    establish provenance/schema, not scientific truth.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-original-hyphal_tip_polarisome
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-hyphal_tip_polarisome-native-coverage
  area: consistency
  topic: Actual protein inventory and typed coverage
  outcome: supported
  summary: Three unreviewed Neurospora OR74A examples and all three nodes COVERED.
    Distinct mature-tip localizations are source-supported; no direct physical-contact
    or universal assembly claim follows from coverage.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-native-hyphal_tip_polarisome-verify
  - septin-native-hyphal_tip_polarisome-causal
  - septin-protein-policy
- assessment_id: septin-hyphal_tip_polarisome-history
  area: provenance
  topic: Dated history and discussion boundaries
  outcome: supported
  summary: Historical reasoning remains provenance. Proposed changes address current
    fields or append dated clarification; no historical rationale is rewritten, no
    unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity
    alone are not findings.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-original-hyphal_tip_polarisome
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-hyphal_tip_polarisome-figures
  area: scope
  topic: Images and exact visual-read limits
  outcome: supported
  summary: No maintained image exists in this target. Genuine textual sections/captions
    and, for Ino80, extracted supplementary tables are distinguished from pixel, video,
    coordinate and raw-data analysis; none of those unperformed analyses is claimed.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-literature-policy
- assessment_id: septin-hyphal_tip_polarisome-structured-sources
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Named SPA2/BUD6/BNI1 polarity, cytoskeleton and secretion claims require
    actual coverage assessment. Complete fresh official catalogue lacks the exact
    biological hosts, so no host-matched downstream module query applies. Primary/authority
    fallback is explicit; E. coli cloning/expression context is not a proxy and noncoverage
    is not biological absence.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-original-hyphal_tip_polarisome
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-ino80_complex-schema-inputs
  area: schema
  topic: Native original schema/render and frozen inputs
  outcome: supported
  summary: Original validation and exact rendering pass; all original historical inputs
    were compared to exact Git objects. Current record hash is unchanged. These checks
    establish provenance/schema, not scientific truth.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-original-ino80_complex
  - septin-original-native-checks
  - septin-review-schema
- assessment_id: septin-ino80_complex-native-coverage
  area: consistency
  topic: Actual protein inventory and typed coverage
  outcome: supported
  summary: Fifteen reviewed S288C reference examples and all fifteen nodes COVERED.
    These are fifteen constituent classes, not a fixed fifteen-protein stoichiometry;
    exact family and activity/necessity scopes are independently assessed.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-native-ino80_complex-verify
  - septin-native-ino80_complex-causal
  - septin-protein-policy
- assessment_id: septin-ino80_complex-history
  area: provenance
  topic: Dated history and discussion boundaries
  outcome: supported
  summary: Historical reasoning remains provenance. Proposed changes address current
    fields or append dated clarification; no historical rationale is rewritten, no
    unrelated record/group issue is disposed, and optional examples or UNKNOWN necessity
    alone are not findings.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-original-ino80_complex
  - septin-curation-policy
  - septin-schema-policy
- assessment_id: septin-ino80_complex-figures
  area: scope
  topic: Images and exact visual-read limits
  outcome: supported
  summary: No maintained image exists in this target. Genuine textual sections/captions
    and, for Ino80, extracted supplementary tables are distinguished from pixel, video,
    coordinate and raw-data analysis; none of those unperformed analyses is claimed.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-literature-policy
  - septin-watanabe-supplement
- assessment_id: septin-ino80_complex-structured-sources
  area: evidence
  topic: Whole-record structured-source applicability
  outcome: supported
  summary: Named Ino80 ATP-dependent chromatin remodeling claims require actual coverage
    assessment. Complete fresh official catalogue lacks the exact biological hosts,
    so no host-matched downstream module query applies. Primary/authority fallback
    is explicit; E. coli cloning/expression context is not a proxy and noncoverage
    is not biological absence.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-original-ino80_complex
  - septin-review-policy
  - septin-adapter-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-holdfast-identity
  area: identity
  topic: Local holdfast identity and extracellular boundary
  outcome: supported
  summary: The polar extracellular polysaccharide adhesin is a structure, distinct
    from the associated Hfa anchor machinery and upstream biosynthesis. GO0031012
    is a broader matrix parent; bounded native holdfast search does not justify adopting
    a guessed exact GO identifier.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-go
  - septin-go-search-holdfast
  - septin-sulkowski-xml
  - septin-hershey-metadata-abstract
- assessment_id: septin-holdfast-material
  area: grounding
  topic: Polymer composition and grouped anchor boundary
  outcome: supported
  summary: Hershey primary abstract explicitly reports glucose, 3-O-methylglucose,
    mannose, GlcNAc and xylose in extracts. It supports the stated composition without
    asserting a unique whole-polymer chemical accession. HfaABD is an associated multiprotein
    anchor, not the holdfast matrix itself; no arbitrary single-protein family or
    lipid identifier is forced.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-hershey-metadata-abstract
  - septin-sulkowski-xml
  - septin-schema-policy
- assessment_id: septin-holdfast-reference-proteins
  area: identity
  topic: Hfa and HfsK reference identities
  outcome: supported
  summary: P27342/hfaA, P27343/hfaB and Q45977/hfaD are reviewed CB15 references.
    HfaB native recommended name remains putative transcription activator, while independent
    primary evidence supplies its anchoring role. External HfsK A0A0H3CE47 is an unreviewed
    NA1000 reference; identity does not establish NA1000 as the adhesive experimental
    strain.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-up-P27342
  - septin-up-P27343
  - septin-up-Q45977
  - septin-up-A0A0H3CE47
  - septin-query-hfaA-190650
  - septin-query-hfaB-190650
  - septin-query-hfaD-190650
  - septin-tax-190650
  - septin-tax-565050
- assessment_id: septin-holdfast-canonical-strain
  area: scope
  topic: Canonical experimental model versus reference genome
  outcome: concern
  summary: The current canonical NA1000 note attributes anchoring/composition/c-di-GMP
    work to Sulkowski. Sulkowski specifies CB15 and derivatives, and Sprecher uses
    NA1000 as a nonadherent comparison. F1 retains the precise strain/source correction
    without invalidating the reference HfsK accession or asserting every engineered
    NA1000 derivative is nonadherent.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-sulkowski-xml
  - septin-sprecher-xml
  - septin-tax-190650
  - septin-tax-565050
  - septin-up-A0A0H3CE47
- assessment_id: septin-holdfast-distribution
  area: scope
  topic: Species presence and developmental state
  outcome: supported
  summary: C. vibrioides/crescentus synonymy and CB15/NA1000 identities are explicit.
    Species-level developmental presence is distinguished from condition, cell-cycle
    state and strain-specific loss/nonadherence. These studies are not an exhaustive
    species prevalence census; the actionable canonical-strain mismatch is separately
    recorded.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-tax-155892
  - septin-tax-190650
  - septin-tax-565050
  - septin-sprecher-xml
  - septin-sulkowski-xml
- assessment_id: septin-holdfast-formation
  area: completeness
  topic: Matrix formation versus anchoring and cohesion
  outcome: supported
  summary: Hfa mutants can synthesize and shed holdfast, supporting DISPENSABLE for
    formation of matrix while anchoring/adhesion fails. HfsK deletion alters cohesion
    and shear resistance; direct chemical substrate/acylation mechanism remains unresolved.
    These measured endpoints are not collapsed into one universal necessity.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-sulkowski-xml
  - septin-sprecher-xml
  - septin-schema-policy
- assessment_id: septin-holdfast-graph
  area: graph
  topic: Coarse cohesion, anchoring and adhesion mechanism
  outcome: supported
  summary: The graph correctly keeps external HfsK separate from polysaccharide and
    Hfa machinery. HfsK tunes cohesion; Hfa retains matrix at pole/stalk; matrix adheres
    cells to surfaces. It does not assert the removed under-evidenced synthesis/export
    edge, direct acetylation chemistry or a universal assembly ordering.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-sulkowski-xml
  - septin-sprecher-xml
  - septin-hershey-metadata-abstract
  - septin-graph-policy
- assessment_id: septin-holdfast-bibliography
  area: provenance
  topic: Sulkowski title and real source access
  outcome: concern
  summary: The current bibliography substitutes Old Cell Pole for the published title
    phrase Outer Membrane. F2 is a local title correction. Sulkowski/Sprecher genuine
    bodies are distinguished from Hershey complete abstract; no failed Hershey route
    is promoted to a body read.
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-sulkowski-metadata
  - septin-sulkowski-xml
  - septin-hershey-metadata-abstract
  - septin-hershey-xml
  - septin-hershey-html
- assessment_id: septin-hyphal_tip-identity
  area: identity
  topic: Fungal tip and region/complex distinction
  outcome: supported
  summary: GO0001411 identifies the fungal hyphal tip; GO0030427 site of polarized
    growth and GO0051286 cell tip are correct parents. Spitzenkorper/polarisome are
    parts of the region, not synonyms for the whole tip or an arbitrary protein class.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-go
  - septin-go-0001411-ancestors
  - septin-lichius-xml
- assessment_id: septin-hyphal_tip-definition
  area: scope
  topic: Expanded definition and cross-lineage source attribution
  outcome: concern
  summary: The maintained definition adds oomycetes and generalized apparatus mechanisms
    while citing only GO0001411. Exact GO wording is fungal, and Lichius directly
    studies Neurospora with prior fungal comparisons; it does not establish the added
    oomycete defining scope. F1 requests relevant evidence/qualification, not an assertion
    that oomycetes lack tips.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-go
  - septin-lichius-xml
  - septin-lichius-metadata-abstract
- assessment_id: septin-hyphal_tip-reference-proteins
  area: identity
  topic: Three native reference proteins and source strains
  outcome: supported
  summary: V5IQM7/spa2/NCU03115, Q7RVZ1/bud6/NCU08468 and Q7RWH7/bni1/NCU01431 are
    unreviewed OR74A examples. Native taxonomy includes N150/FGSC9013 equivalent names,
    while Lichius specifies additional transformed/deletion backgrounds; accession
    identity is not a substitute for each experiment.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-up-V5IQM7
  - septin-up-Q7RVZ1
  - septin-up-Q7RWH7
  - septin-query-spa2-367110
  - septin-query-bud6-367110
  - septin-query-bni1-367110
  - septin-tax-367110
  - septin-lichius-xml
- assessment_id: septin-hyphal_tip-family-boundaries
  area: grounding
  topic: Broader family candidates and optional grounding
  outcome: supported
  summary: Spa2/Sph1 includes paralogues, and the inspected SRCIN1/actin-regulator
    families do not by themselves resolve the exact local classes. Unchecked machine-generated
    descriptive prose is excluded. Existing label-only rows are not automatically
    defective because a broader family or optional example exists.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-ipr-IPR039892
  - septin-ipr-IPR051825
  - septin-ipr-IPR051661
  - septin-curation-policy
- assessment_id: septin-hyphal_tip-taxon-localization
  area: scope
  topic: Neurospora mature-tip observations
  outcome: supported
  summary: Lichius supports the Neurospora model and distinct mature apical-dome localizations,
    including subapical BUD6 outside Spk and SPA2/BNI1 partial Spk/apical localization.
    COMMON is qualitative model-level context, not a measured prevalence fraction
    or an assertion that every developmental stage has identical geometry.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-lichius-xml
  - septin-tax-5141
  - septin-tax-367110
- assessment_id: septin-hyphal_tip-formation
  area: completeness
  topic: Architecture defects versus universal tip formation
  outcome: unknown
  summary: Deletion analyses alter Spk integrity, growth and morphology, but polarized
    extension can persist without a detectable Spk. CONDITIONAL retains this architecture/growth
    evidence without certifying that the whole tip or every partial polarisome cannot
    form. No forced all-or-none essentiality or new experiment is requested.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-lichius-xml
  - septin-schema-policy
- assessment_id: septin-hyphal_tip-graph
  area: graph
  topic: Spatial parthood/function graph mislabeled mechanistic
  outcome: concern
  summary: Five part_of edges plus whole-structure function describe topology and
    function. The MECHANISTIC label and assembly/functional-mechanism title overstate
    what is encoded. F2 can be addressed by accurately labeling this map NONMECHANISTIC
    and narrowing its title; no additional molecular steps are mandatory.
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-graph-policy
  - septin-lichius-xml
  - septin-schema-policy
- assessment_id: septin-hyphal_tip_polarisome-identity
  area: identity
  topic: Localized complex boundary and exact ontology
  outcome: supported
  summary: GO0031562 identifies the protein complex at the tip of a growing fungal
    hypha, with GO0000133 polarisome parent and GO0001411 parthood. It is distinct
    from the whole apical region and from the Spitzenkorper alone.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-go
  - septin-go-0031562-ancestors
  - septin-lichius-xml
- assessment_id: septin-hyphal_tip_polarisome-reference-proteins
  area: identity
  topic: Three native proteins and independent localization
  outcome: supported
  summary: All three unreviewed OR74A accessions, primary genes and loci match the
    maintained examples. Native authority supports identity; Lichius supports the
    relevant localizations. Reference equivalence to N150/FGSC9013 does not erase
    the reported mutant/transformant backgrounds.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-up-V5IQM7
  - septin-up-Q7RVZ1
  - septin-up-Q7RWH7
  - septin-query-spa2-367110
  - septin-query-bud6-367110
  - septin-query-bni1-367110
  - septin-tax-367110
  - septin-lichius-xml
- assessment_id: septin-hyphal_tip_polarisome-families
  area: grounding
  topic: Label-only exact classes and broader candidates
  outcome: supported
  summary: Inspected Spa2/Sph1 and broader SRCIN1/actin-regulator classifications
    do not independently justify forcing exact retained local classes onto broad family
    or domain IDs. Machine-generated descriptive prose is excluded; open grounding
    discussion remains explicitly bounded rather than silently resolved.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-ipr-IPR039892
  - septin-ipr-IPR051825
  - septin-ipr-IPR051661
  - septin-curation-policy
- assessment_id: septin-hyphal_tip_polarisome-localization
  area: scope
  topic: Mature hyphal-tip architecture and other developmental contexts
  outcome: supported
  summary: SPA2 partially overlaps Spk/apical dome; BUD6 forms an excluded subapical
    cloud; BNI1 occupies Spk core plus apical cap. Source also reports germling, cell-fusion,
    septal-plug and cytokinetic contexts, which are kept outside this first mature-tip
    assembly boundary rather than denied biologically.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-lichius-xml
  - septin-tax-5141
- assessment_id: septin-hyphal_tip_polarisome-formation
  area: completeness
  topic: Conditional architecture and unresolved formation necessity
  outcome: unknown
  summary: Deletion phenotypes show conditional architecture/growth contributions,
    not universal abolition of every encompassing tip or residual complex. UNKNOWN
    formation-specific scope is retained and CONDITIONAL is not treated as universal
    catalytic/growth essentiality.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-lichius-xml
  - septin-schema-policy
- assessment_id: septin-hyphal_tip_polarisome-graph
  area: graph
  topic: Accurately labeled nonmechanistic architecture
  outcome: supported
  summary: NONMECHANISTIC FUNCTION scope is appropriate for the mature-tip constituent
    distributions and polarity function. It neither asserts direct physical interactions
    from colocalization nor imports septal-plug/cytokinetic assemblies into this record.
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-lichius-xml
  - septin-graph-policy
- assessment_id: septin-ino80_complex-identity
  area: identity
  topic: Exact complex, ancestry and fifteen constituent classes
  outcome: supported
  summary: GO0031011, parent GO0097346 and nuclear-chromosome parthood are current
    and exact. Actual Supplementary Table2 supports all fifteen named INO80 classes.
    This list is not a fixed fifteen-molecule stoichiometry; Rvb multiplicity and
    shared components remain distinct.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-go
  - septin-go-0031011-ancestors
  - septin-watanabe-body
  - septin-watanabe-supplement
- assessment_id: septin-ino80_complex-native-identities
  area: identity
  topic: Reviewed yeast reference genes and status
  outcome: supported
  summary: All fifteen examples are reviewed S288C references with matching native
    names/aliases and current one-result bounded queries. Native status/identity does
    not assign every cited culture to S288C. Watanabe TAP preparations and recombinant
    E. coli histone expression are separate biological/sample contexts.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-tax-4932
  - septin-tax-559292
  - septin-watanabe-body
  - septin-up-P53115
  - septin-up-Q03940
  - septin-up-Q12464
  - septin-up-P40060
  - septin-up-Q12345
  - septin-up-Q03435
  - septin-up-P32617
  - septin-up-P43579
  - septin-up-Q12386
  - septin-up-P80428
  - septin-up-P60010
  - septin-up-P35189
  - septin-up-P40154
  - septin-up-Q08561
  - septin-up-P53946
- assessment_id: septin-ino80_complex-exact-families
  area: grounding
  topic: Five verified Ies families and broader retained boundaries
  outcome: concern
  summary: Ies1/IPR038014, Ies2/IPR029523, Ies4/IPR062650, Ies5/IPR020366 and Ies6/IPR029525
    are full-family entries with independent native reference-protein membership.
    The current five deferrals remain actionable F1. Shared INO80/SWR1, Rvb1/2, actin/Arp,
    Sas5/TAF14 and HMGB candidates are not forced onto narrower classes; no exhaustive
    absence claim for Ies3.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-ipr-IPR038014
  - septin-ipr-IPR029523
  - septin-ipr-IPR062650
  - septin-ipr-IPR020366
  - septin-ipr-IPR029525
  - septin-up-P43579
  - septin-up-P40154
  - septin-up-Q08561
  - septin-up-P40060
  - septin-up-P32617
  - septin-ipr-IPR050520
  - septin-retry-IPR027238
  - septin-retry-IPR004000
  - septin-retry-IPR016665
  - septin-retry-IPR050342
- assessment_id: septin-ino80_complex-membership
  area: evidence
  topic: Three TAP preparations and physical module associations
  outcome: supported
  summary: Supplementary Table2 reports spectral counts and coverage for all fifteen
    INO80 classes in three independent preparations. Arp8 deletion removes the Arp8/Arp4/Act1
    module; Ies6 deletion removes Arp5 from residual complex. These measured associations
    are bounded positive context, not evidence that the entire complex ceases to form.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-watanabe-body
  - septin-watanabe-supplement
  - septin-pmid-12887900-abstract
  - septin-pmid-15525518-abstract
- assessment_id: septin-ino80_complex-formation
  area: completeness
  topic: Activity, residual complexes and necessity
  outcome: unknown
  summary: Watanabe distinguishes reduced Arp8-module remodeling from inactive Ies6/Arp5
    module-loss preparations, while residual complexes are purified. Functional loss
    and physical module dependence do not establish universal all-or-none formation
    requirements for every constituent. UNKNOWN remains valid and does not deny measured
    module dependencies.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-watanabe-body
  - septin-watanabe-supplement
  - septin-schema-policy
- assessment_id: septin-ino80_complex-graph
  area: graph
  topic: Explicit nonmechanistic inventory and remodeling activity
  outcome: supported
  summary: The graph declares NONMECHANISTIC FUNCTION scope for fifteen members and
    chromatin remodeling. It does not require invented ordered assembly steps. Earlier
    Shen helicase claim and later Watanabe inability to detect helicase, and Tosi
    versus Watanabe Rvb ring interpretations, remain source-specific; the record does
    not assert either contested mechanism/count.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-graph-policy
  - septin-watanabe-body
  - septin-pmid-10952318-abstract
  - septin-pmid-24034245-abstract
- assessment_id: septin-ino80_complex-sources
  area: evidence
  topic: Primary bodies, abstract-only papers and secondary context
  outcome: supported
  summary: Watanabe genuine body and supplementary tables provide current direct composition/module
    evidence. Shen2000/2003, Jonsson2004, Tosi2013 and ancillary localization/Rvb
    studies were read at complete native abstract scope only. Clapier/Cairns2009 is
    secondary abstract context, not primary mechanism evidence. No unseen images,
    coordinates, raw spectra or full bodies are certified.
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-watanabe-body
  - septin-watanabe-supplement
  - septin-pmid-19355820-abstract
  - septin-pmid-10787406-abstract
  - septin-pmid-11604509-abstract
  - septin-pmid-14562095-abstract
  - septin-pmid-8573785-abstract
  - septin-literature-policy
- assessment_id: septin-holdfast-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: 'Needs curation: 2 inherited findings independently retained, no invented
    new predecessor or optional-field defect. Scientific curation remains outside
    this review PR; the applicability bundle defect is corrected by current review
    evidence. Source access, reference strains, formation and visual-read limits remain
    explicit.'
  target_ids:
  - cellstructuremech:holdfast
  evidence_ids:
  - septin-record-holdfast
  - septin-original-holdfast
  - septin-review-policy
  - septin-curation-policy
  - septin-sulkowski-xml
  - septin-sprecher-xml
  - septin-tax-190650
  - septin-tax-565050
  - septin-up-A0A0H3CE47
  - septin-sulkowski-metadata
- assessment_id: septin-hyphal_tip-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: 'Needs curation: 2 inherited findings independently retained, no invented
    new predecessor or optional-field defect. Scientific curation remains outside
    this review PR; the applicability bundle defect is corrected by current review
    evidence. Source access, reference strains, formation and visual-read limits remain
    explicit.'
  target_ids:
  - GO:0001411
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-original-hyphal_tip
  - septin-review-policy
  - septin-curation-policy
  - septin-go
  - septin-lichius-xml
  - septin-lichius-metadata-abstract
  - septin-graph-policy
  - septin-schema-policy
- assessment_id: septin-hyphal_tip_polarisome-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: supported
  summary: 'Pass with limitations: 0 inherited findings independently retained, no
    invented new predecessor or optional-field defect. Scientific curation remains
    outside this review PR; the applicability bundle defect is corrected by current
    review evidence. Source access, reference strains, formation and visual-read limits
    remain explicit.'
  target_ids:
  - GO:0031562
  evidence_ids:
  - septin-record-hyphal_tip_polarisome
  - septin-original-hyphal_tip_polarisome
  - septin-review-policy
- assessment_id: septin-ino80_complex-verdict
  area: consistency
  topic: Independent current scientific disposition
  outcome: concern
  summary: 'Needs curation: 1 inherited findings independently retained, no invented
    new predecessor or optional-field defect. Scientific curation remains outside
    this review PR; the applicability bundle defect is corrected by current review
    evidence. Source access, reference strains, formation and visual-read limits remain
    explicit.'
  target_ids:
  - GO:0031011
  evidence_ids:
  - septin-record-ino80_complex
  - septin-original-ino80_complex
  - septin-review-policy
  - septin-curation-policy
  - septin-ipr-IPR038014
  - septin-ipr-IPR029523
  - septin-ipr-IPR062650
  - septin-ipr-IPR020366
  - septin-ipr-IPR029525
  - septin-up-P43579
  - septin-up-P40154
  - septin-up-Q08561
  - septin-up-P40060
  - septin-up-P32617
  - septin-watanabe-supplement
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0070823
  - GO:1990085
  - GO:0000417
  - cellstructuremech:holdfast
  - GO:0030897
  - cellstructuremech:hsp78_chaperone_complex
  - GO:0001411
  - GO:0031562
  - GO:0031942
  - GO:0031011
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
  issue_key: hda1-resolve-hda1-hda3-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve Hda1 and Hda3 family mappings
  description: The open task and label-only rows still defer all three families. Native
    IPR017321 and IPR026216 now resolve the Hda1 and Hda3 classes, while the inspected
    Hda2 candidate remains broader.
  target_ids:
  - GO:0070823
  field_paths:
  - components[0].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-family-IPR017321-fresh
  - micro-family-IPR026216-fresh
  - micro-family-IPR021006
  - micro-protein-P53973-fresh
  - micro-protein-Q06629-fresh
  - micro-protein-Q06623-fresh
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda1_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074156Z-hda1-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3015
- finding_id: micro-F2
  issue_key: hda-beta-resolve-hda-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Hda family mapping
  description: The Hda component and existing open task defer the exact family although
    native IPR017788 is the verified Hda branch, distinct from DnaA, and matches the
    reviewed reference protein.
  target_ids:
  - GO:1990085
  field_paths:
  - components[0].grounding_status
  - discussions[0]
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
  - micro-family-IPR017788-fresh
  - micro-family-IPR022864-fresh
  - micro-protein-P69931-fresh
  - micro-protein-P0A988-fresh
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda_beta_clamp_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074157Z-hda-beta-clamp-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3016
- finding_id: micro-F3
  issue_key: hir-resolve-hir3-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Hir3 whole-family mapping
  description: The open family task and Hir3 label-only row still defer a mapping
    despite verified IPR033053 Hir3/CABIN1 whole-family identity and the matching
    P47171 reference. Other HIR component boundaries remain unresolved by the inspected
    candidates.
  target_ids:
  - GO:0000417
  field_paths:
  - components[2].grounding_status
  - discussions[1]
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
  - micro-family-IPR033053-fresh
  - micro-family-IPR031120
  - micro-family-IPR014840
  - micro-protein-P32479-fresh
  - micro-protein-P32480-fresh
  - micro-protein-P47171-fresh
  - micro-protein-Q01448-fresh
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hir_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074158Z-hir-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3017
- finding_id: plaque-t4-F1
  issue_key: hops-exact-vps11-vps16-vps41-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground three named HOPS subunit classes
  description: Current native whole-family identities IPR016528 (Vps11), IPR016534
    (Vps16) and IPR016902 (Vps41), corroborated by matched reviewed protein memberships,
    reconfirm original F1. The active reviewed-label-only deferral and open task should
    record these exact mappings. This is not a requirement to ground every remaining
    class or rewrite dated discussion rationale.
  target_ids:
  - GO:0030897
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding_status
  - components[1].grounding_notes
  - components[5].grounding_status
  - components[5].grounding_notes
  evidence_ids:
  - plaque-t4-record
  - plaque-curation
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR016902
  - plaque-up-P12868
  - plaque-up-Q03308
  - plaque-up-P38959
  - plaque-t4-original
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hops_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: A grouped minor current grounding gap under the explicit reviewed-label-only
    contract; correct membership and protein examples already exist. This is not a
    blanket demand for all six optional mappings or a retrospective claim that old
    searches were false.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074159Z-hops-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3018
- finding_id: plaque-t8-F1
  issue_key: i-aaa-added-core-stoichiometry-source-support
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repair source support for the newly added i-AAA core and cofactor edges
  description: The current October24 addition asserts six Yme1 copies and six zinc
    cofactors from CPX-1655, but its full native response has present null stochiometry
    fields for every participant. The Yme1 edge also presents a purported verbatim
    rocky-road/spiral-staircase quotation attributed to DOI10.1083/jcb.201702125 which
    is absent from the complete genuine JATS (including captions). The cited Wu study
    supports recruitment/turnover, not this quoted structural claim. This materially
    misattributes central architecture evidence and conflicts with the record’s retained
    unspecified source counts. It does not establish that a separately studied isolated
    Yme1 core cannot be hexameric.
  target_ids:
  - GO:0031942
  field_paths:
  - causal_graphs[0].edges[0].description
  - causal_graphs[0].edges[0].evidence[0]
  - causal_graphs[0].edges[0].evidence[1].notes
  - causal_graphs[0].edges[1].description
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - plaque-t8-record
  - plaque-curation
  - plaque-stale-diff
  - plaque-cpx-1655
  - plaque-PMC5748973-s3
  - plaque-iaaa-attribution-proof
  - plaque-iaaa-peer-challenge
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/i_aaa_complex.yaml
    role: maintained scientific record
  native_severity: major
  normalization_reason: Central architecture is backed by a purported source quotation
    not present in the cited article and explicit database copy-count assertions contradicted
    by its unspecified fields. Grouped source-integrity correction, without denying
    supported participation or an independently evidenced isolated-core hexamer.
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3019
- finding_id: septin-holdfast-F1
  issue_key: holdfast-canonical-strain-source
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Correct the canonical holdfast model strain
  description: The canonical example names NA1000 tax565050 and attributes its anchoring/composition/c-di-GMP
    model role to Sulkowski2019. That study specifies CB15 and CB15-derived strains;
    the separately cited Sprecher study explicitly uses NA1000 as a nonadherent comparison.
    The current unqualified canonical strain/source pairing is materially misleading.
    Independently reconfirmed against the freshly inspected source/authority scopes
    recorded here. Correct current fields or append dated clarification in separately
    authorized curation; preserve historical rationale.
  target_ids:
  - cellstructuremech:holdfast
  field_paths:
  - canonical_examples[0]
  evidence_ids:
  - septin-record-holdfast
  - septin-original-holdfast
  - septin-curation-policy
  - septin-sulkowski-xml
  - septin-sprecher-xml
  - septin-tax-190650
  - septin-tax-565050
  - septin-up-A0A0H3CE47
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/holdfast.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: major
  normalization_reason: 'Major experimental-model identity mismatch: a named canonical
    strain is assigned work performed in a different strain, with a cited nonadherent
    comparison reinforcing the biological consequence. This does not reject the holdfast
    identity or the independently correct reference-protein accessions.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074158Z-holdfast-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3020
- finding_id: septin-holdfast-F2
  issue_key: holdfast-sulkowski-title
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Sulkowski paper title
  description: The DOI bibliography substitutes Old Cell Pole for Outer Membrane in
    the title. Native MED and the genuine primary title agree on A Multiprotein Complex
    Anchors Adhesive Holdfast at the Outer Membrane of Caulobacter crescentus. Independently
    reconfirmed against the freshly inspected source/authority scopes recorded here.
    Correct current fields or append dated clarification in separately authorized
    curation; preserve historical rationale.
  target_ids:
  - cellstructuremech:holdfast
  field_paths:
  - evidence[0].notes
  evidence_ids:
  - septin-record-holdfast
  - septin-original-holdfast
  - septin-curation-policy
  - septin-sulkowski-metadata
  - septin-sulkowski-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/holdfast.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: Localized bibliographic precision; the DOI resolves to the
    correct scientific study and the anchoring biology remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074158Z-holdfast-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3021
- finding_id: septin-hyphal_tip-F1
  issue_key: hyphal-tip-definition-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Source and qualify the expanded hyphal-tip definition
  description: The fungal GO identity is extended in the maintained defining text
    to oomycetes and generalized apparatus mechanisms while definition_source remains
    GO0001411. The exact GO definition and the cited Neurospora primary study do not
    establish that cross-lineage defining scope. Independently reconfirmed against
    the freshly inspected source/authority scopes recorded here. Correct current fields
    or append dated clarification in separately authorized curation; preserve historical
    rationale.
  target_ids:
  - GO:0001411
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-original-hyphal_tip
  - septin-curation-policy
  - septin-go
  - septin-lichius-xml
  - septin-lichius-metadata-abstract
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: major
  normalization_reason: The unsupported assertion changes the biological scope of
    the defining class, not merely a citation format. Exact GO identity remains intact,
    but it does not validate the added cross-lineage definition.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074200Z-hyphal-tip-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3022
- finding_id: septin-hyphal_tip-F2
  issue_key: hyphal-tip-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Label the spatial graph as nonmechanistic
  description: All five constituent edges are parthood statements and the final edge
    attaches a whole-structure function. The MECHANISTIC label and mechanism title
    imply a causal explanation that the graph does not encode. Independently reconfirmed
    against the freshly inspected source/authority scopes recorded here. Correct current
    fields or append dated clarification in separately authorized curation; preserve
    historical rationale.
  target_ids:
  - GO:0001411
  field_paths:
  - causal_graphs#hyphal_tip_mechanism.scope_status
  - causal_graphs#hyphal_tip_mechanism.title
  evidence_ids:
  - septin-record-hyphal_tip
  - septin-original-hyphal_tip
  - septin-curation-policy
  - septin-graph-policy
  - septin-schema-policy
  - septin-lichius-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported structure identity
    and source-specific biology.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074200Z-hyphal-tip-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3023
- finding_id: septin-ino80_complex-F1
  issue_key: ino80-exact-ies-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground five exact Ies subunit families
  description: Ies1, Ies2, Ies4, Ies5 and Ies6 remain REVIEWED_LABEL_ONLY because
    exact families were not curated in this pass. Current native full-family entries
    and independently verified protein membership resolve those specific classes.
    Independently reconfirmed against the freshly inspected source/authority scopes
    recorded here. Correct current fields or append dated clarification in separately
    authorized curation; preserve historical rationale.
  target_ids:
  - GO:0031011
  field_paths:
  - components#ies1_ino80c_subunit.grounding_status
  - components#ies2_ino80c_subunit.grounding_status
  - components#ies4_ino80c_subunit.grounding_status
  - components#ies5_ino80c_subunit.grounding_status
  - components#ies6_ino80c_arp5_module_subunit.grounding_status
  - discussions
  evidence_ids:
  - septin-record-ino80_complex
  - septin-original-ino80_complex
  - septin-curation-policy
  - septin-ipr-IPR038014
  - septin-ipr-IPR029523
  - septin-ipr-IPR062650
  - septin-ipr-IPR020366
  - septin-ipr-IPR029525
  - septin-up-P43579
  - septin-up-P40154
  - septin-up-Q08561
  - septin-up-P40060
  - septin-up-P32617
  - septin-watanabe-supplement
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ino80_complex.yaml
    role: maintained scientific record
  rule_id: Source-backed identity, grounding and claim scope
  native_severity: minor
  normalization_reason: A bounded correction preserves the supported structure identity
    and source-specific biology.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T074202Z-ino80-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/3024
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0070823
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda1_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground Hda1 and Hda3 at their
    verified whole-family identities and narrow the remaining task to Hda2.
  acceptance_checks:
  - Use IPR017321 for the yeast class-II Hda1 class and IPR026216 for Hda3.
  - Do not use shared IPR021006 as an exact Hda2-only mapping.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve all dated discussions.rationale, posed dates and curation events; record
    progress in current notes, narrow prompts or appended explanation rather than
    rewriting historical observations.
  - Retain supported protein examples, complex boundaries and permissible global UNKNOWN
    formation values; no new experiments or optional exhaustive inventory is required.
  - No maintained record edit occurs in this review PR.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:1990085
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hda_beta_clamp_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground Hda at the verified
    whole-family identity and resolve the existing task.
  acceptance_checks:
  - Use IPR017788 for the Hda class, retaining IPR022864 as narrower Enterobacteriaceae
    context.
  - Keep the DnaN beta ring as the already grounded GO complex and preserve the DnaA
    boundary.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve all dated discussions.rationale, posed dates and curation events; record
    progress in current notes, narrow prompts or appended explanation rather than
    rewriting historical observations.
  - Retain supported protein examples, complex boundaries and permissible global UNKNOWN
    formation values; no new experiments or optional exhaustive inventory is required.
  - No maintained record edit occurs in this review PR.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0000417
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hir_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, ground Hir3 in the verified
    homolog family and narrow the existing task to the unresolved component classes.
  acceptance_checks:
  - Use IPR033053 with the fungal Hir3 reference example and the native homolog breadth
    stated.
  - Do not use mixed HIR1/HIR2 IPR031120 or HRD domain IPR014840 as exact replacements
    for their named complete classes.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
  - Preserve all dated discussions.rationale, posed dates and curation events; record
    progress in current notes, narrow prompts or appended explanation rather than
    rewriting historical observations.
  - Retain supported protein examples, complex boundaries and permissible global UNKNOWN
    formation values; no new experiments or optional exhaustive inventory is required.
  - No maintained record edit occurs in this review PR.
- action_id: plaque-t4-A1
  finding_ids:
  - plaque-t4-F1
  target_ids:
  - GO:0030897
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hops_complex.yaml
    role: maintained scientific record
  description: Curate the verified Vps11/IPR016528, Vps16/IPR016534 and Vps41/IPR016902
    class mappings with exact scope and evidence; update current grounding notes/task
    disposition while preserving dated historical rationale. Do not substitute broader
    families or domains for other unresolved classes.
  acceptance_checks:
  - Each adopted family is the named whole protein class, with original role evidence
    retained.
  - Broader Vps39/Vps3, Vps41/Vps8, Sec1-like families and isolated domains are not
    substituted indiscriminately.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Historical discussion rationale and curation history remain append-only; no unsupported
    mechanism or necessity change.
- action_id: plaque-t8-A1
  finding_ids:
  - plaque-t8-F1
  target_ids:
  - GO:0031942
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/i_aaa_complex.yaml
    role: maintained scientific record
  description: 'Repair the new core/cofactor edge evidence: remove the absent quotation
    and incorrect CPX six-copy attribution. Preserve supported Yme1 proteolytic-core
    and zinc-cofactor participation. If precise hexameric/asymmetric architecture
    is retained, inspect and cite a genuinely supporting primary structural study
    and explicitly distinguish its preparation/isolated core from the adaptor-bearing
    yeast assembly; otherwise qualify or remove unsupported count/architecture clauses.
    Append the correction history without rewriting dated rationale.'
  acceptance_checks:
  - Each retained snippet is verifiably verbatim in its cited inspected source; paraphrases
    stay in notes.
  - CPX1655 participant copy numbers remain unspecified unless an actual source version
    supplies them; no fabricated six-copy annotation.
  - Any retained fixed architecture/count has claim-level primary support and explicit
    preparation/taxon/assembly scope.
  - Existing valid adaptor recruitment/turnover evidence and supported core/cofactor
    roles are preserved; no biological impossibility, universal necessity or new experiment
    demand inferred.
  - Separately authorized record curation uses the native writer and required focused
    validation/history checks.
- action_id: septin-holdfast-A1
  finding_ids:
  - septin-holdfast-F1
  target_ids:
  - cellstructuremech:holdfast
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/holdfast.yaml
    role: maintained scientific record
  description: Use the source-supported CB15 tax190650 canonical example, or provide
    directly read evidence for a specified restored/modified NA1000 genotype and restrict
    its claim accordingly. Keep CB15 experiments separate from the NA1000 HfsK reference
    sequence. This review PR does not edit the maintained record.
  acceptance_checks:
  - Canonical taxon, genotype, note and cited experiment agree.
  - Do not imply unmodified NA1000 supplies the reported adhesive model merely because
    its reference genome contains hfsK.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated discussion and curation history; use current-note edits or an appended
    dated clarification rather than rewriting provenance.
  - Do not infer universal formation necessity or require additional experiments from
    the source-specific observations.
- action_id: septin-holdfast-A2
  finding_ids:
  - septin-holdfast-F2
  target_ids:
  - cellstructuremech:holdfast
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/holdfast.yaml
    role: maintained scientific record
  description: Replace the title with the verified native title while retaining the
    correct DOI and scientific claims. This review PR does not edit the maintained
    record.
  acceptance_checks:
  - Title text matches the native bibliographic record and article header.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
  - Preserve dated discussion and curation history; use current-note edits or an appended
    dated clarification rather than rewriting provenance.
  - Do not infer universal formation necessity or require additional experiments from
    the source-specific observations.
- action_id: septin-hyphal_tip-A1
  finding_ids:
  - septin-hyphal_tip-F1
  target_ids:
  - GO:0001411
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  description: Retain the exact supported fungal-tip definition, or add directly relevant
    evidence and explicit taxon/architecture qualifications for the expanded scope.
    Preserve the supported Neurospora observations and distinguish prior fungal comparisons.
    This review PR does not edit the maintained record.
  acceptance_checks:
  - Do not claim that the lack of an oomycete mention proves biological absence.
  - Ensure every retained defining taxon/mechanistic extension is supported by an
    actually inspected source.
  - Preserve supported source-specific claims and pass applicable native gates.
  - Preserve dated discussion and curation history; use current-note edits or an appended
    dated clarification rather than rewriting provenance.
  - Do not infer universal formation necessity or require additional experiments from
    the source-specific observations.
- action_id: septin-hyphal_tip-A2
  finding_ids:
  - septin-hyphal_tip-F2
  target_ids:
  - GO:0001411
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hyphal_tip.yaml
    role: maintained scientific record
  description: Mark the current graph NONMECHANISTIC and describe its spatial/function
    scope, or add only directly sourced causal steps if a separate authorized curation
    establishes them. This review PR does not edit the maintained record.
  acceptance_checks:
  - Preserve the valid component identities, regional parthood and polarity function.
  - Preserve supported source-specific claims and pass applicable native gates.
  - Preserve dated discussion and curation history; use current-note edits or an appended
    dated clarification rather than rewriting provenance.
  - Do not infer universal formation necessity or require additional experiments from
    the source-specific observations.
- action_id: septin-ino80_complex-A1
  finding_ids:
  - septin-ino80_complex-F1
  target_ids:
  - GO:0031011
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ino80_complex.yaml
    role: maintained scientific record
  description: Map Ies1/IPR038014, Ies2/IPR029523, Ies4/IPR062650, Ies5/IPR020366
    and Ies6/IPR029525, preserving their correct yeast examples and existing complex/module
    boundaries. This review PR does not edit the maintained record.
  acceptance_checks:
  - Retain broader or unresolved other classes as label-only rather than substituting
    domains or shared paralog families.
  - Preserve supported source-specific claims and pass applicable native gates.
  - Preserve dated discussion and curation history; use current-note edits or an appended
    dated clarification rather than rewriting provenance.
  - Do not infer universal formation necessity or require additional experiments from
    the source-specific observations.
limitations:
- 'HDA1, Hda-beta clamp and HIR independent review: Assigned scientific scope is three
  complete nonstale records: HDA1,Hda-beta clamp,HIR.27 actually used maintained inputs
  are17 common rules/config/schema/scripts,three targets,six original artifacts and
  one frozen i-AAA target used only in a separate peer challenge. All47 frozen inputs
  and20 immutable originals are independently hash-audited in finalization.'
- 'HDA1, Hda-beta clamp and HIR independent review: Wu2001 genuine PMC main Methods/Results/Discussion,Tables
  and Figures1–6 text captions were read; no pixels/raw densitometry or supplements.
  Hydrodynamic mass supports a likely2:1:1 model, not atomic stoichiometry; conditional
  recovery,activity and locus-specific ChIP are separate.'
- 'HDA1, Hda-beta clamp and HIR independent review: Carmen1996 remains complete indexed
  abstract plus metadata only in this review; current DOI content negotiation yielded
  bibliographic metadata, not body. Earlier redirect/403 and Panther204 rows retain
  original dates/hashes and honest limits with corrected evidence kinds. No fresh
  Panther access or comprehensive alternative-family absence is claimed.'
- 'HDA1, Hda-beta clamp and HIR independent review: Kurz2004 genuine main body,Methods,Tables1/2
  and Figures1–3 captions read. Purified-binding assays and prior RIDA reaction evidence
  are distinguished; XL1Blue-derived genes and BL21(DE3)pLyS/TB1 preparations are
  not silently assigned reference K-12 or precise1k strain identities. Misfolding
  alternative remains.'
- 'HDA1, Hda-beta clamp and HIR independent review: Green2005 genuine main Results/Discussion,Figures1–4
  captions and Experimental Procedures pointer read. Supplementary detailed protocols/strain
  tables and pixels remain unread. HIR-Asf1 association, remaining-subunit recovery,DNA
  binding and deposition are different assays; global UNKNOWN is not a defect by itself.'
- 'HDA1, Hda-beta clamp and HIR independent review: Mousson2007 is secondary review/abstract
  only; localization articles are exact current indexed metadata/abstracts with UniProt
  annotation provenance, not freshly certified complete bodies. Where individual assays
  are not in an abstract, native annotation scope remains explicit.'
- 'HDA1, Hda-beta clamp and HIR independent review: Current family decisions use native
  type/name/hierarchy/signatures and positive reference xrefs. Generic shared classes
  are valid in principle; the bounded actions target explicitly named classes and
  existing tasks. No whole-protein identity is forced from a domain, no exhaustive
  family search or sequence alignment claimed.'
- 'HDA1, Hda-beta clamp and HIR independent review: Nine current exact reviewed gene/taxon
  queries each have one expected result and no next page; actual native primary/synonym/locus
  fields checked. This is not a reconstruction or disproof of historical selection
  execution.'
- 'HDA1, Hda-beta clamp and HIR independent review: Official catalogue has20 organism
  rows/28 pairs with no Saccharomyces. E.coli precise1k has201 modules,4257 genes,1035
  samples/518 conditions across BW25113,DGF-298,GMOS,MG1655,W3110. hda/b2496 and dnaN/b3701
  match reference accessions and each has0 thresholded memberships across201 rows.
  No gene absence, physical-complex evidence, foreign yeast proxy,AI narrative or
  activity-vector causality is inferred.'
- 'HDA1, Hda-beta clamp and HIR independent review: Historical local runner PermissionError
  remains the actual Nov3 00:49Z observation. Fresh official fallback responses have
  separate dates. Three failed S3 body routes are validation only. Initial sandbox
  DNS failures and exploratory wrong DOI/irrelevant GO probes are retained in scratch
  but not used as biological evidence.'
- 'HDA1, Hda-beta clamp and HIR independent review: Six current root native commands
  exit0: HDA1 three examples/three COVERED nodes;Hda-beta two examples/one COVERED
  Hda node,DnaN STRUCTURE;HIR four examples/four COVERED nodes. Native coverage does
  not establish biology. Original six validate/render commands and42 historical input
  occurrences pass. Root corpus gates/publication/successor/final-head/CI/queue remain
  separately owned, not precertified.'
- 'HDA1, Hda-beta clamp and HIR independent review: Three inherited minor grounding
  findings persist with exact repository/review/finding lineage and three bounded
  future actions. No new own science or stale target; three formal applicability corrections
  plus five historical kind-only occurrences are bundle defects. No record edits,
  broad grouped-issue resolution, universal necessity demand or optional-example defect.'
- 'HDA1, Hda-beta clamp and HIR independent review: Separate immutable i-AAA challenge
  validates source-attribution/quote limits for plaque; it is not an additional own
  scientific finding or complete i-AAA/image review. Exact genuine sources and frozen
  policy/record hashes are bound in that auxiliary receipt.'
- 'HOPS, Hsp78 and i-AAA independent review: Only assigned HOPS, Hsp78 and i-AAA whole
  records and their exact originals were scientifically reviewed. No neighboring record,
  category resolution or unrelated issue disposition inferred.'
- 'HOPS, Hsp78 and i-AAA independent review: Fresh exact native authorities and primary
  scopes are individually declared. Seals Methods/Results/Discussion, bounded Rieder
  core-association sections, Jaworek Results/Discussion/Methods/Data availability
  and Wu Introduction/Results/Discussion plus selected Methods were read; unlisted
  text and cited papers were not certified.'
- 'HOPS, Hsp78 and i-AAA independent review: Actual external Hsp78 Figures1/2 and
  Wu Figure3 pixels inspected; no other primary figure pixels, quantitative image
  reanalysis, complete supplementary workbook or raw proteomic reanalysis claimed.
  TableS1 read only specified ranges.'
- 'HOPS, Hsp78 and i-AAA independent review: Jaworek mutation, salt and protocol conflicts
  remain unresolved but explicitly disclosed by the record. Hsp78 native oligomers,
  purified SEC and activity/solubility/growth assays are not conflated.'
- 'HOPS, Hsp78 and i-AAA independent review: Older Yme1 topology language in Weber
  abstract/UniProt conflicts with modern GO/Wu IMS context. No silent harmonization
  or full-body review of the five older PMID sources claimed.'
- 'HOPS, Hsp78 and i-AAA independent review: i-AAA finding concerns the exact cited
  quotation and CPX count attribution. Complete source-text search is bounded to that
  article; it does not rule out an isolated hexamer established in other primary literature.'
- 'HOPS, Hsp78 and i-AAA independent review: The original runner failure is historical
  November3 00:49Z, not a new execution. The fresh complete official catalogue has
  no yeast dataset; no bacterial expression-host proxy, generated module summary or
  inferred biological absence used.'
- 'HOPS, Hsp78 and i-AAA independent review: Native verify/causal success checks identity
  and declared coverage. It does not establish mechanism, stoichiometry or necessity.
  HOPS Ypt7 external UNANCHORED_WITH_UNIPROT is appropriate, not a missing constituent.'
- 'HOPS, Hsp78 and i-AAA independent review: Original bundles and records are immutable;
  bundle corrections belong in the successor. Scientific actions remain proposed separate
  curation. Global QC, issue publication, final save/CI/queue are parent-owned and
  not independently certified by this source report.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: All four
  assigned current records are byte-identical to their historical frozen record inputs;
  this review refreshes source scrutiny and applicability without any record edit.
  The other six records are not scientifically re-reviewed in this subreport.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: All 55
  original input occurrences match their exact historical Git objects and four old
  pairs validate/render exactly. Historical batch26 global executions are preserved
  as scoped provenance, not reclassified as current PR2394 runs.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Hershey
  complete primary abstract directly enumerates all five claimed sugars. EPMC XML
  returned500, canonical PMC returned200 browser challenge, and two exact public S3
  prefixes returned no package; no genuine Hershey main body, Methods, table or pixel
  inspection is claimed.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Watanabe
  genuine versioned S3 XML and supplement PDF succeeded after failed EPMC/guessed
  paths. Only listed main-text sections and extracted Supplementary Tables1/2 were
  read; no raw MS files, atomic coordinates or figure pixels. Main-text table-number
  inversion is not turned into a record defect.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Shen2000/2003,
  Jonsson2004, Tosi2013 and ancillary localization/Rvb source papers are limited to
  their complete native abstracts; Clapier/Cairns2009 is explicitly secondary abstract
  context. No abstract is promoted to full Methods or an experimental-strain identity.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Lichius
  and Sprecher scope is the enumerated genuine source text and embedded relevant captions,
  not supplementary videos or pixels. Deletion/activity/localization observations
  do not establish universal formation necessity; no direct physical contact is inferred
  solely from colocalization.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: InterPro
  unchecked machine-generated prose is excluded. Native entry name/type plus independent
  UniProt cross-references are used for family identity. Shared full families/domains
  are not forced onto narrower classes; no exhaustive absence of optional identifiers
  is asserted.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Complete
  fresh official iModulonDB catalogue lacks the exact biological hosts and relevant
  named fungal comparison hosts. E. coli recombinant expression/cloning context is
  not a surrogate. Historical runner PermissionError retains its actual Nov3 00:49
  timestamp; no fresh runner invocation or biological absence inferred.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: Native
  source verification covers three reviewed holdfast examples, six unreviewed Neurospora
  example occurrences across two records and fifteen reviewed Ino80 examples:24 occurrences,21
  distinct constituent accessions plus external unreviewed HfsK. Twenty-three typed
  nodes comprise22 COVERED andone UNANCHORED_WITH_UNIPROT; this is reference coverage,
  not proof of membership or causality.'
- 'Holdfast, hyphal tip, hyphal tip polarisome and Ino80 independent review: No maintained
  local image is present in these four targets. Repository/Git/GitHub remain read-only.
  Parent-owned full QC, later successor validation, final-head CI and queue/merge
  are not certified by this source report.'
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
- One changed target, i-AAA complex, requires substantive current-input reassessment;
  nine other current target hashes match original frozen inputs. All used maintained
  context is frozen before synthesis.
- 'Twenty current native protein commands passed across 43 represented protein examples
  and 42 typed GENE_OR_PROTEIN nodes: 40 COVERED and two UNANCHORED_WITH_UNIPROT (holdfast
  HfsK and HOPS Ypt7). External machinery is not forced into constituent rows. Identity
  and coverage are not experimental membership or necessity evidence.'
- Original observations and dated rationale remain immutable. Source bodies, primary
  abstracts, database entries and failed-access diagnostics retain exact scopes and
  dates.
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074156Z-hda1-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074157Z-hda-beta-clamp-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074158Z-hir-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074158Z-holdfast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074159Z-hops-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074159Z-hsp78-chaperone-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074200Z-hyphal-tip-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074201Z-hyphal-tip-polarisome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074201Z-i-aaa-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T074202Z-ino80-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2394
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/3012
- https://github.com/CultureBotAI/CellStructureMech/issues/3013
- https://github.com/CultureBotAI/CellStructureMech/issues/3014
- https://github.com/CultureBotAI/CellStructureMech/issues/3015
- https://github.com/CultureBotAI/CellStructureMech/issues/3016
- https://github.com/CultureBotAI/CellStructureMech/issues/3017
- https://github.com/CultureBotAI/CellStructureMech/issues/3018
- https://github.com/CultureBotAI/CellStructureMech/issues/3019
- https://github.com/CultureBotAI/CellStructureMech/issues/3020
- https://github.com/CultureBotAI/CellStructureMech/issues/3021
- https://github.com/CultureBotAI/CellStructureMech/issues/3022
- https://github.com/CultureBotAI/CellStructureMech/issues/3023
- https://github.com/CultureBotAI/CellStructureMech/issues/3024
- https://github.com/CultureBotAI/CellStructureMech/issues/3025
```
