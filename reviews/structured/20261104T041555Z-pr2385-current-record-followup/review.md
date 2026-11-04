# PR 2385: current-input review of ten records and adversarial follow-up

- Review: 20261104T041555Z-pr2385-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-04T04:02:59.595459Z
- Finished UTC: 2026-11-04T04:15:55Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input independent review of all ten records substantively refreshes the stale COMA target, corrects ten unsupported structured-source exclusions and distinguishes two unsuccessful NEF3 access receipts from database evidence. Ten inherited scientific findings remain across nine targets: one major WDR1 protein-example identity finding and nine minor findings. The core primosome passes with explicit source limits. The overall verdict remains needs_curation; only linked immutable review successors are added.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 3276cff01a281a5d86d8122a0c34978a90e41ed2. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head bd8e9c4b16a27dc303533b69f4d3b8d8f0f977a5.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base e2498a28ea896fb9a053dc378380f1f44786a090.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0017119 | data/structures/other/cog_complex.yaml | maintained | COG complex |
| GO:0000817 | data/structures/other/coma_complex.yaml | maintained | COMA complex |
| GO:0030126 | data/structures/other/copi_vesicle_coat.yaml | maintained | COPI vesicle coat |
| GO:0030127 | data/structures/other/copii_vesicle_coat.yaml | maintained | COPII vesicle coat |
| GO:1990098 | data/structures/other/core_primosome_complex.yaml | maintained | core primosome complex |
| GO:0000438 | data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml | maintained | core TFIIH complex portion of holo TFIIH complex |
| GO:0000440 | data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml | maintained | core TFIIH complex portion of NEF3 complex |
| GO:0033263 | data/structures/other/corvet_complex.yaml | maintained | CORVET complex |
| cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml | maintained | CRL4WDR1 ubiquitin ligase complex |
| GO:0031390 | data/structures/other/ctf18_rfc_like_complex.yaml | maintained | Ctf18 RFC-like complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0017119 | passed | True | GO:0017119 | Documented focused command passed. |
| validate-strict GO:0017119 | passed | True | GO:0017119 | Documented focused command passed. |
| validate GO:0000817 | passed | True | GO:0000817 | Documented focused command passed. |
| validate-strict GO:0000817 | passed | True | GO:0000817 | Documented focused command passed. |
| validate GO:0030126 | passed | True | GO:0030126 | Documented focused command passed. |
| validate-strict GO:0030126 | passed | True | GO:0030126 | Documented focused command passed. |
| validate GO:0030127 | passed | True | GO:0030127 | Documented focused command passed. |
| validate-strict GO:0030127 | passed | True | GO:0030127 | Documented focused command passed. |
| validate GO:1990098 | passed | True | GO:1990098 | Documented focused command passed. |
| validate-strict GO:1990098 | passed | True | GO:1990098 | Documented focused command passed. |
| validate GO:0000438 | passed | True | GO:0000438 | Documented focused command passed. |
| validate-strict GO:0000438 | passed | True | GO:0000438 | Documented focused command passed. |
| validate GO:0000440 | passed | True | GO:0000440 | Documented focused command passed. |
| validate-strict GO:0000440 | passed | True | GO:0000440 | Documented focused command passed. |
| validate GO:0033263 | passed | True | GO:0033263 | Documented focused command passed. |
| validate-strict GO:0033263 | passed | True | GO:0033263 | Documented focused command passed. |
| validate cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Documented focused command passed. |
| validate-strict cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | Documented focused command passed. |
| validate GO:0031390 | passed | True | GO:0031390 | Documented focused command passed. |
| validate-strict GO:0031390 | passed | True | GO:0031390 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Whole-record applicability was assessed for all ten positive molecular or pathway narratives, correcting seven formal expression-only exclusions and three prose exclusions. Official source coverage is distinguished from biological applicability. The covered E. coli primosome genes are checked in the actual five-strain precise1k dataset, with bounded above-threshold membership and module context. Expression membership is not evidence of physical assembly or formation necessity. Other assigned organism contexts are not replaced with unrelated dataset hosts or strains. The unavailable runner receipt remains historical and separate from current catalogue access. |
| Independent claim-level source review | passed | True | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390 | Historical00:49Z invocation unavailable due to OS access restriction. Official catalogue fallback was inspected separately; no fresh invocation is claimed. Actual historical exit1 is retained in the evidence receipt; the native unavailable-check model has no execution exit-code field. |
| Native COG complex UniProt verify check | passed | True | GO:0017119 | 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COG complex UniProt causal check | passed | True | GO:0017119 | 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COMA complex UniProt verify check | passed | True | GO:0000817 | 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COMA complex UniProt causal check | passed | True | GO:0000817 | 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COPI vesicle coat UniProt verify check | passed | True | GO:0030126 | 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COPI vesicle coat UniProt causal check | passed | True | GO:0030126 | 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COPII vesicle coat UniProt verify check | passed | True | GO:0030127 | 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native COPII vesicle coat UniProt causal check | passed | True | GO:0030127 | 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native core primosome complex UniProt verify check | passed | True | GO:1990098 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native core primosome complex UniProt causal check | passed | True | GO:1990098 | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native core TFIIH complex portion of holo TFIIH complex UniProt verify check | passed | True | GO:0000438 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native core TFIIH complex portion of holo TFIIH complex UniProt causal check | passed | True | GO:0000438 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native core TFIIH complex portion of NEF3 complex UniProt verify check | passed | True | GO:0000440 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native core TFIIH complex portion of NEF3 complex UniProt causal check | passed | True | GO:0000440 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CORVET complex UniProt verify check | passed | True | GO:0033263 | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CORVET complex UniProt causal check | passed | True | GO:0033263 | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CRL4WDR1 ubiquitin ligase complex UniProt verify check | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native CRL4WDR1 ubiquitin ligase complex UniProt causal check | passed | True | cellstructuremech:crl4wdr1_ubiquitin_ligase_complex | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Ctf18 RFC-like complex UniProt verify check | passed | True | GO:0031390 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |
| Native Ctf18 RFC-like complex UniProt causal check | passed | True | GO:0031390 | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Native command returned zero. |

## Scientific And Domain Assessments

### Exact COMA structure and boundaries

identity: supported. Targets: GO:0000817.

GO0000817 exactly denotes Ctf19/Okp1/Mcm21/Ame1 COMA; GO0140513 is_a and kinetochore/nuclear-chromosome parthood agree. Neither broader CCAN nor optional Nkp1/2 is forced into this four-subunit record. Native GO Mcm1 typo is deliberately not adopted.

### Substantive four-node/four-edge refresh

provenance: supported. Targets: GO:0000817.

Current delta adds dated history, four component_ref protein nodes and constituent contributes_to edges. Native exact identities and genuine primary COMA composition support these edges. They do not claim atomic interfaces or resolve the two inherited grounding/association-evidence findings.

### Exact Mcm21 family with other-subunit bounds

grounding: concern. Targets: GO:0000817.

Current IPR018464 is a full CENP-O family explicitly including Mcm21 and directly linked by Q06675; retained REVIEWED_LABEL_ONLY is the inherited minor gap. AME1 domain IPR048743 and Ctf19 terminal-domain annotations do not automatically supply exact whole-protein identities for other rows.

### Four exact reviewed reference proteins

grounding: supported. Targets: GO:0000817.

Q02732CTF19/YPL018W, P53298OKP1/YGR179C, Q06675MCM21/YDR318W and P38313AME1/YBR211C are reviewed S288c559292 references. Fresh exact reviewed-gene queries return singleton maintained accessions. Native annotations/citations and primary physical membership remain distinct.

### Nuclear/kinetochore annotations and source tiers

evidence: supported. Targets: GO:0000817.

Native accession comments and ECO0000269 citation joins support the selected nuclear/kinetochore annotations. Ortiz/Huh are freshly read only at abstract tier; Schmitzberger native localization text is body-read. No raw individual Huh images or all strain derivatives are certified.

### Condition-scoped Okp1 physical-association evidence

grounding: concern. Targets: GO:0000817.

Fresh Schmitzberger sec11 and Methods31 establish native S.cerevisiae Okp1Δ325–337 loss of Ctf19 co-IP and Ctf19/Mcm21 localization, with Ame1/outer-kinetochore retention. This concrete bounded association/formation observation supports inherited F2; UNKNOWN itself is not a defect, and no universal ESSENTIAL/viability inference or mandatory new experiment follows.

### Native versus recombinant composition and mechanism

evidence: supported. Targets: GO:0000817.

DeWulf fresh abstract and Schmitzberger body support four-subunit COMA. K.lactis recombinant six-protein COMA-Nkp1-Nkp2 interaction/dimerization differs from native S.cerevisiae and does not force new whole-record stoichiometry or mandatory accessory components. Direct and indirect kinetochore contacts remain explicitly unresolved.

### Species canonical context and reference strains

scope: supported. Targets: GO:0000817.

Species4932 canonical/distribution context is distinct from four S288c559292 example annotations. Fresh native Schmitzberger methods specify most S288C derivatives with unread EV6 exceptions; no exact genotype is invented. COMMON remains qualitative ordinary machinery, not a strain census or universal claim.

### Bounded inner-to-outer kinetochore bridge

graph: supported. Targets: GO:0000817.

NONMECHANISTIC/ASSEMBLY outline retains grouped Cse4-proximal and Ndc80-complex outer nodes, with separately verified P36012/P40460/P33895/Q04477. Spc24 participation in outer attachment machinery is not a direct Spc24–microtubule assertion. Four new constituent edges are supported; primary sec15/16 distinctions between interactions and localization remain.

### Generic DNA-bound core versus narrower examples

identity: supported. Targets: GO:1990098.

GO1990098 exactly denotes the helicase/primase/DNA core, parent1990077. Preprimase1990099 and protein-only DnaB-DnaG1990156 remain distinct, not mandatory generic constituents. The resolved boundary discussion correctly avoids reducing the whole record to its bacterial protein-only example.

### Generic classes not incorrectly forced to bacterial families

grounding: supported. Targets: GO:1990098.

Replicative helicase and DNA primase are legitimate generic classes; DnaB IPR007692 and DnaG IPR050219 are narrower bacterial examples, while IPR006295 is a domain. No exact universal class identity is fabricated; reviewed label-only discussions and DNA template distinction remain bounded.

### Exact K12 reference examples

grounding: supported. Targets: GO:1990098.

Reviewed P0ACB0dnaB b4052/JW4012 and P0ABS5dnaG b3066/JW3038 agree with tax83333 and fresh singleton exact gene queries. Selection does not assert universality of these bacterial families across every primosome.

### Primer synthesis and secondary review scope

evidence: supported. Targets: GO:1990098.

GO0006269 primer synthesis and Kaguni secondary body support the E.coli oriC initiation/elongation context. Prepriming precedes DnaG addition; DnaG interactions during elongation are transient. The review is not misrepresented as a primary experiment and does not prove every generic mechanism or complete loader stoichiometry.

### No invented universal formation requirement

grounding: unknown. Targets: GO:1990098.

Current UNKNOWN fields and broad DNA template are appropriately bounded. General replication function and representative protein identity do not establish a cross-taxon depletion/formation matrix; no missing optional assay or exact chemistry is manufactured into a finding.

### Bacterial synthesis and K12 reference context

scope: supported. Targets: GO:1990098.

Canonical species562 E.coli synthesis in Kaguni is distinct from reference tax83333 and computational five-strain precise1k data. COMMON is qualitative; neither source alone establishes every strain or alternative replisome system.

### Nonmechanistic primer-synthesis outline

graph: supported. Targets: GO:1990098.

Helicase/primase/DNA contributions and broad primer formation agree with FUNCTION/NONMECHANISTIC scope. The maintained graph does not assert exact initiation order, atomic contact or universal DnaB/DnaG stoichiometry; native two-node diagnostic passes.

### Actual matched-host expression dataset and threshold context

scope: supported. Targets: GO:1990098.

Selected precise1k spans five named E.coli strains. b3066/dnaG exceeds module10 threshold; b4052/dnaB exceeds none among201. Module10 has15genes, regulator=null and nucleotide-stress context. Alias-query noncoverage is not absence; generated module prose/activity interpretation is not used. These results do not establish primosome assembly, localization, necessity or causal regulation.

### Exact alternative seven-subunit RFC-like complex

identity: supported. Targets: GO:0031390.

GO0031390 exact definition/synonyms and GO0140513 is_a relation agree: Ctf18/Dcc1/Ctf8 plus RFC2–5. Native Mayer primary abstract identifies this alternative complex, distinct from RFC1/Rad24-containing loaders and from PCNA client.

### Three exact family identities versus shared small-RFC scope

grounding: concern. Targets: GO:0031390.

IPR053016 Ctf18, IPR019128 Dcc1 and IPR018607 Ctf8 are exact families; three current rows remain REVIEWED_LABEL_ONLY. Dcc1/Ctf8 native examples link their families; reviewed ortholog members separately support IPR053016 identity without falsely claiming a P49956 xref. Shared IPR050238 and AAA/RFC domains do not distinguish RFC2–5. Generated prose is excluded from biology.

### Seven exact reviewed reference examples

grounding: supported. Targets: GO:0031390.

All seven maintained accessions, native primary genes/loci and S288c559292 taxa are correct; fresh reviewed-gene queries each return the intended singleton. Reference identity and family coverage do not by themselves prove all molecular activities.

### Ctf8 nuclear annotation and abstract limits

evidence: supported. Targets: GO:0031390.

Native P38877 nuclear localization annotation carries PMID11389843/ECO0000269; the source is freshly inspected only at complete primary-abstract tier. This verifies the authority attribution without claiming the actual microscopy images or full experimental localization protocol were read.

### Membership/cohesion distinct from formation necessity

grounding: unknown. Targets: GO:0031390.

Mayer primary abstract supports seven-member association and cohesion phenotypes; deletion growth/cohesion is not a complete assembly-depletion matrix. UNKNOWN formation fields remain bounded; no compulsory optional assay or universal ESSENTIAL assertion is introduced.

### Clamp loading and cohesion scope

evidence: supported. Targets: GO:0031390.

GO0031390/0003689/0007062 and Kim-MacNeill secondary abstract support alternative clamp-loading/cohesion context. Mayer is primary abstract-only; no detailed purified loading cycle or individual mechanistic sequence is certified.

### Species and strain distinction

scope: supported. Targets: GO:0031390.

Species4932 canonical context is distinct from seven S288c559292 reference examples. The abstract supports S.cerevisiae without demonstrating every precise genotype; no strain substitution or numerical prevalence inference is made.

### Seven constituents and two bounded functions

graph: supported. Targets: GO:0031390.

Seven component_ref contributions to the alternative clamp loader and clamp-loading/cohesion outputs fit FUNCTION/NONMECHANISTIC. PCNA is a client, not forced into constituent inventory; no unsupported ATPase order or universal necessity is asserted.

### Original exclusion corrected by actual host assessment

scope: concern. Targets: GO:0000817.

Original formal check excludes iModulonDB only because no expression-module assertion exists, despite positive protein/pathway content. Native policy requires applicability. Fresh catalogue gives no natural yeast match for COMA/Ctf18; primosome has selected E.coli precise1k gene/module evidence with explicit five-strain and threshold limits. Historical unavailable runner remains separately dated.

### Historical discussion and immutable lineage

provenance: supported. Targets: GO:0000817.

All original findings/actions and current discussions reviewed. Dated rationale/posed_date/history remain append-only; source-neutral grounding TODOs are not automatically resolved by taxon-specific examples. Proposed curation narrows current notes/prompt only after supported changes; records remain untouched.

### Original deterministic artifacts and actual native coverage

schema: supported. Targets: GO:0000817.

Three original pairs validate/render exactly with41 frozen historical inputs and six immutable artifacts. Current own native checks pass: COMA4examples/6typed(4COVERED+2unanchoredxref), primosome2/2covered, Ctf18RFC7/7covered. These results are not biological proof or family-completeness certificates.

### Whole-record coverage with explicit access boundaries

completeness: supported. Targets: GO:0000817.

Complete maintained record and original assessment inspected; no local images/quantitative properties present. Source body/abstract/authority tiers remain explicit; no raw microscopy, sequence alignments, supplemental strain table or cited primary work not read is certified.

### Current independent disposition

other: concern. Targets: GO:0000817.

needs_curation: two inherited minor findings independently confirmed; current COMA additions valid and no new scientific finding.

### Original exclusion corrected by actual host assessment

scope: concern. Targets: GO:1990098.

Original formal check excludes iModulonDB only because no expression-module assertion exists, despite positive protein/pathway content. Native policy requires applicability. Fresh catalogue gives no natural yeast match for COMA/Ctf18; primosome has selected E.coli precise1k gene/module evidence with explicit five-strain and threshold limits. Historical unavailable runner remains separately dated.

### Historical discussion and immutable lineage

provenance: supported. Targets: GO:1990098.

All original findings/actions and current discussions reviewed. Dated rationale/posed_date/history remain append-only; source-neutral grounding TODOs are not automatically resolved by taxon-specific examples. Proposed curation narrows current notes/prompt only after supported changes; records remain untouched.

### Original deterministic artifacts and actual native coverage

schema: supported. Targets: GO:1990098.

Three original pairs validate/render exactly with41 frozen historical inputs and six immutable artifacts. Current own native checks pass: COMA4examples/6typed(4COVERED+2unanchoredxref), primosome2/2covered, Ctf18RFC7/7covered. These results are not biological proof or family-completeness certificates.

### Whole-record coverage with explicit access boundaries

completeness: supported. Targets: GO:1990098.

Complete maintained record and original assessment inspected; no local images/quantitative properties present. Source body/abstract/authority tiers remain explicit; no raw microscopy, sequence alignments, supplemental strain table or cited primary work not read is certified.

### Current independent disposition

other: supported. Targets: GO:1990098.

pass_with_limitations: positive identity, class and function assessments; generic formation and source-access limits remain, no scientific finding.

### Original exclusion corrected by actual host assessment

scope: concern. Targets: GO:0031390.

Original formal check excludes iModulonDB only because no expression-module assertion exists, despite positive protein/pathway content. Native policy requires applicability. Fresh catalogue gives no natural yeast match for COMA/Ctf18; primosome has selected E.coli precise1k gene/module evidence with explicit five-strain and threshold limits. Historical unavailable runner remains separately dated.

### Historical discussion and immutable lineage

provenance: supported. Targets: GO:0031390.

All original findings/actions and current discussions reviewed. Dated rationale/posed_date/history remain append-only; source-neutral grounding TODOs are not automatically resolved by taxon-specific examples. Proposed curation narrows current notes/prompt only after supported changes; records remain untouched.

### Original deterministic artifacts and actual native coverage

schema: supported. Targets: GO:0031390.

Three original pairs validate/render exactly with41 frozen historical inputs and six immutable artifacts. Current own native checks pass: COMA4examples/6typed(4COVERED+2unanchoredxref), primosome2/2covered, Ctf18RFC7/7covered. These results are not biological proof or family-completeness certificates.

### Whole-record coverage with explicit access boundaries

completeness: supported. Targets: GO:0031390.

Complete maintained record and original assessment inspected; no local images/quantitative properties present. Source body/abstract/authority tiers remain explicit; no raw microscopy, sequence alignments, supplemental strain table or cited primary work not read is certified.

### Current independent disposition

other: concern. Targets: GO:0031390.

needs_curation: one inherited minor exact-family subset finding independently confirmed; other supported scopes retained.

### native schema

schema: supported. Targets: GO:0017119.

8 REVIEWED examples/8 typed nodes; all typed nodes COVERED. Historical original and current input checks pass; source identity remains independent of sequence coverage.

### identity scope

identity: supported. Targets: GO:0017119.

Exact active GO identity and coat/tethering boundaries match. Species4932 canonical scope is distinct from reviewed reference strain559292 and the actual laboratory or recombinant preparations. The record is a complex/coat, not a single protein.

### completeness

completeness: supported. Targets: GO:0017119.

Full record read; no maintained image or numeric physical-property observation requiring pixel/measurement verification. Optional examples, additional variable adaptors and exhaustive paralog inventories are not required. No unsupported mandatory experiment is imposed.

### structured source

evidence: supported. Targets: GO:0017119.

Positive protein/traffic/tethering claims trigger coverage review. Original checks[4] formal no-expression exemption is unsupported. Fresh catalogue has no matching biological host, so no downstream foreign-organism proxy is used. Historical00:49Z runner failure remains historical; no fresh runner execution claimed.

### historical provenance

provenance: supported. Targets: GO:0017119.

Original frozen input is identical to current target; native pair/render and source inputs verified. Exact inherited F1 lineage retained, no blanket category or neighboring issue resolution inferred; dated rationale remains append-only.

### necessity

scope: supported. Targets: GO:0017119.

UNKNOWN formation essentiality is retained. Functional transport defects, viability, interaction or reconstituted assembly under selected conditions are not automatically universal structure-formation necessity. Broad grouped components and external interactors are permitted.

### native schema

schema: supported. Targets: GO:0030126.

9 REVIEWED examples/2 typed nodes; all typed nodes COVERED. Historical original and current input checks pass; source identity remains independent of sequence coverage.

### identity scope

identity: supported. Targets: GO:0030126.

Exact active GO identity and coat/tethering boundaries match. Species4932 canonical scope is distinct from reviewed reference strain559292 and the actual laboratory or recombinant preparations. The record is a complex/coat, not a single protein.

### completeness

completeness: supported. Targets: GO:0030126.

Full record read; no maintained image or numeric physical-property observation requiring pixel/measurement verification. Optional examples, additional variable adaptors and exhaustive paralog inventories are not required. No unsupported mandatory experiment is imposed.

### structured source

evidence: supported. Targets: GO:0030126.

Positive protein/traffic/tethering claims trigger coverage review. Original notes[1] prose-only no-applicability exemption is unsupported. Fresh catalogue has no matching biological host, so no downstream foreign-organism proxy is used. Historical00:49Z runner failure remains historical; no fresh runner execution claimed.

### historical provenance

provenance: supported. Targets: GO:0030126.

Original frozen input is identical to current target; native pair/render and source inputs verified. Exact inherited F1 lineage retained, no blanket category or neighboring issue resolution inferred; dated rationale remains append-only.

### necessity

scope: supported. Targets: GO:0030126.

UNKNOWN formation essentiality is retained. Functional transport defects, viability, interaction or reconstituted assembly under selected conditions are not automatically universal structure-formation necessity. Broad grouped components and external interactors are permitted.

### native schema

schema: supported. Targets: GO:0030127.

5 REVIEWED examples/3 typed nodes; all typed nodes COVERED. Historical original and current input checks pass; source identity remains independent of sequence coverage.

### identity scope

identity: supported. Targets: GO:0030127.

Exact active GO identity and coat/tethering boundaries match. Species4932 canonical scope is distinct from reviewed reference strain559292 and the actual laboratory or recombinant preparations. The record is a complex/coat, not a single protein.

### completeness

completeness: supported. Targets: GO:0030127.

Full record read; no maintained image or numeric physical-property observation requiring pixel/measurement verification. Optional examples, additional variable adaptors and exhaustive paralog inventories are not required. No unsupported mandatory experiment is imposed.

### structured source

evidence: supported. Targets: GO:0030127.

Positive protein/traffic/tethering claims trigger coverage review. Original notes[1] prose-only no-applicability exemption is unsupported. Fresh catalogue has no matching biological host, so no downstream foreign-organism proxy is used. Historical00:49Z runner failure remains historical; no fresh runner execution claimed.

### historical provenance

provenance: supported. Targets: GO:0030127.

Original frozen input is identical to current target; native pair/render and source inputs verified. Exact inherited F1 lineage retained, no blanket category or neighboring issue resolution inferred; dated rationale remains append-only.

### necessity

scope: supported. Targets: GO:0030127.

UNKNOWN formation essentiality is retained. Functional transport defects, viability, interaction or reconstituted assembly under selected conditions are not automatically universal structure-formation necessity. Broad grouped components and external interactors are permitted.

### native schema

schema: supported. Targets: GO:0033263.

6 REVIEWED examples/7 typed nodes; six COVERED constituents and one externally anchored Vps21 interactor (UNANCHORED_WITH_UNIPROT), not a missing seventh constituent. Historical original and current input checks pass; source identity remains independent of sequence coverage.

### identity scope

identity: supported. Targets: GO:0033263.

Exact active GO identity and coat/tethering boundaries match. Species4932 canonical scope is distinct from reviewed reference strain559292 and the actual laboratory or recombinant preparations. The record is a complex/coat, not a single protein.

### completeness

completeness: supported. Targets: GO:0033263.

Full record read; no maintained image or numeric physical-property observation requiring pixel/measurement verification. Optional examples, additional variable adaptors and exhaustive paralog inventories are not required. No unsupported mandatory experiment is imposed.

### structured source

evidence: supported. Targets: GO:0033263.

Positive protein/traffic/tethering claims trigger coverage review. Original notes[1] prose-only no-applicability exemption is unsupported. Fresh catalogue has no matching biological host, so no downstream foreign-organism proxy is used. Historical00:49Z runner failure remains historical; no fresh runner execution claimed.

### historical provenance

provenance: supported. Targets: GO:0033263.

Original frozen input is identical to current target; native pair/render and source inputs verified. Exact inherited F1 lineage retained, no blanket category or neighboring issue resolution inferred; dated rationale remains append-only.

### necessity

scope: supported. Targets: GO:0033263.

UNKNOWN formation essentiality is retained. Functional transport defects, viability, interaction or reconstituted assembly under selected conditions are not automatically universal structure-formation necessity. Broad grouped components and external interactors are permitted.

### family grounding

grounding: concern. Targets: GO:0017119.

Eight exact named generic COG classes are represented by IPR033370/009316/007265/048682/019465/010490/019335/007255. Five yeast instances carry their corresponding whole-family annotation; Cog1/2/7 do not, so class grounding must not be misrepresented as new sequence annotation. Reviewed ortholog-member queries and primary divergent-ortholog context support the class interpretation.

### composition architecture

representation: supported. Targets: GO:0017119.

The eight subunits and lobeA1–4/lobeB5–8 match COG architecture. Ha uses recombinant yeast-sequence COG produced in E.coli; separate Kluyveromyces lobe-B work is not conflated. Ishii distinguishes cytosolic octamer from membrane subassemblies. COPI/SNARE interactions do not add constituents.

### graph localization

graph: supported. Targets: GO:0017119.

NONMECHANISTIC membership and Golgi-transport participation are bounded. Removed mammalian-backed yeast localization is not reintroduced. Native Cog3/Cog2 experimental Golgi annotations have specific yeast source joins; other Cog localization annotations largely by similarity remain distinct.

### protein selection

grounding: concern. Targets: GO:0030126.

All nine reviewed instances agree with declared coatomer/Arf symbols and aliases. P53622 primary COP1 aliasRET1 remains correct, but the exact reviewed559292 RET1 query also returns polymeraseP22276; inherited F1 corrects current uniqueness provenance only.

### experimental graph

graph: supported. Targets: GO:0030126.

Coarse coatomer/Arf association, membrane-coat membership, Golgi context and retrieval are supported. Yu mixed-species recombinant structural/biochemical work supplies a recruitment model, not an intact live yeast assembly cycle. Sandmann complete abstract supports yeast retrieval/KKXX scope; no inaccessible body claims made.

### native localization

evidence: supported. Targets: GO:0030126.

Arf1Golgi evidence joins15504911, Arf2/Sec26 joins14562095; native source attribution checked alongside complete primary abstracts. Database by-similarity annotations for other coatomer proteins are not portrayed as independently read direct experiments.

### sar1 grounding

grounding: concern. Targets: GO:0030127.

Exact whole SAR1 family IPR006687 matches current Sar1 class and nativeP20606 cross-reference. This does not ground the distinct Sec23/24 or Sec13/31 heteromeric components with single-protein families.

### composition protein

representation: supported. Targets: GO:0030127.

Five core examples agree with their identities and coarse coat roles. Sec13 is shared with NPC/SEA; Rout2000 is explicitly NPC-localization evidence, not false COPII membership proof. Variable Sfb2/Lst1 cargo coats do not make the stated core inventory an exhaustive-variable-coat claim.

### assembly graph

graph: supported. Targets: GO:0030127.

Sequential Sar1 membrane recruitment then Sec23/24 and Sec13/31 is supported in defined reconstitution. Native/defined membrane stoichiometries, size, nucleotide conditions and fixed-sample EM are distinguished. NONMECHANISTIC graph does not claim a complete universal cargo/hydrolysis cycle or invariant stoichiometry.

### exact families

grounding: concern. Targets: GO:0033263.

Vps11/Pep5 IPR016528 and Vps16 IPR016534 match named whole-protein classes and verified instances. Vps3/Vps39, Vps8/Vps41, Sec1 broad families and Vps18 domain are excluded; shared HOPS membership does not invalidate exact protein-class identity.

### composition interactors

representation: supported. Targets: GO:0033263.

Six native examples match Vps3,Vps8,Pep5/Vps11,Vps16,Pep3/Vps18,Vps33 aliases/loci. Peplowska primary abstract and exact GO support six-subunit CORVET/shared classC core. Vps21 is an external Rab interactor, not a seventh constituent.

### localization graph

graph: supported. Targets: GO:0033263.

Descriptive CORVET/Vps21/endosome biogenesis graph is supported at primary-abstract/authority scope, not detailed unread direct-binding Methods. PEP5 vacuole-membrane evidence from Seals concerns HOPS/shared protein; record keeps it separate from CORVET-specific endosome scope.

### Structure identity and containing-complex boundary

identity: supported. Targets: GO:0000438.

Seven-subunit TFIIH core portion has exact GO identity; TFIIK partner remains outside holo core.

### Exact molecular identity versus broad family

grounding: concern. Targets: GO:0000438.

All seven exact InterPro full-protein families are independently corroborated by reviewed example xrefs. IPR001945 mixed XPG/Rad2 prose does not override the independently matched RAD3/XPD name/member identity; broad generic domains are not substitutes.

### Native accession/status/primary-name and source-locus identity

grounding: supported. Targets: GO:0000438.

Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Current reviewed exact yeast queries return the intended seven genes. Huh nuclear localization is distinct from core membership and functional necessity.

### Actual source access and experiment scopes

evidence: supported. Targets: GO:0000438.

Murakami genuine body sections and canonical ontology/native annotations support composition; Takagi,Ranish,Huh current access is complete metadata/abstract, not unread full bodies.

### Formation necessity versus functional dependence

evidence: unknown. Targets: GO:0000438.

All seven formation-necessity fields remain UNKNOWN. Transcription/DNA-repair defects and purified subcomplex behavior do not establish universal obligatory formation sequence; Tfb6-dependent alternative purification states remain experimental context.

### Complete descriptive graph and evidence mapping

graph: supported. Targets: GO:0000438.

ASSEMBLY/NONMECHANISTIC seven constituent links plus holo parthood describe coarse composition without kinase chemistry or ordered assembly.

### Canonical lineage and reference-versus-assay strains

scope: supported. Targets: GO:0000438.

Saccharomyces4932 and S288C559292 resolve; Murakami multiple yeast backgrounds and bacterial production hosts are not silently equated to reference examples. COMMON is qualitative, not population prevalence.

### Composition, time and size claims

quantity: supported. Targets: GO:0000438.

Canonical seven-core versus three-TFIIK partition is distinguished from Tfb6-associated11-subunit purification and dissociated states; no universal fixed assembly stoichiometry or physical dimension is inferred.

### Maintained image and attribution

evidence: not_applicable. Targets: GO:0000438.

No maintained image on this target.

### Original schema/render and frozen source inputs

schema: supported. Targets: GO:0000438.

Actual original native validate/render0 and exact paired Markdown; 14 historical input occurrences match Git source. Current target nonstale. Batch26 historical global execution is not falsely relabeled fresh48 execution.

### Inventory coverage and unresolved boundaries

completeness: supported. Targets: GO:0000438.

Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Seven canonical classes sufficiently scoped without adding TFIIK/Rad2/Tfb6 as mandatory members of every core context.

### Current correction and immutable dated discussions

provenance: supported. Targets: GO:0000438.

Preserve dated rationale,posed/retrieved dates and curation history. Update current grounding notes/prompts or append a dated clarification; current stale no-examples wording may be reconciled without erasing the earlier observation. No neighbor/group issue disposition inferred.

### Actual whole-record structured-source applicability

evidence: supported. Targets: GO:0000438.

Positive protein/pathway assertions trigger host coverage assessment; lack of expression-module claims is insufficient. Fresh complete official catalogue has no matching Saccharomyces/S288C dataset. Matched downstream gene/module requests do not apply after this bounded assessment; bacterial production hosts are not proxies. Historical00:49Z runner failure and direct current fallback are separate.

### Independent current scientific outcome

consistency: concern. Targets: GO:0000438.

Needs curation for one independently confirmed inherited minor exact-family grounding finding. Qualified positive identity/association/function/source assessments remain; no new record defect is established from optional fields, unavailable bodies or broad families.

### Structure identity and containing-complex boundary

identity: supported. Targets: GO:0000440.

Exact NEF3-context core identity; Rad2 partner is outside core and distinct from core Rad3/XPD.

### Exact molecular identity versus broad family

grounding: concern. Targets: GO:0000440.

All seven exact InterPro full-protein families are independently corroborated by reviewed example xrefs. IPR001945 mixed XPG/Rad2 prose does not override the independently matched RAD3/XPD name/member identity; broad generic domains are not substitutes.

### Native accession/status/primary-name and source-locus identity

grounding: supported. Targets: GO:0000440.

Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Current reviewed exact yeast queries return the intended seven genes. Huh nuclear localization is distinct from core membership and functional necessity.

### Actual source access and experiment scopes

evidence: supported. Targets: GO:0000440.

Murakami genuine body sections and canonical ontology/native annotations support composition; Takagi,Ranish,Huh current access is complete metadata/abstract, not unread full bodies. Prakash is a secondary-review abstract; failed/redirect routes are validation context only.

### Formation necessity versus functional dependence

evidence: unknown. Targets: GO:0000440.

All seven formation-necessity fields remain UNKNOWN. Transcription/DNA-repair defects and purified subcomplex behavior do not establish universal obligatory formation sequence; Tfb6-dependent alternative purification states remain experimental context.

### Complete descriptive graph and evidence mapping

graph: supported. Targets: GO:0000440.

FUNCTION/NONMECHANISTIC seven constituent links, NEF3 parthood and NER support remain coarse; Rad2 nuclease mechanism is not mislabeled as Rad3 activity.

### Canonical lineage and reference-versus-assay strains

scope: supported. Targets: GO:0000440.

Saccharomyces4932 and S288C559292 resolve; Murakami multiple yeast backgrounds and bacterial production hosts are not silently equated to reference examples. COMMON is qualitative, not population prevalence.

### Composition, time and size claims

quantity: supported. Targets: GO:0000440.

Canonical seven-core versus three-TFIIK partition is distinguished from Tfb6-associated11-subunit purification and dissociated states; no universal fixed assembly stoichiometry or physical dimension is inferred.

### Maintained image and attribution

evidence: not_applicable. Targets: GO:0000440.

No maintained image on this target.

### Original schema/render and frozen source inputs

schema: supported. Targets: GO:0000440.

Actual original native validate/render0 and exact paired Markdown; 14 historical input occurrences match Git source. Current target nonstale. Batch26 historical global execution is not falsely relabeled fresh48 execution.

### Inventory coverage and unresolved boundaries

completeness: supported. Targets: GO:0000440.

Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Seven canonical classes sufficiently scoped without adding TFIIK/Rad2/Tfb6 as mandatory members of every core context.

### Current correction and immutable dated discussions

provenance: supported. Targets: GO:0000440.

Preserve dated rationale,posed/retrieved dates and curation history. Update current grounding notes/prompts or append a dated clarification; current stale no-examples wording may be reconciled without erasing the earlier observation. No neighbor/group issue disposition inferred.

### Actual whole-record structured-source applicability

evidence: supported. Targets: GO:0000440.

Positive protein/pathway assertions trigger host coverage assessment; lack of expression-module claims is insufficient. Fresh complete official catalogue has no matching Saccharomyces/S288C dataset. Matched downstream gene/module requests do not apply after this bounded assessment; bacterial production hosts are not proxies. Historical00:49Z runner failure and direct current fallback are separate.

### Independent current scientific outcome

consistency: concern. Targets: GO:0000440.

Needs curation for one independently confirmed inherited minor exact-family grounding finding. Qualified positive identity/association/function/source assessments remain; no new record defect is established from optional fields, unavailable bodies or broad families.

### Structure identity and containing-complex boundary

identity: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Local source-defined WDR1-Cullin4-DDB1 association is narrower than generic Cul4-RING and different named GOcomplexes. Catalytic completeness and obligatory RING identity remain unresolved, without inventing new subunits.

### Exact molecular identity versus broad family

grounding: concern. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Q582R9/Tb927.3.4660 is a different native locus from Hu WDR1/Tb927.10.15080; source-locus zero query cannot authorize the substitution. Broad cullin or RSE1/DDB1/CPSF1 families do not independently specify this assembly; generated family prose excluded.

### Native accession/status/primary-name and source-locus identity

grounding: concern. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Three unreviewed example occurrences/three distinct accessions and one COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not validate the disputed biological assignment.Native identities resolve all three unreviewed accessions, but only Cullin4/DDB1 source loci agree. These identifiers are ORF names rather than formal primary geneName fields. TREU927 is a reference background, not the29-13/Lister427 experimental strain.

### Actual source access and experiment scopes

evidence: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Hu genuine body/captions support source loci and bounded associations/perturbations. Yeast fragments, GST-plus-lysate and co-IP are not a fully purified direct interaction assay. Anti-ubiquitin species may be PLK or partners; phenocopy is not rescue or exclusive mediation. 2025 source table/discussion nomenclature conflict remains explicit.

### Formation necessity versus functional dependence

evidence: unknown. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

All three formation-necessity fields remain UNKNOWN. WDR1 RNAi growth/duplication defects and protein turnover changes do not establish universal assembly necessity or complete catalytic composition.

### Complete descriptive graph and evidence mapping

graph: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

FUNCTION/NONMECHANISTIC RNAi-output graph keeps24h chase/IP/phosphorylation,24/48h protein and48h organelle/attachment outcomes distinct. It does not claim direct covalent ubiquitination, rescue, ordered mediation or client PLK as an invariant component. Its WDR1 actor biological identity remains affected by the inherited example finding despite native COVERED.

### Canonical lineage and reference-versus-assay strains

scope: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Tbrucei5691 and TREU927185431 resolve. Procyclic29-13 RNAi/Lister427 tagging and2025Lister427 experiments are distinct from reference accessions; yeast/Ecoli assay production hosts are not canonical CRL4WDR1 examples. COMMON is qualitative.

### Composition, time and size claims

quantity: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Three supported associated classes do not assert complete catalytic stoichiometry. Source24/48h endpoints and localization5µm scale are scoped; no whole-ligase size or purified ubiquitination rate is claimed.

### Maintained image and attribution

evidence: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Actual frozen Figure2A–F pixels inspected and exact external SHA/MD5 matched. Author attribution/CC-BY4.0 licensed source supported. Image depicts constructs/assays and WDR1 localization, not whole-ligase morphology. FpixelG1-versus-captionS inconsistency is retained as source limitation; maintained G1/S wording is not contradicted. Other record figures are not newly pixel-certified.

### Original schema/render and frozen source inputs

schema: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Actual original native validate/render0 and exact paired Markdown; 15 historical input occurrences match Git source. Current target nonstale. Batch26 historical global execution is not falsely relabeled fresh48 execution.

### Inventory coverage and unresolved boundaries

completeness: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Three unreviewed example occurrences/three distinct accessions and one COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not validate the disputed biological assignment.Cullin4/DDB1 examples remain reference associations; current wrong-WDR1 assignment is actionable. RING, broader DCAFs and complete reaction machinery are explicitly unresolved, not automatically mandatory gaps.

### Current correction and immutable dated discussions

provenance: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Preserve dated rationale,posed/retrieved dates and curation history. Update current grounding notes/prompts or append a dated clarification; current stale no-examples wording may be reconciled without erasing the earlier observation. No neighbor/group issue disposition inferred.

### Actual whole-record structured-source applicability

evidence: supported. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Positive protein/pathway assertions trigger host coverage assessment; lack of expression-module claims is insufficient. Fresh complete official catalogue has no matching Trypanosoma/TREU927/Lister427/29-13 dataset. Matched downstream gene/module requests do not apply after this bounded assessment; bacterial production hosts are not proxies. Historical00:49Z runner failure and direct current fallback are separate.

### Independent current scientific outcome

consistency: concern. Targets: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex.

Needs curation for one independently confirmed inherited major wrong receptor-example finding. Qualified positive identity/association/function/source assessments remain; no new record defect is established from optional fields, unavailable bodies or broad families.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0017119, GO:0000817, GO:0030126, GO:0030127, GO:1990098, GO:0000438, GO:0000440, GO:0033263, cellstructuremech:crl4wdr1_ubiquitin_ligase_complex, GO:0031390.

1 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### micro-F1: Ground the Mcm21 subunit with its exact ortholog family

minor / open / confirmed; issue key: coma-mcm21-family.

IPR018464 is a full family explicitly including yeast Mcm21 and is cross-referenced by Q06675. The maintained Mcm21 row remains REVIEWED_LABEL_ONLY. AME1 and Ctf19 domain candidates do not justify assigning whole-protein groundings to those rows.

### micro-F2: Capture the condition-scoped Okp1 assembly requirement

minor / open / confirmed; issue key: coma-okp1-formation-evidence.

The current Okp1 component lacks the specific physical-association evidence independently confirmed in Schmitzberger2017 Results sec11 and Methods31: native S.cerevisiae Okp1Δ325–337 loses Ctf19 co-IP and Ctf19/Mcm21 centromeric localization, while Ame1/outer-kinetochore localization persists. This supports the inherited minor condition-scoped formation/association curation gap, not a blanket inference from UNKNOWN, viability, or all-species necessity. Original DeWulf sec4 body evidence remains historical and was not freshly re-read after blocked routes.

### micro-F3: Ground Ctf18, Dcc1 and Ctf8 with exact families

minor / open / confirmed; issue key: ctf18-rfc-exact-family-subset.

Current family entries IPR053016, IPR019128 and IPR018607 identify Ctf18, Dcc1 and Ctf8. Their rows remain REVIEWED_LABEL_ONLY. The shared IPR050238 family and AAA/RFC domains are insufficient to distinguish the four small RFC paralogues. CTF18 family identity is separately checked from its unchecked generated description. Native P49956 currently lacks the IPR053016 xref; the exact Ctf18 class is independently supported by the named family/signature and five reviewed ortholog members, not a fabricated P49956 mapping. No sequence alignment or universal RFC2–5 family absence is claimed.

### plaque-t0-F1: Ground the eight named COG subunit classes

minor / open / confirmed; issue key: cog-exact-subunit-families.

Current exact whole-protein families are Cog1 IPR033370, Cog2 IPR009316, Cog3 IPR007265, Cog4 IPR048682, Cog5 IPR019465, Cog6 IPR010490, Cog7 IPR019335 and Cog8 IPR007255. All remain REVIEWED_LABEL_ONLY. Historical deferred grounding is understandable, but the exact class authorities now resolve it. Generic component identity must not be confused with automatic sequence annotation of every yeast example.

### plaque-t2-F1: Correct the RET1 single-hit evidence note

minor / open / confirmed; issue key: copi.ret1_reviewed_query_ambiguity.

The selected P53622 coatomer alpha accession and primary symbol COP1 are correct. Its current evidence note says it is the single reviewed entry for RET1 in S288C. The retained exact native query returns both P53622 (COP1, alias RET1) and P22276 (polymerase subunit RET1), so uniqueness cannot be used as the selection rationale.

### plaque-t3-F1: Resolve the exact SAR1 family grounding

minor / open / confirmed; issue key: copii.exact_sar1_family.

The Sar1-family protein component remains REVIEWED_LABEL_ONLY, although native IPR006687 exactly represents the source-neutral SAR1-type family and is cross-referenced by the verified yeast P20606 example. This current mapping gap is distinct from the historical statement that an earlier pass did not curate it.

### plaque-t7-F1: Resolve two exact CORVET core-protein families

minor / open / confirmed; issue key: corvet.exact_vps11_vps16_families.

Vps11/Pep5 and Vps16 remain REVIEWED_LABEL_ONLY even though native whole-protein families IPR016528 and IPR016534 match those declared classes and their reviewed yeast examples. Shared membership in HOPS does not invalidate their protein-family identity. The broader Vps3/Vps39, Vps8/Vps41, Sec1 and domain-level Vps18 candidates are explicitly excluded from this finding.

### septin-core_tfiih_complex_portion_of_holo_tfiih_complex-F1: Use the verified exact TFIIH core subunit families

minor / open / confirmed; issue key: core_tfiih_complex_portion_of_holo_tfiih_complex-exact-subunit-families.

All seven protein rows are REVIEWED_LABEL_ONLY because exact source-neutral mappings were not curated. Native InterPro now positively verifies the matching full-protein families, and the reviewed example xrefs corroborate each identity: Ssl2/XPB IPR001161, Tfb1/p62 IPR027079, Tfb2/p52 IPR004598, Ssl1/p44 IPR012170, Tfb4/p34 IPR004600, Tfb5/p8 IPR009400, Rad3/XPD IPR001945. This is an available exact-mapping gap, not a proposal to ground subunits to broad domains or to equate Rad3 with the separate Rad2 partner. Fresh exact native identities and source observations independently confirm this inherited finding. Preserve dated discussion history; no historical search dishonesty or unavailable-source refutation is alleged.

### septin-core_tfiih_complex_portion_of_nef3_complex-F1: Use the verified exact TFIIH core subunit families

minor / open / confirmed; issue key: core_tfiih_complex_portion_of_nef3_complex-exact-subunit-families.

All seven protein rows are REVIEWED_LABEL_ONLY because exact source-neutral mappings were not curated. Native InterPro now positively verifies the matching full-protein families, and the reviewed example xrefs corroborate each identity: Ssl2/XPB IPR001161, Tfb1/p62 IPR027079, Tfb2/p52 IPR004598, Ssl1/p44 IPR012170, Tfb4/p34 IPR004600, Tfb5/p8 IPR009400, Rad3/XPD IPR001945. This is an available exact-mapping gap, not a proposal to ground subunits to broad domains or to equate Rad3 with the separate Rad2 partner. Fresh exact native identities and source observations independently confirm this inherited finding. Preserve dated discussion history; no historical search dishonesty or unavailable-source refutation is alleged.

### septin-crl4wdr1_ubiquitin_ligase_complex-F1: Remove or replace the unrelated WDR1 protein example

major / open / confirmed; issue key: crl4wdr1-wrong-receptor-example.

The WDR1 protein_examples row assigns Q582R9/Tb927.3.4660 to WDR1. Hu2017 sec004 explicitly defines WDR1 as Tb927.10.15080. The current native Q582R9 entry and exact-locus query identify the different locus and supply no WDR1 synonym. A zero-result query for the source locus cannot justify selecting another WD-repeat protein. The false correspondence can propagate incorrect receptor identity despite the native identifier validator passing. Fresh exact native identities and source observations independently confirm this inherited finding. Preserve dated discussion history; no historical search dishonesty or unavailable-source refutation is alleged.

## Recommended Actions And Acceptance Checks

### micro-A1

In separately authorized record curation, add the exact Mcm21/CENP-O family mapping IPR018464 and preserve separate current uncertainty for the other three whole-protein families.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Preserve dated curation history, discussions.rationale and posed_date; update current notes/prompt only as supported, appending rather than replacing provenance.
- This PR edits no record. Retain host, method and access-tier limits; identifier/family identity, localization, membership, assembly and function are distinct claims.

### micro-A2

In separately authorized record curation, add the exact native Okp1Δ325–337/Ctf19 co-IP and Ctf19-Mcm21 localization context from Schmitzberger2017, retaining observed Ame1/outer-kinetochore persistence and culture conditions. Qualify formation/association interpretation; do not force universal ESSENTIAL, equate it with viability or mandate new experiments. Reinspect DeWulf full body before newly asserting its allele/temperature details.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Preserve dated curation history, discussions.rationale and posed_date; update current notes/prompt only as supported, appending rather than replacing provenance.
- This PR edits no record. Retain host, method and access-tier limits; identifier/family identity, localization, membership, assembly and function are distinct claims.

### micro-A3

In separately authorized record curation, curate the three exact class mappings and narrow the open family TODO to remaining unresolved paralogue identities. Retain the correct examples and avoid treating family annotation or generated prose as evidence of biological membership.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Preserve dated curation history, discussions.rationale and posed_date; update current notes/prompt only as supported, appending rather than replacing provenance.
- This PR edits no record. Retain host, method and access-tier limits; identifier/family identity, localization, membership, assembly and function are distinct claims.
- Distinguish exact Ctf18 class identity from absent current P49956 xref; exclude unchecked generated description from biological support and do not force shared clamp-loader domains onto RFC2–5.

### plaque-t0-A1

Curate the eight exact class mappings after confirming the generic ortholog-class scope; retain the correct yeast examples and separately sourced memberships. Reconcile the family TODO and document that Cog1/2/7 class grounding is not a new sequence annotation of the reference examples.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Preserve dated append-only rationale/history; append current evidence and update active notes/status as appropriate. Record curation remains outside this review-only PR.

### plaque-t2-A1

Keep P53622 and COP1 with the RET1 alias; replace the uniqueness claim with explicit disambiguation against polymerase P22276. Preserve dated retrieval history.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated append-only rationale/history; append current evidence and update active notes/status as appropriate. Record curation remains outside this review-only PR.

### plaque-t3-A1

Ground the Sar1 component to InterPro:IPR006687 and synchronize current grounding status/notes and any linked node consistently. Preserve its component ID, UNKNOWN necessity, and the distinct unresolved heteromeric subcomplex boundaries.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated append-only rationale/history; append current evidence and update active notes/status as appropriate. Record curation remains outside this review-only PR.

### plaque-t7-A1

Map Vps11/Pep5 to InterPro:IPR016528 and Vps16 to InterPro:IPR016534; synchronize current label-only notes/status and linked nodes while preserving IDs, UNKNOWN necessity and the bounded unresolved classes.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.
- Preserve dated append-only rationale/history; append current evidence and update active notes/status as appropriate. Record curation remains outside this review-only PR.

### septin-core_tfiih_complex_portion_of_holo_tfiih_complex-A1

Map the seven existing subunit rows to their verified exact InterPro families; update current grounding status/notes and TODO while preserving component IDs, genes, protein examples, UNKNOWN essentiality and context-specific containing-complex boundaries. Record curation stays outside this review-only PR. Preserve dated rationale/history; update current notes/prompts or append clarification.

- Confirm each family type, exact subunit scope and native example xref; distinguish RAD3/XPD from the unrelated XPG/Rad2 background prose.
- Do not replace full-family mappings with generic helicase, zinc-finger or domain terms.
- Retain TFIIK or Rad2 as partners outside this seven-subunit core portion.
- Pass applicable schema, strict, identifier, native protein and graph checks.
- Use separately authorized guarded record curation with required append-only record/repository history; preserve source-strain, assay and UNKNOWN formation limits.

### septin-core_tfiih_complex_portion_of_nef3_complex-A1

Map the seven existing subunit rows to their verified exact InterPro families; update current grounding status/notes and TODO while preserving component IDs, genes, protein examples, UNKNOWN essentiality and context-specific containing-complex boundaries. Record curation stays outside this review-only PR. Preserve dated rationale/history; update current notes/prompts or append clarification.

- Confirm each family type, exact subunit scope and native example xref; distinguish RAD3/XPD from the unrelated XPG/Rad2 background prose.
- Do not replace full-family mappings with generic helicase, zinc-finger or domain terms.
- Retain TFIIK or Rad2 as partners outside this seven-subunit core portion.
- Pass applicable schema, strict, identifier, native protein and graph checks.
- Use separately authorized guarded record curation with required append-only record/repository history; preserve source-strain, assay and UNKNOWN formation limits.

### septin-crl4wdr1_ubiquitin_ligase_complex-A1

Remove Q582R9 from the WDR1 example unless independent exact-locus/sequence evidence establishes an identity merger; otherwise replace only with a verified source-locus accession. Preserve Q57XW2 and Q586I3 as reference-strain examples, accurately call their identifiers ORF names, and reconcile stale no-examples discussion text. Do not guess a replacement or change the supported source-defined complex. Record curation stays outside this review-only PR. Preserve dated rationale/history; update current notes/prompts or append clarification.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.
- Use separately authorized guarded record curation with required append-only record/repository history; preserve source-strain, assay and UNKNOWN formation limits.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/other/cog_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac; current SHA256 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261022T051656Z-cog-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/other/coma_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 d27210c22f2b06eb9eb3d5e8aa3ed93f6bf561ac07ae48ae295b11bf39f561da; current SHA256 12d58998e16ab86e55d0c70e47de8fd7cf3a797e528ede3cc99bbff4e8854da5. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261022T051657Z-coma-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/other/copi_vesicle_coat.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195; current SHA256 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/other/copii_vesicle_coat.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2; current SHA256 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/other/core_primosome_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac; current SHA256 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261022T051659Z-core-primosome-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5; current SHA256 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009; current SHA256 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/other/corvet_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0; current SHA256 a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261022T051701Z-corvet-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4; current SHA256 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/other/ctf18_rfc_like_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3; current SHA256 abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261022T051703Z-ctf18-rfc-like-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| micro-record-0 | data/structures/other/coma_complex.yaml; Entire maintained YAML at source e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Complete identity, hierarchy, examples, component evidence, taxonomy, functions, graph, historical discussions and curation events read. No maintained image or quantitative measurement asserted. |
| micro-prior-0 | reviews/structured/20261022T051657Z-coma-complex-audit/review.yaml; Entire immutable original YAML and native-derived Markdown | supports | Original assessments/findings/actions, source tiers and limitations, formal applicability check, historical global checks and frozen inputs reviewed. Historical body readings and old command dates are not silently asserted as current reads/runs. |
| micro-delta-0 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/1-stale.diff; Original frozen target revision to current main base | supports | COMA alone changes: dated history and four component_ref nodes with constituent contributes_to edges. Core primosome and Ctf18 RFC-like remain byte-identical. Current source-scoped reassessment is substantive. |
| micro-record-1 | data/structures/other/core_primosome_complex.yaml; Entire maintained YAML at source e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Complete identity, hierarchy, examples, component evidence, taxonomy, functions, graph, historical discussions and curation events read. No maintained image or quantitative measurement asserted. |
| micro-prior-1 | reviews/structured/20261022T051659Z-core-primosome-complex-audit/review.yaml; Entire immutable original YAML and native-derived Markdown | supports | Original assessments/findings/actions, source tiers and limitations, formal applicability check, historical global checks and frozen inputs reviewed. Historical body readings and old command dates are not silently asserted as current reads/runs. |
| micro-delta-1 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/4-stale.diff; Original frozen target revision to current main base | supports | COMA alone changes: dated history and four component_ref nodes with constituent contributes_to edges. Core primosome and Ctf18 RFC-like remain byte-identical. Current source-scoped reassessment is substantive. |
| micro-record-2 | data/structures/other/ctf18_rfc_like_complex.yaml; Entire maintained YAML at source e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Complete identity, hierarchy, examples, component evidence, taxonomy, functions, graph, historical discussions and curation events read. No maintained image or quantitative measurement asserted. |
| micro-prior-2 | reviews/structured/20261022T051703Z-ctf18-rfc-like-complex-audit/review.yaml; Entire immutable original YAML and native-derived Markdown | supports | Original assessments/findings/actions, source tiers and limitations, formal applicability check, historical global checks and frozen inputs reviewed. Historical body readings and old command dates are not silently asserted as current reads/runs. |
| micro-delta-2 | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/9-stale.diff; Original frozen target revision to current main base | supports | COMA alone changes: dated history and four component_ref nodes with constituent contributes_to edges. Core primosome and Ctf18 RFC-like remain byte-identical. Current source-scoped reassessment is substantive. |
| micro-policy | docs/CURATION.md; Components exact class/family identity and formation essentiality; Discussions append-only rationale/posed_date | supports | REVIEWED_LABEL_ONLY requires no exact term; taxon-specific examples differ from class grounding. Formation differs from viability/function. Preserve rationale/posed_date and dated history; current notes/prompt can be narrowed after evidence-backed curation. |
| micro-schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding_status/essentiality; taxonomic presence; graph actors and scopes | supports | Exact grounding, qualitative COMMON, generic protein families/classes, and functional/nonmechanistic outlines retain native meanings. UNKNOWN does not itself require invented experiments; concrete direct physical-association evidence can justify a bounded curation gap. |
| micro-native-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks plus current config/profile/output contract | supports | Positive named protein/pathway assertions trigger applicability, even without an expression claim. Actual catalogue host coverage and matched gene/module context are bounded; expression is not assembly evidence. Seventeen common inputs are identical to previously read bytes; applicable route/profile/config/checklist and component/discussion rules freshly reread. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Nonmechanistic functional and assembly outlines; component_ref and source-specific edge evidence | supports | Constituent contributions and broad functional context need not invent atomic interactions or universal necessity; grouped nodes and reference xrefs are permitted when scope is explicit. |
| micro-original-audit | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/original-audit.json; Six actual native validate/render commands, 41 historical inputs, six original files | supports | All three original YAMLs validate; each Markdown is byte-exact native render. All41 historical inputs match their frozen revisions; six assigned original artifacts match original PR commit. |
| micro-up-P0ABS5 | https://rest.uniprot.org/uniprotkb/P0ABS5.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P0ABS5.raw | supports | P0ABS5: UniProtKB reviewed (Swiss-Prot); DNA primase; genes ['dnaG']; loci ['b3066', 'JW3038']; taxon 83333; InterPro ['IPR016136', 'IPR037068', 'IPR019475', 'IPR006295', 'IPR013173', 'IPR036977', 'IPR030846', 'IPR013264', 'IPR050219', 'IPR034151', 'IPR006171', 'IPR002694']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P0ACB0 | https://rest.uniprot.org/uniprotkb/P0ACB0.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P0ACB0.raw | supports | P0ACB0: UniProtKB reviewed (Swiss-Prot); Replicative DNA helicase DnaB; genes ['dnaB']; loci ['b4052', 'JW4012']; taxon 83333; InterPro ['IPR003593', 'IPR036185', 'IPR007692', 'IPR007694', 'IPR007693', 'IPR016136', 'IPR027417']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P25559 | https://rest.uniprot.org/uniprotkb/P25559.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P25559.raw | supports | P25559: UniProtKB reviewed (Swiss-Prot); Sister chromatid cohesion protein DCC1; genes ['DCC1']; loci ['YCL016C', 'YCL16C']; taxon 559292; InterPro ['IPR019128']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P33895 | https://rest.uniprot.org/uniprotkb/P33895.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P33895.raw | supports | P33895: UniProtKB reviewed (Swiss-Prot); Kinetochore protein NUF2; genes ['NUF2']; loci ['YOL069W']; taxon 559292; InterPro ['IPR005549', 'IPR038275']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P36012 | https://rest.uniprot.org/uniprotkb/P36012.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P36012.raw | supports | P36012: UniProtKB reviewed (Swiss-Prot); Histone H3-like centromeric protein CSE4; genes ['CSE4']; loci ['YKL049C', 'YKL262']; taxon 559292; InterPro ['IPR007125', 'IPR009072', 'IPR000164']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P38251 | https://rest.uniprot.org/uniprotkb/P38251.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38251.raw | supports | P38251: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit 5; genes ['RFC5']; loci ['YBR087W', 'YBR0810']; taxon 559292; InterPro ['IPR003593', 'IPR008921', 'IPR050238', 'IPR027417']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P38313 | https://rest.uniprot.org/uniprotkb/P38313.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38313.raw | supports | P38313: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit AME1; genes ['AME1']; loci ['YBR211C', 'YBR1458']; taxon 559292; InterPro ['IPR048743']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P38629 | https://rest.uniprot.org/uniprotkb/P38629.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38629.raw | supports | P38629: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit 3; genes ['RFC3']; loci ['YNL290W', 'N0533']; taxon 559292; InterPro ['IPR003593', 'IPR003959', 'IPR008921', 'IPR050238', 'IPR027417', 'IPR013748']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P38877 | https://rest.uniprot.org/uniprotkb/P38877.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38877.raw | supports | P38877: UniProtKB reviewed (Swiss-Prot); Chromosome transmission fidelity protein 8; genes ['CTF8']; loci ['YHR191C']; taxon 559292; InterPro ['IPR018607']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P40339 | https://rest.uniprot.org/uniprotkb/P40339.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P40339.raw | supports | P40339: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit 4; genes ['RFC4']; loci ['YOL094C', 'O0923']; taxon 559292; InterPro ['IPR003593', 'IPR003959', 'IPR008921', 'IPR050238', 'IPR027417', 'IPR013748', 'IPR047854']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P40348 | https://rest.uniprot.org/uniprotkb/P40348.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P40348.raw | supports | P40348: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit 2; genes ['RFC2']; loci ['YJR068W', 'J1808']; taxon 559292; InterPro ['IPR003593', 'IPR003959', 'IPR008921', 'IPR050238', 'IPR027417', 'IPR013748', 'IPR047854']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P40460 | https://rest.uniprot.org/uniprotkb/P40460.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P40460.raw | supports | P40460: UniProtKB reviewed (Swiss-Prot); Kinetochore protein NDC80; genes ['NDC80']; loci ['YIL144W']; taxon 559292; InterPro ['IPR040967', 'IPR005550', 'IPR055260', 'IPR038273']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P49956 | https://rest.uniprot.org/uniprotkb/P49956.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P49956.raw | supports | P49956: UniProtKB reviewed (Swiss-Prot); Chromosome transmission fidelity protein 18; genes ['CTF18']; loci ['YMR078C', 'YM9582.03C']; taxon 559292; InterPro ['IPR003593', 'IPR003959', 'IPR027417', 'IPR047854']. P49956 does not currently carry IPR053016; exact Ctf18 class metadata and reviewed ortholog membership are separately inspected, without asserting a nonexistent accession xref. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-P53298 | https://rest.uniprot.org/uniprotkb/P53298.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P53298.raw | supports | P53298: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit OKP1; genes ['OKP1']; loci ['YGR179C']; taxon 559292; InterPro []. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-Q02732 | https://rest.uniprot.org/uniprotkb/Q02732.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-Q02732.raw | supports | Q02732: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit CTF19; genes ['CTF19']; loci ['YPL018W', 'LPB13W']; taxon 559292; InterPro ['IPR063954', 'IPR063963']. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-Q04477 | https://rest.uniprot.org/uniprotkb/Q04477.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-Q04477.raw | supports | Q04477: UniProtKB reviewed (Swiss-Prot); Kinetochore protein SPC24; genes ['SPC24']; loci ['YMR117C', 'YM9718.16C']; taxon 559292; InterPro ['IPR013252', 'IPR038066']. Spc24 is the centromere-facing end of the outer Ndc80 attachment module; the grouped node does not assert every listed member directly contacts microtubules. Native annotations are distinct from newly inspected primary experiments. |
| micro-up-Q06675 | https://rest.uniprot.org/uniprotkb/Q06675.json; Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-Q06675.raw | supports | Q06675: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit MCM21; genes ['MCM21']; loci ['YDR318W']; taxon 559292; InterPro ['IPR018464']. Native annotations are distinct from newly inspected primary experiments. |
| micro-query-AME1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAME1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-AME1.raw | supports | Current response contains 1 accession(s): ['P38313']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-CTF18 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF18+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-CTF18.raw | supports | Current response contains 1 accession(s): ['P49956']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-CTF19 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF19+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-CTF19.raw | supports | Current response contains 1 accession(s): ['Q02732']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-CTF8 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF8+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-CTF8.raw | supports | Current response contains 1 accession(s): ['P38877']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-DCC1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADCC1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-DCC1.raw | supports | Current response contains 1 accession(s): ['P25559']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-MCM21 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMCM21+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-MCM21.raw | supports | Current response contains 1 accession(s): ['Q06675']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-OKP1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AOKP1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-OKP1.raw | supports | Current response contains 1 accession(s): ['P53298']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-RFC2 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC2.raw | supports | Current response contains 1 accession(s): ['P40348']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-RFC3 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC3+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC3.raw | supports | Current response contains 1 accession(s): ['P38629']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-RFC4 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC4+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC4.raw | supports | Current response contains 1 accession(s): ['P40339']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-RFC5 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC5+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC5.raw | supports | Current response contains 1 accession(s): ['P38251']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-dnaB | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaB+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-dnaB.raw | supports | Current response contains 1 accession(s): ['P0ACB0']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-query-dnaG | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaG+AND+organism_id%3A83333+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Exact reviewed primary-gene/taxon query and complete returned identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-dnaG.raw | supports | Current response contains 1 accession(s): ['P0ABS5']. All13 own exact gene queries are singletons; this is a current bounded identity check, not proof of historical query results or causal membership. |
| micro-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; Exact taxon ID, scientific name, rank and immediate parent; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-4932.raw | supports | Native taxon 4932 is Saccharomyces cerevisiae; rank species; parent {"scientificName": "Saccharomyces", "taxonId": 4930}. Protein reference strains are not silently substituted for every experiment organism. |
| micro-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; Exact taxon ID, scientific name, rank and immediate parent; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-559292.raw | supports | Native taxon 559292 is Saccharomyces cerevisiae (strain ATCC 204508 / S288c); rank strain; parent {"scientificName": "Saccharomyces cerevisiae", "commonName": "Baker's yeast", "taxonId": 4932}. Protein reference strains are not silently substituted for every experiment organism. |
| micro-tax-562 | https://rest.uniprot.org/taxonomy/562.json; Exact taxon ID, scientific name, rank and immediate parent; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-562.raw | supports | Native taxon 562 is Escherichia coli; rank species; parent {"scientificName": "Escherichia", "taxonId": 561}. Protein reference strains are not silently substituted for every experiment organism. |
| micro-tax-83333 | https://rest.uniprot.org/taxonomy/83333.json; Exact taxon ID, scientific name, rank and immediate parent; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-83333.raw | supports | Native taxon 83333 is Escherichia coli (strain K12); rank strain; parent {"scientificName": "Escherichia coli", "taxonId": 562}. Protein reference strains are not silently substituted for every experiment organism. |
| micro-go-0000228 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0000228.raw | supports | Native requested term metadata inspected: [{"id": "GO:0000228", "name": "nuclear chromosome", "isObsolete": false, "definition": {"text": "A chromosome that encodes the nuclear genome and is found in the nucleus of a eukaryotic cell during the cell cycle phases when the nucleus is intact."}, "synonyms": [{"name": "nuclear interphase chromosome", "type": "narrow"}], "relevant_children": [{"id": "GO:0000817", "relation": "part_of"}]}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0000776 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0000776.raw | supports | Native requested term metadata inspected: [{"id": "GO:0000776", "name": "kinetochore", "isObsolete": false, "definition": {"text": "A multisubunit complex that is located at the centromeric region of DNA and provides an attachment point for the spindle microtubules."}, "synonyms": [{"name": "condensed chromosome kinetochore", "type": "exact"}, {"name": "condensed nuclear chromosome kinetochore", "type": "exact"}, {"name": "NMS complex", "type": "narrow"}], "relevant_children": [{"id": "GO:0000817", "relation": "part_of"}]}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0000817 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000817; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0000817.raw | supports | Native requested term metadata inspected: [{"id": "GO:0000817", "name": "COMA complex", "isObsolete": false, "definition": {"text": "A kinetochore multiprotein complex that bridges the subunits that are in contact with centromeric DNA and the subunits bound to microtubules during kinetochore assembly. In yeast, consists of Ctf19p, Okp1p, Mcm21p, and Ame1p.", "xrefs": [{"dbCode": "PMID", "dbId": "14633972"}]}, "synonyms": [{"name": "Ctf19p-Okp1p-Mcm1p-Ame1p complex", "type": "exact"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0003689 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003689; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0003689.raw | supports | Native requested term metadata inspected: [{"id": "GO:0003689", "name": "DNA clamp loader activity", "isObsolete": false, "definition": {"text": "Facilitating the opening of the ring structure of the PCNA complex, or any of the related sliding clamp complexes, and their closing around the DNA duplex, driven by ATP hydrolysis.", "xrefs": [{"dbCode": "PMID", "dbId": "16082778"}]}, "synonyms": [{"name": "DNA clamp loading ATPase activity", "type": "exact"}, {"name": "DNA-protein loading ATPase activity", "type": "related"}, {"name": "PCNA loading activity", "type": "narrow"}, {"name": "PCNA loading complex activity", "type": "narrow"}, {"name": "protein-DNA loading ATPase activity", "type": "related"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0006269 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006269; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0006269.raw | supports | Native requested term metadata inspected: [{"id": "GO:0006269", "name": "DNA replication, synthesis of primer", "isObsolete": false, "definition": {"text": "The synthesis of a short nucleotide polymer using one strand of unwound DNA as a template. The product is usually a RNA molecule between 4-15 nucleotides long that provides a free 3'-OH that can be extended by DNA-directed DNA polymerases. In certain conditions, for example in response to DNA damage, some primases synthesize a DNA primer.", "xrefs": [{"dbCode": "PMID", "dbId": "11395402"}, {"dbCode": "PMID", "dbId": "38203225"}, {"dbCode": "PMID", "dbId": "38492718"}]}, "synonyms": [{"name": "DNA priming", "type": "narrow"}, {"name": "DNA replication, synthesis of DNA primer", "type": "narrow"}, {"name": "DNA replication, synthesis of RNA primer", "type": "narrow"}, {"name": "replication priming", "type": "related"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0007062 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0007062; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0007062.raw | supports | Native requested term metadata inspected: [{"id": "GO:0007062", "name": "sister chromatid cohesion", "isObsolete": false, "definition": {"text": "The cell cycle process in which the sister chromatids of a replicated chromosome become tethered to each other.", "xrefs": [{"dbCode": "ISBN", "dbId": "0815316194"}]}, "synonyms": [{"name": "cohesion-mediated DNA tethering", "type": "exact"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0031390 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031390; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0031390.raw | supports | Native requested term metadata inspected: [{"id": "GO:0031390", "name": "Ctf18 RFC-like complex", "isObsolete": false, "definition": {"text": "A heptameric complex related to replication factor C, which loads the DNA polymerase processivity factor proliferating cell nuclear antigen (PCNA) onto DNA and plays a vital role in chromosome cohesion. In Saccharomyces the subunits are known as Ctf18p, Rfc2p, Rfc3p, Rfc4p, Rfc5p, Dcc1p, and Ctf8p.", "xrefs": [{"dbCode": "PMID", "dbId": "14614842"}]}, "synonyms": [{"name": "Ctf18-RFC", "type": "exact"}, {"name": "Ctf18-RLC", "type": "exact"}, {"name": "RFC (Ctf18)", "type": "exact"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-0140513 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140513; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0140513.raw | supports | Native requested term metadata inspected: [{"id": "GO:0140513", "name": "nuclear protein-containing complex", "isObsolete": false, "definition": {"text": "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together in the nucleus."}, "synonyms": [{"name": "nuclear complex", "type": "exact"}], "relevant_children": [{"id": "GO:0031390", "relation": "is_a"}, {"id": "GO:0000817", "relation": "is_a"}]}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-1990077 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990077; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990077.raw | supports | Native requested term metadata inspected: [{"id": "GO:1990077", "name": "primosome complex", "isObsolete": false, "definition": {"text": "Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart.", "xrefs": [{"dbCode": "PMID", "dbId": "21856207"}]}, "synonyms": [{"name": "primosome", "type": "exact"}], "relevant_children": [{"id": "GO:1990098", "relation": "is_a"}]}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-1990098 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990098; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990098.raw | supports | Native requested term metadata inspected: [{"id": "GO:1990098", "name": "core primosome complex", "isObsolete": false, "definition": {"text": "A protein-DNA complex containing at least one DNA helicase and one primase. Can also contain associated proteins. The helicase component continues to unwind the double-stranded DNA (dsDNA) and the primase component synthesizes a RNA primer during initiation or restart of replication.", "xrefs": [{"dbCode": "PMID", "dbId": "21856207"}]}, "synonyms": [{"name": "core primosome", "type": "exact"}], "relevant_children": [{"id": "GO:1990156", "relation": "part_of"}]}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-1990099 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990099; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990099.raw | supports | Native requested term metadata inspected: [{"id": "GO:1990099", "name": "pre-primosome complex", "isObsolete": false, "definition": {"text": "Any of the protein-DNA complexes that contain a DNA helicase and associated protein(s) at the origin of replication, and build up to assembling the core primosome. The associated protein(s) chaperone the helicase to the DNA, and assembly of the pre-primosome is essential for the initiation or restart of replication. Pre-primosome complexes lack a primase component.", "xrefs": [{"dbCode": "PMID", "dbId": "18179598"}, {"dbCode": "PMID", "dbId": "20129058"}, {"dbCode": "PMID", "dbId": "8663105"}]}, "synonyms": [{"name": "pre-priming complex", "type": "exact"}, {"name": "pre-primosome", "type": "exact"}, {"name": "preprimosome", "type": "exact"}, {"name": "preprimosome complex", "type": "exact"}, {"name": "pre-replication complex", "type": "related"}, {"name": "prereplication complex", "type": "exact"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-go-1990156 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990156; Active term definition, exact synonyms/comments and relevant typed child links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990156.raw | supports | Native requested term metadata inspected: [{"id": "GO:1990156", "name": "DnaB-DnaG complex", "isObsolete": false, "definition": {"text": "A protein complex containing homohexameric DnaB helicase, and DnaG (a primase). Facilitates the unwinding of double-stranded DNA and the synthesis of RNA primer sequences during DNA replication and repair in Prokaryotes.", "xrefs": [{"dbCode": "PMID", "dbId": "14557266"}]}, "synonyms": [{"name": "DnaB-DnaG primosome complex", "type": "related"}], "relevant_children": []}]. Generic/core versus narrower protein-only complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported into COMA. |
| micro-ipr-IPR018464 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018464/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR018464.raw | supports | Native IPR018464: name {'name': 'Centromere protein O', 'short': 'CENP-O'}; type family; description curation flags [{}]. Full CENP-O family explicitly includes yeast Mcm21 and has the Q06675 xref; exact class candidate. |
| micro-ipr-IPR048743 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048743/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR048743.raw | context_only | Native IPR048743: name {'name': 'Inner kinetochore subunit AME1', 'short': 'AME1'}; type domain; description curation flags [{}]. AME1 is a domain annotation, not automatically an exact whole-protein family. |
| micro-ipr-IPR007692 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR007692.raw | context_only | Native IPR007692: name {'name': 'DNA helicase, DnaB type', 'short': 'DNA_helicase_DnaB'}; type family; description curation flags [{}]. DnaB family is a valid E.coli candidate but narrower than generic replicative helicase. |
| micro-ipr-IPR006295 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006295/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR006295.raw | context_only | Native IPR006295: name {'name': 'DNA primase, DnaG', 'short': 'DNA_primase_DnaG'}; type domain; description curation flags [{}, {}]. DnaG-related domain is not the generic archaeal/eukaryotic/bacterial primase class. |
| micro-ipr-IPR050219 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050219/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR050219.raw | context_only | Native IPR050219: name {'name': 'DnaG Primase', 'short': 'DnaG_primase'}; type family; description curation flags [{}]. DnaG family is narrower than generic DNA primase. Unchecked generated prose, including irrelevant exosome wording, is excluded from biological support. |
| micro-ipr-IPR053016 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR053016/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR053016.raw | supports | Native IPR053016: name {'name': 'Chromosome transmission fidelity protein 18', 'short': 'CTF18'}; type family; description curation flags [{}]. CTF18 family PTHR46765 identity is considered separately from unchecked generated description; generated biological assertions are not evidence. |
| micro-ipr-IPR019128 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019128/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR019128.raw | supports | Native IPR019128: name {'name': 'Sister chromatid cohesion protein Dcc1', 'short': 'Dcc1'}; type family; description curation flags [{}]. Exact Dcc1 or Ctf8 family metadata and current native protein xrefs support class identity. |
| micro-ipr-IPR018607-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018607/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR018607-retry.raw | supports | Native IPR018607: name {'name': 'Chromosome transmission fidelity protein 8', 'short': 'Ctf8'}; type family; description curation flags [{}]. Exact Dcc1 or Ctf8 family metadata and current native protein xrefs support class identity. |
| micro-ipr-IPR050238-retry | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/; Complete native metadata/type/name, integrated signatures and description flags; full description read for scope, generated prose excluded; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR050238-retry.raw | context_only | Native IPR050238: name {'name': 'DNA Replication and Repair Clamp Loader Complex', 'short': 'DNA_Rep/Repair_Clamp_Loader'}; type family; description curation flags [{}]. Shared clamp-loader family does not distinguish RFC2–5 paralogues; unchecked generated prose not used as biological evidence. |
| micro-family-CTF18 | https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR053016+AND+reviewed%3Atrue&amp;format=json&amp;size=100&amp;fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name; All returned exact reviewed member identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/family-CTF18.raw | supports | Five reviewed ortholog entries support the named Ctf18 family identity: [{'accession': 'Q8WVB6', 'name': 'Chromosome transmission fidelity protein 18 homolog', 'taxon': 9606}, {'accession': 'Q8BIW9', 'name': 'Chromosome transmission fidelity protein 18 homolog', 'taxon': 10090}, {'accession': 'Q9USQ1', 'name': 'Chromosome transmission fidelity protein 18', 'taxon': 284812}, {'accession': 'Q8IQ05', 'name': 'Chromosome transmission fidelity protein 18 homolog', 'taxon': 7227}, {'accession': 'Q6NU40', 'name': 'Chromosome transmission fidelity protein 18 homolog', 'taxon': 8355}]. This query does not say P49956 currently carries that xref and does not prove biological assembly. |
| micro-pmid-10323865 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-10323865.raw | supports | MED10323865: A putative protein complex consisting of Ctf19, Mcm21, and Okp1 represents a missing link in the budding yeast kinetochore.; DOI 10.1101/gad.13.9.1140. Complete primary study abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-11389843 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11389843+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-11389843.raw | supports | MED11389843: Identification of RFC(Ctf18p, Ctf8p, Dcc1p): an alternative RFC complex required for sister chromatid cohesion in S. cerevisiae.; DOI 10.1016/s1097-2765(01)00254-4. Complete primary study abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-14562095.raw | supports | MED14562095: Global analysis of protein localization in budding yeast.; DOI 10.1038/nature02026. Complete primary study abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-14614842 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-14614842.raw | supports | MED14614842: Genome stability: a new member of the RFC family.; DOI 10.1016/j.cub.2003.10.048. Complete secondary review abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-14633972 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14633972+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-14633972.raw | supports | MED14633972: Hierarchical assembly of the budding yeast kinetochore from multiple subcomplexes.; DOI 10.1101/gad.1144403. Complete primary study abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-21856207 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21856207+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-21856207.raw | supports | MED21856207: Replication initiation at the Escherichia coli chromosomal origin.; DOI 10.1016/j.cbpa.2011.07.016. Complete secondary review abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-23908374 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23908374+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-23908374.raw | supports | MED23908374: The composition, functions, and regulation of the budding yeast kinetochore.; DOI 10.1534/genetics.112.145276. Complete secondary review abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-pmid-29046335 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=25; Complete MED identity/title/authors/date/DOI and entire deposited abstract; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-29046335.raw | supports | MED29046335: Molecular basis for inner kinetochore configuration through RWD domain-peptide interactions.; DOI 10.15252/embj.201796636. Complete primary study abstract read. No full body is certified by this metadata row; detailed source reading is separately enumerated. |
| micro-schmitzberger2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5709738.1/PMC5709738.1.xml; Genuine JATS abstract/Introduction sec1; Results sec3,4,6,11,12; Discussion sec15,16; Methods sec19,30,31,32; Figures1,2,7,8 text captions. No pixels/EV6 strain table/raw data; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/schmitzberger2017-jats.raw | supports | K.lactis recombinant interface/truncation work is distinct from native S.cerevisiae Okp1Δ325–337 co-IP/localization. Native Ctf19 co-IP and centromeric Ctf19/Mcm21 signals are lost while Ame1/MIND/outer signals remain; near-normal vegetative growth does not erase this physical-association phenotype. Co-IP Methods use30°C cultures; S288C-derived unless specified exceptions in unread EV6. Not a universal viability/assembly claim. |
| micro-kaguni2011-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3189269.1/PMC3189269.1.xml; Genuine secondary review JATS Introduction S1; DnaB S5/DnaC S6; loading S9; initiation checkpoint S10; elongation S11; Conclusions S12. Other sections, pixels and cited primary experiments not read; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/kaguni2011-jats.raw | context_only | Review synthesizes E.coli oriC DnaA-dependent DnaB/DnaC loading, prepriming then DnaG primer formation/DnaC release, and transient repeated DnaG association in elongation. This supports bounded canonical background, not a new experiment, universal generic stoichiometry, or individual component formation necessity. |
| micro-dewulf2003-legacy-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/?_escaped_fragment_=; Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-legacy.raw | context_only | HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete fresh abstract and independent Schmitzberger primary body are separately inspected. |
| micro-dewulf2003-canonical-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/; Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-canonical.raw | context_only | HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete fresh abstract and independent Schmitzberger primary body are separately inspected. |
| micro-dewulf2003-numeric-access | https://pmc.ncbi.nlm.nih.gov/articles/289150/; Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-numeric.raw | context_only | HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete fresh abstract and independent Schmitzberger primary body are separately inspected. |
| micro-dewulf2003-jats-access | https://pmc-oa-opendata.s3.amazonaws.com/PMC289150.1/PMC289150.1.xml; Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-jats.raw | context_only | HTTP404; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete fresh abstract and independent Schmitzberger primary body are separately inspected. |
| micro-dewulf2003-biocc-access | https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC289150/unicode; Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-biocc.raw | context_only | HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete fresh abstract and independent Schmitzberger primary body are separately inspected. |
| micro-dewulf2003-pdf-access | https://genesdev.cshlp.org/content/17/23/2902.full.pdf; Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-pdf.raw | context_only | HTTP403; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete fresh abstract and independent Schmitzberger primary body are separately inspected. |
| micro-catalogue | https://imodulondb.org/api/datasets; Complete official organism/dataset catalogue response; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/catalogue.raw | supports | All20 organism rows inspected. E.coli has precise1k and other named datasets; no S.cerevisiae/yeast matching host occurs in this snapshot. Catalogue no-match is not biological absence; no unrelated bacterial proxy substitutes for COMA/Ctf18. |
| micro-ecoli-meta | https://imodulondb.org/api/datasets/e_coli/precise1k/meta; Complete selected e_coli/precise1k dataset metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-meta.raw | context_only | Selected precise1k includes BW25113,DGF-298,GMOS,MG1655,W3110: five strains,1035 samples,201 modules,4257 genes. K-12 is reference-organism context, not an exact single-strain experiment match; source publication metadata does not imply its full-body reading. |
| micro-ecoli-modules | https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons; Complete selected module list and metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-modules.raw | context_only | All201 module records returned for e_coli/precise1k inspected for bounded dataset/module context; downstream gene results define actual hits, not module-title speculation. |
| micro-ecoli-b4052 | https://imodulondb.org/api/genes/b4052/imodulons?organism=e_coli&amp;dataset=precise1k; Complete201 gene/module membership rows, actual threshold/in_imodulon fields; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-b4052.raw | context_only | b4052/dnaB has no above-threshold membership among returned201 modules. This is computational expression context, not physical association, assembly necessity, localization or causal regulation. |
| micro-ecoli-b3066 | https://imodulondb.org/api/genes/b3066/imodulons?organism=e_coli&amp;dataset=precise1k; Complete201 gene/module membership rows, actual threshold/in_imodulon fields; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-b3066.raw | context_only | b3066/dnaG crosses only module10 Nucleotide Stress (weight0.082144995&gt;threshold0.077432849). This is computational expression context, not physical association, assembly necessity, localization or causal regulation. |
| micro-ecoli-JW4012 | https://imodulondb.org/api/genes/JW4012/imodulons?organism=e_coli&amp;dataset=precise1k; Complete201 gene/module membership rows, actual threshold/in_imodulon fields; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-JW4012.raw | context_only | JW4012 alias request returns no above-threshold membership; alias indexing noncoverage is not gene absence. This is computational expression context, not physical association, assembly necessity, localization or causal regulation. |
| micro-ecoli-JW3038 | https://imodulondb.org/api/genes/JW3038/imodulons?organism=e_coli&amp;dataset=precise1k; Complete201 gene/module membership rows, actual threshold/in_imodulon fields; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-JW3038.raw | context_only | JW3038 alias request returns no above-threshold membership; alias indexing noncoverage is not gene absence. This is computational expression context, not physical association, assembly necessity, localization or causal regulation. |
| micro-ecoli-module-10 | https://imodulondb.org/api/imodulons/e_coli/precise1k/10; Complete scalar metadata,15 member gene IDs/weights and threshold; activity table and generated narrative not used for biological claims; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-module-10.raw | context_only | Module10 Nucleotide Stress has regulator=null, function_description DNA repair/stringent ppGpp response/ribosome biogenesis and stability, threshold0.077432849;15 member genes include b3066 weight0.082144995 and exclude b4052. Generated ai_summary is explicitly excluded from experimental or mechanistic support; no direct primosome assembly conclusion. |
| micro-historical-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual2026-11-03T00:49:00.848907–00:49:00.863225Z invocation; unavailable exit1 permission failure | context_only | Historical runner availability limitation only, not a new run. Current official catalogue and selected matched-host endpoints were freshly inspected as the native fallback. |
| micro-native-coma_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-verify-receipt.json; Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 4 reviewed examples;6 typed nodes:4 COVERED and2 UNANCHORED_WITH_UNIPROT. Diagnostics verify implemented accession/graph-example checks, not family completeness, experimental support or biological formation. |
| micro-native-coma_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-causal-receipt.json; Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-causal.log SHA256 db466080285af73e715169620b9d5b400c92d8e428f3e7dd20065fa3e87865b1 | supports | Actual exit0; 4 reviewed examples;6 typed nodes:4 COVERED and2 UNANCHORED_WITH_UNIPROT. Diagnostics verify implemented accession/graph-example checks, not family completeness, experimental support or biological formation. |
| micro-native-core_primosome_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-verify-receipt.json; Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 2 reviewed examples;2 COVERED typed nodes. Diagnostics verify implemented accession/graph-example checks, not family completeness, experimental support or biological formation. |
| micro-native-core_primosome_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-causal-receipt.json; Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-causal.log SHA256 86c84709c0661d272905360926d4aa86c7b0bd0e6e48bbddb4da91863801c0c1 | supports | Actual exit0; 2 reviewed examples;2 COVERED typed nodes. Diagnostics verify implemented accession/graph-example checks, not family completeness, experimental support or biological formation. |
| micro-native-ctf18_rfc_like_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-verify-receipt.json; Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual exit0; 7 reviewed examples;7 COVERED typed nodes. Diagnostics verify implemented accession/graph-example checks, not family completeness, experimental support or biological formation. |
| micro-native-ctf18_rfc_like_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-causal-receipt.json; Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-causal.log SHA256 b77337cdd5a7bc8793f4ed2e383dc3ecee05ecee0677dc4c1b3314167dd0a613 | supports | Actual exit0; 7 reviewed examples;7 COVERED typed nodes. Diagnostics verify implemented accession/graph-example checks, not family completeness, experimental support or biological formation. |
| plaque-current-0 | data/structures/other/cog_complex.yaml; Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Entire record read, including definition, composition, exact examples/evidence, taxon/canonical scope, graphs, discussions and history. Unchanged from original frozen target bytes. |
| plaque-original-0-yaml | reviews/structured/20261022T051656Z-cog-complex-audit/review.yaml; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-original-0-md | reviews/structured/20261022T051656Z-cog-complex-audit/review.md; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-current-2 | data/structures/other/copi_vesicle_coat.yaml; Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Entire record read, including definition, composition, exact examples/evidence, taxon/canonical scope, graphs, discussions and history. Unchanged from original frozen target bytes. |
| plaque-original-2-yaml | reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.yaml; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-original-2-md | reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.md; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-current-3 | data/structures/other/copii_vesicle_coat.yaml; Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Entire record read, including definition, composition, exact examples/evidence, taxon/canonical scope, graphs, discussions and history. Unchanged from original frozen target bytes. |
| plaque-original-3-yaml | reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.yaml; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-original-3-md | reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.md; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-current-7 | data/structures/other/corvet_complex.yaml; Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | Entire record read, including definition, composition, exact examples/evidence, taxon/canonical scope, graphs, discussions and history. Unchanged from original frozen target bytes. |
| plaque-original-7-yaml | reviews/structured/20261022T051701Z-corvet-complex-audit/review.yaml; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-original-7-md | reviews/structured/20261022T051701Z-corvet-complex-audit/review.md; Complete original pair; native validation/render and original frozen-input proof | supports | Immutable historical review independently reassessed; historical validation is not represented as a current global execution. |
| plaque-policy | docs/CURATION.md; Frozen repository rule read and applied | supports | Exact source-neutral class grounding, UNKNOWN formation necessity, optional examples and append-only historical rationale. |
| plaque-review-skill | .claude/skills/review-yaml-record/SKILL.md; Frozen repository rule read and applied | supports | Named molecular/pathway assertions trigger structured-source coverage assessment even without expression-module claims. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen repository rule read and applied | supports | Native graph types permit proteins, families and complexes under GENE_OR_PROTEIN; external interactors need not be components. |
| plaque-review-schema | schema/record_review.yaml; Frozen repository rule read and applied | supports | Native evidence, assessment, finding, action and predecessor contract. |
| plaque-review-profile | docs/record-review-profile.md; Frozen repository rule read and applied | supports | Issue-bearing explicit batch and immutable review-only scope. |
| plaque-checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen repository rule read and applied | supports | Field-by-field scientific review with bounded evidence and completeness assessment. |
| plaque-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139,GO:0005789,GO:0006890,GO:0010008,GO:0017119,GO:0030120,GO:0030126,GO:0030127,GO:0030134,GO:0030137,GO:0033263,GO:0035964,GO:0048193,GO:0090114,GO:0099023; Complete requested15-term response: id/name/isObsolete/definition/synonyms/typed children; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/go.raw | supports | Fifteen active GO identities, definitions and exact typed child relationships inspected. Exact COG/CORVET tethering and COPI/COPII coat identities, coat-versus-vesicle distinction and bounded transport/budding function match. No direct edge inferred from a transitive ancestor response. |
| plaque-tax-4932 | https://rest.uniprot.org/taxonomy/4932.json; Complete scientific name, taxon ID, rank and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/tax-4932.raw | supports | Native Saccharomyces cerevisiae species/reference S288C strain and lineage checked. Paper laboratory/recombinant strains are not silently replaced by S288C. |
| plaque-tax-559292 | https://rest.uniprot.org/taxonomy/559292.json; Complete scientific name, taxon ID, rank and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/tax-559292.raw | supports | Native Saccharomyces cerevisiae species/reference S288C strain and lineage checked. Paper laboratory/recombinant strains are not silently replaced by S288C. |
| plaque-protein-P11076 | https://rest.uniprot.org/uniprotkb/P11076.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P11076.raw | supports | P11076 is reviewed strain559292 ADP-ribosylation factor 1. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P12868 | https://rest.uniprot.org/uniprotkb/P12868.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P12868.raw | supports | P12868 is reviewed strain559292 E3 ubiquitin-protein ligase PEP5. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P15303 | https://rest.uniprot.org/uniprotkb/P15303.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P15303.raw | supports | P15303 is reviewed strain559292 Protein transport protein SEC23. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P19146 | https://rest.uniprot.org/uniprotkb/P19146.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P19146.raw | supports | P19146 is reviewed strain559292 ADP-ribosylation factor 2. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P20606 | https://rest.uniprot.org/uniprotkb/P20606.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P20606.raw | supports | P20606 is reviewed strain559292 Small COPII coat GTPase SAR1. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P20795 | https://rest.uniprot.org/uniprotkb/P20795.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P20795.raw | supports | P20795 is reviewed strain559292 Vacuolar protein sorting-associated protein 33. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P23643 | https://rest.uniprot.org/uniprotkb/P23643.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P23643.raw | supports | P23643 is reviewed strain559292 Vacuolar protein sorting-associated protein 3. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P27801 | https://rest.uniprot.org/uniprotkb/P27801.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P27801.raw | supports | P27801 is reviewed strain559292 Vacuolar membrane protein PEP3. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P32074 | https://rest.uniprot.org/uniprotkb/P32074.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P32074.raw | supports | P32074 is reviewed strain559292 Coatomer subunit gamma. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P36017 | https://rest.uniprot.org/uniprotkb/P36017.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P36017.raw | supports | P36017 is reviewed strain559292 Vacuolar protein sorting-associated protein 21. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P38968 | https://rest.uniprot.org/uniprotkb/P38968.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P38968.raw | supports | P38968 is reviewed strain559292 Protein transport protein SEC31. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P39702 | https://rest.uniprot.org/uniprotkb/P39702.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P39702.raw | supports | P39702 is reviewed strain559292 Vacuolar protein sorting-associated protein 8. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P40094 | https://rest.uniprot.org/uniprotkb/P40094.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P40094.raw | supports | P40094 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 3. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P40482 | https://rest.uniprot.org/uniprotkb/P40482.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P40482.raw | supports | P40482 is reviewed strain559292 Protein transport protein SEC24. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P40509 | https://rest.uniprot.org/uniprotkb/P40509.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P40509.raw | supports | P40509 is reviewed strain559292 Coatomer subunit epsilon. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P41810 | https://rest.uniprot.org/uniprotkb/P41810.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P41810.raw | supports | P41810 is reviewed strain559292 Coatomer subunit beta. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P41811 | https://rest.uniprot.org/uniprotkb/P41811.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P41811.raw | supports | P41811 is reviewed strain559292 Coatomer subunit beta'. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P43621 | https://rest.uniprot.org/uniprotkb/P43621.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P43621.raw | supports | P43621 is reviewed strain559292 Coatomer subunit delta. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53079 | https://rest.uniprot.org/uniprotkb/P53079.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53079.raw | supports | P53079 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 1. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53195 | https://rest.uniprot.org/uniprotkb/P53195.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53195.raw | supports | P53195 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 7. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53271 | https://rest.uniprot.org/uniprotkb/P53271.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53271.raw | supports | P53271 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 2. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53600 | https://rest.uniprot.org/uniprotkb/P53600.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53600.raw | supports | P53600 is reviewed strain559292 Coatomer subunit zeta. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53622 | https://rest.uniprot.org/uniprotkb/P53622.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53622.raw | supports | P53622 is reviewed strain559292 Coatomer subunit alpha. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53951 | https://rest.uniprot.org/uniprotkb/P53951.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53951.raw | supports | P53951 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 5. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-P53959 | https://rest.uniprot.org/uniprotkb/P53959.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53959.raw | supports | P53959 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 6. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-Q03308 | https://rest.uniprot.org/uniprotkb/Q03308.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q03308.raw | supports | Q03308 is reviewed strain559292 Vacuolar protein sorting-associated protein 16. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-Q04491 | https://rest.uniprot.org/uniprotkb/Q04491.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q04491.raw | supports | Q04491 is reviewed strain559292 Protein transport protein SEC13. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-Q04632 | https://rest.uniprot.org/uniprotkb/Q04632.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q04632.raw | supports | Q04632 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 8. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-protein-Q06096 | https://rest.uniprot.org/uniprotkb/Q06096.json; Exact accession/status/protein name/genes/organism; relevant full comments and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q06096.raw | supports | Q06096 is reviewed strain559292 Conserved oligomeric Golgi complex subunit 4. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references checked. Identity and annotation do not prove universal necessity or substitute for a primary experiment. |
| plaque-ipr-IPR033370 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033370/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR033370.raw | supports | Current InterPro IPR033370: Conserved oligomeric Golgi complex subunit 1, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR009316 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009316/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR009316.raw | supports | Current InterPro IPR009316: COG complex component, COG2, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-retry-IPR007265 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007265/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR007265.raw | supports | Current InterPro IPR007265: Conserved oligomeric Golgi complex, subunit 3, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-retry-IPR048682 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048682/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR048682.raw | supports | Current InterPro IPR048682: Conserved oligomeric Golgi complex subunit 4, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-retry-IPR019465 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019465/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR019465.raw | supports | Current InterPro IPR019465: Conserved oligomeric Golgi complex subunit 5, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR010490 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010490/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR010490.raw | supports | Current InterPro IPR010490: Conserved oligomeric Golgi complex subunit 6, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR019335 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019335/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR019335.raw | supports | Current InterPro IPR019335: Conserved oligomeric Golgi complex subunit 7, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR007255 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007255/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR007255.raw | supports | Current InterPro IPR007255: Conserved oligomeric Golgi complex subunit 8, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR006687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006687/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR006687.raw | supports | Current InterPro IPR006687: Small GTPase superfamily, SAR1-type, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR016528 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016528/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR016528.raw | supports | Current InterPro IPR016528: Vacuolar protein sorting-associated protein 11, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR016534 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016534/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR016534.raw | supports | Current InterPro IPR016534: Vacuolar protein sorting-associated protein 16, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR032914 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR032914/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR032914.raw | supports | Current InterPro IPR032914: Vam6/VPS39/TRAP1 family, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-retry-IPR045111 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045111/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR045111.raw | supports | Current InterPro IPR045111: Vacuolar protein sorting-associated protein Vps41/Vps8, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-IPR007810 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007810/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR007810.raw | supports | Current InterPro IPR007810: Pep3/Vps18, beta-propeller domain, type domain; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-ipr-retry-IPR001619 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001619/; Complete metadata/name/type/curated description; compared with relevant native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR001619.raw | supports | Current InterPro IPR001619: Sec1-like protein, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary is used. |
| plaque-gene-RET1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All 2 returned results inspected: P22276,P53622; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/gene-RET1.raw | supports | Exact RET1 reviewed559292 query returns P22276 polymerase RET1 and P53622 coatomer COP1 aliasRET1; the selected coatomer accession is correct but not a unique gene-query hit. |
| plaque-family-IPR033370 | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR033370%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All 6 returned results inspected: Q8WTW3,Q9FFF3,Q9VGC3,Q9Z160,Q9UTL1,Q54ZB3; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/family-IPR033370.raw | supports | Bounded reviewed family-member query confirms named generic COG ortholog-class members in other taxa; it does not add an absent whole-family annotation to S288C Cog1/2/7 sequences. |
| plaque-family-IPR009316 | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR009316%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All 7 returned results inspected: Q14746,F4JRR1,Q9VF78,Q21444,Q921L5,O59705,Q54UC2; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/family-IPR009316.raw | supports | Bounded reviewed family-member query confirms named generic COG ortholog-class members in other taxa; it does not add an absent whole-family annotation to S288C Cog1/2/7 sequences. |
| plaque-family-IPR019335 | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR019335%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; All 7 returned results inspected: P83436,Q9FGN0,Q9VAD6,Q3UM29,Q3T1G7,A2VDR8,Q54LC8; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/family-IPR019335.raw | supports | Bounded reviewed family-member query confirms named generic COG ortholog-class members in other taxa; it does not add an absent whole-family annotation to S288C Cog1/2/7 sequences. |
| plaque-paper-0 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2012.01.015%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-0.raw | supports | Yu2012 mixed-species Arf1-coatomer structural recruitment model; full selected body read separately. |
| plaque-paper-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2007.03.006%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-1.raw | supports | Peplowska2007 identifies six-subunit CORVET, shared four-class-C core, Vps3/Vps8 and Vps21 association/endosomal biogenesis; full body unavailable, exact strain/Methods/direct binary mechanics not certified. |
| plaque-paper-2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2F349248a0%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-2.raw | supports | Waters1991 identifies cytosolic coatomer, a large multisubunit nonclathrin coat complex; complete abstract only. |
| plaque-paper-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb.3263%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-3.raw | supports | Ha2016 reports recombinant COG architecture and interlobe flexibility; selected full body independently read. |
| plaque-paper-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M400662200%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-4.raw | supports | Loh/Hong2004 resolves mammalian Cog1/2/7 and notes structural divergence from yeast; not direct yeast localization evidence. |
| plaque-paper-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200202016%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-5.raw | supports | Ungar2002 mammalian eight-subunit COG, Golgi association and architecture; not a yeast experimental assay. |
| plaque-paper-6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200412003%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-6.raw | supports | Zolov2005 HeLa COG3 depletion/COG interactions with COPI and SNARE machinery; interactors are not thereby COG constituents. |
| plaque-paper-7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e02-11-0736%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-7.raw | supports | Sandmann2003 yeast coatomer retrieval, KKXX cargo binding and conditional-mutant suppression; body routes blocked, no detailed Methods certified. |
| plaque-paper-8 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1247%2Fcsf.18014%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-8.raw | supports | Ishii2018 examines yeast COG subcomplexes at membranes and mitochondrial rerouting; selected body read separately. |
| plaque-paper-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2Felife.00951%22&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-9.raw | supports | Zanetti2013 reconstituted COPII membrane coat cryoET architecture; selected full body read separately. |
| plaque-paper-10 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10562277+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-10.raw | supports | VanRheenen1999 Sec34/Cog3 peripheral membrane/tethering complex; primary abstract plus native protein evidence join. |
| plaque-paper-11 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10588657+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-11.raw | supports | Spelbrink1999 Grd20/Cog3 TGN sorting/actin phenotype; primary abstract scope, not universal structure necessity. |
| plaque-paper-12 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10684247+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-12.raw | supports | Rout2000 NPC protein inventory/localization; Sec13 annotation is explicitly NPC localization of a shared protein, not direct COPII membership proof. |
| plaque-paper-13 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10720463+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-13.raw | supports | Matsuoka/Schekman2000 Methods reconstitution of COPII-coated vesicles from liposomes; abstract tier. |
| plaque-paper-14 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10753972+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-14.raw | supports | Peng2000 distinct Sec24/Sfb2/Lst1 cargo-selection coats; generic core description need not inventory every alternative coat. |
| plaque-paper-15 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10944212+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-15.raw | supports | Seals2000 HOPS complex/vacuole fusion; PEP5 vacuole membrane annotation is shared-core HOPS evidence, not direct CORVET localization. |
| plaque-paper-16 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11086000+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-16.raw | supports | Shimoni2000 Lst1 cooperates with Sec23/24 in Pma1 cargo packaging; not obligatory universal extra coat component. |
| plaque-paper-17 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12235121+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-17.raw | supports | Supek2002 Sec16 stabilization/reconstitution scope; no universal in-vivo stoichiometry inference. |
| plaque-paper-18 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-18.raw | supports | Huh2003 global tagged yeast localization abstract; exact ARF2/Sec26/Cog2 joins come from native annotations, not this abstract naming each protein. |
| plaque-paper-19 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15504911+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-19.raw | supports | Gillingham2004 Rud3/Arf1 cis-Golgi interaction and localization; not every Arf paralog experiment. |
| plaque-paper-20 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8004676+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-20.raw | supports | Barlowe1994 COPII coat/vesicle reconstitution from ER and purified components; nucleotide conditions distinguish coat retention/fusion. |
| plaque-paper-21 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8548805+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-21.raw | supports | Bednarek1995 both COPI and COPII budding from yeast ER/nuclear envelopes; this does not erase steady-state coat localization distinctions. |
| plaque-paper-22 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9568718+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-22.raw | supports | Matsuoka1998 sequential Sar1–Sec23/24–Sec13/31 reconstitution with defined liposomes; selected author PDF read separately. |
| plaque-paper-23 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9606204+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=5; Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed primary abstract actually read; no full-body access implied by this row; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-23.raw | supports | VanRheenen1998 Sec35/Cog2 peripheral membrane docking; direct native localization evidence join checked. |
| plaque-yu2012-body | https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml; Genuine PMC S3 JATS; main sections S3–S7,S9,S10,S12,S13 read; no detailed S8/S14–S15 contacts/methods certification, pixels or supplements; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/yu2012-body.raw | supports | Two Arf1 binding sites, biochemical recruitment and a structural membrane-orientation model support coarse COPI association. Mammalian coatomer fragments plus yeast Arf1 form mixed-species recombinant preparations; this is not a native whole yeast coat structure or complete in-vivo hydrolysis cycle. Authors leave physiological GTPase stimulation unresolved. |
| plaque-ha2016-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4972656.1/PMC4972656.1.xml; Genuine PMC S3 JATS; all main prose P2–P14 and Methods S2/S3; no figure pixels or supplementary datasets; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ha2016-s3.raw | supports | Recombinant S.cerevisiae Cog1–8 negative-stain EM supports octamer/two lobes and flexibility; produced in E.coli, with separate Kluyveromyces lobe-B experiments. Cog5/7 positions remain unresolved and deposition may affect flexibility. Yeast viability differences do not establish universal assembly essentiality. |
| plaque-ishii2018-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6116515.1/PMC6116515.1.xml; Genuine PMC S3 JATS; sections S3,S5,S6,S7,S9–S13 including selected Results/Methods/Discussion; no pixels or supplementary strain lists; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ishii2018-s3.raw | supports | YPH499/BY4741 yeast biochemical fractionation/co-IP and ectopic targeting distinguish stable cytosolic octamer from variable membrane subassemblies. Mitochondrial COG recruitment did not establish autonomous stable Golgi-vesicle tethering. |
| plaque-zanetti2013-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3778437.1/PMC3778437.1.xml; Genuine PMC S3 JATS; s1,s2 opening,s2-2 with Fig6/7 text captions,s3-1 sample preparation,s3-2 electron microscopy; no detailed s2-1 processing, pixels or supplements; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/zanetti2013-s3.raw | supports | Reconstituted yeast COPII GUV coat cryoET supports inner/outer layers, but relative layer positions are constrained rather than fixed. Sec13/31 heterotetramer architecture is compatible with paired building-block descriptions; cargo geometry remains model-scoped. |
| plaque-matsuoka1998-pdf | https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf; Genuine Bednarek lab author PDF; extracted text printed pp263,267,269–271,273–274 including sequential binding, morphology/stoichiometry, Fig7 text caption and experimental procedures; RSY445 microsomes/RSY1113 Sec13/31 preparation. Text inspection only, not figure pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/matsuoka1998-pdf.raw | supports | Defined liposomes and yeast ER support sequential Sar1-GTP recruitment of Sec23/24 then Sec13/31, with conventional fixed-sample EM and lumen-retention assays. Synthetic/native coat stoichiometries and size distributions differ; stronger claims about universal ratios or complete physiological assembly are not made. |
| plaque-peplowska2007-doi | https://api.crossref.org/v1/works/10.1016%2Fj.devcel.2007.03.006/transform; Entire bibliographic JSON; no Results/Methods/figure content; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/peplowska2007-doi.raw | context_only | DOI content-negotiation yielded Crossref bibliographic JSON, not a primary full text. Correct title/DOI metadata only. |
| plaque-access-limitations | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/access-limitations.json; Actual failed/access-limited route receipts; genuine fallback bodies separately scoped | context_only | PMC Ha/Ishii/Sandmann surfaces returned recaptcha HTML; Sandmann BioC429 and Peplowska publisher403 provide no body support. Initial Zanetti406 was an access-format result; genuine S3 body later obtained. Five InterPro429 responses were replaced by separately dated successful serial queries. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Complete fresh same-PR official /api/datasets response independently read; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/catalogue.raw | supports | Complete20 organism rows/28 organism-dataset pairs contain bacterial/archaeal hosts, no S.cerevisiae/S288C, Kluyveromyces or mammalian biological host. Experimental E.coli protein production is not a matching biological dataset. |
| plaque-catalogue-bounded-search | https://imodulondb.org/api/datasets; Full returned organism id/name/dataset catalogue independently screened | context_only | No matched biological host in the inspected catalogue; this is coverage only, not absence of the complexes or their regulation. No foreign-host downstream module proxy applies. |
| plaque-original-current-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/originals-current-proof.json; Actual four native validate/render commands;56 historical input occurrences;48 current source/worktree inputs | supports | All original pairs validate and render byte-identically; all historical inputs match their frozen revisions. All48 current inputs match; all four assigned targets are byte-unchanged from historical input. |
| plaque-native-cog_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cog_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source exit0; 8 REVIEWED examples/8 typed nodes; all typed nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-cog_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/cog_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-causal.log SHA256 825ab0ccb55c67c2e97fe7be7a80fd58d197894220e39b25c4fcbfc9941d1dd0 | supports | Actual current-source exit0; 8 REVIEWED examples/8 typed nodes; all typed nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-copi_vesicle_coat-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/copi_vesicle_coat.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source exit0; 9 REVIEWED examples/2 typed nodes; all typed nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-copi_vesicle_coat-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/copi_vesicle_coat.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-causal.log SHA256 62b80549c9d8c2786488904a26b8a4e91d32a624b11000f16ebce03c1fe02395 | supports | Actual current-source exit0; 9 REVIEWED examples/2 typed nodes; all typed nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-copii_vesicle_coat-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/copii_vesicle_coat.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source exit0; 5 REVIEWED examples/3 typed nodes; all typed nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-copii_vesicle_coat-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/copii_vesicle_coat.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-causal.log SHA256 7571c7db8734ce15009e2ddbae753cc8f2630ee35f7d15d5b98f6eab28929f55 | supports | Actual current-source exit0; 5 REVIEWED examples/3 typed nodes; all typed nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-corvet_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-verify-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/corvet_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source exit0; 6 REVIEWED examples/7 typed nodes; six COVERED constituents and one externally anchored Vps21 interactor (UNANCHORED_WITH_UNIPROT), not a missing seventh constituent. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| plaque-native-corvet_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-causal-receipt.json; Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/other/corvet_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-causal.log SHA256 7712e85ade0de1347ea909a9aaf2d0adab299bcdae10f215c03089983bbde0ff | supports | Actual current-source exit0; 6 REVIEWED examples/7 typed nodes; six COVERED constituents and one externally anchored Vps21 interactor (UNANCHORED_WITH_UNIPROT), not a missing seventh constituent. These gates verify identifiers/coverage, not necessity or all scientific mechanisms. |
| septin-review-policy | .claude/skills/review-yaml-record/SKILL.md; Scientific review and structured-source applicability | supports | Actual whole-record molecular/pathway assertions require host/source coverage assessment; lack of expression-module claims is not sufficient exemption. |
| septin-curation-policy | docs/CURATION.md; Components and Discussions | supports | Exact family identity differs from complex-specific role. Family or class is permitted. Dated rationale/history are append-only; optional examples or broad groups alone do not establish defects. |
| septin-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component identity/essentiality and graph fields | supports | Formation essentiality is distinct from functional activity, localization or cellular viability. FUNCTION/NONMECHANISTIC graphs may describe coarse associations without a complete molecular assembly mechanism. |
| septin-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Native accession/name/status/taxon and query rules | supports | Native primary genes versus ORF names and bounded query coverage are distinct from biological source membership, necessity and source-strain equivalence. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Evidence placement and descriptive graph scope | supports | Constituent relationships, perturbation outputs and co-isolation retain experiment scope; graph coverage alone does not establish molecular identity or direct ubiquitination. |
| septin-literature-policy | .claude/skills/literature-evidence/SKILL.md; Source access, image and read extents | supports | Native metadata/abstract, genuine body/captions, pixels and failed responses are separate tiers. Generated authority prose is excluded as independent biological evidence. |
| septin-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000438,GO:0000439,GO:0000440,GO:0005675,GO:0000112,GO:0006289,GO:0080008,GO:0031464,GO:0031465,GO:0043494,GO:0070912,GO:0070913; All12 exact requested terms: complete active identity/name/definition/synonyms and relevant typed child relationships | supports | GO0000438 and GO0000440 are context-specific children of seven-subunit TFIIH core GO0000439, with holoGO0005675 versus NEF3GO0000112 parthood; Rad2 is separate from Rad3. GO0006289 is NER. GO0080008 is broad Cul4-RING; GO0031464/65,GO0043494,GO0070912/13 describe different named complexes and do not replace the source-specific CRL4WDR1 local identity. |
| septin-catalogue | https://imodulondb.org/api/datasets; Complete official returned20-organism catalogue and dataset keys, independently read from peer fresh snapshot | supports | No Saccharomyces/S288C or Trypanosoma/TREU927/Lister427/29-13 dataset is returned. Other listed E.coli datasets are not proxies for eukaryotic assemblies merely because bacteria produce recombinant proteins. No matched downstream gene/module queries apply after this bounded host coverage assessment. Noncoverage is not biological absence; actual peer fetch timestamp retained. |
| septin-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxId/scientificName/rank/lineage/otherNames | supports | Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292; Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish identity of Lister427 or29-13 experimental strains. |
| septin-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxId/scientificName/rank/lineage/otherNames | supports | Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292; Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish identity of Lister427 or29-13 experimental strains. |
| septin-tax5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete ENA taxId/scientificName/rank/lineage/otherNames | supports | Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292; Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish identity of Lister427 or29-13 experimental strains. |
| septin-tax185431 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431; Complete ENA taxId/scientificName/rank/lineage/otherNames | supports | Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292; Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish identity of Lister427 or29-13 experimental strains. |
| septin-protein-Q00578 | https://rest.uniprot.org/uniprotkb/Q00578.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. SSL2 primary; reviewed S288C XPB/Ssl2 core subunit. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-P32776 | https://rest.uniprot.org/uniprotkb/P32776.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. TFB1 primary; reviewed S288C p62. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q02939 | https://rest.uniprot.org/uniprotkb/Q02939.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. TFB2 primary; reviewed S288C p52. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q04673 | https://rest.uniprot.org/uniprotkb/Q04673.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. SSL1 primary; reviewed S288C p44. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q12004 | https://rest.uniprot.org/uniprotkb/Q12004.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. TFB4 primary; reviewed S288C p34. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q3E7C1 | https://rest.uniprot.org/uniprotkb/Q3E7C1.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. TFB5 primary; reviewed S288C p8/TTDA. Native nucleus evidenceHuh14562095 is localization, not by itself a membership or formation test. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-P06839 | https://rest.uniprot.org/uniprotkb/P06839.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. RAD3 primary; reviewed S288C XPD helicase, distinct from Rad2/XPG. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q57XW2 | https://rest.uniprot.org/uniprotkb/Q57XW2.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. Unreviewed TREU927 putative Cullin4B; ORF names Tb03.1J15.620/Tb927.3.1290, not a formal primary CUL4 gene-name field. Matches Hu source locus. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q586I3 | https://rest.uniprot.org/uniprotkb/Q586I3.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. Unreviewed TREU927 DDB1 annotation; ORF names Tb06.30P15.290/Tb927.6.5110. Matches source locus. Automated nucleus annotation is not a new localization experiment. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-protein-Q582R9 | https://rest.uniprot.org/uniprotkb/Q582R9.json; Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR LOCATION,SIMILARITY comments and InterPro xrefs | supports | Native identity inspected. Unreviewed uncharacterized TREU927 protein; ORF names Tb03.48K5.140/Tb927.3.4660. No native WDR1 synonym. WD-repeat domains do not identify source WDR1 Tb927.10.15080. Native annotation is not an independent primary causal or formation assay; no sequence alignment performed. |
| septin-gene-SSL2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASSL2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match Q00578 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-gene-TFB1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match P32776 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-gene-TFB2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match Q02939 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-gene-SSL1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASSL1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match Q04673 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-gene-TFB4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB4%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match Q12004 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-gene-TFB5-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match Q3E7C1 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-gene-RAD3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARAD3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned page and native result identity fields | supports | Complete returned single reviewed match P06839 agrees with declared yeast symbol. This is current bounded coverage, not reconstruction of an October query. |
| septin-rad3-family-members | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR001945%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id; Complete returned page and native result identity fields | supports | All8 returned reviewed member identities read: P18074,Q8W4M7,Q55G81,A6QLJ0,O08811,P06839,P26659,Q60452 are RAD3/XPD homologs. Together with native family name and P06839 xref, this supports IPR001945 despite unrelated XPG/Rad2 prose in its description; no sequence alignment or exhaustive phylogeny. |
| septin-locus-Tb927.3.1290 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.1290+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete returned page and native result identity fields | supports | Complete current exact-locus result Q57XW2. Source Tb927.10.15080 zero-result search does not establish biological absence and cannot justify substitution of Tb927.3.4660/Q582R9. |
| septin-locus-Tb927.6.5110 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.6.5110+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete returned page and native result identity fields | supports | Complete current exact-locus result Q586I3. Source Tb927.10.15080 zero-result search does not establish biological absence and cannot justify substitution of Tb927.3.4660/Q582R9. |
| septin-locus-Tb927.3.4660 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.4660+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete returned page and native result identity fields | supports | Complete current exact-locus result Q582R9. Source Tb927.10.15080 zero-result search does not establish biological absence and cannot justify substitution of Tb927.3.4660/Q582R9. |
| septin-locus-Tb927.10.15080 | https://rest.uniprot.org/uniprotkb/search?query=Tb927.10.15080+AND+organism_id%3A185431&amp;format=json&amp;size=25; Complete returned page and native result identity fields | supports | Complete current exact-locus result is empty. Source Tb927.10.15080 zero-result search does not establish biological absence and cannot justify substitution of Tb927.3.4660/Q582R9. |
| septin-go-name-CRL4WDR1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=CRL4WDR1&amp;limit=25; Complete returned page and native result identity fields | supports | Bounded exact QuickGO name query returns no hit; no exhaustive ontology-wide or biological absence claimed. Source-defined local identity is retained rather than adopting a broader/different complex. |
| septin-go-name-WDR1 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=WDR1&amp;limit=25; Complete returned page and native result identity fields | supports | Bounded exact QuickGO name query returns no hit; no exhaustive ontology-wide or biological absence claimed. Source-defined local identity is retained rather than adopting a broader/different complex. |
| septin-ipr-IPR001161 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001161/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native family name/type, non-LLM description flags, and matching example cross-reference inspected; general family background is not a universal seven-subunit formation assay. |
| septin-ipr-IPR027079 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027079/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native family name/type, non-LLM description flags, and matching example cross-reference inspected; general family background is not a universal seven-subunit formation assay. |
| septin-ipr-IPR004598 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004598/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native family name/type, non-LLM description flags, and matching example cross-reference inspected; general family background is not a universal seven-subunit formation assay. |
| septin-retry-IPR012170 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012170/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native family name/type, non-LLM description flags, and matching example cross-reference inspected; general family background is not a universal seven-subunit formation assay. |
| septin-ipr-IPR004600 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004600/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native family name/type, non-LLM description flags, and matching example cross-reference inspected; general family background is not a universal seven-subunit formation assay. |
| septin-retry-IPR009400 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009400/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native family name/type, non-LLM description flags, and matching example cross-reference inspected; general family background is not a universal seven-subunit formation assay. |
| septin-retry-IPR001945 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001945/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Exact full-protein family identity matches the reviewed yeast example xref, independent of complex-specific role. Native name/type and reviewed members independently identify RAD3/XPD; unrelated XPG/Rad2 description paragraphs are not used to equate the distinct proteins. |
| septin-ipr-IPR045093 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045093/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Broader family scope does not independently identify the exact WDR1-containing complex. Cullin includes multiple paralogs; no exact Cullin4/WDR1 role inferred from the broad family alone. |
| septin-ipr-IPR050358 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050358/; Complete native name/type/hierarchy/member signatures/description-generation flags, description scope and matching UniProt xref | supports | Broader family scope does not independently identify the exact WDR1-containing complex. RSE1/DDB1/CPSF1 label and member signature are broader than DDB1 alone. Top-level is_llm/is_reviewed_llm flags are true despite differing paragraph flags; all generated functional prose is excluded. |
| septin-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED14562095 complete authors/title/year/DOI/PMCID and abstract | supports | Huh2003 complete abstract: global yeast GFP localization; nuclear location does not alone establish TFIIH membership. |
| septin-pmid-14500720 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14500720+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED14500720 complete authors/title/year/DOI/PMCID and abstract | supports | Takagi2003 complete abstract: TFIIK separation/association and transcription context; unread detailed methods/body not certified. |
| septin-pmid-15220919 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15220919+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED15220919 complete authors/title/year/DOI/PMCID and abstract | supports | Ranish2004 complete abstract: Tfb5/TTDA identification and transcription/recruitment context; unread body not certified. |
| septin-pmid-22411836 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22411836+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED22411836 complete authors/title/year/DOI/PMCID and abstract | supports | Murakami2012 complete abstract; genuine body separately scoped. |
| septin-pmid-10915862 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10915862+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED10915862 complete authors/title/year/DOI/PMCID and abstract | supports | Prakash and Prakash2000 SECONDARY review abstract explicitly says Rad2+TFIIH constitute NEF3; not a new primary assembly experiment. |
| septin-prakash2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fs0027-5107%2800%2900037-3%22&amp;format=json&amp;resultType=core; Unique MED10915862 complete authors/title/year/DOI/PMCID and abstract | supports | Exact DOI resolves the same MED10915862 secondary-review abstract, not full text. |
| septin-doi-9 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1006146%22&amp;format=json&amp;resultType=core; Unique MED28052114 complete authors/title/year/DOI/PMCID and abstract | supports | Hu et al2017 primary article metadata/abstract; genuine body separately scoped. |
| septin-doi-3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-025-32077-9%22&amp;format=json&amp;resultType=core; Unique MED41413177 complete authors/title/year/DOI/PMCID and abstract | supports | Cullin diversity2025 primary article metadata/abstract; exact Table1 and body scopes separately recorded. |
| septin-murakami2012-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC3323989/; Genuine primary HTML Abstract,Table1,Resultssec2–5 with Figures1–4 captions,Discussionsec6,Methodssec8–10,12–13; no pixels/supplements | supports | Yeast purification/MS supports listed core constituents plus TFIIK. Tfb6-associated11-subunit and dissociation states are not a contradiction of the canonical seven-subunit core ontology. Reconstitution supports function and context-dependent Ssl2 retention; it does not prove a unique assembly sequence. FY602/FY603 S288c and other CB010/DG backgrounds are distinguished from generic reference accessions; E.coli Rosetta2/XL10 are production/cloning hosts. |
| septin-PMC5241021-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5241021/fullTextXML; Genuine JATS front/author/license,Resultssec003–008,Discussionsec009,Methodssec011–017,embedded Figures1–8 captions; only Figure2 pixels separately inspected | supports | Hu2017 defines WDR1 Tb927.10.15080, Cullin4 Tb927.3.1290 and DDB1 Tb927.6.5110. Yeast fragment interactions, GST-fusion plus parasite lysate and co-IP establish associations, not a complete purified catalytic complex. PDZ alone is insufficient/not required; PEST deletion disrupts fragment association. RNAi phenotypes and abundance/chase/IP/pSer54-Centrin2 conditions remain separate24h/48h observations. Anti-ubiquitin species may be TbPLK or partners; overexpression phenocopies do not prove rescue/exclusive mediation. 29-13 RNAi and Lister427 tagging remain distinct from TREU927 reference protein identities; Cdc27/APC-C and D-box contributions remain qualified. |
| septin-PMC12816148-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12816148/fullTextXML; Genuine JATS front/abstract,Table1,ResultsSec5/6,DiscussionSec10 and cell cultureSec12; no figure pixels or supplemental LC-MS/MS reanalysis | supports | 2025 table maps Tb927.3.1290 to TbCul-D and Tb927.11.11430 to TbCul-E; discussion attributes old TbPLK work to E, an explicitly retained source nomenclature conflict. TbCul-D immunoisolation includes DDB1,Rbx1 and DCAF loci11.3190/8.840; these are not automatically new invariant members of the earlier WDR1-defined assembly. Lister427 procyclic culture scope retained. |
| septin-prakash2000-doi | https://doi.org/10.1016/s0027-5107(00)00037-3; Exact current route response only | context_only | Current DOI response is HTTP200 redirect-only linking-hub HTML, not article body. Original historical failed-access dates and response types remain separate. |
| septin-prakash2000-publisher | https://www.sciencedirect.com/science/article/pii/S0027510700000373; Exact current route response only | context_only | Current publisher403 is failed access; no body inferred. Original historical failed-access dates and response types remain separate. |
| septin-image-metadata | https://pmc-oa-opendata.s3.amazonaws.com/PMC5241021.1/PMC5241021.1.json; Complete PMC OA metadata,license/retraction state,Figure2 media URL and MD5 | supports | PMC5241021 CC-BY metadata lists Figure2 MD5 75b6e61b8ad7f417a1ca474d1fda5b05, matching the fresh retrieved and frozen local image. JATSfront separately provides CC-BY4.0 and Hu/Zhou/Han/Li attribution. |
| septin-image-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5241021.1/ppat.1006146.g002.jpg; Actual Figure2 image pixels A–F viewed; byte SHA matches frozen image; caption/body separately read | supports | A constructs, B two-hybrid growth, C GST-fusion/lysate pull-down, D co-IP, E WDR1/TbPLK fluorescence across phases and F WDR1/LdCen1 localization are visible. This is not a micrograph of the entire ligase. Caption supplies5µm scale; no whole-complex dimensions measured. PanelF pixel saysG1 while source caption saysS; maintained G1/S wording avoids a false panel-specific phase claim. No Figure3/6/other pixels or supplements inspected in this pass. |
| septin-image-local | data/images/other/crl4wdr1_ubiquitin_ligase_complex/pmc5241021_ppat_1006146_g002_04eab535.jpg; Actual frozen Figure2 pixels independently viewed with view_image | supports | Complete local image is exactly the fresh publisher/PMC media asset. Actual panel inspection, source-caption scope and license are recorded separately; old record claims of other figures having been inspected are historical, not repeated current pixel certification. |
| septin-packet-source-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/source-receipts.json; Actual HTTP receipts/status/types/times and body hashes | context_only | Access provenance only. Three initial InterPro429 responses succeeded on actual sequential retry; PMC challenge HTML/JATS500 and Prakash redirect/403 provide no body evidence. Only separately genuine sources support scientific claims. |
| septin-packet-retry-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/retry-receipts.json; Actual HTTP receipts/status/types/times and body hashes | context_only | Access provenance only. Three initial InterPro429 responses succeeded on actual sequential retry; PMC challenge HTML/JATS500 and Prakash redirect/403 provide no body evidence. Only separately genuine sources support scientific claims. |
| septin-packet-shared-receipts | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/shared-receipts.json; Actual HTTP receipts/status/types/times and body hashes | context_only | Access provenance only. Three initial InterPro429 responses succeeded on actual sequential retry; PMC challenge HTML/JATS500 and Prakash redirect/403 provide no body evidence. Only separately genuine sources support scientific claims. |
| septin-adapter-runner-historical | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical2026-11-03T00:49:00.848907Z–00:49:00.863225Z; exit1 PermissionError reading pyvenv.cfg | context_only | Historical unavailable runner only. No new invocation or successful runner execution claimed; current official catalogue and primary/native fallback are separate. |
| septin-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/original-checks.json; Three actual native validate/render executions; all43 historical input occurrences | supports | All three original native validations/renders pass and Markdown matches exactly. All43 input occurrences match historical source, including image. All current assigned records nonstale. Original batch26 global execution scopes are valid historical reuse, not fresh48 execution. |
| septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex | data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml; Complete maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,graphs,discussions/history and image metadata read. Target nonstale. |
| septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex | reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Historical immutable observations and genuine batch26 execution origin retained. |
| septin-native-core_tfiih_complex_portion_of_holo_tfiih_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Native identity/symbol validation does not prove formation, experimental strain or biological receptor assignment. |
| septin-native-core_tfiih_complex_portion_of_holo_tfiih_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml --causal-graphs; logSHA256 645a9da180103d3b5c10abd60d0e572c1d5ea943ed7b589f189fde48e26b193c | supports | Exit0. Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Native identity/symbol validation does not prove formation, experimental strain or biological receptor assignment. |
| septin-record-core_tfiih_complex_portion_of_nef3_complex | data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml; Complete maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,graphs,discussions/history and image metadata read. Target nonstale. |
| septin-original-core_tfiih_complex_portion_of_nef3_complex | reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Historical immutable observations and genuine batch26 execution origin retained. |
| septin-native-core_tfiih_complex_portion_of_nef3_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Native identity/symbol validation does not prove formation, experimental strain or biological receptor assignment. |
| septin-native-core_tfiih_complex_portion_of_nef3_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml --causal-graphs; logSHA256 69dc56ef8abd646c00d891465ba1ffa7d3593f5bb887334d9130f40e4c8a5da4 | supports | Exit0. Seven reviewed example occurrences/seven distinct accessions and seven COVERED typed nodes. Native identity/symbol validation does not prove formation, experimental strain or biological receptor assignment. |
| septin-record-crl4wdr1_ubiquitin_ligase_complex | data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml; Complete maintained record at e2498a28ea896fb9a053dc378380f1f44786a090 | supports | All identity/relations/components/examples/roles,functions/taxa,canonical notes,graphs,discussions/history and image metadata read. Target nonstale. |
| septin-original-crl4wdr1_ubiquitin_ligase_complex | reviews/structured/20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit/review.yaml; Complete original YAML and exact paired Markdown | supports | Findings/actions/checks/scopes/limitations independently reassessed. Historical immutable observations and genuine batch26 execution origin retained. |
| septin-native-crl4wdr1_ubiquitin_ligase_complex-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-verify-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Exit0. Three unreviewed example occurrences/three distinct accessions and one COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not validate the disputed biological assignment. Native identity/symbol validation does not prove formation, experimental strain or biological receptor assignment. |
| septin-native-crl4wdr1_ubiquitin_ligase_complex-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-causal-receipt.json; Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml --causal-graphs; logSHA256 fdf9c3bef748b6f4560e6e8ce8dde3a92ebb0e08a8417f04075ecc5a770c3b18 | supports | Exit0. Three unreviewed example occurrences/three distinct accessions and one COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not validate the disputed biological assignment. Native identity/symbol validation does not prove formation, experimental strain or biological receptor assignment. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt; exact retained SHA256 reverified during PR2385 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is retained historical availability evidence, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |
| root-native-cog_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-cog_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-coma_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-coma_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-copi_vesicle_coat-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-copi_vesicle_coat-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-copii_vesicle_coat-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-copii_vesicle_coat-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-core_primosome_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-core_primosome_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-core_tfiih_complex_portion_of_nef3_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-core_tfiih_complex_portion_of_nef3_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-corvet_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-corvet_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-crl4wdr1_ubiquitin_ligase_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-crl4wdr1_ubiquitin_ligase_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ctf18_rfc_like_complex-uniprot-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-verify.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |
| root-native-ctf18_rfc_like_complex-uniprot-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-causal.log; Actual native command output; associated receipt binds command, source head, base and UTC interval | context_only | 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native coverage classifications are retained in the command output. Actual exit0; inventory is distinct from biological claim and source-scope assessment. |

## Limits And Additional Notes

- COMA, core-primosome and Ctf18-RFC independent review: Only COMA, core primosome and Ctf18 RFC-like current whole records are independently judged. Other frozen cohort members/image are not read or disposed here; no neighboring/category/group issue is terminally resolved.
- COMA, core-primosome and Ctf18-RFC independent review: Schmitzberger2017 genuine JATS read at the exact listed sections and Figures1/2/7/8 text captions only. K.lactis recombinant work and native S.cerevisiae co-IP/localization are distinct. EV6 strain table, raw images/blots, supplemental data and physical figure pixels were not inspected. S288C-derived methods permit explicit exceptions; exact mutant genotype is not invented.
- COMA, core-primosome and Ctf18-RFC independent review: Current DeWulf2003 terminal body routes returned challenge/404/no-result/403. Fresh complete native abstract was read; a transient web reader supplied only abstract/intro/first-results context, not sec4. Original Oct22 full-body claim remains immutable historical evidence, not a newly certified body read. Current Okp1 finding independently rests on Schmitzberger body.
- COMA, core-primosome and Ctf18-RFC independent review: Biggins2013, Kim-MacNeill2003 and Kaguni2011 metadata are secondary literature; Kaguni body is read at S1,S5,S6,S9–12 as specified. No cited primary experiment, other body sections or figures is certified by that review. Ortiz1999, Huh2003 and Mayer2001 remain complete-primary-abstract/native-authority tiers, not full-body experiments.
- COMA, core-primosome and Ctf18-RFC independent review: InterPro type/name/signature/class identity is separate from generated biological prose. Unchecked descriptions for IPR053016/IPR050219/IPR050238 are excluded from biological support. P49956 lacks current IPR053016 xref; five reviewed ortholog hits support class identity, not a fabricated reference-accession link or new alignment. No exhaustive absence of other RFC2–5 families is asserted.
- COMA, core-primosome and Ctf18-RFC independent review: Current exact-gene searches are bounded reviewed-reference-taxon queries of size100; no historical uniqueness claim is inferred from fresh results. Taxon-specific protein examples and generic component classes remain distinct.
- COMA, core-primosome and Ctf18-RFC independent review: Official catalogue lacks a natural yeast match in its complete returned20 organism rows. E.coli precise1k contains five strains and201 modules; b3066 crosses module10 threshold while b4052 has no above-threshold hit. Alias noncoverage, threshold nonmembership and catalogue absence are not biological absence. Generated module narrative and activity interpretations are not experimental evidence; expression is not assembly/localization/necessity or causal regulation.
- COMA, core-primosome and Ctf18-RFC independent review: Historical unavailable runner is dated2026-11-03T00:49:00.848907–00:49:00.863225Z, not a fresh execution. Root native protein receipts cover current implemented identifiers and graph-example diagnostics only. Root owns full QC, final saved-head CI and queue; no pending stage is certified.
- COMA, core-primosome and Ctf18-RFC independent review: No maintained record, original review pair, Git state or GitHub object is edited by this review. Findings are proposed bounded record curation, while stale/applicability bundle defects require a linked immutable successor.
- COG, COPI/COPII coats and CORVET independent review: Fresh current PR source snapshots are used with actual request completion timestamps; the shared same-PR catalogue retains its original retrieval timestamp and was independently reread. Selected Yu/Ha/Ishii/Zanetti body sections and Matsuoka author-PDF text were actually inspected; other papers remain complete indexed-primary-abstract/native-annotation tiers.
- COG, COPI/COPII coats and CORVET independent review: No maintained images occur in these four records. No external figure pixels, movies, supplementary datasets, raw-data reanalysis or image licence/reproduction permission is certified. Text captions/PDF extraction are not pixel inspection.
- COG, COPI/COPII coats and CORVET independent review: Peplowska full body unavailable (DOI response is bibliographic Crossref JSON; publisher403); Sandmann PMC challenge/BioC429 yielded no body. Exact strain/Methods and detailed mechanistic directness beyond inspected abstracts remain limited. Initial five InterPro429s had separately dated successful native retries.
- COG, COPI/COPII coats and CORVET independent review: Recombinant production hosts are not biological dataset proxies. Ha COG yeast-sequence complexes were produced in E.coli; Yu combines mammalian coatomer and yeast/human Arf components; Matsuoka synthetic/native membrane stoichiometry differs. Neither model geometry nor cell viability automatically establishes universal formation necessity.
- COG, COPI/COPII coats and CORVET independent review: Current generic Cog1/2/7 family mappings do not certify sequence coverage of the maintained S288C examples, whose native entries lack those whole-family IDs. Broader/domain candidates for other CORVET proteins are not promoted to exact groundings.
- COG, COPI/COPII coats and CORVET independent review: No fresh structured-adapter runner execution claimed. The retained00:49Z failure remains historical; current source fallback inspected the complete official catalogue and found no biological yeast/Kluyveromyces/mammalian match. No unrelated host/module proxy or biological absence inferred.
- COG, COPI/COPII coats and CORVET independent review: Four original pairs/56 historical input occurrences and48 current source/worktree hashes verified. All four assigned targets unchanged. Root-owned full QC, post-save, CI and queue are not precertified by this report.
- COG, COPI/COPII coats and CORVET independent review: Four inherited minor findings retained with exact lineage and proposed guarded record curation; no new scientific finding established or neighboring/group/category issue terminally resolved.
- Two TFIIH core contexts and CRL4WDR1 independent review: All three current targets are unchanged from original frozen records. Three inherited findings remain confirmed: two minor TFIIH exact-family mappings and one major CRL4WDR1 wrong-locus example. No new record finding or unrelated terminal issue resolution.
- Two TFIIH core contexts and CRL4WDR1 independent review: 17 protein example occurrences are10 distinct accessions:14 reviewed yeast occurrences share7 accessions;3 unreviewed parasite occurrences are3 accessions. All15 typed nodes are native COVERED, which does not biologically validate Q582R9 as source WDR1. Native command success is not scientific membership or formation proof.
- Two TFIIH core contexts and CRL4WDR1 independent review: Murakami genuine body read only at Abstract/Table1,Resultssec2–5,Discussionsec6,Methodssec8–10/12–13 including cited captions. Takagi/Ranish/Huh current inspection is complete native metadata/abstract only. Prakash is secondary-review abstract only; current DOIredirect and publisher403 are not body access.
- Two TFIIH core contexts and CRL4WDR1 independent review: Hu2017 genuine JATS front/Results003–008/Discussion009/Methods011–017 and embedded Figures1–8 captions were read. Only frozenFigure2A–F pixels were inspected. No other figure/supplement pixels, raw proteomics, sequence alignment or whole-study replication. GST-plus-lysate/co-IP, incomplete fragment interactions, unresolved ubiquitinated species and phenocopy-versus-rescue distinctions remain explicit.
- Two TFIIH core contexts and CRL4WDR1 independent review: 2025 cullin source was read at front/abstract/Table1/Sec5/6/10/12 only; table TbCul-D locus3.1290 versus Discussion oldPLK→TbCul-E attribution conflict is preserved. New Rbx/DCAF coisolates are not automatically members of the earlier WDR1-defined assembly.
- Two TFIIH core contexts and CRL4WDR1 independent review: Frozen Figure2 SHA matches current PMC asset and publisherMD5. JATSfront licensesCC-BY4.0 and authorsHu/Zhou/Han/Li. PixelF saysG1 while source caption saysS; maintainedG1/S scope is not contradicted. No whole-ligase dimension measured or other historical pixel inspection recertified.
- Two TFIIH core contexts and CRL4WDR1 independent review: IPR001945 mixed XPG/Rad2 background is not used as RAD3 identity evidence; native family name, reviewed P06839 xref and all8 returned reviewed family members establish the bounded mapping. IPR050358 top-level generated-prose flags are true, so generated functional prose is excluded; broad Cullin/DDB1-related families do not force exact assembly mappings.
- Two TFIIH core contexts and CRL4WDR1 independent review: Current complete official catalogue has no matching Saccharomyces orTrypanosoma dataset. No unrelated bacterial proxy and no biological-absence inference. Historical runner failure remains actualNov3 00:49Z, with no fresh invocation. Original dated catalogue statements remain historical observations.
- Two TFIIH core contexts and CRL4WDR1 independent review: All43 original input occurrences and three deterministic original pairs verified. Original batch26 global execution scopes retained. Two NEF3 failed-access rows were typed database but alreadycontext_only/explicitlyfailed; correction is kind-only, not an accusation of fabricated body access. Parent global/postsave/finalCI/queue/merge/deletion are outside this source-review attestation.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain byte-identical. COMA now adds four component_ref nodes, four source-cited constituent edges and history. The current added assertions are substantively reassessed against actual sources, not merely assigned a new frozen hash.
- All inherited findings retain exact predecessor identities. Current authority results are dated observations and do not reconstruct historical query results. Formation evidence is limited to the actually assayed conditions and physical-association outcomes.
- All ten complete records have positive molecular or pathway narratives requiring source applicability assessment. Seven formal exclusions and three prose exclusions are replaced by actual coverage assessments with precise organism and strain limits.
- The original NEF3 Prakash DOI and publisher retrieval failures already have context_only support and explicitly disclose failure. The correction distinguishes their evidence kind as validation receipts; it does not allege that the original claimed successful paper-body access. Actual secondary-review metadata and abstract evidence remain separately bounded.
- The actual native protein inventory has 58 represented examples and 50 typed nodes: 47 COVERED and three UNANCHORED_WITH_UNIPROT. These deterministic classifications do not prove biological protein-example correspondence or establish automatic record defects.
- The WDR1 wrong-locus finding remains major despite successful identifier checks and native node coverage. It is separately tracked for record curation. The frozen CRL4WDR1 image is an explicit inspected input; source figure scope remains distinct from molecular-identity evidence.
- Scientific curation remains separate from this review PR. Exact family identities, complex membership, primary experimental scope and current query uniqueness are assessed without forcing universal formation claims or whole-protein mappings from broad domains.
- Local full QC and focused gates passed before saving. Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI are subsequent external gates. Existing issue #2514 tracks native bulk-PMID transport/reporting; bounded supplemental requests verified all 909 affected PMIDs without changing the original report or cache.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T041555Z-pr2385-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2385: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-04T04:02:59.595459Z'
finished_at: '2026-11-04T04:15:55Z'
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
summary: 'Current-input independent review of all ten records substantively refreshes
  the stale COMA target, corrects ten unsupported structured-source exclusions and
  distinguishes two unsuccessful NEF3 access receipts from database evidence. Ten
  inherited scientific findings remain across nine targets: one major WDR1 protein-example
  identity finding and nine minor findings. The core primosome passes with explicit
  source limits. The overall verdict remains needs_curation; only linked immutable
  review successors are added.'
source:
  git_revision: e2498a28ea896fb9a053dc378380f1f44786a090
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
  - path: data/images/other/crl4wdr1_ubiquitin_ligase_complex/pmc5241021_ppat_1006146_g002_04eab535.jpg
    sha256: 670801001c1d236247e8901451b48538d1b444bbeddde152500be4273d75cc62
    role: context
  - path: data/structures/other/cog_complex.yaml
    sha256: 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac
    role: target
  - path: data/structures/other/coma_complex.yaml
    sha256: 12d58998e16ab86e55d0c70e47de8fd7cf3a797e528ede3cc99bbff4e8854da5
    role: target
  - path: data/structures/other/copi_vesicle_coat.yaml
    sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
    role: target
  - path: data/structures/other/copii_vesicle_coat.yaml
    sha256: 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2
    role: target
  - path: data/structures/other/core_primosome_complex.yaml
    sha256: 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac
    role: target
  - path: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    sha256: 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5
    role: target
  - path: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    sha256: 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009
    role: target
  - path: data/structures/other/corvet_complex.yaml
    sha256: a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0
    role: target
  - path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    sha256: 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4
    role: target
  - path: data/structures/other/ctf18_rfc_like_complex.yaml
    sha256: abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3
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
  - path: reviews/structured/20261022T051656Z-cog-complex-audit/review.md
    sha256: 23c098c4064e28bbaacd19fb3e0492d1f879c430b4fa149d61e736a2d9750eeb
    role: context
  - path: reviews/structured/20261022T051656Z-cog-complex-audit/review.yaml
    sha256: 958b6ec5699e9242068a0dc192ad59a515356f82bd3c35c96648a24853075b31
    role: context
  - path: reviews/structured/20261022T051657Z-coma-complex-audit/review.md
    sha256: 830943894b28778e519cf0cf1ec27e31602192ae06b2278ea09303212daf1535
    role: context
  - path: reviews/structured/20261022T051657Z-coma-complex-audit/review.yaml
    sha256: 9ea8645cbc550490dbc1e6b167ec8be991a711a5f4e2930ecce221793a6d4531
    role: context
  - path: reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.md
    sha256: cb5fe6f5d7a8939f8e2c702f405660f657fbc03181471b1b841c046999332c52
    role: context
  - path: reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.yaml
    sha256: 2d0704ab60efd51c8356ca08977da0001cb9d60ea0a30992b2d1c454bc79f145
    role: context
  - path: reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.md
    sha256: 4f16870fa8b53ee75a7786b9a68a89773ee39a9484887e5e0e2299788f77ed48
    role: context
  - path: reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.yaml
    sha256: 60e24f7cc590b681a782336f7f990d7b80b2be36d04ff50fa65eddb30876fb0f
    role: context
  - path: reviews/structured/20261022T051659Z-core-primosome-complex-audit/review.md
    sha256: 9828c5d31f044bc7dd2263d137991c540b3b8cf37135d2cdb10b4f95db76adfa
    role: context
  - path: reviews/structured/20261022T051659Z-core-primosome-complex-audit/review.yaml
    sha256: 9797a7e7c32973e0a3f0a887137b7f3cf686293d225d23a97e1245e74ce4b86d
    role: context
  - path: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit/review.md
    sha256: 035815000a9c442c02a43def02664c7644238698d0e8e71aa8df14034fcf1319
    role: context
  - path: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit/review.yaml
    sha256: 1fa225f21cd3d2930a4e54cdfd3f994163108873e1a0fdc2012c09748fa4bba1
    role: context
  - path: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit/review.md
    sha256: f8838948b66001fcb0937ebeae1faaee3224cb8de37631747114a106b5990833
    role: context
  - path: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit/review.yaml
    sha256: b68a43c5cfa5ecd68a3ebe58c3153365cfbf1608bb26c6c676b0c760b26a9e76
    role: context
  - path: reviews/structured/20261022T051701Z-corvet-complex-audit/review.md
    sha256: 62bf1fd48d7f59294bae41a3fff3c73ca947a97206a07939091cb8f8132398be
    role: context
  - path: reviews/structured/20261022T051701Z-corvet-complex-audit/review.yaml
    sha256: 999552cd820926502a6b5ac08818b6951b954259aabe1d0aa6fe6669b518aaa5
    role: context
  - path: reviews/structured/20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit/review.md
    sha256: a61b13c755331a40dd0c3050b0e5e0f08e2510c08b427878b0961635dc720bfa
    role: context
  - path: reviews/structured/20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit/review.yaml
    sha256: acb8e7f6bc72d13be11eca966f85f51069d051190a3de919f4f8e29e02e6fb50
    role: context
  - path: reviews/structured/20261022T051703Z-ctf18-rfc-like-complex-audit/review.md
    sha256: 89aea6cdb05caa348f7fc18a26e0e7d3034b1178515acb7645594b789d8b4f9e
    role: context
  - path: reviews/structured/20261022T051703Z-ctf18-rfc-like-complex-audit/review.yaml
    sha256: 8c538160352a986a778a5f30206696fee0447095caf5739fec41c975f610be22
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
- target_id: GO:0017119
  path: data/structures/other/cog_complex.yaml
  label: COG complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cog_complex.yaml
    role: maintained scientific record
- target_id: GO:0000817
  path: data/structures/other/coma_complex.yaml
  label: COMA complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
- target_id: GO:0030126
  path: data/structures/other/copi_vesicle_coat.yaml
  label: COPI vesicle coat
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copi_vesicle_coat.yaml
    role: maintained scientific record
- target_id: GO:0030127
  path: data/structures/other/copii_vesicle_coat.yaml
  label: COPII vesicle coat
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copii_vesicle_coat.yaml
    role: maintained scientific record
- target_id: GO:1990098
  path: data/structures/other/core_primosome_complex.yaml
  label: core primosome complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_primosome_complex.yaml
    role: maintained scientific record
- target_id: GO:0000438
  path: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
  label: core TFIIH complex portion of holo TFIIH complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    role: maintained scientific record
- target_id: GO:0000440
  path: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
  label: core TFIIH complex portion of NEF3 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    role: maintained scientific record
- target_id: GO:0033263
  path: data/structures/other/corvet_complex.yaml
  label: CORVET complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/corvet_complex.yaml
    role: maintained scientific record
- target_id: cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  label: CRL4WDR1 ubiquitin ligase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
- target_id: GO:0031390
  path: data/structures/other/ctf18_rfc_like_complex.yaml
  label: Ctf18 RFC-like complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ctf18_rfc_like_complex.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 3276cff01a281a5d86d8122a0c34978a90e41ed2.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    bd8e9c4b16a27dc303533b69f4d3b8d8f0f977a5.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head e2498a28ea896fb9a053dc378380f1f44786a090.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head e2498a28ea896fb9a053dc378380f1f44786a090.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head e2498a28ea896fb9a053dc378380f1f44786a090.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head e2498a28ea896fb9a053dc378380f1f44786a090.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head e2498a28ea896fb9a053dc378380f1f44786a090.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0017119
  status: passed
  required: true
  target_ids:
  - GO:0017119
  command: just validate data/structures/other/cog_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0017119
  status: passed
  required: true
  target_ids:
  - GO:0017119
  command: just validate-strict data/structures/other/cog_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0000817
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: just validate data/structures/other/coma_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0000817
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: just validate-strict data/structures/other/coma_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0030126
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just validate data/structures/other/copi_vesicle_coat.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0030126
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just validate-strict data/structures/other/copi_vesicle_coat.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0030127
  status: passed
  required: true
  target_ids:
  - GO:0030127
  command: just validate data/structures/other/copii_vesicle_coat.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0030127
  status: passed
  required: true
  target_ids:
  - GO:0030127
  command: just validate-strict data/structures/other/copii_vesicle_coat.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:1990098
  status: passed
  required: true
  target_ids:
  - GO:1990098
  command: just validate data/structures/other/core_primosome_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:1990098
  status: passed
  required: true
  target_ids:
  - GO:1990098
  command: just validate-strict data/structures/other/core_primosome_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0000438
  status: passed
  required: true
  target_ids:
  - GO:0000438
  command: just validate data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0000438
  status: passed
  required: true
  target_ids:
  - GO:0000438
  command: just validate-strict data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0000440
  status: passed
  required: true
  target_ids:
  - GO:0000440
  command: just validate data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0000440
  status: passed
  required: true
  target_ids:
  - GO:0000440
  command: just validate-strict data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0033263
  status: passed
  required: true
  target_ids:
  - GO:0033263
  command: just validate data/structures/other/corvet_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0033263
  status: passed
  required: true
  target_ids:
  - GO:0033263
  command: just validate-strict data/structures/other/corvet_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just validate data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: just validate-strict data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0031390
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: just validate data/structures/other/ctf18_rfc_like_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0031390
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: just validate-strict data/structures/other/ctf18_rfc_like_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385
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
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  summary: Whole-record applicability was assessed for all ten positive molecular
    or pathway narratives, correcting seven formal expression-only exclusions and
    three prose exclusions. Official source coverage is distinguished from biological
    applicability. The covered E. coli primosome genes are checked in the actual five-strain
    precise1k dataset, with bounded above-threshold membership and module context.
    Expression membership is not evidence of physical assembly or formation necessity.
    Other assigned organism contexts are not replaced with unrelated dataset hosts
    or strains. The unavailable runner receipt remains historical and separate from
    current catalogue access.
  evidence_ids:
  - micro-catalogue
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-b4052
  - micro-ecoli-b3066
  - micro-ecoli-JW4012
  - micro-ecoli-JW3038
  - micro-ecoli-module-10
  - plaque-catalogue
  - plaque-catalogue-bounded-search
  - septin-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - micro-policy
  - micro-schema
  - micro-native-policy
  - micro-graph-policy
  - micro-up-P0ABS5
  - micro-up-P0ACB0
  - micro-up-P25559
  - micro-up-P33895
  - micro-up-P36012
  - micro-up-P38251
  - micro-up-P38313
  - micro-up-P38629
  - micro-up-P38877
  - micro-up-P40339
  - micro-up-P40348
  - micro-up-P40460
  - micro-up-P49956
  - micro-up-P53298
  - micro-up-Q02732
  - micro-up-Q04477
  - micro-up-Q06675
  - micro-tax-4932
  - micro-tax-559292
  - micro-tax-562
  - micro-tax-83333
  - micro-go-0000228
  - micro-go-0000776
  - micro-go-0000817
  - micro-go-0003689
  - micro-go-0006269
  - micro-go-0007062
  - micro-go-0031390
  - micro-go-0140513
  - micro-go-1990077
  - micro-go-1990098
  - micro-go-1990099
  - micro-go-1990156
  - micro-ipr-IPR018464
  - micro-ipr-IPR048743
  - micro-ipr-IPR007692
  - micro-ipr-IPR006295
  - micro-ipr-IPR050219
  - micro-ipr-IPR053016
  - micro-ipr-IPR019128
  - micro-ipr-IPR018607-retry
  - micro-ipr-IPR050238-retry
  - micro-pmid-10323865
  - micro-pmid-11389843
  - micro-pmid-14562095
  - micro-pmid-14614842
  - micro-pmid-14633972
  - micro-pmid-21856207
  - micro-pmid-23908374
  - micro-pmid-29046335
  - micro-schmitzberger2017-jats
  - micro-kaguni2011-jats
  - micro-ecoli-meta
  - micro-ecoli-module-10
  - plaque-policy
  - plaque-review-skill
  - plaque-schema
  - plaque-review-schema
  - plaque-review-profile
  - plaque-checklist
  - plaque-go
  - plaque-tax-4932
  - plaque-tax-559292
  - plaque-protein-P11076
  - plaque-protein-P12868
  - plaque-protein-P15303
  - plaque-protein-P19146
  - plaque-protein-P20606
  - plaque-protein-P20795
  - plaque-protein-P23643
  - plaque-protein-P27801
  - plaque-protein-P32074
  - plaque-protein-P36017
  - plaque-protein-P38968
  - plaque-protein-P39702
  - plaque-protein-P40094
  - plaque-protein-P40482
  - plaque-protein-P40509
  - plaque-protein-P41810
  - plaque-protein-P41811
  - plaque-protein-P43621
  - plaque-protein-P53079
  - plaque-protein-P53195
  - plaque-protein-P53271
  - plaque-protein-P53600
  - plaque-protein-P53622
  - plaque-protein-P53951
  - plaque-protein-P53959
  - plaque-protein-Q03308
  - plaque-protein-Q04491
  - plaque-protein-Q04632
  - plaque-protein-Q06096
  - plaque-ipr-IPR033370
  - plaque-ipr-IPR009316
  - plaque-ipr-retry-IPR007265
  - plaque-ipr-retry-IPR048682
  - plaque-ipr-retry-IPR019465
  - plaque-ipr-IPR010490
  - plaque-ipr-IPR019335
  - plaque-ipr-IPR007255
  - plaque-ipr-IPR006687
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR032914
  - plaque-ipr-retry-IPR045111
  - plaque-ipr-IPR007810
  - plaque-ipr-retry-IPR001619
  - plaque-paper-0
  - plaque-paper-1
  - plaque-paper-2
  - plaque-paper-3
  - plaque-paper-4
  - plaque-paper-5
  - plaque-paper-6
  - plaque-paper-7
  - plaque-paper-8
  - plaque-paper-9
  - plaque-paper-10
  - plaque-paper-11
  - plaque-paper-12
  - plaque-paper-13
  - plaque-paper-14
  - plaque-paper-15
  - plaque-paper-16
  - plaque-paper-17
  - plaque-paper-18
  - plaque-paper-19
  - plaque-paper-20
  - plaque-paper-21
  - plaque-paper-22
  - plaque-paper-23
  - plaque-yu2012-body
  - plaque-ha2016-s3
  - plaque-ishii2018-s3
  - plaque-zanetti2013-s3
  - plaque-matsuoka1998-pdf
  - plaque-peplowska2007-doi
  - plaque-catalogue
  - septin-review-policy
  - septin-curation-policy
  - septin-schema-policy
  - septin-protein-policy
  - septin-graph-policy
  - septin-literature-policy
  - septin-go
  - septin-catalogue
  - septin-tax4932
  - septin-tax559292
  - septin-tax5691
  - septin-tax185431
  - septin-protein-Q00578
  - septin-protein-P32776
  - septin-protein-Q02939
  - septin-protein-Q04673
  - septin-protein-Q12004
  - septin-protein-Q3E7C1
  - septin-protein-P06839
  - septin-protein-Q57XW2
  - septin-protein-Q586I3
  - septin-protein-Q582R9
  - septin-ipr-IPR001161
  - septin-ipr-IPR027079
  - septin-ipr-IPR004598
  - septin-retry-IPR012170
  - septin-ipr-IPR004600
  - septin-retry-IPR009400
  - septin-retry-IPR001945
  - septin-ipr-IPR045093
  - septin-ipr-IPR050358
  - septin-pmid-14562095
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-22411836
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-doi-9
  - septin-doi-3
  - septin-murakami2012-pmc
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-image-metadata
  - septin-image-s3
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
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
- check_id: cog_complex-uniprot-verify
  name: Native COG complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0017119
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cog_complex.yaml
    --verify
  exit_code: 0
  summary: 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cog_complex-uniprot-verify
- check_id: cog_complex-uniprot-causal
  name: Native COG complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0017119
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/cog_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-cog_complex-uniprot-causal
- check_id: coma_complex-uniprot-verify
  name: Native COMA complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/coma_complex.yaml
    --verify
  exit_code: 0
  summary: 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-coma_complex-uniprot-verify
- check_id: coma_complex-uniprot-causal
  name: Native COMA complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/coma_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-coma_complex-uniprot-causal
- check_id: copi_vesicle_coat-uniprot-verify
  name: Native COPI vesicle coat UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/copi_vesicle_coat.yaml
    --verify
  exit_code: 0
  summary: 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-copi_vesicle_coat-uniprot-verify
- check_id: copi_vesicle_coat-uniprot-causal
  name: Native COPI vesicle coat UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/copi_vesicle_coat.yaml
    --causal-graphs
  exit_code: 0
  summary: 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-copi_vesicle_coat-uniprot-causal
- check_id: copii_vesicle_coat-uniprot-verify
  name: Native COPII vesicle coat UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030127
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/copii_vesicle_coat.yaml
    --verify
  exit_code: 0
  summary: 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-copii_vesicle_coat-uniprot-verify
- check_id: copii_vesicle_coat-uniprot-causal
  name: Native COPII vesicle coat UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030127
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/copii_vesicle_coat.yaml
    --causal-graphs
  exit_code: 0
  summary: 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-copii_vesicle_coat-uniprot-causal
- check_id: core_primosome_complex-uniprot-verify
  name: Native core primosome complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990098
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_primosome_complex.yaml
    --verify
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-core_primosome_complex-uniprot-verify
- check_id: core_primosome_complex-uniprot-causal
  name: Native core primosome complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990098
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_primosome_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-core_primosome_complex-uniprot-causal
- check_id: core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify
  name: Native core TFIIH complex portion of holo TFIIH complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000438
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    --verify
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify
- check_id: core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal
  name: Native core TFIIH complex portion of holo TFIIH complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000438
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal
- check_id: core_tfiih_complex_portion_of_nef3_complex-uniprot-verify
  name: Native core TFIIH complex portion of NEF3 complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000440
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    --verify
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-core_tfiih_complex_portion_of_nef3_complex-uniprot-verify
- check_id: core_tfiih_complex_portion_of_nef3_complex-uniprot-causal
  name: Native core TFIIH complex portion of NEF3 complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000440
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-core_tfiih_complex_portion_of_nef3_complex-uniprot-causal
- check_id: corvet_complex-uniprot-verify
  name: Native CORVET complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033263
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/corvet_complex.yaml
    --verify
  exit_code: 0
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-corvet_complex-uniprot-verify
- check_id: corvet_complex-uniprot-causal
  name: Native CORVET complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033263
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/corvet_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-corvet_complex-uniprot-causal
- check_id: crl4wdr1_ubiquitin_ligase_complex-uniprot-verify
  name: Native CRL4WDR1 ubiquitin ligase complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    --verify
  exit_code: 0
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-crl4wdr1_ubiquitin_ligase_complex-uniprot-verify
- check_id: crl4wdr1_ubiquitin_ligase_complex-uniprot-causal
  name: Native CRL4WDR1 ubiquitin ligase complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-crl4wdr1_ubiquitin_ligase_complex-uniprot-causal
- check_id: ctf18_rfc_like_complex-uniprot-verify
  name: Native Ctf18 RFC-like complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ctf18_rfc_like_complex.yaml
    --verify
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ctf18_rfc_like_complex-uniprot-verify
- check_id: ctf18_rfc_like_complex-uniprot-causal
  name: Native Ctf18 RFC-like complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/ctf18_rfc_like_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Native command returned
    zero.
  scope_note: Actual current source-head execution. Broad protein groups and missing
    optional examples are not automatically scientific defects.
  evidence_ids:
  - root-native-ctf18_rfc_like_complex-uniprot-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/other/cog_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac;
    current SHA256 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac.
    Record bytes unchanged since the original review.
  snapshot_sha256: 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261022T051656Z-cog-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 958b6ec5699e9242068a0dc192ad59a515356f82bd3c35c96648a24853075b31
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/other/coma_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 d27210c22f2b06eb9eb3d5e8aa3ed93f6bf561ac07ae48ae295b11bf39f561da;
    current SHA256 12d58998e16ab86e55d0c70e47de8fd7cf3a797e528ede3cc99bbff4e8854da5.
    Changed record reassessed against current sources.
  snapshot_sha256: 12d58998e16ab86e55d0c70e47de8fd7cf3a797e528ede3cc99bbff4e8854da5
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261022T051657Z-coma-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9ea8645cbc550490dbc1e6b167ec8be991a711a5f4e2930ecce221793a6d4531
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/other/copi_vesicle_coat.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195;
    current SHA256 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 2d0704ab60efd51c8356ca08977da0001cb9d60ea0a30992b2d1c454bc79f145
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/other/copii_vesicle_coat.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2;
    current SHA256 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 60e24f7cc590b681a782336f7f990d7b80b2be36d04ff50fa65eddb30876fb0f
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/other/core_primosome_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac;
    current SHA256 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261022T051659Z-core-primosome-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9797a7e7c32973e0a3f0a887137b7f3cf686293d225d23a97e1245e74ce4b86d
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5;
    current SHA256 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5.
    Record bytes unchanged since the original review.
  snapshot_sha256: 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 1fa225f21cd3d2930a4e54cdfd3f994163108873e1a0fdc2012c09748fa4bba1
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009;
    current SHA256 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009.
    Record bytes unchanged since the original review.
  snapshot_sha256: 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b68a43c5cfa5ecd68a3ebe58c3153365cfbf1608bb26c6c676b0c760b26a9e76
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/other/corvet_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0;
    current SHA256 a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0.
    Record bytes unchanged since the original review.
  snapshot_sha256: a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261022T051701Z-corvet-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 999552cd820926502a6b5ac08818b6951b954259aabe1d0aa6fe6669b518aaa5
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4;
    current SHA256 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: acb8e7f6bc72d13be11eca966f85f51069d051190a3de919f4f8e29e02e6fb50
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/other/ctf18_rfc_like_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Original frozen SHA256 abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3;
    current SHA256 abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3.
    Record bytes unchanged since the original review.
  snapshot_sha256: abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261022T051703Z-ctf18-rfc-like-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-04T04:15:55Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8c538160352a986a778a5f30206696fee0447095caf5739fec41c975f610be22
- evidence_id: micro-record-0
  kind: record_content
  reference: data/structures/other/coma_complex.yaml
  locator: Entire maintained YAML at source e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:12.505632Z'
  support: supports
  summary: Complete identity, hierarchy, examples, component evidence, taxonomy, functions,
    graph, historical discussions and curation events read. No maintained image or
    quantitative measurement asserted.
  snapshot_sha256: 12d58998e16ab86e55d0c70e47de8fd7cf3a797e528ede3cc99bbff4e8854da5
- evidence_id: micro-prior-0
  kind: prior_review
  reference: reviews/structured/20261022T051657Z-coma-complex-audit/review.yaml
  locator: Entire immutable original YAML and native-derived Markdown
  accessed_at: '2026-11-04T04:13:12.505714Z'
  support: supports
  summary: Original assessments/findings/actions, source tiers and limitations, formal
    applicability check, historical global checks and frozen inputs reviewed. Historical
    body readings and old command dates are not silently asserted as current reads/runs.
  snapshot_sha256: 9ea8645cbc550490dbc1e6b167ec8be991a711a5f4e2930ecce221793a6d4531
- evidence_id: micro-delta-0
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/1-stale.diff
  locator: Original frozen target revision to current main base
  accessed_at: '2026-11-04T04:13:12.505750Z'
  support: supports
  summary: 'COMA alone changes: dated history and four component_ref nodes with constituent
    contributes_to edges. Core primosome and Ctf18 RFC-like remain byte-identical.
    Current source-scoped reassessment is substantive.'
  snapshot_sha256: 3ce2c4601010c0902223525b5bcc92d90d9ac579d271610aaa3745ecb45d57cb
- evidence_id: micro-record-1
  kind: record_content
  reference: data/structures/other/core_primosome_complex.yaml
  locator: Entire maintained YAML at source e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:12.505778Z'
  support: supports
  summary: Complete identity, hierarchy, examples, component evidence, taxonomy, functions,
    graph, historical discussions and curation events read. No maintained image or
    quantitative measurement asserted.
  snapshot_sha256: 3f26d4c8ff702a0d53da6fd3c5f94e95420bfcc8be686b3dfdce317245b78bac
- evidence_id: micro-prior-1
  kind: prior_review
  reference: reviews/structured/20261022T051659Z-core-primosome-complex-audit/review.yaml
  locator: Entire immutable original YAML and native-derived Markdown
  accessed_at: '2026-11-04T04:13:12.505797Z'
  support: supports
  summary: Original assessments/findings/actions, source tiers and limitations, formal
    applicability check, historical global checks and frozen inputs reviewed. Historical
    body readings and old command dates are not silently asserted as current reads/runs.
  snapshot_sha256: 9797a7e7c32973e0a3f0a887137b7f3cf686293d225d23a97e1245e74ce4b86d
- evidence_id: micro-delta-1
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/4-stale.diff
  locator: Original frozen target revision to current main base
  accessed_at: '2026-11-04T04:13:12.505826Z'
  support: supports
  summary: 'COMA alone changes: dated history and four component_ref nodes with constituent
    contributes_to edges. Core primosome and Ctf18 RFC-like remain byte-identical.
    Current source-scoped reassessment is substantive.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-record-2
  kind: record_content
  reference: data/structures/other/ctf18_rfc_like_complex.yaml
  locator: Entire maintained YAML at source e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:12.505849Z'
  support: supports
  summary: Complete identity, hierarchy, examples, component evidence, taxonomy, functions,
    graph, historical discussions and curation events read. No maintained image or
    quantitative measurement asserted.
  snapshot_sha256: abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3
- evidence_id: micro-prior-2
  kind: prior_review
  reference: reviews/structured/20261022T051703Z-ctf18-rfc-like-complex-audit/review.yaml
  locator: Entire immutable original YAML and native-derived Markdown
  accessed_at: '2026-11-04T04:13:12.505871Z'
  support: supports
  summary: Original assessments/findings/actions, source tiers and limitations, formal
    applicability check, historical global checks and frozen inputs reviewed. Historical
    body readings and old command dates are not silently asserted as current reads/runs.
  snapshot_sha256: 8c538160352a986a778a5f30206696fee0447095caf5739fec41c975f610be22
- evidence_id: micro-delta-2
  kind: record_content
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/9-stale.diff
  locator: Original frozen target revision to current main base
  accessed_at: '2026-11-04T04:13:12.505902Z'
  support: supports
  summary: 'COMA alone changes: dated history and four component_ref nodes with constituent
    contributes_to edges. Core primosome and Ctf18 RFC-like remain byte-identical.
    Current source-scoped reassessment is substantive.'
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components exact class/family identity and formation essentiality; Discussions
    append-only rationale/posed_date
  accessed_at: '2026-11-04T04:13:12.505922Z'
  support: supports
  summary: REVIEWED_LABEL_ONLY requires no exact term; taxon-specific examples differ
    from class grounding. Formation differs from viability/function. Preserve rationale/posed_date
    and dated history; current notes/prompt can be narrowed after evidence-backed
    curation.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: micro-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding_status/essentiality; taxonomic presence;
    graph actors and scopes
  accessed_at: '2026-11-04T04:13:12.505943Z'
  support: supports
  summary: Exact grounding, qualitative COMMON, generic protein families/classes,
    and functional/nonmechanistic outlines retain native meanings. UNKNOWN does not
    itself require invented experiments; concrete direct physical-association evidence
    can justify a bounded curation gap.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-native-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks plus current config/profile/output contract
  accessed_at: '2026-11-04T04:13:12.505971Z'
  support: supports
  summary: Positive named protein/pathway assertions trigger applicability, even without
    an expression claim. Actual catalogue host coverage and matched gene/module context
    are bounded; expression is not assembly evidence. Seventeen common inputs are
    identical to previously read bytes; applicable route/profile/config/checklist
    and component/discussion rules freshly reread.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Nonmechanistic functional and assembly outlines; component_ref and source-specific
    edge evidence
  accessed_at: '2026-11-04T04:13:12.505989Z'
  support: supports
  summary: Constituent contributions and broad functional context need not invent
    atomic interactions or universal necessity; grouped nodes and reference xrefs
    are permitted when scope is explicit.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-original-audit
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/original-audit.json
  locator: Six actual native validate/render commands, 41 historical inputs, six original
    files
  accessed_at: '2026-11-04T04:05:17.117768Z'
  support: supports
  summary: All three original YAMLs validate; each Markdown is byte-exact native render.
    All41 historical inputs match their frozen revisions; six assigned original artifacts
    match original PR commit.
  snapshot_sha256: fbef595f030087b2fd1c00c4a50b4fb90d8732a5951a17d9891eb156751c9440
- evidence_id: micro-up-P0ABS5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ABS5.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P0ABS5.raw
  accessed_at: '2026-11-04T04:04:48.636890Z'
  support: supports
  summary: 'P0ABS5: UniProtKB reviewed (Swiss-Prot); DNA primase; genes [''dnaG''];
    loci [''b3066'', ''JW3038'']; taxon 83333; InterPro [''IPR016136'', ''IPR037068'',
    ''IPR019475'', ''IPR006295'', ''IPR013173'', ''IPR036977'', ''IPR030846'', ''IPR013264'',
    ''IPR050219'', ''IPR034151'', ''IPR006171'', ''IPR002694'']. Native annotations
    are distinct from newly inspected primary experiments.'
  snapshot_sha256: 3dd4cfacccc5ec8470c469ca2c8962c6ea0c433124507a5921eb70ab0c7aac9e
- evidence_id: micro-up-P0ACB0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ACB0.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P0ACB0.raw
  accessed_at: '2026-11-04T04:04:46.650448Z'
  support: supports
  summary: 'P0ACB0: UniProtKB reviewed (Swiss-Prot); Replicative DNA helicase DnaB;
    genes [''dnaB'']; loci [''b4052'', ''JW4012'']; taxon 83333; InterPro [''IPR003593'',
    ''IPR036185'', ''IPR007692'', ''IPR007694'', ''IPR007693'', ''IPR016136'', ''IPR027417''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: edebd0e1411d58b0f8593f28aec4b2a227356105e8ab65e8095652ff58c1c3ea
- evidence_id: micro-up-P25559
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P25559.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P25559.raw
  accessed_at: '2026-11-04T04:04:56.595846Z'
  support: supports
  summary: 'P25559: UniProtKB reviewed (Swiss-Prot); Sister chromatid cohesion protein
    DCC1; genes [''DCC1'']; loci [''YCL016C'', ''YCL16C'']; taxon 559292; InterPro
    [''IPR019128'']. Native annotations are distinct from newly inspected primary
    experiments.'
  snapshot_sha256: 50a48906aa61a282a8dea0ef8558efc5065eaf82877f919e17108c60e1a57ec9
- evidence_id: micro-up-P33895
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P33895.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P33895.raw
  accessed_at: '2026-11-04T04:04:50.695961Z'
  support: supports
  summary: 'P33895: UniProtKB reviewed (Swiss-Prot); Kinetochore protein NUF2; genes
    [''NUF2'']; loci [''YOL069W'']; taxon 559292; InterPro [''IPR005549'', ''IPR038275''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 571967574ce29a5f5b3a43ad0c65267df722a3e258d80aeb78fea83a2b7323fe
- evidence_id: micro-up-P36012
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P36012.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P36012.raw
  accessed_at: '2026-11-04T04:04:48.648541Z'
  support: supports
  summary: 'P36012: UniProtKB reviewed (Swiss-Prot); Histone H3-like centromeric protein
    CSE4; genes [''CSE4'']; loci [''YKL049C'', ''YKL262'']; taxon 559292; InterPro
    [''IPR007125'', ''IPR009072'', ''IPR000164'']. Native annotations are distinct
    from newly inspected primary experiments.'
  snapshot_sha256: bca7e7c2253768cc51d28557ea8967dd642ffbff3dff58274cecc9e8fae973f5
- evidence_id: micro-up-P38251
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38251.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38251.raw
  accessed_at: '2026-11-04T04:04:54.625815Z'
  support: supports
  summary: 'P38251: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit
    5; genes [''RFC5'']; loci [''YBR087W'', ''YBR0810'']; taxon 559292; InterPro [''IPR003593'',
    ''IPR008921'', ''IPR050238'', ''IPR027417'']. Native annotations are distinct
    from newly inspected primary experiments.'
  snapshot_sha256: bebaced0b8314c495257a26b5d1357bde108a903ac25fc337c51d4970294ff06
- evidence_id: micro-up-P38313
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38313.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38313.raw
  accessed_at: '2026-11-04T04:04:50.617774Z'
  support: supports
  summary: 'P38313: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit AME1;
    genes [''AME1'']; loci [''YBR211C'', ''YBR1458'']; taxon 559292; InterPro [''IPR048743''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 053d6d5cadc71a57b6b685c5ac036757f82d889c4efce071a4a694908c5e0d07
- evidence_id: micro-up-P38629
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38629.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38629.raw
  accessed_at: '2026-11-04T04:04:52.689886Z'
  support: supports
  summary: 'P38629: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit
    3; genes [''RFC3'']; loci [''YNL290W'', ''N0533'']; taxon 559292; InterPro [''IPR003593'',
    ''IPR003959'', ''IPR008921'', ''IPR050238'', ''IPR027417'', ''IPR013748'']. Native
    annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 057ded2799f8c2aaf4cd34a49b0bd062aae33e6e6aa9ab81ec59b7c7d74937dd
- evidence_id: micro-up-P38877
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38877.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P38877.raw
  accessed_at: '2026-11-04T04:04:57.602289Z'
  support: supports
  summary: 'P38877: UniProtKB reviewed (Swiss-Prot); Chromosome transmission fidelity
    protein 8; genes [''CTF8'']; loci [''YHR191C'']; taxon 559292; InterPro [''IPR018607''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 8207f0b46c1a2b1cf5bbc2a038840f091f1753eebe1f72d92c9d715a8dd4f44b
- evidence_id: micro-up-P40339
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40339.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P40339.raw
  accessed_at: '2026-11-04T04:04:53.802295Z'
  support: supports
  summary: 'P40339: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit
    4; genes [''RFC4'']; loci [''YOL094C'', ''O0923'']; taxon 559292; InterPro [''IPR003593'',
    ''IPR003959'', ''IPR008921'', ''IPR050238'', ''IPR027417'', ''IPR013748'', ''IPR047854''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 09609fcf78c540ff8073114b66b849691895e1fc7de9e81219d81dc51fcc35d7
- evidence_id: micro-up-P40348
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40348.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P40348.raw
  accessed_at: '2026-11-04T04:04:51.651878Z'
  support: supports
  summary: 'P40348: UniProtKB reviewed (Swiss-Prot); Replication factor C subunit
    2; genes [''RFC2'']; loci [''YJR068W'', ''J1808'']; taxon 559292; InterPro [''IPR003593'',
    ''IPR003959'', ''IPR008921'', ''IPR050238'', ''IPR027417'', ''IPR013748'', ''IPR047854''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: cd48db2abc9d05e4a2f8f7736b0aced77e8baa2465fb6a839d4f9e8ed95db94e
- evidence_id: micro-up-P40460
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P40460.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P40460.raw
  accessed_at: '2026-11-04T04:04:47.626088Z'
  support: supports
  summary: 'P40460: UniProtKB reviewed (Swiss-Prot); Kinetochore protein NDC80; genes
    [''NDC80'']; loci [''YIL144W'']; taxon 559292; InterPro [''IPR040967'', ''IPR005550'',
    ''IPR055260'', ''IPR038273'']. Native annotations are distinct from newly inspected
    primary experiments.'
  snapshot_sha256: e9118ff7804c75195f78434aabd4f7b07fe4678b12faf54aa90a012fede3f5a6
- evidence_id: micro-up-P49956
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P49956.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P49956.raw
  accessed_at: '2026-11-04T04:04:47.604198Z'
  support: supports
  summary: 'P49956: UniProtKB reviewed (Swiss-Prot); Chromosome transmission fidelity
    protein 18; genes [''CTF18'']; loci [''YMR078C'', ''YM9582.03C'']; taxon 559292;
    InterPro [''IPR003593'', ''IPR003959'', ''IPR027417'', ''IPR047854'']. P49956
    does not currently carry IPR053016; exact Ctf18 class metadata and reviewed ortholog
    membership are separately inspected, without asserting a nonexistent accession
    xref. Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 17fbd45ac56b77d7217359feda21a804a3db9d91e2bceb87b573c94bec6753c9
- evidence_id: micro-up-P53298
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53298.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-P53298.raw
  accessed_at: '2026-11-04T04:04:45.681967Z'
  support: supports
  summary: 'P53298: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit OKP1;
    genes [''OKP1'']; loci [''YGR179C'']; taxon 559292; InterPro []. Native annotations
    are distinct from newly inspected primary experiments.'
  snapshot_sha256: e286b14d37ffacdfdacead4d28a714fb2cd7647ebcccc49df73d642fe0756906
- evidence_id: micro-up-Q02732
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q02732.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-Q02732.raw
  accessed_at: '2026-11-04T04:04:45.761892Z'
  support: supports
  summary: 'Q02732: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit CTF19;
    genes [''CTF19'']; loci [''YPL018W'', ''LPB13W'']; taxon 559292; InterPro [''IPR063954'',
    ''IPR063963'']. Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 4300f75049f2449011c3e78557ed639585c8206f4ea707ce6abda1aaa5b6b62d
- evidence_id: micro-up-Q04477
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q04477.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-Q04477.raw
  accessed_at: '2026-11-04T04:04:51.646429Z'
  support: supports
  summary: 'Q04477: UniProtKB reviewed (Swiss-Prot); Kinetochore protein SPC24; genes
    [''SPC24'']; loci [''YMR117C'', ''YM9718.16C'']; taxon 559292; InterPro [''IPR013252'',
    ''IPR038066'']. Spc24 is the centromere-facing end of the outer Ndc80 attachment
    module; the grouped node does not assert every listed member directly contacts
    microtubules. Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: 7c4ad50bf5ae4e1eb7738038fdb2a60c4f3ba91ee1b8fd9f7484489ef732d559
- evidence_id: micro-up-Q06675
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q06675.json
  locator: Exact accession/status/product/gene/locus/taxon, relevant complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and evidence codes; InterPro links; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/up-Q06675.raw
  accessed_at: '2026-11-04T04:04:46.654802Z'
  support: supports
  summary: 'Q06675: UniProtKB reviewed (Swiss-Prot); Inner kinetochore subunit MCM21;
    genes [''MCM21'']; loci [''YDR318W'']; taxon 559292; InterPro [''IPR018464''].
    Native annotations are distinct from newly inspected primary experiments.'
  snapshot_sha256: a284987a228269755202e144975329d40045d32097395fa0a3b5efbc26dcd801
- evidence_id: micro-query-AME1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAME1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-AME1.raw
  accessed_at: '2026-11-04T04:05:17.399804Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P38313'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: 0d24b7575005296c4ba534d40d5e66dd54a2d6aebf6625ad1180ceb8ff885018
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAME1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:17.399804Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-CTF18
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF18+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-CTF18.raw
  accessed_at: '2026-11-04T04:05:06.760904Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P49956'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: a4ab5388befbeda39e461e4a30196937ca7bbfbb0d2aaecb7701a7fe07458a86
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF18+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:06.760904Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-CTF19
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF19+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-CTF19.raw
  accessed_at: '2026-11-04T04:05:05.996919Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''Q02732'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: a9a47e880c6ddf126c5a8cfc5e899ce09ebe7ebc7a00b39ff7594e40f4a32309
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF19+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:05.996919Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-CTF8
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF8+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-CTF8.raw
  accessed_at: '2026-11-04T04:05:22.772736Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P38877'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: 5f26e82ef1409a8fbf4006d2c55f5ef6f6ea1d272b7d9f8bb6abf00215a7fbc2
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF8+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:22.772736Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-DCC1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADCC1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-DCC1.raw
  accessed_at: '2026-11-04T04:05:11.819343Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P25559'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: e2e1ecc46110b84dd7b50f736495e29305f6dbd2a117b34aeea8d8abc069f4f4
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADCC1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:11.819343Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-MCM21
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMCM21+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-MCM21.raw
  accessed_at: '2026-11-04T04:05:15.807894Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''Q06675'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: a3cc24e2df5723fb6cec03e1893aaf4548a563624f8dc245d6c6e518e7334abd
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMCM21+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:15.807894Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-OKP1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AOKP1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-OKP1.raw
  accessed_at: '2026-11-04T04:05:15.076476Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P53298'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: cbe45d27fdfe19adae898e1527e55b3a9c8b4ecc618ec106ea301c3e7c94c4a3
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AOKP1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:15.076476Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-RFC2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC2.raw
  accessed_at: '2026-11-04T04:05:23.020458Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P40348'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: 5d37684d32d00b6803a2cbe7289849926576cd3f08cc74f6dd6ee2b3c1821068
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:23.020458Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-RFC3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC3+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC3.raw
  accessed_at: '2026-11-04T04:04:58.693937Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P38629'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: a84d7bf13eddb61707649c22403a1d9540d4585cd07d07bb31fcbd5f54cff2c3
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC3+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:04:58.693937Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-RFC4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC4+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC4.raw
  accessed_at: '2026-11-04T04:05:10.943832Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P40339'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: e4ac27ef43308dc3dd4c47939cb4856e61e23e412f8815e785cfb8d758e80a5c
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC4+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:10.943832Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-RFC5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC5+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-RFC5.raw
  accessed_at: '2026-11-04T04:04:59.979713Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P38251'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: 7cfa80c9ae09adeac609a00eb5e3ddcecb79fc26d7ce7848ce2f6f772cfcaabb
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC5+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:04:59.979713Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-dnaB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaB+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-dnaB.raw
  accessed_at: '2026-11-04T04:05:07.844321Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P0ACB0'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: a82408ab2f13701ec5f77df653333e6715273c2cc3fcfad9fe06ad2a5cccb089
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaB+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:07.844321Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-query-dnaG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaG+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=100
  locator: Exact reviewed primary-gene/taxon query and complete returned identities;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/query-dnaG.raw
  accessed_at: '2026-11-04T04:05:32.641183Z'
  support: supports
  summary: 'Current response contains 1 accession(s): [''P0ABS5'']. All13 own exact
    gene queries are singletons; this is a current bounded identity check, not proof
    of historical query results or causal membership.'
  snapshot_sha256: 8c4d7768ca4c12de32448cc28f5fc09c1fdb9401446fa05fc5cc991d07100e5a
  search_scope: UniProtKB REST; literal request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AdnaG+AND+organism_id%3A83333+AND+reviewed%3Atrue&format=json&size=100;
    retrieved 2026-11-04T04:05:32.641183Z; size100, complete returned page inspected,
    no returned pagination link; exact reviewed gene and reference taxon only, not
    every synonym/taxon or past database state.
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Exact taxon ID, scientific name, rank and immediate parent; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-4932.raw
  accessed_at: '2026-11-04T04:04:53.561500Z'
  support: supports
  summary: 'Native taxon 4932 is Saccharomyces cerevisiae; rank species; parent {"scientificName":
    "Saccharomyces", "taxonId": 4930}. Protein reference strains are not silently
    substituted for every experiment organism.'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
- evidence_id: micro-tax-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Exact taxon ID, scientific name, rank and immediate parent; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-559292.raw
  accessed_at: '2026-11-04T04:04:57.602223Z'
  support: supports
  summary: 'Native taxon 559292 is Saccharomyces cerevisiae (strain ATCC 204508 /
    S288c); rank strain; parent {"scientificName": "Saccharomyces cerevisiae", "commonName":
    "Baker''s yeast", "taxonId": 4932}. Protein reference strains are not silently
    substituted for every experiment organism.'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
- evidence_id: micro-tax-562
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/562.json
  locator: Exact taxon ID, scientific name, rank and immediate parent; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-562.raw
  accessed_at: '2026-11-04T04:05:04.898243Z'
  support: supports
  summary: 'Native taxon 562 is Escherichia coli; rank species; parent {"scientificName":
    "Escherichia", "taxonId": 561}. Protein reference strains are not silently substituted
    for every experiment organism.'
  snapshot_sha256: 20aa358053d2fae1e2cd74636ed5aca1efbc372e5b8bcfdb10d3fa80be6789a1
- evidence_id: micro-tax-83333
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/83333.json
  locator: Exact taxon ID, scientific name, rank and immediate parent; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/tax-83333.raw
  accessed_at: '2026-11-04T04:04:59.610036Z'
  support: supports
  summary: 'Native taxon 83333 is Escherichia coli (strain K12); rank strain; parent
    {"scientificName": "Escherichia coli", "taxonId": 562}. Protein reference strains
    are not silently substituted for every experiment organism.'
  snapshot_sha256: 83c59ae9694d1874b8a175d7ce7608f77f5688d35adf307a0859dbb20f9e1c17
- evidence_id: micro-go-0000228
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0000228.raw
  accessed_at: '2026-11-04T04:04:52.465034Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0000228", "name":
    "nuclear chromosome", "isObsolete": false, "definition": {"text": "A chromosome
    that encodes the nuclear genome and is found in the nucleus of a eukaryotic cell
    during the cell cycle phases when the nucleus is intact."}, "synonyms": [{"name":
    "nuclear interphase chromosome", "type": "narrow"}], "relevant_children": [{"id":
    "GO:0000817", "relation": "part_of"}]}]. Generic/core versus narrower protein-only
    complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is
    not imported into COMA.'
  snapshot_sha256: f6f4e35b7013c8315843d2ce0efac17e1256106ac8af95f997ba842d01f444ee
- evidence_id: micro-go-0000776
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000776
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0000776.raw
  accessed_at: '2026-11-04T04:04:52.371194Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0000776", "name":
    "kinetochore", "isObsolete": false, "definition": {"text": "A multisubunit complex
    that is located at the centromeric region of DNA and provides an attachment point
    for the spindle microtubules."}, "synonyms": [{"name": "condensed chromosome kinetochore",
    "type": "exact"}, {"name": "condensed nuclear chromosome kinetochore", "type":
    "exact"}, {"name": "NMS complex", "type": "narrow"}], "relevant_children": [{"id":
    "GO:0000817", "relation": "part_of"}]}]. Generic/core versus narrower protein-only
    complex and is_a versus parthood are distinguished; source synonym Mcm1 typo is
    not imported into COMA.'
  snapshot_sha256: 1b1d92f2f3ec584f7fe8d61021ebb433586609a130c97e9ec37a07cfda864c76
- evidence_id: micro-go-0000817
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000817
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0000817.raw
  accessed_at: '2026-11-04T04:04:52.303860Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0000817", "name":
    "COMA complex", "isObsolete": false, "definition": {"text": "A kinetochore multiprotein
    complex that bridges the subunits that are in contact with centromeric DNA and
    the subunits bound to microtubules during kinetochore assembly. In yeast, consists
    of Ctf19p, Okp1p, Mcm21p, and Ame1p.", "xrefs": [{"dbCode": "PMID", "dbId": "14633972"}]},
    "synonyms": [{"name": "Ctf19p-Okp1p-Mcm1p-Ame1p complex", "type": "exact"}], "relevant_children":
    []}]. Generic/core versus narrower protein-only complex and is_a versus parthood
    are distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: 9b86d651fde1d9304d9b028ad7358596c15000c1500f1d24a19603085f8f36b1
- evidence_id: micro-go-0003689
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003689
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0003689.raw
  accessed_at: '2026-11-04T04:04:53.317337Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0003689", "name":
    "DNA clamp loader activity", "isObsolete": false, "definition": {"text": "Facilitating
    the opening of the ring structure of the PCNA complex, or any of the related sliding
    clamp complexes, and their closing around the DNA duplex, driven by ATP hydrolysis.",
    "xrefs": [{"dbCode": "PMID", "dbId": "16082778"}]}, "synonyms": [{"name": "DNA
    clamp loading ATPase activity", "type": "exact"}, {"name": "DNA-protein loading
    ATPase activity", "type": "related"}, {"name": "PCNA loading activity", "type":
    "narrow"}, {"name": "PCNA loading complex activity", "type": "narrow"}, {"name":
    "protein-DNA loading ATPase activity", "type": "related"}], "relevant_children":
    []}]. Generic/core versus narrower protein-only complex and is_a versus parthood
    are distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: f123eb12d15e9440d784ac0cef214c66c2920ac3fa33e908178e8da7c454a5b8
- evidence_id: micro-go-0006269
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006269
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0006269.raw
  accessed_at: '2026-11-04T04:04:53.087904Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0006269", "name":
    "DNA replication, synthesis of primer", "isObsolete": false, "definition": {"text":
    "The synthesis of a short nucleotide polymer using one strand of unwound DNA as
    a template. The product is usually a RNA molecule between 4-15 nucleotides long
    that provides a free 3''-OH that can be extended by DNA-directed DNA polymerases.
    In certain conditions, for example in response to DNA damage, some primases synthesize
    a DNA primer.", "xrefs": [{"dbCode": "PMID", "dbId": "11395402"}, {"dbCode": "PMID",
    "dbId": "38203225"}, {"dbCode": "PMID", "dbId": "38492718"}]}, "synonyms": [{"name":
    "DNA priming", "type": "narrow"}, {"name": "DNA replication, synthesis of DNA
    primer", "type": "narrow"}, {"name": "DNA replication, synthesis of RNA primer",
    "type": "narrow"}, {"name": "replication priming", "type": "related"}], "relevant_children":
    []}]. Generic/core versus narrower protein-only complex and is_a versus parthood
    are distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: e24540cdcb3dfc5c3053d63a84321f7fa4e1b10324b9088235aa51b2d3e39b79
- evidence_id: micro-go-0007062
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0007062
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0007062.raw
  accessed_at: '2026-11-04T04:04:53.533153Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0007062", "name":
    "sister chromatid cohesion", "isObsolete": false, "definition": {"text": "The
    cell cycle process in which the sister chromatids of a replicated chromosome become
    tethered to each other.", "xrefs": [{"dbCode": "ISBN", "dbId": "0815316194"}]},
    "synonyms": [{"name": "cohesion-mediated DNA tethering", "type": "exact"}], "relevant_children":
    []}]. Generic/core versus narrower protein-only complex and is_a versus parthood
    are distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: fd053fb038b85d71d85bff11f35e80132deb2d4694c57e646364d0e10bd6a356
- evidence_id: micro-go-0031390
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031390
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0031390.raw
  accessed_at: '2026-11-04T04:04:53.220627Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0031390", "name":
    "Ctf18 RFC-like complex", "isObsolete": false, "definition": {"text": "A heptameric
    complex related to replication factor C, which loads the DNA polymerase processivity
    factor proliferating cell nuclear antigen (PCNA) onto DNA and plays a vital role
    in chromosome cohesion. In Saccharomyces the subunits are known as Ctf18p, Rfc2p,
    Rfc3p, Rfc4p, Rfc5p, Dcc1p, and Ctf8p.", "xrefs": [{"dbCode": "PMID", "dbId":
    "14614842"}]}, "synonyms": [{"name": "Ctf18-RFC", "type": "exact"}, {"name": "Ctf18-RLC",
    "type": "exact"}, {"name": "RFC (Ctf18)", "type": "exact"}], "relevant_children":
    []}]. Generic/core versus narrower protein-only complex and is_a versus parthood
    are distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: b57cfa4de9b35cc87a55bfb2549a426ea6135d170c0b7d7a7d46087d4eadd752
- evidence_id: micro-go-0140513
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140513
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-0140513.raw
  accessed_at: '2026-11-04T04:04:52.286870Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:0140513", "name":
    "nuclear protein-containing complex", "isObsolete": false, "definition": {"text":
    "A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids,
    carbohydrates or lipids, in which at least one component is a protein and the
    constituent parts function together in the nucleus."}, "synonyms": [{"name": "nuclear
    complex", "type": "exact"}], "relevant_children": [{"id": "GO:0031390", "relation":
    "is_a"}, {"id": "GO:0000817", "relation": "is_a"}]}]. Generic/core versus narrower
    protein-only complex and is_a versus parthood are distinguished; source synonym
    Mcm1 typo is not imported into COMA.'
  snapshot_sha256: 61c31928c6fb33a97da0bafa0beafb5392a27dac53b617f92ba08fb5cf0511b7
- evidence_id: micro-go-1990077
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990077
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990077.raw
  accessed_at: '2026-11-04T04:04:52.927851Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:1990077", "name":
    "primosome complex", "isObsolete": false, "definition": {"text": "Any of a family
    of protein complexes that form at the origin of replication or stalled replication
    forks and function in replication primer synthesis in all organisms. Early complexes
    initiate double-stranded DNA unwinding. The core unit consists of a replicative
    helicase and a primase. The helicase further unwinds the DNA and recruits the
    polymerase machinery. The primase synthesizes RNA primers that act as templates
    for complementary stand replication by the polymerase machinery. The primosome
    contains a number of associated proteins and protein complexes and contributes
    to the processes of replication initiation, lagging strand elongation, and replication
    restart.", "xrefs": [{"dbCode": "PMID", "dbId": "21856207"}]}, "synonyms": [{"name":
    "primosome", "type": "exact"}], "relevant_children": [{"id": "GO:1990098", "relation":
    "is_a"}]}]. Generic/core versus narrower protein-only complex and is_a versus
    parthood are distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: 39e7c5542064bdf7ca68df76b5b42c8671196b04198bdef4a2b74fe51729070f
- evidence_id: micro-go-1990098
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990098
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990098.raw
  accessed_at: '2026-11-04T04:04:52.590146Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:1990098", "name":
    "core primosome complex", "isObsolete": false, "definition": {"text": "A protein-DNA
    complex containing at least one DNA helicase and one primase. Can also contain
    associated proteins. The helicase component continues to unwind the double-stranded
    DNA (dsDNA) and the primase component synthesizes a RNA primer during initiation
    or restart of replication.", "xrefs": [{"dbCode": "PMID", "dbId": "21856207"}]},
    "synonyms": [{"name": "core primosome", "type": "exact"}], "relevant_children":
    [{"id": "GO:1990156", "relation": "part_of"}]}]. Generic/core versus narrower
    protein-only complex and is_a versus parthood are distinguished; source synonym
    Mcm1 typo is not imported into COMA.'
  snapshot_sha256: ae60a99dc77b90e625bf04f7ab8446609a6efb8c41e74583cbbcd93911c6f282
- evidence_id: micro-go-1990099
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990099
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990099.raw
  accessed_at: '2026-11-04T04:04:52.940925Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:1990099", "name":
    "pre-primosome complex", "isObsolete": false, "definition": {"text": "Any of the
    protein-DNA complexes that contain a DNA helicase and associated protein(s) at
    the origin of replication, and build up to assembling the core primosome. The
    associated protein(s) chaperone the helicase to the DNA, and assembly of the pre-primosome
    is essential for the initiation or restart of replication. Pre-primosome complexes
    lack a primase component.", "xrefs": [{"dbCode": "PMID", "dbId": "18179598"},
    {"dbCode": "PMID", "dbId": "20129058"}, {"dbCode": "PMID", "dbId": "8663105"}]},
    "synonyms": [{"name": "pre-priming complex", "type": "exact"}, {"name": "pre-primosome",
    "type": "exact"}, {"name": "preprimosome", "type": "exact"}, {"name": "preprimosome
    complex", "type": "exact"}, {"name": "pre-replication complex", "type": "related"},
    {"name": "prereplication complex", "type": "exact"}], "relevant_children": []}].
    Generic/core versus narrower protein-only complex and is_a versus parthood are
    distinguished; source synonym Mcm1 typo is not imported into COMA.'
  snapshot_sha256: 4a9c1b38556a834c6ad45ffe49977b2acb64a18627c9bcd9ac75c84372602053
- evidence_id: micro-go-1990156
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990156
  locator: Active term definition, exact synonyms/comments and relevant typed child
    links; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/go-1990156.raw
  accessed_at: '2026-11-04T04:04:53.023551Z'
  support: supports
  summary: 'Native requested term metadata inspected: [{"id": "GO:1990156", "name":
    "DnaB-DnaG complex", "isObsolete": false, "definition": {"text": "A protein complex
    containing homohexameric DnaB helicase, and DnaG (a primase). Facilitates the
    unwinding of double-stranded DNA and the synthesis of RNA primer sequences during
    DNA replication and repair in Prokaryotes.", "xrefs": [{"dbCode": "PMID", "dbId":
    "14557266"}]}, "synonyms": [{"name": "DnaB-DnaG primosome complex", "type": "related"}],
    "relevant_children": []}]. Generic/core versus narrower protein-only complex and
    is_a versus parthood are distinguished; source synonym Mcm1 typo is not imported
    into COMA.'
  snapshot_sha256: 73516b2bd005face6541af32d31d4e68385dbb033bc47b677ae4c52bd8cec9d8
- evidence_id: micro-ipr-IPR018464
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018464/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR018464.raw
  accessed_at: '2026-11-04T04:04:49.261755Z'
  support: supports
  summary: 'Native IPR018464: name {''name'': ''Centromere protein O'', ''short'':
    ''CENP-O''}; type family; description curation flags [{}]. Full CENP-O family
    explicitly includes yeast Mcm21 and has the Q06675 xref; exact class candidate.'
  snapshot_sha256: 96ad879101de27e1856805668c39fea5f0612e63b18cbb014bb0c0e67d69c3d1
- evidence_id: micro-ipr-IPR048743
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048743/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR048743.raw
  accessed_at: '2026-11-04T04:04:49.859340Z'
  support: context_only
  summary: 'Native IPR048743: name {''name'': ''Inner kinetochore subunit AME1'',
    ''short'': ''AME1''}; type domain; description curation flags [{}]. AME1 is a
    domain annotation, not automatically an exact whole-protein family.'
  snapshot_sha256: 4703e3109b23c0469085fbfc9953892e015e27831b1dcf085fb61c4139bc9c52
- evidence_id: micro-ipr-IPR007692
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007692/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR007692.raw
  accessed_at: '2026-11-04T04:04:50.470150Z'
  support: context_only
  summary: 'Native IPR007692: name {''name'': ''DNA helicase, DnaB type'', ''short'':
    ''DNA_helicase_DnaB''}; type family; description curation flags [{}]. DnaB family
    is a valid E.coli candidate but narrower than generic replicative helicase.'
  snapshot_sha256: 88b9a5d41c0b3d6be01e7510bcdc6f5b03d5f0de15075277d153421c33818e10
- evidence_id: micro-ipr-IPR006295
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006295/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR006295.raw
  accessed_at: '2026-11-04T04:04:51.151263Z'
  support: context_only
  summary: 'Native IPR006295: name {''name'': ''DNA primase, DnaG'', ''short'': ''DNA_primase_DnaG''};
    type domain; description curation flags [{}, {}]. DnaG-related domain is not the
    generic archaeal/eukaryotic/bacterial primase class.'
  snapshot_sha256: 24e4589413c8efb43f18433fac55d19aa80d3b100e8779daeff1ac983314d6d3
- evidence_id: micro-ipr-IPR050219
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050219/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR050219.raw
  accessed_at: '2026-11-04T04:04:51.216845Z'
  support: context_only
  summary: 'Native IPR050219: name {''name'': ''DnaG Primase'', ''short'': ''DnaG_primase''};
    type family; description curation flags [{}]. DnaG family is narrower than generic
    DNA primase. Unchecked generated prose, including irrelevant exosome wording,
    is excluded from biological support.'
  snapshot_sha256: 1fcc18624f8fa54ab1f5a0e7586855160ecaa26b28ae4f13e725103b6a8c8ee7
- evidence_id: micro-ipr-IPR053016
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR053016/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR053016.raw
  accessed_at: '2026-11-04T04:04:51.305783Z'
  support: supports
  summary: 'Native IPR053016: name {''name'': ''Chromosome transmission fidelity protein
    18'', ''short'': ''CTF18''}; type family; description curation flags [{}]. CTF18
    family PTHR46765 identity is considered separately from unchecked generated description;
    generated biological assertions are not evidence.'
  snapshot_sha256: d1d6815cae804e3055ebc8ef4c8172cda80d288d20e7adc5822e9fbd84508d7d
- evidence_id: micro-ipr-IPR019128
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019128/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR019128.raw
  accessed_at: '2026-11-04T04:04:51.769986Z'
  support: supports
  summary: 'Native IPR019128: name {''name'': ''Sister chromatid cohesion protein
    Dcc1'', ''short'': ''Dcc1''}; type family; description curation flags [{}]. Exact
    Dcc1 or Ctf8 family metadata and current native protein xrefs support class identity.'
  snapshot_sha256: fd649e6f522442733dee8c7a873a40ddebe01605c22727dd96d58c693f5581fd
- evidence_id: micro-ipr-IPR018607-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018607/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR018607-retry.raw
  accessed_at: '2026-11-04T04:05:43.097965Z'
  support: supports
  summary: 'Native IPR018607: name {''name'': ''Chromosome transmission fidelity protein
    8'', ''short'': ''Ctf8''}; type family; description curation flags [{}]. Exact
    Dcc1 or Ctf8 family metadata and current native protein xrefs support class identity.'
  snapshot_sha256: cd1fcec19c09b0c0149e1a9934d739fe8a528dbc220a0a6642a67fdfc03c3516
- evidence_id: micro-ipr-IPR050238-retry
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/
  locator: Complete native metadata/type/name, integrated signatures and description
    flags; full description read for scope, generated prose excluded; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ipr-IPR050238-retry.raw
  accessed_at: '2026-11-04T04:05:43.080341Z'
  support: context_only
  summary: 'Native IPR050238: name {''name'': ''DNA Replication and Repair Clamp Loader
    Complex'', ''short'': ''DNA_Rep/Repair_Clamp_Loader''}; type family; description
    curation flags [{}]. Shared clamp-loader family does not distinguish RFC2–5 paralogues;
    unchecked generated prose not used as biological evidence.'
  snapshot_sha256: 20cc681dc2b5aa75e096f21d298105d7ac05cc910f786be9e1f63ae05a72dbc0
- evidence_id: micro-family-CTF18
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR053016+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name
  locator: All returned exact reviewed member identities; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/family-CTF18.raw
  accessed_at: '2026-11-04T04:05:08.797046Z'
  support: supports
  summary: 'Five reviewed ortholog entries support the named Ctf18 family identity:
    [{''accession'': ''Q8WVB6'', ''name'': ''Chromosome transmission fidelity protein
    18 homolog'', ''taxon'': 9606}, {''accession'': ''Q8BIW9'', ''name'': ''Chromosome
    transmission fidelity protein 18 homolog'', ''taxon'': 10090}, {''accession'':
    ''Q9USQ1'', ''name'': ''Chromosome transmission fidelity protein 18'', ''taxon'':
    284812}, {''accession'': ''Q8IQ05'', ''name'': ''Chromosome transmission fidelity
    protein 18 homolog'', ''taxon'': 7227}, {''accession'': ''Q6NU40'', ''name'':
    ''Chromosome transmission fidelity protein 18 homolog'', ''taxon'': 8355}]. This
    query does not say P49956 currently carries that xref and does not prove biological
    assembly.'
  snapshot_sha256: 4899d18d633743f5a948e97278ee99912cd2af714394decc935ec29caac43671
  search_scope: UniProtKB exact xref:interpro-IPR053016 AND reviewed:true; request
    https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR053016+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name;
    2026-11-04T04:05:08.797046Z; size100, all five returned entries read, one complete
    page; not all unreviewed proteins or sequence reanalysis.
- evidence_id: micro-pmid-10323865
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-10323865.raw
  accessed_at: '2026-11-04T04:04:54.181611Z'
  support: supports
  summary: 'MED10323865: A putative protein complex consisting of Ctf19, Mcm21, and
    Okp1 represents a missing link in the budding yeast kinetochore.; DOI 10.1101/gad.13.9.1140.
    Complete primary study abstract read. No full body is certified by this metadata
    row; detailed source reading is separately enumerated.'
  snapshot_sha256: a1f5213611e7ba1679d682c8a9bc0cf7a04620ed082252b043d09ac94090d673
- evidence_id: micro-pmid-11389843
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11389843+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-11389843.raw
  accessed_at: '2026-11-04T04:04:54.797353Z'
  support: supports
  summary: 'MED11389843: Identification of RFC(Ctf18p, Ctf8p, Dcc1p): an alternative
    RFC complex required for sister chromatid cohesion in S. cerevisiae.; DOI 10.1016/s1097-2765(01)00254-4.
    Complete primary study abstract read. No full body is certified by this metadata
    row; detailed source reading is separately enumerated.'
  snapshot_sha256: f54addbf5314fcad1bfc5cde3cad5084b8003fb3a2a946ed970ebb5cb0fb9cca
- evidence_id: micro-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-14562095.raw
  accessed_at: '2026-11-04T04:04:54.439267Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.;
    DOI 10.1038/nature02026. Complete primary study abstract read. No full body is
    certified by this metadata row; detailed source reading is separately enumerated.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: micro-pmid-14614842
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14614842+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-14614842.raw
  accessed_at: '2026-11-04T04:04:55.065336Z'
  support: supports
  summary: 'MED14614842: Genome stability: a new member of the RFC family.; DOI 10.1016/j.cub.2003.10.048.
    Complete secondary review abstract read. No full body is certified by this metadata
    row; detailed source reading is separately enumerated.'
  snapshot_sha256: ce96104222d38cccd55e0d12af1caee12799a9263fa40a69bf95b10ac3556041
- evidence_id: micro-pmid-14633972
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14633972+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-14633972.raw
  accessed_at: '2026-11-04T04:04:53.941537Z'
  support: supports
  summary: 'MED14633972: Hierarchical assembly of the budding yeast kinetochore from
    multiple subcomplexes.; DOI 10.1101/gad.1144403. Complete primary study abstract
    read. No full body is certified by this metadata row; detailed source reading
    is separately enumerated.'
  snapshot_sha256: 648ba371eb6387a4ba38a1447a93a385bb1b7974f0721aa730b12f047a352468
- evidence_id: micro-pmid-21856207
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21856207+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-21856207.raw
  accessed_at: '2026-11-04T04:04:54.753257Z'
  support: supports
  summary: 'MED21856207: Replication initiation at the Escherichia coli chromosomal
    origin.; DOI 10.1016/j.cbpa.2011.07.016. Complete secondary review abstract read.
    No full body is certified by this metadata row; detailed source reading is separately
    enumerated.'
  snapshot_sha256: 8e8042a6562a27293db896a9f372196ea05a069d6d507da92610cc8a8ae926c6
- evidence_id: micro-pmid-23908374
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A23908374+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-23908374.raw
  accessed_at: '2026-11-04T04:04:54.133128Z'
  support: supports
  summary: 'MED23908374: The composition, functions, and regulation of the budding
    yeast kinetochore.; DOI 10.1534/genetics.112.145276. Complete secondary review
    abstract read. No full body is certified by this metadata row; detailed source
    reading is separately enumerated.'
  snapshot_sha256: 2a804a9740e0a5e148780a17aa25e487db8f14823bf4cc2b216c0d7768ad3363
- evidence_id: micro-pmid-29046335
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&format=json&resultType=core&pageSize=25
  locator: Complete MED identity/title/authors/date/DOI and entire deposited abstract;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/pmid-29046335.raw
  accessed_at: '2026-11-04T04:04:54.571010Z'
  support: supports
  summary: 'MED29046335: Molecular basis for inner kinetochore configuration through
    RWD domain-peptide interactions.; DOI 10.15252/embj.201796636. Complete primary
    study abstract read. No full body is certified by this metadata row; detailed
    source reading is separately enumerated.'
  snapshot_sha256: d717c792f19e86311fade7b6d9e8fd4d86fd7995ed0cd5ddfbe4deaf57391085
- evidence_id: micro-schmitzberger2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5709738.1/PMC5709738.1.xml
  locator: Genuine JATS abstract/Introduction sec1; Results sec3,4,6,11,12; Discussion
    sec15,16; Methods sec19,30,31,32; Figures1,2,7,8 text captions. No pixels/EV6
    strain table/raw data; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/schmitzberger2017-jats.raw
  accessed_at: '2026-11-04T04:05:24.688514Z'
  support: supports
  summary: K.lactis recombinant interface/truncation work is distinct from native
    S.cerevisiae Okp1Δ325–337 co-IP/localization. Native Ctf19 co-IP and centromeric
    Ctf19/Mcm21 signals are lost while Ame1/MIND/outer signals remain; near-normal
    vegetative growth does not erase this physical-association phenotype. Co-IP Methods
    use30°C cultures; S288C-derived unless specified exceptions in unread EV6. Not
    a universal viability/assembly claim.
  snapshot_sha256: ef185d0000359affb5734dd752fca64de70549007d12f7391c3fd83e318f7033
- evidence_id: micro-kaguni2011-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3189269.1/PMC3189269.1.xml
  locator: Genuine secondary review JATS Introduction S1; DnaB S5/DnaC S6; loading
    S9; initiation checkpoint S10; elongation S11; Conclusions S12. Other sections,
    pixels and cited primary experiments not read; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/kaguni2011-jats.raw
  accessed_at: '2026-11-04T04:05:24.317670Z'
  support: context_only
  summary: Review synthesizes E.coli oriC DnaA-dependent DnaB/DnaC loading, prepriming
    then DnaG primer formation/DnaC release, and transient repeated DnaG association
    in elongation. This supports bounded canonical background, not a new experiment,
    universal generic stoichiometry, or individual component formation necessity.
  snapshot_sha256: b92fcbf186b08bab9d5d0cd448b52a81f65fbbc71639605313e642c7dcf2cc0c
- evidence_id: micro-dewulf2003-legacy-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/?_escaped_fragment_=
  locator: Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-legacy.raw
  accessed_at: '2026-11-04T04:04:45.222721Z'
  support: context_only
  summary: HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result
    or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete
    fresh abstract and independent Schmitzberger primary body are separately inspected.
  snapshot_sha256: 17a4f64482d558f1bc2098a69f2c7367edf2711e647b42e6df875a723cebfb0f
- evidence_id: micro-dewulf2003-canonical-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/
  locator: Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-canonical.raw
  accessed_at: '2026-11-04T04:05:24.166306Z'
  support: context_only
  summary: HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result
    or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete
    fresh abstract and independent Schmitzberger primary body are separately inspected.
  snapshot_sha256: cf6b1f29a83443dad43fd02d8e159dd24b0186d8c08499be731e2e7cdd636d87
- evidence_id: micro-dewulf2003-numeric-access
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/289150/
  locator: Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-numeric.raw
  accessed_at: '2026-11-04T04:05:42.772923Z'
  support: context_only
  summary: HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result
    or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete
    fresh abstract and independent Schmitzberger primary body are separately inspected.
  snapshot_sha256: 7aa1342242db71eadb78137eeacb1dc5340327b0a66af79e5d68a61989896f7f
- evidence_id: micro-dewulf2003-jats-access
  kind: validation
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC289150.1/PMC289150.1.xml
  locator: Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-jats.raw
  accessed_at: '2026-11-04T04:05:24.046511Z'
  support: context_only
  summary: HTTP404; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result
    or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete
    fresh abstract and independent Schmitzberger primary body are separately inspected.
  snapshot_sha256: 127bf6102063eb289af40ac0295ffd85c915a0e34936c705494dd4c060851acb
- evidence_id: micro-dewulf2003-biocc-access
  kind: validation
  reference: https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/PMC289150/unicode
  locator: Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-biocc.raw
  accessed_at: '2026-11-04T04:05:42.883477Z'
  support: context_only
  summary: HTTP200; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result
    or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete
    fresh abstract and independent Schmitzberger primary body are separately inspected.
  snapshot_sha256: 478f38e0765ee9c406831bb2fc27e8019ac5227c20c6b28ca0de582d8449354a
- evidence_id: micro-dewulf2003-pdf-access
  kind: validation
  reference: https://genesdev.cshlp.org/content/17/23/2902.full.pdf
  locator: Actual response access diagnostic /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/dewulf2003-pdf.raw
  accessed_at: '2026-11-04T04:05:42.680096Z'
  support: context_only
  summary: HTTP403; terminal routes returned reCAPTCHA, absent S3 object, BioC no-result
    or publisher403. No DeWulf Results sec4/Methods full-body reread is claimed. Complete
    fresh abstract and independent Schmitzberger primary body are separately inspected.
  snapshot_sha256: 140692abcc9a3a8b987473887bcc6f6b3e6b53b154e0290207967dd987cb39ff
- evidence_id: micro-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Complete official organism/dataset catalogue response; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T04:05:08.101060Z'
  support: supports
  summary: All20 organism rows inspected. E.coli has precise1k and other named datasets;
    no S.cerevisiae/yeast matching host occurs in this snapshot. Catalogue no-match
    is not biological absence; no unrelated bacterial proxy substitutes for COMA/Ctf18.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB official GET /api/datasets, complete returned20 organism
    rows; 2026-11-04T04:05:08.101060Z; no pagination/truncation; exact natural-host
    names/keys checked, no future/unlisted coverage claim.
- evidence_id: micro-ecoli-meta
  kind: database
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/meta
  locator: Complete selected e_coli/precise1k dataset metadata; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-meta.raw
  accessed_at: '2026-11-04T04:05:43.413569Z'
  support: context_only
  summary: 'Selected precise1k includes BW25113,DGF-298,GMOS,MG1655,W3110: five strains,1035
    samples,201 modules,4257 genes. K-12 is reference-organism context, not an exact
    single-strain experiment match; source publication metadata does not imply its
    full-body reading.'
  snapshot_sha256: 6cd60b3e363a11c95c2b5b1d160fe360687c0a680a5b95c18c6c76e7c5d99865
- evidence_id: micro-ecoli-modules
  kind: search
  reference: https://imodulondb.org/api/datasets/e_coli/precise1k/imodulons
  locator: Complete selected module list and metadata; retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-modules.raw
  accessed_at: '2026-11-04T04:05:42.673036Z'
  support: context_only
  summary: All201 module records returned for e_coli/precise1k inspected for bounded
    dataset/module context; downstream gene results define actual hits, not module-title
    speculation.
  snapshot_sha256: c9f7564cc9fa212686b00f75d35b5438d9d8660066eada141b263e580634e26d
  search_scope: iModulonDB e_coli/precise1k /imodulons list; complete201 rows at 2026-11-04T04:05:42.673036Z;
    no other E.coli dataset or experimental condition explored.
- evidence_id: micro-ecoli-b4052
  kind: search
  reference: https://imodulondb.org/api/genes/b4052/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete201 gene/module membership rows, actual threshold/in_imodulon fields;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-b4052.raw
  accessed_at: '2026-11-04T04:05:42.618868Z'
  support: context_only
  summary: b4052/dnaB has no above-threshold membership among returned201 modules.
    This is computational expression context, not physical association, assembly necessity,
    localization or causal regulation.
  snapshot_sha256: 64621a51f7ebc4c85af52da8de15f02c918736f01272f2b04ffdd82e306191ca
  search_scope: iModulonDB selected e_coli/precise1k gene=b4052, request https://imodulondb.org/api/genes/b4052/imodulons?organism=e_coli&dataset=precise1k,
    2026-11-04T04:05:42.618868Z; all201 returned rows inspected; no extrapolation
    to other datasets, untested conditions, biological absence or past query states.
- evidence_id: micro-ecoli-b3066
  kind: search
  reference: https://imodulondb.org/api/genes/b3066/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete201 gene/module membership rows, actual threshold/in_imodulon fields;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-b3066.raw
  accessed_at: '2026-11-04T04:05:42.395429Z'
  support: context_only
  summary: b3066/dnaG crosses only module10 Nucleotide Stress (weight0.082144995>threshold0.077432849).
    This is computational expression context, not physical association, assembly necessity,
    localization or causal regulation.
  snapshot_sha256: 56718b73babc8d2b2edeb3c9f4a36f2d3f56915c3106f6f90ce4310d4f623fc3
  search_scope: iModulonDB selected e_coli/precise1k gene=b3066, request https://imodulondb.org/api/genes/b3066/imodulons?organism=e_coli&dataset=precise1k,
    2026-11-04T04:05:42.395429Z; all201 returned rows inspected; no extrapolation
    to other datasets, untested conditions, biological absence or past query states.
- evidence_id: micro-ecoli-JW4012
  kind: search
  reference: https://imodulondb.org/api/genes/JW4012/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete201 gene/module membership rows, actual threshold/in_imodulon fields;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-JW4012.raw
  accessed_at: '2026-11-04T04:05:42.602453Z'
  support: context_only
  summary: JW4012 alias request returns no above-threshold membership; alias indexing
    noncoverage is not gene absence. This is computational expression context, not
    physical association, assembly necessity, localization or causal regulation.
  snapshot_sha256: 1fa903e5c1f40ad5f2f4da105faee4c1b214cc5b3e15b2377180c120f622400c
  search_scope: iModulonDB selected e_coli/precise1k gene=JW4012, request https://imodulondb.org/api/genes/JW4012/imodulons?organism=e_coli&dataset=precise1k,
    2026-11-04T04:05:42.602453Z; all201 returned rows inspected; no extrapolation
    to other datasets, untested conditions, biological absence or past query states.
- evidence_id: micro-ecoli-JW3038
  kind: search
  reference: https://imodulondb.org/api/genes/JW3038/imodulons?organism=e_coli&dataset=precise1k
  locator: Complete201 gene/module membership rows, actual threshold/in_imodulon fields;
    retained response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-JW3038.raw
  accessed_at: '2026-11-04T04:05:42.664841Z'
  support: context_only
  summary: JW3038 alias request returns no above-threshold membership; alias indexing
    noncoverage is not gene absence. This is computational expression context, not
    physical association, assembly necessity, localization or causal regulation.
  snapshot_sha256: a00f08dc98baf2c732c11000fe6ffaeca10680fbd6884def4466cee0e0b884c2
  search_scope: iModulonDB selected e_coli/precise1k gene=JW3038, request https://imodulondb.org/api/genes/JW3038/imodulons?organism=e_coli&dataset=precise1k,
    2026-11-04T04:05:42.664841Z; all201 returned rows inspected; no extrapolation
    to other datasets, untested conditions, biological absence or past query states.
- evidence_id: micro-ecoli-module-10
  kind: database
  reference: https://imodulondb.org/api/imodulons/e_coli/precise1k/10
  locator: Complete scalar metadata,15 member gene IDs/weights and threshold; activity
    table and generated narrative not used for biological claims; retained response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/ecoli-module-10.raw
  accessed_at: '2026-11-04T04:06:11.932685Z'
  support: context_only
  summary: Module10 Nucleotide Stress has regulator=null, function_description DNA
    repair/stringent ppGpp response/ribosome biogenesis and stability, threshold0.077432849;15
    member genes include b3066 weight0.082144995 and exclude b4052. Generated ai_summary
    is explicitly excluded from experimental or mechanistic support; no direct primosome
    assembly conclusion.
  snapshot_sha256: 2b2a79ee13351d914b0fa98d0aa767843b467db1c4b79cc17681affde8f2d11b
- evidence_id: micro-historical-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual2026-11-03T00:49:00.848907–00:49:00.863225Z invocation;
    unavailable exit1 permission failure
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical runner availability limitation only, not a new run. Current
    official catalogue and selected matched-host endpoints were freshly inspected
    as the native fallback.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-coma_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-verify-receipt.json
  locator: Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:03:46.101888Z'
  support: supports
  summary: Actual exit0; 4 reviewed examples;6 typed nodes:4 COVERED and2 UNANCHORED_WITH_UNIPROT.
    Diagnostics verify implemented accession/graph-example checks, not family completeness,
    experimental support or biological formation.
  snapshot_sha256: f29484c75311c172d74c29974a69eac31cc9d42f6fc197781b65c6a8625cbc02
- evidence_id: micro-native-coma_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-causal-receipt.json
  locator: Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-causal.log
    SHA256 db466080285af73e715169620b9d5b400c92d8e428f3e7dd20065fa3e87865b1
  accessed_at: '2026-11-04T04:03:46.588278Z'
  support: supports
  summary: Actual exit0; 4 reviewed examples;6 typed nodes:4 COVERED and2 UNANCHORED_WITH_UNIPROT.
    Diagnostics verify implemented accession/graph-example checks, not family completeness,
    experimental support or biological formation.
  snapshot_sha256: 39a54387115d29ddf33283ac15b9252c0212d520f27b0c92b128f214a38ffde2
- evidence_id: micro-native-core_primosome_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-verify-receipt.json
  locator: Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:03:51.765475Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples;2 COVERED typed nodes. Diagnostics verify
    implemented accession/graph-example checks, not family completeness, experimental
    support or biological formation.
  snapshot_sha256: bd711aad2ba0700590e379aa0d86d2866729b440bbe8663661dcdfcfa9670ae8
- evidence_id: micro-native-core_primosome_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-causal-receipt.json
  locator: Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-causal.log
    SHA256 86c84709c0661d272905360926d4aa86c7b0bd0e6e48bbddb4da91863801c0c1
  accessed_at: '2026-11-04T04:03:52.221304Z'
  support: supports
  summary: Actual exit0; 2 reviewed examples;2 COVERED typed nodes. Diagnostics verify
    implemented accession/graph-example checks, not family completeness, experimental
    support or biological formation.
  snapshot_sha256: 5051f4db47275371e7b5b9e9b4c8ead743cce7223db90a02302469257774540d
- evidence_id: micro-native-ctf18_rfc_like_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-verify-receipt.json
  locator: Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:04:00.902854Z'
  support: supports
  summary: Actual exit0; 7 reviewed examples;7 COVERED typed nodes. Diagnostics verify
    implemented accession/graph-example checks, not family completeness, experimental
    support or biological formation.
  snapshot_sha256: aea524501f1532c86389a90f04710da231f02b59042ebc71afe277faec7b8ea0
- evidence_id: micro-native-ctf18_rfc_like_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-causal-receipt.json
  locator: Actual receipt and entire log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-causal.log
    SHA256 b77337cdd5a7bc8793f4ed2e383dc3ecee05ecee0677dc4c1b3314167dd0a613
  accessed_at: '2026-11-04T04:04:01.344781Z'
  support: supports
  summary: Actual exit0; 7 reviewed examples;7 COVERED typed nodes. Diagnostics verify
    implemented accession/graph-example checks, not family completeness, experimental
    support or biological formation.
  snapshot_sha256: 5814e2f197ffd288942e9663d61d073b3978efb31f13afcedb8e90c265ac52f3
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/other/cog_complex.yaml
  locator: Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 63a87323bc5724de1cae502db180cb5a1cca96f62a851cb596469216865421ac
  summary: Entire record read, including definition, composition, exact examples/evidence,
    taxon/canonical scope, graphs, discussions and history. Unchanged from original
    frozen target bytes.
  support: supports
- evidence_id: plaque-original-0-yaml
  kind: prior_review
  reference: reviews/structured/20261022T051656Z-cog-complex-audit/review.yaml
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 958b6ec5699e9242068a0dc192ad59a515356f82bd3c35c96648a24853075b31
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-original-0-md
  kind: prior_review
  reference: reviews/structured/20261022T051656Z-cog-complex-audit/review.md
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 23c098c4064e28bbaacd19fb3e0492d1f879c430b4fa149d61e736a2d9750eeb
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/other/copi_vesicle_coat.yaml
  locator: Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
  summary: Entire record read, including definition, composition, exact examples/evidence,
    taxon/canonical scope, graphs, discussions and history. Unchanged from original
    frozen target bytes.
  support: supports
- evidence_id: plaque-original-2-yaml
  kind: prior_review
  reference: reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.yaml
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 2d0704ab60efd51c8356ca08977da0001cb9d60ea0a30992b2d1c454bc79f145
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-original-2-md
  kind: prior_review
  reference: reviews/structured/20261022T051657Z-copi-vesicle-coat-audit/review.md
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: cb5fe6f5d7a8939f8e2c702f405660f657fbc03181471b1b841c046999332c52
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/other/copii_vesicle_coat.yaml
  locator: Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2
  summary: Entire record read, including definition, composition, exact examples/evidence,
    taxon/canonical scope, graphs, discussions and history. Unchanged from original
    frozen target bytes.
  support: supports
- evidence_id: plaque-original-3-yaml
  kind: prior_review
  reference: reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.yaml
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 60e24f7cc590b681a782336f7f990d7b80b2be36d04ff50fa65eddb30876fb0f
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-original-3-md
  kind: prior_review
  reference: reviews/structured/20261022T051658Z-copii-vesicle-coat-audit/review.md
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 4f16870fa8b53ee75a7786b9a68a89773ee39a9484887e5e0e2299788f77ed48
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-current-7
  kind: record_content
  reference: data/structures/other/corvet_complex.yaml
  locator: Entire current maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: a3bf0da311e1d6b869043ba0b102130ef6e9e1dcb5009a8996058b43c40945a0
  summary: Entire record read, including definition, composition, exact examples/evidence,
    taxon/canonical scope, graphs, discussions and history. Unchanged from original
    frozen target bytes.
  support: supports
- evidence_id: plaque-original-7-yaml
  kind: prior_review
  reference: reviews/structured/20261022T051701Z-corvet-complex-audit/review.yaml
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 999552cd820926502a6b5ac08818b6951b954259aabe1d0aa6fe6669b518aaa5
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-original-7-md
  kind: prior_review
  reference: reviews/structured/20261022T051701Z-corvet-complex-audit/review.md
  locator: Complete original pair; native validation/render and original frozen-input
    proof
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 62bf1fd48d7f59294bae41a3fff3c73ca947a97206a07939091cb8f8132398be
  summary: Immutable historical review independently reassessed; historical validation
    is not represented as a current global execution.
  support: supports
- evidence_id: plaque-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Frozen repository rule read and applied
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  summary: Exact source-neutral class grounding, UNKNOWN formation necessity, optional
    examples and append-only historical rationale.
  support: supports
- evidence_id: plaque-review-skill
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen repository rule read and applied
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Named molecular/pathway assertions trigger structured-source coverage assessment
    even without expression-module claims.
  support: supports
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen repository rule read and applied
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: Native graph types permit proteins, families and complexes under GENE_OR_PROTEIN;
    external interactors need not be components.
  support: supports
- evidence_id: plaque-review-schema
  kind: authority
  reference: schema/record_review.yaml
  locator: Frozen repository rule read and applied
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
  summary: Native evidence, assessment, finding, action and predecessor contract.
  support: supports
- evidence_id: plaque-review-profile
  kind: authority
  reference: docs/record-review-profile.md
  locator: Frozen repository rule read and applied
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
  summary: Issue-bearing explicit batch and immutable review-only scope.
  support: supports
- evidence_id: plaque-checklist
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen repository rule read and applied
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
  summary: Field-by-field scientific review with bounded evidence and completeness
    assessment.
  support: supports
- evidence_id: plaque-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139,GO:0005789,GO:0006890,GO:0010008,GO:0017119,GO:0030120,GO:0030126,GO:0030127,GO:0030134,GO:0030137,GO:0033263,GO:0035964,GO:0048193,GO:0090114,GO:0099023
  locator: 'Complete requested15-term response: id/name/isObsolete/definition/synonyms/typed
    children; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/go.raw'
  accessed_at: '2026-11-04T04:05:22.843013Z'
  snapshot_sha256: 7a10fdfabf9a991d62af00e3058a635d4bf4429382d18aa1fe749455caa06134
  summary: Fifteen active GO identities, definitions and exact typed child relationships
    inspected. Exact COG/CORVET tethering and COPI/COPII coat identities, coat-versus-vesicle
    distinction and bounded transport/budding function match. No direct edge inferred
    from a transitive ancestor response.
  support: supports
- evidence_id: plaque-tax-4932
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/4932.json
  locator: Complete scientific name, taxon ID, rank and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/tax-4932.raw
  accessed_at: '2026-11-04T04:05:23.648065Z'
  snapshot_sha256: 963bbf3503fd0aa9e69dc25b64c5ae903f871991b37c4c593353b945c8e31688
  summary: Native Saccharomyces cerevisiae species/reference S288C strain and lineage
    checked. Paper laboratory/recombinant strains are not silently replaced by S288C.
  support: supports
- evidence_id: plaque-tax-559292
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/559292.json
  locator: Complete scientific name, taxon ID, rank and lineage; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/tax-559292.raw
  accessed_at: '2026-11-04T04:05:24.703470Z'
  snapshot_sha256: 9ebcfe8a317cc0c25c329a3a6a7cc9eaa863bb2dfebe5eaff9a34628c6684810
  summary: Native Saccharomyces cerevisiae species/reference S288C strain and lineage
    checked. Paper laboratory/recombinant strains are not silently replaced by S288C.
  support: supports
- evidence_id: plaque-protein-P11076
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11076.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P11076.raw
  accessed_at: '2026-11-04T04:04:55.656494Z'
  snapshot_sha256: fb2ce21f92da7c817647884a2805ab45d84f49b279093b1a68cd4908bbbfb7b4
  summary: P11076 is reviewed strain559292 ADP-ribosylation factor 1. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P12868
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P12868.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P12868.raw
  accessed_at: '2026-11-04T04:04:55.660024Z'
  snapshot_sha256: ff283afab18523326c61ef44b5c5ae24ea501a36b0b32d75e46d7b5834d4a2b0
  summary: P12868 is reviewed strain559292 E3 ubiquitin-protein ligase PEP5. Primary
    symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro
    cross-references checked. Identity and annotation do not prove universal necessity
    or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P15303
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P15303.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P15303.raw
  accessed_at: '2026-11-04T04:05:12.674423Z'
  snapshot_sha256: 13181465e32452a91853f6b16daf92a2d67f378a9dabcb9d19e84585bc1168cf
  summary: P15303 is reviewed strain559292 Protein transport protein SEC23. Primary
    symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro
    cross-references checked. Identity and annotation do not prove universal necessity
    or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P19146
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P19146.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P19146.raw
  accessed_at: '2026-11-04T04:04:56.619175Z'
  snapshot_sha256: 24708ced3c9aedaec94d8882a3a8027bda48da9a3a35e0df473b614ef3f457e2
  summary: P19146 is reviewed strain559292 ADP-ribosylation factor 2. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P20606
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20606.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P20606.raw
  accessed_at: '2026-11-04T04:04:54.623442Z'
  snapshot_sha256: b357bd5a974f24c0409bf017765b03d59132ea51bcd07912699b22356faee9cc
  summary: P20606 is reviewed strain559292 Small COPII coat GTPase SAR1. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P20795
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20795.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P20795.raw
  accessed_at: '2026-11-04T04:05:08.635232Z'
  snapshot_sha256: 74c8787eb68381dc26a6e70ba85414e3a05c4cc15f45e0686a0b57a4882755d6
  summary: P20795 is reviewed strain559292 Vacuolar protein sorting-associated protein
    33. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P23643
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23643.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P23643.raw
  accessed_at: '2026-11-04T04:05:10.599185Z'
  snapshot_sha256: 0d2c8a76a41038fa09099f851ea972dab3b2267d53915877617c7724af91e99f
  summary: P23643 is reviewed strain559292 Vacuolar protein sorting-associated protein
    3. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P27801
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P27801.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P27801.raw
  accessed_at: '2026-11-04T04:05:09.631379Z'
  snapshot_sha256: 6b73997591488f3066e961f073293728183c0b1b17eefa4c162d1abf133dd37d
  summary: P27801 is reviewed strain559292 Vacuolar membrane protein PEP3. Primary
    symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro
    cross-references checked. Identity and annotation do not prove universal necessity
    or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P32074
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32074.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P32074.raw
  accessed_at: '2026-11-04T04:05:13.599637Z'
  snapshot_sha256: 7bf09236856fbe6260a97d9275999613f6bddb1b4dff29b5d2ba0556d23adf5a
  summary: P32074 is reviewed strain559292 Coatomer subunit gamma. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P36017
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36017.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P36017.raw
  accessed_at: '2026-11-04T04:05:18.651061Z'
  snapshot_sha256: 205505359e867eb9af64b706eb08ba86c8df3feefde7dec12aafeec068b36058
  summary: P36017 is reviewed strain559292 Vacuolar protein sorting-associated protein
    21. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P38968
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38968.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P38968.raw
  accessed_at: '2026-11-04T04:05:17.759484Z'
  snapshot_sha256: 3cd679eb515caf22dceb7f5a2b97bb726ea5a88379f3117f90f10ab06364d1fc
  summary: P38968 is reviewed strain559292 Protein transport protein SEC31. Primary
    symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro
    cross-references checked. Identity and annotation do not prove universal necessity
    or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P39702
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39702.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P39702.raw
  accessed_at: '2026-11-04T04:05:09.692494Z'
  snapshot_sha256: 18f49e165869c5037ce9fa87a74d1ac71a7c461f6d189f21c42b2d801987b510
  summary: P39702 is reviewed strain559292 Vacuolar protein sorting-associated protein
    8. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P40094
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40094.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P40094.raw
  accessed_at: '2026-11-04T04:05:30.965605Z'
  snapshot_sha256: 6ebc9ba3bb5efc7bb82134b0fb00a83821b8f3f3e32005ae031e27727eb81888
  summary: P40094 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    3. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P40482
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40482.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P40482.raw
  accessed_at: '2026-11-04T04:05:15.073380Z'
  snapshot_sha256: 364fe7b7178611824e4035d3300302e3e97e8e5a87934557bbf966f0507e4817
  summary: P40482 is reviewed strain559292 Protein transport protein SEC24. Primary
    symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro
    cross-references checked. Identity and annotation do not prove universal necessity
    or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P40509
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40509.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P40509.raw
  accessed_at: '2026-11-04T04:05:15.737806Z'
  snapshot_sha256: d45cedfa27d3a43cd9b9a2666a91b3f35ae4ca29ba7397ac99687002f1cf696a
  summary: P40509 is reviewed strain559292 Coatomer subunit epsilon. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P41810
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41810.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P41810.raw
  accessed_at: '2026-11-04T04:05:11.630840Z'
  snapshot_sha256: 14db746dd9b7298b293cb31c5f9c75daf9d58bf6702ffb741a3c9678c17d1520
  summary: P41810 is reviewed strain559292 Coatomer subunit beta. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P41811
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41811.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P41811.raw
  accessed_at: '2026-11-04T04:05:30.658605Z'
  snapshot_sha256: 9c0c30568e621781e7f544ae72f36ecd3889e7b738a153b35b5b3e262d85e741
  summary: P41811 is reviewed strain559292 Coatomer subunit beta'. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P43621
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P43621.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P43621.raw
  accessed_at: '2026-11-04T04:05:33.655272Z'
  snapshot_sha256: 203f70e6015b5f82bae9395f2195f5cef7e5d6ffa0f536540519ff0e36d76fbd
  summary: P43621 is reviewed strain559292 Coatomer subunit delta. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53079
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53079.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53079.raw
  accessed_at: '2026-11-04T04:05:34.712224Z'
  snapshot_sha256: bd09e8d4ff6869d29d8948f25eab3ed9757db6c49507233dd6f0d91bf3e8e8fe
  summary: P53079 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    1. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53195
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53195.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53195.raw
  accessed_at: '2026-11-04T04:05:16.665803Z'
  snapshot_sha256: b089cd2e3d3bb4d5bb6eed732190e5a5a4ce40c541f7915746ddf49553ab4236
  summary: P53195 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    7. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53271
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53271.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53271.raw
  accessed_at: '2026-11-04T04:05:47.012265Z'
  snapshot_sha256: 204b63408c020e766baabcffa7dfc529239890f177b569353f64eb6c891abcbe
  summary: P53271 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    2. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53600
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53600.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53600.raw
  accessed_at: '2026-11-04T04:05:17.636014Z'
  snapshot_sha256: 05bc720904df87f1debcb5075ba2f0803c2ad2c1984fa00736022aff773e3725
  summary: P53600 is reviewed strain559292 Coatomer subunit zeta. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53622
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53622.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53622.raw
  accessed_at: '2026-11-04T04:05:19.761442Z'
  snapshot_sha256: 3fa8e6ac02935b57b3588e23901528210478283bbb5311fd3d3118999af5ced3
  summary: P53622 is reviewed strain559292 Coatomer subunit alpha. Primary symbol,
    aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro cross-references
    checked. Identity and annotation do not prove universal necessity or substitute
    for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53951
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53951.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53951.raw
  accessed_at: '2026-11-04T04:05:18.686719Z'
  snapshot_sha256: 41285f2630754d46b1574a261a2e39c20b61599169cd425e9545ec9c945ddfdd
  summary: P53951 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    5. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-P53959
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53959.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-P53959.raw
  accessed_at: '2026-11-04T04:05:46.888614Z'
  snapshot_sha256: e4d318a45ded7d621bb4695a7af478dd773d3d2a0bbaf757ac43c8ee369cf1dd
  summary: P53959 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    6. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-Q03308
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03308.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q03308.raw
  accessed_at: '2026-11-04T04:05:19.672612Z'
  snapshot_sha256: 572e18358d76bb4a5bcaa5f12a16aa6c5e0d24f6e8c11a5ad3637907f79c35f1
  summary: Q03308 is reviewed strain559292 Vacuolar protein sorting-associated protein
    16. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-Q04491
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04491.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q04491.raw
  accessed_at: '2026-11-04T04:05:20.851668Z'
  snapshot_sha256: 5ea1f9385e1989653cc9b1251babdb2a1e325e72d3b3617590028f3fca38207c
  summary: Q04491 is reviewed strain559292 Protein transport protein SEC13. Primary
    symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins and InterPro
    cross-references checked. Identity and annotation do not prove universal necessity
    or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-Q04632
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04632.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q04632.raw
  accessed_at: '2026-11-04T04:05:21.775872Z'
  snapshot_sha256: d6e9cbff9991279ae2f9d37c12741c8417cea44e9d675212c762620c15c3c43e
  summary: Q04632 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    8. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-protein-Q06096
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06096.json
  locator: Exact accession/status/protein name/genes/organism; relevant full comments
    and their evidence joins; InterPro IDs; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/protein-Q06096.raw
  accessed_at: '2026-11-04T04:05:21.780626Z'
  snapshot_sha256: 284fb0e937e00b2a123248c0ed9ff2bf9f9d4398dc543216be197fe4d8c3823c
  summary: Q06096 is reviewed strain559292 Conserved oligomeric Golgi complex subunit
    4. Primary symbol, aliases/locus, SUBUNIT and SUBCELLULAR LOCATION evidence joins
    and InterPro cross-references checked. Identity and annotation do not prove universal
    necessity or substitute for a primary experiment.
  support: supports
- evidence_id: plaque-ipr-IPR033370
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033370/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR033370.raw
  accessed_at: '2026-11-04T04:05:32.265116Z'
  snapshot_sha256: 0ed160e5a949d07dff0994d8c37af8a6b9d671ee7f49d0a9946d0db861ba9d61
  summary: 'Current InterPro IPR033370: Conserved oligomeric Golgi complex subunit
    1, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR009316
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009316/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR009316.raw
  accessed_at: '2026-11-04T04:05:32.647951Z'
  snapshot_sha256: 33cff78547c21255584141a41efdb678a419e1f1592b811687715afcbfebe19f
  summary: 'Current InterPro IPR009316: COG complex component, COG2, type family;
    native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished
    from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No
    generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-retry-IPR007265
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007265/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR007265.raw
  accessed_at: '2026-11-04T04:06:43.641107Z'
  snapshot_sha256: 014554c142898f542f52154612939ef60516a1e8403d3a893f5c9af393ca3490
  summary: 'Current InterPro IPR007265: Conserved oligomeric Golgi complex, subunit
    3, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-retry-IPR048682
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048682/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR048682.raw
  accessed_at: '2026-11-04T04:06:45.312115Z'
  snapshot_sha256: 2e3a10a15b8d671e8b49cc29ff00e901324d58ec12c47bb1ec8a7ce74203e481
  summary: 'Current InterPro IPR048682: Conserved oligomeric Golgi complex subunit
    4, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-retry-IPR019465
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019465/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR019465.raw
  accessed_at: '2026-11-04T04:06:47.002716Z'
  snapshot_sha256: f447786bdbc822feedc05edce5c5ee6f3920a476bb1a1dedba859bbb73773a9e
  summary: 'Current InterPro IPR019465: Conserved oligomeric Golgi complex subunit
    5, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR010490
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010490/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR010490.raw
  accessed_at: '2026-11-04T04:05:33.359544Z'
  snapshot_sha256: 1c47891cb4254aaa8aead599bf788726831ca16e52d6a5b4b79507465436e7e2
  summary: 'Current InterPro IPR010490: Conserved oligomeric Golgi complex subunit
    6, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR019335
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019335/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR019335.raw
  accessed_at: '2026-11-04T04:05:33.585651Z'
  snapshot_sha256: 43634beb181f5f7acd1df9b629cf8a73cd2f435e54f6fff623cf584e0b7a9019
  summary: 'Current InterPro IPR019335: Conserved oligomeric Golgi complex subunit
    7, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR007255
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007255/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR007255.raw
  accessed_at: '2026-11-04T04:05:33.707562Z'
  snapshot_sha256: 091980bb50afa48aa6210a2697bddca2ba93d902453ce94c3c1345006a6f8e11
  summary: 'Current InterPro IPR007255: Conserved oligomeric Golgi complex subunit
    8, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR006687
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006687/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR006687.raw
  accessed_at: '2026-11-04T04:05:33.686701Z'
  snapshot_sha256: bcf949d7092e1b0ed46413b8ea6557355dbe34a4fc375e3c7767c5da6b62bd41
  summary: 'Current InterPro IPR006687: Small GTPase superfamily, SAR1-type, type
    family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished
    from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No
    generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR016528
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016528/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR016528.raw
  accessed_at: '2026-11-04T04:05:34.107960Z'
  snapshot_sha256: 73b2d50cac8002fc54c640905ed1b5cede4fcd263942ae55daa674e0ab172bf7
  summary: 'Current InterPro IPR016528: Vacuolar protein sorting-associated protein
    11, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR016534
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016534/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR016534.raw
  accessed_at: '2026-11-04T04:05:34.209986Z'
  snapshot_sha256: ddcd8dd9da4c7607ff524d7af0615638c065e447fa9bd7868b7597340f06610d
  summary: 'Current InterPro IPR016534: Vacuolar protein sorting-associated protein
    16, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact classes
    are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the
    Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR032914
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR032914/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR032914.raw
  accessed_at: '2026-11-04T04:05:34.374516Z'
  snapshot_sha256: c9031c40d2d3cf9701bf98487804ee589d51d46a9af9dd84feb925fba5177ea1
  summary: 'Current InterPro IPR032914: Vam6/VPS39/TRAP1 family, type family; native
    description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from
    Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated
    summary is used.'
  support: supports
- evidence_id: plaque-ipr-retry-IPR045111
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045111/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR045111.raw
  accessed_at: '2026-11-04T04:06:48.687961Z'
  snapshot_sha256: 392e9408a0425a750cca044426425c79c8b9f5970104987bb5107552373f42aa
  summary: 'Current InterPro IPR045111: Vacuolar protein sorting-associated protein
    Vps41/Vps8, type family; native description read. COG1–8/SAR1/Vps11/Vps16 exact
    classes are distinguished from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families
    and the Vps18 domain. No generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-IPR007810
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007810/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-IPR007810.raw
  accessed_at: '2026-11-04T04:05:34.341623Z'
  snapshot_sha256: 23fc282051545d1bba2c2c0c8c893a58ba403301736facb4d3506ab1012a7e77
  summary: 'Current InterPro IPR007810: Pep3/Vps18, beta-propeller domain, type domain;
    native description read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished
    from Vps3/Vps39, Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No
    generated summary is used.'
  support: supports
- evidence_id: plaque-ipr-retry-IPR001619
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001619/
  locator: Complete metadata/name/type/curated description; compared with relevant
    native protein cross-references; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ipr-retry-IPR001619.raw
  accessed_at: '2026-11-04T04:06:50.360947Z'
  snapshot_sha256: 6c3475a301aecf6077b4679c28ba0660810bb1681644a8a5323fcb0a80eddcd9
  summary: 'Current InterPro IPR001619: Sec1-like protein, type family; native description
    read. COG1–8/SAR1/Vps11/Vps16 exact classes are distinguished from Vps3/Vps39,
    Vps8/Vps41 and Sec1 broader families and the Vps18 domain. No generated summary
    is used.'
  support: supports
- evidence_id: plaque-gene-RET1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: 'All 2 returned results inspected: P22276,P53622; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/gene-RET1.raw'
  accessed_at: '2026-11-04T04:05:54.039872Z'
  snapshot_sha256: e08053c7530d77cd89e56c7471167d1ff5c188e01f31390c1a89d329b7b1fe7a
  summary: Exact RET1 reviewed559292 query returns P22276 polymerase RET1 and P53622
    coatomer COP1 aliasRET1; the selected coatomer accession is correct but not a
    unique gene-query hit.
  support: supports
  search_scope: UniProtKB REST; exact URL query https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    size100, reviewed entries only; fetched 2026-11-04T04:05:54.039872Z; all returned
    rows inspected; no exhaustive all-protein or unreviewed-family claim.
- evidence_id: plaque-family-IPR033370
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR033370%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: 'All 6 returned results inspected: Q8WTW3,Q9FFF3,Q9VGC3,Q9Z160,Q9UTL1,Q54ZB3;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/family-IPR033370.raw'
  accessed_at: '2026-11-04T04:05:45.808932Z'
  snapshot_sha256: f9318f479760c7b3d212d6e0810873ff35eb3332a8bdb7db69046035f8abdbb5
  summary: Bounded reviewed family-member query confirms named generic COG ortholog-class
    members in other taxa; it does not add an absent whole-family annotation to S288C
    Cog1/2/7 sequences.
  support: supports
  search_scope: UniProtKB REST; exact URL query https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR033370%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    size100, reviewed entries only; fetched 2026-11-04T04:05:45.808932Z; all returned
    rows inspected; no exhaustive all-protein or unreviewed-family claim.
- evidence_id: plaque-family-IPR009316
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR009316%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: 'All 7 returned results inspected: Q14746,F4JRR1,Q9VF78,Q21444,Q921L5,O59705,Q54UC2;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/family-IPR009316.raw'
  accessed_at: '2026-11-04T04:05:51.831482Z'
  snapshot_sha256: 42f2fefc212c417c2c0aa75d4849a8d49c3dd772f383f51c65ee3a9b0ae3ce6f
  summary: Bounded reviewed family-member query confirms named generic COG ortholog-class
    members in other taxa; it does not add an absent whole-family annotation to S288C
    Cog1/2/7 sequences.
  support: supports
  search_scope: UniProtKB REST; exact URL query https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR009316%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    size100, reviewed entries only; fetched 2026-11-04T04:05:51.831482Z; all returned
    rows inspected; no exhaustive all-protein or unreviewed-family claim.
- evidence_id: plaque-family-IPR019335
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR019335%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: 'All 7 returned results inspected: P83436,Q9FGN0,Q9VAD6,Q3UM29,Q3T1G7,A2VDR8,Q54LC8;
    actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/family-IPR019335.raw'
  accessed_at: '2026-11-04T04:05:45.894831Z'
  snapshot_sha256: f812dc8b2833b07aa0af5b4d9af90c74570dbf7f2d7e60a9889ecd4bdebd18e4
  summary: Bounded reviewed family-member query confirms named generic COG ortholog-class
    members in other taxa; it does not add an absent whole-family annotation to S288C
    Cog1/2/7 sequences.
  support: supports
  search_scope: UniProtKB REST; exact URL query https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR019335%29+AND+%28reviewed%3Atrue%29&format=json&size=100;
    size100, reviewed entries only; fetched 2026-11-04T04:05:45.894831Z; all returned
    rows inspected; no exhaustive all-protein or unreviewed-family claim.
- evidence_id: plaque-paper-0
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2012.01.015%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-0.raw
  accessed_at: '2026-11-04T04:05:24.378580Z'
  snapshot_sha256: 23332fd66e339b39fbc12fed3cbf6527384b525f7556b93b5bd3ca40989e1ba6
  summary: Yu2012 mixed-species Arf1-coatomer structural recruitment model; full selected
    body read separately.
  support: supports
- evidence_id: plaque-paper-1
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2007.03.006%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-1.raw
  accessed_at: '2026-11-04T04:05:25.203817Z'
  snapshot_sha256: ca49c1afb07d9e285634f8d3f85c62376af4c994f9ab117d61989bd414cd1959
  summary: Peplowska2007 identifies six-subunit CORVET, shared four-class-C core,
    Vps3/Vps8 and Vps21 association/endosomal biogenesis; full body unavailable, exact
    strain/Methods/direct binary mechanics not certified.
  support: supports
- evidence_id: plaque-paper-2
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2F349248a0%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-2.raw
  accessed_at: '2026-11-04T04:05:25.457634Z'
  snapshot_sha256: b84012bda447bd0dc87e29af32e15f295830936d6127d5bd00fe3ca9737ae56b
  summary: Waters1991 identifies cytosolic coatomer, a large multisubunit nonclathrin
    coat complex; complete abstract only.
  support: supports
- evidence_id: plaque-paper-3
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb.3263%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-3.raw
  accessed_at: '2026-11-04T04:05:25.943929Z'
  snapshot_sha256: 657466a2267739566aa9db014e4b22cb1649660f5aa56c5ccc8506e5678a3a2c
  summary: Ha2016 reports recombinant COG architecture and interlobe flexibility;
    selected full body independently read.
  support: supports
- evidence_id: plaque-paper-4
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M400662200%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-4.raw
  accessed_at: '2026-11-04T04:05:26.186270Z'
  snapshot_sha256: eb61b22ac632ff201716dd67b493ab678e3271d1ad9415f2b8819e47f8b9e062
  summary: Loh/Hong2004 resolves mammalian Cog1/2/7 and notes structural divergence
    from yeast; not direct yeast localization evidence.
  support: supports
- evidence_id: plaque-paper-5
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200202016%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-5.raw
  accessed_at: '2026-11-04T04:05:26.713025Z'
  snapshot_sha256: 92c56afe6e2a0f320b340fb21dfb8bd89bf6b1b1f04b7961fa22533c82d38c78
  summary: Ungar2002 mammalian eight-subunit COG, Golgi association and architecture;
    not a yeast experimental assay.
  support: supports
- evidence_id: plaque-paper-6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200412003%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-6.raw
  accessed_at: '2026-11-04T04:05:26.998408Z'
  snapshot_sha256: 950b7f67c4fba990cd5c9ac12ddd32d7f2a07466ad9d38529a09a9f12f8676f5
  summary: Zolov2005 HeLa COG3 depletion/COG interactions with COPI and SNARE machinery;
    interactors are not thereby COG constituents.
  support: supports
- evidence_id: plaque-paper-7
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e02-11-0736%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-7.raw
  accessed_at: '2026-11-04T04:05:27.542865Z'
  snapshot_sha256: 70367a694e24a06c6b7d3e968570594f8b58c20479b06dd032b3c992d1df06ef
  summary: Sandmann2003 yeast coatomer retrieval, KKXX cargo binding and conditional-mutant
    suppression; body routes blocked, no detailed Methods certified.
  support: supports
- evidence_id: plaque-paper-8
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1247%2Fcsf.18014%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-8.raw
  accessed_at: '2026-11-04T04:05:27.892073Z'
  snapshot_sha256: 87baf43ab7c9e9c7e9bcdc087bb8f5b2ea638ccd5cb74539868d461e25f33015
  summary: Ishii2018 examines yeast COG subcomplexes at membranes and mitochondrial
    rerouting; selected body read separately.
  support: supports
- evidence_id: plaque-paper-9
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2Felife.00951%22&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-9.raw
  accessed_at: '2026-11-04T04:05:28.405163Z'
  snapshot_sha256: 96d559e58b0a6e9beddca005b5a54a5c500a049761ad2eea1178a96d9a6232eb
  summary: Zanetti2013 reconstituted COPII membrane coat cryoET architecture; selected
    full body read separately.
  support: supports
- evidence_id: plaque-paper-10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10562277+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-10.raw
  accessed_at: '2026-11-04T04:05:28.708705Z'
  snapshot_sha256: af47e49325234ecbc6c13754898bdf6148468b2b37e3b33f8d5343b5380e9d2d
  summary: VanRheenen1999 Sec34/Cog3 peripheral membrane/tethering complex; primary
    abstract plus native protein evidence join.
  support: supports
- evidence_id: plaque-paper-11
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10588657+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-11.raw
  accessed_at: '2026-11-04T04:05:29.174407Z'
  snapshot_sha256: d4f2c801c285128d13a01f0b4861a61d98dcbecf4b3b0ac09d2a1e7508fb8c87
  summary: Spelbrink1999 Grd20/Cog3 TGN sorting/actin phenotype; primary abstract
    scope, not universal structure necessity.
  support: supports
- evidence_id: plaque-paper-12
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10684247+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-12.raw
  accessed_at: '2026-11-04T04:05:29.380631Z'
  snapshot_sha256: fc5e1d2d05be0a2b0b1d452bff074db5f22c62c9a3778f6d22052ae8ea74eda9
  summary: Rout2000 NPC protein inventory/localization; Sec13 annotation is explicitly
    NPC localization of a shared protein, not direct COPII membership proof.
  support: supports
- evidence_id: plaque-paper-13
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10720463+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-13.raw
  accessed_at: '2026-11-04T04:05:29.933345Z'
  snapshot_sha256: bc577c68779c764ed421206f51a1181411415cd15bc45c42d68e2abe92dcf198
  summary: Matsuoka/Schekman2000 Methods reconstitution of COPII-coated vesicles from
    liposomes; abstract tier.
  support: supports
- evidence_id: plaque-paper-14
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10753972+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-14.raw
  accessed_at: '2026-11-04T04:05:30.077613Z'
  snapshot_sha256: 508c54b4ff636370443fa71f8b7ec1d44ea9e2a08342c378524784c6d6a577b5
  summary: Peng2000 distinct Sec24/Sfb2/Lst1 cargo-selection coats; generic core description
    need not inventory every alternative coat.
  support: supports
- evidence_id: plaque-paper-15
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10944212+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-15.raw
  accessed_at: '2026-11-04T04:05:30.645487Z'
  snapshot_sha256: 15f78769fcb804796e5512b261ee469d7458b105ccd1aedb6c095d067b07598a
  summary: Seals2000 HOPS complex/vacuole fusion; PEP5 vacuole membrane annotation
    is shared-core HOPS evidence, not direct CORVET localization.
  support: supports
- evidence_id: plaque-paper-16
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11086000+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-16.raw
  accessed_at: '2026-11-04T04:05:30.897310Z'
  snapshot_sha256: fc44a1328766a384468d8a914e80bdfe74e93f1dd90e1b386c0c0d25f5afb05c
  summary: Shimoni2000 Lst1 cooperates with Sec23/24 in Pma1 cargo packaging; not
    obligatory universal extra coat component.
  support: supports
- evidence_id: plaque-paper-17
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12235121+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-17.raw
  accessed_at: '2026-11-04T04:05:31.268013Z'
  snapshot_sha256: 1692a2cc72acee41b8cdbadc8b4ca9b872fb3f6d74a0ad46db0ffd9e214a58c2
  summary: Supek2002 Sec16 stabilization/reconstitution scope; no universal in-vivo
    stoichiometry inference.
  support: supports
- evidence_id: plaque-paper-18
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-18.raw
  accessed_at: '2026-11-04T04:05:31.269142Z'
  snapshot_sha256: 6bbebaf7c464f3020d5aa566aba7877a477aef2c45cafa1f9a15444db665826a
  summary: Huh2003 global tagged yeast localization abstract; exact ARF2/Sec26/Cog2
    joins come from native annotations, not this abstract naming each protein.
  support: supports
- evidence_id: plaque-paper-19
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15504911+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-19.raw
  accessed_at: '2026-11-04T04:05:31.551297Z'
  snapshot_sha256: cbbd7ce010184cfadc5da034a77c516721657daa6d432e6c4663a2d643ff5ac1
  summary: Gillingham2004 Rud3/Arf1 cis-Golgi interaction and localization; not every
    Arf paralog experiment.
  support: supports
- evidence_id: plaque-paper-20
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8004676+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-20.raw
  accessed_at: '2026-11-04T04:05:31.597985Z'
  snapshot_sha256: d678fd726aa7a02cf4800e175d702ca6eba62c44bbba9964191b6f21cac5293d
  summary: Barlowe1994 COPII coat/vesicle reconstitution from ER and purified components;
    nucleotide conditions distinguish coat retention/fusion.
  support: supports
- evidence_id: plaque-paper-21
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8548805+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-21.raw
  accessed_at: '2026-11-04T04:05:31.965728Z'
  snapshot_sha256: 58cfc96dd86e19b379c13b70a8c422eeb2ff9e3b75858116b4da5ef4ab688e62
  summary: Bednarek1995 both COPI and COPII budding from yeast ER/nuclear envelopes;
    this does not erase steady-state coat localization distinctions.
  support: supports
- evidence_id: plaque-paper-22
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9568718+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-22.raw
  accessed_at: '2026-11-04T04:05:32.007541Z'
  snapshot_sha256: 78d500293b2c49874b0b2ebe8a4e198a285a039acb5400f869dc21c6c94e7870
  summary: Matsuoka1998 sequential Sar1–Sec23/24–Sec13/31 reconstitution with defined
    liposomes; selected author PDF read separately.
  support: supports
- evidence_id: plaque-paper-23
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9606204+AND+SRC%3AMED&format=json&resultType=core&pageSize=5
  locator: Exact DOI/PMID-matched MED entry; title/authors/year and complete indexed
    primary abstract actually read; no full-body access implied by this row; actual
    response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/paper-23.raw
  accessed_at: '2026-11-04T04:05:32.182485Z'
  snapshot_sha256: d69f81781446871b7b616e895fda5c24cc647b8355f32eeb5abf3acdf728cbfd
  summary: VanRheenen1998 Sec35/Cog2 peripheral membrane docking; direct native localization
    evidence join checked.
  support: supports
- evidence_id: plaque-yu2012-body
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml
  locator: Genuine PMC S3 JATS; main sections S3–S7,S9,S10,S12,S13 read; no detailed
    S8/S14–S15 contacts/methods certification, pixels or supplements; actual response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/yu2012-body.raw
  accessed_at: '2026-11-04T04:06:41.442970Z'
  snapshot_sha256: a7adecb3e84137dcc05565185633b97cd4c07fc8e2556c98e9922152c7d34ea6
  summary: Two Arf1 binding sites, biochemical recruitment and a structural membrane-orientation
    model support coarse COPI association. Mammalian coatomer fragments plus yeast
    Arf1 form mixed-species recombinant preparations; this is not a native whole yeast
    coat structure or complete in-vivo hydrolysis cycle. Authors leave physiological
    GTPase stimulation unresolved.
  support: supports
- evidence_id: plaque-ha2016-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4972656.1/PMC4972656.1.xml
  locator: Genuine PMC S3 JATS; all main prose P2–P14 and Methods S2/S3; no figure
    pixels or supplementary datasets; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ha2016-s3.raw
  accessed_at: '2026-11-04T04:07:25.757528Z'
  snapshot_sha256: 0fbbac37af7ce438719471f5bb97f2c1b09cfb39aeb46ce4545b5184f5307d79
  summary: Recombinant S.cerevisiae Cog1–8 negative-stain EM supports octamer/two
    lobes and flexibility; produced in E.coli, with separate Kluyveromyces lobe-B
    experiments. Cog5/7 positions remain unresolved and deposition may affect flexibility.
    Yeast viability differences do not establish universal assembly essentiality.
  support: supports
- evidence_id: plaque-ishii2018-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6116515.1/PMC6116515.1.xml
  locator: Genuine PMC S3 JATS; sections S3,S5,S6,S7,S9–S13 including selected Results/Methods/Discussion;
    no pixels or supplementary strain lists; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/ishii2018-s3.raw
  accessed_at: '2026-11-04T04:07:25.736456Z'
  snapshot_sha256: b85b00e2ec05ca2a5ce0e84059bdfb8a9fff4446cb292fdc9d9eb0a20611ec07
  summary: YPH499/BY4741 yeast biochemical fractionation/co-IP and ectopic targeting
    distinguish stable cytosolic octamer from variable membrane subassemblies. Mitochondrial
    COG recruitment did not establish autonomous stable Golgi-vesicle tethering.
  support: supports
- evidence_id: plaque-zanetti2013-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3778437.1/PMC3778437.1.xml
  locator: Genuine PMC S3 JATS; s1,s2 opening,s2-2 with Fig6/7 text captions,s3-1
    sample preparation,s3-2 electron microscopy; no detailed s2-1 processing, pixels
    or supplements; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/zanetti2013-s3.raw
  accessed_at: '2026-11-04T04:07:26.062527Z'
  snapshot_sha256: cad4c58ff5347e3c0b5bee6b2ed4287d4195c731c3f49bf107b264337baded27
  summary: Reconstituted yeast COPII GUV coat cryoET supports inner/outer layers,
    but relative layer positions are constrained rather than fixed. Sec13/31 heterotetramer
    architecture is compatible with paired building-block descriptions; cargo geometry
    remains model-scoped.
  support: supports
- evidence_id: plaque-matsuoka1998-pdf
  kind: primary_source
  reference: https://bednareklab.biochem.wisc.edu/wp-content/uploads/sites/1623/2022/02/1998_Matsuoka_etal_Cell.pdf
  locator: Genuine Bednarek lab author PDF; extracted text printed pp263,267,269–271,273–274
    including sequential binding, morphology/stoichiometry, Fig7 text caption and
    experimental procedures; RSY445 microsomes/RSY1113 Sec13/31 preparation. Text
    inspection only, not figure pixels; actual response /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/matsuoka1998-pdf.raw
  accessed_at: '2026-11-04T04:06:41.943803Z'
  snapshot_sha256: 4c7e8eafea53f213b25b339d684115bd65a1af9e79d86b9e1222050aa52b0efa
  summary: Defined liposomes and yeast ER support sequential Sar1-GTP recruitment
    of Sec23/24 then Sec13/31, with conventional fixed-sample EM and lumen-retention
    assays. Synthetic/native coat stoichiometries and size distributions differ; stronger
    claims about universal ratios or complete physiological assembly are not made.
  support: supports
- evidence_id: plaque-peplowska2007-doi
  kind: database
  reference: https://api.crossref.org/v1/works/10.1016%2Fj.devcel.2007.03.006/transform
  locator: Entire bibliographic JSON; no Results/Methods/figure content; actual response
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/peplowska2007-doi.raw
  accessed_at: '2026-11-04T04:06:41.542168Z'
  snapshot_sha256: 7513f28b9dda462454ddf8b47296d9d6611a448826e05dbf6c12a4d2fe889898
  summary: DOI content-negotiation yielded Crossref bibliographic JSON, not a primary
    full text. Correct title/DOI metadata only.
  support: context_only
- evidence_id: plaque-access-limitations
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/access-limitations.json
  locator: Actual failed/access-limited route receipts; genuine fallback bodies separately
    scoped
  accessed_at: '2026-11-04T04:13:56.101092Z'
  snapshot_sha256: fdac23a108f8cf8e13ba17db908ae71818ce95a3966e73ce47f4b4159844052f
  summary: PMC Ha/Ishii/Sandmann surfaces returned recaptcha HTML; Sandmann BioC429
    and Peplowska publisher403 provide no body support. Initial Zanetti406 was an
    access-format result; genuine S3 body later obtained. Five InterPro429 responses
    were replaced by separately dated successful serial queries.
  support: context_only
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete fresh same-PR official /api/datasets response independently read;
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-microtubule/catalogue.raw
  accessed_at: '2026-11-04T04:05:08.101060Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: Complete20 organism rows/28 organism-dataset pairs contain bacterial/archaeal
    hosts, no S.cerevisiae/S288C, Kluyveromyces or mammalian biological host. Experimental
    E.coli protein production is not a matching biological dataset.
  support: supports
- evidence_id: plaque-catalogue-bounded-search
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Full returned organism id/name/dataset catalogue independently screened
  accessed_at: '2026-11-04T04:05:08.101060Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No matched biological host in the inspected catalogue; this is coverage
    only, not absence of the complexes or their regulation. No foreign-host downstream
    module proxy applies.
  support: context_only
  search_scope: Official /api/datasets; all20 organism rows/28 organism-dataset pairs
    at 2026-11-04T04:05:08.101060Z; bounded exact/lexical host screen Saccharomyces/cerevisiae/S288C/Kluyveromyces/Homo/bovine/rat;
    no outside databases or biological-negative inference.
- evidence_id: plaque-original-current-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-plaque/originals-current-proof.json
  locator: Actual four native validate/render commands;56 historical input occurrences;48
    current source/worktree inputs
  accessed_at: '2026-11-04T04:11:25.933976Z'
  snapshot_sha256: bc6db261716b4cd09a21ea064984c77dd5462c5f9310bbc772a336c04ae6c614
  summary: All original pairs validate and render byte-identically; all historical
    inputs match their frozen revisions. All48 current inputs match; all four assigned
    targets are byte-unchanged from historical input.
  support: supports
- evidence_id: plaque-native-cog_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cog_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:03:44.244046Z'
  snapshot_sha256: 9993833b50d30ff0d5fded4e094e7c1d0ca19347a0e6ba56a8690a636fe9ded2
  summary: Actual current-source exit0; 8 REVIEWED examples/8 typed nodes; all typed
    nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific
    mechanisms.
  support: supports
- evidence_id: plaque-native-cog_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/cog_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-causal.log
    SHA256 825ab0ccb55c67c2e97fe7be7a80fd58d197894220e39b25c4fcbfc9941d1dd0
  accessed_at: '2026-11-04T04:03:44.726792Z'
  snapshot_sha256: 176817ef69a77c3603f71f2b6c7d496b2641f262d41bfbaa3c3a7570d2d2ff92
  summary: Actual current-source exit0; 8 REVIEWED examples/8 typed nodes; all typed
    nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific
    mechanisms.
  support: supports
- evidence_id: plaque-native-copi_vesicle_coat-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/copi_vesicle_coat.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:03:47.975224Z'
  snapshot_sha256: 7f44605cb7250da8e1da3965440d78e9bb7af5fd3fe90ea9322901721be64d3b
  summary: Actual current-source exit0; 9 REVIEWED examples/2 typed nodes; all typed
    nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific
    mechanisms.
  support: supports
- evidence_id: plaque-native-copi_vesicle_coat-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/copi_vesicle_coat.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-causal.log
    SHA256 62b80549c9d8c2786488904a26b8a4e91d32a624b11000f16ebce03c1fe02395
  accessed_at: '2026-11-04T04:03:48.441854Z'
  snapshot_sha256: d6a9bc8837224984ae775283ddb02cf70700367674f26fdec0d2a371507d8f44
  summary: Actual current-source exit0; 9 REVIEWED examples/2 typed nodes; all typed
    nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific
    mechanisms.
  support: supports
- evidence_id: plaque-native-copii_vesicle_coat-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/copii_vesicle_coat.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:03:49.953193Z'
  snapshot_sha256: 31e0fc53dbf3f4bea2f76d6fd6d0565f2db053f98d7f8607aef23c2862d192da
  summary: Actual current-source exit0; 5 REVIEWED examples/3 typed nodes; all typed
    nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific
    mechanisms.
  support: supports
- evidence_id: plaque-native-copii_vesicle_coat-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/copii_vesicle_coat.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-causal.log
    SHA256 7571c7db8734ce15009e2ddbae753cc8f2630ee35f7d15d5b98f6eab28929f55
  accessed_at: '2026-11-04T04:03:50.417223Z'
  snapshot_sha256: ce8c2917f9d88b68d8bc707fc8fd9b39649b518bcdd69405c6868e23ca92ca79
  summary: Actual current-source exit0; 5 REVIEWED examples/3 typed nodes; all typed
    nodes COVERED. These gates verify identifiers/coverage, not necessity or all scientific
    mechanisms.
  support: supports
- evidence_id: plaque-native-corvet_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-verify-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/corvet_complex.yaml', '--verify']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-04T04:03:57.104140Z'
  snapshot_sha256: eddfdac9be6578d30aeecf0415ec2c5200b544fb474e434886baf312ee07ea98
  summary: Actual current-source exit0; 6 REVIEWED examples/7 typed nodes; six COVERED
    constituents and one externally anchored Vps21 interactor (UNANCHORED_WITH_UNIPROT),
    not a missing seventh constituent. These gates verify identifiers/coverage, not
    necessity or all scientific mechanisms.
  support: supports
- evidence_id: plaque-native-corvet_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-causal-receipt.json
  locator: Actual command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/other/corvet_complex.yaml', '--causal-graphs']; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-causal.log
    SHA256 7712e85ade0de1347ea909a9aaf2d0adab299bcdae10f215c03089983bbde0ff
  accessed_at: '2026-11-04T04:03:57.585371Z'
  snapshot_sha256: 4d4b95ae652281a187740dea7974fc5d8e57959d0f79590f295440d0fba60a48
  summary: Actual current-source exit0; 6 REVIEWED examples/7 typed nodes; six COVERED
    constituents and one externally anchored Vps21 interactor (UNANCHORED_WITH_UNIPROT),
    not a missing seventh constituent. These gates verify identifiers/coverage, not
    necessity or all scientific mechanisms.
  support: supports
- evidence_id: septin-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Scientific review and structured-source applicability
  summary: Actual whole-record molecular/pathway assertions require host/source coverage
    assessment; lack of expression-module claims is not sufficient exemption.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components and Discussions
  summary: Exact family identity differs from complex-specific role. Family or class
    is permitted. Dated rationale/history are append-only; optional examples or broad
    groups alone do not establish defects.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component identity/essentiality and graph fields
  summary: Formation essentiality is distinct from functional activity, localization
    or cellular viability. FUNCTION/NONMECHANISTIC graphs may describe coarse associations
    without a complete molecular assembly mechanism.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Native accession/name/status/taxon and query rules
  summary: Native primary genes versus ORF names and bounded query coverage are distinct
    from biological source membership, necessity and source-strain equivalence.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Evidence placement and descriptive graph scope
  summary: Constituent relationships, perturbation outputs and co-isolation retain
    experiment scope; graph coverage alone does not establish molecular identity or
    direct ubiquitination.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-literature-policy
  kind: authority
  reference: .claude/skills/literature-evidence/SKILL.md
  locator: Source access, image and read extents
  summary: Native metadata/abstract, genuine body/captions, pixels and failed responses
    are separate tiers. Generated authority prose is excluded as independent biological
    evidence.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: f7c3c594b5fb2cd7d4d700844fce3b97c91cc382d4fdca8b2e2a96cf16abd41b
- evidence_id: septin-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000438,GO:0000439,GO:0000440,GO:0005675,GO:0000112,GO:0006289,GO:0080008,GO:0031464,GO:0031465,GO:0043494,GO:0070912,GO:0070913
  locator: 'All12 exact requested terms: complete active identity/name/definition/synonyms
    and relevant typed child relationships'
  summary: GO0000438 and GO0000440 are context-specific children of seven-subunit
    TFIIH core GO0000439, with holoGO0005675 versus NEF3GO0000112 parthood; Rad2 is
    separate from Rad3. GO0006289 is NER. GO0080008 is broad Cul4-RING; GO0031464/65,GO0043494,GO0070912/13
    describe different named complexes and do not replace the source-specific CRL4WDR1
    local identity.
  accessed_at: '2026-11-04T04:05:24.692862Z'
  support: supports
  snapshot_sha256: 2768bcaaec0743eea54e7656796f467a2623f00c3dae44fc4037fc775dd2edf5
- evidence_id: septin-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official returned20-organism catalogue and dataset keys, independently
    read from peer fresh snapshot
  summary: No Saccharomyces/S288C or Trypanosoma/TREU927/Lister427/29-13 dataset is
    returned. Other listed E.coli datasets are not proxies for eukaryotic assemblies
    merely because bacteria produce recombinant proteins. No matched downstream gene/module
    queries apply after this bounded host coverage assessment. Noncoverage is not
    biological absence; actual peer fetch timestamp retained.
  accessed_at: '2026-11-04T04:05:08.101060Z'
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxId/scientificName/rank/lineage/otherNames
  summary: 'Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292;
    Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish
    identity of Lister427 or29-13 experimental strains.'
  accessed_at: '2026-11-04T04:05:24.565514Z'
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxId/scientificName/rank/lineage/otherNames
  summary: 'Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292;
    Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish
    identity of Lister427 or29-13 experimental strains.'
  accessed_at: '2026-11-04T04:05:24.569314Z'
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-tax5691
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete ENA taxId/scientificName/rank/lineage/otherNames
  summary: 'Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292;
    Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish
    identity of Lister427 or29-13 experimental strains.'
  accessed_at: '2026-11-04T04:05:31.808751Z'
  support: supports
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: septin-tax185431
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/185431
  locator: Complete ENA taxId/scientificName/rank/lineage/otherNames
  summary: 'Exact species/strain distinctions resolve: Saccharomyces cerevisiae4932/S288C559292;
    Trypanosoma brucei5691/TREU927185431. TREU927 reference identity does not establish
    identity of Lister427 or29-13 experimental strains.'
  accessed_at: '2026-11-04T04:05:31.702572Z'
  support: supports
  snapshot_sha256: 37f4acd608d79bb144d706335e37a83a0f97a94595aca5175855c8c390ec652d
- evidence_id: septin-protein-Q00578
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q00578.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. SSL2 primary; reviewed S288C XPB/Ssl2 core subunit.
    Native annotation is not an independent primary causal or formation assay; no
    sequence alignment performed.
  accessed_at: '2026-11-04T04:05:52.127848Z'
  support: supports
  snapshot_sha256: 00d085c4c2401d0b000cf09bd3c128f676a44e3c6b0deefe15fa3f40924b5274
- evidence_id: septin-protein-P32776
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32776.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. TFB1 primary; reviewed S288C p62. Native annotation
    is not an independent primary causal or formation assay; no sequence alignment
    performed.
  accessed_at: '2026-11-04T04:05:26.878419Z'
  support: supports
  snapshot_sha256: ece57492f780eb1923e237ac2a46dcc342f4c2e11b99fd3a4bd34809a338da4d
- evidence_id: septin-protein-Q02939
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q02939.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. TFB2 primary; reviewed S288C p52. Native annotation
    is not an independent primary causal or formation assay; no sequence alignment
    performed.
  accessed_at: '2026-11-04T04:05:26.893601Z'
  support: supports
  snapshot_sha256: e2e46662ce65cf8788f9137e9d2ea52c7358f294c801159d8dff07117de4be0b
- evidence_id: septin-protein-Q04673
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04673.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. SSL1 primary; reviewed S288C p44. Native annotation
    is not an independent primary causal or formation assay; no sequence alignment
    performed.
  accessed_at: '2026-11-04T04:05:27.998427Z'
  support: supports
  snapshot_sha256: 361b789b412a1d169b8369779f1efa06e924031bf58ae2e23c50bdd4c14f24b7
- evidence_id: septin-protein-Q12004
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12004.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. TFB4 primary; reviewed S288C p34. Native annotation
    is not an independent primary causal or formation assay; no sequence alignment
    performed.
  accessed_at: '2026-11-04T04:05:28.831505Z'
  support: supports
  snapshot_sha256: 4fb6e18ab5370fb8ed54ded6050130ae37b70634cf8c08389bdd5660f227fec3
- evidence_id: septin-protein-Q3E7C1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3E7C1.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. TFB5 primary; reviewed S288C p8/TTDA. Native
    nucleus evidenceHuh14562095 is localization, not by itself a membership or formation
    test. Native annotation is not an independent primary causal or formation assay;
    no sequence alignment performed.
  accessed_at: '2026-11-04T04:05:48.810866Z'
  support: supports
  snapshot_sha256: 64e2d23b987a77cb288f75feeaf80b1c3421a231420b2d357bed2ffb7820246b
- evidence_id: septin-protein-P06839
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P06839.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. RAD3 primary; reviewed S288C XPD helicase, distinct
    from Rad2/XPG. Native annotation is not an independent primary causal or formation
    assay; no sequence alignment performed.
  accessed_at: '2026-11-04T04:05:54.788113Z'
  support: supports
  snapshot_sha256: 8d6f1695c2551d5aa55cd51e5010a19140be33cff1bb06e175175fcb40740ae9
- evidence_id: septin-protein-Q57XW2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q57XW2.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. Unreviewed TREU927 putative Cullin4B; ORF names
    Tb03.1J15.620/Tb927.3.1290, not a formal primary CUL4 gene-name field. Matches
    Hu source locus. Native annotation is not an independent primary causal or formation
    assay; no sequence alignment performed.
  accessed_at: '2026-11-04T04:05:32.675780Z'
  support: supports
  snapshot_sha256: 78db9b34f405b2f858702f27f90bfde6d3566d76ff0b64c30f67e683f1d5986d
- evidence_id: septin-protein-Q586I3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q586I3.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. Unreviewed TREU927 DDB1 annotation; ORF names
    Tb06.30P15.290/Tb927.6.5110. Matches source locus. Automated nucleus annotation
    is not a new localization experiment. Native annotation is not an independent
    primary causal or formation assay; no sequence alignment performed.
  accessed_at: '2026-11-04T04:05:32.635622Z'
  support: supports
  snapshot_sha256: a81a6676d30c9b48c4928f035c773afe6ec0796da3bf3200874db9ff2218fd3c
- evidence_id: septin-protein-Q582R9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q582R9.json
  locator: Complete native accession/status/name/genes/organism; FUNCTION,SUBUNIT,SUBCELLULAR
    LOCATION,SIMILARITY comments and InterPro xrefs
  summary: Native identity inspected. Unreviewed uncharacterized TREU927 protein;
    ORF names Tb03.48K5.140/Tb927.3.4660. No native WDR1 synonym. WD-repeat domains
    do not identify source WDR1 Tb927.10.15080. Native annotation is not an independent
    primary causal or formation assay; no sequence alignment performed.
  accessed_at: '2026-11-04T04:05:31.675461Z'
  support: supports
  snapshot_sha256: ec71b42e2b1085758d23efa606c6d89e6fcd869b073b1e63fb8023d09d67a6ff
- evidence_id: septin-gene-SSL2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASSL2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match Q00578 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:25.975783Z'
  support: supports
  snapshot_sha256: 43ac93ba56bf2d1b66bb69a43638d94ddc7e618c0af8c12ea0e3a468965d1fb4
  search_scope: Official UniProt REST query (gene_exact:SSL2) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ASSL2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:25.975783Z.
- evidence_id: septin-gene-TFB1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match P32776 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:49.304360Z'
  support: supports
  snapshot_sha256: 0108a1f87e98a7c5dcb80ff26c1fd8b0d41f165358388a1d9bfb1d8c42d738e4
  search_scope: Official UniProt REST query (gene_exact:TFB1) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ATFB1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:49.304360Z.
- evidence_id: septin-gene-TFB2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match Q02939 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:28.852191Z'
  support: supports
  snapshot_sha256: 7ea680a3c4bb22c7a88410f69dd21d2c37b469d36d6f1623cd907b79c5a47a40
  search_scope: Official UniProt REST query (gene_exact:TFB2) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ATFB2%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:28.852191Z.
- evidence_id: septin-gene-SSL1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASSL1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match Q04673 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:25.837346Z'
  support: supports
  snapshot_sha256: 13700efb13e21030d9d3da52f79c1575f004badf98dd168f1930e1861344d014
  search_scope: Official UniProt REST query (gene_exact:SSL1) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ASSL1%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:25.837346Z.
- evidence_id: septin-gene-TFB4-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB4%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match Q12004 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:31.913539Z'
  support: supports
  snapshot_sha256: 1c5e5bb153d3e48e7f64904a2f42d83c157c718be63efd37b3f17f72446aa0d9
  search_scope: Official UniProt REST query (gene_exact:TFB4) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ATFB4%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:31.913539Z.
- evidence_id: septin-gene-TFB5-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATFB5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match Q3E7C1 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:48.979495Z'
  support: supports
  snapshot_sha256: 071c7af70df4deca30c99ffd8e96c16a9f49b47f5f9bb3f296a910f2ba751e63
  search_scope: Official UniProt REST query (gene_exact:TFB5) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ATFB5%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:48.979495Z.
- evidence_id: septin-gene-RAD3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARAD3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned page and native result identity fields
  summary: Complete returned single reviewed match P06839 agrees with declared yeast
    symbol. This is current bounded coverage, not reconstruction of an October query.
  accessed_at: '2026-11-04T04:05:54.364398Z'
  support: supports
  snapshot_sha256: 90bf88e25ae13ac18b32c64ac09933fb99374b9cb13b4f4b2f80cd9f7765759f
  search_scope: Official UniProt REST query (gene_exact:RAD3) AND (taxonomy_id:559292)
    AND (reviewed:true); parameters query=%28gene_exact%3ARAD3%29+AND+%28taxonomy_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500;
    no date filter; complete returned page read at 2026-11-04T04:05:54.364398Z.
- evidence_id: septin-rad3-family-members
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR001945%29+AND+%28reviewed%3Atrue%29&format=json&size=500&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id
  locator: Complete returned page and native result identity fields
  summary: 'All8 returned reviewed member identities read: P18074,Q8W4M7,Q55G81,A6QLJ0,O08811,P06839,P26659,Q60452
    are RAD3/XPD homologs. Together with native family name and P06839 xref, this
    supports IPR001945 despite unrelated XPG/Rad2 prose in its description; no sequence
    alignment or exhaustive phylogeny.'
  accessed_at: '2026-11-04T04:05:30.624440Z'
  support: supports
  snapshot_sha256: 8617bfae335b8e73e188b75c87bb2fd37c5c5977656f79439c425383ad3d1a9a
  search_scope: Official UniProt REST query (xref:interpro-IPR001945) AND (reviewed:true);
    parameters query=%28xref%3Ainterpro-IPR001945%29+AND+%28reviewed%3Atrue%29&format=json&size=500&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id;
    no date filter; complete returned page read at 2026-11-04T04:05:30.624440Z.
- evidence_id: septin-locus-Tb927.3.1290
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.1290+AND+organism_id%3A185431&format=json&size=25
  locator: Complete returned page and native result identity fields
  summary: Complete current exact-locus result Q57XW2. Source Tb927.10.15080 zero-result
    search does not establish biological absence and cannot justify substitution of
    Tb927.3.4660/Q582R9.
  accessed_at: '2026-11-04T04:05:50.762374Z'
  support: supports
  snapshot_sha256: 1a2410deca1e1ec80f0aa0a74d5063eb4668cc57b68b3e5081e5fb570ea11064
  search_scope: Official UniProt REST query Tb927.3.1290 AND organism_id:185431; parameters
    query=Tb927.3.1290+AND+organism_id%3A185431&format=json&size=25; no date filter;
    complete returned page read at 2026-11-04T04:05:50.762374Z.
- evidence_id: septin-locus-Tb927.6.5110
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.6.5110+AND+organism_id%3A185431&format=json&size=25
  locator: Complete returned page and native result identity fields
  summary: Complete current exact-locus result Q586I3. Source Tb927.10.15080 zero-result
    search does not establish biological absence and cannot justify substitution of
    Tb927.3.4660/Q582R9.
  accessed_at: '2026-11-04T04:05:34.645228Z'
  support: supports
  snapshot_sha256: 09ed2918b0fa6005a4d455930fe01739b3a31ea0cc11c85bfdd6177475fbcc0e
  search_scope: Official UniProt REST query Tb927.6.5110 AND organism_id:185431; parameters
    query=Tb927.6.5110+AND+organism_id%3A185431&format=json&size=25; no date filter;
    complete returned page read at 2026-11-04T04:05:34.645228Z.
- evidence_id: septin-locus-Tb927.3.4660
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.3.4660+AND+organism_id%3A185431&format=json&size=25
  locator: Complete returned page and native result identity fields
  summary: Complete current exact-locus result Q582R9. Source Tb927.10.15080 zero-result
    search does not establish biological absence and cannot justify substitution of
    Tb927.3.4660/Q582R9.
  accessed_at: '2026-11-04T04:05:52.424662Z'
  support: supports
  snapshot_sha256: c9ce65743ceceebc4b423fc982ee1b1b05f1fce382991e935b2d5e5219940d8e
  search_scope: Official UniProt REST query Tb927.3.4660 AND organism_id:185431; parameters
    query=Tb927.3.4660+AND+organism_id%3A185431&format=json&size=25; no date filter;
    complete returned page read at 2026-11-04T04:05:52.424662Z.
- evidence_id: septin-locus-Tb927.10.15080
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=Tb927.10.15080+AND+organism_id%3A185431&format=json&size=25
  locator: Complete returned page and native result identity fields
  summary: Complete current exact-locus result is empty. Source Tb927.10.15080 zero-result
    search does not establish biological absence and cannot justify substitution of
    Tb927.3.4660/Q582R9.
  accessed_at: '2026-11-04T04:05:33.690098Z'
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: Official UniProt REST query Tb927.10.15080 AND organism_id:185431;
    parameters query=Tb927.10.15080+AND+organism_id%3A185431&format=json&size=25;
    no date filter; complete returned page read at 2026-11-04T04:05:33.690098Z.
- evidence_id: septin-go-name-CRL4WDR1
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=CRL4WDR1&limit=25
  locator: Complete returned page and native result identity fields
  summary: Bounded exact QuickGO name query returns no hit; no exhaustive ontology-wide
    or biological absence claimed. Source-defined local identity is retained rather
    than adopting a broader/different complex.
  accessed_at: '2026-11-04T04:05:33.719379Z'
  support: supports
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
  search_scope: Official QuickGO query CRL4WDR1; parameters query=CRL4WDR1&limit=25;
    no date filter; complete returned page read at 2026-11-04T04:05:33.719379Z.
- evidence_id: septin-go-name-WDR1
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=WDR1&limit=25
  locator: Complete returned page and native result identity fields
  summary: Bounded exact QuickGO name query returns no hit; no exhaustive ontology-wide
    or biological absence claimed. Source-defined local identity is retained rather
    than adopting a broader/different complex.
  accessed_at: '2026-11-04T04:05:33.870663Z'
  support: supports
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
  search_scope: Official QuickGO query WDR1; parameters query=WDR1&limit=25; no date
    filter; complete returned page read at 2026-11-04T04:05:33.870663Z.
- evidence_id: septin-ipr-IPR001161
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001161/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native family name/type, non-LLM description
    flags, and matching example cross-reference inspected; general family background
    is not a universal seven-subunit formation assay.
  accessed_at: '2026-11-04T04:05:29.266500Z'
  support: supports
  snapshot_sha256: a3b0fa610be32c3a19a82f2d93cea3730b7559b7a27ff5a6465f68582ba18a41
- evidence_id: septin-ipr-IPR027079
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027079/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native family name/type, non-LLM description
    flags, and matching example cross-reference inspected; general family background
    is not a universal seven-subunit formation assay.
  accessed_at: '2026-11-04T04:05:29.307392Z'
  support: supports
  snapshot_sha256: 1d6919cc5a1d4861d411d45cd467c68dc720aa1dfe51de06aaa800db167d36a4
- evidence_id: septin-ipr-IPR004598
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004598/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native family name/type, non-LLM description
    flags, and matching example cross-reference inspected; general family background
    is not a universal seven-subunit formation assay.
  accessed_at: '2026-11-04T04:05:29.202207Z'
  support: supports
  snapshot_sha256: 168323f308db29bc571164f7a587dc18d7c0b35f8e5b72e3c4c0259df120584c
- evidence_id: septin-retry-IPR012170
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012170/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native family name/type, non-LLM description
    flags, and matching example cross-reference inspected; general family background
    is not a universal seven-subunit formation assay.
  accessed_at: '2026-11-04T04:06:13.163992Z'
  support: supports
  snapshot_sha256: 5faa786cfb01cccfc852379fa4a45bf9e572a7c00735ed36cd06c2403c7aeb1c
- evidence_id: septin-ipr-IPR004600
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004600/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native family name/type, non-LLM description
    flags, and matching example cross-reference inspected; general family background
    is not a universal seven-subunit formation assay.
  accessed_at: '2026-11-04T04:05:29.488460Z'
  support: supports
  snapshot_sha256: dfed19449dd2bf2e849d456bc3ea6c14a60e6d0f657e2a9df7612f0a3201133f
- evidence_id: septin-retry-IPR009400
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009400/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native family name/type, non-LLM description
    flags, and matching example cross-reference inspected; general family background
    is not a universal seven-subunit formation assay.
  accessed_at: '2026-11-04T04:06:15.890292Z'
  support: supports
  snapshot_sha256: 374500cc56a6eecc5a57e4e945f06d96c00f044404ebc078bbde3563333dea2a
- evidence_id: septin-retry-IPR001945
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001945/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Exact full-protein family identity matches the reviewed yeast example xref,
    independent of complex-specific role. Native name/type and reviewed members independently
    identify RAD3/XPD; unrelated XPG/Rad2 description paragraphs are not used to equate
    the distinct proteins.
  accessed_at: '2026-11-04T04:06:19.217500Z'
  support: supports
  snapshot_sha256: d3cc7b0f543a85022aa59ed4ca015619399ca445c0074c824e26eab29ffc53e8
- evidence_id: septin-ipr-IPR045093
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045093/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Broader family scope does not independently identify the exact WDR1-containing
    complex. Cullin includes multiple paralogs; no exact Cullin4/WDR1 role inferred
    from the broad family alone.
  accessed_at: '2026-11-04T04:05:32.439265Z'
  support: supports
  snapshot_sha256: 3c1fabca973d9704f4e57ccb886f8ae6284079c9178bdf627cccc8bb35bac5aa
- evidence_id: septin-ipr-IPR050358
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050358/
  locator: Complete native name/type/hierarchy/member signatures/description-generation
    flags, description scope and matching UniProt xref
  summary: Broader family scope does not independently identify the exact WDR1-containing
    complex. RSE1/DDB1/CPSF1 label and member signature are broader than DDB1 alone.
    Top-level is_llm/is_reviewed_llm flags are true despite differing paragraph flags;
    all generated functional prose is excluded.
  accessed_at: '2026-11-04T04:05:32.470185Z'
  support: supports
  snapshot_sha256: 36bb37346da7eabcb9f53419d1b173337dea419712be8c8a3828a6feb7100c3e
- evidence_id: septin-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED14562095 complete authors/title/year/DOI/PMCID and abstract
  summary: 'Huh2003 complete abstract: global yeast GFP localization; nuclear location
    does not alone establish TFIIH membership.'
  accessed_at: '2026-11-04T04:05:27.685833Z'
  support: supports
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
  search_scope: Europe PMC exact query EXT_ID:14562095 AND SRC:MED; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:27.685833Z.
- evidence_id: septin-pmid-14500720
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14500720+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED14500720 complete authors/title/year/DOI/PMCID and abstract
  summary: 'Takagi2003 complete abstract: TFIIK separation/association and transcription
    context; unread detailed methods/body not certified.'
  accessed_at: '2026-11-04T04:05:27.659783Z'
  support: supports
  snapshot_sha256: 096ce72f39137489ef643d0b8a4d111f03007c47d7a662c2b255877c24672f55
  search_scope: Europe PMC exact query EXT_ID:14500720 AND SRC:MED; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:27.659783Z.
- evidence_id: septin-pmid-15220919
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15220919+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED15220919 complete authors/title/year/DOI/PMCID and abstract
  summary: 'Ranish2004 complete abstract: Tfb5/TTDA identification and transcription/recruitment
    context; unread body not certified.'
  accessed_at: '2026-11-04T04:05:28.436275Z'
  support: supports
  snapshot_sha256: 32012d52bee73a9dd4e4e4920023ccd53c4a3e0744e898575f9cd81755d6f2a6
  search_scope: Europe PMC exact query EXT_ID:15220919 AND SRC:MED; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:28.436275Z.
- evidence_id: septin-pmid-22411836
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22411836+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED22411836 complete authors/title/year/DOI/PMCID and abstract
  summary: Murakami2012 complete abstract; genuine body separately scoped.
  accessed_at: '2026-11-04T04:05:28.462557Z'
  support: supports
  snapshot_sha256: d8999ee2edcd2bddc63b4abfe892448b77345de955fa12b4098efcb79bf5345c
  search_scope: Europe PMC exact query EXT_ID:22411836 AND SRC:MED; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:28.462557Z.
- evidence_id: septin-pmid-10915862
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10915862+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED10915862 complete authors/title/year/DOI/PMCID and abstract
  summary: Prakash and Prakash2000 SECONDARY review abstract explicitly says Rad2+TFIIH
    constitute NEF3; not a new primary assembly experiment.
  accessed_at: '2026-11-04T04:05:30.231354Z'
  support: supports
  snapshot_sha256: 97a04e69a70ffa920a6dbe412a1f376e35d76af7a915263a3c6e4368c30c8a50
  search_scope: Europe PMC exact query EXT_ID:10915862 AND SRC:MED; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:30.231354Z.
- evidence_id: septin-prakash2000-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fs0027-5107%2800%2900037-3%22&format=json&resultType=core
  locator: Unique MED10915862 complete authors/title/year/DOI/PMCID and abstract
  summary: Exact DOI resolves the same MED10915862 secondary-review abstract, not
    full text.
  accessed_at: '2026-11-04T04:05:30.420226Z'
  support: supports
  snapshot_sha256: eeb8f3216eb34c53103f359018d8b801e6d82293935d42a007bae209d46cd929
  search_scope: Europe PMC exact query DOI:"10.1016/s0027-5107(00)00037-3"; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:30.420226Z.
- evidence_id: septin-doi-9
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1371%2Fjournal.ppat.1006146%22&format=json&resultType=core
  locator: Unique MED28052114 complete authors/title/year/DOI/PMCID and abstract
  summary: Hu et al2017 primary article metadata/abstract; genuine body separately
    scoped.
  accessed_at: '2026-11-04T04:05:31.011493Z'
  support: supports
  snapshot_sha256: ef8d468dd547d06bb94d6b3641efb1600f5eadaa1558a8cbfd05447b24c46431
  search_scope: Europe PMC exact query DOI:"10.1371/journal.ppat.1006146"; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:31.011493Z.
- evidence_id: septin-doi-3
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41598-025-32077-9%22&format=json&resultType=core
  locator: Unique MED41413177 complete authors/title/year/DOI/PMCID and abstract
  summary: Cullin diversity2025 primary article metadata/abstract; exact Table1 and
    body scopes separately recorded.
  accessed_at: '2026-11-04T04:05:31.168236Z'
  support: supports
  snapshot_sha256: 6a57458ec7bdfd5752a26ff751d7af8150c150b0c45c9ffa4467dcd87fffa62c
  search_scope: Europe PMC exact query DOI:"10.1038/s41598-025-32077-9"; resultType=core,format=json,default
    bounded returned page,no date filter; unique complete result read at 2026-11-04T04:05:31.168236Z.
- evidence_id: septin-murakami2012-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3323989/
  locator: Genuine primary HTML Abstract,Table1,Resultssec2–5 with Figures1–4 captions,Discussionsec6,Methodssec8–10,12–13;
    no pixels/supplements
  summary: Yeast purification/MS supports listed core constituents plus TFIIK. Tfb6-associated11-subunit
    and dissociation states are not a contradiction of the canonical seven-subunit
    core ontology. Reconstitution supports function and context-dependent Ssl2 retention;
    it does not prove a unique assembly sequence. FY602/FY603 S288c and other CB010/DG
    backgrounds are distinguished from generic reference accessions; E.coli Rosetta2/XL10
    are production/cloning hosts.
  accessed_at: '2026-11-04T04:05:28.546601Z'
  support: supports
  snapshot_sha256: b5b84179e73c8362d00a1b226d0f77714b4f0bc428fcb72d7cd892476b23c623
- evidence_id: septin-PMC5241021-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5241021/fullTextXML
  locator: Genuine JATS front/author/license,Resultssec003–008,Discussionsec009,Methodssec011–017,embedded
    Figures1–8 captions; only Figure2 pixels separately inspected
  summary: Hu2017 defines WDR1 Tb927.10.15080, Cullin4 Tb927.3.1290 and DDB1 Tb927.6.5110.
    Yeast fragment interactions, GST-fusion plus parasite lysate and co-IP establish
    associations, not a complete purified catalytic complex. PDZ alone is insufficient/not
    required; PEST deletion disrupts fragment association. RNAi phenotypes and abundance/chase/IP/pSer54-Centrin2
    conditions remain separate24h/48h observations. Anti-ubiquitin species may be
    TbPLK or partners; overexpression phenocopies do not prove rescue/exclusive mediation.
    29-13 RNAi and Lister427 tagging remain distinct from TREU927 reference protein
    identities; Cdc27/APC-C and D-box contributions remain qualified.
  accessed_at: '2026-11-04T04:05:35.532250Z'
  support: supports
  snapshot_sha256: 14db45e5df4366741ab57052076df20ea7453b39d4fa719632051406a30efe9e
- evidence_id: septin-PMC12816148-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12816148/fullTextXML
  locator: Genuine JATS front/abstract,Table1,ResultsSec5/6,DiscussionSec10 and cell
    cultureSec12; no figure pixels or supplemental LC-MS/MS reanalysis
  summary: 2025 table maps Tb927.3.1290 to TbCul-D and Tb927.11.11430 to TbCul-E;
    discussion attributes old TbPLK work to E, an explicitly retained source nomenclature
    conflict. TbCul-D immunoisolation includes DDB1,Rbx1 and DCAF loci11.3190/8.840;
    these are not automatically new invariant members of the earlier WDR1-defined
    assembly. Lister427 procyclic culture scope retained.
  accessed_at: '2026-11-04T04:05:35.992192Z'
  support: supports
  snapshot_sha256: e8e06fecd846a0ceda847b73614fdf72ca794a565399b729fdd2298339b41bd3
- evidence_id: septin-prakash2000-doi
  kind: validation
  reference: https://doi.org/10.1016/s0027-5107(00)00037-3
  locator: Exact current route response only
  summary: Current DOI response is HTTP200 redirect-only linking-hub HTML, not article
    body. Original historical failed-access dates and response types remain separate.
  accessed_at: '2026-11-04T04:05:30.503346Z'
  support: context_only
  snapshot_sha256: 48444b131172b7bd085ac8510e72eca31c6149e85728b37009a5ab8e5ce22bfd
- evidence_id: septin-prakash2000-publisher
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/S0027510700000373
  locator: Exact current route response only
  summary: Current publisher403 is failed access; no body inferred. Original historical
    failed-access dates and response types remain separate.
  accessed_at: '2026-11-04T04:05:30.308481Z'
  support: context_only
  snapshot_sha256: 23fe7a81c10dfd1e8260d013dfd7b7ed63b452e156133c7bde0ff0fd7b18ff62
- evidence_id: septin-image-metadata
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5241021.1/PMC5241021.1.json
  locator: Complete PMC OA metadata,license/retraction state,Figure2 media URL and
    MD5
  summary: PMC5241021 CC-BY metadata lists Figure2 MD5 75b6e61b8ad7f417a1ca474d1fda5b05,
    matching the fresh retrieved and frozen local image. JATSfront separately provides
    CC-BY4.0 and Hu/Zhou/Han/Li attribution.
  accessed_at: '2026-11-04T04:05:35.593116Z'
  support: supports
  snapshot_sha256: 20c07b0ef85f4356056b4e4cbe149ef9c55d3d7769217ac596e2cfb3ce0d56c6
- evidence_id: septin-image-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5241021.1/ppat.1006146.g002.jpg
  locator: Actual Figure2 image pixels A–F viewed; byte SHA matches frozen image;
    caption/body separately read
  summary: A constructs, B two-hybrid growth, C GST-fusion/lysate pull-down, D co-IP,
    E WDR1/TbPLK fluorescence across phases and F WDR1/LdCen1 localization are visible.
    This is not a micrograph of the entire ligase. Caption supplies5µm scale; no whole-complex
    dimensions measured. PanelF pixel saysG1 while source caption saysS; maintained
    G1/S wording avoids a false panel-specific phase claim. No Figure3/6/other pixels
    or supplements inspected in this pass.
  accessed_at: '2026-11-04T04:05:35.593099Z'
  support: supports
  snapshot_sha256: 670801001c1d236247e8901451b48538d1b444bbeddde152500be4273d75cc62
- evidence_id: septin-image-local
  kind: record_content
  reference: data/images/other/crl4wdr1_ubiquitin_ligase_complex/pmc5241021_ppat_1006146_g002_04eab535.jpg
  locator: Actual frozen Figure2 pixels independently viewed with view_image
  summary: Complete local image is exactly the fresh publisher/PMC media asset. Actual
    panel inspection, source-caption scope and license are recorded separately; old
    record claims of other figures having been inspected are historical, not repeated
    current pixel certification.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 670801001c1d236247e8901451b48538d1b444bbeddde152500be4273d75cc62
- evidence_id: septin-packet-source-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/source-receipts.json
  locator: Actual HTTP receipts/status/types/times and body hashes
  summary: Access provenance only. Three initial InterPro429 responses succeeded on
    actual sequential retry; PMC challenge HTML/JATS500 and Prakash redirect/403 provide
    no body evidence. Only separately genuine sources support scientific claims.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: context_only
  snapshot_sha256: 76d66e65af5c1362fa7558e914350bfe78e48a52075b2495d9a73d50134967b3
- evidence_id: septin-packet-retry-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/retry-receipts.json
  locator: Actual HTTP receipts/status/types/times and body hashes
  summary: Access provenance only. Three initial InterPro429 responses succeeded on
    actual sequential retry; PMC challenge HTML/JATS500 and Prakash redirect/403 provide
    no body evidence. Only separately genuine sources support scientific claims.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: context_only
  snapshot_sha256: 04c3e77bf7e6b0cf702fd194a8b4d4bed3925f34c13483c7164be01eb0a310ef
- evidence_id: septin-packet-shared-receipts
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/shared-receipts.json
  locator: Actual HTTP receipts/status/types/times and body hashes
  summary: Access provenance only. Three initial InterPro429 responses succeeded on
    actual sequential retry; PMC challenge HTML/JATS500 and Prakash redirect/403 provide
    no body evidence. Only separately genuine sources support scientific claims.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: context_only
  snapshot_sha256: 7ea7a59a438235e7d9842fecd1e5586cb9ada264b48dc293f8f95c29513dca9a
- evidence_id: septin-adapter-runner-historical
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical2026-11-03T00:49:00.848907Z–00:49:00.863225Z; exit1 PermissionError
    reading pyvenv.cfg
  summary: Historical unavailable runner only. No new invocation or successful runner
    execution claimed; current official catalogue and primary/native fallback are
    separate.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: septin-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/adversary-septin/original-checks.json
  locator: Three actual native validate/render executions; all43 historical input
    occurrences
  summary: All three original native validations/renders pass and Markdown matches
    exactly. All43 input occurrences match historical source, including image. All
    current assigned records nonstale. Original batch26 global execution scopes are
    valid historical reuse, not fresh48 execution.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: ca3cb2d8017fbd564b706c4736300fa18a4388e8a7907463713d0f0338b838ea
- evidence_id: septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  kind: record_content
  reference: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
  locator: Complete maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,graphs,discussions/history and image metadata read. Target nonstale.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 16e82cc28bc358b34fa885dce05ecffea9022fbd529ce122ad9b31f2a0df68d5
- evidence_id: septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  kind: record_content
  reference: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Historical
    immutable observations and genuine batch26 execution origin retained.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 1fa225f21cd3d2930a4e54cdfd3f994163108873e1a0fdc2012c09748fa4bba1
- evidence_id: septin-native-core_tfiih_complex_portion_of_holo_tfiih_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Seven reviewed example occurrences/seven distinct accessions and
    seven COVERED typed nodes. Native identity/symbol validation does not prove formation,
    experimental strain or biological receptor assignment.
  accessed_at: '2026-11-04T04:03:53.558088Z'
  support: supports
  snapshot_sha256: f432c09eed6ff6321c8ff7fd46da5e7acd5f9a4fbcea21016e3745a13cc158f8
- evidence_id: septin-native-core_tfiih_complex_portion_of_holo_tfiih_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    --causal-graphs; logSHA256 645a9da180103d3b5c10abd60d0e572c1d5ea943ed7b589f189fde48e26b193c
  summary: Exit0. Seven reviewed example occurrences/seven distinct accessions and
    seven COVERED typed nodes. Native identity/symbol validation does not prove formation,
    experimental strain or biological receptor assignment.
  accessed_at: '2026-11-04T04:03:54.027346Z'
  support: supports
  snapshot_sha256: 1ba93c83742b6b5fccb1b83d7540cd995c7ab653b78108ce6cbac50b329cc458
- evidence_id: septin-record-core_tfiih_complex_portion_of_nef3_complex
  kind: record_content
  reference: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
  locator: Complete maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,graphs,discussions/history and image metadata read. Target nonstale.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 22ce0324ba1c1113c0ac5ef1d6e8642132923e6f6130a6d5aedeab654f0e8009
- evidence_id: septin-original-core_tfiih_complex_portion_of_nef3_complex
  kind: record_content
  reference: reviews/structured/20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Historical
    immutable observations and genuine batch26 execution origin retained.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: b68a43c5cfa5ecd68a3ebe58c3153365cfbf1608bb26c6c676b0c760b26a9e76
- evidence_id: septin-native-core_tfiih_complex_portion_of_nef3_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Seven reviewed example occurrences/seven distinct accessions and
    seven COVERED typed nodes. Native identity/symbol validation does not prove formation,
    experimental strain or biological receptor assignment.
  accessed_at: '2026-11-04T04:03:55.280440Z'
  support: supports
  snapshot_sha256: 434eafef4eaffb4b07f4fea9e02aaf84b082ec5c5476422bc414b9bfa616041f
- evidence_id: septin-native-core_tfiih_complex_portion_of_nef3_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    --causal-graphs; logSHA256 69dc56ef8abd646c00d891465ba1ffa7d3593f5bb887334d9130f40e4c8a5da4
  summary: Exit0. Seven reviewed example occurrences/seven distinct accessions and
    seven COVERED typed nodes. Native identity/symbol validation does not prove formation,
    experimental strain or biological receptor assignment.
  accessed_at: '2026-11-04T04:03:55.763365Z'
  support: supports
  snapshot_sha256: a721b573277bb3587a625ac89b39ae3043cd016f7445600789930f64a84cc685
- evidence_id: septin-record-crl4wdr1_ubiquitin_ligase_complex
  kind: record_content
  reference: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
  locator: Complete maintained record at e2498a28ea896fb9a053dc378380f1f44786a090
  summary: All identity/relations/components/examples/roles,functions/taxa,canonical
    notes,graphs,discussions/history and image metadata read. Target nonstale.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: 15951ee1c5321044ae8654b108d88de8388e09c2d10706fc7134d5ba32280ac4
- evidence_id: septin-original-crl4wdr1_ubiquitin_ligase_complex
  kind: record_content
  reference: reviews/structured/20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit/review.yaml
  locator: Complete original YAML and exact paired Markdown
  summary: Findings/actions/checks/scopes/limitations independently reassessed. Historical
    immutable observations and genuine batch26 execution origin retained.
  accessed_at: '2026-11-04T04:11:56.369495Z'
  support: supports
  snapshot_sha256: acb8e7f6bc72d13be11eca966f85f51069d051190a3de919f4f8e29e02e6fb50
- evidence_id: septin-native-crl4wdr1_ubiquitin_ligase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-verify-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    --verify; logSHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Exit0. Three unreviewed example occurrences/three distinct accessions and
    one COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not
    validate the disputed biological assignment. Native identity/symbol validation
    does not prove formation, experimental strain or biological receptor assignment.
  accessed_at: '2026-11-04T04:03:58.998839Z'
  support: supports
  snapshot_sha256: e84b6e702b099b571dc7951db7b9f58f62f909116b3a165fa8774095475eb18b
- evidence_id: septin-native-crl4wdr1_ubiquitin_ligase_complex-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-causal-receipt.json
  locator: Actual command .venv/bin/python scripts/uniprot_genes.py --record data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    --causal-graphs; logSHA256 fdf9c3bef748b6f4560e6e8ce8dde3a92ebb0e08a8417f04075ecc5a770c3b18
  summary: Exit0. Three unreviewed example occurrences/three distinct accessions and
    one COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not
    validate the disputed biological assignment. Native identity/symbol validation
    does not prove formation, experimental strain or biological receptor assignment.
  accessed_at: '2026-11-04T04:03:59.459436Z'
  support: supports
  snapshot_sha256: 3bdebd2e3006b0dfb8ca2a31b6b3b2cb30c8d0373cbdc5e27b81dc32949a64ba
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:09:20.010286Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: f044c109bf8a005825f7f68dde0e8b6e160ed3ce2e060e68eb7b2ee6f62ecb06
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:04:12.363501Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:03:48.228561Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:03:49.130406Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-04T04:04:14.068852Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-04T04:15:55Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 56a01af2191746f31fc64d69fc374aaf859b8fe5ed4f928d26eb660f451158bf
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-04T04:05:31.885217Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: b48fe7c6d2fc76bece71aa97b8d9b966b75b6b567018ca85f3d46386c6e3ccfd
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt; exact retained SHA256 reverified
    during PR2385 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is retained historical
    availability evidence, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
- evidence_id: root-native-cog_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:44.244046Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-cog_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/cog_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:44.726792Z'
  support: context_only
  snapshot_sha256: 825ab0ccb55c67c2e97fe7be7a80fd58d197894220e39b25c4fcbfc9941d1dd0
  summary: 8 represented protein examples; 8 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-coma_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:46.101888Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-coma_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/coma_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:46.588278Z'
  support: context_only
  snapshot_sha256: db466080285af73e715169620b9d5b400c92d8e428f3e7dd20065fa3e87865b1
  summary: 4 represented protein examples; 6 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-copi_vesicle_coat-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:47.975224Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-copi_vesicle_coat-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copi_vesicle_coat-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:48.441854Z'
  support: context_only
  snapshot_sha256: 62b80549c9d8c2786488904a26b8a4e91d32a624b11000f16ebce03c1fe02395
  summary: 9 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-copii_vesicle_coat-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:49.953193Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-copii_vesicle_coat-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/copii_vesicle_coat-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:50.417223Z'
  support: context_only
  snapshot_sha256: 7571c7db8734ce15009e2ddbae753cc8f2630ee35f7d15d5b98f6eab28929f55
  summary: 5 represented protein examples; 3 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-core_primosome_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:51.765475Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-core_primosome_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_primosome_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:52.221304Z'
  support: context_only
  snapshot_sha256: 86c84709c0661d272905360926d4aa86c7b0bd0e6e48bbddb4da91863801c0c1
  summary: 2 represented protein examples; 2 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:53.558088Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_holo_tfiih_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:54.027346Z'
  support: context_only
  snapshot_sha256: 645a9da180103d3b5c10abd60d0e572c1d5ea943ed7b589f189fde48e26b193c
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-core_tfiih_complex_portion_of_nef3_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:55.280440Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-core_tfiih_complex_portion_of_nef3_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/core_tfiih_complex_portion_of_nef3_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:55.763365Z'
  support: context_only
  snapshot_sha256: 69dc56ef8abd646c00d891465ba1ffa7d3593f5bb887334d9130f40e4c8a5da4
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-corvet_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:57.104140Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-corvet_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/corvet_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:57.585371Z'
  support: context_only
  snapshot_sha256: 7712e85ade0de1347ea909a9aaf2d0adab299bcdae10f215c03089983bbde0ff
  summary: 6 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-crl4wdr1_ubiquitin_ligase_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:58.998839Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-crl4wdr1_ubiquitin_ligase_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/crl4wdr1_ubiquitin_ligase_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:03:59.459436Z'
  support: context_only
  snapshot_sha256: fdf9c3bef748b6f4560e6e8ce8dde3a92ebb0e08a8417f04075ecc5a770c3b18
  summary: 3 represented protein examples; 1 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ctf18_rfc_like_complex-uniprot-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-verify.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:04:00.902854Z'
  support: context_only
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
- evidence_id: root-native-ctf18_rfc_like_complex-uniprot-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2385/ctf18_rfc_like_complex-uniprot-causal.log
  locator: Actual native command output; associated receipt binds command, source
    head, base and UTC interval
  accessed_at: '2026-11-04T04:04:01.344781Z'
  support: context_only
  snapshot_sha256: b77337cdd5a7bc8793f4ed2e383dc3ecee05ecee0677dc4c1b3314167dd0a613
  summary: 7 represented protein examples; 7 typed GENE_OR_PROTEIN nodes. Full native
    coverage classifications are retained in the command output. Actual exit0; inventory
    is distinct from biological claim and source-scope assessment.
assessments:
- assessment_id: micro-coma-identity
  area: identity
  topic: Exact COMA structure and boundaries
  outcome: supported
  summary: GO0000817 exactly denotes Ctf19/Okp1/Mcm21/Ame1 COMA; GO0140513 is_a and
    kinetochore/nuclear-chromosome parthood agree. Neither broader CCAN nor optional
    Nkp1/2 is forced into this four-subunit record. Native GO Mcm1 typo is deliberately
    not adopted.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-go-0000817
  - micro-go-0140513
  - micro-go-0000776
  - micro-go-0000228
  - micro-pmid-14633972
  - micro-schmitzberger2017-jats
- assessment_id: micro-coma-stale
  area: provenance
  topic: Substantive four-node/four-edge refresh
  outcome: supported
  summary: Current delta adds dated history, four component_ref protein nodes and
    constituent contributes_to edges. Native exact identities and genuine primary
    COMA composition support these edges. They do not claim atomic interfaces or resolve
    the two inherited grounding/association-evidence findings.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-delta-0
  - micro-schmitzberger2017-jats
  - micro-go-0000817
  - micro-native-coma_complex-causal
- assessment_id: micro-coma-family
  area: grounding
  topic: Exact Mcm21 family with other-subunit bounds
  outcome: concern
  summary: Current IPR018464 is a full CENP-O family explicitly including Mcm21 and
    directly linked by Q06675; retained REVIEWED_LABEL_ONLY is the inherited minor
    gap. AME1 domain IPR048743 and Ctf19 terminal-domain annotations do not automatically
    supply exact whole-protein identities for other rows.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR018464
  - micro-ipr-IPR048743
  - micro-up-Q06675
  - micro-up-P38313
  - micro-up-Q02732
  - micro-up-P53298
- assessment_id: micro-coma-examples
  area: grounding
  topic: Four exact reviewed reference proteins
  outcome: supported
  summary: Q02732CTF19/YPL018W, P53298OKP1/YGR179C, Q06675MCM21/YDR318W and P38313AME1/YBR211C
    are reviewed S288c559292 references. Fresh exact reviewed-gene queries return
    singleton maintained accessions. Native annotations/citations and primary physical
    membership remain distinct.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-tax-559292
  - micro-up-Q02732
  - micro-up-P53298
  - micro-up-Q06675
  - micro-up-P38313
  - micro-query-CTF19
  - micro-query-OKP1
  - micro-query-MCM21
  - micro-query-AME1
- assessment_id: micro-coma-localization
  area: evidence
  topic: Nuclear/kinetochore annotations and source tiers
  outcome: supported
  summary: Native accession comments and ECO0000269 citation joins support the selected
    nuclear/kinetochore annotations. Ortiz/Huh are freshly read only at abstract tier;
    Schmitzberger native localization text is body-read. No raw individual Huh images
    or all strain derivatives are certified.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-up-Q02732
  - micro-up-P53298
  - micro-up-Q06675
  - micro-up-P38313
  - micro-pmid-10323865
  - micro-pmid-14562095
  - micro-schmitzberger2017-jats
- assessment_id: micro-coma-formation
  area: grounding
  topic: Condition-scoped Okp1 physical-association evidence
  outcome: concern
  summary: Fresh Schmitzberger sec11 and Methods31 establish native S.cerevisiae Okp1Δ325–337
    loss of Ctf19 co-IP and Ctf19/Mcm21 localization, with Ame1/outer-kinetochore
    retention. This concrete bounded association/formation observation supports inherited
    F2; UNKNOWN itself is not a defect, and no universal ESSENTIAL/viability inference
    or mandatory new experiment follows.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-schema
  - micro-schmitzberger2017-jats
- assessment_id: micro-coma-composition
  area: evidence
  topic: Native versus recombinant composition and mechanism
  outcome: supported
  summary: DeWulf fresh abstract and Schmitzberger body support four-subunit COMA.
    K.lactis recombinant six-protein COMA-Nkp1-Nkp2 interaction/dimerization differs
    from native S.cerevisiae and does not force new whole-record stoichiometry or
    mandatory accessory components. Direct and indirect kinetochore contacts remain
    explicitly unresolved.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-pmid-14633972
  - micro-schmitzberger2017-jats
  - micro-pmid-23908374
- assessment_id: micro-coma-taxonomy
  area: scope
  topic: Species canonical context and reference strains
  outcome: supported
  summary: Species4932 canonical/distribution context is distinct from four S288c559292
    example annotations. Fresh native Schmitzberger methods specify most S288C derivatives
    with unread EV6 exceptions; no exact genotype is invented. COMMON remains qualitative
    ordinary machinery, not a strain census or universal claim.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-tax-4932
  - micro-tax-559292
  - micro-schema
  - micro-schmitzberger2017-jats
- assessment_id: micro-coma-graph
  area: graph
  topic: Bounded inner-to-outer kinetochore bridge
  outcome: supported
  summary: NONMECHANISTIC/ASSEMBLY outline retains grouped Cse4-proximal and Ndc80-complex
    outer nodes, with separately verified P36012/P40460/P33895/Q04477. Spc24 participation
    in outer attachment machinery is not a direct Spc24–microtubule assertion. Four
    new constituent edges are supported; primary sec15/16 distinctions between interactions
    and localization remain.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-graph-policy
  - micro-schmitzberger2017-jats
  - micro-up-P36012
  - micro-up-P40460
  - micro-up-P33895
  - micro-up-Q04477
- assessment_id: micro-primosome-identity
  area: identity
  topic: Generic DNA-bound core versus narrower examples
  outcome: supported
  summary: GO1990098 exactly denotes the helicase/primase/DNA core, parent1990077.
    Preprimase1990099 and protein-only DnaB-DnaG1990156 remain distinct, not mandatory
    generic constituents. The resolved boundary discussion correctly avoids reducing
    the whole record to its bacterial protein-only example.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-go-1990098
  - micro-go-1990077
  - micro-go-1990099
  - micro-go-1990156
- assessment_id: micro-primosome-classes
  area: grounding
  topic: Generic classes not incorrectly forced to bacterial families
  outcome: supported
  summary: Replicative helicase and DNA primase are legitimate generic classes; DnaB
    IPR007692 and DnaG IPR050219 are narrower bacterial examples, while IPR006295
    is a domain. No exact universal class identity is fabricated; reviewed label-only
    discussions and DNA template distinction remain bounded.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-policy
  - micro-ipr-IPR007692
  - micro-ipr-IPR006295
  - micro-ipr-IPR050219
- assessment_id: micro-primosome-proteins
  area: grounding
  topic: Exact K12 reference examples
  outcome: supported
  summary: Reviewed P0ACB0dnaB b4052/JW4012 and P0ABS5dnaG b3066/JW3038 agree with
    tax83333 and fresh singleton exact gene queries. Selection does not assert universality
    of these bacterial families across every primosome.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-up-P0ACB0
  - micro-up-P0ABS5
  - micro-query-dnaB
  - micro-query-dnaG
  - micro-tax-83333
- assessment_id: micro-primosome-function
  area: evidence
  topic: Primer synthesis and secondary review scope
  outcome: supported
  summary: GO0006269 primer synthesis and Kaguni secondary body support the E.coli
    oriC initiation/elongation context. Prepriming precedes DnaG addition; DnaG interactions
    during elongation are transient. The review is not misrepresented as a primary
    experiment and does not prove every generic mechanism or complete loader stoichiometry.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-go-0006269
  - micro-kaguni2011-jats
  - micro-pmid-21856207
- assessment_id: micro-primosome-formation
  area: grounding
  topic: No invented universal formation requirement
  outcome: unknown
  summary: Current UNKNOWN fields and broad DNA template are appropriately bounded.
    General replication function and representative protein identity do not establish
    a cross-taxon depletion/formation matrix; no missing optional assay or exact chemistry
    is manufactured into a finding.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-schema
  - micro-policy
  - micro-kaguni2011-jats
- assessment_id: micro-primosome-taxonomy
  area: scope
  topic: Bacterial synthesis and K12 reference context
  outcome: supported
  summary: Canonical species562 E.coli synthesis in Kaguni is distinct from reference
    tax83333 and computational five-strain precise1k data. COMMON is qualitative;
    neither source alone establishes every strain or alternative replisome system.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-tax-562
  - micro-tax-83333
  - micro-kaguni2011-jats
  - micro-ecoli-meta
- assessment_id: micro-primosome-graph
  area: graph
  topic: Nonmechanistic primer-synthesis outline
  outcome: supported
  summary: Helicase/primase/DNA contributions and broad primer formation agree with
    FUNCTION/NONMECHANISTIC scope. The maintained graph does not assert exact initiation
    order, atomic contact or universal DnaB/DnaG stoichiometry; native two-node diagnostic
    passes.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-graph-policy
  - micro-go-1990098
  - micro-go-0006269
  - micro-kaguni2011-jats
  - micro-native-core_primosome_complex-causal
- assessment_id: micro-primosome-module
  area: scope
  topic: Actual matched-host expression dataset and threshold context
  outcome: supported
  summary: Selected precise1k spans five named E.coli strains. b3066/dnaG exceeds
    module10 threshold; b4052/dnaB exceeds none among201. Module10 has15genes, regulator=null
    and nucleotide-stress context. Alias-query noncoverage is not absence; generated
    module prose/activity interpretation is not used. These results do not establish
    primosome assembly, localization, necessity or causal regulation.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-ecoli-meta
  - micro-ecoli-modules
  - micro-ecoli-b4052
  - micro-ecoli-b3066
  - micro-ecoli-JW4012
  - micro-ecoli-JW3038
  - micro-ecoli-module-10
  - micro-catalogue
- assessment_id: micro-ctf18-identity
  area: identity
  topic: Exact alternative seven-subunit RFC-like complex
  outcome: supported
  summary: 'GO0031390 exact definition/synonyms and GO0140513 is_a relation agree:
    Ctf18/Dcc1/Ctf8 plus RFC2–5. Native Mayer primary abstract identifies this alternative
    complex, distinct from RFC1/Rad24-containing loaders and from PCNA client.'
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-go-0031390
  - micro-go-0140513
  - micro-pmid-11389843
  - micro-pmid-14614842
- assessment_id: micro-ctf18-families
  area: grounding
  topic: Three exact family identities versus shared small-RFC scope
  outcome: concern
  summary: IPR053016 Ctf18, IPR019128 Dcc1 and IPR018607 Ctf8 are exact families;
    three current rows remain REVIEWED_LABEL_ONLY. Dcc1/Ctf8 native examples link
    their families; reviewed ortholog members separately support IPR053016 identity
    without falsely claiming a P49956 xref. Shared IPR050238 and AAA/RFC domains do
    not distinguish RFC2–5. Generated prose is excluded from biology.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR053016
  - micro-ipr-IPR019128
  - micro-ipr-IPR018607-retry
  - micro-ipr-IPR050238-retry
  - micro-family-CTF18
  - micro-up-P49956
  - micro-up-P25559
  - micro-up-P38877
- assessment_id: micro-ctf18-examples
  area: grounding
  topic: Seven exact reviewed reference examples
  outcome: supported
  summary: All seven maintained accessions, native primary genes/loci and S288c559292
    taxa are correct; fresh reviewed-gene queries each return the intended singleton.
    Reference identity and family coverage do not by themselves prove all molecular
    activities.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-tax-559292
  - micro-up-P49956
  - micro-up-P40348
  - micro-up-P38629
  - micro-up-P40339
  - micro-up-P38251
  - micro-up-P25559
  - micro-up-P38877
  - micro-query-CTF18
  - micro-query-RFC2
  - micro-query-RFC3
  - micro-query-RFC4
  - micro-query-RFC5
  - micro-query-DCC1
  - micro-query-CTF8
- assessment_id: micro-ctf18-localization
  area: evidence
  topic: Ctf8 nuclear annotation and abstract limits
  outcome: supported
  summary: Native P38877 nuclear localization annotation carries PMID11389843/ECO0000269;
    the source is freshly inspected only at complete primary-abstract tier. This verifies
    the authority attribution without claiming the actual microscopy images or full
    experimental localization protocol were read.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-up-P38877
  - micro-pmid-11389843
- assessment_id: micro-ctf18-formation
  area: grounding
  topic: Membership/cohesion distinct from formation necessity
  outcome: unknown
  summary: Mayer primary abstract supports seven-member association and cohesion phenotypes;
    deletion growth/cohesion is not a complete assembly-depletion matrix. UNKNOWN
    formation fields remain bounded; no compulsory optional assay or universal ESSENTIAL
    assertion is introduced.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-schema
  - micro-policy
  - micro-pmid-11389843
- assessment_id: micro-ctf18-functions
  area: evidence
  topic: Clamp loading and cohesion scope
  outcome: supported
  summary: GO0031390/0003689/0007062 and Kim-MacNeill secondary abstract support alternative
    clamp-loading/cohesion context. Mayer is primary abstract-only; no detailed purified
    loading cycle or individual mechanistic sequence is certified.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-go-0031390
  - micro-go-0003689
  - micro-go-0007062
  - micro-pmid-11389843
  - micro-pmid-14614842
- assessment_id: micro-ctf18-taxonomy
  area: scope
  topic: Species and strain distinction
  outcome: supported
  summary: Species4932 canonical context is distinct from seven S288c559292 reference
    examples. The abstract supports S.cerevisiae without demonstrating every precise
    genotype; no strain substitution or numerical prevalence inference is made.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-tax-4932
  - micro-tax-559292
  - micro-pmid-11389843
  - micro-schema
- assessment_id: micro-ctf18-graph
  area: graph
  topic: Seven constituents and two bounded functions
  outcome: supported
  summary: Seven component_ref contributions to the alternative clamp loader and clamp-loading/cohesion
    outputs fit FUNCTION/NONMECHANISTIC. PCNA is a client, not forced into constituent
    inventory; no unsupported ATPase order or universal necessity is asserted.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-graph-policy
  - micro-go-0031390
  - micro-go-0003689
  - micro-go-0007062
  - micro-native-ctf18_rfc_like_complex-causal
- assessment_id: micro-adapter-0
  area: scope
  topic: Original exclusion corrected by actual host assessment
  outcome: concern
  summary: Original formal check excludes iModulonDB only because no expression-module
    assertion exists, despite positive protein/pathway content. Native policy requires
    applicability. Fresh catalogue gives no natural yeast match for COMA/Ctf18; primosome
    has selected E.coli precise1k gene/module evidence with explicit five-strain and
    threshold limits. Historical unavailable runner remains separately dated.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-0
  area: provenance
  topic: Historical discussion and immutable lineage
  outcome: supported
  summary: All original findings/actions and current discussions reviewed. Dated rationale/posed_date/history
    remain append-only; source-neutral grounding TODOs are not automatically resolved
    by taxon-specific examples. Proposed curation narrows current notes/prompt only
    after supported changes; records remain untouched.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-policy
  - micro-original-audit
  - micro-delta-0
- assessment_id: micro-schema-0
  area: schema
  topic: Original deterministic artifacts and actual native coverage
  outcome: supported
  summary: 'Three original pairs validate/render exactly with41 frozen historical
    inputs and six immutable artifacts. Current own native checks pass: COMA4examples/6typed(4COVERED+2unanchoredxref),
    primosome2/2covered, Ctf18RFC7/7covered. These results are not biological proof
    or family-completeness certificates.'
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-original-audit
  - micro-native-coma_complex-verify
  - micro-native-coma_complex-causal
- assessment_id: micro-coverage-0
  area: completeness
  topic: Whole-record coverage with explicit access boundaries
  outcome: supported
  summary: Complete maintained record and original assessment inspected; no local
    images/quantitative properties present. Source body/abstract/authority tiers remain
    explicit; no raw microscopy, sequence alignments, supplemental strain table or
    cited primary work not read is certified.
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-prior-0
- assessment_id: micro-verdict-0
  area: other
  topic: Current independent disposition
  outcome: concern
  summary: 'needs_curation: two inherited minor findings independently confirmed;
    current COMA additions valid and no new scientific finding.'
  target_ids:
  - GO:0000817
  evidence_ids:
  - micro-record-0
  - micro-prior-0
  - micro-schmitzberger2017-jats
  - micro-ipr-IPR018464
- assessment_id: micro-adapter-1
  area: scope
  topic: Original exclusion corrected by actual host assessment
  outcome: concern
  summary: Original formal check excludes iModulonDB only because no expression-module
    assertion exists, despite positive protein/pathway content. Native policy requires
    applicability. Fresh catalogue gives no natural yeast match for COMA/Ctf18; primosome
    has selected E.coli precise1k gene/module evidence with explicit five-strain and
    threshold limits. Historical unavailable runner remains separately dated.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
  - micro-ecoli-meta
  - micro-ecoli-b4052
  - micro-ecoli-b3066
  - micro-ecoli-module-10
- assessment_id: micro-history-1
  area: provenance
  topic: Historical discussion and immutable lineage
  outcome: supported
  summary: All original findings/actions and current discussions reviewed. Dated rationale/posed_date/history
    remain append-only; source-neutral grounding TODOs are not automatically resolved
    by taxon-specific examples. Proposed curation narrows current notes/prompt only
    after supported changes; records remain untouched.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-policy
  - micro-original-audit
  - micro-delta-1
- assessment_id: micro-schema-1
  area: schema
  topic: Original deterministic artifacts and actual native coverage
  outcome: supported
  summary: 'Three original pairs validate/render exactly with41 frozen historical
    inputs and six immutable artifacts. Current own native checks pass: COMA4examples/6typed(4COVERED+2unanchoredxref),
    primosome2/2covered, Ctf18RFC7/7covered. These results are not biological proof
    or family-completeness certificates.'
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-original-audit
  - micro-native-core_primosome_complex-verify
  - micro-native-core_primosome_complex-causal
- assessment_id: micro-coverage-1
  area: completeness
  topic: Whole-record coverage with explicit access boundaries
  outcome: supported
  summary: Complete maintained record and original assessment inspected; no local
    images/quantitative properties present. Source body/abstract/authority tiers remain
    explicit; no raw microscopy, sequence alignments, supplemental strain table or
    cited primary work not read is certified.
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-prior-1
- assessment_id: micro-verdict-1
  area: other
  topic: Current independent disposition
  outcome: supported
  summary: 'pass_with_limitations: positive identity, class and function assessments;
    generic formation and source-access limits remain, no scientific finding.'
  target_ids:
  - GO:1990098
  evidence_ids:
  - micro-record-1
  - micro-prior-1
  - micro-kaguni2011-jats
  - micro-go-1990098
- assessment_id: micro-adapter-2
  area: scope
  topic: Original exclusion corrected by actual host assessment
  outcome: concern
  summary: Original formal check excludes iModulonDB only because no expression-module
    assertion exists, despite positive protein/pathway content. Native policy requires
    applicability. Fresh catalogue gives no natural yeast match for COMA/Ctf18; primosome
    has selected E.coli precise1k gene/module evidence with explicit five-strain and
    threshold limits. Historical unavailable runner remains separately dated.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-native-policy
  - micro-catalogue
  - micro-historical-runner
- assessment_id: micro-history-2
  area: provenance
  topic: Historical discussion and immutable lineage
  outcome: supported
  summary: All original findings/actions and current discussions reviewed. Dated rationale/posed_date/history
    remain append-only; source-neutral grounding TODOs are not automatically resolved
    by taxon-specific examples. Proposed curation narrows current notes/prompt only
    after supported changes; records remain untouched.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-policy
  - micro-original-audit
  - micro-delta-2
- assessment_id: micro-schema-2
  area: schema
  topic: Original deterministic artifacts and actual native coverage
  outcome: supported
  summary: 'Three original pairs validate/render exactly with41 frozen historical
    inputs and six immutable artifacts. Current own native checks pass: COMA4examples/6typed(4COVERED+2unanchoredxref),
    primosome2/2covered, Ctf18RFC7/7covered. These results are not biological proof
    or family-completeness certificates.'
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-original-audit
  - micro-native-ctf18_rfc_like_complex-verify
  - micro-native-ctf18_rfc_like_complex-causal
- assessment_id: micro-coverage-2
  area: completeness
  topic: Whole-record coverage with explicit access boundaries
  outcome: supported
  summary: Complete maintained record and original assessment inspected; no local
    images/quantitative properties present. Source body/abstract/authority tiers remain
    explicit; no raw microscopy, sequence alignments, supplemental strain table or
    cited primary work not read is certified.
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-prior-2
- assessment_id: micro-verdict-2
  area: other
  topic: Current independent disposition
  outcome: concern
  summary: 'needs_curation: one inherited minor exact-family subset finding independently
    confirmed; other supported scopes retained.'
  target_ids:
  - GO:0031390
  evidence_ids:
  - micro-record-2
  - micro-prior-2
  - micro-ipr-IPR053016
  - micro-ipr-IPR019128
  - micro-ipr-IPR018607-retry
- assessment_id: plaque-t0-native-schema
  area: schema
  topic: native schema
  outcome: supported
  summary: 8 REVIEWED examples/8 typed nodes; all typed nodes COVERED. Historical
    original and current input checks pass; source identity remains independent of
    sequence coverage.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-original-current-validation
  - plaque-schema
  - plaque-review-schema
  - plaque-native-cog_complex-verify
  - plaque-native-cog_complex-causal
- assessment_id: plaque-t0-identity-scope
  area: identity
  topic: identity scope
  outcome: supported
  summary: Exact active GO identity and coat/tethering boundaries match. Species4932
    canonical scope is distinct from reviewed reference strain559292 and the actual
    laboratory or recombinant preparations. The record is a complex/coat, not a single
    protein.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-go
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t0-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Full record read; no maintained image or numeric physical-property observation
    requiring pixel/measurement verification. Optional examples, additional variable
    adaptors and exhaustive paralog inventories are not required. No unsupported mandatory
    experiment is imposed.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t0-structured-source
  area: evidence
  topic: structured source
  outcome: supported
  summary: Positive protein/traffic/tethering claims trigger coverage review. Original
    checks[4] formal no-expression exemption is unsupported. Fresh catalogue has no
    matching biological host, so no downstream foreign-organism proxy is used. Historical00:49Z
    runner failure remains historical; no fresh runner execution claimed.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-original-0-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-bounded-search
- assessment_id: plaque-t0-historical-provenance
  area: provenance
  topic: historical provenance
  outcome: supported
  summary: Original frozen input is identical to current target; native pair/render
    and source inputs verified. Exact inherited F1 lineage retained, no blanket category
    or neighboring issue resolution inferred; dated rationale remains append-only.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-original-0-yaml
  - plaque-original-current-validation
  - plaque-policy
- assessment_id: plaque-t0-necessity
  area: scope
  topic: necessity
  outcome: supported
  summary: UNKNOWN formation essentiality is retained. Functional transport defects,
    viability, interaction or reconstituted assembly under selected conditions are
    not automatically universal structure-formation necessity. Broad grouped components
    and external interactors are permitted.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-policy
  - plaque-schema
  - plaque-ha2016-s3
  - plaque-ishii2018-s3
- assessment_id: plaque-t2-native-schema
  area: schema
  topic: native schema
  outcome: supported
  summary: 9 REVIEWED examples/2 typed nodes; all typed nodes COVERED. Historical
    original and current input checks pass; source identity remains independent of
    sequence coverage.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-original-current-validation
  - plaque-schema
  - plaque-review-schema
  - plaque-native-copi_vesicle_coat-verify
  - plaque-native-copi_vesicle_coat-causal
- assessment_id: plaque-t2-identity-scope
  area: identity
  topic: identity scope
  outcome: supported
  summary: Exact active GO identity and coat/tethering boundaries match. Species4932
    canonical scope is distinct from reviewed reference strain559292 and the actual
    laboratory or recombinant preparations. The record is a complex/coat, not a single
    protein.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-go
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t2-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Full record read; no maintained image or numeric physical-property observation
    requiring pixel/measurement verification. Optional examples, additional variable
    adaptors and exhaustive paralog inventories are not required. No unsupported mandatory
    experiment is imposed.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t2-structured-source
  area: evidence
  topic: structured source
  outcome: supported
  summary: Positive protein/traffic/tethering claims trigger coverage review. Original
    notes[1] prose-only no-applicability exemption is unsupported. Fresh catalogue
    has no matching biological host, so no downstream foreign-organism proxy is used.
    Historical00:49Z runner failure remains historical; no fresh runner execution
    claimed.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-bounded-search
- assessment_id: plaque-t2-historical-provenance
  area: provenance
  topic: historical provenance
  outcome: supported
  summary: Original frozen input is identical to current target; native pair/render
    and source inputs verified. Exact inherited F1 lineage retained, no blanket category
    or neighboring issue resolution inferred; dated rationale remains append-only.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-original-2-yaml
  - plaque-original-current-validation
  - plaque-policy
- assessment_id: plaque-t2-necessity
  area: scope
  topic: necessity
  outcome: supported
  summary: UNKNOWN formation essentiality is retained. Functional transport defects,
    viability, interaction or reconstituted assembly under selected conditions are
    not automatically universal structure-formation necessity. Broad grouped components
    and external interactors are permitted.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-schema
  - plaque-yu2012-body
- assessment_id: plaque-t3-native-schema
  area: schema
  topic: native schema
  outcome: supported
  summary: 5 REVIEWED examples/3 typed nodes; all typed nodes COVERED. Historical
    original and current input checks pass; source identity remains independent of
    sequence coverage.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-original-current-validation
  - plaque-schema
  - plaque-review-schema
  - plaque-native-copii_vesicle_coat-verify
  - plaque-native-copii_vesicle_coat-causal
- assessment_id: plaque-t3-identity-scope
  area: identity
  topic: identity scope
  outcome: supported
  summary: Exact active GO identity and coat/tethering boundaries match. Species4932
    canonical scope is distinct from reviewed reference strain559292 and the actual
    laboratory or recombinant preparations. The record is a complex/coat, not a single
    protein.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-go
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t3-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Full record read; no maintained image or numeric physical-property observation
    requiring pixel/measurement verification. Optional examples, additional variable
    adaptors and exhaustive paralog inventories are not required. No unsupported mandatory
    experiment is imposed.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t3-structured-source
  area: evidence
  topic: structured source
  outcome: supported
  summary: Positive protein/traffic/tethering claims trigger coverage review. Original
    notes[1] prose-only no-applicability exemption is unsupported. Fresh catalogue
    has no matching biological host, so no downstream foreign-organism proxy is used.
    Historical00:49Z runner failure remains historical; no fresh runner execution
    claimed.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-bounded-search
- assessment_id: plaque-t3-historical-provenance
  area: provenance
  topic: historical provenance
  outcome: supported
  summary: Original frozen input is identical to current target; native pair/render
    and source inputs verified. Exact inherited F1 lineage retained, no blanket category
    or neighboring issue resolution inferred; dated rationale remains append-only.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-original-3-yaml
  - plaque-original-current-validation
  - plaque-policy
- assessment_id: plaque-t3-necessity
  area: scope
  topic: necessity
  outcome: supported
  summary: UNKNOWN formation essentiality is retained. Functional transport defects,
    viability, interaction or reconstituted assembly under selected conditions are
    not automatically universal structure-formation necessity. Broad grouped components
    and external interactors are permitted.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-schema
  - plaque-matsuoka1998-pdf
- assessment_id: plaque-t7-native-schema
  area: schema
  topic: native schema
  outcome: supported
  summary: 6 REVIEWED examples/7 typed nodes; six COVERED constituents and one externally
    anchored Vps21 interactor (UNANCHORED_WITH_UNIPROT), not a missing seventh constituent.
    Historical original and current input checks pass; source identity remains independent
    of sequence coverage.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-original-current-validation
  - plaque-schema
  - plaque-review-schema
  - plaque-native-corvet_complex-verify
  - plaque-native-corvet_complex-causal
- assessment_id: plaque-t7-identity-scope
  area: identity
  topic: identity scope
  outcome: supported
  summary: Exact active GO identity and coat/tethering boundaries match. Species4932
    canonical scope is distinct from reviewed reference strain559292 and the actual
    laboratory or recombinant preparations. The record is a complex/coat, not a single
    protein.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-go
  - plaque-tax-4932
  - plaque-tax-559292
- assessment_id: plaque-t7-completeness
  area: completeness
  topic: completeness
  outcome: supported
  summary: Full record read; no maintained image or numeric physical-property observation
    requiring pixel/measurement verification. Optional examples, additional variable
    adaptors and exhaustive paralog inventories are not required. No unsupported mandatory
    experiment is imposed.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-policy
  - plaque-checklist
- assessment_id: plaque-t7-structured-source
  area: evidence
  topic: structured source
  outcome: supported
  summary: Positive protein/traffic/tethering claims trigger coverage review. Original
    notes[1] prose-only no-applicability exemption is unsupported. Fresh catalogue
    has no matching biological host, so no downstream foreign-organism proxy is used.
    Historical00:49Z runner failure remains historical; no fresh runner execution
    claimed.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-original-7-yaml
  - plaque-review-skill
  - plaque-catalogue
  - plaque-catalogue-bounded-search
- assessment_id: plaque-t7-historical-provenance
  area: provenance
  topic: historical provenance
  outcome: supported
  summary: Original frozen input is identical to current target; native pair/render
    and source inputs verified. Exact inherited F1 lineage retained, no blanket category
    or neighboring issue resolution inferred; dated rationale remains append-only.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-original-7-yaml
  - plaque-original-current-validation
  - plaque-policy
- assessment_id: plaque-t7-necessity
  area: scope
  topic: necessity
  outcome: supported
  summary: UNKNOWN formation essentiality is retained. Functional transport defects,
    viability, interaction or reconstituted assembly under selected conditions are
    not automatically universal structure-formation necessity. Broad grouped components
    and external interactors are permitted.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-policy
  - plaque-schema
  - plaque-paper-1
- assessment_id: plaque-t0-family-grounding
  area: grounding
  topic: family grounding
  outcome: concern
  summary: Eight exact named generic COG classes are represented by IPR033370/009316/007265/048682/019465/010490/019335/007255.
    Five yeast instances carry their corresponding whole-family annotation; Cog1/2/7
    do not, so class grounding must not be misrepresented as new sequence annotation.
    Reviewed ortholog-member queries and primary divergent-ortholog context support
    the class interpretation.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-policy
  - plaque-paper-4
  - plaque-ipr-IPR033370
  - plaque-ipr-IPR009316
  - plaque-ipr-retry-IPR007265
  - plaque-ipr-retry-IPR048682
  - plaque-ipr-retry-IPR019465
  - plaque-ipr-IPR010490
  - plaque-ipr-IPR019335
  - plaque-ipr-IPR007255
  - plaque-ipr-IPR006687
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR032914
  - plaque-ipr-retry-IPR045111
  - plaque-ipr-IPR007810
  - plaque-ipr-retry-IPR001619
  - plaque-family-IPR033370
  - plaque-family-IPR009316
  - plaque-family-IPR019335
  - plaque-protein-P53079
  - plaque-protein-P53271
  - plaque-protein-P53195
- assessment_id: plaque-t0-composition-architecture
  area: representation
  topic: composition architecture
  outcome: supported
  summary: The eight subunits and lobeA1–4/lobeB5–8 match COG architecture. Ha uses
    recombinant yeast-sequence COG produced in E.coli; separate Kluyveromyces lobe-B
    work is not conflated. Ishii distinguishes cytosolic octamer from membrane subassemblies.
    COPI/SNARE interactions do not add constituents.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-ha2016-s3
  - plaque-ishii2018-s3
  - plaque-paper-5
  - plaque-paper-6
  - plaque-protein-P53079
  - plaque-protein-P53271
  - plaque-protein-P40094
  - plaque-protein-Q06096
  - plaque-protein-P53951
  - plaque-protein-P53959
  - plaque-protein-P53195
  - plaque-protein-Q04632
- assessment_id: plaque-t0-graph-localization
  area: graph
  topic: graph localization
  outcome: supported
  summary: NONMECHANISTIC membership and Golgi-transport participation are bounded.
    Removed mammalian-backed yeast localization is not reintroduced. Native Cog3/Cog2
    experimental Golgi annotations have specific yeast source joins; other Cog localization
    annotations largely by similarity remain distinct.
  target_ids:
  - GO:0017119
  evidence_ids:
  - plaque-current-0
  - plaque-paper-10
  - plaque-paper-11
  - plaque-paper-18
  - plaque-paper-23
  - plaque-protein-P40094
  - plaque-protein-P53271
  - plaque-ha2016-s3
- assessment_id: plaque-t2-protein-selection
  area: grounding
  topic: protein selection
  outcome: concern
  summary: All nine reviewed instances agree with declared coatomer/Arf symbols and
    aliases. P53622 primary COP1 aliasRET1 remains correct, but the exact reviewed559292
    RET1 query also returns polymeraseP22276; inherited F1 corrects current uniqueness
    provenance only.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-gene-RET1
  - plaque-protein-P41810
  - plaque-protein-P41811
  - plaque-protein-P32074
  - plaque-protein-P43621
  - plaque-protein-P40509
  - plaque-protein-P53600
  - plaque-protein-P53622
  - plaque-protein-P11076
  - plaque-protein-P19146
- assessment_id: plaque-t2-experimental-graph
  area: graph
  topic: experimental graph
  outcome: supported
  summary: Coarse coatomer/Arf association, membrane-coat membership, Golgi context
    and retrieval are supported. Yu mixed-species recombinant structural/biochemical
    work supplies a recruitment model, not an intact live yeast assembly cycle. Sandmann
    complete abstract supports yeast retrieval/KKXX scope; no inaccessible body claims
    made.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-yu2012-body
  - plaque-paper-2
  - plaque-paper-7
  - plaque-access-limitations
  - plaque-go
- assessment_id: plaque-t2-native-localization
  area: evidence
  topic: native localization
  outcome: supported
  summary: Arf1Golgi evidence joins15504911, Arf2/Sec26 joins14562095; native source
    attribution checked alongside complete primary abstracts. Database by-similarity
    annotations for other coatomer proteins are not portrayed as independently read
    direct experiments.
  target_ids:
  - GO:0030126
  evidence_ids:
  - plaque-current-2
  - plaque-protein-P11076
  - plaque-protein-P19146
  - plaque-protein-P41810
  - plaque-paper-18
  - plaque-paper-19
- assessment_id: plaque-t3-sar1-grounding
  area: grounding
  topic: sar1 grounding
  outcome: concern
  summary: Exact whole SAR1 family IPR006687 matches current Sar1 class and nativeP20606
    cross-reference. This does not ground the distinct Sec23/24 or Sec13/31 heteromeric
    components with single-protein families.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-ipr-IPR006687
  - plaque-protein-P20606
  - plaque-policy
- assessment_id: plaque-t3-composition-protein
  area: representation
  topic: composition protein
  outcome: supported
  summary: Five core examples agree with their identities and coarse coat roles. Sec13
    is shared with NPC/SEA; Rout2000 is explicitly NPC-localization evidence, not
    false COPII membership proof. Variable Sfb2/Lst1 cargo coats do not make the stated
    core inventory an exhaustive-variable-coat claim.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-protein-P20606
  - plaque-protein-P15303
  - plaque-protein-P40482
  - plaque-protein-Q04491
  - plaque-protein-P38968
  - plaque-paper-12
  - plaque-paper-14
  - plaque-paper-16
- assessment_id: plaque-t3-assembly-graph
  area: graph
  topic: assembly graph
  outcome: supported
  summary: Sequential Sar1 membrane recruitment then Sec23/24 and Sec13/31 is supported
    in defined reconstitution. Native/defined membrane stoichiometries, size, nucleotide
    conditions and fixed-sample EM are distinguished. NONMECHANISTIC graph does not
    claim a complete universal cargo/hydrolysis cycle or invariant stoichiometry.
  target_ids:
  - GO:0030127
  evidence_ids:
  - plaque-current-3
  - plaque-paper-20
  - plaque-paper-21
  - plaque-paper-13
  - plaque-paper-17
  - plaque-matsuoka1998-pdf
  - plaque-zanetti2013-s3
- assessment_id: plaque-t7-exact-families
  area: grounding
  topic: exact families
  outcome: concern
  summary: Vps11/Pep5 IPR016528 and Vps16 IPR016534 match named whole-protein classes
    and verified instances. Vps3/Vps39, Vps8/Vps41, Sec1 broad families and Vps18
    domain are excluded; shared HOPS membership does not invalidate exact protein-class
    identity.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-protein-P12868
  - plaque-protein-Q03308
  - plaque-ipr-IPR032914
  - plaque-ipr-retry-IPR045111
  - plaque-ipr-IPR007810
  - plaque-ipr-retry-IPR001619
  - plaque-policy
- assessment_id: plaque-t7-composition-interactors
  area: representation
  topic: composition interactors
  outcome: supported
  summary: Six native examples match Vps3,Vps8,Pep5/Vps11,Vps16,Pep3/Vps18,Vps33 aliases/loci.
    Peplowska primary abstract and exact GO support six-subunit CORVET/shared classC
    core. Vps21 is an external Rab interactor, not a seventh constituent.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-paper-1
  - plaque-go
  - plaque-protein-P23643
  - plaque-protein-P39702
  - plaque-protein-P12868
  - plaque-protein-Q03308
  - plaque-protein-P27801
  - plaque-protein-P20795
  - plaque-protein-P36017
- assessment_id: plaque-t7-localization-graph
  area: graph
  topic: localization graph
  outcome: supported
  summary: Descriptive CORVET/Vps21/endosome biogenesis graph is supported at primary-abstract/authority
    scope, not detailed unread direct-binding Methods. PEP5 vacuole-membrane evidence
    from Seals concerns HOPS/shared protein; record keeps it separate from CORVET-specific
    endosome scope.
  target_ids:
  - GO:0033263
  evidence_ids:
  - plaque-current-7
  - plaque-paper-1
  - plaque-paper-15
  - plaque-protein-P12868
  - plaque-go
  - plaque-access-limitations
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-identity
  area: identity
  topic: Structure identity and containing-complex boundary
  outcome: supported
  summary: Seven-subunit TFIIH core portion has exact GO identity; TFIIK partner remains
    outside holo core.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-grounding
  area: grounding
  topic: Exact molecular identity versus broad family
  outcome: concern
  summary: All seven exact InterPro full-protein families are independently corroborated
    by reviewed example xrefs. IPR001945 mixed XPG/Rad2 prose does not override the
    independently matched RAD3/XPD name/member identity; broad generic domains are
    not substitutes.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-curation-policy
  - septin-rad3-family-members
  - septin-ipr-IPR001161
  - septin-ipr-IPR027079
  - septin-ipr-IPR004598
  - septin-retry-IPR012170
  - septin-ipr-IPR004600
  - septin-retry-IPR009400
  - septin-retry-IPR001945
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-proteins
  area: grounding
  topic: Native accession/status/primary-name and source-locus identity
  outcome: supported
  summary: Seven reviewed example occurrences/seven distinct accessions and seven
    COVERED typed nodes. Current reviewed exact yeast queries return the intended
    seven genes. Huh nuclear localization is distinct from core membership and functional
    necessity.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-protein-policy
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-protein-Q00578
  - septin-protein-P32776
  - septin-protein-Q02939
  - septin-protein-Q04673
  - septin-protein-Q12004
  - septin-protein-Q3E7C1
  - septin-protein-P06839
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-evidence
  area: evidence
  topic: Actual source access and experiment scopes
  outcome: supported
  summary: Murakami genuine body sections and canonical ontology/native annotations
    support composition; Takagi,Ranish,Huh current access is complete metadata/abstract,
    not unread full bodies.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-literature-policy
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-formation
  area: evidence
  topic: Formation necessity versus functional dependence
  outcome: unknown
  summary: All seven formation-necessity fields remain UNKNOWN. Transcription/DNA-repair
    defects and purified subcomplex behavior do not establish universal obligatory
    formation sequence; Tfb6-dependent alternative purification states remain experimental
    context.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-graph
  area: graph
  topic: Complete descriptive graph and evidence mapping
  outcome: supported
  summary: ASSEMBLY/NONMECHANISTIC seven constituent links plus holo parthood describe
    coarse composition without kinase chemistry or ordered assembly.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-graph-policy
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-taxon
  area: scope
  topic: Canonical lineage and reference-versus-assay strains
  outcome: supported
  summary: Saccharomyces4932 and S288C559292 resolve; Murakami multiple yeast backgrounds
    and bacterial production hosts are not silently equated to reference examples.
    COMMON is qualitative, not population prevalence.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-tax4932
  - septin-tax559292
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-quantity
  area: quantity
  topic: Composition, time and size claims
  outcome: supported
  summary: Canonical seven-core versus three-TFIIK partition is distinguished from
    Tfb6-associated11-subunit purification and dissociated states; no universal fixed
    assembly stoichiometry or physical dimension is inferred.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-image
  area: evidence
  topic: Maintained image and attribution
  outcome: not_applicable
  summary: No maintained image on this target.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-schema
  area: schema
  topic: Original schema/render and frozen source inputs
  outcome: supported
  summary: Actual original native validate/render0 and exact paired Markdown; 14 historical
    input occurrences match Git source. Current target nonstale. Batch26 historical
    global execution is not falsely relabeled fresh48 execution.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-original-validation
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-coverage
  area: completeness
  topic: Inventory coverage and unresolved boundaries
  outcome: supported
  summary: Seven reviewed example occurrences/seven distinct accessions and seven
    COVERED typed nodes. Seven canonical classes sufficiently scoped without adding
    TFIIK/Rad2/Tfb6 as mandatory members of every core context.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-native-core_tfiih_complex_portion_of_holo_tfiih_complex-verify
  - septin-native-core_tfiih_complex_portion_of_holo_tfiih_complex-causal
  - septin-protein-policy
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-history
  area: provenance
  topic: Current correction and immutable dated discussions
  outcome: supported
  summary: Preserve dated rationale,posed/retrieved dates and curation history. Update
    current grounding notes/prompts or append a dated clarification; current stale
    no-examples wording may be reconciled without erasing the earlier observation.
    No neighbor/group issue disposition inferred.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-curation-policy
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-adapter
  area: evidence
  topic: Actual whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger host coverage assessment; lack
    of expression-module claims is insufficient. Fresh complete official catalogue
    has no matching Saccharomyces/S288C dataset. Matched downstream gene/module requests
    do not apply after this bounded assessment; bacterial production hosts are not
    proxies. Historical00:49Z runner failure and direct current fallback are separate.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-verdict
  area: consistency
  topic: Independent current scientific outcome
  outcome: concern
  summary: Needs curation for one independently confirmed inherited minor exact-family
    grounding finding. Qualified positive identity/association/function/source assessments
    remain; no new record defect is established from optional fields, unavailable
    bodies or broad families.
  target_ids:
  - GO:0000438
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-identity
  area: identity
  topic: Structure identity and containing-complex boundary
  outcome: supported
  summary: Exact NEF3-context core identity; Rad2 partner is outside core and distinct
    from core Rad3/XPD.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-grounding
  area: grounding
  topic: Exact molecular identity versus broad family
  outcome: concern
  summary: All seven exact InterPro full-protein families are independently corroborated
    by reviewed example xrefs. IPR001945 mixed XPG/Rad2 prose does not override the
    independently matched RAD3/XPD name/member identity; broad generic domains are
    not substitutes.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-curation-policy
  - septin-rad3-family-members
  - septin-ipr-IPR001161
  - septin-ipr-IPR027079
  - septin-ipr-IPR004598
  - septin-retry-IPR012170
  - septin-ipr-IPR004600
  - septin-retry-IPR009400
  - septin-retry-IPR001945
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-proteins
  area: grounding
  topic: Native accession/status/primary-name and source-locus identity
  outcome: supported
  summary: Seven reviewed example occurrences/seven distinct accessions and seven
    COVERED typed nodes. Current reviewed exact yeast queries return the intended
    seven genes. Huh nuclear localization is distinct from core membership and functional
    necessity.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-protein-policy
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-protein-Q00578
  - septin-protein-P32776
  - septin-protein-Q02939
  - septin-protein-Q04673
  - septin-protein-Q12004
  - septin-protein-Q3E7C1
  - septin-protein-P06839
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-evidence
  area: evidence
  topic: Actual source access and experiment scopes
  outcome: supported
  summary: Murakami genuine body sections and canonical ontology/native annotations
    support composition; Takagi,Ranish,Huh current access is complete metadata/abstract,
    not unread full bodies. Prakash is a secondary-review abstract; failed/redirect
    routes are validation context only.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-literature-policy
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-formation
  area: evidence
  topic: Formation necessity versus functional dependence
  outcome: unknown
  summary: All seven formation-necessity fields remain UNKNOWN. Transcription/DNA-repair
    defects and purified subcomplex behavior do not establish universal obligatory
    formation sequence; Tfb6-dependent alternative purification states remain experimental
    context.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-graph
  area: graph
  topic: Complete descriptive graph and evidence mapping
  outcome: supported
  summary: FUNCTION/NONMECHANISTIC seven constituent links, NEF3 parthood and NER
    support remain coarse; Rad2 nuclease mechanism is not mislabeled as Rad3 activity.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-graph-policy
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-taxon
  area: scope
  topic: Canonical lineage and reference-versus-assay strains
  outcome: supported
  summary: Saccharomyces4932 and S288C559292 resolve; Murakami multiple yeast backgrounds
    and bacterial production hosts are not silently equated to reference examples.
    COMMON is qualitative, not population prevalence.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-tax4932
  - septin-tax559292
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-quantity
  area: quantity
  topic: Composition, time and size claims
  outcome: supported
  summary: Canonical seven-core versus three-TFIIK partition is distinguished from
    Tfb6-associated11-subunit purification and dissociated states; no universal fixed
    assembly stoichiometry or physical dimension is inferred.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-image
  area: evidence
  topic: Maintained image and attribution
  outcome: not_applicable
  summary: No maintained image on this target.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-schema
  area: schema
  topic: Original schema/render and frozen source inputs
  outcome: supported
  summary: Actual original native validate/render0 and exact paired Markdown; 14 historical
    input occurrences match Git source. Current target nonstale. Batch26 historical
    global execution is not falsely relabeled fresh48 execution.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-original-validation
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-coverage
  area: completeness
  topic: Inventory coverage and unresolved boundaries
  outcome: supported
  summary: Seven reviewed example occurrences/seven distinct accessions and seven
    COVERED typed nodes. Seven canonical classes sufficiently scoped without adding
    TFIIK/Rad2/Tfb6 as mandatory members of every core context.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-native-core_tfiih_complex_portion_of_nef3_complex-verify
  - septin-native-core_tfiih_complex_portion_of_nef3_complex-causal
  - septin-protein-policy
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-history
  area: provenance
  topic: Current correction and immutable dated discussions
  outcome: supported
  summary: Preserve dated rationale,posed/retrieved dates and curation history. Update
    current grounding notes/prompts or append a dated clarification; current stale
    no-examples wording may be reconciled without erasing the earlier observation.
    No neighbor/group issue disposition inferred.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-curation-policy
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-adapter
  area: evidence
  topic: Actual whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger host coverage assessment; lack
    of expression-module claims is insufficient. Fresh complete official catalogue
    has no matching Saccharomyces/S288C dataset. Matched downstream gene/module requests
    do not apply after this bounded assessment; bacterial production hosts are not
    proxies. Historical00:49Z runner failure and direct current fallback are separate.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-core_tfiih_complex_portion_of_nef3_complex-verdict
  area: consistency
  topic: Independent current scientific outcome
  outcome: concern
  summary: Needs curation for one independently confirmed inherited minor exact-family
    grounding finding. Qualified positive identity/association/function/source assessments
    remain; no new record defect is established from optional fields, unavailable
    bodies or broad families.
  target_ids:
  - GO:0000440
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-identity
  area: identity
  topic: Structure identity and containing-complex boundary
  outcome: supported
  summary: Local source-defined WDR1-Cullin4-DDB1 association is narrower than generic
    Cul4-RING and different named GOcomplexes. Catalytic completeness and obligatory
    RING identity remain unresolved, without inventing new subunits.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-grounding
  area: grounding
  topic: Exact molecular identity versus broad family
  outcome: concern
  summary: Q582R9/Tb927.3.4660 is a different native locus from Hu WDR1/Tb927.10.15080;
    source-locus zero query cannot authorize the substitution. Broad cullin or RSE1/DDB1/CPSF1
    families do not independently specify this assembly; generated family prose excluded.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-protein-Q582R9
  - septin-locus-Tb927.3.4660
  - septin-locus-Tb927.10.15080
  - septin-ipr-IPR045093
  - septin-ipr-IPR050358
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-proteins
  area: grounding
  topic: Native accession/status/primary-name and source-locus identity
  outcome: concern
  summary: Three unreviewed example occurrences/three distinct accessions and one
    COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not validate
    the disputed biological assignment.Native identities resolve all three unreviewed
    accessions, but only Cullin4/DDB1 source loci agree. These identifiers are ORF
    names rather than formal primary geneName fields. TREU927 is a reference background,
    not the29-13/Lister427 experimental strain.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-protein-policy
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-protein-Q57XW2
  - septin-protein-Q586I3
  - septin-protein-Q582R9
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-evidence
  area: evidence
  topic: Actual source access and experiment scopes
  outcome: supported
  summary: Hu genuine body/captions support source loci and bounded associations/perturbations.
    Yeast fragments, GST-plus-lysate and co-IP are not a fully purified direct interaction
    assay. Anti-ubiquitin species may be PLK or partners; phenocopy is not rescue
    or exclusive mediation. 2025 source table/discussion nomenclature conflict remains
    explicit.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-literature-policy
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-formation
  area: evidence
  topic: Formation necessity versus functional dependence
  outcome: unknown
  summary: All three formation-necessity fields remain UNKNOWN. WDR1 RNAi growth/duplication
    defects and protein turnover changes do not establish universal assembly necessity
    or complete catalytic composition.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-schema-policy
  - septin-curation-policy
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-graph
  area: graph
  topic: Complete descriptive graph and evidence mapping
  outcome: supported
  summary: FUNCTION/NONMECHANISTIC RNAi-output graph keeps24h chase/IP/phosphorylation,24/48h
    protein and48h organelle/attachment outcomes distinct. It does not claim direct
    covalent ubiquitination, rescue, ordered mediation or client PLK as an invariant
    component. Its WDR1 actor biological identity remains affected by the inherited
    example finding despite native COVERED.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-graph-policy
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-taxon
  area: scope
  topic: Canonical lineage and reference-versus-assay strains
  outcome: supported
  summary: Tbrucei5691 and TREU927185431 resolve. Procyclic29-13 RNAi/Lister427 tagging
    and2025Lister427 experiments are distinct from reference accessions; yeast/Ecoli
    assay production hosts are not canonical CRL4WDR1 examples. COMMON is qualitative.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-tax5691
  - septin-tax185431
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-quantity
  area: quantity
  topic: Composition, time and size claims
  outcome: supported
  summary: Three supported associated classes do not assert complete catalytic stoichiometry.
    Source24/48h endpoints and localization5µm scale are scoped; no whole-ligase size
    or purified ubiquitination rate is claimed.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-image
  area: evidence
  topic: Maintained image and attribution
  outcome: supported
  summary: Actual frozen Figure2A–F pixels inspected and exact external SHA/MD5 matched.
    Author attribution/CC-BY4.0 licensed source supported. Image depicts constructs/assays
    and WDR1 localization, not whole-ligase morphology. FpixelG1-versus-captionS inconsistency
    is retained as source limitation; maintained G1/S wording is not contradicted.
    Other record figures are not newly pixel-certified.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-image-local
  - septin-image-s3
  - septin-image-metadata
  - septin-PMC5241021-jats
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-schema
  area: schema
  topic: Original schema/render and frozen source inputs
  outcome: supported
  summary: Actual original native validate/render0 and exact paired Markdown; 15 historical
    input occurrences match Git source. Current target nonstale. Batch26 historical
    global execution is not falsely relabeled fresh48 execution.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-original-validation
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-coverage
  area: completeness
  topic: Inventory coverage and unresolved boundaries
  outcome: supported
  summary: Three unreviewed example occurrences/three distinct accessions and one
    COVERED WDR1 typed node; COVERED tests declared symbol coverage and does not validate
    the disputed biological assignment.Cullin4/DDB1 examples remain reference associations;
    current wrong-WDR1 assignment is actionable. RING, broader DCAFs and complete
    reaction machinery are explicitly unresolved, not automatically mandatory gaps.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-native-crl4wdr1_ubiquitin_ligase_complex-verify
  - septin-native-crl4wdr1_ubiquitin_ligase_complex-causal
  - septin-protein-policy
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-history
  area: provenance
  topic: Current correction and immutable dated discussions
  outcome: supported
  summary: Preserve dated rationale,posed/retrieved dates and curation history. Update
    current grounding notes/prompts or append a dated clarification; current stale
    no-examples wording may be reconciled without erasing the earlier observation.
    No neighbor/group issue disposition inferred.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-curation-policy
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-adapter
  area: evidence
  topic: Actual whole-record structured-source applicability
  outcome: supported
  summary: Positive protein/pathway assertions trigger host coverage assessment; lack
    of expression-module claims is insufficient. Fresh complete official catalogue
    has no matching Trypanosoma/TREU927/Lister427/29-13 dataset. Matched downstream
    gene/module requests do not apply after this bounded assessment; bacterial production
    hosts are not proxies. Historical00:49Z runner failure and direct current fallback
    are separate.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-review-policy
  - septin-catalogue
  - septin-adapter-runner-historical
- assessment_id: septin-crl4wdr1_ubiquitin_ligase_complex-verdict
  area: consistency
  topic: Independent current scientific outcome
  outcome: concern
  summary: Needs curation for one independently confirmed inherited major wrong receptor-example
    finding. Qualified positive identity/association/function/source assessments remain;
    no new record defect is established from optional fields, unavailable bodies or
    broad families.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 1 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0017119
  - GO:0000817
  - GO:0030126
  - GO:0030127
  - GO:1990098
  - GO:0000438
  - GO:0000440
  - GO:0033263
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  - GO:0031390
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
  issue_key: coma-mcm21-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the Mcm21 subunit with its exact ortholog family
  description: IPR018464 is a full family explicitly including yeast Mcm21 and is
    cross-referenced by Q06675. The maintained Mcm21 row remains REVIEWED_LABEL_ONLY.
    AME1 and Ctf19 domain candidates do not justify assigning whole-protein groundings
    to those rows.
  target_ids:
  - GO:0000817
  field_paths:
  - components#mcm21_subunit
  evidence_ids:
  - micro-record-0
  - micro-policy
  - micro-ipr-IPR018464
  - micro-up-Q06675
  - micro-ipr-IPR048743
  - micro-up-Q02732
  - micro-up-P53298
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: minor
  normalization_reason: Bounded curation correction supported by exact current authorities
    or condition-scoped primary assays; structural identity is retained.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051657Z-coma-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2895
- finding_id: micro-F2
  issue_key: coma-okp1-formation-evidence
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Capture the condition-scoped Okp1 assembly requirement
  description: 'The current Okp1 component lacks the specific physical-association
    evidence independently confirmed in Schmitzberger2017 Results sec11 and Methods31:
    native S.cerevisiae Okp1Δ325–337 loses Ctf19 co-IP and Ctf19/Mcm21 centromeric
    localization, while Ame1/outer-kinetochore localization persists. This supports
    the inherited minor condition-scoped formation/association curation gap, not a
    blanket inference from UNKNOWN, viability, or all-species necessity. Original
    DeWulf sec4 body evidence remains historical and was not freshly re-read after
    blocked routes.'
  target_ids:
  - GO:0000817
  field_paths:
  - components#okp1_subunit.essentiality
  - components#okp1_subunit.evidence
  evidence_ids:
  - micro-record-0
  - micro-schema
  - micro-policy
  - micro-schmitzberger2017-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: minor
  normalization_reason: Bounded curation correction supported by exact current authorities
    or condition-scoped primary assays; structural identity is retained.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051657Z-coma-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2896
- finding_id: micro-F3
  issue_key: ctf18-rfc-exact-family-subset
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Ctf18, Dcc1 and Ctf8 with exact families
  description: Current family entries IPR053016, IPR019128 and IPR018607 identify
    Ctf18, Dcc1 and Ctf8. Their rows remain REVIEWED_LABEL_ONLY. The shared IPR050238
    family and AAA/RFC domains are insufficient to distinguish the four small RFC
    paralogues. CTF18 family identity is separately checked from its unchecked generated
    description. Native P49956 currently lacks the IPR053016 xref; the exact Ctf18
    class is independently supported by the named family/signature and five reviewed
    ortholog members, not a fabricated P49956 mapping. No sequence alignment or universal
    RFC2–5 family absence is claimed.
  target_ids:
  - GO:0031390
  field_paths:
  - components#ctf18_subunit
  - components#dcc1_subunit
  - components#ctf8_subunit
  - discussions#resolve_ctf18_rfc_subunit_groundings
  evidence_ids:
  - micro-record-2
  - micro-policy
  - micro-ipr-IPR053016
  - micro-ipr-IPR019128
  - micro-ipr-IPR018607-retry
  - micro-ipr-IPR050238-retry
  - micro-family-CTF18
  - micro-up-P49956
  - micro-up-P25559
  - micro-up-P38877
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ctf18_rfc_like_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: minor
  normalization_reason: Bounded curation correction supported by exact current authorities
    or condition-scoped primary assays; structural identity is retained.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051703Z-ctf18-rfc-like-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2897
- finding_id: plaque-t0-F1
  issue_key: cog-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the eight named COG subunit classes
  description: Current exact whole-protein families are Cog1 IPR033370, Cog2 IPR009316,
    Cog3 IPR007265, Cog4 IPR048682, Cog5 IPR019465, Cog6 IPR010490, Cog7 IPR019335
    and Cog8 IPR007255. All remain REVIEWED_LABEL_ONLY. Historical deferred grounding
    is understandable, but the exact class authorities now resolve it. Generic component
    identity must not be confused with automatic sequence annotation of every yeast
    example.
  target_ids:
  - GO:0017119
  field_paths:
  - components
  - discussions#resolve_cog_subunit_family_groundings
  evidence_ids:
  - plaque-current-0
  - plaque-policy
  - plaque-ipr-IPR033370
  - plaque-ipr-IPR009316
  - plaque-ipr-retry-IPR007265
  - plaque-ipr-retry-IPR048682
  - plaque-ipr-retry-IPR019465
  - plaque-ipr-IPR010490
  - plaque-ipr-IPR019335
  - plaque-ipr-IPR007255
  - plaque-ipr-IPR006687
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-ipr-IPR032914
  - plaque-ipr-retry-IPR045111
  - plaque-ipr-IPR007810
  - plaque-ipr-retry-IPR001619
  - plaque-family-IPR033370
  - plaque-family-IPR009316
  - plaque-family-IPR019335
  - plaque-protein-P53079
  - plaque-protein-P53271
  - plaque-protein-P53195
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cog_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: minor
  normalization_reason: Bounded curation correction supported by exact current authorities
    or condition-scoped primary assays; structural identity is retained.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051656Z-cog-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2898
- finding_id: plaque-t2-F1
  issue_key: copi.ret1_reviewed_query_ambiguity
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the RET1 single-hit evidence note
  description: The selected P53622 coatomer alpha accession and primary symbol COP1
    are correct. Its current evidence note says it is the single reviewed entry for
    RET1 in S288C. The retained exact native query returns both P53622 (COP1, alias
    RET1) and P22276 (polymerase subunit RET1), so uniqueness cannot be used as the
    selection rationale.
  target_ids:
  - GO:0030126
  field_paths:
  - components[0].protein_examples[6].evidence[0].notes
  evidence_ids:
  - plaque-current-2
  - plaque-gene-RET1
  - plaque-protein-P53622
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copi_vesicle_coat.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: 'Minor: accession identity, coatomer membership and biology
    remain correct; only a current query-selection provenance statement is inaccurate.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051657Z-copi-vesicle-coat-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2899
- finding_id: plaque-t3-F1
  issue_key: copii.exact_sar1_family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the exact SAR1 family grounding
  description: The Sar1-family protein component remains REVIEWED_LABEL_ONLY, although
    native IPR006687 exactly represents the source-neutral SAR1-type family and is
    cross-referenced by the verified yeast P20606 example. This current mapping gap
    is distinct from the historical statement that an earlier pass did not curate
    it.
  target_ids:
  - GO:0030127
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-ipr-IPR006687
  - plaque-protein-P20606
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copii_vesicle_coat.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: 'Minor: protein identity, coat membership and biology are
    correct; an exact verified family resolves a bounded non-blocking label-only grounding
    gap.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051658Z-copii-vesicle-coat-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2900
- finding_id: plaque-t7-F1
  issue_key: corvet.exact_vps11_vps16_families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve two exact CORVET core-protein families
  description: Vps11/Pep5 and Vps16 remain REVIEWED_LABEL_ONLY even though native
    whole-protein families IPR016528 and IPR016534 match those declared classes and
    their reviewed yeast examples. Shared membership in HOPS does not invalidate their
    protein-family identity. The broader Vps3/Vps39, Vps8/Vps41, Sec1 and domain-level
    Vps18 candidates are explicitly excluded from this finding.
  target_ids:
  - GO:0033263
  field_paths:
  - components[2].grounding
  - components[2].grounding_status
  - components[2].grounding_notes
  - components[3].grounding
  - components[3].grounding_status
  - components[3].grounding_notes
  evidence_ids:
  - plaque-current-7
  - plaque-policy
  - plaque-ipr-IPR016528
  - plaque-ipr-IPR016534
  - plaque-protein-P12868
  - plaque-protein-Q03308
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/corvet_complex.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: 'Minor: subunit biology and the six-member complex remain
    correct; two exact available families resolve a bounded non-blocking grounding
    gap.'
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051701Z-corvet-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2901
- finding_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-F1
  issue_key: core_tfiih_complex_portion_of_holo_tfiih_complex-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use the verified exact TFIIH core subunit families
  description: 'All seven protein rows are REVIEWED_LABEL_ONLY because exact source-neutral
    mappings were not curated. Native InterPro now positively verifies the matching
    full-protein families, and the reviewed example xrefs corroborate each identity:
    Ssl2/XPB IPR001161, Tfb1/p62 IPR027079, Tfb2/p52 IPR004598, Ssl1/p44 IPR012170,
    Tfb4/p34 IPR004600, Tfb5/p8 IPR009400, Rad3/XPD IPR001945. This is an available
    exact-mapping gap, not a proposal to ground subunits to broad domains or to equate
    Rad3 with the separate Rad2 partner. Fresh exact native identities and source
    observations independently confirm this inherited finding. Preserve dated discussion
    history; no historical search dishonesty or unavailable-source refutation is alleged.'
  target_ids:
  - GO:0000438
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding
  - components[1].grounding_status
  - components[1].grounding_notes
  - components[2].grounding
  - components[2].grounding_status
  - components[2].grounding_notes
  - components[3].grounding
  - components[3].grounding_status
  - components[3].grounding_notes
  - components[4].grounding
  - components[4].grounding_status
  - components[4].grounding_notes
  - components[5].grounding
  - components[5].grounding_status
  - components[5].grounding_notes
  - components[6].grounding
  - components[6].grounding_status
  - components[6].grounding_notes
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-original-core_tfiih_complex_portion_of_holo_tfiih_complex
  - septin-go
  - septin-curation-policy
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-rad3-family-members
  - septin-ipr-IPR001161
  - septin-ipr-IPR027079
  - septin-ipr-IPR004598
  - septin-retry-IPR012170
  - septin-ipr-IPR004600
  - septin-retry-IPR009400
  - septin-retry-IPR001945
  - septin-protein-Q00578
  - septin-protein-P32776
  - septin-protein-Q02939
  - septin-protein-Q04673
  - septin-protein-Q12004
  - septin-protein-Q3E7C1
  - septin-protein-P06839
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    role: maintained scientific record
  rule_id: Exact component grounding / REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: The seven component identities, protein examples and complex
    boundary remain correct. The consequential gap is bounded to exact family grounding
    and its current status/rationale.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2892
- finding_id: septin-core_tfiih_complex_portion_of_nef3_complex-F1
  issue_key: core_tfiih_complex_portion_of_nef3_complex-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Use the verified exact TFIIH core subunit families
  description: 'All seven protein rows are REVIEWED_LABEL_ONLY because exact source-neutral
    mappings were not curated. Native InterPro now positively verifies the matching
    full-protein families, and the reviewed example xrefs corroborate each identity:
    Ssl2/XPB IPR001161, Tfb1/p62 IPR027079, Tfb2/p52 IPR004598, Ssl1/p44 IPR012170,
    Tfb4/p34 IPR004600, Tfb5/p8 IPR009400, Rad3/XPD IPR001945. This is an available
    exact-mapping gap, not a proposal to ground subunits to broad domains or to equate
    Rad3 with the separate Rad2 partner. Fresh exact native identities and source
    observations independently confirm this inherited finding. Preserve dated discussion
    history; no historical search dishonesty or unavailable-source refutation is alleged.'
  target_ids:
  - GO:0000440
  field_paths:
  - components[0].grounding
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding
  - components[1].grounding_status
  - components[1].grounding_notes
  - components[2].grounding
  - components[2].grounding_status
  - components[2].grounding_notes
  - components[3].grounding
  - components[3].grounding_status
  - components[3].grounding_notes
  - components[4].grounding
  - components[4].grounding_status
  - components[4].grounding_notes
  - components[5].grounding
  - components[5].grounding_status
  - components[5].grounding_notes
  - components[6].grounding
  - components[6].grounding_status
  - components[6].grounding_notes
  evidence_ids:
  - septin-record-core_tfiih_complex_portion_of_nef3_complex
  - septin-original-core_tfiih_complex_portion_of_nef3_complex
  - septin-go
  - septin-curation-policy
  - septin-murakami2012-pmc
  - septin-pmid-14500720
  - septin-pmid-15220919
  - septin-pmid-14562095
  - septin-pmid-10915862
  - septin-prakash2000-meta
  - septin-rad3-family-members
  - septin-ipr-IPR001161
  - septin-ipr-IPR027079
  - septin-ipr-IPR004598
  - septin-retry-IPR012170
  - septin-ipr-IPR004600
  - septin-retry-IPR009400
  - septin-retry-IPR001945
  - septin-protein-Q00578
  - septin-protein-P32776
  - septin-protein-Q02939
  - septin-protein-Q04673
  - septin-protein-Q12004
  - septin-protein-Q3E7C1
  - septin-protein-P06839
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    role: maintained scientific record
  rule_id: Exact component grounding / REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: The seven component identities, protein examples and complex
    boundary remain correct. The consequential gap is bounded to exact family grounding
    and its current status/rationale.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2893
- finding_id: septin-crl4wdr1_ubiquitin_ligase_complex-F1
  issue_key: crl4wdr1-wrong-receptor-example
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Remove or replace the unrelated WDR1 protein example
  description: The WDR1 protein_examples row assigns Q582R9/Tb927.3.4660 to WDR1.
    Hu2017 sec004 explicitly defines WDR1 as Tb927.10.15080. The current native Q582R9
    entry and exact-locus query identify the different locus and supply no WDR1 synonym.
    A zero-result query for the source locus cannot justify selecting another WD-repeat
    protein. The false correspondence can propagate incorrect receptor identity despite
    the native identifier validator passing. Fresh exact native identities and source
    observations independently confirm this inherited finding. Preserve dated discussion
    history; no historical search dishonesty or unavailable-source refutation is alleged.
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  field_paths:
  - components#wdr1.protein_examples
  - discussions#component_families_and_examples
  evidence_ids:
  - septin-record-crl4wdr1_ubiquitin_ligase_complex
  - septin-original-crl4wdr1_ubiquitin_ligase_complex
  - septin-go
  - septin-curation-policy
  - septin-PMC5241021-jats
  - septin-PMC12816148-jats
  - septin-protein-Q582R9
  - septin-locus-Tb927.3.4660
  - septin-locus-Tb927.10.15080
  - septin-protein-Q57XW2
  - septin-protein-Q586I3
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: major
  normalization_reason: A wrong protein example identifies a different locus and can
    propagate incorrect biological identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2894
actions:
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0000817
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add the exact Mcm21/CENP-O
    family mapping IPR018464 and preserve separate current uncertainty for the other
    three whole-protein families.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Preserve dated curation history, discussions.rationale and posed_date; update
    current notes/prompt only as supported, appending rather than replacing provenance.
  - This PR edits no record. Retain host, method and access-tier limits; identifier/family
    identity, localization, membership, assembly and function are distinct claims.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0000817
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, add the exact native Okp1Δ325–337/Ctf19
    co-IP and Ctf19-Mcm21 localization context from Schmitzberger2017, retaining observed
    Ame1/outer-kinetochore persistence and culture conditions. Qualify formation/association
    interpretation; do not force universal ESSENTIAL, equate it with viability or
    mandate new experiments. Reinspect DeWulf full body before newly asserting its
    allele/temperature details.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Preserve dated curation history, discussions.rationale and posed_date; update
    current notes/prompt only as supported, appending rather than replacing provenance.
  - This PR edits no record. Retain host, method and access-tier limits; identifier/family
    identity, localization, membership, assembly and function are distinct claims.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0031390
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ctf18_rfc_like_complex.yaml
    role: maintained scientific record
  description: In separately authorized record curation, curate the three exact class
    mappings and narrow the open family TODO to remaining unresolved paralogue identities.
    Retain the correct examples and avoid treating family annotation or generated
    prose as evidence of biological membership.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Preserve dated curation history, discussions.rationale and posed_date; update
    current notes/prompt only as supported, appending rather than replacing provenance.
  - This PR edits no record. Retain host, method and access-tier limits; identifier/family
    identity, localization, membership, assembly and function are distinct claims.
  - Distinguish exact Ctf18 class identity from absent current P49956 xref; exclude
    unchecked generated description from biological support and do not force shared
    clamp-loader domains onto RFC2–5.
- action_id: plaque-t0-A1
  finding_ids:
  - plaque-t0-F1
  target_ids:
  - GO:0017119
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cog_complex.yaml
    role: maintained scientific record
  description: Curate the eight exact class mappings after confirming the generic
    ortholog-class scope; retain the correct yeast examples and separately sourced
    memberships. Reconcile the family TODO and document that Cog1/2/7 class grounding
    is not a new sequence annotation of the reference examples.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Preserve dated append-only rationale/history; append current evidence and update
    active notes/status as appropriate. Record curation remains outside this review-only
    PR.
- action_id: plaque-t2-A1
  finding_ids:
  - plaque-t2-F1
  target_ids:
  - GO:0030126
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copi_vesicle_coat.yaml
    role: maintained scientific record
  description: Keep P53622 and COP1 with the RET1 alias; replace the uniqueness claim
    with explicit disambiguation against polymerase P22276. Preserve dated retrieval
    history.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated append-only rationale/history; append current evidence and update
    active notes/status as appropriate. Record curation remains outside this review-only
    PR.
- action_id: plaque-t3-A1
  finding_ids:
  - plaque-t3-F1
  target_ids:
  - GO:0030127
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copii_vesicle_coat.yaml
    role: maintained scientific record
  description: Ground the Sar1 component to InterPro:IPR006687 and synchronize current
    grounding status/notes and any linked node consistently. Preserve its component
    ID, UNKNOWN necessity, and the distinct unresolved heteromeric subcomplex boundaries.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated append-only rationale/history; append current evidence and update
    active notes/status as appropriate. Record curation remains outside this review-only
    PR.
- action_id: plaque-t7-A1
  finding_ids:
  - plaque-t7-F1
  target_ids:
  - GO:0033263
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/corvet_complex.yaml
    role: maintained scientific record
  description: Map Vps11/Pep5 to InterPro:IPR016528 and Vps16 to InterPro:IPR016534;
    synchronize current label-only notes/status and linked nodes while preserving
    IDs, UNKNOWN necessity and the bounded unresolved classes.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
  - Preserve dated append-only rationale/history; append current evidence and update
    active notes/status as appropriate. Record curation remains outside this review-only
    PR.
- action_id: septin-core_tfiih_complex_portion_of_holo_tfiih_complex-A1
  finding_ids:
  - septin-core_tfiih_complex_portion_of_holo_tfiih_complex-F1
  target_ids:
  - GO:0000438
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml
    role: maintained scientific record
  description: Map the seven existing subunit rows to their verified exact InterPro
    families; update current grounding status/notes and TODO while preserving component
    IDs, genes, protein examples, UNKNOWN essentiality and context-specific containing-complex
    boundaries. Record curation stays outside this review-only PR. Preserve dated
    rationale/history; update current notes/prompts or append clarification.
  acceptance_checks:
  - Confirm each family type, exact subunit scope and native example xref; distinguish
    RAD3/XPD from the unrelated XPG/Rad2 background prose.
  - Do not replace full-family mappings with generic helicase, zinc-finger or domain
    terms.
  - Retain TFIIK or Rad2 as partners outside this seven-subunit core portion.
  - Pass applicable schema, strict, identifier, native protein and graph checks.
  - Use separately authorized guarded record curation with required append-only record/repository
    history; preserve source-strain, assay and UNKNOWN formation limits.
- action_id: septin-core_tfiih_complex_portion_of_nef3_complex-A1
  finding_ids:
  - septin-core_tfiih_complex_portion_of_nef3_complex-F1
  target_ids:
  - GO:0000440
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml
    role: maintained scientific record
  description: Map the seven existing subunit rows to their verified exact InterPro
    families; update current grounding status/notes and TODO while preserving component
    IDs, genes, protein examples, UNKNOWN essentiality and context-specific containing-complex
    boundaries. Record curation stays outside this review-only PR. Preserve dated
    rationale/history; update current notes/prompts or append clarification.
  acceptance_checks:
  - Confirm each family type, exact subunit scope and native example xref; distinguish
    RAD3/XPD from the unrelated XPG/Rad2 background prose.
  - Do not replace full-family mappings with generic helicase, zinc-finger or domain
    terms.
  - Retain TFIIK or Rad2 as partners outside this seven-subunit core portion.
  - Pass applicable schema, strict, identifier, native protein and graph checks.
  - Use separately authorized guarded record curation with required append-only record/repository
    history; preserve source-strain, assay and UNKNOWN formation limits.
- action_id: septin-crl4wdr1_ubiquitin_ligase_complex-A1
  finding_ids:
  - septin-crl4wdr1_ubiquitin_ligase_complex-F1
  target_ids:
  - cellstructuremech:crl4wdr1_ubiquitin_ligase_complex
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/crl4wdr1_ubiquitin_ligase_complex.yaml
    role: maintained scientific record
  description: Remove Q582R9 from the WDR1 example unless independent exact-locus/sequence
    evidence establishes an identity merger; otherwise replace only with a verified
    source-locus accession. Preserve Q57XW2 and Q586I3 as reference-strain examples,
    accurately call their identifiers ORF names, and reconcile stale no-examples discussion
    text. Do not guess a replacement or change the supported source-defined complex.
    Record curation stays outside this review-only PR. Preserve dated rationale/history;
    update current notes/prompts or append clarification.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
  - Use separately authorized guarded record curation with required append-only record/repository
    history; preserve source-strain, assay and UNKNOWN formation limits.
limitations:
- 'COMA, core-primosome and Ctf18-RFC independent review: Only COMA, core primosome
  and Ctf18 RFC-like current whole records are independently judged. Other frozen
  cohort members/image are not read or disposed here; no neighboring/category/group
  issue is terminally resolved.'
- 'COMA, core-primosome and Ctf18-RFC independent review: Schmitzberger2017 genuine
  JATS read at the exact listed sections and Figures1/2/7/8 text captions only. K.lactis
  recombinant work and native S.cerevisiae co-IP/localization are distinct. EV6 strain
  table, raw images/blots, supplemental data and physical figure pixels were not inspected.
  S288C-derived methods permit explicit exceptions; exact mutant genotype is not invented.'
- 'COMA, core-primosome and Ctf18-RFC independent review: Current DeWulf2003 terminal
  body routes returned challenge/404/no-result/403. Fresh complete native abstract
  was read; a transient web reader supplied only abstract/intro/first-results context,
  not sec4. Original Oct22 full-body claim remains immutable historical evidence,
  not a newly certified body read. Current Okp1 finding independently rests on Schmitzberger
  body.'
- 'COMA, core-primosome and Ctf18-RFC independent review: Biggins2013, Kim-MacNeill2003
  and Kaguni2011 metadata are secondary literature; Kaguni body is read at S1,S5,S6,S9–12
  as specified. No cited primary experiment, other body sections or figures is certified
  by that review. Ortiz1999, Huh2003 and Mayer2001 remain complete-primary-abstract/native-authority
  tiers, not full-body experiments.'
- 'COMA, core-primosome and Ctf18-RFC independent review: InterPro type/name/signature/class
  identity is separate from generated biological prose. Unchecked descriptions for
  IPR053016/IPR050219/IPR050238 are excluded from biological support. P49956 lacks
  current IPR053016 xref; five reviewed ortholog hits support class identity, not
  a fabricated reference-accession link or new alignment. No exhaustive absence of
  other RFC2–5 families is asserted.'
- 'COMA, core-primosome and Ctf18-RFC independent review: Current exact-gene searches
  are bounded reviewed-reference-taxon queries of size100; no historical uniqueness
  claim is inferred from fresh results. Taxon-specific protein examples and generic
  component classes remain distinct.'
- 'COMA, core-primosome and Ctf18-RFC independent review: Official catalogue lacks
  a natural yeast match in its complete returned20 organism rows. E.coli precise1k
  contains five strains and201 modules; b3066 crosses module10 threshold while b4052
  has no above-threshold hit. Alias noncoverage, threshold nonmembership and catalogue
  absence are not biological absence. Generated module narrative and activity interpretations
  are not experimental evidence; expression is not assembly/localization/necessity
  or causal regulation.'
- 'COMA, core-primosome and Ctf18-RFC independent review: Historical unavailable runner
  is dated2026-11-03T00:49:00.848907–00:49:00.863225Z, not a fresh execution. Root
  native protein receipts cover current implemented identifiers and graph-example
  diagnostics only. Root owns full QC, final saved-head CI and queue; no pending stage
  is certified.'
- 'COMA, core-primosome and Ctf18-RFC independent review: No maintained record, original
  review pair, Git state or GitHub object is edited by this review. Findings are proposed
  bounded record curation, while stale/applicability bundle defects require a linked
  immutable successor.'
- 'COG, COPI/COPII coats and CORVET independent review: Fresh current PR source snapshots
  are used with actual request completion timestamps; the shared same-PR catalogue
  retains its original retrieval timestamp and was independently reread. Selected
  Yu/Ha/Ishii/Zanetti body sections and Matsuoka author-PDF text were actually inspected;
  other papers remain complete indexed-primary-abstract/native-annotation tiers.'
- 'COG, COPI/COPII coats and CORVET independent review: No maintained images occur
  in these four records. No external figure pixels, movies, supplementary datasets,
  raw-data reanalysis or image licence/reproduction permission is certified. Text
  captions/PDF extraction are not pixel inspection.'
- 'COG, COPI/COPII coats and CORVET independent review: Peplowska full body unavailable
  (DOI response is bibliographic Crossref JSON; publisher403); Sandmann PMC challenge/BioC429
  yielded no body. Exact strain/Methods and detailed mechanistic directness beyond
  inspected abstracts remain limited. Initial five InterPro429s had separately dated
  successful native retries.'
- 'COG, COPI/COPII coats and CORVET independent review: Recombinant production hosts
  are not biological dataset proxies. Ha COG yeast-sequence complexes were produced
  in E.coli; Yu combines mammalian coatomer and yeast/human Arf components; Matsuoka
  synthetic/native membrane stoichiometry differs. Neither model geometry nor cell
  viability automatically establishes universal formation necessity.'
- 'COG, COPI/COPII coats and CORVET independent review: Current generic Cog1/2/7 family
  mappings do not certify sequence coverage of the maintained S288C examples, whose
  native entries lack those whole-family IDs. Broader/domain candidates for other
  CORVET proteins are not promoted to exact groundings.'
- 'COG, COPI/COPII coats and CORVET independent review: No fresh structured-adapter
  runner execution claimed. The retained00:49Z failure remains historical; current
  source fallback inspected the complete official catalogue and found no biological
  yeast/Kluyveromyces/mammalian match. No unrelated host/module proxy or biological
  absence inferred.'
- 'COG, COPI/COPII coats and CORVET independent review: Four original pairs/56 historical
  input occurrences and48 current source/worktree hashes verified. All four assigned
  targets unchanged. Root-owned full QC, post-save, CI and queue are not precertified
  by this report.'
- 'COG, COPI/COPII coats and CORVET independent review: Four inherited minor findings
  retained with exact lineage and proposed guarded record curation; no new scientific
  finding established or neighboring/group/category issue terminally resolved.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: All three current targets
  are unchanged from original frozen records. Three inherited findings remain confirmed:
  two minor TFIIH exact-family mappings and one major CRL4WDR1 wrong-locus example.
  No new record finding or unrelated terminal issue resolution.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: 17 protein example occurrences
  are10 distinct accessions:14 reviewed yeast occurrences share7 accessions;3 unreviewed
  parasite occurrences are3 accessions. All15 typed nodes are native COVERED, which
  does not biologically validate Q582R9 as source WDR1. Native command success is
  not scientific membership or formation proof.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: Murakami genuine body
  read only at Abstract/Table1,Resultssec2–5,Discussionsec6,Methodssec8–10/12–13 including
  cited captions. Takagi/Ranish/Huh current inspection is complete native metadata/abstract
  only. Prakash is secondary-review abstract only; current DOIredirect and publisher403
  are not body access.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: Hu2017 genuine JATS front/Results003–008/Discussion009/Methods011–017
  and embedded Figures1–8 captions were read. Only frozenFigure2A–F pixels were inspected.
  No other figure/supplement pixels, raw proteomics, sequence alignment or whole-study
  replication. GST-plus-lysate/co-IP, incomplete fragment interactions, unresolved
  ubiquitinated species and phenocopy-versus-rescue distinctions remain explicit.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: 2025 cullin source was
  read at front/abstract/Table1/Sec5/6/10/12 only; table TbCul-D locus3.1290 versus
  Discussion oldPLK→TbCul-E attribution conflict is preserved. New Rbx/DCAF coisolates
  are not automatically members of the earlier WDR1-defined assembly.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: Frozen Figure2 SHA matches
  current PMC asset and publisherMD5. JATSfront licensesCC-BY4.0 and authorsHu/Zhou/Han/Li.
  PixelF saysG1 while source caption saysS; maintainedG1/S scope is not contradicted.
  No whole-ligase dimension measured or other historical pixel inspection recertified.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: IPR001945 mixed XPG/Rad2
  background is not used as RAD3 identity evidence; native family name, reviewed P06839
  xref and all8 returned reviewed family members establish the bounded mapping. IPR050358
  top-level generated-prose flags are true, so generated functional prose is excluded;
  broad Cullin/DDB1-related families do not force exact assembly mappings.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: Current complete official
  catalogue has no matching Saccharomyces orTrypanosoma dataset. No unrelated bacterial
  proxy and no biological-absence inference. Historical runner failure remains actualNov3
  00:49Z, with no fresh invocation. Original dated catalogue statements remain historical
  observations.'
- 'Two TFIIH core contexts and CRL4WDR1 independent review: All43 original input occurrences
  and three deterministic original pairs verified. Original batch26 global execution
  scopes retained. Two NEF3 failed-access rows were typed database but alreadycontext_only/explicitlyfailed;
  correction is kind-only, not an accusation of fabricated body access. Parent global/postsave/finalCI/queue/merge/deletion
  are outside this source-review attestation.'
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
- All ten original YAML/Markdown pairs remain byte-identical. COMA now adds four component_ref
  nodes, four source-cited constituent edges and history. The current added assertions
  are substantively reassessed against actual sources, not merely assigned a new frozen
  hash.
- All inherited findings retain exact predecessor identities. Current authority results
  are dated observations and do not reconstruct historical query results. Formation
  evidence is limited to the actually assayed conditions and physical-association
  outcomes.
- All ten complete records have positive molecular or pathway narratives requiring
  source applicability assessment. Seven formal exclusions and three prose exclusions
  are replaced by actual coverage assessments with precise organism and strain limits.
- The original NEF3 Prakash DOI and publisher retrieval failures already have context_only
  support and explicitly disclose failure. The correction distinguishes their evidence
  kind as validation receipts; it does not allege that the original claimed successful
  paper-body access. Actual secondary-review metadata and abstract evidence remain
  separately bounded.
- 'The actual native protein inventory has 58 represented examples and 50 typed nodes:
  47 COVERED and three UNANCHORED_WITH_UNIPROT. These deterministic classifications
  do not prove biological protein-example correspondence or establish automatic record
  defects.'
- The WDR1 wrong-locus finding remains major despite successful identifier checks
  and native node coverage. It is separately tracked for record curation. The frozen
  CRL4WDR1 image is an explicit inspected input; source figure scope remains distinct
  from molecular-identity evidence.
- Scientific curation remains separate from this review PR. Exact family identities,
  complex membership, primary experimental scope and current query uniqueness are
  assessed without forcing universal formation claims or whole-protein mappings from
  broad domains.
- 'Local full QC and focused gates passed before saving. Final trusted-base post-save
  review-check, exact-head independent acceptance, final-head CI and merge-group CI
  are subsequent external gates. Existing issue #2514 tracks native bulk-PMID transport/reporting;
  bounded supplemental requests verified all 909 affected PMIDs without changing the
  original report or cache.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051656Z-cog-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051657Z-coma-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051657Z-copi-vesicle-coat-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051658Z-copii-vesicle-coat-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051659Z-core-primosome-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051700Z-core-tfiih-complex-portion-of-holo-tfiih-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051700Z-core-tfiih-complex-portion-of-nef3-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051701Z-corvet-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051702Z-crl4wdr1-ubiquitin-ligase-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261022T051703Z-ctf18-rfc-like-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2385
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2889
- https://github.com/CultureBotAI/CellStructureMech/issues/2890
- https://github.com/CultureBotAI/CellStructureMech/issues/2891
- https://github.com/CultureBotAI/CellStructureMech/issues/2892
- https://github.com/CultureBotAI/CellStructureMech/issues/2893
- https://github.com/CultureBotAI/CellStructureMech/issues/2894
- https://github.com/CultureBotAI/CellStructureMech/issues/2895
- https://github.com/CultureBotAI/CellStructureMech/issues/2896
- https://github.com/CultureBotAI/CellStructureMech/issues/2897
- https://github.com/CultureBotAI/CellStructureMech/issues/2898
- https://github.com/CultureBotAI/CellStructureMech/issues/2899
- https://github.com/CultureBotAI/CellStructureMech/issues/2900
- https://github.com/CultureBotAI/CellStructureMech/issues/2901
```
