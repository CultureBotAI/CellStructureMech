# PR 2352: current-input review of ten records and adversarial follow-up

- Review: 20261103T055122Z-pr2352-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T05:39:52.336144Z
- Finished UTC: 2026-11-03T05:51:22Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2352. Three stale reviews are substantively refreshed: Arp2/3 heteromeric component types, and nda2 gene-symbol additions for aster and astral microtubule. These corrections predate this PR and remain scoped historical context, without terminally resolving unassessed targets of earlier category findings. All ten records retain curation findings: five major and nineteen minor, each with exact original lineage. The successor corrects structured-source coverage for eight original bundles. No scientific record is edited.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 5c6039e8394ca3a3b1456937d152c911fe0eb696. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 4c23da62a367483cdb5a8dd8b70db494726cbbbf.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 9a8a31291456921b6e1984a3a95f110c763c5174.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097729 | data/structures/appendage/9_2_motile_cilium.yaml | maintained | 9+2 motile cilium |
| GO:0097546 | data/structures/appendage/ciliary_base.yaml | maintained | ciliary base |
| GO:0032179 | data/structures/appendage/germ_tube.yaml | maintained | germ tube |
| GO:0097609 | data/structures/appendage/longitudinal_flagellum.yaml | maintained | longitudinal flagellum |
| GO:0031514 | data/structures/appendage/motile_cilium.yaml | maintained | motile cilium |
| GO:0097608 | data/structures/appendage/transverse_flagellum.yaml | maintained | transverse flagellum |
| GO:0005885 | data/structures/cytoskeleton/arp2_3_protein_complex.yaml | maintained | Arp2/3 protein complex |
| GO:0005818 | data/structures/cytoskeleton/aster.yaml | maintained | aster |
| GO:0000235 | data/structures/cytoskeleton/astral_microtubule.yaml | maintained | astral microtubule |
| GO:0120280 | data/structures/cytoskeleton/ciliary_pro_basal_body.yaml | maintained | ciliary pro-basal body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0097729 | passed | True | GO:0097729 | Documented focused command passed. |
| validate-strict GO:0097729 | passed | True | GO:0097729 | Documented focused command passed. |
| validate GO:0097546 | passed | True | GO:0097546 | Documented focused command passed. |
| validate-strict GO:0097546 | passed | True | GO:0097546 | Documented focused command passed. |
| validate GO:0032179 | passed | True | GO:0032179 | Documented focused command passed. |
| validate-strict GO:0032179 | passed | True | GO:0032179 | Documented focused command passed. |
| validate GO:0097609 | passed | True | GO:0097609 | Documented focused command passed. |
| validate-strict GO:0097609 | passed | True | GO:0097609 | Documented focused command passed. |
| validate GO:0031514 | passed | True | GO:0031514 | Documented focused command passed. |
| validate-strict GO:0031514 | passed | True | GO:0031514 | Documented focused command passed. |
| validate GO:0097608 | passed | True | GO:0097608 | Documented focused command passed. |
| validate-strict GO:0097608 | passed | True | GO:0097608 | Documented focused command passed. |
| validate GO:0005885 | passed | True | GO:0005885 | Documented focused command passed. |
| validate-strict GO:0005885 | passed | True | GO:0005885 | Documented focused command passed. |
| validate GO:0005818 | passed | True | GO:0005818 | Documented focused command passed. |
| validate-strict GO:0005818 | passed | True | GO:0005818 | Documented focused command passed. |
| validate GO:0000235 | passed | True | GO:0000235 | Documented focused command passed. |
| validate-strict GO:0000235 | passed | True | GO:0000235 | Documented focused command passed. |
| validate GO:0120280 | passed | True | GO:0120280 | Documented focused command passed. |
| validate-strict GO:0120280 | passed | True | GO:0120280 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | not_applicable | False | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | The complete official catalogue was inspected with actual access timestamps and bounded organism/dataset scope. It contains no matching eukaryotic dataset for the named fungal, algal and protist targets, so downstream matched gene/module queries are not applicable. This conclusion follows catalogue coverage rather than absence of expression claims. Sparse longitudinal and transverse flagellar records are excluded from the eight molecular-coverage defects. Catalogue absence is not biological absence; unrelated bacterial datasets are not substituted. Historical native-runner unavailability remains separately disclosed, with no fresh runner execution or success claimed. |
| Independent claim-level source review | passed | True | GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0097729, GO:0097546, GO:0032179, GO:0031514, GO:0005885, GO:0005818, GO:0000235, GO:0120280 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native nine-two UniProt verify check | passed | True | GO:0097729 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native nine-two UniProt causal check | passed | True | GO:0097729 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native motile-cilium UniProt verify check | passed | True | GO:0031514 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native motile-cilium UniProt causal check | passed | True | GO:0031514 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native ciliary-base UniProt verify check | passed | True | GO:0097546 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native ciliary-base UniProt causal check | passed | True | GO:0097546 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native germ-tube UniProt verify check | passed | True | GO:0032179 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native germ-tube UniProt causal check | passed | True | GO:0032179 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native arp2-3 UniProt verify check | passed | True | GO:0005885 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native arp2-3 UniProt causal check | passed | True | GO:0005885 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native aster UniProt verify check | passed | True | GO:0005818 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native aster UniProt causal check | passed | True | GO:0005818 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native astral UniProt verify check | passed | True | GO:0000235 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |
| Native astral UniProt causal check | passed | True | GO:0000235 | Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS limits remain in evidence. Deterministic coverage does not resolve scientific findings or assembly necessity. |

## Scientific And Domain Assessments

### Generic germ tube and source-scoped septin localization

identity: supported. Targets: GO:0032179.

Exact GO0032179 identity and appendage kind remain correct. Native GO and Candida primary/review context support cap/ring membership and leading-edge septins. The source literature legitimately uses germ tube for Candida outgrowth; no spore-versus-yeast terminology contradiction is manufactured.

### Apical cap versus basal band

provenance: concern. Targets: GO:0032179.

The unchanged definition still merges basal collar/cap and attributes the appended Cdc42/Spitzenkörper/polarisome dependence across three named fungi to the GO-only definition. Native cap and basal-band locations differ. Retain F2 and source/qualify additions without declaring the broader polarity biology false.

### Generic septin identity independent of complete cap cohort

grounding: concern. Targets: GO:0032179.

The component denotes generic septin proteins, not a complete mixed cap complex. Exact IPR016491 therefore supports that family identity independently of species-specific composition. The current rationale still makes a complete cap cohort a prerequisite for grounding; retain F3.

### Parthood-only graph is not an assembly mechanism

graph: concern. Targets: GO:0032179.

All three edges remain is part of; no assembly event or causal intermediate is represented. ASSEMBLY/MECHANISTIC still overstates this membership graph. Retain F1, with correction through separately authorized record curation.

### Generic-class assembly necessity remains unresolved

evidence: unknown. Targets: GO:0032179.

Local septin signal and individual cdc10/cdc11 deletion phenotypes do not establish necessity or dispensability of the whole generic septin class for germ-tube assembly. Other septins persist; viability and morphology are distinct from assembly. Keep the original explicit unknown.

### Generic protein class requires no invented gene examples

completeness: supported. Targets: GO:0032179.

Native verifier passes, while the causal diagnostic honestly reports one NO_GENE_SYMBOLS and zero COVERED. This generic component need not be populated with an invented named gene cohort; absence of optional examples is not a separate finding.

### Whole complex, cortical patch and seven concrete examples

identity: supported. Targets: GO:0005885.

Whole-complex identity and actin-cytoskeleton parthood remain distinct from the patch/polymer on which it acts. All seven reviewed yeast gene/accession/taxon examples resolve, and native membership annotations are source-qualified. Sagot fresh native Methods/Results supports only partial actin-body colocalization of the four cited proteins; it is not evidence that all seven occupy every body.

### Substantive refresh of three component-type changes

consistency: supported. Targets: GO:0005885.

Current Arp2/3 has PROTEIN_COMPLEX on all three deliberately grouped heteromeric components. Each group contains distinct named subunits rather than one family/paralogue class; fresh exact identities and the native type contract support the correction. History already cites closed2420/2431. This PR does not repair the record or terminally supersede the multi-target category findings; only its Arp2/3 slice was reassessed. The changes do not repair original F1/F2.

### Reversed Arc19/Arc18 defining homolog labels persist

grounding: concern. Targets: GO:0005885.

Fresh P33204 identifies ARC19/subunit4, while Q05933 identifies ARC18/subunit3. The definition still reverses their ARPC3/4 pairings, despite correct component labels/examples. Retain original major F1 with exact lineage.

### Young2004 does not support attributed subunit mechanisms

evidence: concern. Targets: GO:0005885.

Full freshly read Young2004 main text/captions/TableI analyzes isolated patches, branches and sac6/cap1 mutants. It does not characterize the Arc35/Arc19 clamp or define Arc40/Arc18/Arc15 activation coupling as claimed. Accessible Kaksonen abstract and Galletta regulator observations do not independently establish the specified short-pitch rearrangement. Retain original major F2; plausible biology is distinct from false source-specific attribution.

### Patch architecture and endocytic dynamics at inspected scope

evidence: supported. Targets: GO:0005885.

Young supports roughly70-degree branch geometry in partially purified patches, with preservation/flattening limits. Galletta supports regulator-specific assembly/movement effects and Kaksonen abstract supports a temporal endocytic pathway. Reference S288C accessions do not assert that every experimental stock is the reference strain. Broad amoeba/filamentous-fungus process combinations were not independently established.

### Group-specific assembly necessity remains unknown

evidence: unknown. Targets: GO:0005885.

The three ESSENTIAL assertions are not established by membership, localization, cell viability or catalytic activity. Winter1997 abstract describes a preparation lacking a40kDa member, but that is not removal of the entire three-protein peripheral group. No group-specific complete-removal/assembly test was checked.

### Current native example and causal-node coverage

evidence: supported. Targets: GO:0005885.

Root-executed verification and causal checks passed at source head and their receipts/log hashes were independently checked. All three nodes are COVERED for all seven declared symbols. Deterministic coverage does not resolve F1/F2 or assembly necessity.

### Actual structured-source applicability

evidence: supported. Targets: GO:0032179.

The fresh complete public catalogue contains no matching fungal dataset for Candida/Aspergillus/Neurospora germ-tube claims, including Cdc42 and septins. Downstream module searches are not applicable after this coverage check. Historical runner unavailability remains separate; no fresh runner success or biological absence is claimed.

### Actual structured-source applicability

evidence: supported. Targets: GO:0005885.

The fresh complete public catalogue contains no matching fungal dataset for the named Saccharomyces Arp2/3 genes and regulators. Downstream module searches are not applicable after this coverage check. Historical runner unavailability remains separate; no fresh runner success or biological absence is claimed.

### Frozen record and historical review integrity

schema: supported. Targets: GO:0097729.

Current and historical target bytes match the frozen original input; original YAML validates and its renderer reproduces Markdown exactly. Prior findings remain open with exact lineage; historical global-validator totals are not current results.

### Named-protein structured-source applicability

provenance: supported. Targets: GO:0097729.

Named proteins trigger the adapter policy. The earlier runner limitation is explicitly historical; the freshly inspected official catalogue contains no matching eukaryotic dataset, so gene/module search and summary are not applicable. This is not negative evidence about the structure.

### Frozen record and historical review integrity

schema: supported. Targets: GO:0097546.

Current and historical target bytes match the frozen original input; original YAML validates and its renderer reproduces Markdown exactly. Prior findings remain open with exact lineage; historical global-validator totals are not current results.

### Named-protein structured-source applicability

provenance: supported. Targets: GO:0097546.

Named proteins trigger the adapter policy. The earlier runner limitation is explicitly historical; the freshly inspected official catalogue contains no matching eukaryotic dataset, so gene/module search and summary are not applicable. This is not negative evidence about the structure.

### Frozen record and historical review integrity

schema: supported. Targets: GO:0031514.

Current and historical target bytes match the frozen original input; original YAML validates and its renderer reproduces Markdown exactly. Prior findings remain open with exact lineage; historical global-validator totals are not current results.

### Named-protein structured-source applicability

provenance: supported. Targets: GO:0031514.

Named proteins trigger the adapter policy. The earlier runner limitation is explicitly historical; the freshly inspected official catalogue contains no matching eukaryotic dataset, so gene/module search and summary are not applicable. This is not negative evidence about the structure.

### Frozen record and historical review integrity

schema: supported. Targets: GO:0120280.

Current and historical target bytes match the frozen original input; original YAML validates and its renderer reproduces Markdown exactly. Prior findings remain open with exact lineage; historical global-validator totals are not current results.

### Named-protein structured-source applicability

provenance: supported. Targets: GO:0120280.

Named proteins trigger the adapter policy. The earlier runner limitation is explicitly historical; the freshly inspected official catalogue contains no matching eukaryotic dataset, so gene/module search and summary are not applicable. This is not negative evidence about the structure.

### Exact class and coarse composition

identity: supported. Targets: GO:0097729.

Exact nine-doublets-plus-central-pair subtype, motile-cilium parent and scoped synonyms agree with GO. Axoneme, membrane, basal body, TZ and associated IFT identities are appropriate. Individual component essentiality is assessed separately.

### Five exact IFT examples and location attribution

grounding: supported. Targets: GO:0097729.

The four reviewed entries and one unreviewed IFT88 match native labels/tokens/taxon. Four reviewed exact-gene matches are unique within the bounded query; IFT88 reviewed search is empty. IFT172/IFT46 experimental annotation citations are location-specific; IFT81/IFT74/IFT88 are identity-only. No sixth IFT52 example or complete protein inventory is forced.

### Assembly necessity remains independently unverified

evidence: unknown. Targets: GO:0097729.

Canonical anatomy, proteomic presence and localization do not independently establish every ESSENTIAL broad-component assembly-necessity claim. No suitable depletion/reconstitution experiment for each entire regional component was checked; the enum is not redefined as activity or viability.

### Assembly, movement and model-system scope

evidence: supported. Targets: GO:0097729.

Chlamydomonas IFT transport and isolated-axoneme architecture support assembly/maintenance and dynein-based movement at their stated scope. Purified WT/mutant fractions are distinguished; broad cross-protist conservation wording is not treated as a fully audited three-species molecular comparison. Silflow body remains unverified.

### Accessory part is not a class-wide obligatory constituent

scope: concern. Targets: GO:0097729.

PFR is limited to some flagellated protists, while unqualified has_part and graph membership are broader. A native inverse part_of child display does not imply universal has_part.

### Static membership and whole-cilium self-assembly

graph: concern. Targets: GO:0097729.

The nine nodes and eight edges provide parthood, association and generic outputs. The whole assembled cilium mediates its own assembly; no actor-to-event causal pathway makes this a MECHANISTIC graph. IFT/motor primary evidence exists but is not encoded by those static edges.

### Exact class and coarse composition

identity: supported. Targets: GO:0031514.

Exact broad motile-cilium class allows variable axonemal arrangements; Chlamydomonas9+2 remains an example, not its universal definition. Axoneme, membrane, basal body, TZ and associated IFT identities are appropriate. Individual component essentiality is assessed separately.

### Five exact IFT examples and location attribution

grounding: supported. Targets: GO:0031514.

The four reviewed entries and one unreviewed IFT88 match native labels/tokens/taxon. Four reviewed exact-gene matches are unique within the bounded query; IFT88 reviewed search is empty. IFT172/IFT46 experimental annotation citations are location-specific; IFT81/IFT74/IFT88 are identity-only. No sixth IFT52 example or complete protein inventory is forced.

### Assembly necessity remains independently unverified

evidence: unknown. Targets: GO:0031514.

Canonical anatomy, proteomic presence and localization do not independently establish every ESSENTIAL broad-component assembly-necessity claim. No suitable depletion/reconstitution experiment for each entire regional component was checked; the enum is not redefined as activity or viability.

### Assembly, movement and model-system scope

evidence: supported. Targets: GO:0031514.

Chlamydomonas IFT transport and isolated-axoneme architecture support assembly/maintenance and dynein-based movement at their stated scope. Purified WT/mutant fractions are distinguished; broad cross-protist conservation wording is not treated as a fully audited three-species molecular comparison. Silflow body remains unverified.

### Accessory part is not a class-wide obligatory constituent

scope: concern. Targets: GO:0031514.

Mastigoneme is limited to some algae, while unqualified has_part and graph membership are broader. A native inverse part_of child display does not imply universal has_part.

### Static membership and whole-cilium self-assembly

graph: concern. Targets: GO:0031514.

The nine nodes and eight edges provide parthood, association and generic outputs. The whole assembled cilium mediates its own assembly; no actor-to-event causal pathway makes this a MECHANISTIC graph. IFT/motor primary evidence exists but is not encoded by those static edges.

### Base is broader than TZ

identity: supported. Targets: GO:0097546.

GO identity, SUBCELLULAR_REGION kind, parent, cilium parthood and four exact synonyms match. GO0097537 correctly identifies the assembled Y-link; generic TZ segment and heterogeneous network need not be forced into whole-axoneme or one-family identity.

### Exact unreviewed ORF examples with published symbol bridges

grounding: supported. Targets: GO:0097546.

Both entries retain correct unreviewed status, native labels and CHLRE ORFs. NCBI maps these to Cre loci; visually checked Fauser Fig4d maps them to CEP290 and NPHP4. The bounded reviewed-symbol search is empty. Automatic location/name annotations are not experimental localization.

### TZ link architecture and composition regulation

evidence: supported. Targets: GO:0097546.

Primary mutant/rescue/localization and composition comparisons support membrane tethering and protein-sorting roles at Chlamydomonas TZ. Wedge defects, Y-link loss, 9+2 architecture and ectosome endpoints are distinct. Independent localization is not proof of a complete interaction hierarchy.

### Known distal basal-body and transition-fiber regions

completeness: concern. Targets: GO:0097546.

The exact base encompasses three regions, but all current component rows and constituent graph nodes describe TZ. Diener isolated TZs exclude transition fibers and lost some in-situ structures; this cannot fill the known non-TZ region gap or certify a full-base proteome.

### Static base membership and gate output

graph: concern. Targets: GO:0097546.

Three regional membership edges, base-to-cilium parthood and base-to-gating output provide no mechanistic intermediate despite MECHANISTIC status. Source-backed tethering/sorting mechanisms could inform later curation but have not been encoded.

### Immature precursor and maturation

identity: supported. Targets: GO:0120280.

GO0120280, parent and scoped synonyms denote the immature partially assembled body; matures-into mature basal body is appropriate. Chlamydomonas interphase has mature and pro-basal pairs, with earliest singlet stages preceding completed triplets.

### Structural components and perturbation limits

grounding: supported. Targets: GO:0120280.

Whole triplet-blade and cartwheel structural classes are not generic single microtubules or individual SAS6/Bld10 proteins. UNKNOWN assembly essentiality is appropriate: uni3-1 proximal doublets do not equal complete triplet absence, and bld12 central-part loss does not equal deletion of every cartwheel element. No exact family or accession is invented for these assemblies.

### Direct cilium nucleation assigned to immature stage

evidence: concern. Targets: GO:0120280.

The definition says the pro-basal body cannot nucleate a cilium, but direct function/edge cites the mature-body definition and assigns anchoring/nucleation to the immature target. Its occurrence note describes only the mature flagellated pair. Route the direct output through maturity and state the immature pair explicitly.

### Cartwheel hub versus spoke tip

evidence: concern. Targets: GO:0120280.

Definition combines SAS6 and Bld10 in a hub, whereas its own component note distinguishes them. Matsuura localizes Bld10 to cartwheel fibers; Hiraki primary abstract identifies a spoke-tip component, and Nakazawa locates SAS6 centrally. Correct wording at the demonstrated Chlamydomonas scope.

### Actual fields and source tiers

completeness: supported. Targets: GO:0097729, GO:0097546, GO:0031514, GO:0120280.

All four current records and their original reviews were inspected. No target carries image assets, quantitative measurements or verbatim snippets; none are invented as mandatory fixes. Review literature, abstracts, body passages, source metadata and plotted labels retain separate access claims.

### Exact structure and hierarchy

identity: supported. Targets: GO:0097609.

GO identity, exact synonym and 9+2-cilium is_a relation match the native terms. This is a specialized eukaryotic cilium, distinct from the sulcus and transverse flagellum.

### Qualitative dinoflagellate distribution

scope: supported. Targets: GO:0097609.

VARIABLE Dinophyceae is an appropriately nonuniversal distribution. The new primary example is one free-living strain; it does not establish every symbiotic species or cell stage.

### Partial sulcus occupancy and planar motion

evidence: concern. Targets: GO:0097609.

The native definition and primary observations support emergence through the sulcus. Maruyama2023 directly reports planar beating in Akashiwo, while Cachon1991 describes nonplanar three-dimensional waves in the studied Ceratium/Oxyrrhis. The class-level planar statement needs qualification; these source/context differences must not be silently harmonized.

### Spatial relation versus assembly mechanism

graph: concern. Targets: GO:0097609.

The sole edge describes location and is backed by metadata-only Taylor evidence. It does not explain assembly or a causal mechanism. Its unqualified lies-within wording also loses the native often/partial scope.

### Wrong current GO definition-xref attribution

provenance: concern. Targets: GO:0097609.

The record says Taylor1980 is cited by GO0097612. Current native GO instead attaches that PMID to cingulum GO0097611; sulcus GO0097612 cites PMID20561119. The Taylor paper itself is correctly identified.

### Optional inventory and mechanism boundaries

completeness: supported. Targets: GO:0097609.

A short specialized-cilium record need not duplicate every axonemal protein or acquire optional images/properties. The retrieved primary paper supplies a concrete future example, but retraction mechanism and biological purpose remain unresolved rather than required invented graph edges.

### Exact structure, name and synonym

identity: supported. Targets: GO:0097608.

The GO identity denotes the intended dinoflagellate transverse motile cilium, and the exact synonym/category/kind are appropriate. The original GO wording is supported; extra causal detail requires its own attribution and scope.

### Is-a parent versus spatial containment

scope: supported. Targets: GO:0097608.

The direct9+2 motile-cilium parent is native is_a, not parthood. Cingulum is a cell-surface furrow and spatial host, not an is-a parent of the flagellum. Both graph node identities are nonlocal GO terms and resolve without relying on neighboring maintained records.

### Dinophyceae variable presence and source species

scope: supported. Targets: GO:0097608.

Taxon2864 and the conditional variable-presence treatment are supported. Direct primary specimens are A.sanguinea NIES-4631 and the specified Ceratium/Oxyrrhis material; they do not establish every dinoflagellate configuration, cell state or swimming behavior. The taxon note correctly assigns Taylor to GO0097611.

### Expanded definition exceeds its stated source

provenance: concern. Targets: GO:0097608.

The appended cingulum clause is unqualified after GO says often, and the striated-strand/waveform explanation is attached to a GO-only definition_source. Primary text supports scoped morphology and contraction, while retaining hypotheses about coiling, force transmission and regulation. This requires attribution/qualification, not a claim that the axoneme or strand is absent.

### Spatial relation mislabeled as assembly mechanism

graph: concern. Targets: GO:0097608.

The only edge states lies within. It has no assembly process or causal chain, despite ASSEMBLY/MECHANISTIC labels. Taylor evidence on this edge expressly says only metadata were available. Native GO and the Akashiwo observations support bounded spatial context; neither the cited metadata nor location alone establishes a mechanistic assembly graph.

### Broad thrust and rotation versus detailed allocation

scope: unknown. Targets: GO:0097608.

GO supports forward-thrust function, and primary studies support transverse motion and rotation in studied taxa. The1991 interpretation differs from the2004 numerical-model and2025 abstract-level thrust/steering assignments. Preserve taxon, mode and source tier; do not infer a universal force partition, direction of rotation, or striated-strand-driven beating cycle from this record.

### Observed contraction versus proposed molecular explanation

evidence: supported. Targets: GO:0097608.

Maruyama2024 distinguishes observed contractions/TEM morphology from proposed calcium switching and unobserved force-transmission/attachment structures. Its non-detergent Mg2+ result includes a membrane-permeability caveat. Cited Peridinium ATP-independent contraction and centrin attribution are prior-study context, not independent experiments performed in Akashiwo; no protein identity is inferred.

### Primary bodies, abstracts, native ontology and failures

provenance: supported. Targets: GO:0097608.

Current Maruyama2024 native HTML and freshly indexed Cachon1991 PDF were read at the stated claim-bearing passages. Taylor remains review metadata/abstract plus coredata. Leadbeater1967 sources are browser abstract/preview; Miyasaka2004 is a native Europe PMC abstract; Schuech2025 is an institutional primary abstract. No recovered native body is claimed for those access-limited sources. Fresh receipts retain actual access timestamps; original historical receipts are not restamped.

### Bounded follow-up without forced optional inventories

completeness: supported. Targets: GO:0097608.

The concrete tasks concern existing definition and graph assertions. Empty components/functions/examples/images/properties are not automatic findings. Further taxon-specific composition and molecular-mechanism work can be useful, but no unverified family/protein identifier or replacement structure is proposed. Historical metadata-access notes and PROPOSED status remain intact.

### Array versus constituent filament

identity: supported. Targets: GO:0005818.

The exact GO identity and maintained hierarchy distinguish the aster array from individual astral microtubules. Native GO supports the declared spindle context. HAA is an aster subclass and its meiotic study is a legitimate specialized example, not an exact synonym for all asters.

### Exact tubulin classes and concrete identities

grounding: supported. Targets: GO:0005818.

Alpha/beta tubulin are supported polymer constituents; IPR002452/002453 are exact family-level identities. P04689/tub1 with atb2/alp2 aliases, P04688/nda2 and P05219/nda3 are correct reviewed strain284812 proteins. Direct mCherry-Atb2 observation supports the alpha-tubulin example; the other entries explicitly provide identity rather than an isoform census.

### Meiotic source preparation is kept separate from reference stock

scope: supported. Targets: GO:0005818.

KT2901 is the homothallic fluorescent Figure4A strain; pat1 mat-Pc diploids provide separate synchronized ultrastructure. The canonical example correctly keeps these preparations distinct and does not identify them with the UniProt reference strain.

### Supported specialized meiotic function

evidence: supported. Targets: GO:0005818.

GO0030989/0032117 and the Tanaka2005 abstract support dynein-driven meiotic nuclear oscillation associated with the astral array. Funaya2012 supports Hrs1-dependent organization and the transition to meiosis I. This does not imply that every aster/astral microtubule performs horsetail movement or directly demonstrate chromosome-pairing/recombination effects.

### Broad capture machinery exceeds the cited taxon and cell-cycle evidence

scope: concern. Targets: GO:0005818.

The appended definition applies Kar9/Bim1 capture machinery and cortical dynein to a broad yeast/fungal/protist mitotic scope while naming only the GO term as definition source. The native definition does not contain this mechanism, and the maintained primary studies concern S.pombe meiotic Hrs1/rMTOC organization. Taxon-specific support or narrower wording is needed; no claim that these proteins are absent from every other taxon is made.

### Ontology parthood and meiotic phase must not be conflated

graph: concern. Targets: GO:0005818.

Constituent part-of and horsetail-function edges have appropriate support. Native GO supports aster part_of spindle, but the corresponding graph edge cites Funaya2012, whose wild-type HAA is disassembled/replaced before the meiosis-I spindle forms. The cited experiment does not establish the transient HAA as a simultaneous integral spindle compartment. The supported topology does not justify the MECHANISTIC scope label: no actor-to-event or organization-to-movement transition is represented. A nonmechanistic summary is an appropriate bounded alternative; atomistic detail is not required.

### No required missing molecular inventory

completeness: supported. Targets: GO:0005818.

The core alpha/beta polymer components and exact families are represented. UNKNOWN essentiality avoids inferring isoform assembly necessity from imaging or generic polymer composition. Additional organizer/motor proteins, images, dimensions and broader taxa require separate evidence and are optional; these are not treated as absent-required-field findings.

### Array versus constituent filament

identity: supported. Targets: GO:0000235.

The exact GO identity and maintained hierarchy distinguish the astral microtubule from its containing aster array. Native GO supports the declared spindle context. HAA is an aster subclass and its meiotic study is a legitimate specialized example, not an exact synonym for all asters.

### Exact tubulin classes and concrete identities

grounding: supported. Targets: GO:0000235.

Alpha/beta tubulin are supported polymer constituents; IPR002452/002453 are exact family-level identities. P04689/tub1 with atb2/alp2 aliases, P04688/nda2 and P05219/nda3 are correct reviewed strain284812 proteins. Direct mCherry-Atb2 observation supports the alpha-tubulin example; the other entries explicitly provide identity rather than an isoform census.

### Meiotic source preparation is kept separate from reference stock

scope: supported. Targets: GO:0000235.

KT2901 is the homothallic fluorescent Figure4A strain; pat1 mat-Pc diploids provide separate synchronized ultrastructure. The canonical example correctly keeps these preparations distinct and does not identify them with the UniProt reference strain.

### Supported specialized meiotic function

evidence: supported. Targets: GO:0000235.

GO0030989/0032117 and the Tanaka2005 abstract support dynein-driven meiotic nuclear oscillation associated with the astral array. Funaya2012 supports Hrs1-dependent organization and the transition to meiosis I. This does not imply that every aster/astral microtubule performs horsetail movement or directly demonstrate chromosome-pairing/recombination effects.

### Broad capture machinery exceeds the cited taxon and cell-cycle evidence

scope: concern. Targets: GO:0000235.

The appended definition applies Kar9/Bim1/EB1/Bik1 capture machinery and cortical dynein to a broad yeast/fungal/protist mitotic scope while naming only the GO term as definition source. The native definition does not contain this mechanism, and the maintained primary studies concern S.pombe meiotic Hrs1/rMTOC organization. Taxon-specific support or narrower wording is needed; no claim that these proteins are absent from every other taxon is made.

### Constituent contributions versus whole-array language

graph: concern. Targets: GO:0000235.

Tubulin-to-filament, filament-to-array and the specialized horsetail contribution are supported. The phrase provides the radial array is read as contribution by its constituent microtubules, not equivalence of one filament to the complete array. No distinct atomic motor-interface mechanism or universal meiotic function is inferred from the MECHANISTIC label. The supported topology does not justify the MECHANISTIC scope label: no actor-to-event or organization-to-movement transition is represented. A nonmechanistic summary is an appropriate bounded alternative; atomistic detail is not required.

### Claimed narrow synonym is not supplied by its cited GO term

provenance: concern. Targets: GO:0000235.

The record assigns cytoplasmic astral microtubule as a NARROW_SYNONYM with GO0000235 as source. The current exact native term has no synonyms. This is a concrete source-attribution gap, not evidence that the phrase is biologically invalid.

### No required missing molecular inventory

completeness: supported. Targets: GO:0000235.

The core alpha/beta polymer components and exact families are represented. UNKNOWN essentiality avoids inferring isoform assembly necessity from imaging or generic polymer composition. Additional organizer/motor proteins, images, dimensions and broader taxa require separate evidence and are optional; these are not treated as absent-required-field findings.

### Refresh changed nda2 input and preserve multi-target lineage

grounding: supported. Targets: GO:0005818.

The current alpha_tubulin.gene_symbols list adds nda2 and a history event to the originally frozen record. Direct reviewed UniProt P04688 identifies nda2 (alpha-1 tubulin); P04689 remains tub1/atb2/alp2, and P05219 nda3/alp12. Both native checks pass. This corrects the assigned target portion of prior category F2, not its unassessed GO0032117/GO1990295 targets. No claim that nda2 was directly visualized in the Atb2 experiment or is indispensable for assembly is added.

### Structured-source applicability for molecular claims

evidence: not_applicable. Targets: GO:0005818.

Named tubulins and capture machinery trigger applicability review. The fresh full official catalogue contains no matching fungus/protist dataset, so gene/module queries lack a valid dataset and are not performed. Historical runner unavailability is disclosed separately; no lack-of-expression-claim exemption is used.

### Refresh changed nda2 input and preserve multi-target lineage

grounding: supported. Targets: GO:0000235.

The current alpha_tubulin.gene_symbols list adds nda2 and a history event to the originally frozen record. Direct reviewed UniProt P04688 identifies nda2 (alpha-1 tubulin); P04689 remains tub1/atb2/alp2, and P05219 nda3/alp12. Both native checks pass. This corrects the assigned target portion of prior category F2, not its unassessed GO0032117/GO1990295 targets. No claim that nda2 was directly visualized in the Atb2 experiment or is indispensable for assembly is added.

### Structured-source applicability for molecular claims

evidence: not_applicable. Targets: GO:0000235.

Named tubulins and capture machinery trigger applicability review. The fresh full official catalogue contains no matching fungus/protist dataset, so gene/module queries lack a valid dataset and are not performed. Historical runner unavailability is disclosed separately; no lack-of-expression-claim exemption is used.

### Sparse flagellar morphology source applicability

evidence: not_applicable. Targets: GO:0097609, GO:0097608.

The two maintained flagellar records contain structure/location/waveform assertions without gene, locus, UniProt, regulator, pathway, trait or transcriptomic targets requiring molecular adapter queries. The transverse original explicitly records this scope; longitudinal original generic no-expression wording is not used as a molecular exemption. No omitted-adapter finding is invented for these sparse records. Optional literature discussion of ungrounded strand identity does not create a maintained gene/protein assertion.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0097729, GO:0097546, GO:0032179, GO:0097609, GO:0031514, GO:0097608, GO:0005885, GO:0005818, GO:0000235, GO:0120280.

3 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-germ-F1: The graph shows parthood rather than an assembly mechanism

minor / open / confirmed; issue key: germ-tube-static-assembly-graph.

The ASSEMBLY/MECHANISTIC graph contains exactly three is-part-of edges and no assembly event or causal intermediate. The cited GO definitions and Douglas review support membership/localization, but membership alone does not establish how the germ tube forms.

### plaque-germ-F2: Separate the apical cap from the basal band and source added claims

minor / open / confirmed; issue key: germ-tube-definition-cap-location-source.

The definition appends a basal septin collar/cap and a broad mechanistic dependence while definition_source remains GO0032179. Native GO and the cited review locate the cap at the leading edge; the basal band is a distinct localization. Retain the exact definition or attach properly scoped literature support to added polarity/vesicle/septin claims. This does not establish that Cdc42 or vesicle traffic has no germ-tube role.

### plaque-germ-F3: Ground the generic septin class independently of cap composition

minor / open / confirmed; issue key: germ-tube-generic-septin-family-gap.

The label-only rationale withholds a family CURIE until a complete germ-tube cap cohort is resolved, although the component label and role denote generic septin GTPases. Native InterPro IPR016491 exactly represents that protein family. Family grounding does not require claiming a complete cap membership list or a species-specific stoichiometry.

### plaque-arp-F1: Correct the reversed Arc19/ARPC4 and Arc18/ARPC3 pairs

major / open / confirmed; issue key: arp19-arp18-definition-pairings-reversed.

The definition pairs Arc19 with ARPC3 and Arc18 with ARPC4. Native P33204 identifies ARC19 as subunit4, while Q05933 identifies ARC18 as subunit3. The component labels and protein examples already use the correct pairs. Correct the definition without replacing those correct examples.

### plaque-arp-F2: Replace unsupported subunit-mechanism attributions to Young2004

major / open / confirmed; issue key: arp-subunit-mechanisms-misattributed-to-patch-em.

Both clamp and peripheral component evidence notes claim that Young2004 characterizes seven-subunit requirements or defines Arc40/Arc18/Arc15 activation coupling. The complete inspected paper instead analyzes isolated cortical actin patch networks and sac6/cap1 mutants. Correct these false evidence summaries and support any retained detailed subunit roles with an appropriate inspected primary structural/biochemical source. Apply the same correction to repeated graph descriptions/evidence; independently verify the short-pitch Arp2/Arp3 activation claim rather than treating the accessible Kaksonen abstract as its proof.

### micro-F1: Restrict the paraflagellar rod to the cilia that contain it

minor / open / confirmed; issue key: nine-two-cilium-paraflagellar-rod-scope.

The record adds GO0097740 as an unqualified has_part and describes it as a constituent of the broad 9+2 cilium class. Native GO explicitly limits this rod to some flagellated protists. A rod part_of 9+2-cilium assertion displayed under GO children does not imply that every 9+2 cilium has that rod. The graph repeats the broad membership and cites the access-limited Silflow review. This finding concerns the positive universalized representation; it does not deny rod membership in trypanosome or other supported subtypes.

### micro-F2: Do not label structural membership and outputs as a mechanism

minor / open / confirmed; issue key: nine-two-cilium-static-graph-mechanistic-scope.

The FUNCTION/MECHANISTIC graph contains only parthood, association and whole-structure output edges. Mechanistic phrases in node descriptions do not provide a causal path, and the whole cilium is the subject of its own assembly. Inspected primary work can support specific motor or transport steps but those steps are not represented in the current graph.

### micro-F3: Represent the graph as structural context or supply causal steps

minor / open / confirmed; issue key: ciliary-base-graph-static-mechanistic-scope.

The graph is a set of constituent/compartment parthood assertions plus a whole-base gating output. It does not explain how a named constituent, interaction or perturbation controls that output. Source-backed molecular mechanisms exist in the primary papers, but the current edge representation does not encode them.

### micro-F4: Represent the defining basal-body and transition-fiber regions

minor / open / confirmed; issue key: ciliary-base-known-non-tz-composition-gap.

The entire component inventory and constituent graph cover only transition-zone structures, despite the exact base definition explicitly comprising distal basal body, transition fibers and TZ. The cited Diener preparation expressly excludes transition fibers from isolated TZs, and the gate review separates those structures. This materially narrows the represented composition of the broad base. It does not require an exhaustive protein inventory or replace the base identity with TZ.

### micro-F5: Qualify mastigoneme parthood within the broad motile-cilium class

minor / open / confirmed; issue key: motile-cilium-mastigoneme-scope.

The unqualified has_part and corresponding graph element make mastigoneme appear as a constituent of the entire motile-cilium class, while the native term explicitly describes some algal flagella. Preserve the supported conditional algal relation and avoid treating an inverse GO part_of lookup as obligatory universal composition.

### micro-F6: The graph labels anatomical summary and product-to-assembly edges as mechanism

minor / open / confirmed; issue key: motile-cilium-graph-self-assembly-and-scope.

