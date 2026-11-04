# PR 2353: current-input review of ten records and adversarial follow-up

- Review: 20261103T062235Z-pr2353-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T06:11:57.988310Z
- Finished UTC: 2026-11-03T06:22:35Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten cytoskeleton records in PR2353. Five stale reviews are substantively refreshed: three gamma-tubulin complexes with changed component types, protein examples and budding-yeast context, plus two meiotic tether/LINC records with corrected Bqt1-Bqt2 component types. Prior record corrections remain scoped historical context. All ten targets retain scientific curation findings. The successor corrects structured-source applicability in all ten original bundles without editing scientific records. Shared findings for the broad and small gamma-tubulin complexes are consolidated with both exact predecessor occurrences and target-specific assessments.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 98550c547790b78459491529fe7d5ef3c691a25f. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 4a45d54e374a9f1c60fe2b191cd824b4a6cf3441.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 05425cc7089baf8133399baaf1ec24c00c661de3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0061645 | data/structures/cytoskeleton/endocytic_patch.yaml | maintained | endocytic patch |
| GO:0000930 | data/structures/cytoskeleton/gamma_tubulin_complex.yaml | maintained | gamma-tubulin complex |
| GO:0000931 | data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml | maintained | gamma-tubulin ring complex |
| GO:0008275 | data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml | maintained | gamma-tubulin small complex |
| GO:0034993 | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml | maintained | meiotic nuclear membrane microtubule tethering complex |
| GO:1990612 | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml | maintained | Sad1-Kms1 LINC complex |
| GO:0032156 | data/structures/cytoskeleton/septin_cytoskeleton.yaml | maintained | septin cytoskeleton |
| GO:0005819 | data/structures/cytoskeleton/spindle.yaml | maintained | spindle |
| GO:0051233 | data/structures/cytoskeleton/spindle_midzone.yaml | maintained | spindle midzone |
| GO:0000922 | data/structures/cytoskeleton/spindle_pole.yaml | maintained | spindle pole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0061645 | passed | True | GO:0061645 | Documented focused command passed. |
| validate-strict GO:0061645 | passed | True | GO:0061645 | Documented focused command passed. |
| validate GO:0000930 | passed | True | GO:0000930 | Documented focused command passed. |
| validate-strict GO:0000930 | passed | True | GO:0000930 | Documented focused command passed. |
| validate GO:0000931 | passed | True | GO:0000931 | Documented focused command passed. |
| validate-strict GO:0000931 | passed | True | GO:0000931 | Documented focused command passed. |
| validate GO:0008275 | passed | True | GO:0008275 | Documented focused command passed. |
| validate-strict GO:0008275 | passed | True | GO:0008275 | Documented focused command passed. |
| validate GO:0034993 | passed | True | GO:0034993 | Documented focused command passed. |
| validate-strict GO:0034993 | passed | True | GO:0034993 | Documented focused command passed. |
| validate GO:1990612 | passed | True | GO:1990612 | Documented focused command passed. |
| validate-strict GO:1990612 | passed | True | GO:1990612 | Documented focused command passed. |
| validate GO:0032156 | passed | True | GO:0032156 | Documented focused command passed. |
| validate-strict GO:0032156 | passed | True | GO:0032156 | Documented focused command passed. |
| validate GO:0005819 | passed | True | GO:0005819 | Documented focused command passed. |
| validate-strict GO:0005819 | passed | True | GO:0005819 | Documented focused command passed. |
| validate GO:0051233 | passed | True | GO:0051233 | Documented focused command passed. |
| validate-strict GO:0051233 | passed | True | GO:0051233 | Documented focused command passed. |
| validate GO:0000922 | passed | True | GO:0000922 | Documented focused command passed. |
| validate-strict GO:0000922 | passed | True | GO:0000922 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | not_applicable | False | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | The complete official catalogue was inspected with actual access timestamps and bounded organism/dataset scope. Its returned20organisms/28datasets contain no matching eukaryotic dataset for these fungal/algal contexts. Downstream matched gene/module queries are therefore not applicable after coverage assessment. Catalogue absence is not biological absence, and unrelated bacterial datasets are not substituted. Historical native-runner unavailability remains separately disclosed, with no fresh runner invocation or success claimed. All ten original reviews require this correction: seven omitted applicability and three used unsupported lack-expression rationales. |
| Independent claim-level source review | passed | True | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native endocytic patch UniProt verify check | passed | True | GO:0061645 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native endocytic patch UniProt causal check | passed | True | GO:0061645 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native gamma-tubulin complex UniProt verify check | passed | True | GO:0000930 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native gamma-tubulin complex UniProt causal check | passed | True | GO:0000930 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native gamma-tubulin ring complex UniProt verify check | passed | True | GO:0000931 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native gamma-tubulin ring complex UniProt causal check | passed | True | GO:0000931 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native gamma-tubulin small complex UniProt verify check | passed | True | GO:0008275 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native gamma-tubulin small complex UniProt causal check | passed | True | GO:0008275 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native meiotic nuclear membrane microtubule tethering complex UniProt verify check | passed | True | GO:0034993 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native meiotic nuclear membrane microtubule tethering complex UniProt causal check | passed | True | GO:0034993 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native Sad1-Kms1 LINC complex UniProt verify check | passed | True | GO:1990612 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native Sad1-Kms1 LINC complex UniProt causal check | passed | True | GO:1990612 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native septin cytoskeleton UniProt verify check | passed | True | GO:0032156 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native septin cytoskeleton UniProt causal check | passed | True | GO:0032156 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native spindle UniProt verify check | passed | True | GO:0005819 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native spindle UniProt causal check | passed | True | GO:0005819 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native spindle midzone UniProt verify check | passed | True | GO:0051233 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native spindle midzone UniProt causal check | passed | True | GO:0051233 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native spindle pole UniProt verify check | passed | True | GO:0000922 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |
| Native spindle pole UniProt causal check | passed | True | GO:0000922 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence; spindle-pole empty inventory and zero molecular graph nodes do not validate its prose mechanisms. Deterministic identifier coverage does not resolve scientific findings or assembly necessity. |

## Scientific And Domain Assessments

### Broad patch identity and yeast actin-rich realization

identity: supported. Targets: GO:0061645.

GO0061645 and cell-cortex parthood are supported. Actin-rich yeast patches are a scoped realization, not obligatory composition of every broad endocytic patch. No new identity or mandatory optional-component finding.

### Eight protein examples and family/complex boundaries

grounding: supported. Targets: GO:0061645.

All eight reviewed S288C accession/gene/name/taxon pairs and exact uniqueness queries match. The seven-member Arp2/3 complex is a legitimate complex cohort. IPR004000 includes Arps and is broader than conventional actin; only this candidate was checked, with no exhaustive family-absence assertion. UNKNOWN essentiality is appropriate uncertainty.

### GO-only attribution of appended fungal mechanism

provenance: concern. Targets: GO:0061645.

The added coat/adaptor/NPF/scission/turgor account exceeds GO-only definition_source. Primary yeast studies support portions with stage and osmotic qualifications; no audited source establishes the complete listed mechanism throughout fungi. Retain original minor F1.

### Early recruitment, actin assembly and inward motion

evidence: supported. Targets: GO:0061645.

Fresh primary morphology and regulator/turgor experiments support actin-rich yeast patch function within preparation/stage limits. Kaksonen remains abstract-only. The early endocytic patch can organize later actin assembly; neither circularity nor impossibility follows from the broad node names.

### Membership/output versus mechanism

graph: concern. Targets: GO:0061645.

Six nodes/five edges provide three parthood and two broad output relations. The GO-only assembly edge omits stage and recruited machinery; MECHANISTIC overstates represented explanation. Original minor F2 remains, separately from whether early sites can organize actin.

### Exact envelope complex and native hierarchy

identity: supported. Targets: GO:0034993.

GO0034993, its three supplied synonyms, GO0106094 parent and GO0034992 parthood are native. It denotes a membrane tether, distinct from HAA/rMTOC.

### Substantive stale Bqt1/Bqt2 grouping reassessment

representation: supported. Targets: GO:0034993.

Current PROTEIN_COMPLEX correctly represents two distinct interacting proteins forming the Rap1–Sad1 connector, rather than one family/paralog class. Abstract bridge evidence and later interaction/degradation data support the grouped identity. ASSOCIATED_MACHINERY remains explicit. #2420 is a prior record correction; no terminal disposition of the seven-target category finding.

### Four reference examples and SUN family

grounding: supported. Targets: GO:0034993.

Fresh Q09825/P87245/Q92358/Q9US52 identity, reviewed status, gene symbols and taxon284812 match. IPR045119 supports the SUN-family grounding. 972h- examples are expressly reference sequences, not claims about exact engineered experimental stock; native verify and three-node graph coverage checks pass.

### Assembly necessity and motor-interface limits

evidence: unknown. Targets: GO:0034993.

Function, localization, viability and Bqt-dependent bouquet attachment are distinct from whether each core LINC assembly forms. Complete core-subunit removal/reconstitution necessity is not established for ESSENTIAL or the connector CONDITIONAL value. Funaya introductory topology is prior-study context, and its direct Hrs1 interaction assays do not alone establish direct dynein-dynactin recruitment. No opposite essentiality or absent-Kms2 finding is invented.

### Exact envelope complex and native hierarchy

identity: supported. Targets: GO:1990612.

GO1990612 exactly denotes Sad1–Kms1; native GO retains its GO0034993 is_a parent. Swartz2014 supports the DSB-repair opening with S/G2/repair-pathway bounds; meiotic roles are additional contexts.

### Substantive stale Bqt1/Bqt2 grouping reassessment

representation: supported. Targets: GO:1990612.

Current PROTEIN_COMPLEX correctly represents two distinct interacting proteins forming the Rap1–Sad1 connector, rather than one family/paralog class. Abstract bridge evidence and later interaction/degradation data support the grouped identity. ASSOCIATED_MACHINERY remains explicit. #2420 is a prior record correction; no terminal disposition of the seven-target category finding.

### Four reference examples and SUN family

grounding: supported. Targets: GO:1990612.

Fresh Q09825/P87245/Q92358/Q9US52 identity, reviewed status, gene symbols and taxon284812 match. IPR045119 supports the SUN-family grounding. 972h- examples are expressly reference sequences, not claims about exact engineered experimental stock; native verify and three-node graph coverage checks pass.

### Assembly necessity and motor-interface limits

evidence: unknown. Targets: GO:1990612.

Function, localization, viability and Bqt-dependent bouquet attachment are distinct from whether each core LINC assembly forms. Complete core-subunit removal/reconstitution necessity is not established for ESSENTIAL or the connector CONDITIONAL value. Funaya introductory topology is prior-study context, and its direct Hrs1 interaction assays do not alone establish direct dynein-dynactin recruitment. No opposite essentiality or absent-Kms2 finding is invented.

### Membrane tether distinct from radial array

scope: concern. Targets: GO:0034993.

The maintained horsetail function and corresponding process/edge say the membrane complex provides the radial array and call GO0032117 its exact definition. GO0032117 is HAA, and Funaya distinguishes Hrs1/rMTOC array organization from membrane bridge. Original major F1 remains; a tether contribution to movement can be retained with exact evidence.

### Fungi COMMON and dynein generalization

scope: concern. Targets: GO:0034993.

Chikashige abstract supports S. pombe Bqt1/Bqt2 connector, not broad fungal prevalence of this microtubule tether or uniform dynein coupling. Lee/Fan demonstrate distinct budding-yeast actin-associated machinery. Original major F2 remains without asserting absence of related tethers in other fungi.

### Represented force transmission

graph: concern. Targets: GO:0034993.

Six nodes/five edges are constituent/compartment relations and whole-structure output. Correcting the copied HAA function does not itself supply a mechanistic tether/force transition. Original minor F3 remains.

### Molecular subject of Fan assays and broad fungal distribution

scope: concern. Targets: GO:1990612.

Fan directly studies Mps2–Mps3–Csm4 in budding yeast; the graph still assigns Fan-only telomere and conversion outputs to Sad1–Kms1. A budding-yeast qualifier inside prose does not change the edge subject. Fungi COMMON/dynein wording also exceeds the fission-yeast source. Original major F1 remains; this does not deny S. pombe telomere/recombination roles.

### Fission-yeast attachment and DSB roles

evidence: supported. Targets: GO:1990612.

Moiseeva supports conditional telomere-SPB attachment/spindle effects with successful divisions retained in a subset, and Jimenez preserves partial mitotic recruitment without complete bouquet. Swartz independently supports DSB repair context. These bounded observations can survive correction of cross-species attribution.

### Meiotic recruitment versus MMS-associated foci

scope: unknown. Targets: GO:1990612.

Yoshida sees Kms2 at meiotic telocentrosomes; Swartz does not detect increased Kms2 in MMS-associated foci but leaves redundancy/low-copy roles open. The definition parenthetical does not establish fixed three-subunit stoichiometry. No universal absence or replacement of the named complex is concluded.

### Functional summary versus causal chain

graph: concern. Targets: GO:1990612.

Seven nodes/six edges give two parthood, one association and three whole-complex outputs; there is no represented bridge/motor/force transition. FUNCTION is reasonable but MECHANISTIC overstates detail. Original minor F2 remains separate from cross-species assignment.

### Molecular triggers and native catalogue applicability

scope: supported. Targets: GO:0061645, GO:0034993, GO:1990612.

ACT1/Arp genes and Sad1/Kms/Bqt genes require an applicability check even without expression claims. Fresh native catalogue contains no matching fungal species/strain; downstream gene/module queries therefore do not apply. The historical shared-runner failure remains unavailable execution; fresh source fallback is not a runner success or experimental mechanism proof.

### Original validation, source hashes and current protein gates

schema: supported. Targets: GO:0061645, GO:0034993, GO:1990612.

Original bundles validate and render exactly with all14 historical hashes each. Six current protein commands at the source head exit0, with logs independently hash-verified. These deterministic results do not erase retained scientific findings; root separately owns corpus QC and final-head CI.

### Current exact structure identity, hierarchy and source-bounded definition

identity: supported. Targets: GO:0000930.

Native GO identity, multiprotein kind and category are sound. Generic complex, TuSC and TuRC are retained as distinct identities; MTOC/SPB/eMTOC are contexts rather than replacement identities. Appended structural details remain subject to the source-specific concerns below.

### Substantive refresh of changed maintained inputs

schema: supported. Targets: GO:0000930.

Original frozen target bytes match their historical source; current main differs. Expanded protein examples and grouped component types have been independently checked. Complex/small also add budding-yeast canonical context and component/edge literature. The original files remain historical; this is a current-input successor with exact finding lineage.

### Current accession identity versus source-specific membership

grounding: supported. Targets: GO:0000930.

All six examples match reviewed identities: P25295/Q9Y705/Q9USQ2 in S. pombe 972h- and P53378/P38863/P53540 in S288C. The added budding-yeast review is correctly scoped secondary evidence for Spc97/Spc98; P25295 is correctly disambiguated from Q9USH8. Vardy/Toda supports Alp6 localization.

### Already merged grouped-type and evidence corrections

consistency: supported. Targets: GO:0000930.

The GCP2/GCP3 component is now PROTEIN_COMPLEX and the added budding-yeast component/edge review source is present. These are already-on-main repairs associated with #2420/#2470, not edits performed by this PR. The wrong fission-yeast Viswanath attribution remains.

### Current source-attribution and molecular scope

evidence: concern. Targets: GO:0000930.

Conserved gamma/Alp4/Alp6 and budding-yeast Tub4/Spc97/Spc98 membership are supported. Viswanath2017 still has the wrong organism/experiment assigned in component, graph and canonical-example fields. Receptor/domain and exact ring-state details require species-specific structural sources rather than GO alone.

### Membership/output summary versus resolved causal mechanism

graph: concern. Targets: GO:0000930.

Functions and graph still use the SPB as acting structure, including duplication/separation, instead of explaining the molecular complex contribution. Membership/context and whole-complex output edges remain labeled MECHANISTIC. Native node coverage does not fix this bounded representation concern.

### Assembly necessity separated from identity, localization and viability

evidence: unknown. Targets: GO:0000930.

ESSENTIAL core, CONDITIONAL noncore and/or DISPENSABLE associated-machinery declarations cannot be independently generalized from identity, viability or nucleation phenotypes. Residual Mto2-mutant PAA activity and conditional Mzt1 core association are specific endpoints, not tests of every complete ring state. The unknown is retained; no finding is invented solely for the lack of a universal assembly assay.

### Taxon, family and nonasserted optional surfaces

scope: supported. Targets: GO:0000930.

Declared taxon identifiers and reference-example names match native authorities. Fission/budding-yeast experiments do not establish a complete eukaryote inventory or identical receptor/geometry across fungi. Gamma family specificity is available; optional ungrounded mixed-family slots are not automatic defects. No image asset, quantitative property, dataset, trait link or verbatim snippet is asserted by these targets.

### Named-protein structured-source applicability

evidence: not_applicable. Targets: GO:0000930.

Named genes/accessions trigger the policy. The historical runner is unavailable, and fresh inspection of all 20 official catalogue organisms/28 dataset keys yields no matching eukaryotic organism. Therefore downstream gene search/module summarize is not applicable; no negative biological conclusion follows. This corrects the original unsupported structural-claim exemption.

### Current native protein diagnostic and historical bundle validation

schema: supported. Targets: GO:0000930.

Root-run current native --verify and --causal-graphs each exited zero with their actual receipts. The two GENE_OR_PROTEIN nodes are covered by declared examples. Independently rerun original schema/render checks pass and reproduce Markdown. These checks certify their bounded syntax/identity coverage, not scientific truth or current CI.

### Current exact structure identity, hierarchy and source-bounded definition

identity: supported. Targets: GO:0000931.

Native GO identity, multiprotein kind and category are sound. Generic complex, TuSC and TuRC are retained as distinct identities; MTOC/SPB/eMTOC are contexts rather than replacement identities. Appended structural details remain subject to the source-specific concerns below.

### Substantive refresh of changed maintained inputs

schema: supported. Targets: GO:0000931.

Original frozen target bytes match their historical source; current main differs. Expanded protein examples and grouped component types have been independently checked. Complex/small also add budding-yeast canonical context and component/edge literature. The original files remain historical; this is a current-input successor with exact finding lineage.

### Current accession identity versus source-specific membership

grounding: supported. Targets: GO:0000931.

All eight declared examples match reviewed identities. New Alp6/Gfh1/Mod21/Alp16 evidence provenance matches native entries, and inspected primary localization/membership studies support those bounded claims. Matsuyama2006 ORFeome is not treated as a newly inspected individual-image experiment. Identity additions do not resolve structural/allosteric source inflation.

### Already merged grouped-type and evidence corrections

consistency: supported. Targets: GO:0000931.

Mto1/Mto2 and GCP4/GCP5/GCP6 grouped components are now PROTEIN_COMPLEX, consistent with historical #2420/#2431 changes. This does not imply new structural proof of a seam or whole-category disposition.

### Current source-attribution and molecular scope

evidence: concern. Targets: GO:0000931.

Core/noncore membership and Mto1/Mto2 recruitment/nucleation are supported. Samejima2010 does not establish 13-protofilament ring geometry; Samejima2005 does not establish a Gfh1/Mod21/Alp16 14-spoke seam. Lynch2014 leaves conformational activation unresolved. Original structural/allostery finding remains open despite the new protein examples.

### Membership/output summary versus resolved causal mechanism

graph: concern. Targets: GO:0000931.

The graph retains component parthood, Mto1/Mto2 association and whole-complex nucleation output, rather than a resolved source-backed causal mechanism. MECHANISTIC scope remains overstated; assembly/activity/source qualifications must be retained.

### Assembly necessity separated from identity, localization and viability

evidence: unknown. Targets: GO:0000931.

ESSENTIAL core, CONDITIONAL noncore and/or DISPENSABLE associated-machinery declarations cannot be independently generalized from identity, viability or nucleation phenotypes. Residual Mto2-mutant PAA activity and conditional Mzt1 core association are specific endpoints, not tests of every complete ring state. The unknown is retained; no finding is invented solely for the lack of a universal assembly assay.

### Taxon, family and nonasserted optional surfaces

scope: supported. Targets: GO:0000931.

Declared taxon identifiers and reference-example names match native authorities. Fission/budding-yeast experiments do not establish a complete eukaryote inventory or identical receptor/geometry across fungi. Gamma family specificity is available; optional ungrounded mixed-family slots are not automatic defects. No image asset, quantitative property, dataset, trait link or verbatim snippet is asserted by these targets.

### Named-protein structured-source applicability

evidence: not_applicable. Targets: GO:0000931.

Named genes/accessions trigger the policy. The historical runner is unavailable, and fresh inspection of all 20 official catalogue organisms/28 dataset keys yields no matching eukaryotic organism. Therefore downstream gene search/module summarize is not applicable; no negative biological conclusion follows. This corrects the original unsupported structural-claim exemption.

### Current native protein diagnostic and historical bundle validation

schema: supported. Targets: GO:0000931.

Root-run current native --verify and --causal-graphs each exited zero with their actual receipts. The two GENE_OR_PROTEIN nodes are covered by declared examples. Independently rerun original schema/render checks pass and reproduce Markdown. These checks certify their bounded syntax/identity coverage, not scientific truth or current CI.

### Current exact structure identity, hierarchy and source-bounded definition

identity: supported. Targets: GO:0008275.

Native GO identity, multiprotein kind and category are sound. Generic complex, TuSC and TuRC are retained as distinct identities; MTOC/SPB/eMTOC are contexts rather than replacement identities. Appended structural details remain subject to the source-specific concerns below.

### Substantive refresh of changed maintained inputs

schema: supported. Targets: GO:0008275.

Original frozen target bytes match their historical source; current main differs. Expanded protein examples and grouped component types have been independently checked. Complex/small also add budding-yeast canonical context and component/edge literature. The original files remain historical; this is a current-input successor with exact finding lineage.

### Current accession identity versus source-specific membership

grounding: supported. Targets: GO:0008275.

All six examples match reviewed identities: P25295/Q9Y705/Q9USQ2 in S. pombe 972h- and P53378/P38863/P53540 in S288C. The added budding-yeast review is correctly scoped secondary evidence for Spc97/Spc98; P25295 is correctly disambiguated from Q9USH8. Vardy/Toda supports Alp6 localization.

### Already merged grouped-type and evidence corrections

consistency: supported. Targets: GO:0008275.

The GCP2/GCP3 component is now PROTEIN_COMPLEX and the added budding-yeast component/edge review source is present. These are already-on-main repairs associated with #2420/#2470, not edits performed by this PR. The wrong fission-yeast Viswanath attribution remains.

### Current source-attribution and molecular scope

evidence: concern. Targets: GO:0008275.

Conserved gamma/Alp4/Alp6 and budding-yeast Tub4/Spc97/Spc98 membership are supported. Viswanath2017 still has the wrong organism/experiment assigned in component, graph and canonical-example fields. Receptor/domain and exact ring-state details require species-specific structural sources rather than GO alone.

### Membership/output summary versus resolved causal mechanism

graph: concern. Targets: GO:0008275.

Functions and graph still use the SPB as acting structure, including duplication/separation, instead of explaining the molecular complex contribution. Membership/context and whole-complex output edges remain labeled MECHANISTIC. Native node coverage does not fix this bounded representation concern.

### Assembly necessity separated from identity, localization and viability

evidence: unknown. Targets: GO:0008275.

ESSENTIAL core, CONDITIONAL noncore and/or DISPENSABLE associated-machinery declarations cannot be independently generalized from identity, viability or nucleation phenotypes. Residual Mto2-mutant PAA activity and conditional Mzt1 core association are specific endpoints, not tests of every complete ring state. The unknown is retained; no finding is invented solely for the lack of a universal assembly assay.

### Taxon, family and nonasserted optional surfaces

scope: supported. Targets: GO:0008275.

Declared taxon identifiers and reference-example names match native authorities. Fission/budding-yeast experiments do not establish a complete eukaryote inventory or identical receptor/geometry across fungi. Gamma family specificity is available; optional ungrounded mixed-family slots are not automatic defects. No image asset, quantitative property, dataset, trait link or verbatim snippet is asserted by these targets.

### Named-protein structured-source applicability

evidence: not_applicable. Targets: GO:0008275.

Named genes/accessions trigger the policy. The historical runner is unavailable, and fresh inspection of all 20 official catalogue organisms/28 dataset keys yields no matching eukaryotic organism. Therefore downstream gene search/module summarize is not applicable; no negative biological conclusion follows. This corrects the original unsupported structural-claim exemption.

### Current native protein diagnostic and historical bundle validation

schema: supported. Targets: GO:0008275.

Root-run current native --verify and --causal-graphs each exited zero with their actual receipts. The two GENE_OR_PROTEIN nodes are covered by declared examples. Independently rerun original schema/render checks pass and reproduce Markdown. These checks certify their bounded syntax/identity coverage, not scientific truth or current CI.

### Whole cytoskeleton and specialized septin assemblies

identity: supported. Targets: GO:0032156.

The GO identity, cytoskeleton parent and declared structural parts are consistent. FILAMENT is a broad local kind classification; the text explicitly includes higher-order complexes and arrays and does not equate the entire framework with a single oligomer.

### An exact generic family is available

grounding: concern. Targets: GO:0032156.

The REVIEWED_LABEL_ONLY rationale requires a family identifier for a complete filament-array-forming cohort. The component itself is the generic septin-proteins class, for which IPR016491 is exact. Family identity does not require an exact inventory of proteins occupying each array.

### Correct vegetative examples remain valid at the broader target scope

evidence: supported. Targets: GO:0032156.

All five reviewed gene/accession/taxon identities are correct. Native UniProt annotations support the specifically attributed Huh, Finnigan and Mino localization notes. Finnigan provides directly read bud-neck experiments; the two other cited papers were metadata/abstract- and native-annotation-scoped. Vegetative members are valid examples for the whole cytoskeleton even though the canonical array examples describe spores.

### Expanded architecture and functions exceed the cited taxon scope

scope: concern. Targets: GO:0032156.

The expanded definition generalizes a cortical network and barrier/scaffold recruitment across yeast, filamentous fungi and green algae and several developmental sites. Fresh Versele Introduction supports green-algal ortholog occurrence, while its functional passages concern yeast. Fresh Douglas sporulation and Aspergillus subsections retain proposal/suggestion language for spore-wall and branch regulation. Finnigan directly tests vegetative yeast Bni5/Myo1 recruitment. These do not establish the full combined definition, whose sole definition_source is GO. Five genes are treated as examples, not an ordered rod.

### Developmental examples are nonexhaustive

scope: supported. Targets: GO:0032156.

The two VARIABLE entries explicitly describe sporulation/chlamydospore arrays, supported by their GO child definitions and review context. They do not say that the entire septin cytoskeleton is absent in vegetative cells. No species-wide percentage or exclusive spore membership is inferred.

### Collective material versus individual assembly requirement

evidence: unknown. Targets: GO:0032156.

ESSENTIAL is attached to the whole septin class, not separately to each of the five examples. Septins are defining material of the target, but the cited studies do not constitute removal of the whole class followed by an assembly assay. Individual truncation, viability or recruitment results cannot verify a five-gene universal assembly requirement; none is inferred.

### Supported parthood is not an assembly transition

graph: concern. Targets: GO:0032156.

The three edges record septin-protein, complex and band parthood. They do not describe how assembly happens, despite ASSEMBLY/MECHANISTIC and the mechanism title. Classify the existing descriptive scope accurately or encode a bounded supported transition.

### No mandatory exhaustive inventory

completeness: supported. Targets: GO:0032156.

The broad framework is represented through generic proteins and named substructures. Additional subunit groups, images, functions or quantitative dimensions are optional. The concrete gaps are unjustified generic-family withholding and source/taxon inflation in the expanded definition; specialized composition should not be promoted to a universal cytoskeleton inventory.

### Structured-source applicability

evidence: not_applicable. Targets: GO:0032156.

Named tubulins/septins or specific regulators in the maintained definition trigger the molecular source policy. Fresh official catalogue has no matching fungal, algal or protist dataset. Therefore downstream gene/module queries are not applicable; this follows source coverage, not absence of expression claims. Historical runner failure is separately disclosed.

### Current native protein and original-bundle checks

schema: supported. Targets: GO:0032156.

Current deterministic native checks pass within their actual inventory. Original bundle validation/render and frozen hashes also pass; these do not resolve retained scientific findings or independently prove assembly necessity.

### Spindle identity and generic topology

identity: supported. Targets: GO:0005819.

The whole spindle is a chromosome-segregating microtubule array, distinct from its poles, asters, microtubules and midzone. Native GO supports the record hierarchy and generic parthood convention. No whole-spindle identity replacement is needed.

### Correct combined protein class and concrete examples

grounding: supported. Targets: GO:0005819.

The three reviewed accession/gene/reference-strain identities are correct. The component intentionally combines alpha and beta tubulins; broad IPR000217 would overmatch, while either individual alpha/beta family would cover only part of the row. Its localization-specific grounding rationale could be clearer, but no forced split or inexact family assignment is warranted.

### Protein identity and cited localization are separate from midzone occupancy

evidence: supported. Targets: GO:0005819.

Native UniProt annotations contain the stated cytoskeleton-localization evidence links. Cederquist2012 has a human disease title but its abstract explicitly includes yeast genetic analysis, so the title alone is not a species mismatch. The two papers were checked at native abstract/annotation scope, not full-body scope; localization does not prove every example occupies every spindle region.

### The collective tubulin row is not three individual essentiality assertions

evidence: unknown. Targets: GO:0005819.

Tubulin polymer is defining material of the spindle and overlap microtubules. ESSENTIAL formally concerns whether the structure forms without the declared component; no complete combined-class removal experiment was inspected. GFP-Tub1 imaging and individual mutant function do not establish that each TUB1/TUB2/TUB3 example is independently necessary.

### Added detailed mechanism exceeds its asserted GO source

evidence: concern. Targets: GO:0005819.

The appended definition names Ase1/PRC1, Cin8/Kip1 and motor-associated spindle organization across yeasts, fungi, microalgae and protists. GO supplies the broad array/function definition. Winey identifies morphology and inferred spindle-fiber classes, not the molecular crossbridges. Jaspersen supports specifically budding-yeast Cin8/Kip1 pole separation; the full appended multi-taxon mechanism is not established by these sources.

### Budding-yeast example and whole-spindle function

scope: supported. Targets: GO:0005819.

Winey directly supports the nuclear-spindle EM example in S.cerevisiae, including an S288c-background diploid; the record species label is appropriate. Straight abstract supports GFP-Tub1 imaging and chromosome movement. COMMON is qualitative occurrence, not a measured fraction of every culture. The ordinary chromosome-segregating whole-spindle function is supported.

### Keep GO parthood while correcting the primary citation

provenance: concern. Targets: GO:0005819.

GO includes the aster in its broad spindle hierarchy. Winey explicitly says astral microtubules are outside the spindle per se and restricts its reconstruction to nuclear microtubules. The aster-to-spindle edge is thus valid under GO but misattributed to that particular primary analysis.

### Descriptive edges do not represent the named molecular mechanism

graph: concern. Targets: GO:0005819.

The graph records tubulin and substructure parthood plus a whole-spindle segregation edge. It does not represent the named crosslinking/motor steps as causal transitions. The supported topology should be distinguished from its MECHANISTIC classification.

### Specific evidence repairs rather than compulsory inventory

completeness: supported. Targets: GO:0005819.

Tubulin, major structural regions and whole-spindle function are represented. The actionable omissions are matching evidence for appended mechanism and accurate graph/source scope, not an obligatory exhaustive list of spindle proteins.

### Structured-source applicability

evidence: not_applicable. Targets: GO:0005819.

Named tubulins/septins or specific regulators in the maintained definition trigger the molecular source policy. Fresh official catalogue has no matching fungal, algal or protist dataset. Therefore downstream gene/module queries are not applicable; this follows source coverage, not absence of expression claims. Historical runner failure is separately disclosed.

### Current native protein and original-bundle checks

schema: supported. Targets: GO:0005819.

Current deterministic native checks pass within their actual inventory. Original bundle validation/render and frozen hashes also pass; these do not resolve retained scientific findings or independently prove assembly necessity.

### Overlap region is distinct from the entire spindle

identity: supported. Targets: GO:0051233.

GO0051233 identifies the region where microtubules from opposite poles overlap; its spindle parthood is correct. Microtubule segments occupy the overlap, but not every spindle microtubule is thereby wholly contained in the midzone. The record should retain this regional boundary when describing parts.

### Correct combined protein class and concrete examples

grounding: supported. Targets: GO:0051233.

The three reviewed accession/gene/reference-strain identities are correct. The component intentionally combines alpha and beta tubulins; broad IPR000217 would overmatch, while either individual alpha/beta family would cover only part of the row. Its localization-specific grounding rationale could be clearer, but no forced split or inexact family assignment is warranted.

### Protein identity and cited localization are separate from midzone occupancy

evidence: supported. Targets: GO:0051233.

Native UniProt annotations contain the stated cytoskeleton-localization evidence links. Cederquist2012 has a human disease title but its abstract explicitly includes yeast genetic analysis, so the title alone is not a species mismatch. The two papers were checked at native abstract/annotation scope, not full-body scope; localization does not prove every example occupies every spindle region.

### The collective tubulin row is not three individual essentiality assertions

evidence: unknown. Targets: GO:0051233.

Tubulin polymer is defining material of the spindle and overlap microtubules. ESSENTIAL formally concerns whether the structure forms without the declared component; no complete combined-class removal experiment was inspected. GFP-Tub1 imaging and individual mutant function do not establish that each TUB1/TUB2/TUB3 example is independently necessary.

### Whole-spindle kinetochore coupling is not a midzone-specific mechanism

graph: concern. Targets: GO:0051233.

The function, process-node description and midzone-to-segregation edge copy the whole-spindle claim about moving chromosomes through kinetochore coupling. Their nearest GO evidence defines the entire spindle. Midzone participation in chromosome separation is reasonable, but that does not establish this regional structure as the whole kinetochore-coupling apparatus. Winey supports overlap/interpolar elongation context while explicitly retaining inferences about kinetochore fibers.

### Specific regulators are not supplied by the ontology definition

evidence: concern. Targets: GO:0051233.

GO defines the overlap region but does not provide the appended Ase1/PRC1, Cin8/Kip1 and Ipl1/Sli15/Bir1 mechanism. The readable ultrastructure does not identify those crossbridges or test chromosomal-passenger regulation. The yeast SPB review supports a narrower Cin8/Kip1 separation context, not the entire multi-taxon central-spindle assertion.

### A plausible phrase is not a source-provided exact synonym

provenance: concern. Targets: GO:0051233.

Native GO0051233 contains central spindle and spindle equator as exact synonyms. It does not supply the maintained central spindle overlap zone string. The phrase can be curated independently, but its current GO attribution is inaccurate.

### Yeast spindle reconstruction provides overlap-region context

scope: supported. Targets: GO:0051233.

Winey analyzes central overlap/interdigitation within nuclear yeast spindles, supporting the species example. The canonical/distribution notes are broad whole-spindle descriptions and could be more specific, but do not assert an incorrect organism. No exact strain identity is inferred beyond the source Methods.

### Descriptive topology and a transferred function are not a mechanistic explanation

graph: concern. Targets: GO:0051233.

The graph gives parthood and a whole-structure mediates edge without a represented overlap-sliding, stabilization or other causal transition. Correct the function attribution and classify the residual descriptive graph accurately; no molecular-detail quota is imposed.

### Correct regional claims before adding optional molecular inventory

completeness: supported. Targets: GO:0051233.

No exhaustive midzone regulator inventory is mandatory. The consequential gaps are source support for specific mechanisms, whole-versus-part functional attribution and a source-labeled synonym, while the basic overlap identity and tubulin class remain sound.

### Structured-source applicability

evidence: not_applicable. Targets: GO:0051233.

Named tubulins/septins or specific regulators in the maintained definition trigger the molecular source policy. Fresh official catalogue has no matching fungal, algal or protist dataset. Therefore downstream gene/module queries are not applicable; this follows source coverage, not absence of expression claims. Historical runner failure is separately disclosed.

### Current native protein and original-bundle checks

schema: supported. Targets: GO:0051233.

Current deterministic native checks pass within their actual inventory. Original bundle validation/render and frozen hashes also pass; these do not resolve retained scientific findings or independently prove assembly necessity.

### Generic pole is broader than a spindle pole body

identity: supported. Targets: GO:0000922.

The target is the polar spindle region, with spindle parthood and a species-specific SPB structural example. It is not equated to only the budding-yeast SPB. The native definition says it usually contains an MTOC; the record distribution also acknowledges acentrosomal poles.

### GO0000930 correctly covers generic gamma-tubulin complexes

grounding: supported. Targets: GO:0000922.

The component label and role explicitly cover gamma-TuSC/gamma-TuRC. Native GO0000930 is the generic gamma-tubulin complex with species-variable partners; its small-complex and ring-complex children must not be confused with the parent. This mapping does not assert that every complex has universal ring geometry or the same subunits.

### The broad pole definition adds a source-unmatched molecular roster

evidence: concern. Targets: GO:0000922.

The appended text combines kinesin-14, NuMA/Pkl1/Mto1 and gamma-tubulin-ring machinery across yeasts, fungi, microalgae and protists. GO supplies the generic regional definition, while Jaspersen is a yeast-SPB review with a centrosome comparison. Its readable sections and Viswanath core context do not establish that entire named combination throughout those groups.

### Keep yeast pole-duplication evidence at its actual scope

scope: concern. Targets: GO:0000922.

The review supports budding-yeast SPB duplication, bridge cleavage and Cin8/Kip1-dependent separation. Its centrosome comparison explicitly preserves similarities and differences. The record evidence notes generalize this to spindle-pole duplication across eukaryotes, including the acentrosomal scope it otherwise acknowledges, without matching evidence.

### Presence and nucleation do not establish universal assembly necessity

evidence: unknown. Targets: GO:0000922.

Both components are ESSENTIAL. Source evidence for yeast MTOC organization and gamma-complex nucleation supports membership/function in that system, but does not show that the broad spindle-pole structure fails to form without each generic component across its taxonomic scope. The schema criterion is formation, not catalytic function, cell viability or presence in the intact reference architecture.

### Broad occurrence and canonical yeast architecture

scope: supported. Targets: GO:0000922.

Eukaryota and S.cerevisiae labels/ranks are correct; the yeast canonical SPB architecture example is supported. COMMON is not treated as a measured prevalence. The broad terminal-region identity does not authorize exporting the exact yeast molecular or duplication mechanism to every eukaryote.

### GO does not supply the maintained narrow synonym

provenance: concern. Targets: GO:0000922.

Native GO0000922 contains no synonym annotation in the inspected response. Mitotic spindle pole is a plausible narrower phrase, but its GO source attribution is unsupported and should be repaired rather than mistaken for a source-provided synonym.

### Organizational description lacks a represented causal transition

graph: concern. Targets: GO:0000922.

The graph links MTOC/gamma-complex/SPB parts and whole-pole functions. Its text describes nucleation/anchoring and duplication, but the edges do not represent those transitions or the component-to-function dependency. Keep supported topology distinct from the stronger MECHANISTIC scope claim.

### No forced molecular census for a generic polar region

completeness: supported. Targets: GO:0000922.

The two class-level components have valid identities. Exact protein examples, stoichiometry, family splitting and full centrosome/SPB inventories are optional. The material problem is unsupported broad mechanism, with assembly necessity explicitly unresolved; optional inventory is not promoted to a finding.

### Structured-source applicability

evidence: not_applicable. Targets: GO:0000922.

Named tubulins/septins or specific regulators in the maintained definition trigger the molecular source policy. Fresh official catalogue has no matching fungal, algal or protist dataset. Therefore downstream gene/module queries are not applicable; this follows source coverage, not absence of expression claims. Historical runner failure is separately disclosed.

### Current native protein and original-bundle checks

schema: supported. Targets: GO:0000922.

Current deterministic native checks pass within their actual inventory. Original bundle validation/render and frozen hashes also pass; these do not resolve retained scientific findings or independently prove assembly necessity.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0061645, GO:0000930, GO:0000931, GO:0008275, GO:0034993, GO:1990612, GO:0032156, GO:0005819, GO:0051233, GO:0000922.

5 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-target0-F1: Source and qualify the added yeast mechanism separately from the GO definition

minor / open / confirmed; issue key: endocytic-patch-expanded-definition-source-scope.

The definition extends the broad GO text with a detailed fungal coat/adaptor/NPF/scission sequence and turgor mechanism while retaining only GO0061645 as its source. The inspected yeast papers support scoped examples and distinguish early coats, actin recruitment and later movement. Attach the appropriate sources and stage/taxon qualifiers, or retain the exact broad definition with the detailed material in supported example notes.

### plaque-target0-F2: Specify assembly stages and recruited machinery or narrow graph scope

minor / open / confirmed; issue key: endocytic-patch-self-assembly-graph-scope.

The FUNCTION/MECHANISTIC graph is a membership/function summary, and the patch-to-actin-cortical-patch-assembly edge cites only a GO process definition. The broad endocytic patch can precede its actin-rich stage: the inspected studies describe early regulator recruitment followed by network assembly. The present graph does not specify those stages or the recruited causal machinery. Preserve valid membership/output context as NONMECHANISTIC or add a source-supported, stage-specific causal transition; do not treat this as proof that an early endocytic patch cannot organize later actin assembly.

### plaque-target4-F1: Keep the membrane tether distinct from the horsetail-astral array

major / open / confirmed; issue key: meiotic-membrane-tether-horsetail-array-function-transfer.

The function description and corresponding graph process/edge state that the membrane complex provides the radial microtubule array. Their GO0032117 evidence is called the exact structure definition, but that term denotes the HAA rather than GO0034993. Funaya2012 directly distinguishes array/rMTOC organization from the envelope bridge. Correct the actor/function and evidence placement without discarding the supported role in connecting chromosomes, membranes and the cytoskeleton.

### plaque-target4-F2: Bound the taxonomic and motor claim to demonstrated systems

major / open / confirmed; issue key: meiotic-membrane-tether-fungi-dynein-scope.

The Fungi COMMON annotation and conserved dynein-coupling note are sourced to Chikashige2006, whose primary abstract establishes an S.pombe Bqt1/Bqt2 bridge. That does not demonstrate the frequency or motor mechanism of a microtubule-tethering complex across fungi. Lee2020 examines a related budding-yeast LINC/Myo2/actin system, so generic SUN/KASH conservation cannot fill that gap. This is not a claim that no other fungus has a microtubule-linked tether.

### plaque-target4-F3: Use an honest scope for the current membership/function graph

minor / open / confirmed; issue key: meiotic-membrane-tether-static-graph-scope.

Even after correcting the copied HAA function, the graph has only constituent/compartment relations and a whole-structure output. It does not encode a tethering or force-transmission causal transition, despite MECHANISTIC scope. Use NONMECHANISTIC or represent a directly sourced transition with the proper actor and preparation.

### plaque-target5-F1: Budding-yeast assays and broad fungal coupling are assigned to the named complex

major / open / confirmed; issue key: sad1-kms1-fungal-linc-scope-transfer.

Fan2020 directly tests budding-yeast Mps2–Mps3–Csm4, while both Fan-only output edges use Sad1–Kms1 as their subject. The pairing description acknowledges budding yeast but that qualifier does not change the graph subject or make the result an assay of Sad1–Kms1. The Fungi COMMON note likewise generalizes this named assembly and dynein/microtubule coupling from fission yeast, despite the distinct actin-associated budding-yeast system. Separate comparative LINC context from functions/distribution of the named S. pombe assembly. This is not a claim that Sad1–Kms1 lacks telomere or recombination roles.

### plaque-target5-F2: Membership and functional outputs are labeled mechanistic

minor / open / confirmed; issue key: sad1-kms1-summary-graph-overstates-mechanistic-scope.

The seven-node graph presents membership/association and whole-complex outputs, without a represented chain explaining how the LINC bridge produces those outcomes. Retain FUNCTION but use honest NONMECHANISTIC scope with notes, or add independently supported causal intermediates and exact edge evidence during authorized curation. This classification issue is separate from the cross-species assignment in F1.

### micro-F1: Replace the budding-yeast paper assigned to fission-yeast composition and example

major / open / confirmed; issue key: wrong-fission-yeast-source.

DOI10.1091/mbc.E17-06-0397 is explicitly a S. cerevisiae SPB-core study. The component evidence and duplicated graph evidence instead say it characterizes fission-yeast Alp4/Alp6, and the canonical S. pombe972h- example says it dissects gamma-TuSC assembly and Mto1/Mto2 nucleation. Those experiments are not in this cited primary source. The underlying fission-yeast biology has suitable primary evidence, so this is an evidence/organism attribution error rather than a wrong GO identity. Current budding-yeast evidence added under #2470 is present but does not correct the remaining fission-yeast source assignment.

### micro-F2: Describe the complex contribution and align graph scope

minor / open / confirmed; issue key: spb-function-and-graph-scope.

The function descriptions make the SPB, including SPB duplication and separation, their acting structure. The graph repeats those descriptions and labels a membership/context/output summary MECHANISTIC. Gamma-complex nucleation is supported, but these fields do not explain its molecular contribution or a causal path.

### micro-F3: Separate ring architecture and activation claims from the cited targeting studies

major / open / confirmed; issue key: ring-structure-and-allostery-source-inflation.

The record says Samejima2010 establishes TuSC assembly into a13-protofilament-matching ring, and E04-11-1003 characterizes Gfh1/Mod21/Alp16 as a14-spoke asymmetric seam. Their full bodies instead study Mto1 targeting and Mto2-mediated recruitment. The Mto1-Mto2 role further states allosteric activation under Samejima2010, whereas the later direct activation study uses bonsai puncta and explicitly leaves conformational/CM1-alone activation unresolved. Basic membership and nucleation are supported; these exact structural/mechanistic source attributions are not. The expanded reviewed protein examples and corrected grouped types establish identity/representation only; they do not repair these source-attribution defects.

### micro-F4: Align the graph label with its represented causal detail

minor / open / confirmed; issue key: ring-graph-summary-scope.

After correcting the source overstatements, the current graph still consists of component parthood, Mto1-Mto2 association and whole-complex-to-nucleation. These relationships can be supported as a functional/structural summary, but they do not themselves trace a resolved molecular mechanism despite scope_status MECHANISTIC.

### septin-S2353-F1: Ground the generic septin class at its actual family scope

minor / open / confirmed; issue key: septin-cytoskeleton-generic-family-withheld.

The generic septin-proteins row is REVIEWED_LABEL_ONLY because no identifier was assigned for the complete filament-array-forming cohort. Native IPR016491 identifies the Septin family, matching this generic component without identifying every assembly-specific member. Correct the class-versus-cohort criterion and preserve source-specific membership limits.

### septin-S2353-F2: Match graph scope to the represented relationships

minor / open / confirmed; issue key: septin_cytoskeleton_mechanism-static-graph-scope.

The ASSEMBLY graph contains only constituent-to-cytoskeleton parthood edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

### septin-S2353-F3: Separate supported fungal functions from unverified green-algal architecture

major / open / confirmed; issue key: septin-cytoskeleton-definition-taxon-function-scope.

The expanded definition presents a plasma-membrane septin network across yeasts, filamentous fungi and green algae and combines barrier/scaffold recruitment at bud necks, hyphal branches and prospore membranes, while definition_source cites only GO0032156. Versele supports green-algal septin ortholog occurrence, not that full cortical architecture or function. Its functional examples concern yeast; Douglas retains proposal-level language for branch regulator and spore-wall recruitment, and Finnigan directly studies vegetative budding yeast. Supply matching evidence and qualifiers for the retained expansion rather than carrying these narrower observations across the entire taxon/site list.

### septin-S2353-F4: Source and delimit the added molecular spindle mechanism

major / open / confirmed; issue key: spindle-definition-molecular-source-scope.

Only GO0005819 is named as definition_source, but the appended definition asserts specific Ase1/PRC1, Cin8/Kip1 and motor mechanisms across broad microbial eukaryote groups. The inspected primary ultrastructure and yeast review do not establish that entire combined assertion. Retain the correct broad definition and either provide inspected, taxon-matched evidence for the specific mechanism or narrow it to what the cited sources show.

### septin-S2353-F5: Cite the native ontology for the generic aster relationship

minor / open / confirmed; issue key: spindle-aster-parthood-winey-attribution.

The aster-to-spindle edge cites Winey1995. That paper explicitly excludes astral microtubules from the spindle per se and analyzes intranuclear microtubules. GO supports the broader class relation, so correct the evidence attribution without deleting the valid generic topology.

### septin-S2353-F6: Match graph scope to the represented relationships

minor / open / confirmed; issue key: spindle_mechanism-static-graph-scope.

The FUNCTION graph contains structural parthood and whole-structure-to-process mediates edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

### septin-S2353-F7: Give the midzone a region-specific contribution to segregation

major / open / confirmed; issue key: midzone-whole-spindle-kinetochore-function-transfer.

The function and graph directly attach whole-spindle kinetochore-coupling prose to the midzone, citing the whole-spindle GO definition. Preserve the supported overlap identity and an appropriately qualified contribution to segregation, but describe the regional process actually supported by evidence instead of transferring the entire spindle mechanism.

### septin-S2353-F8: Support the added midzone regulator mechanism at its taxon scope

major / open / confirmed; issue key: midzone-regulator-definition-source-scope.

The definition cites only GO0051233 while adding Ase1/PRC1, Cin8/Kip1 and chromosomal-passenger identities as an organizing mechanism across yeasts, fungi and microbial eukaryotes. Neither that GO definition nor the inspected primary morphology establishes the entire assertion. The claim needs a matching inspected source and organism/stage qualification.

### septin-S2353-F9: Correct the GO attribution of the added synonym

minor / open / confirmed; issue key: midzone-go-synonym-provenance.

The maintained exact synonym central spindle overlap zone is not a synonym supplied by the inspected native GO0051233 record. GO instead supplies central spindle and spindle equator. Repair the provenance or use an actual source-provided synonym.

### septin-S2353-F10: Match graph scope to the represented relationships

minor / open / confirmed; issue key: spindle_midzone_mechanism-static-graph-scope.

The FUNCTION graph contains structural parthood and whole-structure-to-process mediates edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

### septin-S2353-F11: Bound the specific pole mechanism and duplication claims to their evidence

major / open / confirmed; issue key: spindle-pole-mechanism-taxonomic-source-inflation.

The definition adds a combined kinesin-14/NuMA/Pkl1/Mto1/gamma-ring mechanism across broad microbial eukaryote groups while citing only the generic GO definition. The function and graph evidence further say the yeast-focused review establishes pole duplication/separation across eukaryotes. The inspected review and primary yeast-core context support narrower claims; neither establishes this whole combined generalization.

### septin-S2353-F12: Repair the source attribution of the narrow pole synonym

minor / open / confirmed; issue key: spindle-pole-narrow-synonym-go-provenance.

The phrase mitotic spindle pole is labeled a GO0000922 narrow synonym, but the native term does not supply that synonym. Preserve it only with an appropriate independent source/curator provenance or use the source-provided annotations.

### septin-S2353-F13: Match graph scope to the represented relationships

minor / open / confirmed; issue key: spindle_pole_mechanism-static-graph-scope.

The FUNCTION graph contains structural parthood and whole-structure-to-process mediates edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

## Recommended Actions And Acceptance Checks

### plaque-target0-A1

Preserve the generic endocytic-patch identity while attributing the added molecular and pressure-dependent details to the experiments that support them.

- Do not collapse the broad endocytic site and its actin-rich subtype or all temporal phases.
- Keep turgor-dependent invagination separate from post-scission transport and retain the studied yeast scope.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### plaque-target0-A2

Specify the stage and recruited machinery supporting the assembly edge, or represent the graph at its supported nonmechanistic level.

- Distinguish the early endocytic site from its later actin-rich stage; support the causal transition with experimental evidence rather than the assembly-process definition alone.
- Retain supported actin/Arp2/3 membership and yeast internalization evidence.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### plaque-target4-A1

Describe the supported tethering contribution and cite evidence for that exact role; reserve HAA organization and array identity for the corresponding structures.

- Do not treat a neighboring structure term as the exact identity of this complex.
- Distinguish physical linkage from microtubule nucleation, array organization and motor force generation.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### plaque-target4-A2

Narrow distribution/mechanism to verified taxa or provide separately inspected evidence for the broader microtubule-specific class, preserving the distinction from actin-linked LINC systems.

- COMMON at a broad taxon requires evidence beyond one studied species.
- Do not transfer specific Sad1/Kms1/Bqt or dynein identities to all fungal SUN/KASH assemblies.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### plaque-target4-A3

Calibrate graph scope independently of the supported physical membership statements.

- Retain valid Sad1/Kms1/Bqt relationships and correct function scope.
- A meaningful source-backed causal step suffices; no atomistic mechanism is required.
- Apply only through separately authorized scientific curation, guarded writing, append-only history, rendering and native validation.

### plaque-target5-A1

During authorized curation, bind named Sad1–Kms1 functions and edges to appropriate fission-yeast primary passages. Retain Fan/Lee findings only as explicitly comparative budding-yeast context, with their actual molecular subject. Narrow distribution to evidenced named-complex scope and distinguish conserved LINC architecture from motor/taxon generalizations.

- Every resulting causal edge must have the same molecular subject and organism as its cited assay; retain SK1/S288C versus fission-yeast distinctions.
- Preserve supported S/G2 DSB and meiotic telomere roles without claiming that Swartz mitotic gene conversion is the same assay as Fan meiotic conversion.
- Do not infer COMMON exact-subunit distribution or dynein coupling from Fungi taxonomy or generic SUN-family conservation.
- Run native schema/strict, protein verify/causal coverage, fresh CURIE/history and scientific edge review after an authorized validated-writer change.

### plaque-target5-A2

Reclassify the current graph as NONMECHANISTIC functional context with scope notes, or build a supported mechanistic chain. Distinguish direct localization/depletion results from proposed motor cross-linking, force transmission and CDK/Sad1 pathways.

- Read each new intermediate and edge against its exact primary result or explicitly labeled model passage.
- Preserve species, meiosis versus mitosis, preparation and mutant-background bounds.
- Recheck graph_kind/scope_status and run focused native validators; preserve PROPOSED status and history unless separately authorized.

### micro-A1

Replace the misassigned source with inspected fission-yeast primary evidence for each retained claim. Cite direct structural work for GRIP-domain/receptor detail, preserve species-specific receptor names and do not promote species experiments to an exact stock assertion.

- Read the replacement claim-bearing primary passage and retain its organism, experimental preparation, endpoint and uncertainty.
- Reconcile duplicated component, definition and graph wording; do not infer assembly necessity from viability or nucleation alone.
- After separately authorized curation, use the guarded writer/history rules and rerun native focused schema, strict, identifier and evidence checks.

### micro-A2

Describe gamma-complex nucleation/templating as its contribution to organizing microtubules and building the spindle, with SPB duplication as context. Either represent the graph as a supported functional/structural summary or add a source-backed receptor recruitment, oligomerization and nucleation chain with appropriate species scope.

- Read the replacement claim-bearing primary passage and retain its organism, experimental preparation, endpoint and uncertainty.
- Reconcile duplicated component, definition and graph wording; do not infer assembly necessity from viability or nucleation alone.
- After separately authorized curation, use the guarded writer/history rules and rerun native focused schema, strict, identifier and evidence checks.

### micro-A3

Retain source-backed core/noncore membership and Mto1/Mto2 recruitment/activation. Remove or explicitly qualify exact geometry, asymmetric seam and allosteric claims until a direct structural/mechanistic source is attached, specifying species, native versus reconstituted preparation and open/closed state. Use Anders2006 for its actual noncore membership/phenotype results and Lynch2014 for its actual bonsai activation results. Narrow the DISPENSABLE explanatory note to residual Mto2-mutant PAA production; assess complete-ring assembly separately.

- Read the replacement claim-bearing primary passage and retain its organism, experimental preparation, endpoint and uncertainty.
- Reconcile duplicated component, definition and graph wording; do not infer assembly necessity from viability or nucleation alone.
- After separately authorized curation, use the guarded writer/history rules and rerun native focused schema, strict, identifier and evidence checks.

### micro-A4

Either label the supported membership/output representation appropriately or add an explicitly sourced, taxon-scoped causal path from recruitment/oligomerization through template organization to nucleation. Preserve proposed conformational steps as hypotheses.

- Read the replacement claim-bearing primary passage and retain its organism, experimental preparation, endpoint and uncertainty.
- Reconcile duplicated component, definition and graph wording; do not infer assembly necessity from viability or nucleation alone.
- After separately authorized curation, use the guarded writer/history rules and rerun native focused schema, strict, identifier and evidence checks.

### septin-S2353-C1

During authorized curation, assign IPR016491 to the generic septin-proteins row and explain that family membership does not establish a complete assembly-specific cohort.

- Retain the correct five reviewed protein examples at whole-cytoskeleton scope.
- Do not equate vegetative and sporulation-specific subunit inventories.
- Do not replace the family with a broader GTPase domain.
- Run focused schema, strict-reference and native protein checks.

### septin-S2353-C2

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

### septin-S2353-C3

During authorized curation, distinguish the native GO definition, source-specific fungal functions and green-algal ortholog evidence; qualify proposed recruitment roles or obtain directly matching evidence.

- Do not promote gene occurrence to a demonstrated cortical network or its molecular functions.
- Preserve budding-yeast versus filamentous-fungal versus sporulation scope and observed-versus-proposed distinctions.
- Keep the correct broad cytoskeleton identity and valid vegetative protein examples.
- Run focused schema, strict-reference and scientific evidence checks.

### septin-S2353-C4

During authorized curation, separate the ontology definition from source-supported molecular elaboration and qualify organisms, stage and experimental inference.

- Do not cite GO as the source of molecular detail absent from its definition.
- Retain review-tier status for Jaspersen and primary morphological scope for Winey.
- Use direct inspected evidence for any retained named crosslinker or motor mechanism.
- Run focused schema and strict-reference checks.

### septin-S2353-C5

During authorized curation, use the verified GO relation for this edge and retain Winey for its actual nuclear-spindle reconstruction.

- Preserve the difference between source-specific spindle conventions.
- Do not claim Winey reconstructed an astral array.
- Run focused schema and strict-reference checks.

### septin-S2353-C6

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

### septin-S2353-C7

During authorized curation, qualify the midzone contribution using directly supported overlap/interpolar behavior, or route the broad kinetochore-coupling function through the whole-spindle node.

- Keep GO0051233 as the regional identity.
- Do not treat the generic spindle definition as proof of a region-specific molecular mechanism.
- Preserve source uncertainty about putative kinetochore fibers in the EM analysis.
- Run focused schema, strict-reference and causal-graph checks.

### septin-S2353-C8

During authorized curation, provide source-specific evidence for each retained mechanistic grouping or narrow the definition to the supported overlap structure and bounded yeast behavior.

- Keep ontology and literature-derived statements distinguishable.
- Do not use unidentified ultrastructural crossbridges as identification of Ase1 or CPC.
- Do not infer a uniform molecular cohort across the named taxa.
- Run focused schema and strict-reference checks.

### septin-S2353-C9

During authorized curation, use a native synonym or provide a genuine source for the curated phrase.

- Do not imply that GO supplied a string absent from its annotation.
- Preserve exact-versus-curated synonym distinction.
- Run focused schema and strict-reference checks.

### septin-S2353-C10

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

### septin-S2353-C11

During authorized curation, retain the generic regional definition and qualify named molecular/duplication mechanisms to directly supported organisms and spindle stages, or supply inspected sources covering the broader assertion.

- Preserve the difference between a spindle pole, yeast SPB, centrosome and acentrosomal pole.
- Retain GO0000930 for the generic gamma-complex class; do not replace it with a falsely universal ring-only identity.
- Do not describe review synthesis as primary experimental proof.
- Resolve component assembly necessity separately from nucleation activity.
- Run focused schema, strict-reference and causal-graph checks.

### septin-S2353-C12

During authorized curation, correct the source for the added phrase rather than treating plausible wording as a native GO annotation.

- Verify the exact source string and synonym scope.
- Do not invent an ontology synonym when the response contains none.
- Run focused schema and strict-reference checks.

### septin-S2353-C13

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/cytoskeleton/endocytic_patch.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd; current SHA256 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T094807Z-endocytic-patch-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/cytoskeleton/gamma_tubulin_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b9d0f02cefde432060b919928520d31642f07c3979aa91ba5786e8d5facbc2d1; current SHA256 99fd52614b713f1cc678720626553f27f33f5cc4ee0d43b6adfe22108687798d. Changed record reassessed against current sources. |
| original-review-1 | reviews/structured/20261021T094810Z-gamma-tubulin-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 77875af04893db1912e05c01ece8dd67b958d77d452787639401288060226df9; current SHA256 d8eb02a102133174291f4bdbcf09e2d2dfacdc46b217bea636a9bf598ff3d626. Changed record reassessed against current sources. |
| original-review-2 | reviews/structured/20261021T094812Z-gamma-tubulin-ring-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 31bb27b71d6725bf736455a92b5e47849d17869af98675adc45eb9b4a157e1c6; current SHA256 231626322f95f06e53ca5d2dcff46f9227d686cd3e73dcfd2e5d99696121f7c3. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261021T094813Z-gamma-tubulin-small-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 1edc92bdba11eec4c3da00ba06bd5cae3bd2593f5ba94be9d545c52a9da86049; current SHA256 b88b24ae10c1c8ceb36cb1489992fabe20600bff7e85e71a9fd3048d02e15b00. Changed record reassessed against current sources. |
| original-review-4 | reviews/structured/20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2dc179231cae9404e022e417327a94b550b75c47872ef2e467330ea79d5cdf17; current SHA256 4bf976f7c39fe18c961e155a1e4304153986b271209d2d35aa520a8406c03c65. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261021T094818Z-sad1-kms1-linc-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/cytoskeleton/septin_cytoskeleton.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e; current SHA256 a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T094819Z-septin-cytoskeleton-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/cytoskeleton/spindle.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e; current SHA256 da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e. Record bytes unchanged since the original review. |
| original-review-7 | reviews/structured/20261021T094822Z-spindle-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/cytoskeleton/spindle_midzone.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661; current SHA256 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T094824Z-spindle-midzone-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/cytoskeleton/spindle_pole.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204; current SHA256 c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T094825Z-spindle-pole-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-endocytic-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0005885,GO:0005938,GO:0015629,GO:0030479,GO:0030864,GO:0061645,GO:0110165; All requested term names, definitions, obsoletion, synonym and returned child relation objects | supports | Fresh native terms distinguish broad GO0061645 endocytic patch from its GO0030479 actin-rich subtype and confirm exact Arp2/3, cell-cortex and process identities/relations. GO-only definitions do not establish the added complete fungal molecular sequence. |
| plaque-endocytic-prep-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank and lineage | supports | Native taxonomy resolves 4932 as Saccharomyces cerevisiae (species); taxon validity is distinct from demonstrated distribution of a named assembly. |
| plaque-endocytic-prep-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName, rank and lineage | supports | Native taxonomy resolves 559292 as Saccharomyces cerevisiae S288C (strain); taxon validity is distinct from demonstrated distribution of a named assembly. |
| plaque-endocytic-prep-jats-jcb.200404159 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2172413.1/PMC2172413.1.xml; Entire main scientific Introduction, Results/discussion and Methods; main figure captions; Table I caption (not supplementary assets or image pixels). | partial | Young2004 directly examines partially purified, stabilized S. cerevisiae cortical patches by correlated fluorescence/negative-stain EM. Branched actin geometry is consistent with Arp2/3; Sac6 and Cap1 perturbations distinguish stability from general architecture. KS buffer, crosslinking and latrunculin treatments bound inference; this is not a whole-fungal component census. |
| plaque-endocytic-prep-galletta2008-plos | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060001; Publisher HTML: Introduction three-phase account; first Las17 acidic-domain Results and Figure 2 caption; immediately following Myo3/Myo5 paragraph. Other Results/Methods/supplements not freshly audited. | partial | Galletta2008 distinguishes recruitment, slow inward movement and later motion at yeast endocytic sites. Las17 acidic-domain removal delays actin arrival and affects later movement; GFP-Las17 fusion limitations are explicit. Early patches can organize later actin assembly. This is not evidence that every patch stage has the same composition. |
| plaque-endocytic-prep-aghamohammadzadeh2009-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2875176.1/PMC2875176.1.xml; Entire ten main-body paragraphs, from background through concluding model; supplemental Methods and image pixels not inspected. | partial | Aghamohammadzadeh2009 manipulates osmotic support and actin-bundling/latrunculin conditions in yeast. Sorbitol partially rescues invagination yet post-scission movement remains limited; increased turgor impairs invagination. This supports a condition-specific turgor/actin mechanism, not universal obligatory actin membership at every endocytic stage. |
| plaque-endocytic-prep-kaksonen2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:14622601%20AND%20SRC:MED; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 14622601 10.1016/s0092-8674(03)00883-3 A pathway for association of receptors, adaptors, and actin during endocytic internalization.. No whole-body claim from metadata. Complete abstract read: stage-dependent recruitment, late actin assembly and Sla2-mutant actin comet tails support early endocytic sites organizing subsequent actin assembly. |
| plaque-endocytic-prep-doi-jcb.200404159-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200404159; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 15337772 10.1083/jcb.200404159 Yeast actin patches are networks of branched actin filaments.. No whole-body claim from metadata. |
| plaque-endocytic-prep-doi-journal.pbio.0060001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pbio.0060001; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 18177206 10.1371/journal.pbio.0060001 Distinct roles for Arp2/3 regulators in actin assembly and endocytosis.. No whole-body claim from metadata. |
| plaque-endocytic-prep-pmid-11248049-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11248049%20AND%20SRC%3AMED; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 11248049 10.1073/pnas.051494698 Arp2/3 complex and actin dynamics are required for actin-based mitochondrial motility in yeast.. No whole-body claim from metadata. Complete abstract read: direct focus is Arp2/Arc15 mitochondrial association and dynamics, while the native UniProt localization annotation is separately verified. No body-level patch experiment is inferred. |
| plaque-endocytic-prep-pmid-9210376-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9210376%20AND%20SRC%3AMED; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 9210376 10.1016/s0960-9822(06)00223-5 The complex containing actin-related proteins Arp2 and Arp3 is required for the motility and integrity of yeast actin patches.. No whole-body claim from metadata. Complete abstract read: Arp3 patch localization, conditional mutant effects and purified complex are reported. No full-body inspection claimed. |
| plaque-endocytic-prep-P60010 | https://rest.uniprot.org/uniprotkb/P60010.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P60010 matches ACT1, Actin, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-P32381 | https://rest.uniprot.org/uniprotkb/P32381.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P32381 matches ARP2, Actin-related protein 2, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-P47117 | https://rest.uniprot.org/uniprotkb/P47117.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P47117 matches ARP3, Actin-related protein 3, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-P38328 | https://rest.uniprot.org/uniprotkb/P38328.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P38328 matches ARC40, Actin-related protein 2/3 complex subunit 1, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-P53731 | https://rest.uniprot.org/uniprotkb/P53731.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P53731 matches ARC35, Actin-related protein 2/3 complex subunit 2, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-P33204 | https://rest.uniprot.org/uniprotkb/P33204.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P33204 matches ARC19, Actin-related protein 2/3 complex subunit 4, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-Q05933 | https://rest.uniprot.org/uniprotkb/Q05933.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry Q05933 matches ARC18, Actin-related protein 2/3 complex subunit 3, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-P40518 | https://rest.uniprot.org/uniprotkb/P40518.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P40518 matches ARC15, Actin-related protein 2/3 complex subunit 5, taxon 559292. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-endocytic-prep-ACT1-query | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29%20AND%20%28organism_id%3A559292%29%20AND%20%28gene_exact%3AACT1%29&amp;format=json&amp;size=500; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P60010', 'ACT1', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARP2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARP2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P32381', 'ARP2', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARP3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P47117', 'ARP3', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARC40 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC40%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P38328', 'ARC40', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARC35 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC35%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P53731', 'ARC35', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARC19 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC19%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P33204', 'ARC19', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARC18 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC18%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('Q05933', 'ARC18', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-query-ARC15 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC15%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon query results | supports | Native exact query returns [('P40518', 'ARC15', 559292)]; identity mapping only, not direct localization or mechanism. |
| plaque-endocytic-prep-IPR004000 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/; metadata name/type and non-LLM native description | supports | IPR004000 Actin family explicitly includes divergent Arp subfamilies; it is broader than conventional actin. Its presence does not by itself invalidate the bounded label-only component. No exhaustive exact-family absence claim is made. |
| plaque-tether-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030989,GO:0032117,GO:0034992,GO:0034993,GO:0106094; All requested term names, definitions, obsoletion, synonym and returned child relation objects | supports | Fresh native GO identities and exact returned relationships inspected for GO:0030989 dynein-driven meiotic oscillatory nuclear movement, GO:0106094 nuclear membrane microtubule tethering complex, GO:0032117 horsetail-astral microtubule array, GO:0034992 microtubule organizing center attachment site, GO:0034993 meiotic nuclear membrane microtubule tethering complex. GO0032117 is an array, distinct from GO0034993 tether; GO0034993 has GO1990612 as is_a child. Source-neutral definitions do not establish the appended detailed molecular/taxonomic claims. |
| plaque-tether-prep-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; taxId, scientificName, rank and lineage | supports | Native taxonomy resolves 284812 as Schizosaccharomyces pombe 972h- (strain); taxon validity is distinct from demonstrated distribution of a named assembly. |
| plaque-tether-prep-tax-4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; taxId, scientificName, rank and lineage | supports | Native taxonomy resolves 4751 as Fungi (kingdom); taxon validity is distinct from demonstrated distribution of a named assembly. |
| plaque-tether-prep-doi-j.cell.2006.01.048-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2006.01.048; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 16615890 10.1016/j.cell.2006.01.048 Meiotic proteins bqt1 and bqt2 tether telomeres to form the bouquet arrangement of chromosomes.. No whole-body claim from metadata. Complete primary abstract read: Bqt1 and Bqt2 jointly bridge Rap1 and Sad1; neither alone suffices, including ectopic mitotic expression. Supports distinct-protein complex typing at this scope. |
| plaque-tether-prep-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml; Funaya2012 PMC3382715.1: Introduction sec1; Results sec2.1–2.3 and sec2.5; Discussion sec3; Methods sec4.1. No fresh supplements, figure-pixel or movie inspection. | partial | Fresh primary JATS distinguishes Hrs1-dependent rMTOC/radial array from the nuclear-envelope bridge. EM tomography of synchronized engineered meiotic cells and Hrs1 localization support array organization. Introductory Kms1/Sad1 topology is prior-study background; direct Hrs1 phosphomutant two-hybrid assays test Kms1/Alp4 interactions and discuss possible Kms2 compensation. These are not direct dynein-recruitment assays. |
| plaque-tether-prep-moiseeva2017-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml; Results Bouquet formation ensures entry into meiosis I and Premature termination of the bouquet leads to spindle defects (all paragraphs); Methods Strains/media, Microscope image acquisition and Auxin-inducible system. | partial | Moiseeva2017 shows Bqt1-AID disruption releases telomeres from the SPB and can cause prophase/spindle defects. Approximately half of bouquet-deficient cells still divide; direct spindle imaging uses rdh54 background. Main culture/media and 28 C imaging conditions were inspected. These are attachment/function assays, not a complete core-LINC assembly-necessity test. |
| plaque-tether-prep-jimenez2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml; Results Sec8 paragraphs1–6 including integrated Figure6 caption, Sec9 paragraph1, Sec10 paragraph1/Figure7 caption; Methods Sec14 paragraphs1–3. | partial | Jimenez2025 observes Bqt1/Bqt2-dependent recruitment of Sad1/Kms1, Alp4 and Mto1 to telomeres in Rabl-deficient mitotic haploids. No Dhc1 or complete bouquet was detected in that partial reconstitution. Natural meiotic entry is a separate diploid experiment. The maintained Kms1 example correctly preserves that limitation. |
| plaque-linc-agent-csm2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml; Introduction S1; Results S5–S8; Discussion S10; Methods S14 and S16–S20. No raw movies or complete supplementary strain tables inspected. | partial | Lee2020 tests budding-yeast Mps2/Mps3/Csm4/Myo2 with localization, co-IP, two-hybrid and dominant-negative Myo2. It supports an actin-associated motility model and explicitly allows Csm4 stabilization versus actin-recruitment alternatives and pleiotropic dominant-negative effects. It cannot establish universal dynein coupling across fungal LINC systems. |
| plaque-tether-prep-IPR045119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/; metadata name/type and non-LLM native description | supports | IPR045119 is SUN domain-containing protein 1–5 family, includes Sad1/UNC84 envelope bridge context, and is cross-referenced by Q09825. Family grounding does not establish individual mechanistic experiments. |
| plaque-tether-prep-Q09825 | https://rest.uniprot.org/uniprotkb/Q09825.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry Q09825 matches sad1, Spindle pole body-associated protein sad1, taxon 284812. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-tether-prep-P87245 | https://rest.uniprot.org/uniprotkb/P87245.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry P87245 matches kms1, Karyogamy meiotic segregation protein 1, taxon 284812. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-tether-prep-Q92358 | https://rest.uniprot.org/uniprotkb/Q92358.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry Q92358 matches bqt1, Telomere bouquet protein 1, taxon 284812. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-tether-prep-Q9US52 | https://rest.uniprot.org/uniprotkb/Q9US52.json; entryType, primaryAccession, recommended name, genes, organism; subcellular-location evidence and InterPro cross-references | supports | Fresh reviewed native entry Q9US52 matches bqt2, Telomere bouquet protein 2, taxon 284812. Reference-sequence identity is distinct from exact experimental stock. Native location annotations are database evidence, not an inspected primary experiment. |
| plaque-tether-prep-doi-celldisc.2017.41-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/celldisc.2017.41; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 29123917 10.1038/celldisc.2017.41 The telomere bouquet facilitates meiotic prophase progression and exit in fission yeast.. No whole-body claim from metadata. |
| plaque-tether-prep-doi-j.cub.2012.02.042-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2012.02.042; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 22425159 10.1016/j.cub.2012.02.042 Transient structure associated with the spindle pole body directs meiotic microtubule reorganization in S. pombe.. No whole-body claim from metadata. |
| plaque-tether-prep-doi-j.cub.2005.07.058-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2005.07.058; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 16111942 10.1016/j.cub.2005.07.058 Hrs1p/Mcp6p on the meiotic SPB organizes astral microtubule arrays for oscillatory nuclear movement.. No whole-body claim from metadata. Complete abstract read: Hrs1 loss impairs HAA and movement; ectopic Hrs1 yields HAA-like arrays. Full text and supplements were not inspected. |
| plaque-tether-prep-doi-s41467-025-56049-9-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/s41467-025-56049-9; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 39833200 10.1038/s41467-025-56049-9 Centromere positioning orchestrates telomere bouquet formation and the initiation of meiotic differentiation.. No whole-body claim from metadata. |
| plaque-linc-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990612,GO:0034993,GO:0032200,GO:0032993,GO:0005634,GO:0000228,GO:0000781; All requested term names, definitions, obsoletion, synonym and returned child relation objects | supports | Fresh native GO identities and exact returned relationships inspected for GO:0005634 nucleus, GO:0032993 protein-DNA complex, GO:0000228 nuclear chromosome, GO:1990612 Sad1-Kms1 LINC complex, GO:0000781 chromosome, telomeric region, GO:0032200 telomere organization, GO:0034993 meiotic nuclear membrane microtubule tethering complex. GO0032117 is an array, distinct from GO0034993 tether; GO0034993 has GO1990612 as is_a child. Source-neutral definitions do not establish the appended detailed molecular/taxonomic claims. |
| plaque-linc-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.26508/lsa.202000824%22%20OR%20DOI:%2210.1186/s12915-015-0149-x%22%20OR%20DOI:%2210.1016/j.cub.2020.01.054%22%20OR%20DOI:%2210.1038/s41467-025-56049-9%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 39833200 10.1038/s41467-025-56049-9 Centromere positioning orchestrates telomere bouquet formation and the initiation of meiotic differentiation.; 32967926 10.26508/lsa.202000824 Mps2 links Csm4 and Mps3 to form a telomere-associated LINC complex in budding yeast.; 32059771 10.1016/j.cub.2020.01.054 Extranuclear Structural Components that Mediate Dynamic Chromosome Movements in Yeast Meiosis.; 26058898 10.1186/s12915-015-0149-x Telomere protein Rap1 is a charge resistant scaffolding protein in chromosomal bouquet formation.. No whole-body claim from metadata. |
| plaque-linc-agent-2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.cub.2012.02.042%22&amp;format=json&amp;resultType=core; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 22425159 10.1016/j.cub.2012.02.042 Transient structure associated with the spindle pole body directs meiotic microtubule reorganization in S. pombe.. No whole-body claim from metadata. |
| plaque-linc-agent-chikashige2006-api | https://api.elsevier.com/content/article/pii/S0092867406003187?httpAccept=text/xml; Entire 1953-byte XML response | context_only | Fresh HTTP200 is coredata-only metadata with no article body. It does not extend the Chikashige2006 primary-abstract evidence to Methods or figures; an open-access flag is not itself body retrieval. |
| plaque-linc-agent-fan2020-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC7536833.1/PMC7536833.1.xml; Introduction s1; Results s3–s5, first s6 paragraph and selected next paragraph, full s7–s9; Discussion s10; Methods s12–s18 and displayed main captions. No complete supplementary/raw dataset or image analysis. | partial | Fan2020 directly studies budding-yeast Mps2–Mps3–Csm4, with SK1 meiotic and S288C mitotic experiments. Mps2 depletion/csm4 loss affect Rap1 clustering, delay LYS4 pairing and reduce ARG4/HIS4 conversion; ectopic Csm4/Ndj1 provides mitotic reconstitution. Proposed nonamer and direct cytoskeletal interactions remain models. These are not Sad1–Kms1 experiments. |
| plaque-linc-agent-amelina2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4660835.1/PMC4660835.1.xml; Results Sec5/Sec6 including integrated Figures3/4 captions; Discussion Sec7; Methods Sec10–Sec12. No deposited raw mass spectra reanalysis. | partial | Amelina2015 finds Rap1 DD337AA loses Bqt1/2 interaction and meiotic clustering while preserving other tested interactions. Phosphomimetic/nonphosphorylatable clusters do not support a simple hyperphosphorylation switch. Bqt2-Bqt1 fusion is used in two-hybrid assays; pat1-114 synchronization differs from homothallic live-cell assays. Supports connector function, not detailed stoichiometric or core-LINC removal/reconstitution proof. |
| plaque-linc-agent-yoshida2013-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/PMC3575533.1.xml; Results/discussion first12 paragraphs (telocentrosome recruitment and motor model); Methods Strains/media, Kms2 visualization, zygotic clustering, mat-induced haploid meiosis/MBC, live-cell imaging. | partial | Yoshida2013 observes Kms1/Kms2 at meiotic telocentrosomes and Kms1-dependent Dlc1/Mto1/Alp4 recruitment. Microtubule recovery and motor perturbations support clustering, but detailed cross-linking/transport remains a model and kinesins also contribute. Distinct 25 C zygotic, 30 C haploid-induction and 25–27 C imaging conditions are retained. |
| plaque-linc-agent-swartz2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4142617.1/PMC4142617.1.xml; Results induced site-specific DSBs, Sad1 complexes, Sad1 colocalization, Kms1 promotes gene conversion; Discussion both titled subsections; Methods culture, HO induction and repair-pathway assay. | partial | Swartz2014 supports the exact Sad1–Kms1 DSB-repair identity in S/G2 fission yeast. Loss of Kms1 changes repair-pathway choice while DSB-Sad1 association can persist. No Kms2 increase is detected at MMS foci, but possible redundancy or undetected low-copy roles remain explicit. Figure6 repair mechanisms are proposed. This is separate from meiotic budding-yeast conversion assays. |
| plaque-linc-agent-dsb-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24943839%20OR%20EXT_ID:24947240&amp;format=json&amp;resultType=core&amp;pageSize=100; Returned DOI/PMID/title metadata; abstractText only where explicitly described in this summary | context_only | Identity cross-check: 24947240 10.1016/b978-0-12-397920-9.00004-4 LINC complex proteins in development and disease.; 24943839 10.1091/mbc.e13-10-0569 A role for nuclear envelope-bridging complexes in homology-directed repair.. No whole-body claim from metadata. |
| plaque-adapter-catalogue | https://imodulondb.org/api/datasets; Entire current native catalogue, all organism/dataset keys | context_only | Fresh read-only source fallback lists 20 organisms and 28 datasets, all bacteria/archaea. No Saccharomyces, Schizosaccharomyces or other fungal/eukaryotic matching dataset occurs in this returned catalogue. No matching downstream gene/module search is applicable; absence is not negative biological evidence. This is not execution of the shared adapter runner. |
| plaque-current-0 | data/structures/cytoskeleton/endocytic_patch.yaml; Entire current maintained record at 05425cc7089baf8133399baaf1ec24c00c661de3 | context_only | Full current record read, including components, exact examples, taxonomic/function scope, all graph nodes/edges and history. Unchanged against original frozen target. |
| plaque-current-4 | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml; Entire current maintained record at 05425cc7089baf8133399baaf1ec24c00c661de3 | context_only | Full current record read, including components, exact examples, taxonomic/function scope, all graph nodes/edges and history. Substantively refreshed Bqt1–Bqt2 type change to PROTEIN_COMPLEX and #2420 history; other scientific fields unchanged. |
| plaque-current-5 | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml; Entire current maintained record at 05425cc7089baf8133399baaf1ec24c00c661de3 | context_only | Full current record read, including components, exact examples, taxonomic/function scope, all graph nodes/edges and history. Substantively refreshed Bqt1–Bqt2 type change to PROTEIN_COMPLEX and #2420 history; other scientific fields unchanged. |
| plaque-graph-contract | .claude/skills/curate-causal-graphs/SKILL.md; Scope and completion; native graph rules | context_only | Native policy distinguishes source-bounded causal explanation from membership/function summaries and requires honest uncertainty. |
| plaque-schema | src/cellstructuremech/schema/cellstructuremech.yaml; ComponentTypeEnum, component essentiality and CausalGraphScopeEnum | context_only | PROTEIN_COMPLEX represents named subcomplexes of distinct proteins; assembly necessity differs from viability/function. GENE_OR_PROTEIN graph coverage is not proof of molecular mechanism. |
| plaque-category-context | reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml; F1 exact issue_key, seven affected targets and two assigned Bqt connector fields | context_only | The earlier multi-target finding cytoskeleton-subcomplex-component-types includes these two current Bqt rows. Only their corrected fields were reassessed; this review does not terminally dispose of the whole seven-target predecessor. |
| plaque-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks | context_only | Named genes/proteins trigger actual catalogue applicability review even without an expression-module claim. Unavailable runner execution remains distinct from source fallback. |
| plaque-historical-2420 | https://github.com/CultureBotAI/CellStructureMech/issues/2420; Root-fetched issue JSON body/state and resolution comment reread at current access time | context_only | Issue #2420 is CLOSED and explicitly covers the assigned Bqt component types. Comment identifies prior commit99e590eb. This is historical correction context; no credit to PR2353 and no terminal multi-target scientific disposition. |
| plaque-original-native-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-plaque/original-validation.json; Three native validation/render receipts and fourteen source-input hashes per original | supports | All three originals validate with exit0, render byte-exact Markdown and match all14 historical input hashes each. Two current targets are stale only for the documented component type/history deltas. |
| plaque-native-endocytic_patch-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/endocytic_patch.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/endocytic_patch-uniprot-verify.log; complete root-owned receipt and stdout independently read/hash-verified | supports | Exit0 at exact source head. all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-endocytic_patch-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/endocytic_patch.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/endocytic_patch-uniprot-causal.log; complete root-owned receipt and stdout independently read/hash-verified | supports | Exit0 at exact source head. data/structures/cytoskeleton/endocytic_patch.yaml  (GO:0061645)<br>  endocytic_patch_mechanism	actin	COVERED	-&gt;actin (UniProtKB:P60010)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/meiotic_nuclear_membrane_microtubule_tethering_complex-uniprot-verify.log; complete root-owned receipt and stdout independently read/hash-verified | supports | Exit0 at exact source head. all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/meiotic_nuclear_membrane_microtubule_tethering_complex-uniprot-causal.log; complete root-owned receipt and stdout independently read/hash-verified | supports | Exit0 at exact source head. data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml  (GO:0034993)<br>  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism	sad1_sun_protein	COVERED	-&gt;sad1_sun_protein (UniProtKB:Q09825)<br>  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism	kms1_kash_protein	COVERED	-&gt;kms1_kash_protein (UniProtKB:P87245)<br>  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism	bqt1_bqt2_meiotic_connector	COVERED	-&gt;bqt1_bqt2_meiotic_connector (UniProtKB:Q92358, UniProtKB:Q9US52)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| plaque-native-sad1_kms1_linc_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/sad1_kms1_linc_complex-uniprot-verify.log; complete root-owned receipt and stdout independently read/hash-verified | supports | Exit0 at exact source head. all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-sad1_kms1_linc_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/sad1_kms1_linc_complex-uniprot-causal.log; complete root-owned receipt and stdout independently read/hash-verified | supports | Exit0 at exact source head. data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml  (GO:1990612)<br>  sad1_kms1_linc_complex_mechanism	sad1_sun_protein	COVERED	-&gt;sad1_sun_protein (UniProtKB:Q09825)<br>  sad1_kms1_linc_complex_mechanism	kms1_kash_protein	COVERED	-&gt;kms1_kash_protein (UniProtKB:P87245)<br>  sad1_kms1_linc_complex_mechanism	bqt1_bqt2_meiotic_connector	COVERED	-&gt;bqt1_bqt2_meiotic_connector (UniProtKB:Q92358, UniProtKB:Q9US52)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| micro-record-gamma_tubulin_complex | data/structures/cytoskeleton/gamma_tubulin_complex.yaml; Entire current maintained YAML; definition, components, protein examples, functions, every graph edge and appended curation history. | supports | Personally inspected full current record and original-to-main delta. Target is PROPOSED. Protein additions and grouped component types are reassessed below; no scientific record edit is proposed within this PR. |
| micro-prior-gamma_tubulin_complex | reviews/structured/20261021T094810Z-gamma-tubulin-complex-audit/review.yaml; Original complete review, scientific findings F1 and F2, checks, source inputs, assessments, actions, limitations; paired Markdown roundtrip verified. | supports | Immutable historical needs_curation review has two open findings. Its target hash correctly matches the historical source revision but is stale against current main. Both exact predecessor occurrences are retained in this successor. |
| micro-record-gamma_tubulin_ring_complex | data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml; Entire current maintained YAML; definition, components, protein examples, functions, every graph edge and appended curation history. | supports | Personally inspected full current record and original-to-main delta. Target is PROPOSED. Protein additions and grouped component types are reassessed below; no scientific record edit is proposed within this PR. |
| micro-prior-gamma_tubulin_ring_complex | reviews/structured/20261021T094812Z-gamma-tubulin-ring-complex-audit/review.yaml; Original complete review, scientific findings F1 and F2, checks, source inputs, assessments, actions, limitations; paired Markdown roundtrip verified. | supports | Immutable historical needs_curation review has two open findings. Its target hash correctly matches the historical source revision but is stale against current main. Both exact predecessor occurrences are retained in this successor. |
| micro-record-gamma_tubulin_small_complex | data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml; Entire current maintained YAML; definition, components, protein examples, functions, every graph edge and appended curation history. | supports | Personally inspected full current record and original-to-main delta. Target is PROPOSED. Protein additions and grouped component types are reassessed below; no scientific record edit is proposed within this PR. |
| micro-prior-gamma_tubulin_small_complex | reviews/structured/20261021T094813Z-gamma-tubulin-small-complex-audit/review.yaml; Original complete review, scientific findings F1 and F2, checks, source inputs, assessments, actions, limitations; paired Markdown roundtrip verified. | supports | Immutable historical needs_curation review has two open findings. Its target hash correctly matches the historical source revision but is stale against current main. Both exact predecessor occurrences are retained in this successor. |
| micro-stale-proof | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-microtubule/stale-input-proof.json; All three historical git-show inputs, native frozen hashes, current working bytes and exact current-main bytes. | supports | All three historical hashes match their actual source commit 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. All three current target files equal the current main bytes and differ from those frozen originals. The refresh reassesses the protein, type and evidence deltas rather than replacing hashes alone. |
| micro-original-roundtrip | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-microtubule/original-validation.json; Actual validate and render --content invocations for all three original YAMLs; compare emitted Markdown bytes with committed pairs. | supports | Each native validate exited zero; each native renderer exited zero and reproduced its historical Markdown exactly. A schema/render pass is not a scientific pass. |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks; Evidence Rules; missing-things search contract. | supports | Named genes and UniProt accessions trigger structured-source applicability. Lack of an expression claim is not an exemption. If the runner is unavailable, inspected official source pages are permitted; absence of a matched dataset is not biological negative evidence. |
| micro-config | conf/record_review.yaml; Complete active routes and local rubric list. | supports | Native configuration and profile were read; this is a read-only scientific record review, with issue-bearing batch synthesis owned by the parent reviewer. |
| micro-graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Native graph identity, causal path, membership versus mechanism and scope requirements. | supports | Accession resolution and component_ref coverage do not themselves prove assembly necessity or mechanistic edges. Broad category findings cannot be retired using a partial cohort. |
| micro-native-checklist | .claude/skills/curate-yaml-record/references/review-checklist.md; All field-by-field audit rows and evidence standard. | supports | Component identity, assembly necessity, experimental localization, function and taxonomic distribution are assessed separately. Optional omissions and acknowledged scientific uncertainty do not alone justify findings. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000930,GO:0000931,GO:0008275,GO:0005815,GO:0005816,GO:0032991,GO:0000923,GO:0051418; All eight exact GO id/name/definition/synonym objects and returned parent-child relations. | supports | Active GO:0000930, GO:0000931 and GO:0008275 denote the generic, ring and small complexes respectively. Small and ring are narrower gamma-complex classes; GO:0005815 is an MTOC context and GO:0005816 is fungal SPB. Native definitions support conserved membership and species-dependent complexity, not the appended numerical ring geometry or Mto1 allostery. GO:0000923 and GO:0051418 are equatorial-MTOC and MTOC-mediated nucleation context. |
| micro-taxon-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Exact taxId, scientificName and rank fields. | supports | Eukaryota taxon identity matches; this lookup does not establish universal biological distribution. |
| micro-taxon-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Exact taxId, scientificName and rank fields. | supports | Schizosaccharomyces pombe 972h- reference strain matches. Sequence-example identity is not a claim that the cited experiment used the exact reference stock. |
| micro-taxon-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Exact taxId, scientificName and rank fields. | supports | Schizosaccharomyces pombe species identity matches the ring canonical example. |
| micro-taxon-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName and rank fields. | supports | Saccharomyces cerevisiae S288C reference strain matches new budding-yeast protein examples; literature species context does not itself identify an experimental stock. |
| micro-interpro | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002454/; IPR002454 metadata name/type and description. | supports | IPR002454 is the Gamma tubulin family. An optional family grounding is not invented for the mixed GCP2/GCP3 group, and failure to include an optional family field is not treated as a defect. |
| micro-uniprot-P25295 | https://rest.uniprot.org/uniprotkb/P25295.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | P25295 is reviewed Swiss-Prot Tubulin gamma chain, gene gtb1, taxon 284812. The gtb1/tug1 SPBC32F12.04 entry is gamma tubulin, disambiguated from glucosidase Q9USH8. Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-Q9USH8 | https://rest.uniprot.org/uniprotkb/Q9USH8.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | Q9USH8 is reviewed Swiss-Prot Glucosidase 2 subunit beta, gene gtb1, taxon 284812. This second reviewed gtb1 is ER glucosidase 2 beta, confirming why symbol-only resolution is unsafe. It is not a record component. Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-P53378 | https://rest.uniprot.org/uniprotkb/P53378.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | P53378 is reviewed Swiss-Prot Tubulin gamma chain, gene TUB4, taxon 559292.  Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-Q9Y705 | https://rest.uniprot.org/uniprotkb/Q9Y705.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | Q9Y705 is reviewed Swiss-Prot Spindle pole body component alp4, gene alp4, taxon 284812.  Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-Q9USQ2 | https://rest.uniprot.org/uniprotkb/Q9USQ2.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | Q9USQ2 is reviewed Swiss-Prot Spindle pole body component alp6, gene alp6, taxon 284812. SPB-location evidence explicitly cites ECO:0000269 PMID11080156. Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-P38863 | https://rest.uniprot.org/uniprotkb/P38863.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | P38863 is reviewed Swiss-Prot Spindle pole body component SPC97, gene SPC97, taxon 559292.  Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-P53540 | https://rest.uniprot.org/uniprotkb/P53540.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | P53540 is reviewed Swiss-Prot Spindle pole body component SPC98, gene SPC98, taxon 559292.  Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-Q9P7R5 | https://rest.uniprot.org/uniprotkb/Q9P7R5.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | Q9P7R5 is reviewed Swiss-Prot Gamma-tubulin complex component gfh1, gene gfh1, taxon 284812. SPB-location provenance cites ECO:0000269 PMID15004232 and PMID16823372. Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-Q9UT52 | https://rest.uniprot.org/uniprotkb/Q9UT52.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | Q9UT52 is reviewed Swiss-Prot Gamma-tubulin complex subunit mod21, gene mod21, taxon 284812. SPB-location provenance cites ECO:0000269 PMID16823372 and PMID17021256. Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-P87244 | https://rest.uniprot.org/uniprotkb/P87244.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | P87244 is reviewed Swiss-Prot Spindle pole body component alp16, gene alp16, taxon 284812. SPB-location provenance cites ECO:0000269 PMID12134075. Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-O94488 | https://rest.uniprot.org/uniprotkb/O94488.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | O94488 is reviewed Swiss-Prot Gamma tubulin complex adapter mto1, gene mto1, taxon 284812.  Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-uniprot-Q9USP7 | https://rest.uniprot.org/uniprotkb/Q9USP7.json; primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location evidence references. | supports | Q9USP7 is reviewed Swiss-Prot Gamma tubulin complex adapter mto2, gene mto2, taxon 284812.  Identity/annotation provenance is distinguished from direct evidence of structural membership, stoichiometry or assembly necessity. |
| micro-named-proteins-284812 | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28organism_id%3A284812%29+AND+%28gene_exact%3Agtb1+OR+gene_exact%3Aalp4+OR+gene_exact%3Aalp6+OR+gene_exact%3Agfh1+OR+gene_exact%3Amod21+OR+gene_exact%3Aalp16+OR+gene_exact%3Amzt1+OR+gene_exact%3Amto1+OR+gene_exact%3Amto2%29&amp;format=json&amp;size=500; Every returned entry accession, own primary gene/synonyms/locus and source taxon; response total and pagination headers. | supports | All nine named fission-yeast symbol classes are represented within eleven reviewed results, including two distinct gtb1 and two mto1 entries. Existing declared O94488/P25295 identities are checked by full entries rather than picking a homonym. |
| micro-named-proteins-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28organism_id%3A559292%29+AND+%28gene_exact%3ATUB4+OR+gene_exact%3ASPC97+OR+gene_exact%3ASPC98%29&amp;format=json&amp;size=500; Every returned entry accession, own primary gene/synonyms/locus and source taxon; response total and pagination headers. | supports | The bounded budding-yeast query returns exactly P53378/TUB4, P38863/SPC97 and P53540/SPC98, supporting the record’s reviewed-accession identity claims at this query scope. |
| micro-new-europepmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;pageSize=100&amp;query=EXT_ID%3A11080156+OR+EXT_ID%3A15004232+OR+EXT_ID%3A16823372+OR+EXT_ID%3A17021256+OR+EXT_ID%3A12134075+OR+EXT_ID%3A15068790+OR+DOI%3A%2210.1146%2Fannurev.cellbio.20.022003.114106%22; Seven exact matching results: PMID11080156/15004232/16823372/17021256/12134075/15068790 and Jaspersen/Winey DOI, including titles, author lists and abstractText. | supports | The new PMID citations resolve to Vardy/Toda2000, Venkatram2004, Matsuyama2006, Anders2006 and Fujita2002. Matsuyama ORFeome survey and Zimmerman2004 are credited only at metadata/abstract tier in this review; no individual image, ORFeome table or full Zimmerman body was inspected. Jaspersen/Winey2004 is a secondary review, with separately inspected browser text. |
| micro-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Introduction P2–P3, Results integrative SPB-core representation P27–P28 and final composition P38; title/DOI/PMID. | supports | Viswanath2017 DOI10.1091/mbc.E17-06-0397 studies S. cerevisiae SPB core architecture involving Spc42, Spc29, Spc110, Cnm67 and Cmd1. Its Tub4 context does not establish fission-yeast Alp4/Alp6 composition or Mto1/Mto2-driven nucleation. This directly confirms the retained source-organism attribution defect. |
| micro-samejima2010 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2989437.1/PMC2989437.1.xml; Results MASC-targeting mutants P3–P8, Myp2/Alp4 eMTOC observations P8–P10, Sid4/Cdc11 P11–P15; Figure 1/3/4 captions. | supports | Primary S. pombe targeting experiments separate interphase/mitotic SPBs and equatorial MTOCs; Myp2 loss removes detected equatorial Alp4 and PAA nucleation. Recruitment and site-specific nucleation support the existing Alp4/Mto1 roles, with experimental context retained. The study does not establish 13/14-spoke ring geometry, a GCP4/5/6 seam or Mto1 allosteric ring closure. |
| micro-samejima2008 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2743986.1/PMC2743986.1.xml; Results CM1 binding P5–P12; Mto1-334 and Mto2 deletion P15–P20; Discussion P23. | supports | CM1 mutants lose gamma-complex interaction without losing prospective-MTOC localization. Mto1-334 and mto2 deletion retain restricted SPB and very limited eMTOC nucleation; more sensitive detection reveals weak association. These are recruitment/interaction/activity endpoints rather than class-wide assembly-necessity measurements. |
| micro-lynch2014 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3989768.1/PMC3989768.1.xml; Results minimal Mto1/2-bonsai activation and copy numbers P7–P15; Conclusions P16. | supports | Fission-yeast bonsai complexes activate nucleation independently of targeting, with measured average Mto1/Mto2 and Alp4/Alp6 copy numbers supporting a gamma-TuRC-like inference. Mto2-dependent multimerization matters. The authors explicitly leave conformational activation unconfirmed and do not determine whether Mto1 CM1 alone activates; these data do not validate the record’s affirmative allosteric ring mechanism. |
| micro-brilot2021 | https://pmc-oa-opendata.s3.amazonaws.com/PMC8099430.1/PMC8099430.1.xml; Introduction P3–P7 as cited context; primary cryo-EM/crystallography/XL-MS Results P20–P22 and P37–P42; CM1/Spc110 interfaces. | supports | Direct budding-yeast structures distinguish gamma-TuSC assembly states and resolve Spc110 contacts, including CM1 across an inter-TuSC interface. Species, recombinant/engineered preparation and open/closed state are essential bounds. Background metazoan ring comparisons are not new experiments on native S. pombe Gfh1/Mod21/Alp16. |
| micro-lyon2016 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4945142.1/PMC4945142.1.xml; Introduction P0–P1; Discussion P27–P28; primary study of Spc110 oligomerization and gamma-TuRC assembly. | supports | Budding-yeast Spc110-dependent oligomerization and assembly are supported. The 13-position description involves seven TuSCs with half-TuSC overlap, and recruited versus assembled complexes must be separated. Background Spc72 homology is not direct evidence for identical receptor-dependent geometry throughout fungi. |
| micro-bellingham2023 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/PMC10047812.1.xml; Results P4–P7, Figure 1 timing, relative localization/intensity and PAA network; Methods/context. | supports | Live fission-yeast experiments support Myp2 then Mto1 then PAA recruitment timing. Mto1 enrichment inside Myp2 and the dosage experiment limit a simple direct-complex model. The source studies PAA organization/cytokinesis rather than gamma-ring molecular geometry. Figure captions/body were read; pixels were not independently reanalyzed. |
| micro-florparra2018 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7263743.1/PMC7263743.1.xml; Abstract, Introduction P0–P4 and Results nucleation assays, Mto1-bonsai and Alp14/Alp7 recruitment context. | supports | Flor-Parra2018 separates Alp14-promoted nucleation from polymerization, including interphase Mto1-bonsai and recruitment assays. This is appropriate nucleation context but does not establish the asserted GCP4/5/6 seam or Mto1 allostery. |
| micro-masuda2013 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3771951.1/PMC3771951.1.xml; Results Mzt1 membership/localization and core pull-down P30–P31, Figure 8; Discussion. | supports | Fission-yeast Mzt1 membership and MTOC recruitment are supported. Conditional mzt1 mutants at 36 C retain Alp4–gamma-tubulin core association despite localization defects. This separates core assembly from recruitment; it does not establish full native ring assembly or universal assembly-essentiality labels. |
| micro-samejima2005 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1142446/?pdf=render; Title/DOI; Results P35–P36, P45, P47, P51–P58; Discussion P64–P67. | supports | DOI10.1091/mbc.E04-11-1003 is Samejima et al.2005, a study of Mto2/Mto1 interaction, recruitment and residual PAA activity. The body explicitly presents a possible allosteric role as speculation. It does not characterize Gfh1/Mod21/Alp16 as a 14-spoke seam. Source identity is taken from the paper, not from an old retrieval filename. |
| micro-venkatram2005 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1142447/?pdf=render; Results P33, P39, P43, P46–P47; Discussion P50 and P56–P57. | supports | Distinct DOI10.1091/mbc.E04-12-1043 reports stronger eMTOC/PAA defects and actin-ring anchoring during cps1 arrest or low-dose LatA cytokinesis delay. These preparation-specific results are retained alongside Samejima’s residual activity, rather than used to erase it or infer universal ring-assembly necessity. |
| micro-anders2006 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1679674/?pdf=render; Results P26–P33 and Figure 2 Mod21/Gfh1 association/localization; sucrose-gradient analysis P72–P78, Discussion. | supports | Mod21 is a bona fide fission-yeast gamma-complex member with Alp4/Alp6 coassociation and SPB/eMTOC localization. Gfh1/Mod21/Alp16 are facultative noncore proteins affecting nucleation efficiency. Sedimentation and association depend on preparation and leave native large-complex architecture uncertain; they do not reconstruct a 14-spoke seam. |
| micro-pmid-11080156 | https://pmc.ncbi.nlm.nih.gov/articles/PMC305819/?pdf=render; Vardy/Toda2000 Results P20 and P22–P26, Figure 1/2. | supports | GFP and HA-tagged Alp4/Alp6 localize to SPB/equatorial MTOC and coimmunoprecipitate Gtb1 in S. pombe. This directly supports the new Alp6 localization citation, separately from UniProt’s ECO annotation; mutant phenotypes do not by themselves establish class-wide assembly necessity. |
| micro-pmid-15004232 | https://pmc.ncbi.nlm.nih.gov/articles/PMC404023/?pdf=render; Venkatram2004 Results P23/P29 complex purification and P37–P38 GFP-Gfh1 localization. | supports | Alp4/Alp6-TAP purification and mass spectrometry identify Gfh1/Mbo1; follow-up coimmunoprecipitation supports association. Gfh1 expressed under the low-strength nmt81 promoter localizes to SPB and faint medial eMTOC. This preparation supports the added Gfh1 citation without proving exact native ring geometry. |
| micro-pmid-12134075 | https://pmc.ncbi.nlm.nih.gov/articles/PMC117319/?pdf=render; Fujita2002 Results P30/P35 homology, P39–P44 interaction/fractionation/localization, Figure 4/5. | supports | Alp16 is related to GCP6, coimmunoprecipitates gamma tubulin and localizes to SPB/equatorial MTOC. Lower abundance required antibody-enhanced detection. Large-complex fractionation and variable stoichiometry are preparation-dependent, not a 14-spoke structural determination; viability, complex assembly and nucleation are separate endpoints. |
| micro-jaspersen-secondary | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-uploaded manuscript browser rendering, pages 24–26, lines 978–1067; especially 1004–1022 and 1042–1051. | context_only | Secondary review supports budding-yeast Tub4/Spc97/Spc98 2:1:1 composition and attachment via Spc110 versus Spc72. It describes a recombinant small complex with low nucleation activity and treats capping as likely. Newly accessed browser rendering is cache-mediated (reported crawl three weeks earlier), with no HTTP-status receipt; it is not primary experimental evidence or an exact S288C stock verification. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Complete returned 20 organism records and 28 dataset keys. | supports | The inspected official iModulonDB catalogue has no Schizosaccharomyces, Saccharomyces or other eukaryotic organism dataset. Named-gene applicability was assessed, but no target organism match permits a downstream gene/module search or summarize call. This is a catalogue-bounded not-applicable result, not evidence that gamma complexes or their genes are absent. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual prior runner receipt, started_at/finished_at, exit_code and PermissionError. | context_only | Earlier runner invocation at 2026-11-03T00:49:00Z failed with OS PermissionError for pyvenv.cfg. It is retained as historical unavailability, not a new execution or a passed adapter command. The fresh official catalogue response supplies fallback applicability evidence. |
| micro-native-gamma_tubulin_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-verify-receipt.json | supports | Actual native command exited zero on the declared current head. All declared protein example and graph xref identities verified; this does not validate membership, stoichiometry or scientific mechanism. |
| micro-native-gamma_tubulin_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-causal-receipt.json | supports | Actual native command exited zero on the declared current head. Both GENE_OR_PROTEIN causal nodes are COVERED by component examples; zero partial, missing-symbol, dangling or unanchored nodes in this diagnostic. This covers that node class only and is not a proof that the graph is mechanistic. |
| micro-native-gamma_tubulin_ring_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-verify-receipt.json | supports | Actual native command exited zero on the declared current head. All declared protein example and graph xref identities verified; this does not validate membership, stoichiometry or scientific mechanism. |
| micro-native-gamma_tubulin_ring_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-causal-receipt.json | supports | Actual native command exited zero on the declared current head. Both GENE_OR_PROTEIN causal nodes are COVERED by component examples; zero partial, missing-symbol, dangling or unanchored nodes in this diagnostic. This covers that node class only and is not a proof that the graph is mechanistic. |
| micro-native-gamma_tubulin_small_complex-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-verify.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-verify-receipt.json | supports | Actual native command exited zero on the declared current head. All declared protein example and graph xref identities verified; this does not validate membership, stoichiometry or scientific mechanism. |
| micro-native-gamma_tubulin_small_complex-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-causal.log; receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-causal-receipt.json | supports | Actual native command exited zero on the declared current head. Both GENE_OR_PROTEIN causal nodes are COVERED by component examples; zero partial, missing-symbol, dangling or unanchored nodes in this diagnostic. This covers that node class only and is not a proof that the graph is mechanistic. |
| micro-category-20261023 | reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml; Exact F1 occurrence, issue_key, affected targets and component paths; bounded gamma-target comparison. | supports | Category predecessor includes gamma targets plus out-of-slice records. The current gamma component types are corrected, but this three-record slice does not reassess every affected target and therefore makes no terminal disposition of the whole category finding. |
| micro-category-20261025 | reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.yaml; Exact F1 occurrence, issue_key, affected targets and component paths; bounded gamma-target comparison. | supports | Category predecessor includes gamma targets plus out-of-slice records. The current gamma component types are corrected, but this three-record slice does not reassess every affected target and therefore makes no terminal disposition of the whole category finding. |
| micro-issue-2420 | https://github.com/CultureBotAI/CellStructureMech/issues/2420; Parent-fetched issue JSON body/state and any returned comments; inspected at current review time. Snapshot is tracker context, not an authority for scientific claims. | context_only | Closed historical tracking context. Current gamma grouped components are PROTEIN_COMPLEX, consistent with the recorded scoped repair. No claim is made that all targets of this broader issue were newly reviewed here. |
| micro-issue-2431 | https://github.com/CultureBotAI/CellStructureMech/issues/2431; Parent-fetched issue JSON body/state and any returned comments; inspected at current review time. Snapshot is tracker context, not an authority for scientific claims. | context_only | Closed historical tracking context. Current gamma grouped components are PROTEIN_COMPLEX, consistent with the recorded scoped repair. No claim is made that all targets of this broader issue were newly reviewed here. |
| micro-issue-2470 | https://github.com/CultureBotAI/CellStructureMech/issues/2470; Parent-fetched issue JSON body/state and any returned comments; inspected at current review time. Snapshot is tracker context, not an authority for scientific claims. | context_only | Closed historical tracking context. The added Jaspersen/Winey evidence is present for budding-yeast Spc97/Spc98. The issue body itself incorrectly calls Viswanath2017 a fission-yeast study; that wording is preserved as a limitation and does not establish that current source attribution is correct. |
| septin-septin-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031105,GO:0032156,GO:0032158,GO:0032160,GO:0032161,GO:0032165,GO:0032166; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-tax-5476 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-P32457 | https://rest.uniprot.org/uniprotkb/P32457.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-query-CDC3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-P25342 | https://rest.uniprot.org/uniprotkb/P25342.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-query-CDC10 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC10%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-P32458 | https://rest.uniprot.org/uniprotkb/P32458.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-query-CDC11 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC11%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-P32468 | https://rest.uniprot.org/uniprotkb/P32468.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-query-CDC12 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC12%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-Q07657 | https://rest.uniprot.org/uniprotkb/Q07657.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-query-SHS1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ASHS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-IPR016491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-septin-agent-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14562095%20AND%20SRC%3AMED; Fresh Europe PMC exact PMID primary abstract and native UniProt location citation fields only. | supports | Huh2003 chromosomal GFP localization screen supports the source identity and cited native annotation; individual original image panels and full strain Methods not audited. |
| septin-septin-agent-pmid-25971666 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A25971666%20AND%20SRC%3AMED; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-pmid-9790978 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9790978%20AND%20SRC%3AMED; Fresh Europe PMC exact PMID primary abstract and native UniProt location citation fields only. | supports | Mino1998 abstract reports Shs1 bud-neck localization and Spa2 binding. The abstract does not supply a universal structural inventory or complete assembly necessity assay. |
| septin-septin-agent-versele2005-correct-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16009555%20AND%20SRC%3AMED; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-douglas2005-correct-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16151244%20AND%20SRC%3AMED; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-septin-agent-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; Fresh native PMC secondary review HTML: Introduction/green-algal ortholog paragraph, septin complex overview and budding/fission yeast function/scaffold/barrier passages; no cited primary experiment or image reanalysis. | supports | Green-algal septin ortholog occurrence does not establish the expanded plasma-membrane cortical architecture and recruitment functions across the full taxon/site list. Historical models are context, not fixed current rod stoichiometry. The five-gene list is interpreted as examples, not an ordered rod. |
| septin-septin-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; Fresh native PMC secondary review HTML: introduction and septin-family overview, sporulation/prospore-wall paragraph, and Aspergillus nidulans subsection including developmental localization and scaffold proposals. | supports | Spore-wall recruitment is proposed, and A. nidulans developmental scaffold/regulator recruitment is suggested from scoped phenotypes. These are not demonstrated cross-taxon universal mechanisms; broad septin cytoskeleton is not confined to its spore-array examples. |
| septin-septin-agent-finnigan2015-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC4512547/?pdf=render; Fresh native PMC primary HTML: abstract, relevant strain-construction Methods/Table1 context, Bni5 recruitment and subsequent Myo1 localization Results with Figure7 caption, and relevant CTE-binding Discussion passage. No full-body, supplement or image-pixel audit. | supports | Vegetative S. cerevisiae Cdc11/Shs1 C-terminal contributions to Bni5/Myo1 recruitment are directly studied. Deletion/truncation, tagged-strain effects and recruitment readouts retain their bounds; not all-species architecture or complete septin-class assembly necessity. |
| septin-spindle-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000922,GO:0005818,GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0015630,GO:0043232,GO:0051233,GO:0072686; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-doi-annurev.cellbio.20.022003.114106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev.cellbio.20.022003.114106; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-spindle-agent-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Fresh native PMC JATS primary paper: claim-bearing Introduction and complete Figure1 caption on yeast SPB architecture and modeling context; full Results/Methods not audited. | supports | Inner/outer plaques, anchored gamma-TuSC and the yeast core are supported as source context. Introductory citations and integrative-model context do not independently prove the combined molecular mechanism throughout eukaryotes. |
| septin-spindle-agent-P09733 | https://rest.uniprot.org/uniprotkb/P09733.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-query-TUB1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-spindle-agent-P02557 | https://rest.uniprot.org/uniprotkb/P02557.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-query-TUB2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-spindle-agent-P09734 | https://rest.uniprot.org/uniprotkb/P09734.json; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-query-TUB3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-spindle-agent-doi-jcb.129.6.1601 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.129.6.1601; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-spindle-agent-doi-science.277.5325.574 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.277.5325.574; Fresh Europe PMC exact DOI primary abstract and bibliographic metadata only. | supports | Straight1997 abstract directly reports GFP-Tub1 spindle imaging, chromosomal loci tracking and biphasic dynamics. No current publisher attempt, full-body retrieval or detailed midzone-regulator assay is claimed. |
| septin-spindle-agent-pmid-11739794 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11739794%20AND%20SRC%3AMED; Fresh Europe PMC exact PMID primary abstract and native UniProt attribution cross-check; not full body. | supports | Anders/Botstein2001 studies yeast alpha-tubulin mutations and microtubule dynamics. Localization citation identity agrees; mutant effects do not prove each example is independently necessary for spindle assembly. |
| septin-spindle-agent-pmid-23001566 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A23001566%20AND%20SRC%3AMED; Fresh Europe PMC exact PMID primary abstract and native UniProt attribution cross-check; not full body. | supports | Cederquist2012 explicitly includes yeast genetics despite the human-disease title. Native P02557 cytoskeleton annotation cites it; this is not a taxon-mismatch finding or proof of every-region occupancy. |
| septin-spindle-agent-IPR000217 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-spindle-agent-winey1995-pdf | https://pdfs.semanticscholar.org/cb33/a9630ccea6fbdd5e23d396df29c214465892.pdf; Fresh genuine primary PDF: abstract/Introduction, strain and EM preparation Methods, claim-bearing overlap/core-bundle Results and Figures5–6/12–13 captions, crossbridge Results and beginning of Discussion, pp1601–1602,1606–1607,1609,1611–1612. Not complete main-body, TableI, raw micrograph or image-pixel reanalysis. | supports | S288c and S288c-background diploid nuclear spindles were reconstructed from serial EM. The paper explicitly separates astral microtubules from spindle per se. It shows overlap/interdigitation and crossbridges without molecularly identifying Ase1/PRC1 or proving the appended broad regulator mechanism. Inferred kinetochore/interpolar assignments are not all directly demonstrated. |
| septin-midzone-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0051233,GO:0072686,GO:0110165; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-pole-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000226,GO:0000922,GO:0000930,GO:0005815,GO:0005816,GO:0005819,GO:0051225,GO:0110165; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-pole-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Fresh native issuing-authority response: exact identifier/name, definitions, family hierarchy, taxon/strain and returned evidence annotation fields. | supports | Identifier/authority annotations verified within their returned scope; no independent experimental membership or assembly necessity follows solely from accession identity. |
| septin-pole-agent-doi-mbc.E17-06-0397 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E17-06-0397; Exact request URL and returned bibliographic metadata/available abstract or reviewed gene-query results. | supports | Only returned source identity/abstract or gene match is assessed; metadata is not body inspection and a bounded query is not an exhaustive absence search. |
| septin-current-adapter-catalogue | https://imodulondb.org/api/datasets; Entire current official /api/datasets response: all20organism objects and28dataset keys inspected. | supports | No matching fungal, algal or protist dataset occurs in the returned catalogue. Downstream matched gene/module requests are inapplicable; no unrelated bacterial dataset is substituted and no biological absence is inferred. |
| septin-spindle-agent-jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Fresh browser-indexed author-uploaded secondary review, declared crawl age three weeks; Introduction/core organization displayed lines185–410. Native HTTP request returned403. | supports | Yeast SPB organization and structural layers provide review-tier context, not all-eukaryote primary evidence. |
| septin-spindle-agent-jaspersen-duplication-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Fresh browser-indexed author-uploaded secondary review: duplication and separation displayed lines619–800; no native full-text download. | supports | Budding-yeast bridge cleavage and Cin8/Kip1 separation are scoped mechanisms. No uniform pole-duplication pathway throughout microbial eukaryotes is established. |
| septin-spindle-agent-jaspersen-nucleation-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Fresh browser-indexed author-uploaded secondary review: nucleation displayed lines976–1077 and SPB/centrosome comparison1213–1308; no full-review read claimed. | supports | Tub4/Spc97/Spc98 and Spc110/Spc72 are yeast nucleation context. Centrosome comparisons explicitly preserve differences; capping and some regulatory mechanisms are model or uncertainty-qualified. |
| septin-record-septin_cytoskeleton | data/structures/cytoskeleton/septin_cytoskeleton.yaml; Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all definitions, fields, examples, provenance and graph nodes/edges. | supports | Current SHA equals original frozen target and original source revision. Whole-record scientific reassessment performed; no record edit. |
| septin-record-spindle | data/structures/cytoskeleton/spindle.yaml; Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all definitions, fields, examples, provenance and graph nodes/edges. | supports | Current SHA equals original frozen target and original source revision. Whole-record scientific reassessment performed; no record edit. |
| septin-record-spindle_midzone | data/structures/cytoskeleton/spindle_midzone.yaml; Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all definitions, fields, examples, provenance and graph nodes/edges. | supports | Current SHA equals original frozen target and original source revision. Whole-record scientific reassessment performed; no record edit. |
| septin-record-spindle_pole | data/structures/cytoskeleton/spindle_pole.yaml; Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all definitions, fields, examples, provenance and graph nodes/edges. | supports | Current SHA equals original frozen target and original source revision. Whole-record scientific reassessment performed; no record edit. |
| septin-policy | docs/CURATION.md; Current frozen relevant policy passages. | supports | Evidence scope, grounded identity and distinct assembly-necessity endpoints govern scientific conclusions. |
| septin-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; Current frozen relevant policy passages. | supports | Named gene/protein/regulator claims trigger adapter applicability. Unavailable runner permits source fallback; no covered dataset means downstream N/A, not biological absence. |
| septin-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Current frozen relevant policy passages. | supports | Graph scope must match the represented causal transitions; topology alone is not mechanistic explanation. |
| septin-graph-contract | .claude/skills/add-cell-structure/SKILL.md; Current frozen relevant policy passages. | supports | Source-backed causal mechanism and supported structural/function summary remain distinct; no compulsory atomistic graph or protein census. |
| septin-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-septin/original-checks.json; Four original native validate/render runs and current/frozen/original-source hashes. | supports | All four validate and render exits0; committed Markdown matches native render exactly; all four target hashes unchanged. Historical full-corpus checks are not current CI. |
| septin-native-septin_cytoskeleton-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/septin_cytoskeleton-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/septin_cytoskeleton.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. Declared protein examples and xrefs verified. |
| septin-native-septin_cytoskeleton-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/septin_cytoskeleton-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/septin_cytoskeleton.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. One COVERED GENE_OR_PROTEIN node, no missing-symbol/dangling reference; this is declared inventory coverage, not every species/paralog or mechanism. |
| septin-native-spindle-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/spindle.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. Declared protein examples and xrefs verified. |
| septin-native-spindle-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/spindle.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. One COVERED GENE_OR_PROTEIN node, no missing-symbol/dangling reference; this is declared inventory coverage, not every species/paralog or mechanism. |
| septin-native-spindle_midzone-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_midzone-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/spindle_midzone.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. Declared protein examples and xrefs verified. |
| septin-native-spindle_midzone-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_midzone-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/spindle_midzone.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. One COVERED GENE_OR_PROTEIN node, no missing-symbol/dangling reference; this is declared inventory coverage, not every species/paralog or mechanism. |
| septin-native-spindle_pole-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_pole-uniprot-verify-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/spindle_pole.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. Empty exact-protein inventory and zero GENE_OR_PROTEIN graph nodes; no molecular claim validated by empty scope. |
| septin-native-spindle_pole-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_pole-uniprot-causal-receipt.json; Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/spindle_pole.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read and hash verified. | supports | Exit0. Empty exact-protein inventory and zero GENE_OR_PROTEIN graph nodes; no molecular claim validated by empty scope. |
| septin-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical canary attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z, exit1 PermissionError reading pyvenv.cfg; no fresh invocation. | supports | Historical OS unavailability is separate from fresh official catalogue fallback. No runner success, current execution, or downstream unrelated-dataset query is claimed. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2353 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Endocytic patch and two meiotic tether/LINC complexes independent subreview: Chikashige2006 remains primary-abstract-only: fresh API200 is coredata-only; browser publisher retrieval403 and Citeseer timeout yielded no body. These are route-specific access limits, not global unavailability. Tanaka2005, Kaksonen2003, Boldogh2001 and Winter1997 are metadata/abstract or native-annotation evidence only.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: All retained external source snapshots were freshly retrieved for this PR; actual per-source UTC fetch times and SHA256 are preserved. No cached response is restamped. Source locators distinguish primary direct experiments from introductory background and database annotation.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: No figure-pixel, raw movie, raw mass-spectrum or complete supplementary experimental-stock reanalysis was performed. Funaya and Galletta are freshly read only at named sections; Aghamohammadzadeh main paragraphs were read without supplemental Methods. No record image asset is present in these three targets.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: Only the explicit conventional-actin family candidate IPR004000 was evaluated; no exhaustive exact-family absence claim is made. Missing optional component inventories, properties or images do not generate findings.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: Core assembly necessity and the connector CONDITIONAL assembly interpretation remain unknown; phenotypic function/viability and bouquet attachment are distinct. Kms2 context does not imply fixed stoichiometry or universal absence.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: Existing #2420 is historical scoped context. This three-record review does not terminally resolve the seven-target category finding, other category findings or any record-curation issue; no records were edited.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: The shared structured-source runner failure is historical and unavailable execution; the fresh source catalogue supports the present no-matching-fungal-dataset applicability determination. No downstream expression-module evidence is claimed.
- Endocytic patch and two meiotic tether/LINC complexes independent subreview: Root owns full-corpus gates, final-head CI and publication decisions; the six current protein receipt checks here do not stand in for those gates.
- Three gamma-tubulin complexes independent subreview: Three-target slice only. No global category resolution: the October23 and October25 F1 predecessors also affect targets outside this slice. Current gamma type repairs are positively assessed without retiring those whole findings.
- Three gamma-tubulin complexes independent subreview: Jaspersen/Winey2004 is secondary context, freshly accessed through a browser cache-mediated author manuscript rendering with no HTTP-status receipt. Its source crawl age is separate from the actual current access time. No secondary review is treated as direct mechanistic experiment.
- Three gamma-tubulin complexes independent subreview: Matsuyama2006 ORFeome survey and Zimmerman2004 are limited to native metadata/abstract and exact UniProt annotation provenance where applicable. Individual ORFeome localization images/tables and Zimmerman full text were not inspected. Fresh primary bodies for Alp6/Gfh1/Alp16 and Mod21 were inspected separately.
- Three gamma-tubulin complexes independent subreview: S3 routes for Samejima2005, Venkatram2005, Anders2006 and the three new primary articles returned404. Successful fresh PMC HTML responses then supplied body text. A failed route is not global source unavailability. An optional BeautifulSoup extraction attempt lacked that module; a standard-library HTML parser successfully extracted the returned bodies. This was not a failed repository validator.
- Three gamma-tubulin complexes independent subreview: No microscopy pixels, movies, deposited structural coordinates or supplements were independently reanalyzed. Body methods/results and specified captions were inspected. There are no target-owned image assets to verify.
- Three gamma-tubulin complexes independent subreview: Exact complete-ring assembly necessity and universal cross-eukaryote distribution remain bounded uncertainties. Membership, sequence identity, viability, localization and nucleation activity are not interchangeable.
- Three gamma-tubulin complexes independent subreview: Historical runner unavailability is retained with its original00:49Z time, not represented as a new command. The fresh official catalogue has no target organism match; no gene/module query or summary was manufactured for unmatched organisms.
- Three gamma-tubulin complexes independent subreview: Closed issue #2470 is tracker context only and itself incorrectly calls Viswanath2017 fission yeast. Current source assessment explicitly corrects that interpretation; the issue closure does not establish current scientific correctness.
- Three gamma-tubulin complexes independent subreview: The native protein checks are current root-run receipts inspected here. Global QC, identifiers, CI and merge state remain parent-owned and are not independently rerun or certified by this slice.
- Three gamma-tubulin complexes independent subreview: Common rubric/schema/verifier inputs are byte-identical to those personally read in the prior PR2352 review; current frozen hashes were rechecked and the active review/config/profile and graph checklist passages were reread. No extra maintained neighbor record was used.
- Septin cytoskeleton and three spindle regions independent subreview: Current reassessment is independent and read-only; original frozen bytes and historical source/check receipts remain immutable. All four assigned scientific targets are unchanged. No historical observation is relabeled as a current action.
- Septin cytoskeleton and three spindle regions independent subreview: Versele2005 and Douglas2005 are secondary reviews, freshly read at specified Introduction/function, sporulation and Aspergillus passages. Their prior hypotheses, historical assembly models and taxon occurrence are not new primary experimental proof.
- Septin cytoskeleton and three spindle regions independent subreview: Finnigan2015 fresh primary HTML was read at the stated abstract, strain-construction, recruitment Results/caption and Discussion passages, not the entire body, supplement, figure pixels or raw microscopy. Huh2003 and Mino1998 remain primary abstract plus native-annotation attribution checks.
- Septin cytoskeleton and three spindle regions independent subreview: Jaspersen/Winey2004 is secondary author-manuscript browser text, freshly accessed with a reported three-week crawl age. Native request returned403; no native full-text or complete review read. The stated displayed Introduction, duplication/separation, nucleation and centrosome-comparison passages were inspected.
- Septin cytoskeleton and three spindle regions independent subreview: Viswanath2017 is used at native primary Introduction/Figure1 context only; no complete Results/Methods audit or independent proof for every introductory citation. Broad eukaryote mechanisms remain outside that yeast-core evidence.
- Septin cytoskeleton and three spindle regions independent subreview: Winey1995 genuine PDF was read at specified claim-bearing Methods/Results/caption and Discussion passages, not all main text, TableI, images or raw EM. Morphological kinetochore/interpolar assignments retain their inferential status; observed crossbridges have no demonstrated molecular identity in these passages. Regional overlap does not imply every entire spindle microtubule lies within the midzone.
- Septin cytoskeleton and three spindle regions independent subreview: Straight1997, Anders2001 and Cederquist2012 remain fresh exact primary abstract/metadata plus applicable UniProt attribution checks. No fresh publisher failure or full-body search is invented. The human-disease title of Cederquist does not negate its explicit yeast genetics.
- Septin cytoskeleton and three spindle regions independent subreview: Assembly necessity remains unknown for collective septins, combined alpha/beta tubulin and generic polar components. Neither defining material, native identity, intact structure, individual mutant phenotype nor cell viability establishes the required formation endpoint across every taxon. These unknowns are not fabricated extra issues.
- Septin cytoskeleton and three spindle regions independent subreview: Native protein commands verify the declared examples: septin cytoskeleton and spindle/midzone each have one COVERED graph node; spindle pole has an empty exact-protein inventory and zero GENE_OR_PROTEIN nodes. Empty scope is not successful proof of its named molecular mechanism.
- Septin cytoskeleton and three spindle regions independent subreview: Fresh catalogue covers only returned20organisms/28datasets; no matching eukaryote means downstream source non-applicability, not biological absence. Historical00:49Z runner receipt is retained without a new invocation.
- Septin cytoskeleton and three spindle regions independent subreview: Root owns globalQC, issue deduplication/publication andCI. Generic-septin finding matches #2499 in class and can be added with its exact record/predecessor scope; no issue mutation was performed by this reviewer.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Every inherited finding is reassessed against current sources and retains exact predecessor identity.
- Bundle issues #2574 (five stale reviews) and #2575 (ten structured-source applicability defects) are addressed here. Scientific record-curation findings remain separately tracked. Existing validator #2514 remains open.
- Already-closed #2420, #2431 and #2470 are historical context for earlier record corrections. Their multi-target findings are not terminally superseded by a partial cohort; this review assesses only its current target-specific changes.
- Source commit 05425cc7089baf8133399baaf1ec24c00c661de3 is retained by tag review-base/pr2353-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration, graph/protein policies, the verifier source and two prior category-review pairs.
- Seven original bundles omit structured-source applicability. Endocytic patch, meiotic nuclear membrane microtubule tethering complex and Sad1-Kms1 contain unsupported exemptions based on absence of expression/module claims.
- Fresh source inspection and retained responses use their actual access dates. Primary and secondary sources, abstracts, claim-bearing body sections, captions and any inspected pixels retain distinct scopes.
- The native spindle-pole protein verification has an empty inventory and its graph contains zero GENE_OR_PROTEIN nodes. Exit zero does not validate molecular mechanisms named only in prose.
- All24 current scientific finding keys are linked to #2499 and #2576–#2598. They preserve26 exact original occurrences; two shared gamma-complex findings each list both affected records and predecessors. These curation issues remain open.
- Native validation rejected three policy evidence-kind values in an uncommitted draft. Issue #2599 tracks correction to authority with all references, scopes and substantive content preserved. The corrected draft is revalidated and independently re-reviewed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T062235Z-pr2353-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2353: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T06:11:57.988310Z'
finished_at: '2026-11-03T06:22:35Z'
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
summary: 'Current-input reassessment of all ten cytoskeleton records in PR2353. Five
  stale reviews are substantively refreshed: three gamma-tubulin complexes with changed
  component types, protein examples and budding-yeast context, plus two meiotic tether/LINC
  records with corrected Bqt1-Bqt2 component types. Prior record corrections remain
  scoped historical context. All ten targets retain scientific curation findings.
  The successor corrects structured-source applicability in all ten original bundles
  without editing scientific records. Shared findings for the broad and small gamma-tubulin
  complexes are consolidated with both exact predecessor occurrences and target-specific
  assessments.'
source:
  git_revision: 05425cc7089baf8133399baaf1ec24c00c661de3
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
  - path: data/structures/cytoskeleton/endocytic_patch.yaml
    sha256: 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd
    role: target
  - path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    sha256: 99fd52614b713f1cc678720626553f27f33f5cc4ee0d43b6adfe22108687798d
    role: target
  - path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    sha256: d8eb02a102133174291f4bdbcf09e2d2dfacdc46b217bea636a9bf598ff3d626
    role: target
  - path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    sha256: 231626322f95f06e53ca5d2dcff46f9227d686cd3e73dcfd2e5d99696121f7c3
    role: target
  - path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    sha256: b88b24ae10c1c8ceb36cb1489992fabe20600bff7e85e71a9fd3048d02e15b00
    role: target
  - path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    sha256: 4bf976f7c39fe18c961e155a1e4304153986b271209d2d35aa520a8406c03c65
    role: target
  - path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    sha256: a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e
    role: target
  - path: data/structures/cytoskeleton/spindle.yaml
    sha256: da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e
    role: target
  - path: data/structures/cytoskeleton/spindle_midzone.yaml
    sha256: 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661
    role: target
  - path: data/structures/cytoskeleton/spindle_pole.yaml
    sha256: c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204
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
  - path: reviews/structured/20261021T094807Z-endocytic-patch-audit/review.md
    sha256: 49c7f38aa99056da41534c9ed251731cdac7f3adfc363a9c97f4caf6cb011f6d
    role: context
  - path: reviews/structured/20261021T094807Z-endocytic-patch-audit/review.yaml
    sha256: f6ddb46a3e688c27cbf6bed0d0bff6eadb6565a6b1c687846a207b6b850cfc31
    role: context
  - path: reviews/structured/20261021T094810Z-gamma-tubulin-complex-audit/review.md
    sha256: 2e9673e14bd5b51892c11a56e755552f6116bd1cd399ca3e697b2e8fdb66872f
    role: context
  - path: reviews/structured/20261021T094810Z-gamma-tubulin-complex-audit/review.yaml
    sha256: 21beb5c2956b53e551425105995532ea276f8a33ddbcd98f0d06321d9ee9beb7
    role: context
  - path: reviews/structured/20261021T094812Z-gamma-tubulin-ring-complex-audit/review.md
    sha256: 27e610e8e2e4e7f10d74b1fb7bd00935de1cb1153b6898e61acf6c95e9e2b62c
    role: context
  - path: reviews/structured/20261021T094812Z-gamma-tubulin-ring-complex-audit/review.yaml
    sha256: ab4ec6bfed90f6c65a3f46da69f9ca28af5fe31fda16b7503e2ddda01aaca84a
    role: context
  - path: reviews/structured/20261021T094813Z-gamma-tubulin-small-complex-audit/review.md
    sha256: 019f9342ce2f65ddaa30d653550f12fc75dbd3ed0a0e81d39e9ab1167b308412
    role: context
  - path: reviews/structured/20261021T094813Z-gamma-tubulin-small-complex-audit/review.yaml
    sha256: 39313060aab0aece37d3ab4b8c6ea64ecb311be347c19e82ebafb862b8d974a6
    role: context
  - path: reviews/structured/20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit/review.md
    sha256: dc32b6c3f7688da352cb5636d928e9f0e5f325a53e65bbf725237ec6e64366e0
    role: context
  - path: reviews/structured/20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit/review.yaml
    sha256: eaced5caf3066857faa4ec0fcb88db4f8008ba1ec70f902e0b1cb6a104e88335
    role: context
  - path: reviews/structured/20261021T094818Z-sad1-kms1-linc-complex-audit/review.md
    sha256: d6457ef40cbdf0125299627f926ba84d0f76da27510d75c0c915dd44b7085312
    role: context
  - path: reviews/structured/20261021T094818Z-sad1-kms1-linc-complex-audit/review.yaml
    sha256: 19cdb5d938c218b463b78116ceb59901244e0cc5ca1e16bc2a1ada7ed1dd0a32
    role: context
  - path: reviews/structured/20261021T094819Z-septin-cytoskeleton-audit/review.md
    sha256: 8ef4e20768502f26e0c08a5eaf5916cbf10d31fa023294be66b199f1deb94294
    role: context
  - path: reviews/structured/20261021T094819Z-septin-cytoskeleton-audit/review.yaml
    sha256: 5f0c2da12cbdd4b4d3c16bc78542b41fb5b21f9b58ef52ceba2f7cf5a4e57b74
    role: context
  - path: reviews/structured/20261021T094822Z-spindle-audit/review.md
    sha256: 3e032c5259875a95825f87d213aba9bf1732166d604ce63305a29733b287064f
    role: context
  - path: reviews/structured/20261021T094822Z-spindle-audit/review.yaml
    sha256: 823a761ea54da6f20f9c4b64c8a72bfc10686b0b7c3357a886c45ae5650d756c
    role: context
  - path: reviews/structured/20261021T094824Z-spindle-midzone-audit/review.md
    sha256: cdaafdb961b437f2849139adc1eb9a988dfb57df97dc175dd40ad00293aed391
    role: context
  - path: reviews/structured/20261021T094824Z-spindle-midzone-audit/review.yaml
    sha256: f88a6b35c78bc92def09675aeefbd7953f78bf77511cf46c7d3528af28a475e9
    role: context
  - path: reviews/structured/20261021T094825Z-spindle-pole-audit/review.md
    sha256: b240c5e59b12bc3225aaa97eddcdf131a7cc10171ec356de40765cf612630f6d
    role: context
  - path: reviews/structured/20261021T094825Z-spindle-pole-audit/review.yaml
    sha256: 06fee7037762a59c8cda781490e40f7799675d9f0daff91f8ac42cfedfe3206b
    role: context
  - path: reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.md
    sha256: 09802fd5801576165f6e04640006b691a4ab0ab2f6728ffe25c5bd5c08d5f2a5
    role: context
  - path: reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml
    sha256: ffd4b4cf845f8a4ec0d7806c62152b0e92be5620b6a1373a9e7b292349474def
    role: context
  - path: reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.md
    sha256: 455024d1d5b0c3485d3c43bc1e0cf706295ca320898b0e2445114513bde7587d
    role: context
  - path: reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.yaml
    sha256: d34740ab1423ae3417a5a7ba665d7141ddfea865663a44c75aedfbc77b91d2a4
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
- target_id: GO:0061645
  path: data/structures/cytoskeleton/endocytic_patch.yaml
  label: endocytic patch
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/endocytic_patch.yaml
    role: maintained scientific record
- target_id: GO:0000930
  path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
  label: gamma-tubulin complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    role: maintained scientific record
- target_id: GO:0000931
  path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
  label: gamma-tubulin ring complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    role: maintained scientific record
- target_id: GO:0008275
  path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
  label: gamma-tubulin small complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    role: maintained scientific record
- target_id: GO:0034993
  path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  label: meiotic nuclear membrane microtubule tethering complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
- target_id: GO:1990612
  path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  label: Sad1-Kms1 LINC complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
- target_id: GO:0032156
  path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
  label: septin cytoskeleton
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
- target_id: GO:0005819
  path: data/structures/cytoskeleton/spindle.yaml
  label: spindle
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
- target_id: GO:0051233
  path: data/structures/cytoskeleton/spindle_midzone.yaml
  label: spindle midzone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
- target_id: GO:0000922
  path: data/structures/cytoskeleton/spindle_pole.yaml
  label: spindle pole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 98550c547790b78459491529fe7d5ef3c691a25f.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    4a45d54e374a9f1c60fe2b191cd824b4a6cf3441.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 05425cc7089baf8133399baaf1ec24c00c661de3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 05425cc7089baf8133399baaf1ec24c00c661de3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 05425cc7089baf8133399baaf1ec24c00c661de3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 05425cc7089baf8133399baaf1ec24c00c661de3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 05425cc7089baf8133399baaf1ec24c00c661de3.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0061645
  status: passed
  required: true
  target_ids:
  - GO:0061645
  command: just validate data/structures/cytoskeleton/endocytic_patch.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0061645
  status: passed
  required: true
  target_ids:
  - GO:0061645
  command: just validate-strict data/structures/cytoskeleton/endocytic_patch.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0000930
  status: passed
  required: true
  target_ids:
  - GO:0000930
  command: just validate data/structures/cytoskeleton/gamma_tubulin_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0000930
  status: passed
  required: true
  target_ids:
  - GO:0000930
  command: just validate-strict data/structures/cytoskeleton/gamma_tubulin_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0000931
  status: passed
  required: true
  target_ids:
  - GO:0000931
  command: just validate data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0000931
  status: passed
  required: true
  target_ids:
  - GO:0000931
  command: just validate-strict data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0008275
  status: passed
  required: true
  target_ids:
  - GO:0008275
  command: just validate data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0008275
  status: passed
  required: true
  target_ids:
  - GO:0008275
  command: just validate-strict data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0034993
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: just validate data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0034993
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: just validate-strict data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:1990612
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: just validate data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:1990612
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: just validate-strict data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0032156
  status: passed
  required: true
  target_ids:
  - GO:0032156
  command: just validate data/structures/cytoskeleton/septin_cytoskeleton.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0032156
  status: passed
  required: true
  target_ids:
  - GO:0032156
  command: just validate-strict data/structures/cytoskeleton/septin_cytoskeleton.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0005819
  status: passed
  required: true
  target_ids:
  - GO:0005819
  command: just validate data/structures/cytoskeleton/spindle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0005819
  status: passed
  required: true
  target_ids:
  - GO:0005819
  command: just validate-strict data/structures/cytoskeleton/spindle.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0051233
  status: passed
  required: true
  target_ids:
  - GO:0051233
  command: just validate data/structures/cytoskeleton/spindle_midzone.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0051233
  status: passed
  required: true
  target_ids:
  - GO:0051233
  command: just validate-strict data/structures/cytoskeleton/spindle_midzone.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0000922
  status: passed
  required: true
  target_ids:
  - GO:0000922
  command: just validate data/structures/cytoskeleton/spindle_pole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0000922
  status: passed
  required: true
  target_ids:
  - GO:0000922
  command: just validate-strict data/structures/cytoskeleton/spindle_pole.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353
  exit_code: 0
  summary: 909 PMIDs all OK in bounded native requests; full-command limitations remain
    separate.
  evidence_ids:
  - supplemental-pmid
- check_id: structured-source-applicability
  name: Official structured-source applicability and covered-dataset cross-checks
  status: not_applicable
  required: false
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  summary: 'The complete official catalogue was inspected with actual access timestamps
    and bounded organism/dataset scope. Its returned20organisms/28datasets contain
    no matching eukaryotic dataset for these fungal/algal contexts. Downstream matched
    gene/module queries are therefore not applicable after coverage assessment. Catalogue
    absence is not biological absence, and unrelated bacterial datasets are not substituted.
    Historical native-runner unavailability remains separately disclosed, with no
    fresh runner invocation or success claimed. All ten original reviews require this
    correction: seven omitted applicability and three used unsupported lack-expression
    rationales.'
  evidence_ids:
  - plaque-adapter-catalogue
  - micro-adapter-catalogue
  - septin-current-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-endocytic-prep-go
  - plaque-endocytic-prep-tax-4932
  - plaque-endocytic-prep-tax-559292
  - plaque-endocytic-prep-jats-jcb.200404159
  - plaque-endocytic-prep-galletta2008-plos
  - plaque-endocytic-prep-aghamohammadzadeh2009-jats
  - plaque-endocytic-prep-P60010
  - plaque-endocytic-prep-P32381
  - plaque-endocytic-prep-P47117
  - plaque-endocytic-prep-P38328
  - plaque-endocytic-prep-P53731
  - plaque-endocytic-prep-P33204
  - plaque-endocytic-prep-Q05933
  - plaque-endocytic-prep-P40518
  - plaque-endocytic-prep-IPR004000
  - plaque-tether-prep-go
  - plaque-tether-prep-tax-284812
  - plaque-tether-prep-tax-4751
  - plaque-tether-prep-paper
  - plaque-tether-prep-moiseeva2017-jats
  - plaque-tether-prep-jimenez2025-jats
  - plaque-linc-agent-csm2020-jats
  - plaque-tether-prep-IPR045119
  - plaque-tether-prep-Q09825
  - plaque-tether-prep-P87245
  - plaque-tether-prep-Q92358
  - plaque-tether-prep-Q9US52
  - plaque-linc-agent-go
  - plaque-linc-agent-chikashige2006-api
  - plaque-linc-agent-fan2020-jats
  - plaque-linc-agent-amelina2015-jats
  - plaque-linc-agent-yoshida2013-jats
  - plaque-linc-agent-swartz2014-jats
  - plaque-graph-contract
  - plaque-schema
  - plaque-adapter-policy
  - plaque-historical-2420
  - micro-go
  - micro-taxon-2759
  - micro-taxon-284812
  - micro-taxon-4896
  - micro-taxon-559292
  - micro-interpro
  - micro-uniprot-P25295
  - micro-uniprot-Q9USH8
  - micro-uniprot-P53378
  - micro-uniprot-Q9Y705
  - micro-uniprot-Q9USQ2
  - micro-uniprot-P38863
  - micro-uniprot-P53540
  - micro-uniprot-Q9P7R5
  - micro-uniprot-Q9UT52
  - micro-uniprot-P87244
  - micro-uniprot-O94488
  - micro-uniprot-Q9USP7
  - micro-new-europepmc
  - micro-viswanath2017
  - micro-samejima2010
  - micro-samejima2008
  - micro-lynch2014
  - micro-brilot2021
  - micro-lyon2016
  - micro-bellingham2023
  - micro-florparra2018
  - micro-masuda2013
  - micro-samejima2005
  - micro-venkatram2005
  - micro-anders2006
  - micro-pmid-11080156
  - micro-pmid-15004232
  - micro-pmid-12134075
  - micro-jaspersen-secondary
  - micro-adapter-catalogue
  - septin-septin-agent-go
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-5476
  - septin-septin-agent-tax-559292
  - septin-septin-agent-P32457
  - septin-septin-agent-P25342
  - septin-septin-agent-P32458
  - septin-septin-agent-P32468
  - septin-septin-agent-Q07657
  - septin-septin-agent-IPR016491
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-douglas-pmc
  - septin-septin-agent-finnigan2015-pmc
  - septin-spindle-agent-go
  - septin-spindle-agent-viswanath2017
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-spindle-agent-IPR000217
  - septin-spindle-agent-IPR002452
  - septin-spindle-agent-IPR002453
  - septin-spindle-agent-winey1995-pdf
  - septin-midzone-agent-go
  - septin-pole-agent-go
  - septin-pole-agent-tax-2759
  - septin-current-adapter-catalogue
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-policy
  - septin-adapter-policy
  - septin-graph-policy
  - septin-graph-contract
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
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
- check_id: endocytic_patch-uniprot-verify
  name: Native endocytic patch UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0061645
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/endocytic_patch.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-endocytic_patch-verify
- check_id: endocytic_patch-uniprot-causal
  name: Native endocytic patch UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0061645
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/endocytic_patch.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-endocytic_patch-causal
- check_id: gamma_tubulin_complex-uniprot-verify
  name: Native gamma-tubulin complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000930
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-gamma_tubulin_complex-verify
- check_id: gamma_tubulin_complex-uniprot-causal
  name: Native gamma-tubulin complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000930
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-gamma_tubulin_complex-causal
- check_id: gamma_tubulin_ring_complex-uniprot-verify
  name: Native gamma-tubulin ring complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000931
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-gamma_tubulin_ring_complex-verify
- check_id: gamma_tubulin_ring_complex-uniprot-causal
  name: Native gamma-tubulin ring complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000931
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-gamma_tubulin_ring_complex-causal
- check_id: gamma_tubulin_small_complex-uniprot-verify
  name: Native gamma-tubulin small complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0008275
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-gamma_tubulin_small_complex-verify
- check_id: gamma_tubulin_small_complex-uniprot-causal
  name: Native gamma-tubulin small complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0008275
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-gamma_tubulin_small_complex-causal
- check_id: meiotic_nuclear_membrane_microtubule_tethering_complex-uniprot-verify
  name: Native meiotic nuclear membrane microtubule tethering complex UniProt verify
    check
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-verify
- check_id: meiotic_nuclear_membrane_microtubule_tethering_complex-uniprot-causal
  name: Native meiotic nuclear membrane microtubule tethering complex UniProt causal
    check
  status: passed
  required: true
  target_ids:
  - GO:0034993
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-causal
- check_id: sad1_kms1_linc_complex-uniprot-verify
  name: Native Sad1-Kms1 LINC complex UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-sad1_kms1_linc_complex-verify
- check_id: sad1_kms1_linc_complex-uniprot-causal
  name: Native Sad1-Kms1 LINC complex UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:1990612
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-sad1_kms1_linc_complex-causal
- check_id: septin_cytoskeleton-uniprot-verify
  name: Native septin cytoskeleton UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0032156
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-septin_cytoskeleton-verify
- check_id: septin_cytoskeleton-uniprot-causal
  name: Native septin cytoskeleton UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0032156
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-septin_cytoskeleton-causal
- check_id: spindle-uniprot-verify
  name: Native spindle UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005819
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-spindle-verify
- check_id: spindle-uniprot-causal
  name: Native spindle UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005819
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-spindle-causal
- check_id: spindle_midzone-uniprot-verify
  name: Native spindle midzone UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0051233
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-spindle_midzone-verify
- check_id: spindle_midzone-uniprot-causal
  name: Native spindle midzone UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0051233
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-spindle_midzone-causal
- check_id: spindle_pole-uniprot-verify
  name: Native spindle pole UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000922
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_pole.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-spindle_pole-verify
- check_id: spindle_pole-uniprot-causal
  name: Native spindle pole UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000922
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_pole.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence; spindle-pole empty inventory and zero
    molecular graph nodes do not validate its prose mechanisms. Deterministic identifier
    coverage does not resolve scientific findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-spindle_pole-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/cytoskeleton/endocytic_patch.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd;
    current SHA256 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd.
    Record bytes unchanged since the original review.
  snapshot_sha256: 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T094807Z-endocytic-patch-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f6ddb46a3e688c27cbf6bed0d0bff6eadb6565a6b1c687846a207b6b850cfc31
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 b9d0f02cefde432060b919928520d31642f07c3979aa91ba5786e8d5facbc2d1;
    current SHA256 99fd52614b713f1cc678720626553f27f33f5cc4ee0d43b6adfe22108687798d.
    Changed record reassessed against current sources.
  snapshot_sha256: 99fd52614b713f1cc678720626553f27f33f5cc4ee0d43b6adfe22108687798d
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T094810Z-gamma-tubulin-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 21beb5c2956b53e551425105995532ea276f8a33ddbcd98f0d06321d9ee9beb7
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 77875af04893db1912e05c01ece8dd67b958d77d452787639401288060226df9;
    current SHA256 d8eb02a102133174291f4bdbcf09e2d2dfacdc46b217bea636a9bf598ff3d626.
    Changed record reassessed against current sources.
  snapshot_sha256: d8eb02a102133174291f4bdbcf09e2d2dfacdc46b217bea636a9bf598ff3d626
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T094812Z-gamma-tubulin-ring-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: ab4ec6bfed90f6c65a3f46da69f9ca28af5fe31fda16b7503e2ddda01aaca84a
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 31bb27b71d6725bf736455a92b5e47849d17869af98675adc45eb9b4a157e1c6;
    current SHA256 231626322f95f06e53ca5d2dcff46f9227d686cd3e73dcfd2e5d99696121f7c3.
    Changed record reassessed against current sources.
  snapshot_sha256: 231626322f95f06e53ca5d2dcff46f9227d686cd3e73dcfd2e5d99696121f7c3
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T094813Z-gamma-tubulin-small-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 39313060aab0aece37d3ab4b8c6ea64ecb311be347c19e82ebafb862b8d974a6
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 1edc92bdba11eec4c3da00ba06bd5cae3bd2593f5ba94be9d545c52a9da86049;
    current SHA256 b88b24ae10c1c8ceb36cb1489992fabe20600bff7e85e71a9fd3048d02e15b00.
    Changed record reassessed against current sources.
  snapshot_sha256: b88b24ae10c1c8ceb36cb1489992fabe20600bff7e85e71a9fd3048d02e15b00
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: eaced5caf3066857faa4ec0fcb88db4f8008ba1ec70f902e0b1cb6a104e88335
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 2dc179231cae9404e022e417327a94b550b75c47872ef2e467330ea79d5cdf17;
    current SHA256 4bf976f7c39fe18c961e155a1e4304153986b271209d2d35aa520a8406c03c65.
    Changed record reassessed against current sources.
  snapshot_sha256: 4bf976f7c39fe18c961e155a1e4304153986b271209d2d35aa520a8406c03c65
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T094818Z-sad1-kms1-linc-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 19cdb5d938c218b463b78116ceb59901244e0cc5ca1e16bc2a1ada7ed1dd0a32
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/cytoskeleton/septin_cytoskeleton.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e;
    current SHA256 a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e.
    Record bytes unchanged since the original review.
  snapshot_sha256: a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T094819Z-septin-cytoskeleton-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5f0c2da12cbdd4b4d3c16bc78542b41fb5b21f9b58ef52ceba2f7cf5a4e57b74
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/cytoskeleton/spindle.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e;
    current SHA256 da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e.
    Record bytes unchanged since the original review.
  snapshot_sha256: da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T094822Z-spindle-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 823a761ea54da6f20f9c4b64c8a72bfc10686b0b7c3357a886c45ae5650d756c
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_midzone.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661;
    current SHA256 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661.
    Record bytes unchanged since the original review.
  snapshot_sha256: 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T094824Z-spindle-midzone-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f88a6b35c78bc92def09675aeefbd7953f78bf77511cf46c7d3528af28a475e9
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Original frozen SHA256 c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204;
    current SHA256 c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204.
    Record bytes unchanged since the original review.
  snapshot_sha256: c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T094825Z-spindle-pole-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T06:22:35Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 06fee7037762a59c8cda781490e40f7799675d9f0daff91f8ac42cfedfe3206b
- evidence_id: plaque-endocytic-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0005885,GO:0005938,GO:0015629,GO:0030479,GO:0030864,GO:0061645,GO:0110165
  locator: All requested term names, definitions, obsoletion, synonym and returned
    child relation objects
  accessed_at: '2026-11-03T06:14:05.987882Z'
  summary: Fresh native terms distinguish broad GO0061645 endocytic patch from its
    GO0030479 actin-rich subtype and confirm exact Arp2/3, cell-cortex and process
    identities/relations. GO-only definitions do not establish the added complete
    fungal molecular sequence.
  support: supports
  snapshot_sha256: a239831b9f269db06defa117b5777b310315e86211abb27839644fe0493ca412
- evidence_id: plaque-endocytic-prep-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T06:14:05.988079Z'
  summary: Native taxonomy resolves 4932 as Saccharomyces cerevisiae (species); taxon
    validity is distinct from demonstrated distribution of a named assembly.
  support: supports
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: plaque-endocytic-prep-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T06:14:05.988138Z'
  summary: Native taxonomy resolves 559292 as Saccharomyces cerevisiae S288C (strain);
    taxon validity is distinct from demonstrated distribution of a named assembly.
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: plaque-endocytic-prep-jats-jcb.200404159
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2172413.1/PMC2172413.1.xml
  locator: Entire main scientific Introduction, Results/discussion and Methods; main
    figure captions; Table I caption (not supplementary assets or image pixels).
  accessed_at: '2026-11-03T06:14:05.988213Z'
  summary: Young2004 directly examines partially purified, stabilized S. cerevisiae
    cortical patches by correlated fluorescence/negative-stain EM. Branched actin
    geometry is consistent with Arp2/3; Sac6 and Cap1 perturbations distinguish stability
    from general architecture. KS buffer, crosslinking and latrunculin treatments
    bound inference; this is not a whole-fungal component census.
  support: partial
  snapshot_sha256: 7f6584b83df46499ba5c7e041436bf04a67115725fd90c8470d8c5982e073bf4
- evidence_id: plaque-endocytic-prep-galletta2008-plos
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060001
  locator: 'Publisher HTML: Introduction three-phase account; first Las17 acidic-domain
    Results and Figure 2 caption; immediately following Myo3/Myo5 paragraph. Other
    Results/Methods/supplements not freshly audited.'
  accessed_at: '2026-11-03T06:14:06.389008Z'
  summary: Galletta2008 distinguishes recruitment, slow inward movement and later
    motion at yeast endocytic sites. Las17 acidic-domain removal delays actin arrival
    and affects later movement; GFP-Las17 fusion limitations are explicit. Early patches
    can organize later actin assembly. This is not evidence that every patch stage
    has the same composition.
  support: partial
  snapshot_sha256: 0cdca43d2b1c72883876e77eadbe2a11f872e4a05f8e29aa60ea7d91dd4ac3bc
- evidence_id: plaque-endocytic-prep-aghamohammadzadeh2009-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2875176.1/PMC2875176.1.xml
  locator: Entire ten main-body paragraphs, from background through concluding model;
    supplemental Methods and image pixels not inspected.
  accessed_at: '2026-11-03T06:14:06.603268Z'
  summary: Aghamohammadzadeh2009 manipulates osmotic support and actin-bundling/latrunculin
    conditions in yeast. Sorbitol partially rescues invagination yet post-scission
    movement remains limited; increased turgor impairs invagination. This supports
    a condition-specific turgor/actin mechanism, not universal obligatory actin membership
    at every endocytic stage.
  support: partial
  snapshot_sha256: 386ffb5b2dc79c1e2958156b358387900e88310090681f7a5fad902c89cc275c
- evidence_id: plaque-endocytic-prep-kaksonen2003-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:14622601%20AND%20SRC:MED
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:06.618408Z'
  summary: 'Identity cross-check: 14622601 10.1016/s0092-8674(03)00883-3 A pathway
    for association of receptors, adaptors, and actin during endocytic internalization..
    No whole-body claim from metadata. Complete abstract read: stage-dependent recruitment,
    late actin assembly and Sla2-mutant actin comet tails support early endocytic
    sites organizing subsequent actin assembly.'
  support: context_only
  snapshot_sha256: 231ebac644f0b6710d7390920df5d22ca887f86426188e1fd407d7e98dae6510
  search_scope: Europe PMC REST; format=json&resultType=core&query=EXT_ID:14622601
    AND SRC:MED; accessed 2026-11-03T06:14:06.618408Z; only returned DOI/PMID matches,
    no broad literature-absence inference.
- evidence_id: plaque-endocytic-prep-doi-jcb.200404159-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200404159
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:06.771870Z'
  summary: 'Identity cross-check: 15337772 10.1083/jcb.200404159 Yeast actin patches
    are networks of branched actin filaments.. No whole-body claim from metadata.'
  support: context_only
  snapshot_sha256: 678b444097b37f9988960c614b68996c30f44d37289bcd050157421186ca3097
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1083/jcb.200404159;
    accessed 2026-11-03T06:14:06.771870Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-endocytic-prep-doi-journal.pbio.0060001-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.0060001
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:07.011803Z'
  summary: 'Identity cross-check: 18177206 10.1371/journal.pbio.0060001 Distinct roles
    for Arp2/3 regulators in actin assembly and endocytosis.. No whole-body claim
    from metadata.'
  support: context_only
  snapshot_sha256: ac7737e4a85ce68ea155e71e279b4cb05d0945a25d329982a6f7bd47c3927e15
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1371/journal.pbio.0060001;
    accessed 2026-11-03T06:14:07.011803Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-endocytic-prep-pmid-11248049-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11248049%20AND%20SRC%3AMED
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:07.203299Z'
  summary: 'Identity cross-check: 11248049 10.1073/pnas.051494698 Arp2/3 complex and
    actin dynamics are required for actin-based mitochondrial motility in yeast..
    No whole-body claim from metadata. Complete abstract read: direct focus is Arp2/Arc15
    mitochondrial association and dynamics, while the native UniProt localization
    annotation is separately verified. No body-level patch experiment is inferred.'
  support: context_only
  snapshot_sha256: fe047d85d1c3b0f5f6b0ef27fe7687ff5c4b38a69c446d65ec8b40d0417396e6
  search_scope: Europe PMC REST; format=json&resultType=core&query=EXT_ID:11248049
    AND SRC:MED; accessed 2026-11-03T06:14:07.203299Z; only returned DOI/PMID matches,
    no broad literature-absence inference.
- evidence_id: plaque-endocytic-prep-pmid-9210376-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9210376%20AND%20SRC%3AMED
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:07.317675Z'
  summary: 'Identity cross-check: 9210376 10.1016/s0960-9822(06)00223-5 The complex
    containing actin-related proteins Arp2 and Arp3 is required for the motility and
    integrity of yeast actin patches.. No whole-body claim from metadata. Complete
    abstract read: Arp3 patch localization, conditional mutant effects and purified
    complex are reported. No full-body inspection claimed.'
  support: context_only
  snapshot_sha256: 8c00acf3fa71f64c1bfe2155e0e17151cd881e3ecf51de2c4910d4cdc123baf8
  search_scope: Europe PMC REST; format=json&resultType=core&query=EXT_ID:9210376
    AND SRC:MED; accessed 2026-11-03T06:14:07.317675Z; only returned DOI/PMID matches,
    no broad literature-absence inference.
- evidence_id: plaque-endocytic-prep-P60010
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P60010.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:07.560386Z'
  summary: Fresh reviewed native entry P60010 matches ACT1, Actin, taxon 559292. Reference-sequence
    identity is distinct from exact experimental stock. Native location annotations
    are database evidence, not an inspected primary experiment.
  support: supports
  snapshot_sha256: 85ccbfada9f62388f2b4f90b3b15fd6e7c5df202249d114e3f5ed8482a086034
- evidence_id: plaque-endocytic-prep-P32381
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32381.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:07.763784Z'
  summary: Fresh reviewed native entry P32381 matches ARP2, Actin-related protein
    2, taxon 559292. Reference-sequence identity is distinct from exact experimental
    stock. Native location annotations are database evidence, not an inspected primary
    experiment.
  support: supports
  snapshot_sha256: 2b378f480e51da72d42b3b9dce10343e882ecd765163079ebba5dee3a2597bf9
- evidence_id: plaque-endocytic-prep-P47117
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47117.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:07.841098Z'
  summary: Fresh reviewed native entry P47117 matches ARP3, Actin-related protein
    3, taxon 559292. Reference-sequence identity is distinct from exact experimental
    stock. Native location annotations are database evidence, not an inspected primary
    experiment.
  support: supports
  snapshot_sha256: c1fb00ae697516d543e044536958483b7e17ee1660700e869689adb336de7b71
- evidence_id: plaque-endocytic-prep-P38328
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38328.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:08.006561Z'
  summary: Fresh reviewed native entry P38328 matches ARC40, Actin-related protein
    2/3 complex subunit 1, taxon 559292. Reference-sequence identity is distinct from
    exact experimental stock. Native location annotations are database evidence, not
    an inspected primary experiment.
  support: supports
  snapshot_sha256: cb2cf7eba6e89e1c6e9a26a6cab12515382eff955ca37f302d7762c99853a6eb
- evidence_id: plaque-endocytic-prep-P53731
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53731.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:08.403806Z'
  summary: Fresh reviewed native entry P53731 matches ARC35, Actin-related protein
    2/3 complex subunit 2, taxon 559292. Reference-sequence identity is distinct from
    exact experimental stock. Native location annotations are database evidence, not
    an inspected primary experiment.
  support: supports
  snapshot_sha256: 7c903010adc7254a171b89a0cf935052237882f9599de322c36116a29640f2ad
- evidence_id: plaque-endocytic-prep-P33204
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33204.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:08.540769Z'
  summary: Fresh reviewed native entry P33204 matches ARC19, Actin-related protein
    2/3 complex subunit 4, taxon 559292. Reference-sequence identity is distinct from
    exact experimental stock. Native location annotations are database evidence, not
    an inspected primary experiment.
  support: supports
  snapshot_sha256: 6a510fff14b0f9054f847c6ad26e13dfc29e391b6c173a27dc6410b509bf7000
- evidence_id: plaque-endocytic-prep-Q05933
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q05933.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:08.937867Z'
  summary: Fresh reviewed native entry Q05933 matches ARC18, Actin-related protein
    2/3 complex subunit 3, taxon 559292. Reference-sequence identity is distinct from
    exact experimental stock. Native location annotations are database evidence, not
    an inspected primary experiment.
  support: supports
  snapshot_sha256: a0f9700443c987dd59d04c81980287273147117d9c570aa6e3cafdb62636eb51
- evidence_id: plaque-endocytic-prep-P40518
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40518.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:08.980767Z'
  summary: Fresh reviewed native entry P40518 matches ARC15, Actin-related protein
    2/3 complex subunit 5, taxon 559292. Reference-sequence identity is distinct from
    exact experimental stock. Native location annotations are database evidence, not
    an inspected primary experiment.
  support: supports
  snapshot_sha256: f6a13b306d4e1740fa932240cf28d5ab9ef710a923167a97c1442d240b3014f2
- evidence_id: plaque-endocytic-prep-ACT1-query
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29%20AND%20%28organism_id%3A559292%29%20AND%20%28gene_exact%3AACT1%29&format=json&size=500
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:09.909911Z'
  summary: Native exact query returns [('P60010', 'ACT1', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: 5f32bb1ef917c3425db2aaa4a4d4f98e2a08794a7994a79de7a51aabe7b8c75c
  search_scope: UniProt REST; query=(reviewed:true) AND (organism_id:559292) AND (gene_exact:ACT1)&format=json&size=500;
    accessed 2026-11-03T06:14:09.909911Z; all returned results, bounded to this exact
    reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARP2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARP2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:09.917938Z'
  summary: Native exact query returns [('P32381', 'ARP2', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: dfebbdfdb0fb815de18cf04958a76825298435a28c2b14fb2f4d644fbf8cba8a
  search_scope: UniProt REST; format=json&query=(gene_exact:ARP2) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:09.917938Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:10.915184Z'
  summary: Native exact query returns [('P47117', 'ARP3', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: 2fd3bf9551a26771c0fa16bbc3e318de130696bc94b2f4760fc8e138bf421e61
  search_scope: UniProt REST; format=json&query=(gene_exact:ARP3) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:10.915184Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARC40
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC40%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:11.006255Z'
  summary: Native exact query returns [('P38328', 'ARC40', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: 42f2915f586bbecd94d03031300dd449208983f62bc6db4d9af39e1d3c977873
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC40) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:11.006255Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARC35
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC35%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:11.984834Z'
  summary: Native exact query returns [('P53731', 'ARC35', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: 6cfa62fe3454446fd9c97d4e8ab4b2b8a26222347f367e0f602cf9257c9cb995
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC35) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:11.984834Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARC19
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC19%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:12.033842Z'
  summary: Native exact query returns [('P33204', 'ARC19', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: 1a847c87c46f70cfa1ce9a557d5e37332a3594ef1168d73e6de42081e4fe8c66
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC19) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:12.033842Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARC18
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC18%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:12.893748Z'
  summary: Native exact query returns [('Q05933', 'ARC18', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: f8ea6b20283807a786443913a74fe80a7023003e5e2608a2c103baa8f7fc535a
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC18) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:12.893748Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-query-ARC15
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC15%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon query results
  accessed_at: '2026-11-03T06:14:13.185012Z'
  summary: Native exact query returns [('P40518', 'ARC15', 559292)]; identity mapping
    only, not direct localization or mechanism.
  support: supports
  snapshot_sha256: 75eaaf64f0a1c5a0496ac86ba4e1965a492f606002cc2481475fc5b829c66aa4
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC15) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T06:14:13.185012Z; all returned results,
    bounded to this exact reviewed strain/gene query.
- evidence_id: plaque-endocytic-prep-IPR004000
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004000/
  locator: metadata name/type and non-LLM native description
  accessed_at: '2026-11-03T06:14:13.948014Z'
  summary: IPR004000 Actin family explicitly includes divergent Arp subfamilies; it
    is broader than conventional actin. Its presence does not by itself invalidate
    the bounded label-only component. No exhaustive exact-family absence claim is
    made.
  support: supports
  snapshot_sha256: 353427570f0d1c3842a14f7737374f68e9dd70a98b09cf9fc2a8e8c86062edca
- evidence_id: plaque-tether-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030989,GO:0032117,GO:0034992,GO:0034993,GO:0106094
  locator: All requested term names, definitions, obsoletion, synonym and returned
    child relation objects
  accessed_at: '2026-11-03T06:14:14.036499Z'
  summary: Fresh native GO identities and exact returned relationships inspected for
    GO:0030989 dynein-driven meiotic oscillatory nuclear movement, GO:0106094 nuclear
    membrane microtubule tethering complex, GO:0032117 horsetail-astral microtubule
    array, GO:0034992 microtubule organizing center attachment site, GO:0034993 meiotic
    nuclear membrane microtubule tethering complex. GO0032117 is an array, distinct
    from GO0034993 tether; GO0034993 has GO1990612 as is_a child. Source-neutral definitions
    do not establish the appended detailed molecular/taxonomic claims.
  support: supports
  snapshot_sha256: 1ca86216e19f89b64e2249ec78841fd33387808beb5715ef3db699bd86af381d
- evidence_id: plaque-tether-prep-tax-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T06:14:14.633306Z'
  summary: Native taxonomy resolves 284812 as Schizosaccharomyces pombe 972h- (strain);
    taxon validity is distinct from demonstrated distribution of a named assembly.
  support: supports
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: plaque-tether-prep-tax-4751
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-11-03T06:14:14.636204Z'
  summary: Native taxonomy resolves 4751 as Fungi (kingdom); taxon validity is distinct
    from demonstrated distribution of a named assembly.
  support: supports
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: plaque-tether-prep-doi-j.cell.2006.01.048-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2006.01.048
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:14.983891Z'
  summary: 'Identity cross-check: 16615890 10.1016/j.cell.2006.01.048 Meiotic proteins
    bqt1 and bqt2 tether telomeres to form the bouquet arrangement of chromosomes..
    No whole-body claim from metadata. Complete primary abstract read: Bqt1 and Bqt2
    jointly bridge Rap1 and Sad1; neither alone suffices, including ectopic mitotic
    expression. Supports distinct-protein complex typing at this scope.'
  support: context_only
  snapshot_sha256: 6337fa71c036ba0ceb99ffcc460db9ccf4aecc16c3bf4970ffad68969cb48f0d
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1016/j.cell.2006.01.048;
    accessed 2026-11-03T06:14:14.983891Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-tether-prep-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml
  locator: 'Funaya2012 PMC3382715.1: Introduction sec1; Results sec2.1–2.3 and sec2.5;
    Discussion sec3; Methods sec4.1. No fresh supplements, figure-pixel or movie inspection.'
  accessed_at: '2026-11-03T06:14:14.996166Z'
  summary: Fresh primary JATS distinguishes Hrs1-dependent rMTOC/radial array from
    the nuclear-envelope bridge. EM tomography of synchronized engineered meiotic
    cells and Hrs1 localization support array organization. Introductory Kms1/Sad1
    topology is prior-study background; direct Hrs1 phosphomutant two-hybrid assays
    test Kms1/Alp4 interactions and discuss possible Kms2 compensation. These are
    not direct dynein-recruitment assays.
  support: partial
  snapshot_sha256: 59f662c998abf622fbb9bccbabc3867cb5ffd3174943cc52cb6228b1e35cd93d
- evidence_id: plaque-tether-prep-moiseeva2017-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5674143.1/PMC5674143.1.xml
  locator: Results Bouquet formation ensures entry into meiosis I and Premature termination
    of the bouquet leads to spindle defects (all paragraphs); Methods Strains/media,
    Microscope image acquisition and Auxin-inducible system.
  accessed_at: '2026-11-03T06:14:15.232117Z'
  summary: Moiseeva2017 shows Bqt1-AID disruption releases telomeres from the SPB
    and can cause prophase/spindle defects. Approximately half of bouquet-deficient
    cells still divide; direct spindle imaging uses rdh54 background. Main culture/media
    and 28 C imaging conditions were inspected. These are attachment/function assays,
    not a complete core-LINC assembly-necessity test.
  support: partial
  snapshot_sha256: e5b2fc8c46775b2f6a9e0b176bb16d6f2bae801e78e90b191369414ca23f84a3
- evidence_id: plaque-tether-prep-jimenez2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11747273.1/PMC11747273.1.xml
  locator: Results Sec8 paragraphs1–6 including integrated Figure6 caption, Sec9 paragraph1,
    Sec10 paragraph1/Figure7 caption; Methods Sec14 paragraphs1–3.
  accessed_at: '2026-11-03T06:14:15.462051Z'
  summary: Jimenez2025 observes Bqt1/Bqt2-dependent recruitment of Sad1/Kms1, Alp4
    and Mto1 to telomeres in Rabl-deficient mitotic haploids. No Dhc1 or complete
    bouquet was detected in that partial reconstitution. Natural meiotic entry is
    a separate diploid experiment. The maintained Kms1 example correctly preserves
    that limitation.
  support: partial
  snapshot_sha256: 1e0470a799e49976e35584be8e8449af77c2e85fd1e11576a460227cd526e4ed
- evidence_id: plaque-linc-agent-csm2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7181386.1/PMC7181386.1.xml
  locator: Introduction S1; Results S5–S8; Discussion S10; Methods S14 and S16–S20.
    No raw movies or complete supplementary strain tables inspected.
  accessed_at: '2026-11-03T06:14:15.699376Z'
  summary: Lee2020 tests budding-yeast Mps2/Mps3/Csm4/Myo2 with localization, co-IP,
    two-hybrid and dominant-negative Myo2. It supports an actin-associated motility
    model and explicitly allows Csm4 stabilization versus actin-recruitment alternatives
    and pleiotropic dominant-negative effects. It cannot establish universal dynein
    coupling across fungal LINC systems.
  support: partial
  snapshot_sha256: fc2ee1f306bcb93fb50bd1335c1a60bdd901b50f1ece7f7b1f8c63371a362c9a
- evidence_id: plaque-tether-prep-IPR045119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045119/
  locator: metadata name/type and non-LLM native description
  accessed_at: '2026-11-03T06:14:15.712007Z'
  summary: IPR045119 is SUN domain-containing protein 1–5 family, includes Sad1/UNC84
    envelope bridge context, and is cross-referenced by Q09825. Family grounding does
    not establish individual mechanistic experiments.
  support: supports
  snapshot_sha256: ebf2e470f10e591fe8475c39ac5142261438a51a9bba2571c0282d80a75d359e
- evidence_id: plaque-tether-prep-Q09825
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q09825.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:15.817097Z'
  summary: Fresh reviewed native entry Q09825 matches sad1, Spindle pole body-associated
    protein sad1, taxon 284812. Reference-sequence identity is distinct from exact
    experimental stock. Native location annotations are database evidence, not an
    inspected primary experiment.
  support: supports
  snapshot_sha256: af97b71167c7297318086add00ac1143a9ab78a2f714035f76ff4c31bf77993d
- evidence_id: plaque-tether-prep-P87245
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P87245.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:16.025792Z'
  summary: Fresh reviewed native entry P87245 matches kms1, Karyogamy meiotic segregation
    protein 1, taxon 284812. Reference-sequence identity is distinct from exact experimental
    stock. Native location annotations are database evidence, not an inspected primary
    experiment.
  support: supports
  snapshot_sha256: 84aa928d02abba093e6be0c791d5d9f775268e8701d7955ab7f7d7cbb36eb234
- evidence_id: plaque-tether-prep-Q92358
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q92358.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:16.377509Z'
  summary: Fresh reviewed native entry Q92358 matches bqt1, Telomere bouquet protein
    1, taxon 284812. Reference-sequence identity is distinct from exact experimental
    stock. Native location annotations are database evidence, not an inspected primary
    experiment.
  support: supports
  snapshot_sha256: f4cfccab706bbf9515cd342b8bf6a7409bdb96c9a45f0e6ac5320e967827dd42
- evidence_id: plaque-tether-prep-Q9US52
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9US52.json
  locator: entryType, primaryAccession, recommended name, genes, organism; subcellular-location
    evidence and InterPro cross-references
  accessed_at: '2026-11-03T06:14:16.554669Z'
  summary: Fresh reviewed native entry Q9US52 matches bqt2, Telomere bouquet protein
    2, taxon 284812. Reference-sequence identity is distinct from exact experimental
    stock. Native location annotations are database evidence, not an inspected primary
    experiment.
  support: supports
  snapshot_sha256: 51cfcf49971d8963b57f32b278b49e710b600813b392a15565ffb4b80b2b09e9
- evidence_id: plaque-tether-prep-doi-celldisc.2017.41-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/celldisc.2017.41
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:16.659894Z'
  summary: 'Identity cross-check: 29123917 10.1038/celldisc.2017.41 The telomere bouquet
    facilitates meiotic prophase progression and exit in fission yeast.. No whole-body
    claim from metadata.'
  support: context_only
  snapshot_sha256: 7fa2f4851a8c430ea5d36bebfc02128e84cb4924adb9619c1a567b838b560b4e
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1038/celldisc.2017.41;
    accessed 2026-11-03T06:14:16.659894Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-tether-prep-doi-j.cub.2012.02.042-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2012.02.042
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:16.841181Z'
  summary: 'Identity cross-check: 22425159 10.1016/j.cub.2012.02.042 Transient structure
    associated with the spindle pole body directs meiotic microtubule reorganization
    in S. pombe.. No whole-body claim from metadata.'
  support: context_only
  snapshot_sha256: 74ff9c0672edac602df99d3e760b7346e0642f4100839c6381f1696d4599f944
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1016/j.cub.2012.02.042;
    accessed 2026-11-03T06:14:16.841181Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-tether-prep-doi-j.cub.2005.07.058-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2005.07.058
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:17.008545Z'
  summary: 'Identity cross-check: 16111942 10.1016/j.cub.2005.07.058 Hrs1p/Mcp6p on
    the meiotic SPB organizes astral microtubule arrays for oscillatory nuclear movement..
    No whole-body claim from metadata. Complete abstract read: Hrs1 loss impairs HAA
    and movement; ectopic Hrs1 yields HAA-like arrays. Full text and supplements were
    not inspected.'
  support: context_only
  snapshot_sha256: d5824c952167588e7f7dd5dd666232d47f8d46c48ed266dc0f91e28aa36ac7c1
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1016/j.cub.2005.07.058;
    accessed 2026-11-03T06:14:17.008545Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-tether-prep-doi-s41467-025-56049-9-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41467-025-56049-9
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:17.242367Z'
  summary: 'Identity cross-check: 39833200 10.1038/s41467-025-56049-9 Centromere positioning
    orchestrates telomere bouquet formation and the initiation of meiotic differentiation..
    No whole-body claim from metadata.'
  support: context_only
  snapshot_sha256: 325789797eecd5b9eeed48935df51e17787ef0c6e6f55cbec5ce4ffebe708d6f
  search_scope: Europe PMC REST; format=json&resultType=core&query=DOI:10.1038/s41467-025-56049-9;
    accessed 2026-11-03T06:14:17.242367Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-linc-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990612,GO:0034993,GO:0032200,GO:0032993,GO:0005634,GO:0000228,GO:0000781
  locator: All requested term names, definitions, obsoletion, synonym and returned
    child relation objects
  accessed_at: '2026-11-03T06:14:17.323142Z'
  summary: Fresh native GO identities and exact returned relationships inspected for
    GO:0005634 nucleus, GO:0032993 protein-DNA complex, GO:0000228 nuclear chromosome,
    GO:1990612 Sad1-Kms1 LINC complex, GO:0000781 chromosome, telomeric region, GO:0032200
    telomere organization, GO:0034993 meiotic nuclear membrane microtubule tethering
    complex. GO0032117 is an array, distinct from GO0034993 tether; GO0034993 has
    GO1990612 as is_a child. Source-neutral definitions do not establish the appended
    detailed molecular/taxonomic claims.
  support: supports
  snapshot_sha256: 7eb3c9ffaf4a96aa8a6f064a948d01cacb5f8dba064480cd9ff1add57a3875c6
- evidence_id: plaque-linc-agent-epmc
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.26508/lsa.202000824%22%20OR%20DOI:%2210.1186/s12915-015-0149-x%22%20OR%20DOI:%2210.1016/j.cub.2020.01.054%22%20OR%20DOI:%2210.1038/s41467-025-56049-9%22&format=json&resultType=core&pageSize=100
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:17.487074Z'
  summary: 'Identity cross-check: 39833200 10.1038/s41467-025-56049-9 Centromere positioning
    orchestrates telomere bouquet formation and the initiation of meiotic differentiation.;
    32967926 10.26508/lsa.202000824 Mps2 links Csm4 and Mps3 to form a telomere-associated
    LINC complex in budding yeast.; 32059771 10.1016/j.cub.2020.01.054 Extranuclear
    Structural Components that Mediate Dynamic Chromosome Movements in Yeast Meiosis.;
    26058898 10.1186/s12915-015-0149-x Telomere protein Rap1 is a charge resistant
    scaffolding protein in chromosomal bouquet formation.. No whole-body claim from
    metadata.'
  support: context_only
  snapshot_sha256: 10c11ac6d2714eac827c80c60bc1ba18b04b99764a7843623b43ec37b9c893c5
  search_scope: Europe PMC REST; query=DOI:"10.26508/lsa.202000824" OR DOI:"10.1186/s12915-015-0149-x"
    OR DOI:"10.1016/j.cub.2020.01.054" OR DOI:"10.1038/s41467-025-56049-9"&format=json&resultType=core&pageSize=100;
    accessed 2026-11-03T06:14:17.487074Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-linc-agent-2012-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%2210.1016/j.cub.2012.02.042%22&format=json&resultType=core
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:17.761081Z'
  summary: 'Identity cross-check: 22425159 10.1016/j.cub.2012.02.042 Transient structure
    associated with the spindle pole body directs meiotic microtubule reorganization
    in S. pombe.. No whole-body claim from metadata.'
  support: context_only
  snapshot_sha256: cb2a9bbadec30edf9cbc7db3fb875967aa30edf57b4c38969fe751991a94be54
  search_scope: Europe PMC REST; query=DOI:"10.1016/j.cub.2012.02.042"&format=json&resultType=core;
    accessed 2026-11-03T06:14:17.761081Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-linc-agent-chikashige2006-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/S0092867406003187?httpAccept=text/xml
  locator: Entire 1953-byte XML response
  accessed_at: '2026-11-03T06:14:17.935637Z'
  summary: Fresh HTTP200 is coredata-only metadata with no article body. It does not
    extend the Chikashige2006 primary-abstract evidence to Methods or figures; an
    open-access flag is not itself body retrieval.
  support: context_only
  snapshot_sha256: 27c2e01cb879e50c3450a2143481c0fcb9f545b956a5caf4b957e2fe94046d95
- evidence_id: plaque-linc-agent-fan2020-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7536833.1/PMC7536833.1.xml
  locator: Introduction s1; Results s3–s5, first s6 paragraph and selected next paragraph,
    full s7–s9; Discussion s10; Methods s12–s18 and displayed main captions. No complete
    supplementary/raw dataset or image analysis.
  accessed_at: '2026-11-03T06:14:17.980916Z'
  summary: Fan2020 directly studies budding-yeast Mps2–Mps3–Csm4, with SK1 meiotic
    and S288C mitotic experiments. Mps2 depletion/csm4 loss affect Rap1 clustering,
    delay LYS4 pairing and reduce ARG4/HIS4 conversion; ectopic Csm4/Ndj1 provides
    mitotic reconstitution. Proposed nonamer and direct cytoskeletal interactions
    remain models. These are not Sad1–Kms1 experiments.
  support: partial
  snapshot_sha256: 0013a1fcdd1d7b85b83d74900747997300119411c46cc5a932d59d25f75db9c0
- evidence_id: plaque-linc-agent-amelina2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4660835.1/PMC4660835.1.xml
  locator: Results Sec5/Sec6 including integrated Figures3/4 captions; Discussion
    Sec7; Methods Sec10–Sec12. No deposited raw mass spectra reanalysis.
  accessed_at: '2026-11-03T06:14:18.276448Z'
  summary: Amelina2015 finds Rap1 DD337AA loses Bqt1/2 interaction and meiotic clustering
    while preserving other tested interactions. Phosphomimetic/nonphosphorylatable
    clusters do not support a simple hyperphosphorylation switch. Bqt2-Bqt1 fusion
    is used in two-hybrid assays; pat1-114 synchronization differs from homothallic
    live-cell assays. Supports connector function, not detailed stoichiometric or
    core-LINC removal/reconstitution proof.
  support: partial
  snapshot_sha256: 928c024c3338595e5fe589c9d3c9174f03bdccf5c75eb89648eca6459a5d4112
- evidence_id: plaque-linc-agent-yoshida2013-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3575533.1/PMC3575533.1.xml
  locator: Results/discussion first12 paragraphs (telocentrosome recruitment and motor
    model); Methods Strains/media, Kms2 visualization, zygotic clustering, mat-induced
    haploid meiosis/MBC, live-cell imaging.
  accessed_at: '2026-11-03T06:14:18.321657Z'
  summary: Yoshida2013 observes Kms1/Kms2 at meiotic telocentrosomes and Kms1-dependent
    Dlc1/Mto1/Alp4 recruitment. Microtubule recovery and motor perturbations support
    clustering, but detailed cross-linking/transport remains a model and kinesins
    also contribute. Distinct 25 C zygotic, 30 C haploid-induction and 25–27 C imaging
    conditions are retained.
  support: partial
  snapshot_sha256: 0f228ac437c8af6f3d9edc0552d70b3b15a670714423cd3d32e094ec0cc4e274
- evidence_id: plaque-linc-agent-swartz2014-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4142617.1/PMC4142617.1.xml
  locator: Results induced site-specific DSBs, Sad1 complexes, Sad1 colocalization,
    Kms1 promotes gene conversion; Discussion both titled subsections; Methods culture,
    HO induction and repair-pathway assay.
  accessed_at: '2026-11-03T06:14:18.461252Z'
  summary: Swartz2014 supports the exact Sad1–Kms1 DSB-repair identity in S/G2 fission
    yeast. Loss of Kms1 changes repair-pathway choice while DSB-Sad1 association can
    persist. No Kms2 increase is detected at MMS foci, but possible redundancy or
    undetected low-copy roles remain explicit. Figure6 repair mechanisms are proposed.
    This is separate from meiotic budding-yeast conversion assays.
  support: partial
  snapshot_sha256: 96757e335f80ab5d8d85587382e5be1bd0c74a00689ca413aeaa4598600d595e
- evidence_id: plaque-linc-agent-dsb-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:24943839%20OR%20EXT_ID:24947240&format=json&resultType=core&pageSize=100
  locator: Returned DOI/PMID/title metadata; abstractText only where explicitly described
    in this summary
  accessed_at: '2026-11-03T06:14:18.484915Z'
  summary: 'Identity cross-check: 24947240 10.1016/b978-0-12-397920-9.00004-4 LINC
    complex proteins in development and disease.; 24943839 10.1091/mbc.e13-10-0569
    A role for nuclear envelope-bridging complexes in homology-directed repair.. No
    whole-body claim from metadata.'
  support: context_only
  snapshot_sha256: 652eaea9793d433a60aeb00473fccfd8a223373d4595ef9e587249152a277ec5
  search_scope: Europe PMC REST; query=EXT_ID:24943839 OR EXT_ID:24947240&format=json&resultType=core&pageSize=100;
    accessed 2026-11-03T06:14:18.484915Z; only returned DOI/PMID matches, no broad
    literature-absence inference.
- evidence_id: plaque-adapter-catalogue
  kind: search
  reference: https://imodulondb.org/api/datasets
  locator: Entire current native catalogue, all organism/dataset keys
  accessed_at: '2026-11-03T06:14:18.724993Z'
  summary: Fresh read-only source fallback lists 20 organisms and 28 datasets, all
    bacteria/archaea. No Saccharomyces, Schizosaccharomyces or other fungal/eukaryotic
    matching dataset occurs in this returned catalogue. No matching downstream gene/module
    search is applicable; absence is not negative biological evidence. This is not
    execution of the shared adapter runner.
  support: context_only
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  search_scope: iModulonDB native /api/datasets; complete returned catalogue; query
    matching target fungal species/strains and stated molecular genes; accessed 2026-11-03T06:14:18.724993Z;
    bounded to listed datasets, no claim about unpublished/external modules.
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/cytoskeleton/endocytic_patch.yaml
  locator: Entire current maintained record at 05425cc7089baf8133399baaf1ec24c00c661de3
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: Full current record read, including components, exact examples, taxonomic/function
    scope, all graph nodes/edges and history. Unchanged against original frozen target.
  support: context_only
  snapshot_sha256: 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd
- evidence_id: plaque-current-4
  kind: record_content
  reference: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  locator: Entire current maintained record at 05425cc7089baf8133399baaf1ec24c00c661de3
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: 'Full current record read, including components, exact examples, taxonomic/function
    scope, all graph nodes/edges and history. Substantively refreshed Bqt1–Bqt2 type
    change to PROTEIN_COMPLEX and #2420 history; other scientific fields unchanged.'
  support: context_only
  snapshot_sha256: b88b24ae10c1c8ceb36cb1489992fabe20600bff7e85e71a9fd3048d02e15b00
- evidence_id: plaque-current-5
  kind: record_content
  reference: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  locator: Entire current maintained record at 05425cc7089baf8133399baaf1ec24c00c661de3
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: 'Full current record read, including components, exact examples, taxonomic/function
    scope, all graph nodes/edges and history. Substantively refreshed Bqt1–Bqt2 type
    change to PROTEIN_COMPLEX and #2420 history; other scientific fields unchanged.'
  support: context_only
  snapshot_sha256: 4bf976f7c39fe18c961e155a1e4304153986b271209d2d35aa520a8406c03c65
- evidence_id: plaque-graph-contract
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and completion; native graph rules
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: Native policy distinguishes source-bounded causal explanation from membership/function
    summaries and requires honest uncertainty.
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: ComponentTypeEnum, component essentiality and CausalGraphScopeEnum
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: PROTEIN_COMPLEX represents named subcomplexes of distinct proteins; assembly
    necessity differs from viability/function. GENE_OR_PROTEIN graph coverage is not
    proof of molecular mechanism.
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-category-context
  kind: record_content
  reference: reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml
  locator: F1 exact issue_key, seven affected targets and two assigned Bqt connector
    fields
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: The earlier multi-target finding cytoskeleton-subcomplex-component-types
    includes these two current Bqt rows. Only their corrected fields were reassessed;
    this review does not terminally dispose of the whole seven-target predecessor.
  support: context_only
  snapshot_sha256: ffd4b4cf845f8a4ec0d7806c62152b0e92be5620b6a1373a9e7b292349474def
- evidence_id: plaque-adapter-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: Named genes/proteins trigger actual catalogue applicability review even
    without an expression-module claim. Unavailable runner execution remains distinct
    from source fallback.
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-historical-2420
  kind: authority
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2420
  locator: Root-fetched issue JSON body/state and resolution comment reread at current
    access time
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: 'Issue #2420 is CLOSED and explicitly covers the assigned Bqt component
    types. Comment identifies prior commit99e590eb. This is historical correction
    context; no credit to PR2353 and no terminal multi-target scientific disposition.'
  support: context_only
  snapshot_sha256: f459573d3815b7672af3a500c41e272d14c3c4fa07951d6e9fa74a97f4ebc57c
- evidence_id: plaque-original-native-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-plaque/original-validation.json
  locator: Three native validation/render receipts and fourteen source-input hashes
    per original
  accessed_at: '2026-11-03T06:18:39.183703Z'
  summary: All three originals validate with exit0, render byte-exact Markdown and
    match all14 historical input hashes each. Two current targets are stale only for
    the documented component type/history deltas.
  support: supports
  snapshot_sha256: 197058d9d7d4249caefd2169cd3f14266b8c64f962104bdc1892cd92526d0d24
- evidence_id: plaque-native-endocytic_patch-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/endocytic_patch.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/endocytic_patch-uniprot-verify.log;
    complete root-owned receipt and stdout independently read/hash-verified
  accessed_at: '2026-11-03T06:13:47.563728Z'
  summary: Exit0 at exact source head. all UniProtKB protein_examples and causal_graphs
    xrefs verified ok
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-endocytic_patch-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/endocytic_patch.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/endocytic_patch-uniprot-causal.log;
    complete root-owned receipt and stdout independently read/hash-verified
  accessed_at: '2026-11-03T06:13:48.032787Z'
  summary: "Exit0 at exact source head. data/structures/cytoskeleton/endocytic_patch.yaml\
    \  (GO:0061645)\n  endocytic_patch_mechanism\tactin\tCOVERED\t->actin (UniProtKB:P60010)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  support: supports
  snapshot_sha256: 5133cc11efe9a1d82763f342d094e8782b68b0251358b40294d9d88ca0a6fd26
- evidence_id: plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/meiotic_nuclear_membrane_microtubule_tethering_complex-uniprot-verify.log;
    complete root-owned receipt and stdout independently read/hash-verified
  accessed_at: '2026-11-03T06:13:55.068044Z'
  summary: Exit0 at exact source head. all UniProtKB protein_examples and causal_graphs
    xrefs verified ok
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/meiotic_nuclear_membrane_microtubule_tethering_complex-uniprot-causal.log;
    complete root-owned receipt and stdout independently read/hash-verified
  accessed_at: '2026-11-03T06:13:55.539296Z'
  summary: "Exit0 at exact source head. data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml\
    \  (GO:0034993)\n  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism\t\
    sad1_sun_protein\tCOVERED\t->sad1_sun_protein (UniProtKB:Q09825)\n  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism\t\
    kms1_kash_protein\tCOVERED\t->kms1_kash_protein (UniProtKB:P87245)\n  meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism\t\
    bqt1_bqt2_meiotic_connector\tCOVERED\t->bqt1_bqt2_meiotic_connector (UniProtKB:Q92358,\
    \ UniProtKB:Q9US52)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  support: supports
  snapshot_sha256: addf76366f950d0c7e95a3a7a7ceeb1985f206c317d1360884964f7376c472f9
- evidence_id: plaque-native-sad1_kms1_linc_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/sad1_kms1_linc_complex-uniprot-verify.log;
    complete root-owned receipt and stdout independently read/hash-verified
  accessed_at: '2026-11-03T06:13:56.976661Z'
  summary: Exit0 at exact source head. all UniProtKB protein_examples and causal_graphs
    xrefs verified ok
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-sad1_kms1_linc_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/sad1_kms1_linc_complex-uniprot-causal.log;
    complete root-owned receipt and stdout independently read/hash-verified
  accessed_at: '2026-11-03T06:13:57.424712Z'
  summary: "Exit0 at exact source head. data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml\
    \  (GO:1990612)\n  sad1_kms1_linc_complex_mechanism\tsad1_sun_protein\tCOVERED\t\
    ->sad1_sun_protein (UniProtKB:Q09825)\n  sad1_kms1_linc_complex_mechanism\tkms1_kash_protein\t\
    COVERED\t->kms1_kash_protein (UniProtKB:P87245)\n  sad1_kms1_linc_complex_mechanism\t\
    bqt1_bqt2_meiotic_connector\tCOVERED\t->bqt1_bqt2_meiotic_connector (UniProtKB:Q92358,\
    \ UniProtKB:Q9US52)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  support: supports
  snapshot_sha256: f7904ee0c4b1bcdcbd512a8673dee9e3c7dd3e97c6ad16dc0b8734af0bbca87d
- evidence_id: micro-record-gamma_tubulin_complex
  kind: record_content
  reference: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
  locator: Entire current maintained YAML; definition, components, protein examples,
    functions, every graph edge and appended curation history.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Personally inspected full current record and original-to-main delta. Target
    is PROPOSED. Protein additions and grouped component types are reassessed below;
    no scientific record edit is proposed within this PR.
  support: supports
  snapshot_sha256: 99fd52614b713f1cc678720626553f27f33f5cc4ee0d43b6adfe22108687798d
- evidence_id: micro-prior-gamma_tubulin_complex
  kind: prior_review
  reference: reviews/structured/20261021T094810Z-gamma-tubulin-complex-audit/review.yaml
  locator: Original complete review, scientific findings F1 and F2, checks, source
    inputs, assessments, actions, limitations; paired Markdown roundtrip verified.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Immutable historical needs_curation review has two open findings. Its target
    hash correctly matches the historical source revision but is stale against current
    main. Both exact predecessor occurrences are retained in this successor.
  support: supports
  snapshot_sha256: 21beb5c2956b53e551425105995532ea276f8a33ddbcd98f0d06321d9ee9beb7
- evidence_id: micro-record-gamma_tubulin_ring_complex
  kind: record_content
  reference: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
  locator: Entire current maintained YAML; definition, components, protein examples,
    functions, every graph edge and appended curation history.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Personally inspected full current record and original-to-main delta. Target
    is PROPOSED. Protein additions and grouped component types are reassessed below;
    no scientific record edit is proposed within this PR.
  support: supports
  snapshot_sha256: d8eb02a102133174291f4bdbcf09e2d2dfacdc46b217bea636a9bf598ff3d626
- evidence_id: micro-prior-gamma_tubulin_ring_complex
  kind: prior_review
  reference: reviews/structured/20261021T094812Z-gamma-tubulin-ring-complex-audit/review.yaml
  locator: Original complete review, scientific findings F1 and F2, checks, source
    inputs, assessments, actions, limitations; paired Markdown roundtrip verified.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Immutable historical needs_curation review has two open findings. Its target
    hash correctly matches the historical source revision but is stale against current
    main. Both exact predecessor occurrences are retained in this successor.
  support: supports
  snapshot_sha256: ab4ec6bfed90f6c65a3f46da69f9ca28af5fe31fda16b7503e2ddda01aaca84a
- evidence_id: micro-record-gamma_tubulin_small_complex
  kind: record_content
  reference: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
  locator: Entire current maintained YAML; definition, components, protein examples,
    functions, every graph edge and appended curation history.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Personally inspected full current record and original-to-main delta. Target
    is PROPOSED. Protein additions and grouped component types are reassessed below;
    no scientific record edit is proposed within this PR.
  support: supports
  snapshot_sha256: 231626322f95f06e53ca5d2dcff46f9227d686cd3e73dcfd2e5d99696121f7c3
- evidence_id: micro-prior-gamma_tubulin_small_complex
  kind: prior_review
  reference: reviews/structured/20261021T094813Z-gamma-tubulin-small-complex-audit/review.yaml
  locator: Original complete review, scientific findings F1 and F2, checks, source
    inputs, assessments, actions, limitations; paired Markdown roundtrip verified.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Immutable historical needs_curation review has two open findings. Its target
    hash correctly matches the historical source revision but is stale against current
    main. Both exact predecessor occurrences are retained in this successor.
  support: supports
  snapshot_sha256: 39313060aab0aece37d3ab4b8c6ea64ecb311be347c19e82ebafb862b8d974a6
- evidence_id: micro-stale-proof
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-microtubule/stale-input-proof.json
  locator: All three historical git-show inputs, native frozen hashes, current working
    bytes and exact current-main bytes.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: All three historical hashes match their actual source commit 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
    All three current target files equal the current main bytes and differ from those
    frozen originals. The refresh reassesses the protein, type and evidence deltas
    rather than replacing hashes alone.
  support: supports
  snapshot_sha256: 2a3adb2b760e6d15d32155ab75f04de9a3d39d0b3611f5d98a38269bc657eaa9
- evidence_id: micro-original-roundtrip
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-microtubule/original-validation.json
  locator: Actual validate and render --content invocations for all three original
    YAMLs; compare emitted Markdown bytes with committed pairs.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Each native validate exited zero; each native renderer exited zero and
    reproduced its historical Markdown exactly. A schema/render pass is not a scientific
    pass.
  support: supports
  snapshot_sha256: 8df939a18273bf97480980db15f2c43fde8de0a9eaa963736cf380befda74354
- evidence_id: micro-review-policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks; Evidence Rules; missing-things search contract.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Named genes and UniProt accessions trigger structured-source applicability.
    Lack of an expression claim is not an exemption. If the runner is unavailable,
    inspected official source pages are permitted; absence of a matched dataset is
    not biological negative evidence.
  support: supports
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-config
  kind: record_content
  reference: conf/record_review.yaml
  locator: Complete active routes and local rubric list.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Native configuration and profile were read; this is a read-only scientific
    record review, with issue-bearing batch synthesis owned by the parent reviewer.
  support: supports
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: micro-graph-rubric
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Native graph identity, causal path, membership versus mechanism and scope
    requirements.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Accession resolution and component_ref coverage do not themselves prove
    assembly necessity or mechanistic edges. Broad category findings cannot be retired
    using a partial cohort.
  support: supports
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-native-checklist
  kind: record_content
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: All field-by-field audit rows and evidence standard.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Component identity, assembly necessity, experimental localization, function
    and taxonomic distribution are assessed separately. Optional omissions and acknowledged
    scientific uncertainty do not alone justify findings.
  support: supports
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000930,GO:0000931,GO:0008275,GO:0005815,GO:0005816,GO:0032991,GO:0000923,GO:0051418
  locator: All eight exact GO id/name/definition/synonym objects and returned parent-child
    relations.
  accessed_at: '2026-11-03T06:15:56.059415Z'
  summary: Active GO:0000930, GO:0000931 and GO:0008275 denote the generic, ring and
    small complexes respectively. Small and ring are narrower gamma-complex classes;
    GO:0005815 is an MTOC context and GO:0005816 is fungal SPB. Native definitions
    support conserved membership and species-dependent complexity, not the appended
    numerical ring geometry or Mto1 allostery. GO:0000923 and GO:0051418 are equatorial-MTOC
    and MTOC-mediated nucleation context.
  support: supports
  snapshot_sha256: 344f654b01cb201f9ef82ede64e3d830928d6e5b2a4e96890d9448b76e36756b
- evidence_id: micro-taxon-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Exact taxId, scientificName and rank fields.
  accessed_at: '2026-11-03T06:15:54.069722Z'
  summary: Eukaryota taxon identity matches; this lookup does not establish universal
    biological distribution.
  support: supports
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: micro-taxon-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: Exact taxId, scientificName and rank fields.
  accessed_at: '2026-11-03T06:15:54.860489Z'
  summary: Schizosaccharomyces pombe 972h- reference strain matches. Sequence-example
    identity is not a claim that the cited experiment used the exact reference stock.
  support: supports
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: micro-taxon-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: Exact taxId, scientificName and rank fields.
  accessed_at: '2026-11-03T06:15:54.925260Z'
  summary: Schizosaccharomyces pombe species identity matches the ring canonical example.
  support: supports
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: micro-taxon-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId, scientificName and rank fields.
  accessed_at: '2026-11-03T06:15:55.270533Z'
  summary: Saccharomyces cerevisiae S288C reference strain matches new budding-yeast
    protein examples; literature species context does not itself identify an experimental
    stock.
  support: supports
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro-interpro
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002454/
  locator: IPR002454 metadata name/type and description.
  accessed_at: '2026-11-03T06:15:56.183743Z'
  summary: IPR002454 is the Gamma tubulin family. An optional family grounding is
    not invented for the mixed GCP2/GCP3 group, and failure to include an optional
    family field is not treated as a defect.
  support: supports
  snapshot_sha256: 0cc07ff810e7acb2b8d24c24597c1bcabf177adb7e06ae6ddfabbb352fe0c668
- evidence_id: micro-uniprot-P25295
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25295.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.172238Z'
  summary: P25295 is reviewed Swiss-Prot Tubulin gamma chain, gene gtb1, taxon 284812.
    The gtb1/tug1 SPBC32F12.04 entry is gamma tubulin, disambiguated from glucosidase
    Q9USH8. Identity/annotation provenance is distinguished from direct evidence of
    structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: 6c5e36578b9bdda0edebd4bb5352c22762aacb10b0ce93a9d5fb45fa7ac39dcf
- evidence_id: micro-uniprot-Q9USH8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9USH8.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.172383Z'
  summary: Q9USH8 is reviewed Swiss-Prot Glucosidase 2 subunit beta, gene gtb1, taxon
    284812. This second reviewed gtb1 is ER glucosidase 2 beta, confirming why symbol-only
    resolution is unsafe. It is not a record component. Identity/annotation provenance
    is distinguished from direct evidence of structural membership, stoichiometry
    or assembly necessity.
  support: supports
  snapshot_sha256: cb7cd5f368001d01c48dda1c059ef3e357d038aa3f606482c359baa0a64eface
- evidence_id: micro-uniprot-P53378
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53378.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.377368Z'
  summary: P53378 is reviewed Swiss-Prot Tubulin gamma chain, gene TUB4, taxon 559292.  Identity/annotation
    provenance is distinguished from direct evidence of structural membership, stoichiometry
    or assembly necessity.
  support: supports
  snapshot_sha256: 59410679589d6fbf2d9568a85d3e5f9a5b0f032f422d79e4272bd82e9bc7fde5
- evidence_id: micro-uniprot-Q9Y705
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9Y705.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.379747Z'
  summary: Q9Y705 is reviewed Swiss-Prot Spindle pole body component alp4, gene alp4,
    taxon 284812.  Identity/annotation provenance is distinguished from direct evidence
    of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: 1735b88bbff6bce84e252460f2f8e64bb72fbe3901bd81b9f1db63cba4d23682
- evidence_id: micro-uniprot-Q9USQ2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9USQ2.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.479440Z'
  summary: Q9USQ2 is reviewed Swiss-Prot Spindle pole body component alp6, gene alp6,
    taxon 284812. SPB-location evidence explicitly cites ECO:0000269 PMID11080156.
    Identity/annotation provenance is distinguished from direct evidence of structural
    membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: c2f6a49f8a991fcbd3154ffe9e6d82bbc66e8f5e9b3e72de9dd84e517e97267a
- evidence_id: micro-uniprot-P38863
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38863.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.479575Z'
  summary: P38863 is reviewed Swiss-Prot Spindle pole body component SPC97, gene SPC97,
    taxon 559292.  Identity/annotation provenance is distinguished from direct evidence
    of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: 0cb7bd3da10057e604291058a5948f03e77929eb877301a620cc5d4070a47b06
- evidence_id: micro-uniprot-P53540
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53540.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:51.994078Z'
  summary: P53540 is reviewed Swiss-Prot Spindle pole body component SPC98, gene SPC98,
    taxon 559292.  Identity/annotation provenance is distinguished from direct evidence
    of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: 578c9c305721c265d1181a201d9fa40b95529ff5197991beae0d7e36dcc4cf6a
- evidence_id: micro-uniprot-Q9P7R5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9P7R5.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:52.019438Z'
  summary: Q9P7R5 is reviewed Swiss-Prot Gamma-tubulin complex component gfh1, gene
    gfh1, taxon 284812. SPB-location provenance cites ECO:0000269 PMID15004232 and
    PMID16823372. Identity/annotation provenance is distinguished from direct evidence
    of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: 26ca7112188bb2c14b063a27304e5047dab964a37eefb8291c19c9ae62d43323
- evidence_id: micro-uniprot-Q9UT52
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9UT52.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:52.094913Z'
  summary: Q9UT52 is reviewed Swiss-Prot Gamma-tubulin complex subunit mod21, gene
    mod21, taxon 284812. SPB-location provenance cites ECO:0000269 PMID16823372 and
    PMID17021256. Identity/annotation provenance is distinguished from direct evidence
    of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: a0b73c296c727df6d9146dab519bb90732a3ccba154a4de2cf039a0e146a2d19
- evidence_id: micro-uniprot-P87244
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P87244.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:52.954186Z'
  summary: P87244 is reviewed Swiss-Prot Spindle pole body component alp16, gene alp16,
    taxon 284812. SPB-location provenance cites ECO:0000269 PMID12134075. Identity/annotation
    provenance is distinguished from direct evidence of structural membership, stoichiometry
    or assembly necessity.
  support: supports
  snapshot_sha256: 38957c9fb8aacd05f8cfbd7af42973729be7de329284107b0e91cc7f84af9bcb
- evidence_id: micro-uniprot-O94488
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O94488.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:52.996104Z'
  summary: O94488 is reviewed Swiss-Prot Gamma tubulin complex adapter mto1, gene
    mto1, taxon 284812.  Identity/annotation provenance is distinguished from direct
    evidence of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: 4903509b256bf5164ea7e5b80970bbb89056a71a4ea4a257e9feb8adcaf0e46b
- evidence_id: micro-uniprot-Q9USP7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9USP7.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; subcellular-location
    evidence references.
  accessed_at: '2026-11-03T06:15:54.051118Z'
  summary: Q9USP7 is reviewed Swiss-Prot Gamma tubulin complex adapter mto2, gene
    mto2, taxon 284812.  Identity/annotation provenance is distinguished from direct
    evidence of structural membership, stoichiometry or assembly necessity.
  support: supports
  snapshot_sha256: ae275cdd142bdffa04ce4e120465b57fbd20dbe1223de0be9a72966ec6e40698
- evidence_id: micro-named-proteins-284812
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28organism_id%3A284812%29+AND+%28gene_exact%3Agtb1+OR+gene_exact%3Aalp4+OR+gene_exact%3Aalp6+OR+gene_exact%3Agfh1+OR+gene_exact%3Amod21+OR+gene_exact%3Aalp16+OR+gene_exact%3Amzt1+OR+gene_exact%3Amto1+OR+gene_exact%3Amto2%29&format=json&size=500
  locator: Every returned entry accession, own primary gene/synonyms/locus and source
    taxon; response total and pagination headers.
  accessed_at: '2026-11-03T06:15:56.394844Z'
  summary: All nine named fission-yeast symbol classes are represented within eleven
    reviewed results, including two distinct gtb1 and two mto1 entries. Existing declared
    O94488/P25295 identities are checked by full entries rather than picking a homonym.
  support: supports
  snapshot_sha256: 7716f6a0b85dad9860acd4865cb4f1fbb26d7dc8b458dc48cf64b394948985c9
  search_scope: UniProtKB search accessed 2026-11-03T06:15:56.394844+00:00; reviewed:true
    AND organism_id:284812 AND OR of gene_exact terms gtb1, alp4, alp6, gfh1, mod21,
    alp16, mzt1, mto1, mto2; format=json, size=500. Returned 11 entries, X-Total-Results=11,
    no next-page Link. Only these named genes and this taxon/status are covered; no
    whole-proteome or universal absence conclusion.
- evidence_id: micro-named-proteins-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28reviewed%3Atrue%29+AND+%28organism_id%3A559292%29+AND+%28gene_exact%3ATUB4+OR+gene_exact%3ASPC97+OR+gene_exact%3ASPC98%29&format=json&size=500
  locator: Every returned entry accession, own primary gene/synonyms/locus and source
    taxon; response total and pagination headers.
  accessed_at: '2026-11-03T06:15:56.394945Z'
  summary: The bounded budding-yeast query returns exactly P53378/TUB4, P38863/SPC97
    and P53540/SPC98, supporting the record’s reviewed-accession identity claims at
    this query scope.
  support: supports
  snapshot_sha256: 851a912998ee5daab10c39509fa3001555f8b673252e3bc758e2be0d5d533d45
  search_scope: UniProtKB search accessed 2026-11-03T06:15:56.394945+00:00; reviewed:true
    AND organism_id:559292 AND OR of gene_exact terms TUB4, SPC97, SPC98; format=json,
    size=500. Returned 3 entries, X-Total-Results=3, no next-page Link. Only these
    named genes and this taxon/status are covered; no whole-proteome or universal
    absence conclusion.
- evidence_id: micro-new-europepmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&pageSize=100&query=EXT_ID%3A11080156+OR+EXT_ID%3A15004232+OR+EXT_ID%3A16823372+OR+EXT_ID%3A17021256+OR+EXT_ID%3A12134075+OR+EXT_ID%3A15068790+OR+DOI%3A%2210.1146%2Fannurev.cellbio.20.022003.114106%22
  locator: 'Seven exact matching results: PMID11080156/15004232/16823372/17021256/12134075/15068790
    and Jaspersen/Winey DOI, including titles, author lists and abstractText.'
  accessed_at: '2026-11-03T06:15:56.293160Z'
  summary: The new PMID citations resolve to Vardy/Toda2000, Venkatram2004, Matsuyama2006,
    Anders2006 and Fujita2002. Matsuyama ORFeome survey and Zimmerman2004 are credited
    only at metadata/abstract tier in this review; no individual image, ORFeome table
    or full Zimmerman body was inspected. Jaspersen/Winey2004 is a secondary review,
    with separately inspected browser text.
  support: supports
  snapshot_sha256: a60abd420c72205a8a92a0d2be98806a5d9b7a6746b24374464e8263e488d6af
- evidence_id: micro-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: Introduction P2–P3, Results integrative SPB-core representation P27–P28
    and final composition P38; title/DOI/PMID.
  accessed_at: '2026-11-03T06:15:49.991186Z'
  summary: Viswanath2017 DOI10.1091/mbc.E17-06-0397 studies S. cerevisiae SPB core
    architecture involving Spc42, Spc29, Spc110, Cnm67 and Cmd1. Its Tub4 context
    does not establish fission-yeast Alp4/Alp6 composition or Mto1/Mto2-driven nucleation.
    This directly confirms the retained source-organism attribution defect.
  support: supports
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: micro-samejima2010
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2989437.1/PMC2989437.1.xml
  locator: Results MASC-targeting mutants P3–P8, Myp2/Alp4 eMTOC observations P8–P10,
    Sid4/Cdc11 P11–P15; Figure 1/3/4 captions.
  accessed_at: '2026-11-03T06:15:49.991484Z'
  summary: Primary S. pombe targeting experiments separate interphase/mitotic SPBs
    and equatorial MTOCs; Myp2 loss removes detected equatorial Alp4 and PAA nucleation.
    Recruitment and site-specific nucleation support the existing Alp4/Mto1 roles,
    with experimental context retained. The study does not establish 13/14-spoke ring
    geometry, a GCP4/5/6 seam or Mto1 allosteric ring closure.
  support: supports
  snapshot_sha256: 9337fd098562acbf278e8fa6b6fdb2bce9ed3f0ef1ed2bdd8cbe6d5f66e8edaa
- evidence_id: micro-samejima2008
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2743986.1/PMC2743986.1.xml
  locator: Results CM1 binding P5–P12; Mto1-334 and Mto2 deletion P15–P20; Discussion
    P23.
  accessed_at: '2026-11-03T06:15:49.991572Z'
  summary: CM1 mutants lose gamma-complex interaction without losing prospective-MTOC
    localization. Mto1-334 and mto2 deletion retain restricted SPB and very limited
    eMTOC nucleation; more sensitive detection reveals weak association. These are
    recruitment/interaction/activity endpoints rather than class-wide assembly-necessity
    measurements.
  support: supports
  snapshot_sha256: c495ac9e59ed63f5e88cc383575e83cfa34a9b0a3ffab09e30031f0520748075
- evidence_id: micro-lynch2014
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3989768.1/PMC3989768.1.xml
  locator: Results minimal Mto1/2-bonsai activation and copy numbers P7–P15; Conclusions
    P16.
  accessed_at: '2026-11-03T06:15:50.523940Z'
  summary: Fission-yeast bonsai complexes activate nucleation independently of targeting,
    with measured average Mto1/Mto2 and Alp4/Alp6 copy numbers supporting a gamma-TuRC-like
    inference. Mto2-dependent multimerization matters. The authors explicitly leave
    conformational activation unconfirmed and do not determine whether Mto1 CM1 alone
    activates; these data do not validate the record’s affirmative allosteric ring
    mechanism.
  support: supports
  snapshot_sha256: c79f01751fe2552986d4dc8ff9523ebf86ad6349f546520563c06c3bf32a323b
- evidence_id: micro-brilot2021
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC8099430.1/PMC8099430.1.xml
  locator: Introduction P3–P7 as cited context; primary cryo-EM/crystallography/XL-MS
    Results P20–P22 and P37–P42; CM1/Spc110 interfaces.
  accessed_at: '2026-11-03T06:15:50.524053Z'
  summary: Direct budding-yeast structures distinguish gamma-TuSC assembly states
    and resolve Spc110 contacts, including CM1 across an inter-TuSC interface. Species,
    recombinant/engineered preparation and open/closed state are essential bounds.
    Background metazoan ring comparisons are not new experiments on native S. pombe
    Gfh1/Mod21/Alp16.
  support: supports
  snapshot_sha256: 7937671cd050caa340f7deb2cf8aa17f286a7aa1039b78d93d39bd6eb09aebc0
- evidence_id: micro-lyon2016
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4945142.1/PMC4945142.1.xml
  locator: Introduction P0–P1; Discussion P27–P28; primary study of Spc110 oligomerization
    and gamma-TuRC assembly.
  accessed_at: '2026-11-03T06:15:50.524726Z'
  summary: Budding-yeast Spc110-dependent oligomerization and assembly are supported.
    The 13-position description involves seven TuSCs with half-TuSC overlap, and recruited
    versus assembled complexes must be separated. Background Spc72 homology is not
    direct evidence for identical receptor-dependent geometry throughout fungi.
  support: supports
  snapshot_sha256: 35a2cfa58d7408d012edf0e9874513f1342689af069476a05738e02a805d8793
- evidence_id: micro-bellingham2023
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10047812.1/PMC10047812.1.xml
  locator: Results P4–P7, Figure 1 timing, relative localization/intensity and PAA
    network; Methods/context.
  accessed_at: '2026-11-03T06:15:50.640486Z'
  summary: Live fission-yeast experiments support Myp2 then Mto1 then PAA recruitment
    timing. Mto1 enrichment inside Myp2 and the dosage experiment limit a simple direct-complex
    model. The source studies PAA organization/cytokinesis rather than gamma-ring
    molecular geometry. Figure captions/body were read; pixels were not independently
    reanalyzed.
  support: supports
  snapshot_sha256: 519b1918af37108acb4ae400b29e82b597cdc3e21480263bbf1041f17bf96521
- evidence_id: micro-florparra2018
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7263743.1/PMC7263743.1.xml
  locator: Abstract, Introduction P0–P4 and Results nucleation assays, Mto1-bonsai
    and Alp14/Alp7 recruitment context.
  accessed_at: '2026-11-03T06:15:50.764408Z'
  summary: Flor-Parra2018 separates Alp14-promoted nucleation from polymerization,
    including interphase Mto1-bonsai and recruitment assays. This is appropriate nucleation
    context but does not establish the asserted GCP4/5/6 seam or Mto1 allostery.
  support: supports
  snapshot_sha256: 5c6000e8b847fcdedb2b6d328d7a87e026432a1cb816daf6c5461f8cde76c9aa
- evidence_id: micro-masuda2013
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3771951.1/PMC3771951.1.xml
  locator: Results Mzt1 membership/localization and core pull-down P30–P31, Figure
    8; Discussion.
  accessed_at: '2026-11-03T06:15:50.868091Z'
  summary: Fission-yeast Mzt1 membership and MTOC recruitment are supported. Conditional
    mzt1 mutants at 36 C retain Alp4–gamma-tubulin core association despite localization
    defects. This separates core assembly from recruitment; it does not establish
    full native ring assembly or universal assembly-essentiality labels.
  support: supports
  snapshot_sha256: d613cfbffba6ee950211f12180cb1da7525f4e2a9ea4258c452deff4cc97c959
- evidence_id: micro-samejima2005
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1142446/?pdf=render
  locator: Title/DOI; Results P35–P36, P45, P47, P51–P58; Discussion P64–P67.
  accessed_at: '2026-11-03T06:16:25.673945Z'
  summary: DOI10.1091/mbc.E04-11-1003 is Samejima et al.2005, a study of Mto2/Mto1
    interaction, recruitment and residual PAA activity. The body explicitly presents
    a possible allosteric role as speculation. It does not characterize Gfh1/Mod21/Alp16
    as a 14-spoke seam. Source identity is taken from the paper, not from an old retrieval
    filename.
  support: supports
  snapshot_sha256: 32980f1ae1933ac08cd664efbe23728a3a3975ef350ae7a20105c1a6174f4a66
- evidence_id: micro-venkatram2005
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1142447/?pdf=render
  locator: Results P33, P39, P43, P46–P47; Discussion P50 and P56–P57.
  accessed_at: '2026-11-03T06:16:25.674245Z'
  summary: Distinct DOI10.1091/mbc.E04-12-1043 reports stronger eMTOC/PAA defects
    and actin-ring anchoring during cps1 arrest or low-dose LatA cytokinesis delay.
    These preparation-specific results are retained alongside Samejima’s residual
    activity, rather than used to erase it or infer universal ring-assembly necessity.
  support: supports
  snapshot_sha256: cc339129a749a0971eaf2d1af87380f726fee38ae7b916ae14b40b9a3d4c6b69
- evidence_id: micro-anders2006
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1679674/?pdf=render
  locator: Results P26–P33 and Figure 2 Mod21/Gfh1 association/localization; sucrose-gradient
    analysis P72–P78, Discussion.
  accessed_at: '2026-11-03T06:16:25.674343Z'
  summary: Mod21 is a bona fide fission-yeast gamma-complex member with Alp4/Alp6
    coassociation and SPB/eMTOC localization. Gfh1/Mod21/Alp16 are facultative noncore
    proteins affecting nucleation efficiency. Sedimentation and association depend
    on preparation and leave native large-complex architecture uncertain; they do
    not reconstruct a 14-spoke seam.
  support: supports
  snapshot_sha256: 6eb1a89b4e748cec557eb7c2dc14ba7260e77db766854674f1e4f2899d3a8844
- evidence_id: micro-pmid-11080156
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC305819/?pdf=render
  locator: Vardy/Toda2000 Results P20 and P22–P26, Figure 1/2.
  accessed_at: '2026-11-03T06:17:40.393918Z'
  summary: GFP and HA-tagged Alp4/Alp6 localize to SPB/equatorial MTOC and coimmunoprecipitate
    Gtb1 in S. pombe. This directly supports the new Alp6 localization citation, separately
    from UniProt’s ECO annotation; mutant phenotypes do not by themselves establish
    class-wide assembly necessity.
  support: supports
  snapshot_sha256: 3950afad8032728829669eda467b45589e797ed4433470fc10d0572ad4792a66
- evidence_id: micro-pmid-15004232
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC404023/?pdf=render
  locator: Venkatram2004 Results P23/P29 complex purification and P37–P38 GFP-Gfh1
    localization.
  accessed_at: '2026-11-03T06:17:40.394194Z'
  summary: Alp4/Alp6-TAP purification and mass spectrometry identify Gfh1/Mbo1; follow-up
    coimmunoprecipitation supports association. Gfh1 expressed under the low-strength
    nmt81 promoter localizes to SPB and faint medial eMTOC. This preparation supports
    the added Gfh1 citation without proving exact native ring geometry.
  support: supports
  snapshot_sha256: 4221b995e0398c42c3890f471a2aba84b3b37f986a845f87e5bc5bb09813cae2
- evidence_id: micro-pmid-12134075
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC117319/?pdf=render
  locator: Fujita2002 Results P30/P35 homology, P39–P44 interaction/fractionation/localization,
    Figure 4/5.
  accessed_at: '2026-11-03T06:17:40.394280Z'
  summary: Alp16 is related to GCP6, coimmunoprecipitates gamma tubulin and localizes
    to SPB/equatorial MTOC. Lower abundance required antibody-enhanced detection.
    Large-complex fractionation and variable stoichiometry are preparation-dependent,
    not a 14-spoke structural determination; viability, complex assembly and nucleation
    are separate endpoints.
  support: supports
  snapshot_sha256: 721327eb9311096732940c9d9c332d8ad5bd8cafd33d006aab88171f1a13eb2c
- evidence_id: micro-jaspersen-secondary
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author-uploaded manuscript browser rendering, pages 24–26, lines 978–1067;
    especially 1004–1022 and 1042–1051.
  accessed_at: '2026-11-03T06:17:28Z'
  summary: Secondary review supports budding-yeast Tub4/Spc97/Spc98 2:1:1 composition
    and attachment via Spc110 versus Spc72. It describes a recombinant small complex
    with low nucleation activity and treats capping as likely. Newly accessed browser
    rendering is cache-mediated (reported crawl three weeks earlier), with no HTTP-status
    receipt; it is not primary experimental evidence or an exact S288C stock verification.
  support: context_only
  snapshot_sha256: d96d7a050304ae4dfd22d8754df2e6bd55e7c9a07a66d00ca816fe292ab21724
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned 20 organism records and 28 dataset keys.
  accessed_at: '2026-11-03T06:15:56.089015Z'
  summary: The inspected official iModulonDB catalogue has no Schizosaccharomyces,
    Saccharomyces or other eukaryotic organism dataset. Named-gene applicability was
    assessed, but no target organism match permits a downstream gene/module search
    or summarize call. This is a catalogue-bounded not-applicable result, not evidence
    that gamma complexes or their genes are absent.
  support: supports
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual prior runner receipt, started_at/finished_at, exit_code
    and PermissionError.
  accessed_at: '2026-11-03T00:49:00.848907Z'
  summary: Earlier runner invocation at 2026-11-03T00:49:00Z failed with OS PermissionError
    for pyvenv.cfg. It is retained as historical unavailability, not a new execution
    or a passed adapter command. The fresh official catalogue response supplies fallback
    applicability evidence.
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-gamma_tubulin_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-verify-receipt.json
  accessed_at: '2026-11-03T06:13:49.372003Z'
  summary: Actual native command exited zero on the declared current head. All declared
    protein example and graph xref identities verified; this does not validate membership,
    stoichiometry or scientific mechanism.
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-gamma_tubulin_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_complex-uniprot-causal-receipt.json
  accessed_at: '2026-11-03T06:13:49.846566Z'
  summary: Actual native command exited zero on the declared current head. Both GENE_OR_PROTEIN
    causal nodes are COVERED by component examples; zero partial, missing-symbol,
    dangling or unanchored nodes in this diagnostic. This covers that node class only
    and is not a proof that the graph is mechanistic.
  support: supports
  snapshot_sha256: 715b089e24340024a26136fa88943d013355e8d4c4d5ce10af2659bcbad26dd2
- evidence_id: micro-native-gamma_tubulin_ring_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-verify-receipt.json
  accessed_at: '2026-11-03T06:13:51.057723Z'
  summary: Actual native command exited zero on the declared current head. All declared
    protein example and graph xref identities verified; this does not validate membership,
    stoichiometry or scientific mechanism.
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-gamma_tubulin_ring_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_ring_complex-uniprot-causal-receipt.json
  accessed_at: '2026-11-03T06:13:51.529463Z'
  summary: Actual native command exited zero on the declared current head. Both GENE_OR_PROTEIN
    causal nodes are COVERED by component examples; zero partial, missing-symbol,
    dangling or unanchored nodes in this diagnostic. This covers that node class only
    and is not a proof that the graph is mechanistic.
  support: supports
  snapshot_sha256: 104c1cd38e3514ecd0dcb6b81d2a10d06e84b26eeb7475dee9ecf6abc9a8e523
- evidence_id: micro-native-gamma_tubulin_small_complex-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-verify.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-verify-receipt.json
  accessed_at: '2026-11-03T06:13:52.571405Z'
  summary: Actual native command exited zero on the declared current head. All declared
    protein example and graph xref identities verified; this does not validate membership,
    stoichiometry or scientific mechanism.
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-gamma_tubulin_small_complex-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-causal.log;
    receipt /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/gamma_tubulin_small_complex-uniprot-causal-receipt.json
  accessed_at: '2026-11-03T06:13:53.053981Z'
  summary: Actual native command exited zero on the declared current head. Both GENE_OR_PROTEIN
    causal nodes are COVERED by component examples; zero partial, missing-symbol,
    dangling or unanchored nodes in this diagnostic. This covers that node class only
    and is not a proof that the graph is mechanistic.
  support: supports
  snapshot_sha256: 67ea4fd168da23ca1b4d2ae5fdcfbbdf4cf016ed1e4c935019b1789371c68799
- evidence_id: micro-category-20261023
  kind: prior_review
  reference: reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml
  locator: Exact F1 occurrence, issue_key, affected targets and component paths; bounded
    gamma-target comparison.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Category predecessor includes gamma targets plus out-of-slice records.
    The current gamma component types are corrected, but this three-record slice does
    not reassess every affected target and therefore makes no terminal disposition
    of the whole category finding.
  support: supports
  snapshot_sha256: ffd4b4cf845f8a4ec0d7806c62152b0e92be5620b6a1373a9e7b292349474def
- evidence_id: micro-category-20261025
  kind: prior_review
  reference: reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.yaml
  locator: Exact F1 occurrence, issue_key, affected targets and component paths; bounded
    gamma-target comparison.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Category predecessor includes gamma targets plus out-of-slice records.
    The current gamma component types are corrected, but this three-record slice does
    not reassess every affected target and therefore makes no terminal disposition
    of the whole category finding.
  support: supports
  snapshot_sha256: d34740ab1423ae3417a5a7ba665d7141ddfea865663a44c75aedfbc77b91d2a4
- evidence_id: micro-issue-2420
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2420
  locator: Parent-fetched issue JSON body/state and any returned comments; inspected
    at current review time. Snapshot is tracker context, not an authority for scientific
    claims.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Closed historical tracking context. Current gamma grouped components are
    PROTEIN_COMPLEX, consistent with the recorded scoped repair. No claim is made
    that all targets of this broader issue were newly reviewed here.
  support: context_only
  snapshot_sha256: f459573d3815b7672af3a500c41e272d14c3c4fa07951d6e9fa74a97f4ebc57c
- evidence_id: micro-issue-2431
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2431
  locator: Parent-fetched issue JSON body/state and any returned comments; inspected
    at current review time. Snapshot is tracker context, not an authority for scientific
    claims.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Closed historical tracking context. Current gamma grouped components are
    PROTEIN_COMPLEX, consistent with the recorded scoped repair. No claim is made
    that all targets of this broader issue were newly reviewed here.
  support: context_only
  snapshot_sha256: 7155eca384fb4358fa2a838567700660428fbfeaf08abd87ae01e8d175b21f48
- evidence_id: micro-issue-2470
  kind: prior_review
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2470
  locator: Parent-fetched issue JSON body/state and any returned comments; inspected
    at current review time. Snapshot is tracker context, not an authority for scientific
    claims.
  accessed_at: '2026-11-03T06:21:13.803669Z'
  summary: Closed historical tracking context. The added Jaspersen/Winey evidence
    is present for budding-yeast Spc97/Spc98. The issue body itself incorrectly calls
    Viswanath2017 a fission-yeast study; that wording is preserved as a limitation
    and does not establish that current source attribution is correct.
  support: context_only
  snapshot_sha256: 2230339177bc3fe879c1c810938014ae1b3e9e563351ec41d053b3daef93478a
- evidence_id: septin-septin-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031105,GO:0032156,GO:0032158,GO:0032160,GO:0032161,GO:0032165,GO:0032166
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:52.695761Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 83ea09e6a23c180ff2b82f59f3e4bae62b7ec9b4b609fea348b1d71111324cfa
- evidence_id: septin-septin-agent-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:52.696185Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
- evidence_id: septin-septin-agent-tax-5476
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:52.696273Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: fdba428d1e1abf55ec666204b7320749e8f16f798a55b771ec0f5af932e6ab71
- evidence_id: septin-septin-agent-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:52.696342Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-septin-agent-P32457
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32457.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:52.696429Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 7fc581a719d6b12f8611b58bfc0c11fc057c73e673b217485a3379b8330b6efe
- evidence_id: septin-septin-agent-query-CDC3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:53.441150Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: d15bf1b00b3f29538132111c0a6ab994f6bf134478224348f6857db31c1f4aee
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:53.441150Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-P25342
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P25342.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:53.466798Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 5a5194945989f266f18122a50805faa45f7bc00a599dcefcf7cf6592d753174d
- evidence_id: septin-septin-agent-query-CDC10
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC10%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:53.479149Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: f9b9dc13ffea60b8a6bfb9d653d7a4ede1157e95cf417161793bf122b409fa8c
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC10%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:53.479149Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-P32458
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32458.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:53.517958Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 839db168d3ac73f1e1718845d2d92024c8bd535a96081c789ff55a1a0e98c922
- evidence_id: septin-septin-agent-query-CDC11
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC11%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:53.683197Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 384fe6c570f5d6549a3469d520685905279ff9f0303a7f72da1f0d9399322fc5
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC11%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:53.683197Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-P32468
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P32468.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:54.369648Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 3a96072071fa02a2e65a0d5d80ebcf82c631ff8f674fc6ce5ae642b8b273619e
- evidence_id: septin-septin-agent-query-CDC12
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC12%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:54.386719Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 0096f0d783694af4a97eabab1e461dba9433f5de30a034cd6f25b0b667097721
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC12%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:54.386719Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-Q07657
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q07657.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:55.112301Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 4b3fa80abaa9782dee6cb8412786a5eed43b5df173dd4a150079a04064ec2627
- evidence_id: septin-septin-agent-query-SHS1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ASHS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:56.181441Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 0a077959f8d07e4292e2a3362dd78fb89992cf62800d84b1ad922eca984fd0c2
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ASHS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:56.181441Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-IPR016491
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:56.335484Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: septin-septin-agent-pmid-14562095
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14562095%20AND%20SRC%3AMED
  locator: Fresh Europe PMC exact PMID primary abstract and native UniProt location
    citation fields only.
  accessed_at: '2026-11-03T06:13:56.963452Z'
  support: supports
  summary: Huh2003 chromosomal GFP localization screen supports the source identity
    and cited native annotation; individual original image panels and full strain
    Methods not audited.
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14562095%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:56.963452Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-pmid-25971666
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A25971666%20AND%20SRC%3AMED
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:57.152786Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 8dadefe3e0b3f81cdecb97cda7b343839f33bc16e839803ce704c68b81969130
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A25971666%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:57.152786Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-pmid-9790978
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9790978%20AND%20SRC%3AMED
  locator: Fresh Europe PMC exact PMID primary abstract and native UniProt location
    citation fields only.
  accessed_at: '2026-11-03T06:13:57.572388Z'
  support: supports
  summary: Mino1998 abstract reports Shs1 bud-neck localization and Spa2 binding.
    The abstract does not supply a universal structural inventory or complete assembly
    necessity assay.
  snapshot_sha256: 0ae103e8941711a47963ad52135dcca92de0b2e7d6cc2e2390765db5ba4622f2
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9790978%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:57.572388Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-versele2005-correct-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16009555%20AND%20SRC%3AMED
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:57.774852Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: e357d697a9b677792c488a9a5c9aa2654f106e7bbf22b5c706aaf6fbb0c331e5
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16009555%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:57.774852Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-douglas2005-correct-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16151244%20AND%20SRC%3AMED
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:58.256651Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 63968511f9718fd6e5a4923b2c8911a3f8c346b6ff0692044577fabb8ea1c554
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16151244%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:58.256651Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-septin-agent-versele-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: 'Fresh native PMC secondary review HTML: Introduction/green-algal ortholog
    paragraph, septin complex overview and budding/fission yeast function/scaffold/barrier
    passages; no cited primary experiment or image reanalysis.'
  accessed_at: '2026-11-03T06:13:58.260592Z'
  support: supports
  summary: Green-algal septin ortholog occurrence does not establish the expanded
    plasma-membrane cortical architecture and recruitment functions across the full
    taxon/site list. Historical models are context, not fixed current rod stoichiometry.
    The five-gene list is interpreted as examples, not an ordered rod.
  snapshot_sha256: d9d5a66e42c7521c106eb60ce049d38298c17ae30c6aef9cd3ff9621ff0a5301
- evidence_id: septin-septin-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: 'Fresh native PMC secondary review HTML: introduction and septin-family
    overview, sporulation/prospore-wall paragraph, and Aspergillus nidulans subsection
    including developmental localization and scaffold proposals.'
  accessed_at: '2026-11-03T06:13:58.310646Z'
  support: supports
  summary: Spore-wall recruitment is proposed, and A. nidulans developmental scaffold/regulator
    recruitment is suggested from scoped phenotypes. These are not demonstrated cross-taxon
    universal mechanisms; broad septin cytoskeleton is not confined to its spore-array
    examples.
  snapshot_sha256: a83871622c7de84a9ccb02b47df62eea1c16d1f792b7e5517132cfa6e7f970bf
- evidence_id: septin-septin-agent-finnigan2015-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4512547/?pdf=render
  locator: 'Fresh native PMC primary HTML: abstract, relevant strain-construction
    Methods/Table1 context, Bni5 recruitment and subsequent Myo1 localization Results
    with Figure7 caption, and relevant CTE-binding Discussion passage. No full-body,
    supplement or image-pixel audit.'
  accessed_at: '2026-11-03T06:13:58.452729Z'
  support: supports
  summary: Vegetative S. cerevisiae Cdc11/Shs1 C-terminal contributions to Bni5/Myo1
    recruitment are directly studied. Deletion/truncation, tagged-strain effects and
    recruitment readouts retain their bounds; not all-species architecture or complete
    septin-class assembly necessity.
  snapshot_sha256: 247a3833857273a92d1a8082ae5d173672c1e1a204ac500ebc2b1f6f80000dcd
- evidence_id: septin-spindle-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000922,GO:0005818,GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0015630,GO:0043232,GO:0051233,GO:0072686
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:58.670094Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 46ae38806b0bc59599528cdb0d9562755b49131fb63885db129305d5efeb7645
- evidence_id: septin-spindle-agent-doi-annurev.cellbio.20.022003.114106
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev.cellbio.20.022003.114106
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:58.711384Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 192554940cba86598d7e4090ae7f7500d6d70ba42275c23819122c7edde58d95
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev.cellbio.20.022003.114106;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:58.711384Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: 'Fresh native PMC JATS primary paper: claim-bearing Introduction and complete
    Figure1 caption on yeast SPB architecture and modeling context; full Results/Methods
    not audited.'
  accessed_at: '2026-11-03T06:13:58.896428Z'
  support: supports
  summary: Inner/outer plaques, anchored gamma-TuSC and the yeast core are supported
    as source context. Introductory citations and integrative-model context do not
    independently prove the combined molecular mechanism throughout eukaryotes.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: septin-spindle-agent-P09733
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P09733.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:58.973006Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: aed535980dd8ac2307085497de3917488ff4f5da0252812d09d17d17c739b426
- evidence_id: septin-spindle-agent-query-TUB1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:59.260672Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: ab3ef6eb4aba30b014094695c817ac553dcd2c55c6f8feda6c32fae65e55e16c
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:59.260672Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-P02557
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P02557.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:59.305792Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: d22cba0cfbb4aaa448114cc4356c81a4f7116a79ee7359a05b69dfd659d6b646
- evidence_id: septin-spindle-agent-query-TUB2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:13:59.391178Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 4d1049116e3e865676ca2a31ed8f01bdd757d3cad4b28b84933b5903876ea148
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:13:59.391178Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-P09734
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P09734.json
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:13:59.409660Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 0a6865ddaa8955d9ccdc57056008255b39a4ab55d5b75e640a37a0206c197b67
- evidence_id: septin-spindle-agent-query-TUB3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:14:00.132338Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 1e154b62a419986ae1256476fa07411bfb9f6cc39e678a36cd482cc505e8e62e
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:14:00.132338Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-doi-jcb.129.6.1601
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.129.6.1601
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:14:00.299438Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: 313adbe1b330fba0e7502cfe978a583511f5c53e92c76fcedbb16f6f28d65de4
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.129.6.1601;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:14:00.299438Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-doi-science.277.5325.574
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.277.5325.574
  locator: Fresh Europe PMC exact DOI primary abstract and bibliographic metadata
    only.
  accessed_at: '2026-11-03T06:14:00.912058Z'
  support: supports
  summary: Straight1997 abstract directly reports GFP-Tub1 spindle imaging, chromosomal
    loci tracking and biphasic dynamics. No current publisher attempt, full-body retrieval
    or detailed midzone-regulator assay is claimed.
  snapshot_sha256: 85e5bb2644f5eb8b678b868051d04585c6585435bc1a03ca4913aaadce2fa9ae
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.277.5325.574;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:14:00.912058Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-pmid-11739794
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11739794%20AND%20SRC%3AMED
  locator: Fresh Europe PMC exact PMID primary abstract and native UniProt attribution
    cross-check; not full body.
  accessed_at: '2026-11-03T06:14:00.937338Z'
  support: supports
  summary: Anders/Botstein2001 studies yeast alpha-tubulin mutations and microtubule
    dynamics. Localization citation identity agrees; mutant effects do not prove each
    example is independently necessary for spindle assembly.
  snapshot_sha256: 09d880b0260ec19f9866a41868cb276dd1a1e6ee374c042df5ab39b5d2ee4b57
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11739794%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:14:00.937338Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-pmid-23001566
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A23001566%20AND%20SRC%3AMED
  locator: Fresh Europe PMC exact PMID primary abstract and native UniProt attribution
    cross-check; not full body.
  accessed_at: '2026-11-03T06:14:01.607153Z'
  support: supports
  summary: Cederquist2012 explicitly includes yeast genetics despite the human-disease
    title. Native P02557 cytoskeleton annotation cites it; this is not a taxon-mismatch
    finding or proof of every-region occupancy.
  snapshot_sha256: 11012dca34504a5eb2b11d689f0a93e4ce4338b23cc03fb67b1d2289c64726c1
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A23001566%20AND%20SRC%3AMED;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:14:01.607153Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-spindle-agent-IPR000217
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:14:01.616997Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: ddbf902c6495d576d69c82c85daf1bdf2bc9fea5894925a4efcd87dc45ea3170
- evidence_id: septin-spindle-agent-IPR002452
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:14:02.113570Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: septin-spindle-agent-IPR002453
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:14:02.207236Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: septin-spindle-agent-winey1995-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/cb33/a9630ccea6fbdd5e23d396df29c214465892.pdf
  locator: 'Fresh genuine primary PDF: abstract/Introduction, strain and EM preparation
    Methods, claim-bearing overlap/core-bundle Results and Figures5–6/12–13 captions,
    crossbridge Results and beginning of Discussion, pp1601–1602,1606–1607,1609,1611–1612.
    Not complete main-body, TableI, raw micrograph or image-pixel reanalysis.'
  accessed_at: '2026-11-03T06:14:02.240754Z'
  support: supports
  summary: S288c and S288c-background diploid nuclear spindles were reconstructed
    from serial EM. The paper explicitly separates astral microtubules from spindle
    per se. It shows overlap/interdigitation and crossbridges without molecularly
    identifying Ase1/PRC1 or proving the appended broad regulator mechanism. Inferred
    kinetochore/interpolar assignments are not all directly demonstrated.
  snapshot_sha256: fbf7dccc8b63812b7a8adb44b11b723160921e874a48d27c738971d0109fc251
- evidence_id: septin-midzone-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0051233,GO:0072686,GO:0110165
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:14:02.306471Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 6f51431934e0b34753609506bccef31f6d6165cb993a64547a8495cfc78b0a97
- evidence_id: septin-pole-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000226,GO:0000922,GO:0000930,GO:0005815,GO:0005816,GO:0005819,GO:0051225,GO:0110165
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:14:02.743276Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: a1e41b4887689d9747ff0d411edf75471105dc608579a4a7f7ee69d47dd59cc1
- evidence_id: septin-pole-agent-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: 'Fresh native issuing-authority response: exact identifier/name, definitions,
    family hierarchy, taxon/strain and returned evidence annotation fields.'
  accessed_at: '2026-11-03T06:14:02.767755Z'
  support: supports
  summary: Identifier/authority annotations verified within their returned scope;
    no independent experimental membership or assembly necessity follows solely from
    accession identity.
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: septin-pole-agent-doi-mbc.E17-06-0397
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E17-06-0397
  locator: Exact request URL and returned bibliographic metadata/available abstract
    or reviewed gene-query results.
  accessed_at: '2026-11-03T06:14:02.834072Z'
  support: supports
  summary: Only returned source identity/abstract or gene match is assessed; metadata
    is not body inspection and a bounded query is not an exhaustive absence search.
  snapshot_sha256: cffb3902bb3dc1c67a795170c81ecde54b141b008060bb39765e59b8148ed66f
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E17-06-0397;
    exact query and server/default result limit encoded in URL, executed 2026-11-03T06:14:02.834072Z;
    no publication-date restriction, no pagination. Only returned exact DOI/PMID or
    reviewed gene/taxon results inspected; no exhaustive biological absence assertion.
- evidence_id: septin-current-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire current official /api/datasets response: all20organism objects
    and28dataset keys inspected.'
  accessed_at: '2026-11-03T06:14:03.016074Z'
  support: supports
  summary: No matching fungal, algal or protist dataset occurs in the returned catalogue.
    Downstream matched gene/module requests are inapplicable; no unrelated bacterial
    dataset is substituted and no biological absence is inferred.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-spindle-agent-jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Fresh browser-indexed author-uploaded secondary review, declared crawl
    age three weeks; Introduction/core organization displayed lines185–410. Native
    HTTP request returned403.
  accessed_at: '2026-11-03T06:14:32.056Z'
  support: supports
  summary: Yeast SPB organization and structural layers provide review-tier context,
    not all-eukaryote primary evidence.
  snapshot_sha256: afc218ba4f06b94c87c6153dc79bf41953a19ecf679c4f07c4b2deefe1782717
- evidence_id: septin-spindle-agent-jaspersen-duplication-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Fresh browser-indexed author-uploaded secondary review: duplication and
    separation displayed lines619–800; no native full-text download.'
  accessed_at: '2026-11-03T06:14:38.657Z'
  support: supports
  summary: Budding-yeast bridge cleavage and Cin8/Kip1 separation are scoped mechanisms.
    No uniform pole-duplication pathway throughout microbial eukaryotes is established.
  snapshot_sha256: afc218ba4f06b94c87c6153dc79bf41953a19ecf679c4f07c4b2deefe1782717
- evidence_id: septin-spindle-agent-jaspersen-nucleation-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Fresh browser-indexed author-uploaded secondary review: nucleation displayed
    lines976–1077 and SPB/centrosome comparison1213–1308; no full-review read claimed.'
  accessed_at: '2026-11-03T06:14:32.056Z'
  support: supports
  summary: Tub4/Spc97/Spc98 and Spc110/Spc72 are yeast nucleation context. Centrosome
    comparisons explicitly preserve differences; capping and some regulatory mechanisms
    are model or uncertainty-qualified.
  snapshot_sha256: afc218ba4f06b94c87c6153dc79bf41953a19ecf679c4f07c4b2deefe1782717
- evidence_id: septin-record-septin_cytoskeleton
  kind: record_content
  reference: data/structures/cytoskeleton/septin_cytoskeleton.yaml
  locator: 'Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all
    definitions, fields, examples, provenance and graph nodes/edges.'
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Current SHA equals original frozen target and original source revision.
    Whole-record scientific reassessment performed; no record edit.
  snapshot_sha256: a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e
- evidence_id: septin-record-spindle
  kind: record_content
  reference: data/structures/cytoskeleton/spindle.yaml
  locator: 'Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all
    definitions, fields, examples, provenance and graph nodes/edges.'
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Current SHA equals original frozen target and original source revision.
    Whole-record scientific reassessment performed; no record edit.
  snapshot_sha256: da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e
- evidence_id: septin-record-spindle_midzone
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_midzone.yaml
  locator: 'Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all
    definitions, fields, examples, provenance and graph nodes/edges.'
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Current SHA equals original frozen target and original source revision.
    Whole-record scientific reassessment performed; no record edit.
  snapshot_sha256: 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661
- evidence_id: septin-record-spindle_pole
  kind: record_content
  reference: data/structures/cytoskeleton/spindle_pole.yaml
  locator: 'Complete current YAML at05425cc7089baf8133399baaf1ec24c00c661de3: all
    definitions, fields, examples, provenance and graph nodes/edges.'
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Current SHA equals original frozen target and original source revision.
    Whole-record scientific reassessment performed; no record edit.
  snapshot_sha256: c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204
- evidence_id: septin-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Evidence scope, grounded identity and distinct assembly-necessity endpoints
    govern scientific conclusions.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-adapter-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Named gene/protein/regulator claims trigger adapter applicability. Unavailable
    runner permits source fallback; no covered dataset means downstream N/A, not biological
    absence.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: septin-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Graph scope must match the represented causal transitions; topology alone
    is not mechanistic explanation.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-graph-contract
  kind: authority
  reference: .claude/skills/add-cell-structure/SKILL.md
  locator: Current frozen relevant policy passages.
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: Source-backed causal mechanism and supported structural/function summary
    remain distinct; no compulsory atomistic graph or protein census.
  snapshot_sha256: eee04ee51d2c82c05df98570674084bdce9001e5aa67d6230ac1ed50064a3175
- evidence_id: septin-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/adversary-septin/original-checks.json
  locator: Four original native validate/render runs and current/frozen/original-source
    hashes.
  accessed_at: '2026-11-03T06:17:00.462684Z'
  support: supports
  summary: All four validate and render exits0; committed Markdown matches native
    render exactly; all four target hashes unchanged. Historical full-corpus checks
    are not current CI.
  snapshot_sha256: 615df844a4aa2aef1e5a37b5a3e30d366b4a27742d09c13ddd145714aeb57c27
- evidence_id: septin-native-septin_cytoskeleton-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/septin_cytoskeleton-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/septin_cytoskeleton.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:13:59.212547Z'
  support: supports
  summary: Exit0. Declared protein examples and xrefs verified.
  snapshot_sha256: 387c2967eb8073f52f8f548e1ea1b680cf6cb805582f39582a9acef844b7155b
- evidence_id: septin-native-septin_cytoskeleton-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/septin_cytoskeleton-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/septin_cytoskeleton.yaml', '--causal-graphs'] at
    05425cc7089baf8133399baaf1ec24c00c661de3; exact receipt/log independently read
    and hash verified.
  accessed_at: '2026-11-03T06:13:59.647160Z'
  support: supports
  summary: Exit0. One COVERED GENE_OR_PROTEIN node, no missing-symbol/dangling reference;
    this is declared inventory coverage, not every species/paralog or mechanism.
  snapshot_sha256: 991ede5219f1fd76b2c5e7f126cabee7e05729556a10585de5995fd1a4c3dbb3
- evidence_id: septin-native-spindle-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/spindle.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:14:01.063545Z'
  support: supports
  summary: Exit0. Declared protein examples and xrefs verified.
  snapshot_sha256: fbffa890931fbf4429c37d30085227cebd06a23fe724b9cc58d7f219800fb9c7
- evidence_id: septin-native-spindle-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/spindle.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:14:01.469291Z'
  support: supports
  summary: Exit0. One COVERED GENE_OR_PROTEIN node, no missing-symbol/dangling reference;
    this is declared inventory coverage, not every species/paralog or mechanism.
  snapshot_sha256: d30abefe1e4ba0050cb8966807f495ba610ae6de268b2dcc29d650cdf208c639
- evidence_id: septin-native-spindle_midzone-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_midzone-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/spindle_midzone.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:14:02.913891Z'
  support: supports
  summary: Exit0. Declared protein examples and xrefs verified.
  snapshot_sha256: 16ac2130c4445c627d6383212609e39132e0d8ded05fff4964e53c39cb5fea72
- evidence_id: septin-native-spindle_midzone-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_midzone-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/spindle_midzone.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:14:03.325084Z'
  support: supports
  summary: Exit0. One COVERED GENE_OR_PROTEIN node, no missing-symbol/dangling reference;
    this is declared inventory coverage, not every species/paralog or mechanism.
  snapshot_sha256: 601a7a6cd5f4eb06e0946aeaa1fa371e752ebf78a1111bdf2160da6b52307072
- evidence_id: septin-native-spindle_pole-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_pole-uniprot-verify-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/spindle_pole.yaml', '--verify'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:14:03.730503Z'
  support: supports
  summary: Exit0. Empty exact-protein inventory and zero GENE_OR_PROTEIN graph nodes;
    no molecular claim validated by empty scope.
  snapshot_sha256: 3f1c682aa4682ac409b4955b5c6542a1ea2bef650ebf9224514c6826431d4961
- evidence_id: septin-native-spindle_pole-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/spindle_pole-uniprot-causal-receipt.json
  locator: Root-run command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record',
    'data/structures/cytoskeleton/spindle_pole.yaml', '--causal-graphs'] at 05425cc7089baf8133399baaf1ec24c00c661de3;
    exact receipt/log independently read and hash verified.
  accessed_at: '2026-11-03T06:14:04.137712Z'
  support: supports
  summary: Exit0. Empty exact-protein inventory and zero GENE_OR_PROTEIN graph nodes;
    no molecular claim validated by empty scope.
  snapshot_sha256: 11848c6f87755d57ce8c8a7a87a7cee2521ee90b893ba8dbcd2471c868409088
- evidence_id: septin-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical canary attempt2026-11-03T00:49:00.848907Z–00:49:00.863225Z,
    exit1 PermissionError reading pyvenv.cfg; no fresh invocation.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  summary: Historical OS unavailability is separate from fresh official catalogue
    fallback. No runner success, current execution, or downstream unrelated-dataset
    query is claimed.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:18:53.516891Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 2f063d97b843044001e70a0b1d934e9d27a4e088319a955816e896bf1b98b77f
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:13:59.470586Z'
  support: supports
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:13:34.854866Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:13:31.891629Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T06:13:58.961009Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T06:22:35Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: 46844d145be2fe22e67d916457600af4ac0a4230f7487a13676b7e1768a8d7a1
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2353/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T06:15:05.973580Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 0fb3c76019516ea11425a633f74794fa2cc9522033f49696d6c0a92263a7c37a
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2353 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-endocytic-identity
  area: identity
  topic: Broad patch identity and yeast actin-rich realization
  outcome: supported
  summary: GO0061645 and cell-cortex parthood are supported. Actin-rich yeast patches
    are a scoped realization, not obligatory composition of every broad endocytic
    patch. No new identity or mandatory optional-component finding.
  target_ids:
  - GO:0061645
  evidence_ids:
  - plaque-current-0
  - plaque-endocytic-prep-go
  - plaque-endocytic-prep-jats-jcb.200404159
- assessment_id: plaque-endocytic-components
  area: grounding
  topic: Eight protein examples and family/complex boundaries
  outcome: supported
  summary: All eight reviewed S288C accession/gene/name/taxon pairs and exact uniqueness
    queries match. The seven-member Arp2/3 complex is a legitimate complex cohort.
    IPR004000 includes Arps and is broader than conventional actin; only this candidate
    was checked, with no exhaustive family-absence assertion. UNKNOWN essentiality
    is appropriate uncertainty.
  target_ids:
  - GO:0061645
  evidence_ids:
  - plaque-current-0
  - plaque-endocytic-prep-go
  - plaque-endocytic-prep-IPR004000
  - plaque-endocytic-prep-P60010
  - plaque-endocytic-prep-P32381
  - plaque-endocytic-prep-P47117
  - plaque-endocytic-prep-P38328
  - plaque-endocytic-prep-P53731
  - plaque-endocytic-prep-P33204
  - plaque-endocytic-prep-Q05933
  - plaque-endocytic-prep-P40518
  - plaque-endocytic-prep-ACT1-query
  - plaque-endocytic-prep-query-ARP2
  - plaque-endocytic-prep-query-ARP3
  - plaque-endocytic-prep-query-ARC40
  - plaque-endocytic-prep-query-ARC35
  - plaque-endocytic-prep-query-ARC19
  - plaque-endocytic-prep-query-ARC18
  - plaque-endocytic-prep-query-ARC15
- assessment_id: plaque-endocytic-definition
  area: provenance
  topic: GO-only attribution of appended fungal mechanism
  outcome: concern
  summary: The added coat/adaptor/NPF/scission/turgor account exceeds GO-only definition_source.
    Primary yeast studies support portions with stage and osmotic qualifications;
    no audited source establishes the complete listed mechanism throughout fungi.
    Retain original minor F1.
  target_ids:
  - GO:0061645
  evidence_ids:
  - plaque-current-0
  - plaque-endocytic-prep-go
  - plaque-endocytic-prep-jats-jcb.200404159
  - plaque-endocytic-prep-galletta2008-plos
  - plaque-endocytic-prep-aghamohammadzadeh2009-jats
- assessment_id: plaque-endocytic-function
  area: evidence
  topic: Early recruitment, actin assembly and inward motion
  outcome: supported
  summary: Fresh primary morphology and regulator/turgor experiments support actin-rich
    yeast patch function within preparation/stage limits. Kaksonen remains abstract-only.
    The early endocytic patch can organize later actin assembly; neither circularity
    nor impossibility follows from the broad node names.
  target_ids:
  - GO:0061645
  evidence_ids:
  - plaque-current-0
  - plaque-endocytic-prep-jats-jcb.200404159
  - plaque-endocytic-prep-galletta2008-plos
  - plaque-endocytic-prep-kaksonen2003-meta
  - plaque-endocytic-prep-aghamohammadzadeh2009-jats
- assessment_id: plaque-endocytic-graph
  area: graph
  topic: Membership/output versus mechanism
  outcome: concern
  summary: Six nodes/five edges provide three parthood and two broad output relations.
    The GO-only assembly edge omits stage and recruited machinery; MECHANISTIC overstates
    represented explanation. Original minor F2 remains, separately from whether early
    sites can organize actin.
  target_ids:
  - GO:0061645
  evidence_ids:
  - plaque-current-0
  - plaque-graph-contract
  - plaque-endocytic-prep-galletta2008-plos
  - plaque-endocytic-prep-kaksonen2003-meta
- assessment_id: plaque-tether-identity
  area: identity
  topic: Exact envelope complex and native hierarchy
  outcome: supported
  summary: GO0034993, its three supplied synonyms, GO0106094 parent and GO0034992
    parthood are native. It denotes a membrane tether, distinct from HAA/rMTOC.
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-go
  - plaque-linc-agent-go
  - plaque-linc-agent-swartz2014-jats
- assessment_id: plaque-tether-current-type
  area: representation
  topic: Substantive stale Bqt1/Bqt2 grouping reassessment
  outcome: supported
  summary: 'Current PROTEIN_COMPLEX correctly represents two distinct interacting
    proteins forming the Rap1–Sad1 connector, rather than one family/paralog class.
    Abstract bridge evidence and later interaction/degradation data support the grouped
    identity. ASSOCIATED_MACHINERY remains explicit. #2420 is a prior record correction;
    no terminal disposition of the seven-target category finding.'
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-doi-j.cell.2006.01.048-meta
  - plaque-linc-agent-amelina2015-jats
  - plaque-tether-prep-moiseeva2017-jats
  - plaque-category-context
  - plaque-historical-2420
  - plaque-schema
- assessment_id: plaque-tether-examples
  area: grounding
  topic: Four reference examples and SUN family
  outcome: supported
  summary: Fresh Q09825/P87245/Q92358/Q9US52 identity, reviewed status, gene symbols
    and taxon284812 match. IPR045119 supports the SUN-family grounding. 972h- examples
    are expressly reference sequences, not claims about exact engineered experimental
    stock; native verify and three-node graph coverage checks pass.
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-IPR045119
  - plaque-tether-prep-tax-284812
  - plaque-tether-prep-Q09825
  - plaque-tether-prep-P87245
  - plaque-tether-prep-Q92358
  - plaque-tether-prep-Q9US52
  - plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-verify
  - plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-causal
- assessment_id: plaque-tether-assembly
  area: evidence
  topic: Assembly necessity and motor-interface limits
  outcome: unknown
  summary: Function, localization, viability and Bqt-dependent bouquet attachment
    are distinct from whether each core LINC assembly forms. Complete core-subunit
    removal/reconstitution necessity is not established for ESSENTIAL or the connector
    CONDITIONAL value. Funaya introductory topology is prior-study context, and its
    direct Hrs1 interaction assays do not alone establish direct dynein-dynactin recruitment.
    No opposite essentiality or absent-Kms2 finding is invented.
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-schema
  - plaque-tether-prep-paper
  - plaque-linc-agent-swartz2014-jats
  - plaque-linc-agent-yoshida2013-jats
  - plaque-tether-prep-moiseeva2017-jats
- assessment_id: plaque-linc-identity
  area: identity
  topic: Exact envelope complex and native hierarchy
  outcome: supported
  summary: GO1990612 exactly denotes Sad1–Kms1; native GO retains its GO0034993 is_a
    parent. Swartz2014 supports the DSB-repair opening with S/G2/repair-pathway bounds;
    meiotic roles are additional contexts.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-tether-prep-go
  - plaque-linc-agent-go
  - plaque-linc-agent-swartz2014-jats
- assessment_id: plaque-linc-current-type
  area: representation
  topic: Substantive stale Bqt1/Bqt2 grouping reassessment
  outcome: supported
  summary: 'Current PROTEIN_COMPLEX correctly represents two distinct interacting
    proteins forming the Rap1–Sad1 connector, rather than one family/paralog class.
    Abstract bridge evidence and later interaction/degradation data support the grouped
    identity. ASSOCIATED_MACHINERY remains explicit. #2420 is a prior record correction;
    no terminal disposition of the seven-target category finding.'
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-tether-prep-doi-j.cell.2006.01.048-meta
  - plaque-linc-agent-amelina2015-jats
  - plaque-tether-prep-moiseeva2017-jats
  - plaque-category-context
  - plaque-historical-2420
  - plaque-schema
- assessment_id: plaque-linc-examples
  area: grounding
  topic: Four reference examples and SUN family
  outcome: supported
  summary: Fresh Q09825/P87245/Q92358/Q9US52 identity, reviewed status, gene symbols
    and taxon284812 match. IPR045119 supports the SUN-family grounding. 972h- examples
    are expressly reference sequences, not claims about exact engineered experimental
    stock; native verify and three-node graph coverage checks pass.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-tether-prep-IPR045119
  - plaque-tether-prep-tax-284812
  - plaque-tether-prep-Q09825
  - plaque-tether-prep-P87245
  - plaque-tether-prep-Q92358
  - plaque-tether-prep-Q9US52
  - plaque-native-sad1_kms1_linc_complex-verify
  - plaque-native-sad1_kms1_linc_complex-causal
- assessment_id: plaque-linc-assembly
  area: evidence
  topic: Assembly necessity and motor-interface limits
  outcome: unknown
  summary: Function, localization, viability and Bqt-dependent bouquet attachment
    are distinct from whether each core LINC assembly forms. Complete core-subunit
    removal/reconstitution necessity is not established for ESSENTIAL or the connector
    CONDITIONAL value. Funaya introductory topology is prior-study context, and its
    direct Hrs1 interaction assays do not alone establish direct dynein-dynactin recruitment.
    No opposite essentiality or absent-Kms2 finding is invented.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-schema
  - plaque-tether-prep-paper
  - plaque-linc-agent-swartz2014-jats
  - plaque-linc-agent-yoshida2013-jats
  - plaque-tether-prep-moiseeva2017-jats
- assessment_id: plaque-tether-horsetail
  area: scope
  topic: Membrane tether distinct from radial array
  outcome: concern
  summary: The maintained horsetail function and corresponding process/edge say the
    membrane complex provides the radial array and call GO0032117 its exact definition.
    GO0032117 is HAA, and Funaya distinguishes Hrs1/rMTOC array organization from
    membrane bridge. Original major F1 remains; a tether contribution to movement
    can be retained with exact evidence.
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-go
  - plaque-tether-prep-paper
  - plaque-tether-prep-doi-j.cub.2005.07.058-meta
- assessment_id: plaque-tether-fungal-scope
  area: scope
  topic: Fungi COMMON and dynein generalization
  outcome: concern
  summary: Chikashige abstract supports S. pombe Bqt1/Bqt2 connector, not broad fungal
    prevalence of this microtubule tether or uniform dynein coupling. Lee/Fan demonstrate
    distinct budding-yeast actin-associated machinery. Original major F2 remains without
    asserting absence of related tethers in other fungi.
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-doi-j.cell.2006.01.048-meta
  - plaque-linc-agent-csm2020-jats
  - plaque-linc-agent-fan2020-jats
  - plaque-tether-prep-tax-4751
- assessment_id: plaque-tether-graph
  area: graph
  topic: Represented force transmission
  outcome: concern
  summary: Six nodes/five edges are constituent/compartment relations and whole-structure
    output. Correcting the copied HAA function does not itself supply a mechanistic
    tether/force transition. Original minor F3 remains.
  target_ids:
  - GO:0034993
  evidence_ids:
  - plaque-current-4
  - plaque-graph-contract
  - plaque-tether-prep-paper
- assessment_id: plaque-linc-species-transfer
  area: scope
  topic: Molecular subject of Fan assays and broad fungal distribution
  outcome: concern
  summary: Fan directly studies Mps2–Mps3–Csm4 in budding yeast; the graph still assigns
    Fan-only telomere and conversion outputs to Sad1–Kms1. A budding-yeast qualifier
    inside prose does not change the edge subject. Fungi COMMON/dynein wording also
    exceeds the fission-yeast source. Original major F1 remains; this does not deny
    S. pombe telomere/recombination roles.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-linc-agent-fan2020-jats
  - plaque-linc-agent-csm2020-jats
  - plaque-tether-prep-doi-j.cell.2006.01.048-meta
  - plaque-linc-agent-yoshida2013-jats
- assessment_id: plaque-linc-bounded-functions
  area: evidence
  topic: Fission-yeast attachment and DSB roles
  outcome: supported
  summary: Moiseeva supports conditional telomere-SPB attachment/spindle effects with
    successful divisions retained in a subset, and Jimenez preserves partial mitotic
    recruitment without complete bouquet. Swartz independently supports DSB repair
    context. These bounded observations can survive correction of cross-species attribution.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-tether-prep-moiseeva2017-jats
  - plaque-tether-prep-jimenez2025-jats
  - plaque-linc-agent-swartz2014-jats
- assessment_id: plaque-linc-kms2
  area: scope
  topic: Meiotic recruitment versus MMS-associated foci
  outcome: unknown
  summary: Yoshida sees Kms2 at meiotic telocentrosomes; Swartz does not detect increased
    Kms2 in MMS-associated foci but leaves redundancy/low-copy roles open. The definition
    parenthetical does not establish fixed three-subunit stoichiometry. No universal
    absence or replacement of the named complex is concluded.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-linc-agent-yoshida2013-jats
  - plaque-linc-agent-swartz2014-jats
  - plaque-tether-prep-paper
- assessment_id: plaque-linc-graph
  area: graph
  topic: Functional summary versus causal chain
  outcome: concern
  summary: Seven nodes/six edges give two parthood, one association and three whole-complex
    outputs; there is no represented bridge/motor/force transition. FUNCTION is reasonable
    but MECHANISTIC overstates detail. Original minor F2 remains separate from cross-species
    assignment.
  target_ids:
  - GO:1990612
  evidence_ids:
  - plaque-current-5
  - plaque-graph-contract
  - plaque-linc-agent-yoshida2013-jats
  - plaque-tether-prep-moiseeva2017-jats
- assessment_id: plaque-adapter-coverage
  area: scope
  topic: Molecular triggers and native catalogue applicability
  outcome: supported
  summary: ACT1/Arp genes and Sad1/Kms/Bqt genes require an applicability check even
    without expression claims. Fresh native catalogue contains no matching fungal
    species/strain; downstream gene/module queries therefore do not apply. The historical
    shared-runner failure remains unavailable execution; fresh source fallback is
    not a runner success or experimental mechanism proof.
  target_ids:
  - GO:0061645
  - GO:0034993
  - GO:1990612
  evidence_ids:
  - plaque-current-0
  - plaque-current-4
  - plaque-current-5
  - plaque-adapter-policy
  - plaque-adapter-catalogue
- assessment_id: plaque-native-schema
  area: schema
  topic: Original validation, source hashes and current protein gates
  outcome: supported
  summary: Original bundles validate and render exactly with all14 historical hashes
    each. Six current protein commands at the source head exit0, with logs independently
    hash-verified. These deterministic results do not erase retained scientific findings;
    root separately owns corpus QC and final-head CI.
  target_ids:
  - GO:0061645
  - GO:0034993
  - GO:1990612
  evidence_ids:
  - plaque-original-native-validation
  - plaque-native-endocytic_patch-verify
  - plaque-native-endocytic_patch-causal
  - plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-verify
  - plaque-native-meiotic_nuclear_membrane_microtubule_tethering_complex-causal
  - plaque-native-sad1_kms1_linc_complex-verify
  - plaque-native-sad1_kms1_linc_complex-causal
- assessment_id: micro-gamma_tubulin_complex-identity
  area: identity
  topic: Current exact structure identity, hierarchy and source-bounded definition
  outcome: supported
  summary: Native GO identity, multiprotein kind and category are sound. Generic complex,
    TuSC and TuRC are retained as distinct identities; MTOC/SPB/eMTOC are contexts
    rather than replacement identities. Appended structural details remain subject
    to the source-specific concerns below.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-go
- assessment_id: micro-gamma_tubulin_complex-staleness
  area: schema
  topic: Substantive refresh of changed maintained inputs
  outcome: supported
  summary: Original frozen target bytes match their historical source; current main
    differs. Expanded protein examples and grouped component types have been independently
    checked. Complex/small also add budding-yeast canonical context and component/edge
    literature. The original files remain historical; this is a current-input successor
    with exact finding lineage.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-prior-gamma_tubulin_complex
  - micro-stale-proof
  - micro-original-roundtrip
- assessment_id: micro-gamma_tubulin_complex-proteins
  area: grounding
  topic: Current accession identity versus source-specific membership
  outcome: supported
  summary: 'All six examples match reviewed identities: P25295/Q9Y705/Q9USQ2 in S.
    pombe 972h- and P53378/P38863/P53540 in S288C. The added budding-yeast review
    is correctly scoped secondary evidence for Spc97/Spc98; P25295 is correctly disambiguated
    from Q9USH8. Vardy/Toda supports Alp6 localization.'
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-named-proteins-284812
  - micro-named-proteins-559292
  - micro-uniprot-P25295
  - micro-uniprot-Q9USH8
  - micro-uniprot-Q9USQ2
  - micro-pmid-11080156
  - micro-jaspersen-secondary
- assessment_id: micro-gamma_tubulin_complex-history
  area: consistency
  topic: Already merged grouped-type and evidence corrections
  outcome: supported
  summary: 'The GCP2/GCP3 component is now PROTEIN_COMPLEX and the added budding-yeast
    component/edge review source is present. These are already-on-main repairs associated
    with #2420/#2470, not edits performed by this PR. The wrong fission-yeast Viswanath
    attribution remains.'
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-category-20261023
  - micro-category-20261025
  - micro-issue-2420
  - micro-issue-2431
  - micro-issue-2470
- assessment_id: micro-gamma_tubulin_complex-source-support
  area: evidence
  topic: Current source-attribution and molecular scope
  outcome: concern
  summary: Conserved gamma/Alp4/Alp6 and budding-yeast Tub4/Spc97/Spc98 membership
    are supported. Viswanath2017 still has the wrong organism/experiment assigned
    in component, graph and canonical-example fields. Receptor/domain and exact ring-state
    details require species-specific structural sources rather than GO alone.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-viswanath2017
  - micro-samejima2010
  - micro-samejima2008
  - micro-anders2006
  - micro-brilot2021
  - micro-lyon2016
  - micro-jaspersen-secondary
- assessment_id: micro-gamma_tubulin_complex-graph
  area: graph
  topic: Membership/output summary versus resolved causal mechanism
  outcome: concern
  summary: Functions and graph still use the SPB as acting structure, including duplication/separation,
    instead of explaining the molecular complex contribution. Membership/context and
    whole-complex output edges remain labeled MECHANISTIC. Native node coverage does
    not fix this bounded representation concern.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-graph-rubric
  - micro-lyon2016
  - micro-lynch2014
  - micro-native-gamma_tubulin_complex-causal
- assessment_id: micro-gamma_tubulin_complex-necessity
  area: evidence
  topic: Assembly necessity separated from identity, localization and viability
  outcome: unknown
  summary: ESSENTIAL core, CONDITIONAL noncore and/or DISPENSABLE associated-machinery
    declarations cannot be independently generalized from identity, viability or nucleation
    phenotypes. Residual Mto2-mutant PAA activity and conditional Mzt1 core association
    are specific endpoints, not tests of every complete ring state. The unknown is
    retained; no finding is invented solely for the lack of a universal assembly assay.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-native-checklist
  - micro-pmid-12134075
  - micro-anders2006
  - micro-samejima2008
  - micro-samejima2005
  - micro-masuda2013
- assessment_id: micro-gamma_tubulin_complex-taxonomy-completeness
  area: scope
  topic: Taxon, family and nonasserted optional surfaces
  outcome: supported
  summary: Declared taxon identifiers and reference-example names match native authorities.
    Fission/budding-yeast experiments do not establish a complete eukaryote inventory
    or identical receptor/geometry across fungi. Gamma family specificity is available;
    optional ungrounded mixed-family slots are not automatic defects. No image asset,
    quantitative property, dataset, trait link or verbatim snippet is asserted by
    these targets.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-taxon-2759
  - micro-taxon-284812
  - micro-taxon-4896
  - micro-taxon-559292
  - micro-interpro
  - micro-go
- assessment_id: micro-gamma_tubulin_complex-adapter
  area: evidence
  topic: Named-protein structured-source applicability
  outcome: not_applicable
  summary: Named genes/accessions trigger the policy. The historical runner is unavailable,
    and fresh inspection of all 20 official catalogue organisms/28 dataset keys yields
    no matching eukaryotic organism. Therefore downstream gene search/module summarize
    is not applicable; no negative biological conclusion follows. This corrects the
    original unsupported structural-claim exemption.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-prior-gamma_tubulin_complex
- assessment_id: micro-gamma_tubulin_complex-native
  area: schema
  topic: Current native protein diagnostic and historical bundle validation
  outcome: supported
  summary: Root-run current native --verify and --causal-graphs each exited zero with
    their actual receipts. The two GENE_OR_PROTEIN nodes are covered by declared examples.
    Independently rerun original schema/render checks pass and reproduce Markdown.
    These checks certify their bounded syntax/identity coverage, not scientific truth
    or current CI.
  target_ids:
  - GO:0000930
  evidence_ids:
  - micro-native-gamma_tubulin_complex-verify
  - micro-native-gamma_tubulin_complex-causal
  - micro-original-roundtrip
- assessment_id: micro-gamma_tubulin_ring_complex-identity
  area: identity
  topic: Current exact structure identity, hierarchy and source-bounded definition
  outcome: supported
  summary: Native GO identity, multiprotein kind and category are sound. Generic complex,
    TuSC and TuRC are retained as distinct identities; MTOC/SPB/eMTOC are contexts
    rather than replacement identities. Appended structural details remain subject
    to the source-specific concerns below.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-go
- assessment_id: micro-gamma_tubulin_ring_complex-staleness
  area: schema
  topic: Substantive refresh of changed maintained inputs
  outcome: supported
  summary: Original frozen target bytes match their historical source; current main
    differs. Expanded protein examples and grouped component types have been independently
    checked. Complex/small also add budding-yeast canonical context and component/edge
    literature. The original files remain historical; this is a current-input successor
    with exact finding lineage.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-prior-gamma_tubulin_ring_complex
  - micro-stale-proof
  - micro-original-roundtrip
- assessment_id: micro-gamma_tubulin_ring_complex-proteins
  area: grounding
  topic: Current accession identity versus source-specific membership
  outcome: supported
  summary: All eight declared examples match reviewed identities. New Alp6/Gfh1/Mod21/Alp16
    evidence provenance matches native entries, and inspected primary localization/membership
    studies support those bounded claims. Matsuyama2006 ORFeome is not treated as
    a newly inspected individual-image experiment. Identity additions do not resolve
    structural/allosteric source inflation.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-named-proteins-284812
  - micro-uniprot-Q9USQ2
  - micro-uniprot-Q9P7R5
  - micro-uniprot-Q9UT52
  - micro-uniprot-P87244
  - micro-pmid-11080156
  - micro-pmid-15004232
  - micro-pmid-12134075
  - micro-anders2006
  - micro-new-europepmc
- assessment_id: micro-gamma_tubulin_ring_complex-history
  area: consistency
  topic: Already merged grouped-type and evidence corrections
  outcome: supported
  summary: 'Mto1/Mto2 and GCP4/GCP5/GCP6 grouped components are now PROTEIN_COMPLEX,
    consistent with historical #2420/#2431 changes. This does not imply new structural
    proof of a seam or whole-category disposition.'
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-category-20261023
  - micro-category-20261025
  - micro-issue-2420
  - micro-issue-2431
  - micro-issue-2470
- assessment_id: micro-gamma_tubulin_ring_complex-source-support
  area: evidence
  topic: Current source-attribution and molecular scope
  outcome: concern
  summary: Core/noncore membership and Mto1/Mto2 recruitment/nucleation are supported.
    Samejima2010 does not establish 13-protofilament ring geometry; Samejima2005 does
    not establish a Gfh1/Mod21/Alp16 14-spoke seam. Lynch2014 leaves conformational
    activation unresolved. Original structural/allostery finding remains open despite
    the new protein examples.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-samejima2010
  - micro-samejima2005
  - micro-anders2006
  - micro-lynch2014
  - micro-brilot2021
- assessment_id: micro-gamma_tubulin_ring_complex-graph
  area: graph
  topic: Membership/output summary versus resolved causal mechanism
  outcome: concern
  summary: The graph retains component parthood, Mto1/Mto2 association and whole-complex
    nucleation output, rather than a resolved source-backed causal mechanism. MECHANISTIC
    scope remains overstated; assembly/activity/source qualifications must be retained.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-graph-rubric
  - micro-lyon2016
  - micro-lynch2014
  - micro-native-gamma_tubulin_ring_complex-causal
- assessment_id: micro-gamma_tubulin_ring_complex-necessity
  area: evidence
  topic: Assembly necessity separated from identity, localization and viability
  outcome: unknown
  summary: ESSENTIAL core, CONDITIONAL noncore and/or DISPENSABLE associated-machinery
    declarations cannot be independently generalized from identity, viability or nucleation
    phenotypes. Residual Mto2-mutant PAA activity and conditional Mzt1 core association
    are specific endpoints, not tests of every complete ring state. The unknown is
    retained; no finding is invented solely for the lack of a universal assembly assay.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-native-checklist
  - micro-pmid-12134075
  - micro-anders2006
  - micro-samejima2008
  - micro-samejima2005
  - micro-masuda2013
- assessment_id: micro-gamma_tubulin_ring_complex-taxonomy-completeness
  area: scope
  topic: Taxon, family and nonasserted optional surfaces
  outcome: supported
  summary: Declared taxon identifiers and reference-example names match native authorities.
    Fission/budding-yeast experiments do not establish a complete eukaryote inventory
    or identical receptor/geometry across fungi. Gamma family specificity is available;
    optional ungrounded mixed-family slots are not automatic defects. No image asset,
    quantitative property, dataset, trait link or verbatim snippet is asserted by
    these targets.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-taxon-2759
  - micro-taxon-284812
  - micro-taxon-4896
  - micro-taxon-559292
  - micro-interpro
  - micro-go
- assessment_id: micro-gamma_tubulin_ring_complex-adapter
  area: evidence
  topic: Named-protein structured-source applicability
  outcome: not_applicable
  summary: Named genes/accessions trigger the policy. The historical runner is unavailable,
    and fresh inspection of all 20 official catalogue organisms/28 dataset keys yields
    no matching eukaryotic organism. Therefore downstream gene search/module summarize
    is not applicable; no negative biological conclusion follows. This corrects the
    original unsupported structural-claim exemption.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-prior-gamma_tubulin_ring_complex
- assessment_id: micro-gamma_tubulin_ring_complex-native
  area: schema
  topic: Current native protein diagnostic and historical bundle validation
  outcome: supported
  summary: Root-run current native --verify and --causal-graphs each exited zero with
    their actual receipts. The two GENE_OR_PROTEIN nodes are covered by declared examples.
    Independently rerun original schema/render checks pass and reproduce Markdown.
    These checks certify their bounded syntax/identity coverage, not scientific truth
    or current CI.
  target_ids:
  - GO:0000931
  evidence_ids:
  - micro-native-gamma_tubulin_ring_complex-verify
  - micro-native-gamma_tubulin_ring_complex-causal
  - micro-original-roundtrip
- assessment_id: micro-gamma_tubulin_small_complex-identity
  area: identity
  topic: Current exact structure identity, hierarchy and source-bounded definition
  outcome: supported
  summary: Native GO identity, multiprotein kind and category are sound. Generic complex,
    TuSC and TuRC are retained as distinct identities; MTOC/SPB/eMTOC are contexts
    rather than replacement identities. Appended structural details remain subject
    to the source-specific concerns below.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-go
- assessment_id: micro-gamma_tubulin_small_complex-staleness
  area: schema
  topic: Substantive refresh of changed maintained inputs
  outcome: supported
  summary: Original frozen target bytes match their historical source; current main
    differs. Expanded protein examples and grouped component types have been independently
    checked. Complex/small also add budding-yeast canonical context and component/edge
    literature. The original files remain historical; this is a current-input successor
    with exact finding lineage.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-prior-gamma_tubulin_small_complex
  - micro-stale-proof
  - micro-original-roundtrip
- assessment_id: micro-gamma_tubulin_small_complex-proteins
  area: grounding
  topic: Current accession identity versus source-specific membership
  outcome: supported
  summary: 'All six examples match reviewed identities: P25295/Q9Y705/Q9USQ2 in S.
    pombe 972h- and P53378/P38863/P53540 in S288C. The added budding-yeast review
    is correctly scoped secondary evidence for Spc97/Spc98; P25295 is correctly disambiguated
    from Q9USH8. Vardy/Toda supports Alp6 localization.'
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-named-proteins-284812
  - micro-named-proteins-559292
  - micro-uniprot-P25295
  - micro-uniprot-Q9USH8
  - micro-uniprot-Q9USQ2
  - micro-pmid-11080156
  - micro-jaspersen-secondary
- assessment_id: micro-gamma_tubulin_small_complex-history
  area: consistency
  topic: Already merged grouped-type and evidence corrections
  outcome: supported
  summary: 'The GCP2/GCP3 component is now PROTEIN_COMPLEX and the added budding-yeast
    component/edge review source is present. These are already-on-main repairs associated
    with #2420/#2470, not edits performed by this PR. The wrong fission-yeast Viswanath
    attribution remains.'
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-category-20261023
  - micro-category-20261025
  - micro-issue-2420
  - micro-issue-2431
  - micro-issue-2470
- assessment_id: micro-gamma_tubulin_small_complex-source-support
  area: evidence
  topic: Current source-attribution and molecular scope
  outcome: concern
  summary: Conserved gamma/Alp4/Alp6 and budding-yeast Tub4/Spc97/Spc98 membership
    are supported. Viswanath2017 still has the wrong organism/experiment assigned
    in component, graph and canonical-example fields. Receptor/domain and exact ring-state
    details require species-specific structural sources rather than GO alone.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-viswanath2017
  - micro-samejima2010
  - micro-samejima2008
  - micro-anders2006
  - micro-brilot2021
  - micro-lyon2016
  - micro-jaspersen-secondary
- assessment_id: micro-gamma_tubulin_small_complex-graph
  area: graph
  topic: Membership/output summary versus resolved causal mechanism
  outcome: concern
  summary: Functions and graph still use the SPB as acting structure, including duplication/separation,
    instead of explaining the molecular complex contribution. Membership/context and
    whole-complex output edges remain labeled MECHANISTIC. Native node coverage does
    not fix this bounded representation concern.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-graph-rubric
  - micro-lyon2016
  - micro-lynch2014
  - micro-native-gamma_tubulin_small_complex-causal
- assessment_id: micro-gamma_tubulin_small_complex-necessity
  area: evidence
  topic: Assembly necessity separated from identity, localization and viability
  outcome: unknown
  summary: ESSENTIAL core, CONDITIONAL noncore and/or DISPENSABLE associated-machinery
    declarations cannot be independently generalized from identity, viability or nucleation
    phenotypes. Residual Mto2-mutant PAA activity and conditional Mzt1 core association
    are specific endpoints, not tests of every complete ring state. The unknown is
    retained; no finding is invented solely for the lack of a universal assembly assay.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-native-checklist
  - micro-pmid-12134075
  - micro-anders2006
  - micro-samejima2008
  - micro-samejima2005
  - micro-masuda2013
- assessment_id: micro-gamma_tubulin_small_complex-taxonomy-completeness
  area: scope
  topic: Taxon, family and nonasserted optional surfaces
  outcome: supported
  summary: Declared taxon identifiers and reference-example names match native authorities.
    Fission/budding-yeast experiments do not establish a complete eukaryote inventory
    or identical receptor/geometry across fungi. Gamma family specificity is available;
    optional ungrounded mixed-family slots are not automatic defects. No image asset,
    quantitative property, dataset, trait link or verbatim snippet is asserted by
    these targets.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-record-gamma_tubulin_small_complex
  - micro-taxon-2759
  - micro-taxon-284812
  - micro-taxon-4896
  - micro-taxon-559292
  - micro-interpro
  - micro-go
- assessment_id: micro-gamma_tubulin_small_complex-adapter
  area: evidence
  topic: Named-protein structured-source applicability
  outcome: not_applicable
  summary: Named genes/accessions trigger the policy. The historical runner is unavailable,
    and fresh inspection of all 20 official catalogue organisms/28 dataset keys yields
    no matching eukaryotic organism. Therefore downstream gene search/module summarize
    is not applicable; no negative biological conclusion follows. This corrects the
    original unsupported structural-claim exemption.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
  - micro-prior-gamma_tubulin_small_complex
- assessment_id: micro-gamma_tubulin_small_complex-native
  area: schema
  topic: Current native protein diagnostic and historical bundle validation
  outcome: supported
  summary: Root-run current native --verify and --causal-graphs each exited zero with
    their actual receipts. The two GENE_OR_PROTEIN nodes are covered by declared examples.
    Independently rerun original schema/render checks pass and reproduce Markdown.
    These checks certify their bounded syntax/identity coverage, not scientific truth
    or current CI.
  target_ids:
  - GO:0008275
  evidence_ids:
  - micro-native-gamma_tubulin_small_complex-verify
  - micro-native-gamma_tubulin_small_complex-causal
  - micro-original-roundtrip
- assessment_id: septin-S2353-A1
  area: identity
  topic: Whole cytoskeleton and specialized septin assemblies
  outcome: supported
  target_ids:
  - GO:0032156
  summary: The GO identity, cytoskeleton parent and declared structural parts are
    consistent. FILAMENT is a broad local kind classification; the text explicitly
    includes higher-order complexes and arrays and does not equate the entire framework
    with a single oligomer.
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-douglas-pmc
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A2
  area: grounding
  topic: An exact generic family is available
  outcome: concern
  target_ids:
  - GO:0032156
  summary: The REVIEWED_LABEL_ONLY rationale requires a family identifier for a complete
    filament-array-forming cohort. The component itself is the generic septin-proteins
    class, for which IPR016491 is exact. Family identity does not require an exact
    inventory of proteins occupying each array.
  evidence_ids:
  - septin-septin-agent-IPR016491
  - septin-septin-agent-go
  - septin-record-septin_cytoskeleton
  - septin-policy
- assessment_id: septin-S2353-A3
  area: evidence
  topic: Correct vegetative examples remain valid at the broader target scope
  outcome: supported
  target_ids:
  - GO:0032156
  summary: All five reviewed gene/accession/taxon identities are correct. Native UniProt
    annotations support the specifically attributed Huh, Finnigan and Mino localization
    notes. Finnigan provides directly read bud-neck experiments; the two other cited
    papers were metadata/abstract- and native-annotation-scoped. Vegetative members
    are valid examples for the whole cytoskeleton even though the canonical array
    examples describe spores.
  evidence_ids:
  - septin-septin-agent-P32457
  - septin-septin-agent-P25342
  - septin-septin-agent-P32458
  - septin-septin-agent-P32468
  - septin-septin-agent-Q07657
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-5476
  - septin-septin-agent-tax-559292
  - septin-septin-agent-pmid-14562095
  - septin-septin-agent-pmid-25971666
  - septin-septin-agent-pmid-9790978
  - septin-septin-agent-versele2005-correct-meta
  - septin-septin-agent-douglas2005-correct-meta
  - septin-septin-agent-finnigan2015-pmc
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-douglas-pmc
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A4
  area: scope
  topic: Expanded architecture and functions exceed the cited taxon scope
  outcome: concern
  target_ids:
  - GO:0032156
  summary: The expanded definition generalizes a cortical network and barrier/scaffold
    recruitment across yeast, filamentous fungi and green algae and several developmental
    sites. Fresh Versele Introduction supports green-algal ortholog occurrence, while
    its functional passages concern yeast. Fresh Douglas sporulation and Aspergillus
    subsections retain proposal/suggestion language for spore-wall and branch regulation.
    Finnigan directly tests vegetative yeast Bni5/Myo1 recruitment. These do not establish
    the full combined definition, whose sole definition_source is GO. Five genes are
    treated as examples, not an ordered rod.
  evidence_ids:
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-douglas-pmc
  - septin-septin-agent-finnigan2015-pmc
  - septin-septin-agent-go
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A5
  area: scope
  topic: Developmental examples are nonexhaustive
  outcome: supported
  target_ids:
  - GO:0032156
  summary: The two VARIABLE entries explicitly describe sporulation/chlamydospore
    arrays, supported by their GO child definitions and review context. They do not
    say that the entire septin cytoskeleton is absent in vegetative cells. No species-wide
    percentage or exclusive spore membership is inferred.
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-douglas-pmc
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-5476
  - septin-septin-agent-tax-559292
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A6
  area: evidence
  topic: Collective material versus individual assembly requirement
  outcome: unknown
  target_ids:
  - GO:0032156
  summary: ESSENTIAL is attached to the whole septin class, not separately to each
    of the five examples. Septins are defining material of the target, but the cited
    studies do not constitute removal of the whole class followed by an assembly assay.
    Individual truncation, viability or recruitment results cannot verify a five-gene
    universal assembly requirement; none is inferred.
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-finnigan2015-pmc
  - septin-septin-agent-versele-pmc
  - septin-policy
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A7
  area: graph
  topic: Supported parthood is not an assembly transition
  outcome: concern
  target_ids:
  - GO:0032156
  summary: The three edges record septin-protein, complex and band parthood. They
    do not describe how assembly happens, despite ASSEMBLY/MECHANISTIC and the mechanism
    title. Classify the existing descriptive scope accurately or encode a bounded
    supported transition.
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-finnigan2015-pmc
  - septin-policy
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A8
  area: completeness
  topic: No mandatory exhaustive inventory
  outcome: supported
  target_ids:
  - GO:0032156
  summary: The broad framework is represented through generic proteins and named substructures.
    Additional subunit groups, images, functions or quantitative dimensions are optional.
    The concrete gaps are unjustified generic-family withholding and source/taxon
    inflation in the expanded definition; specialized composition should not be promoted
    to a universal cytoskeleton inventory.
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-IPR016491
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-finnigan2015-pmc
  - septin-policy
  - septin-record-septin_cytoskeleton
- assessment_id: septin-S2353-A9
  area: evidence
  topic: Structured-source applicability
  outcome: not_applicable
  summary: Named tubulins/septins or specific regulators in the maintained definition
    trigger the molecular source policy. Fresh official catalogue has no matching
    fungal, algal or protist dataset. Therefore downstream gene/module queries are
    not applicable; this follows source coverage, not absence of expression claims.
    Historical runner failure is separately disclosed.
  target_ids:
  - GO:0032156
  evidence_ids:
  - septin-record-septin_cytoskeleton
  - septin-adapter-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-S2353-A10
  area: schema
  topic: Current native protein and original-bundle checks
  outcome: supported
  summary: Current deterministic native checks pass within their actual inventory.
    Original bundle validation/render and frozen hashes also pass; these do not resolve
    retained scientific findings or independently prove assembly necessity.
  target_ids:
  - GO:0032156
  evidence_ids:
  - septin-native-septin_cytoskeleton-verify
  - septin-native-septin_cytoskeleton-causal
  - septin-original-native-checks
- assessment_id: septin-S2353-A11
  area: identity
  topic: Spindle identity and generic topology
  outcome: supported
  target_ids:
  - GO:0005819
  summary: The whole spindle is a chromosome-segregating microtubule array, distinct
    from its poles, asters, microtubules and midzone. Native GO supports the record
    hierarchy and generic parthood convention. No whole-spindle identity replacement
    is needed.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-record-spindle
- assessment_id: septin-S2353-A12
  area: grounding
  topic: Correct combined protein class and concrete examples
  outcome: supported
  target_ids:
  - GO:0005819
  summary: The three reviewed accession/gene/reference-strain identities are correct.
    The component intentionally combines alpha and beta tubulins; broad IPR000217
    would overmatch, while either individual alpha/beta family would cover only part
    of the row. Its localization-specific grounding rationale could be clearer, but
    no forced split or inexact family assignment is warranted.
  evidence_ids:
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-spindle-agent-IPR000217
  - septin-spindle-agent-IPR002452
  - septin-spindle-agent-IPR002453
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-559292
  - septin-record-spindle
  - septin-policy
- assessment_id: septin-S2353-A13
  area: evidence
  topic: Protein identity and cited localization are separate from midzone occupancy
  outcome: supported
  target_ids:
  - GO:0005819
  summary: Native UniProt annotations contain the stated cytoskeleton-localization
    evidence links. Cederquist2012 has a human disease title but its abstract explicitly
    includes yeast genetic analysis, so the title alone is not a species mismatch.
    The two papers were checked at native abstract/annotation scope, not full-body
    scope; localization does not prove every example occupies every spindle region.
  evidence_ids:
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-spindle-agent-pmid-11739794
  - septin-spindle-agent-pmid-23001566
  - septin-record-spindle
- assessment_id: septin-S2353-A14
  area: evidence
  topic: The collective tubulin row is not three individual essentiality assertions
  outcome: unknown
  target_ids:
  - GO:0005819
  summary: Tubulin polymer is defining material of the spindle and overlap microtubules.
    ESSENTIAL formally concerns whether the structure forms without the declared component;
    no complete combined-class removal experiment was inspected. GFP-Tub1 imaging
    and individual mutant function do not establish that each TUB1/TUB2/TUB3 example
    is independently necessary.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-doi-science.277.5325.574
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-policy
  - septin-record-spindle
- assessment_id: septin-S2353-A15
  area: evidence
  topic: Added detailed mechanism exceeds its asserted GO source
  outcome: concern
  target_ids:
  - GO:0005819
  summary: The appended definition names Ase1/PRC1, Cin8/Kip1 and motor-associated
    spindle organization across yeasts, fungi, microalgae and protists. GO supplies
    the broad array/function definition. Winey identifies morphology and inferred
    spindle-fiber classes, not the molecular crossbridges. Jaspersen supports specifically
    budding-yeast Cin8/Kip1 pole separation; the full appended multi-taxon mechanism
    is not established by these sources.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-record-spindle
- assessment_id: septin-S2353-A16
  area: scope
  topic: Budding-yeast example and whole-spindle function
  outcome: supported
  target_ids:
  - GO:0005819
  summary: Winey directly supports the nuclear-spindle EM example in S.cerevisiae,
    including an S288c-background diploid; the record species label is appropriate.
    Straight abstract supports GFP-Tub1 imaging and chromosome movement. COMMON is
    qualitative occurrence, not a measured fraction of every culture. The ordinary
    chromosome-segregating whole-spindle function is supported.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-doi-science.277.5325.574
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-559292
  - septin-record-spindle
- assessment_id: septin-S2353-A17
  area: provenance
  topic: Keep GO parthood while correcting the primary citation
  outcome: concern
  target_ids:
  - GO:0005819
  summary: GO includes the aster in its broad spindle hierarchy. Winey explicitly
    says astral microtubules are outside the spindle per se and restricts its reconstruction
    to nuclear microtubules. The aster-to-spindle edge is thus valid under GO but
    misattributed to that particular primary analysis.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-record-spindle
- assessment_id: septin-S2353-A18
  area: graph
  topic: Descriptive edges do not represent the named molecular mechanism
  outcome: concern
  target_ids:
  - GO:0005819
  summary: The graph records tubulin and substructure parthood plus a whole-spindle
    segregation edge. It does not represent the named crosslinking/motor steps as
    causal transitions. The supported topology should be distinguished from its MECHANISTIC
    classification.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-policy
  - septin-record-spindle
- assessment_id: septin-S2353-A19
  area: completeness
  topic: Specific evidence repairs rather than compulsory inventory
  outcome: supported
  target_ids:
  - GO:0005819
  summary: Tubulin, major structural regions and whole-spindle function are represented.
    The actionable omissions are matching evidence for appended mechanism and accurate
    graph/source scope, not an obligatory exhaustive list of spindle proteins.
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-policy
  - septin-record-spindle
- assessment_id: septin-S2353-A20
  area: evidence
  topic: Structured-source applicability
  outcome: not_applicable
  summary: Named tubulins/septins or specific regulators in the maintained definition
    trigger the molecular source policy. Fresh official catalogue has no matching
    fungal, algal or protist dataset. Therefore downstream gene/module queries are
    not applicable; this follows source coverage, not absence of expression claims.
    Historical runner failure is separately disclosed.
  target_ids:
  - GO:0005819
  evidence_ids:
  - septin-record-spindle
  - septin-adapter-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-S2353-A21
  area: schema
  topic: Current native protein and original-bundle checks
  outcome: supported
  summary: Current deterministic native checks pass within their actual inventory.
    Original bundle validation/render and frozen hashes also pass; these do not resolve
    retained scientific findings or independently prove assembly necessity.
  target_ids:
  - GO:0005819
  evidence_ids:
  - septin-native-spindle-verify
  - septin-native-spindle-causal
  - septin-original-native-checks
- assessment_id: septin-S2353-A22
  area: identity
  topic: Overlap region is distinct from the entire spindle
  outcome: supported
  target_ids:
  - GO:0051233
  summary: GO0051233 identifies the region where microtubules from opposite poles
    overlap; its spindle parthood is correct. Microtubule segments occupy the overlap,
    but not every spindle microtubule is thereby wholly contained in the midzone.
    The record should retain this regional boundary when describing parts.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A23
  area: grounding
  topic: Correct combined protein class and concrete examples
  outcome: supported
  target_ids:
  - GO:0051233
  summary: The three reviewed accession/gene/reference-strain identities are correct.
    The component intentionally combines alpha and beta tubulins; broad IPR000217
    would overmatch, while either individual alpha/beta family would cover only part
    of the row. Its localization-specific grounding rationale could be clearer, but
    no forced split or inexact family assignment is warranted.
  evidence_ids:
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-spindle-agent-IPR000217
  - septin-spindle-agent-IPR002452
  - septin-spindle-agent-IPR002453
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-559292
  - septin-record-spindle_midzone
  - septin-policy
- assessment_id: septin-S2353-A24
  area: evidence
  topic: Protein identity and cited localization are separate from midzone occupancy
  outcome: supported
  target_ids:
  - GO:0051233
  summary: Native UniProt annotations contain the stated cytoskeleton-localization
    evidence links. Cederquist2012 has a human disease title but its abstract explicitly
    includes yeast genetic analysis, so the title alone is not a species mismatch.
    The two papers were checked at native abstract/annotation scope, not full-body
    scope; localization does not prove every example occupies every spindle region.
  evidence_ids:
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-spindle-agent-pmid-11739794
  - septin-spindle-agent-pmid-23001566
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A25
  area: evidence
  topic: The collective tubulin row is not three individual essentiality assertions
  outcome: unknown
  target_ids:
  - GO:0051233
  summary: Tubulin polymer is defining material of the spindle and overlap microtubules.
    ESSENTIAL formally concerns whether the structure forms without the declared component;
    no complete combined-class removal experiment was inspected. GFP-Tub1 imaging
    and individual mutant function do not establish that each TUB1/TUB2/TUB3 example
    is independently necessary.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-doi-science.277.5325.574
  - septin-spindle-agent-P09733
  - septin-spindle-agent-P02557
  - septin-spindle-agent-P09734
  - septin-policy
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A26
  area: graph
  topic: Whole-spindle kinetochore coupling is not a midzone-specific mechanism
  outcome: concern
  target_ids:
  - GO:0051233
  summary: The function, process-node description and midzone-to-segregation edge
    copy the whole-spindle claim about moving chromosomes through kinetochore coupling.
    Their nearest GO evidence defines the entire spindle. Midzone participation in
    chromosome separation is reasonable, but that does not establish this regional
    structure as the whole kinetochore-coupling apparatus. Winey supports overlap/interpolar
    elongation context while explicitly retaining inferences about kinetochore fibers.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-doi-science.277.5325.574
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A27
  area: evidence
  topic: Specific regulators are not supplied by the ontology definition
  outcome: concern
  target_ids:
  - GO:0051233
  summary: GO defines the overlap region but does not provide the appended Ase1/PRC1,
    Cin8/Kip1 and Ipl1/Sli15/Bir1 mechanism. The readable ultrastructure does not
    identify those crossbridges or test chromosomal-passenger regulation. The yeast
    SPB review supports a narrower Cin8/Kip1 separation context, not the entire multi-taxon
    central-spindle assertion.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A28
  area: provenance
  topic: A plausible phrase is not a source-provided exact synonym
  outcome: concern
  target_ids:
  - GO:0051233
  summary: Native GO0051233 contains central spindle and spindle equator as exact
    synonyms. It does not supply the maintained central spindle overlap zone string.
    The phrase can be curated independently, but its current GO attribution is inaccurate.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A29
  area: scope
  topic: Yeast spindle reconstruction provides overlap-region context
  outcome: supported
  target_ids:
  - GO:0051233
  summary: Winey analyzes central overlap/interdigitation within nuclear yeast spindles,
    supporting the species example. The canonical/distribution notes are broad whole-spindle
    descriptions and could be more specific, but do not assert an incorrect organism.
    No exact strain identity is inferred beyond the source Methods.
  evidence_ids:
  - septin-spindle-agent-winey1995-pdf
  - septin-septin-agent-tax-4932
  - septin-septin-agent-tax-559292
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A30
  area: graph
  topic: Descriptive topology and a transferred function are not a mechanistic explanation
  outcome: concern
  target_ids:
  - GO:0051233
  summary: The graph gives parthood and a whole-structure mediates edge without a
    represented overlap-sliding, stabilization or other causal transition. Correct
    the function attribution and classify the residual descriptive graph accurately;
    no molecular-detail quota is imposed.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-policy
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A31
  area: completeness
  topic: Correct regional claims before adding optional molecular inventory
  outcome: supported
  target_ids:
  - GO:0051233
  summary: No exhaustive midzone regulator inventory is mandatory. The consequential
    gaps are source support for specific mechanisms, whole-versus-part functional
    attribution and a source-labeled synonym, while the basic overlap identity and
    tubulin class remain sound.
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-policy
  - septin-record-spindle_midzone
- assessment_id: septin-S2353-A32
  area: evidence
  topic: Structured-source applicability
  outcome: not_applicable
  summary: Named tubulins/septins or specific regulators in the maintained definition
    trigger the molecular source policy. Fresh official catalogue has no matching
    fungal, algal or protist dataset. Therefore downstream gene/module queries are
    not applicable; this follows source coverage, not absence of expression claims.
    Historical runner failure is separately disclosed.
  target_ids:
  - GO:0051233
  evidence_ids:
  - septin-record-spindle_midzone
  - septin-adapter-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-S2353-A33
  area: schema
  topic: Current native protein and original-bundle checks
  outcome: supported
  summary: Current deterministic native checks pass within their actual inventory.
    Original bundle validation/render and frozen hashes also pass; these do not resolve
    retained scientific findings or independently prove assembly necessity.
  target_ids:
  - GO:0051233
  evidence_ids:
  - septin-native-spindle_midzone-verify
  - septin-native-spindle_midzone-causal
  - septin-original-native-checks
- assessment_id: septin-S2353-A34
  area: identity
  topic: Generic pole is broader than a spindle pole body
  outcome: supported
  target_ids:
  - GO:0000922
  summary: The target is the polar spindle region, with spindle parthood and a species-specific
    SPB structural example. It is not equated to only the budding-yeast SPB. The native
    definition says it usually contains an MTOC; the record distribution also acknowledges
    acentrosomal poles.
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-pole-agent-tax-2759
  - septin-septin-agent-tax-4932
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A35
  area: grounding
  topic: GO0000930 correctly covers generic gamma-tubulin complexes
  outcome: supported
  target_ids:
  - GO:0000922
  summary: The component label and role explicitly cover gamma-TuSC/gamma-TuRC. Native
    GO0000930 is the generic gamma-tubulin complex with species-variable partners;
    its small-complex and ring-complex children must not be confused with the parent.
    This mapping does not assert that every complex has universal ring geometry or
    the same subunits.
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-spindle-agent-viswanath2017
  - septin-record-spindle_pole
  - septin-policy
- assessment_id: septin-S2353-A36
  area: evidence
  topic: The broad pole definition adds a source-unmatched molecular roster
  outcome: concern
  target_ids:
  - GO:0000922
  summary: The appended text combines kinesin-14, NuMA/Pkl1/Mto1 and gamma-tubulin-ring
    machinery across yeasts, fungi, microalgae and protists. GO supplies the generic
    regional definition, while Jaspersen is a yeast-SPB review with a centrosome comparison.
    Its readable sections and Viswanath core context do not establish that entire
    named combination throughout those groups.
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-spindle-agent-viswanath2017
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A37
  area: scope
  topic: Keep yeast pole-duplication evidence at its actual scope
  outcome: concern
  target_ids:
  - GO:0000922
  summary: The review supports budding-yeast SPB duplication, bridge cleavage and
    Cin8/Kip1-dependent separation. Its centrosome comparison explicitly preserves
    similarities and differences. The record evidence notes generalize this to spindle-pole
    duplication across eukaryotes, including the acentrosomal scope it otherwise acknowledges,
    without matching evidence.
  evidence_ids:
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-spindle-agent-jaspersen-browser
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A38
  area: evidence
  topic: Presence and nucleation do not establish universal assembly necessity
  outcome: unknown
  target_ids:
  - GO:0000922
  summary: Both components are ESSENTIAL. Source evidence for yeast MTOC organization
    and gamma-complex nucleation supports membership/function in that system, but
    does not show that the broad spindle-pole structure fails to form without each
    generic component across its taxonomic scope. The schema criterion is formation,
    not catalytic function, cell viability or presence in the intact reference architecture.
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-spindle-agent-viswanath2017
  - septin-record-spindle_pole
  - septin-policy
- assessment_id: septin-S2353-A39
  area: scope
  topic: Broad occurrence and canonical yeast architecture
  outcome: supported
  target_ids:
  - GO:0000922
  summary: Eukaryota and S.cerevisiae labels/ranks are correct; the yeast canonical
    SPB architecture example is supported. COMMON is not treated as a measured prevalence.
    The broad terminal-region identity does not authorize exporting the exact yeast
    molecular or duplication mechanism to every eukaryote.
  evidence_ids:
  - septin-pole-agent-go
  - septin-pole-agent-tax-2759
  - septin-septin-agent-tax-4932
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-viswanath2017
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A40
  area: provenance
  topic: GO does not supply the maintained narrow synonym
  outcome: concern
  target_ids:
  - GO:0000922
  summary: Native GO0000922 contains no synonym annotation in the inspected response.
    Mitotic spindle pole is a plausible narrower phrase, but its GO source attribution
    is unsupported and should be repaired rather than mistaken for a source-provided
    synonym.
  evidence_ids:
  - septin-pole-agent-go
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A41
  area: graph
  topic: Organizational description lacks a represented causal transition
  outcome: concern
  target_ids:
  - GO:0000922
  summary: The graph links MTOC/gamma-complex/SPB parts and whole-pole functions.
    Its text describes nucleation/anchoring and duplication, but the edges do not
    represent those transitions or the component-to-function dependency. Keep supported
    topology distinct from the stronger MECHANISTIC scope claim.
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-policy
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A42
  area: completeness
  topic: No forced molecular census for a generic polar region
  outcome: supported
  target_ids:
  - GO:0000922
  summary: The two class-level components have valid identities. Exact protein examples,
    stoichiometry, family splitting and full centrosome/SPB inventories are optional.
    The material problem is unsupported broad mechanism, with assembly necessity explicitly
    unresolved; optional inventory is not promoted to a finding.
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-policy
  - septin-record-spindle_pole
- assessment_id: septin-S2353-A43
  area: evidence
  topic: Structured-source applicability
  outcome: not_applicable
  summary: Named tubulins/septins or specific regulators in the maintained definition
    trigger the molecular source policy. Fresh official catalogue has no matching
    fungal, algal or protist dataset. Therefore downstream gene/module queries are
    not applicable; this follows source coverage, not absence of expression claims.
    Historical runner failure is separately disclosed.
  target_ids:
  - GO:0000922
  evidence_ids:
  - septin-record-spindle_pole
  - septin-adapter-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner
- assessment_id: septin-S2353-A44
  area: schema
  topic: Current native protein and original-bundle checks
  outcome: supported
  summary: Current deterministic native checks pass within their actual inventory.
    Original bundle validation/render and frozen hashes also pass; these do not resolve
    retained scientific findings or independently prove assembly necessity.
  target_ids:
  - GO:0000922
  evidence_ids:
  - septin-native-spindle_pole-verify
  - septin-native-spindle_pole-causal
  - septin-original-native-checks
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 5 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0061645
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0034993
  - GO:1990612
  - GO:0032156
  - GO:0005819
  - GO:0051233
  - GO:0000922
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
- finding_id: plaque-target0-F1
  issue_key: endocytic-patch-expanded-definition-source-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Source and qualify the added yeast mechanism separately from the GO definition
  description: The definition extends the broad GO text with a detailed fungal coat/adaptor/NPF/scission
    sequence and turgor mechanism while retaining only GO0061645 as its source. The
    inspected yeast papers support scoped examples and distinguish early coats, actin
    recruitment and later movement. Attach the appropriate sources and stage/taxon
    qualifiers, or retain the exact broad definition with the detailed material in
    supported example notes.
  target_ids:
  - GO:0061645
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - plaque-current-0
  - plaque-endocytic-prep-go
  - plaque-endocytic-prep-galletta2008-plos
  - plaque-endocytic-prep-aghamohammadzadeh2009-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/endocytic_patch.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported identity and basic biology remain intact; this
    is a bounded source-attribution or graph-representation defect.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094807Z-endocytic-patch-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2588
- finding_id: plaque-target0-F2
  issue_key: endocytic-patch-self-assembly-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Specify assembly stages and recruited machinery or narrow graph scope
  description: 'The FUNCTION/MECHANISTIC graph is a membership/function summary, and
    the patch-to-actin-cortical-patch-assembly edge cites only a GO process definition.
    The broad endocytic patch can precede its actin-rich stage: the inspected studies
    describe early regulator recruitment followed by network assembly. The present
    graph does not specify those stages or the recruited causal machinery. Preserve
    valid membership/output context as NONMECHANISTIC or add a source-supported, stage-specific
    causal transition; do not treat this as proof that an early endocytic patch cannot
    organize later actin assembly.'
  target_ids:
  - GO:0061645
  field_paths:
  - causal_graphs[graph_id=endocytic_patch_mechanism].scope_status
  - causal_graphs[graph_id=endocytic_patch_mechanism].edges[subject=endocytic_patch,object=actin_cortical_patch_assembly]
  evidence_ids:
  - plaque-current-0
  - plaque-graph-contract
  - plaque-endocytic-prep-go
  - plaque-endocytic-prep-galletta2008-plos
  - plaque-endocytic-prep-kaksonen2003-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/endocytic_patch.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported identity and basic biology remain intact; this
    is a bounded source-attribution or graph-representation defect.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094807Z-endocytic-patch-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2589
- finding_id: plaque-target4-F1
  issue_key: meiotic-membrane-tether-horsetail-array-function-transfer
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Keep the membrane tether distinct from the horsetail-astral array
  description: The function description and corresponding graph process/edge state
    that the membrane complex provides the radial microtubule array. Their GO0032117
    evidence is called the exact structure definition, but that term denotes the HAA
    rather than GO0034993. Funaya2012 directly distinguishes array/rMTOC organization
    from the envelope bridge. Correct the actor/function and evidence placement without
    discarding the supported role in connecting chromosomes, membranes and the cytoskeleton.
  target_ids:
  - GO:0034993
  field_paths:
  - functions[function_id=horsetail_movement]
  - evidence[reference=GO:0032117]
  - causal_graphs[graph_id=meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism].nodes[node_id=horsetail_movement]
  - causal_graphs[graph_id=meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism].edges[object=horsetail_movement]
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-go
  - plaque-tether-prep-paper
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: The represented structure is assigned a materially different
    structure function or an unsupported broad taxonomic mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2590
- finding_id: plaque-target4-F2
  issue_key: meiotic-membrane-tether-fungi-dynein-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bound the taxonomic and motor claim to demonstrated systems
  description: The Fungi COMMON annotation and conserved dynein-coupling note are
    sourced to Chikashige2006, whose primary abstract establishes an S.pombe Bqt1/Bqt2
    bridge. That does not demonstrate the frequency or motor mechanism of a microtubule-tethering
    complex across fungi. Lee2020 examines a related budding-yeast LINC/Myo2/actin
    system, so generic SUN/KASH conservation cannot fill that gap. This is not a claim
    that no other fungus has a microtubule-linked tether.
  target_ids:
  - GO:0034993
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:4751]
  - definition
  evidence_ids:
  - plaque-current-4
  - plaque-tether-prep-doi-j.cell.2006.01.048-meta
  - plaque-linc-agent-csm2020-jats
  - plaque-tether-prep-tax-4751
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: major
  normalization_reason: The represented structure is assigned a materially different
    structure function or an unsupported broad taxonomic mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2591
- finding_id: plaque-target4-F3
  issue_key: meiotic-membrane-tether-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Use an honest scope for the current membership/function graph
  description: Even after correcting the copied HAA function, the graph has only constituent/compartment
    relations and a whole-structure output. It does not encode a tethering or force-transmission
    causal transition, despite MECHANISTIC scope. Use NONMECHANISTIC or represent
    a directly sourced transition with the proper actor and preparation.
  target_ids:
  - GO:0034993
  field_paths:
  - causal_graphs[graph_id=meiotic_nuclear_membrane_microtubule_tethering_complex_mechanism].scope_status
  evidence_ids:
  - plaque-current-4
  - plaque-graph-contract
  - plaque-tether-prep-paper
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and claim scope; review-checklist
  native_severity: minor
  normalization_reason: The supported identity and basic biology remain intact; this
    is a bounded source-attribution or graph-representation defect.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2592
- finding_id: plaque-target5-F1
  issue_key: sad1-kms1-fungal-linc-scope-transfer
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Budding-yeast assays and broad fungal coupling are assigned to the named
    complex
  description: Fan2020 directly tests budding-yeast Mps2–Mps3–Csm4, while both Fan-only
    output edges use Sad1–Kms1 as their subject. The pairing description acknowledges
    budding yeast but that qualifier does not change the graph subject or make the
    result an assay of Sad1–Kms1. The Fungi COMMON note likewise generalizes this
    named assembly and dynein/microtubule coupling from fission yeast, despite the
    distinct actin-associated budding-yeast system. Separate comparative LINC context
    from functions/distribution of the named S. pombe assembly. This is not a claim
    that Sad1–Kms1 lacks telomere or recombination roles.
  target_ids:
  - GO:1990612
  field_paths:
  - functions[function_id=pairing_and_recombination]
  - functions[function_id=telomere_organization].evidence
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].edges
  - taxonomic_distribution[0]
  evidence_ids:
  - plaque-current-5
  - plaque-linc-agent-fan2020-jats
  - plaque-linc-agent-csm2020-jats
  - plaque-tether-prep-doi-j.cell.2006.01.048-meta
  - plaque-linc-agent-yoshida2013-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  rule_id: review-checklist:Taxonomic scope and Evidence standard; docs/CURATION.md:Evidence
  native_severity: major
  normalization_reason: Major because the molecular subject and taxonomic/motor scope
    of existing causal assignments exceed their direct evidence; this is more than
    an imprecise citation label. Exact named identity and the native parent remain
    valid.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094818Z-sad1-kms1-linc-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2593
- finding_id: plaque-target5-F2
  issue_key: sad1-kms1-summary-graph-overstates-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Membership and functional outputs are labeled mechanistic
  description: The seven-node graph presents membership/association and whole-complex
    outputs, without a represented chain explaining how the LINC bridge produces those
    outcomes. Retain FUNCTION but use honest NONMECHANISTIC scope with notes, or add
    independently supported causal intermediates and exact edge evidence during authorized
    curation. This classification issue is separate from the cross-species assignment
    in F1.
  target_ids:
  - GO:1990612
  field_paths:
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].scope_status
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].description
  - causal_graphs[graph_id=sad1_kms1_linc_complex_mechanism].edges
  evidence_ids:
  - plaque-current-5
  - plaque-graph-contract
  - plaque-linc-agent-yoshida2013-jats
  - plaque-tether-prep-moiseeva2017-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml:CausalGraphScopeEnum;
    review-checklist:Causal graph
  native_severity: minor
  normalization_reason: Minor because supported membership and bounded functional
    associations can remain after scope correction; the graph representation omits
    explanatory steps without independently inventing a new molecular mechanism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094818Z-sad1-kms1-linc-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2594
- finding_id: micro-F1
  issue_key: wrong-fission-yeast-source
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace the budding-yeast paper assigned to fission-yeast composition and
    example
  description: 'DOI10.1091/mbc.E17-06-0397 is explicitly a S. cerevisiae SPB-core
    study. The component evidence and duplicated graph evidence instead say it characterizes
    fission-yeast Alp4/Alp6, and the canonical S. pombe972h- example says it dissects
    gamma-TuSC assembly and Mto1/Mto2 nucleation. Those experiments are not in this
    cited primary source. The underlying fission-yeast biology has suitable primary
    evidence, so this is an evidence/organism attribution error rather than a wrong
    GO identity. Current budding-yeast evidence added under #2470 is present but does
    not correct the remaining fission-yeast source assignment.'
  target_ids:
  - GO:0000930
  - GO:0008275
  field_paths:
  - components[component_id=gcp2_gcp3_spoke_subunits].evidence
  - canonical_examples[0].reference
  - causal_graphs[0].edges[subject=gcp2_gcp3_spoke_subunits].evidence
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-record-gamma_tubulin_small_complex
  - micro-viswanath2017
  - micro-samejima2010
  - micro-samejima2008
  - micro-anders2006
  - micro-issue-2470
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    role: maintained scientific record
  rule_id: 'review-checklist: evidence scope, taxonomic examples, components and causal
    graphs'
  native_severity: major
  normalization_reason: An affirmative source attribution assigns experiments or detailed
    mechanisms that the cited primary body did not establish.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094810Z-gamma-tubulin-complex-audit
    finding_id: F1
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094813Z-gamma-tubulin-small-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2595
- finding_id: micro-F2
  issue_key: spb-function-and-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Describe the complex contribution and align graph scope
  description: The function descriptions make the SPB, including SPB duplication and
    separation, their acting structure. The graph repeats those descriptions and labels
    a membership/context/output summary MECHANISTIC. Gamma-complex nucleation is supported,
    but these fields do not explain its molecular contribution or a causal path.
  target_ids:
  - GO:0000930
  - GO:0008275
  field_paths:
  - functions
  - causal_graphs[0].scope_status
  - causal_graphs[0].nodes
  - causal_graphs[0].edges
  evidence_ids:
  - micro-record-gamma_tubulin_complex
  - micro-record-gamma_tubulin_small_complex
  - micro-jaspersen-secondary
  - micro-lyon2016
  - micro-brilot2021
  - micro-graph-rubric
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    role: maintained scientific record
  rule_id: 'review-checklist: evidence scope, taxonomic examples, components and causal
    graphs'
  native_severity: minor
  normalization_reason: The exact complex and supported membership are retained; this
    bounded graph/function representation needs clarification.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094810Z-gamma-tubulin-complex-audit
    finding_id: F2
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094813Z-gamma-tubulin-small-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2596
- finding_id: micro-F3
  issue_key: ring-structure-and-allostery-source-inflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate ring architecture and activation claims from the cited targeting
    studies
  description: The record says Samejima2010 establishes TuSC assembly into a13-protofilament-matching
    ring, and E04-11-1003 characterizes Gfh1/Mod21/Alp16 as a14-spoke asymmetric seam.
    Their full bodies instead study Mto1 targeting and Mto2-mediated recruitment.
    The Mto1-Mto2 role further states allosteric activation under Samejima2010, whereas
    the later direct activation study uses bonsai puncta and explicitly leaves conformational/CM1-alone
    activation unresolved. Basic membership and nucleation are supported; these exact
    structural/mechanistic source attributions are not. The expanded reviewed protein
    examples and corrected grouped types establish identity/representation only; they
    do not repair these source-attribution defects.
  target_ids:
  - GO:0000931
  field_paths:
  - components[component_id=gamma_tusc_repeating_core].role
  - components[component_id=gamma_tusc_repeating_core].evidence
  - components[component_id=gcp4_gcp5_gcp6_ring_subunits]
  - components[component_id=mto1_mto2_activating_tether].role
  - components[component_id=mto1_mto2_activating_tether].evidence
  - causal_graphs[0].nodes
  - causal_graphs[0].edges
  - definition
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-samejima2010
  - micro-samejima2005
  - micro-anders2006
  - micro-lynch2014
  - micro-brilot2021
  - micro-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    role: maintained scientific record
  rule_id: 'review-checklist: evidence scope, taxonomic examples, components and causal
    graphs'
  native_severity: major
  normalization_reason: An affirmative source attribution assigns experiments or detailed
    mechanisms that the cited primary body did not establish.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094812Z-gamma-tubulin-ring-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2597
- finding_id: micro-F4
  issue_key: ring-graph-summary-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Align the graph label with its represented causal detail
  description: After correcting the source overstatements, the current graph still
    consists of component parthood, Mto1-Mto2 association and whole-complex-to-nucleation.
    These relationships can be supported as a functional/structural summary, but they
    do not themselves trace a resolved molecular mechanism despite scope_status MECHANISTIC.
  target_ids:
  - GO:0000931
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].graph_kind
  - causal_graphs[0].edges
  evidence_ids:
  - micro-record-gamma_tubulin_ring_complex
  - micro-samejima2010
  - micro-lynch2014
  - micro-anders2006
  - micro-graph-rubric
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    role: maintained scientific record
  rule_id: 'review-checklist: evidence scope, taxonomic examples, components and causal
    graphs'
  native_severity: minor
  normalization_reason: The exact complex and supported membership are retained; this
    bounded graph/function representation needs clarification.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094812Z-gamma-tubulin-ring-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2598
- finding_id: septin-S2353-F1
  issue_key: septin-cytoskeleton-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the generic septin class at its actual family scope
  description: The generic septin-proteins row is REVIEWED_LABEL_ONLY because no identifier
    was assigned for the complete filament-array-forming cohort. Native IPR016491
    identifies the Septin family, matching this generic component without identifying
    every assembly-specific member. Correct the class-versus-cohort criterion and
    preserve source-specific membership limits.
  target_ids:
  - GO:0032156
  field_paths:
  - components[component_id=septin_proteins].grounding
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  evidence_ids:
  - septin-septin-agent-IPR016491
  - septin-septin-agent-go
  - septin-record-septin_cytoskeleton
  - septin-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The existing biological class and concrete examples are correct;
    this is a bounded grounding omission caused by an overly narrow criterion.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094819Z-septin-cytoskeleton-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
- finding_id: septin-S2353-F2
  issue_key: septin_cytoskeleton_mechanism-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented relationships
  description: The ASSEMBLY graph contains only constituent-to-cytoskeleton parthood
    edges. Its descriptions mention biological activities, but the graph does not
    connect an explicit assembly or functional transition to those activities. MECHANISTIC
    overstates what is represented; this is a scope classification concern, not a
    claim that the supported topology is false or a demand for atomic detail.
  target_ids:
  - GO:0032156
  field_paths:
  - causal_graphs[graph_id=septin_cytoskeleton_mechanism].scope_status
  - causal_graphs[graph_id=septin_cytoskeleton_mechanism].scope_notes
  - causal_graphs[graph_id=septin_cytoskeleton_mechanism].edges
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-finnigan2015-pmc
  - septin-policy
  - septin-record-septin_cytoskeleton
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The identities and many relationships remain useful. The bounded
    correction concerns the promised explanatory scope, not biological identity or
    missing optional components.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094819Z-septin-cytoskeleton-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2576
- finding_id: septin-S2353-F3
  issue_key: septin-cytoskeleton-definition-taxon-function-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate supported fungal functions from unverified green-algal architecture
  description: The expanded definition presents a plasma-membrane septin network across
    yeasts, filamentous fungi and green algae and combines barrier/scaffold recruitment
    at bud necks, hyphal branches and prospore membranes, while definition_source
    cites only GO0032156. Versele supports green-algal septin ortholog occurrence,
    not that full cortical architecture or function. Its functional examples concern
    yeast; Douglas retains proposal-level language for branch regulator and spore-wall
    recruitment, and Finnigan directly studies vegetative budding yeast. Supply matching
    evidence and qualifiers for the retained expansion rather than carrying these
    narrower observations across the entire taxon/site list.
  target_ids:
  - GO:0032156
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-septin-agent-go
  - septin-septin-agent-versele-pmc
  - septin-septin-agent-douglas-pmc
  - septin-septin-agent-finnigan2015-pmc
  - septin-record-septin_cytoskeleton
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: The unsupported taxon and function extension is part of the
    defining biological claim, consistent with the major rubric for evidence scope
    inflation. It does not establish that green algae lack septin structures or that
    the proposed fungal functions are false.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094819Z-septin-cytoskeleton-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2577
- finding_id: septin-S2353-F4
  issue_key: spindle-definition-molecular-source-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Source and delimit the added molecular spindle mechanism
  description: Only GO0005819 is named as definition_source, but the appended definition
    asserts specific Ase1/PRC1, Cin8/Kip1 and motor mechanisms across broad microbial
    eukaryote groups. The inspected primary ultrastructure and yeast review do not
    establish that entire combined assertion. Retain the correct broad definition
    and either provide inspected, taxon-matched evidence for the specific mechanism
    or narrow it to what the cited sources show.
  target_ids:
  - GO:0005819
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-record-spindle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Unsupported molecular and taxonomic specificity is part of
    the defining mechanism. This is an evidence/scope issue, not proof that the named
    proteins have no spindle role.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094822Z-spindle-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2578
- finding_id: septin-S2353-F5
  issue_key: spindle-aster-parthood-winey-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Cite the native ontology for the generic aster relationship
  description: The aster-to-spindle edge cites Winey1995. That paper explicitly excludes
    astral microtubules from the spindle per se and analyzes intranuclear microtubules.
    GO supports the broader class relation, so correct the evidence attribution without
    deleting the valid generic topology.
  target_ids:
  - GO:0005819
  field_paths:
  - causal_graphs[graph_id=spindle_mechanism].edges[subject=aster,predicate=is part
    of,object=spindle].evidence
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-record-spindle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The relationship itself is supported at the ontology scope;
    the defect is bounded source attribution.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094822Z-spindle-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2579
- finding_id: septin-S2353-F6
  issue_key: spindle_mechanism-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented relationships
  description: The FUNCTION graph contains structural parthood and whole-structure-to-process
    mediates edges. Its descriptions mention biological activities, but the graph
    does not connect an explicit assembly or functional transition to those activities.
    MECHANISTIC overstates what is represented; this is a scope classification concern,
    not a claim that the supported topology is false or a demand for atomic detail.
  target_ids:
  - GO:0005819
  field_paths:
  - causal_graphs[graph_id=spindle_mechanism].scope_status
  - causal_graphs[graph_id=spindle_mechanism].scope_notes
  - causal_graphs[graph_id=spindle_mechanism].edges
  evidence_ids:
  - septin-spindle-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-policy
  - septin-record-spindle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The identities and many relationships remain useful. The bounded
    correction concerns the promised explanatory scope, not biological identity or
    missing optional components.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094822Z-spindle-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2580
- finding_id: septin-S2353-F7
  issue_key: midzone-whole-spindle-kinetochore-function-transfer
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Give the midzone a region-specific contribution to segregation
  description: The function and graph directly attach whole-spindle kinetochore-coupling
    prose to the midzone, citing the whole-spindle GO definition. Preserve the supported
    overlap identity and an appropriately qualified contribution to segregation, but
    describe the regional process actually supported by evidence instead of transferring
    the entire spindle mechanism.
  target_ids:
  - GO:0051233
  field_paths:
  - functions[function_id=chromosome_segregation]
  - causal_graphs[graph_id=spindle_midzone_mechanism].nodes[node_id=chromosome_segregation]
  - causal_graphs[graph_id=spindle_midzone_mechanism].edges[subject=spindle_midzone,predicate=mediates,object=chromosome_segregation]
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-doi-science.277.5325.574
  - septin-record-spindle_midzone
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: The maintained function confuses the target region with its
    containing apparatus, altering the causal interpretation. This does not deny that
    overlap-region activity contributes to chromosome segregation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094824Z-spindle-midzone-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2581
- finding_id: septin-S2353-F8
  issue_key: midzone-regulator-definition-source-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Support the added midzone regulator mechanism at its taxon scope
  description: The definition cites only GO0051233 while adding Ase1/PRC1, Cin8/Kip1
    and chromosomal-passenger identities as an organizing mechanism across yeasts,
    fungi and microbial eukaryotes. Neither that GO definition nor the inspected primary
    morphology establishes the entire assertion. The claim needs a matching inspected
    source and organism/stage qualification.
  target_ids:
  - GO:0051233
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-record-spindle_midzone
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This concerns unsupported specific molecular mechanism and
    taxonomic generalization, not the correctness of the basic overlap definition
    or a demand for optional component rows.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094824Z-spindle-midzone-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2582
- finding_id: septin-S2353-F9
  issue_key: midzone-go-synonym-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the GO attribution of the added synonym
  description: The maintained exact synonym central spindle overlap zone is not a
    synonym supplied by the inspected native GO0051233 record. GO instead supplies
    central spindle and spindle equator. Repair the provenance or use an actual source-provided
    synonym.
  target_ids:
  - GO:0051233
  field_paths:
  - synonyms[synonym_text=central spindle overlap zone]
  evidence_ids:
  - septin-midzone-agent-go
  - septin-record-spindle_midzone
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: This is a non-blocking provenance error; the phrase does not
    change the target overlap-region identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094824Z-spindle-midzone-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2583
- finding_id: septin-S2353-F10
  issue_key: spindle_midzone_mechanism-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented relationships
  description: The FUNCTION graph contains structural parthood and whole-structure-to-process
    mediates edges. Its descriptions mention biological activities, but the graph
    does not connect an explicit assembly or functional transition to those activities.
    MECHANISTIC overstates what is represented; this is a scope classification concern,
    not a claim that the supported topology is false or a demand for atomic detail.
  target_ids:
  - GO:0051233
  field_paths:
  - causal_graphs[graph_id=spindle_midzone_mechanism].scope_status
  - causal_graphs[graph_id=spindle_midzone_mechanism].scope_notes
  - causal_graphs[graph_id=spindle_midzone_mechanism].edges
  evidence_ids:
  - septin-midzone-agent-go
  - septin-spindle-agent-winey1995-pdf
  - septin-policy
  - septin-record-spindle_midzone
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The identities and many relationships remain useful. The bounded
    correction concerns the promised explanatory scope, not biological identity or
    missing optional components.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094824Z-spindle-midzone-audit
    finding_id: F4
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2584
- finding_id: septin-S2353-F11
  issue_key: spindle-pole-mechanism-taxonomic-source-inflation
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Bound the specific pole mechanism and duplication claims to their evidence
  description: The definition adds a combined kinesin-14/NuMA/Pkl1/Mto1/gamma-ring
    mechanism across broad microbial eukaryote groups while citing only the generic
    GO definition. The function and graph evidence further say the yeast-focused review
    establishes pole duplication/separation across eukaryotes. The inspected review
    and primary yeast-core context support narrower claims; neither establishes this
    whole combined generalization.
  target_ids:
  - GO:0000922
  field_paths:
  - definition
  - definition_source
  - functions[function_id=bipolar_spindle_assembly]
  - causal_graphs[graph_id=spindle_pole_mechanism].nodes[node_id=bipolar_spindle_assembly]
  - causal_graphs[graph_id=spindle_pole_mechanism].edges[subject=spindle_pole,predicate=mediates,object=bipolar_spindle_assembly]
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-spindle-agent-viswanath2017
  - septin-record-spindle_pole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is molecular and taxonomic scope inflation affecting
    the stated causal mechanism. Generic spindle-pole and gamma-complex identities
    remain correct.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094825Z-spindle-pole-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2585
- finding_id: septin-S2353-F12
  issue_key: spindle-pole-narrow-synonym-go-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Repair the source attribution of the narrow pole synonym
  description: The phrase mitotic spindle pole is labeled a GO0000922 narrow synonym,
    but the native term does not supply that synonym. Preserve it only with an appropriate
    independent source/curator provenance or use the source-provided annotations.
  target_ids:
  - GO:0000922
  field_paths:
  - synonyms[synonym_text=mitotic spindle pole]
  evidence_ids:
  - septin-pole-agent-go
  - septin-record-spindle_pole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The phrase is a plausible narrowing and does not change target
    identity; the defect is a bounded source-provenance claim.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094825Z-spindle-pole-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2586
- finding_id: septin-S2353-F13
  issue_key: spindle_pole_mechanism-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented relationships
  description: The FUNCTION graph contains structural parthood and whole-structure-to-process
    mediates edges. Its descriptions mention biological activities, but the graph
    does not connect an explicit assembly or functional transition to those activities.
    MECHANISTIC overstates what is represented; this is a scope classification concern,
    not a claim that the supported topology is false or a demand for atomic detail.
  target_ids:
  - GO:0000922
  field_paths:
  - causal_graphs[graph_id=spindle_pole_mechanism].scope_status
  - causal_graphs[graph_id=spindle_pole_mechanism].scope_notes
  - causal_graphs[graph_id=spindle_pole_mechanism].edges
  evidence_ids:
  - septin-pole-agent-go
  - septin-spindle-agent-jaspersen-browser
  - septin-spindle-agent-jaspersen-duplication-browser
  - septin-spindle-agent-jaspersen-nucleation-browser
  - septin-policy
  - septin-record-spindle_pole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The identities and many relationships remain useful. The bounded
    correction concerns the promised explanatory scope, not biological identity or
    missing optional components.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094825Z-spindle-pole-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2587
actions:
- action_id: plaque-target0-A1
  finding_ids:
  - plaque-target0-F1
  target_ids:
  - GO:0061645
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/endocytic_patch.yaml
    role: maintained scientific record
  description: Preserve the generic endocytic-patch identity while attributing the
    added molecular and pressure-dependent details to the experiments that support
    them.
  acceptance_checks:
  - Do not collapse the broad endocytic site and its actin-rich subtype or all temporal
    phases.
  - Keep turgor-dependent invagination separate from post-scission transport and retain
    the studied yeast scope.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: plaque-target0-A2
  finding_ids:
  - plaque-target0-F2
  target_ids:
  - GO:0061645
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/endocytic_patch.yaml
    role: maintained scientific record
  description: Specify the stage and recruited machinery supporting the assembly edge,
    or represent the graph at its supported nonmechanistic level.
  acceptance_checks:
  - Distinguish the early endocytic site from its later actin-rich stage; support
    the causal transition with experimental evidence rather than the assembly-process
    definition alone.
  - Retain supported actin/Arp2/3 membership and yeast internalization evidence.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: plaque-target4-A1
  finding_ids:
  - plaque-target4-F1
  target_ids:
  - GO:0034993
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  description: Describe the supported tethering contribution and cite evidence for
    that exact role; reserve HAA organization and array identity for the corresponding
    structures.
  acceptance_checks:
  - Do not treat a neighboring structure term as the exact identity of this complex.
  - Distinguish physical linkage from microtubule nucleation, array organization and
    motor force generation.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: plaque-target4-A2
  finding_ids:
  - plaque-target4-F2
  target_ids:
  - GO:0034993
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  description: Narrow distribution/mechanism to verified taxa or provide separately
    inspected evidence for the broader microtubule-specific class, preserving the
    distinction from actin-linked LINC systems.
  acceptance_checks:
  - COMMON at a broad taxon requires evidence beyond one studied species.
  - Do not transfer specific Sad1/Kms1/Bqt or dynein identities to all fungal SUN/KASH
    assemblies.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: plaque-target4-A3
  finding_ids:
  - plaque-target4-F3
  target_ids:
  - GO:0034993
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained scientific record
  description: Calibrate graph scope independently of the supported physical membership
    statements.
  acceptance_checks:
  - Retain valid Sad1/Kms1/Bqt relationships and correct function scope.
  - A meaningful source-backed causal step suffices; no atomistic mechanism is required.
  - Apply only through separately authorized scientific curation, guarded writing,
    append-only history, rendering and native validation.
- action_id: plaque-target5-A1
  finding_ids:
  - plaque-target5-F1
  target_ids:
  - GO:1990612
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  description: During authorized curation, bind named Sad1–Kms1 functions and edges
    to appropriate fission-yeast primary passages. Retain Fan/Lee findings only as
    explicitly comparative budding-yeast context, with their actual molecular subject.
    Narrow distribution to evidenced named-complex scope and distinguish conserved
    LINC architecture from motor/taxon generalizations.
  acceptance_checks:
  - Every resulting causal edge must have the same molecular subject and organism
    as its cited assay; retain SK1/S288C versus fission-yeast distinctions.
  - Preserve supported S/G2 DSB and meiotic telomere roles without claiming that Swartz
    mitotic gene conversion is the same assay as Fan meiotic conversion.
  - Do not infer COMMON exact-subunit distribution or dynein coupling from Fungi taxonomy
    or generic SUN-family conservation.
  - Run native schema/strict, protein verify/causal coverage, fresh CURIE/history
    and scientific edge review after an authorized validated-writer change.
  generator: Maintained YAML via guarded writer; no scientific edit is made by this
    review.
- action_id: plaque-target5-A2
  finding_ids:
  - plaque-target5-F2
  target_ids:
  - GO:1990612
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained scientific record
  description: Reclassify the current graph as NONMECHANISTIC functional context with
    scope notes, or build a supported mechanistic chain. Distinguish direct localization/depletion
    results from proposed motor cross-linking, force transmission and CDK/Sad1 pathways.
  acceptance_checks:
  - Read each new intermediate and edge against its exact primary result or explicitly
    labeled model passage.
  - Preserve species, meiosis versus mitosis, preparation and mutant-background bounds.
  - Recheck graph_kind/scope_status and run focused native validators; preserve PROPOSED
    status and history unless separately authorized.
  generator: Maintained YAML graph; derived products only after authorized curation.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0000930
  - GO:0008275
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    role: maintained scientific record
  description: Replace the misassigned source with inspected fission-yeast primary
    evidence for each retained claim. Cite direct structural work for GRIP-domain/receptor
    detail, preserve species-specific receptor names and do not promote species experiments
    to an exact stock assertion.
  acceptance_checks:
  - Read the replacement claim-bearing primary passage and retain its organism, experimental
    preparation, endpoint and uncertainty.
  - Reconcile duplicated component, definition and graph wording; do not infer assembly
    necessity from viability or nucleation alone.
  - After separately authorized curation, use the guarded writer/history rules and
    rerun native focused schema, strict, identifier and evidence checks.
  generator: Maintained target YAML; no generated or scientific source edits made
    by this review.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0000930
  - GO:0008275
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    role: maintained scientific record
  description: Describe gamma-complex nucleation/templating as its contribution to
    organizing microtubules and building the spindle, with SPB duplication as context.
    Either represent the graph as a supported functional/structural summary or add
    a source-backed receptor recruitment, oligomerization and nucleation chain with
    appropriate species scope.
  acceptance_checks:
  - Read the replacement claim-bearing primary passage and retain its organism, experimental
    preparation, endpoint and uncertainty.
  - Reconcile duplicated component, definition and graph wording; do not infer assembly
    necessity from viability or nucleation alone.
  - After separately authorized curation, use the guarded writer/history rules and
    rerun native focused schema, strict, identifier and evidence checks.
  generator: Maintained target YAML; no generated or scientific source edits made
    by this review.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0000931
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    role: maintained scientific record
  description: Retain source-backed core/noncore membership and Mto1/Mto2 recruitment/activation.
    Remove or explicitly qualify exact geometry, asymmetric seam and allosteric claims
    until a direct structural/mechanistic source is attached, specifying species,
    native versus reconstituted preparation and open/closed state. Use Anders2006
    for its actual noncore membership/phenotype results and Lynch2014 for its actual
    bonsai activation results. Narrow the DISPENSABLE explanatory note to residual
    Mto2-mutant PAA production; assess complete-ring assembly separately.
  acceptance_checks:
  - Read the replacement claim-bearing primary passage and retain its organism, experimental
    preparation, endpoint and uncertainty.
  - Reconcile duplicated component, definition and graph wording; do not infer assembly
    necessity from viability or nucleation alone.
  - After separately authorized curation, use the guarded writer/history rules and
    rerun native focused schema, strict, identifier and evidence checks.
  generator: Maintained target YAML; no generated or scientific source edits made
    by this review.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0000931
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    role: maintained scientific record
  description: Either label the supported membership/output representation appropriately
    or add an explicitly sourced, taxon-scoped causal path from recruitment/oligomerization
    through template organization to nucleation. Preserve proposed conformational
    steps as hypotheses.
  acceptance_checks:
  - Read the replacement claim-bearing primary passage and retain its organism, experimental
    preparation, endpoint and uncertainty.
  - Reconcile duplicated component, definition and graph wording; do not infer assembly
    necessity from viability or nucleation alone.
  - After separately authorized curation, use the guarded writer/history rules and
    rerun native focused schema, strict, identifier and evidence checks.
  generator: Maintained target YAML; no generated or scientific source edits made
    by this review.
- action_id: septin-S2353-C1
  finding_ids:
  - septin-S2353-F1
  target_ids:
  - GO:0032156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  description: During authorized curation, assign IPR016491 to the generic septin-proteins
    row and explain that family membership does not establish a complete assembly-specific
    cohort.
  acceptance_checks:
  - Retain the correct five reviewed protein examples at whole-cytoskeleton scope.
  - Do not equate vegetative and sporulation-specific subunit inventories.
  - Do not replace the family with a broader GTPase domain.
  - Run focused schema, strict-reference and native protein checks.
- action_id: septin-S2353-C2
  finding_ids:
  - septin-S2353-F2
  target_ids:
  - GO:0032156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  description: During authorized curation, mark the current descriptive graph NONMECHANISTIC
    with a clear scope note, or represent a specific source-supported transition at
    an explicit organism and developmental scope.
  acceptance_checks:
  - Keep supported identity and parthood relationships.
  - Do not infer an assembly requirement merely from composition or localization.
  - Any added mechanistic edge must cite the source that actually establishes that
    transition.
  - Run focused schema, strict-reference and causal-graph validation.
- action_id: septin-S2353-C3
  finding_ids:
  - septin-S2353-F3
  target_ids:
  - GO:0032156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  description: During authorized curation, distinguish the native GO definition, source-specific
    fungal functions and green-algal ortholog evidence; qualify proposed recruitment
    roles or obtain directly matching evidence.
  acceptance_checks:
  - Do not promote gene occurrence to a demonstrated cortical network or its molecular
    functions.
  - Preserve budding-yeast versus filamentous-fungal versus sporulation scope and
    observed-versus-proposed distinctions.
  - Keep the correct broad cytoskeleton identity and valid vegetative protein examples.
  - Run focused schema, strict-reference and scientific evidence checks.
- action_id: septin-S2353-C4
  finding_ids:
  - septin-S2353-F4
  target_ids:
  - GO:0005819
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
  description: During authorized curation, separate the ontology definition from source-supported
    molecular elaboration and qualify organisms, stage and experimental inference.
  acceptance_checks:
  - Do not cite GO as the source of molecular detail absent from its definition.
  - Retain review-tier status for Jaspersen and primary morphological scope for Winey.
  - Use direct inspected evidence for any retained named crosslinker or motor mechanism.
  - Run focused schema and strict-reference checks.
- action_id: septin-S2353-C5
  finding_ids:
  - septin-S2353-F5
  target_ids:
  - GO:0005819
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
  description: During authorized curation, use the verified GO relation for this edge
    and retain Winey for its actual nuclear-spindle reconstruction.
  acceptance_checks:
  - Preserve the difference between source-specific spindle conventions.
  - Do not claim Winey reconstructed an astral array.
  - Run focused schema and strict-reference checks.
- action_id: septin-S2353-C6
  finding_ids:
  - septin-S2353-F6
  target_ids:
  - GO:0005819
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained scientific record
  description: During authorized curation, mark the current descriptive graph NONMECHANISTIC
    with a clear scope note, or represent a specific source-supported transition at
    an explicit organism and developmental scope.
  acceptance_checks:
  - Keep supported identity and parthood relationships.
  - Do not infer an assembly requirement merely from composition or localization.
  - Any added mechanistic edge must cite the source that actually establishes that
    transition.
  - Run focused schema, strict-reference and causal-graph validation.
- action_id: septin-S2353-C7
  finding_ids:
  - septin-S2353-F7
  target_ids:
  - GO:0051233
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  description: During authorized curation, qualify the midzone contribution using
    directly supported overlap/interpolar behavior, or route the broad kinetochore-coupling
    function through the whole-spindle node.
  acceptance_checks:
  - Keep GO0051233 as the regional identity.
  - Do not treat the generic spindle definition as proof of a region-specific molecular
    mechanism.
  - Preserve source uncertainty about putative kinetochore fibers in the EM analysis.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: septin-S2353-C8
  finding_ids:
  - septin-S2353-F8
  target_ids:
  - GO:0051233
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  description: During authorized curation, provide source-specific evidence for each
    retained mechanistic grouping or narrow the definition to the supported overlap
    structure and bounded yeast behavior.
  acceptance_checks:
  - Keep ontology and literature-derived statements distinguishable.
  - Do not use unidentified ultrastructural crossbridges as identification of Ase1
    or CPC.
  - Do not infer a uniform molecular cohort across the named taxa.
  - Run focused schema and strict-reference checks.
- action_id: septin-S2353-C9
  finding_ids:
  - septin-S2353-F9
  target_ids:
  - GO:0051233
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  description: During authorized curation, use a native synonym or provide a genuine
    source for the curated phrase.
  acceptance_checks:
  - Do not imply that GO supplied a string absent from its annotation.
  - Preserve exact-versus-curated synonym distinction.
  - Run focused schema and strict-reference checks.
- action_id: septin-S2353-C10
  finding_ids:
  - septin-S2353-F10
  target_ids:
  - GO:0051233
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  description: During authorized curation, mark the current descriptive graph NONMECHANISTIC
    with a clear scope note, or represent a specific source-supported transition at
    an explicit organism and developmental scope.
  acceptance_checks:
  - Keep supported identity and parthood relationships.
  - Do not infer an assembly requirement merely from composition or localization.
  - Any added mechanistic edge must cite the source that actually establishes that
    transition.
  - Run focused schema, strict-reference and causal-graph validation.
- action_id: septin-S2353-C11
  finding_ids:
  - septin-S2353-F11
  target_ids:
  - GO:0000922
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  description: During authorized curation, retain the generic regional definition
    and qualify named molecular/duplication mechanisms to directly supported organisms
    and spindle stages, or supply inspected sources covering the broader assertion.
  acceptance_checks:
  - Preserve the difference between a spindle pole, yeast SPB, centrosome and acentrosomal
    pole.
  - Retain GO0000930 for the generic gamma-complex class; do not replace it with a
    falsely universal ring-only identity.
  - Do not describe review synthesis as primary experimental proof.
  - Resolve component assembly necessity separately from nucleation activity.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: septin-S2353-C12
  finding_ids:
  - septin-S2353-F12
  target_ids:
  - GO:0000922
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  description: During authorized curation, correct the source for the added phrase
    rather than treating plausible wording as a native GO annotation.
  acceptance_checks:
  - Verify the exact source string and synonym scope.
  - Do not invent an ontology synonym when the response contains none.
  - Run focused schema and strict-reference checks.
- action_id: septin-S2353-C13
  finding_ids:
  - septin-S2353-F13
  target_ids:
  - GO:0000922
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained scientific record
  description: During authorized curation, mark the current descriptive graph NONMECHANISTIC
    with a clear scope note, or represent a specific source-supported transition at
    an explicit organism and developmental scope.
  acceptance_checks:
  - Keep supported identity and parthood relationships.
  - Do not infer an assembly requirement merely from composition or localization.
  - Any added mechanistic edge must cite the source that actually establishes that
    transition.
  - Run focused schema, strict-reference and causal-graph validation.
limitations:
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: Chikashige2006
  remains primary-abstract-only: fresh API200 is coredata-only; browser publisher
  retrieval403 and Citeseer timeout yielded no body. These are route-specific access
  limits, not global unavailability. Tanaka2005, Kaksonen2003, Boldogh2001 and Winter1997
  are metadata/abstract or native-annotation evidence only.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: All
  retained external source snapshots were freshly retrieved for this PR; actual per-source
  UTC fetch times and SHA256 are preserved. No cached response is restamped. Source
  locators distinguish primary direct experiments from introductory background and
  database annotation.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: No
  figure-pixel, raw movie, raw mass-spectrum or complete supplementary experimental-stock
  reanalysis was performed. Funaya and Galletta are freshly read only at named sections;
  Aghamohammadzadeh main paragraphs were read without supplemental Methods. No record
  image asset is present in these three targets.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: Only
  the explicit conventional-actin family candidate IPR004000 was evaluated; no exhaustive
  exact-family absence claim is made. Missing optional component inventories, properties
  or images do not generate findings.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: Core
  assembly necessity and the connector CONDITIONAL assembly interpretation remain
  unknown; phenotypic function/viability and bouquet attachment are distinct. Kms2
  context does not imply fixed stoichiometry or universal absence.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: Existing
  #2420 is historical scoped context. This three-record review does not terminally
  resolve the seven-target category finding, other category findings or any record-curation
  issue; no records were edited.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: The
  shared structured-source runner failure is historical and unavailable execution;
  the fresh source catalogue supports the present no-matching-fungal-dataset applicability
  determination. No downstream expression-module evidence is claimed.'
- 'Endocytic patch and two meiotic tether/LINC complexes independent subreview: Root
  owns full-corpus gates, final-head CI and publication decisions; the six current
  protein receipt checks here do not stand in for those gates.'
- 'Three gamma-tubulin complexes independent subreview: Three-target slice only. No
  global category resolution: the October23 and October25 F1 predecessors also affect
  targets outside this slice. Current gamma type repairs are positively assessed without
  retiring those whole findings.'
- 'Three gamma-tubulin complexes independent subreview: Jaspersen/Winey2004 is secondary
  context, freshly accessed through a browser cache-mediated author manuscript rendering
  with no HTTP-status receipt. Its source crawl age is separate from the actual current
  access time. No secondary review is treated as direct mechanistic experiment.'
- 'Three gamma-tubulin complexes independent subreview: Matsuyama2006 ORFeome survey
  and Zimmerman2004 are limited to native metadata/abstract and exact UniProt annotation
  provenance where applicable. Individual ORFeome localization images/tables and Zimmerman
  full text were not inspected. Fresh primary bodies for Alp6/Gfh1/Alp16 and Mod21
  were inspected separately.'
- 'Three gamma-tubulin complexes independent subreview: S3 routes for Samejima2005,
  Venkatram2005, Anders2006 and the three new primary articles returned404. Successful
  fresh PMC HTML responses then supplied body text. A failed route is not global source
  unavailability. An optional BeautifulSoup extraction attempt lacked that module;
  a standard-library HTML parser successfully extracted the returned bodies. This
  was not a failed repository validator.'
- 'Three gamma-tubulin complexes independent subreview: No microscopy pixels, movies,
  deposited structural coordinates or supplements were independently reanalyzed. Body
  methods/results and specified captions were inspected. There are no target-owned
  image assets to verify.'
- 'Three gamma-tubulin complexes independent subreview: Exact complete-ring assembly
  necessity and universal cross-eukaryote distribution remain bounded uncertainties.
  Membership, sequence identity, viability, localization and nucleation activity are
  not interchangeable.'
- 'Three gamma-tubulin complexes independent subreview: Historical runner unavailability
  is retained with its original00:49Z time, not represented as a new command. The
  fresh official catalogue has no target organism match; no gene/module query or summary
  was manufactured for unmatched organisms.'
- 'Three gamma-tubulin complexes independent subreview: Closed issue #2470 is tracker
  context only and itself incorrectly calls Viswanath2017 fission yeast. Current source
  assessment explicitly corrects that interpretation; the issue closure does not establish
  current scientific correctness.'
- 'Three gamma-tubulin complexes independent subreview: The native protein checks
  are current root-run receipts inspected here. Global QC, identifiers, CI and merge
  state remain parent-owned and are not independently rerun or certified by this slice.'
- 'Three gamma-tubulin complexes independent subreview: Common rubric/schema/verifier
  inputs are byte-identical to those personally read in the prior PR2352 review; current
  frozen hashes were rechecked and the active review/config/profile and graph checklist
  passages were reread. No extra maintained neighbor record was used.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Current reassessment
  is independent and read-only; original frozen bytes and historical source/check
  receipts remain immutable. All four assigned scientific targets are unchanged. No
  historical observation is relabeled as a current action.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Versele2005
  and Douglas2005 are secondary reviews, freshly read at specified Introduction/function,
  sporulation and Aspergillus passages. Their prior hypotheses, historical assembly
  models and taxon occurrence are not new primary experimental proof.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Finnigan2015
  fresh primary HTML was read at the stated abstract, strain-construction, recruitment
  Results/caption and Discussion passages, not the entire body, supplement, figure
  pixels or raw microscopy. Huh2003 and Mino1998 remain primary abstract plus native-annotation
  attribution checks.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Jaspersen/Winey2004
  is secondary author-manuscript browser text, freshly accessed with a reported three-week
  crawl age. Native request returned403; no native full-text or complete review read.
  The stated displayed Introduction, duplication/separation, nucleation and centrosome-comparison
  passages were inspected.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Viswanath2017
  is used at native primary Introduction/Figure1 context only; no complete Results/Methods
  audit or independent proof for every introductory citation. Broad eukaryote mechanisms
  remain outside that yeast-core evidence.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Winey1995
  genuine PDF was read at specified claim-bearing Methods/Results/caption and Discussion
  passages, not all main text, TableI, images or raw EM. Morphological kinetochore/interpolar
  assignments retain their inferential status; observed crossbridges have no demonstrated
  molecular identity in these passages. Regional overlap does not imply every entire
  spindle microtubule lies within the midzone.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Straight1997,
  Anders2001 and Cederquist2012 remain fresh exact primary abstract/metadata plus
  applicable UniProt attribution checks. No fresh publisher failure or full-body search
  is invented. The human-disease title of Cederquist does not negate its explicit
  yeast genetics.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Assembly necessity
  remains unknown for collective septins, combined alpha/beta tubulin and generic
  polar components. Neither defining material, native identity, intact structure,
  individual mutant phenotype nor cell viability establishes the required formation
  endpoint across every taxon. These unknowns are not fabricated extra issues.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Native protein
  commands verify the declared examples: septin cytoskeleton and spindle/midzone each
  have one COVERED graph node; spindle pole has an empty exact-protein inventory and
  zero GENE_OR_PROTEIN nodes. Empty scope is not successful proof of its named molecular
  mechanism.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Fresh catalogue
  covers only returned20organisms/28datasets; no matching eukaryote means downstream
  source non-applicability, not biological absence. Historical00:49Z runner receipt
  is retained without a new invocation.'
- 'Septin cytoskeleton and three spindle regions independent subreview: Root owns
  globalQC, issue deduplication/publication andCI. Generic-septin finding matches
  #2499 in class and can be added with its exact record/predecessor scope; no issue
  mutation was performed by this reviewer.'
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
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged
  normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy.
  Every inherited finding is reassessed against current sources and retains exact
  predecessor identity.
- 'Bundle issues #2574 (five stale reviews) and #2575 (ten structured-source applicability
  defects) are addressed here. Scientific record-curation findings remain separately
  tracked. Existing validator #2514 remains open.'
- 'Already-closed #2420, #2431 and #2470 are historical context for earlier record
  corrections. Their multi-target findings are not terminally superseded by a partial
  cohort; this review assesses only its current target-specific changes.'
- Source commit 05425cc7089baf8133399baaf1ec24c00c661de3 is retained by tag review-base/pr2353-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration,
  graph/protein policies, the verifier source and two prior category-review pairs.
- Seven original bundles omit structured-source applicability. Endocytic patch, meiotic
  nuclear membrane microtubule tethering complex and Sad1-Kms1 contain unsupported
  exemptions based on absence of expression/module claims.
- Fresh source inspection and retained responses use their actual access dates. Primary
  and secondary sources, abstracts, claim-bearing body sections, captions and any
  inspected pixels retain distinct scopes.
- The native spindle-pole protein verification has an empty inventory and its graph
  contains zero GENE_OR_PROTEIN nodes. Exit zero does not validate molecular mechanisms
  named only in prose.
- 'All24 current scientific finding keys are linked to #2499 and #2576–#2598. They
  preserve26 exact original occurrences; two shared gamma-complex findings each list
  both affected records and predecessors. These curation issues remain open.'
- 'Native validation rejected three policy evidence-kind values in an uncommitted
  draft. Issue #2599 tracks correction to authority with all references, scopes and
  substantive content preserved. The corrected draft is revalidated and independently
  re-reviewed.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094807Z-endocytic-patch-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094810Z-gamma-tubulin-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094812Z-gamma-tubulin-ring-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094813Z-gamma-tubulin-small-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094816Z-meiotic-nuclear-membrane-microtubule-tethering-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094818Z-sad1-kms1-linc-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094819Z-septin-cytoskeleton-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094822Z-spindle-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094824Z-spindle-midzone-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094825Z-spindle-pole-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2353
- https://github.com/CultureBotAI/CellStructureMech/issues/2420
- https://github.com/CultureBotAI/CellStructureMech/issues/2431
- https://github.com/CultureBotAI/CellStructureMech/issues/2470
- https://github.com/CultureBotAI/CellStructureMech/issues/2499
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2574
- https://github.com/CultureBotAI/CellStructureMech/issues/2575
- https://github.com/CultureBotAI/CellStructureMech/issues/2576
- https://github.com/CultureBotAI/CellStructureMech/issues/2577
- https://github.com/CultureBotAI/CellStructureMech/issues/2578
- https://github.com/CultureBotAI/CellStructureMech/issues/2579
- https://github.com/CultureBotAI/CellStructureMech/issues/2580
- https://github.com/CultureBotAI/CellStructureMech/issues/2581
- https://github.com/CultureBotAI/CellStructureMech/issues/2582
- https://github.com/CultureBotAI/CellStructureMech/issues/2583
- https://github.com/CultureBotAI/CellStructureMech/issues/2584
- https://github.com/CultureBotAI/CellStructureMech/issues/2585
- https://github.com/CultureBotAI/CellStructureMech/issues/2586
- https://github.com/CultureBotAI/CellStructureMech/issues/2587
- https://github.com/CultureBotAI/CellStructureMech/issues/2588
- https://github.com/CultureBotAI/CellStructureMech/issues/2589
- https://github.com/CultureBotAI/CellStructureMech/issues/2590
- https://github.com/CultureBotAI/CellStructureMech/issues/2591
- https://github.com/CultureBotAI/CellStructureMech/issues/2592
- https://github.com/CultureBotAI/CellStructureMech/issues/2593
- https://github.com/CultureBotAI/CellStructureMech/issues/2594
- https://github.com/CultureBotAI/CellStructureMech/issues/2595
- https://github.com/CultureBotAI/CellStructureMech/issues/2596
- https://github.com/CultureBotAI/CellStructureMech/issues/2597
- https://github.com/CultureBotAI/CellStructureMech/issues/2598
- https://github.com/CultureBotAI/CellStructureMech/issues/2599
```