Most edges are parthood/association or generic function. The motile_cilium mediates cilium_assembly edge uses a source about IFT delivering precursors and does not establish the assembled cilium as its own assembly driver. Narrow to a NONMECHANISTIC summary or represent source-backed machinery-to-assembly directions.

### micro-F7: Assign cilium anchoring and axoneme nucleation to the mature basal body

major / open / confirmed; issue key: probasal-body-mature-cilium-nucleation-conflation.

The function and the graph edge whose subject is ciliary_pro_basal_body state that this structure anchors a cilium and forms the base of axonemal assembly, using the mature GO0036064 definition as evidence. GO0120280 explicitly says pro-basal bodies cannot nucleate a cilium. Retain the supported maturation relation and attribute the direct function to the mature node, or expressly describe an indirect developmental contribution. The distribution note also describes only the mature flagellum-bearing pair and should identify the accompanying pro-basal pair.

### micro-F8: Separate the SAS6 hub from Bld10 spoke-tip location

minor / open / confirmed; issue key: probasal-bld10-cartwheel-hub-location.

The definition compresses the cartwheel into a SAS6/Bld10p hub. The inspected review sections place Bld10 at the spoke tips/pinheads, and Matsuura2004 localizes it on cartwheel fibers; the existing component notes already correctly distinguish hub from spoke tip. Describe the whole cartwheel without locating both proteins at its hub.

### septin-S2352-F1: The spatial graph is labeled as an assembly mechanism

minor / open / confirmed; issue key: longitudinal-flagellum-spatial-graph-mechanistic-scope.

The graph contains only longitudinal_flagellum lies-within dinoflagellate_sulcus, yet declares ASSEMBLY and MECHANISTIC. Its Taylor evidence explicitly describes metadata access. Retain a qualified spatial relation as nonmechanistic context, or supply a separately evidenced assembly path. Preserve often/partial occupancy rather than implying the entire flagellum remains inside the sulcus.

### septin-S2352-F2: Taylor1980 is attributed to the wrong current GO term

minor / open / confirmed; issue key: longitudinal-flagellum-sulcus-citation-attribution.

The top-level PMID/DOI notes identify Taylor1980 as the review cited by GO0097612. Native GO currently assigns Taylor to GO0097611, while GO0097612 cites Iwataki2010 PMID20561119. Correct the source-to-term attribution without pretending that either full historical paper was read.

### septin-S2352-F3: Scope the planar-wave statement to the observed taxa and conditions

minor / open / confirmed; issue key: longitudinal-flagellum-planar-wave-scope.

The expanded definition describes longitudinal beating with planar waves without a taxon or observation qualifier. Maruyama2023 supports planar Akashiwo motion, whereas Cachon1991 describes three-dimensional nonplanar waves for its studied Ceratium/Oxyrrhis context. Retain the supported specialized-cilium identity while scoping waveform statements and recording the differing observations rather than implying one class-wide pattern.

### septin-S2352-F4: Spatial containment is presented as an assembly mechanism

minor / open / confirmed; issue key: transverse-flagellum-spatial-edge-labeled-mechanistic-assembly.

The graph has one lies-within relation between transverse flagellum and cingulum. It explains neither construction nor a causal mechanism, but is classified ASSEMBLY and MECHANISTIC. Its only edge evidence is Taylor1980 metadata, which the record itself explicitly limits to bibliographic/access information. Preserve supported spatial context with an honest nonmechanistic scope and directly supporting evidence, or replace/remove this graph during authorized curation. Do not infer mechanism from the source title or metadata.

### septin-S2352-F5: Appended waveform explanation needs its own source and scope

minor / open / confirmed; issue key: transverse-flagellum-definition-addition-source-scope.

The definition appends an unqualified cingulum placement and striated-strand-to-helical-wave explanation after the narrower GO text, while definition_source remains GO0097608. That native definition says often and does not contain the appended mechanism. The inspected primary studies support constituent morphology and condition-specific contraction but distinguish direct observations from proposed coiling/regulatory explanations. Retain the exact GO definition or explicitly source and qualify the additions, including relevant organism/configuration limits. This does not establish that the transverse strand or general thrust function is biologically false.

### septin-S2352-F6: Bound the appended mitotic capture mechanism to supported taxa

major / open / confirmed; issue key: aster-cross-taxon-capture-mechanism-unsourced.

The definition extends the native GO identity with Kar9/Bim1 and cortical-dynein mitotic positioning across broad yeast/fungal/microbial-eukaryote groups. GO does not state this mechanism, and the record primary sources inspect S.pombe meiotic Hrs1-dependent arrays and their replacement by a spindle. Add appropriate inspected taxon-specific evidence and qualify the mechanism, or remove the unsupported extension. The supported meiotic example and native ontology hierarchy should remain.

### septin-S2352-F7: Use ontology evidence for spindle parthood without treating HAA as a simultaneous spindle compartment

minor / open / confirmed; issue key: aster-spindle-parthood-primary-source-scope.

The aster-to-spindle graph edge describes an integral compartment and cites Funaya2012. That experiment instead shows the meiotic radial array disappearing as the meiosis-I spindle forms. The generic relation is supported by native GO, so this is a citation/context correction: use the ontology for generic parthood and preserve the primary study temporal distinction.

### septin-S2352-F8: Distinguish a structural/function summary from a represented mechanism

minor / open / confirmed; issue key: aster-static-graph-mechanistic-scope.

The graph consists of constituent and compartment parthood plus a whole-structure function output. These supported relations do not themselves represent how array organization or a motor event causes movement, yet the graph is labeled MECHANISTIC. Use NONMECHANISTIC for the existing summary or add a directly evidenced causal transition. This does not invalidate the underlying topology or demand an atomic motor model.

### septin-S2352-F9: Bound the appended mitotic capture mechanism to supported taxa

major / open / confirmed; issue key: astral-microtubule-cross-taxon-capture-mechanism-unsourced.

The definition extends the native GO identity with Kar9/Bim1/EB1/Bik1 and cortical-dynein mitotic positioning across broad yeast/fungal/microbial-eukaryote groups. GO does not state this mechanism, and the record primary sources inspect S.pombe meiotic Hrs1-dependent arrays and their replacement by a spindle. Add appropriate inspected taxon-specific evidence and qualify the mechanism, or remove the unsupported extension. The supported meiotic example and native ontology hierarchy should remain.

### septin-S2352-F10: Correct the source attribution for the added narrow synonym

minor / open / confirmed; issue key: astral-microtubule-synonym-not-in-cited-go.

The synonym cytoplasmic astral microtubule is attributed to GO0000235, but the native exact term currently has no synonym entries. Retain the phrase only with an appropriate source/curator rationale, or remove this unsupported GO attribution. This is not a claim that the descriptive phrase is biologically wrong.

### septin-S2352-F11: Distinguish a structural/function summary from a represented mechanism

minor / open / confirmed; issue key: astral-microtubule-static-graph-mechanistic-scope.

The graph consists of constituent and compartment parthood plus a whole-structure function output. These supported relations do not themselves represent how array organization or a motor event causes movement, yet the graph is labeled MECHANISTIC. Use NONMECHANISTIC for the existing summary or add a directly evidenced causal transition. This does not invalidate the underlying topology or demand an atomic motor model.

## Recommended Actions And Acceptance Checks

### plaque-germ-A1

Recast the existing graph as NONMECHANISTIC structural context, remove it, or replace it with an organism- and condition-bounded assembly mechanism supported by primary experiments.

- Do not equate is-part-of with required-for-assembly.
- Each mechanistic edge must identify a source-supported action and direction.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### plaque-germ-A2

Correct the spatial distinction between apical cap, diffuse basal band and internal septation ring; remove or source the additional causal clauses with their organism and experimental context.

- Check every retained added clause against the actual cited passage rather than a title.
- Do not infer absence of the entire septin class from single-member deletion phenotypes.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### plaque-germ-A3

Use exact generic septin family grounding for the existing protein class and preserve any unresolved cap composition or organism-specific membership as a separate limitation.

- Verify IPR016491 remains a family named Septin.
- Do not substitute a single septin paralog or a domain for the generic protein-family class.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### plaque-arp-A1

During authorized curation, replace the two reversed definition pairings with Arc19/ARPC4 and Arc18/ARPC3.

- Keep P33204 and Q05933 attached to their current correct genes/components.
- Check the resulting definition against the native reviewed identity snapshots.
- Run focused schema and strict-reference validation.

### plaque-arp-A2

During authorized curation, repair source-specific evidence notes and source or qualify each detailed molecular role consistently in components and graph.

- Retain Young2004 for branched patch morphology at its actual experimental scope.
- Use an inspected structural/biochemical source for subunit contacts and activation rearrangements, or remove/qualify unsupported specificity.
- Keep exact protein identities separate from localization, function and assembly necessity.
- Do not treat ESSENTIAL as a synonym for membership or catalytic contribution.
- Run focused schema, strict-reference and causal-graph checks.

### micro-A1

Remove the unqualified class-wide has_part or represent a taxon-qualified subtype/example; qualify or remove the corresponding graph node/edge and attach direct rod-specific evidence.

- Preserve native GO relation direction and its some-protists qualifier.
- Check the source organism and represented cilium type before asserting rod membership.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### micro-A2

Retain this as NONMECHANISTIC structural/function context with corrected scope, remove it, or replace it with a bounded primary-supported mechanism that separates assembly machinery, cargo, motor action and outcome.

- Read each directed edge against a claim-bearing passage.
- Do not use whole-cilium self-assembly or a membership edge as evidence of a mechanism.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### micro-A3

Mark the present graph NONMECHANISTIC, remove it, or build a bounded mechanism with actual constituent-to-event-to-outcome edges supported by primary experiments.

- Separate localization/parthood from effects on tethering and protein composition.
- Preserve organism, mutant, rescue and preparation boundaries on causal edges.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### micro-A4

Add source-backed structural representation of the distal basal-body and transition-fiber regions, or explicitly delimit the present component view as partial and identify the known missing regions for follow-up. Label-only rows can be used where exact scoped identifiers are unresolved.

- Preserve the complete GO0097546 boundary while keeping TZ-only experimental preparations scoped.
- Do not ground a distal segment to the complete basal body without a segment qualification or infer that isolated TZ proteomics samples transition fibers.
- After separately authorized curation, use the guarded writer and native history/status rules; run focused schema/strict, identifier and evidence checks.

### micro-A5

Represent mastigoneme as a taxon-qualified optional part, or retain the one-way parthood on its own record without an unqualified broad-class inverse.

- Preserve Chlamydomonas/algal support without generalizing to every motile cilium.
- Read exact source support and term direction; do not infer inverse class restrictions from a child listing.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

### micro-A6

Correct the assembly-edge direction/actor and graph scope to match the supported level of explanation.

- Distinguish assembled product, constituent regions, transport machinery and assembly process.
- Retain valid structural edges without claiming that parthood itself establishes causality.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

### micro-A7

During authorized curation, route direct cilium anchoring/axoneme nucleation through the mature_ciliary_basal_body node and make immature occurrence/function wording stage-specific.

- Keep GO0120280 as the target identity and preserve its inability to nucleate before maturation.
- Retain the supported matures-into edge and distinguish developmental contribution from direct nucleation.
- Use review-supported Chlamydomonas pro-basal-pair wording in the occurrence note.
- Run focused schema, strict-reference and causal-graph checks.

### micro-A8

During authorized curation, describe a SAS6-centered cartwheel with Bld10-associated spoke tips, at the source-supported Chlamydomonas scope.

- Do not turn cartwheel localization into specific central-hub localization.
- Keep the existing correct hub/spoke-tip distinction in component grounding notes.
- Avoid extrapolating the exact molecular arrangement to every named ciliate/flagellate without matching evidence.
- Run focused schema and strict-reference validation.

### septin-S2352-C1

Narrow graph kind, scope, descriptions and edge evidence to the actual spatial claim; attach the inspected ontology or appropriate primary passage.

- Do not treat bibliography metadata as evidence of an experimental mechanism.
- Preserve partial, species- and state-dependent sulcus occupancy.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

### septin-S2352-C2

Correct the GO-xref mapping and cite each source only for claims actually inspected.

- Verify current native term xrefs and exact PMID/DOI identities.
- Retain the historical access limitation; do not substitute citation identity for article support.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

### septin-S2352-C3

Qualify the added waveform and propulsion wording with inspected source/taxon/state context, or retain only the broader verified ontology definition.

- Keep planar Akashiwo and nonplanar Ceratium/Oxyrrhis observations distinct.
- Do not infer universal symbiotic-species behavior or an exact thrust partition from these studies.
- Apply only in separately authorized curation through the guarded writer and required history, rendering and validation gates.

### septin-S2352-C4

During authorized curation, recast the current graph as nonmechanistic functional/spatial context with qualifying scope and direct location evidence, remove it, or replace it with an independently supported assembly/mechanistic graph. Do not retain ASSEMBLY solely because a flagellum lies in a groove.

- Read every resulting edge against its actual source passage; metadata-only Taylor cannot establish a mechanism.
- Check graph_kind and scope_status against what the graph actually explains; keep cingulum occupancy conditional where required.
- Run focused schema/strict plus native CURIE/history checks after an authorized validated-writer change.

### septin-S2352-C5

Separate the exact GO definition from any literature-derived elaboration. Retain often/typical-configuration qualifiers, cite the actual primary passages for morphology or contraction, and identify proposed waveform/regulatory mechanisms as proposals.

- Compare the retained definition to native GO0097608, including its often qualifier.
- For each added clause, inspect the primary organism, methods, result and stated uncertainty; do not promote prior cited studies or abstract-only models to direct universal mechanism.
- Preserve PROPOSED status and historical access notes; use the native validated writer, curation event, repository history and focused validators only when curation is separately authorized.

### septin-S2352-C6

During authorized curation, separate general structural identity from taxon- and phase-specific spindle-positioning mechanisms.

- Retain the native GO definition and correct hierarchy.
- Use inspected primary evidence for each retained named capture mechanism and state its organism/cell-cycle scope.
- Preserve the valid S.pombe meiotic HAA example and its distinct Hrs1/rMTOC source context.
- Do not infer universal Kar9/Bim1 machinery from a specialized HAA experiment.
- Run focused schema, strict-reference and causal-graph checks.

### septin-S2352-C7

During authorized curation, attach the appropriate GO support to generic spindle parthood and qualify the HAA-specific temporal context.

- Do not delete a correct native relation merely because the specialized example differs in timing.
- Do not describe the wild-type meiotic HAA as simultaneous with the meiosis-I spindle on Funaya2012 evidence.
- Validate graph and source references.

### septin-S2352-C8

Narrow the graph scope to a nonmechanistic structural/function summary, or encode a source-supported causal transition with organism and meiotic context.

- Preserve correct ontology nodes and supported membership relations.
- Check each retained causal edge against an inspected primary passage; a proposed future mechanism is not a completed graph.
- Any scientific edit requires separate curation authorization and the guarded writer, append-only history, rendering and native validation.

### septin-S2352-C9

During authorized curation, separate general structural identity from taxon- and phase-specific spindle-positioning mechanisms.

- Retain the native GO definition and correct hierarchy.
- Use inspected primary evidence for each retained named capture mechanism and state its organism/cell-cycle scope.
- Preserve the valid S.pombe meiotic HAA example and its distinct Hrs1/rMTOC source context.
- Do not infer universal Kar9/Bim1 machinery from a specialized HAA experiment.
- Run focused schema, strict-reference and causal-graph checks.

### septin-S2352-C10

During authorized curation, repair or remove the unsupported GO synonym attribution.

- Check the exact native term rather than inferring a synonym from a related class.
- If retaining a curated narrow synonym, provide a source that actually supports it.
- Run focused schema and strict-reference validation.

### septin-S2352-C11

Narrow the graph scope to a nonmechanistic structural/function summary, or encode a source-supported causal transition with organism and meiotic context.

- Preserve correct ontology nodes and supported membership relations.
- Check each retained causal edge against an inspected primary passage; a proposed future mechanism is not a completed graph.
- Any scientific edit requires separate curation authorization and the guarded writer, append-only history, rendering and native validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/appendage/9_2_motile_cilium.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97; current SHA256 c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97. Record bytes unchanged since the original review. |
| original-review-0 | reviews/structured/20261021T094726Z-9-2-motile-cilium-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/appendage/ciliary_base.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb; current SHA256 fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T094729Z-ciliary-base-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/appendage/germ_tube.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058; current SHA256 b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T094732Z-germ-tube-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/appendage/longitudinal_flagellum.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac; current SHA256 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac. Record bytes unchanged since the original review. |
| original-review-3 | reviews/structured/20261021T094735Z-longitudinal-flagellum-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/appendage/motile_cilium.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e; current SHA256 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e. Record bytes unchanged since the original review. |
| original-review-4 | reviews/structured/20261021T094737Z-motile-cilium-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/appendage/transverse_flagellum.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c; current SHA256 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c. Record bytes unchanged since the original review. |
| original-review-5 | reviews/structured/20261021T094739Z-transverse-flagellum-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/cytoskeleton/arp2_3_protein_complex.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 a612b062735844ba209722df0054d084db27ef18e8a243dc32d6d180303fd44b; current SHA256 05b7cc75eaf5f65fb7a4839055dcd086303a6c26cf1fb781ad41baf541bd8ecc. Changed record reassessed against current sources. |
| original-review-6 | reviews/structured/20261021T094741Z-arp2-3-protein-complex-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/cytoskeleton/aster.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 ed329cc165c49478a9cad71b9a56809631bed2891dd09a46d8a4cce1523f3ae7; current SHA256 ead65813443a3277dee3611ec40e32b7bc4c3882d8c31508eb352f6fffdfd6df. Changed record reassessed against current sources. |
| original-review-7 | reviews/structured/20261021T094744Z-aster-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/cytoskeleton/astral_microtubule.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 7c5c19cbf7cc39406dcc7d8bf376e4fcff12dcf7c71f702cf8058e766138be1f; current SHA256 45c1ec56a960d58bde433d88317824b726ff48473bc9b0b1d4429c6e2f57041d. Changed record reassessed against current sources. |
| original-review-8 | reviews/structured/20261021T094746Z-astral-microtubule-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/cytoskeleton/ciliary_pro_basal_body.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4; current SHA256 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4. Record bytes unchanged since the original review. |
| original-review-9 | reviews/structured/20261021T094748Z-ciliary-pro-basal-body-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-germ-tube-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032159,GO:0032171,GO:0032172,GO:0032179,GO:0110165; All requested term identities, active status, definitions and relationship metadata | supports | Current nonobsolete native terms [('GO:0110165', 'cellular anatomical structure'), ('GO:0032171', 'germ tube septin cap'), ('GO:0032172', 'germ tube septin ring'), ('GO:0032159', 'septin cap'), ('GO:0032179', 'germ tube')]. Exact structure identity and narrower location/function terms were checked. |
| plaque-germ-tube-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/EC.4.9.1503-1512.2005%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Publication title, authors, DOI/PMID, publication type and available abstract | supports | Fresh metadata identifies Septin function in yeast model systems and pathogenic fungi.; Douglas2005 is secondary review evidence, not an independent three-species mechanistic experiment. |
| plaque-germ-tube-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; Fresh native PMC HTML; Septins in C.albicans subsection, including three localization patterns | supports | The secondary review separates a cytokinetic ring within the tube, a diffuse basal band and a faint cap at the growing tip. This supports anatomical distinction and source-scoped localization, not a universal fungal germination dependence. |
| plaque-germ-tube-agent-warenda2002 | https://pmc.ncbi.nlm.nih.gov/articles/PMC117938/?pdf=render; Fresh native PMC HTML returned by pdf=render URL; Abstract; Methods strains/media and microscopy; claim-bearing localization paragraphs and hyphal-mutant Results; Figures2/7/8 captions; hyphal Discussion | supports | Candida BWP17-derived strains show diffuse germ-tube septins, tip signal and later septal rings. Individual cdc10/cdc11 deletions retain other septins and alter morphogenesis without abolishing all serum-induced growth. They are not complete generic-class ablations. |
| plaque-germ-tube-agent-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; IPR016491 metadata.type/name and non-LLM description | supports | IPR016491 is the generic Septin protein family. This exact class identity does not specify every member or stoichiometry of a germ-tube cap. |
| plaque-arp-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0005885,GO:0015629,GO:0030479,GO:0030864,GO:0032991,GO:0061645; All requested term identities, active status, definitions and relationship metadata | supports | Current nonobsolete native terms [('GO:0030479', 'actin cortical patch'), ('GO:0005885', 'Arp2/3 protein complex'), ('GO:0030864', 'cortical actin cytoskeleton'), ('GO:0015629', 'actin cytoskeleton'), ('GO:0032991', 'protein-containing complex'), ('GO:0000147', 'actin cortical patch assembly'), ('GO:0061645', 'endocytic patch')]. Exact structure identity and narrower location/function terms were checked. |
| plaque-arp-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName and lineage | supports | Native taxonomy distinguishes species4932 from S288C reference-strain559292. Reference sequence identifiers are not exact-stock microscopy assertions. |
| plaque-arp-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; taxId, scientificName and lineage | supports | Native taxonomy distinguishes species4932 from S288C reference-strain559292. Reference sequence identifiers are not exact-stock microscopy assertions. |
| plaque-arp-agent-P32381 | https://rest.uniprot.org/uniprotkb/P32381.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed P32381: ARP2, Actin-related protein 2, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARP2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARP2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('P32381', 'ARP2', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-P47117 | https://rest.uniprot.org/uniprotkb/P47117.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed P47117: ARP3, Actin-related protein 3, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARP3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('P47117', 'ARP3', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-P53731 | https://rest.uniprot.org/uniprotkb/P53731.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed P53731: ARC35, Actin-related protein 2/3 complex subunit 2, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARC35 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC35%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('P53731', 'ARC35', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-P33204 | https://rest.uniprot.org/uniprotkb/P33204.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed P33204: ARC19, Actin-related protein 2/3 complex subunit 4, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARC19 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC19%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('P33204', 'ARC19', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-P38328 | https://rest.uniprot.org/uniprotkb/P38328.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed P38328: ARC40, Actin-related protein 2/3 complex subunit 1, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARC40 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC40%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('P38328', 'ARC40', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-Q05933 | https://rest.uniprot.org/uniprotkb/Q05933.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed Q05933: ARC18, Actin-related protein 2/3 complex subunit 3, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARC18 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC18%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('Q05933', 'ARC18', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-P40518 | https://rest.uniprot.org/uniprotkb/P40518.json; Reviewed primary accession, organism, genes, recommended protein name, SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references | supports | Native reviewed P40518: ARC15, Actin-related protein 2/3 complex subunit 5, taxon559292. Function comments often use similarity evidence; those do not replace direct cited-paper support. Reference membership text uses historical ARC16/p16 naming; this entry’s exact gene is preserved. |
| plaque-arp-agent-query-ARC15 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC15%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned exact gene/reviewed/taxon results | supports | Native exact query resolves [('P40518', 'ARC15', 559292)]. This verifies accession mapping, not experimental localization or mechanism. |
| plaque-arp-agent-kaksonen2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:14622601%20AND%20SRC:MED; Exact Europe PMC bibliographic fields and abstract | supports | Fresh metadata/abstract identifies A pathway for association of receptors, adaptors, and actin during endocytic internalization.. Full-body inspection is only claimed for separately identified article-body evidence. |
| plaque-arp-agent-doi-jcb.200404159 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200404159; Exact Europe PMC bibliographic fields and abstract | supports | Fresh metadata/abstract identifies Yeast actin patches are networks of branched actin filaments.. Full-body inspection is only claimed for separately identified article-body evidence. |
| plaque-arp-agent-doi-journal.pbio.0060001 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pbio.0060001; Exact Europe PMC bibliographic fields and abstract | supports | Fresh metadata/abstract identifies Distinct roles for Arp2/3 regulators in actin assembly and endocytosis.. Full-body inspection is only claimed for separately identified article-body evidence. |
| plaque-arp-agent-doi-mbc.E06-04-0282 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E06-04-0282; Exact Europe PMC bibliographic fields and abstract | supports | Fresh metadata/abstract identifies Actin bodies in yeast quiescent cells: an immediately available actin reserve?. Full-body inspection is only claimed for separately identified article-body evidence. |
| plaque-arp-agent-pmid-9210376 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9210376%20AND%20SRC%3AMED; Exact Europe PMC bibliographic fields and abstract | supports | Fresh metadata/abstract identifies The complex containing actin-related proteins Arp2 and Arp3 is required for the motility and integrity of yeast actin patches.. Full-body inspection is only claimed for separately identified article-body evidence. |
| plaque-arp-agent-jats-jcb.200404159 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2172413.1/PMC2172413.1.xml; Fresh native PMC JATS; complete Introduction, Results/Discussion and Materials/Methods; all main captions and TableI | supports | Young2004 examines partially purified cortical patches, filament branches and sac6/cap1 mutants. Branch geometry agrees with Arp2/3-mediated nucleation; it does not determine the Arc35/Arc19 clamp or individual Arc40/Arc18/Arc15 activation coupling stated in the record. |
| plaque-arp-agent-galletta2008-plos | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060001; Fresh publisher HTML; Introduction, first Las17 acidic-domain Results and Figures1/2 captions, relevant Discussion passages, main Materials/Methods | supports | The experiments track regulator mutations and patch assembly/movement in yeast. Distinct and overlapping activator roles are supported; targeting versus activation and tagged-Las17 limitations remain explicit. No raw movies or complete other-regulator Results audit is claimed. |
| plaque-arp-agent-sagot2006-browser | https://pmc.ncbi.nlm.nih.gov/articles/PMC1635378/; Fresh native PMC HTML (not cached browser excerpt); Methods strains/media/microscopy; Results Several Actin-binding Proteins Colocalize with Actin Bodies and Figure3 caption | supports | The full native page is now accessible. Inspected sections report partial colocalization of Arc15,Arc18,Arc35,Arp2 with quiescent-cell actin bodies in a29-protein screen. This supports the carefully limited example notes, not a whole-complex occupancy census. Other body sections and supplementary data were not audited. |
| plaque-adapter-catalogue | https://imodulondb.org/api/datasets; Complete returned public catalogue,20 organism entries and28 dataset keys | supports | No Saccharomyces,Candida,Aspergillus,Neurospora or other eukaryotic dataset occurs in this bounded current catalogue. Germ-tube molecular polarity/septin claims and Arp named yeast proteins therefore have no matching downstream iModulonDB query. Absence is database coverage, not negative biological evidence. |
| plaque-current-0 | data/structures/appendage/germ_tube.yaml; Entire current maintained YAML including graph and history | supports | Current full record read and compared with historical input; unchanged record reassessed against fresh sources. |
| plaque-original-0 | reviews/structured/20261021T094732Z-germ-tube-audit/review.yaml; Full original review including findings/actions/source scopes | supports | Historical observation preserved. Native validation/render and historical frozen input hashes pass; prior scientific findings are independently reassessed. |
| plaque-current-1 | data/structures/cytoskeleton/arp2_3_protein_complex.yaml; Entire current maintained YAML including graph and history | supports | Current full record read and compared with historical input; stale changed types substantively reassessed. |
| plaque-original-1 | reviews/structured/20261021T094741Z-arp2-3-protein-complex-audit/review.yaml; Full original review including findings/actions/source scopes | supports | Historical observation preserved. Native validation/render and historical frozen input hashes pass; prior scientific findings are independently reassessed. |
| plaque-policy | src/cellstructuremech/schema/cellstructuremech.yaml; ComponentTypeEnum,GraphKindEnum,CausalGraphScopeEnum and essentiality definitions | supports | PROTEIN denotes a family/paralogue group; PROTEIN_COMPLEX denotes a named subcomplex. ASSEMBLY describes how a structure is built; membership alone does not provide assembly mechanism. |
| plaque-graph-contract | .claude/skills/curate-causal-graphs/SKILL.md; Native graph source/scope contract | supports | Require supported causal/assembly paths and keep membership separate from mechanism. |
| plaque-adapter-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks | supports | Molecular triggers require actual applicability assessment; source fallback is allowed when the runner is unavailable. |
| plaque-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; NO_GENE_SYMBOLS and generic-class exception | supports | Generic protein classes may remain without invented species-specific genes/examples; named heteromeric groups require checking declared symbols. |
| plaque-arp-category-0 | reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml; F1 exact Arp2/3 component-type fields and multi-target finding scope | supports | The predecessor covers seven records. Current Arp2/3 fields are corrected, but this subreview does not reassess every predecessor target and does not make a terminal whole-finding disposition. |
| plaque-arp-category-1 | reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.yaml; F1 exact Arp2/3 component-type fields and multi-target finding scope | supports | The predecessor covers two records. Current Arp2/3 fields are corrected, but this subreview does not reassess every predecessor target and does not make a terminal whole-finding disposition. |
| plaque-issue-2420 | https://github.com/CultureBotAI/CellStructureMech/issues/2420; Root-fetched issue body and CLOSED state, independently reread; SHA binds captured JSON | supports | Historical grouped record repair issue is already closed and explicitly includes the relevant Arp2/3 type correction. No record fix is attributed to PR2352. |
| plaque-issue-2431 | https://github.com/CultureBotAI/CellStructureMech/issues/2431; Root-fetched issue body and CLOSED state, independently reread; SHA binds captured JSON | supports | Historical grouped record repair issue is already closed and explicitly includes the relevant Arp2/3 type correction. No record fix is attributed to PR2352. |
| plaque-original-validation | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/adversary-plaque/original-validation.json; Two original native validates/renders and historical input hashes | supports | Both originals validate and render byte-identically; all14/13 historical source inputs match their declared Git revision. |
| plaque-germ-tube-native-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/germ-tube-uniprot-verify-receipt.json; Complete receipt plus log stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root-executed native command passed at source head; this reviewer independently read the receipt/log and verified stdout hash. Existing UniProt examples/xrefs validate; empty germ-tube example inventory is not positive molecular coverage. |
| plaque-germ-tube-native-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/germ-tube-uniprot-causal-receipt.json; Complete receipt plus log stdout SHA256 b6822abc52c170ca6071fcc71dc3f3492257d585e43f5b9f69d69f689b54e063 | supports | Root-executed native command passed at source head; this reviewer independently read the receipt/log and verified stdout hash. Germ tube reports one NO_GENE_SYMBOLS and zero COVERED; generic class scope retained. |
| plaque-arp2-3-native-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/arp2-3-uniprot-verify-receipt.json; Complete receipt plus log stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Root-executed native command passed at source head; this reviewer independently read the receipt/log and verified stdout hash. Existing UniProt examples/xrefs validate; empty germ-tube example inventory is not positive molecular coverage. |
| plaque-arp2-3-native-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/arp2-3-uniprot-causal-receipt.json; Complete receipt plus log stdout SHA256 3ee1f7c6d9fefa540b329cd2e05709cc0e2459a9ab0e66c0ee6415f63ff6f88c | supports | Root-executed native command passed at source head; this reviewer independently read the receipt/log and verified stdout hash. Arp2/3 reports three COVERED component-ref nodes and zero other diagnostic categories; this is declared-symbol coverage, not mechanism/necessity proof. |
| micro-record-nine-two | data/structures/appendage/9_2_motile_cilium.yaml; Entire maintained YAML: definition, hierarchy, all components/examples, taxa, functions, evidence, every graph node/edge and history. | context_only | Complete current target independently assessed. Current source/HEAD and historical source target bytes match the original frozen hash; status remains PROPOSED. No image, quantitative measurement or verbatim snippet is asserted. |
| micro-prior-nine-two | reviews/structured/20261021T094726Z-9-2-motile-cilium-audit/review.yaml; Entire authoritative YAML; all assessments/findings/actions/checks/limitations; native-rendered Markdown compared byte-for-byte. | context_only | Original needs_curation verdict and two exact findings remain historical observations. Source-specific limitations and old validator totals are not represented as current results. |
| micro-record-base | data/structures/appendage/ciliary_base.yaml; Entire maintained YAML: definition, hierarchy, all components/examples, taxa, functions, evidence, every graph node/edge and history. | context_only | Complete current target independently assessed. Current source/HEAD and historical source target bytes match the original frozen hash; status remains PROPOSED. No image, quantitative measurement or verbatim snippet is asserted. |
| micro-prior-base | reviews/structured/20261021T094729Z-ciliary-base-audit/review.yaml; Entire authoritative YAML; all assessments/findings/actions/checks/limitations; native-rendered Markdown compared byte-for-byte. | context_only | Original needs_curation verdict and two exact findings remain historical observations. Source-specific limitations and old validator totals are not represented as current results. |
| micro-record-motile | data/structures/appendage/motile_cilium.yaml; Entire maintained YAML: definition, hierarchy, all components/examples, taxa, functions, evidence, every graph node/edge and history. | context_only | Complete current target independently assessed. Current source/HEAD and historical source target bytes match the original frozen hash; status remains PROPOSED. No image, quantitative measurement or verbatim snippet is asserted. |
| micro-prior-motile | reviews/structured/20261021T094737Z-motile-cilium-audit/review.yaml; Entire authoritative YAML; all assessments/findings/actions/checks/limitations; native-rendered Markdown compared byte-for-byte. | context_only | Original needs_curation verdict and two exact findings remain historical observations. Source-specific limitations and old validator totals are not represented as current results. |
| micro-record-probasal | data/structures/cytoskeleton/ciliary_pro_basal_body.yaml; Entire maintained YAML: definition, hierarchy, all components/examples, taxa, functions, evidence, every graph node/edge and history. | context_only | Complete current target independently assessed. Current source/HEAD and historical source target bytes match the original frozen hash; status remains PROPOSED. No image, quantitative measurement or verbatim snippet is asserted. |
| micro-prior-probasal | reviews/structured/20261021T094748Z-ciliary-pro-basal-body-audit/review.yaml; Entire authoritative YAML; all assessments/findings/actions/checks/limitations; native-rendered Markdown compared byte-for-byte. | context_only | Original needs_curation verdict and two exact findings remain historical observations. Source-specific limitations and old validator totals are not represented as current results. |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Structured Source Cross-Checks; Workflow. | context_only | Named IFT, CEP290/NPHP4 and SAS6/Bld10 trigger structured-source applicability even without an expression-module assertion. Source tiers, exact scopes and stable lineage must be retained. |
| micro-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Source, node/edge, scope and completion requirements; add-cell-structure contract read. | context_only | Static membership and generic outputs do not themselves establish a mechanism. Primary evidence must support directed causal events. |
| micro-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent essentiality and roles; CausalGraph/GraphKindEnum/CausalGraphScopeEnum. | context_only | Essentiality means whether the structure forms without a component. FUNCTION explains how it does its job; NONMECHANISTIC and REVIEW_NEEDED are legal scope values. |
| micro-protein-policy | .claude/skills/uniprot-protein-examples/SKILL.md; Rules 1–5 and read-only verify/causal-graph workflow. | context_only | Check primary accession, exact native token/status/taxon, published locus bridge where needed and location-specific experimental annotations. Structural assemblies are not individual protein families. |
| micro-config | conf/record_review.yaml; Complete active skill and rubric routing. | context_only | Configuration was frozen by root before this slice; the active review route and rubrics were reread. |
| micro-mastigoneme-context | data/structures/appendage/mastigoneme.yaml; Entire neighbor read for identity/modeling context only after root froze it. | context_only | Neighbor separately models bounded Chlamydomonas mastigoneme evidence and unresolved broader scope. Its statements are contextual, not an independently reviewed fifth target or proof of universal motile-cilium membership. |
| micro-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005815,GO:0005874,GO:0005929,GO:0005930,GO:0030990,GO:0031514,GO:0035869,GO:0036064,GO:0060170,GO:0060271,GO:0060285,GO:0097537,GO:0097546,GO:0097729,GO:0097740,GO:0097741,GO:0110165,GO:0120280; All 18 active result id/name/definition/synonym/children/relation fields. | supports | Exact identities and hierarchy agree: 9+2 is a motile-cilium subtype; base belongs to cilium and includes distal basal body, transition fibers and TZ; Y-link is a TZ complex. PFR is limited to some flagellated protists; mastigonemes to some algae. Inverse child part_of listings do not establish obligatory broad-class has_part. GO0120280 explicitly cannot nucleate a cilium until mature; GO0036064 describes the mature nucleating body. |
| micro-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; taxId/scientificName/rank/lineage. | supports | Taxon3055 is Chlamydomonas reinhardtii; this verifies identity, not prevalence at every life-cycle stage. |
| micro-uniprot-Q5DM57 | https://rest.uniprot.org/uniprotkb/Q5DM57.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Reviewed IFT172/FLA11 at taxon3055; experimental basal-body location cites PMID17326139 and9585417. Peribasal primary evidence is not proof of permanent basal-body incorporation. |
| micro-uniprot-Q68RJ5 | https://rest.uniprot.org/uniprotkb/Q68RJ5.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Reviewed IFT81 at taxon3055; its cilium location is ECO0000305, so the record correctly uses identity-only evidence. |
| micro-uniprot-Q6RCE1 | https://rest.uniprot.org/uniprotkb/Q6RCE1.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Reviewed IFT74 with IFT71 and IFT74/72 aliases at taxon3055; location ECO0000305 is not imported as experimental evidence. |
| micro-uniprot-A2T2X4 | https://rest.uniprot.org/uniprotkb/A2T2X4.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Reviewed IFT46/FAP32 at taxon3055; experimental basal-body/cilium localization annotations include PMID15955805,17312020,18852297. These are location-specific annotations, distinct from full primary experiment review. |
| micro-uniprot-Q9FPW0 | https://rest.uniprot.org/uniprotkb/Q9FPW0.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Unreviewed IFT88 at taxon3055; exact submitted label and gene token agree; no location comment supports an experimental localization assertion. |
| micro-uniprot-A0A2K3DWT6 | https://rest.uniprot.org/uniprotkb/A0A2K3DWT6.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Unreviewed exact Cep290-domain label and CHLRE_03g167550v5 ORF at taxon3055. Automatic ARBA location is not experimental evidence; literature mapping is checked separately. |
| micro-uniprot-A0A2K3D4W1 | https://rest.uniprot.org/uniprotkb/A0A2K3D4W1.json; primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR LOCATION and ECO/PubMed attribution where present. | supports | Unreviewed Nephrocystin-4 label and CHLRE_12g531400v5 ORF at taxon3055; no location comment. The current recommended name is inferred by ProtNLM, not new experimental evidence. |
| micro-ift-reviewed-search | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIFT172%20OR%20gene_exact%3AIFT81%20OR%20gene_exact%3AIFT74%20OR%20gene_exact%3AIFT46%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&amp;format=json&amp;size=100; All four result accessions and their own gene tokens; response total and pagination headers. | supports | One reviewed native match each: IFT172 Q5DM57, IFT81 Q68RJ5, IFT74 Q6RCE1, IFT46 A2T2X4; no ambiguity within this bounded query. |
| micro-base-reviewed-search | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP290%20OR%20gene_exact%3ANPHP4%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&amp;format=json&amp;size=100; Complete empty results array; response headers. | supports | Zero reviewed entries for these exact symbols in taxon3055. This does not establish absence under every alternate name. |
| micro-ift88-reviewed-search | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AIFT88+AND+organism_id%3A3055+AND+reviewed%3Atrue&amp;format=json&amp;size=100; Complete empty results array; response headers. | supports | Zero reviewed IFT88 exact-gene matches at taxon3055 in this bounded query; the existing unreviewed accession is retained without asserting universal reviewed-entry absence. |
| micro-ift-bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nrm952%22%20OR%20DOI%3A%2210.1083/jcb.200504008%22%20OR%20DOI%3A%2210.1104/pp.010807%22%20OR%20DOI%3A%2210.1126/science.1128618%22%20OR%20EXT_ID%3A15955805%20OR%20EXT_ID%3A17312020%20OR%20EXT_ID%3A17326139%20OR%20EXT_ID%3A18852297%20OR%20EXT_ID%3A9585417&amp;format=json&amp;resultType=core&amp;pageSize=100; All nine exact DOI/PMID title/author/publication-type identities and returned abstracts. | context_only | Pazour, Nicastro, Cole, Hou, Ahmed, Sloboda and Lucker are primary studies; Silflow and Rosenbaum are reviews. Sloboda/Lucker current reassessment is abstract plus native annotation scope only. Silflow has no returned abstract. Metadata resolution does not prove body access. |
| micro-base-bibliography | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.cub.2014.11.066%22%20OR%20DOI%3A%2210.1038/s41467-022-31751-0%22%20OR%20DOI%3A%2210.1083/jcb.201006105%22%20OR%20DOI%3A%2210.1101/cshperspect.a028134%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Four exact DOI/PMID identities and abstracts. | context_only | Craige2010, Diener2015 and Wang2022 are primary papers; Garcia-Gonzalo/Reiter2017 is secondary. Its inspected abstract separates transition fibers (distal basal body to membrane) from TZ Y-links; current body attempts failed, so no fresh whole-review reading is claimed. |
| micro-pazour2005 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2171396.1/PMC2171396.1.xml; Results Identification of flagellar proteins; Distribution of proteins in flagellar fractions; Discussion A subset of membrane proteins appear to be anchored to the axoneme. | supports | Purified Chlamydomonas flagella support the canonical example and membrane/matrix/axoneme distinction. WT Tergitol material and oda1-1 Nonidet/KCl fractions are distinct preparations. Candidate peptides, co-fractionation and intact membranes do not independently demonstrate assembly necessity or universal membership. |
| micro-cole1998 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132775.1/PMC2132775.1.xml; Cultures and Indirect Immunofluorescence Methods; Discussion Colocalization of FLA10 Kinesin-II and p172 at the Basal Bodies. | supports | IFT p172/p81/p139 concentrate around basal bodies, but the paper leaves their exact relationship to basal bodies versus rootlets unresolved. FLA10 transport and p172 regional targeting are distinct; p172 targeting can persist in bld2/inactive-fla10 contexts. This supports associated assembly machinery, not whole-cilium self-assembly. |
| micro-hou2007 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2064023.1/PMC2064023.1.xml; Results Cloning of C. reinhardtii IFT46; complex-A/B regional compartments; Discussion IFT46 stability and A/B distribution; gene-cloning methods. | supports | IFT46 is complex-B associated, predominantly peribasal with flagellar puncta. Null and suppressor interpretations distinguish assembly, complex stability and outer-arm transport; complex-A/B regional overlap is not interchangeable with permanent incorporation into a structural region. |
| micro-ahmed2008 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2568026.1/PMC2568026.1.xml; Results ODA16 localization; In vivo interaction between ODA16 and IFT particles; C. reinhardtii strains. | supports | Peribasal/flagellar ODA16 distribution and Chlamydomonas extract co-immunoprecipitation with IFT46/IFT81 support cargo-adaptor transport context. ODA16 does not co-purify as a retained outer-arm constituent; the mammalian screen is distinct from algal assays. |
| micro-craige2010 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2935561.1/PMC2935561.1.xml; Results CEP290 location, mutant connector defects, immunogold localization and abnormal flagellar composition; Discussion component/connector interpretation. | supports | Chlamydomonas CEP290 loss/rescue and immunolocalization support TZ link organization and membrane tethering. Mutants have altered Y/wedge connections and composition; most axonemes and basal bodies are normal. No complete Y-link protein inventory or universal gate mechanism follows. |
| micro-wang2022 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9271036.1/PMC9271036.1.xml; Results Loss of TCTN1 ciliogenesis/ultrastructure; independent localization; variable phenotypes; ciliary-composition and ectosome sections at their stated opening comparisons; Strains and cell culture. | supports | TCTN1 wedge defects differ from Y-link loss; a normal 9+2 axoneme can remain. CEP290/TCTN1/NPHP4 occupy distinct TZ positions and localize independently. Mutant/autolysin/media conditions affect visible ciliogenesis. Comparative composition and ectosome assays support coarse regulation claims; no raw proteomics or all supplementary experiments were reanalyzed. |
| micro-diener2015 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4318714.1/PMC4318714.1.xml; Results Isolation of transition zones, Ultrastructure and Proteomic analysis; Fig1B and Fig2 captions. | supports | Resorbing Chlamydomonas flagella yield isolated TZ vesicles with depolymerized outer doublets and missing in-situ features. The enriched preparation supports the canonical TZ-proteomics example, not a complete base inventory. Fig1B explicitly excludes transition fibers from TZ; the broader base therefore has known regions omitted by the current three TZ-only rows. |
| micro-rosenbaum2002 | https://www.nature.com/articles/nrm952; Publisher Key Points and Abstract before subscription-content notice. | context_only | Secondary review context: nonmembrane IFT particles move bidirectionally with kinesin-II and dynein; precursor delivery supports assembly/maintenance. Current access did not include the full review body. |
| micro-silflow-access | https://pmc.ncbi.nlm.nih.gov/articles/PMC1540183/?pdf=1; PMC article metadata and PDF-only body notice. | context_only | Silflow/Lefebvre2001 citation identity is confirmed, but this HTML provides no review body. It supplies no direct current proof of paraflagellar-rod or broad taxonomic claims. |
| micro-gene-5728998 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&amp;id=5728998&amp;retmode=xml; Entrezgene_gene/Gene-ref locus tag, Phytozome cross-reference and formal name. | supports | NCBI Gene5728998 links CHLRE_03g167550v5 to Cre03.g167550. Formal name is uncharacterized protein; this alone does not prove CEP290 or NPHP4 symbol assignment. |
| micro-gene-5718574 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&amp;id=5718574&amp;retmode=xml; Entrezgene_gene/Gene-ref locus tag, Phytozome cross-reference and formal name. | supports | NCBI Gene5718574 links CHLRE_12g531400v5 to Cre12.g531400. Formal name is uncharacterized protein; this alone does not prove CEP290 or NPHP4 symbol assignment. |
| micro-fauser2022 | https://www.nature.com/articles/s41588-022-01052-9.pdf; PDF page5/printed709, Fig4d first two row labels and Fig4 caption; page rendered locally and visually inspected. | supports | Fauser2022 labels Cre12.g531400 as NPHP4 and Cre03.g167550 as CEP290. Together with NCBI locus bridges, this supports the two exact literature-to-native-ORF mappings. Only these labels and caption/context were assessed, not the whole screen or supplementary data. |
| micro-dutcher2016 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4888484.1/PMC4888484.1.xml; Basal body structure and Basal body duplication sections, including Fig1 caption. | context_only | Secondary review distinguishes two mature and two pro-basal bodies, cartwheel-to-triplet progression and maturation; early new pro-basal bodies begin with singlets. BLD10 is associated with spoke tips rather than the SAS6 hub. It supports developmental context, not a new primary experiment. |
| micro-wingfield2018 | https://pmc-oa-opendata.s3.amazonaws.com/PMC6070942.1/PMC6070942.1.xml; Sections2.1 Basal Bodies,2.2 scaffold,4.2 developmental cycle and5.1 axoneme templating. | context_only | Secondary review distinguishes SAS6 spokes and Bld10/Cep135 pinheads, dormant pro-basal bodies versus flagellated generations, and mature axoneme templating. Specific molecular arrangements are not generalized to every protist. |
| micro-matsuura2004 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2172387.1/PMC2172387.1.xml; Results EM of bld10 basal bodies; Localization of Bld10p; Immuno-EM, including Fig7 context. | supports | Primary Bld10 antibody and immunogold evidence localizes Bld10 to cartwheel fibers, including pro-basal bodies. Examined bld10 sections lack morphologically recognizable normal basal bodies; this is not a demonstration that Bld10 forms the central SAS6 hub. |
| micro-dutcher1998-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.9.6.1293; Exact DOI/PMID identity and complete returned primary abstract only. | supports | uni3-1 cells can assemble zero, one or two flagella and show proximal doublets rather than triplets. This is not complete absence of every triplet throughout the organelle, nor proof that triplets are universally dispensable. The exact Discussion sentence cited in the record was not freshly recovered. |
| micro-nakazawa2007-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2007.11.046; Exact DOI/PMID identity and complete returned primary abstract only. | supports | SAS6 localizes centrally; bld12 lacks that central cartwheel part and can form centrioles with variable triplet counts. The record correctly identifies this as abstract-level evidence and retains UNKNOWN assembly essentiality for the whole cartwheel. |
| micro-hiraki2007-abstract | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17900905+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=10; PMID17900905, DOI10.1016/j.cub.2007.09.021; complete returned primary abstract only. | supports | Truncated Bld10 constructs and immunoelectron localization identify Bld10 as a major cartwheel-spoke-tip component attaching triplets. This directly supports correcting the definition’s SAS6/Bld10 hub wording. Exact percentage measurements are not imported into the record. |
| micro-probasal-agent-doi-s13630-016-0039-z | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1186/s13630-016-0039-z; DOI, PMID, title, authors and publication type. | context_only | Bibliographic identity confirms the cited secondary review; source-native full-text sections are evaluated separately. |
| micro-probasal-agent-doi-cells7070079 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.3390/cells7070079; DOI, PMID, title, authors and publication type. | context_only | Bibliographic identity confirms the cited secondary review; source-native full-text sections are evaluated separately. |
| micro-nicastro-browser | https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography; Fresh browser-returned author-uploaded text lines71–77 and112–215, plus displayed Fig1–5 captions37–53. Browser response gives no HTTP status; crawl age is explicitly three weeks. | supports | Primary text supports 9+2 architecture and dynein-based sliding/bending context in Chlamydomonas and sea-urchin preparations. Regulatory-linker roles include models. No whole-paper/SOM, movie or raw microscopy audit is claimed in this reassessment. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Entire official API organism/dataset list:20 organisms and28 dataset keys. | context_only | No Chlamydomonas, Tetrahymena, Trypanosoma or other eukaryotic dataset is listed. Named-protein applicability was considered; with no matching organism, downstream module search/summarize is not applicable. Catalogue absence is not biological negative evidence. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical command, timestamp, exit1, status unavailable and PermissionError reason. | context_only | Earlier 00:49Z runner attempt could not read pyvenv.cfg. This is retained historical evidence, not a new execution or proof of present runner success. The current official catalogue was independently inspected as the permitted fallback. |
| micro-native-nine-two-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/9_2_motile_cilium.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/nine-two-uniprot-verify.log; paired receipt captures exact head/base/start/finish. | supports | Exit0: all existing accession/status/label/native-token/taxon pairs verify. Identity validation does not establish biological membership or free-text symbol orthology. |
| micro-native-nine-two-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/9_2_motile_cilium.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/nine-two-uniprot-causal.log; paired receipt captures exact head/base/start/finish. | supports | Exit0: zero GENE_OR_PROTEIN nodes because graph nodes are STRUCTURE/PROCESS. This does not certify every component gene has an example or that graph causality is supported. |
| micro-native-motile-cilium-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/motile-cilium-uniprot-verify.log; paired receipt captures exact head/base/start/finish. | supports | Exit0: all existing accession/status/label/native-token/taxon pairs verify. Identity validation does not establish biological membership or free-text symbol orthology. |
| micro-native-motile-cilium-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/motile-cilium-uniprot-causal.log; paired receipt captures exact head/base/start/finish. | supports | Exit0: zero GENE_OR_PROTEIN nodes because graph nodes are STRUCTURE/PROCESS. This does not certify every component gene has an example or that graph causality is supported. |
| micro-native-ciliary-base-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml --verify; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/ciliary-base-uniprot-verify.log; paired receipt captures exact head/base/start/finish. | supports | Exit0: all existing accession/status/label/native-token/taxon pairs verify. Identity validation does not establish biological membership or free-text symbol orthology. |
| micro-native-ciliary-base-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml --causal-graphs; /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/ciliary-base-uniprot-causal.log; paired receipt captures exact head/base/start/finish. | supports | Exit0: one GENE_OR_PROTEIN node COVERED, linking the two native examples; not a completed mechanistic causality proof. |
| micro-original-validation | scripts/record_review.py validate; render --content; git show historical target; original-checks.json: four original bundles, exact rendered Markdown and current/historical target hashes. | supports | All four native validations exit0, all four render commands exit0 and match saved Markdown byte-for-byte. Each target hash matches its original frozen input and original source commit as well as current HEAD; no target is stale. |
| septin-s2352-longitudinal-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097609,GO:0097610,GO:0097611,GO:0097612,GO:0097729; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-longitudinal-prep-tax-2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-longitudinal-prep-taylor1980-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A7002229%20AND%20SRC%3AMED; Europe PMC exact PMID primary metadata and review abstract only. | supports | Taylor1980 is a review, not an inspected primary experimental body. Its title/author/DOI agree; native GO separately identifies which current term cites it. |
| septin-s2352-longitudinal-prep-taylor1980-api | https://api.elsevier.com/content/article/pii/0303264780900064?httpAccept=text/xml; Publisher API coredata XML, bibliographic fields and description only; HTTP200 did not supply article body. | supports | Source identity is verified; this response is not evidence of a flagellar assembly mechanism. |
| septin-s2352-longitudinal-prep-sulcus-citation-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:20561119%20AND%20SRC:MED; Europe PMC exact PMID primary-paper metadata and abstract only. | supports | Iwataki2010 concerns Cochlodinium polykrikoides ultrastructure and its flagellar apparatus. Native GO maps this PMID to sulcus GO0097612; no full historical paper inspection is claimed. |
| septin-s2352-longitudinal-prep-maruyama2023-html-native | https://www.jstage.jst.go.jp/article/cytologia/88/4/88_D-23-00024/_html/-char/en; Native J-STAGE primary HTML: abstract, Introduction, culture/live microscopy/extracted-model Methods, claim-bearing longitudinal waveform/retraction Results, Figures1–4 captions and associated Discussion; no raw movies or figure-pixel reanalysis. | supports | A. sanguinea NIES-4631 exhibits planar longitudinal undulation and fold/retraction under specified chamber and temperature conditions. Proposed molecular details and biological purpose remain hypotheses. One strain does not establish class-wide planar motion. |
| septin-s2352-transverse-agent-go-native | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097608,GO:0097729,GO:0097611,GO:0097610; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-transverse-agent-maruyama2024-html-native | https://www.jstage.jst.go.jp/article/cytologia/89/4/89_D-24-00042/_html/-char/en; Native J-STAGE primary HTML: abstract, Introduction, NIES-4631 culture, live microscopy and non-detergent extraction Methods; live undulation, girdle attachment, contraction and reactivation Results; Figures3–6 and10 captions; claim-bearing Discussion. No raw videos or figure-pixel reanalysis. | supports | Observed morphology, attachment and calcium-induced contraction are kept separate from proposed coupling. Mg2+ non-antagonism has a membrane-permeability caveat. Strand morphology does not establish a universal striated-strand-driven beating cycle; force-transmission structures are unresolved. |
| septin-s2352-transverse-agent-epmc-native | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15277560%20OR%20EXT_ID:986199%20OR%20DOI:10.1099/00221287-46-2-305&amp;format=json&amp;resultType=core&amp;pageSize=100; Europe PMC exact PMID/DOI returned primary abstracts and bibliographic metadata, including Miyasaka2004 and Leblond/Taylor1976; Leadbeater1967 entry has no abstract. | supports | Miyasaka2004 uses a Prorocentrum minimum resistive-force numerical model: transverse thrust and longitudinal rudder. This is model/context-specific evidence, not an all-dinoflagellate force partition or a native full-body read. |
| septin-s2352-transverse-agent-schuech2025-dtu-native | https://orbit.dtu.dk/en/publications/fluid-dynamics-of-dinoflagellate-feeding-and-swimming/; DTU institutional publication record: primary abstract, title/authors/DOI only; full paper and underlying flow data not inspected. | supports | Schuech2025 abstract describes flow visualization and computational fluid dynamics, with transverse thrust and trailing steering. Distinguish this abstract-level claim from Cachon1991 organism-specific observations. |
| septin-s2352-aster-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000235,GO:0005818,GO:0005819,GO:0005874,GO:0030989,GO:0032117,GO:0043232,GO:0099080; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-tax-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-P04689 | https://rest.uniprot.org/uniprotkb/P04689.json; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-query-tub1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Atub1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-P04688 | https://rest.uniprot.org/uniprotkb/P04688.json; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-query-nda2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Anda2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-P05219 | https://rest.uniprot.org/uniprotkb/P05219.json; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-query-nda3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3Anda3%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-aster-agent-doi-j.cub.2005.07.058 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2005.07.058; Europe PMC exact DOI primary abstract and bibliographic metadata only. | supports | Tanaka2005 identifies S. pombe Hrs1/Mcp6-dependent meiotic HAA organization, impaired HAA/HNM on deletion, ectopic-expression phenotype and gamma-TuRC interaction. Proposed minus-end stabilization and recombination relevance are not converted to universal mechanisms. |
| septin-s2352-aster-agent-doi-j.cub.2012.02.042 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cub.2012.02.042; Europe PMC exact DOI primary metadata and abstract, distinct from the native full-body source below. | supports | Funaya2012 source identity and meiotic reorganization context verified; claim-specific body/caption/supplement evidence is separately bounded. |
| septin-s2352-aster-agent-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml; Native PMC open-data JATS body: Introduction, Hrs1/rMTOC localization and gamma-tubulin Results, meiotic disassembly and phosphorylation passages, Figure4 full caption and experimental context. Not every remaining paragraph, movie or raw dataset was independently reanalyzed. | supports | S. pombe meiotic radial arrays and Hrs1/rMTOC are distinct from the ensuing MI spindle. Figure4A uses homothallic Hrs1-GFP/mCherry-Atb2 cells; synchronized pat1 mat-Pc diploids are separate experiments. This supports the specialized example, not broad Kar9/Bim1/EB1/Bik1 mitotic capture claims or an isoform occupancy census. |
| septin-s2352-aster-agent-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/mmc1.pdf; Native PMC mmc1 PDF text: TableS1 strains (including KT2901 and separate pat1 mat-Pc diploids), relevant FigureS1–S3 captions and Supplemental Experimental Procedures for synchronization, fluorescent imaging and EM preparation. Not complete supplement-wide or image/movie reanalysis. | supports | KT2901 is homothallic with Hrs1-GFP-2xFLAG and Pnda3-mCherry-atb2; imaging and synchronized ultrastructure preparations remain distinct. Reference UniProt strain identity is not asserted to be the exact experimental stock. |
| septin-s2352-astral-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000235,GO:0005818,GO:0005819,GO:0005874,GO:0005876,GO:0030989,GO:0032117; Fresh native issuing-authority response: exact identifiers, labels, definitions, taxon or returned family/protein annotation fields. | supports | Current identifiers and source attribution checked within the returned authority scope. Identity annotation is not a new primary experiment or proof of assembly necessity. |
| septin-s2352-current-adapter-catalogue | https://imodulondb.org/api/datasets; Entire fresh official /api/datasets response: 20 organism objects and 28 dataset keys; all returned organism names inspected. | supports | No Schizosaccharomyces, other fungal or protist dataset occurs in this bounded returned catalogue. Therefore the molecular aster/astral records have no matching dataset for downstream gene/module queries. This is a catalogue coverage result, not gene absence or an exemption based on lack of expression claims. |
| septin-s2352-cachon-indexed | https://aquaparadox.obs-vlfr.fr/html/PFD/Taxonomic%20Monographs/Cachon%20et%20al%201991.pdf; Fresh browser-indexed primary PDF passages, returned text lines0–66,154–224,254–257,288–323,431–469: organisms/methods, longitudinal waveforms, motility interpretation and proposed coiling. Native download timed out; no native PDF bytes, figure pixels or raw videos read. | supports | Ceratium and Oxyrrhis observations include three-dimensional nonplanar longitudinal waves and different retraction/motility modes. Calcium-driven striated-fiber coiling is proposed in Discussion. These contexts differ from planar Akashiwo; the sources do not establish one universal waveform or thrust partition. |
| septin-s2352-leadbeater-micro-abstract | https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-46-2-305; Fresh publisher page abstract, returned lines47–52 only. Native request403; browser page did not supply full body. | supports | Leadbeater/Dodge1967 abstract describes 9+2 organization, transverse ribbon morphology, shorter striated strand, sheath and hairs. Morphology supports scoped structure, not a complete causal beat mechanism. |
| septin-s2352-leadbeater-nature-preview | https://www.nature.com/articles/213421a0; Fresh indexed publisher abstract/preview only; native HTTP200 response was an authorization page and is not treated as article text. | supports | Preview distinguishes posterior flagellar and transverse helical observations and source taxa. It is not a newly retrieved native full body. |
| septin-s2352-cachon-bounded-search | https://aquaparadox.obs-vlfr.fr/html/PFD/Taxonomic%20Monographs/Cachon%20et%20al%201991.pdf; Saved returned web search results used to locate the matching primary indexed PDF. | supports | Source discovery only; returned hits do not establish literature absence. |
| septin-s2352-record-longitudinal_flagellum | data/structures/appendage/longitudinal_flagellum.yaml; Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174: definition, hierarchy, components, examples, evidence, discussions and every graph node/edge. | supports | Current record equals original frozen target bytes. |
| septin-s2352-record-transverse_flagellum | data/structures/appendage/transverse_flagellum.yaml; Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174: definition, hierarchy, components, examples, evidence, discussions and every graph node/edge. | supports | Current record equals original frozen target bytes. |
| septin-s2352-record-aster | data/structures/cytoskeleton/aster.yaml; Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174: definition, hierarchy, components, examples, evidence, discussions and every graph node/edge. | supports | Current record differs by added nda2 alpha-tubulin symbol plus curation history. Scientific content was reassessed against current sources and native checks; no record edit. |
| septin-s2352-record-astral_microtubule | data/structures/cytoskeleton/astral_microtubule.yaml; Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174: definition, hierarchy, components, examples, evidence, discussions and every graph node/edge. | supports | Current record differs by added nda2 alpha-tubulin symbol plus curation history. Scientific content was reassessed against current sources and native checks; no record edit. |
| septin-s2352-policy | docs/CURATION.md; Current frozen policy/schema, relevant evidence and causal graph passages. | supports | Evidence must match the scientific assertion and taxon/state; named molecular claims require structured-source applicability assessment. |
| septin-s2352-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Current frozen policy/schema, relevant evidence and causal graph passages. | supports | Mechanistic claims need evidenced causal direction; spatial containment alone is not an assembly mechanism. |
| septin-s2352-graph-scope-policy | .claude/skills/add-cell-structure/SKILL.md; Current frozen policy/schema, relevant evidence and causal graph passages. | supports | The native graph contract distinguishes source-backed causal mechanism from topology/function summaries; no atomistic detail or invented mechanism is demanded. |
| septin-s2352-graph-schema | src/cellstructuremech/schema/cellstructuremech.yaml; Current frozen policy/schema, relevant evidence and causal graph passages. | supports | Native schema field/type meanings checked; schema-valid graphs may still exceed their scientific source scope. |
| septin-s2352-prior-nda2-finding | reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml; F2, issue_key cytoskeleton-fission-yeast-nda2-gene-symbol-omission; targets GO0005818, GO0000235, GO0032117, GO1990295. | supports | Current first two assigned records now contain nda2; their corrected symbol is independently verified. Other two targets are unassessed here, so this multi-target historical finding is not terminally resolved by this subreview. Root reports linked issue2421 already closed. |
| septin-s2352-original-native-checks | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/adversary-septin/original-checks.json; Four original native validate and render --content runs; committed Markdown byte comparisons and frozen/source/current hashes. | supports | All four original bundles validate and render identically. Two flagellar targets unchanged; aster/astral changed since original freeze and are substantively refreshed here. Historical QC receipts are not current CI. |
| septin-s2352-aster-native-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/aster-uniprot-verify-receipt.json; Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/aster.yaml', '--verify'] at head 9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently read. | supports | Exit0: protein examples and causal graph UniProt xrefs verified. |
| septin-s2352-aster-native-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/aster-uniprot-causal-receipt.json; Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/aster.yaml', '--causal-graphs'] at head 9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently read. | supports | Exit0: alpha and beta GENE_OR_PROTEIN nodes both COVERED, no missing-symbol/dangling reference. Identifier coverage does not validate broad mechanism or graph-scope claims. |
| septin-s2352-astral-native-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/astral-uniprot-verify-receipt.json; Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/astral_microtubule.yaml', '--verify'] at head 9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently read. | supports | Exit0: protein examples and causal graph UniProt xrefs verified. |
| septin-s2352-astral-native-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/astral-uniprot-causal-receipt.json; Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py', '--record', 'data/structures/cytoskeleton/astral_microtubule.yaml', '--causal-graphs'] at head 9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently read. | supports | Exit0: alpha and beta GENE_OR_PROTEIN nodes both COVERED, no missing-symbol/dangling reference. Identifier coverage does not validate broad mechanism or graph-scope claims. |
| septin-s2352-historical-runner-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z, exit1 PermissionError reading pyvenv.cfg; inherited actual receipt, not a current invocation. | supports | The historical runner was OS-unavailable. Current applicability uses a fresh official catalogue fallback; no runner or downstream gene/module execution is claimed. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2352 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Germ tube and Arp2/3 complex independent subreview: Douglas2005 remains secondary review evidence; the inspected Candida subsection distinguishes localization patterns. Warenda2002 is Candida BWP17-derived primary context, with inspected strains/media, microscopy, claim-bearing localization/hyphal-mutant Results and captions. It is not a direct three-species Cdc42/Spitzenkörper/polarisome test. No raw image pixels, movies or complete septin-class ablation were assessed.
- Germ tube and Arp2/3 complex independent subreview: Young2004 complete main text/captions/TableI were freshly read, including purification and negative-stain limitations. No supplementary data or raw microscopy reanalysis. Galletta2008 scope is Introduction, first Las17 Results/Figures1-2 captions, relevant Discussion passages and main Methods; remaining regulator-specific Results and videos were not audited.
- Germ tube and Arp2/3 complex independent subreview: Kaksonen2003 and Winter1997 are freshly checked at metadata/abstract level only; their entire experimental bodies were not independently inspected. A source-specific attribution finding is not proof that the proposed biological mechanism is false.
- Germ tube and Arp2/3 complex independent subreview: Sagot2006 native HTML was accessible this time. Fresh claim-bearing Methods and partial-colocalization Results/Figure3 caption replace dependence on the older indexed excerpt for this observation. Other body sections, complete supplementary tables and raw images were not audited; the original earlier access limitation remains historical.
- Germ tube and Arp2/3 complex independent subreview: All seven exact Arp protein queries return the expected reviewed reference-strain entry. UniProt FUNCTION annotations often carry similarity evidence and do not independently validate the detailed mechanistic source attribution. The component groups are not asserted to share one whole-group InterPro family.
- Germ tube and Arp2/3 complex independent subreview: Assembly necessity remains unknown for generic septins and each Arp component group. Named-subunit deletions, viability, physical membership and catalytic contribution are different endpoints. Generic germ-tube NO_GENE_SYMBOLS is permitted, not a claim of complete concrete-protein coverage.
- Germ tube and Arp2/3 complex independent subreview: Current adapter applicability uses the fresh complete public catalogue only: no matching fungal/eukaryotic dataset. Historical runner unavailability is retained separately by root; no current runner invocation or gene/module search on an unrelated organism is claimed. Catalogue absence is not biological absence.
- Germ tube and Arp2/3 complex independent subreview: Both prior Arp type findings cover additional records beyond this assigned slice. Closed issues2420/2431 and current Arp type corrections are historical context only; no terminal multi-target disposition is emitted. No record fix is credited to PR2352.
- Germ tube and Arp2/3 complex independent subreview: No neighboring scientific record or tracked image was used. Frozen category review pairs, graph/schema/protein policies and native script were read within requested scope. Root owns corpus QC, current identifier gates, issue mutations and CI.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Nicastro current source is a fresh browser response of author-uploaded text with a stated three-week crawl age and no native HTTP status; only displayed lines112–215 and figure captions were assessed. Direct HTTP returned403. Original historical body/SOM access claims remain historical and are not promoted to fresh full-paper access.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Silflow current PMC HTML is PDF-only metadata with no body, and the bibliographic response has no abstract. Rosenbaum is secondary publisher Key Points/Abstract only. Sloboda and Lucker are primary-abstract/native-annotation checks here, not full-body experiments.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Dutcher1998 and Nakazawa2007 current assessment is primary abstract only. Dutcher native PMC attempt returned a browser challenge and EuropePMC JATS500; the exact Discussion wording was not recovered. Hiraki2007 is also primary abstract only. No dimensional/percentage result is newly imported.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Garcia2017 is secondary abstract context here: S3 returned404, PMC HTTP200 was a browser challenge and EuropePMC JATS500. The original bundle’s successful historical body access remains attributed to its original time; this reassessment does not claim to reproduce it.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Dutcher2016 and Wingfield2018 are secondary reviews at the listed sections. Chlamydomonas developmental evidence is not a complete primary audit of Tetrahymena/Trypanosoma molecular details or all eukaryotic assembly pathways.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Assembly-necessity claims for the broad axoneme/membrane/basal-body regions in both motile-cilium records remain independently unverified. Supported anatomy and function are not a substitute for each assembly endpoint; this scientific unknown is not fabricated into an extra issue.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: No raw micrographs, movies, cryo-ET reconstructions or full supplementary proteomics were reanalyzed. Fauser Fig4d locus labels and its caption were visually inspected on rendered PDF page5; no whole-Fauser-paper or screen-data review is claimed.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: The official iModulonDB catalogue was freshly read; the runner receipt is explicitly reused from00:49Z and no new runner execution is claimed. Lack of matching catalogue taxa only bounds source applicability and gives no biological absence result.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: Root runs full local gates and handles GitHub issue deduplication/publication. This independent slice ran original-bundle validation/render/hash checks and inspected six exact root-produced UniProt receipts/logs; it does not relabel original corpus totals as current QC.
- 9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent subreview: The mastigoneme neighbor was frozen before reading and used only as local modeling context. Its scientific contents are not counted as a fifth reviewed target.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Independent current subreview is read-only. Original reviews retain historical source-access and check receipts; those historical claims are not presented as current actions.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Taylor1980 was checked through native metadata/abstract and publisher coredata only. Iwataki2010 was checked at primary abstract/metadata tier for current GO citation attribution. Neither full historical body was inspected.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Maruyama2023/2024 were inspected at the stated native primary body/caption passages for A. sanguinea NIES-4631 and its experimental conditions. No raw videos, figure pixels or complete supplement reanalysis; proposed molecular coupling and biological explanations remain hypotheses.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Cachon1991 native PDF retrieval timed out; fresh browser-indexed paper passages were inspected. Organism/preparation differences from Maruyama remain unresolved variables. Leadbeater1967 is publisher abstract/preview; native Nature200 was authorization HTML, and Microbiology native403. Miyasaka2004 and Schuech2025 remain primary abstract tier, not full-body experiments audited.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Funaya2012 fresh native JATS claim-bearing body, Figure4 caption and specified supplemental strain/methods text were inspected, not every paragraph, figure pixel, movie or raw tomography dataset. Tanaka2005 remains primary abstract/metadata tier. No full-paper access is inferred from citation identity.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: No systematic cross-fungal/protist Kar9/Bim1/EB1/Bik1 homology or mechanism survey was performed. Findings concern unsupported current attribution/scope, not universal absence. Tubulin IDs and mCherry-Atb2 imaging do not prove an isoform occupancy census or necessity.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Historical category F2/#2421 covers four targets. This review verifies its already-corrected nda2 content only for aster and astral microtubule, and does not terminal-resolve the entire multi-target finding or inspect the two other targets.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Official dataset catalogue coverage is bounded to the current returned20 organisms/28datasets. No matching eukaryotic dataset means no applicable downstream gene/module query here, not biological absence. Historical runner failure is not a new failed execution.
- Longitudinal/transverse flagella, aster and astral microtubule independent subreview: Full QC/CI and GitHub issue deduplication are root-owned; this report includes independently inspected original validation/render checks and four root-run focused native protein receipts only.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs are preserved unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Every inherited finding is reassessed against current sources and retains its exact predecessor identity.
- Bundle issues #2548 (three stale reviews) and #2553 (eight structured-source coverage defects) are addressed here. Scientific curation findings remain separately tracked; generic Septin family grounding reuses #2499 with germ tube explicitly added. Existing validator #2514 remains open.
- Prior record corrections are associated with already-closed #2420, #2421 and #2431. Their multi-target category findings are not terminally superseded by this partial cohort; only the current target-specific changes are assessed.
- Source commit 9a8a31291456921b6e1984a3a95f110c763c5174 is retained by tag review-base/pr2352-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration, graph/protein policies, the verifier source, two prior category-review pairs and the mastigoneme neighbor.
- Seven original bundles omit structured-source applicability, while motile cilium contains an unsupported exemption rationale based on the lack of expression/module claims. Sparse longitudinal and transverse flagellar morphology is excluded from this defect.
- Historical source-access failures are not promoted to current failures where fresh body access succeeded. Secondary reviews, primary Methods/Results, abstracts, figure captions and any directly inspected image pixels retain distinct evidence scopes.
- The 24 scientific finding keys are linked to #2499, #2549–#2552 and #2554–#2572. These record-curation issues remain open; #2499 was reused with an explicit germ-tube scope comment after body/comment deduplication.
- Local validation rejected four assessment area values in an uncommitted draft. Issue #2573 tracks the correction to the native schema area without substantive changes; the corrected successor is revalidated and independently re-reviewed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T055122Z-pr2352-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2352: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T05:39:52.336144Z'
finished_at: '2026-11-03T05:51:22Z'
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
summary: 'Current-input reassessment of all ten records in PR2352. Three stale reviews
  are substantively refreshed: Arp2/3 heteromeric component types, and nda2 gene-symbol
  additions for aster and astral microtubule. These corrections predate this PR and
  remain scoped historical context, without terminally resolving unassessed targets
  of earlier category findings. All ten records retain curation findings: five major
  and nineteen minor, each with exact original lineage. The successor corrects structured-source
  coverage for eight original bundles. No scientific record is edited.'
source:
  git_revision: 9a8a31291456921b6e1984a3a95f110c763c5174
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
  - path: data/structures/appendage/9_2_motile_cilium.yaml
    sha256: c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97
    role: target
  - path: data/structures/appendage/ciliary_base.yaml
    sha256: fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb
    role: target
  - path: data/structures/appendage/germ_tube.yaml
    sha256: b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058
    role: target
  - path: data/structures/appendage/longitudinal_flagellum.yaml
    sha256: 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac
    role: target
  - path: data/structures/appendage/mastigoneme.yaml
    sha256: d494a06dcfd0686ab910c8ae88a4899c1f5dd58634339194d24c4dac64d3fbd1
    role: context
  - path: data/structures/appendage/motile_cilium.yaml
    sha256: 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e
    role: target
  - path: data/structures/appendage/transverse_flagellum.yaml
    sha256: 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c
    role: target
  - path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    sha256: 05b7cc75eaf5f65fb7a4839055dcd086303a6c26cf1fb781ad41baf541bd8ecc
    role: target
  - path: data/structures/cytoskeleton/aster.yaml
    sha256: ead65813443a3277dee3611ec40e32b7bc4c3882d8c31508eb352f6fffdfd6df
    role: target
  - path: data/structures/cytoskeleton/astral_microtubule.yaml
    sha256: 45c1ec56a960d58bde433d88317824b726ff48473bc9b0b1d4429c6e2f57041d
    role: target
  - path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    sha256: 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4
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
  - path: reviews/structured/20261021T094726Z-9-2-motile-cilium-audit/review.md
    sha256: 2084cf105004f91c21fab14451581195a981549920490ef8cfa8d129d063f364
    role: context
  - path: reviews/structured/20261021T094726Z-9-2-motile-cilium-audit/review.yaml
    sha256: a275f7cecebd6a709b7f793b6f5fe9de364e1969def47153c0ccd7050ab9c16e
    role: context
  - path: reviews/structured/20261021T094729Z-ciliary-base-audit/review.md
    sha256: b5b6b5dbd70e3395f762e45d46d39f20bc4f8b4cc31d5c639c2247905d4aba99
    role: context
  - path: reviews/structured/20261021T094729Z-ciliary-base-audit/review.yaml
    sha256: 92eb253a5df08a79a6b8e450b592163e870f6ceccce8af550e18a94c64593ec8
    role: context
  - path: reviews/structured/20261021T094732Z-germ-tube-audit/review.md
    sha256: 9ae7df58c4a9d657d655765d757a127a908c69d1fdfb492cf21d5c3183756135
    role: context
  - path: reviews/structured/20261021T094732Z-germ-tube-audit/review.yaml
    sha256: 9b1de100d315882fe532d2ea80007a5bacc138c156a3504b26ae190814fcd466
    role: context
  - path: reviews/structured/20261021T094735Z-longitudinal-flagellum-audit/review.md
    sha256: ba15f3996f539d06c7fabafdf937ae09183f78eb0612d2e346b90d80668c6817
    role: context
  - path: reviews/structured/20261021T094735Z-longitudinal-flagellum-audit/review.yaml
    sha256: 31f8ba103fd349f2369b0b1cc24dd04de5031b0d8fcf96a28707ddd51a97dcb4
    role: context
  - path: reviews/structured/20261021T094737Z-motile-cilium-audit/review.md
    sha256: 511b4f77a07cb575b00598f9e0e3538036fc384c856dabcc2daf2d5f2971ee68
    role: context
  - path: reviews/structured/20261021T094737Z-motile-cilium-audit/review.yaml
    sha256: 4df9df67ffbd6e8e6e36f1ffdd682bba7143f6041f7989905b0f9c83b9be4edb
    role: context
  - path: reviews/structured/20261021T094739Z-transverse-flagellum-audit/review.md
    sha256: 8423b6ea4549dfbe09e339e4d45e4fbf80d6b07aa19d55f26d365efbf94bcd66
    role: context
  - path: reviews/structured/20261021T094739Z-transverse-flagellum-audit/review.yaml
    sha256: 81af91da6e5ced84e1cddc4fe8ce5c7ed16379ebcf8f5572b02978467123011a
    role: context
  - path: reviews/structured/20261021T094741Z-arp2-3-protein-complex-audit/review.md
    sha256: d19d0b751be3aae3e52565eacedd4ab5894649eb49a56014982b13fee183c3c6
    role: context
  - path: reviews/structured/20261021T094741Z-arp2-3-protein-complex-audit/review.yaml
    sha256: b1c7a26ce89e3baa54504df6a45936b1c947c903e45c02e8126986f9c563d738
    role: context
  - path: reviews/structured/20261021T094744Z-aster-audit/review.md
    sha256: 3cf02741cccdfd338d3e57c54ba19bded1ba634bc0c971cfc0536fdda77ac8b9
    role: context
  - path: reviews/structured/20261021T094744Z-aster-audit/review.yaml
    sha256: 70176bbd52c783ecc051375714e2cabfe3dafa4c9402fe5fcea4abc84bd4eabc
    role: context
  - path: reviews/structured/20261021T094746Z-astral-microtubule-audit/review.md
    sha256: 3d37758909be419c5387b2c490f88525f8b7ad6f7a6cd8058cc50ef7983a3db3
    role: context
  - path: reviews/structured/20261021T094746Z-astral-microtubule-audit/review.yaml
    sha256: 8d018e970882cbbf4cc3a1d094620808c31bdfc1e2caa70de6043e174935a61e
    role: context
  - path: reviews/structured/20261021T094748Z-ciliary-pro-basal-body-audit/review.md
    sha256: b8adfd2c60c60d28b60fb6395e5ef584cfef772de3bfd1a72eb1588ec603fcf8
    role: context
  - path: reviews/structured/20261021T094748Z-ciliary-pro-basal-body-audit/review.yaml
    sha256: d9438d264e1f900eec1e755c2a07e6f90977e5143395bf0b244701e02a24cf42
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
- target_id: GO:0097729
  path: data/structures/appendage/9_2_motile_cilium.yaml
  label: 9+2 motile cilium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/9_2_motile_cilium.yaml
    role: maintained scientific record
- target_id: GO:0097546
  path: data/structures/appendage/ciliary_base.yaml
  label: ciliary base
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
- target_id: GO:0032179
  path: data/structures/appendage/germ_tube.yaml
  label: germ tube
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
- target_id: GO:0097609
  path: data/structures/appendage/longitudinal_flagellum.yaml
  label: longitudinal flagellum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
- target_id: GO:0031514
  path: data/structures/appendage/motile_cilium.yaml
  label: motile cilium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
- target_id: GO:0097608
  path: data/structures/appendage/transverse_flagellum.yaml
  label: transverse flagellum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/transverse_flagellum.yaml
    role: maintained scientific record
- target_id: GO:0005885
  path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  label: Arp2/3 protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
- target_id: GO:0005818
  path: data/structures/cytoskeleton/aster.yaml
  label: aster
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
- target_id: GO:0000235
  path: data/structures/cytoskeleton/astral_microtubule.yaml
  label: astral microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
- target_id: GO:0120280
  path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
  label: ciliary pro-basal body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 5c6039e8394ca3a3b1456937d152c911fe0eb696.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    4c23da62a367483cdb5a8dd8b70db494726cbbbf.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head 9a8a31291456921b6e1984a3a95f110c763c5174.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  command: just validate-products
  exit_code: 0
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head 9a8a31291456921b6e1984a3a95f110c763c5174.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head 9a8a31291456921b6e1984a3a95f110c763c5174.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head 9a8a31291456921b6e1984a3a95f110c763c5174.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head 9a8a31291456921b6e1984a3a95f110c763c5174.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0097729
  status: passed
  required: true
  target_ids:
  - GO:0097729
  command: just validate data/structures/appendage/9_2_motile_cilium.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0097729
  status: passed
  required: true
  target_ids:
  - GO:0097729
  command: just validate-strict data/structures/appendage/9_2_motile_cilium.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0097546
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just validate data/structures/appendage/ciliary_base.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0097546
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: just validate-strict data/structures/appendage/ciliary_base.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0032179
  status: passed
  required: true
  target_ids:
  - GO:0032179
  command: just validate data/structures/appendage/germ_tube.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0032179
  status: passed
  required: true
  target_ids:
  - GO:0032179
  command: just validate-strict data/structures/appendage/germ_tube.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0097609
  status: passed
  required: true
  target_ids:
  - GO:0097609
  command: just validate data/structures/appendage/longitudinal_flagellum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0097609
  status: passed
  required: true
  target_ids:
  - GO:0097609
  command: just validate-strict data/structures/appendage/longitudinal_flagellum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate GO:0031514
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: just validate data/structures/appendage/motile_cilium.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict GO:0031514
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: just validate-strict data/structures/appendage/motile_cilium.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0097608
  status: passed
  required: true
  target_ids:
  - GO:0097608
  command: just validate data/structures/appendage/transverse_flagellum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0097608
  status: passed
  required: true
  target_ids:
  - GO:0097608
  command: just validate-strict data/structures/appendage/transverse_flagellum.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate GO:0005885
  status: passed
  required: true
  target_ids:
  - GO:0005885
  command: just validate data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict GO:0005885
  status: passed
  required: true
  target_ids:
  - GO:0005885
  command: just validate-strict data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0005818
  status: passed
  required: true
  target_ids:
  - GO:0005818
  command: just validate data/structures/cytoskeleton/aster.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0005818
  status: passed
  required: true
  target_ids:
  - GO:0005818
  command: just validate-strict data/structures/cytoskeleton/aster.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0000235
  status: passed
  required: true
  target_ids:
  - GO:0000235
  command: just validate data/structures/cytoskeleton/astral_microtubule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0000235
  status: passed
  required: true
  target_ids:
  - GO:0000235
  command: just validate-strict data/structures/cytoskeleton/astral_microtubule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0120280
  status: passed
  required: true
  target_ids:
  - GO:0120280
  command: just validate data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0120280
  status: passed
  required: true
  target_ids:
  - GO:0120280
  command: just validate-strict data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352
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
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  summary: The complete official catalogue was inspected with actual access timestamps
    and bounded organism/dataset scope. It contains no matching eukaryotic dataset
    for the named fungal, algal and protist targets, so downstream matched gene/module
    queries are not applicable. This conclusion follows catalogue coverage rather
    than absence of expression claims. Sparse longitudinal and transverse flagellar
    records are excluded from the eight molecular-coverage defects. Catalogue absence
    is not biological absence; unrelated bacterial datasets are not substituted. Historical
    native-runner unavailability remains separately disclosed, with no fresh runner
    execution or success claimed.
  evidence_ids:
  - plaque-adapter-catalogue
  - micro-adapter-catalogue
  - septin-s2352-current-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-germ-tube-agent-go
  - plaque-germ-tube-agent-epmc
  - plaque-germ-tube-agent-douglas-pmc
  - plaque-germ-tube-agent-warenda2002
  - plaque-germ-tube-agent-family
  - plaque-arp-agent-go
  - plaque-arp-agent-tax-4932
  - plaque-arp-agent-tax-559292
  - plaque-arp-agent-P32381
  - plaque-arp-agent-P47117
  - plaque-arp-agent-P53731
  - plaque-arp-agent-P33204
  - plaque-arp-agent-P38328
  - plaque-arp-agent-Q05933
  - plaque-arp-agent-P40518
  - plaque-arp-agent-kaksonen2003-meta
  - plaque-arp-agent-doi-jcb.200404159
  - plaque-arp-agent-doi-journal.pbio.0060001
  - plaque-arp-agent-doi-mbc.E06-04-0282
  - plaque-arp-agent-pmid-9210376
  - plaque-arp-agent-jats-jcb.200404159
  - plaque-arp-agent-galletta2008-plos
  - plaque-arp-agent-sagot2006-browser
  - plaque-adapter-catalogue
  - plaque-policy
  - plaque-graph-contract
  - plaque-adapter-policy
  - plaque-protein-policy
  - plaque-issue-2420
  - plaque-issue-2431
  - micro-go
  - micro-tax3055
  - micro-uniprot-Q5DM57
  - micro-uniprot-Q68RJ5
  - micro-uniprot-Q6RCE1
  - micro-uniprot-A2T2X4
  - micro-uniprot-Q9FPW0
  - micro-uniprot-A0A2K3DWT6
  - micro-uniprot-A0A2K3D4W1
  - micro-ift-bibliography
  - micro-base-bibliography
  - micro-pazour2005
  - micro-cole1998
  - micro-hou2007
  - micro-ahmed2008
  - micro-craige2010
  - micro-wang2022
  - micro-diener2015
  - micro-rosenbaum2002
  - micro-silflow-access
  - micro-gene-5728998
  - micro-gene-5718574
  - micro-fauser2022
  - micro-dutcher2016
  - micro-wingfield2018
  - micro-matsuura2004
  - micro-dutcher1998-abstract
  - micro-nakazawa2007-abstract
  - micro-hiraki2007-abstract
  - micro-probasal-agent-doi-s13630-016-0039-z
  - micro-probasal-agent-doi-cells7070079
  - micro-nicastro-browser
  - micro-adapter-catalogue
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-tax-2864
  - septin-s2352-longitudinal-prep-taylor1980-api
  - septin-s2352-longitudinal-prep-maruyama2023-html-native
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-transverse-agent-schuech2025-dtu-native
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-tax-4896
  - septin-s2352-aster-agent-tax-284812
  - septin-s2352-aster-agent-IPR002452
  - septin-s2352-aster-agent-IPR002453
  - septin-s2352-aster-agent-P04689
  - septin-s2352-aster-agent-P04688
  - septin-s2352-aster-agent-P05219
  - septin-s2352-aster-agent-paper
  - septin-s2352-aster-agent-supplement
  - septin-s2352-astral-agent-go
  - septin-s2352-current-adapter-catalogue
  - septin-s2352-cachon-indexed
  - septin-s2352-leadbeater-micro-abstract
  - septin-s2352-policy
  - septin-s2352-graph-policy
  - septin-s2352-graph-scope-policy
  - septin-s2352-graph-schema
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0031514
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
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
- check_id: nine-two-uniprot-verify
  name: Native nine-two UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097729
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/9_2_motile_cilium.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nine-two-verify
- check_id: nine-two-uniprot-causal
  name: Native nine-two UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097729
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/9_2_motile_cilium.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-nine-two-causal
- check_id: motile-cilium-uniprot-verify
  name: Native motile-cilium UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-motile-cilium-verify
- check_id: motile-cilium-uniprot-causal
  name: Native motile-cilium UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0031514
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-motile-cilium-causal
- check_id: ciliary-base-uniprot-verify
  name: Native ciliary-base UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-ciliary-base-verify
- check_id: ciliary-base-uniprot-causal
  name: Native ciliary-base UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0097546
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-ciliary-base-causal
- check_id: germ-tube-uniprot-verify
  name: Native germ-tube UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0032179
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/germ_tube.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-germ-tube-native-verify
- check_id: germ-tube-uniprot-causal
  name: Native germ-tube UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0032179
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/germ_tube.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-germ-tube-native-causal
- check_id: arp2-3-uniprot-verify
  name: Native arp2-3 UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005885
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-arp2-3-native-verify
- check_id: arp2-3-uniprot-causal
  name: Native arp2-3 UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005885
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-arp2-3-native-causal
- check_id: aster-uniprot-verify
  name: Native aster UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0005818
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/aster.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-s2352-aster-native-verify
- check_id: aster-uniprot-causal
  name: Native aster UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0005818
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/aster.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-s2352-aster-native-causal
- check_id: astral-uniprot-verify
  name: Native astral UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0000235
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-s2352-astral-native-verify
- check_id: astral-uniprot-causal
  name: Native astral UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0000235
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/astral_microtubule.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero; exact inventory and any NO_GENE_SYMBOLS
    limits remain in evidence. Deterministic coverage does not resolve scientific
    findings or assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-s2352-astral-native-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/appendage/9_2_motile_cilium.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97;
    current SHA256 c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97.
    Record bytes unchanged since the original review.
  snapshot_sha256: c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T094726Z-9-2-motile-cilium-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: a275f7cecebd6a709b7f793b6f5fe9de364e1969def47153c0ccd7050ab9c16e
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/appendage/ciliary_base.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb;
    current SHA256 fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb.
    Record bytes unchanged since the original review.
  snapshot_sha256: fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T094729Z-ciliary-base-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 92eb253a5df08a79a6b8e450b592163e870f6ceccce8af550e18a94c64593ec8
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/appendage/germ_tube.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058;
    current SHA256 b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058.
    Record bytes unchanged since the original review.
  snapshot_sha256: b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T094732Z-germ-tube-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 9b1de100d315882fe532d2ea80007a5bacc138c156a3504b26ae190814fcd466
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/appendage/longitudinal_flagellum.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac;
    current SHA256 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac.
    Record bytes unchanged since the original review.
  snapshot_sha256: 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T094735Z-longitudinal-flagellum-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 31f8ba103fd349f2369b0b1cc24dd04de5031b0d8fcf96a28707ddd51a97dcb4
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/appendage/motile_cilium.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e;
    current SHA256 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e.
    Record bytes unchanged since the original review.
  snapshot_sha256: 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T094737Z-motile-cilium-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 4df9df67ffbd6e8e6e36f1ffdd682bba7143f6041f7989905b0f9c83b9be4edb
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/appendage/transverse_flagellum.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c;
    current SHA256 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c.
    Record bytes unchanged since the original review.
  snapshot_sha256: 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T094739Z-transverse-flagellum-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 81af91da6e5ced84e1cddc4fe8ce5c7ed16379ebcf8f5572b02978467123011a
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 a612b062735844ba209722df0054d084db27ef18e8a243dc32d6d180303fd44b;
    current SHA256 05b7cc75eaf5f65fb7a4839055dcd086303a6c26cf1fb781ad41baf541bd8ecc.
    Changed record reassessed against current sources.
  snapshot_sha256: 05b7cc75eaf5f65fb7a4839055dcd086303a6c26cf1fb781ad41baf541bd8ecc
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T094741Z-arp2-3-protein-complex-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b1c7a26ce89e3baa54504df6a45936b1c947c903e45c02e8126986f9c563d738
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/cytoskeleton/aster.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 ed329cc165c49478a9cad71b9a56809631bed2891dd09a46d8a4cce1523f3ae7;
    current SHA256 ead65813443a3277dee3611ec40e32b7bc4c3882d8c31508eb352f6fffdfd6df.
    Changed record reassessed against current sources.
  snapshot_sha256: ead65813443a3277dee3611ec40e32b7bc4c3882d8c31508eb352f6fffdfd6df
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T094744Z-aster-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 70176bbd52c783ecc051375714e2cabfe3dafa4c9402fe5fcea4abc84bd4eabc
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/cytoskeleton/astral_microtubule.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 7c5c19cbf7cc39406dcc7d8bf376e4fcff12dcf7c71f702cf8058e766138be1f;
    current SHA256 45c1ec56a960d58bde433d88317824b726ff48473bc9b0b1d4429c6e2f57041d.
    Changed record reassessed against current sources.
  snapshot_sha256: 45c1ec56a960d58bde433d88317824b726ff48473bc9b0b1d4429c6e2f57041d
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T094746Z-astral-microtubule-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 8d018e970882cbbf4cc3a1d094620808c31bdfc1e2caa70de6043e174935a61e
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Original frozen SHA256 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4;
    current SHA256 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4.
    Record bytes unchanged since the original review.
  snapshot_sha256: 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T094748Z-ciliary-pro-basal-body-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T05:51:22Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: d9438d264e1f900eec1e755c2a07e6f90977e5143395bf0b244701e02a24cf42
- evidence_id: plaque-germ-tube-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032159,GO:0032171,GO:0032172,GO:0032179,GO:0110165
  locator: All requested term identities, active status, definitions and relationship
    metadata
  accessed_at: '2026-11-03T05:41:18.464682Z'
  snapshot_sha256: 3a8a62b46c3347b6fe19861d5cf540a1e2a0e723936134b8c9e9dbe7671a8436
  summary: Current nonobsolete native terms [('GO:0110165', 'cellular anatomical structure'),
    ('GO:0032171', 'germ tube septin cap'), ('GO:0032172', 'germ tube septin ring'),
    ('GO:0032159', 'septin cap'), ('GO:0032179', 'germ tube')]. Exact structure identity
    and narrower location/function terms were checked.
  support: supports
- evidence_id: plaque-germ-tube-agent-epmc
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1128/EC.4.9.1503-1512.2005%22&format=json&resultType=core&pageSize=100
  locator: Publication title, authors, DOI/PMID, publication type and available abstract
  accessed_at: '2026-11-03T05:41:18.465868Z'
  snapshot_sha256: 7d84659cec4ab1c3465ec6a67f4636f1d0380f7f42bda7228f67c00696c2100a
  summary: Fresh metadata identifies Septin function in yeast model systems and pathogenic
    fungi.; Douglas2005 is secondary review evidence, not an independent three-species
    mechanistic experiment.
  support: supports
- evidence_id: plaque-germ-tube-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: Fresh native PMC HTML; Septins in C.albicans subsection, including three
    localization patterns
  accessed_at: '2026-11-03T05:41:18.467051Z'
  snapshot_sha256: e49473431becca5eac54c61c452f544a949a2e81b4334706afa36020302610c2
  summary: The secondary review separates a cytokinetic ring within the tube, a diffuse
    basal band and a faint cap at the growing tip. This supports anatomical distinction
    and source-scoped localization, not a universal fungal germination dependence.
  support: supports
- evidence_id: plaque-germ-tube-agent-warenda2002
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC117938/?pdf=render
  locator: Fresh native PMC HTML returned by pdf=render URL; Abstract; Methods strains/media
    and microscopy; claim-bearing localization paragraphs and hyphal-mutant Results;
    Figures2/7/8 captions; hyphal Discussion
  accessed_at: '2026-11-03T05:41:18.468373Z'
  snapshot_sha256: e649a1b11dad56cb7cad3bd8f7f5da65b0ca19082e53eb43c45d7c5714637a2f
  summary: Candida BWP17-derived strains show diffuse germ-tube septins, tip signal
    and later septal rings. Individual cdc10/cdc11 deletions retain other septins
    and alter morphogenesis without abolishing all serum-induced growth. They are
    not complete generic-class ablations.
  support: supports
- evidence_id: plaque-germ-tube-agent-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: IPR016491 metadata.type/name and non-LLM description
  accessed_at: '2026-11-03T05:41:18.867195Z'
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
  summary: IPR016491 is the generic Septin protein family. This exact class identity
    does not specify every member or stoichiometry of a germ-tube cap.
  support: supports
- evidence_id: plaque-arp-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0005885,GO:0015629,GO:0030479,GO:0030864,GO:0032991,GO:0061645
  locator: All requested term identities, active status, definitions and relationship
    metadata
  accessed_at: '2026-11-03T05:41:18.891812Z'
  snapshot_sha256: 52609f09b91414176bd0802335b29604b8cea985ab53da1e1aa84198c85a1fa5
  summary: Current nonobsolete native terms [('GO:0030479', 'actin cortical patch'),
    ('GO:0005885', 'Arp2/3 protein complex'), ('GO:0030864', 'cortical actin cytoskeleton'),
    ('GO:0015629', 'actin cytoskeleton'), ('GO:0032991', 'protein-containing complex'),
    ('GO:0000147', 'actin cortical patch assembly'), ('GO:0061645', 'endocytic patch')].
    Exact structure identity and narrower location/function terms were checked.
  support: supports
- evidence_id: plaque-arp-agent-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:41:19.079746Z'
  snapshot_sha256: 38f43dd1593a1d47416228ae385464f30aeb8302c3aadb45b3588d03744bc814
  summary: Native taxonomy distinguishes species4932 from S288C reference-strain559292.
    Reference sequence identifiers are not exact-stock microscopy assertions.
  support: supports
- evidence_id: plaque-arp-agent-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: taxId, scientificName and lineage
  accessed_at: '2026-11-03T05:41:19.126977Z'
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  summary: Native taxonomy distinguishes species4932 from S288C reference-strain559292.
    Reference sequence identifiers are not exact-stock microscopy assertions.
  support: supports
- evidence_id: plaque-arp-agent-P32381
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32381.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:19.518037Z'
  snapshot_sha256: 2b378f480e51da72d42b3b9dce10343e882ecd765163079ebba5dee3a2597bf9
  summary: 'Native reviewed P32381: ARP2, Actin-related protein 2, taxon559292. Function
    comments often use similarity evidence; those do not replace direct cited-paper
    support. Reference membership text uses historical ARC16/p16 naming; this entry’s
    exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARP2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARP2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:19.545272Z'
  snapshot_sha256: dfebbdfdb0fb815de18cf04958a76825298435a28c2b14fb2f4d644fbf8cba8a
  summary: Native exact query resolves [('P32381', 'ARP2', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARP2) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:19.545272Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-P47117
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47117.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:19.777441Z'
  snapshot_sha256: c1fb00ae697516d543e044536958483b7e17ee1660700e869689adb336de7b71
  summary: 'Native reviewed P47117: ARP3, Actin-related protein 3, taxon559292. Function
    comments often use similarity evidence; those do not replace direct cited-paper
    support. Reference membership text uses historical ARC16/p16 naming; this entry’s
    exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:19.843593Z'
  snapshot_sha256: 2fd3bf9551a26771c0fa16bbc3e318de130696bc94b2f4760fc8e138bf421e61
  summary: Native exact query resolves [('P47117', 'ARP3', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARP3) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:19.843593Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-P53731
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53731.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:20.968520Z'
  snapshot_sha256: 7c903010adc7254a171b89a0cf935052237882f9599de322c36116a29640f2ad
  summary: 'Native reviewed P53731: ARC35, Actin-related protein 2/3 complex subunit
    2, taxon559292. Function comments often use similarity evidence; those do not
    replace direct cited-paper support. Reference membership text uses historical
    ARC16/p16 naming; this entry’s exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARC35
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC35%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:21.816032Z'
  snapshot_sha256: 6cfa62fe3454446fd9c97d4e8ab4b2b8a26222347f367e0f602cf9257c9cb995
  summary: Native exact query resolves [('P53731', 'ARC35', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC35) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:21.816032Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-P33204
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33204.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:21.992303Z'
  snapshot_sha256: 6a510fff14b0f9054f847c6ad26e13dfc29e391b6c173a27dc6410b509bf7000
  summary: 'Native reviewed P33204: ARC19, Actin-related protein 2/3 complex subunit
    4, taxon559292. Function comments often use similarity evidence; those do not
    replace direct cited-paper support. Reference membership text uses historical
    ARC16/p16 naming; this entry’s exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARC19
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC19%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:22.780672Z'
  snapshot_sha256: 1a847c87c46f70cfa1ce9a557d5e37332a3594ef1168d73e6de42081e4fe8c66
  summary: Native exact query resolves [('P33204', 'ARC19', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC19) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:22.780672Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-P38328
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38328.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:23.779191Z'
  snapshot_sha256: cb2cf7eba6e89e1c6e9a26a6cab12515382eff955ca37f302d7762c99853a6eb
  summary: 'Native reviewed P38328: ARC40, Actin-related protein 2/3 complex subunit
    1, taxon559292. Function comments often use similarity evidence; those do not
    replace direct cited-paper support. Reference membership text uses historical
    ARC16/p16 naming; this entry’s exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARC40
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC40%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:24.828480Z'
  snapshot_sha256: 42f2915f586bbecd94d03031300dd449208983f62bc6db4d9af39e1d3c977873
  summary: Native exact query resolves [('P38328', 'ARC40', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC40) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:24.828480Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-Q05933
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q05933.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:24.975986Z'
  snapshot_sha256: a0f9700443c987dd59d04c81980287273147117d9c570aa6e3cafdb62636eb51
  summary: 'Native reviewed Q05933: ARC18, Actin-related protein 2/3 complex subunit
    3, taxon559292. Function comments often use similarity evidence; those do not
    replace direct cited-paper support. Reference membership text uses historical
    ARC16/p16 naming; this entry’s exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARC18
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC18%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:25.754170Z'
  snapshot_sha256: f8ea6b20283807a786443913a74fe80a7023003e5e2608a2c103baa8f7fc535a
  summary: Native exact query resolves [('Q05933', 'ARC18', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC18) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:25.754170Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-P40518
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40518.json
  locator: Reviewed primary accession, organism, genes, recommended protein name,
    SUBUNIT/FUNCTION/location comments, evidence qualifiers and InterPro cross-references
  accessed_at: '2026-11-03T05:41:25.786391Z'
  snapshot_sha256: f6a13b306d4e1740fa932240cf28d5ab9ef710a923167a97c1442d240b3014f2
  summary: 'Native reviewed P40518: ARC15, Actin-related protein 2/3 complex subunit
    5, taxon559292. Function comments often use similarity evidence; those do not
    replace direct cited-paper support. Reference membership text uses historical
    ARC16/p16 naming; this entry’s exact gene is preserved.'
  support: supports
- evidence_id: plaque-arp-agent-query-ARC15
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC15%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned exact gene/reviewed/taxon results
  accessed_at: '2026-11-03T05:41:26.745832Z'
  snapshot_sha256: 75eaaf64f0a1c5a0496ac86ba4e1965a492f606002cc2481475fc5b829c66aa4
  summary: Native exact query resolves [('P40518', 'ARC15', 559292)]. This verifies
    accession mapping, not experimental localization or mechanism.
  search_scope: UniProt REST; format=json&query=(gene_exact:ARC15) AND (organism_id:559292)
    AND (reviewed:true); accessed 2026-11-03T05:41:26.745832Z; only this exact query,
    all returned results inspected.
  support: supports
- evidence_id: plaque-arp-agent-kaksonen2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:14622601%20AND%20SRC:MED
  locator: Exact Europe PMC bibliographic fields and abstract
  accessed_at: '2026-11-03T05:41:27.839193Z'
  snapshot_sha256: 231ebac644f0b6710d7390920df5d22ca887f86426188e1fd407d7e98dae6510
  summary: Fresh metadata/abstract identifies A pathway for association of receptors,
    adaptors, and actin during endocytic internalization.. Full-body inspection is
    only claimed for separately identified article-body evidence.
  support: supports
- evidence_id: plaque-arp-agent-doi-jcb.200404159
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200404159
  locator: Exact Europe PMC bibliographic fields and abstract
  accessed_at: '2026-11-03T05:41:27.877275Z'
  snapshot_sha256: 678b444097b37f9988960c614b68996c30f44d37289bcd050157421186ca3097
  summary: Fresh metadata/abstract identifies Yeast actin patches are networks of
    branched actin filaments.. Full-body inspection is only claimed for separately
    identified article-body evidence.
  support: supports
- evidence_id: plaque-arp-agent-doi-journal.pbio.0060001
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.0060001
  locator: Exact Europe PMC bibliographic fields and abstract
  accessed_at: '2026-11-03T05:41:28.479399Z'
  snapshot_sha256: ac7737e4a85ce68ea155e71e279b4cb05d0945a25d329982a6f7bd47c3927e15
  summary: Fresh metadata/abstract identifies Distinct roles for Arp2/3 regulators
    in actin assembly and endocytosis.. Full-body inspection is only claimed for separately
    identified article-body evidence.
  support: supports
- evidence_id: plaque-arp-agent-doi-mbc.E06-04-0282
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E06-04-0282
  locator: Exact Europe PMC bibliographic fields and abstract
  accessed_at: '2026-11-03T05:41:28.538037Z'
  snapshot_sha256: 7721d53295c55feca2fe04b4a12bea6463a2cc271fd0360986b784b3e31c346a
  summary: 'Fresh metadata/abstract identifies Actin bodies in yeast quiescent cells:
    an immediately available actin reserve?. Full-body inspection is only claimed
    for separately identified article-body evidence.'
  support: supports
- evidence_id: plaque-arp-agent-pmid-9210376
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9210376%20AND%20SRC%3AMED
  locator: Exact Europe PMC bibliographic fields and abstract
  accessed_at: '2026-11-03T05:41:28.752943Z'
  snapshot_sha256: 8c00acf3fa71f64c1bfe2155e0e17151cd881e3ecf51de2c4910d4cdc123baf8
  summary: Fresh metadata/abstract identifies The complex containing actin-related
    proteins Arp2 and Arp3 is required for the motility and integrity of yeast actin
    patches.. Full-body inspection is only claimed for separately identified article-body
    evidence.
  support: supports
- evidence_id: plaque-arp-agent-jats-jcb.200404159
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2172413.1/PMC2172413.1.xml
  locator: Fresh native PMC JATS; complete Introduction, Results/Discussion and Materials/Methods;
    all main captions and TableI
  accessed_at: '2026-11-03T05:41:28.923782Z'
  snapshot_sha256: 7f6584b83df46499ba5c7e041436bf04a67115725fd90c8470d8c5982e073bf4
  summary: Young2004 examines partially purified cortical patches, filament branches
    and sac6/cap1 mutants. Branch geometry agrees with Arp2/3-mediated nucleation;
    it does not determine the Arc35/Arc19 clamp or individual Arc40/Arc18/Arc15 activation
    coupling stated in the record.
  support: supports
- evidence_id: plaque-arp-agent-galletta2008-plos
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060001
  locator: Fresh publisher HTML; Introduction, first Las17 acidic-domain Results and
    Figures1/2 captions, relevant Discussion passages, main Materials/Methods
  accessed_at: '2026-11-03T05:41:29.191803Z'
  snapshot_sha256: 0cdca43d2b1c72883876e77eadbe2a11f872e4a05f8e29aa60ea7d91dd4ac3bc
  summary: The experiments track regulator mutations and patch assembly/movement in
    yeast. Distinct and overlapping activator roles are supported; targeting versus
    activation and tagged-Las17 limitations remain explicit. No raw movies or complete
    other-regulator Results audit is claimed.
  support: supports
- evidence_id: plaque-arp-agent-sagot2006-browser
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1635378/
  locator: Fresh native PMC HTML (not cached browser excerpt); Methods strains/media/microscopy;
    Results Several Actin-binding Proteins Colocalize with Actin Bodies and Figure3
    caption
  accessed_at: '2026-11-03T05:41:29.282795Z'
  snapshot_sha256: 2bb9aba0dd0163250d4e491f22b5bab45da4409279ceca00a54b373dbbde6965
  summary: The full native page is now accessible. Inspected sections report partial
    colocalization of Arc15,Arc18,Arc35,Arp2 with quiescent-cell actin bodies in a29-protein
    screen. This supports the carefully limited example notes, not a whole-complex
    occupancy census. Other body sections and supplementary data were not audited.
  support: supports
- evidence_id: plaque-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned public catalogue,20 organism entries and28 dataset keys
  accessed_at: '2026-11-03T05:41:29.300510Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  summary: No Saccharomyces,Candida,Aspergillus,Neurospora or other eukaryotic dataset
    occurs in this bounded current catalogue. Germ-tube molecular polarity/septin
    claims and Arp named yeast proteins therefore have no matching downstream iModulonDB
    query. Absence is database coverage, not negative biological evidence.
  support: supports
- evidence_id: plaque-current-0
  kind: record_content
  reference: data/structures/appendage/germ_tube.yaml
  locator: Entire current maintained YAML including graph and history
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: b238d9290ea6c71027cd0c398db6954baa769ad167812dd404a3c9fae4c0c058
  summary: Current full record read and compared with historical input; unchanged
    record reassessed against fresh sources.
  support: supports
- evidence_id: plaque-original-0
  kind: prior_review
  reference: reviews/structured/20261021T094732Z-germ-tube-audit/review.yaml
  locator: Full original review including findings/actions/source scopes
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: 9b1de100d315882fe532d2ea80007a5bacc138c156a3504b26ae190814fcd466
  summary: Historical observation preserved. Native validation/render and historical
    frozen input hashes pass; prior scientific findings are independently reassessed.
  support: supports
- evidence_id: plaque-current-1
  kind: record_content
  reference: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  locator: Entire current maintained YAML including graph and history
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: 05b7cc75eaf5f65fb7a4839055dcd086303a6c26cf1fb781ad41baf541bd8ecc
  summary: Current full record read and compared with historical input; stale changed
    types substantively reassessed.
  support: supports
- evidence_id: plaque-original-1
  kind: prior_review
  reference: reviews/structured/20261021T094741Z-arp2-3-protein-complex-audit/review.yaml
  locator: Full original review including findings/actions/source scopes
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: b1c7a26ce89e3baa54504df6a45936b1c947c903e45c02e8126986f9c563d738
  summary: Historical observation preserved. Native validation/render and historical
    frozen input hashes pass; prior scientific findings are independently reassessed.
  support: supports
- evidence_id: plaque-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: ComponentTypeEnum,GraphKindEnum,CausalGraphScopeEnum and essentiality definitions
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  summary: PROTEIN denotes a family/paralogue group; PROTEIN_COMPLEX denotes a named
    subcomplex. ASSEMBLY describes how a structure is built; membership alone does
    not provide assembly mechanism.
  support: supports
- evidence_id: plaque-graph-contract
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Native graph source/scope contract
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
  summary: Require supported causal/assembly paths and keep membership separate from
    mechanism.
  support: supports
- evidence_id: plaque-adapter-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  summary: Molecular triggers require actual applicability assessment; source fallback
    is allowed when the runner is unavailable.
  support: supports
- evidence_id: plaque-protein-policy
  kind: authority
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: NO_GENE_SYMBOLS and generic-class exception
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
  summary: Generic protein classes may remain without invented species-specific genes/examples;
    named heteromeric groups require checking declared symbols.
  support: supports
- evidence_id: plaque-arp-category-0
  kind: prior_review
  reference: reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml
  locator: F1 exact Arp2/3 component-type fields and multi-target finding scope
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: ffd4b4cf845f8a4ec0d7806c62152b0e92be5620b6a1373a9e7b292349474def
  summary: The predecessor covers seven records. Current Arp2/3 fields are corrected,
    but this subreview does not reassess every predecessor target and does not make
    a terminal whole-finding disposition.
  support: supports
- evidence_id: plaque-arp-category-1
  kind: prior_review
  reference: reviews/structured/20261025T071004Z-cytoskeleton-category-review/review.yaml
  locator: F1 exact Arp2/3 component-type fields and multi-target finding scope
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: d34740ab1423ae3417a5a7ba665d7141ddfea865663a44c75aedfbc77b91d2a4
  summary: The predecessor covers two records. Current Arp2/3 fields are corrected,
    but this subreview does not reassess every predecessor target and does not make
    a terminal whole-finding disposition.
  support: supports
- evidence_id: plaque-issue-2420
  kind: database
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2420
  locator: Root-fetched issue body and CLOSED state, independently reread; SHA binds
    captured JSON
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: c88c1c00a6410342718f46bb1c138a2b4c035e8f3159498cd1553db9fd248b50
  summary: Historical grouped record repair issue is already closed and explicitly
    includes the relevant Arp2/3 type correction. No record fix is attributed to PR2352.
  support: supports
- evidence_id: plaque-issue-2431
  kind: database
  reference: https://github.com/CultureBotAI/CellStructureMech/issues/2431
  locator: Root-fetched issue body and CLOSED state, independently reread; SHA binds
    captured JSON
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: e8b470767273a650e8147a42bfa781dc0574b99dc029b2f6bd407248dfce1d38
  summary: Historical grouped record repair issue is already closed and explicitly
    includes the relevant Arp2/3 type correction. No record fix is attributed to PR2352.
  support: supports
- evidence_id: plaque-original-validation
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/adversary-plaque/original-validation.json
  locator: Two original native validates/renders and historical input hashes
  accessed_at: '2026-11-03T05:44:53.270042Z'
  snapshot_sha256: 08e78530c1550522db7320a560def5c3ebcd74773f1ff2e0e9cb41c96ec4fce6
  summary: Both originals validate and render byte-identically; all14/13 historical
    source inputs match their declared Git revision.
  support: supports
- evidence_id: plaque-germ-tube-native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/germ-tube-uniprot-verify-receipt.json
  locator: Complete receipt plus log stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T05:42:02.928209Z'
  snapshot_sha256: eefcd7243ab9439f2da384819bb7b24808e3a04b500e4b2eb6f67fd811d2bbf8
  summary: Root-executed native command passed at source head; this reviewer independently
    read the receipt/log and verified stdout hash. Existing UniProt examples/xrefs
    validate; empty germ-tube example inventory is not positive molecular coverage.
  support: supports
- evidence_id: plaque-germ-tube-native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/germ-tube-uniprot-causal-receipt.json
  locator: Complete receipt plus log stdout SHA256 b6822abc52c170ca6071fcc71dc3f3492257d585e43f5b9f69d69f689b54e063
  accessed_at: '2026-11-03T05:42:03.352864Z'
  snapshot_sha256: ab1017deed40c28f7fcb751f3636a69888a41db6da4d7af551923f94d1c4c81b
  summary: Root-executed native command passed at source head; this reviewer independently
    read the receipt/log and verified stdout hash. Germ tube reports one NO_GENE_SYMBOLS
    and zero COVERED; generic class scope retained.
  support: supports
- evidence_id: plaque-arp2-3-native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/arp2-3-uniprot-verify-receipt.json
  locator: Complete receipt plus log stdout SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T05:42:04.697159Z'
  snapshot_sha256: 1cfaef765d31fc3069fef21f39e5b54e9d99cfc75627498969916e44c261dc9e
  summary: Root-executed native command passed at source head; this reviewer independently
    read the receipt/log and verified stdout hash. Existing UniProt examples/xrefs
    validate; empty germ-tube example inventory is not positive molecular coverage.
  support: supports
- evidence_id: plaque-arp2-3-native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/arp2-3-uniprot-causal-receipt.json
  locator: Complete receipt plus log stdout SHA256 3ee1f7c6d9fefa540b329cd2e05709cc0e2459a9ab0e66c0ee6415f63ff6f88c
  accessed_at: '2026-11-03T05:42:05.131801Z'
  snapshot_sha256: 5bd396dbde47ed48d61ab32307e978ae4963cf503e1d78a3f0832d29fb6fb696
  summary: Root-executed native command passed at source head; this reviewer independently
    read the receipt/log and verified stdout hash. Arp2/3 reports three COVERED component-ref
    nodes and zero other diagnostic categories; this is declared-symbol coverage,
    not mechanism/necessity proof.
  support: supports
- evidence_id: micro-record-nine-two
  kind: record_content
  reference: data/structures/appendage/9_2_motile_cilium.yaml
  locator: 'Entire maintained YAML: definition, hierarchy, all components/examples,
    taxa, functions, evidence, every graph node/edge and history.'
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Complete current target independently assessed. Current source/HEAD and
    historical source target bytes match the original frozen hash; status remains
    PROPOSED. No image, quantitative measurement or verbatim snippet is asserted.
  support: context_only
  snapshot_sha256: c467662c221310d77633097ef15f370573c5bec1c5964ac78f85ffb7e38eca97
- evidence_id: micro-prior-nine-two
  kind: prior_review
  reference: reviews/structured/20261021T094726Z-9-2-motile-cilium-audit/review.yaml
  locator: Entire authoritative YAML; all assessments/findings/actions/checks/limitations;
    native-rendered Markdown compared byte-for-byte.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Original needs_curation verdict and two exact findings remain historical
    observations. Source-specific limitations and old validator totals are not represented
    as current results.
  support: context_only
  snapshot_sha256: a275f7cecebd6a709b7f793b6f5fe9de364e1969def47153c0ccd7050ab9c16e
- evidence_id: micro-record-base
  kind: record_content
  reference: data/structures/appendage/ciliary_base.yaml
  locator: 'Entire maintained YAML: definition, hierarchy, all components/examples,
    taxa, functions, evidence, every graph node/edge and history.'
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Complete current target independently assessed. Current source/HEAD and
    historical source target bytes match the original frozen hash; status remains
    PROPOSED. No image, quantitative measurement or verbatim snippet is asserted.
  support: context_only
  snapshot_sha256: fce7c8f9b88ff6aeca1d3fcde92b8e97fc59d5613749df0e92dc14561aeb4ddb
- evidence_id: micro-prior-base
  kind: prior_review
  reference: reviews/structured/20261021T094729Z-ciliary-base-audit/review.yaml
  locator: Entire authoritative YAML; all assessments/findings/actions/checks/limitations;
    native-rendered Markdown compared byte-for-byte.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Original needs_curation verdict and two exact findings remain historical
    observations. Source-specific limitations and old validator totals are not represented
    as current results.
  support: context_only
  snapshot_sha256: 92eb253a5df08a79a6b8e450b592163e870f6ceccce8af550e18a94c64593ec8
- evidence_id: micro-record-motile
  kind: record_content
  reference: data/structures/appendage/motile_cilium.yaml
  locator: 'Entire maintained YAML: definition, hierarchy, all components/examples,
    taxa, functions, evidence, every graph node/edge and history.'
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Complete current target independently assessed. Current source/HEAD and
    historical source target bytes match the original frozen hash; status remains
    PROPOSED. No image, quantitative measurement or verbatim snippet is asserted.
  support: context_only
  snapshot_sha256: 4c6689b83a38d84b34e3775c18d0b7e6706e6c069e37790c8549db6f14729e1e
- evidence_id: micro-prior-motile
  kind: prior_review
  reference: reviews/structured/20261021T094737Z-motile-cilium-audit/review.yaml
  locator: Entire authoritative YAML; all assessments/findings/actions/checks/limitations;
    native-rendered Markdown compared byte-for-byte.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Original needs_curation verdict and two exact findings remain historical
    observations. Source-specific limitations and old validator totals are not represented
    as current results.
  support: context_only
  snapshot_sha256: 4df9df67ffbd6e8e6e36f1ffdd682bba7143f6041f7989905b0f9c83b9be4edb
- evidence_id: micro-record-probasal
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
  locator: 'Entire maintained YAML: definition, hierarchy, all components/examples,
    taxa, functions, evidence, every graph node/edge and history.'
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Complete current target independently assessed. Current source/HEAD and
    historical source target bytes match the original frozen hash; status remains
    PROPOSED. No image, quantitative measurement or verbatim snippet is asserted.
  support: context_only
  snapshot_sha256: 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4
- evidence_id: micro-prior-probasal
  kind: prior_review
  reference: reviews/structured/20261021T094748Z-ciliary-pro-basal-body-audit/review.yaml
  locator: Entire authoritative YAML; all assessments/findings/actions/checks/limitations;
    native-rendered Markdown compared byte-for-byte.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Original needs_curation verdict and two exact findings remain historical
    observations. Source-specific limitations and old validator totals are not represented
    as current results.
  support: context_only
  snapshot_sha256: d9438d264e1f900eec1e755c2a07e6f90977e5143395bf0b244701e02a24cf42
- evidence_id: micro-review-policy
  kind: record_content
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Structured Source Cross-Checks; Workflow.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Named IFT, CEP290/NPHP4 and SAS6/Bld10 trigger structured-source applicability
    even without an expression-module assertion. Source tiers, exact scopes and stable
    lineage must be retained.
  support: context_only
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: micro-graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Source, node/edge, scope and completion requirements; add-cell-structure
    contract read.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Static membership and generic outputs do not themselves establish a mechanism.
    Primary evidence must support directed causal events.
  support: context_only
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: micro-schema-policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent essentiality and roles; CausalGraph/GraphKindEnum/CausalGraphScopeEnum.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Essentiality means whether the structure forms without a component. FUNCTION
    explains how it does its job; NONMECHANISTIC and REVIEW_NEEDED are legal scope
    values.
  support: context_only
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: micro-protein-policy
  kind: record_content
  reference: .claude/skills/uniprot-protein-examples/SKILL.md
  locator: Rules 1–5 and read-only verify/causal-graph workflow.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Check primary accession, exact native token/status/taxon, published locus
    bridge where needed and location-specific experimental annotations. Structural
    assemblies are not individual protein families.
  support: context_only
  snapshot_sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
- evidence_id: micro-config
  kind: record_content
  reference: conf/record_review.yaml
  locator: Complete active skill and rubric routing.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Configuration was frozen by root before this slice; the active review route
    and rubrics were reread.
  support: context_only
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
- evidence_id: micro-mastigoneme-context
  kind: record_content
  reference: data/structures/appendage/mastigoneme.yaml
  locator: Entire neighbor read for identity/modeling context only after root froze
    it.
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: Neighbor separately models bounded Chlamydomonas mastigoneme evidence and
    unresolved broader scope. Its statements are contextual, not an independently
    reviewed fifth target or proof of universal motile-cilium membership.
  support: context_only
  snapshot_sha256: d494a06dcfd0686ab910c8ae88a4899c1f5dd58634339194d24c4dac64d3fbd1
- evidence_id: micro-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005815,GO:0005874,GO:0005929,GO:0005930,GO:0030990,GO:0031514,GO:0035869,GO:0036064,GO:0060170,GO:0060271,GO:0060285,GO:0097537,GO:0097546,GO:0097729,GO:0097740,GO:0097741,GO:0110165,GO:0120280
  locator: All 18 active result id/name/definition/synonym/children/relation fields.
  accessed_at: '2026-11-03T05:43:10.461041Z'
  summary: 'Exact identities and hierarchy agree: 9+2 is a motile-cilium subtype;
    base belongs to cilium and includes distal basal body, transition fibers and TZ;
    Y-link is a TZ complex. PFR is limited to some flagellated protists; mastigonemes
    to some algae. Inverse child part_of listings do not establish obligatory broad-class
    has_part. GO0120280 explicitly cannot nucleate a cilium until mature; GO0036064
    describes the mature nucleating body.'
  support: supports
  snapshot_sha256: dba356a314f5e07827475b796068d4dc3f1467731ce4f659ff24135a3488f179
- evidence_id: micro-tax3055
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: taxId/scientificName/rank/lineage.
  accessed_at: '2026-11-03T05:43:10.461980Z'
  summary: Taxon3055 is Chlamydomonas reinhardtii; this verifies identity, not prevalence
    at every life-cycle stage.
  support: supports
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: micro-uniprot-Q5DM57
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q5DM57.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:10.462254Z'
  summary: Reviewed IFT172/FLA11 at taxon3055; experimental basal-body location cites
    PMID17326139 and9585417. Peribasal primary evidence is not proof of permanent
    basal-body incorporation.
  support: supports
  snapshot_sha256: 81d0a74e5bda18c90d8bc7a12d6abdcfbb0219f5829ae8bdf58bd9eb6d125b1c
- evidence_id: micro-uniprot-Q68RJ5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q68RJ5.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:10.462662Z'
  summary: Reviewed IFT81 at taxon3055; its cilium location is ECO0000305, so the
    record correctly uses identity-only evidence.
  support: supports
  snapshot_sha256: d200c715553d94a8e16d56f2aab24412a810c125e11f1153c68095486cd9153c
- evidence_id: micro-uniprot-Q6RCE1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6RCE1.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:10.462907Z'
  summary: Reviewed IFT74 with IFT71 and IFT74/72 aliases at taxon3055; location ECO0000305
    is not imported as experimental evidence.
  support: supports
  snapshot_sha256: d392121fd9271634adef9cc3a4b4309205c022bef3ae3efe733ac90b5cf64bf9
- evidence_id: micro-uniprot-A2T2X4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A2T2X4.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:10.463098Z'
  summary: Reviewed IFT46/FAP32 at taxon3055; experimental basal-body/cilium localization
    annotations include PMID15955805,17312020,18852297. These are location-specific
    annotations, distinct from full primary experiment review.
  support: supports
  snapshot_sha256: 9da98899eae02d8a3c974a888104e0e89a3f1b7f6468b130c60fd6e59a9db19e
- evidence_id: micro-uniprot-Q9FPW0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q9FPW0.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:11.133472Z'
  summary: Unreviewed IFT88 at taxon3055; exact submitted label and gene token agree;
    no location comment supports an experimental localization assertion.
  support: supports
  snapshot_sha256: 2317af7a1a68536f1c6ca22036f78420bb40ae73394e48d681b1edc7ee1a6f82
- evidence_id: micro-uniprot-A0A2K3DWT6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2K3DWT6.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:11.234037Z'
  summary: Unreviewed exact Cep290-domain label and CHLRE_03g167550v5 ORF at taxon3055.
    Automatic ARBA location is not experimental evidence; literature mapping is checked
    separately.
  support: supports
  snapshot_sha256: 2e8f6214c08ae3f786a8184d814b6051335991d83e2d80d7c2a0081942e0fd49
- evidence_id: micro-uniprot-A0A2K3D4W1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2K3D4W1.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; SUBCELLULAR
    LOCATION and ECO/PubMed attribution where present.
  accessed_at: '2026-11-03T05:43:11.417345Z'
  summary: Unreviewed Nephrocystin-4 label and CHLRE_12g531400v5 ORF at taxon3055;
    no location comment. The current recommended name is inferred by ProtNLM, not
    new experimental evidence.
  support: supports
  snapshot_sha256: 16666df8d22774e12fe41876dd64b8922335b09df8275a3adaf57c1601b4ace7
- evidence_id: micro-ift-reviewed-search
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AIFT172%20OR%20gene_exact%3AIFT81%20OR%20gene_exact%3AIFT74%20OR%20gene_exact%3AIFT46%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&format=json&size=100
  locator: All four result accessions and their own gene tokens; response total and
    pagination headers.
  accessed_at: '2026-11-03T05:43:13.784427Z'
  summary: 'One reviewed native match each: IFT172 Q5DM57, IFT81 Q68RJ5, IFT74 Q6RCE1,
    IFT46 A2T2X4; no ambiguity within this bounded query.'
  support: supports
  snapshot_sha256: 240c126103910e1e296caa2b223dca221e81b893bc4d435ea5ae0f6ebd0b60fa
  search_scope: 'UniProtKB REST searched 2026-11-03: (gene_exact:IFT172 OR gene_exact:IFT81
    OR gene_exact:IFT74 OR gene_exact:IFT46) AND organism_id:3055 AND reviewed:true,
    JSON size100. Four returned entries inspected; no next page. Other aliases/species
    and IFT52 were not searched. Remote query; local ignored-file scope not applicable.'
- evidence_id: micro-base-reviewed-search
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACEP290%20OR%20gene_exact%3ANPHP4%29%20AND%20organism_id%3A3055%20AND%20reviewed%3Atrue&format=json&size=100
  locator: Complete empty results array; response headers.
  accessed_at: '2026-11-03T05:43:13.672444Z'
  summary: Zero reviewed entries for these exact symbols in taxon3055. This does not
    establish absence under every alternate name.
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: 'UniProtKB REST searched 2026-11-03: (gene_exact:CEP290 OR gene_exact:NPHP4)
    AND organism_id:3055 AND reviewed:true, JSON size100; zero entries, no next page.
    Other aliases/species were not searched; no local absence claim.'
- evidence_id: micro-ift88-reviewed-search
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AIFT88+AND+organism_id%3A3055+AND+reviewed%3Atrue&format=json&size=100
  locator: Complete empty results array; response headers.
  accessed_at: '2026-11-03T05:45:50.664091Z'
  summary: Zero reviewed IFT88 exact-gene matches at taxon3055 in this bounded query;
    the existing unreviewed accession is retained without asserting universal reviewed-entry
    absence.
  support: supports
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: 'UniProtKB REST searched 2026-11-03: gene_exact:IFT88 AND organism_id:3055
    AND reviewed:true, JSON size100; zero returned entries and no next page. Other
    aliases/species were not searched; no local absence claim.'
- evidence_id: micro-ift-bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038/nrm952%22%20OR%20DOI%3A%2210.1083/jcb.200504008%22%20OR%20DOI%3A%2210.1104/pp.010807%22%20OR%20DOI%3A%2210.1126/science.1128618%22%20OR%20EXT_ID%3A15955805%20OR%20EXT_ID%3A17312020%20OR%20EXT_ID%3A17326139%20OR%20EXT_ID%3A18852297%20OR%20EXT_ID%3A9585417&format=json&resultType=core&pageSize=100
  locator: All nine exact DOI/PMID title/author/publication-type identities and returned
    abstracts.
  accessed_at: '2026-11-03T05:43:13.110681Z'
  summary: Pazour, Nicastro, Cole, Hou, Ahmed, Sloboda and Lucker are primary studies;
    Silflow and Rosenbaum are reviews. Sloboda/Lucker current reassessment is abstract
    plus native annotation scope only. Silflow has no returned abstract. Metadata
    resolution does not prove body access.
  support: context_only
  snapshot_sha256: e234fcd401a2ccb6e0912a5b374c238ba93ce8723a7f6e431fbdded42ec28d23
- evidence_id: micro-base-bibliography
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016/j.cub.2014.11.066%22%20OR%20DOI%3A%2210.1038/s41467-022-31751-0%22%20OR%20DOI%3A%2210.1083/jcb.201006105%22%20OR%20DOI%3A%2210.1101/cshperspect.a028134%22&format=json&resultType=core&pageSize=100
  locator: Four exact DOI/PMID identities and abstracts.
  accessed_at: '2026-11-03T05:43:13.168249Z'
  summary: Craige2010, Diener2015 and Wang2022 are primary papers; Garcia-Gonzalo/Reiter2017
    is secondary. Its inspected abstract separates transition fibers (distal basal
    body to membrane) from TZ Y-links; current body attempts failed, so no fresh whole-review
    reading is claimed.
  support: context_only
  snapshot_sha256: 5b45c972a90b35e849387565b268894940b3f59ea9d5e6007fb785d76d151bd8
- evidence_id: micro-pazour2005
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2171396.1/PMC2171396.1.xml
  locator: Results Identification of flagellar proteins; Distribution of proteins
    in flagellar fractions; Discussion A subset of membrane proteins appear to be
    anchored to the axoneme.
  accessed_at: '2026-11-03T05:43:11.607980Z'
  summary: Purified Chlamydomonas flagella support the canonical example and membrane/matrix/axoneme
    distinction. WT Tergitol material and oda1-1 Nonidet/KCl fractions are distinct
    preparations. Candidate peptides, co-fractionation and intact membranes do not
    independently demonstrate assembly necessity or universal membership.
  support: supports
  snapshot_sha256: 07d7ef18479239d9cb12f3064152e086c0abc0f1a9657ac65b3e0cecb43701fa
- evidence_id: micro-cole1998
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132775.1/PMC2132775.1.xml
  locator: Cultures and Indirect Immunofluorescence Methods; Discussion Colocalization
    of FLA10 Kinesin-II and p172 at the Basal Bodies.
  accessed_at: '2026-11-03T05:43:11.690579Z'
  summary: IFT p172/p81/p139 concentrate around basal bodies, but the paper leaves
    their exact relationship to basal bodies versus rootlets unresolved. FLA10 transport
    and p172 regional targeting are distinct; p172 targeting can persist in bld2/inactive-fla10
    contexts. This supports associated assembly machinery, not whole-cilium self-assembly.
  support: supports
  snapshot_sha256: 7a1055581fe4adc86ed8142286edcde67e4059b3c02d89f317f5019b0f1e55ca
- evidence_id: micro-hou2007
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2064023.1/PMC2064023.1.xml
  locator: Results Cloning of C. reinhardtii IFT46; complex-A/B regional compartments;
    Discussion IFT46 stability and A/B distribution; gene-cloning methods.
  accessed_at: '2026-11-03T05:43:11.706748Z'
  summary: IFT46 is complex-B associated, predominantly peribasal with flagellar puncta.
    Null and suppressor interpretations distinguish assembly, complex stability and
    outer-arm transport; complex-A/B regional overlap is not interchangeable with
    permanent incorporation into a structural region.
  support: supports
  snapshot_sha256: d855eecdba394dedd578180b69d1ef7b24d4d5337688f8fd28fb3b1b93d64908
- evidence_id: micro-ahmed2008
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2568026.1/PMC2568026.1.xml
  locator: Results ODA16 localization; In vivo interaction between ODA16 and IFT particles;
    C. reinhardtii strains.
  accessed_at: '2026-11-03T05:43:12.153910Z'
  summary: Peribasal/flagellar ODA16 distribution and Chlamydomonas extract co-immunoprecipitation
    with IFT46/IFT81 support cargo-adaptor transport context. ODA16 does not co-purify
    as a retained outer-arm constituent; the mammalian screen is distinct from algal
    assays.
  support: supports
  snapshot_sha256: 2fde994c6f14e35e2cc5678fc946909c4f3fdc14951956c357be01cfcb1359d2
- evidence_id: micro-craige2010
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2935561.1/PMC2935561.1.xml
  locator: Results CEP290 location, mutant connector defects, immunogold localization
    and abnormal flagellar composition; Discussion component/connector interpretation.
  accessed_at: '2026-11-03T05:43:12.173496Z'
  summary: Chlamydomonas CEP290 loss/rescue and immunolocalization support TZ link
    organization and membrane tethering. Mutants have altered Y/wedge connections
    and composition; most axonemes and basal bodies are normal. No complete Y-link
    protein inventory or universal gate mechanism follows.
  support: supports
  snapshot_sha256: 16b42e69696668b0d2464aca13cc3163fcc0f557d034dfa99efa055a9b728ac1
- evidence_id: micro-wang2022
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9271036.1/PMC9271036.1.xml
  locator: Results Loss of TCTN1 ciliogenesis/ultrastructure; independent localization;
    variable phenotypes; ciliary-composition and ectosome sections at their stated
    opening comparisons; Strains and cell culture.
  accessed_at: '2026-11-03T05:43:12.258559Z'
  summary: TCTN1 wedge defects differ from Y-link loss; a normal 9+2 axoneme can remain.
    CEP290/TCTN1/NPHP4 occupy distinct TZ positions and localize independently. Mutant/autolysin/media
    conditions affect visible ciliogenesis. Comparative composition and ectosome assays
    support coarse regulation claims; no raw proteomics or all supplementary experiments
    were reanalyzed.
  support: supports
  snapshot_sha256: 15fd9769ed3cb90adc858d5997d1cc254334d0e0f6cf26dfe89d239d5b22b366
- evidence_id: micro-diener2015
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4318714.1/PMC4318714.1.xml
  locator: Results Isolation of transition zones, Ultrastructure and Proteomic analysis;
    Fig1B and Fig2 captions.
  accessed_at: '2026-11-03T05:43:12.648743Z'
  summary: Resorbing Chlamydomonas flagella yield isolated TZ vesicles with depolymerized
    outer doublets and missing in-situ features. The enriched preparation supports
    the canonical TZ-proteomics example, not a complete base inventory. Fig1B explicitly
    excludes transition fibers from TZ; the broader base therefore has known regions
    omitted by the current three TZ-only rows.
  support: supports
  snapshot_sha256: 3fcda6631400e1aaf86713554e4a18e089f7a4b0c3a8e7fe0b95ccb7ee759ee4
- evidence_id: micro-rosenbaum2002
  kind: authority
  reference: https://www.nature.com/articles/nrm952
  locator: Publisher Key Points and Abstract before subscription-content notice.
  accessed_at: '2026-11-03T05:43:14.500701Z'
  summary: 'Secondary review context: nonmembrane IFT particles move bidirectionally
    with kinesin-II and dynein; precursor delivery supports assembly/maintenance.
    Current access did not include the full review body.'
  support: context_only
  snapshot_sha256: 16772b6e81c9ef74a9c19e00352b3d765e6c09c4699e2b1665fb30e276c7bedf
- evidence_id: micro-silflow-access
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1540183/?pdf=1
  locator: PMC article metadata and PDF-only body notice.
  accessed_at: '2026-11-03T05:43:14.656000Z'
  summary: Silflow/Lefebvre2001 citation identity is confirmed, but this HTML provides
    no review body. It supplies no direct current proof of paraflagellar-rod or broad
    taxonomic claims.
  support: context_only
  snapshot_sha256: d52a0e6a67850bccd75253cab7de5f16a48d251b497843fc06a62e8a5f041e26
- evidence_id: micro-gene-5728998
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id=5728998&retmode=xml
  locator: Entrezgene_gene/Gene-ref locus tag, Phytozome cross-reference and formal
    name.
  accessed_at: '2026-11-03T05:43:13.281350Z'
  summary: NCBI Gene5728998 links CHLRE_03g167550v5 to Cre03.g167550. Formal name
    is uncharacterized protein; this alone does not prove CEP290 or NPHP4 symbol assignment.
  support: supports
  snapshot_sha256: 1c06ae2af4dcfaa1597ee1154b9c15e543b0180c4b2e239d20b1142f3a2ccf2d
- evidence_id: micro-gene-5718574
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=gene&id=5718574&retmode=xml
  locator: Entrezgene_gene/Gene-ref locus tag, Phytozome cross-reference and formal
    name.
  accessed_at: '2026-11-03T05:43:13.368755Z'
  summary: NCBI Gene5718574 links CHLRE_12g531400v5 to Cre12.g531400. Formal name
    is uncharacterized protein; this alone does not prove CEP290 or NPHP4 symbol assignment.
  support: supports
  snapshot_sha256: a56838b49bdc08ba5f4c60d5269976165461534e61d7e16e5ba5e2afc5824cd8
- evidence_id: micro-fauser2022
  kind: primary_source
  reference: https://www.nature.com/articles/s41588-022-01052-9.pdf
  locator: PDF page5/printed709, Fig4d first two row labels and Fig4 caption; page
    rendered locally and visually inspected.
  accessed_at: '2026-11-03T05:43:13.549624Z'
  summary: Fauser2022 labels Cre12.g531400 as NPHP4 and Cre03.g167550 as CEP290. Together
    with NCBI locus bridges, this supports the two exact literature-to-native-ORF
    mappings. Only these labels and caption/context were assessed, not the whole screen
    or supplementary data.
  support: supports
  snapshot_sha256: fc5fa7785f0d6d090731947488ad8c54ef8e439d1fa51ec4c3067b7a7b451594
- evidence_id: micro-dutcher2016
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4888484.1/PMC4888484.1.xml
  locator: Basal body structure and Basal body duplication sections, including Fig1
    caption.
  accessed_at: '2026-11-03T05:43:12.741712Z'
  summary: Secondary review distinguishes two mature and two pro-basal bodies, cartwheel-to-triplet
    progression and maturation; early new pro-basal bodies begin with singlets. BLD10
    is associated with spoke tips rather than the SAS6 hub. It supports developmental
    context, not a new primary experiment.
  support: context_only
  snapshot_sha256: 429c24022ba00944721b09a7837e0e2c78fb2a041648a150915bd5a658ac188d
- evidence_id: micro-wingfield2018
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6070942.1/PMC6070942.1.xml
  locator: Sections2.1 Basal Bodies,2.2 scaffold,4.2 developmental cycle and5.1 axoneme
    templating.
  accessed_at: '2026-11-03T05:43:12.742094Z'
  summary: Secondary review distinguishes SAS6 spokes and Bld10/Cep135 pinheads, dormant
    pro-basal bodies versus flagellated generations, and mature axoneme templating.
    Specific molecular arrangements are not generalized to every protist.
  support: context_only
  snapshot_sha256: b85cc0486b2c9ca4bbf5ce5b0450fa12a6324ec66cf04638346621a865dbea56
- evidence_id: micro-matsuura2004
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2172387.1/PMC2172387.1.xml
  locator: Results EM of bld10 basal bodies; Localization of Bld10p; Immuno-EM, including
    Fig7 context.
  accessed_at: '2026-11-03T05:43:12.987600Z'
  summary: Primary Bld10 antibody and immunogold evidence localizes Bld10 to cartwheel
    fibers, including pro-basal bodies. Examined bld10 sections lack morphologically
    recognizable normal basal bodies; this is not a demonstration that Bld10 forms
    the central SAS6 hub.
  support: supports
  snapshot_sha256: 5c397de0020904b247df8e98a8eb23868406edc6ba37172c44b983e5a45a0632
- evidence_id: micro-dutcher1998-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.9.6.1293
  locator: Exact DOI/PMID identity and complete returned primary abstract only.
  accessed_at: '2026-11-03T05:43:13.886002Z'
  summary: uni3-1 cells can assemble zero, one or two flagella and show proximal doublets
    rather than triplets. This is not complete absence of every triplet throughout
    the organelle, nor proof that triplets are universally dispensable. The exact
    Discussion sentence cited in the record was not freshly recovered.
  support: supports
  snapshot_sha256: 2e4cddebbd801df2391c39ad5e288a7b09741f6bf9d118dfd14326bd82ee1bf1
- evidence_id: micro-nakazawa2007-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2007.11.046
  locator: Exact DOI/PMID identity and complete returned primary abstract only.
  accessed_at: '2026-11-03T05:43:13.998692Z'
  summary: SAS6 localizes centrally; bld12 lacks that central cartwheel part and can
    form centrioles with variable triplet counts. The record correctly identifies
    this as abstract-level evidence and retains UNKNOWN assembly essentiality for
    the whole cartwheel.
  support: supports
  snapshot_sha256: f022e949b8844d554b6638e807033cc6c8e0e5e3aafb284c1f1c2f8eb793e9ac
- evidence_id: micro-hiraki2007-abstract
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17900905+AND+SRC%3AMED&format=json&resultType=core&pageSize=10
  locator: PMID17900905, DOI10.1016/j.cub.2007.09.021; complete returned primary abstract
    only.
  accessed_at: '2026-11-03T05:44:59.170591Z'
  summary: Truncated Bld10 constructs and immunoelectron localization identify Bld10
    as a major cartwheel-spoke-tip component attaching triplets. This directly supports
    correcting the definition’s SAS6/Bld10 hub wording. Exact percentage measurements
    are not imported into the record.
  support: supports
  snapshot_sha256: 4b1c55a16fa7ea7ca790a5bba99a7c42967d7ccb22853a576c42b3c9ab4f523a
- evidence_id: micro-probasal-agent-doi-s13630-016-0039-z
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1186/s13630-016-0039-z
  locator: DOI, PMID, title, authors and publication type.
  accessed_at: '2026-11-03T05:43:14.079812Z'
  summary: Bibliographic identity confirms the cited secondary review; source-native
    full-text sections are evaluated separately.
  support: context_only
  snapshot_sha256: 0e922762f9988f37fb6a6ec3163dc4929e5cae412a2e92fb0ed1e79e0dd59d39
- evidence_id: micro-probasal-agent-doi-cells7070079
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.3390/cells7070079
  locator: DOI, PMID, title, authors and publication type.
  accessed_at: '2026-11-03T05:43:14.398865Z'
  summary: Bibliographic identity confirms the cited secondary review; source-native
    full-text sections are evaluated separately.
  support: context_only
  snapshot_sha256: 8a4d0d4d8397bebcf5abd355dc59772833d5c9f1a3cd30dbb2c5f6993ffa1f0c
- evidence_id: micro-nicastro-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
  locator: Fresh browser-returned author-uploaded text lines71–77 and112–215, plus
    displayed Fig1–5 captions37–53. Browser response gives no HTTP status; crawl age
    is explicitly three weeks.
  accessed_at: '2026-11-03T05:45:07Z'
  summary: Primary text supports 9+2 architecture and dynein-based sliding/bending
    context in Chlamydomonas and sea-urchin preparations. Regulatory-linker roles
    include models. No whole-paper/SOM, movie or raw microscopy audit is claimed in
    this reassessment.
  support: supports
  snapshot_sha256: 14deb61ce0d772e2bf5a15d4d019e340412bc5d06c4b98e03a8d625d226856f5
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Entire official API organism/dataset list:20 organisms and28 dataset keys.
  accessed_at: '2026-11-03T05:43:52.952118Z'
  summary: No Chlamydomonas, Tetrahymena, Trypanosoma or other eukaryotic dataset
    is listed. Named-protein applicability was considered; with no matching organism,
    downstream module search/summarize is not applicable. Catalogue absence is not
    biological negative evidence.
  support: context_only
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical command, timestamp, exit1, status unavailable and PermissionError
    reason.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  summary: Earlier 00:49Z runner attempt could not read pyvenv.cfg. This is retained
    historical evidence, not a new execution or proof of present runner success. The
    current official catalogue was independently inspected as the permitted fallback.
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: micro-native-nine-two-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/9_2_motile_cilium.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/nine-two-uniprot-verify.log;
    paired receipt captures exact head/base/start/finish.
  accessed_at: '2026-11-03T05:42:50.903352Z'
  summary: 'Exit0: all existing accession/status/label/native-token/taxon pairs verify.
    Identity validation does not establish biological membership or free-text symbol
    orthology.'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-nine-two-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/9_2_motile_cilium.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/nine-two-uniprot-causal.log;
    paired receipt captures exact head/base/start/finish.
  accessed_at: '2026-11-03T05:42:51.451713Z'
  summary: 'Exit0: zero GENE_OR_PROTEIN nodes because graph nodes are STRUCTURE/PROCESS.
    This does not certify every component gene has an example or that graph causality
    is supported.'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-native-motile-cilium-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/motile-cilium-uniprot-verify.log;
    paired receipt captures exact head/base/start/finish.
  accessed_at: '2026-11-03T05:42:52.624619Z'
  summary: 'Exit0: all existing accession/status/label/native-token/taxon pairs verify.
    Identity validation does not establish biological membership or free-text symbol
    orthology.'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-motile-cilium-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/motile_cilium.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/motile-cilium-uniprot-causal.log;
    paired receipt captures exact head/base/start/finish.
  accessed_at: '2026-11-03T05:42:53.195139Z'
  summary: 'Exit0: zero GENE_OR_PROTEIN nodes because graph nodes are STRUCTURE/PROCESS.
    This does not certify every component gene has an example or that graph causality
    is supported.'
  support: supports
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-native-ciliary-base-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --verify
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/ciliary-base-uniprot-verify.log;
    paired receipt captures exact head/base/start/finish.
  accessed_at: '2026-11-03T05:42:54.559644Z'
  summary: 'Exit0: all existing accession/status/label/native-token/taxon pairs verify.
    Identity validation does not establish biological membership or free-text symbol
    orthology.'
  support: supports
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: micro-native-ciliary-base-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/appendage/ciliary_base.yaml
    --causal-graphs
  locator: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/ciliary-base-uniprot-causal.log;
    paired receipt captures exact head/base/start/finish.
  accessed_at: '2026-11-03T05:42:55.093471Z'
  summary: 'Exit0: one GENE_OR_PROTEIN node COVERED, linking the two native examples;
    not a completed mechanistic causality proof.'
  support: supports
  snapshot_sha256: 325ed6b53bc03abedd11adb2cf82cbf4272024d558150b70a030008c54cb7ddf
- evidence_id: micro-original-validation
  kind: validation
  reference: scripts/record_review.py validate; render --content; git show historical
    target
  locator: 'original-checks.json: four original bundles, exact rendered Markdown and
    current/historical target hashes.'
  accessed_at: '2026-11-03T05:48:08.355993Z'
  summary: All four native validations exit0, all four render commands exit0 and match
    saved Markdown byte-for-byte. Each target hash matches its original frozen input
    and original source commit as well as current HEAD; no target is stale.
  support: supports
  snapshot_sha256: 9e4839e2d278c7fcc910865a593ebe9ad29e3ef3be6b9ef79efdad71e26b9735
- evidence_id: septin-s2352-longitudinal-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097609,GO:0097610,GO:0097611,GO:0097612,GO:0097729
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:16.126228Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 05ff0432105e14c07cbd7c22b2cab259ebac685938b8a5cb24698c745d8ab805
- evidence_id: septin-s2352-longitudinal-prep-tax-2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:16.126520Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: da7d6dfa6d6784e4eb22bc3f3e05878f3aae5a281a4996ee25a2012d580f27d4
- evidence_id: septin-s2352-longitudinal-prep-taylor1980-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A7002229%20AND%20SRC%3AMED
  locator: Europe PMC exact PMID primary metadata and review abstract only.
  accessed_at: '2026-11-03T05:41:16.126601Z'
  support: supports
  summary: Taylor1980 is a review, not an inspected primary experimental body. Its
    title/author/DOI agree; native GO separately identifies which current term cites
    it.
  snapshot_sha256: 480504e4e55f80d3ede8eb6d745196886b76b4461701d13457fa794b89cb8106
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A7002229%20AND%20SRC%3AMED;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:16.126601Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-longitudinal-prep-taylor1980-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/0303264780900064?httpAccept=text/xml
  locator: Publisher API coredata XML, bibliographic fields and description only;
    HTTP200 did not supply article body.
  accessed_at: '2026-11-03T05:41:16.126661Z'
  support: supports
  summary: Source identity is verified; this response is not evidence of a flagellar
    assembly mechanism.
  snapshot_sha256: c4412fc99d85956bb46c41524b17fae0d57261ec0302293d8d856dc905528dd5
- evidence_id: septin-s2352-longitudinal-prep-sulcus-citation-meta
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:20561119%20AND%20SRC:MED
  locator: Europe PMC exact PMID primary-paper metadata and abstract only.
  accessed_at: '2026-11-03T05:41:16.126710Z'
  support: supports
  summary: Iwataki2010 concerns Cochlodinium polykrikoides ultrastructure and its
    flagellar apparatus. Native GO maps this PMID to sulcus GO0097612; no full historical
    paper inspection is claimed.
  snapshot_sha256: fa8e45e78bce39ba42890b05a8bd28fe3a9ca6e4822114f96b38022d16ae7ecd
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:20561119%20AND%20SRC:MED;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:16.126710Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-longitudinal-prep-maruyama2023-html-native
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/cytologia/88/4/88_D-23-00024/_html/-char/en
  locator: 'Native J-STAGE primary HTML: abstract, Introduction, culture/live microscopy/extracted-model
    Methods, claim-bearing longitudinal waveform/retraction Results, Figures1–4 captions
    and associated Discussion; no raw movies or figure-pixel reanalysis.'
  accessed_at: '2026-11-03T05:41:16.689126Z'
  support: supports
  summary: A. sanguinea NIES-4631 exhibits planar longitudinal undulation and fold/retraction
    under specified chamber and temperature conditions. Proposed molecular details
    and biological purpose remain hypotheses. One strain does not establish class-wide
    planar motion.
  snapshot_sha256: 9fdf86b1e4198bf3339bbeccfad57af0c1f6f7a53ba12ba4732a273be35665a4
- evidence_id: septin-s2352-transverse-agent-go-native
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097608,GO:0097729,GO:0097611,GO:0097610
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:16.866652Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: cf32d1f50262b3e2624ecf87cf911a31f3d6fade1a5d2d535728088938560ac7
- evidence_id: septin-s2352-transverse-agent-maruyama2024-html-native
  kind: primary_source
  reference: https://www.jstage.jst.go.jp/article/cytologia/89/4/89_D-24-00042/_html/-char/en
  locator: 'Native J-STAGE primary HTML: abstract, Introduction, NIES-4631 culture,
    live microscopy and non-detergent extraction Methods; live undulation, girdle
    attachment, contraction and reactivation Results; Figures3–6 and10 captions; claim-bearing
    Discussion. No raw videos or figure-pixel reanalysis.'
  accessed_at: '2026-11-03T05:41:16.875071Z'
  support: supports
  summary: Observed morphology, attachment and calcium-induced contraction are kept
    separate from proposed coupling. Mg2+ non-antagonism has a membrane-permeability
    caveat. Strand morphology does not establish a universal striated-strand-driven
    beating cycle; force-transmission structures are unresolved.
  snapshot_sha256: 16acafc328db87fb056c0e2061d2fd5351da6d848f5e803d57aac7c0a1f75f97
- evidence_id: septin-s2352-transverse-agent-epmc-native
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15277560%20OR%20EXT_ID:986199%20OR%20DOI:10.1099/00221287-46-2-305&format=json&resultType=core&pageSize=100
  locator: Europe PMC exact PMID/DOI returned primary abstracts and bibliographic
    metadata, including Miyasaka2004 and Leblond/Taylor1976; Leadbeater1967 entry
    has no abstract.
  accessed_at: '2026-11-03T05:41:16.913213Z'
  support: supports
  summary: 'Miyasaka2004 uses a Prorocentrum minimum resistive-force numerical model:
    transverse thrust and longitudinal rudder. This is model/context-specific evidence,
    not an all-dinoflagellate force partition or a native full-body read.'
  snapshot_sha256: def0b3d475c3435b938c3612c4b1e8488d338d3593b9fc512f34941dd3992bf9
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:15277560%20OR%20EXT_ID:986199%20OR%20DOI:10.1099/00221287-46-2-305&format=json&resultType=core&pageSize=100;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:16.913213Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-transverse-agent-schuech2025-dtu-native
  kind: authority
  reference: https://orbit.dtu.dk/en/publications/fluid-dynamics-of-dinoflagellate-feeding-and-swimming/
  locator: 'DTU institutional publication record: primary abstract, title/authors/DOI
    only; full paper and underlying flow data not inspected.'
  accessed_at: '2026-11-03T05:41:17.473018Z'
  support: supports
  summary: Schuech2025 abstract describes flow visualization and computational fluid
    dynamics, with transverse thrust and trailing steering. Distinguish this abstract-level
    claim from Cachon1991 organism-specific observations.
  snapshot_sha256: 356b9d07287b7ff7b30be511ab2f34df6a9d145db52470ebd7d0941f60deeeff
- evidence_id: septin-s2352-aster-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000235,GO:0005818,GO:0005819,GO:0005874,GO:0030989,GO:0032117,GO:0043232,GO:0099080
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:17.853741Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 72f2d3236ea3fa4b2ea57f8e10614f75f54a3a82188d4bdbb7dd69877375c632
- evidence_id: septin-s2352-aster-agent-tax-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:18.045875Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: septin-s2352-aster-agent-tax-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:18.505437Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: septin-s2352-aster-agent-IPR002452
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:18.595879Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: septin-s2352-aster-agent-IPR002453
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:18.675503Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: septin-s2352-aster-agent-P04689
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P04689.json
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:18.763535Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 3bfa569ef452b581ecc2013f8b85880667fd4de3e6d11df1bdcbbc3319ade3e3
- evidence_id: septin-s2352-aster-agent-query-tub1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Atub1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:19.131802Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 002ff4e9a7f59e2d3d6e32bf57e151690c33deb1d844b6dce12d600e6327fd5e
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Atub1%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:19.131802Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-aster-agent-P04688
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P04688.json
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:19.192782Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: f6104d4ad0cb6eae74ad3cdbfc6a3c779f42c9522e262843d52d6ca7ef46f4fd
- evidence_id: septin-s2352-aster-agent-query-nda2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anda2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:19.295588Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: d1fc305203c3dddb4514d3973ea77f424df3ae4d0b108dffb6c31d1d9ed60ca3
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anda2%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:19.295588Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-aster-agent-P05219
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P05219.json
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:19.499465Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 748f30a9ed411acc3358c1828f32354becece0ef6d16b60ef4319c8d6bbe66b2
- evidence_id: septin-s2352-aster-agent-query-nda3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anda3%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:19.869663Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: bb80a570bfc520130e8d196c38f607995175eaec231abebdea20b19676434523
  search_scope: Database/request https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3Anda3%29%20AND%20%28organism_id%3A284812%29%20AND%20%28reviewed%3Atrue%29;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:19.869663Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-aster-agent-doi-j.cub.2005.07.058
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2005.07.058
  locator: Europe PMC exact DOI primary abstract and bibliographic metadata only.
  accessed_at: '2026-11-03T05:41:19.897265Z'
  support: supports
  summary: Tanaka2005 identifies S. pombe Hrs1/Mcp6-dependent meiotic HAA organization,
    impaired HAA/HNM on deletion, ectopic-expression phenotype and gamma-TuRC interaction.
    Proposed minus-end stabilization and recombination relevance are not converted
    to universal mechanisms.
  snapshot_sha256: b774d7d9ae22e94d9758b59c0f24de4bda443578035c5a69ac6db64622120e93
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2005.07.058;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:19.897265Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-aster-agent-doi-j.cub.2012.02.042
  kind: search
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2012.02.042
  locator: Europe PMC exact DOI primary metadata and abstract, distinct from the native
    full-body source below.
  accessed_at: '2026-11-03T05:41:20.551478Z'
  support: supports
  summary: Funaya2012 source identity and meiotic reorganization context verified;
    claim-specific body/caption/supplement evidence is separately bounded.
  snapshot_sha256: 74ff9c0672edac602df99d3e760b7346e0642f4100839c6381f1696d4599f944
  search_scope: Database/request https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cub.2012.02.042;
    exact query and limit encoded in URL, executed 2026-11-03T05:41:20.551478Z; no
    publication-date restriction. Only returned results inspected; no exhaustive literature
    or biological absence assertion.
- evidence_id: septin-s2352-aster-agent-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml
  locator: 'Native PMC open-data JATS body: Introduction, Hrs1/rMTOC localization
    and gamma-tubulin Results, meiotic disassembly and phosphorylation passages, Figure4
    full caption and experimental context. Not every remaining paragraph, movie or
    raw dataset was independently reanalyzed.'
  accessed_at: '2026-11-03T05:41:20.857938Z'
  support: supports
  summary: S. pombe meiotic radial arrays and Hrs1/rMTOC are distinct from the ensuing
    MI spindle. Figure4A uses homothallic Hrs1-GFP/mCherry-Atb2 cells; synchronized
    pat1 mat-Pc diploids are separate experiments. This supports the specialized example,
    not broad Kar9/Bim1/EB1/Bik1 mitotic capture claims or an isoform occupancy census.
  snapshot_sha256: 59f662c998abf622fbb9bccbabc3867cb5ffd3174943cc52cb6228b1e35cd93d
- evidence_id: septin-s2352-aster-agent-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/mmc1.pdf
  locator: 'Native PMC mmc1 PDF text: TableS1 strains (including KT2901 and separate
    pat1 mat-Pc diploids), relevant FigureS1–S3 captions and Supplemental Experimental
    Procedures for synchronization, fluorescent imaging and EM preparation. Not complete
    supplement-wide or image/movie reanalysis.'
  accessed_at: '2026-11-03T05:41:21.158351Z'
  support: supports
  summary: KT2901 is homothallic with Hrs1-GFP-2xFLAG and Pnda3-mCherry-atb2; imaging
    and synchronized ultrastructure preparations remain distinct. Reference UniProt
    strain identity is not asserted to be the exact experimental stock.
  snapshot_sha256: 6dde9cc7999b0e3294aa95f3d3036a319c90b9390920d84bd7194c883dc213f9
- evidence_id: septin-s2352-astral-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000235,GO:0005818,GO:0005819,GO:0005874,GO:0005876,GO:0030989,GO:0032117
  locator: 'Fresh native issuing-authority response: exact identifiers, labels, definitions,
    taxon or returned family/protein annotation fields.'
  accessed_at: '2026-11-03T05:41:21.313484Z'
  support: supports
  summary: Current identifiers and source attribution checked within the returned
    authority scope. Identity annotation is not a new primary experiment or proof
    of assembly necessity.
  snapshot_sha256: 9a41356e287c3a6268afcba7e91591f19f6d7e1ff4c80623664293a74800771a
- evidence_id: septin-s2352-current-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire fresh official /api/datasets response: 20 organism objects and
    28 dataset keys; all returned organism names inspected.'
  accessed_at: '2026-11-03T05:41:21.888575Z'
  support: supports
  summary: No Schizosaccharomyces, other fungal or protist dataset occurs in this
    bounded returned catalogue. Therefore the molecular aster/astral records have
    no matching dataset for downstream gene/module queries. This is a catalogue coverage
    result, not gene absence or an exemption based on lack of expression claims.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: septin-s2352-cachon-indexed
  kind: primary_source
  reference: https://aquaparadox.obs-vlfr.fr/html/PFD/Taxonomic%20Monographs/Cachon%20et%20al%201991.pdf
  locator: 'Fresh browser-indexed primary PDF passages, returned text lines0–66,154–224,254–257,288–323,431–469:
    organisms/methods, longitudinal waveforms, motility interpretation and proposed
    coiling. Native download timed out; no native PDF bytes, figure pixels or raw
    videos read.'
  accessed_at: '2026-11-03T05:43:07.985Z'
  support: supports
  summary: Ceratium and Oxyrrhis observations include three-dimensional nonplanar
    longitudinal waves and different retraction/motility modes. Calcium-driven striated-fiber
    coiling is proposed in Discussion. These contexts differ from planar Akashiwo;
    the sources do not establish one universal waveform or thrust partition.
  snapshot_sha256: a8f9d9d4dc71aee036ba0753c46e41427572b56eb296c346cf36c0d3f6aba832
- evidence_id: septin-s2352-leadbeater-micro-abstract
  kind: primary_source
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-46-2-305
  locator: Fresh publisher page abstract, returned lines47–52 only. Native request403;
    browser page did not supply full body.
  accessed_at: '2026-11-03T05:42:43.280Z'
  support: supports
  summary: Leadbeater/Dodge1967 abstract describes 9+2 organization, transverse ribbon
    morphology, shorter striated strand, sheath and hairs. Morphology supports scoped
    structure, not a complete causal beat mechanism.
  snapshot_sha256: a8f9d9d4dc71aee036ba0753c46e41427572b56eb296c346cf36c0d3f6aba832
- evidence_id: septin-s2352-leadbeater-nature-preview
  kind: search
  reference: https://www.nature.com/articles/213421a0
  locator: Fresh indexed publisher abstract/preview only; native HTTP200 response
    was an authorization page and is not treated as article text.
  accessed_at: '2026-11-03T05:43:18.322Z'
  support: supports
  summary: Preview distinguishes posterior flagellar and transverse helical observations
    and source taxa. It is not a newly retrieved native full body.
  snapshot_sha256: a8f9d9d4dc71aee036ba0753c46e41427572b56eb296c346cf36c0d3f6aba832
  search_scope: Web search at 2026-11-03T05:43:18.322Z; exact queries ['site:nature.com/articles/213421a0
    "flagellum"', 'site:aquaparadox.obs-vlfr.fr "Cachon" "1991" "propose" "coiling"'];
    response_length long, no date restrictions, no pagination. Only exact matching
    Leadbeater publisher preview used; unrelated hits excluded.
- evidence_id: septin-s2352-cachon-bounded-search
  kind: search
  reference: https://aquaparadox.obs-vlfr.fr/html/PFD/Taxonomic%20Monographs/Cachon%20et%20al%201991.pdf
  locator: Saved returned web search results used to locate the matching primary indexed
    PDF.
  accessed_at: '2026-11-03T05:43:00.620Z'
  support: supports
  summary: Source discovery only; returned hits do not establish literature absence.
  snapshot_sha256: a8f9d9d4dc71aee036ba0753c46e41427572b56eb296c346cf36c0d3f6aba832
  search_scope: Web search at 2026-11-03T05:43:00.620Z; queries ['"Dinoflagellate
    flagella adopt various conformations" pdf', '"Cachon" "1991" "non-planar" flagella',
    '"Dinoflagellate flagella" "three-dimensional" "1991"']; response_length long,
    no date/domain restrictions or pagination. Only cited exact-title PDF followed.
- evidence_id: septin-s2352-record-longitudinal_flagellum
  kind: record_content
  reference: data/structures/appendage/longitudinal_flagellum.yaml
  locator: 'Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174:
    definition, hierarchy, components, examples, evidence, discussions and every graph
    node/edge.'
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Current record equals original frozen target bytes.
  snapshot_sha256: 194925fd64e2b09a0877b398d407d96e759784f7df56d8aeda196de1259fb4ac
- evidence_id: septin-s2352-record-transverse_flagellum
  kind: record_content
  reference: data/structures/appendage/transverse_flagellum.yaml
  locator: 'Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174:
    definition, hierarchy, components, examples, evidence, discussions and every graph
    node/edge.'
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Current record equals original frozen target bytes.
  snapshot_sha256: 890d535141482292884c4b8bdedf6355ef8f6330aabba9d0cba890c5bf4df79c
- evidence_id: septin-s2352-record-aster
  kind: record_content
  reference: data/structures/cytoskeleton/aster.yaml
  locator: 'Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174:
    definition, hierarchy, components, examples, evidence, discussions and every graph
    node/edge.'
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Current record differs by added nda2 alpha-tubulin symbol plus curation
    history. Scientific content was reassessed against current sources and native
    checks; no record edit.
  snapshot_sha256: ead65813443a3277dee3611ec40e32b7bc4c3882d8c31508eb352f6fffdfd6df
- evidence_id: septin-s2352-record-astral_microtubule
  kind: record_content
  reference: data/structures/cytoskeleton/astral_microtubule.yaml
  locator: 'Complete current YAML at source HEAD9a8a31291456921b6e1984a3a95f110c763c5174:
    definition, hierarchy, components, examples, evidence, discussions and every graph
    node/edge.'
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Current record differs by added nda2 alpha-tubulin symbol plus curation
    history. Scientific content was reassessed against current sources and native
    checks; no record edit.
  snapshot_sha256: 45c1ec56a960d58bde433d88317824b726ff48473bc9b0b1d4429c6e2f57041d
- evidence_id: septin-s2352-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Current frozen policy/schema, relevant evidence and causal graph passages.
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Evidence must match the scientific assertion and taxon/state; named molecular
    claims require structured-source applicability assessment.
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
- evidence_id: septin-s2352-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Current frozen policy/schema, relevant evidence and causal graph passages.
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Mechanistic claims need evidenced causal direction; spatial containment
    alone is not an assembly mechanism.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: septin-s2352-graph-scope-policy
  kind: authority
  reference: .claude/skills/add-cell-structure/SKILL.md
  locator: Current frozen policy/schema, relevant evidence and causal graph passages.
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: The native graph contract distinguishes source-backed causal mechanism
    from topology/function summaries; no atomistic detail or invented mechanism is
    demanded.
  snapshot_sha256: eee04ee51d2c82c05df98570674084bdce9001e5aa67d6230ac1ed50064a3175
- evidence_id: septin-s2352-graph-schema
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Current frozen policy/schema, relevant evidence and causal graph passages.
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Native schema field/type meanings checked; schema-valid graphs may still
    exceed their scientific source scope.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: septin-s2352-prior-nda2-finding
  kind: prior_review
  reference: reviews/structured/20261023T230503Z-cytoskeleton-category-review/review.yaml
  locator: F2, issue_key cytoskeleton-fission-yeast-nda2-gene-symbol-omission; targets
    GO0005818, GO0000235, GO0032117, GO1990295.
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: Current first two assigned records now contain nda2; their corrected symbol
    is independently verified. Other two targets are unassessed here, so this multi-target
    historical finding is not terminally resolved by this subreview. Root reports
    linked issue2421 already closed.
  snapshot_sha256: ffd4b4cf845f8a4ec0d7806c62152b0e92be5620b6a1373a9e7b292349474def
- evidence_id: septin-s2352-original-native-checks
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/adversary-septin/original-checks.json
  locator: Four original native validate and render --content runs; committed Markdown
    byte comparisons and frozen/source/current hashes.
  accessed_at: '2026-11-03T05:47:11.104051Z'
  support: supports
  summary: All four original bundles validate and render identically. Two flagellar
    targets unchanged; aster/astral changed since original freeze and are substantively
    refreshed here. Historical QC receipts are not current CI.
  snapshot_sha256: 0e162a7bf83ef47ecab48ffef07118d8c7d845fedf3f89988404fc827d40b2a5
- evidence_id: septin-s2352-aster-native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/aster-uniprot-verify-receipt.json
  locator: Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py',
    '--record', 'data/structures/cytoskeleton/aster.yaml', '--verify'] at head 9a8a31291456921b6e1984a3a95f110c763c5174;
    receipt and log independently read.
  accessed_at: '2026-11-03T05:42:06.474758Z'
  support: supports
  summary: 'Exit0: protein examples and causal graph UniProt xrefs verified.'
  snapshot_sha256: fdb208f71d43f76c2cae8559433ff5bdea992f1ecfd3fc86f5a40b6debf18832
- evidence_id: septin-s2352-aster-native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/aster-uniprot-causal-receipt.json
  locator: Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py',
    '--record', 'data/structures/cytoskeleton/aster.yaml', '--causal-graphs'] at head
    9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently read.
  accessed_at: '2026-11-03T05:42:06.912997Z'
  support: supports
  summary: 'Exit0: alpha and beta GENE_OR_PROTEIN nodes both COVERED, no missing-symbol/dangling
    reference. Identifier coverage does not validate broad mechanism or graph-scope
    claims.'
  snapshot_sha256: 6feb4fb171ee3f01ba8d4cc7f013987d90bf208cecf1462f8af755c6deecc9c7
- evidence_id: septin-s2352-astral-native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/astral-uniprot-verify-receipt.json
  locator: Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py',
    '--record', 'data/structures/cytoskeleton/astral_microtubule.yaml', '--verify']
    at head 9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently
    read.
  accessed_at: '2026-11-03T05:42:07.952115Z'
  support: supports
  summary: 'Exit0: protein examples and causal graph UniProt xrefs verified.'
  snapshot_sha256: c7884e73172e2c265750c1855e1c23281e3111506cb9a76cc674aff151f3329e
- evidence_id: septin-s2352-astral-native-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/astral-uniprot-causal-receipt.json
  locator: Root-run exact command ['.venv/bin/python', 'scripts/uniprot_genes.py',
    '--record', 'data/structures/cytoskeleton/astral_microtubule.yaml', '--causal-graphs']
    at head 9a8a31291456921b6e1984a3a95f110c763c5174; receipt and log independently
    read.
  accessed_at: '2026-11-03T05:42:08.381989Z'
  support: supports
  summary: 'Exit0: alpha and beta GENE_OR_PROTEIN nodes both COVERED, no missing-symbol/dangling
    reference. Identifier coverage does not validate broad mechanism or graph-scope
    claims.'
  snapshot_sha256: 413bc985b368e1d34f4768ec07d0014b6f546d6ffbc80f6940f7d8a573eb242f
- evidence_id: septin-s2352-historical-runner-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z,
    exit1 PermissionError reading pyvenv.cfg; inherited actual receipt, not a current
    invocation.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: supports
  summary: The historical runner was OS-unavailable. Current applicability uses a
    fresh official catalogue fallback; no runner or downstream gene/module execution
    is claimed.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:46:49.255523Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: 3ba5420855164cc0ec662fcda9319d899abd7bca366d5dcef60f53b0e1b31022
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:41:22.673008Z'
  support: supports
  summary: 4232 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: d8200b370ec584f49336f01ed9035fbe21f0aa191ad0257a9a421938e9f17ecb
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:41:03.154147Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:41:04.868745Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T05:41:34.115578Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T05:51:22Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: f1f94df00ebfc2ad122eaa175f7c27dddfa3db5d0ce8417269b88bf076d24b63
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2352/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T05:43:12.465380Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 63b5d67ca7eca1b4754dfe014706c7296694e5d9eb66e48f8fb7f4933d9510d8
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2352 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-germ-identity
  area: identity
  topic: Generic germ tube and source-scoped septin localization
  outcome: supported
  summary: Exact GO0032179 identity and appendage kind remain correct. Native GO and
    Candida primary/review context support cap/ring membership and leading-edge septins.
    The source literature legitimately uses germ tube for Candida outgrowth; no spore-versus-yeast
    terminology contradiction is manufactured.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-current-0
  - plaque-germ-tube-agent-go
  - plaque-germ-tube-agent-douglas-pmc
  - plaque-germ-tube-agent-warenda2002
- assessment_id: plaque-germ-definition
  area: provenance
  topic: Apical cap versus basal band
  outcome: concern
  summary: The unchanged definition still merges basal collar/cap and attributes the
    appended Cdc42/Spitzenkörper/polarisome dependence across three named fungi to
    the GO-only definition. Native cap and basal-band locations differ. Retain F2
    and source/qualify additions without declaring the broader polarity biology false.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-current-0
  - plaque-germ-tube-agent-go
  - plaque-germ-tube-agent-douglas-pmc
  - plaque-germ-tube-agent-warenda2002
- assessment_id: plaque-germ-family
  area: grounding
  topic: Generic septin identity independent of complete cap cohort
  outcome: concern
  summary: The component denotes generic septin proteins, not a complete mixed cap
    complex. Exact IPR016491 therefore supports that family identity independently
    of species-specific composition. The current rationale still makes a complete
    cap cohort a prerequisite for grounding; retain F3.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-current-0
  - plaque-germ-tube-agent-family
  - plaque-germ-tube-agent-go
- assessment_id: plaque-germ-graph
  area: graph
  topic: Parthood-only graph is not an assembly mechanism
  outcome: concern
  summary: All three edges remain is part of; no assembly event or causal intermediate
    is represented. ASSEMBLY/MECHANISTIC still overstates this membership graph. Retain
    F1, with correction through separately authorized record curation.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-current-0
  - plaque-graph-contract
  - plaque-policy
  - plaque-germ-tube-agent-go
- assessment_id: plaque-germ-necessity
  area: evidence
  topic: Generic-class assembly necessity remains unresolved
  outcome: unknown
  summary: Local septin signal and individual cdc10/cdc11 deletion phenotypes do not
    establish necessity or dispensability of the whole generic septin class for germ-tube
    assembly. Other septins persist; viability and morphology are distinct from assembly.
    Keep the original explicit unknown.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-current-0
  - plaque-original-0
  - plaque-germ-tube-agent-warenda2002
  - plaque-protein-policy
- assessment_id: plaque-germ-proteins
  area: completeness
  topic: Generic protein class requires no invented gene examples
  outcome: supported
  summary: Native verifier passes, while the causal diagnostic honestly reports one
    NO_GENE_SYMBOLS and zero COVERED. This generic component need not be populated
    with an invented named gene cohort; absence of optional examples is not a separate
    finding.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-current-0
  - plaque-protein-policy
  - plaque-germ-tube-native-verify
  - plaque-germ-tube-native-causal
- assessment_id: plaque-arp-identity
  area: identity
  topic: Whole complex, cortical patch and seven concrete examples
  outcome: supported
  summary: Whole-complex identity and actin-cytoskeleton parthood remain distinct
    from the patch/polymer on which it acts. All seven reviewed yeast gene/accession/taxon
    examples resolve, and native membership annotations are source-qualified. Sagot
    fresh native Methods/Results supports only partial actin-body colocalization of
    the four cited proteins; it is not evidence that all seven occupy every body.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-current-1
  - plaque-arp-agent-go
  - plaque-arp-agent-sagot2006-browser
  - plaque-arp-agent-pmid-9210376
  - plaque-arp-agent-P32381
  - plaque-arp-agent-P47117
  - plaque-arp-agent-P53731
  - plaque-arp-agent-P33204
  - plaque-arp-agent-P38328
  - plaque-arp-agent-Q05933
  - plaque-arp-agent-P40518
- assessment_id: plaque-arp-type-refresh
  area: consistency
  topic: Substantive refresh of three component-type changes
  outcome: supported
  summary: Current Arp2/3 has PROTEIN_COMPLEX on all three deliberately grouped heteromeric
    components. Each group contains distinct named subunits rather than one family/paralogue
    class; fresh exact identities and the native type contract support the correction.
    History already cites closed2420/2431. This PR does not repair the record or terminally
    supersede the multi-target category findings; only its Arp2/3 slice was reassessed.
    The changes do not repair original F1/F2.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-policy
  - plaque-arp-category-0
  - plaque-arp-category-1
  - plaque-issue-2420
  - plaque-issue-2431
  - plaque-arp-agent-P32381
  - plaque-arp-agent-P47117
  - plaque-arp-agent-P53731
  - plaque-arp-agent-P33204
  - plaque-arp-agent-P38328
  - plaque-arp-agent-Q05933
  - plaque-arp-agent-P40518
- assessment_id: plaque-arp-pairings
  area: grounding
  topic: Reversed Arc19/Arc18 defining homolog labels persist
  outcome: concern
  summary: Fresh P33204 identifies ARC19/subunit4, while Q05933 identifies ARC18/subunit3.
    The definition still reverses their ARPC3/4 pairings, despite correct component
    labels/examples. Retain original major F1 with exact lineage.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-current-1
  - plaque-arp-agent-P33204
  - plaque-arp-agent-Q05933
- assessment_id: plaque-arp-mechanism-attribution
  area: evidence
  topic: Young2004 does not support attributed subunit mechanisms
  outcome: concern
  summary: Full freshly read Young2004 main text/captions/TableI analyzes isolated
    patches, branches and sac6/cap1 mutants. It does not characterize the Arc35/Arc19
    clamp or define Arc40/Arc18/Arc15 activation coupling as claimed. Accessible Kaksonen
    abstract and Galletta regulator observations do not independently establish the
    specified short-pitch rearrangement. Retain original major F2; plausible biology
    is distinct from false source-specific attribution.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-current-1
  - plaque-arp-agent-jats-jcb.200404159
  - plaque-arp-agent-galletta2008-plos
  - plaque-arp-agent-kaksonen2003-meta
  - plaque-arp-agent-P32381
  - plaque-arp-agent-P47117
  - plaque-arp-agent-P53731
  - plaque-arp-agent-P33204
  - plaque-arp-agent-P38328
  - plaque-arp-agent-Q05933
  - plaque-arp-agent-P40518
- assessment_id: plaque-arp-functions
  area: evidence
  topic: Patch architecture and endocytic dynamics at inspected scope
  outcome: supported
  summary: Young supports roughly70-degree branch geometry in partially purified patches,
    with preservation/flattening limits. Galletta supports regulator-specific assembly/movement
    effects and Kaksonen abstract supports a temporal endocytic pathway. Reference
    S288C accessions do not assert that every experimental stock is the reference
    strain. Broad amoeba/filamentous-fungus process combinations were not independently
    established.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-arp-agent-jats-jcb.200404159
  - plaque-arp-agent-galletta2008-plos
  - plaque-arp-agent-kaksonen2003-meta
  - plaque-arp-agent-tax-4932
  - plaque-arp-agent-tax-559292
- assessment_id: plaque-arp-necessity
  area: evidence
  topic: Group-specific assembly necessity remains unknown
  outcome: unknown
  summary: The three ESSENTIAL assertions are not established by membership, localization,
    cell viability or catalytic activity. Winter1997 abstract describes a preparation
    lacking a40kDa member, but that is not removal of the entire three-protein peripheral
    group. No group-specific complete-removal/assembly test was checked.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-current-1
  - plaque-original-1
  - plaque-arp-agent-pmid-9210376
  - plaque-policy
- assessment_id: plaque-arp-native-proteins
  area: evidence
  topic: Current native example and causal-node coverage
  outcome: supported
  summary: Root-executed verification and causal checks passed at source head and
    their receipts/log hashes were independently checked. All three nodes are COVERED
    for all seven declared symbols. Deterministic coverage does not resolve F1/F2
    or assembly necessity.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-arp2-3-native-verify
  - plaque-arp2-3-native-causal
- assessment_id: plaque-adapter-0
  area: evidence
  topic: Actual structured-source applicability
  outcome: supported
  summary: The fresh complete public catalogue contains no matching fungal dataset
    for Candida/Aspergillus/Neurospora germ-tube claims, including Cdc42 and septins.
    Downstream module searches are not applicable after this coverage check. Historical
    runner unavailability remains separate; no fresh runner success or biological
    absence is claimed.
  target_ids:
  - GO:0032179
  evidence_ids:
  - plaque-adapter-catalogue
  - plaque-adapter-policy
  - plaque-current-0
- assessment_id: plaque-adapter-1
  area: evidence
  topic: Actual structured-source applicability
  outcome: supported
  summary: The fresh complete public catalogue contains no matching fungal dataset
    for the named Saccharomyces Arp2/3 genes and regulators. Downstream module searches
    are not applicable after this coverage check. Historical runner unavailability
    remains separate; no fresh runner success or biological absence is claimed.
  target_ids:
  - GO:0005885
  evidence_ids:
  - plaque-adapter-catalogue
  - plaque-adapter-policy
  - plaque-current-1
- assessment_id: micro-nine-two-integrity
  area: schema
  topic: Frozen record and historical review integrity
  outcome: supported
  summary: Current and historical target bytes match the frozen original input; original
    YAML validates and its renderer reproduces Markdown exactly. Prior findings remain
    open with exact lineage; historical global-validator totals are not current results.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-prior-nine-two
  - micro-original-validation
- assessment_id: micro-nine-two-adapter
  area: provenance
  topic: Named-protein structured-source applicability
  outcome: supported
  summary: Named proteins trigger the adapter policy. The earlier runner limitation
    is explicitly historical; the freshly inspected official catalogue contains no
    matching eukaryotic dataset, so gene/module search and summary are not applicable.
    This is not negative evidence about the structure.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-base-integrity
  area: schema
  topic: Frozen record and historical review integrity
  outcome: supported
  summary: Current and historical target bytes match the frozen original input; original
    YAML validates and its renderer reproduces Markdown exactly. Prior findings remain
    open with exact lineage; historical global-validator totals are not current results.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-prior-base
  - micro-original-validation
- assessment_id: micro-base-adapter
  area: provenance
  topic: Named-protein structured-source applicability
  outcome: supported
  summary: Named proteins trigger the adapter policy. The earlier runner limitation
    is explicitly historical; the freshly inspected official catalogue contains no
    matching eukaryotic dataset, so gene/module search and summary are not applicable.
    This is not negative evidence about the structure.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-motile-integrity
  area: schema
  topic: Frozen record and historical review integrity
  outcome: supported
  summary: Current and historical target bytes match the frozen original input; original
    YAML validates and its renderer reproduces Markdown exactly. Prior findings remain
    open with exact lineage; historical global-validator totals are not current results.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-prior-motile
  - micro-original-validation
- assessment_id: micro-motile-adapter
  area: provenance
  topic: Named-protein structured-source applicability
  outcome: supported
  summary: Named proteins trigger the adapter policy. The earlier runner limitation
    is explicitly historical; the freshly inspected official catalogue contains no
    matching eukaryotic dataset, so gene/module search and summary are not applicable.
    This is not negative evidence about the structure.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-probasal-integrity
  area: schema
  topic: Frozen record and historical review integrity
  outcome: supported
  summary: Current and historical target bytes match the frozen original input; original
    YAML validates and its renderer reproduces Markdown exactly. Prior findings remain
    open with exact lineage; historical global-validator totals are not current results.
  target_ids:
  - GO:0120280
  evidence_ids:
  - micro-record-probasal
  - micro-prior-probasal
  - micro-original-validation
- assessment_id: micro-probasal-adapter
  area: provenance
  topic: Named-protein structured-source applicability
  outcome: supported
  summary: Named proteins trigger the adapter policy. The earlier runner limitation
    is explicitly historical; the freshly inspected official catalogue contains no
    matching eukaryotic dataset, so gene/module search and summary are not applicable.
    This is not negative evidence about the structure.
  target_ids:
  - GO:0120280
  evidence_ids:
  - micro-record-probasal
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-nine-two-identity
  area: identity
  topic: Exact class and coarse composition
  outcome: supported
  summary: Exact nine-doublets-plus-central-pair subtype, motile-cilium parent and
    scoped synonyms agree with GO. Axoneme, membrane, basal body, TZ and associated
    IFT identities are appropriate. Individual component essentiality is assessed
    separately.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-go
  - micro-pazour2005
  - micro-nicastro-browser
- assessment_id: micro-nine-two-examples
  area: grounding
  topic: Five exact IFT examples and location attribution
  outcome: supported
  summary: The four reviewed entries and one unreviewed IFT88 match native labels/tokens/taxon.
    Four reviewed exact-gene matches are unique within the bounded query; IFT88 reviewed
    search is empty. IFT172/IFT46 experimental annotation citations are location-specific;
    IFT81/IFT74/IFT88 are identity-only. No sixth IFT52 example or complete protein
    inventory is forced.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-protein-policy
  - micro-tax3055
  - micro-ift-reviewed-search
  - micro-ift88-reviewed-search
  - micro-uniprot-Q5DM57
  - micro-uniprot-Q68RJ5
  - micro-uniprot-Q6RCE1
  - micro-uniprot-A2T2X4
  - micro-uniprot-Q9FPW0
  - micro-cole1998
  - micro-hou2007
  - micro-ahmed2008
- assessment_id: micro-nine-two-essentiality
  area: evidence
  topic: Assembly necessity remains independently unverified
  outcome: unknown
  summary: Canonical anatomy, proteomic presence and localization do not independently
    establish every ESSENTIAL broad-component assembly-necessity claim. No suitable
    depletion/reconstitution experiment for each entire regional component was checked;
    the enum is not redefined as activity or viability.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-schema-policy
  - micro-record-nine-two
  - micro-pazour2005
  - micro-cole1998
  - micro-nicastro-browser
- assessment_id: micro-nine-two-function
  area: evidence
  topic: Assembly, movement and model-system scope
  outcome: supported
  summary: Chlamydomonas IFT transport and isolated-axoneme architecture support assembly/maintenance
    and dynein-based movement at their stated scope. Purified WT/mutant fractions
    are distinguished; broad cross-protist conservation wording is not treated as
    a fully audited three-species molecular comparison. Silflow body remains unverified.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-pazour2005
  - micro-cole1998
  - micro-hou2007
  - micro-rosenbaum2002
  - micro-nicastro-browser
  - micro-ift-bibliography
  - micro-silflow-access
- assessment_id: micro-nine-two-part-scope
  area: scope
  topic: Accessory part is not a class-wide obligatory constituent
  outcome: concern
  summary: PFR is limited to some flagellated protists, while unqualified has_part
    and graph membership are broader. A native inverse part_of child display does
    not imply universal has_part.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-go
- assessment_id: micro-nine-two-graph
  area: graph
  topic: Static membership and whole-cilium self-assembly
  outcome: concern
  summary: The nine nodes and eight edges provide parthood, association and generic
    outputs. The whole assembled cilium mediates its own assembly; no actor-to-event
    causal pathway makes this a MECHANISTIC graph. IFT/motor primary evidence exists
    but is not encoded by those static edges.
  target_ids:
  - GO:0097729
  evidence_ids:
  - micro-record-nine-two
  - micro-graph-policy
  - micro-schema-policy
  - micro-cole1998
  - micro-hou2007
  - micro-nicastro-browser
  - micro-rosenbaum2002
- assessment_id: micro-motile-identity
  area: identity
  topic: Exact class and coarse composition
  outcome: supported
  summary: Exact broad motile-cilium class allows variable axonemal arrangements;
    Chlamydomonas9+2 remains an example, not its universal definition. Axoneme, membrane,
    basal body, TZ and associated IFT identities are appropriate. Individual component
    essentiality is assessed separately.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-go
  - micro-pazour2005
  - micro-nicastro-browser
- assessment_id: micro-motile-examples
  area: grounding
  topic: Five exact IFT examples and location attribution
  outcome: supported
  summary: The four reviewed entries and one unreviewed IFT88 match native labels/tokens/taxon.
    Four reviewed exact-gene matches are unique within the bounded query; IFT88 reviewed
    search is empty. IFT172/IFT46 experimental annotation citations are location-specific;
    IFT81/IFT74/IFT88 are identity-only. No sixth IFT52 example or complete protein
    inventory is forced.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-protein-policy
  - micro-tax3055
  - micro-ift-reviewed-search
  - micro-ift88-reviewed-search
  - micro-uniprot-Q5DM57
  - micro-uniprot-Q68RJ5
  - micro-uniprot-Q6RCE1
  - micro-uniprot-A2T2X4
  - micro-uniprot-Q9FPW0
  - micro-cole1998
  - micro-hou2007
  - micro-ahmed2008
- assessment_id: micro-motile-essentiality
  area: evidence
  topic: Assembly necessity remains independently unverified
  outcome: unknown
  summary: Canonical anatomy, proteomic presence and localization do not independently
    establish every ESSENTIAL broad-component assembly-necessity claim. No suitable
    depletion/reconstitution experiment for each entire regional component was checked;
    the enum is not redefined as activity or viability.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-schema-policy
  - micro-record-motile
  - micro-pazour2005
  - micro-cole1998
  - micro-nicastro-browser
- assessment_id: micro-motile-function
  area: evidence
  topic: Assembly, movement and model-system scope
  outcome: supported
  summary: Chlamydomonas IFT transport and isolated-axoneme architecture support assembly/maintenance
    and dynein-based movement at their stated scope. Purified WT/mutant fractions
    are distinguished; broad cross-protist conservation wording is not treated as
    a fully audited three-species molecular comparison. Silflow body remains unverified.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-pazour2005
  - micro-cole1998
  - micro-hou2007
  - micro-rosenbaum2002
  - micro-nicastro-browser
  - micro-ift-bibliography
  - micro-silflow-access
- assessment_id: micro-motile-part-scope
  area: scope
  topic: Accessory part is not a class-wide obligatory constituent
  outcome: concern
  summary: Mastigoneme is limited to some algae, while unqualified has_part and graph
    membership are broader. A native inverse part_of child display does not imply
    universal has_part.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-go
  - micro-mastigoneme-context
- assessment_id: micro-motile-graph
  area: graph
  topic: Static membership and whole-cilium self-assembly
  outcome: concern
  summary: The nine nodes and eight edges provide parthood, association and generic
    outputs. The whole assembled cilium mediates its own assembly; no actor-to-event
    causal pathway makes this a MECHANISTIC graph. IFT/motor primary evidence exists
    but is not encoded by those static edges.
  target_ids:
  - GO:0031514
  evidence_ids:
  - micro-record-motile
  - micro-graph-policy
  - micro-schema-policy
  - micro-cole1998
  - micro-hou2007
  - micro-nicastro-browser
  - micro-rosenbaum2002
- assessment_id: micro-base-identity
  area: identity
  topic: Base is broader than TZ
  outcome: supported
  summary: GO identity, SUBCELLULAR_REGION kind, parent, cilium parthood and four
    exact synonyms match. GO0097537 correctly identifies the assembled Y-link; generic
    TZ segment and heterogeneous network need not be forced into whole-axoneme or
    one-family identity.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-go
  - micro-craige2010
  - micro-wang2022
- assessment_id: micro-base-proteins
  area: grounding
  topic: Exact unreviewed ORF examples with published symbol bridges
  outcome: supported
  summary: Both entries retain correct unreviewed status, native labels and CHLRE
    ORFs. NCBI maps these to Cre loci; visually checked Fauser Fig4d maps them to
    CEP290 and NPHP4. The bounded reviewed-symbol search is empty. Automatic location/name
    annotations are not experimental localization.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-protein-policy
  - micro-uniprot-A0A2K3DWT6
  - micro-uniprot-A0A2K3D4W1
  - micro-gene-5728998
  - micro-gene-5718574
  - micro-fauser2022
  - micro-base-reviewed-search
  - micro-tax3055
- assessment_id: micro-base-gate-evidence
  area: evidence
  topic: TZ link architecture and composition regulation
  outcome: supported
  summary: Primary mutant/rescue/localization and composition comparisons support
    membrane tethering and protein-sorting roles at Chlamydomonas TZ. Wedge defects,
    Y-link loss, 9+2 architecture and ectosome endpoints are distinct. Independent
    localization is not proof of a complete interaction hierarchy.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-craige2010
  - micro-wang2022
  - micro-base-bibliography
- assessment_id: micro-base-completeness
  area: completeness
  topic: Known distal basal-body and transition-fiber regions
  outcome: concern
  summary: The exact base encompasses three regions, but all current component rows
    and constituent graph nodes describe TZ. Diener isolated TZs exclude transition
    fibers and lost some in-situ structures; this cannot fill the known non-TZ region
    gap or certify a full-base proteome.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-go
  - micro-diener2015
  - micro-base-bibliography
- assessment_id: micro-base-graph
  area: graph
  topic: Static base membership and gate output
  outcome: concern
  summary: Three regional membership edges, base-to-cilium parthood and base-to-gating
    output provide no mechanistic intermediate despite MECHANISTIC status. Source-backed
    tethering/sorting mechanisms could inform later curation but have not been encoded.
  target_ids:
  - GO:0097546
  evidence_ids:
  - micro-record-base
  - micro-graph-policy
  - micro-schema-policy
  - micro-craige2010
  - micro-wang2022
- assessment_id: micro-probasal-identity
  area: identity
  topic: Immature precursor and maturation
  outcome: supported
  summary: GO0120280, parent and scoped synonyms denote the immature partially assembled
    body; matures-into mature basal body is appropriate. Chlamydomonas interphase
    has mature and pro-basal pairs, with earliest singlet stages preceding completed
    triplets.
  target_ids:
  - GO:0120280
  evidence_ids:
  - micro-record-probasal
  - micro-go
  - micro-dutcher2016
  - micro-wingfield2018
  - micro-matsuura2004
- assessment_id: micro-probasal-composition
  area: grounding
  topic: Structural components and perturbation limits
  outcome: supported
  summary: 'Whole triplet-blade and cartwheel structural classes are not generic single
    microtubules or individual SAS6/Bld10 proteins. UNKNOWN assembly essentiality
    is appropriate: uni3-1 proximal doublets do not equal complete triplet absence,
    and bld12 central-part loss does not equal deletion of every cartwheel element.
    No exact family or accession is invented for these assemblies.'
  target_ids:
  - GO:0120280
  evidence_ids:
  - micro-record-probasal
  - micro-go
  - micro-matsuura2004
  - micro-dutcher1998-abstract
  - micro-nakazawa2007-abstract
  - micro-schema-policy
- assessment_id: micro-probasal-stage
  area: evidence
  topic: Direct cilium nucleation assigned to immature stage
  outcome: concern
  summary: The definition says the pro-basal body cannot nucleate a cilium, but direct
    function/edge cites the mature-body definition and assigns anchoring/nucleation
    to the immature target. Its occurrence note describes only the mature flagellated
    pair. Route the direct output through maturity and state the immature pair explicitly.
  target_ids:
  - GO:0120280
  evidence_ids:
  - micro-record-probasal
  - micro-go
  - micro-dutcher2016
  - micro-wingfield2018
- assessment_id: micro-probasal-bld10
  area: evidence
  topic: Cartwheel hub versus spoke tip
  outcome: concern
  summary: Definition combines SAS6 and Bld10 in a hub, whereas its own component
    note distinguishes them. Matsuura localizes Bld10 to cartwheel fibers; Hiraki
    primary abstract identifies a spoke-tip component, and Nakazawa locates SAS6 centrally.
    Correct wording at the demonstrated Chlamydomonas scope.
  target_ids:
  - GO:0120280
  evidence_ids:
  - micro-record-probasal
  - micro-matsuura2004
  - micro-hiraki2007-abstract
  - micro-nakazawa2007-abstract
  - micro-wingfield2018
- assessment_id: micro-optional-coverage
  area: completeness
  topic: Actual fields and source tiers
  outcome: supported
  summary: All four current records and their original reviews were inspected. No
    target carries image assets, quantitative measurements or verbatim snippets; none
    are invented as mandatory fixes. Review literature, abstracts, body passages,
    source metadata and plotted labels retain separate access claims.
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0031514
  - GO:0120280
  evidence_ids:
  - micro-record-nine-two
  - micro-record-base
  - micro-record-motile
  - micro-record-probasal
  - micro-review-policy
  - micro-original-validation
- assessment_id: septin-S2352-A1
  area: identity
  topic: Exact structure and hierarchy
  outcome: supported
  target_ids:
  - GO:0097609
  summary: GO identity, exact synonym and 9+2-cilium is_a relation match the native
    terms. This is a specialized eukaryotic cilium, distinct from the sulcus and transverse
    flagellum.
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-record-longitudinal_flagellum
- assessment_id: septin-S2352-A2
  area: scope
  topic: Qualitative dinoflagellate distribution
  outcome: supported
  target_ids:
  - GO:0097609
  summary: VARIABLE Dinophyceae is an appropriately nonuniversal distribution. The
    new primary example is one free-living strain; it does not establish every symbiotic
    species or cell stage.
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-tax-2864
  - septin-s2352-longitudinal-prep-maruyama2023-html-native
  - septin-s2352-record-longitudinal_flagellum
- assessment_id: septin-S2352-A3
  area: evidence
  topic: Partial sulcus occupancy and planar motion
  outcome: concern
  target_ids:
  - GO:0097609
  summary: The native definition and primary observations support emergence through
    the sulcus. Maruyama2023 directly reports planar beating in Akashiwo, while Cachon1991
    describes nonplanar three-dimensional waves in the studied Ceratium/Oxyrrhis.
    The class-level planar statement needs qualification; these source/context differences
    must not be silently harmonized.
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-maruyama2023-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-record-longitudinal_flagellum
- assessment_id: septin-S2352-A4
  area: graph
  topic: Spatial relation versus assembly mechanism
  outcome: concern
  target_ids:
  - GO:0097609
  summary: The sole edge describes location and is backed by metadata-only Taylor
    evidence. It does not explain assembly or a causal mechanism. Its unqualified
    lies-within wording also loses the native often/partial scope.
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-taylor1980-api
  - septin-s2352-record-longitudinal_flagellum
  - septin-s2352-graph-policy
- assessment_id: septin-S2352-A5
  area: provenance
  topic: Wrong current GO definition-xref attribution
  outcome: concern
  target_ids:
  - GO:0097609
  summary: The record says Taylor1980 is cited by GO0097612. Current native GO instead
    attaches that PMID to cingulum GO0097611; sulcus GO0097612 cites PMID20561119.
    The Taylor paper itself is correctly identified.
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-sulcus-citation-meta
  - septin-s2352-record-longitudinal_flagellum
- assessment_id: septin-S2352-A6
  area: completeness
  topic: Optional inventory and mechanism boundaries
  outcome: supported
  target_ids:
  - GO:0097609
  summary: A short specialized-cilium record need not duplicate every axonemal protein
    or acquire optional images/properties. The retrieved primary paper supplies a
    concrete future example, but retraction mechanism and biological purpose remain
    unresolved rather than required invented graph edges.
  evidence_ids:
  - septin-s2352-longitudinal-prep-maruyama2023-html-native
  - septin-s2352-record-longitudinal_flagellum
  - septin-s2352-policy
- assessment_id: septin-S2352-A7
  area: identity
  topic: Exact structure, name and synonym
  outcome: supported
  target_ids:
  - GO:0097608
  summary: The GO identity denotes the intended dinoflagellate transverse motile cilium,
    and the exact synonym/category/kind are appropriate. The original GO wording is
    supported; extra causal detail requires its own attribution and scope.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-leadbeater-nature-preview
  - septin-s2352-record-transverse_flagellum
- assessment_id: septin-S2352-A8
  area: scope
  topic: Is-a parent versus spatial containment
  outcome: supported
  target_ids:
  - GO:0097608
  summary: The direct9+2 motile-cilium parent is native is_a, not parthood. Cingulum
    is a cell-surface furrow and spatial host, not an is-a parent of the flagellum.
    Both graph node identities are nonlocal GO terms and resolve without relying on
    neighboring maintained records.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-record-transverse_flagellum
- assessment_id: septin-S2352-A9
  area: scope
  topic: Dinophyceae variable presence and source species
  outcome: supported
  target_ids:
  - GO:0097608
  summary: Taxon2864 and the conditional variable-presence treatment are supported.
    Direct primary specimens are A.sanguinea NIES-4631 and the specified Ceratium/Oxyrrhis
    material; they do not establish every dinoflagellate configuration, cell state
    or swimming behavior. The taxon note correctly assigns Taylor to GO0097611.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-longitudinal-prep-tax-2864
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-record-transverse_flagellum
- assessment_id: septin-S2352-A10
  area: provenance
  topic: Expanded definition exceeds its stated source
  outcome: concern
  target_ids:
  - GO:0097608
  summary: The appended cingulum clause is unqualified after GO says often, and the
    striated-strand/waveform explanation is attached to a GO-only definition_source.
    Primary text supports scoped morphology and contraction, while retaining hypotheses
    about coiling, force transmission and regulation. This requires attribution/qualification,
    not a claim that the axoneme or strand is absent.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-leadbeater-nature-preview
  - septin-s2352-leadbeater-micro-abstract
  - septin-s2352-record-transverse_flagellum
- assessment_id: septin-S2352-A11
  area: graph
  topic: Spatial relation mislabeled as assembly mechanism
  outcome: concern
  target_ids:
  - GO:0097608
  summary: The only edge states lies within. It has no assembly process or causal
    chain, despite ASSEMBLY/MECHANISTIC labels. Taylor evidence on this edge expressly
    says only metadata were available. Native GO and the Akashiwo observations support
    bounded spatial context; neither the cited metadata nor location alone establishes
    a mechanistic assembly graph.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-taylor1980-api
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-record-transverse_flagellum
  - septin-s2352-graph-schema
- assessment_id: septin-S2352-A12
  area: scope
  topic: Broad thrust and rotation versus detailed allocation
  outcome: unknown
  target_ids:
  - GO:0097608
  summary: GO supports forward-thrust function, and primary studies support transverse
    motion and rotation in studied taxa. The1991 interpretation differs from the2004
    numerical-model and2025 abstract-level thrust/steering assignments. Preserve taxon,
    mode and source tier; do not infer a universal force partition, direction of rotation,
    or striated-strand-driven beating cycle from this record.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-cachon-indexed
  - septin-s2352-transverse-agent-epmc-native
  - septin-s2352-transverse-agent-schuech2025-dtu-native
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-record-transverse_flagellum
- assessment_id: septin-S2352-A13
  area: evidence
  topic: Observed contraction versus proposed molecular explanation
  outcome: supported
  target_ids:
  - GO:0097608
  summary: Maruyama2024 distinguishes observed contractions/TEM morphology from proposed
    calcium switching and unobserved force-transmission/attachment structures. Its
    non-detergent Mg2+ result includes a membrane-permeability caveat. Cited Peridinium
    ATP-independent contraction and centrin attribution are prior-study context, not
    independent experiments performed in Akashiwo; no protein identity is inferred.
  evidence_ids:
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-record-transverse_flagellum
- assessment_id: septin-S2352-A14
  area: provenance
  topic: Primary bodies, abstracts, native ontology and failures
  outcome: supported
  target_ids:
  - GO:0097608
  summary: Current Maruyama2024 native HTML and freshly indexed Cachon1991 PDF were
    read at the stated claim-bearing passages. Taylor remains review metadata/abstract
    plus coredata. Leadbeater1967 sources are browser abstract/preview; Miyasaka2004
    is a native Europe PMC abstract; Schuech2025 is an institutional primary abstract.
    No recovered native body is claimed for those access-limited sources. Fresh receipts
    retain actual access timestamps; original historical receipts are not restamped.
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-taylor1980-api
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-transverse-agent-epmc-native
  - septin-s2352-transverse-agent-schuech2025-dtu-native
  - septin-s2352-leadbeater-nature-preview
  - septin-s2352-leadbeater-micro-abstract
- assessment_id: septin-S2352-A15
  area: completeness
  topic: Bounded follow-up without forced optional inventories
  outcome: supported
  target_ids:
  - GO:0097608
  summary: The concrete tasks concern existing definition and graph assertions. Empty
    components/functions/examples/images/properties are not automatic findings. Further
    taxon-specific composition and molecular-mechanism work can be useful, but no
    unverified family/protein identifier or replacement structure is proposed. Historical
    metadata-access notes and PROPOSED status remain intact.
  evidence_ids:
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-record-transverse_flagellum
  - septin-s2352-policy
- assessment_id: septin-S2352-A16
  area: identity
  topic: Array versus constituent filament
  outcome: supported
  target_ids:
  - GO:0005818
  summary: The exact GO identity and maintained hierarchy distinguish the aster array
    from individual astral microtubules. Native GO supports the declared spindle context.
    HAA is an aster subclass and its meiotic study is a legitimate specialized example,
    not an exact synonym for all asters.
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
- assessment_id: septin-S2352-A17
  area: grounding
  topic: Exact tubulin classes and concrete identities
  outcome: supported
  target_ids:
  - GO:0005818
  summary: Alpha/beta tubulin are supported polymer constituents; IPR002452/002453
    are exact family-level identities. P04689/tub1 with atb2/alp2 aliases, P04688/nda2
    and P05219/nda3 are correct reviewed strain284812 proteins. Direct mCherry-Atb2
    observation supports the alpha-tubulin example; the other entries explicitly provide
    identity rather than an isoform census.
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-IPR002452
  - septin-s2352-aster-agent-IPR002453
  - septin-s2352-aster-agent-P04689
  - septin-s2352-aster-agent-P04688
  - septin-s2352-aster-agent-P05219
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
- assessment_id: septin-S2352-A18
  area: scope
  topic: Meiotic source preparation is kept separate from reference stock
  outcome: supported
  target_ids:
  - GO:0005818
  summary: KT2901 is the homothallic fluorescent Figure4A strain; pat1 mat-Pc diploids
    provide separate synchronized ultrastructure. The canonical example correctly
    keeps these preparations distinct and does not identify them with the UniProt
    reference strain.
  evidence_ids:
  - septin-s2352-aster-agent-tax-4896
  - septin-s2352-aster-agent-tax-284812
  - septin-s2352-aster-agent-paper
  - septin-s2352-aster-agent-supplement
  - septin-s2352-record-aster
- assessment_id: septin-S2352-A19
  area: evidence
  topic: Supported specialized meiotic function
  outcome: supported
  target_ids:
  - GO:0005818
  summary: GO0030989/0032117 and the Tanaka2005 abstract support dynein-driven meiotic
    nuclear oscillation associated with the astral array. Funaya2012 supports Hrs1-dependent
    organization and the transition to meiosis I. This does not imply that every aster/astral
    microtubule performs horsetail movement or directly demonstrate chromosome-pairing/recombination
    effects.
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
- assessment_id: septin-S2352-A20
  area: scope
  topic: Broad capture machinery exceeds the cited taxon and cell-cycle evidence
  outcome: concern
  target_ids:
  - GO:0005818
  summary: The appended definition applies Kar9/Bim1 capture machinery and cortical
    dynein to a broad yeast/fungal/protist mitotic scope while naming only the GO
    term as definition source. The native definition does not contain this mechanism,
    and the maintained primary studies concern S.pombe meiotic Hrs1/rMTOC organization.
    Taxon-specific support or narrower wording is needed; no claim that these proteins
    are absent from every other taxon is made.
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
- assessment_id: septin-S2352-A21
  area: graph
  topic: Ontology parthood and meiotic phase must not be conflated
  outcome: concern
  target_ids:
  - GO:0005818
  summary: 'Constituent part-of and horsetail-function edges have appropriate support.
    Native GO supports aster part_of spindle, but the corresponding graph edge cites
    Funaya2012, whose wild-type HAA is disassembled/replaced before the meiosis-I
    spindle forms. The cited experiment does not establish the transient HAA as a
    simultaneous integral spindle compartment. The supported topology does not justify
    the MECHANISTIC scope label: no actor-to-event or organization-to-movement transition
    is represented. A nonmechanistic summary is an appropriate bounded alternative;
    atomistic detail is not required.'
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
  - septin-s2352-graph-scope-policy
- assessment_id: septin-S2352-A22
  area: completeness
  topic: No required missing molecular inventory
  outcome: supported
  target_ids:
  - GO:0005818
  summary: The core alpha/beta polymer components and exact families are represented.
    UNKNOWN essentiality avoids inferring isoform assembly necessity from imaging
    or generic polymer composition. Additional organizer/motor proteins, images, dimensions
    and broader taxa require separate evidence and are optional; these are not treated
    as absent-required-field findings.
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-IPR002452
  - septin-s2352-aster-agent-IPR002453
  - septin-s2352-aster-agent-paper
  - septin-s2352-aster-agent-supplement
  - septin-s2352-record-aster
  - septin-s2352-policy
- assessment_id: septin-S2352-A23
  area: identity
  topic: Array versus constituent filament
  outcome: supported
  target_ids:
  - GO:0000235
  summary: The exact GO identity and maintained hierarchy distinguish the astral microtubule
    from its containing aster array. Native GO supports the declared spindle context.
    HAA is an aster subclass and its meiotic study is a legitimate specialized example,
    not an exact synonym for all asters.
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-astral_microtubule
- assessment_id: septin-S2352-A24
  area: grounding
  topic: Exact tubulin classes and concrete identities
  outcome: supported
  target_ids:
  - GO:0000235
  summary: Alpha/beta tubulin are supported polymer constituents; IPR002452/002453
    are exact family-level identities. P04689/tub1 with atb2/alp2 aliases, P04688/nda2
    and P05219/nda3 are correct reviewed strain284812 proteins. Direct mCherry-Atb2
    observation supports the alpha-tubulin example; the other entries explicitly provide
    identity rather than an isoform census.
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-IPR002452
  - septin-s2352-aster-agent-IPR002453
  - septin-s2352-aster-agent-P04689
  - septin-s2352-aster-agent-P04688
  - septin-s2352-aster-agent-P05219
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-astral_microtubule
- assessment_id: septin-S2352-A25
  area: scope
  topic: Meiotic source preparation is kept separate from reference stock
  outcome: supported
  target_ids:
  - GO:0000235
  summary: KT2901 is the homothallic fluorescent Figure4A strain; pat1 mat-Pc diploids
    provide separate synchronized ultrastructure. The canonical example correctly
    keeps these preparations distinct and does not identify them with the UniProt
    reference strain.
  evidence_ids:
  - septin-s2352-aster-agent-tax-4896
  - septin-s2352-aster-agent-tax-284812
  - septin-s2352-aster-agent-paper
  - septin-s2352-aster-agent-supplement
  - septin-s2352-record-astral_microtubule
- assessment_id: septin-S2352-A26
  area: evidence
  topic: Supported specialized meiotic function
  outcome: supported
  target_ids:
  - GO:0000235
  summary: GO0030989/0032117 and the Tanaka2005 abstract support dynein-driven meiotic
    nuclear oscillation associated with the astral array. Funaya2012 supports Hrs1-dependent
    organization and the transition to meiosis I. This does not imply that every aster/astral
    microtubule performs horsetail movement or directly demonstrate chromosome-pairing/recombination
    effects.
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-astral_microtubule
- assessment_id: septin-S2352-A27
  area: scope
  topic: Broad capture machinery exceeds the cited taxon and cell-cycle evidence
  outcome: concern
  target_ids:
  - GO:0000235
  summary: The appended definition applies Kar9/Bim1/EB1/Bik1 capture machinery and
    cortical dynein to a broad yeast/fungal/protist mitotic scope while naming only
    the GO term as definition source. The native definition does not contain this
    mechanism, and the maintained primary studies concern S.pombe meiotic Hrs1/rMTOC
    organization. Taxon-specific support or narrower wording is needed; no claim that
    these proteins are absent from every other taxon is made.
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-astral_microtubule
- assessment_id: septin-S2352-A28
  area: graph
  topic: Constituent contributions versus whole-array language
  outcome: concern
  target_ids:
  - GO:0000235
  summary: 'Tubulin-to-filament, filament-to-array and the specialized horsetail contribution
    are supported. The phrase provides the radial array is read as contribution by
    its constituent microtubules, not equivalence of one filament to the complete
    array. No distinct atomic motor-interface mechanism or universal meiotic function
    is inferred from the MECHANISTIC label. The supported topology does not justify
    the MECHANISTIC scope label: no actor-to-event or organization-to-movement transition
    is represented. A nonmechanistic summary is an appropriate bounded alternative;
    atomistic detail is not required.'
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-paper
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-record-astral_microtubule
  - septin-s2352-graph-scope-policy
- assessment_id: septin-S2352-A29
  area: provenance
  topic: Claimed narrow synonym is not supplied by its cited GO term
  outcome: concern
  target_ids:
  - GO:0000235
  summary: The record assigns cytoplasmic astral microtubule as a NARROW_SYNONYM with
    GO0000235 as source. The current exact native term has no synonyms. This is a
    concrete source-attribution gap, not evidence that the phrase is biologically
    invalid.
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-record-astral_microtubule
- assessment_id: septin-S2352-A30
  area: completeness
  topic: No required missing molecular inventory
  outcome: supported
  target_ids:
  - GO:0000235
  summary: The core alpha/beta polymer components and exact families are represented.
    UNKNOWN essentiality avoids inferring isoform assembly necessity from imaging
    or generic polymer composition. Additional organizer/motor proteins, images, dimensions
    and broader taxa require separate evidence and are optional; these are not treated
    as absent-required-field findings.
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-IPR002452
  - septin-s2352-aster-agent-IPR002453
  - septin-s2352-aster-agent-paper
  - septin-s2352-aster-agent-supplement
  - septin-s2352-record-astral_microtubule
  - septin-s2352-policy
- assessment_id: septin-S2352-A31
  area: grounding
  topic: Refresh changed nda2 input and preserve multi-target lineage
  outcome: supported
  summary: The current alpha_tubulin.gene_symbols list adds nda2 and a history event
    to the originally frozen record. Direct reviewed UniProt P04688 identifies nda2
    (alpha-1 tubulin); P04689 remains tub1/atb2/alp2, and P05219 nda3/alp12. Both
    native checks pass. This corrects the assigned target portion of prior category
    F2, not its unassessed GO0032117/GO1990295 targets. No claim that nda2 was directly
    visualized in the Atb2 experiment or is indispensable for assembly is added.
  target_ids:
  - GO:0005818
  evidence_ids:
  - septin-s2352-record-aster
  - septin-s2352-aster-agent-P04688
  - septin-s2352-aster-agent-P04689
  - septin-s2352-aster-agent-P05219
  - septin-s2352-prior-nda2-finding
  - septin-s2352-aster-native-verify
  - septin-s2352-aster-native-causal
  - septin-s2352-aster-agent-paper
- assessment_id: septin-S2352-A32
  area: evidence
  topic: Structured-source applicability for molecular claims
  outcome: not_applicable
  summary: Named tubulins and capture machinery trigger applicability review. The
    fresh full official catalogue contains no matching fungus/protist dataset, so
    gene/module queries lack a valid dataset and are not performed. Historical runner
    unavailability is disclosed separately; no lack-of-expression-claim exemption
    is used.
  target_ids:
  - GO:0005818
  evidence_ids:
  - septin-s2352-record-aster
  - septin-s2352-policy
  - septin-s2352-current-adapter-catalogue
  - septin-s2352-historical-runner-unavailable
- assessment_id: septin-S2352-A33
  area: grounding
  topic: Refresh changed nda2 input and preserve multi-target lineage
  outcome: supported
  summary: The current alpha_tubulin.gene_symbols list adds nda2 and a history event
    to the originally frozen record. Direct reviewed UniProt P04688 identifies nda2
    (alpha-1 tubulin); P04689 remains tub1/atb2/alp2, and P05219 nda3/alp12. Both
    native checks pass. This corrects the assigned target portion of prior category
    F2, not its unassessed GO0032117/GO1990295 targets. No claim that nda2 was directly
    visualized in the Atb2 experiment or is indispensable for assembly is added.
  target_ids:
  - GO:0000235
  evidence_ids:
  - septin-s2352-record-astral_microtubule
  - septin-s2352-aster-agent-P04688
  - septin-s2352-aster-agent-P04689
  - septin-s2352-aster-agent-P05219
  - septin-s2352-prior-nda2-finding
  - septin-s2352-astral-native-verify
  - septin-s2352-astral-native-causal
  - septin-s2352-aster-agent-paper
- assessment_id: septin-S2352-A34
  area: evidence
  topic: Structured-source applicability for molecular claims
  outcome: not_applicable
  summary: Named tubulins and capture machinery trigger applicability review. The
    fresh full official catalogue contains no matching fungus/protist dataset, so
    gene/module queries lack a valid dataset and are not performed. Historical runner
    unavailability is disclosed separately; no lack-of-expression-claim exemption
    is used.
  target_ids:
  - GO:0000235
  evidence_ids:
  - septin-s2352-record-astral_microtubule
  - septin-s2352-policy
  - septin-s2352-current-adapter-catalogue
  - septin-s2352-historical-runner-unavailable
- assessment_id: septin-S2352-A35
  area: evidence
  topic: Sparse flagellar morphology source applicability
  outcome: not_applicable
  summary: The two maintained flagellar records contain structure/location/waveform
    assertions without gene, locus, UniProt, regulator, pathway, trait or transcriptomic
    targets requiring molecular adapter queries. The transverse original explicitly
    records this scope; longitudinal original generic no-expression wording is not
    used as a molecular exemption. No omitted-adapter finding is invented for these
    sparse records. Optional literature discussion of ungrounded strand identity does
    not create a maintained gene/protein assertion.
  target_ids:
  - GO:0097609
  - GO:0097608
  evidence_ids:
  - septin-s2352-record-longitudinal_flagellum
  - septin-s2352-record-transverse_flagellum
  - septin-s2352-policy
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 3 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0097729
  - GO:0097546
  - GO:0032179
  - GO:0097609
  - GO:0031514
  - GO:0097608
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0120280
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
- finding_id: plaque-germ-F1
  issue_key: germ-tube-static-assembly-graph
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: The graph shows parthood rather than an assembly mechanism
  description: The ASSEMBLY/MECHANISTIC graph contains exactly three is-part-of edges
    and no assembly event or causal intermediate. The cited GO definitions and Douglas
    review support membership/localization, but membership alone does not establish
    how the germ tube forms.
  target_ids:
  - GO:0032179
  field_paths:
  - causal_graphs[graph_id=germ_tube_mechanism].graph_kind
  - causal_graphs[graph_id=germ_tube_mechanism].scope_status
  - causal_graphs[graph_id=germ_tube_mechanism].edges
  evidence_ids:
  - plaque-current-0
  - plaque-graph-contract
  - plaque-germ-tube-agent-go
  - plaque-germ-tube-agent-douglas-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The exact structure and most underlying membership/location
    claims remain supported. The bounded defect is an overbroad scope qualifier or
    mechanistic representation, rather than a demonstrated false experimental mechanism
    or wrong identity; calibrated as minor.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094732Z-germ-tube-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2549
- finding_id: plaque-germ-F2
  issue_key: germ-tube-definition-cap-location-source
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Separate the apical cap from the basal band and source added claims
  description: The definition appends a basal septin collar/cap and a broad mechanistic
    dependence while definition_source remains GO0032179. Native GO and the cited
    review locate the cap at the leading edge; the basal band is a distinct localization.
    Retain the exact definition or attach properly scoped literature support to added
    polarity/vesicle/septin claims. This does not establish that Cdc42 or vesicle
    traffic has no germ-tube role.
  target_ids:
  - GO:0032179
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - plaque-germ-tube-agent-go
  - plaque-germ-tube-agent-douglas-pmc
  - plaque-germ-tube-agent-warenda2002
  - plaque-current-0
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The record retains its exact biological identity; this bounded
    wording, grounding or completeness defect does not invalidate the supported core.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094732Z-germ-tube-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2550
- finding_id: plaque-germ-F3
  issue_key: germ-tube-generic-septin-family-gap
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the generic septin class independently of cap composition
  description: The label-only rationale withholds a family CURIE until a complete
    germ-tube cap cohort is resolved, although the component label and role denote
    generic septin GTPases. Native InterPro IPR016491 exactly represents that protein
    family. Family grounding does not require claiming a complete cap membership list
    or a species-specific stoichiometry.
  target_ids:
  - GO:0032179
  field_paths:
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  evidence_ids:
  - plaque-germ-tube-agent-family
  - plaque-germ-tube-agent-go
  - plaque-current-0
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The record retains its exact biological identity; this bounded
    wording, grounding or completeness defect does not invalidate the supported core.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094732Z-germ-tube-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2499
- finding_id: plaque-arp-F1
  issue_key: arp19-arp18-definition-pairings-reversed
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct the reversed Arc19/ARPC4 and Arc18/ARPC3 pairs
  description: The definition pairs Arc19 with ARPC3 and Arc18 with ARPC4. Native
    P33204 identifies ARC19 as subunit4, while Q05933 identifies ARC18 as subunit3.
    The component labels and protein examples already use the correct pairs. Correct
    the definition without replacing those correct examples.
  target_ids:
  - GO:0005885
  field_paths:
  - definition
  evidence_ids:
  - plaque-arp-agent-P33204
  - plaque-arp-agent-Q05933
  - plaque-current-1
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is an explicit molecular identity error in the defining
    composition, not an optional nomenclature preference.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094741Z-arp2-3-protein-complex-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2551
- finding_id: plaque-arp-F2
  issue_key: arp-subunit-mechanisms-misattributed-to-patch-em
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace unsupported subunit-mechanism attributions to Young2004
  description: Both clamp and peripheral component evidence notes claim that Young2004
    characterizes seven-subunit requirements or defines Arc40/Arc18/Arc15 activation
    coupling. The complete inspected paper instead analyzes isolated cortical actin
    patch networks and sac6/cap1 mutants. Correct these false evidence summaries and
    support any retained detailed subunit roles with an appropriate inspected primary
    structural/biochemical source. Apply the same correction to repeated graph descriptions/evidence;
    independently verify the short-pitch Arp2/Arp3 activation claim rather than treating
    the accessible Kaksonen abstract as its proof.
  target_ids:
  - GO:0005885
  field_paths:
  - components[component_id=arc35_arc19_clamp_subunits].evidence
  - components[component_id=arc40_arc18_arc15_peripheral_subunits].evidence
  - components[*].role
  - causal_graphs[graph_id=arp2_3_protein_complex_mechanism].nodes
  - causal_graphs[graph_id=arp2_3_protein_complex_mechanism].edges
  evidence_ids:
  - plaque-arp-agent-jats-jcb.200404159
  - plaque-arp-agent-galletta2008-plos
  - plaque-arp-agent-kaksonen2003-meta
  - plaque-current-1
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: The primary citations affirm experiments and mechanistic conclusions
    the source did not perform; this affects the core claimed mechanism rather than
    only formatting. It does not prove the proposed biological roles false.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094741Z-arp2-3-protein-complex-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2552
- finding_id: micro-F1
  issue_key: nine-two-cilium-paraflagellar-rod-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Restrict the paraflagellar rod to the cilia that contain it
  description: The record adds GO0097740 as an unqualified has_part and describes
    it as a constituent of the broad 9+2 cilium class. Native GO explicitly limits
    this rod to some flagellated protists. A rod part_of 9+2-cilium assertion displayed
    under GO children does not imply that every 9+2 cilium has that rod. The graph
    repeats the broad membership and cites the access-limited Silflow review. This
    finding concerns the positive universalized representation; it does not deny rod
    membership in trypanosome or other supported subtypes.
  target_ids:
  - GO:0097729
  field_paths:
  - has_part
  - causal_graphs[graph_id=9_2_motile_cilium_mechanism].nodes[node_id=paraflagellar_rod]
  - causal_graphs[graph_id=9_2_motile_cilium_mechanism].edges
  evidence_ids:
  - micro-record-nine-two
  - micro-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/9_2_motile_cilium.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The exact structure and most underlying membership/location
    claims remain supported. The bounded defect is an overbroad scope qualifier or
    mechanistic representation, rather than a demonstrated false experimental mechanism
    or wrong identity; calibrated as minor.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094726Z-9-2-motile-cilium-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2554
- finding_id: micro-F2
  issue_key: nine-two-cilium-static-graph-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Do not label structural membership and outputs as a mechanism
  description: The FUNCTION/MECHANISTIC graph contains only parthood, association
    and whole-structure output edges. Mechanistic phrases in node descriptions do
    not provide a causal path, and the whole cilium is the subject of its own assembly.
    Inspected primary work can support specific motor or transport steps but those
    steps are not represented in the current graph.
  target_ids:
  - GO:0097729
  field_paths:
  - causal_graphs[graph_id=9_2_motile_cilium_mechanism].scope_status
  - causal_graphs[graph_id=9_2_motile_cilium_mechanism].edges
  evidence_ids:
  - micro-record-nine-two
  - micro-graph-policy
  - micro-schema-policy
  - micro-cole1998
  - micro-hou2007
  - micro-nicastro-browser
  - micro-rosenbaum2002
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/9_2_motile_cilium.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The exact structure and most underlying membership/location
    claims remain supported. The bounded defect is an overbroad scope qualifier or
    mechanistic representation, rather than a demonstrated false experimental mechanism
    or wrong identity; calibrated as minor.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094726Z-9-2-motile-cilium-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2555
- finding_id: micro-F3
  issue_key: ciliary-base-graph-static-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the graph as structural context or supply causal steps
  description: The graph is a set of constituent/compartment parthood assertions plus
    a whole-base gating output. It does not explain how a named constituent, interaction
    or perturbation controls that output. Source-backed molecular mechanisms exist
    in the primary papers, but the current edge representation does not encode them.
  target_ids:
  - GO:0097546
  field_paths:
  - causal_graphs[graph_id=ciliary_base_mechanism].scope_status
  - causal_graphs[graph_id=ciliary_base_mechanism].edges
  evidence_ids:
  - micro-record-base
  - micro-graph-policy
  - micro-schema-policy
  - micro-craige2010
  - micro-wang2022
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The exact structure and most underlying membership/location
    claims remain supported. The bounded defect is an overbroad scope qualifier or
    mechanistic representation, rather than a demonstrated false experimental mechanism
    or wrong identity; calibrated as minor.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094729Z-ciliary-base-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2556
- finding_id: micro-F4
  issue_key: ciliary-base-known-non-tz-composition-gap
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent the defining basal-body and transition-fiber regions
  description: The entire component inventory and constituent graph cover only transition-zone
    structures, despite the exact base definition explicitly comprising distal basal
    body, transition fibers and TZ. The cited Diener preparation expressly excludes
    transition fibers from isolated TZs, and the gate review separates those structures.
    This materially narrows the represented composition of the broad base. It does
    not require an exhaustive protein inventory or replace the base identity with
    TZ.
  target_ids:
  - GO:0097546
  field_paths:
  - components
  - causal_graphs[graph_id=ciliary_base_mechanism].nodes
  evidence_ids:
  - micro-record-base
  - micro-go
  - micro-diener2015
  - micro-base-bibliography
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity, Components, Evidence and Causal graph; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The record retains its exact biological identity; this bounded
    wording, grounding or completeness defect does not invalidate the supported core.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094729Z-ciliary-base-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2557
- finding_id: micro-F5
  issue_key: motile-cilium-mastigoneme-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify mastigoneme parthood within the broad motile-cilium class
  description: The unqualified has_part and corresponding graph element make mastigoneme
    appear as a constituent of the entire motile-cilium class, while the native term
    explicitly describes some algal flagella. Preserve the supported conditional algal
    relation and avoid treating an inverse GO part_of lookup as obligatory universal
    composition.
  target_ids:
  - GO:0031514
  field_paths:
  - has_part
  - causal_graphs[graph_id=motile_cilium_mechanism].nodes[node_id=mastigoneme]
  - causal_graphs[graph_id=motile_cilium_mechanism].edges[subject=mastigoneme]
  evidence_ids:
  - micro-record-motile
  - micro-go
  - micro-mastigoneme-context
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094737Z-motile-cilium-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2561
- finding_id: micro-F6
  issue_key: motile-cilium-graph-self-assembly-and-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: The graph labels anatomical summary and product-to-assembly edges as mechanism
  description: Most edges are parthood/association or generic function. The motile_cilium
    mediates cilium_assembly edge uses a source about IFT delivering precursors and
    does not establish the assembled cilium as its own assembly driver. Narrow to
    a NONMECHANISTIC summary or represent source-backed machinery-to-assembly directions.
  target_ids:
  - GO:0031514
  field_paths:
  - causal_graphs[graph_id=motile_cilium_mechanism].scope_status
  - causal_graphs[graph_id=motile_cilium_mechanism].edges[subject=motile_cilium,object=cilium_assembly]
  evidence_ids:
  - micro-record-motile
  - micro-graph-policy
  - micro-schema-policy
  - micro-cole1998
  - micro-rosenbaum2002
  - micro-nicastro-browser
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094737Z-motile-cilium-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2562
- finding_id: micro-F7
  issue_key: probasal-body-mature-cilium-nucleation-conflation
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Assign cilium anchoring and axoneme nucleation to the mature basal body
  description: The function and the graph edge whose subject is ciliary_pro_basal_body
    state that this structure anchors a cilium and forms the base of axonemal assembly,
    using the mature GO0036064 definition as evidence. GO0120280 explicitly says pro-basal
    bodies cannot nucleate a cilium. Retain the supported maturation relation and
    attribute the direct function to the mature node, or expressly describe an indirect
    developmental contribution. The distribution note also describes only the mature
    flagellum-bearing pair and should identify the accompanying pro-basal pair.
  target_ids:
  - GO:0120280
  field_paths:
  - functions[function_id=cilium_assembly]
  - causal_graphs[graph_id=ciliary_pro_basal_body_mechanism].nodes[node_id=cilium_assembly]
  - causal_graphs[graph_id=ciliary_pro_basal_body_mechanism].edges[subject=ciliary_pro_basal_body,predicate=mediates,object=cilium_assembly]
  - taxonomic_distribution[taxon_id=NCBITaxon:3055].note
  evidence_ids:
  - micro-record-probasal
  - micro-go
  - micro-dutcher2016
  - micro-wingfield2018
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: The record assigns an explicitly excluded mature-stage capability
    to an immature structure, changing the developmental identity and causal interpretation.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094748Z-ciliary-pro-basal-body-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2571
- finding_id: micro-F8
  issue_key: probasal-bld10-cartwheel-hub-location
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Separate the SAS6 hub from Bld10 spoke-tip location
  description: The definition compresses the cartwheel into a SAS6/Bld10p hub. The
    inspected review sections place Bld10 at the spoke tips/pinheads, and Matsuura2004
    localizes it on cartwheel fibers; the existing component notes already correctly
    distinguish hub from spoke tip. Describe the whole cartwheel without locating
    both proteins at its hub.
  target_ids:
  - GO:0120280
  field_paths:
  - definition
  evidence_ids:
  - micro-record-probasal
  - micro-matsuura2004
  - micro-hiraki2007-abstract
  - micro-nakazawa2007-abstract
  - micro-wingfield2018
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The whole cartwheel component and target identity are correct;
    this is a bounded spatial wording error within the added definition, not an incorrect
    protein accession or whole-structure mapping.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094748Z-ciliary-pro-basal-body-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2572
- finding_id: septin-S2352-F1
  issue_key: longitudinal-flagellum-spatial-graph-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: The spatial graph is labeled as an assembly mechanism
  description: The graph contains only longitudinal_flagellum lies-within dinoflagellate_sulcus,
    yet declares ASSEMBLY and MECHANISTIC. Its Taylor evidence explicitly describes
    metadata access. Retain a qualified spatial relation as nonmechanistic context,
    or supply a separately evidenced assembly path. Preserve often/partial occupancy
    rather than implying the entire flagellum remains inside the sulcus.
  target_ids:
  - GO:0097609
  field_paths:
  - causal_graphs[graph_id=longitudinal_flagellum_mechanism]
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-taylor1980-api
  - septin-s2352-longitudinal-prep-maruyama2023-html-native
  - septin-s2352-record-longitudinal_flagellum
  - septin-s2352-graph-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094735Z-longitudinal-flagellum-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2558
- finding_id: septin-S2352-F2
  issue_key: longitudinal-flagellum-sulcus-citation-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Taylor1980 is attributed to the wrong current GO term
  description: The top-level PMID/DOI notes identify Taylor1980 as the review cited
    by GO0097612. Native GO currently assigns Taylor to GO0097611, while GO0097612
    cites Iwataki2010 PMID20561119. Correct the source-to-term attribution without
    pretending that either full historical paper was read.
  target_ids:
  - GO:0097609
  field_paths:
  - evidence[reference=PMID:7002229].notes
  - evidence[reference=DOI:10.1016/0303-2647(80)90006-4].notes
  - causal_graphs[graph_id=longitudinal_flagellum_mechanism].edges[0].evidence
  evidence_ids:
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-sulcus-citation-meta
  - septin-s2352-record-longitudinal_flagellum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094735Z-longitudinal-flagellum-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2559
- finding_id: septin-S2352-F3
  issue_key: longitudinal-flagellum-planar-wave-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Scope the planar-wave statement to the observed taxa and conditions
  description: The expanded definition describes longitudinal beating with planar
    waves without a taxon or observation qualifier. Maruyama2023 supports planar Akashiwo
    motion, whereas Cachon1991 describes three-dimensional nonplanar waves for its
    studied Ceratium/Oxyrrhis context. Retain the supported specialized-cilium identity
    while scoping waveform statements and recording the differing observations rather
    than implying one class-wide pattern.
  target_ids:
  - GO:0097609
  field_paths:
  - definition
  evidence_ids:
  - septin-s2352-longitudinal-prep-maruyama2023-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-longitudinal-prep-go
  - septin-s2352-record-longitudinal_flagellum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Evidence and scope
  native_severity: minor
  normalization_reason: Bounded representation or attribution defect; exact structure
    identity remains supported.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094735Z-longitudinal-flagellum-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2560
- finding_id: septin-S2352-F4
  issue_key: transverse-flagellum-spatial-edge-labeled-mechanistic-assembly
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Spatial containment is presented as an assembly mechanism
  description: The graph has one lies-within relation between transverse flagellum
    and cingulum. It explains neither construction nor a causal mechanism, but is
    classified ASSEMBLY and MECHANISTIC. Its only edge evidence is Taylor1980 metadata,
    which the record itself explicitly limits to bibliographic/access information.
    Preserve supported spatial context with an honest nonmechanistic scope and directly
    supporting evidence, or replace/remove this graph during authorized curation.
    Do not infer mechanism from the source title or metadata.
  target_ids:
  - GO:0097608
  field_paths:
  - causal_graphs[graph_id=transverse_flagellum_mechanism].graph_kind
  - causal_graphs[graph_id=transverse_flagellum_mechanism].scope_status
  - causal_graphs[graph_id=transverse_flagellum_mechanism].edges
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-longitudinal-prep-taylor1980-meta
  - septin-s2352-longitudinal-prep-taylor1980-api
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-record-transverse_flagellum
  - septin-s2352-graph-schema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/transverse_flagellum.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml:GraphKindEnum; review-checklist:Causal
    graph
  native_severity: minor
  normalization_reason: The biological spatial relation is supported in bounded configurations.
    The defect concerns graph classification and direct evidence attribution, with
    no additional unsupported causal proposition represented; it is a bounded minor
    issue consistent with the analogous longitudinal graph.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094739Z-transverse-flagellum-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2563
- finding_id: septin-S2352-F5
  issue_key: transverse-flagellum-definition-addition-source-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Appended waveform explanation needs its own source and scope
  description: The definition appends an unqualified cingulum placement and striated-strand-to-helical-wave
    explanation after the narrower GO text, while definition_source remains GO0097608.
    That native definition says often and does not contain the appended mechanism.
    The inspected primary studies support constituent morphology and condition-specific
    contraction but distinguish direct observations from proposed coiling/regulatory
    explanations. Retain the exact GO definition or explicitly source and qualify
    the additions, including relevant organism/configuration limits. This does not
    establish that the transverse strand or general thrust function is biologically
    false.
  target_ids:
  - GO:0097608
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-s2352-transverse-agent-go-native
  - septin-s2352-transverse-agent-maruyama2024-html-native
  - septin-s2352-cachon-indexed
  - septin-s2352-leadbeater-nature-preview
  - septin-s2352-leadbeater-micro-abstract
  - septin-s2352-record-transverse_flagellum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/transverse_flagellum.yaml
    role: maintained scientific record
  rule_id: review-checklist:Identity and Evidence standard; docs/CURATION.md:Evidence
  native_severity: minor
  normalization_reason: The exact structure remains identified correctly and scoped
    primary support exists for much of the extra morphology; the bounded defect is
    source attribution and over-broad wording, normalized as minor.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094739Z-transverse-flagellum-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2564
- finding_id: septin-S2352-F6
  issue_key: aster-cross-taxon-capture-mechanism-unsourced
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Bound the appended mitotic capture mechanism to supported taxa
  description: The definition extends the native GO identity with Kar9/Bim1 and cortical-dynein
    mitotic positioning across broad yeast/fungal/microbial-eukaryote groups. GO does
    not state this mechanism, and the record primary sources inspect S.pombe meiotic
    Hrs1-dependent arrays and their replacement by a spindle. Add appropriate inspected
    taxon-specific evidence and qualify the mechanism, or remove the unsupported extension.
    The supported meiotic example and native ontology hierarchy should remain.
  target_ids:
  - GO:0005818
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is a consequential unqualified molecular mechanism and
    taxonomic scope claim in the definition, not a demand for a broader literature
    inventory. The finding concerns support and scope rather than asserting that the
    mechanism is false in every listed organism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094744Z-aster-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2565
- finding_id: septin-S2352-F7
  issue_key: aster-spindle-parthood-primary-source-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Use ontology evidence for spindle parthood without treating HAA as a simultaneous
    spindle compartment
  description: 'The aster-to-spindle graph edge describes an integral compartment
    and cites Funaya2012. That experiment instead shows the meiotic radial array disappearing
    as the meiosis-I spindle forms. The generic relation is supported by native GO,
    so this is a citation/context correction: use the ontology for generic parthood
    and preserve the primary study temporal distinction.'
  target_ids:
  - GO:0005818
  field_paths:
  - causal_graphs[graph_id=aster_mechanism].edges[subject=aster,predicate=is part
    of,object=spindle]
  evidence_ids:
  - septin-s2352-aster-agent-go
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-aster
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The ontology relation itself is correct. Only the experiment
    attribution and simultaneous-compartment implication require a bounded, non-blocking
    correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094744Z-aster-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2566
- finding_id: septin-S2352-F8
  issue_key: aster-static-graph-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish a structural/function summary from a represented mechanism
  description: The graph consists of constituent and compartment parthood plus a whole-structure
    function output. These supported relations do not themselves represent how array
    organization or a motor event causes movement, yet the graph is labeled MECHANISTIC.
    Use NONMECHANISTIC for the existing summary or add a directly evidenced causal
    transition. This does not invalidate the underlying topology or demand an atomic
    motor model.
  target_ids:
  - GO:0005818
  field_paths:
  - causal_graphs[graph_id=aster_mechanism].scope_status
  evidence_ids:
  - septin-s2352-record-aster
  - septin-s2352-aster-agent-paper
  - septin-s2352-graph-scope-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-causal-graphs/SKILL.md:Evidence and graph scope
  native_severity: minor
  normalization_reason: The underlying structure, membership and scoped function remain
    supported. This is a bounded classification defect consistent with the analogous
    composition/function-summary graphs in this batch.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094744Z-aster-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2567
- finding_id: septin-S2352-F9
  issue_key: astral-microtubule-cross-taxon-capture-mechanism-unsourced
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Bound the appended mitotic capture mechanism to supported taxa
  description: The definition extends the native GO identity with Kar9/Bim1/EB1/Bik1
    and cortical-dynein mitotic positioning across broad yeast/fungal/microbial-eukaryote
    groups. GO does not state this mechanism, and the record primary sources inspect
    S.pombe meiotic Hrs1-dependent arrays and their replacement by a spindle. Add
    appropriate inspected taxon-specific evidence and qualify the mechanism, or remove
    the unsupported extension. The supported meiotic example and native ontology hierarchy
    should remain.
  target_ids:
  - GO:0000235
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-aster-agent-doi-j.cub.2005.07.058
  - septin-s2352-aster-agent-paper
  - septin-s2352-record-astral_microtubule
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is a consequential unqualified molecular mechanism and
    taxonomic scope claim in the definition, not a demand for a broader literature
    inventory. The finding concerns support and scope rather than asserting that the
    mechanism is false in every listed organism.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094746Z-astral-microtubule-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2568
- finding_id: septin-S2352-F10
  issue_key: astral-microtubule-synonym-not-in-cited-go
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the source attribution for the added narrow synonym
  description: The synonym cytoplasmic astral microtubule is attributed to GO0000235,
    but the native exact term currently has no synonym entries. Retain the phrase
    only with an appropriate source/curator rationale, or remove this unsupported
    GO attribution. This is not a claim that the descriptive phrase is biologically
    wrong.
  target_ids:
  - GO:0000235
  field_paths:
  - synonyms[synonym_text=cytoplasmic astral microtubule]
  evidence_ids:
  - septin-s2352-astral-agent-go
  - septin-s2352-record-astral_microtubule
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The structure identity is correct and the phrase may be reasonable;
    only the asserted authority/source provenance is unverified and inconsistent with
    the checked current term.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094746Z-astral-microtubule-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2569
- finding_id: septin-S2352-F11
  issue_key: astral-microtubule-static-graph-mechanistic-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish a structural/function summary from a represented mechanism
  description: The graph consists of constituent and compartment parthood plus a whole-structure
    function output. These supported relations do not themselves represent how array
    organization or a motor event causes movement, yet the graph is labeled MECHANISTIC.
    Use NONMECHANISTIC for the existing summary or add a directly evidenced causal
    transition. This does not invalidate the underlying topology or demand an atomic
    motor model.
  target_ids:
  - GO:0000235
  field_paths:
  - causal_graphs[graph_id=astral_microtubule_mechanism].scope_status
  evidence_ids:
  - septin-s2352-record-astral_microtubule
  - septin-s2352-aster-agent-paper
  - septin-s2352-graph-scope-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-causal-graphs/SKILL.md:Evidence and graph scope
  native_severity: minor
  normalization_reason: The underlying structure, membership and scoped function remain
    supported. This is a bounded classification defect consistent with the analogous
    composition/function-summary graphs in this batch.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T094746Z-astral-microtubule-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2570
actions:
- action_id: plaque-germ-A1
  finding_ids:
  - plaque-germ-F1
  target_ids:
  - GO:0032179
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
  description: Recast the existing graph as NONMECHANISTIC structural context, remove
    it, or replace it with an organism- and condition-bounded assembly mechanism supported
    by primary experiments.
  acceptance_checks:
  - Do not equate is-part-of with required-for-assembly.
  - Each mechanistic edge must identify a source-supported action and direction.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: plaque-germ-A2
  finding_ids:
  - plaque-germ-F2
  target_ids:
  - GO:0032179
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
  description: Correct the spatial distinction between apical cap, diffuse basal band
    and internal septation ring; remove or source the additional causal clauses with
    their organism and experimental context.
  acceptance_checks:
  - Check every retained added clause against the actual cited passage rather than
    a title.
  - Do not infer absence of the entire septin class from single-member deletion phenotypes.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: plaque-germ-A3
  finding_ids:
  - plaque-germ-F3
  target_ids:
  - GO:0032179
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/germ_tube.yaml
    role: maintained scientific record
  description: Use exact generic septin family grounding for the existing protein
    class and preserve any unresolved cap composition or organism-specific membership
    as a separate limitation.
  acceptance_checks:
  - Verify IPR016491 remains a family named Septin.
  - Do not substitute a single septin paralog or a domain for the generic protein-family
    class.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: plaque-arp-A1
  finding_ids:
  - plaque-arp-F1
  target_ids:
  - GO:0005885
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
  description: During authorized curation, replace the two reversed definition pairings
    with Arc19/ARPC4 and Arc18/ARPC3.
  acceptance_checks:
  - Keep P33204 and Q05933 attached to their current correct genes/components.
  - Check the resulting definition against the native reviewed identity snapshots.
  - Run focused schema and strict-reference validation.
- action_id: plaque-arp-A2
  finding_ids:
  - plaque-arp-F2
  target_ids:
  - GO:0005885
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
  description: During authorized curation, repair source-specific evidence notes and
    source or qualify each detailed molecular role consistently in components and
    graph.
  acceptance_checks:
  - Retain Young2004 for branched patch morphology at its actual experimental scope.
  - Use an inspected structural/biochemical source for subunit contacts and activation
    rearrangements, or remove/qualify unsupported specificity.
  - Keep exact protein identities separate from localization, function and assembly
    necessity.
  - Do not treat ESSENTIAL as a synonym for membership or catalytic contribution.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - GO:0097729
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/9_2_motile_cilium.yaml
    role: maintained scientific record
  description: Remove the unqualified class-wide has_part or represent a taxon-qualified
    subtype/example; qualify or remove the corresponding graph node/edge and attach
    direct rod-specific evidence.
  acceptance_checks:
  - Preserve native GO relation direction and its some-protists qualifier.
  - Check the source organism and represented cilium type before asserting rod membership.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: micro-A2
  finding_ids:
  - micro-F2
  target_ids:
  - GO:0097729
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/9_2_motile_cilium.yaml
    role: maintained scientific record
  description: Retain this as NONMECHANISTIC structural/function context with corrected
    scope, remove it, or replace it with a bounded primary-supported mechanism that
    separates assembly machinery, cargo, motor action and outcome.
  acceptance_checks:
  - Read each directed edge against a claim-bearing passage.
  - Do not use whole-cilium self-assembly or a membership edge as evidence of a mechanism.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: micro-A3
  finding_ids:
  - micro-F3
  target_ids:
  - GO:0097546
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  description: Mark the present graph NONMECHANISTIC, remove it, or build a bounded
    mechanism with actual constituent-to-event-to-outcome edges supported by primary
    experiments.
  acceptance_checks:
  - Separate localization/parthood from effects on tethering and protein composition.
  - Preserve organism, mutant, rescue and preparation boundaries on causal edges.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: micro-A4
  finding_ids:
  - micro-F4
  target_ids:
  - GO:0097546
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/ciliary_base.yaml
    role: maintained scientific record
  description: Add source-backed structural representation of the distal basal-body
    and transition-fiber regions, or explicitly delimit the present component view
    as partial and identify the known missing regions for follow-up. Label-only rows
    can be used where exact scoped identifiers are unresolved.
  acceptance_checks:
  - Preserve the complete GO0097546 boundary while keeping TZ-only experimental preparations
    scoped.
  - Do not ground a distal segment to the complete basal body without a segment qualification
    or infer that isolated TZ proteomics samples transition fibers.
  - After separately authorized curation, use the guarded writer and native history/status
    rules; run focused schema/strict, identifier and evidence checks.
  generator: Maintained structure YAML; derived products only after authorized curation.
- action_id: micro-A5
  finding_ids:
  - micro-F5
  target_ids:
  - GO:0031514
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  description: Represent mastigoneme as a taxon-qualified optional part, or retain
    the one-way parthood on its own record without an unqualified broad-class inverse.
  acceptance_checks:
  - Preserve Chlamydomonas/algal support without generalizing to every motile cilium.
  - Read exact source support and term direction; do not infer inverse class restrictions
    from a child listing.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
- action_id: micro-A6
  finding_ids:
  - micro-F6
  target_ids:
  - GO:0031514
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/motile_cilium.yaml
    role: maintained scientific record
  description: Correct the assembly-edge direction/actor and graph scope to match
    the supported level of explanation.
  acceptance_checks:
  - Distinguish assembled product, constituent regions, transport machinery and assembly
    process.
  - Retain valid structural edges without claiming that parthood itself establishes
    causality.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
- action_id: micro-A7
  finding_ids:
  - micro-F7
  target_ids:
  - GO:0120280
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    role: maintained scientific record
  description: During authorized curation, route direct cilium anchoring/axoneme nucleation
    through the mature_ciliary_basal_body node and make immature occurrence/function
    wording stage-specific.
  acceptance_checks:
  - Keep GO0120280 as the target identity and preserve its inability to nucleate before
    maturation.
  - Retain the supported matures-into edge and distinguish developmental contribution
    from direct nucleation.
  - Use review-supported Chlamydomonas pro-basal-pair wording in the occurrence note.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: micro-A8
  finding_ids:
  - micro-F8
  target_ids:
  - GO:0120280
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    role: maintained scientific record
  description: During authorized curation, describe a SAS6-centered cartwheel with
    Bld10-associated spoke tips, at the source-supported Chlamydomonas scope.
  acceptance_checks:
  - Do not turn cartwheel localization into specific central-hub localization.
  - Keep the existing correct hub/spoke-tip distinction in component grounding notes.
  - Avoid extrapolating the exact molecular arrangement to every named ciliate/flagellate
    without matching evidence.
  - Run focused schema and strict-reference validation.
- action_id: septin-S2352-C1
  finding_ids:
  - septin-S2352-F1
  target_ids:
  - GO:0097609
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
  description: Narrow graph kind, scope, descriptions and edge evidence to the actual
    spatial claim; attach the inspected ontology or appropriate primary passage.
  acceptance_checks:
  - Do not treat bibliography metadata as evidence of an experimental mechanism.
  - Preserve partial, species- and state-dependent sulcus occupancy.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
- action_id: septin-S2352-C2
  finding_ids:
  - septin-S2352-F2
  target_ids:
  - GO:0097609
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
  description: Correct the GO-xref mapping and cite each source only for claims actually
    inspected.
  acceptance_checks:
  - Verify current native term xrefs and exact PMID/DOI identities.
  - Retain the historical access limitation; do not substitute citation identity for
    article support.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
- action_id: septin-S2352-C3
  finding_ids:
  - septin-S2352-F3
  target_ids:
  - GO:0097609
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/longitudinal_flagellum.yaml
    role: maintained scientific record
  description: Qualify the added waveform and propulsion wording with inspected source/taxon/state
    context, or retain only the broader verified ontology definition.
  acceptance_checks:
  - Keep planar Akashiwo and nonplanar Ceratium/Oxyrrhis observations distinct.
  - Do not infer universal symbiotic-species behavior or an exact thrust partition
    from these studies.
  - Apply only in separately authorized curation through the guarded writer and required
    history, rendering and validation gates.
  generator: Maintained scientific YAML; generated pages are derived.
- action_id: septin-S2352-C4
  finding_ids:
  - septin-S2352-F4
  target_ids:
  - GO:0097608
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/transverse_flagellum.yaml
    role: maintained scientific record
  description: During authorized curation, recast the current graph as nonmechanistic
    functional/spatial context with qualifying scope and direct location evidence,
    remove it, or replace it with an independently supported assembly/mechanistic
    graph. Do not retain ASSEMBLY solely because a flagellum lies in a groove.
  acceptance_checks:
  - Read every resulting edge against its actual source passage; metadata-only Taylor
    cannot establish a mechanism.
  - Check graph_kind and scope_status against what the graph actually explains; keep
    cingulum occupancy conditional where required.
  - Run focused schema/strict plus native CURIE/history checks after an authorized
    validated-writer change.
  generator: Maintained YAML via the guarded writer; derived pages only after authorized
    curation.
- action_id: septin-S2352-C5
  finding_ids:
  - septin-S2352-F5
  target_ids:
  - GO:0097608
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/transverse_flagellum.yaml
    role: maintained scientific record
  description: Separate the exact GO definition from any literature-derived elaboration.
    Retain often/typical-configuration qualifiers, cite the actual primary passages
    for morphology or contraction, and identify proposed waveform/regulatory mechanisms
    as proposals.
  acceptance_checks:
  - Compare the retained definition to native GO0097608, including its often qualifier.
  - For each added clause, inspect the primary organism, methods, result and stated
    uncertainty; do not promote prior cited studies or abstract-only models to direct
    universal mechanism.
  - Preserve PROPOSED status and historical access notes; use the native validated
    writer, curation event, repository history and focused validators only when curation
    is separately authorized.
  generator: Maintained structure YAML; no scientific edits in this review.
- action_id: septin-S2352-C6
  finding_ids:
  - septin-S2352-F6
  target_ids:
  - GO:0005818
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
  description: During authorized curation, separate general structural identity from
    taxon- and phase-specific spindle-positioning mechanisms.
  acceptance_checks:
  - Retain the native GO definition and correct hierarchy.
  - Use inspected primary evidence for each retained named capture mechanism and state
    its organism/cell-cycle scope.
  - Preserve the valid S.pombe meiotic HAA example and its distinct Hrs1/rMTOC source
    context.
  - Do not infer universal Kar9/Bim1 machinery from a specialized HAA experiment.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: septin-S2352-C7
  finding_ids:
  - septin-S2352-F7
  target_ids:
  - GO:0005818
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
  description: During authorized curation, attach the appropriate GO support to generic
    spindle parthood and qualify the HAA-specific temporal context.
  acceptance_checks:
  - Do not delete a correct native relation merely because the specialized example
    differs in timing.
  - Do not describe the wild-type meiotic HAA as simultaneous with the meiosis-I spindle
    on Funaya2012 evidence.
  - Validate graph and source references.
- action_id: septin-S2352-C8
  finding_ids:
  - septin-S2352-F8
  target_ids:
  - GO:0005818
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained scientific record
  description: Narrow the graph scope to a nonmechanistic structural/function summary,
    or encode a source-supported causal transition with organism and meiotic context.
  acceptance_checks:
  - Preserve correct ontology nodes and supported membership relations.
  - Check each retained causal edge against an inspected primary passage; a proposed
    future mechanism is not a completed graph.
  - Any scientific edit requires separate curation authorization and the guarded writer,
    append-only history, rendering and native validation.
- action_id: septin-S2352-C9
  finding_ids:
  - septin-S2352-F9
  target_ids:
  - GO:0000235
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  description: During authorized curation, separate general structural identity from
    taxon- and phase-specific spindle-positioning mechanisms.
  acceptance_checks:
  - Retain the native GO definition and correct hierarchy.
  - Use inspected primary evidence for each retained named capture mechanism and state
    its organism/cell-cycle scope.
  - Preserve the valid S.pombe meiotic HAA example and its distinct Hrs1/rMTOC source
    context.
  - Do not infer universal Kar9/Bim1 machinery from a specialized HAA experiment.
  - Run focused schema, strict-reference and causal-graph checks.
- action_id: septin-S2352-C10
  finding_ids:
  - septin-S2352-F10
  target_ids:
  - GO:0000235
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  description: During authorized curation, repair or remove the unsupported GO synonym
    attribution.
  acceptance_checks:
  - Check the exact native term rather than inferring a synonym from a related class.
  - If retaining a curated narrow synonym, provide a source that actually supports
    it.
  - Run focused schema and strict-reference validation.
- action_id: septin-S2352-C11
  finding_ids:
  - septin-S2352-F11
  target_ids:
  - GO:0000235
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained scientific record
  description: Narrow the graph scope to a nonmechanistic structural/function summary,
    or encode a source-supported causal transition with organism and meiotic context.
  acceptance_checks:
  - Preserve correct ontology nodes and supported membership relations.
  - Check each retained causal edge against an inspected primary passage; a proposed
    future mechanism is not a completed graph.
  - Any scientific edit requires separate curation authorization and the guarded writer,
    append-only history, rendering and native validation.
limitations:
- 'Germ tube and Arp2/3 complex independent subreview: Douglas2005 remains secondary
  review evidence; the inspected Candida subsection distinguishes localization patterns.
  Warenda2002 is Candida BWP17-derived primary context, with inspected strains/media,
  microscopy, claim-bearing localization/hyphal-mutant Results and captions. It is
  not a direct three-species Cdc42/Spitzenkörper/polarisome test. No raw image pixels,
  movies or complete septin-class ablation were assessed.'
- 'Germ tube and Arp2/3 complex independent subreview: Young2004 complete main text/captions/TableI
  were freshly read, including purification and negative-stain limitations. No supplementary
  data or raw microscopy reanalysis. Galletta2008 scope is Introduction, first Las17
  Results/Figures1-2 captions, relevant Discussion passages and main Methods; remaining
  regulator-specific Results and videos were not audited.'
- 'Germ tube and Arp2/3 complex independent subreview: Kaksonen2003 and Winter1997
  are freshly checked at metadata/abstract level only; their entire experimental bodies
  were not independently inspected. A source-specific attribution finding is not proof
  that the proposed biological mechanism is false.'
- 'Germ tube and Arp2/3 complex independent subreview: Sagot2006 native HTML was accessible
  this time. Fresh claim-bearing Methods and partial-colocalization Results/Figure3
  caption replace dependence on the older indexed excerpt for this observation. Other
  body sections, complete supplementary tables and raw images were not audited; the
  original earlier access limitation remains historical.'
- 'Germ tube and Arp2/3 complex independent subreview: All seven exact Arp protein
  queries return the expected reviewed reference-strain entry. UniProt FUNCTION annotations
  often carry similarity evidence and do not independently validate the detailed mechanistic
  source attribution. The component groups are not asserted to share one whole-group
  InterPro family.'
- 'Germ tube and Arp2/3 complex independent subreview: Assembly necessity remains
  unknown for generic septins and each Arp component group. Named-subunit deletions,
  viability, physical membership and catalytic contribution are different endpoints.
  Generic germ-tube NO_GENE_SYMBOLS is permitted, not a claim of complete concrete-protein
  coverage.'
- 'Germ tube and Arp2/3 complex independent subreview: Current adapter applicability
  uses the fresh complete public catalogue only: no matching fungal/eukaryotic dataset.
  Historical runner unavailability is retained separately by root; no current runner
  invocation or gene/module search on an unrelated organism is claimed. Catalogue
  absence is not biological absence.'
- 'Germ tube and Arp2/3 complex independent subreview: Both prior Arp type findings
  cover additional records beyond this assigned slice. Closed issues2420/2431 and
  current Arp type corrections are historical context only; no terminal multi-target
  disposition is emitted. No record fix is credited to PR2352.'
- 'Germ tube and Arp2/3 complex independent subreview: No neighboring scientific record
  or tracked image was used. Frozen category review pairs, graph/schema/protein policies
  and native script were read within requested scope. Root owns corpus QC, current
  identifier gates, issue mutations and CI.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Nicastro current source is a fresh browser response of author-uploaded
  text with a stated three-week crawl age and no native HTTP status; only displayed
  lines112–215 and figure captions were assessed. Direct HTTP returned403. Original
  historical body/SOM access claims remain historical and are not promoted to fresh
  full-paper access.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Silflow current PMC HTML is PDF-only metadata with no body, and the bibliographic
  response has no abstract. Rosenbaum is secondary publisher Key Points/Abstract only.
  Sloboda and Lucker are primary-abstract/native-annotation checks here, not full-body
  experiments.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Dutcher1998 and Nakazawa2007 current assessment is primary abstract only.
  Dutcher native PMC attempt returned a browser challenge and EuropePMC JATS500; the
  exact Discussion wording was not recovered. Hiraki2007 is also primary abstract
  only. No dimensional/percentage result is newly imported.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Garcia2017 is secondary abstract context here: S3 returned404, PMC HTTP200
  was a browser challenge and EuropePMC JATS500. The original bundle’s successful
  historical body access remains attributed to its original time; this reassessment
  does not claim to reproduce it.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Dutcher2016 and Wingfield2018 are secondary reviews at the listed sections.
  Chlamydomonas developmental evidence is not a complete primary audit of Tetrahymena/Trypanosoma
  molecular details or all eukaryotic assembly pathways.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Assembly-necessity claims for the broad axoneme/membrane/basal-body regions
  in both motile-cilium records remain independently unverified. Supported anatomy
  and function are not a substitute for each assembly endpoint; this scientific unknown
  is not fabricated into an extra issue.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: No raw micrographs, movies, cryo-ET reconstructions or full supplementary
  proteomics were reanalyzed. Fauser Fig4d locus labels and its caption were visually
  inspected on rendered PDF page5; no whole-Fauser-paper or screen-data review is
  claimed.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: The official iModulonDB catalogue was freshly read; the runner receipt
  is explicitly reused from00:49Z and no new runner execution is claimed. Lack of
  matching catalogue taxa only bounds source applicability and gives no biological
  absence result.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: Root runs full local gates and handles GitHub issue deduplication/publication.
  This independent slice ran original-bundle validation/render/hash checks and inspected
  six exact root-produced UniProt receipts/logs; it does not relabel original corpus
  totals as current QC.'
- '9+2 motile cilium, ciliary base, motile cilium and ciliary pro-basal body independent
  subreview: The mastigoneme neighbor was frozen before reading and used only as local
  modeling context. Its scientific contents are not counted as a fifth reviewed target.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Independent current subreview is read-only. Original reviews retain historical source-access
  and check receipts; those historical claims are not presented as current actions.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Taylor1980 was checked through native metadata/abstract and publisher coredata only.
  Iwataki2010 was checked at primary abstract/metadata tier for current GO citation
  attribution. Neither full historical body was inspected.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Maruyama2023/2024 were inspected at the stated native primary body/caption passages
  for A. sanguinea NIES-4631 and its experimental conditions. No raw videos, figure
  pixels or complete supplement reanalysis; proposed molecular coupling and biological
  explanations remain hypotheses.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Cachon1991 native PDF retrieval timed out; fresh browser-indexed paper passages
  were inspected. Organism/preparation differences from Maruyama remain unresolved
  variables. Leadbeater1967 is publisher abstract/preview; native Nature200 was authorization
  HTML, and Microbiology native403. Miyasaka2004 and Schuech2025 remain primary abstract
  tier, not full-body experiments audited.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Funaya2012 fresh native JATS claim-bearing body, Figure4 caption and specified supplemental
  strain/methods text were inspected, not every paragraph, figure pixel, movie or
  raw tomography dataset. Tanaka2005 remains primary abstract/metadata tier. No full-paper
  access is inferred from citation identity.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  No systematic cross-fungal/protist Kar9/Bim1/EB1/Bik1 homology or mechanism survey
  was performed. Findings concern unsupported current attribution/scope, not universal
  absence. Tubulin IDs and mCherry-Atb2 imaging do not prove an isoform occupancy
  census or necessity.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Historical category F2/#2421 covers four targets. This review verifies its already-corrected
  nda2 content only for aster and astral microtubule, and does not terminal-resolve
  the entire multi-target finding or inspect the two other targets.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Official dataset catalogue coverage is bounded to the current returned20 organisms/28datasets.
  No matching eukaryotic dataset means no applicable downstream gene/module query
  here, not biological absence. Historical runner failure is not a new failed execution.'
- 'Longitudinal/transverse flagella, aster and astral microtubule independent subreview:
  Full QC/CI and GitHub issue deduplication are root-owned; this report includes independently
  inspected original validation/render checks and four root-run focused native protein
  receipts only.'
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
  Every inherited finding is reassessed against current sources and retains its exact
  predecessor identity.
- 'Bundle issues #2548 (three stale reviews) and #2553 (eight structured-source coverage
  defects) are addressed here. Scientific curation findings remain separately tracked;
  generic Septin family grounding reuses #2499 with germ tube explicitly added. Existing
  validator #2514 remains open.'
- 'Prior record corrections are associated with already-closed #2420, #2421 and #2431.
  Their multi-target category findings are not terminally superseded by this partial
  cohort; only the current target-specific changes are assessed.'
- Source commit 9a8a31291456921b6e1984a3a95f110c763c5174 is retained by tag review-base/pr2352-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native review configuration,
  graph/protein policies, the verifier source, two prior category-review pairs and
  the mastigoneme neighbor.
- Seven original bundles omit structured-source applicability, while motile cilium
  contains an unsupported exemption rationale based on the lack of expression/module
  claims. Sparse longitudinal and transverse flagellar morphology is excluded from
  this defect.
- Historical source-access failures are not promoted to current failures where fresh
  body access succeeded. Secondary reviews, primary Methods/Results, abstracts, figure
  captions and any directly inspected image pixels retain distinct evidence scopes.
- 'The 24 scientific finding keys are linked to #2499, #2549–#2552 and #2554–#2572.
  These record-curation issues remain open; #2499 was reused with an explicit germ-tube
  scope comment after body/comment deduplication.'
- 'Local validation rejected four assessment area values in an uncommitted draft.
  Issue #2573 tracks the correction to the native schema area without substantive
  changes; the corrected successor is revalidated and independently re-reviewed.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094726Z-9-2-motile-cilium-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094729Z-ciliary-base-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094732Z-germ-tube-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094735Z-longitudinal-flagellum-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094737Z-motile-cilium-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094739Z-transverse-flagellum-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094741Z-arp2-3-protein-complex-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094744Z-aster-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094746Z-astral-microtubule-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T094748Z-ciliary-pro-basal-body-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2352
- https://github.com/CultureBotAI/CellStructureMech/issues/2420
- https://github.com/CultureBotAI/CellStructureMech/issues/2421
- https://github.com/CultureBotAI/CellStructureMech/issues/2431
- https://github.com/CultureBotAI/CellStructureMech/issues/2499
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2548
- https://github.com/CultureBotAI/CellStructureMech/issues/2549
- https://github.com/CultureBotAI/CellStructureMech/issues/2550
- https://github.com/CultureBotAI/CellStructureMech/issues/2551
- https://github.com/CultureBotAI/CellStructureMech/issues/2552
- https://github.com/CultureBotAI/CellStructureMech/issues/2553
- https://github.com/CultureBotAI/CellStructureMech/issues/2554
- https://github.com/CultureBotAI/CellStructureMech/issues/2555
- https://github.com/CultureBotAI/CellStructureMech/issues/2556
- https://github.com/CultureBotAI/CellStructureMech/issues/2557
- https://github.com/CultureBotAI/CellStructureMech/issues/2558
- https://github.com/CultureBotAI/CellStructureMech/issues/2559
- https://github.com/CultureBotAI/CellStructureMech/issues/2560
- https://github.com/CultureBotAI/CellStructureMech/issues/2561
- https://github.com/CultureBotAI/CellStructureMech/issues/2562
- https://github.com/CultureBotAI/CellStructureMech/issues/2563
- https://github.com/CultureBotAI/CellStructureMech/issues/2564
- https://github.com/CultureBotAI/CellStructureMech/issues/2565
- https://github.com/CultureBotAI/CellStructureMech/issues/2566
- https://github.com/CultureBotAI/CellStructureMech/issues/2567
- https://github.com/CultureBotAI/CellStructureMech/issues/2568
- https://github.com/CultureBotAI/CellStructureMech/issues/2569
- https://github.com/CultureBotAI/CellStructureMech/issues/2570
- https://github.com/CultureBotAI/CellStructureMech/issues/2571
- https://github.com/CultureBotAI/CellStructureMech/issues/2572
- https://github.com/CultureBotAI/CellStructureMech/issues/2573
```
